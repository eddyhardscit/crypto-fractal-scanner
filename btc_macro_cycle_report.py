# -*- coding: utf-8 -*-
"""Bitcoin Power Law, four-year spiral and cycle-context report.

This module is deliberately macro and diagnostic. It does not add points to
Global Confluence. It separates three questions:

* Power law: where is BTC relative to a long-run log/log growth corridor?
* Spiral: where is BTC in the repeating four-year calendar layout?
* Cycle phase: what happened after the same phase of earlier halving cycles?

SOL/BTC and DOGE/BTC are also projected on the same four-year angle as context,
without fitting a separate power law to either altcoin.
"""

from __future__ import annotations

import csv
import math
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

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

try:
    from relative_strength_btc_report import load_pair
except Exception:
    load_pair = None


REPORTS_DIR = Path("reports")
LATEST_REPORT = REPORTS_DIR / "latest_report.md"
REPORT_PATH = REPORTS_DIR / "btc_macro_cycle_report.md"
POWER_METRICS_PATH = REPORTS_DIR / "btc_power_law_metrics.csv"
POWER_BACKTEST_PATH = REPORTS_DIR / "btc_power_law_backtest.csv"
CYCLE_METRICS_PATH = REPORTS_DIR / "btc_cycle_phase_metrics.csv"
HISTORY_PATH = REPORTS_DIR / "btc_macro_cycle_history.csv"
TRACKER_PATH = REPORTS_DIR / "btc_macro_cycle_tracker_metrics.csv"

POWER_CHART = REPORTS_DIR / "btc_power_law_chart.png"
POWER_LOGLOG_CHART = REPORTS_DIR / "btc_power_law_loglog_chart.png"
SPIRAL_CHART = REPORTS_DIR / "bitcoin_four_year_spiral.png"
ALT_SPIRAL_CHART = REPORTS_DIR / "alt_btc_cycle_spirals.png"

START_MARKER = "<!-- BTC_MACRO_CYCLE_START -->"
END_MARKER = "<!-- BTC_MACRO_CYCLE_END -->"

BTC_TICKER = "BTC-USD"
GENESIS_DATE = pd.Timestamp("2009-01-03")
CALENDAR_CYCLE_ANCHOR = pd.Timestamp("2009-01-01")
FOUR_YEAR_DAYS = 365.2425 * 4.0

HALVINGS = [
    pd.Timestamp("2012-11-28"),
    pd.Timestamp("2016-07-09"),
    pd.Timestamp("2020-05-11"),
    pd.Timestamp("2024-04-19"),
]
# Only confirmed historical macro-bottom dates are marked. The current cycle is
# not labelled until history makes it unambiguous.
MACRO_BOTTOMS = [
    pd.Timestamp("2015-01-14"),
    pd.Timestamp("2018-12-15"),
    pd.Timestamp("2022-11-21"),
]

POWER_BACKTEST_HORIZONS = (90, 180, 365, 730)
LIVE_TRACKER_HORIZONS = (90, 180, 365)


class DataError(RuntimeError):
    pass


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def utc_now_str() -> str:
    return utc_now().strftime("%Y-%m-%d %H:%M UTC")


def ensure_reports() -> None:
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)


def safe_float(value: Any, default: float | None = None) -> float | None:
    try:
        number = float(value)
        if not math.isfinite(number):
            return default
        return number
    except Exception:
        return default


def fmt_money(value: Any) -> str:
    number = safe_float(value)
    if number is None:
        return "n/a"
    if number >= 1000:
        return f"{number:,.0f} $".replace(",", ".")
    return f"{number:.2f} $".replace(".", ",")


def fmt_pct(value: Any, signed: bool = True) -> str:
    number = safe_float(value)
    if number is None:
        return "n/a"
    text = f"{number:+.2f}%" if signed else f"{number:.2f}%"
    return text.replace(".", ",")


def fmt_number(value: Any, digits: int = 3) -> str:
    number = safe_float(value)
    if number is None:
        return "n/a"
    return f"{number:.{digits}f}".replace(".", ",")


def atomic_write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(text, encoding="utf-8", newline="\n")
    tmp.replace(path)


def read_text(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def replace_block(text: str, block: str) -> str:
    wrapped = f"{START_MARKER}\n{block.rstrip()}\n{END_MARKER}"
    if START_MARKER in text and END_MARKER in text:
        pattern = re.compile(
            re.escape(START_MARKER) + r".*?" + re.escape(END_MARKER),
            flags=re.DOTALL,
        )
        return pattern.sub(wrapped, text, count=1)

    relative_start = "<!-- RELATIVE_STRENGTH_BTC_START -->"
    if relative_start in text:
        return text.replace(relative_start, wrapped + "\n\n" + relative_start, 1)

    global_start = "<!-- GLOBAL_CONFLUENCE_START -->"
    if global_start in text:
        return text.replace(global_start, wrapped + "\n\n" + global_start, 1)

    decision_end = "<!-- DECISION_REPORT_END -->"
    if decision_end in text:
        return text.replace(decision_end, decision_end + "\n\n" + wrapped, 1)

    return wrapped + "\n\n" + text


def normalise_frame(frame: pd.DataFrame) -> pd.DataFrame:
    if frame is None or frame.empty:
        return pd.DataFrame()
    out = frame.copy()
    if isinstance(out.columns, pd.MultiIndex):
        out.columns = [column[0] if isinstance(column, tuple) else column for column in out.columns]
    renamed = {}
    for column in out.columns:
        key = str(column).strip().lower()
        if key == "close":
            renamed[column] = "Close"
        elif key == "open":
            renamed[column] = "Open"
        elif key == "high":
            renamed[column] = "High"
        elif key == "low":
            renamed[column] = "Low"
        elif key == "volume":
            renamed[column] = "Volume"
    out = out.rename(columns=renamed)
    if "Close" not in out.columns:
        return pd.DataFrame()
    out["Close"] = pd.to_numeric(out["Close"], errors="coerce")
    for column in ("Open", "High", "Low"):
        if column not in out.columns:
            out[column] = out["Close"]
        else:
            out[column] = pd.to_numeric(out[column], errors="coerce")
    if "Volume" not in out.columns:
        out["Volume"] = np.nan
    out.index = pd.to_datetime(out.index, utc=True, errors="coerce").tz_convert(None)
    out = out[~out.index.isna()].sort_index()
    out = out[~out.index.duplicated(keep="last")]
    out = out.replace([np.inf, -np.inf], np.nan).dropna(subset=["Close"])
    out = out[out["Close"] > 0]
    return out[["Open", "High", "Low", "Close", "Volume"]]


def download_btc() -> pd.DataFrame:
    errors: list[str] = []
    try:
        raw = yf.Ticker(BTC_TICKER).history(period="max", interval="1d", auto_adjust=False, actions=False)
        frame = normalise_frame(raw)
        if len(frame) >= 1000:
            return frame
    except Exception as exc:
        errors.append(f"Ticker.history {type(exc).__name__}: {exc}")
    try:
        raw = yf.download(
            BTC_TICKER,
            period="max",
            interval="1d",
            auto_adjust=False,
            actions=False,
            progress=False,
            threads=False,
        )
        frame = normalise_frame(raw)
        if len(frame) >= 1000:
            return frame
    except Exception as exc:
        errors.append(f"download {type(exc).__name__}: {exc}")
    raise DataError("BTC-USD non disponibile con storia sufficiente. " + " | ".join(errors))


def power_coordinates(frame: pd.DataFrame) -> tuple[np.ndarray, np.ndarray, pd.DatetimeIndex]:
    clean = frame[frame["Close"] > 0].copy()
    days = (clean.index.normalize() - GENESIS_DATE).days.astype(float)
    mask = days > 30
    days = np.asarray(days[mask], dtype=float)
    prices = clean.loc[mask, "Close"].to_numpy(dtype=float)
    dates = clean.loc[mask].index
    return np.log(days), np.log(prices), dates


def fit_power_law(frame: pd.DataFrame) -> dict[str, Any]:
    x, y, dates = power_coordinates(frame)
    if len(x) < 500:
        raise DataError("Campione insufficiente per Power Law.")
    beta, intercept = np.polyfit(x, y, 1)
    fitted = intercept + beta * x
    residuals = y - fitted
    quantiles = {q: float(np.quantile(residuals, q)) for q in (0.10, 0.25, 0.50, 0.75, 0.90)}
    r2 = 1.0 - float(np.sum((y - fitted) ** 2) / np.sum((y - y.mean()) ** 2))
    return {
        "beta": float(beta),
        "intercept": float(intercept),
        "residual_quantiles": quantiles,
        "r2_loglog": r2,
        "start_date": dates[0],
        "end_date": dates[-1],
        "observations": len(x),
    }


def predict_power(fit: dict[str, Any], dates: pd.DatetimeIndex | list[pd.Timestamp], quantile: float = 0.50) -> np.ndarray:
    dates_index = pd.DatetimeIndex(dates)
    days = (dates_index.normalize() - GENESIS_DATE).days.to_numpy(dtype=float)
    days = np.maximum(days, 1.0)
    q = fit["residual_quantiles"].get(quantile, 0.0)
    log_price = fit["intercept"] + fit["beta"] * np.log(days) + q
    return np.exp(log_price)


def current_power_position(frame: pd.DataFrame, fit: dict[str, Any]) -> dict[str, Any]:
    current_date = frame.index[-1]
    current_price = float(frame["Close"].iloc[-1])
    days = max((current_date.normalize() - GENESIS_DATE).days, 1)
    base_log = fit["intercept"] + fit["beta"] * math.log(days)
    residual = math.log(current_price) - base_log
    residuals = np.array(list(fit["residual_quantiles"].values()))
    # Percentile is estimated against the full residual distribution below.
    x, y, _ = power_coordinates(frame)
    full_residuals = y - (fit["intercept"] + fit["beta"] * x)
    percentile = float((full_residuals <= residual).mean() * 100.0)
    q50_price = float(predict_power(fit, [current_date], 0.50)[0])
    q10_price = float(predict_power(fit, [current_date], 0.10)[0])
    q90_price = float(predict_power(fit, [current_date], 0.90)[0])
    deviation = (current_price / q50_price - 1.0) * 100.0
    # The corridor is defined by the actual p10 and p90 price bands.
    # Residual percentile is used only after confirming that price is inside.
    if current_price < q10_price:
        zone = "SOTTO LA BANDA P10"
    elif current_price > q90_price:
        zone = "SOPRA LA BANDA P90"
    elif percentile <= 20:
        zone = "BASSA NEL CORRIDOIO"
    elif percentile >= 80:
        zone = "ALTA NEL CORRIDOIO"
    else:
        zone = "CENTRALE NEL CORRIDOIO"
    return {
        "current_date": current_date,
        "current_price": current_price,
        "central_price": q50_price,
        "lower_price": q10_price,
        "upper_price": q90_price,
        "deviation_from_central_pct": deviation,
        "residual_percentile": percentile,
        "zone": zone,
    }


def fit_stability(frame: pd.DataFrame) -> dict[str, Any]:
    fits: list[dict[str, Any]] = []
    for year in (2014, 2015, 2016, 2017, 2018):
        subset = frame[frame.index >= pd.Timestamp(f"{year}-01-01")]
        if len(subset) < 800:
            continue
        try:
            result = fit_power_law(subset)
            fits.append({"start_year": year, "beta": result["beta"], "r2": result["r2_loglog"]})
        except Exception:
            continue
    betas = [item["beta"] for item in fits]
    if not betas:
        return {"fits": [], "beta_range": np.nan, "label": "NON DISPONIBILE"}
    beta_range = max(betas) - min(betas)
    if beta_range <= 0.15:
        label = "ALTA"
    elif beta_range <= 0.35:
        label = "MEDIA"
    else:
        label = "BASSA"
    return {"fits": fits, "beta_range": beta_range, "label": label}


def nearest_close(frame: pd.DataFrame, date: pd.Timestamp, tolerance_days: int = 7) -> float | None:
    if date in frame.index:
        return safe_float(frame.loc[date, "Close"])
    rows = frame[(frame.index >= date) & (frame.index <= date + pd.Timedelta(days=tolerance_days))]
    if rows.empty:
        return None
    return safe_float(rows["Close"].iloc[0])


def power_backtest(frame: pd.DataFrame) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    detailed: list[dict[str, Any]] = []
    summary: list[dict[str, Any]] = []
    start_cut = max(frame.index[0] + pd.Timedelta(days=3 * 365), pd.Timestamp("2018-01-01"))
    end_cut = frame.index[-1] - pd.Timedelta(days=max(POWER_BACKTEST_HORIZONS) + 10)
    cut_dates = pd.date_range(start_cut, end_cut, freq="MS")

    for cut in cut_dates:
        train = frame[frame.index <= cut]
        if len(train) < 800:
            continue
        try:
            fit = fit_power_law(train)
        except Exception:
            continue
        cut_price = nearest_close(frame, cut)
        if cut_price is None:
            continue
        for horizon in POWER_BACKTEST_HORIZONS:
            target_date = cut + pd.Timedelta(days=horizon)
            actual = nearest_close(frame, target_date)
            if actual is None:
                continue
            predicted = float(predict_power(fit, [target_date], 0.50)[0])
            model_log_error = abs(math.log(actual / predicted))
            naive_log_error = abs(math.log(actual / cut_price))
            detailed.append(
                {
                    "cut_date": cut.date().isoformat(),
                    "target_date": target_date.date().isoformat(),
                    "horizon_days": horizon,
                    "cut_price": cut_price,
                    "predicted_price": predicted,
                    "actual_price": actual,
                    "model_abs_error_pct": (math.exp(model_log_error) - 1.0) * 100.0,
                    "naive_abs_error_pct": (math.exp(naive_log_error) - 1.0) * 100.0,
                    "model_beats_naive": int(model_log_error < naive_log_error),
                }
            )

    for horizon in POWER_BACKTEST_HORIZONS:
        rows = [row for row in detailed if row["horizon_days"] == horizon]
        if not rows:
            summary.append(
                {
                    "horizon_days": horizon,
                    "controls": 0,
                    "win_rate_vs_naive_pct": np.nan,
                    "median_model_error_pct": np.nan,
                    "median_naive_error_pct": np.nan,
                }
            )
            continue
        summary.append(
            {
                "horizon_days": horizon,
                "controls": len(rows),
                "win_rate_vs_naive_pct": sum(row["model_beats_naive"] for row in rows) / len(rows) * 100.0,
                "median_model_error_pct": float(np.median([row["model_abs_error_pct"] for row in rows])),
                "median_naive_error_pct": float(np.median([row["naive_abs_error_pct"] for row in rows])),
            }
        )
    return detailed, summary


def four_year_angle(dates: pd.DatetimeIndex | list[pd.Timestamp]) -> np.ndarray:
    index = pd.DatetimeIndex(dates)
    elapsed = (index.normalize() - CALENDAR_CYCLE_ANCHOR).days.to_numpy(dtype=float)
    phase = np.mod(elapsed / FOUR_YEAR_DAYS, 1.0)
    return phase * 2.0 * np.pi


def last_halving(current_date: pd.Timestamp) -> pd.Timestamp:
    eligible = [date for date in HALVINGS if date <= current_date]
    if not eligible:
        return HALVINGS[0]
    return eligible[-1]


def cycle_phase_metrics(frame: pd.DataFrame) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    current_date = frame.index[-1].normalize()
    current_price = float(frame["Close"].iloc[-1])
    last = last_halving(current_date)
    days_since = int((current_date - last).days)
    phase = min(max(days_since / FOUR_YEAR_DAYS, 0.0), 1.0)
    current = {
        "current_date": current_date,
        "last_halving": last,
        "days_since_halving": days_since,
        "cycle_phase_pct": phase * 100.0,
        "current_price": current_price,
    }

    cycle_rows: list[dict[str, Any]] = []
    completed = [(HALVINGS[i], HALVINGS[i + 1]) for i in range(len(HALVINGS) - 1)]
    for start, end in completed:
        duration = (end - start).days
        analog_date = start + pd.Timedelta(days=round(duration * phase))
        analog_price = nearest_close(frame, analog_date)
        if analog_price is None:
            continue
        row = {
            "cycle_start": start.date().isoformat(),
            "cycle_end": end.date().isoformat(),
            "analog_date": analog_date.date().isoformat(),
            "analog_price": analog_price,
        }
        for horizon in (30, 90, 180, 365):
            future = nearest_close(frame, analog_date + pd.Timedelta(days=horizon))
            row[f"return_{horizon}d_pct"] = (future / analog_price - 1.0) * 100.0 if future else np.nan
        cycle_rows.append(row)
    return current, cycle_rows


def detect_ath_markers(frame: pd.DataFrame) -> pd.DataFrame:
    monthly = frame["Close"].resample("MS").max().dropna()
    running = monthly.cummax()
    ath = monthly[monthly >= running * 0.999999]
    points = []
    for month, price in ath.items():
        rows = frame[(frame.index >= month) & (frame.index < month + pd.offsets.MonthBegin(1))]
        if rows.empty:
            continue
        date = rows["Close"].idxmax()
        points.append({"date": date, "price": float(rows.loc[date, "Close"])})
    return pd.DataFrame(points)


def nearest_date_row(frame: pd.DataFrame, target: pd.Timestamp, days: int = 10) -> tuple[pd.Timestamp, float] | None:
    rows = frame[(frame.index >= target - pd.Timedelta(days=days)) & (frame.index <= target + pd.Timedelta(days=days))]
    if rows.empty:
        return None
    idx = min(rows.index, key=lambda value: abs((value - target).days))
    return idx, float(rows.loc[idx, "Close"])


def plot_power_law(frame: pd.DataFrame, fit: dict[str, Any]) -> None:
    if not CHARTS_AVAILABLE:
        return
    dates = frame.index
    central = predict_power(fit, dates, 0.50)
    low = predict_power(fit, dates, 0.10)
    high = predict_power(fit, dates, 0.90)
    q25 = predict_power(fit, dates, 0.25)
    q75 = predict_power(fit, dates, 0.75)

    fig, ax = plt.subplots(figsize=(14, 8))
    ax.plot(dates, frame["Close"], label="BTC reale", linewidth=1.2)
    ax.plot(dates, central, label="Power Law centrale", linewidth=1.4)
    ax.fill_between(dates, low, high, alpha=0.15, label="Banda p10-p90")
    ax.fill_between(dates, q25, q75, alpha=0.20, label="Banda p25-p75")
    ax.set_yscale("log")
    ax.set_title("Bitcoin Power Law — corridoio macro, non segnale tattico")
    ax.set_ylabel("Prezzo BTC (scala log)")
    ax.grid(True, alpha=0.25)
    ax.legend(loc="best")
    fig.tight_layout()
    fig.savefig(POWER_CHART, dpi=160, bbox_inches="tight")
    plt.close(fig)

    x, y, _ = power_coordinates(frame)
    fitted = fit["intercept"] + fit["beta"] * x + fit["residual_quantiles"][0.50]
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.scatter(x, y, s=3, alpha=0.35, label="Dati giornalieri")
    ax.plot(x, fitted, linewidth=1.6, label="Retta log-log")
    ax.set_title("Bitcoin Power Law — vista log-log")
    ax.set_xlabel("log(giorni dal genesis)")
    ax.set_ylabel("log(prezzo)")
    ax.grid(True, alpha=0.25)
    ax.legend(loc="best")
    fig.tight_layout()
    fig.savefig(POWER_LOGLOG_CHART, dpi=160, bbox_inches="tight")
    plt.close(fig)


def plot_spiral(frame: pd.DataFrame) -> None:
    if not CHARTS_AVAILABLE:
        return
    theta = four_year_angle(frame.index)
    log_price = np.log10(frame["Close"].to_numpy(dtype=float))
    min_exp = math.floor(np.nanmin(log_price))
    max_exp = math.ceil(np.nanmax(log_price))
    radial = log_price - min_exp + 0.25

    fig = plt.figure(figsize=(11, 11))
    ax = fig.add_subplot(111, projection="polar")
    ax.set_theta_zero_location("N")
    ax.set_theta_direction(-1)
    ax.plot(theta, radial, linewidth=1.25, label="Bitcoin")

    ath = detect_ath_markers(frame)
    if not ath.empty:
        ath_theta = four_year_angle(pd.DatetimeIndex(ath["date"]))
        ath_radial = np.log10(ath["price"].to_numpy(dtype=float)) - min_exp + 0.25
        ax.scatter(ath_theta, ath_radial, s=18, label="ATH")

    for target in MACRO_BOTTOMS:
        point = nearest_date_row(frame, target)
        if point:
            date, price = point
            ax.scatter(four_year_angle([date]), [math.log10(price) - min_exp + 0.25], s=38, label="Bottom" if target == MACRO_BOTTOMS[0] else None)

    for target in HALVINGS:
        point = nearest_date_row(frame, target)
        if point:
            date, price = point
            ax.scatter(four_year_angle([date]), [math.log10(price) - min_exp + 0.25], s=38, label="Halving" if target == HALVINGS[0] else None)

    current_date = frame.index[-1]
    current_price = float(frame["Close"].iloc[-1])
    ax.scatter(four_year_angle([current_date]), [math.log10(current_price) - min_exp + 0.25], s=75, marker="*", label="Oggi")

    ticks = list(range(min_exp, max_exp + 1))
    ax.set_yticks([tick - min_exp + 0.25 for tick in ticks])
    ax.set_yticklabels([f"${10 ** tick:,.0f}".replace(",", ".") for tick in ticks])
    ax.set_xticks([0, np.pi / 2, np.pi, 3 * np.pi / 2])
    ax.set_xticklabels(["2009, '13, '17, '21, '25", "2010, '14, '18, '22, '26", "2011, '15, '19, '23, '27", "2012, '16, '20, '24, '28"])
    ax.set_title("Bitcoin Four-Year Spiral\nangolo = tempo; raggio = prezzo logaritmico", pad=28)
    ax.grid(True, alpha=0.3)
    ax.legend(loc="upper right", bbox_to_anchor=(1.22, 1.14))
    fig.tight_layout()
    fig.savefig(SPIRAL_CHART, dpi=170, bbox_inches="tight")
    plt.close(fig)


def plot_alt_spirals() -> list[dict[str, Any]]:
    summaries: list[dict[str, Any]] = []
    if not CHARTS_AVAILABLE or load_pair is None:
        return summaries
    fig, axes = plt.subplots(1, 2, figsize=(16, 8), subplot_kw={"projection": "polar"})
    created = 0
    for ax, asset in zip(axes, ("SOL", "DOGE")):
        try:
            pair = load_pair(asset)
            frame = pair.frame.dropna(subset=["Close"])
            theta = four_year_angle(frame.index)
            log_ratio = np.log10(frame["Close"].to_numpy(dtype=float))
            shift = math.floor(np.nanmin(log_ratio))
            radial = log_ratio - shift + 0.2
            ax.set_theta_zero_location("N")
            ax.set_theta_direction(-1)
            ax.plot(theta, radial, linewidth=1.15)
            current = float(frame["Close"].iloc[-1])
            ax.scatter(four_year_angle([frame.index[-1]]), [math.log10(current) - shift + 0.2], marker="*", s=70, label="Oggi")
            ticks_raw = np.linspace(np.nanmin(log_ratio), np.nanmax(log_ratio), 5)
            ax.set_yticks(ticks_raw - shift + 0.2)
            ax.set_yticklabels([f"{10 ** tick:.6g}" for tick in ticks_raw])
            ax.set_xticks([0, np.pi / 2, np.pi, 3 * np.pi / 2])
            ax.set_xticklabels(["Anno 1", "Anno 2", "Anno 3", "Anno 4"])
            ax.set_title(f"{asset}/BTC nel ciclo quadriennale")
            ax.legend(loc="upper right")
            summaries.append(
                {
                    "asset": asset,
                    "pair": f"{asset}/BTC",
                    "current_ratio": current,
                    "source": pair.source,
                    "synthetic": pair.synthetic,
                }
            )
            created += 1
        except Exception as exc:
            ax.set_title(f"{asset}/BTC non disponibile")
            ax.text(0.5, 0.5, str(exc)[:120], transform=ax.transAxes, ha="center", va="center")
    if created:
        fig.suptitle("Altcoin dentro il tempo del ciclo Bitcoin — contesto, non previsione")
        fig.tight_layout()
        fig.savefig(ALT_SPIRAL_CHART, dpi=160, bbox_inches="tight")
    plt.close(fig)
    return summaries


def read_relative_metrics() -> list[dict[str, str]]:
    path = REPORTS_DIR / "relative_strength_btc_metrics.csv"
    if not path.exists():
        return []
    try:
        with path.open("r", encoding="utf-8", newline="") as handle:
            return list(csv.DictReader(handle))
    except Exception:
        return []


def write_csv(path: Path, rows: Iterable[dict[str, Any]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    with tmp.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow({key: row.get(key, "") for key in fieldnames})
    tmp.replace(path)


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    try:
        with path.open("r", encoding="utf-8", newline="") as handle:
            return list(csv.DictReader(handle))
    except Exception:
        return []


def freeze_history(position: dict[str, Any], cycle: dict[str, Any], fit: dict[str, Any]) -> None:
    fields = [
        "signal_date",
        "generated_utc",
        "btc_price",
        "power_central_price",
        "power_lower_price",
        "power_upper_price",
        "power_percentile",
        "power_deviation_pct",
        "power_beta",
        "cycle_phase_pct",
        "days_since_halving",
        "global_weight",
    ]
    rows = read_csv(HISTORY_PATH)
    today = position["current_date"].date().isoformat()
    month_key = today[:7]

    # Power Law is a macro model. Freeze the first valid live forecast of each
    # UTC calendar month so daily reruns are not counted as independent calls.
    def row_month(row: dict[str, str]) -> str:
        value = str(row.get("signal_date", "")).strip()
        try:
            return datetime.fromisoformat(value[:10]).strftime("%Y-%m")
        except (TypeError, ValueError):
            return ""

    if not any(row_month(row) == month_key for row in rows):
        rows.append(
            {
                "signal_date": today,
                "generated_utc": utc_now().isoformat(),
                "btc_price": position["current_price"],
                "power_central_price": position["central_price"],
                "power_lower_price": position["lower_price"],
                "power_upper_price": position["upper_price"],
                "power_percentile": position["residual_percentile"],
                "power_deviation_pct": position["deviation_from_central_pct"],
                "power_beta": fit["beta"],
                "cycle_phase_pct": cycle["cycle_phase_pct"],
                "days_since_halving": cycle["days_since_halving"],
                "global_weight": 0,
            }
        )
    rows.sort(key=lambda row: row.get("signal_date", ""))
    write_csv(HISTORY_PATH, rows, fields)


def update_live_tracker(frame: pd.DataFrame) -> list[dict[str, Any]]:
    history = read_csv(HISTORY_PATH)
    latest = frame.index[-1].normalize()
    output: list[dict[str, Any]] = []
    for horizon in LIVE_TRACKER_HORIZONS:
        checks = []
        for row in history:
            try:
                start = pd.Timestamp(row["signal_date"])
                target = start + pd.Timedelta(days=horizon)
            except Exception:
                continue
            if target > latest:
                continue
            actual = nearest_close(frame, target)
            predicted = safe_float(row.get("power_central_price"))
            start_price = safe_float(row.get("btc_price"))
            if actual is None or predicted is None or start_price is None or min(actual, predicted, start_price) <= 0:
                continue
            model_err = abs(math.log(actual / predicted))
            naive_err = abs(math.log(actual / start_price))
            checks.append(
                {
                    "model_error_pct": (math.exp(model_err) - 1.0) * 100.0,
                    "naive_error_pct": (math.exp(naive_err) - 1.0) * 100.0,
                    "win": float(model_err < naive_err),
                }
            )
        output.append(
            {
                "generated_utc": utc_now().isoformat(),
                "horizon_days": horizon,
                "controls": len(checks),
                "win_rate_vs_naive_pct": np.mean([item["win"] for item in checks]) * 100.0 if checks else np.nan,
                "median_model_error_pct": np.median([item["model_error_pct"] for item in checks]) if checks else np.nan,
                "median_naive_error_pct": np.median([item["naive_error_pct"] for item in checks]) if checks else np.nan,
                "state": "RACCOLTA LIVE / PESO 0",
                "global_weight": 0,
            }
        )
    write_csv(
        TRACKER_PATH,
        output,
        ["generated_utc", "horizon_days", "controls", "win_rate_vs_naive_pct", "median_model_error_pct", "median_naive_error_pct", "state", "global_weight"],
    )
    return output


def md_table(headers: list[str], rows: list[list[Any]]) -> str:
    lines = ["| " + " | ".join(headers) + " |", "| " + " | ".join(["---"] * len(headers)) + " |"]
    for row in rows:
        lines.append("| " + " | ".join(str(item) for item in row) + " |")
    return "\n".join(lines)


def build_report(
    fit: dict[str, Any],
    position: dict[str, Any],
    stability: dict[str, Any],
    power_summary: list[dict[str, Any]],
    cycle: dict[str, Any],
    cycle_rows: list[dict[str, Any]],
    tracker: list[dict[str, Any]],
    alt_summaries: list[dict[str, Any]],
) -> str:
    relative = read_relative_metrics()
    lines: list[str] = []
    lines.append("# Bitcoin Macro Cycle — Power Law e Four-Year Spiral")
    lines.append("")
    lines.append(f"Generato: {utc_now_str()}")
    lines.append("")
    lines.append(
        "Questo modulo descrive il contesto macro di Bitcoin. Non genera entrate tattiche, non autorizza leva e pesa **0** nel Global Confluence."
    )
    lines.append("")
    lines.append("## Sintesi")
    lines.append("")
    lines.append(
        md_table(
            ["Voce", "Valore", "Lettura"],
            [
                ["Prezzo BTC", fmt_money(position["current_price"]), "prezzo corrente"],
                ["Power Law centrale", fmt_money(position["central_price"]), f"deviazione {fmt_pct(position['deviation_from_central_pct'])}"],
                ["Banda p10-p90", f"{fmt_money(position['lower_price'])} / {fmt_money(position['upper_price'])}", position["zone"]],
                ["Percentile residuo", fmt_pct(position["residual_percentile"], signed=False), "posizione storica nel corridoio"],
                ["Esponente β", fmt_number(fit["beta"], 4), f"R² log-log {fmt_pct(fit['r2_loglog'] * 100.0, signed=False)}"],
                ["Stabilità β", stability["label"], f"range {fmt_number(stability.get('beta_range'), 4)} cambiando finestra"],
                ["Ultimo halving", cycle["last_halving"].date().isoformat(), f"{cycle['days_since_halving']} giorni fa"],
                ["Fase ciclo", fmt_pct(cycle["cycle_phase_pct"], signed=False), "percentuale indicativa del ciclo quadriennale"],
                ["Peso Global", "0", "CONTESTO MACRO / DIAGNOSTICO"],
            ],
        )
    )
    lines.append("")
    lines.append(
        "La Power Law viene trattata come regressione empirica, non come legge fisica. Il report mostra quanto cambia l'esponente usando finestre iniziali diverse e la confronta con il benchmark ingenuo 'prezzo invariato'."
    )
    lines.append("")

    lines.append("## Bitcoin Power Law")
    lines.append("")
    lines.append(f"- Campione: {fit['start_date'].date().isoformat()} → {fit['end_date'].date().isoformat()} ({fit['observations']} osservazioni)")
    lines.append(f"- Formula stimata: prezzo ≈ exp({fit['intercept']:.4f}) × giorni^{fit['beta']:.4f}")
    lines.append(f"- Prezzo centrale oggi: **{fmt_money(position['central_price'])}**")
    lines.append(f"- Posizione corrente: **{position['zone']}**, percentile {fmt_pct(position['residual_percentile'], signed=False)}")
    lines.append(f"- Scarto dal centro: **{fmt_pct(position['deviation_from_central_pct'])}**")
    lines.append("")
    if POWER_CHART.exists():
        lines.append(f"![Bitcoin Power Law]({POWER_CHART.name})")
        lines.append("")
    if POWER_LOGLOG_CHART.exists():
        lines.append(f"![Bitcoin Power Law log-log]({POWER_LOGLOG_CHART.name})")
        lines.append("")

    lines.append("### Stabilità dell'esponente")
    lines.append("")
    stability_rows = []
    for item in stability.get("fits", []):
        stability_rows.append([item["start_year"], fmt_number(item["beta"], 4), fmt_pct(item["r2"] * 100.0, signed=False)])
    lines.append(md_table(["Inizio campione", "β", "R² log-log"], stability_rows or [["n/a", "n/a", "n/a"]]))
    lines.append("")

    lines.append("### Backtest walk-forward contro prezzo invariato")
    lines.append("")
    back_rows = []
    for row in power_summary:
        back_rows.append(
            [
                f"{row['horizon_days']}g",
                row["controls"],
                fmt_pct(row["win_rate_vs_naive_pct"], signed=False),
                fmt_pct(row["median_model_error_pct"], signed=False),
                fmt_pct(row["median_naive_error_pct"], signed=False),
            ]
        )
    lines.append(md_table(["Orizzonte", "Controlli", "Vittorie vs naive", "Errore mediano modello", "Errore mediano naive"], back_rows))
    lines.append("")

    lines.append("## Bitcoin Four-Year Spiral")
    lines.append("")
    lines.append(
        "Nel grafico l'angolo rappresenta il tempo dentro una finestra di quattro anni e il raggio rappresenta il prezzo in scala logaritmica. "
        "ATH, bottom storici e halving sono marker descrittivi: la spirale rende visibili le ricorrenze, ma non dimostra che il ciclo futuro debba ripetersi."
    )
    lines.append("")
    if SPIRAL_CHART.exists():
        lines.append(f"![Bitcoin Four-Year Spiral]({SPIRAL_CHART.name})")
        lines.append("")

    lines.append("## Stessa fase dei cicli halving precedenti")
    lines.append("")
    cycle_table = []
    for row in cycle_rows:
        cycle_table.append(
            [
                f"{row['cycle_start']} → {row['cycle_end']}",
                row["analog_date"],
                fmt_pct(row.get("return_30d_pct")),
                fmt_pct(row.get("return_90d_pct")),
                fmt_pct(row.get("return_180d_pct")),
                fmt_pct(row.get("return_365d_pct")),
            ]
        )
    lines.append(md_table(["Ciclo", "Data analoga", "+30g", "+90g", "+180g", "+365g"], cycle_table or [["n/a", "n/a", "n/a", "n/a", "n/a", "n/a"]]))
    lines.append("")
    lines.append("Campione molto piccolo: questi rendimenti sono contesto di ciclo, non probabilità affidabili.")
    lines.append("")

    lines.append("## SOL/BTC e DOGE/BTC dentro il tempo Bitcoin")
    lines.append("")
    if ALT_SPIRAL_CHART.exists():
        lines.append(f"![Altcoin nel ciclo BTC]({ALT_SPIRAL_CHART.name})")
        lines.append("")
    alt_rows = []
    for row in relative:
        alt_rows.append(
            [
                row.get("asset", "n/a"),
                row.get("pair", "n/a"),
                row.get("bias", "n/a"),
                row.get("raw_score", "0"),
                row.get("candidate_score", "0"),
                row.get("ret_30d_pct", "n/a"),
                "0",
            ]
        )
    if not alt_rows:
        for item in alt_summaries:
            alt_rows.append([item["asset"], item["pair"], "CONTESTO GRAFICO", "n/a", "0", "n/a", "0"])
    lines.append(md_table(["Asset", "Coppia", "Forza vs BTC", "Score raw", "Candidato", "30g", "Peso Global"], alt_rows or [["n/a", "n/a", "n/a", "n/a", "n/a", "n/a", "0"]]))
    lines.append("")

    lines.append("## Tracker live Power Law")
    lines.append("")
    live_rows = []
    for row in tracker:
        live_rows.append(
            [
                f"{row['horizon_days']}g",
                row["controls"],
                fmt_pct(row["win_rate_vs_naive_pct"], signed=False),
                fmt_pct(row["median_model_error_pct"], signed=False),
                fmt_pct(row["median_naive_error_pct"], signed=False),
                row["state"],
            ]
        )
    lines.append(md_table(["Orizzonte", "Controlli", "Vittorie vs naive", "Errore modello", "Errore naive", "Stato"], live_rows))
    lines.append("")
    lines.append("Il modulo resta a peso 0 anche con un buon backtest. Prima si osserva la verifica live, poi si decide se usarlo soltanto per il rischio macro di lungo periodo. Le fotografie live della Power Law vengono salvate una sola volta per mese, così non si contano come indipendenti previsioni giornaliere quasi identiche.")
    lines.append("")
    lines.append("## File prodotti")
    lines.append("")
    for path in (POWER_METRICS_PATH, POWER_BACKTEST_PATH, CYCLE_METRICS_PATH, HISTORY_PATH, TRACKER_PATH):
        lines.append(f"- `{path}`")
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    ensure_reports()
    frame = download_btc()
    fit = fit_power_law(frame)
    position = current_power_position(frame, fit)
    stability = fit_stability(frame)
    detailed_backtest, summary_backtest = power_backtest(frame)
    cycle, cycle_rows = cycle_phase_metrics(frame)

    plot_power_law(frame, fit)
    plot_spiral(frame)
    alt_summaries = plot_alt_spirals()

    metrics_row = {
        "generated_utc": utc_now().isoformat(),
        "sample_start": fit["start_date"].date().isoformat(),
        "sample_end": fit["end_date"].date().isoformat(),
        "observations": fit["observations"],
        "beta": fit["beta"],
        "intercept": fit["intercept"],
        "r2_loglog": fit["r2_loglog"],
        "current_price": position["current_price"],
        "central_price": position["central_price"],
        "p10_price": position["lower_price"],
        "p90_price": position["upper_price"],
        "residual_percentile": position["residual_percentile"],
        "deviation_from_central_pct": position["deviation_from_central_pct"],
        "zone": position["zone"],
        "beta_stability": stability["label"],
        "beta_range": stability.get("beta_range"),
        "global_weight": 0,
    }
    write_csv(POWER_METRICS_PATH, [metrics_row], list(metrics_row.keys()))
    write_csv(
        POWER_BACKTEST_PATH,
        detailed_backtest,
        ["cut_date", "target_date", "horizon_days", "cut_price", "predicted_price", "actual_price", "model_abs_error_pct", "naive_abs_error_pct", "model_beats_naive"],
    )
    cycle_output = []
    for row in cycle_rows:
        cycle_output.append({"generated_utc": utc_now().isoformat(), "current_cycle_phase_pct": cycle["cycle_phase_pct"], **row})
    write_csv(
        CYCLE_METRICS_PATH,
        cycle_output,
        ["generated_utc", "current_cycle_phase_pct", "cycle_start", "cycle_end", "analog_date", "analog_price", "return_30d_pct", "return_90d_pct", "return_180d_pct", "return_365d_pct"],
    )

    freeze_history(position, cycle, fit)
    tracker = update_live_tracker(frame)
    report = build_report(fit, position, stability, summary_backtest, cycle, cycle_rows, tracker, alt_summaries)
    atomic_write(REPORT_PATH, report)
    latest = read_text(LATEST_REPORT)
    atomic_write(LATEST_REPORT, replace_block(latest, report))
    print(f"BTC Macro Cycle report: {REPORT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
