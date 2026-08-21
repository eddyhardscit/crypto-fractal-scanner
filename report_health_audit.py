# -*- coding: utf-8 -*-
"""Automatic report-health audit with Telegram change alerts."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import re
import subprocess
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

import requests


CONFIG_PATH = Path("report_health_config.json")
REPORTS_DIR = Path("reports")
AUDIT_MD = REPORTS_DIR / "report_health_audit.md"
AUDIT_JSON = REPORTS_DIR / "report_health_audit.json"
STATE_PATH = REPORTS_DIR / "report_health_state.json"


def now_utc() -> datetime:
    return datetime.now(timezone.utc)


def iso(value: datetime | None = None) -> str:
    return (value or now_utc()).astimezone(timezone.utc).isoformat(
        timespec="seconds"
    )


def parse_time(value: Any) -> datetime | None:
    if value is None:
        return None
    text = str(value).strip()
    if not text:
        return None
    text = text.replace(" UTC", "+00:00").replace("Z", "+00:00")
    for candidate in (text, text.replace(" ", "T", 1)):
        try:
            parsed = datetime.fromisoformat(candidate)
            if parsed.tzinfo is None:
                parsed = parsed.replace(tzinfo=timezone.utc)
            return parsed.astimezone(timezone.utc)
        except Exception:
            pass
    for fmt in ("%Y-%m-%d %H:%M", "%Y-%m-%d"):
        try:
            return datetime.strptime(str(value).strip(), fmt).replace(
                tzinfo=timezone.utc
            )
        except Exception:
            pass
    return None


def load_json(path: Path, default: Any) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return default


def save_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_suffix(path.suffix + ".tmp")
    temp.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    temp.replace(path)


def changed_files() -> set[str]:
    try:
        result = subprocess.run(
            ["git", "diff", "--name-only", "HEAD", "--", "reports/"],
            capture_output=True,
            text=True,
            check=False,
        )
        return {
            line.strip()
            for line in result.stdout.splitlines()
            if line.strip()
        }
    except Exception:
        return set()


def find_timestamp(path: Path) -> datetime | None:
    try:
        if path.suffix.lower() == ".json":
            payload = load_json(path, {})
            keys = (
                "generated_at_utc",
                "generated_utc",
                "generated_at",
                "updated_utc",
                "timestamp_utc",
            )
            if isinstance(payload, dict):
                for key in keys:
                    parsed = parse_time(payload.get(key))
                    if parsed:
                        return parsed
            return None

        text = path.read_text(encoding="utf-8", errors="replace")
        patterns = (
            r"(?im)^\s*Generato:\s*\**([^*\n]+)",
            r"(?im)^\s*Generated:\s*\**([^*\n]+)",
        )
        for pattern in patterns:
            match = re.search(pattern, text)
            if match:
                parsed = parse_time(match.group(1).strip())
                if parsed:
                    return parsed
    except Exception:
        return None
    return None


def row(
    label: str,
    path: str,
    level: str,
    status: str,
    detail: str,
) -> dict[str, str]:
    return {
        "label": label,
        "path": path,
        "level": level,
        "status": status,
        "detail": detail,
    }


def check_critical(
    item: dict[str, Any],
    current: datetime,
    changed: set[str],
) -> dict[str, str]:
    raw = str(item["path"])
    path = Path(raw)
    label = str(item.get("label", raw))
    limit = float(item.get("max_age_hours", 36))

    if not path.exists():
        return row(label, raw, "CRITICAL", "MISSING", "File mancante.")
    if not path.is_file() or path.stat().st_size == 0:
        return row(label, raw, "CRITICAL", "EMPTY", "File vuoto.")

    timestamp = find_timestamp(path)
    if timestamp is None:
        if raw in changed:
            return row(
                label,
                raw,
                "OK",
                "CHANGED",
                "Rigenerato; timestamp interno non rilevato.",
            )
        return row(
            label,
            raw,
            "WARNING",
            "NO_TIMESTAMP",
            "File invariato e timestamp interno non rilevato.",
        )

    age = max(0.0, (current - timestamp).total_seconds() / 3600.0)
    if age > limit:
        return row(
            label,
            raw,
            "CRITICAL",
            "STALE",
            f"Ultimo dato vecchio di {age:.1f} ore; limite {limit:.0f}.",
        )
    suffix = (
        "rigenerato in questo ciclo"
        if raw in changed
        else "dato interno ancora recente"
    )
    return row(
        label,
        raw,
        "OK",
        "OK",
        f"Ultimo dato {age:.1f} ore fa; {suffix}.",
    )


def check_text(item: dict[str, Any]) -> dict[str, str]:
    raw = str(item["path"])
    path = Path(raw)
    label = str(item.get("label", raw))
    level = str(item.get("level", "WARNING")).upper()
    if not path.exists():
        return row(label, raw, level, "MISSING", "File osservato mancante.")
    text = path.read_text(encoding="utf-8", errors="replace")
    for phrase in item.get("forbidden_text", []):
        if str(phrase).casefold() in text.casefold():
            return row(
                label,
                raw,
                level,
                "CONTENT_WARNING",
                f"Contiene ancora: “{phrase}”.",
            )
    return row(label, raw, "OK", "OK", "Nessun errore noto nel contenuto.")


def check_csv(item: dict[str, Any], current: datetime) -> dict[str, str]:
    raw = str(item["path"])
    path = Path(raw)
    label = str(item.get("label", raw))
    level = str(item.get("level", "WARNING")).upper()
    column = str(item["column"])
    limit = float(item.get("max_age_hours", 72))

    if not path.exists():
        return row(label, raw, level, "MISSING", "CSV osservato mancante.")

    latest = None
    try:
        with path.open(
            "r",
            encoding="utf-8",
            errors="replace",
            newline="",
        ) as handle:
            for record in csv.DictReader(handle):
                parsed = parse_time(record.get(column))
                if parsed and (latest is None or parsed > latest):
                    latest = parsed
    except Exception as exc:
        return row(label, raw, level, "CSV_ERROR", f"CSV non leggibile: {exc}")

    if latest is None:
        return row(
            label,
            raw,
            level,
            "NO_DATE",
            f"Nessuna data leggibile nella colonna {column}.",
        )
    age = max(0.0, (current - latest).total_seconds() / 3600.0)
    if age > limit:
        return row(
            label,
            raw,
            level,
            "STALE",
            f"Ultima riga utile vecchia di {age:.1f} ore; limite {limit:.0f}.",
        )
    return row(label, raw, "OK", "OK", f"Ultima riga utile {age:.1f} ore fa.")


def anomalies(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    return [
        item
        for item in rows
        if item["level"] in {"WARNING", "CRITICAL"}
        and item["status"] != "OK"
    ]


def health_status(
    rows: list[dict[str, str]],
    items: list[dict[str, str]],
    current: datetime,
    max_age_hours: float,
) -> dict[str, Any]:
    """Describe this report audit without claiming system-wide health.

    The audit verifies report artifacts only.  It does not observe the complete
    runtime, so ``operationally_proven`` must remain false unless a separate,
    authoritative operational gate supplies that evidence.
    """
    valid_until = current + timedelta(hours=max_age_hours)
    return {
        "generated_at": iso(current),
        "data_freshness": {
            "state": "FRESH",
            "max_age_hours": max_age_hours,
            "valid_until": iso(valid_until),
        },
        "component_state": "ATTENTION" if items else "OK",
        "operationally_proven": False,
        "stale": False,
        "status": "ATTENTION" if items else "REPORTS_HEALTHY_UNVERIFIED",
        "checks_total": len(rows),
    }


def persisted_health_status(
    payload: dict[str, Any],
    current: datetime,
    default_max_age_hours: float = 36.0,
) -> dict[str, Any]:
    """Return the effective status of a stored audit at ``current``.

    This is deliberately fail-closed for old schema payloads which merely say
    ``status=OK``: a missing or expired generation timestamp is always STALE.
    """
    result = dict(payload)
    generated = parse_time(payload.get("generated_at") or payload.get("generated_utc"))
    freshness = payload.get("data_freshness")
    if not isinstance(freshness, dict):
        freshness = {}
    try:
        max_age_hours = float(freshness.get("max_age_hours", default_max_age_hours))
    except (TypeError, ValueError):
        max_age_hours = default_max_age_hours
    valid_until = parse_time(freshness.get("valid_until"))
    if valid_until is None and generated is not None:
        valid_until = generated + timedelta(hours=max_age_hours)
    stale = generated is None or valid_until is None or current > valid_until
    result["generated_at"] = iso(generated) if generated else None
    result["data_freshness"] = {
        "state": "STALE" if stale else "FRESH",
        "max_age_hours": max_age_hours,
        "valid_until": iso(valid_until) if valid_until else None,
    }
    result["stale"] = stale
    if stale:
        result["status"] = "STALE"
        result["operationally_proven"] = False
    else:
        result.setdefault("operationally_proven", False)
        if str(result.get("status", "")).upper() == "OK":
            result["status"] = "REPORTS_HEALTHY_UNVERIFIED"
    result.setdefault("component_state", "UNKNOWN")
    return result


def signature(items: list[dict[str, str]]) -> str:
    raw = json.dumps(
        sorted(items, key=lambda item: item["path"]),
        ensure_ascii=False,
        sort_keys=True,
    )
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


def send_telegram(text: str) -> bool:
    token = os.getenv("TELEGRAM_BOT_TOKEN", "").strip()
    chat_id = os.getenv("TELEGRAM_CHAT_ID", "").strip()
    if not token or not chat_id:
        return False
    response = requests.post(
        f"https://api.telegram.org/bot{token}/sendMessage",
        json={
            "chat_id": chat_id,
            "text": text,
            "disable_web_page_preview": True,
        },
        timeout=20,
    )
    response.raise_for_status()
    return True


def anomaly_message(items: list[dict[str, str]]) -> str:
    critical = sum(item["level"] == "CRITICAL" for item in items)
    warning = sum(item["level"] == "WARNING" for item in items)
    lines = [
        "🛠 CONTROLLO AUTOMATICO REPORT",
        "",
        f"🔴 Critici: {critical} · 🟡 Da controllare: {warning}",
        "",
    ]
    for item in items[:12]:
        icon = "🔴" if item["level"] == "CRITICAL" else "🟡"
        lines.extend(
            [
                f"{icon} {item['label']}",
                f"File: {item['path']}",
                f"Motivo: {item['detail']}",
                "",
            ]
        )
    lines.append("L’audit non ha modificato o cancellato questi file.")
    return "\n".join(lines)


def recovery_message(old_items: list[dict[str, str]]) -> str:
    paths = sorted({item["path"] for item in old_items})
    return (
        "✅ CONTROLLO REPORT — PROBLEMI RISOLTI\n\n"
        + "\n".join(f"• {path}" for path in paths)
        + "\n\nTutti i controlli configurati risultano ora regolari."
    )


def summary_message(
    rows: list[dict[str, str]],
    items: list[dict[str, str]],
) -> str:
    return (
        "🛠 CONTROLLO AUTOMATICO REPORT — RIEPILOGO\n\n"
        f"🟢 Regolari: {sum(row['level'] == 'OK' for row in rows)}\n"
        f"🟡 Da controllare: {sum(row['level'] == 'WARNING' for row in items)}\n"
        f"🔴 Critici: {sum(row['level'] == 'CRITICAL' for row in items)}\n\n"
        "Nuovi messaggi arriveranno solo quando compare o cambia un "
        "problema, quando viene risolto, oppure come promemoria settimanale."
    )


def write_audit(
    rows: list[dict[str, str]],
    items: list[dict[str, str]],
    current: datetime,
    telegram_sent: bool,
    max_age_hours: float,
) -> None:
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Controllo automatico salute report",
        "",
        f"Generato: {current.strftime('%Y-%m-%d %H:%M UTC')}",
        "",
        f"Anomalie attive: **{len(items)}**",
        "",
        "| Livello | Modulo | File | Stato | Dettaglio |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in rows:
        icon = {"OK": "🟢", "WARNING": "🟡", "CRITICAL": "🔴"}[
            item["level"]
        ]
        detail = item["detail"].replace("|", "/")
        lines.append(
            f"| {icon} {item['level']} | {item['label']} | "
            f"`{item['path']}` | {item['status']} | {detail} |"
        )
    AUDIT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")
    payload = health_status(rows, items, current, max_age_hours)
    payload.update(
        {
            "generated_utc": iso(current),
            "producer_root": str(Path.cwd().resolve()),
            "telegram_sent": telegram_sent,
            "checks": rows,
            "active_anomalies": items,
        }
    )
    save_json(AUDIT_JSON, payload)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument(
        "--status-json",
        type=Path,
        help="Valuta in sola lettura la freshness di un audit persistito.",
    )
    args = parser.parse_args()

    if args.self_test:
        assert parse_time("2026-07-13 06:28 UTC")
        assert parse_time("2026-07-13T06:28:00Z")
        assert len(signature([row("x", "x", "WARNING", "TEST", "x")])) == 64
        print("Report health audit self-test OK")
        return 0

    if args.status_json:
        payload = load_json(args.status_json, {})
        print(
            json.dumps(
                persisted_health_status(payload, now_utc()),
                ensure_ascii=False,
                sort_keys=True,
            )
        )
        return 0

    config = load_json(CONFIG_PATH, {})
    current = now_utc()
    audit_max_age_hours = float(config.get("audit_max_age_hours", 36))
    changed = changed_files()
    rows: list[dict[str, str]] = []

    for item in config.get("critical_reports", []):
        rows.append(check_critical(item, current, changed))
    for item in config.get("watch_checks", []):
        check_type = item.get("type")
        if check_type == "forbidden_text":
            rows.append(check_text(item))
        elif check_type == "csv_latest_timestamp":
            rows.append(check_csv(item, current))

    items = anomalies(rows)
    current_signature = signature(items)
    state = load_json(
        STATE_PATH,
        {
            "active_signature": "",
            "active_anomalies": [],
            "last_alert_utc": "",
        },
    )
    old_signature = str(state.get("active_signature", ""))
    old_items = list(state.get("active_anomalies", []))
    last_alert = parse_time(state.get("last_alert_utc"))
    repeat_hours = float(config.get("repeat_alert_hours", 168))
    manual = os.getenv("GITHUB_EVENT_NAME", "") == "workflow_dispatch"

    recovery = bool(old_items and not items)
    new_or_changed = bool(items and current_signature != old_signature)
    reminder = bool(
        items
        and last_alert
        and current - last_alert >= timedelta(hours=repeat_hours)
    )

    telegram_sent = False
    if recovery:
        telegram_sent = send_telegram(recovery_message(old_items))
    elif new_or_changed or reminder:
        telegram_sent = send_telegram(anomaly_message(items))
    elif manual:
        telegram_sent = send_telegram(summary_message(rows, items))

    state["active_signature"] = current_signature
    state["active_anomalies"] = items
    state["last_run_utc"] = iso(current)
    if telegram_sent:
        state["last_alert_utc"] = iso(current)
    save_json(STATE_PATH, state)
    write_audit(rows, items, current, telegram_sent, audit_max_age_hours)

    print(
        json.dumps(
            {
                "checks": len(rows),
                "anomalies": len(items),
                "telegram_sent": telegram_sent,
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
