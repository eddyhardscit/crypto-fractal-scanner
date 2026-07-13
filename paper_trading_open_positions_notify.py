# -*- coding: utf-8 -*-
"""Separate Telegram report for all currently open paper positions."""

from __future__ import annotations

import math
import os
from datetime import datetime, timezone
from typing import Any

import requests

from paper_trading_display import portfolio_label


def _safe_float(value: Any, default: float = 0.0) -> float:
    try:
        number = float(value)
        return number if math.isfinite(number) else default
    except Exception:
        return default


def _fmt_eur(value: Any, signed: bool = False) -> str:
    number = _safe_float(value)
    if number < 0:
        prefix = "-"
    elif signed and number > 0:
        prefix = "+"
    else:
        prefix = ""
    rendered = f"{prefix}€{abs(number):,.2f}"
    return rendered.replace(",", "X").replace(".", ",").replace("X", ".")


def _fmt_pct(value: Any, signed: bool = False) -> str:
    number = _safe_float(value)
    prefix = "+" if signed and number > 0 else ""
    return f"{prefix}{number:.2f}%".replace(".", ",")


def _fmt_price(value: Any) -> str:
    number = _safe_float(value)
    if number >= 100:
        rendered = f"{number:,.2f}"
        return rendered.replace(",", "X").replace(".", ",").replace("X", ".")
    if number >= 1:
        return f"{number:.4f}".rstrip("0").rstrip(".").replace(".", ",")
    return f"{number:.8f}".rstrip("0").rstrip(".").replace(".", ",")


def _parse_iso(value: Any) -> datetime | None:
    if not value:
        return None
    try:
        parsed = datetime.fromisoformat(str(value).replace("Z", "+00:00"))
        if parsed.tzinfo is None:
            parsed = parsed.replace(tzinfo=timezone.utc)
        return parsed.astimezone(timezone.utc)
    except Exception:
        return None


def _duration_text(opened_at: Any, current: datetime) -> str:
    opened = _parse_iso(opened_at)
    if opened is None:
        return "n/a"
    seconds = max(0, int((current - opened).total_seconds()))
    days, remainder = divmod(seconds, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes = remainder // 60
    if days:
        return f"{days}g {hours}h"
    if hours:
        return f"{hours}h {minutes}m"
    return f"{minutes}m"


def _mark_prices(bundle: dict[str, Any]) -> dict[str, float]:
    prices: dict[str, float] = {}
    for asset, payload in bundle.get("assets", {}).items():
        if not isinstance(payload, dict):
            continue
        price = _safe_float(payload.get("mark_price"))
        if price > 0:
            prices[str(asset)] = price
    return prices


def _unrealized_eur(
    position: dict[str, Any],
    mark: float,
    eur_usdt_rate: float,
) -> float:
    entry = _safe_float(position.get("entry_price"))
    quantity = abs(_safe_float(position.get("quantity")))
    funding = _safe_float(position.get("funding_pnl_eur"))
    side = str(position.get("side", "")).upper()
    if entry <= 0 or mark <= 0 or quantity <= 0:
        return funding
    raw_usdt = (
        (mark - entry) * quantity
        if side == "LONG"
        else (entry - mark) * quantity
    )
    return raw_usdt / max(eur_usdt_rate, 1e-9) + funding


def _distance_pct(
    mark: float,
    level: float,
    side: str,
    kind: str,
) -> float | None:
    if mark <= 0 or level <= 0:
        return None
    side = side.upper()
    if kind == "stop":
        return (
            (mark - level) / mark * 100.0
            if side == "LONG"
            else (level - mark) / mark * 100.0
        )
    return (
        (level - mark) / mark * 100.0
        if side == "LONG"
        else (mark - level) / mark * 100.0
    )


def _fmt_distance(value: float | None) -> str:
    if value is None:
        return "n/a"
    if value < 0:
        return f"superato di {_fmt_pct(abs(value))}"
    return _fmt_pct(value)


def _risk_assessment(
    position: dict[str, Any],
    pnl_eur: float,
    stop_distance_pct: float | None,
) -> tuple[str, str]:
    """Classify residual position risk, recognizing protected stops first."""
    margin = max(_safe_float(position.get("margin_eur")), 1e-9)
    leverage = _safe_float(position.get("leverage"))
    entry = _safe_float(position.get("entry_price"))
    stop = _safe_float(position.get("stop_price"))
    side = str(position.get("side", "")).upper()
    pnl_on_margin = pnl_eur / margin * 100.0

    # A profitable trade with the stop at entry is not "high risk":
    # it is protected around break-even. If the stop has crossed entry
    # in the profitable direction, part of the profit is already locked.
    if pnl_eur > 0 and entry > 0 and stop > 0 and side in {"LONG", "SHORT"}:
        stop_vs_entry_pct = (stop - entry) / entry * 100.0
        entry_tolerance_pct = 0.10

        if abs(stop_vs_entry_pct) <= entry_tolerance_pct:
            return (
                "🟢 BREAK-EVEN",
                (
                    "stop sull'entry: perdita residua limitata "
                    "a costi/slippage; profitto aperto non ancora bloccato"
                ),
            )

        profit_locked = (
            side == "LONG" and stop_vs_entry_pct > entry_tolerance_pct
        ) or (
            side == "SHORT" and stop_vs_entry_pct < -entry_tolerance_pct
        )
        if profit_locked:
            return (
                "🟢 PROFITTO PROTETTO",
                "stop oltre l'entry: una parte del profitto è già bloccata",
            )

    # Normalize ATR defensively. Some historical positions may contain
    # a decimal ratio (0.039) while others contain percent points (3.9).
    # Malformed/extreme values must never turn a 25% stop distance into
    # a false "stop very close" warning.
    atr_raw = abs(_safe_float(position.get("atr_pct")))
    if 0 < atr_raw <= 0.50:
        atr_pct = atr_raw * 100.0
    elif atr_raw <= 25.0:
        atr_pct = atr_raw
    else:
        atr_pct = 0.0

    red_stop_threshold = max(
        1.0,
        min(3.0, atr_pct * 0.60),
    )
    yellow_stop_threshold = max(
        2.5,
        min(6.0, atr_pct * 1.20),
    )

    if (
        stop_distance_pct is not None
        and stop_distance_pct <= red_stop_threshold
    ):
        return "🔴 ALTO", "stop molto vicino rispetto alla volatilità"
    if pnl_on_margin <= -8.0:
        return "🔴 ALTO", "perdita elevata rispetto al margine"
    if leverage >= 10.0:
        return "🔴 ALTO", "leva molto elevata"

    if (
        stop_distance_pct is not None
        and stop_distance_pct <= yellow_stop_threshold
    ):
        return "🟡 MEDIO", "stop relativamente vicino"
    if pnl_on_margin <= -3.0:
        return "🟡 MEDIO", "posizione in perdita"
    if leverage >= 5.0:
        return "🟡 MEDIO", "leva significativa"

    return "🟢 BASSO", "margine di sicurezza ancora ampio"


def _chunks(lines: list[str], max_chars: int = 3500) -> list[str]:
    messages: list[str] = []
    current: list[str] = []
    length = 0
    for line in lines:
        extra = len(line) + (1 if current else 0)
        if current and length + extra > max_chars:
            messages.append("\n".join(current))
            current = [line]
            length = len(line)
        else:
            current.append(line)
            length += extra
    if current:
        messages.append("\n".join(current))
    return messages


def build_open_positions_messages(
    state: dict[str, Any],
    config: dict[str, Any],
    bundle: dict[str, Any],
    now: datetime | None = None,
) -> list[str]:
    current = (now or datetime.now(timezone.utc)).astimezone(timezone.utc)
    prices = _mark_prices(bundle)
    eur_rate = _safe_float(
        bundle.get(
            "eur_usdt_rate",
            config.get("eur_usdt_fallback_rate", 1.0),
        ),
        1.0,
    ) or 1.0

    portfolios = dict(state.get("portfolios", {}))
    configured_names = [
        str(row.get("name", ""))
        for row in config.get("portfolios", [])
        if row.get("enabled", True)
    ]
    ordered_names = [name for name in configured_names if name in portfolios]
    ordered_names.extend(name for name in portfolios if name not in ordered_names)
    account_number = {
        name: index
        for index, name in enumerate(ordered_names, start=1)
    }

    total_positions = sum(
        len(portfolio.get("open_positions", []))
        for portfolio in portfolios.values()
    )
    if total_positions == 0:
        return [
            (
                "📌 POSIZIONI PAPER ANCORA APERTE\n\n"
                "Nessuna posizione paper attualmente aperta."
            )
        ]

    lines = [
        "📌 POSIZIONI PAPER ANCORA APERTE",
        (
            f"Totale: {total_positions}. "
            "Ogni conto è una simulazione separata."
        ),
    ]

    for name in ordered_names:
        portfolio = portfolios[name]
        positions = list(portfolio.get("open_positions", []))
        if not positions:
            continue

        number = account_number[name]
        account_pnl = 0.0
        rendered_positions: list[str] = []

        for position in positions:
            asset = str(position.get("asset", ""))
            side = str(position.get("side", "")).upper()
            entry = _safe_float(position.get("entry_price"))
            mark = prices.get(asset, entry)
            stop = _safe_float(position.get("stop_price"))
            target = _safe_float(position.get("target_price"))
            margin = _safe_float(position.get("margin_eur"))
            notional = _safe_float(position.get("notional_eur"))
            leverage = _safe_float(position.get("leverage"))
            pnl = _unrealized_eur(position, mark, eur_rate)
            pnl_pct = pnl / margin * 100.0 if margin > 0 else 0.0
            stop_distance = _distance_pct(mark, stop, side, "stop")
            target_distance = _distance_pct(mark, target, side, "target")
            risk, risk_reason = _risk_assessment(
                position,
                pnl,
                stop_distance,
            )

            account_pnl += pnl
            side_icon = "🟢" if side == "LONG" else "🔴"
            pnl_icon = "✅" if pnl > 0 else "❌" if pnl < 0 else "➖"

            rendered_positions.extend(
                [
                    "",
                    (
                        f"{side_icon} {asset} {side} · "
                        f"{leverage:.1f}x · "
                        f"TF {position.get('timeframe_minutes', '')}m"
                    ),
                    (
                        f"Entry {_fmt_price(entry)} · "
                        f"Mark {_fmt_price(mark)}"
                    ),
                    (
                        f"{pnl_icon} P/L {_fmt_eur(pnl, signed=True)} "
                        f"({_fmt_pct(pnl_pct, signed=True)} sul margine)"
                    ),
                    (
                        f"Margine {_fmt_eur(margin)} · "
                        f"Esposizione {_fmt_eur(notional)}"
                    ),
                    (
                        f"Stop {_fmt_price(stop)} · "
                        f"distanza {_fmt_distance(stop_distance)}"
                    ),
                    (
                        f"Target {_fmt_price(target)} · "
                        f"distanza {_fmt_distance(target_distance)}"
                    ),
                    (
                        f"Rischio: {risk} — {risk_reason} · "
                        f"aperta da "
                        f"{_duration_text(position.get('opened_at'), current)}"
                    ),
                ]
            )

        account_icon = (
            "🟢"
            if account_pnl > 0
            else "🔴"
            if account_pnl < 0
            else "⚪"
        )
        lines.extend(
            [
                "",
                "──────────────",
                (
                    f"{account_icon} Conto {number} — "
                    f"{portfolio_label(name)}"
                ),
                (
                    f"{len(positions)} aperte · "
                    f"P/L aperto conto {_fmt_eur(account_pnl, signed=True)}"
                ),
            ]
        )
        lines.extend(rendered_positions)

    lines.extend(
        [
            "",
            "Legenda rischio:",
            (
                "🟢 ampio margine · 🟡 attenzione · "
                "🔴 stop vicino, perdita elevata o leva molto alta"
            ),
            f"Controllato: {current.isoformat(timespec='seconds')}",
        ]
    )
    return _chunks(lines)


def send_open_positions_report(
    state: dict[str, Any],
    config: dict[str, Any],
    bundle: dict[str, Any],
    now: datetime | None = None,
) -> dict[str, Any]:
    token = os.getenv("TELEGRAM_BOT_TOKEN", "").strip()
    chat_id = os.getenv("TELEGRAM_CHAT_ID", "").strip()
    result = {
        "configured": bool(token and chat_id),
        "sent": False,
        "messages": 0,
    }
    if not token or not chat_id:
        return result

    messages = build_open_positions_messages(
        state,
        config,
        bundle,
        now,
    )
    for message in messages:
        response = requests.post(
            f"https://api.telegram.org/bot{token}/sendMessage",
            json={
                "chat_id": chat_id,
                "text": message,
                "disable_web_page_preview": True,
            },
            timeout=20,
        )
        response.raise_for_status()

    result["sent"] = bool(messages)
    result["messages"] = len(messages)
    return result
