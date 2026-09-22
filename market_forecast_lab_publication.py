"""Stage complete official generations, then publish with one Linux directory rename.

Runtime files live in Git's private directory on the provenance volume. No pointer
symlinks: reports/ remains ordinary files covered by the publisher's git add.
"""
from contextlib import contextmanager
import ctypes
import fcntl
import hashlib
import os
from pathlib import Path
import shutil
import subprocess
import tempfile

from market_forecast_lab_run import initialize_scope, read_official_latest, read_history, HISTORIES


def runtime_root(code_root, destination):
    result = subprocess.run(['git', '-c', f'safe.directory={code_root}', '-C', str(code_root),
                             'rev-parse', '--git-common-dir'], capture_output=True, text=True, check=True)
    git_dir = (Path(code_root) / result.stdout.strip()).resolve()
    root = git_dir / 'market-forecast-lab-runtime' / hashlib.sha256(str(destination).encode()).hexdigest()[:20]
    root.mkdir(parents=True, exist_ok=True)
    if root.stat().st_dev != destination.parent.stat().st_dev:
        raise ValueError('ATOMIC_PUBLICATION_REQUIRES_SAME_VOLUME')
    return root


def exchange_directories(staged, destination):
    """Fail closed if atomic exchange is unavailable; never emulate with two moves."""
    libc = ctypes.CDLL(None, use_errno=True)
    renameat2 = libc.renameat2
    renameat2.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_int, ctypes.c_char_p, ctypes.c_uint]
    renameat2.restype = ctypes.c_int
    if renameat2(-100, os.fsencode(staged), -100, os.fsencode(destination), 2):
        errno = ctypes.get_errno()
        raise OSError(errno, os.strerror(errno))


def sync_tree(root):
    for path in sorted(root.rglob('*'), reverse=True) + [root]:
        if path.is_file() or path.is_dir():
            fd = os.open(path, os.O_RDONLY)
            try:
                os.fsync(fd)
            finally:
                os.close(fd)


@contextmanager
def official_transaction(destination, runtime, ctx):
    destination, runtime = Path(destination), Path(runtime)
    runtime.mkdir(parents=True, exist_ok=True)
    with (runtime / 'publication.lock').open('a') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        # Validate before copying: do not follow aliases into protected artifacts.
        if destination.exists():
            if destination.is_symlink():
                raise ValueError('ALIASED_OUTPUT_REJECTED')
            initialize_scope(destination, ctx)
        with tempfile.TemporaryDirectory(prefix='generation-', dir=runtime) as temp:
            staged = Path(temp) / 'market_forecast_lab'
            if destination.exists():
                shutil.copytree(destination, staged)
            initialize_scope(staged, ctx)
            yield staged
            latest = read_official_latest(staged / 'latest.json')
            if latest is None or not latest['run']['universe_complete']:
                raise ValueError('INCOMPLETE_OFFICIAL_GENERATION')
            for name in HISTORIES:
                read_history(staged, name, ctx)
                previous = destination / name
                if previous.exists() and not (staged / name).read_bytes().startswith(previous.read_bytes()):
                    raise ValueError('OFFICIAL_HISTORY_NOT_APPEND_ONLY:' + name)
            for forecast in latest['forecasts']:
                checksum = forecast['input_manifest_id'].removeprefix('sha256:')
                if len(checksum) != 64 or any(c not in '0123456789abcdef' for c in checksum):
                    raise ValueError('INVALID_INPUT_MANIFEST_ID')
                if hashlib.sha256((staged / 'inputs' / (checksum + '.json')).read_bytes()).hexdigest() != checksum:
                    raise ValueError('INPUT_MANIFEST_HASH_MISMATCH')
            # Runtime-only files cannot enter git add reports/.
            for name in ('.run.lock', '.yfinance-cache'):
                if (staged / name).is_dir():
                    shutil.rmtree(staged / name)
                else:
                    (staged / name).unlink(missing_ok=True)
            sync_tree(staged)
            if destination.exists():
                exchange_directories(staged, destination)
            else:
                os.rename(staged, destination)
            # The commit point is the rename: all histories/latest are now one generation.
            # Cleanup only removes the old generation under the private runtime directory.
