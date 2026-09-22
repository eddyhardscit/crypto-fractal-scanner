from __future__ import annotations

import hashlib
import json
import math
from collections import Counter
from datetime import timedelta
from pathlib import Path

import matplotlib
matplotlib.use("Agg")

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# ---------------------------------------------------------------------
# Method
# ---------------------------------------------------------------------

CONDITION_DOWN_PCT = -5.0
CONDITION_RECOVERY_PCT = 10.0
CONDITION_WINDOW_DAYS = 30

# 60d are retained for path classification.
# The visible comparison remains 30d.
SUCCESSOR_STORE_DAYS = 60
DISPLAY_DAYS = 30

DYNAMIC_CHART = Path(
    "reports/scanner_forecast_SOL_conditional_successor_current.png"
)
DYNAMIC_JSON = Path(
    "reports/sol_conditional_successor_current.json"
)

FROZEN_PATH_CSV = Path(
    "reports/sol_conditional_successor_vintage_20260918.csv"
)
FROZEN_META_JSON = Path(
    "reports/sol_conditional_successor_vintage_20260918.json"
)
FROZEN_CHART = Path(
    "reports/scanner_forecast_SOL_conditional_successor_vintage_20260918.png"
)

BLOCK_START = "<!-- SOL_CONDITIONAL_ANALYSES_START -->"
BLOCK_END = "<!-- SOL_CONDITIONAL_ANALYSES_END -->"


# ---------------------------------------------------------------------
# Original chat vintage
# ---------------------------------------------------------------------

FROZEN_VINTAGE_DATE = "2026-09-18"

# Approximate SOL anchor used in the original chat analysis.
FROZEN_ANCHOR_PRICE = 112.70

FROZEN_COHORT = (
    ("BNB-USD",  "2023-10-13", "2024-01-20"),
    ("HBAR-USD", "2020-11-04", "2021-02-11"),
    ("RUNE-USD", "2020-03-28", "2020-07-05"),
    ("ETH-USD",  "2020-05-11", "2020-08-18"),
    ("ADA-USD",  "2020-09-08", "2020-12-16"),
    ("BCH-USD",  "2019-01-17", "2019-04-26"),
    ("RUNE-USD", "2023-06-01", "2023-09-08"),
    ("HBAR-USD", "2024-09-04", "2024-12-12"),
)

EXPECTED_FROZEN_EPISODES = 8
EXPECTED_FROZEN_ASSETS = 6

# Results recorded in the original analysis.
EXPECTED_MEDIANS = {
    7: -11.51,
    14: 8.85,
    21: 36.80,
    30: 49.55,
}

# Allows small differences from adjusted historical vendor data,
# but rejects a methodologically different reconstruction.
PARITY_TOLERANCE_PP = 5.0


# ---------------------------------------------------------------------
# Utilities
# ---------------------------------------------------------------------

def number(value):
    try:
        value = float(value)
    except (TypeError, ValueError, OverflowError):
        return float("nan")

    return value if math.isfinite(value) else float("nan")


def money(value):
    value = number(value)

    if not math.isfinite(value):
        return "n/a"

    return f"{value:,.2f} $"


def pct(value):
    value = number(value)

    if not math.isfinite(value):
        return "n/a"

    return f"{value:.2f}%"


def position_on_or_after(frame, value):
    if frame is None or frame.empty:
        return None

    target = pd.to_datetime(
        value,
        errors="coerce",
    )

    if pd.isna(target):
        return None

    index = pd.DatetimeIndex(
        frame.index
    )

    if index.tz is not None:
        index = index.tz_convert(None)

    positions = np.where(
        index.normalize()
        >= target.normalize()
    )[0]

    if not len(positions):
        return None

    return int(positions[0])


def first_touch(
    values,
    threshold,
    *,
    at_least,
    start=1,
):
    for pos in range(start, len(values)):
        value = number(values[pos])

        if not math.isfinite(value):
            continue

        if at_least and value >= threshold:
            return pos

        if not at_least and value <= threshold:
            return pos

    return None


def classify_successor(values):
    plus10 = first_touch(
        values,
        10.0,
        at_least=True,
        start=1,
    )

    minus5 = first_touch(
        values,
        -5.0,
        at_least=False,
        start=1,
    )

    minus10 = first_touch(
        values,
        -10.0,
        at_least=False,
        start=1,
    )

    minus15 = first_touch(
        values,
        -15.0,
        at_least=False,
        start=1,
    )

    if (
        plus10 is not None
        and (
            minus5 is None
            or plus10 < minus5
        )
    ):
        return "DIRECT_CONTINUATION"

    if (
        minus5 is not None
        and plus10 is not None
        and (
            minus10 is None
            or plus10 < minus10
        )
    ):
        return "SHALLOW_PULLBACK_THEN_CONTINUATION"

    if (
        minus10 is not None
        and plus10 is not None
        and (
            minus15 is None
            or plus10 < minus15
        )
    ):
        return "DEEP_PULLBACK_THEN_RECOVERY"

    if (
        minus15 is not None
        and (
            plus10 is None
            or minus15 < plus10
        )
    ):
        return "FAILURE"

    return "UNRESOLVED"


# ---------------------------------------------------------------------
# Core: 40 analogues -> strict condition -> N successors
# ---------------------------------------------------------------------

def build_conditioned_paths(
    matches,
    data,
):
    rows = []

    if matches is None or matches.empty:
        return pd.DataFrame()

    required = {
        "similar_asset",
        "end_date",
    }

    if not required.issubset(
        matches.columns
    ):
        return pd.DataFrame()

    for _, match in matches.iterrows():
        asset = str(
            match.get(
                "similar_asset",
                "",
            )
        ).strip()

        if (
            not asset
            or asset not in data
            or data[asset].empty
        ):
            continue

        frame = (
            data[asset]
            .copy()
            .sort_index()
        )

        if "Close" not in frame.columns:
            continue

        close = pd.to_numeric(
            frame["Close"],
            errors="coerce",
        )

        baseline_pos = position_on_or_after(
            frame,
            match.get("end_date"),
        )

        if baseline_pos is None:
            continue

        baseline = number(
            close.iloc[baseline_pos]
        )

        if (
            not math.isfinite(baseline)
            or baseline <= 0
        ):
            continue

        condition = close.iloc[
            baseline_pos:
            baseline_pos
            + CONDITION_WINDOW_DAYS
            + 1
        ]

        if len(condition) < (
            CONDITION_WINDOW_DAYS + 1
        ):
            continue

        condition_pct = (
            condition / baseline - 1.0
        ).to_numpy(dtype=float) * 100.0

        # Strict order:
        # FIRST -5%, THEN +10%.
        down_day = first_touch(
            condition_pct,
            CONDITION_DOWN_PCT,
            at_least=False,
            start=1,
        )

        if down_day is None:
            continue

        recovery_day = first_touch(
            condition_pct,
            CONDITION_RECOVERY_PCT,
            at_least=True,
            start=down_day + 1,
        )

        if recovery_day is None:
            continue

        anchor_pos = (
            baseline_pos
            + recovery_day
        )

        successor = close.iloc[
            anchor_pos:
            anchor_pos
            + SUCCESSOR_STORE_DAYS
            + 1
        ]

        if len(successor) != (
            SUCCESSOR_STORE_DAYS + 1
        ):
            continue

        anchor_close = number(
            successor.iloc[0]
        )

        if (
            not math.isfinite(anchor_close)
            or anchor_close <= 0
        ):
            continue

        successor_pct = (
            successor
            / anchor_close
            - 1.0
        ).to_numpy(dtype=float) * 100.0

        index = pd.DatetimeIndex(
            frame.index
        )

        if index.tz is not None:
            index = index.tz_convert(None)

        row = {
            "similar_asset": asset,
            "episode_start_date": str(
                match.get(
                    "start_date",
                    "",
                )
            ),
            "episode_end_date": str(
                match.get(
                    "end_date",
                    "",
                )
            ),
            "similarity": number(
                match.get("similarity")
            ),
            "baseline_date": (
                index[
                    baseline_pos
                ]
                .date()
                .isoformat()
            ),
            "minus5_hit_date": (
                index[
                    baseline_pos
                    + down_day
                ]
                .date()
                .isoformat()
            ),
            "plus10_anchor_date": (
                index[
                    anchor_pos
                ]
                .date()
                .isoformat()
            ),
            "days_to_minus5": int(
                down_day
            ),
            "days_minus5_to_plus10": int(
                recovery_day
                - down_day
            ),
            "path_class_60d": (
                classify_successor(
                    successor_pct
                )
            ),
        }

        for day in range(
            SUCCESSOR_STORE_DAYS + 1
        ):
            row[
                f"day_{day}"
            ] = float(
                successor_pct[day]
            )

        rows.append(row)

    return pd.DataFrame(rows)


def quantile_frame(
    paths,
    max_day=DISPLAY_DAYS,
):
    if paths is None or paths.empty:
        return pd.DataFrame()

    rows = []

    for day in range(max_day + 1):
        column = f"day_{day}"

        if column not in paths.columns:
            break

        values = pd.to_numeric(
            paths[column],
            errors="coerce",
        ).dropna().to_numpy(
            dtype=float
        )

        if not len(values):
            continue

        q10, q25, q50, q75, q90 = (
            np.percentile(
                values,
                [10, 25, 50, 75, 90],
            )
        )

        rows.append({
            "day": day,
            "count": int(
                len(values)
            ),
            "p10_pct": float(q10),
            "p25_pct": float(q25),
            "p50_pct": float(q50),
            "p75_pct": float(q75),
            "p90_pct": float(q90),
        })

    return pd.DataFrame(rows)


def q30_summary(
    paths,
    anchor_price,
):
    q = quantile_frame(
        paths,
        DISPLAY_DAYS,
    )

    if q.empty:
        return None

    terminal = q[
        q["day"] == DISPLAY_DAYS
    ]

    if terminal.empty:
        return None

    row = terminal.iloc[0]

    out = {
        "count": int(row["count"]),
    }

    for key in (
        "p10",
        "p25",
        "p50",
        "p75",
        "p90",
    ):
        value_pct = float(
            row[
                f"{key}_pct"
            ]
        )

        out[
            f"{key}_pct"
        ] = value_pct

        out[
            f"{key}_price"
        ] = float(
            anchor_price
            * (
                1.0
                + value_pct
                / 100.0
            )
        )

    return out


def class_summary(paths):
    if (
        paths is None
        or paths.empty
    ):
        return {}

    counts = Counter(
        paths[
            "path_class_60d"
        ].astype(str)
    )

    total = len(paths)

    return {
        name: {
            "count": int(count),
            "pct": float(
                100.0
                * count
                / total
            ),
        }
        for name, count
        in counts.items()
    }


def episode_records(paths):
    if (
        paths is None
        or paths.empty
    ):
        return []

    result = []

    for _, row in paths.iterrows():
        result.append({
            "asset": str(
                row["similar_asset"]
            ),
            "episode_start_date": str(
                row["episode_start_date"]
            ),
            "episode_end_date": str(
                row["episode_end_date"]
            ),
            "similarity": number(
                row.get("similarity")
            ),
            "minus5_hit_date": str(
                row["minus5_hit_date"]
            ),
            "plus10_anchor_date": str(
                row[
                    "plus10_anchor_date"
                ]
            ),
            "path_class_60d": str(
                row[
                    "path_class_60d"
                ]
            ),
        })

    return result


# ---------------------------------------------------------------------
# Charting
# ---------------------------------------------------------------------

def anchored_prices(
    percentages,
    anchor_price,
):
    return (
        float(anchor_price)
        * (
            1.0
            + np.asarray(
                percentages,
                dtype=float,
            )
            / 100.0
        )
    )


def render_paths_chart(
    paths,
    anchor_price,
    forecast_date,
    output_path,
    *,
    title,
    subtitle,
    actual_sol=None,
    actual_start_date=None,
):
    if (
        paths is None
        or paths.empty
    ):
        return None

    q = quantile_frame(
        paths,
        DISPLAY_DAYS,
    )

    if q.empty:
        return None

    start = pd.Timestamp(
        forecast_date
    ).normalize()

    dates = [
        start
        + timedelta(
            days=int(day)
        )
        for day in q["day"]
    ]

    fig, ax = plt.subplots(
        figsize=(13.5, 7.4)
    )

    show_episode_labels = (
        len(paths) <= 10
    )

    for _, row in paths.iterrows():
        values = [
            row[f"day_{day}"]
            for day in range(
                DISPLAY_DAYS + 1
            )
        ]

        label = (
            f"{row['similar_asset']} "
            f"({row['plus10_anchor_date']})"
            if show_episode_labels
            else "_nolegend_"
        )

        ax.plot(
            dates,
            anchored_prices(
                values,
                anchor_price,
            ),
            linewidth=0.95,
            alpha=0.30,
            label=label,
        )

    qprices = {}

    for key in (
        "p10",
        "p25",
        "p50",
        "p75",
        "p90",
    ):
        qprices[key] = (
            anchored_prices(
                q[f"{key}_pct"],
                anchor_price,
            )
        )

    ax.fill_between(
        dates,
        qprices["p10"],
        qprices["p90"],
        alpha=0.12,
        label="p10-p90",
    )

    ax.fill_between(
        dates,
        qprices["p25"],
        qprices["p75"],
        alpha=0.22,
        label="p25-p75",
    )

    ax.plot(
        dates,
        qprices["p50"],
        linewidth=3.1,
        marker="o",
        markersize=3.4,
        label="Conditional p50",
        zorder=6,
    )

    ax.plot(
        dates,
        qprices["p10"],
        linestyle="--",
        linewidth=1.0,
        label="p10",
    )

    ax.plot(
        dates,
        qprices["p90"],
        linestyle="--",
        linewidth=1.0,
        label="p90",
    )

    actual_progress = {
        "actual_available": False,
    }

    if (
        actual_sol is not None
        and not actual_sol.empty
        and actual_start_date
    ):
        actual = (
            actual_sol
            .copy()
            .sort_index()
        )

        index = pd.DatetimeIndex(
            actual.index
        )

        if index.tz is not None:
            index = index.tz_convert(None)

        actual.index = (
            index.normalize()
        )

        actual_start = pd.Timestamp(
            actual_start_date
        ).normalize()

        actual_end = (
            actual_start
            + pd.Timedelta(
                days=DISPLAY_DAYS
            )
        )

        actual = actual[
            (actual.index >= actual_start)
            & (
                actual.index
                <= actual_end
            )
        ]

        if not actual.empty:
            ax.plot(
                actual.index,
                actual["Close"],
                linewidth=2.7,
                marker="o",
                markersize=4,
                label="SOL reale",
                zorder=7,
            )

            latest_date = (
                actual.index[-1]
            )

            latest_price = float(
                actual[
                    "Close"
                ].iloc[-1]
            )

            elapsed = int(
                max(
                    0,
                    min(
                        DISPLAY_DAYS,
                        (
                            latest_date
                            - actual_start
                        ).days,
                    ),
                )
            )

            qrow = q[
                q["day"] == elapsed
            ].iloc[0]

            actual_progress = {
                "actual_available": True,
                "latest_actual_date": (
                    latest_date
                    .date()
                    .isoformat()
                ),
                "latest_actual_price": (
                    latest_price
                ),
                "elapsed_days": elapsed,
            }

            for key in (
                "p10",
                "p25",
                "p50",
                "p75",
                "p90",
            ):
                actual_progress[
                    f"{key}_price"
                ] = float(
                    anchored_prices(
                        [
                            qrow[
                                f"{key}_pct"
                            ]
                        ],
                        anchor_price,
                    )[0]
                )

            actual_progress[
                "inside_p10_p90"
            ] = bool(
                actual_progress[
                    "p10_price"
                ]
                <= latest_price
                <= actual_progress[
                    "p90_price"
                ]
            )

            actual_progress[
                "inside_p25_p75"
            ] = bool(
                actual_progress[
                    "p25_price"
                ]
                <= latest_price
                <= actual_progress[
                    "p75_price"
                ]
            )

    ax.scatter(
        [start],
        [anchor_price],
        s=70,
        zorder=8,
        label=(
            f"Anchor ${anchor_price:.2f}"
        ),
    )

    ax.set_title(
        title + "\n" + subtitle,
        loc="left",
        fontsize=14.5,
        fontweight="bold",
    )

    ax.set_xlabel(
        "30 giorni successivi "
        "all'anchor +10%"
    )

    ax.set_ylabel(
        "SOL-equivalent price (USD)"
    )

    ax.grid(
        True,
        alpha=0.22,
    )

    ax.text(
        0.01,
        0.98,
        (
            "DIAGNOSTIC ONLY"
            + (
                " · SMALL SAMPLE"
                if len(paths) < 10
                else ""
            )
        ),
        transform=ax.transAxes,
        va="top",
        fontsize=9.5,
        fontweight="bold",
    )

    ax.legend(
        loc="best",
        fontsize=7.2,
        ncol=2,
    )

    ax.xaxis.set_major_formatter(
        mdates.DateFormatter(
            "%d %b"
        )
    )

    fig.autofmt_xdate()
    fig.tight_layout()

    output_path = Path(
        output_path
    )

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    fig.savefig(
        output_path,
        dpi=160,
        bbox_inches="tight",
        facecolor="white",
    )

    plt.close(fig)

    return {
        "chart_filename": (
            output_path.name
        ),
        "actual_progress": (
            actual_progress
        ),
    }


# ---------------------------------------------------------------------
# Dynamic current analysis
# ---------------------------------------------------------------------

def build_dynamic_analysis(
    matches,
    data,
    current_price,
    forecast_date,
):
    try:
        paths = build_conditioned_paths(
            matches,
            data,
        )

        if paths.empty:
            return {
                "status": (
                    "NO_QUALIFIED_EPISODES"
                ),
                "qualified_episodes": 0,
                "distinct_assets": 0,
                "forecast_date": str(
                    forecast_date
                ),
                "current_price": number(
                    current_price
                ),
            }

        chart = render_paths_chart(
            paths,
            float(current_price),
            forecast_date,
            DYNAMIC_CHART,
            title=(
                "SOL — Conditional Successor corrente"
            ),
            subtitle=(
                f"{len(paths)} episodi qualificati "
                f"su 40 · "
                f"{paths['similar_asset'].nunique()} "
                "asset distinti"
            ),
        )

        result = {
            "status": "AVAILABLE",
            "forecast_date": str(
                forecast_date
            ),
            "current_price": float(
                current_price
            ),
            "qualified_episodes": int(
                len(paths)
            ),
            "distinct_assets": int(
                paths[
                    "similar_asset"
                ].nunique()
            ),
            "small_sample": bool(
                len(paths) < 10
            ),
            "condition": {
                "first": (
                    CONDITION_DOWN_PCT
                ),
                "then": (
                    CONDITION_RECOVERY_PCT
                ),
                "within_days": (
                    CONDITION_WINDOW_DAYS
                ),
            },
            "q30": q30_summary(
                paths,
                float(current_price),
            ),
            "path_classes_60d": (
                class_summary(paths)
            ),
            "episodes": (
                episode_records(paths)
            ),
            "chart_filename": (
                chart[
                    "chart_filename"
                ]
                if chart
                else None
            ),
        }

        DYNAMIC_JSON.write_text(
            json.dumps(
                result,
                indent=2,
                sort_keys=True,
                allow_nan=False,
            ) + "\n",
            encoding="utf-8",
        )

        return result

    except Exception as exc:
        return {
            "status": "UNAVAILABLE",
            "reason": (
                f"{type(exc).__name__}:"
                f"{exc}"
            ),
            "forecast_date": str(
                forecast_date
            ),
        }


# ---------------------------------------------------------------------
# Frozen vintage creation / verification
# ---------------------------------------------------------------------

def sha256_file(path):
    return hashlib.sha256(
        Path(path).read_bytes()
    ).hexdigest()


def build_frozen_paths(data):
    matches = pd.DataFrame([
        {
            "similar_asset": asset,
            "start_date": start,
            "end_date": end,
            "similarity": float(
                100 - index
            ),
        }
        for index, (
            asset,
            start,
            end,
        ) in enumerate(
            FROZEN_COHORT
        )
    ])

    paths = build_conditioned_paths(
        matches,
        data,
    )

    if len(paths) != (
        EXPECTED_FROZEN_EPISODES
    ):
        raise RuntimeError(
            "FROZEN_EPISODE_COUNT_PARITY_FAIL:"
            f"expected={EXPECTED_FROZEN_EPISODES}:"
            f"got={len(paths)}"
        )

    distinct = int(
        paths[
            "similar_asset"
        ].nunique()
    )

    if distinct != (
        EXPECTED_FROZEN_ASSETS
    ):
        raise RuntimeError(
            "FROZEN_ASSET_COUNT_PARITY_FAIL:"
            f"expected={EXPECTED_FROZEN_ASSETS}:"
            f"got={distinct}"
        )

    actual_medians = {}

    for day, expected in (
        EXPECTED_MEDIANS.items()
    ):
        actual = float(
            np.median(
                pd.to_numeric(
                    paths[
                        f"day_{day}"
                    ],
                    errors="coerce",
                )
            )
        )

        actual_medians[
            str(day)
        ] = actual

        if abs(
            actual - expected
        ) > PARITY_TOLERANCE_PP:
            raise RuntimeError(
                "FROZEN_MEDIAN_PARITY_FAIL:"
                f"day={day}:"
                f"expected={expected}:"
                f"got={actual:.4f}"
            )

    return paths, actual_medians


def write_frozen_artifacts(
    paths,
    medians,
):
    FROZEN_PATH_CSV.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    paths.to_csv(
        FROZEN_PATH_CSV,
        index=False,
    )

    q30 = q30_summary(
        paths,
        FROZEN_ANCHOR_PRICE,
    )

    meta = {
        "schema": (
            "SOL_CONDITIONAL_SUCCESSOR_"
            "FROZEN_VINTAGE_V1"
        ),
        "vintage_date": (
            FROZEN_VINTAGE_DATE
        ),
        "anchor_price": (
            FROZEN_ANCHOR_PRICE
        ),
        "anchor_semantics": (
            "approximate_chat_anchor"
        ),
        "qualified_episodes": int(
            len(paths)
        ),
        "distinct_assets": int(
            paths[
                "similar_asset"
            ].nunique()
        ),
        "condition": {
            "first": (
                CONDITION_DOWN_PCT
            ),
            "then": (
                CONDITION_RECOVERY_PCT
            ),
            "within_days": (
                CONDITION_WINDOW_DAYS
            ),
        },
        "stored_successor_days": (
            SUCCESSOR_STORE_DAYS
        ),
        "visible_days": DISPLAY_DAYS,
        "manual_analysis_medians": {
            str(key): value
            for key, value
            in EXPECTED_MEDIANS.items()
        },
        "reproduced_medians": (
            medians
        ),
        "q30": q30,
        "sensitivity_status": (
            "UNSTABLE"
        ),
        "diagnostic_only": True,
        "path_csv": str(
            FROZEN_PATH_CSV
        ),
        "path_csv_sha256": (
            sha256_file(
                FROZEN_PATH_CSV
            )
        ),
        "path_classes_60d": (
            class_summary(paths)
        ),
        "episodes": (
            episode_records(paths)
        ),
    }

    FROZEN_META_JSON.write_text(
        json.dumps(
            meta,
            indent=2,
            sort_keys=True,
            allow_nan=False,
        ) + "\n",
        encoding="utf-8",
    )

    return meta


def load_frozen_artifacts():
    if (
        not FROZEN_PATH_CSV.exists()
        or not FROZEN_META_JSON.exists()
    ):
        raise RuntimeError(
            "FROZEN_VINTAGE_ARTIFACTS_MISSING"
        )

    meta = json.loads(
        FROZEN_META_JSON.read_text(
            encoding="utf-8"
        )
    )

    expected_hash = meta[
        "path_csv_sha256"
    ]

    actual_hash = sha256_file(
        FROZEN_PATH_CSV
    )

    if actual_hash != expected_hash:
        raise RuntimeError(
            "FROZEN_VINTAGE_HASH_MISMATCH"
        )

    paths = pd.read_csv(
        FROZEN_PATH_CSV
    )

    if len(paths) != (
        EXPECTED_FROZEN_EPISODES
    ):
        raise RuntimeError(
            "FROZEN_VINTAGE_COUNT_CHANGED"
        )

    if int(
        paths[
            "similar_asset"
        ].nunique()
    ) != EXPECTED_FROZEN_ASSETS:
        raise RuntimeError(
            "FROZEN_VINTAGE_ASSET_COUNT_CHANGED"
        )

    return paths, meta


def render_frozen_vintage(
    sol_frame,
):
    try:
        paths, meta = (
            load_frozen_artifacts()
        )

        chart = render_paths_chart(
            paths,
            FROZEN_ANCHOR_PRICE,
            FROZEN_VINTAGE_DATE,
            FROZEN_CHART,
            title=(
                "SOL — Conditional Successor "
                "vintage congelato"
            ),
            subtitle=(
                "18 Sep 2026 · "
                "8 episodi / 6 asset"
            ),
            actual_sol=sol_frame,
            actual_start_date=(
                FROZEN_VINTAGE_DATE
            ),
        )

        return {
            "status": "AVAILABLE",
            "meta": meta,
            "q30": meta["q30"],
            "chart_filename": (
                chart[
                    "chart_filename"
                ]
                if chart
                else None
            ),
            "actual_progress": (
                chart[
                    "actual_progress"
                ]
                if chart
                else {
                    "actual_available": False
                }
            ),
        }

    except Exception as exc:
        return {
            "status": "UNAVAILABLE",
            "reason": (
                f"{type(exc).__name__}:"
                f"{exc}"
            ),
        }


# ---------------------------------------------------------------------
# Markdown report
# ---------------------------------------------------------------------

def _target_date(
    forecast_date,
):
    try:
        return (
            pd.Timestamp(
                forecast_date
            )
            + pd.Timedelta(
                days=DISPLAY_DAYS
            )
        ).date().isoformat()
    except Exception:
        return "n/a"


def _table_row(
    label,
    vintage,
    sample,
    target_date,
    q30,
):
    if not q30:
        return (
            f"| {label} | {vintage} | "
            f"{sample} | {target_date} | "
            "n/a | n/a | n/a | n/a | n/a |"
        )

    return (
        f"| {label} | {vintage} | "
        f"{sample} | {target_date} | "
        f"{money(q30.get('p10_price'))} | "
        f"{money(q30.get('p25_price'))} | "
        f"{money(q30.get('p50_price'))} | "
        f"{money(q30.get('p75_price'))} | "
        f"{money(q30.get('p90_price'))} |"
    )


def report_lines(
    dynamic,
    frozen,
    canonical_q30,
    canonical_snapshot_date,
):
    lines = [
        "",
        BLOCK_START,
        "#### SOL — Analisi condizionata -5% → +10%",
        "",
        (
            "Queste analisi sono **separate dal cono SOL originale**. "
            "Il cono sopra continua a usare normalmente i **40 analoghi "
            "più simili a SOL**."
        ),
        "",
        (
            "Il filtro condizionato parte proprio da quei 40 casi e conserva "
            "soltanto gli episodi che hanno toccato **prima -5%** dal proprio "
            "baseline e **successivamente +10% entro 30 giorni**."
        ),
        "",
    ]

    # -------------------------------------------------------------
    # Dynamic
    # -------------------------------------------------------------
    lines.extend([
        "##### A. Conditional Successor corrente — dinamico",
        "",
        (
            "Questo campione viene ricostruito ad ogni run dai **40 analoghi "
            "SOL correnti**. Di conseguenza il numero di episodi qualificati "
            "e gli asset possono cambiare giorno per giorno."
        ),
        "",
    ])

    if (
        not dynamic
        or dynamic.get("status")
        != "AVAILABLE"
    ):
        reason = (
            dynamic.get(
                "reason",
                dynamic.get(
                    "status",
                    "UNAVAILABLE",
                ),
            )
            if dynamic
            else "UNAVAILABLE"
        )

        lines.extend([
            f"Conditional corrente non disponibile: `{reason}`.",
            "",
        ])
    else:
        n = int(
            dynamic[
                "qualified_episodes"
            ]
        )

        assets = int(
            dynamic[
                "distinct_assets"
            ]
        )

        lines.append(
            f"**Campione corrente:** {n} episodi qualificati su 40 · "
            f"{assets} asset distinti."
        )
        lines.append("")

        if dynamic.get("small_sample"):
            lines.extend([
                (
                    "**SMALL SAMPLE / DIAGNOSTIC ONLY:** "
                    "le frequenze empiriche non sono probabilità calibrate."
                ),
                "",
            ])

        lines.extend([
            (
                f"![SOL conditional successor corrente]"
                f"({dynamic['chart_filename']})"
            ),
            "",
            "###### Confronto diretto a 30 giorni",
            "",
            "| Modello | Vintage | N | Target | P10 | P25 | P50 | P75 | P90 |",
            "| --- | --- | ---: | --- | ---: | ---: | ---: | ---: | ---: |",
            _table_row(
                "Cono standard",
                str(
                    canonical_snapshot_date
                ),
                40,
                _target_date(
                    canonical_snapshot_date
                ),
                canonical_q30,
            ),
            _table_row(
                "Conditional corrente",
                str(
                    dynamic[
                        "forecast_date"
                    ]
                ),
                n,
                _target_date(
                    dynamic[
                        "forecast_date"
                    ]
                ),
                dynamic.get("q30"),
            ),
            "",
        ])

        classes = (
            dynamic.get(
                "path_classes_60d"
            )
            or {}
        )

        if classes:
            lines.extend([
                "###### Struttura successiva dei casi correnti",
                "",
                "| Classe | Episodi | Frequenza empirica |",
                "| --- | ---: | ---: |",
            ])

            for name in (
                "DIRECT_CONTINUATION",
                "SHALLOW_PULLBACK_THEN_CONTINUATION",
                "DEEP_PULLBACK_THEN_RECOVERY",
                "FAILURE",
                "UNRESOLVED",
            ):
                item = classes.get(
                    name,
                    {
                        "count": 0,
                        "pct": 0.0,
                    },
                )

                lines.append(
                    f"| {name} | "
                    f"{int(item['count'])} | "
                    f"{pct(item['pct'])} |"
                )

            lines.append("")

        lines.extend([
            "###### Episodi qualificati oggi",
            "",
            "| Asset | Match window | -5% hit | +10% anchor | Classe 60d |",
            "| --- | --- | --- | --- | --- |",
        ])

        for episode in dynamic.get(
            "episodes",
            [],
        ):
            lines.append(
                f"| {episode['asset']} | "
                f"{episode['episode_start_date']} → "
                f"{episode['episode_end_date']} | "
                f"{episode['minus5_hit_date']} | "
                f"{episode['plus10_anchor_date']} | "
                f"{episode['path_class_60d']} |"
            )

        lines.append("")

    # -------------------------------------------------------------
    # Frozen vintage
    # -------------------------------------------------------------
    lines.extend([
        "##### B. Vintage originale 18 settembre — congelato",
        "",
        (
            "Questo invece **non cambia più**. Conserva gli 8 episodi / "
            "6 asset della nostra analisi originale e serve per verificare "
            "fuori campione se quella specifica previsione descrive bene SOL."
        ),
        "",
        (
            f"Anchor della chat: circa **${FROZEN_ANCHOR_PRICE:.2f}** "
            f"il **{FROZEN_VINTAGE_DATE}**."
        ),
        "",
        (
            "**SMALL SAMPLE · SENSITIVITY UNSTABLE · DIAGNOSTIC ONLY.**"
        ),
        "",
    ])

    if (
        not frozen
        or frozen.get("status")
        != "AVAILABLE"
    ):
        reason = (
            frozen.get(
                "reason",
                "UNAVAILABLE",
            )
            if frozen
            else "UNAVAILABLE"
        )

        lines.extend([
            f"Vintage congelato non disponibile: `{reason}`.",
            "",
        ])
    else:
        lines.extend([
            (
                f"![SOL conditional successor vintage]"
                f"({frozen['chart_filename']})"
            ),
            "",
            "###### Percentili congelati a 30 giorni",
            "",
            "| Modello | Vintage | N | Target | P10 | P25 | P50 | P75 | P90 |",
            "| --- | --- | ---: | --- | ---: | ---: | ---: | ---: | ---: |",
            _table_row(
                "Conditional vintage",
                FROZEN_VINTAGE_DATE,
                8,
                _target_date(
                    FROZEN_VINTAGE_DATE
                ),
                frozen.get("q30"),
            ),
            "",
        ])

        progress = (
            frozen.get(
                "actual_progress"
            )
            or {}
        )

        if progress.get(
            "actual_available"
        ):
            lines.extend([
                "###### Verifica contro SOL reale",
                "",
                (
                    f"- Ultimo close disponibile: "
                    f"**{progress['latest_actual_date']}** · "
                    f"SOL **{money(progress['latest_actual_price'])}**."
                ),
                (
                    f"- Giorno del vintage: "
                    f"**{progress['elapsed_days']}/30**."
                ),
                (
                    f"- P50 condizionato previsto per quel giorno: "
                    f"**{money(progress['p50_price'])}**."
                ),
                (
                    "- SOL reale: "
                    + (
                        "**DENTRO p10-p90**"
                        if progress[
                            "inside_p10_p90"
                        ]
                        else "**FUORI p10-p90**"
                    )
                    + " · "
                    + (
                        "**DENTRO p25-p75**"
                        if progress[
                            "inside_p25_p75"
                        ]
                        else "**FUORI p25-p75**"
                    )
                    + "."
                ),
                "",
            ])

        meta = (
            frozen.get("meta")
            or {}
        )

        medians = (
            meta.get(
                "reproduced_medians"
            )
            or {}
        )

        if medians:
            lines.extend([
                "###### Parità con l'analisi originale",
                "",
                "| Giorno | Mediana return riprodotta |",
                "| ---: | ---: |",
            ])

            for day in (
                "7",
                "14",
                "21",
                "30",
            ):
                if day in medians:
                    lines.append(
                        f"| {day} | "
                        f"{pct(medians[day])} |"
                    )

            lines.append("")

        lines.extend([
            "###### Gli 8 episodi congelati",
            "",
            "| Asset | Match window | -5% hit | +10% anchor |",
            "| --- | --- | --- | --- |",
        ])

        for episode in (
            meta.get(
                "episodes"
            )
            or []
        ):
            lines.append(
                f"| {episode['asset']} | "
                f"{episode['episode_start_date']} → "
                f"{episode['episode_end_date']} | "
                f"{episode['minus5_hit_date']} | "
                f"{episode['plus10_anchor_date']} |"
            )

        lines.append("")

    lines.extend([
        (
            "**Come leggere la differenza:** il cono standard risponde a "
            "\"cosa hanno fatto i 40 casi più simili?\". Il Conditional "
            "Successor risponde a una domanda più stretta: \"tra quei casi, "
            "cosa è successo dopo che avevano già completato -5% → +10%?\". "
            "Per questo il secondo può risultare più rialzista ma anche molto "
            "più fragile statisticamente."
        ),
        "",
        (
            "I due modelli **non vengono mediati**, non sostituiscono l'uno "
            "l'altro e non modificano Global Confluence, segnali o decisioni."
        ),
        "",
        BLOCK_END,
        "",
    ])

    return lines


def inject_block(
    text,
    lines,
):
    block = "\n".join(
        lines
    ).strip()

    if (
        BLOCK_START in text
        and BLOCK_END in text
    ):
        prefix, rest = text.split(
            BLOCK_START,
            1,
        )

        _, suffix = rest.split(
            BLOCK_END,
            1,
        )

        return (
            prefix.rstrip()
            + "\n\n"
            + block
            + "\n\n"
            + suffix.lstrip()
        )

    anchor = (
        "![Scanner forecast SOL]"
        "(scanner_forecast_SOL.png)"
    )

    if anchor not in text:
        raise RuntimeError(
            "CANONICAL_SOL_CHART_ANCHOR_MISSING"
        )

    return text.replace(
        anchor,
        anchor
        + "\n\n"
        + block,
        1,
    )
