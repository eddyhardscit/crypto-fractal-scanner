# -*- coding: utf-8 -*-
"""Persistent storage for the dedicated RSI 5m paper scalper.

Usage:
    python paper_rsi5_scalper_storage.py restore
    python paper_rsi5_scalper_storage.py upload
    python paper_rsi5_scalper_storage.py audit
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
STATUS_PATH = REPORTS_DIR / "paper_rsi5_scalper_storage_status.json"
RELEASE_TAG = os.getenv("RSI5_PAPER_RELEASE_TAG", "paper-rsi5-scalper-v1")
ASSET_NAME = os.getenv("RSI5_PAPER_ASSET_NAME", "paper-rsi5-scalper-state.zip")

FILES = (
    "paper_rsi5_scalper_state.json",
    "paper_rsi5_scalper_trades.csv",
    "paper_rsi5_scalper_signals.csv",
    "paper_rsi5_scalper_latest.md",
    "paper_rsi5_scalper_latest.json",
    "paper_rsi5_scalper_shadow_trades.csv",
    "paper_rsi5_scalper_shadow_report.md",
    "paper_rsi5_scalper_shadow_latest.json",
    "paper_rsi5_scalper_storage_status.json",
)


class StorageError(RuntimeError):
    pass


def repo_name() -> str:
    value = os.getenv("GITHUB_REPOSITORY", "").strip()
    if not value or "/" not in value:
        raise StorageError("GITHUB_REPOSITORY mancante o non valido")
    return value


def token() -> str:
    value = os.getenv("GITHUB_TOKEN", "").strip()
    if not value:
        raise StorageError("GITHUB_TOKEN mancante")
    return value


def session() -> requests.Session:
    client = requests.Session()
    client.headers.update(
        {
            "Authorization": f"Bearer {token()}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "crypto-fractal-scanner-rsi5-storage/1.0",
        }
    )
    return client


def api_url(path: str) -> str:
    return f"https://api.github.com/repos/{repo_name()}{path}"


def request_json(client: requests.Session, method: str, url: str, **kwargs: Any) -> Any:
    response = client.request(method, url, timeout=60, **kwargs)
    if response.status_code >= 400:
        raise StorageError(
            f"GitHub {method} {url}: {response.status_code} {response.text[:500]}"
        )
    return response.json() if response.content else None


def get_or_create_release(client: requests.Session) -> dict[str, Any]:
    response = client.get(api_url(f"/releases/tags/{RELEASE_TAG}"), timeout=30)
    if response.status_code == 200:
        return response.json()
    if response.status_code != 404:
        raise StorageError(
            f"Ricerca release fallita: {response.status_code} {response.text[:500]}"
        )
    return request_json(
        client,
        "POST",
        api_url("/releases"),
        json={
            "tag_name": RELEASE_TAG,
            "name": "RSI 5m Paper Scalper State",
            "body": "Stato persistente separato della strategia RSI 5m. Solo paper trading.",
            "draft": False,
            "prerelease": False,
        },
    )


def find_asset(release: dict[str, Any]) -> dict[str, Any] | None:
    for asset in release.get("assets", []):
        if asset.get("name") == ASSET_NAME:
            return asset
    return None


def download_asset(client: requests.Session, asset: dict[str, Any]) -> bytes:
    response = client.get(
        asset["url"],
        headers={"Accept": "application/octet-stream"},
        timeout=90,
    )
    response.raise_for_status()
    return response.content


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
            if info.is_dir() or normalized not in allowed:
                continue
            target = Path(normalized)
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(archive.read(info))
            restored.append(normalized)
    return restored


def write_status(action: str, ok: bool, detail: dict[str, Any]) -> None:
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    STATUS_PATH.write_text(
        json.dumps(
            {
                "action": action,
                "ok": ok,
                "release_tag": RELEASE_TAG,
                "asset_name": ASSET_NAME,
                **detail,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )


def restore() -> None:
    client = session()
    response = client.get(api_url(f"/releases/tags/{RELEASE_TAG}"), timeout=30)
    if response.status_code == 404:
        write_status("restore", True, {"restored": [], "message": "prima esecuzione"})
        print("Release RSI5 non ancora esistente: prima esecuzione.")
        return
    if response.status_code >= 400:
        raise StorageError(
            f"Restore release: {response.status_code} {response.text[:500]}"
        )
    release = response.json()
    asset = find_asset(release)
    if not asset:
        write_status("restore", True, {"restored": [], "message": "asset assente"})
        print("Asset RSI5 non ancora esistente: prima esecuzione.")
        return
    restored = safe_extract(download_asset(client, asset))
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
        raise StorageError(
            f"Upload stato: {response.status_code} {response.text[:500]}"
        )
    result = response.json()
    write_status(
        "upload",
        True,
        {"bytes": len(payload), "asset_id": result.get("id")},
    )
    print(f"Stato RSI5 caricato: {len(payload)} byte")


def audit() -> None:
    existing = [name for name in FILES if (REPORTS_DIR / name).exists()]
    state_ok = (REPORTS_DIR / "paper_rsi5_scalper_state.json").exists()
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
