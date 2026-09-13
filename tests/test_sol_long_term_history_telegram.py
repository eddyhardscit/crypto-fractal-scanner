"""Offline regression checks for the daily SOL summary and its observation trend."""

from __future__ import annotations

import ast
import copy
import hashlib
import importlib.util
import io
import json
import tempfile
import unittest
from contextlib import redirect_stdout
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from unittest.mock import patch

from sol_long_term_history import FIELDS, csv_bytes, read_daily_csv, recent_statistics


SUMMARY_FILE = Path(__file__).resolve().parents[1] / "deploy" / "sol_long_term_probability_cone_telegram.py"
if not SUMMARY_FILE.exists():
    SUMMARY_FILE = SUMMARY_FILE.parent.parent / "sol_long_term_probability_cone_telegram.py"
_spec = importlib.util.spec_from_file_location("sol_history_telegram_candidate", SUMMARY_FILE)
summary = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(summary)


def fixtures():
    report = {
        "current_price": 100.0,
        "generated_at_utc": "2026-09-13T08:00:00Z",
        "role": "DIAGNOSTIC_ONLY",
        "horizons": {},
    }
    current = {"cohort_sha256": "current", "horizons": {}}
    for horizon in (90, 180, 365, 730):
        report["horizons"][str(horizon)] = {
            "raw_episodes": 40,
            "distinct_assets": 12,
            "distributions": {"LOG_ROBUST_TAIL": {"final_return": {
                "implicit_sol_prices": {"p10": 50, "p25": 75, "p50": 100, "p75": 200, "p90": 300}}}},
            "empirical_price_threshold_probabilities": {"LOG_ROBUST_TAIL": {
                "p_sol_ge_200": 50, "p_sol_ge_300": 30, "p_sol_ge_500": 20, "p_sol_ge_800": 10}},
        }
        current["horizons"][str(horizon)] = {
            "log_robust_p50_price": 100, "p_ge_300": 30, "p_ge_500": 20}
    old = copy.deepcopy(current)
    old["cohort_sha256"] = "previous"
    return report, [old, current]


def rows_for(count, *, start=date(2026, 8, 15), price_step=1.0, probability_step=0.2):
    rows = []
    for index in range(count):
        day = start + timedelta(days=index)
        rows.append({
            "date_local": day.isoformat(), "generated_at": f"{day}T08:00:00Z",
            "cohort_sha256": "synthetic-test-cohort", "spot_sol": 90.0 + index,
            "h180_p50": 100.0 + index * price_step,
            "h365_p50": 200.0 + index * price_step,
            "h730_p50": 300.0 + index * price_step,
            "h730_p_ge_300": 40.0 + index * probability_step,
            "h730_p_ge_500": 20.0 + index * probability_step,
        })
    return rows


class HistoryRenderingTests(unittest.TestCase):
    def render(self, rows):
        return summary.render_message(*fixtures(), daily_rows=rows,
            now=datetime(2026, 9, 13, 10, tzinfo=timezone.utc))

    def test_seven_day_trend_uses_observation_asof_seven_days_earlier(self):
        message = self.render(rows_for(8))
        self.assertIn("📈 Trend 7 giorni", message)
        self.assertIn("6M p50: $100.00 → $107.00 (+7.0%)", message)
        self.assertIn("1Y p50: $200.00 → $207.00 (+3.5%)", message)
        self.assertIn("2Y p50: $300.00 → $307.00 (+2.3%)", message)
        self.assertIn("2Y P≥$300: 40.0% → 41.4% (+1.4 pp)", message)
        self.assertIn("2Y P≥$500: 20.0% → 21.4% (+1.4 pp)", message)
        self.assertNotIn("storico <7 giorni", message)

    def test_short_seven_day_history_uses_first_real_row(self):
        message = self.render(rows_for(3))
        self.assertIn("storico <7 giorni", message)
        self.assertIn("6M p50: $100.00 → $102.00 (+2.0%)", message)
        self.assertIn("2Y P≥$300: 40.0% → 40.4% (+0.4 pp)", message)

    def test_missing_calendar_days_are_not_interpolated(self):
        rows = rows_for(12)
        rows = [rows[0], rows[3], rows[7], rows[11]]
        message = self.render(rows)
        self.assertIn("6M p50: $103.00 → $111.00 (+7.8%)", message)
        self.assertIn("storico <30 giorni", message)

    def test_thirty_day_stability_uses_last_thirty_calendar_days(self):
        message = self.render(rows_for(35))
        self.assertIn("📊 Stabilità 30 giorni", message)
        self.assertIn("2Y p50:\nmediana $319.50\nrange $305.00–$334.00", message)
        self.assertIn("2Y P≥$300:\nmediana 43.9%\nrange 41.0%–46.8%", message)
        self.assertNotIn("storico <30 giorni", message)

    def test_short_thirty_day_history_uses_available_observations(self):
        message = self.render(rows_for(3))
        self.assertIn("storico <30 giorni", message)
        self.assertIn("2Y p50:\nmediana $301.00\nrange $300.00–$302.00", message)

    def test_status_classification_and_exact_boundaries(self):
        for p50_values, probability_values, expected in (
            ((100, 110), (40, 42), "STABLE"),
            ((90, 110), (40, 42), "CAUTION"),
            ((80, 120), (40, 42), "VOLATILE"),
            ((100, 110), (40, 50), "CAUTION"),
            ((100, 110), (40, 60), "VOLATILE"),
        ):
            with self.subTest(expected=expected, p50_values=p50_values, probability_values=probability_values):
                rows = rows_for(2)
                for row, price, probability in zip(rows, p50_values, probability_values):
                    row["h730_p50"] = price
                    row["h730_p_ge_300"] = probability
                self.assertEqual(expected, recent_statistics(rows)["drift_status"])
                self.assertIn(f"FORECAST_DRIFT_STATUS={expected}", self.render(rows))

    def test_missing_values_stay_unavailable(self):
        rows = rows_for(2)
        for row in rows:
            row["h730_p50"] = None
            row["h730_p_ge_300"] = None
        message = self.render(rows)
        self.assertIn("2Y p50: N/D → N/D (N/D)", message)
        self.assertIn("2Y p50:\nmediana N/D\nrange N/D–N/D", message)
        self.assertIn("FORECAST_DRIFT_STATUS=CAUTION", message)

    def test_empty_ledger_preserves_current_summary(self):
        message = self.render([])
        self.assertIn("6 mesi\np50: $100.00", message)
        self.assertIn("Storico giornaliero non disponibile.", message)
        self.assertIn("FORECAST_DRIFT_STATUS=CAUTION", message)

    def test_github_link_and_both_distinct_statuses(self):
        message = self.render(rows_for(3))
        self.assertIn("SCENARIO_TREND=STABLE", message)
        self.assertIn("FORECAST_DRIFT_STATUS=STABLE", message)
        self.assertTrue(message.endswith("🔗 Storico completo:\n"
            "https://github.com/eddyhardscit/crypto-fractal-scanner/blob/main/reports/sol_long_term_history/README.md"))

    def test_trend_observation_dates_disclose_actual_ledger_coverage(self):
        rows = rows_for(8, start=date(2026, 9, 5))
        message = self.render(rows)
        self.assertIn("📊 SOL LONG-TERM CONE — 13/09/2026", message)
        self.assertIn("Osservazioni: 2026-09-05 → 2026-09-12", message)
        self.assertNotIn("Osservazioni:", self.render([]))

    def test_render_has_no_network_state_credentials_or_file_access(self):
        with patch.object(summary.urllib.request, "urlopen", side_effect=AssertionError("network")), \
             patch.object(summary, "send_message", side_effect=AssertionError("send")), \
             patch.object(summary, "_load_env", side_effect=AssertionError("credentials")), \
             patch.object(summary, "load_state", side_effect=AssertionError("state")), \
             patch.object(summary, "read_daily_csv", side_effect=AssertionError("ledger read")), \
             patch.object(Path, "read_text", side_effect=AssertionError("file read")):
            self.assertIn("📈 Trend 7 giorni", self.render(rows_for(8)))

    def test_daily_csv_parsing_and_rendering_keep_missing_values(self):
        rows = rows_for(3)
        rows[0]["h730_p_ge_500"] = None
        complete = [{**dict.fromkeys(FIELDS), **row} for row in rows]
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "daily.csv"
            path.write_bytes(csv_bytes(complete, FIELDS))
            parsed = read_daily_csv(path)
        self.assertEqual(3, len(parsed))
        self.assertIsNone(parsed[0]["h730_p_ge_500"])
        self.assertEqual(rows[-1]["date_local"], parsed[-1]["date_local"])
        self.assertIn("2Y P≥$500: N/D → 20.4% (N/D)", self.render(parsed))

    def test_existing_report_and_history_parsing(self):
        report, history = fixtures()
        with tempfile.TemporaryDirectory() as directory:
            report_path, history_path = Path(directory) / "report.json", Path(directory) / "history.jsonl"
            report_path.write_text(json.dumps(report), encoding="utf-8")
            history_path.write_text("\n".join(json.dumps(row) for row in history) + "\n", encoding="utf-8")
            with patch.object(summary, "REPORT_PATH", report_path), patch.object(summary, "HISTORY_PATH", history_path):
                self.assertEqual((report, history), summary.load_inputs())


class SafetyRegressionTests(unittest.TestCase):
    def test_existing_send_state_and_credential_functions_are_byte_identical(self):
        source = Path(summary.__file__).read_text(encoding="utf-8")
        expected = {
            "_load_env": "43ca7a55e6b41ae92249e4fac0bfbac79ef1a3a606ec01269517638d93a98691",
            "send_message": "aaab106230bdc6d4b4006f16ea39d86fff1e6b1fc693c44798aa6e415b742166",
            "load_state": "1fb9bba9daaff1306651ccbd731dd9658252b8ce6db7b2956177c1ee4283fc37",
            "save_state": "14bce350397ba716500ee609905e30c55bc4ec09b36ed73b5f5e2d939d3aade0",
        }
        for node in ast.parse(source).body:
            if isinstance(node, ast.FunctionDef) and node.name in expected:
                self.assertEqual(expected.pop(node.name),
                    hashlib.sha256(ast.get_source_segment(source, node).encode()).hexdigest())
        self.assertEqual({}, expected)

    def test_main_dedup_and_send_path_ast_remain_unchanged(self):
        tree = ast.parse(Path(summary.__file__).read_text(encoding="utf-8"))
        main = next(node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == "main")
        daily_read = [node for node in main.body if isinstance(node, ast.Try)]
        self.assertEqual(1, len(daily_read))
        self.assertIn("read_daily_csv", ast.dump(daily_read[0]))
        main.body = [node for node in main.body if node not in daily_read]
        for node in ast.walk(main):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == "render_message":
                node.keywords = [keyword for keyword in node.keywords if keyword.arg != "daily_rows"]
        self.assertEqual("32ab6dc42a5572fb3ad4bd96aa21b61c33c9e8b5a29986410292067fcaac2e67",
            hashlib.sha256(ast.dump(main, include_attributes=False).encode()).hexdigest())

    def test_destination_and_credential_selection_are_unchanged(self):
        tree = ast.parse(Path(summary.__file__).read_text(encoding="utf-8"))
        credential = next(node for node in tree.body if isinstance(node, ast.Assign)
            and any(isinstance(target, ast.Name) and target.id == "CREDENTIAL_PATH" for target in node.targets))
        expected = ast.parse('CREDENTIAL_PATH = Path(os.getenv("CREDENTIALS_DIRECTORY", '
            '"/run/credentials/crypto-sol-long-term-cone-telegram.service")) / "telegram.env"').body[0]
        self.assertEqual(ast.dump(expected), ast.dump(credential))
        self.assertEqual(Path("/var/lib/crypto-sol-long-term-cone-telegram/state.json"), summary.STATE_PATH)

    def test_imports_do_not_include_statistical_model_or_execution_modules(self):
        tree = ast.parse(Path(summary.__file__).read_text(encoding="utf-8"))
        allowed = {"__future__", "argparse", "json", "math", "os", "tempfile", "urllib",
            "datetime", "pathlib", "typing", "zoneinfo", "sol_long_term_history"}
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                self.assertTrue(all(alias.name.split(".")[0] in allowed for alias in node.names))
            elif isinstance(node, ast.ImportFrom):
                self.assertIn(node.module.split(".")[0], allowed)

    def test_main_render_only_does_not_send_or_write_state(self):
        with patch("sys.argv", ["summary", "--force", "--render-only"]), \
             patch.object(summary, "load_inputs", return_value=fixtures()), \
             patch.object(summary, "load_state", return_value={}), \
             patch.object(summary, "read_daily_csv", return_value=rows_for(3)), \
             patch.object(summary, "send_message", side_effect=AssertionError("send")), \
             patch.object(summary, "save_state", side_effect=AssertionError("state write")), \
             redirect_stdout(io.StringIO()) as output:
            self.assertEqual(0, summary.main())
        self.assertIn(summary.LONG_TERM_HISTORY_URL, output.getvalue())

    def test_daily_dedup_unchanged_and_precedes_ledger_read(self):
        today = datetime.now(timezone.utc).astimezone(summary.LOCAL_ZONE).date().isoformat()
        with patch("sys.argv", ["summary"]), \
             patch.object(summary, "load_inputs", return_value=fixtures()), \
             patch.object(summary, "load_state", return_value={"last_local_date": today}), \
             patch.object(summary, "read_daily_csv", side_effect=AssertionError("ledger read")), \
             patch.object(summary, "send_message", side_effect=AssertionError("send")), \
             patch.object(summary, "save_state", side_effect=AssertionError("state write")), \
             redirect_stdout(io.StringIO()) as output:
            self.assertEqual(0, summary.main())
        self.assertEqual("SKIP_ALREADY_SENT_TODAY\n", output.getvalue())

    def test_test_message_dedup_remains_invariant(self):
        with patch("sys.argv", ["summary", "--test"]), \
             patch.object(summary, "load_inputs", return_value=fixtures()), \
             patch.object(summary, "load_state", return_value={"test_sent_at": "2026-09-01T10:00:00Z"}), \
             patch.object(summary, "read_daily_csv", side_effect=AssertionError("ledger read")), \
             patch.object(summary, "send_message", side_effect=AssertionError("send")), \
             redirect_stdout(io.StringIO()) as output:
            self.assertEqual(0, summary.main())
        self.assertEqual("SKIP_TEST_ALREADY_SENT\n", output.getvalue())

    def test_missing_or_corrupt_csv_does_not_break_existing_summary(self):
        for error in (FileNotFoundError("missing ledger"), ValueError("invalid ledger")):
            with self.subTest(error=type(error).__name__), \
                 patch("sys.argv", ["summary", "--force", "--render-only"]), \
                 patch.object(summary, "load_inputs", return_value=fixtures()), \
                 patch.object(summary, "load_state", return_value={}), \
                 patch.object(summary, "read_daily_csv", side_effect=error), \
                 patch.object(summary, "send_message", side_effect=AssertionError("send")), \
                 redirect_stdout(io.StringIO()) as output:
                self.assertEqual(0, summary.main())
            self.assertIn("6 mesi\np50: $100.00", output.getvalue())
            self.assertIn("Storico giornaliero non disponibile.", output.getvalue())


if __name__ == "__main__":
    unittest.main()
