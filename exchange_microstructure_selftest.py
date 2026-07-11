# -*- coding: utf-8 -*-
from __future__ import annotations

import csv
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def assert_close(actual, expected, tolerance=1e-9):
    if actual is None or abs(float(actual) - float(expected)) > tolerance:
        raise AssertionError(f"{actual!r} != {expected!r}")


def synthetic_source(exchange: str, price: float, funding_pct: float, oi: float, ratio: float, imbalance: float):
    return {
        "available": True,
        "source_state": "OK",
        "symbol": f"{exchange}-{price}",
        "market_type": "perpetual",
        "last_price": price,
        "mark_price": price,
        "index_price": price * 0.999,
        "basis_pct": (price / (price * 0.999) - 1) * 100,
        "funding_rate_pct": funding_pct,
        "funding_rate_raw": None,
        "funding_interval_hours": 8,
        "price_change_24h_pct": 1.5,
        "open_interest_base": None,
        "open_interest_usd": oi,
        "oi_change_4h_pct": None,
        "oi_change_24h_pct": None,
        "global_long_short_ratio": None,
        "top_account_long_short_ratio": None,
        "top_position_long_short_ratio": None,
        "taker_buy_sell_ratio_recent": ratio,
        "taker_buy_notional_recent": 1000,
        "taker_sell_notional_recent": 1000 / ratio,
        "recent_trade_count": 100,
        "orderbook": {
            "imbalance_0_25pct": None,
            "imbalance_0_5pct": imbalance,
            "imbalance_1_0pct": None,
            "imbalance_2_0pct": None,
            "bid_notional_0_5pct": 1_000_000 * (1 + imbalance),
            "ask_notional_0_5pct": 1_000_000 * (1 - imbalance),
            "spread_bps": 1.0,
            "largest_bid_wall": {},
            "largest_ask_wall": {},
        },
        "capabilities": {},
        "notes": [],
    }


def build_fixture():
    sys.path.insert(0, str(ROOT))
    import exchange_market_data as emd

    # Funding normalization checks.
    assert_close(
        emd.normalize_funding_8h_pct(
            "kraken",
            {"funding_rate_raw": -0.1024, "index_price": 64000, "funding_interval_hours": 1},
        ),
        -0.00128,
        1e-12,
    )
    assert_close(
        emd.normalize_funding_8h_pct(
            "bitget", {"funding_rate_raw": -0.000022, "funding_interval_hours": 8}
        ),
        -0.0022,
        1e-12,
    )
    assert_close(
        emd.normalize_funding_8h_pct(
            "kucoin", {"funding_rate_raw": 0.000061, "funding_interval_hours": 8}
        ),
        0.0061,
        1e-12,
    )

    prices = {"BTC": 64000.0, "SOL": 78.0, "DOGE": 0.074}
    assets = {}
    for asset, price in prices.items():
        source_rows = {
            "kraken": synthetic_source("kraken", price, -0.001, 100_000_000, 1.15, 0.10),
            "bitget": synthetic_source("bitget", price, 0.002, 200_000_000, 1.10, 0.08),
            "kucoin": synthetic_source("kucoin", price, 0.001, 150_000_000, 1.12, 0.09),
            "okx": synthetic_source("okx", price, 0.001, 170_000_000, 1.05, 0.03),
            "coinbase": synthetic_source("coinbase", price, 0.0, 0.0, 1.08, 0.05),
        }
        combined = emd.combine_asset(asset, source_rows)
        if combined["exchange_count"] != 3:
            raise AssertionError(combined)
        assert_close(combined["data_coverage"], 1.0)
        assets[asset] = combined
    return {
        "schema_version": "2.1.3",
        "generated_utc": "2026-07-11T10:00:00+00:00",
        "snapshot_date": "2026-07-11",
        "liquidation_sample_seconds": 0,
        "collector_mode": "selftest",
        "primary_derivative_exchanges": ["kraken", "bitget", "kucoin"],
        "auxiliary_exchanges": ["okx", "coinbase"],
        "assets": assets,
    }


def write_csv(path: Path, headers: list[str], rows: list[dict]):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)


def integration_test():
    fixture = build_fixture()
    with tempfile.TemporaryDirectory(prefix="exchange-v213-") as temp_name:
        temp = Path(temp_name)
        for name in (
            "alternative_exchange_sources.py",
            "exchange_market_data.py",
            "exchange_microstructure_report.py",
            "exchange_signal_tracker.py",
        ):
            shutil.copy2(ROOT / name, temp / name)
        reports = temp / "reports"
        reports.mkdir()
        fixture_path = temp / "fixture.json"
        fixture_path.write_text(json.dumps(fixture), encoding="utf-8")
        (reports / "latest_report.md").write_text("<!-- LIQUIDATION_SUMMARY_START -->\n", encoding="utf-8")
        (reports / "exchange_market_data_health.json").write_text(
            json.dumps(
                {
                    "status": "OK",
                    "collector_mode": "selftest",
                    "available_exchange_asset_pairs": 9,
                    "total_exchange_asset_pairs": 9,
                    "available_auxiliary_asset_pairs": 6,
                    "total_auxiliary_asset_pairs": 6,
                    "exchange_status": {"kraken": "OK", "bitget": "OK", "kucoin": "OK", "okx": "OK", "coinbase": "PARZIALE"},
                    "assets": {},
                    "liquidation_streams": {},
                }
            ),
            encoding="utf-8",
        )
        (reports / "exchange_storage_status.json").write_text(json.dumps({"status": "OK", "asset": "exchange_state_A.tar.gz"}), encoding="utf-8")
        write_csv(
            reports / "technical_structure_metrics.csv",
            ["asset", "price", "rsi14", "fib_state", "fib_confluence", "wyckoff", "dominant_bullish_pattern", "dominant_bullish_status", "dominant_bearish_pattern", "dominant_bearish_status", "support", "resistance"],
            [
                {"asset": "BTC", "price": 64000, "rsi14": 55, "fib_state": "TENUTO", "fib_confluence": "supporto", "wyckoff": "Possibile accumulazione", "dominant_bullish_pattern": "Doppio minimo", "dominant_bullish_status": "CANDIDATO", "dominant_bearish_pattern": "", "dominant_bearish_status": "", "support": 62000, "resistance": 65000},
                {"asset": "SOL", "price": 78, "rsi14": 50, "fib_state": "TESTATO", "fib_confluence": "neckline", "wyckoff": "Range", "dominant_bullish_pattern": "Doppio minimo", "dominant_bullish_status": "CONFERMATO RECENTE", "dominant_bearish_pattern": "", "dominant_bearish_status": "", "support": 75, "resistance": 84},
                {"asset": "DOGE", "price": 0.074, "rsi14": 35, "fib_state": "NON ATTIVO", "fib_confluence": "resistenza", "wyckoff": "Markdown / debolezza", "dominant_bullish_pattern": "", "dominant_bullish_status": "", "dominant_bearish_pattern": "Triplo massimo", "dominant_bearish_status": "MATURO", "support": 0.069, "resistance": 0.079},
            ],
        )
        write_csv(
            reports / "latest_scanner_summary.csv",
            ["asset", "positive_cases_30d", "return_p50_pct"],
            [
                {"asset": "BTC", "positive_cases_30d": 70, "return_p50_pct": 8},
                {"asset": "SOL", "positive_cases_30d": 50, "return_p50_pct": 0},
                {"asset": "DOGE", "positive_cases_30d": 20, "return_p50_pct": -10},
            ],
        )
        env = os.environ.copy()
        env["EXCHANGE_TEST_FIXTURE"] = str(fixture_path)
        subprocess.run([sys.executable, "exchange_market_data.py"], cwd=temp, env=env, check=True)
        # Restore the realistic health file overwritten by fixture mode.
        (reports / "exchange_market_data_health.json").write_text(
            json.dumps(
                {
                    "status": "OK",
                    "collector_mode": "selftest",
                    "available_exchange_asset_pairs": 9,
                    "total_exchange_asset_pairs": 9,
                    "available_auxiliary_asset_pairs": 6,
                    "total_auxiliary_asset_pairs": 6,
                    "exchange_status": {"kraken": "OK", "bitget": "OK", "kucoin": "OK", "okx": "OK", "coinbase": "PARZIALE"},
                    "assets": {},
                    "liquidation_streams": {},
                }
            ),
            encoding="utf-8",
        )
        subprocess.run([sys.executable, "exchange_microstructure_report.py"], cwd=temp, check=True)
        report = (reports / "exchange_microstructure_report.md").read_text(encoding="utf-8")
        if "Kraken" not in report or "Bitget" not in report or "Funding 8h eq." not in report:
            raise AssertionError(report[:2000])
        if "Binance" in report or "Bybit" in report:
            raise AssertionError("Legacy exchange names leaked into V2.1.3 report")
        metrics = list(csv.DictReader((reports / "exchange_microstructure_metrics.csv").open(encoding="utf-8")))
        if len(metrics) != 3 or any(row.get("global_score") not in {"0", "0.0"} for row in metrics):
            raise AssertionError(metrics)
        # A single recent-trades sample must never create a daily candidate.
        if any(row.get("candidate_global_score") not in {"0", "0.0"} for row in metrics):
            raise AssertionError(metrics)
        intraday_path = reports / "exchange_market_data_intraday.csv"
        intraday = list(csv.DictReader(intraday_path.open(encoding="utf-8")))
        if len(intraday) != 3 or not all(row.get("kraken_available", "").lower() in {"true", "1"} for row in intraday):
            raise AssertionError(intraday)

        # After three snapshots spanning one hour, the rolling 4h sample may
        # produce a candidate, while the calibrated Global score stays zero.
        headers = list(intraday[0].keys())
        expanded = []
        for timestamp in ("2026-07-11T09:00:00+00:00", "2026-07-11T09:30:00+00:00", "2026-07-11T10:00:00+00:00"):
            for row in intraday:
                copied = dict(row)
                copied["timestamp_utc"] = timestamp
                expanded.append(copied)
        write_csv(intraday_path, headers, expanded)
        subprocess.run([sys.executable, "exchange_microstructure_report.py"], cwd=temp, check=True)
        mature_metrics = {row["asset"]: row for row in csv.DictReader((reports / "exchange_microstructure_metrics.csv").open(encoding="utf-8"))}
        if mature_metrics["BTC"].get("candidate_global_score") not in {"1", "1.0"}:
            raise AssertionError(mature_metrics["BTC"])
        if mature_metrics["BTC"].get("global_score") not in {"0", "0.0"}:
            raise AssertionError(mature_metrics["BTC"])
        if float(mature_metrics["BTC"].get("intraday_span_4h_hours") or 0) < 0.75:
            raise AssertionError(mature_metrics["BTC"])


def main():
    integration_test()
    print("Exchange Microstructure V2.1.3 self-test: OK")


if __name__ == "__main__":
    main()
