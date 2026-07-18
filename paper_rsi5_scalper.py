# -*- coding: utf-8 -*-
"""Standalone 5-minute RSI long/short paper scalper for KuCoin futures.

Paper trading only: no private KuCoin keys and no real orders.

Operational accounts:
- LONG RSI 20 and 25, leverage 10x and 20x
- SHORT RSI 70 and 75, leverage 10x and 20x

Each operational account can hold one position at a time and sends Telegram
notifications. A separate silent statistical layer opens every valid signal
with unlimited simulated capital, allowing concurrent positions across assets.
Those shadow trades are written only to reports.
"""

from __future__ import annotations

import csv
import json
import math
import os
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

CONFIG_PATH = Path(os.getenv("RSI5_SCALPER_CONFIG", "paper_rsi5_scalper_config.json"))
REPORTS_DIR = Path("reports")
STATE_PATH = REPORTS_DIR / "paper_rsi5_scalper_state.json"
TRADES_PATH = REPORTS_DIR / "paper_rsi5_scalper_trades.csv"
SIGNALS_PATH = REPORTS_DIR / "paper_rsi5_scalper_signals.csv"
LATEST_MD_PATH = REPORTS_DIR / "paper_rsi5_scalper_latest.md"
LATEST_JSON_PATH = REPORTS_DIR / "paper_rsi5_scalper_latest.json"
SHADOW_TRADES_PATH = REPORTS_DIR / "paper_rsi5_scalper_shadow_trades.csv"
SHADOW_REPORT_PATH = REPORTS_DIR / "paper_rsi5_scalper_shadow_report.md"
SHADOW_JSON_PATH = REPORTS_DIR / "paper_rsi5_scalper_shadow_latest.json"

FUTURES_BASE = os.getenv("KUCOIN_FUTURES_BASE_URL", "https://api-futures.kucoin.com")

TRADE_FIELDS = [
    "trade_id",
    "account",
    "account_label",
    "book",
    "direction",
    "asset",
    "symbol",
    "rsi_trigger",
    "signal_rsi",
    "leverage",
    "opened_at",
    "closed_at",
    "holding_minutes",
    "entry_price",
    "exit_price",
    "stop_price",
    "target_price",
    "liquidation_price",
    "margin_usdt",
    "notional_usdt",
    "quantity",
    "gross_pnl_usdt",
    "entry_fee_usdt",
    "exit_fee_usdt",
    "net_pnl_usdt",
    "return_on_margin_pct",
    "close_reason",
    "balance_after_usdt",
]

SIGNAL_FIELDS = [
    "processed_at",
    "candle_time",
    "account",
    "account_label",
    "direction",
    "asset",
    "symbol",
    "rsi_trigger",
    "previous_rsi",
    "current_rsi",
    "price",
    "decision",
    "reason",
]


def now_utc() -> datetime:
    return datetime.now(timezone.utc)


def iso_utc(value: datetime | pd.Timestamp | None = None) -> str:
    if value is None:
        value = now_utc()
    stamp = pd.Timestamp(value)
    if stamp.tzinfo is None:
        stamp = stamp.tz_localize("UTC")
    return stamp.isoformat()


def parse_time(value: Any) -> datetime:
    stamp = pd.Timestamp(value)
    if stamp.tzinfo is None:
        stamp = stamp.tz_localize("UTC")
    return stamp.to_pydatetime()


def safe_float(value: Any, default: float = math.nan) -> float:
    try:
        number = float(value)
    except Exception:
        return default
    return number if math.isfinite(number) else default


def load_config() -> dict[str, Any]:
    if not CONFIG_PATH.exists():
        raise FileNotFoundError(f"Configurazione non trovata: {CONFIG_PATH}")
    config = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    if not config.get("paper_only", False):
        raise ValueError("La configurazione deve avere paper_only=true")
    if int(config.get("timeframe_minutes", 0)) != 5:
        raise ValueError("Questa strategia richiede timeframe_minutes=5")
    if not config.get("accounts"):
        raise ValueError("Nessun conto paper configurato")
    if not config.get("assets"):
        raise ValueError("Nessun asset configurato")
    return config


def make_session() -> requests.Session:
    client = requests.Session()
    retry = Retry(
        total=4,
        read=4,
        connect=4,
        backoff_factor=0.7,
        status_forcelist=(429, 500, 502, 503, 504),
        allowed_methods=("GET", "POST"),
        raise_on_status=False,
    )
    client.mount("https://", HTTPAdapter(max_retries=retry))
    client.headers.update({"User-Agent": "crypto-fractal-scanner-rsi5-paper/1.0"})
    return client


def get_json(
    client: requests.Session,
    base: str,
    path: str,
    params: dict[str, Any] | None = None,
) -> Any:
    response = client.get(base + path, params=params or {}, timeout=25)
    response.raise_for_status()
    payload = response.json()
    if isinstance(payload, dict) and payload.get("code") not in (None, "200000"):
        raise RuntimeError(
            f"KuCoin {path}: code={payload.get('code')} msg={payload.get('msg')}"
        )
    return payload.get("data") if isinstance(payload, dict) and "data" in payload else payload


def asset_from_symbol(symbol: str) -> str:
    raw = str(symbol).upper().strip()
    if raw.endswith("USDTM"):
        raw = raw[:-5]
    elif raw.endswith("USDM"):
        raw = raw[:-4]
    return "BTC" if raw == "XBT" else raw


def fetch_contracts(client: requests.Session) -> dict[str, dict[str, Any]]:
    rows = get_json(client, FUTURES_BASE, "/api/v1/contracts/active")
    output: dict[str, dict[str, Any]] = {}
    for row in rows if isinstance(rows, list) else []:
        if not isinstance(row, dict):
            continue
        symbol = str(row.get("symbol", "")).upper().strip()
        if not symbol.endswith("USDTM"):
            continue
        asset = asset_from_symbol(symbol)
        mark = safe_float(row.get("markPrice"), safe_float(row.get("lastTradePrice")))
        turnover = max(0.0, safe_float(row.get("turnoverOf24h"), 0.0))
        status = str(row.get("status", row.get("marketStage", ""))).lower()
        if not asset or not math.isfinite(mark) or mark <= 0:
            continue
        if status in {"closed", "settled", "pause", "paused"}:
            continue
        previous = output.get(asset)
        if previous is None or turnover > float(previous["turnover_24h"]):
            output[asset] = {
                "asset": asset,
                "symbol": symbol,
                "mark_price": mark,
                "turnover_24h": turnover,
            }
    return output


def normalize_klines(rows: Any) -> pd.DataFrame:
    normalized: list[dict[str, Any]] = []
    for row in rows if isinstance(rows, list) else []:
        if not isinstance(row, (list, tuple)) or len(row) < 6:
            continue
        timestamp = safe_float(row[0])
        if not math.isfinite(timestamp):
            continue
        unit = "ms" if timestamp > 10_000_000_000 else "s"
        try:
            index = pd.to_datetime(int(timestamp), unit=unit, utc=True)
        except Exception:
            continue
        opened, high, low, close, volume = map(safe_float, row[1:6])
        if not all(math.isfinite(x) and x > 0 for x in (opened, high, low, close)):
            continue
        normalized.append(
            {
                "time": index,
                "open": opened,
                "high": high,
                "low": low,
                "close": close,
                "volume": max(0.0, volume if math.isfinite(volume) else 0.0),
            }
        )
    if not normalized:
        return pd.DataFrame(columns=["open", "high", "low", "close", "volume"])
    return (
        pd.DataFrame(normalized)
        .drop_duplicates("time")
        .set_index("time")
        .sort_index()[["open", "high", "low", "close", "volume"]]
    )


def fetch_klines(
    client: requests.Session,
    symbol: str,
    timeframe_minutes: int,
    current: datetime,
    limit: int = 200,
) -> pd.DataFrame:
    interval_ms = timeframe_minutes * 60_000
    current_ms = int(current.timestamp() * 1000)
    current_open_ms = (current_ms // interval_ms) * interval_ms
    end = current_open_ms - 1
    start = current_open_ms - limit * interval_ms
    rows = get_json(
        client,
        FUTURES_BASE,
        "/api/v1/kline/query",
        {
            "symbol": symbol,
            "granularity": timeframe_minutes,
            "from": start,
            "to": end,
        },
    )
    frame = normalize_klines(rows)
    if frame.empty:
        rows = get_json(
            client,
            FUTURES_BASE,
            "/api/v1/kline/query",
            {"symbol": symbol, "granularity": timeframe_minutes},
        )
        frame = normalize_klines(rows)
    if len(frame) > limit:
        frame = frame.tail(limit)
    return frame


def rsi_wilder(series: pd.Series, period: int = 14) -> pd.Series:
    close = pd.to_numeric(series, errors="coerce")
    delta = close.diff()
    gains = delta.clip(lower=0.0)
    losses = (-delta.clip(upper=0.0))
    avg_gain = gains.ewm(alpha=1 / period, adjust=False, min_periods=period).mean()
    avg_loss = losses.ewm(alpha=1 / period, adjust=False, min_periods=period).mean()
    rs = avg_gain / avg_loss.replace(0.0, np.nan)
    result = 100.0 - 100.0 / (1.0 + rs)
    result = result.mask((avg_loss == 0.0) & (avg_gain > 0.0), 100.0)
    result = result.mask((avg_gain == 0.0) & (avg_loss > 0.0), 0.0)
    result = result.mask((avg_gain == 0.0) & (avg_loss == 0.0), 50.0)
    return result


def prepare_market(
    config: dict[str, Any], current: datetime
) -> tuple[dict[str, pd.DataFrame], dict[str, dict[str, Any]], list[str]]:
    client = make_session()
    contracts = fetch_contracts(client)
    timeframe = int(config["timeframe_minutes"])
    period = int(config["rsi_period"])
    minimum_turnover = float(config.get("minimum_turnover_24h_usdt", 0.0))
    frames: dict[str, pd.DataFrame] = {}
    metadata: dict[str, dict[str, Any]] = {}
    warnings: list[str] = []

    for configured_asset in config.get("assets", []):
        asset = str(configured_asset).upper().strip()
        contract = contracts.get(asset)
        if not contract:
            warnings.append(f"{asset}: contratto futures USDT non disponibile su KuCoin")
            continue
        if float(contract["turnover_24h"]) < minimum_turnover:
            warnings.append(
                f"{asset}: turnover 24h {float(contract['turnover_24h']):,.0f} USDT sotto il minimo"
            )
            continue
        try:
            frame = fetch_klines(client, contract["symbol"], timeframe, current)
        except Exception as exc:
            warnings.append(f"{asset}: errore candele: {exc}")
            continue
        if len(frame) < period + 3:
            warnings.append(f"{asset}: solo {len(frame)} candele disponibili")
            continue
        frame = frame.copy()
        frame["rsi"] = rsi_wilder(frame["close"], period)
        frame["previous_rsi"] = frame["rsi"].shift(1)
        frame = frame.dropna(subset=["rsi", "previous_rsi"])
        if frame.empty:
            warnings.append(f"{asset}: RSI non calcolabile")
            continue
        frames[asset] = frame
        metadata[asset] = contract
    return frames, metadata, warnings


def new_account_state(definition: dict[str, Any], current: datetime) -> dict[str, Any]:
    capital = float(definition["initial_capital_usdt"])
    return {
        "name": str(definition["name"]),
        "label": str(definition.get("label", definition["name"])),
        "direction": str(definition.get("direction", "LONG")).upper(),
        "created_utc": iso_utc(current),
        "balance_usdt": capital,
        "peak_equity_usdt": capital,
        "max_drawdown_pct": 0.0,
        "open_position": None,
        "closed_trades": 0,
        "winning_trades": 0,
        "gross_profit_usdt": 0.0,
        "gross_loss_usdt": 0.0,
        "asset_guards": {},
    }


def new_shadow_state(definition: dict[str, Any], current: datetime) -> dict[str, Any]:
    return {
        "name": str(definition["name"]),
        "label": str(definition.get("label", definition["name"])),
        "direction": str(definition.get("direction", "LONG")).upper(),
        "created_utc": iso_utc(current),
        "open_positions": [],
        "closed_trades": 0,
        "winning_trades": 0,
        "gross_profit_usdt": 0.0,
        "gross_loss_usdt": 0.0,
        "net_pnl_usdt": 0.0,
        "asset_guards": {},
    }


def initial_state(config: dict[str, Any], current: datetime) -> dict[str, Any]:
    return {
        "schema_version": 1,
        "created_utc": iso_utc(current),
        "updated_utc": iso_utc(current),
        "last_processed_candle": None,
        "last_daily_status_date": None,
        "telegram_started_sent": False,
        "fixed_sizing_notice_sent": False,
        "accounts": {
            str(item["name"]): new_account_state(item, current)
            for item in config["accounts"]
        },
        "shadow_accounts": {
            str(item["name"]): new_shadow_state(item, current)
            for item in config["accounts"]
        },
    }


def load_state(config: dict[str, Any], current: datetime) -> dict[str, Any]:
    if not STATE_PATH.exists():
        return initial_state(config, current)
    try:
        state = json.loads(STATE_PATH.read_text(encoding="utf-8"))
    except Exception:
        broken = STATE_PATH.with_suffix(".json.broken")
        STATE_PATH.replace(broken)
        return initial_state(config, current)
    state.setdefault("accounts", {})
    state.setdefault("shadow_accounts", {})
    for definition in config["accounts"]:
        name = str(definition["name"])
        if name not in state["accounts"]:
            state["accounts"][name] = new_account_state(definition, current)
        if name not in state["shadow_accounts"]:
            state["shadow_accounts"][name] = new_shadow_state(definition, current)
    state.setdefault("last_processed_candle", None)
    state.setdefault("last_daily_status_date", None)
    state.setdefault("telegram_started_sent", False)
    state.setdefault("fixed_sizing_notice_sent", False)
    return state


def save_state(state: dict[str, Any], current: datetime) -> None:
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    state["updated_utc"] = iso_utc(current)
    temporary = STATE_PATH.with_suffix(".json.tmp")
    temporary.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")
    temporary.replace(STATE_PATH)


def append_csv(path: Path, fields: list[str], row: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    exists = path.exists() and path.stat().st_size > 0
    with path.open("a", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        if not exists:
            writer.writeheader()
        writer.writerow({field: row.get(field, "") for field in fields})


def account_definition(config: dict[str, Any], name: str) -> dict[str, Any]:
    for item in config["accounts"]:
        if str(item["name"]) == name:
            return item
    raise KeyError(name)


def execution_price(
    raw_price: float,
    direction: str,
    opening: bool,
    slippage_bps: float,
) -> float:
    direction = direction.upper()
    # LONG: buy to open (+slippage), sell to close (-slippage).
    # SHORT: sell to open (-slippage), buy to close (+slippage).
    adverse_up = (direction == "LONG" and opening) or (
        direction == "SHORT" and not opening
    )
    multiplier = 1.0 + slippage_bps / 10_000.0 if adverse_up else 1.0 - slippage_bps / 10_000.0
    return raw_price * multiplier


def guard_for(account: dict[str, Any], asset: str) -> dict[str, Any]:
    guards = account.setdefault("asset_guards", {})
    return guards.setdefault(
        asset,
        {"needs_rearm": False, "cooldown_until": None, "last_close_reason": None},
    )


def guard_status(guard: dict[str, Any], candle_time: datetime) -> tuple[bool, str]:
    cooldown_raw = guard.get("cooldown_until")
    if cooldown_raw:
        cooldown_until = parse_time(cooldown_raw)
        if candle_time < cooldown_until:
            return False, f"cooldown fino a {iso_utc(cooldown_until)}"
    if guard.get("needs_rearm", False):
        return False, "attesa reset RSI sopra 35"
    return True, "OK"


def update_rearms(
    account: dict[str, Any],
    rows_at_time: dict[str, pd.Series],
    candle_time: datetime,
    direction: str,
    config: dict[str, Any],
) -> None:
    direction = direction.upper()
    for asset, row in rows_at_time.items():
        guard = guard_for(account, asset)
        if not guard.get("needs_rearm", False):
            continue
        cooldown_raw = guard.get("cooldown_until")
        if cooldown_raw and candle_time < parse_time(cooldown_raw):
            continue
        current_rsi = float(row["rsi"])
        reset_ok = (
            current_rsi >= float(config.get("long_rearm_rsi", 35.0))
            if direction == "LONG"
            else current_rsi <= float(config.get("short_rearm_rsi", 65.0))
        )
        if reset_ok:
            guard["needs_rearm"] = False
            guard["cooldown_until"] = None


def position_unrealized(position: dict[str, Any], price: float) -> float:
    entry = float(position["entry_price"])
    quantity = float(position["quantity"])
    return (
        (price - entry) * quantity
        if str(position.get("direction", "LONG")).upper() == "LONG"
        else (entry - price) * quantity
    )


def account_equity(account: dict[str, Any], latest_prices: dict[str, float]) -> float:
    equity = float(account["balance_usdt"])
    position = account.get("open_position")
    if position:
        price = latest_prices.get(position["asset"], float(position["entry_price"]))
        equity += position_unrealized(position, price)
    return equity


def update_account_drawdown(account: dict[str, Any], equity: float) -> None:
    peak = max(float(account.get("peak_equity_usdt", equity)), equity)
    account["peak_equity_usdt"] = peak
    drawdown = max(0.0, (peak - equity) / peak * 100.0) if peak > 0 else 0.0
    account["max_drawdown_pct"] = max(float(account.get("max_drawdown_pct", 0.0)), drawdown)


def open_position(
    account: dict[str, Any],
    definition: dict[str, Any],
    asset: str,
    metadata: dict[str, Any],
    row: pd.Series,
    candle_time: datetime,
    config: dict[str, Any],
) -> tuple[dict[str, Any] | None, str]:
    balance = float(account["balance_usdt"])
    leverage = float(definition["leverage"])
    margin_fraction = float(definition.get("margin_fraction", 1.0))

    # FIXED_SIZING_V1
    # Durante la fase di confronto i profitti aumentano il saldo, ma non la
    # dimensione delle operazioni. Le perdite, invece, riducono la size quando
    # il saldo scende sotto il capitale iniziale: non si simula capitale che il
    # conto non possiede più.
    reinvest_profits = bool(
        definition.get(
            "reinvest_profits",
            config.get("reinvest_profits", False),
        )
    )
    initial_capital = float(definition["initial_capital_usdt"])
    sizing_capital = (
        balance
        if reinvest_profits
        else min(balance, initial_capital)
    )
    margin = max(0.0, sizing_capital * margin_fraction)
    notional = margin * leverage
    if margin <= 0 or notional < 25:
        return None, "capitale insufficiente"

    slippage_bps = float(config["slippage_bps"])
    fee_rate = float(config["taker_fee_bps"]) / 10_000.0
    direction = str(definition.get("direction", "LONG")).upper()
    entry_price = execution_price(float(row["close"]), direction, True, slippage_bps)
    quantity = notional / entry_price
    entry_fee = notional * fee_rate
    if entry_fee >= balance:
        return None, "commissione d'ingresso superiore al saldo"

    stop_pct = float(
        definition.get("stop_loss_pct", config["stop_loss_pct"])
    )
    target_pct = float(
        definition.get("take_profit_pct", config["take_profit_pct"])
    )
    if direction == "LONG":
        stop_price = entry_price * (1.0 - stop_pct)
        target_price = entry_price * (1.0 + target_pct)
    else:
        stop_price = entry_price * (1.0 + stop_pct)
        target_price = entry_price * (1.0 - target_pct)
    liquidation_distance = max(
        0.001,
        1.0 / leverage - float(config.get("liquidation_buffer_fraction", 0.005)),
    )
    liquidation_price = (
        entry_price * (1.0 - liquidation_distance)
        if direction == "LONG"
        else entry_price * (1.0 + liquidation_distance)
    )
    if (
        (direction == "LONG" and stop_price <= liquidation_price)
        or (direction == "SHORT" and stop_price >= liquidation_price)
    ):
        return None, "stop oltre la liquidazione stimata"

    trade_id = (
        f"{definition['name']}:{asset}:{pd.Timestamp(candle_time).strftime('%Y%m%dT%H%M%SZ')}"
    )
    position = {
        "trade_id": trade_id,
        "account": str(definition["name"]),
        "account_label": str(definition.get("label", definition["name"])),
        "book": "OPERATIONAL",
        "direction": direction,
        "asset": asset,
        "symbol": str(metadata["symbol"]),
        "rsi_trigger": float(definition["rsi_trigger"]),
        "signal_rsi": float(row["rsi"]),
        "previous_rsi": float(row["previous_rsi"]),
        "leverage": leverage,
        "opened_at": iso_utc(candle_time),
        "opened_candle_time": iso_utc(candle_time),
        "entry_price": entry_price,
        "stop_price": stop_price,
        "target_price": target_price,
        "liquidation_price": liquidation_price,
        "margin_usdt": margin,
        "notional_usdt": notional,
        "quantity": quantity,
        "entry_fee_usdt": entry_fee,
        "max_holding_hours": float(config["max_holding_hours"]),
    }
    account["balance_usdt"] = balance - entry_fee
    account["open_position"] = position
    return position, "aperta"


def choose_exit(
    position: dict[str, Any],
    row: pd.Series,
    candle_time: datetime,
    config: dict[str, Any],
) -> tuple[float | None, str]:
    opened_candle = parse_time(position["opened_candle_time"])
    if candle_time <= opened_candle:
        return None, ""

    candle_open = float(row["open"])
    candle_high = float(row["high"])
    candle_low = float(row["low"])
    candle_close = float(row["close"])
    stop = float(position["stop_price"])
    target = float(position["target_price"])
    liquidation = float(position["liquidation_price"])
    direction = str(position.get("direction", "LONG")).upper()

    if direction == "LONG":
        if candle_open <= liquidation:
            return liquidation, "LIQUIDATION_GAP"
        if candle_open <= stop:
            return candle_open, "STOP_GAP"
        if candle_open >= target:
            return candle_open, "TARGET_GAP"
        stop_hit = candle_low <= stop
        target_hit = candle_high >= target
    else:
        if candle_open >= liquidation:
            return liquidation, "LIQUIDATION_GAP"
        if candle_open >= stop:
            return candle_open, "STOP_GAP"
        if candle_open <= target:
            return candle_open, "TARGET_GAP"
        stop_hit = candle_high >= stop
        target_hit = candle_low <= target

    if stop_hit and target_hit:
        if str(config.get("same_candle_policy", "STOP_FIRST")).upper() == "TARGET_FIRST":
            return target, "TARGET_SAME_CANDLE"
        return stop, "STOP_SAME_CANDLE_CONSERVATIVE"
    if stop_hit:
        return stop, "STOP"
    if target_hit:
        return target, "TARGET"

    age_hours = (candle_time - parse_time(position["opened_at"])).total_seconds() / 3600.0
    if age_hours >= float(position["max_holding_hours"]):
        return candle_close, "TIME_EXIT"
    return None, ""


def close_position(
    account: dict[str, Any],
    position: dict[str, Any],
    raw_exit_price: float,
    reason: str,
    candle_time: datetime,
    config: dict[str, Any],
) -> dict[str, Any]:
    fee_rate = float(config["taker_fee_bps"]) / 10_000.0
    direction = str(position.get("direction", "LONG")).upper()
    exit_price = execution_price(
        raw_exit_price, direction, False, float(config["slippage_bps"])
    )
    quantity = float(position["quantity"])
    entry_price = float(position["entry_price"])
    gross = (
        (exit_price - entry_price) * quantity
        if direction == "LONG"
        else (entry_price - exit_price) * quantity
    )
    exit_notional = abs(exit_price * quantity)
    exit_fee = exit_notional * fee_rate
    entry_fee = float(position["entry_fee_usdt"])
    net = gross - entry_fee - exit_fee
    account["balance_usdt"] = float(account["balance_usdt"]) + gross - exit_fee
    account["open_position"] = None
    account["closed_trades"] = int(account.get("closed_trades", 0)) + 1
    if net > 0:
        account["winning_trades"] = int(account.get("winning_trades", 0)) + 1
        account["gross_profit_usdt"] = float(account.get("gross_profit_usdt", 0.0)) + net
    else:
        account["gross_loss_usdt"] = float(account.get("gross_loss_usdt", 0.0)) + abs(net)

    opened = parse_time(position["opened_at"])
    record = {
        **position,
        "closed_at": iso_utc(candle_time),
        "holding_minutes": round((candle_time - opened).total_seconds() / 60.0, 2),
        "exit_price": exit_price,
        "gross_pnl_usdt": gross,
        "exit_fee_usdt": exit_fee,
        "net_pnl_usdt": net,
        "return_on_margin_pct": net / max(float(position["margin_usdt"]), 1e-12) * 100.0,
        "close_reason": reason,
        "balance_after_usdt": float(account["balance_usdt"]),
    }
    append_csv(TRADES_PATH, TRADE_FIELDS, record)
    return record


def log_signal(
    current: datetime,
    candle_time: datetime,
    definition: dict[str, Any],
    asset: str,
    metadata: dict[str, Any],
    row: pd.Series,
    decision: str,
    reason: str,
) -> None:
    append_csv(
        SIGNALS_PATH,
        SIGNAL_FIELDS,
        {
            "processed_at": iso_utc(current),
            "candle_time": iso_utc(candle_time),
            "account": definition["name"],
            "account_label": definition.get("label", definition["name"]),
            "direction": str(definition.get("direction", "LONG")).upper(),
            "asset": asset,
            "symbol": metadata["symbol"],
            "rsi_trigger": float(definition["rsi_trigger"]),
            "previous_rsi": float(row["previous_rsi"]),
            "current_rsi": float(row["rsi"]),
            "price": float(row["close"]),
            "decision": decision,
            "reason": reason,
        },
    )


def open_shadow_position(
    shadow: dict[str, Any],
    definition: dict[str, Any],
    asset: str,
    metadata: dict[str, Any],
    row: pd.Series,
    candle_time: datetime,
    config: dict[str, Any],
) -> dict[str, Any] | None:
    # Every signal receives an independent fixed 3,800 USDT simulation.
    fake_account = {
        "balance_usdt": float(definition["initial_capital_usdt"]),
        "open_position": None,
    }
    position, _ = open_position(
        fake_account, definition, asset, metadata, row, candle_time, config
    )
    if not position:
        return None
    position = dict(position)
    position["book"] = "SHADOW"
    position["trade_id"] = position["trade_id"] + ":SHADOW"
    shadow.setdefault("open_positions", []).append(position)
    return position


def close_shadow_position(
    shadow: dict[str, Any],
    position: dict[str, Any],
    raw_exit_price: float,
    reason: str,
    candle_time: datetime,
    config: dict[str, Any],
) -> dict[str, Any]:
    direction = str(position.get("direction", "LONG")).upper()
    exit_price = execution_price(
        raw_exit_price, direction, False, float(config["slippage_bps"])
    )
    quantity = float(position["quantity"])
    entry_price = float(position["entry_price"])
    gross = (
        (exit_price - entry_price) * quantity
        if direction == "LONG"
        else (entry_price - exit_price) * quantity
    )
    exit_fee = abs(exit_price * quantity) * float(config["taker_fee_bps"]) / 10_000.0
    entry_fee = float(position["entry_fee_usdt"])
    net = gross - entry_fee - exit_fee
    opened = parse_time(position["opened_at"])
    shadow["closed_trades"] = int(shadow.get("closed_trades", 0)) + 1
    if net > 0:
        shadow["winning_trades"] = int(shadow.get("winning_trades", 0)) + 1
        shadow["gross_profit_usdt"] = float(shadow.get("gross_profit_usdt", 0.0)) + net
    else:
        shadow["gross_loss_usdt"] = float(shadow.get("gross_loss_usdt", 0.0)) + abs(net)
    shadow["net_pnl_usdt"] = float(shadow.get("net_pnl_usdt", 0.0)) + net
    record = {
        **position,
        "closed_at": iso_utc(candle_time),
        "holding_minutes": round((candle_time - opened).total_seconds() / 60.0, 2),
        "exit_price": exit_price,
        "gross_pnl_usdt": gross,
        "exit_fee_usdt": exit_fee,
        "net_pnl_usdt": net,
        "return_on_margin_pct": net / max(float(position["margin_usdt"]), 1e-12) * 100.0,
        "close_reason": reason,
        "balance_after_usdt": "",
    }
    append_csv(SHADOW_TRADES_PATH, TRADE_FIELDS, record)
    return record


def process_shadow_account(
    shadow: dict[str, Any],
    definition: dict[str, Any],
    rows_at_time: dict[str, pd.Series],
    metadata: dict[str, dict[str, Any]],
    candle_time: datetime,
    config: dict[str, Any],
    cooldown_minutes: int,
) -> None:
    direction = str(definition.get("direction", "LONG")).upper()
    update_rearms(shadow, rows_at_time, candle_time, direction, config)

    remaining: list[dict[str, Any]] = []
    for position in list(shadow.get("open_positions", [])):
        row = rows_at_time.get(position["asset"])
        if row is None:
            remaining.append(position)
            continue
        raw_exit, reason = choose_exit(position, row, candle_time, config)
        if raw_exit is None:
            remaining.append(position)
            continue
        close_shadow_position(
            shadow, position, raw_exit, reason, candle_time, config
        )
        guard = guard_for(shadow, position["asset"])
        guard["needs_rearm"] = True
        guard["last_close_reason"] = reason
        guard["cooldown_until"] = (
            iso_utc(candle_time + timedelta(minutes=cooldown_minutes))
            if reason.startswith("STOP") or reason.startswith("LIQUIDATION")
            else None
        )
    shadow["open_positions"] = remaining

    trigger = float(definition["rsi_trigger"])
    assets_already_open = {
        str(position["asset"]) for position in shadow.get("open_positions", [])
    }
    for asset, row in rows_at_time.items():
        previous_rsi = float(row["previous_rsi"])
        current_rsi = float(row["rsi"])
        crossed = (
            previous_rsi > trigger and current_rsi <= trigger
            if direction == "LONG"
            else previous_rsi < trigger and current_rsi >= trigger
        )
        if not crossed or asset in assets_already_open:
            continue
        guard = guard_for(shadow, asset)
        ready, _ = guard_status(guard, candle_time)
        if not ready:
            continue
        opened = open_shadow_position(
            shadow, definition, asset, metadata[asset], row, candle_time, config
        )
        if opened:
            assets_already_open.add(asset)


def format_money(value: float, signed: bool = False) -> str:
    sign = "+" if signed and value > 0 else ""
    return f"{sign}{value:,.2f} USDT"


def build_status_lines(
    state: dict[str, Any],
    config: dict[str, Any],
    latest_prices: dict[str, float],
) -> list[str]:
    lines = ["📊 RSI 5M SCALPER — STATO CONTI PAPER"]
    for definition in config["accounts"]:
        account = state["accounts"][str(definition["name"])]
        equity = account_equity(account, latest_prices)
        closed = int(account.get("closed_trades", 0))
        wins = int(account.get("winning_trades", 0))
        win_rate = wins / closed * 100.0 if closed else 0.0
        position = account.get("open_position")
        position_text = (
            f"aperta {position['asset']} @ {float(position['entry_price']):.8g}"
            if position
            else "nessuna posizione"
        )
        lines.append(
            f"• {definition.get('label', definition['name'])}: "
            f"saldo {format_money(float(account['balance_usdt']))} · "
            f"equity {format_money(equity)} · chiuse {closed} · WR {win_rate:.1f}% · "
            f"{position_text}"
        )
    return lines


def send_telegram(message: str) -> bool:
    token = (
        os.getenv("RSI5_TELEGRAM_BOT_TOKEN", "").strip()
        or os.getenv("TELEGRAM_BOT_TOKEN", "").strip()
    )
    chat_id = (
        os.getenv("RSI5_TELEGRAM_CHAT_ID", "").strip()
        or os.getenv("TELEGRAM_CHAT_ID", "").strip()
    )
    if not token or not chat_id:
        print("Telegram non configurato: messaggio non inviato.")
        return False
    response = requests.post(
        f"https://api.telegram.org/bot{token}/sendMessage",
        json={"chat_id": chat_id, "text": message, "disable_web_page_preview": True},
        timeout=20,
    )
    response.raise_for_status()
    return True


def write_reports(
    state: dict[str, Any],
    config: dict[str, Any],
    frames: dict[str, pd.DataFrame],
    metadata: dict[str, dict[str, Any]],
    warnings: list[str],
    current: datetime,
) -> None:
    latest_prices = {
        asset: float(frame["close"].iloc[-1]) for asset, frame in frames.items() if not frame.empty
    }
    account_rows: list[dict[str, Any]] = []
    for definition in config["accounts"]:
        account = state["accounts"][str(definition["name"])]
        equity = account_equity(account, latest_prices)
        closed = int(account.get("closed_trades", 0))
        wins = int(account.get("winning_trades", 0))
        gross_profit = float(account.get("gross_profit_usdt", 0.0))
        gross_loss = float(account.get("gross_loss_usdt", 0.0))
        account_rows.append(
            {
                "account": definition["name"],
                "label": definition.get("label", definition["name"]),
                "direction": str(definition.get("direction", "LONG")).upper(),
                "rsi_trigger": float(definition["rsi_trigger"]),
                "leverage": float(definition["leverage"]),
                "balance_usdt": float(account["balance_usdt"]),
                "equity_usdt": equity,
                "closed_trades": closed,
                "winning_trades": wins,
                "win_rate_pct": wins / closed * 100.0 if closed else 0.0,
                "profit_factor": gross_profit / gross_loss if gross_loss > 0 else (math.inf if gross_profit > 0 else 0.0),
                "max_drawdown_pct": float(account.get("max_drawdown_pct", 0.0)),
                "open_position": account.get("open_position"),
            }
        )

    asset_rows = []
    for asset, frame in frames.items():
        last = frame.iloc[-1]
        asset_rows.append(
            {
                "asset": asset,
                "symbol": metadata[asset]["symbol"],
                "price": float(last["close"]),
                "rsi": float(last["rsi"]),
                "turnover_24h_usdt": float(metadata[asset]["turnover_24h"]),
                "candle_time": iso_utc(frame.index[-1]),
            }
        )

    shadow_rows: list[dict[str, Any]] = []
    for definition in config["accounts"]:
        shadow = state["shadow_accounts"][str(definition["name"])]
        closed = int(shadow.get("closed_trades", 0))
        wins = int(shadow.get("winning_trades", 0))
        gross_profit = float(shadow.get("gross_profit_usdt", 0.0))
        gross_loss = float(shadow.get("gross_loss_usdt", 0.0))
        shadow_rows.append(
            {
                "account": definition["name"],
                "label": definition.get("label", definition["name"]),
                "direction": str(definition.get("direction", "LONG")).upper(),
                "rsi_trigger": float(definition["rsi_trigger"]),
                "leverage": float(definition["leverage"]),
                "closed_trades": closed,
                "winning_trades": wins,
                "win_rate_pct": wins / closed * 100.0 if closed else 0.0,
                "net_pnl_usdt": float(shadow.get("net_pnl_usdt", 0.0)),
                "profit_factor": gross_profit / gross_loss if gross_loss > 0 else (
                    math.inf if gross_profit > 0 else 0.0
                ),
                "open_positions": len(shadow.get("open_positions", [])),
            }
        )

    payload = {
        "generated_utc": iso_utc(current),
        "strategy": config["strategy_name"],
        "paper_only": True,
        "reinvest_profits": bool(config.get("reinvest_profits", False)),
        "sizing_mode": (
            "COMPOUNDING"
            if config.get("reinvest_profits", False)
            else "INITIAL_CAPITAL_CAPPED"
        ),
        "last_processed_candle": state.get("last_processed_candle"),
        "accounts": account_rows,
        "shadow_accounts": shadow_rows,
        "assets": asset_rows,
        "warnings": warnings,
    }
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    LATEST_JSON_PATH.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    lines = [
        "# RSI 5m Fixed TP Scalper — paper trading",
        "",
        f"Generato: {iso_utc(current)}",
        "",
        "> Solo simulazione: nessun ordine reale e nessuna chiave KuCoin privata.",
        "",
        (
            "> Sizing: compounding attivo."
            if config.get("reinvest_profits", False)
            else "> Sizing fisso: i profitti non aumentano la size; tetto 3.800 USDT per conto."
        ),
        "",
        "## Conti",
        "",
        "| Conto | Lato | Trigger | Leva | Saldo | Equity | Trade | WR | Max DD | Posizione |",
        "| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in account_rows:
        position = row["open_position"]
        position_text = (
            f"{position['asset']} @ {float(position['entry_price']):.8g}"
            if position
            else "—"
        )
        pf = row["profit_factor"]
        lines.append(
            f"| {row['label']} | {row['direction']} | {row['rsi_trigger']:.0f} | {row['leverage']:.0f}× | "
            f"{row['balance_usdt']:.2f} | {row['equity_usdt']:.2f} | "
            f"{row['closed_trades']} | {row['win_rate_pct']:.1f}% | "
            f"{row['max_drawdown_pct']:.2f}% | {position_text} |"
        )
    lines.extend(
        [
            "",
            "## Mercato monitorato",
            "",
            "| Asset | Prezzo | RSI 5m | Turnover 24h | Ultima candela |",
            "| --- | ---: | ---: | ---: | --- |",
        ]
    )
    for row in sorted(asset_rows, key=lambda item: item["asset"]):
        lines.append(
            f"| {row['asset']} | {row['price']:.8g} | {row['rsi']:.2f} | "
            f"{row['turnover_24h_usdt']:,.0f} | {row['candle_time']} |"
        )
    if warnings:
        lines.extend(["", "## Avvisi", ""])
        lines.extend(f"- {warning}" for warning in warnings)
    LATEST_MD_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")

    shadow_payload = {
        "generated_utc": iso_utc(current),
        "description": "Tutti i segnali validi, capitale illimitato, nessun Telegram",
        "accounts": shadow_rows,
    }
    SHADOW_JSON_PATH.write_text(
        json.dumps(shadow_payload, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    shadow_lines = [
        "# RSI 5m — registro statistico silenzioso",
        "",
        f"Generato: {iso_utc(current)}",
        "",
        "> Apre virtualmente ogni segnale valido anche quando il conto operativo è occupato.",
        "> Nessuna notifica Telegram. Ogni trade usa una simulazione indipendente da 3.800 USDT.",
        "",
        "| Conto teorico | Lato | Trigger | Leva | Chiuse | WR | P/L netto cumulato | Profit factor | Aperte |",
        "| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in shadow_rows:
        pf = row["profit_factor"]
        pf_text = "∞" if math.isinf(pf) else f"{pf:.2f}"
        shadow_lines.append(
            f"| {row['label']} | {row['direction']} | {row['rsi_trigger']:.0f} | "
            f"{row['leverage']:.0f}× | {row['closed_trades']} | "
            f"{row['win_rate_pct']:.1f}% | {row['net_pnl_usdt']:+.2f} | "
            f"{pf_text} | {row['open_positions']} |"
        )
    SHADOW_REPORT_PATH.write_text(
        "\n".join(shadow_lines) + "\n",
        encoding="utf-8",
    )


def run_cycle() -> None:
    current = now_utc()
    config = load_config()
    state = load_state(config, current)
    frames, metadata, warnings = prepare_market(config, current)
    if not frames:
        raise RuntimeError("Nessun asset con dati validi: " + "; ".join(warnings))

    all_times = sorted({pd.Timestamp(index) for frame in frames.values() for index in frame.index})
    last_processed_raw = state.get("last_processed_candle")
    if last_processed_raw:
        last_processed = pd.Timestamp(last_processed_raw)
        if last_processed.tzinfo is None:
            last_processed = last_processed.tz_localize("UTC")
        process_times = [time for time in all_times if time > last_processed]
    else:
        # Prima installazione: considera soltanto l'ultima candela chiusa. In questo
        # modo non apre operazioni retroattive sulle 16 ore precedenti.
        process_times = [all_times[-1]]

    events: list[str] = []
    latest_prices = {
        asset: float(frame["close"].iloc[-1]) for asset, frame in frames.items() if not frame.empty
    }
    cooldown_minutes = int(config["cooldown_after_stop_bars"]) * int(config["timeframe_minutes"])

    for timestamp in process_times:
        candle_time = timestamp.to_pydatetime()
        rows_at_time: dict[str, pd.Series] = {
            asset: frame.loc[timestamp]
            for asset, frame in frames.items()
            if timestamp in frame.index
        }
        if not rows_at_time:
            continue

        for definition in config["accounts"]:
            account_name = str(definition["name"])
            account = state["accounts"][account_name]
            direction = str(definition.get("direction", "LONG")).upper()
            update_rearms(account, rows_at_time, candle_time, direction, config)

            position = account.get("open_position")
            if position and position["asset"] in rows_at_time:
                raw_exit, reason = choose_exit(
                    position,
                    rows_at_time[position["asset"]],
                    candle_time,
                    config,
                )
                if raw_exit is not None:
                    record = close_position(
                        account,
                        position,
                        raw_exit,
                        reason,
                        candle_time,
                        config,
                    )
                    guard = guard_for(account, position["asset"])
                    guard["needs_rearm"] = True
                    guard["last_close_reason"] = reason
                    if reason.startswith("STOP") or reason.startswith("LIQUIDATION"):
                        guard["cooldown_until"] = iso_utc(
                            candle_time + timedelta(minutes=cooldown_minutes)
                        )
                    else:
                        guard["cooldown_until"] = None
                    emoji = "✅" if float(record["net_pnl_usdt"]) > 0 else "🛑"
                    events.append(
                        f"{emoji} CHIUSURA · {record['account_label']}\n"
                        f"{record['asset']} · {record['close_reason']} · "
                        f"P/L {format_money(float(record['net_pnl_usdt']), signed=True)}\n"
                        f"Saldo {format_money(float(record['balance_after_usdt']))} · "
                        f"durata {float(record['holding_minutes']):.0f} min"
                    )

            crossings: list[tuple[str, pd.Series]] = []
            trigger = float(definition["rsi_trigger"])
            for asset, row in rows_at_time.items():
                previous_rsi = float(row["previous_rsi"])
                current_rsi = float(row["rsi"])
                crossed = (
                    previous_rsi > trigger and current_rsi <= trigger
                    if direction == "LONG"
                    else previous_rsi < trigger and current_rsi >= trigger
                )
                if not crossed:
                    continue
                if account.get("open_position"):
                    log_signal(
                        current,
                        candle_time,
                        definition,
                        asset,
                        metadata[asset],
                        row,
                        "ACCOUNT_BUSY",
                        "conto già impegnato in un'altra posizione",
                    )
                    continue
                guard = guard_for(account, asset)
                ready, guard_reason = guard_status(guard, candle_time)
                if not ready:
                    decision = "COOLDOWN" if "cooldown" in guard_reason else "WAIT_REARM"
                    log_signal(
                        current,
                        candle_time,
                        definition,
                        asset,
                        metadata[asset],
                        row,
                        decision,
                        guard_reason,
                    )
                    continue
                crossings.append((asset, row))

            if not account.get("open_position") and crossings:
                crossings.sort(
                    key=lambda item: (
                        float(item[1]["rsi"]) if direction == "LONG" else -float(item[1]["rsi"]),
                        -float(metadata[item[0]]["turnover_24h"]),
                        item[0],
                    )
                )
                selected_asset, selected_row = crossings[0]
                for skipped_asset, skipped_row in crossings[1:]:
                    log_signal(
                        current,
                        candle_time,
                        definition,
                        skipped_asset,
                        metadata[skipped_asset],
                        skipped_row,
                        "NOT_SELECTED",
                        f"selezionato {selected_asset} con RSI più estremo",
                    )
                position, open_reason = open_position(
                    account,
                    definition,
                    selected_asset,
                    metadata[selected_asset],
                    selected_row,
                    candle_time,
                    config,
                )
                if position:
                    log_signal(
                        current,
                        candle_time,
                        definition,
                        selected_asset,
                        metadata[selected_asset],
                        selected_row,
                        "OPENED",
                        "crossing RSI confermato alla chiusura della candela",
                    )
                    events.append(
                        f"🟢 APERTURA · {position['account_label']}\n"
                        f"{position['direction']} {position['asset']} · RSI {float(position['signal_rsi']):.2f} "
                        f"(soglia {float(position['rsi_trigger']):.0f})\n"
                        f"Entrata {float(position['entry_price']):.8g} · "
                        f"TP {float(position['target_price']):.8g} · "
                        f"SL {float(position['stop_price']):.8g}\n"
                        f"Margine {format_money(float(position['margin_usdt']))} · "
                        f"notional {format_money(float(position['notional_usdt']))}"
                    )
                else:
                    log_signal(
                        current,
                        candle_time,
                        definition,
                        selected_asset,
                        metadata[selected_asset],
                        selected_row,
                        "REJECTED",
                        open_reason,
                    )

            prices_at_time = {
                asset: float(row["close"]) for asset, row in rows_at_time.items()
            }
            equity = account_equity(account, {**latest_prices, **prices_at_time})
            update_account_drawdown(account, equity)

        # Silent statistical books: every valid signal, unlimited concurrent capital.
        for definition in config["accounts"]:
            shadow = state["shadow_accounts"][str(definition["name"])]
            process_shadow_account(
                shadow,
                definition,
                rows_at_time,
                metadata,
                candle_time,
                config,
                cooldown_minutes,
            )

        state["last_processed_candle"] = iso_utc(timestamp)

    if not state.get("telegram_started_sent", False):
        events.insert(
            0,
            "🚀 RSI 5M SCALPER PAPER ATTIVATO\n"
            "8 conti indipendenti da 3.800 USDT · LONG RSI 20/25 · "
            "SHORT RSI 70/75 · leve 10×/20× · TP 0,50% · SL 0,25%.\n"
            "Registro statistico parallelo attivo senza notifiche Telegram.",
        )
        state["telegram_started_sent"] = True

    if (
        not config.get("reinvest_profits", False)
        and not state.get("fixed_sizing_notice_sent", False)
    ):
        events.insert(
            0,
            "🔒 RSI 5M — SIZING FISSO ATTIVATO\n"
            "I profitti restano nel saldo ma non aumentano la size. "
            "Margine massimo 3.800 USDT per conto; dopo una perdita la size "
            "si riduce se il saldo scende sotto 3.800 USDT.",
        )
        state["fixed_sizing_notice_sent"] = True

    daily_hour = int(config.get("telegram_daily_status_utc_hour", 18))
    today = current.date().isoformat()
    if current.hour >= daily_hour and state.get("last_daily_status_date") != today:
        events.append("\n".join(build_status_lines(state, config, latest_prices)))
        state["last_daily_status_date"] = today

    write_reports(state, config, frames, metadata, warnings, current)
    save_state(state, current)

    if events:
        send_telegram("\n\n".join(events))
    print(
        json.dumps(
            {
                "ok": True,
                "generated_utc": iso_utc(current),
                "processed_candles": len(process_times),
                "events": len(events),
                "assets": sorted(frames),
                "warnings": warnings,
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    run_cycle()
