# -*- coding: utf-8 -*-
"""Block 4.5 Crash Cascade Guard and liquidation-realism model.

Paper-only safety layer.

Normal market behaviour is pass-through: executable signals are not reduced.
Filtering starts only for stale data, statistically abnormal volatility,
directional cascades or the short recovery period following a cascade.

The module also:
- keeps a counterfactual simulation of every blocked signal;
- measures losses avoided and profits missed;
- runs portfolio-wide +/-10/20/30/40 percent stress tests;
- supplies a conservative stop/liquidation resolver to the Paper engine.

It does not place orders and does not modify the live spot bot.
"""

from __future__ import annotations

import csv
import json
import math
import statistics
from dataclasses import asdict, is_dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Iterable

import pandas as pd

from kucoin_public_data import bundle_frames, safe_float


REPORTS_DIR = Path("reports")
CONFIG_PATH = Path("config/crash_guard_block4_5.json")

STATE_PATH = REPORTS_DIR / "paper_trading_crash_guard_state.json"
DECISIONS_PATH = REPORTS_DIR / "paper_trading_crash_guard_decisions.csv"
EVENTS_PATH = REPORTS_DIR / "paper_trading_crash_guard_events.csv"
SHADOW_RESULTS_PATH = (
    REPORTS_DIR / "paper_trading_crash_guard_shadow_results.csv"
)
STRESS_PATH = REPORTS_DIR / "paper_trading_crash_guard_stress_test.json"
REPORT_PATH = REPORTS_DIR / "paper_trading_crash_guard_report.md"
CONFIG_SNAPSHOT_PATH = (
    REPORTS_DIR / "paper_trading_crash_guard_config_snapshot.json"
)

ENGINE_VERSION = "block4_5-crash-guard-v1.1"
RISK_MODEL_VERSION = "block4_5_v1"
MARKET_SCOPE_VERSION = "asset_market_separation_v1"
SCHEMA_VERSION = 1

_CONFIG_CACHE: dict[str, Any] | None = None
_CONFIG_CACHE_MTIME_NS: int | None = None

LEVEL_RANK = {
    "NORMAL": 0,
    "WATCH": 1,
    "STRESS": 2,
    "RECOVERY": 3,
    "CRASH": 4,
    "EXTREME": 5,
    "DATA_GUARD": 6,
}

DECISION_FIELDS = [
    "generated_utc",
    "signal_id",
    "portfolio",
    "strategy",
    "asset",
    "side",
    "leverage",
    "score",
    "guard_level",
    "guard_direction",
    "asset_level",
    "decision",
    "reason",
    "simulation_started",
]

EVENT_FIELDS = [
    "generated_utc",
    "event_type",
    "previous_level",
    "current_level",
    "direction",
    "cooldown_until_utc",
    "blocked_signals",
    "details_json",
]

SHADOW_RESULT_FIELDS = [
    "generated_utc",
    "signal_id",
    "portfolio",
    "strategy",
    "asset",
    "side",
    "leverage",
    "guard_level",
    "guard_direction",
    "block_reason",
    "opened_at",
    "closed_at",
    "entry_price",
    "exit_price",
    "stop_price",
    "target_price",
    "liquidation_price",
    "close_reason",
    "outcome_r",
    "guard_value_r",
    "would_have_won",
    "would_have_liquidated",
    "holding_hours",
    "full_from_signal",
]

DEFAULT_CONFIG: dict[str, Any] = {
    "schema_version": 1,
    "enabled": True,
    "paper_only": True,
    "normal_market_passthrough": True,
    "protect_spot_or_1x": False,
    "risk_model_version": RISK_MODEL_VERSION,
    "analysis_timeframes_minutes": [15, 60],
    "thresholds": {
        "watch_mark_move_pct": 2.0,
        "stress_mark_move_pct": 3.5,
        "crash_mark_move_pct": 6.0,
        "extreme_mark_move_pct": 10.0,
        "watch_15m_return_pct": 2.0,
        "stress_15m_return_pct": 3.5,
        "crash_15m_return_pct": 5.0,
        "extreme_15m_return_pct": 8.0,
        "watch_15m_range_pct": 4.0,
        "stress_15m_range_pct": 6.0,
        "crash_15m_range_pct": 9.0,
        "extreme_15m_range_pct": 15.0,
        "stress_range_multiple": 3.0,
        "crash_range_multiple": 5.0,
        "extreme_range_multiple": 8.0,
        "stress_60m_return_pct": 6.0,
        "crash_60m_return_pct": 9.0,
        "extreme_60m_return_pct": 15.0,
        "breadth_move_pct": 2.0,
        "breadth_stress_fraction": 0.50,
        "breadth_crash_fraction": 0.65,
        "breadth_extreme_fraction": 0.80,
    },
    "market_scope": {
        "version": MARKET_SCOPE_VERSION,
        "core_assets": ["BTC", "ETH", "SOL"],
        "stress_breadth_fraction": 0.35,
        "crash_breadth_fraction": 0.50,
        "extreme_breadth_fraction": 0.65,
        "stress_min_core_count": 2,
        "crash_require_btc": True,
        "crash_min_additional_core_count": 1,
        "extreme_require_btc": True,
        "extreme_min_additional_core_count": 1,
    },
    "entry_policy": {
        "block_all_leveraged_on_extreme": True,
        "block_with_direction_on_crash": True,
        "block_all_leveraged_on_stale_data": True,
        "stress_max_new_leveraged_per_cycle": 2,
        "stress_max_correlated_same_direction": 3,
        "recovery_max_new_leveraged_per_cycle": 1,
        "recovery_max_correlated_same_direction": 2,
        "crash_opposite_direction_max_new_per_cycle": 1,
        "cooldown_minutes_after_crash": 30,
        "cooldown_minutes_after_extreme": 60,
    },
    "execution_model": {
        "intrabar_liquidation_policy": (
            "WORST_CASE_IF_STOP_AND_LIQUIDATION_CROSSED_IN_CRASH"
        ),
        "normal_extra_slippage_bps": 0.0,
        "watch_extra_slippage_bps": 5.0,
        "stress_extra_slippage_bps": 30.0,
        "recovery_extra_slippage_bps": 20.0,
        "crash_extra_slippage_bps": 100.0,
        "extreme_extra_slippage_bps": 250.0,
        "gap_extra_slippage_bps": 40.0,
        "penetration_capture_fraction": 0.35,
        "maximum_stop_slippage_pct": 0.15,
    },
    "blocked_signal_shadow": {
        "enabled": True,
        "maximum_active_simulations": 5000,
        "maximum_seen_signal_ids": 50000,
        "same_candle_policy": "STOP_FIRST",
        "estimated_round_trip_fee_bps": 12.0,
    },
    "stress_test": {
        "shock_fractions": [0.10, 0.20, 0.30, 0.40],
        "isolated_margin_loss_cap": True,
    },
    "live_readiness_requirements": {
        "margin_mode": "ISOLATED",
        "exchange_native_stop_required": True,
        "stop_confirmation_required_before_position_acceptance": True,
        "cross_margin_forbidden": True,
    },
}


def now_utc() -> datetime:
    return datetime.now(timezone.utc)


def iso_utc(value: datetime | None = None) -> str:
    return (value or now_utc()).astimezone(timezone.utc).isoformat(
        timespec="seconds"
    )


def parse_time(value: Any) -> datetime:
    timestamp = pd.Timestamp(value)
    if timestamp.tzinfo is None:
        timestamp = timestamp.tz_localize("UTC")
    return timestamp.to_pydatetime()


def finite(value: Any, default: float = 0.0) -> float:
    try:
        number = float(value)
    except (TypeError, ValueError):
        return default
    return number if math.isfinite(number) else default


def truthy(value: Any) -> bool:
    return str(value).strip().lower() in {
        "1", "true", "yes", "y"
    }


def signal_dict(signal: Any) -> dict[str, Any]:
    if is_dataclass(signal):
        return asdict(signal)
    if hasattr(signal, "to_dict"):
        return dict(signal.to_dict())
    if isinstance(signal, dict):
        return dict(signal)
    return dict(vars(signal))


def deep_merge(
    base: dict[str, Any],
    custom: dict[str, Any],
) -> dict[str, Any]:
    output = json.loads(json.dumps(base))
    for key, value in custom.items():
        if (
            isinstance(value, dict)
            and isinstance(output.get(key), dict)
        ):
            output[key] = deep_merge(output[key], value)
        else:
            output[key] = value
    return output


def atomic_write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(text, encoding="utf-8")
    temporary.replace(path)


def atomic_write_json(path: Path, value: Any) -> None:
    atomic_write_text(
        path,
        json.dumps(
            value,
            ensure_ascii=False,
            indent=2,
            sort_keys=True,
        )
        + "\n",
    )


def append_csv(
    path: Path,
    fields: list[str],
    rows: Iterable[dict[str, Any]],
) -> None:
    rows = list(rows)
    if not rows:
        if not path.exists():
            path.parent.mkdir(parents=True, exist_ok=True)
            with path.open(
                "w",
                encoding="utf-8",
                newline="",
            ) as handle:
                csv.DictWriter(
                    handle,
                    fieldnames=fields,
                ).writeheader()
        return

    path.parent.mkdir(parents=True, exist_ok=True)
    exists = path.exists() and path.stat().st_size > 0
    with path.open(
        "a",
        encoding="utf-8",
        newline="",
    ) as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=fields,
            extrasaction="ignore",
        )
        if not exists:
            writer.writeheader()
        for row in rows:
            writer.writerow(
                {field: row.get(field, "") for field in fields}
            )


def load_config() -> dict[str, Any]:
    global _CONFIG_CACHE, _CONFIG_CACHE_MTIME_NS

    mtime_ns = (
        CONFIG_PATH.stat().st_mtime_ns
        if CONFIG_PATH.exists()
        else None
    )
    if (
        _CONFIG_CACHE is not None
        and _CONFIG_CACHE_MTIME_NS == mtime_ns
    ):
        return json.loads(json.dumps(_CONFIG_CACHE))

    config = json.loads(json.dumps(DEFAULT_CONFIG))
    if CONFIG_PATH.exists():
        try:
            custom = json.loads(
                CONFIG_PATH.read_text(encoding="utf-8")
            )
            if isinstance(custom, dict):
                config = deep_merge(config, custom)
        except Exception as exc:
            print(
                "Configurazione Block 4.5 non valida, uso default: "
                f"{exc}"
            )

    _CONFIG_CACHE = json.loads(json.dumps(config))
    _CONFIG_CACHE_MTIME_NS = mtime_ns
    atomic_write_json(CONFIG_SNAPSHOT_PATH, config)
    return json.loads(json.dumps(config))


def load_state() -> dict[str, Any]:
    default = {
        "schema_version": SCHEMA_VERSION,
        "engine_version": ENGINE_VERSION,
        "market_scope_version": MARKET_SCOPE_VERSION,
        "created_utc": iso_utc(),
        "updated_utc": iso_utc(),
        "previous_level": "NORMAL",
        "previous_direction": "NONE",
        "cooldown_until_utc": "",
        "active_simulations": {},
        "seen_blocked_signal_ids": [],
        "totals": {
            "blocked_signals": 0,
            "completed_simulations": 0,
            "avoided_liquidations": 0,
            "guard_value_r": 0.0,
            "missed_profit_r": 0.0,
        },
    }
    if not STATE_PATH.exists():
        return default
    try:
        value = json.loads(
            STATE_PATH.read_text(encoding="utf-8")
        )
        if not isinstance(value, dict):
            return default
    except Exception:
        return default

    legacy_scope_missing = "market_scope_version" not in value
    for key, item in default.items():
        value.setdefault(key, item)
    if legacy_scope_missing:
        value["market_scope_version"] = "legacy_block4_5_v1"
    value.setdefault("active_simulations", {})
    value.setdefault("seen_blocked_signal_ids", [])
    value.setdefault("totals", default["totals"])
    return value


def level_max(first: str, second: str) -> str:
    return (
        first
        if LEVEL_RANK.get(first, 0)
        >= LEVEL_RANK.get(second, 0)
        else second
    )


def level_for_magnitude(
    mark_move: float,
    return_15: float,
    range_15: float,
    range_multiple: float,
    return_60: float,
    thresholds: dict[str, Any],
) -> str:
    magnitude_mark = abs(mark_move)
    magnitude_15 = abs(return_15)
    magnitude_60 = abs(return_60)

    if (
        magnitude_mark
        >= finite(thresholds["extreme_mark_move_pct"])
        or magnitude_15
        >= finite(thresholds["extreme_15m_return_pct"])
        or range_15
        >= finite(thresholds["extreme_15m_range_pct"])
        or (
            range_15
            >= finite(thresholds["crash_15m_range_pct"])
            and range_multiple
            >= finite(thresholds["extreme_range_multiple"])
        )
        or magnitude_60
        >= finite(thresholds["extreme_60m_return_pct"])
    ):
        return "EXTREME"
    if (
        magnitude_mark
        >= finite(thresholds["crash_mark_move_pct"])
        or magnitude_15
        >= finite(thresholds["crash_15m_return_pct"])
        or range_15
        >= finite(thresholds["crash_15m_range_pct"])
        or (
            range_15
            >= finite(thresholds["stress_15m_range_pct"])
            and range_multiple
            >= finite(thresholds["crash_range_multiple"])
        )
        or magnitude_60
        >= finite(thresholds["crash_60m_return_pct"])
    ):
        return "CRASH"
    if (
        magnitude_mark
        >= finite(thresholds["stress_mark_move_pct"])
        or magnitude_15
        >= finite(thresholds["stress_15m_return_pct"])
        or range_15
        >= finite(thresholds["stress_15m_range_pct"])
        or (
            range_15
            >= finite(thresholds["watch_15m_range_pct"])
            and range_multiple
            >= finite(thresholds["stress_range_multiple"])
        )
        or magnitude_60
        >= finite(thresholds["stress_60m_return_pct"])
    ):
        return "STRESS"
    if (
        magnitude_mark
        >= finite(thresholds["watch_mark_move_pct"])
        or magnitude_15
        >= finite(thresholds["watch_15m_return_pct"])
        or range_15
        >= finite(thresholds["watch_15m_range_pct"])
    ):
        return "WATCH"
    return "NORMAL"


def asset_market_metrics(
    asset: str,
    bundle: dict[str, Any],
    frames: dict[str, dict[int, pd.DataFrame]],
    config: dict[str, Any],
) -> dict[str, Any]:
    thresholds = config["thresholds"]
    frame_15 = frames.get(asset, {}).get(15)
    frame_60 = frames.get(asset, {}).get(60)

    if frame_15 is None or frame_15.empty:
        return {
            "asset": asset,
            "level": "DATA_GUARD",
            "direction": "NONE",
            "reason": "NO_15M_CANDLES",
        }

    candle_15 = frame_15.iloc[-1]
    opened_15 = max(finite(candle_15.get("open")), 1e-12)
    close_15 = finite(candle_15.get("close"), opened_15)
    high_15 = finite(candle_15.get("high"), opened_15)
    low_15 = finite(candle_15.get("low"), opened_15)

    return_15 = (close_15 / opened_15 - 1.0) * 100.0
    range_15 = (high_15 - low_15) / opened_15 * 100.0

    previous_ranges: list[float] = []
    if len(frame_15) > 1:
        history = frame_15.iloc[-49:-1]
        for _, candle in history.iterrows():
            opened = max(finite(candle.get("open")), 1e-12)
            previous_ranges.append(
                (
                    finite(candle.get("high"), opened)
                    - finite(candle.get("low"), opened)
                )
                / opened
                * 100.0
            )
    median_range = (
        statistics.median(previous_ranges)
        if previous_ranges
        else max(range_15, 0.01)
    )
    range_multiple = range_15 / max(median_range, 0.01)

    return_60 = 0.0
    if frame_60 is not None and not frame_60.empty:
        candle_60 = frame_60.iloc[-1]
        opened_60 = max(finite(candle_60.get("open")), 1e-12)
        return_60 = (
            finite(candle_60.get("close"), opened_60)
            / opened_60
            - 1.0
        ) * 100.0

    mark = finite(
        bundle.get("assets", {}).get(asset, {}).get("mark_price"),
        close_15,
    )
    mark_move = (mark / max(close_15, 1e-12) - 1.0) * 100.0

    directional_value = (
        mark_move
        if abs(mark_move) >= abs(return_15)
        else return_15
    )
    if abs(return_60) > abs(directional_value):
        directional_value = return_60
    direction = (
        "DOWN"
        if directional_value < 0
        else "UP"
        if directional_value > 0
        else "NONE"
    )

    level = level_for_magnitude(
        mark_move,
        return_15,
        range_15,
        range_multiple,
        return_60,
        thresholds,
    )
    return {
        "asset": asset,
        "level": level,
        "direction": direction,
        "mark_move_pct": mark_move,
        "return_15m_pct": return_15,
        "range_15m_pct": range_15,
        "range_multiple": range_multiple,
        "return_60m_pct": return_60,
        "candle_time_15m": pd.Timestamp(
            frame_15.index[-1]
        ).isoformat(),
    }


def market_context(
    bundle: dict[str, Any],
    config: dict[str, Any],
    state: dict[str, Any],
    when: datetime,
) -> dict[str, Any]:
    scope = config.get("market_scope", {})
    scope_version = str(
        scope.get("version", MARKET_SCOPE_VERSION)
    )

    # One-time migration from Block 4.5 v1. The old implementation could
    # start a global cooldown from one isolated volatile asset. That cooldown
    # must not survive the Asset/Market separation upgrade.
    if state.get("market_scope_version") != scope_version:
        state["market_scope_version"] = scope_version
        state["cooldown_until_utc"] = ""
        state["previous_level"] = "NORMAL"
        state["previous_direction"] = "NONE"

    freshness = bundle.get("_paper_freshness", {})
    freshness_status = str(
        freshness.get("status", "FRESH")
    ).upper()
    source = str(bundle.get("source", "")).upper()
    if (
        freshness_status not in {"FRESH", "OK"}
        or "STALE" in source
    ):
        return {
            "generated_utc": iso_utc(when),
            "risk_model_version": RISK_MODEL_VERSION,
            "market_scope_version": scope_version,
            "level": "DATA_GUARD",
            "direction": "NONE",
            "reason": (
                f"MARKET_DATA_{freshness_status or 'UNKNOWN'}"
            ),
            "market_level_source": "DATA_QUALITY",
            "asset_context": {},
            "isolated_asset_alerts": [],
            "cooldown_until_utc": state.get(
                "cooldown_until_utc",
                "",
            ),
        }

    frames = bundle_frames(bundle)
    assets = sorted(bundle.get("assets", {}))
    asset_context = {
        asset: asset_market_metrics(
            asset,
            bundle,
            frames,
            config,
        )
        for asset in assets
    }

    valid_metrics = [
        metrics
        for metrics in asset_context.values()
        if metrics.get("level") != "DATA_GUARD"
    ]
    count = len(valid_metrics)
    thresholds = config["thresholds"]
    breadth_move = finite(thresholds["breadth_move_pct"])
    returns = [
        finite(metrics.get("return_15m_pct"))
        for metrics in valid_metrics
    ]
    down_fraction = (
        sum(value <= -breadth_move for value in returns) / count
        if count
        else 0.0
    )
    up_fraction = (
        sum(value >= breadth_move for value in returns) / count
        if count
        else 0.0
    )
    median_return = statistics.median(returns) if returns else 0.0

    core_assets = {
        str(asset).upper()
        for asset in scope.get(
            "core_assets",
            ["BTC", "ETH", "SOL"],
        )
    }
    directional: dict[str, dict[str, Any]] = {}
    for direction in ("DOWN", "UP"):
        matching = [
            metrics
            for metrics in valid_metrics
            if str(metrics.get("direction")) == direction
        ]
        stress_assets = [
            metrics
            for metrics in matching
            if LEVEL_RANK.get(str(metrics.get("level")), 0)
            >= LEVEL_RANK["STRESS"]
        ]
        crash_assets = [
            metrics
            for metrics in matching
            if LEVEL_RANK.get(str(metrics.get("level")), 0)
            >= LEVEL_RANK["CRASH"]
        ]
        extreme_assets = [
            metrics
            for metrics in matching
            if LEVEL_RANK.get(str(metrics.get("level")), 0)
            >= LEVEL_RANK["EXTREME"]
        ]

        stress_core = {
            str(metrics.get("asset", "")).upper()
            for metrics in stress_assets
            if str(metrics.get("asset", "")).upper()
            in core_assets
        }
        crash_core = {
            str(metrics.get("asset", "")).upper()
            for metrics in crash_assets
            if str(metrics.get("asset", "")).upper()
            in core_assets
        }
        extreme_core = {
            str(metrics.get("asset", "")).upper()
            for metrics in extreme_assets
            if str(metrics.get("asset", "")).upper()
            in core_assets
        }

        non_btc_crash_core = crash_core - {"BTC"}
        non_btc_extreme_core = extreme_core - {"BTC"}
        crash_core_trigger = (
            (
                not truthy(scope.get("crash_require_btc", True))
                or "BTC" in crash_core
            )
            and len(non_btc_crash_core)
            >= int(
                finite(
                    scope.get(
                        "crash_min_additional_core_count",
                        1,
                    ),
                    1,
                )
            )
        )
        extreme_core_trigger = (
            (
                not truthy(scope.get("extreme_require_btc", True))
                or "BTC" in extreme_core
            )
            and len(non_btc_extreme_core)
            >= int(
                finite(
                    scope.get(
                        "extreme_min_additional_core_count",
                        1,
                    ),
                    1,
                )
            )
        )
        stress_core_trigger = len(stress_core) >= int(
            finite(scope.get("stress_min_core_count", 2), 2)
        )

        directional[direction] = {
            "stress_count": len(stress_assets),
            "crash_count": len(crash_assets),
            "extreme_count": len(extreme_assets),
            "stress_fraction": (
                len(stress_assets) / count if count else 0.0
            ),
            "crash_fraction": (
                len(crash_assets) / count if count else 0.0
            ),
            "extreme_fraction": (
                len(extreme_assets) / count if count else 0.0
            ),
            "stress_core_assets": sorted(stress_core),
            "crash_core_assets": sorted(crash_core),
            "extreme_core_assets": sorted(extreme_core),
            "stress_core_trigger": stress_core_trigger,
            "crash_core_trigger": crash_core_trigger,
            "extreme_core_trigger": extreme_core_trigger,
        }

    candidates: list[tuple[str, str, str, float]] = []
    for direction, metrics in directional.items():
        if (
            metrics["extreme_fraction"]
            >= finite(scope.get("extreme_breadth_fraction", 0.65))
            or metrics["extreme_core_trigger"]
        ):
            candidates.append(
                (
                    "EXTREME",
                    direction,
                    (
                        "CORE_OVERRIDE"
                        if metrics["extreme_core_trigger"]
                        else "BREADTH"
                    ),
                    metrics["extreme_fraction"],
                )
            )
        elif (
            metrics["crash_fraction"]
            >= finite(scope.get("crash_breadth_fraction", 0.50))
            or metrics["crash_core_trigger"]
        ):
            candidates.append(
                (
                    "CRASH",
                    direction,
                    (
                        "CORE_OVERRIDE"
                        if metrics["crash_core_trigger"]
                        else "BREADTH"
                    ),
                    metrics["crash_fraction"],
                )
            )
        elif (
            metrics["stress_fraction"]
            >= finite(scope.get("stress_breadth_fraction", 0.35))
            or metrics["stress_core_trigger"]
        ):
            candidates.append(
                (
                    "STRESS",
                    direction,
                    (
                        "CORE_OVERRIDE"
                        if metrics["stress_core_trigger"]
                        else "BREADTH"
                    ),
                    metrics["stress_fraction"],
                )
            )

    if candidates:
        global_level, global_direction, trigger, _ = max(
            candidates,
            key=lambda item: (
                LEVEL_RANK[item[0]],
                item[3],
                item[1] == (
                    "UP" if median_return >= 0.0 else "DOWN"
                ),
            ),
        )
        market_level_source = f"MARKET_{trigger}"
    else:
        global_level = "NORMAL"
        global_direction = "NONE"
        market_level_source = "NO_MARKET_WIDE_TRIGGER"

    isolated_asset_alerts = [
        {
            "asset": metrics.get("asset"),
            "level": metrics.get("level"),
            "direction": metrics.get("direction"),
        }
        for metrics in valid_metrics
        if LEVEL_RANK.get(str(metrics.get("level")), 0)
        >= LEVEL_RANK["STRESS"]
    ]

    policy = config["entry_policy"]
    cooldown_until = str(state.get("cooldown_until_utc", ""))
    previous_direction = str(
        state.get("previous_direction", "NONE")
    )
    if global_level in {"CRASH", "EXTREME"}:
        minutes = (
            finite(policy["cooldown_minutes_after_extreme"])
            if global_level == "EXTREME"
            else finite(policy["cooldown_minutes_after_crash"])
        )
        cooldown = when + timedelta(minutes=minutes)
        cooldown_until = iso_utc(cooldown)
        state["cooldown_until_utc"] = cooldown_until
        state["previous_direction"] = global_direction
    else:
        try:
            cooldown_time = (
                parse_time(cooldown_until)
                if cooldown_until
                else None
            )
        except Exception:
            cooldown_time = None
        if cooldown_time is not None and when < cooldown_time:
            global_level = "RECOVERY"
            global_direction = previous_direction
            market_level_source = "VALID_MARKET_COOLDOWN"
        elif cooldown_time is not None:
            state["cooldown_until_utc"] = ""
            cooldown_until = ""

    return {
        "generated_utc": iso_utc(when),
        "risk_model_version": RISK_MODEL_VERSION,
        "market_scope_version": scope_version,
        "level": global_level,
        "direction": global_direction,
        "reason": "MARKET_METRICS_ASSET_SEPARATED",
        "market_level_source": market_level_source,
        "down_breadth_fraction": down_fraction,
        "up_breadth_fraction": up_fraction,
        "median_15m_return_pct": median_return,
        "directional_market_evidence": directional,
        "asset_context": asset_context,
        "isolated_asset_alerts": isolated_asset_alerts,
        "cooldown_until_utc": cooldown_until,
    }

def open_leveraged_positions(
    paper_state: dict[str, Any],
) -> list[dict[str, Any]]:
    output = []
    for portfolio_name, portfolio in paper_state.get(
        "portfolios", {}
    ).items():
        for position in portfolio.get("open_positions", []):
            if finite(position.get("leverage"), 1.0) <= 1.0:
                continue
            output.append(
                {
                    **position,
                    "_portfolio_name": portfolio_name,
                }
            )
    return output


def signal_block_reason(
    row: dict[str, Any],
    context: dict[str, Any],
    config: dict[str, Any],
    correlated_count: int,
    admitted_this_cycle: int,
) -> str:
    leverage = finite(row.get("leverage"), 1.0)
    if (
        leverage <= 1.0
        and not truthy(config.get("protect_spot_or_1x"))
    ):
        return ""

    level = str(context.get("level", "NORMAL"))
    direction = str(context.get("direction", "NONE"))
    side = str(row.get("side", "")).upper()
    asset = str(row.get("asset", ""))
    asset_metrics = context.get("asset_context", {}).get(
        asset,
        {},
    )
    asset_level = str(asset_metrics.get("level", "NORMAL"))
    asset_direction = str(
        asset_metrics.get("direction", "NONE")
    )
    policy = config["entry_policy"]

    if level == "DATA_GUARD" and truthy(
        policy["block_all_leveraged_on_stale_data"]
    ):
        return "CRASH_GUARD_STALE_MARKET_DATA"

    if level == "EXTREME" and truthy(
        policy["block_all_leveraged_on_extreme"]
    ):
        return "CRASH_GUARD_GLOBAL_EXTREME"

    if (
        asset_level == "EXTREME"
        and truthy(policy["block_all_leveraged_on_extreme"])
    ):
        return "CRASH_GUARD_ASSET_EXTREME"

    if level == "CRASH" and truthy(
        policy["block_with_direction_on_crash"]
    ):
        if (
            direction == "DOWN" and side == "LONG"
        ) or (
            direction == "UP" and side == "SHORT"
        ):
            return "CRASH_GUARD_GLOBAL_DIRECTIONAL"

    if asset_level == "CRASH" and truthy(
        policy["block_with_direction_on_crash"]
    ):
        if (
            asset_direction == "DOWN" and side == "LONG"
        ) or (
            asset_direction == "UP" and side == "SHORT"
        ):
            return "CRASH_GUARD_ASSET_DIRECTIONAL"

    if level == "RECOVERY":
        if admitted_this_cycle >= int(
            finite(
                policy[
                    "recovery_max_new_leveraged_per_cycle"
                ],
                1,
            )
        ):
            return "CRASH_GUARD_RECOVERY_CYCLE_LIMIT"
        if correlated_count >= int(
            finite(
                policy[
                    "recovery_max_correlated_same_direction"
                ],
                2,
            )
        ):
            return "CRASH_GUARD_RECOVERY_CORRELATION_LIMIT"

    if level == "STRESS":
        if admitted_this_cycle >= int(
            finite(
                policy[
                    "stress_max_new_leveraged_per_cycle"
                ],
                2,
            )
        ):
            return "CRASH_GUARD_STRESS_CYCLE_LIMIT"
        if correlated_count >= int(
            finite(
                policy[
                    "stress_max_correlated_same_direction"
                ],
                3,
            )
        ):
            return "CRASH_GUARD_STRESS_CORRELATION_LIMIT"

    if level == "CRASH":
        adverse = (
            (direction == "DOWN" and side == "LONG")
            or (direction == "UP" and side == "SHORT")
        )
        if not adverse and admitted_this_cycle >= int(
            finite(
                policy[
                    "crash_opposite_direction_max_new_per_cycle"
                ],
                1,
            )
        ):
            return "CRASH_GUARD_CRASH_CYCLE_LIMIT"

    return ""


def simulation_from_signal(
    row: dict[str, Any],
    context: dict[str, Any],
    bundle: dict[str, Any],
    when: datetime,
    reason: str,
) -> dict[str, Any]:
    side = str(row.get("side", "")).upper()
    direction = 1.0 if side == "LONG" else -1.0
    asset = str(row.get("asset", ""))
    entry = finite(
        bundle.get("assets", {}).get(asset, {}).get(
            "mark_price"
        ),
        finite(row.get("entry_reference_price")),
    )
    stop_pct = max(finite(row.get("stop_pct"), 0.01), 0.0001)
    target_pct = max(
        finite(row.get("target_pct"), stop_pct * 2.0),
        0.0001,
    )
    leverage = max(finite(row.get("leverage"), 1.0), 1.0)
    liquidation_distance = max(0.001, 1.0 / leverage - 0.005)

    frames = bundle_frames(bundle)
    frame = frames.get(asset, {}).get(15)
    last_candle = (
        pd.Timestamp(frame.index[-1]).isoformat()
        if frame is not None and not frame.empty
        else ""
    )

    return {
        "signal_id": str(row.get("signal_id", "")),
        "portfolio": str(row.get("portfolio", "")),
        "strategy": str(row.get("strategy", "")),
        "asset": asset,
        "side": side,
        "leverage": leverage,
        "guard_level": str(context.get("level", "")),
        "guard_direction": str(context.get("direction", "")),
        "block_reason": reason,
        "opened_at": iso_utc(when),
        "entry_price": entry,
        "stop_pct": stop_pct,
        "target_pct": target_pct,
        "stop_price": entry * (1.0 - direction * stop_pct),
        "target_price": entry * (
            1.0 + direction * target_pct
        ),
        "liquidation_price": entry * (
            1.0 - direction * liquidation_distance
        ),
        "max_holding_hours": max(
            finite(row.get("max_holding_hours"), 24.0),
            1.0,
        ),
        "last_processed_candle": last_candle,
        "full_from_signal": True,
    }


def shadow_exit_decision(
    simulation: dict[str, Any],
    candle: pd.Series,
    config: dict[str, Any],
) -> tuple[float | None, str]:
    side = simulation["side"]
    stop = finite(simulation["stop_price"])
    target = finite(simulation["target_price"])
    liquidation = finite(simulation["liquidation_price"])
    opened = finite(candle.get("open"))
    high = finite(candle.get("high"))
    low = finite(candle.get("low"))

    if side == "LONG":
        if opened <= liquidation:
            return liquidation, "LIQUIDATION_GAP"
        stop_hit = low <= stop
        target_hit = high >= target
        liquidation_crossed = low <= liquidation
    else:
        if opened >= liquidation:
            return liquidation, "LIQUIDATION_GAP"
        stop_hit = high >= stop
        target_hit = low <= target
        liquidation_crossed = high >= liquidation

    if stop_hit and liquidation_crossed:
        return liquidation, "LIQUIDATION_INTRABAR_WORST_CASE"
    if stop_hit and target_hit:
        if (
            config["blocked_signal_shadow"][
                "same_candle_policy"
            ]
            == "TARGET_FIRST"
        ):
            return target, "TARGET_SAME_CANDLE"
        return stop, "STOP_SAME_CANDLE_CONSERVATIVE"
    if stop_hit:
        return stop, "STOP"
    if target_hit:
        return target, "TARGET"
    return None, ""


def simulation_outcome_r(
    simulation: dict[str, Any],
    exit_price: float,
    config: dict[str, Any],
) -> float:
    entry = max(finite(simulation["entry_price"]), 1e-12)
    direction = (
        1.0 if simulation["side"] == "LONG" else -1.0
    )
    gross_return = (exit_price / entry - 1.0) * direction
    stop_pct = max(finite(simulation["stop_pct"]), 1e-12)
    fee = finite(
        config["blocked_signal_shadow"][
            "estimated_round_trip_fee_bps"
        ]
    ) / 10_000.0
    return (gross_return - fee) / stop_pct


def update_shadow_simulations(
    state: dict[str, Any],
    bundle: dict[str, Any],
    config: dict[str, Any],
    when: datetime,
) -> list[dict[str, Any]]:
    frames = bundle_frames(bundle)
    completed: list[dict[str, Any]] = []
    remaining: dict[str, dict[str, Any]] = {}

    for signal_id, simulation in state.get(
        "active_simulations", {}
    ).items():
        asset = simulation["asset"]
        frame = frames.get(asset, {}).get(15)
        exit_price = None
        close_reason = ""
        closed_at = None

        if frame is not None and not frame.empty:
            last_processed = str(
                simulation.get("last_processed_candle", "")
            )
            for candle_time, candle in frame.iterrows():
                candle_iso = pd.Timestamp(candle_time).isoformat()
                if last_processed and candle_iso <= last_processed:
                    continue
                simulation["last_processed_candle"] = candle_iso
                exit_price, close_reason = shadow_exit_decision(
                    simulation,
                    candle,
                    config,
                )
                if exit_price is not None:
                    closed_at = parse_time(candle_iso)
                    break

        opened_at = parse_time(simulation["opened_at"])
        if exit_price is None and (
            when - opened_at
        ).total_seconds() / 3600.0 >= finite(
            simulation["max_holding_hours"]
        ):
            exit_price = finite(
                bundle.get("assets", {})
                .get(asset, {})
                .get("mark_price"),
                simulation["entry_price"],
            )
            close_reason = "TIME_EXIT"
            closed_at = when

        if exit_price is None:
            remaining[signal_id] = simulation
            continue

        outcome_r = simulation_outcome_r(
            simulation,
            exit_price,
            config,
        )
        result = {
            "generated_utc": iso_utc(when),
            **simulation,
            "closed_at": iso_utc(closed_at or when),
            "exit_price": exit_price,
            "close_reason": close_reason,
            "outcome_r": outcome_r,
            "guard_value_r": -outcome_r,
            "would_have_won": outcome_r > 0,
            "would_have_liquidated": close_reason.startswith(
                "LIQUIDATION"
            ),
            "holding_hours": (
                (closed_at or when) - opened_at
            ).total_seconds()
            / 3600.0,
        }
        completed.append(result)

    state["active_simulations"] = remaining
    totals = state.setdefault("totals", {})
    totals["completed_simulations"] = int(
        totals.get("completed_simulations", 0)
    ) + len(completed)
    totals["avoided_liquidations"] = int(
        totals.get("avoided_liquidations", 0)
    ) + sum(
        truthy(result["would_have_liquidated"])
        for result in completed
    )
    totals["guard_value_r"] = finite(
        totals.get("guard_value_r")
    ) + sum(finite(result["guard_value_r"]) for result in completed)
    totals["missed_profit_r"] = finite(
        totals.get("missed_profit_r")
    ) + sum(
        max(0.0, finite(result["outcome_r"]))
        for result in completed
    )

    append_csv(
        SHADOW_RESULTS_PATH,
        SHADOW_RESULT_FIELDS,
        completed,
    )
    return completed


def filter_signals(
    signals: list[Any],
    paper_state: dict[str, Any],
    bundle: dict[str, Any],
    config: dict[str, Any],
    guard_state: dict[str, Any],
    context: dict[str, Any],
    when: datetime,
) -> tuple[list[Any], list[dict[str, Any]]]:
    seen_blocked = set(
        str(value)
        for value in guard_state.get(
            "seen_blocked_signal_ids", []
        )
    )
    global_passthrough = (
        context.get("level") in {"NORMAL", "WATCH"}
        and truthy(config.get("normal_market_passthrough"))
    )

    active = guard_state.setdefault(
        "active_simulations", {}
    )
    maximum_active = int(
        finite(
            config["blocked_signal_shadow"][
                "maximum_active_simulations"
            ],
            5000,
        )
    )

    positions = open_leveraged_positions(paper_state)
    correlated = {
        "LONG": sum(
            str(position.get("side", "")).upper() == "LONG"
            for position in positions
        ),
        "SHORT": sum(
            str(position.get("side", "")).upper() == "SHORT"
            for position in positions
        ),
    }

    ordered = (
        list(signals)
        if global_passthrough
        else sorted(
            signals,
            key=lambda signal: abs(
                finite(signal_dict(signal).get("score"))
            ),
            reverse=True,
        )
    )
    allowed: list[Any] = []
    decisions: list[dict[str, Any]] = []
    admitted_leveraged = 0

    for signal in ordered:
        row = signal_dict(signal)
        signal_id = str(row.get("signal_id", ""))
        leverage = finite(row.get("leverage"), 1.0)
        side = str(row.get("side", "")).upper()
        asset = str(row.get("asset", ""))
        asset_level = str(
            context.get("asset_context", {})
            .get(asset, {})
            .get("level", "NORMAL")
        )

        if signal_id in seen_blocked:
            decisions.append(
                {
                    "generated_utc": iso_utc(when),
                    **row,
                    "guard_level": context.get("level"),
                    "guard_direction": context.get(
                        "direction"
                    ),
                    "asset_level": asset_level,
                    "decision": "BLOCKED_PREVIOUSLY",
                    "reason": (
                        "CRASH_GUARD_SIGNAL_ALREADY_BLOCKED"
                    ),
                    "simulation_started": False,
                }
            )
            continue

        reason = signal_block_reason(
            row,
            context,
            config,
            correlated.get(side, 0),
            admitted_leveraged,
        )
        if not reason:
            allowed.append(signal)
            if leverage > 1.0:
                admitted_leveraged += 1
                correlated[side] = correlated.get(side, 0) + 1
            continue

        seen_blocked.add(signal_id)
        started = False
        if (
            truthy(
                config["blocked_signal_shadow"]["enabled"]
            )
            and len(active) < maximum_active
            and signal_id
        ):
            active[signal_id] = simulation_from_signal(
                row,
                context,
                bundle,
                when,
                reason,
            )
            started = True

        decisions.append(
            {
                "generated_utc": iso_utc(when),
                **row,
                "guard_level": context.get("level"),
                "guard_direction": context.get(
                    "direction"
                ),
                "asset_level": asset_level,
                "decision": "BLOCKED",
                "reason": reason,
                "simulation_started": started,
            }
        )

    maximum_seen = int(
        finite(
            config["blocked_signal_shadow"][
                "maximum_seen_signal_ids"
            ],
            50000,
        )
    )
    guard_state["seen_blocked_signal_ids"] = list(
        seen_blocked
    )[-maximum_seen:]
    guard_state["active_simulations"] = active
    guard_state.setdefault("totals", {})[
        "blocked_signals"
    ] = int(
        guard_state.setdefault("totals", {}).get(
            "blocked_signals",
            0,
        )
    ) + sum(
        row.get("decision") == "BLOCKED"
        for row in decisions
    )

    append_csv(
        DECISIONS_PATH,
        DECISION_FIELDS,
        decisions,
    )
    return allowed, decisions


def stress_matrix(
    paper_state: dict[str, Any],
    bundle: dict[str, Any],
    config: dict[str, Any],
    when: datetime,
) -> dict[str, Any]:
    positions = open_leveraged_positions(paper_state)
    shocks = [
        finite(value)
        for value in config["stress_test"][
            "shock_fractions"
        ]
    ]
    scenarios = []

    for direction in ("DOWN", "UP"):
        for shock in shocks:
            liquidations = 0
            estimated_loss = 0.0
            margin_at_risk = 0.0
            affected = 0
            for position in positions:
                side = str(position.get("side", "")).upper()
                adverse = (
                    direction == "DOWN" and side == "LONG"
                ) or (
                    direction == "UP" and side == "SHORT"
                )
                if not adverse:
                    continue
                affected += 1
                asset = str(position.get("asset", ""))
                mark = finite(
                    bundle.get("assets", {})
                    .get(asset, {})
                    .get("mark_price"),
                    position.get("entry_price"),
                )
                shocked = (
                    mark * (1.0 - shock)
                    if direction == "DOWN"
                    else mark * (1.0 + shock)
                )
                liquidation = finite(
                    position.get("liquidation_price")
                )
                is_liquidated = (
                    side == "LONG" and shocked <= liquidation
                ) or (
                    side == "SHORT" and shocked >= liquidation
                )
                notional = finite(position.get("notional_eur"))
                margin = finite(position.get("margin_eur"))
                margin_at_risk += margin
                if is_liquidated:
                    liquidations += 1
                    estimated_loss += margin
                else:
                    estimated_loss += min(
                        margin,
                        notional * shock,
                    )

            scenarios.append(
                {
                    "scenario": (
                        f"{direction}_{int(shock * 100)}"
                    ),
                    "direction": direction,
                    "shock_pct": shock * 100.0,
                    "affected_positions": affected,
                    "estimated_liquidations": liquidations,
                    "estimated_loss_eur": estimated_loss,
                    "margin_at_risk_eur": margin_at_risk,
                }
            )

    payload = {
        "schema_version": SCHEMA_VERSION,
        "risk_model_version": RISK_MODEL_VERSION,
        "generated_utc": iso_utc(when),
        "note": (
            "Somma di portafogli Paper indipendenti; non rappresenta "
            "ancora un singolo conto live."
        ),
        "leveraged_open_positions": len(positions),
        "scenarios": scenarios,
    }
    atomic_write_json(STRESS_PATH, payload)
    return payload


def report_markdown(
    context: dict[str, Any],
    decisions: list[dict[str, Any]],
    completed: list[dict[str, Any]],
    guard_state: dict[str, Any],
    stress: dict[str, Any],
    when: datetime,
) -> str:
    totals = guard_state.get("totals", {})
    lines = [
        "# Blocco 4.5 — Crash Cascade Guard",
        "",
        f"Generato: {iso_utc(when)}",
        "",
        "> Paper-only. In mercato NORMAL/WATCH non riduce i segnali. "
        "Le limitazioni iniziano soltanto in STRESS, RECOVERY, CRASH, "
        "EXTREME o con dati non affidabili.",
        "",
        "## Stato corrente",
        "",
        f"- Livello: **{context.get('level', 'NORMAL')}**",
        f"- Direzione: **{context.get('direction', 'NONE')}**",
        f"- Segnali bloccati nel ciclo: **{sum(row.get('decision') == 'BLOCKED' for row in decisions)}**",
        f"- Simulazioni bloccate attive: **{len(guard_state.get('active_simulations', {}))}**",
        f"- Simulazioni completate nel ciclo: **{len(completed)}**",
        f"- Liquidazioni virtuali evitate totali: **{int(totals.get('avoided_liquidations', 0))}**",
        f"- Valore cumulato del filtro: **{finite(totals.get('guard_value_r')):.2f} R**",
        f"- Profitto virtuale mancato: **{finite(totals.get('missed_profit_r')):.2f} R**",
        "",
        "## Stress test portafogli Paper",
        "",
        "| Scenario | Posizioni interessate | Liquidazioni stimate | Perdita stimata EUR |",
        "| --- | ---: | ---: | ---: |",
    ]
    for row in stress.get("scenarios", []):
        lines.append(
            f"| {row['scenario']} | "
            f"{row['affected_positions']} | "
            f"{row['estimated_liquidations']} | "
            f"{row['estimated_loss_eur']:.2f} |"
        )
    lines.extend(
        [
            "",
            "## Modello di esecuzione",
            "",
            "Se una candela di cascata attraversa nello stesso intervallo "
            "sia lo stop sia il prezzo di liquidazione, il Paper usa il "
            "caso peggiore e registra una liquidazione intrabar. Gli stop "
            "in gap o in regime di stress ricevono slippage aggiuntivo.",
            "",
            "## Requisiti prima del live futures",
            "",
            "- modalità ISOLATED obbligatoria;",
            "- stop nativo sull'exchange;",
            "- conferma dello stop prima di accettare la posizione;",
            "- cross margin vietato.",
            "",
        ]
    )
    text = "\n".join(lines)
    atomic_write_text(REPORT_PATH, text)
    return text


def run_crash_guard_cycle(
    paper_state: dict[str, Any],
    signals: list[Any],
    bundle: dict[str, Any],
    core_config: dict[str, Any],
    when: datetime | None = None,
) -> dict[str, Any]:
    current = when or now_utc()
    config = load_config()
    if not truthy(config.get("enabled", True)):
        return {
            "enabled": False,
            "status": "DISABLED",
            "allowed_signals": list(signals),
            "blocked_signal_objects": [],
            "context": {
                "level": "NORMAL",
                "direction": "NONE",
                "risk_model_version": RISK_MODEL_VERSION,
            },
            "report_markdown": "",
        }

    state = load_state()
    completed = update_shadow_simulations(
        state,
        bundle,
        config,
        current,
    )
    context = market_context(
        bundle,
        config,
        state,
        current,
    )
    bundle["_crash_guard_config"] = config
    bundle["_crash_guard_context"] = context
    allowed, decisions = filter_signals(
        signals,
        paper_state,
        bundle,
        config,
        state,
        context,
        current,
    )

    blocked_ids = {
        str(row.get("signal_id", ""))
        for row in decisions
        if row.get("decision") == "BLOCKED"
    }
    blocked_objects = [
        signal
        for signal in signals
        if str(signal_dict(signal).get("signal_id", ""))
        in blocked_ids
    ]

    previous_level = str(
        state.get("previous_level", "NORMAL")
    )
    if previous_level != context["level"]:
        append_csv(
            EVENTS_PATH,
            EVENT_FIELDS,
            [
                {
                    "generated_utc": iso_utc(current),
                    "event_type": "LEVEL_CHANGE",
                    "previous_level": previous_level,
                    "current_level": context["level"],
                    "direction": context["direction"],
                    "cooldown_until_utc": context.get(
                        "cooldown_until_utc",
                        "",
                    ),
                    "blocked_signals": len(blocked_ids),
                    "details_json": json.dumps(
                        {
                            "down_breadth_fraction": context.get(
                                "down_breadth_fraction"
                            ),
                            "up_breadth_fraction": context.get(
                                "up_breadth_fraction"
                            ),
                            "median_15m_return_pct": context.get(
                                "median_15m_return_pct"
                            ),
                        },
                        separators=(",", ":"),
                    ),
                }
            ],
        )

    state["previous_level"] = context["level"]
    state["previous_direction"] = context["direction"]
    state["updated_utc"] = iso_utc(current)

    stress = stress_matrix(
        paper_state,
        bundle,
        config,
        current,
    )
    markdown = report_markdown(
        context,
        decisions,
        completed,
        state,
        stress,
        current,
    )
    atomic_write_json(STATE_PATH, state)

    return {
        "enabled": True,
        "status": "OK",
        "risk_model_version": RISK_MODEL_VERSION,
        "level": context["level"],
        "direction": context["direction"],
        "allowed_signals": allowed,
        "blocked_signal_objects": blocked_objects,
        "blocked_signals": len(blocked_ids),
        "decisions": decisions,
        "active_simulations": len(
            state.get("active_simulations", {})
        ),
        "completed_simulations": len(completed),
        "avoided_liquidations_total": int(
            state.get("totals", {}).get(
                "avoided_liquidations",
                0,
            )
        ),
        "normal_market_passthrough": True,
        "context": context,
        "stress_test": stress,
        "report_markdown": markdown,
        "paper_positions_modified": False,
        "paper_exits_modified_by_filter": False,
        "live_modified": False,
        "orders_sent": False,
    }


def severity_from_candle(
    candle: pd.Series,
    context: dict[str, Any],
    asset: str,
    config: dict[str, Any],
) -> str:
    level = str(
        context.get("asset_context", {})
        .get(asset, {})
        .get("level", context.get("level", "NORMAL"))
    )
    opened = max(finite(candle.get("open")), 1e-12)
    candle_range = (
        finite(candle.get("high"), opened)
        - finite(candle.get("low"), opened)
    ) / opened * 100.0
    thresholds = config["thresholds"]
    if candle_range >= finite(
        thresholds["extreme_15m_range_pct"]
    ):
        return "EXTREME"
    if candle_range >= finite(
        thresholds["crash_15m_range_pct"]
    ):
        return level_max(level, "CRASH")
    if candle_range >= finite(
        thresholds["stress_15m_range_pct"]
    ):
        return level_max(level, "STRESS")
    return level


def stressed_stop_fill(
    stop: float,
    adverse_extreme: float,
    side: str,
    level: str,
    config: dict[str, Any],
    *,
    gap: bool = False,
) -> tuple[float, float]:
    execution = config["execution_model"]
    bps_name = {
        "NORMAL": "normal_extra_slippage_bps",
        "WATCH": "watch_extra_slippage_bps",
        "STRESS": "stress_extra_slippage_bps",
        "RECOVERY": "recovery_extra_slippage_bps",
        "CRASH": "crash_extra_slippage_bps",
        "EXTREME": "extreme_extra_slippage_bps",
        "DATA_GUARD": "crash_extra_slippage_bps",
    }.get(level, "normal_extra_slippage_bps")
    base = finite(execution[bps_name]) / 10_000.0
    if gap:
        base += finite(
            execution["gap_extra_slippage_bps"]
        ) / 10_000.0

    penetration = (
        max(0.0, (stop - adverse_extreme) / stop)
        if side == "LONG"
        else max(0.0, (adverse_extreme - stop) / stop)
    )
    extra = min(
        finite(execution["maximum_stop_slippage_pct"]),
        base
        + penetration
        * finite(
            execution["penetration_capture_fraction"]
        ),
    )
    fill = (
        stop * (1.0 - extra)
        if side == "LONG"
        else stop * (1.0 + extra)
    )
    return fill, extra * 100.0


def resolve_protective_exit(
    position: dict[str, Any],
    candle: pd.Series,
    stop: float,
    target: float,
    liquidation: float | None,
    bundle: dict[str, Any],
    core_config: dict[str, Any],
) -> dict[str, Any]:
    config = bundle.get("_crash_guard_config")
    if not isinstance(config, dict):
        config = load_config()
    context_is_explicit = "_crash_guard_context" in bundle
    context = bundle.get(
        "_crash_guard_context",
        {
            "level": "NORMAL",
            "direction": "NONE",
            "asset_context": {},
        },
    )
    asset = str(position.get("asset", ""))
    side = str(position.get("side", "")).upper()
    level = (
        severity_from_candle(
            candle,
            context,
            asset,
            config,
        )
        if context_is_explicit
        else "NORMAL"
    )
    opened = finite(candle.get("open"))
    high = finite(candle.get("high"))
    low = finite(candle.get("low"))

    if side == "LONG":
        liquidation_gap = (
            liquidation is not None and opened <= liquidation
        )
        stop_gap = opened <= stop
        stop_hit = low <= stop
        target_hit = high >= target
        liquidation_crossed = (
            liquidation is not None and low <= liquidation
        )
        adverse_extreme = low
    else:
        liquidation_gap = (
            liquidation is not None and opened >= liquidation
        )
        stop_gap = opened >= stop
        stop_hit = high >= stop
        target_hit = low <= target
        liquidation_crossed = (
            liquidation is not None and high >= liquidation
        )
        adverse_extreme = high

    result = {
        "exit_price": None,
        "reason": "",
        "pre_slipped": False,
        "risk_model_version_at_exit": RISK_MODEL_VERSION,
        "crash_guard_level_at_exit": str(
            context.get("level", "NORMAL")
        ),
        "asset_stress_level_at_exit": level,
        "stop_slippage_pct": 0.0,
        "liquidation_crossed_intrabar": bool(
            liquidation_crossed
        ),
        "protective_execution_model": (
            "PAPER_STOP_MARKET_STRESSED_V1"
        ),
    }

    if liquidation_gap:
        result.update(
            {
                "exit_price": liquidation,
                "reason": "LIQUIDATION_GAP",
                "pre_slipped": True,
            }
        )
        return result

    if stop_gap and stop_hit:
        fill, slippage_pct = stressed_stop_fill(
            opened,
            adverse_extreme,
            side,
            level,
            config,
            gap=True,
        )
        if liquidation is not None and (
            (side == "LONG" and fill <= liquidation)
            or (side == "SHORT" and fill >= liquidation)
        ):
            result.update(
                {
                    "exit_price": liquidation,
                    "reason": "LIQUIDATION_STOP_GAP_STRESS",
                    "pre_slipped": True,
                    "stop_slippage_pct": slippage_pct,
                }
            )
        else:
            result.update(
                {
                    "exit_price": fill,
                    "reason": "STOP_GAP_STRESS",
                    "pre_slipped": True,
                    "stop_slippage_pct": slippage_pct,
                }
            )
        return result

    worst_case_policy = (
        config["execution_model"][
            "intrabar_liquidation_policy"
        ]
        == (
            "WORST_CASE_IF_STOP_AND_LIQUIDATION_"
            "CROSSED_IN_CRASH"
        )
    )
    if (
        stop_hit
        and liquidation_crossed
        and level in {"CRASH", "EXTREME"}
        and worst_case_policy
    ):
        result.update(
            {
                "exit_price": liquidation,
                "reason": (
                    "LIQUIDATION_INTRABAR_WORST_CASE"
                ),
                "pre_slipped": True,
            }
        )
        return result

    if stop_hit and target_hit:
        if (
            core_config["execution"].get(
                "same_candle_stop_target_policy"
            )
            == "TARGET_FIRST"
            and level not in {
                "STRESS",
                "RECOVERY",
                "CRASH",
                "EXTREME",
            }
        ):
            result.update(
                {
                    "exit_price": target,
                    "reason": "TARGET_SAME_CANDLE",
                }
            )
            return result
        stop_hit = True

    if stop_hit:
        if level in {
            "STRESS",
            "RECOVERY",
            "CRASH",
            "EXTREME",
        }:
            fill, slippage_pct = stressed_stop_fill(
                stop,
                adverse_extreme,
                side,
                level,
                config,
            )
            if liquidation is not None and (
                (side == "LONG" and fill <= liquidation)
                or (side == "SHORT" and fill >= liquidation)
            ):
                result.update(
                    {
                        "exit_price": liquidation,
                        "reason": (
                            "LIQUIDATION_STOP_STRESS"
                        ),
                        "pre_slipped": True,
                        "stop_slippage_pct": (
                            slippage_pct
                        ),
                    }
                )
            else:
                result.update(
                    {
                        "exit_price": fill,
                        "reason": "STOP_STRESS_SLIPPAGE",
                        "pre_slipped": True,
                        "stop_slippage_pct": (
                            slippage_pct
                        ),
                    }
                )
        else:
            result.update(
                {
                    "exit_price": stop,
                    "reason": (
                        "STOP_SAME_CANDLE_CONSERVATIVE"
                        if target_hit
                        else "STOP"
                    ),
                }
            )
        return result

    if target_hit:
        result.update(
            {
                "exit_price": target,
                "reason": "TARGET",
            }
        )
    return result
