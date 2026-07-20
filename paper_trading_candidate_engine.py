# -*- coding: utf-8 -*-
"""Block 5 controlled candidate generation for the Paper runtime.

This module is Paper-only. It consumes only Block 4 evaluations already marked
ELIGIBLE_FOR_MUTATION and creates persistent CANDIDATE portfolios. Existing
portfolios are never edited: each child is a deep clone of one parent with
exactly one supported scalar parameter changed.

Block 5 v1 supports only mutations that the current engine already executes
natively and can express as one parameter:
- FIXED_R -> reward_risk
- TIME_EXIT -> max_holding_hours
- ATR_TRAIL -> trailing_at_r OR trailing_atr_multiple, but only when exactly
  one of the two values differs from the parent.

MFE_GIVEBACK and BREAKEVEN remain recorded as unsupported evidence in v1; they
are not approximated and do not create a misleading candidate. The module does
not promote, retire or replace strategies and sends no orders.
"""

from __future__ import annotations

import copy
import csv
import hashlib
import json
import math
import re
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

from paper_trading_config import validate_config
from paper_trading_promotion_governor import apply_runtime_roles
from paper_trading_evolution_memory import mutation_policy_decision
from paper_trading_regime_evolution import regime_candidate_policy_decision

REPORTS_DIR = Path("reports")
INPUT_PATH = REPORTS_DIR / "paper_trading_shadow_evaluation_candidates.json"
STATE_PATH = REPORTS_DIR / "paper_trading_evolution_candidate_state.json"
REGISTRY_PATH = REPORTS_DIR / "paper_trading_evolution_candidate_registry.json"
EVENTS_PATH = REPORTS_DIR / "paper_trading_evolution_candidate_events.csv"
REPORT_PATH = REPORTS_DIR / "paper_trading_evolution_candidate_report.md"
CONFIG_SNAPSHOT_PATH = REPORTS_DIR / "paper_trading_evolution_candidate_config_snapshot.json"
CONFIG_PATH = Path("config/evolution_candidate_block5.json")

SCHEMA_VERSION = 1
ENGINE_VERSION = "block5-controlled-candidate-v1"
NAMESPACE = uuid.UUID("bb279560-2ea4-4cca-af20-a61fed9dc34b")

EVENT_FIELDS = [
    "generated_utc",
    "event_type",
    "candidate_id",
    "candidate_portfolio",
    "parent_portfolio",
    "parent_strategy_id",
    "mutation_parameter",
    "old_value_json",
    "new_value_json",
    "scenario_id",
    "scope",
    "evidence_score",
    "sample_eligible",
    "reason",
]

DEFAULT_CONFIG: dict[str, Any] = {
    "schema_version": 1,
    "enabled": True,
    "paper_only": True,
    "automatic_promotion": False,
    "automatic_retirement": False,
    "modify_existing_portfolios": False,
    "allow_recursive_candidates": False,
    "allow_main_parent": True,
    "maximum_active_candidates": 12,
    "maximum_candidates_per_parent": 2,
    "maximum_new_candidates_per_cycle": 2,
    "minimum_sample_eligible": 120,
    "minimum_evidence_score": 78.0,
    "allowed_scopes": ["PORTFOLIO", "STRATEGY"],
    "allowed_statuses": ["ELIGIBLE_FOR_MUTATION"],
    "supported_scenario_kinds": ["FIXED_R", "TIME_EXIT", "ATR_TRAIL"],
    "candidate_name_prefix": "EVO_CAND",
    "maximum_candidate_name_length": 63,
    "candidate_compact_shadow": True,
    "candidate_enabled": True,
    "retain_inactive_candidates": True,
}


def now_utc() -> datetime:
    return datetime.now(timezone.utc)


def iso_utc(value: datetime | None = None) -> str:
    return (value or now_utc()).astimezone(timezone.utc).isoformat(timespec="seconds")


def finite(value: Any, default: float = 0.0) -> float:
    try:
        number = float(value)
    except (TypeError, ValueError):
        return default
    return number if math.isfinite(number) else default


def integer(value: Any, default: int = 0) -> int:
    return int(finite(value, default))


def truthy(value: Any) -> bool:
    return str(value).strip().lower() in {"1", "true", "yes", "y"}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", value.lower()).strip("_") or "unknown"


def stable_id(kind: str, key: str) -> str:
    return str(uuid.uuid5(NAMESPACE, f"crypto-fractal-scanner:{kind}:{key}".lower()))


def fingerprint(value: Any) -> str:
    raw = json.dumps(value, sort_keys=True, ensure_ascii=False, default=str)
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


def deep_merge(base: dict[str, Any], custom: dict[str, Any]) -> dict[str, Any]:
    output = copy.deepcopy(base)
    for key, value in custom.items():
        if isinstance(value, dict) and isinstance(output.get(key), dict):
            output[key] = deep_merge(output[key], value)
        else:
            output[key] = copy.deepcopy(value)
    return output


def atomic_write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(text, encoding="utf-8")
    temporary.replace(path)


def atomic_write_json(path: Path, value: Any) -> None:
    atomic_write_text(
        path,
        json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
    )


def append_csv(path: Path, fields: list[str], rows: Iterable[dict[str, Any]]) -> None:
    values = list(rows)
    path.parent.mkdir(parents=True, exist_ok=True)
    exists = path.exists() and path.stat().st_size > 0
    with path.open("a", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        if not exists:
            writer.writeheader()
        for row in values:
            writer.writerow({field: row.get(field, "") for field in fields})


def load_json(path: Path, default: Any) -> Any:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return copy.deepcopy(default)
    return value


def load_config() -> dict[str, Any]:
    config = copy.deepcopy(DEFAULT_CONFIG)
    custom = load_json(CONFIG_PATH, {})
    if isinstance(custom, dict):
        config = deep_merge(config, custom)
    config["allowed_scopes"] = [
        str(value).upper()
        for value in config.get("allowed_scopes", [])
        if str(value).upper() in {"PORTFOLIO", "STRATEGY"}
    ]
    config["allowed_statuses"] = [
        str(value).upper() for value in config.get("allowed_statuses", [])
    ]
    config["supported_scenario_kinds"] = [
        str(value).upper()
        for value in config.get("supported_scenario_kinds", [])
        if str(value).upper() in {"FIXED_R", "TIME_EXIT", "ATR_TRAIL"}
    ]
    atomic_write_json(CONFIG_SNAPSHOT_PATH, config)
    return config


def empty_state() -> dict[str, Any]:
    return {
        "schema_version": SCHEMA_VERSION,
        "engine_version": ENGINE_VERSION,
        "created_utc": iso_utc(),
        "updated_utc": iso_utc(),
        "candidates": {},
        "processed_evidence": {},
        "totals": {
            "created": 0,
            "rejected": 0,
            "automatic_promotions": 0,
            "automatic_retirements": 0,
        },
    }


def load_state() -> dict[str, Any]:
    value = load_json(STATE_PATH, empty_state())
    if not isinstance(value, dict):
        value = empty_state()
    value.setdefault("candidates", {})
    value.setdefault("processed_evidence", {})
    value.setdefault("totals", empty_state()["totals"])
    value["schema_version"] = SCHEMA_VERSION
    value["engine_version"] = ENGINE_VERSION
    return value


def parse_parameters(candidate: dict[str, Any]) -> dict[str, Any]:
    raw = candidate.get("scenario_parameters_json", {})
    if isinstance(raw, dict):
        return dict(raw)
    try:
        value = json.loads(str(raw or "{}"))
    except json.JSONDecodeError:
        return {}
    return dict(value) if isinstance(value, dict) else {}


def default_parent_value(parent: dict[str, Any], parameter: str) -> float:
    strategy = str(parent.get("strategy", ""))
    defaults = {
        "reward_risk": 1.5 if strategy == "rsi_extreme_reversal" else 2.0,
        "max_holding_hours": 4.0 if strategy == "rsi_extreme_reversal" else 168.0,
        "trailing_at_r": 1.0 if strategy == "rsi_extreme_reversal" else 0.0,
        "trailing_atr_multiple": 0.8 if strategy == "rsi_extreme_reversal" else 0.0,
    }
    return finite(parent.get(parameter), defaults[parameter])


def close_enough(first: float, second: float) -> bool:
    return math.isclose(first, second, rel_tol=0.0, abs_tol=1e-9)


def mutation_from_evidence(
    parent: dict[str, Any],
    evidence: dict[str, Any],
) -> tuple[dict[str, Any] | None, str]:
    kind = str(evidence.get("scenario_kind", "")).upper()
    params = parse_parameters(evidence)

    if kind == "FIXED_R":
        new_value = finite(params.get("target_r"), -1.0)
        if new_value <= 0:
            return None, "INVALID_TARGET_R"
        old_value = default_parent_value(parent, "reward_risk")
        if close_enough(old_value, new_value):
            return None, "NO_PARAMETER_CHANGE"
        return {
            "parameter": "reward_risk",
            "old_value": old_value,
            "new_value": new_value,
            "scenario_kind": kind,
        }, "OK"

    if kind == "TIME_EXIT":
        new_value = finite(params.get("hours"), -1.0)
        if new_value <= 0:
            return None, "INVALID_TIME_EXIT"
        old_value = default_parent_value(parent, "max_holding_hours")
        if close_enough(old_value, new_value):
            return None, "NO_PARAMETER_CHANGE"
        return {
            "parameter": "max_holding_hours",
            "old_value": old_value,
            "new_value": int(new_value) if new_value.is_integer() else new_value,
            "scenario_kind": kind,
        }, "OK"

    if kind == "ATR_TRAIL":
        new_activation = finite(params.get("activation_r"), -1.0)
        new_multiple = finite(params.get("atr_multiple"), -1.0)
        if new_activation < 0 or new_multiple <= 0:
            return None, "INVALID_ATR_TRAIL"
        old_activation = default_parent_value(parent, "trailing_at_r")
        old_multiple = default_parent_value(parent, "trailing_atr_multiple")
        changes = []
        if not close_enough(old_activation, new_activation):
            changes.append(("trailing_at_r", old_activation, new_activation))
        if not close_enough(old_multiple, new_multiple):
            changes.append(("trailing_atr_multiple", old_multiple, new_multiple))
        if not changes:
            return None, "NO_PARAMETER_CHANGE"
        if len(changes) != 1:
            return None, "REQUIRES_TWO_PARAMETER_MUTATION"
        parameter, old_value, new_value = changes[0]
        return {
            "parameter": parameter,
            "old_value": old_value,
            "new_value": new_value,
            "scenario_kind": kind,
        }, "OK"

    return None, "UNSUPPORTED_SCENARIO_KIND"


def parent_definitions(base_config: dict[str, Any], evidence: dict[str, Any]) -> list[dict[str, Any]]:
    scope = str(evidence.get("scope", "")).upper()
    portfolios = [
        item for item in base_config.get("portfolios", [])
        if isinstance(item, dict) and item.get("enabled", True)
    ]
    if scope == "PORTFOLIO":
        name = str(evidence.get("portfolio") or evidence.get("scope_value") or "")
        return [item for item in portfolios if str(item.get("name")) == name]
    if scope == "STRATEGY":
        strategy = str(evidence.get("strategy") or evidence.get("scope_value") or "")
        return [item for item in portfolios if str(item.get("strategy")) == strategy]
    return []


def evidence_key(evidence: dict[str, Any], parent_name: str) -> str:
    parts = (
        parent_name,
        evidence.get("scope"),
        evidence.get("scope_value"),
        evidence.get("scenario_set_version"),
        evidence.get("scenario_id"),
    )
    return fingerprint(parts)


def mutation_fingerprint(parent_name: str, mutation: dict[str, Any]) -> str:
    return fingerprint(
        {
            "parent": parent_name,
            "parameter": mutation["parameter"],
            "new_value": mutation["new_value"],
        }
    )


def candidate_name(parent_name: str, scenario_id: str, candidate_id: str, config: dict[str, Any]) -> str:
    prefix = re.sub(r"[^A-Za-z0-9_]+", "_", str(config["candidate_name_prefix"]))
    parent = re.sub(r"[^A-Za-z0-9_]+", "_", parent_name).strip("_") or "PARENT"
    scenario = re.sub(r"[^A-Za-z0-9_]+", "_", scenario_id).strip("_") or "MUT"
    suffix = candidate_id.replace("-", "")[:8]
    maximum = max(24, integer(config.get("maximum_candidate_name_length"), 63))
    raw = f"{prefix}_{parent}_{scenario}_{suffix}"
    if len(raw) <= maximum:
        return raw
    fixed = f"{prefix}__{scenario}_{suffix}"
    available = max(4, maximum - len(fixed))
    return f"{prefix}_{parent[:available]}_{scenario}_{suffix}"[:maximum]


def build_candidate_record(
    parent: dict[str, Any],
    evidence: dict[str, Any],
    mutation: dict[str, Any],
    config: dict[str, Any],
    when: datetime,
) -> dict[str, Any]:
    parent_name = str(parent["name"])
    parent_strategy = str(parent.get("strategy", "unknown"))
    parent_strategy_id = stable_id("portfolio", parent_name)
    mutation_key = mutation_fingerprint(parent_name, mutation)
    candidate_id = stable_id("candidate", f"{parent_strategy_id}:{mutation_key}")
    scenario_id = str(evidence.get("scenario_id", "MUTATION"))
    name = candidate_name(parent_name, scenario_id, candidate_id, config)
    version = f"1.0.1-candidate.{candidate_id.replace('-', '')[:10]}"

    definition = copy.deepcopy(parent)
    definition["name"] = name
    definition["enabled"] = bool(config.get("candidate_enabled", True))
    definition["is_main"] = False
    definition["compact_shadow"] = bool(config.get("candidate_compact_shadow", True))
    definition[mutation["parameter"]] = mutation["new_value"]
    definition.update(
        {
            "evolution_candidate": True,
            "evolution_candidate_id": candidate_id,
            "evolution_parent_portfolio": parent_name,
            "evolution_parent_strategy_id": parent_strategy_id,
            "evolution_family_id": slug(parent_strategy),
            "evolution_version": version,
            "evolution_status": "CANDIDATE",
            "evolution_mutation_parameter": mutation["parameter"],
            "evolution_mutation_old_value": mutation["old_value"],
            "evolution_mutation_new_value": mutation["new_value"],
            "evolution_source_scenario_id": scenario_id,
            "evolution_source_scope": str(evidence.get("scope", "")),
            "evolution_created_utc": iso_utc(when),
            "automatic_promotion_allowed": False,
            "live_side_effects_allowed": False,
        }
    )

    return {
        "candidate_id": candidate_id,
        "strategy_id": candidate_id,
        "family_id": slug(parent_strategy),
        "portfolio_name": name,
        "name": name,
        "version": version,
        "status": "CANDIDATE",
        "active": True,
        "parent_id": parent_strategy_id,
        "parent_portfolio": parent_name,
        "parent_strategy": parent_strategy,
        "created_by": ENGINE_VERSION,
        "created_at": iso_utc(when),
        "mutation": {
            "parameter": mutation["parameter"],
            "old_value": mutation["old_value"],
            "new_value": mutation["new_value"],
            "reason": str(evidence.get("decision_summary", "Block 4 evidence")),
            "mutation_type": "single_parameter",
            "created_at": iso_utc(when),
        },
        "source_evidence": {
            "scope": evidence.get("scope"),
            "scope_value": evidence.get("scope_value"),
            "scenario_set_version": evidence.get("scenario_set_version"),
            "scenario_id": scenario_id,
            "scenario_kind": evidence.get("scenario_kind"),
            "sample_eligible": integer(evidence.get("sample_eligible")),
            "average_delta_r": finite(evidence.get("average_delta_r")),
            "median_delta_r": finite(evidence.get("median_delta_r")),
            "bootstrap_ci_low_delta_r": finite(evidence.get("bootstrap_ci_low_delta_r")),
            "improved_pct": finite(evidence.get("improved_pct")),
            "evidence_score": finite(evidence.get("evidence_score")),
            "status": evidence.get("status"),
        },
        "mutation_fingerprint": mutation_key,
        "portfolio_definition": definition,
        "safety": {
            "paper_only": True,
            "automatic_promotion": False,
            "existing_portfolio_modified": False,
            "live_modified": False,
            "orders_sent": False,
        },
    }


def registry_payload(state: dict[str, Any], when: datetime) -> dict[str, Any]:
    candidates = [
        value for value in state.get("candidates", {}).values()
        if isinstance(value, dict)
    ]
    candidates.sort(key=lambda row: (str(row.get("created_at", "")), str(row.get("candidate_id", ""))))
    return {
        "schema_version": SCHEMA_VERSION,
        "engine_version": ENGINE_VERSION,
        "generated_utc": iso_utc(when),
        "paper_only": True,
        "automatic_promotions": 0,
        "automatic_retirements": 0,
        "live_modified": False,
        "orders_sent": False,
        "candidate_count": len(candidates),
        "active_candidate_count": sum(bool(row.get("active", True)) for row in candidates),
        "candidates": [
            {
                "strategy_id": row["strategy_id"],
                "family_id": row["family_id"],
                "name": row["name"],
                "version": row["version"],
                "status": str(row.get("status", "CANDIDATE")),
                "parent_id": row["parent_id"],
                "child_ids": [],
                "mutation": row["mutation"],
                "created_by": row["created_by"],
                "created_at": row["created_at"],
                "metadata": {
                    "source_kind": "evolution_candidate",
                    "source_path": str(REGISTRY_PATH),
                    "source_key": row["candidate_id"],
                    "legacy_profile_name": row["portfolio_name"],
                    "role": f"{str(row.get('status', 'CANDIDATE'))}_PAPER",
                    "enabled": bool(row.get("active", True)),
                    "strategy_engine": row["parent_strategy"],
                    "parent_portfolio": row["parent_portfolio"],
                    "configuration_fingerprint": fingerprint(row["portfolio_definition"]),
                    "configuration_snapshot": row["portfolio_definition"],
                    "source_evidence": row["source_evidence"],
                    "evolution_policy": {
                        "observe": True,
                        "allow_mutation": False,
                        "allow_automatic_promotion": False,
                        "allow_live_side_effects": False,
                        "require_human_approval_for_promotion": True,
                    },
                },
            }
            for row in candidates
        ],
    }


def render_report(
    state: dict[str, Any],
    new_records: list[dict[str, Any]],
    rejections: list[dict[str, Any]],
    when: datetime,
) -> str:
    candidates = list(state.get("candidates", {}).values())
    active = [row for row in candidates if bool(row.get("active", True))]
    lines = [
        "# Blocco 5 — Candidati evolutivi controllati",
        "",
        f"Generato: {iso_utc(when)}",
        "",
        "> Paper-only. Nessuna promozione, sostituzione del MASTER, modifica live o ordine reale.",
        "",
        "## Stato",
        "",
        f"- Candidati attivi: **{len(active)}**",
        f"- Nuovi candidati nel ciclo: **{len(new_records)}**",
        f"- Evidenze rifiutate nel ciclo: **{len(rejections)}**",
        "- Promozioni automatiche: **0**",
        "- Pensionamenti automatici: **0**",
        "",
        "## Regola di mutazione",
        "",
        "Ogni candidato è una copia indipendente del genitore e cambia un solo parametro scalare. Il file principale paper_trading_config.json non viene riscritto.",
        "",
        "## Candidati attivi",
        "",
        "| Candidato | Genitore | Parametro | Vecchio | Nuovo | Scenario |",
        "| --- | --- | --- | ---: | ---: | --- |",
    ]
    for row in active:
        mutation = row.get("mutation", {})
        evidence = row.get("source_evidence", {})
        lines.append(
            f"| {row.get('portfolio_name')} | {row.get('parent_portfolio')} | "
            f"{mutation.get('parameter')} | {mutation.get('old_value')} | "
            f"{mutation.get('new_value')} | {evidence.get('scenario_id')} |"
        )
    if not active:
        lines.append("| — | — | — | — | — | — |")
    lines.extend([
        "",
        "## Vincoli v1",
        "",
        "- Supportati: FIXED_R, TIME_EXIT e ATR_TRAIL solo quando richiede una singola variazione.",
        "- MFE_GIVEBACK e BREAKEVEN non vengono approssimati: restano evidenze da implementare in una versione successiva.",
        "- Nessun candidato può diventare MASTER nel Blocco 5.",
        "",
    ])
    text = "\n".join(lines)
    atomic_write_text(REPORT_PATH, text)
    return text


def prepare_candidate_config(
    base_config: dict[str, Any],
    when: datetime | None = None,
) -> dict[str, Any]:
    current = when or now_utc()
    config = load_config()
    state = load_state()
    new_records: list[dict[str, Any]] = []
    rejections: list[dict[str, Any]] = []

    if not truthy(config.get("enabled", True)):
        report = render_report(state, [], [], current)
        return {
            "config": copy.deepcopy(base_config),
            "summary": {
                "status": "DISABLED",
                "active_candidates": 0,
                "new_candidates": 0,
                "rejected_evidence": 0,
                "automatic_promotions": 0,
            },
            "report_markdown": report,
        }

    candidates_doc = load_json(INPUT_PATH, {"candidates": []})
    evidence_rows = candidates_doc.get("candidates", []) if isinstance(candidates_doc, dict) else []
    evidence_rows = [row for row in evidence_rows if isinstance(row, dict)]
    evidence_rows.sort(
        key=lambda row: (
            finite(row.get("evidence_score")),
            integer(row.get("sample_eligible")),
            finite(row.get("average_delta_r")),
        ),
        reverse=True,
    )

    existing = state.setdefault("candidates", {})
    processed = state.setdefault("processed_evidence", {})
    active_records = [row for row in existing.values() if isinstance(row, dict) and bool(row.get("active", True)) and str(row.get("status", "CANDIDATE")) == "CANDIDATE"]
    active_fingerprints = {str(row.get("mutation_fingerprint", "")) for row in active_records}
    parent_counts: dict[str, int] = {}
    for row in active_records:
        parent = str(row.get("parent_portfolio", ""))
        parent_counts[parent] = parent_counts.get(parent, 0) + 1

    maximum_active = integer(config.get("maximum_active_candidates"), 12)
    maximum_parent = integer(config.get("maximum_candidates_per_parent"), 2)
    maximum_new = integer(config.get("maximum_new_candidates_per_cycle"), 2)

    for evidence in evidence_rows:
        if len(new_records) >= maximum_new or len(active_records) + len(new_records) >= maximum_active:
            break
        scope = str(evidence.get("scope", "")).upper()
        status = str(evidence.get("status", "")).upper()
        kind = str(evidence.get("scenario_kind", "")).upper()
        if scope not in config["allowed_scopes"]:
            continue
        if status not in config["allowed_statuses"]:
            continue
        if integer(evidence.get("sample_eligible")) < integer(config.get("minimum_sample_eligible"), 120):
            continue
        if finite(evidence.get("evidence_score")) < finite(config.get("minimum_evidence_score"), 78.0):
            continue

        parents = parent_definitions(base_config, evidence)
        if not parents:
            key = fingerprint((scope, evidence.get("scope_value"), evidence.get("scenario_id")))
            if key not in processed:
                processed[key] = {"outcome": "REJECTED", "reason": "PARENT_NOT_FOUND", "processed_utc": iso_utc(current)}
                rejections.append({"reason": "PARENT_NOT_FOUND", "evidence": evidence})
            continue

        for parent in parents:
            if len(new_records) >= maximum_new or len(active_records) + len(new_records) >= maximum_active:
                break
            parent_name = str(parent.get("name", ""))
            key = evidence_key(evidence, parent_name)
            if key in processed:
                continue
            if bool(parent.get("evolution_candidate")) and not truthy(config.get("allow_recursive_candidates")):
                reason = "RECURSIVE_CANDIDATE_DISABLED"
            elif bool(parent.get("is_main")) and not truthy(config.get("allow_main_parent")):
                reason = "MAIN_PARENT_DISABLED"
            elif parent_counts.get(parent_name, 0) >= maximum_parent:
                reason = "MAX_CANDIDATES_PER_PARENT"
            elif kind not in config["supported_scenario_kinds"]:
                reason = "UNSUPPORTED_SCENARIO_KIND"
            else:
                mutation, reason = mutation_from_evidence(parent, evidence)
                if mutation is not None:
                    memory_decision = mutation_policy_decision(
                        parent,
                        mutation,
                        evidence,
                    )
                    if not bool(memory_decision.get("allow", True)):
                        reason = str(
                            memory_decision.get(
                                "reason",
                                "GENETIC_MEMORY_AVOID",
                            )
                        )
                    else:
                        regime_decision = regime_candidate_policy_decision(
                            parent,
                            evidence,
                        )
                        if not bool(regime_decision.get("allow", True)):
                            reason = str(
                                regime_decision.get(
                                    "reason",
                                    "REGIME_MEMORY_AVOID",
                                )
                            )
                        else:
                            mut_fp = mutation_fingerprint(parent_name, mutation)
                            if mut_fp in active_fingerprints:
                                reason = "DUPLICATE_MUTATION"
                            else:
                                record = build_candidate_record(parent, evidence, mutation, config, current)
                                record["genetic_memory"] = memory_decision
                                record["regime_context"] = regime_decision
                                record["portfolio_definition"]["evolution_genetic_memory_status"] = memory_decision.get("status")
                                record["portfolio_definition"]["evolution_genetic_memory_score"] = memory_decision.get("memory_score")
                                record["portfolio_definition"]["evolution_birth_regime"] = regime_decision.get("regime")
                                record["portfolio_definition"]["evolution_regime_memory_status"] = regime_decision.get("status")
                                record["portfolio_definition"]["evolution_regime_routing_mode"] = "ADVISORY_ONLY"
                                existing[record["candidate_id"]] = record
                                new_records.append(record)
                                active_fingerprints.add(mut_fp)
                                parent_counts[parent_name] = parent_counts.get(parent_name, 0) + 1
                                processed[key] = {
                                    "outcome": "CREATED",
                                    "candidate_id": record["candidate_id"],
                                    "genetic_memory": memory_decision,
                                    "regime_context": regime_decision,
                                    "processed_utc": iso_utc(current),
                                }
                                append_csv(EVENTS_PATH, EVENT_FIELDS, [{
                                    "generated_utc": iso_utc(current),
                                    "event_type": "CANDIDATE_CREATED",
                                    "candidate_id": record["candidate_id"],
                                    "candidate_portfolio": record["portfolio_name"],
                                    "parent_portfolio": record["parent_portfolio"],
                                    "parent_strategy_id": record["parent_id"],
                                    "mutation_parameter": record["mutation"]["parameter"],
                                    "old_value_json": json.dumps(record["mutation"]["old_value"]),
                                    "new_value_json": json.dumps(record["mutation"]["new_value"]),
                                    "scenario_id": evidence.get("scenario_id"),
                                    "scope": evidence.get("scope"),
                                    "evidence_score": evidence.get("evidence_score"),
                                    "sample_eligible": evidence.get("sample_eligible"),
                                    "reason": (
                                        "BLOCK4_ELIGIBLE_SINGLE_PARAMETER;"
                                        + str(memory_decision.get("status", "NO_HISTORY"))
                                        + ";REGIME_"
                                        + str(regime_decision.get("status", "NO_HISTORY"))
                                    ),
                                }])
                                continue

            processed[key] = {"outcome": "REJECTED", "reason": reason, "processed_utc": iso_utc(current)}
            rejections.append({"reason": reason, "parent": parent_name, "evidence": evidence})
            append_csv(EVENTS_PATH, EVENT_FIELDS, [{
                "generated_utc": iso_utc(current),
                "event_type": "EVIDENCE_REJECTED",
                "candidate_id": "",
                "candidate_portfolio": "",
                "parent_portfolio": parent_name,
                "parent_strategy_id": stable_id("portfolio", parent_name),
                "mutation_parameter": "",
                "old_value_json": "",
                "new_value_json": "",
                "scenario_id": evidence.get("scenario_id"),
                "scope": evidence.get("scope"),
                "evidence_score": evidence.get("evidence_score"),
                "sample_eligible": evidence.get("sample_eligible"),
                "reason": reason,
            }])

    augmented = copy.deepcopy(base_config)
    base_names = {str(row.get("name", "")) for row in augmented.get("portfolios", []) if isinstance(row, dict)}
    active_candidates = []
    for record in existing.values():
        if not isinstance(record, dict) or not bool(record.get("active", True)):
            continue
        definition = copy.deepcopy(record.get("portfolio_definition", {}))
        if not isinstance(definition, dict) or not definition.get("name"):
            continue
        if str(definition["name"]) in base_names:
            continue
        augmented.setdefault("portfolios", []).append(definition)
        base_names.add(str(definition["name"]))
        active_candidates.append(record)

    augmented, promotion_role_summary = apply_runtime_roles(augmented, state)
    validate_config(augmented)

    state["updated_utc"] = iso_utc(current)
    state.setdefault("totals", {})["created"] = integer(state.get("totals", {}).get("created")) + len(new_records)
    state.setdefault("totals", {})["rejected"] = integer(state.get("totals", {}).get("rejected")) + len(rejections)
    state.setdefault("totals", {})["automatic_promotions"] = 0
    state.setdefault("totals", {})["automatic_retirements"] = 0

    atomic_write_json(STATE_PATH, state)
    registry = registry_payload(state, current)
    atomic_write_json(REGISTRY_PATH, registry)
    report = render_report(state, new_records, rejections, current)

    return {
        "config": augmented,
        "summary": {
            "status": "OK",
            "active_candidates": sum(str(row.get("status", "CANDIDATE")) == "CANDIDATE" for row in active_candidates),
            "active_evolution_records": len(active_candidates),
            "new_candidates": len(new_records),
            "rejected_evidence": len(rejections),
            "genetic_memory_blocked": sum(
                row.get("reason") == "GENETIC_MEMORY_AVOID"
                for row in rejections
            ),
            "genetic_memory_favored": sum(
                str(row.get("genetic_memory", {}).get("status", ""))
                == "FAVOR"
                for row in new_records
            ),
            "regime_memory_blocked": sum(
                row.get("reason") == "REGIME_MEMORY_AVOID"
                for row in rejections
            ),
            "regime_memory_favored": sum(
                str(row.get("regime_context", {}).get("status", ""))
                == "FAVOR"
                for row in new_records
            ),
            "candidate_birth_regimes": sorted({
                str(row.get("regime_context", {}).get("regime", "UNKNOWN"))
                for row in new_records
            }),
            "automatic_promotions": 0,
            "automatic_retirements": 0,
            "promoted_masters": promotion_role_summary.get("masters", 0),
            "ex_masters": promotion_role_summary.get("ex_masters", 0),
            "base_portfolios_modified": False,
            "live_modified": False,
            "orders_sent": False,
        },
        "new_candidates": new_records,
        "rejections": rejections,
        "registry": registry,
        "report_markdown": report,
    }
