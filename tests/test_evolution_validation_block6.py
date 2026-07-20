from __future__ import annotations

import csv
import json
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path
from unittest import mock

import paper_trading_candidate_validator as validator


NOW = datetime(2026, 7, 19, tzinfo=timezone.utc)


def candidate_record() -> dict:
    return {
        "candidate_id": "candidate-1",
        "strategy_id": "candidate-1",
        "portfolio_name": "CAND",
        "parent_portfolio": "PARENT",
        "created_at": (NOW - timedelta(days=10)).isoformat(),
        "status": "CANDIDATE",
        "active": True,
        "mutation": {
            "parameter": "reward_risk",
            "old_value": 1.5,
            "new_value": 2.0,
        },
    }


def trade(
    portfolio: str,
    group: str,
    r_value: float,
    *,
    asset: str = "SOL",
    side: str = "LONG",
    close_reason: str = "TARGET",
    risk_model: str = "block4_5_v1",
    quality: str = "FULL_FROM_ENTRY",
    closed_offset: int = 0,
) -> dict:
    closed = NOW - timedelta(days=5) + timedelta(
        minutes=closed_offset
    )
    return {
        "trade_id": f"{portfolio}-{group}",
        "experiment_group_id": group,
        "portfolio": portfolio,
        "asset": asset,
        "side": side,
        "closed_at": closed.isoformat(),
        "r_multiple": str(r_value),
        "close_reason": close_reason,
        "risk_model_version_at_exit": risk_model,
        "excursion_quality": quality,
    }


def pairs(
    count: int,
    candidate_delta: float,
    *,
    assets=("SOL", "BTC"),
) -> list[dict]:
    rows = []
    for index in range(count):
        base = 0.25 if index % 3 else -0.50
        asset = assets[index % len(assets)]
        rows.append(
            trade(
                "PARENT",
                f"G{index}",
                base,
                asset=asset,
                closed_offset=index,
            )
        )
        rows.append(
            trade(
                "CAND",
                f"G{index}",
                base + candidate_delta,
                asset=asset,
                closed_offset=index,
            )
        )
    return rows


class Block6CandidateValidationTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        root = Path(self.temporary.name)
        self.paths = {
            "CONFIG_PATH": root / "config.json",
            "CONFIG_SNAPSHOT_PATH": root / "config_snapshot.json",
            "CANDIDATE_STATE_PATH": root / "candidate_state.json",
            "CANDIDATE_REGISTRY_PATH": root / "candidate_registry.json",
            "TRADE_LOG_PATH": root / "trades.csv",
            "STATE_PATH": root / "validation_state.json",
            "EVALUATIONS_PATH": root / "evaluations.csv",
            "HISTORY_PATH": root / "history.csv",
            "PROMOTION_REVIEW_PATH": root / "promotion.json",
            "REPORT_PATH": root / "report.md",
        }
        self.patchers = [
            mock.patch.object(validator, name, value)
            for name, value in self.paths.items()
        ]
        for patcher in self.patchers:
            patcher.start()
        self.config = json.loads(
            json.dumps(validator.DEFAULT_CONFIG)
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

    def write_candidate_inputs(self):
        record = candidate_record()
        self.paths["CANDIDATE_STATE_PATH"].write_text(
            json.dumps(
                {"candidates": {"candidate-1": record}}
            ),
            encoding="utf-8",
        )
        self.paths["CANDIDATE_REGISTRY_PATH"].write_text(
            json.dumps(
                {
                    "paper_only": True,
                    "automatic_promotions": 0,
                    "automatic_retirements": 0,
                    "candidates": [
                        {
                            "strategy_id": "candidate-1",
                            "status": "CANDIDATE",
                            "metadata": {},
                        }
                    ],
                }
            ),
            encoding="utf-8",
        )

    def test_01_no_candidates_is_ok(self):
        self.paths["CANDIDATE_STATE_PATH"].write_text(
            json.dumps({"candidates": {}}),
            encoding="utf-8",
        )
        self.paths["CANDIDATE_REGISTRY_PATH"].write_text(
            json.dumps({"candidates": []}),
            encoding="utf-8",
        )
        result = validator.run_candidate_validation_cycle(NOW)
        self.assertEqual(result["status"], "OK")
        self.assertEqual(result["evaluated_candidates"], 0)

    def test_02_pairs_use_same_experiment_group(self):
        rows = pairs(5, 0.1)
        matched, candidate_count, parent_count = (
            validator.paired_rows(
                rows,
                candidate_record(),
                self.config,
            )
        )
        self.assertEqual(len(matched), 5)
        self.assertEqual(candidate_count, 5)
        self.assertEqual(parent_count, 5)

    def test_03_mismatched_assets_are_not_paired(self):
        rows = [
            trade("PARENT", "G1", 0.1, asset="BTC"),
            trade("CAND", "G1", 0.2, asset="SOL"),
        ]
        matched, _, _ = validator.paired_rows(
            rows,
            candidate_record(),
            self.config,
        )
        self.assertEqual(matched, [])

    def test_04_pre_creation_trades_are_excluded(self):
        row = trade("CAND", "G1", 0.2)
        row["closed_at"] = (
            NOW - timedelta(days=20)
        ).isoformat()
        self.assertFalse(
            validator.eligible_trade(
                row,
                validator.parse_time(
                    candidate_record()["created_at"]
                ),
                self.config,
            )
        )

    def test_05_wrong_risk_model_is_excluded(self):
        row = trade(
            "CAND",
            "G1",
            0.2,
            risk_model="legacy",
        )
        self.assertFalse(
            validator.eligible_trade(
                row,
                validator.parse_time(
                    candidate_record()["created_at"]
                ),
                self.config,
            )
        )

    def test_06_partial_excursion_is_excluded(self):
        row = trade(
            "CAND",
            "G1",
            0.2,
            quality="PARTIAL",
        )
        self.assertFalse(
            validator.eligible_trade(
                row,
                validator.parse_time(
                    candidate_record()["created_at"]
                ),
                self.config,
            )
        )

    def test_07_incubating_below_30_pairs(self):
        evaluation = validator.evaluate_candidate(
            candidate_record(),
            pairs(20, 0.10),
            self.config,
            NOW,
        )
        self.assertEqual(evaluation["status"], "INCUBATING")

    def test_08_validating_between_30_and_80(self):
        evaluation = validator.evaluate_candidate(
            candidate_record(),
            pairs(50, 0.01),
            self.config,
            NOW,
        )
        self.assertEqual(evaluation["status"], "VALIDATING")

    def test_09_robust_underperformance(self):
        evaluation = validator.evaluate_candidate(
            candidate_record(),
            pairs(100, -0.20),
            self.config,
            NOW,
        )
        self.assertEqual(
            evaluation["status"],
            "UNDERPERFORMING",
        )

    def test_10_extra_liquidation_is_risk_rejected(self):
        rows = pairs(40, 0.10)
        for row in rows:
            if row["portfolio"] == "CAND":
                row["close_reason"] = "LIQUIDATION_GAP"
                break
        evaluation = validator.evaluate_candidate(
            candidate_record(),
            rows,
            self.config,
            NOW,
        )
        self.assertEqual(
            evaluation["status"],
            "RISK_REJECTED",
        )

    def test_11_profit_factor_handles_no_losses(self):
        self.assertEqual(
            validator.profit_factor([1.0, 0.5]),
            99.0,
        )

    def test_12_max_drawdown_is_positive_magnitude(self):
        self.assertAlmostEqual(
            validator.max_drawdown(
                [1.0, -0.5, -1.0, 0.2]
            ),
            1.5,
        )

    def test_13_bootstrap_is_deterministic(self):
        first = validator.bootstrap_ci(
            [0.1, 0.2, 0.3],
            "C1",
            300,
            0.95,
        )
        second = validator.bootstrap_ci(
            [0.1, 0.2, 0.3],
            "C1",
            300,
            0.95,
        )
        self.assertEqual(first, second)

    def test_14_temporal_folds(self):
        values = list(range(8))
        folds = validator.temporal_fold_means(
            values,
            4,
        )
        self.assertEqual(len(folds), 4)

    def test_15_registry_is_enriched_not_promoted(self):
        self.write_candidate_inputs()
        evaluation = validator.evaluate_candidate(
            candidate_record(),
            pairs(20, 0.1),
            self.config,
            NOW,
        )
        result = validator.enrich_candidate_registry(
            [evaluation],
            NOW,
        )
        registry = json.loads(
            self.paths[
                "CANDIDATE_REGISTRY_PATH"
            ].read_text(encoding="utf-8")
        )
        row = registry["candidates"][0]
        self.assertEqual(row["status"], "CANDIDATE")
        self.assertIn(
            "block6_validation",
            row["metadata"],
        )
        self.assertEqual(
            registry["automatic_promotions"],
            0,
        )
        self.assertEqual(result["enriched_rows"], 1)

    def test_16_promotion_ready_requires_large_strict_sample(self):
        rows = []
        for index in range(180):
            parent = 0.25 if index % 4 else -0.40
            delta = 0.10 if index % 10 else 0.04
            asset = ("SOL", "BTC", "ETH")[index % 3]
            rows.extend(
                [
                    trade(
                        "PARENT",
                        f"G{index}",
                        parent,
                        asset=asset,
                        closed_offset=index,
                    ),
                    trade(
                        "CAND",
                        f"G{index}",
                        parent + delta,
                        asset=asset,
                        closed_offset=index,
                    ),
                ]
            )
        evaluation = validator.evaluate_candidate(
            candidate_record(),
            rows,
            self.config,
            NOW,
        )
        self.assertEqual(
            evaluation["status"],
            "PROMOTION_REVIEW_READY",
        )

    def test_17_promotion_ready_is_only_recommendation(self):
        self.write_candidate_inputs()
        self.write_trades(pairs(20, 0.1))
        result = validator.run_candidate_validation_cycle(
            NOW
        )
        self.assertEqual(result["automatic_promotions"], 0)
        self.assertEqual(result["automatic_retirements"], 0)

    def test_18_history_records_status_change(self):
        self.write_candidate_inputs()
        self.write_trades(pairs(20, 0.1))
        validator.run_candidate_validation_cycle(NOW)
        rows = list(
            csv.DictReader(
                self.paths["HISTORY_PATH"].open(
                    encoding="utf-8"
                )
            )
        )
        self.assertEqual(len(rows), 1)
        self.assertEqual(
            rows[0]["current_status"],
            "INCUBATING",
        )

    def test_19_second_same_status_adds_no_history(self):
        self.write_candidate_inputs()
        self.write_trades(pairs(20, 0.1))
        validator.run_candidate_validation_cycle(NOW)
        validator.run_candidate_validation_cycle(
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

    def test_20_cycle_writes_all_outputs(self):
        self.write_candidate_inputs()
        self.write_trades(pairs(20, 0.1))
        result = validator.run_candidate_validation_cycle(
            NOW
        )
        self.assertEqual(result["status"], "OK")
        for key in (
            "STATE_PATH",
            "EVALUATIONS_PATH",
            "HISTORY_PATH",
            "PROMOTION_REVIEW_PATH",
            "REPORT_PATH",
            "CONFIG_SNAPSHOT_PATH",
        ):
            self.assertTrue(self.paths[key].exists())

    def test_21_candidate_and_parent_states_are_not_modified(self):
        self.write_candidate_inputs()
        before = self.paths[
            "CANDIDATE_STATE_PATH"
        ].read_text(encoding="utf-8")
        self.write_trades(pairs(20, 0.1))
        result = validator.run_candidate_validation_cycle(
            NOW
        )
        after = self.paths[
            "CANDIDATE_STATE_PATH"
        ].read_text(encoding="utf-8")
        self.assertEqual(before, after)
        self.assertFalse(
            result["candidate_state_modified"]
        )
        self.assertFalse(
            result["parent_state_modified"]
        )

    def test_22_safety_defaults_disable_promotion(self):
        self.assertFalse(
            validator.DEFAULT_CONFIG[
                "automatic_promotion"
            ]
        )
        self.assertFalse(
            validator.DEFAULT_CONFIG[
                "automatic_retirement"
            ]
        )
        self.assertTrue(
            validator.DEFAULT_CONFIG["paper_only"]
        )


if __name__ == "__main__":
    unittest.main()
