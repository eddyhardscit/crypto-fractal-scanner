from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List

from .models import LifecycleEvent
from .storage import JsonStore


class EvolutionHistory:
    def __init__(self, path: str | Path) -> None:
        self._store = JsonStore(path, default={"schema_version": 1, "events": []})

    def append(self, event: LifecycleEvent | Dict[str, Any]) -> None:
        document = self._store.read()
        payload = event.to_dict() if isinstance(event, LifecycleEvent) else dict(event)
        document.setdefault("events", []).append(payload)
        self._store.write(document)

    def list_events(self) -> List[Dict[str, Any]]:
        return list(self._store.read().get("events", []))
