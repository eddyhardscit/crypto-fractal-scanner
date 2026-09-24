"""Forward-calendar visualizations for the recorded SOL Long-Term Cone.

Presentation only:
- no model recalculation
- no market-data download
- no synthetic forecast observations
- exact recorded 90/180/365/730-day horizon values only
"""
from __future__ import annotations

from datetime import date, timedelta
import csv
import json
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
    "p10": "#7f8c99",
    "p25": "#4f7fa8",
    "p50": "#185b96",
    "p75": "#b36905",
    "p90": "#9b3b8b",
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


def _load_short_term_context(
    output_dir: Path,
) -> dict[str, Any]:
    """Load existing short-term SOL outputs without recalculation."""
    reports_dir = output_dir.parent
    context: dict[str, Any] = {
        "available": False,
        "standard": None,
        "conditional": None,
        "frozen": None,
    }

    latest_path = reports_dir / "scanner_forecast_latest.csv"
    if latest_path.is_file():
        try:
            with latest_path.open(
                "r", encoding="utf-8", newline=""
            ) as handle:
                rows = list(csv.DictReader(handle))
            sol = next(
                (
                    row
                    for row in reversed(rows)
                    if str(row.get("asset", "")).strip() == "SOL"
                ),
                None,
            )
            if sol:
                context["standard"] = {
                    "snapshot_date": sol.get("snapshot_date"),
                    "sample": 40,
                    "p10_price": sol.get("p10_30d_price"),
                    "p25_price": sol.get("p25_30d_price"),
                    "p50_price": sol.get("p50_30d_price"),
                    "p75_price": sol.get("p75_30d_price"),
                    "p90_price": sol.get("p90_30d_price"),
                }
        except Exception:
            context["standard"] = None

    dynamic_path = reports_dir / "sol_conditional_successor_current.json"
    if dynamic_path.is_file():
        try:
            payload = json.loads(dynamic_path.read_text(encoding="utf-8"))
            if payload.get("status") == "AVAILABLE" and payload.get("q30"):
                context["conditional"] = {
                    "snapshot_date": payload.get("forecast_date"),
                    "sample": payload.get("qualified_episodes"),
                    **payload["q30"],
                }
        except Exception:
            context["conditional"] = None

    frozen_path = reports_dir / "sol_conditional_successor_vintage_20260918.json"
    if frozen_path.is_file():
        try:
            payload = json.loads(frozen_path.read_text(encoding="utf-8"))
            if payload.get("q30"):
                context["frozen"] = {
                    "snapshot_date": payload.get("vintage_date"),
                    "sample": payload.get("qualified_episodes"),
                    **payload["q30"],
                }
        except Exception:
            context["frozen"] = None

    context["available"] = any(
        context.get(key)
        for key in ("standard", "conditional", "frozen")
    )
    return context


def _short_term_readme_lines(
    context: Mapping[str, Any] | None,
) -> list[str]:
    lines = [
        "## Short-term context (30 giorni)",
        "",
        (
            "Questa pagina resta il **Long-Term Cone** (3M/6M/1Y/2Y). "

            "Il blocco seguente riporta, senza ricalcolarli o mescolarli, "

            "gli ultimi output dello scanner SOL a 30 giorni."
        ),
        "",
    ]

    if not context or not context.get("available"):
        lines += [
            (
                "Dati short-term non disponibili in questo snapshot; "

                "il Long-Term Cone resta invariato."
            ),
            "",
            "[Apri il report short-term](../latest_report.md)",
            "",
        ]
        return lines

    lines += [
        (
            "| Modello short-term | Snapshot | Campione | "

            "P10 | P25 | P50 | P75 | P90 |"
        ),
        "| --- | --- | --- | ---: | ---: | ---: | ---: | ---: |",
    ]

    rows = (
        ("Cono standard", context.get("standard"), "40 analoghi correnti"),
        ("Conditional -5% → +10% corrente", context.get("conditional"), None),
        ("Conditional vintage 18 Sep", context.get("frozen"), None),
    )

    for label, row, fixed_sample in rows:
        if not row:
            continue
        sample = fixed_sample if fixed_sample is not None else str(row.get("sample", "—"))
        lines.append(
            f"| {label} | {row.get('snapshot_date') or '—'} | {sample} | "

            f"{_money(row.get('p10_price'))} | {_money(row.get('p25_price'))} | "

            f"{_money(row.get('p50_price'))} | {_money(row.get('p75_price'))} | "

            f"{_money(row.get('p90_price'))} |"
        )

    lines += [
        "",
        "- **Standard:** usa i 40 analoghi SOL correnti.",
        (
            "- **Conditional corrente:** filtra quei 40 e mantiene solo "

            "gli episodi che fanno prima -5% e poi +10% entro 30 giorni."
        ),
        (
            "- **Vintage 18 Sep:** resta congelato per la verifica "

            "fuori campione della previsione originale."
        ),
        (
            "- Questi numeri non vengono mediati con il Long-Term Cone "

            "e non ne modificano il modello."
        ),
        "",
        "[Apri il dettaglio short-term](../latest_report.md)",
        "",
    ]
    return lines


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
        label="_nolegend_",
    )

    axis.fill_between(
        target_dates,
        quantiles["p25"],
        quantiles["p75"],
        color="#8fb9dc",
        label="_nolegend_",
    )

    quantile_styles = (
        ("p10", 1.15, ":", "v", 0.80),
        ("p25", 1.55, "--", "s", 0.90),
        ("p50", 2.90, "-", "o", 1.00),
        ("p75", 1.55, "--", "s", 0.90),
        ("p90", 1.15, ":", "^", 0.80),
    )

    for quantile, width, linestyle, marker, alpha in quantile_styles:
        axis.plot(
            target_dates,
            quantiles[quantile],
            color=COLORS[quantile],
            linewidth=width,
            linestyle=linestyle,
            marker=marker,
            markersize=6.2 if quantile == "p50" else 4.8,
            markeredgecolor="white",
            markeredgewidth=0.65,
            alpha=alpha,
            label=quantile,
            gid=f"forward_{quantile}",
            zorder=4 if quantile == "p50" else 3,
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
    current: Mapping[str, Any],
    short_term: Mapping[str, Any] | None = None,
) -> str:
    forecast_day = _forecast_day(current)

    lines = [
        "<!-- SOL_FORWARD_VIEWS_START -->",
    ]
    lines += _short_term_readme_lines(short_term)
    lines += [
        "## Forward calendar",
        "",
        f"![SOL Long-Term Cone — Forward Calendar]({CALENDAR_NAME})",
        "",
        "Asse X = date future reali. Le linee mostrano esplicitamente "
        "p10, p25, p50, p75 e p90 ai soli orizzonti registrati "
        "90/180/365/730 giorni; i segmenti collegano i punti per "
        "leggibilità e non creano previsioni intermedie.",
        "",
        "| Horizon | Target date | p10 | p25 | p50 | p75 | p90 |",
        "| --- | --- | ---: | ---: | ---: | ---: | ---: |",
    ]

    for horizon, label in FORWARD_HORIZONS:
        target = (
            forecast_day
            + timedelta(days=horizon)
        )

        lines.append(
            f"| {label} | {target.isoformat()} | "
            f"{_money(current.get(f'h{horizon}_p10'))} | "
            f"{_money(current.get(f'h{horizon}_p25'))} | "
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
    short_term: Mapping[str, Any] | None = None,
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
        current,
        short_term,
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

    short_term = _load_short_term_context(
        output
    )

    inject_readme(
        readme,
        current,
        short_term,
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
