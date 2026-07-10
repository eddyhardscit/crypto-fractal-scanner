# -*- coding: utf-8 -*-
"""Shared market snapshot utilities.

All downstream modules should use the same BTC/SOL/DOGE spot price created by
``market_snapshot.py``. Historical OHLC data still comes from each module's
normal data source, but the latest candle is aligned to the shared snapshot so
current-price comparisons, lifecycle checks and report values cannot drift
between modules during the same workflow run.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd


REPORTS_DIR = Path("reports")
SNAPSHOT_JSON_PATH = REPORTS_DIR / "latest_market_snapshot.json"
SNAPSHOT_CSV_PATH = REPORTS_DIR / "latest_market_snapshot.csv"

ASSET_BY_TICKER = {
    "BTC-USD": "BTC",
    "SOL-USD": "SOL",
    "DOGE-USD": "DOGE",
}
TICKER_BY_ASSET = {value: key for key, value in ASSET_BY_TICKER.items()}


def _safe_float(value: Any) -> float | None:
    try:
        number = float(value)
        if pd.isna(number) or np.isinf(number):
            return None
        return number
    except (TypeError, ValueError):
        return None


def normalize_asset(value: Any) -> str:
    text = str(value or "").strip().upper()
    if text in ASSET_BY_TICKER:
        return ASSET_BY_TICKER[text]
    if text.endswith("-USD"):
        text = text[:-4]
    return text


def _normalise_record(asset: str, record: dict[str, Any], meta: dict[str, Any]) -> dict[str, Any]:
    out = dict(record or {})
    out["asset"] = asset
    out["ticker"] = out.get("ticker") or TICKER_BY_ASSET.get(asset, f"{asset}-USD")
    out["price"] = _safe_float(out.get("price") or out.get("close"))
    out["close"] = _safe_float(out.get("close") or out.get("price"))
    out["open"] = _safe_float(out.get("open"))
    out["high"] = _safe_float(out.get("high"))
    out["low"] = _safe_float(out.get("low"))
    out["volume"] = _safe_float(out.get("volume"))
    out["candle_date_utc"] = str(out.get("candle_date_utc") or out.get("date") or "").strip()
    out["generated_at_utc"] = meta.get("generated_at_utc")
    out["source"] = meta.get("source") or "shared market snapshot"
    return out


def load_snapshot() -> dict[str, Any]:
    """Load the latest shared snapshot from JSON, with CSV fallback."""
    if SNAPSHOT_JSON_PATH.exists():
        try:
            payload = json.loads(SNAPSHOT_JSON_PATH.read_text(encoding="utf-8"))
            assets_raw = payload.get("assets", {})
            assets: dict[str, dict[str, Any]] = {}
            for key, record in assets_raw.items():
                asset = normalize_asset(key or (record or {}).get("asset"))
                if asset:
                    assets[asset] = _normalise_record(asset, record or {}, payload)
            return {
                "schema_version": payload.get("schema_version", 1),
                "generated_at_utc": payload.get("generated_at_utc"),
                "source": payload.get("source") or "shared market snapshot",
                "assets": assets,
            }
        except Exception:
            pass

    if SNAPSHOT_CSV_PATH.exists():
        try:
            with SNAPSHOT_CSV_PATH.open("r", encoding="utf-8", newline="") as handle:
                rows = list(csv.DictReader(handle))
            meta = {
                "generated_at_utc": rows[0].get("generated_at_utc") if rows else None,
                "source": rows[0].get("source") if rows else "shared market snapshot",
            }
            assets = {}
            for row in rows:
                asset = normalize_asset(row.get("asset") or row.get("ticker"))
                if asset:
                    assets[asset] = _normalise_record(asset, row, meta)
            return {
                "schema_version": 1,
                **meta,
                "assets": assets,
            }
        except Exception:
            pass

    return {
        "schema_version": 1,
        "generated_at_utc": None,
        "source": "snapshot unavailable",
        "assets": {},
    }


def snapshot_record(asset_or_ticker: Any) -> dict[str, Any]:
    asset = normalize_asset(asset_or_ticker)
    return dict(load_snapshot().get("assets", {}).get(asset, {}))


def snapshot_price(asset_or_ticker: Any, default: Any = None) -> float | Any:
    record = snapshot_record(asset_or_ticker)
    value = _safe_float(record.get("price") or record.get("close"))
    return default if value is None else value


def snapshot_date(asset_or_ticker: Any) -> pd.Timestamp | None:
    record = snapshot_record(asset_or_ticker)
    raw = record.get("candle_date_utc")
    if not raw:
        return None
    try:
        value = pd.Timestamp(raw)
        if value.tzinfo is not None:
            value = value.tz_convert("UTC").tz_localize(None)
        return value.normalize()
    except Exception:
        return None


def snapshot_source_label(asset_or_ticker: Any) -> str:
    record = snapshot_record(asset_or_ticker)
    generated = record.get("generated_at_utc") or "ora non disponibile"
    source = record.get("source") or "snapshot condiviso"
    return f"{source}; snapshot {generated}"


def _normalise_index(frame: pd.DataFrame) -> pd.DataFrame:
    out = frame.copy()
    out.index = pd.to_datetime(out.index, errors="coerce")
    out = out[~out.index.isna()]
    try:
        if out.index.tz is not None:
            out.index = out.index.tz_convert(None)
    except Exception:
        pass
    out.index = out.index.normalize()
    return out[~out.index.duplicated(keep="last")].sort_index()


def apply_snapshot_to_ohlcv(
    frame: pd.DataFrame,
    asset_or_ticker: Any,
    *,
    append_if_missing: bool = True,
) -> pd.DataFrame:
    """Align the latest daily candle to the shared snapshot.

    The function truncates candles later than the shared snapshot date, updates
    the matching candle close, and preserves OHLC validity by expanding high/low
    when needed. When the snapshot day is missing, it appends one synthetic
    daily candle with zero volume. This is preferable to allowing each module to
    use a slightly different intraday close.
    """
    if frame is None or frame.empty:
        return frame

    price = snapshot_price(asset_or_ticker, None)
    date = snapshot_date(asset_or_ticker)
    if price is None or date is None:
        return frame

    out = _normalise_index(frame)
    if out.empty:
        return out

    # Freeze every module to the exact same snapshot day.
    out = out[out.index <= date].copy()

    if date not in out.index:
        if not append_if_missing:
            return out
        row: dict[str, Any] = {}
        for column in out.columns:
            if column in {"Open", "High", "Low", "Close", "Adj Close"}:
                row[column] = price
            elif column == "Volume":
                row[column] = 0.0
            else:
                row[column] = np.nan
        out.loc[date] = row
        out = out.sort_index()
    else:
        if "Close" in out.columns:
            out.at[date, "Close"] = price
        if "Adj Close" in out.columns:
            out.at[date, "Adj Close"] = price
        if "Open" in out.columns and pd.isna(out.at[date, "Open"]):
            out.at[date, "Open"] = price
        if "High" in out.columns:
            current_high = _safe_float(out.at[date, "High"])
            out.at[date, "High"] = price if current_high is None else max(current_high, price)
        if "Low" in out.columns:
            current_low = _safe_float(out.at[date, "Low"])
            out.at[date, "Low"] = price if current_low is None else min(current_low, price)

    return out
