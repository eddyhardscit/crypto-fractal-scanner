#!/usr/bin/env python3
"""Safely apply the reviewed Evolution Registry preview.

Default behavior is DRY RUN. Nothing is written unless --apply is supplied.

Writes, when applied:
- data/evolution/strategy_registry.json
- data/evolution/evolution_history.json
- data/evolution/research_layers.json
- data/evolution/deployments.json
- reports/evolution_registry_apply_result.json

Before any write, current evolution data files are copied to a timestamped
backup directory under data/evolution/backups/.

No trading configuration is edited and no service is restarted.
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
        raise RuntimeError(f"Expected a JSON object in {path}")
    return value


def atomic_report(path: Path, value: dict[str, Any]) -> None:
    JsonStore(path, default={}).write(value)


def strategy_metadata(item: dict[str, Any]) -> dict[str, Any]:
    metadata = dict(item.get("metadata") or {})
    metadata.update(
        {
            "source_kind": item.get("source_kind"),
            "source_path": item.get("source_path"),
            "source_key": item.get("source_key"),
            "role": item.get("role"),
            "enabled": item.get("enabled"),
            "evolution_policy": item.get("evolution_policy") or {},
            "legacy_imported": True,
        }
    )
    return metadata


def validate_preview(preview: dict[str, Any]) -> None:
    if preview.get("mode") != "PREVIEW_ONLY":
        raise RuntimeError("The input is not an Evolution Registry preview.")
    validation = preview.get("validation") or {}
    if validation.get("valid") is not True:
        raise RuntimeError("Preview validation is not OK; refusing to apply.")
    if not isinstance(preview.get("strategies"), list):
        raise RuntimeError("Preview has no valid strategies list.")
    if not isinstance(preview.get("research_layers"), list):
        raise RuntimeError("Preview has no valid research_layers list.")
    if not isinstance(preview.get("deployments"), list):
        raise RuntimeError("Preview has no valid deployments list.")

    for deployment in preview["deployments"]:
        if (
            deployment.get("deployment_type") == "LIVE"
            and deployment.get("protected") is not True
        ):
            raise RuntimeError(
                f"Unprotected live deployment: {deployment.get('name')}"
            )


def identity_conflict(existing: StrategyRecord, incoming: dict[str, Any]) -> str | None:
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
    if actual != expected:
        return f"identity mismatch: existing={actual}, incoming={expected}"
    return None


def build_plan(
    registry: StrategyRegistry,
    preview: dict[str, Any],
) -> dict[str, Any]:
    existing_by_id = {item.strategy_id: item for item in registry.list_all()}
    create: list[str] = []
    unchanged: list[str] = []
    metadata_update: list[str] = []
    conflicts: list[dict[str, str]] = []

    for incoming in preview["strategies"]:
        strategy_id = str(incoming.get("strategy_id", "")).strip()
        if not strategy_id:
            conflicts.append(
                {"strategy_id": "", "reason": "missing incoming strategy_id"}
            )
            continue

        existing = existing_by_id.get(strategy_id)
        if existing is None:
            create.append(strategy_id)
            continue

        conflict = identity_conflict(existing, incoming)
        if conflict:
            conflicts.append({"strategy_id": strategy_id, "reason": conflict})
            continue

        expected_metadata = strategy_metadata(incoming)
        differs = any(
            existing.metadata.get(key) != value
            for key, value in expected_metadata.items()
        )
        if differs:
            metadata_update.append(strategy_id)
        else:
            unchanged.append(strategy_id)

    return {
        "create_ids": create,
        "metadata_update_ids": metadata_update,
        "unchanged_ids": unchanged,
        "conflicts": conflicts,
        "counts": {
            "create": len(create),
            "metadata_update": len(metadata_update),
            "unchanged": len(unchanged),
            "conflicts": len(conflicts),
        },
    }


def make_backup(repo: Path, paths: list[Path]) -> Path:
    backup_dir = repo / "data" / "evolution" / "backups" / timestamp_slug()
    backup_dir.mkdir(parents=True, exist_ok=False)
    for path in paths:
        if path.exists():
            relative = path.relative_to(repo)
            destination = backup_dir / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(path, destination)
    return backup_dir


def apply_strategies(
    registry: StrategyRegistry,
    preview: dict[str, Any],
    plan: dict[str, Any],
) -> dict[str, int]:
    incoming_by_id = {
        str(item["strategy_id"]): item for item in preview["strategies"]
    }
    created = 0
    updated = 0

    for strategy_id in plan["create_ids"]:
        item = incoming_by_id[strategy_id]
        record = StrategyRecord(
            family_id=str(item["family_id"]),
            name=str(item["name"]),
            version=str(item["version"]),
            status=StrategyStatus(str(item["status"])),
            strategy_id=strategy_id,
            parent_id=item.get("parent_id"),
            child_ids=list(item.get("child_ids") or []),
            mutation=None,
            created_by=str(item.get("created_by") or "legacy_import"),
            metadata=strategy_metadata(item),
        )
        registry.register(record)
        created += 1

    for strategy_id in plan["metadata_update_ids"]:
        item = incoming_by_id[strategy_id]
        record = registry.get(strategy_id)
        record.metadata.update(strategy_metadata(item))
        # Preserve the current lifecycle status on later idempotent runs.
        registry.save(record)
        updated += 1

    return {"created": created, "metadata_updated": updated}


def write_auxiliary_data(repo: Path, preview: dict[str, Any]) -> None:
    evolution_dir = repo / "data" / "evolution"
    JsonStore(
        evolution_dir / "research_layers.json",
        default={"schema_version": 1, "layers": []},
    ).write(
        {
            "schema_version": 1,
            "updated_at": utc_now_iso(),
            "layers": preview["research_layers"],
        }
    )
    JsonStore(
        evolution_dir / "deployments.json",
        default={"schema_version": 1, "deployments": []},
    ).write(
        {
            "schema_version": 1,
            "updated_at": utc_now_iso(),
            "deployments": preview["deployments"],
        }
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", default=".")
    parser.add_argument(
        "--preview",
        default="reports/evolution_registry_preview.json",
    )
    parser.add_argument(
        "--result",
        default="reports/evolution_registry_apply_result.json",
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Actually write the registry. Without this flag, performs dry run.",
    )
    args = parser.parse_args()

    repo = Path(args.repo).expanduser().resolve()
    preview_path = (repo / args.preview).resolve()
    result_path = (repo / args.result).resolve()

    preview = read_json(preview_path)
    validate_preview(preview)

    registry_path = repo / "data" / "evolution" / "strategy_registry.json"
    history_path = repo / "data" / "evolution" / "evolution_history.json"
    registry = StrategyRegistry(registry_path, history_path)
    plan = build_plan(registry, preview)

    result: dict[str, Any] = {
        "schema_version": 1,
        "generated_at": utc_now_iso(),
        "mode": "APPLY" if args.apply else "DRY_RUN",
        "repository": str(repo),
        "preview_path": str(preview_path),
        "plan": plan,
        "applied": False,
        "backup_dir": None,
        "write_result": None,
        "safety": {
            "trading_configuration_changed": False,
            "services_restarted": False,
            "live_deployments_remain_protected": True,
        },
    }

    if plan["conflicts"]:
        atomic_report(result_path, result)
        print("ERRORE: sono presenti conflitti; nessun file è stato modificato.")
        for item in plan["conflicts"]:
            print(f"- {item['strategy_id']}: {item['reason']}")
        print(f"Report: {result_path}")
        return 2

    print("=== EVOLUTION REGISTRY APPLY PLAN ===")
    print(f"Modalità: {'APPLY' if args.apply else 'DRY RUN'}")
    print(f"Da creare: {plan['counts']['create']}")
    print(f"Metadati da aggiornare: {plan['counts']['metadata_update']}")
    print(f"Già invariati: {plan['counts']['unchanged']}")
    print(f"Conflitti: {plan['counts']['conflicts']}")
    print(f"Research layers: {len(preview['research_layers'])}")
    print(f"Deployments: {len(preview['deployments'])}")

    if not args.apply:
        atomic_report(result_path, result)
        print("DRY RUN OK: il registro reale NON è stato modificato.")
        print(f"Report: {result_path}")
        print("Per applicare, rieseguire aggiungendo --apply.")
        return 0

    paths_to_backup = [
        registry_path,
        history_path,
        repo / "data" / "evolution" / "research_layers.json",
        repo / "data" / "evolution" / "deployments.json",
    ]
    backup_dir = make_backup(repo, paths_to_backup)
    write_result = apply_strategies(registry, preview, plan)
    write_auxiliary_data(repo, preview)

    registry.history.append(
        {
            "event_type": "registry_import_applied",
            "created_at": utc_now_iso(),
            "reason": "approved_legacy_ecosystem_import",
            "metadata": {
                "preview_path": str(preview_path),
                "created": write_result["created"],
                "metadata_updated": write_result["metadata_updated"],
                "research_layers": len(preview["research_layers"]),
                "deployments": len(preview["deployments"]),
                "backup_dir": str(backup_dir),
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
    atomic_report(result_path, result)

    print("APPLICAZIONE COMPLETATA.")
    print(f"Strategie create: {write_result['created']}")
    print(f"Metadati aggiornati: {write_result['metadata_updated']}")
    print(f"Totale nel registro: {final_count}")
    print(f"Backup: {backup_dir}")
    print(f"Report: {result_path}")
    print("Nessun servizio è stato riavviato.")
    print("Nessuna configurazione di trading è stata modificata.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
