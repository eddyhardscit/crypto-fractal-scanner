# -*- coding: utf-8 -*-
"""Shadow capital allocator for the paper-trading strategy laboratory.

This module never changes the 30 source portfolios and never sends orders.
It converts the comparative ranking into a conservative monthly allocation
proposal only after enough strategies have statistically evaluable samples.
"""

from __future__ import annotations

import csv
import json
import math
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import requests

REPORTS_DIR = Path("reports")
INPUT_PATH = REPORTS_DIR / "paper_trading_comparative_latest.json"
REPORT_PATH = REPORTS_DIR / "paper_trading_capital_allocator_report.md"
JSON_PATH = REPORTS_DIR / "paper_trading_capital_allocator_latest.json"
CSV_PATH = REPORTS_DIR / "paper_trading_capital_allocator_weights.csv"
HISTORY_PATH = REPORTS_DIR / "paper_trading_capital_allocator_history.csv"
STATE_PATH = REPORTS_DIR / "paper_trading_capital_allocator_state.json"

INITIAL_CAPITAL_EUR = 10_000.0
MIN_EVALUABLE_STRATEGIES = 3
MIN_CLOSED_TRADES = 30
MAX_SELECTED = 5
CASH_RESERVE_PCT = 20.0
MAX_WEIGHT_PCT = 30.0
MAX_DRAWDOWN_PCT = 15.0
MIN_PROFIT_FACTOR = 1.10


def now_utc() -> datetime:
    return datetime.now(timezone.utc)


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


def load_input() -> dict[str, Any]:
    if not INPUT_PATH.exists():
        raise FileNotFoundError(
            "Comparative report missing. Run paper_trading_comparative_report.py first."
        )
    payload = json.loads(INPUT_PATH.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError("Invalid comparative report payload.")
    return payload


def load_state() -> dict[str, Any]:
    if not STATE_PATH.exists():
        return {
            "schema_version": 1,
            "created_utc": now_utc().isoformat(timespec="seconds"),
            "initial_capital_eur": INITIAL_CAPITAL_EUR,
            "last_month": "",
            "last_mode": "OBSERVATION",
            "last_weights": {},
        }
    try:
        state = json.loads(STATE_PATH.read_text(encoding="utf-8"))
        return state if isinstance(state, dict) else {}
    except Exception:
        return {}


def eligible(row: dict[str, Any]) -> bool:
    return (
        int(safe_float(row.get("closed_trades"))) >= MIN_CLOSED_TRADES
        and safe_float(row.get("total_return_pct")) > 0.0
        and safe_float(row.get("profit_factor")) >= MIN_PROFIT_FACTOR
        and safe_float(row.get("expectancy_eur")) > 0.0
        and abs(safe_float(row.get("max_drawdown_pct"))) <= MAX_DRAWDOWN_PCT
        and safe_float(row.get("comparison_score")) > 0.0
    )


def quality_score(row: dict[str, Any]) -> float:
    closed = int(safe_float(row.get("closed_trades")))
    sample_factor = min(1.0, math.sqrt(closed / 100.0))
    return max(
        0.0,
        safe_float(row.get("comparison_score")) * sample_factor,
    )


def capped_weights(
    rows: list[dict[str, Any]],
    investable_pct: float,
) -> dict[str, float]:
    if not rows or investable_pct <= 0:
        return {}

    raw = {
        str(row.get("portfolio")): quality_score(row)
        for row in rows
    }
    total = sum(raw.values())
    if total <= 0:
        equal = investable_pct / len(rows)
        return {
            name: min(MAX_WEIGHT_PCT, equal)
            for name in raw
        }

    weights = {
        name: value / total * investable_pct
        for name, value in raw.items()
    }

    # Iterative cap and redistribution.
    for _ in range(20):
        over = {
            name: value
            for name, value in weights.items()
            if value > MAX_WEIGHT_PCT + 1e-9
        }
        if not over:
            break

        excess = sum(
            value - MAX_WEIGHT_PCT
            for value in over.values()
        )
        for name in over:
            weights[name] = MAX_WEIGHT_PCT

        under = [
            name
            for name, value in weights.items()
            if value < MAX_WEIGHT_PCT - 1e-9
        ]
        if not under or excess <= 1e-9:
            break

        denominator = sum(raw[name] for name in under)
        if denominator <= 0:
            increment = excess / len(under)
            for name in under:
                weights[name] += increment
        else:
            for name in under:
                weights[name] += (
                    excess * raw[name] / denominator
                )

    assigned = sum(weights.values())
    if assigned > investable_pct and assigned > 0:
        scale = investable_pct / assigned
        weights = {
            name: value * scale
            for name, value in weights.items()
        }
    return weights


def build_allocation(payload: dict[str, Any]) -> dict[str, Any]:
    rows = list(payload.get("rows", []))
    evaluable = [
        row
        for row in rows
        if int(safe_float(row.get("closed_trades"))) >= MIN_CLOSED_TRADES
    ]
    qualified = [
        row
        for row in evaluable
        if eligible(row)
    ]
    qualified.sort(
        key=lambda row: (
            quality_score(row),
            safe_float(row.get("total_return_pct")),
        ),
        reverse=True,
    )
    selected = qualified[:MAX_SELECTED]

    enabled = (
        len(evaluable) >= MIN_EVALUABLE_STRATEGIES
        and len(selected) >= MIN_EVALUABLE_STRATEGIES
    )
    mode = "SHADOW_ROTATION" if enabled else "OBSERVATION"
    cash_pct = CASH_RESERVE_PCT if enabled else 100.0
    investable_pct = 100.0 - cash_pct
    weights = capped_weights(selected, investable_pct) if enabled else {}

    allocations = []
    by_name = {
        str(row.get("portfolio")): row
        for row in rows
    }
    for portfolio, weight in sorted(
        weights.items(),
        key=lambda item: item[1],
        reverse=True,
    ):
        row = by_name[portfolio]
        allocations.append({
            "portfolio": portfolio,
            "label": str(row.get("label", portfolio)),
            "weight_pct": weight,
            "capital_eur": INITIAL_CAPITAL_EUR * weight / 100.0,
            "closed_trades": int(safe_float(row.get("closed_trades"))),
            "profit_factor": safe_float(row.get("profit_factor")),
            "expectancy_eur": safe_float(row.get("expectancy_eur")),
            "total_return_pct": safe_float(row.get("total_return_pct")),
            "max_drawdown_pct": safe_float(row.get("max_drawdown_pct")),
            "comparison_score": safe_float(row.get("comparison_score")),
            "quality_score": quality_score(row),
        })

    reasons = []
    if len(evaluable) < MIN_EVALUABLE_STRATEGIES:
        reasons.append(
            f"Strategie valutabili: {len(evaluable)}/{MIN_EVALUABLE_STRATEGIES} richieste."
        )
    if len(selected) < MIN_EVALUABLE_STRATEGIES:
        reasons.append(
            f"Strategie che superano tutti i filtri: {len(selected)}/{MIN_EVALUABLE_STRATEGIES} richieste."
        )
    if enabled:
        reasons.append(
            "Rotazione esclusivamente virtuale: nessun conto sorgente viene modificato."
        )

    return {
        "schema_version": 1,
        "generated_utc": now_utc().isoformat(timespec="seconds"),
        "source_generated_utc": payload.get("generated_utc", ""),
        "mode": mode,
        "paper_only": True,
        "orders_enabled": False,
        "source_portfolios_modified": False,
        "initial_capital_eur": INITIAL_CAPITAL_EUR,
        "evaluable_count": len(evaluable),
        "qualified_count": len(qualified),
        "selected_count": len(allocations),
        "cash_weight_pct": cash_pct,
        "cash_eur": INITIAL_CAPITAL_EUR * cash_pct / 100.0,
        "allocations": allocations,
        "rules": {
            "min_evaluable_strategies": MIN_EVALUABLE_STRATEGIES,
            "min_closed_trades": MIN_CLOSED_TRADES,
            "max_selected": MAX_SELECTED,
            "cash_reserve_pct": CASH_RESERVE_PCT,
            "max_weight_pct": MAX_WEIGHT_PCT,
            "max_drawdown_pct": MAX_DRAWDOWN_PCT,
            "min_profit_factor": MIN_PROFIT_FACTOR,
            "positive_expectancy_required": True,
            "positive_return_required": True,
            "rebalance_frequency": "MONTHLY_RECOMMENDATION",
        },
        "reasons": reasons,
    }


def write_outputs(result: dict[str, Any]) -> None:
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    JSON_PATH.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    fields = [
        "portfolio", "label", "weight_pct", "capital_eur",
        "closed_trades", "profit_factor", "expectancy_eur",
        "total_return_pct", "max_drawdown_pct",
        "comparison_score", "quality_score",
    ]
    with CSV_PATH.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=fields,
            extrasaction="ignore",
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(result["allocations"])

    lines = [
        "# Allocatore virtuale del capitale",
        "",
        f"Generato: {result['generated_utc']}",
        "",
        f"**Modalità:** {result['mode']}",
        "",
        "> Simulazione separata. Non modifica i 30 conti, non invia ordini "
        "e non autorizza il trading reale.",
        "",
        "## Stato",
        "",
        f"- Strategie valutabili: **{result['evaluable_count']}**",
        f"- Strategie qualificate: **{result['qualified_count']}**",
        f"- Strategie selezionate: **{result['selected_count']}**",
        f"- Liquidità: **{fmt_pct(result['cash_weight_pct'])}** "
        f"({fmt_eur(result['cash_eur'])})",
        "",
    ]

    if result["allocations"]:
        lines.extend([
            "## Allocazione virtuale proposta",
            "",
            "| Strategia | Peso | Capitale | Trade | PF | Expectancy | Rendimento | DD max |",
            "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
        ])
        for row in result["allocations"]:
            lines.append(
                f"| {row['label']} | {fmt_pct(row['weight_pct'])} | "
                f"{fmt_eur(row['capital_eur'])} | {row['closed_trades']} | "
                f"{row['profit_factor']:.2f} | {fmt_eur(row['expectancy_eur'], signed=True)} | "
                f"{fmt_pct(row['total_return_pct'], signed=True)} | "
                f"{fmt_pct(row['max_drawdown_pct'])} |"
            )
        lines.append("")
    else:
        lines.extend([
            "## Allocazione",
            "",
            "**100% liquidità virtuale.** Il campione è ancora insufficiente.",
            "",
        ])

    lines.extend([
        "## Motivi",
        "",
        *[f"- {reason}" for reason in result["reasons"]],
        "",
        "## Regole di sicurezza",
        "",
        "- Almeno 3 strategie valutabili e qualificate.",
        "- Almeno 30 trade chiusi per strategia.",
        "- Profit factor ≥1,10.",
        "- Expectancy e rendimento positivi.",
        "- Drawdown massimo ≤15%.",
        "- Massimo 30% su una singola strategia.",
        "- Almeno 20% in liquidità quando la rotazione virtuale è attiva.",
        "",
    ])
    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")

    month = now_utc().strftime("%Y-%m")
    exists = HISTORY_PATH.exists() and HISTORY_PATH.stat().st_size > 0
    with HISTORY_PATH.open("a", encoding="utf-8", newline="") as handle:
        fields = [
            "generated_utc", "month", "mode", "evaluable_count",
            "qualified_count", "selected_count", "cash_weight_pct",
            "allocation_json",
        ]
        writer = csv.DictWriter(
            handle,
            fieldnames=fields,
            lineterminator="\n",
        )
        if not exists:
            writer.writeheader()
        writer.writerow({
            "generated_utc": result["generated_utc"],
            "month": month,
            "mode": result["mode"],
            "evaluable_count": result["evaluable_count"],
            "qualified_count": result["qualified_count"],
            "selected_count": result["selected_count"],
            "cash_weight_pct": result["cash_weight_pct"],
            "allocation_json": json.dumps(
                result["allocations"],
                ensure_ascii=False,
                separators=(",", ":"),
            ),
        })

    state = load_state()
    state.update({
        "schema_version": 1,
        "updated_utc": result["generated_utc"],
        "last_month": month,
        "last_mode": result["mode"],
        "last_weights": {
            row["portfolio"]: row["weight_pct"]
            for row in result["allocations"]
        },
    })
    STATE_PATH.write_text(
        json.dumps(state, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def telegram_text(result: dict[str, Any]) -> str:
    lines = [
        "🧭 <b>ALLOCATORE VIRTUALE STRATEGIE</b>",
        "",
        f"Modalità: <b>{result['mode']}</b>",
        f"Valutabili: <b>{result['evaluable_count']}</b> · "
        f"qualificate: <b>{result['qualified_count']}</b>",
        f"Liquidità virtuale: <b>{fmt_pct(result['cash_weight_pct'])}</b> "
        f"({fmt_eur(result['cash_eur'])})",
        "",
    ]
    if result["allocations"]:
        lines.append("<b>Pesi proposti</b>")
        for row in result["allocations"]:
            lines.append(
                f"• {row['label']}: <b>{fmt_pct(row['weight_pct'])}</b> "
                f"({fmt_eur(row['capital_eur'])})"
            )
    else:
        lines.extend([
            "<b>Nessuna rotazione.</b>",
            "Il capitale resta 100% cash finché il campione non è sufficiente.",
        ])
    lines.extend([
        "",
        "🧪 Solo simulazione: nessun ordine e nessuna modifica ai 30 conti.",
    ])
    return "\n".join(lines)


def send_telegram(text: str) -> None:
    token = os.getenv("TELEGRAM_BOT_TOKEN", "").strip()
    chat_id = os.getenv("TELEGRAM_CHAT_ID", "").strip()
    if not token or not chat_id:
        print("Telegram secrets missing; allocator report generated only.")
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


def main() -> None:
    payload = load_input()
    result = build_allocation(payload)
    write_outputs(result)
    send_telegram(telegram_text(result))
    print(json.dumps({
        "status": "PASS",
        "mode": result["mode"],
        "evaluable": result["evaluable_count"],
        "qualified": result["qualified_count"],
        "selected": result["selected_count"],
        "cash_pct": result["cash_weight_pct"],
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
