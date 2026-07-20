#!/usr/bin/env python3
"""Read-only preview for importing the current scanner into Evolution Core.

Creates:
- reports/evolution_registry_preview.json
- reports/evolution_registry_preview.md

It never writes data/evolution/strategy_registry.json, imports project modules,
changes trading configuration, or restarts services.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import uuid
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

NAMESPACE = uuid.UUID("bb279560-2ea4-4cca-af20-a61fed9dc34b")


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def stable_id(kind: str, key: str) -> str:
    return str(uuid.uuid5(NAMESPACE, f"crypto-fractal-scanner:{kind}:{key}".lower()))


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", value.lower()).strip("_") or "unknown"


def read_json(path: Path) -> dict[str, Any] | None:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None
    return value if isinstance(value, dict) else None


def fingerprint(value: Any) -> str:
    raw = json.dumps(value, sort_keys=True, ensure_ascii=False, default=str).encode()
    return hashlib.sha256(raw).hexdigest()


def classify(p: dict[str, Any]) -> tuple[str, str]:
    name = str(p.get("name", "")).upper()
    if bool(p.get("paper_only_high_leverage_test")):
        return "TEST", "CANDIDATE"
    if bool(p.get("compact_shadow")) or name.startswith("SHADOW_"):
        return "SHADOW", "SHADOW"
    if p.get("is_main") is True:
        return "MAIN", "MASTER"
    return "PAPER", "SHADOW"


def portfolio_records(repo: Path) -> tuple[list[dict[str, Any]], list[str]]:
    data = read_json(repo / "paper_trading_config.json")
    if not data or not isinstance(data.get("portfolios"), list):
        return [], ["paper_trading_config.json missing or invalid"]

    records: list[dict[str, Any]] = []
    warnings: list[str] = []
    for index, p in enumerate(data["portfolios"]):
        if not isinstance(p, dict):
            warnings.append(f"portfolios[{index}] is not an object")
            continue
        name = str(p.get("name", "")).strip()
        engine = str(p.get("strategy", "")).strip()
        if not name or not engine:
            warnings.append(f"portfolios[{index}] missing name or strategy")
            continue
        role, status = classify(p)
        records.append({
            "strategy_id": stable_id("portfolio", name),
            "family_id": slug(engine),
            "name": name,
            "version": f"1.0.0-legacy.{index + 1}",
            "status": status,
            "parent_id": None,
            "child_ids": [],
            "mutation": None,
            "created_by": "legacy_import_preview",
            "source_kind": "paper_portfolio",
            "source_path": "paper_trading_config.json",
            "source_key": f"portfolios[{index}]",
            "role": role,
            "enabled": bool(p.get("enabled", False)),
            "evolution_policy": {
                "observe": True,
                "allow_mutation": role != "MAIN",
                "allow_automatic_promotion": False,
                "allow_live_side_effects": False,
            },
            "metadata": {
                "strategy_engine": engine,
                "legacy_profile_index": index,
                "is_main": p.get("is_main"),
                "compact_shadow": p.get("compact_shadow"),
                "paper_only_high_leverage_test": p.get("paper_only_high_leverage_test"),
                "timeframe_minutes": p.get("timeframe_minutes"),
                "leverage": p.get("leverage"),
                "max_leverage": p.get("max_leverage"),
                "fixed_margin_eur": p.get("fixed_margin_eur"),
                "configuration_fingerprint": fingerprint(p),
                "configuration_snapshot": p,
            },
        })
    return records, warnings


def first_existing(repo: Path, names: tuple[str, ...]) -> Path | None:
    for name in names:
        path = repo / name
        if path.is_file():
            return path
    return None


def sol_records(repo: Path) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[str]]:
    bot = repo / "sol_spot_adaptive_bot.py"
    paper_cfg_path = first_existing(repo, (
        "sol_spot_adaptive_config.json",
        "sol_spot_adaptive_bot_config.json",
    ))
    live_runner = repo / "sol_spot_live_guarded.py"
    live_cfg_path = first_existing(repo, ("sol_spot_live_config.json",))
    if not any((bot.exists(), paper_cfg_path, live_runner.exists(), live_cfg_path)):
        return [], [], []

    paper_cfg = read_json(paper_cfg_path) if paper_cfg_path else None
    strategy_name = "SOL Spot Adaptive Range"
    if paper_cfg:
        for key in ("strategy_name", "name", "bot_name"):
            if isinstance(paper_cfg.get(key), str) and paper_cfg[key].strip():
                strategy_name = paper_cfg[key].strip()
                break
    enabled = bool(paper_cfg.get("enabled", True)) if paper_cfg else True
    sid = stable_id("standalone", "sol_spot_adaptive_range")
    strategy = {
        "strategy_id": sid,
        "family_id": "sol_spot_adaptive_range",
        "name": strategy_name,
        "version": "1.0.0-legacy.standalone",
        "status": "MASTER" if enabled else "BACKGROUND",
        "parent_id": None,
        "child_ids": [],
        "mutation": None,
        "created_by": "legacy_import_preview",
        "source_kind": "standalone_paper_bot",
        "source_path": str(paper_cfg_path.relative_to(repo)) if paper_cfg_path else "sol_spot_adaptive_bot.py",
        "source_key": "sol_spot_adaptive_range",
        "role": "STANDALONE_PAPER",
        "enabled": enabled,
        "evolution_policy": {
            "observe": True,
            "allow_mutation": True,
            "allow_automatic_promotion": False,
            "allow_live_side_effects": False,
        },
        "metadata": {
            "bot_path": "sol_spot_adaptive_bot.py" if bot.exists() else None,
            "paper_config_path": str(paper_cfg_path.relative_to(repo)) if paper_cfg_path else None,
            "real_orders_enabled": bool(paper_cfg.get("real_orders_enabled", False)) if paper_cfg else False,
            "configuration_fingerprint": fingerprint(paper_cfg) if paper_cfg else None,
        },
    }

    deployments: list[dict[str, Any]] = []
    if live_runner.exists() or live_cfg_path:
        live_cfg = read_json(live_cfg_path) if live_cfg_path else None
        deployments.append({
            "deployment_id": stable_id("deployment", "sol_spot_live"),
            "name": "SOL Spot Live Guarded",
            "deployment_type": "LIVE",
            "linked_strategy_id": sid,
            "runner_path": "sol_spot_live_guarded.py" if live_runner.exists() else None,
            "config_path": str(live_cfg_path.relative_to(repo)) if live_cfg_path else None,
            "protected": True,
            "evolution_policy": {
                "observe": True,
                "allow_parameter_changes": False,
                "allow_strategy_switch": False,
                "allow_automatic_promotion": False,
                "require_human_approval": True,
            },
            "metadata": {
                "real_orders_enabled": bool(live_cfg.get("real_orders_enabled")) if live_cfg else None,
            },
        })
    warnings = []
    if strategy["metadata"]["real_orders_enabled"]:
        warnings.append("SOL adaptive paper config has real_orders_enabled=true; review required")
    return [strategy], deployments, warnings


def research_layer(repo: Path, candidate_ids: list[str]) -> dict[str, Any] | None:
    checks = {
        "paper_trading_runner.py": ("run_research_cycle", "research_signals", "research_eligible_ids"),
        "research_sample_watch.py": ("research_strategy_milestones", "meta_ready"),
        "research_all_signals.py": ("research",),
        "paper_trading_notify.py": ("research_marks",),
    }
    evidence: list[str] = []
    files: list[str] = []
    for relative, terms in checks.items():
        path = repo / relative
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        matches = [term for term in terms if term in text]
        if matches:
            files.append(relative)
            evidence.extend(f"{relative}:{term}" for term in matches)
    if not files:
        return None
    return {
        "layer_id": stable_id("research_layer", "research_signal"),
        "name": "Research Signal",
        "kind": "RESEARCH_LAYER",
        "status": "LEARNING",
        "source_files": sorted(files),
        "evidence": sorted(evidence),
        "link_mode": "runtime_signal_id",
        "statically_linked_strategy_ids": [],
        "candidate_strategy_ids": sorted(candidate_ids),
        "evolution_policy": {
            "observe": True,
            "collect_milestones": True,
            "collect_regime_context": True,
            "create_duplicate_strategies": False,
            "allow_trading_side_effects": False,
        },
        "interpretation": "Research Signal is linked to eligible raw signals at runtime and is not duplicated as a portfolio.",
    }


def services(repo: Path) -> list[dict[str, Any]]:
    inventory = read_json(repo / "reports/evolution_inventory.json")
    values = inventory.get("systemd_services", []) if inventory else []
    result = []
    for item in values if isinstance(values, list) else []:
        if isinstance(item, dict):
            result.append({
                "unit": item.get("unit"),
                "runtime_state": item.get("runtime_state"),
                "working_directory": item.get("working_directory"),
                "exec_start": item.get("exec_start", []),
            })
    return result


def validate(strategies: list[dict[str, Any]], deployments: list[dict[str, Any]]) -> dict[str, Any]:
    ids = [x["strategy_id"] for x in strategies]
    pairs = [(x["name"], x["version"]) for x in strategies]
    masters: dict[str, list[str]] = defaultdict(list)
    for x in strategies:
        if x["status"] == "MASTER":
            masters[x["family_id"]].append(x["strategy_id"])
    duplicate_ids = sorted(x for x, n in Counter(ids).items() if n > 1)
    duplicate_pairs = [list(x) for x, n in Counter(pairs).items() if n > 1]
    multiple_masters = {k: v for k, v in masters.items() if len(v) > 1}
    unprotected_live = [x["deployment_id"] for x in deployments if x.get("deployment_type") == "LIVE" and not x.get("protected")]
    ok = not (duplicate_ids or duplicate_pairs or multiple_masters or unprotected_live)
    return {
        "valid": ok,
        "duplicate_strategy_ids": duplicate_ids,
        "duplicate_name_versions": duplicate_pairs,
        "families_with_multiple_masters": multiple_masters,
        "unprotected_live_deployments": unprotected_live,
    }


def build(repo: Path) -> dict[str, Any]:
    paper, warnings = portfolio_records(repo)
    sol, deployments, sol_warnings = sol_records(repo)
    warnings += sol_warnings
    strategies = paper + sol
    research = research_layer(repo, [x["strategy_id"] for x in paper])

    families: dict[str, dict[str, Any]] = {}
    for x in strategies:
        f = families.setdefault(x["family_id"], {
            "family_id": x["family_id"],
            "member_ids": [], "master_ids": [], "shadow_ids": [],
            "candidate_ids": [], "background_ids": [],
        })
        f["member_ids"].append(x["strategy_id"])
        key = {"MASTER": "master_ids", "SHADOW": "shadow_ids", "CANDIDATE": "candidate_ids", "BACKGROUND": "background_ids"}.get(x["status"])
        if key:
            f[key].append(x["strategy_id"])

    role_counts = Counter(x["role"] for x in strategies)
    status_counts = Counter(x["status"] for x in strategies)
    return {
        "schema_version": 1,
        "generated_at": now_iso(),
        "repository": str(repo),
        "mode": "PREVIEW_ONLY",
        "safety": {
            "registry_written": False,
            "trading_configuration_changed": False,
            "services_restarted": False,
            "project_modules_imported": False,
            "live_deployments_protected": True,
        },
        "summary": {
            "strategy_record_count": len(strategies),
            "paper_portfolio_record_count": len(paper),
            "standalone_strategy_record_count": len(sol),
            "family_count": len(families),
            "role_counts": dict(sorted(role_counts.items())),
            "status_counts": dict(sorted(status_counts.items())),
            "research_layer_count": 1 if research else 0,
            "deployment_count": len(deployments),
            "protected_live_deployment_count": sum(1 for x in deployments if x.get("deployment_type") == "LIVE" and x.get("protected")),
        },
        "validation": validate(strategies, deployments),
        "warnings": warnings,
        "strategies": strategies,
        "families": [families[k] for k in sorted(families)],
        "research_layers": [research] if research else [],
        "deployments": deployments,
        "systemd_services": services(repo),
        "apply_plan": {
            "next_action": "Review this preview before running a separate apply script.",
            "idempotency": "IDs are deterministic UUIDv5 values.",
            "research_rule": "Research Signal remains a linked layer, not a duplicate strategy.",
            "live_rule": "Live deployments are inventoried but protected from automatic evolution.",
        },
    }


def md(preview: dict[str, Any]) -> str:
    s = preview["summary"]
    lines = [
        "# Evolution Registry Preview", "",
        f"Generated: `{preview['generated_at']}`", "",
        "> PREVIEW ONLY — the real registry has not been modified.", "",
        "## Summary", "",
        f"- Strategy records: **{s['strategy_record_count']}**",
        f"- Paper portfolios: **{s['paper_portfolio_record_count']}**",
        f"- Standalone strategies: **{s['standalone_strategy_record_count']}**",
        f"- Families: **{s['family_count']}**",
        f"- Roles: `{json.dumps(s['role_counts'], ensure_ascii=False, sort_keys=True)}`",
        f"- Statuses: `{json.dumps(s['status_counts'], ensure_ascii=False, sort_keys=True)}`",
        f"- Research layers: **{s['research_layer_count']}**",
        f"- Deployments: **{s['deployment_count']}**",
        f"- Protected live deployments: **{s['protected_live_deployment_count']}**",
        f"- Validation: **{'OK' if preview['validation']['valid'] else 'ERROR'}**", "",
        "## Strategies", "",
        "| Name | Family | Version | Role | Status | Enabled |", "|---|---|---|---|---|:---:|",
    ]
    for x in preview["strategies"]:
        lines.append(f"| {x['name']} | {x['family_id']} | {x['version']} | {x['role']} | {x['status']} | {'yes' if x['enabled'] else 'no'} |")
    lines += ["", "## Research Signal", ""]
    if preview["research_layers"]:
        r = preview["research_layers"][0]
        lines += [f"- Status: `{r['status']}`", f"- Link mode: `{r['link_mode']}`", f"- Duplicate strategies: `{r['evolution_policy']['create_duplicate_strategies']}`", f"- {r['interpretation']}"]
    else:
        lines.append("- Not detected.")
    lines += ["", "## Live deployments", ""]
    if preview["deployments"]:
        for d in preview["deployments"]:
            lines += [f"- **{d['name']}** — protected: `{d['protected']}`; human approval: `{d['evolution_policy']['require_human_approval']}`"]
    else:
        lines.append("- None detected.")
    lines += ["", "## Validation", "", "```json", json.dumps(preview["validation"], indent=2, ensure_ascii=False, sort_keys=True), "```", ""]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", default=".")
    args = parser.parse_args()
    repo = Path(args.repo).expanduser().resolve()
    if not repo.is_dir():
        raise SystemExit(f"Repository not found: {repo}")
    preview = build(repo)
    reports = repo / "reports"
    reports.mkdir(parents=True, exist_ok=True)
    json_path = reports / "evolution_registry_preview.json"
    md_path = reports / "evolution_registry_preview.md"
    json_path.write_text(json.dumps(preview, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    md_path.write_text(md(preview) + "\n", encoding="utf-8")
    s = preview["summary"]
    print("=== EVOLUTION REGISTRY PREVIEW ===")
    print(f"Strategie da registrare: {s['strategy_record_count']}")
    print(f"  Portafogli paper: {s['paper_portfolio_record_count']}")
    print(f"  Strategie standalone: {s['standalone_strategy_record_count']}")
    print(f"Famiglie: {s['family_count']}")
    print(f"Ruoli: {s['role_counts']}")
    print(f"Stati: {s['status_counts']}")
    print(f"Research layer: {s['research_layer_count']}")
    print(f"Deployment: {s['deployment_count']}")
    print(f"Live protetti: {s['protected_live_deployment_count']}")
    print(f"Validazione: {'OK' if preview['validation']['valid'] else 'ERRORE'}")
    for warning in preview["warnings"]:
        print(f"AVVISO: {warning}")
    print(f"JSON: {json_path}")
    print(f"Markdown: {md_path}")
    print("Il registro reale NON è stato modificato.")
    return 0 if preview["validation"]["valid"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
