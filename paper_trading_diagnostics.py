# -*- coding: utf-8 -*-
# Explain why paper-trading signals did or did not enter.

from __future__ import annotations

import json
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

import pandas as pd

from kucoin_public_data import bundle_frames
from paper_signal_engine import (
    Signal,
    _read_latest_by_asset,
    compute_features,
    exchange_overlay_for_asset,
    global_overlay_for_asset,
    score_features,
    strategy_accepts,
    EXCHANGE_METRICS_PATH,
    GLOBAL_METRICS_PATH,
)
from paper_rsi_extreme_scalping import extreme_reversal_setup
from paper_trading_engine import (
    can_open,
    current_prices,
    portfolio_equity,
)

DIAGNOSTICS_PATH = Path(
    "reports/paper_trading_signal_diagnostics.json"
)


RSI_MTF_METRICS_PATH = Path(
    "reports/rsi_multitimeframe_divergence_metrics.csv"
)


def _load_rsi_multitimeframe_contexts() -> dict[str, dict[str, str]]:
    if not RSI_MTF_METRICS_PATH.exists():
        return {}
    try:
        frame = pd.read_csv(RSI_MTF_METRICS_PATH)
    except Exception:
        return {}

    output: dict[str, dict[str, str]] = {}
    for _, row in frame.iterrows():
        asset = str(row.get("asset", "")).strip()
        timeframe = str(row.get("timeframe", "")).strip()
        summary = str(row.get("summary_label", "n/a")).strip()
        state = str(row.get("lifecycle_state", "n/a")).strip()
        if not asset or not timeframe:
            continue
        output.setdefault(asset, {})[timeframe] = (
            f"{summary} [{state}]"
        )
    return output


def _rsi_multitimeframe_text(
    contexts: dict[str, dict[str, str]],
    asset: str,
) -> str:
    values = contexts.get(asset, {})
    daily = values.get("1D", "n/a")
    weekly = values.get("1W", "n/a")
    return f"D: {daily} | W: {weekly} | peso 0"


def _now(value: datetime | None = None) -> datetime:
    current = value or datetime.now(timezone.utc)
    if current.tzinfo is None:
        current = current.replace(tzinfo=timezone.utc)
    return current.astimezone(timezone.utc)


def _parse_time(value: Any) -> datetime | None:
    if value in (None, "", "n/a"):
        return None
    try:
        parsed = pd.Timestamp(value)
        if parsed.tzinfo is None:
            parsed = parsed.tz_localize("UTC")
        return parsed.to_pydatetime().astimezone(
            timezone.utc
        )
    except Exception:
        return None


def _age_minutes(
    value: Any,
    current: datetime,
) -> float | None:
    parsed = _parse_time(value)
    if parsed is None:
        return None
    return max(
        0.0,
        (current - parsed).total_seconds() / 60.0,
    )


# CANDLE_GRACE_BY_TIMEFRAME_V1
def _candle_grace_minutes(
    config: dict[str, Any],
    timeframe: int,
) -> float:
    execution = dict(config.get("execution", {}))
    mapping = execution.get(
        "candle_grace_minutes_by_timeframe",
        {},
    )
    value = None
    if isinstance(mapping, dict):
        value = mapping.get(str(timeframe))
        if value is None:
            value = mapping.get(timeframe)
    if value is None:
        value = execution.get("stale_data_minutes", 25)
    try:
        return max(0.0, float(value))
    except Exception:
        return 25.0


def annotate_market_freshness(
    bundle: dict[str, Any],
    config: dict[str, Any],
    current: datetime | None = None,
) -> dict[str, Any]:
    checked = _now(current)
    limit = float(
        config.get("execution", {}).get(
            "stale_data_minutes",
            25,
        )
    )
    generated = bundle.get("generated_utc")
    age = _age_minutes(generated, checked)
    source = str(bundle.get("source", "UNKNOWN"))
    fallback = "STALE_FALLBACK" in source.upper()
    stale = (
        fallback
        or age is None
        or age > limit
    )
    if fallback:
        status = "STALE_FALLBACK"
    elif age is None:
        status = "UNKNOWN"
    elif age > limit:
        status = "STALE"
    else:
        status = "FRESH"

    bundle["_paper_freshness"] = {
        "status": status,
        "source": source,
        "snapshot_generated_utc": str(
            generated or "n/a"
        ),
        "checked_utc": checked.isoformat(
            timespec="seconds"
        ),
        "snapshot_age_minutes": age,
        "stale_limit_minutes": limit,
        "fallback_used": fallback,
        "new_entries_allowed": not stale,
    }
    return bundle


def _strategy_reason(
    strategy: str,
    side: str,
    features: dict[str, Any],
) -> str:
    if strategy == "momentum_breakout":
        expected = "UP" if side == "LONG" else "DOWN"
        return (
            "Filtro momentum: serve breakout "
            f"{expected} oppure movimento breve ≥1,5%; "
            f"breakout={features.get('breakout_state', 'NONE')}, "
            f"movimento={features.get('ret_short_pct', 0.0):+.2f}%."
        )
    if strategy == "rsi_extreme_reversal":
        missing = str(
            features.get(
                "extreme_missing_text",
                "filtri di inversione non superati",
            )
        )
        return (
            "Filtro scalp RSI estremo: servono RSI estremo, "
            "shock, volume e conferma della candela successiva; "
            f"manca: {missing}. "
            f"RSI {features.get('extreme_candidate_rsi', 0.0):.1f}"
            f"→{features.get('extreme_confirmation_rsi', 0.0):.1f}; "
            f"volume x{features.get('extreme_volume_ratio', 0.0):.2f}; "
            f"shock {features.get('extreme_shock_atr', 0.0):.2f} ATR."
        )
    if strategy == "relative_strength":
        relative = (
            0.65
            * float(
                features.get(
                    "relative_medium_pct",
                    0.0,
                )
            )
            + 0.35
            * float(
                features.get(
                    "relative_long_pct",
                    0.0,
                )
            )
        )
        return (
            "Filtro forza relativa: serve almeno ±2,0% "
            f"contro BTC; valore={relative:+.2f}%."
        )
    return "Filtro specifico della strategia non superato."


def _timeframe_summary(
    frames: dict[str, dict[int, pd.DataFrame]],
    current: datetime,
    config: dict[str, Any],
) -> dict[str, Any]:
    requested = sorted(
        {
            int(value)
            for value in config.get(
                "universe",
                {},
            ).get(
                "timeframes_minutes",
                [15, 60, 240],
            )
        }
    )
    output: dict[str, Any] = {}
    for timeframe in requested:
        grace = _candle_grace_minutes(
            config,
            timeframe,
        )
        latest_values: list[datetime] = []
        for asset_frames in frames.values():
            frame = asset_frames.get(timeframe)
            if frame is None or frame.empty:
                continue
            parsed = _parse_time(frame.index[-1])
            if parsed is not None:
                latest_values.append(parsed)
        if not latest_values:
            output[str(timeframe)] = {
                "timeframe_minutes": timeframe,
                "assets_with_data": 0,
                "latest_closed_candle_utc": "n/a",
                "oldest_closed_candle_utc": "n/a",
                "max_candle_age_minutes": None,
                "max_close_delay_minutes": None,
                "allowed_age_minutes": timeframe + grace,
                "grace_minutes": grace,
                "status": "NO_DATA",
            }
            continue
        newest = max(latest_values)
        oldest = min(latest_values)
        max_age = max(
            0.0,
            (current - oldest).total_seconds()
            / 60.0,
        )
        close_delay = max(
            0.0,
            max_age - timeframe,
        )
        allowed_age = timeframe + grace
        output[str(timeframe)] = {
            "timeframe_minutes": timeframe,
            "assets_with_data": len(latest_values),
            "latest_closed_candle_utc": newest.isoformat(
                timespec="seconds"
            ),
            "oldest_closed_candle_utc": oldest.isoformat(
                timespec="seconds"
            ),
            "max_candle_age_minutes": max_age,
            "max_close_delay_minutes": close_delay,
            "allowed_age_minutes": allowed_age,
            "grace_minutes": grace,
            "status": (
                "OK"
                if max_age <= allowed_age
                else "STALE_CANDLE"
            ),
        }
    return output


def build_signal_diagnostics(
    bundle: dict[str, Any],
    config: dict[str, Any],
    signals: list[Signal],
    state: dict[str, Any],
    current: datetime | None = None,
) -> dict[str, Any]:
    checked = _now(current)
    if "_paper_freshness" not in bundle:
        annotate_market_freshness(
            bundle,
            config,
            checked,
        )
    freshness = dict(bundle["_paper_freshness"])
    frames = bundle_frames(bundle)
    freshness["timeframes"] = _timeframe_summary(
        frames,
        checked,
        config,
    )

    global_rows = _read_latest_by_asset(
        GLOBAL_METRICS_PATH
    )
    exchange_rows = _read_latest_by_asset(
        EXCHANGE_METRICS_PATH
    )
    rsi_multitimeframe_contexts = (
        _load_rsi_multitimeframe_contexts()
    )
    btc_frames = frames.get("BTC", {})
    prices = current_prices(bundle)
    eur_rate = float(
        bundle.get(
            "eur_usdt_rate",
            config.get("eur_usdt_fallback_rate", 1.0),
        )
    )
    raw_by_key = {
        (signal.portfolio, signal.asset): signal
        for signal in signals
    }
    allowed_ids: list[str] = []
    rows: list[dict[str, Any]] = []
    near_gap = float(
        config.get("notifications", {}).get(
            "near_miss_score_gap",
            1.5,
        )
    )

    for definition in config.get("portfolios", []):
        if not definition.get("enabled", True):
            continue
        portfolio_name = str(definition["name"])
        portfolio = state.get("portfolios", {}).get(
            portfolio_name,
            {},
        )
        timeframe = int(
            definition["timeframe_minutes"]
        )
        threshold = float(
            definition["minimum_abs_score"]
        )
        strategy = str(
            definition.get(
                "strategy",
                "confluence_trend",
            )
        )
        for asset in sorted(bundle.get("assets", {})):
            frame = frames.get(asset, {}).get(timeframe)
            base = {
                "portfolio": portfolio_name,
                "is_main": bool(
                    definition.get("is_main")
                ),
                "strategy": strategy,
                "asset": asset,
                "timeframe_minutes": timeframe,
                "minimum_abs_score": threshold,
                "rsi_multitimeframe_context": (
                    _rsi_multitimeframe_text(
                        rsi_multitimeframe_contexts,
                        asset,
                    )
                ),
            }
            if frame is None or len(frame) < 60:
                rows.append(
                    {
                        **base,
                        "side": "n/a",
                        "score": None,
                        "score_gap": None,
                        "confidence": "n/a",
                        "candle_time": "n/a",
                        "candle_age_minutes": None,
                        "breakout_state": "n/a",
                        "relative_strength_score": None,
                        "status": "NO_FEATURES",
                        "near_miss": False,
                        "reason": (
                            "Dati insufficienti: servono "
                            "almeno 60 candele utilizzabili."
                        ),
                        "signal_id": "",
                    }
                )
                continue

            btc_frame = btc_frames.get(timeframe)
            features = compute_features(
                frame,
                (
                    btc_frame
                    if asset != "BTC"
                    else frame
                ),
            )
            if not features:
                rows.append(
                    {
                        **base,
                        "side": "n/a",
                        "score": None,
                        "score_gap": None,
                        "confidence": "n/a",
                        "candle_time": "n/a",
                        "candle_age_minutes": None,
                        "breakout_state": "n/a",
                        "relative_strength_score": None,
                        "status": "NO_FEATURES",
                        "near_miss": False,
                        "reason": (
                            "Indicatori non calcolabili "
                            "dalle candele disponibili."
                        ),
                        "signal_id": "",
                    }
                )
                continue

            global_overlay, global_reason = (
                global_overlay_for_asset(
                    asset,
                    global_rows,
                )
            )
            exchange_overlay, exchange_reason = (
                exchange_overlay_for_asset(
                    asset,
                    exchange_rows,
                )
            )

            if strategy == "rsi_extreme_reversal":
                side = str(
                    definition.get(
                        "reversal_side",
                        "LONG",
                    )
                ).upper()
                extreme = extreme_reversal_setup(
                    frame,
                    side,
                    definition,
                )
                features.update(
                    {
                        "extreme_accepted": bool(
                            extreme.get("accepted")
                        ),
                        "extreme_missing_text": str(
                            extreme.get(
                                "missing_text",
                                "",
                            )
                        ),
                        "extreme_candidate_rsi": float(
                            extreme.get(
                                "candidate_rsi",
                                0.0,
                            )
                        ),
                        "extreme_confirmation_rsi": float(
                            extreme.get(
                                "confirmation_rsi",
                                0.0,
                            )
                        ),
                        "extreme_volume_ratio": float(
                            extreme.get(
                                "volume_ratio",
                                0.0,
                            )
                        ),
                        "extreme_shock_atr": float(
                            extreme.get(
                                "shock_atr",
                                0.0,
                            )
                        ),
                        "candle_time": str(
                            extreme.get(
                                "candle_time",
                                features.get(
                                    "candle_time",
                                    "n/a",
                                ),
                            )
                        ),
                        "breakout_state": str(
                            extreme.get(
                                "state",
                                "RSI_EXTREME_REVERSAL",
                            )
                        ),
                    }
                )
                score = float(
                    extreme.get("score", 0.0)
                )
                score_reasons = list(
                    extreme.get("reasons", [])
                )
            else:
                score, score_reasons = score_features(
                    features,
                    global_overlay,
                    exchange_overlay,
                )
                side = (
                    "LONG"
                    if score > 0
                    else "SHORT"
                )
            candle_time = str(
                features.get("candle_time", "n/a")
            )
            candle_age = _age_minutes(
                candle_time,
                checked,
            )
            candle_grace = _candle_grace_minutes(
                config,
                timeframe,
            )
            allowed_candle_age = timeframe + candle_grace
            close_delay = (
                max(0.0, candle_age - timeframe)
                if candle_age is not None
                else None
            )
            relative = (
                0.65
                * float(
                    features.get(
                        "relative_medium_pct",
                        0.0,
                    )
                )
                + 0.35
                * float(
                    features.get(
                        "relative_long_pct",
                        0.0,
                    )
                )
            )
            gap = max(
                0.0,
                threshold - abs(score),
            )
            signal = raw_by_key.get(
                (portfolio_name, asset)
            )
            signal_id = (
                signal.signal_id
                if signal is not None
                else ""
            )
            status = "READY"
            reason = (
                "Tutti i filtri del generatore "
                "sono stati superati."
            )

            if not freshness.get(
                "new_entries_allowed",
                False,
            ):
                status = "STALE_MARKET_DATA"
                reason = (
                    "Nuove entrate bloccate: snapshot "
                    "mercato vecchio o cache di fallback."
                )
            elif (
                candle_age is None
                or candle_age > allowed_candle_age
            ):
                status = "STALE_CANDLE"
                delay_text = (
                    f"{close_delay:.1f}"
                    if close_delay is not None
                    else "n/a"
                )
                reason = (
                    "Segnale arrivato troppo tardi: candela "
                    f"chiusa da {delay_text} minuti; tolleranza "
                    f"{candle_grace:.0f} minuti."
                )
            elif abs(score) < threshold:
                status = "BELOW_SCORE"
                reason = (
                    f"Punteggio {score:+.2f}; soglia "
                    f"±{threshold:.2f}; mancano "
                    f"{gap:.2f} punti."
                )
            elif (
                side == "LONG"
                and not definition.get(
                    "allow_long",
                    True,
                )
            ):
                status = "SIDE_DISABLED"
                reason = (
                    "Long disabilitati nel portafoglio."
                )
            elif (
                side == "SHORT"
                and not definition.get(
                    "allow_short",
                    True,
                )
            ):
                status = "SIDE_DISABLED"
                reason = (
                    "Short disabilitati nel portafoglio."
                )
            elif not strategy_accepts(
                strategy,
                side,
                features,
                score,
            ):
                status = "STRATEGY_FILTER"
                reason = _strategy_reason(
                    strategy,
                    side,
                    features,
                )
            elif signal is None:
                status = "NO_SIGNAL_OBJECT"
                reason = (
                    "Il punteggio sembra valido, ma il "
                    "generatore non ha prodotto il segnale."
                )
            elif signal_id in set(
                portfolio.get(
                    "seen_signal_ids",
                    [],
                )
            ):
                status = "ALREADY_PROCESSED"
                reason = (
                    "Questa stessa candela/segnale era "
                    "già stata elaborata."
                )
            else:
                equity, _ = portfolio_equity(
                    portfolio,
                    prices,
                    eur_rate,
                )
                permitted, gate_reason = can_open(
                    portfolio,
                    signal,
                    equity,
                    config,
                )
                if not permitted:
                    status = "RISK_GATE"
                    reason = (
                        "Filtro rischio/esecuzione: "
                        f"{gate_reason}."
                    )
                else:
                    allowed_ids.append(signal_id)

            near_miss = (
                (
                    status == "BELOW_SCORE"
                    and gap <= near_gap
                )
                or status
                in {
                    "STRATEGY_FILTER",
                    "RISK_GATE",
                    "READY",
                }
            )
            rows.append(
                {
                    **base,
                    "side": side,
                    "score": round(score, 4),
                    "score_gap": round(gap, 4),
                    "confidence": (
                        signal.confidence
                        if signal is not None
                        else "BASSA"
                    ),
                    "candle_time": candle_time,
                    "candle_age_minutes": (
                        round(candle_age, 2)
                        if candle_age is not None
                        else None
                    ),
                    "close_delay_minutes": (
                        round(close_delay, 2)
                        if close_delay is not None
                        else None
                    ),
                    "candle_grace_minutes": candle_grace,
                    "allowed_candle_age_minutes": (
                        allowed_candle_age
                    ),
                    "breakout_state": str(
                        features.get(
                            "breakout_state",
                            "NONE",
                        )
                    ),
                    "relative_strength_score": round(
                        relative,
                        4,
                    ),
                    "global_overlay": round(
                        global_overlay,
                        4,
                    ),
                    "exchange_overlay": round(
                        exchange_overlay,
                        4,
                    ),
                    "status": status,
                    "near_miss": near_miss,
                    "reason": reason,
                    "score_reasons": score_reasons,
                    "global_reason": global_reason,
                    "exchange_reason": exchange_reason,
                    "signal_id": signal_id,
                }
            )

    def sort_key(
        row: dict[str, Any],
    ) -> tuple[Any, ...]:
        status = str(row.get("status", ""))
        priority = {
            "READY": 0,
            "STRATEGY_FILTER": 1,
            "RISK_GATE": 2,
            "BELOW_SCORE": 3,
            "STALE_MARKET_DATA": 4,
            "STALE_CANDLE": 5,
            "ALREADY_PROCESSED": 6,
            "NO_SIGNAL_OBJECT": 7,
            "NO_FEATURES": 8,
        }.get(status, 9)
        gap_value = row.get("score_gap")
        gap_sort = (
            float(gap_value)
            if gap_value is not None
            else 999.0
        )
        return (
            0 if row.get("is_main") else 1,
            priority,
            gap_sort,
            -abs(float(row.get("score") or 0.0)),
            str(row.get("asset", "")),
        )

    maximum_rows = int(
        config.get("notifications", {}).get(
            "near_miss_max_rows",
            20,
        )
    )
    interesting = [
        row
        for row in rows
        if row.get("near_miss")
        or row.get("status")
        in {
            "STALE_MARKET_DATA",
            "STALE_CANDLE",
        }
    ]
    if not interesting:
        interesting = rows
    display_rows = sorted(
        interesting,
        key=sort_key,
    )[:maximum_rows]

    return {
        "schema_version": 1,
        "generated_utc": checked.isoformat(
            timespec="seconds"
        ),
        "market": freshness,
        "raw_signal_count": len(signals),
        "executable_signal_ids": sorted(
            set(allowed_ids)
        ),
        "executable_signal_count": len(
            set(allowed_ids)
        ),
        "rows": rows,
        "display_rows": display_rows,
        "summary": {
            "ready": sum(
                row["status"] == "READY"
                for row in rows
            ),
            "near_miss": sum(
                bool(row.get("near_miss"))
                for row in rows
            ),
            "below_score": sum(
                row["status"] == "BELOW_SCORE"
                for row in rows
            ),
            "strategy_filter": sum(
                row["status"]
                == "STRATEGY_FILTER"
                for row in rows
            ),
            "stale": sum(
                row["status"]
                in {
                    "STALE_MARKET_DATA",
                    "STALE_CANDLE",
                }
                for row in rows
            ),
        },
    }


def finalize_signal_diagnostics(
    payload: dict[str, Any],
    execution_summary: dict[str, Any],
) -> dict[str, Any]:
    opened_ids = {
        str(row.get("trade_id", ""))
        for row in execution_summary.get(
            "opened",
            [],
        )
    }
    for row in payload.get("rows", []):
        signal_id = str(row.get("signal_id", ""))
        if signal_id and signal_id in opened_ids:
            row["status"] = "OPENED"
            row["reason"] = (
                "Posizione virtuale aperta "
                "in questa esecuzione."
            )
            row["near_miss"] = True

    display_keys = {
        (
            row.get("portfolio"),
            row.get("asset"),
            row.get("signal_id"),
        )
        for row in payload.get("display_rows", [])
    }
    for row in payload.get("rows", []):
        key = (
            row.get("portfolio"),
            row.get("asset"),
            row.get("signal_id"),
        )
        if (
            row.get("status") == "OPENED"
            and key not in display_keys
        ):
            payload.setdefault(
                "display_rows",
                [],
            ).insert(0, row)

    payload["execution"] = {
        "opened": len(
            execution_summary.get("opened", [])
        ),
        "closed": len(
            execution_summary.get("closed", [])
        ),
    }
    payload.setdefault("summary", {})["opened"] = len(
        execution_summary.get("opened", [])
    )
    return payload


def write_signal_diagnostics(
    payload: dict[str, Any],
) -> None:
    DIAGNOSTICS_PATH.parent.mkdir(
        parents=True,
        exist_ok=True,
    )
    temp = DIAGNOSTICS_PATH.with_suffix(
        ".json.tmp"
    )
    temp.write_text(
        json.dumps(
            payload,
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    temp.replace(DIAGNOSTICS_PATH)
