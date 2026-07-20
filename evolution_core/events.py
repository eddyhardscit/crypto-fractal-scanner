from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from threading import RLock
from typing import Any, Callable, Dict, List
from uuid import uuid4


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


@dataclass(frozen=True, slots=True)
class EvolutionEvent:
    event_type: str
    payload: Dict[str, Any]
    event_id: str = field(default_factory=lambda: str(uuid4()))
    created_at: str = field(default_factory=utc_now_iso)


EventHandler = Callable[[EvolutionEvent], None]


class EventBus:
    """Synchronous internal event bus.

    Synchronous dispatch is intentional in Block 1: deterministic, testable
    and safe. A queue-backed adapter can be introduced later without changing
    publishers or handlers.
    """

    def __init__(self) -> None:
        self._subscribers: Dict[str, List[EventHandler]] = {}
        self._lock = RLock()

    def subscribe(self, event_type: str, handler: EventHandler) -> None:
        with self._lock:
            handlers = self._subscribers.setdefault(event_type, [])
            if handler not in handlers:
                handlers.append(handler)

    def unsubscribe(self, event_type: str, handler: EventHandler) -> None:
        with self._lock:
            handlers = self._subscribers.get(event_type, [])
            if handler in handlers:
                handlers.remove(handler)

    def publish(self, event: EvolutionEvent) -> List[Exception]:
        with self._lock:
            handlers = list(self._subscribers.get(event.event_type, []))
            handlers += list(self._subscribers.get("*", []))

        errors: List[Exception] = []
        for handler in handlers:
            try:
                handler(event)
            except Exception as exc:
                errors.append(exc)
        return errors
