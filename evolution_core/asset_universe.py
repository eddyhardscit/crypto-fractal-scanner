from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional

from .events import EventBus, EvolutionEvent
from .models import AssetStatus
from .storage import JsonStore


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


@dataclass(slots=True)
class AssetRecord:
    symbol: str
    status: AssetStatus = AssetStatus.WATCHLIST
    first_seen_at: str = field(default_factory=utc_now_iso)
    last_seen_at: str = field(default_factory=utc_now_iso)
    activated_at: Optional[str] = None
    deactivated_at: Optional[str] = None
    consecutive_eligible_checks: int = 0
    consecutive_ineligible_checks: int = 0
    metrics: Dict[str, Any] = field(default_factory=dict)
    reasons: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        result = asdict(self)
        result["status"] = self.status.value
        return result

    @classmethod
    def from_dict(cls, value: Dict[str, Any]) -> "AssetRecord":
        payload = dict(value)
        payload["status"] = AssetStatus(payload["status"])
        return cls(**payload)


class AssetUniverseManager:
    """Tracks the changing crypto universe without forcing trading changes.

    Block 1 defaults to observation mode. Assets enter or leave ACTIVE only
    when `allow_automatic_status_changes` is explicitly enabled. This avoids
    survivorship bias and prevents a temporary popularity spike from changing
    the trading universe immediately.
    """

    def __init__(
        self,
        path: str | Path,
        event_bus: EventBus | None = None,
        *,
        allow_automatic_status_changes: bool = False,
        activation_confirmations: int = 7,
        cooling_confirmations: int = 7,
        background_confirmations: int = 30,
    ) -> None:
        self._store = JsonStore(
            path,
            default={"schema_version": 1, "assets": {}, "snapshots": []},
        )
        self.event_bus = event_bus or EventBus()
        self.allow_automatic_status_changes = allow_automatic_status_changes
        self.activation_confirmations = activation_confirmations
        self.cooling_confirmations = cooling_confirmations
        self.background_confirmations = background_confirmations

    def observe(
        self,
        symbol: str,
        *,
        eligible: bool,
        metrics: Dict[str, Any],
        reasons: Iterable[str] = (),
        observed_at: Optional[str] = None,
    ) -> AssetRecord:
        symbol = symbol.upper().strip()
        if not symbol:
            raise ValueError("symbol cannot be empty")

        now = observed_at or utc_now_iso()
        document = self._store.read()
        assets = document.setdefault("assets", {})
        record = (
            AssetRecord.from_dict(assets[symbol])
            if symbol in assets
            else AssetRecord(symbol=symbol, first_seen_at=now, last_seen_at=now)
        )

        record.last_seen_at = now
        record.metrics = dict(metrics)
        record.reasons = list(reasons)

        if eligible:
            record.consecutive_eligible_checks += 1
            record.consecutive_ineligible_checks = 0
        else:
            record.consecutive_ineligible_checks += 1
            record.consecutive_eligible_checks = 0

        old_status = record.status
        proposed = self._proposed_status(record, eligible)

        if self.allow_automatic_status_changes and proposed != old_status:
            record.status = proposed
            if proposed == AssetStatus.ACTIVE and record.activated_at is None:
                record.activated_at = now
            if proposed in {AssetStatus.BACKGROUND, AssetStatus.DELISTED, AssetStatus.REJECTED}:
                record.deactivated_at = now

        assets[symbol] = record.to_dict()
        document.setdefault("snapshots", []).append(
            {
                "symbol": symbol,
                "observed_at": now,
                "eligible": eligible,
                "current_status": record.status.value,
                "proposed_status": proposed.value,
                "metrics": metrics,
                "reasons": list(reasons),
            }
        )
        self._store.write(document)

        self.event_bus.publish(
            EvolutionEvent(
                "asset_universe_observed",
                {
                    "symbol": symbol,
                    "eligible": eligible,
                    "current_status": record.status.value,
                    "proposed_status": proposed.value,
                    "automatic_changes_enabled": self.allow_automatic_status_changes,
                },
            )
        )
        return record

    def _proposed_status(self, record: AssetRecord, eligible: bool) -> AssetStatus:
        if eligible:
            if record.status in {
                AssetStatus.WATCHLIST,
                AssetStatus.CANDIDATE,
                AssetStatus.COOLING,
                AssetStatus.BACKGROUND,
            }:
                if record.consecutive_eligible_checks >= self.activation_confirmations:
                    return AssetStatus.ACTIVE
                return AssetStatus.CANDIDATE
            return record.status

        if record.status == AssetStatus.ACTIVE:
            if record.consecutive_ineligible_checks >= self.cooling_confirmations:
                return AssetStatus.COOLING
        if record.status == AssetStatus.COOLING:
            if record.consecutive_ineligible_checks >= self.background_confirmations:
                return AssetStatus.BACKGROUND
        return record.status

    def list_assets(self) -> List[AssetRecord]:
        values = self._store.read().get("assets", {}).values()
        return [AssetRecord.from_dict(value) for value in values]

    def latest_snapshot(self, symbol: str) -> Optional[Dict[str, Any]]:
        symbol = symbol.upper().strip()
        snapshots = self._store.read().get("snapshots", [])
        for item in reversed(snapshots):
            if item["symbol"] == symbol:
                return item
        return None
