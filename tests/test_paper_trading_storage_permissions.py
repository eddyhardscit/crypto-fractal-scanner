import io
import os
import tempfile
import unittest
import zipfile
from pathlib import Path

import paper_trading_storage as storage


class PaperTradingStoragePermissionTests(unittest.TestCase):
    def test_safe_extract_atomically_replaces_read_only_snapshot(self) -> None:
        name = "paper_trading_crash_guard_config_snapshot.json"
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            reports = root / "reports"
            reports.mkdir()
            target = reports / name
            target.write_bytes(b"old")
            target.chmod(0o444)
            before_inode = target.stat().st_ino

            payload = io.BytesIO()
            with zipfile.ZipFile(payload, "w") as archive:
                archive.writestr(f"reports/{name}", b"new")

            original = Path.cwd()
            try:
                os.chdir(root)
                restored = storage.safe_extract(payload.getvalue())
            finally:
                os.chdir(original)

            self.assertEqual([f"reports/{name}"], restored)
            self.assertEqual(b"new", target.read_bytes())
            self.assertNotEqual(before_inode, target.stat().st_ino)


if __name__ == "__main__":
    unittest.main()
