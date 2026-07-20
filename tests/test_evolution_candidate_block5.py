from __future__ import annotations

import copy
import json
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path
from unittest import mock

import paper_trading_candidate_engine as engine

NOW = datetime(2026, 7, 19, tzinfo=timezone.utc)


def base_config():
    return {
        "initial_capital_eur": 40000.0,
        "monthly_target_eur": 3000.0,
        "target_policy": "MONITOR_ONLY_NEVER_CHASE",
        "risk": {
            "risk_per_trade": 0.005,
            "max_total_open_risk": 0.02,
            "max_daily_loss": 0.02,
            "max_weekly_loss": 0.05,
            "max_monthly_drawdown": 0.10,
            "absolute_max_leverage": 5.0,
            "default_leverage": 3.0,
        },
        "portfolios": [
            {
                "name": "MAIN_ALPHA",
                "enabled": True,
                "is_main": True,
                "strategy": "combo_adaptive",
                "timeframe_minutes": 60,
                "minimum_abs_score": 5.0,
                "leverage": 3.0,
                "reward_risk": 2.0,
                "max_holding_hours": 168,
                "trailing_at_r": 1.0,
                "trailing_atr_multiple": 2.0,
            },
            {
                "name": "SHADOW_BETA",
                "enabled": True,
                "is_main": False,
                "compact_shadow": True,
                "strategy": "combo_adaptive",
                "timeframe_minutes": 60,
                "minimum_abs_score": 5.0,
                "leverage": 3.0,
                "reward_risk": 1.5,
                "max_holding_hours": 24,
                "trailing_at_r": 1.0,
                "trailing_atr_multiple": 2.0,
            },
        ],
    }


def evidence(kind="FIXED_R", params=None, scope="PORTFOLIO", portfolio="SHADOW_BETA", strategy="combo_adaptive", scenario_id="TP_R200", score=90.0, samples=160):
    return {
        "scope": scope,
        "scope_value": portfolio if scope == "PORTFOLIO" else strategy,
        "portfolio": portfolio,
        "strategy": strategy,
        "scenario_set_version": "block3-v1-r-matrix",
        "scenario_id": scenario_id,
        "scenario_kind": kind,
        "scenario_parameters_json": json.dumps(params or {"target_r": 2.0}),
        "sample_eligible": samples,
        "average_delta_r": 0.08,
        "median_delta_r": 0.04,
        "bootstrap_ci_low_delta_r": 0.02,
        "improved_pct": 61.0,
        "evidence_score": score,
        "status": "ELIGIBLE_FOR_MUTATION",
        "decision_summary": "robust evidence",
    }


class Block5Tests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        self.paths = {
            "INPUT_PATH": root / "block4_candidates.json",
            "STATE_PATH": root / "state.json",
            "REGISTRY_PATH": root / "registry.json",
            "EVENTS_PATH": root / "events.csv",
            "REPORT_PATH": root / "report.md",
            "CONFIG_SNAPSHOT_PATH": root / "config_snapshot.json",
            "CONFIG_PATH": root / "config.json",
        }
        self.patchers = [mock.patch.object(engine, name, path) for name, path in self.paths.items()]
        for patcher in self.patchers:
            patcher.start()

    def tearDown(self):
        for patcher in reversed(self.patchers):
            patcher.stop()
        self.tmp.cleanup()

    def write_evidence(self, rows):
        self.paths["INPUT_PATH"].write_text(json.dumps({"candidates": rows}), encoding="utf-8")

    def execute(self, config=None):
        return engine.prepare_candidate_config(config or base_config(), NOW)

    def test_01_no_evidence_keeps_base_unchanged(self):
        base = base_config()
        result = self.execute(base)
        self.assertEqual(result["summary"]["active_candidates"], 0)
        self.assertEqual(result["config"], base)

    def test_02_fixed_r_changes_only_reward_risk(self):
        self.write_evidence([evidence()])
        base = base_config()
        result = self.execute(base)
        child = result["config"]["portfolios"][-1]
        parent = base["portfolios"][1]
        self.assertEqual(child["reward_risk"], 2.0)
        for key, value in parent.items():
            if key == "reward_risk":
                self.assertEqual(child[key], 2.0)
            elif key == "name":
                self.assertNotEqual(child[key], value)
            elif key == "is_main":
                self.assertFalse(child[key])
            else:
                self.assertEqual(child[key], value)

    def test_03_time_exit_changes_only_holding_hours(self):
        self.write_evidence([evidence("TIME_EXIT", {"hours": 12}, scenario_id="TIME_12H")])
        result = self.execute()
        child = result["config"]["portfolios"][-1]
        self.assertEqual(child["max_holding_hours"], 12)
        self.assertEqual(child["reward_risk"], 1.5)

    def test_04_atr_multiple_single_change_allowed(self):
        self.write_evidence([evidence("ATR_TRAIL", {"activation_r": 1.0, "atr_multiple": 3.0}, scenario_id="ATR30_R100")])
        result = self.execute()
        child = result["config"]["portfolios"][-1]
        self.assertEqual(child["trailing_at_r"], 1.0)
        self.assertEqual(child["trailing_atr_multiple"], 3.0)

    def test_05_atr_two_parameter_change_rejected(self):
        self.write_evidence([evidence("ATR_TRAIL", {"activation_r": 0.5, "atr_multiple": 3.0}, scenario_id="ATR30_R050")])
        result = self.execute()
        self.assertEqual(result["summary"]["active_candidates"], 0)
        self.assertEqual(result["summary"]["rejected_evidence"], 1)

    def test_06_mfe_giveback_is_not_approximated(self):
        self.write_evidence([evidence("MFE_GIVEBACK", {"activation_r": 1.0, "giveback_fraction": 0.3}, scenario_id="GB30_R100")])
        result = self.execute()
        self.assertEqual(result["summary"]["new_candidates"], 0)

    def test_07_breakeven_is_not_approximated(self):
        self.write_evidence([evidence("BREAKEVEN", {"activation_r": 1.0}, scenario_id="BE_R100")])
        result = self.execute()
        self.assertEqual(result["summary"]["new_candidates"], 0)

    def test_08_insufficient_samples_ignored(self):
        self.write_evidence([evidence(samples=119)])
        result = self.execute()
        self.assertEqual(result["summary"]["new_candidates"], 0)

    def test_09_low_evidence_score_ignored(self):
        self.write_evidence([evidence(score=77.9)])
        result = self.execute()
        self.assertEqual(result["summary"]["new_candidates"], 0)

    def test_10_noneligible_status_ignored(self):
        row = evidence()
        row["status"] = "ROBUST"
        self.write_evidence([row])
        result = self.execute()
        self.assertEqual(result["summary"]["new_candidates"], 0)

    def test_11_duplicate_is_idempotent(self):
        self.write_evidence([evidence()])
        first = self.execute()
        second = self.execute()
        self.assertEqual(first["summary"]["new_candidates"], 1)
        self.assertEqual(second["summary"]["new_candidates"], 0)
        self.assertEqual(second["summary"]["active_candidates"], 1)

    def test_12_candidates_persist_without_input(self):
        self.write_evidence([evidence()])
        self.execute()
        self.paths["INPUT_PATH"].unlink()
        result = self.execute()
        self.assertEqual(result["summary"]["active_candidates"], 1)

    def test_13_strategy_scope_expands_to_both_parents(self):
        self.write_evidence([evidence(scope="STRATEGY", portfolio="", strategy="combo_adaptive", params={"target_r": 1.0}, scenario_id="TP_R100")])
        result = self.execute()
        self.assertEqual(result["summary"]["new_candidates"], 2)

    def test_14_portfolio_scope_selects_exact_parent(self):
        self.write_evidence([evidence(portfolio="SHADOW_BETA")])
        result = self.execute()
        candidate = next(iter(result["registry"]["candidates"]))
        self.assertEqual(candidate["metadata"]["parent_portfolio"], "SHADOW_BETA")

    def test_15_main_parent_creates_nonmain_candidate(self):
        self.write_evidence([evidence(portfolio="MAIN_ALPHA", params={"target_r": 1.0}, scenario_id="TP_R100")])
        result = self.execute()
        child = result["config"]["portfolios"][-1]
        self.assertFalse(child["is_main"])
        self.assertTrue(child["evolution_candidate"])

    def test_16_recursive_parent_is_rejected(self):
        config = base_config()
        config["portfolios"][1]["evolution_candidate"] = True
        self.write_evidence([evidence()])
        result = self.execute(config)
        self.assertEqual(result["summary"]["new_candidates"], 0)

    def test_17_base_input_is_not_mutated(self):
        base = base_config()
        original = copy.deepcopy(base)
        self.write_evidence([evidence()])
        self.execute(base)
        self.assertEqual(base, original)

    def test_18_candidate_name_is_deterministic(self):
        self.write_evidence([evidence()])
        first = self.execute()["config"]["portfolios"][-1]["name"]
        self.paths["STATE_PATH"].unlink()
        self.paths["REGISTRY_PATH"].unlink()
        second = self.execute()["config"]["portfolios"][-1]["name"]
        self.assertEqual(first, second)

    def test_19_candidate_name_respects_limit(self):
        cfg = engine.DEFAULT_CONFIG.copy()
        cfg["maximum_candidate_name_length"] = 40
        self.paths["CONFIG_PATH"].write_text(json.dumps(cfg), encoding="utf-8")
        self.write_evidence([evidence()])
        name = self.execute()["config"]["portfolios"][-1]["name"]
        self.assertLessEqual(len(name), 40)

    def test_20_registry_has_zero_promotions(self):
        self.write_evidence([evidence()])
        registry = self.execute()["registry"]
        self.assertEqual(registry["automatic_promotions"], 0)
        self.assertFalse(registry["live_modified"])

    def test_21_parent_risk_and_leverage_are_preserved(self):
        self.write_evidence([evidence()])
        child = self.execute()["config"]["portfolios"][-1]
        parent = base_config()["portfolios"][1]
        self.assertEqual(child["leverage"], parent["leverage"])
        self.assertEqual(child["minimum_abs_score"], parent["minimum_abs_score"])
        self.assertEqual(child["timeframe_minutes"], parent["timeframe_minutes"])

    def test_22_exactly_one_main_remains(self):
        self.write_evidence([evidence(portfolio="MAIN_ALPHA")])
        portfolios = self.execute()["config"]["portfolios"]
        self.assertEqual(sum(bool(row.get("is_main")) for row in portfolios), 1)


if __name__ == "__main__":
    unittest.main()
