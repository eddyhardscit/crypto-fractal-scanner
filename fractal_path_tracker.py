# -*- coding: utf-8 -*-
"""Track the BTC 2022 -> SOL 2026 analogue without confusing shape and price adherence.

Main corrections:
- reads structured metrics from btc_2022_vs_sol_2026_metrics.csv first;
- keeps the original bottom-anchored path separate from the projection re-anchored today;
- reports signed 7-day gap and absolute 7-day error separately;
- writes a structured tracker summary for downstream modules;
- never treats a re-anchored projection as proof that the original path is still aligned.
"""

from __future__ import annotations

import csv
import os
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import yfinance as yf
from tabulate import tabulate


REPORT_DIR = Path("reports")
MAIN_REPORT_PATH = REPORT_DIR / "latest_report.md"

BTC_SOL_REPORT_PATH = REPORT_DIR / "btc_2022_vs_sol_2026_report.md"
BTC_SOL_METRICS_PATH = REPORT_DIR / "btc_2022_vs_sol_2026_metrics.csv"

REPORT_PATH = REPORT_DIR / "fractal_path_tracker.md"
TRACKING_FULL_CSV_PATH = REPORT_DIR / "btc_2022_vs_sol_2026_path_tracking_full.csv"
FUTURE_DAILY_CSV_PATH = REPORT_DIR / "btc_2022_vs_sol_2026_future_daily_projection.csv"
PROJECTION_LOG_CSV_PATH = REPORT_DIR / "btc_2022_vs_sol_2026_projection_log.csv"
TRACKER_METRICS_CSV_PATH = REPORT_DIR / "fractal_path_tracker_metrics.csv"

PATH_TRACKING_CHART_PATH = REPORT_DIR / "btc_2022_vs_sol_2026_path_tracking_chart.png"
BOTTOM_BACKTEST_CHART_PATH = REPORT_DIR / "btc_2022_vs_sol_2026_bottom_backtest_chart.png"
GAP_60D_CHART_PATH = REPORT_DIR / "btc_2022_vs_sol_2026_gap_60d_chart.png"

START_MARKER = "<!-- FRACTAL_PATH_TRACKER_START -->"
END_MARKER = "<!-- FRACTAL_PATH_TRACKER_END -->"

BTC_SOL_START = "<!-- BTC_SOL_FRACTAL_START -->"
BTC_SOL_END = "<!-- BTC_SOL_FRACTAL_END -->"

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


def now_utc() -> datetime:
    return datetime.now(timezone.utc)


def read_text(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8", errors="replace")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def clean_md(value: Any) -> str:
    if value is None:
        return ""
    text = str(value)
    for token in ("**", "__", "`", "\u2022"):
        text = text.replace(token, "")
    text = re.sub(r"\s+", " ", text).strip(" -:|")
    return text.strip()


def safe_float(value: Any, default=np.nan) -> float:
    try:
        if value is None:
            return default
        if isinstance(value, str):
            text = clean_md(value)
            if not text or text.lower() in {"nan", "none", "null", "n/a", "na", "n/d"}:
                return default
            text = (
                text.replace("%", "")
                .replace("$", "")
                .replace("\u20ac", "")
                .replace("+", "")
                .replace("\u2212", "-")
                .replace(" ", "")
            )
            if "," in text and "." in text:
                text = text.replace(".", "").replace(",", ".")
            elif "," in text:
                text = text.replace(",", ".")
            text = re.sub(r"[^0-9.\-]", "", text)
            if not text or text in {"-", ".", "-."}:
                return default
            return float(text)
        if pd.isna(value):
            return default
        return float(value)
    except Exception:
        return default


def fmt_number(value: Any, decimals: int = 2) -> str:
    number = safe_float(value)
    if pd.isna(number):
        return "n/a"
    return f"{number:.{decimals}f}".replace(".", ",")


def fmt_pct(value: Any, decimals: int = 2, signed: bool = True) -> str:
    number = safe_float(value)
    if pd.isna(number):
        return "n/a"
    sign = "+" if signed and number > 0 else ""
    return f"{sign}{number:.{decimals}f}%".replace(".", ",")


def fmt_price(value: Any, decimals: int = 2) -> str:
    number = safe_float(value)
    if pd.isna(number):
        return "n/a"
    text = f"{number:,.{decimals}f}"
    text = text.replace(",", "X").replace(".", ",").replace("X", ".")
    return f"{text} $"


def parse_date_any(value: Any) -> pd.Timestamp | None:
    if value is None:
        return None
    text = clean_md(value)
    if not text:
        return None

    iso_match = re.search(r"(\d{4})-(\d{2})-(\d{2})", text)
    if iso_match:
        try:
            return pd.Timestamp(iso_match.group(0)).normalize()
        except Exception:
            pass

    ita_match = re.search(
        r"(\d{1,2})\s+([a-z\u00e0\u00e8\u00e9\u00ec\u00f2\u00f9]+)\s+(\d{4})",
        text.lower(),
        re.IGNORECASE,
    )
    if ita_match:
        day = int(ita_match.group(1))
        month = ITALIAN_MONTHS.get(ita_match.group(2).lower())
        year = int(ita_match.group(3))
        if month:
            return pd.Timestamp(year=year, month=month, day=day).normalize()

    try:
        return pd.Timestamp(text).normalize()
    except Exception:
        return None


def extract_between(text: str, start_marker: str, end_marker: str) -> str:
    if start_marker not in text or end_marker not in text:
        return ""
    start = text.index(start_marker)
    end = text.index(end_marker) + len(end_marker)
    return text[start:end]


def extract_line_value(label: str, text: str) -> str | None:
    label_lower = label.lower()
    for line in text.splitlines():
        cleaned = clean_md(line)
        if label_lower in cleaned.lower() and ":" in cleaned:
            return clean_md(cleaned.split(":", 1)[1])
    return None


def read_csv_rows(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    try:
        with path.open("r", encoding="utf-8", newline="") as handle:
            return list(csv.DictReader(handle))
    except Exception:
        return []


def read_main_fractal_summary() -> dict[str, Any]:
    rows = read_csv_rows(BTC_SOL_METRICS_PATH)
    for row in rows:
        if clean_md(row.get("row_type")).lower() == "summary":
            return row
    return {}


def build_metadata(latest_text: str, btc_report_text: str) -> dict[str, Any]:
    structured = read_main_fractal_summary()

    if structured:
        sol_bottom = parse_date_any(structured.get("sol_anchor_date")) or DEFAULT_SOL_BOTTOM_DATE
        btc_bottom = parse_date_any(structured.get("btc_anchor_date")) or DEFAULT_BTC_BOTTOM_DATE
        program_start = parse_date_any(structured.get("program_start_date")) or DEFAULT_PROGRAM_START_DATE
        btc_equiv = parse_date_any(structured.get("btc_equivalent_date"))

        metadata = {
            "source": "structured_csv",
            "verdict": clean_md(structured.get("verdict")) or "n/a",
            "structural_similarity": safe_float(
                structured.get("structural_similarity"),
                safe_float(structured.get("total_similarity")),
            ),
            "live_adherence_score": safe_float(
                structured.get("live_adherence_score"),
                safe_float(structured.get("live_program_alignment_score")),
            ),
            "live_avg_abs_gap_pct": safe_float(
                structured.get("live_avg_abs_gap_pct"),
                safe_float(structured.get("live_program_avg_abs_gap_pct")),
            ),
            "main_current_gap_pct": safe_float(
                structured.get("phase_gap_pct"),
                safe_float(structured.get("live_program_last_gap_pct")),
            ),
            "operational_weight": int(safe_float(structured.get("operational_weight"), 0) or 0),
            "phase": clean_md(structured.get("phase_label")) or "n/a",
            "risk": clean_md(structured.get("phase_risk")) or "n/a",
            "sol_day_from_report": int(safe_float(structured.get("sol_elapsed_days"), 0) or 0),
            "btc_equiv_from_report": btc_equiv,
            "sol_bottom_date": pd.Timestamp(sol_bottom).normalize(),
            "btc_bottom_date": pd.Timestamp(btc_bottom).normalize(),
            "program_start_date": pd.Timestamp(program_start).normalize(),
        }
        return metadata

    btc_section = extract_between(latest_text, BTC_SOL_START, BTC_SOL_END)
    if not btc_section:
        btc_section = btc_report_text

    verdict = extract_line_value("Verdetto", btc_section) or "n/a"
    structural = extract_line_value("Somiglianza strutturale", btc_section)
    live_adherence = extract_line_value("Aderenza prezzo live", btc_section)
    live_gap = extract_line_value("Errore medio live", btc_section)
    current_gap = extract_line_value("Gap prezzo corrente", btc_section)
    phase = extract_line_value("Fase attuale", btc_section) or "n/a"
    risk = extract_line_value("Rischio fase", btc_section) or "n/a"
    program_start = parse_date_any(extract_line_value("Inizio programma/scanner", btc_section))
    sol_day_raw = extract_line_value("SOL e al giorno", btc_section) or extract_line_value("SOL \u00e8 al giorno", btc_section)
    btc_equiv = parse_date_any(extract_line_value("Giorno BTC equivalente", btc_section))

    sol_day = int(safe_float(sol_day_raw, 0) or 0)
    btc_bottom = btc_equiv - pd.Timedelta(days=sol_day) if btc_equiv is not None else DEFAULT_BTC_BOTTOM_DATE

    return {
        "source": "markdown_fallback",
        "verdict": clean_md(verdict),
        "structural_similarity": safe_float(structural),
        "live_adherence_score": safe_float(live_adherence),
        "live_avg_abs_gap_pct": safe_float(live_gap),
        "main_current_gap_pct": safe_float(current_gap),
        "operational_weight": 0,
        "phase": clean_md(phase),
        "risk": clean_md(risk),
        "sol_day_from_report": sol_day,
        "btc_equiv_from_report": btc_equiv,
        "sol_bottom_date": DEFAULT_SOL_BOTTOM_DATE,
        "btc_bottom_date": pd.Timestamp(btc_bottom).normalize(),
        "program_start_date": pd.Timestamp(program_start or DEFAULT_PROGRAM_START_DATE).normalize(),
    }


def normalize_ohlcv(df: pd.DataFrame) -> pd.DataFrame:
    if df is None or df.empty:
        return pd.DataFrame()

    out = df.copy()

    if isinstance(out.columns, pd.MultiIndex):
        fields = ["Open", "High", "Low", "Close", "Adj Close", "Volume"]
        level0 = list(out.columns.get_level_values(0))
        level1 = list(out.columns.get_level_values(1))

        if any(field in level0 for field in fields):
            values = {}
            for field in fields:
                if field in level0:
                    part = out.xs(field, axis=1, level=0)
                    values[field] = part.iloc[:, 0]
            out = pd.DataFrame(values)
        elif any(field in level1 for field in fields):
            values = {}
            for field in fields:
                if field in level1:
                    part = out.xs(field, axis=1, level=1)
                    values[field] = part.iloc[:, 0]
            out = pd.DataFrame(values)

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
    return out.dropna(subset=["Close"])


def download_daily(ticker: str) -> pd.DataFrame:
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


def close_on_or_before(df: pd.DataFrame, date: Any) -> float:
    target = pd.Timestamp(date).normalize()
    sliced = df[df.index <= target]
    if sliced.empty:
        return np.nan
    return safe_float(sliced.iloc[-1]["Close"])


def available_date_on_or_before(df: pd.DataFrame, date: Any) -> pd.Timestamp | None:
    target = pd.Timestamp(date).normalize()
    sliced = df[df.index <= target]
    if sliced.empty:
        return None
    return pd.Timestamp(sliced.index[-1]).normalize()


def build_tracking_dataframe(sol_df: pd.DataFrame, btc_df: pd.DataFrame, metadata: dict[str, Any]) -> pd.DataFrame:
    sol_bottom_date = metadata["sol_bottom_date"]
    btc_bottom_date = metadata["btc_bottom_date"]

    sol_bottom_price = close_on_or_before(sol_df, sol_bottom_date)
    btc_bottom_price = close_on_or_before(btc_df, btc_bottom_date)

    if pd.isna(sol_bottom_price) or pd.isna(btc_bottom_price) or btc_bottom_price == 0:
        raise RuntimeError("Impossibile calcolare la scala del frattale: bottom mancanti.")

    latest_sol_date = available_date_on_or_before(sol_df, sol_df.index.max())
    if latest_sol_date is None:
        raise RuntimeError("Nessuna data SOL disponibile.")

    day_count = int((latest_sol_date - sol_bottom_date).days)
    rows = []

    for day in range(day_count + 1):
        sol_date = sol_bottom_date + pd.Timedelta(days=day)
        btc_date = btc_bottom_date + pd.Timedelta(days=day)
        sol_price = close_on_or_before(sol_df, sol_date)
        btc_price = close_on_or_before(btc_df, btc_date)

        if pd.isna(sol_price) or pd.isna(btc_price):
            continue

        anchored_price = (btc_price / btc_bottom_price) * sol_bottom_price
        error_pct = (sol_price / anchored_price - 1) * 100 if anchored_price else np.nan

        rows.append(
            {
                "day": day,
                "sol_date": sol_date,
                "btc_equiv_date": btc_date,
                "sol_close": sol_price,
                "btc_close": btc_price,
                "btc_scaled_to_sol": anchored_price,
                "anchored_fractal_price": anchored_price,
                "error_pct": error_pct,
                "abs_error_pct": abs(error_pct) if not pd.isna(error_pct) else np.nan,
                "phase": "prima programma" if sol_date < metadata["program_start_date"] else "da inizio programma",
            }
        )

    tracking = pd.DataFrame(rows)
    if tracking.empty:
        raise RuntimeError("Tracking frattale vuoto.")
    return tracking


def classify_tracking_state(mean_abs_error: Any, last_error: Any) -> str:
    mean_abs = safe_float(mean_abs_error)
    last = safe_float(last_error)

    if pd.isna(mean_abs):
        return "n/a"
    if mean_abs <= 5:
        return "IN LINEA"
    if mean_abs <= 12:
        return "DEVIAZIONE MODERATA"
    if mean_abs <= 18:
        return "IN DEVIAZIONE"
    if mean_abs <= 25:
        return "STACCATO / MOLTO IN ANTICIPO" if last > 0 else "STACCATO / IN RITARDO"
    return "FRATTALE MOLTO DEVIATO"


def classify_gap_state(last_gap: Any) -> str:
    gap = safe_float(last_gap)
    if pd.isna(gap):
        return "n/a"
    if gap >= 18:
        return "DISALLINEATO SOPRA IL FRATTALE"
    if gap >= 12:
        return "IN DEVIAZIONE SOPRA IL FRATTALE"
    if gap >= 5:
        return "SOPRA IL FRATTALE"
    if gap > -5:
        return "VICINO AL FRATTALE"
    if gap > -12:
        return "SOTTO IL FRATTALE"
    if gap > -18:
        return "IN DEVIAZIONE SOTTO IL FRATTALE"
    return "DISALLINEATO SOTTO IL FRATTALE"


def classify_gap_trend(last_gap: Any, recent_change: Any) -> str:
    gap = safe_float(last_gap)
    change = safe_float(recent_change)

    if pd.isna(gap) or pd.isna(change):
        return "n/a"
    if gap > 0 and change < -1:
        return "SOL resta sopra il percorso ancorato, ma sta riducendo il distacco"
    if gap > 0 and change > 1:
        return "SOL sta aumentando il distacco sopra il percorso ancorato"
    if gap > 0:
        return "SOL resta sopra il percorso ancorato con distacco quasi stabile"
    if gap < 0 and change > 1:
        return "SOL e sotto il percorso ancorato ma sta recuperando"
    if gap < 0 and change < -1:
        return "SOL si sta allontanando sotto il percorso ancorato"
    return "SOL e vicino al percorso ancorato"


def build_future_projection(
    sol_df: pd.DataFrame,
    btc_df: pd.DataFrame,
    tracking: pd.DataFrame,
    metadata: dict[str, Any],
) -> tuple[pd.DataFrame, pd.DataFrame]:
    latest = tracking.iloc[-1]

    current_sol_date = pd.Timestamp(latest["sol_date"]).normalize()
    current_btc_date = pd.Timestamp(latest["btc_equiv_date"]).normalize()
    current_sol_price = safe_float(latest["sol_close"])

    sol_bottom_price = close_on_or_before(sol_df, metadata["sol_bottom_date"])
    btc_bottom_price = close_on_or_before(btc_df, metadata["btc_bottom_date"])
    btc_current_price = close_on_or_before(btc_df, current_btc_date)

    if (
        pd.isna(current_sol_price)
        or pd.isna(sol_bottom_price)
        or pd.isna(btc_bottom_price)
        or pd.isna(btc_current_price)
        or btc_bottom_price == 0
        or btc_current_price == 0
    ):
        raise RuntimeError("Impossibile costruire le proiezioni future.")

    rows = []
    anchored_values: list[float] = []
    reanchored_values: list[float] = []

    for day in range(max(WEEKLY_HORIZONS) + 1):
        btc_future_date = current_btc_date + pd.Timedelta(days=day)
        sol_target_date = current_sol_date + pd.Timedelta(days=day)
        btc_future_price = close_on_or_before(btc_df, btc_future_date)

        if pd.isna(btc_future_price):
            continue

        anchored = sol_bottom_price * (btc_future_price / btc_bottom_price)
        reanchored = current_sol_price * (btc_future_price / btc_current_price)

        anchored_values.append(anchored)
        reanchored_values.append(reanchored)

        rows.append(
            {
                "horizon_days": day,
                "horizon": f"{day}g",
                "prediction_date": current_sol_date,
                "target_date": sol_target_date,
                "btc_equiv_target_date": btc_future_date,
                "anchored_fractal": anchored,
                "reanchored_projection": reanchored,
                "base_fractal": reanchored,
                "anchored_min_path": np.nanmin(anchored_values),
                "anchored_max_path": np.nanmax(anchored_values),
                "reanchored_min_path": np.nanmin(reanchored_values),
                "reanchored_max_path": np.nanmax(reanchored_values),
                "min_path": np.nanmin(reanchored_values),
                "max_path": np.nanmax(reanchored_values),
            }
        )

    daily = pd.DataFrame(rows)
    weekly = daily[daily["horizon_days"].isin(WEEKLY_HORIZONS)].copy()
    return daily, weekly


def update_projection_log(
    weekly_projection: pd.DataFrame,
    sol_df: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    latest_sol_date = available_date_on_or_before(sol_df, sol_df.index.max())
    if weekly_projection is None or weekly_projection.empty:
        return pd.DataFrame(), pd.DataFrame()

    projection_date = pd.Timestamp(weekly_projection.iloc[0]["prediction_date"]).strftime("%Y-%m-%d")
    new_rows = weekly_projection.copy()

    for col in ["prediction_date", "target_date", "btc_equiv_target_date"]:
        new_rows[col] = pd.to_datetime(new_rows[col]).dt.strftime("%Y-%m-%d")

    new_rows["checked"] = False
    new_rows["actual_price"] = np.nan
    new_rows["error_pct"] = np.nan
    new_rows["error_reanchored_pct"] = np.nan
    new_rows["error_anchored_pct"] = np.nan
    new_rows["inside_band"] = np.nan
    new_rows["inside_reanchored_band"] = np.nan
    new_rows["inside_anchored_band"] = np.nan

    if PROJECTION_LOG_CSV_PATH.exists():
        try:
            log = pd.read_csv(PROJECTION_LOG_CSV_PATH)
        except Exception:
            log = pd.DataFrame()
    else:
        log = pd.DataFrame()

    if not log.empty and "prediction_date" in log.columns:
        log = log[log["prediction_date"].astype(str) != projection_date].copy()

    log = pd.concat([log, new_rows], ignore_index=True, sort=False)

    for idx, row in log.iterrows():
        target_date = parse_date_any(row.get("target_date"))
        if target_date is None or latest_sol_date is None or target_date > latest_sol_date:
            continue

        actual = close_on_or_before(sol_df, target_date)
        reanchored = safe_float(row.get("reanchored_projection"), safe_float(row.get("base_fractal")))
        anchored = safe_float(row.get("anchored_fractal"))

        if pd.isna(actual):
            continue

        log.loc[idx, "checked"] = True
        log.loc[idx, "actual_price"] = actual

        if not pd.isna(reanchored) and reanchored != 0:
            err_re = (actual / reanchored - 1) * 100
            log.loc[idx, "error_reanchored_pct"] = err_re
            log.loc[idx, "error_pct"] = err_re

        if not pd.isna(anchored) and anchored != 0:
            log.loc[idx, "error_anchored_pct"] = (actual / anchored - 1) * 100

        re_min = safe_float(row.get("reanchored_min_path"), safe_float(row.get("min_path")))
        re_max = safe_float(row.get("reanchored_max_path"), safe_float(row.get("max_path")))
        an_min = safe_float(row.get("anchored_min_path"))
        an_max = safe_float(row.get("anchored_max_path"))

        if not pd.isna(re_min) and not pd.isna(re_max):
            inside_re = bool(re_min <= actual <= re_max)
            log.loc[idx, "inside_reanchored_band"] = inside_re
            log.loc[idx, "inside_band"] = inside_re

        if not pd.isna(an_min) and not pd.isna(an_max):
            log.loc[idx, "inside_anchored_band"] = bool(an_min <= actual <= an_max)

    log["horizon_days"] = pd.to_numeric(log["horizon_days"], errors="coerce").fillna(0).astype(int)
    log = log.sort_values(["prediction_date", "horizon_days"]).reset_index(drop=True)
    log.to_csv(PROJECTION_LOG_CSV_PATH, index=False)

    checked = log[log["checked"].astype(str).str.lower().isin(["true", "1"])].copy()
    accuracy_rows = []

    for horizon in WEEKLY_HORIZONS:
        sample = checked[checked["horizon_days"] == horizon].copy()
        if sample.empty:
            accuracy_rows.append(
                {
                    "Orizzonte": f"{horizon}g",
                    "Controlli": 0,
                    "Dentro banda riancorata": "n/a",
                    "Errore ass. riancorato": "n/a",
                    "Errore ass. ancorato": "n/a",
                }
            )
            continue

        inside = sample["inside_reanchored_band"].astype(str).str.lower().isin(["true", "1"]).mean() * 100
        err_re = pd.to_numeric(sample["error_reanchored_pct"], errors="coerce")
        err_an = pd.to_numeric(sample["error_anchored_pct"], errors="coerce")

        accuracy_rows.append(
            {
                "Orizzonte": f"{horizon}g",
                "Controlli": int(len(sample)),
                "Dentro banda riancorata": fmt_pct(inside, signed=False),
                "Errore ass. riancorato": fmt_pct(err_re.abs().mean(), signed=False),
                "Errore ass. ancorato": fmt_pct(err_an.abs().mean(), signed=False),
            }
        )

    return log, pd.DataFrame(accuracy_rows)


def format_tracking_tail(tracking: pd.DataFrame, rows: int = 10) -> pd.DataFrame:
    tail = tracking.tail(rows).copy()
    return pd.DataFrame(
        {
            "Giorno": tail["day"].astype(int),
            "Data SOL": tail["sol_date"].dt.strftime("%Y-%m-%d"),
            "Data BTC eq.": tail["btc_equiv_date"].dt.strftime("%Y-%m-%d"),
            "SOL reale": tail["sol_close"].map(fmt_price),
            "Percorso ancorato": tail["anchored_fractal_price"].map(fmt_price),
            "Gap firmato": tail["error_pct"].map(lambda value: fmt_pct(value, signed=True)),
            "Fase": tail["phase"],
        }
    )


def format_weekly_projection_table(weekly: pd.DataFrame, log: pd.DataFrame) -> pd.DataFrame:
    rows = []

    for _, row in weekly.iterrows():
        horizon = int(row["horizon_days"])
        prediction_date = pd.Timestamp(row["prediction_date"]).strftime("%Y-%m-%d")
        target_date = pd.Timestamp(row["target_date"]).strftime("%Y-%m-%d")

        selected = pd.DataFrame()
        if log is not None and not log.empty:
            selected = log[
                (log["prediction_date"].astype(str) == prediction_date)
                & (log["horizon_days"].astype(int) == horizon)
            ]

        checked = "no"
        actual = "n/a"
        err_re = "n/a"
        err_an = "n/a"

        if not selected.empty:
            saved = selected.iloc[-1]
            if str(saved.get("checked")).lower() in {"true", "1"}:
                checked = "si"
                actual = fmt_price(saved.get("actual_price"))
                err_re = fmt_pct(saved.get("error_reanchored_pct"), signed=True)
                err_an = fmt_pct(saved.get("error_anchored_pct"), signed=True)

        rows.append(
            {
                "Orizzonte": f"{horizon}g",
                "Data target": target_date,
                "Percorso ancorato": fmt_price(row["anchored_fractal"]),
                "Scenario riancorato oggi": fmt_price(row["reanchored_projection"]),
                "Min/max riancorato": (
                    f"{fmt_price(row['reanchored_min_path'])} / "
                    f"{fmt_price(row['reanchored_max_path'])}"
                ),
                "Controllato": checked,
                "Prezzo reale": actual,
                "Errore riancorato": err_re,
                "Errore ancorato": err_an,
            }
        )

    return pd.DataFrame(rows)


def df_to_markdown(df: pd.DataFrame) -> str:
    if df is None or df.empty:
        return "_Nessun dato disponibile._"
    return tabulate(df, headers="keys", tablefmt="pipe", showindex=False)


def create_charts(
    tracking: pd.DataFrame,
    daily_projection: pd.DataFrame,
    metadata: dict[str, Any],
) -> None:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)

    future = daily_projection.copy() if daily_projection is not None else pd.DataFrame()

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(tracking["sol_date"], tracking["sol_close"], label="SOL reale")
    ax.plot(tracking["sol_date"], tracking["anchored_fractal_price"], label="Percorso BTC ancorato al bottom")

    if not future.empty:
        ax.plot(
            future["target_date"],
            future["anchored_fractal"],
            linestyle="--",
            label="Continuazione ancorata al bottom",
        )
        ax.plot(
            future["target_date"],
            future["reanchored_projection"],
            linestyle=":",
            label="Scenario riancorato al prezzo di oggi",
        )

    ax.axvline(metadata["program_start_date"], linestyle="-.", label="Inizio programma/scanner")
    ax.set_title("Percorso SOL/BTC: ancorato al bottom vs riancorato oggi")
    ax.set_xlabel("Data SOL")
    ax.set_ylabel("Prezzo SOL")
    ax.legend()
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(PATH_TRACKING_CHART_PATH, dpi=160)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(tracking["sol_date"], tracking["sol_close"], label="SOL reale dal bottom")
    ax.plot(tracking["sol_date"], tracking["anchored_fractal_price"], label="BTC 2022 scalato dal bottom")
    ax.axvline(metadata["program_start_date"], linestyle=":", label="Inizio programma/scanner")
    ax.set_title("Backtest dal bottom: SOL reale vs percorso BTC ancorato")
    ax.set_xlabel("Data SOL")
    ax.set_ylabel("Prezzo SOL")
    ax.legend()
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(BOTTOM_BACKTEST_CHART_PATH, dpi=160)
    plt.close(fig)

    gap_df = tracking.tail(60).copy()

    fig, ax = plt.subplots(figsize=(12, 5))
    ax.plot(gap_df["sol_date"], gap_df["error_pct"], label="Gap firmato SOL vs percorso ancorato")
    for level in [0, 5, -5, 12, -12, 18, -18]:
        ax.axhline(level, linestyle="--", alpha=0.28)
    ax.set_title("Gap SOL vs BTC scalato - soglie 5% / 12% / 18%")
    ax.set_xlabel("Data SOL")
    ax.set_ylabel("Gap %")
    ax.legend()
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(GAP_60D_CHART_PATH, dpi=160)
    plt.close(fig)


def build_report(
    metadata: dict[str, Any],
    tracking: pd.DataFrame,
    daily_projection: pd.DataFrame,
    weekly_projection: pd.DataFrame,
    log: pd.DataFrame,
    accuracy_df: pd.DataFrame,
) -> tuple[str, dict[str, Any]]:
    generated = now_utc().strftime("%Y-%m-%d %H:%M UTC")

    latest = tracking.iloc[-1]
    latest_sol_date = pd.Timestamp(latest["sol_date"]).normalize()
    latest_btc_date = pd.Timestamp(latest["btc_equiv_date"]).normalize()

    current_price = safe_float(latest["sol_close"])
    last_gap = safe_float(latest["error_pct"])

    from_program = tracking[tracking["sol_date"] >= metadata["program_start_date"]].copy()
    last_7 = tracking.tail(7).copy()

    mean_abs_bottom = tracking["abs_error_pct"].mean()
    mean_abs_program = from_program["abs_error_pct"].mean() if not from_program.empty else np.nan
    signed_gap_7 = last_7["error_pct"].mean() if not last_7.empty else np.nan
    mean_abs_gap_7 = last_7["abs_error_pct"].mean() if not last_7.empty else np.nan

    tracking_state = classify_tracking_state(mean_abs_program, last_gap)

    if len(tracking) >= 4:
        recent_change = last_gap - safe_float(tracking.iloc[-4]["error_pct"])
    else:
        recent_change = np.nan

    gap_state = classify_gap_state(last_gap)
    gap_trend = classify_gap_trend(last_gap, recent_change)

    tail_df = format_tracking_tail(tracking, 10)
    projection_table = format_weekly_projection_table(weekly_projection, log)

    if accuracy_df is None or accuracy_df.empty:
        accuracy_df = pd.DataFrame(
            [
                {
                    "Orizzonte": f"{horizon}g",
                    "Controlli": 0,
                    "Dentro banda riancorata": "n/a",
                    "Errore ass. riancorato": "n/a",
                    "Errore ass. ancorato": "n/a",
                }
                for horizon in WEEKLY_HORIZONS
            ]
        )

    report = f"""{START_MARKER}
# Tracking percorso frattale SOL/BTC

Generato: {generated}

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **{metadata['source']}**
- Data corrente: **{latest_sol_date.strftime('%Y-%m-%d')}**
- Bottom SOL usato: **{metadata['sol_bottom_date'].strftime('%Y-%m-%d')}**
- Bottom BTC equivalente: **{metadata['btc_bottom_date'].strftime('%Y-%m-%d')}**
- Giorno BTC equivalente: **{latest_btc_date.strftime('%Y-%m-%d')}**
- Inizio programma/scanner: **{metadata['program_start_date'].strftime('%Y-%m-%d')}**
- Prezzo SOL corrente: **{fmt_price(current_price)}**
- Verdetto principale: **{metadata['verdict']}**
- Somiglianza strutturale: **{fmt_pct(metadata['structural_similarity'])}**
- Aderenza live principale: **{fmt_pct(metadata['live_adherence_score'])}**
- Errore medio live principale: **{fmt_pct(metadata['live_avg_abs_gap_pct'], signed=False)}**
- Peso operativo suggerito: **{metadata['operational_weight']}**
- Fase: **{metadata['phase']}**
- Rischio fase: **{metadata['risk']}**

## Aderenza del percorso ancorato

- Giorni controllati dal bottom: **{len(tracking)}**
- Giorni controllati da inizio programma/scanner: **{len(from_program)}**
- Errore assoluto medio dal bottom: **{fmt_pct(mean_abs_bottom, signed=False)}**
- Errore assoluto medio da inizio programma: **{fmt_pct(mean_abs_program, signed=False)}**
- Gap firmato medio ultimi 7 giorni: **{fmt_pct(signed_gap_7, signed=True)}**
- Errore assoluto medio ultimi 7 giorni: **{fmt_pct(mean_abs_gap_7, signed=False)}**
- Gap ultimo giorno: **{fmt_pct(last_gap, signed=True)}**
- Stato aderenza: **{tracking_state}**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **{fmt_pct(last_gap, signed=True)}**
- Gap firmato medio 7g: **{fmt_pct(signed_gap_7, signed=True)}**
- Errore assoluto medio 7g: **{fmt_pct(mean_abs_gap_7, signed=False)}**
- Variazione recente gap: **{fmt_pct(recent_change, signed=True)}**
- Stato gap: **{gap_state}**
- Trend gap: **{gap_trend}**

Soglie operative del grafico:

- entro **\u00b15%**: percorso vicino;
- tra **\u00b15% e \u00b112%**: deviazione gestibile;
- oltre **\u00b112%**: frattale non abbastanza aderente per conferma operativa;
- oltre **\u00b118%**: disallineamento marcato.

## Ultimi giorni del confronto ancorato

{df_to_markdown(tail_df)}

## Proiezione futura salvata

{df_to_markdown(projection_table)}

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

{df_to_markdown(accuracy_df)}

## Regola di lettura

- La somiglianza strutturale descrive la forma.
- Il gap ancorato descrive la distanza reale dal percorso.
- Lo scenario riancorato non dimostra che il frattale sia valido.
- Prima di pesare il modulo servono milestone maturate e un errore ancorato accettabile.
{END_MARKER}
"""

    metrics = {
        "generated_utc": now_utc().isoformat(),
        "asset": "SOL",
        "source": metadata["source"],
        "current_date": latest_sol_date.strftime("%Y-%m-%d"),
        "current_price": current_price,
        "structural_similarity": metadata["structural_similarity"],
        "main_live_adherence_score": metadata["live_adherence_score"],
        "main_live_avg_abs_gap_pct": metadata["live_avg_abs_gap_pct"],
        "main_operational_weight": metadata["operational_weight"],
        "tracker_days_from_bottom": int(len(tracking)),
        "tracker_live_days": int(len(from_program)),
        "tracker_avg_abs_gap_from_bottom_pct": mean_abs_bottom,
        "tracker_live_avg_abs_gap_pct": mean_abs_program,
        "tracker_signed_gap_7d_pct": signed_gap_7,
        "tracker_avg_abs_gap_7d_pct": mean_abs_gap_7,
        "tracker_last_gap_pct": last_gap,
        "tracker_gap_state": gap_state,
        "tracker_gap_trend": gap_trend,
        "tracker_alignment_state": tracking_state,
    }
    return report, metrics


def write_tracker_metrics(metrics: dict[str, Any]) -> None:
    pd.DataFrame([metrics]).to_csv(TRACKER_METRICS_CSV_PATH, index=False)


def replace_section_in_latest_report(section_text: str) -> None:
    if not MAIN_REPORT_PATH.exists():
        write_text(MAIN_REPORT_PATH, section_text)
        return

    content = read_text(MAIN_REPORT_PATH)

    if START_MARKER in content and END_MARKER in content:
        start_idx = content.index(START_MARKER)
        end_idx = content.index(END_MARKER, start_idx) + len(END_MARKER)
        updated = content[:start_idx] + section_text + content[end_idx:]
    else:
        insert_after = "<!-- LIQUIDATION_SUMMARY_END -->"
        if insert_after in content:
            idx = content.index(insert_after) + len(insert_after)
            updated = content[:idx] + "\n\n" + section_text + "\n" + content[idx:]
        else:
            updated = content.rstrip() + "\n\n" + section_text + "\n"

    write_text(MAIN_REPORT_PATH, updated)


def main() -> None:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)

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

    report_text, metrics = build_report(
        metadata=metadata,
        tracking=tracking,
        daily_projection=daily_projection,
        weekly_projection=weekly_projection,
        log=log,
        accuracy_df=accuracy_df,
    )

    write_text(REPORT_PATH, report_text)
    write_tracker_metrics(metrics)
    replace_section_in_latest_report(report_text)

    latest = tracking.iloc[-1]

    print(f"Report scritto in: {REPORT_PATH}")
    print(f"Latest report aggiornato: {MAIN_REPORT_PATH}")
    print(f"CSV tracking completo: {TRACKING_FULL_CSV_PATH}")
    print(f"CSV proiezione futura: {FUTURE_DAILY_CSV_PATH}")
    print(f"CSV log proiezioni: {PROJECTION_LOG_CSV_PATH}")
    print(f"Metriche tracker: {TRACKER_METRICS_CSV_PATH}")
    print(f"Ultima data SOL: {pd.Timestamp(latest['sol_date']).strftime('%Y-%m-%d')}")
    print(f"Prezzo SOL: {safe_float(latest['sol_close']):.4f}")
    print(f"Gap ancorato ultimo: {safe_float(latest['error_pct']):.2f}%")
    print(f"Verdetto letto: {metadata['verdict']}")
    print(f"Peso operativo letto: {metadata['operational_weight']}")


if __name__ == "__main__":
    main()
