import os
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

import numpy as np
import pandas as pd
import yfinance as yf

from shared_market_snapshot import apply_snapshot_to_ohlcv, snapshot_record

try:
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    CHARTS_AVAILABLE = True
except Exception:
    CHARTS_AVAILABLE = False


REPORT_DIR = "reports"
MAIN_REPORT_PATH = "reports/latest_report.md"
REPORT_PATH = "reports/btc_2022_vs_sol_2026_report.md"
CSV_PATH = "reports/btc_2022_vs_sol_2026_metrics.csv"
TRACKING_LOG_PATH = "reports/btc_2022_vs_sol_2026_tracking_log.csv"

FRACTAL_CHART_PATH = "reports/btc_2022_vs_sol_2026_fractal_chart.png"
PROJECTION_CHART_PATH = "reports/btc_2022_vs_sol_2026_projection_chart.png"
CYCLE_CHART_PATH = "reports/btc_2022_vs_sol_2026_cycle_chart.png"
CYCLE_BASE_CHART_PATH = "reports/btc_2022_vs_sol_2026_cycle_base_chart.png"
CYCLE_BETA_CHART_PATH = "reports/btc_2022_vs_sol_2026_cycle_beta_chart.png"
CYCLE_LOG_CHART_PATH = "reports/btc_2022_vs_sol_2026_cycle_log_chart.png"
TRACKING_CHART_PATH = "reports/btc_2022_vs_sol_2026_tracking_chart.png"

FRACTAL_CHART_FILE = os.path.basename(FRACTAL_CHART_PATH)
PROJECTION_CHART_FILE = os.path.basename(PROJECTION_CHART_PATH)
CYCLE_CHART_FILE = os.path.basename(CYCLE_CHART_PATH)
CYCLE_BASE_CHART_FILE = os.path.basename(CYCLE_BASE_CHART_PATH)
CYCLE_BETA_CHART_FILE = os.path.basename(CYCLE_BETA_CHART_PATH)
CYCLE_LOG_CHART_FILE = os.path.basename(CYCLE_LOG_CHART_PATH)
TRACKING_CHART_FILE = os.path.basename(TRACKING_CHART_PATH)

BTC_TICKER = "BTC-USD"
SOL_TICKER = "SOL-USD"

BTC_BOTTOM_SEARCH_START = "2022-11-01"
BTC_BOTTOM_SEARCH_END = "2023-01-31"
BTC_TOP_SEARCH_START = "2025-01-01"
BTC_TOP_SEARCH_END = "2025-12-31"
SOL_BOTTOM_SEARCH_START = "2026-06-01"

PROGRAM_START_DATE = os.getenv("PROGRAM_START_DATE", "2026-07-03")

FORECAST_DAYS = [7, 14, 30, 60, 90, 120, 180, 365]
CHART_LABEL_DAYS = [7, 30, 60, 120, 365]
STAGE_BUCKETS = [
    (0, 14, "Step 1 - prossime 2 settimane"),
    (15, 30, "Step 2 - primo mese"),
    (31, 60, "Step 3 - secondo mese"),
    (61, 90, "Step 4 - terzo mese"),
    (91, 120, "Step 5 - quarto mese"),
    (121, 180, "Step 6 - estensione 6 mesi"),
]

# Soglie operative. La somiglianza di forma e l'aderenza di prezzo sono due cose diverse.
MIN_LIVE_DAYS = 5
GOOD_LIVE_AVG_GAP = 8.0
ACCEPTABLE_LIVE_AVG_GAP = 12.0
MAX_OPERATIVE_LIVE_AVG_GAP = 15.0
MAX_OPERATIVE_LAST_GAP = 18.0
GAP_REENTRY_THRESHOLD = 12.0
PUBLIC_REFERENCE_INTERVAL = "1m"
PUBLIC_REFERENCE_PERIOD = "1d"
DISPLAY_STALE_AFTER_HOURS = 24.0


def safe_float(value):
    try:
        if pd.isna(value):
            return None
        value = float(value)
        if np.isnan(value) or np.isinf(value):
            return None
        return value
    except Exception:
        return None


def fmt_number(value, decimals=2):
    value = safe_float(value)
    if value is None:
        return "n/d"
    text = f"{value:,.{decimals}f}"
    return text.replace(",", "X").replace(".", ",").replace("X", ".")


def fmt_pct(value, decimals=2):
    value = safe_float(value)
    if value is None:
        return "n/d"
    sign = "+" if value > 0 else ""
    return f"{sign}{fmt_number(value, decimals)}%"


def fmt_price(value):
    value = safe_float(value)
    if value is None:
        return "n/d"
    if abs(value) >= 1000:
        return f"{fmt_number(value, 0)} $"
    if abs(value) >= 1:
        return f"{fmt_number(value, 2)} $"
    return f"{fmt_number(value, 5)} $"


def fmt_chart_price(value):
    value = safe_float(value)
    if value is None:
        return "n/d"
    return f"{fmt_number(value, 2)} USD"


def fmt_date(value):
    try:
        return pd.to_datetime(value).strftime("%Y-%m-%d")
    except Exception:
        return "n/d"


def fmt_date_it(value):
    try:
        dt = pd.to_datetime(value)
        months = {
            1: "gennaio",
            2: "febbraio",
            3: "marzo",
            4: "aprile",
            5: "maggio",
            6: "giugno",
            7: "luglio",
            8: "agosto",
            9: "settembre",
            10: "ottobre",
            11: "novembre",
            12: "dicembre",
        }
        return f"{dt.day} {months[dt.month]} {dt.year}"
    except Exception:
        return "n/d"


def add_days(date_value, days):
    try:
        return pd.to_datetime(date_value) + pd.Timedelta(days=int(days))
    except Exception:
        return None


def md_table(headers, rows):
    def clean(value):
        return str(value).replace("|", "\\|").replace("\n", " ")

    lines = [
        "| " + " | ".join(clean(h) for h in headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(clean(cell) for cell in row) + " |")
    return "\n".join(lines)


def utc_timestamp(value):
    """Return a timezone-aware UTC timestamp, or ``None`` for invalid input."""
    try:
        result = pd.Timestamp(value)
        if pd.isna(result):
            return None
        if result.tzinfo is None:
            return result.tz_localize("UTC")
        return result.tz_convert("UTC")
    except Exception:
        return None


def utc_iso(value):
    value = utc_timestamp(value)
    if value is None:
        return None
    return value.isoformat(timespec="seconds").replace("+00:00", "Z")


def _latest_close(frame):
    if frame is None or frame.empty:
        return None, None
    if isinstance(frame.columns, pd.MultiIndex):
        close_columns = [column for column in frame.columns if "Close" in column]
        if not close_columns:
            return None, None
        series = frame[close_columns[0]]
    elif "Close" in frame.columns:
        series = frame["Close"]
    else:
        return None, None
    valid = pd.to_numeric(series, errors="coerce").dropna()
    if valid.empty:
        return None, None
    return safe_float(valid.iloc[-1]), valid.index[-1]


def fetch_current_public_reference(*, downloader=None, acquired_at=None):
    """Fetch a display-only public SOL reference without affecting model inputs."""
    downloader = downloader or yf.download
    acquired_at = utc_timestamp(acquired_at or datetime.now(timezone.utc))
    base = {
        "available": False,
        "price": None,
        "timestamp": None,
        "acquired_at": utc_iso(acquired_at),
        "symbol": SOL_TICKER,
        "provider": "Yahoo Finance",
        "field": "Close",
        "timeframe": PUBLIC_REFERENCE_INTERVAL,
        "purpose": "DISPLAY_ONLY",
    }
    try:
        frame = downloader(
            SOL_TICKER,
            period=PUBLIC_REFERENCE_PERIOD,
            interval=PUBLIC_REFERENCE_INTERVAL,
            auto_adjust=True,
            progress=False,
            threads=False,
            timeout=15,
        )
        price, timestamp = _latest_close(frame)
        if price is None or timestamp is None:
            return {**base, "status": "UNAVAILABLE", "reason": "empty public quote"}
        return {
            **base,
            "available": True,
            "price": price,
            "timestamp": utc_iso(timestamp),
            "status": "AVAILABLE",
            "reason": None,
        }
    except Exception as exc:
        return {
            **base,
            "status": "UNAVAILABLE",
            "reason": f"public quote unavailable ({type(exc).__name__})",
        }


def build_computational_anchor(sol_current_price, sol_current_date):
    """Describe the exact existing model boundary without changing its value."""
    record = snapshot_record(SOL_TICKER)
    record_price = safe_float(record.get("price") or record.get("close"))
    record_date = utc_timestamp(record.get("candle_date_utc"))
    model_date = utc_timestamp(sol_current_date)
    matches_snapshot = (
        record_price is not None
        and sol_current_price is not None
        and abs(record_price - sol_current_price) <= 1e-9
        and record_date is not None
        and model_date is not None
        and record_date.normalize() == model_date.normalize()
    )
    observed_at = (utc_timestamp(record.get("generated_at_utc")) or model_date) if matches_snapshot else model_date
    candle_open = model_date.normalize() if model_date is not None else None
    candle_close = candle_open + pd.Timedelta(days=1) if candle_open is not None else None
    completed = bool(observed_at is not None and candle_close is not None and observed_at >= candle_close)
    return {
        "price": safe_float(sol_current_price),
        "timestamp": utc_iso(observed_at),
        "candle_open_timestamp": utc_iso(candle_open),
        "candle_close_timestamp": utc_iso(candle_close),
        "symbol": record.get("ticker") or SOL_TICKER,
        "provider": (
            record.get("source") or "Yahoo Finance daily shared snapshot"
            if matches_snapshot
            else "Yahoo Finance daily historical download"
        ),
        "field": "Close",
        "timeframe": "1d",
        "completed": completed,
        "reproducible": matches_snapshot,
        "purpose": "MODEL_INPUT",
    }


def build_price_context(anchor, current_reference, *, report_generated_at=None):
    generated_at = utc_timestamp(report_generated_at or datetime.now(timezone.utc))
    anchor_timestamp = utc_timestamp(anchor.get("timestamp"))
    age_seconds = None
    if generated_at is not None and anchor_timestamp is not None:
        age_seconds = max(0.0, (generated_at - anchor_timestamp).total_seconds())
    anchor_price = safe_float(anchor.get("price"))
    current_price = safe_float(current_reference.get("price")) if current_reference.get("available") else None
    gap_usd = current_price - anchor_price if current_price is not None and anchor_price is not None else None
    gap_pct = (current_price / anchor_price - 1.0) * 100 if current_price is not None and anchor_price not in (None, 0) else None
    age_hours = age_seconds / 3600.0 if age_seconds is not None else None
    display_freshness = "UNKNOWN"
    if age_hours is not None:
        display_freshness = "STALE_FOR_CURRENT_DISPLAY" if age_hours > DISPLAY_STALE_AFTER_HOURS else "WITHIN_DAILY_REPORT_CADENCE"
    return {
        "report_generated_at": utc_iso(generated_at),
        "anchor": dict(anchor),
        "current_reference": dict(current_reference),
        "anchor_age_seconds": age_seconds,
        "anchor_age_hours": age_hours,
        "current_vs_anchor_gap_usd": gap_usd,
        "current_vs_anchor_gap_pct": gap_pct,
        "model_input_status": "REPRODUCIBLE_SHARED_SNAPSHOT" if anchor.get("reproducible") else "HISTORICAL_DAILY_INPUT",
        "current_display_freshness": display_freshness,
    }


def format_age(seconds):
    seconds = safe_float(seconds)
    if seconds is None:
        return "n/d"
    total_minutes = max(0, int(seconds // 60))
    hours, minutes = divmod(total_minutes, 60)
    return f"{hours}h {minutes}m"


def build_price_context_block(price_context, *, include_machine_metadata=True):
    anchor = price_context.get("anchor", {})
    reference = price_context.get("current_reference", {})
    reference_price = fmt_price(reference.get("price")) if reference.get("available") else "UNAVAILABLE"
    reference_timestamp = reference.get("timestamp") or "UNAVAILABLE"
    reference_provider = reference.get("provider") or "UNAVAILABLE"
    rows = [
        ["Anchor computazionale", fmt_price(anchor.get("price")), f"{anchor.get('timestamp') or 'n/d'} | {anchor.get('provider') or 'n/d'} | Close 1d"],
        ["Candela anchor completata", "YES" if anchor.get("completed") else "NO", "Stato esplicito; il valore non viene sostituito dal prezzo pubblico."],
        ["Riferimento pubblico corrente", reference_price, f"{reference_timestamp} | {reference_provider} | solo display"],
        ["Età anchor alla generazione", format_age(price_context.get("anchor_age_seconds")), price_context.get("current_display_freshness", "UNKNOWN")],
        ["Gap corrente vs anchor", fmt_price(price_context.get("current_vs_anchor_gap_usd")), fmt_pct(price_context.get("current_vs_anchor_gap_pct"))],
        ["Validità input modello", price_context.get("model_input_status", "UNKNOWN"), "Non è una dichiarazione di validità del segnale/trading."],
    ]
    lines = ["## SOL PRICE CONTEXT", "", md_table(["Voce", "Valore", "Provenienza / significato"], rows)]
    if include_machine_metadata:
        machine = [
            f"COMPUTATIONAL_ANCHOR_PRICE={anchor.get('price') if anchor.get('price') is not None else 'UNAVAILABLE'}",
            f"COMPUTATIONAL_ANCHOR_FIELD={anchor.get('field') or 'UNAVAILABLE'}",
            f"COMPUTATIONAL_ANCHOR_TIMESTAMP={anchor.get('timestamp') or 'UNAVAILABLE'}",
            f"COMPUTATIONAL_ANCHOR_SYMBOL={anchor.get('symbol') or 'UNAVAILABLE'}",
            f"COMPUTATIONAL_ANCHOR_PROVIDER={anchor.get('provider') or 'UNAVAILABLE'}",
            f"COMPUTATIONAL_ANCHOR_TIMEFRAME={anchor.get('timeframe') or 'UNAVAILABLE'}",
            f"COMPUTATIONAL_ANCHOR_COMPLETED={'YES' if anchor.get('completed') else 'NO'}",
            f"CURRENT_PUBLIC_REFERENCE_PRICE={reference.get('price') if reference.get('available') else 'UNAVAILABLE'}",
            f"CURRENT_PUBLIC_REFERENCE_TIMESTAMP={reference_timestamp}",
            f"CURRENT_PUBLIC_REFERENCE_ACQUIRED_AT={reference.get('acquired_at') or 'UNAVAILABLE'}",
            f"CURRENT_PUBLIC_REFERENCE_SYMBOL={reference.get('symbol') or 'UNAVAILABLE'}",
            f"CURRENT_PUBLIC_REFERENCE_PROVIDER={reference_provider}",
            f"CURRENT_PUBLIC_REFERENCE_FIELD={reference.get('field') or 'UNAVAILABLE'}",
            f"CURRENT_PUBLIC_REFERENCE_TIMEFRAME={reference.get('timeframe') or 'UNAVAILABLE'}",
            f"CURRENT_PUBLIC_REFERENCE_STATUS={reference.get('status') or 'UNAVAILABLE'}",
            f"ANCHOR_AGE_SECONDS={price_context.get('anchor_age_seconds') if price_context.get('anchor_age_seconds') is not None else 'UNAVAILABLE'}",
            f"ANCHOR_AGE_HOURS={price_context.get('anchor_age_hours') if price_context.get('anchor_age_hours') is not None else 'UNAVAILABLE'}",
            f"CURRENT_VS_ANCHOR_GAP_USD={price_context.get('current_vs_anchor_gap_usd') if price_context.get('current_vs_anchor_gap_usd') is not None else 'UNAVAILABLE'}",
            f"CURRENT_VS_ANCHOR_GAP_PCT={price_context.get('current_vs_anchor_gap_pct') if price_context.get('current_vs_anchor_gap_pct') is not None else 'UNAVAILABLE'}",
        ]
        lines += ["", "```text", *machine, "```"]
    return "\n".join(lines)


def download_close(ticker, start):
    df = yf.download(
        ticker,
        start=start,
        interval="1d",
        auto_adjust=True,
        progress=False,
        threads=False,
    )
    if df.empty:
        return pd.DataFrame()
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = [c[0] for c in df.columns]
    if "Close" not in df.columns:
        return pd.DataFrame()
    df = df[["Close"]].dropna().copy()
    df.index = pd.to_datetime(df.index)
    if getattr(df.index, "tz", None) is not None:
        df.index = df.index.tz_convert(None)
    df.index = df.index.normalize()
    return df


def rsi(close, period=14):
    close = pd.to_numeric(close, errors="coerce")
    delta = close.diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    avg_gain = gain.ewm(alpha=1 / period, adjust=False).mean()
    avg_loss = loss.ewm(alpha=1 / period, adjust=False).mean()
    rs = avg_gain / avg_loss.replace(0, np.nan)
    return 100 - (100 / (1 + rs))


def add_features(df):
    df = df.copy()
    df["rsi_14"] = rsi(df["Close"], 14)
    for ma in [20, 50, 100, 200]:
        df[f"ma_{ma}"] = df["Close"].rolling(ma).mean()
        df[f"dist_ma_{ma}"] = (df["Close"] / df[f"ma_{ma}"] - 1) * 100
    df["log_return"] = np.log(df["Close"] / df["Close"].shift(1))
    return df


def find_low_anchor(df, start, end=None):
    if df.empty:
        return None, None
    if end is None:
        period = df.loc[pd.to_datetime(start) :].copy()
    else:
        period = df.loc[pd.to_datetime(start) : pd.to_datetime(end)].copy()
    if period.empty:
        period = df.tail(90).copy()
    low_date = period["Close"].idxmin()
    return low_date, safe_float(period.loc[low_date, "Close"])


def find_high_anchor(df, start, end):
    if df.empty:
        return None, None
    period = df.loc[pd.to_datetime(start) : pd.to_datetime(end)].copy()
    if period.empty:
        return None, None
    high_date = period["Close"].idxmax()
    return high_date, safe_float(period.loc[high_date, "Close"])


def normalize_path(df, anchor_date, anchor_price):
    path = df[df.index >= anchor_date].copy()
    if path.empty or anchor_price is None or anchor_price <= 0:
        return pd.DataFrame()
    path["norm"] = path["Close"] / anchor_price * 100
    path["pct_from_anchor"] = (path["Close"] / anchor_price - 1) * 100
    return path


def calendarize_path(path):
    """Rende il percorso realmente giornaliero, colmando eventuali buchi Yahoo.

    BTC e SOL trattano i giorni del frattale come giorni di calendario. Se Yahoo
    salta una candela, usare semplicemente ``len(path) - 1`` crea uno
    sfalsamento di un giorno tra report principale e tracker. Il forward-fill è
    coerente con la logica ``close on or before`` già usata dal tracker.
    """
    if path is None or path.empty:
        return pd.DataFrame()

    out = path.copy()
    out.index = pd.to_datetime(out.index, errors="coerce")
    try:
        out.index = out.index.tz_convert(None)
    except Exception:
        try:
            out.index = out.index.tz_localize(None)
        except Exception:
            pass

    out.index = out.index.normalize()
    out = out[~out.index.duplicated(keep="last")].sort_index()
    full_index = pd.date_range(out.index.min(), out.index.max(), freq="D")
    out = out.reindex(full_index)

    if "Volume" in out.columns:
        out["Volume"] = out["Volume"].fillna(0)

    other_cols = [col for col in out.columns if col != "Volume"]
    if other_cols:
        out[other_cols] = out[other_cols].ffill()

    out.index.name = path.index.name
    return out


def to_numeric_series(values):
    return pd.to_numeric(pd.Series(values).reset_index(drop=True), errors="coerce")


def correlation_similarity(a, b):
    a = to_numeric_series(a)
    b = to_numeric_series(b)
    valid = pd.concat([a, b], axis=1).dropna()
    if len(valid) < 5:
        return None
    x = valid.iloc[:, 0].to_numpy(dtype=float)
    y = valid.iloc[:, 1].to_numpy(dtype=float)
    if np.std(x) == 0 or np.std(y) == 0:
        return None
    corr = float(np.corrcoef(x, y)[0, 1])
    if np.isnan(corr):
        return None
    return max(0.0, min(100.0, (corr + 1.0) * 50.0))


def mean_abs_similarity(a, b, scale):
    a = to_numeric_series(a)
    b = to_numeric_series(b)
    valid = pd.concat([a, b], axis=1).dropna()
    if len(valid) < 5:
        return None
    mean_abs = float(np.mean(np.abs(valid.iloc[:, 0] - valid.iloc[:, 1])))
    return max(0.0, min(100.0, 100.0 - mean_abs * scale))


def combine_scores(items):
    total_score = 0.0
    total_weight = 0.0
    for score, weight in items:
        score = safe_float(score)
        if score is None:
            continue
        total_score += score * weight
        total_weight += weight
    if total_weight == 0:
        return None
    return total_score / total_weight


def quality_label(score):
    score = safe_float(score)
    if score is None:
        return "n/d"
    if score >= 80:
        return "ALTA"
    if score >= 65:
        return "MEDIA"
    if score >= 50:
        return "BASSA / DA CONTROLLARE"
    return "DEBOLE"


def phase_gap_status(sol_norm_now, btc_norm_equiv):
    sol_norm_now = safe_float(sol_norm_now)
    btc_norm_equiv = safe_float(btc_norm_equiv)
    if sol_norm_now is None or btc_norm_equiv is None or btc_norm_equiv <= 0:
        return None, "n/d"
    gap_pct = (sol_norm_now / btc_norm_equiv - 1) * 100
    if gap_pct > 15:
        text = "SOL è molto sopra il percorso BTC equivalente: la forma può essere simile, ma il prezzo non è aderente."
    elif gap_pct > 5:
        text = "SOL è sopra il percorso BTC equivalente."
    elif gap_pct < -15:
        text = "SOL è molto sotto il percorso BTC equivalente."
    elif gap_pct < -5:
        text = "SOL è sotto il percorso BTC equivalente."
    else:
        text = "SOL è abbastanza vicino al percorso BTC equivalente."
    return gap_pct, text


def compute_structural_similarity(btc_path, sol_path):
    """Misura la somiglianza della forma, non l'aderenza del livello di prezzo."""
    compare_len = min(len(btc_path), len(sol_path))
    if compare_len < 15:
        return {
            "compare_len": compare_len,
            "price_shape_similarity": None,
            "return_similarity": None,
            "rsi_similarity": None,
            "ma_similarity": None,
            "structural_similarity": None,
            # alias di compatibilità con i vecchi report/parser
            "price_similarity": None,
            "total_similarity": None,
        }

    btc = btc_path.iloc[:compare_len].copy()
    sol = sol_path.iloc[:compare_len].copy()

    btc_log_path = np.log(pd.to_numeric(btc["norm"], errors="coerce") / 100.0)
    sol_log_path = np.log(pd.to_numeric(sol["norm"], errors="coerce") / 100.0)

    # La correlazione è invariante rispetto alla scala: descrive la forma.
    price_shape_similarity = correlation_similarity(btc_log_path, sol_log_path)

    # Confronto del ritmo giornaliero, smussato a 3 giorni per ridurre rumore.
    btc_ret = pd.to_numeric(btc["log_return"], errors="coerce").rolling(3).mean()
    sol_ret = pd.to_numeric(sol["log_return"], errors="coerce").rolling(3).mean()
    return_similarity = correlation_similarity(btc_ret, sol_ret)

    rsi_similarity = mean_abs_similarity(
        btc["rsi_14"].reset_index(drop=True),
        sol["rsi_14"].reset_index(drop=True),
        scale=2.0,
    )

    ma_scores = []
    for ma in [20, 50, 100]:
        col = f"dist_ma_{ma}"
        ma_scores.append(
            mean_abs_similarity(
                btc[col].reset_index(drop=True),
                sol[col].reset_index(drop=True),
                scale=2.8,
            )
        )
    ma_similarity = combine_scores([(score, 1.0) for score in ma_scores])

    structural_similarity = combine_scores(
        [
            (price_shape_similarity, 0.50),
            (return_similarity, 0.20),
            (rsi_similarity, 0.20),
            (ma_similarity, 0.10),
        ]
    )

    return {
        "compare_len": compare_len,
        "price_shape_similarity": price_shape_similarity,
        "return_similarity": return_similarity,
        "rsi_similarity": rsi_similarity,
        "ma_similarity": ma_similarity,
        "structural_similarity": structural_similarity,
        "price_similarity": price_shape_similarity,
        "total_similarity": structural_similarity,
    }


def infer_program_start_date(sol_anchor_date, sol_current_date):
    anchor = pd.to_datetime(sol_anchor_date).normalize()
    current = pd.to_datetime(sol_current_date).normalize()
    try:
        start = pd.to_datetime(PROGRAM_START_DATE).normalize()
    except Exception:
        start = current
    return min(max(start, anchor), current)


def alignment_status(avg_abs_gap_pct):
    gap = safe_float(avg_abs_gap_pct)
    if gap is None:
        return "n/d"
    if gap <= 5:
        return "MOLTO ALLINEATO"
    if gap <= 10:
        return "ABBASTANZA ALLINEATO"
    if gap <= 15:
        return "DEVIAZIONE MODERATA"
    if gap <= 25:
        return "STACCATO / NON ADERENTE"
    return "MOLTO DEVIATO"


def compute_segment_alignment(btc_path, sol_path, start_day, end_day):
    if btc_path.empty or sol_path.empty:
        return {}
    max_day = min(len(btc_path), len(sol_path)) - 1
    start_day = int(max(0, start_day))
    end_day = int(min(max_day, end_day))
    if end_day < start_day:
        return {
            "start_day": start_day,
            "end_day": end_day,
            "days_checked": 0,
            "start_date": None,
            "end_date": None,
            "avg_abs_gap_pct": None,
            "median_abs_gap_pct": None,
            "last_gap_pct": None,
            "max_positive_gap_pct": None,
            "max_negative_gap_pct": None,
            "simple_alignment_score": None,
            "status": "n/d",
        }

    btc_seg = btc_path.iloc[start_day : end_day + 1]
    sol_seg = sol_path.iloc[start_day : end_day + 1]
    compare_len = min(len(btc_seg), len(sol_seg))
    btc_norm = pd.to_numeric(btc_seg["norm"].iloc[:compare_len], errors="coerce").reset_index(drop=True)
    sol_norm = pd.to_numeric(sol_seg["norm"].iloc[:compare_len], errors="coerce").reset_index(drop=True)
    valid = pd.concat([btc_norm, sol_norm], axis=1)
    valid.columns = ["btc_norm", "sol_norm"]
    valid = valid.dropna()
    valid = valid[valid["btc_norm"] > 0]

    if valid.empty:
        avg_abs_gap = median_abs_gap = last_gap = None
        max_positive_gap = max_negative_gap = simple_score = None
    else:
        gaps = (valid["sol_norm"] / valid["btc_norm"] - 1) * 100
        avg_abs_gap = float(np.mean(np.abs(gaps)))
        median_abs_gap = float(np.median(np.abs(gaps)))
        last_gap = float(gaps.iloc[-1])
        max_positive_gap = float(gaps.max())
        max_negative_gap = float(gaps.min())
        simple_score = max(0.0, min(100.0, 100.0 - avg_abs_gap * 2.0))

    return {
        "start_day": start_day,
        "end_day": end_day,
        "days_checked": compare_len,
        "start_date": fmt_date(sol_path.index[start_day]),
        "end_date": fmt_date(sol_path.index[end_day]),
        "start_date_it": fmt_date_it(sol_path.index[start_day]),
        "end_date_it": fmt_date_it(sol_path.index[end_day]),
        "avg_abs_gap_pct": avg_abs_gap,
        "median_abs_gap_pct": median_abs_gap,
        "last_gap_pct": last_gap,
        "max_positive_gap_pct": max_positive_gap,
        "max_negative_gap_pct": max_negative_gap,
        "simple_alignment_score": simple_score,
        "status": alignment_status(avg_abs_gap),
    }


def build_split_alignment(btc_path, sol_path, sol_anchor_date, sol_current_date):
    program_start_date = infer_program_start_date(sol_anchor_date, sol_current_date)
    anchor = pd.to_datetime(sol_anchor_date).normalize()
    max_day = min(len(btc_path), len(sol_path)) - 1
    program_start_day = int((program_start_date - anchor).days)
    program_start_day = max(0, min(max_day, program_start_day))
    pre_end_day = program_start_day - 1

    if pre_end_day < 0:
        pre_program = compute_segment_alignment(btc_path, sol_path, 0, 0)
        pre_program["note"] = "Il monitoraggio parte dal bottom."
    else:
        pre_program = compute_segment_alignment(btc_path, sol_path, 0, pre_end_day)
        pre_program["note"] = "Backtest retroattivo precedente al monitoraggio reale."

    live_program = compute_segment_alignment(btc_path, sol_path, program_start_day, max_day)
    live_program["note"] = "Periodo osservato davvero dal programma."
    all_program = compute_segment_alignment(btc_path, sol_path, 0, max_day)
    all_program["note"] = "Media totale dal bottom."

    return {
        "program_start_date": fmt_date(program_start_date),
        "program_start_date_it": fmt_date_it(program_start_date),
        "program_start_day": program_start_day,
        "pre_program": pre_program,
        "live_program": live_program,
        "all": all_program,
    }


def build_split_alignment_table(split_alignment):
    rows = []
    for label, item in [
        ("Prima del programma", split_alignment.get("pre_program", {})),
        ("Da inizio programma", split_alignment.get("live_program", {})),
        ("Totale dal bottom", split_alignment.get("all", {})),
    ]:
        rows.append(
            [
                label,
                f"{item.get('start_date_it', 'n/d')} -> {item.get('end_date_it', 'n/d')}",
                item.get("days_checked", 0),
                fmt_pct(item.get("simple_alignment_score")),
                fmt_pct(item.get("avg_abs_gap_pct")),
                fmt_pct(item.get("last_gap_pct")),
                item.get("status", "n/d"),
            ]
        )
    return md_table(
        ["Periodo", "Date", "Giorni", "Aderenza prezzo", "Errore medio", "Gap ultimo", "Stato"],
        rows,
    )


def build_split_alignment_block(split_alignment):
    return "\n".join(
        [
            "Questa sezione separa la somiglianza della forma dall'aderenza reale del prezzo.",
            "",
            f"- **Inizio programma/scanner:** {split_alignment.get('program_start_date_it', 'n/d')}",
            "- **Prima del programma** = backtest retroattivo.",
            "- **Da inizio programma** = verifica live: è la parte più importante per l'uso operativo.",
            "",
            build_split_alignment_table(split_alignment),
            "",
            "Nota: un frattale può avere una forma simile ma un prezzo distante. In quel caso non è operativo finché il gap non rientra.",
        ]
    )


def build_operational_verdict(structural, split_alignment, phase_gap_pct):
    structural_score = safe_float(structural.get("structural_similarity"))
    live = split_alignment.get("live_program", {})
    live_days = int(live.get("days_checked") or 0)
    live_avg_gap = safe_float(live.get("avg_abs_gap_pct"))
    live_adherence = safe_float(live.get("simple_alignment_score"))
    last_gap = safe_float(phase_gap_pct)

    reasons = []
    if structural_score is not None:
        reasons.append(f"Somiglianza strutturale {fmt_pct(structural_score)}.")
    if live_adherence is not None:
        reasons.append(f"Aderenza prezzo live {fmt_pct(live_adherence)}.")
    if live_avg_gap is not None:
        reasons.append(f"Errore medio live {fmt_pct(live_avg_gap)}.")
    if last_gap is not None:
        reasons.append(f"Gap corrente SOL vs BTC scalato {fmt_pct(last_gap)}.")

    if structural_score is None:
        return {
            "label": "DATI INSUFFICIENTI",
            "short": "Non ci sono abbastanza dati per valutare il frattale.",
            "action": "Aspetta altri dati.",
            "confidence": "n/d",
            "operational_weight": 0,
            "reasons": reasons,
        }

    if structural_score < 50:
        return {
            "label": "NO, STRUTTURA POCO ANALOGA",
            "short": "La forma del percorso non è abbastanza simile a BTC 2022.",
            "action": "Non usare questo frattale come guida.",
            "confidence": "DEBOLE",
            "operational_weight": 0,
            "reasons": reasons,
        }

    if live_days < MIN_LIVE_DAYS:
        return {
            "label": "STRUTTURA ANALOGA, VERIFICA LIVE TROPPO CORTA",
            "short": "La struttura è interessante, ma il monitoraggio reale è ancora troppo breve.",
            "action": "Usalo solo come scenario secondario.",
            "confidence": "BASSA",
            "operational_weight": 0,
            "reasons": reasons,
        }

    if (
        structural_score >= 75
        and live_avg_gap is not None
        and live_avg_gap <= GOOD_LIVE_AVG_GAP
        and last_gap is not None
        and abs(last_gap) <= 10
    ):
        return {
            "label": "SI, STRUTTURA E PREZZO ADERENTI",
            "short": "Forma e livello di prezzo stanno seguendo bene il percorso BTC 2022.",
            "action": "Il frattale può essere uno scenario principale, sempre con invalidazioni chiare.",
            "confidence": "ALTA" if live_days >= 14 else "MEDIA",
            "operational_weight": 2,
            "reasons": reasons,
        }

    if (
        structural_score >= 65
        and live_avg_gap is not None
        and live_avg_gap <= ACCEPTABLE_LIVE_AVG_GAP
        and last_gap is not None
        and abs(last_gap) <= 15
    ):
        return {
            "label": "PARZIALMENTE SI / ADERENZA DISCRETA",
            "short": "La forma è simile e il prezzo è abbastanza vicino, ma non perfettamente aderente.",
            "action": "Scenario utile ma secondario finché l'aderenza non migliora.",
            "confidence": "MEDIA",
            "operational_weight": 1,
            "reasons": reasons,
        }

    if structural_score >= 65 and (
        (live_avg_gap is not None and live_avg_gap > MAX_OPERATIVE_LIVE_AVG_GAP)
        or (last_gap is not None and abs(last_gap) > MAX_OPERATIVE_LAST_GAP)
    ):
        return {
            "label": "STRUTTURA ANALOGA, PREZZO NON ADERENTE",
            "short": "La geometria ricorda BTC 2022, ma SOL è troppo distante dal percorso scalato per usarlo come conferma operativa.",
            "action": (
                f"Non assegnare punti operativi al frattale finché il gap non rientra circa entro ±{GAP_REENTRY_THRESHOLD:.0f}% "
                "e l'aderenza live non migliora."
            ),
            "confidence": "BASSA / NON OPERATIVO",
            "operational_weight": 0,
            "reasons": reasons,
        }

    if structural_score >= 55:
        return {
            "label": "ANALOGIA DEBOLE / SCENARIO SECONDARIO",
            "short": "Esistono alcuni elementi comuni, ma non abbastanza per una conferma.",
            "action": "Osserva soltanto; non usarlo per leva o decisioni principali.",
            "confidence": "BASSA",
            "operational_weight": 0,
            "reasons": reasons,
        }

    return {
        "label": "NO, NON LO STA SEGUENDO BENE",
        "short": "Il paragone con BTC 2022 è debole.",
        "action": "Le proiezioni hanno poca utilità finché i dati non migliorano.",
        "confidence": "DEBOLE",
        "operational_weight": 0,
        "reasons": reasons,
    }


def price_adherence_failed(verdict):
    """True only when explicit price-gap evidence (or its canonical label) failed."""
    if "price_adherence_failed" in verdict:
        return bool(verdict.get("price_adherence_failed"))
    return verdict.get("label") == "STRUTTURA ANALOGA, PREZZO NON ADERENTE"


def verdict_status_text(verdict):
    label = str(verdict.get("label") or "MOTIVO NON DISPONIBILE")
    if verdict.get("operational_weight", 0) == 0:
        reasons = [label]
        if price_adherence_failed(verdict) and "PREZZO NON ADERENTE" not in label:
            reasons.append("PREZZO NON ADERENTE (soglia esplicita fallita)")
        return "NON OPERATIVO: " + " | ".join(reasons)
    return f"SCENARIO CONDIZIONALE: {label}"


def projection_caveat(verdict):
    if price_adherence_failed(verdict):
        return "Nota: le proiezioni restano condizionali; il prezzo non è aderente secondo le soglie canoniche."
    return f"Nota: le proiezioni restano condizionali. Motivo del verdetto: {verdict.get('label') or 'n/d'}."


def build_verdict_metadata(verdict, split_alignment, phase_gap_pct):
    live_avg_gap = safe_float(split_alignment.get("live_program", {}).get("avg_abs_gap_pct"))
    last_gap = safe_float(phase_gap_pct)
    live_avg_gap_failed = live_avg_gap is not None and live_avg_gap > MAX_OPERATIVE_LIVE_AVG_GAP
    last_gap_failed = last_gap is not None and abs(last_gap) > MAX_OPERATIVE_LAST_GAP
    return {
        "verdict_label": verdict.get("label"),
        "price_adherence_failed": live_avg_gap_failed or last_gap_failed,
        "price_adherence_live_avg_gap_failed": live_avg_gap_failed,
        "price_adherence_last_gap_failed": last_gap_failed,
        "price_adherence_live_avg_gap_threshold_pct": MAX_OPERATIVE_LIVE_AVG_GAP,
        "price_adherence_last_gap_threshold_pct": MAX_OPERATIVE_LAST_GAP,
        "price_adherence_observed_live_avg_gap_pct": live_avg_gap,
        "price_adherence_observed_last_gap_pct": last_gap,
    }


def build_verdict_metadata_block(verdict, split_alignment, phase_gap_pct):
    metadata = build_verdict_metadata(verdict, split_alignment, phase_gap_pct)
    return "\n".join(
        [
            "### Metadata aderenza prezzo",
            "",
            "```text",
            f"OPERATIONAL_VERDICT_REASON={metadata.get('verdict_label') or 'UNAVAILABLE'}",
            f"PRICE_ADHERENCE_FAILED={'YES' if metadata.get('price_adherence_failed') else 'NO'}",
            f"PRICE_ADHERENCE_LIVE_AVG_GAP_FAILED={'YES' if metadata.get('price_adherence_live_avg_gap_failed') else 'NO'}",
            f"PRICE_ADHERENCE_LAST_GAP_FAILED={'YES' if metadata.get('price_adherence_last_gap_failed') else 'NO'}",
            f"PRICE_ADHERENCE_LIVE_AVG_GAP_THRESHOLD_PCT={metadata.get('price_adherence_live_avg_gap_threshold_pct')}",
            f"PRICE_ADHERENCE_LAST_GAP_THRESHOLD_PCT={metadata.get('price_adherence_last_gap_threshold_pct')}",
            f"PRICE_ADHERENCE_OBSERVED_LIVE_AVG_GAP_PCT={metadata.get('price_adherence_observed_live_avg_gap_pct')}",
            f"PRICE_ADHERENCE_OBSERVED_LAST_GAP_PCT={metadata.get('price_adherence_observed_last_gap_pct')}",
            "```",
        ]
    )


def volatility_beta(btc_path, sol_path, compare_len):
    btc_ret = btc_path["log_return"].iloc[:compare_len].dropna()
    sol_ret = sol_path["log_return"].iloc[:compare_len].dropna()
    if len(btc_ret) < 10 or len(sol_ret) < 10:
        return 1.0
    btc_vol = float(btc_ret.std())
    sol_vol = float(sol_ret.std())
    if btc_vol <= 0:
        return 1.0
    return max(0.60, min(2.00, sol_vol / btc_vol))


def projection_price(sol_current_price, relative_move, beta_ratio=1.0):
    sol_current_price = safe_float(sol_current_price)
    relative_move = safe_float(relative_move)
    beta_ratio = safe_float(beta_ratio) or 1.0
    if sol_current_price is None or relative_move is None or relative_move <= 0:
        return None
    return sol_current_price * np.exp(np.log(relative_move) * beta_ratio)


def projection_from_btc(btc_path, sol_current_price, sol_current_date, sol_elapsed_days, beta_ratio):
    rows = []
    if btc_path.empty or sol_current_price is None:
        return rows
    current_idx = min(sol_elapsed_days, len(btc_path) - 1)
    current_norm = safe_float(btc_path["norm"].iloc[current_idx])
    if current_norm is None or current_norm <= 0:
        return rows

    for horizon in FORECAST_DAYS:
        future_idx = current_idx + horizon
        if future_idx >= len(btc_path):
            continue
        future_norm = safe_float(btc_path["norm"].iloc[future_idx])
        if future_norm is None:
            continue
        future_slice = btc_path["norm"].iloc[current_idx : future_idx + 1]
        relative_slice = future_slice / current_norm
        relative = future_norm / current_norm
        low_relative = safe_float(relative_slice.min())
        high_relative = safe_float(relative_slice.max())
        rows.append(
            {
                "horizon_days": horizon,
                "sol_current_date": fmt_date(sol_current_date),
                "sol_future_date": fmt_date(add_days(sol_current_date, horizon)),
                "sol_future_date_it": fmt_date_it(add_days(sol_current_date, horizon)),
                "btc_equivalent_future_date": str(btc_path.index[future_idx].date()),
                "btc_move_from_equivalent_today_pct": (relative - 1) * 100,
                "sol_projection_base_price": sol_current_price * relative,
                "sol_projection_beta_price": projection_price(sol_current_price, relative, beta_ratio),
                "sol_path_low_base_price": sol_current_price * low_relative,
                "sol_path_low_beta_price": projection_price(sol_current_price, low_relative, beta_ratio),
                "sol_path_low_base_pct": (low_relative - 1) * 100,
                "sol_path_high_base_price": sol_current_price * high_relative,
                "sol_path_high_beta_price": projection_price(sol_current_price, high_relative, beta_ratio),
                "sol_path_high_base_pct": (high_relative - 1) * 100,
            }
        )
    return rows


def stage_sequence_label(low_pct, high_pct, end_pct, low_offset, high_offset):
    low_pct = safe_float(low_pct)
    high_pct = safe_float(high_pct)
    end_pct = safe_float(end_pct)
    if low_pct is None or high_pct is None or end_pct is None:
        return "n/d"
    if low_pct <= -3 and high_pct >= 3:
        return "Prima retest / debolezza, poi recupero." if low_offset <= high_offset else "Prima spike, poi scarico."
    if end_pct >= 8 and low_pct > -3:
        return "Spinta rialzista abbastanza pulita."
    if end_pct >= 4:
        return "Leggera continuazione rialzista."
    if end_pct <= -8:
        return "Fase negativa / rischio discesa."
    if high_pct >= 5 and end_pct < 2:
        return "Spike poco sostenuto."
    if low_pct <= -5 and end_pct > -2:
        return "Pullback e recupero parziale."
    return "Laterale / movimento non forte."


def build_stage_roadmap(btc_path, sol_current_price, sol_current_date, sol_elapsed_days, beta_ratio):
    rows = []
    if btc_path.empty or sol_current_price is None:
        return rows
    current_idx = min(sol_elapsed_days, len(btc_path) - 1)
    current_norm = safe_float(btc_path["norm"].iloc[current_idx])
    if current_norm is None or current_norm <= 0:
        return rows

    for start_offset, end_offset, stage_name in STAGE_BUCKETS:
        start_idx = current_idx + start_offset
        end_idx = min(current_idx + end_offset, len(btc_path) - 1)
        if start_idx >= len(btc_path) or end_idx < start_idx:
            continue
        stage_slice = btc_path["norm"].iloc[start_idx : end_idx + 1]
        if stage_slice.empty:
            continue
        end_norm = safe_float(btc_path["norm"].iloc[end_idx])
        low_norm = safe_float(stage_slice.min())
        high_norm = safe_float(stage_slice.max())
        low_idx = stage_slice.idxmin()
        high_idx = stage_slice.idxmax()
        low_offset = int((low_idx - btc_path.index[current_idx]).days)
        high_offset = int((high_idx - btc_path.index[current_idx]).days)
        end_relative = end_norm / current_norm
        low_relative = low_norm / current_norm
        high_relative = high_norm / current_norm
        end_pct = (end_relative - 1) * 100
        low_pct = (low_relative - 1) * 100
        high_pct = (high_relative - 1) * 100
        rows.append(
            {
                "stage": stage_name,
                "start_day": start_offset,
                "end_day": end_offset,
                "sol_stage_start_date": fmt_date(add_days(sol_current_date, start_offset)),
                "sol_stage_start_date_it": fmt_date_it(add_days(sol_current_date, start_offset)),
                "sol_stage_end_date": fmt_date(add_days(sol_current_date, end_offset)),
                "sol_stage_end_date_it": fmt_date_it(add_days(sol_current_date, end_offset)),
                "btc_end_date": str(btc_path.index[end_idx].date()),
                "btc_end_move_pct": end_pct,
                "btc_low_move_pct": low_pct,
                "btc_high_move_pct": high_pct,
                "low_day_offset": low_offset,
                "high_day_offset": high_offset,
                "sol_low_date": fmt_date(add_days(sol_current_date, low_offset)),
                "sol_low_date_it": fmt_date_it(add_days(sol_current_date, low_offset)),
                "sol_high_date": fmt_date(add_days(sol_current_date, high_offset)),
                "sol_high_date_it": fmt_date_it(add_days(sol_current_date, high_offset)),
                "sol_end_base_price": sol_current_price * end_relative,
                "sol_end_beta_price": projection_price(sol_current_price, end_relative, beta_ratio),
                "sol_low_base_price": sol_current_price * low_relative,
                "sol_low_beta_price": projection_price(sol_current_price, low_relative, beta_ratio),
                "sol_high_base_price": sol_current_price * high_relative,
                "sol_high_beta_price": projection_price(sol_current_price, high_relative, beta_ratio),
                "sequence": stage_sequence_label(low_pct, high_pct, end_pct, low_offset, high_offset),
            }
        )
    return rows


def build_key_levels(sol_current_price, sol_anchor_price, projections):
    sol_current_price = safe_float(sol_current_price)
    sol_anchor_price = safe_float(sol_anchor_price)
    if sol_current_price is None:
        return {
            "confirm_1": None,
            "confirm_2": None,
            "soft_invalid": None,
            "hard_invalid": sol_anchor_price,
            "gap_reentry_threshold": GAP_REENTRY_THRESHOLD,
            "support_note": "Dati insufficienti.",
        }

    first_14 = [p for p in projections if p.get("horizon_days") in [7, 14]]
    first_30 = [p for p in projections if p.get("horizon_days") in [14, 30]]
    first_60 = [p for p in projections if p.get("horizon_days") in [30, 60]]

    highs_14 = [safe_float(p.get("sol_path_high_base_price")) for p in first_14]
    highs_30 = [safe_float(p.get("sol_path_high_base_price")) for p in first_30]
    highs_60 = [safe_float(p.get("sol_path_high_base_price")) for p in first_60]
    lows_30 = [safe_float(p.get("sol_path_low_base_price")) for p in first_30]
    highs_14 = [x for x in highs_14 if x is not None]
    highs_30 = [x for x in highs_30 if x is not None]
    highs_60 = [x for x in highs_60 if x is not None]
    lows_30 = [x for x in lows_30 if x is not None]

    # Prima conferma più vicina e pratica: almeno +5% o massimo del primo tratto breve.
    confirm_1 = max([sol_current_price * 1.05] + highs_14)
    # Seconda conferma: rottura più importante del percorso 30/60g.
    confirm_2 = max([sol_current_price * 1.12] + highs_30 + highs_60)
    projected_low_30 = min(lows_30) if lows_30 else sol_current_price * 0.98
    soft_invalid = min(projected_low_30, sol_current_price * 0.95)
    if sol_anchor_price is not None:
        soft_invalid = max(soft_invalid, sol_anchor_price * 1.12)
    hard_invalid = sol_anchor_price
    if hard_invalid is not None and hard_invalid > sol_current_price:
        hard_invalid = sol_current_price * 0.90

    support_note = (
        f"Per tornare operativo non basta salire: il gap rispetto al BTC scalato deve rientrare circa entro ±{GAP_REENTRY_THRESHOLD:.0f}%. "
        f"La prima conferma di prezzo è {fmt_price(confirm_1)}, mentre l'invalidazione soft è {fmt_price(soft_invalid)}."
    )
    return {
        "confirm_1": confirm_1,
        "confirm_2": confirm_2,
        "soft_invalid": soft_invalid,
        "hard_invalid": hard_invalid,
        "gap_reentry_threshold": GAP_REENTRY_THRESHOLD,
        "support_note": support_note,
    }


def current_phase(sol_current_price, key_levels, verdict):
    price = safe_float(sol_current_price)
    confirm_1 = safe_float(key_levels.get("confirm_1"))
    confirm_2 = safe_float(key_levels.get("confirm_2"))
    soft_invalid = safe_float(key_levels.get("soft_invalid"))
    hard_invalid = safe_float(key_levels.get("hard_invalid"))
    label = verdict.get("label", "")

    if price is None:
        return {"label": "DATI INSUFFICIENTI", "text": "Fase non classificabile.", "risk": "n/d"}
    if verdict.get("operational_weight", 0) == 0 and "PREZZO NON ADERENTE" in label:
        return {
            "label": "FRATTALE NON CONFERMATO DAL PREZZO",
            "text": "La forma è simile, ma il livello di prezzo è troppo distante. Non è una fase d'ingresso basata sul frattale.",
            "risk": "ALTO",
        }
    if verdict.get("operational_weight", 0) == 0 and ("NO" in label or "DEBOLE" in label or "TROPPO CORTA" in label):
        return {
            "label": "FRATTALE SOLO DI CONTESTO",
            "text": "Il paragone non ha ancora forza operativa.",
            "risk": "ALTO",
        }
    if hard_invalid is not None and price <= hard_invalid:
        return {"label": "FRATTALE ROTTO", "text": "SOL ha perso il bottom usato.", "risk": "MOLTO ALTO"}
    if soft_invalid is not None and price <= soft_invalid:
        return {"label": "SOTTO PRESSIONE", "text": "Il setup si indebolisce e richiede recupero.", "risk": "ALTO"}
    if confirm_1 is not None and price < confirm_1:
        return {"label": "FASE ANTICIPATA", "text": "Prima conferma non ancora superata.", "risk": "MEDIO / ALTO"}
    if confirm_2 is not None and price < confirm_2:
        return {"label": "CONFERMA INIZIALE", "text": "Il prezzo ha iniziato a confermare, ma manca la rottura principale.", "risk": "MEDIO"}
    return {
        "label": "CONFERMA FORTE / ATTENZIONE A INSEGUIRE",
        "text": "Il frattale è più credibile, ma il rischio di entrare tardi aumenta.",
        "risk": "MEDIO / RISCHIO INSEGUIMENTO",
    }


def build_operational_plan(sol_current_price, key_levels, verdict, phase, split_alignment, phase_gap_pct):
    confirm_1 = safe_float(key_levels.get("confirm_1"))
    confirm_2 = safe_float(key_levels.get("confirm_2"))
    soft_invalid = safe_float(key_levels.get("soft_invalid"))
    hard_invalid = safe_float(key_levels.get("hard_invalid"))
    live = split_alignment.get("live_program", {})
    live_adherence = live.get("simple_alignment_score")
    live_avg_gap = live.get("avg_abs_gap_pct")

    if verdict.get("operational_weight", 0) == 0:
        actual_reason = verdict.get("label") or "MOTIVO NON DISPONIBILE"
        summary = f"Il frattale resta non operativo. Motivo effettivo: {actual_reason}."
        rows = [
            ["Uso operativo", "NO", f"Peso 0 per il verdetto: {actual_reason}."],
            ["Aderenza live", fmt_pct(live_adherence), f"Errore medio live {fmt_pct(live_avg_gap)}."],
            ["Gap corrente", fmt_pct(phase_gap_pct), "Metrica separata dal motivo del verdetto."],
            ["Prima conferma prezzo", fmt_price(confirm_1), "Serve anche miglioramento del gap, non solo una candela sopra il livello."],
            ["Seconda conferma", fmt_price(confirm_2), "Rende più credibile il percorso, ma non sostituisce l'aderenza."],
            ["Invalidazione soft", fmt_price(soft_invalid), "Sotto questa zona il quadro peggiora."],
            ["Invalidazione forte", fmt_price(hard_invalid), "Sotto il bottom il paragone è quasi rotto."],
        ]
        if price_adherence_failed(verdict):
            rows[2][2] = f"Prezzo non aderente: superata almeno una soglia canonica ({MAX_OPERATIVE_LIVE_AVG_GAP:.0f}% medio / {MAX_OPERATIVE_LAST_GAP:.0f}% ultimo)."
        return summary, rows

    if "FASE ANTICIPATA" in phase.get("label", ""):
        summary = "Fase anticipata ma già aderente: eventuale esposizione solo a tranche, senza leva aggressiva."
        rows = [
            ["Spot anticipato", "SI, ma a tranche", "Forma e prezzo sono abbastanza aderenti."],
            ["Aggiunta", fmt_price(confirm_1), "Solo se rompe e tiene il livello."],
            ["Seconda conferma", fmt_price(confirm_2), "Scenario più credibile."],
            ["Invalidazione soft", fmt_price(soft_invalid), "Sotto questa zona il setup si indebolisce."],
            ["Invalidazione forte", fmt_price(hard_invalid), "Sotto questa zona il frattale è quasi rotto."],
        ]
        return summary, rows

    summary = "Il frattale è operativo solo con gestione prudente e controllo continuo del gap."
    rows = [
        ["Gestione", "Tranche / retest", "Non inseguire movimenti verticali."],
        ["Gap massimo utile", f"±{GAP_REENTRY_THRESHOLD:.0f}%", "Sopra questa distanza l'affidabilità operativa cala."],
        ["Invalidazione soft", fmt_price(soft_invalid), "Perdita di conferma."],
        ["Invalidazione forte", fmt_price(hard_invalid), "Frattale quasi rotto."],
    ]
    return summary, rows


def build_next_step_text(stages, verdict):
    if not stages:
        return "Dati insufficienti per il prossimo step."
    first = stages[0]
    prefix = "Proiezione condizionale, non conferma operativa" if verdict.get("operational_weight", 0) == 0 else "Prossimo step previsto"
    return (
        f"{prefix}: **{first.get('sequence', 'n/d')}** "
        f"Zona bassa **{fmt_price(first.get('sol_low_base_price'))}** intorno al **{first.get('sol_low_date_it', 'n/d')}**; "
        f"zona alta **{fmt_price(first.get('sol_high_base_price'))}** intorno al **{first.get('sol_high_date_it', 'n/d')}**; "
        f"fine step circa **{fmt_price(first.get('sol_end_base_price'))}** entro il **{first.get('sol_stage_end_date_it', 'n/d')}**."
    )


def make_daily_projection_path(btc_path, sol_current_price, sol_current_date, sol_elapsed_days, beta_ratio, max_days=365):
    rows = []
    if btc_path.empty or sol_current_price is None:
        return pd.DataFrame()
    current_idx = min(sol_elapsed_days, len(btc_path) - 1)
    current_norm = safe_float(btc_path["norm"].iloc[current_idx])
    if current_norm is None or current_norm <= 0:
        return pd.DataFrame()
    max_future_idx = min(len(btc_path) - 1, current_idx + max_days)
    for idx in range(current_idx, max_future_idx + 1):
        offset = idx - current_idx
        norm = safe_float(btc_path["norm"].iloc[idx])
        if norm is None:
            continue
        relative = norm / current_norm
        rows.append(
            {
                "offset_days": offset,
                "sol_date": add_days(sol_current_date, offset),
                "btc_equiv_date": btc_path.index[idx],
                "base_price": sol_current_price * relative,
                "beta_price": projection_price(sol_current_price, relative, beta_ratio),
                "base_norm": relative * 100,
            }
        )
    return pd.DataFrame(rows)


def build_cycle_projection(
    btc_path,
    btc_anchor_date,
    btc_anchor_price,
    btc_top_date,
    btc_top_price,
    sol_anchor_date,
    sol_anchor_price,
    sol_current_date,
    sol_current_price,
    sol_elapsed_days,
    beta_ratio,
):
    if btc_top_date is None or btc_top_price is None or btc_path.empty:
        return {}, pd.DataFrame()
    if sol_current_price is None or sol_anchor_price is None:
        return {}, pd.DataFrame()

    current_idx = min(int(sol_elapsed_days), len(btc_path) - 1)
    top_idx = int((pd.to_datetime(btc_top_date) - pd.to_datetime(btc_anchor_date)).days)
    top_idx = min(max(top_idx, 0), len(btc_path) - 1)
    if top_idx <= current_idx:
        return {}, pd.DataFrame()
    current_norm = safe_float(btc_path["norm"].iloc[current_idx])
    top_norm = safe_float(btc_path["norm"].iloc[top_idx])
    if current_norm is None or current_norm <= 0 or top_norm is None:
        return {}, pd.DataFrame()

    bottom_to_top_mult = btc_top_price / btc_anchor_price
    current_to_top_mult = top_norm / current_norm
    rows = []
    for idx in range(current_idx, top_idx + 1):
        offset = idx - current_idx
        norm = safe_float(btc_path["norm"].iloc[idx])
        if norm is None:
            continue
        relative = norm / current_norm
        rows.append(
            {
                "offset_days": offset,
                "sol_date": add_days(sol_current_date, offset),
                "btc_equiv_date": btc_path.index[idx],
                "base_price": sol_current_price * relative,
                "beta_price": projection_price(sol_current_price, relative, beta_ratio),
                "base_norm": relative * 100,
            }
        )
    cycle_daily = pd.DataFrame(rows)
    base_max_price = beta_max_price = None
    base_max_date = beta_max_date = None
    if not cycle_daily.empty:
        base_idx = cycle_daily["base_price"].idxmax()
        beta_idx = cycle_daily["beta_price"].idxmax()
        base_max_price = safe_float(cycle_daily.loc[base_idx, "base_price"])
        beta_max_price = safe_float(cycle_daily.loc[beta_idx, "beta_price"])
        base_max_date = fmt_date(cycle_daily.loc[base_idx, "sol_date"])
        beta_max_date = fmt_date(cycle_daily.loc[beta_idx, "sol_date"])

    cycle = {
        "btc_top_date": str(pd.to_datetime(btc_top_date).date()),
        "btc_top_date_it": fmt_date_it(btc_top_date),
        "btc_top_price": btc_top_price,
        "btc_top_offset_days": top_idx,
        "btc_bottom_to_top_mult": bottom_to_top_mult,
        "btc_current_to_top_mult": current_to_top_mult,
        "sol_cycle_top_date": fmt_date(add_days(sol_anchor_date, top_idx)),
        "sol_cycle_top_date_it": fmt_date_it(add_days(sol_anchor_date, top_idx)),
        "cycle_remaining_days": top_idx - current_idx,
        "target_from_bottom_base": sol_anchor_price * bottom_to_top_mult,
        "target_from_bottom_beta": projection_price(sol_anchor_price, bottom_to_top_mult, beta_ratio),
        "target_from_current_base": sol_current_price * current_to_top_mult,
        "target_from_current_beta": projection_price(sol_current_price, current_to_top_mult, beta_ratio),
        "cycle_max_base_price": base_max_price,
        "cycle_max_beta_price": beta_max_price,
        "cycle_max_base_date": base_max_date,
        "cycle_max_beta_date": beta_max_date,
        "cycle_max_base_date_it": fmt_date_it(base_max_date),
        "cycle_max_beta_date_it": fmt_date_it(beta_max_date),
    }
    return cycle, cycle_daily


def update_tracking_log(summary):
    columns = [
        "tracking_date",
        "generated_at_utc",
        "sol_current_price",
        "sol_elapsed_days",
        "btc_equivalent_date",
        "price_similarity",
        "rsi_similarity",
        "ma_similarity",
        "total_similarity",
        "structural_similarity",
        "live_adherence_score",
        "live_avg_abs_gap_pct",
        "phase_gap_pct",
        "verdict",
        "verdict_confidence",
        "operational_weight",
        "phase_label",
        "phase_risk",
        "confirm_1",
        "confirm_2",
        "soft_invalid",
        "hard_invalid",
        "cycle_max_base_price",
        "cycle_max_beta_price",
        "program_start_date",
        "pre_program_alignment_score",
        "pre_program_avg_abs_gap_pct",
        "live_program_alignment_score",
        "live_program_avg_abs_gap_pct",
        "all_alignment_score",
        "all_avg_abs_gap_pct",
    ]
    row = {key: summary.get(key) for key in columns}
    row["generated_at_utc"] = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    if os.path.exists(TRACKING_LOG_PATH):
        try:
            df = pd.read_csv(TRACKING_LOG_PATH)
        except Exception:
            df = pd.DataFrame(columns=columns)
    else:
        df = pd.DataFrame(columns=columns)
    for col in columns:
        if col not in df.columns:
            df[col] = np.nan
    if row.get("tracking_date") is not None:
        df = df[df["tracking_date"].astype(str) != str(row["tracking_date"])]
    df = pd.concat([df, pd.DataFrame([row])], ignore_index=True)
    df = df[columns]
    df["_sort"] = pd.to_datetime(df["tracking_date"], errors="coerce")
    df = df.sort_values("_sort").drop(columns="_sort")
    df.to_csv(TRACKING_LOG_PATH, index=False)
    return df


def build_tracking_status(tracking_df):
    if tracking_df is None or tracking_df.empty or len(tracking_df) < 2:
        return {"label": "STORICO INIZIALE", "text": "Storico ancora troppo corto.", "delta_similarity": None}
    df = tracking_df.copy()
    df["date"] = pd.to_datetime(df["tracking_date"], errors="coerce")
    df["sim"] = pd.to_numeric(df["structural_similarity"], errors="coerce")
    df = df.dropna(subset=["date", "sim"]).sort_values("date")
    if len(df) < 2:
        return {"label": "STORICO INIZIALE", "text": "Storico ancora troppo corto.", "delta_similarity": None}
    delta = float(df.iloc[-1]["sim"] - df.iloc[-2]["sim"])
    if delta >= 3:
        return {"label": "STRUTTURA IN MIGLIORAMENTO", "text": f"Somiglianza strutturale salita di {fmt_pct(delta)}.", "delta_similarity": delta}
    if delta <= -3:
        return {"label": "STRUTTURA IN PEGGIORAMENTO", "text": f"Somiglianza strutturale scesa di {fmt_pct(delta)}.", "delta_similarity": delta}
    return {"label": "STRUTTURA STABILE", "text": f"Variazione strutturale {fmt_pct(delta)}.", "delta_similarity": delta}


def build_projection_table(projections):
    rows = []
    for p in projections:
        rows.append(
            [
                f"{p['horizon_days']} giorni",
                p["sol_future_date_it"],
                p["btc_equivalent_future_date"],
                fmt_pct(p["btc_move_from_equivalent_today_pct"]),
                fmt_price(p["sol_projection_base_price"]),
                fmt_price(p["sol_projection_beta_price"]),
                fmt_price(p["sol_path_low_base_price"]),
                fmt_price(p["sol_path_high_base_price"]),
            ]
        )
    return md_table(
        ["Orizzonte", "Data SOL", "Data BTC eq.", "BTC fece", "SOL base", "SOL beta", "Min percorso", "Max percorso"],
        rows,
    ) if rows else "Dati insufficienti."


def build_stage_table(stages):
    rows = []
    for s in stages:
        rows.append(
            [
                s["stage"],
                f"{s['sol_stage_start_date_it']} -> {s['sol_stage_end_date_it']}",
                fmt_pct(s["btc_end_move_pct"]),
                fmt_price(s["sol_end_base_price"]),
                f"{fmt_price(s['sol_low_base_price'])} ({s['sol_low_date_it']})",
                f"{fmt_price(s['sol_high_base_price'])} ({s['sol_high_date_it']})",
                s["sequence"],
            ]
        )
    return md_table(
        ["Step", "Date SOL", "BTC fine", "SOL fine base", "Zona bassa", "Zona alta", "Lettura"],
        rows,
    ) if rows else "Dati insufficienti."


def build_cycle_table(cycle, verdict):
    if not cycle:
        return "Dati insufficienti."
    status = "CONTESTO MACRO, NON OPERATIVO" if verdict.get("operational_weight", 0) == 0 else "SCENARIO CONDIZIONALE"
    return md_table(
        ["Voce", "Valore", "Lettura"],
        [
            ["Stato", status, "Non è un segnale d'ingresso."],
            ["Top BTC 2025 usato", f"{cycle.get('btc_top_date_it')} - {fmt_price(cycle.get('btc_top_price'))}", "Massimo close BTC nella finestra 2025."],
            ["Data SOL equivalente", cycle.get("sol_cycle_top_date_it"), "Data analogica, non previsione certa."],
            ["Target base dal bottom", fmt_price(cycle.get("target_from_bottom_base")), "Scenario base."],
            ["Target base dall'anchor modello", fmt_price(cycle.get("target_from_current_base")), "Scenario condizionale dall'input computazionale, non dal riferimento live."],
            ["Massimo percorso base", f"{fmt_price(cycle.get('cycle_max_base_price'))} ({cycle.get('cycle_max_base_date_it')})", "Massimo base nel percorso."],
            ["Massimo beta", f"{fmt_price(cycle.get('cycle_max_beta_price'))} ({cycle.get('cycle_max_beta_date_it')})", "Scenario speculativo, non target principale."],
        ],
    )


def generate_fractal_chart(btc_path, sol_path, sol_elapsed_days, split_alignment):
    if not CHARTS_AVAILABLE or btc_path.empty or sol_path.empty:
        return False
    try:
        chart_end = min(len(btc_path) - 1, sol_elapsed_days + 365)
        btc_chart = btc_path.iloc[: chart_end + 1]
        sol_actual = sol_path.copy()
        current_idx = min(sol_elapsed_days, len(btc_path) - 1)
        btc_current_norm = safe_float(btc_path["norm"].iloc[current_idx])
        sol_current_norm = safe_float(sol_path["norm"].iloc[-1])
        projection_x, projection_y = [], []
        if btc_current_norm and sol_current_norm:
            for idx in range(current_idx, chart_end + 1):
                norm = safe_float(btc_path["norm"].iloc[idx])
                if norm is None:
                    continue
                projection_x.append(idx)
                projection_y.append(sol_current_norm * norm / btc_current_norm)

        fig, ax = plt.subplots(figsize=(12, 6))
        ax.plot(np.arange(len(btc_chart)), btc_chart["norm"], label="BTC dal bottom 2022")
        ax.plot(np.arange(len(sol_actual)), sol_actual["norm"], label="SOL dal bottom 2026")
        ax.plot(projection_x, projection_y, linestyle="--", label="Proiezione condizionale dall'anchor")
        ax.axvline(sol_elapsed_days, linestyle=":", alpha=0.8, label="Anchor SOL")
        live = split_alignment.get("live_program", {})
        subtitle = f"Struttura e prezzo separati | Aderenza live {fmt_pct(live.get('simple_alignment_score'))} | gap {fmt_pct(live.get('last_gap_pct'))}"
        ax.set_title("Frattale BTC 2022 vs SOL 2026 — INDICE BASE 100, NON USD\n" + subtitle)
        ax.set_xlabel("Giorni dal bottom")
        ax.set_ylabel("Prezzo normalizzato a 100 (indice; non USD)")
        ax.grid(True, alpha=0.3)
        ax.legend()
        fig.tight_layout()
        fig.savefig(FRACTAL_CHART_PATH, dpi=170, bbox_inches="tight")
        plt.close(fig)
        return True
    except Exception as exc:
        print(f"Could not generate fractal chart: {exc}")
        return False


def projection_chart_title(verdict, price_context=None):
    status = verdict_status_text(verdict)
    if not price_context:
        return f"Proiezione condizionale SOL — anchor modello\n{status}"
    anchor = price_context.get("anchor", {})
    reference = price_context.get("current_reference", {})
    anchor_line = (
        f"Anchor modello {fmt_chart_price(anchor.get('price'))} — {anchor.get('timestamp') or 'timestamp n/d'}"
        f" | {anchor.get('provider') or 'fonte n/d'} | Età {format_age(price_context.get('anchor_age_seconds'))}"
    )
    if reference.get("available"):
        reference_line = (
            f"Riferimento pubblico {fmt_chart_price(reference.get('price'))} — {reference.get('timestamp') or 'timestamp n/d'}"
            f" | {reference.get('provider') or 'fonte n/d'}"
            f" | Gap {fmt_chart_price(price_context.get('current_vs_anchor_gap_usd'))} / {fmt_pct(price_context.get('current_vs_anchor_gap_pct'))}"
        )
    else:
        reference_line = "Riferimento pubblico corrente: UNAVAILABLE (anchor modello invariato)"
    return f"Proiezione condizionale SOL — anchor modello invariato\n{anchor_line}\n{reference_line}\n{status}"


def generate_projection_chart(sol_path, projection_daily, key_levels, verdict, price_context=None):
    if not CHARTS_AVAILABLE or sol_path.empty or projection_daily.empty:
        return False
    try:
        fig, ax = plt.subplots(figsize=(14, 8))
        ax.plot(sol_path.index, sol_path["Close"], linewidth=2, label="SOL storico / input modello")
        ax.plot(projection_daily["sol_date"], projection_daily["base_price"], linestyle="--", linewidth=2, label="Percorso base dall'anchor modello")
        ax.plot(projection_daily["sol_date"], projection_daily["beta_price"], linestyle=":", linewidth=1.5, label="Percorso beta dall'anchor modello")
        current_date = sol_path.index[-1]
        current_price = safe_float(sol_path["Close"].iloc[-1])
        ax.axvline(current_date, linestyle=":", alpha=0.7)
        if current_price is not None:
            ax.scatter([current_date], [current_price], s=55, zorder=5, label="Anchor computazionale")
        reference = (price_context or {}).get("current_reference", {})
        reference_price = safe_float(reference.get("price")) if reference.get("available") else None
        reference_date = utc_timestamp(reference.get("timestamp"))
        if reference_price is not None:
            ax.axhline(reference_price, color="purple", linestyle="-.", alpha=0.6, label="Riferimento pubblico (solo display)")
            if reference_date is not None:
                ax.scatter([reference_date.tz_localize(None)], [reference_price], color="purple", marker="D", s=48, zorder=6)
        for label, value in [
            ("Prima conferma", key_levels.get("confirm_1")),
            ("Seconda conferma", key_levels.get("confirm_2")),
            ("Invalidazione soft", key_levels.get("soft_invalid")),
            ("Invalidazione forte", key_levels.get("hard_invalid")),
        ]:
            value = safe_float(value)
            if value is not None:
                ax.axhline(value, linestyle="--", alpha=0.25)
                ax.annotate(f"{label}: {fmt_price(value)}", xy=(1.005, value), xycoords=("axes fraction", "data"), fontsize=8, va="center")
        ax.set_title(projection_chart_title(verdict, price_context), fontsize=11)
        ax.set_xlabel("Data")
        ax.set_ylabel("Prezzo SOL (USD)")
        ax.grid(True, alpha=0.3)
        ax.legend(loc="upper left")
        fig.autofmt_xdate()
        fig.tight_layout()
        fig.savefig(PROJECTION_CHART_PATH, dpi=180, bbox_inches="tight")
        plt.close(fig)
        return True
    except Exception as exc:
        print(f"Could not generate projection chart: {exc}")
        return False


def generate_single_cycle_chart(sol_path, cycle_daily, cycle, output_path, mode="base", log_scale=False):
    if sol_path.empty or cycle_daily.empty or not cycle:
        return False
    fig, ax = plt.subplots(figsize=(14, 8))
    ax.plot(sol_path.index, sol_path["Close"], linewidth=2, label="SOL reale")
    if mode == "base":
        ax.plot(cycle_daily["sol_date"], cycle_daily["base_price"], linestyle="--", linewidth=2, label="Scenario base")
        title = "SCENARIO ANALOGICO SOL base fino al top equivalente BTC 2025"
    elif mode == "beta":
        ax.plot(cycle_daily["sol_date"], cycle_daily["beta_price"], linestyle=":", linewidth=2, label="Scenario beta speculativo")
        title = "SCENARIO ANALOGICO SOL beta speculativo"
    else:
        ax.plot(cycle_daily["sol_date"], cycle_daily["base_price"], linestyle="--", linewidth=1.8, label="Scenario base")
        ax.plot(cycle_daily["sol_date"], cycle_daily["beta_price"], linestyle=":", linewidth=1.5, label="Scenario beta")
        title = "SCENARIO ANALOGICO SOL base + beta"
    if log_scale:
        ax.set_yscale("log")
        ax.set_ylabel("Prezzo SOL - scala log")
    else:
        ax.set_ylabel("Prezzo SOL")
    ax.set_title(title + "\nNON è una previsione live — NON è un segnale di trading")
    ax.set_xlabel("Data SOL equivalente")
    ax.grid(True, alpha=0.3, which="both")
    ax.legend(loc="upper left")
    fig.autofmt_xdate()
    fig.tight_layout()
    fig.savefig(output_path, dpi=180, bbox_inches="tight")
    plt.close(fig)
    return True


def generate_cycle_chart(sol_path, cycle_daily, cycle):
    if not CHARTS_AVAILABLE:
        return False
    try:
        results = [
            generate_single_cycle_chart(sol_path, cycle_daily, cycle, CYCLE_BASE_CHART_PATH, "base", False),
            generate_single_cycle_chart(sol_path, cycle_daily, cycle, CYCLE_BETA_CHART_PATH, "beta", False),
            generate_single_cycle_chart(sol_path, cycle_daily, cycle, CYCLE_LOG_CHART_PATH, "log", True),
            generate_single_cycle_chart(sol_path, cycle_daily, cycle, CYCLE_CHART_PATH, "log", False),
        ]
        return any(results)
    except Exception as exc:
        print(f"Could not generate cycle charts: {exc}")
        return False


def generate_tracking_chart(tracking_df):
    if not CHARTS_AVAILABLE or tracking_df is None or tracking_df.empty or len(tracking_df) < 2:
        return False
    try:
        df = tracking_df.copy()
        df["date"] = pd.to_datetime(df["tracking_date"], errors="coerce")
        df["structural"] = pd.to_numeric(df["structural_similarity"], errors="coerce")
        df["adherence"] = pd.to_numeric(df["live_adherence_score"], errors="coerce")
        df = df.dropna(subset=["date"])
        fig, ax = plt.subplots(figsize=(12, 5))
        ax.plot(df["date"], df["structural"], marker="o", label="Somiglianza strutturale")
        ax.plot(df["date"], df["adherence"], marker="o", label="Aderenza prezzo live")
        ax.axhline(65, linestyle="--", alpha=0.3)
        ax.set_title("Tracking separato: struttura vs aderenza prezzo")
        ax.set_xlabel("Data")
        ax.set_ylabel("Score %")
        ax.grid(True, alpha=0.3)
        ax.legend()
        fig.autofmt_xdate()
        fig.tight_layout()
        fig.savefig(TRACKING_CHART_PATH, dpi=160, bbox_inches="tight")
        plt.close(fig)
        return True
    except Exception as exc:
        print(f"Could not generate tracking chart: {exc}")
        return False


def build_chart_block(fractal_ok, projection_ok, cycle_ok, tracking_ok):
    lines = ["## Grafici", ""]
    if fractal_ok:
        lines += [
            "### Frattale sovrapposto",
            "",
            "**Scala:** indice normalizzato, base 100. I valori non sono prezzi USD.",
            "",
            f"![Frattale BTC 2022 vs SOL 2026]({FRACTAL_CHART_FILE})",
            "",
        ]
    if projection_ok:
        lines += [
            "### Proiezione condizionale SOL",
            "",
            "Blu e proiezioni usano l'anchor computazionale; l'eventuale riferimento pubblico è un marker separato, solo display.",
            "",
            f"![Proiezione SOL BTC 2022]({PROJECTION_CHART_FILE})",
            "",
        ]
    if cycle_ok:
        lines += [
            "### Ciclo base fino al top BTC 2025",
            "",
            "**Scenario analogico in USD: non è una previsione live e non è un segnale di trading.**",
            "",
            f"![Ciclo base SOL BTC 2025]({CYCLE_BASE_CHART_FILE})",
            "",
            "### Base + beta in scala logaritmica",
            "",
            f"![Ciclo log SOL BTC 2025]({CYCLE_LOG_CHART_FILE})",
            "",
            "### Beta speculativo separato",
            "",
            f"![Ciclo beta SOL BTC 2025]({CYCLE_BETA_CHART_FILE})",
            "",
        ]
    if tracking_ok:
        lines += ["### Tracking struttura vs aderenza", "", f"![Tracking frattale BTC SOL]({TRACKING_CHART_FILE})", ""]
    if len(lines) == 2:
        lines += ["Grafici non generati.", ""]
    return "\n".join(lines)


def build_verdict_block(verdict, structural, split_alignment, key_levels, phase, phase_gap_pct, next_step_text):
    live = split_alignment.get("live_program", {})
    lines = [
        "## Verdetto diretto",
        "",
        "**SOL sta seguendo BTC 2022?**",
        "",
        f"### {verdict['label']}",
        "",
        f"**Sintesi:** {verdict['short']}",
        "",
        f"**Somiglianza strutturale:** {fmt_pct(structural.get('structural_similarity'))}",
        "",
        f"**Aderenza prezzo live:** {fmt_pct(live.get('simple_alignment_score'))}",
        "",
        f"**Errore medio live:** {fmt_pct(live.get('avg_abs_gap_pct'))}",
        "",
        f"**Gap corrente:** {fmt_pct(phase_gap_pct)}",
        "",
        f"**Fase attuale:** {phase['label']}",
        "",
        f"**Lettura fase:** {phase['text']}",
        "",
        f"**Rischio fase:** {phase['risk']}",
        "",
        f"**Prossimo step:** {next_step_text}",
        "",
        f"**Cosa fare:** {verdict['action']}",
        "",
        f"**Affidabilità:** {verdict['confidence']}",
        "",
        "### Perché",
        "",
    ]
    lines.extend([f"- {reason}" for reason in verdict.get("reasons", [])] or ["- Dati insufficienti."])
    lines += [
        "",
        "### Livelli pratici",
        "",
        md_table(
            ["Livello", "Prezzo / soglia", "Significato"],
            [
                ["Rientro gap", f"entro ±{key_levels.get('gap_reentry_threshold', GAP_REENTRY_THRESHOLD):.0f}%", "Condizione necessaria per tornare operativo."],
                ["Prima conferma prezzo", fmt_price(key_levels.get("confirm_1")), "Rottura iniziale, da accompagnare al rientro del gap."],
                ["Seconda conferma", fmt_price(key_levels.get("confirm_2")), "Scenario più credibile."],
                ["Invalidazione soft", fmt_price(key_levels.get("soft_invalid")), "Il setup si indebolisce."],
                ["Invalidazione forte", fmt_price(key_levels.get("hard_invalid")), "Il paragone è quasi rotto."],
            ],
        ),
        "",
        key_levels.get("support_note", ""),
    ]
    return "\n".join(lines)


def build_tracking_block(tracking_status, tracking_df):
    rows = []
    if tracking_df is not None and not tracking_df.empty:
        for _, row in tracking_df.tail(7).iterrows():
            rows.append(
                [
                    row.get("tracking_date", "n/d"),
                    fmt_price(row.get("sol_current_price")),
                    fmt_pct(row.get("structural_similarity")),
                    fmt_pct(row.get("live_adherence_score")),
                    fmt_pct(row.get("phase_gap_pct")),
                    row.get("verdict", "n/d"),
                ]
            )
    lines = [
        "## Tracking giornaliero",
        "",
        f"**Stato struttura:** {tracking_status.get('label')}",
        "",
        tracking_status.get("text", ""),
        "",
    ]
    if rows:
        lines.append(md_table(["Data", "Prezzo SOL", "Struttura", "Aderenza live", "Gap", "Verdetto"], rows))
    else:
        lines.append("Storico non disponibile.")
    return "\n".join(lines)


def build_report(
    btc_anchor_date,
    btc_anchor_price,
    sol_anchor_date,
    sol_anchor_price,
    sol_current_price,
    sol_current_date,
    sol_elapsed_days,
    btc_equiv_date,
    btc_norm_equiv,
    sol_norm_now,
    phase_gap_pct,
    phase_text,
    structural,
    beta_ratio,
    verdict,
    key_levels,
    phase,
    next_step_text,
    operational_summary,
    operational_rows,
    projections,
    stages,
    cycle,
    split_alignment,
    tracking_status,
    tracking_df,
    fractal_chart_ok,
    projection_chart_ok,
    cycle_chart_ok,
    tracking_chart_ok,
    price_context=None,
):
    generated_at = utc_timestamp((price_context or {}).get("report_generated_at") or datetime.now(timezone.utc))
    rome_now = generated_at.tz_convert(ZoneInfo("Europe/Rome")).strftime("%Y-%m-%d %H:%M:%S %Z")
    utc_now = generated_at.strftime("%Y-%m-%d %H:%M:%S UTC")
    lines = [
        "# Frattale mirato: BTC novembre 2022 vs SOL giugno 2026",
        "",
        f"Generato: **{rome_now}**",
        f"UTC: **{utc_now}**",
        "",
        f"Ultima candela SOL usata: **{fmt_date_it(sol_current_date)}**",
        "",
        build_price_context_block(price_context, include_machine_metadata=True) if price_context else "SOL PRICE CONTEXT non disponibile.",
        "",
        "Correzione metodologica: questo report separa **somiglianza strutturale** e **aderenza reale del prezzo**.",
        "Un 70% di forma simile non significa che il prezzo sia vicino al percorso BTC scalato.",
        "",
        build_verdict_block(verdict, structural, split_alignment, key_levels, phase, phase_gap_pct, next_step_text),
        "",
        build_verdict_metadata_block(verdict, split_alignment, phase_gap_pct),
        "",
        "## Somiglianza prima e dopo inizio programma",
        "",
        build_split_alignment_block(split_alignment),
        "",
        "## Lettura operativa",
        "",
        operational_summary,
        "",
        md_table(["Voce", "Risposta", "Perché"], operational_rows),
        "",
        build_tracking_block(tracking_status, tracking_df),
        "",
        build_chart_block(fractal_chart_ok, projection_chart_ok, cycle_chart_ok, tracking_chart_ok),
        "",
        "## Proiezione fino al top BTC 2025",
        "",
        build_cycle_table(cycle, verdict),
        "",
        "## Prossimi step condizionali",
        "",
        build_stage_table(stages),
        "",
        "## Proiezione standard a giorni fissi",
        "",
        "Queste proiezioni partono dall'anchor computazionale SOL e replicano i movimenti futuri del BTC equivalente. Il riferimento pubblico corrente è solo contesto e non modifica i percorsi.",
        "",
        build_projection_table(projections),
        "",
        "## Dati base",
        "",
        md_table(
            ["Voce", "Data", "Valore"],
            [
                ["BTC bottom usato", str(btc_anchor_date.date()), fmt_price(btc_anchor_price)],
                ["SOL bottom usato", str(sol_anchor_date.date()), fmt_price(sol_anchor_price)],
                ["Anchor computazionale SOL", fmt_date_it(sol_current_date), fmt_price(sol_current_price)],
                ["Giorni SOL dal bottom", "-", sol_elapsed_days],
                ["Data BTC equivalente", str(btc_equiv_date.date()), "-"],
                ["BTC normalizzato equivalente", "-", fmt_number(btc_norm_equiv, 2)],
                ["SOL normalizzato oggi", "-", fmt_number(sol_norm_now, 2)],
                ["Gap SOL vs BTC equivalente", "-", fmt_pct(phase_gap_pct)],
                ["Lettura gap", "-", phase_text],
                ["Somiglianza forma prezzo", "-", fmt_pct(structural.get("price_shape_similarity"))],
                ["Somiglianza ritmo/rendimenti", "-", fmt_pct(structural.get("return_similarity"))],
                ["Somiglianza RSI", "-", fmt_pct(structural.get("rsi_similarity"))],
                ["Somiglianza medie", "-", fmt_pct(structural.get("ma_similarity"))],
                ["Somiglianza strutturale", "-", fmt_pct(structural.get("structural_similarity"))],
                ["Beta volatilità SOL/BTC", "-", fmt_number(beta_ratio, 2)],
            ],
        ),
        "",
        "## Regola di lettura",
        "",
        "- **Struttura alta + aderenza alta** = frattale utile.",
        "- **Struttura alta + aderenza bassa** = forma simile, ma non conferma operativa.",
        "- **Gap oltre ±15/18%** = il prezzo è troppo staccato per assegnare punti al Global.",
        "- **Rientro del gap entro circa ±12%** = primo requisito per rivalutare il frattale.",
        "",
    ]
    return "\n".join(lines)


def build_main_report_block(
    verdict,
    structural,
    sol_current_date,
    sol_elapsed_days,
    btc_equiv_date,
    key_levels,
    phase,
    phase_gap_pct,
    next_step_text,
    operational_summary,
    operational_rows,
    stages,
    projections,
    cycle,
    split_alignment,
    tracking_status,
    fractal_chart_ok,
    projection_chart_ok,
    cycle_chart_ok,
    tracking_chart_ok,
    price_context=None,
):
    live = split_alignment.get("live_program", {})
    quick_projection_rows = []
    for p in projections:
        if p["horizon_days"] in [7, 14, 30, 60, 90, 120]:
            quick_projection_rows.append(
                [
                    f"{p['horizon_days']} giorni",
                    p["sol_future_date_it"],
                    fmt_pct(p["btc_move_from_equivalent_today_pct"]),
                    fmt_price(p["sol_projection_base_price"]),
                    fmt_price(p["sol_path_low_base_price"]),
                    fmt_price(p["sol_path_high_base_price"]),
                ]
            )
    quick_stage_rows = []
    for s in stages[:4]:
        quick_stage_rows.append(
            [
                s["stage"],
                f"{s['sol_stage_start_date_it']} -> {s['sol_stage_end_date_it']}",
                fmt_pct(s["btc_end_move_pct"]),
                f"{fmt_price(s['sol_low_base_price'])} ({s['sol_low_date_it']})",
                f"{fmt_price(s['sol_high_base_price'])} ({s['sol_high_date_it']})",
                fmt_price(s["sol_end_base_price"]),
                s["sequence"],
            ]
        )

    chart_lines = []
    if fractal_chart_ok:
        chart_lines += ["### Grafico frattale sovrapposto", "", "Scala normalizzata base 100; valori non USD.", "", f"![Frattale BTC 2022 vs SOL 2026]({FRACTAL_CHART_FILE})", ""]
    if projection_chart_ok:
        chart_lines += ["### Grafico proiezione condizionale", "", "Serie e proiezioni ancorate all'input computazionale; riferimento pubblico separato e solo display.", "", f"![Proiezione SOL BTC 2022]({PROJECTION_CHART_FILE})", ""]
    if cycle_chart_ok:
        chart_lines += ["### Grafico ciclo base", "", "Scenario analogico in USD; non previsione live e non segnale di trading.", "", f"![Ciclo base SOL BTC 2025]({CYCLE_BASE_CHART_FILE})", ""]
    if tracking_chart_ok:
        chart_lines += ["### Grafico struttura vs aderenza", "", f"![Tracking frattale BTC SOL]({TRACKING_CHART_FILE})", ""]

    cycle_rows = []
    if cycle:
        cycle_rows = [
            ["Stato", "CONTESTO / NON OPERATIVO" if verdict.get("operational_weight", 0) == 0 else "CONDIZIONALE"],
            ["Top BTC 2025", f"{cycle.get('btc_top_date_it')} - {fmt_price(cycle.get('btc_top_price'))}"],
            ["Data SOL equivalente", cycle.get("sol_cycle_top_date_it")],
            ["Target ciclo base dall'anchor modello", fmt_price(cycle.get("target_from_current_base"))],
            ["Massimo percorso base", f"{fmt_price(cycle.get('cycle_max_base_price'))} ({cycle.get('cycle_max_base_date_it')})"],
        ]

    return "\n".join(
        [
            "<!-- BTC_SOL_FRACTAL_START -->",
            "",
            "---",
            "",
            "# Frattale mirato: BTC 2022 vs SOL 2026",
            "",
            "Report separato completo: [btc_2022_vs_sol_2026_report.md](btc_2022_vs_sol_2026_report.md)",
            "",
            f"Ultima candela SOL usata: **{fmt_date_it(sol_current_date)}**",
            "",
            build_price_context_block(price_context, include_machine_metadata=True) if price_context else "SOL PRICE CONTEXT non disponibile.",
            "",
            f"## Verdetto: {verdict['label']}",
            "",
            f"- **Fase attuale:** {phase['label']}",
            f"- **Somiglianza totale:** {fmt_pct(structural.get('structural_similarity'))}",
            f"- **Somiglianza strutturale:** {fmt_pct(structural.get('structural_similarity'))}",
            f"- **Aderenza prezzo live:** {fmt_pct(live.get('simple_alignment_score'))}",
            f"- **Errore medio live:** {fmt_pct(live.get('avg_abs_gap_pct'))}",
            f"- **Gap prezzo corrente:** {fmt_pct(phase_gap_pct)}",
            f"- **Peso operativo suggerito:** {verdict.get('operational_weight', 0)}",
            f"- **Affidabilita:** {verdict['confidence']}",
            f"- **Rischio fase:** {phase['risk']}",
            f"- **Trend tracking:** {tracking_status.get('label')}",
            f"- **Sintesi:** {verdict['short']}",
            f"- **SOL è al giorno:** {sol_elapsed_days} dal bottom usato.",
            f"- **Giorno BTC equivalente:** {btc_equiv_date.date()}",
            f"- **Prossimo step:** {next_step_text}",
            "",
            build_verdict_metadata_block(verdict, split_alignment, phase_gap_pct),
            "",
            "## Somiglianza prima e dopo inizio programma",
            "",
            build_split_alignment_block(split_alignment),
            "",
            "## Lettura operativa veloce",
            "",
            operational_summary,
            "",
            md_table(["Voce", "Risposta", "Perché"], operational_rows),
            "",
            "## Target ciclo fino al top BTC 2025",
            "",
            md_table(["Voce", "Valore"], cycle_rows) if cycle_rows else "Dati insufficienti.",
            "",
            "## Grafici",
            "",
            "\n".join(chart_lines).strip() if chart_lines else "Grafici non generati.",
            "",
            "## Livelli chiave",
            "",
            md_table(
                ["Livello", "Prezzo / soglia", "Lettura"],
                [
                    ["Rientro gap", f"entro ±{GAP_REENTRY_THRESHOLD:.0f}%", "Condizione necessaria per tornare operativo."],
                    ["Prima conferma", fmt_price(key_levels.get("confirm_1")), "Deve accompagnarsi al rientro del gap."],
                    ["Seconda conferma", fmt_price(key_levels.get("confirm_2")), "Scenario più credibile."],
                    ["Invalidazione soft", fmt_price(key_levels.get("soft_invalid")), "Il frattale si indebolisce."],
                    ["Invalidazione forte", fmt_price(key_levels.get("hard_invalid")), "Il paragone si rompe."],
                ],
            ),
            "",
            "## Proiezione veloce con date SOL",
            "",
            md_table(["Orizzonte", "Data SOL", "BTC fece", "SOL base", "Min percorso", "Max percorso"], quick_projection_rows) if quick_projection_rows else "Dati insufficienti.",
            "",
            "## Prossimi step se SOL segue BTC 2022",
            "",
            md_table(["Step", "Date SOL", "BTC fine", "SOL zona bassa", "SOL zona alta", "SOL fine base", "Lettura"], quick_stage_rows) if quick_stage_rows else "Dati insufficienti.",
            "",
            projection_caveat(verdict),
            "",
            "<!-- BTC_SOL_FRACTAL_END -->",
        ]
    )


def inject_into_main_report(block):
    if not os.path.exists(MAIN_REPORT_PATH):
        return
    with open(MAIN_REPORT_PATH, "r", encoding="utf-8") as file:
        current = file.read()
    start_marker = "<!-- BTC_SOL_FRACTAL_START -->"
    end_marker = "<!-- BTC_SOL_FRACTAL_END -->"
    if start_marker in current and end_marker in current:
        before = current.split(start_marker)[0].rstrip()
        after = current.split(end_marker, 1)[1].lstrip()
        current = before + "\n\n" + after
    decision_end = "<!-- DECISION_REPORT_END -->"
    if decision_end in current:
        pos = current.find(decision_end) + len(decision_end)
        updated = current[:pos].rstrip() + "\n\n" + block.strip() + "\n\n" + current[pos:].lstrip()
    else:
        updated = block.strip() + "\n\n" + current.lstrip()
    with open(MAIN_REPORT_PATH, "w", encoding="utf-8") as file:
        file.write(updated.rstrip() + "\n")


def write_csv(summary, projections, stages, projection_daily, cycle, cycle_daily):
    rows = []
    summary_row = dict(summary)
    summary_row["row_type"] = "summary"
    rows.append(summary_row)
    if cycle:
        row = dict(cycle)
        row["row_type"] = "cycle_summary"
        rows.append(row)
    for item in projections:
        row = dict(item)
        row["row_type"] = "projection"
        rows.append(row)
    for item in stages:
        row = dict(item)
        row["row_type"] = "stage"
        rows.append(row)
    if not projection_daily.empty:
        for _, item in projection_daily.iterrows():
            rows.append(
                {
                    "row_type": "daily_projection",
                    "offset_days": item.get("offset_days"),
                    "sol_date": fmt_date(item.get("sol_date")),
                    "btc_equiv_date": fmt_date(item.get("btc_equiv_date")),
                    "base_price": item.get("base_price"),
                    "beta_price": item.get("beta_price"),
                    "base_norm": item.get("base_norm"),
                }
            )
    if cycle_daily is not None and not cycle_daily.empty:
        for _, item in cycle_daily.iterrows():
            rows.append(
                {
                    "row_type": "cycle_daily_projection",
                    "offset_days": item.get("offset_days"),
                    "sol_date": fmt_date(item.get("sol_date")),
                    "btc_equiv_date": fmt_date(item.get("btc_equiv_date")),
                    "base_price": item.get("base_price"),
                    "beta_price": item.get("beta_price"),
                    "base_norm": item.get("base_norm"),
                }
            )
    pd.DataFrame(rows).to_csv(CSV_PATH, index=False)


def main():
    os.makedirs(REPORT_DIR, exist_ok=True)
    btc = download_close(BTC_TICKER, start="2022-01-01")
    sol = download_close(SOL_TICKER, start="2026-01-01")
    btc = apply_snapshot_to_ohlcv(btc, BTC_TICKER)
    sol = apply_snapshot_to_ohlcv(sol, SOL_TICKER)
    if btc.empty or sol.empty:
        with open(REPORT_PATH, "w", encoding="utf-8") as file:
            file.write("# Frattale BTC 2022 vs SOL 2026\n\nDati insufficienti da Yahoo Finance.\n")
        print("Insufficient data.")
        return

    btc = add_features(btc)
    sol = add_features(sol)
    btc_anchor_date, btc_anchor_price = find_low_anchor(btc, BTC_BOTTOM_SEARCH_START, BTC_BOTTOM_SEARCH_END)
    btc_top_date, btc_top_price = find_high_anchor(btc, BTC_TOP_SEARCH_START, BTC_TOP_SEARCH_END)
    sol_anchor_date, sol_anchor_price = find_low_anchor(sol, SOL_BOTTOM_SEARCH_START, None)
    if btc_anchor_date is None or sol_anchor_date is None:
        raise RuntimeError("Anchor BTC/SOL non trovati.")

    btc_path = calendarize_path(normalize_path(btc, btc_anchor_date, btc_anchor_price))
    sol_path = calendarize_path(normalize_path(sol, sol_anchor_date, sol_anchor_price))
    if btc_path.empty or sol_path.empty:
        raise RuntimeError("Percorsi normalizzati non disponibili.")

    sol_current_price = safe_float(sol_path["Close"].iloc[-1])
    sol_current_date = sol_path.index[-1]
    sol_elapsed_days = len(sol_path) - 1
    btc_equiv_idx = min(sol_elapsed_days, len(btc_path) - 1)
    btc_equiv_date = btc_path.index[btc_equiv_idx]
    expected_btc_equiv_date = pd.to_datetime(btc_anchor_date).normalize() + pd.Timedelta(days=sol_elapsed_days)
    if pd.to_datetime(btc_equiv_date).normalize() != expected_btc_equiv_date:
        raise RuntimeError(
            "Allineamento frattale incoerente: la data BTC equivalente non "
            "corrisponde ai giorni di calendario dal bottom SOL."
        )
    btc_norm_equiv = safe_float(btc_path["norm"].iloc[btc_equiv_idx])
    sol_norm_now = safe_float(sol_path["norm"].iloc[-1])

    phase_gap_pct, phase_text = phase_gap_status(sol_norm_now, btc_norm_equiv)
    structural = compute_structural_similarity(btc_path, sol_path)
    compare_len = structural.get("compare_len") or min(len(btc_path), len(sol_path))
    beta_ratio = volatility_beta(btc_path, sol_path, compare_len)
    split_alignment = build_split_alignment(btc_path, sol_path, sol_anchor_date, sol_current_date)
    verdict = build_operational_verdict(structural, split_alignment, phase_gap_pct)
    verdict_metadata = build_verdict_metadata(verdict, split_alignment, phase_gap_pct)
    verdict["price_adherence_failed"] = verdict_metadata["price_adherence_failed"]
    verdict["price_adherence_live_avg_gap_failed"] = verdict_metadata["price_adherence_live_avg_gap_failed"]
    verdict["price_adherence_last_gap_failed"] = verdict_metadata["price_adherence_last_gap_failed"]

    projections = projection_from_btc(btc_path, sol_current_price, sol_current_date, sol_elapsed_days, beta_ratio)
    stages = build_stage_roadmap(btc_path, sol_current_price, sol_current_date, sol_elapsed_days, beta_ratio)
    key_levels = build_key_levels(sol_current_price, sol_anchor_price, projections)
    phase = current_phase(sol_current_price, key_levels, verdict)
    next_step_text = build_next_step_text(stages, verdict)
    operational_summary, operational_rows = build_operational_plan(
        sol_current_price,
        key_levels,
        verdict,
        phase,
        split_alignment,
        phase_gap_pct,
    )

    projection_daily = make_daily_projection_path(
        btc_path,
        sol_current_price,
        sol_current_date,
        sol_elapsed_days,
        beta_ratio,
        max_days=365,
    )
    cycle, cycle_daily = build_cycle_projection(
        btc_path,
        btc_anchor_date,
        btc_anchor_price,
        btc_top_date,
        btc_top_price,
        sol_anchor_date,
        sol_anchor_price,
        sol_current_date,
        sol_current_price,
        sol_elapsed_days,
        beta_ratio,
    )

    # Display context is deliberately collected only after every model, verdict,
    # level and projection input has been computed from the canonical anchor.
    # It must never flow back into those calculations.
    current_public_reference = fetch_current_public_reference()
    report_generated_at = datetime.now(timezone.utc)
    computational_anchor = build_computational_anchor(sol_current_price, sol_current_date)
    price_context = build_price_context(
        computational_anchor,
        current_public_reference,
        report_generated_at=report_generated_at,
    )

    pre = split_alignment.get("pre_program", {})
    live = split_alignment.get("live_program", {})
    all_period = split_alignment.get("all", {})
    summary = {
        "tracking_date": fmt_date(sol_current_date),
        "btc_anchor_date": str(btc_anchor_date.date()),
        "btc_anchor_price": btc_anchor_price,
        "btc_top_date": str(btc_top_date.date()) if btc_top_date is not None else None,
        "btc_top_price": btc_top_price,
        "sol_anchor_date": str(sol_anchor_date.date()),
        "sol_anchor_price": sol_anchor_price,
        "sol_current_date": fmt_date(sol_current_date),
        "sol_current_date_it": fmt_date_it(sol_current_date),
        "sol_current_price": sol_current_price,
        "sol_elapsed_days": sol_elapsed_days,
        "btc_equivalent_date": str(btc_equiv_date.date()),
        "btc_norm_equiv": btc_norm_equiv,
        "sol_norm_now": sol_norm_now,
        "phase_gap_pct": phase_gap_pct,
        "phase_text": phase_text,
        "price_similarity": structural.get("price_shape_similarity"),
        "rsi_similarity": structural.get("rsi_similarity"),
        "ma_similarity": structural.get("ma_similarity"),
        "total_similarity": structural.get("structural_similarity"),
        "structural_similarity": structural.get("structural_similarity"),
        "return_similarity": structural.get("return_similarity"),
        "live_adherence_score": live.get("simple_alignment_score"),
        "live_avg_abs_gap_pct": live.get("avg_abs_gap_pct"),
        "quality_label": quality_label(structural.get("structural_similarity")),
        "verdict": verdict.get("label"),
        "verdict_confidence": verdict.get("confidence"),
        "operational_weight": verdict.get("operational_weight", 0),
        "phase_label": phase.get("label"),
        "phase_risk": phase.get("risk"),
        "next_step_text": next_step_text,
        "operational_summary": operational_summary,
        "beta_ratio": beta_ratio,
        "confirm_1": key_levels.get("confirm_1"),
        "confirm_2": key_levels.get("confirm_2"),
        "soft_invalid": key_levels.get("soft_invalid"),
        "hard_invalid": key_levels.get("hard_invalid"),
        "cycle_max_base_price": cycle.get("cycle_max_base_price") if cycle else None,
        "cycle_max_beta_price": cycle.get("cycle_max_beta_price") if cycle else None,
        "program_start_date": split_alignment.get("program_start_date"),
        "program_start_day": split_alignment.get("program_start_day"),
        "pre_program_alignment_score": pre.get("simple_alignment_score"),
        "pre_program_avg_abs_gap_pct": pre.get("avg_abs_gap_pct"),
        "pre_program_last_gap_pct": pre.get("last_gap_pct"),
        "pre_program_status": pre.get("status"),
        "live_program_alignment_score": live.get("simple_alignment_score"),
        "live_program_avg_abs_gap_pct": live.get("avg_abs_gap_pct"),
        "live_program_last_gap_pct": live.get("last_gap_pct"),
        "live_program_status": live.get("status"),
        "all_alignment_score": all_period.get("simple_alignment_score"),
        "all_avg_abs_gap_pct": all_period.get("avg_abs_gap_pct"),
        "all_last_gap_pct": all_period.get("last_gap_pct"),
        "all_status": all_period.get("status"),
        "computational_anchor_price": computational_anchor.get("price"),
        "computational_anchor_field": computational_anchor.get("field"),
        "computational_anchor_timestamp": computational_anchor.get("timestamp"),
        "computational_anchor_symbol": computational_anchor.get("symbol"),
        "computational_anchor_provider": computational_anchor.get("provider"),
        "computational_anchor_timeframe": computational_anchor.get("timeframe"),
        "computational_anchor_completed": computational_anchor.get("completed"),
        "current_public_reference_price": current_public_reference.get("price"),
        "current_public_reference_timestamp": current_public_reference.get("timestamp"),
        "current_public_reference_acquired_at": current_public_reference.get("acquired_at"),
        "current_public_reference_symbol": current_public_reference.get("symbol"),
        "current_public_reference_provider": current_public_reference.get("provider"),
        "current_vs_anchor_gap_usd": price_context.get("current_vs_anchor_gap_usd"),
        "current_vs_anchor_gap_pct": price_context.get("current_vs_anchor_gap_pct"),
        "anchor_age_seconds": price_context.get("anchor_age_seconds"),
        "anchor_age_hours": price_context.get("anchor_age_hours"),
        **verdict_metadata,
    }

    tracking_df = update_tracking_log(summary)
    tracking_status = build_tracking_status(tracking_df)
    fractal_chart_ok = generate_fractal_chart(btc_path, sol_path, sol_elapsed_days, split_alignment)
    projection_chart_ok = generate_projection_chart(sol_path, projection_daily, key_levels, verdict, price_context)
    cycle_chart_ok = generate_cycle_chart(sol_path, cycle_daily, cycle)
    tracking_chart_ok = generate_tracking_chart(tracking_df)

    report = build_report(
        btc_anchor_date,
        btc_anchor_price,
        sol_anchor_date,
        sol_anchor_price,
        sol_current_price,
        sol_current_date,
        sol_elapsed_days,
        btc_equiv_date,
        btc_norm_equiv,
        sol_norm_now,
        phase_gap_pct,
        phase_text,
        structural,
        beta_ratio,
        verdict,
        key_levels,
        phase,
        next_step_text,
        operational_summary,
        operational_rows,
        projections,
        stages,
        cycle,
        split_alignment,
        tracking_status,
        tracking_df,
        fractal_chart_ok,
        projection_chart_ok,
        cycle_chart_ok,
        tracking_chart_ok,
        price_context,
    )
    with open(REPORT_PATH, "w", encoding="utf-8") as file:
        file.write(report)

    write_csv(summary, projections, stages, projection_daily, cycle, cycle_daily)
    main_block = build_main_report_block(
        verdict,
        structural,
        sol_current_date,
        sol_elapsed_days,
        btc_equiv_date,
        key_levels,
        phase,
        phase_gap_pct,
        next_step_text,
        operational_summary,
        operational_rows,
        stages,
        projections,
        cycle,
        split_alignment,
        tracking_status,
        fractal_chart_ok,
        projection_chart_ok,
        cycle_chart_ok,
        tracking_chart_ok,
        price_context,
    )
    inject_into_main_report(main_block)

    print(f"Wrote {REPORT_PATH}")
    print(f"Wrote {CSV_PATH}")
    print(f"Wrote {TRACKING_LOG_PATH}")
    print(f"Updated {MAIN_REPORT_PATH}")
    print(f"Verdict: {verdict.get('label')}")
    print(f"Structural similarity: {fmt_pct(structural.get('structural_similarity'))}")
    print(f"Live adherence: {fmt_pct(live.get('simple_alignment_score'))}")
    print(f"Live average gap: {fmt_pct(live.get('avg_abs_gap_pct'))}")
    print(f"Current gap: {fmt_pct(phase_gap_pct)}")
    print(f"Operational weight: {verdict.get('operational_weight', 0)}")
    print(f"Computational anchor: {computational_anchor.get('price')} ({computational_anchor.get('timestamp')})")
    print(f"Current public reference: {current_public_reference.get('price')} ({current_public_reference.get('timestamp')})")


if __name__ == "__main__":
    main()
