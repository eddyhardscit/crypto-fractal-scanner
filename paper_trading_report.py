# -*- coding: utf-8 -*-
"""Markdown and CSV reporting for automatic paper trading."""

from __future__ import annotations

import csv
import json
import math
import os
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import pandas as pd

from paper_trading_config import load_config
from paper_trading_engine import STATE_PATH, TRADE_LOG_PATH
from paper_trading_sample_watch import sample_snapshot

REPORTS_DIR = Path("reports")
REPORT_PATH = REPORTS_DIR / "paper_trading_report.md"
LIVE_REPORT_PATH = REPORTS_DIR / "paper_trading_live.md"
LATEST_REPORT_PATH = REPORTS_DIR / "latest_report.md"
MARKET_CACHE_PATH = REPORTS_DIR / "paper_trading_market_cache.json"
METRICS_PATH = REPORTS_DIR / "paper_trading_shadow_metrics.csv"
START_MARKER = "<!-- PAPER_TRADING_START -->"
END_MARKER = "<!-- PAPER_TRADING_END -->"


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def fmt_eur(value: Any) -> str:
    try:
        return f"€{float(value):,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    except Exception:
        return "n/a"


def fmt_pct(value: Any, signed: bool = False) -> str:
    try:
        number = float(value)
        prefix = "+" if signed and number > 0 else ""
        return f"{prefix}{number:.2f}%".replace(".", ",")
    except Exception:
        return "n/a"


def fmt_num(value: Any, digits: int = 2) -> str:
    try:
        number = float(value)
        if math.isinf(number):
            return "∞"
        return f"{number:.{digits}f}".replace(".", ",")
    except Exception:
        return "n/a"


def md_table(headers: list[str], rows: list[list[Any]]) -> str:
    lines = ["| " + " | ".join(headers) + " |", "| " + " | ".join(["---"] * len(headers)) + " |"]
    lines.extend("| " + " | ".join(str(x) for x in row) + " |" for row in rows)
    return "\n".join(lines)


def read_json(path: Path, default: Any) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return default


def load_trades() -> pd.DataFrame:
    if not TRADE_LOG_PATH.exists():
        return pd.DataFrame()
    try:
        return pd.read_csv(TRADE_LOG_PATH)
    except Exception:
        return pd.DataFrame()


def market_prices() -> tuple[dict[str, float], float, str, str]:
    payload = read_json(MARKET_CACHE_PATH, {})
    prices: dict[str, float] = {}
    for asset, row in payload.get("assets", {}).items():
        try:
            prices[asset] = float(row.get("mark_price"))
        except Exception:
            pass
    return (
        prices,
        float(payload.get("eur_usdt_rate", 1.0) or 1.0),
        str(payload.get("eur_usdt_rate_source", "n/a")),
        str(payload.get("generated_utc", "n/a")),
    )


def unrealized(position: dict[str, Any], prices: dict[str, float], eur_rate: float) -> float:
    mark = prices.get(position["asset"], float(position["entry_price"]))
    direction = 1.0 if position["side"] == "LONG" else -1.0
    return (mark - float(position["entry_price"])) * float(position["quantity"]) * direction / eur_rate


def portfolio_metrics(state: dict[str, Any], config: dict[str, Any]) -> list[dict[str, Any]]:
    trades = load_trades()
    prices, eur_rate, _, _ = market_prices()
    target = float(config.get("monthly_target_eur", 0.0))
    rows: list[dict[str, Any]] = []

    for name, portfolio in state.get("portfolios", {}).items():
        unreal = sum(unrealized(position, prices, eur_rate) for position in portfolio.get("open_positions", []))
        equity = float(portfolio.get("balance_eur", 0.0)) + unreal
        month_start = float(portfolio.get("periods", {}).get("month_start_equity_eur", equity))
        month_pnl = equity - month_start
        subset = trades[trades["portfolio"].astype(str) == name].copy() if not trades.empty and "portfolio" in trades.columns else pd.DataFrame()
        if subset.empty:
            trade_count = wins = unique_events = 0
            net = expectancy = win_rate = 0.0
            profit_factor = 0.0
        else:
            pnl = pd.to_numeric(subset.get("net_pnl_eur"), errors="coerce").fillna(0.0)
            trade_count = len(subset)
            wins = int((pnl > 0).sum())
            unique_events = subset.get("experiment_group_id", pd.Series(dtype=str)).astype(str).nunique()
            net = float(pnl.sum())
            expectancy = float(pnl.mean())
            win_rate = wins / trade_count * 100.0
            gross_profit = float(pnl[pnl > 0].sum())
            gross_loss = abs(float(pnl[pnl < 0].sum()))
            profit_factor = gross_profit / gross_loss if gross_loss > 0 else (math.inf if gross_profit > 0 else 0.0)
        rows.append(
            {
                "generated_utc": now_iso(),
                "portfolio": name,
                "is_main": bool(portfolio.get("is_main")),
                "strategy": portfolio.get("strategy", ""),
                "equity_eur": equity,
                "balance_eur": portfolio.get("balance_eur", 0.0),
                "unrealized_pnl_eur": unreal,
                "month_pnl_eur": month_pnl,
                "monthly_target_eur": target,
                "target_progress_pct": month_pnl / target * 100.0 if target > 0 else 0.0,
                "open_positions": len(portfolio.get("open_positions", [])),
                "closed_trades": trade_count,
                "unique_market_events": unique_events,
                "winning_trades": wins,
                "win_rate_pct": win_rate,
                "profit_factor": profit_factor,
                "expectancy_eur": expectancy,
                "net_pnl_closed_eur": net,
                "max_drawdown_pct": float(portfolio.get("max_drawdown_pct", 0.0)),
            }
        )
    return rows


def write_metrics(rows: list[dict[str, Any]]) -> None:
    fields = [
        "generated_utc", "portfolio", "is_main", "strategy", "equity_eur", "balance_eur",
        "unrealized_pnl_eur", "month_pnl_eur", "monthly_target_eur", "target_progress_pct",
        "open_positions", "closed_trades", "unique_market_events", "winning_trades", "win_rate_pct",
        "profit_factor", "expectancy_eur", "net_pnl_closed_eur", "max_drawdown_pct"
    ]
    METRICS_PATH.parent.mkdir(parents=True, exist_ok=True)
    with METRICS_PATH.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def open_position_rows(state: dict[str, Any]) -> list[list[Any]]:
    prices, eur_rate, _, _ = market_prices()
    rows: list[list[Any]] = []
    for name, portfolio in state.get("portfolios", {}).items():
        for position in portfolio.get("open_positions", []):
            mark = prices.get(position["asset"], float(position["entry_price"]))
            pnl = unrealized(position, prices, eur_rate)
            rows.append(
                [
                    name,
                    position["asset"],
                    position["side"],
                    position["strategy"],
                    f"{position['timeframe_minutes']}m",
                    fmt_num(position["entry_price"], 5),
                    fmt_num(mark, 5),
                    fmt_num(position["stop_price"], 5),
                    fmt_num(position["target_price"], 5),
                    fmt_eur(position["margin_eur"]),
                    fmt_eur(pnl),
                ]
            )
    return rows


def recent_closed_rows(limit: int = 12) -> list[list[Any]]:
    trades = load_trades()
    if trades.empty:
        return []
    ordered = trades.tail(limit).iloc[::-1]
    rows: list[list[Any]] = []
    for _, trade in ordered.iterrows():
        rows.append(
            [
                str(trade.get("portfolio", "")),
                str(trade.get("asset", "")),
                str(trade.get("side", "")),
                str(trade.get("closed_at", "")),
                fmt_num(trade.get("exit_price"), 5),
                fmt_eur(trade.get("net_pnl_eur")),
                fmt_num(trade.get("r_multiple")),
                str(trade.get("close_reason", "")),
            ]
        )
    return rows


def render_report(state: dict[str, Any], config: dict[str, Any]) -> str:
    metrics = portfolio_metrics(state, config)
    write_metrics(metrics)
    _, _, rate_source, market_generated = market_prices()
    main = next((row for row in metrics if row["is_main"]), metrics[0] if metrics else None)
    initial = float(state.get("initial_capital_eur", config["initial_capital_eur"]))
    configured_initial = float(config["initial_capital_eur"])
    target = float(config["monthly_target_eur"])
    sample = sample_snapshot(state, config)

    lines = [
        "# Paper trading automatico KuCoin",
        "",
        f"Generato: {now_iso()}",
        "",
        "## Configurazione attiva",
        "",
        f"- Capitale iniziale della simulazione: **{fmt_eur(initial)}**",
        f"- Capitale indicato nel file di configurazione: **{fmt_eur(configured_initial)}**",
        f"- Obiettivo mensile monitorato: **{fmt_eur(target)}**",
        f"- Compounding: **{'ATTIVO' if config.get('compounding_enabled') else 'DISATTIVO'}**",
        f"- Reinvestimento dei profitti: **{fmt_pct(float(config.get('reinvestment_rate', 1.0)) * 100)}**",
        "- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**",
        f"- Ultimi prezzi: **{market_generated}**; conversione EUR/USDT: **{rate_source}**",
        (
            "- Dashboard intraday: "
            f"[apri la pagina live](https://github.com/{os.getenv('GITHUB_REPOSITORY', 'eddyhardscit/crypto-fractal-scanner')}/blob/"
            f"{config.get('notifications', {}).get('live_report_branch', 'paper-trading-live')}/reports/paper_trading_live.md)"
        ),
        "",
    ]

    if main:
        total_return = (float(main["equity_eur"]) / initial - 1.0) * 100.0 if initial > 0 else 0.0
        lines.extend(
            [
                "## Portafoglio principale",
                "",
                md_table(
                    ["Equity", "Rendimento", "P&L mese", "Target", "Progresso", "Aperte", "Chiuse", "Win rate", "PF", "Max DD"],
                    [[
                        fmt_eur(main["equity_eur"]),
                        fmt_pct(total_return, signed=True),
                        fmt_eur(main["month_pnl_eur"]),
                        fmt_eur(target),
                        fmt_pct(main["target_progress_pct"]),
                        main["open_positions"],
                        main["closed_trades"],
                        fmt_pct(main["win_rate_pct"]),
                        fmt_num(main["profit_factor"]),
                        fmt_pct(main["max_drawdown_pct"]),
                    ]],
                ),
                "",
            ]
        )

    next_milestone = sample.get("next_milestone")
    next_text = (
        f"{next_milestone} (mancano {sample['remaining_to_next']})"
        if next_milestone is not None
        else "tutte le soglie raggiunte"
    )
    lines.extend(
        [
            "## Stato del campione statistico",
            "",
            md_table(
                [
                    "MAIN eventi indip.",
                    "Sistema eventi indip.",
                    "Stato",
                    "Prossima soglia",
                ],
                [[
                    sample["main_independent_events"],
                    sample["system_independent_events"],
                    sample["status"],
                    next_text,
                ]],
            ),
            "",
            (
                f"- Trade MAIN chiusi: **{sample['closed_trades']}**; "
                f"win rate **{fmt_pct(sample['win_rate_pct'])}**; "
                f"profit factor **{fmt_num(sample['profit_factor'])}**."
            ),
            (
                f"- Expectancy: **{fmt_eur(sample['expectancy_eur'])}** "
                f"per trade; P&L netto: "
                f"**{fmt_eur(sample['net_pnl_eur'])}**; "
                f"max drawdown: "
                f"**{fmt_pct(sample['max_drawdown_pct'])}**."
            ),
            f"- Valutazione: **{sample['meaning']}**",
            (
                "- Soglie automatiche Telegram: **30, 100, 200 "
                "e 300 eventi indipendenti chiusi del MAIN**."
            ),
            (
                "- Una soglia richiede una valutazione; non attiva "
                "automaticamente il trading reale."
            ),
            "",
        ]
    )
    lines.extend(["## Confronto portafogli", ""])
    ordered = sorted(metrics, key=lambda row: (not row["is_main"], -float(row["equity_eur"])))
    comparison_rows = []
    for row in ordered:
        comparison_rows.append(
            [
                "MAIN" if row["is_main"] else "OMBRA",
                row["portfolio"],
                row["strategy"],
                fmt_eur(row["equity_eur"]),
                fmt_eur(row["net_pnl_closed_eur"]),
                row["closed_trades"],
                row["unique_market_events"],
                fmt_pct(row["win_rate_pct"]),
                fmt_num(row["profit_factor"]),
                fmt_eur(row["expectancy_eur"]),
                fmt_pct(row["max_drawdown_pct"]),
            ]
        )
    lines.extend(
        [
            md_table(
                ["Tipo", "Portafoglio", "Strategia", "Equity", "P&L chiuso", "Trade", "Eventi indip.", "Win rate", "PF", "Expectancy", "Max DD"],
                comparison_rows,
            ),
            "",
            "**Eventi indip.** conta gli eventi di mercato distinti; le varianti di stop, target e timeframe restano collegate allo stesso evento sperimentale.",
            "",
            "## Posizioni aperte",
            "",
        ]
    )
    positions = open_position_rows(state)
    if positions:
        lines.append(md_table(["Portafoglio", "Asset", "Lato", "Strategia", "TF", "Entry", "Mark", "Stop", "Target", "Margine", "P&L"], positions))
    else:
        lines.append("_Nessuna posizione virtuale aperta._")

    lines.extend(["", "## Ultime operazioni chiuse", ""])
    recent = recent_closed_rows()
    if recent:
        lines.append(md_table(["Portafoglio", "Asset", "Lato", "Chiusura UTC", "Exit", "P&L netto", "R", "Motivo"], recent))
    else:
        lines.append("_Nessuna operazione virtuale chiusa._")

    lines.extend(
        [
            "",
            "## Regole invarianti",
            "",
            "- Nessuna martingala e nessuna mediazione automatica in perdita.",
            "- Il target mensile riduce il rischio quando viene avvicinato o raggiunto; non lo aumenta mai.",
            "- Il portafoglio principale e quelli ombra hanno contabilità separata.",
            "- Commissioni, slippage e funding sono inclusi nella simulazione secondo i parametri configurati.",
            "- Quando stop e target risultano toccati nella stessa candela, prevale lo stop salvo modifica esplicita della configurazione.",
            "",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def replace_block(text: str, report: str) -> str:
    full = f"{START_MARKER}\n{report.rstrip()}\n{END_MARKER}"
    pattern = re.compile(re.escape(START_MARKER) + r".*?" + re.escape(END_MARKER), re.DOTALL)
    if pattern.search(text):
        return pattern.sub(full, text)
    decision_end = "<!-- DECISION_REPORT_END -->"
    if decision_end in text:
        return text.replace(decision_end, decision_end + "\n\n" + full, 1)
    return text.rstrip() + "\n\n" + full + "\n"


def main() -> None:
    config = load_config()
    state = read_json(STATE_PATH, {})
    if not state:
        raise SystemExit("Stato paper trading non disponibile. Eseguire prima paper_trading_runner.py.")
    report = render_report(state, config)
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(report, encoding="utf-8")
    LIVE_REPORT_PATH.write_text(report, encoding="utf-8")
    latest = LATEST_REPORT_PATH.read_text(encoding="utf-8") if LATEST_REPORT_PATH.exists() else ""
    LATEST_REPORT_PATH.write_text(replace_block(latest, report), encoding="utf-8")
    print(f"Paper trading report aggiornato: {REPORT_PATH}")


if __name__ == "__main__":
    main()
