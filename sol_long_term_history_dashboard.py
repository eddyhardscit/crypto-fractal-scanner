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
    if len(set(dates)) == 1:
        center = mdates.date2num(dates[0])
        axis.set_xlim(center - 0.5, center + 0.5)
        axis.set_xticks([center])
        axis.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))
    else:
        locator = mdates.AutoDateLocator(minticks=2, maxticks=8)
        axis.xaxis.set_major_locator(locator)
        axis.xaxis.set_major_formatter(mdates.ConciseDateFormatter(locator))
    axis.set_xlabel("Real observation date · Europe/Madrid")


def _history_figure(rows: Sequence[Mapping[str, Any]]):
    figure, axes = plt.subplots(3, 1, figsize=(12, 11), sharex=True)
    dates = [date.fromisoformat(str(row["date_local"])) for row in rows]
    for axis, (horizon, label) in zip(axes, HORIZONS):
        for quantile in ("p50", "p75", "p90"):
            # Scatter deliberately leaves unobserved dates and missing values empty.
            values = [_number(row.get(f"h{horizon}_{quantile}")) for row in rows]
            axis.scatter(dates, values, label=quantile, color=COLORS[quantile], s=35, alpha=0.88)
        axis.scatter(dates, [_number(row.get("spot_sol")) for row in rows],
                     label="SOL spot", marker="x", color=COLORS["spot"], s=38)
        axis.set_title(label, loc="left", fontsize=12, fontweight="bold")
        _style_axis(axis, "SOL price (USD)")
        axis.legend(loc="best", frameon=False, ncol=4, fontsize=9)
    _date_axis(axes[-1], dates)
    figure.suptitle("SOL Long-Term Cone — Forecast History", x=0.08, y=0.992,
                     ha="left", fontsize=17, fontweight="bold")
    figure.text(0.08, 0.955, "LOG_ROBUST_TAIL · Real daily observations only · No interpolation · DIAGNOSTIC ONLY",
                fontsize=10, color="#506479")
    figure.tight_layout(rect=(0, 0, 1, 0.94))
    return figure


def _probability_figure(rows: Sequence[Mapping[str, Any]]):
    figure, axis = plt.subplots(figsize=(12, 6.3))
    dates = [date.fromisoformat(str(row["date_local"])) for row in rows]
    series = (
        ("h730_p_ge_300", "2Y P(SOL ≥ $300)", "#185b96", "o"),
        ("h730_p_ge_500", "2Y P(SOL ≥ $500)", "#b36905", "s"),
        ("h730_p_ge_800", "2Y P(SOL ≥ $800)", "#9b3b8b", "^"),
        ("h180_p_ge_200", "6M P(SOL ≥ $200)", "#187e70", "x"),
        ("h180_p_ge_300", "6M P(SOL ≥ $300)", "#777777", "+"),
    )
    for key, label, color, marker in series:
        axis.scatter(dates, [_number(row.get(key)) for row in rows], label=label,
                     color=color, marker=marker, s=43, alpha=0.88)
    axis.set_ylim(0, 100)
    _style_axis(axis, "Empirical analog frequency (%)")
    _date_axis(axis, dates)
    axis.set_title("SOL Long-Term Cone — Probability History", loc="left", fontsize=17, pad=35, fontweight="bold")
    axis.text(0, 1.045, "LOG_ROBUST_TAIL · Real daily observations only · DIAGNOSTIC ONLY",
              transform=axis.transAxes, color="#506479")
    axis.legend(loc="best", frameon=False, ncol=2, fontsize=9)
    figure.tight_layout()
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
        "Solo osservazioni reali; i marker non interpolano giorni mancanti.", "",
        "## Probability history", "", "![SOL Long-Term Cone — Probability History](sol_long_term_probability_history.png)", "",
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
