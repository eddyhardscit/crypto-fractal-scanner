#!/usr/bin/env python3
"""Synchronize Paper Block 5 candidates into Evolution Core.

The script only registers or refreshes CANDIDATE records. It never promotes,
retires or changes Paper/live configuration. Parent-child genealogy is updated
through StrategyRegistry.register().
"""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from evolution_core import MutationRecord, StrategyRecord, StrategyRegistry, StrategyStatus
from evolution_core.storage import JsonStore


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def read_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"Invalid candidate registry JSON: {exc}") from exc
    if not isinstance(value, dict):
        raise RuntimeError("Candidate registry root must be an object")
    return value


def validate_source(source: dict[str, Any]) -> list[dict[str, Any]]:
    if source.get("paper_only") is not True:
        raise RuntimeError("Candidate source is not Paper-only")
    if int(source.get("automatic_promotions", 0)) != 0:
        raise RuntimeError("Automatic promotions are forbidden")
    if int(source.get("automatic_retirements", 0)) != 0:
        raise RuntimeError("Automatic retirements are forbidden")
    if source.get("live_modified") is not False:
        raise RuntimeError("Live modification marker is not false")
    if source.get("orders_sent") is not False:
        raise RuntimeError("Order marker is not false")
    rows = source.get("candidates", [])
    if not isinstance(rows, list):
        raise RuntimeError("Candidate list is invalid")
    return [row for row in rows if isinstance(row, dict)]


def find_parent(registry: StrategyRegistry, parent_id: str, candidate: dict[str, Any]):
    try:
        return registry.get(parent_id)
    except KeyError:
        parent_name = str((candidate.get("metadata") or {}).get("parent_portfolio") or "")
        for record in registry.list_all():
            metadata = record.metadata or {}
            profile = str(metadata.get("legacy_profile_name") or metadata.get("source_key") or record.name)
            if profile == parent_name:
                return record
    raise RuntimeError(f"Parent strategy not registered: {parent_id}")


def identity_conflict(existing: StrategyRecord, incoming: dict[str, Any], parent_id: str) -> str | None:
    expected = (
        str(incoming.get("family_id")),
        str(incoming.get("name")),
        str(incoming.get("version")),
        parent_id,
    )
    actual = (existing.family_id, existing.name, existing.version, existing.parent_id)
    return None if actual == expected else f"identity mismatch existing={actual} incoming={expected}"


def sync(repo: Path, source_path: Path, result_path: Path) -> dict[str, Any]:
    source = read_json(source_path)
    rows = validate_source(source) if source else []
    registry = StrategyRegistry(
        repo / "data/evolution/strategy_registry.json",
        repo / "data/evolution/evolution_history.json",
    )
    existing = {record.strategy_id: record for record in registry.list_all()}
    created = 0
    refreshed = 0
    unchanged = 0
    conflicts: list[dict[str, str]] = []

    for row in rows:
        incoming_status = str(row.get("status", "CANDIDATE"))
        if incoming_status not in {"CANDIDATE", "SHADOW", "MASTER", "EX_MASTER", "BACKGROUND"}:
            conflicts.append({"strategy_id": str(row.get("strategy_id", "")), "reason": "status_not_supported"})
            continue
        mutation = row.get("mutation") or {}
        if str(mutation.get("mutation_type")) != "single_parameter" or not mutation.get("parameter"):
            conflicts.append({"strategy_id": str(row.get("strategy_id", "")), "reason": "mutation_not_single_parameter"})
            continue
        strategy_id = str(row.get("strategy_id", "")).strip()
        parent_id = str(row.get("parent_id", "")).strip()
        if not strategy_id or not parent_id:
            conflicts.append({"strategy_id": strategy_id, "reason": "missing_identity"})
            continue
        parent = find_parent(registry, parent_id, row)
        parent_id = parent.strategy_id
        current = existing.get(strategy_id)
        if current is None:
            if incoming_status != "CANDIDATE":
                conflicts.append({"strategy_id": strategy_id, "reason": "new_non_candidate_forbidden"})
                continue
            record = StrategyRecord(
                family_id=str(row["family_id"]),
                name=str(row["name"]),
                version=str(row["version"]),
                status=StrategyStatus.CANDIDATE,
                strategy_id=strategy_id,
                parent_id=parent_id,
                child_ids=[],
                mutation=MutationRecord.from_dict(dict(mutation)),
                created_by=str(row.get("created_by") or "block5_candidate_sync"),
                created_at=str(row.get("created_at") or now_iso()),
                metadata=dict(row.get("metadata") or {}),
            )
            registry.register(record)
            existing[strategy_id] = record
            created += 1
            continue
        conflict = identity_conflict(current, row, parent_id)
        if conflict:
            conflicts.append({"strategy_id": strategy_id, "reason": conflict})
            continue
        expected_metadata = dict(row.get("metadata") or {})
        if current.status.value != incoming_status:
            conflicts.append({"strategy_id": strategy_id, "reason": f"status_mismatch_existing_{current.status.value}_source_{incoming_status}"})
            continue
        if current.metadata != expected_metadata:
            current.metadata = expected_metadata
            current.mutation = MutationRecord.from_dict(dict(mutation))
            registry.save(current)
            refreshed += 1
        else:
            unchanged += 1

    result = {
        "schema_version": 1,
        "generated_at": now_iso(),
        "source": str(source_path),
        "candidate_rows": len(rows),
        "created": created,
        "refreshed": refreshed,
        "unchanged": unchanged,
        "conflicts": conflicts,
        "success": not conflicts,
        "safety": {
            "promotions": 0,
            "retirements": 0,
            "paper_configuration_changed": False,
            "live_modified": False,
            "services_restarted": False,
            "orders_sent": False,
        },
    }
    JsonStore(result_path, default={}).write(result)
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", default="/root/crypto-fractal-scanner")
    parser.add_argument(
        "--source",
        default="/opt/crypto-fractal-scanner-vps/reports/paper_trading_evolution_candidate_registry.json",
    )
    parser.add_argument(
        "--result",
        default="reports/evolution_candidate_registry_sync_result.json",
    )
    args = parser.parse_args()
    repo = Path(args.repo).resolve()
    source = Path(args.source).resolve()
    result_path = (repo / args.result).resolve()
    try:
        result = sync(repo, source, result_path)
    except Exception as exc:
        result = {
            "schema_version": 1,
            "generated_at": now_iso(),
            "source": str(source),
            "success": False,
            "error": str(exc),
            "safety": {"promotions": 0, "retirements": 0, "live_modified": False, "orders_sent": False},
        }
        JsonStore(result_path, default={}).write(result)
        print(f"Evolution candidate sync failed: {exc}")
        return 2
    print("=== EVOLUTION CANDIDATE REGISTRY SYNC ===")
    print(f"Candidates: {result['candidate_rows']}")
    print(f"Created: {result['created']}")
    print(f"Refreshed: {result['refreshed']}")
    print(f"Unchanged: {result['unchanged']}")
    print(f"Conflicts: {len(result['conflicts'])}")
    print("Promotions: 0")
    print("Live modified: NO")
    return 0 if result["success"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
