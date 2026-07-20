import tempfile
import unittest
from pathlib import Path

from evolution_core import (
    AssetUniverseManager,
    MutationRecord,
    StrategyFamilyManager,
    StrategyLifecycleManager,
    StrategyRecord,
    StrategyRegistry,
    StrategyStatus,
)


class CoreEvolutionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        base = Path(self.temp.name)
        self.registry = StrategyRegistry(
            base / "strategy_registry.json",
            base / "evolution_history.json",
        )
        self.lifecycle = StrategyLifecycleManager(self.registry)

    def tearDown(self):
        self.temp.cleanup()

    def test_master_replacement_preserves_ex_master(self):
        first = self.registry.register(
            StrategyRecord(
                family_id="rapid",
                name="Rapid",
                version="1.0.0",
                status=StrategyStatus.SHADOW,
            )
        )
        second = self.registry.register(
            StrategyRecord(
                family_id="rapid",
                name="Rapid",
                version="1.1.0",
                status=StrategyStatus.SHADOW,
                parent_id=first.strategy_id,
                mutation=MutationRecord(
                    parameter="trailing_pct",
                    old_value=0.10,
                    new_value=0.12,
                    reason="test wider trailing",
                ),
            )
        )

        self.lifecycle.transition(first.strategy_id, StrategyStatus.MASTER, "initial")
        self.lifecycle.transition(second.strategy_id, StrategyStatus.MASTER, "promotion")

        self.assertEqual(
            self.registry.get(first.strategy_id).status,
            StrategyStatus.EX_MASTER,
        )
        self.assertEqual(
            self.registry.get(second.strategy_id).status,
            StrategyStatus.MASTER,
        )

    def test_family_tree_contains_child(self):
        parent = self.registry.register(
            StrategyRecord(
                family_id="combo",
                name="Combo",
                version="1.0.0",
                status=StrategyStatus.SHADOW,
            )
        )
        child = self.registry.register(
            StrategyRecord(
                family_id="combo",
                name="Combo",
                version="1.1.0",
                status=StrategyStatus.CANDIDATE,
                parent_id=parent.strategy_id,
            )
        )

        tree = StrategyFamilyManager(self.registry).family_tree("combo")
        child_ids = [item["strategy_id"] for item in tree["roots"][0]["children"]]
        self.assertIn(child.strategy_id, child_ids)

    def test_asset_universe_observation_mode_does_not_activate(self):
        base = Path(self.temp.name)
        manager = AssetUniverseManager(
            base / "asset_universe.json",
            allow_automatic_status_changes=False,
            activation_confirmations=2,
        )
        manager.observe("SOL-USDT", eligible=True, metrics={"volume": 1})
        record = manager.observe("SOL-USDT", eligible=True, metrics={"volume": 2})

        self.assertEqual(record.status.value, "WATCHLIST")
        latest = manager.latest_snapshot("SOL-USDT")
        self.assertEqual(latest["proposed_status"], "ACTIVE")

    def test_asset_universe_can_activate_when_enabled(self):
        base = Path(self.temp.name)
        manager = AssetUniverseManager(
            base / "asset_universe_enabled.json",
            allow_automatic_status_changes=True,
            activation_confirmations=2,
        )
        manager.observe("HYPE-USDT", eligible=True, metrics={})
        record = manager.observe("HYPE-USDT", eligible=True, metrics={})
        self.assertEqual(record.status.value, "ACTIVE")


if __name__ == "__main__":
    unittest.main()
