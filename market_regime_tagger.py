# -*- coding: utf-8 -*-
"""Observational crypto market-regime classifier for paper-trading research."""

from __future__ import annotations

import csv
import json
import math
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

from kucoin_public_data import bundle_frames

REPORTS_DIR = Path("reports")
LATEST_PATH = REPORTS_DIR / "market_regime_latest.json"
HISTORY_PATH = REPORTS_DIR / "market_regime_history.csv"

HISTORY_FIELDS = [
    "generated_utc",
    "regime",
    "regime_family",
    "confidence_pct",
    "volatility_state",
    "btc_timeframe_minutes",
    "btc_trend_score",
    "btc_adx",
    "btc_atr_pct",
    "btc_volatility_ratio",
    "btc_return_24h_pct",
    "breadth_above_ema20_pct",
    "breadth_above_ema50_pct",
    "breadth_above_ema200_pct",
    "breadth_breakout_up_pct",
    "breadth_breakout_down_pct",
    "alt_relative_median_pct",
    "alt_outperform_share_pct",
    "alt_underperform_share_pct",
    "cross_asset_dispersion_pct",
    "assets_used",
    "reason",
]


def _now_utc() -> datetime:
    return datetime.now(timezone.utc)


def _finite(value: Any, default: float = 0.0) -> float:
    try:
        number = float(value)
        return number if math.isfinite(number) else default
    except Exception:
        return default


def _ema(series: pd.Series, span: int) -> pd.Series:
    return series.ewm(
        span=span,
        adjust=False,
        min_periods=min(span, max(5, len(series) // 3)),
    ).mean()


def _atr(frame: pd.DataFrame, period: int = 14) -> pd.Series:
    previous = frame["close"].shift(1)
    true_range = pd.concat(
        [
            frame["high"] - frame["low"],
            (frame["high"] - previous).abs(),
            (frame["low"] - previous).abs(),
        ],
        axis=1,
    ).max(axis=1)
    return true_range.ewm(
        alpha=1 / period,
        adjust=False,
        min_periods=period,
    ).mean()


def _adx(frame: pd.DataFrame, period: int = 14) -> pd.Series:
    up_move = frame["high"].diff()
    down_move = -frame["low"].diff()
    plus_dm = pd.Series(
        np.where(
            (up_move > down_move) & (up_move > 0),
            up_move,
            0.0,
        ),
        index=frame.index,
    )
    minus_dm = pd.Series(
        np.where(
            (down_move > up_move) & (down_move > 0),
            down_move,
            0.0,
        ),
        index=frame.index,
    )
    atr_value = _atr(frame, period).replace(0, np.nan)
    plus_di = (
        100
        * plus_dm.ewm(
            alpha=1 / period,
            adjust=False,
            min_periods=period,
        ).mean()
        / atr_value
    )
    minus_di = (
        100
        * minus_dm.ewm(
            alpha=1 / period,
            adjust=False,
            min_periods=period,
        ).mean()
        / atr_value
    )
    dx = (
        100
        * (plus_di - minus_di).abs()
        / (plus_di + minus_di).replace(0, np.nan)
    )
    return dx.ewm(
        alpha=1 / period,
        adjust=False,
        min_periods=period,
    ).mean().fillna(0.0)


def _return_pct(series: pd.Series, bars: int) -> float:
    clean = pd.to_numeric(series, errors="coerce").dropna()
    if len(clean) <= bars:
        return 0.0
    start = float(clean.iloc[-bars - 1])
    end = float(clean.iloc[-1])
    return 0.0 if start <= 0 else (end / start - 1.0) * 100.0


def _frame_features(
    frame: pd.DataFrame,
    return_bars: int,
) -> dict[str, float | bool]:
    if frame is None or len(frame) < 60:
        return {}
    data = frame.copy().sort_index()
    for column in ("open", "high", "low", "close"):
        data[column] = pd.to_numeric(
            data[column],
            errors="coerce",
        )
    data = data.dropna(
        subset=["open", "high", "low", "close"]
    )
    if len(data) < 60:
        return {}

    close = data["close"]
    price = float(close.iloc[-1])
    if price <= 0:
        return {}

    ema20 = _ema(close, 20)
    ema50 = _ema(close, 50)
    ema200 = _ema(close, 200)
    atr_series = _atr(data, 14)
    atr_pct_series = (
        atr_series / close.replace(0, np.nan) * 100.0
    )
    current_atr_pct = _finite(
        atr_pct_series.iloc[-1],
        0.0,
    )
    baseline = _finite(
        atr_pct_series.tail(60).median(),
        current_atr_pct,
    )
    volatility_ratio = (
        current_atr_pct / baseline
        if baseline > 0
        else 1.0
    )

    previous_high = _finite(
        data["high"]
        .shift(1)
        .rolling(20, min_periods=10)
        .max()
        .iloc[-1],
        price,
    )
    previous_low = _finite(
        data["low"]
        .shift(1)
        .rolling(20, min_periods=10)
        .min()
        .iloc[-1],
        price,
    )

    return {
        "price": price,
        "ema20": _finite(ema20.iloc[-1], price),
        "ema50": _finite(ema50.iloc[-1], price),
        "ema200": _finite(ema200.iloc[-1], price),
        "adx": _finite(_adx(data, 14).iloc[-1], 0.0),
        "atr_pct": max(0.0, current_atr_pct),
        "volatility_ratio": max(
            0.0,
            volatility_ratio,
        ),
        "return_pct": _return_pct(
            close,
            min(
                return_bars,
                max(1, len(close) - 2),
            ),
        ),
        "breakout_up": price > previous_high,
        "breakout_down": price < previous_low,
    }


def _choose_btc_frame(
    frames: dict[str, dict[int, pd.DataFrame]],
) -> tuple[pd.DataFrame | None, int]:
    btc = frames.get("BTC", {})
    for timeframe in (240, 60, 15):
        frame = btc.get(timeframe)
        if frame is not None and len(frame) >= 60:
            return frame, timeframe
    return None, 0


def _pct(part: int, total: int) -> float:
    return part / total * 100.0 if total else 0.0


def _confidence(
    agreement: float,
    data_coverage: float,
) -> float:
    raw = 42.0 + 48.0 * max(
        0.0,
        min(1.0, agreement),
    )
    raw *= 0.75 + 0.25 * max(
        0.0,
        min(1.0, data_coverage),
    )
    return round(max(35.0, min(95.0, raw)), 1)


def classify_market_regime(
    bundle: dict[str, Any],
) -> dict[str, Any]:
    frames = bundle_frames(bundle)
    btc_frame, btc_timeframe = _choose_btc_frame(
        frames
    )
    generated = str(
        bundle.get(
            "generated_utc",
            _now_utc().isoformat(timespec="seconds"),
        )
    )

    if btc_frame is None:
        return {
            "generated_utc": generated,
            "regime": "UNKNOWN",
            "regime_family": "UNKNOWN",
            "confidence_pct": 0.0,
            "volatility_state": "UNKNOWN",
            "rotation_mode": "OBSERVATION_ONLY",
            "features": {
                "assets_used": 0,
            },
            "reason": (
                "Dati BTC insufficienti per classificare "
                "il regime."
            ),
        }

    btc_return_bars = (
        6 if btc_timeframe == 240
        else 24 if btc_timeframe == 60
        else 96
    )
    btc = _frame_features(
        btc_frame,
        btc_return_bars,
    )
    if not btc:
        return {
            "generated_utc": generated,
            "regime": "UNKNOWN",
            "regime_family": "UNKNOWN",
            "confidence_pct": 0.0,
            "volatility_state": "UNKNOWN",
            "rotation_mode": "OBSERVATION_ONLY",
            "features": {
                "assets_used": 0,
            },
            "reason": (
                "Indicatori BTC insufficienti per "
                "classificare il regime."
            ),
        }

    trend_score = 0.0
    trend_score += (
        1.0
        if btc["price"] > btc["ema20"]
        else -1.0
    )
    trend_score += (
        1.0
        if btc["ema20"] > btc["ema50"]
        else -1.0
    )
    trend_score += (
        1.0
        if btc["ema50"] > btc["ema200"]
        else -1.0
    )
    if btc["return_pct"] >= 1.0:
        trend_score += 1.0
    elif btc["return_pct"] <= -1.0:
        trend_score -= 1.0

    market_timeframe = (
        60
        if any(
            60 in asset_frames
            and len(asset_frames[60]) >= 60
            for asset_frames in frames.values()
        )
        else btc_timeframe
    )
    return_bars = (
        24
        if market_timeframe == 60
        else 6 if market_timeframe == 240 else 96
    )
    btc_market_features = _frame_features(
        frames.get("BTC", {}).get(
            market_timeframe,
            btc_frame,
        ),
        return_bars,
    )
    btc_market_return = _finite(
        btc_market_features.get(
            "return_pct",
            btc["return_pct"],
        ),
        btc["return_pct"],
    )

    asset_rows: list[dict[str, Any]] = []
    for asset, asset_frames in frames.items():
        frame = asset_frames.get(market_timeframe)
        features = _frame_features(
            frame,
            return_bars,
        )
        if not features:
            continue
        relative = (
            float(features["return_pct"])
            - btc_market_return
        )
        asset_rows.append(
            {
                "asset": asset,
                **features,
                "relative_pct": relative,
            }
        )

    total = len(asset_rows)
    above20 = sum(
        row["price"] > row["ema20"]
        for row in asset_rows
    )
    above50 = sum(
        row["price"] > row["ema50"]
        for row in asset_rows
    )
    above200 = sum(
        row["price"] > row["ema200"]
        for row in asset_rows
    )
    breakout_up = sum(
        bool(row["breakout_up"])
        for row in asset_rows
    )
    breakout_down = sum(
        bool(row["breakout_down"])
        for row in asset_rows
    )

    alt_rows = [
        row
        for row in asset_rows
        if row["asset"] != "BTC"
    ]
    relative_values = [
        float(row["relative_pct"])
        for row in alt_rows
    ]
    alt_relative_median = (
        float(np.median(relative_values))
        if relative_values
        else 0.0
    )
    dispersion = (
        float(np.std(relative_values))
        if len(relative_values) >= 2
        else 0.0
    )
    outperform_share = _pct(
        sum(value >= 1.0 for value in relative_values),
        len(relative_values),
    )
    underperform_share = _pct(
        sum(value <= -1.0 for value in relative_values),
        len(relative_values),
    )
    market_volatility_ratio = (
        float(
            np.median(
                [
                    float(row["volatility_ratio"])
                    for row in asset_rows
                ]
            )
        )
        if asset_rows
        else float(btc["volatility_ratio"])
    )

    breadth20 = _pct(above20, total)
    breadth50 = _pct(above50, total)
    breadth200 = _pct(above200, total)
    breakout_up_pct = _pct(
        breakout_up,
        total,
    )
    breakout_down_pct = _pct(
        breakout_down,
        total,
    )

    high_vol = (
        float(btc["volatility_ratio"]) >= 1.25
        or market_volatility_ratio >= 1.25
        or float(btc["atr_pct"]) >= 3.5
    )
    low_vol = (
        float(btc["volatility_ratio"]) <= 0.80
        and market_volatility_ratio <= 0.90
    )
    volatility_state = (
        "HIGH"
        if high_vol
        else "LOW" if low_vol else "NORMAL"
    )

    rotation_up_strength = min(
        1.0,
        max(0.0, alt_relative_median / 3.0)
        * 0.55
        + max(0.0, outperform_share / 60.0)
        * 0.45,
    )
    rotation_down_strength = min(
        1.0,
        max(0.0, -alt_relative_median / 3.0)
        * 0.55
        + max(0.0, underperform_share / 60.0)
        * 0.45,
    )

    rotation_up = (
        len(alt_rows) >= 4
        and alt_relative_median >= 1.25
        and outperform_share >= 45.0
        and dispersion >= 1.0
    )
    rotation_down = (
        len(alt_rows) >= 4
        and alt_relative_median <= -1.25
        and underperform_share >= 45.0
        and dispersion >= 1.0
    )

    up_confirmation = (
        max(0.0, trend_score) / 4.0 * 0.45
        + max(0.0, (breadth50 - 50.0) / 50.0)
        * 0.30
        + min(1.0, float(btc["adx"]) / 35.0)
        * 0.25
    )
    down_confirmation = (
        max(0.0, -trend_score) / 4.0 * 0.45
        + max(0.0, (50.0 - breadth50) / 50.0)
        * 0.30
        + min(1.0, float(btc["adx"]) / 35.0)
        * 0.25
    )

    if rotation_up:
        regime = "ALT_ROTATION_UP"
        family = "ALT_ROTATION"
        agreement = rotation_up_strength
        reason = (
            "Le altcoin stanno sovraperformando BTC: "
            f"mediana relativa {alt_relative_median:+.2f}%, "
            f"{outperform_share:.0f}% oltre +1%."
        )
    elif rotation_down:
        regime = "ALT_ROTATION_DOWN"
        family = "ALT_ROTATION"
        agreement = rotation_down_strength
        reason = (
            "Le altcoin stanno sottoperformando BTC: "
            f"mediana relativa {alt_relative_median:+.2f}%, "
            f"{underperform_share:.0f}% sotto -1%."
        )
    elif (
        trend_score >= 2.0
        and breadth50 >= 52.0
        and float(btc["adx"]) >= 18.0
    ):
        family = "TREND_UP"
        regime = (
            "TREND_UP_HIGH_VOL"
            if high_vol
            else "TREND_UP"
        )
        agreement = up_confirmation
        reason = (
            "Trend BTC rialzista confermato dalla breadth: "
            f"score {trend_score:+.1f}, "
            f"{breadth50:.0f}% sopra EMA50, "
            f"ADX {float(btc['adx']):.1f}."
        )
    elif (
        trend_score <= -2.0
        and breadth50 <= 48.0
        and float(btc["adx"]) >= 18.0
    ):
        family = "TREND_DOWN"
        regime = (
            "TREND_DOWN_HIGH_VOL"
            if high_vol
            else "TREND_DOWN"
        )
        agreement = down_confirmation
        reason = (
            "Trend BTC ribassista confermato dalla breadth: "
            f"score {trend_score:+.1f}, "
            f"{breadth50:.0f}% sopra EMA50, "
            f"ADX {float(btc['adx']):.1f}."
        )
    elif (
        abs(trend_score) <= 1.0
        or float(btc["adx"]) < 18.0
    ):
        family = "RANGE"
        regime = (
            "RANGE_HIGH_VOL"
            if high_vol
            else "RANGE_LOW_VOL"
            if low_vol
            else "RANGE"
        )
        agreement = (
            0.45
            + min(
                0.35,
                abs(50.0 - breadth50) / 50.0,
            )
            + (
                0.15
                if float(btc["adx"]) < 18.0
                else 0.0
            )
        )
        reason = (
            "Direzione poco definita: "
            f"score BTC {trend_score:+.1f}, "
            f"breadth EMA50 {breadth50:.0f}%, "
            f"ADX {float(btc['adx']):.1f}."
        )
    else:
        family = "TRANSITION"
        regime = "TRANSITION"
        agreement = 0.50 + min(
            0.25,
            abs(trend_score) / 8.0,
        )
        reason = (
            "Segnali contrastanti tra trend BTC, "
            "breadth e forza delle altcoin."
        )

    expected_assets = max(
        1,
        len(bundle.get("assets", {})),
    )
    coverage = min(
        1.0,
        total / expected_assets,
    )
    confidence = _confidence(
        agreement,
        coverage,
    )

    features = {
        "btc_timeframe_minutes": btc_timeframe,
        "market_timeframe_minutes": market_timeframe,
        "btc_trend_score": round(trend_score, 3),
        "btc_adx": round(float(btc["adx"]), 3),
        "btc_atr_pct": round(
            float(btc["atr_pct"]),
            4,
        ),
        "btc_volatility_ratio": round(
            float(btc["volatility_ratio"]),
            4,
        ),
        "btc_return_24h_pct": round(
            btc_market_return,
            4,
        ),
        "breadth_above_ema20_pct": round(
            breadth20,
            3,
        ),
        "breadth_above_ema50_pct": round(
            breadth50,
            3,
        ),
        "breadth_above_ema200_pct": round(
            breadth200,
            3,
        ),
        "breadth_breakout_up_pct": round(
            breakout_up_pct,
            3,
        ),
        "breadth_breakout_down_pct": round(
            breakout_down_pct,
            3,
        ),
        "alt_relative_median_pct": round(
            alt_relative_median,
            4,
        ),
        "alt_outperform_share_pct": round(
            outperform_share,
            3,
        ),
        "alt_underperform_share_pct": round(
            underperform_share,
            3,
        ),
        "cross_asset_dispersion_pct": round(
            dispersion,
            4,
        ),
        "market_volatility_ratio": round(
            market_volatility_ratio,
            4,
        ),
        "assets_used": total,
    }

    return {
        "generated_utc": generated,
        "regime": regime,
        "regime_family": family,
        "confidence_pct": confidence,
        "volatility_state": volatility_state,
        "rotation_mode": "OBSERVATION_ONLY",
        "features": features,
        "reason": reason,
    }


def _history_row(
    result: dict[str, Any],
) -> dict[str, Any]:
    features = dict(result.get("features", {}))
    return {
        "generated_utc": result.get(
            "generated_utc",
            "",
        ),
        "regime": result.get("regime", "UNKNOWN"),
        "regime_family": result.get(
            "regime_family",
            "UNKNOWN",
        ),
        "confidence_pct": result.get(
            "confidence_pct",
            0.0,
        ),
        "volatility_state": result.get(
            "volatility_state",
            "UNKNOWN",
        ),
        "btc_timeframe_minutes": features.get(
            "btc_timeframe_minutes",
            0,
        ),
        "btc_trend_score": features.get(
            "btc_trend_score",
            0.0,
        ),
        "btc_adx": features.get("btc_adx", 0.0),
        "btc_atr_pct": features.get(
            "btc_atr_pct",
            0.0,
        ),
        "btc_volatility_ratio": features.get(
            "btc_volatility_ratio",
            0.0,
        ),
        "btc_return_24h_pct": features.get(
            "btc_return_24h_pct",
            0.0,
        ),
        "breadth_above_ema20_pct": features.get(
            "breadth_above_ema20_pct",
            0.0,
        ),
        "breadth_above_ema50_pct": features.get(
            "breadth_above_ema50_pct",
            0.0,
        ),
        "breadth_above_ema200_pct": features.get(
            "breadth_above_ema200_pct",
            0.0,
        ),
        "breadth_breakout_up_pct": features.get(
            "breadth_breakout_up_pct",
            0.0,
        ),
        "breadth_breakout_down_pct": features.get(
            "breadth_breakout_down_pct",
            0.0,
        ),
        "alt_relative_median_pct": features.get(
            "alt_relative_median_pct",
            0.0,
        ),
        "alt_outperform_share_pct": features.get(
            "alt_outperform_share_pct",
            0.0,
        ),
        "alt_underperform_share_pct": features.get(
            "alt_underperform_share_pct",
            0.0,
        ),
        "cross_asset_dispersion_pct": features.get(
            "cross_asset_dispersion_pct",
            0.0,
        ),
        "assets_used": features.get(
            "assets_used",
            0,
        ),
        "reason": result.get("reason", ""),
    }


def _parse_timestamp(value: Any) -> datetime | None:
    try:
        stamp = pd.Timestamp(value)
        if stamp.tzinfo is None:
            stamp = stamp.tz_localize("UTC")
        return stamp.to_pydatetime().astimezone(
            timezone.utc
        )
    except Exception:
        return None


def _last_history_row() -> dict[str, str] | None:
    if not HISTORY_PATH.exists():
        return None
    try:
        with HISTORY_PATH.open(
            "r",
            encoding="utf-8",
            newline="",
        ) as handle:
            rows = list(csv.DictReader(handle))
        return rows[-1] if rows else None
    except Exception:
        return None


def persist_regime_snapshot(
    result: dict[str, Any],
) -> None:
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    LATEST_PATH.write_text(
        json.dumps(
            result,
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )

    latest = _last_history_row()
    append = latest is None
    if latest is not None:
        previous_regime = str(
            latest.get("regime", "")
        )
        previous_time = _parse_timestamp(
            latest.get("generated_utc")
        )
        current_time = _parse_timestamp(
            result.get("generated_utc")
        )
        changed = (
            previous_regime
            != str(result.get("regime", ""))
        )
        elapsed_hour = (
            previous_time is None
            or current_time is None
            or (
                current_time - previous_time
            ).total_seconds()
            >= 3600
        )
        append = changed or elapsed_hour

    if not append:
        return

    exists = (
        HISTORY_PATH.exists()
        and HISTORY_PATH.stat().st_size > 0
    )
    with HISTORY_PATH.open(
        "a",
        encoding="utf-8",
        newline="",
    ) as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=HISTORY_FIELDS,
            extrasaction="ignore",
        )
        if not exists:
            writer.writeheader()
        writer.writerow(_history_row(result))
