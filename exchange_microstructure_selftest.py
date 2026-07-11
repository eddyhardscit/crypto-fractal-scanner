# -*- coding: utf-8 -*-
"""Offline self-test for Exchange Microstructure Upgrade v2.1.

It validates KuCoin contract multipliers, three-exchange aggregation, the Global
weight lock, report/tracker output, and the one-time installer on a temporary
copy. No live exchange request is required.
"""

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
        raise AssertionError(f"Expected {expected}, got {actual}")


def test_kucoin_parser() -> None:
    import exchange_market_data as emd

    original_get_json = emd.get_json

    contract = {
        "symbol": "XBTUSDTM",
        "multiplier": 0.001,
        "fundingFeeRate": 0.0001,
        "openInterest": "100000",
        "markPrice": 100.0,
        "indexPrice": 99.9,
        "lastTradePrice": 100.0,
        "priceChgPct": 0.02,
        "turnoverOf24h": 123456,
        "volumeOf24h": 1200,
    }
    payloads = {
        "/api/v1/contracts/XBTUSDTM": {"code": "200000", "data": contract},
        "/api/v1/ticker": {"code": "200000", "data": {"symbol": "XBTUSDTM", "price": "100"}},
        "/api/v1/level2/snapshot": {
            "code": "200000",
            "data": {"bids": [[99.9, 1000]], "asks": [[100.1, 500]], "sequence": 1},
        },
        "/api/v1/trade/history": {
            "code": "200000",
            "data": [
                {"price": "100", "size": 1000, "side": "buy", "ts": 1},
                {"price": "100", "size": 500, "side": "sell", "ts": 2},
            ],
        },
        "/api/v1/funding-rate/XBTUSDTM/current": {
            "code": "200000",
            "data": {"value": 0.0002, "fundingTime": 123},
        },
        "/api/ua/v1/market/open-interest": {
            "code": "200000",
            "data": [{"openInterest": str(100000 + i * 1000), "ts": i} for i in range(30)],
        },
    }

    def fake_get_json(session, base, path, params):
        payload = payloads[path]
        return emd.FetchResult(True, data=payload, url=base + path, status_code=200)

    emd.get_json = fake_get_json
    try:
        result, health = emd.fetch_kucoin_asset(object(), "BTC")
    finally:
        emd.get_json = original_get_json

    parsed = result["parsed"]
    assert parsed["available"]
    assert_close(parsed["open_interest_base"], 100.0)
    assert_close(parsed["open_interest_usd"], 10000.0)
    assert_close(parsed["funding_rate_pct"], 0.02)
    assert_close(parsed["taker_buy_sell_ratio_recent"], 2.0)
    # Bid: 99.9 * 1000 contracts * 0.001 BTC/contract.
    assert_close(parsed["orderbook"]["bid_notional_0_25pct"], 99.9)
    if not all(item["ok"] for item in health.values()):
        raise AssertionError(f"Unexpected KuCoin health failure: {health}")


def synthetic_snapshot() -> dict:
    assets = {}
    prices = {"BTC": 64000.0, "SOL": 78.0, "DOGE": 0.074}
    for asset, price in prices.items():
        exchanges = {}
        for index, exchange in enumerate(("binance", "bybit", "kucoin")):
            bullish = asset == "BTC"
            bearish = asset == "DOGE"
            ratio = 1.14 if bullish else 0.84 if bearish else 1.0
            imbalance = 0.12 if bullish else -0.14 if bearish else 0.01
            oi_change = 4.0 if bullish else 5.0 if bearish else -1.0
            funding = 0.008 if bullish else 0.04 if bearish else 0.001
            exchanges[exchange] = {
                "available": True,
                "funding_rate_pct": funding + index * 0.0001,
                "basis_pct": 0.03,
                "price_change_24h_pct": 2.0 if bullish else -2.0 if bearish else 0.0,
                "open_interest_usd": 1_000_000_000 / (index + 1),
                "oi_change_4h_pct": oi_change,
                "oi_change_24h_pct": oi_change,
                "global_long_short_ratio": 1.1 if exchange != "kucoin" else None,
                "top_account_long_short_ratio": 1.1 if exchange == "binance" else None,
                "top_position_long_short_ratio": 1.1 if exchange == "binance" else None,
                "taker_buy_sell_ratio_1h": ratio if exchange == "binance" else None,
                "taker_buy_sell_ratio_4h": ratio if exchange == "binance" else None,
                "taker_buy_sell_ratio_24h": ratio if exchange == "binance" else None,
                "taker_buy_sell_ratio_recent": ratio if exchange != "binance" else None,
                "orderbook": {
                    "imbalance_0_25pct": imbalance,
                    "imbalance_0_5pct": imbalance,
                    "imbalance_1_0pct": imbalance,
                    "imbalance_2_0pct": imbalance,
                    "bid_notional_0_25pct": 2_000_000 if imbalance >= 0 else 1_000_000,
                    "ask_notional_0_25pct": 1_000_000 if imbalance >= 0 else 2_000_000,
                    "bid_notional_0_5pct": 4_000_000 if imbalance >= 0 else 2_000_000,
                    "ask_notional_0_5pct": 2_000_000 if imbalance >= 0 else 4_000_000,
                    "bid_notional_1_0pct": 8_000_000 if imbalance >= 0 else 4_000_000,
                    "ask_notional_1_0pct": 4_000_000 if imbalance >= 0 else 8_000_000,
                    "bid_notional_2_0pct": 12_000_000 if imbalance >= 0 else 6_000_000,
                    "ask_notional_2_0pct": 6_000_000 if imbalance >= 0 else 12_000_000,
                    "spread_bps": 1.0,
                    "largest_bid_wall": {"price": price * 0.99, "notional": 2_000_000, "distance_pct": -1.0, "multiple_median": 4.0},
                    "largest_ask_wall": {"price": price * 1.01, "notional": 2_000_000, "distance_pct": 1.0, "multiple_median": 4.0},
                },
            }
        import exchange_market_data as emd
        combined = emd.combine_asset(
            asset,
            {"parsed": exchanges["binance"]},
            {"parsed": exchanges["bybit"]},
            {"parsed": exchanges["kucoin"]},
            {
                "events": 1,
                "long_liquidation_usd": 100_000 if asset == "DOGE" else 0,
                "short_liquidation_usd": 300_000 if asset == "BTC" else 0,
                "largest_event_usd": 300_000,
            },
        )
        combined["price"] = price
        assets[asset] = combined
    return {
        "schema_version": "2.1",
        "generated_utc": "2026-07-11T00:00:00+00:00",
        "snapshot_date": "2026-07-11",
        "liquidation_sample_seconds": 20,
        "assets": assets,
    }


def write_csv(path: Path, fieldnames: list[str], rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def test_report_and_tracker() -> None:
    with tempfile.TemporaryDirectory(prefix="exchange-v2-report-") as tmp_name:
        tmp = Path(tmp_name)
        for name in ("exchange_market_data.py", "exchange_microstructure_report.py", "exchange_signal_tracker.py"):
            shutil.copy2(ROOT / name, tmp / name)
        reports = tmp / "reports"
        reports.mkdir()
        fixture = tmp / "fixture.json"
        fixture.write_text(json.dumps(synthetic_snapshot(), ensure_ascii=False), encoding="utf-8")
        (reports / "latest_report.md").write_text("<!-- LIQUIDATION_SUMMARY_START -->\n", encoding="utf-8")
        write_csv(
            reports / "technical_structure_metrics.csv",
            [
                "asset", "price", "rsi14", "fib_state", "fib_confluence", "wyckoff",
                "dominant_bullish_pattern", "dominant_bullish_status",
                "dominant_bearish_pattern", "dominant_bearish_status", "support", "resistance",
            ],
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
        env["EXCHANGE_TEST_FIXTURE"] = str(fixture)
        subprocess.run([sys.executable, "exchange_market_data.py"], cwd=tmp, env=env, check=True)
        intraday_path = reports / "exchange_market_data_intraday.csv"
        if not intraday_path.exists():
            raise AssertionError("Intraday exchange history was not created")
        intraday_rows = list(csv.DictReader(intraday_path.open(encoding="utf-8")))
        if len(intraday_rows) != 3 or not all(row.get("kucoin_available", "").lower() in {"true", "1"} for row in intraday_rows):
            raise AssertionError(f"Invalid intraday rows: {intraday_rows}")
        # Tracker runs first in the real daily workflow; no history exists yet.
        subprocess.run([sys.executable, "exchange_signal_tracker.py"], cwd=tmp, check=True)
        subprocess.run([sys.executable, "exchange_microstructure_report.py"], cwd=tmp, check=True)

        rows = list(csv.DictReader((reports / "exchange_microstructure_metrics.csv").open(encoding="utf-8")))
        if len(rows) != 3:
            raise AssertionError(f"Expected 3 metric rows, got {len(rows)}")
        for row in rows:
            if row["kucoin_available"].lower() not in {"true", "1"}:
                raise AssertionError(f"KuCoin missing in row: {row}")
            if int(float(row["exchange_count"])) != 3:
                raise AssertionError(f"Expected exchange_count=3: {row}")
            if int(float(row["global_score"])) != 0:
                raise AssertionError(f"Global must stay locked at 0 before calibration: {row}")
        report = (reports / "exchange_microstructure_report.md").read_text(encoding="utf-8")
        for token in ("Binance", "Bybit", "KuCoin", "LOCKED / RACCOLTA 7G"):
            if token not in report:
                raise AssertionError(f"Report token missing: {token}")



def test_persistent_storage() -> None:
    with tempfile.TemporaryDirectory(prefix="exchange-v2-1-storage-") as tmp_name:
        tmp = Path(tmp_name)
        shutil.copy2(ROOT / "exchange_persistent_storage.py", tmp / "exchange_persistent_storage.py")
        reports = tmp / "reports"
        reports.mkdir()
        local_store = tmp / "release-assets"

        # Use dates in a completed month so the permanent archive path is tested.
        rows = [
            {
                "schema_version": "2.1",
                "timestamp_utc": "2026-06-30T23:45:00+00:00",
                "snapshot_date": "2026-06-30",
                "asset": asset,
                "price": value,
            }
            for asset, value in (("BTC", 64000), ("SOL", 78), ("DOGE", 0.074))
        ]
        write_csv(reports / "exchange_market_data_intraday.csv", list(rows[0]), rows)
        (reports / "exchange_market_data_snapshot.json").write_text(
            json.dumps({"schema_version": "2.1", "assets": {}}), encoding="utf-8"
        )
        (reports / "exchange_market_data_health.json").write_text(
            json.dumps({"schema_version": "2.1", "status": "OK"}), encoding="utf-8"
        )

        base = [sys.executable, "exchange_persistent_storage.py", "--local-dir", str(local_store)]
        # argparse expects command before optional args.
        subprocess.run(
            [sys.executable, "exchange_persistent_storage.py", "publish-state", "--local-dir", str(local_store)],
            cwd=tmp,
            check=True,
        )
        first_assets = sorted(path.name for path in local_store.iterdir())
        if len([name for name in first_assets if name.startswith("exchange_state_")]) != 1:
            raise AssertionError(f"First redundant state missing: {first_assets}")

        # Publish a second time: both A and B must then exist.
        subprocess.run(
            [sys.executable, "exchange_persistent_storage.py", "publish-state", "--local-dir", str(local_store)],
            cwd=tmp,
            check=True,
        )
        state_assets = sorted(path.name for path in local_store.iterdir() if path.name.startswith("exchange_state_"))
        if state_assets != ["exchange_state_A.tar.gz", "exchange_state_B.tar.gz"]:
            raise AssertionError(f"Redundant slots invalid: {state_assets}")

        # Corrupt the newest slot and prove automatic fallback to the other copy.
        (local_store / "exchange_state_B.tar.gz").write_bytes(b"corrupted-state")
        for path in reports.iterdir():
            path.unlink()
        subprocess.run(
            [sys.executable, "exchange_persistent_storage.py", "restore", "--local-dir", str(local_store)],
            cwd=tmp,
            check=True,
        )
        restored = list(csv.DictReader((reports / "exchange_market_data_intraday.csv").open(encoding="utf-8")))
        if len(restored) != 3:
            raise AssertionError(f"Persistent restore failed: {restored}")
        status = json.loads((reports / "exchange_storage_status.json").read_text(encoding="utf-8"))
        if not status.get("fallback_used") or status.get("asset") != "exchange_state_A.tar.gz":
            raise AssertionError(f"Redundant fallback was not used: {status}")

        subprocess.run(
            [sys.executable, "exchange_persistent_storage.py", "archive-completed-months", "--local-dir", str(local_store)],
            cwd=tmp,
            check=True,
        )
        archive_name = "exchange_intraday_2026-06.csv.gz"
        archive_path = local_store / "exchange-data-archive-2026" / archive_name
        if not archive_path.exists():
            raise AssertionError(f"Permanent monthly archive not created: {archive_path}")

def test_installer() -> None:
    needed = [
        "global_confluence_report.py",
        "module_signal_tracker.py",
        "compact_latest_report.py",
        "data_quality_coherence_report.py",
    ]
    source_root = ROOT if all((ROOT / name).exists() for name in needed) else ROOT.parent
    missing = [name for name in needed if not (source_root / name).exists()]
    if missing:
        print("Installer integration test skipped; base scanner files unavailable:", ", ".join(missing))
        return

    with tempfile.TemporaryDirectory(prefix="exchange-v2-install-") as tmp_name:
        tmp = Path(tmp_name)
        for name in needed:
            shutil.copy2(source_root / name, tmp / name)
        for name in (
            "exchange_market_data.py",
            "exchange_microstructure_report.py",
            "exchange_signal_tracker.py",
            "exchange_microstructure_selftest.py",
            "exchange_persistent_storage.py",
            "requirements-exchange.txt",
            "requirements-exchange-collector.txt",
            "apply_exchange_microstructure_upgrade_v2_1.py",
        ):
            shutil.copy2(ROOT / name, tmp / name)
        workflow = tmp / ".github" / "workflows" / "daily.yml"
        workflow.parent.mkdir(parents=True)
        workflow.write_text(
            """name: Daily\non: workflow_dispatch\njobs:\n  run:\n    runs-on: ubuntu-latest\n    steps:\n      - name: Setup\n        run: echo setup\n      - name: Technical\n        run: python technical_structure_report.py\n      - name: Global\n        run: python global_confluence_report.py\n      - name: Compact\n        run: python compact_latest_report.py\n""",
            encoding="utf-8",
        )
        subprocess.run([sys.executable, "apply_exchange_microstructure_upgrade_v2_1.py"], cwd=tmp, check=True)
        global_text = (tmp / "global_confluence_report.py").read_text(encoding="utf-8")
        tracker_text = (tmp / "module_signal_tracker.py").read_text(encoding="utf-8")
        daily_text = workflow.read_text(encoding="utf-8")
        if "exchange_candidate_score_component" not in global_text:
            raise AssertionError("Global candidate field not installed")
        if '"score_col": "exchange_candidate_score_component"' not in tracker_text:
            raise AssertionError("Module tracker does not calibrate candidate")
        positions = [daily_text.find(token) for token in (
            "python exchange_persistent_storage.py restore",
            "python exchange_persistent_storage.py audit",
            "python exchange_persistent_storage.py archive-completed-months",
            "python exchange_signal_tracker.py",
            "python exchange_microstructure_report.py",
            "python global_confluence_report.py",
        )]
        if positions != sorted(positions) or min(positions) < 0:
            raise AssertionError(f"Daily order invalid: {positions}")


def main() -> None:
    test_kucoin_parser()
    test_report_and_tracker()
    test_persistent_storage()
    test_installer()
    print("Exchange Microstructure Upgrade v2.1 self-test: OK")


if __name__ == "__main__":
    main()
