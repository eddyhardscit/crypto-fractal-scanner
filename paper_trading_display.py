# -*- coding: utf-8 -*-
'''Human-readable labels and exposure/risk summaries for paper trading.'''

from __future__ import annotations

from collections.abc import Iterable
from typing import Any


PORTFOLIO_LABELS = {
    "MAIN": "Principale 4H",
    "SHADOW_1H_BALANCED": "Bilanciata 1H",
    "SHADOW_1H_FAST": "Rapida 1H",
    "SHADOW_4H_WIDE": "Ampia 4H",
    "SHADOW_RELATIVE_STRENGTH": "Forza relativa 1H",
}

PORTFOLIO_DESCRIPTIONS = {
    "MAIN": (
        "Riferimento principale: confluenza di trend su 4 ore, "
        "soglia più selettiva."
    ),
    "SHADOW_1H_BALANCED": (
        "Test bilanciato a 1 ora basato sulla confluenza di trend."
    ),
    "SHADOW_1H_FAST": (
        "Test rapido a 1 ora che cerca momentum e breakout."
    ),
    "SHADOW_4H_WIDE": (
        "Test a 4 ore con stop più ampio, leva inferiore e durata maggiore."
    ),
    "SHADOW_RELATIVE_STRENGTH": (
        "Test a 1 ora che seleziona forza o debolezza rispetto a Bitcoin."
    ),
}

STRATEGY_LABELS = {
    "confluence_trend": "Confluenza trend",
    "momentum_breakout": "Momentum / breakout",
    "relative_strength": "Forza relativa vs BTC",
}


def _number(value: Any) -> float:
    try:
        return float(value)
    except Exception:
        return 0.0


def portfolio_label(name: Any) -> str:
    raw = str(name or "")
    return PORTFOLIO_LABELS.get(
        raw,
        raw.replace("SHADOW_", "").replace("_", " ").title(),
    )


def portfolio_description(name: Any) -> str:
    raw = str(name or "")
    return PORTFOLIO_DESCRIPTIONS.get(
        raw,
        "Portafoglio sperimentale separato.",
    )


def portfolio_type(name: Any, is_main: bool = False) -> str:
    return "PRINCIPALE" if is_main or str(name) == "MAIN" else "TEST"


def strategy_label(strategy: Any) -> str:
    raw = str(strategy or "")
    return STRATEGY_LABELS.get(
        raw,
        raw.replace("_", " ").title(),
    )


def current_stop_risk_eur(position: dict[str, Any]) -> float:
    # Loss from entry to the current stop; zero once profit is protected.
    entry = _number(position.get("entry_price"))
    stop = _number(position.get("stop_price"))
    quantity = abs(_number(position.get("quantity")))
    rate = _number(position.get("eur_usdt_rate")) or 1.0
    side = str(position.get("side", "")).upper()

    if entry <= 0 or stop <= 0 or quantity <= 0:
        return max(0.0, _number(position.get("initial_risk_eur")))

    if side == "LONG":
        price_risk = max(0.0, entry - stop)
    elif side == "SHORT":
        price_risk = max(0.0, stop - entry)
    else:
        return max(0.0, _number(position.get("initial_risk_eur")))

    return price_risk * quantity / rate


def aggregate_positions(
    positions: Iterable[dict[str, Any]],
) -> dict[str, float | int]:
    rows = list(positions)
    return {
        "count": len(rows),
        "margin_eur": sum(
            _number(row.get("margin_eur"))
            for row in rows
        ),
        "notional_eur": sum(
            _number(row.get("notional_eur"))
            for row in rows
        ),
        "initial_risk_eur": sum(
            _number(row.get("initial_risk_eur"))
            for row in rows
        ),
        "current_stop_risk_eur": sum(
            current_stop_risk_eur(row)
            for row in rows
        ),
    }
