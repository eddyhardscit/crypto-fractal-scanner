from __future__ import annotations

from typing import Dict, Set

from .events import EvolutionEvent
from .models import LifecycleEvent, StrategyStatus
from .registry import StrategyRegistry


_ALLOWED: Dict[StrategyStatus, Set[StrategyStatus]] = {
    StrategyStatus.CANDIDATE: {
        StrategyStatus.SHADOW,
        StrategyStatus.BACKGROUND,
        StrategyStatus.RETIRED,
    },
    StrategyStatus.SHADOW: {
        StrategyStatus.MASTER,
        StrategyStatus.BACKGROUND,
        StrategyStatus.RETIRED,
    },
    StrategyStatus.MASTER: {
        StrategyStatus.EX_MASTER,
    },
    StrategyStatus.EX_MASTER: {
        StrategyStatus.MASTER,
        StrategyStatus.BACKGROUND,
        StrategyStatus.RETIRED,
    },
    StrategyStatus.BACKGROUND: {
        StrategyStatus.SHADOW,
        StrategyStatus.RETIRED,
    },
    StrategyStatus.RETIRED: {
        StrategyStatus.BACKGROUND,
    },
}


class StrategyLifecycleManager:
    def __init__(self, registry: StrategyRegistry) -> None:
        self.registry = registry

    def transition(
        self,
        strategy_id: str,
        new_status: StrategyStatus,
        reason: str,
        metadata: dict | None = None,
    ):
        record = self.registry.get(strategy_id)
        old_status = record.status

        if new_status == old_status:
            return record
        if new_status not in _ALLOWED[old_status]:
            raise ValueError(
                f"Invalid lifecycle transition: {old_status.value} -> {new_status.value}"
            )

        if new_status == StrategyStatus.MASTER:
            self._demote_existing_master(record.family_id, replacement_id=strategy_id)

        record.status = new_status
        self.registry.save(record)

        event = LifecycleEvent(
            strategy_id=strategy_id,
            event_type="strategy_status_changed",
            old_status=old_status.value,
            new_status=new_status.value,
            reason=reason,
            metadata=metadata or {},
        )
        self.registry.history.append(event)
        self.registry.event_bus.publish(
            EvolutionEvent("strategy_status_changed", event.to_dict())
        )
        return record

    def _demote_existing_master(self, family_id: str, replacement_id: str) -> None:
        for current in self.registry.by_family(family_id):
            if current.status == StrategyStatus.MASTER and current.strategy_id != replacement_id:
                old_status = current.status
                current.status = StrategyStatus.EX_MASTER
                self.registry.save(current)
                event = LifecycleEvent(
                    strategy_id=current.strategy_id,
                    event_type="strategy_status_changed",
                    old_status=old_status.value,
                    new_status=StrategyStatus.EX_MASTER.value,
                    reason=f"replaced_by:{replacement_id}",
                )
                self.registry.history.append(event)
                self.registry.event_bus.publish(
                    EvolutionEvent("strategy_status_changed", event.to_dict())
                )
