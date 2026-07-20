# -*- coding: utf-8 -*-
"""Persist paper-trading state in a dedicated GitHub Release asset.

Usage:
    python paper_trading_storage.py restore
    python paper_trading_storage.py upload
    python paper_trading_storage.py audit
"""

from __future__ import annotations

import csv
import io
import json
import os
import sys
import zipfile
from pathlib import Path, PurePosixPath
from typing import Any

import requests

REPORTS_DIR = Path("reports")
STATUS_PATH = REPORTS_DIR / "paper_trading_storage_status.json"
ASSET_NAME = os.getenv("PAPER_TRADING_ASSET_NAME", "paper-trading-state.zip")
TRADE_LEDGER_ASSET_NAME = os.getenv(
    "PAPER_TRADING_TRADE_LEDGER_ASSET_NAME",
    "paper-trading-permanent-trades.csv",
)
SIGNAL_LEDGER_ASSET_NAME = os.getenv(
    "PAPER_TRADING_SIGNAL_LEDGER_ASSET_NAME",
    "paper-trading-permanent-signals.csv",
)
RELEASE_TAG = os.getenv("PAPER_TRADING_RELEASE_TAG", "paper-trading-v1")

TRADE_LOG_NAME = "paper_trading_trade_log.csv"
SIGNAL_LOG_NAME = "paper_trading_signal_log.csv"
TRADE_LOG_PATH = REPORTS_DIR / TRADE_LOG_NAME
SIGNAL_LOG_PATH = REPORTS_DIR / SIGNAL_LOG_NAME

FILES = (
    "paper_trading_state.json",
    "paper_trading_trade_log.csv",
    "paper_trading_trade_path.csv",
    "paper_trading_exit_analysis.csv",
    "paper_trading_exit_analysis.md",
    "paper_trading_trade_log_repair_status.json",
    "paper_trading_trade_log_quarantine.csv",
    "paper_trading_trade_log_before_repair.csv",
    "paper_trading_signal_log.csv",
    "paper_trading_equity.csv",
    "paper_trading_open_positions.csv",
    "paper_trading_shadow_metrics.csv",
    # BLOCK3_SHADOW_EXIT_STORAGE_START
    "paper_trading_shadow_exit_state.json",
    "paper_trading_shadow_exit_events.csv",
    "paper_trading_shadow_exit_results.csv",
    "paper_trading_shadow_exit_metrics.csv",
    "paper_trading_shadow_exit_report.md",
    "paper_trading_shadow_exit_config_snapshot.json",
    # BLOCK3_SHADOW_EXIT_STORAGE_END
    # BLOCK4_SHADOW_EVALUATION_STORAGE_START
    "paper_trading_shadow_evaluation_state.json",
    "paper_trading_shadow_evaluations.csv",
    "paper_trading_shadow_evaluation_history.csv",
    "paper_trading_shadow_evaluation_candidates.json",
    "paper_trading_shadow_evaluation_report.md",
    "paper_trading_shadow_evaluation_config_snapshot.json",
    # BLOCK4_SHADOW_EVALUATION_STORAGE_END
    # BLOCK4_5_CRASH_GUARD_STORAGE_START
    "paper_trading_crash_guard_state.json",
    "paper_trading_crash_guard_decisions.csv",
    "paper_trading_crash_guard_events.csv",
    "paper_trading_crash_guard_shadow_results.csv",
    "paper_trading_crash_guard_stress_test.json",
    "paper_trading_crash_guard_report.md",
    "paper_trading_crash_guard_config_snapshot.json",
    # BLOCK4_5_CRASH_GUARD_STORAGE_END
    # BLOCK5_EVOLUTION_CANDIDATE_STORAGE_START
    "paper_trading_evolution_candidate_state.json",
    "paper_trading_evolution_candidate_registry.json",
    "paper_trading_evolution_candidate_events.csv",
    "paper_trading_evolution_candidate_report.md",
    "paper_trading_evolution_candidate_config_snapshot.json",
    # BLOCK5_EVOLUTION_CANDIDATE_STORAGE_END
    # BLOCK6_CANDIDATE_VALIDATION_STORAGE_START
    "paper_trading_evolution_candidate_validation_state.json",
    "paper_trading_evolution_candidate_validations.csv",
    "paper_trading_evolution_candidate_validation_history.csv",
    "paper_trading_evolution_promotion_review.json",
    "paper_trading_evolution_candidate_validation_report.md",
    "paper_trading_evolution_candidate_validation_config_snapshot.json",
    # BLOCK6_CANDIDATE_VALIDATION_STORAGE_END
    # BLOCK7_PROMOTION_GOVERNANCE_STORAGE_START
    "paper_trading_evolution_promotion_state.json",
    "paper_trading_evolution_promotion_governance_state.json",
    "paper_trading_evolution_promotion_plans.json",
    "paper_trading_evolution_promotion_events.csv",
    "paper_trading_evolution_promotion_report.md",
    "paper_trading_evolution_promotion_config_snapshot.json",
    # BLOCK7_PROMOTION_GOVERNANCE_STORAGE_END
    # BLOCK8_POST_PROMOTION_WATCHDOG_STORAGE_START
    "paper_trading_evolution_post_promotion_state.json",
    "paper_trading_evolution_post_promotion_comparisons.csv",
    "paper_trading_evolution_post_promotion_history.csv",
    "paper_trading_evolution_rollback_recommendations.json",
    "paper_trading_evolution_post_promotion_report.md",
    "paper_trading_evolution_post_promotion_config_snapshot.json",
    # BLOCK8_POST_PROMOTION_WATCHDOG_STORAGE_END
    # BLOCK9_EVOLUTION_MEMORY_STORAGE_START
    "paper_trading_evolution_memory_state.json",
    "paper_trading_evolution_scores.csv",
    "paper_trading_evolution_hall_of_fame.json",
    "paper_trading_evolution_hall_of_fame.csv",
    "paper_trading_evolution_genetic_memory.json",
    "paper_trading_evolution_genetic_memory.csv",
    "paper_trading_evolution_memory_history.csv",
    "paper_trading_evolution_memory_report.md",
    "paper_trading_evolution_memory_config_snapshot.json",
    # BLOCK9_EVOLUTION_MEMORY_STORAGE_END
    # BLOCK10_REGIME_EVOLUTION_STORAGE_START
    "paper_trading_evolution_regime_state.json",
    "paper_trading_evolution_regime_performance.csv",
    "paper_trading_evolution_regime_leaderboard.json",
    "paper_trading_evolution_regime_memory.json",
    "paper_trading_evolution_regime_history.csv",
    "paper_trading_evolution_regime_report.md",
    "paper_trading_evolution_regime_config_snapshot.json",
    # BLOCK10_REGIME_EVOLUTION_STORAGE_END
    # BLOCK11_PROTECTED_LIVE_BRIDGE_STORAGE_START
    "paper_trading_evolution_live_bridge_state.json",
    "paper_trading_evolution_live_release_candidates.csv",
    "paper_trading_evolution_live_release_plans.json",
    "paper_trading_evolution_live_release_approvals.json",
    "paper_trading_evolution_live_release_history.csv",
    "paper_trading_evolution_live_release_report.md",
    "paper_trading_evolution_live_release_config_snapshot.json",
    # BLOCK11_PROTECTED_LIVE_BRIDGE_STORAGE_END
    # BLOCK12_EVOLUTION_CONTROL_TOWER_STORAGE_START
    "paper_trading_evolution_control_tower_state.json",
    "paper_trading_evolution_control_tower_checks.csv",
    "paper_trading_evolution_control_tower_incidents.json",
    "paper_trading_evolution_control_tower_audit_chain.csv",
    "paper_trading_evolution_recovery_readiness.json",
    "paper_trading_evolution_control_tower_report.md",
    "paper_trading_evolution_control_tower_config_snapshot.json",
    # BLOCK12_EVOLUTION_CONTROL_TOWER_STORAGE_END
    "paper_trading_config_snapshot.json",
    "paper_trading_market_cache.json",
    "paper_trading_signal_diagnostics.json",
    "paper_trading_report.md",
    "research_all_signals_state.json",
    "research_all_signals_trades.csv",
    "research_all_signals_report.md",
    "research_all_signals_latest.json",
    "market_regime_latest.json",
    "market_regime_history.csv",
    "doge_rejection_short_state.json",
    "doge_rejection_short_trades.csv",
    "doge_rejection_short_report.md",
    "doge_rejection_short_latest.json",
    "doge_rejection_short_status_state.json",
)


class StorageError(RuntimeError):
    pass


def repo_name() -> str:
    value = os.getenv("GITHUB_REPOSITORY", "").strip()
    if not value or "/" not in value:
        raise StorageError("GITHUB_REPOSITORY mancante o non valido.")
    return value


def token() -> str:
    value = os.getenv("GITHUB_TOKEN", "").strip()
    if not value:
        raise StorageError("GITHUB_TOKEN mancante.")
    return value


def session() -> requests.Session:
    client = requests.Session()
    client.headers.update(
        {
            "Authorization": f"Bearer {token()}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "crypto-fractal-scanner-paper-storage/1.0",
        }
    )
    return client


def api_url(path: str) -> str:
    return f"https://api.github.com/repos/{repo_name()}{path}"


def request_json(client: requests.Session, method: str, url: str, **kwargs: Any) -> Any:
    response = client.request(method, url, timeout=30, **kwargs)
    if response.status_code >= 400:
        raise StorageError(f"GitHub {method} {url}: {response.status_code} {response.text[:500]}")
    if not response.content:
        return None
    return response.json()


def get_or_create_release(client: requests.Session) -> dict[str, Any]:
    response = client.get(api_url(f"/releases/tags/{RELEASE_TAG}"), timeout=30)
    if response.status_code == 200:
        return response.json()
    if response.status_code != 404:
        raise StorageError(f"Ricerca release fallita: {response.status_code} {response.text[:500]}")
    return request_json(
        client,
        "POST",
        api_url("/releases"),
        json={
            "tag_name": RELEASE_TAG,
            "name": "Paper Trading Persistent State",
            "body": "Stato automatico del paper trading. Asset gestito da GitHub Actions.",
            "draft": False,
            "prerelease": False,
        },
    )


def find_named_asset(
    release: dict[str, Any],
    name: str,
) -> dict[str, Any] | None:
    for asset in release.get("assets", []):
        if asset.get("name") == name:
            return asset
    return None


def find_asset(release: dict[str, Any]) -> dict[str, Any] | None:
    return find_named_asset(release, ASSET_NAME)


def download_asset_bytes(
    client: requests.Session,
    asset: dict[str, Any],
) -> bytes:
    response = client.get(
        asset["url"],
        headers={"Accept": "application/octet-stream"},
        timeout=60,
    )
    response.raise_for_status()
    return response.content


def read_csv_bytes(payload: bytes) -> list[dict[str, str]]:
    text = payload.decode("utf-8-sig", errors="replace")
    return list(csv.DictReader(io.StringIO(text)))


def read_csv_path(path: Path) -> list[dict[str, str]]:
    if not path.exists() or path.stat().st_size == 0:
        return []
    with path.open(
        "r",
        encoding="utf-8-sig",
        newline="",
    ) as handle:
        return list(csv.DictReader(handle))


def csv_bytes(rows: list[dict[str, str]]) -> bytes:
    if not rows:
        return b""
    fields: list[str] = []
    for row in rows:
        for key in row:
            if key not in fields:
                fields.append(key)
    buffer = io.StringIO()
    writer = csv.DictWriter(
        buffer,
        fieldnames=fields,
        extrasaction="ignore",
        lineterminator="\n",
    )
    writer.writeheader()
    writer.writerows(rows)
    return buffer.getvalue().encode("utf-8")


def write_csv_path(
    path: Path,
    rows: list[dict[str, str]],
) -> None:
    if not rows:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(csv_bytes(rows))


def trade_key(row: dict[str, Any]) -> tuple[str, str, str]:
    return (
        str(row.get("trade_id", "")).strip(),
        str(row.get("portfolio", "")).strip(),
        str(row.get("closed_at", "")).strip(),
    )


def signal_key(row: dict[str, Any]) -> tuple[str, str, str, str]:
    return (
        str(row.get("signal_id", "")).strip(),
        str(row.get("portfolio", "")).strip(),
        str(row.get("processed_at", "")).strip(),
        str(row.get("decision", "")).strip(),
    )


def merge_rows(
    remote_rows: list[dict[str, str]],
    local_rows: list[dict[str, str]],
    key_function,
) -> list[dict[str, str]]:
    merged = {}
    for row in remote_rows + local_rows:
        key = key_function(row)
        if any(key):
            merged[key] = row
    return sorted(
        merged.values(),
        key=lambda row: (
            str(
                row.get("closed_at")
                or row.get("processed_at")
                or row.get("opened_at")
                or ""
            ),
            str(row.get("portfolio", "")),
            str(row.get("trade_id") or row.get("signal_id") or ""),
        ),
    )


def restore_permanent_csv(
    client: requests.Session,
    release: dict[str, Any],
    asset_name: str,
    local_path: Path,
    key_function,
) -> int:
    asset = find_named_asset(release, asset_name)
    remote_rows = (
        read_csv_bytes(download_asset_bytes(client, asset))
        if asset
        else []
    )
    merged = merge_rows(
        remote_rows,
        read_csv_path(local_path),
        key_function,
    )
    if merged:
        write_csv_path(local_path, merged)
    return len(merged)


def upload_named_asset(
    client: requests.Session,
    release: dict[str, Any],
    name: str,
    payload: bytes,
    content_type: str,
) -> int | None:
    existing = find_named_asset(release, name)
    if existing:
        request_json(
            client,
            "DELETE",
            api_url(f"/releases/assets/{existing['id']}"),
        )
    upload_url = str(release["upload_url"]).split("{")[0]
    response = client.post(
        upload_url,
        params={"name": name},
        data=payload,
        headers={"Content-Type": content_type},
        timeout=90,
    )
    if response.status_code >= 400:
        raise StorageError(
            f"Upload {name}: "
            f"{response.status_code} {response.text[:500]}"
        )
    return response.json().get("id")


def merge_and_upload_permanent_csv(
    client: requests.Session,
    release: dict[str, Any],
    asset_name: str,
    local_path: Path,
    key_function,
) -> tuple[int, int | None]:
    asset = find_named_asset(release, asset_name)
    remote_rows = (
        read_csv_bytes(download_asset_bytes(client, asset))
        if asset
        else []
    )
    merged = merge_rows(
        remote_rows,
        read_csv_path(local_path),
        key_function,
    )
    if not merged:
        return 0, None
    write_csv_path(local_path, merged)
    asset_id = upload_named_asset(
        client,
        release,
        asset_name,
        csv_bytes(merged),
        "text/csv; charset=utf-8",
    )
    return len(merged), asset_id


def build_archive() -> bytes:
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for name in FILES:
            path = REPORTS_DIR / name
            if path.exists() and path.is_file():
                archive.write(path, arcname=f"reports/{name}")
    return buffer.getvalue()


def safe_extract(payload: bytes) -> list[str]:
    restored: list[str] = []
    allowed = {f"reports/{name}" for name in FILES}
    with zipfile.ZipFile(io.BytesIO(payload)) as archive:
        for info in archive.infolist():
            normalized = str(PurePosixPath(info.filename))
            if normalized not in allowed or info.is_dir():
                continue
            target = Path(normalized)
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(archive.read(info))
            restored.append(normalized)
    return restored


def write_status(action: str, ok: bool, detail: dict[str, Any]) -> None:
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    STATUS_PATH.write_text(
        json.dumps({"action": action, "ok": ok, "tag": RELEASE_TAG, "asset": ASSET_NAME, **detail}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def restore() -> None:
    client = session()
    response = client.get(api_url(f"/releases/tags/{RELEASE_TAG}"), timeout=30)
    if response.status_code == 404:
        write_status("restore", True, {"restored": [], "message": "release non ancora esistente"})
        print("Nessuno stato remoto: prima esecuzione.")
        return
    if response.status_code >= 400:
        raise StorageError(f"Restore release: {response.status_code} {response.text[:500]}")
    release = response.json()
    asset = find_asset(release)
    if not asset:
        write_status("restore", True, {"restored": [], "message": "asset non ancora esistente"})
        print("Nessun asset remoto: prima esecuzione.")
        return
    restored = safe_extract(
        download_asset_bytes(client, asset)
    )

    trade_rows = restore_permanent_csv(
        client,
        release,
        TRADE_LEDGER_ASSET_NAME,
        TRADE_LOG_PATH,
        trade_key,
    )
    signal_rows = restore_permanent_csv(
        client,
        release,
        SIGNAL_LEDGER_ASSET_NAME,
        SIGNAL_LOG_PATH,
        signal_key,
    )

    write_status(
        "restore",
        True,
        {
            "restored": restored,
            "asset_id": asset.get("id"),
            "permanent_trade_rows": trade_rows,
            "permanent_signal_rows": signal_rows,
        },
    )
    print(
        "Ripristinati:",
        ", ".join(restored) if restored else "nessun file",
    )
    print(
        f"Ledger permanenti: trade={trade_rows}, "
        f"segnali={signal_rows}"
    )


def upload() -> None:
    client = session()
    release = get_or_create_release(client)

    trade_rows, trade_asset_id = (
        merge_and_upload_permanent_csv(
            client,
            release,
            TRADE_LEDGER_ASSET_NAME,
            TRADE_LOG_PATH,
            trade_key,
        )
    )
    signal_rows, signal_asset_id = (
        merge_and_upload_permanent_csv(
            client,
            release,
            SIGNAL_LEDGER_ASSET_NAME,
            SIGNAL_LOG_PATH,
            signal_key,
        )
    )

    payload = build_archive()
    state_asset_id = upload_named_asset(
        client,
        release,
        ASSET_NAME,
        payload,
        "application/zip",
    )

    write_status(
        "upload",
        True,
        {
            "bytes": len(payload),
            "asset_id": state_asset_id,
            "permanent_trade_rows": trade_rows,
            "permanent_trade_asset_id": trade_asset_id,
            "permanent_signal_rows": signal_rows,
            "permanent_signal_asset_id": signal_asset_id,
        },
    )
    print(f"Stato caricato: {len(payload)} byte")
    print(
        f"Ledger permanenti caricati: trade={trade_rows}, "
        f"segnali={signal_rows}"
    )


def audit() -> None:
    existing = [name for name in FILES if (REPORTS_DIR / name).exists()]
    state_ok = (REPORTS_DIR / "paper_trading_state.json").exists()
    write_status("audit", state_ok, {"existing": existing, "state_available": state_ok})
    print(json.dumps({"state_available": state_ok, "existing": existing}, ensure_ascii=False))


def main() -> None:
    action = sys.argv[1] if len(sys.argv) > 1 else "audit"
    try:
        if action == "restore":
            restore()
        elif action == "upload":
            upload()
        elif action == "audit":
            audit()
        else:
            raise StorageError(f"Azione sconosciuta: {action}")
    except Exception as exc:
        write_status(action, False, {"error": str(exc)})
        raise


if __name__ == "__main__":
    main()
