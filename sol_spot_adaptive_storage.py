# -*- coding: utf-8 -*-
"""Dedicated GitHub Release storage for SOL spot adaptive paper state."""

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
STATUS_PATH = REPORTS_DIR / "sol_spot_adaptive_storage_status.json"
ASSET_NAME = os.getenv("SOL_SPOT_ADAPTIVE_ASSET_NAME", "sol-spot-adaptive-state.zip")
RELEASE_TAG = os.getenv("SOL_SPOT_ADAPTIVE_RELEASE_TAG", "sol-spot-adaptive-v1")
FILES = (
    "sol_spot_adaptive_state.json",
    "sol_spot_adaptive_trades.csv",
    "sol_spot_adaptive_equity.csv",
    "sol_spot_adaptive_latest.json",
    "sol_spot_adaptive_report.md",
    "sol_spot_adaptive_config_snapshot.json",
)


class StorageError(RuntimeError):
    pass


def repo_name() -> str:
    value = os.getenv("GITHUB_REPOSITORY", "").strip()
    if not value or "/" not in value:
        raise StorageError("GITHUB_REPOSITORY missing or invalid.")
    return value


def token() -> str:
    value = os.getenv("GITHUB_TOKEN", "").strip()
    if not value:
        raise StorageError("GITHUB_TOKEN missing.")
    return value


def session() -> requests.Session:
    client = requests.Session()
    client.headers.update(
        {
            "Authorization": f"Bearer {token()}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "crypto-fractal-scanner-sol-spot-storage/1.0",
        }
    )
    return client


def api_url(path: str) -> str:
    return f"https://api.github.com/repos/{repo_name()}{path}"


def request_json(client: requests.Session, method: str, url: str, **kwargs: Any) -> Any:
    response = client.request(method, url, timeout=30, **kwargs)
    if response.status_code >= 400:
        raise StorageError(f"GitHub {method} {url}: {response.status_code} {response.text[:500]}")
    return response.json() if response.content else None


def get_or_create_release(client: requests.Session) -> dict[str, Any]:
    response = client.get(api_url(f"/releases/tags/{RELEASE_TAG}"), timeout=30)
    if response.status_code == 200:
        return response.json()
    if response.status_code != 404:
        raise StorageError(f"Release lookup failed: {response.status_code} {response.text[:500]}")
    return request_json(
        client,
        "POST",
        api_url("/releases"),
        json={
            "tag_name": RELEASE_TAG,
            "name": "SOL Spot Adaptive Range Paper State",
            "body": "Persistent state for the SOL-only spot paper simulation. No exchange orders.",
            "draft": False,
            "prerelease": False,
        },
    )


def find_asset(release: dict[str, Any]) -> dict[str, Any] | None:
    return next((asset for asset in release.get("assets", []) if asset.get("name") == ASSET_NAME), None)


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
        json.dumps(
            {"action": action, "ok": ok, "tag": RELEASE_TAG, "asset": ASSET_NAME, **detail},
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )


def restore() -> None:
    client = session()
    response = client.get(api_url(f"/releases/tags/{RELEASE_TAG}"), timeout=30)
    if response.status_code == 404:
        write_status("restore", True, {"restored": [], "message": "first run"})
        print("No remote SOL spot paper state yet.")
        return
    if response.status_code >= 400:
        raise StorageError(f"Restore failed: {response.status_code} {response.text[:500]}")
    asset = find_asset(response.json())
    if not asset:
        write_status("restore", True, {"restored": [], "message": "asset not created yet"})
        print("SOL spot paper release exists without state asset.")
        return
    download = client.get(asset["url"], headers={"Accept": "application/octet-stream"}, timeout=60)
    download.raise_for_status()
    restored = safe_extract(download.content)
    write_status("restore", True, {"restored": restored, "asset_id": asset.get("id")})
    print("Restored:", ", ".join(restored) if restored else "none")


def upload() -> None:
    client = session()
    release = get_or_create_release(client)
    existing = find_asset(release)
    if existing:
        request_json(client, "DELETE", api_url(f"/releases/assets/{existing['id']}"))
    payload = build_archive()
    if not payload:
        raise StorageError("SOL spot paper archive is empty.")
    upload_url = str(release["upload_url"]).split("{")[0]
    response = client.post(
        upload_url,
        params={"name": ASSET_NAME},
        data=payload,
        headers={"Content-Type": "application/zip"},
        timeout=90,
    )
    if response.status_code >= 400:
        raise StorageError(f"Upload failed: {response.status_code} {response.text[:500]}")
    write_status("upload", True, {"bytes": len(payload), "asset_id": response.json().get("id")})
    print(f"Uploaded SOL spot paper state: {len(payload)} bytes")


def audit() -> None:
    existing = [name for name in FILES if (REPORTS_DIR / name).exists()]
    state_ok = (REPORTS_DIR / "sol_spot_adaptive_state.json").exists()
    write_status("audit", state_ok, {"existing": existing, "state_available": state_ok})
    print(json.dumps({"state_available": state_ok, "existing": existing}))


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
            raise StorageError(f"Unknown action: {action}")
    except Exception as exc:
        write_status(action, False, {"error": str(exc)})
        raise


if __name__ == "__main__":
    main()
