# -*- coding: utf-8 -*-
"""Periodic Telegram status for the dedicated DOGE rejection-short paper setup."""

from __future__ import annotations

import json
import math
import os
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

import requests


REPORTS_DIR = Path("reports")
DOGE_CONFIG_PATH = Path("doge_rejection_short_config.json")
DOGE_STATE_PATH = REPORTS_DIR / "doge_rejection_short_state.json"
STATUS_STATE_PATH = REPORTS_DIR / "doge_rejection_short_status_state.json"


def _safe_float(value: Any, default: float = 0.0) -> float:
    try:
        number = float(value)
        return number if math.isfinite(number) else default
    except Exception:
        return default


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


def _iso(value: datetime) -> str:
    return value.astimezone(timezone.utc).isoformat(timespec="seconds")


def _read_json(path: Path, default: dict[str, Any]) -> dict[str, Any]:
    if not path.exists():
        return dict(default)
    try:
        loaded = json.loads(path.read_text(encoding="utf-8"))
        return loaded if isinstance(loaded, dict) else dict(default)
    except Exception:
        return dict(default)


def _write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_suffix(path.suffix + ".tmp")
    temp.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    temp.replace(path)


def _fmt_price(value: Any) -> str:
    number = _safe_float(value)
    return f"{number:.6f}".rstrip("0").rstrip(".")


def _fmt_eur(value: Any, signed: bool = False) -> str:
    number = _safe_float(value)
    prefix = "+" if signed and number > 0 else ""
    rendered = f"{prefix}€{number:,.2f}"
    return rendered.replace(",", "X").replace(".", ",").replace("X", ".")


def _fmt_distance(mark: float, level: float) -> str:
    if mark <= 0 or level <= 0:
        return "n/a"
    value = (level / mark - 1.0) * 100.0
    prefix = "+" if value > 0 else ""
    return f"{prefix}{value:.2f}%".replace(".", ",")


def _phase_text(phase: str, mark: float, config: dict[str, Any]) -> str:
    prealert = _safe_float(config.get("prealert_price"), 0.0765)
    armed = _safe_float(config.get("armed_price"), 0.0775)
    trigger = _safe_float(config.get("trigger_price"), 0.0780)
    invalidation = _safe_float(
        config.get("bearish_invalidation_close"),
        0.07966,
    )

    if phase == "OPEN":
        return "Posizione paper aperta e gestita automaticamente."
    if phase == "COOLDOWN":
        return "Pausa dopo la chiusura; nessun nuovo ingresso."
    if phase == "INVALIDATED":
        return "Setup annullato; attende il riarmo sotto 0,07550."
    if mark <= 0:
        return "Prezzo DOGE non disponibile."
    if mark < prealert:
        return (
            "Fuori dalla zona: manca "
            f"{_fmt_distance(mark, prealert)} al pre-allarme."
        )
    if mark < armed:
        return "Pre-allarme: DOGE si sta avvicinando alla zona short."
    if mark < trigger:
        return "Zona armata: attende il test di 0,078 e la rejection 15m."
    if mark < invalidation:
        return "Dentro la zona trigger: attende una chiusura 15m respinta."
    return "Sopra l’invalidazione: nessuna entrata short finché non rientra."


def _due(
    status_state: dict[str, Any],
    config: dict[str, Any],
    current: datetime,
) -> tuple[bool, str]:
    manual = os.getenv("GITHUB_EVENT_NAME", "").strip() == "workflow_dispatch"
    force = (
        os.getenv("DOGE_STATUS_FORCE", "").strip().lower()
        in {"1", "true", "yes"}
        or os.getenv("TELEGRAM_FORCE_SUMMARY", "").strip().lower()
        in {"1", "true", "yes"}
    )
    if force:
        return True, "forced"
    if manual and bool(config.get("telegram_status_on_manual", True)):
        return True, "manual"

    interval = _safe_float(
        config.get("telegram_status_interval_hours"),
        4.0,
    )
    if interval <= 0:
        return False, "disabled"

    last = _parse_iso(status_state.get("last_sent_utc"))
    if last is None or current - last >= timedelta(hours=interval):
        return True, "periodic"
    return False, "not_due"


def _build_message(
    bundle: dict[str, Any],
    config: dict[str, Any],
    state: dict[str, Any],
    current: datetime,
) -> str:
    assets = bundle.get("assets", {})
    mark = _safe_float(assets.get("DOGE", {}).get("mark_price"))
    eur_rate = _safe_float(bundle.get("eur_usdt_rate"), 1.0) or 1.0
    phase = str(state.get("phase", "WAITING")).upper()

    last_checks = state.get("last_checks", {})
    static = last_checks.get("static", {}) if isinstance(last_checks, dict) else {}
    rejection = (
        last_checks.get("rejection", {})
        if isinstance(last_checks, dict)
        else {}
    )
    checks = (
        static.get("checks", {})
        if isinstance(static, dict)
        else {}
    )

    filter_keys = [
        "fresh_market",
        "candle_15m_fresh",
        "global_bearish",
        "classic_bearish",
        "relative_weak",
        "bearish_pattern_valid",
        "btc_not_breaking_out",
    ]
    passed = sum(bool(checks.get(key)) for key in filter_keys)

    prealert = _safe_float(config.get("prealert_price"), 0.0765)
    armed = _safe_float(config.get("armed_price"), 0.0775)
    trigger = _safe_float(config.get("trigger_price"), 0.0780)
    resistance = _safe_float(config.get("resistance_price"), 0.07923)
    invalidation = _safe_float(
        config.get("bearish_invalidation_close"),
        0.07966,
    )
    min_stop = _safe_float(config.get("minimum_stop_price"), 0.08060)
    max_stop = _safe_float(config.get("maximum_stop_price"), 0.08120)

    lines = [
        "🎯 DOGE SHORT €3.600 · STATO DEDICATO",
        "Paper only — nessun ordine reale.",
        "",
        f"DOGE: {_fmt_price(mark)}",
        f"Stato: {phase}",
        _phase_text(phase, mark, config),
        "",
        "LIVELLI DEL SETUP",
        (
            f"Pre-allarme {_fmt_price(prealert)} "
            f"({_fmt_distance(mark, prealert)} dal prezzo)"
        ),
        (
            f"Zona armata {_fmt_price(armed)} "
            f"({_fmt_distance(mark, armed)} dal prezzo)"
        ),
        (
            f"Trigger rejection {_fmt_price(trigger)} "
            f"({_fmt_distance(mark, trigger)} dal prezzo)"
        ),
        (
            f"Resistenza {_fmt_price(resistance)} · "
            f"invalidazione 15m {_fmt_price(invalidation)}"
        ),
        (
            f"Stop previsto {_fmt_price(min_stop)}–"
            f"{_fmt_price(max_stop)}"
        ),
        "TP 0,07107 / 0,06961 / 0,064 / 0,060",
        "",
        f"FILTRI VALIDI: {passed}/{len(filter_keys)}",
        (
            f"{'✅' if checks.get('fresh_market') else '❌'} dati freschi · "
            f"{'✅' if checks.get('candle_15m_fresh') else '❌'} candela 15m"
        ),
        (
            f"{'✅' if checks.get('global_bearish') else '❌'} "
            f"Global {_safe_float(static.get('global_score')):+.0f} · "
            f"{'✅' if checks.get('classic_bearish') else '❌'} "
            f"Classic {_safe_float(static.get('classic_raw_score')):+.0f}"
        ),
        (
            f"{'✅' if checks.get('relative_weak') else '❌'} "
            f"DOGE/BTC {_safe_float(static.get('relative_raw_score')):+.0f} · "
            f"{'✅' if checks.get('bearish_pattern_valid') else '❌'} "
            f"pattern {static.get('bearish_pattern_status', 'n/a')}"
        ),
        (
            f"{'✅' if checks.get('btc_not_breaking_out') else '❌'} "
            f"BTC {_fmt_price(static.get('btc_mark'))} "
            f"< {_fmt_price(config.get('btc_breakout_filter', 65544))}"
        ),
        "",
        "ULTIMA CANDELA 15m",
        (
            f"High {_fmt_price(rejection.get('high'))} · "
            f"close {_fmt_price(rejection.get('close'))}"
        ),
        (
            f"Wick alta "
            f"{_safe_float(rejection.get('upper_wick_ratio')) * 100:.1f}% · "
            f"volume x{_safe_float(rejection.get('volume_ratio')):.2f}"
        ),
        (
            "Rejection completa: "
            f"{'SÌ' if rejection.get('accepted') else 'NO'}"
        ),
    ]

    position = state.get("position")
    if isinstance(position, dict):
        entry = _safe_float(position.get("entry_price"))
        quantity = _safe_float(position.get("remaining_quantity"))
        unrealized = (entry - mark) * quantity / eur_rate
        balance = _safe_float(state.get("balance_eur"))
        equity = balance + unrealized
        lines.extend(
            [
                "",
                "📌 POSIZIONE PAPER APERTA",
                (
                    f"Entry {_fmt_price(entry)} · "
                    f"mark {_fmt_price(mark)}"
                ),
                (
                    f"Stop {_fmt_price(position.get('stop_price'))} · "
                    f"liquidazione stimata "
                    f"{_fmt_price(position.get('liquidation_price'))}"
                ),
                (
                    f"Margine {_fmt_eur(position.get('margin_eur'))} · "
                    f"esposizione residua "
                    f"{_fmt_eur(position.get('remaining_notional_eur'))}"
                ),
                (
                    f"P&L aperto {_fmt_eur(unrealized, signed=True)} · "
                    f"equity {_fmt_eur(equity)}"
                ),
            ]
        )
    else:
        lines.extend(
            [
                "",
                "Nessuna posizione aperta.",
                (
                    "Il bot continua a controllare il setup ogni 15 minuti "
                    "e invierà subito pre-allarme, zona armata o entrata."
                ),
            ]
        )

    lines.extend(["", f"Controllato: {_iso(current)}"])
    return "\n".join(lines)


def send_doge_short_status(
    bundle: dict[str, Any],
    now: datetime | None = None,
) -> dict[str, Any]:
    current = (now or datetime.now(timezone.utc)).astimezone(timezone.utc)
    config = _read_json(
        DOGE_CONFIG_PATH,
        {
            "telegram_status_interval_hours": 4.0,
            "telegram_status_on_manual": True,
        },
    )
    status_state = _read_json(STATUS_STATE_PATH, {})
    due, reason = _due(status_state, config, current)

    result: dict[str, Any] = {
        "configured": False,
        "sent": False,
        "due": due,
        "reason": reason,
    }
    if not due:
        return result

    token = os.getenv("TELEGRAM_BOT_TOKEN", "").strip()
    chat_id = os.getenv("TELEGRAM_CHAT_ID", "").strip()
    result["configured"] = bool(token and chat_id)
    if not token or not chat_id:
        result["error"] = "Telegram non configurato"
        return result

    doge_state = _read_json(DOGE_STATE_PATH, {})
    message = _build_message(
        bundle,
        config,
        doge_state,
        current,
    )
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

    status_state["last_sent_utc"] = _iso(current)
    status_state["last_reason"] = reason
    status_state["last_price"] = _safe_float(
        bundle.get("assets", {}).get("DOGE", {}).get("mark_price")
    )
    _write_json(STATUS_STATE_PATH, status_state)

    result["sent"] = True
    result["price"] = status_state["last_price"]
    return result
