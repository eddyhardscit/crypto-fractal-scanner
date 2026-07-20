from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Iterable, List, Optional

from .events import EventBus, EvolutionEvent
from .history import EvolutionHistory
from .models import LifecycleEvent, StrategyRecord, StrategyStatus
from .storage import JsonStore


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


class StrategyRegistry:
    def __init__(
        self,
        registry_path: str | Path,
        history_path: str | Path,
        event_bus: EventBus | None = None,
    ) -> None:
        self._store = JsonStore(
            registry_path,
            default={"schema_version": 1, "strategies": {}},
        )
        self.history = EvolutionHistory(history_path)
        self.event_bus = event_bus or EventBus()

    def register(self, record: StrategyRecord) -> StrategyRecord:
        document = self._store.read()
        strategies = document.setdefault("strategies", {})
        if record.strategy_id in strategies:
            raise ValueError(f"Strategy id already registered: {record.strategy_id}")
        if record.parent_id and record.parent_id not in strategies:
            raise ValueError(f"Unknown parent strategy: {record.parent_id}")

        strategies[record.strategy_id] = record.to_dict()

        if record.parent_id:
            parent = StrategyRecord.from_dict(strategies[record.parent_id])
            if record.strategy_id not in parent.child_ids:
                parent.child_ids.append(record.strategy_id)
                parent.updated_at = utc_now_iso()
                strategies[parent.strategy_id] = parent.to_dict()

        self._store.write(document)
        event = LifecycleEvent(
            strategy_id=record.strategy_id,
            event_type="strategy_registered",
            old_status=None,
            new_status=record.status.value,
            reason="registration",
            metadata={"family_id": record.family_id, "version": record.version},
        )
        self.history.append(event)
        self.event_bus.publish(EvolutionEvent("strategy_registered", event.to_dict()))
        return record

    def get(self, strategy_id: str) -> StrategyRecord:
        strategies = self._store.read().get("strategies", {})
        try:
            return StrategyRecord.from_dict(strategies[strategy_id])
        except KeyError as exc:
            raise KeyError(f"Unknown strategy id: {strategy_id}") from exc

    def save(self, record: StrategyRecord) -> None:
        document = self._store.read()
        strategies = document.setdefault("strategies", {})
        if record.strategy_id not in strategies:
            raise KeyError(f"Unknown strategy id: {record.strategy_id}")
        record.updated_at = utc_now_iso()
        strategies[record.strategy_id] = record.to_dict()
        self._store.write(document)

    def list_all(self) -> List[StrategyRecord]:
        values = self._store.read().get("strategies", {}).values()
        return [StrategyRecord.from_dict(value) for value in values]

    def by_family(self, family_id: str) -> List[StrategyRecord]:
        return [item for item in self.list_all() if item.family_id == family_id]

    def by_status(self, status: StrategyStatus) -> List[StrategyRecord]:
        return [item for item in self.list_all() if item.status == status]

    def find(self, name: str, version: str) -> Optional[StrategyRecord]:
        for item in self.list_all():
            if item.name == name and item.version == version:
                return item
        return None
