from __future__ import annotations
import csv
import json
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path
from unittest import mock

import paper_trading_evolution_memory as memory

NOW = datetime(2026, 7, 20, tzinfo=timezone.utc)


def candidate(cid="C1", status="CANDIDATE"):
    return {
        "candidate_id": cid,
        "strategy_id": cid,
        "family_id": "trend",
        "portfolio_name": f"PORT-{cid}",
        "status": status,
        "mutation": {
            "parameter": "reward_risk",
            "old_value": 1.5,
            "new_value": 2.0,
            "mutation_type": "single_parameter",
        },
        "source_evidence": {
            "scenario_kind": "FIXED_R",
            "evidence_score": 85,
        },
    }


def validation(cid="C1", status="PROMOTION_REVIEW_READY", pairs=180, delta=0.10):
    return {
        "candidate_id": cid,
        "status": status,
        "matched_pairs": str(pairs),
        "mean_delta_r": str(delta),
        "validation_score": "90",
        "candidate_expectancy_r": "0.25",
        "candidate_profit_factor": "1.6",
        "candidate_win_rate": "0.58",
        "candidate_max_drawdown_r": "2.0",
        "candidate_liquidations": "0",
        "bootstrap_ci_low_r": "0.03",
        "positive_folds": "4",
    }


class Block9Tests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        root = Path(self.temp.name)
        names = {
            "CONFIG_PATH": "config.json",
            "CANDIDATE_STATE": "candidate_state.json",
            "CANDIDATE_REGISTRY": "candidate_registry.json",
            "VALIDATIONS": "validations.csv",
            "PROMOTIONS": "promotions.json",
            "POST_PROMOTION": "post.csv",
            "TRADE_LOG": "trades.csv",
            "STATE": "state.json",
            "SCORES": "scores.csv",
            "HALL_JSON": "hall.json",
            "HALL_CSV": "hall.csv",
            "MEMORY_JSON": "memory.json",
            "MEMORY_CSV": "memory.csv",
            "HISTORY": "history.csv",
            "REPORT": "report.md",
            "CONFIG_SNAPSHOT": "snapshot.json",
        }
        self.paths = {key: root / value for key, value in names.items()}
        self.patchers = [
            mock.patch.object(memory, key, value)
            for key, value in self.paths.items()
        ]
        for patcher in self.patchers:
            patcher.start()
        self.config = dict(memory.DEFAULT_CONFIG)

    def tearDown(self):
        for patcher in reversed(self.patchers):
            patcher.stop()
        self.temp.cleanup()

    def write_csv(self, path, rows):
        if not rows:
            path.write_text("", encoding="utf-8")
            return
        fields = sorted({key for row in rows for key in row})
        with path.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fields)
            writer.writeheader()
            writer.writerows(rows)

    def inputs(self, candidates=None, validations=None, promotions=None, posts=None):
        candidates = candidates or []
        self.paths["CANDIDATE_STATE"].write_text(
            json.dumps({"candidates": {row["candidate_id"]: row for row in candidates}}),
            encoding="utf-8",
        )
        self.paths["CANDIDATE_REGISTRY"].write_text(
            json.dumps({
                "candidates": [{
                    "strategy_id": row["candidate_id"],
                    "family_id": row["family_id"],
                    "status": row["status"],
                    "mutation": row["mutation"],
                    "metadata": {"source_evidence": row["source_evidence"]},
                } for row in candidates]
            }),
            encoding="utf-8",
        )
        self.write_csv(self.paths["VALIDATIONS"], validations or [])
        self.paths["PROMOTIONS"].write_text(
            json.dumps(promotions or {"transactions": [], "active_by_family": {}}),
            encoding="utf-8",
        )
        self.write_csv(self.paths["POST_PROMOTION"], posts or [])
        self.write_csv(self.paths["TRADE_LOG"], [])

    def test_01_empty_cycle(self):
        self.inputs()
        result = memory.run_evolution_memory_cycle(NOW)
        self.assertEqual(result["status"], "OK")
        self.assertEqual(result["memory_records"], 0)

    def test_02_direction(self):
        self.assertEqual(memory.direction(1, 2), "INCREASE")
        self.assertEqual(memory.direction(2, 1), "DECREASE")

    def test_03_bucket(self):
        self.assertEqual(memory.target_bucket("reward_risk", 1.76), "2")

    def test_04_signature_stable(self):
        self.assertEqual(
            memory.mutation_signature("Trend", "fixed_r", "reward_risk", 1.5, 2),
            memory.mutation_signature("Trend", "FIXED_R", "reward_risk", 1.5, 2),
        )

    def test_05_score_bounded(self):
        row = memory.score_strategy(
            "C1", "trend", "P", "MASTER", "TEST", 100,
            validation(), {"status": "HEALTHY"}, {}, self.config, NOW,
        )
        self.assertGreaterEqual(row["evolution_score"], 0)
        self.assertLessEqual(row["evolution_score"], 100)

    def test_06_master_hall_eligible(self):
        row = memory.score_strategy(
            "C1", "trend", "P", "MASTER", "TEST", 0,
            None, None, {}, self.config, NOW,
        )
        self.assertTrue(row["hall_eligible"])

    def test_07_candidate_not_eligible_at_79(self):
        row = memory.score_strategy(
            "C1", "trend", "P", "CANDIDATE", "TEST", 80,
            validation(pairs=79), None, {}, self.config, NOW,
        )
        self.assertFalse(row["hall_eligible"])

    def test_08_one_trial_insufficient(self):
        rows = memory.build_memory(
            {"candidates": {"C1": candidate()}},
            {"C1": validation(pairs=40)}, {}, set(), {}, self.config, NOW,
        )
        family = next(row for row in rows if row["scope"] == "FAMILY")
        self.assertEqual(family["status"], "INSUFFICIENT")

    def test_09_repeated_success_favor(self):
        candidates = {"C1": candidate("C1"), "C2": candidate("C2")}
        vals = {"C1": validation("C1"), "C2": validation("C2")}
        promotions = {
            "C1": {"status": "EXECUTED"},
            "C2": {"status": "EXECUTED"},
        }
        posts = {
            "C1": {"status": "HEALTHY"},
            "C2": {"status": "HEALTHY"},
        }
        rows = memory.build_memory(
            {"candidates": candidates}, vals, promotions, set(), posts, self.config, NOW,
        )
        family = next(row for row in rows if row["scope"] == "FAMILY")
        self.assertEqual(family["status"], "FAVOR")

    def test_10_critical_avoid_and_block(self):
        rows = memory.build_memory(
            {"candidates": {"C1": candidate()}},
            {"C1": validation()}, {"C1": {"status": "EXECUTED"}},
            set(), {"C1": {"status": "CRITICAL"}}, self.config, NOW,
        )
        family = next(row for row in rows if row["scope"] == "FAMILY")
        self.assertEqual(family["status"], "AVOID")
        self.assertTrue(family["block_new_candidates"])

    def test_11_no_history_allows(self):
        self.paths["MEMORY_JSON"].write_text(json.dumps({"records": {}}), encoding="utf-8")
        decision = memory.mutation_policy_decision(
            {"strategy": "trend"},
            {"scenario_kind": "FIXED_R", "parameter": "reward_risk",
             "old_value": 1.5, "new_value": 2.0},
        )
        self.assertTrue(decision["allow"])

    def test_12_avoid_blocks(self):
        signature = memory.mutation_signature(
            "trend", "FIXED_R", "reward_risk", 1.5, 2.0
        )
        self.paths["MEMORY_JSON"].write_text(
            json.dumps({"records": {signature: {
                "signature": signature, "scope": "FAMILY",
                "status": "AVOID", "memory_score": 10,
                "block_new_candidates": True,
            }}}),
            encoding="utf-8",
        )
        decision = memory.mutation_policy_decision(
            {"strategy": "trend"},
            {"scenario_kind": "FIXED_R", "parameter": "reward_risk",
             "old_value": 1.5, "new_value": 2.0},
        )
        self.assertFalse(decision["allow"])

    def test_13_family_precedes_global(self):
        family = memory.mutation_signature(
            "trend", "FIXED_R", "reward_risk", 1.5, 2
        )
        global_id = memory.mutation_signature(
            "GLOBAL", "FIXED_R", "reward_risk", 1.5, 2
        )
        self.paths["MEMORY_JSON"].write_text(
            json.dumps({"records": {
                family: {"signature": family, "scope": "FAMILY",
                         "status": "FAVOR", "memory_score": 90,
                         "block_new_candidates": False},
                global_id: {"signature": global_id, "scope": "GLOBAL",
                            "status": "AVOID", "memory_score": 10,
                            "block_new_candidates": True},
            }}),
            encoding="utf-8",
        )
        decision = memory.mutation_policy_decision(
            {"strategy": "trend"},
            {"scenario_kind": "FIXED_R", "parameter": "reward_risk",
             "old_value": 1.5, "new_value": 2.0},
        )
        self.assertTrue(decision["allow"])
        self.assertEqual(decision["scope"], "FAMILY")

    def test_14_registry_status_unchanged(self):
        self.inputs([candidate()], [validation()])
        score = memory.score_strategy(
            "C1", "trend", "PORT-C1", "CANDIDATE", "TEST",
            85, validation(), None, {}, self.config, NOW,
        )
        memory.enrich_registry([score], [], NOW)
        registry = json.loads(
            self.paths["CANDIDATE_REGISTRY"].read_text(encoding="utf-8")
        )
        self.assertEqual(registry["candidates"][0]["status"], "CANDIDATE")

    def test_15_all_outputs_written(self):
        self.inputs([candidate()], [validation(pairs=40)])
        memory.run_evolution_memory_cycle(NOW)
        for key in (
            "STATE", "SCORES", "HALL_JSON", "HALL_CSV", "MEMORY_JSON",
            "MEMORY_CSV", "HISTORY", "REPORT", "CONFIG_SNAPSHOT",
        ):
            self.assertTrue(self.paths[key].exists())

    def test_16_candidate_state_unchanged(self):
        self.inputs([candidate()], [validation(pairs=40)])
        before = self.paths["CANDIDATE_STATE"].read_text(encoding="utf-8")
        result = memory.run_evolution_memory_cycle(NOW)
        after = self.paths["CANDIDATE_STATE"].read_text(encoding="utf-8")
        self.assertEqual(before, after)
        self.assertFalse(result["candidate_state_modified"])

    def test_17_no_automatic_actions(self):
        self.inputs()
        result = memory.run_evolution_memory_cycle(NOW)
        self.assertEqual(result["automatic_mutations"], 0)
        self.assertEqual(result["automatic_promotions"], 0)
        self.assertFalse(result["live_modified"])
        self.assertFalse(result["orders_sent"])

    def test_18_hall_ranking(self):
        rows = [
            {"strategy_id": "A", "lifecycle_status": "MASTER",
             "hall_eligible": True, "evolution_score": 90,
             "matched_pairs": 100, "closed_trades": 100},
            {"strategy_id": "B", "lifecycle_status": "MASTER",
             "hall_eligible": True, "evolution_score": 80,
             "matched_pairs": 100, "closed_trades": 100},
        ]
        categories, _ = memory.hall_categories(rows, self.config, NOW)
        self.assertEqual(categories["ALL_TIME"][0]["strategy_id"], "A")

    def test_19_history_not_duplicated(self):
        self.inputs([candidate()], [validation(pairs=40)])
        memory.run_evolution_memory_cycle(NOW)
        first = list(csv.DictReader(self.paths["HISTORY"].open(encoding="utf-8")))
        memory.run_evolution_memory_cycle(NOW)
        second = list(csv.DictReader(self.paths["HISTORY"].open(encoding="utf-8")))
        self.assertEqual(len(first), len(second))

    def test_20_disabled_policy_allows(self):
        self.paths["CONFIG_PATH"].write_text(
            json.dumps({"candidate_policy_enabled": False}),
            encoding="utf-8",
        )
        decision = memory.mutation_policy_decision(
            {"strategy": "trend"},
            {"scenario_kind": "FIXED_R", "parameter": "reward_risk",
             "old_value": 1.5, "new_value": 2.0},
        )
        self.assertTrue(decision["allow"])
        self.assertEqual(decision["status"], "DISABLED")


if __name__ == "__main__":
    unittest.main()
