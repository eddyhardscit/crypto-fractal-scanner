from __future__ import annotations

import csv
import json
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path
from unittest import mock

import paper_trading_post_promotion_watchdog as watchdog


NOW = datetime(2026, 7, 19, tzinfo=timezone.utc)


def transaction(
    *,
    deadline_days: int = 20,
) -> dict:
    return {
        "transaction_id": "TX-1",
        "plan_id": "PROMO-1",
        "family_id": "FAMILY-1",
        "candidate_id": "CAND-ID",
        "candidate_portfolio": "NEW_MASTER",
        "parent_id": "OLD-ID",
        "parent_portfolio": "OLD_MASTER",
        "status": "EXECUTED",
        "executed_utc": (
            NOW - timedelta(days=10)
        ).isoformat(),
        "rollback_deadline_utc": (
            NOW + timedelta(days=deadline_days)
        ).isoformat(),
    }


def trade(
    portfolio: str,
    group: str,
    r_value: float,
    *,
    asset: str = "SOL",
    side: str = "LONG",
    reason: str = "TARGET",
    risk_model: str = "block4_5_v1",
    quality: str = "FULL_FROM_ENTRY",
    offset: int = 0,
) -> dict:
    return {
        "trade_id": f"{portfolio}-{group}",
        "experiment_group_id": group,
        "portfolio": portfolio,
        "asset": asset,
        "side": side,
        "closed_at": (
            NOW - timedelta(days=5)
            + timedelta(minutes=offset)
        ).isoformat(),
        "r_multiple": str(r_value),
        "close_reason": reason,
        "risk_model_version_at_exit": risk_model,
        "excursion_quality": quality,
    }


def paired_trades(
    count: int,
    delta: float,
    *,
    assets=("SOL", "BTC"),
) -> list[dict]:
    rows = []
    for index in range(count):
        base = 0.35 if index % 4 else -0.45
        asset = assets[index % len(assets)]
        rows.extend(
            [
                trade(
                    "OLD_MASTER",
                    f"G{index}",
                    base,
                    asset=asset,
                    offset=index,
                ),
                trade(
                    "NEW_MASTER",
                    f"G{index}",
                    base + delta,
                    asset=asset,
                    offset=index,
                ),
            ]
        )
    return rows


class Block8PostPromotionTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        root = Path(self.temporary.name)
        self.paths = {
            "CONFIG_PATH": root / "config.json",
            "CONFIG_SNAPSHOT_PATH": root / "config_snapshot.json",
            "PROMOTION_STATE_PATH": root / "promotion_state.json",
            "TRADE_LOG_PATH": root / "trade_log.csv",
            "STATE_PATH": root / "state.json",
            "COMPARISONS_PATH": root / "comparisons.csv",
            "HISTORY_PATH": root / "history.csv",
            "ROLLBACK_RECOMMENDATIONS_PATH": root / "recommendations.json",
            "REPORT_PATH": root / "report.md",
        }
        self.patchers = [
            mock.patch.object(
                watchdog,
                name,
                value,
            )
            for name, value in self.paths.items()
        ]
        for patcher in self.patchers:
            patcher.start()
        self.config = json.loads(
            json.dumps(watchdog.DEFAULT_CONFIG)
        )

    def tearDown(self):
        for patcher in reversed(self.patchers):
            patcher.stop()
        self.temporary.cleanup()

    def write_trades(self, rows):
        fields = sorted(
            {
                key
                for row in rows
                for key in row
            }
        )
        with self.paths["TRADE_LOG_PATH"].open(
            "w",
            encoding="utf-8",
            newline="",
        ) as handle:
            writer = csv.DictWriter(
                handle,
                fieldnames=fields,
            )
            writer.writeheader()
            writer.writerows(rows)

    def write_promotion(self, tx=None):
        row = tx or transaction()
        self.paths["PROMOTION_STATE_PATH"].write_text(
            json.dumps(
                {
                    "active_by_family": {
                        "FAMILY-1": row
                    }
                }
            ),
            encoding="utf-8",
        )

    def test_01_no_active_promotions_is_ok(self):
        self.paths["PROMOTION_STATE_PATH"].write_text(
            json.dumps({"active_by_family": {}}),
            encoding="utf-8",
        )
        result = (
            watchdog.run_post_promotion_watchdog_cycle(
                NOW
            )
        )
        self.assertEqual(result["status"], "OK")
        self.assertEqual(result["active_promotions"], 0)

    def test_02_only_executed_transactions_are_active(self):
        tx = transaction()
        tx["status"] = "ROLLED_BACK"
        rows = watchdog.active_transactions(
            {
                "active_by_family": {
                    "FAMILY-1": tx
                }
            }
        )
        self.assertEqual(rows, [])

    def test_03_pairs_same_experiment_group(self):
        rows = paired_trades(5, 0.1)
        matched, master_count, old_count = (
            watchdog.paired_rows(
                rows,
                transaction(),
                self.config,
            )
        )
        self.assertEqual(len(matched), 5)
        self.assertEqual(master_count, 5)
        self.assertEqual(old_count, 5)

    def test_04_mismatched_asset_not_paired(self):
        rows = [
            trade(
                "OLD_MASTER",
                "G1",
                0.1,
                asset="BTC",
            ),
            trade(
                "NEW_MASTER",
                "G1",
                0.2,
                asset="SOL",
            ),
        ]
        matched, _, _ = watchdog.paired_rows(
            rows,
            transaction(),
            self.config,
        )
        self.assertEqual(matched, [])

    def test_05_pre_promotion_trade_excluded(self):
        row = trade("NEW_MASTER", "G1", 0.1)
        row["closed_at"] = (
            NOW - timedelta(days=20)
        ).isoformat()
        self.assertFalse(
            watchdog.eligible_trade(
                row,
                watchdog.parse_time(
                    transaction()["executed_utc"]
                ),
                self.config,
            )
        )

    def test_06_wrong_risk_model_excluded(self):
        row = trade(
            "NEW_MASTER",
            "G1",
            0.1,
            risk_model="legacy",
        )
        self.assertFalse(
            watchdog.eligible_trade(
                row,
                watchdog.parse_time(
                    transaction()["executed_utc"]
                ),
                self.config,
            )
        )

    def test_07_partial_excursion_excluded(self):
        row = trade(
            "NEW_MASTER",
            "G1",
            0.1,
            quality="PARTIAL",
        )
        self.assertFalse(
            watchdog.eligible_trade(
                row,
                watchdog.parse_time(
                    transaction()["executed_utc"]
                ),
                self.config,
            )
        )

    def test_08_waiting_sample_below_20(self):
        result = watchdog.evaluate_transaction(
            transaction(),
            paired_trades(10, 0.1),
            self.config,
            NOW,
        )
        self.assertEqual(
            result["status"],
            "WAITING_SAMPLE",
        )

    def test_09_monitoring_between_20_and_50(self):
        result = watchdog.evaluate_transaction(
            transaction(),
            paired_trades(30, 0.02),
            self.config,
            NOW,
        )
        self.assertEqual(
            result["status"],
            "MONITORING",
        )

    def test_10_healthy_after_sufficient_sample(self):
        result = watchdog.evaluate_transaction(
            transaction(),
            paired_trades(60, 0.08),
            self.config,
            NOW,
        )
        self.assertEqual(result["status"], "HEALTHY")

    def test_11_watch_for_early_deterioration(self):
        result = watchdog.evaluate_transaction(
            transaction(),
            paired_trades(60, -0.04),
            self.config,
            NOW,
        )
        self.assertEqual(result["status"], "WATCH")

    def test_12_rollback_recommended_robust_loss(self):
        result = watchdog.evaluate_transaction(
            transaction(),
            paired_trades(100, -0.15),
            self.config,
            NOW,
        )
        self.assertEqual(
            result["status"],
            "ROLLBACK_RECOMMENDED",
        )

    def test_13_extra_liquidation_recommends_rollback(self):
        rows = paired_trades(90, 0.02)
        for row in rows:
            if row["portfolio"] == "NEW_MASTER":
                row["close_reason"] = (
                    "LIQUIDATION_INTRABAR_WORST_CASE"
                )
                break
        result = watchdog.evaluate_transaction(
            transaction(),
            rows,
            self.config,
            NOW,
        )
        self.assertEqual(
            result["status"],
            "ROLLBACK_RECOMMENDED",
        )

    def test_14_two_extra_liquidations_are_critical(self):
        rows = paired_trades(90, 0.02)
        changed = 0
        for row in rows:
            if row["portfolio"] == "NEW_MASTER":
                row["close_reason"] = "LIQUIDATION_GAP"
                changed += 1
                if changed == 2:
                    break
        result = watchdog.evaluate_transaction(
            transaction(),
            rows,
            self.config,
            NOW,
        )
        self.assertEqual(result["status"], "CRITICAL")

    def test_15_expired_window_is_explicit(self):
        result = watchdog.evaluate_transaction(
            transaction(deadline_days=-1),
            paired_trades(100, -0.15),
            self.config,
            NOW,
        )
        self.assertEqual(
            result["status"],
            "ROLLBACK_WINDOW_EXPIRED",
        )

    def test_16_bootstrap_is_deterministic(self):
        first = watchdog.bootstrap_ci(
            [0.1, 0.2, -0.1],
            "TX",
            300,
            0.95,
        )
        second = watchdog.bootstrap_ci(
            [0.1, 0.2, -0.1],
            "TX",
            300,
            0.95,
        )
        self.assertEqual(first, second)

    def test_17_no_automatic_rollback_defaults(self):
        self.assertFalse(
            watchdog.DEFAULT_CONFIG[
                "automatic_rollback"
            ]
        )
        self.assertTrue(
            watchdog.DEFAULT_CONFIG["paper_only"]
        )

    def test_18_recommendation_payload_actionable_only(self):
        rows = [
            {
                "status": "HEALTHY",
                "transaction_id": "A",
            },
            {
                "status": "ROLLBACK_RECOMMENDED",
                "transaction_id": "B",
            },
        ]
        payload = watchdog.recommendation_payload(
            rows,
            NOW,
        )
        self.assertEqual(
            payload["recommendation_count"],
            1,
        )
        self.assertEqual(
            payload["automatic_rollbacks"],
            0,
        )

    def test_19_cycle_writes_all_outputs(self):
        self.write_promotion()
        self.write_trades(paired_trades(10, 0.1))
        result = (
            watchdog.run_post_promotion_watchdog_cycle(
                NOW
            )
        )
        self.assertEqual(result["status"], "OK")
        for key in (
            "STATE_PATH",
            "COMPARISONS_PATH",
            "HISTORY_PATH",
            "ROLLBACK_RECOMMENDATIONS_PATH",
            "REPORT_PATH",
            "CONFIG_SNAPSHOT_PATH",
        ):
            self.assertTrue(self.paths[key].exists())

    def test_20_history_only_on_status_change(self):
        self.write_promotion()
        self.write_trades(paired_trades(10, 0.1))
        watchdog.run_post_promotion_watchdog_cycle(NOW)
        watchdog.run_post_promotion_watchdog_cycle(
            NOW + timedelta(hours=1)
        )
        rows = list(
            csv.DictReader(
                self.paths["HISTORY_PATH"].open(
                    encoding="utf-8"
                )
            )
        )
        self.assertEqual(len(rows), 1)

    def test_21_promotion_state_not_modified(self):
        self.write_promotion()
        before = self.paths[
            "PROMOTION_STATE_PATH"
        ].read_text(encoding="utf-8")
        self.write_trades(paired_trades(10, 0.1))
        result = (
            watchdog.run_post_promotion_watchdog_cycle(
                NOW
            )
        )
        after = self.paths[
            "PROMOTION_STATE_PATH"
        ].read_text(encoding="utf-8")
        self.assertEqual(before, after)
        self.assertFalse(
            result["promotion_state_modified"]
        )

    def test_22_live_and_orders_are_never_modified(self):
        self.write_promotion()
        self.write_trades(paired_trades(10, 0.1))
        result = (
            watchdog.run_post_promotion_watchdog_cycle(
                NOW
            )
        )
        self.assertFalse(result["live_modified"])
        self.assertFalse(result["orders_sent"])
        self.assertEqual(
            result["automatic_rollbacks"],
            0,
        )


if __name__ == "__main__":
    unittest.main()
