from __future__ import annotations

import json
import os
import stat
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import paper_trading_shadow_exit as shadow


class Block3PermissionHotfixTests(unittest.TestCase):
    def test_load_config_replaces_read_only_existing_snapshot(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            config_path = root / "config.json"
            snapshot_path = root / "reports" / "snapshot.json"
            snapshot_path.parent.mkdir(parents=True)
            snapshot_path.write_text('{"old": true}\n', encoding="utf-8")
            snapshot_path.chmod(0o444)

            with mock.patch.object(shadow, "CONFIG_PATH", config_path), \
                 mock.patch.object(shadow, "CONFIG_SNAPSHOT_PATH", snapshot_path):
                config = shadow.load_config()

            self.assertEqual(
                len(config["scenarios"]),
                len(shadow.DEFAULT_CONFIG["scenarios"]),
            )
            saved = json.loads(snapshot_path.read_text(encoding="utf-8"))
            self.assertEqual(saved["scenario_set_version"], config["scenario_set_version"])
            self.assertEqual(len(saved["scenarios"]), len(config["scenarios"]))

    def test_source_uses_atomic_snapshot_write(self) -> None:
        source = Path(shadow.__file__).read_text(encoding="utf-8")
        self.assertIn(
            "atomic_write_json(CONFIG_SNAPSHOT_PATH, config)",
            source,
        )


if __name__ == "__main__":
    unittest.main()
