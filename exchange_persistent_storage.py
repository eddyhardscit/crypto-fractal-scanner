# -*- coding: utf-8 -*-
"""Persistent storage for exchange intraday data without Git commits.

Design goals:
- keep a rolling 180-day working state in two redundant GitHub Release assets;
- keep one immutable compressed archive per completed UTC month;
- restore the newest valid state and fall back to the second slot if necessary;
- validate every state bundle with SHA-256 hashes before restoring it;
- support an offline local-directory backend for self-tests.

The GitHub backend uses only the repository-scoped ``GITHUB_TOKEN`` and the
repository's own Release assets. No external account, database, or secret is
required.
"""

from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import io
import json
import os
import shutil
import tarfile
import tempfile
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable
from urllib.parse import quote

import requests


SCHEMA_VERSION = "2.1.1"
DEFAULT_RELEASE_TAG = "exchange-data-v2-1"
STATE_ASSETS = ("exchange_state_A.tar.gz", "exchange_state_B.tar.gz")
ACTIVE_CSV = Path("reports/exchange_market_data_intraday.csv")
STATUS_PATH = Path("reports/exchange_storage_status.json")
WORK_DIR = Path(".exchange_storage")
STATE_FILES = (
    Path("reports/exchange_market_data_intraday.csv"),
    Path("reports/exchange_market_data_snapshot.json"),
    Path("reports/exchange_market_data_health.json"),
    Path("reports/exchange_market_data_raw.json"),
)
MANIFEST_NAME = "exchange_state_manifest.json"
ARCHIVE_PREFIX = "exchange_intraday_"
ARCHIVE_SUFFIX = ".csv.gz"
HTTP_TIMEOUT = 30


@dataclass(frozen=True)
class Asset:
    id: int | str
    name: str
    size: int
    updated_at: str
    url: str = ""


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def utc_now_iso() -> str:
    return utc_now().isoformat(timespec="seconds")


def atomic_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(payload, ensure_ascii=False, indent=2, default=str) + "\n", encoding="utf-8")
    tmp.replace(path)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def parse_iso(value: str) -> datetime:
    text = (value or "").strip().replace("Z", "+00:00")
    try:
        parsed = datetime.fromisoformat(text)
    except ValueError:
        return datetime.fromtimestamp(0, tz=timezone.utc)
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def csv_stats(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {"rows": 0, "first_timestamp_utc": None, "last_timestamp_utc": None}
    rows = 0
    first: str | None = None
    last: str | None = None
    with path.open("r", encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            timestamp = str(row.get("timestamp_utc", "")).strip()
            rows += 1
            if timestamp:
                first = timestamp if first is None or timestamp < first else first
                last = timestamp if last is None or timestamp > last else last
    return {"rows": rows, "first_timestamp_utc": first, "last_timestamp_utc": last}


class Store:
    def scoped(self, release_tag: str) -> "Store":
        raise NotImplementedError

    def ensure_release(self) -> None:
        raise NotImplementedError

    def list_assets(self) -> list[Asset]:
        raise NotImplementedError

    def download(self, asset: Asset, destination: Path) -> None:
        raise NotImplementedError

    def upload_replace(self, name: str, source: Path) -> Asset:
        raise NotImplementedError

    def upload_if_missing(self, name: str, source: Path) -> Asset:
        assets = {asset.name: asset for asset in self.list_assets()}
        if name in assets:
            return assets[name]
        return self.upload_replace(name, source)


class LocalStore(Store):
    """Filesystem backend used by offline tests."""

    def __init__(self, root: Path):
        self.root = root

    def scoped(self, release_tag: str) -> Store:
        return LocalStore(self.root / release_tag)

    def ensure_release(self) -> None:
        self.root.mkdir(parents=True, exist_ok=True)

    def list_assets(self) -> list[Asset]:
        self.ensure_release()
        result: list[Asset] = []
        for path in self.root.iterdir():
            if not path.is_file():
                continue
            stat = path.stat()
            result.append(
                Asset(
                    id=path.name,
                    name=path.name,
                    size=stat.st_size,
                    updated_at=datetime.fromtimestamp(stat.st_mtime, tz=timezone.utc).isoformat(),
                    url=str(path),
                )
            )
        return result

    def download(self, asset: Asset, destination: Path) -> None:
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(self.root / asset.name, destination)

    def upload_replace(self, name: str, source: Path) -> Asset:
        self.ensure_release()
        destination = self.root / name
        tmp = destination.with_suffix(destination.suffix + ".tmp")
        shutil.copy2(source, tmp)
        tmp.replace(destination)
        return next(asset for asset in self.list_assets() if asset.name == name)


class GitHubReleaseStore(Store):
    def __init__(self, repository: str, token: str, release_tag: str):
        if "/" not in repository:
            raise RuntimeError("GITHUB_REPOSITORY mancante o non valido (atteso OWNER/REPO).")
        if not token:
            raise RuntimeError("GITHUB_TOKEN/ GH_TOKEN mancante: impossibile usare lo storage persistente.")
        self.repository = repository
        self.token = token
        self.release_tag = release_tag
        self.api = "https://api.github.com"
        self.session = requests.Session()
        self.session.headers.update(
            {
                "Authorization": f"Bearer {token}",
                "Accept": "application/vnd.github+json",
                "X-GitHub-Api-Version": "2022-11-28",
                "User-Agent": "crypto-scanner-exchange-storage/2.1.1",
            }
        )
        self._release: dict[str, Any] | None = None

    def scoped(self, release_tag: str) -> Store:
        return GitHubReleaseStore(self.repository, self.token, release_tag)

    def _request(self, method: str, url: str, **kwargs: Any) -> requests.Response:
        response = self.session.request(method, url, timeout=HTTP_TIMEOUT, **kwargs)
        return response

    def _get_release(self) -> dict[str, Any] | None:
        if self._release is not None:
            return self._release
        url = f"{self.api}/repos/{self.repository}/releases/tags/{quote(self.release_tag, safe='')}"
        response = self._request("GET", url)
        if response.status_code == 404:
            return None
        if response.status_code != 200:
            raise RuntimeError(f"GitHub release lookup HTTP {response.status_code}: {response.text[:400]}")
        self._release = response.json()
        return self._release

    def ensure_release(self) -> None:
        if self._get_release() is not None:
            return
        target = os.getenv("GITHUB_SHA") or os.getenv("GITHUB_REF_NAME") or "main"
        url = f"{self.api}/repos/{self.repository}/releases"
        is_archive = self.release_tag.startswith("exchange-data-archive-")
        archive_year = self.release_tag.rsplit("-", 1)[-1] if is_archive else ""
        payload = {
            "tag_name": self.release_tag,
            "target_commitish": target,
            "name": f"Exchange Intraday Archive {archive_year}" if is_archive else "Exchange Data Storage v2.1",
            "body": (
                f"Archivio mensile permanente dei dati intraday exchange per il {archive_year}. "
                "Non modificare manualmente."
                if is_archive
                else "Storage tecnico automatico dello scanner. Contiene due copie ridondanti "
                "dello stato intraday mobile. Non modificare manualmente."
            ),
            "draft": False,
            "prerelease": True,
        }
        response = self._request("POST", url, json=payload)
        if response.status_code not in (200, 201):
            # A concurrent run may have created it between lookup and POST.
            self._release = None
            if self._get_release() is not None:
                return
            raise RuntimeError(f"GitHub release create HTTP {response.status_code}: {response.text[:400]}")
        self._release = response.json()

    def list_assets(self) -> list[Asset]:
        self.ensure_release()
        assert self._release is not None
        release_id = self._release["id"]
        page = 1
        assets: list[Asset] = []
        while True:
            url = f"{self.api}/repos/{self.repository}/releases/{release_id}/assets"
            response = self._request("GET", url, params={"per_page": 100, "page": page})
            if response.status_code != 200:
                raise RuntimeError(f"GitHub assets list HTTP {response.status_code}: {response.text[:400]}")
            payload = response.json()
            if not isinstance(payload, list):
                raise RuntimeError("GitHub assets payload non valido.")
            for item in payload:
                assets.append(
                    Asset(
                        id=int(item["id"]),
                        name=str(item["name"]),
                        size=int(item.get("size", 0)),
                        updated_at=str(item.get("updated_at") or item.get("created_at") or ""),
                        url=str(item.get("url") or ""),
                    )
                )
            if len(payload) < 100:
                break
            page += 1
        return assets

    def download(self, asset: Asset, destination: Path) -> None:
        destination.parent.mkdir(parents=True, exist_ok=True)
        url = f"{self.api}/repos/{self.repository}/releases/assets/{asset.id}"
        response = self._request("GET", url, headers={"Accept": "application/octet-stream"}, allow_redirects=True)
        if response.status_code != 200:
            raise RuntimeError(f"GitHub asset download HTTP {response.status_code}: {response.text[:400]}")
        tmp = destination.with_suffix(destination.suffix + ".tmp")
        tmp.write_bytes(response.content)
        tmp.replace(destination)

    def _delete_named_asset(self, name: str) -> None:
        for asset in self.list_assets():
            if asset.name != name:
                continue
            url = f"{self.api}/repos/{self.repository}/releases/assets/{asset.id}"
            response = self._request("DELETE", url)
            if response.status_code not in (204, 404):
                raise RuntimeError(f"GitHub asset delete HTTP {response.status_code}: {response.text[:400]}")
            break

    def upload_replace(self, name: str, source: Path) -> Asset:
        self.ensure_release()
        assert self._release is not None
        self._delete_named_asset(name)
        upload_url = str(self._release["upload_url"]).split("{")[0]
        content_type = "application/gzip" if name.endswith(".gz") else "application/octet-stream"
        with source.open("rb") as handle:
            response = self._request(
                "POST",
                upload_url,
                params={"name": name},
                headers={"Content-Type": content_type},
                data=handle,
            )
        if response.status_code not in (200, 201):
            raise RuntimeError(f"GitHub asset upload HTTP {response.status_code}: {response.text[:400]}")
        item = response.json()
        return Asset(
            id=int(item["id"]),
            name=str(item["name"]),
            size=int(item.get("size", 0)),
            updated_at=str(item.get("updated_at") or item.get("created_at") or ""),
            url=str(item.get("url") or ""),
        )


def make_store(args: argparse.Namespace) -> Store:
    local_dir = args.local_dir or os.getenv("EXCHANGE_STORAGE_LOCAL_DIR", "").strip()
    if local_dir:
        return LocalStore(Path(local_dir))
    repository = os.getenv("GITHUB_REPOSITORY", "").strip()
    token = os.getenv("GITHUB_TOKEN", "").strip() or os.getenv("GH_TOKEN", "").strip()
    release_tag = args.release_tag or os.getenv("EXCHANGE_STORAGE_RELEASE_TAG", DEFAULT_RELEASE_TAG)
    return GitHubReleaseStore(repository, token, release_tag)


def safe_member_name(name: str) -> bool:
    path = Path(name)
    return not path.is_absolute() and ".." not in path.parts


def build_state_bundle(destination: Path) -> dict[str, Any]:
    existing = [path for path in STATE_FILES if path.exists()]
    if ACTIVE_CSV not in existing:
        raise RuntimeError(f"Stato intraday mancante: {ACTIVE_CSV}")

    manifest: dict[str, Any] = {
        "schema_version": SCHEMA_VERSION,
        "generated_utc": utc_now_iso(),
        "files": {},
        "intraday": csv_stats(ACTIVE_CSV),
    }
    for path in existing:
        manifest["files"][path.as_posix()] = {
            "sha256": sha256_file(path),
            "size": path.stat().st_size,
        }

    destination.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="exchange-state-build-") as tmp_name:
        tmp = Path(tmp_name)
        manifest_path = tmp / MANIFEST_NAME
        manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        bundle_tmp = destination.with_suffix(destination.suffix + ".tmp")
        with tarfile.open(bundle_tmp, "w:gz") as archive:
            archive.add(manifest_path, arcname=MANIFEST_NAME)
            for path in existing:
                archive.add(path, arcname=path.as_posix())
        bundle_tmp.replace(destination)
    return manifest


def validate_and_restore_bundle(bundle: Path) -> dict[str, Any]:
    with tempfile.TemporaryDirectory(prefix="exchange-state-restore-") as tmp_name:
        tmp = Path(tmp_name)
        with tarfile.open(bundle, "r:gz") as archive:
            for member in archive.getmembers():
                if not safe_member_name(member.name):
                    raise RuntimeError(f"Percorso non sicuro nel bundle: {member.name}")
                if not member.isfile():
                    raise RuntimeError(f"Tipo di membro non consentito nel bundle: {member.name}")
                source = archive.extractfile(member)
                if source is None:
                    raise RuntimeError(f"Membro non leggibile nel bundle: {member.name}")
                destination = tmp / member.name
                destination.parent.mkdir(parents=True, exist_ok=True)
                with destination.open("wb") as handle:
                    shutil.copyfileobj(source, handle)

        manifest_path = tmp / MANIFEST_NAME
        if not manifest_path.exists():
            raise RuntimeError("Manifest mancante nel bundle.")
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        if not isinstance(manifest, dict):
            raise RuntimeError("Manifest non valido.")
        files = manifest.get("files")
        if not isinstance(files, dict) or not files:
            raise RuntimeError("Manifest senza file.")

        for relative, info in files.items():
            if not safe_member_name(relative):
                raise RuntimeError(f"Percorso manifest non sicuro: {relative}")
            source = tmp / relative
            if not source.exists():
                raise RuntimeError(f"File manifest mancante nel bundle: {relative}")
            expected = str((info or {}).get("sha256", ""))
            actual = sha256_file(source)
            if not expected or actual != expected:
                raise RuntimeError(f"SHA-256 non valido per {relative}")

        # Copy only after the whole bundle has passed validation.
        for relative in files:
            source = tmp / relative
            destination = Path(relative)
            destination.parent.mkdir(parents=True, exist_ok=True)
            copy_tmp = destination.with_suffix(destination.suffix + ".restore_tmp")
            shutil.copy2(source, copy_tmp)
            copy_tmp.replace(destination)
        return manifest


def state_candidates(assets: Iterable[Asset]) -> list[Asset]:
    allowed = set(STATE_ASSETS)
    return sorted(
        (asset for asset in assets if asset.name in allowed),
        key=lambda asset: parse_iso(asset.updated_at),
        reverse=True,
    )


def command_restore(store: Store) -> int:
    store.ensure_release()
    candidates = state_candidates(store.list_assets())
    errors: list[str] = []
    if not candidates:
        atomic_json(
            STATUS_PATH,
            {
                "schema_version": SCHEMA_VERSION,
                "generated_utc": utc_now_iso(),
                "status": "EMPTY",
                "message": "Nessuno stato persistente ancora pubblicato. Avvia prima il workflow intraday.",
            },
        )
        print("Exchange storage: nessuno stato persistente disponibile.")
        return 0

    WORK_DIR.mkdir(parents=True, exist_ok=True)
    for asset in candidates:
        destination = WORK_DIR / asset.name
        try:
            store.download(asset, destination)
            manifest = validate_and_restore_bundle(destination)
            atomic_json(
                STATUS_PATH,
                {
                    "schema_version": SCHEMA_VERSION,
                    "generated_utc": utc_now_iso(),
                    "status": "RESTORED",
                    "asset": asset.name,
                    "asset_updated_at": asset.updated_at,
                    "manifest": manifest,
                    "fallback_used": asset.name != candidates[0].name,
                    "errors_before_success": errors,
                },
            )
            print(f"Exchange storage: ripristinato {asset.name} ({manifest.get('intraday', {}).get('rows', 0)} righe).")
            return 0
        except Exception as exc:
            errors.append(f"{asset.name}: {type(exc).__name__}: {exc}")

    atomic_json(
        STATUS_PATH,
        {
            "schema_version": SCHEMA_VERSION,
            "generated_utc": utc_now_iso(),
            "status": "ERROR",
            "errors": errors,
        },
    )
    raise RuntimeError("Nessuna copia dello stato exchange è valida: " + " | ".join(errors))


def choose_publish_slot(assets: Iterable[Asset]) -> tuple[str, str | None]:
    by_name = {asset.name: asset for asset in assets if asset.name in STATE_ASSETS}
    for name in STATE_ASSETS:
        if name not in by_name:
            backup = next((other for other in STATE_ASSETS if other in by_name), None)
            return name, backup
    oldest = min(by_name.values(), key=lambda asset: parse_iso(asset.updated_at))
    backup = next(name for name in STATE_ASSETS if name != oldest.name)
    return oldest.name, backup


def command_publish_state(store: Store) -> int:
    store.ensure_release()
    WORK_DIR.mkdir(parents=True, exist_ok=True)
    bundle = WORK_DIR / "exchange_state_candidate.tar.gz"
    manifest = build_state_bundle(bundle)
    assets = store.list_assets()
    slot, backup = choose_publish_slot(assets)
    uploaded = store.upload_replace(slot, bundle)
    atomic_json(
        STATUS_PATH,
        {
            "schema_version": SCHEMA_VERSION,
            "generated_utc": utc_now_iso(),
            "status": "PUBLISHED",
            "asset": uploaded.name,
            "asset_size": uploaded.size,
            "backup_asset": backup,
            "manifest": manifest,
        },
    )
    print(
        f"Exchange storage: pubblicato {uploaded.name}; backup disponibile: {backup or 'non ancora, sarà creato al prossimo run'}."
    )
    return 0


def month_from_timestamp(value: str) -> str | None:
    text = (value or "").strip()
    if len(text) < 7:
        return None
    month = text[:7]
    try:
        datetime.strptime(month, "%Y-%m")
    except ValueError:
        return None
    return month


def completed_month_rows(path: Path) -> tuple[list[str], dict[str, list[dict[str, str]]]]:
    if not path.exists():
        return [], {}
    current_month = utc_now().strftime("%Y-%m")
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        fieldnames = list(reader.fieldnames or [])
        groups: dict[str, list[dict[str, str]]] = {}
        for row in reader:
            month = month_from_timestamp(str(row.get("timestamp_utc", "")))
            if month is None or month >= current_month:
                continue
            groups.setdefault(month, []).append({field: str(row.get(field, "")) for field in fieldnames})
    return fieldnames, groups


def write_gzip_csv(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    seen: set[tuple[str, str]] = set()
    cleaned: list[dict[str, str]] = []
    for row in sorted(rows, key=lambda item: (item.get("timestamp_utc", ""), item.get("asset", ""))):
        key = (row.get("timestamp_utc", ""), row.get("asset", ""))
        if key in seen:
            continue
        seen.add(key)
        cleaned.append(row)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    with gzip.open(tmp, "wt", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(cleaned)
    tmp.replace(path)


def command_archive_completed_months(store: Store) -> int:
    fieldnames, groups = completed_month_rows(ACTIVE_CSV)
    if not fieldnames or not groups:
        print("Exchange storage: nessun mese completato da archiviare.")
        return 0
    WORK_DIR.mkdir(parents=True, exist_ok=True)
    uploaded: list[str] = []
    skipped: list[str] = []
    stores_by_year: dict[str, Store] = {}
    existing_by_year: dict[str, set[str]] = {}
    for month, rows in sorted(groups.items()):
        year = month[:4]
        archive_store = stores_by_year.get(year)
        if archive_store is None:
            archive_store = store.scoped(f"exchange-data-archive-{year}")
            archive_store.ensure_release()
            stores_by_year[year] = archive_store
            existing_by_year[year] = {asset.name for asset in archive_store.list_assets()}
        name = f"{ARCHIVE_PREFIX}{month}{ARCHIVE_SUFFIX}"
        if name in existing_by_year[year]:
            skipped.append(name)
            continue
        local = WORK_DIR / name
        write_gzip_csv(local, fieldnames, rows)
        archive_store.upload_if_missing(name, local)
        uploaded.append(name)
        existing_by_year[year].add(name)
    print(
        "Exchange storage: archivi mensili nuovi: "
        + (", ".join(uploaded) if uploaded else "nessuno")
        + f"; già presenti: {len(skipped)}."
    )
    return 0


def command_audit(store: Store) -> int:
    store.ensure_release()
    assets = store.list_assets()
    states = state_candidates(assets)
    local = csv_stats(ACTIVE_CSV)
    last_timestamp = local.get("last_timestamp_utc")
    age_hours: float | None = None
    if last_timestamp:
        age_hours = max(0.0, (utc_now() - parse_iso(str(last_timestamp))).total_seconds() / 3600.0)
    healthy = bool(states) and local.get("rows", 0) > 0 and age_hours is not None and age_hours <= 3.0
    status = {
        "schema_version": SCHEMA_VERSION,
        "generated_utc": utc_now_iso(),
        "status": "OK" if healthy else "WARN",
        "asset": states[0].name if states else None,
        "state_assets": [asset.__dict__ for asset in states],
        "archive_policy": "one yearly release, one immutable asset per completed UTC month",
        "local_intraday": local,
        "latest_sample_age_hours": age_hours,
        "freshness_limit_hours": 3.0,
    }
    atomic_json(STATUS_PATH, status)
    age_text = "n/a" if age_hours is None else f"{age_hours:.2f}h"
    print(
        f"Exchange storage audit: {len(states)} copie stato, "
        f"{local['rows']} righe locali, età ultimo campione {age_text}, stato {status['status']}."
    )
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Persistent exchange data storage")
    parser.add_argument(
        "command",
        choices=("restore", "publish-state", "archive-completed-months", "audit"),
    )
    parser.add_argument("--release-tag", default="", help="Override release tag")
    parser.add_argument("--local-dir", default="", help="Offline filesystem backend")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    store = make_store(args)
    commands = {
        "restore": command_restore,
        "publish-state": command_publish_state,
        "archive-completed-months": command_archive_completed_months,
        "audit": command_audit,
    }
    commands[args.command](store)


if __name__ == "__main__":
    main()
