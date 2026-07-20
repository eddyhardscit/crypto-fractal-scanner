#!/usr/bin/env python3
"""Build the Evolution runtime snapshot from remote permanent Paper ledgers.

This script is read-only with respect to trading.

It:
- loads the same environment used by crypto-paper-main.service without printing it;
- uses paper_trading_storage.session() and api_url();
- downloads the GitHub Release assets for RELEASE_TAG;
- reads the state ZIP entirely in memory;
- reads permanent trade/signal CSV ledgers entirely in memory;
- maps runtime data to the 35 registered strategy records;
- writes only Evolution outputs.

It NEVER calls paper_trading_storage.restore() or upload().
It NEVER writes into reports/ operational CSV/JSON files.
It NEVER restarts a service or sends an order.
"""

from __future__ import annotations

import argparse
import csv
import io
import json
import os
import re
import subprocess
import sys
import zipfile
from collections import Counter
from pathlib import Path
from typing import Any

# The previously installed snapshot module contains the normalized mapping logic.
import evolution_runtime_snapshot as base


def load_env_file(path: Path) -> None:
    """Load KEY=VALUE pairs without printing secrets or overwriting existing env."""
    if not path.exists() or not path.is_file():
        return
    try:
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    except OSError:
        return

    for raw in lines:
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        if line.startswith("export "):
            line = line[7:].lstrip()
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip()
        if not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", key):
            continue
        if (
            len(value) >= 2
            and value[0] == value[-1]
            and value[0] in {"'", '"'}
        ):
            value = value[1:-1]
        os.environ.setdefault(key, value)


def load_service_environment(repo: Path) -> list[str]:
    """Load likely repo and systemd EnvironmentFile values, returning paths only."""
    loaded: list[str] = []

    candidates = [
        repo / ".env",
        repo / ".env.local",
    ]

    try:
        process = subprocess.run(
            [
                "systemctl",
                "show",
                "crypto-paper-main.service",
                "--no-pager",
                "-p",
                "EnvironmentFiles",
                "--value",
            ],
            capture_output=True,
            text=True,
            timeout=10,
            check=False,
        )
        # Extract absolute file paths only. Do not expose or log file contents.
        for match in re.findall(r"(/[^\s;()]+)", process.stdout):
            candidates.append(Path(match))
    except Exception:
        pass

    seen: set[str] = set()
    for path in candidates:
        key = str(path)
        if key in seen:
            continue
        seen.add(key)
        if path.exists() and path.is_file():
            load_env_file(path)
            loaded.append(key)
    return loaded


def release_asset(release: dict[str, Any], name: str) -> dict[str, Any]:
    assets = release.get("assets", [])
    if not isinstance(assets, list):
        raise RuntimeError("GitHub release assets is not a list")
    for asset in assets:
        if isinstance(asset, dict) and str(asset.get("name")) == name:
            return asset
    available = [
        str(asset.get("name"))
        for asset in assets
        if isinstance(asset, dict)
    ]
    raise RuntimeError(
        f"Remote asset not found: {name}. Available: {available}"
    )


def parse_csv_bytes(payload: bytes) -> list[dict[str, str]]:
    text = payload.decode("utf-8-sig", errors="replace")
    return list(csv.DictReader(io.StringIO(text)))


def parse_json_bytes(payload: bytes) -> Any:
    return json.loads(payload.decode("utf-8-sig", errors="replace"))


def zip_member_bytes(payload: bytes, target_name: str) -> bytes | None:
    """Find either reports/<name> or a member ending in /<name>."""
    with zipfile.ZipFile(io.BytesIO(payload), "r") as archive:
        exact_candidates = {
            target_name,
            f"reports/{target_name}",
        }
        for info in archive.infolist():
            normalized = info.filename.replace("\\", "/").lstrip("/")
            if normalized in exact_candidates or normalized.endswith(f"/{target_name}"):
                return archive.read(info)
    return None


def zip_json(payload: bytes, target_name: str) -> tuple[Any, str | None]:
    raw = zip_member_bytes(payload, target_name)
    if raw is None:
        return None, "missing_in_remote_zip"
    try:
        return parse_json_bytes(raw), None
    except Exception as exc:
        return None, f"invalid_remote_json:{exc}"


def zip_csv(payload: bytes, target_name: str) -> tuple[list[dict[str, str]], str | None]:
    raw = zip_member_bytes(payload, target_name)
    if raw is None:
        return [], "missing_in_remote_zip"
    try:
        return parse_csv_bytes(raw), None
    except Exception as exc:
        return [], f"invalid_remote_csv:{exc}"


def local_json(path: Path) -> tuple[Any, str | None]:
    return base.read_json(path)


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

    loaded_env_files = load_service_environment(repo)

    # Import only after environment loading. Importing this module has no
    # trading execution side effects; we explicitly call download helpers only.
    import paper_trading_storage as storage

    forbidden = {"restore", "upload"}
    # A visible internal guard: this script does not reference/call either action.
    assert forbidden.isdisjoint({"session", "api_url", "download_asset_bytes"})

    client = storage.session()
    release_url = storage.api_url(f"/releases/tags/{storage.RELEASE_TAG}")
    response = client.get(release_url, timeout=30)
    if response.status_code >= 400:
        raise RuntimeError(
            f"Cannot read remote Paper release: HTTP {response.status_code}"
        )
    release = response.json()
    if not isinstance(release, dict):
        raise RuntimeError("Invalid GitHub release response")

    state_asset = release_asset(release, storage.ASSET_NAME)
    trade_asset = release_asset(release, storage.TRADE_LEDGER_ASSET_NAME)
    signal_asset = release_asset(release, storage.SIGNAL_LEDGER_ASSET_NAME)

    state_zip = storage.download_asset_bytes(client, state_asset)
    trade_payload = storage.download_asset_bytes(client, trade_asset)
    signal_payload = storage.download_asset_bytes(client, signal_asset)

    errors: dict[str, str] = {}

    paper_state, error = zip_json(state_zip, "paper_trading_state.json")
    if error:
        errors["paper_state"] = error

    trade_rows = parse_csv_bytes(trade_payload)
    signal_rows = parse_csv_bytes(signal_payload)

    equity_rows, error = zip_csv(state_zip, "paper_trading_equity.csv")
    if error:
        errors["paper_equity_log"] = error

    open_position_rows, error = zip_csv(
        state_zip,
        "paper_trading_open_positions.csv",
    )
    if error:
        errors["paper_open_positions"] = error

    config_snapshot, error = zip_json(
        state_zip,
        "paper_trading_config_snapshot.json",
    )
    if error:
        errors["paper_config_snapshot"] = error

    research_state, error = zip_json(
        state_zip,
        "research_all_signals_state.json",
    )
    if error:
        errors["research_state"] = error

    # Local Evolution and standalone bot states are persistent and safe to read.
    registry_doc, error = local_json(
        repo / "data/evolution/strategy_registry.json"
    )
    if error:
        raise RuntimeError(f"Cannot read strategy registry: {error}")

    research_layers, error = local_json(
        repo / "data/evolution/research_layers.json"
    )
    if error:
        errors["research_layers"] = error

    deployments, error = local_json(
        repo / "data/evolution/deployments.json"
    )
    if error:
        errors["deployments"] = error

    sol_paper_state, error = local_json(
        repo / "reports/sol_spot_adaptive_state.json"
    )
    if error:
        errors["sol_paper_state"] = error

    sol_live_state, error = local_json(
        repo / "reports/sol_spot_live_state.json"
    )
    if error:
        errors["sol_live_state"] = error

    sol_live_status, error = local_json(
        repo / "reports/sol_spot_live_status.json"
    )
    if error:
        errors["sol_live_status"] = error

    records = base.registry_records(registry_doc)
    accounts, unmapped_profiles = base.build_paper_accounts(
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
        item["trade_summary"].get("closed_trades") or 0
        for item in accounts
    )

    registered_profiles = {
        str((item.get("metadata") or {}).get("legacy_profile_name") or "").strip()
        for item in records
        if (item.get("metadata") or {}).get("source_kind") == "paper_portfolio"
    }
    mapped_profiles = {item["profile_name"] for item in accounts}
    missing_registry_profiles = sorted(
        name for name in registered_profiles if name and name not in mapped_profiles
    )

    protected_live = base.compact_json_state(sol_live_state, live=True)
    protected_live["status_report"] = base.compact_json_state(
        sol_live_status,
        live=True,
    )
    protected_live["deployment_registry"] = deployments

    validation = {
        "valid": (
            not missing_registry_profiles
            and len(accounts) == len(registered_profiles)
            and len(trade_rows) > 0
            and len(signal_rows) > 0
        ),
        "registered_paper_profiles": len(registered_profiles),
        "mapped_paper_accounts": len(accounts),
        "missing_registry_profiles": missing_registry_profiles,
        "unmapped_runtime_profiles": unmapped_profiles,
        "source_errors": errors,
        "remote_trade_ledger_rows": len(trade_rows),
        "remote_signal_ledger_rows": len(signal_rows),
        "live_is_observation_only": True,
    }

    snapshot = {
        "schema_version": base.SCHEMA_VERSION,
        "generated_at": base.utc_now_iso(),
        "repository": str(repo),
        "mode": "REMOTE_LEDGER_OBSERVATION_ONLY",
        "safety": {
            "trading_state_changed": False,
            "trading_configuration_changed": False,
            "services_restarted": False,
            "orders_sent": False,
            "live_parameter_changes_allowed": False,
            "paper_restore_called": False,
            "paper_upload_called": False,
            "operational_reports_written": False,
        },
        "remote_source": {
            "release_tag": storage.RELEASE_TAG,
            "state_asset_name": storage.ASSET_NAME,
            "trade_ledger_asset_name": storage.TRADE_LEDGER_ASSET_NAME,
            "signal_ledger_asset_name": storage.SIGNAL_LEDGER_ASSET_NAME,
            "state_asset_id": state_asset.get("id"),
            "trade_asset_id": trade_asset.get("id"),
            "signal_asset_id": signal_asset.get("id"),
            "state_zip_bytes": len(state_zip),
            "trade_ledger_bytes": len(trade_payload),
            "signal_ledger_bytes": len(signal_payload),
            "environment_files_loaded_count": len(loaded_env_files),
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
            "source": "github_release_permanent_ledgers",
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
            **base.summarize_research(research_state),
            "registered_layers": research_layers,
        },
        "sol_spot_adaptive_paper": base.compact_json_state(sol_paper_state),
        "live_deployment": protected_live,
        "validation": validation,
    }

    output = repo / args.output
    markdown_output = repo / args.markdown_output
    base.atomic_write_json(output, snapshot)
    base.atomic_write_text(markdown_output, base.render_markdown(snapshot))

    print("=== EVOLUTION REMOTE RUNTIME SNAPSHOT ===")
    print(f"Release: {storage.RELEASE_TAG}")
    print(f"Strategie registrate: {len(records)}")
    print(f"Account paper mappati: {len(accounts)}")
    print(f"Con posizioni aperte: {activity_counts['ACTIVE_POSITION']}")
    print(f"Con storico: {activity_counts['HAS_HISTORY']}")
    print(f"A zero attività: {activity_counts['ZERO_ACTIVITY']}")
    print(f"Posizioni paper aperte: {total_open}")
    print(f"Trade permanenti: {len(trade_rows)}")
    print(f"Segnali permanenti: {len(signal_rows)}")
    print(f"Profili runtime non mappati: {len(unmapped_profiles)}")
    print(f"Errori/assenze non critiche: {len(errors)}")
    print(f"Validazione: {'OK' if validation['valid'] else 'ATTENZIONE'}")
    print(f"JSON: {output}")
    print(f"Markdown: {markdown_output}")
    print("Restore Paper NON eseguito.")
    print("Upload Paper NON eseguito.")
    print("Nessun file operativo è stato modificato.")
    print("Nessun servizio è stato riavviato.")
    print("Nessun ordine è stato inviato.")
    return 0 if validation["valid"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
