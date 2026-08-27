import os
import re
from datetime import datetime, timedelta, timezone

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import yfinance as yf



from shared_market_snapshot import snapshot_price, snapshot_record
from scanner_forecast_shadow_calibration import (
    SHADOW_LATEST_PATH,
    SHADOW_METRICS_PATH,
    build_shadow_cone,
    build_shadow_snapshot_rows,
    current_shadow_status_table,
    evaluate_shadow_history,
    plot_frozen_cone_review,
    plot_shadow_cone,
    shadow_metrics_table,
    update_shadow_history,
)
REPORTS_DIR = "reports"
MAIN_REPORT_PATH = os.path.join(REPORTS_DIR, "latest_report.md")

START_MARKER = "<!-- SCANNER_FORECAST_TRACKER_START -->"
END_MARKER = "<!-- SCANNER_FORECAST_TRACKER_END -->"

HISTORY_PATH = os.path.join(REPORTS_DIR, "scanner_forecast_history.csv")
LATEST_PATH = os.path.join(REPORTS_DIR, "scanner_forecast_latest.csv")
METRICS_PATH = os.path.join(REPORTS_DIR, "scanner_forecast_tracker_metrics.csv")
REPORT_PATH = os.path.join(REPORTS_DIR, "scanner_forecast_tracker_report.md")
REGIME_ADJUSTED_LATEST_PATH = os.path.join(
    REPORTS_DIR,
    "scanner_forecast_regime_adjusted_latest.csv",
)
TAIL_OUTLIER_AUDIT_PATH = os.path.join(
    REPORTS_DIR,
    "scanner_forecast_tail_outlier_audit.csv",
)
TAIL_OUTLIER_REPORT_PATH = os.path.join(
    REPORTS_DIR,
    "scanner_forecast_tail_outlier_audit.md",
)

FULL_MATCHES_PATH = os.path.join(REPORTS_DIR, "latest_scanner_matches.csv")
REGIME_MATCHES_PATH = os.path.join(REPORTS_DIR, "market_regime_match_matches.csv")

TARGETS = {
    "BTC-USD": "BTC",
    "SOL-USD": "SOL",
    "DOGE-USD": "DOGE",
}

FORECAST_DAYS = 30
MATCH_LIMIT = 40
ACCURACY_HORIZONS = [1, 3, 7, 14, 30]


def positive_int_env(name, default):
    try:
        return max(1, int(os.getenv(name, str(default))))
    except (TypeError, ValueError):
        return int(default)


MIN_REGIME_ADJUSTED_MATCHES = positive_int_env(
    "SCANNER_MIN_REGIME_ADJUSTED_MATCHES",
    5,
)


def ensure_reports_dir():
    os.makedirs(REPORTS_DIR, exist_ok=True)


def asset_short(ticker):
    return TARGETS.get(ticker, ticker.replace("-USD", ""))


def asset_name(ticker):
    names = {
        "BTC-USD": "Bitcoin",
        "SOL-USD": "Solana",
        "DOGE-USD": "Dogecoin",
    }
    return names.get(ticker, ticker)


def fmt_number_it(value, decimals=2):
    try:
        if pd.isna(value):
            return "n/a"
        s = f"{float(value):,.{decimals}f}"
        return s.replace(",", "X").replace(".", ",").replace("X", ".")
    except Exception:
        return "n/a"


def fmt_pct(value, decimals=2):
    if pd.isna(value):
        return "n/a"
    return f"{fmt_number_it(value, decimals)}%"


def fmt_price(value, ticker=None):
    if pd.isna(value):
        return "n/a"

    if ticker == "DOGE-USD" or (ticker and "DOGE" in str(ticker)):
        return f"{float(value):.5f} $"

    if abs(float(value)) < 1:
        return f"{float(value):.5f} $"

    return f"{fmt_number_it(value, 2)} $"


def safe_read_csv(path):
    if not os.path.exists(path):
        return pd.DataFrame()

    try:
        return pd.read_csv(path)
    except Exception as e:
        print(f"Errore lettura CSV {path}: {e}")
        return pd.DataFrame()


def df_to_markdown(df):
    if df is None or df.empty:
        return "_Nessun dato._"
    try:
        return df.to_markdown(index=False)
    except ImportError:
        return "```csv\n" + df.to_csv(index=False).rstrip() + "\n```"


def load_matches_for_target(target):
    all_matches = safe_read_csv(FULL_MATCHES_PATH)

    if not all_matches.empty and "target" in all_matches.columns:
        out = all_matches[all_matches["target"].astype(str) == target].copy()
        if not out.empty:
            if "similarity" in out.columns:
                out["similarity"] = pd.to_numeric(out["similarity"], errors="coerce")
                out = out.sort_values("similarity", ascending=False)
            return out.head(MATCH_LIMIT).reset_index(drop=True)

    short = asset_short(target)
    fallback_path = os.path.join(REPORTS_DIR, f"{short}_matches.csv")
    out = safe_read_csv(fallback_path)

    if out.empty:
        return out

    out["target"] = target

    if "similarity" in out.columns:
        out["similarity"] = pd.to_numeric(out["similarity"], errors="coerce")
        out = out.sort_values("similarity", ascending=False)

    return out.head(MATCH_LIMIT).reset_index(drop=True)


def as_bool(value):
    if isinstance(value, (bool, np.bool_)):
        return bool(value)
    if pd.isna(value):
        return False
    return str(value).strip().lower() in {"1", "true", "yes", "y"}


def normalized_match_key(row):
    def norm_date(value):
        dt = pd.to_datetime(value, errors="coerce")
        return "" if pd.isna(dt) else dt.date().isoformat()

    return (
        str(row.get("target", "")).strip(),
        str(row.get("similar_asset", "")).strip(),
        norm_date(row.get("start_date")),
        norm_date(row.get("end_date")),
    )


def select_regime_adjusted_matches(
    raw_matches,
    regime_matches,
    target,
    min_matches=None,
    expected_snapshot_date=None,
):
    """Select one non-mixed regime cohort using the documented hierarchy."""
    threshold = (
        MIN_REGIME_ADJUSTED_MATCHES
        if min_matches is None
        else max(1, int(min_matches))
    )
    base_status = {
        "status": "UNAVAILABLE_REGIME_DATA",
        "selected_regime_group": "NONE",
        "full_regime_matches": 0,
        "same_asset_regime_matches": 0,
        "same_btc_regime_matches": 0,
        "selected_sample_size": 0,
        "minimum_required": threshold,
        "fallback_level": "NONE",
        "selection_reason": "REGIME_MATCH_FILE_MISSING_OR_INVALID",
        "reason": "REGIME_MATCH_FILE_MISSING_OR_INVALID",
        "matched_raw_rows": 0,
    }

    required = {
        "target",
        "similar_asset",
        "start_date",
        "end_date",
        "same_full_regime_as_today",
        "same_asset_regime_as_today",
        "same_btc_regime_as_today",
    }
    if (
        raw_matches is None
        or raw_matches.empty
        or regime_matches is None
        or regime_matches.empty
        or not required.issubset(regime_matches.columns)
    ):
        return pd.DataFrame(), base_status

    raw = raw_matches.copy()
    if "target" not in raw.columns:
        raw["target"] = target
    raw = raw[raw["target"].astype(str) == str(target)].copy()
    regime = regime_matches[
        regime_matches["target"].astype(str) == str(target)
    ].copy()

    if expected_snapshot_date and "target_regime_snapshot_date" in regime.columns:
        regime_dates = pd.to_datetime(
            regime["target_regime_snapshot_date"],
            errors="coerce",
        ).dropna()
        expected_date = pd.to_datetime(expected_snapshot_date, errors="coerce")
        if (
            not pd.isna(expected_date)
            and (
                regime_dates.empty
                or not (regime_dates.dt.normalize() == expected_date.normalize()).all()
            )
        ):
            status = dict(base_status)
            status["status"] = "STALE_REGIME_DATA"
            status["selection_reason"] = (
                "REGIME_SNAPSHOT_DOES_NOT_MATCH_PRICE_SNAPSHOT"
            )
            status["reason"] = status["selection_reason"]
            return pd.DataFrame(), status

    raw_keys = {normalized_match_key(row) for _, row in raw.iterrows()}
    regime["_match_key"] = [
        normalized_match_key(row) for _, row in regime.iterrows()
    ]
    regime = regime[regime["_match_key"].isin(raw_keys)].copy()
    regime = regime.drop_duplicates(subset=["_match_key"], keep="first")

    if regime.empty:
        status = dict(base_status)
        status["selection_reason"] = "NO_REGIME_ROWS_MATCH_CURRENT_RAW_COHORT"
        status["reason"] = status["selection_reason"]
        return pd.DataFrame(), status

    regime["_same_full"] = regime["same_full_regime_as_today"].apply(as_bool)
    regime["_same_asset"] = regime["same_asset_regime_as_today"].apply(as_bool)
    regime["_same_btc"] = regime["same_btc_regime_as_today"].apply(as_bool)

    full_count = int(regime["_same_full"].sum())
    asset_count = int(regime["_same_asset"].sum())
    btc_count = int(regime["_same_btc"].sum())

    if full_count >= threshold:
        selected_group = "SAME_BTC_AND_ASSET_REGIME"
        selected_mask = regime["_same_full"]
        fallback_level = "0_FULL_REGIME"
        selection_reason = "FULL_REGIME_THRESHOLD_MET"
    elif asset_count >= threshold:
        selected_group = "SAME_ASSET_REGIME"
        selected_mask = regime["_same_asset"]
        fallback_level = "1_SAME_ASSET_FALLBACK"
        selection_reason = "FALLBACK_TO_SAME_ASSET_REGIME"
    elif btc_count >= threshold:
        selected_group = "SAME_BTC_REGIME"
        selected_mask = regime["_same_btc"]
        fallback_level = "2_SAME_BTC_FALLBACK"
        selection_reason = "FALLBACK_TO_SAME_BTC_REGIME"
    else:
        selected_group = "NONE"
        selected_mask = pd.Series(False, index=regime.index)
        fallback_level = "NONE"
        selection_reason = "INSUFFICIENT_REGIME_MATCHES"

    selected = regime[selected_mask].drop(
        columns=["_match_key", "_same_full", "_same_asset", "_same_btc"],
        errors="ignore",
    )
    selected_count = int(len(selected))
    status = {
        "status": (
            "AVAILABLE"
            if selected_group != "NONE"
            else "INSUFFICIENT_REGIME_MATCHES"
        ),
        "selected_regime_group": selected_group,
        "full_regime_matches": full_count,
        "same_asset_regime_matches": asset_count,
        "same_btc_regime_matches": btc_count,
        "selected_sample_size": selected_count,
        "minimum_required": threshold,
        "fallback_level": fallback_level,
        "selection_reason": selection_reason,
        "reason": selection_reason,
        "matched_raw_rows": int(len(regime)),
    }
    if selected_group == "NONE":
        return selected.reset_index(drop=True), status

    if "similarity" in selected.columns:
        selected["similarity"] = pd.to_numeric(
            selected["similarity"],
            errors="coerce",
        )
        selected = selected.sort_values("similarity", ascending=False)
    return selected.reset_index(drop=True), status


def normalize_yfinance_df(raw, ticker):
    if raw is None or raw.empty:
        return pd.DataFrame()

    try:
        if isinstance(raw.columns, pd.MultiIndex):
            if ticker not in raw.columns.get_level_values(0):
                return pd.DataFrame()
            df = raw[ticker].copy()
        else:
            df = raw.copy()

        df = df.dropna(how="all").copy()

        if "Close" not in df.columns:
            return pd.DataFrame()

        df.index = pd.to_datetime(df.index)

        if df.index.tz is not None:
            df.index = df.index.tz_convert(None)

        df = df.sort_index()
        df = df[~df.index.duplicated(keep="last")]

        return df
    except Exception as e:
        print(f"{ticker}: errore normalizzazione dati yfinance: {e}")
        return pd.DataFrame()


def download_price_data(tickers):
    tickers = sorted(set([t for t in tickers if isinstance(t, str) and t.strip()]))

    if not tickers:
        return {}

    print(f"Download prezzi per {len(tickers)} ticker...")

    raw = yf.download(
        tickers,
        period="10y",
        interval="1d",
        auto_adjust=True,
        progress=False,
        group_by="ticker",
        threads=True,
    )

    data = {}

    for ticker in tickers:
        df = normalize_yfinance_df(raw, ticker)

        if not df.empty and len(df) > FORECAST_DAYS + 5:
            data[ticker] = df
            print(f"{ticker}: OK {df.index[0].date()} -> {df.index[-1].date()}")
        else:
            print(f"{ticker}: dati insufficienti")

    return data


def position_on_or_after(df, date_value):
    if df.empty:
        return None

    dt = pd.to_datetime(date_value, errors="coerce")

    if pd.isna(dt):
        return None

    idx = pd.DatetimeIndex(df.index)

    if idx.tz is not None:
        idx = idx.tz_convert(None)

    idx_norm = idx.normalize()
    dt_norm = dt.normalize()

    positions = np.where(idx_norm >= dt_norm)[0]

    if len(positions) == 0:
        return None

    return int(positions[0])


def close_on_or_after(df, date_value):
    pos = position_on_or_after(df, date_value)

    if pos is None:
        return np.nan

    try:
        return float(df["Close"].iloc[pos])
    except Exception:
        return np.nan


# SHARED_SNAPSHOT_PRICE_PATCH_V1
def current_price_for_target(target, data):
    """Usa lo stesso prezzo corrente di tutti gli altri moduli.

    Il close scaricato da Yahoo resta soltanto un fallback. In questo modo il
    cono, i percentili in dollari, il CSV latest e il report sono tutti ancorati
    allo snapshot creato a inizio workflow.
    """
    asset = asset_short(target)
    shared = pd.to_numeric(snapshot_price(asset, np.nan), errors="coerce")
    if not pd.isna(shared) and float(shared) > 0:
        return float(shared)
    if target in data and not data[target].empty:
        return float(data[target]["Close"].iloc[-1])
    return np.nan


def input_snapshot_context(target, matches, data):
    record = snapshot_record(target)
    price_date = pd.to_datetime(
        record.get("candle_date_utc"),
        errors="coerce",
    )
    if pd.isna(price_date) and target in data and not data[target].empty:
        price_date = pd.Timestamp(data[target].index[-1])

    generated_values = pd.Series(dtype="datetime64[ns]")
    timestamp_source = matches
    if (
        timestamp_source is None
        or timestamp_source.empty
        or "generated_at_utc" not in timestamp_source.columns
    ):
        full_matches = safe_read_csv(FULL_MATCHES_PATH)
        if "target_ticker" in full_matches.columns:
            timestamp_source = full_matches[
                full_matches["target_ticker"].astype(str) == str(target)
            ]
    if (
        timestamp_source is not None
        and not timestamp_source.empty
        and "generated_at_utc" in timestamp_source.columns
    ):
        generated_values = pd.to_datetime(
            timestamp_source["generated_at_utc"],
            errors="coerce",
        ).dropna()

    return {
        "price_snapshot_date": (
            price_date.date().isoformat()
            if not pd.isna(price_date)
            else "UNKNOWN"
        ),
        "price_snapshot_generated_at_utc": record.get("generated_at_utc") or "UNKNOWN",
        "price_snapshot_source": record.get("source") or "download fallback",
        "match_snapshot_generated_at_utc": (
            generated_values.max().strftime("%Y-%m-%d %H:%M:%S")
            if not generated_values.empty
            else "UNKNOWN"
        ),
    }


def build_path_matrix(matches, data):
    rows = []

    if matches.empty:
        return pd.DataFrame()

    required = {"similar_asset", "end_date"}

    if not required.issubset(matches.columns):
        print("Match senza colonne richieste similar_asset/end_date.")
        return pd.DataFrame()

    for _, row in matches.iterrows():
        similar_asset = str(row.get("similar_asset", "")).strip()

        if similar_asset not in data:
            continue

        df = data[similar_asset].copy()
        pos = position_on_or_after(df, row.get("end_date"))

        if pos is None:
            continue

        if pos + FORECAST_DAYS >= len(df):
            continue

        base_price = float(df["Close"].iloc[pos])

        if base_price <= 0 or pd.isna(base_price):
            continue

        future = df["Close"].iloc[pos:pos + FORECAST_DAYS + 1].astype(float)
        pct_path = (future / base_price - 1.0) * 100.0

        if len(pct_path) < FORECAST_DAYS + 1:
            continue

        out = {
            "similar_asset": similar_asset,
            "start_date": row.get("start_date", ""),
            "end_date": row.get("end_date", ""),
            "similarity": pd.to_numeric(row.get("similarity", np.nan), errors="coerce"),
            "return_30d": pd.to_numeric(row.get("return_30d", np.nan), errors="coerce"),
            "regime_alignment": row.get("regime_alignment", "RAW"),
            "btc_regime_at_match": row.get("btc_regime_at_match", ""),
            "similar_asset_regime_at_match": row.get(
                "similar_asset_regime_at_match",
                "",
            ),
        }

        for d in range(FORECAST_DAYS + 1):
            out[f"day_{d}"] = float(pct_path.iloc[d])

        rows.append(out)

    return pd.DataFrame(rows)


def quantile_paths(paths):
    if paths.empty:
        return pd.DataFrame()

    day_cols = [f"day_{d}" for d in range(FORECAST_DAYS + 1)]
    matrix = paths[day_cols].apply(pd.to_numeric, errors="coerce").to_numpy(dtype=float)

    rows = []

    for d in range(FORECAST_DAYS + 1):
        values = matrix[:, d]
        values = values[~np.isnan(values)]

        if len(values) == 0:
            continue

        rows.append({
            "day": d,
            "count": len(values),
            "p10_pct": np.percentile(values, 10),
            "p25_pct": np.percentile(values, 25),
            "p50_pct": np.percentile(values, 50),
            "p75_pct": np.percentile(values, 75),
            "p90_pct": np.percentile(values, 90),
            "mean_pct": np.mean(values),
        })

    return pd.DataFrame(rows)


def add_price_levels(quantiles, current_price):
    q = quantiles.copy()

    for col in ["p10", "p25", "p50", "p75", "p90", "mean"]:
        q[f"{col}_price"] = current_price * (1 + q[f"{col}_pct"] / 100.0)

    return q


def build_tail_outlier_audit(
    target,
    cohort,
    paths,
    cohort_status="AVAILABLE",
    selected_regime_group=None,
    fallback_level=None,
):
    """Explain terminal tail membership and leave-one-out quantile influence.

    This is diagnostic only: flagged rows are never removed from either cone.
    """
    columns = [
        "target_ticker",
        "asset",
        "cohort",
        "cohort_status",
        "selected_regime_group",
        "fallback_level",
        "cases_used",
        "similar_asset",
        "start_date",
        "end_date",
        "similarity",
        "regime_alignment",
        "return_30d_pct",
        "tail_side",
        "iqr_outlier",
        "is_tail_or_outlier",
        "p10_full_pct",
        "p50_full_pct",
        "p90_full_pct",
        "p10_without_match_pct",
        "p50_without_match_pct",
        "p90_without_match_pct",
        "p10_impact_pct_points",
        "p50_impact_pct_points",
        "p90_impact_pct_points",
        "mean_impact_pct_points",
    ]
    if paths is None or paths.empty or f"day_{FORECAST_DAYS}" not in paths.columns:
        return pd.DataFrame(columns=columns)

    values = pd.to_numeric(paths[f"day_{FORECAST_DAYS}"], errors="coerce")
    valid = paths.loc[values.notna()].copy().reset_index(drop=True)
    values = pd.to_numeric(valid[f"day_{FORECAST_DAYS}"], errors="coerce").to_numpy(dtype=float)
    if len(values) == 0:
        return pd.DataFrame(columns=columns)

    p10, p25, p50, p75, p90 = np.percentile(values, [10, 25, 50, 75, 90])
    iqr = p75 - p25
    lower_fence = p25 - 1.5 * iqr
    upper_fence = p75 + 1.5 * iqr
    full_mean = float(np.mean(values))
    rows = []

    for pos, (_, row) in enumerate(valid.iterrows()):
        value = float(values[pos])
        without = np.delete(values, pos)
        if len(without):
            loo_p10, loo_p50, loo_p90 = np.percentile(without, [10, 50, 90])
            loo_mean = float(np.mean(without))
        else:
            loo_p10 = loo_p50 = loo_p90 = loo_mean = np.nan

        if value >= p90:
            tail_side = "UPPER_P90"
        elif value <= p10:
            tail_side = "LOWER_P10"
        else:
            tail_side = "CENTRAL"
        iqr_outlier = bool(value < lower_fence or value > upper_fence)

        rows.append({
            "target_ticker": target,
            "asset": asset_short(target),
            "cohort": cohort,
            "cohort_status": cohort_status,
            "selected_regime_group": (
                selected_regime_group
                or ("ALL_MATCHES" if cohort == "RAW" else "NONE")
            ),
            "fallback_level": fallback_level or "NONE",
            "cases_used": int(len(values)),
            "similar_asset": row.get("similar_asset", ""),
            "start_date": row.get("start_date", ""),
            "end_date": row.get("end_date", ""),
            "similarity": row.get("similarity", np.nan),
            "regime_alignment": row.get("regime_alignment", "RAW"),
            "return_30d_pct": value,
            "tail_side": tail_side,
            "iqr_outlier": iqr_outlier,
            "is_tail_or_outlier": bool(tail_side != "CENTRAL" or iqr_outlier),
            "p10_full_pct": p10,
            "p50_full_pct": p50,
            "p90_full_pct": p90,
            "p10_without_match_pct": loo_p10,
            "p50_without_match_pct": loo_p50,
            "p90_without_match_pct": loo_p90,
            "p10_impact_pct_points": p10 - loo_p10,
            "p50_impact_pct_points": p50 - loo_p50,
            "p90_impact_pct_points": p90 - loo_p90,
            "mean_impact_pct_points": full_mean - loo_mean,
        })

    return pd.DataFrame(rows, columns=columns)


def direction_from_matches(matches):
    if matches.empty or "return_30d" not in matches.columns:
        return "n/a", np.nan

    returns = pd.to_numeric(matches["return_30d"], errors="coerce").dropna()

    if len(returns) == 0:
        return "n/a", np.nan

    positive = (returns > 0).mean() * 100.0
    negative = 100.0 - positive

    if positive >= 60:
        return "SALITA", positive

    if negative >= 60:
        return "DISCESA", positive

    return "INCERTO", positive


def plot_forecast_cone(target, quantiles_price, current_price, generated_date, data):
    short = asset_short(target)
    out_path = os.path.join(REPORTS_DIR, f"scanner_forecast_{short}.png")

    if quantiles_price.empty:
        return None

    future_dates = [
        generated_date + timedelta(days=int(d))
        for d in quantiles_price["day"].tolist()
    ]

    fig, ax = plt.subplots(figsize=(12, 6))

    ax.fill_between(
        future_dates,
        quantiles_price["p10_price"],
        quantiles_price["p90_price"],
        alpha=0.16,
        label="Banda larga p10-p90",
    )

    ax.fill_between(
        future_dates,
        quantiles_price["p25_price"],
        quantiles_price["p75_price"],
        alpha=0.28,
        label="Banda centrale p25-p75",
    )

    ax.plot(
        future_dates,
        quantiles_price["p50_price"],
        linewidth=2.5,
        marker="o",
        markersize=3,
        label="Scenario centrale p50",
    )

    ax.plot(
        future_dates,
        quantiles_price["p10_price"],
        linestyle="--",
        linewidth=1,
        label="p10",
    )

    ax.plot(
        future_dates,
        quantiles_price["p90_price"],
        linestyle="--",
        linewidth=1,
        label="p90",
    )

    if target in data and not data[target].empty:
        target_df = data[target].copy()
        idx = pd.DatetimeIndex(target_df.index)

        if idx.tz is not None:
            idx = idx.tz_convert(None)

        target_df.index = idx.normalize()

        start = pd.to_datetime(generated_date).normalize()
        end = start + pd.Timedelta(days=FORECAST_DAYS)

        real = target_df[(target_df.index >= start) & (target_df.index <= end)].copy()

        if not real.empty:
            ax.plot(
                real.index,
                real["Close"],
                color="red",
                marker="o",
                linewidth=2,
                label=f"{short} reale",
            )
        else:
            ax.scatter(
                [generated_date],
                [current_price],
                color="red",
                zorder=5,
                label=f"{short} reale oggi",
            )

    ax.set_title(f"{short} — cono previsionale scanner 40 casi")
    ax.set_xlabel("Data")
    ax.set_ylabel("Prezzo")
    ax.grid(True, alpha=0.25)
    ax.legend(loc="best")
    fig.autofmt_xdate()

    plt.tight_layout()
    plt.savefig(out_path, dpi=160)
    plt.close(fig)

    return out_path


def plot_regime_adjusted_cone(
    target,
    raw_quantiles_price,
    adjusted_quantiles_price,
    generated_date,
    selected_regime_group,
    fallback_level,
):
    if adjusted_quantiles_price is None or adjusted_quantiles_price.empty:
        return None

    short = asset_short(target)
    out_path = os.path.join(
        REPORTS_DIR,
        f"scanner_forecast_{short}_regime_adjusted.png",
    )
    future_dates = [
        generated_date + timedelta(days=int(d))
        for d in adjusted_quantiles_price["day"].tolist()
    ]

    fig, ax = plt.subplots(figsize=(12, 6))
    if raw_quantiles_price is not None and not raw_quantiles_price.empty:
        raw_dates = [
            generated_date + timedelta(days=int(d))
            for d in raw_quantiles_price["day"].tolist()
        ]
        ax.fill_between(
            raw_dates,
            raw_quantiles_price["p10_price"],
            raw_quantiles_price["p90_price"],
            color="gray",
            alpha=0.10,
            label="Raw p10-p90",
        )
        ax.plot(
            raw_dates,
            raw_quantiles_price["p50_price"],
            color="gray",
            linestyle="--",
            linewidth=1.5,
            label="Raw p50",
        )

    ax.fill_between(
        future_dates,
        adjusted_quantiles_price["p10_price"],
        adjusted_quantiles_price["p90_price"],
        color="tab:green",
        alpha=0.18,
        label="Regime-adjusted p10-p90",
    )
    ax.fill_between(
        future_dates,
        adjusted_quantiles_price["p25_price"],
        adjusted_quantiles_price["p75_price"],
        color="tab:green",
        alpha=0.30,
        label="Regime-adjusted p25-p75",
    )
    ax.plot(
        future_dates,
        adjusted_quantiles_price["p50_price"],
        color="tab:green",
        linewidth=2.5,
        marker="o",
        markersize=3,
        label="Regime-adjusted p50",
    )
    cases = int(adjusted_quantiles_price["count"].min())
    ax.set_title(
        f"{short} — cono regime-adjusted ({cases} casi)\n"
        f"{selected_regime_group} | {fallback_level}"
    )
    ax.set_xlabel("Data")
    ax.set_ylabel("Prezzo")
    ax.grid(True, alpha=0.25)
    ax.legend(loc="best")
    fig.autofmt_xdate()
    plt.tight_layout()
    plt.savefig(out_path, dpi=160)
    plt.close(fig)
    return out_path


def build_snapshot_rows(
    target,
    quantiles_price,
    current_price,
    generated_at,
    snapshot_date=None,
):
    rows = []
    snapshot_date = snapshot_date or generated_at[:10]
    generated_date = pd.to_datetime(snapshot_date)

    for _, row in quantiles_price.iterrows():
        day = int(row["day"])
        target_date = generated_date + pd.Timedelta(days=day)

        rows.append({
            "snapshot_date": snapshot_date,
            "generated_at_utc": generated_at,
            "target_ticker": target,
            "asset": asset_short(target),
            "current_price": current_price,
            "horizon_day": day,
            "target_date": target_date.date().isoformat(),
            "p10_pct": row["p10_pct"],
            "p25_pct": row["p25_pct"],
            "p50_pct": row["p50_pct"],
            "p75_pct": row["p75_pct"],
            "p90_pct": row["p90_pct"],
            "mean_pct": row["mean_pct"],
            "p10_price": row["p10_price"],
            "p25_price": row["p25_price"],
            "p50_price": row["p50_price"],
            "p75_price": row["p75_price"],
            "p90_price": row["p90_price"],
            "mean_price": row["mean_price"],
            "cases_used": row["count"],
        })

    return rows


def update_forecast_history(new_rows):
    new_df = pd.DataFrame(new_rows)

    if new_df.empty:
        return new_df

    old = safe_read_csv(HISTORY_PATH)

    if old.empty:
        history = new_df.copy()
    else:
        history = pd.concat([old, new_df], ignore_index=True, sort=False)

    key_cols = ["snapshot_date", "target_ticker", "horizon_day"]

    if set(key_cols).issubset(history.columns):
        history = history.drop_duplicates(subset=key_cols, keep="last")

    history.to_csv(HISTORY_PATH, index=False)
    return history


def evaluate_forecast_history(history, data):
    if history.empty:
        return pd.DataFrame()

    required = {
        "target_ticker",
        "asset",
        "snapshot_date",
        "target_date",
        "horizon_day",
        "current_price",
        "p10_price",
        "p25_price",
        "p50_price",
        "p75_price",
        "p90_price",
    }

    if not required.issubset(history.columns):
        return pd.DataFrame()

    rows = []

    hist = history.copy()
    hist["horizon_day"] = pd.to_numeric(hist["horizon_day"], errors="coerce")
    hist["target_date_dt"] = pd.to_datetime(hist["target_date"], errors="coerce")
    hist["snapshot_date_dt"] = pd.to_datetime(hist["snapshot_date"], errors="coerce")

    for target in TARGETS:
        if target not in data or data[target].empty:
            continue

        target_df = data[target].copy()
        idx = pd.DatetimeIndex(target_df.index)

        if idx.tz is not None:
            idx = idx.tz_convert(None)

        target_df.index = idx.normalize()
        last_available_date = target_df.index.max().normalize()

        for horizon in ACCURACY_HORIZONS:
            hrows = hist[
                (hist["target_ticker"].astype(str) == target) &
                (hist["horizon_day"] == horizon) &
                (hist["target_date_dt"].notna()) &
                (hist["target_date_dt"].dt.normalize() <= last_available_date)
            ].copy()

            inside_p10_p90 = []
            inside_p25_p75 = []
            abs_errors = []
            signed_errors = []

            for _, row in hrows.iterrows():
                actual_price = close_on_or_after(target_df, row["target_date_dt"])

                if pd.isna(actual_price):
                    continue

                current_price = pd.to_numeric(row.get("current_price"), errors="coerce")
                p10 = pd.to_numeric(row.get("p10_price"), errors="coerce")
                p25 = pd.to_numeric(row.get("p25_price"), errors="coerce")
                p50 = pd.to_numeric(row.get("p50_price"), errors="coerce")
                p75 = pd.to_numeric(row.get("p75_price"), errors="coerce")
                p90 = pd.to_numeric(row.get("p90_price"), errors="coerce")

                if pd.isna(current_price) or current_price <= 0:
                    continue

                if not pd.isna(p10) and not pd.isna(p90):
                    inside_p10_p90.append(p10 <= actual_price <= p90)

                if not pd.isna(p25) and not pd.isna(p75):
                    inside_p25_p75.append(p25 <= actual_price <= p75)

                if not pd.isna(p50):
                    signed_error = (actual_price - p50) / current_price * 100.0
                    signed_errors.append(signed_error)
                    abs_errors.append(abs(signed_error))

            count = len(abs_errors)

            rows.append({
                "asset": asset_short(target),
                "target_ticker": target,
                "horizon": f"{horizon}g",
                "horizon_day": horizon,
                "controls": count,
                "inside_p10_p90_pct": np.mean(inside_p10_p90) * 100.0 if inside_p10_p90 else np.nan,
                "inside_p25_p75_pct": np.mean(inside_p25_p75) * 100.0 if inside_p25_p75 else np.nan,
                "avg_abs_error_vs_p50_pct": np.mean(abs_errors) if abs_errors else np.nan,
                "avg_error_vs_p50_pct": np.mean(signed_errors) if signed_errors else np.nan,
            })

    return pd.DataFrame(rows)


def format_latest_table(latest_rows):
    out = []

    for row in latest_rows:
        target = row["target_ticker"]
        q30 = row["q30"]

        if q30 is None:
            out.append({
                "Asset": row["asset"],
                "Data": row["snapshot_date"],
                "Prezzo iniziale": fmt_price(row["current_price"], target),
                "Direzione scanner": row["direction"],
                "Casi positivi": fmt_pct(row["positive_cases"]),
                "P10 30g": "n/a",
                "P25 30g": "n/a",
                "P50 30g": "n/a",
                "P75 30g": "n/a",
                "P90 30g": "n/a",
            })
            continue

        out.append({
            "Asset": row["asset"],
            "Data": row["snapshot_date"],
            "Prezzo iniziale": fmt_price(row["current_price"], target),
            "Direzione scanner": row["direction"],
            "Casi positivi": fmt_pct(row["positive_cases"]),
            "P10 30g": fmt_price(q30["p10_price"], target),
            "P25 30g": fmt_price(q30["p25_price"], target),
            "P50 30g": fmt_price(q30["p50_price"], target),
            "P75 30g": fmt_price(q30["p75_price"], target),
            "P90 30g": fmt_price(q30["p90_price"], target),
        })

    return pd.DataFrame(out)


def format_accuracy_table(metrics):
    rows = []

    if metrics.empty:
        for target in TARGETS:
            for horizon in ACCURACY_HORIZONS:
                rows.append({
                    "Asset": asset_short(target),
                    "Giorno": f"{horizon}g",
                    "Controlli": 0,
                    "Dentro p10-p90": "n/a",
                    "Dentro p25-p75": "n/a",
                    "Errore medio abs vs p50": "n/a",
                    "Errore medio vs p50": "n/a",
                })
        return pd.DataFrame(rows)

    for _, row in metrics.iterrows():
        rows.append({
            "Asset": row["asset"],
            "Giorno": row["horizon"],
            "Controlli": int(row["controls"]) if not pd.isna(row["controls"]) else 0,
            "Dentro p10-p90": fmt_pct(row["inside_p10_p90_pct"]),
            "Dentro p25-p75": fmt_pct(row["inside_p25_p75_pct"]),
            "Errore medio abs vs p50": fmt_pct(row["avg_abs_error_vs_p50_pct"]),
            "Errore medio vs p50": fmt_pct(row["avg_error_vs_p50_pct"]),
        })

    return pd.DataFrame(rows)


def format_regime_adjusted_table(latest_rows):
    rows = []
    for row in latest_rows:
        raw_q30 = row.get("q30")
        adjusted_q30 = row.get("regime_adjusted_q30")
        status = row.get("regime_adjusted_status") or {}
        target = row["target_ticker"]
        rows.append({
            "Asset": row["asset"],
            "Stato adjusted": status.get("status", "UNAVAILABLE_REGIME_DATA"),
            "selected_regime_group": status.get("selected_regime_group", "NONE"),
            "full_regime_matches": status.get("full_regime_matches", 0),
            "same_asset_regime_matches": status.get(
                "same_asset_regime_matches",
                0,
            ),
            "same_btc_regime_matches": status.get("same_btc_regime_matches", 0),
            "selected_sample_size": status.get("selected_sample_size", 0),
            "minimum_required": status.get(
                "minimum_required",
                MIN_REGIME_ADJUSTED_MATCHES,
            ),
            "fallback_level": status.get("fallback_level", "NONE"),
            "selection_reason": status.get("selection_reason", status.get("reason", "")),
            "Raw p50 30g": (
                fmt_price(raw_q30.get("p50_price"), target)
                if raw_q30 is not None
                else "n/a"
            ),
            "Adjusted p50 30g": (
                fmt_price(adjusted_q30.get("p50_price"), target)
                if adjusted_q30 is not None
                else "n/a"
            ),
            "Raw p90 30g": (
                fmt_price(raw_q30.get("p90_price"), target)
                if raw_q30 is not None
                else "n/a"
            ),
            "Adjusted p90 30g": (
                fmt_price(adjusted_q30.get("p90_price"), target)
                if adjusted_q30 is not None
                else "n/a"
            ),
        })
    return pd.DataFrame(rows)


def build_regime_adjusted_latest_frame(latest_rows):
    rows = []
    for row in latest_rows:
        status = row.get("regime_adjusted_status") or {}
        context = row.get("input_snapshot") or {}
        q30 = row.get("regime_adjusted_q30")
        out = {
            "snapshot_date": row.get("snapshot_date"),
            "asset": row.get("asset"),
            "target_ticker": row.get("target_ticker"),
            "current_price": row.get("current_price"),
            "price_snapshot_generated_at_utc": context.get(
                "price_snapshot_generated_at_utc"
            ),
            "match_snapshot_generated_at_utc": context.get(
                "match_snapshot_generated_at_utc"
            ),
            "status": status.get("status"),
            "reason": status.get("reason"),
            "selected_regime_group": status.get("selected_regime_group", "NONE"),
            "full_regime_matches": status.get("full_regime_matches", 0),
            "same_asset_regime_matches": status.get(
                "same_asset_regime_matches",
                0,
            ),
            "same_btc_regime_matches": status.get("same_btc_regime_matches", 0),
            "selected_sample_size": status.get("selected_sample_size", 0),
            "usable_paths": status.get("usable_paths", 0),
            "minimum_required": status.get(
                "minimum_required",
                MIN_REGIME_ADJUSTED_MATCHES,
            ),
            "fallback_level": status.get("fallback_level", "NONE"),
            "selection_reason": status.get(
                "selection_reason",
                status.get("reason"),
            ),
            "chart_filename": row.get("regime_adjusted_chart_filename"),
        }
        if q30 is not None:
            for percentile in ["p10", "p25", "p50", "p75", "p90"]:
                out[f"{percentile}_30d_price"] = q30[f"{percentile}_price"]
                out[f"{percentile}_30d_pct"] = q30[f"{percentile}_pct"]
        rows.append(out)
    return pd.DataFrame(rows)


def build_tail_outlier_report(generated_at, latest_rows, audit):
    lines = [
        "# Scanner forecast tail / outlier audit",
        "",
        f"Generato: {generated_at} UTC",
        "",
        (
            "Audit diagnostico dei percorsi a 30 giorni. I casi in coda o "
            "outlier non vengono rimossi dal cono: l'impatto leave-one-out "
            "mostra soltanto quanto ciascun analogo muove p10, p50, p90 e media."
        ),
        "",
        "## Disponibilità coorti",
        "",
        df_to_markdown(format_regime_adjusted_table(latest_rows)),
        "",
    ]
    for row in latest_rows:
        status = row.get("regime_adjusted_status") or {}
        if status.get("fallback_level") in {
            "1_SAME_ASSET_FALLBACK",
            "2_SAME_BTC_FALLBACK",
        }:
            lines.extend([
                f"- WARNING {row['asset']}: {status.get('selected_regime_group')} "
                "is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.",
                "",
            ])

    for row in latest_rows:
        asset = row["asset"]
        lines.extend([f"## {asset}", ""])
        if audit is None or audit.empty:
            lines.extend(["Nessun percorso auditabile.", ""])
            continue

        target_rows = audit[audit["asset"].astype(str) == asset].copy()
        notable = target_rows[target_rows["is_tail_or_outlier"].apply(as_bool)].copy()
        if notable.empty:
            lines.extend(["Nessun caso di coda/outlier disponibile.", ""])
            continue

        notable["_influence"] = notable[
            [
                "p10_impact_pct_points",
                "p50_impact_pct_points",
                "p90_impact_pct_points",
                "mean_impact_pct_points",
            ]
        ].abs().max(axis=1)
        notable = notable.sort_values(
            ["cohort", "_influence"],
            ascending=[True, False],
        ).head(16)
        display = notable[
            [
                "cohort",
                "cohort_status",
                "selected_regime_group",
                "fallback_level",
                "similar_asset",
                "start_date",
                "end_date",
                "return_30d_pct",
                "tail_side",
                "iqr_outlier",
                "p10_impact_pct_points",
                "p50_impact_pct_points",
                "p90_impact_pct_points",
                "mean_impact_pct_points",
            ]
        ].copy()
        for col in [
            "return_30d_pct",
            "p10_impact_pct_points",
            "p50_impact_pct_points",
            "p90_impact_pct_points",
            "mean_impact_pct_points",
        ]:
            display[col] = display[col].apply(fmt_pct)
        lines.extend([df_to_markdown(display), ""])

    return "\n".join(lines).rstrip() + "\n"


def build_report(generated_at, latest_rows, metrics, shadow_metrics):
    lines = []

    lines.append(START_MARKER)
    lines.append("# Scanner forecast path / cono probabilistico")
    lines.append("")
    lines.append(f"Generato: {generated_at} UTC")
    lines.append("")
    lines.append("## Snapshot effettivamente usato")
    lines.append("")
    snapshot_rows = []
    for row in latest_rows:
        context = row.get("input_snapshot") or {}
        snapshot_rows.append({
            "Asset": row["asset"],
            "Snapshot prezzo": context.get("price_snapshot_date", "UNKNOWN"),
            "Generazione snapshot prezzo": context.get(
                "price_snapshot_generated_at_utc",
                "UNKNOWN",
            ),
            "Snapshot match scanner": context.get(
                "match_snapshot_generated_at_utc",
                "UNKNOWN",
            ),
        })
    lines.append(df_to_markdown(pd.DataFrame(snapshot_rows)))
    lines.append("")
    lines.append(
        "La data di generazione del report non sostituisce la data degli input: "
        "se gli snapshot locali sono più vecchi, i valori restano riferiti agli "
        "snapshot indicati in tabella."
    )
    lines.append("")
    lines.append(
        "Questo report trasforma i 40 casi simili dello scanner in un cono previsionale leggibile."
    )
    lines.append("")
    lines.append("Per ogni asset crea:")
    lines.append("")
    lines.append("- banda larga p10-p90")
    lines.append("- banda centrale p25-p75")
    lines.append("- scenario centrale p50")
    lines.append("- prezzo reale sovrapposto quando sono disponibili dati successivi")
    lines.append("")
    lines.append(
        "Correzione importante: il cono ora viene calcolato dai percorsi reali dei match storici, "
        "non solo dai percentili finali a 30 giorni. Quindi il grafico non deve più mostrare solo due puntini."
    )
    lines.append("")

    latest_table = format_latest_table(latest_rows)

    lines.append("## Ultimo cono previsionale salvato")
    lines.append("")

    if latest_table.empty:
        lines.append("Nessun cono disponibile.")
    else:
        lines.append(df_to_markdown(latest_table))

    lines.append("")
    lines.append("## Confronto raw / regime-adjusted")
    lines.append("")
    lines.append(
        "Il cono raw continua a usare i 40 casi dello scanner. Il cono "
        "regime-adjusted sceglie una sola coorte nella gerarchia "
        "SAME_BTC_AND_ASSET_REGIME → SAME_ASSET_REGIME → SAME_BTC_REGIME. "
        f"Ogni livello richiede almeno {MIN_REGIME_ADJUSTED_MATCHES} match; "
        "le coorti non vengono mai combinate e ogni fallback è dichiarato."
    )
    lines.append("")
    lines.append(df_to_markdown(format_regime_adjusted_table(latest_rows)))

    lines.append("")
    lines.append("## Grafici")
    lines.append("")

    for row in latest_rows:
        asset = row["asset"]
        img = row.get("chart_filename")

        lines.append(f"### {asset}")
        lines.append("")

        if img:
            lines.append(f"![Scanner forecast {asset}]({img})")
        else:
            lines.append("Grafico non disponibile: dati insufficienti.")

        historical_img = row.get("historical_chart_filename")
        historical = row.get("historical_review") or {}
        if historical_img:
            lines.append("")
            lines.append("#### Verifica storica e discrepanza")
            lines.append("")
            lines.append(
                f"![Verifica storica cono {asset}]({historical_img})"
            )
            state = (
                "COMPLETO 30/30g"
                if historical.get("complete")
                else (
                    f"PARZIALE {historical.get('elapsed_days', 0)}/"
                    f"{FORECAST_DAYS}g"
                )
            )
            wide_state = (
                "DENTRO p10-p90"
                if historical.get("inside_p10_p90")
                else "FUORI p10-p90"
            )
            central_state = (
                "DENTRO p25-p75"
                if historical.get("inside_p25_p75")
                else "FUORI p25-p75"
            )
            lines.append("")
            lines.append(
                f"- Cono congelato il "
                f"**{historical.get('snapshot_date', 'n/a')}**; "
                f"verificato fino al "
                f"**{historical.get('through_date', 'n/a')}**; "
                f"stato **{state}**."
            )
            lines.append(
                f"- Reale "
                f"**{fmt_price(historical.get('latest_actual_price'), row.get('target_ticker'))}**; "
                f"p50 previsto "
                f"**{fmt_price(historical.get('latest_p50_price'), row.get('target_ticker'))}**; "
                f"scarto "
                f"**{fmt_pct(historical.get('latest_discrepancy_pct'))}**."
            )
            lines.append(
                f"- Errore medio assoluto "
                f"**{fmt_pct(historical.get('mean_abs_discrepancy_pct'))}**; "
                f"massimo "
                f"**{fmt_pct(historical.get('max_abs_discrepancy_pct'))}**; "
                f"{wide_state}; {central_state}."
            )

        shadow_img = row.get("shadow_chart_filename")
        if shadow_img:
            lines.append("")
            lines.append("#### Cono calibrato shadow")
            lines.append("")
            lines.append(
                f"![Cono calibrato shadow {asset}]({shadow_img})"
            )

        adjusted_img = row.get("regime_adjusted_chart_filename")
        adjusted_status = row.get("regime_adjusted_status") or {}
        lines.append("")
        lines.append("#### Cono regime-adjusted")
        lines.append("")
        lines.append(
            f"Gruppo selezionato: **{adjusted_status.get('selected_regime_group', 'NONE')}**; "
            f"fallback: **{adjusted_status.get('fallback_level', 'NONE')}**; "
            f"motivo: **{adjusted_status.get('selection_reason', adjusted_status.get('reason', 'UNKNOWN'))}**."
        )
        lines.append("")
        if adjusted_status.get("fallback_level") in {
            "1_SAME_ASSET_FALLBACK",
            "2_SAME_BTC_FALLBACK",
        }:
            lines.append(
                "**WARNING:** coorte fallback meno stringente rispetto a "
                "SAME_BTC_AND_ASSET_REGIME."
            )
            lines.append("")
        if adjusted_img:
            lines.append(
                f"![Scanner forecast regime-adjusted {asset}]({adjusted_img})"
            )
        else:
            lines.append(
                "Non disponibile: "
                f"{adjusted_status.get('selection_reason', adjusted_status.get('reason', 'REGIME_DATA_UNAVAILABLE'))} "
                f"(campione selezionato {adjusted_status.get('selected_sample_size', 0)}/"
                f"{adjusted_status.get('minimum_required', MIN_REGIME_ADJUSTED_MATCHES)} match)."
            )

        lines.append("")

    lines.append("## Accuratezza percorso scanner")
    lines.append("")

    accuracy_table = format_accuracy_table(metrics)
    lines.append(df_to_markdown(accuracy_table))
    lines.append("")

    lines.append("## Tail / outlier audit")
    lines.append("")
    lines.append(
        "I casi di coda restano nel calcolo. L'audit leave-one-out quantifica "
        "la sensibilità dei percentili senza trasformare l'analisi in un filtro discrezionale."
    )
    lines.append("")
    lines.append(
        "Dettaglio completo: "
        "[scanner_forecast_tail_outlier_audit.md]"
        "(scanner_forecast_tail_outlier_audit.md)."
    )
    lines.append("")

    lines.append("## Calibratore shadow")
    lines.append("")
    lines.append(
        "Il cono ufficiale resta grezzo e invariato. Il calibratore usa "
        "soltanto previsioni passate già mature, campionate una volta a "
        "settimana per ridurre la falsa indipendenza. Ogni orizzonte si "
        "attiva a 30 controlli indipendenti: parte al 25% della correzione "
        "stimata e cresce gradualmente fino al 100% a 100 controlli."
    )
    lines.append("")
    shadow_status_table = current_shadow_status_table(latest_rows)
    if shadow_status_table.empty:
        lines.append("Nessuno stato shadow disponibile.")
    else:
        lines.append(shadow_status_table.to_markdown(index=False))
    lines.append("")
    lines.append("### Confronto fuori campione: grezzo vs shadow")
    lines.append("")
    shadow_table = shadow_metrics_table(shadow_metrics)
    if shadow_table.empty:
        lines.append(
            "Nessun controllo fuori campione con calibratore attivo: "
            "la raccolta è ancora in corso."
        )
    else:
        lines.append(shadow_table.to_markdown(index=False))
    lines.append("")

    lines.append("## Come leggerlo")
    lines.append("")
    lines.append(
        "- Se il prezzo resta dentro p10-p90, lo scanner sta ancora descrivendo bene il range largo."
    )
    lines.append(
        "- Se il prezzo resta dentro p25-p75, lo scanner sta descrivendo bene anche il range centrale."
    )
    lines.append(
        "- Se il prezzo segue p50, il percorso reale è vicino allo scenario normale."
    )
    lines.append(
        "- Se il prezzo esce da p10-p90, il modello statistico dei 40 casi sta perdendo aderenza."
    )
    lines.append(
        "- Questo non sostituisce drawdown e max gain: serve soprattutto a vedere il percorso del return previsto."
    )
    lines.append("")
    lines.append(
        "Nota: servono almeno 5 controlli prima di dare un peso minimo al cono. "
        "Sotto 5 controlli resta solo osservazione."
    )
    lines.append(END_MARKER)

    return "\n".join(lines)


def update_marked_block(text, block):
    pattern = re.compile(
        re.escape(START_MARKER) + r".*?" + re.escape(END_MARKER),
        flags=re.DOTALL,
    )

    if pattern.search(text):
        return pattern.sub(block, text)

    preferred_anchors = [
        "<!-- BOUNCE_AFTER_DRAWDOWN_END -->",
        "<!-- DAILY_CHANGE_END -->",
        "<!-- MAJOR_ALT_LIFECYCLE_SQUEEZE_END -->",
    ]

    for anchor in preferred_anchors:
        pos = text.find(anchor)
        if pos != -1:
            insert_pos = pos + len(anchor)
            return text[:insert_pos] + "\n\n" + block + "\n\n" + text[insert_pos:]

    return text.rstrip() + "\n\n" + block + "\n"


def update_latest_report(block):
    if os.path.exists(MAIN_REPORT_PATH):
        with open(MAIN_REPORT_PATH, "r", encoding="utf-8", errors="replace") as f:
            text = f.read()
    else:
        text = ""

    updated = update_marked_block(text, block)

    with open(MAIN_REPORT_PATH, "w", encoding="utf-8") as f:
        f.write(updated)


def main():
    ensure_reports_dir()

    generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    snapshot_date = generated_at[:10]
    generated_date = pd.to_datetime(snapshot_date)

    matches_by_target = {}
    all_tickers = set(TARGETS.keys())

    for target in TARGETS:
        matches = load_matches_for_target(target)
        matches_by_target[target] = matches

        if not matches.empty and "similar_asset" in matches.columns:
            all_tickers.update(matches["similar_asset"].dropna().astype(str).tolist())

    data = download_price_data(all_tickers)
    # SHADOW_CALIBRATION_NO_LEAKAGE_V1
    # Only forecasts already saved before today's run can calibrate today's
    # shadow cone. The official raw cone remains untouched.
    prior_history = safe_read_csv(HISTORY_PATH)
    regime_matches = safe_read_csv(REGIME_MATCHES_PATH)

    latest_rows = []
    snapshot_rows = []
    shadow_snapshot_rows = []
    audit_frames = []

    for target, matches in matches_by_target.items():
        short = asset_short(target)
        print(f"Costruzione cono {short}...")

        current_price = current_price_for_target(target, data)
        input_snapshot = input_snapshot_context(target, matches, data)
        target_snapshot_date = input_snapshot["price_snapshot_date"]
        if target_snapshot_date == "UNKNOWN":
            target_snapshot_date = snapshot_date
        target_generated_date = pd.to_datetime(target_snapshot_date)
        direction, positive_cases = direction_from_matches(matches)

        paths = build_path_matrix(matches, data)
        quant = quantile_paths(paths)

        regime_cohort, regime_status = select_regime_adjusted_matches(
            raw_matches=matches,
            regime_matches=regime_matches,
            target=target,
            expected_snapshot_date=target_snapshot_date,
        )
        regime_paths = build_path_matrix(regime_cohort, data)
        usable_regime_paths = int(len(regime_paths))
        regime_status["usable_paths"] = usable_regime_paths
        if (
            regime_status["status"] == "AVAILABLE"
            and usable_regime_paths < MIN_REGIME_ADJUSTED_MATCHES
        ):
            regime_status["status"] = "INSUFFICIENT_PATHS"
            regime_status["selection_reason"] = (
                "INSUFFICIENT_USABLE_SELECTED_REGIME_PATHS"
            )
            regime_status["reason"] = regime_status["selection_reason"]

        audit_frames.append(
            build_tail_outlier_audit(
                target,
                "RAW",
                paths,
                cohort_status="AVAILABLE" if not paths.empty else "NO_PATHS",
                selected_regime_group="ALL_MATCHES",
                fallback_level="NONE",
            )
        )
        if not regime_paths.empty:
            audit_frames.append(
                build_tail_outlier_audit(
                    target,
                    "REGIME_ADJUSTED",
                    regime_paths,
                    cohort_status=regime_status["status"],
                    selected_regime_group=regime_status[
                        "selected_regime_group"
                    ],
                    fallback_level=regime_status["fallback_level"],
                )
            )

        if quant.empty or pd.isna(current_price):
            latest_rows.append({
                "target_ticker": target,
                "asset": short,
                "snapshot_date": target_snapshot_date,
                "current_price": current_price,
                "direction": direction,
                "positive_cases": positive_cases,
                "q30": None,
                "chart_filename": None,
                "regime_adjusted_q30": None,
                "regime_adjusted_chart_filename": None,
                "regime_adjusted_status": regime_status,
                "input_snapshot": input_snapshot,
            })
            continue

        quant_price = add_price_levels(quant, current_price)

        shadow_quant, shadow_status = build_shadow_cone(
            target=target,
            raw_quantiles=quant_price,
            raw_history=prior_history,
            data=data,
        )
        shadow_chart_path = plot_shadow_cone(
            target=target,
            shadow_quantiles=shadow_quant,
            generated_date=generated_date,
        )
        shadow_chart_filename = (
            os.path.basename(shadow_chart_path)
            if shadow_chart_path
            else None
        )
        regime_quant_price = pd.DataFrame()
        regime_q30 = None
        regime_chart_path = None
        if regime_status["status"] == "AVAILABLE":
            regime_quant = quantile_paths(regime_paths)
            if not regime_quant.empty:
                regime_quant_price = add_price_levels(regime_quant, current_price)
                q30_rows = regime_quant_price[
                    regime_quant_price["day"] == FORECAST_DAYS
                ]
                regime_q30 = (
                    q30_rows.iloc[0].to_dict()
                    if not q30_rows.empty
                    else None
                )
                regime_chart_path = plot_regime_adjusted_cone(
                    target=target,
                    raw_quantiles_price=quant_price,
                    adjusted_quantiles_price=regime_quant_price,
                    generated_date=target_generated_date,
                    selected_regime_group=regime_status[
                        "selected_regime_group"
                    ],
                    fallback_level=regime_status["fallback_level"],
                )

        chart_path = plot_forecast_cone(
            target=target,
            quantiles_price=quant_price,
            current_price=current_price,
            generated_date=target_generated_date,
            data=data,
        )

        chart_filename = os.path.basename(chart_path) if chart_path else None

        q30_rows = quant_price[quant_price["day"] == FORECAST_DAYS]
        q30 = q30_rows.iloc[0].to_dict() if not q30_rows.empty else None

        latest_rows.append({
            "target_ticker": target,
            "asset": short,
            "snapshot_date": target_snapshot_date,
            "current_price": current_price,
            "direction": direction,
            "positive_cases": positive_cases,
            "q30": q30,
            "chart_filename": chart_filename,
            "shadow_chart_filename": shadow_chart_filename,
            "shadow_status": shadow_status,
            "regime_adjusted_q30": regime_q30,
            "regime_adjusted_chart_filename": (
                os.path.basename(regime_chart_path)
                if regime_chart_path
                else None
            ),
            "regime_adjusted_status": regime_status,
            "input_snapshot": input_snapshot,
        })

        asset_snapshot_rows = build_snapshot_rows(
            target=target,
            quantiles_price=quant_price,
            current_price=current_price,
            generated_at=generated_at,
            snapshot_date=target_snapshot_date,
        )
        snapshot_rows.extend(asset_snapshot_rows)
        shadow_snapshot_rows.extend(
            build_shadow_snapshot_rows(
                target=target,
                shadow_quantiles=shadow_quant,
                current_price=current_price,
                generated_at=generated_at,
            )
        )

    latest_df = pd.DataFrame([
        {
            "snapshot_date": r["snapshot_date"],
            "asset": r["asset"],
            "target_ticker": r["target_ticker"],
            "current_price": r["current_price"],
            "direction": r["direction"],
            "positive_cases": r["positive_cases"],
            "chart_filename": r["chart_filename"],
            **({
                "p10_30d_price": r["q30"]["p10_price"],
                "p25_30d_price": r["q30"]["p25_price"],
                "p50_30d_price": r["q30"]["p50_price"],
                "p75_30d_price": r["q30"]["p75_price"],
                "p90_30d_price": r["q30"]["p90_price"],
                "p10_30d_pct": r["q30"]["p10_pct"],
                "p25_30d_pct": r["q30"]["p25_pct"],
                "p50_30d_pct": r["q30"]["p50_pct"],
                "p75_30d_pct": r["q30"]["p75_pct"],
                "p90_30d_pct": r["q30"]["p90_pct"],
            } if r["q30"] is not None else {})
        }
        for r in latest_rows
    ])
    latest_df.to_csv(LATEST_PATH, index=False)

    shadow_latest = current_shadow_status_table(latest_rows)
    shadow_latest.to_csv(SHADOW_LATEST_PATH, index=False)
    adjusted_latest_df = build_regime_adjusted_latest_frame(latest_rows)
    adjusted_latest_df.to_csv(REGIME_ADJUSTED_LATEST_PATH, index=False)

    nonempty_audits = [frame for frame in audit_frames if not frame.empty]
    audit = (
        pd.concat(nonempty_audits, ignore_index=True)
        if nonempty_audits
        else build_tail_outlier_audit("", "RAW", pd.DataFrame())
    )
    audit.to_csv(TAIL_OUTLIER_AUDIT_PATH, index=False)
    tail_report = build_tail_outlier_report(generated_at, latest_rows, audit)
    with open(TAIL_OUTLIER_REPORT_PATH, "w", encoding="utf-8") as f:
        f.write(tail_report)

    history = update_forecast_history(snapshot_rows)

    for row in latest_rows:
        historical_path, historical_review = plot_frozen_cone_review(
            target=row["target_ticker"],
            raw_history=history,
            data=data,
            forecast_days=FORECAST_DAYS,
        )
        row["historical_chart_filename"] = (
            os.path.basename(historical_path)
            if historical_path
            else None
        )
        row["historical_review"] = historical_review

    metrics = evaluate_forecast_history(history, data)
    metrics.to_csv(METRICS_PATH, index=False)

    shadow_history = update_shadow_history(shadow_snapshot_rows)
    shadow_metrics = evaluate_shadow_history(
        shadow_history,
        data,
    )
    shadow_metrics.to_csv(SHADOW_METRICS_PATH, index=False)

    report = build_report(
        generated_at,
        latest_rows,
        metrics,
        shadow_metrics,
    )

    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        f.write(report)

    update_latest_report(report)

    print(report)
    print(f"Report salvato in {REPORT_PATH}")
    print(f"Latest salvato in {LATEST_PATH}")
    print(f"History salvata in {HISTORY_PATH}")
    print(f"Metrics salvate in {METRICS_PATH}")
    print(f"Regime-adjusted latest salvato in {REGIME_ADJUSTED_LATEST_PATH}")
    print(f"Tail/outlier audit salvato in {TAIL_OUTLIER_AUDIT_PATH}")


if __name__ == "__main__":
    main()
