# -*- coding: utf-8 -*-
"""RSI top-cycle warning for SOL.

Metodo prudente:
- usa almeno 3 pivot RSI validi per stimare una top-line;
- separa la semplice vicinanza matematica dal rischio reale di top;
- non assegna rischio operativo con RSI ancora basso;
- limita l'extrapolazione della trendline a un massimo di 12 mesi;
- disattiva la top-line quando il fit è debole o scende a livelli RSI
  non compatibili con una vera area di esaurimento ciclo.
"""

from __future__ import annotations

import itertools
import os
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

import numpy as np
import pandas as pd
import yfinance as yf

from shared_market_snapshot import apply_snapshot_to_ohlcv, snapshot_source_label

try:
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    CHARTS_AVAILABLE = True
except Exception:
    CHARTS_AVAILABLE = False


REPORT_DIR = "reports"
MAIN_REPORT_PATH = "reports/latest_report.md"
REPORT_PATH = "reports/rsi_top_cycle_report.md"
CSV_PATH = "reports/rsi_top_cycle_metrics.csv"
BTC_SOL_METRICS_PATH = "reports/btc_2022_vs_sol_2026_metrics.csv"

WEEKLY_CHART_PATH = "reports/rsi_top_cycle_SOL_weekly.png"
MONTHLY_CHART_PATH = "reports/rsi_top_cycle_SOL_monthly.png"
WEEKLY_CHART_FILE = "rsi_top_cycle_SOL_weekly.png"
MONTHLY_CHART_FILE = "rsi_top_cycle_SOL_monthly.png"

TICKER = "SOL-USD"
ASSET_NAME = "SOL"
DOWNLOAD_START = "2020-01-01"
RSI_PERIOD = 14
ANCHOR_START_DATE = "2023-01-01"

# Pivot e ancore.
MIN_ANCHORS = 3
MAX_CANDIDATE_PIVOTS = 12
WEEKLY_MAX_ANCHORS = 6
MONTHLY_MAX_ANCHORS = 5

WEEKLY_MIN_RSI = 60
WEEKLY_PIVOT_WINDOW = 7
WEEKLY_MIN_GAP_DAYS = 90

MONTHLY_MIN_RSI = 55
MONTHLY_PIVOT_WINDOW = 3
MONTHLY_MIN_GAP_DAYS = 150

# Qualità minima del fit.
MIN_LINE_R2 = 0.45
MAX_LINE_RMSE = 8.0
MAX_ABS_SLOPE_PER_YEAR = 30.0

# Una top-line sotto questi valori non è più una vera soglia di esaurimento.
WEEKLY_MIN_OPERATIONAL_TOPLINE = 60.0
MONTHLY_MIN_OPERATIONAL_TOPLINE = 55.0

# Anche con una linea valida, il rischio top resta nullo finché RSI è basso.
WEEKLY_MIN_RSI_FOR_WARNING = 60.0
MONTHLY_MIN_RSI_FOR_WARNING = 55.0

# Nessuna linea viene proiettata oltre 12 mesi.
WEEKLY_MAX_PROJECTION_DAYS = 365
MONTHLY_MAX_PROJECTION_DAYS = 365

START_MARKER = "<!-- RSI_TOP_CYCLE_START -->"
END_MARKER = "<!-- RSI_TOP_CYCLE_END -->"


# -----------------------------------------------------------------------------
# Utility
# -----------------------------------------------------------------------------


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


def md_table(headers, rows):
    def clean(x):
        return str(x).replace("|", "\\|").replace("\n", " ")

    lines = [
        "| " + " | ".join(clean(h) for h in headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]

    for row in rows:
        lines.append("| " + " | ".join(clean(c) for c in row) + " |")

    return "\n".join(lines)


def period_config(period_name):
    period = str(period_name).lower()

    if period == "monthly":
        return {
            "min_gap_days": MONTHLY_MIN_GAP_DAYS,
            "max_anchors": MONTHLY_MAX_ANCHORS,
            "min_operational_topline": MONTHLY_MIN_OPERATIONAL_TOPLINE,
            "min_rsi_for_warning": MONTHLY_MIN_RSI_FOR_WARNING,
            "max_projection_days": MONTHLY_MAX_PROJECTION_DAYS,
        }

    return {
        "min_gap_days": WEEKLY_MIN_GAP_DAYS,
        "max_anchors": WEEKLY_MAX_ANCHORS,
        "min_operational_topline": WEEKLY_MIN_OPERATIONAL_TOPLINE,
        "min_rsi_for_warning": WEEKLY_MIN_RSI_FOR_WARNING,
        "max_projection_days": WEEKLY_MAX_PROJECTION_DAYS,
    }


# -----------------------------------------------------------------------------
# Dati e RSI
# -----------------------------------------------------------------------------


def rsi(close, period=14):
    close = pd.to_numeric(close, errors="coerce")
    delta = close.diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    avg_gain = gain.ewm(alpha=1 / period, adjust=False).mean()
    avg_loss = loss.ewm(alpha=1 / period, adjust=False).mean()
    rs = avg_gain / avg_loss.replace(0, np.nan)
    return 100 - (100 / (1 + rs))


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
    df = df[~df.index.duplicated(keep="last")]
    return df.sort_index()


def resample_close(df, mode):
    if df.empty:
        return pd.DataFrame()

    if mode == "weekly":
        out = df["Close"].resample("W").last().dropna().to_frame("Close")
    else:
        out = df["Close"].resample("ME").last().dropna().to_frame("Close")

    out["rsi"] = rsi(out["Close"], RSI_PERIOD)
    return out.dropna().copy()


# -----------------------------------------------------------------------------
# Pivot, ancore e regressione
# -----------------------------------------------------------------------------


def find_pivot_highs(df, window, min_rsi):
    if df.empty or "rsi" not in df.columns:
        return pd.DataFrame(columns=["date", "rsi", "close"])

    s = pd.to_numeric(df["rsi"], errors="coerce").dropna()
    half = max(1, int(window // 2))
    rows = []

    for i in range(half, len(s) - half):
        value = safe_float(s.iloc[i])
        if value is None or value < min_rsi:
            continue

        local = s.iloc[i - half : i + half + 1]
        local_max = safe_float(local.max())
        if local_max is None:
            continue

        # In caso di plateau conserva soltanto il primo massimo locale.
        if value >= local_max - 1e-9:
            first_max_pos = int(np.argmax(local.to_numpy(dtype=float)))
            if first_max_pos != half:
                continue

            date = s.index[i]
            rows.append(
                {
                    "date": pd.to_datetime(date),
                    "rsi": value,
                    "close": safe_float(df.loc[date, "Close"]),
                }
            )

    pivots = pd.DataFrame(rows)
    if pivots.empty:
        return pd.DataFrame(columns=["date", "rsi", "close"])

    return pivots.sort_values("date").reset_index(drop=True)


def fit_line(anchors):
    if anchors is None or anchors.empty or len(anchors) < MIN_ANCHORS:
        return None

    a = anchors.copy()
    a["date"] = pd.to_datetime(a["date"], errors="coerce")
    a["rsi"] = pd.to_numeric(a["rsi"], errors="coerce")
    a = a.dropna(subset=["date", "rsi"]).sort_values("date")

    if len(a) < MIN_ANCHORS:
        return None

    x = a["date"].map(pd.Timestamp.toordinal).astype(float).to_numpy()
    y = a["rsi"].astype(float).to_numpy()

    if np.std(x) == 0:
        return None

    slope, intercept = np.polyfit(x, y, 1)
    predicted = slope * x + intercept
    residuals = y - predicted

    ss_res = float(np.sum(residuals**2))
    ss_tot = float(np.sum((y - np.mean(y)) ** 2))
    r2 = 1.0 if ss_tot == 0 else 1.0 - ss_res / ss_tot
    rmse = float(np.sqrt(np.mean(residuals**2)))

    return {
        "slope": float(slope),
        "intercept": float(intercept),
        "slope_per_year": float(slope * 365.25),
        "r2": float(r2),
        "rmse": rmse,
        "anchor_count": int(len(a)),
        "fit_start_date": fmt_date(a.iloc[0]["date"]),
        "fit_end_date": fmt_date(a.iloc[-1]["date"]),
        "anchor_1_date": fmt_date(a.iloc[0]["date"]),
        "anchor_1_rsi": safe_float(a.iloc[0]["rsi"]),
        "anchor_1_price": safe_float(a.iloc[0].get("close")),
        "anchor_2_date": fmt_date(a.iloc[-1]["date"]),
        "anchor_2_rsi": safe_float(a.iloc[-1]["rsi"]),
        "anchor_2_price": safe_float(a.iloc[-1].get("close")),
    }


def line_value(model, date_value):
    if not model:
        return None

    try:
        ordinal = pd.to_datetime(date_value).toordinal()
        return float(model["slope"] * ordinal + model["intercept"])
    except Exception:
        return None


def _candidate_score(model, anchors, latest_pivot_date):
    if not model:
        return -1e9

    r2 = safe_float(model.get("r2")) or 0.0
    rmse = safe_float(model.get("rmse")) or 99.0
    slope_per_year = safe_float(model.get("slope_per_year")) or 0.0
    anchor_count = int(model.get("anchor_count") or 0)

    last_anchor_date = pd.to_datetime(anchors.iloc[-1]["date"])
    days_old = max(0, int((latest_pivot_date - last_anchor_date).days))

    recency_bonus = max(0.0, 18.0 - days_old / 30.0)
    anchor_bonus = anchor_count * 4.0
    slope_penalty = max(0.0, abs(slope_per_year) - 18.0) * 0.8

    return r2 * 100.0 - rmse * 5.0 + recency_bonus + anchor_bonus - slope_penalty


def choose_anchors(period_name, pivots):
    if pivots is None or pivots.empty or len(pivots) < MIN_ANCHORS:
        return pd.DataFrame(columns=["date", "rsi", "close"])

    cfg = period_config(period_name)
    min_gap = int(cfg["min_gap_days"])
    max_anchors = int(cfg["max_anchors"])

    p = pivots.copy()
    p["date"] = pd.to_datetime(p["date"], errors="coerce")
    p["rsi"] = pd.to_numeric(p["rsi"], errors="coerce")
    p = p.dropna(subset=["date", "rsi"]).sort_values("date")
    p = p.tail(MAX_CANDIDATE_PIVOTS).reset_index(drop=True)

    if len(p) < MIN_ANCHORS:
        return pd.DataFrame(columns=["date", "rsi", "close"])

    latest_pivot_date = pd.to_datetime(p["date"].max())
    best = None
    best_score = -1e9

    max_k = min(max_anchors, len(p))

    for k in range(MIN_ANCHORS, max_k + 1):
        for indexes in itertools.combinations(range(len(p)), k):
            candidate = p.iloc[list(indexes)].copy().sort_values("date")
            dates = pd.to_datetime(candidate["date"]).tolist()

            gaps_ok = all(
                (dates[i] - dates[i - 1]).days >= min_gap
                for i in range(1, len(dates))
            )
            if not gaps_ok:
                continue

            model = fit_line(candidate)
            if not model:
                continue

            slope_per_year = safe_float(model.get("slope_per_year"))
            if slope_per_year is None:
                continue

            # La top-line deve essere piatta o discendente, non crescente.
            if slope_per_year > 1.0:
                continue

            score = _candidate_score(model, candidate, latest_pivot_date)
            if score > best_score:
                best_score = score
                best = candidate

    if best is None:
        return pd.DataFrame(columns=["date", "rsi", "close"])

    return best.reset_index(drop=True)


# -----------------------------------------------------------------------------
# Qualità linea e rischio top
# -----------------------------------------------------------------------------


def evaluate_line_quality(period_name, model, current_date, cycle_date=None):
    cfg = period_config(period_name)
    min_topline = float(cfg["min_operational_topline"])
    max_projection_days = int(cfg["max_projection_days"])

    result = {
        "operational": False,
        "quality": "NON DISPONIBILE",
        "reason": "Trendline non disponibile.",
        "line_now_raw": None,
        "projection_end_date": None,
        "projection_days": 0,
        "line_at_projection_end": None,
        "line_at_cycle_top": None,
        "cycle_projection_status": "non disponibile",
    }

    if not model:
        return result

    anchor_count = int(model.get("anchor_count") or 0)
    r2 = safe_float(model.get("r2"))
    rmse = safe_float(model.get("rmse"))
    slope_per_year = safe_float(model.get("slope_per_year"))
    line_now = line_value(model, current_date)

    result["line_now_raw"] = line_now

    if anchor_count < MIN_ANCHORS:
        result["quality"] = "NON VALIDA"
        result["reason"] = f"Servono almeno {MIN_ANCHORS} picchi RSI validi."
        return result

    if slope_per_year is None or slope_per_year > 1.0:
        result["quality"] = "NON VALIDA"
        result["reason"] = "La linea non è piatta/discendente."
        return result

    if abs(slope_per_year) > MAX_ABS_SLOPE_PER_YEAR:
        result["quality"] = "NON VALIDA"
        result["reason"] = "Pendenza troppo estrema per una top-line affidabile."
        return result

    if r2 is None or r2 < MIN_LINE_R2:
        result["quality"] = "DEBOLE / NON OPERATIVA"
        result["reason"] = f"Fit insufficiente: R² {fmt_number(r2, 2)}."
        return result

    if rmse is None or rmse > MAX_LINE_RMSE:
        result["quality"] = "DEBOLE / NON OPERATIVA"
        result["reason"] = f"Errore del fit troppo alto: RMSE {fmt_number(rmse, 2)} RSI."
        return result

    if line_now is None or line_now < min_topline:
        result["quality"] = "IRREALISTICA / NON OPERATIVA"
        result["reason"] = (
            f"La top-line stimata oggi è sotto RSI {fmt_number(min_topline, 0)}; "
            "non rappresenta più una vera area di esaurimento ciclo."
        )
        return result

    current_date = pd.to_datetime(current_date)
    projection_days = max_projection_days

    # Se la linea discendente raggiunge la soglia minima prima di 12 mesi,
    # la proiezione viene fermata in quel punto.
    slope = safe_float(model.get("slope"))
    if slope is not None and slope < 0:
        days_to_floor = int(np.floor((min_topline - line_now) / slope))
        if days_to_floor > 0:
            projection_days = min(projection_days, days_to_floor)

    projection_days = max(0, projection_days)
    projection_end = current_date + pd.Timedelta(days=projection_days)
    line_at_projection_end = line_value(model, projection_end)

    result.update(
        {
            "operational": True,
            "quality": "VALIDA / USO PRUDENTE",
            "reason": (
                f"Fit basato su {anchor_count} picchi, R² {fmt_number(r2, 2)}, "
                f"RMSE {fmt_number(rmse, 2)}."
            ),
            "projection_end_date": fmt_date(projection_end),
            "projection_days": projection_days,
            "line_at_projection_end": line_at_projection_end,
        }
    )

    if cycle_date is None or pd.isna(cycle_date):
        result["cycle_projection_status"] = "data ciclo non disponibile"
        return result

    cycle_date = pd.to_datetime(cycle_date)

    if cycle_date > projection_end:
        result["cycle_projection_status"] = (
            f"non proiettata fino al {fmt_date(cycle_date)}: limite massimo {projection_days} giorni"
        )
        return result

    cycle_value = line_value(model, cycle_date)
    if cycle_value is None or cycle_value < min_topline:
        result["cycle_projection_status"] = "valore ciclo non realistico"
        return result

    result["line_at_cycle_top"] = cycle_value
    result["cycle_projection_status"] = "disponibile entro orizzonte valido"
    return result


def classify_math_proximity(current_rsi, line_now_raw):
    current_rsi = safe_float(current_rsi)
    line_now_raw = safe_float(line_now_raw)

    if current_rsi is None or line_now_raw is None:
        return {
            "status": "N/D",
            "distance": None,
            "text": "Vicinanza matematica non disponibile.",
        }

    distance = line_now_raw - current_rsi

    if distance > 10:
        status = "LONTANO"
    elif distance > 5:
        status = "IN AVVICINAMENTO"
    elif distance > 0:
        status = "VICINO"
    elif distance >= -3:
        status = "TOCCO / LEGGERO SUPERAMENTO"
    else:
        status = "SOPRA LA LINEA"

    return {
        "status": status,
        "distance": distance,
        "text": (
            f"Distanza matematica dalla linea: {fmt_number(distance, 2)} punti RSI. "
            "Questa misura da sola non determina il rischio top."
        ),
    }


def classify_top_risk(period_name, current_rsi, math_proximity, line_quality):
    cfg = period_config(period_name)
    min_rsi_for_warning = float(cfg["min_rsi_for_warning"])

    current_rsi = safe_float(current_rsi)
    distance = safe_float(math_proximity.get("distance"))
    operational = bool(line_quality.get("operational"))

    if current_rsi is None:
        return {
            "status": "DATI INSUFFICIENTI",
            "score": 0,
            "text": "RSI non disponibile.",
        }

    if not operational:
        return {
            "status": "LINEA NON AFFIDABILE / RISCHIO NON ATTIVO",
            "score": 0,
            "text": (
                f"La top-line {period_name} non supera i controlli di qualità. "
                "Non viene usata per generare rischio top-cycle."
            ),
        }

    if current_rsi < min_rsi_for_warning:
        return {
            "status": "RSI TROPPO BASSO PER RISCHIO TOP",
            "score": 0,
            "text": (
                f"RSI {period_name} è {fmt_number(current_rsi, 1)}, sotto la soglia prudente "
                f"{fmt_number(min_rsi_for_warning, 0)}. Anche se fosse vicino alla linea, "
                "non è una vera zona di esaurimento ciclo."
            ),
        }

    if distance is None:
        return {
            "status": "DATI INSUFFICIENTI",
            "score": 0,
            "text": "Distanza dalla linea non disponibile.",
        }

    if distance > 10:
        return {
            "status": "LONTANO DALLA TOP-LINE",
            "score": 0,
            "text": f"RSI {period_name} è alto abbastanza da essere monitorato, ma resta lontano dalla top-line.",
        }

    if distance > 5:
        return {
            "status": "IN AVVICINAMENTO / SOLO MONITORAGGIO",
            "score": 0,
            "text": f"RSI {period_name} si avvicina alla top-line, ma non genera ancora rischio operativo.",
        }

    if distance > 0:
        return {
            "status": "TEST VICINO ALLA TOP-LINE",
            "score": 1,
            "text": f"RSI {period_name} è alto e vicino alla top-line: possibile top locale, da confermare col prezzo.",
        }

    if distance >= -3:
        return {
            "status": "TOCCO / BREAKOUT LEGGERO",
            "score": 2,
            "text": f"RSI {period_name} sta toccando o superando di poco una top-line valida.",
        }

    return {
        "status": "SOPRA TOP-LINE / ESTENSIONE",
        "score": 3,
        "text": f"RSI {period_name} è sopra una top-line valida: possibile estensione estrema o distribuzione.",
    }


# -----------------------------------------------------------------------------
# Contesto ciclo
# -----------------------------------------------------------------------------


def read_cycle_context():
    ctx = {
        "cycle_max_base_price": None,
        "cycle_max_base_date": None,
        "cycle_max_beta_price": None,
        "target_from_current_base": None,
        "target_from_bottom_base": None,
    }

    if not os.path.exists(BTC_SOL_METRICS_PATH):
        return ctx

    try:
        df = pd.read_csv(BTC_SOL_METRICS_PATH)
    except Exception:
        return ctx

    if df.empty or "row_type" not in df.columns:
        return ctx

    rows = df[df["row_type"].astype(str) == "cycle_summary"].copy()
    if rows.empty:
        return ctx

    row = rows.iloc[-1]

    for key in list(ctx.keys()):
        if key in row:
            ctx[key] = row.get(key)

    return ctx


# -----------------------------------------------------------------------------
# Sintesi per periodo e confluenza
# -----------------------------------------------------------------------------


def build_period_summary(period_name, df, min_rsi, window, cycle_date=None):
    empty_result = {
        "period": period_name,
        "ok": False,
        "current_date": None,
        "current_price": None,
        "current_rsi": None,
        "line_now": None,
        "line_now_raw": None,
        "distance": None,
        "math_status": "N/D",
        "risk_status": "DATI INSUFFICIENTI",
        "status": "DATI INSUFFICIENTI",
        "text": "Dati insufficienti.",
        "score": 0,
        "anchors": pd.DataFrame(columns=["date", "rsi", "close"]),
        "model": None,
        "line_at_cycle_top": None,
        "line_quality": "NON DISPONIBILE",
        "line_quality_reason": "Dati insufficienti.",
        "projection_end_date": None,
        "projection_days": 0,
        "line_at_projection_end": None,
        "cycle_projection_status": "non disponibile",
    }

    if df.empty:
        return empty_result

    anchor_df = df[df.index >= pd.to_datetime(ANCHOR_START_DATE)].copy()
    if anchor_df.empty or len(anchor_df) < 8:
        anchor_df = df.copy()

    pivots = find_pivot_highs(anchor_df, window=window, min_rsi=min_rsi)
    anchors = choose_anchors(period_name, pivots)
    model = fit_line(anchors)

    current_date = df.index[-1]
    current_rsi = safe_float(df["rsi"].iloc[-1])
    current_close = safe_float(df["Close"].iloc[-1])

    quality = evaluate_line_quality(period_name, model, current_date, cycle_date)
    math_proximity = classify_math_proximity(current_rsi, quality.get("line_now_raw"))
    top_risk = classify_top_risk(period_name, current_rsi, math_proximity, quality)

    line_now_operational = quality.get("line_now_raw") if quality.get("operational") else None

    return {
        "period": period_name,
        "ok": model is not None,
        "current_date": fmt_date(current_date),
        "current_price": current_close,
        "current_rsi": current_rsi,
        "line_now": line_now_operational,
        "line_now_raw": quality.get("line_now_raw"),
        "distance": math_proximity.get("distance"),
        "math_status": math_proximity.get("status"),
        "math_text": math_proximity.get("text"),
        "risk_status": top_risk.get("status"),
        "status": top_risk.get("status"),
        "text": top_risk.get("text"),
        "score": top_risk.get("score", 0),
        "anchors": anchors,
        "pivots": pivots,
        "model": model,
        "line_at_cycle_top": quality.get("line_at_cycle_top"),
        "line_quality": quality.get("quality"),
        "line_quality_reason": quality.get("reason"),
        "line_operational": quality.get("operational", False),
        "projection_end_date": quality.get("projection_end_date"),
        "projection_days": quality.get("projection_days", 0),
        "line_at_projection_end": quality.get("line_at_projection_end"),
        "cycle_projection_status": quality.get("cycle_projection_status"),
    }


def classify_confluence(weekly, monthly, current_price, ctx):
    current_price = safe_float(current_price)
    cycle_target = safe_float(ctx.get("cycle_max_base_price")) or safe_float(
        ctx.get("target_from_current_base")
    )

    weekly_score = int(weekly.get("score", 0) or 0)
    monthly_score = int(monthly.get("score", 0) or 0)

    progress = None
    if current_price is not None and cycle_target is not None and cycle_target > 0:
        progress = current_price / cycle_target * 100

    if progress is None:
        bucket = "n/d"
    elif progress < 35:
        bucket = "inizio ciclo / lontano dal target macro"
    elif progress < 60:
        bucket = "fase intermedia"
    elif progress < 80:
        bucket = "fase avanzata"
    else:
        bucket = "vicino al target ciclo"

    weekly_active = weekly_score > 0
    monthly_active = monthly_score > 0

    # Regola prudente: un RSI 40-50 o una linea non valida non può generare
    # rischio ALTO/MOLTO ALTO e non deve sottrarre punti al Global.
    if progress is not None and progress < 35:
        label = "BASSO"
        action = (
            "Nessun segnale top-cycle macro attivo. Prezzo ancora lontano dal target ciclo; "
            "il filtro RSI resta solo di monitoraggio."
        )
    elif weekly_score >= 3 and monthly_score >= 2 and progress is not None and progress >= 80:
        label = "MOLTO ALTO"
        action = (
            "Weekly e monthly RSI sono in estensione su top-line valide mentre il prezzo è vicino "
            "alla zona ciclo. Area da distribuire, non da inseguire."
        )
    elif weekly_score >= 2 and monthly_score >= 1 and progress is not None and progress >= 60:
        label = "ALTO"
        action = (
            "Conferma RSI multi-timeframe in zona avanzata di prezzo. Ha senso ridurre rischio e "
            "prendere profitto parziale."
        )
    elif weekly_active or monthly_active:
        label = "MEDIO"
        action = (
            "Un timeframe RSI sta testando una top-line valida. È un avviso, non una conferma di top macro."
        )
    else:
        label = "BASSO"
        action = (
            "RSI non segnala esaurimento ciclo macro. Le linee non valide o gli RSI bassi non vengono pesati."
        )

    return {
        "label": label,
        "action": action,
        "price_progress_pct": progress,
        "price_bucket": bucket,
        "cycle_target": cycle_target,
        "weekly_score": weekly_score,
        "monthly_score": monthly_score,
    }


# -----------------------------------------------------------------------------
# Grafici
# -----------------------------------------------------------------------------


def _plot_quality_note(ax, summary):
    if summary.get("line_operational"):
        text = (
            f"Top-line valida | {summary.get('line_quality_reason', '')} | "
            f"proiezione max {summary.get('projection_days', 0)} giorni"
        )
    else:
        text = (
            "TOP-LINE NON USATA NEL PUNTEGGIO\n"
            f"{summary.get('line_quality', 'NON DISPONIBILE')}: "
            f"{summary.get('line_quality_reason', 'n/d')}"
        )

    ax.text(
        0.01,
        0.02,
        text,
        transform=ax.transAxes,
        fontsize=9,
        va="bottom",
        ha="left",
        bbox=dict(boxstyle="round,pad=0.35", fc="white", alpha=0.85),
    )


def plot_chart(period_name, df, summary, ctx, output_path):
    if not CHARTS_AVAILABLE:
        return False

    try:
        fig, ax = plt.subplots(figsize=(13, 6))

        if df.empty:
            ax.text(
                0.5,
                0.5,
                "Dati insufficienti per RSI top-cycle",
                ha="center",
                va="center",
                fontsize=12,
            )
            ax.set_title(f"{ASSET_NAME} RSI {period_name} top-cycle")
            ax.axis("off")
            fig.tight_layout()
            fig.savefig(output_path, dpi=160, bbox_inches="tight")
            plt.close(fig)
            return os.path.exists(output_path)

        ax.plot(df.index, df["rsi"], linewidth=1.7, label=f"RSI {period_name}")
        ax.axhline(70, linestyle=":", alpha=0.45)
        ax.axhline(50, linestyle=":", alpha=0.45)
        ax.axhline(30, linestyle=":", alpha=0.45)

        model = summary.get("model")
        anchors = summary.get("anchors")

        if model and anchors is not None and not anchors.empty:
            anchor_dates = pd.to_datetime(anchors["date"])
            fit_start = anchor_dates.min()
            fit_end = max(anchor_dates.max(), df.index.max())
            fit_dates = pd.date_range(start=fit_start, end=fit_end, periods=240)
            fit_values = [line_value(model, d) for d in fit_dates]
            fit_values = [np.nan if v is None else v for v in fit_values]

            ax.plot(
                fit_dates,
                fit_values,
                linestyle="--",
                linewidth=1.6,
                label="Fit top-line su almeno 3 picchi",
            )

            if summary.get("line_operational") and summary.get("projection_days", 0) > 0:
                projection_end = pd.to_datetime(summary.get("projection_end_date"), errors="coerce")
                if not pd.isna(projection_end) and projection_end > df.index.max():
                    future_dates = pd.date_range(
                        start=df.index.max(),
                        end=projection_end,
                        periods=120,
                    )
                    future_values = [line_value(model, d) for d in future_dates]
                    future_values = [np.nan if v is None else v for v in future_values]
                    ax.plot(
                        future_dates,
                        future_values,
                        linestyle=":",
                        linewidth=1.4,
                        label="Proiezione limitata della top-line",
                    )

            ax.scatter(
                anchor_dates,
                pd.to_numeric(anchors["rsi"], errors="coerce"),
                s=55,
                zorder=5,
                label="Picchi RSI usati",
            )

            for _, row in anchors.iterrows():
                ax.annotate(
                    f"{fmt_date(row['date'])}\nRSI {fmt_number(row['rsi'], 1)}",
                    xy=(pd.to_datetime(row["date"]), safe_float(row["rsi"])),
                    xytext=(8, 9),
                    textcoords="offset points",
                    fontsize=8,
                    bbox=dict(boxstyle="round,pad=0.18", fc="white", alpha=0.78),
                )

        current_date = df.index[-1]
        current_rsi = safe_float(df["rsi"].iloc[-1])

        if current_rsi is not None:
            ax.scatter([current_date], [current_rsi], s=60, zorder=6)
            ax.annotate(
                f"Oggi RSI {fmt_number(current_rsi, 1)}",
                xy=(current_date, current_rsi),
                xytext=(8, 12),
                textcoords="offset points",
                fontsize=8,
                bbox=dict(boxstyle="round,pad=0.18", fc="white", alpha=0.82),
            )

        cycle_date = ctx.get("cycle_max_base_date")
        cycle_date = pd.to_datetime(cycle_date, errors="coerce") if cycle_date is not None else None

        if cycle_date is not None and not pd.isna(cycle_date):
            projection_end = pd.to_datetime(summary.get("projection_end_date"), errors="coerce")
            if (
                summary.get("line_operational")
                and not pd.isna(projection_end)
                and cycle_date <= projection_end
            ):
                ax.axvline(cycle_date, linestyle=":", alpha=0.4)
                ax.annotate(
                    "Data ciclo entro orizzonte valido",
                    xy=(cycle_date, 50),
                    xytext=(8, 8),
                    textcoords="offset points",
                    fontsize=8,
                    bbox=dict(boxstyle="round,pad=0.18", fc="white", alpha=0.75),
                )

        _plot_quality_note(ax, summary)

        ax.set_ylim(0, 100)
        ax.set_title(
            f"{ASSET_NAME} RSI {period_name}: top-cycle warning\n"
            f"Rischio: {summary.get('risk_status', 'n/d')}"
        )
        ax.set_xlabel("Data")
        ax.set_ylabel("RSI")
        ax.grid(True, alpha=0.28)
        ax.legend(loc="upper right")
        fig.autofmt_xdate()
        fig.tight_layout()
        fig.savefig(output_path, dpi=170, bbox_inches="tight")
        plt.close(fig)

        return os.path.exists(output_path) and os.path.getsize(output_path) > 1000

    except Exception as exc:
        print(f"Could not generate RSI {period_name} chart: {exc}")
        return False


# -----------------------------------------------------------------------------
# Report Markdown
# -----------------------------------------------------------------------------


def build_anchor_rows(weekly, monthly):
    rows = []

    for label, item in [("Weekly", weekly), ("Monthly", monthly)]:
        anchors = item.get("anchors")

        if anchors is None or anchors.empty:
            rows.append([label, "n/d", "n/d", "n/d"])
            continue

        for _, row in anchors.iterrows():
            rows.append(
                [
                    label,
                    fmt_date(row.get("date")),
                    fmt_number(row.get("rsi"), 2),
                    fmt_price(row.get("close")),
                ]
            )

    return rows


def build_report(weekly, monthly, confluence, ctx, weekly_ok, monthly_ok):
    rome_now = datetime.now(ZoneInfo("Europe/Rome")).strftime("%Y-%m-%d %H:%M:%S %Z")
    utc_now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

    current_price = weekly.get("current_price") or monthly.get("current_price")

    summary_rows = []
    for label, item in [("Weekly RSI", weekly), ("Monthly RSI", monthly)]:
        model = item.get("model") or {}
        summary_rows.append(
            [
                label,
                fmt_number(item.get("current_rsi"), 2),
                fmt_number(item.get("line_now_raw"), 2),
                fmt_number(item.get("distance"), 2),
                item.get("math_status", "n/d"),
                item.get("risk_status", "n/d"),
                model.get("anchor_count", 0),
                fmt_number(model.get("r2"), 2),
                fmt_number(model.get("rmse"), 2),
                item.get("line_quality", "n/d"),
            ]
        )

    cycle_rows = [
        ["Prezzo SOL attuale", fmt_price(current_price)],
        ["Target ciclo base", fmt_price(confluence.get("cycle_target"))],
        ["Avanzamento verso target base", fmt_pct(confluence.get("price_progress_pct"))],
        ["Fase prezzo", confluence.get("price_bucket", "n/d")],
        ["Rischio top-cycle RSI", confluence.get("label", "n/d")],
        ["Score weekly", confluence.get("weekly_score", 0)],
        ["Score monthly", confluence.get("monthly_score", 0)],
    ]

    quality_rows = []
    for label, item in [("Weekly", weekly), ("Monthly", monthly)]:
        model = item.get("model") or {}
        quality_rows.append(
            [
                label,
                model.get("anchor_count", 0),
                fmt_number(model.get("slope_per_year"), 2),
                fmt_number(model.get("r2"), 2),
                fmt_number(model.get("rmse"), 2),
                item.get("line_quality", "n/d"),
                item.get("line_quality_reason", "n/d"),
                item.get("projection_end_date", "n/d"),
                item.get("cycle_projection_status", "n/d"),
            ]
        )

    lines = [
        "# RSI top-cycle warning - SOL",
        "",
        f"Generato: **{rome_now}**  ",
        f"UTC: **{utc_now}**",
        "",
        "Questo report usa l'RSI soltanto come filtro di possibile esaurimento ciclo.",
        "La vicinanza matematica a una retta non basta: la linea deve essere costruita su almeno tre picchi, superare i controlli di qualità e trovarsi in una vera zona RSI da top.",
        "",
        "## Sintesi",
        "",
        md_table(
            [
                "Voce",
                "RSI attuale",
                "Linea stimata grezza",
                "Distanza matematica",
                "Vicinanza matematica",
                "Rischio reale",
                "Picchi",
                "R²",
                "RMSE",
                "Qualità linea",
            ],
            summary_rows,
        ),
        "",
        "## Confluenza con target ciclo SOL",
        "",
        md_table(["Voce", "Valore"], cycle_rows),
        "",
        f"**Lettura:** {confluence.get('action', 'n/d')}",
        "",
        "## Controllo qualità delle top-line",
        "",
        md_table(
            [
                "Periodo",
                "Picchi usati",
                "Pendenza RSI/anno",
                "R²",
                "RMSE",
                "Stato",
                "Motivo",
                "Fine proiezione",
                "Proiezione alla data ciclo",
            ],
            quality_rows,
        ),
        "",
        "Regole applicate:",
        "",
        f"- servono almeno **{MIN_ANCHORS} picchi RSI validi**;",
        f"- R² minimo **{MIN_LINE_R2:.2f}** e RMSE massimo **{MAX_LINE_RMSE:.1f}**;",
        f"- weekly top-line operativa solo da RSI **{WEEKLY_MIN_OPERATIONAL_TOPLINE:.0f}** in su;",
        f"- monthly top-line operativa solo da RSI **{MONTHLY_MIN_OPERATIONAL_TOPLINE:.0f}** in su;",
        "- nessuna proiezione oltre **12 mesi**;",
        "- se RSI attuale è sotto la soglia di warning, il rischio resta **0** anche se la distanza matematica è piccola.",
        "",
        "## Picchi RSI usati",
        "",
        md_table(["Periodo", "Data", "RSI", "Prezzo SOL"], build_anchor_rows(weekly, monthly)),
        "",
        "## Come leggerlo",
        "",
        "- **Vicinanza matematica** descrive soltanto la distanza dalla retta.",
        "- **Rischio reale** considera qualità della linea, livello assoluto dell'RSI e contesto prezzo.",
        "- RSI tra 40 e 50 non è una zona top-cycle e non deve generare penalità nel Global.",
        "- Una linea che scende verso RSI 50 o meno non viene più trattata come top-line macro.",
        "- Il target 2029 non viene usato per prolungare una retta oltre il suo orizzonte statistico ragionevole.",
        "",
        "## Grafici",
        "",
    ]

    if weekly_ok:
        lines += [
            "### SOL weekly RSI top-line",
            "",
            f"![SOL weekly RSI top-line]({WEEKLY_CHART_FILE})",
            "",
        ]

    if monthly_ok:
        lines += [
            "### SOL monthly RSI top-line",
            "",
            f"![SOL monthly RSI top-line]({MONTHLY_CHART_FILE})",
            "",
        ]

    lines += [
        "## Stato attuale",
        "",
        f"- **Weekly:** {weekly.get('text', 'n/d')}",
        f"- **Monthly:** {monthly.get('text', 'n/d')}",
        f"- **Rischio top-cycle attuale:** {confluence.get('label', 'n/d')}",
        "",
        "Traduzione pratica: questo modulo serve soprattutto quando RSI weekly/monthly tornano davvero in area alta. Con RSI basso o con una top-line non affidabile resta neutrale e non sottrae punti al Global Confluence.",
        "",
    ]

    return "\n".join(lines)


def build_main_block(weekly, monthly, confluence, weekly_ok, monthly_ok):
    current_price = weekly.get("current_price") or monthly.get("current_price")

    rows = [
        ["Prezzo SOL", fmt_price(current_price), ""],
        [
            "Weekly RSI",
            (
                f"{fmt_number(weekly.get('current_rsi'), 2)} / "
                f"linea grezza {fmt_number(weekly.get('line_now_raw'), 2)}"
            ),
            f"{weekly.get('risk_status', 'n/d')} — {weekly.get('line_quality', 'n/d')}",
        ],
        [
            "Monthly RSI",
            (
                f"{fmt_number(monthly.get('current_rsi'), 2)} / "
                f"linea grezza {fmt_number(monthly.get('line_now_raw'), 2)}"
            ),
            f"{monthly.get('risk_status', 'n/d')} — {monthly.get('line_quality', 'n/d')}",
        ],
        [
            "Target ciclo base",
            fmt_price(confluence.get("cycle_target")),
            f"Avanzamento {fmt_pct(confluence.get('price_progress_pct'))}",
        ],
        [
            "Rischio top-cycle RSI",
            confluence.get("label", "n/d"),
            confluence.get("action", "n/d"),
        ],
    ]

    lines = [
        START_MARKER,
        "",
        "---",
        "",
        "# RSI top-cycle warning - SOL",
        "",
        "Report separato completo: [rsi_top_cycle_report.md](rsi_top_cycle_report.md)",
        "",
        "Filtro prudente: usa almeno 3 picchi RSI, separa vicinanza matematica e rischio reale, e non proietta la top-line oltre 12 mesi.",
        "",
        md_table(["Voce", "Valore", "Lettura"], rows),
        "",
        "## Lettura semplice",
        "",
        f"- Weekly: {weekly.get('text', 'n/d')}",
        f"- Monthly: {monthly.get('text', 'n/d')}",
        f"- Confluenza prezzo + RSI: **{confluence.get('label', 'n/d')}**",
        "",
        "Questo non è un segnale di entrata. RSI bassi o trendline non affidabili restano neutrali e non penalizzano il Global Confluence.",
        "",
    ]

    if weekly_ok or monthly_ok:
        lines += ["## Grafici RSI", ""]

        if weekly_ok:
            lines += [f"![SOL weekly RSI top-line]({WEEKLY_CHART_FILE})", ""]

        if monthly_ok:
            lines += [f"![SOL monthly RSI top-line]({MONTHLY_CHART_FILE})", ""]

    lines.append(END_MARKER)
    return "\n".join(lines)


# -----------------------------------------------------------------------------
# Scrittura e integrazione
# -----------------------------------------------------------------------------


def inject_main(block):
    if not os.path.exists(MAIN_REPORT_PATH):
        return

    with open(MAIN_REPORT_PATH, "r", encoding="utf-8") as f:
        current = f.read()

    if START_MARKER in current and END_MARKER in current:
        before = current.split(START_MARKER)[0].rstrip()
        after = current.split(END_MARKER, 1)[1].lstrip()
        current = before + "\n\n" + after

    insert_after = "<!-- BTC_SOL_FRACTAL_END -->"

    if insert_after in current:
        pos = current.find(insert_after) + len(insert_after)
        new_text = (
            current[:pos].rstrip()
            + "\n\n"
            + block.strip()
            + "\n\n"
            + current[pos:].lstrip()
        )
    else:
        new_text = block.strip() + "\n\n" + current.lstrip()

    with open(MAIN_REPORT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(new_text.rstrip() + "\n")


def write_csv(weekly, monthly, confluence, ctx):
    rows = []

    for item in [weekly, monthly]:
        model = item.get("model") or {}
        rows.append(
            {
                "row_type": "period_summary",
                "period": item.get("period"),
                "current_date": item.get("current_date"),
                "current_price": item.get("current_price"),
                "current_rsi": item.get("current_rsi"),
                "line_now": item.get("line_now"),
                "line_now_raw": item.get("line_now_raw"),
                "distance": item.get("distance"),
                "math_status": item.get("math_status"),
                "risk_status": item.get("risk_status"),
                "score": item.get("score"),
                "anchor_count": model.get("anchor_count"),
                "fit_start_date": model.get("fit_start_date"),
                "fit_end_date": model.get("fit_end_date"),
                "slope_per_year": model.get("slope_per_year"),
                "r2": model.get("r2"),
                "rmse": model.get("rmse"),
                "line_quality": item.get("line_quality"),
                "line_quality_reason": item.get("line_quality_reason"),
                "line_operational": item.get("line_operational"),
                "projection_end_date": item.get("projection_end_date"),
                "projection_days": item.get("projection_days"),
                "line_at_projection_end": item.get("line_at_projection_end"),
                "line_at_cycle_top": item.get("line_at_cycle_top"),
                "cycle_projection_status": item.get("cycle_projection_status"),
            }
        )

    for item in [weekly, monthly]:
        anchors = item.get("anchors")
        if anchors is None or anchors.empty:
            continue

        for _, anchor in anchors.iterrows():
            rows.append(
                {
                    "row_type": "anchor",
                    "period": item.get("period"),
                    "anchor_date": fmt_date(anchor.get("date")),
                    "anchor_rsi": safe_float(anchor.get("rsi")),
                    "anchor_price": safe_float(anchor.get("close")),
                }
            )

    rows.append(
        {
            "row_type": "confluence",
            "risk_label": confluence.get("label"),
            "action": confluence.get("action"),
            "weekly_score": confluence.get("weekly_score"),
            "monthly_score": confluence.get("monthly_score"),
            "price_progress_pct": confluence.get("price_progress_pct"),
            "price_bucket": confluence.get("price_bucket"),
            "cycle_target": confluence.get("cycle_target"),
            "cycle_max_base_price": ctx.get("cycle_max_base_price"),
            "cycle_max_base_date": ctx.get("cycle_max_base_date"),
            "cycle_max_beta_price": ctx.get("cycle_max_beta_price"),
        }
    )

    pd.DataFrame(rows).to_csv(CSV_PATH, index=False)


# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------


def main():
    os.makedirs(REPORT_DIR, exist_ok=True)

    daily = download_close(TICKER, DOWNLOAD_START)
    daily = apply_snapshot_to_ohlcv(daily, TICKER)

    if daily.empty:
        with open(REPORT_PATH, "w", encoding="utf-8", newline="\n") as f:
            f.write(
                "# RSI top-cycle warning - SOL\n\n"
                "Dati insufficienti: download prezzi vuoto.\n"
            )
        print("RSI top-cycle report: no data")
        return

    weekly_df = resample_close(daily, "weekly")
    monthly_df = resample_close(daily, "monthly")

    ctx = read_cycle_context()

    cycle_date = None
    if ctx.get("cycle_max_base_date") is not None:
        cycle_date = pd.to_datetime(ctx.get("cycle_max_base_date"), errors="coerce")
        if pd.isna(cycle_date):
            cycle_date = None

    weekly = build_period_summary(
        "weekly",
        weekly_df,
        min_rsi=WEEKLY_MIN_RSI,
        window=WEEKLY_PIVOT_WINDOW,
        cycle_date=cycle_date,
    )

    monthly = build_period_summary(
        "monthly",
        monthly_df,
        min_rsi=MONTHLY_MIN_RSI,
        window=MONTHLY_PIVOT_WINDOW,
        cycle_date=cycle_date,
    )

    current_price = safe_float(daily["Close"].iloc[-1])
    confluence = classify_confluence(weekly, monthly, current_price, ctx)

    weekly_ok = plot_chart("weekly", weekly_df, weekly, ctx, WEEKLY_CHART_PATH)
    monthly_ok = plot_chart("monthly", monthly_df, monthly, ctx, MONTHLY_CHART_PATH)

    report = build_report(weekly, monthly, confluence, ctx, weekly_ok, monthly_ok)

    with open(REPORT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(report.rstrip() + "\n")

    write_csv(weekly, monthly, confluence, ctx)
    inject_main(build_main_block(weekly, monthly, confluence, weekly_ok, monthly_ok))

    print("RSI top-cycle report generated")
    print(f"Weekly RSI chart ok: {weekly_ok} -> {WEEKLY_CHART_PATH}")
    print(f"Monthly RSI chart ok: {monthly_ok} -> {MONTHLY_CHART_PATH}")
    print(f"Weekly line quality: {weekly.get('line_quality')}")
    print(f"Monthly line quality: {monthly.get('line_quality')}")
    print(f"Top-cycle risk: {confluence.get('label')}")


if __name__ == "__main__":
    main()
