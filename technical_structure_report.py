from pathlib import Path
from datetime import datetime

import numpy as np
import pandas as pd
import yfinance as yf


REPORTS_DIR = Path("reports")
OUTPUT_REPORT = REPORTS_DIR / "technical_structure_report.md"
OUTPUT_METRICS = REPORTS_DIR / "technical_structure_metrics.csv"
LATEST_REPORT = REPORTS_DIR / "latest_report.md"

START_MARKER = "<!-- TECHNICAL_STRUCTURE_START -->"
END_MARKER = "<!-- TECHNICAL_STRUCTURE_END -->"

TICKERS = ["BTC-USD", "SOL-USD", "DOGE-USD"]

PIVOT_WINDOW = 4
LOOKBACK_DAYS = 220


def safe_float(x):
    try:
        if pd.isna(x):
            return np.nan
        return float(x)
    except Exception:
        return np.nan


def fmt_num(x, digits=2):
    x = safe_float(x)
    if pd.isna(x):
        return "n/a"
    return f"{x:.{digits}f}"


def fmt_price(ticker, x):
    x = safe_float(x)
    if pd.isna(x):
        return "n/a"

    if "DOGE" in ticker:
        return f"{x:.5f}"

    if x >= 1000:
        return f"{x:,.0f}".replace(",", ".")

    return f"{x:.2f}".replace(".", ",")


def fmt_pct(x):
    x = safe_float(x)
    if pd.isna(x):
        return "n/a"
    return f"{x:.2f}%".replace(".", ",")


def df_to_markdown(df):
    if df is None or df.empty:
        return "_Nessun dato disponibile._"

    try:
        return df.to_markdown(index=False)
    except Exception:
        return "```csv\n" + df.to_csv(index=False) + "\n```"


def it_label(value):
    mapping = {
        "BULLISH_TECNICO": "RIALZISTA TECNICO",
        "COSTRUTTIVO_MA_NON_CONFERMATO": "COSTRUTTIVO MA NON CONFERMATO",
        "NEUTRALE_MISTO": "NEUTRALE / MISTO",
        "DEBOLE": "DEBOLE",
        "BEARISH_TECNICO": "RIBASSISTA TECNICO",

        "BULLISH_TREND": "Trend rialzista",
        "BEARISH_TREND": "Trend ribassista",
        "MIXED_TREND": "Trend misto",

        "MOMENTUM_IMPROVING": "Momentum in miglioramento",
        "MOMENTUM_WEAK": "Momentum debole",
        "MOMENTUM_MIXED": "Momentum misto",

        "ACCUMULATION_VOLUME": "Volume da accumulazione",
        "DISTRIBUTION_VOLUME": "Volume da distribuzione",
        "NEUTRAL_VOLUME": "Volume neutrale",

        "HH_HL_UPSTRUCTURE": "Struttura rialzista con massimi e minimi crescenti",
        "LH_LL_DOWNSTRUCTURE": "Struttura ribassista con massimi e minimi decrescenti",
        "COMPRESSION_TRIANGLE": "Compressione / triangolo",
        "EXPANDING_VOLATILITY": "Volatilità in espansione",
        "UNKNOWN": "Sconosciuto",

        "BULLISH_RSI_DIVERGENCE": "Divergenza rialzista RSI",
        "BEARISH_RSI_DIVERGENCE": "Divergenza ribassista RSI",
        "HIDDEN_BULLISH_RSI_DIVERGENCE": "Divergenza rialzista nascosta RSI",
        "HIDDEN_BEARISH_RSI_DIVERGENCE": "Divergenza ribassista nascosta RSI",
        "NONE": "Nessuna",

        "ACCUMULATION_CANDIDATE": "Possibile accumulazione",
        "DISTRIBUTION_CANDIDATE": "Possibile distribuzione",
        "MARKUP": "Markup / fase rialzista",
        "MARKDOWN": "Markdown / fase ribassista",
        "RANGE_OR_UNKNOWN": "Range / fase non chiara",

        "ASSENTE": "Assente",
        "POSSIBILE": "Possibile",
        "CONFERMATO": "Confermato",

        "ADAM_AND_EVE_BOTTOM": "Adam and Eve Bottom",
        "EVE_AND_ADAM_BOTTOM": "Eve and Adam Bottom",
        "ADAM_AND_EVE_TOP": "Adam and Eve Top",
        "EVE_AND_ADAM_TOP": "Eve and Adam Top",
    }

    if pd.isna(value):
        return "n/a"

    value = str(value)

    if "," in value:
        parts = [p.strip() for p in value.split(",")]
        return ", ".join(mapping.get(p, p) for p in parts)

    return mapping.get(value, value)


def normalize_ohlcv(df):
    if df is None or df.empty:
        return pd.DataFrame()

    out = df.copy()

    if isinstance(out.columns, pd.MultiIndex):
        level0 = list(out.columns.get_level_values(0))
        level1 = list(out.columns.get_level_values(1))

        fields = ["Open", "High", "Low", "Close", "Adj Close", "Volume"]

        if any(f in level0 for f in fields):
            tmp = {}
            for field in fields:
                if field in level0:
                    part = out.xs(field, axis=1, level=0)
                    tmp[field] = part.iloc[:, 0]
            out = pd.DataFrame(tmp)

        elif any(f in level1 for f in fields):
            tmp = {}
            for field in fields:
                if field in level1:
                    part = out.xs(field, axis=1, level=1)
                    tmp[field] = part.iloc[:, 0]
            out = pd.DataFrame(tmp)

        else:
            return pd.DataFrame()

    needed = ["Open", "High", "Low", "Close", "Volume"]

    for col in needed:
        if col not in out.columns:
            if col in ["Open", "High", "Low"] and "Close" in out.columns:
                out[col] = out["Close"]
            elif col == "Volume":
                out[col] = np.nan
            else:
                return pd.DataFrame()

    out = out[needed].copy()
    out.index = pd.to_datetime(out.index)

    try:
        if out.index.tz is not None:
            out.index = out.index.tz_convert(None)
    except Exception:
        pass

    out.index = out.index.normalize()
    out = out[~out.index.duplicated(keep="last")]
    out = out.sort_index()
    out = out.dropna(subset=["Close"])

    return out


def download_asset(ticker):
    try:
        raw = yf.download(
            ticker,
            period="max",
            interval="1d",
            progress=False,
            auto_adjust=False,
            actions=False,
            threads=False,
        )
        return normalize_ohlcv(raw)
    except Exception as e:
        print(f"Download fallito per {ticker}: {e}")
        return pd.DataFrame()


def ema(series, span):
    return series.ewm(span=span, adjust=False).mean()


def rsi(series, period=14):
    delta = series.diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.ewm(alpha=1 / period, min_periods=period, adjust=False).mean()
    avg_loss = loss.ewm(alpha=1 / period, min_periods=period, adjust=False).mean()

    rs = avg_gain / avg_loss.replace(0, np.nan)
    out = 100 - (100 / (1 + rs))

    return out.fillna(50)


def add_indicators(df):
    d = df.copy()

    d["ma20"] = d["Close"].rolling(20, min_periods=10).mean()
    d["ma50"] = d["Close"].rolling(50, min_periods=25).mean()
    d["ma100"] = d["Close"].rolling(100, min_periods=50).mean()
    d["ma200"] = d["Close"].rolling(200, min_periods=100).mean()

    d["ema12"] = ema(d["Close"], 12)
    d["ema26"] = ema(d["Close"], 26)
    d["macd"] = d["ema12"] - d["ema26"]
    d["macd_signal"] = ema(d["macd"], 9)
    d["macd_hist"] = d["macd"] - d["macd_signal"]

    d["rsi14"] = rsi(d["Close"], 14)

    d["vol_ma20"] = d["Volume"].rolling(20, min_periods=10).mean()

    prev_close = d["Close"].shift(1)
    tr1 = d["High"] - d["Low"]
    tr2 = (d["High"] - prev_close).abs()
    tr3 = (d["Low"] - prev_close).abs()
    d["tr"] = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)
    d["atr14"] = d["tr"].rolling(14, min_periods=7).mean()

    direction = np.sign(d["Close"].diff()).fillna(0)
    d["obv"] = (direction * d["Volume"].fillna(0)).cumsum()
    d["obv_ma20"] = d["obv"].rolling(20, min_periods=10).mean()

    denom = (d["High"] - d["Low"]).replace(0, np.nan)
    mfm = ((d["Close"] - d["Low"]) - (d["High"] - d["Close"])) / denom
    mfv = mfm.fillna(0) * d["Volume"].fillna(0)

    d["cmf20"] = (
        mfv.rolling(20, min_periods=10).sum()
        / d["Volume"].rolling(20, min_periods=10).sum().replace(0, np.nan)
    )

    return d


def slope_pct(series, days):
    s = series.dropna()

    if len(s) <= days:
        return np.nan

    now = safe_float(s.iloc[-1])
    old = safe_float(s.iloc[-days])

    if pd.isna(now) or pd.isna(old) or old == 0:
        return np.nan

    return (now / old - 1) * 100


def pct_change_days(series, days):
    s = series.dropna()

    if len(s) <= days:
        return np.nan

    now = safe_float(s.iloc[-1])
    old = safe_float(s.iloc[-days])

    if pd.isna(now) or pd.isna(old) or old == 0:
        return np.nan

    return (now / old - 1) * 100


def find_pivots(df, window=PIVOT_WINDOW):
    d = df.copy()

    highs = d["High"]
    lows = d["Low"]

    roll_high = highs.rolling(window * 2 + 1, center=True).max()
    roll_low = lows.rolling(window * 2 + 1, center=True).min()

    d["pivot_high"] = highs == roll_high
    d["pivot_low"] = lows == roll_low

    d["pivot_high"] = d["pivot_high"] & (highs.shift(1) < highs) & (highs.shift(-1) < highs)
    d["pivot_low"] = d["pivot_low"] & (lows.shift(1) > lows) & (lows.shift(-1) > lows)

    return d


def recent_slice(df, days=LOOKBACK_DAYS):
    if df.empty:
        return df

    cutoff = df.index[-1] - pd.Timedelta(days=days)
    return df[df.index >= cutoff].copy()


def pivot_rows(df, kind, days=LOOKBACK_DAYS):
    d = recent_slice(df, days)

    col = "pivot_low" if kind == "low" else "pivot_high"

    if col not in d.columns:
        return pd.DataFrame()

    piv = d[d[col]].copy()

    if piv.empty:
        return piv

    price_col = "Low" if kind == "low" else "High"

    return piv[
        [price_col, "Close", "rsi14", "macd_hist", "Volume"]
    ].rename(columns={price_col: "pivot_price"})


def near(a, b, tolerance_pct):
    a = safe_float(a)
    b = safe_float(b)

    if pd.isna(a) or pd.isna(b) or b == 0:
        return False

    return abs(a / b - 1) * 100 <= tolerance_pct


def empty_bottom_result():
    return {
        "status": "ASSENTE",
        "confidence": "LOW",
        "details": "",
        "neckline": np.nan,
        "support": np.nan,
        "confirmed": False,
        "score": 0,
    }


def empty_top_result():
    return {
        "status": "ASSENTE",
        "confidence": "LOW",
        "details": "",
        "neckline": np.nan,
        "resistance": np.nan,
        "confirmed": False,
        "score": 0,
    }


def pattern_double_bottom(df, ticker):
    lows = pivot_rows(df, "low")
    highs = pivot_rows(df, "high")

    result = empty_bottom_result()

    if len(lows) < 2:
        return result

    recent_lows = lows.tail(5)
    best = None

    for i in range(len(recent_lows) - 1):
        for j in range(i + 1, len(recent_lows)):
            d1 = recent_lows.index[i]
            d2 = recent_lows.index[j]

            p1 = safe_float(recent_lows.iloc[i]["pivot_price"])
            p2 = safe_float(recent_lows.iloc[j]["pivot_price"])

            sep = (d2 - d1).days

            if sep < 10 or sep > 160:
                continue

            if not near(p1, p2, 7.0):
                continue

            between_highs = highs[(highs.index > d1) & (highs.index < d2)]

            if between_highs.empty:
                continue

            neckline = safe_float(between_highs["pivot_price"].max())
            support = min(p1, p2)
            close = safe_float(df["Close"].iloc[-1])
            confirmed = close > neckline if not pd.isna(neckline) else False

            strength = 100 - abs(p1 / p2 - 1) * 100 + min(sep, 80) / 10
            candidate = (strength, d1, d2, support, neckline, confirmed)

            if best is None or candidate[0] > best[0]:
                best = candidate

    if best is None:
        return result

    _, d1, d2, support, neckline, confirmed = best

    status = "CONFERMATO" if confirmed else "POSSIBILE"
    score = 2 if confirmed else 1

    result.update({
        "status": status,
        "confidence": "MEDIUM" if confirmed else "LOW/MEDIUM",
        "details": (
            f"Due minimi simili vicino a {fmt_price(ticker, support)} "
            f"tra {d1.date()} e {d2.date()}. "
            f"Neckline stimata: {fmt_price(ticker, neckline)}."
        ),
        "neckline": neckline,
        "support": support,
        "confirmed": confirmed,
        "score": score,
    })

    return result


def pattern_triple_bottom(df, ticker):
    lows = pivot_rows(df, "low")
    highs = pivot_rows(df, "high")

    result = empty_bottom_result()

    if len(lows) < 3:
        return result

    recent = lows.tail(7)
    best = None

    for a in range(len(recent) - 2):
        for b in range(a + 1, len(recent) - 1):
            for c in range(b + 1, len(recent)):
                dates = [recent.index[a], recent.index[b], recent.index[c]]
                prices = [
                    safe_float(recent.iloc[a]["pivot_price"]),
                    safe_float(recent.iloc[b]["pivot_price"]),
                    safe_float(recent.iloc[c]["pivot_price"]),
                ]

                span = (dates[-1] - dates[0]).days

                if span < 20 or span > 220:
                    continue

                if max(prices) / min(prices) - 1 > 0.09:
                    continue

                between_highs = highs[(highs.index > dates[0]) & (highs.index < dates[-1])]

                if between_highs.empty:
                    continue

                neckline = safe_float(between_highs["pivot_price"].max())
                support = min(prices)
                close = safe_float(df["Close"].iloc[-1])
                confirmed = close > neckline if not pd.isna(neckline) else False

                tightness = 100 - (max(prices) / min(prices) - 1) * 100
                candidate = (tightness, dates, support, neckline, confirmed)

                if best is None or candidate[0] > best[0]:
                    best = candidate

    if best is None:
        return result

    _, dates, support, neckline, confirmed = best

    status = "CONFERMATO" if confirmed else "POSSIBILE"
    score = 3 if confirmed else 1

    result.update({
        "status": status,
        "confidence": "MEDIUM" if confirmed else "LOW/MEDIUM",
        "details": (
            f"Tre minimi simili vicino a {fmt_price(ticker, support)} "
            f"dal {dates[0].date()} al {dates[-1].date()}. "
            f"Neckline stimata: {fmt_price(ticker, neckline)}."
        ),
        "neckline": neckline,
        "support": support,
        "confirmed": confirmed,
        "score": score,
    })

    return result


def pattern_double_top(df, ticker):
    highs = pivot_rows(df, "high")
    lows = pivot_rows(df, "low")

    result = empty_top_result()

    if len(highs) < 2:
        return result

    recent_highs = highs.tail(5)
    best = None

    for i in range(len(recent_highs) - 1):
        for j in range(i + 1, len(recent_highs)):
            d1 = recent_highs.index[i]
            d2 = recent_highs.index[j]

            p1 = safe_float(recent_highs.iloc[i]["pivot_price"])
            p2 = safe_float(recent_highs.iloc[j]["pivot_price"])

            sep = (d2 - d1).days

            if sep < 10 or sep > 160:
                continue

            if not near(p1, p2, 7.0):
                continue

            between_lows = lows[(lows.index > d1) & (lows.index < d2)]

            if between_lows.empty:
                continue

            neckline = safe_float(between_lows["pivot_price"].min())
            resistance = max(p1, p2)
            close = safe_float(df["Close"].iloc[-1])
            confirmed = close < neckline if not pd.isna(neckline) else False

            strength = 100 - abs(p1 / p2 - 1) * 100 + min(sep, 80) / 10
            candidate = (strength, d1, d2, resistance, neckline, confirmed)

            if best is None or candidate[0] > best[0]:
                best = candidate

    if best is None:
        return result

    _, d1, d2, resistance, neckline, confirmed = best

    status = "CONFERMATO" if confirmed else "POSSIBILE"
    score = -2 if confirmed else -1

    result.update({
        "status": status,
        "confidence": "MEDIUM" if confirmed else "LOW/MEDIUM",
        "details": (
            f"Due massimi simili vicino a {fmt_price(ticker, resistance)} "
            f"tra {d1.date()} e {d2.date()}. "
            f"Neckline ribassista stimata: {fmt_price(ticker, neckline)}."
        ),
        "neckline": neckline,
        "resistance": resistance,
        "confirmed": confirmed,
        "score": score,
    })

    return result


def pattern_triple_top(df, ticker):
    highs = pivot_rows(df, "high")
    lows = pivot_rows(df, "low")

    result = empty_top_result()

    if len(highs) < 3:
        return result

    recent = highs.tail(7)
    best = None

    for a in range(len(recent) - 2):
        for b in range(a + 1, len(recent) - 1):
            for c in range(b + 1, len(recent)):
                dates = [recent.index[a], recent.index[b], recent.index[c]]
                prices = [
                    safe_float(recent.iloc[a]["pivot_price"]),
                    safe_float(recent.iloc[b]["pivot_price"]),
                    safe_float(recent.iloc[c]["pivot_price"]),
                ]

                span = (dates[-1] - dates[0]).days

                if span < 20 or span > 220:
                    continue

                if max(prices) / min(prices) - 1 > 0.09:
                    continue

                between_lows = lows[(lows.index > dates[0]) & (lows.index < dates[-1])]

                if between_lows.empty:
                    continue

                neckline = safe_float(between_lows["pivot_price"].min())
                resistance = max(prices)
                close = safe_float(df["Close"].iloc[-1])
                confirmed = close < neckline if not pd.isna(neckline) else False

                tightness = 100 - (max(prices) / min(prices) - 1) * 100
                candidate = (tightness, dates, resistance, neckline, confirmed)

                if best is None or candidate[0] > best[0]:
                    best = candidate

    if best is None:
        return result

    _, dates, resistance, neckline, confirmed = best

    status = "CONFERMATO" if confirmed else "POSSIBILE"
    score = -3 if confirmed else -1

    result.update({
        "status": status,
        "confidence": "MEDIUM" if confirmed else "LOW/MEDIUM",
        "details": (
            f"Tre massimi simili vicino a {fmt_price(ticker, resistance)} "
            f"dal {dates[0].date()} al {dates[-1].date()}. "
            f"Neckline ribassista stimata: {fmt_price(ticker, neckline)}."
        ),
        "neckline": neckline,
        "resistance": resistance,
        "confirmed": confirmed,
        "score": score,
    })

    return result


def bottom_shape_metrics(df, pivot_date):
    if pivot_date not in df.index:
        return {"sharp_score": 0, "round_score": 0}

    pos = df.index.get_loc(pivot_date)

    if isinstance(pos, slice):
        pos = pos.start

    start = max(0, pos - 12)
    end = min(len(df) - 1, pos + 12)

    window = df.iloc[start:end + 1]

    if window.empty:
        return {"sharp_score": 0, "round_score": 0}

    low = safe_float(df.loc[pivot_date, "Low"])
    atr = safe_float(df.loc[pivot_date, "atr14"])

    if pd.isna(atr) or atr == 0:
        atr = safe_float((window["High"] - window["Low"]).mean())

    left_high = safe_float(df.iloc[start:pos + 1]["High"].max())
    right_high = safe_float(df.iloc[pos:end + 1]["High"].max())

    left_drop = (left_high / low - 1) * 100 if low and not pd.isna(left_high) else 0
    right_rebound = (right_high / low - 1) * 100 if low and not pd.isna(right_high) else 0

    sharp_score = 0

    if left_drop >= 8:
        sharp_score += 1

    if right_rebound >= 8:
        sharp_score += 1

    if not pd.isna(atr) and low > 0 and (atr / low * 100) >= 4:
        sharp_score += 1

    near_low = window[window["Low"] <= low * 1.07]

    round_score = 0

    if len(near_low) >= 5:
        round_score += 1

    if len(near_low) >= 8:
        round_score += 1

    if not pd.isna(atr) and low > 0 and (atr / low * 100) < 6:
        round_score += 1

    return {"sharp_score": sharp_score, "round_score": round_score}


def top_shape_metrics(df, pivot_date):
    if pivot_date not in df.index:
        return {"sharp_score": 0, "round_score": 0}

    pos = df.index.get_loc(pivot_date)

    if isinstance(pos, slice):
        pos = pos.start

    start = max(0, pos - 12)
    end = min(len(df) - 1, pos + 12)

    window = df.iloc[start:end + 1]

    if window.empty:
        return {"sharp_score": 0, "round_score": 0}

    high = safe_float(df.loc[pivot_date, "High"])
    atr = safe_float(df.loc[pivot_date, "atr14"])

    if pd.isna(atr) or atr == 0:
        atr = safe_float((window["High"] - window["Low"]).mean())

    left_low = safe_float(df.iloc[start:pos + 1]["Low"].min())
    right_low = safe_float(df.iloc[pos:end + 1]["Low"].min())

    left_rise = (high / left_low - 1) * 100 if left_low and not pd.isna(left_low) else 0
    right_drop = (high / right_low - 1) * 100 if right_low and not pd.isna(right_low) else 0

    sharp_score = 0

    if left_rise >= 8:
        sharp_score += 1

    if right_drop >= 8:
        sharp_score += 1

    if not pd.isna(atr) and high > 0 and (atr / high * 100) >= 4:
        sharp_score += 1

    near_high = window[window["High"] >= high * 0.93]

    round_score = 0

    if len(near_high) >= 5:
        round_score += 1

    if len(near_high) >= 8:
        round_score += 1

    if not pd.isna(atr) and high > 0 and (atr / high * 100) < 6:
        round_score += 1

    return {"sharp_score": sharp_score, "round_score": round_score}


def empty_adam_eve_bottom_result():
    out = empty_bottom_result()
    out["variant"] = ""
    return out


def empty_adam_eve_top_result():
    out = empty_top_result()
    out["variant"] = ""
    return out


def pattern_adam_eve_bottom(df, ticker):
    lows = pivot_rows(df, "low")
    highs = pivot_rows(df, "high")

    result = empty_adam_eve_bottom_result()

    if len(lows) < 2:
        return result

    recent_lows = lows.tail(6)
    best = None

    for i in range(len(recent_lows) - 1):
        for j in range(i + 1, len(recent_lows)):
            d1 = recent_lows.index[i]
            d2 = recent_lows.index[j]

            p1 = safe_float(recent_lows.iloc[i]["pivot_price"])
            p2 = safe_float(recent_lows.iloc[j]["pivot_price"])

            sep = (d2 - d1).days

            if sep < 12 or sep > 180:
                continue

            if not near(p1, p2, 9.0):
                continue

            m1 = bottom_shape_metrics(df, d1)
            m2 = bottom_shape_metrics(df, d2)

            variant = ""
            pattern_score = 0

            if m1["sharp_score"] >= 2 and m2["round_score"] >= 2:
                variant = "ADAM_AND_EVE_BOTTOM"
                pattern_score = m1["sharp_score"] + m2["round_score"]

            elif m1["round_score"] >= 2 and m2["sharp_score"] >= 2:
                variant = "EVE_AND_ADAM_BOTTOM"
                pattern_score = m1["round_score"] + m2["sharp_score"]

            if not variant:
                continue

            between_highs = highs[(highs.index > d1) & (highs.index < d2)]

            if between_highs.empty:
                continue

            neckline = safe_float(between_highs["pivot_price"].max())
            support = min(p1, p2)
            close = safe_float(df["Close"].iloc[-1])
            confirmed = close > neckline if not pd.isna(neckline) else False

            candidate = (pattern_score, d1, d2, support, neckline, confirmed, variant)

            if best is None or candidate[0] > best[0]:
                best = candidate

    if best is None:
        return result

    _, d1, d2, support, neckline, confirmed, variant = best

    status = "CONFERMATO" if confirmed else "POSSIBILE"
    score = 3 if confirmed else 1

    variant_it = it_label(variant)

    result.update({
        "status": status,
        "confidence": "MEDIUM" if confirmed else "LOW/MEDIUM",
        "variant": variant,
        "details": (
            f"Possibile pattern {variant_it} vicino a {fmt_price(ticker, support)} "
            f"dal {d1.date()} al {d2.date()}. "
            f"Nel modello Adam/Eve un minimo è più appuntito e violento, "
            f"l'altro è più arrotondato. "
            f"Neckline stimata: {fmt_price(ticker, neckline)}."
        ),
        "neckline": neckline,
        "support": support,
        "confirmed": confirmed,
        "score": score,
    })

    return result


def pattern_adam_eve_top(df, ticker):
    highs = pivot_rows(df, "high")
    lows = pivot_rows(df, "low")

    result = empty_adam_eve_top_result()

    if len(highs) < 2:
        return result

    recent_highs = highs.tail(6)
    best = None

    for i in range(len(recent_highs) - 1):
        for j in range(i + 1, len(recent_highs)):
            d1 = recent_highs.index[i]
            d2 = recent_highs.index[j]

            p1 = safe_float(recent_highs.iloc[i]["pivot_price"])
            p2 = safe_float(recent_highs.iloc[j]["pivot_price"])

            sep = (d2 - d1).days

            if sep < 12 or sep > 180:
                continue

            if not near(p1, p2, 9.0):
                continue

            m1 = top_shape_metrics(df, d1)
            m2 = top_shape_metrics(df, d2)

            variant = ""
            pattern_score = 0

            if m1["sharp_score"] >= 2 and m2["round_score"] >= 2:
                variant = "ADAM_AND_EVE_TOP"
                pattern_score = m1["sharp_score"] + m2["round_score"]

            elif m1["round_score"] >= 2 and m2["sharp_score"] >= 2:
                variant = "EVE_AND_ADAM_TOP"
                pattern_score = m1["round_score"] + m2["sharp_score"]

            if not variant:
                continue

            between_lows = lows[(lows.index > d1) & (lows.index < d2)]

            if between_lows.empty:
                continue

            neckline = safe_float(between_lows["pivot_price"].min())
            resistance = max(p1, p2)
            close = safe_float(df["Close"].iloc[-1])
            confirmed = close < neckline if not pd.isna(neckline) else False

            candidate = (pattern_score, d1, d2, resistance, neckline, confirmed, variant)

            if best is None or candidate[0] > best[0]:
                best = candidate

    if best is None:
        return result

    _, d1, d2, resistance, neckline, confirmed, variant = best

    status = "CONFERMATO" if confirmed else "POSSIBILE"
    score = -3 if confirmed else -1

    variant_it = it_label(variant)

    result.update({
        "status": status,
        "confidence": "MEDIUM" if confirmed else "LOW/MEDIUM",
        "variant": variant,
        "details": (
            f"Possibile pattern {variant_it} vicino a {fmt_price(ticker, resistance)} "
            f"dal {d1.date()} al {d2.date()}. "
            f"Nel modello Adam/Eve un massimo è più appuntito e violento, "
            f"l'altro è più arrotondato. "
            f"Neckline ribassista stimata: {fmt_price(ticker, neckline)}."
        ),
        "neckline": neckline,
        "resistance": resistance,
        "confirmed": confirmed,
        "score": score,
    })

    return result


def recent_structure(df):
    lows = pivot_rows(df, "low")
    highs = pivot_rows(df, "high")

    structure = "UNKNOWN"
    score = 0
    details = ""

    if len(lows) >= 2 and len(highs) >= 2:
        l1 = safe_float(lows.iloc[-2]["pivot_price"])
        l2 = safe_float(lows.iloc[-1]["pivot_price"])
        h1 = safe_float(highs.iloc[-2]["pivot_price"])
        h2 = safe_float(highs.iloc[-1]["pivot_price"])

        higher_low = l2 > l1
        higher_high = h2 > h1
        lower_low = l2 < l1
        lower_high = h2 < h1

        if higher_low and higher_high:
            structure = "HH_HL_UPSTRUCTURE"
            score = 2

        elif lower_low and lower_high:
            structure = "LH_LL_DOWNSTRUCTURE"
            score = -2

        elif higher_low and lower_high:
            structure = "COMPRESSION_TRIANGLE"
            score = 0

        elif lower_low and higher_high:
            structure = "EXPANDING_VOLATILITY"
            score = 0

        details = (
            f"Ultimi minimi: {l1:.4g} -> {l2:.4g}. "
            f"Ultimi massimi: {h1:.4g} -> {h2:.4g}."
        )

    return structure, score, details


def detect_divergences(df):
    lows = pivot_rows(df, "low", days=260)
    highs = pivot_rows(df, "high", days=260)

    divs = []
    score = 0

    if len(lows) >= 2:
        p1 = safe_float(lows.iloc[-2]["pivot_price"])
        p2 = safe_float(lows.iloc[-1]["pivot_price"])
        r1 = safe_float(lows.iloc[-2]["rsi14"])
        r2 = safe_float(lows.iloc[-1]["rsi14"])

        if p2 < p1 and r2 > r1 + 2:
            divs.append("BULLISH_RSI_DIVERGENCE")
            score += 2

        elif p2 > p1 and r2 < r1 - 2:
            divs.append("HIDDEN_BULLISH_RSI_DIVERGENCE")
            score += 1

    if len(highs) >= 2:
        p1 = safe_float(highs.iloc[-2]["pivot_price"])
        p2 = safe_float(highs.iloc[-1]["pivot_price"])
        r1 = safe_float(highs.iloc[-2]["rsi14"])
        r2 = safe_float(highs.iloc[-1]["rsi14"])

        if p2 > p1 and r2 < r1 - 2:
            divs.append("BEARISH_RSI_DIVERGENCE")
            score -= 2

        elif p2 < p1 and r2 > r1 + 2:
            divs.append("HIDDEN_BEARISH_RSI_DIVERGENCE")
            score -= 1

    if not divs:
        divs.append("NONE")

    return ", ".join(divs), score


def trend_score(df):
    latest = df.iloc[-1]

    close = safe_float(latest["Close"])
    ma20 = safe_float(latest.get("ma20"))
    ma50 = safe_float(latest.get("ma50"))
    ma200 = safe_float(latest.get("ma200"))

    ma20_slope = slope_pct(df["ma20"], 10)
    ma50_slope = slope_pct(df["ma50"], 20)
    ma200_slope = slope_pct(df["ma200"], 60)

    score = 0

    if not pd.isna(ma20):
        score += 1 if close > ma20 else -1

    if not pd.isna(ma50):
        score += 1 if close > ma50 else -1

    if not pd.isna(ma200):
        score += 1 if close > ma200 else -1

    if not pd.isna(ma50_slope):
        score += 1 if ma50_slope > 0 else -1

    if not pd.isna(ma200_slope):
        score += 1 if ma200_slope > 0 else -1

    score = int(max(-3, min(3, score)))

    if score >= 2:
        label = "BULLISH_TREND"
    elif score <= -2:
        label = "BEARISH_TREND"
    else:
        label = "MIXED_TREND"

    return label, score, ma20_slope, ma50_slope, ma200_slope


def momentum_score(df):
    latest = df.iloc[-1]
    prev5 = df.iloc[-6] if len(df) > 6 else latest

    rsi_now = safe_float(latest["rsi14"])
    rsi_prev = safe_float(prev5["rsi14"])

    macd = safe_float(latest["macd"])
    signal = safe_float(latest["macd_signal"])

    hist_now = safe_float(latest["macd_hist"])
    hist_prev = safe_float(prev5["macd_hist"])

    score = 0

    if not pd.isna(rsi_now):
        if rsi_now >= 55:
            score += 1
        elif rsi_now <= 40:
            score -= 1

    if not pd.isna(rsi_now) and not pd.isna(rsi_prev):
        score += 1 if rsi_now > rsi_prev else -1

    if not pd.isna(macd) and not pd.isna(signal):
        score += 1 if macd > signal else -1

    if not pd.isna(hist_now) and not pd.isna(hist_prev):
        score += 1 if hist_now > hist_prev else -1

    score = int(max(-3, min(3, score)))

    if score >= 2:
        label = "MOMENTUM_IMPROVING"
    elif score <= -2:
        label = "MOMENTUM_WEAK"
    else:
        label = "MOMENTUM_MIXED"

    return label, score


def volume_score(df):
    latest = df.iloc[-1]

    close = safe_float(latest["Close"])
    prev_close = safe_float(df["Close"].iloc[-2]) if len(df) > 2 else np.nan

    volume = safe_float(latest["Volume"])
    vol_ma20 = safe_float(latest["vol_ma20"])

    obv = safe_float(latest["obv"])
    obv_ma20 = safe_float(latest["obv_ma20"])

    cmf = safe_float(latest["cmf20"])

    score = 0

    up_day = False

    if not pd.isna(close) and not pd.isna(prev_close):
        up_day = close > prev_close

    if not pd.isna(volume) and not pd.isna(vol_ma20) and vol_ma20 > 0:
        if volume > vol_ma20 * 1.2 and up_day:
            score += 1
        elif volume > vol_ma20 * 1.2 and not up_day:
            score -= 1

    if not pd.isna(obv) and not pd.isna(obv_ma20):
        score += 1 if obv > obv_ma20 else -1

    if not pd.isna(cmf):
        if cmf > 0.05:
            score += 1
        elif cmf < -0.05:
            score -= 1

    score = int(max(-2, min(2, score)))

    if score >= 1:
        label = "ACCUMULATION_VOLUME"
    elif score <= -1:
        label = "DISTRIBUTION_VOLUME"
    else:
        label = "NEUTRAL_VOLUME"

    return label, score


def wyckoff_candidate(df):
    close = df["Close"]
    latest = df.iloc[-1]

    price = safe_float(latest["Close"])
    ma200 = safe_float(latest["ma200"])
    rsi_now = safe_float(latest["rsi14"])

    ret90 = pct_change_days(close, 90)
    ret30 = pct_change_days(close, 30)

    recent = recent_slice(df, 120)

    if recent.empty:
        return "UNKNOWN", 0, "Dati insufficienti per stimare la fase Wyckoff."

    high_120 = safe_float(recent["High"].max())
    low_120 = safe_float(recent["Low"].min())

    range_pct = (high_120 / low_120 - 1) * 100 if low_120 and not pd.isna(high_120) else np.nan

    near_range_low = False
    near_range_high = False

    if not pd.isna(range_pct) and high_120 > low_120:
        pos_in_range = (price - low_120) / (high_120 - low_120)
        near_range_low = pos_in_range <= 0.35
        near_range_high = pos_in_range >= 0.65
    else:
        pos_in_range = np.nan

    below_ma200 = not pd.isna(ma200) and price < ma200
    above_ma200 = not pd.isna(ma200) and price > ma200

    ma50_rising = slope_pct(df["ma50"], 20)
    ma50_up = not pd.isna(ma50_rising) and ma50_rising > 0

    if below_ma200 and not pd.isna(ret90) and ret90 < 0 and near_range_low and not pd.isna(rsi_now) and rsi_now < 55:
        return (
            "ACCUMULATION_CANDIDATE",
            1,
            f"Prezzo sotto MA200, vicino alla parte bassa del range a 120 giorni, RSI {rsi_now:.1f}.",
        )

    if above_ma200 and ma50_up and not pd.isna(ret30) and ret30 > 5:
        return (
            "MARKUP",
            2,
            "Prezzo sopra MA200, MA50 in salita e trend a 30 giorni positivo.",
        )

    if above_ma200 and near_range_high and not pd.isna(rsi_now) and rsi_now < 55 and not pd.isna(ret30) and ret30 < 0:
        return (
            "DISTRIBUTION_CANDIDATE",
            -2,
            "Prezzo sopra MA200 ma momentum debole vicino alla parte alta del range.",
        )

    if below_ma200 and not pd.isna(ret90) and ret90 < -10:
        return (
            "MARKDOWN",
            -2,
            "Prezzo sotto MA200 con trend a 90 giorni ancora debole.",
        )

    pos_txt = fmt_pct(pos_in_range * 100 if not pd.isna(pos_in_range) else np.nan)

    return (
        "RANGE_OR_UNKNOWN",
        0,
        f"Posizione nel range a 120 giorni: {pos_txt}. Fase non abbastanza chiara.",
    )


def support_resistance(df):
    lows = pivot_rows(df, "low")
    highs = pivot_rows(df, "high")

    close = safe_float(df["Close"].iloc[-1])

    support = np.nan
    resistance = np.nan

    if not lows.empty:
        below = lows[lows["pivot_price"] <= close]

        if not below.empty:
            support = safe_float(below["pivot_price"].iloc[-1])
        else:
            support = safe_float(lows["pivot_price"].iloc[-1])

    if not highs.empty:
        above = highs[highs["pivot_price"] >= close]

        if not above.empty:
            resistance = safe_float(above["pivot_price"].iloc[-1])
        else:
            resistance = safe_float(highs["pivot_price"].iloc[-1])

    return support, resistance


def verdict_from_score(score):
    if score >= 7:
        return "BULLISH_TECNICO"
    if score >= 3:
        return "COSTRUTTIVO_MA_NON_CONFERMATO"
    if score >= -2:
        return "NEUTRALE_MISTO"
    if score >= -6:
        return "DEBOLE"
    return "BEARISH_TECNICO"


def analyze_asset(ticker):
    raw = download_asset(ticker)

    if raw.empty or len(raw) < 220:
        return None

    df = add_indicators(raw)
    df = find_pivots(df)

    latest = df.iloc[-1]
    price = safe_float(latest["Close"])

    t_label, t_score, ma20_slope, ma50_slope, ma200_slope = trend_score(df)
    m_label, m_score = momentum_score(df)
    v_label, v_score = volume_score(df)

    struct_label, struct_score, struct_details = recent_structure(df)
    div_label, div_score = detect_divergences(df)
    wy_label, wy_score, wy_details = wyckoff_candidate(df)

    db = pattern_double_bottom(df, ticker)
    tb = pattern_triple_bottom(df, ticker)
    dt = pattern_double_top(df, ticker)
    tt = pattern_triple_top(df, ticker)
    ae_bottom = pattern_adam_eve_bottom(df, ticker)
    ae_top = pattern_adam_eve_top(df, ticker)

    pattern_score = 0
    pattern_score += db["score"]
    pattern_score += tb["score"]
    pattern_score += dt["score"]
    pattern_score += tt["score"]
    pattern_score += ae_bottom["score"]
    pattern_score += ae_top["score"]
    pattern_score = int(max(-4, min(4, pattern_score)))

    total_score = int(
        t_score
        + m_score
        + v_score
        + struct_score
        + div_score
        + wy_score
        + pattern_score
    )

    total_score = int(max(-12, min(12, total_score)))

    support, resistance = support_resistance(df)

    verdict = verdict_from_score(total_score)

    row = {
        "asset": ticker.replace("-USD", ""),
        "ticker": ticker,
        "price": price,
        "technical_score": total_score,
        "verdict": verdict,

        "trend": t_label,
        "trend_score": t_score,

        "momentum": m_label,
        "momentum_score": m_score,

        "volume": v_label,
        "volume_score": v_score,

        "structure": struct_label,
        "structure_score": struct_score,

        "divergence": div_label,
        "divergence_score": div_score,

        "wyckoff": wy_label,
        "wyckoff_score": wy_score,

        "pattern_score": pattern_score,

        "double_bottom": db["status"],
        "triple_bottom": tb["status"],
        "double_top": dt["status"],
        "triple_top": tt["status"],

        "adam_eve_bottom": ae_bottom["status"],
        "adam_eve_bottom_variant": ae_bottom["variant"],

        "adam_eve_top": ae_top["status"],
        "adam_eve_top_variant": ae_top["variant"],

        "support": support,
        "resistance": resistance,

        "rsi14": safe_float(latest["rsi14"]),
        "macd_hist": safe_float(latest["macd_hist"]),

        "ma20": safe_float(latest["ma20"]),
        "ma50": safe_float(latest["ma50"]),
        "ma200": safe_float(latest["ma200"]),

        "ma20_slope_10d": ma20_slope,
        "ma50_slope_20d": ma50_slope,
        "ma200_slope_60d": ma200_slope,

        "return_30d": pct_change_days(df["Close"], 30),
        "return_90d": pct_change_days(df["Close"], 90),

        "wyckoff_details": wy_details,
        "structure_details": struct_details,

        "double_bottom_details": db["details"],
        "triple_bottom_details": tb["details"],
        "double_top_details": dt["details"],
        "triple_top_details": tt["details"],

        "adam_eve_bottom_details": ae_bottom["details"],
        "adam_eve_top_details": ae_top["details"],
    }

    return row


def render_report(metrics):
    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

    lines = []

    lines.append("# Report struttura tecnica")
    lines.append("")
    lines.append(f"Generato: {now}")
    lines.append("")
    lines.append("Questo report aggiunge al tuo scanner una lettura classica di analisi tecnica.")
    lines.append("")
    lines.append("Moduli inclusi:")
    lines.append("")
    lines.append("- Struttura trend con MA20 / MA50 / MA200")
    lines.append("- Massimi e minimi crescenti oppure decrescenti")
    lines.append("- Doppio minimo, triplo minimo, doppio massimo, triplo massimo")
    lines.append("- Pattern Adam and Eve Bottom / Top")
    lines.append("- Divergenze RSI e divergenze RSI nascoste")
    lines.append("- Momentum MACD")
    lines.append("- Conferma volume con OBV / CMF")
    lines.append("- Candidato fase Wyckoff")
    lines.append("- Punteggio tecnico di confluenza")
    lines.append("")

    lines.append("## Sintesi")
    lines.append("")

    summary_rows = []

    for _, r in metrics.iterrows():
        ticker = r["ticker"]

        summary_rows.append({
            "Asset": r["asset"],
            "Prezzo": fmt_price(ticker, r["price"]),
            "Punteggio": int(r["technical_score"]),
            "Verdetto": it_label(r["verdict"]),
            "Trend": it_label(r["trend"]),
            "Momentum": it_label(r["momentum"]),
            "Struttura": it_label(r["structure"]),
            "Divergenza": it_label(r["divergence"]),
            "Wyckoff": it_label(r["wyckoff"]),
            "Supporto": fmt_price(ticker, r["support"]),
            "Resistenza": fmt_price(ticker, r["resistance"]),
        })

    lines.append(df_to_markdown(pd.DataFrame(summary_rows)))
    lines.append("")

    lines.append("## Riepilogo pattern")
    lines.append("")

    pattern_rows = []

    for _, r in metrics.iterrows():
        adam_bottom = it_label(r["adam_eve_bottom_variant"]) if r["adam_eve_bottom"] != "ASSENTE" else "Assente"
        adam_top = it_label(r["adam_eve_top_variant"]) if r["adam_eve_top"] != "ASSENTE" else "Assente"

        pattern_rows.append({
            "Asset": r["asset"],
            "Doppio minimo": it_label(r["double_bottom"]),
            "Triplo minimo": it_label(r["triple_bottom"]),
            "Adam/Eve Bottom": adam_bottom,
            "Doppio massimo": it_label(r["double_top"]),
            "Triplo massimo": it_label(r["triple_top"]),
            "Adam/Eve Top": adam_top,
            "Punteggio pattern": int(r["pattern_score"]),
        })

    lines.append(df_to_markdown(pd.DataFrame(pattern_rows)))
    lines.append("")

    lines.append("## Indicatori tecnici")
    lines.append("")

    ind_rows = []

    for _, r in metrics.iterrows():
        ticker = r["ticker"]

        ind_rows.append({
            "Asset": r["asset"],
            "RSI 14": fmt_num(r["rsi14"], 2),
            "Istogramma MACD": fmt_num(r["macd_hist"], 5),
            "MA20": fmt_price(ticker, r["ma20"]),
            "MA50": fmt_price(ticker, r["ma50"]),
            "MA200": fmt_price(ticker, r["ma200"]),
            "Pendenza MA50 20g": fmt_pct(r["ma50_slope_20d"]),
            "Pendenza MA200 60g": fmt_pct(r["ma200_slope_60d"]),
            "Rendimento 30g": fmt_pct(r["return_30d"]),
            "Rendimento 90g": fmt_pct(r["return_90d"]),
        })

    lines.append(df_to_markdown(pd.DataFrame(ind_rows)))
    lines.append("")

    lines.append("## Dettaglio asset")
    lines.append("")

    for _, r in metrics.iterrows():
        ticker = r["ticker"]

        lines.append(f"### {r['asset']}")
        lines.append("")
        lines.append(f"- Prezzo: **{fmt_price(ticker, r['price'])}**")
        lines.append(f"- Punteggio tecnico: **{int(r['technical_score'])} / 12**")
        lines.append(f"- Verdetto: **{it_label(r['verdict'])}**")
        lines.append(f"- Trend: **{it_label(r['trend'])}** ({int(r['trend_score'])})")
        lines.append(f"- Momentum: **{it_label(r['momentum'])}** ({int(r['momentum_score'])})")
        lines.append(f"- Volume: **{it_label(r['volume'])}** ({int(r['volume_score'])})")
        lines.append(f"- Struttura: **{it_label(r['structure'])}** ({int(r['structure_score'])})")

        if r["structure_details"]:
            lines.append(f"  - Dettaglio struttura: {r['structure_details']}")

        lines.append(f"- Divergenza: **{it_label(r['divergence'])}** ({int(r['divergence_score'])})")
        lines.append(f"- Fase Wyckoff candidata: **{it_label(r['wyckoff'])}** ({int(r['wyckoff_score'])})")

        if r["wyckoff_details"]:
            lines.append(f"  - Dettaglio Wyckoff: {r['wyckoff_details']}")

        lines.append(f"- Supporto più vicino: **{fmt_price(ticker, r['support'])}**")
        lines.append(f"- Resistenza più vicina: **{fmt_price(ticker, r['resistance'])}**")
        lines.append("")

        lines.append("Pattern classici:")
        lines.append("")
        lines.append(f"- Doppio minimo: **{it_label(r['double_bottom'])}**")

        if r["double_bottom_details"]:
            lines.append(f"  - {r['double_bottom_details']}")

        lines.append(f"- Triplo minimo: **{it_label(r['triple_bottom'])}**")

        if r["triple_bottom_details"]:
            lines.append(f"  - {r['triple_bottom_details']}")

        adam_bottom = it_label(r["adam_eve_bottom_variant"]) if r["adam_eve_bottom"] != "ASSENTE" else "Assente"
        lines.append(f"- Adam/Eve Bottom: **{adam_bottom}**")

        if r["adam_eve_bottom_details"]:
            lines.append(f"  - {r['adam_eve_bottom_details']}")

        lines.append(f"- Doppio massimo: **{it_label(r['double_top'])}**")

        if r["double_top_details"]:
            lines.append(f"  - {r['double_top_details']}")

        lines.append(f"- Triplo massimo: **{it_label(r['triple_top'])}**")

        if r["triple_top_details"]:
            lines.append(f"  - {r['triple_top_details']}")

        adam_top = it_label(r["adam_eve_top_variant"]) if r["adam_eve_top"] != "ASSENTE" else "Assente"
        lines.append(f"- Adam/Eve Top: **{adam_top}**")

        if r["adam_eve_top_details"]:
            lines.append(f"  - {r['adam_eve_top_details']}")

        lines.append("")

    lines.append("## Come leggere il punteggio")
    lines.append("")
    lines.append("- Da +7 a +12: forte confluenza tecnica rialzista.")
    lines.append("- Da +3 a +6: struttura costruttiva, ma serve ancora conferma.")
    lines.append("- Da -2 a +2: situazione mista / neutrale.")
    lines.append("- Da -6 a -3: struttura tecnica debole.")
    lines.append("- Da -12 a -7: forte confluenza tecnica ribassista.")
    lines.append("")
    lines.append("Nota importante: questo report non è una previsione da solo. È un filtro tecnico da leggere insieme a scanner frattale, market regime, futures e RSI.")
    lines.append("")

    return "\n".join(lines) + "\n"


def inject_into_latest_report(section_md):
    if not LATEST_REPORT.exists():
        return

    try:
        old = LATEST_REPORT.read_text(encoding="utf-8")
    except Exception:
        return

    clean = section_md.strip()

    if START_MARKER in old and END_MARKER in old:
        start = old.find(START_MARKER)
        end = old.find(END_MARKER)

        if start != -1 and end != -1 and end > start:
            end = end + len(END_MARKER)
            new = old[:start] + START_MARKER + "\n" + clean + "\n" + END_MARKER + old[end:]
        else:
            new = old.rstrip() + "\n\n" + START_MARKER + "\n" + clean + "\n" + END_MARKER + "\n"
    else:
        new = old.rstrip() + "\n\n" + START_MARKER + "\n" + clean + "\n" + END_MARKER + "\n"

    LATEST_REPORT.write_text(new, encoding="utf-8")


def main():
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    rows = []

    for ticker in TICKERS:
        print(f"Analisi tecnica di {ticker}...")
        row = analyze_asset(ticker)

        if row is not None:
            rows.append(row)

    if not rows:
        md = "# Report struttura tecnica\n\nNessun dato valido scaricato.\n"
        OUTPUT_REPORT.write_text(md, encoding="utf-8")
        inject_into_latest_report(md)
        print("Nessun dato valido scaricato.")
        return

    metrics = pd.DataFrame(rows)
    metrics.to_csv(OUTPUT_METRICS, index=False)

    md = render_report(metrics)
    OUTPUT_REPORT.write_text(md, encoding="utf-8")
    inject_into_latest_report(md)

    print(f"Creato {OUTPUT_REPORT}")
    print(f"Creato {OUTPUT_METRICS}")


if __name__ == "__main__":
    main()
