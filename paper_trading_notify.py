# -*- coding: utf-8 -*-
"""Telegram notifications for automatic KuCoin paper trading.

The bot sends immediate messages only for meaningful changes (open, close,
trailing-stop updates and risk blocks) plus a compact periodic status digest.
Manual workflow runs force a digest, which makes them useful for connection
tests without fabricating trades.
"""

from __future__ import annotations

import csv
import json
import math
import os
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

import requests

from paper_trading_event_enrichment import opening_status_lines

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


REPORTS_DIR = Path("reports")
RESEARCH_STATE_PATH = REPORTS_DIR / "research_all_signals_state.json"
RESEARCH_TRADES_PATH = REPORTS_DIR / "research_all_signals_trades.csv"
DOGE_STATE_PATH = REPORTS_DIR / "doge_rejection_short_state.json"
DOGE_TRADES_PATH = REPORTS_DIR / "doge_rejection_short_trades.csv"


def _read_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
        return value if isinstance(value, dict) else {}
    except Exception:
        return {}


def _read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists() or path.stat().st_size == 0:
        return []
    try:
        with path.open("r", encoding="utf-8-sig", newline="") as handle:
            return list(csv.DictReader(handle))
    except Exception:
        return []


def _safe_float(value: Any) -> float:
    try:
        number = float(value)
        return number if math.isfinite(number) else 0.0
    except Exception:
        return 0.0


def _official_lab_lines(metrics: list[dict[str, Any]], initial: float) -> list[str]:
    rows = []
    for row in metrics:
        pnl = _safe_float(row.get("equity_eur")) - initial
        rows.append({
            "label": portfolio_label(str(row.get("portfolio", ""))),
            "pnl": pnl,
            "closed": int(_safe_float(row.get("closed_trades"))),
            "open": int(_safe_float(row.get("open_positions"))),
        })

    profitable = sum(item["pnl"] > 0 for item in rows)
    losing = sum(item["pnl"] < 0 for item in rows)
    flat = len(rows) - profitable - losing
    active = [item for item in rows if item["closed"] or item["open"]]
    pool = active or rows
    top = sorted(pool, key=lambda item: item["pnl"], reverse=True)[:5]
    bottom = sorted(pool, key=lambda item: item["pnl"])[:5]

    lines = [
        "",
        "🧪 LABORATORIO — 30 STRATEGIE UFFICIALI",
        f"In profitto: {profitable} · in perdita: {losing} · ferme: {flat}",
        f"P/L aggregato tecnico: {_fmt_eur(sum(item['pnl'] for item in rows), signed=True)}",
        f"Strategie con attività: {len(active)}/{len(rows)}",
        "",
        "🏆 HALL OF FAME — TOP 5",
    ]
    for index, item in enumerate(top, 1):
        lines.append(
            f"{index}. {item['label']} · {_fmt_eur(item['pnl'], signed=True)} · "
            f"{item['closed']} chiusi/{item['open']} aperti"
        )

    lines.extend(["", "📉 BOTTOM 5"])
    for index, item in enumerate(bottom, 1):
        lines.append(
            f"{index}. {item['label']} · {_fmt_eur(item['pnl'], signed=True)} · "
            f"{item['closed']} chiusi/{item['open']} aperti"
        )
    return lines


def _auxiliary_lab_lines() -> list[str]:
    research_state = _read_json(RESEARCH_STATE_PATH)
    trades = _read_csv(RESEARCH_TRADES_PATH)

    pnl_by_profile: dict[str, float] = {}
    closed_by_profile: dict[str, int] = {}
    for trade in trades:
        profile = str(trade.get("profile", "UNKNOWN")) or "UNKNOWN"
        pnl_by_profile[profile] = pnl_by_profile.get(profile, 0.0) + _safe_float(
            trade.get("net_pnl_eur")
        )
        closed_by_profile[profile] = closed_by_profile.get(profile, 0) + 1

    open_by_profile: dict[str, int] = {}
    for position in research_state.get("open_positions", []):
        if not isinstance(position, dict):
            continue
        profile = str(position.get("profile", "UNKNOWN")) or "UNKNOWN"
        open_by_profile[profile] = open_by_profile.get(profile, 0) + 1

    profiles = sorted(set(pnl_by_profile) | set(open_by_profile))
    rows = [{
        "label": profile,
        "pnl": pnl_by_profile.get(profile, 0.0),
        "closed": closed_by_profile.get(profile, 0),
        "open": open_by_profile.get(profile, 0),
    } for profile in profiles]

    doge_state = _read_json(DOGE_STATE_PATH)
    doge_trades = _read_csv(DOGE_TRADES_PATH)
    rows.append({
        "label": "DOGE rejection short 5x",
        "pnl": sum(_safe_float(item.get("net_pnl_eur")) for item in doge_trades),
        "closed": int(_safe_float(doge_state.get("closed_events"))),
        "open": 1 if doge_state.get("position") else 0,
    })

    profitable = sum(item["pnl"] > 0 for item in rows)
    losing = sum(item["pnl"] < 0 for item in rows)
    flat = len(rows) - profitable - losing
    active = sum(bool(item["closed"] or item["open"]) for item in rows)
    total = sum(item["pnl"] for item in rows)

    lines = [
        "",
        "🔬 BACKGROUND — PROFILI AUSILIARI",
        "Profili previsti: 15 (14 ricerca normalizzata + 1 DOGE)",
        f"Con dati/attività: {active}/{len(rows)} · profitto: {profitable} · "
        f"perdita: {losing} · fermi: {flat}",
        f"P/L chiuso normalizzato: {_fmt_eur(total, signed=True)}",
    ]
    if rows:
        best = max(rows, key=lambda item: item["pnl"])
        worst = min(rows, key=lambda item: item["pnl"])
        lines.append(f"Migliore: {best['label']} · {_fmt_eur(best['pnl'], signed=True)}")
        lines.append(f"Peggiore: {worst['label']} · {_fmt_eur(worst['pnl'], signed=True)}")
    lines.append("Nota: il P/L background è sperimentale e non va sommato ai 30 conti.")
    return lines


COMBO_PREFIX = "SHADOW_COMBO_"
COMBO_LABELS = {
    "SHADOW_COMBO_TREND": "Combo Trend",
    "SHADOW_COMBO_MEAN_REVERSION": "Combo Mean Reversion",
    "SHADOW_COMBO_SCANNER": "Combo Scanner",
    "SHADOW_COMBO_ADAPTIVE": "Combo Adaptive",
}


def _is_combo(name: Any) -> bool:
    return str(name).startswith(COMBO_PREFIX)


def _combo_lines(
    metrics: list[dict[str, Any]],
    initial: float,
) -> list[str]:
    rows = []
    for row in metrics:
        name = str(row.get("portfolio", ""))
        equity = _safe_float(row.get("equity_eur"))
        rows.append({
            "name": name,
            "label": COMBO_LABELS.get(name, name),
            "pnl": equity - initial,
            "closed": int(_safe_float(row.get("closed_trades"))),
            "open": int(_safe_float(row.get("open_positions"))),
            "pf": _safe_float(row.get("profit_factor")),
        })

    lines = ["", "🧬 STRATEGIE COMBINATE — SHADOW"]
    for item in rows:
        lines.append(
            f"{item['label']}: "
            f"{_fmt_eur(item['pnl'], signed=True)} · "
            f"{item['closed']} trade · "
            f"PF {_fmt_num(item['pf'])} · "
            f"{item['open']} aperti"
        )

    active = [
        item for item in rows
        if item["closed"] > 0 or item["open"] > 0
    ]
    if active:
        best = max(active, key=lambda item: item["pnl"])
        lines.append(
            f"Migliore: {best['label']} · "
            f"{_fmt_eur(best['pnl'], signed=True)}"
        )
    else:
        lines.append("Ancora nessuna operazione combinata.")
    lines.append(
        "Solo paper shadow; movimenti dettagliati nascosti, "
        "storico completo conservato."
    )
    return lines


def build_event_messages(summary: dict[str, Any]) -> list[str]:
    opened = [
        row for row in summary.get("opened", [])
        if not _is_combo(row.get("portfolio"))
    ]
    closed = [
        row for row in summary.get("closed", [])
        if not _is_combo(row.get("portfolio"))
    ]
    trailing = [
        row for row in summary.get("trailing_updates", [])
        if not _is_combo(row.get("portfolio"))
    ]
    risk_alerts = [
        row for row in summary.get("risk_alerts", [])
        if not _is_combo(row.get("portfolio"))
    ]
    risk_recoveries = [
        row for row in summary.get("risk_recoveries", [])
        if not _is_combo(row.get("portfolio"))
    ]
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
                        # TELEGRAM_OPENING_STATUS_LINES_V1
                        *opening_status_lines(position),
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
                (
                    f"MFE netto {_fmt_eur(trade.get('mfe_net_eur'), signed=True)} · "
                    f"MAE netto {_fmt_eur(trade.get('mae_net_eur'), signed=True)}"
                ),
                (
                    f"Profitto trattenuto "
                    f"{_fmt_pct(trade.get('profit_retained_pct'), signed=True)} · "
                    f"Giveback dal picco "
                    f"{_fmt_eur(trade.get('peak_profit_giveback_eur'))}"
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

    all_metrics = portfolio_metrics(state, config)
    if not all_metrics:
        return "💼 RIEPILOGO CONTI — stato non disponibile"

    combo_metrics = [
        row for row in all_metrics
        if _is_combo(row.get("portfolio"))
    ]
    metrics = [
        row for row in all_metrics
        if not _is_combo(row.get("portfolio"))
    ]

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

    lines.extend(_official_lab_lines(metrics, initial))
    lines.extend(_auxiliary_lab_lines())
    lines.extend(_combo_lines(combo_metrics, initial))

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

