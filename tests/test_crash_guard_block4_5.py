
from __future__ import annotations

import json
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path
from types import SimpleNamespace

import pandas as pd

import paper_trading_crash_guard as guard
import paper_trading_shadow_exit as shadow_exit


NOW = datetime(2026, 7, 19, tzinfo=timezone.utc)


def candles(
    opened: float = 100.0,
    high: float = 101.0,
    low: float = 99.0,
    close: float = 100.0,
    *,
    count: int = 60,
    minutes: int = 15,
) -> list[dict]:
    output = []
    start = pd.Timestamp("2026-07-18T00:00:00Z")
    for index in range(count - 1):
        output.append(
            {
                "time": str(
                    start + pd.Timedelta(minutes=minutes * index)
                ),
                "open": 100.0,
                "high": 101.0,
                "low": 99.0,
                "close": 100.0,
                "volume": 1.0,
            }
        )
    output.append(
        {
            "time": str(
                start + pd.Timedelta(minutes=minutes * (count - 1))
            ),
            "open": opened,
            "high": high,
            "low": low,
            "close": close,
            "volume": 1.0,
        }
    )
    return output


def bundle_for(
    *,
    close: float = 100.0,
    high: float = 101.0,
    low: float = 99.0,
    mark: float | None = None,
    assets: tuple[str, ...] = ("BTC", "SOL"),
    freshness: str = "FRESH",
) -> dict:
    bundle = {
        "source": "TEST",
        "_paper_freshness": {"status": freshness},
        "assets": {},
        "frames": {},
    }
    for asset in assets:
        candle_15 = candles(
            opened=100.0,
            high=high,
            low=low,
            close=close,
            minutes=15,
        )
        candle_60 = candles(
            opened=100.0,
            high=max(high, 101.0),
            low=min(low, 99.0),
            close=close,
            minutes=60,
        )
        bundle["assets"][asset] = {
            "mark_price": close if mark is None else mark,
            "candles": {
                "15": candle_15,
                "60": candle_60,
            },
        }
        bundle["frames"][asset] = {
            15: pd.DataFrame(candle_15).assign(
                time=lambda frame: pd.to_datetime(
                    frame["time"], utc=True
                )
            ).set_index("time"),
            60: pd.DataFrame(candle_60).assign(
                time=lambda frame: pd.to_datetime(
                    frame["time"], utc=True
                )
            ).set_index("time"),
        }
    return bundle



def set_asset_move(
    bundle: dict,
    asset: str,
    *,
    close: float,
    high: float,
    low: float,
    mark: float | None = None,
    close_15: float | None = None,
    close_60: float | None = None,
) -> None:
    candle_15 = candles(
        opened=100.0,
        high=high,
        low=low,
        close=close if close_15 is None else close_15,
        minutes=15,
    )
    candle_60 = candles(
        opened=100.0,
        high=max(high, 101.0),
        low=min(low, 99.0),
        close=close if close_60 is None else close_60,
        minutes=60,
    )
    bundle["assets"][asset] = {
        "mark_price": close if mark is None else mark,
        "candles": {
            "15": candle_15,
            "60": candle_60,
        },
    }
    bundle["frames"][asset] = {
        15: pd.DataFrame(candle_15).assign(
            time=lambda frame: pd.to_datetime(
                frame["time"], utc=True
            )
        ).set_index("time"),
        60: pd.DataFrame(candle_60).assign(
            time=lambda frame: pd.to_datetime(
                frame["time"], utc=True
            )
        ).set_index("time"),
    }


def signal(
    signal_id: str = "S1",
    *,
    side: str = "LONG",
    leverage: float = 5.0,
    score: float = 10.0,
    asset: str = "SOL",
) -> SimpleNamespace:
    return SimpleNamespace(
        signal_id=signal_id,
        experiment_group_id="G",
        portfolio="P1",
        is_main=False,
        strategy="TEST",
        asset=asset,
        symbol=f"{asset}USDTM",
        timeframe_minutes=15,
        candle_time="2026-07-19T00:00:00+00:00",
        side=side,
        score=score,
        confidence="HIGH",
        entry_reference_price=100.0,
        atr_pct=2.0,
        stop_pct=0.01,
        target_pct=0.02,
        leverage=leverage,
        max_holding_hours=24,
        trailing_at_r=0.0,
        trailing_atr_multiple=0.0,
        reason="test",
        relative_strength_score=0.0,
        breakout_state="",
        global_overlay=0.0,
        exchange_overlay=0.0,
    )


def paper_state(open_positions: list[dict] | None = None) -> dict:
    return {
        "portfolios": {
            "P1": {
                "open_positions": list(open_positions or [])
            }
        }
    }


class CrashGuardBlock45Tests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        root = Path(self.temporary.name)
        self.path_originals = {}
        for name, filename in {
            "STATE_PATH": "state.json",
            "DECISIONS_PATH": "decisions.csv",
            "EVENTS_PATH": "events.csv",
            "SHADOW_RESULTS_PATH": "shadow_results.csv",
            "STRESS_PATH": "stress.json",
            "REPORT_PATH": "report.md",
            "CONFIG_SNAPSHOT_PATH": "config_snapshot.json",
            "CONFIG_PATH": "missing_config.json",
        }.items():
            self.path_originals[name] = getattr(guard, name)
            setattr(guard, name, root / filename)
        guard._CONFIG_CACHE = None
        guard._CONFIG_CACHE_MTIME_NS = None

        self.config = json.loads(
            json.dumps(guard.DEFAULT_CONFIG)
        )
        self.state = {
            "schema_version": 1,
            "engine_version": guard.ENGINE_VERSION,
            "previous_level": "NORMAL",
            "previous_direction": "NONE",
            "cooldown_until_utc": "",
            "active_simulations": {},
            "seen_blocked_signal_ids": [],
            "totals": {
                "blocked_signals": 0,
                "completed_simulations": 0,
                "avoided_liquidations": 0,
                "guard_value_r": 0.0,
                "missed_profit_r": 0.0,
            },
        }

    def tearDown(self) -> None:
        for name, value in self.path_originals.items():
            setattr(guard, name, value)
        guard._CONFIG_CACHE = None
        guard._CONFIG_CACHE_MTIME_NS = None
        self.temporary.cleanup()

    def test_normal_market_preserves_every_new_signal(self) -> None:
        signals = [
            signal(f"S{index}", side="LONG" if index % 2 else "SHORT")
            for index in range(12)
        ]
        allowed, decisions = guard.filter_signals(
            signals,
            paper_state(),
            bundle_for(),
            self.config,
            self.state,
            {
                "level": "NORMAL",
                "direction": "NONE",
                "asset_context": {},
            },
            NOW,
        )
        self.assertEqual(len(allowed), len(signals))
        self.assertEqual(decisions, [])

    def test_watch_market_is_passthrough(self) -> None:
        allowed, decisions = guard.filter_signals(
            [signal("A")],
            paper_state(),
            bundle_for(),
            self.config,
            self.state,
            {
                "level": "WATCH",
                "direction": "DOWN",
                "asset_context": {},
            },
            NOW,
        )
        self.assertEqual(len(allowed), 1)
        self.assertEqual(decisions, [])

    def test_down_crash_blocks_leveraged_long(self) -> None:
        allowed, decisions = guard.filter_signals(
            [signal("A", side="LONG")],
            paper_state(),
            bundle_for(),
            self.config,
            self.state,
            {
                "level": "CRASH",
                "direction": "DOWN",
                "asset_context": {},
            },
            NOW,
        )
        self.assertEqual(allowed, [])
        self.assertEqual(decisions[0]["decision"], "BLOCKED")

    def test_down_crash_allows_one_opposite_short(self) -> None:
        allowed, _ = guard.filter_signals(
            [signal("A", side="SHORT")],
            paper_state(),
            bundle_for(),
            self.config,
            self.state,
            {
                "level": "CRASH",
                "direction": "DOWN",
                "asset_context": {},
            },
            NOW,
        )
        self.assertEqual(len(allowed), 1)

    def test_extreme_blocks_all_leveraged_signals(self) -> None:
        allowed, _ = guard.filter_signals(
            [signal("A", side="SHORT")],
            paper_state(),
            bundle_for(),
            self.config,
            self.state,
            {
                "level": "EXTREME",
                "direction": "DOWN",
                "asset_context": {},
            },
            NOW,
        )
        self.assertEqual(allowed, [])

    def test_one_x_is_not_blocked_by_default(self) -> None:
        allowed, _ = guard.filter_signals(
            [signal("A", leverage=1.0)],
            paper_state(),
            bundle_for(),
            self.config,
            self.state,
            {
                "level": "EXTREME",
                "direction": "DOWN",
                "asset_context": {},
            },
            NOW,
        )
        self.assertEqual(len(allowed), 1)

    def test_stale_data_enters_data_guard(self) -> None:
        context = guard.market_context(
            bundle_for(freshness="STALE"),
            self.config,
            self.state,
            NOW,
        )
        self.assertEqual(context["level"], "DATA_GUARD")
        allowed, _ = guard.filter_signals(
            [signal("A")],
            paper_state(),
            bundle_for(freshness="STALE"),
            self.config,
            self.state,
            context,
            NOW,
        )
        self.assertEqual(allowed, [])

    def test_market_context_detects_directional_crash(self) -> None:
        context = guard.market_context(
            bundle_for(
                close=93.0,
                high=101.0,
                low=90.0,
                mark=92.0,
            ),
            self.config,
            self.state,
            NOW,
        )
        self.assertIn(context["level"], {"CRASH", "EXTREME"})
        self.assertEqual(context["direction"], "DOWN")

    def test_small_range_multiple_does_not_create_false_crash(self) -> None:
        level = guard.level_for_magnitude(
            mark_move=0.0,
            return_15=0.2,
            range_15=1.5,
            range_multiple=9.0,
            return_60=0.5,
            thresholds=self.config["thresholds"],
        )
        self.assertEqual(level, "NORMAL")

    def test_recovery_admits_only_one_new_leveraged_signal(self) -> None:
        allowed, _ = guard.filter_signals(
            [signal("A"), signal("B", asset="BTC")],
            paper_state(),
            bundle_for(),
            self.config,
            self.state,
            {
                "level": "RECOVERY",
                "direction": "DOWN",
                "asset_context": {},
            },
            NOW,
        )
        self.assertEqual(len(allowed), 1)

    def test_blocked_signal_starts_counterfactual(self) -> None:
        _, decisions = guard.filter_signals(
            [signal("A")],
            paper_state(),
            bundle_for(),
            self.config,
            self.state,
            {
                "level": "CRASH",
                "direction": "DOWN",
                "asset_context": {},
            },
            NOW,
        )
        self.assertTrue(decisions[0]["simulation_started"])
        self.assertIn("A", self.state["active_simulations"])

    def test_previously_blocked_signal_never_reopens_in_normal(self) -> None:
        self.state["seen_blocked_signal_ids"] = ["A"]
        allowed, decisions = guard.filter_signals(
            [signal("A"), signal("B")],
            paper_state(),
            bundle_for(),
            self.config,
            self.state,
            {
                "level": "NORMAL",
                "direction": "NONE",
                "asset_context": {},
            },
            NOW,
        )
        self.assertEqual(
            [item.signal_id for item in allowed],
            ["B"],
        )
        self.assertEqual(
            decisions[0]["decision"],
            "BLOCKED_PREVIOUSLY",
        )

    def test_shadow_stop_produces_negative_r(self) -> None:
        simulation = guard.simulation_from_signal(
            guard.signal_dict(signal("A")),
            {"level": "CRASH", "direction": "DOWN"},
            bundle_for(),
            NOW,
            "BLOCK",
        )
        candle = pd.Series(
            {"open": 100.0, "high": 100.5, "low": 98.0, "close": 99.0}
        )
        exit_price, reason = guard.shadow_exit_decision(
            simulation,
            candle,
            self.config,
        )
        self.assertEqual(reason, "STOP")
        self.assertLess(
            guard.simulation_outcome_r(
                simulation,
                float(exit_price),
                self.config,
            ),
            0,
        )

    def test_shadow_crossing_liquidation_is_liquidated(self) -> None:
        simulation = guard.simulation_from_signal(
            guard.signal_dict(signal("A", leverage=5.0)),
            {"level": "CRASH", "direction": "DOWN"},
            bundle_for(),
            NOW,
            "BLOCK",
        )
        _, reason = guard.shadow_exit_decision(
            simulation,
            pd.Series(
                {"open": 100.0, "high": 101.0, "low": 70.0, "close": 95.0}
            ),
            self.config,
        )
        self.assertEqual(
            reason,
            "LIQUIDATION_INTRABAR_WORST_CASE",
        )

    def test_stress_matrix_flags_5x_at_minus_30(self) -> None:
        position = {
            "side": "LONG",
            "asset": "SOL",
            "entry_price": 100.0,
            "liquidation_price": 80.5,
            "leverage": 5.0,
            "margin_eur": 1000.0,
            "notional_eur": 5000.0,
        }
        with tempfile.TemporaryDirectory() as temporary:
            original = guard.STRESS_PATH
            guard.STRESS_PATH = Path(temporary) / "stress.json"
            try:
                result = guard.stress_matrix(
                    paper_state([position]),
                    bundle_for(mark=100.0),
                    self.config,
                    NOW,
                )
            finally:
                guard.STRESS_PATH = original
        row = next(
            item
            for item in result["scenarios"]
            if item["scenario"] == "DOWN_30"
        )
        self.assertEqual(row["estimated_liquidations"], 1)

    def test_stress_matrix_2x_survives_minus_30(self) -> None:
        position = {
            "side": "LONG",
            "asset": "SOL",
            "entry_price": 100.0,
            "liquidation_price": 50.5,
            "leverage": 2.0,
            "margin_eur": 1000.0,
            "notional_eur": 2000.0,
        }
        with tempfile.TemporaryDirectory() as temporary:
            original = guard.STRESS_PATH
            guard.STRESS_PATH = Path(temporary) / "stress.json"
            try:
                result = guard.stress_matrix(
                    paper_state([position]),
                    bundle_for(mark=100.0),
                    self.config,
                    NOW,
                )
            finally:
                guard.STRESS_PATH = original
        row = next(
            item
            for item in result["scenarios"]
            if item["scenario"] == "DOWN_30"
        )
        self.assertEqual(row["estimated_liquidations"], 0)

    def test_normal_stop_fill_is_unchanged(self) -> None:
        result = guard.resolve_protective_exit(
            {"side": "LONG", "asset": "SOL"},
            pd.Series(
                {"open": 100.0, "high": 100.5, "low": 98.5, "close": 99.0}
            ),
            99.0,
            102.0,
            80.5,
            {
                "_crash_guard_config": self.config,
                "_crash_guard_context": {
                    "level": "NORMAL",
                    "asset_context": {},
                },
            },
            {
                "execution": {
                    "same_candle_stop_target_policy": "STOP_FIRST"
                }
            },
        )
        self.assertEqual(result["reason"], "STOP")
        self.assertEqual(result["exit_price"], 99.0)

    def test_crash_stop_and_liquidation_use_worst_case(self) -> None:
        result = guard.resolve_protective_exit(
            {"side": "LONG", "asset": "SOL"},
            pd.Series(
                {"open": 100.0, "high": 101.0, "low": 70.0, "close": 95.0}
            ),
            99.0,
            102.0,
            80.5,
            {
                "_crash_guard_config": self.config,
                "_crash_guard_context": {
                    "level": "CRASH",
                    "asset_context": {
                        "SOL": {"level": "CRASH"}
                    },
                },
            },
            {
                "execution": {
                    "same_candle_stop_target_policy": "STOP_FIRST"
                }
            },
        )
        self.assertEqual(
            result["reason"],
            "LIQUIDATION_INTRABAR_WORST_CASE",
        )
        self.assertTrue(result["pre_slipped"])

    def test_gap_stop_has_stressed_fill(self) -> None:
        result = guard.resolve_protective_exit(
            {"side": "LONG", "asset": "SOL"},
            pd.Series(
                {"open": 97.0, "high": 98.0, "low": 95.0, "close": 96.0}
            ),
            99.0,
            102.0,
            80.5,
            {
                "_crash_guard_config": self.config,
                "_crash_guard_context": {
                    "level": "STRESS",
                    "asset_context": {
                        "SOL": {"level": "STRESS"}
                    },
                },
            },
            {
                "execution": {
                    "same_candle_stop_target_policy": "STOP_FIRST"
                }
            },
        )
        self.assertIn(
            result["reason"],
            {
                "STOP_GAP_STRESS",
                "LIQUIDATION_STOP_GAP_STRESS",
            },
        )
        self.assertTrue(result["pre_slipped"])
        self.assertGreater(result["stop_slippage_pct"], 0)

    def test_live_requirements_are_isolated_and_native_stop(self) -> None:
        requirements = self.config["live_readiness_requirements"]
        self.assertEqual(requirements["margin_mode"], "ISOLATED")
        self.assertTrue(requirements["exchange_native_stop_required"])
        self.assertTrue(requirements["cross_margin_forbidden"])

    def test_block3_versions_results_by_risk_model(self) -> None:
        position = {
            "trade_id": "T1",
            "strategy": "S1",
            "asset": "BTC",
            "symbol": "BTC-USDT",
            "side": "LONG",
            "timeframe_minutes": 15,
            "opened_at": "2026-07-19T10:00:00+00:00",
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
            "risk_model_version_at_entry": "block4_5_v1",
        }
        config = json.loads(json.dumps(shadow_exit.DEFAULT_CONFIG))
        config["scenarios"] = [config["scenarios"][0]]
        group = shadow_exit.create_group(
            position,
            "P1",
            config,
            "",
            "FULL_FROM_ENTRY",
        )
        self.assertEqual(
            group["risk_model_version"],
            "block4_5_v1",
        )
        self.assertTrue(
            group["scenario_set_version"].endswith(
                "|risk=block4_5_v1"
            )
        )

    def test_risk_model_version_is_declared(self) -> None:
        self.assertEqual(
            guard.RISK_MODEL_VERSION,
            "block4_5_v1",
        )
        self.assertTrue(self.config["normal_market_passthrough"])


    def test_isolated_asset_crash_does_not_become_market_crash(self) -> None:
        assets = ("BTC", "ETH", "SOL", "ADA", "XRP", "BANK")
        bundle = bundle_for(assets=assets)
        set_asset_move(
            bundle,
            "BANK",
            close=97.1,
            close_60=109.8,
            high=101.0,
            low=95.5,
            mark=97.65,
        )
        context = guard.market_context(
            bundle,
            self.config,
            self.state,
            NOW,
        )
        self.assertEqual(context["level"], "NORMAL")
        self.assertEqual(
            context["asset_context"]["BANK"]["level"],
            "CRASH",
        )
        self.assertEqual(
            context["market_level_source"],
            "NO_MARKET_WIDE_TRIGGER",
        )

    def test_isolated_asset_crash_blocks_only_that_asset(self) -> None:
        assets = ("BTC", "ETH", "SOL", "ADA", "XRP", "BANK")
        bundle = bundle_for(assets=assets)
        set_asset_move(
            bundle,
            "BANK",
            close=97.1,
            close_60=109.8,
            high=101.0,
            low=95.5,
            mark=97.65,
        )
        context = guard.market_context(
            bundle,
            self.config,
            self.state,
            NOW,
        )
        allowed, decisions = guard.filter_signals(
            [
                signal("BANK-S", asset="BANK", side="SHORT"),
                signal("SOL-S", asset="SOL", side="SHORT"),
            ],
            paper_state(),
            bundle,
            self.config,
            self.state,
            context,
            NOW,
        )
        self.assertEqual(
            [item.signal_id for item in allowed],
            ["SOL-S"],
        )
        self.assertEqual(
            decisions[0]["reason"],
            "CRASH_GUARD_ASSET_DIRECTIONAL",
        )

    def test_isolated_asset_stress_does_not_reduce_other_trades(self) -> None:
        assets = ("BTC", "ETH", "SOL", "ADA", "XRP", "ESPORTS")
        bundle = bundle_for(assets=assets)
        set_asset_move(
            bundle,
            "ESPORTS",
            close=100.35,
            close_60=92.66,
            high=102.0,
            low=98.2,
            mark=96.92,
        )
        context = guard.market_context(
            bundle,
            self.config,
            self.state,
            NOW,
        )
        self.assertEqual(context["level"], "NORMAL")
        self.assertEqual(
            context["asset_context"]["ESPORTS"]["level"],
            "STRESS",
        )
        signals = [
            signal("E-L", asset="ESPORTS", side="LONG"),
            signal("S-L", asset="SOL", side="LONG"),
        ]
        allowed, decisions = guard.filter_signals(
            signals,
            paper_state(),
            bundle,
            self.config,
            self.state,
            context,
            NOW,
        )
        self.assertEqual(
            [item.signal_id for item in allowed],
            ["E-L", "S-L"],
        )
        self.assertEqual(decisions, [])

    def test_real_directional_breadth_creates_market_crash(self) -> None:
        assets = (
            "BTC", "ETH", "SOL", "ADA", "XRP",
            "DOGE", "PEPE", "ZEC", "BANK", "ESPORTS",
        )
        bundle = bundle_for(assets=assets)
        for asset in assets[:6]:
            set_asset_move(
                bundle,
                asset,
                close=94.0,
                high=101.0,
                low=92.0,
            )
        context = guard.market_context(
            bundle,
            self.config,
            self.state,
            NOW,
        )
        self.assertEqual(context["level"], "CRASH")
        self.assertEqual(context["direction"], "DOWN")
        self.assertIn(
            context["market_level_source"],
            {"MARKET_BREADTH", "MARKET_CORE_OVERRIDE"},
        )

    def test_isolated_extreme_asset_does_not_freeze_market(self) -> None:
        assets = (
            "BTC", "ETH", "SOL", "ADA", "XRP",
            "DOGE", "PEPE", "ZEC", "BANK", "ESPORTS",
        )
        bundle = bundle_for(assets=assets)
        set_asset_move(
            bundle,
            "BANK",
            close=116.0,
            high=118.0,
            low=97.0,
        )
        context = guard.market_context(
            bundle,
            self.config,
            self.state,
            NOW,
        )
        self.assertEqual(context["level"], "NORMAL")
        self.assertEqual(
            context["asset_context"]["BANK"]["level"],
            "EXTREME",
        )

    def test_two_core_assets_can_trigger_market_stress(self) -> None:
        assets = (
            "BTC", "ETH", "SOL", "ADA", "XRP",
            "DOGE", "PEPE", "ZEC", "BANK", "ESPORTS",
        )
        bundle = bundle_for(assets=assets)
        for asset in ("ETH", "SOL"):
            set_asset_move(
                bundle,
                asset,
                close=93.5,
                high=101.0,
                low=92.5,
            )
        context = guard.market_context(
            bundle,
            self.config,
            self.state,
            NOW,
        )
        self.assertEqual(context["level"], "STRESS")
        self.assertEqual(context["direction"], "DOWN")
        self.assertEqual(
            context["market_level_source"],
            "MARKET_CORE_OVERRIDE",
        )

    def test_btc_and_sol_crash_can_trigger_market_crash(self) -> None:
        assets = (
            "BTC", "ETH", "SOL", "ADA", "XRP",
            "DOGE", "PEPE", "ZEC", "BANK", "ESPORTS",
        )
        bundle = bundle_for(assets=assets)
        for asset in ("BTC", "SOL"):
            set_asset_move(
                bundle,
                asset,
                close=94.0,
                high=101.0,
                low=92.0,
            )
        context = guard.market_context(
            bundle,
            self.config,
            self.state,
            NOW,
        )
        self.assertEqual(context["level"], "CRASH")
        self.assertEqual(context["direction"], "DOWN")
        self.assertEqual(
            context["market_level_source"],
            "MARKET_CORE_OVERRIDE",
        )

    def test_upgrade_clears_false_legacy_cooldown(self) -> None:
        legacy_state = dict(self.state)
        legacy_state.pop("market_scope_version", None)
        legacy_state["previous_level"] = "CRASH"
        legacy_state["previous_direction"] = "UP"
        legacy_state["cooldown_until_utc"] = (
            "2026-07-19T21:00:00+00:00"
        )
        guard.STATE_PATH.write_text(
            json.dumps(legacy_state),
            encoding="utf-8",
        )
        loaded = guard.load_state()
        self.assertEqual(
            loaded["market_scope_version"],
            "legacy_block4_5_v1",
        )
        context = guard.market_context(
            bundle_for(
                assets=("BTC", "ETH", "SOL", "ADA")
            ),
            self.config,
            loaded,
            NOW,
        )
        self.assertEqual(context["level"], "NORMAL")
        self.assertEqual(context["cooldown_until_utc"], "")
        self.assertEqual(
            loaded["market_scope_version"],
            guard.MARKET_SCOPE_VERSION,
        )

if __name__ == "__main__":
    unittest.main()
