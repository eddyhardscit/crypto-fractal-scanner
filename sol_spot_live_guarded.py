# -*- coding: utf-8 -*-
"""Guarded SOL-USDT spot runner for a dedicated KuCoin sub-account.

Strategy: SOL Adaptive Range Guarded v1.

The runner reuses the public-data adaptive range from the paper bot, but applies
much tighter live constraints for the first 100 USDT:
- maximum 50 USDT SOL exposure;
- maximum 10 USDT ordinary order;
- 20 USDT cash reserve;
- 20 USDT ordinary daily turnover;
- regime-specific target exposure;
- staged profit taking, trailing protection and stop rules;
- daily/total loss gates and a file kill switch.

No scheduler is installed by this file. ``status`` and ``test-order`` never
place a real order. ``execute`` reaches a real order only after all independent
safety gates pass and the kill-switch file is absent.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import os
import time
import uuid
from datetime import datetime, timedelta, timezone
from decimal import Decimal
from pathlib import Path
from typing import Any

import pandas as pd

from kucoin_spot_private import (
    KuCoinAPIError,
    KuCoinSpotClient,
    decimal_text,
    floor_to_increment,
)
from sol_spot_adaptive_bot import (
    add_indicators,
    fetch_spot_klines,
    make_session,
    range_snapshot,
    validate_config as validate_paper_strategy_config,
)
from sol_spot_live_telegram import (
    send_alert as telegram_send_alert,
    send_order_event as telegram_send_order_event,
    send_status_digest as telegram_send_status_digest,
    send_test as telegram_send_test,
)

CONFIG_PATH = Path(
    os.getenv("SOL_SPOT_LIVE_CONFIG", "sol_spot_live_config.json")
)
REAL_ACK = "I_UNDERSTAND_THIS_PLACES_REAL_ORDERS"
REAL_CONFIRM = "REAL_SOL_SPOT"
RISK_EXIT_REASONS = {
    "TOTAL_DRAWDOWN_EXIT",
    "HARD_STOP",
    "TREND_STOP",
}


class LiveSafetyError(RuntimeError):
    """Raised when a live safety invariant is not satisfied."""


def telegram_enabled(config: dict[str, Any]) -> bool:
    return config.get("telegram_notifications", {}).get("enabled") is True


def notify_order_safely(
    *,
    config: dict[str, Any],
    account: dict[str, Any],
    managed: dict[str, Any],
    strategy: dict[str, Any],
    risk: dict[str, Any],
    state: dict[str, Any],
    plan: dict[str, Any],
    reconciled: dict[str, Any] | None,
    order_id: str,
) -> None:
    if not telegram_enabled(config):
        return
    if config.get("telegram_notifications", {}).get("send_order_events") is not True:
        return
    try:
        telegram_send_order_event(
            config=config,
            account=account,
            managed=managed,
            strategy=strategy,
            risk=risk,
            state=state,
            plan=plan,
            reconciled=reconciled,
            order_id=order_id,
        )
        print("Notifica Telegram ordine: OK")
    except Exception as exc:
        # Never raise after a real fill: a notification failure must not invite a retry.
        print(f"ATTENZIONE: ordine eseguito ma notifica Telegram fallita: {type(exc).__name__}: {exc}")



def notify_error_safely(message: str) -> None:
    try:
        config = load_json(CONFIG_PATH) if CONFIG_PATH.exists() else {}
        settings = config.get("telegram_notifications", {})
        if settings.get("enabled") is not True or settings.get("send_error_alerts") is not True:
            return
        telegram_send_alert("ERRORE/BLOCCO", message[:3000])
        print("Notifica Telegram errore: OK")
    except Exception as notify_exc:
        print(f"ATTENZIONE: notifica Telegram errore fallita: {type(notify_exc).__name__}: {notify_exc}")



def now_utc() -> datetime:
    return datetime.now(timezone.utc)


def iso_utc(value: datetime | None = None) -> str:
    return (value or now_utc()).isoformat(timespec="seconds")


def parse_iso(value: Any) -> datetime | None:
    if value in (None, ""):
        return None
    timestamp = pd.Timestamp(value)
    if timestamp.tzinfo is None:
        timestamp = timestamp.tz_localize("UTC")
    return timestamp.to_pydatetime()


def decimal_value(value: Any, default: str = "0") -> Decimal:
    try:
        number = Decimal(str(value))
    except Exception:
        number = Decimal(default)
    if not number.is_finite():
        return Decimal(default)
    return number


def clamp_decimal(value: Decimal, minimum: Decimal, maximum: Decimal) -> Decimal:
    return min(maximum, max(minimum, value))


def load_json(path: Path) -> dict[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise LiveSafetyError(f"JSON non valido: {path}")
    return payload


def load_config(path: Path = CONFIG_PATH) -> dict[str, Any]:
    config = load_json(path)
    validate_live_config(config)
    return config


def _fraction(value: Any, name: str, *, allow_zero: bool = False) -> Decimal:
    number = decimal_value(value, "-1")
    minimum = Decimal("0") if allow_zero else Decimal("0.00000001")
    if not (minimum <= number <= Decimal("1")):
        raise LiveSafetyError(f"{name} deve essere compreso tra 0 e 1.")
    return number


def validate_live_config(config: dict[str, Any]) -> None:
    if int(config.get("schema_version", 0)) != 2:
        raise LiveSafetyError("È richiesta la configurazione live schema_version=2.")
    if str(config.get("symbol", "")).upper() != "SOL-USDT":
        raise LiveSafetyError("Il simbolo live deve restare SOL-USDT.")
    if str(config.get("base_asset", "")).upper() != "SOL":
        raise LiveSafetyError("L'asset base live deve restare SOL.")
    if str(config.get("quote_asset", "")).upper() != "USDT":
        raise LiveSafetyError("La valuta quote live deve restare USDT.")

    mode = str(config.get("mode", "")).upper()
    if mode not in {"READ_ONLY", "LIVE"}:
        raise LiveSafetyError("mode deve essere READ_ONLY oppure LIVE.")
    if config.get("live_orders_enabled") is True and mode != "LIVE":
        raise LiveSafetyError("live_orders_enabled=true richiede mode=LIVE.")

    managed = decimal_value(config.get("managed_capital_usdt"))
    reserve = decimal_value(config.get("minimum_cash_reserve_usdt"))
    maximum_order = decimal_value(config.get("maximum_order_usdt"))
    minimum_order = decimal_value(config.get("minimum_order_usdt"))
    emergency = decimal_value(config.get("maximum_emergency_sell_usdt"))
    maximum_sol = decimal_value(config.get("maximum_sol_value_usdt"))
    max_daily = decimal_value(config.get("maximum_daily_turnover_usdt"))
    band = decimal_value(config.get("rebalance_band_fraction"))
    interval = int(config.get("minimum_minutes_between_orders", 0))

    if managed <= Decimal("0"):
        raise LiveSafetyError(
            "managed_capital_usdt deve essere maggiore di zero."
        )
    if not (Decimal("0") <= reserve < managed):
        raise LiveSafetyError("Riserva USDT non valida.")
    if not (Decimal("0") < minimum_order <= maximum_order <= Decimal("10")):
        raise LiveSafetyError("L'ordine ordinario deve restare tra il minimo e 10 USDT.")
    if not (maximum_order <= emergency <= Decimal("50")):
        raise LiveSafetyError("Il limite di vendita d'emergenza deve essere tra 10 e 50 USDT.")
    if not (Decimal("0") < maximum_sol <= Decimal("50")):
        raise LiveSafetyError("L'esposizione SOL massima deve restare entro 50 USDT.")
    if not (Decimal("0") < max_daily <= Decimal("20")):
        raise LiveSafetyError("Il turnover ordinario giornaliero deve restare entro 20 USDT.")
    if not (Decimal("0") <= band <= Decimal("0.20")):
        raise LiveSafetyError("Rebalance band non valida.")
    if interval < 120:
        raise LiveSafetyError("Servono almeno 120 minuti tra ordini ordinari.")

    expected_regimes = {
        "STRONG_UPTREND",
        "UPTREND",
        "RANGE",
        "DOWNTREND",
        "STRONG_DOWNTREND",
    }
    bands = config.get("regime_target_bands", {})
    if set(bands) != expected_regimes:
        raise LiveSafetyError("regime_target_bands incompleto o non valido.")
    for regime, values in bands.items():
        if not isinstance(values, list) or len(values) != 2:
            raise LiveSafetyError(f"Banda non valida per {regime}.")
        low = _fraction(values[0], f"{regime}.min", allow_zero=True)
        high = _fraction(values[1], f"{regime}.max", allow_zero=True)
        if low > high or high > Decimal("0.50"):
            raise LiveSafetyError(f"Banda esposizione non valida per {regime}.")
    if [decimal_value(v) for v in bands["STRONG_DOWNTREND"]] != [Decimal("0"), Decimal("0")]:
        raise LiveSafetyError("STRONG_DOWNTREND deve imporre esposizione SOL zero.")

    pp = config.get("profit_protection", {})
    lp = config.get("loss_protection", {})
    for key in (
        "take_profit_1_pct",
        "take_profit_1_sell_fraction",
        "take_profit_2_pct",
        "take_profit_2_sell_fraction",
        "trailing_activation_pct",
        "trailing_drawdown_pct",
        "trailing_sell_fraction",
    ):
        _fraction(pp.get(key), f"profit_protection.{key}")
    if decimal_value(pp["take_profit_1_pct"]) >= decimal_value(pp["take_profit_2_pct"]):
        raise LiveSafetyError("Il secondo take profit deve essere sopra il primo.")
    for key in (
        "trend_stop_pct",
        "trend_stop_sell_fraction",
        "hard_stop_pct",
    ):
        _fraction(lp.get(key), f"loss_protection.{key}")
    if decimal_value(lp["trend_stop_pct"]) >= decimal_value(lp["hard_stop_pct"]):
        raise LiveSafetyError("L'hard stop deve essere più distante del trend stop.")
    if decimal_value(lp.get("stop_cooldown_hours")) < Decimal("1"):
        raise LiveSafetyError("Cooldown stop non valido.")
    if not (Decimal("0") < decimal_value(lp.get("maximum_daily_loss_usdt")) <= Decimal("3")):
        raise LiveSafetyError("La perdita giornaliera massima deve restare entro 3 USDT.")
    if not (Decimal("0") < decimal_value(lp.get("maximum_total_drawdown_usdt")) <= Decimal("10")):
        raise LiveSafetyError("Il drawdown totale massimo deve restare entro 10 USDT.")

    allowed = {
        str(item).upper()
        for item in config.get("allowed_trade_account_currencies", [])
    }
    if allowed != {"USDT", "SOL"}:
        raise LiveSafetyError("Le sole valute ammesse nel conto trade sono USDT e SOL.")


def strategy_snapshot(config: dict[str, Any]) -> dict[str, Any]:
    strategy_path = Path(config["strategy_config_path"])
    strategy_config = load_json(strategy_path)
    validate_paper_strategy_config(strategy_config)
    if str(strategy_config.get("symbol", "")).upper() != "SOL-USDT":
        raise LiveSafetyError("La strategia paper non usa SOL-USDT.")

    session = make_session()
    frame = fetch_spot_klines(
        session,
        "SOL-USDT",
        int(strategy_config["timeframe_minutes"]),
        int(strategy_config["lookback_candles"]),
    )
    frame = add_indicators(frame, strategy_config)

    signal_cfg = config.get("entry_signals", {})
    rsi_period = int(signal_cfg.get("rsi_period", 14))

    if rsi_period < 2:
        raise LiveSafetyError("rsi_period deve essere almeno 2.")

    delta = frame["close"].diff()
    gains = delta.clip(lower=0.0)
    losses = -delta.clip(upper=0.0)

    avg_gain = gains.ewm(
        alpha=1.0 / rsi_period,
        adjust=False,
        min_periods=rsi_period,
    ).mean()

    avg_loss = losses.ewm(
        alpha=1.0 / rsi_period,
        adjust=False,
        min_periods=rsi_period,
    ).mean()

    rs = avg_gain / avg_loss.replace(0.0, float("nan"))
    frame["rsi"] = 100.0 - (100.0 / (1.0 + rs))

    frame.loc[
        (avg_loss == 0.0) & (avg_gain > 0.0),
        "rsi",
    ] = 100.0

    frame.loc[
        (avg_loss == 0.0) & (avg_gain == 0.0),
        "rsi",
    ] = 50.0
    usable = frame.dropna(
        subset=[
            "atr",
            "ema_fast",
            "ema_center",
            "ema_slow",
            "rolling_median",
            "rolling_std",
            "rsi",
        ]
    )
    if len(usable) < 2:
        raise LiveSafetyError("Storico SOL insufficiente per il range adattivo.")

    candle_time = pd.Timestamp(usable.index[-1])
    snapshot = range_snapshot(usable.iloc[-1], candle_time, 1.0, strategy_config)

    previous_candle_time = pd.Timestamp(usable.index[-2])

    previous_snapshot = range_snapshot(
        usable.iloc[-2],
        previous_candle_time,
        1.0,
        strategy_config,
    )
    regime = str(snapshot.regime).upper()
    if regime not in config["regime_target_bands"]:
        raise LiveSafetyError(f"Regime non riconosciuto: {regime}")
    low, high = [
        Decimal(str(value))
        for value in config["regime_target_bands"][regime]
    ]
    raw_target = Decimal(str(snapshot.target_sol_weight))
    guarded_target = clamp_decimal(raw_target, low, high)
    range_module = analyze_range_module(
        usable=usable,
        strategy_config=strategy_config,
        config=config,
        snapshot=snapshot,
        previous_snapshot=previous_snapshot,
        regime=regime,
    )

    return {
        "range_module": range_module,
        "candle_time_utc": snapshot.time_utc,
        "market_price_usdt": snapshot.price_eur,
        "range_lower_usdt": snapshot.lower_eur,
        "range_center_usdt": snapshot.center_eur,
        "range_upper_usdt": snapshot.upper_eur,
        "regime": regime,
        "trend_atr": snapshot.trend_atr,
        "raw_target_sol_weight": raw_target,
        "target_band_min": low,
        "target_band_max": high,
        "target_sol_weight": guarded_target,
        "rsi": Decimal(str(usable.iloc[-1]["rsi"])),
        "previous_rsi": Decimal(str(usable.iloc[-2]["rsi"])),
        "previous_market_price_usdt": Decimal(
            str(usable.iloc[-2]["close"])
        ),
        "previous_range_lower_usdt": Decimal(
            str(previous_snapshot.lower_eur)
        ),
        "previous_range_center_usdt": Decimal(
            str(previous_snapshot.center_eur)
        ),
    }



# RANGE_MODULE_OBSERVE_START
def analyze_range_module(
    *,
    usable: pd.DataFrame,
    strategy_config: dict[str, Any],
    config: dict[str, Any],
    snapshot: Any,
    previous_snapshot: Any,
    regime: str,
) -> dict[str, Any]:
    """Analizza un range stabile senza modificare il piano operativo."""

    range_cfg = config.get("range_module", {})
    enabled = bool(range_cfg.get("enabled", False))
    mode = str(range_cfg.get("mode", "observe")).upper()

    current_price = Decimal(str(snapshot.price_eur))
    current_lower = Decimal(str(snapshot.lower_eur))
    current_center = Decimal(str(snapshot.center_eur))
    current_upper = Decimal(str(snapshot.upper_eur))
    current_width = max(
        Decimal("0"),
        current_upper - current_lower,
    )

    result: dict[str, Any] = {
        "enabled": enabled,
        "mode": mode,
        "status": "DISABLED",
        "confirmed": False,
        "lookback_bars": 0,
        "consecutive_range_bars": 0,
        "duration_hours": Decimal("0"),
        "lower_touches": 0,
        "upper_touches": 0,
        "center_drift_half_widths": Decimal("0"),
        "width_pct": Decimal("0"),
        "zone": "NONE",
        "proposal": "NONE",
        "breakout_up": False,
        "breakout_down": False,
        "lower_usdt": current_lower,
        "center_usdt": current_center,
        "upper_usdt": current_upper,
    }

    if not enabled:
        return result

    requested_lookback = max(
        8,
        int(range_cfg.get("lookback_bars", 24)),
    )
    minimum_confirmed_bars = max(
        4,
        int(range_cfg.get("minimum_confirmed_bars", 12)),
    )
    minimum_touch_count = max(
        1,
        int(range_cfg.get("minimum_touch_count", 2)),
    )

    touch_tolerance_fraction = decimal_value(
        range_cfg.get("touch_tolerance_fraction", "0.15")
    )
    maximum_center_drift = decimal_value(
        range_cfg.get(
            "maximum_center_drift_half_widths",
            "0.75",
        )
    )
    minimum_width_pct = decimal_value(
        range_cfg.get("minimum_width_pct", "1.20")
    )
    lower_zone_fraction = decimal_value(
        range_cfg.get("lower_zone_fraction", "0.20")
    )
    upper_zone_fraction = decimal_value(
        range_cfg.get("upper_zone_fraction", "0.20")
    )
    buy_rsi_max = decimal_value(
        range_cfg.get("buy_rsi_max", "45")
    )

    recent = usable.tail(requested_lookback)
    range_rows: list[dict[str, Any]] = []

    for row_index, row in recent.iterrows():
        row_time = pd.Timestamp(row_index)
        row_snapshot = range_snapshot(
            row,
            row_time,
            1.0,
            strategy_config,
        )

        row_lower = Decimal(str(row_snapshot.lower_eur))
        row_center = Decimal(str(row_snapshot.center_eur))
        row_upper = Decimal(str(row_snapshot.upper_eur))

        range_rows.append(
            {
                "regime": str(row_snapshot.regime).upper(),
                "price": Decimal(str(row_snapshot.price_eur)),
                "low": Decimal(str(row["low"])),
                "high": Decimal(str(row["high"])),
                "lower": row_lower,
                "center": row_center,
                "upper": row_upper,
                "width": max(
                    Decimal("0"),
                    row_upper - row_lower,
                ),
            }
        )

    result["lookback_bars"] = len(range_rows)

    if len(range_rows) < 2:
        result["status"] = "INSUFFICIENT_HISTORY"
        return result

    consecutive_range_bars = 0
    for item in reversed(range_rows):
        if item["regime"] != "RANGE":
            break
        consecutive_range_bars += 1

    active_rows = (
        range_rows[-consecutive_range_bars:]
        if consecutive_range_bars
        else []
    )

    lower_touches = 0
    upper_touches = 0
    stability_ratio = Decimal("999")

    width_pct = (
        current_width / current_center * Decimal("100")
        if current_center > 0
        else Decimal("0")
    )

    if active_rows:
        centers = [item["center"] for item in active_rows]
        half_widths = [
            item["width"] / Decimal("2")
            for item in active_rows
            if item["width"] > 0
        ]

        if half_widths:
            ordered = sorted(half_widths)
            median_half_width = ordered[len(ordered) // 2]
            center_drift = max(centers) - min(centers)

            stability_ratio = (
                center_drift / median_half_width
                if median_half_width > 0
                else Decimal("999")
            )

        lower_flags: list[bool] = []
        upper_flags: list[bool] = []

        for item in active_rows:
            tolerance = (
                item["width"] * touch_tolerance_fraction
            )
            lower_flags.append(
                item["low"] <= item["lower"] + tolerance
            )
            upper_flags.append(
                item["high"] >= item["upper"] - tolerance
            )

        previous_flag = False
        for flag in lower_flags:
            if flag and not previous_flag:
                lower_touches += 1
            previous_flag = flag

        previous_flag = False
        for flag in upper_flags:
            if flag and not previous_flag:
                upper_touches += 1
            previous_flag = flag

    previous_price = Decimal(
        str(previous_snapshot.price_eur)
    )
    previous_lower = Decimal(
        str(previous_snapshot.lower_eur)
    )
    previous_upper = Decimal(
        str(previous_snapshot.upper_eur)
    )

    prior_range_bars = sum(
        1
        for item in range_rows[:-2]
        if item["regime"] == "RANGE"
    )

    breakout_down = (
        prior_range_bars >= minimum_confirmed_bars
        and previous_price < previous_lower
        and current_price < current_lower
    )
    breakout_up = (
        prior_range_bars >= minimum_confirmed_bars
        and previous_price > previous_upper
        and current_price > current_upper
    )

    stable = stability_ratio <= maximum_center_drift
    duration_ok = (
        consecutive_range_bars >= minimum_confirmed_bars
    )
    touches_ok = (
        lower_touches >= minimum_touch_count
        and upper_touches >= minimum_touch_count
    )
    width_ok = width_pct >= minimum_width_pct

    confirmed = (
        regime == "RANGE"
        and duration_ok
        and stable
        and touches_ok
        and width_ok
    )

    timeframe_minutes = max(
        1,
        int(strategy_config.get("timeframe_minutes", 60)),
    )
    duration_hours = (
        Decimal(consecutive_range_bars)
        * Decimal(timeframe_minutes)
        / Decimal("60")
    )

    if current_width <= 0:
        zone = "NONE"
    elif current_price <= (
        current_lower
        + current_width * lower_zone_fraction
    ):
        zone = "LOWER"
    elif current_price >= (
        current_upper
        - current_width * upper_zone_fraction
    ):
        zone = "UPPER"
    elif current_price < current_center:
        zone = "LOWER_HALF"
    else:
        zone = "UPPER_HALF"

    current_rsi = Decimal(str(usable.iloc[-1]["rsi"]))
    previous_rsi = Decimal(str(usable.iloc[-2]["rsi"]))

    if breakout_down:
        status = "BREAKOUT_DOWN"
        proposal = "MITIGATE_LOSS_REVIEW"
    elif breakout_up:
        status = "BREAKOUT_UP"
        proposal = "TRAILING_BREAKOUT_REVIEW"
    elif confirmed:
        status = "CONFIRMED"

        if (
            zone == "LOWER"
            and current_rsi <= buy_rsi_max
            and current_rsi >= previous_rsi
        ):
            proposal = "BUY_ZONE_CANDIDATE"
        elif zone == "UPPER":
            proposal = "UPPER_SELL_ZONE_CANDIDATE"
        elif zone == "UPPER_HALF":
            proposal = "CENTER_OR_UPPER_REVIEW"
        else:
            proposal = "HOLD_INSIDE_RANGE"
    elif regime == "RANGE":
        status = "CANDIDATE"
        proposal = "WAIT_RANGE_CONFIRMATION"
    else:
        status = "NO_ACTIVE_RANGE"
        proposal = "NONE"

    result.update(
        {
            "status": status,
            "confirmed": confirmed,
            "consecutive_range_bars": consecutive_range_bars,
            "duration_hours": duration_hours,
            "lower_touches": lower_touches,
            "upper_touches": upper_touches,
            "center_drift_half_widths": stability_ratio,
            "width_pct": width_pct,
            "zone": zone,
            "proposal": proposal,
            "breakout_up": breakout_up,
            "breakout_down": breakout_down,
        }
    )

    return result
# RANGE_MODULE_OBSERVE_END

# RANGE_OBSERVER_NOTIFICATIONS_START
def _range_observer_state(
    state: dict[str, Any],
) -> dict[str, Any]:
    observer = state.setdefault("range_observer", {})

    defaults = {
        "confirmed_ranges_started": 0,
        "completed_ranges": 0,
        "useful_signals": 0,
        "anomalies": 0,
        "in_confirmed_range": False,
        "last_status": "",
        "last_signal_signature": "",
        "last_anomaly_signature": "",
        "readiness_notified": False,
        "readiness_logged": False,
        "current_cycle_started_utc": None,
        "last_event_utc": None,
    }

    for key, value in defaults.items():
        observer.setdefault(key, value)

    return observer


def _append_range_history(
    *,
    config: dict[str, Any],
    strategy: dict[str, Any],
    observer: dict[str, Any],
    event: str,
) -> None:
    range_cfg = config.get("range_module", {})
    history_path = Path(
        range_cfg.get(
            "history_path",
            "reports/sol_range_observation_events.jsonl",
        )
    )
    history_path.parent.mkdir(parents=True, exist_ok=True)

    module = strategy.get("range_module", {})

    record = {
        "recorded_utc": iso_utc(),
        "candle_time_utc": str(
            strategy.get("candle_time_utc", "")
        ),
        "event": event,
        "status": module.get("status"),
        "proposal": module.get("proposal"),
        "zone": module.get("zone"),
        "regime": strategy.get("regime"),
        "market_price_usdt": decimal_text(
            strategy.get("market_price_usdt", 0)
        ),
        "range_lower_usdt": decimal_text(
            module.get("lower_usdt", 0)
        ),
        "range_center_usdt": decimal_text(
            module.get("center_usdt", 0)
        ),
        "range_upper_usdt": decimal_text(
            module.get("upper_usdt", 0)
        ),
        "duration_hours": decimal_text(
            module.get("duration_hours", 0)
        ),
        "lower_touches": int(
            module.get("lower_touches", 0)
        ),
        "upper_touches": int(
            module.get("upper_touches", 0)
        ),
        "width_pct": decimal_text(
            module.get("width_pct", 0)
        ),
        "center_drift_half_widths": decimal_text(
            module.get("center_drift_half_widths", 0)
        ),
        "confirmed_ranges_started": int(
            observer.get("confirmed_ranges_started", 0)
        ),
        "completed_ranges": int(
            observer.get("completed_ranges", 0)
        ),
        "useful_signals": int(
            observer.get("useful_signals", 0)
        ),
        "anomalies": int(
            observer.get("anomalies", 0)
        ),
    }

    with history_path.open("a", encoding="utf-8") as handle:
        handle.write(
            json.dumps(record, ensure_ascii=False) + "\n"
        )


def _send_range_alert_safely(
    *,
    config: dict[str, Any],
    title: str,
    detail: str,
) -> bool:
    if not telegram_enabled(config):
        return False

    try:
        telegram_send_alert(title, detail)
        return True
    except Exception as exc:
        print(
            "AVVISO: notifica Telegram range non inviata:",
            f"{type(exc).__name__}: {exc}",
        )
        return False


def _range_event_detail(
    *,
    strategy: dict[str, Any],
    observer: dict[str, Any],
) -> str:
    module = strategy.get("range_module", {})

    return "\n".join(
        [
            f"Regime: {strategy.get('regime', 'N/D')}",
            f"Stato range: {module.get('status', 'N/D')}",
            f"Zona: {module.get('zone', 'N/D')}",
            f"Proposta: {module.get('proposal', 'N/D')}",
            (
                "Prezzo SOL: "
                f"{decimal_text(strategy.get('market_price_usdt', 0))} "
                "USDT"
            ),
            (
                "Range inferiore/centro/superiore: "
                f"{decimal_text(module.get('lower_usdt', 0))} / "
                f"{decimal_text(module.get('center_usdt', 0))} / "
                f"{decimal_text(module.get('upper_usdt', 0))} USDT"
            ),
            (
                "Durata: "
                f"{decimal_text(module.get('duration_hours', 0))} ore"
            ),
            (
                "Tocchi inferiore/superiore: "
                f"{module.get('lower_touches', 0)}/"
                f"{module.get('upper_touches', 0)}"
            ),
            (
                "Progressi: "
                f"{observer.get('completed_ranges', 0)} "
                "range completati, "
                f"{observer.get('useful_signals', 0)} "
                "segnali utili"
            ),
            "",
            "Modalità OBSERVE: nessun ordine range viene eseguito.",
        ]
    )


def process_range_observation(
    *,
    config: dict[str, Any],
    strategy: dict[str, Any],
    state: dict[str, Any],
) -> None:
    module = strategy.get("range_module", {})

    if not module.get("enabled"):
        return

    observer = _range_observer_state(state)
    range_cfg = config.get("range_module", {})
    notifications_enabled = bool(
        range_cfg.get("notify_significant_events", True)
    )

    status = str(module.get("status", "UNKNOWN"))
    proposal = str(module.get("proposal", "NONE"))
    zone = str(module.get("zone", "NONE"))
    previous_status = str(
        observer.get("last_status", "")
    )

    lower = decimal_value(module.get("lower_usdt", 0))
    center = decimal_value(module.get("center_usdt", 0))
    upper = decimal_value(module.get("upper_usdt", 0))

    events: list[tuple[str, str]] = []

    anomaly = not (
        lower > 0
        and lower < center
        and center < upper
        and int(module.get("lower_touches", 0)) >= 0
        and int(module.get("upper_touches", 0)) >= 0
    )

    if anomaly:
        anomaly_signature = (
            f"{strategy.get('candle_time_utc')}|"
            f"{lower}|{center}|{upper}"
        )

        if (
            anomaly_signature
            != observer.get("last_anomaly_signature", "")
        ):
            observer["anomalies"] = (
                int(observer.get("anomalies", 0)) + 1
            )
            observer["last_anomaly_signature"] = (
                anomaly_signature
            )
            events.append(
                (
                    "RANGE_ANOMALY",
                    "⚠️ MODULO RANGE — ANOMALIA",
                )
            )

    if (
        status == "CONFIRMED"
        and not bool(observer.get("in_confirmed_range"))
    ):
        observer["in_confirmed_range"] = True
        observer["confirmed_ranges_started"] = (
            int(
                observer.get(
                    "confirmed_ranges_started",
                    0,
                )
            )
            + 1
        )
        observer["current_cycle_started_utc"] = iso_utc()

        events.append(
            (
                "RANGE_CONFIRMED",
                "📊 MODULO RANGE — RANGE CONFERMATO",
            )
        )

    if status in {"BREAKOUT_DOWN", "BREAKOUT_UP"}:
        if bool(observer.get("in_confirmed_range")):
            observer["completed_ranges"] = (
                int(observer.get("completed_ranges", 0)) + 1
            )
            observer["in_confirmed_range"] = False
            observer["current_cycle_started_utc"] = None

        if status != previous_status:
            observer["useful_signals"] = (
                int(observer.get("useful_signals", 0)) + 1
            )

            title = (
                "🔻 MODULO RANGE — ROTTURA RIBASSISTA"
                if status == "BREAKOUT_DOWN"
                else "🔺 MODULO RANGE — ROTTURA RIALZISTA"
            )
            events.append((status, title))

    elif (
        status == "NO_ACTIVE_RANGE"
        and bool(observer.get("in_confirmed_range"))
    ):
        observer["completed_ranges"] = (
            int(observer.get("completed_ranges", 0)) + 1
        )
        observer["in_confirmed_range"] = False
        observer["current_cycle_started_utc"] = None

        events.append(
            (
                "RANGE_COMPLETED",
                "🏁 MODULO RANGE — RANGE TERMINATO",
            )
        )

    actionable_proposals = {
        "BUY_ZONE_CANDIDATE":
            "🟢 MODULO RANGE — ZONA ACQUISTO",
        "UPPER_SELL_ZONE_CANDIDATE":
            "🔵 MODULO RANGE — ZONA VENDITA",
    }

    if proposal in actionable_proposals:
        signal_signature = f"{proposal}|{zone}"

        if (
            signal_signature
            != observer.get("last_signal_signature", "")
        ):
            observer["useful_signals"] = (
                int(observer.get("useful_signals", 0)) + 1
            )
            observer["last_signal_signature"] = (
                signal_signature
            )

            events.append(
                (
                    proposal,
                    actionable_proposals[proposal],
                )
            )
    else:
        observer["last_signal_signature"] = ""

    observer["last_status"] = status

    for event, title in events:
        observer["last_event_utc"] = iso_utc()

        _append_range_history(
            config=config,
            strategy=strategy,
            observer=observer,
            event=event,
        )

        if notifications_enabled:
            _send_range_alert_safely(
                config=config,
                title=title,
                detail=_range_event_detail(
                    strategy=strategy,
                    observer=observer,
                ),
            )

    minimum_completed_ranges = int(
        range_cfg.get(
            "readiness_min_completed_ranges",
            3,
        )
    )
    minimum_signals = int(
        range_cfg.get("readiness_min_signals", 15)
    )
    maximum_anomalies = int(
        range_cfg.get("readiness_max_anomalies", 0)
    )

    ready = (
        int(observer.get("completed_ranges", 0))
        >= minimum_completed_ranges
        and int(observer.get("useful_signals", 0))
        >= minimum_signals
        and int(observer.get("anomalies", 0))
        <= maximum_anomalies
    )

    if ready and not bool(
        observer.get("readiness_logged")
    ):
        _append_range_history(
            config=config,
            strategy=strategy,
            observer=observer,
            event="READINESS_REACHED",
        )
        observer["readiness_logged"] = True

    if (
        ready
        and not bool(observer.get("readiness_notified"))
        and notifications_enabled
    ):
        readiness_detail = "\n".join(
            [
                (
                    "Range completi osservati: "
                    f"{observer.get('completed_ranges', 0)}"
                ),
                (
                    "Segnali utili registrati: "
                    f"{observer.get('useful_signals', 0)}"
                ),
                (
                    "Anomalie rilevate: "
                    f"{observer.get('anomalies', 0)}"
                ),
                "",
                (
                    "Il modulo ha raggiunto la soglia minima "
                    "per la revisione."
                ),
                (
                    "Nessuna operazione range è stata "
                    "attivata automaticamente."
                ),
                (
                    "Serve la tua autorizzazione esplicita "
                    "per passare da OBSERVE ad ACTIVE."
                ),
            ]
        )

        sent = _send_range_alert_safely(
            config=config,
            title="✅ MODULO RANGE — DATI SUFFICIENTI",
            detail=readiness_detail,
        )

        if sent:
            observer["readiness_notified"] = True

    strategy["range_observer_progress"] = {
        "confirmed_ranges_started": int(
            observer.get("confirmed_ranges_started", 0)
        ),
        "completed_ranges": int(
            observer.get("completed_ranges", 0)
        ),
        "useful_signals": int(
            observer.get("useful_signals", 0)
        ),
        "anomalies": int(
            observer.get("anomalies", 0)
        ),
        "ready": ready,
        "minimum_completed_ranges":
            minimum_completed_ranges,
        "minimum_signals": minimum_signals,
    }
# RANGE_OBSERVER_NOTIFICATIONS_END




def empty_balance() -> dict[str, Decimal]:
    return {"balance": Decimal("0"), "available": Decimal("0"), "holds": Decimal("0")}


def account_snapshot(client: KuCoinSpotClient, config: dict[str, Any]) -> dict[str, Any]:
    balances = client.balances()
    allowed = {
        str(item).upper()
        for item in config["allowed_trade_account_currencies"]
    }
    foreign_threshold = decimal_value(config.get("foreign_asset_abort_balance", "0.00000001"))
    foreign = {
        currency: data["balance"]
        for currency, data in balances.items()
        if currency not in allowed and data["balance"] > foreign_threshold
    }
    if foreign:
        details = ", ".join(
            f"{currency}={decimal_text(value)}"
            for currency, value in sorted(foreign.items())
        )
        raise LiveSafetyError("Valute estranee nel sub-account dedicato: " + details)

    usdt = balances.get("USDT", empty_balance())
    sol = balances.get("SOL", empty_balance())
    ticker = client.get_ticker("SOL-USDT")
    price = decimal_value(ticker.get("price"))
    if price <= 0:
        raise LiveSafetyError("Prezzo SOL-USDT non valido.")
    sol_value = sol["balance"] * price
    total_equity = usdt["balance"] + sol_value
    return {
        "price": price,
        "usdt": usdt,
        "sol": sol,
        "sol_value": sol_value,
        "total_equity": total_equity,
        "raw_balances": balances,
    }


def symbol_rules(client: KuCoinSpotClient, symbol: str) -> dict[str, Decimal]:
    metadata = client.get_symbol(symbol)
    if metadata.get("enableTrading") is False:
        raise LiveSafetyError(f"Trading disabilitato su {symbol}.")
    rules = {
        "base_increment": decimal_value(metadata.get("baseIncrement")),
        "quote_increment": decimal_value(metadata.get("quoteIncrement")),
        "base_min_size": decimal_value(metadata.get("baseMinSize")),
        "min_funds": decimal_value(metadata.get("minFunds")),
    }
    if any(value <= 0 for value in rules.values()):
        raise LiveSafetyError(f"Regole di mercato incomplete per {symbol}: {rules}")
    return rules


def state_path(config: dict[str, Any]) -> Path:
    return Path(config["state_path"])


def new_state(config: dict[str, Any], account: dict[str, Any]) -> dict[str, Any]:
    managed_cap = decimal_value(config["managed_capital_usdt"])
    protected_excess = max(Decimal("0"), account["total_equity"] - managed_cap)
    managed_equity = max(Decimal("0"), account["total_equity"] - protected_excess)
    if account["sol"]["balance"] > decimal_value(config.get("balance_sync_tolerance_sol", "0.00001")):
        raise LiveSafetyError(
            "SOL già presente ma costo medio non tracciato. Riportare SOL a zero o inizializzare manualmente lo stato."
        )
    today = now_utc().date().isoformat()
    return {
        "schema_version": 2,
        "created_utc": iso_utc(),
        "updated_utc": iso_utc(),
        "day_utc": today,
        "protected_excess_usdt": decimal_text(protected_excess),
        "initial_managed_equity_usdt": decimal_text(managed_equity),
        "day_start_managed_equity_usdt": decimal_text(managed_equity),
        "peak_managed_equity_usdt": decimal_text(managed_equity),
        "daily_turnover_usdt": "0",
        "last_executed_candle_utc": None,
        "last_order_time_utc": None,
        "last_client_oid": None,
        "last_order": None,
        "tracked_sol_units": "0",
        "average_cost_usdt": "0",
        "position_peak_price_usdt": "0",
        "tp1_done": False,
        "tp2_done": False,
        "trailing_done": False,
        "cooldown_until_utc": None,
        "realized_pnl_usdt": "0",
    }


def load_state(config: dict[str, Any], account: dict[str, Any]) -> dict[str, Any]:
    path = state_path(config)
    if not path.exists():
        return new_state(config, account)
    state = load_json(path)
    if int(state.get("schema_version", 0)) != 2:
        raise LiveSafetyError(
            "Stato live precedente non compatibile. Con saldo SOL a zero, rinominare reports/sol_spot_live_state.json e riprovare."
        )
    return state


def save_state(state: dict[str, Any], config: dict[str, Any]) -> None:
    state["updated_utc"] = iso_utc()
    path = state_path(config)
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_suffix(path.suffix + ".tmp")
    temp.write_text(json.dumps(state, indent=2, ensure_ascii=False), encoding="utf-8")
    temp.replace(path)


def reconcile_external_usdt(
    state: dict[str, Any],
    account: dict[str, Any],
    config: dict[str, Any],
) -> None:
    """Protegge depositi esterni e permette di reinvestire i profitti del bot."""
    actual = account["usdt"]["balance"]
    tolerance = decimal_value(
        config.get("external_transfer_tolerance_usdt", "0.01")
    )

    if "tracked_usdt_balance" not in state:
        state["tracked_usdt_balance"] = decimal_text(actual)
        return

    tracked = decimal_value(state["tracked_usdt_balance"])
    difference = actual - tracked

    if abs(difference) <= tolerance:
        state["tracked_usdt_balance"] = decimal_text(actual)
        return

    protected = max(
        Decimal("0"),
        decimal_value(state.get("protected_excess_usdt", "0")),
    )

    if difference > 0:
        # Nuovo trasferimento esterno: non diventa capitale del bot.
        protected += difference
    else:
        # Un prelievo è consentito soltanto dalla quota protetta.
        withdrawn = -difference
        if withdrawn > protected + tolerance:
            raise LiveSafetyError(
                "Saldo USDT ridotto oltre l'eccedenza protetta. "
                "Possibile prelievo dal capitale gestito."
            )
        protected = max(Decimal("0"), protected - withdrawn)

    state["protected_excess_usdt"] = decimal_text(protected)
    state["tracked_usdt_balance"] = decimal_text(actual)


def managed_snapshot(
    account: dict[str, Any],
    state: dict[str, Any],
) -> dict[str, Decimal]:
    protected = max(Decimal("0"), decimal_value(state.get("protected_excess_usdt")))
    managed_cash_balance = max(Decimal("0"), account["usdt"]["balance"] - protected)
    managed_cash_available = max(Decimal("0"), account["usdt"]["available"] - protected)
    managed_equity = managed_cash_balance + account["sol_value"]
    current_weight = account["sol_value"] / managed_equity if managed_equity > 0 else Decimal("0")
    return {
        "protected_excess": protected,
        "managed_cash_balance": managed_cash_balance,
        "managed_cash_available": managed_cash_available,
        "managed_equity": managed_equity,
        "current_sol_weight": current_weight,
    }


def refresh_state_periods(
    state: dict[str, Any],
    managed: dict[str, Decimal],
    account: dict[str, Any],
    config: dict[str, Any],
) -> dict[str, Decimal | bool | str | None]:
    current = now_utc()
    today = current.date().isoformat()
    equity = managed["managed_equity"]
    if state.get("day_utc") != today:
        state["day_utc"] = today
        state["day_start_managed_equity_usdt"] = decimal_text(equity)
        state["daily_turnover_usdt"] = "0"

    peak_equity = max(decimal_value(state.get("peak_managed_equity_usdt")), equity)
    state["peak_managed_equity_usdt"] = decimal_text(peak_equity)

    tracked = decimal_value(state.get("tracked_sol_units"))
    tolerance = decimal_value(config.get("balance_sync_tolerance_sol", "0.00001"))
    actual = account["sol"]["balance"]
    if abs(actual - tracked) > tolerance:
        raise LiveSafetyError(
            "Saldo SOL diverso dallo stato tracciato. Possibile modifica manuale o stato non sincronizzato."
        )

    if actual > tolerance:
        peak_price = max(decimal_value(state.get("position_peak_price_usdt")), account["price"])
        state["position_peak_price_usdt"] = decimal_text(peak_price)
    else:
        state["position_peak_price_usdt"] = "0"

    initial = decimal_value(state.get("initial_managed_equity_usdt"), "100")
    day_start = decimal_value(state.get("day_start_managed_equity_usdt"), decimal_text(equity))
    daily_loss = max(Decimal("0"), day_start - equity)
    total_loss = max(Decimal("0"), initial - equity)
    cooldown_until = parse_iso(state.get("cooldown_until_utc"))
    cooldown_active = cooldown_until is not None and current < cooldown_until
    return {
        "daily_loss_usdt": daily_loss,
        "total_loss_usdt": total_loss,
        "cooldown_active": cooldown_active,
        "cooldown_until_utc": iso_utc(cooldown_until) if cooldown_active else None,
    }


def serializable(value: Any) -> Any:
    if isinstance(value, Decimal):
        return decimal_text(value)
    if isinstance(value, datetime):
        return iso_utc(value)
    if isinstance(value, dict):
        return {key: serializable(item) for key, item in value.items()}
    if isinstance(value, list):
        return [serializable(item) for item in value]
    return value


def _sell_plan(
    *,
    reason: str,
    fraction: Decimal,
    account: dict[str, Any],
    rules: dict[str, Decimal],
    config: dict[str, Any],
    base_plan: dict[str, Any],
    emergency: bool,
    state_flag: str | None = None,
    start_cooldown: bool = False,
    kill_after_execution: bool = False,
) -> dict[str, Any]:
    available = account["sol"]["available"]
    size = floor_to_increment(available * fraction, rules["base_increment"])
    value = size * account["price"]
    maximum = decimal_value(
        config["maximum_emergency_sell_usdt"] if emergency else config["maximum_order_usdt"]
    )
    if value > maximum and account["price"] > 0:
        size = floor_to_increment(maximum / account["price"], rules["base_increment"])
        value = size * account["price"]
    minimum = max(decimal_value(config["minimum_order_usdt"]), rules["min_funds"])
    if size < rules["base_min_size"] or value < minimum:
        base_plan["reason"] = reason + "_BELOW_MINIMUM"
        return base_plan
    base_plan.update(
        {
            "action": "SELL",
            "reason": reason,
            "order_value_usdt": value,
            "size": size,
            "risk_exit": emergency,
            "state_flag_to_set": state_flag,
            "start_cooldown": start_cooldown,
            "kill_after_execution": kill_after_execution,
        }
    )
    return base_plan


def make_plan(
    account: dict[str, Any],
    managed: dict[str, Decimal],
    strategy: dict[str, Any],
    rules: dict[str, Decimal],
    state: dict[str, Any],
    risk: dict[str, Any],
    config: dict[str, Any],
) -> dict[str, Any]:
    price = account["price"]
    managed_equity = managed["managed_equity"]
    target_weight = decimal_value(strategy["target_sol_weight"])
    target_value = min(
        managed_equity * target_weight,
        decimal_value(config["maximum_sol_value_usdt"]),
    )
    difference = target_value - account["sol_value"]
    threshold = max(
        decimal_value(config["minimum_order_usdt"]),
        managed_equity * decimal_value(config["rebalance_band_fraction"]),
        rules["min_funds"],
    )
    plan: dict[str, Any] = {
        "action": "HOLD",
        "reason": "REBALANCE_BAND",
        "symbol": config["symbol"],
        "candle_time_utc": strategy["candle_time_utc"],
        "price_usdt": price,
        "managed_equity_usdt": managed_equity,
        "target_sol_weight": target_weight,
        "current_sol_weight": managed["current_sol_weight"],
        "target_sol_value_usdt": target_value,
        "difference_usdt": difference,
        "order_value_usdt": Decimal("0"),
        "funds": None,
        "size": None,
        "risk_exit": False,
        "state_flag_to_set": None,
        "start_cooldown": False,
        "kill_after_execution": False,
    }
    sol_available = account["sol"]["available"]
    average_cost = decimal_value(state.get("average_cost_usdt"))
    has_position = sol_available > rules["base_min_size"] and average_cost > 0
    pnl_pct = (price / average_cost - Decimal("1")) if has_position else Decimal("0")
    plan["position_pnl_pct"] = pnl_pct
    plan["average_cost_usdt"] = average_cost

    lp = config["loss_protection"]
    pp = config["profit_protection"]
    total_limit = decimal_value(lp["maximum_total_drawdown_usdt"])

    if risk["total_loss_usdt"] >= total_limit:
        if sol_available > rules["base_min_size"]:
            return _sell_plan(
                reason="TOTAL_DRAWDOWN_EXIT",
                fraction=Decimal("1"),
                account=account,
                rules=rules,
                config=config,
                base_plan=plan,
                emergency=True,
                start_cooldown=True,
                kill_after_execution=True,
            )
        if config["loss_protection"].get("auto_kill_switch_on_total_drawdown") is True:
            Path(config["kill_switch_path"]).touch(exist_ok=True)
        plan["reason"] = "TOTAL_DRAWDOWN_KILL_SWITCH"
        return plan

    if has_position and pnl_pct <= -decimal_value(lp["hard_stop_pct"]):
        return _sell_plan(
            reason="HARD_STOP",
            fraction=Decimal("1"),
            account=account,
            rules=rules,
            config=config,
            base_plan=plan,
            emergency=True,
            start_cooldown=True,
        )

    if (
        has_position
        and pnl_pct <= -decimal_value(lp["trend_stop_pct"])
        and strategy["regime"] in {"DOWNTREND", "STRONG_DOWNTREND"}
    ):
        return _sell_plan(
            reason="TREND_STOP",
            fraction=decimal_value(lp["trend_stop_sell_fraction"]),
            account=account,
            rules=rules,
            config=config,
            base_plan=plan,
            emergency=True,
            start_cooldown=True,
        )

    if has_position and not bool(state.get("tp2_done")) and pnl_pct >= decimal_value(pp["take_profit_2_pct"]):
        return _sell_plan(
            reason="TAKE_PROFIT_2",
            fraction=decimal_value(pp["take_profit_2_sell_fraction"]),
            account=account,
            rules=rules,
            config=config,
            base_plan=plan,
            emergency=False,
            state_flag="tp2_done",
        )

    if has_position and not bool(state.get("tp1_done")) and pnl_pct >= decimal_value(pp["take_profit_1_pct"]):
        return _sell_plan(
            reason="TAKE_PROFIT_1",
            fraction=decimal_value(pp["take_profit_1_sell_fraction"]),
            account=account,
            rules=rules,
            config=config,
            base_plan=plan,
            emergency=False,
            state_flag="tp1_done",
        )

    peak_price = decimal_value(state.get("position_peak_price_usdt"))
    trailing_active = has_position and peak_price >= average_cost * (Decimal("1") + decimal_value(pp["trailing_activation_pct"]))
    trailing_hit = trailing_active and price <= peak_price * (Decimal("1") - decimal_value(pp["trailing_drawdown_pct"]))
    if trailing_hit and not bool(state.get("trailing_done")):
        return _sell_plan(
            reason="TRAILING_PROFIT_PROTECTION",
            fraction=decimal_value(pp["trailing_sell_fraction"]),
            account=account,
            rules=rules,
            config=config,
            base_plan=plan,
            emergency=False,
            state_flag="trailing_done",
        )

    if managed_equity <= 0:
        plan["reason"] = "NO_MANAGED_CAPITAL"
        return plan

    regime = str(strategy["regime"]).upper()

    # Nel ribasso più forte non vengono aperti nuovi ingressi.
    # L'eventuale posizione esistente non viene venduta per inseguire
    # il target zero: resta affidata alle protezioni già configurate.
    if regime == "STRONG_DOWNTREND":
        plan["reason"] = "BUY_BLOCKED_STRONG_DOWNTREND"
        plan["entry_target_sol_weight"] = Decimal("0")
        plan["effective_position_target_sol_weight"] = (
            managed["current_sol_weight"]
            if has_position
            else Decimal("0")
        )
        plan["existing_position_policy"] = (
            "MANAGED_BY_STOPS"
            if has_position
            else "NO_POSITION"
        )
        plan["target_sol_weight_semantics"] = "NEW_ENTRIES_ONLY"
        return plan

    # Il tetto SOL cresce o diminuisce insieme al capitale gestito.
    # Eventuali trasferimenti esterni protetti ne restano esclusi.
    maximum_sol_fraction = decimal_value(
        config.get("maximum_sol_fraction", "0.40")
    )
    max_sol_value = managed_equity * maximum_sol_fraction

    capacity = max(
        Decimal("0"),
        max_sol_value - account["sol_value"],
    )

    if capacity < threshold:
        plan["reason"] = "MAX_SOL_EXPOSURE_REACHED"
        return plan

    signal_cfg = config.get("entry_signals", {})

    rsi = decimal_value(strategy["rsi"])
    previous_rsi = decimal_value(strategy["previous_rsi"])

    previous_price = decimal_value(
        strategy["previous_market_price_usdt"]
    )

    lower = decimal_value(strategy["range_lower_usdt"])
    previous_lower = decimal_value(
        strategy["previous_range_lower_usdt"]
    )

    center = decimal_value(strategy["range_center_usdt"])
    previous_center = decimal_value(
        strategy["previous_range_center_usdt"]
    )

    mean_reversion_rsi = decimal_value(
        signal_cfg.get("mean_reversion_rsi_max", 38)
    )

    downtrend_rsi = decimal_value(
        signal_cfg.get("downtrend_recovery_rsi_max", 32)
    )

    bull_rsi_min = decimal_value(
        signal_cfg.get("bull_pullback_rsi_min", 45)
    )

    bull_rsi_max = decimal_value(
        signal_cfg.get("bull_pullback_rsi_max", 65)
    )

    # Recupero dopo essere scesi sotto la fascia inferiore.
    lower_band_recovery = (
        previous_price <= previous_lower
        and price > lower
        and previous_rsi <= mean_reversion_rsi
        and rsi > previous_rsi
    )

    # Nel downtrend serve una condizione ancora più severa.
    downtrend_recovery = (
        regime == "DOWNTREND"
        and lower_band_recovery
        and previous_rsi <= downtrend_rsi
    )

    # In rialzo compra il recupero della zona centrale
    # dopo un pullback, non il prezzo già lanciato verso l'alto.
    bull_pullback_recovery = (
        regime in {"UPTREND", "STRONG_UPTREND"}
        and previous_price <= previous_center
        and price > center
        and bull_rsi_min <= rsi <= bull_rsi_max
        and rsi > previous_rsi
    )

    if regime == "DOWNTREND":
        entry_allowed = downtrend_recovery
    elif regime == "RANGE":
        entry_allowed = lower_band_recovery
    elif regime in {"UPTREND", "STRONG_UPTREND"}:
        entry_allowed = (
            lower_band_recovery
            or bull_pullback_recovery
        )
    else:
        entry_allowed = False

    plan["rsi"] = rsi
    plan["previous_rsi"] = previous_rsi
    plan["lower_band_recovery"] = lower_band_recovery
    plan["downtrend_recovery"] = downtrend_recovery
    plan["bull_pullback_recovery"] = bull_pullback_recovery

    if not entry_allowed:
        plan["reason"] = "BUY_WAITING_TECHNICAL_RECOVERY"
        return plan

    if risk["cooldown_active"]:
        plan["reason"] = "BUY_BLOCKED_STOP_COOLDOWN"
        return plan

    if risk["daily_loss_usdt"] >= decimal_value(
        lp["maximum_daily_loss_usdt"]
    ):
        plan["reason"] = "BUY_BLOCKED_DAILY_LOSS"
        return plan

    reserve = decimal_value(
        config["minimum_cash_reserve_usdt"]
    )

    spendable = max(
        Decimal("0"),
        managed["managed_cash_available"] - reserve,
    )

    configured_order_max = decimal_value(
        config["maximum_order_usdt"]
    )

    # Nel downtrend la tranche viene dimezzata.
    regime_order_max = (
        min(configured_order_max, Decimal("5"))
        if regime == "DOWNTREND"
        else configured_order_max
    )

    raw_funds = min(
        regime_order_max,
        spendable,
        capacity,
    )

    funds = floor_to_increment(
        raw_funds,
        rules["quote_increment"],
    )

    if funds < threshold or funds < rules["min_funds"]:
        plan["reason"] = "BUY_BELOW_MINIMUM_OR_RESERVE"
        return plan

    if regime == "DOWNTREND":
        reason = "DOWNTREND_CONFIRMED_RECOVERY_BUY"
    elif bull_pullback_recovery:
        reason = "BULL_PULLBACK_RECOVERY_BUY"
    else:
        reason = "RSI_LOWER_BAND_RECOVERY_BUY"

    plan.update(
        {
            "action": "BUY",
            "reason": reason,
            "order_value_usdt": funds,
            "funds": funds,
        }
    )

    return plan


def hold_gate(config: dict[str, Any], account: dict[str, Any]) -> None:
    if config.get("require_zero_holds_before_order") is not True:
        return
    if account["usdt"]["holds"] > 0 or account["sol"]["holds"] > 0:
        raise LiveSafetyError("Ordine bloccato: esistono fondi SOL/USDT già in hold.")


def minimum_interval_gate(config: dict[str, Any], state: dict[str, Any], plan: dict[str, Any]) -> None:
    if plan.get("risk_exit") is True:
        return
    last = parse_iso(state.get("last_order_time_utc"))
    if last is None:
        return
    interval = timedelta(minutes=int(config["minimum_minutes_between_orders"]))
    if now_utc() - last < interval:
        raise LiveSafetyError("Ordine bloccato: intervallo minimo di 2 ore non trascorso.")


def live_gates(
    *,
    config: dict[str, Any],
    account: dict[str, Any],
    plan: dict[str, Any],
    state: dict[str, Any],
    cli_confirmation: str | None,
) -> None:
    if str(config["mode"]).upper() != "LIVE":
        raise LiveSafetyError("Config non armata: mode non è LIVE.")
    if config.get("live_orders_enabled") is not True:
        raise LiveSafetyError("Config non armata: live_orders_enabled non è true.")
    if config.get("real_order_confirmation") != REAL_CONFIRM:
        raise LiveSafetyError("Config non armata: real_order_confirmation errata.")
    if os.getenv("SOL_LIVE_TRADING_ACK", "") != REAL_ACK:
        raise LiveSafetyError("Variabile SOL_LIVE_TRADING_ACK mancante o errata.")
    if cli_confirmation != REAL_CONFIRM:
        raise LiveSafetyError(f"Conferma CLI richiesta: --confirm {REAL_CONFIRM}")
    if Path(config["kill_switch_path"]).exists():
        raise LiveSafetyError(f"Kill switch attivo: {config['kill_switch_path']}")
    if plan["action"] not in {"BUY", "SELL"}:
        raise LiveSafetyError("Nessun ordine previsto dal piano corrente.")
    if state.get("last_executed_candle_utc") == plan["candle_time_utc"]:
        raise LiveSafetyError("Ordine già eseguito per questa candela chiusa.")

    hold_gate(config, account)
    minimum_interval_gate(config, state, plan)
    current_turnover = decimal_value(state.get("daily_turnover_usdt", "0"))
    maximum_turnover = decimal_value(config["maximum_daily_turnover_usdt"])
    if plan.get("risk_exit") is not True and current_turnover + plan["order_value_usdt"] > maximum_turnover:
        raise LiveSafetyError("Ordine bloccato dal limite di turnover giornaliero.")


def update_position_state_after_fill(
    *,
    state: dict[str, Any],
    before: dict[str, Any],
    after: dict[str, Any],
    plan: dict[str, Any],
    config: dict[str, Any],
) -> None:
    before_sol = before["sol"]["balance"]
    after_sol = after["sol"]["balance"]
    before_usdt = before["usdt"]["balance"]
    after_usdt = after["usdt"]["balance"]
    old_average = decimal_value(state.get("average_cost_usdt"))
    old_units = before_sol
    realized = Decimal("0")

    if plan["action"] == "BUY":
        acquired = max(Decimal("0"), after_sol - before_sol)
        spent = max(Decimal("0"), before_usdt - after_usdt)
        if acquired <= 0 or spent <= 0:
            raise LiveSafetyError("Ordine BUY non riconciliato nei saldi.")
        new_units = after_sol
        prior_cost = old_units * old_average
        state["average_cost_usdt"] = decimal_text((prior_cost + spent) / new_units)
        state["position_peak_price_usdt"] = decimal_text(after["price"])
        state["tp1_done"] = False
        state["tp2_done"] = False
        state["trailing_done"] = False
    else:
        sold = max(Decimal("0"), before_sol - after_sol)
        proceeds = max(Decimal("0"), after_usdt - before_usdt)
        if sold <= 0 or proceeds <= 0:
            raise LiveSafetyError("Ordine SELL non riconciliato nei saldi.")
        realized = proceeds - sold * old_average
        state["realized_pnl_usdt"] = decimal_text(
            decimal_value(state.get("realized_pnl_usdt")) + realized
        )
        if after_sol <= decimal_value(config.get("balance_sync_tolerance_sol", "0.00001")):
            state["average_cost_usdt"] = "0"
            state["position_peak_price_usdt"] = "0"
            state["tp1_done"] = False
            state["tp2_done"] = False
            state["trailing_done"] = False
        flag = plan.get("state_flag_to_set")
        if flag:
            state[flag] = True

    state["tracked_sol_units"] = decimal_text(after_sol)
    state["tracked_usdt_balance"] = decimal_text(after_usdt)
    if plan.get("start_cooldown") is True:
        hours = float(config["loss_protection"]["stop_cooldown_hours"])
        state["cooldown_until_utc"] = iso_utc(now_utc() + timedelta(hours=hours))
    state["last_realized_pnl_usdt"] = decimal_text(realized)


def write_status(
    *,
    config: dict[str, Any],
    account: dict[str, Any],
    managed: dict[str, Decimal],
    strategy: dict[str, Any],
    risk: dict[str, Any],
    state: dict[str, Any],
    plan: dict[str, Any],
    test_result: Any | None = None,
    real_result: Any | None = None,
    reconciled_order: Any | None = None,
) -> dict[str, Any]:
    status = {
        "generated_utc": iso_utc(),
        "mode": str(config["mode"]).upper(),
        "live_orders_enabled": bool(config["live_orders_enabled"]),
        "kill_switch_active": Path(config["kill_switch_path"]).exists(),
        "symbol": config["symbol"],
        "account": {
            "usdt_balance": account["usdt"]["balance"],
            "usdt_available": account["usdt"]["available"],
            "sol_balance": account["sol"]["balance"],
            "sol_available": account["sol"]["available"],
            "sol_price_usdt": account["price"],
            "sol_value_usdt": account["sol_value"],
            "total_equity_usdt": account["total_equity"],
            "managed_equity_usdt": managed["managed_equity"],
            "managed_cash_available_usdt": managed["managed_cash_available"],
            "protected_excess_usdt": managed["protected_excess"],
        },
        "position": {
            "average_cost_usdt": decimal_value(state.get("average_cost_usdt")),
            "peak_price_usdt": decimal_value(state.get("position_peak_price_usdt")),
            "tracked_sol_units": decimal_value(state.get("tracked_sol_units")),
            "realized_pnl_usdt": decimal_value(state.get("realized_pnl_usdt")),
            "tp1_done": bool(state.get("tp1_done")),
            "tp2_done": bool(state.get("tp2_done")),
            "trailing_done": bool(state.get("trailing_done")),
        },
        "risk": risk,
        "strategy": strategy,
        "plan": plan,
        "test_result": test_result,
        "real_result": real_result,
        "reconciled_order": reconciled_order,
    }
    path = Path(config["status_path"])
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_suffix(path.suffix + ".tmp")
    temp.write_text(json.dumps(serializable(status), indent=2, ensure_ascii=False), encoding="utf-8")
    temp.replace(path)
    return status


def append_order_log(config: dict[str, Any], row: dict[str, Any]) -> None:
    path = Path(config["orders_log_path"])
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "time_utc",
        "client_oid",
        "order_id",
        "symbol",
        "side",
        "reason",
        "risk_exit",
        "planned_value_usdt",
        "planned_funds",
        "planned_size",
        "candle_time_utc",
        "target_sol_weight",
        "current_sol_weight",
        "daily_turnover_after_usdt",
        "average_cost_after_usdt",
        "tracked_sol_after",
        "realized_pnl_this_order_usdt",
        "reconciled_deal_funds",
        "reconciled_deal_size",
        "reconciled_fee",
        "reconciled_fee_currency",
    ]
    exists = path.exists() and path.stat().st_size > 0
    with path.open("a", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        if not exists:
            writer.writeheader()
        writer.writerow({field: serializable(row.get(field, "")) for field in fields})


def print_summary(
    config: dict[str, Any],
    account: dict[str, Any],
    managed: dict[str, Decimal],
    strategy: dict[str, Any],
    risk: dict[str, Any],
    state: dict[str, Any],
    plan: dict[str, Any],
) -> None:
    print("=== SOL ADAPTIVE RANGE GUARDED v1 ===")
    print(f"Modalità: {str(config['mode']).upper()}")
    print("Ordini reali abilitati in config:", "SI" if config["live_orders_enabled"] else "NO")
    print("Kill switch:", "ATTIVO" if Path(config["kill_switch_path"]).exists() else "DISATTIVO")
    print(
        "Saldo trade:",
        f"{decimal_text(account['usdt']['available'])} USDT,",
        f"{decimal_text(account['sol']['available'])} SOL",
    )
    print("Equity gestita:", f"{decimal_text(managed['managed_equity'])} USDT")
    print("Eccedenza protetta:", f"{decimal_text(managed['protected_excess'])} USDT")
    print("Liquidità gestita disponibile:", f"{decimal_text(managed['managed_cash_available'])} USDT")
    if plan.get("reason") == "BUY_BLOCKED_STRONG_DOWNTREND":
        print(
            "Peso SOL attuale:",
            f"{float(managed['current_sol_weight']) * 100:.2f}%",
        )
        print(
            "Nuovi ingressi SOL:",
            f"{float(plan.get('entry_target_sol_weight', 0)) * 100:.2f}%",
        )
        if plan.get("existing_position_policy") == "MANAGED_BY_STOPS":
            print(
                "Posizione esistente:",
                "mantenuta e gestita da trend stop, hard stop, "
                "take profit e trailing.",
            )
        else:
            print("Posizione esistente: nessuna.")
    else:
        print(
            "Peso SOL:",
            f"{float(managed['current_sol_weight']) * 100:.2f}% ->",
            f"{float(plan['target_sol_weight']) * 100:.2f}%",
        )
    print(
        "Regime:", strategy["regime"],
        f"| banda {float(strategy['target_band_min']) * 100:.0f}-{float(strategy['target_band_max']) * 100:.0f}%",
        "| candela:", strategy["candle_time_utc"],
    )
    range_module = strategy.get("range_module", {})
    if range_module.get("enabled"):
        print(
            "Modulo range:",
            range_module.get("mode", "OBSERVE"),
            "| stato:",
            range_module.get("status", "UNKNOWN"),
            "| durata:",
            f"{decimal_text(range_module.get('duration_hours', 0))} h",
        )
        print(
            "Range diagnostica:",
            f"tocchi {range_module.get('lower_touches', 0)}/"
            f"{range_module.get('upper_touches', 0)}",
            "| stabilità:",
            f"{decimal_text(range_module.get('center_drift_half_widths', 0))} HW",
            "| ampiezza:",
            f"{decimal_text(range_module.get('width_pct', 0))}%",
        )
        print(
            "Range osservazione:",
            "zona",
            range_module.get("zone", "NONE"),
            "| proposta:",
            range_module.get("proposal", "NONE"),
        )

    progress = strategy.get(
        "range_observer_progress",
        {},
    )
    if progress:
        print(
            "Range raccolta:",
            f"completi "
            f"{progress.get('completed_ranges', 0)}/"
            f"{progress.get('minimum_completed_ranges', 3)}",
            "| segnali",
            f"{progress.get('useful_signals', 0)}/"
            f"{progress.get('minimum_signals', 15)}",
            "| anomalie",
            progress.get("anomalies", 0),
            "| pronto:",
            "SI" if progress.get("ready") else "NO",
        )

    average = decimal_value(state.get("average_cost_usdt"))
    pnl_pct = decimal_value(plan.get("position_pnl_pct")) * Decimal("100")
    print("Costo medio tracciato:", f"{decimal_text(average)} USDT", "| P/L posizione:", f"{float(pnl_pct):+.2f}%")
    print(
        "Rischio:",
        f"perdita giorno {decimal_text(risk['daily_loss_usdt'])} USDT,",
        f"perdita totale {decimal_text(risk['total_loss_usdt'])} USDT,",
        "cooldown" if risk["cooldown_active"] else "nessun cooldown",
    )
    print(
        "Piano:", plan["action"],
        "| motivo:", plan["reason"],
        "| valore:", f"{decimal_text(plan['order_value_usdt'])} USDT",
    )


def build_runtime() -> tuple[
    dict[str, Any],
    KuCoinSpotClient,
    dict[str, Any],
    dict[str, Decimal],
    dict[str, Any],
    dict[str, Decimal],
    dict[str, Any],
    dict[str, Any],
]:
    config = load_config()
    client = KuCoinSpotClient()
    account = account_snapshot(client, config)
    rules = symbol_rules(client, config["symbol"])
    state = load_state(config, account)
    reconcile_external_usdt(state, account, config)
    managed = managed_snapshot(account, state)
    risk = refresh_state_periods(state, managed, account, config)
    strategy = strategy_snapshot(config)
    process_range_observation(
        config=config,
        strategy=strategy,
        state=state,
    )

    plan = make_plan(account, managed, strategy, rules, state, risk, config)
    save_state(state, config)
    return config, client, account, managed, strategy, rules, state, {"risk": risk, "plan": plan}


def run_status() -> int:
    config, _, account, managed, strategy, _, state, runtime = build_runtime()
    risk, plan = runtime["risk"], runtime["plan"]
    print_summary(config, account, managed, strategy, risk, state, plan)
    write_status(
        config=config,
        account=account,
        managed=managed,
        strategy=strategy,
        risk=risk,
        state=state,
        plan=plan,
    )
    return 0


def run_test_order() -> int:
    config, client, account, managed, strategy, _, state, runtime = build_runtime()
    risk, plan = runtime["risk"], runtime["plan"]
    print_summary(config, account, managed, strategy, risk, state, plan)
    if plan["action"] == "HOLD":
        print("TEST ORDER non eseguito: il piano corrente è HOLD.")
        write_status(
            config=config,
            account=account,
            managed=managed,
            strategy=strategy,
            risk=risk,
            state=state,
            plan=plan,
        )
        return 0

    hold_gate(config, account)
    result = client.test_market_order(
        symbol=config["symbol"],
        side=plan["action"].lower(),
        funds=plan["funds"],
        size=plan["size"],
        client_oid=str(uuid.uuid4()),
    )
    print("KuCoin Add Order Test: OK")
    print("Nessun ordine è entrato nel matching system.")
    write_status(
        config=config,
        account=account,
        managed=managed,
        strategy=strategy,
        risk=risk,
        state=state,
        plan=plan,
        test_result=result,
    )
    return 0


def run_telegram_test() -> int:
    telegram_send_test()
    print("Messaggio Telegram di prova inviato. Nessun ordine eseguito.")
    return 0


def run_telegram_status(force: bool = False) -> int:
    config, _, account, managed, strategy, _, state, runtime = build_runtime()
    risk, plan = runtime["risk"], runtime["plan"]
    if not telegram_enabled(config):
        raise LiveSafetyError("Notifiche Telegram disabilitate nella configurazione.")
    sent = telegram_send_status_digest(
        config=config,
        account=account,
        managed=managed,
        strategy=strategy,
        risk=risk,
        state=state,
        plan=plan,
        force=force,
    )
    print("Riepilogo Telegram inviato." if sent else "Riepilogo non dovuto: intervallo non trascorso.")
    return 0



def run_execute(cli_confirmation: str | None) -> int:
    config, client, account, managed, strategy, _, state, runtime = build_runtime()
    risk, plan = runtime["risk"], runtime["plan"]
    print_summary(config, account, managed, strategy, risk, state, plan)
    save_state(state, config)

    if plan.get("action") not in {"BUY", "SELL"}:
        print(
            "HOLD normale: "
            f"{plan.get('reason', 'NESSUN_ORDINE_PREVISTO')}."
        )
        return 0

    live_gates(
        config=config,
        account=account,
        plan=plan,
        state=state,
        cli_confirmation=cli_confirmation,
    )

    client.test_market_order(
        symbol=config["symbol"],
        side=plan["action"].lower(),
        funds=plan["funds"],
        size=plan["size"],
        client_oid=str(uuid.uuid4()),
    )

    client_oid = str(uuid.uuid4())
    result = client.place_market_order(
        symbol=config["symbol"],
        side=plan["action"].lower(),
        funds=plan["funds"],
        size=plan["size"],
        client_oid=client_oid,
    )

    reconciled: dict[str, Any] | None = None
    for _ in range(8):
        time.sleep(1)
        try:
            reconciled = client.get_order_by_client_oid(client_oid=client_oid, symbol=config["symbol"])
            if str(reconciled.get("isActive", "false")).lower() in {"false", "0"}:
                break
        except KuCoinAPIError:
            continue

    time.sleep(1)
    after = account_snapshot(client, config)
    try:
        update_position_state_after_fill(
            state=state,
            before=account,
            after=after,
            plan=plan,
            config=config,
        )
    except Exception:
        Path(config["kill_switch_path"]).touch(exist_ok=True)
        state["last_order"] = {
            "result": result,
            "reconciled": reconciled,
            "plan": serializable(plan),
            "warning": "Riconciliazione saldo fallita; kill switch creato.",
        }
        save_state(state, config)
        raise

    current_turnover = decimal_value(state.get("daily_turnover_usdt", "0"))
    turnover_after = current_turnover + plan["order_value_usdt"]
    state.update(
        {
            "daily_turnover_usdt": decimal_text(turnover_after),
            "last_executed_candle_utc": plan["candle_time_utc"],
            "last_order_time_utc": iso_utc(),
            "last_client_oid": client_oid,
            "last_order": {
                "result": result,
                "reconciled": reconciled,
                "plan": serializable(plan),
            },
        }
    )
    if plan.get("kill_after_execution") is True:
        Path(config["kill_switch_path"]).touch(exist_ok=True)
    save_state(state, config)

    order_id = result.get("orderId", "") if isinstance(result, dict) else ""
    append_order_log(
        config,
        {
            "time_utc": iso_utc(),
            "client_oid": client_oid,
            "order_id": order_id,
            "symbol": config["symbol"],
            "side": plan["action"],
            "reason": plan["reason"],
            "risk_exit": plan.get("risk_exit"),
            "planned_value_usdt": plan["order_value_usdt"],
            "planned_funds": plan["funds"],
            "planned_size": plan["size"],
            "candle_time_utc": plan["candle_time_utc"],
            "target_sol_weight": plan["target_sol_weight"],
            "current_sol_weight": plan["current_sol_weight"],
            "daily_turnover_after_usdt": turnover_after,
            "average_cost_after_usdt": state.get("average_cost_usdt"),
            "tracked_sol_after": state.get("tracked_sol_units"),
            "realized_pnl_this_order_usdt": state.get("last_realized_pnl_usdt"),
            "reconciled_deal_funds": reconciled.get("dealFunds", "") if isinstance(reconciled, dict) else "",
            "reconciled_deal_size": reconciled.get("dealSize", "") if isinstance(reconciled, dict) else "",
            "reconciled_fee": reconciled.get("fee", "") if isinstance(reconciled, dict) else "",
            "reconciled_fee_currency": reconciled.get("feeCurrency", "") if isinstance(reconciled, dict) else "",
        },
    )

    managed_after = managed_snapshot(after, state)
    risk_after = refresh_state_periods(state, managed_after, after, config)
    write_status(
        config=config,
        account=after,
        managed=managed_after,
        strategy=strategy,
        risk=risk_after,
        state=state,
        plan=plan,
        real_result=result,
        reconciled_order=reconciled,
    )
    notify_order_safely(
        config=config,
        account=after,
        managed=managed_after,
        strategy=strategy,
        risk=risk_after,
        state=state,
        plan=plan,
        reconciled=reconciled,
        order_id=order_id,
    )
    print("ORDINE REALE INVIATO.")
    print("clientOid:", client_oid)
    print("orderId:", order_id or "non restituito")
    print("Riconciliazione:", "OK" if reconciled is not None else "PENDING - NON RIPETERE")
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="SOL Adaptive Range Guarded v1")
    parser.add_argument(
        "command",
        nargs="?",
        choices=("status", "test-order", "telegram-test", "telegram-status", "execute"),
        default="status",
    )
    parser.add_argument("--confirm", default=None, help="Required only for a real order.")
    parser.add_argument("--force", action="store_true", help="Force a Telegram status message.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        if args.command == "status":
            return run_status()
        if args.command == "test-order":
            return run_test_order()
        if args.command == "telegram-test":
            return run_telegram_test()
        if args.command == "telegram-status":
            return run_telegram_status(force=args.force)
        return run_execute(args.confirm)
    except (LiveSafetyError, KuCoinAPIError, OSError, ValueError) as exc:
        print(f"BLOCCATO: {exc}")
        notify_error_safely(f"{type(exc).__name__}: {exc}")
        return 2
    except Exception as exc:
        print(f"ERRORE NON PREVISTO: {type(exc).__name__}: {exc}")
        notify_error_safely(f"{type(exc).__name__}: {exc}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
