# -*- coding: utf-8 -*-
"""Telegram notifications for automatic KuCoin paper trading.

The bot sends immediate messages only for meaningful changes (open, close,
trailing-stop updates and risk blocks) plus a compact periodic status digest.
Manual workflow runs force a digest, which makes them useful for connection
tests without fabricating trades.
"""

from __future__ import annotations

import math
import os
from datetime import datetime, timedelta, timezone
from typing import Any

import requests

from paper_trading_sample_watch import (
    mark_milestones_sent,
    pending_milestone_notification,
)

from research_sample_watch import (
    mark_research_notifications_sent,
    pending_research_notifications,
)

from paper_trading_display import (
    aggregate_positions,
    current_stop_risk_eur,
    portfolio_description,
    portfolio_label,
    strategy_label,
)


def _fmt_eur(value: Any, signed: bool = False) -> str:
    try:
        number = float(value)
        if number < 0:
            prefix = "-"
        elif signed and number > 0:
            prefix = "+"
        else:
            prefix = ""
        rendered = f"{prefix}€{abs(number):,.2f}"
        return rendered.replace(",", "X").replace(".", ",").replace("X", ".")
    except Exception:
        return "n/a"


def _fmt_pct(value: Any, signed: bool = False) -> str:
    try:
        number = float(value)
        prefix = "+" if signed and number > 0 else ""
        return f"{prefix}{number:.2f}%".replace(".", ",")
    except Exception:
        return "n/a"


def _fmt_num(value: Any, digits: int = 2) -> str:
    try:
        number = float(value)
        if math.isinf(number):
            return "∞"
        return f"{number:.{digits}f}".replace(".", ",")
    except Exception:
        return "n/a"


def _chunks(lines: list[str], max_chars: int = 3600) -> list[str]:
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


def _settings(config: dict[str, Any]) -> dict[str, Any]:
    return dict(config.get("notifications", {}))


def build_event_messages(summary: dict[str, Any]) -> list[str]:
    opened = list(summary.get("opened", []))
    closed = list(summary.get("closed", []))
    trailing = list(summary.get("trailing_updates", []))
    risk_alerts = list(summary.get("risk_alerts", []))
    risk_recoveries = list(summary.get("risk_recoveries", []))
    if (
        not opened
        and not closed
        and not trailing
        and not risk_alerts
        and not risk_recoveries
    ):
        return []

    lines = ["🧪 PAPER TRADING KUCOIN — EVENTI"]

    if opened:
        lines.extend(
            [
                "",
                "📌 NUOVE APERTURE",
                (
                    "Ogni portafoglio è una simulazione separata: "
                    "i margini dei diversi portafogli non rappresentano "
                    "un unico conto reale."
                ),
            ]
        )
        grouped: dict[str, list[dict[str, Any]]] = {}
        for position in opened:
            name = str(position.get("portfolio", ""))
            grouped.setdefault(name, []).append(position)

        ordered_names = sorted(
            grouped,
            key=lambda name: (
                0 if name == "MAIN" else 1,
                portfolio_label(name),
            ),
        )
        for name in ordered_names:
            positions = grouped[name]
            totals = aggregate_positions(positions)
            count = int(totals["count"])
            average_risk = (
                float(totals["initial_risk_eur"]) / count
                if count
                else 0.0
            )
            plural = "posizione" if count == 1 else "posizioni"
            lines.extend(
                [
                    "",
                    (
                        f"📁 {portfolio_label(name).upper()} — "
                        f"{count} nuove {plural}"
                    ),
                    portfolio_description(name),
                    (
                        f"Margine impegnato "
                        f"{_fmt_eur(totals['margin_eur'])} · "
                        f"Esposizione con leva "
                        f"{_fmt_eur(totals['notional_eur'])}"
                    ),
                    (
                        f"Capitale a rischio agli stop "
                        f"{_fmt_eur(totals['initial_risk_eur'])} · "
                        f"media {_fmt_eur(average_risk)} per posizione"
                    ),
                ]
            )
            for position in positions:
                icon = (
                    "🟢"
                    if position.get("side") == "LONG"
                    else "🔴"
                )
                lines.extend(
                    [
                        "",
                        (
                            f"{icon} {position.get('asset', '')} "
                            f"{position.get('side', '')} · "
                            f"{float(position.get('leverage', 0.0)):.1f}x "
                            f"· TF {position.get('timeframe_minutes', '')}m"
                        ),
                        (
                            f"Entry "
                            f"{float(position.get('entry_price', 0.0)):.6g} "
                            f"· Stop "
                            f"{float(position.get('stop_price', 0.0)):.6g}"
                        ),
                        (
                            f"Liquidazione stimata "
                            f"{float(position.get('liquidation_price', 0.0)):.6g} "
                            f"· Target "
                            f"{float(position.get('target_price', 0.0)):.6g}"
                        ),
                        (
                            f"Margine "
                            f"{_fmt_eur(position.get('margin_eur'))} "
                            f"· Esposizione "
                            f"{_fmt_eur(position.get('notional_eur'))} "
                            f"· Rischio massimo "
                            f"{_fmt_eur(position.get('initial_risk_eur'))}"
                        ),
                    ]
                )

    for update in trailing:
        lines.extend(
            [
                "",
                (
                    f"🔄 STOP AGGIORNATO "
                    f"{portfolio_label(update.get('portfolio', ''))}"
                ),
                (
                    f"{update.get('asset', '')} "
                    f"{update.get('side', '')} · "
                    f"{float(update.get('old_stop_price', 0.0)):.6g} "
                    f"→ {float(update.get('new_stop_price', 0.0)):.6g}"
                ),
                f"Mark {float(update.get('mark_price', 0.0)):.6g}",
            ]
        )

    for trade in closed:
        pnl = float(trade.get("net_pnl_eur", 0.0))
        icon = "✅" if pnl > 0 else "❌" if pnl < 0 else "➖"
        lines.extend(
            [
                "",
                (
                    f"{icon} CHIUSURA "
                    f"{portfolio_label(trade.get('portfolio', ''))}"
                ),
                (
                    f"{trade.get('asset', '')} "
                    f"{trade.get('side', '')} · "
                    f"{trade.get('close_reason', '')}"
                ),
                (
                    f"P&L netto {_fmt_eur(pnl, signed=True)} · "
                    f"R {_fmt_num(trade.get('r_multiple'))}"
                ),
                (
                    f"Exit {float(trade.get('exit_price', 0.0)):.6g} · "
                    f"Durata {_fmt_num(trade.get('holding_hours'))} h"
                ),
            ]
        )

    for alert in risk_alerts:
        lines.extend(
            [
                "",
                (
                    f"⚠️ BLOCCO RISCHIO "
                    f"{portfolio_label(alert.get('portfolio', ''))}"
                ),
                str(alert.get("reason", "limite di rischio raggiunto")),
                f"Equity {_fmt_eur(alert.get('equity_eur'))}",
            ]
        )

    for recovery in risk_recoveries:
        lines.extend(
            [
                "",
                (
                    f"✅ RISCHIO RIABILITATO "
                    f"{portfolio_label(recovery.get('portfolio', ''))}"
                ),
                f"Equity {_fmt_eur(recovery.get('equity_eur'))}",
            ]
        )
    return _chunks(lines)


def should_send_periodic(
    state: dict[str, Any],
    config: dict[str, Any],
    now: datetime | None = None,
) -> bool:
    force = os.getenv("TELEGRAM_FORCE_SUMMARY", "").strip().lower() in {"1", "true", "yes"}
    manual = os.getenv("GITHUB_EVENT_NAME", "").strip() == "workflow_dispatch"
    if force or manual:
        return True

    interval = float(_settings(config).get("telegram_digest_interval_hours", 4.0))
    if interval <= 0:
        return False
    current = (now or datetime.now(timezone.utc)).astimezone(timezone.utc)
    last = _parse_iso(state.get("notifications", {}).get("telegram_last_digest_utc"))
    return last is None or current - last >= timedelta(hours=interval)


def build_status_message(
    state: dict[str, Any],
    config: dict[str, Any],
    summary: dict[str, Any] | None = None,
) -> str:
    # Separate compact account summary for Telegram.
    from paper_trading_report import portfolio_metrics

    metrics = portfolio_metrics(state, config)
    if not metrics:
        return "💼 RIEPILOGO CONTI — stato non disponibile"

    initial = float(
        state.get(
            "initial_capital_eur",
            config.get("initial_capital_eur", 0.0),
        )
    )
    by_name = {
        str(row.get("portfolio", "")): row
        for row in metrics
    }

    ordered_names = [
        str(definition.get("name", ""))
        for definition in config.get("portfolios", [])
        if definition.get("enabled", True)
        and str(definition.get("name", "")) in by_name
    ]
    ordered_names.extend(
        name
        for name in by_name
        if name not in ordered_names
    )
    account_number = {
        name: index
        for index, name in enumerate(
            ordered_names,
            start=1,
        )
    }

    activity = summary or {}
    opened = list(activity.get("opened", []))
    closed = list(activity.get("closed", []))

    new_margin = sum(
        float(row.get("margin_eur", 0.0))
        for row in opened
    )
    new_exposure = sum(
        float(row.get("notional_eur", 0.0))
        for row in opened
    )
    closed_margin = sum(
        float(row.get("margin_eur", 0.0))
        for row in closed
    )
    realized = sum(
        float(row.get("net_pnl_eur", 0.0))
        for row in closed
    )

    total_open_margin = sum(
        float(row.get("open_margin_eur", 0.0))
        for row in metrics
    )
    total_open_pnl = sum(
        float(row.get("unrealized_pnl_eur", 0.0))
        for row in metrics
    )
    total_closed_pnl = sum(
        float(row.get("net_pnl_closed_eur", 0.0))
        for row in metrics
    )

    lines = [
        "💼 RIEPILOGO SINTETICO CONTI PAPER",
        (
            "Ogni conto è una simulazione separata; "
            "le somme complessive sono solo un riepilogo tecnico."
        ),
    ]

    if opened or closed:
        lines.extend(
            [
                "",
                "🔄 MOVIMENTI DELL’ULTIMO CICLO",
                (
                    f"Entrate: {len(opened)} · "
                    f"margine impiegato {_fmt_eur(new_margin)} · "
                    f"esposizione {_fmt_eur(new_exposure)}"
                ),
                (
                    f"Uscite: {len(closed)} · "
                    f"margine liberato {_fmt_eur(closed_margin)} · "
                    f"P/L realizzato "
                    f"{_fmt_eur(realized, signed=True)}"
                ),
            ]
        )

        for position in opened[:8]:
            name = str(position.get("portfolio", ""))
            number = account_number.get(name, "?")
            lines.append(
                (
                    f"↗ C{number} "
                    f"{position.get('asset', '')} "
                    f"{position.get('side', '')} · "
                    f"entry "
                    f"{float(position.get('entry_price', 0.0)):.6g} · "
                    f"impiegato "
                    f"{_fmt_eur(position.get('margin_eur'))}"
                )
            )

        for trade in closed[:8]:
            name = str(trade.get("portfolio", ""))
            number = account_number.get(name, "?")
            lines.append(
                (
                    f"↘ C{number} "
                    f"{trade.get('asset', '')} "
                    f"{trade.get('side', '')} · "
                    f"{float(trade.get('entry_price', 0.0)):.6g}"
                    f"→{float(trade.get('exit_price', 0.0)):.6g} · "
                    f"P/L "
                    f"{_fmt_eur(trade.get('net_pnl_eur'), signed=True)}"
                )
            )

        hidden = max(0, len(opened) - 8) + max(
            0,
            len(closed) - 8,
        )
        if hidden:
            lines.append(
                f"…altri {hidden} movimenti nel messaggio dettagliato."
            )

    lines.extend(
        [
            "",
            "📊 STATO DEI CONTI",
            (
                f"Margine aperto complessivo "
                f"{_fmt_eur(total_open_margin)} · "
                f"P/L aperto "
                f"{_fmt_eur(total_open_pnl, signed=True)} · "
                f"P/L chiuso "
                f"{_fmt_eur(total_closed_pnl, signed=True)}"
            ),
        ]
    )

    for name in ordered_names:
        row = by_name[name]
        number = account_number[name]
        equity = float(row.get("equity_eur", 0.0))
        total_pnl = equity - initial
        icon = (
            "🟢"
            if total_pnl > 0
            else "🔴"
            if total_pnl < 0
            else "⚪"
        )
        lines.extend(
            [
                "",
                (
                    f"{icon} Conto {number} — "
                    f"{portfolio_label(name)}"
                ),
                (
                    f"Impiegato "
                    f"{_fmt_eur(row.get('open_margin_eur'))} · "
                    f"Equity {_fmt_eur(equity)} · "
                    f"aperte {row.get('open_positions', 0)}"
                ),
                (
                    f"P/L aperto "
                    f"{_fmt_eur(row.get('unrealized_pnl_eur'), signed=True)} · "
                    f"chiuso "
                    f"{_fmt_eur(row.get('net_pnl_closed_eur'), signed=True)} · "
                    f"totale "
                    f"{_fmt_eur(total_pnl, signed=True)}"
                ),
            ]
        )

    return "\n".join(lines)


def _send_text(token: str, chat_id: str, text: str) -> None:
    response = requests.post(
        f"https://api.telegram.org/bot{token}/sendMessage",
        json={"chat_id": chat_id, "text": text, "disable_web_page_preview": True},
        timeout=20,
    )
    response.raise_for_status()


def notify(
    summary: dict[str, Any],
    state: dict[str, Any] | None = None,
    config: dict[str, Any] | None = None,
    now: datetime | None = None,
) -> dict[str, Any]:
    token = os.getenv("TELEGRAM_BOT_TOKEN", "").strip()
    chat_id = os.getenv("TELEGRAM_CHAT_ID", "").strip()
    result = {
        "configured": bool(token and chat_id),
        "sent": False,
        "event_messages": 0,
        "account_summary_sent": False,
        "digest_sent": False,
        "sample_milestone_sent": False,
        "sample_milestones": [],
        "research_milestone_messages": 0,
        "research_milestones_sent": False,
        "research_meta_ready_sent": False,
    }
    if not token or not chat_id:
        return result

    active_config = config or {}
    settings = _settings(active_config)
    messages: list[str] = []

    event_messages: list[str] = []
    if settings.get("send_live_trade_events", True):
        event_messages = build_event_messages(summary)
        messages.extend(event_messages)
        result["event_messages"] = len(event_messages)

    milestone_message = None
    reached_milestones: list[int] = []
    if state is not None and config is not None:
        (
            milestone_message,
            reached_milestones,
            _,
        ) = pending_milestone_notification(
            state,
            config,
        )
        if milestone_message:
            messages.extend(
                _chunks(milestone_message.splitlines())
            )
            result["sample_milestones"] = (
                reached_milestones
            )

    research_marks: dict[str, Any] = {}
    if state is not None and config is not None:
        (
            research_messages,
            research_marks,
            research_snapshot,
        ) = pending_research_notifications(
            state,
            config,
        )
        messages.extend(research_messages)
        result["research_milestone_messages"] = len(
            research_messages
        )
        result["research_snapshot"] = research_snapshot

    current = (
        now or datetime.now(timezone.utc)
    ).astimezone(timezone.utc)
    digest_due = (
        state is not None
        and config is not None
        and should_send_periodic(
            state,
            config,
            current,
        )
    )

    event_activity = bool(
        summary.get("opened")
        or summary.get("closed")
        or summary.get("trailing_updates")
        or summary.get("risk_alerts")
        or summary.get("risk_recoveries")
    )
    account_summary_due = (
        state is not None
        and config is not None
        and (digest_due or event_activity)
    )
    if account_summary_due:
        messages.extend(
            _chunks(
                build_status_message(
                    state,
                    config,
                    summary,
                ).splitlines()
            )
        )
        result["account_summary_sent"] = True

    if not messages:
        return result

    for message in messages:
        _send_text(token, chat_id, message)
    result["sent"] = True

    if reached_milestones and state is not None:
        mark_milestones_sent(
            state,
            reached_milestones,
        )
        result["sample_milestone_sent"] = True

    if research_marks and state is not None:
        mark_research_notifications_sent(
            state,
            research_marks,
        )
        result["research_milestones_sent"] = bool(
            research_marks.get("strategy")
            or research_marks.get("regime")
        )
        result["research_meta_ready_sent"] = bool(
            research_marks.get("meta_ready")
        )

    if digest_due and state is not None:
        state.setdefault(
            "notifications",
            {},
        )["telegram_last_digest_utc"] = (
            current.isoformat(timespec="seconds")
        )
        result["digest_sent"] = True
    return result

