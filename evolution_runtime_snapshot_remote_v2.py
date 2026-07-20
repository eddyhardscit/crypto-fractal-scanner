#!/usr/bin/env python3
"""Evolution remote runtime snapshot — current and historical profiles.

Reads the permanent Paper ledgers from the GitHub Release entirely in memory,
maps both current paper portfolios and imported historical BACKGROUND profiles,
and writes only Evolution outputs.

No restore/upload action is called. No operational Paper/live file is changed.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

import evolution_runtime_snapshot as base
import evolution_runtime_snapshot_remote as remote


CURRENT_SOURCE = "paper_portfolio"
HISTORICAL_SOURCE = "historical_paper_profile"


def profile_name(record: dict[str, Any]) -> str:
    metadata = record.get("metadata") or {}
    return str(
        metadata.get("legacy_profile_name")
        or metadata.get("source_key")
        or record.get("name")
        or ""
    ).strip()


def source_kind(record: dict[str, Any]) -> str:
    return str((record.get("metadata") or {}).get("source_kind") or "")


def build_profile(
    record: dict[str, Any],
    state_by_name: dict[str, dict[str, Any]],
    trades_by_name: dict[str, list[dict[str, str]]],
    equity_by_name: dict[str, list[dict[str, str]]],
    positions_by_name: dict[str, list[dict[str, str]]],
    signals_by_name: dict[str, list[dict[str, str]]],
) -> dict[str, Any]:
    name = profile_name(record)
    metadata = record.get("metadata") or {}
    state = state_by_name.get(name, {})
    trades = trades_by_name.get(name, [])
    equity_rows = equity_by_name.get(name, [])
    position_rows = positions_by_name.get(name, [])
    signals = signals_by_name.get(name, [])

    normalized_positions: list[dict[str, Any]] = []
    state_positions = state.get("open_positions", [])
    if isinstance(state_positions, list):
        normalized_positions = [
            base.normalize_position(item)
            for item in state_positions
            if isinstance(item, dict)
        ]
    if not normalized_positions:
        normalized_positions = [
            base.normalize_position(item) for item in position_rows
        ]

    latest_eq = base.latest_equity(equity_rows)
    trade_summary = base.extract_trade_summary(trades, state)

    balance = base.safe_float(
        base.first_present(state, ("balance_eur", "cash_eur", "balance"))
    )
    equity = base.safe_float(
        base.first_present(
            state,
            ("equity_eur", "portfolio_equity_eur", "equity"),
        )
    )
    peak_equity = base.safe_float(
        base.first_present(state, ("peak_equity_eur", "peak_equity"))
    )
    drawdown = base.safe_float(
        base.first_present(state, ("max_drawdown_pct", "drawdown_pct"))
    )

    if latest_eq:
        balance = balance if balance is not None else latest_eq.get("balance_eur")
        equity = equity if equity is not None else latest_eq.get("equity_eur")
        peak_equity = (
            peak_equity
            if peak_equity is not None
            else latest_eq.get("peak_equity_eur")
        )
        drawdown = (
            drawdown
            if drawdown is not None
            else latest_eq.get("drawdown_pct")
        )

    last_signal = base.row_timestamp(signals[-1]) if signals else None
    last_activity = (
        trade_summary.get("last_trade_activity")
        or last_signal
        or (latest_eq.get("timestamp") if latest_eq else None)
    )

    historical = source_kind(record) == HISTORICAL_SOURCE
    activity_class = (
        "HISTORICAL_OPEN_REVIEW"
        if historical and normalized_positions
        else "ACTIVE_POSITION"
        if normalized_positions
        else "HAS_HISTORY"
        if (trade_summary.get("closed_trades") or signals)
        else "ZERO_ACTIVITY"
    )

    return {
        "strategy_id": record.get("strategy_id"),
        "family_id": record.get("family_id"),
        "profile_name": name,
        "source_kind": source_kind(record),
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
        "max_drawdown_pct": drawdown,
        "open_position_count": len(normalized_positions),
        "open_positions": normalized_positions,
        "trade_summary": trade_summary,
        "signal_log_rows": len(signals),
        "last_activity": last_activity,
        "activity_class": activity_class,
        "source_presence": {
            "state": name in state_by_name,
            "trade_log": bool(trades),
            "equity_log": bool(equity_rows),
            "open_positions_csv": bool(position_rows),
            "signal_log": bool(signals),
        },
    }


def render_markdown(snapshot: dict[str, Any]) -> str:
    s = snapshot["summary"]
    lines = [
        "# Evolution Runtime Snapshot V2",
        "",
        f"Generated: `{snapshot['generated_at']}`",
        "",
        "> Observation only. Current and historical Paper profiles are mapped.",
        "",
        "## Summary",
        "",
        f"- Registered strategies: **{s['registered_strategy_count']}**",
        f"- Current paper profiles: **{s['current_profile_count']}**",
        f"- Historical BACKGROUND profiles: **{s['historical_profile_count']}**",
        f"- Standalone strategies: **{s['standalone_strategy_count']}**",
        f"- Current profiles with open positions: **{s['current_profiles_with_open_positions']}**",
        f"- Historical profiles requiring open-position review: **{s['historical_open_review_count']}**",
        f"- Total current open positions: **{s['current_open_position_count']}**",
        f"- Total historical open markers: **{s['historical_open_marker_count']}**",
        f"- Permanent trades: **{s['permanent_trade_rows']}**",
        f"- Permanent signals: **{s['permanent_signal_rows']}**",
        f"- Unmapped runtime profiles: **{s['unmapped_runtime_profile_count']}**",
        f"- Validation: **{'OK' if snapshot['validation']['valid'] else 'ATTENTION'}**",
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
        "## Historical BACKGROUND profiles",
        "",
        "| Profile | Family | Closed | Open markers | Review | Last activity |",
        "|---|---|---:|---:|:---:|---|",
    ]
    for item in snapshot["historical_background_profiles"]:
        lines.append(
            f"| {item['profile_name']} | {item.get('family_id')} | "
            f"{item['trade_summary'].get('closed_trades')} | "
            f"{item.get('open_position_count')} | "
            f"{'yes' if item.get('requires_open_position_review') else 'no'} | "
            f"{item.get('last_activity')} |"
        )

    lines += [
        "",
        "## Validation",
        "",
        "```json",
        json.dumps(
            snapshot["validation"],
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
    import paper_trading_storage as storage

    client = storage.session()
    response = client.get(
        storage.api_url(f"/releases/tags/{storage.RELEASE_TAG}"),
        timeout=30,
    )
    if response.status_code >= 400:
        raise RuntimeError(
            f"Cannot read Paper release: HTTP {response.status_code}"
        )
    release = response.json()

    state_asset = remote.release_asset(release, storage.ASSET_NAME)
    trade_asset = remote.release_asset(
        release,
        storage.TRADE_LEDGER_ASSET_NAME,
    )
    signal_asset = remote.release_asset(
        release,
        storage.SIGNAL_LEDGER_ASSET_NAME,
    )

    state_zip = storage.download_asset_bytes(client, state_asset)
    trade_rows = remote.parse_csv_bytes(
        storage.download_asset_bytes(client, trade_asset)
    )
    signal_rows = remote.parse_csv_bytes(
        storage.download_asset_bytes(client, signal_asset)
    )

    errors: dict[str, str] = {}

    paper_state, error = remote.zip_json(
        state_zip,
        "paper_trading_state.json",
    )
    if error:
        errors["paper_state"] = error

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

    registry_doc, error = base.read_json(
        repo / "data/evolution/strategy_registry.json"
    )
    if error:
        raise RuntimeError(f"Cannot read strategy registry: {error}")

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
        item for item in records if source_kind(item) == CURRENT_SOURCE
    ]
    historical_records = [
        item for item in records if source_kind(item) == HISTORICAL_SOURCE
    ]
    standalone_records = [
        item for item in records
        if source_kind(item) not in {CURRENT_SOURCE, HISTORICAL_SOURCE}
    ]

    state_by_name = base.extract_state_portfolios(paper_state)
    trades_by_name = base.group_rows_by_profile(trade_rows)
    signals_by_name = base.group_rows_by_profile(signal_rows)
    equity_by_name = base.group_rows_by_profile(equity_rows)
    positions_by_name = base.group_rows_by_profile(open_rows)

    current_profiles = [
        build_profile(
            item,
            state_by_name,
            trades_by_name,
            equity_by_name,
            positions_by_name,
            signals_by_name,
        )
        for item in current_records
    ]
    historical_profiles = [
        build_profile(
            item,
            state_by_name,
            trades_by_name,
            equity_by_name,
            positions_by_name,
            signals_by_name,
        )
        for item in historical_records
    ]

    registered_runtime_names = {
        profile_name(item)
        for item in current_records + historical_records
        if profile_name(item)
    }
    discovered_runtime_names = (
        set(state_by_name)
        | set(trades_by_name)
        | set(signals_by_name)
        | set(equity_by_name)
        | set(positions_by_name)
    )

    unmapped_runtime = sorted(
        name
        for name in discovered_runtime_names
        if name and name not in registered_runtime_names
    )
    missing_current = sorted(
        name
        for name in (profile_name(item) for item in current_records)
        if name and name not in discovered_runtime_names
    )
    missing_historical = sorted(
        name
        for name in (profile_name(item) for item in historical_records)
        if name and name not in discovered_runtime_names
    )

    current_open_accounts = sum(
        1 for item in current_profiles if item["open_position_count"] > 0
    )
    current_open_positions = sum(
        item["open_position_count"] for item in current_profiles
    )
    historical_open_accounts = sum(
        1
        for item in historical_profiles
        if item["open_position_count"] > 0
    )
    historical_open_markers = sum(
        item["open_position_count"] for item in historical_profiles
    )

    current_activity = Counter(
        item["activity_class"] for item in current_profiles
    )
    historical_activity = Counter(
        item["activity_class"] for item in historical_profiles
    )

    validation = {
        "valid": (
            not unmapped_runtime
            and not missing_current
            and not missing_historical
            and len(current_profiles) == 34
            and len(historical_profiles) == 36
            and len(trade_rows) > 0
            and len(signal_rows) > 0
        ),
        "unmapped_runtime_profiles": unmapped_runtime,
        "missing_current_profiles": missing_current,
        "missing_historical_profiles": missing_historical,
        "current_profile_count": len(current_profiles),
        "historical_profile_count": len(historical_profiles),
        "permanent_trade_rows": len(trade_rows),
        "permanent_signal_rows": len(signal_rows),
        "source_errors": errors,
        "live_is_observation_only": True,
        "historical_reactivation_blocked": all(
            item["reactivation_blocked"] for item in historical_profiles
        ),
    }

    protected_live = base.compact_json_state(sol_live_state, live=True)
    protected_live["status_report"] = base.compact_json_state(
        sol_live_status,
        live=True,
    )
    protected_live["deployment_registry"] = deployments

    snapshot = {
        "schema_version": 2,
        "generated_at": base.utc_now_iso(),
        "repository": str(repo),
        "mode": "REMOTE_LEDGER_FULL_REGISTRY_OBSERVATION_ONLY",
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
            "trade_ledger_asset_name": storage.TRADE_LEDGER_ASSET_NAME,
            "signal_ledger_asset_name": storage.SIGNAL_LEDGER_ASSET_NAME,
            "state_asset_id": state_asset.get("id"),
            "trade_asset_id": trade_asset.get("id"),
            "signal_asset_id": signal_asset.get("id"),
        },
        "summary": {
            "registered_strategy_count": len(records),
            "current_profile_count": len(current_profiles),
            "historical_profile_count": len(historical_profiles),
            "standalone_strategy_count": len(standalone_records),
            "current_profiles_with_open_positions": current_open_accounts,
            "historical_open_review_count": historical_open_accounts,
            "current_open_position_count": current_open_positions,
            "historical_open_marker_count": historical_open_markers,
            "current_zero_activity_count": current_activity["ZERO_ACTIVITY"],
            "historical_zero_activity_count": historical_activity[
                "ZERO_ACTIVITY"
            ],
            "permanent_trade_rows": len(trade_rows),
            "permanent_signal_rows": len(signal_rows),
            "unmapped_runtime_profile_count": len(unmapped_runtime),
        },
        "current_paper_profiles": current_profiles,
        "historical_background_profiles": historical_profiles,
        "standalone_strategies": standalone_records,
        "research_signal": {
            **base.summarize_research(research_state),
            "registered_layers": research_layers,
        },
        "sol_spot_adaptive_paper": base.compact_json_state(
            sol_paper_state
        ),
        "live_deployment": protected_live,
        "validation": validation,
    }

    output = repo / args.output
    markdown_output = repo / args.markdown_output
    base.atomic_write_json(output, snapshot)
    base.atomic_write_text(
        markdown_output,
        render_markdown(snapshot),
    )

    print("=== EVOLUTION FULL RUNTIME SNAPSHOT V2 ===")
    print(f"Strategie registrate: {len(records)}")
    print(f"Profili paper correnti: {len(current_profiles)}")
    print(f"Profili storici BACKGROUND: {len(historical_profiles)}")
    print(f"Strategie standalone: {len(standalone_records)}")
    print(f"Account correnti con posizioni: {current_open_accounts}")
    print(
        "Profili storici con marker aperti:",
        historical_open_accounts,
    )
    print(f"Posizioni correnti aperte: {current_open_positions}")
    print(f"Marker storici aperti: {historical_open_markers}")
    print(f"Trade permanenti: {len(trade_rows)}")
    print(f"Segnali permanenti: {len(signal_rows)}")
    print(f"Profili runtime non mappati: {len(unmapped_runtime)}")
    print(f"Validazione: {'OK' if validation['valid'] else 'ATTENZIONE'}")
    print(f"JSON: {output}")
    print(f"Markdown: {markdown_output}")
    print("Restore Paper NON eseguito.")
    print("Upload Paper NON eseguito.")
    print("Nessun profilo storico è stato riattivato.")
    print("Nessun file operativo è stato modificato.")
    print("Nessun servizio è stato riavviato.")
    print("Nessun ordine è stato inviato.")
    return 0 if validation["valid"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
