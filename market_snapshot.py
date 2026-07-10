# -*- coding: utf-8 -*-
"""Create and read one shared BTC/SOL/DOGE market-price snapshot.

Run this script once near the beginning of the GitHub Actions workflow. Every
subsequent report can then read the same prices and candle dates instead of
making its own independent price request.
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping

import pandas as pd
import yfinance as yf


REPORTS_DIR = Path("reports")
SNAPSHOT_JSON_PATH = REPORTS_DIR / "latest_market_snapshot.json"
SNAPSHOT_CSV_PATH = REPORTS_DIR / "latest_market_snapshot.csv"

TICKERS = {
    "BTC": "BTC-USD",
    "SOL": "SOL-USD",
    "DOGE": "DOGE-USD",
}


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def utc_iso(value: datetime | None = None) -> str:
    value = value or utc_now()
    return value.astimezone(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def safe_float(value: Any) -> float | None:
    try:
        value = float(value)
        if pd.isna(value):
            return None
        return value
    except (TypeError, ValueError):
        return None


def _date_iso(value: Any) -> str | None:
    try:
        ts = pd.Timestamp(value)
        if pd.isna(ts):
            return None
        if ts.tzinfo is not None:
            ts = ts.tz_convert("UTC").tz_localize(None)
        return ts.date().isoformat()
    except Exception:
        return None


def _normalise_frame(frame: pd.DataFrame) -> pd.DataFrame:
    if frame is None or frame.empty:
        return pd.DataFrame()

    out = frame.copy()
    out.index = pd.to_datetime(out.index, errors="coerce")
    out = out[~out.index.isna()].sort_index()
    out = out[~out.index.duplicated(keep="last")]

    if "Adj Close" in out.columns and "Close" not in out.columns:
        out["Close"] = out["Adj Close"]

    return out


def _frame_for_ticker(raw: pd.DataFrame, ticker: str) -> pd.DataFrame:
    if raw is None or raw.empty:
        return pd.DataFrame()

    if not isinstance(raw.columns, pd.MultiIndex):
        return _normalise_frame(raw)

    # yfinance can return either (ticker, field) or (field, ticker).
    level0 = raw.columns.get_level_values(0)
    level1 = raw.columns.get_level_values(-1)

    if ticker in level0:
        return _normalise_frame(raw[ticker])

    if ticker in level1:
        try:
            return _normalise_frame(raw.xs(ticker, axis=1, level=-1))
        except Exception:
            pass

    return pd.DataFrame()


def _asset_record(asset: str, ticker: str, frame: pd.DataFrame) -> dict[str, Any] | None:
    frame = _normalise_frame(frame)
    if frame.empty or "Close" not in frame.columns:
        return None

    valid = frame.dropna(subset=["Close"])
    if valid.empty:
        return None

    row = valid.iloc[-1]
    idx = valid.index[-1]

    record: dict[str, Any] = {
        "asset": asset,
        "ticker": ticker,
        "candle_date_utc": _date_iso(idx),
        "price": safe_float(row.get("Close")),
        "open": safe_float(row.get("Open")),
        "high": safe_float(row.get("High")),
        "low": safe_float(row.get("Low")),
        "close": safe_float(row.get("Close")),
        "volume": safe_float(row.get("Volume")),
    }
    return record


def build_snapshot_from_frames(
    frames: Mapping[str, pd.DataFrame],
    *,
    generated_at_utc: str | None = None,
    source: str = "Yahoo Finance",
) -> dict[str, Any]:
    assets: dict[str, dict[str, Any]] = {}

    for asset, ticker in TICKERS.items():
        record = _asset_record(asset, ticker, frames.get(ticker, pd.DataFrame()))
        if record is not None:
            assets[asset] = record

    return {
        "schema_version": 1,
        "generated_at_utc": generated_at_utc or utc_iso(),
        "source": source,
        "assets": assets,
    }


def _atomic_write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(text, encoding="utf-8", newline="\n")
    tmp.replace(path)


def write_snapshot(snapshot: Mapping[str, Any]) -> dict[str, Any]:
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    payload = dict(snapshot)
    _atomic_write_text(
        SNAPSHOT_JSON_PATH,
        json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=False) + "\n",
    )

    rows = []
    for asset, record in payload.get("assets", {}).items():
        rows.append({
            "generated_at_utc": payload.get("generated_at_utc"),
            "source": payload.get("source"),
            "asset": asset,
            **record,
        })

    pd.DataFrame(rows).to_csv(SNAPSHOT_CSV_PATH, index=False, encoding="utf-8", lineterminator="\n")
    return payload


def download_market_snapshot() -> dict[str, Any]:
    raw = yf.download(
        list(TICKERS.values()),
        period="10d",
        interval="1d",
        auto_adjust=True,
        progress=False,
        group_by="ticker",
        threads=True,
    )

    frames = {ticker: _frame_for_ticker(raw, ticker) for ticker in TICKERS.values()}
    snapshot = build_snapshot_from_frames(frames, source="Yahoo Finance daily shared snapshot")

    missing = sorted(set(TICKERS) - set(snapshot["assets"]))
    if missing:
        raise RuntimeError(f"Snapshot incompleto. Asset mancanti: {', '.join(missing)}")

    return write_snapshot(snapshot)


def write_snapshot_from_asset_data(
    asset_data: Mapping[str, pd.DataFrame],
    *,
    generated_at_utc: str | None = None,
) -> dict[str, Any]:
    snapshot = build_snapshot_from_frames(
        asset_data,
        generated_at_utc=generated_at_utc,
        source="Yahoo Finance scanner shared snapshot",
    )
    return write_snapshot(snapshot)


def load_market_snapshot(
    path: Path | str = SNAPSHOT_JSON_PATH,
    *,
    max_age_hours: float | None = None,
) -> dict[str, Any]:
    path = Path(path)
    if not path.exists():
        return {}

    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}

    if max_age_hours is not None:
        try:
            generated = pd.Timestamp(payload.get("generated_at_utc"))
            if generated.tzinfo is None:
                generated = generated.tz_localize("UTC")
            age_hours = (pd.Timestamp.now(tz="UTC") - generated).total_seconds() / 3600
            if age_hours > max_age_hours:
                return {}
        except Exception:
            return {}

    return payload


def get_snapshot_price(snapshot: Mapping[str, Any], asset_or_ticker: str) -> float | None:
    key = str(asset_or_ticker).upper().replace("-USD", "")
    record = snapshot.get("assets", {}).get(key, {})
    return safe_float(record.get("price"))


def get_snapshot_candle_date(snapshot: Mapping[str, Any], asset_or_ticker: str) -> str | None:
    key = str(asset_or_ticker).upper().replace("-USD", "")
    record = snapshot.get("assets", {}).get(key, {})
    value = record.get("candle_date_utc")
    return str(value) if value else None


def main() -> None:
    snapshot = download_market_snapshot()
    print(f"Creato {SNAPSHOT_JSON_PATH}")
    print(f"Creato {SNAPSHOT_CSV_PATH}")
    for asset, record in snapshot.get("assets", {}).items():
        print(f"{asset}: {record.get('price')} ({record.get('candle_date_utc')})")


if __name__ == "__main__":
    main()
