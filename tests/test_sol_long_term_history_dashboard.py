"""Dashboard verification: only supplied observations reach plots and tables."""
from copy import deepcopy
from datetime import date, timedelta
import math
from pathlib import Path
import tempfile
import unittest

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np

import sol_long_term_history_dashboard as dashboard


def observation(day="2026-09-01", offset=0):
    row = {"date_local": day, "generated_at": f"{day}T06:00:00Z", "cohort_sha256": "a" * 64,
           "spot_sol": 82.0 + offset, "distinct_assets": 12, "raw_episode_count": 38,
           "canonical_cohort_count": 40, "h365_stability": "STABLE"}
    for horizon in (90, 180, 365, 730):
        for index, quantile in enumerate(("p10", "p25", "p50", "p75", "p90")):
            row[f"h{horizon}_{quantile}"] = 50 + 30 * index + horizon / 10 + offset
        for threshold in (150, 200, 250, 300, 400, 500, 600, 800, 1000):
            row[f"h{horizon}_p_ge_{threshold}"] = 20.0 + offset
    return row


class DashboardTests(unittest.TestCase):
    def assert_real_series(self, axis, gid, rows, key):
        """Every plotted vertex is a real observation; segments stop at gaps."""
        lines = [line for line in axis.lines if line.get_gid() == gid]
        actual = []
        for line in lines:
            self.assertIn(line.get_linestyle(), ("-", "--"))
            self.assertNotIn(line.get_marker(), (None, "", "None", "none", " "))
            xdata = np.asarray(line.get_xdata(orig=False), dtype=float)
            ydata = np.asarray(line.get_ydata(orig=False), dtype=float)
            self.assertTrue(np.isfinite(xdata).all())
            self.assertTrue(np.isfinite(ydata).all())
            for left, right in zip(xdata, xdata[1:]):
                self.assertEqual(right - left, 1, "a line crosses an unobserved day")
            actual.extend(zip(xdata.tolist(), ydata.tolist()))
        expected = []
        for row in rows:
            try:
                value = float(row.get(key))
            except (TypeError, ValueError):
                continue
            if math.isfinite(value):
                expected.append((mdates.date2num(date.fromisoformat(row["date_local"])), value))
        self.assertEqual(sorted(actual), sorted(expected))
        self.assertEqual(len(actual), len(set(actual)), "a real point was repeated")
        return lines

    def test_one_snapshot_has_all_figures_and_required_readme_sections(self):
        row = observation()
        with tempfile.TemporaryDirectory() as temporary:
            files = dashboard.render_dashboard([row], row, temporary, row["generated_at"], row["generated_at"])
            self.assertEqual([path.name for path in files], list(dashboard.OUTPUT_NAMES))
            for path in files[:3]:
                self.assertEqual(path.read_bytes()[:8], b"\x89PNG\r\n\x1a\n")
                self.assertGreater(path.stat().st_size, 1000)
            report = files[3].read_text()
            for section in ("Current cone", "Forecast history", "Probability history", "Latest snapshot",
                            "Recent drift", "30-day stability", "Methodology", "Data availability"):
                self.assertIn(f"## {section}", report)
            self.assertIn("DAILY_ROWS=1", report)
            self.assertIn("storico <7 giorni", report)
            self.assertIn("storico <30 giorni", report)
            self.assertIn("non dimostra stabilità temporale", report)

    def test_forecast_lines_markers_real_dates_and_all_panel_data(self):
        rows = [observation("2026-09-01"), observation("2026-09-02", 2),
                observation("2026-09-04", 4), observation("2026-09-13", 8)]
        before = deepcopy(rows)
        figure = dashboard._history_figure(rows)
        try:
            self.assertEqual(len(figure.axes), 3)
            for axis, (horizon, _) in zip(figure.axes, dashboard.HORIZONS):
                self.assertEqual(len(axis.collections), 0)
                for quantile in ("p50", "p75", "p90"):
                    lines = self.assert_real_series(axis, quantile, rows, f"h{horizon}_{quantile}")
                    self.assertEqual(sorted(len(line.get_ydata()) for line in lines), [1, 1, 2])
                self.assert_real_series(axis, "spot", rows, "spot_sol")
        finally:
            plt.close(figure)
        with tempfile.TemporaryDirectory() as temporary:
            files = dashboard.render_dashboard(rows, rows[-1], temporary, rows[0]["generated_at"], rows[-1]["generated_at"])
            report = files[-1].read_text()
            self.assertIn("DAILY_ROWS=4", report)
            self.assertNotIn("| 2026-09-03 |", report)
        self.assertEqual(rows, before)

    def test_forecast_hierarchy_distinct_spot_and_final_labels(self):
        rows = [observation("2026-09-01"), observation("2026-09-02", 4)]
        figure = dashboard._history_figure(rows)
        try:
            for axis, (horizon, _) in zip(figure.axes, dashboard.HORIZONS):
                lines = {line.get_gid(): line for line in axis.lines}
                self.assertGreater(lines["p50"].get_linewidth(), lines["p75"].get_linewidth())
                self.assertGreater(lines["p75"].get_linewidth(), lines["p90"].get_linewidth())
                self.assertEqual(lines["spot"].get_linestyle(), "--")
                self.assertLess(lines["spot"].get_linewidth(), lines["p50"].get_linewidth())
                self.assertNotEqual(lines["spot"].get_marker(), lines["p50"].get_marker())
                self.assertNotEqual(lines["spot"].get_color(), lines["p50"].get_color())
                texts = "\n".join(item.get_text() for item in axis.texts)
                for quantile in ("p50", "p75", "p90"):
                    self.assertIn(f"{quantile} ${rows[-1][f'h{horizon}_{quantile}']:,.2f}", texts)
                self.assertIn(f"SOL ${rows[-1]['spot_sol']:,.2f}", texts)
                self.assertIsNotNone(axis.get_legend())
        finally:
            plt.close(figure)

    def test_panel_scales_independent_no_clipped_real_values(self):
        rows = [observation("2026-09-01"), observation("2026-09-02", 2)]
        rows[1]["h730_p90"] = 1600
        figure = dashboard._history_figure(rows)
        try:
            self.assertEqual(len(set(axis.get_ylim() for axis in figure.axes)), 3)
            for axis, (horizon, _) in zip(figure.axes, dashboard.HORIZONS):
                for other in figure.axes:
                    if other is not axis:
                        self.assertFalse(axis.get_shared_y_axes().joined(axis, other))
                values = [row[key] for row in rows for key in
                          (f"h{horizon}_p50", f"h{horizon}_p75", f"h{horizon}_p90", "spot_sol")]
                lower, upper = axis.get_ylim()
                self.assertLess(lower, min(values))
                self.assertGreater(upper, max(values))
            self.assertLess(figure.axes[0].get_ylim()[1], 1600)
        finally:
            plt.close(figure)

    def test_panel_titles_show_exact_seven_day_p50_change(self):
        rows = [observation((date(2026, 9, 1) + timedelta(days=index)).isoformat(), index * 5)
                for index in range(10)]
        figure = dashboard._history_figure(rows)
        try:
            for axis, (horizon, label) in zip(figure.axes, dashboard.HORIZONS):
                title = " ".join(axis.get_title(loc=loc) for loc in ("left", "center", "right"))
                latest = rows[-1][f"h{horizon}_p50"]
                old = rows[2][f"h{horizon}_p50"]
                change = 100 * (latest / old - 1)
                self.assertIn(label, title)
                self.assertIn(f"Latest p50 ${latest:,.2f}", title)
                self.assertIn("7d", title)
                self.assertIn(f"{change:+.1f}%", title)
                self.assertNotIn("available history", title)
        finally:
            plt.close(figure)

    def test_short_history_title_uses_first_observation(self):
        rows = [observation("2026-09-03"), observation("2026-09-05", -3)]
        figure = dashboard._history_figure(rows)
        try:
            for axis, (horizon, _) in zip(figure.axes, dashboard.HORIZONS):
                title = " ".join(axis.get_title(loc=loc) for loc in ("left", "center", "right"))
                change = 100 * (rows[-1][f"h{horizon}_p50"] / rows[0][f"h{horizon}_p50"] - 1)
                self.assertIn("available history", title)
                self.assertIn(f"{change:+.1f}%", title)
        finally:
            plt.close(figure)

    def test_missing_values_omitted_without_zero_fill_or_connecting_across_them(self):
        rows = [observation("2026-09-01"), observation("2026-09-02", 2), observation("2026-09-03", 4)]
        rows[1]["h730_p50"] = None
        rows[1]["h730_p_ge_300"] = ""
        rows[1]["h180_p75"] = float("nan")
        for factory, pairs in (
            (dashboard._history_figure, ((2, "p50", "h730_p50"), (0, "p75", "h180_p75"))),
            (dashboard._probability_figure, ((0, "h730_p_ge_300", "h730_p_ge_300"),)),
        ):
            figure = factory(rows)
            try:
                for index, gid, key in pairs:
                    lines = self.assert_real_series(figure.axes[index], gid, rows, key)
                    self.assertEqual([len(line.get_ydata()) for line in lines], [1, 1])
            finally:
                plt.close(figure)
        row = rows[1]
        report = dashboard._render_readme([row], row, row["generated_at"], row["generated_at"])
        latest_2y = next(line for line in report.splitlines() if line.startswith("| 2Y |"))
        self.assertIn("| 2Y | — |", latest_2y)
        self.assertIn("| — |", latest_2y)
        self.assertNotRegex(report.lower(), r"\bnan\b")
        self.assertNotIn("$0.00", report)

    def test_single_missing_series_does_not_invent_point(self):
        row = observation()
        row["h730_p50"] = None
        row["h730_p_ge_300"] = None
        for factory, index, gid, key in (
            (dashboard._history_figure, 2, "p50", "h730_p50"),
            (dashboard._probability_figure, 0, "h730_p_ge_300", "h730_p_ge_300"),
        ):
            figure = factory([row])
            try:
                self.assert_real_series(figure.axes[index], gid, [row], key)
            finally:
                plt.close(figure)

    def test_probability_two_panels_percent_scale_lines_markers_end_labels(self):
        rows = [observation("2026-09-01"), observation("2026-09-02", 2), observation("2026-09-05", 4)]
        figure = dashboard._probability_figure(rows)
        try:
            self.assertEqual(len(figure.axes), 2)
            for axis, horizon, thresholds in ((figure.axes[0], 730, (300, 500, 800)),
                                               (figure.axes[1], 180, (200, 300))):
                self.assertEqual(axis.get_ylim(), (0.0, 100.0))
                self.assertEqual(len(axis.collections), 0)
                self.assertEqual({line.get_gid() for line in axis.lines},
                                 {f"h{horizon}_p_ge_{threshold}" for threshold in thresholds})
                texts = "\n".join(item.get_text() for item in axis.texts)
                for threshold in thresholds:
                    key = f"h{horizon}_p_ge_{threshold}"
                    self.assert_real_series(axis, key, rows, key)
                    self.assertIn(f"${threshold}: {rows[-1][key]:.1f}%", texts)
                self.assertIsNotNone(axis.get_legend())
        finally:
            plt.close(figure)

    def test_short_date_ticks_readable_madrid_display(self):
        rows = [observation((date(2026, 9, 3) + timedelta(days=index)).isoformat(), index) for index in range(11)]
        for factory in (dashboard._history_figure, dashboard._probability_figure):
            figure = factory(rows)
            try:
                figure.canvas.draw()
                axis = figure.axes[-1]
                labels = [tick.get_text() for tick in axis.get_xticklabels() if tick.get_text()]
                self.assertIn("03 Sep", labels)
                self.assertIn("13 Sep", labels)
                for label in labels:
                    self.assertRegex(label, r"^\d{2} [A-Z][a-z]{2}$")
                self.assertIn("Europe/Madrid", axis.get_xlabel())
            finally:
                plt.close(figure)

    def test_long_history_sparse_ticks_preserve_all_real_points(self):
        rows = [observation((date(2025, 1, 1) + timedelta(days=index)).isoformat(), index / 100)
                for index in range(400)]
        figure = dashboard._history_figure(rows)
        try:
            figure.canvas.draw()
            self.assertLessEqual(len(figure.axes[-1].get_xticks()), 14)
            for axis, (horizon, _) in zip(figure.axes, dashboard.HORIZONS):
                for quantile in ("p50", "p75", "p90"):
                    self.assert_real_series(axis, quantile, rows, f"h{horizon}_{quantile}")
                self.assert_real_series(axis, "spot", rows, "spot_sol")
        finally:
            plt.close(figure)

    def test_current_exact_horizons_bands_lines_spot_and_scales(self):
        row = observation()
        figure = dashboard._current_figure(row)
        try:
            axis = figure.axes[0]
            horizons = (90, 180, 365, 730)
            self.assertEqual(axis.get_xticks().tolist(), list(horizons))
            self.assertEqual(axis.get_xlim(), (70, 750))
            self.assertEqual(axis.get_xscale(), "linear")
            self.assertEqual(axis.get_yscale(), "linear")
            self.assertEqual(len(axis.collections), 2)
            for collection, low, high in ((axis.collections[0], "p10", "p90"),
                                          (axis.collections[1], "p25", "p75")):
                vertices = collection.get_paths()[0].vertices
                actual = set(map(tuple, vertices.tolist()))
                expected = {(float(h), float(row[f"h{h}_{q}"])) for h in horizons for q in (low, high)}
                self.assertEqual(actual, expected)
            self.assertEqual(axis.lines[0].get_xdata().tolist(), list(horizons))
            self.assertEqual(axis.lines[0].get_ydata().tolist(), [row[f"h{h}_p50"] for h in horizons])
            self.assertEqual(axis.lines[1].get_ydata(), [row["spot_sol"], row["spot_sol"]])
            self.assertIn("Current", axis.get_title(loc="left"))
        finally:
            plt.close(figure)

    def test_render_preserves_ledger_vintages_and_30_day_artifacts(self):
        rows = [observation("2026-09-01"), observation("2026-09-02", 2)]
        before_rows = deepcopy(rows)
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            protected = {
                root / "sol_long_term_daily_history.csv": b"date_local,spot_sol\n2026-09-01,82.0\n",
                root / "forecast_vintages.csv": b"forecast_date,target_date\n2026-09-01,2027-03-01\n",
                **{root / f"scanner_forecast_{symbol}.png": b"preserved existing image " + symbol.encode()
                   for symbol in ("BTC", "SOL", "DOGE")},
            }
            for path, contents in protected.items():
                path.write_bytes(contents)
            files = dashboard.render_dashboard(rows, rows[-1], root, rows[0]["generated_at"], rows[-1]["generated_at"])
            self.assertEqual(set(root.iterdir()), set(protected) | set(files))
            for path, contents in protected.items():
                self.assertEqual(path.read_bytes(), contents, str(path))
            first_current = files[0].read_bytes()
            dashboard.render_dashboard(rows, rows[-1], root, rows[0]["generated_at"], rows[-1]["generated_at"])
            self.assertEqual(files[0].read_bytes(), first_current)
        self.assertEqual(rows, before_rows)

    def test_readme_explains_quantiles_and_empirical_probabilities(self):
        row = observation()
        report = dashboard._render_readme([row], row, row["generated_at"], row["generated_at"])
        forecast = report.split("## Forecast history", 1)[1].split("## Probability history", 1)[0]
        probability = report.split("## Probability history", 1)[1].split("## Latest snapshot", 1)[0]
        for explanation in ("p50 = mediana degli analoghi", "p75 = 25% degli analoghi sopra questo livello",
                            "p90 = 10% degli analoghi sopra questo livello",
                            "SOL spot = prezzo osservato nel giorno dello snapshot"):
            self.assertIn(explanation, forecast)
        self.assertIn("frequenza empirica degli analoghi", probability)
        self.assertIn("all'orizzonte indicato", probability)

    def test_recent_table_has_last_seven_real_observations(self):
        rows = [observation((date(2026, 9, 1) + timedelta(days=index)).isoformat(), index) for index in range(10)]
        report = dashboard._render_readme(rows, rows[-1], rows[0]["generated_at"], rows[-1]["generated_at"])
        recent = report.split("## Recent drift\n", 1)[1].split("## 30-day stability", 1)[0]
        self.assertEqual(sum(line.startswith("| 2026-") for line in recent.splitlines()), 7)
        self.assertNotIn("| 2026-09-03 |", recent)
        self.assertIn("| 2026-09-04 |", recent)

    def test_empty_or_duplicate_observations_fail_before_writes(self):
        row = observation()
        with tempfile.TemporaryDirectory() as temporary:
            for rows in ([], [row, row]):
                with self.assertRaises(ValueError):
                    dashboard.render_dashboard(rows, row, temporary, "", "")
            self.assertEqual(list(Path(temporary).iterdir()), [])

    def test_no_model_or_network_imports(self):
        import ast
        source = Path(dashboard.__file__).read_text()
        tree = ast.parse(source)
        names = []
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                names.extend(item.name for item in node.names)
            elif isinstance(node, ast.ImportFrom):
                names.append(node.module or "")
        for forbidden in ("sol_long_term_probability_cone", "scanner_forecast_tracker", "requests", "yfinance", "urllib", "subprocess"):
            self.assertFalse(any(name == forbidden or name.startswith(forbidden + ".") for name in names), forbidden)


if __name__ == "__main__":
    unittest.main()
