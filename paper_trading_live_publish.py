# -*- coding: utf-8 -*-
"""Publish the stable paper-trading dashboard on a dedicated GitHub branch.

Using a separate branch avoids conflicting with the long daily scanner commit on
``main``. The branch is created automatically from the default branch the first
time the intraday workflow publishes a dashboard.
"""

from __future__ import annotations

import base64
import os
from typing import Any

import requests


def _credentials() -> tuple[str, str]:
    return (
        os.getenv("GITHUB_TOKEN", "").strip(),
        os.getenv("GITHUB_REPOSITORY", "").strip(),
    )


def _headers(token: str) -> dict[str, str]:
    return {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "crypto-fractal-scanner-live-dashboard/1.0",
    }


def _ensure_branch(
    session: requests.Session,
    api_root: str,
    headers: dict[str, str],
    branch: str,
    base_branch: str,
) -> None:
    response = session.get(f"{api_root}/git/ref/heads/{branch}", headers=headers, timeout=30)
    if response.status_code == 200:
        return
    if response.status_code != 404:
        response.raise_for_status()

    base = session.get(f"{api_root}/git/ref/heads/{base_branch}", headers=headers, timeout=30)
    base.raise_for_status()
    sha = base.json()["object"]["sha"]
    created = session.post(
        f"{api_root}/git/refs",
        headers=headers,
        json={"ref": f"refs/heads/{branch}", "sha": sha},
        timeout=30,
    )
    if created.status_code not in (201, 422):
        created.raise_for_status()


def publish_markdown(
    repository_path: str,
    content: str,
    commit_message: str = "Update live paper trading dashboard",
    branch: str = "paper-trading-live",
    base_branch: str = "main",
) -> dict[str, Any]:
    token, repository = _credentials()
    result: dict[str, Any] = {
        "configured": bool(token and repository and "/" in repository),
        "published": False,
        "unchanged": False,
        "path": repository_path,
        "branch": branch,
    }
    if not result["configured"]:
        result["reason"] = "GitHub environment unavailable"
        return result

    headers = _headers(token)
    api_root = f"https://api.github.com/repos/{repository}"
    url = f"{api_root}/contents/{repository_path}"
    desired = content.encode("utf-8")
    session = requests.Session()
    _ensure_branch(session, api_root, headers, branch, base_branch)

    def current_file() -> tuple[str | None, bytes | None]:
        response = session.get(url, headers=headers, params={"ref": branch}, timeout=30)
        if response.status_code == 404:
            return None, None
        response.raise_for_status()
        payload = response.json()
        encoded = str(payload.get("content", "")).replace("\n", "")
        remote = base64.b64decode(encoded) if encoded else b""
        return str(payload.get("sha", "")) or None, remote

    for attempt in range(2):
        sha, remote = current_file()
        if remote == desired:
            result["unchanged"] = True
            return result
        payload: dict[str, Any] = {
            "message": commit_message,
            "content": base64.b64encode(desired).decode("ascii"),
            "branch": branch,
        }
        if sha:
            payload["sha"] = sha
        response = session.put(url, headers=headers, json=payload, timeout=45)
        if response.status_code in (200, 201):
            body = response.json()
            result["published"] = True
            result["commit_sha"] = body.get("commit", {}).get("sha")
            result["html_url"] = f"https://github.com/{repository}/blob/{branch}/{repository_path}"
            return result
        if response.status_code == 409 and attempt == 0:
            continue
        response.raise_for_status()

    return result
