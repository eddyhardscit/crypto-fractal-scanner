# -*- coding: utf-8 -*-
"""Signal generation for the KuCoin automatic paper-trading layer."""

from __future__ import annotations

import csv
import hashlib
import math
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

from kucoin_public_data import bundle_frames, safe_float

REPORTS_DIR = Path("reports")
GLOBAL_METRICS_PATH = REPORTS_DIR / "global_confluence_metrics.csv"
EXCHANGE_METRICS_PATH = REPORTS_DIR / "exchange_microstructure_metrics.csv"


@dataclass
class Signal:
    signal_id: str
    experiment_group_id: str
    portfolio: str
    is_main: bool
    strategy: str
    asset: str
    symbol: str
    timeframe_minutes: int
    candle_time: str
    side: str
    score: float
    confidence: str
    entry_reference_price: float
    atr_pct: float
    stop_pct: float
    target_pct: float
    leverage: float
    max_holding_hours: int
    trailing_at_r: float
    trailing_atr_multiple: float
    reason: str
    relative_strength_score: float
    breakout_state: str
    global_overlay: float
    exchange_overlay: float

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def _safe_num(value: Any, default: float = 0.0) -> float:
    number = safe_float(value, default)
    return default if not math.isfinite(number) else float(number)


def _read_latest_by_asset(path: Path) -> dict[str, dict[str, str]]:
    if not path.exists():
        return {}
    try:
        with path.open("r", encoding="utf-8", newline="") as handle:
            rows = list(csv.DictReader(handle))
    except Exception:
        return {}
    output: dict[str, dict[str, str]] = {}
    for row in rows:
        asset = str(row.get("asset", row.get("ticker", ""))).upper().replace("-USD", "").strip()
        if asset:
            output[asset] = row
    return output


def ema(series: pd.Series, span: int) -> pd.Series:
    return series.ewm(span=span, adjust=False, min_periods=span).mean()


def rsi(series: pd.Series, period: int = 14) -> pd.Series:
    delta = series.diff()
    gain = delta.clip(lower=0).ewm(alpha=1 / period, adjust=False, min_periods=period).mean()
    loss = (-delta.clip(upper=0)).ewm(alpha=1 / period, adjust=False, min_periods=period).mean()
    rs = gain / loss.replace(0, np.nan)
    result = 100 - 100 / (1 + rs)
    return result.fillna(50.0)


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
    return true_range.ewm(alpha=1 / period, adjust=False, min_periods=period).mean()


def adx(frame: pd.DataFrame, period: int = 14) -> pd.Series:
    up_move = frame["high"].diff()
    down_move = -frame["low"].diff()
    plus_dm = pd.Series(np.where((up_move > down_move) & (up_move > 0), up_move, 0.0), index=frame.index)
    minus_dm = pd.Series(np.where((down_move > up_move) & (down_move > 0), down_move, 0.0), index=frame.index)
    atr_value = atr(frame, period).replace(0, np.nan)
    plus_di = 100 * plus_dm.ewm(alpha=1 / period, adjust=False, min_periods=period).mean() / atr_value
    minus_di = 100 * minus_dm.ewm(alpha=1 / period, adjust=False, min_periods=period).mean() / atr_value
    dx = 100 * (plus_di - minus_di).abs() / (plus_di + minus_di).replace(0, np.nan)
    return dx.ewm(alpha=1 / period, adjust=False, min_periods=period).mean().fillna(0.0)


def _return_pct(series: pd.Series, bars: int) -> float:
    if len(series) <= bars:
        return 0.0
    start = float(series.iloc[-bars - 1])
    end = float(series.iloc[-1])
    return 0.0 if start <= 0 else (end / start - 1.0) * 100.0


def compute_features(frame: pd.DataFrame, btc_frame: pd.DataFrame | None = None) -> dict[str, Any]:
    if frame is None or len(frame) < 60:
        return {}
    data = frame.copy().sort_index()
    close = pd.to_numeric(data["close"], errors="coerce")
    high = pd.to_numeric(data["high"], errors="coerce")
    low = pd.to_numeric(data["low"], errors="coerce")
    volume = pd.to_numeric(data.get("volume", 0.0), errors="coerce").fillna(0.0)
    if close.isna().any() or close.iloc[-1] <= 0:
        return {}

    ema20 = ema(close, 20)
    ema50 = ema(close, 50)
    ema200 = ema(close, 200)
    rsi14 = rsi(close, 14)
    atr14 = atr(data, 14)
    adx14 = adx(data, 14)
    current = float(close.iloc[-1])
    atr_value = _safe_num(atr14.iloc[-1], 0.0)
    atr_pct = atr_value / current * 100.0 if current > 0 else 0.0

    prior_high_20 = float(high.shift(1).rolling(20, min_periods=10).max().iloc[-1])
    prior_low_20 = float(low.shift(1).rolling(20, min_periods=10).min().iloc[-1])
    breakout_state = "NONE"
    if math.isfinite(prior_high_20) and current > prior_high_20:
        breakout_state = "UP"
    elif math.isfinite(prior_low_20) and current < prior_low_20:
        breakout_state = "DOWN"

    volume_median = float(volume.tail(30).median()) if len(volume) >= 10 else 0.0
    volume_ratio = float(volume.iloc[-1] / volume_median) if volume_median > 0 else 1.0
    ret_short = _return_pct(close, 6)
    ret_medium = _return_pct(close, 24)
    ret_long = _return_pct(close, 72)

    btc_ret_medium = 0.0
    btc_ret_long = 0.0
    if btc_frame is not None and not btc_frame.empty:
        btc_close = pd.to_numeric(btc_frame["close"], errors="coerce").dropna()
        btc_ret_medium = _return_pct(btc_close, min(24, max(1, len(btc_close) - 2)))
        btc_ret_long = _return_pct(btc_close, min(72, max(1, len(btc_close) - 2)))

    return {
        "candle_time": pd.Timestamp(data.index[-1]).isoformat(),
        "price": current,
        "ema20": _safe_num(ema20.iloc[-1], current),
        "ema50": _safe_num(ema50.iloc[-1], current),
        "ema200": _safe_num(ema200.iloc[-1], current),
        "rsi14": _safe_num(rsi14.iloc[-1], 50.0),
        "atr_pct": max(0.0, atr_pct),
        "adx14": _safe_num(adx14.iloc[-1], 0.0),
        "volume_ratio": max(0.0, volume_ratio),
        "ret_short_pct": ret_short,
        "ret_medium_pct": ret_medium,
        "ret_long_pct": ret_long,
        "relative_medium_pct": ret_medium - btc_ret_medium,
        "relative_long_pct": ret_long - btc_ret_long,
        "breakout_state": breakout_state,
        "prior_high_20": prior_high_20,
        "prior_low_20": prior_low_20,
    }


def global_overlay_for_asset(asset: str, rows: dict[str, dict[str, str]]) -> tuple[float, str]:
    row = rows.get(asset, {})
    if not row:
        return 0.0, "Global non disponibile"
    raw = _safe_num(row.get("global_score"), 0.0)
    overlay = max(-2.0, min(2.0, raw / 3.0))
    action = str(row.get("action", row.get("direction", ""))).strip()
    return overlay, f"Global {raw:+.0f} {action}".strip()


def exchange_overlay_for_asset(asset: str, rows: dict[str, dict[str, str]]) -> tuple[float, str]:
    row = rows.get(asset, {})
    if not row:
        return 0.0, "Exchange non disponibile"
    raw = _safe_num(row.get("candidate_global_score", row.get("raw_score", 0.0)), 0.0)
    coverage = _safe_num(row.get("data_coverage"), 0.0)
    overlay = max(-1.0, min(1.0, raw / 4.0))
    if coverage and coverage < 0.5:
        overlay *= 0.5
    return overlay, f"Exchange raw {raw:+.1f}, coverage {coverage:.2f}"


def score_features(features: dict[str, Any], global_overlay: float, exchange_overlay: float) -> tuple[float, list[str]]:
    price = features["price"]
    ema20_value = features["ema20"]
    ema50_value = features["ema50"]
    ema200_value = features["ema200"]
    score = 0.0
    reasons: list[str] = []

    if price > ema20_value > ema50_value:
        score += 2.0
        reasons.append("prezzo>EMA20>EMA50")
    elif price < ema20_value < ema50_value:
        score -= 2.0
        reasons.append("prezzo<EMA20<EMA50")
    if price > ema200_value and ema50_value > ema200_value:
        score += 1.5
        reasons.append("trend sopra EMA200")
    elif price < ema200_value and ema50_value < ema200_value:
        score -= 1.5
        reasons.append("trend sotto EMA200")

    rsi14_value = features["rsi14"]
    if 55 <= rsi14_value <= 72:
        score += 1.5
        reasons.append(f"RSI costruttivo {rsi14_value:.1f}")
    elif 28 <= rsi14_value <= 45:
        score -= 1.5
        reasons.append(f"RSI debole {rsi14_value:.1f}")
    elif rsi14_value > 78:
        score -= 0.5
        reasons.append("RSI molto tirato")
    elif rsi14_value < 22:
        score += 0.5
        reasons.append("RSI molto scarico")

    breakout_state = features["breakout_state"]
    if breakout_state == "UP":
        score += 1.5
        reasons.append("breakout 20 barre")
    elif breakout_state == "DOWN":
        score -= 1.5
        reasons.append("breakdown 20 barre")

    if features["adx14"] >= 22:
        direction = 1.0 if features["ret_short_pct"] > 0 else -1.0 if features["ret_short_pct"] < 0 else 0.0
        score += direction * 0.75
        reasons.append(f"ADX {features['adx14']:.1f}")
    if features["volume_ratio"] >= 1.5:
        direction = 0.5 if features["ret_short_pct"] > 0 else -0.5 if features["ret_short_pct"] < 0 else 0.0
        score += direction
        reasons.append(f"volume x{features['volume_ratio']:.1f}")

    relative = 0.65 * features["relative_medium_pct"] + 0.35 * features["relative_long_pct"]
    relative_score = max(-2.0, min(2.0, relative / 5.0))
    score += relative_score
    if abs(relative_score) >= 0.4:
        reasons.append(f"forza vs BTC {relative:+.1f}%")

    score += global_overlay + exchange_overlay
    return max(-10.0, min(10.0, score)), reasons


def confidence_from_score(score: float) -> str:
    absolute = abs(score)
    if absolute >= 7.5:
        return "ALTA"
    if absolute >= 6.0:
        return "BUONA"
    if absolute >= 4.5:
        return "MEDIA"
    return "BASSA"


def deterministic_id(*parts: Any, length: int = 20) -> str:
    raw = "|".join(str(part) for part in parts)
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()[:length]


def strategy_accepts(strategy: str, side: str, features: dict[str, Any], score: float) -> bool:
    if strategy == "momentum_breakout":
        return features["breakout_state"] == ("UP" if side == "LONG" else "DOWN") or abs(features["ret_short_pct"]) >= 1.5
    if strategy == "relative_strength":
        relative = 0.65 * features["relative_medium_pct"] + 0.35 * features["relative_long_pct"]
        return relative >= 2.0 if side == "LONG" else relative <= -2.0
    return True


def generate_signals(bundle: dict[str, Any], config: dict[str, Any]) -> list[Signal]:
    frames = bundle_frames(bundle)
    global_rows = _read_latest_by_asset(GLOBAL_METRICS_PATH)
    exchange_rows = _read_latest_by_asset(EXCHANGE_METRICS_PATH)
    btc_frames = frames.get("BTC", {})
    signals: list[Signal] = []

    for portfolio in config.get("portfolios", []):
        if not portfolio.get("enabled", True):
            continue
        timeframe = int(portfolio["timeframe_minutes"])
        minimum_score = float(portfolio["minimum_abs_score"])
        strategy = str(portfolio.get("strategy", "confluence_trend"))

        for asset, payload in bundle.get("assets", {}).items():
            frame = frames.get(asset, {}).get(timeframe)
            btc_frame = btc_frames.get(timeframe)
            features = compute_features(frame, btc_frame if asset != "BTC" else frame)
            if not features:
                continue
            global_overlay, global_reason = global_overlay_for_asset(asset, global_rows)
            exchange_overlay, exchange_reason = exchange_overlay_for_asset(asset, exchange_rows)
            score, reasons = score_features(features, global_overlay, exchange_overlay)

            if abs(score) < minimum_score:
                continue
            side = "LONG" if score > 0 else "SHORT"
            if side == "LONG" and not portfolio.get("allow_long", True):
                continue
            if side == "SHORT" and not portfolio.get("allow_short", True):
                continue
            if not strategy_accepts(strategy, side, features, score):
                continue

            atr_pct = max(float(config["risk"].get("minimum_stop_pct", 0.008)) * 100.0, features["atr_pct"])
            stop_pct = atr_pct / 100.0 * float(portfolio.get("atr_stop_multiple", 2.0))
            stop_pct = max(float(config["risk"].get("minimum_stop_pct", 0.008)), stop_pct)
            stop_pct = min(float(config["risk"].get("maximum_stop_pct", 0.12)), stop_pct)
            target_pct = stop_pct * float(portfolio.get("reward_risk", 2.0))
            candle_time = features["candle_time"]
            experiment_group = deterministic_id(asset, timeframe, candle_time, side, "market_event")
            signal_id = deterministic_id(portfolio["name"], strategy, experiment_group)
            relative_blend = 0.65 * features["relative_medium_pct"] + 0.35 * features["relative_long_pct"]
            reason = "; ".join(reasons + [global_reason, exchange_reason])

            signals.append(
                Signal(
                    signal_id=signal_id,
                    experiment_group_id=experiment_group,
                    portfolio=str(portfolio["name"]),
                    is_main=bool(portfolio.get("is_main")),
                    strategy=strategy,
                    asset=asset,
                    symbol=str(payload.get("symbol", "")),
                    timeframe_minutes=timeframe,
                    candle_time=candle_time,
                    side=side,
                    score=round(score, 4),
                    confidence=confidence_from_score(score),
                    entry_reference_price=float(payload.get("mark_price") or features["price"]),
                    atr_pct=round(features["atr_pct"], 6),
                    stop_pct=round(stop_pct, 8),
                    target_pct=round(target_pct, 8),
                    leverage=float(portfolio.get("leverage", config["risk"].get("default_leverage", 1.0))),
                    max_holding_hours=int(portfolio.get("max_holding_hours", 168)),
                    trailing_at_r=float(portfolio.get("trailing_at_r", 0.0)),
                    trailing_atr_multiple=float(portfolio.get("trailing_atr_multiple", 0.0)),
                    reason=reason,
                    relative_strength_score=round(relative_blend, 4),
                    breakout_state=str(features["breakout_state"]),
                    global_overlay=round(global_overlay, 4),
                    exchange_overlay=round(exchange_overlay, 4),
                )
            )
    return signals
