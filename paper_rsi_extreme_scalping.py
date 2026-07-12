
# -*- coding: utf-8 -*-
"""RSI extreme-reversal setups for 15-minute paper scalping."""

from __future__ import annotations

import math
from typing import Any

import pandas as pd


def _safe_num(value: Any, default: float = 0.0) -> float:
    try:
        number = float(value)
    except Exception:
        return default
    return number if math.isfinite(number) else default


def rsi(series: pd.Series, period: int = 14) -> pd.Series:
    delta = series.diff()
    gain = delta.clip(lower=0).ewm(
        alpha=1 / period,
        adjust=False,
        min_periods=period,
    ).mean()
    loss = (-delta.clip(upper=0)).ewm(
        alpha=1 / period,
        adjust=False,
        min_periods=period,
    ).mean()
    rs = gain / loss.replace(0, float("nan"))
    result = 100 - 100 / (1 + rs)
    return pd.to_numeric(result, errors="coerce").fillna(50.0)


def atr(frame: pd.DataFrame, period: int = 14) -> pd.Series:
    previous_close = frame["close"].shift(1)
    true_range = pd.concat(
        [
            frame["high"] - frame["low"],
            (frame["high"] - previous_close).abs(),
            (frame["low"] - previous_close).abs(),
        ],
        axis=1,
    ).max(axis=1)
    return true_range.ewm(
        alpha=1 / period,
        adjust=False,
        min_periods=period,
    ).mean()


def extreme_reversal_setup(
    frame: pd.DataFrame,
    side: str,
    settings: dict[str, Any] | None = None,
) -> dict[str, Any]:
    cfg = settings or {}
    direction = str(side or "").upper()
    if direction not in {"LONG", "SHORT"}:
        raise ValueError(f"Lato scalp non valido: {side!r}")

    if frame is None or len(frame) < 40:
        return {
            "accepted": False,
            "side": direction,
            "score": 0.0,
            "missing": ["almeno 40 candele"],
            "missing_text": "almeno 40 candele",
            "reasons": ["Dati insufficienti per lo scalp RSI."],
            "candle_time": "n/a",
            "state": "NO_DATA",
        }

    data = frame.copy().sort_index()
    for column in ("open", "high", "low", "close"):
        data[column] = pd.to_numeric(
            data[column],
            errors="coerce",
        )
    if "volume" in data.columns:
        data["volume"] = pd.to_numeric(
            data["volume"],
            errors="coerce",
        ).fillna(0.0)
    else:
        data["volume"] = pd.Series(
            0.0,
            index=data.index,
        )
    data = data.dropna(
        subset=["open", "high", "low", "close"]
    )
    if len(data) < 40 or float(data["close"].iloc[-1]) <= 0:
        return {
            "accepted": False,
            "side": direction,
            "score": 0.0,
            "missing": ["prezzi validi"],
            "missing_text": "prezzi validi",
            "reasons": ["Prezzi non validi per lo scalp RSI."],
            "candle_time": "n/a",
            "state": "NO_DATA",
        }

    close = data["close"]
    opened = data["open"]
    high = data["high"]
    low = data["low"]
    volume = data["volume"]
    rsi14 = rsi(close, 14)
    atr14 = atr(data, 14)

    candidate_index = -2
    confirmation_index = -1
    candidate_open = float(opened.iloc[candidate_index])
    candidate_high = float(high.iloc[candidate_index])
    candidate_low = float(low.iloc[candidate_index])
    candidate_close = float(close.iloc[candidate_index])
    confirmation_close = float(close.iloc[confirmation_index])
    candidate_rsi = _safe_num(
        rsi14.iloc[candidate_index],
        50.0,
    )
    confirmation_rsi = _safe_num(
        rsi14.iloc[confirmation_index],
        50.0,
    )
    atr_value = _safe_num(
        atr14.iloc[candidate_index],
        0.0,
    )
    candle_time = pd.Timestamp(
        data.index[confirmation_index]
    ).isoformat()
    if atr_value <= 0 or candidate_close <= 0:
        return {
            "accepted": False,
            "side": direction,
            "score": 0.0,
            "missing": ["ATR valido"],
            "missing_text": "ATR valido",
            "reasons": ["ATR non disponibile per lo scalp RSI."],
            "candle_time": candle_time,
            "state": "NO_ATR",
        }

    candidate_range = max(
        1e-12,
        candidate_high - candidate_low,
    )
    range_atr = candidate_range / atr_value
    history = volume.iloc[
        max(0, len(volume) - 32):-2
    ].tail(20)
    volume_median = (
        float(history.median())
        if not history.empty
        else 0.0
    )
    volume_ratio = (
        float(volume.iloc[candidate_index] / volume_median)
        if volume_median > 0
        else 1.0
    )

    lower_wick = max(
        0.0,
        min(candidate_open, candidate_close)
        - candidate_low,
    )
    upper_wick = max(
        0.0,
        candidate_high
        - max(candidate_open, candidate_close),
    )
    lower_wick_ratio = lower_wick / candidate_range
    upper_wick_ratio = upper_wick / candidate_range

    prior_close = float(close.iloc[candidate_index - 1])
    candidate_return_pct = (
        (candidate_close / prior_close - 1.0) * 100.0
        if prior_close > 0
        else 0.0
    )
    swing_start = float(close.iloc[max(0, len(close) - 6)])
    atr_pct = atr_value / candidate_close * 100.0
    multi_bar_move_pct = (
        (candidate_close / swing_start - 1.0) * 100.0
        if swing_start > 0
        else 0.0
    )
    multi_bar_shock_atr = (
        abs(multi_bar_move_pct) / atr_pct
        if atr_pct > 0
        else 0.0
    )
    shock_atr = max(range_atr, multi_bar_shock_atr)

    min_shock_atr = float(
        cfg.get("min_shock_atr", 1.5)
    )
    min_volume_ratio = float(
        cfg.get("min_volume_ratio", 2.0)
    )
    min_wick_ratio = float(
        cfg.get("min_wick_ratio", 0.12)
    )
    min_reversal_atr = float(
        cfg.get("min_reversal_atr", 0.20)
    )
    stop_buffer_atr = float(
        cfg.get("stop_buffer_atr", 0.15)
    )
    minimum_stop_pct = float(
        cfg.get("minimum_stop_pct", 0.004)
    )
    maximum_stop_pct = float(
        cfg.get("maximum_stop_pct", 0.05)
    )

    if direction == "LONG":
        trigger = float(cfg.get("rsi_trigger", 15.0))
        recovery = float(cfg.get("rsi_recovery", 20.0))
        rebound_points = float(
            cfg.get("rsi_rebound_points", 3.0)
        )
        extreme_ok = candidate_rsi <= trigger
        shock_ok = (
            candidate_return_pct < 0
            and shock_atr >= min_shock_atr
        )
        recovery_ok = (
            confirmation_rsi >= recovery
            and confirmation_rsi - candidate_rsi
            >= rebound_points
            and confirmation_close > candidate_close
        )
        reversal_atr = (
            confirmation_close - candidate_close
        ) / atr_value
        wick_ratio = lower_wick_ratio
        rejection_ok = (
            wick_ratio >= min_wick_ratio
            or reversal_atr >= min_reversal_atr
        )
        raw_stop_price = max(
            1e-12,
            candidate_low - stop_buffer_atr * atr_value,
        )
        raw_stop_pct = max(
            0.0,
            (confirmation_close - raw_stop_price)
            / confirmation_close,
        )
        state = "RSI_CAPITULATION_LONG"
        extreme_text = f"RSI ≤{trigger:.1f}"
        recovery_text = (
            f"RSI ≥{recovery:.1f} in recupero"
        )
        wick_text = "wick inferiore o rimbalzo"
    else:
        trigger = float(cfg.get("rsi_trigger", 85.0))
        recovery = float(cfg.get("rsi_recovery", 80.0))
        rebound_points = float(
            cfg.get("rsi_rebound_points", 3.0)
        )
        extreme_ok = candidate_rsi >= trigger
        shock_ok = (
            candidate_return_pct > 0
            and shock_atr >= min_shock_atr
        )
        recovery_ok = (
            confirmation_rsi <= recovery
            and candidate_rsi - confirmation_rsi
            >= rebound_points
            and confirmation_close < candidate_close
        )
        reversal_atr = (
            candidate_close - confirmation_close
        ) / atr_value
        wick_ratio = upper_wick_ratio
        rejection_ok = (
            wick_ratio >= min_wick_ratio
            or reversal_atr >= min_reversal_atr
        )
        raw_stop_price = (
            candidate_high + stop_buffer_atr * atr_value
        )
        raw_stop_pct = max(
            0.0,
            (raw_stop_price - confirmation_close)
            / confirmation_close,
        )
        state = "RSI_EUPHORIA_SHORT"
        extreme_text = f"RSI ≥{trigger:.1f}"
        recovery_text = (
            f"RSI ≤{recovery:.1f} in rientro"
        )
        wick_text = "wick superiore o inversione"

    volume_ok = volume_ratio >= min_volume_ratio
    stop_ok = (
        raw_stop_pct > 0
        and raw_stop_pct <= maximum_stop_pct
    )
    stop_pct = max(
        minimum_stop_pct,
        min(maximum_stop_pct, raw_stop_pct),
    )

    score = 0.0
    if extreme_ok:
        score += 3.0
    elif (
        direction == "LONG"
        and candidate_rsi <= trigger + 5.0
    ) or (
        direction == "SHORT"
        and candidate_rsi >= trigger - 5.0
    ):
        score += 1.0

    score += (
        2.0
        if shock_ok
        else 1.0
        if shock_atr >= min_shock_atr * 0.75
        else 0.0
    )
    score += (
        2.0
        if volume_ok
        else 1.0
        if volume_ratio >= max(
            1.2,
            min_volume_ratio * 0.75,
        )
        else 0.0
    )
    score += (
        2.0
        if recovery_ok
        else 1.0
        if (
            confirmation_close > candidate_close
            if direction == "LONG"
            else confirmation_close < candidate_close
        )
        else 0.0
    )
    score += 1.0 if rejection_ok else 0.0

    missing: list[str] = []
    if not extreme_ok:
        missing.append(extreme_text)
    if not shock_ok:
        missing.append(
            f"shock direzionale ≥{min_shock_atr:.2f} ATR"
        )
    if not volume_ok:
        missing.append(
            f"volume ≥{min_volume_ratio:.2f}x"
        )
    if not recovery_ok:
        missing.append(recovery_text)
    if not rejection_ok:
        missing.append(wick_text)
    if not stop_ok:
        missing.append(
            f"stop tecnico ≤{maximum_stop_pct * 100:.1f}%"
        )

    accepted = all(
        (
            extreme_ok,
            shock_ok,
            volume_ok,
            recovery_ok,
            rejection_ok,
            stop_ok,
        )
    )
    reasons = [
        (
            f"{state}: RSI {candidate_rsi:.1f} → "
            f"{confirmation_rsi:.1f}"
        ),
        (
            f"shock {shock_atr:.2f} ATR; "
            f"volume x{volume_ratio:.2f}"
        ),
        (
            f"wick {wick_ratio * 100:.1f}%; "
            f"inversione {reversal_atr:.2f} ATR"
        ),
        f"stop tecnico {stop_pct * 100:.2f}%",
    ]
    return {
        "accepted": accepted,
        "side": direction,
        "score": round(score, 4),
        "missing": missing,
        "missing_text": (
            ", ".join(missing)
            if missing
            else "nessun filtro mancante"
        ),
        "reasons": reasons,
        "candle_time": candle_time,
        "candidate_time": pd.Timestamp(
            data.index[candidate_index]
        ).isoformat(),
        "candidate_rsi": candidate_rsi,
        "confirmation_rsi": confirmation_rsi,
        "candidate_low": candidate_low,
        "candidate_high": candidate_high,
        "candidate_close": candidate_close,
        "confirmation_close": confirmation_close,
        "shock_atr": shock_atr,
        "volume_ratio": volume_ratio,
        "wick_ratio": wick_ratio,
        "reversal_atr": reversal_atr,
        "atr_pct": max(0.0, atr_pct),
        "stop_pct": stop_pct,
        "raw_stop_pct": raw_stop_pct,
        "state": state,
    }
