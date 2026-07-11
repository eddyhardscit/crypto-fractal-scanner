# -*- coding: utf-8 -*-
"""Optional Telegram notifications for paper-trading events."""

from __future__ import annotations

import os
from typing import Any

import requests


def _fmt_eur(value: Any) -> str:
    try:
        return f"€{float(value):,.2f}"
    except Exception:
        return "n/a"


def build_message(summary: dict[str, Any]) -> str:
    opened = summary.get("opened", [])
    closed = summary.get("closed", [])
    lines = ["🧪 Paper trading KuCoin"]
    for position in opened:
        lines.append(
            f"OPEN {position['portfolio']} | {position['asset']} {position['side']} "
            f"{position['leverage']:.1f}x | entry {position['entry_price']:.6g} | "
            f"stop {position['stop_price']:.6g} | target {position['target_price']:.6g} | "
            f"rischio {_fmt_eur(position['initial_risk_eur'])}"
        )
    for trade in closed:
        lines.append(
            f"CLOSE {trade['portfolio']} | {trade['asset']} {trade['side']} | "
            f"{trade['close_reason']} | P&L {_fmt_eur(trade['net_pnl_eur'])} | R {trade['r_multiple']:.2f}"
        )
    return "\n".join(lines)


def notify(summary: dict[str, Any]) -> bool:
    if not summary.get("opened") and not summary.get("closed"):
        return False
    token = os.getenv("TELEGRAM_BOT_TOKEN", "").strip()
    chat_id = os.getenv("TELEGRAM_CHAT_ID", "").strip()
    if not token or not chat_id:
        return False
    response = requests.post(
        f"https://api.telegram.org/bot{token}/sendMessage",
        json={"chat_id": chat_id, "text": build_message(summary), "disable_web_page_preview": True},
        timeout=20,
    )
    response.raise_for_status()
    return True
