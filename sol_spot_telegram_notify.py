# -*- coding: utf-8 -*-
"""Telegram notifier for the separate SOL Spot Adaptive paper portfolio."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
from typing import Any

import requests

STATE_PATH = Path("reports/sol_spot_adaptive_state.json")
REPORT_PATH = Path("reports/sol_spot_adaptive_report.md")


def _credentials() -> tuple[str, str]:
    return (
        os.getenv("TELEGRAM_BOT_TOKEN", "").strip(),
        os.getenv("TELEGRAM_CHAT_ID", "").strip(),
    )


def _load_state() -> dict[str, Any]:
    if not STATE_PATH.exists():
        raise FileNotFoundError(f"State SOL non trovato: {STATE_PATH}")
    return json.loads(STATE_PATH.read_text(encoding="utf-8"))


def _digest(state: dict[str, Any]) -> str:
    relevant = {
        "last_action": state.get("last_action"),
        "last_reason": state.get("last_reason"),
        "sol_qty": round(float(state.get("sol_qty", 0.0)), 8),
        "cash_eur": round(float(state.get("cash_eur", 0.0)), 2),
        "equity_eur": round(float(state.get("equity_eur", 0.0)), 2),
        "trades": int(state.get("trades", 0)),
        "last_candle_time": state.get("last_candle_time"),
    }
    payload = json.dumps(relevant, sort_keys=True, ensure_ascii=False)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def _fmt_eur(value: float) -> str:
    return f"€{value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def _message(state: dict[str, Any]) -> str:
    bands = dict(state.get("bands", {}))
    action = str(state.get("last_action", "HOLD"))
    reason = str(state.get("last_reason", "Nessuna motivazione disponibile"))
    return (
        "🟣 SOL SPOT ADAPTIVE — PAPER TRADING\n\n"
        f"Decisione: {action}\n"
        f"Motivo: {reason}\n\n"
        f"Prezzo SOL: ${float(state.get('last_price', 0.0)):.4f}\n"
        f"Equity: {_fmt_eur(float(state.get('equity_eur', 40000.0)))}\n"
        f"Cash: {_fmt_eur(float(state.get('cash_eur', 40000.0)))}\n"
        f"SOL detenuti: {float(state.get('sol_qty', 0.0)):.6f}\n"
        f"Rendimento: {float(state.get('return_pct', 0.0)):+.2f}%\n"
        f"Operazioni: {int(state.get('trades', 0))}\n"
        f"Max drawdown: {float(state.get('max_drawdown_pct', 0.0)):.2f}%\n\n"
        "Bande 4H:\n"
        f"L2 {float(bands.get('lower2', 0.0)):.4f} · "
        f"L1 {float(bands.get('lower1', 0.0)):.4f} · "
        f"Media {float(bands.get('mid', 0.0)):.4f} · "
        f"U1 {float(bands.get('upper1', 0.0)):.4f} · "
        f"U2 {float(bands.get('upper2', 0.0)):.4f}\n\n"
        "Solo spot · nessuna leva · capitale separato €40.000"
    )


def _send_message(token: str, chat_id: str, text: str) -> None:
    response = requests.post(
        f"https://api.telegram.org/bot{token}/sendMessage",
        json={
            "chat_id": chat_id,
            "text": text,
            "disable_web_page_preview": True,
        },
        timeout=30,
    )
    response.raise_for_status()


def _send_document(token: str, chat_id: str) -> None:
    if not REPORT_PATH.exists():
        return
    with REPORT_PATH.open("rb") as handle:
        response = requests.post(
            f"https://api.telegram.org/bot{token}/sendDocument",
            data={
                "chat_id": chat_id,
                "caption": "Report SOL Spot Adaptive — paper trading separato.",
            },
            files={"document": (REPORT_PATH.name, handle, "text/markdown")},
            timeout=60,
        )
    response.raise_for_status()


def send(force: bool = False) -> bool:
    token, chat_id = _credentials()
    if not token or not chat_id:
        raise RuntimeError("Secret TELEGRAM_BOT_TOKEN o TELEGRAM_CHAT_ID mancanti.")

    state = _load_state()
    digest = _digest(state)
    notifications = state.setdefault("notifications", {})
    previous = notifications.get("telegram_last_sol_digest")

    if not force and previous == digest:
        print("Notifica SOL invariata: nessun messaggio Telegram inviato.")
        return False

    _send_message(token, chat_id, _message(state))
    _send_document(token, chat_id)

    notifications["telegram_last_sol_digest"] = digest
    notifications["telegram_last_sol_sent_utc"] = state.get("updated_utc")
    STATE_PATH.write_text(
        json.dumps(state, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print("Notifica Telegram SOL inviata.")
    return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()
    send(force=args.force)
