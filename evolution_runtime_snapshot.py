#!/usr/bin/env python3
"""Create a read-only runtime snapshot for the Evolution Framework.

Reads existing operational files but never modifies them:
- reports/paper_trading_state.json
- reports/paper_trading_trade_log.csv
- reports/paper_trading_signal_log.csv
- reports/paper_trading_equity.csv
- reports/paper_trading_open_positions.csv
- reports/paper_trading_config_snapshot.json
- reports/research_all_signals_state.json
- reports/sol_spot_adaptive_state.json
- reports/sol_spot_live_state.json
- reports/sol_spot_live_status.json
- data/evolution/strategy_registry.json
- data/evolution/research_layers.json
- data/evolution/deployments.json

Writes only:
- data/evolution/runtime_snapshot.json
- reports/evolution_runtime_snapshot.md

The script imports no trading module, sends no order and restarts no service.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import os
import tempfile
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable


SCHEMA_VERSION = 1

PATHS = {
    "registry": "data/evolution/strategy_registry.json",
    "research_layers": "data/evolution/research_layers.json",
    "deployments": "data/evolution/deployments.json",
    "paper_state": "reports/paper_trading_state.json",
    "paper_trade_log": "reports/paper_trading_trade_log.csv",
    "paper_signal_log": "reports/paper_trading_signal_log.csv",
    "paper_equity_log": "reports/paper_trading_equity.csv",
    "paper_open_positions": "reports/paper_trading_open_positions.csv",
    "paper_config_snapshot": "reports/paper_trading_config_snapshot.json",
    "research_state": "reports/research_all_signals_state.json",
    "sol_paper_state": "reports/sol_spot_adaptive_state.json",
    "sol_live_state": "reports/sol_spot_live_state.json",
    "sol_live_status": "reports/sol_spot_live_status.json",
}


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def safe_float(value: Any) -> float | None:
    if value is None or value == "":
        return None
    try:
        number = float(str(value).replace(",", "."))
    except (TypeError, ValueError):
        return None
    return number if math.isfinite(number) else None


def safe_int(value: Any) -> int | None:
    number = safe_float(value)
    return int(number) if number is not None else None


def safe_bool(value: Any) -> bool | None:
    if isinstance(value, bool):
        return value
    if value is None or value == "":
        return None
    text = str(value).strip().lower()
    if text in {"1", "true", "yes", "y", "on"}:
        return True
    if text in {"0", "false", "no", "n", "off"}:
        return False
    return None


def read_json(path: Path) -> tuple[Any, str | None]:
    if not path.exists():
        return None, "missing"
    try:
        return json.loads(path.read_text(encoding="utf-8")), None
    except json.JSONDecodeError as exc:
        return None, f"invalid_json:{exc}"
    except OSError as exc:
        return None, f"read_error:{exc}"


def read_csv(path: Path) -> tuple[list[dict[str, str]], str | None]:
    if not path.exists():
        return [], "missing"
    try:
        with path.open("r", encoding="utf-8-sig", newline="") as handle:
            return list(csv.DictReader(handle)), None
    except (OSError, csv.Error) as exc:
        return [], f"read_error:{exc}"


def atomic_write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temp_name = tempfile.mkstemp(
        prefix=f".{path.name}.",
        suffix=".tmp",
        dir=str(path.parent),
        text=True,
    )
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            json.dump(value, handle, indent=2, ensure_ascii=False, sort_keys=True)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temp_name, path)
    except Exception:
        try:
            os.unlink(temp_name)
        except OSError:
            pass
        raise


def atomic_write_text(path: Path, value: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temp_name = tempfile.mkstemp(
        prefix=f".{path.name}.",
        suffix=".tmp",
        dir=str(path.parent),
        text=True,
    )
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            handle.write(value)
            if not value.endswith("\n"):
                handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temp_name, path)
    except Exception:
        try:
            os.unlink(temp_name)
        except OSError:
            pass
        raise


def first_present(mapping: dict[str, Any], names: Iterable[str]) -> Any:
    for name in names:
        if name in mapping and mapping[name] not in (None, ""):
            return mapping[name]
    return None


def row_profile_name(row: dict[str, Any]) -> str:
    value = first_present(
        row,
        (
            "portfolio",
            "portfolio_name",
            "account",
            "account_name",
            "profile",
            "name",
        ),
    )
    return str(value or "").strip()


def row_timestamp(row: dict[str, Any]) -> str | None:
    value = first_present(
        row,
        (
            "closed_at",
            "exit_time",
            "timestamp",
            "generated_utc",
            "updated_utc",
            "opened_at",
            "entry_time",
            "time",
            "date",
        ),
    )
    return str(value).strip() if value not in (None, "") else None


def registry_records(registry_doc: Any) -> list[dict[str, Any]]:
    if not isinstance(registry_doc, dict):
        return []
    strategies = registry_doc.get("strategies", {})
    if isinstance(strategies, dict):
        return [item for item in strategies.values() if isinstance(item, dict)]
    if isinstance(strategies, list):
        return [item for item in strategies if isinstance(item, dict)]
    return []


def build_registry_indexes(
    records: list[dict[str, Any]],
) -> tuple[dict[str, dict[str, Any]], dict[str, dict[str, Any]]]:
    by_profile: dict[str, dict[str, Any]] = {}
    by_id: dict[str, dict[str, Any]] = {}
    for item in records:
        strategy_id = str(item.get("strategy_id", "")).strip()
        if strategy_id:
            by_id[strategy_id] = item
        metadata = item.get("metadata") or {}
        profile = str(
            metadata.get("legacy_profile_name")
            or metadata.get("source_key")
            or item.get("name")
            or ""
        ).strip()
        if profile:
            by_profile[profile] = item
    return by_profile, by_id


def extract_state_portfolios(state_doc: Any) -> dict[str, dict[str, Any]]:
    """Handle both dict-by-name and list portfolio state formats."""
    if not isinstance(state_doc, dict):
        return {}
    raw = state_doc.get("portfolios", {})
    result: dict[str, dict[str, Any]] = {}

    if isinstance(raw, dict):
        for key, value in raw.items():
            if isinstance(value, dict):
                name = str(value.get("name") or key).strip()
                if name:
                    result[name] = value
    elif isinstance(raw, list):
        for value in raw:
            if isinstance(value, dict):
                name = str(value.get("name") or value.get("portfolio") or "").strip()
                if name:
                    result[name] = value
    return result


def group_rows_by_profile(rows: list[dict[str, str]]) -> dict[str, list[dict[str, str]]]:
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        name = row_profile_name(row)
        if name:
            grouped[name].append(row)
    return grouped


def normalize_position(row: dict[str, Any]) -> dict[str, Any]:
    return {
        "trade_id": first_present(row, ("trade_id", "id")),
        "asset": first_present(row, ("asset", "symbol", "ticker")),
        "side": first_present(row, ("side", "direction")),
        "strategy": first_present(row, ("strategy",)),
        "entry_price": safe_float(first_present(row, ("entry_price", "open_price"))),
        "mark_price": safe_float(first_present(row, ("mark_price", "current_price"))),
        "quantity": safe_float(first_present(row, ("quantity", "qty", "size"))),
        "opened_at": first_present(row, ("opened_at", "entry_time", "created_at")),
        "raw": row,
    }


def latest_equity(rows: list[dict[str, str]]) -> dict[str, Any] | None:
    if not rows:
        return None
    row = rows[-1]
    return {
        "timestamp": row_timestamp(row),
        "balance_eur": safe_float(
            first_present(row, ("balance_eur", "balance", "cash_eur"))
        ),
        "equity_eur": safe_float(
            first_present(row, ("equity_eur", "equity", "portfolio_equity_eur"))
        ),
        "peak_equity_eur": safe_float(
            first_present(row, ("peak_equity_eur", "peak_equity"))
        ),
        "drawdown_pct": safe_float(
            first_present(row, ("drawdown_pct", "max_drawdown_pct"))
        ),
        "raw": row,
    }


def extract_trade_summary(
    trade_rows: list[dict[str, str]],
    state: dict[str, Any] | None,
) -> dict[str, Any]:
    state = state or {}
    closed_count_state = safe_int(state.get("closed_trades"))
    winning_state = safe_int(state.get("winning_trades"))
    losing_state = safe_int(state.get("losing_trades"))

    pnl_values: list[float] = []
    last_activity = None
    for row in trade_rows:
        pnl = safe_float(
            first_present(
                row,
                (
                    "realized_pnl_eur",
                    "pnl_eur",
                    "profit_eur",
                    "net_pnl_eur",
                    "realized_pnl",
                ),
            )
        )
        if pnl is not None:
            pnl_values.append(pnl)
        timestamp = row_timestamp(row)
        if timestamp:
            last_activity = timestamp

    wins_from_rows = sum(1 for value in pnl_values if value > 0)
    losses_from_rows = sum(1 for value in pnl_values if value < 0)

    return {
        "closed_trades": (
            closed_count_state
            if closed_count_state is not None
            else len(trade_rows)
        ),
        "winning_trades": (
            winning_state if winning_state is not None else wins_from_rows
        ),
        "losing_trades": (
            losing_state if losing_state is not None else losses_from_rows
        ),
        "realized_pnl_eur_from_rows": (
            round(sum(pnl_values), 10) if pnl_values else None
        ),
        "last_trade_activity": last_activity,
        "trade_log_rows": len(trade_rows),
    }


def build_paper_accounts(
    records: list[dict[str, Any]],
    state_doc: Any,
    trade_rows: list[dict[str, str]],
    equity_rows: list[dict[str, str]],
    open_position_rows: list[dict[str, str]],
    signal_rows: list[dict[str, str]],
) -> tuple[list[dict[str, Any]], list[str]]:
    state_by_name = extract_state_portfolios(state_doc)
    trades_by_name = group_rows_by_profile(trade_rows)
    equity_by_name = group_rows_by_profile(equity_rows)
    positions_by_name = group_rows_by_profile(open_position_rows)
    signals_by_name = group_rows_by_profile(signal_rows)

    accounts: list[dict[str, Any]] = []
    mapped_profiles: set[str] = set()

    for record in records:
        metadata = record.get("metadata") or {}
        if metadata.get("source_kind") != "paper_portfolio":
            continue
        profile = str(metadata.get("legacy_profile_name") or record.get("name") or "").strip()
        if not profile:
            continue
        mapped_profiles.add(profile)

        state = state_by_name.get(profile, {})
        trade_group = trades_by_name.get(profile, [])
        equity_group = equity_by_name.get(profile, [])
        position_group = positions_by_name.get(profile, [])
        signal_group = signals_by_name.get(profile, [])

        state_positions = state.get("open_positions", [])
        normalized_positions: list[dict[str, Any]] = []
        if isinstance(state_positions, list):
            normalized_positions.extend(
                normalize_position(item)
                for item in state_positions
                if isinstance(item, dict)
            )
        if not normalized_positions:
            normalized_positions.extend(normalize_position(item) for item in position_group)

        latest_signal = signal_group[-1] if signal_group else None
        latest_eq = latest_equity(equity_group)

        balance = safe_float(
            first_present(state, ("balance_eur", "cash_eur", "balance"))
        )
        equity = safe_float(
            first_present(state, ("peak_equity_eur",))
        )
        current_equity = safe_float(
            first_present(state, ("equity_eur", "portfolio_equity_eur", "equity"))
        )
        if current_equity is None and latest_eq:
            current_equity = latest_eq.get("equity_eur")
        if balance is None and latest_eq:
            balance = latest_eq.get("balance_eur")

        trade_summary = extract_trade_summary(trade_group, state)
        last_signal_activity = row_timestamp(latest_signal) if latest_signal else None
        last_activity = (
            trade_summary.get("last_trade_activity")
            or last_signal_activity
            or (latest_eq.get("timestamp") if latest_eq else None)
        )

        accounts.append(
            {
                "strategy_id": record.get("strategy_id"),
                "family_id": record.get("family_id"),
                "profile_name": profile,
                "strategy_engine": metadata.get("strategy_engine"),
                "role": metadata.get("role"),
                "lifecycle_status": record.get("status"),
                "enabled": metadata.get("enabled"),
                "balance_eur": balance,
                "equity_eur": current_equity,
                "peak_equity_eur": safe_float(
                    first_present(state, ("peak_equity_eur", "peak_equity"))
                ) or (latest_eq.get("peak_equity_eur") if latest_eq else None),
                "max_drawdown_pct": safe_float(
                    first_present(state, ("max_drawdown_pct", "drawdown_pct"))
                ) or (latest_eq.get("drawdown_pct") if latest_eq else None),
                "open_position_count": len(normalized_positions),
                "open_positions": normalized_positions,
                "trade_summary": trade_summary,
                "seen_signal_count": (
                    len(state.get("seen_signal_ids", []))
                    if isinstance(state.get("seen_signal_ids"), list)
                    else None
                ),
                "signal_log_rows": len(signal_group),
                "last_activity": last_activity,
                "activity_class": (
                    "ACTIVE_POSITION"
                    if normalized_positions
                    else "HAS_HISTORY"
                    if trade_summary["closed_trades"] or signal_group
                    else "ZERO_ACTIVITY"
                ),
                "source_presence": {
                    "state": profile in state_by_name,
                    "trade_log": bool(trade_group),
                    "equity_log": bool(equity_group),
                    "open_positions_csv": bool(position_group),
                    "signal_log": bool(signal_group),
                },
            }
        )

    discovered_profiles = (
        set(state_by_name)
        | set(trades_by_name)
        | set(equity_by_name)
        | set(positions_by_name)
        | set(signals_by_name)
    )
    unmapped = sorted(name for name in discovered_profiles if name not in mapped_profiles)
    return accounts, unmapped


def compact_json_state(value: Any, *, live: bool = False) -> dict[str, Any]:
    if not isinstance(value, dict):
        return {"available": False}
    allowed = {
        "created_utc",
        "updated_utc",
        "generated_utc",
        "schema_version",
        "strategy_name",
        "strategy",
        "symbol",
        "mode",
        "plan",
        "kill_switch_active",
        "live_orders_enabled",
        "real_orders_enabled",
        "cash_eur",
        "cash_usdt",
        "equity_eur",
        "managed_equity_usdt",
        "realized_pnl_eur",
        "realized_pnl_usdt",
        "return_pct",
        "max_drawdown_pct",
        "sol_qty",
        "tracked_sol_units",
        "position",
        "trades",
        "last_action",
        "last_reason",
        "last_order",
        "last_reconciled_order",
        "last_executed_candle_utc",
        "last_realized_pnl_utc",
        "cooldown_until_utc",
        "test_result",
        "real_result",
        "account",
        "risk",
    }
    result = {key: value.get(key) for key in allowed if key in value}
    result["available"] = True
    if live:
        result["protected_observation_only"] = True
    return result


def summarize_research(value: Any) -> dict[str, Any]:
    if not isinstance(value, dict):
        return {"available": False}
    open_positions = value.get("open_positions")
    if isinstance(open_positions, dict):
        open_count = len(open_positions)
    elif isinstance(open_positions, list):
        open_count = len(open_positions)
    else:
        open_count = 0
    seen = value.get("seen_research_ids")
    return {
        "available": True,
        "schema_version": value.get("schema_version"),
        "created_utc": value.get("created_utc"),
        "updated_utc": value.get("updated_utc"),
        "open_position_count": open_count,
        "seen_research_id_count": len(seen) if isinstance(seen, list) else None,
        "legacy_open_positions_discarded": value.get(
            "legacy_open_positions_discarded"
        ),
    }


def render_markdown(snapshot: dict[str, Any]) -> str:
    summary = snapshot["summary"]
    lines = [
        "# Evolution Runtime Snapshot",
        "",
        f"Generated: `{snapshot['generated_at']}`",
        "",
        "> Observation only. No trading state, configuration or service was modified.",
        "",
        "## Summary",
        "",
        f"- Registered strategies: **{summary['registered_strategy_count']}**",
        f"- Paper accounts mapped: **{summary['paper_account_count']}**",
        f"- Accounts with open positions: **{summary['accounts_with_open_positions']}**",
        f"- Accounts with history but no open position: **{summary['accounts_with_history']}**",
        f"- Accounts with zero activity: **{summary['zero_activity_accounts']}**",
        f"- Total open paper positions: **{summary['total_open_paper_positions']}**",
        f"- Total closed paper trades: **{summary['total_closed_paper_trades']}**",
        f"- Unmapped runtime profiles: **{summary['unmapped_runtime_profile_count']}**",
        "",
        "## Paper accounts",
        "",
        "| Profile | Role | Status | Equity | Closed | Open | Activity |",
        "|---|---|---|---:|---:|---:|---|",
    ]
    for account in snapshot["paper_accounts"]:
        lines.append(
            f"| {account['profile_name']} | {account.get('role')} | "
            f"{account.get('lifecycle_status')} | "
            f"{account.get('equity_eur')} | "
            f"{account['trade_summary'].get('closed_trades')} | "
            f"{account.get('open_position_count')} | "
            f"{account.get('activity_class')} |"
        )

    lines += [
        "",
        "## Research Signal",
        "",
        f"```json\n{json.dumps(snapshot['research_signal'], indent=2, ensure_ascii=False, sort_keys=True)}\n```",
        "",
        "## SOL Spot Adaptive paper",
        "",
        f"```json\n{json.dumps(snapshot['sol_spot_adaptive_paper'], indent=2, ensure_ascii=False, sort_keys=True)}\n```",
        "",
        "## Live deployment — protected observation",
        "",
        f"```json\n{json.dumps(snapshot['live_deployment'], indent=2, ensure_ascii=False, sort_keys=True)}\n```",
        "",
        "## Validation",
        "",
        f"```json\n{json.dumps(snapshot['validation'], indent=2, ensure_ascii=False, sort_keys=True)}\n```",
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

    resolved = {key: repo / relative for key, relative in PATHS.items()}
    errors: dict[str, str] = {}

    registry_doc, error = read_json(resolved["registry"])
    if error:
        raise SystemExit(f"Cannot load strategy registry: {error}")
    records = registry_records(registry_doc)
    by_profile, _ = build_registry_indexes(records)

    paper_state, error = read_json(resolved["paper_state"])
    if error:
        errors["paper_state"] = error

    trade_rows, error = read_csv(resolved["paper_trade_log"])
    if error:
        errors["paper_trade_log"] = error

    signal_rows, error = read_csv(resolved["paper_signal_log"])
    if error:
        errors["paper_signal_log"] = error

    equity_rows, error = read_csv(resolved["paper_equity_log"])
    if error:
        errors["paper_equity_log"] = error

    open_position_rows, error = read_csv(resolved["paper_open_positions"])
    if error:
        errors["paper_open_positions"] = error

    config_snapshot, error = read_json(resolved["paper_config_snapshot"])
    if error:
        errors["paper_config_snapshot"] = error

    research_state, error = read_json(resolved["research_state"])
    if error:
        errors["research_state"] = error

    sol_paper_state, error = read_json(resolved["sol_paper_state"])
    if error:
        errors["sol_paper_state"] = error

    sol_live_state, error = read_json(resolved["sol_live_state"])
    if error:
        errors["sol_live_state"] = error

    sol_live_status, error = read_json(resolved["sol_live_status"])
    if error:
        errors["sol_live_status"] = error

    research_layers, error = read_json(resolved["research_layers"])
    if error:
        errors["research_layers"] = error

    deployments, error = read_json(resolved["deployments"])
    if error:
        errors["deployments"] = error

    accounts, unmapped_profiles = build_paper_accounts(
        records,
        paper_state,
        trade_rows,
        equity_rows,
        open_position_rows,
        signal_rows,
    )

    activity_counts = Counter(item["activity_class"] for item in accounts)
    total_open = sum(item["open_position_count"] for item in accounts)
    total_closed = sum(
        item["trade_summary"].get("closed_trades") or 0 for item in accounts
    )

    registry_profile_names = {
        str((item.get("metadata") or {}).get("legacy_profile_name") or "").strip()
        for item in records
        if (item.get("metadata") or {}).get("source_kind") == "paper_portfolio"
    }
    missing_registry_profiles = sorted(
        name for name in registry_profile_names if name and name not in by_profile
    )

    protected_live = compact_json_state(sol_live_state, live=True)
    protected_live["status_report"] = compact_json_state(sol_live_status, live=True)
    protected_live["deployment_registry"] = deployments

    validation = {
        "valid": not missing_registry_profiles,
        "registered_paper_profiles": len(registry_profile_names),
        "mapped_paper_accounts": len(accounts),
        "missing_registry_profiles": missing_registry_profiles,
        "unmapped_runtime_profiles": unmapped_profiles,
        "source_errors": errors,
        "live_is_observation_only": True,
    }

    snapshot = {
        "schema_version": SCHEMA_VERSION,
        "generated_at": utc_now_iso(),
        "repository": str(repo),
        "mode": "OBSERVATION_ONLY",
        "safety": {
            "trading_state_changed": False,
            "trading_configuration_changed": False,
            "services_restarted": False,
            "orders_sent": False,
            "live_parameter_changes_allowed": False,
        },
        "summary": {
            "registered_strategy_count": len(records),
            "paper_account_count": len(accounts),
            "accounts_with_open_positions": activity_counts["ACTIVE_POSITION"],
            "accounts_with_history": activity_counts["HAS_HISTORY"],
            "zero_activity_accounts": activity_counts["ZERO_ACTIVITY"],
            "total_open_paper_positions": total_open,
            "total_closed_paper_trades": total_closed,
            "unmapped_runtime_profile_count": len(unmapped_profiles),
        },
        "paper_accounts": accounts,
        "paper_runtime": {
            "state_available": isinstance(paper_state, dict),
            "state_schema_version": (
                paper_state.get("schema_version")
                if isinstance(paper_state, dict)
                else None
            ),
            "state_created_utc": (
                paper_state.get("created_utc")
                if isinstance(paper_state, dict)
                else None
            ),
            "state_updated_utc": (
                paper_state.get("updated_utc")
                if isinstance(paper_state, dict)
                else None
            ),
            "trade_log_rows": len(trade_rows),
            "signal_log_rows": len(signal_rows),
            "equity_log_rows": len(equity_rows),
            "open_positions_csv_rows": len(open_position_rows),
            "config_snapshot_available": isinstance(config_snapshot, dict),
        },
        "research_signal": {
            **summarize_research(research_state),
            "registered_layers": research_layers,
        },
        "sol_spot_adaptive_paper": compact_json_state(sol_paper_state),
        "live_deployment": protected_live,
        "validation": validation,
    }

    output = repo / args.output
    markdown_output = repo / args.markdown_output
    atomic_write_json(output, snapshot)
    atomic_write_text(markdown_output, render_markdown(snapshot))

    print("=== EVOLUTION RUNTIME SNAPSHOT ===")
    print(f"Strategie registrate: {len(records)}")
    print(f"Account paper mappati: {len(accounts)}")
    print(f"Con posizioni aperte: {activity_counts['ACTIVE_POSITION']}")
    print(f"Con storico: {activity_counts['HAS_HISTORY']}")
    print(f"A zero attività: {activity_counts['ZERO_ACTIVITY']}")
    print(f"Posizioni paper aperte: {total_open}")
    print(f"Trade paper chiusi: {total_closed}")
    print(f"Profili runtime non mappati: {len(unmapped_profiles)}")
    print(f"Errori/assenze sorgenti: {len(errors)}")
    print(f"Validazione: {'OK' if validation['valid'] else 'ATTENZIONE'}")
    print(f"JSON: {output}")
    print(f"Markdown: {markdown_output}")
    print("Nessun file operativo è stato modificato.")
    print("Nessun servizio è stato riavviato.")
    print("Nessun ordine è stato inviato.")
    return 0 if validation["valid"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
