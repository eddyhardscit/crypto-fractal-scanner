# -*- coding: utf-8 -*-
"""Send each new daily scanner report to Telegram exactly once."""

from __future__ import annotations

import hashlib
import os
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import requests

LATEST_REPORT = Path("reports/latest_report.md")
DECISION_REPORT = Path("reports/decision_report.md")


def _credentials() -> tuple[str, str]:
    return (
        os.getenv("TELEGRAM_BOT_TOKEN", "").strip(),
        os.getenv("TELEGRAM_CHAT_ID", "").strip(),
    )


def _decision_digest() -> str | None:
    if not DECISION_REPORT.exists():
        return None
    return hashlib.sha256(DECISION_REPORT.read_bytes()).hexdigest()


def _decision_text() -> str:
    source = DECISION_REPORT if DECISION_REPORT.exists() else LATEST_REPORT
    if not source.exists():
        return ""
    text = source.read_text(encoding="utf-8", errors="replace")
    marker = re.search(
        r"<!-- DECISION_REPORT_START -->(.*?)<!-- DECISION_REPORT_END -->",
        text,
        flags=re.DOTALL,
    )
    if marker:
        text = marker.group(1)

    generated = next((line.strip() for line in text.splitlines() if line.strip().startswith("Generato:")), "")
    rows: list[str] = []
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped.startswith("|") or stripped.startswith("| ---") or stripped.startswith("| Asset |"):
            continue
        cells = [cell.strip() for cell in stripped.strip("|").split("|")]
        if len(cells) < 9:
            continue
        asset, global_score, direction, spot, long_action, short_action, _, _, risk = cells[:9]
        if asset.upper() not in {"BTC", "SOL", "DOGE", "HYPE", "ETH"}:
            continue
        rows.extend(
            [
                f"{asset} — {direction} (Global {global_score})",
                f"Spot: {spot}",
                f"Leva: long {long_action} · short {short_action}",
                f"Rischio: {risk}",
                "",
            ]
        )
    body = "\n".join(rows).strip()
    if not body:
        plain = [line.strip("# ") for line in text.splitlines() if line.strip()][:12]
        body = "\n".join(plain)
    return "\n".join(part for part in (generated, body) if part)[:3400]


def _send_message(token: str, chat_id: str, text: str) -> None:
    response = requests.post(
        f"https://api.telegram.org/bot{token}/sendMessage",
        json={"chat_id": chat_id, "text": text, "disable_web_page_preview": True},
        timeout=30,
    )
    response.raise_for_status()


def _send_document(token: str, chat_id: str, path: Path, caption: str) -> None:
    with path.open("rb") as handle:
        response = requests.post(
            f"https://api.telegram.org/bot{token}/sendDocument",
            data={"chat_id": chat_id, "caption": caption[:1024]},
            files={"document": (path.name, handle, "text/markdown")},
            timeout=60,
        )
    response.raise_for_status()


def send_if_changed(
    state: dict[str, Any],
    config: dict[str, Any],
    now: datetime | None = None,
) -> dict[str, Any]:
    settings = dict(config.get("notifications", {}))
    result: dict[str, Any] = {"sent": False, "configured": False, "changed": False}
    if not settings.get("send_daily_scanner_report", True):
        result["reason"] = "disabled by configuration"
        return result

    token, chat_id = _credentials()
    result["configured"] = bool(token and chat_id)
    if not token or not chat_id:
        result["reason"] = "Telegram secrets missing"
        return result
    if not LATEST_REPORT.exists() or not DECISION_REPORT.exists():
        result["reason"] = "scanner report unavailable"
        return result

    digest = _decision_digest()
    previous = state.get("notifications", {}).get("telegram_last_scanner_digest")
    result["changed"] = bool(digest and digest != previous)
    if not result["changed"]:
        return result

    message = "📡 SCANNER CRYPTO GIORNALIERO\n\n"
    message += _decision_text() or "Report aggiornato; il file completo è allegato."
    _send_message(token, chat_id, message)
    _send_document(
        token,
        chat_id,
        LATEST_REPORT,
        "Report completo: scanner, confluenze, rischio e paper trading KuCoin.",
    )
    current = (now or datetime.now(timezone.utc)).astimezone(timezone.utc)
    notifications = state.setdefault("notifications", {})
    notifications["telegram_last_scanner_digest"] = digest
    notifications["telegram_last_scanner_sent_utc"] = current.isoformat(timespec="seconds")
    result["sent"] = True
    return result
