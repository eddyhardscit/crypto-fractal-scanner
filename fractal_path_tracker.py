from pathlib import Path
from datetime import datetime, timezone
import re

import numpy as np
import pandas as pd
import yfinance as yf

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


REPORTS_DIR = Path("reports")
LATEST_REPORT = REPORTS_DIR / "latest_report.md"
FRACTAL_REPORT = REPORTS_DIR / "btc_2022_vs_sol_2026_report.md"

FORECAST_LOG = REPORTS_DIR / "fractal_path_forecasts.csv"
ACCURACY_METRICS = REPORTS_DIR / "fractal_path_accuracy_metrics.csv"
OUTPUT_REPORT = REPORTS_DIR / "fractal_path_accuracy_report.md"

TRACKING_CHART = REPORTS_DIR / "btc_2022_vs_sol_2026_path_tracking_chart.png"
ERROR_CHART = REPORTS_DIR / "btc_2022_vs_sol_2026_path_error_chart.png"
BOTTOM_BACKTEST_CHART = REPORTS_DIR / "btc_2022_vs_sol_2026_bottom_backtest_chart.png"
BOTTOM_BACKTEST_CSV = REPORTS_DIR / "btc_2022_vs_sol_2026_bottom_backtest.csv"

START_MARKER = "<!-- FRACTAL_PATH_TRACKER_START -->"
END_MARKER = "<!-- FRACTAL_PATH_TRACKER_END -->"

ASSET = "SOL"
SOL_TICKER = "SOL-USD"
BTC_TICKER = "BTC-USD"
SOURCE = "BTC_2022_vs_SOL_2026"
HORIZONS = [7, 14, 30, 60, 90, 120]

ITALIAN_MONTHS = {
    "gennaio": "January",
    "febbraio": "February",
    "marzo": "March",
    "aprile": "April",
    "maggio": "May",
    "giugno": "June",
    "luglio": "July",
    "agosto": "August",
    "settembre": "September",
    "ottobre": "October",
    "novembre": "November",
    "dicembre": "December",
}


def utc_now():
    return datetime.now(timezone.utc)


def today_str():
    return utc_now().strftime("%Y-%m-%d")


def safe_float(x):
    try:
        if pd.isna(x):
            return np.nan
        return float(x)
    except Exception:
        return np.nan


def parse_number(value):
    if value is None:
        return np.nan

    s = str(value).strip()

    if not s or s.lower() == "nan":
        return np.nan

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
        return np.nan

    try:
        return float(s)
    except Exception:
        return np.nan


def parse_pct(value):
    if value is None:
        return np.nan

    s = str(value).strip()
    s = s.replace("%", "")
    s = s.replace("+", "")
    s = s.replace("−", "-")
    s = s.replace(",", ".")
    s = re.sub(r"[^0-9.\-]", "", s)

    if not s or s in ["-", ".", "-."]:
        return np.nan

    try:
        return float(s)
    except Exception:
        return np.nan


def parse_italian_date(value):
    if value is None:
        return pd.NaT

    s = str(value).strip().lower()
    s = s.replace(",", " ")
    s = re.sub(r"\s+", " ", s)

    for it_month, en_month in ITALIAN_MONTHS.items():
        s = re.sub(rf"\b{it_month}\b", en_month, s, flags=re.IGNORECASE)

    return pd.to_datetime(s, errors="coerce", dayfirst=True)


def fmt_pct(x):
    x = safe_float(x)

    if pd.isna(x):
        return "n/a"

    return f"{x:.2f}%".replace(".", ",")


def fmt_price(x):
    x = safe_float(x)

    if pd.isna(x):
        return "n/a"

    return f"{x:.2f} $".replace(".", ",")


def df_to_markdown(df):
    if df is None or df.empty:
        return "_Nessun dato disponibile._"

    try:
        return df.to_markdown(index=False)
    except Exception:
        return "```csv\n" + df.to_csv(index=False) + "\n```"


def read_text(path):
    if not path.exists():
        return ""

    try:
        return path.read_text(encoding="utf-8")
    except Exception:
        return ""


def clean_text(s):
    if s is None:
        return ""

    s = str(s)
    s = s.replace("**", "")
    s = s.replace("__", "")
    s = s.replace("`", "")
    s = s.replace("|", " ")
    s = re.sub(r"\s+", " ", s)

    return s.strip()


def extract_fractal_section():
    latest = read_text(LATEST_REPORT)

    if "<!-- BTC_SOL_FRACTAL_START -->" in latest and "<!-- BTC_SOL_FRACTAL_END -->" in latest:
        start = latest.find("<!-- BTC_SOL_FRACTAL_START -->")
        end = latest.find("<!-- BTC_SOL_FRACTAL_END -->")

        if end > start:
            return latest[start:end]

    return read_text(FRACTAL_REPORT)


def line_value(section, label):
    label_low = label.lower()

    for line in section.splitlines():
        clean = clean_text(line)

        if label_low in clean.lower():
            if ":" in clean:
                return clean.split(":", 1)[-1].strip()

            return clean

    return ""


def first_price(text):
    if not text:
        return np.nan

    m = re.search(r"([0-9]+(?:[\.,][0-9]+)?)\s*\$", str(text))

    if m:
        return parse_number(m.group(1))

    return np.nan


def first_pct(text):
    if not text:
        return np.nan

    m = re.search(r"([+\-]?[0-9]+(?:[\.,][0-9]+)?)\s*%", str(text))

    if m:
        return parse_pct(m.group(1))

    return np.nan


def first_int(text):
    if not text:
        return np.nan

    m = re.search(r"([0-9]+)", str(text))

    if m:
        return int(m.group(1))

    return np.nan


def normalize_price_from_cell(cell):
    if "$" in str(cell):
        return first_price(cell)

    return parse_number(cell)


def parse_markdown_table_after_heading(section, heading_text):
    lines = section.splitlines()
    start = None

    for i, line in enumerate(lines):
        if heading_text.lower() in line.lower():
            start = i
            break

    if start is None:
        return pd.DataFrame()

    table_lines = []
    found_table = False

    for line in lines[start + 1:]:
        if line.strip().startswith("|"):
            found_table = True
            table_lines.append(line.strip())
        elif found_table:
            break

    if len(table_lines) < 3:
        return pd.DataFrame()

    header = [clean_text(c) for c in table_lines[0].strip("|").split("|")]
    data_lines = table_lines[2:]

    rows = []

    for line in data_lines:
        cells = [clean_text(c) for c in line.strip("|").split("|")]

        if len(cells) != len(header):
            continue

        rows.append(dict(zip(header, cells)))

    return pd.DataFrame(rows)


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


def download_prices(ticker, start=None):
    try:
        kwargs = {
            "tickers": ticker,
            "interval": "1d",
            "progress": False,
            "auto_adjust": False,
            "actions": False,
            "threads": False,
        }

        if start:
            kwargs["start"] = start
        else:
            kwargs["period"] = "max"

        raw = yf.download(**kwargs)

        return normalize_ohlcv(raw)

    except Exception as e:
        print(f"Download prezzi fallito per {ticker}: {e}")
        return pd.DataFrame()


def current_price_from_market():
    df = download_prices(SOL_TICKER, start="2020-01-01")

    if df.empty:
        return np.nan

    return safe_float(df["Close"].iloc[-1])


def actual_price_on_or_after(df, date):
    if df.empty:
        return np.nan

    date = pd.to_datetime(date).normalize()
    d = df[df.index >= date]

    if d.empty:
        return np.nan

    return safe_float(d.iloc[0]["Close"])


def infer_program_start_date():
    candidates = []

    known_logs = [
        REPORTS_DIR / "fractal_path_forecasts.csv",
        REPORTS_DIR / "module_signal_log.csv",
        REPORTS_DIR / "scanner_forecast_path_log.csv",
        REPORTS_DIR / "prediction_log.csv",
        REPORTS_DIR / "predictions_log.csv",
        REPORTS_DIR / "forecast_log.csv",
        REPORTS_DIR / "forecast_history.csv",
        REPORTS_DIR / "scanner_prediction_log.csv",
        REPORTS_DIR / "scanner_predictions.csv",
        REPORTS_DIR / "scanner_prediction_history.csv",
    ]

    date_columns = [
        "forecast_date",
        "prediction_date",
        "date",
        "created_at",
        "created_at_utc",
    ]

    for path in known_logs:
        if not path.exists():
            continue

        try:
            df = pd.read_csv(path)
        except Exception:
            continue

        for col in date_columns:
            if col not in df.columns:
                continue

            dates = pd.to_datetime(df[col], errors="coerce")
            dates = dates.dropna()

            if not dates.empty:
                candidates.append(dates.min().normalize())

    latest_text = read_text(LATEST_REPORT)

    if latest_text:
        checks = re.findall(r"Prossimo controllo\s*\|\s*([0-9]{4}-[0-9]{2}-[0-9]{2})", latest_text)

        for c in checks:
            dt = pd.to_datetime(c, errors="coerce")

            if not pd.isna(dt):
                candidates.append((dt - pd.Timedelta(days=30)).normalize())

        checks2 = re.findall(r"Prossimo controllo[^0-9]*([0-9]{4}-[0-9]{2}-[0-9]{2})", latest_text)

        for c in checks2:
            dt = pd.to_datetime(c, errors="coerce")

            if not pd.isna(dt):
                candidates.append((dt - pd.Timedelta(days=30)).normalize())

    if not candidates:
        return pd.NaT

    return min(candidates)


def infer_bottom_date(meta):
    last_dt = pd.to_datetime(meta.get("last_candle_date", pd.NaT), errors="coerce")
    day_from_bottom = safe_float(meta.get("day_from_bottom", np.nan))

    if pd.isna(last_dt) or pd.isna(day_from_bottom):
        return pd.to_datetime(meta["forecast_date"])

    return (last_dt.normalize() - pd.Timedelta(days=int(day_from_bottom))).normalize()


def infer_btc_bottom_date(meta):
    btc_equiv = pd.to_datetime(meta.get("btc_equivalent_date", pd.NaT), errors="coerce")
    day_from_bottom = safe_float(meta.get("day_from_bottom", np.nan))

    if pd.isna(btc_equiv) or pd.isna(day_from_bottom):
        return pd.to_datetime("2022-11-21")

    return (btc_equiv.normalize() - pd.Timedelta(days=int(day_from_bottom))).normalize()


def parse_fractal_forecast():
    section = extract_fractal_section()

    if not section:
        return pd.DataFrame(), {}

    meta = {
        "forecast_date": today_str(),
        "created_at_utc": utc_now().strftime("%Y-%m-%d %H:%M:%S UTC"),
        "asset": ASSET,
        "ticker": SOL_TICKER,
        "source": SOURCE,
        "verdict": "",
        "similarity": np.nan,
        "tracking": "",
        "phase": "",
        "risk": "",
        "start_price": np.nan,
        "last_candle_date": pd.NaT,
        "day_from_bottom": np.nan,
        "sol_bottom_date": pd.NaT,
        "btc_equivalent_date": pd.NaT,
        "btc_bottom_date": pd.NaT,
        "program_start_date": pd.NaT,
        "sol_bottom_price": np.nan,
        "btc_bottom_price": np.nan,
        "first_confirmation": np.nan,
        "second_confirmation": np.nan,
        "soft_invalidation": np.nan,
        "strong_invalidation": np.nan,
    }

    last_candle_value = line_value(section, "Ultima candela SOL usata")
    last_dt = parse_italian_date(last_candle_value)

    if not pd.isna(last_dt):
        meta["last_candle_date"] = last_dt.strftime("%Y-%m-%d")

    day_line = line_value(section, "SOL e al giorno")

    if day_line:
        meta["day_from_bottom"] = first_int(day_line)

    btc_equiv_value = line_value(section, "Giorno BTC equivalente")
    btc_equiv_dt = pd.to_datetime(btc_equiv_value, errors="coerce")

    if not pd.isna(btc_equiv_dt):
        meta["btc_equivalent_date"] = btc_equiv_dt.strftime("%Y-%m-%d")

    verdict_match = re.search(r"##\s*Verdetto:\s*([^\n]+)", section, flags=re.IGNORECASE)

    if verdict_match:
        meta["verdict"] = clean_text(verdict_match.group(1))

    sim_value = line_value(section, "Somiglianza totale")
    meta["similarity"] = first_pct(sim_value)

    meta["tracking"] = line_value(section, "Trend tracking")
    meta["phase"] = line_value(section, "Fase attuale")
    meta["risk"] = line_value(section, "Rischio fase")

    price_line = line_value(section, "Prezzo SOL")
    meta["start_price"] = first_price(price_line)

    if pd.isna(meta["start_price"]):
        meta["start_price"] = current_price_from_market()

    def price_for_label(label):
        for line in section.splitlines():
            if label.lower() in line.lower():
                p = first_price(line)

                if not pd.isna(p):
                    return p

        return np.nan

    meta["first_confirmation"] = price_for_label("Prima conferma")
    meta["second_confirmation"] = price_for_label("Seconda conferma")
    meta["soft_invalidation"] = price_for_label("Invalidazione soft")
    meta["strong_invalidation"] = price_for_label("Invalidazione forte")

    sol_bottom_dt = infer_bottom_date(meta)
    btc_bottom_dt = infer_btc_bottom_date(meta)
    program_start_dt = infer_program_start_date()

    if pd.isna(program_start_dt):
        program_start_dt = pd.to_datetime(meta["forecast_date"])

    meta["sol_bottom_date"] = sol_bottom_dt.strftime("%Y-%m-%d")
    meta["btc_bottom_date"] = btc_bottom_dt.strftime("%Y-%m-%d")
    meta["program_start_date"] = program_start_dt.strftime("%Y-%m-%d")

    sol_prices = download_prices(
        SOL_TICKER,
        start=(sol_bottom_dt - pd.Timedelta(days=3)).strftime("%Y-%m-%d"),
    )

    btc_prices = download_prices(
        BTC_TICKER,
        start=(btc_bottom_dt - pd.Timedelta(days=3)).strftime("%Y-%m-%d"),
    )

    if not sol_prices.empty:
        meta["sol_bottom_price"] = actual_price_on_or_after(sol_prices, sol_bottom_dt)

    if not btc_prices.empty:
        meta["btc_bottom_price"] = actual_price_on_or_after(btc_prices, btc_bottom_dt)

    proj = parse_markdown_table_after_heading(section, "Proiezione veloce con date SOL")

    rows = []

    if not proj.empty:
        for _, r in proj.iterrows():
            horizon_text = str(r.get("Orizzonte", ""))
            m = re.search(r"([0-9]+)", horizon_text)

            if not m:
                continue

            horizon = int(m.group(1))

            if horizon not in HORIZONS:
                continue

            target_date_raw = r.get("Data SOL prevista", "")
            target_dt = parse_italian_date(target_date_raw)

            if pd.isna(target_dt):
                target_dt = pd.to_datetime(meta["forecast_date"]) + pd.Timedelta(days=horizon)

            rows.append({
                **meta,
                "horizon_days": horizon,
                "target_date": target_dt.strftime("%Y-%m-%d"),
                "btc_return_text": r.get("BTC fece", ""),
                "projected_base": normalize_price_from_cell(r.get("SOL base", np.nan)),
                "projected_min": normalize_price_from_cell(r.get("Min percorso", np.nan)),
                "projected_max": normalize_price_from_cell(r.get("Max percorso", np.nan)),
                "checked": 0.0,
                "actual_price": np.nan,
                "error_pct": np.nan,
                "inside_projected_band": np.nan,
            })

    if not rows:
        for horizon in HORIZONS:
            target_dt = pd.to_datetime(meta["forecast_date"]) + pd.Timedelta(days=horizon)

            rows.append({
                **meta,
                "horizon_days": horizon,
                "target_date": target_dt.strftime("%Y-%m-%d"),
                "btc_return_text": "",
                "projected_base": np.nan,
                "projected_min": np.nan,
                "projected_max": np.nan,
                "checked": 0.0,
                "actual_price": np.nan,
                "error_pct": np.nan,
                "inside_projected_band": np.nan,
            })

    return pd.DataFrame(rows), meta


def append_today_forecast(today_df):
    if FORECAST_LOG.exists():
        old = pd.read_csv(FORECAST_LOG)
    else:
        old = pd.DataFrame()

    if old.empty:
        combined = today_df
    else:
        keys = ["forecast_date", "asset", "source", "horizon_days"]

        for k in keys:
            if k not in old.columns:
                old[k] = np.nan

        marker = old[keys].astype(str).agg("|".join, axis=1)
        today_marker = today_df[keys].astype(str).agg("|".join, axis=1)

        old = old[~marker.isin(set(today_marker))]
        combined = pd.concat([old, today_df], ignore_index=True)

    combined.to_csv(FORECAST_LOG, index=False)

    return combined


def update_forecast_checks(log_df):
    if log_df.empty:
        return log_df

    today = pd.to_datetime(today_str()).normalize()
    min_date = pd.to_datetime(log_df["forecast_date"], errors="coerce").min()

    if pd.isna(min_date):
        min_date = today - pd.Timedelta(days=10)

    dl_start = (min_date - pd.Timedelta(days=3)).strftime("%Y-%m-%d")
    prices = download_prices(SOL_TICKER, start=dl_start)

    for idx, row in log_df.iterrows():
        checked = safe_float(row.get("checked", 0.0))

        if not pd.isna(checked) and checked >= 1:
            continue

        target_date = pd.to_datetime(row.get("target_date", ""), errors="coerce")

        if pd.isna(target_date):
            continue

        if target_date.normalize() > today:
            continue

        actual = actual_price_on_or_after(prices, target_date)

        if pd.isna(actual):
            continue

        projected_base = safe_float(row.get("projected_base", np.nan))
        projected_min = safe_float(row.get("projected_min", np.nan))
        projected_max = safe_float(row.get("projected_max", np.nan))

        error_pct = np.nan

        if not pd.isna(projected_base) and projected_base != 0:
            error_pct = (actual / projected_base - 1) * 100

        inside = np.nan

        if not pd.isna(projected_min) and not pd.isna(projected_max):
            lo = min(projected_min, projected_max)
            hi = max(projected_min, projected_max)
            inside = 1.0 if lo <= actual <= hi else 0.0

        log_df.at[idx, "checked"] = 1.0
        log_df.at[idx, "actual_price"] = actual
        log_df.at[idx, "error_pct"] = error_pct
        log_df.at[idx, "inside_projected_band"] = inside

    log_df.to_csv(FORECAST_LOG, index=False)

    return log_df


def summarize_accuracy(log_df):
    if log_df.empty:
        return pd.DataFrame()

    checked = log_df[pd.to_numeric(log_df["checked"], errors="coerce").fillna(0) >= 1].copy()

    if checked.empty:
        rows = []

        for h in HORIZONS:
            rows.append({
                "asset": ASSET,
                "source": SOURCE,
                "horizon_days": h,
                "checked_predictions": 0,
                "inside_band_rate": np.nan,
                "avg_abs_error_pct": np.nan,
                "avg_error_pct": np.nan,
            })

        return pd.DataFrame(rows)

    rows = []

    for h in HORIZONS:
        d = checked[pd.to_numeric(checked["horizon_days"], errors="coerce") == h].copy()
        n = len(d)

        if n == 0:
            inside_rate = np.nan
            avg_abs_error = np.nan
            avg_error = np.nan
        else:
            inside_values = pd.to_numeric(d["inside_projected_band"], errors="coerce").dropna()

            if len(inside_values) == 0:
                inside_rate = np.nan
            else:
                inside_rate = inside_values.mean() * 100

            errors = pd.to_numeric(d["error_pct"], errors="coerce")
            avg_abs_error = errors.abs().mean()
            avg_error = errors.mean()

        rows.append({
            "asset": ASSET,
            "source": SOURCE,
            "horizon_days": h,
            "checked_predictions": n,
            "inside_band_rate": inside_rate,
            "avg_abs_error_pct": avg_abs_error,
            "avg_error_pct": avg_error,
        })

    return pd.DataFrame(rows)


def latest_forecast(log_df):
    if log_df.empty:
        return pd.DataFrame()

    d = log_df.copy()
    d["forecast_date_dt"] = pd.to_datetime(d["forecast_date"], errors="coerce")
    max_date = d["forecast_date_dt"].max()

    out = d[d["forecast_date_dt"] == max_date].copy()
    out["horizon_days"] = pd.to_numeric(out["horizon_days"], errors="coerce")

    return out.sort_values("horizon_days")


def build_projection_points(latest):
    if latest.empty:
        return pd.DataFrame()

    first = latest.iloc[0]
    forecast_dt = pd.to_datetime(first["forecast_date"])
    start_price = safe_float(first.get("start_price", np.nan))

    points = [{
        "date": forecast_dt,
        "base": start_price,
        "min": start_price,
        "max": start_price,
    }]

    for _, r in latest.iterrows():
        points.append({
            "date": pd.to_datetime(r["target_date"]),
            "base": safe_float(r["projected_base"]),
            "min": safe_float(r["projected_min"]),
            "max": safe_float(r["projected_max"]),
        })

    p = pd.DataFrame(points)
    p = p.dropna(subset=["date"])
    p = p.sort_values("date")

    return p


def build_btc_scaled_path(first, end_date):
    sol_bottom_date = pd.to_datetime(first.get("sol_bottom_date", pd.NaT), errors="coerce")
    btc_bottom_date = pd.to_datetime(first.get("btc_bottom_date", pd.NaT), errors="coerce")
    sol_bottom_price = safe_float(first.get("sol_bottom_price", np.nan))
    btc_bottom_price = safe_float(first.get("btc_bottom_price", np.nan))

    if pd.isna(sol_bottom_date) or pd.isna(btc_bottom_date):
        return pd.DataFrame()

    if pd.isna(sol_bottom_price) or pd.isna(btc_bottom_price) or btc_bottom_price == 0:
        return pd.DataFrame()

    max_days = int((pd.to_datetime(end_date).normalize() - sol_bottom_date.normalize()).days)

    if max_days < 0:
        return pd.DataFrame()

    btc_prices = download_prices(
        BTC_TICKER,
        start=(btc_bottom_date - pd.Timedelta(days=3)).strftime("%Y-%m-%d"),
    )

    rows = []

    for day in range(max_days + 1):
        btc_date = btc_bottom_date + pd.Timedelta(days=day)
        sol_mapped_date = sol_bottom_date + pd.Timedelta(days=day)
        btc_price = actual_price_on_or_after(btc_prices, btc_date)

        if pd.isna(btc_price):
            continue

        btc_scaled = sol_bottom_price * (btc_price / btc_bottom_price)

        rows.append({
            "day_from_bottom": day,
            "sol_mapped_date": sol_mapped_date,
            "btc_date": btc_date,
            "btc_price": btc_price,
            "btc_scaled_to_sol": btc_scaled,
        })

    return pd.DataFrame(rows)


def build_bottom_backtest(first):
    sol_bottom_date = pd.to_datetime(first.get("sol_bottom_date", pd.NaT), errors="coerce")
    btc_bottom_date = pd.to_datetime(first.get("btc_bottom_date", pd.NaT), errors="coerce")
    forecast_date = pd.to_datetime(first.get("forecast_date", today_str()), errors="coerce")
    program_start_date = pd.to_datetime(first.get("program_start_date", pd.NaT), errors="coerce")

    sol_bottom_price = safe_float(first.get("sol_bottom_price", np.nan))
    btc_bottom_price = safe_float(first.get("btc_bottom_price", np.nan))

    if pd.isna(sol_bottom_date) or pd.isna(btc_bottom_date):
        return pd.DataFrame(), {}

    if pd.isna(sol_bottom_price) or pd.isna(btc_bottom_price) or btc_bottom_price == 0:
        return pd.DataFrame(), {}

    max_day = int((forecast_date.normalize() - sol_bottom_date.normalize()).days)

    if max_day < 0:
        return pd.DataFrame(), {}

    sol_prices = download_prices(
        SOL_TICKER,
        start=(sol_bottom_date - pd.Timedelta(days=3)).strftime("%Y-%m-%d"),
    )

    btc_prices = download_prices(
        BTC_TICKER,
        start=(btc_bottom_date - pd.Timedelta(days=3)).strftime("%Y-%m-%d"),
    )

    rows = []

    for day in range(max_day + 1):
        sol_date = sol_bottom_date + pd.Timedelta(days=day)
        btc_date = btc_bottom_date + pd.Timedelta(days=day)

        sol_price = actual_price_on_or_after(sol_prices, sol_date)
        btc_price = actual_price_on_or_after(btc_prices, btc_date)

        if pd.isna(sol_price) or pd.isna(btc_price):
            continue

        btc_scaled = sol_bottom_price * (btc_price / btc_bottom_price)
        error_pct = np.nan

        if btc_scaled != 0:
            error_pct = (sol_price / btc_scaled - 1) * 100

        phase = "prima programma"

        if not pd.isna(program_start_date) and sol_date.normalize() >= program_start_date.normalize():
            phase = "da inizio programma"

        rows.append({
            "day_from_bottom": day,
            "sol_date": sol_date.strftime("%Y-%m-%d"),
            "btc_equivalent_date": btc_date.strftime("%Y-%m-%d"),
            "sol_price": sol_price,
            "btc_price": btc_price,
            "btc_scaled_to_sol": btc_scaled,
            "error_pct": error_pct,
            "phase": phase,
        })

    backtest = pd.DataFrame(rows)

    if backtest.empty:
        return backtest, {}

    errors = pd.to_numeric(backtest["error_pct"], errors="coerce").dropna()

    last_row = backtest.iloc[-1]
    last_error = safe_float(last_row.get("error_pct", np.nan))

    last7 = backtest.tail(7)
    last7_errors = pd.to_numeric(last7["error_pct"], errors="coerce").dropna()

    if not pd.isna(program_start_date):
        from_program = backtest[pd.to_datetime(backtest["sol_date"]) >= program_start_date.normalize()]
    else:
        from_program = pd.DataFrame()

    program_errors = pd.to_numeric(from_program["error_pct"], errors="coerce").dropna() if not from_program.empty else pd.Series(dtype=float)

    avg_abs_error = errors.abs().mean() if len(errors) else np.nan
    last7_abs_error = last7_errors.abs().mean() if len(last7_errors) else np.nan
    program_abs_error = program_errors.abs().mean() if len(program_errors) else np.nan

    if pd.isna(last_error):
        status = "n/a"
    elif abs(last_error) <= 8:
        status = "IN LINEA"
    elif abs(last_error) <= 15:
        status = "DEVIAZIONE MODERATA"
    elif last_error > 15:
        status = "SOL IN ANTICIPO / SOPRA IL FRACTAL"
    else:
        status = "SOL IN RITARDO / SOTTO IL FRACTAL"

    summary = {
        "days_checked": len(backtest),
        "avg_abs_error_pct": avg_abs_error,
        "last_error_pct": last_error,
        "last7_abs_error_pct": last7_abs_error,
        "program_abs_error_pct": program_abs_error,
        "status": status,
        "program_days_checked": len(from_program),
    }

    return backtest, summary


def plot_tracking_chart(log_df, backtest_df=None):
    latest = latest_forecast(log_df)

    if latest.empty:
        return

    first = latest.iloc[0]

    forecast_date = pd.to_datetime(first["forecast_date"]).normalize()
    sol_bottom_date = pd.to_datetime(first.get("sol_bottom_date", first["forecast_date"]), errors="coerce")
    program_start_date = pd.to_datetime(first.get("program_start_date", pd.NaT), errors="coerce")

    if pd.isna(sol_bottom_date):
        sol_bottom_date = forecast_date

    end_date = pd.to_datetime(latest["target_date"], errors="coerce").max()

    if pd.isna(end_date):
        end_date = forecast_date + pd.Timedelta(days=120)

    sol_prices = download_prices(
        SOL_TICKER,
        start=(sol_bottom_date - pd.Timedelta(days=3)).strftime("%Y-%m-%d"),
    )

    if not sol_prices.empty:
        sol_prices = sol_prices[
            (sol_prices.index >= sol_bottom_date.normalize()) &
            (sol_prices.index <= end_date.normalize())
        ]

    projection = build_projection_points(latest)
    btc_scaled = build_btc_scaled_path(first, end_date)

    plt.figure(figsize=(13, 7))

    if not btc_scaled.empty:
        plt.plot(
            btc_scaled["sol_mapped_date"],
            btc_scaled["btc_scaled_to_sol"],
            linewidth=2,
            label="BTC 2022 scalato su SOL",
        )

    if not sol_prices.empty:
        sol_past = sol_prices[sol_prices.index <= forecast_date]
        sol_future = sol_prices[sol_prices.index > forecast_date]

        if not sol_past.empty:
            plt.plot(sol_past.index, sol_past["Close"], marker="o", label="SOL reale dal bottom")

        if not sol_future.empty:
            plt.plot(sol_future.index, sol_future["Close"], marker="o", label="SOL reale dopo previsione")

    if not projection.empty:
        plt.plot(projection["date"], projection["base"], marker="o", label="Proiezione frattale base")
        plt.plot(projection["date"], projection["min"], linestyle="--", label="Percorso minimo")
        plt.plot(projection["date"], projection["max"], linestyle="--", label="Percorso massimo")

        if projection["min"].notna().any() and projection["max"].notna().any():
            plt.fill_between(projection["date"], projection["min"], projection["max"], alpha=0.15)

    if not pd.isna(sol_bottom_date):
        plt.axvline(sol_bottom_date, linestyle=":", linewidth=1.2, label="Bottom SOL usato")

    if not pd.isna(program_start_date):
        plt.axvline(program_start_date, linestyle="-.", linewidth=1.2, label="Inizio programma/scanner")

    plt.axvline(forecast_date, linestyle=":", linewidth=1.2, label="Oggi / inizio nuova previsione")

    plt.title("BTC 2022 scalato vs SOL reale dal bottom + proiezione futura")
    plt.xlabel("Data SOL")
    plt.ylabel("Prezzo SOL")
    plt.legend()
    plt.grid(True, alpha=0.25)
    plt.tight_layout()
    plt.savefig(TRACKING_CHART, dpi=160)
    plt.close()


def plot_bottom_backtest_chart(backtest_df, first):
    if backtest_df is None or backtest_df.empty:
        return

    df = backtest_df.copy()
    df["sol_date_dt"] = pd.to_datetime(df["sol_date"], errors="coerce")
    df = df.dropna(subset=["sol_date_dt"])

    if df.empty:
        return

    forecast_date = pd.to_datetime(first.get("forecast_date", today_str()), errors="coerce")
    program_start_date = pd.to_datetime(first.get("program_start_date", pd.NaT), errors="coerce")
    sol_bottom_date = pd.to_datetime(first.get("sol_bottom_date", pd.NaT), errors="coerce")

    plt.figure(figsize=(13, 6))
    plt.plot(df["sol_date_dt"], df["sol_price"], marker="o", label="SOL reale")
    plt.plot(df["sol_date_dt"], df["btc_scaled_to_sol"], linewidth=2, label="BTC 2022 scalato su SOL")

    if not pd.isna(sol_bottom_date):
        plt.axvline(sol_bottom_date, linestyle=":", linewidth=1.2, label="Bottom SOL")

    if not pd.isna(program_start_date):
        plt.axvline(program_start_date, linestyle="-.", linewidth=1.2, label="Inizio programma/scanner")

    if not pd.isna(forecast_date):
        plt.axvline(forecast_date, linestyle=":", linewidth=1.2, label="Oggi")

    plt.title("Backtest dal bottom: SOL reale vs BTC 2022 scalato")
    plt.xlabel("Data SOL")
    plt.ylabel("Prezzo SOL")
    plt.legend()
    plt.grid(True, alpha=0.25)
    plt.tight_layout()
    plt.savefig(BOTTOM_BACKTEST_CHART, dpi=160)
    plt.close()


def plot_error_chart(log_df):
    checked = log_df[pd.to_numeric(log_df["checked"], errors="coerce").fillna(0) >= 1].copy()

    if checked.empty:
        return

    checked["target_date_dt"] = pd.to_datetime(checked["target_date"], errors="coerce")
    checked["error_pct"] = pd.to_numeric(checked["error_pct"], errors="coerce")
    checked = checked.dropna(subset=["target_date_dt", "error_pct"])

    if checked.empty:
        return

    plt.figure(figsize=(11, 5))
    plt.axhline(0, linewidth=1)
    plt.plot(
        checked["target_date_dt"],
        checked["error_pct"],
        marker="o",
        label="Errore % vs base frattale",
    )
    plt.title("Errore del frattale SOL/BTC nel tempo")
    plt.xlabel("Data target")
    plt.ylabel("Errore %")
    plt.legend()
    plt.grid(True, alpha=0.25)
    plt.tight_layout()
    plt.savefig(ERROR_CHART, dpi=160)
    plt.close()


def yes_no_nan(x):
    x = safe_float(x)

    if pd.isna(x):
        return "n/a"

    return "sì" if x >= 1 else "no"


def render_report(log_df, metrics, backtest_df, backtest_summary):
    now = utc_now().strftime("%Y-%m-%d %H:%M UTC")
    latest = latest_forecast(log_df)

    lines = []

    lines.append("# Tracking percorso frattale SOL/BTC")
    lines.append("")
    lines.append(f"Generato: {now}")
    lines.append("")
    lines.append("Questo report controlla se SOL sta seguendo il percorso previsto dal frattale BTC 2022 vs SOL 2026.")
    lines.append("")
    lines.append("Ora il controllo è diviso in tre parti:")
    lines.append("")
    lines.append("- confronto dal bottom: BTC 2022 scalato contro SOL reale")
    lines.append("- tratto da inizio programma/scanner: verifica se il tracking recente sta reggendo")
    lines.append("- proiezione futura: percorso atteso da oggi in avanti")
    lines.append("")

    if latest.empty:
        lines.append("_Nessuna previsione frattale salvata._")
        return "\n".join(lines) + "\n"

    first = latest.iloc[0]

    lines.append("## Stato ultimo frattale salvato")
    lines.append("")
    lines.append(f"- Data previsione: **{first.get('forecast_date', 'n/a')}**")
    lines.append(f"- Bottom SOL usato: **{first.get('sol_bottom_date', 'n/a')}**")
    lines.append(f"- Bottom BTC 2022 equivalente: **{first.get('btc_bottom_date', 'n/a')}**")
    lines.append(f"- Inizio programma/scanner rilevato: **{first.get('program_start_date', 'n/a')}**")
    lines.append(f"- Prezzo iniziale SOL: **{fmt_price(first.get('start_price', np.nan))}**")
    lines.append(f"- Verdetto: **{first.get('verdict', 'n/a')}**")
    lines.append(f"- Somiglianza: **{fmt_pct(first.get('similarity', np.nan))}**")
    lines.append(f"- Tracking: **{first.get('tracking', 'n/a')}**")
    lines.append(f"- Fase: **{first.get('phase', 'n/a')}**")
    lines.append(f"- Rischio fase: **{first.get('risk', 'n/a')}**")
    lines.append("")

    if backtest_summary:
        lines.append("## Confronto dal bottom a oggi")
        lines.append("")
        lines.append(f"- Giorni controllati dal bottom: **{backtest_summary.get('days_checked', 0)}**")
        lines.append(f"- Giorni controllati da inizio programma/scanner: **{backtest_summary.get('program_days_checked', 0)}**")
        lines.append(f"- Errore medio assoluto dal bottom: **{fmt_pct(backtest_summary.get('avg_abs_error_pct', np.nan))}**")
        lines.append(f"- Errore medio assoluto ultimi 7 giorni: **{fmt_pct(backtest_summary.get('last7_abs_error_pct', np.nan))}**")
        lines.append(f"- Errore medio assoluto da inizio programma/scanner: **{fmt_pct(backtest_summary.get('program_abs_error_pct', np.nan))}**")
        lines.append(f"- Errore ultimo giorno: **{fmt_pct(backtest_summary.get('last_error_pct', np.nan))}**")
        lines.append(f"- Stato: **{backtest_summary.get('status', 'n/a')}**")
        lines.append("")

    if TRACKING_CHART.exists():
        lines.append("## Grafico completo: bottom, inizio programma e proiezione")
        lines.append("")
        lines.append(f"![Tracking percorso frattale]({TRACKING_CHART.name})")
        lines.append("")

    if BOTTOM_BACKTEST_CHART.exists():
        lines.append("## Grafico backtest dal bottom")
        lines.append("")
        lines.append(f"![Backtest dal bottom]({BOTTOM_BACKTEST_CHART.name})")
        lines.append("")

    if backtest_df is not None and not backtest_df.empty:
        last_rows = backtest_df.tail(10).copy()
        table = []

        for _, r in last_rows.iterrows():
            table.append({
                "Giorno": int(r["day_from_bottom"]),
                "Data SOL": r["sol_date"],
                "Data BTC eq.": r["btc_equivalent_date"],
                "SOL reale": fmt_price(r["sol_price"]),
                "BTC scalato": fmt_price(r["btc_scaled_to_sol"]),
                "Errore": fmt_pct(r["error_pct"]),
                "Fase": r["phase"],
            })

        lines.append("## Ultimi giorni del confronto dal bottom")
        lines.append("")
        lines.append(df_to_markdown(pd.DataFrame(table)))
        lines.append("")

    table_rows = []

    for _, r in latest.iterrows():
        table_rows.append({
            "Orizzonte": f"{int(r['horizon_days'])}g",
            "Data target": r.get("target_date", ""),
            "Base frattale": fmt_price(r.get("projected_base", np.nan)),
            "Min percorso": fmt_price(r.get("projected_min", np.nan)),
            "Max percorso": fmt_price(r.get("projected_max", np.nan)),
            "Controllato": yes_no_nan(r.get("checked", np.nan)),
            "Prezzo reale": fmt_price(r.get("actual_price", np.nan)),
            "Errore": fmt_pct(r.get("error_pct", np.nan)),
            "Dentro banda": yes_no_nan(r.get("inside_projected_band", np.nan)),
        })

    lines.append("## Proiezione futura salvata")
    lines.append("")
    lines.append(df_to_markdown(pd.DataFrame(table_rows)))
    lines.append("")

    lines.append("## Accuratezza storica della proiezione futura")
    lines.append("")

    if metrics.empty:
        lines.append("_Dati insufficienti._")
    else:
        metric_rows = []

        for _, r in metrics.iterrows():
            metric_rows.append({
                "Orizzonte": f"{int(r['horizon_days'])}g",
                "Controlli": int(r["checked_predictions"]),
                "Dentro banda": fmt_pct(r["inside_band_rate"]),
                "Errore medio assoluto": fmt_pct(r["avg_abs_error_pct"]),
                "Errore medio": fmt_pct(r["avg_error_pct"]),
            })

        lines.append(df_to_markdown(pd.DataFrame(metric_rows)))

    lines.append("")

    if ERROR_CHART.exists():
        lines.append("## Grafico errore proiezioni future")
        lines.append("")
        lines.append(f"![Errore frattale]({ERROR_CHART.name})")
        lines.append("")

    lines.append("## Come leggerlo")
    lines.append("")
    lines.append("- BTC 2022 scalato su SOL è il percorso che SOL dovrebbe seguire se il frattale resta valido.")
    lines.append("- SOL reale mostra cosa ha fatto davvero dal bottom.")
    lines.append("- La linea 'inizio programma/scanner' separa il backtest retroattivo dalla parte che stiamo monitorando davvero giorno per giorno.")
    lines.append("- Se SOL resta vicino a BTC scalato, il frattale è in linea.")
    lines.append("- Se SOL sta sopra BTC scalato, il frattale è in anticipo o più forte.")
    lines.append("- Se SOL sta sotto BTC scalato, il frattale è in ritardo o più debole.")
    lines.append("- La proiezione futura va letta insieme alle conferme e invalidazioni del report frattale principale.")
    lines.append("")

    return "\n".join(lines) + "\n"


def inject_into_latest_report(section_md):
    if not LATEST_REPORT.exists():
        return

    old = read_text(LATEST_REPORT)

    if not old:
        return

    clean = section_md.strip()
    new_section = START_MARKER + "\n" + clean + "\n" + END_MARKER

    if START_MARKER in old and END_MARKER in old:
        start = old.find(START_MARKER)
        end = old.find(END_MARKER)

        if start != -1 and end != -1 and end > start:
            end = end + len(END_MARKER)
            new = old[:start] + new_section + old[end:]
        else:
            new = old.rstrip() + "\n\n" + new_section + "\n"
    else:
        anchor = "<!-- BTC_SOL_FRACTAL_END -->"

        if anchor in old:
            idx = old.find(anchor) + len(anchor)
            new = old[:idx] + "\n\n" + new_section + old[idx:]
        else:
            new = old.rstrip() + "\n\n" + new_section + "\n"

    LATEST_REPORT.write_text(new, encoding="utf-8")


def main():
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    today_df, meta = parse_fractal_forecast()

    if today_df.empty:
        md = "# Tracking percorso frattale SOL/BTC\n\nNessuna previsione frattale trovata.\n"
        OUTPUT_REPORT.write_text(md, encoding="utf-8")
        inject_into_latest_report(md)
        print("Nessuna previsione frattale trovata.")
        return

    log_df = append_today_forecast(today_df)
    log_df = update_forecast_checks(log_df)

    metrics = summarize_accuracy(log_df)
    metrics.to_csv(ACCURACY_METRICS, index=False)

    latest = latest_forecast(log_df)
    first = latest.iloc[0] if not latest.empty else None

    backtest_df = pd.DataFrame()
    backtest_summary = {}

    if first is not None:
        backtest_df, backtest_summary = build_bottom_backtest(first)

        if not backtest_df.empty:
            backtest_df.to_csv(BOTTOM_BACKTEST_CSV, index=False)

    plot_tracking_chart(log_df, backtest_df)
    plot_bottom_backtest_chart(backtest_df, first) if first is not None else None
    plot_error_chart(log_df)

    md = render_report(log_df, metrics, backtest_df, backtest_summary)

    OUTPUT_REPORT.write_text(md, encoding="utf-8")
    inject_into_latest_report(md)

    print(f"Creato/aggiornato {FORECAST_LOG}")
    print(f"Creato {ACCURACY_METRICS}")
    print(f"Creato {OUTPUT_REPORT}")

    if not backtest_df.empty:
        print(f"Creato {BOTTOM_BACKTEST_CSV}")

    if TRACKING_CHART.exists():
        print(f"Creato {TRACKING_CHART}")

    if BOTTOM_BACKTEST_CHART.exists():
        print(f"Creato {BOTTOM_BACKTEST_CHART}")

    if ERROR_CHART.exists():
        print(f"Creato {ERROR_CHART}")


if __name__ == "__main__":
    main()
