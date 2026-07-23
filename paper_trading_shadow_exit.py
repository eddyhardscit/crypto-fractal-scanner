# -*- coding: utf-8 -*-
"""Passive Block 3 shadow-exit simulator for Paper Trading.

The engine never changes a real Paper position.  It creates independent
counterfactual exit variants that share the original entry, quantity, initial
protective stop and observed market path.  Variants can exit before or after
the original trade, allowing the reports to distinguish:

- an earlier exit that protected profit;
- an earlier exit that cut a winner too soon;
- a later exit that captured additional trend;
- a later exit that returned too much profit.

Only completed 15-minute OHLC candles are used.  Same-candle ambiguities are
resolved conservatively.  Funding is excluded from both the actual and shadow
comparison because a reliable historical funding series is not available in
the Paper bundle; actual P&L is therefore compared net of fees but excluding
funding on both sides.
"""

from __future__ import annotations

import csv
import json
import math
import statistics
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

import pandas as pd

from kucoin_public_data import bundle_frames, safe_float

REPORTS_DIR = Path("reports")
STATE_PATH = REPORTS_DIR / "paper_trading_shadow_exit_state.json"
EVENTS_PATH = REPORTS_DIR / "paper_trading_shadow_exit_events.csv"
RESULTS_PATH = REPORTS_DIR / "paper_trading_shadow_exit_results.csv"
METRICS_PATH = REPORTS_DIR / "paper_trading_shadow_exit_metrics.csv"
REPORT_PATH = REPORTS_DIR / "paper_trading_shadow_exit_report.md"
CONFIG_SNAPSHOT_PATH = REPORTS_DIR / "paper_trading_shadow_exit_config_snapshot.json"
CONFIG_PATH = Path("config/shadow_exit_block3.json")
TRADE_LOG_PATH = REPORTS_DIR / "paper_trading_trade_log.csv"

ENGINE_VERSION = "block3-shadow-exit-v1"
STATE_SCHEMA_VERSION = 1
RESULT_SCHEMA_VERSION = 1

EVENT_FIELDS = [
    "timestamp",
    "event_type",
    "trade_key",
    "trade_id",
    "portfolio",
    "asset",
    "side",
    "scenario_id",
    "scenario_version",
    "reason",
    "price",
    "net_pnl_ex_funding_eur",
    "quality",
    "same_candle_ambiguous",
]

RESULT_FIELDS = [
    "schema_version",
    "engine_version",
    "risk_model_version",
    "scenario_set_version",
    "scenario_id",
    "scenario_kind",
    "scenario_parameters_json",
    "trade_key",
    "trade_id",
    "portfolio",
    "strategy",
    "asset",
    "symbol",
    "side",
    "timeframe_minutes",
    "opened_at",
    "actual_closed_at",
    "shadow_closed_at",
    "actual_close_reason",
    "shadow_close_reason",
    "entry_price",
    "actual_exit_price",
    "shadow_exit_price",
    "quantity",
    "margin_eur",
    "initial_risk_eur",
    "actual_net_pnl_eur",
    "actual_funding_pnl_eur",
    "actual_comparable_pnl_eur",
    "shadow_comparable_pnl_eur",
    "delta_vs_actual_eur",
    "actual_holding_hours",
    "shadow_holding_hours",
    "timing_relation",
    "timing_assessment",
    "full_from_entry",
    "observation_quality",
    "observed_candles",
    "candle_gap_count",
    "same_candle_ambiguity_count",
    "result_quality",
]

METRIC_FIELDS = [
    "generated_utc",
    "scope",
    "portfolio",
    "scenario_id",
    "scenario_kind",
    "sample_total",
    "sample_full_from_entry",
    "sample_partial",
    "average_actual_comparable_pnl_eur",
    "average_shadow_comparable_pnl_eur",
    "average_delta_vs_actual_eur",
    "median_delta_vs_actual_eur",
    "total_delta_vs_actual_eur",
    "improved_count",
    "worsened_count",
    "equal_count",
    "improved_pct",
    "shadow_win_rate_pct",
    "actual_win_rate_pct",
    "shadow_profit_factor",
    "shadow_expectancy_eur",
    "earlier_better_count",
    "too_early_count",
    "later_better_count",
    "too_late_count",
    "same_time_better_count",
    "same_time_worse_count",
    "ambiguous_count",
    "data_stage",
]

DEFAULT_CONFIG: dict[str, Any] = {
    "schema_version": 1,
    "scenario_set_version": "block3-v1-r-matrix",
    "enabled": True,
    "timeframe_minutes": 15,
    "minimum_evaluation_horizon_hours": 24.0,
    "evaluation_horizon_multiplier": 2.0,
    "maximum_evaluation_horizon_hours": 168.0,
    "comparison_tolerance_eur": 0.01,
    "scenarios": [
        {"id": "GB20_R050", "kind": "MFE_GIVEBACK", "activation_r": 0.5, "giveback_fraction": 0.20},
        {"id": "GB30_R050", "kind": "MFE_GIVEBACK", "activation_r": 0.5, "giveback_fraction": 0.30},
        {"id": "GB40_R050", "kind": "MFE_GIVEBACK", "activation_r": 0.5, "giveback_fraction": 0.40},
        {"id": "GB50_R050", "kind": "MFE_GIVEBACK", "activation_r": 0.5, "giveback_fraction": 0.50},
        {"id": "GB20_R100", "kind": "MFE_GIVEBACK", "activation_r": 1.0, "giveback_fraction": 0.20},
        {"id": "GB30_R100", "kind": "MFE_GIVEBACK", "activation_r": 1.0, "giveback_fraction": 0.30},
        {"id": "GB40_R100", "kind": "MFE_GIVEBACK", "activation_r": 1.0, "giveback_fraction": 0.40},
        {"id": "GB50_R100", "kind": "MFE_GIVEBACK", "activation_r": 1.0, "giveback_fraction": 0.50},
        {"id": "TP_R050", "kind": "FIXED_R", "target_r": 0.5},
        {"id": "TP_R100", "kind": "FIXED_R", "target_r": 1.0},
        {"id": "TP_R150", "kind": "FIXED_R", "target_r": 1.5},
        {"id": "TP_R200", "kind": "FIXED_R", "target_r": 2.0},
        {"id": "BE_R050", "kind": "BREAKEVEN", "activation_r": 0.5},
        {"id": "BE_R100", "kind": "BREAKEVEN", "activation_r": 1.0},
        {"id": "ATR15_R100", "kind": "ATR_TRAIL", "activation_r": 1.0, "atr_multiple": 1.5},
        {"id": "ATR20_R100", "kind": "ATR_TRAIL", "activation_r": 1.0, "atr_multiple": 2.0},
        {"id": "ATR30_R100", "kind": "ATR_TRAIL", "activation_r": 1.0, "atr_multiple": 3.0},
        {"id": "TIME_6H", "kind": "TIME_EXIT", "hours": 6.0},
        {"id": "TIME_12H", "kind": "TIME_EXIT", "hours": 12.0},
        {"id": "TIME_24H", "kind": "TIME_EXIT", "hours": 24.0},
    ],
}


def now_utc() -> datetime:
    return datetime.now(timezone.utc)


def iso_utc(value: datetime | None = None) -> str:
    return (value or now_utc()).astimezone(timezone.utc).isoformat(timespec="seconds")


def parse_time(value: Any) -> datetime | None:
    if value in (None, ""):
        return None
    try:
        parsed = pd.Timestamp(value)
        if parsed.tzinfo is None:
            parsed = parsed.tz_localize("UTC")
        return parsed.to_pydatetime().astimezone(timezone.utc)
    except Exception:
        return None


def finite_float(value: Any, default: float = 0.0) -> float:
    try:
        number = float(value)
    except (TypeError, ValueError):
        return default
    return number if math.isfinite(number) else default


def optional_float(value: Any) -> float | None:
    if value in (None, ""):
        return None
    try:
        number = float(value)
    except (TypeError, ValueError):
        return None
    return number if math.isfinite(number) else None


def atomic_write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    temporary.replace(path)


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists() or path.stat().st_size == 0:
        return []
    try:
        with path.open("r", encoding="utf-8-sig", newline="") as handle:
            return list(csv.DictReader(handle))
    except Exception:
        return []


def write_csv(path: Path, fields: list[str], rows: Iterable[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    with temporary.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fields})
    temporary.replace(path)


def append_events(rows: list[dict[str, Any]]) -> None:
    if not rows:
        return
    existing = read_csv(EVENTS_PATH)
    keys = {
        (
            row.get("timestamp", ""),
            row.get("event_type", ""),
            row.get("trade_key", ""),
            row.get("scenario_id", ""),
            row.get("reason", ""),
        )
        for row in existing
    }
    merged: list[dict[str, Any]] = list(existing)
    for row in rows:
        key = (
            str(row.get("timestamp", "")),
            str(row.get("event_type", "")),
            str(row.get("trade_key", "")),
            str(row.get("scenario_id", "")),
            str(row.get("reason", "")),
        )
        if key not in keys:
            merged.append(row)
            keys.add(key)
    write_csv(EVENTS_PATH, EVENT_FIELDS, merged)


def load_config() -> dict[str, Any]:
    config = json.loads(json.dumps(DEFAULT_CONFIG))
    if CONFIG_PATH.exists():
        try:
            custom = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
            if isinstance(custom, dict):
                config.update({key: value for key, value in custom.items() if key != "scenarios"})
                if isinstance(custom.get("scenarios"), list):
                    config["scenarios"] = custom["scenarios"]
        except Exception as exc:
            print(f"Configurazione Block 3 non valida, uso default: {exc}")

    seen: set[str] = set()
    scenarios: list[dict[str, Any]] = []
    allowed = {"MFE_GIVEBACK", "FIXED_R", "BREAKEVEN", "ATR_TRAIL", "TIME_EXIT"}
    for raw in config.get("scenarios", []):
        if not isinstance(raw, dict):
            continue
        scenario_id = str(raw.get("id", "")).strip()
        kind = str(raw.get("kind", "")).strip().upper()
        if not scenario_id or scenario_id in seen or kind not in allowed:
            continue
        item = dict(raw)
        item["id"] = scenario_id
        item["kind"] = kind
        scenarios.append(item)
        seen.add(scenario_id)
    config["scenarios"] = scenarios
    # Use atomic replacement instead of opening the existing snapshot in-place.
    # The Block 3 installer validates the module as root, while the scheduled
    # Paper service runs as ``cryptobot``.  Atomic replacement only requires
    # write permission on the reports directory and therefore remains safe
    # even when an older snapshot was created by a different user.
    atomic_write_json(CONFIG_SNAPSHOT_PATH, config)
    return config


def load_state() -> dict[str, Any]:
    if not STATE_PATH.exists():
        return {
            "schema_version": STATE_SCHEMA_VERSION,
            "engine_version": ENGINE_VERSION,
            "created_utc": iso_utc(),
            "updated_utc": iso_utc(),
            "groups": {},
        }
    try:
        state = json.loads(STATE_PATH.read_text(encoding="utf-8"))
        if not isinstance(state, dict):
            raise ValueError("state root is not an object")
    except Exception:
        broken = STATE_PATH.with_suffix(".json.broken")
        try:
            STATE_PATH.replace(broken)
        except OSError:
            pass
        return {
            "schema_version": STATE_SCHEMA_VERSION,
            "engine_version": ENGINE_VERSION,
            "created_utc": iso_utc(),
            "updated_utc": iso_utc(),
            "groups": {},
        }
    state.setdefault("groups", {})
    state["schema_version"] = STATE_SCHEMA_VERSION
    state["engine_version"] = ENGINE_VERSION
    return state


def save_state(state: dict[str, Any], when: datetime) -> None:
    state["updated_utc"] = iso_utc(when)
    atomic_write_json(STATE_PATH, state)


def current_prices(bundle: dict[str, Any]) -> dict[str, float]:
    output: dict[str, float] = {}
    for asset, payload in bundle.get("assets", {}).items():
        price = safe_float(payload.get("mark_price"), float("nan"))
        if math.isfinite(price) and price > 0:
            output[str(asset)] = float(price)
    return output


def slippage_bps(bundle: dict[str, Any], asset: str, paper_config: dict[str, Any]) -> float:
    payload = bundle.get("assets", {}).get(asset, {})
    turnover = safe_float(payload.get("turnover_24h"), 0.0)
    minimum = float(paper_config.get("universe", {}).get("minimum_turnover_24h_usdt", 0.0))
    execution = paper_config.get("execution", {})
    if minimum > 0 and turnover < minimum * 3:
        return float(execution.get("illiquid_slippage_bps", 6.0))
    return float(execution.get("default_slippage_bps", 2.0))


def adverse_exit_price(raw_price: float, side: str, bps: float) -> float:
    direction = 1.0 if side.upper() == "LONG" else -1.0
    return raw_price * (1.0 - direction * bps / 10_000.0)


def comparable_pnl_at_price(
    group: dict[str, Any],
    raw_exit_price: float,
    bundle: dict[str, Any],
    paper_config: dict[str, Any],
) -> tuple[float, float]:
    bps = slippage_bps(bundle, str(group["asset"]), paper_config)
    exit_price = adverse_exit_price(raw_exit_price, str(group["side"]), bps)
    direction = 1.0 if str(group["side"]).upper() == "LONG" else -1.0
    quantity = float(group["quantity"])
    rate = max(float(group.get("eur_usdt_rate", 1.0)), 1e-12)
    gross_eur = (exit_price - float(group["entry_price"])) * quantity * direction / rate
    exit_notional_eur = abs(exit_price * quantity / rate)
    fee_rate = float(paper_config.get("execution", {}).get("taker_fee_bps", 0.0)) / 10_000.0
    exit_fee = exit_notional_eur * fee_rate
    net = gross_eur - float(group.get("entry_fee_eur", 0.0)) - exit_fee
    return exit_price, net


def trade_key(portfolio: str, trade_id: str) -> str:
    return f"{portfolio}:{trade_id}"


def latest_candle_id(frames: dict[str, Any], asset: str, timeframe: int) -> str:
    frame = frames.get(asset, {}).get(timeframe)
    if frame is None or frame.empty:
        return ""
    return pd.Timestamp(frame.index[-1]).isoformat()


def scenario_initial_state(definition: dict[str, Any], group: dict[str, Any]) -> dict[str, Any]:
    return {
        "id": definition["id"],
        "kind": definition["kind"],
        "parameters": {key: value for key, value in definition.items() if key not in {"id", "kind"}},
        "status": "ACTIVE",
        "activated": False,
        "peak_favorable_price": float(group["entry_price"]),
        "stop_price": float(group["initial_stop_price"]),
        "exit_raw_price": None,
        "exit_price": None,
        "exit_time": "",
        "exit_reason": "",
        "comparable_pnl_eur": None,
        "observed_candles": 0,
        "candle_gap_count": 0,
        "same_candle_ambiguity_count": 0,
        "last_candle_time": "",
        "result_written": False,
    }


def evaluation_horizon_hours(position: dict[str, Any], config: dict[str, Any]) -> float:
    original = max(finite_float(position.get("max_holding_hours"), 24.0), 0.25)
    minimum = max(finite_float(config.get("minimum_evaluation_horizon_hours"), 24.0), 0.25)
    multiplier = max(finite_float(config.get("evaluation_horizon_multiplier"), 2.0), 1.0)
    maximum = max(finite_float(config.get("maximum_evaluation_horizon_hours"), 168.0), minimum)
    return min(max(original * multiplier, minimum), maximum)



def scenario_applies_to_group(
    definition: dict[str, Any],
    group: dict[str, Any],
) -> bool:
    """Apply optional scenario portfolio/side filters.

    Missing filters preserve the historical global behaviour.
    """

    def matches(raw: Any, current: Any) -> bool:
        if raw is None:
            return True

        values = (
            raw
            if isinstance(raw, (list, tuple, set))
            else [raw]
        )

        allowed = {
            str(value).strip().upper()
            for value in values
            if str(value).strip()
        }

        current_value = str(current or "").strip().upper()

        return (
            not allowed
            or "*" in allowed
            or current_value in allowed
        )

    return (
        matches(
            definition.get("apply_to_portfolios"),
            group.get("portfolio"),
        )
        and matches(
            definition.get("apply_to_sides"),
            group.get("side"),
        )
    )


def create_group(
    position: dict[str, Any],
    portfolio_name: str,
    block_config: dict[str, Any],
    last_candle: str,
    quality: str,
) -> dict[str, Any]:
    entry = finite_float(position.get("entry_price"))
    initial_stop = finite_float(position.get("initial_stop_price"), finite_float(position.get("stop_price"), entry))
    risk_price = abs(entry - initial_stop)
    if risk_price <= 0:
        risk_price = max(abs(entry) * 0.01, 1e-12)
    group = {
        "trade_key": trade_key(portfolio_name, str(position.get("trade_id", ""))),
        "trade_id": str(position.get("trade_id", "")),
        "portfolio": portfolio_name,
        "strategy": str(position.get("strategy", "")),
        "asset": str(position.get("asset", "")),
        "symbol": str(position.get("symbol", "")),
        "side": str(position.get("side", "")).upper(),
        "timeframe_minutes": int(finite_float(position.get("timeframe_minutes"), 15)),
        "opened_at": str(position.get("opened_at", "")),
        "entry_price": entry,
        "quantity": abs(finite_float(position.get("quantity"))),
        "margin_eur": finite_float(position.get("margin_eur")),
        "initial_risk_eur": finite_float(position.get("initial_risk_eur")),
        "initial_stop_price": initial_stop,
        "liquidation_price": optional_float(position.get("liquidation_price")),
        "initial_risk_price": risk_price,
        "entry_fee_eur": finite_float(position.get("entry_fee_eur")),
        "eur_usdt_rate": max(finite_float(position.get("eur_usdt_rate"), 1.0), 1e-12),
        "atr_pct": max(finite_float(position.get("atr_pct"), 0.0), 0.0),
        "original_max_holding_hours": finite_float(position.get("max_holding_hours"), 24.0),
        "evaluation_horizon_hours": evaluation_horizon_hours(position, block_config),
        "observation_quality": quality,
        "full_from_entry": quality == "FULL_FROM_ENTRY",
        "risk_model_version": str(
            position.get(
                "risk_model_version_at_entry",
                "legacy_pre_block4_5",
            )
        ),
        "scenario_set_version": (
            str(block_config.get("scenario_set_version", "block3-v1"))
            + "|risk="
            + str(
                position.get(
                    "risk_model_version_at_entry",
                    "legacy_pre_block4_5",
                )
            )
        ),
        "last_processed_candle": last_candle,
        "actual": {
            "closed": False,
            "closed_at": "",
            "exit_price": None,
            "net_pnl_eur": None,
            "funding_pnl_eur": None,
            "comparable_pnl_eur": None,
            "holding_hours": None,
            "close_reason": "",
        },
        "scenarios": {},
    }
    group["scenarios"] = {
        definition["id"]: scenario_initial_state(definition, group)
        for definition in block_config.get("scenarios", [])
        if scenario_applies_to_group(definition, group)
    }
    return group


def favorable_r(group: dict[str, Any], favorable_price: float) -> float:
    entry = float(group["entry_price"])
    risk = max(float(group["initial_risk_price"]), 1e-12)
    if str(group["side"]) == "LONG":
        return max(0.0, (favorable_price - entry) / risk)
    return max(0.0, (entry - favorable_price) / risk)


def price_for_r(group: dict[str, Any], multiple: float) -> float:
    direction = 1.0 if str(group["side"]) == "LONG" else -1.0
    return float(group["entry_price"]) + direction * float(group["initial_risk_price"]) * multiple


def touched(side: str, low: float, high: float, level: float, kind: str) -> bool:
    if kind == "UP":
        return high >= level
    if kind == "DOWN":
        return low <= level
    if side == "LONG":
        return low <= level
    return high >= level


def worse_exit(group: dict[str, Any], candidates: list[tuple[str, float]]) -> tuple[str, float]:
    side = str(group["side"])
    if side == "LONG":
        return min(candidates, key=lambda item: item[1])
    return max(candidates, key=lambda item: item[1])


def update_dynamic_levels_after_candle(
    group: dict[str, Any],
    scenario: dict[str, Any],
    candle_high: float,
    candle_low: float,
    candle_close: float,
) -> None:
    side = str(group["side"])
    favorable_price = candle_high if side == "LONG" else candle_low
    old_peak = float(scenario.get("peak_favorable_price", group["entry_price"]))
    new_peak = max(old_peak, favorable_price) if side == "LONG" else min(old_peak, favorable_price)
    scenario["peak_favorable_price"] = new_peak
    peak_r = favorable_r(group, new_peak)
    params = scenario.get("parameters", {})
    kind = str(scenario["kind"])

    if kind == "MFE_GIVEBACK":
        activation = max(finite_float(params.get("activation_r"), 0.5), 0.0)
        if peak_r >= activation:
            scenario["activated"] = True
        if scenario.get("activated"):
            fraction = min(max(finite_float(params.get("giveback_fraction"), 0.3), 0.0), 0.95)
            entry = float(group["entry_price"])
            if side == "LONG":
                candidate = entry + (new_peak - entry) * (1.0 - fraction)
                scenario["stop_price"] = max(float(group["initial_stop_price"]), candidate)
            else:
                candidate = entry - (entry - new_peak) * (1.0 - fraction)
                scenario["stop_price"] = min(float(group["initial_stop_price"]), candidate)

    elif kind == "BREAKEVEN":
        activation = max(finite_float(params.get("activation_r"), 0.5), 0.0)
        if peak_r >= activation:
            scenario["activated"] = True
            if side == "LONG":
                scenario["stop_price"] = max(float(scenario["stop_price"]), float(group["entry_price"]))
            else:
                scenario["stop_price"] = min(float(scenario["stop_price"]), float(group["entry_price"]))

    elif kind == "ATR_TRAIL":
        activation = max(finite_float(params.get("activation_r"), 1.0), 0.0)
        if peak_r >= activation:
            scenario["activated"] = True
        if scenario.get("activated"):
            multiple = max(finite_float(params.get("atr_multiple"), 2.0), 0.0)
            distance = candle_close * float(group.get("atr_pct", 0.0)) / 100.0 * multiple
            if side == "LONG":
                candidate = max(float(group["entry_price"]), candle_close - distance)
                scenario["stop_price"] = max(float(scenario["stop_price"]), candidate)
            else:
                candidate = min(float(group["entry_price"]), candle_close + distance)
                scenario["stop_price"] = min(float(scenario["stop_price"]), candidate)


def close_scenario(
    group: dict[str, Any],
    scenario: dict[str, Any],
    raw_price: float,
    reason: str,
    closed_at: datetime,
    bundle: dict[str, Any],
    paper_config: dict[str, Any],
    ambiguous: bool = False,
) -> dict[str, Any]:
    exit_price, pnl = comparable_pnl_at_price(group, raw_price, bundle, paper_config)
    scenario["status"] = "EXITED"
    scenario["exit_raw_price"] = raw_price
    scenario["exit_price"] = exit_price
    scenario["exit_time"] = iso_utc(closed_at)
    scenario["exit_reason"] = reason
    scenario["comparable_pnl_eur"] = pnl
    if ambiguous:
        scenario["same_candle_ambiguity_count"] = int(scenario.get("same_candle_ambiguity_count", 0)) + 1
    return {
        "timestamp": iso_utc(closed_at),
        "event_type": "SHADOW_EXIT",
        "trade_key": group["trade_key"],
        "trade_id": group["trade_id"],
        "portfolio": group["portfolio"],
        "asset": group["asset"],
        "side": group["side"],
        "scenario_id": scenario["id"],
        "scenario_version": group["scenario_set_version"],
        "reason": reason,
        "price": exit_price,
        "net_pnl_ex_funding_eur": pnl,
        "quality": group["observation_quality"],
        "same_candle_ambiguous": ambiguous,
    }


def process_scenario_candle(
    group: dict[str, Any],
    scenario: dict[str, Any],
    candle_time: datetime,
    candle: pd.Series,
    bundle: dict[str, Any],
    paper_config: dict[str, Any],
) -> dict[str, Any] | None:
    if scenario.get("status") != "ACTIVE":
        return None

    candle_open = finite_float(candle.get("open"), float(group["entry_price"]))
    candle_high = finite_float(candle.get("high"), candle_open)
    candle_low = finite_float(candle.get("low"), candle_open)
    candle_close = finite_float(candle.get("close"), candle_open)
    side = str(group["side"])
    protective_stop = float(group["initial_stop_price"])
    dynamic_stop = float(
        scenario.get("stop_price", protective_stop)
    )
    liquidation = optional_float(group.get("liquidation_price"))
    scenario["observed_candles"] = int(scenario.get("observed_candles", 0)) + 1

    last_time = parse_time(scenario.get("last_candle_time"))
    if last_time is not None and (candle_time - last_time).total_seconds() > 31 * 60:
        scenario["candle_gap_count"] = int(scenario.get("candle_gap_count", 0)) + 1
    scenario["last_candle_time"] = iso_utc(candle_time)

    if liquidation is not None:
        gap = candle_open <= liquidation if side == "LONG" else candle_open >= liquidation
        if gap:
            return close_scenario(
                group, scenario, liquidation, "LIQUIDATION_GAP", candle_time,
                bundle, paper_config,
            )

    protective_stop_hit = (
        candle_low <= protective_stop
        if side == "LONG"
        else candle_high >= protective_stop
    )
    scenario_candidates: list[tuple[str, float]] = []
    kind = str(scenario["kind"])
    params = scenario.get("parameters", {})

    if kind == "FIXED_R":
        target = price_for_r(group, max(finite_float(params.get("target_r"), 1.0), 0.0))
        target_hit = candle_high >= target if side == "LONG" else candle_low <= target
        if target_hit:
            scenario_candidates.append(("FIXED_R_TARGET", target))

    elif kind in {"MFE_GIVEBACK", "BREAKEVEN", "ATR_TRAIL"}:
        if scenario.get("activated"):
            dynamic_hit = (
                candle_low <= dynamic_stop
                if side == "LONG"
                else candle_high >= dynamic_stop
            )
            if dynamic_hit:
                label = {
                    "MFE_GIVEBACK": "MFE_GIVEBACK",
                    "BREAKEVEN": "BREAKEVEN_STOP",
                    "ATR_TRAIL": "ATR_TRAIL_STOP",
                }[kind]
                scenario_candidates.append((label, dynamic_stop))

    opened = parse_time(group.get("opened_at")) or candle_time
    elapsed_hours = max(0.0, (candle_time - opened).total_seconds() / 3600.0)
    if kind == "TIME_EXIT" and elapsed_hours >= max(finite_float(params.get("hours"), 24.0), 0.0):
        scenario_candidates.append(("TIME_EXIT", candle_close))

    horizon = max(finite_float(group.get("evaluation_horizon_hours"), 24.0), 0.25)
    if elapsed_hours >= horizon:
        scenario_candidates.append(("EVALUATION_HORIZON", candle_close))

    candidates: list[tuple[str, float]] = list(scenario_candidates)
    if protective_stop_hit:
        # Avoid duplicating the same level when a dynamic rule has not yet
        # improved the initial stop.
        if not any(
            math.isclose(
                price,
                protective_stop,
                rel_tol=0.0,
                abs_tol=max(1e-12, abs(protective_stop) * 1e-10),
            )
            for _, price in candidates
        ):
            candidates.append(
                ("INITIAL_PROTECTIVE_STOP", protective_stop)
            )

    if candidates:
        ambiguous = len(candidates) > 1
        reason, raw_price = worse_exit(group, candidates) if ambiguous else candidates[0]
        return close_scenario(
            group, scenario, raw_price, reason, candle_time,
            bundle, paper_config, ambiguous=ambiguous,
        )

    # Dynamic changes derived from this candle become active only on the next
    # completed candle, preventing same-candle look-ahead.
    update_dynamic_levels_after_candle(
        group, scenario, candle_high, candle_low, candle_close
    )
    return None


def process_mark_timeout(
    group: dict[str, Any],
    scenario: dict[str, Any],
    when: datetime,
    mark: float,
    bundle: dict[str, Any],
    paper_config: dict[str, Any],
) -> dict[str, Any] | None:
    if scenario.get("status") != "ACTIVE":
        return None
    opened = parse_time(group.get("opened_at")) or when
    elapsed = max(0.0, (when - opened).total_seconds() / 3600.0)
    params = scenario.get("parameters", {})
    if scenario["kind"] == "TIME_EXIT" and elapsed >= max(finite_float(params.get("hours"), 24.0), 0.0):
        return close_scenario(group, scenario, mark, "TIME_EXIT_MARK_ONLY", when, bundle, paper_config)
    if elapsed >= max(finite_float(group.get("evaluation_horizon_hours"), 24.0), 0.25):
        return close_scenario(group, scenario, mark, "EVALUATION_HORIZON_MARK_ONLY", when, bundle, paper_config)
    return None


def actual_records(summary: dict[str, Any]) -> dict[str, dict[str, Any]]:
    records: dict[str, dict[str, Any]] = {}
    for row in read_csv(TRADE_LOG_PATH):
        key = trade_key(str(row.get("portfolio", "")), str(row.get("trade_id", "")))
        if key != ":":
            records[key] = row
    for row in summary.get("closed", []):
        key = trade_key(str(row.get("portfolio", "")), str(row.get("trade_id", "")))
        if key != ":":
            records[key] = row
    return records


def attach_actual(group: dict[str, Any], record: dict[str, Any]) -> None:
    actual = group.setdefault("actual", {})
    net = optional_float(record.get("net_pnl_eur"))
    funding = finite_float(record.get("funding_pnl_eur"), 0.0)
    actual.update({
        "closed": True,
        "closed_at": str(record.get("closed_at", "")),
        "exit_price": optional_float(record.get("exit_price")),
        "net_pnl_eur": net,
        "funding_pnl_eur": funding,
        "comparable_pnl_eur": None if net is None else net - funding,
        "holding_hours": optional_float(record.get("holding_hours")),
        "close_reason": str(record.get("close_reason", "")),
        "risk_model_version_at_exit": str(
            record.get("risk_model_version_at_exit", "")
        ),
    })


def timing_labels(
    actual_time: datetime | None,
    shadow_time: datetime | None,
    delta: float,
    tolerance: float,
) -> tuple[str, str]:
    if actual_time is None or shadow_time is None:
        return "UNKNOWN", "UNKNOWN"
    seconds = (shadow_time - actual_time).total_seconds()
    if abs(seconds) < 60:
        relation = "SAME_TIME"
    elif seconds < 0:
        relation = "BEFORE_ACTUAL"
    else:
        relation = "AFTER_ACTUAL"

    if abs(delta) <= tolerance:
        return relation, "EQUIVALENT"
    better = delta > 0
    if relation == "BEFORE_ACTUAL":
        return relation, "EARLIER_BETTER" if better else "TOO_EARLY"
    if relation == "AFTER_ACTUAL":
        return relation, "LATER_BETTER" if better else "TOO_LATE"
    return relation, "SAME_TIME_BETTER" if better else "SAME_TIME_WORSE"


def result_row(group: dict[str, Any], scenario: dict[str, Any], tolerance: float) -> dict[str, Any] | None:
    actual = group.get("actual", {})
    if not actual.get("closed") or scenario.get("status") != "EXITED":
        return None
    actual_pnl = optional_float(actual.get("comparable_pnl_eur"))
    shadow_pnl = optional_float(scenario.get("comparable_pnl_eur"))
    if actual_pnl is None or shadow_pnl is None:
        return None
    delta = shadow_pnl - actual_pnl
    actual_time = parse_time(actual.get("closed_at"))
    shadow_time = parse_time(scenario.get("exit_time"))
    relation, assessment = timing_labels(actual_time, shadow_time, delta, tolerance)
    quality = "FULL" if group.get("full_from_entry") else "PARTIAL"
    if int(scenario.get("candle_gap_count", 0)) > 0:
        quality += "_WITH_GAPS"
    if int(scenario.get("same_candle_ambiguity_count", 0)) > 0:
        quality += "_CONSERVATIVE_AMBIGUITY"
    opened = parse_time(group.get("opened_at"))
    shadow_holding = (
        (shadow_time - opened).total_seconds() / 3600.0
        if shadow_time is not None and opened is not None
        else None
    )
    return {
        "schema_version": RESULT_SCHEMA_VERSION,
        "engine_version": ENGINE_VERSION,
        "risk_model_version": group.get(
            "risk_model_version",
            "legacy_pre_block4_5",
        ),
        "scenario_set_version": group["scenario_set_version"],
        "scenario_id": scenario["id"],
        "scenario_kind": scenario["kind"],
        "scenario_parameters_json": json.dumps(scenario.get("parameters", {}), sort_keys=True, separators=(",", ":")),
        "trade_key": group["trade_key"],
        "trade_id": group["trade_id"],
        "portfolio": group["portfolio"],
        "strategy": group["strategy"],
        "asset": group["asset"],
        "symbol": group["symbol"],
        "side": group["side"],
        "timeframe_minutes": group["timeframe_minutes"],
        "opened_at": group["opened_at"],
        "actual_closed_at": actual.get("closed_at", ""),
        "shadow_closed_at": scenario.get("exit_time", ""),
        "actual_close_reason": actual.get("close_reason", ""),
        "shadow_close_reason": scenario.get("exit_reason", ""),
        "entry_price": group["entry_price"],
        "actual_exit_price": actual.get("exit_price", ""),
        "shadow_exit_price": scenario.get("exit_price", ""),
        "quantity": group["quantity"],
        "margin_eur": group["margin_eur"],
        "initial_risk_eur": group["initial_risk_eur"],
        "actual_net_pnl_eur": actual.get("net_pnl_eur", ""),
        "actual_funding_pnl_eur": actual.get("funding_pnl_eur", ""),
        "actual_comparable_pnl_eur": actual_pnl,
        "shadow_comparable_pnl_eur": shadow_pnl,
        "delta_vs_actual_eur": delta,
        "actual_holding_hours": actual.get("holding_hours", ""),
        "shadow_holding_hours": shadow_holding,
        "timing_relation": relation,
        "timing_assessment": assessment,
        "full_from_entry": bool(group.get("full_from_entry")),
        "observation_quality": group.get("observation_quality", ""),
        "observed_candles": scenario.get("observed_candles", 0),
        "candle_gap_count": scenario.get("candle_gap_count", 0),
        "same_candle_ambiguity_count": scenario.get("same_candle_ambiguity_count", 0),
        "result_quality": quality,
    }


def merge_result_rows(new_rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    existing = read_csv(RESULTS_PATH)
    merged: dict[tuple[str, str, str], dict[str, Any]] = {}
    for row in [*existing, *new_rows]:
        key = (
            str(row.get("trade_key", "")),
            str(row.get("scenario_set_version", "")),
            str(row.get("scenario_id", "")),
        )
        if all(key):
            merged[key] = row
    return sorted(
        merged.values(),
        key=lambda row: (
            str(row.get("actual_closed_at", "")),
            str(row.get("portfolio", "")),
            str(row.get("trade_id", "")),
            str(row.get("scenario_id", "")),
        ),
    )


def profit_factor(values: list[float]) -> float:
    gains = sum(value for value in values if value > 0)
    losses = abs(sum(value for value in values if value < 0))
    if losses > 0:
        return gains / losses
    return math.inf if gains > 0 else 0.0


def data_stage(full_sample: int) -> str:
    if full_sample <= 0:
        return "WAITING_FULL_SAMPLE"
    if full_sample < 10:
        return "COLLECTING"
    if full_sample < 30:
        return "PRELIMINARY_SAMPLE"
    return "READY_FOR_BLOCK4_EVALUATION"


def metric_row(scope: str, portfolio: str, scenario_id: str, rows: list[dict[str, Any]], generated: str) -> dict[str, Any]:
    actual = [finite_float(row.get("actual_comparable_pnl_eur")) for row in rows]
    shadow = [finite_float(row.get("shadow_comparable_pnl_eur")) for row in rows]
    delta = [finite_float(row.get("delta_vs_actual_eur")) for row in rows]
    full = sum(str(row.get("full_from_entry", "")).lower() in {"true", "1", "yes"} for row in rows)
    assessments = Counter(str(row.get("timing_assessment", "")) for row in rows)
    improved = sum(value > 0.01 for value in delta)
    worsened = sum(value < -0.01 for value in delta)
    equal = len(delta) - improved - worsened
    ambiguous = sum(finite_float(row.get("same_candle_ambiguity_count")) > 0 for row in rows)
    pf = profit_factor(shadow)
    kind = str(rows[0].get("scenario_kind", "")) if rows else ""
    return {
        "generated_utc": generated,
        "scope": scope,
        "portfolio": portfolio,
        "scenario_id": scenario_id,
        "scenario_kind": kind,
        "sample_total": len(rows),
        "sample_full_from_entry": full,
        "sample_partial": len(rows) - full,
        "average_actual_comparable_pnl_eur": statistics.fmean(actual) if actual else 0.0,
        "average_shadow_comparable_pnl_eur": statistics.fmean(shadow) if shadow else 0.0,
        "average_delta_vs_actual_eur": statistics.fmean(delta) if delta else 0.0,
        "median_delta_vs_actual_eur": statistics.median(delta) if delta else 0.0,
        "total_delta_vs_actual_eur": sum(delta),
        "improved_count": improved,
        "worsened_count": worsened,
        "equal_count": equal,
        "improved_pct": improved / len(rows) * 100.0 if rows else 0.0,
        "shadow_win_rate_pct": sum(value > 0 for value in shadow) / len(shadow) * 100.0 if shadow else 0.0,
        "actual_win_rate_pct": sum(value > 0 for value in actual) / len(actual) * 100.0 if actual else 0.0,
        "shadow_profit_factor": "inf" if math.isinf(pf) else pf,
        "shadow_expectancy_eur": statistics.fmean(shadow) if shadow else 0.0,
        "earlier_better_count": assessments["EARLIER_BETTER"],
        "too_early_count": assessments["TOO_EARLY"],
        "later_better_count": assessments["LATER_BETTER"],
        "too_late_count": assessments["TOO_LATE"],
        "same_time_better_count": assessments["SAME_TIME_BETTER"],
        "same_time_worse_count": assessments["SAME_TIME_WORSE"],
        "ambiguous_count": ambiguous,
        "data_stage": data_stage(full),
    }


def build_metrics(results: list[dict[str, Any]], when: datetime) -> list[dict[str, Any]]:
    generated = iso_utc(when)
    groups: dict[tuple[str, str, str], list[dict[str, Any]]] = defaultdict(list)
    for row in results:
        portfolio = str(row.get("portfolio", ""))
        scenario = str(row.get("scenario_id", ""))
        groups[("PORTFOLIO", portfolio, scenario)].append(row)
        groups[("ALL", "ALL", scenario)].append(row)
    metrics = [
        metric_row(scope, portfolio, scenario, rows, generated)
        for (scope, portfolio, scenario), rows in sorted(groups.items())
    ]
    write_csv(METRICS_PATH, METRIC_FIELDS, metrics)
    return metrics


def fmt_eur(value: Any, signed: bool = False) -> str:
    number = finite_float(value)
    prefix = "+" if signed and number > 0 else ""
    return f"{prefix}€{number:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def fmt_pct(value: Any) -> str:
    return f"{finite_float(value):.1f}%".replace(".", ",")


def render_report(
    state: dict[str, Any],
    results: list[dict[str, Any]],
    metrics: list[dict[str, Any]],
    when: datetime,
) -> str:
    active_groups = list(state.get("groups", {}).values())
    active_scenarios = sum(
        scenario.get("status") == "ACTIVE"
        for group in active_groups
        for scenario in group.get("scenarios", {}).values()
    )
    waiting_actual = sum(not group.get("actual", {}).get("closed") for group in active_groups)
    waiting_shadow = sum(
        group.get("actual", {}).get("closed")
        and any(scenario.get("status") == "ACTIVE" for scenario in group.get("scenarios", {}).values())
        for group in active_groups
    )
    all_metrics = [row for row in metrics if row.get("scope") == "ALL"]
    ranked = sorted(
        all_metrics,
        key=lambda row: (
            int(row.get("sample_full_from_entry", 0)),
            finite_float(row.get("average_delta_vs_actual_eur")),
        ),
        reverse=True,
    )
    lines = [
        "# Block 3 — Shadow Exit Engine",
        "",
        f"Generato: {iso_utc(when)}",
        "",
        "> Motore esclusivamente osservativo e Paper-only. Non modifica le uscite reali. "
        "I confronti escludono il funding sia dall'uscita originale sia dalle varianti.",
        "",
        "## Stato operativo",
        "",
        f"- Gruppi di trade ancora monitorati: **{len(active_groups)}**",
        f"- Scenari virtuali ancora attivi: **{active_scenarios}**",
        f"- Gruppi in attesa dell'uscita originale: **{waiting_actual}**",
        f"- Gruppi con originale chiuso ma Shadow ancora attive: **{waiting_shadow}**",
        f"- Confronti completati: **{len(results)}**",
        "",
        "## Classifica osservativa complessiva",
        "",
        "| Scenario | Campione completo | Campione totale | Δ medio vs originale | Migliora | Troppo presto | Troppo tardi | Stato dati |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    if not ranked:
        lines.append("| — | 0 | 0 | — | — | — | — | WAITING_FULL_SAMPLE |")
    else:
        for row in ranked[:20]:
            lines.append(
                "| {scenario} | {full} | {total} | {delta} | {improved} | {early} | {late} | {stage} |".format(
                    scenario=row["scenario_id"],
                    full=row["sample_full_from_entry"],
                    total=row["sample_total"],
                    delta=fmt_eur(row["average_delta_vs_actual_eur"], signed=True),
                    improved=fmt_pct(row["improved_pct"]),
                    early=row["too_early_count"],
                    late=row["too_late_count"],
                    stage=row["data_stage"],
                )
            )
    lines.extend([
        "",
        "## Come leggere il controllo",
        "",
        "- **EARLIER_BETTER**: la variante è uscita prima e ha conservato più profitto.",
        "- **TOO_EARLY**: la variante è uscita prima ma ha tagliato un movimento migliore.",
        "- **LATER_BETTER**: la variante ha continuato dopo l'uscita originale e ha guadagnato di più.",
        "- **TOO_LATE**: la variante è rimasta aperta più a lungo e ha peggiorato il risultato.",
        "",
        "## Limiti e protezioni",
        "",
        "Le regole Shadow mantengono entrata, quantità, commissioni, stop protettivo iniziale e liquidazione. "
        "Le ambiguità all'interno della stessa candela vengono risolte scegliendo l'esito peggiore. "
        "Le posizioni già aperte al momento dell'installazione sono marcate come campione parziale e non "
        "saranno utilizzate dal futuro Blocco 4 come prova piena.",
        "",
    ])
    text = "\n".join(lines)
    REPORT_PATH.write_text(text, encoding="utf-8")
    return text


def reconcile_open_groups(
    shadow_state: dict[str, Any],
    paper_state: dict[str, Any],
    summary: dict[str, Any],
    frames: dict[str, Any],
    block_config: dict[str, Any],
    events: list[dict[str, Any]],
) -> None:
    groups = shadow_state.setdefault("groups", {})
    newly_opened = {
        trade_key(str(row.get("portfolio", "")), str(row.get("trade_id", "")))
        for row in summary.get("opened", [])
    }
    for portfolio_name, portfolio in paper_state.get("portfolios", {}).items():
        for position in portfolio.get("open_positions", []):
            key = trade_key(portfolio_name, str(position.get("trade_id", "")))
            if key in groups or key == f"{portfolio_name}:":
                continue
            quality = "FULL_FROM_ENTRY" if key in newly_opened else "PARTIAL_FROM_BLOCK3_ACTIVATION"
            last = latest_candle_id(
                frames,
                str(position.get("asset", "")),
                int(block_config.get("timeframe_minutes", 15)),
            )
            group = create_group(position, portfolio_name, block_config, last, quality)
            groups[key] = group
            events.append({
                "timestamp": iso_utc(),
                "event_type": "GROUP_CREATED",
                "trade_key": key,
                "trade_id": group["trade_id"],
                "portfolio": group["portfolio"],
                "asset": group["asset"],
                "side": group["side"],
                "scenario_id": "",
                "scenario_version": group["scenario_set_version"],
                "reason": quality,
                "price": group["entry_price"],
                "net_pnl_ex_funding_eur": "",
                "quality": quality,
                "same_candle_ambiguous": False,
            })


def process_group(
    group: dict[str, Any],
    frames: dict[str, Any],
    prices: dict[str, float],
    block_config: dict[str, Any],
    bundle: dict[str, Any],
    paper_config: dict[str, Any],
    when: datetime,
    events: list[dict[str, Any]],
) -> None:
    timeframe = int(block_config.get("timeframe_minutes", 15))
    frame = frames.get(str(group["asset"]), {}).get(timeframe)
    processed_any = False
    last = parse_time(group.get("last_processed_candle"))
    opened = parse_time(group.get("opened_at"))
    if frame is not None and not frame.empty:
        for index, candle in frame.sort_index().iterrows():
            candle_time = pd.Timestamp(index)
            if candle_time.tzinfo is None:
                candle_time = candle_time.tz_localize("UTC")
            dt = candle_time.to_pydatetime().astimezone(timezone.utc)
            if last is not None and dt <= last:
                continue
            if opened is not None and dt <= opened:
                continue
            for scenario in group.get("scenarios", {}).values():
                event = process_scenario_candle(
                    group, scenario, dt, candle, bundle, paper_config
                )
                if event:
                    events.append(event)
            group["last_processed_candle"] = iso_utc(dt)
            processed_any = True
    if not processed_any:
        mark = prices.get(str(group["asset"]), float(group["entry_price"]))
        for scenario in group.get("scenarios", {}).values():
            event = process_mark_timeout(
                group, scenario, when, mark, bundle, paper_config
            )
            if event:
                events.append(event)


def run_shadow_exit_cycle(
    summary: dict[str, Any],
    paper_state: dict[str, Any],
    bundle: dict[str, Any],
    paper_config: dict[str, Any],
    when: datetime | None = None,
) -> dict[str, Any]:
    """Run one passive Block 3 simulation cycle.

    The function is deliberately isolated from the real execution engine.  It
    returns a compact summary for the Paper cycle payload and the rendered
    Markdown section for inclusion in the main report.
    """
    current = when or now_utc()
    block_config = load_config()
    if not block_config.get("enabled", True):
        return {
            "enabled": False,
            "status": "DISABLED",
            "report_markdown": "",
        }

    shadow_state = load_state()
    frames = bundle_frames(bundle)
    prices = current_prices(bundle)
    events: list[dict[str, Any]] = []

    reconcile_open_groups(
        shadow_state,
        paper_state,
        summary,
        frames,
        block_config,
        events,
    )

    actual_by_key = actual_records(summary)
    for key, group in shadow_state.get("groups", {}).items():
        record = actual_by_key.get(key)
        if record is not None:
            attach_actual(group, record)

    for group in list(shadow_state.get("groups", {}).values()):
        process_group(
            group,
            frames,
            prices,
            block_config,
            bundle,
            paper_config,
            current,
            events,
        )

    tolerance = max(finite_float(block_config.get("comparison_tolerance_eur"), 0.01), 0.0)
    new_results: list[dict[str, Any]] = []
    completed_keys: list[str] = []
    for key, group in shadow_state.get("groups", {}).items():
        all_written = bool(group.get("actual", {}).get("closed"))
        for scenario in group.get("scenarios", {}).values():
            if not scenario.get("result_written"):
                row = result_row(group, scenario, tolerance)
                if row is not None:
                    new_results.append(row)
                    scenario["result_written"] = True
            all_written = all_written and bool(scenario.get("result_written"))
        if all_written:
            completed_keys.append(key)

    results = merge_result_rows(new_results)
    write_csv(RESULTS_PATH, RESULT_FIELDS, results)
    for key in completed_keys:
        shadow_state.get("groups", {}).pop(key, None)

    append_events(events)
    metrics = build_metrics(results, current)
    report_markdown = render_report(shadow_state, results, metrics, current)
    save_state(shadow_state, current)

    active_groups = len(shadow_state.get("groups", {}))
    active_scenarios = sum(
        scenario.get("status") == "ACTIVE"
        for group in shadow_state.get("groups", {}).values()
        for scenario in group.get("scenarios", {}).values()
    )
    return {
        "enabled": True,
        "status": "OK",
        "engine_version": ENGINE_VERSION,
        "scenario_set_version": block_config.get("scenario_set_version"),
        "scenario_definitions": len(block_config.get("scenarios", [])),
        "active_groups": active_groups,
        "active_scenarios": active_scenarios,
        "new_results": len(new_results),
        "completed_results": len(results),
        "events_written": len(events),
        "report_path": str(REPORT_PATH),
        "report_markdown": report_markdown,
        "paper_positions_modified": False,
        "orders_sent": False,
    }
