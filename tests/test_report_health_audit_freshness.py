from __future__ import annotations

import unittest
from datetime import datetime, timezone

from report_health_audit import health_status, persisted_health_status, row


NOW = datetime(2026, 8, 21, 12, 0, tzinfo=timezone.utc)


class ReportHealthFreshnessTests(unittest.TestCase):
    def test_fresh_report_health_does_not_claim_operational_proof(self):
        rows = [row("ledger", "reports/ledger.json", "OK", "OK", "fresh")]

        status = health_status(rows, [], NOW, 36)

        self.assertEqual(status["status"], "REPORTS_HEALTHY_UNVERIFIED")
        self.assertEqual(status["component_state"], "OK")
        self.assertEqual(status["data_freshness"]["state"], "FRESH")
        self.assertFalse(status["operationally_proven"])
        self.assertFalse(status["stale"])

    def test_old_unqualified_ok_is_effectively_stale(self):
        legacy_payload = {
            "generated_utc": "2026-07-17T07:33:57+00:00",
            "status": "OK",
        }

        status = persisted_health_status(legacy_payload, NOW)

        self.assertEqual(status["status"], "STALE")
        self.assertEqual(status["data_freshness"]["state"], "STALE")
        self.assertFalse(status["operationally_proven"])
        self.assertTrue(status["stale"])

    def test_fresh_legacy_ok_is_qualified(self):
        legacy_payload = {
            "generated_utc": "2026-08-21T11:00:00+00:00",
            "status": "OK",
        }

        status = persisted_health_status(legacy_payload, NOW)

        self.assertEqual(status["status"], "REPORTS_HEALTHY_UNVERIFIED")
        self.assertEqual(status["data_freshness"]["state"], "FRESH")
        self.assertFalse(status["stale"])

    def test_missing_generation_time_fails_closed(self):
        status = persisted_health_status({"status": "OK"}, NOW)

        self.assertEqual(status["status"], "STALE")
        self.assertTrue(status["stale"])


if __name__ == "__main__":
    unittest.main()
