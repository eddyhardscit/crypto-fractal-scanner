# -*- coding: utf-8 -*-
"""Persistent, fully automatic paper-trading execution engine."""

from __future__ import annotations

import csv
import json
import math
import os
from dataclasses import asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import pandas as pd

from kucoin_public_data import bundle_frames, safe_float
from paper_signal_engine import Signal
from paper_trading_config import public_config_snapshot

REPORTS_DIR = Path("reports")
STATE_PATH = REPORTS_DIR / "paper_trading_state.json"
TRADE_LOG_PATH = REPORTS_DIR / "paper_trading_trade_log.csv"
SIGNAL_LOG_PATH = REPORTS_DIR / "paper_trading_signal_log.csv"
EQUITY_LOG_PATH = REPORTS_DIR / "paper_trading_equity.csv"
OPEN_POSITIONS_PATH = REPORTS_DIR / "paper_trading_open_positions.csv"
CONFIG_SNAPSHOT_PATH = REPORTS_DIR / "paper_trading_config_snapshot.json"

TRADE_FIELDS = [
    "trade_id", "experiment_group_id", "portfolio", "is_main", "strategy", "asset", "symbol", "side",
    "timeframe_minutes", "opened_at", "closed_at", "holding_hours", "entry_price", "exit_price",
    "quantity", "notional_eur", "margin_eur", "leverage", "liquidation_price", "initial_stop_price", "final_stop_price",
    "target_price", "gross_pnl_eur", "entry_fee_eur", "exit_fee_eur", "funding_pnl_eur",
    "net_pnl_eur", "return_on_margin_pct", "r_multiple",
    "max_favorable_price", "max_adverse_price",
    "mfe_gross_eur", "mae_gross_eur", "mfe_net_eur", "mae_net_eur",
    "profit_retained_pct", "peak_profit_giveback_eur",
    "close_reason", "signal_score", "confidence",
    "source", "eur_usdt_rate"
]
SIGNAL_FIELDS = [
    "processed_at", "signal_id", "experiment_group_id", "portfolio", "is_main", "strategy", "asset",
    "symbol", "timeframe_minutes", "candle_time", "side", "score", "confidence", "entry_reference_price",
    "stop_pct", "target_pct", "relative_strength_score", "breakout_state", "decision", "decision_reason"
]
EQUITY_FIELDS = [
    "generated_utc", "portfolio", "is_main", "balance_eur", "unrealized_pnl_eur", "equity_eur",
    "peak_equity_eur", "drawdown_pct", "month_start_equity_eur", "month_pnl_eur", "monthly_target_eur",
    "target_progress_pct", "open_positions", "closed_trades", "win_rate_pct", "profit_factor",
    "max_drawdown_pct"
]


def now_utc() -> datetime:
    return datetime.now(timezone.utc)


def iso_utc(value: datetime | None = None) -> str:
    return (value or now_utc()).isoformat(timespec="seconds")


def parse_time(value: Any) -> datetime:
    timestamp = pd.Timestamp(value)
    if timestamp.tzinfo is None:
        timestamp = timestamp.tz_localize("UTC")
    return timestamp.to_pydatetime()


def append_csv(path: Path, fieldnames: list[str], row: dict[str, Any]) -> None:
    # TRADE_LOG_SCHEMA_GUARD_V1
    if path == TRADE_LOG_PATH:
        from paper_trading_trade_log_repair import (
            ensure_trade_log_schema,
        )
        ensure_trade_log_schema(path, fieldnames)
    path.parent.mkdir(parents=True, exist_ok=True)
    exists = path.exists() and path.stat().st_size > 0
    with path.open("a", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
        if not exists:
            writer.writeheader()
        writer.writerow({field: row.get(field, "") for field in fieldnames})


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_suffix(path.suffix + ".tmp")
    with temp.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fieldnames})
    temp.replace(path)


def week_key(value: datetime) -> str:
    year, week, _ = value.isocalendar()
    return f"{year}-W{week:02d}"


def month_key(value: datetime) -> str:
    return value.strftime("%Y-%m")


def day_key(value: datetime) -> str:
    return value.strftime("%Y-%m-%d")


def new_portfolio_state(portfolio: dict[str, Any], capital: float, when: datetime) -> dict[str, Any]:
    return {
        "name": portfolio["name"],
        "is_main": bool(portfolio.get("is_main")),
        "strategy": portfolio.get("strategy", ""),
        "balance_eur": capital,
        "peak_equity_eur": capital,
        "max_drawdown_pct": 0.0,
        "open_positions": [],
        "seen_signal_ids": [],
        "closed_trades": 0,
        "winning_trades": 0,
        "gross_profit_eur": 0.0,
        "gross_loss_eur": 0.0,
        "periods": {
            "day_key": day_key(when),
            "day_start_equity_eur": capital,
            "week_key": week_key(when),
            "week_start_equity_eur": capital,
            "month_key": month_key(when),
            "month_start_equity_eur": capital,
        },
    }


def initial_state(config: dict[str, Any], when: datetime | None = None) -> dict[str, Any]:
    current = when or now_utc()
    capital = float(config["initial_capital_eur"])
    portfolios = {
        p["name"]: new_portfolio_state(p, capital, current)
        for p in config.get("portfolios", []) if p.get("enabled", True)
    }
    return {
        "schema_version": 1,
        "created_utc": iso_utc(current),
        "updated_utc": iso_utc(current),
        "initial_capital_eur": capital,
        "config_snapshot": public_config_snapshot(config),
        "portfolios": portfolios,
    }


def load_state(config: dict[str, Any], when: datetime | None = None) -> dict[str, Any]:
    reset = os.getenv("PAPER_RESET_STATE", "").strip().lower() in {"1", "true", "yes"}
    if reset or not STATE_PATH.exists():
        return initial_state(config, when)
    try:
        state = json.loads(STATE_PATH.read_text(encoding="utf-8"))
    except Exception:
        broken = STATE_PATH.with_suffix(".json.broken")
        STATE_PATH.replace(broken)
        return initial_state(config, when)

    current = when or now_utc()
    capital = float(state.get("initial_capital_eur", config["initial_capital_eur"]))
    for portfolio in config.get("portfolios", []):
        if not portfolio.get("enabled", True):
            continue
        state.setdefault("portfolios", {})
        if portfolio["name"] not in state["portfolios"]:
            state["portfolios"][portfolio["name"]] = new_portfolio_state(portfolio, capital, current)
    # CONFIG_PORTFOLIO_ORDER_V2
    existing_portfolios = dict(state.setdefault("portfolios", {}))
    ordered_portfolios: dict[str, Any] = {}
    for definition in config.get("portfolios", []):
        if not definition.get("enabled", True):
            continue
        name = str(definition.get("name", ""))
        if name in existing_portfolios:
            ordered_portfolios[name] = existing_portfolios[name]
    for name, value in existing_portfolios.items():
        if name not in ordered_portfolios:
            ordered_portfolios[name] = value
    state["portfolios"] = ordered_portfolios
    state["config_snapshot"] = public_config_snapshot(config)
    return state


def save_state(state: dict[str, Any], config: dict[str, Any], when: datetime | None = None) -> None:
    current = when or now_utc()
    state["updated_utc"] = iso_utc(current)
    state["config_snapshot"] = public_config_snapshot(config)
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    temp = STATE_PATH.with_suffix(".json.tmp")
    temp.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")
    temp.replace(STATE_PATH)
    CONFIG_SNAPSHOT_PATH.write_text(
        json.dumps(public_config_snapshot(config), ensure_ascii=False, indent=2), encoding="utf-8"
    )


def current_prices(bundle: dict[str, Any]) -> dict[str, float]:
    output: dict[str, float] = {}
    for asset, payload in bundle.get("assets", {}).items():
        price = safe_float(payload.get("mark_price"))
        if math.isfinite(price) and price > 0:
            output[asset] = price
    return output


def position_unrealized(position: dict[str, Any], mark_price: float, eur_usdt_rate: float) -> float:
    quantity = float(position["quantity"])
    direction = 1.0 if position["side"] == "LONG" else -1.0
    gross_usdt = (mark_price - float(position["entry_price"])) * quantity * direction
    return gross_usdt / eur_usdt_rate


def portfolio_equity(portfolio: dict[str, Any], prices: dict[str, float], eur_usdt_rate: float) -> tuple[float, float]:
    unrealized = 0.0
    for position in portfolio.get("open_positions", []):
        mark = prices.get(position["asset"], float(position["entry_price"]))
        unrealized += position_unrealized(position, mark, eur_usdt_rate)
    return float(portfolio["balance_eur"]) + unrealized, unrealized


def roll_periods(portfolio: dict[str, Any], equity: float, when: datetime) -> None:
    periods = portfolio.setdefault("periods", {})
    if periods.get("day_key") != day_key(when):
        periods["day_key"] = day_key(when)
        periods["day_start_equity_eur"] = equity
    if periods.get("week_key") != week_key(when):
        periods["week_key"] = week_key(when)
        periods["week_start_equity_eur"] = equity
    if periods.get("month_key") != month_key(when):
        periods["month_key"] = month_key(when)
        periods["month_start_equity_eur"] = equity


def update_drawdown(portfolio: dict[str, Any], equity: float) -> None:
    portfolio["peak_equity_eur"] = max(float(portfolio.get("peak_equity_eur", equity)), equity)
    peak = float(portfolio["peak_equity_eur"])
    drawdown = max(0.0, (peak - equity) / peak) if peak > 0 else 0.0
    portfolio["max_drawdown_pct"] = max(float(portfolio.get("max_drawdown_pct", 0.0)), drawdown * 100.0)


def effective_risk_fraction(portfolio: dict[str, Any], equity: float, config: dict[str, Any]) -> float:
    base = float(config["risk"]["risk_per_trade"])
    target = float(config.get("monthly_target_eur", 0.0))
    month_start = float(portfolio["periods"].get("month_start_equity_eur", equity))
    month_pnl = equity - month_start
    progress = month_pnl / target if target > 0 else 0.0
    multiplier = 1.0
    for step in sorted(config.get("profit_protection", []), key=lambda item: float(item["target_progress"])):
        if progress >= float(step["target_progress"]):
            multiplier = min(multiplier, float(step["risk_multiplier"]))
    return base * multiplier


def risk_gate(portfolio: dict[str, Any], equity: float, config: dict[str, Any]) -> tuple[bool, str]:
    periods = portfolio["periods"]
    checks = (
        ("daily", float(periods.get("day_start_equity_eur", equity)), float(config["risk"]["max_daily_loss"])),
        ("weekly", float(periods.get("week_start_equity_eur", equity)), float(config["risk"]["max_weekly_loss"])),
        ("monthly", float(periods.get("month_start_equity_eur", equity)), float(config["risk"]["max_monthly_drawdown"])),
    )
    for label, start, limit in checks:
        if start > 0 and (equity / start - 1.0) <= -limit:
            return False, f"blocco perdita {label} raggiunto"
    if equity <= 0:
        return False, "equity non positiva"
    return True, "OK"


def open_risk_eur(portfolio: dict[str, Any]) -> float:
    return sum(float(position.get("initial_risk_eur", 0.0)) for position in portfolio.get("open_positions", []))


def open_margin_eur(portfolio: dict[str, Any]) -> float:
    return sum(float(position.get("margin_eur", 0.0)) for position in portfolio.get("open_positions", []))


def slippage_bps(bundle: dict[str, Any], asset: str, config: dict[str, Any]) -> float:
    payload = bundle.get("assets", {}).get(asset, {})
    turnover = safe_float(payload.get("turnover_24h"), 0.0)
    minimum = float(config["universe"].get("minimum_turnover_24h_usdt", 0.0))
    if minimum > 0 and turnover < minimum * 3:
        return float(config["execution"].get("illiquid_slippage_bps", 6.0))
    return float(config["execution"].get("default_slippage_bps", 2.0))


def adverse_price(price: float, side: str, opening: bool, bps: float) -> float:
    direction = 1.0 if side == "LONG" else -1.0
    sign = direction if opening else -direction
    return price * (1.0 + sign * bps / 10_000.0)


def portfolio_definition(config: dict[str, Any], name: str) -> dict[str, Any]:
    for item in config.get("portfolios", []):
        if item.get("name") == name:
            return item
    raise KeyError(name)


def can_open(
    portfolio: dict[str, Any],
    signal: Signal,
    equity: float,
    config: dict[str, Any],
) -> tuple[bool, str]:
    allowed, reason = risk_gate(
        portfolio,
        equity,
        config,
    )
    if not allowed:
        return False, reason

    definition = portfolio_definition(
        config,
        signal.portfolio,
    )
    positions = portfolio.get("open_positions", [])
    max_positions = int(
        definition.get(
            "max_open_positions",
            config["risk"]["max_open_positions"],
        )
    )
    if len(positions) >= max_positions:
        return False, "numero massimo posizioni"
    if any(
        position["asset"] == signal.asset
        for position in positions
    ):
        return False, "asset già aperto nel portafoglio"

    same_direction = sum(
        position["side"] == signal.side
        for position in positions
    )
    max_same_direction = int(
        definition.get(
            "max_same_direction_positions",
            config["risk"][
                "max_same_direction_positions"
            ],
        )
    )
    if same_direction >= max_same_direction:
        return (
            False,
            "limite posizioni nella stessa direzione",
        )
    return True, "OK"


def build_position(
    portfolio: dict[str, Any],
    signal: Signal,
    bundle: dict[str, Any],
    equity: float,
    config: dict[str, Any],
    when: datetime,
) -> tuple[dict[str, Any] | None, str]:
    eur_usdt_rate = float(
        bundle.get(
            "eur_usdt_rate",
            config.get("eur_usdt_fallback_rate", 1.0),
        )
    )
    if eur_usdt_rate <= 0:
        return None, "cambio EUR/USDT non valido"

    definition = portfolio_definition(
        config,
        signal.portfolio,
    )
    sizing_equity = (
        equity
        if config.get("compounding_enabled", True)
        else float(
            state_initial_capital(
                portfolio,
                config,
            )
        )
    )
    reinvestment = float(
        config.get("reinvestment_rate", 1.0)
    )
    if config.get("compounding_enabled", True):
        initial = float(config["initial_capital_eur"])
        sizing_equity = (
            initial
            + max(0.0, equity - initial) * reinvestment
            + min(0.0, equity - initial)
        )

    min_stop = float(
        definition.get(
            "minimum_stop_pct",
            config["risk"]["minimum_stop_pct"],
        )
    )
    max_stop = float(
        definition.get(
            "maximum_stop_pct",
            config["risk"]["maximum_stop_pct"],
        )
    )
    stop_pct = max(
        min_stop,
        min(max_stop, float(signal.stop_pct)),
    )

    global_leverage_cap = float(
        config["risk"]["absolute_max_leverage"]
    )
    leverage_cap = float(
        definition.get(
            "max_leverage",
            global_leverage_cap,
        )
    )
    leverage = min(
        float(signal.leverage),
        leverage_cap,
    )
    if leverage <= 0:
        return None, "leva non valida"

    max_total_risk = (
        equity
        * float(
            config["risk"]["max_total_open_risk"]
        )
    )
    remaining_risk = max(
        0.0,
        max_total_risk - open_risk_eur(portfolio),
    )
    if remaining_risk <= 0:
        return None, "limite rischio complessivo"

    max_notional_by_margin = (
        equity
        * float(
            config["risk"]["max_margin_per_position"]
        )
        * leverage
    )
    remaining_margin = max(
        0.0,
        equity
        * float(config["risk"]["max_total_margin"])
        - open_margin_eur(portfolio),
    )
    max_notional_by_total_margin = (
        remaining_margin * leverage
    )
    max_notional_by_risk = (
        remaining_risk / stop_pct
    )

    fixed_margin = definition.get("fixed_margin_eur")
    if fixed_margin is not None:
        desired_notional = (
            float(fixed_margin) * leverage
        )
        notional_eur = min(
            desired_notional,
            max_notional_by_risk,
            max_notional_by_margin,
            max_notional_by_total_margin,
        )
    else:
        risk_fraction = float(
            definition.get(
                "risk_per_trade_override",
                effective_risk_fraction(
                    portfolio,
                    equity,
                    config,
                ),
            )
        )
        desired_risk = max(
            0.0,
            sizing_equity * risk_fraction,
        )
        risk_budget = min(
            desired_risk,
            remaining_risk,
        )
        if risk_budget <= 0:
            return None, "budget rischio nullo"
        notional_eur = min(
            risk_budget / stop_pct,
            max_notional_by_margin,
            max_notional_by_total_margin,
        )

    if notional_eur < 25.0:
        return None, "posizione inferiore a 25 EUR"

    risk_budget = notional_eur * stop_pct
    bps = slippage_bps(
        bundle,
        signal.asset,
        config,
    )
    reference = float(
        bundle.get("assets", {})
        .get(signal.asset, {})
        .get("mark_price")
        or signal.entry_reference_price
    )
    entry_price = adverse_price(
        reference,
        signal.side,
        True,
        bps,
    )
    notional_usdt = notional_eur * eur_usdt_rate
    quantity = notional_usdt / entry_price
    margin_eur = notional_eur / leverage
    direction = (
        1.0
        if signal.side == "LONG"
        else -1.0
    )
    stop_price = entry_price * (
        1.0 - direction * stop_pct
    )
    target_price = entry_price * (
        1.0 + direction * signal.target_pct
    )

    liquidation_buffer = float(
        definition.get(
            "liquidation_buffer_fraction",
            0.005,
        )
    )
    liquidation_distance = max(
        0.001,
        1.0 / leverage - liquidation_buffer,
    )
    liquidation_price = entry_price * (
        1.0 - direction * liquidation_distance
    )
    if (
        signal.side == "LONG"
        and stop_price <= liquidation_price
    ):
        return None, "stop oltre la liquidazione stimata"
    if (
        signal.side == "SHORT"
        and stop_price >= liquidation_price
    ):
        return None, "stop oltre la liquidazione stimata"

    fee_rate = (
        float(config["execution"]["taker_fee_bps"])
        / 10_000.0
    )
    entry_fee_eur = notional_eur * fee_rate
    if entry_fee_eur >= portfolio["balance_eur"]:
        return (
            None,
            "saldo insufficiente per commissione",
        )

    portfolio["balance_eur"] = (
        float(portfolio["balance_eur"])
        - entry_fee_eur
    )
    position = {
        "trade_id": signal.signal_id,
        "experiment_group_id": (
            signal.experiment_group_id
        ),
        "portfolio": signal.portfolio,
        "is_main": signal.is_main,
        "strategy": signal.strategy,
        "asset": signal.asset,
        "symbol": signal.symbol,
        "side": signal.side,
        "timeframe_minutes": (
            signal.timeframe_minutes
        ),
        "opened_at": iso_utc(when),
        "entry_price": entry_price,
        "quantity": quantity,
        "notional_eur": notional_eur,
        "margin_eur": margin_eur,
        "leverage": leverage,
        "liquidation_price": liquidation_price,
        "initial_stop_price": stop_price,
        "stop_price": stop_price,
        "target_price": target_price,
        "initial_risk_eur": risk_budget,
        "entry_fee_eur": entry_fee_eur,
        "funding_pnl_eur": 0.0,
        "max_favorable_price": entry_price,
        "max_adverse_price": entry_price,
        "mfe_gross_eur": 0.0,
        "mae_gross_eur": 0.0,
        "mfe_net_eur": -entry_fee_eur,
        "mae_net_eur": -entry_fee_eur,
        "last_funding_time": iso_utc(when),
        "last_processed_candle": "",
        "max_holding_hours": (
            signal.max_holding_hours
        ),
        "trailing_at_r": signal.trailing_at_r,
        "trailing_atr_multiple": (
            signal.trailing_atr_multiple
        ),
        "atr_pct": signal.atr_pct,
        "signal_score": signal.score,
        "confidence": signal.confidence,
        "source": bundle.get("source", ""),
        "eur_usdt_rate": eur_usdt_rate,
    }
    return position, "aperta"


def state_initial_capital(portfolio: dict[str, Any], config: dict[str, Any]) -> float:
    return float(config.get("initial_capital_eur", 10000.0))


def apply_funding(position: dict[str, Any], portfolio: dict[str, Any], bundle: dict[str, Any], config: dict[str, Any], when: datetime) -> None:
    interval_hours = float(config["execution"].get("funding_interval_hours", 8))
    if interval_hours <= 0:
        return
    last = parse_time(position.get("last_funding_time", position["opened_at"]))
    elapsed = (when - last).total_seconds() / 3600.0
    intervals = int(elapsed // interval_hours)
    if intervals <= 0:
        return
    rate = safe_float(bundle.get("assets", {}).get(position["asset"], {}).get("funding_rate"), 0.0)
    if not math.isfinite(rate):
        rate = 0.0
    direction_cost = -1.0 if position["side"] == "LONG" else 1.0
    funding = float(position["notional_eur"]) * rate * intervals * direction_cost
    portfolio["balance_eur"] = float(portfolio["balance_eur"]) + funding
    position["funding_pnl_eur"] = float(position.get("funding_pnl_eur", 0.0)) + funding
    position["last_funding_time"] = iso_utc(last + pd.Timedelta(hours=intervals * interval_hours).to_pytimedelta())


def update_position_excursions(
    position: dict[str, Any],
    candle: pd.Series,
    config: dict[str, Any],
) -> None:
    """Track favorable and adverse excursion from completed 15m candles."""
    entry = float(position["entry_price"])
    quantity = abs(float(position["quantity"]))
    rate = max(float(position.get("eur_usdt_rate", 1.0)), 1e-12)
    direction = 1.0 if position["side"] == "LONG" else -1.0

    high = float(candle.get("high", entry))
    low = float(candle.get("low", entry))
    favorable_price = high if direction > 0 else low
    adverse_price = low if direction > 0 else high

    old_favorable = float(position.get("max_favorable_price", entry))
    old_adverse = float(position.get("max_adverse_price", entry))

    if direction > 0:
        max_favorable_price = max(old_favorable, favorable_price)
        max_adverse_price = min(old_adverse, adverse_price)
    else:
        max_favorable_price = min(old_favorable, favorable_price)
        max_adverse_price = max(old_adverse, adverse_price)

    def gross_pnl(price: float) -> float:
        return (price - entry) * quantity * direction / rate

    fee_rate = (
        float(config["execution"]["taker_fee_bps"])
        / 10_000.0
    )
    entry_fee = float(position.get("entry_fee_eur", 0.0))
    funding = float(position.get("funding_pnl_eur", 0.0))

    favorable_gross = gross_pnl(max_favorable_price)
    adverse_gross = gross_pnl(max_adverse_price)
    favorable_exit_fee = (
        abs(max_favorable_price * quantity / rate)
        * fee_rate
    )
    adverse_exit_fee = (
        abs(max_adverse_price * quantity / rate)
        * fee_rate
    )
    favorable_net = (
        favorable_gross
        - favorable_exit_fee
        - entry_fee
        + funding
    )
    adverse_net = (
        adverse_gross
        - adverse_exit_fee
        - entry_fee
        + funding
    )

    position["max_favorable_price"] = max_favorable_price
    position["max_adverse_price"] = max_adverse_price
    position["mfe_gross_eur"] = max(
        float(position.get("mfe_gross_eur", 0.0)),
        favorable_gross,
    )
    position["mae_gross_eur"] = min(
        float(position.get("mae_gross_eur", 0.0)),
        adverse_gross,
    )
    position["mfe_net_eur"] = max(
        float(position.get("mfe_net_eur", -entry_fee)),
        favorable_net,
    )
    position["mae_net_eur"] = min(
        float(position.get("mae_net_eur", -entry_fee)),
        adverse_net,
    )


def maybe_trail(position: dict[str, Any], candle: pd.Series, mark: float) -> None:
    trigger_r = float(position.get("trailing_at_r", 0.0))
    atr_multiple = float(position.get("trailing_atr_multiple", 0.0))
    if trigger_r <= 0 or atr_multiple <= 0:
        return
    entry = float(position["entry_price"])
    initial_risk_price = abs(entry - float(position["initial_stop_price"]))
    if initial_risk_price <= 0:
        return
    if position["side"] == "LONG":
        favorable_r = (float(candle["high"]) - entry) / initial_risk_price
        if favorable_r >= trigger_r:
            distance = mark * float(position.get("atr_pct", 0.0)) / 100.0 * atr_multiple
            candidate = max(entry, mark - distance)
            position["stop_price"] = max(float(position["stop_price"]), candidate)
    else:
        favorable_r = (entry - float(candle["low"])) / initial_risk_price
        if favorable_r >= trigger_r:
            distance = mark * float(position.get("atr_pct", 0.0)) / 100.0 * atr_multiple
            candidate = min(entry, mark + distance)
            position["stop_price"] = min(float(position["stop_price"]), candidate)


def close_position(
    portfolio: dict[str, Any], position: dict[str, Any], raw_exit_price: float, reason: str,
    bundle: dict[str, Any], config: dict[str, Any], when: datetime
) -> dict[str, Any]:
    bps = slippage_bps(bundle, position["asset"], config)
    exit_price = adverse_price(raw_exit_price, position["side"], False, bps)
    direction = 1.0 if position["side"] == "LONG" else -1.0
    gross_usdt = (exit_price - float(position["entry_price"])) * float(position["quantity"]) * direction
    rate = float(position.get("eur_usdt_rate", bundle.get("eur_usdt_rate", 1.0)))
    gross_eur = gross_usdt / rate
    exit_notional_eur = abs(exit_price * float(position["quantity"]) / rate)
    exit_fee = exit_notional_eur * float(config["execution"]["taker_fee_bps"]) / 10_000.0
    net_before_entry_fee = gross_eur - exit_fee + float(position.get("funding_pnl_eur", 0.0))
    net_total = net_before_entry_fee - float(position.get("entry_fee_eur", 0.0))
    portfolio["balance_eur"] = float(portfolio["balance_eur"]) + gross_eur - exit_fee
    portfolio["closed_trades"] = int(portfolio.get("closed_trades", 0)) + 1
    if net_total > 0:
        portfolio["winning_trades"] = int(portfolio.get("winning_trades", 0)) + 1
        portfolio["gross_profit_eur"] = float(portfolio.get("gross_profit_eur", 0.0)) + net_total
    else:
        portfolio["gross_loss_eur"] = float(portfolio.get("gross_loss_eur", 0.0)) + abs(net_total)

    opened = parse_time(position["opened_at"])
    initial_risk = max(float(position.get("initial_risk_eur", 0.0)), 1e-9)
    mfe_net = float(position.get("mfe_net_eur", 0.0))
    profit_retained_pct = (
        net_total / mfe_net * 100.0
        if mfe_net > 0
        else 0.0
    )
    peak_profit_giveback = (
        mfe_net - net_total
        if mfe_net > 0
        else 0.0
    )
    record = {
        **position,
        "closed_at": iso_utc(when),
        "holding_hours": round((when - opened).total_seconds() / 3600.0, 4),
        "exit_price": exit_price,
        "final_stop_price": position["stop_price"],
        "gross_pnl_eur": gross_eur,
        "exit_fee_eur": exit_fee,
        "net_pnl_eur": net_total,
        "return_on_margin_pct": net_total / max(float(position["margin_eur"]), 1e-9) * 100.0,
        "r_multiple": net_total / initial_risk,
        "max_favorable_price": position.get(
            "max_favorable_price",
            position["entry_price"],
        ),
        "max_adverse_price": position.get(
            "max_adverse_price",
            position["entry_price"],
        ),
        "mfe_gross_eur": position.get("mfe_gross_eur", 0.0),
        "mae_gross_eur": position.get("mae_gross_eur", 0.0),
        "mfe_net_eur": mfe_net,
        "mae_net_eur": position.get("mae_net_eur", 0.0),
        "profit_retained_pct": profit_retained_pct,
        "peak_profit_giveback_eur": peak_profit_giveback,
        "close_reason": reason,
        "eur_usdt_rate": rate,
    }
    append_csv(TRADE_LOG_PATH, TRADE_FIELDS, record)
    return record


def update_positions(
    portfolio: dict[str, Any], bundle: dict[str, Any], config: dict[str, Any], when: datetime
) -> list[dict[str, Any]]:
    frames = bundle_frames(bundle)
    prices = current_prices(bundle)
    closed: list[dict[str, Any]] = []
    remaining: list[dict[str, Any]] = []

    for position in portfolio.get("open_positions", []):
        apply_funding(position, portfolio, bundle, config, when)
        asset = position["asset"]
        mark = prices.get(asset, float(position["entry_price"]))
        frame = frames.get(asset, {}).get(15)
        if frame is None or frame.empty:
            if (when - parse_time(position["opened_at"])).total_seconds() / 3600.0 >= float(position["max_holding_hours"]):
                closed.append(close_position(portfolio, position, mark, "TIME_EXIT_NO_CANDLES", bundle, config, when))
            else:
                remaining.append(position)
            continue

        candle = frame.iloc[-1]
        candle_time = pd.Timestamp(frame.index[-1]).isoformat()
        if position.get("last_processed_candle") == candle_time:
            remaining.append(position)
            continue
        position["last_processed_candle"] = candle_time
        update_position_excursions(position, candle, config)
        maybe_trail(position, candle, mark)

        stop = float(position["stop_price"])
        target = float(position["target_price"])
        liquidation_raw = position.get(
            "liquidation_price"
        )
        liquidation = (
            float(liquidation_raw)
            if liquidation_raw not in (None, "")
            else None
        )
        candle_open = float(candle.get("open", mark))
        if position["side"] == "LONG":
            stop_hit = float(candle["low"]) <= stop
            target_hit = float(candle["high"]) >= target
            liquidation_gap = (
                liquidation is not None
                and candle_open <= liquidation
            )
        else:
            stop_hit = float(candle["high"]) >= stop
            target_hit = float(candle["low"]) <= target
            liquidation_gap = (
                liquidation is not None
                and candle_open >= liquidation
            )

        exit_price = None
        reason = ""
        if liquidation_gap:
            exit_price = liquidation
            reason = "LIQUIDATION_GAP"
        elif stop_hit and target_hit:
            if config["execution"].get("same_candle_stop_target_policy") == "TARGET_FIRST":
                exit_price, reason = target, "TARGET_SAME_CANDLE"
            else:
                exit_price, reason = stop, "STOP_SAME_CANDLE_CONSERVATIVE"
        elif stop_hit:
            exit_price, reason = stop, "STOP"
        elif target_hit:
            exit_price, reason = target, "TARGET"
        elif (when - parse_time(position["opened_at"])).total_seconds() / 3600.0 >= float(position["max_holding_hours"]):
            exit_price, reason = mark, "TIME_EXIT"

        if exit_price is not None:
            closed.append(close_position(portfolio, position, exit_price, reason, bundle, config, when))
        else:
            remaining.append(position)

    portfolio["open_positions"] = remaining
    return closed


def close_on_signal_flip(
    portfolio: dict[str, Any], signals: list[Signal], bundle: dict[str, Any], config: dict[str, Any], when: datetime
) -> list[dict[str, Any]]:
    signal_by_asset = {signal.asset: signal for signal in signals if signal.portfolio == portfolio["name"]}
    prices = current_prices(bundle)
    closed: list[dict[str, Any]] = []
    remaining: list[dict[str, Any]] = []
    for position in portfolio.get("open_positions", []):
        signal = signal_by_asset.get(position["asset"])
        if signal and signal.side != position["side"]:
            price = prices.get(position["asset"], float(position["entry_price"]))
            closed.append(close_position(portfolio, position, price, "SIGNAL_FLIP", bundle, config, when))
        else:
            remaining.append(position)
    portfolio["open_positions"] = remaining
    return closed


def signal_log(signal: Signal, decision: str, reason: str, when: datetime) -> None:
    row = signal.to_dict()
    row.update({"processed_at": iso_utc(when), "decision": decision, "decision_reason": reason})
    append_csv(SIGNAL_LOG_PATH, SIGNAL_FIELDS, row)


def process_new_signals(
    portfolio: dict[str, Any], signals: list[Signal], bundle: dict[str, Any], config: dict[str, Any], when: datetime
) -> list[dict[str, Any]]:
    prices = current_prices(bundle)
    eur_rate = float(bundle.get("eur_usdt_rate", config.get("eur_usdt_fallback_rate", 1.0)))
    equity, _ = portfolio_equity(portfolio, prices, eur_rate)
    opened: list[dict[str, Any]] = []
    seen = set(portfolio.get("seen_signal_ids", []))

    candidates = sorted(
        (signal for signal in signals if signal.portfolio == portfolio["name"]),
        key=lambda item: abs(item.score), reverse=True
    )
    for signal in candidates:
        if signal.signal_id in seen:
            continue
        seen.add(signal.signal_id)
        allowed, reason = can_open(portfolio, signal, equity, config)
        if not allowed:
            signal_log(signal, "REJECTED", reason, when)
            continue
        position, reason = build_position(portfolio, signal, bundle, equity, config, when)
        if position is None:
            signal_log(signal, "REJECTED", reason, when)
            continue
        portfolio.setdefault("open_positions", []).append(position)
        opened.append(position)
        signal_log(signal, "OPENED", reason, when)
        equity, _ = portfolio_equity(portfolio, prices, eur_rate)

    portfolio["seen_signal_ids"] = list(seen)[-20_000:]
    return opened


def trade_stats(portfolio: dict[str, Any]) -> tuple[float, float]:
    closed = int(portfolio.get("closed_trades", 0))
    wins = int(portfolio.get("winning_trades", 0))
    win_rate = wins / closed * 100.0 if closed else 0.0
    profit = float(portfolio.get("gross_profit_eur", 0.0))
    loss = float(portfolio.get("gross_loss_eur", 0.0))
    profit_factor = profit / loss if loss > 0 else (math.inf if profit > 0 else 0.0)
    return win_rate, profit_factor


def log_equity(state: dict[str, Any], bundle: dict[str, Any], config: dict[str, Any], when: datetime) -> None:
    prices = current_prices(bundle)
    rate = float(bundle.get("eur_usdt_rate", config.get("eur_usdt_fallback_rate", 1.0)))
    target = float(config.get("monthly_target_eur", 0.0))
    for portfolio in state["portfolios"].values():
        equity, unrealized = portfolio_equity(portfolio, prices, rate)
        roll_periods(portfolio, equity, when)
        update_drawdown(portfolio, equity)
        month_start = float(portfolio["periods"]["month_start_equity_eur"])
        month_pnl = equity - month_start
        progress = month_pnl / target * 100.0 if target > 0 else 0.0
        drawdown = (float(portfolio["peak_equity_eur"]) - equity) / max(float(portfolio["peak_equity_eur"]), 1e-9) * 100.0
        win_rate, profit_factor = trade_stats(portfolio)
        append_csv(
            EQUITY_LOG_PATH,
            EQUITY_FIELDS,
            {
                "generated_utc": iso_utc(when),
                "portfolio": portfolio["name"],
                "is_main": portfolio["is_main"],
                "balance_eur": portfolio["balance_eur"],
                "unrealized_pnl_eur": unrealized,
                "equity_eur": equity,
                "peak_equity_eur": portfolio["peak_equity_eur"],
                "drawdown_pct": drawdown,
                "month_start_equity_eur": month_start,
                "month_pnl_eur": month_pnl,
                "monthly_target_eur": target,
                "target_progress_pct": progress,
                "open_positions": len(portfolio.get("open_positions", [])),
                "closed_trades": portfolio.get("closed_trades", 0),
                "win_rate_pct": win_rate,
                "profit_factor": profit_factor if math.isfinite(profit_factor) else "inf",
                "max_drawdown_pct": portfolio.get("max_drawdown_pct", 0.0),
            },
        )


def write_open_positions(state: dict[str, Any], bundle: dict[str, Any]) -> None:
    rows: list[dict[str, Any]] = []
    fields = [
        "portfolio", "is_main", "trade_id", "experiment_group_id", "asset", "symbol", "side", "strategy",
        "timeframe_minutes", "opened_at", "entry_price", "mark_price", "stop_price", "liquidation_price", "target_price", "quantity",
        "notional_eur", "margin_eur", "leverage", "initial_risk_eur", "entry_fee_eur", "funding_pnl_eur",
        "max_favorable_price", "max_adverse_price",
        "mfe_gross_eur", "mae_gross_eur", "mfe_net_eur", "mae_net_eur",
        "signal_score", "confidence"
    ]
    prices = current_prices(bundle)
    for portfolio in state["portfolios"].values():
        for position in portfolio.get("open_positions", []):
            rows.append({**position, "portfolio": portfolio["name"], "is_main": portfolio["is_main"], "mark_price": prices.get(position["asset"], "")})
    write_csv(OPEN_POSITIONS_PATH, fields, rows)


def run_execution_cycle(
    state: dict[str, Any], signals: list[Signal], bundle: dict[str, Any], config: dict[str, Any], when: datetime | None = None
) -> dict[str, Any]:
    current = when or now_utc()
    summary = {"opened": [], "closed": [], "generated_utc": iso_utc(current)}
    prices = current_prices(bundle)
    rate = float(bundle.get("eur_usdt_rate", config.get("eur_usdt_fallback_rate", 1.0)))

    for name, portfolio in state["portfolios"].items():
        equity, _ = portfolio_equity(portfolio, prices, rate)
        roll_periods(portfolio, equity, current)
        summary["closed"].extend(update_positions(portfolio, bundle, config, current))
        summary["closed"].extend(close_on_signal_flip(portfolio, signals, bundle, config, current))
        summary["opened"].extend(process_new_signals(portfolio, signals, bundle, config, current))
        equity, _ = portfolio_equity(portfolio, prices, rate)
        update_drawdown(portfolio, equity)

    log_equity(state, bundle, config, current)
    write_open_positions(state, bundle)
    save_state(state, config, current)
    return summary
