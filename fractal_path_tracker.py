import os
import re
from datetime import datetime, timedelta, timezone

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import yfinance as yf
from tabulate import tabulate


REPORT_DIR = "reports"
MAIN_REPORT_PATH = os.path.join(REPORT_DIR, "latest_report.md")

BTC_SOL_REPORT_PATH = os.path.join(REPORT_DIR, "btc_2022_vs_sol_2026_report.md")

REPORT_PATH = os.path.join(REPORT_DIR, "fractal_path_tracker.md")
TRACKING_FULL_CSV_PATH = os.path.join(REPORT_DIR, "btc_2022_vs_sol_2026_path_tracking_full.csv")
FUTURE_DAILY_CSV_PATH = os.path.join(REPORT_DIR, "btc_2022_vs_sol_2026_future_daily_projection.csv")
PROJECTION_LOG_CSV_PATH = os.path.join(REPORT_DIR, "btc_2022_vs_sol_2026_projection_log.csv")

PATH_TRACKING_CHART_PATH = os.path.join(REPORT_DIR, "btc_2022_vs_sol_2026_path_tracking_chart.png")
BOTTOM_BACKTEST_CHART_PATH = os.path.join(REPORT_DIR, "btc_2022_vs_sol_2026_bottom_backtest_chart.png")
GAP_60D_CHART_PATH = os.path.join(REPORT_DIR, "btc_2022_vs_sol_2026_gap_60d_chart.png")

START_MARKER = "<!-- FRACTAL_PATH_TRACKER_START -->"
END_MARKER = "<!-- FRACTAL_PATH_TRACKER_END -->"

BTC_SOL_START = "<!-- BTC_SOL_FRACTAL_START -->"
BTC_SOL_END = "<!-- BTC_SOL_FRACTAL_END -->"

FRACTAL_PATH_START = "<!-- FRACTAL_PATH_TRACKER_START -->"
FRACTAL_PATH_END = "<!-- FRACTAL_PATH_TRACKER_END -->"

SOL_TICKER = "SOL-USD"
BTC_TICKER = "BTC-USD"

DEFAULT_SOL_BOTTOM_DATE = pd.Timestamp("2026-06-06")
DEFAULT_BTC_BOTTOM_DATE = pd.Timestamp("2022-11-21")
DEFAULT_PROGRAM_START_DATE = pd.Timestamp("2026-07-03")

WEEKLY_HORIZONS = list(range(7, 127, 7))


ITALIAN_MONTHS = {
    "gennaio": 1,
    "febbraio": 2,
    "marzo": 3,
    "aprile": 4,
    "maggio": 5,
    "giugno": 6,
    "luglio": 7,
    "agosto": 8,
    "settembre": 9,
    "ottobre": 10,
    "novembre": 11,
    "dicembre": 12,
}


def now_utc():
    return datetime.now(timezone.utc)


def read_text(path):
    if not os.path.exists(path):
        return ""

    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def write_text(path, text):
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def clean_md(value):
    if value is None:
        return ""

    value = str(value)
    value = value.replace("**", "")
    value = value.replace("__", "")
    value = value.replace("`", "")
    value = value.replace("•", "")
    value = value.strip()
    value = re.sub(r"\s+", " ", value)
    value = value.strip(" -:|")

    return value.strip()


def safe_float(value, default=np.nan):
    try:
        if value is None:
            return default

        if isinstance(value, str):
            s = clean_md(value)
            if not s or s.lower() in ["nan", "none", "null", "n/a", "na"]:
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

        if pd.isna(value):
            return default

        return float(value)

    except Exception:
        return default


def fmt_number(value, decimals=2):
    value = safe_float(value)

    if pd.isna(value):
        return "n/a"

    return f"{value:.{decimals}f}".replace(".", ",")


def fmt_pct(value, decimals=2, signed=True):
    value = safe_float(value)

    if pd.isna(value):
        return "n/a"

    sign = "+" if signed and value > 0 else ""
    return f"{sign}{value:.{decimals}f}%".replace(".", ",")


def fmt_price(value, decimals=2):
    value = safe_float(value)

    if pd.isna(value):
        return "n/a"

    text = f"{value:,.{decimals}f}"
    text = text.replace(",", "X").replace(".", ",").replace("X", ".")
    return f"{text} $"


def fmt_date_ita(value):
    if value is None or pd.isna(value):
        return "n/a"

    ts = pd.Timestamp(value)
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

    return f"{ts.day} {months[ts.month]} {ts.year}"


def parse_date_any(value):
    if value is None:
        return None

    s = clean_md(value)

    if not s:
        return None

    iso_match = re.search(r"(\d{4})-(\d{2})-(\d{2})", s)
    if iso_match:
        try:
            return pd.Timestamp(iso_match.group(0)).normalize()
        except Exception:
            pass

    ita_match = re.search(
        r"(\d{1,2})\s+([a-zàèéìòù]+)\s+(\d{4})",
        s.lower(),
        re.IGNORECASE,
    )
    if ita_match:
        day = int(ita_match.group(1))
        month_name = ita_match.group(2).lower()
        year = int(ita_match.group(3))
        month = ITALIAN_MONTHS.get(month_name)

        if month:
            return pd.Timestamp(year=year, month=month, day=day).normalize()

    try:
        return pd.Timestamp(s).normalize()
    except Exception:
        return None


def extract_between(text, start_marker, end_marker):
    if not text:
        return ""

    if start_marker in text and end_marker in text:
        start = text.index(start_marker)
        end = text.index(end_marker) + len(end_marker)
        return text[start:end]

    return ""


def extract_first(pattern, text, flags=re.IGNORECASE | re.MULTILINE):
    m = re.search(pattern, text, flags)

    if not m:
        return None

    return clean_md(m.group(1))


def extract_line_value(label, text):
    label_norm = label.lower()

    for line in text.splitlines():
        line_clean = clean_md(line)

        if label_norm in line_clean.lower() and ":" in line_clean:
            return clean_md(line_clean.split(":", 1)[1])

    return None


def extract_table_date_from_total_bottom(text):
    for line in text.splitlines():
        if "Totale dal bottom" not in line:
            continue

        cells = [clean_md(c) for c in line.strip().strip("|").split("|")]

        if len(cells) < 2:
            continue

        date_cell = cells[1]
        if "->" in date_cell:
            left = date_cell.split("->", 1)[0].strip()
            parsed = parse_date_any(left)
            if parsed is not None:
                return parsed

    return None


def normalize_ohlcv(df):
    if df is None or df.empty:
        return pd.DataFrame()

    out = df.copy()

    if isinstance(out.columns, pd.MultiIndex):
        fields = ["Open", "High", "Low", "Close", "Adj Close", "Volume"]

        level0 = list(out.columns.get_level_values(0))
        level1 = list(out.columns.get_level_values(1))

        if any(field in level0 for field in fields):
            tmp = {}
            for field in fields:
                if field in level0:
                    part = out.xs(field, axis=1, level=0)
                    tmp[field] = part.iloc[:, 0]
            out = pd.DataFrame(tmp)

        elif any(field in level1 for field in fields):
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
        out.index = out.index.tz_convert(None)
    except Exception:
        try:
            out.index = out.index.tz_localize(None)
        except Exception:
            pass

    out.index = out.index.normalize()
    out = out[~out.index.duplicated(keep="last")]
    out = out.sort_index()
    out = out.dropna(subset=["Close"])

    return out


def download_daily(ticker):
    raw = yf.download(
        ticker,
        period="max",
        interval="1d",
        auto_adjust=False,
        progress=False,
        actions=False,
        threads=False,
    )

    out = normalize_ohlcv(raw)

    if out.empty:
        raise RuntimeError(f"Dati daily non disponibili per {ticker}")

    return out


def close_on_or_before(df, date):
    date = pd.Timestamp(date).normalize()
    sliced = df[df.index <= date]

    if sliced.empty:
        return np.nan

    return safe_float(sliced.iloc[-1]["Close"])


def close_on_exact_or_before(df, date):
    return close_on_or_before(df, date)


def available_date_on_or_before(df, date):
    date = pd.Timestamp(date).normalize()
    sliced = df[df.index <= date]

    if sliced.empty:
        return None

    return pd.Timestamp(sliced.index[-1]).normalize()


def build_metadata(latest_text, btc_report_text):
    btc_section = extract_between(latest_text, BTC_SOL_START, BTC_SOL_END)

    if not btc_section:
        btc_section = btc_report_text

    old_tracker_section = extract_between(latest_text, FRACTAL_PATH_START, FRACTAL_PATH_END)

    source_text = "\n\n".join([btc_section, old_tracker_section, btc_report_text, latest_text])

    verdict = extract_first(r"##\s*Verdetto:\s*([^\n]+)", btc_section)
    if not verdict:
        verdict = extract_line_value("Verdetto", btc_section)

    similarity = extract_line_value("Somiglianza totale", btc_section)
    tracking = extract_line_value("Trend tracking", btc_section)
    phase = extract_line_value("Fase attuale", btc_section)
    risk = extract_line_value("Rischio fase", btc_section)

    sol_day_raw = extract_line_value("SOL e al giorno", btc_section)
    if not sol_day_raw:
        sol_day_raw = extract_line_value("SOL è al giorno", btc_section)

    sol_day = None
    if sol_day_raw:
        m = re.search(r"(\d+)", sol_day_raw)
        if m:
            sol_day = int(m.group(1))

    btc_equiv_raw = extract_line_value("Giorno BTC equivalente", btc_section)
    btc_equiv_date = parse_date_any(btc_equiv_raw)

    program_start_raw = extract_line_value("Inizio programma/scanner", btc_section)
    program_start_date = parse_date_any(program_start_raw)

    sol_bottom_raw = extract_line_value("Bottom SOL usato", old_tracker_section)
    sol_bottom_date = parse_date_any(sol_bottom_raw)

    if sol_bottom_date is None:
        sol_bottom_date = extract_table_date_from_total_bottom(btc_section)

    btc_bottom_raw = extract_line_value("Bottom BTC 2022 equivalente", old_tracker_section)
    btc_bottom_date = parse_date_any(btc_bottom_raw)

    if btc_bottom_date is None and btc_equiv_date is not None and sol_day is not None:
        btc_bottom_date = btc_equiv_date - pd.Timedelta(days=sol_day)

    if sol_bottom_date is None:
        sol_bottom_date = DEFAULT_SOL_BOTTOM_DATE

    if btc_bottom_date is None:
        btc_bottom_date = DEFAULT_BTC_BOTTOM_DATE

    if program_start_date is None:
        program_start_date = DEFAULT_PROGRAM_START_DATE

    if verdict is None:
        verdict = "n/a"

    if similarity is None:
        similarity = "n/a"

    if tracking is None:
        tracking = "n/a"

    if phase is None:
        phase = "n/a"

    if risk is None:
        risk = "n/a"

    metadata = {
        "verdict": clean_md(verdict),
        "similarity": clean_md(similarity),
        "tracking": clean_md(tracking),
        "phase": clean_md(phase),
        "risk": clean_md(risk),
        "sol_day_from_report": sol_day,
        "btc_equiv_from_report": btc_equiv_date,
        "sol_bottom_date": pd.Timestamp(sol_bottom_date).normalize(),
        "btc_bottom_date": pd.Timestamp(btc_bottom_date).normalize(),
        "program_start_date": pd.Timestamp(program_start_date).normalize(),
    }

    return metadata


def build_tracking_dataframe(sol_df, btc_df, metadata):
    sol_bottom_date = metadata["sol_bottom_date"]
    btc_bottom_date = metadata["btc_bottom_date"]

    sol_bottom_price = close_on_exact_or_before(sol_df, sol_bottom_date)
    btc_bottom_price = close_on_exact_or_before(btc_df, btc_bottom_date)

    if pd.isna(sol_bottom_price) or pd.isna(btc_bottom_price) or btc_bottom_price == 0:
        raise RuntimeError("Impossibile calcolare scala frattale: prezzi bottom mancanti.")

    latest_sol_date = available_date_on_or_before(sol_df, sol_df.index.max())

    if latest_sol_date is None:
        raise RuntimeError("Nessuna data SOL disponibile.")

    day_count = int((latest_sol_date - sol_bottom_date).days)

    rows = []

    for day in range(0, day_count + 1):
        sol_date = sol_bottom_date + pd.Timedelta(days=day)
        btc_date = btc_bottom_date + pd.Timedelta(days=day)

        sol_price = close_on_exact_or_before(sol_df, sol_date)
        btc_price = close_on_exact_or_before(btc_df, btc_date)

        if pd.isna(sol_price) or pd.isna(btc_price):
            continue

        btc_scaled = (btc_price / btc_bottom_price) * sol_bottom_price

        if btc_scaled == 0 or pd.isna(btc_scaled):
            error_pct = np.nan
        else:
            error_pct = (sol_price / btc_scaled - 1) * 100

        if sol_date < metadata["program_start_date"]:
            phase = "prima programma"
        else:
            phase = "da inizio programma"

        rows.append(
            {
                "day": day,
                "sol_date": sol_date,
                "btc_equiv_date": btc_date,
                "sol_close": sol_price,
                "btc_close": btc_price,
                "btc_scaled_to_sol": btc_scaled,
                "error_pct": error_pct,
                "abs_error_pct": abs(error_pct) if not pd.isna(error_pct) else np.nan,
                "phase": phase,
            }
        )

    tracking = pd.DataFrame(rows)

    if tracking.empty:
        raise RuntimeError("Tracking frattale vuoto: controlla date bottom e dati Yahoo.")

    return tracking


def classify_tracking_state(mean_abs_error, last_error):
    mean_abs_error = safe_float(mean_abs_error)
    last_error = safe_float(last_error)

    if pd.isna(mean_abs_error):
        return "n/a"

    if mean_abs_error <= 5:
        return "IN LINEA"

    if mean_abs_error <= 12:
        return "DEVIAZIONE MODERATA"

    if mean_abs_error <= 25:
        if last_error > 0:
            return "STACCATO / MOLTO IN ANTICIPO"
        return "STACCATO / IN RITARDO"

    return "FRATTALE MOLTO DEVIATO"


def classify_gap_state(last_gap):
    last_gap = safe_float(last_gap)

    if pd.isna(last_gap):
        return "n/a"

    if last_gap >= 15:
        return "SOPRA FRATTALE / MOLTO IN ANTICIPO"

    if last_gap >= 5:
        return "SOPRA FRATTALE"

    if last_gap > -5:
        return "VICINO AL FRATTALE"

    if last_gap > -15:
        return "SOTTO FRATTALE"

    return "SOTTO FRATTALE / MOLTO IN RITARDO"


def classify_gap_trend(last_gap, recent_change):
    last_gap = safe_float(last_gap)
    recent_change = safe_float(recent_change)

    if pd.isna(last_gap) or pd.isna(recent_change):
        return "n/a"

    if last_gap > 0 and recent_change < -1:
        return "SOL resta sopra il frattale, ma sta perdendo anticipo e si sta riavvicinando al percorso BTC scalato"

    if last_gap > 0 and recent_change > 1:
        return "SOL sta aumentando l'anticipo rispetto al percorso BTC scalato"

    if last_gap > 0:
        return "SOL resta sopra il frattale con gap stabile"

    if last_gap < 0 and recent_change > 1:
        return "SOL è sotto il frattale, ma sta recuperando verso il percorso BTC scalato"

    if last_gap < 0 and recent_change < -1:
        return "SOL si sta indebolendo rispetto al percorso BTC scalato"

    return "SOL è vicino al percorso BTC scalato"


def build_future_projection(sol_df, btc_df, tracking, metadata):
    latest_row = tracking.iloc[-1]

    current_sol_date = pd.Timestamp(latest_row["sol_date"]).normalize()
    current_btc_date = pd.Timestamp(latest_row["btc_equiv_date"]).normalize()
    current_sol_price = safe_float(latest_row["sol_close"])

    btc_current_price = close_on_exact_or_before(btc_df, current_btc_date)

    if pd.isna(current_sol_price) or pd.isna(btc_current_price) or btc_current_price == 0:
        raise RuntimeError("Impossibile costruire proiezione futura: prezzo corrente BTC/SOL mancante.")

    max_horizon = max(WEEKLY_HORIZONS)

    rows = []

    projected_values = []

    for day in range(0, max_horizon + 1):
        btc_future_date = current_btc_date + pd.Timedelta(days=day)
        sol_target_date = current_sol_date + pd.Timedelta(days=day)

        btc_future_price = close_on_exact_or_before(btc_df, btc_future_date)

        if pd.isna(btc_future_price):
            continue

        base_fractal_price = current_sol_price * (btc_future_price / btc_current_price)

        projected_values.append(base_fractal_price)

        rows.append(
            {
                "horizon_days": day,
                "horizon": f"{day}g",
                "prediction_date": current_sol_date,
                "target_date": sol_target_date,
                "btc_equiv_target_date": btc_future_date,
                "base_fractal": base_fractal_price,
                "min_path": np.nanmin(projected_values),
                "max_path": np.nanmax(projected_values),
            }
        )

    daily_projection = pd.DataFrame(rows)

    weekly_projection = daily_projection[daily_projection["horizon_days"].isin(WEEKLY_HORIZONS)].copy()

    return daily_projection, weekly_projection


def update_projection_log(weekly_projection, sol_df):
    latest_sol_date = available_date_on_or_before(sol_df, sol_df.index.max())

    if weekly_projection is None or weekly_projection.empty:
        return pd.DataFrame(), pd.DataFrame()

    projection_date = pd.Timestamp(weekly_projection.iloc[0]["prediction_date"]).strftime("%Y-%m-%d")

    new_rows = weekly_projection.copy()
    new_rows["prediction_date"] = pd.to_datetime(new_rows["prediction_date"]).dt.strftime("%Y-%m-%d")
    new_rows["target_date"] = pd.to_datetime(new_rows["target_date"]).dt.strftime("%Y-%m-%d")
    new_rows["btc_equiv_target_date"] = pd.to_datetime(new_rows["btc_equiv_target_date"]).dt.strftime("%Y-%m-%d")
    new_rows["checked"] = False
    new_rows["actual_price"] = np.nan
    new_rows["error_pct"] = np.nan
    new_rows["inside_band"] = np.nan

    if os.path.exists(PROJECTION_LOG_CSV_PATH):
        try:
            log = pd.read_csv(PROJECTION_LOG_CSV_PATH)
        except Exception:
            log = pd.DataFrame()
    else:
        log = pd.DataFrame()

    if not log.empty and "prediction_date" in log.columns:
        log = log[log["prediction_date"].astype(str) != projection_date].copy()

    log = pd.concat([log, new_rows], ignore_index=True)

    if log.empty:
        log.to_csv(PROJECTION_LOG_CSV_PATH, index=False)
        return log, pd.DataFrame()

    for idx, row in log.iterrows():
        target_date = parse_date_any(row.get("target_date"))

        if target_date is None or latest_sol_date is None:
            continue

        if target_date <= latest_sol_date:
            actual = close_on_exact_or_before(sol_df, target_date)
            base = safe_float(row.get("base_fractal"))
            min_path = safe_float(row.get("min_path"))
            max_path = safe_float(row.get("max_path"))

            if not pd.isna(actual) and not pd.isna(base) and base != 0:
                log.loc[idx, "checked"] = True
                log.loc[idx, "actual_price"] = actual
                log.loc[idx, "error_pct"] = (actual / base - 1) * 100

                if not pd.isna(min_path) and not pd.isna(max_path):
                    log.loc[idx, "inside_band"] = bool(min_path <= actual <= max_path)
                else:
                    log.loc[idx, "inside_band"] = np.nan

    log["horizon_days"] = log["horizon_days"].astype(int)
    log = log.sort_values(["prediction_date", "horizon_days"]).reset_index(drop=True)
    log.to_csv(PROJECTION_LOG_CSV_PATH, index=False)

    accuracy_rows = []

    checked = log[log["checked"].astype(str).str.lower().isin(["true", "1"])].copy()

    for horizon_days in WEEKLY_HORIZONS:
        c = checked[checked["horizon_days"] == horizon_days].copy()

        if c.empty:
            accuracy_rows.append(
                {
                    "Orizzonte": f"{horizon_days}g",
                    "Controlli": 0,
                    "Dentro banda": "n/a",
                    "Errore medio assoluto": "n/a",
                    "Errore medio": "n/a",
                }
            )
            continue

        inside = c["inside_band"].astype(str).str.lower().isin(["true", "1"]).mean() * 100
        err = pd.to_numeric(c["error_pct"], errors="coerce")

        accuracy_rows.append(
            {
                "Orizzonte": f"{horizon_days}g",
                "Controlli": int(len(c)),
                "Dentro banda": fmt_pct(inside, signed=False),
                "Errore medio assoluto": fmt_pct(err.abs().mean(), signed=False),
                "Errore medio": fmt_pct(err.mean(), signed=True),
            }
        )

    accuracy_df = pd.DataFrame(accuracy_rows)

    return log, accuracy_df


def format_tracking_tail(tracking, rows=10):
    tail = tracking.tail(rows).copy()

    out = pd.DataFrame(
        {
            "Giorno": tail["day"].astype(int),
            "Data SOL": tail["sol_date"].dt.strftime("%Y-%m-%d"),
            "Data BTC eq.": tail["btc_equiv_date"].dt.strftime("%Y-%m-%d"),
            "SOL reale": tail["sol_close"].map(fmt_price),
            "BTC scalato": tail["btc_scaled_to_sol"].map(fmt_price),
            "Errore": tail["error_pct"].map(lambda x: fmt_pct(x, signed=True)),
            "Fase": tail["phase"],
        }
    )

    return out


def format_weekly_projection_table(weekly_projection, log):
    rows = []

    for _, row in weekly_projection.iterrows():
        horizon_days = int(row["horizon_days"])
        prediction_date = pd.Timestamp(row["prediction_date"]).strftime("%Y-%m-%d")
        target_date = pd.Timestamp(row["target_date"]).strftime("%Y-%m-%d")

        log_row = pd.DataFrame()

        if log is not None and not log.empty:
            log_row = log[
                (log["prediction_date"].astype(str) == prediction_date)
                & (log["horizon_days"].astype(int) == horizon_days)
            ].copy()

        checked = "no"
        actual_price = "n/a"
        error = "n/a"
        inside = "n/a"

        if not log_row.empty:
            r = log_row.iloc[-1]
            checked_bool = str(r.get("checked")).lower() in ["true", "1"]

            if checked_bool:
                checked = "si"
                actual_price = fmt_price(r.get("actual_price"))
                error = fmt_pct(r.get("error_pct"), signed=True)

                inside_value = str(r.get("inside_band")).lower()
                if inside_value in ["true", "1"]:
                    inside = "si"
                elif inside_value in ["false", "0"]:
                    inside = "no"

        rows.append(
            {
                "Orizzonte": f"{horizon_days}g",
                "Data target": target_date,
                "Base frattale": fmt_price(row["base_fractal"]),
                "Min percorso": fmt_price(row["min_path"]),
                "Max percorso": fmt_price(row["max_path"]),
                "Controllato": checked,
                "Prezzo reale": actual_price,
                "Errore": error,
                "Dentro banda": inside,
            }
        )

    return pd.DataFrame(rows)


def df_to_markdown(df):
    if df is None or df.empty:
        return "_Nessun dato disponibile._"

    return tabulate(df, headers="keys", tablefmt="pipe", showindex=False)


def create_charts(tracking, daily_projection, metadata):
    if tracking is None or tracking.empty:
        return

    os.makedirs(REPORT_DIR, exist_ok=True)

    chart_df = tracking.copy()

    future_df = daily_projection.copy() if daily_projection is not None else pd.DataFrame()

    plt.figure(figsize=(12, 6))
    plt.plot(chart_df["sol_date"], chart_df["sol_close"], label="SOL reale")
    plt.plot(chart_df["sol_date"], chart_df["btc_scaled_to_sol"], label="BTC 2022 scalato su SOL")

    if not future_df.empty:
        plt.plot(
            future_df["target_date"],
            future_df["base_fractal"],
            linestyle="--",
            label="Proiezione BTC 2022 scalata",
        )

    plt.axvline(metadata["program_start_date"], linestyle=":", label="Inizio programma/scanner")
    plt.title("Tracking percorso frattale SOL/BTC")
    plt.xlabel("Data SOL")
    plt.ylabel("Prezzo SOL")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(PATH_TRACKING_CHART_PATH, dpi=150)
    plt.close()

    plt.figure(figsize=(12, 6))
    plt.plot(chart_df["sol_date"], chart_df["sol_close"], label="SOL reale dal bottom")
    plt.plot(chart_df["sol_date"], chart_df["btc_scaled_to_sol"], label="BTC 2022 scalato dal bottom")
    plt.axvline(metadata["program_start_date"], linestyle=":", label="Inizio programma/scanner")
    plt.title("Backtest dal bottom: SOL reale vs BTC 2022 scalato")
    plt.xlabel("Data SOL")
    plt.ylabel("Prezzo SOL")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(BOTTOM_BACKTEST_CHART_PATH, dpi=150)
    plt.close()

    gap_df = chart_df.tail(60).copy()

    plt.figure(figsize=(12, 5))
    plt.plot(gap_df["sol_date"], gap_df["error_pct"], label="Gap SOL vs BTC scalato")
    plt.axhline(0, linestyle="--", label="Linea 0%")
    plt.title("Gap SOL vs BTC scalato - ultimi 60 giorni")
    plt.xlabel("Data SOL")
    plt.ylabel("Gap %")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(GAP_60D_CHART_PATH, dpi=150)
    plt.close()


def build_report(metadata, tracking, daily_projection, weekly_projection, log, accuracy_df):
    generated = now_utc().strftime("%Y-%m-%d %H:%M UTC")

    latest = tracking.iloc[-1]
    latest_sol_date = pd.Timestamp(latest["sol_date"]).normalize()
    latest_btc_date = pd.Timestamp(latest["btc_equiv_date"]).normalize()

    current_price = safe_float(latest["sol_close"])
    last_error = safe_float(latest["error_pct"])

    bottom_days = int(len(tracking))
    day_from_bottom = int(latest["day"])

    from_program = tracking[tracking["sol_date"] >= metadata["program_start_date"]].copy()
    last_7 = tracking.tail(7).copy()

    mean_abs_bottom = tracking["abs_error_pct"].mean()
    mean_abs_program = from_program["abs_error_pct"].mean() if not from_program.empty else np.nan
    mean_abs_last_7 = last_7["abs_error_pct"].mean() if not last_7.empty else np.nan

    tracking_state = classify_tracking_state(mean_abs_bottom, last_error)

    if len(tracking) >= 4:
        recent_change = last_error - safe_float(tracking.iloc[-4]["error_pct"])
    else:
        recent_change = np.nan

    gap_ma7 = mean_abs_last_7
    gap_state = classify_gap_state(last_error)
    gap_trend = classify_gap_trend(last_error, recent_change)

    tail_df = format_tracking_tail(tracking, 10)
    projection_table = format_weekly_projection_table(weekly_projection, log)

    if accuracy_df is None or accuracy_df.empty:
        accuracy_rows = [
            {
                "Orizzonte": f"{h}g",
                "Controlli": 0,
                "Dentro banda": "n/a",
                "Errore medio assoluto": "n/a",
                "Errore medio": "n/a",
            }
            for h in WEEKLY_HORIZONS
        ]
        accuracy_df = pd.DataFrame(accuracy_rows)

    report = f"""{START_MARKER}
# Tracking percorso frattale SOL/BTC

Generato: {generated}

Questo report controlla se SOL sta seguendo il percorso previsto dal frattale BTC 2022 vs SOL 2026.

Ora il controllo è diviso in cinque parti:

- confronto dal bottom: BTC 2022 scalato contro SOL reale
- tratto da inizio programma/scanner: verifica se il tracking recente sta reggendo
- proiezione futura giornaliera: BTC 2022 viene scalato giorno per giorno su SOL
- controllo settimanale: ogni previsione viene verificata a 7, 14, 21, 28 giorni e così via fino a 126 giorni
- grafico gap: differenza leggibile tra SOL reale e BTC scalato

## Stato ultimo frattale salvato

- Data previsione: **{latest_sol_date.strftime("%Y-%m-%d")}**
- Bottom SOL usato: **{metadata["sol_bottom_date"].strftime("%Y-%m-%d")}**
- Bottom BTC 2022 equivalente: **{metadata["btc_bottom_date"].strftime("%Y-%m-%d")}**
- Giorno BTC equivalente oggi: **{latest_btc_date.strftime("%Y-%m-%d")}**
- Inizio programma/scanner rilevato: **{metadata["program_start_date"].strftime("%Y-%m-%d")}**
- Prezzo SOL corrente: **{fmt_price(current_price)}**
- Verdetto: **{metadata["verdict"]}**
- Somiglianza: **{metadata["similarity"]}**
- Tracking: **{metadata["tracking"]}**
- Fase: **{metadata["phase"]}**
- Rischio fase: **{metadata["risk"]}**

## Confronto dal bottom a oggi

- Giorni controllati dal bottom: **{bottom_days}**
- Giorni controllati da inizio programma/scanner: **{len(from_program)}**
- Errore medio assoluto dal bottom: **{fmt_pct(mean_abs_bottom, signed=False)}**
- Errore medio assoluto ultimi 7 giorni: **{fmt_pct(mean_abs_last_7, signed=False)}**
- Errore medio assoluto da inizio programma/scanner: **{fmt_pct(mean_abs_program, signed=False)}**
- Errore ultimo giorno: **{fmt_pct(last_error, signed=True)}**
- Stato: **{tracking_state}**

## Grafico completo: bottom, inizio programma e proiezione giornaliera

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato - ultimi 60 giorni

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap: **{fmt_pct(last_error, signed=True)}**
- Media mobile 7g gap: **{fmt_pct(gap_ma7, signed=True)}**
- Variazione recente gap: **{fmt_pct(recent_change, signed=True)}**
- Stato gap: **{gap_state}**
- Trend gap: **{gap_trend}**

Come leggerlo:

- **Sopra 0%** = SOL è sopra il percorso BTC scalato.
- **Sotto 0%** = SOL è sotto il percorso BTC scalato.
- Se il gap sale, SOL si sta allontanando sopra il frattale.
- Se il gap scende mentre resta positivo, SOL resta più forte del frattale ma sta perdendo anticipo.
- Questo è il grafico più leggibile per capire subito se SOL si sta orientando sopra o sotto il frattale.

## Ultimi giorni del confronto dal bottom

{df_to_markdown(tail_df)}

## Proiezione futura salvata

{df_to_markdown(projection_table)}

Nota: la tabella sopra mostra le milestone settimanali principali. Il grafico invece usa la proiezione giornaliera del frattale BTC scalato su SOL.

## Accuratezza storica della proiezione futura

{df_to_markdown(accuracy_df)}

## Come leggerlo

- BTC 2022 scalato su SOL è il percorso che SOL dovrebbe seguire se il frattale resta valido.
- SOL reale mostra cosa ha fatto davvero dal bottom.
- La linea di inizio programma/scanner separa il backtest retroattivo dalla parte che stiamo monitorando davvero giorno per giorno.
- Se SOL resta vicino a BTC scalato, il frattale è in linea.
- Se SOL sta sopra BTC scalato, il frattale è in anticipo o più forte.
- Se SOL sta sotto BTC scalato, il frattale è in ritardo o più debole.
- Il grafico gap ultimi 60 giorni serve proprio per vedere meglio questa differenza.
- Le milestone settimanali servono a controllare il percorso passo passo.
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
        insert_after_marker = "<!-- LIQUIDATION_SUMMARY_END -->"

        if insert_after_marker in content:
            idx = content.index(insert_after_marker) + len(insert_after_marker)
            new_content = content[:idx] + "\n\n" + section_text + "\n" + content[idx:]
        else:
            if not content.endswith("\n"):
                content += "\n"
            new_content = content + "\n" + section_text

    write_text(MAIN_REPORT_PATH, new_content)


def main():
    os.makedirs(REPORT_DIR, exist_ok=True)

    latest_text = read_text(MAIN_REPORT_PATH)
    btc_report_text = read_text(BTC_SOL_REPORT_PATH)

    metadata = build_metadata(latest_text, btc_report_text)

    sol_df = download_daily(SOL_TICKER)
    btc_df = download_daily(BTC_TICKER)

    tracking = build_tracking_dataframe(sol_df, btc_df, metadata)
    daily_projection, weekly_projection = build_future_projection(sol_df, btc_df, tracking, metadata)

    tracking.to_csv(TRACKING_FULL_CSV_PATH, index=False)
    daily_projection.to_csv(FUTURE_DAILY_CSV_PATH, index=False)

    log, accuracy_df = update_projection_log(weekly_projection, sol_df)

    create_charts(tracking, daily_projection, metadata)

    report_text = build_report(
        metadata=metadata,
        tracking=tracking,
        daily_projection=daily_projection,
        weekly_projection=weekly_projection,
        log=log,
        accuracy_df=accuracy_df,
    )

    write_text(REPORT_PATH, report_text)
    replace_section_in_latest_report(report_text)

    latest = tracking.iloc[-1]

    print(f"Report scritto in: {REPORT_PATH}")
    print(f"Latest report aggiornato: {MAIN_REPORT_PATH}")
    print(f"CSV tracking completo: {TRACKING_FULL_CSV_PATH}")
    print(f"CSV proiezione futura giornaliera: {FUTURE_DAILY_CSV_PATH}")
    print(f"CSV log proiezioni: {PROJECTION_LOG_CSV_PATH}")
    print(f"Ultima data SOL: {pd.Timestamp(latest['sol_date']).strftime('%Y-%m-%d')}")
    print(f"Prezzo SOL: {safe_float(latest['sol_close']):.4f}")
    print(f"Gap ultimo: {safe_float(latest['error_pct']):.2f}%")
    print(f"Verdetto letto: {metadata['verdict']}")
    print(f"Somiglianza letta: {metadata['similarity']}")
    print(f"Tracking letto: {metadata['tracking']}")


if __name__ == "__main__":
    main()
