"""Explicit run identity and fail-closed publication/storage boundaries for the Lab."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import uuid

import forecast_provenance as fp

MODES = ('TRIAL', 'OFFICIAL_DAILY', 'REPLAY')
CONTEXT_FIELDS = ('run_mode', 'run_id', 'generated_at_utc', 'code_version', 'official_daily')
HISTORIES = ('universe_history.jsonl', 'forecast_vintages.jsonl',
             'forecast_path_versions.jsonl', 'evaluation_versions.jsonl')


def new_context(mode):
    if mode not in MODES:
        raise ValueError('EXPLICIT_RUN_MODE_REQUIRED')
    return dict(run_mode=mode, run_id=f'market-lab:{mode}:{uuid.uuid4().hex}',
                generated_at_utc=fp.utc_now(), code_version=fp.code_version(),
                official_daily=mode == 'OFFICIAL_DAILY')


def context(record):
    if not all(k in record for k in CONTEXT_FIELDS):
        raise ValueError('MISSING_RUN_CONTEXT')
    result = {k: record[k] for k in CONTEXT_FIELDS}
    if (result['run_mode'] not in MODES or
            result['official_daily'] is not (result['run_mode'] == 'OFFICIAL_DAILY') or
            not all(isinstance(result[k], str) and result[k] for k in CONTEXT_FIELDS[:-1])):
        raise ValueError('INVALID_RUN_CONTEXT')
    return result


def is_official(record):
    try:
        return context(record)['run_mode'] == 'OFFICIAL_DAILY'
    except ValueError:
        return False


def official_rows(rows):
    """Single consumer predicate: missing/legacy flags and TRIAL never qualify."""
    return [r for r in rows if is_official(r)]


def read_history(output, name, ctx):
    if name not in HISTORIES:
        raise ValueError('UNKNOWN_OFFICIAL_HISTORY')
    if context(ctx)['run_mode'] != 'OFFICIAL_DAILY':
        return []
    rows = fp._read_jsonl(Path(output) / name)
    if len(official_rows(rows)) != len(rows):
        raise ValueError('NON_OFFICIAL_HISTORY_REJECTED:' + name)
    return rows


def require_official(output, ctx, rows):
    """Gate before every official history mutation, including empty-file creation."""
    if context(ctx)['run_mode'] != 'OFFICIAL_DAILY':
        raise ValueError('OFFICIAL_HISTORY_WRITE_FORBIDDEN')
    marker = json.loads((Path(output) / '.lab_scope.json').read_text())
    if not is_official(marker) or any(not is_official(r) for r in rows):
        raise ValueError('NON_OFFICIAL_HISTORY_REJECTED')


def overlaps(a, b):
    a, b = Path(a).resolve(), Path(b).resolve()
    return a == b or a.is_relative_to(b) or b.is_relative_to(a)


def initialize_scope(output, ctx):
    """Never adopt an existing unclassified/pre-release artifact directory."""
    output = Path(output)
    marker = output / '.lab_scope.json'
    if output.exists() and not marker.exists() and any(output.iterdir()):
        raise ValueError('UNCLASSIFIED_OUTPUT_DIRECTORY_REJECTED')
    if marker.exists():
        if context(json.loads(marker.read_text()))['run_mode'] != ctx['run_mode']:
            raise ValueError('OUTPUT_MODE_MISMATCH')
    else:
        output.mkdir(parents=True, exist_ok=True)
        fp._atomic_write(marker, fp.canonical_json(context(ctx)))
    for path in output.rglob('*'):
        if path.is_symlink() or (path.is_file() and path.stat().st_nlink > 1):
            raise ValueError('ALIASED_OUTPUT_REJECTED')
    for name in HISTORIES:
        read_history(output, name, ctx)


def prepare_paths(args, ctx, source_root, reports, source_code_root):
    mode = context(ctx)['run_mode']
    if mode == 'REPLAY':
        raise ValueError('REPLAY_CANNOT_PREPARE_WRITABLE_PATHS')
    if mode == 'TRIAL':
        if args.output:
            raise ValueError('TRIAL_USES_TRIAL_ROOT_NOT_OFFICIAL_OUTPUT')
        base = Path(args.trial_root or (source_root.parent.parent / '.market_forecast_lab_trials')).resolve()
        run_dir = base / ctx['run_id'].split(':')[-1]
        protected = (source_root.parent, reports, Path(source_code_root) / 'reports')
        if any(overlaps(run_dir, p) for p in protected):
            raise ValueError('TRIAL_ROOT_OVERLAPS_OFFICIAL_DATA')
        # A fresh directory per invocation; user-provided paths cannot adopt old history.
        run_dir.mkdir(parents=True, exist_ok=False)
        output, write_root = run_dir / 'market_forecast_lab', run_dir / 'provenance'
        write_root.mkdir()
    else:
        if args.trial_root:
            raise ValueError('TRIAL_ROOT_NOT_ALLOWED_FOR_OFFICIAL')
        output = Path(args.output or (Path(source_code_root) / 'reports/market_forecast_lab')).resolve()
        write_root = source_root
        if output.name != 'market_forecast_lab' or overlaps(output, source_root) or reports.is_relative_to(output):
            raise ValueError('UNSAFE_OUTPUT_DIRECTORY')
    initialize_scope(output, ctx)
    if output.stat().st_dev != source_root.stat().st_dev:
        raise ValueError('OUTPUT_MUST_USE_PROVENANCE_VOLUME')
    return output, write_root


def seed_trial_store(source, destination, snapshot_ids, canonical, ctx):
    """Copy only referenced frozen bytes, with the existing CAS format; no hardlinks.

    Source is read-only. The trial store is a disposable instance of the existing
    provenance mechanism, not a second production OHLC subsystem.
    """
    if context(ctx)['run_mode'] != 'TRIAL' or overlaps(source, destination):
        raise ValueError('TRIAL_PROVENANCE_ISOLATION_REQUIRED')
    ids = set(snapshot_ids.values()) | {r['price_market_snapshot_id'] for r in canonical.values()}
    records = {r['snapshot_id']: r for r in fp._read_jsonl(source / 'raw_market_snapshots.jsonl')}
    for sid in sorted(ids):
        checksum = sid.split(':')[1]
        payload = (source / 'raw_ohlc' / (checksum + '.csv')).read_bytes()
        if hashlib.sha256(payload).hexdigest() != checksum:
            raise ValueError('RAW_HASH_MISMATCH')
        target = destination / 'raw_ohlc' / (checksum + '.csv')
        fp._install_content_addressed(target, payload, checksum)
        record = {**records[sid], 'source_run_id': records[sid]['run_id'],
                  'dataset_path': str(target), 'purpose': 'market_forecast_lab_trial_input_copy', **ctx}
        fp.append_jsonl(destination / 'raw_market_snapshots.jsonl', record)
    for record in canonical.values():
        name = record['cohort_id'].split(':')[1] + '.json'
        # Cohort body and source metadata remain canonical input, never a new Lab vintage.
        fp._atomic_write(destination / 'cohorts' / name, (source / 'cohorts' / name).read_bytes(), mode=0o444)
    fp._atomic_write(destination / 'run_context.json', fp.canonical_json(ctx))


def freeze_run_ohlc(frame, *, ticker, as_of, ctx, source='Yahoo Finance/yfinance',
                    requested_range='period=10y'):
    """Existing CAS/ledger primitives, with explicit run metadata on new records."""
    if context(ctx)['run_mode'] not in ('TRIAL', 'OFFICIAL_DAILY'):
        raise ValueError('REPLAY_PROVENANCE_WRITE_FORBIDDEN')
    marker = fp.ROOT / 'run_context.json'
    if ctx['run_mode'] == 'TRIAL':
        if not marker.is_file() or context(json.loads(marker.read_text())) != context(ctx):
            raise ValueError('TRIAL_PROVENANCE_ISOLATION_REQUIRED')
    elif marker.exists() and not is_official(json.loads(marker.read_text())):
        raise ValueError('OFFICIAL_CANNOT_WRITE_TRIAL_PROVENANCE')
    payload = fp._canonical_ohlc(frame)
    checksum = hashlib.sha256(payload).hexdigest()
    sid = 'sha256:' + checksum
    target = fp.RAW_DIR / (checksum + '.csv')
    fp._install_content_addressed(target, payload, checksum)
    record = dict(schema_version=1, snapshot_id=sid, sha256=checksum, ticker=ticker,
                  source=source, downloaded_at_utc=fp.utc_now(),
                  requested_interval='1d', requested_range=requested_range, timezone='UTC',
                  purpose='market_forecast_lab_' + ctx['run_mode'].lower(),
                  row_count=len(frame), dataset_path=str(target), forecast_date=as_of, **ctx)
    fp.append_jsonl_once(fp.RAW_INDEX, record, ('snapshot_id',))
    return sid


def read_official_latest(path):
    """Contract for the future Control Room. No TRIAL/pre-release fallback."""
    path = Path(path)
    envelope = json.loads(path.read_text())
    if not is_official(envelope):
        return None
    for key in ('forecasts', 'rotation'):
        if len(official_rows(envelope[key])) != len(envelope[key]):
            raise ValueError('MIXED_MODE_OFFICIAL_VIEW')
    for name, expected in envelope['artifacts'].items():
        if Path(name).name != name:
            raise ValueError('INVALID_ARTIFACT_NAME')
        if hashlib.sha256((path.parent / name).read_bytes()).hexdigest() != expected:
            raise ValueError('INCOMPLETE_OFFICIAL_PUBLICATION')
    return envelope
