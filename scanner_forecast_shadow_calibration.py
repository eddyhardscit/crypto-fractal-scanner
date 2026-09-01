# -*- coding: utf-8 -*-
"""Shadow calibration and frozen-history review for scanner forecast cones.

The official raw cone is never modified here. The shadow cone activates one
horizon at a time only after enough weekly-spaced matured forecasts exist.
"""

from __future__ import annotations

import math
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from forecast_provenance import (
    LEGACY_SHADOW_BASELINE, REPO_ROOT, append_csv_atomic, append_evaluation,
    code_provenance, find_evaluation, freeze_legacy_aggregate_baseline, load_frozen_ohlc,
)


REPORTS_DIR = "reports"
SHADOW_HISTORY_PATH = os.path.join(
    REPORTS_DIR,
    "scanner_forecast_shadow_history.csv",
)
SHADOW_METRICS_PATH = os.path.join(
    REPORTS_DIR,
    "scanner_forecast_shadow_metrics.csv",
)
SHADOW_LATEST_PATH = os.path.join(
    REPORTS_DIR,
    "scanner_forecast_shadow_latest.csv",
)

CALIBRATION_MIN_CONTROLS = 30
CALIBRATION_FULL_CONTROLS = 100
CALIBRATION_MAX_CENTER_SHIFT_LOG = math.log(1.15)
CALIBRATION_MIN_WIDTH_SCALE = 0.75
CALIBRATION_MAX_WIDTH_SCALE = 1.50
KEY_HORIZONS = [1, 3, 7, 14, 30]


def _safe_read_csv(path: str) -> pd.DataFrame:
    if not os.path.exists(path):
        return pd.DataFrame()
    try:
        return pd.read_csv(path)
    except Exception:
        return pd.DataFrame()


def _safe_float(value: Any, default: float = np.nan) -> float:
    try:
        number = float(value)
    except (TypeError, ValueError):
        return default
    return number if math.isfinite(number) else default


def _price_frame(data: dict[str, pd.DataFrame], target: str) -> pd.DataFrame:
    if target not in data or data[target].empty:
        return pd.DataFrame()
    frame = data[target].copy()
    index = pd.DatetimeIndex(frame.index)
    if index.tz is not None:
        index = index.tz_convert(None)
    frame.index = index.normalize()
    frame = frame.sort_index()
    frame = frame[~frame.index.duplicated(keep="last")]
    frame["Close"] = pd.to_numeric(frame["Close"], errors="coerce")
    return frame.dropna(subset=["Close"])


def _close_on_or_after(frame: pd.DataFrame, date_value: Any) -> float:
    if frame.empty:
        return np.nan
    target = pd.to_datetime(date_value, errors="coerce")
    if pd.isna(target):
        return np.nan
    rows = frame[frame.index >= target.normalize()]
    if rows.empty:
        return np.nan
    return _safe_float(rows["Close"].iloc[0])


def _weekly_independent_rows(
    raw_history: pd.DataFrame,
    target: str,
    horizon_day: int,
    prices: pd.DataFrame,
) -> pd.DataFrame:
    if raw_history.empty or prices.empty:
        return pd.DataFrame()

    required = {
        "snapshot_date",
        "target_ticker",
        "target_date",
        "horizon_day",
        "p10_price",
        "p25_price",
        "p50_price",
        "p75_price",
        "p90_price",
    }
    if not required.issubset(raw_history.columns):
        return pd.DataFrame()

    history = raw_history.copy()
    history["snapshot_date_dt"] = pd.to_datetime(
        history["snapshot_date"],
        errors="coerce",
    ).dt.normalize()
    history["target_date_dt"] = pd.to_datetime(
        history["target_date"],
        errors="coerce",
    ).dt.normalize()
    history["horizon_day_num"] = pd.to_numeric(
        history["horizon_day"],
        errors="coerce",
    )
    latest = prices.index.max().normalize()

    subset = history[
        (history["target_ticker"].astype(str) == target)
        & (history["horizon_day_num"] == int(horizon_day))
        & history["snapshot_date_dt"].notna()
        & history["target_date_dt"].notna()
        & (history["target_date_dt"] <= latest)
    ].copy()
    if subset.empty:
        return subset

    subset = subset.sort_values("snapshot_date_dt")
    subset["week_key"] = (
        subset["snapshot_date_dt"]
        .dt.to_period("W-SUN")
        .astype(str)
    )
    # One frozen call per calendar week prevents daily overlapping cones from
    # pretending to be independent calibration observations.
    subset = subset.drop_duplicates(
        subset=["week_key"],
        keep="first",
    )

    rows: list[dict[str, Any]] = []
    for _, row in subset.iterrows():
        actual = _close_on_or_after(
            prices,
            row["target_date_dt"],
        )
        p10 = _safe_float(row.get("p10_price"))
        p25 = _safe_float(row.get("p25_price"))
        p50 = _safe_float(row.get("p50_price"))
        p75 = _safe_float(row.get("p75_price"))
        p90 = _safe_float(row.get("p90_price"))
        values = [actual, p10, p25, p50, p75, p90]
        if (
            not all(math.isfinite(value) for value in values)
            or min(values) <= 0
        ):
            continue
        if not (p10 <= p25 <= p50 <= p75 <= p90):
            continue
        rows.append(
            {
                "snapshot_date": row["snapshot_date_dt"],
                "target_date": row["target_date_dt"],
                "actual_price": actual,
                "p10_price": p10,
                "p25_price": p25,
                "p50_price": p50,
                "p75_price": p75,
                "p90_price": p90,
                "log_error": math.log(actual / p50),
                "wide_half_log": max(
                    1e-9,
                    (
                        abs(math.log(p50 / p10))
                        + abs(math.log(p90 / p50))
                    )
                    / 2.0,
                ),
                "central_half_log": max(
                    1e-9,
                    (
                        abs(math.log(p50 / p25))
                        + abs(math.log(p75 / p50))
                    )
                    / 2.0,
                ),
            }
        )
    return pd.DataFrame(rows)


def _strength(controls: int) -> float:
    if controls < CALIBRATION_MIN_CONTROLS:
        return 0.0
    if controls >= CALIBRATION_FULL_CONTROLS:
        return 1.0
    span = CALIBRATION_FULL_CONTROLS - CALIBRATION_MIN_CONTROLS
    progress = (controls - CALIBRATION_MIN_CONTROLS) / span
    return 0.25 + 0.75 * progress


def _calibration_parameters(samples: pd.DataFrame) -> dict[str, Any]:
    controls = int(len(samples))
    strength = _strength(controls)
    base = {
        "controls": controls,
        "active": strength > 0,
        "strength": strength,
        "center_shift_log": 0.0,
        "center_shift_pct": 0.0,
        "wide_scale": 1.0,
        "central_scale": 1.0,
        "raw_bias_pct": np.nan,
    }
    if controls < CALIBRATION_MIN_CONTROLS:
        return base

    errors = pd.to_numeric(
        samples["log_error"],
        errors="coerce",
    ).dropna()
    if len(errors) < CALIBRATION_MIN_CONTROLS:
        base["controls"] = int(len(errors))
        base["active"] = False
        base["strength"] = 0.0
        return base

    median_error = float(np.median(errors))
    clipped = float(
        np.clip(
            median_error,
            -CALIBRATION_MAX_CENTER_SHIFT_LOG,
            CALIBRATION_MAX_CENTER_SHIFT_LOG,
        )
    )
    center_shift = clipped * strength

    centered_abs = np.abs(errors.to_numpy(dtype=float) - median_error)
    observed_wide = float(np.quantile(centered_abs, 0.80))
    observed_central = float(np.quantile(centered_abs, 0.50))
    predicted_wide = float(
        pd.to_numeric(
            samples["wide_half_log"],
            errors="coerce",
        ).dropna().median()
    )
    predicted_central = float(
        pd.to_numeric(
            samples["central_half_log"],
            errors="coerce",
        ).dropna().median()
    )

    raw_wide_scale = (
        observed_wide / predicted_wide
        if predicted_wide > 0
        else 1.0
    )
    raw_central_scale = (
        observed_central / predicted_central
        if predicted_central > 0
        else 1.0
    )
    raw_wide_scale = float(
        np.clip(
            raw_wide_scale,
            CALIBRATION_MIN_WIDTH_SCALE,
            CALIBRATION_MAX_WIDTH_SCALE,
        )
    )
    raw_central_scale = float(
        np.clip(
            raw_central_scale,
            CALIBRATION_MIN_WIDTH_SCALE,
            CALIBRATION_MAX_WIDTH_SCALE,
        )
    )

    wide_scale = 1.0 + strength * (raw_wide_scale - 1.0)
    central_scale = 1.0 + strength * (raw_central_scale - 1.0)

    base.update(
        {
            "active": True,
            "strength": strength,
            "center_shift_log": center_shift,
            "center_shift_pct": (math.exp(center_shift) - 1.0) * 100.0,
            "wide_scale": wide_scale,
            "central_scale": central_scale,
            "raw_bias_pct": (math.exp(median_error) - 1.0) * 100.0,
        }
    )
    return base


def build_shadow_cone(
    target: str,
    raw_quantiles: pd.DataFrame,
    raw_history: pd.DataFrame,
    data: dict[str, pd.DataFrame],
) -> tuple[pd.DataFrame, list[dict[str, Any]]]:
    if raw_quantiles.empty:
        return pd.DataFrame(), []

    prices = _price_frame(data, target)
    output = raw_quantiles.copy()
    status_by_day: dict[int, dict[str, Any]] = {}

    for column in (
        "p10_price",
        "p25_price",
        "p50_price",
        "p75_price",
        "p90_price",
    ):
        output[f"raw_{column}"] = pd.to_numeric(
            output[column],
            errors="coerce",
        )

    shadow_rows: list[dict[str, Any]] = []
    for _, row in output.iterrows():
        day = int(row["day"])
        samples = _weekly_independent_rows(
            raw_history,
            target,
            day,
            prices,
        )
        params = _calibration_parameters(samples)
        status_by_day[day] = params

        raw_p10 = _safe_float(row["raw_p10_price"])
        raw_p25 = _safe_float(row["raw_p25_price"])
        raw_p50 = _safe_float(row["raw_p50_price"])
        raw_p75 = _safe_float(row["raw_p75_price"])
        raw_p90 = _safe_float(row["raw_p90_price"])

        raw_values = [
            raw_p10,
            raw_p25,
            raw_p50,
            raw_p75,
            raw_p90,
        ]
        if (
            day == 0
            or not params["active"]
            or not all(
                math.isfinite(value)
                for value in raw_values
            )
            or min(raw_values) <= 0
        ):
            shadow_p10 = raw_p10
            shadow_p25 = raw_p25
            shadow_p50 = raw_p50
            shadow_p75 = raw_p75
            shadow_p90 = raw_p90
        else:
            shadow_p50 = raw_p50 * math.exp(
                params["center_shift_log"]
            )
            shadow_p10 = shadow_p50 * math.exp(
                -abs(math.log(raw_p50 / raw_p10))
                * params["wide_scale"]
            )
            shadow_p90 = shadow_p50 * math.exp(
                abs(math.log(raw_p90 / raw_p50))
                * params["wide_scale"]
            )
            shadow_p25 = shadow_p50 * math.exp(
                -abs(math.log(raw_p50 / raw_p25))
                * params["central_scale"]
            )
            shadow_p75 = shadow_p50 * math.exp(
                abs(math.log(raw_p75 / raw_p50))
                * params["central_scale"]
            )

        ordered = sorted(
            [
                shadow_p10,
                shadow_p25,
                shadow_p50,
                shadow_p75,
                shadow_p90,
            ]
        )
        shadow_rows.append(
            {
                **row.to_dict(),
                "shadow_p10_price": ordered[0],
                "shadow_p25_price": ordered[1],
                "shadow_p50_price": ordered[2],
                "shadow_p75_price": ordered[3],
                "shadow_p90_price": ordered[4],
                "calibration_controls": params["controls"],
                "calibration_active": bool(params["active"]),
                "calibration_strength": params["strength"],
                "center_shift_pct": params["center_shift_pct"],
                "raw_bias_pct": params["raw_bias_pct"],
                "wide_scale": params["wide_scale"],
                "central_scale": params["central_scale"],
            }
        )

    shadow = pd.DataFrame(shadow_rows)
    status = []
    for horizon in KEY_HORIZONS:
        params = status_by_day.get(
            horizon,
            {
                "controls": 0,
                "active": False,
                "strength": 0.0,
                "center_shift_pct": 0.0,
                "wide_scale": 1.0,
                "central_scale": 1.0,
            },
        )
        status.append(
            {
                "horizon_day": horizon,
                **params,
                "minimum_controls": CALIBRATION_MIN_CONTROLS,
            }
        )
    return shadow, status


def build_shadow_snapshot_rows(
    target: str,
    shadow_quantiles: pd.DataFrame,
    current_price: float,
    generated_at: str,
) -> list[dict[str, Any]]:
    if shadow_quantiles.empty:
        return []
    snapshot_date = generated_at[:10]
    generated_date = pd.to_datetime(snapshot_date)
    rows: list[dict[str, Any]] = []
    for _, row in shadow_quantiles.iterrows():
        day = int(row["day"])
        rows.append(
            {
                "snapshot_date": snapshot_date,
                "generated_at_utc": generated_at,
                "target_ticker": target,
                "asset": target.replace("-USD", ""),
                "current_price": current_price,
                "horizon_day": day,
                "target_date": (
                    generated_date + pd.Timedelta(days=day)
                ).date().isoformat(),
                "raw_p10_price": row["raw_p10_price"],
                "raw_p25_price": row["raw_p25_price"],
                "raw_p50_price": row["raw_p50_price"],
                "raw_p75_price": row["raw_p75_price"],
                "raw_p90_price": row["raw_p90_price"],
                "shadow_p10_price": row["shadow_p10_price"],
                "shadow_p25_price": row["shadow_p25_price"],
                "shadow_p50_price": row["shadow_p50_price"],
                "shadow_p75_price": row["shadow_p75_price"],
                "shadow_p90_price": row["shadow_p90_price"],
                "calibration_controls": row["calibration_controls"],
                "calibration_active": int(bool(row["calibration_active"])),
                "calibration_strength": row["calibration_strength"],
                "center_shift_pct": row["center_shift_pct"],
                "raw_bias_pct": row["raw_bias_pct"],
                "wide_scale": row["wide_scale"],
                "central_scale": row["central_scale"],
            }
        )
    return rows


def update_shadow_history(new_rows: list[dict[str, Any]]) -> pd.DataFrame:
    new_frame = pd.DataFrame(new_rows)
    old = _safe_read_csv(SHADOW_HISTORY_PATH)
    if new_frame.empty:
        return old
    versions_path = REPO_ROOT / "reports" / "forecast_provenance" / "scanner_shadow_versions.csv"
    append_csv_atomic(versions_path, new_frame)
    history = (
        new_frame.copy()
        if old.empty
        else pd.concat([old, new_frame], ignore_index=True, sort=False)
    )
    keys = ["snapshot_date", "target_ticker", "horizon_day"]
    history = history.drop_duplicates(subset=keys, keep="last")
    history = history.sort_values(keys)
    history.to_csv(SHADOW_HISTORY_PATH, index=False)
    return history


def _finite(value: Any, default: float = 0.0) -> float:
    number = _safe_float(value, default)
    return number if math.isfinite(number) else default


def freeze_shadow_legacy_baseline(metrics_path=SHADOW_METRICS_PATH,
                                  baseline_path=LEGACY_SHADOW_BASELINE):
    published = _safe_read_csv(metrics_path)
    rows = []
    for _, row in published.iterrows():
        controls = int(_finite(row.get("active_out_of_sample_controls")))
        def hits(column):
            return int(round(_finite(row.get(column)) * controls / 100.0))
        rows.append({
            "asset": row.get("asset"), "target_ticker": row.get("target_ticker"),
            "horizon": row.get("horizon"), "horizon_day": int(row.get("horizon_day")),
            "controls": controls,
            "sum_raw_abs_error": _finite(row.get("raw_mae_pct")) * controls,
            "sum_shadow_abs_error": _finite(row.get("shadow_mae_pct")) * controls,
            "shadow_win_hits": hits("shadow_win_rate_pct"),
            "raw_wide_hits": hits("raw_p10_p90_coverage_pct"),
            "shadow_wide_hits": hits("shadow_p10_p90_coverage_pct"),
            "raw_central_hits": hits("raw_p25_p75_coverage_pct"),
            "shadow_central_hits": hits("shadow_p25_p75_coverage_pct"),
            "published_metrics": row.to_dict(),
        })
    return freeze_legacy_aggregate_baseline(
        metrics_path, Path(baseline_path), kind="SCANNER_FORECAST_SHADOW", rows=rows
    )


def combine_shadow_metrics_with_legacy_baseline(metrics, baseline):
    new_by_key = {
        (str(row.get("target_ticker")), int(row.get("horizon_day"))): row
        for _, row in metrics.iterrows()
    } if not metrics.empty else {}
    combined = []
    rate_columns = {
        "shadow_win_rate_pct": "shadow_win_hits",
        "raw_p10_p90_coverage_pct": "raw_wide_hits",
        "shadow_p10_p90_coverage_pct": "shadow_wide_hits",
        "raw_p25_p75_coverage_pct": "raw_central_hits",
        "shadow_p25_p75_coverage_pct": "shadow_central_hits",
    }
    for base in baseline.get("rows", []):
        key = (str(base["target_ticker"]), int(base["horizon_day"]))
        new = new_by_key.pop(key, None)
        new_n = int(new.get("active_out_of_sample_controls", 0)) if new is not None else 0
        if new_n == 0:
            combined.append(dict(base["published_metrics"])); continue
        total = int(base["controls"]) + new_n
        raw_sum = float(base["sum_raw_abs_error"]) + _finite(new.get("raw_mae_pct")) * new_n
        shadow_sum = float(base["sum_shadow_abs_error"]) + _finite(new.get("shadow_mae_pct")) * new_n
        out = {**base["published_metrics"], "active_out_of_sample_controls": total,
               "raw_mae_pct": raw_sum / total, "shadow_mae_pct": shadow_sum / total}
        out["mae_improvement_pct"] = (1 - out["shadow_mae_pct"] / out["raw_mae_pct"]) * 100 if out["raw_mae_pct"] > 0 else np.nan
        for column, hit_field in rate_columns.items():
            hits = int(base[hit_field]) + int(round(_finite(new.get(column)) * new_n / 100.0))
            out[column] = hits / total * 100.0
        combined.append(out)
    combined.extend(row.to_dict() for row in new_by_key.values())
    return pd.DataFrame(combined)


def evaluate_shadow_history(
    shadow_history: pd.DataFrame,
    data: dict[str, pd.DataFrame],
    evaluation_snapshot_ids: dict[str, str] | None = None,
    *, certified_replay: bool = False,
) -> pd.DataFrame:
    if shadow_history.empty:
        return pd.DataFrame()

    history = shadow_history.copy()
    history["target_date_dt"] = pd.to_datetime(
        history["target_date"],
        errors="coerce",
    ).dt.normalize()
    history["horizon_day_num"] = pd.to_numeric(
        history["horizon_day"],
        errors="coerce",
    )
    if "calibration_active" not in history.columns:
        history["calibration_active"] = 0
    history["calibration_active_num"] = pd.to_numeric(
        history["calibration_active"],
        errors="coerce",
    ).fillna(0)

    output: list[dict[str, Any]] = []
    replay_unfrozen = 0
    replay_not_due = 0
    replay_today = pd.Timestamp.now(tz="UTC").tz_localize(None).normalize()
    for target in sorted(history["target_ticker"].dropna().astype(str).unique()):
        for horizon in KEY_HORIZONS:
            rows = history[
                (history["target_ticker"].astype(str) == target)
                & (history["horizon_day_num"] == horizon)
                & history["target_date_dt"].notna()
                & (history["calibration_active_num"] > 0)
            ].copy()

            raw_errors: list[float] = []
            shadow_errors: list[float] = []
            raw_wide: list[bool] = []
            shadow_wide: list[bool] = []
            raw_central: list[bool] = []
            shadow_central: list[bool] = []
            shadow_wins: list[bool] = []

            for _, row in rows.iterrows():
                forecast_id = row.get("forecast_id")
                snapshot_id = (evaluation_snapshot_ids or {}).get(target)
                if pd.isna(forecast_id) or not str(forecast_id).strip():
                    if certified_replay:
                        if row["target_date_dt"] > replay_today:
                            replay_not_due += 1
                        else:
                            replay_unfrozen += 1
                    continue
                existing = find_evaluation(str(forecast_id), int(horizon), row["target_date_dt"].date().isoformat())
                if existing is not None:
                    actual = _safe_float(existing.get("actual_close"))
                    frozen_prices = None
                else:
                    if not snapshot_id:
                        if certified_replay:
                            if row["target_date_dt"] > replay_today:
                                replay_not_due += 1
                            else:
                                replay_unfrozen += 1
                        continue
                    try:
                        frozen_prices = _price_frame({target: load_frozen_ohlc(str(snapshot_id))}, target)
                    except RuntimeError:
                        continue
                    actual = _close_on_or_after(frozen_prices, row["target_date_dt"])
                raw_p50 = _safe_float(row.get("raw_p50_price"))
                shadow_p50 = _safe_float(row.get("shadow_p50_price"))
                raw_p10 = _safe_float(row.get("raw_p10_price"))
                raw_p25 = _safe_float(row.get("raw_p25_price"))
                raw_p75 = _safe_float(row.get("raw_p75_price"))
                raw_p90 = _safe_float(row.get("raw_p90_price"))
                shadow_p10 = _safe_float(row.get("shadow_p10_price"))
                shadow_p25 = _safe_float(row.get("shadow_p25_price"))
                shadow_p75 = _safe_float(row.get("shadow_p75_price"))
                shadow_p90 = _safe_float(row.get("shadow_p90_price"))
                if (
                    not math.isfinite(actual)
                    or min(raw_p50, shadow_p50) <= 0
                ):
                    continue
                raw_error = abs(math.log(actual / raw_p50))
                shadow_error = abs(math.log(actual / shadow_p50))
                raw_errors.append((math.exp(raw_error) - 1.0) * 100.0)
                shadow_errors.append(
                    (math.exp(shadow_error) - 1.0) * 100.0
                )
                shadow_wins.append(shadow_error < raw_error)
                raw_wide.append(raw_p10 <= actual <= raw_p90)
                shadow_wide.append(
                    shadow_p10 <= actual <= shadow_p90
                )
                raw_central.append(raw_p25 <= actual <= raw_p75)
                shadow_central.append(
                    shadow_p25 <= actual <= shadow_p75
                )
                if existing is None:
                    actual_date = frozen_prices.index[frozen_prices.index >= row["target_date_dt"]][0]
                    current = _safe_float(row.get("current_price"))
                    start = pd.to_datetime(row.get("snapshot_date"), errors="coerce")
                    path = frozen_prices.loc[(frozen_prices.index >= start) & (frozen_prices.index <= actual_date), "Close"]
                    append_evaluation({
                        "forecast_id": str(forecast_id), "asset": target,
                        "forecast_generated_at_utc": row.get("generated_at_utc"),
                        "forecast_date": pd.to_datetime(row.get("snapshot_date")).date().isoformat(),
                        "horizon_days": int(horizon),
                        "requested_target_date": row["target_date_dt"].date().isoformat(),
                        "actual_candle_date": pd.Timestamp(actual_date).date().isoformat(),
                        "on_or_after_shift_days": int((pd.Timestamp(actual_date).normalize() - row["target_date_dt"]).days),
                        "actual_close": actual, "raw_market_snapshot_id": snapshot_id,
                        "raw_market_snapshot_sha256": str(snapshot_id).split(":", 1)[-1],
                        "p10": (shadow_p10 / current - 1) * 100,
                        "p25": (shadow_p25 / current - 1) * 100,
                        "p50": (shadow_p50 / current - 1) * 100,
                        "p75": (shadow_p75 / current - 1) * 100,
                        "p90": (shadow_p90 / current - 1) * 100,
                        "inside_p10_p90": shadow_p10 <= actual <= shadow_p90,
                        "inside_p25_p75": shadow_p25 <= actual <= shadow_p75,
                        "direction_forecast": "UP" if shadow_p50 >= current else "DOWN",
                        "direction_result": "UP" if actual >= current else "DOWN",
                        "drawdown": (float(path.min()) / current - 1) * 100,
                        "max_gain": (float(path.max()) / current - 1) * 100,
                        "drawdown_classifications": {
                            "classification_status": "NOT_AVAILABLE",
                            "reason": "SHADOW_FORECAST_HAS_NO_DRAWDOWN_BANDS",
                        },
                        "max_gain_classifications": {
                            "classification_status": "NOT_AVAILABLE",
                            "reason": "SHADOW_FORECAST_HAS_NO_MAX_GAIN_BANDS",
                        },
                        "evaluation_generated_at_utc": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
                        **code_provenance(), "path_price_semantics": "CLOSE_ONLY_LEGACY_COMPATIBLE",
                    })

            controls = len(raw_errors)
            output.append(
                {
                    "asset": target.replace("-USD", ""),
                    "target_ticker": target,
                    "horizon": f"{horizon}g",
                    "horizon_day": horizon,
                    "active_out_of_sample_controls": controls,
                    "raw_mae_pct": (
                        float(np.mean(raw_errors))
                        if raw_errors
                        else np.nan
                    ),
                    "shadow_mae_pct": (
                        float(np.mean(shadow_errors))
                        if shadow_errors
                        else np.nan
                    ),
                    "mae_improvement_pct": (
                        (
                            1.0
                            - float(np.mean(shadow_errors))
                            / float(np.mean(raw_errors))
                        )
                        * 100.0
                        if raw_errors and float(np.mean(raw_errors)) > 0
                        else np.nan
                    ),
                    "shadow_win_rate_pct": (
                        float(np.mean(shadow_wins)) * 100.0
                        if shadow_wins
                        else np.nan
                    ),
                    "raw_p10_p90_coverage_pct": (
                        float(np.mean(raw_wide)) * 100.0
                        if raw_wide
                        else np.nan
                    ),
                    "shadow_p10_p90_coverage_pct": (
                        float(np.mean(shadow_wide)) * 100.0
                        if shadow_wide
                        else np.nan
                    ),
                    "raw_p25_p75_coverage_pct": (
                        float(np.mean(raw_central)) * 100.0
                        if raw_central
                        else np.nan
                    ),
                    "shadow_p25_p75_coverage_pct": (
                        float(np.mean(shadow_central)) * 100.0
                        if shadow_central
                        else np.nan
                    ),
                }
            )
    result = pd.DataFrame(output)
    result.attrs["replay_status"] = (
        "HISTORICAL_RAW_DATA_NOT_FROZEN" if replay_unfrozen
        else "NO_CONTROL_DUE" if replay_not_due else "REPRODUCIBLE"
    )
    result.attrs["legacy_unfrozen_rows"] = replay_unfrozen
    result.attrs["not_due_rows"] = replay_not_due
    return result


def plot_shadow_cone(
    target: str,
    shadow_quantiles: pd.DataFrame,
    generated_date: pd.Timestamp,
) -> str | None:
    if shadow_quantiles.empty:
        return None
    active = shadow_quantiles[
        shadow_quantiles["calibration_active"].astype(bool)
    ]
    if active.empty:
        return None

    short = target.replace("-USD", "")
    output_path = os.path.join(
        REPORTS_DIR,
        f"scanner_forecast_shadow_{short}.png",
    )
    dates = [
        pd.to_datetime(generated_date)
        + pd.Timedelta(days=int(day))
        for day in shadow_quantiles["day"].tolist()
    ]

    figure, axis = plt.subplots(figsize=(12, 6))
    axis.fill_between(
        dates,
        shadow_quantiles["shadow_p10_price"],
        shadow_quantiles["shadow_p90_price"],
        alpha=0.16,
        label="Shadow p10-p90",
    )
    axis.fill_between(
        dates,
        shadow_quantiles["shadow_p25_price"],
        shadow_quantiles["shadow_p75_price"],
        alpha=0.28,
        label="Shadow p25-p75",
    )
    axis.plot(
        dates,
        shadow_quantiles["raw_p50_price"],
        linestyle="--",
        linewidth=1.5,
        label="p50 grezzo",
    )
    axis.plot(
        dates,
        shadow_quantiles["shadow_p50_price"],
        linewidth=2.4,
        label="p50 calibrato shadow",
    )
    axis.set_title(
        f"{short} — calibratore shadow, nessun effetto sul cono ufficiale"
    )
    axis.set_xlabel("Data")
    axis.set_ylabel("Prezzo")
    axis.grid(True, alpha=0.25)
    axis.legend(loc="best")
    figure.autofmt_xdate()
    figure.tight_layout()
    figure.savefig(output_path, dpi=160, bbox_inches="tight")
    plt.close(figure)
    return output_path


def plot_frozen_cone_review(
    target: str,
    raw_history: pd.DataFrame,
    data: dict[str, pd.DataFrame],
    forecast_days: int = 30,
) -> tuple[str | None, dict[str, Any] | None]:
    prices = _price_frame(data, target)
    if raw_history.empty or prices.empty:
        return None, None

    required = {
        "target_ticker",
        "snapshot_date",
        "target_date",
        "horizon_day",
        "p10_price",
        "p25_price",
        "p50_price",
        "p75_price",
        "p90_price",
    }
    if not required.issubset(raw_history.columns):
        return None, None

    history = raw_history[
        raw_history["target_ticker"].astype(str) == target
    ].copy()
    history["snapshot_date_dt"] = pd.to_datetime(
        history["snapshot_date"],
        errors="coerce",
    ).dt.normalize()
    history["target_date_dt"] = pd.to_datetime(
        history["target_date"],
        errors="coerce",
    ).dt.normalize()
    history["horizon_day_num"] = pd.to_numeric(
        history["horizon_day"],
        errors="coerce",
    )
    history = history.dropna(
        subset=[
            "snapshot_date_dt",
            "target_date_dt",
            "horizon_day_num",
        ]
    )
    latest = prices.index.max().normalize()
    snapshots = sorted(
        pd.DatetimeIndex(history["snapshot_date_dt"].unique())
    )
    snapshots = [date for date in snapshots if date < latest]
    if not snapshots:
        return None, None

    complete = [
        date
        for date in snapshots
        if date + pd.Timedelta(days=forecast_days) <= latest
    ]
    selected_date = max(complete) if complete else min(snapshots)
    elapsed = min(
        forecast_days,
        max(0, int((latest - selected_date).days)),
    )
    if elapsed < 1:
        return None, None

    forecast = history[
        (history["snapshot_date_dt"] == selected_date)
        & (history["horizon_day_num"] <= elapsed)
    ].copy()
    forecast = forecast.sort_values("horizon_day_num")
    forecast = forecast.drop_duplicates(
        subset=["horizon_day_num"],
        keep="last",
    )
    if forecast.empty:
        return None, None

    review_rows: list[dict[str, Any]] = []
    for _, row in forecast.iterrows():
        actual = _close_on_or_after(prices, row["target_date_dt"])
        p10 = _safe_float(row.get("p10_price"))
        p25 = _safe_float(row.get("p25_price"))
        p50 = _safe_float(row.get("p50_price"))
        p75 = _safe_float(row.get("p75_price"))
        p90 = _safe_float(row.get("p90_price"))
        values = [actual, p10, p25, p50, p75, p90]
        if (
            not all(math.isfinite(value) for value in values)
            or min(values) <= 0
        ):
            continue
        review_rows.append(
            {
                "date": row["target_date_dt"],
                "actual": actual,
                "p10": p10,
                "p25": p25,
                "p50": p50,
                "p75": p75,
                "p90": p90,
                "discrepancy_pct": (actual / p50 - 1.0) * 100.0,
                "inside_wide": p10 <= actual <= p90,
                "inside_central": p25 <= actual <= p75,
            }
        )
    if not review_rows:
        return None, None

    review = pd.DataFrame(review_rows).sort_values("date")
    short = target.replace("-USD", "")
    output_path = os.path.join(
        REPORTS_DIR,
        f"scanner_forecast_history_{short}.png",
    )

    figure, (price_axis, error_axis) = plt.subplots(
        2,
        1,
        figsize=(12, 8),
        sharex=True,
        gridspec_kw={"height_ratios": [3, 1]},
    )
    price_axis.fill_between(
        review["date"],
        review["p10"],
        review["p90"],
        alpha=0.16,
        label="Banda congelata p10-p90",
    )
    price_axis.fill_between(
        review["date"],
        review["p25"],
        review["p75"],
        alpha=0.28,
        label="Banda congelata p25-p75",
    )
    price_axis.plot(
        review["date"],
        review["p50"],
        linewidth=2.2,
        label="p50 congelato",
    )
    price_axis.plot(
        review["date"],
        review["actual"],
        marker="o",
        linewidth=2.0,
        label=f"{short} reale",
    )
    outside = review[~review["inside_wide"]]
    if not outside.empty:
        price_axis.scatter(
            outside["date"],
            outside["actual"],
            marker="x",
            s=55,
            label="Fuori p10-p90",
        )
    state = (
        "completo 30/30 giorni"
        if elapsed >= forecast_days
        else f"parziale {elapsed}/{forecast_days} giorni"
    )
    price_axis.set_title(
        f"{short} — cono congelato {selected_date.date()} ({state})"
    )
    price_axis.set_ylabel("Prezzo")
    price_axis.grid(True, alpha=0.25)
    price_axis.legend(loc="best")

    error_axis.plot(
        review["date"],
        review["discrepancy_pct"],
        marker="o",
        linewidth=1.8,
        label="Scarto reale vs p50",
    )
    error_axis.axhline(0.0, linestyle="--", linewidth=1.0)
    error_axis.set_xlabel("Data")
    error_axis.set_ylabel("Scarto %")
    error_axis.grid(True, alpha=0.25)
    error_axis.legend(loc="best")
    figure.autofmt_xdate()
    figure.tight_layout()
    figure.savefig(output_path, dpi=160, bbox_inches="tight")
    plt.close(figure)

    latest_row = review.iloc[-1]
    summary = {
        "snapshot_date": selected_date.date().isoformat(),
        "through_date": pd.Timestamp(latest_row["date"]).date().isoformat(),
        "elapsed_days": elapsed,
        "complete": elapsed >= forecast_days,
        "latest_actual_price": float(latest_row["actual"]),
        "latest_p50_price": float(latest_row["p50"]),
        "latest_discrepancy_pct": float(
            latest_row["discrepancy_pct"]
        ),
        "mean_abs_discrepancy_pct": float(
            review["discrepancy_pct"].abs().mean()
        ),
        "max_abs_discrepancy_pct": float(
            review["discrepancy_pct"].abs().max()
        ),
        "inside_p10_p90": bool(latest_row["inside_wide"]),
        "inside_p25_p75": bool(latest_row["inside_central"]),
    }
    return output_path, summary


def current_shadow_status_table(
    latest_rows: list[dict[str, Any]],
) -> pd.DataFrame:
    rows: list[dict[str, Any]] = []
    for item in latest_rows:
        asset = item.get("asset", "n/a")
        for status in item.get("shadow_status", []) or []:
            controls = int(status.get("controls", 0))
            minimum = int(
                status.get(
                    "minimum_controls",
                    CALIBRATION_MIN_CONTROLS,
                )
            )
            active = bool(status.get("active"))
            rows.append(
                {
                    "Asset": asset,
                    "Orizzonte": f"{status.get('horizon_day', 0)}g",
                    "Controlli indipendenti": controls,
                    "Soglia": minimum,
                    "Stato": (
                        "SHADOW ATTIVO"
                        if active
                        else f"RACCOLTA ({max(0, minimum - controls)} mancanti)"
                    ),
                    "Forza correzione": (
                        f"{float(status.get('strength', 0.0)) * 100.0:.1f}%"
                        if active
                        else "0,0%"
                    ),
                    "Shift p50": (
                        f"{float(status.get('center_shift_pct', 0.0)):+.2f}%"
                        if active
                        else "0,00%"
                    ),
                    "Scala p10-p90": (
                        f"{float(status.get('wide_scale', 1.0)):.3f}"
                        if active
                        else "1,000"
                    ),
                }
            )
    return pd.DataFrame(rows)


def shadow_metrics_table(metrics: pd.DataFrame) -> pd.DataFrame:
    columns = [
        "Asset",
        "Orizzonte",
        "Controlli OOS",
        "MAE grezzo",
        "MAE shadow",
        "Miglioramento",
        "Shadow vince",
        "Copertura larga grezza",
        "Copertura larga shadow",
    ]
    if metrics.empty:
        return pd.DataFrame(columns=columns)

    rows: list[dict[str, Any]] = []
    for _, row in metrics.iterrows():
        def pct(value: Any) -> str:
            number = _safe_float(value)
            return (
                "n/a"
                if not math.isfinite(number)
                else f"{number:.2f}%".replace(".", ",")
            )

        rows.append(
            {
                "Asset": row.get("asset", "n/a"),
                "Orizzonte": row.get("horizon", "n/a"),
                "Controlli OOS": int(
                    _safe_float(
                        row.get("active_out_of_sample_controls"),
                        0.0,
                    )
                ),
                "MAE grezzo": pct(row.get("raw_mae_pct")),
                "MAE shadow": pct(row.get("shadow_mae_pct")),
                "Miglioramento": pct(row.get("mae_improvement_pct")),
                "Shadow vince": pct(row.get("shadow_win_rate_pct")),
                "Copertura larga grezza": pct(
                    row.get("raw_p10_p90_coverage_pct")
                ),
                "Copertura larga shadow": pct(
                    row.get("shadow_p10_p90_coverage_pct")
                ),
            }
        )
    return pd.DataFrame(rows, columns=columns)
