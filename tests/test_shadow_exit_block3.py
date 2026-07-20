from __future__ import annotations

import json
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path
from unittest.mock import patch

import pandas as pd

import paper_trading_shadow_exit as shadow


class ShadowExitBlock3Tests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.cwd = patch("os.getcwd", return_value=self.temp.name)
        self.old_paths = {
            name: getattr(shadow, name)
            for name in (
                "REPORTS_DIR", "STATE_PATH", "EVENTS_PATH", "RESULTS_PATH",
                "METRICS_PATH", "REPORT_PATH", "CONFIG_SNAPSHOT_PATH",
                "CONFIG_PATH", "TRADE_LOG_PATH",
            )
        }
        root = Path(self.temp.name)
        shadow.REPORTS_DIR = root / "reports"
        shadow.STATE_PATH = shadow.REPORTS_DIR / "paper_trading_shadow_exit_state.json"
        shadow.EVENTS_PATH = shadow.REPORTS_DIR / "paper_trading_shadow_exit_events.csv"
        shadow.RESULTS_PATH = shadow.REPORTS_DIR / "paper_trading_shadow_exit_results.csv"
        shadow.METRICS_PATH = shadow.REPORTS_DIR / "paper_trading_shadow_exit_metrics.csv"
        shadow.REPORT_PATH = shadow.REPORTS_DIR / "paper_trading_shadow_exit_report.md"
        shadow.CONFIG_SNAPSHOT_PATH = shadow.REPORTS_DIR / "paper_trading_shadow_exit_config_snapshot.json"
        shadow.CONFIG_PATH = root / "config/shadow_exit_block3.json"
        shadow.TRADE_LOG_PATH = shadow.REPORTS_DIR / "paper_trading_trade_log.csv"
        shadow.CONFIG_PATH.parent.mkdir(parents=True)
        shadow.CONFIG_PATH.write_text(json.dumps(shadow.DEFAULT_CONFIG), encoding="utf-8")

    def tearDown(self) -> None:
        for name, value in self.old_paths.items():
            setattr(shadow, name, value)
        self.temp.cleanup()

    @staticmethod
    def paper_config() -> dict:
        return {
            "execution": {
                "taker_fee_bps": 0.0,
                "default_slippage_bps": 0.0,
                "illiquid_slippage_bps": 0.0,
            },
            "universe": {"minimum_turnover_24h_usdt": 0.0},
        }

    @staticmethod
    def bundle(price: float = 100.0) -> dict:
        return {
            "eur_usdt_rate": 1.0,
            "assets": {
                "BTC": {
                    "mark_price": price,
                    "turnover_24h": 1_000_000_000,
                }
            },
        }

    @staticmethod
    def position(opened_at: str = "2026-07-19T10:00:00+00:00") -> dict:
        return {
            "trade_id": "T1",
            "portfolio": "P1",
            "strategy": "S1",
            "asset": "BTC",
            "symbol": "BTC-USDT",
            "side": "LONG",
            "timeframe_minutes": 15,
            "opened_at": opened_at,
            "entry_price": 100.0,
            "quantity": 1.0,
            "margin_eur": 10.0,
            "initial_risk_eur": 10.0,
            "initial_stop_price": 90.0,
            "stop_price": 90.0,
            "liquidation_price": 80.0,
            "entry_fee_eur": 0.0,
            "eur_usdt_rate": 1.0,
            "atr_pct": 2.0,
            "max_holding_hours": 24.0,
        }

    def group_with(self, definition: dict) -> tuple[dict, dict]:
        cfg = dict(shadow.DEFAULT_CONFIG)
        cfg["scenarios"] = [definition]
        group = shadow.create_group(
            self.position(), "P1", cfg, "", "FULL_FROM_ENTRY"
        )
        return group, group["scenarios"][definition["id"]]

    def candle(self, open_: float, high: float, low: float, close: float) -> pd.Series:
        return pd.Series({"open": open_, "high": high, "low": low, "close": close})

    def test_fixed_target_and_stop_same_candle_is_conservative(self) -> None:
        group, scenario = self.group_with(
            {"id": "TP1", "kind": "FIXED_R", "target_r": 1.0}
        )
        event = shadow.process_scenario_candle(
            group,
            scenario,
            datetime(2026, 7, 19, 10, 15, tzinfo=timezone.utc),
            self.candle(100, 111, 89, 100),
            self.bundle(),
            self.paper_config(),
        )
        self.assertIsNotNone(event)
        self.assertEqual(scenario["exit_reason"], "INITIAL_PROTECTIVE_STOP")
        self.assertEqual(scenario["same_candle_ambiguity_count"], 1)
        self.assertAlmostEqual(scenario["comparable_pnl_eur"], -10.0)

    def test_giveback_activation_does_not_exit_on_activation_candle(self) -> None:
        group, scenario = self.group_with(
            {
                "id": "GB",
                "kind": "MFE_GIVEBACK",
                "activation_r": 0.5,
                "giveback_fraction": 0.2,
            }
        )
        first = shadow.process_scenario_candle(
            group,
            scenario,
            datetime(2026, 7, 19, 10, 15, tzinfo=timezone.utc),
            self.candle(100, 110, 100, 108),
            self.bundle(),
            self.paper_config(),
        )
        self.assertIsNone(first)
        self.assertTrue(scenario["activated"])
        self.assertAlmostEqual(scenario["stop_price"], 108.0)

        second = shadow.process_scenario_candle(
            group,
            scenario,
            datetime(2026, 7, 19, 10, 30, tzinfo=timezone.utc),
            self.candle(108, 109, 107, 107.5),
            self.bundle(),
            self.paper_config(),
        )
        self.assertIsNotNone(second)
        self.assertEqual(scenario["exit_reason"], "MFE_GIVEBACK")
        self.assertAlmostEqual(scenario["comparable_pnl_eur"], 8.0)

    def test_breakeven_becomes_active_next_candle(self) -> None:
        group, scenario = self.group_with(
            {"id": "BE", "kind": "BREAKEVEN", "activation_r": 0.5}
        )
        event = shadow.process_scenario_candle(
            group,
            scenario,
            datetime(2026, 7, 19, 10, 15, tzinfo=timezone.utc),
            self.candle(100, 106, 95, 105),
            self.bundle(),
            self.paper_config(),
        )
        self.assertIsNone(event)
        self.assertTrue(scenario["activated"])
        self.assertAlmostEqual(scenario["stop_price"], 100.0)

        event = shadow.process_scenario_candle(
            group,
            scenario,
            datetime(2026, 7, 19, 10, 30, tzinfo=timezone.utc),
            self.candle(105, 106, 99, 100),
            self.bundle(),
            self.paper_config(),
        )
        self.assertIsNotNone(event)
        self.assertEqual(scenario["exit_reason"], "BREAKEVEN_STOP")
        self.assertAlmostEqual(scenario["comparable_pnl_eur"], 0.0)

    def test_atr_trail_uses_next_candle_stop(self) -> None:
        group, scenario = self.group_with(
            {
                "id": "ATR",
                "kind": "ATR_TRAIL",
                "activation_r": 1.0,
                "atr_multiple": 2.0,
            }
        )
        event = shadow.process_scenario_candle(
            group,
            scenario,
            datetime(2026, 7, 19, 10, 15, tzinfo=timezone.utc),
            self.candle(100, 112, 100, 110),
            self.bundle(),
            self.paper_config(),
        )
        self.assertIsNone(event)
        self.assertTrue(scenario["activated"])
        self.assertAlmostEqual(scenario["stop_price"], 105.6)

    def test_actual_comparison_excludes_funding_on_both_sides(self) -> None:
        group, scenario = self.group_with(
            {"id": "TP1", "kind": "FIXED_R", "target_r": 1.0}
        )
        shadow.close_scenario(
            group,
            scenario,
            110.0,
            "FIXED_R_TARGET",
            datetime(2026, 7, 19, 11, 0, tzinfo=timezone.utc),
            self.bundle(),
            self.paper_config(),
        )
        shadow.attach_actual(
            group,
            {
                "closed_at": "2026-07-19T11:30:00+00:00",
                "exit_price": 108.0,
                "net_pnl_eur": 9.0,
                "funding_pnl_eur": 1.0,
                "holding_hours": 1.5,
                "close_reason": "TARGET",
            },
        )
        row = shadow.result_row(group, scenario, 0.01)
        self.assertIsNotNone(row)
        self.assertAlmostEqual(row["actual_comparable_pnl_eur"], 8.0)
        self.assertAlmostEqual(row["shadow_comparable_pnl_eur"], 10.0)
        self.assertAlmostEqual(row["delta_vs_actual_eur"], 2.0)
        self.assertEqual(row["timing_assessment"], "EARLIER_BETTER")

    def test_timing_classification_all_four_directions(self) -> None:
        actual = datetime(2026, 7, 19, 12, 0, tzinfo=timezone.utc)
        self.assertEqual(
            shadow.timing_labels(actual, actual - timedelta(hours=1), 5.0, 0.01)[1],
            "EARLIER_BETTER",
        )
        self.assertEqual(
            shadow.timing_labels(actual, actual - timedelta(hours=1), -5.0, 0.01)[1],
            "TOO_EARLY",
        )
        self.assertEqual(
            shadow.timing_labels(actual, actual + timedelta(hours=1), 5.0, 0.01)[1],
            "LATER_BETTER",
        )
        self.assertEqual(
            shadow.timing_labels(actual, actual + timedelta(hours=1), -5.0, 0.01)[1],
            "TOO_LATE",
        )

    def test_legacy_open_position_is_partial(self) -> None:
        config = dict(shadow.DEFAULT_CONFIG)
        config["scenarios"] = [{"id": "TP1", "kind": "FIXED_R", "target_r": 1.0}]
        state = {"portfolios": {"P1": {"open_positions": [self.position()]}}}
        shadow_state = {"groups": {}}
        events = []
        frame = pd.DataFrame(
            [{"open": 100, "high": 101, "low": 99, "close": 100}],
            index=[pd.Timestamp("2026-07-19T10:15:00Z")],
        )
        shadow.reconcile_open_groups(
            shadow_state,
            state,
            {"opened": []},
            {"BTC": {15: frame}},
            config,
            events,
        )
        group = shadow_state["groups"]["P1:T1"]
        self.assertFalse(group["full_from_entry"])
        self.assertEqual(group["observation_quality"], "PARTIAL_FROM_BLOCK3_ACTIVATION")

    def test_newly_opened_position_is_full_from_entry(self) -> None:
        config = dict(shadow.DEFAULT_CONFIG)
        config["scenarios"] = [{"id": "TP1", "kind": "FIXED_R", "target_r": 1.0}]
        position = self.position()
        state = {"portfolios": {"P1": {"open_positions": [position]}}}
        shadow_state = {"groups": {}}
        events = []
        frame = pd.DataFrame(
            [{"open": 100, "high": 101, "low": 99, "close": 100}],
            index=[pd.Timestamp("2026-07-19T10:15:00Z")],
        )
        shadow.reconcile_open_groups(
            shadow_state,
            state,
            {"opened": [position]},
            {"BTC": {15: frame}},
            config,
            events,
        )
        group = shadow_state["groups"]["P1:T1"]
        self.assertTrue(group["full_from_entry"])
        self.assertEqual(group["observation_quality"], "FULL_FROM_ENTRY")

    def test_metric_stage_is_not_statistical_promotion(self) -> None:
        self.assertEqual(shadow.data_stage(0), "WAITING_FULL_SAMPLE")
        self.assertEqual(shadow.data_stage(9), "COLLECTING")
        self.assertEqual(shadow.data_stage(29), "PRELIMINARY_SAMPLE")
        self.assertEqual(shadow.data_stage(30), "READY_FOR_BLOCK4_EVALUATION")

    def test_end_to_end_shadow_result_waits_for_actual_close(self) -> None:
        config = dict(shadow.DEFAULT_CONFIG)
        config["scenarios"] = [
            {"id": "TP1", "kind": "FIXED_R", "target_r": 1.0}
        ]
        shadow.CONFIG_PATH.write_text(json.dumps(config), encoding="utf-8")
        position = self.position()
        paper_state = {
            "portfolios": {"P1": {"open_positions": [position]}}
        }
        first_frame = pd.DataFrame(
            [{"open": 100, "high": 101, "low": 99, "close": 100}],
            index=[pd.Timestamp("2026-07-19T10:15:00Z")],
        )
        with patch.object(
            shadow, "bundle_frames", return_value={"BTC": {15: first_frame}}
        ):
            first = shadow.run_shadow_exit_cycle(
                {"opened": [position], "closed": []},
                paper_state,
                self.bundle(),
                self.paper_config(),
                datetime(2026, 7, 19, 10, 16, tzinfo=timezone.utc),
            )
        self.assertEqual(first["active_groups"], 1)
        self.assertEqual(first["new_results"], 0)

        second_frame = pd.DataFrame(
            [
                {"open": 100, "high": 101, "low": 99, "close": 100},
                {"open": 100, "high": 111, "low": 100, "close": 110},
            ],
            index=[
                pd.Timestamp("2026-07-19T10:15:00Z"),
                pd.Timestamp("2026-07-19T10:30:00Z"),
            ],
        )
        with patch.object(
            shadow, "bundle_frames", return_value={"BTC": {15: second_frame}}
        ):
            second = shadow.run_shadow_exit_cycle(
                {"opened": [], "closed": []},
                paper_state,
                self.bundle(110),
                self.paper_config(),
                datetime(2026, 7, 19, 10, 31, tzinfo=timezone.utc),
            )
        self.assertEqual(second["new_results"], 0)
        self.assertEqual(second["active_scenarios"], 0)
        self.assertEqual(second["active_groups"], 1)

        closed = {
            **position,
            "closed_at": "2026-07-19T10:45:00+00:00",
            "exit_price": 105.0,
            "net_pnl_eur": 5.0,
            "funding_pnl_eur": 0.0,
            "holding_hours": 0.75,
            "close_reason": "SIGNAL_FLIP",
        }
        paper_state["portfolios"]["P1"]["open_positions"] = []
        with patch.object(
            shadow, "bundle_frames", return_value={"BTC": {15: second_frame}}
        ):
            third = shadow.run_shadow_exit_cycle(
                {"opened": [], "closed": [closed]},
                paper_state,
                self.bundle(105),
                self.paper_config(),
                datetime(2026, 7, 19, 10, 46, tzinfo=timezone.utc),
            )
        self.assertEqual(third["new_results"], 1)
        self.assertEqual(third["active_groups"], 0)
        rows = shadow.read_csv(shadow.RESULTS_PATH)
        self.assertEqual(len(rows), 1)
        self.assertAlmostEqual(float(rows[0]["delta_vs_actual_eur"]), 5.0)
        self.assertEqual(rows[0]["timing_assessment"], "EARLIER_BETTER")

    def test_time_exit_uses_mark_when_no_new_candle(self) -> None:
        group, scenario = self.group_with(
            {"id": "TIME", "kind": "TIME_EXIT", "hours": 6.0}
        )
        event = shadow.process_mark_timeout(
            group,
            scenario,
            datetime(2026, 7, 19, 16, 1, tzinfo=timezone.utc),
            105.0,
            self.bundle(105.0),
            self.paper_config(),
        )
        self.assertIsNotNone(event)
        self.assertEqual(scenario["exit_reason"], "TIME_EXIT_MARK_ONLY")
        self.assertAlmostEqual(scenario["comparable_pnl_eur"], 5.0)


if __name__ == "__main__":
    unittest.main()
