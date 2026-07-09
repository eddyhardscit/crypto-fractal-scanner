import csv
import json
import math
import os
import re
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

import numpy as np
import pandas as pd
import yfinance as yf


REPORT_DIR = "reports"
MAIN_REPORT_PATH = "reports/latest_report.md"

REPORT_PATH = "reports/major_alt_lifecycle_squeeze_report.md"
EVENTS_CSV_PATH = "reports/major_alt_lifecycle_squeeze_events.csv"
HISTORY_CSV_PATH = "reports/major_alt_lifecycle_squeeze_history.csv"
LATEST_JSON_PATH = "reports/major_alt_lifecycle_squeeze_latest.json"
CHART_PATH = "reports/major_alt_lifecycle_squeeze_SOL_chart.png"

START_MARKER = "<!-- MAJOR_ALT_LIFECYCLE_SQUEEZE_START -->"
END_MARKER = "<!-- MAJOR_ALT_LIFECYCLE_SQUEEZE_END -->"

SOL_ONCHAIN_END = "<!-- SOL_ONCHAIN_METRICS_END -->"
RSI_END = "<!-- RSI_TOP_CYCLE_END -->"
BTC_SOL_END = "<!-- BTC_SOL_FRACTAL_END -->"
GLOBAL_END = "<!-- GLOBAL_CONFLUENCE_END -->"

TARGET_TICKER = "SOL-USD"

CROSS_NEAR_BAND_PCT = 2.0

MAX_ANALOG_EVENTS_TOTAL = 30
MAX_ANALOG_EVENTS_PER_ASSET = 3
MIN_ANALOG_SIMILARITY = 45.0

CRYPTO_ASSETS = {
    "BTC-USD": "Bitcoin",
    "ETH-USD": "Ethereum",
    "BNB-USD": "BNB",
    "XRP-USD": "XRP",
    "ADA-USD": "Cardano",
    "SOL-USD": "Solana",
    "DOGE-USD": "Dogecoin",
    "TRX-USD": "TRON",
    "LINK-USD": "Chainlink",
    "LTC-USD": "Litecoin",
    "BCH-USD": "Bitcoin Cash",
    "XLM-USD": "Stellar",
    "AVAX-USD": "Avalanche",
    "DOT-USD": "Polkadot",
    "MATIC-USD": "Polygon",
    "NEAR-USD": "NEAR",
    "ATOM-USD": "Cosmos",
    "FIL-USD": "Filecoin",
    "ICP-USD": "Internet Computer",
    "APT-USD": "Aptos",
    "ARB-USD": "Arbitrum",
    "OP-USD": "Optimism",
    "ETC-USD": "Ethereum Classic",
    "UNI7083-USD": "Uniswap",
    "AAVE-USD": "Aave",
    "MKR-USD": "Maker",
    "INJ-USD": "Injective",
    "RUNE-USD": "THORChain",
    "FTM-USD": "Fantom",
    "SAND-USD": "The Sandbox",
    "MANA-USD": "Decentraland",
    "ALGO-USD": "Algorand",
    "VET-USD": "VeChain",
    "THETA-USD": "Theta",
    "EGLD-USD": "MultiversX",
    "AXS-USD": "Axie Infinity",
    "QNT-USD": "Quant",
    "STX-USD": "Stacks",
    "HBAR-USD": "Hedera",
    "GRT6719-USD": "The Graph",
}

ASSET_LAUNCH_DATES = {
    "BTC-USD": "2009-01-03",
    "ETH-USD": "2015-07-30",
    "BNB-USD": "2017-07-25",
    "XRP-USD": "2012-06-01",
    "ADA-USD": "2017-09-29",
    "SOL-USD": "2020-03-16",
    "DOGE-USD": "2013-12-06",
    "TRX-USD": "2017-09-13",
    "LINK-USD": "2017-09-20",
    "LTC-USD": "2011-10-13",
    "BCH-USD": "2017-08-01",
    "XLM-USD": "2014-07-31",
    "AVAX-USD": "2020-09-21",
    "DOT-USD": "2020-08-18",
    "MATIC-USD": "2019-04-26",
    "NEAR-USD": "2020-10-13",
    "ATOM-USD": "2019-03-13",
    "FIL-USD": "2020-10-15",
    "ICP-USD": "2021-05-10",
    "APT-USD": "2022-10-12",
    "ARB-USD": "2023-03-23",
    "OP-USD": "2022-05-31",
    "ETC-USD": "2016-07-20",
    "UNI7083-USD": "2020-09-17",
    "AAVE-USD": "2020-10-02",
    "MKR-USD": "2017-11-25",
    "INJ-USD": "2020-10-21",
    "RUNE-USD": "2019-07-20",
    "FTM-USD": "2018-06-15",
    "SAND-USD": "2020-08-14",
    "MANA-USD": "2017-09-18",
    "ALGO-USD": "2019-06-19",
    "VET-USD": "2018-06-30",
    "THETA-USD": "2018-01-17",
    "EGLD-USD": "2020-07-30",
    "AXS-USD": "2020-11-04",
    "QNT-USD": "2018-08-10",
    "STX-USD": "2019-10-25",
    "HBAR-USD": "2019-09-16",
    "GRT6719-USD": "2020-12-17",
}

EVENT_COLUMNS = [
    "asset",
    "name",
    "event_date",
    "age_reference_date",
    "age_years",
    "close",
    "ema20",
    "ema50",
    "ema100",
    "ema200",
    "price_to_ema200_pct",
    "upside_to_ema200_pct",
    "ema50_ema200_gap_pct",
    "ema50_slope_4w_pct",
    "ema200_slope_8w_pct",
    "rsi14",
    "rsi_4w_change",
    "gain_from_26w_low_pct",
    "cross_state",
    "weeks_since_death_cross",
    "hit_ema200_4w",
    "hit_ema200_8w",
    "hit_ema200_12w",
    "hit_ema200_16w",
    "weeks_to_ema200",
    "max_gain_4w_pct",
    "max_gain_8w_pct",
    "max_gain_12w_pct",
    "max_gain_16w_pct",
    "drawdown_4w_pct",
    "drawdown_8w_pct",
    "drawdown_12w_pct",
    "drawdown_16w_pct",
    "return_4w_pct",
    "return_8w_pct",
    "return_12w_pct",
    "return_16w_pct",
    "similarity_to_sol",
]

HISTORY_COLUMNS = [
    "date",
    "generated_at_utc",
    "sol_price",
    "sol_ema20",
    "sol_ema50",
    "sol_ema100",
    "sol_ema200",
    "sol_price_to_ema200_pct",
    "sol_upside_to_ema200_pct",
    "sol_ema50_ema200_gap_pct",
    "sol_rsi14",
    "sol_rsi_4w_change",
    "sol_gain_from_26w_low_pct",
    "sol_age_reference_date",
    "sol_age_years",
    "cross_state",
    "weeks_since_death_cross",
    "historical_events",
    "analog_events",
    "max_analog_events_per_asset",
    "analog_hit_ema200_8w_pct",
    "analog_hit_ema200_12w_pct",
    "analog_hit_ema200_16w_pct",
    "analog_median_max_gain_12w_pct",
    "analog_median_drawdown_12w_pct",
    "lifecycle_score",
    "lifecycle_bias",
    "global_weight_suggestion",
    "squeeze_trend",
    "squeeze_trend_score",
    "squeeze_trend_previous_date",
    "squeeze_trend_reasons",
    "target_ema200",
    "first_confirmation",
    "second_confirmation",
    "soft_invalidation",
    "hard_invalidation",
]


def now_utc():
    return datetime.now(timezone.utc)


def today_str():
    return now_utc().strftime("%Y-%m-%d")


def utc_str():
    return now_utc().strftime("%Y-%m-%d %H:%M:%S UTC")


def clean_text(value):
    if value is None:
        return ""
    return str(value).replace("\xa0", " ").strip()


def safe_float(value):
    if value is None:
        return None

    try:
        value = float(value)
        if math.isnan(value) or math.isinf(value):
            return None
        return value
    except Exception:
        pass

    text = clean_text(value)
    if text == "":
        return None

    text = text.replace("$", "").replace("€", "").replace("%", "").replace(" ", "")
    match = re.search(r"[-+]?\d[\d\.,]*", text)
    if not match:
        return None

    number = match.group(0)

    if "," in number:
        number = number.replace(".", "")
        number = number.replace(",", ".")
    elif number.count(".") > 1:
        number = number.replace(".", "")

    try:
        return float(number)
    except Exception:
        return None


def to_naive_timestamp(value):
    ts = pd.Timestamp(value)

    if ts.tzinfo is not None:
        try:
            ts = ts.tz_convert(None)
        except Exception:
            ts = ts.tz_localize(None)

    return ts.normalize()


def get_age_reference_date(ticker, df):
    manual = ASSET_LAUNCH_DATES.get(ticker)

    if manual:
        return to_naive_timestamp(manual)

    if df is not None and not df.empty:
        return to_naive_timestamp(df.index[0])

    return None


def years_between(start_date, end_date):
    try:
        start = to_naive_timestamp(start_date)
        end = to_naive_timestamp(end_date)
        return (end - start).days / 365.25
    except Exception:
        return None


def pct_change(new, old):
    new = safe_float(new)
    old = safe_float(old)

    if new is None or old is None or old == 0:
        return None

    return (new / old - 1.0) * 100.0


def fmt_number(value, decimals=2):
    value = safe_float(value)

    if value is None:
        return "n/a"

    formatted = f"{value:,.{decimals}f}"
    return formatted.replace(",", "X").replace(".", ",").replace("X", ".")


def fmt_price(value):
    value = safe_float(value)

    if value is None:
        return "n/a"

    if abs(value) >= 1000:
        return f"{fmt_number(value, 0)} $"

    if abs(value) >= 1:
        return f"{fmt_number(value, 2)} $"

    return f"{fmt_number(value, 6)} $"


def fmt_pct(value, decimals=2, force_sign=True):
    value = safe_float(value)

    if value is None:
        return "n/a"

    sign = "+" if force_sign and value > 0 else ""
    return f"{sign}{fmt_number(value, decimals)}%"


def yes_no(value):
    if value is True:
        return "sì"
    if value is False:
        return "no"
    return "n/a"


def md_table(headers, rows):
    def cell(value):
        value = "" if value is None else str(value)
        return value.replace("|", "\\|").replace("\n", " ")

    lines = []
    lines.append("| " + " | ".join(cell(h) for h in headers) + " |")
    lines.append("| " + " | ".join("---" for _ in headers) + " |")

    for row in rows:
        lines.append("| " + " | ".join(cell(v) for v in row) + " |")

    return "\n".join(lines)


def normalize_yfinance_df(df, ticker):
    if df is None or df.empty:
        return pd.DataFrame()

    df = df.copy()

    if isinstance(df.columns, pd.MultiIndex):
        try:
            if ticker in df.columns.get_level_values(1):
                df = df.xs(ticker, axis=1, level=1, drop_level=True)
            else:
                df.columns = [col[0] for col in df.columns]
        except Exception:
            df.columns = [col[0] if isinstance(col, tuple) else col for col in df.columns]

    rename = {}

    for col in df.columns:
        c = str(col).lower()

        if c == "open":
            rename[col] = "Open"
        elif c == "high":
            rename[col] = "High"
        elif c == "low":
            rename[col] = "Low"
        elif c == "close":
            rename[col] = "Close"
        elif c == "adj close":
            rename[col] = "Adj Close"
        elif c == "volume":
            rename[col] = "Volume"

    df = df.rename(columns=rename)

    required = ["Open", "High", "Low", "Close", "Volume"]

    for col in required:
        if col not in df.columns:
            df[col] = np.nan

    df = df[required]
    df = df.dropna(subset=["Close"])
    df = df[~df.index.duplicated(keep="last")]
    df = df.sort_index()

    return df


def fetch_weekly_crypto(ticker):
    try:
        df = yf.download(
            ticker,
            period="max",
            interval="1wk",
            auto_adjust=True,
            progress=False,
            threads=False,
        )
    except Exception:
        return pd.DataFrame()

    return normalize_yfinance_df(df, ticker)


def compute_rsi(close, length=14):
    delta = close.diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.ewm(alpha=1 / length, adjust=False, min_periods=length).mean()
    avg_loss = loss.ewm(alpha=1 / length, adjust=False, min_periods=length).mean()

    rs = avg_gain / avg_loss.replace(0, np.nan)
    rsi = 100 - (100 / (1 + rs))

    return rsi


def add_indicators(df):
    df = df.copy()

    df["EMA20"] = df["Close"].ewm(span=20, adjust=False, min_periods=20).mean()
    df["EMA50"] = df["Close"].ewm(span=50, adjust=False, min_periods=50).mean()
    df["EMA100"] = df["Close"].ewm(span=100, adjust=False, min_periods=100).mean()
    df["EMA200"] = df["Close"].ewm(span=200, adjust=False, min_periods=200).mean()
    df["RSI14"] = compute_rsi(df["Close"], 14)

    df["EMA50_EMA200_GAP_PCT"] = (df["EMA50"] / df["EMA200"] - 1.0) * 100.0
    df["PRICE_TO_EMA200_PCT"] = (df["Close"] / df["EMA200"] - 1.0) * 100.0
    df["UPSIDE_TO_EMA200_PCT"] = (df["EMA200"] / df["Close"] - 1.0) * 100.0
    df["EMA50_SLOPE_4W_PCT"] = (df["EMA50"] / df["EMA50"].shift(4) - 1.0) * 100.0
    df["EMA200_SLOPE_8W_PCT"] = (df["EMA200"] / df["EMA200"].shift(8) - 1.0) * 100.0
    df["RSI_4W_CHANGE"] = df["RSI14"] - df["RSI14"].shift(4)
    df["LOW_26W"] = df["Low"].rolling(26, min_periods=10).min()
    df["GAIN_FROM_26W_LOW_PCT"] = (df["Close"] / df["LOW_26W"] - 1.0) * 100.0

    return df


def find_weeks_since_death_cross(df, pos):
    if pos <= 1:
        return None

    start = max(1, pos - 80)

    for j in range(pos, start, -1):
        prev_gap = safe_float(df["EMA50_EMA200_GAP_PCT"].iloc[j - 1])
        gap = safe_float(df["EMA50_EMA200_GAP_PCT"].iloc[j])

        if prev_gap is None or gap is None:
            continue

        if prev_gap >= 0 and gap < 0:
            return pos - j

    return None


def classify_cross_state(df, pos):
    gap = safe_float(df["EMA50_EMA200_GAP_PCT"].iloc[pos])
    ema50_slope = safe_float(df["EMA50_SLOPE_4W_PCT"].iloc[pos])
    weeks_since = find_weeks_since_death_cross(df, pos)

    if gap is None:
        return "n/a", None

    if abs(gap) <= CROSS_NEAR_BAND_PCT:
        if gap >= 0:
            return "EMA50/EMA200 SOVRAPPOSTE / INCROCIO IMMINENTE", weeks_since
        return "EMA50/EMA200 SOVRAPPOSTE / INCROCIO IN CORSO", weeks_since

    if gap > CROSS_NEAR_BAND_PCT and gap <= 8 and ema50_slope is not None and ema50_slope < 0:
        return "EMA50 SOPRA EMA200 MA IN AVVICINAMENTO", weeks_since

    if gap > 8:
        return "EMA50 ANCORA SOPRA EMA200", weeks_since

    if gap < -CROSS_NEAR_BAND_PCT and weeks_since is not None:
        if weeks_since <= 4:
            return "DEATH CROSS RECENTE / APPENA CONFERMATO", weeks_since
        if weeks_since <= 12:
            return "DEATH CROSS CONFERMATO DA POCO", weeks_since

    if gap < -8:
        return "EMA50 SOTTO EMA200 DA TEMPO", weeks_since

    return "EMA50 SOTTO EMA200 / CROSS GIÀ AVVENUTO", weeks_since


def get_row_setup(df, pos, ticker, name):
    row = df.iloc[pos]

    event_date = df.index[pos]
    age_ref = get_age_reference_date(ticker, df)
    age_years = years_between(age_ref, event_date)

    cross_state, weeks_since = classify_cross_state(df, pos)

    return {
        "asset": ticker,
        "name": name,
        "event_date": pd.Timestamp(event_date).strftime("%Y-%m-%d"),
        "age_reference_date": age_ref.strftime("%Y-%m-%d") if age_ref is not None else None,
        "age_years": safe_float(age_years),
        "close": safe_float(row.get("Close")),
        "ema20": safe_float(row.get("EMA20")),
        "ema50": safe_float(row.get("EMA50")),
        "ema100": safe_float(row.get("EMA100")),
        "ema200": safe_float(row.get("EMA200")),
        "price_to_ema200_pct": safe_float(row.get("PRICE_TO_EMA200_PCT")),
        "upside_to_ema200_pct": safe_float(row.get("UPSIDE_TO_EMA200_PCT")),
        "ema50_ema200_gap_pct": safe_float(row.get("EMA50_EMA200_GAP_PCT")),
        "ema50_slope_4w_pct": safe_float(row.get("EMA50_SLOPE_4W_PCT")),
        "ema200_slope_8w_pct": safe_float(row.get("EMA200_SLOPE_8W_PCT")),
        "rsi14": safe_float(row.get("RSI14")),
        "rsi_4w_change": safe_float(row.get("RSI_4W_CHANGE")),
        "gain_from_26w_low_pct": safe_float(row.get("GAIN_FROM_26W_LOW_PCT")),
        "cross_state": cross_state,
        "weeks_since_death_cross": weeks_since,
    }


def setup_is_lifecycle_squeeze_candidate(setup):
    age = safe_float(setup.get("age_years"))
    price_to_ema200 = safe_float(setup.get("price_to_ema200_pct"))
    upside = safe_float(setup.get("upside_to_ema200_pct"))
    ema_gap = safe_float(setup.get("ema50_ema200_gap_pct"))
    ema50_slope = safe_float(setup.get("ema50_slope_4w_pct"))
    rsi = safe_float(setup.get("rsi14"))
    cross_state = setup.get("cross_state") or ""

    if age is None or age < 2.0:
        return False

    if price_to_ema200 is None or price_to_ema200 > -12:
        return False

    if upside is None or upside < 15:
        return False

    if ema_gap is None:
        return False

    near_cross = (
        abs(ema_gap) <= 12
        or "SOVRAPPOSTE" in cross_state
        or "IMMINENTE" in cross_state
        or "IN CORSO" in cross_state
        or "RECENTE" in cross_state
        or "CONFERMATO DA POCO" in cross_state
        or "AVVICINAMENTO" in cross_state
    )

    if not near_cross:
        return False

    if ema50_slope is not None and ema50_slope > 3:
        return False

    if rsi is None or rsi < 25 or rsi > 62:
        return False

    return True


def add_forward_outcomes(df, pos, setup):
    close = safe_float(setup.get("close"))
    target = safe_float(setup.get("ema200"))

    if close is None or close <= 0:
        return setup

    for horizon in [4, 8, 12, 16]:
        future = df.iloc[pos + 1 : pos + 1 + horizon]

        if future.empty:
            setup[f"hit_ema200_{horizon}w"] = None
            setup[f"max_gain_{horizon}w_pct"] = None
            setup[f"drawdown_{horizon}w_pct"] = None
            setup[f"return_{horizon}w_pct"] = None
            continue

        high = safe_float(future["High"].max())
        low = safe_float(future["Low"].min())
        end_close = safe_float(future["Close"].iloc[-1])

        setup[f"max_gain_{horizon}w_pct"] = pct_change(high, close)
        setup[f"drawdown_{horizon}w_pct"] = pct_change(low, close)
        setup[f"return_{horizon}w_pct"] = pct_change(end_close, close)

        if target is not None:
            setup[f"hit_ema200_{horizon}w"] = bool(high is not None and high >= target)
        else:
            setup[f"hit_ema200_{horizon}w"] = None

    weeks_to_hit = None

    if target is not None:
        future = df.iloc[pos + 1 : pos + 1 + 52]

        for offset, (_, r) in enumerate(future.iterrows(), start=1):
            high = safe_float(r.get("High"))

            if high is not None and high >= target:
                weeks_to_hit = offset
                break

    setup["weeks_to_ema200"] = weeks_to_hit

    return setup


def detect_historical_events(ticker, name, df):
    events = []

    if df is None or df.empty:
        return events

    df = add_indicators(df)
    df = df.dropna(subset=["EMA200", "EMA50", "RSI14", "Close"])

    if len(df) < 230:
        return events

    cooldown_until = -1

    for pos in range(0, len(df) - 17):
        if pos < cooldown_until:
            continue

        setup = get_row_setup(df, pos, ticker, name)

        if not setup_is_lifecycle_squeeze_candidate(setup):
            continue

        setup = add_forward_outcomes(df, pos, setup)
        setup["similarity_to_sol"] = None
        events.append(setup)

        cooldown_until = pos + 8

    return events


def get_current_sol_setup():
    df = fetch_weekly_crypto(TARGET_TICKER)

    if df.empty:
        return None, pd.DataFrame()

    df = add_indicators(df)
    df_valid = df.dropna(subset=["EMA200", "EMA50", "RSI14", "Close"])

    if df_valid.empty:
        return None, df

    last_index = df.index.get_loc(df_valid.index[-1])
    setup = get_row_setup(df, last_index, TARGET_TICKER, CRYPTO_ASSETS.get(TARGET_TICKER, "Solana"))

    return setup, df


def feature_distance(a, b, key, scale, weight):
    av = safe_float(a.get(key))
    bv = safe_float(b.get(key))

    if av is None or bv is None or scale == 0:
        return 0.0, 0.0

    d = abs(av - bv) / scale
    d = min(d, 2.0)

    return d * weight, weight * 2.0


def compute_similarity_to_sol(event, sol_setup):
    pairs = [
        ("price_to_ema200_pct", 25.0, 1.6),
        ("upside_to_ema200_pct", 35.0, 1.2),
        ("ema50_ema200_gap_pct", 12.0, 1.4),
        ("rsi14", 18.0, 1.0),
        ("rsi_4w_change", 10.0, 0.8),
        ("gain_from_26w_low_pct", 50.0, 1.0),
        ("age_years", 5.0, 0.9),
    ]

    distance = 0.0
    max_distance = 0.0

    for key, scale, weight in pairs:
        d, max_d = feature_distance(event, sol_setup, key, scale, weight)
        distance += d
        max_distance += max_d

    if max_distance <= 0:
        return None

    similarity = 100.0 * (1.0 - distance / max_distance)
    similarity = max(0.0, min(100.0, similarity))

    return similarity


def compute_all_similarities(events, sol_setup):
    for event in events:
        event["similarity_to_sol"] = compute_similarity_to_sol(event, sol_setup)

    events.sort(
        key=lambda r: (
            safe_float(r.get("similarity_to_sol")) or -1,
            r.get("event_date") or "",
        ),
        reverse=True,
    )

    return events


def take_balanced_events(candidates, max_total, max_per_asset):
    selected = []
    counts = {}

    for event in candidates:
        asset = event.get("asset") or "UNKNOWN"

        if counts.get(asset, 0) >= max_per_asset:
            continue

        selected.append(event)
        counts[asset] = counts.get(asset, 0) + 1

        if len(selected) >= max_total:
            break

    return selected


def build_analog_set(events):
    if not events:
        return []

    filtered = [
        e for e in events
        if safe_float(e.get("similarity_to_sol")) is not None
        and safe_float(e.get("similarity_to_sol")) >= MIN_ANALOG_SIMILARITY
    ]

    candidates = filtered if len(filtered) >= 8 else events

    balanced = take_balanced_events(
        candidates,
        max_total=MAX_ANALOG_EVENTS_TOTAL,
        max_per_asset=MAX_ANALOG_EVENTS_PER_ASSET,
    )

    if len(balanced) < 12:
        balanced = take_balanced_events(
            candidates,
            max_total=MAX_ANALOG_EVENTS_TOTAL,
            max_per_asset=5,
        )

    return balanced


def bool_mean(rows, key):
    values = []

    for row in rows:
        value = row.get(key)

        if value is True:
            values.append(1.0)
        elif value is False:
            values.append(0.0)

    if not values:
        return None

    return sum(values) / len(values) * 100.0


def median_value(rows, key):
    values = []

    for row in rows:
        value = safe_float(row.get(key))

        if value is not None:
            values.append(value)

    if not values:
        return None

    return float(np.median(values))


def compute_stats(events, analog_events):
    source = analog_events if analog_events else events

    return {
        "historical_events": len(events),
        "analog_events": len(source),
        "hit_ema200_4w_pct": bool_mean(source, "hit_ema200_4w"),
        "hit_ema200_8w_pct": bool_mean(source, "hit_ema200_8w"),
        "hit_ema200_12w_pct": bool_mean(source, "hit_ema200_12w"),
        "hit_ema200_16w_pct": bool_mean(source, "hit_ema200_16w"),
        "median_max_gain_4w_pct": median_value(source, "max_gain_4w_pct"),
        "median_max_gain_8w_pct": median_value(source, "max_gain_8w_pct"),
        "median_max_gain_12w_pct": median_value(source, "max_gain_12w_pct"),
        "median_max_gain_16w_pct": median_value(source, "max_gain_16w_pct"),
        "median_drawdown_4w_pct": median_value(source, "drawdown_4w_pct"),
        "median_drawdown_8w_pct": median_value(source, "drawdown_8w_pct"),
        "median_drawdown_12w_pct": median_value(source, "drawdown_12w_pct"),
        "median_drawdown_16w_pct": median_value(source, "drawdown_16w_pct"),
        "median_weeks_to_ema200": median_value(
            [e for e in source if safe_float(e.get("weeks_to_ema200")) is not None],
            "weeks_to_ema200",
        ),
    }


def parse_price_from_text(text):
    if text is None:
        return None

    text = clean_text(text)
    text = text.replace("$", "").replace("€", "").replace("%", "")
    match = re.search(r"[-+]?\d[\d\.,]*", text)

    if not match:
        return None

    value = match.group(0)

    if "," in value:
        value = value.replace(".", "").replace(",", ".")
    elif value.count(".") > 1:
        value = value.replace(".", "")

    try:
        return float(value)
    except Exception:
        return None


def parse_latest_report_levels():
    levels = {
        "first_confirmation": None,
        "second_confirmation": None,
        "soft_invalidation": None,
        "hard_invalidation": None,
    }

    if not os.path.exists(MAIN_REPORT_PATH):
        return levels

    try:
        with open(MAIN_REPORT_PATH, "r", encoding="utf-8") as f:
            text = f.read()
    except Exception:
        return levels

    patterns = {
        "first_confirmation": r"Prima conferma\s*\|\s*([0-9\.,]+)",
        "second_confirmation": r"Seconda conferma\s*\|\s*([0-9\.,]+)",
        "soft_invalidation": r"Invalidazione soft\s*\|\s*([0-9\.,]+)",
        "hard_invalidation": r"Invalidazione forte\s*\|\s*([0-9\.,]+)",
    }

    for key, pattern in patterns.items():
        m = re.search(pattern, text, flags=re.IGNORECASE)

        if m:
            levels[key] = parse_price_from_text(m.group(1))

    if levels["first_confirmation"] is None:
        m = re.search(r"Conferme sopra\s+([0-9\.,]+)\s*/\s*([0-9\.,]+)\s*/\s*([0-9\.,]+)", text)

        if m:
            levels["first_confirmation"] = parse_price_from_text(m.group(1))
            levels["second_confirmation"] = parse_price_from_text(m.group(3))

    if levels["soft_invalidation"] is None:
        m = re.search(r"Allarmi sotto\s+([0-9\.,]+)\s*/\s*([0-9\.,]+)\s*/\s*([0-9\.,]+)", text)

        if m:
            levels["soft_invalidation"] = parse_price_from_text(m.group(1))
            levels["hard_invalidation"] = parse_price_from_text(m.group(3))

    return levels


def add_score_component(components, score, name, value, points, reason):
    components.append(
        {
            "name": name,
            "value": value,
            "points": points,
            "reason": reason,
        }
    )

    return score + points


def compute_lifecycle_score(sol_setup, stats, levels):
    score = 0
    components = []

    close = safe_float(sol_setup.get("close"))
    price_to_ema200 = safe_float(sol_setup.get("price_to_ema200_pct"))
    upside_to_ema200 = safe_float(sol_setup.get("upside_to_ema200_pct"))
    ema_gap = safe_float(sol_setup.get("ema50_ema200_gap_pct"))
    rsi = safe_float(sol_setup.get("rsi14"))
    rsi_change = safe_float(sol_setup.get("rsi_4w_change"))
    age = safe_float(sol_setup.get("age_years"))
    cross_state = sol_setup.get("cross_state") or ""
    hit_12w = safe_float(stats.get("hit_ema200_12w_pct"))
    soft_invalidation = safe_float(levels.get("soft_invalidation"))
    hard_invalidation = safe_float(levels.get("hard_invalidation"))

    if price_to_ema200 is not None:
        if price_to_ema200 <= -35:
            score = add_score_component(
                components,
                score,
                "Prezzo vs EMA200",
                fmt_pct(price_to_ema200),
                2,
                "SOL è molto sotto EMA200 weekly: spazio forte per mean reversion.",
            )
        elif price_to_ema200 <= -25:
            score = add_score_component(
                components,
                score,
                "Prezzo vs EMA200",
                fmt_pct(price_to_ema200),
                1,
                "SOL è sotto EMA200 weekly: possibile magnete tecnico.",
            )
        elif price_to_ema200 > -10:
            score = add_score_component(
                components,
                score,
                "Prezzo vs EMA200",
                fmt_pct(price_to_ema200),
                -1,
                "SOL non è abbastanza lontana da EMA200: meno spazio per squeeze.",
            )
        else:
            score = add_score_component(
                components,
                score,
                "Prezzo vs EMA200",
                fmt_pct(price_to_ema200),
                0,
                "Distanza da EMA200 presente ma non estrema.",
            )

    if upside_to_ema200 is not None:
        if upside_to_ema200 >= 35:
            score = add_score_component(
                components,
                score,
                "Upside verso EMA200",
                fmt_pct(upside_to_ema200),
                1,
                "La EMA200 weekly è abbastanza lontana da essere un target tecnico rilevante.",
            )
        elif upside_to_ema200 < 15:
            score = add_score_component(
                components,
                score,
                "Upside verso EMA200",
                fmt_pct(upside_to_ema200),
                -1,
                "Poco spazio verso EMA200: squeeze meno interessante.",
            )
        else:
            score = add_score_component(
                components,
                score,
                "Upside verso EMA200",
                fmt_pct(upside_to_ema200),
                0,
                "Spazio verso EMA200 discreto ma non enorme.",
            )

    if ema_gap is not None:
        if "SOVRAPPOSTE" in cross_state or "IMMINENTE" in cross_state or "IN CORSO" in cross_state:
            score = add_score_component(
                components,
                score,
                "EMA50/EMA200",
                f"{cross_state} ({fmt_pct(ema_gap)})",
                1,
                "Le medie sono praticamente attaccate: fase compatibile con incrocio tardivo/squeeze.",
            )
        elif "RECENTE" in cross_state or "CONFERMATO DA POCO" in cross_state or "AVVICINAMENTO" in cross_state:
            score = add_score_component(
                components,
                score,
                "EMA50/EMA200",
                f"{cross_state} ({fmt_pct(ema_gap)})",
                1,
                "Fase compatibile con death cross tardivo / squeeze da mean reversion.",
            )
        elif abs(ema_gap) <= 15:
            score = add_score_component(
                components,
                score,
                "EMA50/EMA200",
                f"{cross_state} ({fmt_pct(ema_gap)})",
                0,
                "Le medie sono abbastanza vicine, ma il segnale non è pulito.",
            )
        else:
            score = add_score_component(
                components,
                score,
                "EMA50/EMA200",
                f"{cross_state} ({fmt_pct(ema_gap)})",
                -1,
                "Le medie non sono nella fase tipica dello squeeze osservato.",
            )

    if rsi is not None:
        if 30 <= rsi <= 50 and rsi_change is not None and rsi_change > 0:
            score = add_score_component(
                components,
                score,
                "RSI weekly",
                f"{fmt_number(rsi, 2)} / cambio 4w {fmt_number(rsi_change, 2)}",
                1,
                "RSI basso ma in recupero: setup coerente con relief rally.",
            )
        elif rsi > 60:
            score = add_score_component(
                components,
                score,
                "RSI weekly",
                fmt_number(rsi, 2),
                -1,
                "RSI già alto: lo squeeze potrebbe essere avanzato.",
            )
        else:
            score = add_score_component(
                components,
                score,
                "RSI weekly",
                f"{fmt_number(rsi, 2)} / cambio 4w {fmt_number(rsi_change, 2)}",
                0,
                "RSI non dà conferma forte.",
            )

    if age is not None:
        if 3 <= age <= 8:
            score = add_score_component(
                components,
                score,
                "Età asset",
                f"{fmt_number(age, 1)} anni",
                1,
                "SOL è in fascia giovane-matura: abbastanza storica, ma ancora growth.",
            )
        elif age < 2:
            score = add_score_component(
                components,
                score,
                "Età asset",
                f"{fmt_number(age, 1)} anni",
                -1,
                "Asset troppo giovane: EMA200 meno affidabile.",
            )
        else:
            score = add_score_component(
                components,
                score,
                "Età asset",
                f"{fmt_number(age, 1)} anni",
                0,
                "Asset più maturo: squeeze possibile ma meno esplosivo.",
            )

    if hit_12w is not None:
        if hit_12w >= 55:
            score = add_score_component(
                components,
                score,
                "Analoghi storici",
                f"{fmt_pct(hit_12w, force_sign=False)} hit EMA200 entro 12w",
                1,
                "Negli analoghi simili, il ritorno verso EMA200 è avvenuto spesso.",
            )
        elif hit_12w < 30:
            score = add_score_component(
                components,
                score,
                "Analoghi storici",
                f"{fmt_pct(hit_12w, force_sign=False)} hit EMA200 entro 12w",
                -1,
                "Negli analoghi simili, il ritorno verso EMA200 è stato raro.",
            )
        else:
            score = add_score_component(
                components,
                score,
                "Analoghi storici",
                f"{fmt_pct(hit_12w, force_sign=False)} hit EMA200 entro 12w",
                0,
                "Gli analoghi storici sono misti.",
            )

    if close is not None and hard_invalidation is not None and close < hard_invalidation:
        score = add_score_component(
            components,
            score,
            "Invalidazione forte",
            f"Prezzo {fmt_price(close)} < {fmt_price(hard_invalidation)}",
            -4,
            "SOL è sotto invalidazione forte: setup lifecycle quasi rotto.",
        )
    elif close is not None and soft_invalidation is not None and close < soft_invalidation:
        score = add_score_component(
            components,
            score,
            "Invalidazione soft",
            f"Prezzo {fmt_price(close)} < {fmt_price(soft_invalidation)}",
            -2,
            "SOL è sotto invalidazione soft: squeeze più fragile.",
        )

    score = max(-6, min(8, score))

    if score >= 5:
        bias = "SQUEEZE SETUP FORTE"
        action = "CONFLUENZA BUONA VERSO EMA200, MA SOLO CON CONFERME"
    elif score >= 3:
        bias = "SQUEEZE SETUP INTERESSANTE"
        action = "DA MONITORARE PER RUN VERSO EMA200"
    elif score >= 1:
        bias = "SQUEEZE SETUP PARZIALE"
        action = "POSSIBILE, MA NON ANCORA PULITO"
    elif score == 0:
        bias = "NEUTRALE / MISTO"
        action = "NESSUNA CONFERMA FORTE"
    else:
        bias = "DEBOLE / RISCHIOSO"
        action = "NON FORZARE, SETUP POCO PULITO"

    if score >= 3:
        global_weight = 1
    elif score <= -2:
        global_weight = -1
    else:
        global_weight = 0

    return score, bias, action, global_weight, components


def save_events_csv(events):
    os.makedirs(REPORT_DIR, exist_ok=True)

    with open(EVENTS_CSV_PATH, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=EVENT_COLUMNS)
        writer.writeheader()

        for event in events:
            writer.writerow({col: event.get(col) for col in EVENT_COLUMNS})


def load_history():
    if not os.path.exists(HISTORY_CSV_PATH):
        return []

    rows = []

    try:
        with open(HISTORY_CSV_PATH, "r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)

            for row in reader:
                rows.append(dict(row))
    except Exception:
        return []

    return rows


def save_history(rows):
    os.makedirs(REPORT_DIR, exist_ok=True)

    with open(HISTORY_CSV_PATH, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=HISTORY_COLUMNS)
        writer.writeheader()

        for row in rows:
            writer.writerow({col: row.get(col) for col in HISTORY_COLUMNS})


def update_history(row):
    rows = load_history()
    date_value = row.get("date")

    rows = [r for r in rows if r.get("date") != date_value]
    rows.append(row)
    rows.sort(key=lambda r: r.get("date", ""))

    save_history(rows)

    return rows


def find_previous_history_row(history_rows, current_date):
    valid_rows = []

    for row in history_rows:
        row_date = clean_text(row.get("date"))

        if not row_date:
            continue

        if row_date == current_date:
            continue

        valid_rows.append(row)

    if not valid_rows:
        return None

    valid_rows.sort(key=lambda r: r.get("date", ""))

    return valid_rows[-1]


def trend_point(reasons, name, previous, current, points, reading):
    reasons.append(
        {
            "name": name,
            "previous": previous,
            "current": current,
            "points": points,
            "reading": reading,
        }
    )

    return points


def classify_squeeze_trend(score):
    if score >= 4:
        return "IN FORTE MIGLIORAMENTO"
    if score >= 2:
        return "IN MIGLIORAMENTO"
    if score <= -4:
        return "IN FORTE PEGGIORAMENTO"
    if score <= -2:
        return "IN PEGGIORAMENTO"
    return "STABILE / DA CONFERMARE"


def compute_squeeze_trend(sol_setup, stats, levels, lifecycle_score, history_rows):
    current_date = today_str()
    previous = find_previous_history_row(history_rows, current_date)

    reasons = []

    if previous is None:
        return {
            "label": "PRIMO CONTROLLO / BASELINE",
            "score": 0,
            "previous_date": None,
            "reasons": [
                {
                    "name": "Storico",
                    "previous": "n/a",
                    "current": current_date,
                    "points": 0,
                    "reading": "Serve almeno un controllo precedente per capire se il setup sta migliorando o peggiorando.",
                }
            ],
        }

    trend_score = 0

    prev_price = safe_float(previous.get("sol_price"))
    cur_price = safe_float(sol_setup.get("close"))

    if prev_price is not None and cur_price is not None:
        price_change = pct_change(cur_price, prev_price)

        if price_change is not None and price_change >= 1.5:
            trend_score += trend_point(
                reasons,
                "Prezzo SOL",
                fmt_price(prev_price),
                fmt_price(cur_price),
                1,
                f"Prezzo in aumento rispetto al controllo precedente ({fmt_pct(price_change)}).",
            )
        elif price_change is not None and price_change <= -1.5:
            trend_score += trend_point(
                reasons,
                "Prezzo SOL",
                fmt_price(prev_price),
                fmt_price(cur_price),
                -1,
                f"Prezzo in calo rispetto al controllo precedente ({fmt_pct(price_change)}).",
            )
        else:
            trend_score += trend_point(
                reasons,
                "Prezzo SOL",
                fmt_price(prev_price),
                fmt_price(cur_price),
                0,
                "Prezzo quasi stabile rispetto al controllo precedente.",
            )

    prev_dist = safe_float(previous.get("sol_price_to_ema200_pct"))
    cur_dist = safe_float(sol_setup.get("price_to_ema200_pct"))

    if prev_dist is not None and cur_dist is not None:
        diff = cur_dist - prev_dist

        if diff >= 1.0:
            trend_score += trend_point(
                reasons,
                "Distanza da EMA200",
                fmt_pct(prev_dist),
                fmt_pct(cur_dist),
                1,
                "SOL si è avvicinata alla EMA200: miglioramento del setup squeeze.",
            )
        elif diff <= -1.0:
            trend_score += trend_point(
                reasons,
                "Distanza da EMA200",
                fmt_pct(prev_dist),
                fmt_pct(cur_dist),
                -1,
                "SOL si è allontanata dalla EMA200: peggioramento del setup squeeze.",
            )
        else:
            trend_score += trend_point(
                reasons,
                "Distanza da EMA200",
                fmt_pct(prev_dist),
                fmt_pct(cur_dist),
                0,
                "Distanza da EMA200 quasi invariata.",
            )

    prev_upside = safe_float(previous.get("sol_upside_to_ema200_pct"))
    cur_upside = safe_float(sol_setup.get("upside_to_ema200_pct"))

    if prev_upside is not None and cur_upside is not None:
        diff = cur_upside - prev_upside

        if diff <= -1.0:
            trend_score += trend_point(
                reasons,
                "Upside verso EMA200",
                fmt_pct(prev_upside),
                fmt_pct(cur_upside),
                1,
                "L'upside residuo verso EMA200 si è ridotto: SOL si sta avvicinando al target.",
            )
        elif diff >= 1.0:
            trend_score += trend_point(
                reasons,
                "Upside verso EMA200",
                fmt_pct(prev_upside),
                fmt_pct(cur_upside),
                -1,
                "L'upside residuo verso EMA200 è aumentato: SOL si è allontanata dal target.",
            )
        else:
            trend_score += trend_point(
                reasons,
                "Upside verso EMA200",
                fmt_pct(prev_upside),
                fmt_pct(cur_upside),
                0,
                "Upside verso EMA200 quasi invariato.",
            )

    prev_rsi = safe_float(previous.get("sol_rsi14"))
    cur_rsi = safe_float(sol_setup.get("rsi14"))

    if prev_rsi is not None and cur_rsi is not None:
        diff = cur_rsi - prev_rsi

        if diff >= 1.0 and cur_rsi <= 55:
            trend_score += trend_point(
                reasons,
                "RSI weekly",
                fmt_number(prev_rsi, 2),
                fmt_number(cur_rsi, 2),
                1,
                "RSI in recupero da zona ancora non estrema: migliora il momentum.",
            )
        elif diff <= -1.0:
            trend_score += trend_point(
                reasons,
                "RSI weekly",
                fmt_number(prev_rsi, 2),
                fmt_number(cur_rsi, 2),
                -1,
                "RSI in calo: momentum più debole.",
            )
        elif cur_rsi > 60:
            trend_score += trend_point(
                reasons,
                "RSI weekly",
                fmt_number(prev_rsi, 2),
                fmt_number(cur_rsi, 2),
                -1,
                "RSI già alto: lo squeeze potrebbe essere avanzato.",
            )
        else:
            trend_score += trend_point(
                reasons,
                "RSI weekly",
                fmt_number(prev_rsi, 2),
                fmt_number(cur_rsi, 2),
                0,
                "RSI quasi stabile.",
            )

    prev_lifecycle_score = safe_float(previous.get("lifecycle_score"))

    if prev_lifecycle_score is not None:
        if lifecycle_score > prev_lifecycle_score:
            trend_score += trend_point(
                reasons,
                "Lifecycle score",
                fmt_number(prev_lifecycle_score, 0),
                fmt_number(lifecycle_score, 0),
                1,
                "Score lifecycle in aumento.",
            )
        elif lifecycle_score < prev_lifecycle_score:
            trend_score += trend_point(
                reasons,
                "Lifecycle score",
                fmt_number(prev_lifecycle_score, 0),
                fmt_number(lifecycle_score, 0),
                -1,
                "Score lifecycle in diminuzione.",
            )
        else:
            trend_score += trend_point(
                reasons,
                "Lifecycle score",
                fmt_number(prev_lifecycle_score, 0),
                fmt_number(lifecycle_score, 0),
                0,
                "Score lifecycle stabile.",
            )

    prev_hit12 = safe_float(previous.get("analog_hit_ema200_12w_pct"))
    cur_hit12 = safe_float(stats.get("hit_ema200_12w_pct"))

    if prev_hit12 is not None and cur_hit12 is not None:
        diff = cur_hit12 - prev_hit12

        if diff >= 5.0:
            trend_score += trend_point(
                reasons,
                "Analoghi hit EMA200 12w",
                fmt_pct(prev_hit12, force_sign=False),
                fmt_pct(cur_hit12, force_sign=False),
                1,
                "Gli analoghi selezionati sono diventati più favorevoli.",
            )
        elif diff <= -5.0:
            trend_score += trend_point(
                reasons,
                "Analoghi hit EMA200 12w",
                fmt_pct(prev_hit12, force_sign=False),
                fmt_pct(cur_hit12, force_sign=False),
                -1,
                "Gli analoghi selezionati sono diventati meno favorevoli.",
            )
        else:
            trend_score += trend_point(
                reasons,
                "Analoghi hit EMA200 12w",
                fmt_pct(prev_hit12, force_sign=False),
                fmt_pct(cur_hit12, force_sign=False),
                0,
                "Probabilità storica degli analoghi quasi invariata.",
            )

    prev_drawdown = safe_float(previous.get("analog_median_drawdown_12w_pct"))
    cur_drawdown = safe_float(stats.get("median_drawdown_12w_pct"))

    if prev_drawdown is not None and cur_drawdown is not None:
        diff = cur_drawdown - prev_drawdown

        if diff >= 5.0:
            trend_score += trend_point(
                reasons,
                "Drawdown mediano analoghi",
                fmt_pct(prev_drawdown),
                fmt_pct(cur_drawdown),
                1,
                "Il drawdown mediano degli analoghi è meno negativo: rischio storico più leggero.",
            )
        elif diff <= -5.0:
            trend_score += trend_point(
                reasons,
                "Drawdown mediano analoghi",
                fmt_pct(prev_drawdown),
                fmt_pct(cur_drawdown),
                -1,
                "Il drawdown mediano degli analoghi è più negativo: rischio storico più pesante.",
            )
        else:
            trend_score += trend_point(
                reasons,
                "Drawdown mediano analoghi",
                fmt_pct(prev_drawdown),
                fmt_pct(cur_drawdown),
                0,
                "Drawdown mediano degli analoghi quasi invariato.",
            )

    soft_invalidation = safe_float(levels.get("soft_invalidation"))
    hard_invalidation = safe_float(levels.get("hard_invalidation"))
    first_confirmation = safe_float(levels.get("first_confirmation"))
    second_confirmation = safe_float(levels.get("second_confirmation"))

    if cur_price is not None and hard_invalidation is not None and cur_price < hard_invalidation:
        trend_score += trend_point(
            reasons,
            "Invalidazione forte",
            fmt_price(hard_invalidation),
            fmt_price(cur_price),
            -4,
            "Prezzo sotto invalidazione forte: setup quasi rotto.",
        )
    elif cur_price is not None and soft_invalidation is not None and cur_price < soft_invalidation:
        trend_score += trend_point(
            reasons,
            "Invalidazione soft",
            fmt_price(soft_invalidation),
            fmt_price(cur_price),
            -2,
            "Prezzo sotto invalidazione soft: setup in peggioramento.",
        )
    elif cur_price is not None and soft_invalidation is not None and cur_price <= soft_invalidation * 1.05:
        trend_score += trend_point(
            reasons,
            "Vicinanza invalidazione soft",
            fmt_price(soft_invalidation),
            fmt_price(cur_price),
            -1,
            "Prezzo ancora troppo vicino all'invalidazione soft.",
        )

    if cur_price is not None and second_confirmation is not None and cur_price >= second_confirmation:
        trend_score += trend_point(
            reasons,
            "Seconda conferma",
            fmt_price(second_confirmation),
            fmt_price(cur_price),
            3,
            "Prezzo sopra seconda conferma: squeeze verso EMA200 molto più credibile.",
        )
    elif cur_price is not None and first_confirmation is not None and cur_price >= first_confirmation:
        trend_score += trend_point(
            reasons,
            "Prima conferma",
            fmt_price(first_confirmation),
            fmt_price(cur_price),
            2,
            "Prezzo sopra prima conferma: setup in netto miglioramento.",
        )

    trend_score = max(-8, min(8, trend_score))

    return {
        "label": classify_squeeze_trend(trend_score),
        "score": trend_score,
        "previous_date": previous.get("date"),
        "reasons": reasons,
    }


def trend_reasons_to_text(trend):
    reasons = trend.get("reasons") or []

    parts = []

    for r in reasons:
        name = clean_text(r.get("name"))
        points = r.get("points")
        reading = clean_text(r.get("reading"))

        if points is None:
            points_text = "0"
        elif points > 0:
            points_text = f"+{points}"
        else:
            points_text = str(points)

        parts.append(f"{name}: {points_text} — {reading}")

    return " | ".join(parts)


def make_sol_chart(sol_df, sol_setup):
    try:
        import matplotlib.pyplot as plt
    except Exception:
        return None

    if sol_df is None or sol_df.empty:
        return None

    df = add_indicators(sol_df).dropna(subset=["EMA200", "EMA50", "Close"])

    if df.empty:
        return None

    df = df.tail(180)

    os.makedirs(REPORT_DIR, exist_ok=True)

    try:
        plt.figure(figsize=(12, 7))
        plt.plot(df.index, df["Close"], label="SOL close")
        plt.plot(df.index, df["EMA20"], label="EMA20")
        plt.plot(df.index, df["EMA50"], label="EMA50")
        plt.plot(df.index, df["EMA100"], label="EMA100")
        plt.plot(df.index, df["EMA200"], label="EMA200")

        ema200 = safe_float(sol_setup.get("ema200"))
        close = safe_float(sol_setup.get("close"))

        if ema200 is not None:
            plt.axhline(ema200, linestyle="--", linewidth=1, label=f"EMA200 target {ema200:.2f}")

        if close is not None:
            plt.axhline(close, linestyle=":", linewidth=1, label=f"Prezzo {close:.2f}")

        plt.title("SOL weekly lifecycle squeeze: prezzo vs EMA")
        plt.legend()
        plt.tight_layout()
        plt.savefig(CHART_PATH, dpi=140)
        plt.close()

        return os.path.basename(CHART_PATH)
    except Exception:
        try:
            plt.close()
        except Exception:
            pass

        return None


def build_score_table(components):
    rows = []

    for c in components:
        points = c.get("points")

        if points is None:
            points_text = "0"
        elif points > 0:
            points_text = f"+{points}"
        else:
            points_text = str(points)

        rows.append(
            [
                c.get("name"),
                c.get("value"),
                points_text,
                c.get("reason"),
            ]
        )

    if not rows:
        return "Nessun componente disponibile."

    return md_table(["Componente", "Valore", "Punti", "Lettura"], rows)


def build_squeeze_trend_table(trend):
    reasons = trend.get("reasons") or []

    if not reasons:
        return "Nessun autocontrollo disponibile."

    rows = []

    for r in reasons:
        points = r.get("points")

        if points is None:
            points_text = "0"
        elif points > 0:
            points_text = f"+{points}"
        else:
            points_text = str(points)

        rows.append(
            [
                r.get("name"),
                r.get("previous"),
                r.get("current"),
                points_text,
                r.get("reading"),
            ]
        )

    return md_table(
        ["Controllo", "Precedente", "Attuale", "Punti", "Lettura"],
        rows,
    )


def build_top_analogs_table(analog_events, limit=15):
    rows = []

    for event in analog_events[:limit]:
        rows.append(
            [
                event.get("event_date"),
                event.get("name"),
                event.get("asset"),
                fmt_pct(event.get("similarity_to_sol"), force_sign=False),
                f"{fmt_number(event.get('age_years'), 1)} anni",
                event.get("age_reference_date"),
                fmt_price(event.get("close")),
                fmt_pct(event.get("price_to_ema200_pct")),
                fmt_pct(event.get("ema50_ema200_gap_pct")),
                event.get("cross_state"),
                fmt_number(event.get("rsi14"), 2),
                yes_no(event.get("hit_ema200_12w")),
                fmt_pct(event.get("max_gain_12w_pct")),
                fmt_pct(event.get("drawdown_12w_pct")),
            ]
        )

    if not rows:
        return "Nessun analogo storico trovato."

    return md_table(
        [
            "Data",
            "Asset",
            "Ticker",
            "Similarità",
            "Età",
            "Ref. età",
            "Prezzo",
            "Dist. EMA200",
            "Gap EMA50/200",
            "Stato cross",
            "RSI",
            "Hit EMA200 12w",
            "Max gain 12w",
            "Drawdown 12w",
        ],
        rows,
    )


def build_stats_table(stats):
    return md_table(
        ["Metrica", "Valore"],
        [
            ["Eventi storici trovati", stats.get("historical_events")],
            ["Analoghi usati", stats.get("analog_events")],
            ["Limite massimo per singolo asset", MAX_ANALOG_EVENTS_PER_ASSET],
            ["Hit EMA200 entro 4 settimane", fmt_pct(stats.get("hit_ema200_4w_pct"), force_sign=False)],
            ["Hit EMA200 entro 8 settimane", fmt_pct(stats.get("hit_ema200_8w_pct"), force_sign=False)],
            ["Hit EMA200 entro 12 settimane", fmt_pct(stats.get("hit_ema200_12w_pct"), force_sign=False)],
            ["Hit EMA200 entro 16 settimane", fmt_pct(stats.get("hit_ema200_16w_pct"), force_sign=False)],
            ["Max gain mediano 12w", fmt_pct(stats.get("median_max_gain_12w_pct"))],
            ["Drawdown mediano 12w", fmt_pct(stats.get("median_drawdown_12w_pct"))],
            ["Settimane mediane per toccare EMA200", fmt_number(stats.get("median_weeks_to_ema200"), 1)],
        ],
    )


def build_current_table(sol_setup, levels):
    return md_table(
        ["Voce", "Valore", "Lettura"],
        [
            ["Fonte prezzi", "Yahoo Finance SOL-USD weekly", "Può differire da KuCoin/CoinEx/Binance per chiusura candela e storico EMA."],
            ["Prezzo SOL", fmt_price(sol_setup.get("close")), "Prezzo weekly attuale."],
            ["EMA20", fmt_price(sol_setup.get("ema20")), "Media breve."],
            ["EMA50", fmt_price(sol_setup.get("ema50")), "Media intermedia."],
            ["EMA100", fmt_price(sol_setup.get("ema100")), "Media lunga intermedia."],
            ["EMA200", fmt_price(sol_setup.get("ema200")), "Target naturale del bear-market squeeze."],
            ["Distanza prezzo da EMA200", fmt_pct(sol_setup.get("price_to_ema200_pct")), "Negativa = prezzo sotto EMA200."],
            ["Upside verso EMA200", fmt_pct(sol_setup.get("upside_to_ema200_pct")), "Quanto dovrebbe salire per tornare a EMA200."],
            ["Gap EMA50/EMA200", fmt_pct(sol_setup.get("ema50_ema200_gap_pct")), "Dentro ±2% = medie sovrapposte, non cross netto."],
            ["Stato incrocio", sol_setup.get("cross_state"), "Fase EMA50/EMA200."],
            ["RSI weekly", fmt_number(sol_setup.get("rsi14"), 2), "RSI basso/in recupero può aiutare il relief rally."],
            ["Cambio RSI 4w", fmt_number(sol_setup.get("rsi_4w_change"), 2), "Positivo = RSI in recupero."],
            ["Gain da minimo 26w", fmt_pct(sol_setup.get("gain_from_26w_low_pct")), "Misura se il primo spike è già partito."],
            ["Età asset", f"{fmt_number(sol_setup.get('age_years'), 1)} anni", "Calcolata da data reale di riferimento, non dal primo dato Yahoo."],
            ["Data riferimento età", sol_setup.get("age_reference_date"), "Genesis/mainnet/lancio pubblico o trading rilevante."],
            ["Prima conferma frattale", fmt_price(levels.get("first_confirmation")), "Livello letto dal report principale, se disponibile."],
            ["Seconda conferma frattale", fmt_price(levels.get("second_confirmation")), "Livello letto dal report principale, se disponibile."],
            ["Invalidazione soft", fmt_price(levels.get("soft_invalidation")), "Sotto qui il setup si indebolisce."],
            ["Invalidazione forte", fmt_price(levels.get("hard_invalidation")), "Sotto qui il setup si rompe quasi del tutto."],
        ],
    )


def build_history_table(rows):
    if not rows:
        return "Nessuno storico salvato."

    last_rows = rows[-30:]
    table_rows = []

    for r in last_rows:
        table_rows.append(
            [
                r.get("date"),
                fmt_price(r.get("sol_price")),
                fmt_price(r.get("sol_ema200")),
                fmt_pct(r.get("sol_upside_to_ema200_pct")),
                r.get("cross_state"),
                fmt_number(r.get("sol_rsi14"), 2),
                fmt_pct(r.get("analog_hit_ema200_12w_pct"), force_sign=False),
                r.get("lifecycle_score"),
                r.get("lifecycle_bias"),
                r.get("squeeze_trend") or "n/a",
            ]
        )

    return md_table(
        [
            "Data",
            "SOL",
            "EMA200",
            "Upside EMA200",
            "Stato cross",
            "RSI",
            "Hit EMA200 12w",
            "Score",
            "Bias",
            "Trend squeeze",
        ],
        table_rows,
    )


def build_markdown_report(sol_setup, stats, analog_events, components, history_rows, levels, score, bias, action, global_weight, squeeze_trend):
    rome_now = datetime.now(ZoneInfo("Europe/Rome")).strftime("%Y-%m-%d %H:%M:%S %Z")

    chart_name = None

    if os.path.exists(CHART_PATH):
        chart_name = os.path.basename(CHART_PATH)

    lines = []
    lines.append("# Major alt lifecycle squeeze report - SOL")
    lines.append("")
    lines.append(f"Generato: **{rome_now}**  ")
    lines.append(f"UTC: **{utc_str()}**")
    lines.append("")
    lines.append("Questo modulo confronta SOL con altre crypto storiche in fasi simili di ciclo.")
    lines.append("")
    lines.append("Idea centrale: una EMA50 che scende verso EMA200 non è rialzista di per sé. Però, se arriva tardi dopo un forte bear market e il prezzo è molto sotto EMA200 weekly, può diventare un setup da **bear-market squeeze / mean reversion rally** verso EMA200.")
    lines.append("")
    lines.append("> Nota fonte dati: il modulo usa **Yahoo Finance SOL-USD weekly**. KuCoin, CoinEx, Binance o altri exchange possono mostrare EMA leggermente diverse. Se EMA50/EMA200 sono dentro ±2%, il modulo non considera il cross come netto: lo classifica come medie sovrapposte / incrocio in corso.")
    lines.append("")
    lines.append("## Sintesi")
    lines.append("")
    lines.append(
        md_table(
            ["Voce", "Valore"],
            [
                ["Lifecycle squeeze score", score],
                ["Bias", bias],
                ["Azione coerente", action],
                ["Peso suggerito nel Global", global_weight],
                ["Trend squeeze", squeeze_trend.get("label")],
                ["Trend squeeze score", squeeze_trend.get("score")],
                ["Confronto precedente", squeeze_trend.get("previous_date") or "n/a"],
                ["Target tecnico naturale", fmt_price(sol_setup.get("ema200"))],
                ["Upside verso EMA200", fmt_pct(sol_setup.get("upside_to_ema200_pct"))],
                ["Stato EMA50/EMA200", sol_setup.get("cross_state")],
                ["Gap EMA50/EMA200", fmt_pct(sol_setup.get("ema50_ema200_gap_pct"))],
                ["Probabilità storica hit EMA200 12w", fmt_pct(stats.get("hit_ema200_12w_pct"), force_sign=False)],
                ["Max gain mediano 12w analoghi", fmt_pct(stats.get("median_max_gain_12w_pct"))],
                ["Drawdown mediano 12w analoghi", fmt_pct(stats.get("median_drawdown_12w_pct"))],
            ],
        )
    )
    lines.append("")
    lines.append("## Autocontrollo setup")
    lines.append("")
    lines.append(f"Trend squeeze: **{squeeze_trend.get('label')}**  ")
    lines.append(f"Score trend: **{squeeze_trend.get('score')}**  ")
    lines.append(f"Confronto con: **{squeeze_trend.get('previous_date') or 'n/a'}**")
    lines.append("")
    lines.append(build_squeeze_trend_table(squeeze_trend))
    lines.append("")
    lines.append("## SOL oggi")
    lines.append("")
    lines.append(build_current_table(sol_setup, levels))
    lines.append("")
    lines.append("## Componenti del punteggio")
    lines.append("")
    lines.append(build_score_table(components))
    lines.append("")
    lines.append("## Statistiche sugli analoghi crypto")
    lines.append("")
    lines.append(build_stats_table(stats))
    lines.append("")
    lines.append("## Top analoghi storici più simili a SOL oggi")
    lines.append("")
    lines.append(build_top_analogs_table(analog_events, 15))
    lines.append("")

    if chart_name:
        lines.append("## Grafico SOL")
        lines.append("")
        lines.append(f"![SOL lifecycle squeeze]({chart_name})")
        lines.append("")

    lines.append("## Storico ultimi salvataggi")
    lines.append("")
    lines.append(build_history_table(history_rows))
    lines.append("")
    lines.append("## Come leggerlo")
    lines.append("")
    lines.append("- **Prezzo molto sotto EMA200 weekly**: aumenta lo spazio per un rally di ritorno alla media.")
    lines.append("- **EMA50 vicina a EMA200 / medie sovrapposte**: spesso è una fase tardiva del bear market, non necessariamente un nuovo short pulito.")
    lines.append("- **RSI basso ma in recupero**: migliora la possibilità di relief rally.")
    lines.append("- **Asset giovane-maturo**: non è più una microcoin appena nata, ma può ancora avere squeeze più forti di un asset molto maturo.")
    lines.append("- **Hit EMA200 12w**: quante volte gli analoghi storici hanno toccato EMA200 entro circa 3 mesi.")
    lines.append("- **Autocontrollo setup**: confronta il controllo attuale con l'ultimo controllo precedente e dice se il setup verso EMA200 sta migliorando o peggiorando.")
    lines.append("")
    lines.append("## Lettura pratica")
    lines.append("")
    lines.append(f"Target tecnico naturale: **{fmt_price(sol_setup.get('ema200'))}**.")
    lines.append("")
    lines.append(f"Conferme: **{fmt_price(levels.get('first_confirmation'))} / {fmt_price(levels.get('second_confirmation'))}**.")
    lines.append("")
    lines.append(f"Invalidazioni: **{fmt_price(levels.get('soft_invalidation'))} / {fmt_price(levels.get('hard_invalidation'))}**.")
    lines.append("")
    lines.append("Questo modulo non dice che SOL deve per forza arrivare alla EMA200. Dice se il setup attuale assomiglia a vecchie fasi crypto dove il prezzo ha fatto uno squeeze verso la media lunga.")
    lines.append("")

    return "\n".join(lines)


def build_main_report_block(sol_setup, stats, score, bias, action, global_weight, squeeze_trend):
    return "\n".join(
        [
            START_MARKER,
            "",
            "---",
            "",
            "# Major alt lifecycle squeeze - SOL",
            "",
            "Report separato completo: **[major_alt_lifecycle_squeeze_report.md](major_alt_lifecycle_squeeze_report.md)**",
            "",
            md_table(
                ["Voce", "Valore"],
                [
                    ["Lifecycle squeeze score", score],
                    ["Bias", bias],
                    ["Azione coerente", action],
                    ["Peso suggerito Global", global_weight],
                    ["Trend squeeze", squeeze_trend.get("label")],
                    ["Trend squeeze score", squeeze_trend.get("score")],
                    ["Confronto precedente", squeeze_trend.get("previous_date") or "n/a"],
                    ["Fonte prezzi", "Yahoo Finance SOL-USD weekly"],
                    ["Prezzo SOL", fmt_price(sol_setup.get("close"))],
                    ["EMA200 weekly target", fmt_price(sol_setup.get("ema200"))],
                    ["Upside verso EMA200", fmt_pct(sol_setup.get("upside_to_ema200_pct"))],
                    ["Distanza prezzo da EMA200", fmt_pct(sol_setup.get("price_to_ema200_pct"))],
                    ["Gap EMA50/EMA200", fmt_pct(sol_setup.get("ema50_ema200_gap_pct"))],
                    ["Stato cross", sol_setup.get("cross_state")],
                    ["RSI weekly", fmt_number(sol_setup.get("rsi14"), 2)],
                    ["Età SOL", f"{fmt_number(sol_setup.get('age_years'), 1)} anni"],
                    ["Analoghi storici usati", stats.get("analog_events")],
                    ["Max analoghi per asset", MAX_ANALOG_EVENTS_PER_ASSET],
                    ["Hit EMA200 12w analoghi", fmt_pct(stats.get("hit_ema200_12w_pct"), force_sign=False)],
                    ["Max gain mediano 12w", fmt_pct(stats.get("median_max_gain_12w_pct"))],
                    ["Drawdown mediano 12w", fmt_pct(stats.get("median_drawdown_12w_pct"))],
                ],
            ),
            "",
            "Lettura semplice:",
            "",
            f"**{action}**",
            "",
            f"Autocontrollo: **{squeeze_trend.get('label')}**.",
            "",
            "Questo modulo confronta SOL con altre crypto in fasi simili di età, distanza da EMA200, EMA50/EMA200 e RSI. Non usa stock market.",
            "",
            "Nota: se EMA50/EMA200 sono dentro ±2%, il modulo parla di medie sovrapposte / incrocio in corso, perché exchange diversi possono mostrare il cross leggermente prima o dopo.",
            "",
            END_MARKER,
        ]
    )


def inject_into_main_report(sol_setup, stats, score, bias, action, global_weight, squeeze_trend):
    if not os.path.exists(MAIN_REPORT_PATH):
        return

    try:
        with open(MAIN_REPORT_PATH, "r", encoding="utf-8") as f:
            text = f.read()
    except Exception:
        return

    if START_MARKER in text and END_MARKER in text:
        before = text.split(START_MARKER)[0].rstrip()
        after = text.split(END_MARKER, 1)[1].lstrip()
        text = before + "\n\n" + after

    block = build_main_report_block(sol_setup, stats, score, bias, action, global_weight, squeeze_trend).strip()

    if SOL_ONCHAIN_END in text:
        pos = text.find(SOL_ONCHAIN_END) + len(SOL_ONCHAIN_END)
        new_text = text[:pos].rstrip() + "\n\n" + block + "\n\n" + text[pos:].lstrip()
    elif RSI_END in text:
        pos = text.find(RSI_END) + len(RSI_END)
        new_text = text[:pos].rstrip() + "\n\n" + block + "\n\n" + text[pos:].lstrip()
    elif BTC_SOL_END in text:
        pos = text.find(BTC_SOL_END) + len(BTC_SOL_END)
        new_text = text[:pos].rstrip() + "\n\n" + block + "\n\n" + text[pos:].lstrip()
    elif GLOBAL_END in text:
        pos = text.find(GLOBAL_END) + len(GLOBAL_END)
        new_text = text[:pos].rstrip() + "\n\n" + block + "\n\n" + text[pos:].lstrip()
    else:
        new_text = text.rstrip() + "\n\n" + block + "\n"

    with open(MAIN_REPORT_PATH, "w", encoding="utf-8") as f:
        f.write(new_text.rstrip() + "\n")


def build_history_row(sol_setup, stats, levels, score, bias, global_weight, squeeze_trend):
    return {
        "date": today_str(),
        "generated_at_utc": utc_str(),
        "sol_price": sol_setup.get("close"),
        "sol_ema20": sol_setup.get("ema20"),
        "sol_ema50": sol_setup.get("ema50"),
        "sol_ema100": sol_setup.get("ema100"),
        "sol_ema200": sol_setup.get("ema200"),
        "sol_price_to_ema200_pct": sol_setup.get("price_to_ema200_pct"),
        "sol_upside_to_ema200_pct": sol_setup.get("upside_to_ema200_pct"),
        "sol_ema50_ema200_gap_pct": sol_setup.get("ema50_ema200_gap_pct"),
        "sol_rsi14": sol_setup.get("rsi14"),
        "sol_rsi_4w_change": sol_setup.get("rsi_4w_change"),
        "sol_gain_from_26w_low_pct": sol_setup.get("gain_from_26w_low_pct"),
        "sol_age_reference_date": sol_setup.get("age_reference_date"),
        "sol_age_years": sol_setup.get("age_years"),
        "cross_state": sol_setup.get("cross_state"),
        "weeks_since_death_cross": sol_setup.get("weeks_since_death_cross"),
        "historical_events": stats.get("historical_events"),
        "analog_events": stats.get("analog_events"),
        "max_analog_events_per_asset": MAX_ANALOG_EVENTS_PER_ASSET,
        "analog_hit_ema200_8w_pct": stats.get("hit_ema200_8w_pct"),
        "analog_hit_ema200_12w_pct": stats.get("hit_ema200_12w_pct"),
        "analog_hit_ema200_16w_pct": stats.get("hit_ema200_16w_pct"),
        "analog_median_max_gain_12w_pct": stats.get("median_max_gain_12w_pct"),
        "analog_median_drawdown_12w_pct": stats.get("median_drawdown_12w_pct"),
        "lifecycle_score": score,
        "lifecycle_bias": bias,
        "global_weight_suggestion": global_weight,
        "squeeze_trend": squeeze_trend.get("label"),
        "squeeze_trend_score": squeeze_trend.get("score"),
        "squeeze_trend_previous_date": squeeze_trend.get("previous_date"),
        "squeeze_trend_reasons": trend_reasons_to_text(squeeze_trend),
        "target_ema200": sol_setup.get("ema200"),
        "first_confirmation": levels.get("first_confirmation"),
        "second_confirmation": levels.get("second_confirmation"),
        "soft_invalidation": levels.get("soft_invalidation"),
        "hard_invalidation": levels.get("hard_invalidation"),
    }


def run_scan():
    os.makedirs(REPORT_DIR, exist_ok=True)

    sol_setup, sol_df = get_current_sol_setup()

    if sol_setup is None:
        raise RuntimeError("Impossibile leggere SOL-USD o calcolare EMA200 weekly.")

    all_events = []

    for ticker, name in CRYPTO_ASSETS.items():
        df = fetch_weekly_crypto(ticker)

        if df.empty:
            continue

        events = detect_historical_events(ticker, name, df)
        all_events.extend(events)

    all_events = compute_all_similarities(all_events, sol_setup)
    analog_events = build_analog_set(all_events)
    stats = compute_stats(all_events, analog_events)
    levels = parse_latest_report_levels()

    score, bias, action, global_weight, components = compute_lifecycle_score(sol_setup, stats, levels)

    history_rows_before = load_history()
    squeeze_trend = compute_squeeze_trend(sol_setup, stats, levels, score, history_rows_before)

    save_events_csv(all_events)

    make_sol_chart(sol_df, sol_setup)

    history_row = build_history_row(sol_setup, stats, levels, score, bias, global_weight, squeeze_trend)
    history_rows = update_history(history_row)

    latest_payload = {
        "generated_at_utc": utc_str(),
        "source": "Yahoo Finance SOL-USD weekly",
        "cross_near_band_pct": CROSS_NEAR_BAND_PCT,
        "max_analog_events_total": MAX_ANALOG_EVENTS_TOTAL,
        "max_analog_events_per_asset": MAX_ANALOG_EVENTS_PER_ASSET,
        "sol_setup": sol_setup,
        "stats": stats,
        "levels": levels,
        "score": score,
        "bias": bias,
        "action": action,
        "global_weight_suggestion": global_weight,
        "squeeze_trend": squeeze_trend,
        "top_analogs": analog_events[:20],
    }

    with open(LATEST_JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(latest_payload, f, indent=2, ensure_ascii=False)

    markdown = build_markdown_report(
        sol_setup=sol_setup,
        stats=stats,
        analog_events=analog_events,
        components=components,
        history_rows=history_rows,
        levels=levels,
        score=score,
        bias=bias,
        action=action,
        global_weight=global_weight,
        squeeze_trend=squeeze_trend,
    )

    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        f.write(markdown)

    inject_into_main_report(sol_setup, stats, score, bias, action, global_weight, squeeze_trend)

    print(f"Wrote {REPORT_PATH}")
    print(f"Wrote {EVENTS_CSV_PATH}")
    print(f"Wrote {HISTORY_CSV_PATH}")
    print(f"Wrote {LATEST_JSON_PATH}")
    print(f"Updated {MAIN_REPORT_PATH}")
    print(f"SOL lifecycle squeeze score: {score} / {bias}")
    print(f"Squeeze trend: {squeeze_trend.get('label')} ({squeeze_trend.get('score')})")
    print(f"Cross state: {sol_setup.get('cross_state')}")
    print(f"EMA50/EMA200 gap: {fmt_pct(sol_setup.get('ema50_ema200_gap_pct'))}")
    print(f"Target EMA200 weekly: {fmt_price(sol_setup.get('ema200'))}")
    print(f"Upside to EMA200: {fmt_pct(sol_setup.get('upside_to_ema200_pct'))}")


def main():
    run_scan()


if __name__ == "__main__":
    main()
