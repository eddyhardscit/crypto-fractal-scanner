# -*- coding: utf-8 -*-
"""Relative-strength technical analysis for SOL/BTC and DOGE/BTC.

The module answers a different question from the USD charts: is the altcoin
actually outperforming Bitcoin, or is its USD price merely following BTC?

Design choices
--------------
* SOL/BTC and DOGE/BTC are analysed on daily and weekly timeframes.
* Direct Yahoo pair candles are preferred. If unavailable, a conservative
  synthetic OHLC ratio is built from ALT-USD / BTC-USD.
* A raw relative-strength score is produced, but its Global Confluence weight
  is hard-locked to zero until a separate live tracker matures.
* The first snapshot for each date/pair is frozen so reruns do not rewrite the
  signal history.
* A historical walk-forward diagnostic is included immediately, while live
  calibration remains separate.

No exchange credentials or trading permissions are required.
"""

from __future__ import annotations

import csv
import math
import re
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Iterable

import numpy as np
import pandas as pd
import yfinance as yf

try:
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    CHARTS_AVAILABLE = True
except Exception:
    CHARTS_AVAILABLE = False


REPORTS_DIR = Path("reports")
LATEST_REPORT = REPORTS_DIR / "latest_report.md"
REPORT_PATH = REPORTS_DIR / "relative_strength_btc_report.md"
METRICS_PATH = REPORTS_DIR / "relative_strength_btc_metrics.csv"
HISTORY_PATH = REPORTS_DIR / "relative_strength_btc_history.csv"
TRACKER_PATH = REPORTS_DIR / "relative_strength_btc_tracker_metrics.csv"
BACKTEST_PATH = REPORTS_DIR / "relative_strength_btc_backtest.csv"

START_MARKER = "<!-- RELATIVE_STRENGTH_BTC_START -->"
END_MARKER = "<!-- RELATIVE_STRENGTH_BTC_END -->"

PAIRS = {
    "SOL": {
        "direct": "SOL-BTC",
        "alt_usd": "SOL-USD",
        "btc_usd": "BTC-USD",
        "label": "SOL/BTC",
        "chart": REPORTS_DIR / "relative_strength_SOLBTC.png",
        "tolerance": 0.055,
    },
    "DOGE": {
        "direct": "DOGE-BTC",
        "alt_usd": "DOGE-USD",
        "btc_usd": "BTC-USD",
        "label": "DOGE/BTC",
        "chart": REPORTS_DIR / "relative_strength_DOGEBTC.png",
        "tolerance": 0.085,
    },
}

HORIZONS = (1, 3, 7, 14, 30)
HISTORICAL_BACKTEST_HORIZONS = (7, 30, 90)
MIN_LIVE_CONTROLS = 30
MIN_LIVE_ACCURACY = 55.0


@dataclass
class PairData:
    frame: pd.DataFrame
    source: str
    synthetic: bool


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def utc_now_str() -> str:
    return utc_now().strftime("%Y-%m-%d %H:%M UTC")


def ensure_reports() -> None:
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)


def safe_float(value: Any, default: float | None = None) -> float | None:
    try:
        number = float(value)
        if not math.isfinite(number):
            return default
        return number
    except Exception:
        return default


def fmt_ratio(value: Any, digits: int = 8) -> str:
    number = safe_float(value)
    if number is None:
        return "n/a"
    return f"{number:.{digits}f}"


def fmt_pct(value: Any, signed: bool = True) -> str:
    number = safe_float(value)
    if number is None:
        return "n/a"
    token = f"{number:+.2f}%" if signed else f"{number:.2f}%"
    return token.replace(".", ",")


def fmt_score(value: Any) -> str:
    number = int(safe_float(value, 0) or 0)
    return f"+{number}" if number > 0 else str(number)


def atomic_write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(text, encoding="utf-8", newline="\n")
    tmp.replace(path)


def read_text(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def replace_block(text: str, block: str) -> str:
    wrapped = f"{START_MARKER}\n{block.rstrip()}\n{END_MARKER}"
    if START_MARKER in text and END_MARKER in text:
        pattern = re.compile(
            re.escape(START_MARKER) + r".*?" + re.escape(END_MARKER),
            flags=re.DOTALL,
        )
        return pattern.sub(wrapped, text, count=1)

    global_start = "<!-- GLOBAL_CONFLUENCE_START -->"
    if global_start in text:
        return text.replace(global_start, wrapped + "\n\n" + global_start, 1)

    decision_end = "<!-- DECISION_REPORT_END -->"
    if decision_end in text:
        return text.replace(decision_end, decision_end + "\n\n" + wrapped, 1)

    return wrapped + "\n\n" + text


def normalise_ohlcv(frame: pd.DataFrame) -> pd.DataFrame:
    if frame is None or frame.empty:
        return pd.DataFrame()

    out = frame.copy()
    if isinstance(out.columns, pd.MultiIndex):
        out.columns = [column[0] if isinstance(column, tuple) else column for column in out.columns]

    aliases = {
        "open": "Open",
        "high": "High",
        "low": "Low",
        "close": "Close",
        "adj close": "Adj Close",
        "volume": "Volume",
    }
    renamed = {}
    for column in out.columns:
        key = str(column).strip().lower()
        if key in aliases:
            renamed[column] = aliases[key]
    out = out.rename(columns=renamed)

    if "Close" not in out.columns:
        return pd.DataFrame()

    for column in ("Open", "High", "Low"):
        if column not in out.columns:
            out[column] = out["Close"]
    if "Volume" not in out.columns:
        out["Volume"] = np.nan

    wanted = ["Open", "High", "Low", "Close", "Volume"]
    out = out[wanted].apply(pd.to_numeric, errors="coerce")
    out.index = pd.to_datetime(out.index, utc=True, errors="coerce").tz_convert(None)
    out = out[~out.index.isna()].sort_index()
    out = out[~out.index.duplicated(keep="last")]
    out = out.replace([np.inf, -np.inf], np.nan)
    out = out.dropna(subset=["Close"])
    out = out[out["Close"] > 0]
    return out


def download_history(ticker: str, period: str = "max") -> pd.DataFrame:
    errors: list[str] = []
    try:
        raw = yf.Ticker(ticker).history(
            period=period,
            interval="1d",
            auto_adjust=False,
            actions=False,
        )
        frame = normalise_ohlcv(raw)
        if len(frame) >= 220:
            return frame
    except Exception as exc:
        errors.append(f"Ticker.history: {type(exc).__name__}: {exc}")

    try:
        raw = yf.download(
            ticker,
            period=period,
            interval="1d",
            auto_adjust=False,
            actions=False,
            progress=False,
            threads=False,
        )
        frame = normalise_ohlcv(raw)
        if len(frame) >= 220:
            return frame
    except Exception as exc:
        errors.append(f"download: {type(exc).__name__}: {exc}")

    raise RuntimeError(f"Dati insufficienti per {ticker}. {' | '.join(errors)}")


def build_synthetic_pair(alt: pd.DataFrame, btc: pd.DataFrame) -> pd.DataFrame:
    joined = alt.add_prefix("ALT_").join(btc.add_prefix("BTC_"), how="inner")
    if joined.empty:
        return pd.DataFrame()

    out = pd.DataFrame(index=joined.index)
    out["Open"] = joined["ALT_Open"] / joined["BTC_Open"]
    # Conservative bounds for a ratio built from two independent OHLC candles.
    out["High"] = joined["ALT_High"] / joined["BTC_Low"]
    out["Low"] = joined["ALT_Low"] / joined["BTC_High"]
    out["Close"] = joined["ALT_Close"] / joined["BTC_Close"]
    out["Volume"] = np.nan
    out = out.replace([np.inf, -np.inf], np.nan).dropna(subset=["Close"])
    return out[out["Close"] > 0]


def load_pair(asset: str) -> PairData:
    spec = PAIRS[asset]
    try:
        direct = download_history(spec["direct"], period="max")
        if len(direct) >= 220 and direct["Close"].nunique() > 100:
            return PairData(direct, f"Yahoo Finance {spec['direct']}", False)
    except Exception:
        pass

    alt = download_history(spec["alt_usd"], period="max")
    btc = download_history(spec["btc_usd"], period="max")
    synthetic = build_synthetic_pair(alt, btc)
    if len(synthetic) < 220:
        raise RuntimeError(f"Impossibile costruire {spec['label']} con dati sufficienti.")
    return PairData(synthetic, f"Rapporto sintetico {spec['alt_usd']} / BTC-USD", True)


def ema(series: pd.Series, span: int) -> pd.Series:
    return series.ewm(span=span, adjust=False, min_periods=span).mean()


def rsi(series: pd.Series, length: int = 14) -> pd.Series:
    delta = series.diff()
    gain = delta.clip(lower=0.0)
    loss = -delta.clip(upper=0.0)
    avg_gain = gain.ewm(alpha=1.0 / length, adjust=False, min_periods=length).mean()
    avg_loss = loss.ewm(alpha=1.0 / length, adjust=False, min_periods=length).mean()
    rs = avg_gain / avg_loss.replace(0.0, np.nan)
    output = 100.0 - (100.0 / (1.0 + rs))
    output = output.where(avg_loss != 0.0, 100.0)
    return output


def add_indicators(frame: pd.DataFrame) -> pd.DataFrame:
    out = frame.copy()
    close = out["Close"]
    out["MA20"] = close.rolling(20, min_periods=20).mean()
    out["MA50"] = close.rolling(50, min_periods=50).mean()
    out["MA200"] = close.rolling(200, min_periods=200).mean()
    out["RSI14"] = rsi(close, 14)
    out["MACD"] = ema(close, 12) - ema(close, 26)
    out["MACD_SIGNAL"] = ema(out["MACD"], 9)
    out["MACD_HIST"] = out["MACD"] - out["MACD_SIGNAL"]
    out["RET7"] = close.pct_change(7) * 100.0
    out["RET30"] = close.pct_change(30) * 100.0
    out["RET90"] = close.pct_change(90) * 100.0
    out["RET180"] = close.pct_change(180) * 100.0
    return out


def to_weekly(frame: pd.DataFrame) -> pd.DataFrame:
    weekly = pd.DataFrame(index=frame.resample("W-SUN").last().index)
    weekly["Open"] = frame["Open"].resample("W-SUN").first()
    weekly["High"] = frame["High"].resample("W-SUN").max()
    weekly["Low"] = frame["Low"].resample("W-SUN").min()
    weekly["Close"] = frame["Close"].resample("W-SUN").last()
    weekly["Volume"] = frame["Volume"].resample("W-SUN").sum(min_count=1)
    weekly = weekly.dropna(subset=["Close"])
    weekly["MA10"] = weekly["Close"].rolling(10, min_periods=10).mean()
    weekly["MA30"] = weekly["Close"].rolling(30, min_periods=30).mean()
    weekly["MA40"] = weekly["Close"].rolling(40, min_periods=40).mean()
    weekly["RSI14"] = rsi(weekly["Close"], 14)
    weekly["MACD"] = ema(weekly["Close"], 12) - ema(weekly["Close"], 26)
    weekly["MACD_SIGNAL"] = ema(weekly["MACD"], 9)
    weekly["MACD_HIST"] = weekly["MACD"] - weekly["MACD_SIGNAL"]
    return weekly


def pivot_points(frame: pd.DataFrame, window: int = 4) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    highs: list[dict[str, Any]] = []
    lows: list[dict[str, Any]] = []
    high = frame["High"].to_numpy(dtype=float)
    low = frame["Low"].to_numpy(dtype=float)
    index = frame.index

    for i in range(window, len(frame) - window):
        high_slice = high[i - window : i + window + 1]
        low_slice = low[i - window : i + window + 1]
        if np.isfinite(high[i]) and high[i] >= np.nanmax(high_slice):
            highs.append({"date": index[i], "price": float(high[i])})
        if np.isfinite(low[i]) and low[i] <= np.nanmin(low_slice):
            lows.append({"date": index[i], "price": float(low[i])})

    return highs, lows


def structure_label(highs: list[dict[str, Any]], lows: list[dict[str, Any]]) -> tuple[str, int]:
    if len(highs) < 2 or len(lows) < 2:
        return "STRUTTURA NON DEFINITA", 0
    h1, h2 = highs[-2]["price"], highs[-1]["price"]
    l1, l2 = lows[-2]["price"], lows[-1]["price"]
    if h2 > h1 and l2 > l1:
        return "MASSIMI E MINIMI CRESCENTI", 1
    if h2 < h1 and l2 < l1:
        return "MASSIMI E MINIMI DECRESCENTI", -1
    if h2 < h1 and l2 > l1:
        return "COMPRESSIONE / TRIANGOLO POSSIBILE", 0
    return "VOLATILITÀ IN ESPANSIONE", 0


def support_resistance(frame: pd.DataFrame, highs: list[dict[str, Any]], lows: list[dict[str, Any]]) -> dict[str, float | None]:
    close = float(frame["Close"].iloc[-1])
    supports = [point["price"] for point in lows[-12:] if point["price"] < close]
    resistances = [point["price"] for point in highs[-12:] if point["price"] > close]
    recent = frame.iloc[-65:-3] if len(frame) >= 80 else frame.tail(60)
    return {
        "support": max(supports) if supports else safe_float(frame["Low"].tail(80).min()),
        "resistance": min(resistances) if resistances else safe_float(frame["High"].tail(80).max()),
        "breakout": safe_float(recent["High"].max()) if not recent.empty else None,
        "breakdown": safe_float(recent["Low"].min()) if not recent.empty else None,
    }


def recent_swing_fibonacci(frame: pd.DataFrame, lookback: int = 140) -> dict[str, Any]:
    recent = frame.tail(lookback)
    if len(recent) < 40:
        return {"state": "N/A"}
    high_date = recent["High"].idxmax()
    low_date = recent["Low"].idxmin()
    high = float(recent.loc[high_date, "High"])
    low = float(recent.loc[low_date, "Low"])
    if high <= low:
        return {"state": "N/A"}

    direction = "UP" if low_date < high_date else "DOWN"
    if direction == "UP":
        levels = {
            "23.6": high - (high - low) * 0.236,
            "38.2": high - (high - low) * 0.382,
            "50.0": high - (high - low) * 0.500,
            "61.8": high - (high - low) * 0.618,
            "78.6": high - (high - low) * 0.786,
        }
    else:
        levels = {
            "23.6": low + (high - low) * 0.236,
            "38.2": low + (high - low) * 0.382,
            "50.0": low + (high - low) * 0.500,
            "61.8": low + (high - low) * 0.618,
            "78.6": low + (high - low) * 0.786,
        }

    close = float(frame["Close"].iloc[-1])
    nearest_ratio, nearest_level = min(levels.items(), key=lambda item: abs(close - item[1]))
    distance_pct = (close / nearest_level - 1.0) * 100.0
    state = "VICINO" if abs(distance_pct) <= 2.0 else "NON ATTIVO"
    return {
        "state": state,
        "direction": direction,
        "start_date": min(high_date, low_date).strftime("%Y-%m-%d"),
        "end_date": max(high_date, low_date).strftime("%Y-%m-%d"),
        "high": high,
        "low": low,
        "nearest_ratio": nearest_ratio,
        "nearest_level": nearest_level,
        "distance_pct": distance_pct,
        "levels": levels,
    }


def double_pattern(
    frame: pd.DataFrame,
    highs: list[dict[str, Any]],
    lows: list[dict[str, Any]],
    tolerance: float,
) -> dict[str, Any]:
    close = float(frame["Close"].iloc[-1])
    candidates: list[dict[str, Any]] = []

    for family, points, opposite, bullish in (
        ("DOPPIO MINIMO", lows[-6:], highs, True),
        ("DOPPIO MASSIMO", highs[-6:], lows, False),
    ):
        if len(points) < 2:
            continue
        for first, second in zip(points[:-1], points[1:]):
            average = (first["price"] + second["price"]) / 2.0
            if average <= 0:
                continue
            similarity = abs(first["price"] - second["price"]) / average
            days = (second["date"] - first["date"]).days
            if similarity > tolerance or days < 7 or days > 120:
                continue
            between = [p for p in opposite if first["date"] < p["date"] < second["date"]]
            if not between:
                continue
            neckline_point = max(between, key=lambda p: p["price"]) if bullish else min(between, key=lambda p: p["price"])
            neckline = float(neckline_point["price"])
            post_pattern = frame.loc[second["date"]:].copy()
            if bullish:
                target = neckline + (neckline - average)
                confirmation_mask = post_pattern["Close"] > neckline * 1.005
                confirmed = bool(confirmation_mask.any())
                if confirmed:
                    confirmation_date = confirmation_mask[confirmation_mask].index[0]
                    target_column = "High" if "High" in post_pattern.columns else "Close"
                    target_path = post_pattern.loc[confirmation_date:, target_column]
                    target_reached = bool((target_path >= target).any())
                else:
                    target_reached = False
            else:
                target = neckline - (average - neckline)
                confirmation_mask = post_pattern["Close"] < neckline * 0.995
                confirmed = bool(confirmation_mask.any())
                if confirmed:
                    confirmation_date = confirmation_mask[confirmation_mask].index[0]
                    target_column = "Low" if "Low" in post_pattern.columns else "Close"
                    target_path = post_pattern.loc[confirmation_date:, target_column]
                    target_reached = bool((target_path <= target).any())
                else:
                    target_reached = False

            if target_reached:
                state = "TARGET RAGGIUNTO"
            elif confirmed:
                state = "CONFERMATO"
            else:
                state = "CANDIDATO"

            candidates.append(
                {
                    "family": family,
                    "state": state,
                    "bullish": bullish,
                    "first_date": first["date"].strftime("%Y-%m-%d"),
                    "second_date": second["date"].strftime("%Y-%m-%d"),
                    "neckline": neckline,
                    "target": target,
                    "similarity_pct": similarity * 100.0,
                    "age_days": (frame.index[-1] - second["date"]).days,
                }
            )

    if not candidates:
        return {"family": "NESSUNO", "state": "ASSENTE"}

    state_priority = {"TARGET RAGGIUNTO": 3, "CONFERMATO": 2, "CANDIDATO": 1}
    candidates.sort(
        key=lambda item: (
            state_priority.get(item["state"], 0),
            -item["age_days"],
            -item["similarity_pct"],
        ),
        reverse=True,
    )
    return candidates[0]


def slope_pct(series: pd.Series, periods: int) -> float | None:
    clean = series.dropna()
    if len(clean) <= periods:
        return None
    old = float(clean.iloc[-periods - 1])
    new = float(clean.iloc[-1])
    if old == 0:
        return None
    return (new / old - 1.0) * 100.0


def score_pair(daily: pd.DataFrame, weekly: pd.DataFrame, structure_score: int, levels: dict[str, Any]) -> dict[str, Any]:
    row = daily.iloc[-1]
    week = weekly.iloc[-1]
    close = float(row["Close"])
    score = 0
    reasons: list[str] = []

    ma50 = safe_float(row.get("MA50"))
    ma200 = safe_float(row.get("MA200"))
    ma50_slope = slope_pct(daily["MA50"], 20)
    ma200_slope = slope_pct(daily["MA200"], 60)

    if ma50 is not None:
        if close > ma50:
            score += 1
            reasons.append("prezzo sopra MA50 daily")
        else:
            score -= 1
            reasons.append("prezzo sotto MA50 daily")
    if ma200 is not None:
        if close > ma200:
            score += 1
            reasons.append("prezzo sopra MA200 daily")
        else:
            score -= 1
            reasons.append("prezzo sotto MA200 daily")
    if ma50_slope is not None:
        if ma50_slope > 1.0:
            score += 1
            reasons.append("MA50 daily in salita")
        elif ma50_slope < -1.0:
            score -= 1
            reasons.append("MA50 daily in discesa")

    week_ma30 = safe_float(week.get("MA30"))
    week_ma_slope = slope_pct(weekly["MA30"], 8)
    if week_ma30 is not None:
        if float(week["Close"]) > week_ma30:
            score += 1
            reasons.append("prezzo sopra MA30 weekly")
        else:
            score -= 1
            reasons.append("prezzo sotto MA30 weekly")
    if week_ma_slope is not None:
        if week_ma_slope > 1.0:
            score += 1
            reasons.append("MA30 weekly in salita")
        elif week_ma_slope < -1.0:
            score -= 1
            reasons.append("MA30 weekly in discesa")

    score += int(structure_score)
    if structure_score > 0:
        reasons.append("struttura con massimi/minimi crescenti")
    elif structure_score < 0:
        reasons.append("struttura con massimi/minimi decrescenti")

    rsi14 = safe_float(row.get("RSI14"))
    if rsi14 is not None:
        if rsi14 >= 57:
            score += 1
            reasons.append("RSI relativo forte")
        elif rsi14 <= 43:
            score -= 1
            reasons.append("RSI relativo debole")

    macd_hist = safe_float(row.get("MACD_HIST"))
    if macd_hist is not None:
        if macd_hist > 0:
            score += 1
            reasons.append("MACD relativo positivo")
        elif macd_hist < 0:
            score -= 1
            reasons.append("MACD relativo negativo")

    breakout = safe_float(levels.get("breakout"))
    breakdown = safe_float(levels.get("breakdown"))
    if breakout is not None and close > breakout * 1.005:
        score += 2
        reasons.append("breakout relativo 60g")
    elif breakdown is not None and close < breakdown * 0.995:
        score -= 2
        reasons.append("breakdown relativo 60g")

    score = int(max(-8, min(8, score)))
    candidate = 1 if score >= 4 else -1 if score <= -4 else 0
    if candidate > 0:
        label = "SOVRAPERFORMA BTC"
    elif candidate < 0:
        label = "SOTTOPERFORMA BTC"
    else:
        label = "RELATIVA MISTA / NON CONFERMATA"

    confidence = "MEDIA" if abs(score) >= 5 else "BASSA"
    return {
        "raw_score": score,
        "candidate_score": candidate,
        "global_score": 0,
        "label": label,
        "confidence": confidence,
        "reasons": reasons,
        "ma50_slope_20d_pct": ma50_slope,
        "ma200_slope_60d_pct": ma200_slope,
        "weekly_ma30_slope_8w_pct": week_ma_slope,
    }


def read_usd_technical(asset: str) -> dict[str, Any]:
    path = REPORTS_DIR / "technical_structure_metrics.csv"
    if not path.exists():
        return {}
    try:
        frame = pd.read_csv(path)
    except Exception:
        return {}
    if "asset" not in frame.columns:
        return {}
    rows = frame[frame["asset"].astype(str).str.upper() == asset]
    if rows.empty:
        return {}
    row = rows.iloc[-1].to_dict()
    score = safe_float(row.get("technical_score"), 0) or 0
    if score >= 3:
        direction = "RIALZISTA"
    elif score <= -3:
        direction = "RIBASSISTA"
    else:
        direction = "MISTA"
    return {
        "score": int(score),
        "direction": direction,
        "verdict": str(row.get("verdict", "")),
        "price": safe_float(row.get("price")),
    }


def matrix_interpretation(usd_direction: str, relative_candidate: int) -> str:
    usd = usd_direction.upper()
    if usd == "RIALZISTA" and relative_candidate > 0:
        return "CONFERMA FORTE: sale in USD e batte BTC"
    if usd == "RIALZISTA" and relative_candidate < 0:
        return "SALE SOLO IN USD: BTC resta più forte"
    if usd == "RIBASSISTA" and relative_candidate > 0:
        return "FORZA RELATIVA NASCOSTA: debole in USD ma migliore di BTC"
    if usd == "RIBASSISTA" and relative_candidate < 0:
        return "DEBOLEZZA COMPLETA: scende in USD e contro BTC"
    if relative_candidate > 0:
        return "FORZA RELATIVA POSITIVA, USD ANCORA MISTO"
    if relative_candidate < 0:
        return "FORZA RELATIVA NEGATIVA, USD ANCORA MISTO"
    return "QUADRO MISTO / NESSUNA CONFERMA RELATIVA"


def vectorised_backtest_score(daily: pd.DataFrame) -> pd.Series:
    close = daily["Close"]
    ma50 = close.rolling(50, min_periods=50).mean()
    ma200 = close.rolling(200, min_periods=200).mean()
    ma50_slope = ma50.pct_change(20)
    rel30 = close.pct_change(30)
    rsi14 = rsi(close, 14)
    macd = ema(close, 12) - ema(close, 26)
    hist = macd - ema(macd, 9)

    score = pd.Series(0.0, index=daily.index)
    score += np.where(close > ma50, 1.0, -1.0)
    score += np.where(close > ma200, 1.0, -1.0)
    score += np.where(ma50_slope > 0.01, 1.0, np.where(ma50_slope < -0.01, -1.0, 0.0))
    score += np.where(rsi14 >= 57, 1.0, np.where(rsi14 <= 43, -1.0, 0.0))
    score += np.where(hist > 0, 1.0, np.where(hist < 0, -1.0, 0.0))
    score += np.where(rel30 > 0.05, 1.0, np.where(rel30 < -0.05, -1.0, 0.0))
    score[(ma200.isna()) | (rsi14.isna()) | (hist.isna())] = np.nan
    return score


def historical_backtest(asset: str, daily: pd.DataFrame) -> list[dict[str, Any]]:
    score = vectorised_backtest_score(daily)
    candidate = pd.Series(0.0, index=score.index)
    candidate[score >= 3] = 1.0
    candidate[score <= -3] = -1.0

    # Weekly sampling reduces extreme overlap while retaining enough observations.
    sampled_index = daily.index[::7]
    rows: list[dict[str, Any]] = []
    for horizon in HISTORICAL_BACKTEST_HORIZONS:
        future_return = daily["Close"].shift(-horizon) / daily["Close"] - 1.0
        sample = pd.DataFrame(
            {
                "candidate": candidate.reindex(sampled_index),
                "future_return": future_return.reindex(sampled_index),
            }
        ).dropna()
        sample = sample[sample["candidate"] != 0]
        if sample.empty:
            rows.append(
                {
                    "asset": asset,
                    "horizon_days": horizon,
                    "controls": 0,
                    "accuracy_pct": np.nan,
                    "directional_return_pct": np.nan,
                    "median_future_return_pct": np.nan,
                }
            )
            continue
        correct = np.sign(sample["future_return"]) == np.sign(sample["candidate"])
        directional = sample["future_return"] * sample["candidate"]
        rows.append(
            {
                "asset": asset,
                "horizon_days": horizon,
                "controls": int(len(sample)),
                "accuracy_pct": float(correct.mean() * 100.0),
                "directional_return_pct": float(directional.mean() * 100.0),
                "median_future_return_pct": float(sample["future_return"].median() * 100.0),
            }
        )
    return rows


def read_csv_dicts(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    try:
        with path.open("r", encoding="utf-8", newline="") as handle:
            return list(csv.DictReader(handle))
    except Exception:
        return []


def write_csv_dicts(path: Path, rows: Iterable[dict[str, Any]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    with tmp.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow({key: row.get(key, "") for key in fieldnames})
    tmp.replace(path)


def freeze_daily_history(metrics: list[dict[str, Any]]) -> None:
    fields = [
        "signal_date",
        "generated_utc",
        "asset",
        "pair",
        "pair_price",
        "raw_score",
        "candidate_score",
        "global_score",
        "confidence",
        "source",
        "synthetic",
        "usd_technical_direction",
        "matrix_interpretation",
    ]
    existing = read_csv_dicts(HISTORY_PATH)
    keys = {(row.get("signal_date", ""), row.get("asset", "")) for row in existing}
    today = utc_now().date().isoformat()
    for row in metrics:
        key = (today, row["asset"])
        if key in keys:
            continue
        existing.append(
            {
                "signal_date": today,
                "generated_utc": utc_now().isoformat(),
                "asset": row["asset"],
                "pair": row["pair"],
                "pair_price": row["pair_price"],
                "raw_score": row["raw_score"],
                "candidate_score": row["candidate_score"],
                "global_score": 0,
                "confidence": row["confidence"],
                "source": row["source"],
                "synthetic": row["synthetic"],
                "usd_technical_direction": row["usd_technical_direction"],
                "matrix_interpretation": row["matrix_interpretation"],
            }
        )
        keys.add(key)
    existing.sort(key=lambda row: (row.get("signal_date", ""), row.get("asset", "")))
    write_csv_dicts(HISTORY_PATH, existing, fields)


def price_on_or_after(frame: pd.DataFrame, date: pd.Timestamp) -> float | None:
    rows = frame[frame.index >= date]
    if rows.empty:
        return None
    return safe_float(rows["Close"].iloc[0])


def update_live_tracker(pair_frames: dict[str, pd.DataFrame]) -> list[dict[str, Any]]:
    history = read_csv_dicts(HISTORY_PATH)
    summaries: list[dict[str, Any]] = []
    latest_available = {
        asset: frame.index[-1].normalize() for asset, frame in pair_frames.items() if not frame.empty
    }
    for asset in PAIRS:
        asset_rows = [row for row in history if row.get("asset") == asset]
        frame = pair_frames.get(asset)
        for horizon in HORIZONS:
            checked: list[dict[str, float]] = []
            if frame is not None and not frame.empty:
                for row in asset_rows:
                    candidate = safe_float(row.get("candidate_score"), 0) or 0
                    if candidate == 0:
                        continue
                    try:
                        start_date = pd.Timestamp(row["signal_date"])
                    except Exception:
                        continue
                    target_date = start_date + pd.Timedelta(days=horizon)
                    if target_date > latest_available.get(asset, target_date - pd.Timedelta(days=1)):
                        continue
                    start_price = safe_float(row.get("pair_price"))
                    end_price = price_on_or_after(frame, target_date)
                    if start_price is None or end_price is None or start_price <= 0:
                        continue
                    ret = (end_price / start_price - 1.0) * 100.0
                    checked.append(
                        {
                            "correct": float(np.sign(ret) == np.sign(candidate)),
                            "directional_return": ret * candidate,
                        }
                    )
            if checked:
                controls = len(checked)
                accuracy = sum(item["correct"] for item in checked) / controls * 100.0
                directional_return = sum(item["directional_return"] for item in checked) / controls
            else:
                controls = 0
                accuracy = np.nan
                directional_return = np.nan
            active = (
                horizon == 7
                and controls >= MIN_LIVE_CONTROLS
                and math.isfinite(accuracy)
                and accuracy >= MIN_LIVE_ACCURACY
                and math.isfinite(directional_return)
                and directional_return > 0
            )
            summaries.append(
                {
                    "generated_utc": utc_now().isoformat(),
                    "asset": asset,
                    "horizon_days": horizon,
                    "controls": controls,
                    "accuracy_pct": accuracy,
                    "directional_return_pct": directional_return,
                    "activation_state": "ELIGIBILE FUTURO ±1" if active else "LOCKED / RACCOLTA LIVE",
                    "global_weight": 0,
                }
            )

    fields = [
        "generated_utc",
        "asset",
        "horizon_days",
        "controls",
        "accuracy_pct",
        "directional_return_pct",
        "activation_state",
        "global_weight",
    ]
    write_csv_dicts(TRACKER_PATH, summaries, fields)
    return summaries


def plot_pair(asset: str, daily: pd.DataFrame, weekly: pd.DataFrame, levels: dict[str, Any], pattern: dict[str, Any]) -> None:
    if not CHARTS_AVAILABLE:
        return
    spec = PAIRS[asset]
    plot_df = daily.tail(365)
    fig, axes = plt.subplots(3, 1, figsize=(14, 10), sharex=True, gridspec_kw={"height_ratios": [4, 1.3, 1.2]})

    axes[0].plot(plot_df.index, plot_df["Close"], label=spec["label"], linewidth=1.6)
    axes[0].plot(plot_df.index, plot_df["MA20"], label="MA20", linewidth=1.0)
    axes[0].plot(plot_df.index, plot_df["MA50"], label="MA50", linewidth=1.0)
    axes[0].plot(plot_df.index, plot_df["MA200"], label="MA200", linewidth=1.0)
    for key, label in (("support", "Supporto"), ("resistance", "Resistenza"), ("breakout", "Breakout 60g"), ("breakdown", "Breakdown 60g")):
        value = safe_float(levels.get(key))
        if value is not None:
            axes[0].axhline(value, linestyle="--", linewidth=0.8, label=f"{label} {value:.8f}")
    neckline = safe_float(pattern.get("neckline"))
    target = safe_float(pattern.get("target"))
    if neckline is not None:
        axes[0].axhline(neckline, linestyle=":", linewidth=1.1, label=f"Neckline {neckline:.8f}")
    if target is not None:
        axes[0].axhline(target, linestyle=":", linewidth=1.1, label=f"Target {target:.8f}")
    axes[0].set_title(f"{spec['label']} — forza relativa contro Bitcoin")
    axes[0].set_yscale("log")
    axes[0].legend(loc="best", fontsize=8, ncol=2)
    axes[0].grid(True, alpha=0.25)

    axes[1].plot(plot_df.index, plot_df["RSI14"], label="RSI14")
    axes[1].axhline(70, linestyle="--", linewidth=0.8)
    axes[1].axhline(50, linestyle=":", linewidth=0.8)
    axes[1].axhline(30, linestyle="--", linewidth=0.8)
    axes[1].set_ylim(0, 100)
    axes[1].set_ylabel("RSI")
    axes[1].grid(True, alpha=0.25)

    axes[2].plot(plot_df.index, plot_df["MACD_HIST"], label="MACD histogram")
    axes[2].axhline(0, linewidth=0.8)
    axes[2].set_ylabel("MACD")
    axes[2].grid(True, alpha=0.25)

    fig.tight_layout()
    fig.savefig(spec["chart"], dpi=150, bbox_inches="tight")
    plt.close(fig)


def analyse_asset(asset: str, pair_data: PairData) -> tuple[dict[str, Any], pd.DataFrame]:
    daily = add_indicators(pair_data.frame)
    weekly = to_weekly(pair_data.frame)
    highs, lows = pivot_points(daily.tail(260), window=4)
    structure, structure_score = structure_label(highs, lows)
    levels = support_resistance(daily, highs, lows)
    fib = recent_swing_fibonacci(daily)
    pattern = double_pattern(daily, highs, lows, PAIRS[asset]["tolerance"])
    scoring = score_pair(daily, weekly, structure_score, levels)
    usd = read_usd_technical(asset)
    matrix = matrix_interpretation(usd.get("direction", "MISTA"), scoring["candidate_score"])
    row = daily.iloc[-1]
    week = weekly.iloc[-1]

    metrics = {
        "generated_utc": utc_now().isoformat(),
        "asset": asset,
        "pair": PAIRS[asset]["label"],
        "pair_price": float(row["Close"]),
        "source": pair_data.source,
        "synthetic": pair_data.synthetic,
        "raw_score": scoring["raw_score"],
        "candidate_score": scoring["candidate_score"],
        "global_score": 0,
        "activation_state": "DIAGNOSTICO / PESO 0",
        "bias": scoring["label"],
        "confidence": scoring["confidence"],
        "ret_7d_pct": safe_float(row.get("RET7")),
        "ret_30d_pct": safe_float(row.get("RET30")),
        "ret_90d_pct": safe_float(row.get("RET90")),
        "ret_180d_pct": safe_float(row.get("RET180")),
        "daily_rsi14": safe_float(row.get("RSI14")),
        "daily_macd_hist": safe_float(row.get("MACD_HIST")),
        "daily_ma20": safe_float(row.get("MA20")),
        "daily_ma50": safe_float(row.get("MA50")),
        "daily_ma200": safe_float(row.get("MA200")),
        "daily_ma50_slope_20d_pct": scoring["ma50_slope_20d_pct"],
        "daily_ma200_slope_60d_pct": scoring["ma200_slope_60d_pct"],
        "weekly_ma10": safe_float(week.get("MA10")),
        "weekly_ma30": safe_float(week.get("MA30")),
        "weekly_ma40": safe_float(week.get("MA40")),
        "weekly_ma30_slope_8w_pct": scoring["weekly_ma30_slope_8w_pct"],
        "weekly_rsi14": safe_float(week.get("RSI14")),
        "weekly_macd_hist": safe_float(week.get("MACD_HIST")),
        "structure": structure,
        "support": levels.get("support"),
        "resistance": levels.get("resistance"),
        "breakout_60d": levels.get("breakout"),
        "breakdown_60d": levels.get("breakdown"),
        "pattern": pattern.get("family", "NESSUNO"),
        "pattern_state": pattern.get("state", "ASSENTE"),
        "pattern_neckline": pattern.get("neckline"),
        "pattern_target": pattern.get("target"),
        "fib_state": fib.get("state", "N/A"),
        "fib_nearest_ratio": fib.get("nearest_ratio"),
        "fib_nearest_level": fib.get("nearest_level"),
        "usd_technical_score": usd.get("score", 0),
        "usd_technical_direction": usd.get("direction", "MISTA"),
        "usd_technical_verdict": usd.get("verdict", ""),
        "matrix_interpretation": matrix,
        "reasons": "; ".join(scoring["reasons"]),
    }
    plot_pair(asset, daily, weekly, levels, pattern)
    return metrics, daily


def write_metrics(metrics: list[dict[str, Any]]) -> None:
    fields = [
        "generated_utc",
        "asset",
        "pair",
        "pair_price",
        "source",
        "synthetic",
        "raw_score",
        "candidate_score",
        "global_score",
        "activation_state",
        "bias",
        "confidence",
        "ret_7d_pct",
        "ret_30d_pct",
        "ret_90d_pct",
        "ret_180d_pct",
        "daily_rsi14",
        "daily_macd_hist",
        "daily_ma20",
        "daily_ma50",
        "daily_ma200",
        "daily_ma50_slope_20d_pct",
        "daily_ma200_slope_60d_pct",
        "weekly_ma10",
        "weekly_ma30",
        "weekly_ma40",
        "weekly_ma30_slope_8w_pct",
        "weekly_rsi14",
        "weekly_macd_hist",
        "structure",
        "support",
        "resistance",
        "breakout_60d",
        "breakdown_60d",
        "pattern",
        "pattern_state",
        "pattern_neckline",
        "pattern_target",
        "fib_state",
        "fib_nearest_ratio",
        "fib_nearest_level",
        "usd_technical_score",
        "usd_technical_direction",
        "usd_technical_verdict",
        "matrix_interpretation",
        "reasons",
    ]
    write_csv_dicts(METRICS_PATH, metrics, fields)


def md_table(headers: list[str], rows: list[list[Any]]) -> str:
    lines = ["| " + " | ".join(headers) + " |", "| " + " | ".join(["---"] * len(headers)) + " |"]
    for row in rows:
        lines.append("| " + " | ".join(str(cell) for cell in row) + " |")
    return "\n".join(lines)


def tracker_lookup(tracker: list[dict[str, Any]], asset: str, horizon: int) -> dict[str, Any]:
    for row in tracker:
        if row["asset"] == asset and int(row["horizon_days"]) == horizon:
            return row
    return {}


def build_report(metrics: list[dict[str, Any]], backtest: list[dict[str, Any]], tracker: list[dict[str, Any]]) -> str:
    lines: list[str] = []
    lines.append("# Forza relativa SOL/BTC e DOGE/BTC")
    lines.append("")
    lines.append(f"Generato: {utc_now_str()}")
    lines.append("")
    lines.append(
        "Questo modulo controlla se SOL e DOGE stanno davvero battendo Bitcoin. "
        "Una salita in USD accompagnata da una coppia ALT/BTC ribassista è spesso soltanto trascinamento di BTC."
    )
    lines.append("")
    lines.append(
        "**Protezione iniziale:** il candidato relativo è limitato a -1/0/+1, ma il peso nel Global resta **0**. "
        "La coppia BTC conferma o indebolisce il tecnico USD; non viene sommata come secondo modulo indipendente."
    )
    lines.append("")
    summary_rows = []
    for row in metrics:
        summary_rows.append(
            [
                row["asset"],
                row["pair"],
                fmt_ratio(row["pair_price"]),
                fmt_score(row["raw_score"]),
                fmt_score(row["candidate_score"]),
                "0",
                row["bias"],
                row["confidence"],
                fmt_pct(row["ret_30d_pct"]),
                row["usd_technical_direction"],
                row["matrix_interpretation"],
            ]
        )
    lines.append("## Sintesi")
    lines.append("")
    lines.append(
        md_table(
            ["Asset", "Coppia", "Prezzo", "Score raw", "Candidato", "Peso Global", "Forza vs BTC", "Confidenza", "30g", "Tecnico USD", "Lettura combinata"],
            summary_rows,
        )
    )
    lines.append("")

    lines.append("## Matrice di lettura")
    lines.append("")
    lines.append(
        md_table(
            ["ALT/USD", "ALT/BTC", "Interpretazione"],
            [
                ["Rialzista", "Rialzista", "Conferma migliore: sale e batte BTC"],
                ["Rialzista", "Ribassista", "Sale soprattutto perché BTC trascina il mercato"],
                ["Ribassista", "Rialzista", "Forza relativa nascosta / possibile rotazione futura"],
                ["Ribassista", "Ribassista", "Debolezza completa"],
            ],
        )
    )
    lines.append("")

    for row in metrics:
        asset = row["asset"]
        lines.append(f"## {row['pair']}")
        lines.append("")
        lines.append(f"- **Verdetto relativo:** {row['bias']} ({fmt_score(row['raw_score'])})")
        lines.append(f"- **Candidato futuro:** {fmt_score(row['candidate_score'])}; **peso attuale Global: 0**")
        lines.append(f"- **Lettura combinata USD/BTC:** {row['matrix_interpretation']}")
        lines.append(f"- **Struttura:** {row['structure']}")
        lines.append(f"- **Rendimenti relativi:** 7g {fmt_pct(row['ret_7d_pct'])}; 30g {fmt_pct(row['ret_30d_pct'])}; 90g {fmt_pct(row['ret_90d_pct'])}; 180g {fmt_pct(row['ret_180d_pct'])}")
        lines.append(f"- **Daily:** RSI {safe_float(row['daily_rsi14'], float('nan')):.2f}; MA50 {fmt_ratio(row['daily_ma50'])}; MA200 {fmt_ratio(row['daily_ma200'])}")
        lines.append(f"- **Weekly:** MA30 {fmt_ratio(row['weekly_ma30'])}; RSI {safe_float(row['weekly_rsi14'], float('nan')):.2f}")
        lines.append(f"- **Livelli:** supporto {fmt_ratio(row['support'])}; resistenza {fmt_ratio(row['resistance'])}; breakout 60g {fmt_ratio(row['breakout_60d'])}; breakdown 60g {fmt_ratio(row['breakdown_60d'])}")
        lines.append(f"- **Pattern:** {row['pattern']} / {row['pattern_state']}; neckline {fmt_ratio(row['pattern_neckline'])}; target {fmt_ratio(row['pattern_target'])}")
        lines.append(f"- **Fibonacci:** {row['fib_state']} — {row['fib_nearest_ratio'] or 'n/a'}% a {fmt_ratio(row['fib_nearest_level'])}")
        lines.append(f"- **Fonte:** {row['source']} ({'sintetica' if row['synthetic'] else 'coppia diretta'})")
        lines.append(f"- **Motivi score:** {row['reasons'] or 'n/a'}")
        lines.append("")
        chart = PAIRS[asset]["chart"].name
        if PAIRS[asset]["chart"].exists():
            lines.append(f"![Grafico {row['pair']}]({chart})")
            lines.append("")

    lines.append("## Backtest storico diagnostico")
    lines.append("")
    lines.append(
        "Il backtest usa soltanto indicatori disponibili alla data del segnale e campiona una volta a settimana. "
        "È utile subito, ma non sostituisce il tracker live: le soglie sono state definite prima di vedere il risultato."
    )
    lines.append("")
    backtest_rows = []
    for row in backtest:
        backtest_rows.append(
            [
                row["asset"],
                f"{row['horizon_days']}g",
                row["controls"],
                fmt_pct(row["accuracy_pct"], signed=False),
                fmt_pct(row["directional_return_pct"]),
                fmt_pct(row["median_future_return_pct"]),
            ]
        )
    lines.append(md_table(["Asset", "Orizzonte", "Controlli", "Accuratezza", "Return corretto direzione", "Return futuro mediano"], backtest_rows))
    lines.append("")

    lines.append("## Tracker live e gate futuro")
    lines.append("")
    tracker_rows = []
    for row in tracker:
        tracker_rows.append(
            [
                row["asset"],
                f"{row['horizon_days']}g",
                row["controls"],
                fmt_pct(row["accuracy_pct"], signed=False),
                fmt_pct(row["directional_return_pct"]),
                row["activation_state"],
                "0",
            ]
        )
    lines.append(md_table(["Asset", "Orizzonte", "Controlli", "Accuratezza", "Return corretto", "Stato", "Peso Global"], tracker_rows))
    lines.append("")
    lines.append(
        "Gate prudente: almeno 30 controlli live a 7 giorni, accuratezza almeno 55% e return corretto direzione positivo. "
        "Anche dopo il gate, il contributo futuro non dovrà superare ±1 e dovrà restare dentro la famiglia tecnica."
    )
    lines.append("")
    lines.append("## File prodotti")
    lines.append("")
    for path in (METRICS_PATH, HISTORY_PATH, TRACKER_PATH, BACKTEST_PATH):
        lines.append(f"- `{path}`")
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    ensure_reports()
    metrics: list[dict[str, Any]] = []
    pair_frames: dict[str, pd.DataFrame] = {}
    backtest: list[dict[str, Any]] = []
    errors: list[str] = []

    for asset in PAIRS:
        try:
            pair_data = load_pair(asset)
            row, daily = analyse_asset(asset, pair_data)
            metrics.append(row)
            pair_frames[asset] = daily
            backtest.extend(historical_backtest(asset, daily))
        except Exception as exc:
            errors.append(f"{asset}: {type(exc).__name__}: {exc}")

    if not metrics:
        raise RuntimeError("Nessuna coppia relativa disponibile. " + " | ".join(errors))

    write_metrics(metrics)
    freeze_daily_history(metrics)
    tracker = update_live_tracker(pair_frames)
    write_csv_dicts(
        BACKTEST_PATH,
        backtest,
        ["asset", "horizon_days", "controls", "accuracy_pct", "directional_return_pct", "median_future_return_pct"],
    )

    report = build_report(metrics, backtest, tracker)
    if errors:
        report += "\n## Avvisi raccolta\n\n" + "\n".join(f"- {error}" for error in errors) + "\n"
    atomic_write(REPORT_PATH, report)

    latest = read_text(LATEST_REPORT)
    atomic_write(LATEST_REPORT, replace_block(latest, report))
    print(f"Relative Strength BTC report: {REPORT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
