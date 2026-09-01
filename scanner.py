# -*- coding: utf-8 -*-
import json
import os
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd
import yfinance as yf
from scipy.spatial.distance import cosine

from market_snapshot import (
    get_snapshot_candle_date,
    get_snapshot_price,
    load_market_snapshot,
    write_snapshot_from_asset_data,
)
from forecast_provenance import (
    append_evaluation,
    append_forecast,
    code_version,
    find_evaluation,
    freeze_cohort,
    freeze_ohlc,
    load_frozen_ohlc,
    new_run_id,
)


WINDOW = 100
FORWARD_DAYS = [7, 14, 30, 60]
STEP = 5
TOP_N = 200
CLEAN_TOP_N = 40
MIN_GAP_DAYS = 90

TARGETS = ["BTC-USD", "SOL-USD", "DOGE-USD"]

CRYPTO_TICKERS = [
    "BTC-USD", "ETH-USD", "SOL-USD", "BNB-USD", "XRP-USD",
    "ADA-USD", "AVAX-USD", "DOGE-USD", "LINK-USD", "DOT-USD",
    "LTC-USD", "NEAR-USD", "UNI-USD", "ATOM-USD", "ETC-USD",
    "FIL-USD", "APT-USD", "ARB-USD", "OP-USD", "SUI-USD",
    "ICP-USD", "INJ-USD", "AAVE-USD", "MATIC-USD", "TRX-USD",
    "BCH-USD", "XLM-USD", "HBAR-USD", "VET-USD", "ALGO-USD",
    "EOS-USD", "XTZ-USD", "MANA-USD", "SAND-USD", "GRT-USD",
    "CHZ-USD", "EGLD-USD", "FTM-USD", "RUNE-USD", "THETA-USD",
    "KSM-USD", "ZEC-USD", "DASH-USD", "COMP-USD", "MKR-USD",
    "SNX-USD", "CRV-USD", "ENJ-USD", "BAT-USD", "ZIL-USD",
    "WAVES-USD", "KAVA-USD", "ONE-USD", "IOTA-USD", "NEO-USD",
    "QTUM-USD", "OMG-USD", "YFI-USD", "1INCH-USD", "LRC-USD"
]

PREDICTION_LOG_PATH = "reports/prediction_log.csv"
ACCURACY_REPORT_PATH = "reports/accuracy_report.csv"
CALIBRATION_REPORT_PATH = "reports/calibration_report.csv"
LATEST_SCANNER_MATCHES_PATH = "reports/latest_scanner_matches.csv"
LATEST_SCANNER_SUMMARY_CSV_PATH = "reports/latest_scanner_summary.csv"
LATEST_SCANNER_SUMMARY_JSON_PATH = "reports/latest_scanner_summary.json"

MIN_CALIBRATION_EVALS = 30
STRONG_CALIBRATION_EVALS = 60
CALIBRATION_WINDOW = 60


def add_indicators(df):
    df = df.copy()

    df["return"] = df["Close"].pct_change()

    df["ma20"] = df["Close"].rolling(20).mean()
    df["ma50"] = df["Close"].rolling(50).mean()
    df["ma200"] = df["Close"].rolling(200).mean()

    df["dist_ma20"] = (df["Close"] / df["ma20"]) - 1
    df["dist_ma50"] = (df["Close"] / df["ma50"]) - 1
    df["dist_ma200"] = (df["Close"] / df["ma200"]) - 1

    delta = df["Close"].diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.rolling(14).mean()
    avg_loss = loss.rolling(14).mean()

    rs = avg_gain / avg_loss
    df["rsi"] = 100 - (100 / (1 + rs))

    ema12 = df["Close"].ewm(span=12, adjust=False).mean()
    ema26 = df["Close"].ewm(span=26, adjust=False).mean()

    df["macd"] = ema12 - ema26
    df["macd_signal"] = df["macd"].ewm(span=9, adjust=False).mean()
    df["macd_hist"] = df["macd"] - df["macd_signal"]

    df["volatility"] = df["return"].rolling(20).std()
    df["volume_norm"] = df["Volume"] / df["Volume"].rolling(20).mean()

    rolling_max = df["Close"].rolling(100).max()
    df["drawdown"] = (df["Close"] / rolling_max) - 1

    return df.replace([np.inf, -np.inf], np.nan).dropna()


def zscore_array(x):
    x = np.array(x, dtype=float)
    mean = np.nanmean(x)
    std = np.nanstd(x)

    if std == 0 or np.isnan(std):
        std = 1

    return (x - mean) / std


def make_signature_v2(df, start_idx=None, window=WINDOW):
    if start_idx is None:
        w = df.tail(window).copy()
    else:
        w = df.iloc[start_idx:start_idx + window].copy()

    w = w.replace([np.inf, -np.inf], np.nan).dropna()

    if len(w) < window:
        return None

    price_shape = np.log(w["Close"] / w["Close"].iloc[0])

    features = np.column_stack([
        zscore_array(price_shape),
        zscore_array(w["rsi"]),
        zscore_array(w["dist_ma20"]),
        zscore_array(w["dist_ma50"]),
        zscore_array(w["drawdown"]),
    ])

    weights = np.array([3.0, 1.5, 1.0, 1.0, 1.0])
    return (features * weights).flatten()


def future_stats(df, end_idx):
    close_now = df["Close"].iloc[end_idx]
    results = {}

    for d in FORWARD_DAYS:
        if end_idx + d < len(df):
            future_close = df["Close"].iloc[end_idx + d]
            future_slice = df["Close"].iloc[end_idx:end_idx + d + 1]

            results[f"return_{d}d"] = (future_close / close_now - 1) * 100
            results[f"drawdown_{d}d"] = (future_slice.min() / close_now - 1) * 100
            results[f"max_gain_{d}d"] = (future_slice.max() / close_now - 1) * 100
        else:
            results[f"return_{d}d"] = np.nan
            results[f"drawdown_{d}d"] = np.nan
            results[f"max_gain_{d}d"] = np.nan

    return results


def download_data(*, run_id=None, downloaded_at_utc=None):
    print("Downloading data...")

    raw = yf.download(
        CRYPTO_TICKERS,
        period="10y",
        interval="1d",
        auto_adjust=True,
        progress=False,
        group_by="ticker",
        threads=True,
    )

    asset_data = {}
    raw_snapshot_ids = {}

    for ticker in CRYPTO_TICKERS:
        try:
            df = raw[ticker].dropna().copy()

            if run_id and downloaded_at_utc:
                raw_snapshot_ids[ticker] = freeze_ohlc(
                    df,
                    ticker=ticker,
                    source="Yahoo Finance/yfinance",
                    downloaded_at_utc=downloaded_at_utc,
                    requested_interval="1d",
                    requested_range="period=10y",
                    run_id=run_id,
                    purpose="forecast_generation_and_evaluation",
                )

            if len(df) > 300:
                processed = add_indicators(df)

                if len(processed) > 250:
                    asset_data[ticker] = processed
                    print(
                        f"{ticker}: OK "
                        f"{processed.index[0].date()} -> {processed.index[-1].date()}"
                    )

        except Exception as e:
            print(f"{ticker}: skipped ({e})")

    return asset_data, raw_snapshot_ids


def find_similar_patterns(target_ticker, data_with_indicators):
    target_sig = make_signature_v2(data_with_indicators[target_ticker])
    matches = []

    for ticker, df in data_with_indicators.items():
        max_start = len(df) - WINDOW - max(FORWARD_DAYS)

        for start_idx in range(0, max_start, STEP):
            end_idx = start_idx + WINDOW - 1

            if ticker == target_ticker and end_idx >= len(df) - max(FORWARD_DAYS) - 5:
                continue

            sig = make_signature_v2(df, start_idx=start_idx)

            if sig is None:
                continue

            similarity = 1 - cosine(target_sig, sig)

            if np.isnan(similarity):
                continue

            stats = future_stats(df, end_idx)

            matches.append({
                "target": target_ticker,
                "similar_asset": ticker,
                "start_date": df.index[start_idx].date(),
                "end_date": df.index[end_idx].date(),
                "similarity": similarity * 100,
                **stats
            })

    results = pd.DataFrame(matches)
    return results.sort_values("similarity", ascending=False).head(TOP_N)


def deoverlap_matches(matches):
    m = matches.copy()
    m["end_date_dt"] = pd.to_datetime(m["end_date"])
    m = m.sort_values("similarity", ascending=False)

    kept_rows = []
    kept_dates_by_asset = {}

    for _, row in m.iterrows():
        asset = row["similar_asset"]
        end_date = row["end_date_dt"]

        previous_dates = kept_dates_by_asset.get(asset, [])

        too_close = any(
            abs((end_date - prev_date).days) < MIN_GAP_DAYS
            for prev_date in previous_dates
        )

        if not too_close:
            kept_rows.append(row)
            kept_dates_by_asset.setdefault(asset, []).append(end_date)

        if len(kept_rows) >= CLEAN_TOP_N:
            break

    clean = pd.DataFrame(kept_rows)
    return clean.drop(columns=["end_date_dt"], errors="ignore")


def verdict(matches):
    ret30 = matches["return_30d"].mean()
    win30 = (matches["return_30d"] > 0).mean() * 100

    if win30 >= 60 and ret30 > 0:
        return "RIALZISTA"

    if win30 <= 40 and ret30 < 0:
        return "RIBASSISTA"

    return "NEUTRALE / INCERTO"


def direction_label(positive_cases):
    up = float(positive_cases)
    down = 100 - up

    if up >= 60:
        return "SALITA", up, down

    if down >= 60:
        return "DISCESA", up, down

    return "INCERTO", up, down


def signal_strength(positive_cases):
    up = float(positive_cases)
    down = 100 - up
    edge = abs(up - down)

    if edge >= 40:
        return "forte"

    if edge >= 25:
        return "medio"

    if edge >= 12:
        return "debole"

    return "molto debole / quasi pari"


def simple_direction_sentence(direction, strength):
    if direction == "SALITA":
        return (
            f"La lettura principale è rialzista, con segnale {strength}. "
            "Nei casi storici simili, il prezzo ha chiuso sopra dopo 30 giorni "
            "più spesso di quanto abbia chiuso sotto."
        )

    if direction == "DISCESA":
        return (
            f"La lettura principale è ribassista, con segnale {strength}. "
            "Nei casi storici simili, il prezzo ha chiuso sotto dopo 30 giorni "
            "più spesso di quanto abbia chiuso sopra."
        )

    return (
        f"La lettura principale è incerta, con segnale {strength}. "
        "Nei casi storici simili non c'è stato un vantaggio chiaro né per salita né per discesa."
    )


def summary_table(matches):
    return {
        "match_count": len(matches),
        "similarity_avg": matches["similarity"].mean(),
        "similarity_median": matches["similarity"].median(),
        "return_30d_avg": matches["return_30d"].mean(),
        "return_30d_median": matches["return_30d"].median(),
        "positive_cases_30d": (matches["return_30d"] > 0).mean() * 100,
        "drawdown_30d_avg": matches["drawdown_30d"].mean(),
        "max_gain_30d_avg": matches["max_gain_30d"].mean(),
    }


def price_scenarios(matches, current_price):
    avg_ret = matches["return_30d"].mean()
    med_ret = matches["return_30d"].median()
    avg_dd = matches["drawdown_30d"].mean()
    avg_gain = matches["max_gain_30d"].mean()

    return {
        "current_price": current_price,
        "scenario_avg_30d": current_price * (1 + avg_ret / 100),
        "scenario_median_30d": current_price * (1 + med_ret / 100),
        "drawdown_avg_30d": current_price * (1 + avg_dd / 100),
        "max_gain_avg_30d": current_price * (1 + avg_gain / 100),
    }


def percentile_report(matches, current_price):
    rows = []

    for metric in ["return_30d", "drawdown_30d", "max_gain_30d"]:
        values = matches[metric].dropna()

        for q in [10, 25, 50, 75, 90]:
            pct = np.percentile(values, q)
            price = current_price * (1 + pct / 100)

            rows.append({
                "metric": metric,
                "percentile": q,
                "percent_value": pct,
                "price_level": price,
            })

    return pd.DataFrame(rows)


def fmt_number_it(value):
    try:
        s = f"{float(value):,.2f}"
        return s.replace(",", "X").replace(".", ",").replace("X", ".")
    except Exception:
        return str(value)


def fmt_price(value):
    return f"{fmt_number_it(value)} $"


def fmt_pct(value):
    return f"{fmt_number_it(value)}%"


def pct_to_price(current_price, pct_value):
    if pd.isna(pct_value):
        return np.nan

    return current_price * (1 + pct_value / 100)


def semaforo(verdict_value):
    if verdict_value == "RIALZISTA":
        return "🟢 VERDE / Favorevole"
    if verdict_value == "RIBASSISTA":
        return "🔴 ROSSO / Prudenza"
    return "🟡 GIALLO / Incerto"


def asset_name(target):
    if target == "BTC-USD":
        return "Bitcoin"
    if target == "SOL-USD":
        return "Solana"
    if target == "DOGE-USD":
        return "Dogecoin"
    return target


def simple_verdict_text(target, verdict_value):
    name = asset_name(target)

    if verdict_value == "RIALZISTA":
        return (
            f"{name} ha un segnale favorevole. "
            "La statistica dei casi simili indica più possibilità di salita che di discesa, "
            "ma resta comunque una probabilità, non una certezza."
        )

    if verdict_value == "RIBASSISTA":
        return (
            f"{name} richiede prudenza. "
            "La statistica dei casi simili indica più possibilità di discesa che di salita. "
            "Con leva, il rischio principale è il drawdown durante il percorso."
        )

    return (
        f"{name} è in una situazione incerta. "
        "Lo scanner non vede un vantaggio chiaro né per la salita né per la discesa. "
        "In questi casi è meglio non forzare la previsione."
    )


def get_percentile_price(percentiles, metric, q):
    row = percentiles[
        (percentiles["metric"] == metric) &
        (percentiles["percentile"] == q)
    ]

    if len(row) == 0:
        return None, None

    percent_value = float(row["percent_value"].iloc[0])
    price_level = float(row["price_level"].iloc[0])

    return percent_value, price_level


def percentile_explanation(metric, q):
    if metric == "return_30d":
        explanations = {
            10: "Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.",
            25: "Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.",
            50: "Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.",
            75: "Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.",
            90: "Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.",
        }
        return explanations[q]

    if metric == "drawdown_30d":
        explanations = {
            10: "Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.",
            25: "Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.",
            50: "Percentile 50: discesa normale durante il mese. È il drawdown centrale.",
            75: "Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.",
            90: "Percentile 90: discesa molto contenuta. Scenario molto tranquillo.",
        }
        return explanations[q]

    if metric == "max_gain_30d":
        explanations = {
            10: "Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.",
            25: "Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.",
            50: "Percentile 50: rialzo normale. È lo spike centrale più realistico.",
            75: "Percentile 75: rialzo buono. Zona interessante per possibile take profit.",
            90: "Percentile 90: rialzo molto forte. Possibile, ma meno comune.",
        }
        return explanations[q]

    return ""


def percentile_lines(percentiles, metric):
    labels = {
        10: "10%",
        25: "25%",
        50: "50%",
        75: "75%",
        90: "90%",
    }

    lines = []

    for q in [10, 25, 50, 75, 90]:
        percent_value, price_level = get_percentile_price(percentiles, metric, q)

        if percent_value is None:
            continue

        lines.append(
            f"- **Percentile {labels[q]}**: {fmt_pct(percent_value)} → **{fmt_price(price_level)}**"
        )
        lines.append(f"  - {percentile_explanation(metric, q)}")

    return lines


def load_prediction_log():
    if os.path.exists(PREDICTION_LOG_PATH):
        return pd.read_csv(PREDICTION_LOG_PATH, encoding="utf-8")

    return pd.DataFrame()


def percentile_value(percentiles, metric, q, column):
    row = percentiles[
        (percentiles["metric"] == metric) &
        (percentiles["percentile"] == q)
    ]

    if len(row) == 0:
        return np.nan

    return float(row[column].iloc[0])


def update_prediction_log(log, all_results, generated_at, run_id=None, raw_snapshot_ids=None):
    prediction_date = generated_at[:10]

    for target, result in all_results.items():
        summary = result["summary"]
        prices = result["prices"]
        percentiles = result["percentiles"]

        row = {
            "prediction_date": prediction_date,
            "forecast_date": prediction_date,
            "generated_at_utc": generated_at,
            "asset": target,
            "verdict": result["verdict"],
            "current_price": prices["current_price"],
            "scenario_avg_30d": prices["scenario_avg_30d"],
            "scenario_median_30d": prices["scenario_median_30d"],
            "drawdown_avg_30d": prices["drawdown_avg_30d"],
            "max_gain_avg_30d": prices["max_gain_avg_30d"],
            "similarity_avg": summary["similarity_avg"],
            "positive_cases_30d": summary["positive_cases_30d"],
            "return_30d_avg": summary["return_30d_avg"],
            "return_30d_median": summary["return_30d_median"],
            "drawdown_30d_avg": summary["drawdown_30d_avg"],
            "max_gain_30d_avg": summary["max_gain_30d_avg"],
            "evaluated": False,
            "evaluation_date": "",
            "actual_30d_price": np.nan,
            "actual_30d_return_pct": np.nan,
            "actual_min_price_30d": np.nan,
            "actual_drawdown_pct": np.nan,
            "actual_max_price_30d": np.nan,
            "actual_max_gain_pct": np.nan,
            "directional_correct": np.nan,
            "central_error_pct": np.nan,
            "risk_zone_touched": np.nan,
            "upside_zone_touched": np.nan,
            "return_within_p10_p90": np.nan,
            "drawdown_within_p10_p90": np.nan,
            "max_gain_within_p10_p90": np.nan,
        }

        if run_id:
            forecast_id = f"{run_id}:{target}"
            row.update({
                "forecast_id": forecast_id,
                "run_id": run_id,
                "official_daily": True,
                "official_daily_version": generated_at,
                "cohort_id": result.get("cohort_id"),
                "cohort_manifest_sha256": result.get("cohort_manifest_sha256"),
                "raw_market_snapshot_id": (raw_snapshot_ids or {}).get(target),
                "price_market_snapshot_id": result.get("price_market_snapshot_id"),
                "code_version": code_version(),
            })

        for metric, prefix in [
            ("return_30d", "return"),
            ("drawdown_30d", "drawdown"),
            ("max_gain_30d", "max_gain"),
        ]:
            for q in [10, 25, 50, 75, 90]:
                row[f"{prefix}_p{q}_pct"] = percentile_value(
                    percentiles, metric, q, "percent_value"
                )
                row[f"{prefix}_p{q}_price"] = percentile_value(
                    percentiles, metric, q, "price_level"
                )

        if run_id:
            append_forecast(dict(row))

        # prediction_log.csv remains the backward-compatible latest-daily view.
        # The immutable source of truth for new runs is forecast_versions.jsonl.
        if not log.empty and {"prediction_date", "asset"}.issubset(log.columns):
            duplicate_mask = (
                (log["prediction_date"].astype(str) == prediction_date) &
                (log["asset"].astype(str) == target)
            )
            log = log[~duplicate_mask].copy()

        log = pd.concat([log, pd.DataFrame([row])], ignore_index=True)

    return log


def to_float(value):
    try:
        return float(value)
    except Exception:
        return np.nan


def bool_is_true(value):
    return str(value).lower() in ["true", "1", "yes"]


def evaluate_prediction_log(log, data, raw_snapshot_ids=None, *, certified_replay=False):
    if log.empty:
        return log

    if "evaluated" not in log.columns:
        log["evaluated"] = False

    for idx, row in log.iterrows():
        if bool_is_true(row.get("evaluated", False)):
            continue

        asset = row.get("asset")

        prediction_date = pd.to_datetime(row.get("prediction_date"), errors="coerce")

        if pd.isna(prediction_date):
            continue

        due_date = prediction_date + pd.Timedelta(30, unit="D")

        forecast_id = row.get("forecast_id")
        generation_snapshot_id = row.get("raw_market_snapshot_id")
        evaluation_snapshot_id = (raw_snapshot_ids or {}).get(asset)
        if pd.isna(forecast_id) or not str(forecast_id).strip():
            if certified_replay:
                if due_date.normalize() > pd.Timestamp.now(tz="UTC").tz_localize(None).normalize():
                    continue
                raise RuntimeError("HISTORICAL_RAW_DATA_NOT_FROZEN")
            continue

        existing = find_evaluation(str(forecast_id), 30, due_date.date().isoformat())
        if existing is not None:
            actual_close = to_float(existing.get("actual_close"))
            actual_return = to_float(existing.get("actual_return_pct"))
            actual_drawdown = to_float(existing.get("drawdown"))
            actual_max_gain = to_float(existing.get("max_gain"))
            drawdown_classes = existing.get("drawdown_classifications") or {}
            max_gain_classes = existing.get("max_gain_classifications") or {}
            log.at[idx, "evaluated"] = True
            log.at[idx, "evaluation_date"] = existing["actual_candle_date"]
            log.at[idx, "actual_30d_price"] = actual_close
            log.at[idx, "actual_30d_return_pct"] = actual_return
            log.at[idx, "actual_drawdown_pct"] = actual_drawdown
            log.at[idx, "actual_max_gain_pct"] = actual_max_gain
            current = to_float(row.get("current_price"))
            log.at[idx, "actual_min_price_30d"] = current * (1 + actual_drawdown / 100)
            log.at[idx, "actual_max_price_30d"] = current * (1 + actual_max_gain / 100)
            expected_direction = {"RIALZISTA": "UP", "RIBASSISTA": "DOWN"}.get(existing.get("direction_forecast"))
            log.at[idx, "directional_correct"] = (
                expected_direction == existing.get("direction_result")
                if expected_direction is not None else np.nan
            )
            median = to_float(row.get("scenario_median_30d"))
            log.at[idx, "central_error_pct"] = abs(actual_close - median) / current * 100
            log.at[idx, "risk_zone_touched"] = drawdown_classes.get("risk_zone_touched")
            log.at[idx, "upside_zone_touched"] = max_gain_classes.get("upside_zone_touched")
            log.at[idx, "return_within_p10_p90"] = existing.get("inside_p10_p90")
            log.at[idx, "drawdown_within_p10_p90"] = drawdown_classes.get("inside_p10_p90")
            log.at[idx, "max_gain_within_p10_p90"] = max_gain_classes.get("inside_p10_p90")
            continue

        if not evaluation_snapshot_id:
            if certified_replay or not generation_snapshot_id:
                raise RuntimeError("HISTORICAL_RAW_DATA_NOT_FROZEN")
            continue

        # The normal daily path freezes the newly acquired evaluation dataset
        # before reaching this point. Certified replay never consults a vendor.
        df = load_frozen_ohlc(str(evaluation_snapshot_id))

        df_index = pd.DatetimeIndex(df.index)

        if df_index.tz is not None:
            df_index = df_index.tz_convert(None)

        df_index = df_index.normalize()

        future_positions = np.where(df_index >= due_date.normalize())[0]

        if len(future_positions) == 0:
            continue

        actual_pos = future_positions[0]
        actual_date = df_index[actual_pos]

        path_mask = (
            (df_index >= prediction_date.normalize()) &
            (df_index <= actual_date)
        )

        path = df.loc[path_mask]

        if len(path) == 0:
            continue

        prediction_price = to_float(row.get("current_price"))

        if np.isnan(prediction_price) or prediction_price <= 0:
            continue

        actual_price = float(df["Close"].iloc[actual_pos])
        actual_return = (actual_price / prediction_price - 1) * 100

        actual_min = float(path["Close"].min())
        actual_drawdown = (actual_min / prediction_price - 1) * 100

        actual_max = float(path["Close"].max())
        actual_max_gain = (actual_max / prediction_price - 1) * 100

        scenario_median_price = to_float(row.get("scenario_median_30d"))
        drawdown_avg_price = to_float(row.get("drawdown_avg_30d"))
        max_gain_avg_price = to_float(row.get("max_gain_avg_30d"))

        verdict_value = str(row.get("verdict", ""))

        if verdict_value == "RIALZISTA":
            directional_correct = actual_return > 0
        elif verdict_value == "RIBASSISTA":
            directional_correct = actual_return < 0
        else:
            directional_correct = np.nan

        if not np.isnan(scenario_median_price):
            central_error_pct = abs(actual_price - scenario_median_price) / prediction_price * 100
        else:
            central_error_pct = np.nan

        risk_zone_touched = (
            actual_min <= drawdown_avg_price
            if not np.isnan(drawdown_avg_price)
            else np.nan
        )

        upside_zone_touched = (
            actual_max >= max_gain_avg_price
            if not np.isnan(max_gain_avg_price)
            else np.nan
        )

        return_p10 = to_float(row.get("return_p10_pct"))
        return_p90 = to_float(row.get("return_p90_pct"))
        drawdown_p10 = to_float(row.get("drawdown_p10_pct"))
        drawdown_p90 = to_float(row.get("drawdown_p90_pct"))
        max_gain_p10 = to_float(row.get("max_gain_p10_pct"))
        max_gain_p90 = to_float(row.get("max_gain_p90_pct"))

        return_within = (
            return_p10 <= actual_return <= return_p90
            if not np.isnan(return_p10) and not np.isnan(return_p90)
            else np.nan
        )

        drawdown_within = (
            drawdown_p10 <= actual_drawdown <= drawdown_p90
            if not np.isnan(drawdown_p10) and not np.isnan(drawdown_p90)
            else np.nan
        )

        max_gain_within = (
            max_gain_p10 <= actual_max_gain <= max_gain_p90
            if not np.isnan(max_gain_p10) and not np.isnan(max_gain_p90)
            else np.nan
        )

        log.at[idx, "evaluated"] = True
        log.at[idx, "evaluation_date"] = actual_date.date().isoformat()
        log.at[idx, "actual_30d_price"] = actual_price
        log.at[idx, "actual_30d_return_pct"] = actual_return
        log.at[idx, "actual_min_price_30d"] = actual_min
        log.at[idx, "actual_drawdown_pct"] = actual_drawdown
        log.at[idx, "actual_max_price_30d"] = actual_max
        log.at[idx, "actual_max_gain_pct"] = actual_max_gain
        log.at[idx, "directional_correct"] = directional_correct
        log.at[idx, "central_error_pct"] = central_error_pct
        log.at[idx, "risk_zone_touched"] = risk_zone_touched
        log.at[idx, "upside_zone_touched"] = upside_zone_touched
        log.at[idx, "return_within_p10_p90"] = return_within
        log.at[idx, "drawdown_within_p10_p90"] = drawdown_within
        log.at[idx, "max_gain_within_p10_p90"] = max_gain_within

        append_evaluation({
                "forecast_id": str(forecast_id),
                "asset": asset,
                "forecast_generated_at_utc": row.get("generated_at_utc"),
                "forecast_date": prediction_date.date().isoformat(),
                "horizon_days": 30,
                "requested_target_date": due_date.date().isoformat(),
                "actual_candle_date": actual_date.date().isoformat(),
                "on_or_after_shift_days": int((actual_date.normalize() - due_date.normalize()).days),
                "actual_close": actual_price,
                "raw_market_snapshot_id": evaluation_snapshot_id,
                "raw_market_snapshot_sha256": str(evaluation_snapshot_id).split(":", 1)[-1],
                "p10": return_p10, "p25": to_float(row.get("return_p25_pct")),
                "p50": to_float(row.get("return_p50_pct")),
                "p75": to_float(row.get("return_p75_pct")), "p90": return_p90,
                "inside_p10_p90": return_within,
                "inside_p25_p75": (
                    to_float(row.get("return_p25_pct")) <= actual_return <= to_float(row.get("return_p75_pct"))
                    if not np.isnan(to_float(row.get("return_p25_pct"))) and not np.isnan(to_float(row.get("return_p75_pct")))
                    else np.nan
                ),
                "direction_forecast": verdict_value,
                "direction_result": "UP" if actual_return > 0 else "DOWN" if actual_return < 0 else "FLAT",
                "actual_return_pct": actual_return,
                "drawdown": actual_drawdown,
                "max_gain": actual_max_gain,
                "drawdown_classifications": {"inside_p10_p90": drawdown_within, "risk_zone_touched": risk_zone_touched},
                "max_gain_classifications": {"inside_p10_p90": max_gain_within, "upside_zone_touched": upside_zone_touched},
                "evaluation_generated_at_utc": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
                "code_version": code_version(),
                "path_price_semantics": "CLOSE_ONLY_LEGACY_COMPATIBLE",
            })

    return log


def boolean_rate(series):
    if series is None or len(series) == 0:
        return np.nan

    valid = series.dropna()

    if len(valid) == 0:
        return np.nan

    valid = valid[
        valid.astype(str).str.lower().isin(["true", "false", "1", "0"])
    ]

    if len(valid) == 0:
        return np.nan

    return valid.astype(str).str.lower().isin(["true", "1"]).mean() * 100


def accuracy_summary(log):
    if log.empty or "evaluated" not in log.columns:
        return pd.DataFrame()

    evaluated_mask = log["evaluated"].astype(str).str.lower().isin(["true", "1"])
    evaluated = log[evaluated_mask].copy()

    if evaluated.empty:
        return pd.DataFrame()

    rows = []

    for asset in sorted(evaluated["asset"].unique()):
        asset_rows = evaluated[evaluated["asset"] == asset].copy()

        central_error = pd.to_numeric(
            asset_rows.get("central_error_pct"),
            errors="coerce"
        ).mean()

        rows.append({
            "asset": asset,
            "evaluated_predictions": len(asset_rows),
            "directional_accuracy_pct": boolean_rate(asset_rows.get("directional_correct")),
            "avg_central_error_pct": central_error,
            "risk_zone_touched_pct": boolean_rate(asset_rows.get("risk_zone_touched")),
            "upside_zone_touched_pct": boolean_rate(asset_rows.get("upside_zone_touched")),
            "return_inside_p10_p90_pct": boolean_rate(asset_rows.get("return_within_p10_p90")),
            "drawdown_inside_p10_p90_pct": boolean_rate(asset_rows.get("drawdown_within_p10_p90")),
            "max_gain_inside_p10_p90_pct": boolean_rate(asset_rows.get("max_gain_within_p10_p90")),
        })

    return pd.DataFrame(rows)


def reliability_label(accuracy_pct, n):
    if n < MIN_CALIBRATION_EVALS or pd.isna(accuracy_pct):
        return "non ancora valutabile"

    if accuracy_pct >= 65:
        return "alta"

    if accuracy_pct >= 55:
        return "media"

    if accuracy_pct >= 45:
        return "debole"

    return "bassa"


def bias_sentence(metric, bias):
    if pd.isna(bias):
        return "Dati insufficienti."

    if metric == "return":
        if bias > 2:
            return "Lo scanner è stato troppo pessimista sul prezzo finale."
        if bias < -2:
            return "Lo scanner è stato troppo ottimista sul prezzo finale."
        return "Lo scanner è stato abbastanza centrato sul prezzo finale."

    if metric == "drawdown":
        if bias < -2:
            return "Lo scanner ha sottostimato il rischio: nella realtà il prezzo è sceso più del previsto."
        if bias > 2:
            return "Lo scanner è stato troppo prudente: nella realtà il prezzo è sceso meno del previsto."
        return "Lo scanner è stato abbastanza centrato sul drawdown."

    if metric == "max_gain":
        if bias > 2:
            return "Lo scanner ha sottostimato gli spike: nella realtà il prezzo è salito più del previsto."
        if bias < -2:
            return "Lo scanner ha sovrastimato gli spike: nella realtà il prezzo è salito meno del previsto."
        return "Lo scanner è stato abbastanza centrato sul max gain."

    return ""


def calibrated_direction(calibrated_return_pct):
    if pd.isna(calibrated_return_pct):
        return "NON DISPONIBILE"

    if calibrated_return_pct > 2:
        return "SALITA"

    if calibrated_return_pct < -2:
        return "DISCESA"

    return "INCERTO"


def evaluated_prediction_rows(log):
    if log.empty or "evaluated" not in log.columns:
        return pd.DataFrame()

    mask = log["evaluated"].astype(str).str.lower().isin(["true", "1"])
    evaluated = log[mask].copy()

    if "prediction_date" in evaluated.columns:
        evaluated["prediction_date_dt"] = pd.to_datetime(
            evaluated["prediction_date"],
            errors="coerce"
        )
        evaluated = evaluated.sort_values("prediction_date_dt")

    return evaluated


def calibration_summary(log):
    rows = []
    evaluated = evaluated_prediction_rows(log)

    for asset in TARGETS:
        asset_rows = evaluated[evaluated.get("asset", pd.Series(dtype=str)) == asset].copy()

        n_total = len(asset_rows)

        base = {
            "asset": asset,
            "evaluated_predictions": n_total,
            "calibration_status": "insufficient_data",
            "used_predictions": 0,
            "directional_accuracy_pct": np.nan,
            "reliability": "non ancora valutabile",
            "return_bias_pct": np.nan,
            "drawdown_bias_pct": np.nan,
            "max_gain_bias_pct": np.nan,
            "avg_actual_return_pct": np.nan,
            "avg_actual_drawdown_pct": np.nan,
            "avg_actual_max_gain_pct": np.nan,
        }

        required_columns = [
            "actual_30d_return_pct",
            "actual_drawdown_pct",
            "actual_max_gain_pct",
            "return_p50_pct",
            "drawdown_p50_pct",
            "max_gain_p50_pct",
        ]

        if n_total < MIN_CALIBRATION_EVALS:
            rows.append(base)
            continue

        missing = [c for c in required_columns if c not in asset_rows.columns]
        if missing:
            base["calibration_status"] = "missing_columns"
            rows.append(base)
            continue

        recent = asset_rows.tail(CALIBRATION_WINDOW).copy()

        actual_return = pd.to_numeric(recent["actual_30d_return_pct"], errors="coerce")
        actual_drawdown = pd.to_numeric(recent["actual_drawdown_pct"], errors="coerce")
        actual_max_gain = pd.to_numeric(recent["actual_max_gain_pct"], errors="coerce")

        predicted_return = pd.to_numeric(recent["return_p50_pct"], errors="coerce")
        predicted_drawdown = pd.to_numeric(recent["drawdown_p50_pct"], errors="coerce")
        predicted_max_gain = pd.to_numeric(recent["max_gain_p50_pct"], errors="coerce")

        return_error = actual_return - predicted_return
        drawdown_error = actual_drawdown - predicted_drawdown
        max_gain_error = actual_max_gain - predicted_max_gain

        acc = boolean_rate(recent.get("directional_correct"))

        base.update({
            "calibration_status": "active" if n_total >= MIN_CALIBRATION_EVALS else "insufficient_data",
            "used_predictions": len(recent),
            "directional_accuracy_pct": acc,
            "reliability": reliability_label(acc, n_total),
            "return_bias_pct": return_error.mean(),
            "drawdown_bias_pct": drawdown_error.mean(),
            "max_gain_bias_pct": max_gain_error.mean(),
            "avg_actual_return_pct": actual_return.mean(),
            "avg_actual_drawdown_pct": actual_drawdown.mean(),
            "avg_actual_max_gain_pct": actual_max_gain.mean(),
        })

        rows.append(base)

    return pd.DataFrame(rows)


def append_accuracy_section(lines, prediction_log):
    lines.append("# Controllo accuratezza dello scanner")
    lines.append("")
    lines.append(
        "Questa sezione controlla se lo scanner sta funzionando davvero. "
        "Ogni giorno viene salvata una previsione. Dopo 30 giorni, lo scanner confronta "
        "quella previsione con quello che è successo realmente."
    )
    lines.append("")
    lines.append("## Come leggerla")
    lines.append("")
    lines.append(
        "- **Previsioni già controllate** = quante vecchie previsioni hanno già compiuto 30 giorni."
    )
    lines.append(
        "- **Direzione corretta** = quante volte lo scanner ha indovinato salita o discesa finale a 30 giorni."
    )
    lines.append(
        "- **Errore medio scenario centrale** = quanto era distante il prezzo reale dal prezzo centrale previsto."
    )
    lines.append(
        "- **Zona rischio toccata** = quante volte il prezzo è sceso fino alla zona di rischio prevista."
    )
    lines.append(
        "- **Zona rialzo toccata** = quante volte il prezzo è salito fino alla zona rialzo prevista."
    )
    lines.append("")

    summary = accuracy_summary(prediction_log)

    if summary.empty:
        lines.append(
            "Per ora non ci sono ancora previsioni vecchie di 30 giorni da controllare."
        )
        lines.append(
            "Il controllo vero inizierà automaticamente dopo il primo mese di utilizzo."
        )
        lines.append("")
        return

    lines.append("## Riassunto accuratezza")
    lines.append("")

    for _, row in summary.iterrows():
        name = asset_name(row["asset"])

        lines.append(f"### {name}")
        lines.append("")
        lines.append(
            f"- Previsioni già controllate: **{int(row['evaluated_predictions'])}**"
        )

        if not np.isnan(row["directional_accuracy_pct"]):
            lines.append(
                f"- Direzione corretta: **{fmt_pct(row['directional_accuracy_pct'])}**"
            )
        else:
            lines.append(
                "- Direzione corretta: non ancora calcolabile, perché molti segnali erano neutrali."
            )

        if not np.isnan(row["avg_central_error_pct"]):
            lines.append(
                f"- Errore medio dello scenario centrale: **{fmt_pct(row['avg_central_error_pct'])}**"
            )

        if not np.isnan(row["risk_zone_touched_pct"]):
            lines.append(
                f"- Zona rischio toccata: **{fmt_pct(row['risk_zone_touched_pct'])}**"
            )

        if not np.isnan(row["upside_zone_touched_pct"]):
            lines.append(
                f"- Zona rialzo media toccata: **{fmt_pct(row['upside_zone_touched_pct'])}**"
            )

        if not np.isnan(row["return_inside_p10_p90_pct"]):
            lines.append(
                f"- Prezzo finale dentro lo scenario 10%-90%: **{fmt_pct(row['return_inside_p10_p90_pct'])}**"
            )

        lines.append("")

    lines.append(
        "Spiegazione semplice: se col tempo la direzione corretta è bassa o l'errore medio è alto, "
        "lo scanner va preso con più cautela. Se invece molte previsioni finiscono dentro i livelli "
        "previsti, allora lo scanner sta diventando più affidabile."
    )
    lines.append("")


def append_calibration_section(lines, prediction_log, all_results):
    lines.append("# Scanner autocalibrato")
    lines.append("")
    lines.append(
        "Questa è una sezione separata dalla previsione storica grezza. "
        "La previsione grezza resta quella basata sui pattern storici. "
        "Qui invece lo scanner guarda i propri errori passati e prova a correggere leggermente la lettura."
    )
    lines.append("")
    lines.append("## Come funziona")
    lines.append("")
    lines.append(
        "Lo scanner confronta le sue vecchie previsioni con la realtà dopo 30 giorni."
    )
    lines.append("")
    lines.append("- Se in passato è stato troppo ottimista, abbassa la stima.")
    lines.append("- Se in passato è stato troppo pessimista, alza la stima.")
    lines.append("- Se ha sottostimato il drawdown, rende la zona rischio più prudente.")
    lines.append("- Se ha sovrastimato gli spike, riduce la zona rialzo calibrata.")
    lines.append("")
    lines.append(
        "La calibrazione non modifica il codice. Crea solo una seconda lettura: "
        "**scanner grezzo** contro **scanner corretto dai suoi errori reali**."
    )
    lines.append("")
    lines.append(
        f"Regola: servono almeno **{MIN_CALIBRATION_EVALS} previsioni controllate per asset** "
        "prima di applicare la calibrazione. Prima di allora mostra solo dati insufficienti."
    )
    lines.append("")

    calibration = calibration_summary(prediction_log)

    if calibration.empty:
        lines.append("Dati insufficienti per qualsiasi calibrazione.")
        lines.append("")
        return

    for target, result in all_results.items():
        name = asset_name(target)
        current_price = result["prices"]["current_price"]
        percentiles = result["percentiles"]
        summary = result["summary"]

        cal_row = calibration[calibration["asset"] == target]

        if cal_row.empty:
            continue

        cal = cal_row.iloc[0]
        n = int(cal["evaluated_predictions"])

        lines.append(f"## {name}")
        lines.append("")

        if cal["calibration_status"] != "active":
            lines.append(
                f"Dati ancora insufficienti: previsioni controllate **{n}** su "
                f"**{MIN_CALIBRATION_EVALS}** necessarie."
            )
            lines.append("")
            lines.append(
                "Per ora si usa solo lo scanner storico grezzo. "
                "Quando ci saranno abbastanza previsioni controllate, qui apparirà la lettura autocalibrata."
            )
            lines.append("")
            continue

        raw_return_p50, raw_return_p50_price = get_percentile_price(
            percentiles,
            "return_30d",
            50
        )
        raw_drawdown_p50, raw_drawdown_p50_price = get_percentile_price(
            percentiles,
            "drawdown_30d",
            50
        )
        raw_max_gain_p50, raw_max_gain_p50_price = get_percentile_price(
            percentiles,
            "max_gain_30d",
            50
        )

        return_bias = float(cal["return_bias_pct"])
        drawdown_bias = float(cal["drawdown_bias_pct"])
        max_gain_bias = float(cal["max_gain_bias_pct"])

        calibrated_return = raw_return_p50 + return_bias
        calibrated_drawdown = raw_drawdown_p50 + drawdown_bias
        calibrated_max_gain = raw_max_gain_p50 + max_gain_bias

        calibrated_return_price = pct_to_price(current_price, calibrated_return)
        calibrated_drawdown_price = pct_to_price(current_price, calibrated_drawdown)
        calibrated_max_gain_price = pct_to_price(current_price, calibrated_max_gain)

        raw_direction, up_prob, down_prob = direction_label(summary["positive_cases_30d"])
        final_direction = calibrated_direction(calibrated_return)

        lines.append(f"- Previsioni controllate: **{n}**")
        lines.append(f"- Previsioni usate per la calibrazione recente: **{int(cal['used_predictions'])}**")
        lines.append(f"- Affidabilità direzionale storica: **{cal['reliability']}**")
        if not pd.isna(cal["directional_accuracy_pct"]):
            lines.append(f"- Direzione indovinata in passato: **{fmt_pct(cal['directional_accuracy_pct'])}**")
        lines.append("")

        lines.append("### Confronto: grezzo vs autocalibrato")
        lines.append("")
        lines.append(f"- Direzione grezza oggi: **{raw_direction}**")
        lines.append(f"- Direzione calibrata oggi: **{final_direction}**")
        lines.append("")

        lines.append("### Return 30d — prezzo finale fra 30 giorni")
        lines.append("")
        lines.append(f"- Grezzo: **{fmt_pct(raw_return_p50)}** → **{fmt_price(raw_return_p50_price)}**")
        lines.append(f"- Correzione imparata dagli errori: **{fmt_pct(return_bias)}**")
        lines.append(f"- Calibrato: **{fmt_pct(calibrated_return)}** → **{fmt_price(calibrated_return_price)}**")
        lines.append(f"- Lettura: {bias_sentence('return', return_bias)}")
        lines.append("")

        lines.append("### Drawdown 30d — rischio di discesa durante il mese")
        lines.append("")
        lines.append(f"- Grezzo: **{fmt_pct(raw_drawdown_p50)}** → **{fmt_price(raw_drawdown_p50_price)}**")
        lines.append(f"- Correzione imparata dagli errori: **{fmt_pct(drawdown_bias)}**")
        lines.append(f"- Calibrato: **{fmt_pct(calibrated_drawdown)}** → **{fmt_price(calibrated_drawdown_price)}**")
        lines.append(f"- Lettura: {bias_sentence('drawdown', drawdown_bias)}")
        lines.append("")

        lines.append("### Max gain 30d — rialzo/spike durante il mese")
        lines.append("")
        lines.append(f"- Grezzo: **{fmt_pct(raw_max_gain_p50)}** → **{fmt_price(raw_max_gain_p50_price)}**")
        lines.append(f"- Correzione imparata dagli errori: **{fmt_pct(max_gain_bias)}**")
        lines.append(f"- Calibrato: **{fmt_pct(calibrated_max_gain)}** → **{fmt_price(calibrated_max_gain_price)}**")
        lines.append(f"- Lettura: {bias_sentence('max_gain', max_gain_bias)}")
        lines.append("")

        lines.append("### Come leggerlo")
        lines.append("")
        lines.append(
            "La parte grezza ti dice cosa mostrano i vecchi pattern storici. "
            "La parte calibrata ti dice come cambia quella lettura dopo aver visto se lo scanner, "
            "nel mercato reale, è stato troppo ottimista o troppo pessimista."
        )
        lines.append("")


def add_how_to_read_report(lines):
    lines.append("# Come leggere questo report")
    lines.append("")
    lines.append("Leggilo sempre in questo ordine:")
    lines.append("")
    lines.append("1. **Direzione più probabile**: ti dice se storicamente era più facile salita, discesa o incertezza.")
    lines.append("2. **Casi positivi / negativi**: ti dice la percentuale storica di salita o discesa dopo 30 giorni.")
    lines.append("3. **Return 30d**: ti dice dove potrebbe stare il prezzo fra 30 giorni.")
    lines.append("4. **Drawdown 30d**: ti dice quanto potrebbe scendere durante quei 30 giorni.")
    lines.append("5. **Max gain 30d**: ti dice quanto potrebbe salire durante quei 30 giorni.")
    lines.append("6. **Scanner autocalibrato**: dopo abbastanza dati, confronta previsione e realtà e corregge la lettura.")
    lines.append("")
    lines.append("La frase più importante è questa:")
    lines.append("")
    lines.append("> **Return = prezzo finale dopo 30 giorni. Drawdown = discesa durante il mese. Max gain = rialzo durante il mese.**")
    lines.append("")
    lines.append("---")
    lines.append("")


def add_percentile_cheatsheet(lines):
    lines.append("# Scheda veloce: cosa sono i percentili")
    lines.append("")
    lines.append(
        "I **percentili** sono solo un modo per trasformare i 40 casi storici simili "
        "in scenari semplici."
    )
    lines.append("")
    lines.append("## Traduzione semplice")
    lines.append("")
    lines.append("- **Percentile 10%** = molto male / scenario brutto.")
    lines.append("- **Percentile 25%** = male / scenario negativo.")
    lines.append("- **Percentile 50%** = normale / scenario centrale. È il più importante.")
    lines.append("- **Percentile 75%** = bene / scenario buono.")
    lines.append("- **Percentile 90%** = molto bene / scenario molto forte.")
    lines.append("")
    lines.append("## Cosa guardare davvero")
    lines.append("")
    lines.append("- Per capire la situazione normale: guarda sempre il **Percentile 50%**.")
    lines.append("- Per capire il rischio con leva: guarda **Drawdown 25%** e **Drawdown 10%**.")
    lines.append("- Per capire un possibile take profit: guarda **Max gain 50%** e **Max gain 75%**.")
    lines.append("")
    lines.append("## I tre tipi di percentili")
    lines.append("")
    lines.append("- **Percentili Return 30d** = dove potrebbe stare il prezzo fra 30 giorni.")
    lines.append("- **Percentili Drawdown 30d** = quanto potrebbe scendere durante i 30 giorni.")
    lines.append("- **Percentili Max gain 30d** = quanto potrebbe salire durante i 30 giorni.")
    lines.append("")
    lines.append("## Esempio semplice")
    lines.append("")
    lines.append("Se SOL oggi vale 82 $ e il report dice:")
    lines.append("")
    lines.append("- **Return 50% → 81 $**: fra 30 giorni lo scenario normale è circa 81 $.")
    lines.append("- **Drawdown 50% → 77 $**: durante il mese può scendere normalmente verso 77 $.")
    lines.append("- **Max gain 50% → 92 $**: durante il mese può fare uno spike normale verso 92 $.")
    lines.append("")
    lines.append("Quindi può salire e scendere durante il mese, ma il **return** guarda solo dove finisce dopo 30 giorni.")
    lines.append("")
    lines.append("---")
    lines.append("")


def add_asset_simple_map(lines, target, result):
    name = asset_name(target)
    summary = result["summary"]
    prices = result["prices"]
    percentiles = result["percentiles"]
    verdict_value = result["verdict"]

    direction, up_prob, down_prob = direction_label(summary["positive_cases_30d"])
    strength = signal_strength(summary["positive_cases_30d"])

    return_p10, return_p10_price = get_percentile_price(percentiles, "return_30d", 10)
    return_p25, return_p25_price = get_percentile_price(percentiles, "return_30d", 25)
    return_p50, return_p50_price = get_percentile_price(percentiles, "return_30d", 50)
    return_p75, return_p75_price = get_percentile_price(percentiles, "return_30d", 75)
    return_p90, return_p90_price = get_percentile_price(percentiles, "return_30d", 90)

    drawdown_p10, drawdown_p10_price = get_percentile_price(percentiles, "drawdown_30d", 10)
    drawdown_p25, drawdown_p25_price = get_percentile_price(percentiles, "drawdown_30d", 25)
    drawdown_p50, drawdown_p50_price = get_percentile_price(percentiles, "drawdown_30d", 50)

    max_gain_p50, max_gain_p50_price = get_percentile_price(percentiles, "max_gain_30d", 50)
    max_gain_p75, max_gain_p75_price = get_percentile_price(percentiles, "max_gain_30d", 75)
    max_gain_p90, max_gain_p90_price = get_percentile_price(percentiles, "max_gain_30d", 90)

    lines.append(f"# {name} — mappa semplice dei prossimi 30 giorni")
    lines.append("")
    lines.append(f"**Semaforo:** {semaforo(verdict_value)}")
    lines.append(f"**Prezzo attuale:** {fmt_price(prices['current_price'])}")
    lines.append("")
    lines.append(f"**Direzione più probabile a 30 giorni:** **{direction}**")
    lines.append(f"- Probabilità storica di salita: **{fmt_pct(up_prob)}**")
    lines.append(f"- Probabilità storica di discesa: **{fmt_pct(down_prob)}**")
    lines.append(f"- Quanto è netto il segnale: **{strength}**")
    lines.append("")
    lines.append("## Come leggere questa parte")
    lines.append("")
    lines.append(
        "- **Probabilità storica di salita** = su 40 casi simili, quanti hanno chiuso sopra dopo 30 giorni."
    )
    lines.append(
        "- **Probabilità storica di discesa** = su 40 casi simili, quanti hanno chiuso sotto dopo 30 giorni."
    )
    lines.append(
        "- **Quanto è netto il segnale** = quanto è grande la differenza tra salita e discesa. "
        "Non vuol dire certezza, vuol dire solo che il risultato storico non è vicino al 50/50."
    )
    lines.append("")
    lines.append(simple_direction_sentence(direction, strength))
    lines.append("")

    lines.append("## 1. Return 30d — prezzo fra 30 giorni")
    lines.append("")
    lines.append(
        "**Return** significa rendimento finale. Qui guardiamo dove potrebbe stare il prezzo "
        "**alla fine dei 30 giorni**, non durante il percorso."
    )
    lines.append("")
    lines.append(f"- Se va molto male: **{fmt_price(return_p10_price)}** ({fmt_pct(return_p10)})")
    lines.append(f"- Se va male: **{fmt_price(return_p25_price)}** ({fmt_pct(return_p25)})")
    lines.append(f"- Scenario normale: **{fmt_price(return_p50_price)}** ({fmt_pct(return_p50)})")
    lines.append(f"- Se va bene: **{fmt_price(return_p75_price)}** ({fmt_pct(return_p75)})")
    lines.append(f"- Se va molto bene: **{fmt_price(return_p90_price)}** ({fmt_pct(return_p90)})")
    lines.append("")
    lines.append("**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.")
    lines.append("")

    lines.append("## 2. Drawdown 30d — discesa durante i 30 giorni")
    lines.append("")
    lines.append(
        "**Drawdown** significa la discesa massima durante il periodo. "
        "Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese."
    )
    lines.append("")
    lines.append(f"- Discesa normale: **{fmt_price(drawdown_p50_price)}** ({fmt_pct(drawdown_p50)})")
    lines.append(f"- Discesa brutta: **{fmt_price(drawdown_p25_price)}** ({fmt_pct(drawdown_p25)})")
    lines.append(f"- Discesa molto brutta: **{fmt_price(drawdown_p10_price)}** ({fmt_pct(drawdown_p10)})")
    lines.append("")
    lines.append(
        "**Come leggerlo:** se usi leva, questa è la parte più importante. "
        "Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui."
    )
    lines.append("")

    lines.append("## 3. Max gain 30d — rialzo durante i 30 giorni")
    lines.append("")
    lines.append(
        "**Max gain** significa il massimo rialzo toccato durante il mese. "
        "Non è il prezzo finale: può essere anche solo uno spike temporaneo."
    )
    lines.append("")
    lines.append(f"- Rialzo normale: **{fmt_price(max_gain_p50_price)}** ({fmt_pct(max_gain_p50)})")
    lines.append(f"- Rialzo buono: **{fmt_price(max_gain_p75_price)}** ({fmt_pct(max_gain_p75)})")
    lines.append(f"- Rialzo molto forte: **{fmt_price(max_gain_p90_price)}** ({fmt_pct(max_gain_p90)})")
    lines.append("")
    lines.append(
        "**Come leggerlo:** questa parte serve per capire possibili zone di take profit. "
        "Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune."
    )
    lines.append("")

    lines.append("## Lettura pratica finale")
    lines.append("")

    lines.append(
        f"Scenario normale: nei casi simili, {name} tendeva a muoversi tra "
        f"una zona bassa intorno a **{fmt_price(drawdown_p50_price)}** "
        f"e uno spike normale intorno a **{fmt_price(max_gain_p50_price)}**."
    )
    lines.append("")

    if direction == "DISCESA":
        lines.append(
            f"La chiusura a 30 giorni era più spesso negativa: salita {fmt_pct(up_prob)}, "
            f"discesa {fmt_pct(down_prob)}. Quindi la lettura principale è prudente/debole."
        )
    elif direction == "SALITA":
        lines.append(
            f"La chiusura a 30 giorni era più spesso positiva: salita {fmt_pct(up_prob)}, "
            f"discesa {fmt_pct(down_prob)}. Quindi la lettura principale è favorevole."
        )
    else:
        lines.append(
            f"La chiusura a 30 giorni è incerta: salita {fmt_pct(up_prob)}, "
            f"discesa {fmt_pct(down_prob)}. Non c'è un vantaggio netto."
        )

    lines.append("")

    if target == "BTC-USD":
        lines.append(
            "Nota leva BTC: se la liquidazione è vicina a 51.000 $, guarda soprattutto "
            "la discesa brutta e molto brutta. Il prezzo può recuperare dopo, ma la leva può saltare prima."
        )
        lines.append("")

    lines.append("---")
    lines.append("")


def build_markdown_report(all_results, generated_at, prediction_log):
    lines = []

    lines.append("# Report giornaliero BTC / SOL / DOGE")
    lines.append("")
    lines.append(f"Aggiornato il: **{generated_at} UTC**")
    lines.append("")
    lines.append(
        "Questo report confronta il grafico attuale di Bitcoin, Solana e Dogecoin "
        "con tanti grafici storici di altre crypto."
    )
    lines.append("")
    lines.append(
        "Non è una previsione certa. È uno scanner statistico: "
        "guarda situazioni simili già successe e mostra cosa accadde dopo nei 30 giorni successivi."
    )
    lines.append("")

    add_how_to_read_report(lines)
    add_percentile_cheatsheet(lines)

    lines.append("# Lettura velocissima")
    lines.append("")
    lines.append(
        "Questa è la parte da leggere per prima. Ti dice subito se lo scenario è più da salita, discesa o incertezza."
    )
    lines.append("")

    for target, result in all_results.items():
        name = asset_name(target)
        summary = result["summary"]
        prices = result["prices"]
        percentiles = result["percentiles"]

        direction, up_prob, down_prob = direction_label(summary["positive_cases_30d"])
        strength = signal_strength(summary["positive_cases_30d"])

        return_p50, return_p50_price = get_percentile_price(percentiles, "return_30d", 50)
        drawdown_p50, drawdown_p50_price = get_percentile_price(percentiles, "drawdown_30d", 50)
        drawdown_p25, drawdown_p25_price = get_percentile_price(percentiles, "drawdown_30d", 25)
        max_gain_p50, max_gain_p50_price = get_percentile_price(percentiles, "max_gain_30d", 50)
        max_gain_p75, max_gain_p75_price = get_percentile_price(percentiles, "max_gain_30d", 75)

        lines.append(f"## {name}")
        lines.append(f"- Direzione più probabile a 30 giorni: **{direction}**")
        lines.append(f"- Casi positivi / salita storica: **{fmt_pct(up_prob)}**")
        lines.append(f"- Casi negativi / discesa storica: **{fmt_pct(down_prob)}**")
        lines.append(f"- Quanto è netto il segnale: **{strength}**")
        lines.append(f"- Prezzo attuale: **{fmt_price(prices['current_price'])}**")
        lines.append(f"- Return normale fra 30 giorni: **{fmt_price(return_p50_price)}** ({fmt_pct(return_p50)})")
        lines.append(f"- Drawdown normale durante il mese: **{fmt_price(drawdown_p50_price)}** ({fmt_pct(drawdown_p50)})")
        lines.append(f"- Drawdown brutto da rispettare: **{fmt_price(drawdown_p25_price)}** ({fmt_pct(drawdown_p25)})")
        lines.append(f"- Max gain normale durante il mese: **{fmt_price(max_gain_p50_price)}** ({fmt_pct(max_gain_p50)})")
        lines.append(f"- Max gain buono / take profit ottimistico: **{fmt_price(max_gain_p75_price)}** ({fmt_pct(max_gain_p75)})")
        lines.append("")
        lines.append(
            "**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. "
            "Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. "
            "Max gain ti dice il possibile rialzo durante il mese."
        )
        lines.append("")

    lines.append("## Messaggio del giorno")
    lines.append("")

    directions = [
        direction_label(result["summary"]["positive_cases_30d"])[0]
        for result in all_results.values()
    ]

    if directions.count("DISCESA") >= 2:
        lines.append(
            "Il quadro generale oggi è prudente/debole. "
            "Lo scanner vede più rischio di discesa che salita pulita su più asset."
        )
    elif directions.count("SALITA") >= 2:
        lines.append(
            "Il quadro generale oggi è più favorevole. "
            "Lo scanner vede più possibilità di salita su più asset."
        )
    else:
        lines.append(
            "Il quadro generale oggi è misto. "
            "Alcuni asset possono avere lettura diversa, quindi è meglio valutare asset per asset."
        )

    lines.append("")
    lines.append("---")
    lines.append("")

    lines.append("# Mappa semplice asset per asset")
    lines.append("")

    for target, result in all_results.items():
        add_asset_simple_map(lines, target, result)

    lines.append("# Come leggere correttamente i 30 giorni")
    lines.append("")
    lines.append(
        "Ogni report giornaliero è una previsione statistica sui **prossimi 30 giorni**."
    )
    lines.append("")
    lines.append("Ci sono tre dati diversi:")
    lines.append("")
    lines.append("1. **Return 30d** = dove potrebbe stare il prezzo fra 30 giorni.")
    lines.append("2. **Drawdown 30d** = quanto potrebbe scendere durante quei 30 giorni.")
    lines.append("3. **Max gain 30d** = quanto potrebbe salire al massimo durante quei 30 giorni.")
    lines.append("")
    lines.append(
        "Il prezzo può salire durante il mese e poi chiudere sotto, oppure scendere prima e poi recuperare. "
        "Per chi usa leva, il drawdown è spesso più importante del prezzo finale."
    )
    lines.append("")

    append_accuracy_section(lines, prediction_log)

    lines.append("---")
    lines.append("")

    append_calibration_section(lines, prediction_log, all_results)

    for target, result in all_results.items():
        name = asset_name(target)
        verdict_value = result["verdict"]
        summary = result["summary"]
        prices = result["prices"]
        percentiles = result["percentiles"]

        lines.append("---")
        lines.append("")
        lines.append(f"# Approfondimento tecnico — {name} ({target})")
        lines.append("")
        lines.append(f"## Semaforo: {semaforo(verdict_value)}")
        lines.append("")
        lines.append(f"**Prezzo attuale:** {fmt_price(prices['current_price'])}")
        lines.append("")
        lines.append(simple_verdict_text(target, verdict_value))
        lines.append("")

        lines.append("## Casi positivi e negativi")
        lines.append("")
        lines.append(f"- Casi positivi dopo 30 giorni: **{fmt_number_it(summary['positive_cases_30d'])}%**")
        lines.append(f"- Casi negativi dopo 30 giorni: **{fmt_number_it(100 - summary['positive_cases_30d'])}%**")
        lines.append("")
        lines.append(
            "**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, "
            "il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire "
            "se storicamente era più probabile salita o discesa."
        )
        lines.append("")

        lines.append("## Cosa dicono i 40 casi storici più simili")
        lines.append("")
        lines.append(f"- Somiglianza media dei pattern: **{fmt_pct(summary['similarity_avg'])}**")
        lines.append(f"- Rendimento medio dopo 30 giorni: **{fmt_pct(summary['return_30d_avg'])}**")
        lines.append(f"- Rendimento centrale dopo 30 giorni: **{fmt_pct(summary['return_30d_median'])}**")
        lines.append(f"- Discesa media durante i 30 giorni: **{fmt_pct(summary['drawdown_30d_avg'])}**")
        lines.append(f"- Massimo rialzo medio durante i 30 giorni: **{fmt_pct(summary['max_gain_30d_avg'])}**")
        lines.append("")
        lines.append(
            "**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. "
            "La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda "
            "il possibile spike durante il mese."
        )
        lines.append("")

        lines.append("## Livelli principali")
        lines.append("")
        lines.append(f"- Scenario medio a 30 giorni: **{fmt_price(prices['scenario_avg_30d'])}**")
        lines.append(f"- Scenario centrale a 30 giorni: **{fmt_price(prices['scenario_median_30d'])}**")
        lines.append(f"- Zona di rischio media: **{fmt_price(prices['drawdown_avg_30d'])}**")
        lines.append(f"- Zona di rialzo media: **{fmt_price(prices['max_gain_avg_30d'])}**")
        lines.append("")
        lines.append(
            "**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. "
            "Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike."
        )
        lines.append("")

        lines.append("## Percentili return — prezzo fra 30 giorni")
        lines.append("")
        lines.append(
            "**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi."
        )
        lines.append("")
        lines.extend(percentile_lines(percentiles, "return_30d"))
        lines.append("")

        lines.append("## Percentili drawdown — discesa durante i 30 giorni")
        lines.append("")
        lines.append(
            "**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera."
        )
        lines.append("")
        lines.extend(percentile_lines(percentiles, "drawdown_30d"))
        lines.append("")

        lines.append("## Percentili max gain — rialzo durante i 30 giorni")
        lines.append("")
        lines.append(
            "**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente."
        )
        lines.append("")
        lines.extend(percentile_lines(percentiles, "max_gain_30d"))
        lines.append("")

        lines.append("## Dati tecnici per controllo")
        lines.append("")
        lines.append(
            "Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. "
            "Non è obbligatorio leggerla ogni giorno."
        )
        lines.append("")

        top = result["matches"].head(10)[[
            "similar_asset", "start_date", "end_date", "similarity",
            "return_30d", "drawdown_30d", "max_gain_30d"
        ]].round(2)

        lines.append(top.to_markdown(index=False))
        lines.append("")

    return "\n".join(lines)


def target_asset_code(ticker):
    return ticker.replace("-USD", "")


def export_latest_scanner_matches(all_results, generated_at):
    """
    Esporta tutti i 40 match puliti usati dallo scanner per ogni asset.

    Questo file serve ai report successivi, per esempio:
    - extreme_cases_path_report.py
    - grafici dei casi positivi/negativi estremi
    - analisi dei percorsi storici dopo il match

    Output:
    reports/latest_scanner_matches.csv
    """

    rows = []

    for target, result in all_results.items():
        matches = result.get("matches")

        if matches is None or matches.empty:
            continue

        target_asset = target_asset_code(target)
        m = matches.copy().reset_index(drop=True)

        for idx, row in m.iterrows():
            match_rank = idx + 1

            return_30d = to_float(row.get("return_30d"))
            drawdown_30d = to_float(row.get("drawdown_30d"))
            max_gain_30d = to_float(row.get("max_gain_30d"))

            if not np.isnan(return_30d) and return_30d > 0:
                direction_30d = "POSITIVE"
                positive_case_30d = True
                negative_case_30d = False
            elif not np.isnan(return_30d) and return_30d < 0:
                direction_30d = "NEGATIVE"
                positive_case_30d = False
                negative_case_30d = True
            else:
                direction_30d = "FLAT"
                positive_case_30d = False
                negative_case_30d = False

            export_row = {
                "generated_at_utc": generated_at,
                "target_asset": target_asset,
                "target_ticker": target,
                "match_rank": match_rank,
                "similar_asset": row.get("similar_asset"),
                "start_date": row.get("start_date"),
                "end_date": row.get("end_date"),
                "similarity": row.get("similarity"),
                "direction_30d": direction_30d,
                "positive_case_30d": positive_case_30d,
                "negative_case_30d": negative_case_30d,
                "return_30d": return_30d,
                "drawdown_30d": drawdown_30d,
                "max_gain_30d": max_gain_30d,
                "window": WINDOW,
                "step": STEP,
                "top_n_raw": TOP_N,
                "clean_top_n": CLEAN_TOP_N,
                "min_gap_days": MIN_GAP_DAYS,
            }

            for d in FORWARD_DAYS:
                export_row[f"return_{d}d"] = row.get(f"return_{d}d")
                export_row[f"drawdown_{d}d"] = row.get(f"drawdown_{d}d")
                export_row[f"max_gain_{d}d"] = row.get(f"max_gain_{d}d")

            rows.append(export_row)

    if not rows:
        empty = pd.DataFrame()
        empty.to_csv(LATEST_SCANNER_MATCHES_PATH, index=False, encoding="utf-8", lineterminator="\n")
        return empty

    out = pd.DataFrame(rows)

    preferred_columns = [
        "generated_at_utc",
        "target_asset",
        "target_ticker",
        "match_rank",
        "similar_asset",
        "start_date",
        "end_date",
        "similarity",
        "direction_30d",
        "positive_case_30d",
        "negative_case_30d",
        "return_30d",
        "drawdown_30d",
        "max_gain_30d",
    ]

    for d in FORWARD_DAYS:
        preferred_columns.extend([
            f"return_{d}d",
            f"drawdown_{d}d",
            f"max_gain_{d}d",
        ])

    preferred_columns.extend([
        "window",
        "step",
        "top_n_raw",
        "clean_top_n",
        "min_gap_days",
    ])

    existing_columns = [c for c in preferred_columns if c in out.columns]
    remaining_columns = [c for c in out.columns if c not in existing_columns]

    out = out[existing_columns + remaining_columns]
    out.to_csv(LATEST_SCANNER_MATCHES_PATH, index=False, encoding="utf-8", lineterminator="\n")

    return out



def _atomic_write_text(path, text):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(text, encoding="utf-8", newline="\n")
    tmp.replace(path)


def _json_clean(value):
    if isinstance(value, dict):
        return {str(k): _json_clean(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [_json_clean(v) for v in value]
    if isinstance(value, (np.integer,)):
        return int(value)
    if isinstance(value, (np.floating, float)):
        return None if pd.isna(value) else float(value)
    if pd.isna(value) if not isinstance(value, str) else False:
        return None
    return value


def export_latest_scanner_summary(all_results, generated_at, snapshot=None):
    """Esporta una riga strutturata per asset, pronta per il Global Confluence.

    Questo elimina la necessità di estrarre direzione e percentili dal Markdown.
    I file prodotti sono:
    - reports/latest_scanner_summary.csv
    - reports/latest_scanner_summary.json
    """
    Path(LATEST_SCANNER_SUMMARY_CSV_PATH).parent.mkdir(parents=True, exist_ok=True)
    rows = []

    for target, result in all_results.items():
        asset = target_asset_code(target)
        summary = result["summary"]
        prices = result["prices"]
        percentiles = result["percentiles"]
        direction, up_prob, down_prob = direction_label(summary["positive_cases_30d"])

        row = {
            "generated_at_utc": generated_at,
            "snapshot_generated_at_utc": (snapshot or {}).get("generated_at_utc"),
            "snapshot_candle_date_utc": get_snapshot_candle_date(snapshot or {}, target),
            "asset": asset,
            "ticker": target,
            "current_price": to_float(prices.get("current_price")),
            "verdict": result.get("verdict"),
            "direction_30d": direction,
            "signal_strength": signal_strength(up_prob),
            "match_count": int(summary.get("match_count", 0)),
            "positive_cases_30d": to_float(up_prob),
            "negative_cases_30d": to_float(down_prob),
            "similarity_avg": to_float(summary.get("similarity_avg")),
            "similarity_median": to_float(summary.get("similarity_median")),
            "return_30d_avg": to_float(summary.get("return_30d_avg")),
            "return_30d_median": to_float(summary.get("return_30d_median")),
            "drawdown_30d_avg": to_float(summary.get("drawdown_30d_avg")),
            "max_gain_30d_avg": to_float(summary.get("max_gain_30d_avg")),
            "scenario_avg_30d_price": to_float(prices.get("scenario_avg_30d")),
            "scenario_median_30d_price": to_float(prices.get("scenario_median_30d")),
            "drawdown_avg_30d_price": to_float(prices.get("drawdown_avg_30d")),
            "max_gain_avg_30d_price": to_float(prices.get("max_gain_avg_30d")),
        }

        for metric, prefix in [
            ("return_30d", "return"),
            ("drawdown_30d", "drawdown"),
            ("max_gain_30d", "max_gain"),
        ]:
            for q in [10, 25, 50, 75, 90]:
                pct, price = get_percentile_price(percentiles, metric, q)
                row[f"{prefix}_p{q}_pct"] = to_float(pct)
                row[f"{prefix}_p{q}_price"] = to_float(price)

        rows.append(row)

    out = pd.DataFrame(rows).sort_values("asset").reset_index(drop=True)
    out.to_csv(
        LATEST_SCANNER_SUMMARY_CSV_PATH,
        index=False,
        encoding="utf-8",
        lineterminator="\n",
    )

    payload = {
        "schema_version": 1,
        "generated_at_utc": generated_at,
        "snapshot_generated_at_utc": (snapshot or {}).get("generated_at_utc"),
        "assets": {row["asset"]: row for row in rows},
    }
    _atomic_write_text(
        LATEST_SCANNER_SUMMARY_JSON_PATH,
        json.dumps(_json_clean(payload), ensure_ascii=False, indent=2, allow_nan=False) + "\n",
    )
    return out

def main():
    generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    generated_at_iso = generated_at.replace(" ", "T") + "Z"
    os.makedirs("reports", exist_ok=True)

    run_id = new_run_id(generated_at_iso)
    data, raw_snapshot_ids = download_data(
        run_id=run_id, downloaded_at_utc=generated_at_iso
    )

    # Preferisce lo snapshot già creato dal workflow. Se manca o è vecchio,
    # lo ricrea usando esattamente i dati appena scaricati dallo scanner.
    snapshot = load_market_snapshot(max_age_hours=24)
    required_assets = {target_asset_code(t) for t in TARGETS}
    if not snapshot or not required_assets.issubset(set(snapshot.get("assets", {}))):
        snapshot = write_snapshot_from_asset_data(
            data, generated_at_utc=generated_at_iso
        )

    price_snapshot_ids = {}
    for record in (snapshot.get("assets", {}) if snapshot else {}).values():
        ticker = record.get("ticker")
        candle_date = record.get("candle_date_utc")
        if not ticker or not candle_date:
            continue
        snapshot_frame = pd.DataFrame([{
            "Open": record.get("open"), "High": record.get("high"),
            "Low": record.get("low"), "Close": record.get("close"),
            "Volume": record.get("volume"),
        }], index=pd.DatetimeIndex([pd.Timestamp(candle_date, tz="UTC")]))
        price_snapshot_ids[ticker] = freeze_ohlc(
            snapshot_frame, ticker=ticker,
            source=str(snapshot.get("source", "shared market snapshot")),
            downloaded_at_utc=str(snapshot.get("generated_at_utc", generated_at_iso)),
            requested_interval="1d", requested_range=f"candle={candle_date}",
            run_id=run_id, purpose="forecast_current_price",
        )

    all_results = {}

    for target in TARGETS:
        print(f"Scanning {target}...")

        if target not in data:
            raise RuntimeError(f"Target {target} not found in downloaded data.")

        matches_raw = find_similar_patterns(target, data)
        matches_clean = deoverlap_matches(matches_raw)
        cohort_id, cohort_sha = freeze_cohort(
            matches_clean, target=target, run_id=run_id,
            generated_at_utc=generated_at_iso,
        )

        current_price = get_snapshot_price(snapshot, target)
        if current_price is None:
            current_price = float(data[target]["Close"].iloc[-1])

        all_results[target] = {
            "matches": matches_clean,
            "summary": summary_table(matches_clean),
            "prices": price_scenarios(matches_clean, current_price),
            "percentiles": percentile_report(matches_clean, current_price),
            "verdict": verdict(matches_clean),
            "cohort_id": cohort_id,
            "cohort_manifest_sha256": cohort_sha,
            "price_market_snapshot_id": price_snapshot_ids.get(target),
        }

        safe_target = target.replace("-USD", "")
        matches_clean.to_csv(
            f"reports/{safe_target}_matches.csv",
            index=False,
            encoding="utf-8",
            lineterminator="\n",
        )

        all_results[target]["percentiles"].to_csv(
            f"reports/{safe_target}_percentiles.csv",
            index=False,
            encoding="utf-8",
            lineterminator="\n",
        )

    latest_matches = export_latest_scanner_matches(all_results, generated_at)
    latest_summary = export_latest_scanner_summary(
        all_results, generated_at, snapshot=snapshot
    )

    prediction_log = load_prediction_log()
    prediction_log = update_prediction_log(
        prediction_log, all_results, generated_at, run_id, raw_snapshot_ids
    )
    prediction_log = evaluate_prediction_log(prediction_log, data, raw_snapshot_ids)
    prediction_log.to_csv(PREDICTION_LOG_PATH, index=False, encoding="utf-8", lineterminator="\n")

    accuracy = accuracy_summary(prediction_log)
    accuracy.to_csv(ACCURACY_REPORT_PATH, index=False, encoding="utf-8", lineterminator="\n")

    calibration = calibration_summary(prediction_log)
    calibration.to_csv(CALIBRATION_REPORT_PATH, index=False, encoding="utf-8", lineterminator="\n")

    report_md = build_markdown_report(all_results, generated_at, prediction_log)

    _atomic_write_text("reports/latest_report.md", report_md.rstrip() + "\n")

    print(report_md)
    print("Report saved in reports/latest_report.md")
    print("Prediction log saved in reports/prediction_log.csv")
    print("Accuracy report saved in reports/accuracy_report.csv")
    print("Calibration report saved in reports/calibration_report.csv")
    print(f"Latest scanner matches saved in {LATEST_SCANNER_MATCHES_PATH}")
    print(f"Latest scanner matches rows: {len(latest_matches)}")
    print(f"Latest scanner summary saved in {LATEST_SCANNER_SUMMARY_CSV_PATH}")
    print(f"Latest scanner summary JSON saved in {LATEST_SCANNER_SUMMARY_JSON_PATH}")
    print(f"Latest scanner summary rows: {len(latest_summary)}")


if __name__ == "__main__":
    main()
