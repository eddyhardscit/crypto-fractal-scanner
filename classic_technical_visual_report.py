import csv
import math
import re
from datetime import datetime, timezone
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import yfinance as yf


REPORTS_DIR = Path("reports")
LATEST_REPORT_PATH = REPORTS_DIR / "latest_report.md"

REPORT_PATH = REPORTS_DIR / "classic_technical_visual_report.md"
METRICS_CSV_PATH = REPORTS_DIR / "classic_technical_visual_metrics.csv"

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


# =========================
# Utility
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


def fmt_signed(value) -> str:
    if value is None or pd.isna(value):
        return "n/a"
    v = float(value)
    if v > 0:
        return f"+{v:.2f}".replace(".", ",")
    return f"{v:.2f}".replace(".", ",")


def fmt_pct(value, decimals: int = 2) -> str:
    if value is None or pd.isna(value):
        return "n/a"
    return f"{float(value):+.{decimals}f}%".replace(".", ",")


def fmt_pct_plain(value, decimals: int = 2) -> str:
    if value is None or pd.isna(value):
        return "n/a"
    return f"{float(value):.{decimals}f}%".replace(".", ",")


def fmt_price(asset: str, value) -> str:
    if value is None or pd.isna(value):
        return "n/a"

    v = float(value)

    if asset == "BTC":
        return f"{v:,.0f}".replace(",", ".")

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


def safe_float(value):
    try:
        if value is None:
            return np.nan
        if pd.isna(value):
            return np.nan
        return float(value)
    except Exception:
        return np.nan


# =========================
# Dati e indicatori
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
    df["Volume"] = df["Volume"].fillna(0)

    df.index = pd.to_datetime(df.index).tz_localize(None)
    df = df.sort_index()

    return df


def download_ohlcv(ticker: str, period: str = "900d", interval: str = "1d") -> pd.DataFrame:
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

    delta = close.diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    avg_gain = gain.ewm(alpha=1 / 14, adjust=False).mean()
    avg_loss = loss.ewm(alpha=1 / 14, adjust=False).mean()
    rs = avg_gain / avg_loss.replace(0, np.nan)
    out["RSI14"] = 100 - (100 / (1 + rs))

    out["VOL_MA20"] = volume.rolling(20).mean()
    out["VOL_RATIO_20"] = volume / out["VOL_MA20"].replace(0, np.nan)

    out["EMA12"] = close.ewm(span=12, adjust=False).mean()
    out["EMA26"] = close.ewm(span=26, adjust=False).mean()
    out["MACD"] = out["EMA12"] - out["EMA26"]
    out["MACD_SIGNAL"] = out["MACD"].ewm(span=9, adjust=False).mean()
    out["MACD_HIST"] = out["MACD"] - out["MACD_SIGNAL"]

    tr1 = high - low
    tr2 = (high - close.shift(1)).abs()
    tr3 = (low - close.shift(1)).abs()
    tr = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)
    out["ATR14"] = tr.rolling(14).mean()
    out["ATR14_PCT"] = out["ATR14"] / close * 100

    out["RET_30D"] = close.pct_change(30) * 100
    out["RET_90D"] = close.pct_change(90) * 100

    return out


# =========================
# Pivot e pattern
# =========================

def find_pivots(df: pd.DataFrame, lookback: int = 220, pivot: int = 4):
    recent = df.tail(lookback).copy()

    highs = []
    lows = []

    if len(recent) < pivot * 2 + 10:
        return highs, lows

    for i in range(pivot, len(recent) - pivot):
        window = recent.iloc[i - pivot : i + pivot + 1]
        row = recent.iloc[i]
        date = recent.index[i]

        if row["High"] >= window["High"].max():
            highs.append(
                {
                    "date": date,
                    "price": float(row["High"]),
                    "kind": "HIGH",
                    "i": df.index.get_loc(date),
                }
            )

        if row["Low"] <= window["Low"].min():
            lows.append(
                {
                    "date": date,
                    "price": float(row["Low"]),
                    "kind": "LOW",
                    "i": df.index.get_loc(date),
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


def pct_diff(a, b) -> float:
    if a is None or b is None:
        return np.nan
    denom = max(abs(a), abs(b), 1e-12)
    return abs(a - b) / denom


def find_between_pivots(pivots, i1, i2, kind=None):
    out = []
    for p in pivots:
        if i1 < p["i"] < i2:
            if kind is None or p["kind"] == kind:
                out.append(p)
    return out


def detect_double_bottom(df: pd.DataFrame, highs, lows, asset: str):
    tol = tolerance_for_asset(asset)
    close = float(df["Close"].iloc[-1])

    candidates = []

    last_lows = lows[-8:]

    for a in range(len(last_lows)):
        for b in range(a + 1, len(last_lows)):
            p1 = last_lows[a]
            p2 = last_lows[b]

            if p2["i"] - p1["i"] < 10:
                continue

            if pct_diff(p1["price"], p2["price"]) > tol:
                continue

            between_highs = find_between_pivots(highs, p1["i"], p2["i"], "HIGH")
            if not between_highs:
                continue

            neckline = max(h["price"] for h in between_highs)
            confirmed = close > neckline * 1.005

            candidates.append(
                {
                    "name": "Doppio minimo",
                    "family": "rialzista",
                    "state": "CONFERMATO" if confirmed else "CANDIDATO",
                    "score": 2 if confirmed else 1,
                    "neckline": neckline,
                    "points": [p1, p2],
                    "extra_points": between_highs,
                    "detail": (
                        f"Due minimi simili a {fmt_money(asset, p1['price'])} e "
                        f"{fmt_money(asset, p2['price'])}. Neckline circa "
                        f"{fmt_money(asset, neckline)}."
                    ),
                }
            )

    if not candidates:
        return None

    candidates.sort(key=lambda x: (x["score"], x["points"][-1]["i"]), reverse=True)
    return candidates[0]


def detect_double_top(df: pd.DataFrame, highs, lows, asset: str):
    tol = tolerance_for_asset(asset)
    close = float(df["Close"].iloc[-1])

    candidates = []

    last_highs = highs[-8:]

    for a in range(len(last_highs)):
        for b in range(a + 1, len(last_highs)):
            p1 = last_highs[a]
            p2 = last_highs[b]

            if p2["i"] - p1["i"] < 10:
                continue

            if pct_diff(p1["price"], p2["price"]) > tol:
                continue

            between_lows = find_between_pivots(lows, p1["i"], p2["i"], "LOW")
            if not between_lows:
                continue

            neckline = min(l["price"] for l in between_lows)
            confirmed = close < neckline * 0.995

            candidates.append(
                {
                    "name": "Doppio massimo",
                    "family": "ribassista",
                    "state": "CONFERMATO" if confirmed else "CANDIDATO",
                    "score": -2 if confirmed else -1,
                    "neckline": neckline,
                    "points": [p1, p2],
                    "extra_points": between_lows,
                    "detail": (
                        f"Due massimi simili a {fmt_money(asset, p1['price'])} e "
                        f"{fmt_money(asset, p2['price'])}. Neckline circa "
                        f"{fmt_money(asset, neckline)}."
                    ),
                }
            )

    if not candidates:
        return None

    candidates.sort(key=lambda x: (abs(x["score"]), x["points"][-1]["i"]), reverse=True)
    return candidates[0]


def detect_head_shoulders(df: pd.DataFrame, highs, lows, asset: str):
    tol = tolerance_for_asset(asset)
    close = float(df["Close"].iloc[-1])

    candidates = []

    last_highs = highs[-8:]

    for i in range(len(last_highs) - 2):
        left = last_highs[i]
        head = last_highs[i + 1]
        right = last_highs[i + 2]

        if not (head["price"] > left["price"] and head["price"] > right["price"]):
            continue

        shoulders_close = pct_diff(left["price"], right["price"]) <= tol * 1.5
        head_higher_enough = head["price"] > max(left["price"], right["price"]) * 1.03

        if not shoulders_close or not head_higher_enough:
            continue

        lows_left_head = find_between_pivots(lows, left["i"], head["i"], "LOW")
        lows_head_right = find_between_pivots(lows, head["i"], right["i"], "LOW")

        if not lows_left_head or not lows_head_right:
            continue

        neckline = (min(x["price"] for x in lows_left_head) + min(x["price"] for x in lows_head_right)) / 2
        confirmed = close < neckline * 0.995

        candidates.append(
            {
                "name": "Testa e spalle",
                "family": "ribassista",
                "state": "CONFERMATO" if confirmed else "CANDIDATO",
                "score": -3 if confirmed else -1,
                "neckline": neckline,
                "points": [left, head, right],
                "extra_points": lows_left_head + lows_head_right,
                "detail": (
                    f"Spalla sinistra {fmt_money(asset, left['price'])}, testa "
                    f"{fmt_money(asset, head['price'])}, spalla destra "
                    f"{fmt_money(asset, right['price'])}. Neckline circa "
                    f"{fmt_money(asset, neckline)}."
                ),
            }
        )

    if not candidates:
        return None

    candidates.sort(key=lambda x: (abs(x["score"]), x["points"][-1]["i"]), reverse=True)
    return candidates[0]


def detect_inverse_head_shoulders(df: pd.DataFrame, highs, lows, asset: str):
    tol = tolerance_for_asset(asset)
    close = float(df["Close"].iloc[-1])

    candidates = []

    last_lows = lows[-8:]

    for i in range(len(last_lows) - 2):
        left = last_lows[i]
        head = last_lows[i + 1]
        right = last_lows[i + 2]

        if not (head["price"] < left["price"] and head["price"] < right["price"]):
            continue

        shoulders_close = pct_diff(left["price"], right["price"]) <= tol * 1.5
        head_lower_enough = head["price"] < min(left["price"], right["price"]) * 0.97

        if not shoulders_close or not head_lower_enough:
            continue

        highs_left_head = find_between_pivots(highs, left["i"], head["i"], "HIGH")
        highs_head_right = find_between_pivots(highs, head["i"], right["i"], "HIGH")

        if not highs_left_head or not highs_head_right:
            continue

        neckline = (max(x["price"] for x in highs_left_head) + max(x["price"] for x in highs_head_right)) / 2
        confirmed = close > neckline * 1.005

        candidates.append(
            {
                "name": "Testa e spalle inverso",
                "family": "rialzista",
                "state": "CONFERMATO" if confirmed else "CANDIDATO",
                "score": 3 if confirmed else 1,
                "neckline": neckline,
                "points": [left, head, right],
                "extra_points": highs_left_head + highs_head_right,
                "detail": (
                    f"Spalla sinistra {fmt_money(asset, left['price'])}, testa "
                    f"{fmt_money(asset, head['price'])}, spalla destra "
                    f"{fmt_money(asset, right['price'])}. Neckline circa "
                    f"{fmt_money(asset, neckline)}."
                ),
            }
        )

    if not candidates:
        return None

    candidates.sort(key=lambda x: (x["score"], x["points"][-1]["i"]), reverse=True)
    return candidates[0]


def detect_triangle_compression(df: pd.DataFrame, highs, lows, asset: str):
    close = float(df["Close"].iloc[-1])

    if len(highs) < 3 or len(lows) < 3:
        return None

    h = highs[-3:]
    l = lows[-3:]

    highs_descending = h[-1]["price"] < h[-2]["price"] < h[-3]["price"]
    lows_ascending = l[-1]["price"] > l[-2]["price"] > l[-3]["price"]

    highs_flat = pct_diff(h[-1]["price"], h[-2]["price"]) < tolerance_for_asset(asset)
    lows_flat = pct_diff(l[-1]["price"], l[-2]["price"]) < tolerance_for_asset(asset)

    if highs_descending and lows_ascending:
        name = "Triangolo simmetrico / compressione"
        family = "neutrale"
        score = 0
        detail = "Massimi decrescenti e minimi crescenti: compressione in corso."
    elif highs_flat and lows_ascending:
        name = "Triangolo ascendente possibile"
        family = "rialzista"
        score = 1
        detail = "Resistenza quasi piatta e minimi crescenti."
    elif highs_descending and lows_flat:
        name = "Triangolo discendente possibile"
        family = "ribassista"
        score = -1
        detail = "Massimi decrescenti e supporto quasi piatto."
    else:
        return None

    neckline = None

    return {
        "name": name,
        "family": family,
        "state": "CANDIDATO",
        "score": score,
        "neckline": neckline,
        "points": h + l,
        "extra_points": [],
        "detail": detail,
    }


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
            p = detector(df, highs, lows, asset)
            if p:
                patterns.append(p)
        except Exception:
            pass

    candle, candle_score = detect_latest_candle(df)

    if patterns:
        patterns.sort(
            key=lambda x: (
                1 if x["state"] == "CONFERMATO" else 0,
                abs(x["score"]),
                max(pt["i"] for pt in x["points"]) if x.get("points") else 0,
            ),
            reverse=True,
        )
        primary = patterns[0]
    else:
        primary = {
            "name": "Nessun pattern classico pulito",
            "family": "neutrale",
            "state": "n/a",
            "score": 0,
            "neckline": np.nan,
            "points": [],
            "extra_points": [],
            "detail": "Non è stato trovato un pattern classico abbastanza pulito nel lookback usato.",
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
# Supporti/resistenze
# =========================

def support_resistance_levels(df: pd.DataFrame, highs, lows):
    close = float(df["Close"].iloc[-1])

    low_prices = [p["price"] for p in lows if p["price"] < close]
    high_prices = [p["price"] for p in highs if p["price"] > close]

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

def plot_asset(asset: str, df: pd.DataFrame, detection: dict, levels: dict) -> Path:
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
    plot_end = plot_df.index[-1]

    highs = [p for p in detection["highs"] if p["date"] >= plot_start]
    lows = [p for p in detection["lows"] if p["date"] >= plot_start]

    if highs:
        ax.scatter(
            [p["date"] for p in highs],
            [p["price"] for p in highs],
            marker="v",
            s=40,
            label="Pivot high",
            zorder=5,
        )

    if lows:
        ax.scatter(
            [p["date"] for p in lows],
            [p["price"] for p in lows],
            marker="^",
            s=40,
            label="Pivot low",
            zorder=5,
        )

    primary = detection["primary"]

    pattern_points = [p for p in primary.get("points", []) if p["date"] >= plot_start]

    if pattern_points:
        ax.plot(
            [p["date"] for p in pattern_points],
            [p["price"] for p in pattern_points],
            linewidth=2.4,
            marker="o",
            label=f"Pattern: {primary['name']}",
            zorder=6,
        )

        for p in pattern_points:
            ax.annotate(
                p["kind"],
                xy=(p["date"], p["price"]),
                xytext=(0, 10),
                textcoords="offset points",
                ha="center",
                fontsize=8,
            )

    neckline = primary.get("neckline")
    if neckline is not None and not pd.isna(neckline):
        ax.axhline(float(neckline), linewidth=1.6, linestyle="-.", label="Neckline pattern")

    title = (
        f"{asset} — {primary['name']} ({primary['state']}) | "
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
    levels = support_resistance_levels(df, detection["highs"], detection["lows"])
    image_path = plot_asset(asset, df, detection, levels)

    last = df.iloc[-1]
    primary = detection["primary"]

    close = float(last["Close"])
    atr_pct = safe_float(last.get("ATR14_PCT"))
    rsi = safe_float(last.get("RSI14"))
    vol_ratio = safe_float(last.get("VOL_RATIO_20"))
    ret_30d = safe_float(last.get("RET_30D"))
    ret_90d = safe_float(last.get("RET_90D"))

    breakout = close > levels["breakout_level"] * 1.005 if not pd.isna(levels["breakout_level"]) else False
    breakdown = close < levels["breakdown_level"] * 0.995 if not pd.isna(levels["breakdown_level"]) else False

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
        "image": image_path.name,
        "primary_pattern": primary["name"],
        "pattern_family": primary["family"],
        "pattern_state": primary["state"],
        "pattern_score": primary["score"],
        "pattern_neckline": primary.get("neckline"),
        "pattern_detail": primary["detail"],
        "patterns_count": len(detection["patterns"]),
        "all_patterns": detection["patterns"],
        "latest_candle": detection["candle"],
        "latest_candle_score": detection["candle_score"],
        "support": levels["support"],
        "resistance": levels["resistance"],
        "breakout_level": levels["breakout_level"],
        "breakdown_level": levels["breakdown_level"],
        "price_state": price_state,
        "breakout": breakout,
        "breakdown": breakdown,
        "rsi14": rsi,
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

def build_report(results):
    generated = now_utc_str()

    summary_rows = []

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
                ]
            )
            continue

        summary_rows.append(
            [
                asset,
                fmt_money(asset, r["price"]),
                r["primary_pattern"],
                r["pattern_state"],
                r["pattern_family"],
                r["price_state"],
                fmt_money(asset, r["support"]),
                fmt_money(asset, r["resistance"]),
            ]
        )

    lines = []

    lines.append("# Classic technical visual report")
    lines.append("")
    lines.append(f"Generato: {generated}")
    lines.append("")
    lines.append(
        "Questo report crea grafici visivi dei pattern tecnici principali. "
        "Serve per vedere il grafico, non per aggiungere automaticamente punteggio al Global."
    )
    lines.append("")
    lines.append("Pattern controllati:")
    lines.append("")
    lines.append("- doppio minimo")
    lines.append("- doppio massimo")
    lines.append("- testa e spalle")
    lines.append("- testa e spalle inverso")
    lines.append("- triangolo / compressione")
    lines.append("- candela giornaliera principale")
    lines.append("- pivot high / pivot low")
    lines.append("- supporto, resistenza, breakout e breakdown 60 giorni")
    lines.append("")
    lines.append("## Sintesi visiva")
    lines.append("")
    lines.append(
        md_table(
            [
                "Asset",
                "Prezzo",
                "Pattern principale",
                "Stato",
                "Famiglia",
                "Prezzo",
                "Supporto",
                "Resistenza",
            ],
            summary_rows,
        )
    )

    for r in results:
        asset = r["asset"]

        lines.append("")
        lines.append(f"## {asset}")

        if not r.get("ok"):
            lines.append("")
            lines.append(f"Errore: {r.get('error', 'n/a')}")
            continue

        lines.append("")
        lines.append(f"![Classic visual {asset}]({r['image']})")
        lines.append("")
        lines.append(f"- Pattern principale: **{r['primary_pattern']}**")
        lines.append(f"- Stato pattern: **{r['pattern_state']}**")
        lines.append(f"- Famiglia: **{r['pattern_family']}**")
        lines.append(f"- Dettaglio: {r['pattern_detail']}")
        lines.append(f"- Candela più recente: **{r['latest_candle']}**")
        lines.append(f"- Stato prezzo: **{r['price_state']}**")
        lines.append(f"- Supporto: **{fmt_money(asset, r['support'])}**")
        lines.append(f"- Resistenza: **{fmt_money(asset, r['resistance'])}**")
        lines.append(f"- Breakout 60g: **{fmt_money(asset, r['breakout_level'])}**")
        lines.append(f"- Breakdown 60g: **{fmt_money(asset, r['breakdown_level'])}**")
        lines.append(f"- RSI14: **{r['rsi14']:.2f}**" if not pd.isna(r["rsi14"]) else "- RSI14: **n/a**")
        lines.append(f"- ATR14: **{fmt_pct_plain(r['atr14_pct'])}**")
        lines.append(f"- Volume ratio 20g: **{r['vol_ratio']:.2f}**" if not pd.isna(r["vol_ratio"]) else "- Volume ratio 20g: **n/a**")
        lines.append(f"- Rendimento 30g: **{fmt_pct(r['ret_30d'])}**")
        lines.append(f"- Rendimento 90g: **{fmt_pct(r['ret_90d'])}**")

        if r["all_patterns"]:
            pattern_rows = []
            for p in r["all_patterns"]:
                pattern_rows.append(
                    [
                        p["name"],
                        p["state"],
                        p["family"],
                        fmt_money(asset, p.get("neckline")),
                        p["detail"],
                    ]
                )

            lines.append("")
            lines.append("### Pattern trovati")
            lines.append("")
            lines.append(
                md_table(
                    ["Pattern", "Stato", "Famiglia", "Neckline", "Dettaglio"],
                    pattern_rows,
                )
            )
        else:
            lines.append("")
            lines.append("Nessun pattern classico abbastanza pulito nel lookback usato.")

    lines.append("")
    lines.append("## Come leggerlo")
    lines.append("")
    lines.append("- Il grafico in alto mostra prezzo, MA20, MA50, MA200, supporti, resistenze e pattern.")
    lines.append("- Il pannello centrale mostra RSI14.")
    lines.append("- Il pannello basso mostra volume e media volume 20 giorni.")
    lines.append("- Un pattern **candidato** non è un segnale operativo: serve rottura della neckline o conferma del prezzo.")
    lines.append("- Un pattern **confermato** è più interessante, ma va comunque letto insieme a scanner, market regime, futures e rischio leva.")
    lines.append("")
    lines.append(
        "Nota: questi pattern sono riconosciuti con regole algoritmiche semplici. "
        "Sono utili per visualizzare il grafico, ma vanno sempre controllati a occhio."
    )

    return "\n".join(lines).rstrip() + "\n"


def write_metrics_csv(results):
    fieldnames = [
        "generated_utc",
        "asset",
        "ticker",
        "date",
        "price",
        "image",
        "primary_pattern",
        "pattern_family",
        "pattern_state",
        "pattern_score",
        "pattern_neckline",
        "patterns_count",
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

    for r in results:
        if not r.get("ok"):
            rows.append(
                {
                    "generated_utc": generated,
                    "asset": r.get("asset"),
                    "ticker": r.get("ticker"),
                    "date": "",
                    "price": "",
                    "image": "",
                    "primary_pattern": "ERROR",
                    "pattern_detail": r.get("error", ""),
                }
            )
            continue

        row = {k: r.get(k, "") for k in fieldnames}
        row["generated_utc"] = generated
        rows.append(row)

    with METRICS_CSV_PATH.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main():
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    results = []

    for asset, ticker in ASSETS.items():
        print(f"Creo visual report per {asset}...")
        result = analyze_asset(asset, ticker)
        results.append(result)

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


if __name__ == "__main__":
    main()
