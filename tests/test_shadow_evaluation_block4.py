from __future__ import annotations

import csv
import json
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path
from unittest import mock

import paper_trading_shadow_evaluation as evaluation


def result_row(
    index: int,
    delta_r: float,
    *,
    full: bool = True,
    scenario: str = "GB30_R100",
    portfolio: str = "P1",
    strategy: str = "S1",
    asset: str = "BTC",
    ambiguous: int = 0,
    gaps: int = 0,
) -> dict[str, str]:
    risk = 100.0
    actual = 20.0
    delta = delta_r * risk
    closed = (
        datetime(2026, 1, 1, tzinfo=timezone.utc)
        + timedelta(hours=index)
    ).isoformat()
    quality = "FULL" if full else "PARTIAL"
    if ambiguous:
        quality += "_CONSERVATIVE_AMBIGUITY"
    if gaps:
        quality += "_WITH_GAPS"
    return {
        "scenario_set_version": "block3-v1-r-matrix",
        "scenario_id": scenario,
        "scenario_kind": "MFE_GIVEBACK",
        "scenario_parameters_json": "{}",
        "trade_key": f"{portfolio}:T{index}",
        "trade_id": f"T{index}",
        "portfolio": portfolio,
        "strategy": strategy,
        "asset": asset,
        "actual_closed_at": closed,
        "shadow_closed_at": closed,
        "full_from_entry": str(full),
        "result_quality": quality,
        "initial_risk_eur": str(risk),
        "actual_comparable_pnl_eur": str(actual),
        "shadow_comparable_pnl_eur": str(actual + delta),
        "delta_vs_actual_eur": str(delta),
        "same_candle_ambiguity_count": str(ambiguous),
        "candle_gap_count": str(gaps),
    }


class Block4EvaluationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.config = json.loads(
            json.dumps(evaluation.DEFAULT_CONFIG)
        )
        self.when = datetime(
            2026,
            7,
            19,
            tzinfo=timezone.utc,
        )

    def evaluate_all(self, rows):
        prepared = evaluation.prepare_rows(rows, self.config)
        groups = evaluation.group_rows(prepared, ["ALL"])
        self.assertEqual(len(groups), 1)
        key, grouped = next(iter(groups.items()))
        return evaluation.evaluate_group(
            key,
            grouped,
            self.config,
            evaluation.iso_utc(self.when),
        )

    def test_partial_samples_are_not_primary_evidence(self):
        rows = [
            result_row(i, 0.20, full=False)
            for i in range(150)
        ]
        row = self.evaluate_all(rows)
        self.assertEqual(row["sample_total"], 150)
        self.assertEqual(row["sample_eligible"], 0)
        self.assertEqual(row["sample_partial"], 150)
        self.assertEqual(row["status"], "INSUFFICIENT_DATA")

    def test_29_samples_are_insufficient(self):
        row = self.evaluate_all(
            [result_row(i, 0.10) for i in range(29)]
        )
        self.assertEqual(row["status"], "INSUFFICIENT_DATA")

    def test_30_samples_are_early_signal(self):
        row = self.evaluate_all(
            [result_row(i, 0.10) for i in range(30)]
        )
        self.assertEqual(row["status"], "EARLY_SIGNAL")

    def test_50_samples_are_validating(self):
        row = self.evaluate_all(
            [result_row(i, 0.10) for i in range(50)]
        )
        self.assertEqual(row["status"], "VALIDATING")

    def test_strong_100_sample_is_robust(self):
        rows = [
            result_row(i, 0.08 if i % 5 else -0.02)
            for i in range(100)
        ]
        row = self.evaluate_all(rows)
        self.assertEqual(row["status"], "ROBUST")
        self.assertFalse(row["eligible_for_mutation"])
        self.assertGreater(row["bootstrap_ci_low_delta_r"], 0)

    def test_strong_120_sample_is_eligible(self):
        rows = [
            result_row(i, 0.10 if i % 6 else -0.02)
            for i in range(120)
        ]
        row = self.evaluate_all(rows)
        self.assertEqual(
            row["status"],
            "ELIGIBLE_FOR_MUTATION",
        )
        self.assertTrue(row["eligible_for_mutation"])

    def test_consistently_negative_is_underperforming(self):
        rows = [
            result_row(i, -0.10 if i % 5 else -0.04)
            for i in range(120)
        ]
        row = self.evaluate_all(rows)
        self.assertEqual(row["status"], "UNDERPERFORMING")
        self.assertFalse(row["eligible_for_mutation"])

    def test_outlier_concentration_blocks_robustness(self):
        rows = [
            result_row(i, 0.01)
            for i in range(119)
        ]
        rows.append(result_row(119, 20.0))
        row = self.evaluate_all(rows)
        blockers = json.loads(row["blockers_json"])
        self.assertIn(
            "OUTLIER_CONCENTRATION_TOO_HIGH",
            blockers,
        )
        self.assertNotEqual(
            row["status"],
            "ELIGIBLE_FOR_MUTATION",
        )

    def test_latest_negative_fold_blocks_robustness(self):
        rows = []
        for i in range(90):
            rows.append(result_row(i, 0.15))
        for i in range(90, 120):
            rows.append(result_row(i, -0.20))
        row = self.evaluate_all(rows)
        blockers = json.loads(row["blockers_json"])
        self.assertIn(
            "LATEST_TEMPORAL_FOLD_NOT_POSITIVE",
            blockers,
        )

    def test_bootstrap_is_deterministic(self):
        values = [0.1, 0.2, -0.05, 0.3]
        first = evaluation.bootstrap_mean_interval(
            values,
            iterations=200,
            confidence=0.95,
            seed=123,
        )
        second = evaluation.bootstrap_mean_interval(
            values,
            iterations=200,
            confidence=0.95,
            seed=123,
        )
        self.assertEqual(first, second)

    def test_grouping_produces_required_scopes(self):
        rows = evaluation.prepare_rows(
            [
                result_row(
                    1,
                    0.10,
                    portfolio="P1",
                    strategy="S1",
                    asset="BTC",
                )
            ],
            self.config,
        )
        groups = evaluation.group_rows(
            rows,
            ["ALL", "PORTFOLIO", "STRATEGY", "ASSET"],
        )
        self.assertEqual(len(groups), 4)

    def test_candidate_payload_only_uses_allowed_scopes(self):
        base = {
            "eligible_for_mutation": True,
            "status": "ELIGIBLE_FOR_MUTATION",
            "scope_value": "X",
            "portfolio": "P1",
            "strategy": "S1",
            "asset": "BTC",
            "scenario_set_version": "v1",
            "scenario_id": "GB30",
            "scenario_kind": "MFE_GIVEBACK",
            "scenario_parameters_json": "{}",
            "sample_eligible": 120,
            "average_delta_r": 0.1,
            "median_delta_r": 0.08,
            "bootstrap_ci_low_delta_r": 0.03,
            "improved_pct": 60.0,
            "evidence_score": 85.0,
            "decision_summary": "ok",
        }
        rows = [
            {**base, "scope": "ALL"},
            {**base, "scope": "STRATEGY"},
        ]
        payload = evaluation.candidate_payload(
            rows,
            self.config,
            self.when,
        )
        self.assertEqual(payload["candidate_count"], 1)
        self.assertEqual(
            payload["candidates"][0]["scope"],
            "STRATEGY",
        )
        self.assertEqual(
            payload["automatic_mutations_created"],
            0,
        )

    def test_history_records_only_status_changes(self):
        state = {"evaluations": {}}
        row = {
            "scope": "ALL",
            "scope_value": "ALL",
            "scenario_set_version": "v1",
            "scenario_id": "GB30",
            "status": "EARLY_SIGNAL",
            "eligible_for_mutation": False,
            "sample_eligible": 30,
            "average_delta_r": 0.1,
            "median_delta_r": 0.1,
            "bootstrap_ci_low_delta_r": 0.02,
            "improved_pct": 60.0,
            "evidence_score": 40.0,
            "decision_summary": "early",
        }
        with tempfile.TemporaryDirectory() as temporary:
            history = Path(temporary) / "history.csv"
            with mock.patch.object(
                evaluation,
                "HISTORY_PATH",
                history,
            ):
                first = evaluation.append_history(
                    [row],
                    state,
                    self.when,
                )
                second = evaluation.append_history(
                    [row],
                    state,
                    self.when,
                )
        self.assertEqual(first, 1)
        self.assertEqual(second, 0)

    def test_cycle_with_no_results_is_safe_and_read_only(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            reports = root / "reports"
            config_dir = root / "config"
            reports.mkdir()
            config_dir.mkdir()
            patches = {
                "RESULTS_PATH": reports / "results.csv",
                "STATE_PATH": reports / "state.json",
                "EVALUATIONS_PATH": reports / "evaluations.csv",
                "HISTORY_PATH": reports / "history.csv",
                "CANDIDATES_PATH": reports / "candidates.json",
                "REPORT_PATH": reports / "report.md",
                "CONFIG_SNAPSHOT_PATH": reports / "config_snapshot.json",
                "CONFIG_PATH": config_dir / "config.json",
            }
            stack = [
                mock.patch.object(evaluation, name, value)
                for name, value in patches.items()
            ]
            for patch in stack:
                patch.start()
            try:
                result = evaluation.run_shadow_evaluation_cycle(
                    self.when
                )
            finally:
                for patch in reversed(stack):
                    patch.stop()

        self.assertEqual(result["status"], "OK")
        self.assertEqual(result["raw_results"], 0)
        self.assertEqual(result["eligible_for_mutation"], 0)
        self.assertFalse(result["paper_positions_modified"])
        self.assertFalse(result["paper_exits_modified"])
        self.assertEqual(result["mutations_created"], 0)


if __name__ == "__main__":
    unittest.main()
