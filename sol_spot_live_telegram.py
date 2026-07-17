# -*- coding: utf-8 -*-
"""Telegram notifications for the guarded SOL live bot."""

from __future__ import annotations

import hashlib
import json
import os
from datetime import datetime, timezone
from decimal import Decimal
from pathlib import Path
from typing import Any

import requests

STATE_PATH = Path("reports/sol_spot_live_telegram_state.json")


def _credentials() -> tuple[str, str]:
    token = os.getenv("TELEGRAM_BOT_TOKEN", "").strip()
    chat_id = os.getenv("TELEGRAM_CHAT_ID", "").strip()
    if not token or not chat_id:
        raise RuntimeError("TELEGRAM_BOT_TOKEN o TELEGRAM_CHAT_ID mancanti.")
    return token, chat_id


def _text(value: Any) -> str:
    if isinstance(value, Decimal):
        return format(value, "f")
    return str(value)


def _send(text: str) -> None:
    token, chat_id = _credentials()
    response = requests.post(
        f"https://api.telegram.org/bot{token}/sendMessage",
        json={
            "chat_id": chat_id,
            "text": text[:4000],
            "disable_web_page_preview": True,
        },
        timeout=20,
    )
    payload = response.json()
    if response.status_code >= 400 or not payload.get("ok"):
        raise RuntimeError(f"Telegram ha rifiutato il messaggio: {payload}")


def send_alert(title: str, detail: str) -> None:
    _send(f"{title}\n\n{detail}")


def send_test() -> None:
    _send("✅ Test Telegram bot SOL live riuscito.\nNessun ordine è stato eseguito.")


def send_order_event(
    *,
    config: dict[str, Any],
    account: dict[str, Any],
    managed: dict[str, Any],
    strategy: dict[str, Any],
    risk: dict[str, Any],
    state: dict[str, Any],
    plan: dict[str, Any],
    reconciled: dict[str, Any] | None,
    order_id: str,
) -> None:
    lines = [
        "💰 ORDINE REALE SOL ESEGUITO",
        "",
        f"Azione: {plan.get('action')}",
        f"Motivo: {plan.get('reason')}",
        f"Valore pianificato: {_text(plan.get('order_value_usdt', 0))} USDT",
        f"Prezzo SOL: {_text(account.get('price', 0))} USDT",
        f"Regime: {strategy.get('regime')}",
        f"Peso SOL: {float(managed.get('current_sol_weight', 0))*100:.2f}%",
        f"Order ID: {order_id or 'non restituito'}",
        f"Riconciliazione: {'OK' if reconciled else 'PENDING - NON RIPETERE'}",
    ]
    _send("\n".join(lines))


def _load_state() -> dict[str, Any]:
    if not STATE_PATH.exists():
        return {}
    try:
        return json.loads(STATE_PATH.read_text(encoding="utf-8"))
    except Exception:
        return {}


def send_status_digest(
    *,
    config: dict[str, Any],
    account: dict[str, Any],
    managed: dict[str, Any],
    strategy: dict[str, Any],
    risk: dict[str, Any],
    state: dict[str, Any],
    plan: dict[str, Any],
    force: bool = False,
) -> bool:
    message = "\n".join(
        [
            "🤖 SOL LIVE — STATO",
            "",
            f"Prezzo: {_text(account.get('price', 0))} USDT",
            f"USDT disponibili: {_text(account.get('usdt', {}).get('available', 0))}",
            f"SOL disponibili: {_text(account.get('sol', {}).get('available', 0))}",
            f"Equity gestita: {_text(managed.get('managed_equity', 0))} USDT",
            f"Regime: {strategy.get('regime')}",
            f"Piano: {plan.get('action')} — {plan.get('reason')}",
            f"Perdita giorno: {_text(risk.get('daily_loss_usdt', 0))} USDT",
            f"Perdita totale: {_text(risk.get('total_loss_usdt', 0))} USDT",
        ]
    )
    digest = hashlib.sha256(message.encode()).hexdigest()
    saved = _load_state()
    now = datetime.now(timezone.utc)
    last = saved.get("last_sent_utc")
    interval = float(config.get("telegram_notifications", {}).get("status_interval_hours", 4))
    due = True
    if last:
        try:
            previous = datetime.fromisoformat(last)
            due = (now - previous).total_seconds() >= interval * 3600
        except Exception:
            due = True
    if not force and (not due or saved.get("last_digest") == digest):
        return False
    _send(message)
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    STATE_PATH.write_text(
        json.dumps(
            {"last_sent_utc": now.isoformat(), "last_digest": digest},
            indent=2,
        ),
        encoding="utf-8",
    )
    return True
