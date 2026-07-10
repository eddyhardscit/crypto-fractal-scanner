import csv
import math
import re
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd
import yfinance as yf


REPORTS_DIR = Path("reports")
LATEST_REPORT_PATH = REPORTS_DIR / "latest_report.md"

REPORT_PATH = REPORTS_DIR / "classic_technical_confirmation_report.md"
METRICS_CSV_PATH = REPORTS_DIR / "classic_technical_confirmation_metrics.csv"

START_MARKER = "<!-- CLASSIC_TECHNICAL_CONFIRMATION_START -->"
END_MARKER = "<!-- CLASSIC_TECHNICAL_CONFIRMATION_END -->"

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


# =========================
# Utility base
# =========================

def now_utc_str() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")


def read_text(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def replace_or_insert_block(text: str, block: str) -> str:
    full_block = f"{START_MARKER}\n{block.rstrip()}\n{END_MARKER}"

    if START_MARKER in text and END_MARKER in text:
        pattern = re.compile(
            re.escape(START_MARKER) + r".*?" + re.escape(END_MARKER),
            flags=re.DOTALL,
        )
        return pattern.sub(full_block, text)

    global_start = "<!-- GLOBAL_CONFLUENCE_START -->"
    if global_start in text:
        return text.replace(global_start, full_block + "\n\n" + global_start, 1)

    tech_end = "<!-- TECHNICAL_STRUCTURE_END -->"
    if tech_end in text:
        return text.replace(tech_end, tech_end + "\n\n" + full_block, 1)

    return text.rstrip() + "\n\n" + full_block + "\n"


def safe_float(value):
    try:
        if value is None:
            return np.nan
        if pd.isna(value):
            return np.nan
        return float(value)
    except Exception:
        return np.nan


def clamp(value: int, low: int, high: int) -> int:
    return max(low, min(high, int(value)))


def fmt_signed(value) -> str:
    try:
        v = int(value)
    except Exception:
        return "0"
    if v > 0:
        return f"+{v}"
    return str(v)


def fmt_pct(value, decimals: int = 2) -> str:
    if value is None or pd.isna(value):
        return "n/a"
    s = f"{float(value):+.{decimals}f}%"
    return s.replace(".", ",")


def fmt_pct_plain(value, decimals: int = 2) -> str:
    if value is None or pd.isna(value):
        return "n/a"
    s = f"{float(value):.{decimals}f}%"
    return s.replace(".", ",")


def fmt_price(asset: str, value) -> str:
    if value is None or pd.isna(value):
        return "n/a"

    v = float(value)

    if asset == "BTC":
        s = f"{v:,.0f}"
        return s.replace(",", ".")

    if asset == "DOGE":
        return f"{v:.5f}"

    s = f"{v:,.2f}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".")


def fmt_money(asset: str, value) -> str:
    p = fmt_price(asset, value)
    if p == "n/a":
        return "n/a"
    return f"{p} $"


def md_table(headers, rows) -> str:
    out = []
    out.append("| " + " | ".join(headers) + " |")
    out.append("| " + " | ".join(["---"] * len(headers)) + " |")
    for row in rows:
        out.append("| " + " | ".join(str(x) for x in row) + " |")
    return "\n".join(out)


# =========================
# Download dati
# =========================

def normalize_yfinance_df(df: pd.DataFrame) -> pd.DataFrame:
    if df is None or df.empty:
        return pd.DataFrame()

    df = df.copy()

    if isinstance(df.columns, pd.MultiIndex):
        df.columns = [c[0] for c in df.columns]

    rename = {}
    for c in df.columns:
        cl = str(c).lower().strip()
        if cl == "open":
            rename[c] = "Open"
        elif cl == "high":
            rename[c] = "High"
        elif cl == "low":
            rename[c] = "Low"
        elif cl == "close":
            rename[c] = "Close"
        elif cl == "adj close":
            rename[c] = "Adj Close"
        elif cl == "volume":
            rename[c] = "Volume"

    df = df.rename(columns=rename)

    required = ["Open", "High", "Low", "Close", "Volume"]
    for col in required:
        if col not in df.columns:
            return pd.DataFrame()

    df = df[required].copy()
    df = df.dropna(subset=["Open", "High", "Low", "Close"])

    if "Volume" in df.columns:
        df["Volume"] = df["Volume"].fillna(0)

    df.index = pd.to_datetime(df.index).tz_localize(None)
    df = df.sort_index()

    return df


def download_ohlcv(ticker: str, period: str = "1200d", interval: str = "1d") -> pd.DataFrame:
    try:
        df = yf.download(
            ticker,
            period=period,
            interval=interval,
            auto_adjust=False,
            progress=False,
            threads=False,
        )
        return normalize_yfinance_df(df)
    except Exception:
        return pd.DataFrame()


# =========================
# Indicatori tecnici
# =========================

def add_indicators(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return df

    out = df.copy()

    close = out["Close"]
    high = out["High"]
    low = out["Low"]
    volume = out["Volume"]

    out["MA20"] = close.rolling(20).mean()
    out["MA50"] = close.rolling(50).mean()
    out["MA100"] = close.rolling(100).mean()
    out["MA200"] = close.rolling(200).mean()

    out["EMA12"] = close.ewm(span=12, adjust=False).mean()
    out["EMA26"] = close.ewm(span=26, adjust=False).mean()
    out["MACD"] = out["EMA12"] - out["EMA26"]
    out["MACD_SIGNAL"] = out["MACD"].ewm(span=9, adjust=False).mean()
    out["MACD_HIST"] = out["MACD"] - out["MACD_SIGNAL"]

    delta = close.diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    avg_gain = gain.ewm(alpha=1 / 14, adjust=False).mean()
    avg_loss = loss.ewm(alpha=1 / 14, adjust=False).mean()
    rs = avg_gain / avg_loss.replace(0, np.nan)
    out["RSI14"] = 100 - (100 / (1 + rs))

    tr1 = high - low
    tr2 = (high - close.shift(1)).abs()
    tr3 = (low - close.shift(1)).abs()
    tr = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)
    out["ATR14"] = tr.rolling(14).mean()
    out["ATR14_PCT"] = out["ATR14"] / close * 100

    out["BB_MID"] = close.rolling(20).mean()
    out["BB_STD"] = close.rolling(20).std()
    out["BB_UPPER"] = out["BB_MID"] + 2 * out["BB_STD"]
    out["BB_LOWER"] = out["BB_MID"] - 2 * out["BB_STD"]
    out["BB_WIDTH_PCT"] = (out["BB_UPPER"] - out["BB_LOWER"]) / close * 100
    out["BB_POSITION"] = (close - out["BB_LOWER"]) / (out["BB_UPPER"] - out["BB_LOWER"])

    obv_direction = np.sign(close.diff()).fillna(0)
    out["OBV"] = (obv_direction * volume).cumsum()
    out["OBV_MA20"] = out["OBV"].rolling(20).mean()

    money_flow_multiplier = ((close - low) - (high - close)) / (high - low).replace(0, np.nan)
    money_flow_volume = money_flow_multiplier.fillna(0) * volume
    out["CMF20"] = money_flow_volume.rolling(20).sum() / volume.rolling(20).sum().replace(0, np.nan)

    out["VOL_MA20"] = volume.rolling(20).mean()
    out["VOL_MA50"] = volume.rolling(50).mean()
    out["VOL_RATIO_20"] = volume / out["VOL_MA20"].replace(0, np.nan)
    out["VOL_RATIO_50"] = volume / out["VOL_MA50"].replace(0, np.nan)

    out["RET_1D"] = close.pct_change(1) * 100
    out["RET_7D"] = close.pct_change(7) * 100
    out["RET_30D"] = close.pct_change(30) * 100
    out["RET_90D"] = close.pct_change(90) * 100

    out["MA50_SLOPE_20D"] = (out["MA50"] / out["MA50"].shift(20) - 1) * 100
    out["MA200_SLOPE_60D"] = (out["MA200"] / out["MA200"].shift(60) - 1) * 100

    out["RSI_SLOPE_5D"] = out["RSI14"] - out["RSI14"].shift(5)
    out["MACD_HIST_SLOPE_3D"] = out["MACD_HIST"] - out["MACD_HIST"].shift(3)

    return out


def resample_weekly(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return pd.DataFrame()

    weekly = pd.DataFrame()
    weekly["Open"] = df["Open"].resample("W-FRI").first()
    weekly["High"] = df["High"].resample("W-FRI").max()
    weekly["Low"] = df["Low"].resample("W-FRI").min()
    weekly["Close"] = df["Close"].resample("W-FRI").last()
    weekly["Volume"] = df["Volume"].resample("W-FRI").sum()
    weekly = weekly.dropna(subset=["Open", "High", "Low", "Close"])
    return add_indicators(weekly)


# =========================
# Swing, struttura, candele
# =========================

def find_pivots(df: pd.DataFrame, lookback: int = 140, pivot: int = 3):
    recent = df.tail(lookback).copy()

    highs = []
    lows = []

    if len(recent) < pivot * 2 + 5:
        return highs, lows

    for i in range(pivot, len(recent) - pivot):
        window = recent.iloc[i - pivot : i + pivot + 1]
        row = recent.iloc[i]
        date = recent.index[i]

        if row["High"] >= window["High"].max():
            highs.append((date, float(row["High"])))

        if row["Low"] <= window["Low"].min():
            lows.append((date, float(row["Low"])))

    return highs, lows


def get_structure(df: pd.DataFrame):
    highs, lows = find_pivots(df, lookback=160, pivot=3)

    structure = "RANGE / STRUTTURA NON CHIARA"
    score = 0

    last_highs = highs[-3:]
    last_lows = lows[-3:]

    if len(last_highs) >= 2 and len(last_lows) >= 2:
        h1 = last_highs[-2][1]
        h2 = last_highs[-1][1]
        l1 = last_lows[-2][1]
        l2 = last_lows[-1][1]

        if h2 > h1 and l2 > l1:
            structure = "MASSIMI E MINIMI CRESCENTI"
            score = 2
        elif h2 < h1 and l2 < l1:
            structure = "MASSIMI E MINIMI DECRESCENTI"
            score = -2
        elif h2 > h1 and l2 < l1:
            structure = "VOLATILITÀ IN ESPANSIONE"
            score = 0
        elif h2 < h1 and l2 > l1:
            structure = "COMPRESSIONE / TRIANGOLO POSSIBILE"
            score = 0

    close = float(df["Close"].iloc[-1])

    pivot_lows_below = [v for _, v in lows if v < close]
    pivot_highs_above = [v for _, v in highs if v > close]

    support = max(pivot_lows_below) if pivot_lows_below else float(df["Low"].tail(60).min())
    resistance = min(pivot_highs_above) if pivot_highs_above else float(df["High"].tail(60).max())

    return {
        "structure": structure,
        "structure_score": score,
        "support": support,
        "resistance": resistance,
        "pivot_highs": highs,
        "pivot_lows": lows,
    }


def breakout_breakdown_state(df: pd.DataFrame):
    if len(df) < 80:
        return {
            "breakout": False,
            "breakdown": False,
            "breakout_level": np.nan,
            "breakdown_level": np.nan,
            "volume_confirmed": False,
        }

    recent_ex_last = df.iloc[-65:-3]

    breakout_level = float(recent_ex_last["High"].max())
    breakdown_level = float(recent_ex_last["Low"].min())

    last = df.iloc[-1]

    close = float(last["Close"])
    vol_ratio = safe_float(last.get("VOL_RATIO_20"))

    breakout = close > breakout_level * 1.005
    breakdown = close < breakdown_level * 0.995
    volume_confirmed = bool(vol_ratio is not None and not pd.isna(vol_ratio) and vol_ratio >= 1.20)

    return {
        "breakout": breakout,
        "breakdown": breakdown,
        "breakout_level": breakout_level,
        "breakdown_level": breakdown_level,
        "volume_confirmed": volume_confirmed,
        "vol_ratio": vol_ratio,
    }


def candle_patterns(df: pd.DataFrame):
    if len(df) < 3:
        return {
            "pattern": "n/a",
            "score": 0,
        }

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
        return {"pattern": "Bullish engulfing", "score": 1}
    if hammer:
        return {"pattern": "Hammer / rejection basso", "score": 1}
    if bearish_engulfing:
        return {"pattern": "Bearish engulfing", "score": -1}
    if shooting_star:
        return {"pattern": "Shooting star / rejection alto", "score": -1}
    if doji:
        return {"pattern": "Doji / indecisione", "score": 0}

    return {"pattern": "Nessuna candela forte", "score": 0}


# =========================
# Stage analysis / Wyckoff
# =========================

def stage_analysis(weekly: pd.DataFrame):
    if weekly.empty or len(weekly) < 40:
        return {
            "stage": "UNKNOWN",
            "score": 0,
            "detail": "Dati weekly insufficienti.",
        }

    w = weekly.copy()
    w["W_MA30"] = w["Close"].rolling(30).mean()
    w["W_MA30_SLOPE_10W"] = (w["W_MA30"] / w["W_MA30"].shift(10) - 1) * 100

    last = w.iloc[-1]
    close = safe_float(last["Close"])
    ma30 = safe_float(last["W_MA30"])
    slope = safe_float(last["W_MA30_SLOPE_10W"])

    if pd.isna(ma30) or pd.isna(slope):
        return {
            "stage": "UNKNOWN",
            "score": 0,
            "detail": "Media weekly 30 non ancora disponibile.",
        }

    if close > ma30 and slope > 2:
        return {
            "stage": "STAGE 2 / MARKUP",
            "score": 2,
            "detail": "Prezzo sopra MA30 weekly con MA30 in salita.",
        }

    if close < ma30 and slope < -2:
        return {
            "stage": "STAGE 4 / MARKDOWN",
            "score": -2,
            "detail": "Prezzo sotto MA30 weekly con MA30 in discesa.",
        }

    if close < ma30 and abs(slope) <= 2:
        return {
            "stage": "STAGE 1 / ACCUMULO POSSIBILE",
            "score": 0,
            "detail": "Prezzo sotto MA30 weekly ma pendenza non chiaramente negativa.",
        }

    if close > ma30 and slope <= 2:
        return {
            "stage": "STAGE 3 / DISTRIBUZIONE O PAUSA",
            "score": -1,
            "detail": "Prezzo sopra MA30 weekly ma pendenza debole o piatta.",
        }

    return {
        "stage": "MISTO",
        "score": 0,
        "detail": "Stage non pulito.",
    }


def wyckoff_simple(df: pd.DataFrame):
    if len(df) < 140:
        return {
            "phase": "UNKNOWN",
            "score": 0,
            "detail": "Dati insufficienti.",
        }

    last = df.iloc[-1]
    close = safe_float(last["Close"])
    rsi = safe_float(last["RSI14"])
    cmf = safe_float(last["CMF20"])

    lookback = df.tail(120)
    range_low = float(lookback["Low"].min())
    range_high = float(lookback["High"].max())
    range_pos = (close - range_low) / max(range_high - range_low, 1e-12)

    recent_low_20 = float(df["Low"].tail(20).min())
    previous_low_100 = float(df["Low"].iloc[-120:-20].min())

    spring_candidate = (
        recent_low_20 < previous_low_100 * 0.99
        and close > previous_low_100
        and rsi is not None
        and not pd.isna(rsi)
        and rsi > 40
    )

    sos_candidate = (
        range_pos > 0.65
        and cmf is not None
        and not pd.isna(cmf)
        and cmf > 0.03
        and close > df["MA50"].iloc[-1]
    )

    distribution_candidate = (
        range_pos > 0.75
        and cmf is not None
        and not pd.isna(cmf)
        and cmf < -0.03
    )

    markdown_candidate = (
        range_pos < 0.35
        and close < df["MA50"].iloc[-1]
        and close < df["MA200"].iloc[-1]
    )

    if spring_candidate:
        return {
            "phase": "SPRING / TEST POSSIBILE",
            "score": 1,
            "detail": "Ha bucato un minimo importante e ha recuperato: possibile spring, da confermare.",
            "range_position": range_pos,
        }

    if sos_candidate:
        return {
            "phase": "SIGN OF STRENGTH POSSIBILE",
            "score": 2,
            "detail": "Prezzo nella parte alta del range con flusso volume positivo.",
            "range_position": range_pos,
        }

    if distribution_candidate:
        return {
            "phase": "DISTRIBUZIONE POSSIBILE",
            "score": -2,
            "detail": "Prezzo alto nel range ma CMF negativo: possibile distribuzione.",
            "range_position": range_pos,
        }

    if markdown_candidate:
        return {
            "phase": "MARKDOWN / DEBOLEZZA",
            "score": -2,
            "detail": "Prezzo basso nel range e sotto medie principali.",
            "range_position": range_pos,
        }

    if range_pos < 0.45:
        return {
            "phase": "ACCUMULO POSSIBILE / RANGE BASSO",
            "score": 0,
            "detail": "Prezzo nella metà bassa del range, ma senza spring confermato.",
            "range_position": range_pos,
        }

    return {
        "phase": "RANGE / FASE NON CHIARA",
        "score": 0,
        "detail": "Nessuna fase Wyckoff pulita.",
        "range_position": range_pos,
    }


# =========================
# Scoring classico
# =========================

def score_trend(df: pd.DataFrame, weekly: pd.DataFrame):
    last = df.iloc[-1]

    close = safe_float(last["Close"])
    ma20 = safe_float(last["MA20"])
    ma50 = safe_float(last["MA50"])
    ma100 = safe_float(last["MA100"])
    ma200 = safe_float(last["MA200"])
    ma50_slope = safe_float(last["MA50_SLOPE_20D"])
    ma200_slope = safe_float(last["MA200_SLOPE_60D"])

    score = 0
    notes = []

    if not pd.isna(ma200):
        if close > ma200:
            score += 1
            notes.append("prezzo sopra MA200 daily")
        else:
            score -= 1
            notes.append("prezzo sotto MA200 daily")

    if not any(pd.isna(x) for x in [ma20, ma50, ma100, ma200]):
        if close > ma20 > ma50 > ma100 > ma200:
            score += 2
            notes.append("medie daily allineate rialziste")
        elif close < ma20 < ma50 < ma100 < ma200:
            score -= 2
            notes.append("medie daily allineate ribassiste")
        elif close > ma20 and ma20 > ma50:
            score += 1
            notes.append("breve termine sopra MA20/MA50")
        elif close < ma20 and ma20 < ma50:
            score -= 1
            notes.append("breve termine sotto MA20/MA50")

    if not pd.isna(ma50_slope):
        if ma50_slope > 3:
            score += 1
            notes.append("MA50 daily in salita")
        elif ma50_slope < -3:
            score -= 1
            notes.append("MA50 daily in discesa")

    if not pd.isna(ma200_slope):
        if ma200_slope > 2:
            score += 1
            notes.append("MA200 daily in salita")
        elif ma200_slope < -2:
            score -= 1
            notes.append("MA200 daily in discesa")

    stage = stage_analysis(weekly)
    score += stage["score"]
    notes.append(stage["stage"])

    score = clamp(score, -4, 4)

    return {
        "score": score,
        "detail": "; ".join(notes) if notes else "n/a",
        "stage": stage,
    }


def score_momentum(df: pd.DataFrame):
    last = df.iloc[-1]

    rsi = safe_float(last["RSI14"])
    rsi_slope = safe_float(last["RSI_SLOPE_5D"])
    macd = safe_float(last["MACD"])
    macd_signal = safe_float(last["MACD_SIGNAL"])
    macd_hist = safe_float(last["MACD_HIST"])
    macd_hist_slope = safe_float(last["MACD_HIST_SLOPE_3D"])

    score = 0
    notes = []

    if not pd.isna(rsi):
        if 50 <= rsi <= 68:
            score += 1
            notes.append(f"RSI sano {rsi:.1f}")
        elif rsi > 70:
            score -= 1
            notes.append(f"RSI alto {rsi:.1f}")
        elif rsi < 38:
            score -= 1
            notes.append(f"RSI debole {rsi:.1f}")
        else:
            notes.append(f"RSI neutrale {rsi:.1f}")

    if not pd.isna(rsi_slope):
        if rsi_slope > 3:
            score += 1
            notes.append("RSI in miglioramento")
        elif rsi_slope < -3:
            score -= 1
            notes.append("RSI in peggioramento")

    if not any(pd.isna(x) for x in [macd, macd_signal, macd_hist]):
        if macd > macd_signal and macd_hist > 0:
            score += 1
            notes.append("MACD sopra signal")
        elif macd < macd_signal and macd_hist < 0:
            score -= 1
            notes.append("MACD sotto signal")

    if not pd.isna(macd_hist_slope):
        if macd_hist_slope > 0:
            score += 1
            notes.append("istogramma MACD in miglioramento")
        elif macd_hist_slope < 0:
            score -= 1
            notes.append("istogramma MACD in peggioramento")

    score = clamp(score, -3, 3)

    return {
        "score": score,
        "detail": "; ".join(notes) if notes else "n/a",
    }


def score_volume(df: pd.DataFrame):
    last = df.iloc[-1]

    obv = safe_float(last["OBV"])
    obv_ma20 = safe_float(last["OBV_MA20"])
    cmf = safe_float(last["CMF20"])
    vol_ratio = safe_float(last["VOL_RATIO_20"])
    ret_1d = safe_float(last["RET_1D"])

    score = 0
    notes = []

    if not any(pd.isna(x) for x in [obv, obv_ma20]):
        if obv > obv_ma20:
            score += 1
            notes.append("OBV sopra media")
        else:
            score -= 1
            notes.append("OBV sotto media")

    if not pd.isna(cmf):
        if cmf > 0.05:
            score += 1
            notes.append(f"CMF positivo {cmf:.2f}")
        elif cmf < -0.05:
            score -= 1
            notes.append(f"CMF negativo {cmf:.2f}")
        else:
            notes.append(f"CMF neutrale {cmf:.2f}")

    if not any(pd.isna(x) for x in [vol_ratio, ret_1d]):
        if ret_1d > 2 and vol_ratio > 1.2:
            score += 1
            notes.append("rialzo con volume sopra media")
        elif ret_1d < -2 and vol_ratio > 1.2:
            score -= 1
            notes.append("discesa con volume sopra media")
        else:
            notes.append(f"volume ratio {vol_ratio:.2f}")

    score = clamp(score, -3, 3)

    return {
        "score": score,
        "detail": "; ".join(notes) if notes else "n/a",
    }


def score_price_confirmation(df: pd.DataFrame):
    state = breakout_breakdown_state(df)

    score = 0

    if state["breakout"] and state["volume_confirmed"]:
        score = 3
        detail = "Breakout sopra resistenza 60g con volume."
    elif state["breakout"]:
        score = 1
        detail = "Breakout sopra resistenza 60g, ma volume non forte."
    elif state["breakdown"] and state["volume_confirmed"]:
        score = -3
        detail = "Breakdown sotto supporto 60g con volume."
    elif state["breakdown"]:
        score = -1
        detail = "Breakdown sotto supporto 60g, ma volume non forte."
    else:
        detail = "Nessuna rottura confermata di prezzo."

    return {
        "score": score,
        "detail": detail,
        "state": state,
    }


# CLASSIC_LOCAL_VOLATILITY_LABEL_PATCH_V1
# Questa funzione misura solo volatilità ATR e distanza da supporto/resistenza.
# Non rappresenta il rischio operativo complessivo dell'asset o della leva.
def risk_label(asset: str, atr_pct, close, support, resistance):
    if atr_pct is None or pd.isna(atr_pct):
        return "n/a", "ATR non disponibile."

    atr_pct = float(atr_pct)

    support_distance = None
    resistance_distance = None

    if support is not None and not pd.isna(support) and close:
        support_distance = (float(close) / float(support) - 1) * 100

    if resistance is not None and not pd.isna(resistance) and close:
        resistance_distance = (float(resistance) / float(close) - 1) * 100

    if asset == "BTC":
        high_risk_atr = 5.0
        extreme_risk_atr = 8.0
    else:
        high_risk_atr = 8.0
        extreme_risk_atr = 13.0

    if atr_pct >= extreme_risk_atr:
        risk = "MOLTO ALTO"
    elif atr_pct >= high_risk_atr:
        risk = "ALTO"
    elif atr_pct >= high_risk_atr * 0.55:
        risk = "MEDIO"
    else:
        risk = "BASSO"

    detail_parts = [f"ATR14 {fmt_pct_plain(atr_pct)}"]

    if support_distance is not None:
        detail_parts.append(f"distanza supporto {fmt_pct_plain(support_distance)}")

    if resistance_distance is not None:
        detail_parts.append(f"distanza resistenza {fmt_pct_plain(resistance_distance)}")

    return risk, "; ".join(detail_parts)


def verdict_from_score(score: int, price_confirmation_score: int) -> str:
    if score >= 8 and price_confirmation_score >= 1:
        return "CONFERMATO RIALZISTA"
    if score >= 5:
        return "COSTRUTTIVO / CONFERMA PARZIALE"
    if score >= 2:
        return "ANTICIPATO / COSTRUTTIVO MA NON CONFERMATO"
    if score >= -1:
        return "NEUTRALE / MISTO"
    if score >= -4:
        return "DEBOLE / NON CONFERMATO"
    if score <= -8 and price_confirmation_score <= -1:
        return "CONFERMATO RIBASSISTA"
    return "RIBASSISTA / FRAGILE"


def action_from_result(asset: str, score: int, verdict: str, risk: str) -> str:
    if asset == "BTC":
        if score >= 5:
            return "SPOT OK / LONG SOLO PRUDENTE SU CONFERMA"
        if score >= 0:
            return "HOLD / ASPETTA ROTTURA RESISTENZA"
        return "RIDUCI RISCHIO / NO LONG A LEVA"

    if asset == "SOL":
        if score >= 5:
            return "TRANCHE PICCOLE / NO LEVA FINCHÉ NON ROMPE CONFERME"
        if score >= 0:
            return "HOLD LEGGERO / ATTESA CONFERME"
        return "NON INSEGUIRE / TAKE PROFIT SU SPIKE"

    if asset == "DOGE":
        if score >= 5:
            return "SOLO TRADING VELOCE / NO LEVA AGGRESSIVA"
        if score >= 0:
            return "STAI ALLA FINESTRA"
        return "NO LONG / SHORT SOLO DOPO SPIKE E REJECTION"

    return "n/a"


def analyze_asset(asset: str, ticker: str):
    daily = download_ohlcv(ticker, period="1200d", interval="1d")
    if daily.empty or len(daily) < 260:
        return {
            "asset": asset,
            "ticker": ticker,
            "ok": False,
            "error": "Dati insufficienti da Yahoo Finance.",
        }

    daily = add_indicators(daily)
    weekly = resample_weekly(daily)

    daily = daily.dropna(subset=["Close"])
    last = daily.iloc[-1]
    close = safe_float(last["Close"])

    structure = get_structure(daily)
    trend = score_trend(daily, weekly)
    momentum = score_momentum(daily)
    volume = score_volume(daily)
    price_confirmation = score_price_confirmation(daily)
    candles = candle_patterns(daily)
    wyckoff = wyckoff_simple(daily)

    atr_pct = safe_float(last["ATR14_PCT"])
    risk, risk_detail = risk_label(
        asset,
        atr_pct,
        close,
        structure["support"],
        structure["resistance"],
    )

    raw_score = (
        trend["score"]
        + structure["structure_score"]
        + momentum["score"]
        + volume["score"]
        + price_confirmation["score"]
        + candles["score"]
        + wyckoff["score"]
    )

    score = clamp(raw_score, -12, 12)
    verdict = verdict_from_score(score, price_confirmation["score"])
    action = action_from_result(asset, score, verdict, risk)

    breakout_level = price_confirmation["state"].get("breakout_level")
    breakdown_level = price_confirmation["state"].get("breakdown_level")
    vol_ratio = price_confirmation["state"].get("vol_ratio")

    return {
        "asset": asset,
        "ticker": ticker,
        "ok": True,
        "date": daily.index[-1].strftime("%Y-%m-%d"),
        "price": close,
        "score": score,
        "raw_score": raw_score,
        "verdict": verdict,
        "action": action,
        "risk": risk,
        "risk_detail": risk_detail,
        "trend_score": trend["score"],
        "trend_detail": trend["detail"],
        "stage": trend["stage"]["stage"],
        "stage_detail": trend["stage"]["detail"],
        "structure_score": structure["structure_score"],
        "structure": structure["structure"],
        "support": structure["support"],
        "resistance": structure["resistance"],
        "momentum_score": momentum["score"],
        "momentum_detail": momentum["detail"],
        "volume_score": volume["score"],
        "volume_detail": volume["detail"],
        "price_confirmation_score": price_confirmation["score"],
        "price_confirmation_detail": price_confirmation["detail"],
        "breakout_level": breakout_level,
        "breakdown_level": breakdown_level,
        "breakout": price_confirmation["state"].get("breakout"),
        "breakdown": price_confirmation["state"].get("breakdown"),
        "volume_confirmed": price_confirmation["state"].get("volume_confirmed"),
        "vol_ratio": vol_ratio,
        "candle_score": candles["score"],
        "candle_pattern": candles["pattern"],
        "wyckoff_score": wyckoff["score"],
        "wyckoff_phase": wyckoff["phase"],
        "wyckoff_detail": wyckoff["detail"],
        "range_position": wyckoff.get("range_position", np.nan),
        "rsi14": safe_float(last["RSI14"]),
        "macd_hist": safe_float(last["MACD_HIST"]),
        "cmf20": safe_float(last["CMF20"]),
        "obv": safe_float(last["OBV"]),
        "atr14_pct": atr_pct,
        "bb_width_pct": safe_float(last["BB_WIDTH_PCT"]),
        "bb_position": safe_float(last["BB_POSITION"]),
        "ma20": safe_float(last["MA20"]),
        "ma50": safe_float(last["MA50"]),
        "ma100": safe_float(last["MA100"]),
        "ma200": safe_float(last["MA200"]),
        "ma50_slope_20d": safe_float(last["MA50_SLOPE_20D"]),
        "ma200_slope_60d": safe_float(last["MA200_SLOPE_60D"]),
        "ret_30d": safe_float(last["RET_30D"]),
        "ret_90d": safe_float(last["RET_90D"]),
    }


# =========================
# Report
# =========================

def build_report(results):
    generated = now_utc_str()

    summary_rows = []
    score_rows = []
    level_rows = []

    for r in results:
        asset = r["asset"]

        if not r.get("ok"):
            summary_rows.append(
                [
                    asset,
                    "n/a",
                    "ERRORE",
                    r.get("error", "n/a"),
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
                fmt_money(asset, r["price"]),
                fmt_signed(r["score"]),
                r["verdict"],
                r["stage"],
                r["structure"],
                r["wyckoff_phase"],
                r["risk"],
                r["action"],
            ]
        )

        score_rows.append(
            [
                asset,
                fmt_signed(r["trend_score"]),
                fmt_signed(r["structure_score"]),
                fmt_signed(r["momentum_score"]),
                fmt_signed(r["volume_score"]),
                fmt_signed(r["price_confirmation_score"]),
                fmt_signed(r["candle_score"]),
                fmt_signed(r["wyckoff_score"]),
                fmt_signed(r["score"]),
            ]
        )

        level_rows.append(
            [
                asset,
                fmt_money(asset, r["support"]),
                fmt_money(asset, r["resistance"]),
                fmt_money(asset, r["breakout_level"]),
                fmt_money(asset, r["breakdown_level"]),
                fmt_pct_plain(r["atr14_pct"]),
                fmt_pct_plain(r["ret_30d"]),
                fmt_pct_plain(r["ret_90d"]),
            ]
        )

    lines = []

    lines.append("# Classic technical confirmation report")
    lines.append("")
    lines.append(f"Generato: {generated}")
    lines.append("")
    lines.append(
        "Questo modulo controlla se il setup è confermato secondo analisi tecnica classica. "
        "Non sostituisce lo scanner frattale: serve come filtro di conferma."
    )
    lines.append("")
    lines.append("Cosa controlla:")
    lines.append("")
    lines.append("- trend daily e weekly")
    lines.append("- stage analysis stile Weinstein")
    lines.append("- struttura massimi/minimi")
    lines.append("- breakout o breakdown con volume")
    lines.append("- RSI e MACD")
    lines.append("- OBV, CMF e volume relativo")
    lines.append("- candele principali")
    lines.append("- Wyckoff semplificato")
    lines.append("- volatilità tecnica locale tramite ATR e distanza dai livelli")
    lines.append("")
    lines.append("## Sintesi")
    lines.append("")
    lines.append(
        md_table(
            [
                "Asset",
                "Prezzo",
                "Score",
                "Verdetto",
                "Stage",
                "Struttura",
                "Wyckoff",
                "Volatilità locale",
                "Azione",
            ],
            summary_rows,
        )
    )
    lines.append("")
    lines.append("## Punteggi per area")
    lines.append("")
    lines.append(
        md_table(
            [
                "Asset",
                "Trend",
                "Struttura",
                "Momentum",
                "Volume",
                "Prezzo",
                "Candela",
                "Wyckoff",
                "Totale",
            ],
            score_rows,
        )
    )
    lines.append("")
    lines.append("## Livelli tecnici")
    lines.append("")
    lines.append(
        md_table(
            [
                "Asset",
                "Supporto",
                "Resistenza",
                "Breakout 60g",
                "Breakdown 60g",
                "ATR14",
                "Rendimento 30g",
                "Rendimento 90g",
            ],
            level_rows,
        )
    )
    lines.append("")
    lines.append("## Lettura dettagliata")

    for r in results:
        asset = r["asset"]
        lines.append("")
        lines.append(f"### {asset}")

        if not r.get("ok"):
            lines.append("")
            lines.append(f"Errore: {r.get('error', 'n/a')}")
            continue

        lines.append("")
        lines.append(f"- Prezzo: **{fmt_money(asset, r['price'])}**")
        lines.append(f"- Score classico: **{fmt_signed(r['score'])} / 12**")
        lines.append(f"- Verdetto: **{r['verdict']}**")
        lines.append(f"- Azione coerente: **{r['action']}**")
        lines.append(f"- Volatilità tecnica locale: **{r['risk']}** — {r['risk_detail']}")
        lines.append("")
        lines.append("Dettaglio:")
        lines.append("")
        lines.append(f"- Trend: **{fmt_signed(r['trend_score'])}** — {r['trend_detail']}")
        lines.append(f"- Stage weekly: **{r['stage']}** — {r['stage_detail']}")
        lines.append(f"- Struttura: **{fmt_signed(r['structure_score'])}** — {r['structure']}")
        lines.append(f"- Momentum: **{fmt_signed(r['momentum_score'])}** — {r['momentum_detail']}")
        lines.append(f"- Volume: **{fmt_signed(r['volume_score'])}** — {r['volume_detail']}")
        lines.append(f"- Conferma prezzo: **{fmt_signed(r['price_confirmation_score'])}** — {r['price_confirmation_detail']}")
        lines.append(f"- Candela: **{fmt_signed(r['candle_score'])}** — {r['candle_pattern']}")
        lines.append(f"- Wyckoff: **{fmt_signed(r['wyckoff_score'])}** — {r['wyckoff_phase']}. {r['wyckoff_detail']}")
        lines.append("")
        lines.append("Indicatori principali:")
        lines.append("")
        lines.append(
            md_table(
                ["Indicatore", "Valore"],
                [
                    ["RSI14", f"{r['rsi14']:.2f}" if not pd.isna(r["rsi14"]) else "n/a"],
                    ["MACD histogram", f"{r['macd_hist']:.5f}" if not pd.isna(r["macd_hist"]) else "n/a"],
                    ["CMF20", f"{r['cmf20']:.3f}" if not pd.isna(r["cmf20"]) else "n/a"],
                    ["Volume ratio 20", f"{r['vol_ratio']:.2f}" if r["vol_ratio"] is not None and not pd.isna(r["vol_ratio"]) else "n/a"],
                    ["MA20", fmt_money(asset, r["ma20"])],
                    ["MA50", fmt_money(asset, r["ma50"])],
                    ["MA100", fmt_money(asset, r["ma100"])],
                    ["MA200", fmt_money(asset, r["ma200"])],
                    ["Pendenza MA50 20g", fmt_pct(r["ma50_slope_20d"])],
                    ["Pendenza MA200 60g", fmt_pct(r["ma200_slope_60d"])],
                    ["Bollinger width", fmt_pct_plain(r["bb_width_pct"])],
                    ["Bollinger position", f"{r['bb_position']:.2f}" if not pd.isna(r["bb_position"]) else "n/a"],
                ],
            )
        )

    lines.append("")
    lines.append("## Come leggere lo score")
    lines.append("")
    lines.append("- **+8 a +12**: conferma tecnica rialzista forte.")
    lines.append("- **+5 a +7**: setup costruttivo, ma può mancare ancora una rottura pulita.")
    lines.append("- **+2 a +4**: setup anticipato, interessante ma non confermato.")
    lines.append("- **-1 a +1**: neutrale / misto.")
    lines.append("- **-4 a -2**: debole / non confermato.")
    lines.append("- **-8 o meno**: conferma tecnica ribassista.")
    lines.append("")
    lines.append(
        "Nota: questo modulo deve pesare poco nel Global finché non viene verificato dalla calibrazione. "
        "La funzione principale è evitare di confondere un contesto interessante con una conferma vera."
    )

    return "\n".join(lines).rstrip() + "\n"


def write_metrics_csv(results):
    fieldnames = [
        "generated_utc",
        "asset",
        "ticker",
        "date",
        "price",
        "score",
        "verdict",
        "action",
        "risk",
        "trend_score",
        "stage",
        "structure_score",
        "structure",
        "support",
        "resistance",
        "momentum_score",
        "volume_score",
        "price_confirmation_score",
        "breakout",
        "breakdown",
        "breakout_level",
        "breakdown_level",
        "volume_confirmed",
        "candle_score",
        "candle_pattern",
        "wyckoff_score",
        "wyckoff_phase",
        "rsi14",
        "macd_hist",
        "cmf20",
        "vol_ratio",
        "atr14_pct",
        "bb_width_pct",
        "bb_position",
        "ma20",
        "ma50",
        "ma100",
        "ma200",
        "ma50_slope_20d",
        "ma200_slope_60d",
        "ret_30d",
        "ret_90d",
    ]

    generated = datetime.now(timezone.utc).isoformat()

    rows = []

    for r in results:
        if not r.get("ok"):
            rows.append(
                {
                    "generated_utc": generated,
                    "asset": r.get("asset"),
                    "ticker": r.get("ticker"),
                    "date": "",
                    "price": "",
                    "score": "",
                    "verdict": "ERROR",
                    "action": r.get("error", ""),
                    "risk": "",
                }
            )
            continue

        row = {k: r.get(k, "") for k in fieldnames}
        row["generated_utc"] = generated
        rows.append(row)

    METRICS_CSV_PATH.parent.mkdir(parents=True, exist_ok=True)

    with METRICS_CSV_PATH.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main():
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    results = []

    for asset, ticker in ASSETS.items():
        result = analyze_asset(asset, ticker)
        results.append(result)

    report_md = build_report(results)

    write_text(REPORT_PATH, report_md)
    write_metrics_csv(results)

    latest_text = read_text(LATEST_REPORT_PATH)
    if latest_text:
        latest_updated = replace_or_insert_block(latest_text, report_md)
        write_text(LATEST_REPORT_PATH, latest_updated)
    else:
        write_text(LATEST_REPORT_PATH, f"{START_MARKER}\n{report_md}{END_MARKER}\n")

    print(f"Classic technical confirmation report scritto in: {REPORT_PATH}")
    print(f"Metriche scritte in: {METRICS_CSV_PATH}")


if __name__ == "__main__":
    main()
