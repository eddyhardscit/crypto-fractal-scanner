#!/usr/bin/env python3
"""Evolution remote runtime snapshot V3.

Authoritative identity rules:
- current profiles come exactly from local paper_trading_config.json;
- remote active/state profiles come exactly from the remote config snapshot;
- imported historical profiles come from the Evolution registry;
- historical profiles absent from remote state but present in permanent ledgers
  are classified as ARCHIVED_LEDGER_ONLY, not as errors.

The script downloads the Paper GitHub Release assets entirely in memory.
It never calls restore/upload, never writes operational Paper files, never
restarts services and never sends orders.

Writes only:
- data/evolution/runtime_snapshot.json
- reports/evolution_runtime_snapshot.md
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any

import evolution_runtime_snapshot as base
import evolution_runtime_snapshot_remote as remote


CURRENT_SOURCE = "paper_portfolio"
HISTORICAL_SOURCE = "historical_paper_profile"
CANDIDATE_SOURCE = "evolution_candidate"


def source_kind(record: dict[str, Any]) -> str:
    return str((record.get("metadata") or {}).get("source_kind") or "")


def record_profile_name(record: dict[str, Any]) -> str:
    metadata = record.get("metadata") or {}
    return str(
        metadata.get("legacy_profile_name")
        or record.get("name")
        or metadata.get("source_key")
        or ""
    ).strip()


def load_wrapper_environment() -> str | None:
    """Load ENV_FILE used by the Paper wrapper, without printing its contents."""
    wrapper = Path("/usr/local/sbin/crypto-paper-main-cycle")
    if not wrapper.exists():
        return None

    try:
        text = wrapper.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None

    match = re.search(
        r"(?m)^\s*ENV_FILE\s*=\s*(?P<value>[^\n#]+)",
        text,
    )
    if not match:
        return None

    value = match.group("value").strip()
    if (
        len(value) >= 2
        and value[0] == value[-1]
        and value[0] in {"'", '"'}
    ):
        value = value[1:-1]

    path = Path(os.path.expandvars(value)).expanduser()
    if not path.is_absolute():
        path = wrapper.parent / path

    if path.exists() and path.is_file():
        remote.load_env_file(path)
        return str(path)
    return None


def portfolio_names(document: Any) -> list[str]:
    if not isinstance(document, dict):
        return []

    portfolios = document.get("portfolios", [])
    names: set[str] = set()

    if isinstance(portfolios, list):
        for item in portfolios:
            if not isinstance(item, dict):
                continue
            name = str(item.get("name") or "").strip()
            if name:
                names.add(name)

    elif isinstance(portfolios, dict):
        for key, item in portfolios.items():
            if not isinstance(item, dict):
                continue
            name = str(item.get("name") or key).strip()
            if name:
                names.add(name)

    return sorted(names)


def build_profile(
    record: dict[str, Any],
    state_by_name: dict[str, dict[str, Any]],
    trades_by_name: dict[str, list[dict[str, str]]],
    equity_by_name: dict[str, list[dict[str, str]]],
    positions_by_name: dict[str, list[dict[str, str]]],
    signals_by_name: dict[str, list[dict[str, str]]],
    *,
    current_names: set[str],
    remote_state_names: set[str],
) -> dict[str, Any]:
    name = record_profile_name(record)
    metadata = record.get("metadata") or {}
    historical = source_kind(record) == HISTORICAL_SOURCE

    state = state_by_name.get(name, {})
    trades = trades_by_name.get(name, [])
    equities = equity_by_name.get(name, [])
    position_rows = positions_by_name.get(name, [])
    signals = signals_by_name.get(name, [])

    state_positions = state.get("open_positions", [])
    normalized_positions: list[dict[str, Any]] = []

    if isinstance(state_positions, list):
        normalized_positions = [
            base.normalize_position(item)
            for item in state_positions
            if isinstance(item, dict)
        ]

    if not normalized_positions:
        normalized_positions = [
            base.normalize_position(item)
            for item in position_rows
        ]

    latest_equity = base.latest_equity(equities)
    trade_summary = base.extract_trade_summary(trades, state)

    balance = base.safe_float(
        base.first_present(
            state,
            ("balance_eur", "cash_eur", "balance"),
        )
    )
    equity = base.safe_float(
        base.first_present(
            state,
            ("equity_eur", "portfolio_equity_eur", "equity"),
        )
    )
    peak_equity = base.safe_float(
        base.first_present(
            state,
            ("peak_equity_eur", "peak_equity"),
        )
    )
    max_drawdown = base.safe_float(
        base.first_present(
            state,
            ("max_drawdown_pct", "drawdown_pct"),
        )
    )

    if latest_equity:
        if balance is None:
            balance = latest_equity.get("balance_eur")
        if equity is None:
            equity = latest_equity.get("equity_eur")
        if peak_equity is None:
            peak_equity = latest_equity.get("peak_equity_eur")
        if max_drawdown is None:
            max_drawdown = latest_equity.get("drawdown_pct")

    last_signal = (
        base.row_timestamp(signals[-1])
        if signals
        else None
    )
    last_activity = (
        trade_summary.get("last_trade_activity")
        or last_signal
        or (
            latest_equity.get("timestamp")
            if latest_equity
            else None
        )
    )

    if name in current_names:
        runtime_class = "CURRENT"
    elif name in remote_state_names:
        runtime_class = "HISTORICAL_REMOTE_STATE"
    else:
        runtime_class = "ARCHIVED_LEDGER_ONLY"

    if historical and normalized_positions:
        activity_class = "HISTORICAL_OPEN_REVIEW"
    elif normalized_positions:
        activity_class = "ACTIVE_POSITION"
    elif trade_summary.get("closed_trades") or signals:
        activity_class = "HAS_HISTORY"
    else:
        activity_class = "ZERO_ACTIVITY"

    return {
        "strategy_id": record.get("strategy_id"),
        "family_id": record.get("family_id"),
        "profile_name": name,
        "source_kind": source_kind(record),
        "runtime_class": runtime_class,
        "role": metadata.get("role"),
        "lifecycle_status": record.get("status"),
        "enabled": metadata.get("enabled"),
        "strategy_engine": metadata.get("strategy_engine"),
        "historical_background": historical,
        "reactivation_blocked": bool(
            metadata.get("reactivation_blocked", historical)
        ),
        "requires_open_position_review": bool(
            metadata.get("requires_open_position_review")
            or (historical and normalized_positions)
        ),
        "balance_eur": balance,
        "equity_eur": equity,
        "peak_equity_eur": peak_equity,
        "max_drawdown_pct": max_drawdown,
        "open_position_count": len(normalized_positions),
        "open_positions": normalized_positions,
        "trade_summary": trade_summary,
        "signal_log_rows": len(signals),
        "last_activity": last_activity,
        "activity_class": activity_class,
        "source_presence": {
            "remote_state": name in state_by_name,
            "trade_ledger": bool(trades),
            "equity_log": bool(equities),
            "open_positions_csv": bool(position_rows),
            "signal_ledger": bool(signals),
        },
    }


def render_markdown(snapshot: dict[str, Any]) -> str:
    summary = snapshot["summary"]
    validation = snapshot["validation"]

    lines = [
        "# Evolution Runtime Snapshot V3",
        "",
        f"Generated: `{snapshot['generated_at']}`",
        "",
        "> Observation only. Identity mapping uses exact local and remote configuration names.",
        "",
        "## Summary",
        "",
        f"- Registered strategies: **{summary['registered_strategy_count']}**",
        f"- Current profiles: **{summary['current_profile_count']}**",
        f"- Historical profiles: **{summary['historical_profile_count']}**",
        f"- Evolution candidates: **{summary.get('candidate_profile_count', 0)}**",
        f"- Candidate open positions: **{summary.get('candidate_open_position_count', 0)}**",
        f"- Historical profiles in remote state: **{summary['historical_remote_state_count']}**",
        f"- Historical ledger-only profiles: **{summary['historical_ledger_only_count']}**",
        f"- Current accounts with open positions: **{summary['current_accounts_with_open_positions']}**",
        f"- Current open positions: **{summary['current_open_position_count']}**",
        f"- Historical profiles requiring review: **{summary['historical_open_review_count']}**",
        f"- Historical open markers: **{summary['historical_open_marker_count']}**",
        f"- Permanent trades: **{summary['permanent_trade_rows']}**",
        f"- Permanent signals: **{summary['permanent_signal_rows']}**",
        f"- Unmapped runtime profiles: **{summary['unmapped_runtime_profile_count']}**",
        f"- Validation: **{'OK' if validation['valid'] else 'ATTENTION'}**",
        "",
        "## Current profiles",
        "",
        "| Profile | Role | Status | Closed | Open | Activity |",
        "|---|---|---|---:|---:|---|",
    ]

    for item in snapshot["current_paper_profiles"]:
        lines.append(
            f"| {item['profile_name']} | {item.get('role')} | "
            f"{item.get('lifecycle_status')} | "
            f"{item['trade_summary'].get('closed_trades')} | "
            f"{item.get('open_position_count')} | "
            f"{item.get('activity_class')} |"
        )

    lines += [
        "",
        "## Evolution CANDIDATE profiles",
        "",
        "| Profile | Parent | Status | Closed | Open | Activity |",
        "|---|---|---|---:|---:|---|",
    ]

    for item in snapshot.get("evolution_candidate_profiles", []):
        lines.append(
            f"| {item['profile_name']} | — | "
            f"{item.get('lifecycle_status')} | "
            f"{item['trade_summary'].get('closed_trades')} | "
            f"{item.get('open_position_count')} | "
            f"{item.get('activity_class')} |"
        )

    lines += [
        "",
        "## Historical BACKGROUND profiles",
        "",
        "| Profile | Runtime class | Family | Closed | Open | Review |",
        "|---|---|---|---:|---:|:---:|",
    ]

    for item in snapshot["historical_background_profiles"]:
        lines.append(
            f"| {item['profile_name']} | {item['runtime_class']} | "
            f"{item.get('family_id')} | "
            f"{item['trade_summary'].get('closed_trades')} | "
            f"{item.get('open_position_count')} | "
            f"{'yes' if item.get('requires_open_position_review') else 'no'} |"
        )

    lines += [
        "",
        "## Validation",
        "",
        "```json",
        json.dumps(
            validation,
            indent=2,
            ensure_ascii=False,
            sort_keys=True,
        ),
        "```",
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", default=".")
    parser.add_argument(
        "--output",
        default="data/evolution/runtime_snapshot.json",
    )
    parser.add_argument(
        "--markdown-output",
        default="reports/evolution_runtime_snapshot.md",
    )
    args = parser.parse_args()

    repo = Path(args.repo).expanduser().resolve()
    if not repo.is_dir():
        raise SystemExit(f"Repository not found: {repo}")

    os.chdir(repo)
    if str(repo) not in sys.path:
        sys.path.insert(0, str(repo))

    remote.load_service_environment(repo)
    wrapper_env = load_wrapper_environment()

    import paper_trading_storage as storage

    client = storage.session()
    response = client.get(
        storage.api_url(
            f"/releases/tags/{storage.RELEASE_TAG}"
        ),
        timeout=30,
    )
    if response.status_code >= 400:
        raise RuntimeError(
            f"Cannot read Paper release: HTTP {response.status_code}"
        )
    release = response.json()

    state_asset = remote.release_asset(
        release,
        storage.ASSET_NAME,
    )
    trade_asset = remote.release_asset(
        release,
        storage.TRADE_LEDGER_ASSET_NAME,
    )
    signal_asset = remote.release_asset(
        release,
        storage.SIGNAL_LEDGER_ASSET_NAME,
    )

    state_zip = storage.download_asset_bytes(
        client,
        state_asset,
    )
    trade_rows = remote.parse_csv_bytes(
        storage.download_asset_bytes(
            client,
            trade_asset,
        )
    )
    signal_rows = remote.parse_csv_bytes(
        storage.download_asset_bytes(
            client,
            signal_asset,
        )
    )

    errors: dict[str, str] = {}

    paper_state, error = remote.zip_json(
        state_zip,
        "paper_trading_state.json",
    )
    if error:
        errors["paper_state"] = error

    remote_config, error = remote.zip_json(
        state_zip,
        "paper_trading_config_snapshot.json",
    )
    if error:
        errors["remote_config"] = error

    equity_rows, error = remote.zip_csv(
        state_zip,
        "paper_trading_equity.csv",
    )
    if error:
        errors["paper_equity"] = error

    open_rows, error = remote.zip_csv(
        state_zip,
        "paper_trading_open_positions.csv",
    )
    if error:
        errors["paper_open_positions"] = error

    research_state, error = remote.zip_json(
        state_zip,
        "research_all_signals_state.json",
    )
    if error:
        errors["research_state"] = error

    local_config, error = base.read_json(
        repo / "paper_trading_config.json"
    )
    if error:
        raise RuntimeError(
            f"Cannot read local paper configuration: {error}"
        )

    registry_doc, error = base.read_json(
        repo / "data/evolution/strategy_registry.json"
    )
    if error:
        raise RuntimeError(
            f"Cannot read strategy registry: {error}"
        )

    research_layers, error = base.read_json(
        repo / "data/evolution/research_layers.json"
    )
    if error:
        errors["research_layers"] = error

    deployments, error = base.read_json(
        repo / "data/evolution/deployments.json"
    )
    if error:
        errors["deployments"] = error

    sol_paper_state, error = base.read_json(
        repo / "reports/sol_spot_adaptive_state.json"
    )
    if error:
        errors["sol_paper_state"] = error

    sol_live_state, error = base.read_json(
        repo / "reports/sol_spot_live_state.json"
    )
    if error:
        errors["sol_live_state"] = error

    sol_live_status, error = base.read_json(
        repo / "reports/sol_spot_live_status.json"
    )
    if error:
        errors["sol_live_status"] = error

    records = base.registry_records(registry_doc)

    current_records = [
        item
        for item in records
        if source_kind(item) == CURRENT_SOURCE
    ]
    historical_records = [
        item
        for item in records
        if source_kind(item) == HISTORICAL_SOURCE
    ]
    candidate_records = [
        item
        for item in records
        if source_kind(item) == CANDIDATE_SOURCE
    ]
    standalone_records = [
        item
        for item in records
        if source_kind(item)
        not in {CURRENT_SOURCE, HISTORICAL_SOURCE, CANDIDATE_SOURCE}
    ]

    current_names = set(portfolio_names(local_config))
    remote_config_names = set(
        portfolio_names(remote_config)
    )
    remote_state_names = set(
        base.extract_state_portfolios(paper_state)
    )

    state_by_name = base.extract_state_portfolios(
        paper_state
    )
    trades_by_name = base.group_rows_by_profile(
        trade_rows
    )
    signals_by_name = base.group_rows_by_profile(
        signal_rows
    )
    equity_by_name = base.group_rows_by_profile(
        equity_rows
    )
    positions_by_name = base.group_rows_by_profile(
        open_rows
    )

    record_by_name: dict[str, dict[str, Any]] = {}
    duplicate_registry_names: list[str] = []

    for record in current_records + historical_records:
        name = record_profile_name(record)
        if not name:
            continue
        if name in record_by_name:
            duplicate_registry_names.append(name)
        else:
            record_by_name[name] = record

    missing_current_registry_records = sorted(
        current_names - set(record_by_name)
    )
    historical_registry_names = {
        record_profile_name(item)
        for item in historical_records
        if record_profile_name(item)
    }
    candidate_registry_names = {
        record_profile_name(item)
        for item in candidate_records
        if record_profile_name(item)
    }

    for record in candidate_records:
        name = record_profile_name(record)
        if not name:
            continue
        if name in record_by_name:
            duplicate_registry_names.append(name)
        else:
            record_by_name[name] = record

    current_profiles = [
        build_profile(
            record_by_name[name],
            state_by_name,
            trades_by_name,
            equity_by_name,
            positions_by_name,
            signals_by_name,
            current_names=current_names,
            remote_state_names=remote_state_names,
        )
        for name in sorted(current_names)
        if name in record_by_name
    ]

    historical_profiles = [
        build_profile(
            record_by_name[name],
            state_by_name,
            trades_by_name,
            equity_by_name,
            positions_by_name,
            signals_by_name,
            current_names=current_names,
            remote_state_names=remote_state_names,
        )
        for name in sorted(historical_registry_names)
        if name in record_by_name
    ]
    candidate_profiles = [
        build_profile(
            record_by_name[name],
            state_by_name,
            trades_by_name,
            equity_by_name,
            positions_by_name,
            signals_by_name,
            current_names=candidate_registry_names,
            remote_state_names=remote_state_names,
        )
        for name in sorted(candidate_registry_names)
        if name in record_by_name
    ]

    discovered_runtime_names = (
        set(state_by_name)
        | set(trades_by_name)
        | set(signals_by_name)
        | set(equity_by_name)
        | set(positions_by_name)
    )

    registered_runtime_names = (
        current_names | historical_registry_names | candidate_registry_names
    )

    unmapped_runtime = sorted(
        discovered_runtime_names
        - registered_runtime_names
    )
    missing_current_runtime = sorted(
        current_names
        - discovered_runtime_names
    )
    remote_extra_names = (
        remote_config_names - current_names
    )
    remote_historical_missing_registry = sorted(
        remote_extra_names
        - historical_registry_names
        - candidate_registry_names
    )
    historical_ledger_only_names = sorted(
        historical_registry_names
        - remote_state_names
    )

    current_open_accounts = sum(
        1
        for item in current_profiles
        if item["open_position_count"] > 0
    )
    current_open_positions = sum(
        item["open_position_count"]
        for item in current_profiles
    )
    historical_open_accounts = sum(
        1
        for item in historical_profiles
        if item["open_position_count"] > 0
    )
    historical_open_markers = sum(
        item["open_position_count"]
        for item in historical_profiles
    )
    historical_remote_count = sum(
        1
        for item in historical_profiles
        if item["runtime_class"]
        == "HISTORICAL_REMOTE_STATE"
    )
    historical_ledger_only_count = sum(
        1
        for item in historical_profiles
        if item["runtime_class"]
        == "ARCHIVED_LEDGER_ONLY"
    )

    current_activity = Counter(
        item["activity_class"]
        for item in current_profiles
    )
    historical_activity = Counter(
        item["activity_class"]
        for item in historical_profiles
    )
    candidate_activity = Counter(
        item["activity_class"]
        for item in candidate_profiles
    )
    candidate_open_accounts = sum(
        1 for item in candidate_profiles
        if item["open_position_count"] > 0
    )
    candidate_open_positions = sum(
        item["open_position_count"]
        for item in candidate_profiles
    )

    validation = {
        "valid": (
            not duplicate_registry_names
            and not missing_current_registry_records
            and not unmapped_runtime
            and not missing_current_runtime
            and not remote_historical_missing_registry
            and current_names == set(
                portfolio_names(local_config)
            )
            and remote_config_names == remote_state_names
            and len(current_profiles) == 34
            and len(historical_profiles) == 36
            and len(trade_rows) > 0
            and len(signal_rows) > 0
        ),
        "duplicate_registry_profile_names": sorted(
            set(duplicate_registry_names)
        ),
        "missing_current_registry_records": (
            missing_current_registry_records
        ),
        "unmapped_runtime_profiles": unmapped_runtime,
        "missing_current_runtime_profiles": (
            missing_current_runtime
        ),
        "remote_historical_missing_registry": (
            remote_historical_missing_registry
        ),
        "historical_ledger_only_profiles": (
            historical_ledger_only_names
        ),
        "local_current_profile_count": len(
            current_names
        ),
        "remote_config_profile_count": len(
            remote_config_names
        ),
        "remote_state_profile_count": len(
            remote_state_names
        ),
        "historical_registry_profile_count": len(
            historical_registry_names
        ),
        "candidate_registry_profile_count": len(
            candidate_registry_names
        ),
        "candidate_remote_profile_count": len(
            candidate_registry_names & remote_state_names
        ),
        "candidate_support_version": "block5-v1",
        "permanent_trade_rows": len(trade_rows),
        "permanent_signal_rows": len(signal_rows),
        "source_errors": errors,
        "wrapper_environment_loaded": bool(
            wrapper_env
        ),
        "live_is_observation_only": True,
        "historical_reactivation_blocked": all(
            item["reactivation_blocked"]
            for item in historical_profiles
        ),
    }

    protected_live = base.compact_json_state(
        sol_live_state,
        live=True,
    )
    protected_live["status_report"] = (
        base.compact_json_state(
            sol_live_status,
            live=True,
        )
    )
    protected_live["deployment_registry"] = (
        deployments
    )

    snapshot = {
        "schema_version": 3,
        "generated_at": base.utc_now_iso(),
        "repository": str(repo),
        "mode": (
            "REMOTE_LEDGER_EXACT_IDENTITY_"
            "OBSERVATION_ONLY"
        ),
        "safety": {
            "trading_state_changed": False,
            "trading_configuration_changed": False,
            "services_restarted": False,
            "orders_sent": False,
            "paper_restore_called": False,
            "paper_upload_called": False,
            "historical_profiles_reactivated": False,
            "live_parameter_changes_allowed": False,
        },
        "remote_source": {
            "release_tag": storage.RELEASE_TAG,
            "state_asset_name": storage.ASSET_NAME,
            "trade_ledger_asset_name": (
                storage.TRADE_LEDGER_ASSET_NAME
            ),
            "signal_ledger_asset_name": (
                storage.SIGNAL_LEDGER_ASSET_NAME
            ),
            "state_asset_id": state_asset.get("id"),
            "trade_asset_id": trade_asset.get("id"),
            "signal_asset_id": signal_asset.get("id"),
        },
        "summary": {
            "registered_strategy_count": len(records),
            "current_profile_count": len(
                current_profiles
            ),
            "historical_profile_count": len(
                historical_profiles
            ),
            "standalone_strategy_count": len(
                standalone_records
            ),
            "candidate_profile_count": len(
                candidate_profiles
            ),
            "candidate_accounts_with_open_positions": (
                candidate_open_accounts
            ),
            "candidate_open_position_count": (
                candidate_open_positions
            ),
            "candidate_zero_activity_count": (
                candidate_activity["ZERO_ACTIVITY"]
            ),
            "historical_remote_state_count": (
                historical_remote_count
            ),
            "historical_ledger_only_count": (
                historical_ledger_only_count
            ),
            "current_accounts_with_open_positions": (
                current_open_accounts
            ),
            "current_open_position_count": (
                current_open_positions
            ),
            "historical_open_review_count": (
                historical_open_accounts
            ),
            "historical_open_marker_count": (
                historical_open_markers
            ),
            "current_zero_activity_count": (
                current_activity["ZERO_ACTIVITY"]
            ),
            "historical_zero_activity_count": (
                historical_activity["ZERO_ACTIVITY"]
            ),
            "permanent_trade_rows": len(trade_rows),
            "permanent_signal_rows": len(
                signal_rows
            ),
            "unmapped_runtime_profile_count": len(
                unmapped_runtime
            ),
        },
        "current_paper_profiles": current_profiles,
        "evolution_candidate_profiles": candidate_profiles,
        "historical_background_profiles": (
            historical_profiles
        ),
        "standalone_strategies": standalone_records,
        "research_signal": {
            **base.summarize_research(
                research_state
            ),
            "registered_layers": research_layers,
        },
        "sol_spot_adaptive_paper": (
            base.compact_json_state(
                sol_paper_state
            )
        ),
        "live_deployment": protected_live,
        "validation": validation,
    }

    output = repo / args.output
    markdown_output = repo / args.markdown_output

    base.atomic_write_json(
        output,
        snapshot,
    )
    base.atomic_write_text(
        markdown_output,
        render_markdown(snapshot),
    )

    print("=== EVOLUTION RUNTIME SNAPSHOT V3 ===")
    print(
        f"Strategie registrate: {len(records)}"
    )
    print(
        f"Profili paper correnti: {len(current_profiles)}"
    )
    print(
        f"Candidati evolutivi: {len(candidate_profiles)}"
    )
    print(
        "Profili storici BACKGROUND:",
        len(historical_profiles),
    )
    print(
        "Storici nello stato remoto:",
        historical_remote_count,
    )
    print(
        "Storici solo ledger:",
        historical_ledger_only_count,
    )
    print(
        "Account correnti con posizioni:",
        current_open_accounts,
    )
    print(
        "Posizioni correnti aperte:",
        current_open_positions,
    )
    print(
        "Profili storici con marker aperti:",
        historical_open_accounts,
    )
    print(
        "Marker storici aperti:",
        historical_open_markers,
    )
    print(
        f"Trade permanenti: {len(trade_rows)}"
    )
    print(
        f"Segnali permanenti: {len(signal_rows)}"
    )
    print(
        "Profili runtime non mappati:",
        len(unmapped_runtime),
    )
    print(
        f"Validazione: "
        f"{'OK' if validation['valid'] else 'ATTENZIONE'}"
    )
    print(f"JSON: {output}")
    print(f"Markdown: {markdown_output}")
    print("Restore Paper NON eseguito.")
    print("Upload Paper NON eseguito.")
    print(
        "Nessun profilo storico è stato riattivato."
    )
    print(
        "Nessun file operativo è stato modificato."
    )
    print("Nessun servizio è stato riavviato.")
    print("Nessun ordine è stato inviato.")

    return 0 if validation["valid"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
