import hashlib
import json
import tempfile
import unittest
import os
import subprocess
from pathlib import Path
from unittest.mock import patch

import numpy as np
import pandas as pd

import forecast_provenance as fp
import bounce_after_drawdown_report as bounce
from bounce_after_drawdown_report import first_touch_day
from scanner_forecast_tracker import (
    combine_tracker_metrics_with_legacy_baseline, evaluate_forecast_history,
    freeze_tracker_legacy_baseline, tracker_replay_status_row,
    write_tracker_replay_status, TrackerRunMode,
)
from scanner_forecast_shadow_calibration import (
    combine_shadow_metrics_with_legacy_baseline, evaluate_shadow_history,
)
from scanner import evaluate_prediction_log, find_similar_patterns
import scanner as scanner_module
import scanner_forecast_tracker as tracker_module
import forecast_30d_history_report as history_30d


class ForecastProvenanceTests(unittest.TestCase):
    DEPLOYED_HARDENING_COMMIT = "1e3d164aca274d521775949826a504652a056418"

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        root = Path(self.temp.name) / "provenance"
        attrs = {"ROOT": root, "RAW_DIR": root / "raw_ohlc", "COHORT_DIR": root / "cohorts",
                 "RAW_INDEX": root / "raw_market_snapshots.jsonl",
                 "FORECAST_LOG": root / "forecast_versions.jsonl",
                 "EVALUATION_LOG": root / "evaluation_versions.jsonl",
                 "LATEST_DAILY": root / "forecast_latest_daily.csv"}
        self.patchers = [patch.object(fp, key, value) for key, value in attrs.items()]
        for item in self.patchers: item.start()

    def tearDown(self):
        for item in reversed(self.patchers): item.stop()
        self.temp.cleanup()

    @staticmethod
    def sample_ohlc(values=(100.0, 101.0, 102.0)):
        idx = pd.date_range("2026-01-01", periods=len(values), tz="UTC")
        return pd.DataFrame({"Open": values, "High": np.array(values) + 1,
                             "Low": np.array(values) - 1, "Close": values,
                             "Volume": [10] * len(values)}, index=idx)

    @staticmethod
    def freeze(frame, run="r1"):
        return fp.freeze_ohlc(frame, ticker="BTC-USD", source="test",
            downloaded_at_utc="2026-01-03T00:00:00Z", requested_interval="1d",
            requested_range="test-range", run_id=run, purpose="test")

    def test_raw_snapshot_is_content_addressed_and_vendor_changes_do_not_mutate_old(self):
        snapshot = self.freeze(self.sample_ohlc())
        old = fp.load_frozen_ohlc(snapshot)
        revised_snapshot = self.freeze(self.sample_ohlc((100.0, 999.0, 102.0)), "r2")
        self.assertNotEqual(revised_snapshot, snapshot)
        self.assertEqual(fp.load_frozen_ohlc(snapshot).loc[pd.Timestamp("2026-01-02"), "Close"], 101.0)
        self.assertTrue(old.equals(fp.load_frozen_ohlc(snapshot)))

    def test_first_forecast_rerun_and_previous_day_are_append_only(self):
        previous = {"prediction_date": "2025-12-31", "asset": "BTC-USD",
                    "forecast_id": "old", "generated_at_utc": "2025-12-31T23:00:00Z"}
        first = {"prediction_date": "2026-01-01", "asset": "BTC-USD",
                 "forecast_id": "f1", "generated_at_utc": "2026-01-01T01:00:00Z"}
        second = {**first, "forecast_id": "f2", "generated_at_utc": "2026-01-01T02:00:00Z"}
        fp.append_forecast(previous); fp.append_forecast(first)
        first_bytes = fp.FORECAST_LOG.read_bytes()
        fp.append_forecast(second)
        lines = fp.FORECAST_LOG.read_text().splitlines()
        self.assertEqual(len(lines), 3)
        self.assertTrue(fp.FORECAST_LOG.read_bytes().startswith(first_bytes))
        immutable = [json.loads(line) for line in lines]
        self.assertNotIn("official_daily", immutable[1])
        self.assertTrue(immutable[1]["official_daily_candidate"])
        latest = pd.read_csv(fp.LATEST_DAILY).sort_values("forecast_date")
        self.assertEqual(latest.forecast_id.tolist(), ["old", "f2"])
        self.assertTrue(latest.official_daily.all())

    def test_cohort_manifest_hash_and_quantiles_replay_exactly(self):
        matches = pd.DataFrame({"similar_asset": ["A", "B", "C"],
            "start_date": ["2020-01-01"] * 3, "end_date": ["2020-04-01"] * 3,
            "similarity": [99.0, 98.0, 97.0], "return_30d": [-10.0, 5.0, 20.0]})
        cohort_id, digest = fp.freeze_cohort(matches, target="BTC-USD", run_id="r", generated_at_utc="x")
        manifest = json.loads((fp.COHORT_DIR / f"{digest}.json").read_text())
        values = [row["return_30d"] for row in manifest["matches"]]
        self.assertTrue(np.allclose(np.percentile(values, [10, 25, 50, 75, 90]),
                                    np.percentile(matches.return_30d, [10, 25, 50, 75, 90])))
        self.assertEqual(cohort_id, f"sha256:{digest}")
        body = {k: manifest[k] for k in ["schema_version", "target", "cases_used", "matches"]}
        self.assertEqual(hashlib.sha256(fp.canonical_json(body)).hexdigest(), digest)
        quantiles = np.percentile(values, [10, 25, 50, 75, 90])
        original_quantiles = np.percentile(matches.return_30d, [10, 25, 50, 75, 90])
        self.assertTrue(np.allclose(quantiles, original_quantiles))
        positive_rate = np.mean(np.asarray(values) > 0) * 100
        original_positive_rate = (matches.return_30d > 0).mean() * 100
        self.assertEqual(positive_rate, original_positive_rate)
        direction = "RIALZISTA" if positive_rate >= 50 else "RIBASSISTA"
        original_direction = "RIALZISTA" if original_positive_rate >= 50 else "RIBASSISTA"
        self.assertEqual(direction, original_direction)

    @staticmethod
    def evaluation(**overrides):
        record = {"forecast_id": "f", "asset": "BTC-USD",
            "forecast_generated_at_utc": "2026-01-01T00:00:00Z", "forecast_date": "2026-01-01",
            "horizon_days": 1, "requested_target_date": "2026-01-02",
            "actual_candle_date": "2026-01-04", "on_or_after_shift_days": 2,
            "actual_close": 101.0, "raw_market_snapshot_id": "sha256:x",
            "raw_market_snapshot_sha256": "x", "p10": -10, "p25": -5, "p50": 0,
            "p75": 5, "p90": 10, "inside_p10_p90": True, "inside_p25_p75": True,
            "direction_forecast": "UP", "direction_result": "UP", "drawdown": -1,
            "max_gain": 2, "drawdown_classifications": {"inside": True},
            "max_gain_classifications": {"inside": True},
            "evaluation_generated_at_utc": "2026-01-04T00:00:00Z", "code_version": "test",
            "path_price_semantics": "CLOSE_ONLY_LEGACY_COMPATIBLE"}
        record.update(overrides); return record

    def test_evaluation_manifest_is_complete_integrity_checked_and_idempotent(self):
        snapshot = self.freeze(self.sample_ohlc())
        raw_hash = snapshot.split(":", 1)[1]
        first = fp.append_evaluation(self.evaluation(raw_market_snapshot_id=snapshot, raw_market_snapshot_sha256=raw_hash))
        second = fp.append_evaluation(self.evaluation(raw_market_snapshot_id=snapshot, raw_market_snapshot_sha256=raw_hash,
                                                      evaluation_generated_at_utc="later", code_version="later"))
        self.assertEqual(first, second)
        self.assertEqual(len(fp.EVALUATION_LOG.read_text().splitlines()), 1)
        self.assertEqual(first["on_or_after_shift_days"], 2)
        self.assertTrue(fp.EVALUATION_REQUIRED.issubset(first))
        self.assertEqual(fp.find_evaluation("f", 1, "2026-01-02"), first)

    def test_raw_index_is_idempotent_and_hash_change_is_new(self):
        one = self.freeze(self.sample_ohlc(), "r1")
        two = self.freeze(self.sample_ohlc(), "r2")
        three = self.freeze(self.sample_ohlc((100, 101, 103)), "r3")
        self.assertEqual(one, two); self.assertNotEqual(one, three)
        self.assertEqual(len(fp.RAW_INDEX.read_text().splitlines()), 2)

    def test_raw_index_identity_ignores_purpose(self):
        frame = self.sample_ohlc()
        first = fp.freeze_ohlc(frame, ticker="BTC-USD", source="test",
            downloaded_at_utc="one", requested_interval="1d", requested_range="r",
            run_id="one", purpose="generation")
        second = fp.freeze_ohlc(frame, ticker="BTC-USD", source="test",
            downloaded_at_utc="two", requested_interval="1d", requested_range="r",
            run_id="two", purpose="evaluation")
        self.assertEqual(first, second)
        self.assertEqual(len(fp.RAW_INDEX.read_text().splitlines()), 1)

    def test_content_collision_hard_fails(self):
        snapshot = self.freeze(self.sample_ohlc())
        path = fp.RAW_DIR / f"{snapshot.split(':', 1)[1]}.csv"
        path.chmod(0o644); path.write_text("corrupt")
        with self.assertRaisesRegex(RuntimeError, "CONTENT_ADDRESS_COLLISION"):
            self.freeze(self.sample_ohlc())

    def test_provenance_paths_do_not_follow_cwd(self):
        configured = fp.ROOT
        with tempfile.TemporaryDirectory() as elsewhere:
            previous = Path.cwd()
            try:
                os.chdir(elsewhere); self.freeze(self.sample_ohlc())
            finally:
                os.chdir(previous)
        self.assertTrue(fp.RAW_INDEX.is_relative_to(configured))

    def test_tracker_uses_frozen_evaluation_data_not_mutated_vendor_frame(self):
        snapshot = self.freeze(self.sample_ohlc((100.0, 101.0, 102.0)))
        history = pd.DataFrame([{
            "forecast_id": "f:1", "target_ticker": "BTC-USD", "asset": "BTC",
            "snapshot_date": "2026-01-01", "target_date": "2026-01-02",
            "horizon_day": 1, "current_price": 100.0,
            "p10_price": 90.0, "p25_price": 95.0, "p50_price": 100.0,
            "p75_price": 105.0, "p90_price": 110.0,
        }])
        mutable_vendor = {"BTC-USD": self.sample_ohlc((100.0, 999.0, 102.0))}
        result = evaluate_forecast_history(
            history, mutable_vendor, evaluation_snapshot_ids={"BTC-USD": snapshot}
        )
        self.assertEqual(result.iloc[0].controls, 1)
        self.assertAlmostEqual(result.iloc[0].avg_error_vs_p50_pct, 1.0)
        manifest = json.loads(fp.EVALUATION_LOG.read_text())
        self.assertEqual(manifest["drawdown_classifications"]["classification_status"], "NOT_AVAILABLE")
        self.assertEqual(manifest["max_gain_classifications"]["classification_status"], "NOT_AVAILABLE")

    def test_legacy_tracker_row_without_frozen_provenance_is_not_requeried(self):
        history = pd.DataFrame([{"target_ticker": "BTC-USD", "asset": "BTC",
            "snapshot_date": "2026-01-01", "target_date": "2026-01-02", "horizon_day": 1,
            "current_price": 100.0, "p10_price": 90.0, "p25_price": 95.0,
            "p50_price": 100.0, "p75_price": 105.0, "p90_price": 110.0}])
        result = evaluate_forecast_history(
            history, {"BTC-USD": self.sample_ohlc()}, evaluation_snapshot_ids={}
        )
        self.assertEqual(int(result.iloc[0].controls), 0)

    def test_certified_tracker_replay_reports_legacy_unfrozen_without_vendor(self):
        history = pd.DataFrame([{"target_ticker": "BTC-USD", "asset": "BTC",
            "snapshot_date": "2026-01-01", "target_date": "2026-01-02", "horizon_day": 1,
            "current_price": 100.0, "p10_price": 90.0, "p25_price": 95.0,
            "p50_price": 100.0, "p75_price": 105.0, "p90_price": 110.0}])
        with patch("scanner_forecast_tracker.yf.download", side_effect=RuntimeError("vendor down")) as vendor:
            result = evaluate_forecast_history(history, {}, certified_replay=True)
        self.assertEqual(vendor.call_count, 0)
        self.assertEqual(result.attrs["replay_status"], "HISTORICAL_RAW_DATA_NOT_FROZEN")
        self.assertEqual(result.attrs["legacy_unfrozen_rows"], 1)

    def test_normal_daily_status_uses_baseline_without_replay_error(self):
        with tempfile.TemporaryDirectory() as directory:
            status_path = Path(directory) / "tracker_replay_status.csv"
            write_tracker_replay_status(
                status_path, generated_at_utc="2026-01-01T00:00:00Z",
                mode=TrackerRunMode.NORMAL_DAILY,
                legacy_rows_without_snapshot=4743, evaluated_frozen_rows=0,
            )
            row = pd.read_csv(status_path).iloc[0]
        self.assertEqual(row.status, "NORMAL_DAILY")
        self.assertEqual(row.legacy_baseline_used, "YES")
        self.assertEqual(row.certified_replay_requested, "NO")
        self.assertEqual(int(row.legacy_rows_without_snapshot), 4743)
        self.assertNotEqual(row.status, "HISTORICAL_RAW_DATA_NOT_FROZEN")

    def test_certified_replay_status_is_fail_closed_and_mode_specific(self):
        row = tracker_replay_status_row(
            generated_at_utc="2026-01-01T00:00:00Z",
            mode=TrackerRunMode.CERTIFIED_REPLAY,
            legacy_rows_without_snapshot=4743, evaluated_frozen_rows=0,
        )
        self.assertEqual(row["status"], "HISTORICAL_RAW_DATA_NOT_FROZEN")
        self.assertEqual(row["certified_replay_requested"], "YES")

    def test_normal_daily_vendor_acquisition_freezes_new_evaluation_then_replays(self):
        index = pd.date_range("2026-01-01", periods=45, tz="UTC")
        frame = pd.DataFrame({"Open": np.arange(45) + 100.0,
                              "High": np.arange(45) + 101.0,
                              "Low": np.arange(45) + 99.0,
                              "Close": np.arange(45) + 100.0,
                              "Volume": [10] * 45}, index=index)
        with patch("scanner_forecast_tracker.yf.download", return_value=frame) as vendor:
            _, snapshots = tracker_module.download_price_data(
                ["BTC-USD"], run_id="normal-run",
                downloaded_at_utc="2026-02-15T00:00:00Z",
            )
        self.assertGreaterEqual(vendor.call_count, 1)
        snapshot = snapshots["BTC-USD"]
        history = pd.DataFrame([{
            "forecast_id": "normal:new:1", "generated_at_utc": "2026-01-01T00:00:00Z",
            "target_ticker": "BTC-USD", "asset": "BTC", "snapshot_date": "2026-01-01",
            "target_date": "2026-01-02", "horizon_day": 1, "current_price": 100.0,
            "p10_price": 90.0, "p25_price": 95.0, "p50_price": 100.0,
            "p75_price": 105.0, "p90_price": 110.0,
        }])
        first = evaluate_forecast_history(
            history, {}, evaluation_snapshot_ids={"BTC-USD": snapshot}
        )
        self.assertEqual(int(first.iloc[0].controls), 1)
        with patch("scanner_forecast_tracker.yf.download") as replay_vendor:
            replay = evaluate_forecast_history(history, {}, certified_replay=True)
        self.assertEqual(replay_vendor.call_count, 0)
        self.assertEqual(int(replay.iloc[0].controls), 1)

    def test_normal_daily_legacy_rows_never_query_vendor_or_emit_replay_error(self):
        legacy = pd.DataFrame([{"target_ticker": "BTC-USD", "asset": "BTC",
            "snapshot_date": "2026-01-01", "target_date": "2026-01-02", "horizon_day": 1,
            "current_price": 100.0, "p10_price": 90.0, "p25_price": 95.0,
            "p50_price": 100.0, "p75_price": 105.0, "p90_price": 110.0}])
        with patch("scanner_forecast_tracker.yf.download") as vendor:
            result = evaluate_forecast_history(legacy, {}, certified_replay=False)
        self.assertEqual(vendor.call_count, 0)
        self.assertEqual(int(result.iloc[0].controls), 0)
        self.assertEqual(result.attrs["replay_status"], "REPRODUCIBLE")

    def test_frozen_tracker_replay_needs_no_current_vendor_data(self):
        snapshot = self.freeze(self.sample_ohlc())
        history = pd.DataFrame([{"forecast_id": "frozen:1", "generated_at_utc": "2026-01-01T00:00:00Z",
            "target_ticker": "BTC-USD", "asset": "BTC", "snapshot_date": "2026-01-01",
            "target_date": "2026-01-02", "horizon_day": 1, "current_price": 100.0,
            "p10_price": 90.0, "p25_price": 95.0, "p50_price": 100.0,
            "p75_price": 105.0, "p90_price": 110.0}])
        evaluate_forecast_history(history, {"BTC-USD": self.sample_ohlc()},
                                  evaluation_snapshot_ids={"BTC-USD": snapshot})
        with patch("scanner_forecast_tracker.yf.download", side_effect=RuntimeError("vendor down")) as vendor:
            replay = evaluate_forecast_history(history, {}, certified_replay=True)
        self.assertEqual(vendor.call_count, 0)
        self.assertEqual(int(replay.iloc[0].controls), 1)
        self.assertEqual(replay.attrs["replay_status"], "REPRODUCIBLE")

    def test_legacy_baseline_23_plus_one_is_combined_mathematically(self):
        baseline = {"rows": [{"asset": "BTC", "target_ticker": "BTC-USD", "horizon": "30g",
            "horizon_day": 30, "controls": 23, "inside_p10_p90_hits": 23,
            "inside_p25_p75_hits": 20, "sum_abs_error_vs_p50": 230.0,
            "sum_signed_error_vs_p50": 115.0,
            "published_metrics": {"asset": "BTC", "target_ticker": "BTC-USD", "horizon": "30g",
                "horizon_day": 30, "controls": 23, "inside_p10_p90_pct": 100.0,
                "inside_p25_p75_pct": 20/23*100, "avg_abs_error_vs_p50_pct": 10.0,
                "avg_error_vs_p50_pct": 5.0}}]}
        new = pd.DataFrame([{"asset": "BTC", "target_ticker": "BTC-USD", "horizon": "30g",
            "horizon_day": 30, "controls": 1, "inside_p10_p90_pct": 0.0,
            "inside_p25_p75_pct": 0.0, "avg_abs_error_vs_p50_pct": 34.0,
            "avg_error_vs_p50_pct": -5.0}])
        result = combine_tracker_metrics_with_legacy_baseline(new, baseline).iloc[0]
        self.assertEqual(result.controls, 24)
        self.assertAlmostEqual(result.inside_p10_p90_pct, 23/24*100)
        self.assertAlmostEqual(result.avg_abs_error_vs_p50_pct, 264/24)
        self.assertAlmostEqual(result.avg_error_vs_p50_pct, 110/24)

    def test_legacy_baseline_manifest_is_aggregate_only(self):
        metrics = Path(self.temp.name) / "metrics.csv"; baseline_path = Path(self.temp.name) / "baseline.json"
        pd.DataFrame([{"asset":"BTC","target_ticker":"BTC-USD","horizon":"30g","horizon_day":30,
            "controls":23,"inside_p10_p90_pct":100.0,"inside_p25_p75_pct":50.0,
            "avg_abs_error_vs_p50_pct":10.0,"avg_error_vs_p50_pct":5.0}]).to_csv(metrics,index=False)
        manifest = freeze_tracker_legacy_baseline(metrics, baseline_path)
        self.assertEqual(manifest["provenance_type"], "LEGACY_AGGREGATE_BASELINE")
        self.assertEqual(manifest["raw_point_in_time_replay_available"], "NO")
        self.assertNotIn("forecast_id", json.dumps(manifest))

    def test_shadow_baseline_does_not_reset_controls(self):
        baseline = {"rows": [{"target_ticker":"BTC-USD","horizon_day":1,"controls":23,
            "sum_raw_abs_error":230.0,"sum_shadow_abs_error":184.0,"shadow_win_hits":12,
            "raw_wide_hits":20,"shadow_wide_hits":21,"raw_central_hits":15,"shadow_central_hits":16,
            "published_metrics":{"asset":"BTC","target_ticker":"BTC-USD","horizon":"1g","horizon_day":1,
                "active_out_of_sample_controls":23,"raw_mae_pct":10.0,"shadow_mae_pct":8.0}}]}
        new = pd.DataFrame([{"asset":"BTC","target_ticker":"BTC-USD","horizon":"1g","horizon_day":1,
            "active_out_of_sample_controls":1,"raw_mae_pct":34.0,"shadow_mae_pct":20.0,
            "shadow_win_rate_pct":100.0,"raw_p10_p90_coverage_pct":100.0,
            "shadow_p10_p90_coverage_pct":100.0,"raw_p25_p75_coverage_pct":0.0,
            "shadow_p25_p75_coverage_pct":100.0}])
        result = combine_shadow_metrics_with_legacy_baseline(new, baseline).iloc[0]
        self.assertEqual(result.active_out_of_sample_controls, 24)
        self.assertAlmostEqual(result.raw_mae_pct, 264/24)

    def test_frozen_shadow_replay_needs_no_current_vendor_data(self):
        snapshot = self.freeze(self.sample_ohlc()); digest = snapshot.split(":", 1)[1]
        fp.append_evaluation(self.evaluation(forecast_id="shadow:1",
            raw_market_snapshot_id=snapshot, raw_market_snapshot_sha256=digest,
            actual_close=101.0))
        history = pd.DataFrame([{"forecast_id":"shadow:1", "target_ticker":"BTC-USD",
            "snapshot_date":"2026-01-01", "generated_at_utc":"2026-01-01T00:00:00Z",
            "target_date":"2026-01-02", "horizon_day":1, "current_price":100.0,
            "calibration_active":1, "raw_p10_price":90.0, "raw_p25_price":95.0,
            "raw_p50_price":100.0, "raw_p75_price":105.0, "raw_p90_price":110.0,
            "shadow_p10_price":90.0, "shadow_p25_price":95.0, "shadow_p50_price":100.0,
            "shadow_p75_price":105.0, "shadow_p90_price":110.0}])
        with patch("scanner_forecast_tracker.yf.download", side_effect=RuntimeError("vendor down")) as vendor:
            result = evaluate_shadow_history(history, {}, certified_replay=True)
        self.assertEqual(vendor.call_count, 0)
        self.assertEqual(int(result.iloc[0].active_out_of_sample_controls), 1)
        self.assertEqual(result.attrs["replay_status"], "REPRODUCIBLE")

    def test_current_evaluation_freezes_then_replay_reuses_without_vendor(self):
        snapshot = self.freeze(self.sample_ohlc())
        row = {"prediction_date": "2026-01-01", "forecast_date": "2026-01-01",
            "generated_at_utc": "2026-01-01T00:00:00Z", "forecast_id": "daily:1",
            "raw_market_snapshot_id": snapshot, "asset": "BTC-USD", "current_price": 100.0,
            "verdict": "RIALZISTA", "evaluated": False, "return_p10_pct": 50,
            "return_p25_pct": 52, "return_p50_pct": 55, "return_p75_pct": 58,
            "return_p90_pct": 60, "drawdown_p10_pct": -10, "drawdown_p90_pct": 0,
            "max_gain_p10_pct": 0, "max_gain_p90_pct": 10,
            "scenario_median_30d": 100, "drawdown_avg_30d": 90, "max_gain_avg_30d": 110}
        # Use a one-day horizon date by moving the canonical forecast date back 29 days.
        row["prediction_date"] = "2025-12-03"; row["forecast_date"] = "2025-12-03"
        history = pd.DataFrame([row])
        with patch("scanner.yf.download") as vendor:
            first = evaluate_prediction_log(history.copy(), {}, {"BTC-USD": snapshot})
            second = evaluate_prediction_log(history.copy(), {}, {}, certified_replay=True)
        self.assertEqual(vendor.call_count, 0)
        self.assertTrue(bool(first.iloc[0].evaluated)); self.assertTrue(bool(second.iloc[0].evaluated))
        self.assertEqual(len(fp.EVALUATION_LOG.read_text().splitlines()), 1)
        manifest = json.loads(fp.EVALUATION_LOG.read_text())
        self.assertFalse(manifest["inside_p10_p90"])
        self.assertTrue(manifest["drawdown_classifications"]["inside_p10_p90"])
        self.assertTrue(manifest["max_gain_classifications"]["inside_p10_p90"])

    def test_legacy_unfrozen_certified_replay_fails_closed(self):
        row = pd.DataFrame([{"prediction_date": "2025-01-01", "asset": "BTC-USD", "evaluated": False}])
        with self.assertRaisesRegex(RuntimeError, "HISTORICAL_RAW_DATA_NOT_FROZEN"):
            evaluate_prediction_log(row, {}, {}, certified_replay=True)

    def test_strict_sequence_requires_later_candle(self):
        path = pd.Series([95.0, 111.0]); first = first_touch_day(path, 100.0, -5, "down")
        second = first_touch_day(path.iloc[first + 1:], 100.0, 10, "up")
        self.assertGreater(first + 1 + second, first)

    def test_strict_sequence_second_day_and_average_have_no_off_by_one(self):
        paths = {
            1: (100.0, pd.Series([95.0, 111.0])),
            2: (100.0, pd.Series([95.0, 96.0, 97.0, 111.0])),
        }
        matches = pd.DataFrame({"case": [1, 2]})
        with patch.object(bounce, "get_forward_path", side_effect=lambda row, data: paths[row["case"]]):
            result = bounce.summarize_sequence("TEST", matches, {}, 100, "bounce", -5, 10)
        self.assertEqual(result["second_hits_after_first"], 2)
        self.assertEqual(result["avg_days_to_first"], 0.0)
        self.assertEqual(result["avg_days_to_second"], 2.0)

    def test_match_selection_never_uses_an_outcome_beyond_available_data(self):
        index = pd.date_range("2020-01-01", periods=420, freq="D")
        def frame(offset):
            close = np.linspace(100 + offset, 200 + offset, len(index)) + np.sin(np.arange(len(index)))
            return pd.DataFrame({"Close": close, "rsi": 50 + np.sin(np.arange(len(index))),
                "dist_ma20": .01, "dist_ma50": .02, "drawdown": -.05}, index=index)
        matches = find_similar_patterns("BTC-USD", {"BTC-USD": frame(0), "ETH-USD": frame(5)})
        latest_safe_end = index[-61]
        self.assertTrue((pd.to_datetime(matches.end_date) <= latest_safe_end).all())

    def test_published_sol_sequence_values_unchanged(self):
        payload = subprocess.check_output([
            "git", "-c", f"safe.directory={Path.cwd()}", "show",
            f"{self.DEPLOYED_HARDENING_COMMIT}:reports/bounce_after_drawdown_metrics.csv",
        ], text=True)
        metrics = pd.read_csv(__import__("io").StringIO(payload))
        expected = {("bounce", -5, 10): 62.857142857142854, ("bounce", -5, 20): 40.0,
                    ("dump", 5, -5): 40.625, ("dump", 10, -5): 25.806451612903224}
        for (sequence, first, second), value in expected.items():
            row = metrics[(metrics.asset == "SOL-USD") & (metrics.sequence_type == sequence)
                          & (metrics.first_pct == first) & (metrics.second_pct == second)]
            self.assertEqual(len(row), 1); self.assertTrue(np.isclose(row.iloc[0].second_rate_after_first, value))

    def test_deployed_forecast_accuracy_invariants_unchanged(self):
        payload = subprocess.check_output([
            "git", "-c", f"safe.directory={Path.cwd()}", "show",
            f"{self.DEPLOYED_HARDENING_COMMIT}:reports/accuracy_report.csv",
        ], text=True)
        metrics = pd.read_csv(__import__("io").StringIO(payload)).set_index("asset")
        expected = {
            "BTC-USD": (86.95652173913044, 100.0),
            "SOL-USD": (100.0, 100.0),
            "DOGE-USD": (92.5925925925926, 93.33333333333333),
        }
        for asset, (direction, coverage) in expected.items():
            self.assertTrue(np.isclose(metrics.at[asset, "directional_accuracy_pct"], direction))
            self.assertTrue(np.isclose(metrics.at[asset, "return_inside_p10_p90_pct"], coverage))

    def test_legacy_paths_and_existing_columns_remain_compatible(self):
        self.assertEqual(scanner_module.PREDICTION_LOG_PATH, "reports/prediction_log.csv")
        self.assertEqual(tracker_module.HISTORY_PATH, "reports/scanner_forecast_history.csv")
        self.assertEqual(tracker_module.METRICS_PATH, "reports/scanner_forecast_tracker_metrics.csv")
        self.assertEqual(history_30d.HISTORY_CSV_PATH, "reports/forecast_30d_history.csv")
        required = {"prediction_date", "generated_at_utc", "asset", "verdict",
                    "positive_cases_30d", "return_p10_pct", "return_p90_pct"}
        self.assertTrue(required.issubset(pd.read_csv(scanner_module.PREDICTION_LOG_PATH, nrows=0).columns))
        tracker_required = {"snapshot_date", "target_ticker", "horizon_day", "p10_price", "p90_price"}
        self.assertTrue(tracker_required.issubset(pd.read_csv(tracker_module.HISTORY_PATH, nrows=0).columns))

    def test_forecast_30d_versions_are_idempotent_and_collision_safe(self):
        history_path = Path(self.temp.name) / "forecast_30d_history.csv"
        versions_path = Path(self.temp.name) / "provenance" / "forecast_30d_versions.csv"
        row = {column: None for column in history_30d.COLUMNS}
        row.update({"forecast_date":"2026-01-01","target_date_30d":"2026-01-31",
                    "generated_at_utc":"2026-01-01T00:00:00Z","asset":"BTC",
                    "asset_name":"Bitcoin","current_price":100.0})
        with patch.object(history_30d, "HISTORY_CSV_PATH", str(history_path)), \
             patch.object(history_30d, "VERSIONS_CSV_PATH", str(versions_path)):
            history_30d.update_history([row]); history_30d.update_history([row])
            self.assertEqual(len(pd.read_csv(versions_path)), 1)
            changed = dict(row); changed["current_price"] = 101.0
            with self.assertRaisesRegex(RuntimeError, "IMMUTABLE_CSV_KEY_COLLISION"):
                history_30d.update_history([changed])

    def test_forecast_30d_automatic_owner_is_health_cycle(self):
        daily_override = Path("/etc/systemd/system/crypto-daily-scanner.service.d/health-watch.conf").read_text()
        health_service = Path("/etc/systemd/system/crypto-report-health.service").read_text()
        health_cycle = Path("/usr/local/sbin/crypto-report-health-cycle").read_text()
        self.assertIn("OnSuccess=crypto-report-health.service", daily_override)
        self.assertIn("ExecStart=/usr/local/sbin/crypto-report-health-cycle", health_service)
        self.assertIn('"$PYTHON" forecast_30d_history_report.py', health_cycle)

    def test_code_version_separates_commit_from_source_dirty_state(self):
        with tempfile.TemporaryDirectory() as directory:
            repo = Path(directory)
            subprocess.run(["git", "init", "-q"], cwd=repo, check=True)
            subprocess.run(["git", "config", "user.name", "test"], cwd=repo, check=True)
            subprocess.run(["git", "config", "user.email", "test@example.invalid"], cwd=repo, check=True)
            (repo / "reports").mkdir(); (repo / "scanner.py").write_text("VALUE = 1\n")
            (repo / "reports" / "runtime.csv").write_text("value\n1\n")
            subprocess.run(["git", "add", "."], cwd=repo, check=True)
            subprocess.run(["git", "commit", "-qm", "fixture"], cwd=repo, check=True)
            head = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=repo, text=True).strip()
            with patch.object(fp, "REPO_ROOT", repo):
                self.assertEqual(fp.code_version(), head)
                (repo / "reports" / "runtime.csv").write_text("value\n2\n")
                self.assertFalse(fp.source_worktree_dirty())
                self.assertEqual(fp.code_version(), head)
                (repo / "scanner.py").write_text("VALUE = 2\n")
                self.assertTrue(fp.source_worktree_dirty())
                self.assertEqual(fp.code_version(), head)


if __name__ == "__main__": unittest.main()
