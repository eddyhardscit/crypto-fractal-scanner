# -*- coding: utf-8 -*-
"""Block 12: final Evolution Control Tower and tamper-evident audit chain.

This is a Paper-only observability and recovery-readiness layer. It reads the
outputs of Blocks 1-11, checks safety invariants and persistence coverage, and
writes a consolidated health report. It never restarts services, repairs files,
changes strategies, changes positions, enables live execution or sends orders.
"""
from __future__ import annotations

import csv
import hashlib
import json
import math
import os
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

REPORTS = Path("reports")
CONFIG_PATH = Path("config/evolution_control_tower_block12.json")
STATE_PATH = REPORTS / "paper_trading_evolution_control_tower_state.json"
CHECKS_PATH = REPORTS / "paper_trading_evolution_control_tower_checks.csv"
INCIDENTS_PATH = REPORTS / "paper_trading_evolution_control_tower_incidents.json"
AUDIT_PATH = REPORTS / "paper_trading_evolution_control_tower_audit_chain.csv"
RECOVERY_PATH = REPORTS / "paper_trading_evolution_recovery_readiness.json"
REPORT_PATH = REPORTS / "paper_trading_evolution_control_tower_report.md"
CONFIG_SNAPSHOT_PATH = REPORTS / "paper_trading_evolution_control_tower_config_snapshot.json"

SCHEMA_VERSION = 1
ENGINE_VERSION = "block12-evolution-control-tower-v1"
GENESIS_HASH = "GENESIS"

PIPELINE_KEYS = {
    "BLOCK3_SHADOW_EXIT": "shadow_exit",
    "BLOCK4_SHADOW_EVALUATION": "shadow_evaluation",
    "BLOCK4_5_CRASH_GUARD": "crash_guard",
    "BLOCK5_CANDIDATES": "evolution_candidates",
    "BLOCK6_VALIDATION": "evolution_candidate_validation",
    "BLOCK7_PROMOTION": "evolution_promotion_governance",
    "BLOCK8_POST_PROMOTION": "evolution_post_promotion",
    "BLOCK9_MEMORY": "evolution_memory",
    "BLOCK10_REGIME": "evolution_regime",
    "BLOCK11_LIVE_BRIDGE": "evolution_live_bridge",
}

CRITICAL_OUTPUTS = [
    "paper_trading_trade_log.csv",
    "paper_trading_shadow_exit_state.json",
    "paper_trading_shadow_evaluation_state.json",
    "paper_trading_crash_guard_state.json",
    "paper_trading_evolution_candidate_state.json",
    "paper_trading_evolution_candidate_validation_state.json",
    "paper_trading_evolution_promotion_governance_state.json",
    "paper_trading_evolution_post_promotion_state.json",
    "paper_trading_evolution_memory_state.json",
    "paper_trading_evolution_regime_state.json",
    "paper_trading_evolution_live_bridge_state.json",
]

BLOCK12_OUTPUTS = [
    "paper_trading_evolution_control_tower_state.json",
    "paper_trading_evolution_control_tower_checks.csv",
    "paper_trading_evolution_control_tower_incidents.json",
    "paper_trading_evolution_control_tower_audit_chain.csv",
    "paper_trading_evolution_recovery_readiness.json",
    "paper_trading_evolution_control_tower_report.md",
    "paper_trading_evolution_control_tower_config_snapshot.json",
]

DEFAULT_CONFIG = {
    "schema_version": 1,
    "enabled": True,
    "paper_only": True,
    "mode": "OBSERVE_AUDIT_ONLY",
    "max_output_age_hours": 24.0,
    "critical_outputs": CRITICAL_OUTPUTS,
    "required_storage_files": CRITICAL_OUTPUTS + BLOCK12_OUTPUTS,
    "observe_systemd": True,
    "paper_timer_unit": "crypto-paper-main.timer",
    "candidate_sync_unit": "crypto-evolution-candidate-sync.service",
    "sol_live_service_unit": "sol-live.service",
    "sol_live_timer_unit": "sol-live.timer",
    "require_live_bridge_mode": "LOCKED_REVIEW_ONLY",
    "require_live_adapter_unconfigured": True,
    "require_live_execution_disabled": True,
    "require_regime_advisory_only": True,
    "automatic_repairs": False,
    "automatic_restarts": False,
    "automatic_mutations": False,
    "automatic_promotions": False,
    "automatic_retirements": False,
    "automatic_rollbacks": False,
    "automatic_releases": False,
    "live_side_effects_allowed": False,
    "orders_allowed": False,
    "telegram_alerts": False,
}

CHECK_FIELDS = [
    "generated_utc", "category", "check_id", "status", "severity",
    "observed", "expected", "detail",
]
AUDIT_FIELDS = [
    "generated_utc", "cycle_number", "health", "check_count",
    "warning_count", "critical_count", "pipeline_complete", "live_locked",
    "storage_complete", "recovery_status", "previous_hash", "record_hash",
]


def now_utc() -> datetime:
    return datetime.now(timezone.utc)


def iso(value: datetime | None = None) -> str:
    return (value or now_utc()).astimezone(timezone.utc).isoformat(timespec="seconds")


def truthy(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    return str(value).strip().lower() in {"1", "true", "yes", "y", "on"}


def integer(value: Any, default: int = 0) -> int:
    try:
        return int(float(value))
    except (TypeError, ValueError, OverflowError):
        return default


def finite(value: Any, default: float = 0.0) -> float:
    try:
        number = float(value)
    except (TypeError, ValueError):
        return default
    return number if math.isfinite(number) else default


def load_json(path: Path, default: Any) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return default


def atomic_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(text, encoding="utf-8")
    temporary.replace(path)


def atomic_json(path: Path, payload: Any) -> None:
    atomic_text(path, json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n")


def write_csv(path: Path, fields: list[str], rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    with temporary.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fields})
    temporary.replace(path)


def append_csv(path: Path, fields: list[str], row: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    exists = path.exists() and path.stat().st_size > 0
    with path.open("a", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        if not exists:
            writer.writeheader()
        writer.writerow({field: row.get(field, "") for field in fields})


def load_config(write_snapshot: bool = True) -> dict[str, Any]:
    custom = load_json(CONFIG_PATH, {})
    config = dict(DEFAULT_CONFIG)
    if isinstance(custom, dict):
        config.update(custom)
    # Safety values cannot be enabled by configuration in Block 12.
    for key in (
        "automatic_repairs", "automatic_restarts", "automatic_mutations",
        "automatic_promotions", "automatic_retirements", "automatic_rollbacks",
        "automatic_releases", "live_side_effects_allowed", "orders_allowed",
        "telegram_alerts",
    ):
        config[key] = False
    config["paper_only"] = True
    config["mode"] = "OBSERVE_AUDIT_ONLY"
    if write_snapshot:
        atomic_json(CONFIG_SNAPSHOT_PATH, config)
    return config


def check(
    when: datetime,
    category: str,
    check_id: str,
    status: str,
    severity: str,
    observed: Any,
    expected: Any,
    detail: str,
) -> dict[str, Any]:
    return {
        "generated_utc": iso(when), "category": category, "check_id": check_id,
        "status": status, "severity": severity,
        "observed": json.dumps(observed, ensure_ascii=False, sort_keys=True)
        if isinstance(observed, (dict, list)) else str(observed),
        "expected": json.dumps(expected, ensure_ascii=False, sort_keys=True)
        if isinstance(expected, (dict, list)) else str(expected),
        "detail": detail,
    }


def _canonical_audit(row: dict[str, Any]) -> str:
    payload = {field: str(row.get(field, "")) for field in AUDIT_FIELDS if field != "record_hash"}
    return json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def audit_hash(row: dict[str, Any]) -> str:
    return hashlib.sha256(_canonical_audit(row).encode("utf-8")).hexdigest()


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    try:
        with path.open("r", encoding="utf-8", newline="") as handle:
            return list(csv.DictReader(handle))
    except (OSError, csv.Error):
        return []


def verify_audit_chain(path: Path = AUDIT_PATH) -> dict[str, Any]:
    if not path.exists() or path.stat().st_size == 0:
        return {"valid": True, "rows": 0, "last_hash": GENESIS_HASH, "error": ""}
    rows = read_csv(path)
    previous = GENESIS_HASH
    for index, row in enumerate(rows, 1):
        if str(row.get("previous_hash", "")) != previous:
            return {
                "valid": False, "rows": len(rows), "last_hash": previous,
                "error": f"previous_hash mismatch at row {index}",
            }
        expected = audit_hash(row)
        if str(row.get("record_hash", "")) != expected:
            return {
                "valid": False, "rows": len(rows), "last_hash": previous,
                "error": f"record_hash mismatch at row {index}",
            }
        previous = expected
    return {"valid": True, "rows": len(rows), "last_hash": previous, "error": ""}


def append_audit_record(path: Path, payload: dict[str, Any]) -> dict[str, Any]:
    before = verify_audit_chain(path)
    if not before["valid"]:
        return before
    row = {field: payload.get(field, "") for field in AUDIT_FIELDS}
    row["previous_hash"] = before["last_hash"]
    row["record_hash"] = audit_hash(row)
    append_csv(path, AUDIT_FIELDS, row)
    after = verify_audit_chain(path)
    after["appended_hash"] = row["record_hash"]
    return after


def _systemd(unit: str) -> dict[str, str]:
    try:
        result = subprocess.run(
            [
                "systemctl", "show", unit, "--no-pager",
                "--property=ActiveState", "--property=SubState",
                "--property=UnitFileState",
            ],
            capture_output=True, text=True, timeout=8, check=False,
        )
    except Exception as exc:
        return {"available": "false", "error": str(exc)}
    values: dict[str, str] = {"available": "true" if result.returncode == 0 else "false"}
    for line in result.stdout.splitlines():
        if "=" in line:
            key, value = line.split("=", 1)
            values[key] = value
    if result.returncode != 0:
        values["error"] = (result.stderr or result.stdout).strip()[:500]
    return values


def _status_value(value: Any) -> str:
    return str(value or "").strip().upper()


def _storage_files() -> set[str]:
    try:
        from paper_trading_storage import FILES
        return {str(item) for item in FILES}
    except Exception:
        return set()


def _automatic_or_live_violations(summary: dict[str, Any]) -> list[tuple[str, Any]]:
    violations: list[tuple[str, Any]] = []
    count_keys = {
        "automatic_mutations", "automatic_promotions", "automatic_retirements",
        "automatic_rollbacks", "automatic_releases", "automatic_strategy_switches",
        "automatic_position_changes",
    }
    bool_keys = {
        "live_modified", "orders_sent", "live_execution_enabled",
        "existing_strategies_modified", "candidate_state_modified",
        "promotion_state_modified",
    }
    for block_name, block in summary.items():
        if not isinstance(block, dict):
            continue
        for key in count_keys:
            if integer(block.get(key)) != 0:
                violations.append((f"{block_name}.{key}", block.get(key)))
        for key in bool_keys:
            if truthy(block.get(key)):
                violations.append((f"{block_name}.{key}", block.get(key)))
    return violations


def _render_report(result: dict[str, Any]) -> str:
    lines = [
        "# Blocco 12 — Evolution Control Tower", "",
        f"Generato: {result['generated_utc']}", "",
        "> Ultimo livello di osservabilità della pipeline. Non ripara, non riavvia, "
        "non modifica strategie o posizioni e non invia ordini.", "",
        "## Stato generale", "",
        f"- Salute: **{result['health']}**",
        f"- Pipeline completa: **{'SI' if result['pipeline_complete'] else 'NO'}**",
        f"- Live bloccato: **{'SI' if result['live_locked'] else 'NO'}**",
        f"- Persistenza completa: **{'SI' if result['storage_complete'] else 'NO'}**",
        f"- Catena audit valida: **{'SI' if result['audit_chain_valid'] else 'NO'}**",
        f"- Recovery readiness: **{result['recovery_status']}**",
        f"- Controlli: **{result['check_count']}**",
        f"- Warning: **{result['warning_count']}**",
        f"- Critici: **{result['critical_count']}**", "",
        "## Controlli non superati", "",
        "| Categoria | Controllo | Stato | Severità | Dettaglio |",
        "| --- | --- | --- | --- | --- |",
    ]
    failures = [row for row in result.get("checks", []) if row.get("status") != "PASS"]
    for row in failures:
        lines.append(
            f"| {row.get('category')} | {row.get('check_id')} | {row.get('status')} | "
            f"{row.get('severity')} | {row.get('detail')} |"
        )
    if not failures:
        lines.append("| — | Tutti i controlli | PASS | INFO | Nessuna anomalia |")
    lines += [
        "", "## Sicurezza", "",
        "- Riparazioni automatiche: **0**",
        "- Riavvii automatici: **0**",
        "- Mutazioni/promozioni/rollback/rilasci automatici: **0**",
        "- Modifiche live: **NO**",
        "- Ordini reali: **0**", "",
    ]
    return "\n".join(lines)


def run_control_tower_cycle(
    summary: dict[str, Any] | None = None,
    market_bundle: dict[str, Any] | None = None,
    when: datetime | None = None,
) -> dict[str, Any]:
    current = when or now_utc()
    config = load_config()
    summary = summary if isinstance(summary, dict) else {}
    market_bundle = market_bundle if isinstance(market_bundle, dict) else {}
    if not truthy(config.get("enabled", True)):
        return {
            "enabled": False, "status": "DISABLED", "health": "DISABLED",
            "check_count": 0, "warning_count": 0, "critical_count": 0,
            "pipeline_complete": False, "live_locked": True,
            "storage_complete": False, "audit_chain_valid": True,
            "recovery_status": "DISABLED", "automatic_actions": 0,
            "live_modified": False, "orders_sent": False,
            "report_markdown": "",
        }

    checks: list[dict[str, Any]] = []
    missing_pipeline = 0
    pipeline_errors = 0
    for label, key in PIPELINE_KEYS.items():
        block = summary.get(key)
        if not isinstance(block, dict):
            missing_pipeline += 1
            checks.append(check(
                current, "PIPELINE", label, "BOOTSTRAP", "WARN", "MISSING",
                "BLOCK SUMMARY PRESENT", "Riepilogo del blocco non ancora disponibile.",
            ))
            continue
        status = _status_value(block.get("status"))
        if status in {"ERROR", "FAILED", "CRITICAL"}:
            pipeline_errors += 1
            checks.append(check(
                current, "PIPELINE", label, "FAIL", "CRITICAL", status,
                "NOT ERROR", "Il blocco ha dichiarato un errore operativo.",
            ))
        else:
            checks.append(check(
                current, "PIPELINE", label, "PASS", "INFO", status or "NO_STATUS",
                "NOT ERROR", "Blocco presente e senza errore dichiarato.",
            ))

    live_bridge = summary.get("evolution_live_bridge", {})
    if not isinstance(live_bridge, dict):
        live_bridge = {}
    required_mode = str(config.get("require_live_bridge_mode", "LOCKED_REVIEW_ONLY"))
    mode_ok = str(live_bridge.get("mode", required_mode)) == required_mode
    checks.append(check(
        current, "SAFETY", "LIVE_BRIDGE_MODE",
        "PASS" if mode_ok else "FAIL", "INFO" if mode_ok else "CRITICAL",
        live_bridge.get("mode", "MISSING"), required_mode,
        "Il bridge deve restare bloccato alla sola revisione.",
    ))
    execution_disabled = not truthy(live_bridge.get("live_execution_enabled"))
    checks.append(check(
        current, "SAFETY", "LIVE_EXECUTION_DISABLED",
        "PASS" if execution_disabled else "FAIL",
        "INFO" if execution_disabled else "CRITICAL",
        live_bridge.get("live_execution_enabled", False), False,
        "L'esecuzione live deve restare disabilitata.",
    ))
    adapter_unconfigured = not truthy(live_bridge.get("live_adapter_configured"))
    checks.append(check(
        current, "SAFETY", "LIVE_ADAPTER_UNCONFIGURED",
        "PASS" if adapter_unconfigured else "FAIL",
        "INFO" if adapter_unconfigured else "CRITICAL",
        live_bridge.get("live_adapter_configured", False), False,
        "L'adattatore live resta volutamente non configurato.",
    ))

    violations = _automatic_or_live_violations(summary)
    checks.append(check(
        current, "SAFETY", "NO_AUTOMATIC_OR_LIVE_SIDE_EFFECTS",
        "PASS" if not violations else "FAIL",
        "INFO" if not violations else "CRITICAL",
        violations, [],
        "Nessuna azione automatica o modifica live è consentita.",
    ))

    regime = summary.get("evolution_regime", {})
    if not isinstance(regime, dict):
        regime = {}
    routing = str(regime.get("routing_mode", "ADVISORY_ONLY"))
    routing_ok = routing == "ADVISORY_ONLY"
    checks.append(check(
        current, "SAFETY", "REGIME_ROUTING_ADVISORY",
        "PASS" if routing_ok else "WARN", "INFO" if routing_ok else "WARN",
        routing, "ADVISORY_ONLY",
        "Il routing automatico non deve essere attivo nel rollout iniziale.",
    ))

    freshness = str((market_bundle.get("_paper_freshness", {}) or {}).get("status", "UNKNOWN")).upper()
    freshness_ok = freshness not in {"STALE", "ERROR", "INVALID"}
    checks.append(check(
        current, "DATA", "MARKET_DATA_FRESHNESS",
        "PASS" if freshness_ok else "WARN", "INFO" if freshness_ok else "WARN",
        freshness, "NOT STALE/ERROR",
        "La freschezza dati è osservata; il Crash Guard resta il filtro operativo.",
    ))

    max_age = finite(config.get("max_output_age_hours"), 24.0)
    missing_outputs = 0
    stale_outputs = 0
    for filename in list(config.get("critical_outputs", CRITICAL_OUTPUTS)):
        path = REPORTS / str(filename)
        if not path.is_file() or path.stat().st_size == 0:
            missing_outputs += 1
            checks.append(check(
                current, "FILES", str(filename), "BOOTSTRAP", "WARN", "MISSING",
                "NONEMPTY FILE", "Output non ancora inizializzato o mancante.",
            ))
            continue
        age_hours = max(0.0, (current.timestamp() - path.stat().st_mtime) / 3600.0)
        fresh = age_hours <= max_age
        if not fresh:
            stale_outputs += 1
        checks.append(check(
            current, "FILES", str(filename), "PASS" if fresh else "WARN",
            "INFO" if fresh else "WARN", round(age_hours, 3), f"<= {max_age}h",
            "Controllo presenza e freschezza dell'output persistente.",
        ))

    storage_files = _storage_files()
    required_storage = {str(item) for item in config.get("required_storage_files", [])}
    missing_storage = sorted(required_storage - storage_files)
    storage_complete = bool(storage_files) and not missing_storage
    checks.append(check(
        current, "PERSISTENCE", "STORAGE_MANIFEST_COMPLETE",
        "PASS" if storage_complete else "FAIL",
        "INFO" if storage_complete else "CRITICAL",
        missing_storage if storage_files else "STORAGE_IMPORT_FAILED", [],
        "Tutti gli stati critici e gli output Block 12 devono essere nel bundle persistente.",
    ))

    chain_before = verify_audit_chain(AUDIT_PATH)
    checks.append(check(
        current, "INTEGRITY", "AUDIT_CHAIN_PRECHECK",
        "PASS" if chain_before["valid"] else "FAIL",
        "INFO" if chain_before["valid"] else "CRITICAL",
        chain_before.get("error") or f"rows={chain_before.get('rows', 0)}", "VALID",
        "La catena hash non deve presentare modifiche retroattive.",
    ))

    systemd_snapshot: dict[str, Any] = {}
    if truthy(config.get("observe_systemd", True)):
        units = {
            "paper_timer": str(config.get("paper_timer_unit")),
            "candidate_sync": str(config.get("candidate_sync_unit")),
            "sol_live_service": str(config.get("sol_live_service_unit")),
            "sol_live_timer": str(config.get("sol_live_timer_unit")),
        }
        for name, unit in units.items():
            observation = _systemd(unit)
            systemd_snapshot[name] = observation
            available = observation.get("available") == "true"
            enabled_ok = observation.get("UnitFileState") in {"enabled", "static", "indirect"}
            status = "PASS" if available and (not name.endswith("timer") or enabled_ok) else "WARN"
            checks.append(check(
                current, "SYSTEMD", name, status, "INFO" if status == "PASS" else "WARN",
                observation, "OBSERVABLE; TIMERS ENABLED",
                "Osservazione read-only: nessun servizio viene riavviato o modificato.",
            ))

    critical_count = sum(row["status"] == "FAIL" for row in checks)
    warning_count = sum(row["status"] == "WARN" for row in checks)
    bootstrap_count = sum(row["status"] == "BOOTSTRAP" for row in checks)
    pipeline_complete = missing_pipeline == 0 and pipeline_errors == 0
    live_locked = mode_ok and execution_disabled and adapter_unconfigured and not violations

    if critical_count:
        health = "CRITICAL"
    elif bootstrap_count:
        health = "BOOTSTRAPPING"
    elif warning_count:
        health = "DEGRADED"
    else:
        health = "HEALTHY"

    recovery_ready = (
        storage_complete and chain_before["valid"] and live_locked
        and os.access(REPORTS, os.W_OK) and pipeline_complete
        and missing_outputs == 0
    )
    recovery_status = "READY" if recovery_ready else (
        "BLOCKED" if critical_count else "BUILDING"
    )

    previous_state = load_json(STATE_PATH, {})
    cycle_number = integer(previous_state.get("cycles"), 0) + 1 if isinstance(previous_state, dict) else 1
    audit_payload = {
        "generated_utc": iso(current), "cycle_number": cycle_number,
        "health": health, "check_count": len(checks),
        "warning_count": warning_count + bootstrap_count,
        "critical_count": critical_count,
        "pipeline_complete": pipeline_complete, "live_locked": live_locked,
        "storage_complete": storage_complete, "recovery_status": recovery_status,
    }
    chain_after = chain_before
    if chain_before["valid"]:
        chain_after = append_audit_record(AUDIT_PATH, audit_payload)
    if not chain_after.get("valid", False):
        health = "CRITICAL"
        recovery_status = "BLOCKED"
        critical_count += 1
        checks.append(check(
            current, "INTEGRITY", "AUDIT_CHAIN_APPEND", "FAIL", "CRITICAL",
            chain_after.get("error", "UNKNOWN"), "VALID",
            "Impossibile estendere in modo valido la catena audit.",
        ))
    else:
        checks.append(check(
            current, "INTEGRITY", "AUDIT_CHAIN_APPEND", "PASS", "INFO",
            chain_after.get("appended_hash", chain_after.get("last_hash")), "VALID HASH",
            "Record del ciclo aggiunto alla catena tamper-evident.",
        ))

    result = {
        "schema_version": SCHEMA_VERSION, "engine_version": ENGINE_VERSION,
        "generated_utc": iso(current), "enabled": True, "status": "OK",
        "mode": "OBSERVE_AUDIT_ONLY", "health": health,
        "check_count": len(checks),
        "warning_count": sum(row["status"] in {"WARN", "BOOTSTRAP"} for row in checks),
        "critical_count": sum(row["status"] == "FAIL" for row in checks),
        "bootstrap_count": sum(row["status"] == "BOOTSTRAP" for row in checks),
        "pipeline_complete": pipeline_complete, "live_locked": live_locked,
        "storage_complete": storage_complete,
        "audit_chain_valid": bool(chain_after.get("valid")),
        "audit_rows": integer(chain_after.get("rows")),
        "audit_last_hash": chain_after.get("last_hash", chain_after.get("appended_hash", GENESIS_HASH)),
        "recovery_status": recovery_status,
        "missing_outputs": missing_outputs, "stale_outputs": stale_outputs,
        "systemd": systemd_snapshot, "checks": checks,
        "automatic_repairs": 0, "automatic_restarts": 0,
        "automatic_mutations": 0, "automatic_promotions": 0,
        "automatic_retirements": 0, "automatic_rollbacks": 0,
        "automatic_releases": 0, "live_modified": False,
        "orders_sent": False, "telegram_sent": False,
    }
    report = _render_report(result)
    result["report_markdown"] = report

    write_csv(CHECKS_PATH, CHECK_FIELDS, checks)
    atomic_json(INCIDENTS_PATH, {
        "schema_version": SCHEMA_VERSION, "generated_utc": iso(current),
        "health": health,
        "incidents": [row for row in checks if row["status"] in {"FAIL", "WARN", "BOOTSTRAP"}],
        "automatic_actions": 0, "live_modified": False, "orders_sent": False,
    })
    atomic_json(RECOVERY_PATH, {
        "schema_version": SCHEMA_VERSION, "generated_utc": iso(current),
        "status": recovery_status, "reports_writable": os.access(REPORTS, os.W_OK),
        "storage_complete": storage_complete,
        "audit_chain_valid": bool(chain_after.get("valid")),
        "pipeline_complete": pipeline_complete, "live_locked": live_locked,
        "automatic_restore": False, "automatic_rollback": False,
        "manual_recovery_required": True,
    })
    atomic_json(STATE_PATH, {
        "schema_version": SCHEMA_VERSION, "engine_version": ENGINE_VERSION,
        "created_utc": previous_state.get("created_utc", iso(current)) if isinstance(previous_state, dict) else iso(current),
        "updated_utc": iso(current), "cycles": cycle_number,
        "health": health, "pipeline_complete": pipeline_complete,
        "live_locked": live_locked, "storage_complete": storage_complete,
        "audit_chain_valid": bool(chain_after.get("valid")),
        "audit_last_hash": chain_after.get("last_hash", chain_after.get("appended_hash", GENESIS_HASH)),
        "recovery_status": recovery_status,
        "automatic_actions": 0, "live_modified": False, "orders_sent": False,
    })
    atomic_text(REPORT_PATH, report + "\n")
    return result
