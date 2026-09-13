"""Render the SOL history dashboard from validated observations only.

This module has no market-data, model, network, publishing, or trading imports.
All prices and empirical probabilities are values recorded by the cone producer.
"""
from __future__ import annotations

from datetime import date
import math
from pathlib import Path
from typing import Any, Mapping, Sequence

import matplotlib

matplotlib.use("Agg")
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np

from sol_long_term_history import recent_statistics


HORIZONS = ((180, "6M"), (365, "1Y"), (730, "2Y"))
OUTPUT_NAMES = (
    "sol_long_term_cone_current.png",
    "sol_long_term_cone_history.png",
    "sol_long_term_probability_history.png",
    "README.md",
)
COLORS = {"p50": "#185b96", "p75": "#b36905", "p90": "#9b3b8b", "spot": "#273443"}


def _number(value: Any) -> float:
    """Missing or non-finite observations stay missing, never zero-filled."""
    try:
        result = float(value)
    except (TypeError, ValueError, OverflowError):
        return float("nan")
    return result if math.isfinite(result) else float("nan")


def _money(value: Any) -> str:
    number = _number(value)
    return f"${number:,.2f}" if math.isfinite(number) else "—"


def _percent(value: Any) -> str:
    number = _number(value)
    return f"{number:.2f}%" if math.isfinite(number) else "—"


def _plain(value: Any) -> str:
    if value is None or value == "":
        return "—"
    if isinstance(value, float) and not math.isfinite(value):
        return "—"
    return str(value).replace("|", "\\|").replace("\n", " ")


def _style_axis(axis, ylabel: str) -> None:
    axis.set_ylabel(ylabel)
    axis.grid(axis="y", color="#dde4ec", linewidth=0.7)
    axis.set_axisbelow(True)
    axis.spines[["top", "right"]].set_visible(False)
    axis.spines[["bottom", "left"]].set_color("#b8c4d1")


def _save(figure, path: Path) -> None:
    try:
        figure.savefig(path, dpi=150, bbox_inches="tight", facecolor="white")
    finally:
        plt.close(figure)


def _current_figure(current: Mapping[str, Any]):
    figure, axis = plt.subplots(figsize=(12, 6.2))
    days = np.asarray([90, 180, 365, 730], dtype=float)
    quantiles = {quantile: np.asarray([_number(current.get(f"h{int(day)}_{quantile}")) for day in days])
                 for quantile in ("p10", "p25", "p50", "p75", "p90")}
    axis.fill_between(days, quantiles["p10"], quantiles["p90"], color="#d5e6f5", label="p10–p90")
    axis.fill_between(days, quantiles["p25"], quantiles["p75"], color="#8fb9dc", label="p25–p75")
    axis.plot(days, quantiles["p50"], color=COLORS["p50"], linewidth=2.2, marker="o", label="p50")
    spot = _number(current.get("spot_sol"))
    if math.isfinite(spot):
        axis.axhline(spot, color=COLORS["spot"], linestyle="--", linewidth=1.5, label=f"SOL spot {_money(spot)}")
    axis.set_xticks(days, ["90", "180", "365", "730"])
    axis.set_xlabel("Horizon (days)")
    axis.set_xlim(70, 750)
    _style_axis(axis, "SOL price (USD)")
    axis.set_title("SOL Long-Term Probability Cone — Current", loc="left", fontsize=17, pad=35, fontweight="bold")
    axis.text(0, 1.045, "LOG_ROBUST_TAIL · Recorded horizon quantiles", transform=axis.transAxes, color="#506479")
    axis.legend(loc="best", frameon=False, ncol=2)
    figure.text(0.07, 0.018,
                f"generated_at: {_plain(current.get('generated_at'))}  |  "
                f"cohort: {_plain(current.get('canonical_cohort_count'))}  |  "
                f"distinct assets: {_plain(current.get('distinct_assets'))}  |  DIAGNOSTIC ONLY",
                fontsize=8, color="#506479")
    figure.tight_layout(rect=(0, 0.055, 1, 1))
    return figure


def _date_axis(axis, dates: Sequence[date]) -> None:
    """Thin only tick labels; retain every supplied observation in the plots."""
    unique = sorted(set(dates))
    indices = np.unique(np.linspace(0, len(unique) - 1, min(len(unique), 12), dtype=int))
    ticks = [unique[index] for index in indices]
    axis.set_xticks(mdates.date2num(ticks))
    pattern = "%d %b" if unique[0].year == unique[-1].year else "%d %b %y"
    axis.xaxis.set_major_formatter(mdates.DateFormatter(pattern))
    first, last = mdates.date2num([unique[0], unique[-1]])
    margin = max((last - first) * 0.025, 0.3)
    axis.set_xlim(first - margin, last + margin)
    year = str(unique[0].year) if unique[0].year == unique[-1].year else f"{unique[0].year}–{unique[-1].year}"
    axis.set_xlabel(f"Snapshot date · Europe/Madrid · {year}", labelpad=10, color="#506479")
    axis.tick_params(axis="x", labelsize=9)


def _plot_observed_series(axis, dates, values, *, label, gid, color,
                          marker="o", linewidth=2, linestyle="-", alpha=1):
    """Draw separate runs of adjacent real dates, never inserting missing dates.

    A missing value ends a run as well. Every finite value appears in exactly
    one Line2D, with its original date and value and a visible marker.
    """
    runs, run = [], []
    for day, raw in zip(dates, values):
        value = _number(raw)
        if not math.isfinite(value):
            if run:
                runs.append(run)
                run = []
            continue
        if run and (day - run[-1][0]).days != 1:
            runs.append(run)
            run = []
        run.append((day, value))
    if run:
        runs.append(run)
    for index, points in enumerate(runs):
        axis.plot([p[0] for p in points], [p[1] for p in points],
                  label=label if index == 0 else "_nolegend_", gid=gid,
                  color=color, linewidth=linewidth, linestyle=linestyle,
                  marker=marker, markersize=5.6 if linewidth >= 2.5 else 4.6,
                  markeredgecolor="white", markeredgewidth=0.65, alpha=alpha,
                  zorder=4 if linewidth >= 2.5 else 3)
    return runs[-1][-1] if runs else None


def _end_labels(axis, entries):
    """Place labels outside the axes with leaders to the exact real endpoints."""
    if not entries:
        return
    low, high = axis.get_ylim()
    ordered = sorted(entries, key=lambda item: item[0][1])
    minimum, maximum, gap = 0.065, 0.94, 0.095
    positions = [max(minimum, min(maximum, (point[1] - low) / (high - low)))
                 for point, _, _ in ordered]
    for index in range(1, len(positions)):
        positions[index] = max(positions[index], positions[index - 1] + gap)
    if positions[-1] > maximum:
        positions[-1] = maximum
        for index in range(len(positions) - 2, -1, -1):
            positions[index] = min(positions[index], positions[index + 1] - gap)
    for (point, label, color), y in zip(ordered, positions):
        axis.annotate(label, xy=(mdates.date2num(point[0]), point[1]), xycoords="data",
                      xytext=(1.025, y), textcoords="axes fraction", va="center", ha="left",
                      fontsize=10, fontweight="normal", color=color, annotation_clip=False,
                      arrowprops={"arrowstyle": "-", "color": color, "linewidth": 0.75,
                                  "alpha": 0.6, "connectionstyle": "angle3,angleA=0,angleB=90"},
                      bbox={"facecolor": "white", "edgecolor": "none", "pad": 1.5})


def _panel_drift_title(label, horizon, statistics):
    latest = statistics.get("trend_new") or {}
    old = statistics.get("trend_old") or {}
    key = f"h{horizon}_p50"
    before, after = _number(old.get(key)), _number(latest.get(key))
    change = (after / before - 1) * 100 if math.isfinite(before) and before > 0 and math.isfinite(after) else float("nan")
    period = "available history" if statistics["short_7d"] else "7d"
    delta = f"{change:+.1f}%" if math.isfinite(change) else "—"
    return f"{label} — Latest p50 {_money(after)} · {period} {delta}"


def _history_figure(rows: Sequence[Mapping[str, Any]]):
    figure, axes = plt.subplots(3, 1, figsize=(14, 12), sharex=True, sharey=False)
    dates = [date.fromisoformat(str(row["date_local"])) for row in rows]
    statistics = recent_statistics(rows)
    styles = (("p50", 2.8, "o", 1.0), ("p75", 1.8, "s", 0.95), ("p90", 1.15, "^", 0.72))
    for axis, (horizon, label) in zip(axes, HORIZONS):
        labels, present = [], []
        for quantile, width, marker, alpha in styles:
            values = [_number(row.get(f"h{horizon}_{quantile}")) for row in rows]
            present.extend(value for value in values if math.isfinite(value))
            endpoint = _plot_observed_series(axis, dates, values, label=quantile, gid=quantile,
                color=COLORS[quantile], linewidth=width, marker=marker, alpha=alpha)
            if endpoint:
                labels.append((endpoint, f"{quantile} {_money(endpoint[1])}", COLORS[quantile]))
        spot = [_number(row.get("spot_sol")) for row in rows]
        present.extend(value for value in spot if math.isfinite(value))
        endpoint = _plot_observed_series(axis, dates, spot, label="SOL spot", gid="spot",
            color=COLORS["spot"], linewidth=1.05, linestyle="--", marker="D")
        if endpoint:
            labels.append((endpoint, f"SOL {_money(endpoint[1])}", COLORS["spot"]))
        if present:
            lower, upper = min(present), max(present)
            span = max(upper - lower, abs(upper) * 0.1, 1)
            axis.set_ylim(max(0, lower - span * 0.10), upper + span * 0.16)
        _style_axis(axis, "SOL price (USD)")
        axis.set_title(_panel_drift_title(label, horizon, statistics), loc="left",
                       fontsize=12, fontweight="bold", pad=13)
        axis.legend(loc="upper right", frameon=False, ncol=4, fontsize=9,
                    handlelength=2.5, columnspacing=1.3)
        _date_axis(axis, dates)
        axis.tick_params(axis="x", labelbottom=True)
        _end_labels(axis, labels)
    figure.suptitle("SOL Long-Term Cone — Forecast History", x=0.075, y=0.985,
                   ha="left", fontsize=20, fontweight="bold")
    figure.text(0.075, 0.95,
                "LOG_ROBUST_TAIL · Real observations with markers · Missing days remain gaps · DIAGNOSTIC ONLY",
                fontsize=10, color="#506479")
    figure.subplots_adjust(left=0.075, right=0.83, top=0.895, bottom=0.075, hspace=0.64)
    return figure


def _probability_figure(rows: Sequence[Mapping[str, Any]]):
    figure, axes = plt.subplots(2, 1, figsize=(14, 9.5), sharex=True)
    dates = [date.fromisoformat(str(row["date_local"])) for row in rows]
    panels = (
        ("2 YEARS", (("h730_p_ge_300", 300, "#185b96", "o"),
                      ("h730_p_ge_500", 500, "#b36905", "s"),
                      ("h730_p_ge_800", 800, "#9b3b8b", "^"))),
        ("6 MONTHS", (("h180_p_ge_200", 200, "#187e70", "o"),
                       ("h180_p_ge_300", 300, "#6a627d", "s"))),
    )
    for axis, (title, series) in zip(axes, panels):
        labels = []
        for key, threshold, color, marker in series:
            endpoint = _plot_observed_series(axis, dates, [row.get(key) for row in rows],
                label=f"P(SOL ≥ ${threshold})", gid=key, color=color, marker=marker, linewidth=2.1)
            if endpoint:
                labels.append((endpoint, f"≥ ${threshold}: {endpoint[1]:.1f}%", color))
        axis.set_ylim(0, 100)
        axis.set_yticks([0, 20, 40, 60, 80, 100], ["0%", "20%", "40%", "60%", "80%", "100%"])
        _style_axis(axis, "Empirical analog frequency")
        axis.set_title(title, loc="left", fontsize=13, fontweight="bold", pad=13)
        _date_axis(axis, dates)
        axis.tick_params(axis="x", labelbottom=True)
        axis.legend(loc="upper right", frameon=False, ncol=len(series), fontsize=9, handlelength=2.5)
        _end_labels(axis, labels)
    figure.suptitle("SOL Long-Term Cone — Probability History", x=0.075, y=0.98,
                   ha="left", fontsize=20, fontweight="bold")
    figure.text(0.075, 0.94,
                "LOG_ROBUST_TAIL · Real observations with markers · Missing days remain gaps · DIAGNOSTIC ONLY",
                fontsize=10, color="#506479")
    figure.subplots_adjust(left=0.075, right=0.83, top=0.875, bottom=0.09, hspace=0.45)
    return figure


def _render_readme(rows: Sequence[Mapping[str, Any]], current: Mapping[str, Any],
                   first_snapshot: str, latest_snapshot: str) -> str:
    statistics = recent_statistics(rows)
    metrics = statistics["metrics"]
    lines = [
        "# SOL Long-Term Cone History", "",
        f"Ultimo aggiornamento: **{_plain(current.get('generated_at'))}**  ",
        f"SOL spot: **{_money(current.get('spot_sol'))}**  ",
        f"Cohort: **{_plain(current.get('canonical_cohort_count'))}** analoghi / "
        f"**{_plain(current.get('distinct_assets'))}** distinct assets  ",
        "**LOG_ROBUST_TAIL · DIAGNOSTIC ONLY**", "",
        "## Current cone", "", "![SOL Long-Term Probability Cone — Current](sol_long_term_cone_current.png)", "",
        "## Forecast history", "", "![SOL Long-Term Cone — Forecast History](sol_long_term_cone_history.png)", "",
        "Linee tra osservazioni reali consecutive, con marker; i giorni mancanti restano gap.", "",
        "- p50 = mediana degli analoghi",
        "- p75 = 25% degli analoghi sopra questo livello",
        "- p90 = 10% degli analoghi sopra questo livello",
        "- SOL spot = prezzo osservato nel giorno dello snapshot", "",
        "## Probability history", "", "![SOL Long-Term Cone — Probability History](sol_long_term_probability_history.png)", "",
        "Le percentuali rappresentano la frequenza empirica degli analoghi che terminano "
        "sopra la soglia all'orizzonte indicato.", "",
        "## Latest snapshot", "",
        "| Horizon | p50 | p75 | p90 | P≥300 | P≥500 |",
        "| --- | ---: | ---: | ---: | ---: | ---: |",
    ]
    for horizon, label in HORIZONS:
        values = [_money(current.get(f"h{horizon}_{q}")) for q in ("p50", "p75", "p90")]
        values.extend(_percent(current.get(f"h{horizon}_p_ge_{threshold}")) for threshold in (300, 500))
        lines.append(f"| {label} | " + " | ".join(values) + " |")
    lines += ["", "## Recent drift", "", "Ultime 7 daily observations reali (non necessariamente consecutive).", ""]
    if statistics["short_7d"]:
        lines += ["**storico <7 giorni**: confronto con la prima osservazione giornaliera disponibile.", ""]
    lines += ["| Date | Spot | 6M p50 | 1Y p50 | 2Y p50 | 2Y P≥300 | 2Y P≥500 |",
              "| --- | ---: | ---: | ---: | ---: | ---: | ---: |"]
    for row in rows[-7:]:
        values = [_plain(row["date_local"]), _money(row.get("spot_sol"))]
        values.extend(_money(row.get(f"h{horizon}_p50")) for horizon, _ in HORIZONS)
        values.extend(_percent(row.get(f"h730_p_ge_{threshold}")) for threshold in (300, 500))
        lines.append("| " + " | ".join(values) + " |")
    lines += ["", "## 30-day stability", "",
              f"Finestra: {len(statistics['window_rows'])} osservazioni reali disponibili negli ultimi 30 giorni di calendario; "
              "i giorni mancanti non vengono interpolati.", ""]
    if statistics["short_30d"]:
        lines += ["**storico <30 giorni**: statistiche sullo storico disponibile. "
                  "Campione insufficiente per interpretare lo status come prova di stabilità duratura.", ""]
    lines += ["| Metric | Median | Min | Max | range_pct | Range (pp) |",
              "| --- | ---: | ---: | ---: | ---: | ---: |"]
    for key, label in (("h180_p50", "6M p50"), ("h365_p50", "1Y p50"), ("h730_p50", "2Y p50"),
                       ("h730_p_ge_300", "2Y P≥300"), ("h730_p_ge_500", "2Y P≥500")):
        metric = metrics.get(key, {})
        formatter = _percent if "_p_ge_" in key else _money
        values = [formatter(metric.get(field)) for field in ("median", "min", "max")]
        if "_p_ge_" in key:
            probability_range = _number(metric.get("range"))
            values.extend(["—", f"{probability_range:.2f}" if math.isfinite(probability_range) else "—"])
        else:
            values.extend([_percent(metric.get("range_pct")), "—"])
        lines.append(f"| {label} | " + " | ".join(values) + " |")
    lines += ["", f"**FORECAST_DRIFT_STATUS={statistics['drift_status']}**", "",
              "`range_pct = 100 × (max − min) / median` per i prezzi. "
              "Le variazioni delle probabilità sono punti percentuali (pp).", "",
              "- **STABLE**: 2Y p50 range_pct <20% e 2Y P≥300 range <10 pp.",
              "- **VOLATILE**: 2Y p50 range_pct ≥40% oppure 2Y P≥300 range ≥20 pp.",
              "- **CAUTION**: gli altri casi, inclusi dati insufficienti per classificare.", "",
              "Indicatore diagnostico; non va usato per decisioni operative. "
              "Una sola osservazione ha range zero e non dimostra stabilità temporale.", "",
              "## Methodology", "",
              "- Stesso cohort canonico Legacy, con massimo 40 analoghi; il cohort non viene modificato.",
              "- Vista LOG_ROBUST_TAIL e asset-level robustification già prodotte dal Long-Term Cone.",
              "- Probabilities = empirical analog frequencies, espresse in percentuale; non probabilità calibrate.",
              "- Diagnostic only. Nessun modello ricalcolato per questa pagina, nessun segnale o decisione operativa.",
              "- Daily observation in Europe/Madrid: all'importazione iniziale si sceglie l'ultimo snapshot "
              "qualificante disponibile per ogni data locale. Alla prima pubblicazione la riga diventa "
              "immutabile: i successivi run non la sostituiscono e non duplicano la giornata.",
              "- I giorni senza snapshot reale restano assenti; i valori mancanti sono indicati con —, senza stime o interpolazione.",
              "- Ogni osservazione produce forecast vintages con target_date = forecast_date + target_horizon_days. "
              "Nessun outcome futuro viene inventato o maturato anticipatamente.", "",
              "## Data availability", "",
              f"FIRST_REAL_SNAPSHOT={_plain(first_snapshot)}  ",
              f"FIRST_AVAILABLE_LONG_TERM_SNAPSHOT={_plain(first_snapshot)}  ",
              f"LATEST_SNAPSHOT={_plain(latest_snapshot)}  ",
              f"DAILY_ROWS={len(rows)}", "",
              "Fonti autoritative: `sol_long_term_probability_cone.json`, "
              "`sol_long_term_probability_cone_history.jsonl` e snapshot immutabili in "
              "`sol_long_term_probability_cone_history/` nel publisher canonico.", "",
              "Download: [daily observation ledger](sol_long_term_daily_history.csv) · "
              "[forecast vintages](forecast_vintages.csv).", ""]
    return "\n".join(lines)


def render_dashboard(rows: Sequence[Mapping[str, Any]], current: Mapping[str, Any],
                     output_dir: str | Path, first_snapshot: str, latest_snapshot: str) -> list[Path]:
    """Write three figures and README into the caller's staging directory.

    The caller validates all outputs before publishing the complete staging set.
    No source files, observation ledgers, or existing forecast images are changed.
    """
    if not rows:
        raise ValueError("at least one real daily observation is required")
    ordered_rows = sorted(rows, key=lambda row: str(row["date_local"]))
    dates = [str(row["date_local"]) for row in ordered_rows]
    if len(set(dates)) != len(dates):
        raise ValueError("duplicate daily observation date")
    for day in dates:
        date.fromisoformat(day)
    output = Path(output_dir)
    output.mkdir(parents=True, exist_ok=True)
    files = [output / name for name in OUTPUT_NAMES]
    with plt.rc_context({"font.family": "DejaVu Sans", "font.size": 10}):
        _save(_current_figure(current), files[0])
        _save(_history_figure(ordered_rows), files[1])
        _save(_probability_figure(ordered_rows), files[2])
    files[3].write_text(_render_readme(ordered_rows, current, first_snapshot, latest_snapshot), encoding="utf-8")
    return files
