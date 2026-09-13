"""Dashboard verification: only supplied observations reach plots and tables."""
from copy import deepcopy
from datetime import date, timedelta
import math
from pathlib import Path
import tempfile
import unittest

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

    def test_multiple_snapshots_keep_real_dates_and_no_connecting_lines(self):
        rows = [observation("2026-09-01"), observation("2026-09-04", 4), observation("2026-09-13", 8)]
        before = deepcopy(rows)
        figure = dashboard._history_figure(rows)
        try:
            for axis in figure.axes:
                self.assertEqual(len(axis.lines), 0)
                self.assertEqual(len(axis.collections), 4)
                for collection in axis.collections:
                    self.assertEqual(len(collection.get_offsets()), 3)
                    self.assertEqual(len(set(collection.get_offsets()[:, 0].tolist())), 3)
        finally:
            plt.close(figure)
        with tempfile.TemporaryDirectory() as temporary:
            files = dashboard.render_dashboard(rows, rows[-1], temporary, rows[0]["generated_at"], rows[-1]["generated_at"])
            report = files[-1].read_text()
            self.assertIn("DAILY_ROWS=3", report)
            self.assertNotIn("| 2026-09-02 |", report)
        self.assertEqual(rows, before)

    def test_missing_values_are_omitted_from_points_and_not_zero_filled(self):
        row = observation()
        row["h730_p50"] = None
        row["h730_p_ge_300"] = ""
        row["h180_p75"] = float("nan")
        figure = dashboard._history_figure([row])
        try:
            self.assertTrue(np.ma.getmaskarray(figure.axes[2].collections[0].get_offsets())[0, 1])
        finally:
            plt.close(figure)
        report = dashboard._render_readme([row], row, row["generated_at"], row["generated_at"])
        latest_2y = next(line for line in report.splitlines() if line.startswith("| 2Y |"))
        self.assertIn("| 2Y | — |", latest_2y)
        self.assertIn("| — |", latest_2y)
        self.assertNotIn("nan", report.lower())
        self.assertNotIn("$0.00", report)

    def test_probability_axis_uses_percentage_source_scale(self):
        figure = dashboard._probability_figure([observation()])
        try:
            self.assertEqual(figure.axes[0].get_ylim(), (0.0, 100.0))
            self.assertEqual(figure.axes[0].collections[0].get_offsets()[0, 1], 20.0)
            self.assertEqual(len(figure.axes[0].lines), 0)
        finally:
            plt.close(figure)

    def test_current_plot_has_exact_horizons_bands_and_spot(self):
        row = observation()
        figure = dashboard._current_figure(row)
        try:
            axis = figure.axes[0]
            self.assertEqual(axis.get_xticks().tolist(), [90, 180, 365, 730])
            self.assertEqual(len(axis.collections), 2)
            self.assertEqual(axis.lines[0].get_ydata().tolist(), [row[f"h{h}_p50"] for h in (90, 180, 365, 730)])
            self.assertEqual(axis.lines[1].get_ydata(), [row["spot_sol"], row["spot_sol"]])
            self.assertIn("Current", axis.get_title(loc="left"))
        finally:
            plt.close(figure)

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
