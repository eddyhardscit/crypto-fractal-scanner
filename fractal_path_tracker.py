import json
import math
import os
import re
from datetime import datetime, timezone

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import yfinance as yf
from tabulate import tabulate


REPORT_DIR = "reports"
MAIN_REPORT_PATH = os.path.join(REPORT_DIR, "latest_report.md")
REPORT_PATH = os.path.join(REPORT_DIR, "fractal_path_tracker.md")

START_MARKER = "<!-- FRACTAL_PATH_TRACKER_START -->"
END_MARKER = "<!-- FRACTAL_PATH_TRACKER_END -->"

HORIZONS = [7, 14, 30, 60, 90, 120]

TRACKING_INPUT_CANDIDATES = [
    os.path.join(REPORT_DIR, "btc_2022_vs_sol_2026_tracking_history.csv"),
    os.path.join(REPORT_DIR, "btc_2022_vs_sol_2026_history.csv"),
    os.path.join(REPORT_DIR, "sol_btc_fractal_history.csv"),
]

LATEST_JSON_CANDIDATES = [
    os.path.join(REPORT_DIR, "btc_2022_vs_sol_2026_latest.json"),
    os.path.join(REPORT_DIR, "btc_2022_vs_sol_2026_report.json"),
]

PATH_TRACKING_CHART_PATH = os.path.join(REPORT_DIR, "btc_2022_vs_sol_2026_path_tracking_chart.png")
BOTTOM_BACKTEST_CHART_PATH = os.path.join(REPORT_DIR, "btc_2022_vs_sol_2026_bottom_backtest_chart.png")
GAP_60D_CHART_PATH = os.path.join(REPORT_DIR, "btc_2022_vs_sol_2026_gap_60d_chart.png")

FUTURE_DAILY_PROJECTION_CSV = os.path.join(REPORT_DIR, "btc_2022_vs_sol_2026_future_daily_projection.csv")
PROJECTION_LOG_CSV = os.path.join(REPORT_DIR, "btc_2022_vs_sol_2026_projection_log.csv")


def now_utc():
    return datetime.now(timezone.utc)


def today_date():
    return pd.Timestamp.utcnow().normalize().tz_localize(None)


def pick_existing_path(candidates):
    for path in candidates:
        if os.path.exists(path):
            return path
    return None


def read_text(path):
    if not os.path.exists(path):
        return ""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def write_text(path, text):
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def load_json_if_exists(path):
    if not path or not os.path.exists(path):
        return {}
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}


def normalize_columns(df):
    df = df.copy()
    df.columns = [str(c).strip() for c in df.columns]
    return df


def normalize_key(s):
    s = str(s).strip().lower()
    s = s.replace("%", "pct")
    s = s.replace("/", "_")
    s = s.replace("-", "_")
    s = s.replace(".", "")
    s = s.replace(" ", "_")
    s = re.sub(r"[^a-z0-9_àèéìòù]", "", s)
    s = re.sub(r"_+", "_", s)
    return s.strip("_")


def find_col(df, candidates, required=True):
    if df is None or df.empty:
        if required:
            raise KeyError("DataFrame vuoto.")
        return None

    norm_map = {normalize_key(c): c for c in df.columns}

    for cand in candidates:
        c = normalize_key(cand)
        if c in norm_map:
            return norm_map[c]

    if required:
        raise KeyError(
            f"Colonna non trovata. Candidate: {candidates}. "
            f"Colonne disponibili: {list(df.columns)}"
        )

    return None


def pick_value(d, keys, default=None):
    if not isinstance(d, dict):
        return default

    for k in keys:
        if k in d and d[k] is not None:
            return d[k]

    return default


def safe_float(v, default=np.nan):
    try:
        if v is None:
            return default

        if isinstance(v, str):
            s = v.strip()

            if not s or s.lower() in ["nan", "none", "null", "n/a", "na", "n/d"]:
                return default

            s = s.replace("%", "")
            s = s.replace("$", "")
            s = s.replace("€", "")
            s = s.replace("+", "")
            s = s.replace("−", "-")
            s = s.replace(" ", "")

            if "," in s and "." in s:
                s = s.replace(".", "").replace(",", ".")
            elif "," in s:
                s = s.replace(",", ".")

            s = re.sub(r"[^0-9.\-]", "", s)

            if not s or s in ["-", ".", "-."]:
                return default

            return float(s)

        if pd.isna(v):
            return default

        return float(v)

    except Exception:
        return default


def fmt_price(v, decimals=2, dollar=True):
    v = safe_float(v)

    if pd.isna(v):
        return "n/a"

    s = f"{v:,.{decimals}f}"
    s = s.replace(",", "X").replace(".", ",").replace("X", ".")

    if dollar:
        return f"{s} $"

    return s


def fmt_pct(v, decimals=2, signed=False):
    v = safe_float(v)

    if pd.isna(v):
        return "n/a"

    if signed and v > 0:
        return f"+{v:.{decimals}f}%".replace(".", ",")

    return f"{v:.{decimals}f}%".replace(".", ",")


def fmt_int(v):
    try:
        if pd.isna(v):
            return "0"
        return str(int(v))
    except Exception:
        return "0"


def parse_date(value):
    if value is None:
        return pd.NaT

    try:
        dt = pd.to_datetime(value, errors="coerce")

        if pd.isna(dt):
            return pd.NaT

        if getattr(dt, "tzinfo", None) is not None:
            dt = dt.tz_convert(None)

        return pd.Timestamp(dt).normalize()

    except Exception:
        return pd.NaT


def parse_date_series(series):
    out = pd.to_datetime(series, errors="coerce")

    try:
        out = out.dt.tz_localize(None)
    except Exception:
        pass

    return out.dt.normalize()


def df_to_markdown(df):
    if df is None or df.empty:
        return "_Nessun dato disponibile._"

    try:
        return tabulate(df, headers="keys", tablefmt="pipe", showindex=False)
    except Exception:
        return "```csv\n" + df.to_csv(index=False) + "\n```"


def normalize_ohlcv(df):
    if df is None or df.empty:
        return pd.DataFrame()

    out = df.copy()

    if isinstance(out.columns, pd.MultiIndex):
        fields = ["Open", "High", "Low", "Close", "Adj Close", "Volume"]

        level0 = list(out.columns.get_level_values(0))
        level1 = list(out.columns.get_level_values(1))

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

    if "Close" not in out.columns:
        return pd.DataFrame()

    for col in ["Open", "High", "Low"]:
        if col not in out.columns:
            out[col] = out["Close"]

    if "Volume" not in out.columns:
        out["Volume"] = np.nan

    out = out[["Open", "High", "Low", "Close", "Volume"]].copy()
    out.index = pd.to_datetime(out.index, errors="coerce")

    try:
        out.index = out.index.tz_localize(None)
    except Exception:
        pass

    out.index = out.index.normalize()
    out = out[~out.index.duplicated(keep="last")]
    out = out.sort_index()
    out = out.dropna(subset=["Close"])

    return out


def download_prices(ticker, start=None, end=None, period=None):
    try:
        kwargs = {
            "tickers": ticker,
            "interval": "1d",
            "progress": False,
            "auto_adjust": False,
            "actions": False,
            "threads": False,
        }

        if start is not None:
            kwargs["start"] = str(start)

        if end is not None:
            kwargs["end"] = str(end)

        if start is None and period is not None:
            kwargs["period"] = period
        elif start is None and period is None:
            kwargs["period"] = "max"

        raw = yf.download(**kwargs)

        return normalize_ohlcv(raw)

    except Exception as e:
        print(f"Download prezzi fallito per {ticker}: {e}")
        return pd.DataFrame()


def get_close_on_or_before(prices, date):
    if prices is None or prices.empty:
        return np.nan

    date = parse_date(date)

    if pd.isna(date):
        return np.nan

    d = prices[prices.index <= date]

    if d.empty:
        return np.nan

    return safe_float(d.iloc[-1]["Close"])


def get_close_on_or_after(prices, date):
    if prices is None or prices.empty:
        return np.nan

    date = parse_date(date)

    if pd.isna(date):
        return np.nan

    d = prices[prices.index >= date]

    if d.empty:
        return np.nan

    return safe_float(d.iloc[0]["Close"])


def ensure_tracking_dataframe(path):
    if not path or not os.path.exists(path):
        raise FileNotFoundError(
            "Non trovo il file di tracking del frattale. "
            "Controlla che btc_2022_vs_sol_2026_report.py stia salvando uno storico CSV."
        )

    df = pd.read_csv(path)
    df = normalize_columns(df)

    col_day = find_col(
        df,
        ["giorno", "day", "day_index", "index"],
        required=False,
    )

    col_sol_date = find_col(
        df,
        ["data sol", "sol_date", "date_sol", "date", "data"],
        required=False,
    )

    col_btc_eq = find_col(
        df,
        [
            "data btc eq.",
            "data btc eq",
            "btc_equivalent_date",
            "btc_eq_date",
            "btc_date",
            "data btc",
        ],
        required=False,
    )

    col_sol_real = find_col(
        df,
        [
            "sol reale",
            "sol_price_real",
            "sol_real",
            "sol_price",
            "price_real",
            "prezzo sol",
            "prezzo",
            "current_price",
        ],
        required=False,
    )

    col_btc_scaled = find_col(
        df,
        [
            "btc scalato",
            "btc_scaled",
            "btc_scaled_price",
            "scaled_btc_price",
            "btc_scaled_on_sol",
            "btc path",
            "btc_path",
            "fractal_price",
            "prezzo btc scalato",
        ],
        required=False,
    )

    col_error = find_col(
        df,
        [
            "errore",
            "error_pct",
            "error",
            "gap_pct",
            "gap",
            "gap sol btc",
            "gap_sol_btc",
            "differenza",
        ],
        required=False,
    )

    col_phase = find_col(
        df,
        ["fase", "phase", "segment", "programma"],
        required=False,
    )

    if not col_sol_real:
        raise KeyError(
            "Non trovo la colonna del prezzo reale SOL nello storico tracking. "
            f"Colonne disponibili: {list(df.columns)}"
        )

    out = pd.DataFrame()

    if col_day:
        out["day_index"] = pd.to_numeric(df[col_day], errors="coerce")
    else:
        out["day_index"] = np.arange(len(df))

    if col_sol_date:
        out["sol_date"] = parse_date_series(df[col_sol_date])
    else:
        out["sol_date"] = pd.NaT

    if col_btc_eq:
        out["btc_eq_date"] = parse_date_series(df[col_btc_eq])
    else:
        out["btc_eq_date"] = pd.NaT

    out["sol_real"] = pd.to_numeric(df[col_sol_real], errors="coerce")

    if col_btc_scaled:
        out["btc_scaled"] = pd.to_numeric(df[col_btc_scaled], errors="coerce")

    elif col_error:
        error_pct = df[col_error].map(safe_float)
        denominator = 1.0 + (error_pct / 100.0)
        denominator = denominator.replace(0, np.nan)

        out["btc_scaled"] = out["sol_real"] / denominator
        out["error_pct"] = error_pct

        print(
            "Nota: colonna BTC scalato non trovata. "
            f"Ricostruita usando la colonna errore/gap: {col_error}"
        )

    else:
        out["btc_scaled"] = out["sol_real"]
        out["error_pct"] = 0.0

        print(
            "ATTENZIONE: non trovo né BTC scalato né errore/gap nello storico tracking. "
            "Uso fallback neutro: BTC scalato = SOL reale. "
            "Il grafico gap sarà temporaneamente piatto a 0%."
        )

    if "error_pct" not in out.columns:
        out["error_pct"] = ((out["sol_real"] / out["btc_scaled"]) - 1.0) * 100.0

    if col_phase:
        out["phase"] = df[col_phase].astype(str)
    else:
        out["phase"] = "n/a"

    out = out.dropna(subset=["sol_real", "btc_scaled"]).reset_index(drop=True)

    out["day_index"] = pd.to_numeric(out["day_index"], errors="coerce")
    missing_day = out["day_index"].isna()

    if missing_day.any():
        out.loc[missing_day, "day_index"] = out.index[missing_day]

    out["day_index"] = out["day_index"].astype(int)

    out["error_pct"] = ((out["sol_real"] / out["btc_scaled"]) - 1.0) * 100.0
    out["abs_error_pct"] = out["error_pct"].abs()

    return out


def derive_metadata(df, latest_json):
    metadata = {}

    forecast_date = pick_value(
        latest_json,
        ["forecast_date", "data_previsione", "date", "last_date"],
        None,
    )

    sol_bottom_date = pick_value(
        latest_json,
        ["sol_bottom_date", "bottom_sol_date", "bottom_date_sol"],
        None,
    )

    btc_bottom_date = pick_value(
        latest_json,
        ["btc_bottom_date", "bottom_btc_date", "bottom_date_btc"],
        None,
    )

    program_start_date = pick_value(
        latest_json,
        ["program_start_date", "scanner_start_date", "start_program_date"],
        None,
    )

    current_price = pick_value(
        latest_json,
        ["sol_price_today", "price_today", "sol_price", "current_price", "latest_price"],
        None,
    )

    if df is not None and not df.empty:
        if forecast_date is None and "sol_date" in df.columns and df["sol_date"].notna().any():
            forecast_date = df["sol_date"].iloc[-1]

        if sol_bottom_date is None and "sol_date" in df.columns and df["sol_date"].notna().any():
            sol_bottom_date = df["sol_date"].iloc[0]

        if btc_bottom_date is None and "btc_eq_date" in df.columns and df["btc_eq_date"].notna().any():
            btc_bottom_date = df["btc_eq_date"].iloc[0]

        if current_price is None or pd.isna(safe_float(current_price)):
            current_price = safe_float(df["sol_real"].iloc[-1])

    if program_start_date is None:
        program_start_date = "2026-07-03"

    metadata["forecast_date"] = parse_date(forecast_date)
    metadata["sol_bottom_date"] = parse_date(sol_bottom_date)
    metadata["btc_bottom_date"] = parse_date(btc_bottom_date)
    metadata["program_start_date"] = parse_date(program_start_date)
    metadata["current_price"] = safe_float(current_price)

    metadata["verdict"] = pick_value(latest_json, ["verdict", "verdetto"], "n/a")
    metadata["similarity"] = safe_float(
        pick_value(latest_json, ["similarity_total", "somiglianza_totale", "similarity"], np.nan)
    )
    metadata["tracking"] = pick_value(latest_json, ["tracking_status", "tracking"], "n/a")
    metadata["phase"] = pick_value(latest_json, ["phase", "fase"], "n/a")
    metadata["phase_risk"] = pick_value(latest_json, ["phase_risk", "rischio_fase"], "n/a")

    return metadata


def classify_deviation(last_abs_error):
    last_abs_error = safe_float(last_abs_error)

    if pd.isna(last_abs_error):
        return "n/a"

    if last_abs_error <= 5:
        return "MOLTO VICINO AL FRATTALE"

    if last_abs_error <= 10:
        return "DEVIAZIONE CONTENUTA"

    if last_abs_error <= 20:
        return "DEVIAZIONE MODERATA"

    return "DEVIAZIONE FORTE"


def classify_gap(gap):
    gap = safe_float(gap)

    if pd.isna(gap):
        return "n/a"

    if gap >= 15:
        return "SOPRA FRATTALE / MOLTO IN ANTICIPO"

    if gap >= 5:
        return "SOPRA FRATTALE"

    if gap > -5:
        return "IN LINEA"

    if gap > -15:
        return "SOTTO FRATTALE"

    return "SOTTO FRATTALE / MOLTO IN RITARDO"


def build_daily_fractal_projection(df, metadata):
    forecast_date = metadata.get("forecast_date", pd.NaT)
    sol_bottom_date = metadata.get("sol_bottom_date", pd.NaT)
    btc_bottom_date = metadata.get("btc_bottom_date", pd.NaT)
    start_price = safe_float(metadata.get("current_price", np.nan))

    if pd.isna(forecast_date) and df is not None and not df.empty and df["sol_date"].notna().any():
        forecast_date = df["sol_date"].iloc[-1]

    if pd.isna(sol_bottom_date) and df is not None and not df.empty and df["sol_date"].notna().any():
        sol_bottom_date = df["sol_date"].iloc[0]

    if pd.isna(btc_bottom_date) and df is not None and not df.empty and df["btc_eq_date"].notna().any():
        btc_bottom_date = df["btc_eq_date"].iloc[0]

    if pd.isna(start_price) and df is not None and not df.empty:
        start_price = safe_float(df["sol_real"].iloc[-1])

    if pd.isna(forecast_date) or pd.isna(sol_bottom_date) or pd.isna(btc_bottom_date) or pd.isna(start_price):
        return pd.DataFrame()

    day_from_bottom_today = int((forecast_date - sol_bottom_date).days)
    btc_equivalent_today = btc_bottom_date + pd.Timedelta(days=day_from_bottom_today)
    max_forward_days = max(HORIZONS)

    btc_start = (btc_equivalent_today - pd.Timedelta(days=5)).strftime("%Y-%m-%d")
    btc_end = (btc_equivalent_today + pd.Timedelta(days=max_forward_days + 10)).strftime("%Y-%m-%d")

    btc_prices = download_prices("BTC-USD", start=btc_start, end=btc_end)

    if btc_prices.empty:
        return pd.DataFrame()

    btc_today_price = get_close_on_or_before(btc_prices, btc_equivalent_today)

    if pd.isna(btc_today_price) or btc_today_price == 0:
        return pd.DataFrame()

    rows = []

    for forward_day in range(0, max_forward_days + 1):
        target_sol_date = forecast_date + pd.Timedelta(days=forward_day)
        target_btc_date = btc_equivalent_today + pd.Timedelta(days=forward_day)

        btc_future_price = get_close_on_or_before(btc_prices, target_btc_date)

        if pd.isna(btc_future_price):
            continue

        projected_base = start_price * (btc_future_price / btc_today_price)

        rows.append({
            "forecast_date": forecast_date.strftime("%Y-%m-%d"),
            "forward_day": forward_day,
            "target_sol_date": target_sol_date.strftime("%Y-%m-%d"),
            "target_btc_date": target_btc_date.strftime("%Y-%m-%d"),
            "btc_today_price": btc_today_price,
            "btc_future_price": btc_future_price,
            "sol_start_price": start_price,
            "projected_base": projected_base,
        })

    out = pd.DataFrame(rows)

    if out.empty:
        return out

    out["path_min"] = out["projected_base"].cummin()
    out["path_max"] = out["projected_base"].cummax()

    out.to_csv(FUTURE_DAILY_PROJECTION_CSV, index=False)

    return out


def build_milestones_from_daily_projection(daily_projection):
    if daily_projection is None or daily_projection.empty:
        return pd.DataFrame()

    rows = []

    for h in HORIZONS:
        d = daily_projection[daily_projection["forward_day"] == h].copy()

        if d.empty:
            d = daily_projection[daily_projection["forward_day"] <= h].tail(1).copy()

        if d.empty:
            continue

        r = d.iloc[0]

        base = safe_float(r["projected_base"])
        min_path = safe_float(r["path_min"])
        max_path = safe_float(r["path_max"])
        start_price = safe_float(r["sol_start_price"])

        btc_move = np.nan

        if not pd.isna(start_price) and start_price != 0:
            btc_move = (base / start_price - 1.0) * 100.0

        rows.append({
            "horizon_days": h,
            "label": f"{h}g",
            "target_date": r["target_sol_date"],
            "btc_did_pct": btc_move,
            "base_fractal": base,
            "min_path": min_path,
            "max_path": max_path,
        })

    return pd.DataFrame(rows)


def append_and_check_projection_log(milestones):
    if milestones is None or milestones.empty:
        return pd.DataFrame(), pd.DataFrame()

    first_horizon = int(milestones["horizon_days"].iloc[0])
    forecast_date_dt = parse_date(milestones["target_date"].iloc[0]) - pd.Timedelta(days=first_horizon)
    forecast_date = forecast_date_dt.strftime("%Y-%m-%d")

    new_rows = []

    for _, r in milestones.iterrows():
        new_rows.append({
            "forecast_date": forecast_date,
            "horizon_days": int(r["horizon_days"]),
            "target_date": r["target_date"],
            "base_fractal": safe_float(r["base_fractal"]),
            "min_path": safe_float(r["min_path"]),
            "max_path": safe_float(r["max_path"]),
            "checked": "no",
            "real_price": np.nan,
            "error_pct": np.nan,
            "inside_band": "n/a",
        })

    new_df = pd.DataFrame(new_rows)

    if os.path.exists(PROJECTION_LOG_CSV):
        try:
            old = pd.read_csv(PROJECTION_LOG_CSV)
        except Exception:
            old = pd.DataFrame()
    else:
        old = pd.DataFrame()

    if old.empty:
        log_df = new_df.copy()
    else:
        for col in new_df.columns:
            if col not in old.columns:
                old[col] = np.nan

        key_cols = ["forecast_date", "horizon_days"]

        old_key = old[key_cols].astype(str).agg("|".join, axis=1)
        new_key = new_df[key_cols].astype(str).agg("|".join, axis=1)

        old = old[~old_key.isin(set(new_key))]
        log_df = pd.concat([old, new_df], ignore_index=True)

    today = today_date()

    unchecked = log_df[log_df["checked"].astype(str).str.lower() != "yes"].copy()

    if not unchecked.empty:
        min_target = pd.to_datetime(unchecked["target_date"], errors="coerce").min()

        if pd.notna(min_target):
            sol_prices = download_prices(
                "SOL-USD",
                start=(min_target - pd.Timedelta(days=5)).strftime("%Y-%m-%d"),
                end=(today + pd.Timedelta(days=2)).strftime("%Y-%m-%d"),
            )
        else:
            sol_prices = pd.DataFrame()

        if not sol_prices.empty:
            for idx, row in log_df.iterrows():
                if str(row.get("checked", "")).lower() == "yes":
                    continue

                target_date = parse_date(row.get("target_date"))

                if pd.isna(target_date) or target_date > today:
                    continue

                real_price = get_close_on_or_after(sol_prices, target_date)
                base = safe_float(row.get("base_fractal", np.nan))
                min_path = safe_float(row.get("min_path", np.nan))
                max_path = safe_float(row.get("max_path", np.nan))

                if pd.isna(real_price) or pd.isna(base) or base == 0:
                    continue

                error_pct = (real_price / base - 1.0) * 100.0

                inside = "yes"

                if not pd.isna(min_path) and real_price < min_path:
                    inside = "no"

                if not pd.isna(max_path) and real_price > max_path:
                    inside = "no"

                log_df.at[idx, "checked"] = "yes"
                log_df.at[idx, "real_price"] = real_price
                log_df.at[idx, "error_pct"] = error_pct
                log_df.at[idx, "inside_band"] = inside

    log_df.to_csv(PROJECTION_LOG_CSV, index=False)

    latest_rows = log_df[log_df["forecast_date"].astype(str) == str(forecast_date)].copy()

    return log_df, latest_rows


def build_projection_accuracy(log_df):
    if log_df is None or log_df.empty:
        return pd.DataFrame()

    checked = log_df[log_df["checked"].astype(str).str.lower() == "yes"].copy()

    rows = []

    for h in HORIZONS:
        d = checked[pd.to_numeric(checked["horizon_days"], errors="coerce") == h].copy()

        if d.empty:
            rows.append({
                "Orizzonte": f"{h}g",
                "Controlli": 0,
                "Dentro banda": "n/a",
                "Errore medio assoluto": "n/a",
                "Errore medio": "n/a",
            })
            continue

        inside = d["inside_band"].astype(str).str.lower().eq("yes").mean() * 100.0
        errors = pd.to_numeric(d["error_pct"], errors="coerce")

        rows.append({
            "Orizzonte": f"{h}g",
            "Controlli": len(d),
            "Dentro banda": fmt_pct(inside),
            "Errore medio assoluto": fmt_pct(errors.abs().mean()),
            "Errore medio": fmt_pct(errors.mean(), signed=True),
        })

    return pd.DataFrame(rows)


def generate_bottom_backtest_chart(df):
    if df is None or df.empty:
        return

    x = df["sol_date"] if df["sol_date"].notna().any() else df["day_index"]

    plt.figure(figsize=(12, 6))
    plt.plot(x, df["sol_real"], label="SOL reale")
    plt.plot(x, df["btc_scaled"], label="BTC scalato su SOL", linestyle="--")
    plt.title("Backtest dal bottom: SOL reale vs BTC scalato")
    plt.xlabel("Data SOL" if df["sol_date"].notna().any() else "Giorni dal bottom")
    plt.ylabel("Prezzo SOL")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig(BOTTOM_BACKTEST_CHART_PATH, dpi=160)
    plt.close()


def generate_path_tracking_chart(df, daily_projection):
    if df is None or df.empty:
        return

    plt.figure(figsize=(12, 6))

    x_real = df["sol_date"] if df["sol_date"].notna().any() else df["day_index"]

    plt.plot(x_real, df["sol_real"], label="SOL reale")
    plt.plot(x_real, df["btc_scaled"], label="BTC scalato su SOL", linestyle="--")

    if daily_projection is not None and not daily_projection.empty:
        future_dates = pd.to_datetime(daily_projection["target_sol_date"], errors="coerce")

        plt.plot(
            future_dates,
            daily_projection["projected_base"],
            label="Proiezione frattale giornaliera",
            linestyle="-.",
        )

        plt.plot(
            future_dates,
            daily_projection["path_min"],
            label="Min percorso futuro",
            linestyle=":",
            linewidth=1,
        )

        plt.plot(
            future_dates,
            daily_projection["path_max"],
            label="Max percorso futuro",
            linestyle=":",
            linewidth=1,
        )

        try:
            plt.fill_between(
                future_dates,
                daily_projection["path_min"].astype(float),
                daily_projection["path_max"].astype(float),
                alpha=0.10,
            )
        except Exception:
            pass

    if len(df) >= 1:
        last_x = x_real.iloc[-1]
        last_y = df["sol_real"].iloc[-1]
        plt.scatter([last_x], [last_y], s=50)

        try:
            plt.annotate("Oggi SOL", (last_x, last_y), xytext=(10, 10), textcoords="offset points")
        except Exception:
            pass

    plt.title("Tracking percorso frattale BTC 2022 vs SOL 2026")
    plt.xlabel("Data SOL" if df["sol_date"].notna().any() else "Giorni dal bottom")
    plt.ylabel("Prezzo SOL")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig(PATH_TRACKING_CHART_PATH, dpi=160)
    plt.close()


def generate_gap_60d_chart(df):
    if df is None or df.empty:
        return pd.DataFrame()

    gap_df = df.copy()
    gap_df["gap_pct"] = ((gap_df["sol_real"] / gap_df["btc_scaled"]) - 1.0) * 100.0
    gap_df = gap_df.tail(60).copy()

    if gap_df.empty:
        return gap_df

    gap_df["gap_ma7"] = gap_df["gap_pct"].rolling(7, min_periods=1).mean()

    x = gap_df["sol_date"] if gap_df["sol_date"].notna().any() else gap_df["day_index"]

    plt.figure(figsize=(12, 6))

    plt.axhline(0, linestyle="--", linewidth=1, color="black", alpha=0.7)

    try:
        plt.fill_between(
            x,
            gap_df["gap_pct"],
            0,
            where=gap_df["gap_pct"] >= 0,
            alpha=0.18,
            color="green",
            interpolate=True,
            label="SOL sopra BTC scalato",
        )

        plt.fill_between(
            x,
            gap_df["gap_pct"],
            0,
            where=gap_df["gap_pct"] < 0,
            alpha=0.18,
            color="red",
            interpolate=True,
            label="SOL sotto BTC scalato",
        )
    except Exception:
        pass

    plt.plot(x, gap_df["gap_pct"], label="Gap % giornaliero", color="blue", linewidth=1.5)
    plt.plot(x, gap_df["gap_ma7"], label="Media mobile 7g", color="orange", linewidth=2.2)

    last_x = x.iloc[-1]
    last_gap = safe_float(gap_df["gap_pct"].iloc[-1])

    plt.scatter([last_x], [last_gap], s=85, color="black", zorder=5)

    try:
        plt.annotate(
            f"Oggi {last_gap:+.2f}%".replace(".", ","),
            (last_x, last_gap),
            xytext=(12, 12),
            textcoords="offset points",
            fontsize=11,
            fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="black", alpha=0.85),
        )
    except Exception:
        pass

    plt.title("Gap SOL vs BTC scalato - ultimi 60 giorni")
    plt.xlabel("Data SOL" if gap_df["sol_date"].notna().any() else "Giorni")
    plt.ylabel("Gap % = SOL reale vs BTC scalato")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig(GAP_60D_CHART_PATH, dpi=160)
    plt.close()

    return gap_df


def build_recent_table(df, rows=10):
    if df is None or df.empty:
        return pd.DataFrame()

    tail = df.tail(rows).copy()

    if tail["sol_date"].notna().any():
        sol_dates = tail["sol_date"].dt.strftime("%Y-%m-%d")
    else:
        sol_dates = ["n/a"] * len(tail)

    if tail["btc_eq_date"].notna().any():
        btc_dates = tail["btc_eq_date"].dt.strftime("%Y-%m-%d")
    else:
        btc_dates = ["n/a"] * len(tail)

    display = pd.DataFrame({
        "Giorno": tail["day_index"].astype(int),
        "Data SOL": sol_dates,
        "Data BTC eq.": btc_dates,
        "SOL reale": [fmt_price(v) for v in tail["sol_real"]],
        "BTC scalato": [fmt_price(v) for v in tail["btc_scaled"]],
        "Errore": [fmt_pct(v, signed=True) for v in tail["error_pct"]],
        "Fase": tail["phase"].astype(str),
    })

    return display


def build_milestone_table(milestones, latest_projection_rows):
    rows = []

    if latest_projection_rows is not None and not latest_projection_rows.empty:
        for _, r in latest_projection_rows.iterrows():
            h = int(safe_float(r.get("horizon_days", np.nan)))

            rows.append({
                "Orizzonte": f"{h}g",
                "Data target": str(r.get("target_date", "")),
                "Base frattale": fmt_price(r.get("base_fractal", np.nan)),
                "Min percorso": fmt_price(r.get("min_path", np.nan)),
                "Max percorso": fmt_price(r.get("max_path", np.nan)),
                "Controllato": r.get("checked", "no"),
                "Prezzo reale": fmt_price(r.get("real_price", np.nan)),
                "Errore": fmt_pct(r.get("error_pct", np.nan), signed=True),
                "Dentro banda": r.get("inside_band", "n/a"),
            })

    elif milestones is not None and not milestones.empty:
        for _, r in milestones.iterrows():
            rows.append({
                "Orizzonte": r.get("label", f"{int(r.get('horizon_days'))}g"),
                "Data target": r.get("target_date", "n/a"),
                "Base frattale": fmt_price(r.get("base_fractal", np.nan)),
                "Min percorso": fmt_price(r.get("min_path", np.nan)),
                "Max percorso": fmt_price(r.get("max_path", np.nan)),
                "Controllato": "no",
                "Prezzo reale": "n/a",
                "Errore": "n/a",
                "Dentro banda": "n/a",
            })

    return pd.DataFrame(rows)


def build_gap_summary(gap_df):
    if gap_df is None or gap_df.empty:
        return {
            "last_gap": np.nan,
            "ma7": np.nan,
            "prev_ma7": np.nan,
            "gap_state": "n/a",
            "gap_trend": "n/a",
        }

    last_gap = safe_float(gap_df["gap_pct"].iloc[-1])
    ma7 = safe_float(gap_df["gap_pct"].tail(7).mean())

    if len(gap_df) >= 14:
        prev_ma7 = safe_float(gap_df["gap_pct"].tail(14).head(7).mean())
    else:
        prev_ma7 = safe_float(gap_df["gap_pct"].head(max(len(gap_df) - 7, 1)).mean())

    gap_state = classify_gap(last_gap)

    if pd.isna(ma7) or pd.isna(prev_ma7):
        gap_trend = "n/a"
    elif ma7 > prev_ma7 + 1:
        gap_trend = "SOL si sta rafforzando rispetto al frattale"
    elif ma7 < prev_ma7 - 1:
        gap_trend = "SOL si sta indebolendo rispetto al frattale"
    else:
        gap_trend = "Gap abbastanza stabile"

    return {
        "last_gap": last_gap,
        "ma7": ma7,
        "prev_ma7": prev_ma7,
        "gap_state": gap_state,
        "gap_trend": gap_trend,
    }


def build_report(df, metadata, daily_projection, milestones, log_df, latest_projection_rows, gap_df):
    generated = now_utc().strftime("%Y-%m-%d %H:%M UTC")

    forecast_date = metadata["forecast_date"]
    sol_bottom_date = metadata["sol_bottom_date"]
    btc_bottom_date = metadata["btc_bottom_date"]
    program_start_date = metadata["program_start_date"]

    if pd.notna(program_start_date) and df is not None and not df.empty and df["sol_date"].notna().any():
        from_program_df = df[df["sol_date"] >= program_start_date].copy()
    else:
        from_program_df = pd.DataFrame()

    total_days = len(df)
    from_program_days = len(from_program_df)
    last_7_df = df.tail(7).copy()

    mean_abs_full = df["abs_error_pct"].mean() if not df.empty else np.nan
    mean_abs_7 = last_7_df["abs_error_pct"].mean() if not last_7_df.empty else np.nan
    mean_abs_program = from_program_df["abs_error_pct"].mean() if not from_program_df.empty else np.nan
    last_error = df["error_pct"].iloc[-1] if not df.empty else np.nan
    deviation_state = classify_deviation(abs(last_error))

    gap_summary = build_gap_summary(gap_df)

    recent_table = build_recent_table(df)
    milestone_table = build_milestone_table(milestones, latest_projection_rows)
    accuracy_table = build_projection_accuracy(log_df)

    report = f"""{START_MARKER}
# Tracking percorso frattale SOL/BTC

Generato: {generated}

Questo report controlla se SOL sta seguendo il percorso previsto dal frattale BTC 2022 vs SOL 2026.

Ora il controllo è diviso in quattro parti:

- confronto dal bottom: BTC 2022 scalato contro SOL reale
- tratto da inizio programma/scanner: verifica se il tracking recente sta reggendo
- proiezione futura giornaliera: BTC 2022 viene scalato giorno per giorno su SOL
- grafico gap: differenza leggibile tra SOL reale e BTC scalato

## Stato ultimo frattale salvato

- Data previsione: **{forecast_date.strftime("%Y-%m-%d") if pd.notna(forecast_date) else "n/a"}**
- Bottom SOL usato: **{sol_bottom_date.strftime("%Y-%m-%d") if pd.notna(sol_bottom_date) else "n/a"}**
- Bottom BTC 2022 equivalente: **{btc_bottom_date.strftime("%Y-%m-%d") if pd.notna(btc_bottom_date) else "n/a"}**
- Inizio programma/scanner rilevato: **{program_start_date.strftime("%Y-%m-%d") if pd.notna(program_start_date) else "n/a"}**
- Prezzo iniziale SOL: **{fmt_price(metadata.get("current_price", np.nan))}**
- Verdetto: **{metadata.get("verdict", "n/a")}**
- Somiglianza: **{fmt_pct(metadata.get("similarity", np.nan))}**
- Tracking: **{metadata.get("tracking", "n/a")}**
- Fase: **{metadata.get("phase", "n/a")}**
- Rischio fase: **{metadata.get("phase_risk", "n/a")}**

## Confronto dal bottom a oggi

- Giorni controllati dal bottom: **{total_days}**
- Giorni controllati da inizio programma/scanner: **{from_program_days}**
- Errore medio assoluto dal bottom: **{fmt_pct(mean_abs_full)}**
- Errore medio assoluto ultimi 7 giorni: **{fmt_pct(mean_abs_7)}**
- Errore medio assoluto da inizio programma/scanner: **{fmt_pct(mean_abs_program)}**
- Errore ultimo giorno: **{fmt_pct(last_error, signed=True)}**
- Stato: **{deviation_state}**

## Grafico completo: bottom, inizio programma e proiezione giornaliera

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato - ultimi 60 giorni

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap: **{fmt_pct(gap_summary["last_gap"], signed=True)}**
- Media mobile 7g gap: **{fmt_pct(gap_summary["ma7"], signed=True)}**
- Stato gap: **{gap_summary["gap_state"]}**
- Trend gap: **{gap_summary["gap_trend"]}**

Come leggerlo:

- **Sopra 0%** = SOL è sopra il percorso BTC scalato.
- **Sotto 0%** = SOL è sotto il percorso BTC scalato.
- Se il gap sale, SOL si sta rafforzando rispetto al frattale.
- Se il gap scende, SOL si sta indebolendo rispetto al frattale.
- Questo è il grafico più leggibile per capire subito se SOL si sta orientando sopra o sotto il frattale.

## Ultimi giorni del confronto dal bottom

{df_to_markdown(recent_table)}

## Proiezione futura salvata

{df_to_markdown(milestone_table)}

Nota: la tabella sopra mostra solo le milestone principali. Il grafico invece usa la proiezione giornaliera del frattale BTC scalato su SOL.

## Accuratezza storica della proiezione futura

{df_to_markdown(accuracy_table)}

## Come leggerlo

- BTC 2022 scalato su SOL è il percorso che SOL dovrebbe seguire se il frattale resta valido.
- SOL reale mostra cosa ha fatto davvero dal bottom.
- La linea di inizio programma/scanner separa il backtest retroattivo dalla parte che stiamo monitorando davvero giorno per giorno.
- Se SOL resta vicino a BTC scalato, il frattale è in linea.
- Se SOL sta sopra BTC scalato, il frattale è in anticipo o più forte.
- Se SOL sta sotto BTC scalato, il frattale è in ritardo o più debole.
- Il grafico gap ultimi 60 giorni serve proprio per vedere meglio questa differenza.
- La proiezione futura va letta insieme alle conferme e invalidazioni del report frattale principale.
{END_MARKER}
"""
    return report


def replace_section_in_latest_report(section_text):
    if not os.path.exists(MAIN_REPORT_PATH):
        write_text(MAIN_REPORT_PATH, section_text)
        return

    content = read_text(MAIN_REPORT_PATH)

    if START_MARKER in content and END_MARKER in content:
        start_idx = content.index(START_MARKER)
        end_idx = content.index(END_MARKER) + len(END_MARKER)
        new_content = content[:start_idx] + section_text + content[end_idx:]
    else:
        if not content.endswith("\n"):
            content += "\n"
        new_content = content + "\n" + section_text

    write_text(MAIN_REPORT_PATH, new_content)


def main():
    os.makedirs(REPORT_DIR, exist_ok=True)

    tracking_path = pick_existing_path(TRACKING_INPUT_CANDIDATES)
    latest_json_path = pick_existing_path(LATEST_JSON_CANDIDATES)

    df = ensure_tracking_dataframe(tracking_path)
    latest_json = load_json_if_exists(latest_json_path)
    metadata = derive_metadata(df, latest_json)

    daily_projection = build_daily_fractal_projection(df, metadata)
    milestones = build_milestones_from_daily_projection(daily_projection)
    projection_log, latest_projection_rows = append_and_check_projection_log(milestones)

    generate_bottom_backtest_chart(df)
    generate_path_tracking_chart(df, daily_projection)
    gap_df = generate_gap_60d_chart(df)

    report_text = build_report(
        df=df,
        metadata=metadata,
        daily_projection=daily_projection,
        milestones=milestones,
        log_df=projection_log,
        latest_projection_rows=latest_projection_rows,
        gap_df=gap_df,
    )

    write_text(REPORT_PATH, report_text)
    replace_section_in_latest_report(report_text)

    print(f"Report scritto in: {REPORT_PATH}")
    print(f"Latest report aggiornato: {MAIN_REPORT_PATH}")
    print(f"Grafico tracking salvato in: {PATH_TRACKING_CHART_PATH}")
    print(f"Grafico backtest salvato in: {BOTTOM_BACKTEST_CHART_PATH}")
    print(f"Grafico gap 60d salvato in: {GAP_60D_CHART_PATH}")
    print(f"CSV proiezione giornaliera salvato in: {FUTURE_DAILY_PROJECTION_CSV}")
    print(f"CSV log proiezioni salvato in: {PROJECTION_LOG_CSV}")


if __name__ == "__main__":
    main()
