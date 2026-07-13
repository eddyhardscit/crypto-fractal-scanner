# -*- coding: utf-8 -*-
"""SOL-only adaptive-range spot paper trader.

The module uses public KuCoin spot market data and simulates fills locally.
It has no authenticated exchange client and contains no real-order path.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import os
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

CONFIG_PATH = Path(os.getenv("SOL_SPOT_ADAPTIVE_CONFIG", "sol_spot_adaptive_config.json"))
REPORTS_DIR = Path("reports")
STATE_PATH = REPORTS_DIR / "sol_spot_adaptive_state.json"
TRADES_PATH = REPORTS_DIR / "sol_spot_adaptive_trades.csv"
EQUITY_PATH = REPORTS_DIR / "sol_spot_adaptive_equity.csv"
LATEST_PATH = REPORTS_DIR / "sol_spot_adaptive_latest.json"
REPORT_PATH = REPORTS_DIR / "sol_spot_adaptive_report.md"
CONFIG_SNAPSHOT_PATH = REPORTS_DIR / "sol_spot_adaptive_config_snapshot.json"

SPOT_BASE = os.getenv("KUCOIN_SPOT_BASE_URL", "https://api.kucoin.com")
TRADE_FIELDS = [
    "trade_id",
    "time_utc",
    "side",
    "reason",
    "market_price_eur",
    "execution_price_eur",
    "quantity_sol",
    "gross_eur",
    "fee_eur",
    "cash_after_eur",
    "sol_after",
    "average_cost_after_eur",
    "realized_pnl_eur",
    "target_sol_weight",
    "regime",
    "range_lower_eur",
    "range_center_eur",
    "range_upper_eur",
]
EQUITY_FIELDS = [
    "time_utc",
    "price_eur",
    "cash_eur",
    "sol_units",
    "sol_value_eur",
    "equity_eur",
    "sol_weight",
    "peak_equity_eur",
    "drawdown_pct",
    "target_sol_weight",
    "regime",
]


class SafetyError(RuntimeError):
    pass


@dataclass(frozen=True)
class RangeSnapshot:
    time_utc: str
    price_eur: float
    lower_eur: float
    center_eur: float
    upper_eur: float
    half_width_pct: float
    atr_eur: float
    volatility_pct: float
    trend_atr: float
    regime: str
    target_sol_weight: float


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def iso_utc(value: datetime | pd.Timestamp | None = None) -> str:
    current = value if value is not None else utc_now()
    timestamp = pd.Timestamp(current)
    if timestamp.tzinfo is None:
        timestamp = timestamp.tz_localize("UTC")
    return timestamp.tz_convert("UTC").isoformat()


def safe_float(value: Any, default: float = math.nan) -> float:
    try:
        number = float(value)
    except Exception:
        return default
    return number if math.isfinite(number) else default


def clamp(value: float, lower: float, upper: float) -> float:
    return min(upper, max(lower, value))


def load_config(path: Path = CONFIG_PATH) -> dict[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    validate_config(payload)
    return payload


def validate_config(config: dict[str, Any]) -> None:
    checks = {
        "mode must be PAPER_ONLY": str(config.get("mode", "")).upper() == "PAPER_ONLY",
        "asset must be SOL": str(config.get("asset", "")).upper() == "SOL",
        "symbol must be SOL-USDT": str(config.get("symbol", "")).upper() == "SOL-USDT",
        "initial capital must be EUR 40,000": math.isclose(
            safe_float(config.get("initial_capital_eur"), 0.0), 40000.0, rel_tol=0.0, abs_tol=1e-9
        ),
        "public data only": config.get("public_data_only") is True,
        "real orders disabled": config.get("real_orders_enabled") is False,
        "shorting disabled": config.get("allow_short") is False,
        "leverage fixed at 1x": math.isclose(
            safe_float(config.get("leverage"), 0.0), 1.0, rel_tol=0.0, abs_tol=1e-12
        ),
    }
    failed = [message for message, ok in checks.items() if not ok]
    if failed:
        raise SafetyError("Unsafe SOL spot configuration: " + "; ".join(failed))

    allocation = config.get("allocation", {})
    minimum = safe_float(allocation.get("minimum_sol_weight"), -1.0)
    maximum = safe_float(allocation.get("maximum_sol_weight"), 2.0)
    reserve = safe_float(allocation.get("minimum_cash_reserve_fraction"), -1.0)
    if not (0.0 <= minimum < maximum <= 1.0):
        raise SafetyError("SOL allocation limits must remain between 0 and 1.")
    if not (0.0 <= reserve < 1.0 and maximum <= 1.0 - reserve + 1e-12):
        raise SafetyError("Cash reserve is incompatible with maximum SOL allocation.")


def make_session() -> requests.Session:
    session = requests.Session()
    retry = Retry(
        total=4,
        read=4,
        connect=4,
        backoff_factor=0.7,
        status_forcelist=(429, 500, 502, 503, 504),
        allowed_methods=("GET",),
        raise_on_status=False,
    )
    session.mount("https://", HTTPAdapter(max_retries=retry))
    session.headers.update({"User-Agent": "crypto-fractal-scanner-sol-spot-paper/1.0"})
    return session


def get_public_json(
    session: requests.Session,
    path: str,
    params: dict[str, Any] | None = None,
) -> Any:
    response = session.get(SPOT_BASE + path, params=params or {}, timeout=25)
    response.raise_for_status()
    payload = response.json()
    if not isinstance(payload, dict) or payload.get("code") != "200000":
        raise RuntimeError(
            f"KuCoin public market-data error at {path}: "
            f"code={payload.get('code') if isinstance(payload, dict) else 'n/a'}"
        )
    return payload.get("data")


def fetch_eur_usdt_rate(session: requests.Session, fallback: float) -> tuple[float, str]:
    env = safe_float(os.getenv("EUR_USDT_RATE"), math.nan)
    if math.isfinite(env) and env > 0:
        return env, "ENV:EUR_USDT_RATE"
    try:
        data = get_public_json(
            session,
            "/api/v1/market/orderbook/level1",
            {"symbol": "EUR-USDT"},
        )
        price = safe_float(data.get("price") if isinstance(data, dict) else None)
        if math.isfinite(price) and price > 0:
            return price, "KUCOIN_PUBLIC:EUR-USDT"
    except Exception:
        pass
    if fallback <= 0:
        raise RuntimeError("EUR/USDT fallback rate must be positive.")
    return fallback, "CONFIG_FALLBACK"


def fetch_spot_klines(
    session: requests.Session,
    symbol: str,
    timeframe_minutes: int,
    limit: int,
    now: datetime | None = None,
) -> pd.DataFrame:
    interval_names = {1: "1min", 3: "3min", 5: "5min", 15: "15min", 30: "30min", 60: "1hour", 240: "4hour"}
    if timeframe_minutes not in interval_names:
        raise RuntimeError(f"Unsupported KuCoin spot timeframe: {timeframe_minutes} minutes")
    current = now or utc_now()
    count = min(max(int(limit), 220), 1500)
    end_at = int(current.timestamp())
    start_at = end_at - count * timeframe_minutes * 60
    rows = get_public_json(
        session,
        "/api/v1/market/candles",
        {
            "symbol": symbol,
            "type": interval_names[timeframe_minutes],
            "startAt": start_at,
            "endAt": end_at,
        },
    )
    normalized: list[dict[str, Any]] = []
    for row in rows if isinstance(rows, list) else []:
        if not isinstance(row, (list, tuple)) or len(row) < 7:
            continue
        timestamp = pd.to_datetime(row[0], unit="s", utc=True, errors="coerce")
        opened = safe_float(row[1])
        closed = safe_float(row[2])
        high = safe_float(row[3])
        low = safe_float(row[4])
        volume = safe_float(row[5], 0.0)
        turnover = safe_float(row[6], 0.0)
        if pd.isna(timestamp) or not all(math.isfinite(v) and v > 0 for v in (opened, high, low, closed)):
            continue
        normalized.append(
            {
                "time": timestamp,
                "open": opened,
                "high": high,
                "low": low,
                "close": closed,
                "volume": max(0.0, volume),
                "turnover": max(0.0, turnover),
            }
        )
    if not normalized:
        raise RuntimeError("KuCoin returned no usable SOL spot candles.")
    frame = (
        pd.DataFrame(normalized)
        .drop_duplicates("time")
        .set_index("time")
        .sort_index()
    )
    last_start = pd.Timestamp(frame.index[-1])
    if last_start.tzinfo is None:
        last_start = last_start.tz_localize("UTC")
    if last_start + pd.Timedelta(minutes=timeframe_minutes) > pd.Timestamp(current) - pd.Timedelta(seconds=20):
        frame = frame.iloc[:-1].copy()
    if frame.empty:
        raise RuntimeError("No fully closed SOL spot candle is available.")
    return frame.tail(count)


def add_indicators(frame: pd.DataFrame, config: dict[str, Any]) -> pd.DataFrame:
    periods = config["indicators"]
    out = frame.copy()
    previous_close = out["close"].shift(1)
    true_range = pd.concat(
        [
            out["high"] - out["low"],
            (out["high"] - previous_close).abs(),
            (out["low"] - previous_close).abs(),
        ],
        axis=1,
    ).max(axis=1)
    out["atr"] = true_range.ewm(span=int(periods["atr_period"]), adjust=False, min_periods=int(periods["atr_period"])).mean()
    out["ema_fast"] = out["close"].ewm(span=int(periods["fast_ema"]), adjust=False, min_periods=int(periods["fast_ema"])).mean()
    out["ema_center"] = out["close"].ewm(span=int(periods["center_ema"]), adjust=False, min_periods=int(periods["center_ema"])).mean()
    out["ema_slow"] = out["close"].ewm(span=int(periods["slow_ema"]), adjust=False, min_periods=int(periods["slow_ema"])).mean()
    std_period = int(periods["std_period"])
    out["rolling_median"] = out["close"].rolling(std_period, min_periods=std_period).median()
    out["rolling_std"] = out["close"].rolling(std_period, min_periods=std_period).std(ddof=0)
    return out


def range_snapshot(
    row: pd.Series,
    time_utc: pd.Timestamp,
    eur_usdt_rate: float,
    config: dict[str, Any],
) -> RangeSnapshot:
    price_usdt = safe_float(row["close"])
    atr_usdt = safe_float(row["atr"])
    center_ema = safe_float(row["ema_center"])
    median = safe_float(row["rolling_median"])
    rolling_std = safe_float(row["rolling_std"])
    ema_fast = safe_float(row["ema_fast"])
    ema_slow = safe_float(row["ema_slow"])
    required = (price_usdt, atr_usdt, center_ema, median, rolling_std, ema_fast, ema_slow, eur_usdt_rate)
    if not all(math.isfinite(value) and value > 0 for value in required):
        raise RuntimeError("Insufficient closed-candle history for adaptive range indicators.")

    center_usdt = 0.65 * center_ema + 0.35 * median
    range_cfg = config["range"]
    half_width_usdt = max(
        atr_usdt * safe_float(range_cfg["atr_half_width_multiple"]),
        rolling_std * safe_float(range_cfg["std_half_width_multiple"]),
        center_usdt * safe_float(range_cfg["minimum_half_width_pct"]),
    )
    half_width_usdt = min(
        half_width_usdt,
        center_usdt * safe_float(range_cfg["maximum_half_width_pct"]),
    )
    lower_usdt = max(1e-12, center_usdt - half_width_usdt)
    upper_usdt = center_usdt + half_width_usdt
    position = clamp((price_usdt - lower_usdt) / max(upper_usdt - lower_usdt, 1e-12), 0.0, 1.0)

    trend_atr = (ema_fast - ema_slow) / max(atr_usdt, 1e-12)
    threshold = safe_float(range_cfg["trend_atr_threshold"])
    strong_threshold = safe_float(range_cfg["strong_trend_atr_threshold"])
    if trend_atr >= strong_threshold:
        regime = "STRONG_UPTREND"
    elif trend_atr >= threshold:
        regime = "UPTREND"
    elif trend_atr <= -strong_threshold:
        regime = "STRONG_DOWNTREND"
    elif trend_atr <= -threshold:
        regime = "DOWNTREND"
    else:
        regime = "RANGE"

    allocation = config["allocation"]
    minimum = safe_float(allocation["minimum_sol_weight"])
    maximum = safe_float(allocation["maximum_sol_weight"])
    target = maximum - position * (maximum - minimum)
    if regime in {"UPTREND", "STRONG_UPTREND"}:
        target += safe_float(allocation["uptrend_bias"])
    if regime == "STRONG_UPTREND":
        target += safe_float(allocation["strong_uptrend_extra_bias"])
        target = max(target, safe_float(allocation["strong_uptrend_minimum_weight"]))
    if regime in {"DOWNTREND", "STRONG_DOWNTREND"}:
        target += safe_float(allocation["downtrend_bias"])
    if regime == "STRONG_DOWNTREND":
        target += safe_float(allocation["strong_downtrend_extra_bias"])
        target = min(target, safe_float(allocation["strong_downtrend_maximum_weight"]))
    target = clamp(target, minimum, maximum)

    price_eur = price_usdt / eur_usdt_rate
    center_eur = center_usdt / eur_usdt_rate
    half_width_eur = half_width_usdt / eur_usdt_rate
    return RangeSnapshot(
        time_utc=iso_utc(time_utc),
        price_eur=price_eur,
        lower_eur=max(1e-12, center_eur - half_width_eur),
        center_eur=center_eur,
        upper_eur=center_eur + half_width_eur,
        half_width_pct=half_width_usdt / center_usdt * 100.0,
        atr_eur=atr_usdt / eur_usdt_rate,
        volatility_pct=atr_usdt / price_usdt * 100.0,
        trend_atr=trend_atr,
        regime=regime,
        target_sol_weight=target,
    )


def new_state(config: dict[str, Any], current: datetime | None = None) -> dict[str, Any]:
    now = iso_utc(current)
    capital = safe_float(config["initial_capital_eur"])
    return {
        "schema_version": 1,
        "strategy": config["strategy_name"],
        "mode": "PAPER_ONLY",
        "asset": "SOL",
        "symbol": "SOL-USDT",
        "created_utc": now,
        "updated_utc": now,
        "initial_capital_eur": capital,
        "cash_eur": capital,
        "sol_units": 0.0,
        "average_cost_eur": 0.0,
        "realized_pnl_eur": 0.0,
        "fees_paid_eur": 0.0,
        "peak_equity_eur": capital,
        "maximum_drawdown_pct": 0.0,
        "last_candle_time_utc": None,
        "last_price_eur": None,
        "last_range": None,
        "trade_count": 0,
        "publication": {"last_report_utc": None},
        "notifications": {"last_digest_utc": None},
    }


def load_state(config: dict[str, Any]) -> dict[str, Any]:
    if not STATE_PATH.exists():
        return new_state(config)
    state = json.loads(STATE_PATH.read_text(encoding="utf-8"))
    if str(state.get("mode", "")).upper() != "PAPER_ONLY":
        raise SafetyError("Persistent state is not marked PAPER_ONLY.")
    if str(state.get("asset", "")).upper() != "SOL":
        raise SafetyError("Persistent state is not SOL-only.")
    for key in ("cash_eur", "sol_units"):
        value = safe_float(state.get(key), -1.0)
        if value < -1e-8:
            raise SafetyError(f"Persistent state contains negative {key}.")
    return state


def save_state(state: dict[str, Any], config: dict[str, Any]) -> None:
    validate_config(config)
    cash = max(0.0, safe_float(state.get("cash_eur"), 0.0))
    units = max(0.0, safe_float(state.get("sol_units"), 0.0))
    state["cash_eur"] = cash
    state["sol_units"] = units
    state["updated_utc"] = iso_utc()
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    STATE_PATH.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")
    CONFIG_SNAPSHOT_PATH.write_text(json.dumps(config, ensure_ascii=False, indent=2), encoding="utf-8")


def portfolio_snapshot(state: dict[str, Any], price_eur: float) -> dict[str, float]:
    cash = max(0.0, safe_float(state.get("cash_eur"), 0.0))
    units = max(0.0, safe_float(state.get("sol_units"), 0.0))
    sol_value = units * price_eur
    equity = cash + sol_value
    weight = sol_value / equity if equity > 0 else 0.0
    return {
        "cash_eur": cash,
        "sol_units": units,
        "sol_value_eur": sol_value,
        "equity_eur": equity,
        "sol_weight": weight,
    }


def append_csv(path: Path, fields: list[str], row: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    exists = path.exists() and path.stat().st_size > 0
    with path.open("a", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        if not exists:
            writer.writeheader()
        writer.writerow({key: row.get(key, "") for key in fields})


def execute_rebalance(
    state: dict[str, Any],
    snapshot: RangeSnapshot,
    config: dict[str, Any],
    *,
    record: bool = True,
) -> dict[str, Any] | None:
    validate_config(config)
    current = portfolio_snapshot(state, snapshot.price_eur)
    equity = current["equity_eur"]
    if equity <= 0:
        raise SafetyError("Paper portfolio equity is not positive.")

    allocation = config["allocation"]
    target_value = snapshot.target_sol_weight * equity
    difference = target_value - current["sol_value_eur"]
    threshold = max(
        safe_float(allocation["minimum_trade_eur"]),
        equity * safe_float(allocation["rebalance_band_fraction"]),
    )
    if abs(difference) < threshold:
        return None

    trade_limit = equity * safe_float(allocation["maximum_trade_fraction_of_equity"])
    fee_rate = safe_float(config["execution"]["fee_bps"]) / 10000.0
    slippage_rate = safe_float(config["execution"]["slippage_bps"]) / 10000.0
    trade_id = int(state.get("trade_count", 0)) + 1

    if difference > 0:
        reserve = equity * safe_float(allocation["minimum_cash_reserve_fraction"])
        spendable = max(0.0, current["cash_eur"] - reserve)
        total_spend = min(difference, trade_limit, spendable)
        if total_spend < safe_float(allocation["minimum_trade_eur"]):
            return None
        execution_price = snapshot.price_eur * (1.0 + slippage_rate)
        gross = total_spend / (1.0 + fee_rate)
        fee = total_spend - gross
        quantity = gross / execution_price
        old_units = current["sol_units"]
        old_cost = safe_float(state.get("average_cost_eur"), 0.0)
        new_units = old_units + quantity
        new_cost_total = old_units * old_cost + total_spend
        state["cash_eur"] = current["cash_eur"] - total_spend
        state["sol_units"] = new_units
        state["average_cost_eur"] = new_cost_total / new_units if new_units > 0 else 0.0
        realized = 0.0
        side = "BUY"
        gross_eur = gross
        reason = "TARGET_WEIGHT_BELOW_RANGE_POSITION"
    else:
        gross_target = min(-difference, trade_limit, current["sol_value_eur"])
        execution_price = snapshot.price_eur * (1.0 - slippage_rate)
        quantity = min(current["sol_units"], gross_target / execution_price)
        gross = quantity * execution_price
        if gross < safe_float(allocation["minimum_trade_eur"]):
            return None
        fee = gross * fee_rate
        proceeds = gross - fee
        average_cost = safe_float(state.get("average_cost_eur"), 0.0)
        realized = proceeds - quantity * average_cost
        state["cash_eur"] = current["cash_eur"] + proceeds
        state["sol_units"] = max(0.0, current["sol_units"] - quantity)
        if state["sol_units"] <= 1e-12:
            state["sol_units"] = 0.0
            state["average_cost_eur"] = 0.0
        state["realized_pnl_eur"] = safe_float(state.get("realized_pnl_eur"), 0.0) + realized
        side = "SELL"
        gross_eur = gross
        reason = "TARGET_WEIGHT_ABOVE_RANGE_POSITION"

    state["fees_paid_eur"] = safe_float(state.get("fees_paid_eur"), 0.0) + fee
    state["trade_count"] = trade_id
    after = portfolio_snapshot(state, snapshot.price_eur)
    if state["cash_eur"] < -1e-7 or state["sol_units"] < -1e-12:
        raise SafetyError("Spot-only invariant violated after simulated fill.")

    trade = {
        "trade_id": trade_id,
        "time_utc": snapshot.time_utc,
        "side": side,
        "reason": reason,
        "market_price_eur": round(snapshot.price_eur, 8),
        "execution_price_eur": round(execution_price, 8),
        "quantity_sol": round(quantity, 12),
        "gross_eur": round(gross_eur, 8),
        "fee_eur": round(fee, 8),
        "cash_after_eur": round(after["cash_eur"], 8),
        "sol_after": round(after["sol_units"], 12),
        "average_cost_after_eur": round(safe_float(state.get("average_cost_eur"), 0.0), 8),
        "realized_pnl_eur": round(realized, 8),
        "target_sol_weight": round(snapshot.target_sol_weight, 8),
        "regime": snapshot.regime,
        "range_lower_eur": round(snapshot.lower_eur, 8),
        "range_center_eur": round(snapshot.center_eur, 8),
        "range_upper_eur": round(snapshot.upper_eur, 8),
    }
    if record:
        append_csv(TRADES_PATH, TRADE_FIELDS, trade)
    return trade


def record_equity(
    state: dict[str, Any],
    snapshot: RangeSnapshot,
) -> dict[str, Any]:
    current = portfolio_snapshot(state, snapshot.price_eur)
    peak = max(safe_float(state.get("peak_equity_eur"), 0.0), current["equity_eur"])
    drawdown = (current["equity_eur"] / peak - 1.0) * 100.0 if peak > 0 else 0.0
    state["peak_equity_eur"] = peak
    state["maximum_drawdown_pct"] = min(
        safe_float(state.get("maximum_drawdown_pct"), 0.0),
        drawdown,
    )
    row = {
        "time_utc": snapshot.time_utc,
        "price_eur": round(snapshot.price_eur, 8),
        "cash_eur": round(current["cash_eur"], 8),
        "sol_units": round(current["sol_units"], 12),
        "sol_value_eur": round(current["sol_value_eur"], 8),
        "equity_eur": round(current["equity_eur"], 8),
        "sol_weight": round(current["sol_weight"], 8),
        "peak_equity_eur": round(peak, 8),
        "drawdown_pct": round(drawdown, 8),
        "target_sol_weight": round(snapshot.target_sol_weight, 8),
        "regime": snapshot.regime,
    }
    append_csv(EQUITY_PATH, EQUITY_FIELDS, row)
    return row


def parse_iso(value: Any) -> datetime | None:
    if not value:
        return None
    try:
        parsed = datetime.fromisoformat(str(value).replace("Z", "+00:00"))
        if parsed.tzinfo is None:
            parsed = parsed.replace(tzinfo=timezone.utc)
        return parsed.astimezone(timezone.utc)
    except Exception:
        return None


def recent_trades(limit: int) -> list[dict[str, Any]]:
    if not TRADES_PATH.exists():
        return []
    try:
        frame = pd.read_csv(TRADES_PATH)
    except Exception:
        return []
    if frame.empty:
        return []
    return frame.tail(limit).replace({np.nan: None}).to_dict(orient="records")


def fmt_eur(value: Any) -> str:
    number = safe_float(value, 0.0)
    return f"€{number:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def fmt_pct(value: Any) -> str:
    return f"{safe_float(value, 0.0):+.2f}%".replace(".", ",")



def telegram_credentials() -> tuple[str, str]:
    return (
        os.getenv("TELEGRAM_BOT_TOKEN", "").strip(),
        os.getenv("TELEGRAM_CHAT_ID", "").strip(),
    )


def send_telegram_message(text: str, config: dict[str, Any]) -> dict[str, Any]:
    notifications = config.get("notifications", {})
    if notifications.get("telegram_enabled") is not True:
        return {"configured": False, "sent": False, "reason": "disabled"}
    token, chat_id = telegram_credentials()
    if not token or not chat_id:
        return {"configured": False, "sent": False, "reason": "missing_secrets"}
    response = requests.post(
        f"https://api.telegram.org/bot{token}/sendMessage",
        json={
            "chat_id": chat_id,
            "text": text,
            "parse_mode": "HTML",
            "disable_web_page_preview": True,
        },
        timeout=25,
    )
    response.raise_for_status()
    payload = response.json()
    if not payload.get("ok"):
        raise RuntimeError(f"Telegram API error: {payload}")
    return {"configured": True, "sent": True}


def telegram_trade_message(
    trade: dict[str, Any],
    state: dict[str, Any],
    snapshot: RangeSnapshot,
) -> str:
    current = portfolio_snapshot(state, snapshot.price_eur)
    initial = safe_float(state.get("initial_capital_eur"), 40000.0)
    total_pnl = current["equity_eur"] - initial
    total_return = total_pnl / initial * 100.0 if initial > 0 else 0.0
    average_cost = safe_float(state.get("average_cost_eur"), 0.0)
    unrealized = (snapshot.price_eur - average_cost) * current["sol_units"] if current["sol_units"] > 0 else 0.0
    side = str(trade.get("side", ""))
    icon = "🟢" if side == "BUY" else "🔴"
    action = "ACQUISTO VIRTUALE" if side == "BUY" else "VENDITA VIRTUALE"
    realized = safe_float(trade.get("realized_pnl_eur"), 0.0)
    result_line = (
        f"P/L realizzato operazione: <b>{fmt_eur(realized)}</b>"
        if side == "SELL"
        else "P/L realizzato operazione: <b>€0,00</b> (posizione aumentata)"
    )
    return "\n".join([
        f"{icon} <b>SOL Spot Adaptive — {action}</b>",
        "",
        f"Operazione n. <b>{int(float(trade.get('trade_id', 0)))}</b>",
        f"Motivo: <b>{trade.get('reason', '')}</b>",
        f"Regime: <b>{snapshot.regime}</b>",
        f"Quantità: <b>{safe_float(trade.get('quantity_sol')):.6f} SOL</b>",
        f"Prezzo simulato: <b>{fmt_eur(trade.get('execution_price_eur'))}</b>",
        f"Controvalore: <b>{fmt_eur(trade.get('gross_eur'))}</b>",
        f"Fee simulata: <b>{fmt_eur(trade.get('fee_eur'))}</b>",
        result_line,
        "",
        f"Equity conto: <b>{fmt_eur(current['equity_eur'])}</b>",
        f"Risultato totale: <b>{fmt_eur(total_pnl)} ({fmt_pct(total_return)})</b>",
        f"P/L realizzato cumulato: <b>{fmt_eur(state.get('realized_pnl_eur', 0.0))}</b>",
        f"P/L non realizzato stimato: <b>{fmt_eur(unrealized)}</b>",
        f"Liquidità: <b>{fmt_eur(current['cash_eur'])}</b>",
        f"SOL detenuti: <b>{current['sol_units']:.6f}</b>",
        f"Valore SOL: <b>{fmt_eur(current['sol_value_eur'])}</b>",
        f"Peso SOL: <b>{current['sol_weight'] * 100:.2f}%</b> → obiettivo <b>{snapshot.target_sol_weight * 100:.2f}%</b>",
        "",
        f"Range: {fmt_eur(snapshot.lower_eur)} — {fmt_eur(snapshot.center_eur)} — {fmt_eur(snapshot.upper_eur)}",
        f"Prezzo SOL: <b>{fmt_eur(snapshot.price_eur)}</b>",
        f"Drawdown massimo: <b>{fmt_pct(state.get('maximum_drawdown_pct', 0.0))}</b>",
        "",
        "🧪 Simulazione paper trading: nessuna operazione reale inviata a KuCoin.",
    ])


def telegram_digest_message(
    state: dict[str, Any],
    snapshot: RangeSnapshot,
    current: dict[str, Any],
) -> str:
    initial = safe_float(state.get("initial_capital_eur"), 40000.0)
    equity = safe_float(current.get("equity_eur"), 0.0)
    total_pnl = equity - initial
    total_return = total_pnl / initial * 100.0 if initial > 0 else 0.0
    average_cost = safe_float(state.get("average_cost_eur"), 0.0)
    unrealized = (snapshot.price_eur - average_cost) * safe_float(current.get("sol_units"), 0.0) if safe_float(current.get("sol_units"), 0.0) > 0 else 0.0
    return "\n".join([
        "📊 <b>SOL Spot Adaptive — riepilogo periodico</b>",
        "",
        f"Equity: <b>{fmt_eur(equity)}</b>",
        f"Guadagno/perdita totale: <b>{fmt_eur(total_pnl)} ({fmt_pct(total_return)})</b>",
        f"P/L realizzato: <b>{fmt_eur(state.get('realized_pnl_eur', 0.0))}</b>",
        f"P/L non realizzato stimato: <b>{fmt_eur(unrealized)}</b>",
        f"Fee simulate cumulative: <b>{fmt_eur(state.get('fees_paid_eur', 0.0))}</b>",
        f"Operazioni simulate: <b>{int(state.get('trade_count', 0))}</b>",
        "",
        f"Liquidità: <b>{fmt_eur(current.get('cash_eur'))}</b>",
        f"SOL detenuti: <b>{safe_float(current.get('sol_units')):.6f}</b>",
        f"Valore SOL: <b>{fmt_eur(current.get('sol_value_eur'))}</b>",
        f"Peso SOL: <b>{safe_float(current.get('sol_weight')) * 100:.2f}%</b>",
        f"Peso obiettivo: <b>{snapshot.target_sol_weight * 100:.2f}%</b>",
        "",
        f"Prezzo SOL: <b>{fmt_eur(snapshot.price_eur)}</b>",
        f"Range adattivo: {fmt_eur(snapshot.lower_eur)} — {fmt_eur(snapshot.center_eur)} — {fmt_eur(snapshot.upper_eur)}",
        f"Regime: <b>{snapshot.regime}</b>",
        f"Volatilità ATR: <b>{snapshot.volatility_pct:.2f}%</b>",
        f"Drawdown attuale: <b>{fmt_pct(current.get('drawdown_pct', 0.0))}</b>",
        f"Drawdown massimo: <b>{fmt_pct(state.get('maximum_drawdown_pct', 0.0))}</b>",
        "",
        "🧪 Solo paper trading spot, senza leva, short o ordini reali.",
    ])


def digest_due(state: dict[str, Any], config: dict[str, Any], current: datetime) -> bool:
    notifications = config.get("notifications", {})
    if notifications.get("send_periodic_digest") is not True:
        return False
    if os.getenv("GITHUB_EVENT_NAME", "") == "workflow_dispatch":
        return True
    last = parse_iso(state.get("notifications", {}).get("last_digest_utc"))
    interval = timedelta(hours=safe_float(notifications.get("digest_interval_hours"), 4.0))
    return last is None or current - last >= interval


def render_report(
    state: dict[str, Any],
    snapshot: RangeSnapshot,
    current: dict[str, Any],
    config: dict[str, Any],
    eur_usdt_rate: float,
    rate_source: str,
    trades_this_cycle: list[dict[str, Any]],
) -> str:
    initial = safe_float(state.get("initial_capital_eur"), 40000.0)
    equity = safe_float(current.get("equity_eur"), 0.0)
    total_return = (equity / initial - 1.0) * 100.0 if initial > 0 else 0.0
    recent = recent_trades(int(config["publishing"].get("recent_trades_in_report", 12)))
    lines = [
        "# SOL Spot Adaptive Range — paper trading",
        "",
        f"Generato: {iso_utc()}",
        "",
        "## Vincoli di sicurezza",
        "",
        "- Modalità: **PAPER ONLY**",
        "- Asset: **SOL soltanto**",
        "- Mercato simulato: **spot SOL-USDT**",
        "- Capitale iniziale: **€40.000**",
        "- Leva: **1× (nessuna leva)**",
        "- Short: **disabilitati**",
        "- Ordini reali: **impossibili; il codice usa soltanto dati pubblici GET**",
        "",
        "## Stato portafoglio",
        "",
        "| Voce | Valore |",
        "| --- | ---: |",
        f"| Equity | {fmt_eur(equity)} |",
        f"| Rendimento totale | {fmt_pct(total_return)} |",
        f"| Liquidità | {fmt_eur(current['cash_eur'])} |",
        f"| SOL detenuti | {current['sol_units']:.6f} |",
        f"| Valore SOL | {fmt_eur(current['sol_value_eur'])} |",
        f"| Peso SOL attuale | {current['sol_weight'] * 100:.2f}% |",
        f"| Peso SOL obiettivo | {snapshot.target_sol_weight * 100:.2f}% |",
        f"| P/L realizzato | {fmt_eur(state.get('realized_pnl_eur', 0.0))} |",
        f"| Commissioni simulate | {fmt_eur(state.get('fees_paid_eur', 0.0))} |",
        f"| Drawdown massimo | {fmt_pct(state.get('maximum_drawdown_pct', 0.0))} |",
        f"| Operazioni simulate | {int(state.get('trade_count', 0))} |",
        "",
        "## Range adattivo corrente",
        "",
        "| Voce | Valore |",
        "| --- | ---: |",
        f"| Prezzo SOL | {fmt_eur(snapshot.price_eur)} |",
        f"| Limite inferiore | {fmt_eur(snapshot.lower_eur)} |",
        f"| Centro | {fmt_eur(snapshot.center_eur)} |",
        f"| Limite superiore | {fmt_eur(snapshot.upper_eur)} |",
        f"| Semilarghezza | {snapshot.half_width_pct:.2f}% |",
        f"| ATR | {fmt_eur(snapshot.atr_eur)} ({snapshot.volatility_pct:.2f}%) |",
        f"| Regime | **{snapshot.regime}** |",
        f"| Trend normalizzato ATR | {snapshot.trend_atr:+.2f} |",
        f"| EUR/USDT | {eur_usdt_rate:.6f} ({rate_source}) |",
        "",
        "La strategia aumenta gradualmente il peso SOL nella parte bassa del range e lo riduce nella parte alta. Il range si allarga con ATR e deviazione standard e viene inclinato dal trend, senza mai usare debito o vendere SOL non posseduti.",
        "",
    ]
    if trades_this_cycle:
        lines += ["## Movimenti di questo ciclo", ""]
        for trade in trades_this_cycle:
            lines.append(
                f"- **{trade['side']}** {float(trade['quantity_sol']):.6f} SOL a {fmt_eur(trade['execution_price_eur'])}; "
                f"controvalore {fmt_eur(trade['gross_eur'])}, fee {fmt_eur(trade['fee_eur'])}."
            )
        lines.append("")
    lines += ["## Ultime operazioni", ""]
    if not recent:
        lines.append("_Nessuna operazione simulata ancora registrata._")
    else:
        lines += [
            "| # | Data UTC | Lato | Quantità SOL | Prezzo | Controvalore | P/L realizzato | Regime |",
            "| ---: | --- | --- | ---: | ---: | ---: | ---: | --- |",
        ]
        for trade in reversed(recent):
            lines.append(
                f"| {int(float(trade.get('trade_id', 0)))} | {trade.get('time_utc', '')} | {trade.get('side', '')} | "
                f"{safe_float(trade.get('quantity_sol'), 0.0):.6f} | {fmt_eur(trade.get('execution_price_eur'))} | "
                f"{fmt_eur(trade.get('gross_eur'))} | {fmt_eur(trade.get('realized_pnl_eur'))} | {trade.get('regime', '')} |"
            )
    lines += [
        "",
        "## Nota metodologica",
        "",
        "I risultati includono fee e slippage configurati, ma restano una simulazione. Non sono una promessa di rendimento e non attivano alcuna operazione sull'exchange.",
        "",
    ]
    return "\n".join(lines)


def report_due(
    state: dict[str, Any],
    config: dict[str, Any],
    current: datetime,
    trade_happened: bool,
) -> bool:
    if trade_happened or not REPORT_PATH.exists():
        return True
    if os.getenv("GITHUB_EVENT_NAME", "") == "workflow_dispatch":
        return True
    last = parse_iso(state.get("publication", {}).get("last_report_utc"))
    interval = timedelta(hours=safe_float(config["publishing"]["report_interval_hours"], 4.0))
    return last is None or current - last >= interval


def run_cycle(config: dict[str, Any], now: datetime | None = None) -> dict[str, Any]:
    validate_config(config)
    current_time = now or utc_now()
    session = make_session()
    eur_usdt_rate, rate_source = fetch_eur_usdt_rate(
        session, safe_float(config.get("eur_usdt_fallback_rate"), 1.0)
    )
    frame_usdt = fetch_spot_klines(
        session,
        config["symbol"],
        int(config["timeframe_minutes"]),
        int(config["lookback_candles"]),
        now=current_time,
    )
    frame = frame_usdt.copy()
    for column in ("open", "high", "low", "close"):
        frame[column] = frame[column] / eur_usdt_rate
    frame = add_indicators(frame, config)
    minimum_history = max(int(value) for value in config["indicators"].values())
    usable = frame.dropna(subset=["atr", "ema_fast", "ema_center", "ema_slow", "rolling_median", "rolling_std"])
    if len(frame) < minimum_history or usable.empty:
        raise RuntimeError(
            f"Only {len(frame)} closed candles available; at least {minimum_history} are required."
        )

    state = load_state(config)
    last_time = parse_iso(state.get("last_candle_time_utc"))
    indices = [pd.Timestamp(index) for index in usable.index]
    pending = [index for index in indices if last_time is None or index.to_pydatetime() > last_time]
    if last_time is None and pending:
        pending = pending[-1:]

    trades_this_cycle: list[dict[str, Any]] = []
    latest_snapshot: RangeSnapshot | None = None
    latest_equity: dict[str, Any] | None = None
    for index in pending:
        row = usable.loc[index]
        # Values are already converted to EUR above, so the conversion rate is 1 here.
        latest_snapshot = range_snapshot(row, index, 1.0, config)
        trade = execute_rebalance(state, latest_snapshot, config)
        if trade:
            trades_this_cycle.append(trade)
        latest_equity = record_equity(state, latest_snapshot)
        state["last_candle_time_utc"] = latest_snapshot.time_utc
        state["last_price_eur"] = latest_snapshot.price_eur
        state["last_range"] = latest_snapshot.__dict__

    if latest_snapshot is None:
        last_index = pd.Timestamp(usable.index[-1])
        latest_snapshot = range_snapshot(usable.iloc[-1], last_index, 1.0, config)
        latest_equity = portfolio_snapshot(state, latest_snapshot.price_eur)
        latest_equity.update(
            {
                "peak_equity_eur": safe_float(state.get("peak_equity_eur"), latest_equity["equity_eur"]),
                "drawdown_pct": (
                    latest_equity["equity_eur"] / max(safe_float(state.get("peak_equity_eur"), latest_equity["equity_eur"]), 1e-12) - 1.0
                ) * 100.0,
                "target_sol_weight": latest_snapshot.target_sol_weight,
                "regime": latest_snapshot.regime,
            }
        )

    latest = {
        "generated_utc": iso_utc(current_time),
        "mode": "PAPER_ONLY",
        "asset": "SOL",
        "symbol": "SOL-USDT",
        "source": "KUCOIN_PUBLIC_SPOT_API",
        "eur_usdt_rate": eur_usdt_rate,
        "eur_usdt_rate_source": rate_source,
        "new_closed_candles": len(pending),
        "trades_this_cycle": trades_this_cycle,
        "portfolio": latest_equity,
        "range": latest_snapshot.__dict__,
        "safety": {
            "real_orders_enabled": False,
            "allow_short": False,
            "leverage": 1.0,
            "public_data_only": True,
        },
    }
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    LATEST_PATH.write_text(json.dumps(latest, ensure_ascii=False, indent=2), encoding="utf-8")

    if report_due(state, config, current_time, bool(trades_this_cycle)):
        report = render_report(
            state,
            latest_snapshot,
            latest_equity,
            config,
            eur_usdt_rate,
            rate_source,
            trades_this_cycle,
        )
        REPORT_PATH.write_text(report, encoding="utf-8")
        state.setdefault("publication", {})["last_report_utc"] = iso_utc(current_time)
        latest["report_updated"] = True
    else:
        latest["report_updated"] = False

    telegram_results: list[dict[str, Any]] = []
    notifications = config.get("notifications", {})
    if notifications.get("send_trade_events") is True:
        for trade in trades_this_cycle:
            try:
                telegram_results.append(send_telegram_message(telegram_trade_message(trade, state, latest_snapshot), config))
            except Exception as exc:
                telegram_results.append({"configured": True, "sent": False, "error": str(exc)})
                print(f"Telegram trade notification failed: {exc}")
    if digest_due(state, config, current_time):
        try:
            digest_result = send_telegram_message(telegram_digest_message(state, latest_snapshot, latest_equity), config)
            telegram_results.append({"type": "digest", **digest_result})
            if digest_result.get("sent"):
                state.setdefault("notifications", {})["last_digest_utc"] = iso_utc(current_time)
        except Exception as exc:
            telegram_results.append({"type": "digest", "configured": True, "sent": False, "error": str(exc)})
            print(f"Telegram digest failed: {exc}")
    latest["telegram"] = telegram_results

    save_state(state, config)
    LATEST_PATH.write_text(json.dumps(latest, ensure_ascii=False, indent=2), encoding="utf-8")
    return latest


def self_test(config_path: Path = CONFIG_PATH) -> None:
    config = json.loads(config_path.read_text(encoding="utf-8")) if config_path.exists() else {
        "mode": "PAPER_ONLY",
        "strategy_name": "SOL Spot Adaptive Range",
        "asset": "SOL",
        "symbol": "SOL-USDT",
        "initial_capital_eur": 40000.0,
        "public_data_only": True,
        "real_orders_enabled": False,
        "allow_short": False,
        "leverage": 1.0,
        "allocation": {
            "minimum_sol_weight": 0.10,
            "maximum_sol_weight": 0.90,
            "minimum_cash_reserve_fraction": 0.10,
            "rebalance_band_fraction": 0.04,
            "maximum_trade_fraction_of_equity": 0.15,
            "minimum_trade_eur": 250.0,
        },
        "execution": {"fee_bps": 10.0, "slippage_bps": 2.0},
    }
    validate_config(config)
    state = new_state(config, datetime(2026, 7, 13, tzinfo=timezone.utc))
    buy_snapshot = RangeSnapshot(
        time_utc="2026-07-13T00:00:00+00:00",
        price_eur=100.0,
        lower_eur=90.0,
        center_eur=110.0,
        upper_eur=130.0,
        half_width_pct=18.18,
        atr_eur=2.0,
        volatility_pct=2.0,
        trend_atr=0.0,
        regime="RANGE",
        target_sol_weight=0.80,
    )
    buy = execute_rebalance(state, buy_snapshot, config, record=False)
    assert buy and buy["side"] == "BUY"
    assert state["cash_eur"] >= 4000.0 - 1e-6
    assert state["sol_units"] > 0
    sell_snapshot = RangeSnapshot(
        time_utc="2026-07-13T00:15:00+00:00",
        price_eur=120.0,
        lower_eur=90.0,
        center_eur=105.0,
        upper_eur=120.0,
        half_width_pct=14.29,
        atr_eur=2.0,
        volatility_pct=1.67,
        trend_atr=0.0,
        regime="RANGE",
        target_sol_weight=0.10,
    )
    sell = execute_rebalance(state, sell_snapshot, config, record=False)
    assert sell and sell["side"] == "SELL"
    assert state["cash_eur"] >= 0
    assert state["sol_units"] >= 0
    assert config["leverage"] == 1.0
    assert config["allow_short"] is False
    assert config["real_orders_enabled"] is False
    print(json.dumps({"self_test": "PASS", "cash_eur": state["cash_eur"], "sol_units": state["sol_units"]}))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default=str(CONFIG_PATH))
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    config_path = Path(args.config)
    if args.self_test:
        self_test(config_path)
        return
    config = load_config(config_path)
    try:
        result = run_cycle(config)
    except Exception as exc:
        if config.get("notifications", {}).get("send_errors") is True:
            try:
                send_telegram_message(
                    "🚨 <b>SOL Spot Adaptive — errore</b>\n\n"
                    f"Il ciclo paper trading non è stato completato.\n"
                    f"Errore: <code>{str(exc)[:1200]}</code>\n\n"
                    "Nessun ordine reale può essere stato inviato.",
                    config,
                )
            except Exception as notify_exc:
                print(f"Telegram error notification failed: {notify_exc}")
        raise
    print(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    main()
