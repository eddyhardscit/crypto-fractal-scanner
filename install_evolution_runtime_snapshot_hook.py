#!/usr/bin/env python3
"""Install the automatic Evolution runtime snapshot hook safely.

Default mode is DRY RUN. Add --apply to write systemd files.

The installation creates:
- /etc/systemd/system/crypto-evolution-runtime-snapshot.service
- /etc/systemd/system/crypto-paper-main.service.d/evolution-runtime-snapshot.conf
- reports/evolution_runtime_hook_install_result.json

Behavior:
- after crypto-paper-main.service completes successfully, systemd starts the
  separate read-only snapshot service;
- the Paper service is not restarted or manually started by this installer;
- a non-blocking flock prevents overlapping snapshot executions;
- the live bot and operational Paper files are not modified.

The snapshot service runs:
  /root/crypto-fractal-scanner/.venv/bin/python
  evolution_runtime_snapshot_remote_v3.py --repo /root/crypto-fractal-scanner
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


REPO = Path("/root/crypto-fractal-scanner")
PYTHON = REPO / ".venv/bin/python"
SNAPSHOT_SCRIPT = REPO / "evolution_runtime_snapshot_remote_v3.py"

MAIN_UNIT = "crypto-paper-main.service"
SNAPSHOT_UNIT = "crypto-evolution-runtime-snapshot.service"

SERVICE_PATH = Path("/etc/systemd/system") / SNAPSHOT_UNIT
DROPIN_DIR = Path("/etc/systemd/system/crypto-paper-main.service.d")
DROPIN_PATH = DROPIN_DIR / "evolution-runtime-snapshot.conf"

REPORT_PATH = REPO / "reports/evolution_runtime_hook_install_result.json"

SERVICE_CONTENT = f"""\
[Unit]
Description=Evolution Runtime Snapshot V3 (read-only)
Wants=network-online.target
After=network-online.target
ConditionPathExists={PYTHON}
ConditionPathExists={SNAPSHOT_SCRIPT}

[Service]
Type=oneshot
User=root
WorkingDirectory={REPO}
Environment=PYTHONUNBUFFERED=1
ExecStart=/usr/bin/flock -n /run/crypto-evolution-runtime-snapshot.lock {PYTHON} {SNAPSHOT_SCRIPT} --repo {REPO}
TimeoutStartSec=240
Nice=10
IOSchedulingClass=best-effort
IOSchedulingPriority=7
NoNewPrivileges=true
PrivateTmp=true
UMask=0077
SyslogIdentifier=crypto-evolution-runtime-snapshot
"""

DROPIN_CONTENT = f"""\
[Unit]
OnSuccess={SNAPSHOT_UNIT}
"""


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def timestamp_slug() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def run(
    args: list[str],
    *,
    check: bool = False,
    timeout: int = 30,
) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        args,
        capture_output=True,
        text=True,
        check=check,
        timeout=timeout,
    )


def atomic_write(path: Path, content: str, mode: int = 0o644) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(
        prefix=f".{path.name}.",
        suffix=".tmp",
        dir=str(path.parent),
        text=True,
    )
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            handle.write(content)
            if not content.endswith("\n"):
                handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        os.chmod(temporary, mode)
        os.replace(temporary, path)
    except Exception:
        try:
            os.unlink(temporary)
        except OSError:
            pass
        raise


def atomic_json(path: Path, value: dict[str, Any]) -> None:
    atomic_write(
        path,
        json.dumps(
            value,
            indent=2,
            ensure_ascii=False,
            sort_keys=True,
        )
        + "\n",
        0o600,
    )


def file_state(path: Path, expected: str) -> str:
    if not path.exists():
        return "CREATE"
    try:
        current = path.read_text(encoding="utf-8")
    except OSError:
        return "UNREADABLE"
    return "UNCHANGED" if current == expected else "UPDATE"


def unit_exists(unit: str) -> bool:
    result = run(
        ["systemctl", "show", unit, "--property=LoadState", "--value"]
    )
    return result.returncode == 0 and result.stdout.strip() not in {
        "",
        "not-found",
    }


def python_syntax_ok() -> tuple[bool, str]:
    result = run(
        [
            str(PYTHON),
            "-m",
            "py_compile",
            str(SNAPSHOT_SCRIPT),
        ],
        timeout=60,
    )
    detail = (result.stderr or result.stdout).strip()
    return result.returncode == 0, detail


def backup_files(paths: list[Path]) -> Path:
    backup_dir = (
        REPO
        / "data/evolution/backups"
        / f"runtime_snapshot_hook_{timestamp_slug()}"
    )
    backup_dir.mkdir(parents=True, exist_ok=False)

    manifest: list[dict[str, Any]] = []
    for path in paths:
        entry: dict[str, Any] = {
            "path": str(path),
            "existed": path.exists(),
        }
        if path.exists():
            relative = str(path).lstrip("/")
            destination = backup_dir / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(path, destination)
            entry["backup_path"] = str(destination)
        manifest.append(entry)

    atomic_json(
        backup_dir / "manifest.json",
        {
            "created_at": utc_now_iso(),
            "files": manifest,
        },
    )
    return backup_dir


def restore_backup(backup_dir: Path, paths: list[Path]) -> None:
    manifest_path = backup_dir / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    by_path = {
        item["path"]: item
        for item in manifest.get("files", [])
        if isinstance(item, dict) and item.get("path")
    }

    for path in paths:
        item = by_path.get(str(path), {})
        if item.get("existed"):
            source = Path(item["backup_path"])
            path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, path)
        elif path.exists():
            path.unlink()


def systemd_verify() -> tuple[bool, str]:
    # Verify the standalone unit. The drop-in is validated by daemon-reload
    # and by reading the resolved OnSuccess property.
    result = run(
        ["systemd-analyze", "verify", str(SERVICE_PATH)],
        timeout=60,
    )
    detail = "\n".join(
        value.strip()
        for value in (result.stdout, result.stderr)
        if value.strip()
    )
    return result.returncode == 0, detail


def resolved_hook() -> str:
    result = run(
        [
            "systemctl",
            "show",
            MAIN_UNIT,
            "--property=OnSuccess",
            "--value",
        ]
    )
    return result.stdout.strip()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Write the systemd unit and drop-in. Default is dry run.",
    )
    args = parser.parse_args()

    errors: list[str] = []
    warnings: list[str] = []

    if os.geteuid() != 0:
        errors.append("The installer must run as root.")

    if not REPO.is_dir():
        errors.append(f"Repository not found: {REPO}")
    if not PYTHON.exists():
        errors.append(f"Project Python not found: {PYTHON}")
    if not SNAPSHOT_SCRIPT.exists():
        errors.append(f"Snapshot V3 not found: {SNAPSHOT_SCRIPT}")
    if not Path("/usr/bin/flock").exists():
        errors.append("/usr/bin/flock not found.")
    if not unit_exists(MAIN_UNIT):
        errors.append(f"Main Paper unit not found: {MAIN_UNIT}")

    syntax_ok = False
    syntax_detail = ""
    if not errors:
        syntax_ok, syntax_detail = python_syntax_ok()
        if not syntax_ok:
            errors.append(
                "Snapshot V3 syntax check failed"
                + (f": {syntax_detail}" if syntax_detail else ".")
            )

    service_action = file_state(SERVICE_PATH, SERVICE_CONTENT)
    dropin_action = file_state(DROPIN_PATH, DROPIN_CONTENT)

    plan = {
        "service_path": str(SERVICE_PATH),
        "service_action": service_action,
        "dropin_path": str(DROPIN_PATH),
        "dropin_action": dropin_action,
        "main_unit": MAIN_UNIT,
        "snapshot_unit": SNAPSHOT_UNIT,
        "snapshot_script": str(SNAPSHOT_SCRIPT),
        "project_python": str(PYTHON),
        "trigger": f"OnSuccess={SNAPSHOT_UNIT}",
        "services_to_restart": [],
        "services_to_start": [],
    }

    result: dict[str, Any] = {
        "schema_version": 1,
        "generated_at": utc_now_iso(),
        "mode": "APPLY" if args.apply else "DRY_RUN",
        "plan": plan,
        "preflight": {
            "root": os.geteuid() == 0,
            "repository_exists": REPO.is_dir(),
            "python_exists": PYTHON.exists(),
            "snapshot_script_exists": SNAPSHOT_SCRIPT.exists(),
            "snapshot_syntax_ok": syntax_ok,
            "main_unit_exists": unit_exists(MAIN_UNIT),
            "flock_exists": Path("/usr/bin/flock").exists(),
        },
        "errors": errors,
        "warnings": warnings,
        "applied": False,
        "backup_dir": None,
        "resolved_on_success": None,
        "safety": {
            "paper_service_restarted": False,
            "paper_service_started": False,
            "paper_timer_restarted": False,
            "snapshot_service_started": False,
            "trading_files_changed": False,
            "orders_sent": False,
        },
    }

    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)

    print("=== EVOLUTION RUNTIME HOOK INSTALLER ===")
    print(f"Modalità: {'APPLY' if args.apply else 'DRY RUN'}")
    print(f"Unit snapshot: {service_action}")
    print(f"Drop-in Paper OnSuccess: {dropin_action}")
    print(f"Script V3: {'OK' if syntax_ok else 'ERRORE'}")
    print(f"Servizio Paper trovato: {'SI' if unit_exists(MAIN_UNIT) else 'NO'}")
    print("Servizi da riavviare: nessuno")
    print("Servizi da avviare durante installazione: nessuno")

    if errors:
        atomic_json(REPORT_PATH, result)
        print("PRECHECK FALLITO.")
        for error in errors:
            print(f"- {error}")
        print(f"Report: {REPORT_PATH}")
        return 2

    if not args.apply:
        atomic_json(REPORT_PATH, result)
        print("DRY RUN OK: nessun file systemd è stato modificato.")
        print(f"Report: {REPORT_PATH}")
        print("Per installare, rieseguire aggiungendo --apply.")
        return 0

    managed_paths = [SERVICE_PATH, DROPIN_PATH]
    backup_dir = backup_files(managed_paths)
    result["backup_dir"] = str(backup_dir)

    try:
        atomic_write(SERVICE_PATH, SERVICE_CONTENT, 0o644)
        atomic_write(DROPIN_PATH, DROPIN_CONTENT, 0o644)

        daemon_reload = run(
            ["systemctl", "daemon-reload"],
            timeout=60,
        )
        if daemon_reload.returncode != 0:
            raise RuntimeError(
                "systemctl daemon-reload failed: "
                + (daemon_reload.stderr or daemon_reload.stdout).strip()
            )

        verify_ok, verify_detail = systemd_verify()
        if not verify_ok:
            raise RuntimeError(
                "systemd unit verification failed"
                + (f": {verify_detail}" if verify_detail else "")
            )

        on_success = resolved_hook()
        if SNAPSHOT_UNIT not in on_success.split():
            raise RuntimeError(
                f"Resolved OnSuccess does not contain {SNAPSHOT_UNIT}: "
                f"{on_success!r}"
            )

        result["applied"] = True
        result["resolved_on_success"] = on_success
        result["verification"] = {
            "systemd_analyze_verify": True,
            "resolved_on_success_contains_snapshot_unit": True,
        }
        atomic_json(REPORT_PATH, result)

    except Exception as exc:
        restore_backup(backup_dir, managed_paths)
        run(["systemctl", "daemon-reload"], timeout=60)
        result["errors"].append(str(exc))
        result["rolled_back"] = True
        atomic_json(REPORT_PATH, result)
        print("INSTALLAZIONE FALLITA: rollback eseguito.")
        print(f"- {exc}")
        print(f"Backup: {backup_dir}")
        print(f"Report: {REPORT_PATH}")
        return 3

    print("INSTALLAZIONE COMPLETATA.")
    print(f"OnSuccess risolto: {result['resolved_on_success']}")
    print(f"Backup: {backup_dir}")
    print(f"Report: {REPORT_PATH}")
    print("Il servizio Paper NON è stato riavviato.")
    print("Il timer Paper NON è stato riavviato.")
    print("Lo snapshot NON è stato avviato dall'installer.")
    print(
        "Il collegamento entrerà in funzione al prossimo completamento "
        "riuscito di crypto-paper-main.service."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
