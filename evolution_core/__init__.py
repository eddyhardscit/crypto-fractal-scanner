"""Core Evolution Framework for the crypto scanner.

Block 1 is deliberately read-only with respect to trading execution.
It provides identity, lifecycle, genealogy, persistence, events and
dynamic asset-universe observation.
"""

from .models import (
    AssetStatus,
    LifecycleEvent,
    MutationRecord,
    StrategyRecord,
    StrategyStatus,
)
from .registry import StrategyRegistry
from .lifecycle import StrategyLifecycleManager
from .family import StrategyFamilyManager
from .events import EventBus, EvolutionEvent
from .asset_universe import AssetUniverseManager

__all__ = [
    "AssetStatus",
    "LifecycleEvent",
    "MutationRecord",
    "StrategyRecord",
    "StrategyStatus",
    "StrategyRegistry",
    "StrategyLifecycleManager",
    "StrategyFamilyManager",
    "EventBus",
    "EvolutionEvent",
    "AssetUniverseManager",
]
