from __future__ import annotations

import csv
import json
import os
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path
from unittest import mock

import paper_trading_evolution_control_tower as tower

NOW = datetime(2026, 7, 20, 8, 0, tzinfo=timezone.utc)


def good_summary():
    result = {}
    for key in tower.PIPELINE_KEYS.values():
        result[key] = {"status": "OK"}
    result["evolution_live_bridge"].update({
        "mode": "LOCKED_REVIEW_ONLY",
        "live_adapter_configured": False,
        "live_execution_enabled": False,
        "live_modified": False,
        "orders_sent": False,
        "automatic_releases": 0,
    })
    result["evolution_regime"]["routing_mode"] = "ADVISORY_ONLY"
    return result


class Block12RuntimeTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        root = Path(self.temp.name)
        self.reports = root / "reports"
        self.reports.mkdir()
        paths = {
            "REPORTS": self.reports,
            "CONFIG_PATH": root / "config.json",
            "STATE_PATH": self.reports / "state.json",
            "CHECKS_PATH": self.reports / "checks.csv",
            "INCIDENTS_PATH": self.reports / "incidents.json",
            "AUDIT_PATH": self.reports / "audit.csv",
            "RECOVERY_PATH": self.reports / "recovery.json",
            "REPORT_PATH": self.reports / "report.md",
            "CONFIG_SNAPSHOT_PATH": self.reports / "snapshot.json",
        }
        self.patchers = [mock.patch.object(tower, key, value) for key, value in paths.items()]
        for patcher in self.patchers:
            patcher.start()
        self.config = dict(tower.DEFAULT_CONFIG)
        self.config["observe_systemd"] = False
        self.config["critical_outputs"] = ["one.json", "two.csv"]
        self.config["required_storage_files"] = ["one.json", "two.csv"] + tower.BLOCK12_OUTPUTS
        paths["CONFIG_PATH"].write_text(json.dumps(self.config), encoding="utf-8")
        (self.reports / "one.json").write_text("{}", encoding="utf-8")
        (self.reports / "two.csv").write_text("a\n1\n", encoding="utf-8")
        self.storage = set(self.config["required_storage_files"])
        self.storage_patcher = mock.patch.object(tower, "_storage_files", return_value=self.storage)
        self.storage_patcher.start()

    def tearDown(self):
        self.storage_patcher.stop()
        for patcher in reversed(self.patchers):
            patcher.stop()
        self.temp.cleanup()

    def run_cycle(self, summary=None, bundle=None):
        return tower.run_control_tower_cycle(
            summary=good_summary() if summary is None else summary,
            market_bundle={"_paper_freshness": {"status": "FRESH"}} if bundle is None else bundle,
            when=NOW,
        )

    def test_01_good_cycle_healthy(self):
        result = self.run_cycle()
        self.assertEqual(result["health"], "HEALTHY")

    def test_02_empty_summary_bootstrapping(self):
        result = self.run_cycle(summary={})
        self.assertEqual(result["health"], "BOOTSTRAPPING")

    def test_03_pipeline_error_critical(self):
        summary = good_summary()
        summary["evolution_memory"]["status"] = "ERROR"
        self.assertEqual(self.run_cycle(summary)["health"], "CRITICAL")

    def test_04_live_modified_critical(self):
        summary = good_summary()
        summary["evolution_live_bridge"]["live_modified"] = True
        self.assertEqual(self.run_cycle(summary)["health"], "CRITICAL")

    def test_05_orders_sent_critical(self):
        summary = good_summary()
        summary["evolution_live_bridge"]["orders_sent"] = True
        self.assertEqual(self.run_cycle(summary)["health"], "CRITICAL")

    def test_06_automatic_release_critical(self):
        summary = good_summary()
        summary["evolution_live_bridge"]["automatic_releases"] = 1
        self.assertEqual(self.run_cycle(summary)["health"], "CRITICAL")

    def test_07_execution_enabled_critical(self):
        summary = good_summary()
        summary["evolution_live_bridge"]["live_execution_enabled"] = True
        self.assertEqual(self.run_cycle(summary)["health"], "CRITICAL")

    def test_08_adapter_configured_critical(self):
        summary = good_summary()
        summary["evolution_live_bridge"]["live_adapter_configured"] = True
        self.assertEqual(self.run_cycle(summary)["health"], "CRITICAL")

    def test_09_wrong_live_mode_critical(self):
        summary = good_summary()
        summary["evolution_live_bridge"]["mode"] = "EXECUTE"
        self.assertEqual(self.run_cycle(summary)["health"], "CRITICAL")

    def test_10_regime_routing_warning(self):
        summary = good_summary()
        summary["evolution_regime"]["routing_mode"] = "AUTO"
        self.assertEqual(self.run_cycle(summary)["health"], "DEGRADED")

    def test_11_missing_output_bootstrapping(self):
        (self.reports / "one.json").unlink()
        self.assertEqual(self.run_cycle()["health"], "BOOTSTRAPPING")

    def test_12_stale_output_degraded(self):
        old = (NOW - timedelta(hours=48)).timestamp()
        os.utime(self.reports / "one.json", (old, old))
        self.assertEqual(self.run_cycle()["health"], "DEGRADED")

    def test_13_storage_missing_critical(self):
        self.storage.remove("two.csv")
        self.assertEqual(self.run_cycle()["health"], "CRITICAL")

    def test_14_empty_chain_valid(self):
        self.assertTrue(tower.verify_audit_chain(tower.AUDIT_PATH)["valid"])

    def test_15_tampered_chain_invalid(self):
        self.run_cycle()
        rows = list(csv.DictReader(tower.AUDIT_PATH.open(encoding="utf-8")))
        rows[0]["health"] = "TAMPERED"
        tower.write_csv(tower.AUDIT_PATH, tower.AUDIT_FIELDS, rows)
        self.assertFalse(tower.verify_audit_chain(tower.AUDIT_PATH)["valid"])

    def test_16_chain_appends(self):
        self.run_cycle()
        self.run_cycle()
        self.assertEqual(tower.verify_audit_chain(tower.AUDIT_PATH)["rows"], 2)

    def test_17_no_automatic_actions(self):
        result = self.run_cycle()
        self.assertEqual(result["automatic_repairs"], 0)
        self.assertEqual(result["automatic_restarts"], 0)
        self.assertEqual(result["automatic_releases"], 0)

    def test_18_outputs_written(self):
        self.run_cycle()
        for path in (
            tower.STATE_PATH, tower.CHECKS_PATH, tower.INCIDENTS_PATH,
            tower.AUDIT_PATH, tower.RECOVERY_PATH, tower.REPORT_PATH,
            tower.CONFIG_SNAPSHOT_PATH,
        ):
            self.assertTrue(path.exists())

    def test_19_systemd_unavailable_is_warning(self):
        self.config["observe_systemd"] = True
        tower.CONFIG_PATH.write_text(json.dumps(self.config), encoding="utf-8")
        with mock.patch.object(tower, "_systemd", return_value={"available": "false"}):
            self.assertEqual(self.run_cycle()["health"], "DEGRADED")

    def test_20_recovery_ready(self):
        self.assertEqual(self.run_cycle()["recovery_status"], "READY")

    def test_21_stale_market_degraded(self):
        result = self.run_cycle(bundle={"_paper_freshness": {"status": "STALE"}})
        self.assertEqual(result["health"], "DEGRADED")

    def test_22_cycles_increment(self):
        self.run_cycle()
        self.run_cycle()
        state = json.loads(tower.STATE_PATH.read_text(encoding="utf-8"))
        self.assertEqual(state["cycles"], 2)

    def test_23_disabled(self):
        self.config["enabled"] = False
        tower.CONFIG_PATH.write_text(json.dumps(self.config), encoding="utf-8")
        self.assertEqual(self.run_cycle()["status"], "DISABLED")

    def test_24_report_safety_text(self):
        report = self.run_cycle()["report_markdown"]
        self.assertIn("Ordini reali: **0**", report)
        self.assertIn("Riavvii automatici: **0**", report)


if __name__ == "__main__":
    unittest.main()
