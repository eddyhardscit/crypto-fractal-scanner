# -*- coding: utf-8 -*-
'''Human-readable labels and exposure/risk summaries for paper trading.'''

from __future__ import annotations

import re
from collections.abc import Iterable
from typing import Any


PORTFOLIO_LABELS = {
    "MAIN": "Principale 4H",
    "SHADOW_1H_BALANCED": "Bilanciata 1H",
    "SHADOW_1H_FAST": "Rapida 1H",
    "SHADOW_4H_WIDE": "Ampia 4H",
    "SHADOW_RELATIVE_STRENGTH": "Forza relativa 1H",
    "SHADOW_RSI_LONG_15X_10": "Scalp RSI Long €10 · 15x",
    "SHADOW_RSI_LONG_15X_50": "Scalp RSI Long €50 · 15x",
    "SHADOW_RSI_LONG_5X": "Scalp RSI Long prudente 5x",
    "SHADOW_RSI_SHORT_15X_10": "Scalp RSI Short €10 · 15x",
    "SHADOW_RSI_SHORT_15X_50": "Scalp RSI Short €50 · 15x",
    "SHADOW_RSI_SHORT_5X": "Scalp RSI Short prudente 5x",
    "SHADOW_DONCHIAN_1H": "Benchmark Donchian breakout 1H",
    "SHADOW_BOLLINGER_MR_1H": "Benchmark Bollinger mean reversion 1H",
    "SHADOW_EMA_TREND_1H": "Benchmark trend following EMA 1H",
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
    "SHADOW_RSI_LONG_15X_10": (
        "Scalp long 15m dopo capitolazione RSI confermata; margine fisso €10 e leva paper 15x."
    ),
    "SHADOW_RSI_LONG_15X_50": (
        "Scalp long 15m sullo stesso segnale; margine fisso €50 e leva paper 15x."
    ),
    "SHADOW_RSI_LONG_5X": (
        "Versione prudente long dello scalp RSI 15m, leva 5x e rischio ridotto."
    ),
    "SHADOW_RSI_SHORT_15X_10": (
        "Scalp short 15m dopo euforia RSI confermata; margine fisso €10 e leva paper 15x."
    ),
    "SHADOW_RSI_SHORT_15X_50": (
        "Scalp short 15m sullo stesso segnale; margine fisso €50 e leva paper 15x."
    ),
    "SHADOW_RSI_SHORT_5X": (
        "Versione prudente short dello scalp RSI 15m, leva 5x e rischio ridotto."
    ),
    "SHADOW_DONCHIAN_1H": (
        "Benchmark puro: breakout o breakdown dei massimi/minimi delle 20 barre precedenti, con filtro ADX."
    ),
    "SHADOW_BOLLINGER_MR_1H": (
        "Benchmark puro: ritorno verso la media dopo uscita dalle Bollinger e conferma RSI estrema."
    ),
    "SHADOW_EMA_TREND_1H": (
        "Benchmark puro: trend following con prezzo, EMA20, EMA50 e filtro ADX."
    ),
}

STRATEGY_LABELS = {
    "confluence_trend": "Confluenza trend",
    "momentum_breakout": "Momentum / breakout",
    "relative_strength": "Forza relativa vs BTC",
    "rsi_extreme_reversal": "Inversione RSI estrema 15m",
    "donchian_breakout": "Donchian breakout 20 barre",
    "bollinger_mean_reversion": "Bollinger mean reversion",
    "ema_trend_following": "Trend following EMA",
}


def _number(value: Any) -> float:
    try:
        return float(value)
    except Exception:
        return 0.0


def portfolio_label(name: Any) -> str:
    raw = str(name or "")

    match = re.fullmatch(
        r"SHADOW_RSI_(LONG|SHORT)_(15X_10|15X_50|5X)_RSI(15|20|25|75|80|85)",
        raw,
    )
    if match:
        side, profile, trigger = match.groups()

        if profile == "15X_10":
            profile_label = "€10 · 15x"
        elif profile == "15X_50":
            profile_label = "€50 · 15x"
        else:
            profile_label = "prudente · 5x"

        return (
            f"Scalp RSI {side.title()} {trigger} · "
            f"{profile_label}"
        )

    return PORTFOLIO_LABELS.get(
        raw,
        raw.replace("SHADOW_", "").replace("_", " ").title(),
    )


def portfolio_description(name: Any) -> str:
    raw = str(name or "")

    match = re.fullmatch(
        r"SHADOW_RSI_(LONG|SHORT)_(15X_10|15X_50|5X)_RSI(15|20|25|75|80|85)",
        raw,
    )
    if match:
        side, profile, trigger = match.groups()

        if side == "LONG":
            recovery = {
                "15": "20",
                "20": "25",
                "25": "30",
            }[trigger]
            setup = (
                f"Scalp long 15m: RSI scende fino a {trigger} "
                f"e conferma il recupero verso {recovery}."
            )
        else:
            recovery = {
                "85": "80",
                "80": "75",
                "75": "70",
            }[trigger]
            setup = (
                f"Scalp short 15m: RSI sale fino a {trigger} "
                f"e conferma il rientro verso {recovery}."
            )

        if profile == "15X_10":
            risk_text = "Margine fisso €10, leva paper 15x."
        elif profile == "15X_50":
            risk_text = "Margine fisso €50, leva paper 15x."
        else:
            risk_text = "Versione prudente, leva 5x e rischio ridotto."

        return f"{setup} {risk_text}"

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
