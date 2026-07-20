# -*- coding: utf-8 -*-
"""Canonical MFE/MAE calculations for automatic paper trading.

The module keeps three concepts separate:
- signed capture: final net P/L divided by positive net MFE;
- winner capture: the same ratio, but only for profitable trades;
- giveback: the distance from positive net MFE to the final net result.

A losing trade after positive MFE may therefore have a negative signed capture
and a giveback above 100%, but it never receives a negative
``profit_retained_pct`` value.
"""

from __future__ import annotations

import math
from typing import Any

import pandas as pd


QUALITY_PRIORITY = {
    "": 0,
    "NO_OBSERVATIONS": 0,
    "MARK_ONLY": 1,
    "COMPLETED_15M_OHLC": 2,
    "EXIT_CAPPED_OHLC_CONSERVATIVE": 3,
    "LEGACY_MFE_MAE_AVAILABLE": 4,
    "LEGACY_UNAVAILABLE": 5,
}


def optional_float(value: Any) -> float | None:
    try:
        if value in (None, ""):
            return None
        number = float(value)
        return number if math.isfinite(number) else None
    except Exception:
        return None


def merge_quality(current: Any, incoming: str) -> str:
    current_text = str(current or "")
    if QUALITY_PRIORITY.get(incoming, 0) >= QUALITY_PRIORITY.get(current_text, 0):
        return incoming
    return current_text or incoming


def price_excursion_pct(entry: float, price: float, side: str) -> float:
    if entry <= 0:
        return 0.0
    direction = 1.0 if str(side).upper() == "LONG" else -1.0
    return (price - entry) / entry * direction * 100.0


def _net_pnl_at_price(
    position: dict[str, Any],
    price: float,
    taker_fee_bps: float,
) -> tuple[float, float]:
    entry = float(position["entry_price"])
    quantity = abs(float(position["quantity"]))
    rate = max(float(position.get("eur_usdt_rate", 1.0)), 1e-12)
    direction = 1.0 if position["side"] == "LONG" else -1.0
    gross = (price - entry) * quantity * direction / rate
    exit_fee = abs(price * quantity / rate) * taker_fee_bps / 10_000.0
    net = (
        gross
        - exit_fee
        - float(position.get("entry_fee_eur", 0.0))
        + float(position.get("funding_pnl_eur", 0.0))
    )
    return gross, net


def update_position_excursion(
    position: dict[str, Any],
    *,
    observed_high: float,
    observed_low: float,
    taker_fee_bps: float,
    observed_at: str,
    quality: str,
) -> None:
    """Update one position from an observed price interval.

    ``observed_high`` and ``observed_low`` may represent a complete candle or a
    conservative path capped at an intrabar exit. The function is side-aware.
    """
    entry = float(position["entry_price"])
    side = str(position["side"]).upper()
    favorable_price = observed_high if side == "LONG" else observed_low
    adverse_price = observed_low if side == "LONG" else observed_high

    old_favorable = float(position.get("max_favorable_price", entry))
    old_adverse = float(position.get("max_adverse_price", entry))

    if side == "LONG":
        new_favorable = max(old_favorable, favorable_price)
        new_adverse = min(old_adverse, adverse_price)
        favorable_changed = new_favorable > old_favorable
        adverse_changed = new_adverse < old_adverse
    else:
        new_favorable = min(old_favorable, favorable_price)
        new_adverse = max(old_adverse, adverse_price)
        favorable_changed = new_favorable < old_favorable
        adverse_changed = new_adverse > old_adverse

    favorable_gross, favorable_net = _net_pnl_at_price(
        position, new_favorable, taker_fee_bps
    )
    adverse_gross, adverse_net = _net_pnl_at_price(
        position, new_adverse, taker_fee_bps
    )

    previous_mfe = optional_float(position.get("mfe_net_eur"))
    previous_mae = optional_float(position.get("mae_net_eur"))

    position["max_favorable_price"] = new_favorable
    position["max_adverse_price"] = new_adverse
    position["mfe_gross_eur"] = max(
        optional_float(position.get("mfe_gross_eur")) or 0.0,
        favorable_gross,
    )
    position["mae_gross_eur"] = min(
        optional_float(position.get("mae_gross_eur")) or 0.0,
        adverse_gross,
    )
    position["mfe_net_eur"] = max(
        previous_mfe
        if previous_mfe is not None
        else -float(position.get("entry_fee_eur", 0.0)),
        favorable_net,
    )
    position["mae_net_eur"] = min(
        previous_mae
        if previous_mae is not None
        else -float(position.get("entry_fee_eur", 0.0)),
        adverse_net,
    )
    position["mfe_pct"] = price_excursion_pct(entry, new_favorable, side)
    position["mae_pct"] = price_excursion_pct(entry, new_adverse, side)

    if favorable_changed or previous_mfe is None or favorable_net > previous_mfe:
        position["mfe_at_utc"] = observed_at
    if adverse_changed or previous_mae is None or adverse_net < previous_mae:
        position["mae_at_utc"] = observed_at

    position["excursion_observation_count"] = int(
        position.get("excursion_observation_count", 0) or 0
    ) + 1
    position["excursion_quality"] = merge_quality(
        position.get("excursion_quality"), quality
    )


def update_position_excursion_at_price(
    position: dict[str, Any],
    *,
    price: float,
    taker_fee_bps: float,
    observed_at: str,
    quality: str = "MARK_ONLY",
) -> None:
    update_position_excursion(
        position,
        observed_high=price,
        observed_low=price,
        taker_fee_bps=taker_fee_bps,
        observed_at=observed_at,
        quality=quality,
    )


def conservative_exit_interval(
    candle_open: float,
    exit_price: float,
) -> tuple[float, float]:
    """Return a monotonic, chronology-safe interval from open to first exit."""
    return max(candle_open, exit_price), min(candle_open, exit_price)


def close_excursion_metrics(
    net_pnl_eur: float,
    mfe_net_eur: float,
) -> dict[str, Any]:
    """Return non-overlapping exit-efficiency metrics.

    ``profit_retained_pct`` remains as a backwards-compatible winner-only
    percentage. It is blank for losing/breakeven trades.
    """
    if mfe_net_eur <= 0:
        return {
            "capture_ratio_signed": None,
            "winner_capture_ratio": None,
            "profit_retained_pct": None,
            "peak_profit_giveback_eur": 0.0,
            "profit_giveback_pct_of_mfe": None,
            "lost_after_positive_mfe": False,
        }

    signed_capture = net_pnl_eur / mfe_net_eur
    winner_capture = signed_capture if net_pnl_eur > 0 else None
    giveback = max(mfe_net_eur - net_pnl_eur, 0.0)
    return {
        "capture_ratio_signed": signed_capture,
        "winner_capture_ratio": winner_capture,
        "profit_retained_pct": (
            winner_capture * 100.0 if winner_capture is not None else None
        ),
        "peak_profit_giveback_eur": giveback,
        "profit_giveback_pct_of_mfe": giveback / mfe_net_eur * 100.0,
        "lost_after_positive_mfe": net_pnl_eur < 0,
    }


def backfill_trade_excursion_fields(record: dict[str, Any]) -> tuple[dict[str, Any], bool]:
    """Safely enrich a historical row only from values already stored in it."""
    enriched = dict(record)
    before = dict(enriched)

    entry = optional_float(enriched.get("entry_price"))
    favorable = optional_float(enriched.get("max_favorable_price"))
    adverse = optional_float(enriched.get("max_adverse_price"))
    side = str(enriched.get("side", "")).upper()
    mfe = optional_float(enriched.get("mfe_net_eur"))
    mae = optional_float(enriched.get("mae_net_eur"))
    net = optional_float(enriched.get("net_pnl_eur"))

    if entry and favorable is not None and side in {"LONG", "SHORT"}:
        enriched["mfe_pct"] = price_excursion_pct(entry, favorable, side)
    if entry and adverse is not None and side in {"LONG", "SHORT"}:
        enriched["mae_pct"] = price_excursion_pct(entry, adverse, side)

    if mfe is not None and mae is not None:
        if net is not None:
            derived = close_excursion_metrics(net, mfe)
            enriched.update(
                {key: ("" if value is None else value) for key, value in derived.items()}
            )
        if not str(enriched.get("excursion_quality", "")).strip():
            enriched["excursion_quality"] = "LEGACY_MFE_MAE_AVAILABLE"
    elif not str(enriched.get("excursion_quality", "")).strip():
        enriched["excursion_quality"] = "LEGACY_UNAVAILABLE"

    changed = any(
        str(before.get(key, "")) != str(value)
        for key, value in enriched.items()
    )
    return enriched, changed


def _numeric(frame: pd.DataFrame, field: str) -> pd.Series:
    if field not in frame.columns:
        return pd.Series(index=frame.index, dtype=float)
    return pd.to_numeric(frame[field], errors="coerce")


def summarize_excursion_frame(frame: pd.DataFrame) -> dict[str, Any]:
    """Aggregate comparable per-trade MFE/MAE observations for reports."""
    if frame.empty:
        return {
            "average_mfe_net_eur": 0.0,
            "average_mae_net_eur": 0.0,
            "excursion_sample": 0,
            "average_signed_capture_pct": 0.0,
            "signed_capture_sample": 0,
            "average_winner_capture_pct": 0.0,
            "winner_capture_sample": 0,
            "average_profit_giveback_eur": 0.0,
            "average_profit_giveback_pct_of_mfe": 0.0,
            "giveback_sample": 0,
            "lost_after_positive_mfe_count": 0,
        }

    pnl = _numeric(frame, "net_pnl_eur")
    mfe = _numeric(frame, "mfe_net_eur")
    mae = _numeric(frame, "mae_net_eur")
    valid_excursion = mfe.notna() & mae.notna()
    positive_mfe = mfe > 0

    signed = _numeric(frame, "capture_ratio_signed")
    derived_signed = pnl / mfe
    signed = signed.where(signed.notna(), derived_signed)
    signed_valid = positive_mfe & pnl.notna() & signed.notna()

    winner = _numeric(frame, "winner_capture_ratio")
    derived_winner = pnl / mfe
    winner = winner.where(winner.notna(), derived_winner)
    winner_valid = positive_mfe & (pnl > 0) & winner.notna()

    giveback = _numeric(frame, "peak_profit_giveback_eur")
    derived_giveback = (mfe - pnl).clip(lower=0.0)
    giveback = giveback.where(giveback.notna(), derived_giveback)
    giveback_pct = _numeric(frame, "profit_giveback_pct_of_mfe")
    derived_giveback_pct = giveback / mfe * 100.0
    giveback_pct = giveback_pct.where(giveback_pct.notna(), derived_giveback_pct)
    giveback_valid = positive_mfe & pnl.notna() & giveback.notna()

    lost_after_positive = positive_mfe & (pnl < 0)

    def mean_or_zero(series: pd.Series) -> float:
        cleaned = series.dropna()
        return float(cleaned.mean()) if not cleaned.empty else 0.0

    return {
        "average_mfe_net_eur": mean_or_zero(mfe[valid_excursion]),
        "average_mae_net_eur": mean_or_zero(mae[valid_excursion]),
        "excursion_sample": int(valid_excursion.sum()),
        "average_signed_capture_pct": mean_or_zero(signed[signed_valid]) * 100.0,
        "signed_capture_sample": int(signed_valid.sum()),
        "average_winner_capture_pct": mean_or_zero(winner[winner_valid]) * 100.0,
        "winner_capture_sample": int(winner_valid.sum()),
        "average_profit_giveback_eur": mean_or_zero(giveback[giveback_valid]),
        "average_profit_giveback_pct_of_mfe": mean_or_zero(
            giveback_pct[giveback_valid]
        ),
        "giveback_sample": int(giveback_valid.sum()),
        "lost_after_positive_mfe_count": int(lost_after_positive.sum()),
    }
