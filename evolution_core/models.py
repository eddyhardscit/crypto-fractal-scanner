from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Any, Dict, List, Optional
from uuid import uuid4


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


class StrategyStatus(str, Enum):
    CANDIDATE = "CANDIDATE"
    SHADOW = "SHADOW"
    MASTER = "MASTER"
    EX_MASTER = "EX_MASTER"
    BACKGROUND = "BACKGROUND"
    RETIRED = "RETIRED"


class AssetStatus(str, Enum):
    WATCHLIST = "WATCHLIST"
    CANDIDATE = "CANDIDATE"
    ACTIVE = "ACTIVE"
    COOLING = "COOLING"
    BACKGROUND = "BACKGROUND"
    DELISTED = "DELISTED"
    REJECTED = "REJECTED"


@dataclass(slots=True)
class MutationRecord:
    parameter: str
    old_value: Any
    new_value: Any
    reason: str
    mutation_type: str = "single_parameter"
    created_at: str = field(default_factory=utc_now_iso)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, value: Dict[str, Any]) -> "MutationRecord":
        return cls(**value)


@dataclass(slots=True)
class StrategyRecord:
    family_id: str
    name: str
    version: str
    status: StrategyStatus = StrategyStatus.CANDIDATE
    strategy_id: str = field(default_factory=lambda: str(uuid4()))
    parent_id: Optional[str] = None
    child_ids: List[str] = field(default_factory=list)
    mutation: Optional[MutationRecord] = None
    created_by: str = "system"
    created_at: str = field(default_factory=utc_now_iso)
    updated_at: str = field(default_factory=utc_now_iso)
    metadata: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        result = asdict(self)
        result["status"] = self.status.value
        return result

    @classmethod
    def from_dict(cls, value: Dict[str, Any]) -> "StrategyRecord":
        payload = dict(value)
        payload["status"] = StrategyStatus(payload["status"])
        if payload.get("mutation"):
            payload["mutation"] = MutationRecord.from_dict(payload["mutation"])
        return cls(**payload)


@dataclass(slots=True)
class LifecycleEvent:
    strategy_id: str
    event_type: str
    old_status: Optional[str]
    new_status: Optional[str]
    reason: str
    event_id: str = field(default_factory=lambda: str(uuid4()))
    created_at: str = field(default_factory=utc_now_iso)
    metadata: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)
