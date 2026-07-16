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
from paper_rsi_extreme_scalping import extreme_reversal_setup
from market_regime_tagger import classify_market_regime

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
    bollinger_mid = close.rolling(20, min_periods=20).mean()
    bollinger_std = close.rolling(20, min_periods=20).std(ddof=0)
    bollinger_upper = bollinger_mid + 2.0 * bollinger_std
    bollinger_lower = bollinger_mid - 2.0 * bollinger_std
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
        "bollinger_mid": _safe_num(
            bollinger_mid.iloc[-1],
            current,
        ),
        "bollinger_upper": _safe_num(
            bollinger_upper.iloc[-1],
            current,
        ),
        "bollinger_lower": _safe_num(
            bollinger_lower.iloc[-1],
            current,
        ),
        "bollinger_zscore": (
            (current - _safe_num(bollinger_mid.iloc[-1], current))
            / max(_safe_num(bollinger_std.iloc[-1], 0.0), 1e-12)
        ),
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


def benchmark_strategy_score(
    strategy: str,
    features: dict[str, Any],
) -> tuple[bool, float, list[str]]:
    """Pure benchmark rules, independent from global/exchange overlays."""
    price = float(features["price"])
    rsi14_value = float(features["rsi14"])
    adx14_value = float(features["adx14"])
    volume_ratio = float(features["volume_ratio"])
    ret_medium = float(features["ret_medium_pct"])

    if strategy == "donchian_breakout":
        state = str(features["breakout_state"])
        if state == "UP" and adx14_value >= 18:
            score = 5.0 + min(2.0, adx14_value / 25.0)
            score += min(1.0, max(0.0, volume_ratio - 1.0))
            return True, score, [
                "breakout Donchian 20 barre",
                f"ADX {adx14_value:.1f}",
                f"volume x{volume_ratio:.1f}",
            ]
        if state == "DOWN" and adx14_value >= 18:
            score = 5.0 + min(2.0, adx14_value / 25.0)
            score += min(1.0, max(0.0, volume_ratio - 1.0))
            return True, -score, [
                "breakdown Donchian 20 barre",
                f"ADX {adx14_value:.1f}",
                f"volume x{volume_ratio:.1f}",
            ]
        return False, 0.0, []

    if strategy == "bollinger_mean_reversion":
        upper = float(features["bollinger_upper"])
        lower = float(features["bollinger_lower"])
        zscore = float(features["bollinger_zscore"])
        if price <= lower and rsi14_value <= 30:
            score = 5.0 + min(2.5, abs(zscore))
            return True, score, [
                "prezzo sotto Bollinger inferiore",
                f"RSI {rsi14_value:.1f}",
                f"z-score {zscore:.2f}",
            ]
        if price >= upper and rsi14_value >= 70:
            score = 5.0 + min(2.5, abs(zscore))
            return True, -score, [
                "prezzo sopra Bollinger superiore",
                f"RSI {rsi14_value:.1f}",
                f"z-score {zscore:.2f}",
            ]
        return False, 0.0, []

    if strategy == "ema_trend_following":
        ema20_value = float(features["ema20"])
        ema50_value = float(features["ema50"])
        if (
            price > ema20_value > ema50_value
            and adx14_value >= 20
            and ret_medium > 0
        ):
            score = 5.0 + min(2.0, adx14_value / 25.0)
            return True, score, [
                "prezzo>EMA20>EMA50",
                f"ADX {adx14_value:.1f}",
                f"ritorno medio {ret_medium:+.1f}%",
            ]
        if (
            price < ema20_value < ema50_value
            and adx14_value >= 20
            and ret_medium < 0
        ):
            score = 5.0 + min(2.0, adx14_value / 25.0)
            return True, -score, [
                "prezzo<EMA20<EMA50",
                f"ADX {adx14_value:.1f}",
                f"ritorno medio {ret_medium:+.1f}%",
            ]
        return False, 0.0, []

    return False, 0.0, []


def build_live_scanner_ranking(
    features_by_asset: dict[str, dict[str, Any]],
) -> list[dict[str, Any]]:
    """Rank the live KuCoin paper universe without using future data."""
    rows: list[dict[str, Any]] = []
    for asset, features in features_by_asset.items():
        if not features:
            continue

        price = float(features["price"])
        ema20_value = float(features["ema20"])
        ema50_value = float(features["ema50"])
        ema200_value = float(features["ema200"])
        rsi14_value = float(features["rsi14"])
        adx14_value = float(features["adx14"])
        volume_ratio = float(features["volume_ratio"])
        ret_short = float(features["ret_short_pct"])
        ret_medium = float(features["ret_medium_pct"])
        ret_long = float(features["ret_long_pct"])
        relative_medium = float(features["relative_medium_pct"])
        relative_long = float(features["relative_long_pct"])
        breakout_state = str(features["breakout_state"])

        score = (
            0.30 * ret_short
            + 0.25 * ret_medium
            + 0.10 * ret_long
            + 0.20 * relative_medium
            + 0.10 * relative_long
        )

        if price > ema20_value > ema50_value:
            score += 2.0
        elif price < ema20_value < ema50_value:
            score -= 2.0

        if price > ema200_value and ema50_value > ema200_value:
            score += 1.0
        elif price < ema200_value and ema50_value < ema200_value:
            score -= 1.0

        if breakout_state == "UP":
            score += 1.25
        elif breakout_state == "DOWN":
            score -= 1.25

        if adx14_value >= 20:
            score += 0.75 if ret_short > 0 else -0.75 if ret_short < 0 else 0.0
        if volume_ratio >= 1.5:
            score += 0.5 if ret_short > 0 else -0.5 if ret_short < 0 else 0.0
        if rsi14_value >= 75:
            score -= 0.35
        elif rsi14_value <= 25:
            score += 0.35

        rows.append(
            {
                "asset": asset,
                "score": max(-20.0, min(20.0, score)),
                "relative_medium_pct": relative_medium,
                "relative_long_pct": relative_long,
                "breakout_state": breakout_state,
                "features": features,
            }
        )

    rows.sort(key=lambda row: row["score"], reverse=True)
    for rank, row in enumerate(rows, start=1):
        row["rank"] = rank
        row["reverse_rank"] = len(rows) - rank + 1
    return rows


def scanner_family_score(
    strategy: str,
    asset: str,
    features: dict[str, Any],
    ranking_by_asset: dict[str, dict[str, Any]],
    global_rows: dict[str, dict[str, str]],
    exchange_rows: dict[str, dict[str, str]],
    portfolio: dict[str, Any],
) -> tuple[bool, float, list[str]]:
    row = ranking_by_asset.get(asset)
    if not row:
        return False, 0.0, []

    rank = int(row["rank"])
    universe_size = len(ranking_by_asset)
    top_n = max(1, int(portfolio.get("scanner_top_n", 5)))
    bottom_threshold = max(1, universe_size - top_n + 1)
    rank_score = float(row["score"])
    relative_medium = float(features["relative_medium_pct"])
    relative_long = float(features["relative_long_pct"])
    relative_blend = 0.65 * relative_medium + 0.35 * relative_long
    price = float(features["price"])
    ema20_value = float(features["ema20"])
    ema50_value = float(features["ema50"])
    adx14_value = float(features["adx14"])
    breakout_state = str(features["breakout_state"])

    long_confirmed = (
        price > ema20_value
        and (
            ema20_value > ema50_value
            or breakout_state == "UP"
        )
        and adx14_value >= 16
    )
    short_confirmed = (
        price < ema20_value
        and (
            ema20_value < ema50_value
            or breakout_state == "DOWN"
        )
        and adx14_value >= 16
    )

    if strategy == "scanner_top5_long":
        minimum = float(portfolio.get("minimum_scanner_rank_score", 1.0))
        accepted = rank <= top_n and rank_score >= minimum and long_confirmed
        return accepted, max(5.0, min(9.5, 5.0 + rank_score / 4.0)), [
            f"rank live {rank}/{universe_size}",
            f"scanner score {rank_score:+.2f}",
            "conferma tecnica long",
        ]

    if strategy == "scanner_bottom5_short":
        maximum = float(portfolio.get("maximum_scanner_rank_score", -1.0))
        accepted = (
            rank >= bottom_threshold
            and rank_score <= maximum
            and short_confirmed
        )
        return accepted, -max(5.0, min(9.5, 5.0 + abs(rank_score) / 4.0)), [
            f"rank live {rank}/{universe_size}",
            f"scanner score {rank_score:+.2f}",
            "conferma tecnica short",
        ]

    if strategy == "scanner_top5_btc_strength":
        minimum_relative = float(
            portfolio.get("minimum_relative_strength_pct", 0.5)
        )
        accepted = (
            rank <= top_n
            and rank_score >= float(
                portfolio.get("minimum_scanner_rank_score", 1.0)
            )
            and relative_blend >= minimum_relative
            and long_confirmed
        )
        return accepted, max(5.0, min(9.5, 5.0 + rank_score / 4.0)), [
            f"rank live {rank}/{universe_size}",
            f"scanner score {rank_score:+.2f}",
            f"forza vs BTC {relative_blend:+.2f}%",
            "conferma tecnica long",
        ]

    if strategy == "global_confluence_pure":
        global_row = global_rows.get(asset, {})
        exchange_row = exchange_rows.get(asset, {})
        global_score = _safe_num(global_row.get("global_score"), 0.0)
        action = str(
            global_row.get(
                "action",
                global_row.get("direction", ""),
            )
        ).upper()
        exchange_score = _safe_num(
            exchange_row.get(
                "candidate_global_score",
                exchange_row.get("raw_score"),
            ),
            0.0,
        )
        minimum_global = float(
            portfolio.get("minimum_global_score", 4.0)
        )
        minimum_exchange = float(
            portfolio.get("minimum_exchange_alignment", 0.0)
        )

        long_action = any(
            token in action
            for token in ("LONG", "BUY", "RIALZ", "ACCUM")
        )
        short_action = any(
            token in action
            for token in ("SHORT", "SELL", "RIBASS", "DISTRIB")
        )

        if (
            global_score >= minimum_global
            and exchange_score >= minimum_exchange
            and long_action
            and long_confirmed
        ):
            score = min(
                9.5,
                max(5.0, 5.0 + global_score / 3.0),
            )
            return True, score, [
                f"Global {global_score:+.1f} {action}",
                f"Exchange {exchange_score:+.1f}",
                "struttura tecnica long allineata",
            ]

        if (
            global_score <= -minimum_global
            and exchange_score <= -minimum_exchange
            and short_action
            and short_confirmed
        ):
            score = min(
                9.5,
                max(5.0, 5.0 + abs(global_score) / 3.0),
            )
            return True, -score, [
                f"Global {global_score:+.1f} {action}",
                f"Exchange {exchange_score:+.1f}",
                "struttura tecnica short allineata",
            ]

        return False, 0.0, []

    return False, 0.0, []


def combined_strategy_score(
    strategy: str,
    asset: str,
    features: dict[str, Any],
    ranking_by_asset: dict[str, dict[str, Any]],
    global_rows: dict[str, dict[str, str]],
    exchange_rows: dict[str, dict[str, str]],
    portfolio: dict[str, Any],
) -> tuple[bool, float, list[str]]:
    """Consensus strategies built from existing independent modules."""
    component_votes: list[tuple[str, float, list[str]]] = []

    def add_vote(
        label: str,
        accepted: bool,
        score: float,
        reasons: list[str],
    ) -> None:
        if accepted and abs(score) > 0:
            component_votes.append(
                (label, score, reasons)
            )

    def consensus(
        minimum_votes: int,
        extra_reasons: list[str] | None = None,
    ) -> tuple[bool, float, list[str]]:
        long_votes = [
            item for item in component_votes if item[1] > 0
        ]
        short_votes = [
            item for item in component_votes if item[1] < 0
        ]
        selected = (
            long_votes
            if len(long_votes) > len(short_votes)
            else short_votes
        )
        if len(selected) < minimum_votes:
            return False, 0.0, []

        direction = 1.0 if selected[0][1] > 0 else -1.0
        magnitude = sum(abs(item[1]) for item in selected) / len(selected)
        magnitude = max(5.0, min(9.5, magnitude))
        reasons = [
            f"{label}: {', '.join(details[:2])}"
            for label, _, details in selected
        ]
        reasons.append(
            f"consenso {len(selected)}/{len(component_votes)} moduli"
        )
        reasons.extend(extra_reasons or [])
        return True, direction * magnitude, reasons

    relative_blend = (
        0.65 * float(features["relative_medium_pct"])
        + 0.35 * float(features["relative_long_pct"])
    )
    global_row = global_rows.get(asset, {})
    global_score = _safe_num(
        global_row.get("global_score"),
        0.0,
    )
    global_action = str(
        global_row.get(
            "action",
            global_row.get("direction", ""),
        )
    ).upper()

    if strategy in {"combo_trend", "combo_adaptive"}:
        ema_ok, ema_score, ema_reasons = benchmark_strategy_score(
            "ema_trend_following",
            features,
        )
        add_vote("EMA", ema_ok, ema_score, ema_reasons)

        don_ok, don_score, don_reasons = benchmark_strategy_score(
            "donchian_breakout",
            features,
        )
        add_vote(
            "Donchian",
            don_ok,
            don_score,
            don_reasons,
        )

        if abs(relative_blend) >= 1.0:
            add_vote(
                "Forza BTC",
                True,
                (
                    max(5.0, min(8.0, 5.0 + abs(relative_blend) / 2.0))
                    * (1.0 if relative_blend > 0 else -1.0)
                ),
                [f"forza relativa {relative_blend:+.2f}%"],
            )

        long_global = (
            global_score >= 3.0
            and any(
                token in global_action
                for token in ("LONG", "BUY", "RIALZ", "ACCUM")
            )
        )
        short_global = (
            global_score <= -3.0
            and any(
                token in global_action
                for token in ("SHORT", "SELL", "RIBASS", "DISTRIB")
            )
        )
        if long_global or short_global:
            add_vote(
                "Global",
                True,
                (
                    max(5.0, min(9.0, 5.0 + abs(global_score) / 3.0))
                    * (1.0 if long_global else -1.0)
                ),
                [f"Global {global_score:+.1f} {global_action}"],
            )

        if strategy == "combo_trend":
            if float(features["adx14"]) < 18.0:
                return False, 0.0, []
            return consensus(
                int(portfolio.get("minimum_combo_votes", 2)),
                [f"ADX trend {float(features['adx14']):.1f}"],
            )

    if strategy in {"combo_mean_reversion", "combo_adaptive"}:
        if strategy == "combo_adaptive":
            component_votes.clear()

        boll_ok, boll_score, boll_reasons = benchmark_strategy_score(
            "bollinger_mean_reversion",
            features,
        )
        add_vote(
            "Bollinger",
            boll_ok,
            boll_score,
            boll_reasons,
        )

        rsi_value = float(features["rsi14"])
        if rsi_value <= 32.0:
            add_vote(
                "RSI",
                True,
                5.0 + min(2.5, (32.0 - rsi_value) / 5.0),
                [f"RSI scarico {rsi_value:.1f}"],
            )
        elif rsi_value >= 68.0:
            add_vote(
                "RSI",
                True,
                -(5.0 + min(2.5, (rsi_value - 68.0) / 5.0)),
                [f"RSI tirato {rsi_value:.1f}"],
            )

        zscore = float(features["bollinger_zscore"])
        if abs(zscore) >= 1.6:
            add_vote(
                "Z-score",
                True,
                (
                    -(5.0 + min(2.0, abs(zscore) - 1.0))
                    if zscore > 0
                    else 5.0 + min(2.0, abs(zscore) - 1.0)
                ),
                [f"z-score {zscore:+.2f}"],
            )

        if strategy == "combo_mean_reversion":
            if float(features["adx14"]) > 25.0:
                return False, 0.0, []
            return consensus(
                int(portfolio.get("minimum_combo_votes", 2)),
                [f"ADX laterale {float(features['adx14']):.1f}"],
            )

    if strategy in {"combo_scanner", "combo_adaptive"}:
        if strategy == "combo_adaptive":
            component_votes.clear()

        for source_strategy, label in (
            ("scanner_top5_long", "Top 5"),
            ("scanner_bottom5_short", "Bottom 5"),
            ("scanner_top5_btc_strength", "Forza BTC"),
            ("global_confluence_pure", "Global"),
        ):
            accepted, source_score, source_reasons = (
                scanner_family_score(
                    source_strategy,
                    asset,
                    features,
                    ranking_by_asset,
                    global_rows,
                    exchange_rows,
                    portfolio,
                )
            )
            add_vote(
                label,
                accepted,
                source_score,
                source_reasons,
            )

        if strategy == "combo_scanner":
            return consensus(
                int(portfolio.get("minimum_combo_votes", 2)),
                ["consenso scanner live"],
            )

    if strategy == "combo_adaptive":
        adx_value = float(features["adx14"])

        # Rebuild and delegate to the family suited to the regime.
        delegated = dict(portfolio)
        if adx_value >= 22.0:
            delegated["minimum_combo_votes"] = max(
                2,
                int(portfolio.get("minimum_combo_votes", 2)),
            )
            accepted, value, reasons = combined_strategy_score(
                "combo_trend",
                asset,
                features,
                ranking_by_asset,
                global_rows,
                exchange_rows,
                delegated,
            )
            if accepted:
                return True, value, [
                    "regime adattivo: TREND",
                    *reasons,
                ]
        elif adx_value <= 18.0:
            accepted, value, reasons = combined_strategy_score(
                "combo_mean_reversion",
                asset,
                features,
                ranking_by_asset,
                global_rows,
                exchange_rows,
                delegated,
            )
            if accepted:
                return True, value, [
                    "regime adattivo: RANGE",
                    *reasons,
                ]
        else:
            accepted, value, reasons = combined_strategy_score(
                "combo_scanner",
                asset,
                features,
                ranking_by_asset,
                global_rows,
                exchange_rows,
                delegated,
            )
            if accepted:
                return True, value, [
                    "regime adattivo: TRANSIZIONE",
                    *reasons,
                ]

    return False, 0.0, []



# RELATIVE_STRENGTH_V2_RULES_V2
def relative_strength_v2_accepts(
    side: str,
    features: dict[str, Any],
    portfolio: dict[str, Any],
    market_context: dict[str, Any],
) -> bool:
    relative = (
        0.65 * float(features["relative_medium_pct"])
        + 0.35 * float(features["relative_long_pct"])
    )
    minimum_relative = float(
        portfolio.get("minimum_relative_strength_pct", 3.0)
    )
    if float(features["adx14"]) < float(
        portfolio.get("minimum_adx", 18.0)
    ):
        return False

    regime = str(market_context.get("regime", "UNKNOWN")).upper()
    excluded = {
        str(value).upper()
        for value in portfolio.get("excluded_regimes", ["RANGE_HIGH_VOL"])
    }
    if regime in excluded:
        return False

    price = float(features["price"])
    ema20_value = float(features["ema20"])
    ema50_value = float(features["ema50"])
    rsi_value = float(features["rsi14"])
    ret_short = float(features["ret_short_pct"])
    ret_medium = float(features["ret_medium_pct"])

    if side == "LONG":
        return (
            relative >= minimum_relative
            and price > ema20_value > ema50_value
            and ret_short > 0.0
            and ret_medium > 0.0
            and float(portfolio.get("long_rsi_min", 52.0))
            <= rsi_value
            <= float(portfolio.get("long_rsi_max", 72.0))
        )

    context_features = dict(market_context.get("features", {}))
    broad_bullish = (
        float(context_features.get("btc_trend_score", 0.0))
        >= float(portfolio.get("broad_bullish_btc_trend_score", 2.0))
        and float(context_features.get("breadth_above_ema50_pct", 0.0))
        >= float(
            portfolio.get(
                "broad_bullish_breadth_above_ema50_pct",
                55.0,
            )
        )
        and float(context_features.get("alt_relative_median_pct", 0.0))
        >= float(
            portfolio.get(
                "broad_bullish_alt_relative_median_pct",
                0.0,
            )
        )
    )
    if portfolio.get("block_short_in_broad_bullish_market", True) and broad_bullish:
        return False

    return (
        relative <= -minimum_relative
        and price < ema20_value < ema50_value
        and ret_short < 0.0
        and ret_medium < 0.0
        and float(portfolio.get("short_rsi_min", 28.0))
        <= rsi_value
        <= float(portfolio.get("short_rsi_max", 48.0))
    )


def apply_signal_caps(
    signals: list[Signal],
    config: dict[str, Any],
) -> list[Signal]:
    definitions = {
        str(row.get("name")): row
        for row in config.get("portfolios", [])
    }
    keep: set[int] = set()
    grouped: dict[
        tuple[str, str, str],
        list[tuple[int, Signal]],
    ] = {}

    for index, signal in enumerate(signals):
        definition = definitions.get(str(signal.portfolio), {})
        limit = int(definition.get("max_signals_per_candle_side", 0) or 0)
        if limit <= 0:
            keep.add(index)
            continue
        key = (
            str(signal.portfolio),
            str(signal.candle_time),
            str(signal.side),
        )
        grouped.setdefault(key, []).append((index, signal))

    for rows in grouped.values():
        definition = definitions.get(str(rows[0][1].portfolio), {})
        limit = int(definition.get("max_signals_per_candle_side", 0) or 0)
        ranked = sorted(
            rows,
            key=lambda item: (
                abs(float(item[1].relative_strength_score)),
                abs(float(item[1].score)),
                str(item[1].asset),
            ),
            reverse=True,
        )
        keep.update(index for index, _ in ranked[:limit])

    return [
        signal
        for index, signal in enumerate(signals)
        if index in keep
    ]


def strategy_accepts(
    strategy: str,
    side: str,
    features: dict[str, Any],
    score: float,
) -> bool:
    if strategy == "momentum_breakout":
        return (
            features["breakout_state"]
            == ("UP" if side == "LONG" else "DOWN")
            or abs(features["ret_short_pct"]) >= 1.5
        )
    if strategy == "relative_strength":
        relative = (
            0.65 * features["relative_medium_pct"]
            + 0.35 * features["relative_long_pct"]
        )
        return (
            relative >= 2.0
            if side == "LONG"
            else relative <= -2.0
        )
    if strategy == "rsi_extreme_reversal":
        return bool(features.get("extreme_accepted"))
    return True


def generate_signals(
    bundle: dict[str, Any],
    config: dict[str, Any],
) -> list[Signal]:
    frames = bundle_frames(bundle)
    global_rows = _read_latest_by_asset(
        GLOBAL_METRICS_PATH
    )
    exchange_rows = _read_latest_by_asset(
        EXCHANGE_METRICS_PATH
    )
    btc_frames = frames.get("BTC", {})
    signals: list[Signal] = []
    market_context = classify_market_regime(bundle)

    scanner_features_1h: dict[str, dict[str, Any]] = {}
    for asset in bundle.get("assets", {}):
        frame = frames.get(asset, {}).get(60)
        btc_frame = btc_frames.get(60)
        features = compute_features(
            frame,
            btc_frame if asset != "BTC" else frame,
        )
        if features:
            scanner_features_1h[asset] = features

    scanner_ranking = build_live_scanner_ranking(
        scanner_features_1h
    )
    scanner_ranking_by_asset = {
        str(row["asset"]): row
        for row in scanner_ranking
    }

    for portfolio in config.get("portfolios", []):
        if not portfolio.get("enabled", True):
            continue

        timeframe = int(portfolio["timeframe_minutes"])
        minimum_score = float(
            portfolio["minimum_abs_score"]
        )
        strategy = str(
            portfolio.get(
                "strategy",
                "confluence_trend",
            )
        )
        allowed_assets = {
            str(value).upper().strip()
            for value in portfolio.get("assets", [])
            if str(value).strip()
        }

        for asset, payload in bundle.get(
            "assets",
            {},
        ).items():
            if (
                allowed_assets
                and str(asset).upper() not in allowed_assets
            ):
                continue
            frame = frames.get(asset, {}).get(timeframe)
            btc_frame = btc_frames.get(timeframe)
            features = compute_features(
                frame,
                btc_frame if asset != "BTC" else frame,
            )
            if not features:
                continue

            global_overlay, global_reason = (
                global_overlay_for_asset(
                    asset,
                    global_rows,
                )
            )
            exchange_overlay, exchange_reason = (
                exchange_overlay_for_asset(
                    asset,
                    exchange_rows,
                )
            )

            if strategy == "rsi_extreme_reversal":
                side = str(
                    portfolio.get(
                        "reversal_side",
                        "LONG",
                    )
                ).upper()
                setup = extreme_reversal_setup(
                    frame,
                    side,
                    portfolio,
                )
                score = float(
                    setup.get("score", 0.0)
                )
                if (
                    score < minimum_score
                    or not setup.get("accepted")
                ):
                    continue
                if (
                    side == "LONG"
                    and not portfolio.get(
                        "allow_long",
                        True,
                    )
                ):
                    continue
                if (
                    side == "SHORT"
                    and not portfolio.get(
                        "allow_short",
                        True,
                    )
                ):
                    continue

                stop_pct = float(
                    setup.get("stop_pct", 0.0)
                )
                target_pct = stop_pct * float(
                    portfolio.get("reward_risk", 1.5)
                )
                candle_time = str(
                    setup.get(
                        "candle_time",
                        features["candle_time"],
                    )
                )
                experiment_group = deterministic_id(
                    asset,
                    timeframe,
                    candle_time,
                    side,
                    "rsi_extreme_reversal_event",
                )
                signal_id = deterministic_id(
                    portfolio["name"],
                    strategy,
                    experiment_group,
                )
                relative_blend = (
                    0.65
                    * features["relative_medium_pct"]
                    + 0.35
                    * features["relative_long_pct"]
                )
                reason = "; ".join(
                    list(setup.get("reasons", []))
                    + [
                        global_reason
                        + " (solo contesto, peso 0)",
                        exchange_reason
                        + " (solo contesto, peso 0)",
                    ]
                )

                signals.append(
                    Signal(
                        signal_id=signal_id,
                        experiment_group_id=experiment_group,
                        portfolio=str(
                            portfolio["name"]
                        ),
                        is_main=bool(
                            portfolio.get("is_main")
                        ),
                        strategy=strategy,
                        asset=asset,
                        symbol=str(
                            payload.get("symbol", "")
                        ),
                        timeframe_minutes=timeframe,
                        candle_time=candle_time,
                        side=side,
                        score=round(score, 4),
                        confidence=confidence_from_score(
                            score
                        ),
                        entry_reference_price=float(
                            payload.get("mark_price")
                            or features["price"]
                        ),
                        atr_pct=round(
                            float(
                                setup.get(
                                    "atr_pct",
                                    0.0,
                                )
                            ),
                            6,
                        ),
                        stop_pct=round(
                            stop_pct,
                            8,
                        ),
                        target_pct=round(
                            target_pct,
                            8,
                        ),
                        leverage=float(
                            portfolio.get(
                                "leverage",
                                config["risk"].get(
                                    "default_leverage",
                                    1.0,
                                ),
                            )
                        ),
                        max_holding_hours=int(
                            portfolio.get(
                                "max_holding_hours",
                                4,
                            )
                        ),
                        trailing_at_r=float(
                            portfolio.get(
                                "trailing_at_r",
                                1.0,
                            )
                        ),
                        trailing_atr_multiple=float(
                            portfolio.get(
                                "trailing_atr_multiple",
                                0.8,
                            )
                        ),
                        reason=reason,
                        relative_strength_score=round(
                            relative_blend,
                            4,
                        ),
                        breakout_state=str(
                            setup.get(
                                "state",
                                "RSI_EXTREME_REVERSAL",
                            )
                        ),
                        global_overlay=round(
                            global_overlay,
                            4,
                        ),
                        exchange_overlay=round(
                            exchange_overlay,
                            4,
                        ),
                    )
                )
                continue

            scanner_strategies = {
                "scanner_top5_long",
                "scanner_bottom5_short",
                "scanner_top5_btc_strength",
                "global_confluence_pure",
            }
            benchmark_strategies = {
                "donchian_breakout",
                "bollinger_mean_reversion",
                "ema_trend_following",
            }
            combo_strategies = {
                "combo_trend",
                "combo_mean_reversion",
                "combo_scanner",
                "combo_adaptive",
            }
            if strategy in combo_strategies:
                accepted, score, reasons = combined_strategy_score(
                    strategy,
                    asset,
                    features,
                    scanner_ranking_by_asset,
                    global_rows,
                    exchange_rows,
                    portfolio,
                )
                if not accepted or abs(score) < minimum_score:
                    continue
                reasons = reasons + [
                    "conto shadow combinato",
                ]
            elif strategy in scanner_strategies:
                accepted, score, reasons = scanner_family_score(
                    strategy,
                    asset,
                    features,
                    scanner_ranking_by_asset,
                    global_rows,
                    exchange_rows,
                    portfolio,
                )
                if not accepted or abs(score) < minimum_score:
                    continue
                reasons = reasons + [
                    "ranking live KuCoin",
                ]
            elif strategy in benchmark_strategies:
                accepted, score, reasons = benchmark_strategy_score(
                    strategy,
                    features,
                )
                if not accepted or abs(score) < minimum_score:
                    continue
                reasons = reasons + [
                    global_reason + " (solo contesto, peso 0)",
                    exchange_reason + " (solo contesto, peso 0)",
                ]
            else:
                score, reasons = score_features(
                    features,
                    global_overlay,
                    exchange_overlay,
                )
                if abs(score) < minimum_score:
                    continue

            side = "LONG" if score > 0 else "SHORT"
            if (
                side == "LONG"
                and not portfolio.get("allow_long", True)
            ):
                continue
            if (
                side == "SHORT"
                and not portfolio.get("allow_short", True)
            ):
                continue
            if strategy == "relative_strength_v2":
                if not relative_strength_v2_accepts(
                    side,
                    features,
                    portfolio,
                    market_context,
                ):
                    continue
            elif not strategy_accepts(
                strategy,
                side,
                features,
                score,
            ):
                continue

            atr_pct = max(
                float(
                    config["risk"].get(
                        "minimum_stop_pct",
                        0.008,
                    )
                )
                * 100.0,
                features["atr_pct"],
            )
            stop_pct = (
                atr_pct
                / 100.0
                * float(
                    portfolio.get(
                        "atr_stop_multiple",
                        2.0,
                    )
                )
            )
            stop_pct = max(
                float(
                    config["risk"].get(
                        "minimum_stop_pct",
                        0.008,
                    )
                ),
                stop_pct,
            )
            stop_pct = min(
                float(
                    config["risk"].get(
                        "maximum_stop_pct",
                        0.12,
                    )
                ),
                stop_pct,
            )
            target_pct = stop_pct * float(
                portfolio.get("reward_risk", 2.0)
            )
            candle_time = features["candle_time"]
            if strategy == "relative_strength_v2":
                experiment_group = deterministic_id(
                    timeframe,
                    candle_time,
                    side,
                    "relative_strength_v2_market_episode",
                )
                signal_id = deterministic_id(
                    portfolio["name"],
                    strategy,
                    asset,
                    experiment_group,
                )
            else:
                experiment_group = deterministic_id(
                    asset,
                    timeframe,
                    candle_time,
                    side,
                    "market_event",
                )
                signal_id = deterministic_id(
                    portfolio["name"],
                    strategy,
                    experiment_group,
                )
            relative_blend = (
                0.65 * features["relative_medium_pct"]
                + 0.35 * features["relative_long_pct"]
            )
            if strategy in benchmark_strategies:
                reason = "; ".join(reasons)
                signal_global_overlay = 0.0
                signal_exchange_overlay = 0.0
            elif strategy in combo_strategies:
                reason = "; ".join(reasons)
                signal_global_overlay = 0.0
                signal_exchange_overlay = 0.0
            elif strategy in scanner_strategies:
                reason = "; ".join(reasons)
                signal_global_overlay = 0.0
                signal_exchange_overlay = 0.0
            else:
                reason = "; ".join(
                    reasons
                    + [global_reason, exchange_reason]
                )
                signal_global_overlay = global_overlay
                signal_exchange_overlay = exchange_overlay

            signals.append(
                Signal(
                    signal_id=signal_id,
                    experiment_group_id=experiment_group,
                    portfolio=str(portfolio["name"]),
                    is_main=bool(
                        portfolio.get("is_main")
                    ),
                    strategy=strategy,
                    asset=asset,
                    symbol=str(
                        payload.get("symbol", "")
                    ),
                    timeframe_minutes=timeframe,
                    candle_time=candle_time,
                    side=side,
                    score=round(score, 4),
                    confidence=confidence_from_score(
                        score
                    ),
                    entry_reference_price=float(
                        payload.get("mark_price")
                        or features["price"]
                    ),
                    atr_pct=round(
                        features["atr_pct"],
                        6,
                    ),
                    stop_pct=round(
                        stop_pct,
                        8,
                    ),
                    target_pct=round(
                        target_pct,
                        8,
                    ),
                    leverage=float(
                        portfolio.get(
                            "leverage",
                            config["risk"].get(
                                "default_leverage",
                                1.0,
                            ),
                        )
                    ),
                    max_holding_hours=int(
                        portfolio.get(
                            "max_holding_hours",
                            168,
                        )
                    ),
                    trailing_at_r=float(
                        portfolio.get(
                            "trailing_at_r",
                            0.0,
                        )
                    ),
                    trailing_atr_multiple=float(
                        portfolio.get(
                            "trailing_atr_multiple",
                            0.0,
                        )
                    ),
                    reason=reason,
                    relative_strength_score=round(
                        relative_blend,
                        4,
                    ),
                    breakout_state=str(
                        features["breakout_state"]
                    ),
                    global_overlay=round(
                        signal_global_overlay,
                        4,
                    ),
                    exchange_overlay=round(
                        signal_exchange_overlay,
                        4,
                    ),
                )
            )
    return apply_signal_caps(signals, config)
