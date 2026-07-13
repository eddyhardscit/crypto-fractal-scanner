# -*- coding: utf-8 -*-
"""Dedicated DOGE rejection-short paper strategy.

This module is intentionally isolated from the normal €10,000 paper portfolios.
It simulates a €3,600 isolated-margin short at 5x only after a confirmed 15-minute
rejection of the 0.078-0.079 area. It never sends real orders.
"""

from __future__ import annotations

import csv
import json
import math
import os
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

import pandas as pd
import requests


REPORTS_DIR = Path("reports")
CONFIG_PATH = Path("doge_rejection_short_config.json")
STATE_PATH = REPORTS_DIR / "doge_rejection_short_state.json"
TRADES_PATH = REPORTS_DIR / "doge_rejection_short_trades.csv"
REPORT_PATH = REPORTS_DIR / "doge_rejection_short_report.md"
LATEST_PATH = REPORTS_DIR / "doge_rejection_short_latest.json"
GLOBAL_METRICS_PATH = REPORTS_DIR / "global_confluence_metrics.csv"
RELATIVE_METRICS_PATH = REPORTS_DIR / "relative_strength_btc_metrics.csv"

TRADE_FIELDS = [
    "event_id",
    "opened_at",
    "closed_at",
    "reason",
    "entry_price",
    "exit_price",
    "quantity",
    "fraction_closed",
    "gross_pnl_eur",
    "entry_fee_allocated_eur",
    "exit_fee_eur",
    "funding_allocated_eur",
    "net_pnl_eur",
    "remaining_quantity",
    "balance_eur",
]

DEFAULT_CONFIG: dict[str, Any] = {
    "schema_version": 1,
    "enabled": True,
    "paper_only": True,
    "asset": "DOGE",
    "symbol": "DOGE-USDT",
    "timeframe_minutes": 15,
    "initial_capital_eur": 3600.0,
    "fixed_margin_eur": 3600.0,
    "leverage": 5.0,
    "prealert_price": 0.0765,
    "armed_price": 0.0775,
    "trigger_price": 0.0780,
    "entry_min_price": 0.0770,
    "entry_max_price": 0.0785,
    "resistance_price": 0.07923,
    "bearish_invalidation_close": 0.07966,
    "minimum_stop_price": 0.08060,
    "maximum_stop_price": 0.08120,
    "stop_above_rejection_high_pct": 0.002,
    "rearm_below_price": 0.07550,
    "btc_breakout_filter": 65544.0,
    "minimum_global_score": -5.0,
    "maximum_classic_raw_score": -5.0,
    "maximum_relative_raw_score": -5.0,
    "minimum_upper_wick_ratio": 0.30,
    "maximum_normal_volume_ratio": 1.80,
    "high_volume_close_location_max": 0.35,
    "entry_slippage_bps": 2.0,
    "exit_slippage_bps": 2.0,
    "taker_fee_bps": 6.0,
    "liquidation_buffer_fraction": 0.005,
    "max_holding_hours": 168,
    "cooldown_hours": 24,
    "targets": [
        {"name": "TP1", "price": 0.07107, "fraction": 0.25},
        {"name": "TP2", "price": 0.06961, "fraction": 0.25},
        {"name": "TP3", "price": 0.06400, "fraction": 0.25},
        {"name": "TP4", "price": 0.06000, "fraction": 0.25},
    ],
}


def now_utc() -> datetime:
    return datetime.now(timezone.utc)


def iso_utc(value: datetime | None = None) -> str:
    return (value or now_utc()).astimezone(timezone.utc).isoformat(timespec="seconds")


def parse_time(value: Any) -> datetime | None:
    if not value:
        return None
    try:
        parsed = datetime.fromisoformat(str(value).replace("Z", "+00:00"))
        if parsed.tzinfo is None:
            parsed = parsed.replace(tzinfo=timezone.utc)
        return parsed.astimezone(timezone.utc)
    except Exception:
        return None


def safe_float(value: Any, default: float = 0.0) -> float:
    try:
        number = float(value)
        return number if math.isfinite(number) else default
    except Exception:
        return default


def fmt_eur(value: Any, signed: bool = False) -> str:
    number = safe_float(value)
    prefix = "+" if signed and number > 0 else ""
    rendered = f"{prefix}€{number:,.2f}"
    return rendered.replace(",", "X").replace(".", ",").replace("X", ".")


def fmt_price(value: Any) -> str:
    number = safe_float(value)
    return f"{number:.6f}".rstrip("0").rstrip(".")


def md_table(headers: list[str], rows: list[list[Any]]) -> str:
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(["---"] * len(headers)) + " |",
    ]
    lines.extend("| " + " | ".join(str(value) for value in row) + " |" for row in rows)
    return "\n".join(lines)


def load_config() -> dict[str, Any]:
    config = json.loads(json.dumps(DEFAULT_CONFIG))
    if CONFIG_PATH.exists():
        try:
            override = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
            if isinstance(override, dict):
                config.update(override)
        except Exception:
            pass
    return config


def initial_state(config: dict[str, Any], when: datetime) -> dict[str, Any]:
    capital = float(config["initial_capital_eur"])
    return {
        "schema_version": 1,
        "created_utc": iso_utc(when),
        "updated_utc": iso_utc(when),
        "initial_capital_eur": capital,
        "balance_eur": capital,
        "peak_equity_eur": capital,
        "max_drawdown_pct": 0.0,
        "phase": "WAITING",
        "approach_id": 0,
        "last_candle_time": "",
        "last_prealert_approach": -1,
        "last_armed_approach": -1,
        "last_invalidated_approach": -1,
        "cooldown_until": "",
        "position": None,
        "closed_events": 0,
        "winning_events": 0,
        "gross_profit_eur": 0.0,
        "gross_loss_eur": 0.0,
        "notifications": {"pending": []},
        "last_checks": {},
    }


def load_state(config: dict[str, Any], when: datetime) -> dict[str, Any]:
    if not STATE_PATH.exists():
        return initial_state(config, when)
    try:
        state = json.loads(STATE_PATH.read_text(encoding="utf-8"))
        if not isinstance(state, dict):
            raise ValueError("state non dict")
    except Exception:
        broken = STATE_PATH.with_suffix(".json.broken")
        try:
            STATE_PATH.replace(broken)
        except Exception:
            pass
        return initial_state(config, when)

    base = initial_state(config, when)
    for key, value in base.items():
        state.setdefault(key, value)
    state.setdefault("notifications", {}).setdefault("pending", [])
    state["initial_capital_eur"] = float(config["initial_capital_eur"])
    return state


def save_state(state: dict[str, Any], when: datetime) -> None:
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    state["updated_utc"] = iso_utc(when)
    temp = STATE_PATH.with_suffix(".json.tmp")
    temp.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")
    temp.replace(STATE_PATH)


def append_trade(row: dict[str, Any]) -> None:
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    exists = TRADES_PATH.exists() and TRADES_PATH.stat().st_size > 0
    with TRADES_PATH.open("a", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=TRADE_FIELDS, extrasaction="ignore")
        if not exists:
            writer.writeheader()
        writer.writerow({field: row.get(field, "") for field in TRADE_FIELDS})


def read_latest_row(path: Path, asset: str) -> dict[str, Any]:
    if not path.exists():
        return {}
    try:
        frame = pd.read_csv(path)
    except Exception:
        return {}
    if frame.empty or "asset" not in frame.columns:
        return {}
    subset = frame[frame["asset"].astype(str).str.upper() == asset.upper()]
    if subset.empty:
        return {}
    return subset.iloc[-1].to_dict()


def current_equity(state: dict[str, Any], mark: float, eur_rate: float) -> tuple[float, float]:
    position = state.get("position")
    unrealized = 0.0
    if isinstance(position, dict):
        quantity = safe_float(position.get("remaining_quantity"))
        entry = safe_float(position.get("entry_price"))
        unrealized = (entry - mark) * quantity / max(eur_rate, 1e-12)
    equity = safe_float(state.get("balance_eur")) + unrealized
    return equity, unrealized


def update_drawdown(state: dict[str, Any], equity: float) -> None:
    peak = max(safe_float(state.get("peak_equity_eur"), equity), equity)
    state["peak_equity_eur"] = peak
    drawdown = max(0.0, (peak - equity) / max(peak, 1e-12) * 100.0)
    state["max_drawdown_pct"] = max(safe_float(state.get("max_drawdown_pct")), drawdown)


def queue_message(state: dict[str, Any], event_id: str, text: str) -> None:
    pending = state.setdefault("notifications", {}).setdefault("pending", [])
    if any(str(item.get("id")) == event_id for item in pending):
        return
    pending.append({"id": event_id, "text": text, "created_utc": iso_utc(), "sent": False})


def send_pending(state: dict[str, Any], when: datetime) -> dict[str, Any]:
    token = os.getenv("TELEGRAM_BOT_TOKEN", "").strip()
    chat_id = os.getenv("TELEGRAM_CHAT_ID", "").strip()
    pending = state.setdefault("notifications", {}).setdefault("pending", [])
    result = {"configured": bool(token and chat_id), "sent": 0, "pending": 0}
    if not token or not chat_id:
        result["pending"] = sum(not bool(item.get("sent")) for item in pending)
        return result

    for item in pending:
        if item.get("sent"):
            continue
        response = requests.post(
            f"https://api.telegram.org/bot{token}/sendMessage",
            json={
                "chat_id": chat_id,
                "text": str(item.get("text", "")),
                "disable_web_page_preview": True,
            },
            timeout=20,
        )
        response.raise_for_status()
        item["sent"] = True
        item["sent_utc"] = iso_utc(when)
        result["sent"] += 1
        save_state(state, when)

    # Keep a compact audit trail without growing forever.
    sent_items = [item for item in pending if item.get("sent")][-100:]
    unsent_items = [item for item in pending if not item.get("sent")]
    state["notifications"]["pending"] = sent_items + unsent_items
    result["pending"] = len(unsent_items)
    return result


def static_filters(
    bundle: dict[str, Any],
    config: dict[str, Any],
) -> tuple[bool, dict[str, Any]]:
    global_row = read_latest_row(GLOBAL_METRICS_PATH, "DOGE")
    relative_row = read_latest_row(RELATIVE_METRICS_PATH, "DOGE")
    assets = bundle.get("assets", {})
    doge_mark = safe_float(assets.get("DOGE", {}).get("mark_price"))
    btc_mark = safe_float(assets.get("BTC", {}).get("mark_price"))

    freshness = bundle.get("_paper_freshness", {})
    freshness_status = str(freshness.get("status", "UNKNOWN")).upper()

    global_score = safe_float(
        global_row.get("global_score", global_row.get("score")),
        default=999.0,
    )
    classic_raw = safe_float(global_row.get("classic_technical_raw_score"), default=999.0)
    relative_raw = safe_float(relative_row.get("raw_score"), default=999.0)
    bearish_status = str(global_row.get("technical_dominant_bearish_status", "")).upper()

    checks = {
        "fresh_market": freshness_status == "FRESH",
        "doge_price_available": doge_mark > 0,
        "btc_price_available": btc_mark > 0,
        "global_bearish": global_score <= float(config["minimum_global_score"]),
        "classic_bearish": classic_raw <= float(config["maximum_classic_raw_score"]),
        "relative_weak": relative_raw <= float(config["maximum_relative_raw_score"]),
        "bearish_pattern_valid": bearish_status in {
            "ATTIVO",
            "ACTIVE",
            "CONFERMATO_RECENTE",
            "CONFIRMED_RECENT",
            "MATURO",
            "MATURE",
        },
        "btc_not_breaking_out": 0 < btc_mark < float(config["btc_breakout_filter"]),
    }
    details = {
        "checks": checks,
        "freshness_status": freshness_status,
        "doge_mark": doge_mark,
        "btc_mark": btc_mark,
        "global_score": global_score,
        "classic_raw_score": classic_raw,
        "relative_raw_score": relative_raw,
        "bearish_pattern_status": bearish_status or "n/a",
    }
    return all(checks.values()), details


def _normalise_frame(frame: pd.DataFrame) -> pd.DataFrame:
    output = frame.copy()
    for column in ("open", "high", "low", "close", "volume"):
        if column not in output.columns:
            return pd.DataFrame()
        output[column] = pd.to_numeric(output[column], errors="coerce")
    return output.dropna(subset=["open", "high", "low", "close", "volume"])


def evaluate_rejection(
    frame: pd.DataFrame,
    mark: float,
    config: dict[str, Any],
) -> dict[str, Any]:
    clean = _normalise_frame(frame)
    if len(clean) < 22:
        return {"accepted": False, "reason": "candele 15m insufficienti"}

    candle = clean.iloc[-1]
    previous = clean.iloc[-2]
    prior_volume = clean["volume"].iloc[-21:-1]
    volume_mean = safe_float(prior_volume.mean())
    volume_ratio = (
        safe_float(candle["volume"]) / volume_mean
        if volume_mean > 0
        else 0.0
    )

    open_price = safe_float(candle["open"])
    high = safe_float(candle["high"])
    low = safe_float(candle["low"])
    close = safe_float(candle["close"])
    previous_close = safe_float(previous["close"])
    candle_range = max(high - low, 1e-12)
    upper_wick_ratio = max(0.0, high - max(open_price, close)) / candle_range
    close_location = (close - low) / candle_range
    bearish_confirmation = close < open_price or close < previous_close
    volume_ok = (
        volume_ratio <= float(config["maximum_normal_volume_ratio"])
        or (
            close < open_price
            and close_location <= float(config["high_volume_close_location_max"])
        )
    )
    stop_price = max(
        float(config["minimum_stop_price"]),
        high * (1.0 + float(config["stop_above_rejection_high_pct"])),
    )

    conditions = {
        "trigger_touched": high >= float(config["trigger_price"]),
        "closed_back_below_trigger": close < float(config["trigger_price"]),
        "close_below_invalidation": close < float(config["bearish_invalidation_close"]),
        "entry_not_chased": (
            float(config["entry_min_price"])
            <= mark
            <= float(config["entry_max_price"])
        ),
        "upper_wick": upper_wick_ratio >= float(config["minimum_upper_wick_ratio"]),
        "bearish_confirmation": bearish_confirmation,
        "volume_valid": volume_ok,
        "stop_within_limit": stop_price <= float(config["maximum_stop_price"]),
    }
    return {
        "accepted": all(conditions.values()),
        "conditions": conditions,
        "candle_time": str(clean.index[-1]),
        "open": open_price,
        "high": high,
        "low": low,
        "close": close,
        "previous_close": previous_close,
        "volume_ratio": volume_ratio,
        "upper_wick_ratio": upper_wick_ratio,
        "close_location": close_location,
        "stop_price": stop_price,
        "reason": "OK" if all(conditions.values()) else ", ".join(
            name for name, passed in conditions.items() if not passed
        ),
    }


def apply_funding(
    state: dict[str, Any],
    bundle: dict[str, Any],
    config: dict[str, Any],
    when: datetime,
) -> None:
    position = state.get("position")
    if not isinstance(position, dict):
        return
    last = parse_time(position.get("last_funding_time")) or parse_time(position.get("opened_at")) or when
    elapsed_hours = max(0.0, (when - last).total_seconds() / 3600.0)
    intervals = int(elapsed_hours // 8)
    if intervals <= 0:
        return
    rate = safe_float(bundle.get("assets", {}).get("DOGE", {}).get("funding_rate"))
    remaining_notional = safe_float(position.get("remaining_notional_eur"))
    # A positive funding rate pays shorts in this simplified paper model.
    funding = remaining_notional * rate * intervals
    state["balance_eur"] = safe_float(state.get("balance_eur")) + funding
    position["funding_pnl_eur"] = safe_float(position.get("funding_pnl_eur")) + funding
    position["last_funding_time"] = iso_utc(last + timedelta(hours=intervals * 8))


def open_position(
    state: dict[str, Any],
    bundle: dict[str, Any],
    config: dict[str, Any],
    rejection: dict[str, Any],
    when: datetime,
) -> dict[str, Any]:
    eur_rate = safe_float(
        bundle.get("eur_usdt_rate"),
        safe_float(config.get("eur_usdt_fallback_rate"), 1.0),
    ) or 1.0
    mark = safe_float(bundle.get("assets", {}).get("DOGE", {}).get("mark_price"))
    slippage = float(config["entry_slippage_bps"]) / 10_000.0
    entry = mark * (1.0 - slippage)
    margin = float(config["fixed_margin_eur"])
    leverage = float(config["leverage"])
    notional_eur = margin * leverage
    notional_usdt = notional_eur * eur_rate
    quantity = notional_usdt / entry
    fee_rate = float(config["taker_fee_bps"]) / 10_000.0
    entry_fee = notional_eur * fee_rate
    stop_price = safe_float(rejection["stop_price"])
    liquidation_distance = max(
        0.001,
        1.0 / leverage - float(config["liquidation_buffer_fraction"]),
    )
    liquidation_price = entry * (1.0 + liquidation_distance)
    event_id = f"DOGE_REJECTION_SHORT_{when.strftime('%Y%m%dT%H%M%SZ')}"
    targets = []
    for row in config["targets"]:
        targets.append(
            {
                "name": str(row["name"]),
                "price": float(row["price"]),
                "fraction": float(row["fraction"]),
                "filled": False,
            }
        )

    position = {
        "event_id": event_id,
        "opened_at": iso_utc(when),
        "entry_price": entry,
        "original_quantity": quantity,
        "remaining_quantity": quantity,
        "original_notional_eur": notional_eur,
        "remaining_notional_eur": notional_eur,
        "margin_eur": margin,
        "leverage": leverage,
        "initial_stop_price": stop_price,
        "stop_price": stop_price,
        "liquidation_price": liquidation_price,
        "entry_fee_eur": entry_fee,
        "entry_fee_remaining_eur": entry_fee,
        "funding_pnl_eur": 0.0,
        "last_funding_time": iso_utc(when),
        "targets": targets,
        "rejection": rejection,
    }
    state["balance_eur"] = safe_float(state.get("balance_eur")) - entry_fee
    state["position"] = position
    state["phase"] = "OPEN"

    risk_eur = max(0.0, (stop_price - entry) * quantity / eur_rate) + entry_fee
    potential_eur = max(0.0, (entry - float(config["targets"][-1]["price"])) * quantity / eur_rate)
    queue_message(
        state,
        f"{event_id}:OPEN",
        "\n".join(
            [
                "🔴 DOGE REJECTION SHORT — ENTRATA PAPER",
                "Nessun ordine reale è stato inviato.",
                f"Capitale separato: {fmt_eur(config['initial_capital_eur'])}",
                f"Margine: {fmt_eur(margin)} · Leva: {leverage:.1f}x",
                f"Esposizione: {fmt_eur(notional_eur)}",
                f"Entry simulata: {fmt_price(entry)}",
                f"Stop iniziale: {fmt_price(stop_price)}",
                f"Liquidazione stimata: {fmt_price(liquidation_price)}",
                "Target: 0,07107 / 0,06961 / 0,064 / 0,060",
                f"Rischio stimato allo stop: {fmt_eur(risk_eur)}",
                f"Profitto lordo potenziale a 0,060: {fmt_eur(potential_eur)}",
                (
                    "Conferme: wick superiore "
                    f"{rejection['upper_wick_ratio'] * 100:.1f}% · "
                    f"volume x{rejection['volume_ratio']:.2f} · "
                    "chiusura 15m respinta."
                ),
            ]
        ),
    )
    return position


def close_quantity(
    state: dict[str, Any],
    bundle: dict[str, Any],
    config: dict[str, Any],
    raw_exit: float,
    quantity: float,
    reason: str,
    when: datetime,
) -> dict[str, Any]:
    position = state.get("position")
    if not isinstance(position, dict):
        return {}
    remaining_before = safe_float(position.get("remaining_quantity"))
    quantity = min(max(0.0, quantity), remaining_before)
    if quantity <= 0:
        return {}

    eur_rate = safe_float(bundle.get("eur_usdt_rate"), 1.0) or 1.0
    exit_slippage = float(config["exit_slippage_bps"]) / 10_000.0
    exit_price = raw_exit * (1.0 + exit_slippage)
    entry = safe_float(position.get("entry_price"))
    gross = (entry - exit_price) * quantity / eur_rate
    exit_notional_eur = exit_price * quantity / eur_rate
    exit_fee = exit_notional_eur * float(config["taker_fee_bps"]) / 10_000.0

    fraction_of_remaining = quantity / max(remaining_before, 1e-12)
    entry_fee_remaining = safe_float(position.get("entry_fee_remaining_eur"))
    entry_fee_allocated = entry_fee_remaining * fraction_of_remaining
    funding_remaining = safe_float(position.get("funding_pnl_eur"))
    funding_allocated = funding_remaining * fraction_of_remaining

    net = gross - exit_fee - entry_fee_allocated + funding_allocated
    state["balance_eur"] = safe_float(state.get("balance_eur")) + gross - exit_fee + funding_allocated
    position["remaining_quantity"] = max(0.0, remaining_before - quantity)
    position["remaining_notional_eur"] = (
        safe_float(position.get("original_notional_eur"))
        * position["remaining_quantity"]
        / max(safe_float(position.get("original_quantity")), 1e-12)
    )
    position["entry_fee_remaining_eur"] = max(0.0, entry_fee_remaining - entry_fee_allocated)
    position["funding_pnl_eur"] = funding_remaining - funding_allocated

    record = {
        "event_id": position.get("event_id"),
        "opened_at": position.get("opened_at"),
        "closed_at": iso_utc(when),
        "reason": reason,
        "entry_price": entry,
        "exit_price": exit_price,
        "quantity": quantity,
        "fraction_closed": quantity / max(safe_float(position.get("original_quantity")), 1e-12),
        "gross_pnl_eur": gross,
        "entry_fee_allocated_eur": entry_fee_allocated,
        "exit_fee_eur": exit_fee,
        "funding_allocated_eur": funding_allocated,
        "net_pnl_eur": net,
        "remaining_quantity": position["remaining_quantity"],
        "balance_eur": state["balance_eur"],
    }
    append_trade(record)
    return record


def finalise_position(
    state: dict[str, Any],
    total_event_net: float,
    when: datetime,
    config: dict[str, Any],
) -> None:
    state["closed_events"] = int(state.get("closed_events", 0)) + 1
    if total_event_net > 0:
        state["winning_events"] = int(state.get("winning_events", 0)) + 1
        state["gross_profit_eur"] = safe_float(state.get("gross_profit_eur")) + total_event_net
    else:
        state["gross_loss_eur"] = safe_float(state.get("gross_loss_eur")) + abs(total_event_net)
    state["position"] = None
    state["phase"] = "COOLDOWN"
    state["cooldown_until"] = iso_utc(
        when + timedelta(hours=float(config["cooldown_hours"]))
    )


def event_net_from_log(event_id: str) -> float:
    if not TRADES_PATH.exists():
        return 0.0
    try:
        frame = pd.read_csv(TRADES_PATH)
    except Exception:
        return 0.0
    if frame.empty or "event_id" not in frame.columns:
        return 0.0
    subset = frame[frame["event_id"].astype(str) == str(event_id)]
    return float(pd.to_numeric(subset.get("net_pnl_eur"), errors="coerce").fillna(0.0).sum())


def manage_position(
    state: dict[str, Any],
    bundle: dict[str, Any],
    frame: pd.DataFrame | None,
    config: dict[str, Any],
    when: datetime,
) -> dict[str, Any]:
    position = state.get("position")
    if not isinstance(position, dict) or frame is None:
        return {"events": []}
    clean = _normalise_frame(frame)
    if clean.empty:
        return {"events": []}

    apply_funding(state, bundle, config, when)
    candle = clean.iloc[-1]
    candle_time = str(clean.index[-1])
    if str(position.get("last_processed_candle", "")) == candle_time:
        return {"events": []}
    position["last_processed_candle"] = candle_time

    high = safe_float(candle["high"])
    low = safe_float(candle["low"])
    candle_open = safe_float(candle["open"])
    mark = safe_float(bundle.get("assets", {}).get("DOGE", {}).get("mark_price"))
    stop = safe_float(position.get("stop_price"))
    liquidation = safe_float(position.get("liquidation_price"))
    event_id = str(position.get("event_id"))
    events: list[dict[str, Any]] = []

    # Conservative policy: liquidation gap, then stop, then targets.
    if candle_open >= liquidation:
        qty = safe_float(position.get("remaining_quantity"))
        record = close_quantity(
            state, bundle, config, liquidation, qty, "LIQUIDATION_GAP", when
        )
        events.append(record)
    elif high >= stop:
        qty = safe_float(position.get("remaining_quantity"))
        record = close_quantity(state, bundle, config, stop, qty, "STOP", when)
        events.append(record)
    else:
        original_qty = safe_float(position.get("original_quantity"))
        for index, target in enumerate(position.get("targets", [])):
            if target.get("filled") or low > float(target["price"]):
                continue
            desired_qty = original_qty * float(target["fraction"])
            qty = min(desired_qty, safe_float(position.get("remaining_quantity")))
            record = close_quantity(
                state,
                bundle,
                config,
                float(target["price"]),
                qty,
                str(target["name"]),
                when,
            )
            target["filled"] = True
            events.append(record)
            if index == 0:
                cost_buffer = (
                    float(config["entry_slippage_bps"])
                    + float(config["exit_slippage_bps"])
                    + 2.0 * float(config["taker_fee_bps"])
                ) / 10_000.0
                old_stop = safe_float(position.get("stop_price"))
                new_stop = min(old_stop, safe_float(position.get("entry_price")) * (1.0 - cost_buffer))
                position["stop_price"] = new_stop
                queue_message(
                    state,
                    f"{event_id}:STOP_AFTER_TP1",
                    "\n".join(
                        [
                            "🛡️ DOGE SHORT — TP1 RAGGIUNTO",
                            f"Uscito 25% a {fmt_price(target['price'])}.",
                            f"Stop residuo spostato al pareggio costi: {fmt_price(new_stop)}.",
                        ]
                    ),
                )
            elif index == 1:
                old_stop = safe_float(position.get("stop_price"))
                new_stop = min(old_stop, float(config["targets"][0]["price"]))
                position["stop_price"] = new_stop
                queue_message(
                    state,
                    f"{event_id}:STOP_AFTER_TP2",
                    "\n".join(
                        [
                            "🛡️ DOGE SHORT — TP2 RAGGIUNTO",
                            f"Uscito un altro 25% a {fmt_price(target['price'])}.",
                            f"Stop residuo spostato a {fmt_price(new_stop)}.",
                        ]
                    ),
                )
            elif index == 2:
                old_stop = safe_float(position.get("stop_price"))
                new_stop = min(old_stop, float(config["targets"][1]["price"]))
                position["stop_price"] = new_stop
                queue_message(
                    state,
                    f"{event_id}:STOP_AFTER_TP3",
                    "\n".join(
                        [
                            "🛡️ DOGE SHORT — TP3 RAGGIUNTO",
                            f"Uscito un altro 25% a {fmt_price(target['price'])}.",
                            f"Stop residuo spostato a {fmt_price(new_stop)}.",
                        ]
                    ),
                )
            if safe_float(position.get("remaining_quantity")) <= 1e-12:
                break

    position = state.get("position")
    if isinstance(position, dict) and safe_float(position.get("remaining_quantity")) > 1e-12:
        opened = parse_time(position.get("opened_at")) or when
        if (when - opened).total_seconds() / 3600.0 >= float(config["max_holding_hours"]):
            qty = safe_float(position.get("remaining_quantity"))
            events.append(
                close_quantity(state, bundle, config, mark, qty, "TIME_EXIT", when)
            )

    position = state.get("position")
    if isinstance(position, dict) and safe_float(position.get("remaining_quantity")) <= 1e-12:
        total_net = event_net_from_log(event_id)
        finalise_position(state, total_net, when, config)
        queue_message(
            state,
            f"{event_id}:CLOSED",
            "\n".join(
                [
                    "🏁 DOGE REJECTION SHORT — POSIZIONE CHIUSA",
                    f"P&L netto complessivo: {fmt_eur(total_net, signed=True)}",
                    f"Capitale/equity realizzato: {fmt_eur(state.get('balance_eur'))}",
                    "Il conto resta separato dagli altri portafogli paper.",
                ]
            ),
        )
    elif events:
        last = events[-1]
        queue_message(
            state,
            f"{event_id}:FILL:{last.get('reason')}:{last.get('closed_at')}",
            "\n".join(
                [
                    f"📉 DOGE SHORT — {last.get('reason')}",
                    f"Exit simulata: {fmt_price(last.get('exit_price'))}",
                    f"P&L netto tranche: {fmt_eur(last.get('net_pnl_eur'), signed=True)}",
                    (
                        "Quantità residua: "
                        f"{safe_float(state.get('position', {}).get('remaining_quantity')):,.0f} DOGE"
                    ),
                ]
            ),
        )
    return {"events": events}


def render_report(
    state: dict[str, Any],
    bundle: dict[str, Any],
    config: dict[str, Any],
    static: dict[str, Any],
    rejection: dict[str, Any],
    when: datetime,
) -> str:
    mark = safe_float(bundle.get("assets", {}).get("DOGE", {}).get("mark_price"))
    eur_rate = safe_float(bundle.get("eur_usdt_rate"), 1.0) or 1.0
    equity, unrealized = current_equity(state, mark, eur_rate)
    update_drawdown(state, equity)
    position = state.get("position")
    closed_events = int(state.get("closed_events", 0))
    wins = int(state.get("winning_events", 0))
    win_rate = wins / closed_events * 100.0 if closed_events else 0.0
    profit = safe_float(state.get("gross_profit_eur"))
    loss = safe_float(state.get("gross_loss_eur"))
    pf = profit / loss if loss > 0 else (math.inf if profit > 0 else 0.0)

    lines = [
        "## 🎯 DOGE Rejection Short — conto dedicato €3.600",
        "",
        (
            "Simulazione separata **paper only**: capitale/margine iniziale "
            "**€3.600**, leva **5x**, esposizione iniziale **€18.000**. "
            "Non modifica i conti paper da €10.000 e non invia ordini reali."
        ),
        "",
        f"- Stato: **{state.get('phase', 'UNKNOWN')}**",
        f"- Prezzo DOGE: **{fmt_price(mark)}**",
        (
            f"- Pre-allarme: **{fmt_price(config['prealert_price'])}**; "
            f"zona armata: **{fmt_price(config['armed_price'])}**; "
            f"trigger rejection: **{fmt_price(config['trigger_price'])}**"
        ),
        (
            f"- Invalidazione prima dell’entrata: chiusura 15m sopra "
            f"**{fmt_price(config['bearish_invalidation_close'])}**"
        ),
        "",
        md_table(
            ["Capitale iniziale", "Balance", "Equity", "P&L aperto", "Eventi chiusi", "Win rate", "PF", "Max DD"],
            [[
                fmt_eur(config["initial_capital_eur"]),
                fmt_eur(state.get("balance_eur")),
                fmt_eur(equity),
                fmt_eur(unrealized, signed=True),
                closed_events,
                f"{win_rate:.2f}%".replace(".", ","),
                "∞" if math.isinf(pf) else f"{pf:.2f}".replace(".", ","),
                f"{safe_float(state.get('max_drawdown_pct')):.2f}%".replace(".", ","),
            ]],
        ),
        "",
        "### Filtri correnti",
        "",
        md_table(
            ["Filtro", "Valore", "Stato"],
            [
                ["Dati mercato", static.get("freshness_status", "n/a"), "OK" if static.get("checks", {}).get("fresh_market") else "NO"],
                ["Candela 15m", f"{safe_float(static.get('candle_age_minutes'), math.inf):.1f} min", "OK" if static.get("checks", {}).get("candle_15m_fresh") else "NO"],
                ["Global DOGE", static.get("global_score", "n/a"), "OK" if static.get("checks", {}).get("global_bearish") else "NO"],
                ["Classic raw", static.get("classic_raw_score", "n/a"), "OK" if static.get("checks", {}).get("classic_bearish") else "NO"],
                ["DOGE/BTC raw", static.get("relative_raw_score", "n/a"), "OK" if static.get("checks", {}).get("relative_weak") else "NO"],
                ["Pattern ribassista", static.get("bearish_pattern_status", "n/a"), "OK" if static.get("checks", {}).get("bearish_pattern_valid") else "NO"],
                ["BTC sotto filtro", fmt_price(static.get("btc_mark")), "OK" if static.get("checks", {}).get("btc_not_breaking_out") else "NO"],
            ],
        ),
        "",
    ]

    if isinstance(position, dict):
        targets_text = " / ".join(
            f"{target['name']} {fmt_price(target['price'])}{' ✅' if target.get('filled') else ''}"
            for target in position.get("targets", [])
        )
        lines.extend(
            [
                "### Posizione aperta",
                "",
                md_table(
                    ["Entry", "Mark", "Stop", "Liquidazione", "Margine", "Esposizione", "Quantità residua", "P&L aperto"],
                    [[
                        fmt_price(position.get("entry_price")),
                        fmt_price(mark),
                        fmt_price(position.get("stop_price")),
                        fmt_price(position.get("liquidation_price")),
                        fmt_eur(position.get("margin_eur")),
                        fmt_eur(position.get("remaining_notional_eur")),
                        f"{safe_float(position.get('remaining_quantity')):,.0f}",
                        fmt_eur(unrealized, signed=True),
                    ]],
                ),
                "",
                f"- Target: **{targets_text}**",
                "",
            ]
        )
    else:
        lines.extend(
            [
                "### Ultima candela 15m valutata",
                "",
                (
                    f"- Rejection accettata: **{'SI' if rejection.get('accepted') else 'NO'}**; "
                    f"motivo: **{rejection.get('reason', 'n/a')}**"
                ),
                (
                    f"- High **{fmt_price(rejection.get('high'))}**; "
                    f"close **{fmt_price(rejection.get('close'))}**; "
                    f"wick alta **{safe_float(rejection.get('upper_wick_ratio')) * 100:.1f}%**; "
                    f"volume **x{safe_float(rejection.get('volume_ratio')):.2f}**"
                ),
                "",
            ]
        )

    lines.extend(
        [
            "### Gestione",
            "",
            "- TP1 0,07107: chiude 25% e porta lo stop residuo al pareggio costi.",
            "- TP2 0,06961: chiude 25% e porta lo stop residuo a TP1.",
            "- TP3 0,06400: chiude 25% e porta lo stop residuo a TP2.",
            "- TP4 0,06000: chiude l’ultimo 25%.",
            "- Stop iniziale dinamico: almeno 0,08060, sopra il massimo della rejection con buffer 0,2%, mai oltre 0,08120.",
            "- Politica conservativa: se stop e target sono toccati nella stessa candela, prevale lo stop.",
            "",
        ]
    )
    report = "\n".join(lines).rstrip() + "\n"
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(report, encoding="utf-8")
    return report


def run_doge_rejection_cycle(
    bundle: dict[str, Any],
    paper_config: dict[str, Any] | None = None,
    when: datetime | None = None,
) -> dict[str, Any]:
    from kucoin_public_data import bundle_frames

    current = (when or now_utc()).astimezone(timezone.utc)
    config = load_config()
    state = load_state(config, current)
    frames = bundle_frames(bundle)
    frame = frames.get("DOGE", {}).get(int(config["timeframe_minutes"]))
    mark = safe_float(bundle.get("assets", {}).get("DOGE", {}).get("mark_price"))
    static_ok, static = static_filters(bundle, config)

    candle_age_minutes = math.inf
    if frame is None or frame.empty:
        rejection = {"accepted": False, "reason": "frame DOGE 15m non disponibile"}
        candle_fresh = False
    else:
        rejection = evaluate_rejection(frame, mark, config)
        try:
            candle_time = pd.Timestamp(frame.index[-1])
            if candle_time.tzinfo is None:
                candle_time = candle_time.tz_localize("UTC")
            candle_age_minutes = max(
                0.0,
                (pd.Timestamp(current) - candle_time.tz_convert("UTC")).total_seconds() / 60.0,
            )
        except Exception:
            candle_age_minutes = math.inf
        candle_fresh = candle_age_minutes <= 40.0

    static.setdefault("checks", {})["candle_15m_fresh"] = candle_fresh
    static["candle_age_minutes"] = candle_age_minutes
    static_ok = static_ok and candle_fresh

    state["last_checks"] = {
        "generated_utc": iso_utc(current),
        "static": static,
        "rejection": rejection,
    }

    # Re-arm only after price has moved clearly away from the setup.
    cooldown_until = parse_time(state.get("cooldown_until"))
    cooldown_complete = cooldown_until is None or current >= cooldown_until
    if (
        not isinstance(state.get("position"), dict)
        and mark > 0
        and mark <= float(config["rearm_below_price"])
        and cooldown_complete
        and state.get("phase") in {"PREALERT", "ARMED", "INVALIDATED", "COOLDOWN"}
    ):
        state["phase"] = "WAITING"
        state["approach_id"] = int(state.get("approach_id", 0)) + 1

    opened_this_cycle = 0
    if isinstance(state.get("position"), dict):
        management = manage_position(state, bundle, frame, config, current)
    else:
        management = {"events": []}
        approach_id = int(state.get("approach_id", 0))
        last_candle_time = str(rejection.get("candle_time", ""))

        invalidated = (
            last_candle_time
            and safe_float(rejection.get("close"))
            >= float(config["bearish_invalidation_close"])
        )
        if invalidated:
            if int(state.get("last_invalidated_approach", -1)) != approach_id:
                state["last_invalidated_approach"] = approach_id
                state["phase"] = "INVALIDATED"
                queue_message(
                    state,
                    f"APPROACH:{approach_id}:INVALIDATED",
                    "\n".join(
                        [
                            "⛔ DOGE SHORT — SETUP ANNULLATO",
                            (
                                f"La candela 15m ha chiuso a {fmt_price(rejection.get('close'))}, "
                                "sopra l’invalidazione 0,07966."
                            ),
                            "Nessuna posizione è stata aperta. Il bot aspetterà un nuovo riarmo.",
                        ]
                    ),
                )
        else:
            entry_ready = (
                static_ok
                and rejection.get("accepted")
                and last_candle_time
                and str(state.get("last_candle_time", "")) != last_candle_time
                and state.get("phase") != "COOLDOWN"
            )
            if entry_ready:
                state["last_candle_time"] = last_candle_time
                open_position(state, bundle, config, rejection, current)
                opened_this_cycle = 1
            else:
                if static_ok and mark >= float(config["prealert_price"]):
                    if int(state.get("last_prealert_approach", -1)) != approach_id:
                        state["last_prealert_approach"] = approach_id
                        state["phase"] = "PREALERT"
                        queue_message(
                            state,
                            f"APPROACH:{approach_id}:PREALERT",
                            "\n".join(
                                [
                                    "👀 PRE-ALLARME DOGE SHORT",
                                    f"DOGE ha raggiunto {fmt_price(mark)}.",
                                    (
                                        "Si avvicina alla zona 0,0775–0,07923. "
                                        "Nessuna posizione è stata aperta."
                                    ),
                                    (
                                        "Il bot aspetta una rejection su candela 15m, "
                                        "wick superiore, volume non da breakout e chiusura sotto 0,078."
                                    ),
                                    (
                                        f"Global {static['global_score']:+.0f} · "
                                        f"DOGE/BTC raw {static['relative_raw_score']:+.0f} · "
                                        f"BTC {fmt_price(static['btc_mark'])}."
                                    ),
                                ]
                            ),
                        )

                zone_reached = (
                    mark >= float(config["armed_price"])
                    or safe_float(rejection.get("high")) >= float(config["armed_price"])
                )
                if static_ok and zone_reached:
                    if int(state.get("last_armed_approach", -1)) != approach_id:
                        state["last_armed_approach"] = approach_id
                        state["phase"] = "ARMED"
                        queue_message(
                            state,
                            f"APPROACH:{approach_id}:ARMED",
                            "\n".join(
                                [
                                    "⚠️ DOGE SHORT — ZONA RAGGIUNTA",
                                    f"Prezzo/High osservato: {fmt_price(max(mark, safe_float(rejection.get('high'))))}",
                                    "Setup armato, ma ancora nessuna entrata.",
                                    (
                                        "Attendo la chiusura 15m sotto 0,078 senza breakout "
                                        "rialzista confermato sopra 0,07966."
                                    ),
                                ]
                            ),
                        )

    equity, unrealized = current_equity(
        state,
        mark,
        safe_float(bundle.get("eur_usdt_rate"), 1.0) or 1.0,
    )
    update_drawdown(state, equity)
    report = render_report(state, bundle, config, static, rejection, current)
    latest = {
        "generated_utc": iso_utc(current),
        "phase": state.get("phase"),
        "mark_price": mark,
        "equity_eur": equity,
        "unrealized_pnl_eur": unrealized,
        "position_open": isinstance(state.get("position"), dict),
        "static_filters_ok": static_ok,
        "rejection_accepted": bool(rejection.get("accepted")),
        "telegram": {},
    }
    LATEST_PATH.write_text(json.dumps(latest, ensure_ascii=False, indent=2), encoding="utf-8")
    save_state(state, current)
    try:
        telegram = send_pending(state, current)
    except Exception as exc:
        telegram = {"configured": True, "sent": 0, "error": str(exc)}
    latest["telegram"] = telegram
    LATEST_PATH.write_text(json.dumps(latest, ensure_ascii=False, indent=2), encoding="utf-8")
    save_state(state, current)

    return {
        "report_markdown": report,
        "phase": state.get("phase"),
        "position_open": isinstance(state.get("position"), dict),
        "equity_eur": equity,
        "opened_this_cycle": opened_this_cycle,
        "management_events": len(management.get("events", [])),
        "telegram": telegram,
    }


if __name__ == "__main__":
    raise SystemExit(
        "Questo modulo viene eseguito da paper_trading_runner.py; non invia ordini reali."
    )
