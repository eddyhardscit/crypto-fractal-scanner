"""Canonical publishing extension safety and artifact integration checks.

Only the optional hook is executed, with a failing fake interpreter. The complete
daily wrapper, all producer models, network clients, and real senders stay idle.
"""
from contextlib import redirect_stdout
import csv
from datetime import date, timedelta
import hashlib
import io
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

import sol_long_term_history as history
import sol_long_term_history_publish as publisher


REAL_REPORTS = Path("/opt/crypto-fractal-scanner-publisher/reports")
ROOT = Path(__file__).resolve().parents[1]
FORECAST_NAMES = [f"scanner_forecast_{asset}.png" for asset in ("BTC", "SOL", "DOGE")]


def tree_bytes(root):
    return {str(path.relative_to(root)): path.read_bytes()
            for path in sorted(root.rglob("*")) if path.is_file()}


def quiet_publish(*args, **kwargs):
    with redirect_stdout(io.StringIO()):
        return publisher.publish(*args, **kwargs)


class PublisherFailureTests(unittest.TestCase):
    def test_missing_source_keeps_last_page_bytes_and_existing_index(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            out = root / publisher.OUTPUT_DIR
            out.mkdir()
            (out / "README.md").write_bytes(b"Previously validated dashboard\n")
            (out / "sol_long_term_cone_history.png").write_bytes(b"previous chart bytes")
            (root / "latest_report.md").write_bytes(b"Original BTC/SOL/DOGE page" + publisher.INDEX_SECTION.encode())
            before = tree_bytes(root)
            self.assertFalse(quiet_publish(root))
            self.assertEqual(tree_bytes(root), before)

    def test_missing_source_does_not_create_dashboard_or_dead_link(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            original = b"# Existing forecasts\r\nBTC/SOL/DOGE\r\n"
            (root / "latest_report.md").write_bytes(original)
            self.assertFalse(quiet_publish(root))
            self.assertEqual(tree_bytes(root), {"latest_report.md": original})

    def test_index_append_is_exact_byte_preserving_and_idempotent(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            out = root / publisher.OUTPUT_DIR
            out.mkdir()
            (out / "README.md").write_text("# SOL Long-Term Cone History\n")
            original = b"# BTC\r\n![BTC](scanner_forecast_BTC.png)\r\n\x20\x20\nLast byte retained"
            index = root / "latest_report.md"
            index.write_bytes(original)
            self.assertTrue(publisher.add_index_link(index, out))
            expected = original + publisher.INDEX_SECTION.encode("utf-8")
            self.assertEqual(index.read_bytes(), expected)
            self.assertFalse(publisher.add_index_link(index, out))
            self.assertEqual(index.read_bytes(), expected)
            self.assertEqual(index.read_bytes().count(b"SOL_LONG_TERM_CONE_HISTORY_START"), 1)

    def test_isolated_daily_hook_failure_allows_publisher_to_continue(self):
        candidate = ROOT / "deploy" / "crypto-daily-scanner-cycle"
        if not candidate.exists():
            self.skipTest("candidate wrapper is not bundled in this checkout")
        source = candidate.read_text()
        start = source.index("# Artifact-only SOL long-term history;")
        end = source.index('git config user.name', start)
        hook = source[start:end]
        self.assertNotIn("source ", hook)
        self.assertNotIn("ENV_FILE", hook)
        self.assertNotIn("git ", hook)
        self.assertNotIn("scanner_forecast_tracker.py", hook)
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "sol_long_term_history_publish.py").write_text("raise AssertionError('must not execute')\n")
            fake = root / "fake-python"
            fake.write_text("#!/bin/sh\nexit 23\n")
            fake.chmod(0o700)
            script = 'set -Eeuo pipefail\nPYTHON="$1"\n' + hook + '\nprintf "EXISTING_PUBLISHER_CONTINUES\\n"\n'
            result = subprocess.run(["bash", "-c", script, "isolated-hook-test", str(fake)],
                                    cwd=root, capture_output=True, text=True, timeout=10)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("LONG_TERM_HISTORY_RETAINED_LAST_VALID", result.stdout)
            self.assertIn("EXISTING_PUBLISHER_CONTINUES", result.stdout)


@unittest.skipUnless((REAL_REPORTS / "sol_long_term_probability_cone.json").is_file(),
                     "authoritative read-only SOL history is unavailable")
class RealPublisherIntegrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.snapshots, cls.current, cls.warnings = history.discover_snapshots(REAL_REPORTS)

    def test_real_generation_preserves_btc_sol_doge_30day_artifacts(self):
        before = {name: hashlib.sha256((REAL_REPORTS / name).read_bytes()).hexdigest() for name in FORECAST_NAMES}
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary) / "output"
            manifest = publisher.generate(REAL_REPORTS, output)
            self.assertGreater(manifest["DAILY_HISTORY_ROWS"], 0)
            self.assertEqual(len(list(output.iterdir())), 7)
            self.assertEqual(manifest["FORECAST_VINTAGE_ROWS"], 4 * manifest["DAILY_HISTORY_ROWS"])
        after = {name: hashlib.sha256((REAL_REPORTS / name).read_bytes()).hexdigest() for name in FORECAST_NAMES}
        self.assertEqual(after, before)

    def test_render_failure_keeps_every_previous_output_byte(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            output = root / publisher.OUTPUT_DIR
            publisher.generate(REAL_REPORTS, output)
            (root / "latest_report.md").write_bytes(b"Original forecast page" + publisher.INDEX_SECTION.encode())
            before = tree_bytes(root)
            with patch("sol_long_term_history_dashboard.render_dashboard", side_effect=RuntimeError("injected render failure")):
                self.assertFalse(quiet_publish(REAL_REPORTS, output_dir=output, index_path=root / "latest_report.md"))
            self.assertEqual(tree_bytes(root), before)

    def test_output_write_failure_rolls_back_already_replaced_files(self):
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary) / "output"
            output.mkdir()
            (output / "README.md").write_bytes(b"previous valid page")
            (output / "sol_long_term_cone_current.png").write_bytes(b"previous current plot")
            before = tree_bytes(output)
            real_write = publisher.atomic_write
            calls = 0

            def fail_once(path, content):
                nonlocal calls
                calls += 1
                if calls == 2:
                    raise OSError("injected replacement failure")
                return real_write(path, content)

            with patch.object(publisher, "atomic_write", side_effect=fail_once):
                with self.assertRaises(OSError):
                    publisher.generate(REAL_REPORTS, output)
            self.assertEqual(tree_bytes(output), before)

    def test_ledgers_same_day_rerun_are_byte_identical(self):
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary)
            publisher.generate(REAL_REPORTS, output)
            before = {name: (output / name).read_bytes() for name in (publisher.DAILY_CSV, publisher.VINTAGES_CSV)}
            publisher.generate(REAL_REPORTS, output)
            self.assertEqual({name: (output / name).read_bytes() for name in before}, before)

    def test_new_real_day_appends_without_rewriting_committed_prefix(self):
        selected = history.select_daily(self.snapshots)
        if len(selected) < 2:
            self.skipTest("at least two real observation dates are needed for append smoke test")
        first_day = selected[0]["date_local"]
        first = [row for row in self.snapshots if row["date_local"] == first_day]
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary)
            with patch.object(publisher, "discover_snapshots", return_value=(first, first[-1], [])):
                initial = publisher.generate(REAL_REPORTS, output)
            before = {name: (output / name).read_bytes() for name in (publisher.DAILY_CSV, publisher.VINTAGES_CSV)}
            complete = publisher.generate(REAL_REPORTS, output)
            self.assertGreater(complete["DAILY_HISTORY_ROWS"], initial["DAILY_HISTORY_ROWS"])
            for name, prefix in before.items():
                self.assertTrue((output / name).read_bytes().startswith(prefix), name)

    def test_truncated_vintage_newline_fails_before_appending_another_day(self):
        selected = history.select_daily(self.snapshots)
        if len(selected) < 2:
            self.skipTest("at least two real observation dates are needed")
        first = [row for row in self.snapshots if row["date_local"] == selected[0]["date_local"]]
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary)
            with patch.object(publisher, "discover_snapshots", return_value=(first, first[-1], [])):
                publisher.generate(REAL_REPORTS, output)
            vintage = output / publisher.VINTAGES_CSV
            vintage.write_bytes(vintage.read_bytes().removesuffix(b"\n"))
            before = tree_bytes(output)
            with self.assertRaises(history.HistoryError):
                publisher.generate(REAL_REPORTS, output)
            self.assertEqual(tree_bytes(output), before)

    def test_forecast_target_dates_are_exact_and_no_outcomes_materialize(self):
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary)
            publisher.generate(REAL_REPORTS, output)
            with (output / publisher.VINTAGES_CSV).open() as handle:
                reader = csv.DictReader(handle)
                self.assertEqual(reader.fieldnames, history.VINTAGE_FIELDS)
                self.assertFalse(any("outcome" in name or "realized" in name or "mature" in name for name in reader.fieldnames))
                rows = list(reader)
            self.assertGreater(len(rows), 0)
            for row in rows:
                expected = date.fromisoformat(row["forecast_date"]) + timedelta(days=int(row["target_horizon_days"]))
                self.assertEqual(row["target_date"], expected.isoformat())
                self.assertGreater(date.fromisoformat(row["target_date"]), date.fromisoformat(row["forecast_date"]))


if __name__ == "__main__":
    unittest.main()
