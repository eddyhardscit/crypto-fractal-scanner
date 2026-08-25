import inspect
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path
from unittest import mock

import numpy as np
import pandas as pd

import btc_2022_vs_sol_2026_report as report
import global_confluence_report as confluence


class SolReportPriceContextTests(unittest.TestCase):
    def _split(self, *, days=10, average_gap=5.0, adherence=90.0):
        return {
            "live_program": {
                "days_checked": days,
                "avg_abs_gap_pct": average_gap,
                "simple_alignment_score": adherence,
            }
        }

    def _anchor(self, price=94.05, timestamp="2026-08-24T05:30:23Z"):
        return {
            "price": price,
            "timestamp": timestamp,
            "symbol": "SOL-USD",
            "provider": "Yahoo Finance daily shared snapshot",
            "field": "Close",
            "timeframe": "1d",
            "completed": False,
            "reproducible": True,
            "purpose": "MODEL_INPUT",
        }

    def _reference(self, price=101.27, timestamp="2026-08-25T05:14:00Z"):
        return {
            "available": True,
            "price": price,
            "timestamp": timestamp,
            "acquired_at": "2026-08-25T05:14:01Z",
            "symbol": "SOL-USD",
            "provider": "Yahoo Finance",
            "field": "Close",
            "timeframe": "1m",
            "purpose": "DISPLAY_ONLY",
        }

    def test_price_adherence_pass_never_emits_failure_label(self):
        verdict = report.build_operational_verdict(
            {"structural_similarity": 80.0}, self._split(average_gap=5.0), 4.0
        )
        self.assertFalse(report.price_adherence_failed(verdict))
        self.assertNotIn("prezzo non aderente", report.verdict_status_text(verdict).lower())

    def test_explicit_price_adherence_failure_emits_canonical_reason(self):
        split = self._split(average_gap=16.0, adherence=68.0)
        verdict = report.build_operational_verdict(
            {"structural_similarity": 70.0}, split, 19.0
        )
        metadata = report.build_verdict_metadata(verdict, split, 19.0)
        self.assertTrue(report.price_adherence_failed(verdict))
        self.assertIn("PREZZO NON ADERENTE", report.verdict_status_text(verdict))
        self.assertEqual(15.0, metadata["price_adherence_live_avg_gap_threshold_pct"])
        self.assertEqual(18.0, metadata["price_adherence_last_gap_threshold_pct"])
        self.assertEqual(16.0, metadata["price_adherence_observed_live_avg_gap_pct"])
        self.assertEqual(19.0, metadata["price_adherence_observed_last_gap_pct"])
        rendered = report.build_verdict_metadata_block(verdict, split, 19.0)
        self.assertIn("PRICE_ADHERENCE_FAILED=YES", rendered)
        self.assertIn("PRICE_ADHERENCE_LIVE_AVG_GAP_THRESHOLD_PCT=15.0", rendered)

    def test_zero_weight_for_weak_structure_reports_actual_reason(self):
        verdict = report.build_operational_verdict(
            {"structural_similarity": 60.0}, self._split(average_gap=4.0), 3.0
        )
        self.assertEqual(0, verdict["operational_weight"])
        self.assertIn("ANALOGIA DEBOLE", report.verdict_status_text(verdict))
        self.assertNotIn("PREZZO NON ADERENTE", report.verdict_status_text(verdict))
        summary, rows = report.build_operational_plan(
            94.05,
            {"confirm_1": 100, "confirm_2": 110, "soft_invalid": 85, "hard_invalid": 75},
            verdict,
            {"label": "FRATTALE SOLO DI CONTESTO"},
            self._split(average_gap=4.0),
            3.0,
        )
        rendered = summary + str(rows)
        self.assertIn("ANALOGIA DEBOLE", rendered)
        self.assertNotIn("prezzo resta non aderente", rendered.lower())

    def test_multiple_failures_report_weak_structure_and_explicit_price_gap(self):
        split = self._split(average_gap=14.4, adherence=71.0)
        verdict = report.build_operational_verdict(
            {"structural_similarity": 63.5}, split, 19.2
        )
        metadata = report.build_verdict_metadata(verdict, split, 19.2)
        verdict.update(metadata)
        status = report.verdict_status_text(verdict)
        self.assertIn("ANALOGIA DEBOLE", status)
        self.assertIn("PREZZO NON ADERENTE", status)
        self.assertFalse(metadata["price_adherence_live_avg_gap_failed"])
        self.assertTrue(metadata["price_adherence_last_gap_failed"])

    def test_computational_anchor_preserves_shared_snapshot_value(self):
        snapshot = {
            "ticker": "SOL-USD",
            "price": 94.05,
            "close": 94.05,
            "candle_date_utc": "2026-08-24",
            "generated_at_utc": "2026-08-24T05:30:23Z",
            "source": "Yahoo Finance daily shared snapshot",
        }
        with mock.patch.object(report, "snapshot_record", return_value=snapshot):
            anchor = report.build_computational_anchor(94.05, pd.Timestamp("2026-08-24"))
        self.assertEqual(94.05, anchor["price"])
        self.assertEqual("2026-08-24T05:30:23Z", anchor["timestamp"])
        self.assertEqual("Close", anchor["field"])
        self.assertTrue(anchor["reproducible"])
        self.assertFalse(anchor["completed"])

    def test_public_reference_does_not_replace_projection_anchor(self):
        btc_path = pd.DataFrame(
            {"norm": [100.0, 110.0]},
            index=pd.date_range("2022-11-21", periods=2, freq="D"),
        )
        projection = report.make_daily_projection_path(
            btc_path,
            94.05,
            pd.Timestamp("2026-08-24"),
            0,
            1.25,
            max_days=1,
        )
        context = report.build_price_context(
            self._anchor(), self._reference(101.27), report_generated_at="2026-08-25T05:32:23Z"
        )
        self.assertEqual(94.05, projection.iloc[0]["base_price"])
        self.assertEqual(94.05, projection.iloc[0]["beta_price"])
        self.assertEqual(101.27, context["current_reference"]["price"])

    def test_public_reference_provenance_and_utc_timestamp_are_displayed(self):
        frame = pd.DataFrame(
            {"Close": [101.27]},
            index=pd.DatetimeIndex(["2026-08-25T07:14:00+02:00"]),
        )
        downloader = mock.Mock(return_value=frame)
        reference = report.fetch_current_public_reference(
            downloader=downloader, acquired_at="2026-08-25T05:14:01Z"
        )
        self.assertTrue(reference["available"])
        self.assertEqual(101.27, reference["price"])
        self.assertEqual("2026-08-25T05:14:00Z", reference["timestamp"])
        self.assertEqual("Yahoo Finance", reference["provider"])
        self.assertEqual("SOL-USD", reference["symbol"])
        kwargs = downloader.call_args.kwargs
        self.assertEqual("1m", kwargs["interval"])
        self.assertNotIn("api_key", kwargs)

    def test_anchor_age_and_positive_gap_are_exact(self):
        context = report.build_price_context(
            self._anchor(), self._reference(), report_generated_at="2026-08-25T05:32:23Z"
        )
        self.assertEqual(86520.0, context["anchor_age_seconds"])
        self.assertAlmostEqual(24.0333333333, context["anchor_age_hours"])
        self.assertAlmostEqual(7.22, context["current_vs_anchor_gap_usd"])
        self.assertAlmostEqual((101.27 / 94.05 - 1) * 100, context["current_vs_anchor_gap_pct"])
        self.assertEqual("STALE_FOR_CURRENT_DISPLAY", context["current_display_freshness"])

    def test_unavailable_quote_fails_gracefully_and_anchor_is_unchanged(self):
        def unavailable(*args, **kwargs):
            raise RuntimeError("offline")

        reference = report.fetch_current_public_reference(
            downloader=unavailable, acquired_at="2026-08-25T05:14:01Z"
        )
        context = report.build_price_context(
            self._anchor(), reference, report_generated_at="2026-08-25T05:32:23Z"
        )
        block = report.build_price_context_block(context)
        self.assertFalse(reference["available"])
        self.assertEqual(94.05, context["anchor"]["price"])
        self.assertIsNone(context["current_vs_anchor_gap_usd"])
        self.assertIn("CURRENT_PUBLIC_REFERENCE_PRICE=UNAVAILABLE", block)
        self.assertIn("COMPUTATIONAL_ANCHOR_PRICE=94.05", block)

    def test_price_context_renders_equal_positive_and_negative_gaps(self):
        for current in (94.05, 120.0, 70.0):
            with self.subTest(current=current):
                context = report.build_price_context(
                    self._anchor(),
                    self._reference(current),
                    report_generated_at="2026-08-24T06:30:23Z",
                )
                block = report.build_price_context_block(context)
                self.assertIn("SOL PRICE CONTEXT", block)
                self.assertIn("CURRENT_VS_ANCHOR_GAP_USD=", block)
                self.assertIn("CURRENT_VS_ANCHOR_GAP_PCT=", block)
                self.assertIn("COMPUTATIONAL_ANCHOR_TIMESTAMP=2026-08-24T05:30:23Z", block)

    def test_projection_title_separates_anchor_from_public_reference(self):
        verdict = {"label": "ANALOGIA DEBOLE / SCENARIO SECONDARIO", "operational_weight": 0}
        context = report.build_price_context(
            self._anchor(), self._reference(), report_generated_at="2026-08-25T05:32:23Z"
        )
        title = report.projection_chart_title(verdict, context)
        self.assertIn("Anchor modello", title)
        self.assertIn("Riferimento pubblico", title)
        self.assertIn("Yahoo Finance daily shared snapshot", title)
        self.assertIn("Età 24h 2m", title)
        self.assertIn("ANALOGIA DEBOLE", title)
        self.assertNotIn("prezzo non aderente", title.lower())

    def test_normalized_overlay_remains_base_100_and_explicitly_not_usd(self):
        source = inspect.getsource(report.generate_fractal_chart)
        self.assertIn("Prezzo normalizzato a 100", source)
        self.assertIn("indice; non USD", source)
        self.assertNotIn("set_ylabel(\"Prezzo SOL (USD)\")", source)
        prices = pd.DataFrame(
            {"Close": [62.0, 93.0]}, index=pd.date_range("2026-06-06", periods=2, freq="D")
        )
        normalized = report.normalize_path(prices, prices.index[0], 62.0)
        self.assertEqual(100.0, normalized.iloc[0]["norm"])
        self.assertEqual(150.0, normalized.iloc[1]["norm"])
        self.assertNotEqual(150.0, normalized.iloc[1]["Close"])

    def test_base_cycle_remains_analog_and_non_operational(self):
        source = inspect.getsource(report.generate_single_cycle_chart)
        self.assertIn("SCENARIO ANALOGICO", source)
        self.assertIn("NON è una previsione live", source)
        self.assertIn("NON è un segnale di trading", source)

    def test_display_reference_requires_no_private_or_trading_api(self):
        source = inspect.getsource(report.fetch_current_public_reference).lower()
        for forbidden in ("api_key", "secret", "private", "place_order", "create_order"):
            self.assertNotIn(forbidden, source)
        self.assertIn("yf.download", source)
        self.assertEqual("DISPLAY_ONLY", report.fetch_current_public_reference(
            downloader=lambda *a, **k: pd.DataFrame(),
            acquired_at="2026-08-25T05:14:01Z",
        )["purpose"])

    def test_display_reference_change_does_not_change_verdict_or_projection(self):
        structural = {"structural_similarity": 60.0}
        split = self._split(average_gap=4.0)
        verdict_before = report.build_operational_verdict(structural, split, 3.0)
        verdict_after = report.build_operational_verdict(structural, split, 3.0)
        btc_path = pd.DataFrame(
            {"norm": [100.0, 95.0, 110.0]},
            index=pd.date_range("2022-11-21", periods=3, freq="D"),
        )
        model_before = report.make_daily_projection_path(
            btc_path, 94.05, pd.Timestamp("2026-08-24"), 0, 1.2, max_days=2
        )
        report.build_price_context(
            self._anchor(), self._reference(150.0), report_generated_at="2026-08-25T05:32:23Z"
        )
        model_after = report.make_daily_projection_path(
            btc_path, 94.05, pd.Timestamp("2026-08-24"), 0, 1.2, max_days=2
        )
        self.assertEqual(verdict_before, verdict_after)
        pd.testing.assert_frame_equal(model_before, model_after)

    @unittest.skipUnless(report.CHARTS_AVAILABLE, "matplotlib unavailable")
    def test_canonical_generator_renders_all_context_in_temporary_outputs(self):
        class FrozenDateTime(datetime):
            @classmethod
            def now(cls, tz=None):
                fixed = cls(2026, 8, 25, 5, 32, 23, tzinfo=timezone.utc)
                return fixed.astimezone(tz) if tz is not None else fixed.replace(tzinfo=None)

        btc_index = pd.date_range("2022-01-01", "2025-12-31", freq="D")
        sol_index = pd.date_range("2026-01-01", "2026-08-24", freq="D")
        btc = pd.DataFrame(
            {"Close": 16000.0 + np.linspace(0.0, 90000.0, len(btc_index))},
            index=btc_index,
        )
        sol = pd.DataFrame(
            {"Close": 60.0 + np.linspace(0.0, 34.05, len(sol_index))},
            index=sol_index,
        )
        sol_price = float(sol["Close"].iloc[-1])
        snapshot = {
            "ticker": "SOL-USD",
            "price": sol_price,
            "close": sol_price,
            "candle_date_utc": "2026-08-24",
            "generated_at_utc": "2026-08-24T05:30:23Z",
            "source": "Yahoo Finance daily shared snapshot",
        }
        reference = self._reference(101.27)

        with tempfile.TemporaryDirectory(prefix="legacy_sol_report_test_") as temp_name:
            temp = Path(temp_name)
            paths = {
                "REPORT_DIR": str(temp),
                "MAIN_REPORT_PATH": str(temp / "latest_report.md"),
                "REPORT_PATH": str(temp / "btc_report.md"),
                "CSV_PATH": str(temp / "metrics.csv"),
                "TRACKING_LOG_PATH": str(temp / "tracking.csv"),
                "FRACTAL_CHART_PATH": str(temp / "fractal.png"),
                "PROJECTION_CHART_PATH": str(temp / "projection.png"),
                "CYCLE_CHART_PATH": str(temp / "cycle.png"),
                "CYCLE_BASE_CHART_PATH": str(temp / "cycle_base.png"),
                "CYCLE_BETA_CHART_PATH": str(temp / "cycle_beta.png"),
                "CYCLE_LOG_CHART_PATH": str(temp / "cycle_log.png"),
                "TRACKING_CHART_PATH": str(temp / "tracking.png"),
            }
            (temp / "latest_report.md").write_text(
                "# Fixture\n\n<!-- DECISION_REPORT_END -->\n", encoding="utf-8"
            )

            def fake_download(ticker, start):
                return btc.copy() if ticker == "BTC-USD" else sol.copy()

            with (
                mock.patch.multiple(report, **paths),
                mock.patch.object(report, "download_close", side_effect=fake_download),
                mock.patch.object(report, "apply_snapshot_to_ohlcv", side_effect=lambda frame, ticker: frame),
                mock.patch.object(report, "snapshot_record", return_value=snapshot),
                mock.patch.object(report, "fetch_current_public_reference", return_value=reference),
                mock.patch.object(report, "datetime", FrozenDateTime),
            ):
                report.main()
                artifact_names = (
                    "btc_report.md",
                    "latest_report.md",
                    "metrics.csv",
                    "tracking.csv",
                    "fractal.png",
                    "projection.png",
                    "cycle_base.png",
                )
                first_run = {
                    name: (temp / name).read_bytes()
                    for name in artifact_names
                }
                report.main()
                second_run = {
                    name: (temp / name).read_bytes()
                    for name in artifact_names
                }

            dedicated = (temp / "btc_report.md").read_text(encoding="utf-8")
            latest = (temp / "latest_report.md").read_text(encoding="utf-8")
            for rendered in (dedicated, latest):
                self.assertIn("SOL PRICE CONTEXT", rendered)
                self.assertIn("COMPUTATIONAL_ANCHOR_PRICE=94.05", rendered)
                self.assertIn("CURRENT_PUBLIC_REFERENCE_PRICE=101.27", rendered)
                self.assertIn("base 100", rendered)
                self.assertIn("cenario analogico", rendered)
            self.assertTrue((temp / "projection.png").is_file())
            self.assertTrue((temp / "fractal.png").is_file())
            self.assertTrue((temp / "cycle_base.png").is_file())
            self.assertEqual(first_run, second_run)
            parsed = confluence.parse_sol_fractal_component(latest)
            self.assertEqual(2, parsed["score"])
            self.assertEqual(2.0, parsed["data"]["operational_weight"])
            metrics = pd.read_csv(temp / "metrics.csv")
            summary = metrics.loc[metrics["row_type"] == "summary"].iloc[0]
            self.assertEqual(94.05, summary["sol_current_price"])
            self.assertEqual(101.27, summary["current_public_reference_price"])


if __name__ == "__main__":
    unittest.main()
