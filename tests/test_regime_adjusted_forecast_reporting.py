import unittest
from pathlib import Path

import numpy as np
import pandas as pd

import market_regime_match_report as regime_report
import scanner_forecast_tracker as tracker


def match_rows(count, target="SOL-USD"):
    rows = []
    for index in range(count):
        rows.append(
            {
                "target": target,
                "similar_asset": f"ASSET{index}-USD",
                "start_date": f"2020-01-{index + 1:02d}",
                "end_date": f"2020-04-{index + 1:02d}",
                "similarity": 90.0 - index,
            }
        )
    return pd.DataFrame(rows)


class RegimeAdjustedSelectionTests(unittest.TestCase):
    @staticmethod
    def hierarchy_rows(full_count, asset_count, btc_count, total=10):
        frame = match_rows(total)
        frame["same_full_regime_as_today"] = False
        frame["same_asset_regime_as_today"] = False
        frame["same_btc_regime_as_today"] = False
        frame.loc[: full_count - 1, [
            "same_full_regime_as_today",
            "same_asset_regime_as_today",
            "same_btc_regime_as_today",
        ]] = True
        if asset_count > full_count:
            frame.loc[
                full_count : asset_count - 1,
                "same_asset_regime_as_today",
            ] = True
        if btc_count > full_count:
            btc_only_start = max(asset_count, full_count)
            needed = btc_count - full_count
            frame.loc[
                btc_only_start : btc_only_start + needed - 1,
                "same_btc_regime_as_today",
            ] = True
        return frame

    def select(self, regime, min_matches=5):
        return tracker.select_regime_adjusted_matches(
            regime.copy(),
            regime,
            "SOL-USD",
            min_matches=min_matches,
        )

    def test_full_regime_at_threshold_uses_full_group(self):
        regime = self.hierarchy_rows(5, 7, 8)
        selected, status = self.select(regime)
        self.assertEqual(status["selected_regime_group"], "SAME_BTC_AND_ASSET_REGIME")
        self.assertEqual(status["fallback_level"], "0_FULL_REGIME")
        self.assertEqual(status["selection_reason"], "FULL_REGIME_THRESHOLD_MET")
        self.assertEqual(len(selected), 5)

    def test_falls_back_to_same_asset_when_full_is_small(self):
        regime = self.hierarchy_rows(4, 6, 4)
        selected, status = self.select(regime)
        self.assertEqual(status["selected_regime_group"], "SAME_ASSET_REGIME")
        self.assertEqual(status["fallback_level"], "1_SAME_ASSET_FALLBACK")
        self.assertEqual(status["selection_reason"], "FALLBACK_TO_SAME_ASSET_REGIME")
        self.assertEqual(len(selected), 6)
        self.assertTrue(selected["same_asset_regime_as_today"].all())

    def test_falls_back_to_same_btc_when_stricter_groups_are_small(self):
        regime = self.hierarchy_rows(3, 4, 6)
        selected, status = self.select(regime)
        self.assertEqual(status["selected_regime_group"], "SAME_BTC_REGIME")
        self.assertEqual(status["fallback_level"], "2_SAME_BTC_FALLBACK")
        self.assertEqual(status["selection_reason"], "FALLBACK_TO_SAME_BTC_REGIME")
        self.assertEqual(len(selected), 6)
        self.assertTrue(selected["same_btc_regime_as_today"].all())

    def test_all_groups_below_threshold_are_insufficient(self):
        regime = self.hierarchy_rows(3, 4, 4)
        selected, status = self.select(regime)
        self.assertTrue(selected.empty)
        self.assertEqual(status["status"], "INSUFFICIENT_REGIME_MATCHES")
        self.assertEqual(status["selected_regime_group"], "NONE")
        self.assertEqual(status["selected_sample_size"], 0)

    def test_selected_cohort_is_not_a_union_of_fallback_groups(self):
        regime = self.hierarchy_rows(4, 6, 7)
        selected, status = self.select(regime)
        self.assertEqual(status["selected_regime_group"], "SAME_ASSET_REGIME")
        expected = set(
            regime.loc[
                regime["same_asset_regime_as_today"],
                "similar_asset",
            ]
        )
        self.assertEqual(set(selected["similar_asset"]), expected)
        self.assertFalse(
            selected["similar_asset"].isin(
                regime.loc[
                    ~regime["same_asset_regime_as_today"]
                    & regime["same_btc_regime_as_today"],
                    "similar_asset",
                ]
            ).any()
        )

    def test_raw_frame_and_raw_quantiles_are_unchanged_by_selection(self):
        raw = self.hierarchy_rows(4, 6, 7)
        raw_before = raw.copy(deep=True)
        values = pd.DataFrame({
            f"day_{day}": [float(day), float(day + 1)]
            for day in range(tracker.FORECAST_DAYS + 1)
        })
        quantiles_before = tracker.quantile_paths(values)
        self.select(raw)
        quantiles_after = tracker.quantile_paths(values)
        pd.testing.assert_frame_equal(raw, raw_before)
        pd.testing.assert_frame_equal(quantiles_before, quantiles_after)

    def test_market_annotation_persists_hierarchy_fields(self):
        enriched = self.hierarchy_rows(4, 6, 4)
        annotated = regime_report.annotate_regime_adjusted_selection(
            enriched,
            min_matches=5,
        )
        required = {
            "selected_regime_group",
            "full_regime_matches",
            "same_asset_regime_matches",
            "same_btc_regime_matches",
            "selected_sample_size",
            "minimum_required",
            "fallback_level",
            "selection_reason",
        }
        self.assertTrue(required.issubset(annotated.columns))
        self.assertEqual(annotated.iloc[0]["selected_regime_group"], "SAME_ASSET_REGIME")
        self.assertEqual(int(annotated["regime_adjusted_selected"].sum()), 6)

    def test_tracker_rejects_a_stale_regime_snapshot(self):
        raw = match_rows(5)
        regime = raw.copy()
        regime["same_full_regime_as_today"] = True
        regime["same_asset_regime_as_today"] = True
        regime["same_btc_regime_as_today"] = True
        regime["target_regime_snapshot_date"] = "2026-07-14"

        selected, status = tracker.select_regime_adjusted_matches(
            raw,
            regime,
            "SOL-USD",
            min_matches=5,
            expected_snapshot_date="2026-07-15",
        )
        self.assertTrue(selected.empty)
        self.assertEqual(status["status"], "STALE_REGIME_DATA")


class TailOutlierAuditTests(unittest.TestCase):
    def test_adjusted_audit_identifies_the_effective_selected_group(self):
        paths = match_rows(6)
        for day in range(tracker.FORECAST_DAYS + 1):
            paths[f"day_{day}"] = np.arange(6, dtype=float) + day
        audit = tracker.build_tail_outlier_audit(
            "SOL-USD",
            "REGIME_ADJUSTED",
            paths,
            selected_regime_group="SAME_ASSET_REGIME",
            fallback_level="1_SAME_ASSET_FALLBACK",
        )
        self.assertEqual(set(audit["selected_regime_group"]), {"SAME_ASSET_REGIME"})
        self.assertEqual(set(audit["fallback_level"]), {"1_SAME_ASSET_FALLBACK"})
        self.assertEqual(set(audit["cases_used"]), {6})

    def test_upper_outlier_and_leave_one_out_p90_impact_are_visible(self):
        paths = match_rows(6)
        terminal_returns = [0.0, 1.0, 2.0, 3.0, 4.0, 100.0]
        for day in range(tracker.FORECAST_DAYS + 1):
            paths[f"day_{day}"] = np.array(terminal_returns) * (
                day / tracker.FORECAST_DAYS
            )
        paths["regime_alignment"] = "RAW"

        audit = tracker.build_tail_outlier_audit(
            "SOL-USD",
            "RAW",
            paths,
        )
        outlier = audit[audit["similar_asset"] == "ASSET5-USD"].iloc[0]

        self.assertEqual(outlier["tail_side"], "UPPER_P90")
        self.assertTrue(bool(outlier["iqr_outlier"]))
        self.assertTrue(bool(outlier["is_tail_or_outlier"]))
        self.assertGreater(float(outlier["p90_impact_pct_points"]), 0.0)
        self.assertGreater(float(outlier["mean_impact_pct_points"]), 0.0)

    def test_report_and_csv_show_selected_group_and_fallback_reason(self):
        latest_rows = [
            {
                "asset": "SOL",
                "target_ticker": "SOL-USD",
                "snapshot_date": "2026-08-27",
                "current_price": 100.0,
                "direction": "SALITA",
                "positive_cases": 60.0,
                "q30": None,
                "chart_filename": None,
                "regime_adjusted_q30": None,
                "regime_adjusted_chart_filename": None,
                "regime_adjusted_status": {
                    "status": "AVAILABLE",
                    "reason": "FALLBACK_TO_SAME_ASSET_REGIME",
                    "selected_regime_group": "SAME_ASSET_REGIME",
                    "full_regime_matches": 4,
                    "same_asset_regime_matches": 6,
                    "same_btc_regime_matches": 4,
                    "selected_sample_size": 6,
                    "minimum_required": 5,
                    "fallback_level": "1_SAME_ASSET_FALLBACK",
                    "selection_reason": "FALLBACK_TO_SAME_ASSET_REGIME",
                },
                "input_snapshot": {},
            }
        ]
        report = tracker.build_report(
            "2026-08-27 12:00:00",
            latest_rows,
            pd.DataFrame(),
            pd.DataFrame(),
        )
        csv_frame = tracker.build_regime_adjusted_latest_frame(latest_rows)
        self.assertIn("selected_regime_group", csv_frame.columns)
        self.assertIn("selection_reason", csv_frame.columns)
        self.assertEqual(csv_frame.iloc[0]["selected_regime_group"], "SAME_ASSET_REGIME")
        self.assertEqual(
            csv_frame.iloc[0]["selection_reason"],
            "FALLBACK_TO_SAME_ASSET_REGIME",
        )
        self.assertIn("SAME_ASSET_REGIME", report)
        self.assertIn("FALLBACK_TO_SAME_ASSET_REGIME", report)
        self.assertIn("fallback meno stringente", report)


class WorkflowOrderingTests(unittest.TestCase):
    def test_regime_report_runs_before_forecast_tracker(self):
        workflow = (
            Path(__file__).resolve().parents[1] / ".github/workflows/daily.yml"
        ).read_text(encoding="utf-8")
        self.assertLess(
            workflow.index("python market_regime_match_report.py"),
            workflow.index("python scanner_forecast_tracker.py"),
        )


if __name__ == "__main__":
    unittest.main()
