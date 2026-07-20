from __future__ import annotations

from typing import Any, Dict, List, Optional

from .models import StrategyRecord, StrategyStatus
from .registry import StrategyRegistry


class StrategyFamilyManager:
    def __init__(self, registry: StrategyRegistry) -> None:
        self.registry = registry

    def family_tree(self, family_id: str) -> Dict[str, Any]:
        members = self.registry.by_family(family_id)
        by_id = {item.strategy_id: item for item in members}
        roots = [
            item for item in members
            if item.parent_id is None or item.parent_id not in by_id
        ]

        def node(item: StrategyRecord) -> Dict[str, Any]:
            children = [
                node(by_id[child_id])
                for child_id in item.child_ids
                if child_id in by_id
            ]
            return {
                "strategy_id": item.strategy_id,
                "name": item.name,
                "version": item.version,
                "status": item.status.value,
                "mutation": item.mutation.to_dict() if item.mutation else None,
                "children": children,
            }

        return {
            "family_id": family_id,
            "master": self.current_master(family_id).strategy_id
            if self.current_master(family_id)
            else None,
            "roots": [node(item) for item in roots],
        }

    def current_master(self, family_id: str) -> Optional[StrategyRecord]:
        masters = [
            item for item in self.registry.by_family(family_id)
            if item.status == StrategyStatus.MASTER
        ]
        if len(masters) > 1:
            raise RuntimeError(f"Family {family_id} has more than one MASTER")
        return masters[0] if masters else None
