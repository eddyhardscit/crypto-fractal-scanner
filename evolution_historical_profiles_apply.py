#!/usr/bin/env python3
"""Safely import reviewed historical Paper profiles into the Evolution Registry.

Default mode is DRY RUN. Add --apply to write.

Inputs:
- reports/evolution_historical_profiles_preview.json
- data/evolution/strategy_registry.json
- data/evolution/evolution_history.json

Writes only when --apply is used:
- data/evolution/strategy_registry.json
- data/evolution/evolution_history.json
- data/evolution/historical_profile_reviews.json
- reports/evolution_historical_profiles_apply_result.json

Safety rules:
- every imported profile is BACKGROUND;
- no profile is enabled or reactivated;
- no mutation or automatic promotion is allowed;
- profiles with historical open positions are flagged for review;
- low-confidence inferred families remain isolated legacy families;
- no operational Paper or live file is modified;
- no service is restarted and no order is sent.
"""

from __future__ import annotations

import argparse
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from evolution_core import StrategyRecord, StrategyRegistry, StrategyStatus
from evolution_core.storage import JsonStore


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def timestamp_slug() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def read_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise RuntimeError(f"File not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"Invalid JSON in {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise RuntimeError(f"Expected JSON object in {path}")
    return value


def atomic_write(path: Path, value: dict[str, Any]) -> None:
    JsonStore(path, default={}).write(value)


def validate_preview(preview: dict[str, Any]) -> None:
    if preview.get("mode") != "PREVIEW_ONLY":
        raise RuntimeError("Input is not a historical profiles preview.")
    validation = preview.get("validation") or {}
    if validation.get("valid") is not True:
        raise RuntimeError("Preview validation is not OK.")
    profiles = preview.get("historical_profiles")
    if not isinstance(profiles, list):
        raise RuntimeError("historical_profiles is missing or invalid.")

    for item in profiles:
        if item.get("status") != "BACKGROUND":
            raise RuntimeError(
                f"Unsafe status for {item.get('name')}: {item.get('status')}"
            )
        policy = item.get("evolution_policy") or {}
        if policy.get("allow_mutation") is not False:
            raise RuntimeError(
                f"Mutation must be disabled for {item.get('name')}"
            )
        if policy.get("allow_automatic_promotion") is not False:
            raise RuntimeError(
                f"Automatic promotion must be disabled for {item.get('name')}"
            )
        if policy.get("allow_live_side_effects") is not False:
            raise RuntimeError(
                f"Live side effects must be disabled for {item.get('name')}"
            )


def incoming_metadata(item: dict[str, Any]) -> dict[str, Any]:
    metadata = dict(item.get("metadata") or {})
    metadata.update(
        {
            "source_kind": item.get("source_kind"),
            "source_path": item.get("source_path"),
            "source_key": item.get("source_key"),
            "role": item.get("role"),
            "enabled": False,
            "evolution_policy": item.get("evolution_policy") or {},
            "historical_background_import": True,
            "reactivation_blocked": True,
        }
    )
    return metadata


def identity_conflict(
    existing: StrategyRecord,
    incoming: dict[str, Any],
) -> str | None:
    expected = {
        "family_id": str(incoming.get("family_id")),
        "name": str(incoming.get("name")),
        "version": str(incoming.get("version")),
    }
    actual = {
        "family_id": existing.family_id,
        "name": existing.name,
        "version": existing.version,
    }
    if expected != actual:
        return f"identity mismatch: existing={actual}, incoming={expected}"
    return None


def build_plan(
    registry: StrategyRegistry,
    preview: dict[str, Any],
) -> dict[str, Any]:
    existing = {item.strategy_id: item for item in registry.list_all()}
    create_ids: list[str] = []
    update_ids: list[str] = []
    unchanged_ids: list[str] = []
    conflicts: list[dict[str, str]] = []

    for incoming in preview["historical_profiles"]:
        strategy_id = str(incoming.get("strategy_id", "")).strip()
        if not strategy_id:
            conflicts.append(
                {"strategy_id": "", "reason": "missing strategy_id"}
            )
            continue

        current = existing.get(strategy_id)
        if current is None:
            create_ids.append(strategy_id)
            continue

        conflict = identity_conflict(current, incoming)
        if conflict:
            conflicts.append(
                {"strategy_id": strategy_id, "reason": conflict}
            )
            continue

        expected_metadata = incoming_metadata(incoming)
        differs = (
            current.status != StrategyStatus.BACKGROUND
            or any(
                current.metadata.get(key) != value
                for key, value in expected_metadata.items()
            )
        )
        if differs:
            update_ids.append(strategy_id)
        else:
            unchanged_ids.append(strategy_id)

    return {
        "create_ids": create_ids,
        "update_ids": update_ids,
        "unchanged_ids": unchanged_ids,
        "conflicts": conflicts,
        "counts": {
            "create": len(create_ids),
            "update": len(update_ids),
            "unchanged": len(unchanged_ids),
            "conflicts": len(conflicts),
        },
    }


def make_backup(repo: Path, paths: list[Path]) -> Path:
    backup_dir = (
        repo
        / "data"
        / "evolution"
        / "backups"
        / f"historical_profiles_{timestamp_slug()}"
    )
    backup_dir.mkdir(parents=True, exist_ok=False)

    for path in paths:
        if not path.exists():
            continue
        relative = path.relative_to(repo)
        destination = backup_dir / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, destination)

    return backup_dir


def build_review_document(
    preview: dict[str, Any],
) -> dict[str, Any]:
    open_position_reviews: list[dict[str, Any]] = []
    low_confidence_reviews: list[dict[str, Any]] = []

    for item in preview["historical_profiles"]:
        metadata = item.get("metadata") or {}
        common = {
            "strategy_id": item.get("strategy_id"),
            "name": item.get("name"),
            "family_id": item.get("family_id"),
            "historical_trade_rows": metadata.get("historical_trade_rows"),
            "historical_signal_rows": metadata.get("historical_signal_rows"),
            "historical_open_position_count": metadata.get(
                "historical_open_position_count"
            ),
            "last_trade_activity": metadata.get("last_trade_activity"),
            "last_signal_activity": metadata.get("last_signal_activity"),
            "inference_confidence": metadata.get("inference_confidence"),
        }

        if metadata.get("requires_open_position_review"):
            open_position_reviews.append(
                {
                    **common,
                    "review_status": "PENDING",
                    "operational_action_allowed": False,
                    "note": (
                        "Historical Paper position marker only. Do not close, "
                        "reopen or modify automatically."
                    ),
                }
            )

        if metadata.get("inference_confidence") == "low":
            low_confidence_reviews.append(
                {
                    **common,
                    "review_status": "PENDING",
                    "family_change_allowed_automatically": False,
                    "note": (
                        "Legacy family retained separately until manually "
                        "classified from source configuration/history."
                    ),
                }
            )

    return {
        "schema_version": 1,
        "updated_at": utc_now_iso(),
        "mode": "OBSERVATION_ONLY",
        "open_position_reviews": open_position_reviews,
        "low_confidence_family_reviews": low_confidence_reviews,
        "summary": {
            "open_position_review_count": len(open_position_reviews),
            "low_confidence_family_review_count": len(
                low_confidence_reviews
            ),
        },
    }


def apply_profiles(
    registry: StrategyRegistry,
    preview: dict[str, Any],
    plan: dict[str, Any],
) -> dict[str, int]:
    incoming_by_id = {
        str(item["strategy_id"]): item
        for item in preview["historical_profiles"]
    }

    created = 0
    updated = 0

    for strategy_id in plan["create_ids"]:
        item = incoming_by_id[strategy_id]
        record = StrategyRecord(
            family_id=str(item["family_id"]),
            name=str(item["name"]),
            version=str(item["version"]),
            status=StrategyStatus.BACKGROUND,
            strategy_id=strategy_id,
            parent_id=None,
            child_ids=[],
            mutation=None,
            created_by=str(
                item.get("created_by")
                or "historical_runtime_import"
            ),
            metadata=incoming_metadata(item),
        )
        registry.register(record)
        created += 1

    for strategy_id in plan["update_ids"]:
        item = incoming_by_id[strategy_id]
        record = registry.get(strategy_id)
        # Force safe historical state. Never reactivate on re-import.
        record.status = StrategyStatus.BACKGROUND
        record.metadata.update(incoming_metadata(item))
        registry.save(record)
        updated += 1

    return {"created": created, "updated": updated}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", default=".")
    parser.add_argument(
        "--preview",
        default="reports/evolution_historical_profiles_preview.json",
    )
    parser.add_argument(
        "--result",
        default="reports/evolution_historical_profiles_apply_result.json",
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Write changes. Without this option the script is a dry run.",
    )
    args = parser.parse_args()

    repo = Path(args.repo).expanduser().resolve()
    preview_path = (repo / args.preview).resolve()
    result_path = (repo / args.result).resolve()

    preview = read_json(preview_path)
    validate_preview(preview)

    registry_path = repo / "data/evolution/strategy_registry.json"
    history_path = repo / "data/evolution/evolution_history.json"
    reviews_path = (
        repo / "data/evolution/historical_profile_reviews.json"
    )

    registry = StrategyRegistry(registry_path, history_path)
    plan = build_plan(registry, preview)
    review_document = build_review_document(preview)

    result: dict[str, Any] = {
        "schema_version": 1,
        "generated_at": utc_now_iso(),
        "mode": "APPLY" if args.apply else "DRY_RUN",
        "repository": str(repo),
        "preview_path": str(preview_path),
        "plan": plan,
        "review_summary": review_document["summary"],
        "applied": False,
        "backup_dir": None,
        "write_result": None,
        "safety": {
            "all_imports_background": True,
            "reactivation_blocked": True,
            "automatic_mutation_disabled": True,
            "automatic_promotion_disabled": True,
            "operational_files_changed": False,
            "services_restarted": False,
            "orders_sent": False,
        },
    }

    atomic_write(result_path, result)

    print("=== HISTORICAL PROFILES APPLY PLAN ===")
    print(f"Modalità: {'APPLY' if args.apply else 'DRY RUN'}")
    print(f"Da creare: {plan['counts']['create']}")
    print(f"Da aggiornare: {plan['counts']['update']}")
    print(f"Già invariati: {plan['counts']['unchanged']}")
    print(f"Conflitti: {plan['counts']['conflicts']}")
    print(
        "Revisioni posizioni storiche:",
        review_document["summary"]["open_position_review_count"],
    )
    print(
        "Revisioni famiglie incerte:",
        review_document["summary"][
            "low_confidence_family_review_count"
        ],
    )

    if plan["conflicts"]:
        print("ERRORE: conflitti presenti. Nessun file è stato modificato.")
        for conflict in plan["conflicts"]:
            print(
                f"- {conflict['strategy_id']}: {conflict['reason']}"
            )
        print(f"Report: {result_path}")
        return 2

    if not args.apply:
        print("DRY RUN OK: il registro reale NON è stato modificato.")
        print(f"Report: {result_path}")
        print("Per applicare, rieseguire aggiungendo --apply.")
        return 0

    backup_dir = make_backup(
        repo,
        [registry_path, history_path, reviews_path],
    )
    write_result = apply_profiles(registry, preview, plan)
    atomic_write(reviews_path, review_document)

    registry.history.append(
        {
            "event_type": "historical_profiles_import_applied",
            "created_at": utc_now_iso(),
            "reason": "approved_historical_background_import",
            "metadata": {
                "created": write_result["created"],
                "updated": write_result["updated"],
                "open_position_reviews": review_document["summary"][
                    "open_position_review_count"
                ],
                "low_confidence_family_reviews": review_document[
                    "summary"
                ]["low_confidence_family_review_count"],
                "backup_dir": str(backup_dir),
                "preview_path": str(preview_path),
            },
        }
    )

    final_count = len(registry.list_all())
    result["applied"] = True
    result["backup_dir"] = str(backup_dir)
    result["write_result"] = {
        **write_result,
        "final_registry_count": final_count,
    }
    atomic_write(result_path, result)

    print("APPLICAZIONE COMPLETATA.")
    print(f"Profili storici creati: {write_result['created']}")
    print(f"Profili storici aggiornati: {write_result['updated']}")
    print(f"Totale strategie nel registro: {final_count}")
    print(f"Backup: {backup_dir}")
    print(f"Revisioni: {reviews_path}")
    print(f"Report: {result_path}")
    print("Tutti i profili importati restano BACKGROUND.")
    print("Nessun file operativo è stato modificato.")
    print("Nessun servizio è stato riavviato.")
    print("Nessun ordine è stato inviato.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
