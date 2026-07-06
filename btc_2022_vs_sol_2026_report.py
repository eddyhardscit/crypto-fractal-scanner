import os
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

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

FRACTAL_CHART_FILE = "btc_2022_vs_sol_2026_fractal_chart.png"
PROJECTION_CHART_FILE = "btc_2022_vs_sol_2026_projection_chart.png"
CYCLE_CHART_FILE = "btc_2022_vs_sol_2026_cycle_chart.png"
CYCLE_BASE_CHART_FILE = "btc_2022_vs_sol_2026_cycle_base_chart.png"
CYCLE_BETA_CHART_FILE = "btc_2022_vs_sol_2026_cycle_beta_chart.png"
CYCLE_LOG_CHART_FILE = "btc_2022_vs_sol_2026_cycle_log_chart.png"
TRACKING_CHART_FILE = "btc_2022_vs_sol_2026_tracking_chart.png"

BTC_TICKER = "BTC-USD"
SOL_TICKER = "SOL-USD"

BTC_BOTTOM_SEARCH_START = "2022-11-01"
BTC_BOTTOM_SEARCH_END = "2023-01-31"

BTC_TOP_SEARCH_START = "2025-01-01"
BTC_TOP_SEARCH_END = "2025-12-31"

SOL_BOTTOM_SEARCH_START = "2026-06-01"

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
    s = f"{value:,.{decimals}f}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".")


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
    def clean(x):
        return str(x).replace("|", "\\|").replace("\n", " ")

    lines = []
    lines.append("| " + " | ".join(clean(h) for h in headers) + " |")
    lines.append("| " + " | ".join("---" for _ in headers) + " |")

    for row in rows:
        lines.append("| " + " | ".join(clean(cell) for cell in row) + " |")

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
        period = df.loc[pd.to_datetime(start):].copy()
    else:
        period = df.loc[pd.to_datetime(start):pd.to_datetime(end)].copy()

    if period.empty:
        period = df.tail(90).copy()

    low_date = period["Close"].idxmin()
    low_price = safe_float(period.loc[low_date, "Close"])
    return low_date, low_price


def find_high_anchor(df, start, end):
    if df.empty:
        return None, None

    period = df.loc[pd.to_datetime(start):pd.to_datetime(end)].copy()

    if period.empty:
        return None, None

    high_date = period["Close"].idxmax()
    high_price = safe_float(period.loc[high_date, "Close"])
    return high_date, high_price


def normalize_path(df, anchor_date, anchor_price):
    path = df[df.index >= anchor_date].copy()

    if path.empty or anchor_price is None or anchor_price <= 0:
        return pd.DataFrame()

    path["norm"] = path["Close"] / anchor_price * 100
    path["pct_from_anchor"] = (path["Close"] / anchor_price - 1) * 100
    return path


def to_clean_series(values):
    s = pd.Series(values).reset_index(drop=True)
    return pd.to_numeric(s, errors="coerce")


def correlation_similarity(a, b):
    a = to_clean_series(a)
    b = to_clean_series(b)
    valid = pd.concat([a, b], axis=1).dropna()

    if len(valid) < 5:
        return None

    x = valid.iloc[:, 0].values
    y = valid.iloc[:, 1].values

    if np.std(x) == 0 or np.std(y) == 0:
        return None

    corr = np.corrcoef(x, y)[0, 1]

    if np.isnan(corr):
        return None

    return max(0, min(100, (corr + 1) / 2 * 100))


def error_similarity(a, b, tolerance=0.45):
    a = to_clean_series(a)
    b = to_clean_series(b)
    valid = pd.concat([a, b], axis=1).dropna()

    if len(valid) < 5:
        return None

    diff = valid.iloc[:, 0].values - valid.iloc[:, 1].values
    rms = float(np.sqrt(np.mean(diff ** 2)))
    return max(0, min(100, 100 * (1 - rms / tolerance)))


def mean_abs_similarity(a, b, scale):
    a = to_clean_series(a)
    b = to_clean_series(b)
    valid = pd.concat([a, b], axis=1).dropna()

    if len(valid) < 5:
        return None

    mean_abs = float(np.mean(np.abs(valid.iloc[:, 0].values - valid.iloc[:, 1].values)))
    return max(0, min(100, 100 - mean_abs * scale))


def combine_scores(items):
    total_weight = 0
    total_score = 0

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
        text = "SOL e piu forte / piu avanti del BTC equivalente."
    elif gap_pct > 5:
        text = "SOL e leggermente piu forte del BTC equivalente."
    elif gap_pct < -15:
        text = "SOL e piu debole / piu indietro del BTC equivalente."
    elif gap_pct < -5:
        text = "SOL e leggermente piu debole del BTC equivalente."
    else:
        text = "SOL e abbastanza allineato al BTC equivalente."

    return gap_pct, text


def compute_similarity(btc_path, sol_path):
    compare_len = min(len(btc_path), len(sol_path))

    if compare_len < 15:
        return {
            "compare_len": compare_len,
            "price_similarity": None,
            "rsi_similarity": None,
            "ma_similarity": None,
            "total_similarity": None,
        }

    btc = btc_path.iloc[:compare_len].copy()
    sol = sol_path.iloc[:compare_len].copy()

    btc_log_norm = np.log(btc["norm"].reset_index(drop=True) / 100)
    sol_log_norm = np.log(sol["norm"].reset_index(drop=True) / 100)

    price_corr_sim = correlation_similarity(btc_log_norm, sol_log_norm)
    price_error_sim = error_similarity(btc_log_norm, sol_log_norm, tolerance=0.45)

    price_similarity = combine_scores(
        [
            (price_corr_sim, 0.65),
            (price_error_sim, 0.35),
        ]
    )

    rsi_similarity = mean_abs_similarity(
        btc["rsi_14"].reset_index(drop=True),
        sol["rsi_14"].reset_index(drop=True),
        scale=2.0,
    )

    ma_scores = []
    for ma in [20, 50, 100]:
        col = f"dist_ma_{ma}"
        if col in btc.columns and col in sol.columns:
            ma_scores.append(
                mean_abs_similarity(
                    btc[col].reset_index(drop=True),
                    sol[col].reset_index(drop=True),
                    scale=2.8,
                )
            )

    ma_similarity = combine_scores([(s, 1) for s in ma_scores])

    total_similarity = combine_scores(
        [
            (price_similarity, 0.60),
            (rsi_similarity, 0.25),
            (ma_similarity, 0.15),
        ]
    )

    return {
        "compare_len": compare_len,
        "price_similarity": price_similarity,
        "rsi_similarity": rsi_similarity,
        "ma_similarity": ma_similarity,
        "total_similarity": total_similarity,
    }


def direct_verdict(total_similarity, price_similarity, rsi_similarity, ma_similarity, phase_gap_pct):
    total = safe_float(total_similarity)
    price = safe_float(price_similarity)
    rsi_score = safe_float(rsi_similarity)
    ma_score = safe_float(ma_similarity)
    gap = safe_float(phase_gap_pct)

    reasons = []

    if total is None:
        return {
            "label": "DATI INSUFFICIENTI",
            "short": "Non ci sono ancora abbastanza dati per dire se SOL sta seguendo BTC 2022.",
            "action": "Aspetta altri dati.",
            "confidence": "n/d",
            "reasons": ["Dati insufficienti per calcolare una somiglianza affidabile."],
        }

    if price is not None:
        if price >= 75:
            reasons.append("La forma del prezzo e molto simile.")
        elif price >= 60:
            reasons.append("La forma del prezzo e abbastanza simile.")
        else:
            reasons.append("La forma del prezzo non combacia abbastanza.")

    if rsi_score is not None:
        if rsi_score >= 70:
            reasons.append("La forza RSI conferma abbastanza il paragone.")
        elif rsi_score >= 55:
            reasons.append("La forza RSI conferma solo parzialmente.")
        else:
            reasons.append("La forza RSI e piu debole del frattale BTC.")

    if ma_score is not None:
        if ma_score >= 70:
            reasons.append("La posizione rispetto alle medie mobili e coerente.")
        elif ma_score >= 55:
            reasons.append("Le medie mobili sono solo parzialmente coerenti.")
        else:
            reasons.append("Le medie mobili non confermano bene il frattale.")

    if gap is not None:
        if gap > 15:
            reasons.append("SOL e piu avanti o piu forte rispetto al BTC equivalente.")
        elif gap < -15:
            reasons.append("SOL e piu indietro o piu debole rispetto al BTC equivalente.")
        else:
            reasons.append("SOL e abbastanza in linea con il punto equivalente di BTC.")

    strong_price = price is not None and price >= 72
    decent_price = price is not None and price >= 60

    weak_internal = False
    if rsi_score is not None and rsi_score < 50:
        weak_internal = True
    if ma_score is not None and ma_score < 50:
        weak_internal = True

    if total >= 80 and strong_price and not weak_internal:
        label = "SI, LO STA SEGUENDO BENE"
        short = "Il frattale BTC 2022 e al momento uno scenario forte per SOL."
        action = "Le proiezioni valgono come scenario principale, finche SOL non perde i livelli di invalidazione."
        confidence = "ALTA"
    elif total >= 65 and decent_price:
        label = "PARZIALMENTE SI"
        short = "SOL sta seguendo abbastanza il frattale BTC 2022, ma non in modo perfetto."
        action = "Le proiezioni sono utili, ma vanno confermate con i prossimi livelli."
        confidence = "MEDIA"
    elif total >= 50:
        label = "SOLO DEBOLMENTE"
        short = "C'e una somiglianza, ma non basta per dire che SOL lo stia seguendo davvero."
        action = "Usalo come scenario secondario, non come guida principale."
        confidence = "BASSA"
    else:
        label = "NO, NON LO STA SEGUENDO BENE"
        short = "Il paragone con BTC 2022 e debole."
        action = "Le proiezioni sono poco affidabili finche la somiglianza non migliora."
        confidence = "DEBOLE"

    return {
        "label": label,
        "short": short,
        "action": action,
        "confidence": confidence,
        "reasons": reasons,
    }


def volatility_beta(btc_path, sol_path, compare_len):
    btc_ret = btc_path["log_return"].iloc[:compare_len].dropna()
    sol_ret = sol_path["log_return"].iloc[:compare_len].dropna()

    if len(btc_ret) < 10 or len(sol_ret) < 10:
        return 1.0

    btc_vol = float(btc_ret.std())
    sol_vol = float(sol_ret.std())

    if btc_vol <= 0:
        return 1.0

    ratio = sol_vol / btc_vol
    return max(0.60, min(2.00, ratio))


def projection_price(sol_current_price, relative_move, beta_ratio=1.0):
    if sol_current_price is None:
        return None

    relative_move = safe_float(relative_move)
    if relative_move is None or relative_move <= 0:
        return None

    beta_ratio = safe_float(beta_ratio) or 1.0
    return sol_current_price * np.exp(np.log(relative_move) * beta_ratio)


def projection_from_btc(btc_path, sol_current_price, sol_current_date, sol_elapsed_days, beta_ratio):
    rows = []

    if btc_path.empty or sol_current_price is None:
        return rows

    btc_current_idx = min(sol_elapsed_days, len(btc_path) - 1)
    btc_current_norm = safe_float(btc_path["norm"].iloc[btc_current_idx])

    if btc_current_norm is None or btc_current_norm <= 0:
        return rows

    for horizon in FORECAST_DAYS:
        future_idx = btc_current_idx + horizon

        if future_idx >= len(btc_path):
            continue

        btc_future_norm = safe_float(btc_path["norm"].iloc[future_idx])
        if btc_future_norm is None:
            continue

        sol_future_date = add_days(sol_current_date, horizon)
        future_slice = btc_path["norm"].iloc[btc_current_idx:future_idx + 1]
        relative_slice = future_slice / btc_current_norm

        btc_move_pct = (btc_future_norm / btc_current_norm - 1) * 100
        base_relative = btc_future_norm / btc_current_norm

        base_price = sol_current_price * base_relative
        beta_price = projection_price(sol_current_price, base_relative, beta_ratio)

        low_relative = safe_float(relative_slice.min())
        high_relative = safe_float(relative_slice.max())

        low_base_price = sol_current_price * low_relative
        high_base_price = sol_current_price * high_relative

        low_beta_price = projection_price(sol_current_price, low_relative, beta_ratio)
        high_beta_price = projection_price(sol_current_price, high_relative, beta_ratio)

        low_base_pct = (low_base_price / sol_current_price - 1) * 100
        high_base_pct = (high_base_price / sol_current_price - 1) * 100

        rows.append(
            {
                "horizon_days": horizon,
                "sol_current_date": fmt_date(sol_current_date),
                "sol_future_date": fmt_date(sol_future_date),
                "sol_future_date_it": fmt_date_it(sol_future_date),
                "btc_equivalent_future_date": str(btc_path.index[future_idx].date()),
                "btc_move_from_equivalent_today_pct": btc_move_pct,
                "sol_projection_base_price": base_price,
                "sol_projection_beta_price": beta_price,
                "sol_path_low_base_price": low_base_price,
                "sol_path_low_beta_price": low_beta_price,
                "sol_path_low_base_pct": low_base_pct,
                "sol_path_high_base_price": high_base_price,
                "sol_path_high_beta_price": high_beta_price,
                "sol_path_high_base_pct": high_base_pct,
            }
        )

    return rows


def stage_sequence_label(low_pct, high_pct, end_pct, low_offset, high_offset):
    low_pct = safe_float(low_pct)
    high_pct = safe_float(high_pct)
    end_pct = safe_float(end_pct)

    if low_pct is None or high_pct is None or end_pct is None:
        return "n/d"

    low_is_real = low_pct <= -3
    high_is_real = high_pct >= 3

    if low_is_real and high_is_real:
        if low_offset <= high_offset:
            return "Prima retest / debolezza, poi recupero."
        return "Prima spike, poi scarico."

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

    btc_current_idx = min(sol_elapsed_days, len(btc_path) - 1)
    btc_current_norm = safe_float(btc_path["norm"].iloc[btc_current_idx])

    if btc_current_norm is None or btc_current_norm <= 0:
        return rows

    for start_offset, end_offset, stage_name in STAGE_BUCKETS:
        start_idx = btc_current_idx + start_offset
        end_idx = btc_current_idx + end_offset

        if start_idx >= len(btc_path):
            continue
        if end_idx >= len(btc_path):
            end_idx = len(btc_path) - 1

        stage_slice = btc_path["norm"].iloc[start_idx:end_idx + 1]
        if stage_slice.empty:
            continue

        sol_stage_start_date = add_days(sol_current_date, start_offset)
        sol_stage_end_date = add_days(sol_current_date, end_offset)

        end_norm = safe_float(btc_path["norm"].iloc[end_idx])
        low_norm = safe_float(stage_slice.min())
        high_norm = safe_float(stage_slice.max())

        low_idx = stage_slice.idxmin()
        high_idx = stage_slice.idxmax()

        low_offset = int((low_idx - btc_path.index[btc_current_idx]).days)
        high_offset = int((high_idx - btc_path.index[btc_current_idx]).days)

        sol_low_date = add_days(sol_current_date, low_offset)
        sol_high_date = add_days(sol_current_date, high_offset)

        end_relative = end_norm / btc_current_norm
        low_relative = low_norm / btc_current_norm
        high_relative = high_norm / btc_current_norm

        end_pct = (end_relative - 1) * 100
        low_pct = (low_relative - 1) * 100
        high_pct = (high_relative - 1) * 100

        end_base_price = sol_current_price * end_relative
        end_beta_price = projection_price(sol_current_price, end_relative, beta_ratio)
        low_base_price = sol_current_price * low_relative
        high_base_price = sol_current_price * high_relative
        low_beta_price = projection_price(sol_current_price, low_relative, beta_ratio)
        high_beta_price = projection_price(sol_current_price, high_relative, beta_ratio)

        sequence = stage_sequence_label(low_pct, high_pct, end_pct, low_offset, high_offset)

        rows.append(
            {
                "stage": stage_name,
                "start_day": start_offset,
                "end_day": end_offset,
                "sol_stage_start_date": fmt_date(sol_stage_start_date),
                "sol_stage_start_date_it": fmt_date_it(sol_stage_start_date),
                "sol_stage_end_date": fmt_date(sol_stage_end_date),
                "sol_stage_end_date_it": fmt_date_it(sol_stage_end_date),
                "btc_end_date": str(btc_path.index[end_idx].date()),
                "btc_end_move_pct": end_pct,
                "btc_low_move_pct": low_pct,
                "btc_high_move_pct": high_pct,
                "low_day_offset": low_offset,
                "high_day_offset": high_offset,
                "sol_low_date": fmt_date(sol_low_date),
                "sol_low_date_it": fmt_date_it(sol_low_date),
                "sol_high_date": fmt_date(sol_high_date),
                "sol_high_date_it": fmt_date_it(sol_high_date),
                "sol_end_base_price": end_base_price,
                "sol_end_beta_price": end_beta_price,
                "sol_low_base_price": low_base_price,
                "sol_low_beta_price": low_beta_price,
                "sol_high_base_price": high_base_price,
                "sol_high_beta_price": high_beta_price,
                "sequence": sequence,
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
            "support_note": "Dati insufficienti.",
        }

    first_30 = [p for p in projections if p.get("horizon_days") in [7, 14, 30]]
    first_60 = [p for p in projections if p.get("horizon_days") in [30, 60]]

    highs_30 = [
        safe_float(p.get("sol_path_high_base_price"))
        for p in first_30
        if safe_float(p.get("sol_path_high_base_price")) is not None
    ]
    highs_60 = [
        safe_float(p.get("sol_path_high_base_price"))
        for p in first_60
        if safe_float(p.get("sol_path_high_base_price")) is not None
    ]
    lows_30 = [
        safe_float(p.get("sol_path_low_base_price"))
        for p in first_30
        if safe_float(p.get("sol_path_low_base_price")) is not None
    ]

    confirm_1 = max(highs_30) if highs_30 else sol_current_price * 1.08
    confirm_2 = max(highs_60) if highs_60 else sol_current_price * 1.15

    projected_low_30 = min(lows_30) if lows_30 else sol_current_price * 0.98

    # Invalidazione soft piu pratica:
    # prima guardo il minimo previsto dal frattale, ma pretendo anche un drawdown reale.
    # Cosi non basta una candela normale sotto il prezzo attuale per dire che il frattale e rovinato.
    soft_invalid = min(projected_low_30, sol_current_price * 0.95)

    # Evita che la soft invalidation venga calcolata troppo vicina al bottom assoluto.
    # La hard invalidation resta il bottom vero.
    if sol_anchor_price is not None:
        soft_invalid = max(soft_invalid, sol_anchor_price * 1.12)

    hard_invalid = sol_anchor_price

    if hard_invalid is not None and hard_invalid > sol_current_price:
        hard_invalid = sol_current_price * 0.90

    support_note = (
        "La prima zona bassa prevista nei prossimi 30 giorni va letta come area di attenzione. "
        "Per una lettura piu pratica, considero invalidazione soft solo sotto un drawdown reale "
        f"di circa 5% dal prezzo attuale ({fmt_price(soft_invalid)}). "
        "Se SOL perde anche il bottom usato come ancoraggio, il frattale BTC 2022 e praticamente invalidato."
    )

    return {
        "confirm_1": confirm_1,
        "confirm_2": confirm_2,
        "soft_invalid": soft_invalid,
        "hard_invalid": hard_invalid,
        "support_note": support_note,
    }


def current_phase(sol_current_price, key_levels, verdict):
    price = safe_float(sol_current_price)
    confirm_1 = safe_float(key_levels.get("confirm_1"))
    confirm_2 = safe_float(key_levels.get("confirm_2"))
    soft_invalid = safe_float(key_levels.get("soft_invalid"))
    hard_invalid = safe_float(key_levels.get("hard_invalid"))
    verdict_label = verdict.get("label", "")

    if price is None:
        return {"label": "DATI INSUFFICIENTI", "text": "Non posso classificare la fase attuale.", "risk": "n/d"}

    if "NO" in verdict_label:
        return {
            "label": "FRATTALE DEBOLE",
            "text": "Il paragone con BTC 2022 non e abbastanza forte. Le proiezioni valgono poco.",
            "risk": "ALTO",
        }

    if hard_invalid is not None and price <= hard_invalid:
        return {
            "label": "FRATTALE ROTTO",
            "text": "SOL e sotto o vicino al bottom usato. Il frattale BTC 2022 e praticamente invalidato.",
            "risk": "MOLTO ALTO",
        }

    if soft_invalid is not None and price <= soft_invalid:
        return {
            "label": "SOTTO PRESSIONE",
            "text": "SOL e nella zona in cui il frattale si indebolisce. Serve recupero veloce.",
            "risk": "ALTO",
        }

    if confirm_1 is not None and price < confirm_1:
        return {
            "label": "FASE ANTICIPATA",
            "text": "Il prezzo e ancora prima della conferma. Qui il potenziale e migliore, ma la certezza e bassa.",
            "risk": "MEDIO / ALTO",
        }

    if confirm_2 is not None and price < confirm_2:
        return {
            "label": "CONFERMA INIZIALE",
            "text": "SOL ha iniziato a confermare il frattale, ma non e ancora una conferma forte.",
            "risk": "MEDIO",
        }

    return {
        "label": "CONFERMA FORTE / ATTENZIONE A INSEGUIRE",
        "text": "Il frattale e piu confermato, ma una parte della mossa e gia stata fatta. Meglio gestire il rischio invece di inseguire a caso.",
        "risk": "MEDIO / RISCHIO INSEGUIMENTO",
    }


def build_operational_plan(sol_current_price, key_levels, verdict, phase):
    price = safe_float(sol_current_price)
    confirm_1 = safe_float(key_levels.get("confirm_1"))
    confirm_2 = safe_float(key_levels.get("confirm_2"))
    soft_invalid = safe_float(key_levels.get("soft_invalid"))
    hard_invalid = safe_float(key_levels.get("hard_invalid"))

    verdict_label = verdict.get("label", "")
    phase_label = phase.get("label", "")

    if price is None:
        summary = "Dati insufficienti per una lettura operativa."
        rows = [
            ["Spot anticipato", "NO", "Mancano dati sufficienti."],
            ["Aggiunta su conferma", "NO", "Mancano dati sufficienti."],
            ["Rischio inseguimento", "n/d", "Mancano dati sufficienti."],
        ]
        return summary, rows

    if "NO" in verdict_label or "ROTTO" in phase_label or "DEBOLE" in phase_label:
        summary = "Operativita prudente: il frattale non e abbastanza valido per usarlo come guida principale."
        rows = [
            ["Spot anticipato", "NO / molto prudente", "Il frattale BTC 2022 non conferma abbastanza."],
            ["Aggiunta su conferma", "Solo se migliora", f"Prima deve recuperare e superare {fmt_price(confirm_1)}."],
            ["Rischio inseguimento", "ALTO", "Comprare solo perche sale sarebbe poco giustificato dal frattale."],
            ["Invalidazione", fmt_price(hard_invalid), "Sotto questa zona il paragone e quasi rotto."],
        ]
        return summary, rows

    if "FASE ANTICIPATA" in phase_label:
        summary = "Fase anticipata: ingresso migliore come prezzo, ma certezza ancora bassa. Ha senso ragionare a tranche, non tutto insieme."
        rows = [
            ["Spot anticipato", "SI, ma a tranche", "La zona e ancora prima della conferma piena."],
            ["Aggiunta su conferma", "SI", f"Aggiunta sensata se rompe e tiene {fmt_price(confirm_1)}."],
            ["Seconda conferma", fmt_price(confirm_2), "Sopra questa zona il frattale diventa molto piu credibile."],
            ["Rischio inseguimento", "BASSO / MEDIO", "Non sei ancora troppo in ritardo, ma serve invalidazione chiara."],
            ["Invalidazione soft", fmt_price(soft_invalid), "Sotto questa zona il frattale si indebolisce."],
            ["Invalidazione forte", fmt_price(hard_invalid), "Sotto questa zona il frattale e quasi rotto."],
        ]
        return summary, rows

    if "CONFERMA INIZIALE" in phase_label:
        summary = "Conferma iniziale: il frattale sta migliorando, ma una parte della mossa e gia partita. Meglio evitare di comprare tutto in breakout."
        rows = [
            ["Spot anticipato", "GIA TARDIVO", "La parte migliore era prima della conferma."],
            ["Aggiunta su conferma", "SI, ma piccola", f"Possibile sopra {fmt_price(confirm_2)} o su retest pulito."],
            ["Rischio inseguimento", "MEDIO", "Comprare aggressivo ora significa pagare la conferma."],
            ["Gestione", "Tenere / aggiungere su pullback", "Meglio scalare che inseguire una candela forte."],
            ["Invalidazione soft", fmt_price(soft_invalid), "Se torna sotto, la conferma perde valore."],
            ["Invalidazione forte", fmt_price(hard_invalid), "Sotto questa zona il frattale e quasi rotto."],
        ]
        return summary, rows

    summary = "Conferma forte: il frattale e piu chiaro, ma il rischio principale diventa inseguire troppo tardi."
    rows = [
        ["Spot anticipato", "NO", "La fase anticipata e passata."],
        ["Aggiunta su conferma", "Solo su retest", "Meglio aspettare scarichi o consolidamenti."],
        ["Rischio inseguimento", "ALTO", "Piu aumenta la conferma, piu peggiora il rapporto rischio/rendimento."],
        ["Gestione", "Prendere profitto parziale / trailing", "Qui conta proteggere la mossa gia fatta."],
        ["Invalidazione soft", fmt_price(soft_invalid), "Sotto questa zona il frattale si indebolisce."],
        ["Invalidazione forte", fmt_price(hard_invalid), "Sotto questa zona il frattale e quasi rotto."],
    ]
    return summary, rows


def build_next_step_text(phase, stages):
    if not stages:
        return "Dati insufficienti per descrivere il prossimo step."

    first = stages[0]
    low = fmt_price(first.get("sol_low_base_price"))
    low_date = first.get("sol_low_date_it", "n/d")
    high = fmt_price(first.get("sol_high_base_price"))
    high_date = first.get("sol_high_date_it", "n/d")
    end_price = fmt_price(first.get("sol_end_base_price"))
    end_date = first.get("sol_stage_end_date_it", "n/d")
    sequence = first.get("sequence", "n/d")

    return (
        f"Prossimo step previsto dal frattale: **{sequence}** "
        f"Zona bassa stimata: **{low}** intorno al **{low_date}**. "
        f"Zona alta stimata: **{high}** intorno al **{high_date}**. "
        f"Fine step: circa **{end_price}** entro il **{end_date}**."
    )


def make_daily_projection_path(btc_path, sol_current_price, sol_current_date, sol_elapsed_days, beta_ratio, max_days=365):
    rows = []

    if btc_path.empty or sol_current_price is None:
        return pd.DataFrame()

    btc_current_idx = min(sol_elapsed_days, len(btc_path) - 1)
    btc_current_norm = safe_float(btc_path["norm"].iloc[btc_current_idx])

    if btc_current_norm is None or btc_current_norm <= 0:
        return pd.DataFrame()

    max_future_idx = min(len(btc_path) - 1, btc_current_idx + max_days)

    for idx in range(btc_current_idx, max_future_idx + 1):
        offset = idx - btc_current_idx
        btc_norm = safe_float(btc_path["norm"].iloc[idx])
        if btc_norm is None:
            continue

        relative = btc_norm / btc_current_norm
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
    if btc_top_date is None or btc_top_price is None:
        return {}, pd.DataFrame()

    if btc_path.empty or sol_current_price is None or sol_anchor_price is None:
        return {}, pd.DataFrame()

    btc_current_idx = min(int(sol_elapsed_days), len(btc_path) - 1)
    btc_top_idx = int((pd.to_datetime(btc_top_date) - pd.to_datetime(btc_anchor_date)).days)
    btc_top_idx = min(max(btc_top_idx, 0), len(btc_path) - 1)

    if btc_top_idx <= btc_current_idx:
        return {}, pd.DataFrame()

    btc_current_norm = safe_float(btc_path["norm"].iloc[btc_current_idx])
    btc_top_norm = safe_float(btc_path["norm"].iloc[btc_top_idx])

    if btc_current_norm is None or btc_current_norm <= 0 or btc_top_norm is None:
        return {}, pd.DataFrame()

    btc_bottom_to_top_mult = btc_top_price / btc_anchor_price
    btc_current_to_top_mult = btc_top_norm / btc_current_norm

    sol_cycle_top_date = add_days(sol_anchor_date, btc_top_idx)
    remaining_days = btc_top_idx - btc_current_idx

    target_from_bottom_base = sol_anchor_price * btc_bottom_to_top_mult
    target_from_bottom_beta = projection_price(sol_anchor_price, btc_bottom_to_top_mult, beta_ratio)
    target_from_current_base = sol_current_price * btc_current_to_top_mult
    target_from_current_beta = projection_price(sol_current_price, btc_current_to_top_mult, beta_ratio)

    rows = []
    for idx in range(btc_current_idx, btc_top_idx + 1):
        offset = idx - btc_current_idx
        btc_norm = safe_float(btc_path["norm"].iloc[idx])
        if btc_norm is None:
            continue

        relative = btc_norm / btc_current_norm
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

    cycle_max_base_price = None
    cycle_max_beta_price = None
    cycle_max_base_date = None
    cycle_max_beta_date = None

    if not cycle_daily.empty:
        base_idx = cycle_daily["base_price"].idxmax()
        beta_idx = cycle_daily["beta_price"].idxmax()
        cycle_max_base_price = safe_float(cycle_daily.loc[base_idx, "base_price"])
        cycle_max_beta_price = safe_float(cycle_daily.loc[beta_idx, "beta_price"])
        cycle_max_base_date = fmt_date(cycle_daily.loc[base_idx, "sol_date"])
        cycle_max_beta_date = fmt_date(cycle_daily.loc[beta_idx, "sol_date"])

    cycle = {
        "btc_top_date": str(pd.to_datetime(btc_top_date).date()),
        "btc_top_date_it": fmt_date_it(btc_top_date),
        "btc_top_price": btc_top_price,
        "btc_top_offset_days": btc_top_idx,
        "btc_bottom_to_top_mult": btc_bottom_to_top_mult,
        "btc_current_to_top_mult": btc_current_to_top_mult,
        "sol_cycle_top_date": fmt_date(sol_cycle_top_date),
        "sol_cycle_top_date_it": fmt_date_it(sol_cycle_top_date),
        "cycle_remaining_days": remaining_days,
        "target_from_bottom_base": target_from_bottom_base,
        "target_from_bottom_beta": target_from_bottom_beta,
        "target_from_current_base": target_from_current_base,
        "target_from_current_beta": target_from_current_beta,
        "cycle_max_base_price": cycle_max_base_price,
        "cycle_max_beta_price": cycle_max_beta_price,
        "cycle_max_base_date": cycle_max_base_date,
        "cycle_max_beta_date": cycle_max_beta_date,
        "cycle_max_base_date_it": fmt_date_it(cycle_max_base_date),
        "cycle_max_beta_date_it": fmt_date_it(cycle_max_beta_date),
    }

    return cycle, cycle_daily


def update_tracking_log(summary_dict):
    tracking_columns = [
        "tracking_date",
        "generated_at_utc",
        "sol_current_price",
        "sol_elapsed_days",
        "btc_equivalent_date",
        "price_similarity",
        "rsi_similarity",
        "ma_similarity",
        "total_similarity",
        "phase_gap_pct",
        "verdict",
        "verdict_confidence",
        "phase_label",
        "phase_risk",
        "confirm_1",
        "confirm_2",
        "soft_invalid",
        "hard_invalid",
        "cycle_max_base_price",
        "cycle_max_beta_price",
    ]

    row = {
        "tracking_date": summary_dict.get("sol_current_date"),
        "generated_at_utc": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
        "sol_current_price": summary_dict.get("sol_current_price"),
        "sol_elapsed_days": summary_dict.get("sol_elapsed_days"),
        "btc_equivalent_date": summary_dict.get("btc_equivalent_date"),
        "price_similarity": summary_dict.get("price_similarity"),
        "rsi_similarity": summary_dict.get("rsi_similarity"),
        "ma_similarity": summary_dict.get("ma_similarity"),
        "total_similarity": summary_dict.get("total_similarity"),
        "phase_gap_pct": summary_dict.get("phase_gap_pct"),
        "verdict": summary_dict.get("verdict"),
        "verdict_confidence": summary_dict.get("verdict_confidence"),
        "phase_label": summary_dict.get("phase_label"),
        "phase_risk": summary_dict.get("phase_risk"),
        "confirm_1": summary_dict.get("confirm_1"),
        "confirm_2": summary_dict.get("confirm_2"),
        "soft_invalid": summary_dict.get("soft_invalid"),
        "hard_invalid": summary_dict.get("hard_invalid"),
        "cycle_max_base_price": summary_dict.get("cycle_max_base_price"),
        "cycle_max_beta_price": summary_dict.get("cycle_max_beta_price"),
    }

    if os.path.exists(TRACKING_LOG_PATH):
        try:
            df = pd.read_csv(TRACKING_LOG_PATH)
        except Exception:
            df = pd.DataFrame(columns=tracking_columns)
    else:
        df = pd.DataFrame(columns=tracking_columns)

    for col in tracking_columns:
        if col not in df.columns:
            df[col] = np.nan

    tracking_date = row.get("tracking_date")
    if tracking_date is not None:
        df = df[df["tracking_date"].astype(str) != str(tracking_date)]

    df = pd.concat([df, pd.DataFrame([row])], ignore_index=True)
    df = df[tracking_columns]
    df["tracking_date_sort"] = pd.to_datetime(df["tracking_date"], errors="coerce")
    df = df.sort_values("tracking_date_sort").drop(columns=["tracking_date_sort"])
    df.to_csv(TRACKING_LOG_PATH, index=False)
    return df


def build_tracking_status(tracking_df, summary_dict):
    if tracking_df is None or tracking_df.empty or len(tracking_df) < 2:
        return {
            "label": "STORICO INIZIALE",
            "text": "Ho iniziato ora a registrare lo storico. Da domani potro dire se il frattale migliora o peggiora.",
            "delta_similarity": None,
            "delta_price": None,
        }

    df = tracking_df.copy()
    df["tracking_date_dt"] = pd.to_datetime(df["tracking_date"], errors="coerce")
    df = df.dropna(subset=["tracking_date_dt"]).sort_values("tracking_date_dt")

    if len(df) < 2:
        return {
            "label": "STORICO INIZIALE",
            "text": "Storico ancora troppo corto per valutare il trend.",
            "delta_similarity": None,
            "delta_price": None,
        }

    last = df.iloc[-1]
    prev = df.iloc[-2]

    last_sim = safe_float(last.get("total_similarity"))
    prev_sim = safe_float(prev.get("total_similarity"))
    last_price = safe_float(last.get("sol_current_price"))
    prev_price = safe_float(prev.get("sol_current_price"))

    delta_sim = None if last_sim is None or prev_sim is None else last_sim - prev_sim
    delta_price = None if last_price is None or prev_price is None else last_price - prev_price

    if delta_sim is None:
        label = "TREND NON CALCOLABILE"
        text = "Non posso confrontare la somiglianza con ieri."
    elif delta_sim >= 3:
        label = "FRATTALE IN MIGLIORAMENTO"
        text = f"La somiglianza totale e salita di {fmt_pct(delta_sim)} rispetto alla rilevazione precedente."
    elif delta_sim <= -3:
        label = "FRATTALE IN PEGGIORAMENTO"
        text = f"La somiglianza totale e scesa di {fmt_pct(delta_sim)} rispetto alla rilevazione precedente."
    else:
        label = "FRATTALE STABILE"
        text = f"La somiglianza totale e quasi stabile: variazione {fmt_pct(delta_sim)} rispetto alla rilevazione precedente."

    return {
        "label": label,
        "text": text,
        "delta_similarity": delta_sim,
        "delta_price": delta_price,
    }


def build_projection_table(projections):
    if not projections:
        return "Dati insufficienti per la proiezione."

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
                fmt_pct(p["sol_path_low_base_pct"]),
                fmt_price(p["sol_path_high_base_price"]),
                fmt_pct(p["sol_path_high_base_pct"]),
            ]
        )

    return md_table(
        [
            "Orizzonte",
            "Data SOL prevista",
            "Data BTC equivalente",
            "BTC fece",
            "SOL base",
            "SOL beta",
            "Min percorso",
            "Min %",
            "Max percorso",
            "Max %",
        ],
        rows,
    )


def build_stage_table(stages):
    if not stages:
        return "Dati insufficienti per costruire gli step."

    rows = []
    for s in stages:
        rows.append(
            [
                s["stage"],
                f"{s['sol_stage_start_date_it']} -> {s['sol_stage_end_date_it']}",
                f"{s['start_day']}-{s['end_day']} giorni",
                s["btc_end_date"],
                fmt_pct(s["btc_end_move_pct"]),
                fmt_price(s["sol_end_base_price"]),
                fmt_price(s["sol_end_beta_price"]),
                f"{fmt_price(s['sol_low_base_price'])} ({s['sol_low_date_it']})",
                f"{fmt_price(s['sol_high_base_price'])} ({s['sol_high_date_it']})",
                s["sequence"],
            ]
        )

    return md_table(
        [
            "Step",
            "Date SOL previste",
            "Periodo",
            "BTC data equiv.",
            "BTC fine step",
            "SOL fine base",
            "SOL fine beta",
            "Zona bassa + data",
            "Zona alta + data",
            "Lettura",
        ],
        rows,
    )


def build_cycle_table(cycle):
    if not cycle:
        return "Dati insufficienti per la proiezione ciclo fino al top BTC 2025."

    return md_table(
        ["Voce", "Valore", "Lettura"],
        [
            ["Top BTC 2025 usato", f"{cycle.get('btc_top_date_it')} - {fmt_price(cycle.get('btc_top_price'))}", "Massimo close BTC nella finestra 2025."],
            ["Moltiplicatore BTC bottom -> top", f"{fmt_number(cycle.get('btc_bottom_to_top_mult'), 2)}x", "Quanto BTC ha fatto dal bottom 2022 al top 2025."],
            ["Data SOL equivalente del top", cycle.get("sol_cycle_top_date_it"), "Quando cadrebbe il top se SOL seguisse gli stessi tempi."],
            ["Target ciclo base dal bottom SOL", fmt_price(cycle.get("target_from_bottom_base")), "Proiezione pulita bottom-to-top."],
            ["Target ciclo beta dal bottom SOL", fmt_price(cycle.get("target_from_bottom_beta")), "Scenario aggressivo, amplificato dalla volatilita SOL."],
            ["Target ciclo base da oggi", fmt_price(cycle.get("target_from_current_base")), "Proiezione da prezzo attuale al top equivalente."],
            ["Target ciclo beta da oggi", fmt_price(cycle.get("target_from_current_beta")), "Scenario molto aggressivo da prezzo attuale."],
            ["Massimo percorso base", f"{fmt_price(cycle.get('cycle_max_base_price'))} ({cycle.get('cycle_max_base_date_it')})", "Massimo base lungo tutto il percorso fino al top."],
            ["Massimo percorso beta", f"{fmt_price(cycle.get('cycle_max_beta_price'))} ({cycle.get('cycle_max_beta_date_it')})", "Massimo aggressivo lungo tutto il percorso."],
        ],
    )


def build_summary_rows(
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
    similarity,
    beta_ratio,
):
    return [
        ["BTC bottom usato", str(btc_anchor_date.date()), fmt_price(btc_anchor_price)],
        ["SOL bottom usato", str(sol_anchor_date.date()), fmt_price(sol_anchor_price)],
        ["Ultima data SOL usata", fmt_date_it(sol_current_date), "-"],
        ["Prezzo SOL attuale", "-", fmt_price(sol_current_price)],
        ["Giorni SOL dal bottom", "-", sol_elapsed_days],
        ["Data BTC equivalente", str(btc_equiv_date.date()), "-"],
        ["BTC normalizzato al giorno equivalente", "-", fmt_number(btc_norm_equiv, 2)],
        ["SOL normalizzato oggi", "-", fmt_number(sol_norm_now, 2)],
        ["Gap SOL vs BTC equivalente", "-", fmt_pct(phase_gap_pct)],
        ["Lettura fase", "-", phase_text],
        ["Giorni confrontati", "-", similarity.get("compare_len")],
        ["Somiglianza prezzo", "-", fmt_pct(similarity.get("price_similarity"))],
        ["Somiglianza RSI", "-", fmt_pct(similarity.get("rsi_similarity"))],
        ["Somiglianza medie", "-", fmt_pct(similarity.get("ma_similarity"))],
        ["Somiglianza totale", "-", fmt_pct(similarity.get("total_similarity"))],
        ["Qualita frattale", "-", quality_label(similarity.get("total_similarity"))],
        ["Beta volatilita SOL/BTC", "-", fmt_number(beta_ratio, 2)],
    ]


def generate_fractal_chart(btc_path, sol_path, sol_elapsed_days):
    if not CHARTS_AVAILABLE:
        return False

    try:
        if btc_path.empty or sol_path.empty:
            return False

        sol_elapsed_days = int(sol_elapsed_days)
        future_days = 365
        chart_end_idx = min(len(btc_path) - 1, sol_elapsed_days + future_days)

        btc_chart = btc_path.iloc[:chart_end_idx + 1].copy()
        btc_x = np.arange(len(btc_chart))
        btc_y = btc_chart["norm"].values

        sol_actual = sol_path.copy()
        sol_x = np.arange(len(sol_actual))
        sol_y = sol_actual["norm"].values

        btc_current_idx = min(sol_elapsed_days, len(btc_path) - 1)
        btc_current_norm = safe_float(btc_path["norm"].iloc[btc_current_idx])
        sol_current_norm = safe_float(sol_path["norm"].iloc[-1])

        projection_x = []
        projection_y = []

        if btc_current_norm is not None and btc_current_norm > 0 and sol_current_norm is not None:
            for idx in range(btc_current_idx, chart_end_idx + 1):
                btc_norm = safe_float(btc_path["norm"].iloc[idx])
                if btc_norm is None:
                    continue
                projection_x.append(idx)
                projection_y.append(sol_current_norm * (btc_norm / btc_current_norm))

        fig, ax = plt.subplots(figsize=(12, 6))
        ax.plot(btc_x, btc_y, label="BTC dal bottom nov 2022")
        ax.plot(sol_x, sol_y, label="SOL dal bottom giu 2026")
        ax.plot(projection_x, projection_y, linestyle="--", label="Proiezione SOL 365g se segue BTC")
        ax.axvline(sol_elapsed_days, linestyle=":", alpha=0.8, label="Oggi SOL")

        if sol_current_norm is not None:
            ax.scatter([sol_elapsed_days], [sol_current_norm], s=55, zorder=5)
            ax.annotate("Oggi SOL", xy=(sol_elapsed_days, sol_current_norm), xytext=(8, 10), textcoords="offset points", fontsize=9)

        for day in CHART_LABEL_DAYS:
            idx = btc_current_idx + day
            if idx > chart_end_idx or btc_current_norm is None or btc_current_norm <= 0 or sol_current_norm is None:
                continue
            btc_norm = safe_float(btc_path["norm"].iloc[idx])
            if btc_norm is None:
                continue
            y = sol_current_norm * (btc_norm / btc_current_norm)
            ax.scatter([idx], [y], s=28, zorder=5)
            ax.annotate(f"+{day}g", xy=(idx, y), xytext=(5, 7), textcoords="offset points", fontsize=8)

        ax.set_title("Frattale sovrapposto: BTC 2022 vs SOL 2026")
        ax.set_xlabel("Giorni dal bottom")
        ax.set_ylabel("Prezzo normalizzato a 100 dal bottom")
        ax.grid(True, alpha=0.3)
        ax.legend()
        fig.tight_layout()
        fig.savefig(FRACTAL_CHART_PATH, dpi=160, bbox_inches="tight")
        plt.close(fig)
        return True
    except Exception as e:
        print(f"Could not generate fractal chart: {e}")
        return False


def generate_projection_chart(sol_path, projection_daily, key_levels, projections):
    if not CHARTS_AVAILABLE:
        return False

    try:
        if sol_path.empty or projection_daily.empty:
            return False

        fig, ax = plt.subplots(figsize=(14, 8))

        ax.plot(
            sol_path.index,
            sol_path["Close"],
            linewidth=2,
            label="SOL storico dal bottom",
        )

        ax.plot(
            projection_daily["sol_date"],
            projection_daily["base_price"],
            linestyle="--",
            linewidth=2,
            label="Proiezione SOL base",
        )

        ax.plot(
            projection_daily["sol_date"],
            projection_daily["beta_price"],
            linestyle=":",
            linewidth=1.8,
            label="Proiezione SOL beta",
        )

        sol_current_date = sol_path.index[-1]
        sol_current_price = safe_float(sol_path["Close"].iloc[-1])

        if sol_current_price is not None:
            ax.axvline(sol_current_date, linestyle=":", alpha=0.75)
            ax.scatter([sol_current_date], [sol_current_price], s=60, zorder=5)

            ax.annotate(
                f"Oggi\\n{fmt_price(sol_current_price)}",
                xy=(sol_current_date, sol_current_price),
                xytext=(10, 14),
                textcoords="offset points",
                fontsize=9,
                bbox=dict(boxstyle="round,pad=0.25", fc="white", alpha=0.85),
            )

        # Etichette target solo sui punti piu utili e con offset alternato.
        label_offsets = {
            7: (10, 18),
            30: (10, -26),
            60: (10, 18),
            120: (10, -26),
            365: (10, 18),
        }

        for p in projections:
            horizon = p.get("horizon_days")

            if horizon not in CHART_LABEL_DAYS:
                continue

            date_value = pd.to_datetime(p.get("sol_future_date"))
            price_value = safe_float(p.get("sol_projection_base_price"))

            if price_value is None:
                continue

            ax.scatter([date_value], [price_value], s=35, zorder=5)
            dx, dy = label_offsets.get(horizon, (10, 10))

            ax.annotate(
                f"{horizon}g\\n{fmt_price(price_value)}",
                xy=(date_value, price_value),
                xytext=(dx, dy),
                textcoords="offset points",
                fontsize=8,
                bbox=dict(boxstyle="round,pad=0.20", fc="white", alpha=0.80),
            )

        # Livelli chiave: sul margine destro, non sopra le linee.
        level_specs = [
            ("Prima conferma", key_levels.get("confirm_1"), 16),
            ("Seconda conferma", key_levels.get("confirm_2"), 0),
            ("Invalidazione soft", key_levels.get("soft_invalid"), -16),
            ("Invalidazione forte", key_levels.get("hard_invalid"), -32),
        ]

        for label, value, y_offset in level_specs:
            value = safe_float(value)

            if value is None:
                continue

            ax.axhline(value, linestyle="--", alpha=0.35)

            ax.annotate(
                f"{label}: {fmt_price(value)}",
                xy=(1.005, value),
                xycoords=("axes fraction", "data"),
                xytext=(4, y_offset),
                textcoords="offset points",
                ha="left",
                va="center",
                fontsize=8,
                bbox=dict(boxstyle="round,pad=0.20", fc="white", alpha=0.85),
                annotation_clip=False,
            )

        # Piu respiro a destra per leggere bene le etichette.
        last_proj_date = pd.to_datetime(projection_daily["sol_date"]).max()
        left_date = sol_path.index.min() - pd.Timedelta(days=5)
        right_date = last_proj_date + pd.Timedelta(days=25)
        ax.set_xlim(left_date, right_date)

        ax.margins(y=0.12)
        ax.set_title("Proiezione SOL in dollari se segue il frattale BTC 2022")
        ax.set_xlabel("Data")
        ax.set_ylabel("Prezzo SOL")
        ax.grid(True, alpha=0.3)
        ax.legend(loc="upper left")

        fig.autofmt_xdate()
        fig.tight_layout()
        fig.savefig(PROJECTION_CHART_PATH, dpi=180, bbox_inches="tight")
        plt.close(fig)

        return True

    except Exception as e:
        print(f"Could not generate projection chart: {e}")
        return False


def annotate_last_and_max(ax, x_dates, y_values, max_date, max_price, max_label):
    try:
        if len(x_dates) == 0 or len(y_values) == 0:
            return

        last_date = pd.to_datetime(x_dates.iloc[-1] if hasattr(x_dates, "iloc") else x_dates[-1])
        last_price = safe_float(y_values.iloc[-1] if hasattr(y_values, "iloc") else y_values[-1])

        if last_price is not None:
            ax.scatter([last_date], [last_price], s=45, zorder=5)
            ax.annotate(
                f"Fine percorso\n{fmt_price(last_price)}",
                xy=(last_date, last_price),
                xytext=(8, -18),
                textcoords="offset points",
                fontsize=8,
                bbox=dict(boxstyle="round,pad=0.20", fc="white", alpha=0.80),
            )

        max_price = safe_float(max_price)

        if max_price is not None and max_date is not None:
            max_date = pd.to_datetime(max_date)
            ax.scatter([max_date], [max_price], s=55, zorder=6)
            ax.annotate(
                f"{max_label}\n{fmt_price(max_price)}",
                xy=(max_date, max_price),
                xytext=(8, 10),
                textcoords="offset points",
                fontsize=8,
                bbox=dict(boxstyle="round,pad=0.20", fc="white", alpha=0.80),
            )
    except Exception:
        return


def generate_single_cycle_chart(
    sol_path,
    cycle_daily,
    cycle,
    output_path,
    mode="base",
    log_scale=False,
):
    if sol_path.empty or cycle_daily.empty or not cycle:
        return False

    fig, ax = plt.subplots(figsize=(14, 8))

    sol_current_date = sol_path.index[-1]
    sol_current_price = safe_float(sol_path["Close"].iloc[-1])

    if mode == "base":
        ax.plot(sol_path.index, sol_path["Close"], linewidth=2, label="SOL reale dal bottom")
        ax.plot(
            cycle_daily["sol_date"],
            cycle_daily["base_price"],
            linestyle="--",
            linewidth=2,
            label="Scenario ciclo BASE",
        )

        max_date = cycle.get("cycle_max_base_date")
        max_price = cycle.get("cycle_max_base_price")
        max_label = "Max base"
        title = "Ciclo SOL base fino al top equivalente BTC 2025"

        annotate_last_and_max(
            ax=ax,
            x_dates=cycle_daily["sol_date"],
            y_values=cycle_daily["base_price"],
            max_date=max_date,
            max_price=max_price,
            max_label=max_label,
        )

    elif mode == "beta":
        ax.plot(sol_path.index, sol_path["Close"], linewidth=2, label="SOL reale dal bottom")
        ax.plot(
            cycle_daily["sol_date"],
            cycle_daily["beta_price"],
            linestyle=":",
            linewidth=2,
            label="Scenario ciclo BETA aggressivo",
        )

        max_date = cycle.get("cycle_max_beta_date")
        max_price = cycle.get("cycle_max_beta_price")
        max_label = "Max beta"
        title = "Ciclo SOL beta aggressivo fino al top equivalente BTC 2025"

        annotate_last_and_max(
            ax=ax,
            x_dates=cycle_daily["sol_date"],
            y_values=cycle_daily["beta_price"],
            max_date=max_date,
            max_price=max_price,
            max_label=max_label,
        )

    else:
        ax.plot(sol_path.index, sol_path["Close"], linewidth=2, label="SOL reale dal bottom")
        ax.plot(
            cycle_daily["sol_date"],
            cycle_daily["base_price"],
            linestyle="--",
            linewidth=1.8,
            label="Scenario ciclo BASE",
        )
        ax.plot(
            cycle_daily["sol_date"],
            cycle_daily["beta_price"],
            linestyle=":",
            linewidth=1.7,
            label="Scenario ciclo BETA aggressivo",
        )

        title = "Ciclo SOL base + beta in scala logaritmica" if log_scale else "Ciclo SOL base + beta fino al top BTC 2025"

    if sol_current_price is not None:
        ax.axvline(sol_current_date, linestyle=":", alpha=0.75)
        ax.scatter([sol_current_date], [sol_current_price], s=55, zorder=6)
        ax.annotate(
            f"Oggi\n{fmt_price(sol_current_price)}",
            xy=(sol_current_date, sol_current_price),
            xytext=(8, 10),
            textcoords="offset points",
            fontsize=8,
            bbox=dict(boxstyle="round,pad=0.20", fc="white", alpha=0.80),
        )

    # Marker annuali solo sul percorso base, per non sporcare troppo il grafico.
    if mode in ["base", "log"]:
        for year in [2027, 2028, 2029]:
            year_rows = cycle_daily[pd.to_datetime(cycle_daily["sol_date"]).dt.year == year]
            if year_rows.empty:
                continue

            row = year_rows.iloc[0]
            date_value = pd.to_datetime(row["sol_date"])
            price_value = safe_float(row["base_price"])

            if price_value is None:
                continue

            ax.scatter([date_value], [price_value], s=25, zorder=5)
            ax.annotate(
                f"{year}\n{fmt_price(price_value)}",
                xy=(date_value, price_value),
                xytext=(5, 7),
                textcoords="offset points",
                fontsize=7,
                bbox=dict(boxstyle="round,pad=0.18", fc="white", alpha=0.75),
            )

    if log_scale:
        ax.set_yscale("log")
        ax.set_ylabel("Prezzo SOL - scala log")
    else:
        ax.set_ylabel("Prezzo SOL")

    ax.set_title(title)
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
        if sol_path.empty or cycle_daily.empty or not cycle:
            return False

        base_ok = generate_single_cycle_chart(
            sol_path=sol_path,
            cycle_daily=cycle_daily,
            cycle=cycle,
            output_path=CYCLE_BASE_CHART_PATH,
            mode="base",
            log_scale=False,
        )

        beta_ok = generate_single_cycle_chart(
            sol_path=sol_path,
            cycle_daily=cycle_daily,
            cycle=cycle,
            output_path=CYCLE_BETA_CHART_PATH,
            mode="beta",
            log_scale=False,
        )

        log_ok = generate_single_cycle_chart(
            sol_path=sol_path,
            cycle_daily=cycle_daily,
            cycle=cycle,
            output_path=CYCLE_LOG_CHART_PATH,
            mode="log",
            log_scale=True,
        )

        # Mantengo anche il vecchio file combinato per compatibilita con link gia esistenti.
        legacy_ok = generate_single_cycle_chart(
            sol_path=sol_path,
            cycle_daily=cycle_daily,
            cycle=cycle,
            output_path=CYCLE_CHART_PATH,
            mode="log",
            log_scale=False,
        )

        return bool(base_ok or beta_ok or log_ok or legacy_ok)
    except Exception as e:
        print(f"Could not generate cycle charts: {e}")
        return False


def generate_tracking_chart(tracking_df):
    if not CHARTS_AVAILABLE:
        return False

    try:
        if tracking_df is None or tracking_df.empty or len(tracking_df) < 2:
            return False

        df = tracking_df.copy()
        df["tracking_date_dt"] = pd.to_datetime(df["tracking_date"], errors="coerce")
        df["total_similarity_num"] = pd.to_numeric(df["total_similarity"], errors="coerce")
        df["sol_current_price_num"] = pd.to_numeric(df["sol_current_price"], errors="coerce")
        df = df.dropna(subset=["tracking_date_dt", "total_similarity_num"])

        if len(df) < 2:
            return False

        fig, ax = plt.subplots(figsize=(12, 5))
        ax.plot(df["tracking_date_dt"], df["total_similarity_num"], marker="o", label="Somiglianza totale")
        ax.axhline(65, linestyle="--", alpha=0.35)
        ax.axhline(80, linestyle="--", alpha=0.35)
        ax.set_title("Tracking giornaliero frattale BTC 2022 vs SOL 2026")
        ax.set_xlabel("Data")
        ax.set_ylabel("Somiglianza totale %")
        ax.grid(True, alpha=0.3)
        ax.legend()
        fig.autofmt_xdate()
        fig.tight_layout()
        fig.savefig(TRACKING_CHART_PATH, dpi=160, bbox_inches="tight")
        plt.close(fig)
        return True
    except Exception as e:
        print(f"Could not generate tracking chart: {e}")
        return False


def build_chart_block(fractal_chart_ok, projection_chart_ok, cycle_chart_ok, tracking_chart_ok):
    lines = ["## Grafici", ""]

    if fractal_chart_ok:
        lines += [
            "### Grafico 1 - Frattale sovrapposto BTC 2022 vs SOL 2026",
            "",
            "Questo grafico normalizza entrambi i prezzi a 100 dal rispettivo bottom. I marker +7g, +30g, +60g, ecc. indicano dove andrebbe SOL se continuasse a seguire BTC.",
            "",
            f"![Frattale BTC 2022 vs SOL 2026]({FRACTAL_CHART_FILE})",
            "",
        ]
    else:
        lines += ["Grafico frattale non generato. Controlla che `matplotlib` sia installato.", ""]

    if projection_chart_ok:
        lines += [
            "### Grafico 2 - Proiezione SOL in dollari a 365 giorni",
            "",
            "Questo grafico mostra SOL storico, il punto di oggi, i livelli chiave e la proiezione futura in dollari. Le etichette sono volutamente ridotte per non sovrapporsi.",
            "",
            f"![Proiezione SOL BTC 2022]({PROJECTION_CHART_FILE})",
            "",
        ]
    else:
        lines += ["Grafico proiezione non generato. Controlla che `matplotlib` sia installato.", ""]

    if cycle_chart_ok:
        lines += [
            "### Grafico 3 - Ciclo BASE fino al top BTC 2025",
            "",
            "Questo e il grafico principale: mostra SOL reale e lo scenario base, senza farsi schiacciare dalla beta aggressiva.",
            "",
            f"![Ciclo base SOL BTC 2025]({CYCLE_BASE_CHART_FILE})",
            "",
            "### Grafico 4 - Ciclo BASE + BETA in scala logaritmica",
            "",
            "Questo serve per vedere insieme scenario base e aggressivo senza perdere la leggibilita della parte iniziale.",
            "",
            f"![Ciclo log SOL BTC 2025]({CYCLE_LOG_CHART_FILE})",
            "",
            "### Grafico 5 - Ciclo BETA aggressivo separato",
            "",
            "Questo e lo scenario estremo/speculativo. Va guardato separato, non come target principale.",
            "",
            f"![Ciclo beta SOL BTC 2025]({CYCLE_BETA_CHART_FILE})",
            "",
        ]

    if tracking_chart_ok:
        lines += [
            "### Grafico 6 - Tracking giornaliero somiglianza",
            "",
            "Questo grafico mostra se il frattale sta migliorando o peggiorando giorno dopo giorno.",
            "",
            f"![Tracking frattale BTC SOL]({TRACKING_CHART_FILE})",
            "",
        ]

    return "\n".join(lines)


def build_operational_block(operational_summary, operational_rows):
    return "\n".join(
        [
            "## Lettura operativa",
            "",
            operational_summary,
            "",
            md_table(["Voce", "Risposta", "Perche"], operational_rows),
        ]
    )


def build_verdict_block(verdict, key_levels, phase, next_step_text):
    reasons = verdict.get("reasons", [])
    reason_lines = [f"- {r}" for r in reasons] if reasons else ["- Dati insufficienti."]

    lines = []
    lines.append("## Verdetto diretto")
    lines.append("")
    lines.append("**SOL sta seguendo BTC 2022?**")
    lines.append("")
    lines.append(f"### {verdict['label']}")
    lines.append("")
    lines.append(f"**Sintesi:** {verdict['short']}")
    lines.append("")
    lines.append(f"**Fase attuale:** {phase['label']}")
    lines.append("")
    lines.append(f"**Lettura fase:** {phase['text']}")
    lines.append("")
    lines.append(f"**Rischio fase:** {phase['risk']}")
    lines.append("")
    lines.append(f"**Prossimo step:** {next_step_text}")
    lines.append("")
    lines.append(f"**Cosa fare con questa informazione:** {verdict['action']}")
    lines.append("")
    lines.append(f"**Affidabilita del frattale:** {verdict['confidence']}")
    lines.append("")
    lines.append("### Perche")
    lines.append("")
    lines.extend(reason_lines)
    lines.append("")
    lines.append("### Livelli pratici")
    lines.append("")
    lines.append(
        md_table(
            ["Livello", "Prezzo", "Significato"],
            [
                ["Prima conferma", fmt_price(key_levels.get("confirm_1")), "Se SOL rompe questa zona, il frattale BTC 2022 migliora."],
                ["Seconda conferma", fmt_price(key_levels.get("confirm_2")), "Se rompe anche questa, lo scenario rialzista diventa piu credibile."],
                ["Invalidazione soft", fmt_price(key_levels.get("soft_invalid")), "Se perde questa zona, il frattale si indebolisce."],
                ["Invalidazione forte", fmt_price(key_levels.get("hard_invalid")), "Se perde il bottom usato, il paragone con BTC 2022 e quasi rotto."],
            ],
        )
    )
    lines.append("")
    lines.append(key_levels.get("support_note", ""))
    return "\n".join(lines)


def build_tracking_block(tracking_status, tracking_df):
    if tracking_df is None or tracking_df.empty:
        rows = []
    else:
        df = tracking_df.copy().tail(7)
        rows = []
        for _, r in df.iterrows():
            rows.append(
                [
                    r.get("tracking_date", "n/d"),
                    fmt_price(r.get("sol_current_price")),
                    fmt_pct(r.get("total_similarity")),
                    r.get("phase_label", "n/d"),
                    r.get("verdict", "n/d"),
                ]
            )

    lines = []
    lines.append("## Tracking giornaliero del frattale")
    lines.append("")
    lines.append(f"**Stato tracking:** {tracking_status.get('label')}")
    lines.append("")
    lines.append(tracking_status.get("text", ""))
    lines.append("")

    if rows:
        lines.append(md_table(["Data", "Prezzo SOL", "Somiglianza", "Fase", "Verdetto"], rows))
    else:
        lines.append("Storico non ancora disponibile.")

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
    similarity,
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
    tracking_status,
    tracking_df,
    fractal_chart_ok,
    projection_chart_ok,
    cycle_chart_ok,
    tracking_chart_ok,
):
    rome_now = datetime.now(ZoneInfo("Europe/Rome")).strftime("%Y-%m-%d %H:%M:%S %Z")
    utc_now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

    lines = []
    lines.append("# Frattale mirato: BTC novembre 2022 vs SOL giugno 2026")
    lines.append("")
    lines.append(f"Generato: **{rome_now}**  ")
    lines.append(f"UTC: **{utc_now}**")
    lines.append("")
    lines.append(f"Ultima candela SOL usata: **{fmt_date_it(sol_current_date)}**")
    lines.append("")
    lines.append("Questo report risponde a cinque domande:")
    lines.append("")
    lines.append("1. **SOL sta seguendo il frattale di Bitcoin post-bottom novembre 2022?**")
    lines.append("2. **In che fase siamo: anticipo, conferma, o rischio inseguimento?**")
    lines.append("3. **Se lo sta seguendo, quali dovrebbero essere i prossimi step con date precise?**")
    lines.append("4. **Quanto proietta SOL nel primo anno equivalente?**")
    lines.append("5. **Quanto proietta SOL se estendiamo il ciclo fino al top BTC 2025?**")
    lines.append("")
    lines.append(build_verdict_block(verdict, key_levels, phase, next_step_text))
    lines.append("")
    lines.append(build_operational_block(operational_summary, operational_rows))
    lines.append("")
    lines.append(build_tracking_block(tracking_status, tracking_df))
    lines.append("")
    lines.append(build_chart_block(fractal_chart_ok, projection_chart_ok, cycle_chart_ok, tracking_chart_ok))
    lines.append("")
    lines.append("## Proiezione fino al top bull market BTC 2025")
    lines.append("")
    lines.append("Questa sezione estende il frattale oltre i 365 giorni e cerca automaticamente il massimo BTC nel 2025.")
    lines.append("")
    lines.append(build_cycle_table(cycle))
    lines.append("")
    lines.append("## Prossimi step se il frattale resta valido")
    lines.append("")
    lines.append("Questa e la parte piu pratica: non dice solo il target finale, ma il percorso a step con le date reali per SOL.")
    lines.append("")
    lines.append(build_stage_table(stages))
    lines.append("")
    lines.append("## Proiezione standard a giorni fissi")
    lines.append("")
    lines.append("- **Data SOL prevista**: il giorno reale futuro, per esempio fra 7 / 14 / 30 giorni.")
    lines.append("- **Data BTC equivalente**: il giorno del frattale BTC 2022 che corrisponde a quella proiezione.")
    lines.append("- **SOL base**: SOL replica la percentuale di BTC.")
    lines.append("- **SOL beta**: SOL replica BTC ma con volatilita SOL/BTC.")
    lines.append("- **Min percorso**: quanto potrebbe scendere prima di arrivare al prezzo finale dello scenario.")
    lines.append("- **Max percorso**: quale zona alta potrebbe toccare durante lo stesso tratto.")
    lines.append("")
    lines.append(build_projection_table(projections))
    lines.append("")
    lines.append("## Dati base")
    lines.append("")
    lines.append(
        md_table(
            ["Voce", "Data", "Valore"],
            build_summary_rows(
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
                similarity,
                beta_ratio,
            ),
        )
    )
    lines.append("")
    lines.append("## Come leggerlo semplice")
    lines.append("")
    lines.append("- **Fase anticipata**: prezzo migliore, ma certezza bassa.")
    lines.append("- **Conferma iniziale**: il frattale sta migliorando, ma una parte della mossa e gia partita.")
    lines.append("- **Conferma forte**: frattale piu chiaro, ma aumenta il rischio di inseguire.")
    lines.append("- **Sotto pressione / rotto**: il paragone con BTC 2022 perde valore.")
    lines.append("- **Top ciclo BTC 2025**: e una proiezione macro, non un segnale di entrata giornaliero.")
    lines.append("")
    lines.append("La certezza arriva sempre tardi. La parte utile e capire quando il frattale e abbastanza plausibile e dove si invalida.")
    lines.append("")
    return "\n".join(lines)


def build_main_report_block(
    verdict,
    similarity,
    sol_current_date,
    sol_elapsed_days,
    btc_equiv_date,
    key_levels,
    phase,
    next_step_text,
    operational_summary,
    operational_rows,
    stages,
    projections,
    cycle,
    tracking_status,
    fractal_chart_ok,
    projection_chart_ok,
    cycle_chart_ok,
    tracking_chart_ok,
):
    score = similarity.get("total_similarity")

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

    quick_projection_table = (
        md_table(["Orizzonte", "Data SOL prevista", "BTC fece", "SOL base", "Min percorso", "Max percorso"], quick_projection_rows)
        if quick_projection_rows
        else "Dati insufficienti per la proiezione."
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

    quick_stage_table = (
        md_table(["Step", "Date SOL", "BTC fine", "SOL zona bassa", "SOL zona alta", "SOL fine base", "Lettura"], quick_stage_rows)
        if quick_stage_rows
        else "Dati insufficienti per costruire gli step."
    )

    chart_lines = []
    if fractal_chart_ok:
        chart_lines += ["### Grafico frattale sovrapposto", "", f"![Frattale BTC 2022 vs SOL 2026]({FRACTAL_CHART_FILE})", ""]
    if projection_chart_ok:
        chart_lines += ["### Grafico proiezione SOL", "", f"![Proiezione SOL BTC 2022]({PROJECTION_CHART_FILE})", ""]
    if cycle_chart_ok:
        chart_lines += [
            "### Grafico ciclo BASE fino al top BTC 2025",
            "",
            f"![Ciclo base SOL BTC 2025]({CYCLE_BASE_CHART_FILE})",
            "",
            "Nel report completo trovi anche il grafico beta separato e il grafico in scala logaritmica.",
            "",
        ]
    if tracking_chart_ok:
        chart_lines += ["### Grafico tracking giornaliero", "", f"![Tracking frattale BTC SOL]({TRACKING_CHART_FILE})", ""]
    if not chart_lines:
        chart_lines += ["Grafici non generati. Controlla che `matplotlib` sia installato.", ""]

    cycle_rows = []
    if cycle:
        cycle_rows = [
            ["Top BTC 2025", f"{cycle.get('btc_top_date_it')} - {fmt_price(cycle.get('btc_top_price'))}"],
            ["Data SOL equivalente", cycle.get("sol_cycle_top_date_it")],
            ["Target ciclo base dal bottom", fmt_price(cycle.get("target_from_bottom_base"))],
            ["Target ciclo base da oggi", fmt_price(cycle.get("target_from_current_base"))],
            ["Massimo percorso base", f"{fmt_price(cycle.get('cycle_max_base_price'))} ({cycle.get('cycle_max_base_date_it')})"],
            ["Massimo percorso beta", f"{fmt_price(cycle.get('cycle_max_beta_price'))} ({cycle.get('cycle_max_beta_date_it')})"],
        ]
    cycle_table = md_table(["Voce", "Valore"], cycle_rows) if cycle_rows else "Dati ciclo insufficienti."

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
            f"## Verdetto: {verdict['label']}",
            "",
            f"- **Fase attuale:** {phase['label']}",
            f"- **Somiglianza totale:** {fmt_pct(score)}",
            f"- **Affidabilita:** {verdict['confidence']}",
            f"- **Rischio fase:** {phase['risk']}",
            f"- **Trend tracking:** {tracking_status.get('label')}",
            f"- **Sintesi:** {verdict['short']}",
            f"- **SOL e al giorno:** {sol_elapsed_days} dal bottom usato.",
            f"- **Giorno BTC equivalente:** {btc_equiv_date.date()}",
            f"- **Prossimo step:** {next_step_text}",
            "",
            "## Lettura operativa veloce",
            "",
            operational_summary,
            "",
            md_table(["Voce", "Risposta", "Perche"], operational_rows),
            "",
            "## Target ciclo fino al top BTC 2025",
            "",
            cycle_table,
            "",
            "## Grafici",
            "",
            "\n".join(chart_lines).strip(),
            "",
            "## Livelli chiave",
            "",
            md_table(
                ["Livello", "Prezzo", "Lettura"],
                [
                    ["Prima conferma", fmt_price(key_levels.get("confirm_1")), "Migliora il frattale."],
                    ["Seconda conferma", fmt_price(key_levels.get("confirm_2")), "Scenario rialzista piu credibile."],
                    ["Invalidazione soft", fmt_price(key_levels.get("soft_invalid")), "Il frattale si indebolisce."],
                    ["Invalidazione forte", fmt_price(key_levels.get("hard_invalid")), "Il paragone BTC 2022 si rompe."],
                ],
            ),
            "",
            "## Proiezione veloce con date SOL",
            "",
            quick_projection_table,
            "",
            "## Prossimi step se SOL segue BTC 2022",
            "",
            quick_stage_table,
            "",
            "Nota: questa e una proiezione analogica. Conta soprattutto se SOL rispetta i livelli di conferma e invalidazione.",
            "",
            "<!-- BTC_SOL_FRACTAL_END -->",
        ]
    )


def inject_into_main_report(
    verdict,
    similarity,
    sol_current_date,
    sol_elapsed_days,
    btc_equiv_date,
    key_levels,
    phase,
    next_step_text,
    operational_summary,
    operational_rows,
    stages,
    projections,
    cycle,
    tracking_status,
    fractal_chart_ok,
    projection_chart_ok,
    cycle_chart_ok,
    tracking_chart_ok,
):
    if not os.path.exists(MAIN_REPORT_PATH):
        return

    with open(MAIN_REPORT_PATH, "r", encoding="utf-8") as f:
        current = f.read()

    start_marker = "<!-- BTC_SOL_FRACTAL_START -->"
    end_marker = "<!-- BTC_SOL_FRACTAL_END -->"

    if start_marker in current and end_marker in current:
        before = current.split(start_marker)[0].rstrip()
        after = current.split(end_marker, 1)[1].lstrip()
        current = before + "\n\n" + after

    block = build_main_report_block(
        verdict=verdict,
        similarity=similarity,
        sol_current_date=sol_current_date,
        sol_elapsed_days=sol_elapsed_days,
        btc_equiv_date=btc_equiv_date,
        key_levels=key_levels,
        phase=phase,
        next_step_text=next_step_text,
        operational_summary=operational_summary,
        operational_rows=operational_rows,
        stages=stages,
        projections=projections,
        cycle=cycle,
        tracking_status=tracking_status,
        fractal_chart_ok=fractal_chart_ok,
        projection_chart_ok=projection_chart_ok,
        cycle_chart_ok=cycle_chart_ok,
        tracking_chart_ok=tracking_chart_ok,
    ).strip()

    decision_end = "<!-- DECISION_REPORT_END -->"

    if decision_end in current:
        insert_pos = current.find(decision_end) + len(decision_end)
        new_text = current[:insert_pos].rstrip() + "\n\n" + block + "\n\n" + current[insert_pos:].lstrip()
    else:
        new_text = block + "\n\n" + current.lstrip()

    with open(MAIN_REPORT_PATH, "w", encoding="utf-8") as f:
        f.write(new_text.rstrip() + "\n")


def write_csv(summary_dict, projections, stages, projection_daily, cycle, cycle_daily):
    rows = []

    base = dict(summary_dict)
    base["row_type"] = "summary"
    rows.append(base)

    if cycle:
        cycle_row = dict(cycle)
        cycle_row["row_type"] = "cycle_summary"
        rows.append(cycle_row)

    for p in projections:
        row = dict(p)
        row["row_type"] = "projection"
        rows.append(row)

    for s in stages:
        row = dict(s)
        row["row_type"] = "stage"
        rows.append(row)

    if not projection_daily.empty:
        for _, item in projection_daily.iterrows():
            row = {
                "row_type": "daily_projection",
                "offset_days": item.get("offset_days"),
                "sol_date": fmt_date(item.get("sol_date")),
                "btc_equiv_date": fmt_date(item.get("btc_equiv_date")),
                "base_price": item.get("base_price"),
                "beta_price": item.get("beta_price"),
                "base_norm": item.get("base_norm"),
            }
            rows.append(row)

    if cycle_daily is not None and not cycle_daily.empty:
        for _, item in cycle_daily.iterrows():
            row = {
                "row_type": "cycle_daily_projection",
                "offset_days": item.get("offset_days"),
                "sol_date": fmt_date(item.get("sol_date")),
                "btc_equiv_date": fmt_date(item.get("btc_equiv_date")),
                "base_price": item.get("base_price"),
                "beta_price": item.get("beta_price"),
                "base_norm": item.get("base_norm"),
            }
            rows.append(row)

    df = pd.DataFrame(rows)
    df.to_csv(CSV_PATH, index=False)


def main():
    os.makedirs(REPORT_DIR, exist_ok=True)

    btc = download_close(BTC_TICKER, start="2022-01-01")
    sol = download_close(SOL_TICKER, start="2026-01-01")

    if btc.empty or sol.empty:
        report = "# Frattale BTC 2022 vs SOL 2026\n\nDati insufficienti da Yahoo Finance.\n"
        with open(REPORT_PATH, "w", encoding="utf-8") as f:
            f.write(report)
        print("Insufficient data.")
        return

    btc = add_features(btc)
    sol = add_features(sol)

    btc_anchor_date, btc_anchor_price = find_low_anchor(btc, BTC_BOTTOM_SEARCH_START, BTC_BOTTOM_SEARCH_END)
    btc_top_date, btc_top_price = find_high_anchor(btc, BTC_TOP_SEARCH_START, BTC_TOP_SEARCH_END)
    sol_anchor_date, sol_anchor_price = find_low_anchor(sol, SOL_BOTTOM_SEARCH_START, None)

    if btc_anchor_date is None or sol_anchor_date is None:
        report = "# Frattale BTC 2022 vs SOL 2026\n\nAnchor non trovati.\n"
        with open(REPORT_PATH, "w", encoding="utf-8") as f:
            f.write(report)
        print("Anchors not found.")
        return

    btc_path = normalize_path(btc, btc_anchor_date, btc_anchor_price)
    sol_path = normalize_path(sol, sol_anchor_date, sol_anchor_price)

    if btc_path.empty or sol_path.empty:
        report = "# Frattale BTC 2022 vs SOL 2026\n\nPercorsi non disponibili.\n"
        with open(REPORT_PATH, "w", encoding="utf-8") as f:
            f.write(report)
        print("Paths unavailable.")
        return

    sol_current_price = safe_float(sol_path["Close"].iloc[-1])
    sol_current_date = sol_path.index[-1]
    sol_elapsed_days = len(sol_path) - 1

    btc_equiv_idx = min(sol_elapsed_days, len(btc_path) - 1)
    btc_equiv_date = btc_path.index[btc_equiv_idx]
    btc_norm_equiv = safe_float(btc_path["norm"].iloc[btc_equiv_idx])
    sol_norm_now = safe_float(sol_path["norm"].iloc[-1])

    phase_gap_pct, phase_text = phase_gap_status(sol_norm_now, btc_norm_equiv)
    similarity = compute_similarity(btc_path, sol_path)
    compare_len = similarity.get("compare_len") or min(len(btc_path), len(sol_path))
    beta_ratio = volatility_beta(btc_path, sol_path, compare_len)

    projections = projection_from_btc(btc_path, sol_current_price, sol_current_date, sol_elapsed_days, beta_ratio)
    stages = build_stage_roadmap(btc_path, sol_current_price, sol_current_date, sol_elapsed_days, beta_ratio)
    key_levels = build_key_levels(sol_current_price, sol_anchor_price, projections)

    verdict = direct_verdict(
        total_similarity=similarity.get("total_similarity"),
        price_similarity=similarity.get("price_similarity"),
        rsi_similarity=similarity.get("rsi_similarity"),
        ma_similarity=similarity.get("ma_similarity"),
        phase_gap_pct=phase_gap_pct,
    )

    phase = current_phase(sol_current_price, key_levels, verdict)
    next_step_text = build_next_step_text(phase, stages)
    operational_summary, operational_rows = build_operational_plan(sol_current_price, key_levels, verdict, phase)

    projection_daily = make_daily_projection_path(
        btc_path=btc_path,
        sol_current_price=sol_current_price,
        sol_current_date=sol_current_date,
        sol_elapsed_days=sol_elapsed_days,
        beta_ratio=beta_ratio,
        max_days=365,
    )

    cycle, cycle_daily = build_cycle_projection(
        btc_path=btc_path,
        btc_anchor_date=btc_anchor_date,
        btc_anchor_price=btc_anchor_price,
        btc_top_date=btc_top_date,
        btc_top_price=btc_top_price,
        sol_anchor_date=sol_anchor_date,
        sol_anchor_price=sol_anchor_price,
        sol_current_date=sol_current_date,
        sol_current_price=sol_current_price,
        sol_elapsed_days=sol_elapsed_days,
        beta_ratio=beta_ratio,
    )

    summary_dict = {
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
        "price_similarity": similarity.get("price_similarity"),
        "rsi_similarity": similarity.get("rsi_similarity"),
        "ma_similarity": similarity.get("ma_similarity"),
        "total_similarity": similarity.get("total_similarity"),
        "quality_label": quality_label(similarity.get("total_similarity")),
        "verdict": verdict.get("label"),
        "verdict_confidence": verdict.get("confidence"),
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
    }

    tracking_df = update_tracking_log(summary_dict)
    tracking_status = build_tracking_status(tracking_df, summary_dict)

    fractal_chart_ok = generate_fractal_chart(btc_path, sol_path, sol_elapsed_days)
    projection_chart_ok = generate_projection_chart(sol_path, projection_daily, key_levels, projections)
    cycle_chart_ok = generate_cycle_chart(sol_path, cycle_daily, cycle)
    tracking_chart_ok = generate_tracking_chart(tracking_df)

    summary_dict.update(
        {
            "tracking_status": tracking_status.get("label"),
            "fractal_chart_ok": fractal_chart_ok,
            "projection_chart_ok": projection_chart_ok,
            "cycle_chart_ok": cycle_chart_ok,
            "tracking_chart_ok": tracking_chart_ok,
        }
    )

    report = build_report(
        btc_anchor_date=btc_anchor_date,
        btc_anchor_price=btc_anchor_price,
        sol_anchor_date=sol_anchor_date,
        sol_anchor_price=sol_anchor_price,
        sol_current_price=sol_current_price,
        sol_current_date=sol_current_date,
        sol_elapsed_days=sol_elapsed_days,
        btc_equiv_date=btc_equiv_date,
        btc_norm_equiv=btc_norm_equiv,
        sol_norm_now=sol_norm_now,
        phase_gap_pct=phase_gap_pct,
        phase_text=phase_text,
        similarity=similarity,
        beta_ratio=beta_ratio,
        verdict=verdict,
        key_levels=key_levels,
        phase=phase,
        next_step_text=next_step_text,
        operational_summary=operational_summary,
        operational_rows=operational_rows,
        projections=projections,
        stages=stages,
        cycle=cycle,
        tracking_status=tracking_status,
        tracking_df=tracking_df,
        fractal_chart_ok=fractal_chart_ok,
        projection_chart_ok=projection_chart_ok,
        cycle_chart_ok=cycle_chart_ok,
        tracking_chart_ok=tracking_chart_ok,
    )

    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        f.write(report)

    write_csv(summary_dict, projections, stages, projection_daily, cycle, cycle_daily)

    inject_into_main_report(
        verdict=verdict,
        similarity=similarity,
        sol_current_date=sol_current_date,
        sol_elapsed_days=sol_elapsed_days,
        btc_equiv_date=btc_equiv_date,
        key_levels=key_levels,
        phase=phase,
        next_step_text=next_step_text,
        operational_summary=operational_summary,
        operational_rows=operational_rows,
        stages=stages,
        projections=projections,
        cycle=cycle,
        tracking_status=tracking_status,
        fractal_chart_ok=fractal_chart_ok,
        projection_chart_ok=projection_chart_ok,
        cycle_chart_ok=cycle_chart_ok,
        tracking_chart_ok=tracking_chart_ok,
    )

    print(f"Wrote {REPORT_PATH}")
    print(f"Wrote {CSV_PATH}")
    print(f"Wrote {TRACKING_LOG_PATH}")
    print(f"Updated {MAIN_REPORT_PATH}")
    print(f"Fractal chart: {fractal_chart_ok}")
    print(f"Projection chart: {projection_chart_ok}")
    print(f"Cycle chart: {cycle_chart_ok}")
    print(f"Tracking chart: {tracking_chart_ok}")
    print(f"Verdict: {verdict.get('label')}")
    print(f"Phase: {phase.get('label')}")
    print(f"Tracking: {tracking_status.get('label')}")


if __name__ == "__main__":
    main()
