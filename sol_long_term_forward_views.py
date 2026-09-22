"""Forward-calendar visualizations for the recorded SOL Long-Term Cone.

Presentation only:
- no model recalculation
- no market-data download
- no synthetic forecast observations
- exact recorded 90/180/365/730-day horizon values only
"""
from __future__ import annotations

from datetime import date, timedelta
import math
from pathlib import Path
from typing import Any, Mapping, Sequence

import matplotlib

matplotlib.use("Agg")
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np


FORWARD_HORIZONS = (
    (90, "3M"),
    (180, "6M"),
    (365, "1Y"),
    (730, "2Y"),
)

CALENDAR_NAME = "sol_long_term_forward_calendar.svg"
VINTAGES_NAME = "sol_long_term_forward_vintages.svg"

COLORS = {
    "p50": "#185b96",
    "spot": "#273443",
}


def _number(value: Any) -> float:
    try:
        value = float(value)
    except (TypeError, ValueError, OverflowError):
        return float("nan")
    return value if math.isfinite(value) else float("nan")


def _money(value: Any) -> str:
    value = _number(value)
    return f"${value:,.2f}" if math.isfinite(value) else "—"


def _style_axis(axis, ylabel: str) -> None:
    axis.set_ylabel(ylabel)
    axis.grid(axis="y", color="#dde4ec", linewidth=0.7)
    axis.set_axisbelow(True)
    axis.spines[["top", "right"]].set_visible(False)
    axis.spines[["bottom", "left"]].set_color("#b8c4d1")


def _save(figure, path: Path) -> None:
    try:
        figure.savefig(
            path,
            format="svg",
            bbox_inches="tight",
            facecolor="white",
        )

        # Matplotlib SVG output can contain trailing spaces in path-data
        # lines. Normalize them so git diff --check stays clean.
        text = path.read_text(encoding="utf-8")
        normalized = "\n".join(
            line.rstrip(" \t")
            for line in text.splitlines()
        ) + "\n"
        path.write_text(normalized, encoding="utf-8")

    finally:
        plt.close(figure)


def _forecast_day(current: Mapping[str, Any]) -> date:
    return date.fromisoformat(str(current["generated_at"])[:10])


def forward_calendar_figure(current: Mapping[str, Any]):
    figure, axis = plt.subplots(figsize=(14, 7.2))

    forecast_day = _forecast_day(current)

    horizons = [item[0] for item in FORWARD_HORIZONS]

    target_dates = [
        forecast_day + timedelta(days=horizon)
        for horizon in horizons
    ]

    quantiles = {
        quantile: np.asarray([
            _number(current.get(f"h{horizon}_{quantile}"))
            for horizon in horizons
        ])
        for quantile in ("p10", "p25", "p50", "p75", "p90")
    }

    axis.fill_between(
        target_dates,
        quantiles["p10"],
        quantiles["p90"],
        color="#d5e6f5",
        label="p10–p90",
    )

    axis.fill_between(
        target_dates,
        quantiles["p25"],
        quantiles["p75"],
        color="#8fb9dc",
        label="p25–p75",
    )

    axis.plot(
        target_dates,
        quantiles["p50"],
        color=COLORS["p50"],
        linewidth=2.8,
        marker="o",
        markersize=6.2,
        label="p50",
    )

    spot = _number(current.get("spot_sol"))

    if math.isfinite(spot):
        axis.scatter(
            [forecast_day],
            [spot],
            color=COLORS["spot"],
            marker="D",
            s=48,
            zorder=5,
            label=f"SOL spot {_money(spot)}",
        )

        axis.annotate(
            f"Spot {_money(spot)}",
            (forecast_day, spot),
            xytext=(8, 8),
            textcoords="offset points",
            fontsize=9,
            color=COLORS["spot"],
        )

    for target, (_, label), value in zip(
        target_dates,
        FORWARD_HORIZONS,
        quantiles["p50"],
    ):
        if math.isfinite(value):
            axis.annotate(
                f"{label} p50 {_money(value)}",
                (target, value),
                xytext=(0, 10),
                textcoords="offset points",
                ha="center",
                fontsize=9,
                color=COLORS["p50"],
                fontweight="bold",
            )

    axis.set_xticks(mdates.date2num(target_dates))

    axis.set_xticklabels([
        f"{label}\n{target:%d %b %Y}"
        for target, (_, label) in zip(
            target_dates,
            FORWARD_HORIZONS,
        )
    ])

    axis.set_xlim(
        mdates.date2num(
            forecast_day - timedelta(days=35)
        ),
        mdates.date2num(
            target_dates[-1] + timedelta(days=45)
        ),
    )

    _style_axis(axis, "SOL price (USD)")

    axis.set_xlabel(
        f"Future target date · forecast vintage "
        f"{forecast_day.isoformat()} · Europe/Madrid",
        labelpad=12,
        color="#506479",
    )

    axis.set_title(
        "SOL Long-Term Cone — Forward Calendar",
        loc="left",
        fontsize=18,
        pad=32,
        fontweight="bold",
    )

    axis.text(
        0,
        1.035,
        "Recorded 90/180/365/730-day horizons on real target dates · "
        "lines only connect recorded horizons",
        transform=axis.transAxes,
        color="#506479",
    )

    axis.legend(
        loc="upper left",
        frameon=False,
        ncol=4,
    )

    figure.text(
        0.075,
        0.02,
        "No intermediate forecast points are created · DIAGNOSTIC ONLY",
        fontsize=9,
        color="#506479",
    )

    figure.tight_layout(
        rect=(0, 0.045, 1, 1)
    )

    return figure


def forward_vintages_figure(
    rows: Sequence[Mapping[str, Any]]
):
    figure, axis = plt.subplots(
        figsize=(14, 7.6)
    )

    ordered = sorted(
        rows,
        key=lambda row: str(row["date_local"]),
    )

    latest = ordered[-1]

    for row in ordered:
        forecast_day = date.fromisoformat(
            str(row["date_local"])
        )

        dates = [forecast_day] + [
            forecast_day + timedelta(days=horizon)
            for horizon, _ in FORWARD_HORIZONS
        ]

        values = [
            _number(row.get("spot_sol"))
        ] + [
            _number(row.get(f"h{horizon}_p50"))
            for horizon, _ in FORWARD_HORIZONS
        ]

        points = [
            (day, value)
            for day, value in zip(dates, values)
            if math.isfinite(value)
        ]

        if len(points) < 2:
            continue

        is_latest = row is latest

        axis.plot(
            [point[0] for point in points],
            [point[1] for point in points],
            color=(
                COLORS["p50"]
                if is_latest
                else "#8fa6bb"
            ),
            linewidth=(
                2.8 if is_latest else 0.9
            ),
            alpha=(
                1.0 if is_latest else 0.30
            ),
            marker=(
                "o" if is_latest else None
            ),
            markersize=(
                5.5 if is_latest else 0
            ),
            label=(
                f"Latest vintage {row['date_local']}"
                if is_latest
                else "_nolegend_"
            ),
        )

    latest_day = date.fromisoformat(
        str(latest["date_local"])
    )

    for horizon, label in FORWARD_HORIZONS:
        value = _number(
            latest.get(f"h{horizon}_p50")
        )

        if not math.isfinite(value):
            continue

        target = (
            latest_day
            + timedelta(days=horizon)
        )

        axis.annotate(
            f"{label} {_money(value)}",
            (target, value),
            xytext=(0, 9),
            textcoords="offset points",
            ha="center",
            fontsize=9,
            color=COLORS["p50"],
            fontweight="bold",
        )

    _style_axis(
        axis,
        "SOL p50 (USD)",
    )

    axis.set_xlabel(
        "Calendar date · each line uses its own exact target dates",
        labelpad=12,
        color="#506479",
    )

    axis.xaxis.set_major_locator(
        mdates.AutoDateLocator(
            minticks=6,
            maxticks=10,
        )
    )

    axis.xaxis.set_major_formatter(
        mdates.DateFormatter("%b %Y")
    )

    axis.set_title(
        "SOL Long-Term Cone — Forward Vintages (p50)",
        loc="left",
        fontsize=18,
        pad=32,
        fontweight="bold",
    )

    axis.text(
        0,
        1.035,
        "Each faint line = one real daily vintage projected onto exact "
        "90/180/365/730-day target dates · latest highlighted",
        transform=axis.transAxes,
        color="#506479",
    )

    axis.legend(
        loc="upper left",
        frameon=False,
    )

    figure.text(
        0.075,
        0.02,
        "Spot + recorded p50 horizon points only · "
        "no intermediate forecast points · DIAGNOSTIC ONLY",
        fontsize=9,
        color="#506479",
    )

    figure.tight_layout(
        rect=(0, 0.045, 1, 1)
    )

    return figure


def _forward_readme_block(
    current: Mapping[str, Any]
) -> str:
    forecast_day = _forecast_day(current)

    lines = [
        "<!-- SOL_FORWARD_VIEWS_START -->",
        "## Forward calendar",
        "",
        f"![SOL Long-Term Cone — Forward Calendar]({CALENDAR_NAME})",
        "",
        "Asse X = date future reali. Sono mostrati soltanto gli "
        "orizzonti registrati 90/180/365/730 giorni; le linee "
        "collegano i punti per leggibilità e non creano "
        "previsioni intermedie.",
        "",
        "| Horizon | Target date | p50 | p75 | p90 |",
        "| --- | --- | ---: | ---: | ---: |",
    ]

    for horizon, label in FORWARD_HORIZONS:
        target = (
            forecast_day
            + timedelta(days=horizon)
        )

        lines.append(
            f"| {label} | {target.isoformat()} | "
            f"{_money(current.get(f'h{horizon}_p50'))} | "
            f"{_money(current.get(f'h{horizon}_p75'))} | "
            f"{_money(current.get(f'h{horizon}_p90'))} |"
        )

    lines += [
        "",
        "## Forward vintages",
        "",
        f"![SOL Long-Term Cone — Forward Vintages]({VINTAGES_NAME})",
        "",
        "Ogni linea è un vero snapshot giornaliero proiettato "
        "sulle sue date target esatte. La linea più marcata è "
        "l'ultimo vintage; sono usati spot e p50 registrati, "
        "senza punti sintetici.",
        "",
        "<!-- SOL_FORWARD_VIEWS_END -->",
    ]

    return "\n".join(lines)


def inject_readme(
    path: Path,
    current: Mapping[str, Any],
) -> None:
    text = path.read_text(
        encoding="utf-8"
    )

    start = "<!-- SOL_FORWARD_VIEWS_START -->"
    end = "<!-- SOL_FORWARD_VIEWS_END -->"

    if start in text and end in text:
        before, rest = text.split(
            start,
            1,
        )
        _, after = rest.split(
            end,
            1,
        )

        text = (
            before.rstrip()
            + "\n\n"
            + after.lstrip()
        )

    marker = "## Forecast history"

    if marker not in text:
        raise RuntimeError(
            "Forecast history README marker missing"
        )

    before, after = text.split(
        marker,
        1,
    )

    block = _forward_readme_block(
        current
    )

    text = (
        before.rstrip()
        + "\n\n"
        + block
        + "\n\n"
        + marker
        + after
    )

    path.write_text(
        text.rstrip() + "\n",
        encoding="utf-8",
    )


def render_forward_views(
    rows: Sequence[Mapping[str, Any]],
    current: Mapping[str, Any],
    output_dir: str | Path,
) -> list[Path]:

    if not rows:
        raise ValueError(
            "at least one real daily observation is required"
        )

    output = Path(output_dir)
    output.mkdir(
        parents=True,
        exist_ok=True,
    )

    calendar = (
        output / CALENDAR_NAME
    )

    vintages = (
        output / VINTAGES_NAME
    )

    readme = (
        output / "README.md"
    )

    if not readme.is_file():
        raise RuntimeError(
            "base README must be rendered first"
        )

    before_rows = [
        dict(row)
        for row in rows
    ]

    with plt.rc_context({
        "font.family": "DejaVu Sans",
        "font.size": 10,
    }):
        _save(
            forward_calendar_figure(current),
            calendar,
        )

        _save(
            forward_vintages_figure(rows),
            vintages,
        )

    inject_readme(
        readme,
        current,
    )

    if before_rows != [
        dict(row)
        for row in rows
    ]:
        raise RuntimeError(
            "forward rendering mutated source observations"
        )

    return [
        calendar,
        vintages,
    ]
