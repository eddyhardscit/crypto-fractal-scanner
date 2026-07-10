from pathlib import Path
from datetime import datetime, timezone

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

# Ciclo di vita dei pattern.
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


# -----------------------------------------------------------------------------
# Utility
# -----------------------------------------------------------------------------


def safe_float(x):
    try:
        if pd.isna(x):
            return np.nan
        return float(x)
    except Exception:
        return np.nan


def safe_int(x, default=0):
    x = safe_float(x)
    if pd.isna(x):
        return default
    return int(x)


def safe_date_str(value):
    if value is None or value == "":
        return ""
    try:
        return pd.Timestamp(value).strftime("%Y-%m-%d")
    except Exception:
        return str(value)


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


def fmt_signed_int(x):
    x = safe_int(x, 0)
    return f"+{x}" if x > 0 else str(x)


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
        "EXPANDING_VOLATILITY": "VolatilitÃ  in espansione",
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

        "ASSENTE": "ASSENTE",
        "CANDIDATO": "CANDIDATO",
        "ATTIVO": "ATTIVO",
        "CONFERMATO_RECENTE": "CONFERMATO RECENTE",
        "MATURO": "MATURO",
        "TARGET_RAGGIUNTO": "TARGET RAGGIUNTO",
        "INVALIDATO": "INVALIDATO",

        "ADAM_AND_EVE_BOTTOM": "Adam and Eve Bottom",
        "EVE_AND_ADAM_BOTTOM": "Eve and Adam Bottom",
        "ADAM_AND_EVE_TOP": "Adam and Eve Top",
        "EVE_AND_ADAM_TOP": "Eve and Adam Top",

        "BULLISH": "rialzista",
        "BEARISH": "ribassista",
        "ABOVE_NECKLINE": "sopra neckline",
        "BELOW_NECKLINE": "sotto neckline",
        "NEAR_NECKLINE": "vicino alla neckline",
        "UNKNOWN_RELATION": "relazione non disponibile",
    }

    if pd.isna(value):
        return "n/a"

    value = str(value)

    if "," in value:
        parts = [p.strip() for p in value.split(",")]
        return ", ".join(mapping.get(p, p) for p in parts)

    return mapping.get(value, value)


# -----------------------------------------------------------------------------
# Dati e indicatori
# -----------------------------------------------------------------------------


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

    return piv[[price_col, "Close", "rsi14", "macd_hist", "Volume"]].rename(
        columns={price_col: "pivot_price"}
    )


def near(a, b, tolerance_pct):
    a = safe_float(a)
    b = safe_float(b)

    if pd.isna(a) or pd.isna(b) or b == 0:
        return False

    return abs(a / b - 1) * 100 <= tolerance_pct


# -----------------------------------------------------------------------------
# Ciclo di vita pattern
# -----------------------------------------------------------------------------


def empty_pattern_result(direction):
    return {
        "status": "ASSENTE",
        "direction": direction,
        "confidence": "LOW",
        "details": "",
        "variant": "",
        "neckline": np.nan,
        "anchor": np.nan,
        "support": np.nan,
        "resistance": np.nan,
        "target": np.nan,
        "invalidation_level": np.nan,
        "target_progress_pct": np.nan,
        "current_relation": "UNKNOWN_RELATION",
        "start_date": "",
        "end_date": "",
        "formation_age_days": np.nan,
        "breakout_date": "",
        "breakout_age_days": np.nan,
        "confirmed": False,
        "target_reached": False,
        "invalidated": False,
        "score": 0,
        "geometry_rank": 0.0,
    }


def current_relation_to_neckline(close, neckline):
    close = safe_float(close)
    neckline = safe_float(neckline)

    if pd.isna(close) or pd.isna(neckline) or neckline == 0:
        return "UNKNOWN_RELATION"

    distance_pct = (close / neckline - 1) * 100

    if abs(distance_pct) <= 1.0:
        return "NEAR_NECKLINE"
    if distance_pct > 0:
        return "ABOVE_NECKLINE"
    return "BELOW_NECKLINE"


def theoretical_target(direction, neckline, anchor):
    neckline = safe_float(neckline)
    anchor = safe_float(anchor)

    if pd.isna(neckline) or pd.isna(anchor):
        return np.nan

    if direction == "BULLISH":
        height = max(0.0, neckline - anchor)
        return neckline + height

    height = max(0.0, anchor - neckline)
    return max(neckline - height, neckline * 0.05)


def target_progress(direction, close, neckline, target):
    close = safe_float(close)
    neckline = safe_float(neckline)
    target = safe_float(target)

    if pd.isna(close) or pd.isna(neckline) or pd.isna(target):
        return np.nan

    if direction == "BULLISH":
        denom = target - neckline
        if denom <= 0:
            return np.nan
        return (close - neckline) / denom * 100

    denom = neckline - target
    if denom <= 0:
        return np.nan
    return (neckline - close) / denom * 100


def first_breakout_date(df, pattern_end, direction, neckline):
    if pd.isna(neckline):
        return None

    pattern_end = pd.Timestamp(pattern_end)
    after = df[df.index >= pattern_end].copy()

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


def has_consecutive_true(series, count):
    if series is None or len(series) < count:
        return False

    values = pd.Series(series).fillna(False).astype(bool)
    runs = values.astype(int).rolling(count).sum()
    return bool((runs >= count).any())


def evaluate_pattern_lifecycle(
    df,
    ticker,
    direction,
    start_date,
    end_date,
    anchor,
    neckline,
    geometry_details,
    geometry_rank,
    variant="",
):
    result = empty_pattern_result(direction)

    start_date = pd.Timestamp(start_date)
    end_date = pd.Timestamp(end_date)
    last_date = pd.Timestamp(df.index[-1])
    close = safe_float(df["Close"].iloc[-1])

    target = theoretical_target(direction, neckline, anchor)
    formation_age = max(0, (last_date - end_date).days)
    breakout_date = first_breakout_date(df, end_date, direction, neckline)

    result.update({
        "variant": variant,
        "neckline": neckline,
        "anchor": anchor,
        "support": anchor if direction == "BULLISH" else np.nan,
        "resistance": anchor if direction == "BEARISH" else np.nan,
        "target": target,
        "start_date": safe_date_str(start_date),
        "end_date": safe_date_str(end_date),
        "formation_age_days": formation_age,
        "current_relation": current_relation_to_neckline(close, neckline),
        "geometry_rank": float(geometry_rank),
    })

    if direction == "BULLISH":
        invalidation_level = neckline * (1 - INVALIDATION_BUFFER_PCT / 100)
    else:
        invalidation_level = neckline * (1 + INVALIDATION_BUFFER_PCT / 100)

    result["invalidation_level"] = invalidation_level

    if breakout_date is None:
        result.update({
            "status": "CANDIDATO",
            "confidence": "LOW/MEDIUM",
            "confirmed": False,
            "score": 0,
            "target_progress_pct": target_progress(direction, close, neckline, target),
            "details": (
                f"{geometry_details} Stato: CANDIDATO; la neckline non Ã¨ ancora stata "
                f"rotta con un margine di almeno {BREAKOUT_BUFFER_PCT:.2f}%. "
                f"EtÃ  della formazione: {formation_age} giorni."
            ),
        })
        return result

    breakout_age = max(0, (last_date - breakout_date).days)
    post_breakout = df[df.index >= breakout_date].copy()

    if direction == "BULLISH":
        target_reached = bool((post_breakout["High"] >= target).any()) if not pd.isna(target) else False
        invalid_flags = post_breakout["Close"] < invalidation_level
    else:
        target_reached = bool((post_breakout["Low"] <= target).any()) if not pd.isna(target) else False
        invalid_flags = post_breakout["Close"] > invalidation_level

    invalidated = has_consecutive_true(invalid_flags, INVALIDATION_CONFIRM_DAYS)

    if target_reached:
        status = "TARGET_RAGGIUNTO"
        score = 0
        confidence = "COMPLETATO"
    elif invalidated:
        status = "INVALIDATO"
        score = 0
        confidence = "ANNULLATO"
    elif breakout_age <= ACTIVE_MAX_DAYS:
        status = "ATTIVO"
        score = 1 if direction == "BULLISH" else -1
        confidence = "MEDIUM"
    elif breakout_age <= RECENT_MAX_DAYS:
        status = "CONFERMATO_RECENTE"
        score = 2 if direction == "BULLISH" else -2
        confidence = "MEDIUM/HIGH"
    else:
        status = "MATURO"
        score = 1 if direction == "BULLISH" else -1
        confidence = "MEDIUM/DECAY"

    progress = target_progress(direction, close, neckline, target)

    result.update({
        "status": status,
        "confidence": confidence,
        "confirmed": status in {"ATTIVO", "CONFERMATO_RECENTE", "MATURO", "TARGET_RAGGIUNTO"},
        "breakout_date": safe_date_str(breakout_date),
        "breakout_age_days": breakout_age,
        "target_reached": target_reached,
        "invalidated": invalidated,
        "target_progress_pct": progress,
        "score": score,
        "details": (
            f"{geometry_details} Breakout neckline: {safe_date_str(breakout_date)} "
            f"({breakout_age} giorni fa). Stato: {it_label(status)}. "
            f"Target teorico: {fmt_price(ticker, target)}; progresso corrente: "
            f"{fmt_pct(progress)}. Relazione prezzo/neckline: "
            f"{it_label(result['current_relation'])}."
        ),
    })

    return result


def pattern_sort_key(result):
    status_priority = PATTERN_STATUS_PRIORITY.get(result.get("status", "ASSENTE"), 0)
    score_strength = abs(safe_int(result.get("score"), 0))

    breakout_date = result.get("breakout_date") or ""
    end_date = result.get("end_date") or ""

    try:
        recency = pd.Timestamp(breakout_date or end_date).value
    except Exception:
        recency = 0

    geometry = safe_float(result.get("geometry_rank"))
    if pd.isna(geometry):
        geometry = 0.0

    return status_priority, score_strength, recency, geometry


def choose_best_pattern(named_results, direction):
    candidates = []

    for name, result in named_results:
        if result.get("direction") != direction:
            continue
        if result.get("status") == "ASSENTE":
            continue
        candidates.append((name, result))

    if not candidates:
        return "", empty_pattern_result(direction)

    return max(candidates, key=lambda item: pattern_sort_key(item[1]))


def pattern_score_from_results(named_results):
    bull_name, bull = choose_best_pattern(named_results, "BULLISH")
    bear_name, bear = choose_best_pattern(named_results, "BEARISH")

    bull_score = safe_int(bull.get("score"), 0)
    bear_score = safe_int(bear.get("score"), 0)
    net = int(max(-3, min(3, bull_score + bear_score)))

    parts = []

    if bull_name:
        parts.append(
            f"rialzista dominante: {bull_name} ({it_label(bull.get('status'))}, {fmt_signed_int(bull_score)})"
        )

    if bear_name:
        parts.append(
            f"ribassista dominante: {bear_name} ({it_label(bear.get('status'))}, {fmt_signed_int(bear_score)})"
        )

    explanation = "; ".join(parts) if parts else "nessun pattern operativo dominante"

    return net, bull_name, bull, bear_name, bear, explanation


# -----------------------------------------------------------------------------
# Riconoscimento geometrico pattern
# -----------------------------------------------------------------------------


def pattern_double_bottom(df, ticker):
    lows = pivot_rows(df, "low")
    highs = pivot_rows(df, "high")

    if len(lows) < 2:
        return empty_pattern_result("BULLISH")

    recent_lows = lows.tail(5)
    best = None
    last_date = pd.Timestamp(df.index[-1])

    for i in range(len(recent_lows) - 1):
        for j in range(i + 1, len(recent_lows)):
            d1 = recent_lows.index[i]
            d2 = recent_lows.index[j]
            p1 = safe_float(recent_lows.iloc[i]["pivot_price"])
            p2 = safe_float(recent_lows.iloc[j]["pivot_price"])
            sep = (d2 - d1).days

            if sep < 10 or sep > 160 or not near(p1, p2, 7.0):
                continue

            between_highs = highs[(highs.index > d1) & (highs.index < d2)]
            if between_highs.empty:
                continue

            neckline = safe_float(between_highs["pivot_price"].max())
            support = min(p1, p2)
            recency_bonus = max(0, 90 - (last_date - d2).days) / 10
            rank = 100 - abs(p1 / p2 - 1) * 100 + min(sep, 80) / 10 + recency_bonus
            candidate = (rank, d1, d2, support, neckline)

            if best is None or candidate[0] > best[0]:
                best = candidate

    if best is None:
        return empty_pattern_result("BULLISH")

    rank, d1, d2, support, neckline = best
    details = (
        f"Due minimi simili vicino a {fmt_price(ticker, support)} tra "
        f"{d1.date()} e {d2.date()}. Neckline stimata: {fmt_price(ticker, neckline)}."
    )

    return evaluate_pattern_lifecycle(
        df, ticker, "BULLISH", d1, d2, support, neckline, details, rank
    )


def pattern_triple_bottom(df, ticker):
    lows = pivot_rows(df, "low")
    highs = pivot_rows(df, "high")

    if len(lows) < 3:
        return empty_pattern_result("BULLISH")

    recent = lows.tail(7)
    best = None
    last_date = pd.Timestamp(df.index[-1])

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
                if min(prices) <= 0 or max(prices) / min(prices) - 1 > 0.09:
                    continue

                between_highs = highs[(highs.index > dates[0]) & (highs.index < dates[-1])]
                if between_highs.empty:
                    continue

                neckline = safe_float(between_highs["pivot_price"].max())
                support = min(prices)
                recency_bonus = max(0, 100 - (last_date - dates[-1]).days) / 10
                rank = 100 - (max(prices) / min(prices) - 1) * 100 + recency_bonus
                candidate = (rank, dates, support, neckline)

                if best is None or candidate[0] > best[0]:
                    best = candidate

    if best is None:
        return empty_pattern_result("BULLISH")

    rank, dates, support, neckline = best
    details = (
        f"Tre minimi simili vicino a {fmt_price(ticker, support)} dal "
        f"{dates[0].date()} al {dates[-1].date()}. Neckline stimata: "
        f"{fmt_price(ticker, neckline)}."
    )

    return evaluate_pattern_lifecycle(
        df, ticker, "BULLISH", dates[0], dates[-1], support, neckline, details, rank
    )


def pattern_double_top(df, ticker):
    highs = pivot_rows(df, "high")
    lows = pivot_rows(df, "low")

    if len(highs) < 2:
        return empty_pattern_result("BEARISH")

    recent_highs = highs.tail(5)
    best = None
    last_date = pd.Timestamp(df.index[-1])

    for i in range(len(recent_highs) - 1):
        for j in range(i + 1, len(recent_highs)):
            d1 = recent_highs.index[i]
            d2 = recent_highs.index[j]
            p1 = safe_float(recent_highs.iloc[i]["pivot_price"])
            p2 = safe_float(recent_highs.iloc[j]["pivot_price"])
            sep = (d2 - d1).days

            if sep < 10 or sep > 160 or not near(p1, p2, 7.0):
                continue

            between_lows = lows[(lows.index > d1) & (lows.index < d2)]
            if between_lows.empty:
                continue

            neckline = safe_float(between_lows["pivot_price"].min())
            resistance = max(p1, p2)
            recency_bonus = max(0, 90 - (last_date - d2).days) / 10
            rank = 100 - abs(p1 / p2 - 1) * 100 + min(sep, 80) / 10 + recency_bonus
            candidate = (rank, d1, d2, resistance, neckline)

            if best is None or candidate[0] > best[0]:
                best = candidate

    if best is None:
        return empty_pattern_result("BEARISH")

    rank, d1, d2, resistance, neckline = best
    details = (
        f"Due massimi simili vicino a {fmt_price(ticker, resistance)} tra "
        f"{d1.date()} e {d2.date()}. Neckline ribassista stimata: "
        f"{fmt_price(ticker, neckline)}."
    )

    return evaluate_pattern_lifecycle(
        df, ticker, "BEARISH", d1, d2, resistance, neckline, details, rank
    )


def pattern_triple_top(df, ticker):
    highs = pivot_rows(df, "high")
    lows = pivot_rows(df, "low")

    if len(highs) < 3:
        return empty_pattern_result("BEARISH")

    recent = highs.tail(7)
    best = None
    last_date = pd.Timestamp(df.index[-1])

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
                if min(prices) <= 0 or max(prices) / min(prices) - 1 > 0.09:
                    continue

                between_lows = lows[(lows.index > dates[0]) & (lows.index < dates[-1])]
                if between_lows.empty:
                    continue

                neckline = safe_float(between_lows["pivot_price"].min())
                resistance = max(prices)
                recency_bonus = max(0, 100 - (last_date - dates[-1]).days) / 10
                rank = 100 - (max(prices) / min(prices) - 1) * 100 + recency_bonus
                candidate = (rank, dates, resistance, neckline)

                if best is None or candidate[0] > best[0]:
                    best = candidate

    if best is None:
        return empty_pattern_result("BEARISH")

    rank, dates, resistance, neckline = best
    details = (
        f"Tre massimi simili vicino a {fmt_price(ticker, resistance)} dal "
        f"{dates[0].date()} al {dates[-1].date()}. Neckline ribassista stimata: "
        f"{fmt_price(ticker, neckline)}."
    )

    return evaluate_pattern_lifecycle(
        df, ticker, "BEARISH", dates[0], dates[-1], resistance, neckline, details, rank
    )


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
    sharp_score += int(left_drop >= 8)
    sharp_score += int(right_rebound >= 8)
    sharp_score += int(not pd.isna(atr) and low > 0 and (atr / low * 100) >= 4)

    near_low = window[window["Low"] <= low * 1.07]
    round_score = 0
    round_score += int(len(near_low) >= 5)
    round_score += int(len(near_low) >= 8)
    round_score += int(not pd.isna(atr) and low > 0 and (atr / low * 100) < 6)

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
    sharp_score += int(left_rise >= 8)
    sharp_score += int(right_drop >= 8)
    sharp_score += int(not pd.isna(atr) and high > 0 and (atr / high * 100) >= 4)

    near_high = window[window["High"] >= high * 0.93]
    round_score = 0
    round_score += int(len(near_high) >= 5)
    round_score += int(len(near_high) >= 8)
    round_score += int(not pd.isna(atr) and high > 0 and (atr / high * 100) < 6)

    return {"sharp_score": sharp_score, "round_score": round_score}


def pattern_adam_eve_bottom(df, ticker):
    lows = pivot_rows(df, "low")
    highs = pivot_rows(df, "high")

    if len(lows) < 2:
        return empty_pattern_result("BULLISH")

    recent_lows = lows.tail(6)
    best = None
    last_date = pd.Timestamp(df.index[-1])

    for i in range(len(recent_lows) - 1):
        for j in range(i + 1, len(recent_lows)):
            d1 = recent_lows.index[i]
            d2 = recent_lows.index[j]
            p1 = safe_float(recent_lows.iloc[i]["pivot_price"])
            p2 = safe_float(recent_lows.iloc[j]["pivot_price"])
            sep = (d2 - d1).days

            if sep < 12 or sep > 180 or not near(p1, p2, 9.0):
                continue

            m1 = bottom_shape_metrics(df, d1)
            m2 = bottom_shape_metrics(df, d2)
            variant = ""
            shape_rank = 0

            if m1["sharp_score"] >= 2 and m2["round_score"] >= 2:
                variant = "ADAM_AND_EVE_BOTTOM"
                shape_rank = m1["sharp_score"] + m2["round_score"]
            elif m1["round_score"] >= 2 and m2["sharp_score"] >= 2:
                variant = "EVE_AND_ADAM_BOTTOM"
                shape_rank = m1["round_score"] + m2["sharp_score"]

            if not variant:
                continue

            between_highs = highs[(highs.index > d1) & (highs.index < d2)]
            if between_highs.empty:
                continue

            neckline = safe_float(between_highs["pivot_price"].max())
            support = min(p1, p2)
            recency_bonus = max(0, 100 - (last_date - d2).days) / 10
            rank = shape_rank * 10 + recency_bonus - abs(p1 / p2 - 1) * 100
            candidate = (rank, d1, d2, support, neckline, variant)

            if best is None or candidate[0] > best[0]:
                best = candidate

    if best is None:
        return empty_pattern_result("BULLISH")

    rank, d1, d2, support, neckline, variant = best
    details = (
        f"Pattern {it_label(variant)} vicino a {fmt_price(ticker, support)} dal "
        f"{d1.date()} al {d2.date()}. Un minimo Ã¨ piÃ¹ appuntito e l'altro piÃ¹ "
        f"arrotondato. Neckline stimata: {fmt_price(ticker, neckline)}."
    )

    return evaluate_pattern_lifecycle(
        df,
        ticker,
        "BULLISH",
        d1,
        d2,
        support,
        neckline,
        details,
        rank,
        variant=variant,
    )


def pattern_adam_eve_top(df, ticker):
    highs = pivot_rows(df, "high")
    lows = pivot_rows(df, "low")

    if len(highs) < 2:
        return empty_pattern_result("BEARISH")

    recent_highs = highs.tail(6)
    best = None
    last_date = pd.Timestamp(df.index[-1])

    for i in range(len(recent_highs) - 1):
        for j in range(i + 1, len(recent_highs)):
            d1 = recent_highs.index[i]
            d2 = recent_highs.index[j]
            p1 = safe_float(recent_highs.iloc[i]["pivot_price"])
            p2 = safe_float(recent_highs.iloc[j]["pivot_price"])
            sep = (d2 - d1).days

            if sep < 12 or sep > 180 or not near(p1, p2, 9.0):
                continue

            m1 = top_shape_metrics(df, d1)
            m2 = top_shape_metrics(df, d2)
            variant = ""
            shape_rank = 0

            if m1["sharp_score"] >= 2 and m2["round_score"] >= 2:
                variant = "ADAM_AND_EVE_TOP"
                shape_rank = m1["sharp_score"] + m2["round_score"]
            elif m1["round_score"] >= 2 and m2["sharp_score"] >= 2:
                variant = "EVE_AND_ADAM_TOP"
                shape_rank = m1["round_score"] + m2["sharp_score"]

            if not variant:
                continue

            between_lows = lows[(lows.index > d1) & (lows.index < d2)]
            if between_lows.empty:
                continue

            neckline = safe_float(between_lows["pivot_price"].min())
            resistance = max(p1, p2)
            recency_bonus = max(0, 100 - (last_date - d2).days) / 10
            rank = shape_rank * 10 + recency_bonus - abs(p1 / p2 - 1) * 100
            candidate = (rank, d1, d2, resistance, neckline, variant)

            if best is None or candidate[0] > best[0]:
                best = candidate

    if best is None:
        return empty_pattern_result("BEARISH")

    rank, d1, d2, resistance, neckline, variant = best
    details = (
        f"Pattern {it_label(variant)} vicino a {fmt_price(ticker, resistance)} dal "
        f"{d1.date()} al {d2.date()}. Un massimo Ã¨ piÃ¹ appuntito e l'altro piÃ¹ "
        f"arrotondato. Neckline ribassista stimata: {fmt_price(ticker, neckline)}."
    )

    return evaluate_pattern_lifecycle(
        df,
        ticker,
        "BEARISH",
        d1,
        d2,
        resistance,
        neckline,
        details,
        rank,
        variant=variant,
    )


# -----------------------------------------------------------------------------
# Struttura, trend, momentum, volume, Wyckoff
# -----------------------------------------------------------------------------


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


# -----------------------------------------------------------------------------
# Analisi asset e metriche
# -----------------------------------------------------------------------------


def add_pattern_columns(row, prefix, result):
    row[prefix] = result.get("status", "ASSENTE")
    row[f"{prefix}_score"] = safe_int(result.get("score"), 0)
    row[f"{prefix}_direction"] = result.get("direction", "")
    row[f"{prefix}_variant"] = result.get("variant", "")
    row[f"{prefix}_start_date"] = result.get("start_date", "")
    row[f"{prefix}_end_date"] = result.get("end_date", "")
    row[f"{prefix}_formation_age_days"] = result.get("formation_age_days", np.nan)
    row[f"{prefix}_breakout_date"] = result.get("breakout_date", "")
    row[f"{prefix}_breakout_age_days"] = result.get("breakout_age_days", np.nan)
    row[f"{prefix}_neckline"] = result.get("neckline", np.nan)
    row[f"{prefix}_target"] = result.get("target", np.nan)
    row[f"{prefix}_target_progress_pct"] = result.get("target_progress_pct", np.nan)
    row[f"{prefix}_invalidation_level"] = result.get("invalidation_level", np.nan)
    row[f"{prefix}_current_relation"] = result.get("current_relation", "")
    row[f"{prefix}_target_reached"] = bool(result.get("target_reached", False))
    row[f"{prefix}_invalidated"] = bool(result.get("invalidated", False))
    row[f"{prefix}_details"] = result.get("details", "")


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

    named_patterns = [
        ("Doppio minimo", db),
        ("Triplo minimo", tb),
        (it_label(ae_bottom.get("variant")) if ae_bottom.get("variant") else "Adam/Eve Bottom", ae_bottom),
        ("Doppio massimo", dt),
        ("Triplo massimo", tt),
        (it_label(ae_top.get("variant")) if ae_top.get("variant") else "Adam/Eve Top", ae_top),
    ]

    (
        pattern_score,
        dominant_bullish_name,
        dominant_bullish,
        dominant_bearish_name,
        dominant_bearish,
        pattern_score_explanation,
    ) = pattern_score_from_results(named_patterns)

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
        "pattern_score_explanation": pattern_score_explanation,
        "dominant_bullish_pattern": dominant_bullish_name,
        "dominant_bullish_status": dominant_bullish.get("status", "ASSENTE"),
        "dominant_bullish_score": safe_int(dominant_bullish.get("score"), 0),
        "dominant_bearish_pattern": dominant_bearish_name,
        "dominant_bearish_status": dominant_bearish.get("status", "ASSENTE"),
        "dominant_bearish_score": safe_int(dominant_bearish.get("score"), 0),

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
    }

    add_pattern_columns(row, "double_bottom", db)
    add_pattern_columns(row, "triple_bottom", tb)
    add_pattern_columns(row, "double_top", dt)
    add_pattern_columns(row, "triple_top", tt)
    add_pattern_columns(row, "adam_eve_bottom", ae_bottom)
    add_pattern_columns(row, "adam_eve_top", ae_top)

    # CompatibilitÃ  con i nomi giÃ  letti da altri script.
    row["adam_eve_bottom_variant"] = ae_bottom.get("variant", "")
    row["adam_eve_top_variant"] = ae_top.get("variant", "")

    return row


# -----------------------------------------------------------------------------
# Report
# -----------------------------------------------------------------------------


def pattern_cell(status, variant=""):
    status_txt = it_label(status)
    if variant:
        return f"{it_label(variant)} â {status_txt}"
    return status_txt


def append_pattern_detail(lines, ticker, label, row, prefix, variant_col=None):
    status = row.get(prefix, "ASSENTE")
    variant = row.get(variant_col, "") if variant_col else ""
    title = it_label(variant) if variant else label

    lines.append(f"- {title}: **{it_label(status)}** ({fmt_signed_int(row.get(f'{prefix}_score', 0))})")

    details = row.get(f"{prefix}_details", "")
    if details:
        lines.append(f"  - {details}")

    if status != "ASSENTE":
        neckline = row.get(f"{prefix}_neckline")
        target = row.get(f"{prefix}_target")
        breakout = row.get(f"{prefix}_breakout_date", "")
        age = row.get(f"{prefix}_breakout_age_days")
        progress = row.get(f"{prefix}_target_progress_pct")
        relation = row.get(f"{prefix}_current_relation", "")

        extra = [
            f"neckline {fmt_price(ticker, neckline)}",
            f"target {fmt_price(ticker, target)}",
            f"progresso {fmt_pct(progress)}",
            f"prezzo {it_label(relation)}",
        ]

        if breakout:
            extra.insert(2, f"breakout {breakout} ({safe_int(age, 0)}g)")

        lines.append("  - " + "; ".join(extra) + ".")


def render_report(metrics):
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
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
    lines.append("- Ciclo di vita pattern: candidato, attivo, confermato recente, maturo, target raggiunto, invalidato")
    lines.append("- Data breakout, etÃ , target teorico, progresso e recupero della neckline")
    lines.append("- Divergenze RSI e divergenze RSI nascoste")
    lines.append("- Momentum MACD")
    lines.append("- Conferma volume con OBV / CMF")
    lines.append("- Candidato fase Wyckoff")
    lines.append("- Punteggio tecnico di confluenza")
    lines.append("")
    lines.append(
        "Regola anti-pattern-zombie: un pattern vecchio non resta indefinitamente confermato. "
        "Dopo il target vale 0; se viene recuperata stabilmente la neckline viene invalidato; "
        "se resta valido ma invecchia passa a MATURO con peso ridotto."
    )
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
            "Pattern score": fmt_signed_int(r["pattern_score"]),
            "Pattern rialzista": (
                f"{r['dominant_bullish_pattern']} / {it_label(r['dominant_bullish_status'])}"
                if r["dominant_bullish_pattern"] else "nessuno"
            ),
            "Pattern ribassista": (
                f"{r['dominant_bearish_pattern']} / {it_label(r['dominant_bearish_status'])}"
                if r["dominant_bearish_pattern"] else "nessuno"
            ),
            "Supporto": fmt_price(ticker, r["support"]),
            "Resistenza": fmt_price(ticker, r["resistance"]),
        })

    lines.append(df_to_markdown(pd.DataFrame(summary_rows)))
    lines.append("")

    lines.append("## Riepilogo ciclo di vita pattern")
    lines.append("")

    pattern_rows = []

    for _, r in metrics.iterrows():
        pattern_rows.append({
            "Asset": r["asset"],
            "Doppio minimo": pattern_cell(r["double_bottom"]),
            "Triplo minimo": pattern_cell(r["triple_bottom"]),
            "Adam/Eve Bottom": pattern_cell(r["adam_eve_bottom"], r["adam_eve_bottom_variant"]),
            "Doppio massimo": pattern_cell(r["double_top"]),
            "Triplo massimo": pattern_cell(r["triple_top"]),
            "Adam/Eve Top": pattern_cell(r["adam_eve_top"], r["adam_eve_top_variant"]),
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

        lines.append(f"- Punteggio pattern: **{fmt_signed_int(r['pattern_score'])}**")
        lines.append(f"  - {r['pattern_score_explanation']}.")
        lines.append(f"- Supporto piÃ¹ vicino: **{fmt_price(ticker, r['support'])}**")
        lines.append(f"- Resistenza piÃ¹ vicina: **{fmt_price(ticker, r['resistance'])}**")
        lines.append("")

        lines.append("Pattern classici e ciclo di vita:")
        lines.append("")
        append_pattern_detail(lines, ticker, "Doppio minimo", r, "double_bottom")
        append_pattern_detail(lines, ticker, "Triplo minimo", r, "triple_bottom")
        append_pattern_detail(
            lines,
            ticker,
            "Adam/Eve Bottom",
            r,
            "adam_eve_bottom",
            variant_col="adam_eve_bottom_variant",
        )
        append_pattern_detail(lines, ticker, "Doppio massimo", r, "double_top")
        append_pattern_detail(lines, ticker, "Triplo massimo", r, "triple_top")
        append_pattern_detail(
            lines,
            ticker,
            "Adam/Eve Top",
            r,
            "adam_eve_top",
            variant_col="adam_eve_top_variant",
        )
        lines.append("")

    lines.append("## Stati del ciclo di vita")
    lines.append("")
    lines.append("- **CANDIDATO**: geometria presente, ma neckline non ancora rotta; punteggio 0.")
    lines.append("- **ATTIVO**: breakout avvenuto da 0 a 3 giorni; peso prudente Â±1.")
    lines.append("- **CONFERMATO RECENTE**: breakout da 4 a 14 giorni; peso massimo prudente Â±2.")
    lines.append("- **MATURO**: breakout piÃ¹ vecchio di 14 giorni e ancora valido; peso ridotto Â±1.")
    lines.append("- **TARGET RAGGIUNTO**: movimento teorico giÃ  sviluppato; punteggio 0.")
    lines.append("- **INVALIDATO**: recupero stabile della neckline contro il pattern; punteggio 0.")
    lines.append("")
    lines.append(
        "Per evitare doppio conteggio, nel punteggio entra soltanto il miglior pattern "
        "rialzista e il miglior pattern ribassista. Doppio, triplo e Adam/Eve che descrivono "
        "la stessa struttura non vengono piÃ¹ sommati tutti insieme."
    )
    lines.append("")

    lines.append("## Come leggere il punteggio")
    lines.append("")
    lines.append("- Da +7 a +12: forte confluenza tecnica rialzista.")
    lines.append("- Da +3 a +6: struttura costruttiva, ma serve ancora conferma.")
    lines.append("- Da -2 a +2: situazione mista / neutrale.")
    lines.append("- Da -6 a -3: struttura tecnica debole.")
    lines.append("- Da -12 a -7: forte confluenza tecnica ribassista.")
    lines.append("")
    lines.append(
        "Nota importante: questo report non Ã¨ una previsione da solo. Ã un filtro tecnico "
        "da leggere insieme a scanner frattale, market regime, futures e RSI."
    )
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

    LATEST_REPORT.write_text(new, encoding="utf-8", newline="\n")


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
        OUTPUT_REPORT.write_text(md, encoding="utf-8", newline="\n")
        inject_into_latest_report(md)
        print("Nessun dato valido scaricato.")
        return

    metrics = pd.DataFrame(rows)
    metrics.to_csv(OUTPUT_METRICS, index=False)

    md = render_report(metrics)
    OUTPUT_REPORT.write_text(md, encoding="utf-8", newline="\n")
    inject_into_latest_report(md)

    print(f"Creato {OUTPUT_REPORT}")
    print(f"Creato {OUTPUT_METRICS}")

    for _, row in metrics.iterrows():
        print(
            f"{row['asset']}: tecnico {fmt_signed_int(row['technical_score'])} | "
            f"pattern {fmt_signed_int(row['pattern_score'])} | "
            f"bull {row['dominant_bullish_pattern'] or 'nessuno'} "
            f"({it_label(row['dominant_bullish_status'])}) | "
            f"bear {row['dominant_bearish_pattern'] or 'nessuno'} "
            f"({it_label(row['dominant_bearish_status'])})"
        )


if __name__ == "__main__":
    main()
