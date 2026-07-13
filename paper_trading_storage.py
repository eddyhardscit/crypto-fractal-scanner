# -*- coding: utf-8 -*-
"""Persist paper-trading state in a dedicated GitHub Release asset.

Usage:
    python paper_trading_storage.py restore
    python paper_trading_storage.py upload
    python paper_trading_storage.py audit
"""

from __future__ import annotations

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
RELEASE_TAG = os.getenv("PAPER_TRADING_RELEASE_TAG", "paper-trading-v1")
FILES = (
    "paper_trading_state.json",
    "paper_trading_trade_log.csv",
    "paper_trading_signal_log.csv",
    "paper_trading_equity.csv",
    "paper_trading_open_positions.csv",
    "paper_trading_shadow_metrics.csv",
    "paper_trading_config_snapshot.json",
    "paper_trading_market_cache.json",
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


def find_asset(release: dict[str, Any]) -> dict[str, Any] | None:
    for asset in release.get("assets", []):
        if asset.get("name") == ASSET_NAME:
            return asset
    return None


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
    download = client.get(asset["url"], headers={"Accept": "application/octet-stream"}, timeout=60)
    download.raise_for_status()
    restored = safe_extract(download.content)
    write_status("restore", True, {"restored": restored, "asset_id": asset.get("id")})
    print("Ripristinati:", ", ".join(restored) if restored else "nessun file")


def upload() -> None:
    client = session()
    release = get_or_create_release(client)
    existing = find_asset(release)
    if existing:
        request_json(client, "DELETE", api_url(f"/releases/assets/{existing['id']}"))
    payload = build_archive()
    upload_url = str(release["upload_url"]).split("{")[0]
    response = client.post(
        upload_url,
        params={"name": ASSET_NAME},
        data=payload,
        headers={"Content-Type": "application/zip"},
        timeout=90,
    )
    if response.status_code >= 400:
        raise StorageError(f"Upload asset: {response.status_code} {response.text[:500]}")
    asset = response.json()
    write_status("upload", True, {"bytes": len(payload), "asset_id": asset.get("id")})
    print(f"Stato caricato: {len(payload)} byte")


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
