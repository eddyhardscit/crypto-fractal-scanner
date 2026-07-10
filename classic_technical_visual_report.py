# -*- coding: utf-8 -*-
"""Create the diagnostic classic-technical visual report.

The module is intentionally diagnostic: it creates charts and lifecycle metadata,
but it does not add points directly to Global Confluence.

Pattern lifecycle:
- CANDIDATO
- ATTIVO
- CONFERMATO_RECENTE
- MATURO
- TARGET_RAGGIUNTO
- INVALIDATO

The lifecycle prevents old chart patterns from remaining "confirmed" forever.
"""

from __future__ import annotations

import csv
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import yfinance as yf

from shared_market_snapshot import (
    apply_snapshot_to_ohlcv,
    snapshot_record,
    snapshot_source_label,
)


REPORTS_DIR = Path("reports")
LATEST_REPORT_PATH = REPORTS_DIR / "latest_report.md"

REPORT_PATH = REPORTS_DIR / "classic_technical_visual_report.md"
METRICS_CSV_PATH = REPORTS_DIR / "classic_technical_visual_metrics.csv"
TECHNICAL_METRICS_CSV_PATH = REPORTS_DIR / "technical_structure_metrics.csv"

START_MARKER = "<!-- CLASSIC_TECHNICAL_VISUAL_START -->"
END_MARKER = "<!-- CLASSIC_TECHNICAL_VISUAL_END -->"

ASSETS = {
    "BTC": "BTC-USD",
    "SOL": "SOL-USD",
    "DOGE": "DOGE-USD",
}

ASSET_NAMES = {
    "BTC": "Bitcoin",
    "SOL": "Solana",
    "DOGE": "Dogecoin",
}

# Lifecycle aligned with technical_structure_report.py.
BREAKOUT_BUFFER_PCT = 0.50
INVALIDATION_BUFFER_PCT = 2.00
INVALIDATION_CONFIRM_DAYS = 2
ACTIVE_MAX_DAYS = 3
RECENT_MAX_DAYS = 14

PATTERN_STATUS_PRIORITY = {
    "ASSENTE": 0,
    "INVALIDATO": 1,
    "TARGET_RAGGIUNTO": 2,
    "CANDIDATO": 3,
    "MATURO": 4,
    "ATTIVO": 5,
    "CONFERMATO_RECENTE": 6,
}

STATUS_LABELS = {
    "ASSENTE": "ASSENTE",
    "CANDIDATO": "CANDIDATO",
    "ATTIVO": "ATTIVO",
    "CONFERMATO_RECENTE": "CONFERMATO RECENTE",
    "MATURO": "MATURO",
    "TARGET_RAGGIUNTO": "TARGET RAGGIUNTO",
    "INVALIDATO": "INVALIDATO",
}


# =========================
# Utility
# =========================


def now_utc_str() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")


def read_text(path: Path) -> str:
    if not path.exists():
        return ""
    try:
        return path.read_text(encoding="utf-8")
    except OSError:
        return ""


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def replace_or_insert_block(text: str, block: str) -> str:
    full_block = f"{START_MARKER}\n{block.rstrip()}\n{END_MARKER}"

    if START_MARKER in text and END_MARKER in text:
        pattern = re.compile(
            re.escape(START_MARKER) + r".*?" + re.escape(END_MARKER),
            flags=re.DOTALL,
        )
        return pattern.sub(full_block, text)

    classic_end = "<!-- CLASSIC_TECHNICAL_CONFIRMATION_END -->"
    if classic_end in text:
        return text.replace(classic_end, classic_end + "\n\n" + full_block, 1)

    global_start = "<!-- GLOBAL_CONFLUENCE_START -->"
    if global_start in text:
        return text.replace(global_start, full_block + "\n\n" + global_start, 1)

    tech_end = "<!-- TECHNICAL_STRUCTURE_END -->"
    if tech_end in text:
        return text.replace(tech_end, tech_end + "\n\n" + full_block, 1)

    return text.rstrip() + "\n\n" + full_block + "\n"


def safe_float(value: Any) -> float:
    try:
        if value is None or pd.isna(value):
            return np.nan
        return float(value)
    except (TypeError, ValueError):
        return np.nan


def safe_int(value: Any, default: int = 0) -> int:
    number = safe_float(value)
    if pd.isna(number):
        return default
    return int(number)


def safe_date_str(value: Any) -> str:
    if value is None or value == "":
        return ""
    try:
        return pd.Timestamp(value).strftime("%Y-%m-%d")
    except Exception:
        return str(value)


def status_label(value: Any) -> str:
    return STATUS_LABELS.get(str(value), str(value))


def fmt_signed(value: Any) -> str:
    if value is None or pd.isna(value):
        return "n/a"
    number = float(value)
    if number > 0:
        return f"+{number:.2f}".replace(".", ",")
    return f"{number:.2f}".replace(".", ",")


def fmt_signed_int(value: Any) -> str:
    number = safe_int(value, 0)
    return f"+{number}" if number > 0 else str(number)


def fmt_pct(value: Any, decimals: int = 2) -> str:
    if value is None or pd.isna(value):
        return "n/a"
    return f"{float(value):+.{decimals}f}%".replace(".", ",")


def fmt_pct_plain(value: Any, decimals: int = 2) -> str:
    if value is None or pd.isna(value):
        return "n/a"
    return f"{float(value):.{decimals}f}%".replace(".", ",")


def fmt_price(asset: str, value: Any) -> str:
    if value is None or pd.isna(value):
        return "n/a"

    number = float(value)

    if asset == "BTC":
        return f"{number:,.0f}".replace(",", ".")

    if asset == "DOGE":
        return f"{number:.5f}"

    text = f"{number:,.2f}"
    return text.replace(",", "X").replace(".", ",").replace("X", ".")


def fmt_money(asset: str, value: Any) -> str:
    price = fmt_price(asset, value)
    if price == "n/a":
        return "n/a"
    return f"{price} $"


def md_table(headers: list[str], rows: list[list[Any]]) -> str:
    out = ["| " + " | ".join(headers) + " |"]
    out.append("| " + " | ".join(["---"] * len(headers)) + " |")
    for row in rows:
        out.append("| " + " | ".join(str(x) for x in row) + " |")
    return "\n".join(out)


# =========================
# Dati e indicatori
# =========================


def normalize_yfinance_df(df: pd.DataFrame) -> pd.DataFrame:
    if df is None or df.empty:
        return pd.DataFrame()

    out = df.copy()

    if isinstance(out.columns, pd.MultiIndex):
        # Single-ticker download normally has fields on level 0. Keep a robust
        # fallback for the inverse arrangement.
        level0 = out.columns.get_level_values(0)
        level1 = out.columns.get_level_values(-1)
        fields = ["Open", "High", "Low", "Close", "Adj Close", "Volume"]

        if any(field in level0 for field in fields):
            extracted: dict[str, pd.Series] = {}
            for field in fields:
                if field in level0:
                    part = out.xs(field, axis=1, level=0)
                    extracted[field] = part.iloc[:, 0]
            out = pd.DataFrame(extracted)
        elif any(field in level1 for field in fields):
            extracted = {}
            for field in fields:
                if field in level1:
                    part = out.xs(field, axis=1, level=-1)
                    extracted[field] = part.iloc[:, 0]
            out = pd.DataFrame(extracted)
        else:
            return pd.DataFrame()

    rename: dict[Any, str] = {}
    for column in out.columns:
        label = str(column).lower().strip()
        if label == "open":
            rename[column] = "Open"
        elif label == "high":
            rename[column] = "High"
        elif label == "low":
            rename[column] = "Low"
        elif label == "close":
            rename[column] = "Close"
        elif label == "adj close":
            rename[column] = "Adj Close"
        elif label == "volume":
            rename[column] = "Volume"

    out = out.rename(columns=rename)

    required = ["Open", "High", "Low", "Close", "Volume"]
    for column in required:
        if column not in out.columns:
            return pd.DataFrame()

    out = out[required].copy()
    out.index = pd.to_datetime(out.index, errors="coerce")
    out = out[~out.index.isna()]

    try:
        if out.index.tz is not None:
            out.index = out.index.tz_convert(None)
    except Exception:
        pass

    out.index = out.index.normalize()
    out = out[~out.index.duplicated(keep="last")].sort_index()
    out = out.dropna(subset=["Open", "High", "Low", "Close"])
    out["Volume"] = out["Volume"].fillna(0)

    return out


def download_ohlcv(ticker: str, period: str = "900d", interval: str = "1d") -> pd.DataFrame:
    try:
        frame = yf.download(
            ticker,
            period=period,
            interval=interval,
            auto_adjust=False,
            progress=False,
            threads=False,
        )
        return normalize_yfinance_df(frame)
    except Exception as exc:
        print(f"Download fallito per {ticker}: {exc}")
        return pd.DataFrame()


def add_indicators(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return df

    out = df.copy()

    close = out["Close"]
    high = out["High"]
    low = out["Low"]
    volume = out["Volume"]

    out["MA20"] = close.rolling(20, min_periods=10).mean()
    out["MA50"] = close.rolling(50, min_periods=25).mean()
    out["MA100"] = close.rolling(100, min_periods=50).mean()
    out["MA200"] = close.rolling(200, min_periods=100).mean()

    delta = close.diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    avg_gain = gain.ewm(alpha=1 / 14, adjust=False, min_periods=14).mean()
    avg_loss = loss.ewm(alpha=1 / 14, adjust=False, min_periods=14).mean()
    rs = avg_gain / avg_loss.replace(0, np.nan)
    out["RSI14"] = (100 - (100 / (1 + rs))).fillna(50)

    out["VOL_MA20"] = volume.rolling(20, min_periods=10).mean()
    out["VOL_RATIO_20"] = volume / out["VOL_MA20"].replace(0, np.nan)

    out["EMA12"] = close.ewm(span=12, adjust=False).mean()
    out["EMA26"] = close.ewm(span=26, adjust=False).mean()
    out["MACD"] = out["EMA12"] - out["EMA26"]
    out["MACD_SIGNAL"] = out["MACD"].ewm(span=9, adjust=False).mean()
    out["MACD_HIST"] = out["MACD"] - out["MACD_SIGNAL"]

    tr1 = high - low
    tr2 = (high - close.shift(1)).abs()
    tr3 = (low - close.shift(1)).abs()
    true_range = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)
    out["ATR14"] = true_range.rolling(14, min_periods=7).mean()
    out["ATR14_PCT"] = out["ATR14"] / close * 100

    out["RET_30D"] = close.pct_change(30) * 100
    out["RET_90D"] = close.pct_change(90) * 100

    return out


# =========================
# Pivot e lifecycle pattern
# =========================


def find_pivots(df: pd.DataFrame, lookback: int = 220, pivot: int = 4):
    recent = df.tail(lookback).copy()

    highs: list[dict[str, Any]] = []
    lows: list[dict[str, Any]] = []

    if len(recent) < pivot * 2 + 10:
        return highs, lows

    for i in range(pivot, len(recent) - pivot):
        window = recent.iloc[i - pivot : i + pivot + 1]
        row = recent.iloc[i]
        date = pd.Timestamp(recent.index[i])

        if row["High"] >= window["High"].max():
            highs.append(
                {
                    "date": date,
                    "price": float(row["High"]),
                    "kind": "HIGH",
                    "i": int(df.index.get_loc(date)),
                }
            )

        if row["Low"] <= window["Low"].min():
            lows.append(
                {
                    "date": date,
                    "price": float(row["Low"]),
                    "kind": "LOW",
                    "i": int(df.index.get_loc(date)),
                }
            )

    return highs, lows


def tolerance_for_asset(asset: str) -> float:
    if asset == "BTC":
        return 0.035
    if asset == "SOL":
        return 0.055
    if asset == "DOGE":
        return 0.075
    return 0.05


def pct_diff(a: Any, b: Any) -> float:
    a = safe_float(a)
    b = safe_float(b)
    if pd.isna(a) or pd.isna(b):
        return np.nan
    denom = max(abs(a), abs(b), 1e-12)
    return abs(a - b) / denom


def find_between_pivots(pivots, i1: int, i2: int, kind: str | None = None):
    out = []
    for point in pivots:
        if i1 < point["i"] < i2:
            if kind is None or point["kind"] == kind:
                out.append(point)
    return out


def direction_from_family(family: str) -> str:
    if family == "rialzista":
        return "BULLISH"
    if family == "ribassista":
        return "BEARISH"
    return "NEUTRAL"


def theoretical_target(direction: str, neckline: Any, anchor: Any) -> float:
    neckline = safe_float(neckline)
    anchor = safe_float(anchor)

    if pd.isna(neckline) or pd.isna(anchor):
        return np.nan

    if direction == "BULLISH":
        height = max(0.0, neckline - anchor)
        return neckline + height

    if direction == "BEARISH":
        height = max(0.0, anchor - neckline)
        return max(neckline - height, neckline * 0.05)

    return np.nan


def target_progress(direction: str, close: Any, neckline: Any, target: Any) -> float:
    close = safe_float(close)
    neckline = safe_float(neckline)
    target = safe_float(target)

    if pd.isna(close) or pd.isna(neckline) or pd.isna(target):
        return np.nan

    if direction == "BULLISH":
        distance = target - neckline
        if distance <= 0:
            return np.nan
        return (close - neckline) / distance * 100

    if direction == "BEARISH":
        distance = neckline - target
        if distance <= 0:
            return np.nan
        return (neckline - close) / distance * 100

    return np.nan


def distance_to_neckline(direction: str, close: Any, neckline: Any) -> float:
    close = safe_float(close)
    neckline = safe_float(neckline)
    if pd.isna(close) or pd.isna(neckline) or close == 0 or neckline == 0:
        return np.nan
    if direction == "BULLISH":
        return (neckline / close - 1.0) * 100.0
    if direction == "BEARISH":
        return (close / neckline - 1.0) * 100.0
    return np.nan


def current_relation_to_neckline(close: Any, neckline: Any) -> str:
    close = safe_float(close)
    neckline = safe_float(neckline)

    if pd.isna(close) or pd.isna(neckline) or neckline == 0:
        return "n/a"

    distance_pct = (close / neckline - 1) * 100
    if abs(distance_pct) <= 1.0:
        return "vicino alla neckline"
    if distance_pct > 0:
        return "sopra neckline"
    return "sotto neckline"


def first_breakout_date(
    df: pd.DataFrame,
    pattern_end: Any,
    direction: str,
    neckline: Any,
) -> pd.Timestamp | None:
    neckline = safe_float(neckline)
    if pd.isna(neckline) or direction not in {"BULLISH", "BEARISH"}:
        return None

    start = pd.Timestamp(pattern_end)
    after = df[df.index >= start]
    if after.empty:
        return None

    if direction == "BULLISH":
        threshold = neckline * (1 + BREAKOUT_BUFFER_PCT / 100)
        hits = after[after["Close"] > threshold]
    else:
        threshold = neckline * (1 - BREAKOUT_BUFFER_PCT / 100)
        hits = after[after["Close"] < threshold]

    if hits.empty:
        return None

    return pd.Timestamp(hits.index[0])


def has_consecutive_true(series: pd.Series, count: int) -> bool:
    if series is None or len(series) < count:
        return False
    values = pd.Series(series).fillna(False).astype(bool)
    runs = values.astype(int).rolling(count).sum()
    return bool((runs >= count).any())


def make_candidate_pattern(
    *,
    name: str,
    family: str,
    neckline: Any,
    anchor: Any,
    points: list[dict[str, Any]],
    extra_points: list[dict[str, Any]],
    detail: str,
    geometry_rank: float,
) -> dict[str, Any]:
    direction = direction_from_family(family)
    start_date = min((point["date"] for point in points), default=None)
    end_date = max((point["date"] for point in points), default=None)

    return {
        "name": name,
        "family": family,
        "direction": direction,
        "state": "CANDIDATO",
        "score": 0,
        "neckline": safe_float(neckline),
        "anchor": safe_float(anchor),
        "target": theoretical_target(direction, neckline, anchor),
        "invalidation_level": np.nan,
        "target_progress_pct": np.nan,
        "distance_to_neckline_pct": np.nan,
        "current_relation": "n/a",
        "start_date": safe_date_str(start_date),
        "end_date": safe_date_str(end_date),
        "formation_age_days": np.nan,
        "breakout_date": "",
        "breakout_age_days": np.nan,
        "target_reached": False,
        "invalidated": False,
        "confidence": "LOW/MEDIUM",
        "points": points,
        "extra_points": extra_points,
        "detail": detail,
        "geometry_rank": float(geometry_rank),
    }


def apply_pattern_lifecycle(
    df: pd.DataFrame,
    asset: str,
    pattern: dict[str, Any],
) -> dict[str, Any]:
    result = dict(pattern)
    direction = result.get("direction", "NEUTRAL")
    neckline = safe_float(result.get("neckline"))
    anchor = safe_float(result.get("anchor"))
    close = safe_float(df["Close"].iloc[-1])
    last_date = pd.Timestamp(df.index[-1])

    end_date_raw = result.get("end_date")
    if not end_date_raw:
        result["state"] = "CANDIDATO"
        result["score"] = 0
        return result

    end_date = pd.Timestamp(end_date_raw)
    formation_age = max(0, (last_date - end_date).days)
    target = theoretical_target(direction, neckline, anchor)

    result["formation_age_days"] = formation_age
    result["target"] = target
    result["target_progress_pct"] = np.nan
    result["distance_to_neckline_pct"] = distance_to_neckline(direction, close, neckline)
    result["current_relation"] = current_relation_to_neckline(close, neckline)

    if direction not in {"BULLISH", "BEARISH"} or pd.isna(neckline):
        result["state"] = "CANDIDATO"
        result["score"] = 0
        result["confidence"] = "LOW/MEDIUM"
        result["detail"] = (
            f"{result['detail']} Stato: CANDIDATO; il pattern non ha una neckline "
            "univoca da usare per il lifecycle."
        )
        return result

    invalidation_level = (
        neckline * (1 - INVALIDATION_BUFFER_PCT / 100)
        if direction == "BULLISH"
        else neckline * (1 + INVALIDATION_BUFFER_PCT / 100)
    )
    result["invalidation_level"] = invalidation_level

    breakout_date = first_breakout_date(df, end_date, direction, neckline)

    if breakout_date is None:
        result["state"] = "CANDIDATO"
        result["score"] = 0
        result["confidence"] = "LOW/MEDIUM"
        result["detail"] = (
            f"{result['detail']} Stato: CANDIDATO; la neckline non è ancora stata "
            f"rotta con un margine di almeno {BREAKOUT_BUFFER_PCT:.2f}%. "
            f"Età formazione: {formation_age} giorni."
        )
        return result

    breakout_age = max(0, (last_date - breakout_date).days)
    post_breakout = df[df.index >= breakout_date]

    if direction == "BULLISH":
        target_reached = bool((post_breakout["High"] >= target).any()) if not pd.isna(target) else False
        invalid_flags = post_breakout["Close"] < invalidation_level
    else:
        target_reached = bool((post_breakout["Low"] <= target).any()) if not pd.isna(target) else False
        invalid_flags = post_breakout["Close"] > invalidation_level

    invalidated = has_consecutive_true(invalid_flags, INVALIDATION_CONFIRM_DAYS)

    if target_reached:
        state = "TARGET_RAGGIUNTO"
        score = 0
        confidence = "COMPLETATO"
    elif invalidated:
        state = "INVALIDATO"
        score = 0
        confidence = "ANNULLATO"
    elif breakout_age <= ACTIVE_MAX_DAYS:
        state = "ATTIVO"
        score = 1 if direction == "BULLISH" else -1
        confidence = "MEDIUM"
    elif breakout_age <= RECENT_MAX_DAYS:
        state = "CONFERMATO_RECENTE"
        score = 2 if direction == "BULLISH" else -2
        confidence = "MEDIUM/HIGH"
    else:
        state = "MATURO"
        score = 1 if direction == "BULLISH" else -1
        confidence = "MEDIUM/DECAY"

    result["target_progress_pct"] = target_progress(direction, close, neckline, target)

    result.update(
        {
            "state": state,
            "score": score,
            "confidence": confidence,
            "breakout_date": safe_date_str(breakout_date),
            "breakout_age_days": breakout_age,
            "target_reached": target_reached,
            "invalidated": invalidated,
            "detail": (
                f"{result['detail']} Breakout neckline: {safe_date_str(breakout_date)} "
                f"({breakout_age} giorni fa). Stato: {status_label(state)}. "
                f"Target teorico: {fmt_money(asset, target)}; progresso: "
                f"{fmt_pct_plain(result['target_progress_pct'])}; prezzo "
                f"{result['current_relation']}."
            ),
        }
    )

    return result


def pattern_sort_key(pattern: dict[str, Any]):
    priority = PATTERN_STATUS_PRIORITY.get(pattern.get("state", "ASSENTE"), 0)
    strength = abs(safe_int(pattern.get("score"), 0))

    date_value = pattern.get("breakout_date") or pattern.get("end_date") or ""
    try:
        recency = pd.Timestamp(date_value).value
    except Exception:
        recency = 0

    geometry = safe_float(pattern.get("geometry_rank"))
    if pd.isna(geometry):
        geometry = 0.0

    return priority, strength, recency, geometry


# =========================
# Riconoscimento pattern
# =========================


def detect_double_bottom(df: pd.DataFrame, highs, lows, asset: str):
    tolerance = tolerance_for_asset(asset)
    candidates = []
    last_lows = lows[-8:]
    last_index = len(df) - 1

    for a in range(len(last_lows)):
        for b in range(a + 1, len(last_lows)):
            p1 = last_lows[a]
            p2 = last_lows[b]

            separation = p2["i"] - p1["i"]
            if separation < 10:
                continue
            if pct_diff(p1["price"], p2["price"]) > tolerance:
                continue

            between_highs = find_between_pivots(highs, p1["i"], p2["i"], "HIGH")
            if not between_highs:
                continue

            neckline = max(point["price"] for point in between_highs)
            anchor = min(p1["price"], p2["price"])
            recency_bonus = max(0, 90 - (last_index - p2["i"])) / 10
            geometry_rank = 100 - pct_diff(p1["price"], p2["price"]) * 100 + recency_bonus

            detail = (
                f"Due minimi simili a {fmt_money(asset, p1['price'])} e "
                f"{fmt_money(asset, p2['price'])}. Neckline circa "
                f"{fmt_money(asset, neckline)}."
            )

            pattern = make_candidate_pattern(
                name="Doppio minimo",
                family="rialzista",
                neckline=neckline,
                anchor=anchor,
                points=[p1, p2],
                extra_points=between_highs,
                detail=detail,
                geometry_rank=geometry_rank,
            )
            candidates.append(apply_pattern_lifecycle(df, asset, pattern))

    return max(candidates, key=pattern_sort_key) if candidates else None


def detect_double_top(df: pd.DataFrame, highs, lows, asset: str):
    tolerance = tolerance_for_asset(asset)
    candidates = []
    last_highs = highs[-8:]
    last_index = len(df) - 1

    for a in range(len(last_highs)):
        for b in range(a + 1, len(last_highs)):
            p1 = last_highs[a]
            p2 = last_highs[b]

            separation = p2["i"] - p1["i"]
            if separation < 10:
                continue
            if pct_diff(p1["price"], p2["price"]) > tolerance:
                continue

            between_lows = find_between_pivots(lows, p1["i"], p2["i"], "LOW")
            if not between_lows:
                continue

            neckline = min(point["price"] for point in between_lows)
            anchor = max(p1["price"], p2["price"])
            recency_bonus = max(0, 90 - (last_index - p2["i"])) / 10
            geometry_rank = 100 - pct_diff(p1["price"], p2["price"]) * 100 + recency_bonus

            detail = (
                f"Due massimi simili a {fmt_money(asset, p1['price'])} e "
                f"{fmt_money(asset, p2['price'])}. Neckline circa "
                f"{fmt_money(asset, neckline)}."
            )

            pattern = make_candidate_pattern(
                name="Doppio massimo",
                family="ribassista",
                neckline=neckline,
                anchor=anchor,
                points=[p1, p2],
                extra_points=between_lows,
                detail=detail,
                geometry_rank=geometry_rank,
            )
            candidates.append(apply_pattern_lifecycle(df, asset, pattern))

    return max(candidates, key=pattern_sort_key) if candidates else None


def detect_head_shoulders(df: pd.DataFrame, highs, lows, asset: str):
    tolerance = tolerance_for_asset(asset)
    candidates = []
    last_highs = highs[-8:]
    last_index = len(df) - 1

    for i in range(len(last_highs) - 2):
        left = last_highs[i]
        head = last_highs[i + 1]
        right = last_highs[i + 2]

        if not (head["price"] > left["price"] and head["price"] > right["price"]):
            continue

        shoulders_close = pct_diff(left["price"], right["price"]) <= tolerance * 1.5
        head_higher_enough = head["price"] > max(left["price"], right["price"]) * 1.03
        if not shoulders_close or not head_higher_enough:
            continue

        lows_left_head = find_between_pivots(lows, left["i"], head["i"], "LOW")
        lows_head_right = find_between_pivots(lows, head["i"], right["i"], "LOW")
        if not lows_left_head or not lows_head_right:
            continue

        neckline = (
            min(point["price"] for point in lows_left_head)
            + min(point["price"] for point in lows_head_right)
        ) / 2
        anchor = head["price"]
        shoulder_similarity = pct_diff(left["price"], right["price"])
        recency_bonus = max(0, 100 - (last_index - right["i"])) / 10
        geometry_rank = 120 - shoulder_similarity * 100 + recency_bonus

        detail = (
            f"Spalla sinistra {fmt_money(asset, left['price'])}, testa "
            f"{fmt_money(asset, head['price'])}, spalla destra "
            f"{fmt_money(asset, right['price'])}. Neckline circa "
            f"{fmt_money(asset, neckline)}."
        )

        pattern = make_candidate_pattern(
            name="Testa e spalle",
            family="ribassista",
            neckline=neckline,
            anchor=anchor,
            points=[left, head, right],
            extra_points=lows_left_head + lows_head_right,
            detail=detail,
            geometry_rank=geometry_rank,
        )
        candidates.append(apply_pattern_lifecycle(df, asset, pattern))

    return max(candidates, key=pattern_sort_key) if candidates else None


def detect_inverse_head_shoulders(df: pd.DataFrame, highs, lows, asset: str):
    tolerance = tolerance_for_asset(asset)
    candidates = []
    last_lows = lows[-8:]
    last_index = len(df) - 1

    for i in range(len(last_lows) - 2):
        left = last_lows[i]
        head = last_lows[i + 1]
        right = last_lows[i + 2]

        if not (head["price"] < left["price"] and head["price"] < right["price"]):
            continue

        shoulders_close = pct_diff(left["price"], right["price"]) <= tolerance * 1.5
        head_lower_enough = head["price"] < min(left["price"], right["price"]) * 0.97
        if not shoulders_close or not head_lower_enough:
            continue

        highs_left_head = find_between_pivots(highs, left["i"], head["i"], "HIGH")
        highs_head_right = find_between_pivots(highs, head["i"], right["i"], "HIGH")
        if not highs_left_head or not highs_head_right:
            continue

        neckline = (
            max(point["price"] for point in highs_left_head)
            + max(point["price"] for point in highs_head_right)
        ) / 2
        anchor = head["price"]
        shoulder_similarity = pct_diff(left["price"], right["price"])
        recency_bonus = max(0, 100 - (last_index - right["i"])) / 10
        geometry_rank = 120 - shoulder_similarity * 100 + recency_bonus

        detail = (
            f"Spalla sinistra {fmt_money(asset, left['price'])}, testa "
            f"{fmt_money(asset, head['price'])}, spalla destra "
            f"{fmt_money(asset, right['price'])}. Neckline circa "
            f"{fmt_money(asset, neckline)}."
        )

        pattern = make_candidate_pattern(
            name="Testa e spalle inverso",
            family="rialzista",
            neckline=neckline,
            anchor=anchor,
            points=[left, head, right],
            extra_points=highs_left_head + highs_head_right,
            detail=detail,
            geometry_rank=geometry_rank,
        )
        candidates.append(apply_pattern_lifecycle(df, asset, pattern))

    return max(candidates, key=pattern_sort_key) if candidates else None


def detect_triangle_compression(df: pd.DataFrame, highs, lows, asset: str):
    if len(highs) < 3 or len(lows) < 3:
        return None

    high_points = highs[-3:]
    low_points = lows[-3:]

    highs_descending = high_points[-1]["price"] < high_points[-2]["price"] < high_points[-3]["price"]
    lows_ascending = low_points[-1]["price"] > low_points[-2]["price"] > low_points[-3]["price"]

    highs_flat = pct_diff(high_points[-1]["price"], high_points[-2]["price"]) < tolerance_for_asset(asset)
    lows_flat = pct_diff(low_points[-1]["price"], low_points[-2]["price"]) < tolerance_for_asset(asset)

    if highs_descending and lows_ascending:
        name = "Triangolo simmetrico / compressione"
        family = "neutrale"
        detail = "Massimi decrescenti e minimi crescenti: compressione in corso."
    elif highs_flat and lows_ascending:
        name = "Triangolo ascendente possibile"
        family = "rialzista"
        detail = "Resistenza quasi piatta e minimi crescenti."
    elif highs_descending and lows_flat:
        name = "Triangolo discendente possibile"
        family = "ribassista"
        detail = "Massimi decrescenti e supporto quasi piatto."
    else:
        return None

    points = high_points + low_points
    pattern = make_candidate_pattern(
        name=name,
        family=family,
        neckline=np.nan,
        anchor=np.nan,
        points=points,
        extra_points=[],
        detail=detail,
        geometry_rank=30.0,
    )
    return apply_pattern_lifecycle(df, asset, pattern)


def detect_latest_candle(df: pd.DataFrame):
    if len(df) < 3:
        return "n/a", 0

    prev = df.iloc[-2]
    last = df.iloc[-1]

    o1, c1 = float(prev["Open"]), float(prev["Close"])
    o2, c2 = float(last["Open"]), float(last["Close"])
    h2, l2 = float(last["High"]), float(last["Low"])

    body = abs(c2 - o2)
    candle_range = max(h2 - l2, 1e-12)
    upper_wick = h2 - max(o2, c2)
    lower_wick = min(o2, c2) - l2

    bullish_engulfing = c1 < o1 and c2 > o2 and c2 > o1 and o2 < c1
    bearish_engulfing = c1 > o1 and c2 < o2 and c2 < o1 and o2 > c1

    hammer = lower_wick > body * 2 and upper_wick < body * 1.2 and c2 > o2
    shooting_star = upper_wick > body * 2 and lower_wick < body * 1.2 and c2 < o2
    doji = body / candle_range < 0.12

    if bullish_engulfing:
        return "Bullish engulfing", 1
    if hammer:
        return "Hammer / rejection basso", 1
    if bearish_engulfing:
        return "Bearish engulfing", -1
    if shooting_star:
        return "Shooting star / rejection alto", -1
    if doji:
        return "Doji / indecisione", 0

    return "Nessuna candela forte", 0


def detect_all_patterns(df: pd.DataFrame, asset: str):
    highs, lows = find_pivots(df, lookback=220, pivot=4)

    patterns = []
    for detector in [
        detect_double_bottom,
        detect_double_top,
        detect_head_shoulders,
        detect_inverse_head_shoulders,
        detect_triangle_compression,
    ]:
        try:
            pattern = detector(df, highs, lows, asset)
            if pattern:
                patterns.append(pattern)
        except Exception as exc:
            print(f"Pattern detector {detector.__name__} fallito per {asset}: {exc}")

    candle, candle_score = detect_latest_candle(df)

    if patterns:
        patterns.sort(key=pattern_sort_key, reverse=True)
        primary = patterns[0]
    else:
        primary = {
            "name": "Nessun pattern classico pulito",
            "family": "neutrale",
            "direction": "NEUTRAL",
            "state": "ASSENTE",
            "score": 0,
            "neckline": np.nan,
            "anchor": np.nan,
            "target": np.nan,
            "invalidation_level": np.nan,
            "target_progress_pct": np.nan,
            "current_relation": "n/a",
            "start_date": "",
            "end_date": "",
            "formation_age_days": np.nan,
            "breakout_date": "",
            "breakout_age_days": np.nan,
            "target_reached": False,
            "invalidated": False,
            "confidence": "LOW",
            "points": [],
            "extra_points": [],
            "detail": "Non è stato trovato un pattern classico abbastanza pulito nel lookback usato.",
            "geometry_rank": 0.0,
        }

    return {
        "highs": highs,
        "lows": lows,
        "patterns": patterns,
        "primary": primary,
        "candle": candle,
        "candle_score": candle_score,
    }


# =========================
# Sorgente tecnica autorevole / Fibonacci
# =========================


def read_technical_metrics_row(asset: str) -> dict[str, Any]:
    if not TECHNICAL_METRICS_CSV_PATH.exists():
        return {}
    try:
        with TECHNICAL_METRICS_CSV_PATH.open("r", encoding="utf-8", newline="") as handle:
            for row in csv.DictReader(handle):
                if str(row.get("asset", "")).strip().upper() == asset.upper():
                    return dict(row)
    except Exception:
        return {}
    return {}


def technical_pattern_prefix(name: Any) -> str:
    text = str(name or "").strip().lower()
    if "doppio minimo" in text:
        return "double_bottom"
    if "triplo minimo" in text:
        return "triple_bottom"
    if "bottom" in text:
        return "adam_eve_bottom"
    if "doppio massimo" in text:
        return "double_top"
    if "triplo massimo" in text:
        return "triple_top"
    if "top" in text:
        return "adam_eve_top"
    return ""


def technical_authoritative_primary(asset: str) -> tuple[dict[str, Any] | None, dict[str, Any]]:
    row = read_technical_metrics_row(asset)
    if not row:
        return None, {}

    candidates = []
    for family, direction, name_key, status_key, score_key in [
        ("rialzista", "BULLISH", "dominant_bullish_pattern", "dominant_bullish_status", "dominant_bullish_score"),
        ("ribassista", "BEARISH", "dominant_bearish_pattern", "dominant_bearish_status", "dominant_bearish_score"),
    ]:
        name = str(row.get(name_key, "")).strip()
        if not name:
            continue
        prefix = technical_pattern_prefix(name)
        if not prefix:
            continue
        status = str(row.get(status_key, "ASSENTE")).strip() or "ASSENTE"
        pattern = {
            "name": name,
            "family": family,
            "direction": direction,
            "state": status,
            "score": safe_int(row.get(score_key), 0),
            "neckline": safe_float(row.get(f"{prefix}_neckline")),
            "anchor": safe_float(row.get(f"{prefix}_anchor")),
            "target": safe_float(row.get(f"{prefix}_target")),
            "invalidation_level": safe_float(row.get(f"{prefix}_invalidation_level")),
            "target_progress_pct": safe_float(row.get(f"{prefix}_target_progress_pct")),
            "distance_to_neckline_pct": safe_float(row.get(f"{prefix}_distance_to_neckline_pct")),
            "current_relation": str(row.get(f"{prefix}_current_relation", "")).replace("ABOVE_NECKLINE", "sopra neckline").replace("BELOW_NECKLINE", "sotto neckline").replace("NEAR_NECKLINE", "vicino alla neckline"),
            "start_date": str(row.get(f"{prefix}_start_date", "")),
            "end_date": str(row.get(f"{prefix}_end_date", "")),
            "formation_age_days": safe_float(row.get(f"{prefix}_formation_age_days")),
            "breakout_date": str(row.get(f"{prefix}_breakout_date", "")),
            "breakout_age_days": safe_float(row.get(f"{prefix}_breakout_age_days")),
            "target_reached": str(row.get(f"{prefix}_target_reached", "")).lower() in {"true", "1", "yes"},
            "invalidated": str(row.get(f"{prefix}_invalidated", "")).lower() in {"true", "1", "yes"},
            "confidence": "TECHNICAL STRUCTURE",
            "points": [],
            "extra_points": [],
            "detail": str(row.get(f"{prefix}_details", "")) + " Fonte lifecycle: technical_structure_metrics.csv.",
            "geometry_rank": 0.0,
            "source": "technical_structure_metrics.csv",
        }
        candidates.append(pattern)

    primary = max(candidates, key=pattern_sort_key) if candidates else None
    return primary, row


def fib_from_technical_row(row: dict[str, Any]) -> dict[str, Any]:
    if not row:
        return {}
    out = {
        "direction": str(row.get("fib_direction", "")),
        "state": str(row.get("fib_state", "NON_ATTIVO")),
        "score": safe_int(row.get("fib_score"), 0),
        "nearest_ratio": safe_float(row.get("fib_nearest_ratio")),
        "nearest_level": safe_float(row.get("fib_nearest_level")),
        "confluence": str(row.get("fib_confluence", "")),
        "details": str(row.get("fib_details", "")),
        "start_date": str(row.get("fib_start_date", "")),
        "end_date": str(row.get("fib_end_date", "")),
        "start_price": safe_float(row.get("fib_start_price")),
        "end_price": safe_float(row.get("fib_end_price")),
    }
    for key in ("fib_236", "fib_382", "fib_500", "fib_618", "fib_786", "fib_ext_1272", "fib_ext_1618"):
        out[key] = safe_float(row.get(key))
    return out


# =========================
# Supporti/resistenze
# =========================


def support_resistance_levels(df: pd.DataFrame, highs, lows):
    close = float(df["Close"].iloc[-1])

    low_prices = [point["price"] for point in lows if point["price"] < close]
    high_prices = [point["price"] for point in highs if point["price"] > close]

    support = max(low_prices) if low_prices else float(df["Low"].tail(80).min())
    resistance = min(high_prices) if high_prices else float(df["High"].tail(80).max())

    recent = df.iloc[-65:-3] if len(df) >= 80 else df.tail(60)
    breakout_level = float(recent["High"].max()) if not recent.empty else np.nan
    breakdown_level = float(recent["Low"].min()) if not recent.empty else np.nan

    return {
        "support": support,
        "resistance": resistance,
        "breakout_level": breakout_level,
        "breakdown_level": breakdown_level,
    }


# =========================
# Grafici
# =========================


def plot_asset(asset: str, df: pd.DataFrame, detection: dict, levels: dict, fib: dict | None = None) -> Path:
    plot_df = df.tail(180).copy()
    image_path = REPORTS_DIR / f"classic_visual_{asset}.png"

    fig, axes = plt.subplots(
        3,
        1,
        figsize=(14, 10),
        sharex=True,
        gridspec_kw={"height_ratios": [4, 1.3, 1.2]},
    )

    ax = axes[0]
    ax_rsi = axes[1]
    ax_vol = axes[2]

    ax.plot(plot_df.index, plot_df["Close"], label="Close", linewidth=1.8)
    ax.plot(plot_df.index, plot_df["MA20"], label="MA20", linewidth=1.0)
    ax.plot(plot_df.index, plot_df["MA50"], label="MA50", linewidth=1.0)
    ax.plot(plot_df.index, plot_df["MA200"], label="MA200", linewidth=1.2)

    support = levels["support"]
    resistance = levels["resistance"]
    breakout_level = levels["breakout_level"]
    breakdown_level = levels["breakdown_level"]

    ax.axhline(support, linestyle="--", linewidth=1.0, label="Supporto")
    ax.axhline(resistance, linestyle="--", linewidth=1.0, label="Resistenza")
    ax.axhline(breakout_level, linestyle=":", linewidth=1.0, label="Breakout 60g")
    ax.axhline(breakdown_level, linestyle=":", linewidth=1.0, label="Breakdown 60g")

    plot_start = plot_df.index[0]
    highs = [point for point in detection["highs"] if point["date"] >= plot_start]
    lows = [point for point in detection["lows"] if point["date"] >= plot_start]

    if highs:
        ax.scatter(
            [point["date"] for point in highs],
            [point["price"] for point in highs],
            marker="v",
            s=40,
            label="Pivot high",
            zorder=5,
        )

    if lows:
        ax.scatter(
            [point["date"] for point in lows],
            [point["price"] for point in lows],
            marker="^",
            s=40,
            label="Pivot low",
            zorder=5,
        )

    primary = detection["primary"]
    pattern_points = [
        point for point in primary.get("points", []) if point["date"] >= plot_start
    ]

    if pattern_points:
        ax.plot(
            [point["date"] for point in pattern_points],
            [point["price"] for point in pattern_points],
            linewidth=2.4,
            marker="o",
            label=f"Pattern: {primary['name']}",
            zorder=6,
        )

        for point in pattern_points:
            ax.annotate(
                point["kind"],
                xy=(point["date"], point["price"]),
                xytext=(0, 10),
                textcoords="offset points",
                ha="center",
                fontsize=8,
            )

    neckline = safe_float(primary.get("neckline"))
    if not pd.isna(neckline):
        ax.axhline(neckline, linewidth=1.6, linestyle="-.", label="Neckline pattern")

    target = safe_float(primary.get("target"))
    if not pd.isna(target):
        ax.axhline(target, linewidth=1.3, linestyle="--", label="Target teorico")

    invalidation = safe_float(primary.get("invalidation_level"))
    if not pd.isna(invalidation):
        ax.axhline(invalidation, linewidth=1.0, linestyle=":", label="Invalidazione pattern")

    breakout_date = primary.get("breakout_date")
    if breakout_date:
        breakout_ts = pd.Timestamp(breakout_date)
        if breakout_ts >= plot_start:
            ax.axvline(breakout_ts, linewidth=1.0, linestyle="-.", label="Breakout pattern")

    fib = fib or {}
    for key, label in [
        ("fib_236", "Fib 23,6%"),
        ("fib_382", "Fib 38,2%"),
        ("fib_500", "Fib 50%"),
        ("fib_618", "Fib 61,8%"),
        ("fib_786", "Fib 78,6%"),
    ]:
        value = safe_float(fib.get(key))
        if not pd.isna(value):
            linewidth = 1.4 if key in {"fib_382", "fib_500", "fib_618"} else 0.8
            ax.axhline(value, linewidth=linewidth, linestyle="--", alpha=0.55, label=label)

    title = (
        f"{asset} — {primary['name']} ({status_label(primary['state'])}) | "
        f"Close {fmt_money(asset, plot_df['Close'].iloc[-1])}"
    )

    ax.set_title(title)
    ax.set_ylabel("Prezzo")
    ax.grid(True, alpha=0.25)
    ax.legend(loc="upper left", fontsize=8, ncol=3)

    ax_rsi.plot(plot_df.index, plot_df["RSI14"], label="RSI14", linewidth=1.4)
    ax_rsi.axhline(70, linestyle="--", linewidth=0.9)
    ax_rsi.axhline(50, linestyle=":", linewidth=0.9)
    ax_rsi.axhline(30, linestyle="--", linewidth=0.9)
    ax_rsi.set_ylabel("RSI")
    ax_rsi.set_ylim(0, 100)
    ax_rsi.grid(True, alpha=0.25)
    ax_rsi.legend(loc="upper left", fontsize=8)

    ax_vol.bar(plot_df.index, plot_df["Volume"], label="Volume", width=1.0)
    ax_vol.plot(plot_df.index, plot_df["VOL_MA20"], label="Volume MA20", linewidth=1.2)
    ax_vol.set_ylabel("Volume")
    ax_vol.grid(True, alpha=0.25)
    ax_vol.legend(loc="upper left", fontsize=8)

    plt.tight_layout()
    fig.savefig(image_path, dpi=160, bbox_inches="tight")
    plt.close(fig)

    return image_path


# =========================
# Analisi asset
# =========================


def analyze_asset(asset: str, ticker: str):
    df = download_ohlcv(ticker)
    df = apply_snapshot_to_ohlcv(df, ticker)

    if df.empty or len(df) < 260:
        return {
            "asset": asset,
            "ticker": ticker,
            "ok": False,
            "error": "Dati insufficienti da Yahoo Finance.",
        }

    df = add_indicators(df)
    df = df.dropna(subset=["Close"])

    detection = detect_all_patterns(df, asset)
    authoritative_primary, technical_row = technical_authoritative_primary(asset)
    if authoritative_primary is not None:
        detection["primary"] = authoritative_primary
        # Keep the authoritative lifecycle visible in the table even when the
        # visual detector found a different geometric variant.
        if not any(
            p.get("name") == authoritative_primary.get("name")
            and p.get("state") == authoritative_primary.get("state")
            for p in detection["patterns"]
        ):
            detection["patterns"].insert(0, authoritative_primary)

    fib = fib_from_technical_row(technical_row)
    levels = support_resistance_levels(df, detection["highs"], detection["lows"])
    image_path = plot_asset(asset, df, detection, levels, fib)

    last = df.iloc[-1]
    primary = detection["primary"]

    close = float(last["Close"])
    atr_pct = safe_float(last.get("ATR14_PCT"))
    rsi_value = safe_float(last.get("RSI14"))
    vol_ratio = safe_float(last.get("VOL_RATIO_20"))
    ret_30d = safe_float(last.get("RET_30D"))
    ret_90d = safe_float(last.get("RET_90D"))

    breakout = (
        close > levels["breakout_level"] * 1.005
        if not pd.isna(levels["breakout_level"])
        else False
    )
    breakdown = (
        close < levels["breakdown_level"] * 0.995
        if not pd.isna(levels["breakdown_level"])
        else False
    )

    if breakout:
        price_state = "BREAKOUT 60G"
    elif breakdown:
        price_state = "BREAKDOWN 60G"
    else:
        price_state = "NEL RANGE"

    return {
        "asset": asset,
        "ticker": ticker,
        "ok": True,
        "date": df.index[-1].strftime("%Y-%m-%d"),
        "price": close,
        "price_source": snapshot_source_label(ticker),
        "snapshot_candle_date": snapshot_record(ticker).get("candle_date_utc", ""),
        "image": image_path.name,
        "primary_pattern": primary["name"],
        "pattern_family": primary["family"],
        "pattern_direction": primary.get("direction", "NEUTRAL"),
        "pattern_state": primary["state"],
        "pattern_score": primary["score"],
        "pattern_confidence": primary.get("confidence", ""),
        "pattern_neckline": primary.get("neckline"),
        "pattern_anchor": primary.get("anchor"),
        "pattern_target": primary.get("target"),
        "pattern_target_progress_pct": primary.get("target_progress_pct"),
        "pattern_distance_to_neckline_pct": primary.get("distance_to_neckline_pct"),
        "pattern_invalidation_level": primary.get("invalidation_level"),
        "pattern_current_relation": primary.get("current_relation", ""),
        "pattern_start_date": primary.get("start_date", ""),
        "pattern_end_date": primary.get("end_date", ""),
        "pattern_formation_age_days": primary.get("formation_age_days"),
        "pattern_breakout_date": primary.get("breakout_date", ""),
        "pattern_breakout_age_days": primary.get("breakout_age_days"),
        "pattern_target_reached": bool(primary.get("target_reached", False)),
        "pattern_invalidated": bool(primary.get("invalidated", False)),
        "pattern_detail": primary["detail"],
        "patterns_count": len(detection["patterns"]),
        "all_patterns": detection["patterns"],
        "technical_lifecycle_source": primary.get("source", "visual detector"),
        "fib": fib,
        "fib_state": fib.get("state", "NON_ATTIVO"),
        "fib_score": fib.get("score", 0),
        "fib_nearest_ratio": fib.get("nearest_ratio"),
        "fib_nearest_level": fib.get("nearest_level"),
        "fib_confluence": fib.get("confluence", ""),
        "fib_details": fib.get("details", ""),
        "latest_candle": detection["candle"],
        "latest_candle_score": detection["candle_score"],
        "support": levels["support"],
        "resistance": levels["resistance"],
        "breakout_level": levels["breakout_level"],
        "breakdown_level": levels["breakdown_level"],
        "price_state": price_state,
        "breakout": breakout,
        "breakdown": breakdown,
        "rsi14": rsi_value,
        "atr14_pct": atr_pct,
        "vol_ratio": vol_ratio,
        "ret_30d": ret_30d,
        "ret_90d": ret_90d,
        "ma20": safe_float(last.get("MA20")),
        "ma50": safe_float(last.get("MA50")),
        "ma200": safe_float(last.get("MA200")),
    }


# =========================
# Report markdown / CSV
# =========================


def lifecycle_progress_text(state, progress) -> str:
    """Target progress is meaningful only after a confirmed breakout."""
    if str(state or "").upper() == "CANDIDATO":
        return "n/a"
    return fmt_pct_plain(progress)


def lifecycle_distance_text(state, distance) -> str:
    """Distance to neckline replaces misleading negative target progress for candidates."""
    if str(state or "").upper() != "CANDIDATO":
        return "n/a"
    return fmt_pct_plain(distance)


def fibonacci_summary(result) -> str:
    state = str(result.get("fib_state") or "NON_ATTIVO").replace("_", " ")
    score = fmt_signed_int(result.get("fib_score", 0))
    ratio = result.get("fib_nearest_ratio")
    level = result.get("fib_nearest_level")
    if ratio in (None, "") or pd.isna(safe_float(ratio)):
        return f"{state} ({score})"
    # FIBONACCI_PERCENT_LABEL_PATCH_V1
    ratio_value = float(ratio)
    # Nei CSV il rapporto è normalmente 0.236, 0.382, 0.500, ecc.
    # Se arriva già come 23.6 non viene moltiplicato una seconda volta.
    if abs(ratio_value) <= 1.0:
        ratio_value *= 100.0
    ratio_text = f"{ratio_value:.1f}".replace(".", ",")
    return f"Fib {ratio_text}% {state} ({score}) @ {fmt_money(result['asset'], level)}"


def build_report(results):
    generated = now_utc_str()
    summary_rows = []

    for result in results:
        asset = result["asset"]

        if not result.get("ok"):
            summary_rows.append(
                [
                    asset,
                    "n/a",
                    "ERRORE",
                    result.get("error", "n/a"),
                    "n/a",
                    "n/a",
                    "n/a",
                    "n/a",
                    "n/a",
                    "n/a",
                    "n/a",
                    "n/a",
                ]
            )
            continue

        summary_rows.append(
            [
                asset,
                fmt_money(asset, result["price"]),
                result["primary_pattern"],
                status_label(result["pattern_state"]),
                result["pattern_family"],
                result["pattern_breakout_date"] or "n/a",
                fmt_money(asset, result["pattern_target"]),
                lifecycle_progress_text(result["pattern_state"], result["pattern_target_progress_pct"]),
                lifecycle_distance_text(result["pattern_state"], result["pattern_distance_to_neckline_pct"]),
                fibonacci_summary(result),
                result["price_state"],
                fmt_money(asset, result["support"]),
            ]
        )

    lines = [
        "# Classic technical visual report",
        "",
        f"Generato: {generated}",
        "",
        (
            "Questo report crea grafici visivi dei pattern tecnici principali. "
            "Serve per vedere il grafico e il ciclo di vita dei pattern; non aggiunge "
            "automaticamente punteggio al Global."
        ),
        "",
        "Regola anti-pattern-zombie: dopo il breakout un pattern passa da ATTIVO a "
        "CONFERMATO RECENTE, poi a MATURO. Quando raggiunge il target o viene invalidato "
        "vale 0 e non resta confermato per sempre.",
        "",
        "Pattern controllati:",
        "",
        "- doppio minimo",
        "- doppio massimo",
        "- testa e spalle",
        "- testa e spalle inverso",
        "- triangolo / compressione",
        "- candela giornaliera principale",
        "- pivot high / pivot low",
        "- supporto, resistenza, breakout e breakdown 60 giorni",
        "- data breakout, età, target teorico, progresso e invalidazione",
        "- livelli Fibonacci 23,6 / 38,2 / 50 / 61,8 / 78,6 letti dal Technical Structure",
        "",
        "## Sintesi visiva",
        "",
        md_table(
            [
                "Asset",
                "Prezzo",
                "Pattern principale",
                "Stato",
                "Famiglia",
                "Breakout",
                "Target",
                "Progresso",
                "Distanza neckline",
                "Fibonacci",
                "Stato prezzo",
                "Supporto",
            ],
            summary_rows,
        ),
    ]

    for result in results:
        asset = result["asset"]
        lines.extend(["", f"## {asset}"])

        if not result.get("ok"):
            lines.extend(["", f"Errore: {result.get('error', 'n/a')}"])
            continue

        lines.extend(
            [
                "",
                f"![Classic visual {asset}]({result['image']})",
                "",
                f"- Pattern principale: **{result['primary_pattern']}**",
                f"- Stato pattern: **{status_label(result['pattern_state'])}** ({fmt_signed_int(result['pattern_score'])})",
                f"- Famiglia: **{result['pattern_family']}**",
                f"- Confidenza lifecycle: **{result['pattern_confidence'] or 'n/a'}**",
                f"- Formazione: **{result['pattern_start_date'] or 'n/a'} -> {result['pattern_end_date'] or 'n/a'}**",
                f"- Età formazione: **{safe_int(result['pattern_formation_age_days'], 0)} giorni**",
                f"- Breakout pattern: **{result['pattern_breakout_date'] or 'n/a'}**",
                (
                    f"- Età breakout: **{safe_int(result['pattern_breakout_age_days'], 0)} giorni**"
                    if result["pattern_breakout_date"]
                    else "- Età breakout: **n/a**"
                ),
                f"- Neckline: **{fmt_money(asset, result['pattern_neckline'])}**",
                f"- Target teorico: **{fmt_money(asset, result['pattern_target'])}**",
                f"- Progresso verso target: **{lifecycle_progress_text(result['pattern_state'], result['pattern_target_progress_pct'])}**",
                f"- Distanza dalla neckline: **{lifecycle_distance_text(result['pattern_state'], result['pattern_distance_to_neckline_pct'])}**",
                f"- Fonte lifecycle: **{result['technical_lifecycle_source']}**",
                f"- Fibonacci: **{fibonacci_summary(result)}** — {result['fib_details'] or 'nessuna lettura attiva'}",
                f"- Invalidazione: **{fmt_money(asset, result['pattern_invalidation_level'])}**",
                f"- Relazione prezzo/neckline: **{result['pattern_current_relation'] or 'n/a'}**",
                f"- Dettaglio: {result['pattern_detail']}",
                f"- Candela più recente: **{result['latest_candle']}**",
                f"- Stato prezzo: **{result['price_state']}**",
                f"- Supporto: **{fmt_money(asset, result['support'])}**",
                f"- Resistenza: **{fmt_money(asset, result['resistance'])}**",
                f"- Breakout 60g: **{fmt_money(asset, result['breakout_level'])}**",
                f"- Breakdown 60g: **{fmt_money(asset, result['breakdown_level'])}**",
                (
                    f"- RSI14: **{result['rsi14']:.2f}**"
                    if not pd.isna(result["rsi14"])
                    else "- RSI14: **n/a**"
                ),
                f"- ATR14: **{fmt_pct_plain(result['atr14_pct'])}**",
                (
                    f"- Volume ratio 20g: **{result['vol_ratio']:.2f}**"
                    if not pd.isna(result["vol_ratio"])
                    else "- Volume ratio 20g: **n/a**"
                ),
                f"- Rendimento 30g: **{fmt_pct(result['ret_30d'])}**",
                f"- Rendimento 90g: **{fmt_pct(result['ret_90d'])}**",
            ]
        )

        if result["all_patterns"]:
            pattern_rows = []
            for pattern in result["all_patterns"]:
                breakout_age = (
                    f"{safe_int(pattern.get('breakout_age_days'), 0)}g"
                    if pattern.get("breakout_date")
                    else "n/a"
                )
                pattern_rows.append(
                    [
                        pattern["name"],
                        status_label(pattern["state"]),
                        fmt_signed_int(pattern.get("score", 0)),
                        pattern["family"],
                        fmt_money(asset, pattern.get("neckline")),
                        pattern.get("breakout_date") or "n/a",
                        breakout_age,
                        fmt_money(asset, pattern.get("target")),
                        lifecycle_progress_text(pattern.get("state"), pattern.get("target_progress_pct")),
                        lifecycle_distance_text(pattern.get("state"), pattern.get("distance_to_neckline_pct")),
                        fmt_money(asset, pattern.get("invalidation_level")),
                        pattern["detail"],
                    ]
                )

            lines.extend(
                [
                    "",
                    "### Pattern trovati",
                    "",
                    md_table(
                        [
                            "Pattern",
                            "Stato",
                            "Score",
                            "Famiglia",
                            "Neckline",
                            "Breakout",
                            "Età",
                            "Target",
                            "Progresso",
                            "Distanza neckline",
                            "Invalidazione",
                            "Dettaglio",
                        ],
                        pattern_rows,
                    ),
                ]
            )
        else:
            lines.extend(["", "Nessun pattern classico abbastanza pulito nel lookback usato."])

    lines.extend(
        [
            "",
            "## Stati del ciclo di vita",
            "",
            "- **CANDIDATO**: geometria presente, ma neckline non ancora rotta; score 0.",
            "- **ATTIVO**: breakout avvenuto da 0 a 3 giorni; score prudente ±1.",
            "- **CONFERMATO RECENTE**: breakout da 4 a 14 giorni; score ±2.",
            "- **MATURO**: breakout più vecchio di 14 giorni e ancora valido; score ridotto ±1.",
            "- **TARGET RAGGIUNTO**: movimento teorico già completato; score 0.",
            "- **INVALIDATO**: due chiusure consecutive oltre la soglia opposta; score 0.",
            "",
            "## Come leggerlo",
            "",
            "- Il grafico in alto mostra prezzo, MA20, MA50, MA200, supporti, resistenze, neckline, target, invalidazione e livelli Fibonacci.",
            "- Il pannello centrale mostra RSI14.",
            "- Il pannello basso mostra volume e media volume 20 giorni.",
            "- Un pattern CANDIDATO non è un segnale operativo: il progresso target resta n/a e viene mostrata soltanto la distanza dalla neckline.",
            "- TARGET RAGGIUNTO e INVALIDATO restano visibili per memoria storica, ma valgono 0.",
            "- Il pattern principale usa come fonte autorevole il lifecycle di technical_structure_metrics.csv; il detector visuale resta di supporto grafico.",
            "- Fibonacci non crea un segnale autonomo: pesa al massimo ±1 nel Technical Structure solo con una confluenza indipendente.",
            "",
            (
                "Nota: questi pattern sono riconosciuti con regole algoritmiche semplici. "
                "Sono utili per visualizzare il grafico, ma vanno sempre controllati a occhio."
            ),
        ]
    )

    return "\n".join(lines).rstrip() + "\n"


def write_metrics_csv(results):
    fieldnames = [
        "generated_utc",
        "asset",
        "ticker",
        "date",
        "price",
        "price_source",
        "snapshot_candle_date",
        "image",
        "primary_pattern",
        "pattern_family",
        "pattern_direction",
        "pattern_state",
        "pattern_score",
        "pattern_confidence",
        "pattern_neckline",
        "pattern_anchor",
        "pattern_target",
        "pattern_target_progress_pct",
        "pattern_distance_to_neckline_pct",
        "pattern_invalidation_level",
        "pattern_current_relation",
        "pattern_start_date",
        "pattern_end_date",
        "pattern_formation_age_days",
        "pattern_breakout_date",
        "pattern_breakout_age_days",
        "pattern_target_reached",
        "pattern_invalidated",
        "patterns_count",
        "technical_lifecycle_source",
        "fib_state",
        "fib_score",
        "fib_nearest_ratio",
        "fib_nearest_level",
        "fib_confluence",
        "fib_details",
        "latest_candle",
        "latest_candle_score",
        "support",
        "resistance",
        "breakout_level",
        "breakdown_level",
        "price_state",
        "breakout",
        "breakdown",
        "rsi14",
        "atr14_pct",
        "vol_ratio",
        "ret_30d",
        "ret_90d",
        "ma20",
        "ma50",
        "ma200",
        "pattern_detail",
    ]

    generated = datetime.now(timezone.utc).isoformat()
    rows = []

    for result in results:
        if not result.get("ok"):
            rows.append(
                {
                    "generated_utc": generated,
                    "asset": result.get("asset"),
                    "ticker": result.get("ticker"),
                    "date": "",
                    "price": "",
                    "image": "",
                    "primary_pattern": "ERROR",
                    "pattern_detail": result.get("error", ""),
                }
            )
            continue

        row = {key: result.get(key, "") for key in fieldnames}
        row["generated_utc"] = generated
        rows.append(row)

    METRICS_CSV_PATH.parent.mkdir(parents=True, exist_ok=True)
    with METRICS_CSV_PATH.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main():
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    results = []
    for asset, ticker in ASSETS.items():
        print(f"Creo visual report per {asset}...")
        results.append(analyze_asset(asset, ticker))

    report_md = build_report(results)
    write_text(REPORT_PATH, report_md)
    write_metrics_csv(results)

    latest_text = read_text(LATEST_REPORT_PATH)
    if latest_text:
        updated_latest = replace_or_insert_block(latest_text, report_md)
        write_text(LATEST_REPORT_PATH, updated_latest)
    else:
        write_text(LATEST_REPORT_PATH, f"{START_MARKER}\n{report_md}{END_MARKER}\n")

    print(f"Classic technical visual report scritto in: {REPORT_PATH}")
    print(f"Metriche visual scritte in: {METRICS_CSV_PATH}")

    for result in results:
        if not result.get("ok"):
            print(f"{result['asset']}: ERRORE — {result.get('error', 'n/a')}")
            continue
        print(
            f"{result['asset']}: {result['primary_pattern']} | "
            f"{status_label(result['pattern_state'])} | "
            f"score {fmt_signed_int(result['pattern_score'])} | "
            f"target {fmt_money(result['asset'], result['pattern_target'])}"
        )


if __name__ == "__main__":
    main()
