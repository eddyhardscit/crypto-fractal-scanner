from __future__ import annotations

import ast
import unittest
from pathlib import Path


RUNNER = Path("paper_trading_runner.py")


class Block12CurrentScopeHotfixTests(unittest.TestCase):
    def test_01_runner_compiles(self):
        source = RUNNER.read_text(encoding="utf-8")
        ast.parse(source)

    def test_02_control_tower_uses_cycle_time(self):
        source = RUNNER.read_text(encoding="utf-8")
        expected = (
            "control_tower_result = run_control_tower_cycle(\n"
            "            summary=summary,\n"
            "            market_bundle=bundle,\n"
            "            when=cycle_time,\n"
            "        )"
        )
        self.assertIn(expected, source)

    def test_03_unbound_current_call_removed(self):
        source = RUNNER.read_text(encoding="utf-8")
        bad = (
            "control_tower_result = run_control_tower_cycle(\n"
            "            summary=summary,\n"
            "            market_bundle=bundle,\n"
            "            when=current,\n"
            "        )"
        )
        self.assertNotIn(bad, source)


if __name__ == "__main__":
    unittest.main()
