# -*- coding: utf-8 -*-
"""Daily comparative ranking for all automatic paper-trading portfolios."""

from __future__ import annotations

import csv
import json
import math
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import pandas as pd
import requests

from paper_trading_config import load_config
from paper_trading_display import portfolio_label
from paper_trading_engine import STATE_PATH, TRADE_FIELDS, TRADE_LOG_PATH
from paper_trading_report import market_prices, unrealized
from paper_trading_trade_log_repair import load_trade_frame_resilient

REPORTS_DIR = Path("reports")
REPORT_PATH = REPORTS_DIR / "paper_trading_comparative_report.md"
CSV_PATH = REPORTS_DIR / "paper_trading_comparative_ranking.csv"
JSON_PATH = REPORTS_DIR / "paper_trading_comparative_latest.json"


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def safe_float(value: Any, default: float = 0.0) -> float:
    try:
        number = float(value)
        return number if math.isfinite(number) else default
    except Exception:
        return default


def fmt_eur(value: Any, signed: bool = False) -> str:
    number = safe_float(value)
    prefix = "+" if signed and number > 0 else ""
    return (
        f"{prefix}€{number:,.2f}"
        .replace(",", "X")
        .replace(".", ",")
        .replace("X", ".")
    )


def fmt_pct(value: Any, signed: bool = False) -> str:
    number = safe_float(value)
    prefix = "+" if signed and number > 0 else ""
    return f"{prefix}{number:.2f}%".replace(".", ",")


def fmt_ratio(value: Any) -> str:
    number = safe_float(value)
    return f"{number:.2f}".replace(".", ",")


def sample_status(closed: int) -> tuple[str, int]:
    if closed <= 0:
        return "IN ATTESA", 0
    if closed < 10:
        return "PRELIMINARE", 1
    if closed < 30:
        return "IN OSSERVAZIONE", 2
    if closed < 100:
        return "VALUTABILE", 3
    return "ROBUSTO", 4


def load_state() -> dict[str, Any]:
    if not STATE_PATH.exists():
        raise FileNotFoundError(
            "Stato paper trading non trovato. Eseguire prima il restore."
        )
    return json.loads(STATE_PATH.read_text(encoding="utf-8"))


def load_trades() -> pd.DataFrame:
    return load_trade_frame_resilient(TRADE_LOG_PATH, TRADE_FIELDS)


def compute_score(row: dict[str, Any]) -> float:
    """Conservative comparison score; never used to allocate capital."""
    closed = int(row["closed_trades"])
    if closed <= 0:
        return -1_000_000.0

    sample_weight = min(1.0, math.sqrt(closed / 30.0))
    return_pct = safe_float(row["total_return_pct"])
    pf = min(3.0, max(0.0, safe_float(row["profit_factor"])))
    win_rate = safe_float(row["win_rate_pct"])
    drawdown = abs(safe_float(row["max_drawdown_pct"]))
    retention = safe_float(row["average_profit_retained_pct"])
    expectancy = safe_float(row["expectancy_eur"])

    raw = (
        return_pct * 4.0
        + (pf - 1.0) * 5.0
        + (win_rate - 50.0) * 0.08
        - drawdown * 1.5
        + max(-100.0, min(100.0, retention)) * 0.015
        + max(-50.0, min(50.0, expectancy)) * 0.03
    )
    return raw * sample_weight


def build_rows() -> list[dict[str, Any]]:
    config = load_config()
    state = load_state()
    trades = load_trades()
    prices, eur_rate, _, _ = market_prices()
    initial = safe_float(config.get("initial_capital_eur"), 10_000.0)

    rows: list[dict[str, Any]] = []

    configured_names = [
        str(item["name"])
        for item in config.get("portfolios", [])
        if item.get("enabled", True)
    ]

    for name in configured_names:
        portfolio = state.get("portfolios", {}).get(name, {})
        positions = list(portfolio.get("open_positions", []))
        open_pnl = sum(
            unrealized(position, prices, eur_rate)
            for position in positions
        )
        balance = safe_float(portfolio.get("balance_eur"), initial)
        equity = balance + open_pnl
        closed_pnl_fallback = (
            safe_float(portfolio.get("gross_profit_eur"))
            - safe_float(portfolio.get("gross_loss_eur"))
        )

        subset = (
            trades[trades["portfolio"].astype(str) == name].copy()
            if not trades.empty and "portfolio" in trades.columns
            else pd.DataFrame()
        )

        state_closed = int(portfolio.get("closed_trades", 0))
        csv_closed = len(subset)
        closed = max(state_closed, csv_closed)
        wins = int(portfolio.get("winning_trades", 0))
        closed_pnl = closed_pnl_fallback
        profit_factor = 0.0
        expectancy = 0.0
        avg_mfe = 0.0
        avg_mae = 0.0
        avg_retention = 0.0
        retention_sample = 0

        if not subset.empty:
            pnl = pd.to_numeric(
                subset.get("net_pnl_eur"), errors="coerce"
            ).fillna(0.0)
            csv_wins = int((pnl > 0).sum())
            if csv_closed >= state_closed:
                wins = csv_wins
                closed_pnl = float(pnl.sum())
            expectancy = float(pnl.mean()) if len(pnl) else 0.0
            gross_profit = float(pnl[pnl > 0].sum())
            gross_loss = abs(float(pnl[pnl < 0].sum()))
            profit_factor = (
                gross_profit / gross_loss
                if gross_loss > 0
                else (3.0 if gross_profit > 0 else 0.0)
            )

            if "mfe_net_eur" in subset.columns:
                mfe = pd.to_numeric(
                    subset["mfe_net_eur"], errors="coerce"
                )
                mae = pd.to_numeric(
                    subset.get("mae_net_eur"), errors="coerce"
                )
                retention = pd.to_numeric(
                    subset.get("profit_retained_pct"), errors="coerce"
                )
                valid_mfe = mfe.notna()
                avg_mfe = (
                    float(mfe[valid_mfe].mean())
                    if valid_mfe.any()
                    else 0.0
                )
                avg_mae = (
                    float(mae.dropna().mean())
                    if mae.notna().any()
                    else 0.0
                )
                valid_retention = retention.notna() & (mfe > 0)
                retention_sample = int(valid_retention.sum())
                avg_retention = (
                    float(retention[valid_retention].mean())
                    if retention_sample
                    else 0.0
                )

        if closed and not profit_factor:
            profit = safe_float(portfolio.get("gross_profit_eur"))
            loss = safe_float(portfolio.get("gross_loss_eur"))
            profit_factor = (
                profit / loss if loss > 0 else (3.0 if profit > 0 else 0.0)
            )
            expectancy = closed_pnl / closed

        win_rate = wins / closed * 100.0 if closed else 0.0
        total_pnl = equity - initial
        total_return = total_pnl / initial * 100.0 if initial > 0 else 0.0
        status, maturity = sample_status(closed)

        row = {
            "portfolio": name,
            "label": portfolio_label(name),
            "strategy": str(portfolio.get("strategy", "")),
            "equity_eur": equity,
            "total_pnl_eur": total_pnl,
            "total_return_pct": total_return,
            "closed_pnl_eur": closed_pnl,
            "open_pnl_eur": open_pnl,
            "open_positions": len(positions),
            "closed_trades": closed,
            "winning_trades": wins,
            "win_rate_pct": win_rate,
            "profit_factor": profit_factor,
            "expectancy_eur": expectancy,
            "max_drawdown_pct": safe_float(
                portfolio.get("max_drawdown_pct")
            ),
            "average_mfe_net_eur": avg_mfe,
            "average_mae_net_eur": avg_mae,
            "average_profit_retained_pct": avg_retention,
            "profit_retention_sample": retention_sample,
            "sample_status": status,
            "sample_maturity": maturity,
        }
        row["comparison_score"] = compute_score(row)
        rows.append(row)

    rows.sort(
        key=lambda item: (
            item["sample_maturity"],
            item["comparison_score"],
            item["total_return_pct"],
        ),
        reverse=True,
    )
    for rank, row in enumerate(rows, start=1):
        row["rank"] = rank
    return rows


def markdown_report(rows: list[dict[str, Any]]) -> str:
    generated = now_iso()
    active = [row for row in rows if row["closed_trades"] > 0]
    evaluable = [row for row in rows if row["closed_trades"] >= 30]
    robust = [row for row in rows if row["closed_trades"] >= 100]

    lines = [
        "# Classifica comparativa conti paper",
        "",
        f"Generato: {generated}",
        "",
        "> La classifica privilegia l'ampiezza del campione. "
        "Non autorizza rotazioni automatiche del capitale.",
        "",
        "## Stato del campione",
        "",
        f"- Conti totali: **{len(rows)}**",
        f"- Con almeno un trade chiuso: **{len(active)}**",
        f"- Valutabili (≥30 trade): **{len(evaluable)}**",
        f"- Robusti (≥100 trade): **{len(robust)}**",
        "",
        "## Classifica generale",
        "",
        "| # | Conto | Campione | Trade | Totale | Chiuso | Aperto | Win | PF | DD max | MFE medio | MAE medio | Trattenuto |",
        "| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]

    for row in rows:
        retention = (
            fmt_pct(row["average_profit_retained_pct"])
            if row["profit_retention_sample"] > 0
            else "N/D"
        )
        lines.append(
            "| {rank} | {label} | {status} | {closed} | {total} | "
            "{closed_pnl} | {open_pnl} | {win} | {pf} | {dd} | "
            "{mfe} | {mae} | {retention} |".format(
                rank=row["rank"],
                label=row["label"],
                status=row["sample_status"],
                closed=row["closed_trades"],
                total=fmt_eur(row["total_pnl_eur"], signed=True),
                closed_pnl=fmt_eur(row["closed_pnl_eur"], signed=True),
                open_pnl=fmt_eur(row["open_pnl_eur"], signed=True),
                win=fmt_pct(row["win_rate_pct"]),
                pf=fmt_ratio(row["profit_factor"]),
                dd=fmt_pct(row["max_drawdown_pct"]),
                mfe=fmt_eur(row["average_mfe_net_eur"], signed=True),
                mae=fmt_eur(row["average_mae_net_eur"], signed=True),
                retention=retention,
            )
        )

    lines.extend([
        "",
        "## Interpretazione",
        "",
        "- **IN ATTESA:** 0 trade chiusi.",
        "- **PRELIMINARE:** 1–9 trade.",
        "- **IN OSSERVAZIONE:** 10–29 trade.",
        "- **VALUTABILE:** 30–99 trade.",
        "- **ROBUSTO:** almeno 100 trade.",
        "",
        "La rotazione del capitale virtuale deve restare disattivata "
        "finché non esistono più strategie con campione almeno valutabile.",
        "",
    ])
    return "\n".join(lines)


def telegram_report(rows: list[dict[str, Any]]) -> str:
    active = [row for row in rows if row["closed_trades"] > 0]
    evaluable = [row for row in rows if row["closed_trades"] >= 30]
    top = active[:10]

    lines = [
        "🏆 <b>CLASSIFICA COMPARATIVA CONTI PAPER</b>",
        "",
        f"Conti: <b>{len(rows)}</b> · attivi: <b>{len(active)}</b> · "
        f"valutabili ≥30 trade: <b>{len(evaluable)}</b>",
        "",
    ]

    if not top:
        lines.extend([
            "Nessun conto ha ancora trade chiusi.",
            "La classifica resta in attesa di dati.",
        ])
    else:
        for row in top:
            retention = (
                fmt_pct(row["average_profit_retained_pct"])
                if row["profit_retention_sample"] > 0
                else "N/D"
            )
            lines.extend([
                f"<b>{row['rank']}. {row['label']}</b>",
                f"{row['sample_status']} · {row['closed_trades']} trade",
                f"Totale {fmt_eur(row['total_pnl_eur'], signed=True)} · "
                f"Win {fmt_pct(row['win_rate_pct'])} · "
                f"PF {fmt_ratio(row['profit_factor'])}",
                f"DD {fmt_pct(row['max_drawdown_pct'])} · "
                f"MFE {fmt_eur(row['average_mfe_net_eur'], signed=True)} · "
                f"MAE {fmt_eur(row['average_mae_net_eur'], signed=True)} · "
                f"trattenuto {retention}",
                "",
            ])

    lines.extend([
        "⚠️ <b>Nessuna rotazione automatica del capitale.</b>",
        "Prima servono campioni sufficienti e stabili.",
    ])
    return "\n".join(lines)


def send_telegram(text: str) -> None:
    token = os.getenv("TELEGRAM_BOT_TOKEN", "").strip()
    chat_id = os.getenv("TELEGRAM_CHAT_ID", "").strip()
    if not token or not chat_id:
        print("Telegram secrets mancanti: report generato senza invio.")
        return

    response = requests.post(
        f"https://api.telegram.org/bot{token}/sendMessage",
        json={
            "chat_id": chat_id,
            "text": text,
            "parse_mode": "HTML",
            "disable_web_page_preview": True,
        },
        timeout=30,
    )
    response.raise_for_status()
    payload = response.json()
    if not payload.get("ok"):
        raise RuntimeError(f"Telegram API error: {payload}")


def write_outputs(rows: list[dict[str, Any]]) -> None:
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(markdown_report(rows), encoding="utf-8")
    JSON_PATH.write_text(
        json.dumps(
            {
                "generated_utc": now_iso(),
                "account_count": len(rows),
                "rows": rows,
            },
            ensure_ascii=False,
            indent=2,
            allow_nan=False,
        ),
        encoding="utf-8",
    )

    fields = [
        "rank", "portfolio", "label", "strategy", "sample_status",
        "sample_maturity", "closed_trades", "winning_trades",
        "win_rate_pct", "profit_factor", "expectancy_eur",
        "equity_eur", "total_pnl_eur", "total_return_pct",
        "closed_pnl_eur", "open_pnl_eur", "open_positions",
        "max_drawdown_pct", "average_mfe_net_eur",
        "average_mae_net_eur", "average_profit_retained_pct",
        "profit_retention_sample", "comparison_score",
    ]
    with CSV_PATH.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=fields,
            extrasaction="ignore",
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    rows = build_rows()
    write_outputs(rows)
    send_telegram(telegram_report(rows))
    print(json.dumps({
        "status": "PASS",
        "accounts": len(rows),
        "active_accounts": sum(row["closed_trades"] > 0 for row in rows),
        "evaluable_accounts": sum(row["closed_trades"] >= 30 for row in rows),
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
