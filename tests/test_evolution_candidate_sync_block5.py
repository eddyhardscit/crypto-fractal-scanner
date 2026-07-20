from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from evolution_core import MutationRecord, StrategyRecord, StrategyRegistry, StrategyStatus

import evolution_candidate_registry_sync as syncer


class CandidateSyncTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.repo = Path(self.tmp.name)
        (self.repo / "data/evolution").mkdir(parents=True)
        (self.repo / "reports").mkdir(parents=True)
        self.registry = StrategyRegistry(
            self.repo / "data/evolution/strategy_registry.json",
            self.repo / "data/evolution/evolution_history.json",
        )
        self.parent = StrategyRecord(
            family_id="combo_adaptive",
            name="SHADOW_BETA",
            version="1.0.0-legacy.2",
            status=StrategyStatus.SHADOW,
            strategy_id="parent-id",
            metadata={"legacy_profile_name": "SHADOW_BETA", "source_kind": "paper_portfolio"},
        )
        self.registry.register(self.parent)
        self.source = self.repo / "source.json"
        self.result = self.repo / "reports/result.json"

    def tearDown(self):
        self.tmp.cleanup()

    def payload(self):
        return {
            "paper_only": True,
            "automatic_promotions": 0,
            "automatic_retirements": 0,
            "live_modified": False,
            "orders_sent": False,
            "candidates": [{
                "strategy_id": "candidate-id",
                "family_id": "combo_adaptive",
                "name": "EVO_CAND_SHADOW_BETA",
                "version": "1.0.1-candidate.abc",
                "status": "CANDIDATE",
                "parent_id": "parent-id",
                "mutation": {
                    "parameter": "reward_risk",
                    "old_value": 1.5,
                    "new_value": 2.0,
                    "reason": "evidence",
                    "mutation_type": "single_parameter",
                    "created_at": "2026-07-19T00:00:00+00:00",
                },
                "created_by": "block5",
                "created_at": "2026-07-19T00:00:00+00:00",
                "metadata": {
                    "source_kind": "evolution_candidate",
                    "legacy_profile_name": "EVO_CAND_SHADOW_BETA",
                    "parent_portfolio": "SHADOW_BETA",
                },
            }],
        }

    def write(self, payload=None):
        self.source.write_text(json.dumps(payload or self.payload()), encoding="utf-8")

    def test_01_empty_missing_source_is_safe(self):
        result = syncer.sync(self.repo, self.source, self.result)
        self.assertEqual(result["created"], 0)
        self.assertTrue(result["success"])

    def test_02_registers_candidate(self):
        self.write()
        result = syncer.sync(self.repo, self.source, self.result)
        self.assertEqual(result["created"], 1)
        self.assertEqual(self.registry.get("candidate-id").status, StrategyStatus.CANDIDATE)

    def test_03_updates_parent_child_genealogy(self):
        self.write()
        syncer.sync(self.repo, self.source, self.result)
        parent = self.registry.get("parent-id")
        self.assertIn("candidate-id", parent.child_ids)

    def test_04_idempotent_second_sync(self):
        self.write()
        syncer.sync(self.repo, self.source, self.result)
        result = syncer.sync(self.repo, self.source, self.result)
        self.assertEqual(result["created"], 0)
        self.assertEqual(result["unchanged"], 1)

    def test_05_rejects_non_candidate_status(self):
        payload = self.payload()
        payload["candidates"][0]["status"] = "MASTER"
        self.write(payload)
        result = syncer.sync(self.repo, self.source, self.result)
        self.assertFalse(result["success"])

    def test_06_rejects_automatic_promotion_marker(self):
        payload = self.payload()
        payload["automatic_promotions"] = 1
        self.write(payload)
        with self.assertRaises(RuntimeError):
            syncer.sync(self.repo, self.source, self.result)

    def test_07_rejects_non_single_mutation(self):
        payload = self.payload()
        payload["candidates"][0]["mutation"]["mutation_type"] = "multi_parameter"
        self.write(payload)
        result = syncer.sync(self.repo, self.source, self.result)
        self.assertFalse(result["success"])

    def test_08_rejects_identity_conflict(self):
        self.write()
        syncer.sync(self.repo, self.source, self.result)
        payload = self.payload()
        payload["candidates"][0]["name"] = "OTHER_NAME"
        self.write(payload)
        result = syncer.sync(self.repo, self.source, self.result)
        self.assertFalse(result["success"])

    def test_09_parent_fallback_by_profile_name(self):
        payload = self.payload()
        payload["candidates"][0]["parent_id"] = "unknown-derived-id"
        self.write(payload)
        result = syncer.sync(self.repo, self.source, self.result)
        self.assertTrue(result["success"])
        self.assertEqual(self.registry.get("candidate-id").parent_id, "parent-id")

    def test_10_source_kind_is_candidate(self):
        self.write()
        syncer.sync(self.repo, self.source, self.result)
        record = self.registry.get("candidate-id")
        self.assertEqual(record.metadata["source_kind"], "evolution_candidate")


class SnapshotSourceTests(unittest.TestCase):
    def setUp(self):
        self.source = Path(__file__).resolve().parents[1] / "evolution_runtime_snapshot_remote_v3.py"
        self.text = self.source.read_text(encoding="utf-8")

    def test_11_candidate_source_constant_exists(self):
        self.assertIn('CANDIDATE_SOURCE = "evolution_candidate"', self.text)

    def test_12_candidate_profiles_are_mapped(self):
        self.assertIn('"evolution_candidate_profiles": candidate_profiles', self.text)

    def test_13_candidate_not_counted_as_standalone(self):
        self.assertIn(
            'not in {CURRENT_SOURCE, HISTORICAL_SOURCE, CANDIDATE_SOURCE}',
            self.text,
        )


if __name__ == "__main__":
    unittest.main()
