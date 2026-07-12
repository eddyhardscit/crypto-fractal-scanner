# -*- coding: utf-8 -*-
"""Offline end-to-end self-test for paper trading v1."""

from __future__ import annotations

import csv
import json
import os
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, timedelta, timezone
from pathlib import Path

RUNTIME_FILES = (
    "paper_trading_config.json",
    "paper_trading_config.py",
    "kucoin_public_data.py",
    "paper_signal_engine.py",
    "paper_trading_engine.py",
    "paper_trading_report.py",
    "paper_trading_notify.py",
    "paper_trading_live_publish.py",
    "telegram_scanner_notify.py",
    "paper_trading_runner.py",
)
ROOT = Path(__file__).resolve().parent


def candle_rows(start: datetime, count: int, minutes: int, start_price: float, drift: float, volatility: float = 0.003):
    rows = []
    price = start_price
    for index in range(count):
        opened = price
        close = opened * (1.0 + drift)
        high = max(opened, close) * (1.0 + volatility)
        low = min(opened, close) * (1.0 - volatility)
        volume = 1000.0 + index * 2
        rows.append(
            {
                "time": (start + timedelta(minutes=minutes * index)).isoformat(),
                "open": opened,
                "high": high,
                "low": low,
                "close": close,
                "volume": volume,
            }
        )
        price = close
    # Make the last candle a clear volume-backed breakout.
    rows[-1]["close"] *= 1.012
    rows[-1]["high"] = rows[-1]["close"] * 1.004
    rows[-1]["volume"] *= 3.0
    return rows


def make_fixture(path: Path, crash: bool = False) -> None:
    now = datetime(2026, 7, 12, 12, 0, tzinfo=timezone.utc)
    assets = {}
    specs = {"BTC": (65000.0, 0.0010), "SOL": (95.0, 0.0016), "HYPE": (40.0, 0.0019)}
    for asset, (price, drift) in specs.items():
        candles = {
            "15": candle_rows(now - timedelta(minutes=15 * 260), 260, 15, price, drift),
            "60": candle_rows(now - timedelta(minutes=60 * 260), 260, 60, price, drift),
            "240": candle_rows(now - timedelta(minutes=240 * 260), 260, 240, price, drift),
        }
        mark = candles["15"][-1]["close"]
        if crash:
            candles["15"][-1]["low"] = mark * 0.50
            candles["15"][-1]["close"] = mark * 0.95
            mark = candles["15"][-1]["close"]
        assets[asset] = {
            "symbol": "XBTUSDTM" if asset == "BTC" else f"{asset}USDTM",
            "mark_price": mark,
            "turnover_24h": 500_000_000,
            "volume_24h": 10_000_000,
            "multiplier": 1.0,
            "funding_rate": 0.0001,
            "candles": candles,
        }
    payload = {
        "schema_version": 1,
        "generated_utc": now.isoformat(),
        "source": "OFFLINE_SELFTEST",
        "eur_usdt_rate": 1.08,
        "eur_usdt_rate_source": "SELFTEST",
        "assets": assets,
        "failures": [],
    }
    path.write_text(json.dumps(payload), encoding="utf-8")


def write_csv(path: Path, fieldnames: list[str], rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def run_runner(tmp: Path, fixture: Path, reset: bool = False) -> dict:
    env = os.environ.copy()
    env["PAPER_TRADING_FIXTURE"] = str(fixture)
    env["PAPER_TRADING_CONFIG"] = str(tmp / "paper_trading_config.json")
    if reset:
        env["PAPER_RESET_STATE"] = "true"
    else:
        env.pop("PAPER_RESET_STATE", None)
    output = subprocess.check_output([sys.executable, "paper_trading_runner.py"], cwd=tmp, env=env, text=True)
    return json.loads(output.strip().splitlines()[-1])


def main() -> None:
    with tempfile.TemporaryDirectory(prefix="paper-trading-v1-") as directory:
        tmp = Path(directory)
        for name in RUNTIME_FILES:
            shutil.copy2(ROOT / name, tmp / name)
        reports = tmp / "reports"
        reports.mkdir()
        (reports / "latest_report.md").write_text("# Scanner\n", encoding="utf-8")
        write_csv(
            reports / "global_confluence_metrics.csv",
            ["asset", "global_score", "action"],
            [
                {"asset": "BTC", "global_score": 6, "action": "LONG"},
                {"asset": "SOL", "global_score": 6, "action": "LONG"},
                {"asset": "HYPE", "global_score": 6, "action": "LONG"},
            ],
        )
        write_csv(
            reports / "exchange_microstructure_metrics.csv",
            ["asset", "candidate_global_score", "data_coverage"],
            [
                {"asset": "BTC", "candidate_global_score": 4, "data_coverage": 1},
                {"asset": "SOL", "candidate_global_score": 4, "data_coverage": 1},
                {"asset": "HYPE", "candidate_global_score": 4, "data_coverage": 1},
            ],
        )

        fixture = tmp / "fixture.json"
        make_fixture(fixture, crash=False)
        first = run_runner(tmp, fixture)
        if first["opened"] < 3:
            raise AssertionError(f"Attese aperture automatiche, risultato: {first}")

        state = json.loads((reports / "paper_trading_state.json").read_text(encoding="utf-8"))
        main_portfolio = state["portfolios"]["MAIN"]
        if abs(float(state["initial_capital_eur"]) - 10_000.0) > 1e-9:
            raise AssertionError("Capitale iniziale errato")
        if not main_portfolio["open_positions"]:
            raise AssertionError("Il portafoglio MAIN non ha aperto posizioni")

        signal_rows = list(csv.DictReader((reports / "paper_trading_signal_log.csv").open(encoding="utf-8")))
        opened_rows = [row for row in signal_rows if row["decision"] == "OPENED"]
        unique_groups = {row["experiment_group_id"] for row in opened_rows}
        if len(unique_groups) >= len(opened_rows):
            raise AssertionError("Le varianti ombra non risultano raggruppate per evento di mercato")

        make_fixture(fixture, crash=True)
        second = run_runner(tmp, fixture)
        if second["closed"] < 1:
            raise AssertionError(f"Lo stop sintetico non ha chiuso operazioni: {second}")
        trades = list(csv.DictReader((reports / "paper_trading_trade_log.csv").open(encoding="utf-8")))
        if not trades or not all(row["close_reason"] for row in trades):
            raise AssertionError("Trade log non valido")
        if "PAPER_TRADING_START" not in (reports / "latest_report.md").read_text(encoding="utf-8"):
            raise AssertionError("Report non inserito nel latest_report.md")

        # Flexibility test: 20k capital and 1k target on a fresh state.
        config = json.loads((tmp / "paper_trading_config.json").read_text(encoding="utf-8"))
        config["initial_capital_eur"] = 20_000
        config["monthly_target_eur"] = 1_000
        (tmp / "paper_trading_config.json").write_text(json.dumps(config), encoding="utf-8")
        fresh = run_runner(tmp, fixture, reset=True)
        state = json.loads((reports / "paper_trading_state.json").read_text(encoding="utf-8"))
        if float(state["initial_capital_eur"]) != 20_000:
            raise AssertionError("Il capitale configurabile non è stato applicato")
        snapshot = json.loads((reports / "paper_trading_config_snapshot.json").read_text(encoding="utf-8"))
        if float(snapshot["monthly_target_eur"]) != 1_000:
            raise AssertionError("Il target mensile configurabile non è stato applicato")

        print("Paper Trading Upgrade v1 self-test: OK", first, second, fresh)


if __name__ == "__main__":
    main()
