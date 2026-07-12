# -*- coding: utf-8 -*-
"""RSI divergences on daily and weekly timeframes.

Diagnostic-only module:
- detects regular and hidden RSI divergences;
- distinguishes confirmed, forming and invalidated states;
- records confirmed independent divergence events;
- evaluates outcomes after 30/60/90/180 days;
- always keeps operational weight at zero.
"""

from __future__ import annotations

import hashlib
import math
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
import yfinance as yf


REPORTS_DIR = Path("reports")
REPORT_PATH = REPORTS_DIR / "rsi_multitimeframe_divergence_report.md"
METRICS_PATH = REPORTS_DIR / "rsi_multitimeframe_divergence_metrics.csv"
HISTORY_PATH = REPORTS_DIR / "rsi_multitimeframe_divergence_history.csv"
TRACKER_PATH = REPORTS_DIR / "rsi_multitimeframe_divergence_tracker_metrics.csv"
LATEST_REPORT = REPORTS_DIR / "latest_report.md"

START_MARKER = "<!-- RSI_MULTI_TIMEFRAME_DIVERGENCE_START -->"
END_MARKER = "<!-- RSI_MULTI_TIMEFRAME_DIVERGENCE_END -->"
COMPACT_START = "<!-- COMPACT_SECTION_START:rsi_multitimeframe_divergence -->"
COMPACT_END = "<!-- COMPACT_SECTION_END:rsi_multitimeframe_divergence -->"

ASSETS = {
    "BTC": "BTC-USD",
    "SOL": "SOL-USD",
    "DOGE": "DOGE-USD",
}
HORIZONS = (30, 60, 90, 180)
DIVERGENCE_TYPES = {
    "BULLISH_RSI_DIVERGENCE",
    "BEARISH_RSI_DIVERGENCE",
    "HIDDEN_BULLISH_RSI_DIVERGENCE",
    "HIDDEN_BEARISH_RSI_DIVERGENCE",
}

TIMEFRAME_SETTINGS = {
    "1D": {
        "pivot_window": 4,
        "signal_max_age_bars": 60,
        "forming_recent_bars": 4,
        "context_lookback": 14,
        "context_price_threshold_pct": 3.0,
        "price_noise_pct": 0.25,
    },
    "1W": {
        "pivot_window": 2,
        "signal_max_age_bars": 20,
        "forming_recent_bars": 2,
        "context_lookback": 6,
        "context_price_threshold_pct": 5.0,
        "price_noise_pct": 0.50,
    },
}

ITALIAN_LABELS = {
    "BULLISH_RSI_DIVERGENCE": "Bullish regolare",
    "BEARISH_RSI_DIVERGENCE": "Bearish regolare",
    "HIDDEN_BULLISH_RSI_DIVERGENCE": "Hidden bullish",
    "HIDDEN_BEARISH_RSI_DIVERGENCE": "Hidden bearish",
    "BULLISH_CONFIRMATION": "Conferma rialzista",
    "BEARISH_CONFIRMATION": "Conferma ribassista",
    "MOMENTUM_IMPROVING_NO_CONFIRMED_DIVERGENCE": "Momentum in miglioramento, divergenza non confermata",
    "MOMENTUM_WEAKENING_NO_CONFIRMED_DIVERGENCE": "Momentum in indebolimento, divergenza non confermata",
    "MIXED_NO_DIVERGENCE": "Misto / nessuna divergenza",
    "NONE": "Nessuna",
}


def safe_float(value: Any) -> float:
    try:
        number = float(value)
        if math.isnan(number):
            return np.nan
        return number
    except Exception:
        return np.nan


def fmt_num(value: Any, digits: int = 2) -> str:
    number = safe_float(value)
    if pd.isna(number):
        return "n/a"
    return f"{number:.{digits}f}".replace(".", ",")


def fmt_pct(value: Any, digits: int = 2, signed: bool = True) -> str:
    number = safe_float(value)
    if pd.isna(number):
        return "n/a"
    sign = "+" if signed and number > 0 else ""
    return f"{sign}{number:.{digits}f}%".replace(".", ",")


def fmt_price(asset: str, value: Any) -> str:
    number = safe_float(value)
    if pd.isna(number):
        return "n/a"
    if asset == "DOGE":
        return f"{number:.5f} $"
    if number >= 1000:
        return f"{number:,.0f} $".replace(",", ".")
    return f"{number:.2f} $".replace(".", ",")


def label(signal_type: str) -> str:
    return ITALIAN_LABELS.get(str(signal_type), str(signal_type).replace("_", " ").title())


def normalize_ohlcv(raw: pd.DataFrame) -> pd.DataFrame:
    if raw is None or raw.empty:
        return pd.DataFrame()

    out = raw.copy()
    if isinstance(out.columns, pd.MultiIndex):
        if len(out.columns.levels) >= 2:
            first = list(out.columns.get_level_values(0))
            if any(name in first for name in ["Open", "High", "Low", "Close", "Volume"]):
                out.columns = out.columns.get_level_values(0)
            else:
                out.columns = out.columns.get_level_values(-1)

    needed = ["Open", "High", "Low", "Close", "Volume"]
    for column in needed:
        if column not in out.columns:
            if column == "Volume":
                out[column] = 0.0
            elif "Close" in out.columns:
                out[column] = out["Close"]
            else:
                return pd.DataFrame()

    out = out[needed].copy()
    out.index = pd.to_datetime(out.index, utc=True, errors="coerce")
    out = out[~out.index.isna()]
    out.index = out.index.tz_convert(None).normalize()
    out = out[~out.index.duplicated(keep="last")].sort_index()
    out = out.apply(pd.to_numeric, errors="coerce")
    out = out.dropna(subset=["Close", "High", "Low"])
    return out


def download_daily(ticker: str) -> pd.DataFrame:
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
    except Exception as exc:
        print(f"Download RSI multi-timeframe fallito per {ticker}: {exc}")
        return pd.DataFrame()


def resample_weekly(daily: pd.DataFrame) -> pd.DataFrame:
    if daily.empty:
        return pd.DataFrame()
    weekly = daily.resample("W-SUN").agg(
        {
            "Open": "first",
            "High": "max",
            "Low": "min",
            "Close": "last",
            "Volume": "sum",
        }
    )
    return weekly.dropna(subset=["Close", "High", "Low"])


def rsi(series: pd.Series, period: int = 14) -> pd.Series:
    delta = series.diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    avg_gain = gain.ewm(
        alpha=1 / period,
        min_periods=period,
        adjust=False,
    ).mean()
    avg_loss = loss.ewm(
        alpha=1 / period,
        min_periods=period,
        adjust=False,
    ).mean()
    rs = avg_gain / avg_loss.replace(0, np.nan)
    result = 100 - (100 / (1 + rs))
    return result.fillna(50.0)


def add_indicators(frame: pd.DataFrame) -> pd.DataFrame:
    out = frame.copy()
    out["rsi14"] = rsi(out["Close"], 14)
    return out


def confirmed_pivots(
    frame: pd.DataFrame,
    kind: str,
    window: int,
) -> pd.DataFrame:
    price_column = "Low" if kind == "LOW" else "High"
    prices = frame[price_column]
    width = window * 2 + 1
    if kind == "LOW":
        rolling = prices.rolling(width, center=True).min()
        mask = (
            prices.eq(rolling)
            & prices.shift(1).gt(prices)
            & prices.shift(-1).gt(prices)
        )
    else:
        rolling = prices.rolling(width, center=True).max()
        mask = (
            prices.eq(rolling)
            & prices.shift(1).lt(prices)
            & prices.shift(-1).lt(prices)
        )

    pivots = frame.loc[mask.fillna(False), [price_column, "rsi14"]].copy()
    pivots = pivots.rename(columns={price_column: "pivot_price"})
    pivots["pivot_kind"] = kind
    return pivots


def classify_pivot_pair(
    kind: str,
    price_1: float,
    price_2: float,
    rsi_1: float,
    rsi_2: float,
    price_noise_pct: float = 0.25,
    rsi_threshold: float = 2.0,
) -> str | None:
    """Classify two confirmed price pivots and their RSI values."""
    values = [price_1, price_2, rsi_1, rsi_2]
    if any(pd.isna(safe_float(value)) for value in values):
        return None
    if price_1 <= 0:
        return None

    price_change_pct = (price_2 / price_1 - 1.0) * 100.0
    rsi_change = rsi_2 - rsi_1

    if kind == "LOW":
        if price_change_pct < -price_noise_pct and rsi_change >= rsi_threshold:
            return "BULLISH_RSI_DIVERGENCE"
        if price_change_pct > price_noise_pct and rsi_change <= -rsi_threshold:
            return "HIDDEN_BULLISH_RSI_DIVERGENCE"
    else:
        if price_change_pct > price_noise_pct and rsi_change <= -rsi_threshold:
            return "BEARISH_RSI_DIVERGENCE"
        if price_change_pct < -price_noise_pct and rsi_change >= rsi_threshold:
            return "HIDDEN_BEARISH_RSI_DIVERGENCE"

    return None


def classify_context(
    price_change_pct: float,
    rsi_change: float,
    price_threshold_pct: float,
) -> str:
    if price_change_pct <= -price_threshold_pct and rsi_change <= -2.0:
        return "BEARISH_CONFIRMATION"
    if price_change_pct >= price_threshold_pct and rsi_change >= 2.0:
        return "BULLISH_CONFIRMATION"
    if price_change_pct < 0 and rsi_change > 2.0:
        return "MOMENTUM_IMPROVING_NO_CONFIRMED_DIVERGENCE"
    if price_change_pct > 0 and rsi_change < -2.0:
        return "MOMENTUM_WEAKENING_NO_CONFIRMED_DIVERGENCE"
    return "MIXED_NO_DIVERGENCE"


def _direction(signal_type: str) -> str:
    if "BULLISH" in signal_type:
        return "BULLISH"
    if "BEARISH" in signal_type:
        return "BEARISH"
    return "NEUTRAL"


def _pivot_payload(
    first_date: pd.Timestamp,
    first_row: pd.Series,
    second_date: pd.Timestamp,
    second_row: pd.Series,
    kind: str,
) -> dict[str, Any]:
    return {
        "pivot_kind": kind,
        "pivot_1_date": pd.Timestamp(first_date).strftime("%Y-%m-%d"),
        "pivot_2_date": pd.Timestamp(second_date).strftime("%Y-%m-%d"),
        "pivot_1_price": safe_float(first_row["pivot_price"]),
        "pivot_2_price": safe_float(second_row["pivot_price"]),
        "pivot_1_rsi": safe_float(first_row["rsi14"]),
        "pivot_2_rsi": safe_float(second_row["rsi14"]),
    }


def detect_timeframe(
    asset: str,
    timeframe: str,
    frame: pd.DataFrame,
    previous_row: dict[str, Any] | None = None,
) -> dict[str, Any]:
    settings = TIMEFRAME_SETTINGS[timeframe]
    base = {
        "asset": asset,
        "timeframe": timeframe,
        "signal_type": "NONE",
        "summary_label": label("NONE"),
        "lifecycle_state": "NESSUNA",
        "direction": "NEUTRAL",
        "weight_global": 0,
        "weight_paper_trading": 0,
        "price": np.nan,
        "rsi14": np.nan,
        "price_change_context_pct": np.nan,
        "rsi_change_context": np.nan,
        "pivot_kind": "",
        "pivot_1_date": "",
        "pivot_2_date": "",
        "pivot_1_price": np.nan,
        "pivot_2_price": np.nan,
        "pivot_1_rsi": np.nan,
        "pivot_2_rsi": np.nan,
        "previous_signal_type": "",
        "interpretation": "Dati insufficienti.",
    }
    if frame is None or len(frame) < 40:
        return base

    data = add_indicators(frame)
    latest = data.iloc[-1]
    base["price"] = safe_float(latest["Close"])
    base["rsi14"] = safe_float(latest["rsi14"])

    lows = confirmed_pivots(
        data,
        "LOW",
        int(settings["pivot_window"]),
    )
    highs = confirmed_pivots(
        data,
        "HIGH",
        int(settings["pivot_window"]),
    )

    candidates: list[dict[str, Any]] = []
    for kind, pivots in [("LOW", lows), ("HIGH", highs)]:
        if len(pivots) < 2:
            continue
        first_date = pivots.index[-2]
        second_date = pivots.index[-1]
        first_row = pivots.iloc[-2]
        second_row = pivots.iloc[-1]
        age_bars = max(
            0,
            len(data) - 1 - data.index.get_loc(second_date),
        )
        if age_bars > int(settings["signal_max_age_bars"]):
            continue
        signal_type = classify_pivot_pair(
            kind,
            safe_float(first_row["pivot_price"]),
            safe_float(second_row["pivot_price"]),
            safe_float(first_row["rsi14"]),
            safe_float(second_row["rsi14"]),
            float(settings["price_noise_pct"]),
        )
        if signal_type:
            candidates.append(
                {
                    "signal_type": signal_type,
                    "lifecycle_state": "CONFERMATA",
                    "event_date": pd.Timestamp(second_date),
                    **_pivot_payload(
                        first_date,
                        first_row,
                        second_date,
                        second_row,
                        kind,
                    ),
                }
            )

    forming: list[dict[str, Any]] = []
    recent_count = int(settings["forming_recent_bars"])
    recent = data.tail(max(recent_count, 1))
    for kind, pivots, price_column in [
        ("LOW", lows, "Low"),
        ("HIGH", highs, "High"),
    ]:
        if pivots.empty:
            continue
        prior_date = pivots.index[-1]
        prior = pivots.iloc[-1]
        if kind == "LOW":
            current_date = recent[price_column].idxmin()
        else:
            current_date = recent[price_column].idxmax()
        current_price = safe_float(data.loc[current_date, price_column])
        current_rsi = safe_float(data.loc[current_date, "rsi14"])
        signal_type = classify_pivot_pair(
            kind,
            safe_float(prior["pivot_price"]),
            current_price,
            safe_float(prior["rsi14"]),
            current_rsi,
            float(settings["price_noise_pct"]),
        )
        if signal_type:
            current_row = pd.Series(
                {
                    "pivot_price": current_price,
                    "rsi14": current_rsi,
                }
            )
            forming.append(
                {
                    "signal_type": signal_type,
                    "lifecycle_state": "IN_FORMAZIONE",
                    "event_date": pd.Timestamp(current_date),
                    **_pivot_payload(
                        prior_date,
                        prior,
                        current_date,
                        current_row,
                        kind,
                    ),
                }
            )

    active_signals = candidates + forming
    if active_signals:
        chosen = max(
            active_signals,
            key=lambda row: (
                row["event_date"],
                1 if row["lifecycle_state"] == "CONFERMATA" else 0,
                1 if row["signal_type"] in {
                    "BULLISH_RSI_DIVERGENCE",
                    "BEARISH_RSI_DIVERGENCE",
                } else 0,
            ),
        )
        signal_type = str(chosen["signal_type"])
        lifecycle = str(chosen["lifecycle_state"])
        base.update(chosen)
        base["event_date"] = pd.Timestamp(chosen["event_date"]).strftime("%Y-%m-%d")
        base["summary_label"] = label(signal_type)
        base["direction"] = _direction(signal_type)
        if lifecycle == "CONFERMATA":
            base["interpretation"] = (
                f"{label(signal_type)} confermata sui due pivot del prezzo e dell'RSI. "
                "Contesto diagnostico: nessun punto operativo viene aggiunto."
            )
        else:
            base["interpretation"] = (
                f"{label(signal_type)} in formazione: il secondo estremo non è ancora "
                "un pivot confermato. Peso operativo sempre 0."
            )
        return base

    lookback = int(settings["context_lookback"])
    if len(data) > lookback:
        old = data.iloc[-lookback - 1]
        price_change = (
            safe_float(latest["Close"]) / safe_float(old["Close"]) - 1.0
        ) * 100.0
        rsi_change = safe_float(latest["rsi14"]) - safe_float(old["rsi14"])
        context_type = classify_context(
            price_change,
            rsi_change,
            float(settings["context_price_threshold_pct"]),
        )
        base["signal_type"] = context_type
        base["summary_label"] = label(context_type)
        base["lifecycle_state"] = "CONTESTO"
        base["direction"] = _direction(context_type)
        base["price_change_context_pct"] = price_change
        base["rsi_change_context"] = rsi_change
        if context_type == "BEARISH_CONFIRMATION":
            base["interpretation"] = (
                "Prezzo e RSI stanno scendendo insieme: momentum ribassista "
                "confermato, nessuna bullish divergence attiva."
            )
        elif context_type == "BULLISH_CONFIRMATION":
            base["interpretation"] = (
                "Prezzo e RSI stanno salendo insieme: momentum rialzista confermato."
            )
        else:
            base["interpretation"] = (
                f"{label(context_type)}. Non esiste una divergenza confermata "
                "sugli ultimi pivot."
            )

    previous_signal = str((previous_row or {}).get("signal_type", ""))
    previous_state = str((previous_row or {}).get("lifecycle_state", ""))
    if (
        previous_signal in DIVERGENCE_TYPES
        and previous_state in {"CONFERMATA", "IN_FORMAZIONE"}
        and base["signal_type"] not in DIVERGENCE_TYPES
    ):
        base["previous_signal_type"] = previous_signal
        base["lifecycle_state"] = "INVALIDATA"
        base["summary_label"] = f"{label(previous_signal)} invalidata"
        base["direction"] = "NEUTRAL"
        base["interpretation"] = (
            f"La precedente {label(previous_signal).lower()} non è più sostenuta "
            "dalla relazione corrente tra pivot di prezzo e RSI."
        )

    return base


def _read_previous_metrics() -> dict[tuple[str, str], dict[str, Any]]:
    if not METRICS_PATH.exists():
        return {}
    try:
        frame = pd.read_csv(METRICS_PATH)
    except Exception:
        return {}
    output: dict[tuple[str, str], dict[str, Any]] = {}
    for _, row in frame.iterrows():
        output[(str(row.get("asset")), str(row.get("timeframe")))] = row.to_dict()
    return output


def _event_id(row: dict[str, Any]) -> str:
    raw = "|".join(
        [
            str(row.get("asset", "")),
            str(row.get("timeframe", "")),
            str(row.get("signal_type", "")),
            str(row.get("pivot_1_date", "")),
            str(row.get("pivot_2_date", "")),
        ]
    )
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()[:20]


def _history_columns() -> list[str]:
    columns = [
        "signal_id",
        "snapshot_date",
        "asset",
        "ticker",
        "timeframe",
        "signal_type",
        "direction",
        "entry_price",
        "entry_rsi",
        "pivot_kind",
        "pivot_1_date",
        "pivot_2_date",
        "pivot_1_price",
        "pivot_2_price",
        "pivot_1_rsi",
        "pivot_2_rsi",
        "weight_global",
        "weight_paper_trading",
    ]
    for horizon in HORIZONS:
        columns.extend(
            [
                f"checked_{horizon}d",
                f"exit_date_{horizon}d",
                f"return_{horizon}d_pct",
                f"corrected_return_{horizon}d_pct",
                f"direction_correct_{horizon}d",
                f"max_gain_{horizon}d_pct",
                f"drawdown_{horizon}d_pct",
            ]
        )
    return columns


def _load_history() -> pd.DataFrame:
    columns = _history_columns()
    if not HISTORY_PATH.exists():
        return pd.DataFrame(columns=columns)
    try:
        history = pd.read_csv(HISTORY_PATH)
    except Exception:
        return pd.DataFrame(columns=columns)
    for column in columns:
        if column not in history.columns:
            history[column] = np.nan
    return history[columns]


def _bool_value(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    return str(value).strip().lower() in {"true", "1", "yes"}


def update_history(
    metrics_rows: list[dict[str, Any]],
    daily_data: dict[str, pd.DataFrame],
) -> pd.DataFrame:
    history = _load_history()
    today = pd.Timestamp(datetime.now(timezone.utc).date())
    existing_ids = set(history["signal_id"].astype(str)) if not history.empty else set()

    new_rows: list[dict[str, Any]] = []
    for row in metrics_rows:
        if (
            row.get("signal_type") not in DIVERGENCE_TYPES
            or row.get("lifecycle_state") != "CONFERMATA"
        ):
            continue
        signal_id = _event_id(row)
        if signal_id in existing_ids:
            continue
        record: dict[str, Any] = {
            "signal_id": signal_id,
            "snapshot_date": today.strftime("%Y-%m-%d"),
            "asset": row["asset"],
            "ticker": ASSETS[row["asset"]],
            "timeframe": row["timeframe"],
            "signal_type": row["signal_type"],
            "direction": row["direction"],
            "entry_price": row["price"],
            "entry_rsi": row["rsi14"],
            "pivot_kind": row["pivot_kind"],
            "pivot_1_date": row["pivot_1_date"],
            "pivot_2_date": row["pivot_2_date"],
            "pivot_1_price": row["pivot_1_price"],
            "pivot_2_price": row["pivot_2_price"],
            "pivot_1_rsi": row["pivot_1_rsi"],
            "pivot_2_rsi": row["pivot_2_rsi"],
            "weight_global": 0,
            "weight_paper_trading": 0,
        }
        for horizon in HORIZONS:
            record[f"checked_{horizon}d"] = False
        new_rows.append(record)
        existing_ids.add(signal_id)

    if new_rows:
        history = pd.concat(
            [history, pd.DataFrame(new_rows)],
            ignore_index=True,
            sort=False,
        )

    if history.empty:
        history.to_csv(HISTORY_PATH, index=False)
        return history

    for index, row in history.iterrows():
        asset = str(row.get("asset", ""))
        prices = daily_data.get(asset, pd.DataFrame())
        if prices.empty:
            continue
        snapshot_date = pd.Timestamp(row.get("snapshot_date"))
        entry_price = safe_float(row.get("entry_price"))
        direction = str(row.get("direction", "NEUTRAL"))
        if pd.isna(entry_price) or entry_price <= 0:
            continue

        for horizon in HORIZONS:
            checked_col = f"checked_{horizon}d"
            if _bool_value(row.get(checked_col)):
                continue
            target_date = snapshot_date + pd.Timedelta(days=horizon)
            if today < target_date:
                continue
            future = prices[prices.index >= target_date]
            if future.empty:
                continue
            exit_date = pd.Timestamp(future.index[0])
            exit_price = safe_float(future.iloc[0]["Close"])
            if pd.isna(exit_price):
                continue
            path = prices[
                (prices.index > snapshot_date)
                & (prices.index <= exit_date)
            ]
            raw_return = (exit_price / entry_price - 1.0) * 100.0
            sign = 1.0 if direction == "BULLISH" else -1.0
            corrected = raw_return * sign
            correct = raw_return > 0 if direction == "BULLISH" else raw_return < 0
            max_gain = (
                (safe_float(path["High"].max()) / entry_price - 1.0) * 100.0
                if not path.empty
                else np.nan
            )
            drawdown = (
                (safe_float(path["Low"].min()) / entry_price - 1.0) * 100.0
                if not path.empty
                else np.nan
            )
            history.at[index, checked_col] = True
            history.at[index, f"exit_date_{horizon}d"] = exit_date.strftime("%Y-%m-%d")
            history.at[index, f"return_{horizon}d_pct"] = raw_return
            history.at[index, f"corrected_return_{horizon}d_pct"] = corrected
            history.at[index, f"direction_correct_{horizon}d"] = bool(correct)
            history.at[index, f"max_gain_{horizon}d_pct"] = max_gain
            history.at[index, f"drawdown_{horizon}d_pct"] = drawdown

    history = history[_history_columns()]
    history.to_csv(HISTORY_PATH, index=False)
    return history


def build_tracker(history: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, Any]] = []
    if history.empty:
        tracker = pd.DataFrame(
            columns=[
                "asset",
                "timeframe",
                "signal_type",
                "horizon_days",
                "controls",
                "accuracy_pct",
                "corrected_return_mean_pct",
                "raw_return_mean_pct",
                "status",
                "operational_weight",
            ]
        )
        tracker.to_csv(TRACKER_PATH, index=False)
        return tracker

    groups = history.groupby(["asset", "timeframe", "signal_type"], dropna=False)
    for (asset, timeframe, signal_type), group in groups:
        for horizon in HORIZONS:
            checked = group[
                group[f"checked_{horizon}d"].map(_bool_value)
            ].copy()
            controls = len(checked)
            accuracy = (
                checked[f"direction_correct_{horizon}d"]
                .map(_bool_value)
                .mean()
                * 100.0
                if controls
                else np.nan
            )
            corrected_mean = (
                pd.to_numeric(
                    checked[f"corrected_return_{horizon}d_pct"],
                    errors="coerce",
                ).mean()
                if controls
                else np.nan
            )
            raw_mean = (
                pd.to_numeric(
                    checked[f"return_{horizon}d_pct"],
                    errors="coerce",
                ).mean()
                if controls
                else np.nan
            )
            if controls >= 100:
                status = "CAMPIONE SERIO / ANCORA PESO 0"
            elif controls >= 60:
                status = "LETTURA UTILE / ANCORA PESO 0"
            elif controls >= 30:
                status = "PRIMA LETTURA / ANCORA PESO 0"
            else:
                status = "RACCOLTA DATI"
            rows.append(
                {
                    "asset": asset,
                    "timeframe": timeframe,
                    "signal_type": signal_type,
                    "horizon_days": horizon,
                    "controls": controls,
                    "accuracy_pct": accuracy,
                    "corrected_return_mean_pct": corrected_mean,
                    "raw_return_mean_pct": raw_mean,
                    "status": status,
                    "operational_weight": 0,
                }
            )

    tracker = pd.DataFrame(rows)
    tracker.to_csv(TRACKER_PATH, index=False)
    return tracker


def _detail_pair(row: pd.Series, asset: str) -> str:
    if not row.get("pivot_1_date") or not row.get("pivot_2_date"):
        return "n/a"
    return (
        f"{row.get('pivot_1_date')} {fmt_price(asset, row.get('pivot_1_price'))} "
        f"/ RSI {fmt_num(row.get('pivot_1_rsi'))} → "
        f"{row.get('pivot_2_date')} {fmt_price(asset, row.get('pivot_2_price'))} "
        f"/ RSI {fmt_num(row.get('pivot_2_rsi'))}"
    )


def render_report(
    metrics: pd.DataFrame,
    history: pd.DataFrame,
    tracker: pd.DataFrame,
) -> str:
    generated = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines = [
        "# Divergenze RSI multi-timeframe — diagnostica",
        "",
        f"Generato: {generated}",
        "",
        (
            "Il modulo confronta prezzo e RSI 14 sui pivot confermati **daily e weekly**. "
            "Riconosce divergenze regolari e nascoste, segnali in formazione, "
            "invalidazioni e semplice conferma del momentum."
        ),
        "",
        (
            "**Peso operativo: 0.** Non modifica il Global Confluence, non cambia "
            "le soglie del Paper Trading e non apre né blocca operazioni. "
            "I risultati vengono misurati prima di qualsiasi futura decisione sul peso."
        ),
        "",
        "## Sintesi corrente",
        "",
    ]

    summary_rows = []
    for asset in ASSETS:
        asset_rows = metrics[metrics["asset"] == asset]
        daily = asset_rows[asset_rows["timeframe"] == "1D"]
        weekly = asset_rows[asset_rows["timeframe"] == "1W"]
        daily_row = daily.iloc[0] if not daily.empty else pd.Series(dtype=object)
        weekly_row = weekly.iloc[0] if not weekly.empty else pd.Series(dtype=object)
        summary_rows.append(
            {
                "Asset": asset,
                "Daily": daily_row.get("summary_label", "n/a"),
                "Stato D": daily_row.get("lifecycle_state", "n/a"),
                "Weekly": weekly_row.get("summary_label", "n/a"),
                "Stato W": weekly_row.get("lifecycle_state", "n/a"),
                "Lettura weekly": weekly_row.get("interpretation", "n/a"),
                "Peso": "0",
            }
        )
    lines.append(pd.DataFrame(summary_rows).to_markdown(index=False))
    lines.append("")

    lines.extend(["## Dettaglio dei pivot", ""])
    detail_rows = []
    for _, row in metrics.iterrows():
        asset = str(row["asset"])
        detail_rows.append(
            {
                "Asset": asset,
                "TF": row["timeframe"],
                "Tipo": row["summary_label"],
                "Stato": row["lifecycle_state"],
                "Prezzo / RSI": f"{fmt_price(asset, row['price'])} / {fmt_num(row['rsi14'])}",
                "Pivot confrontati": _detail_pair(row, asset),
                "Δ prezzo contesto": fmt_pct(row.get("price_change_context_pct")),
                "Δ RSI contesto": fmt_num(row.get("rsi_change_context")),
                "Peso": "0",
            }
        )
    lines.append(pd.DataFrame(detail_rows).to_markdown(index=False))
    lines.append("")

    for asset in ASSETS:
        lines.extend([f"### {asset}", ""])
        for timeframe in ["1D", "1W"]:
            selected = metrics[
                (metrics["asset"] == asset)
                & (metrics["timeframe"] == timeframe)
            ]
            if selected.empty:
                continue
            row = selected.iloc[0]
            lines.append(
                f"- **{timeframe} — {row['summary_label']} / "
                f"{row['lifecycle_state']}**: {row['interpretation']}"
            )
        lines.append("")

    lines.extend(
        [
            "## Tracker live delle divergenze confermate",
            "",
            (
                "Viene salvato un solo evento per combinazione di asset, timeframe, "
                "tipo e coppia di pivot. Gli esiti vengono controllati dopo "
                "30, 60, 90 e 180 giorni."
            ),
            "",
            f"- Eventi indipendenti salvati: **{len(history)}**.",
            "- Soglie di lettura: **30 / 60 / 100 controlli**.",
            "- Anche oltre le soglie il peso resta **0** finché non viene presa una decisione esplicita.",
            "",
        ]
    )

    matured = tracker[tracker["controls"] > 0] if not tracker.empty else tracker
    if matured is not None and not matured.empty:
        display = matured.copy()
        display["Tipo"] = display["signal_type"].map(label)
        display["Accuratezza"] = display["accuracy_pct"].map(fmt_pct)
        display["Return corretto"] = display["corrected_return_mean_pct"].map(fmt_pct)
        display = display[
            [
                "asset",
                "timeframe",
                "Tipo",
                "horizon_days",
                "controls",
                "Accuratezza",
                "Return corretto",
                "status",
                "operational_weight",
            ]
        ].rename(
            columns={
                "asset": "Asset",
                "timeframe": "TF",
                "horizon_days": "Orizzonte",
                "controls": "Controlli",
                "status": "Stato",
                "operational_weight": "Peso",
            }
        )
        lines.append(display.to_markdown(index=False))
    else:
        lines.append("_Nessun controllo maturato: il tracker ha appena iniziato a raccogliere dati._")
    lines.append("")

    lines.extend(
        [
            "## Regole di prudenza",
            "",
            "- Una divergenza **in formazione** può scomparire prima che il pivot sia confermato.",
            "- Una divergenza weekly può anticipare il prezzo di diverse settimane.",
            "- Prezzo in calo e RSI in calo non è bullish divergence: è conferma ribassista.",
            "- Le divergenze restano dentro la famiglia tecnica e non vengono sommate come prova indipendente.",
            "- Nessuna statistica di questo modulo autorizza automaticamente il trading reale.",
            "",
        ]
    )
    return "\n".join(lines)


def inject_into_latest_report(report_body: str) -> None:
    if not LATEST_REPORT.exists():
        return
    try:
        old = LATEST_REPORT.read_text(encoding="utf-8")
    except Exception:
        return

    compact = "\n".join(
        [
            COMPACT_START,
            "<details>",
            "<summary><strong>📉 Divergenze RSI daily / weekly — peso 0</strong></summary>",
            "",
            START_MARKER,
            report_body.strip(),
            END_MARKER,
            "",
            "</details>",
            COMPACT_END,
        ]
    )

    if COMPACT_START in old and COMPACT_END in old:
        start = old.find(COMPACT_START)
        end = old.find(COMPACT_END, start)
        if end != -1:
            end += len(COMPACT_END)
            new = old[:start] + compact + old[end:]
        else:
            new = old.rstrip() + "\n\n" + compact + "\n"
    else:
        insertion_candidates = [
            "<!-- COMPACT_SECTION_START:technical_structure -->",
            "<!-- TECHNICAL_STRUCTURE_START -->",
        ]
        insertion = -1
        for marker in insertion_candidates:
            insertion = old.find(marker)
            if insertion != -1:
                break
        if insertion == -1:
            new = old.rstrip() + "\n\n" + compact + "\n"
        else:
            new = old[:insertion] + compact + "\n\n" + old[insertion:]

    LATEST_REPORT.write_text(new, encoding="utf-8", newline="\n")


def main() -> None:
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    previous = _read_previous_metrics()
    daily_data: dict[str, pd.DataFrame] = {}
    rows: list[dict[str, Any]] = []

    for asset, ticker in ASSETS.items():
        print(f"RSI multi-timeframe: scarico {ticker}...")
        daily = download_daily(ticker)
        daily_data[asset] = daily
        weekly = resample_weekly(daily)
        for timeframe, frame in [("1D", daily), ("1W", weekly)]:
            row = detect_timeframe(
                asset,
                timeframe,
                frame,
                previous.get((asset, timeframe)),
            )
            rows.append(row)

    metrics = pd.DataFrame(rows)
    if metrics.empty:
        metrics = pd.DataFrame(
            columns=[
                "asset",
                "timeframe",
                "signal_type",
                "summary_label",
                "lifecycle_state",
                "direction",
                "weight_global",
                "weight_paper_trading",
            ]
        )
    metrics.to_csv(METRICS_PATH, index=False)

    history = update_history(rows, daily_data)
    tracker = build_tracker(history)
    report = render_report(metrics, history, tracker)
    REPORT_PATH.write_text(report, encoding="utf-8", newline="\n")
    inject_into_latest_report(report)

    print(f"Creato {REPORT_PATH}")
    print(f"Creato {METRICS_PATH}")
    print(f"Creato {HISTORY_PATH}")
    print(f"Creato {TRACKER_PATH}")
    for _, row in metrics.iterrows():
        print(
            f"{row['asset']} {row['timeframe']}: "
            f"{row['summary_label']} / {row['lifecycle_state']} / peso 0"
        )


if __name__ == "__main__":
    main()

