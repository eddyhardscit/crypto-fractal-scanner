from __future__ import annotations
import csv
import json
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path
from unittest import mock

import paper_trading_regime_evolution as regime

NOW = datetime(2026, 7, 20, 12, 0, tzinfo=timezone.utc)


def trade(index: int, opened: str, value: float, portfolio: str = "P1", liquidation: bool = False):
    return {
        "trade_id": f"T{index}",
        "portfolio": portfolio,
        "opened_at": opened,
        "closed_at": "2026-07-21T00:00:00+00:00",
        "r_multiple": str(value),
        "close_reason": "LIQUIDATION" if liquidation else "TARGET",
    }


class Block10Tests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        root = Path(self.temp.name)
        names = {
            "CONFIG_PATH": "config.json",
            "MARKET_LATEST": "latest.json",
            "MARKET_HISTORY": "history_input.csv",
            "TRADE_LOG": "trades.csv",
            "CANDIDATE_STATE": "candidate_state.json",
            "CANDIDATE_REGISTRY": "candidate_registry.json",
            "EVOLUTION_SCORES": "scores_input.csv",
            "STATE": "state.json",
            "PERFORMANCE": "performance.csv",
            "LEADERBOARD": "leaderboard.json",
            "MEMORY": "memory.json",
            "HISTORY": "history.csv",
            "REPORT": "report.md",
            "CONFIG_SNAPSHOT": "snapshot.json",
        }
        self.paths = {key: root / value for key, value in names.items()}
        self.patchers = [mock.patch.object(regime, key, value) for key, value in self.paths.items()]
        for patcher in self.patchers:
            patcher.start()
        self.paths["CANDIDATE_STATE"].write_text(json.dumps({"candidates": {}}), encoding="utf-8")
        self.paths["CANDIDATE_REGISTRY"].write_text(json.dumps({"candidates": []}), encoding="utf-8")
        self.write_csv(self.paths["EVOLUTION_SCORES"], [])

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

    def timeline(self):
        rows = [
            {"generated_utc": "2026-07-01T00:00:00+00:00", "regime": "BULL"},
            {"generated_utc": "2026-07-10T00:00:00+00:00", "regime": "BEAR"},
        ]
        self.write_csv(self.paths["MARKET_HISTORY"], rows)
        return regime.load_timeline()

    def test_01_crash_mapping(self):
        self.assertEqual(regime.canonical_regime({"state": "capitulation crash"}), "CRASH")

    def test_02_recovery_mapping(self):
        self.assertEqual(regime.canonical_regime({"state": "recovery"}), "RECOVERY")

    def test_03_high_vol_mapping(self):
        self.assertEqual(regime.canonical_regime({"level": "HIGH_VOL"}), "HIGH_VOLATILITY")

    def test_04_bull_mapping(self):
        self.assertEqual(regime.canonical_regime({"trend": "bull"}), "BULL_TREND")

    def test_05_bear_mapping(self):
        self.assertEqual(regime.canonical_regime({"trend": "bear"}), "BEAR_TREND")

    def test_06_range_mapping(self):
        self.assertEqual(regime.canonical_regime({"state": "sideways"}), "RANGE")

    def test_07_unknown_mapping(self):
        self.assertEqual(regime.canonical_regime({"foo": "bar"}), "UNKNOWN")

    def test_08_timeline_prior_assignment(self):
        timeline = self.timeline()
        moment = regime.parse_time("2026-07-05T00:00:00+00:00")
        self.assertEqual(regime.regime_at(moment, timeline), "BULL_TREND")

    def test_09_no_future_leakage(self):
        timeline = self.timeline()
        moment = regime.parse_time("2026-06-30T00:00:00+00:00")
        self.assertEqual(regime.regime_at(moment, timeline), "UNKNOWN")

    def test_10_fitness_is_bounded(self):
        value = regime.fitness([1.0] * 100, 0)["fitness_score"]
        self.assertGreaterEqual(value, 0)
        self.assertLessEqual(value, 100)

    def test_11_small_sample_insufficient(self):
        metrics = regime.fitness([0.2] * 9, 0)
        self.assertEqual(regime.classify(metrics, regime.DEFAULT_CONFIG), "INSUFFICIENT")

    def test_12_observing_between_10_and_29(self):
        metrics = regime.fitness([0.2] * 15, 0)
        self.assertEqual(regime.classify(metrics, regime.DEFAULT_CONFIG), "OBSERVING")

    def test_13_strong_sample_specialist(self):
        metrics = regime.fitness([0.5] * 60, 0)
        self.assertEqual(regime.classify(metrics, regime.DEFAULT_CONFIG), "SPECIALIST")

    def test_14_two_liquidations_avoid(self):
        metrics = regime.fitness([0.2] * 40, 2)
        self.assertEqual(regime.classify(metrics, regime.DEFAULT_CONFIG), "AVOID")

    def test_15_performance_groups_by_entry_regime(self):
        timeline = self.timeline()
        trades = [
            trade(1, "2026-07-05T00:00:00+00:00", 1.0),
            trade(2, "2026-07-12T00:00:00+00:00", -1.0),
        ]
        rows = regime.build_performance(trades, timeline, regime.DEFAULT_CONFIG, NOW)
        regimes = {row["regime"] for row in rows if row["scope"] == "PORTFOLIO"}
        self.assertEqual(regimes, {"BULL_TREND", "BEAR_TREND"})

    def test_16_memory_created_per_family_and_regime(self):
        row = {
            "scope": "FAMILY", "family_id": "trend", "regime": "BULL_TREND",
            "status": "COMPATIBLE", "fitness_score": 65, "closed_trades": 40,
            "expectancy_r": 0.1, "profit_factor": 1.3,
        }
        document = regime.build_regime_memory([row], "BULL_TREND", regime.DEFAULT_CONFIG, NOW)
        self.assertIn("trend|BULL_TREND", document["records"])

    def test_17_avoid_memory_is_advisory_by_default(self):
        row = {
            "scope": "FAMILY", "family_id": "trend", "regime": "BEAR_TREND",
            "status": "AVOID", "fitness_score": 10, "closed_trades": 100,
            "expectancy_r": -0.2, "profit_factor": 0.5,
        }
        document = regime.build_regime_memory([row], "BEAR_TREND", regime.DEFAULT_CONFIG, NOW)
        self.assertFalse(document["records"]["trend|BEAR_TREND"]["block_new_candidates"])

    def test_18_blocking_requires_explicit_config(self):
        cfg = dict(regime.DEFAULT_CONFIG)
        cfg["candidate_blocking_enabled"] = True
        row = {
            "scope": "FAMILY", "family_id": "trend", "regime": "BEAR_TREND",
            "status": "AVOID", "fitness_score": 10, "closed_trades": 100,
            "expectancy_r": -0.2, "profit_factor": 0.5,
        }
        document = regime.build_regime_memory([row], "BEAR_TREND", cfg, NOW)
        self.assertTrue(document["records"]["trend|BEAR_TREND"]["block_new_candidates"])

    def test_19_policy_unknown_is_permissive(self):
        decision = regime.regime_candidate_policy_decision({"strategy": "trend"})
        self.assertTrue(decision["allow"])

    def test_20_policy_reads_favor_memory(self):
        self.paths["MARKET_LATEST"].write_text(json.dumps({"regime": "BULL"}), encoding="utf-8")
        self.paths["MEMORY"].write_text(json.dumps({"records": {
            "trend|BULL_TREND": {
                "status": "FAVOR", "fitness_score": 80,
                "closed_trades": 100, "block_new_candidates": False,
            }
        }}), encoding="utf-8")
        decision = regime.regime_candidate_policy_decision({"strategy": "trend"})
        self.assertTrue(decision["allow"])
        self.assertEqual(decision["status"], "FAVOR")

    def test_21_policy_can_block_when_record_is_blocked(self):
        self.paths["MARKET_LATEST"].write_text(json.dumps({"regime": "BEAR"}), encoding="utf-8")
        self.paths["MEMORY"].write_text(json.dumps({"records": {
            "trend|BEAR_TREND": {
                "status": "AVOID", "fitness_score": 10,
                "closed_trades": 100, "block_new_candidates": True,
            }
        }}), encoding="utf-8")
        decision = regime.regime_candidate_policy_decision({"strategy": "trend"})
        self.assertFalse(decision["allow"])

    def test_22_cycle_writes_all_outputs(self):
        self.paths["MARKET_LATEST"].write_text(json.dumps({"regime": "RANGE"}), encoding="utf-8")
        self.write_csv(self.paths["MARKET_HISTORY"], [])
        self.write_csv(self.paths["TRADE_LOG"], [])
        result = regime.run_regime_evolution_cycle(NOW)
        self.assertEqual(result["status"], "OK")
        for key in ("STATE", "PERFORMANCE", "LEADERBOARD", "MEMORY", "HISTORY", "REPORT", "CONFIG_SNAPSHOT"):
            self.assertTrue(self.paths[key].exists())

    def test_23_candidate_registry_status_unchanged(self):
        self.paths["CANDIDATE_REGISTRY"].write_text(json.dumps({"candidates": [{
            "strategy_id": "C1", "status": "CANDIDATE", "portfolio_name": "P1", "metadata": {}
        }]}), encoding="utf-8")
        regime.enrich_registry([], {"regime": "RANGE"}, NOW)
        value = json.loads(self.paths["CANDIDATE_REGISTRY"].read_text(encoding="utf-8"))
        self.assertEqual(value["candidates"][0]["status"], "CANDIDATE")

    def test_24_no_automatic_actions(self):
        self.paths["MARKET_LATEST"].write_text(json.dumps({"regime": "RANGE"}), encoding="utf-8")
        self.write_csv(self.paths["MARKET_HISTORY"], [])
        self.write_csv(self.paths["TRADE_LOG"], [])
        result = regime.run_regime_evolution_cycle(NOW)
        self.assertEqual(result["automatic_switches"], 0)
        self.assertEqual(result["automatic_position_changes"], 0)
        self.assertFalse(result["live_modified"])
        self.assertFalse(result["orders_sent"])


if __name__ == "__main__":
    unittest.main()
