from __future__ import annotations

import csv
import sys
import tempfile
import types
import unittest
from pathlib import Path
from unittest import mock

import pandas as pd

kucoin_stub = types.ModuleType("kucoin_public_data")
kucoin_stub.bundle_frames = lambda bundle: bundle.get("frames", {})
kucoin_stub.safe_float = lambda value, default=0.0: float(value) if value not in (None, "") else default
sys.modules.setdefault("kucoin_public_data", kucoin_stub)

signal_stub = types.ModuleType("paper_signal_engine")
signal_stub.Signal = type("Signal", (), {})
sys.modules.setdefault("paper_signal_engine", signal_stub)

import paper_trading_engine as engine
from paper_trading_excursions import (
    backfill_trade_excursion_fields,
    close_excursion_metrics,
    summarize_excursion_frame,
    update_position_excursion,
)
import paper_trading_trade_log_repair as trade_repair
from paper_trading_trade_log_repair import repair_trade_log


NEW_FIELDS = {
    "mfe_pct",
    "mae_pct",
    "mfe_at_utc",
    "mae_at_utc",
    "excursion_observation_count",
    "excursion_quality",
    "capture_ratio_signed",
    "winner_capture_ratio",
    "profit_giveback_pct_of_mfe",
    "lost_after_positive_mfe",
}


class ExcursionMetricTests(unittest.TestCase):
    def test_winner_and_loser_metrics_are_separate(self) -> None:
        winner = close_excursion_metrics(60.0, 100.0)
        self.assertAlmostEqual(winner["capture_ratio_signed"], 0.6)
        self.assertAlmostEqual(winner["winner_capture_ratio"], 0.6)
        self.assertAlmostEqual(winner["profit_retained_pct"], 60.0)
        self.assertAlmostEqual(winner["peak_profit_giveback_eur"], 40.0)
        self.assertAlmostEqual(winner["profit_giveback_pct_of_mfe"], 40.0)
        self.assertFalse(winner["lost_after_positive_mfe"])

        loser = close_excursion_metrics(-20.0, 100.0)
        self.assertAlmostEqual(loser["capture_ratio_signed"], -0.2)
        self.assertIsNone(loser["winner_capture_ratio"])
        self.assertIsNone(loser["profit_retained_pct"])
        self.assertAlmostEqual(loser["peak_profit_giveback_eur"], 120.0)
        self.assertAlmostEqual(loser["profit_giveback_pct_of_mfe"], 120.0)
        self.assertTrue(loser["lost_after_positive_mfe"])

    def test_position_updates_long_and_short(self) -> None:
        base = {
            "entry_price": 100.0,
            "quantity": 10.0,
            "eur_usdt_rate": 1.0,
            "entry_fee_eur": 1.0,
            "funding_pnl_eur": 0.0,
            "max_favorable_price": 100.0,
            "max_adverse_price": 100.0,
            "mfe_net_eur": -1.0,
            "mae_net_eur": -1.0,
            "excursion_observation_count": 0,
            "excursion_quality": "NO_OBSERVATIONS",
        }
        long = {**base, "side": "LONG"}
        update_position_excursion(
            long,
            observed_high=110.0,
            observed_low=95.0,
            taker_fee_bps=0.0,
            observed_at="2026-07-19T10:00:00+00:00",
            quality="COMPLETED_15M_OHLC",
        )
        self.assertEqual(long["max_favorable_price"], 110.0)
        self.assertEqual(long["max_adverse_price"], 95.0)
        self.assertAlmostEqual(long["mfe_pct"], 10.0)
        self.assertAlmostEqual(long["mae_pct"], -5.0)

        short = {**base, "side": "SHORT"}
        update_position_excursion(
            short,
            observed_high=105.0,
            observed_low=90.0,
            taker_fee_bps=0.0,
            observed_at="2026-07-19T10:00:00+00:00",
            quality="COMPLETED_15M_OHLC",
        )
        self.assertEqual(short["max_favorable_price"], 90.0)
        self.assertEqual(short["max_adverse_price"], 105.0)
        self.assertAlmostEqual(short["mfe_pct"], 10.0)
        self.assertAlmostEqual(short["mae_pct"], -5.0)

    def test_summary_excludes_losers_from_winner_capture(self) -> None:
        frame = pd.DataFrame(
            [
                {"net_pnl_eur": 60, "mfe_net_eur": 100, "mae_net_eur": -20},
                {"net_pnl_eur": -20, "mfe_net_eur": 100, "mae_net_eur": -40},
            ]
        )
        summary = summarize_excursion_frame(frame)
        self.assertEqual(summary["winner_capture_sample"], 1)
        self.assertAlmostEqual(summary["average_winner_capture_pct"], 60.0)
        self.assertEqual(summary["signed_capture_sample"], 2)
        self.assertAlmostEqual(summary["average_signed_capture_pct"], 20.0)
        self.assertEqual(summary["lost_after_positive_mfe_count"], 1)
        self.assertAlmostEqual(summary["average_profit_giveback_eur"], 80.0)

    def test_backfill_is_semantically_idempotent(self) -> None:
        record = {
            "side": "LONG",
            "entry_price": "100.0",
            "max_favorable_price": "110.0",
            "max_adverse_price": "95.0",
            "mfe_net_eur": "100.0",
            "mae_net_eur": "-50.0",
            "net_pnl_eur": "-20.0",
            "profit_retained_pct": "-20.0",
        }
        first, changed = backfill_trade_excursion_fields(record)
        self.assertTrue(changed)
        self.assertEqual(first["profit_retained_pct"], "")
        self.assertEqual(first["lost_after_positive_mfe"], True)
        second, changed_again = backfill_trade_excursion_fields(first)
        self.assertFalse(changed_again)
        self.assertEqual(second, first)


class EngineChronologyTests(unittest.TestCase):
    def _position(self, **overrides):
        position = {
            "trade_id": "t1",
            "asset": "BTC",
            "side": "LONG",
            "entry_price": 100.0,
            "quantity": 1.0,
            "eur_usdt_rate": 1.0,
            "entry_fee_eur": 0.0,
            "funding_pnl_eur": 0.0,
            "opened_at": "2026-07-19T09:00:00+00:00",
            "last_processed_candle": "",
            "max_holding_hours": 24.0,
            "stop_price": 95.0,
            "initial_stop_price": 95.0,
            "target_price": 110.0,
            "liquidation_price": 50.0,
            "max_favorable_price": 100.0,
            "max_adverse_price": 100.0,
            "mfe_gross_eur": 0.0,
            "mae_gross_eur": 0.0,
            "mfe_net_eur": 0.0,
            "mae_net_eur": 0.0,
            "excursion_observation_count": 0,
            "excursion_quality": "NO_OBSERVATIONS",
            "trailing_at_r": 0.0,
            "trailing_atr_multiple": 0.0,
            "atr_pct": 1.0,
        }
        position.update(overrides)
        return position

    def _config(self):
        return {
            "execution": {
                "taker_fee_bps": 0.0,
                "same_candle_stop_target_policy": "STOP_FIRST",
                "funding_interval_hours": 8,
            }
        }

    def test_stop_candle_does_not_count_post_exit_high(self) -> None:
        frame = pd.DataFrame(
            [{"open": 100.0, "high": 108.0, "low": 94.0, "close": 96.0}],
            index=pd.to_datetime(["2026-07-19T10:00:00Z"]),
        )
        portfolio = {"open_positions": [self._position()]}
        captured = []

        def fake_close(portfolio, position, price, reason, bundle, config, when):
            captured.append((position.copy(), price, reason))
            return {"reason": reason}

        with (
            mock.patch.object(engine, "bundle_frames", return_value={"BTC": {15: frame}}),
            mock.patch.object(engine, "current_prices", return_value={"BTC": 96.0}),
            mock.patch.object(engine, "apply_funding", return_value=None),
            mock.patch.object(engine, "close_position", side_effect=fake_close),
        ):
            closed = engine.update_positions(
                portfolio,
                {},
                self._config(),
                pd.Timestamp("2026-07-19T10:15:00Z").to_pydatetime(),
            )

        self.assertEqual(len(closed), 1)
        position, price, reason = captured[0]
        self.assertEqual(reason, "STOP")
        self.assertEqual(price, 95.0)
        self.assertEqual(position["max_favorable_price"], 100.0)
        self.assertEqual(position["max_adverse_price"], 95.0)
        self.assertEqual(
            position["excursion_quality"],
            "EXIT_CAPPED_OHLC_CONSERVATIVE",
        )

    def test_new_trailing_stop_is_not_applied_to_same_candle(self) -> None:
        frame = pd.DataFrame(
            [{"open": 100.0, "high": 110.0, "low": 95.0, "close": 100.0}],
            index=pd.to_datetime(["2026-07-19T10:00:00Z"]),
        )
        position = self._position(
            stop_price=90.0,
            initial_stop_price=90.0,
            target_price=120.0,
            trailing_at_r=0.5,
            trailing_atr_multiple=2.0,
            atr_pct=1.0,
        )
        portfolio = {"open_positions": [position]}

        with (
            mock.patch.object(engine, "bundle_frames", return_value={"BTC": {15: frame}}),
            mock.patch.object(engine, "current_prices", return_value={"BTC": 100.0}),
            mock.patch.object(engine, "apply_funding", return_value=None),
        ):
            closed = engine.update_positions(
                portfolio,
                {},
                self._config(),
                pd.Timestamp("2026-07-19T10:15:00Z").to_pydatetime(),
            )

        self.assertEqual(closed, [])
        self.assertEqual(len(portfolio["open_positions"]), 1)
        self.assertAlmostEqual(portfolio["open_positions"][0]["stop_price"], 100.0)


class TradeRepairTests(unittest.TestCase):
    def test_legacy_rows_are_enriched_without_fabrication(self) -> None:
        legacy_fields = [field for field in engine.TRADE_FIELDS if field not in NEW_FIELDS]
        row = {field: "" for field in legacy_fields}
        row.update(
            {
                "trade_id": "legacy-1",
                "portfolio": "TEST",
                "asset": "BTC",
                "side": "LONG",
                "closed_at": "2026-07-19T10:00:00+00:00",
                "entry_price": "100",
                "max_favorable_price": "110",
                "max_adverse_price": "95",
                "mfe_net_eur": "100",
                "mae_net_eur": "-50",
                "net_pnl_eur": "-20",
                "profit_retained_pct": "-20",
            }
        )
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "trades.csv"
            with path.open("w", encoding="utf-8", newline="") as handle:
                writer = csv.DictWriter(handle, fieldnames=legacy_fields)
                writer.writeheader()
                writer.writerow(row)

            with (
                mock.patch.object(
                    trade_repair, "BACKUP_PATH", Path(directory) / "backup.csv"
                ),
                mock.patch.object(
                    trade_repair, "QUARANTINE_PATH", Path(directory) / "quarantine.csv"
                ),
                mock.patch.object(
                    trade_repair, "STATUS_PATH", Path(directory) / "status.json"
                ),
            ):
                first = repair_trade_log(path, engine.TRADE_FIELDS)
                self.assertTrue(first["rewritten"])
                self.assertEqual(first["rows_excursion_enriched"], 1)
                with path.open("r", encoding="utf-8", newline="") as handle:
                    repaired = next(csv.DictReader(handle))
                self.assertEqual(repaired["profit_retained_pct"], "")
                self.assertEqual(repaired["lost_after_positive_mfe"], "True")
                self.assertEqual(
                    repaired["excursion_quality"],
                    "LEGACY_MFE_MAE_AVAILABLE",
                )

                second = repair_trade_log(path, engine.TRADE_FIELDS)
                self.assertFalse(second["rewritten"])
                self.assertEqual(second["rows_excursion_enriched"], 0)



if __name__ == "__main__":
    unittest.main()
