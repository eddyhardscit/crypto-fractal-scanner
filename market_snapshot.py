# -*- coding: utf-8 -*-
"""Create and read one shared BTC/SOL/DOGE market-price snapshot.

Run this script once near the beginning of the GitHub Actions workflow. Every
subsequent report can then read the same prices and candle dates instead of
making its own independent price request.

This version avoids the yfinance SQLite "database is locked" failure by:
- using a private cache directory for this process;
- disabling parallel yfinance downloads;
- retrying transient failures;
- retrying missing assets one by one.
"""

from __future__ import annotations

import json
import os
import tempfile
import time
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

DOWNLOAD_ATTEMPTS = 4
RETRY_BASE_SECONDS = 2


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

    if isinstance(out.columns, pd.MultiIndex):
        # Single-ticker downloads can still return a MultiIndex such as
        # ("Close", "BTC-USD"). Remove a level only when it contains one value.
        while isinstance(out.columns, pd.MultiIndex):
            removable_level = None
            for level in range(out.columns.nlevels):
                if len(pd.Index(out.columns.get_level_values(level)).unique()) == 1:
                    removable_level = level
                    break

            if removable_level is None:
                break

            out.columns = out.columns.droplevel(removable_level)

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
    for level in range(raw.columns.nlevels):
        values = raw.columns.get_level_values(level)
        if ticker in values:
            try:
                return _normalise_frame(raw.xs(ticker, axis=1, level=level))
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

    if record["price"] is None:
        return None

    return record


def build_snapshot_from_frames(
    frames: Mapping[str, pd.DataFrame],
    *,
    generated_at_utc: str | None = None,
    source: str = "Yahoo Finance",
) -> dict[str, Any]:
    assets: dict[str, dict[str, Any]] = {}

    for asset, ticker in TICKERS.items():
        # Preserve compatibility with callers that key frames either by ticker
        # ("BTC-USD") or by asset ("BTC").
        frame = frames.get(ticker)
        if frame is None:
            frame = frames.get(asset, pd.DataFrame())

        record = _asset_record(asset, ticker, frame)
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


def _atomic_write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    pd.DataFrame(rows).to_csv(
        tmp,
        index=False,
        encoding="utf-8",
        lineterminator="\n",
    )
    tmp.replace(path)


def write_snapshot(snapshot: Mapping[str, Any]) -> dict[str, Any]:
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    payload = dict(snapshot)
    _atomic_write_text(
        SNAPSHOT_JSON_PATH,
        json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=False) + "\n",
    )

    rows: list[dict[str, Any]] = []
    for asset, record in payload.get("assets", {}).items():
        rows.append(
            {
                "generated_at_utc": payload.get("generated_at_utc"),
                "source": payload.get("source"),
                "asset": asset,
                **record,
            }
        )

    _atomic_write_csv(SNAPSHOT_CSV_PATH, rows)
    return payload


def _configure_private_yfinance_cache() -> str:
    """Give this process its own yfinance SQLite cache directory.

    yfinance stores timezone/cookie data in SQLite. Parallel access can
    occasionally produce ``OperationalError: database is locked``. A private
    cache plus serial downloads prevents different workers from contending for
    the same database.
    """
    cache_dir = tempfile.mkdtemp(
        prefix=f"yfinance_snapshot_{os.getpid()}_",
    )

    setter = getattr(yf, "set_tz_cache_location", None)
    if callable(setter):
        try:
            setter(cache_dir)
            print(f"yfinance cache privato: {cache_dir}")
        except Exception as exc:
            print(f"Avviso: impossibile impostare cache yfinance privata: {exc}")

    return cache_dir


def _sleep_before_retry(attempt: int) -> None:
    seconds = RETRY_BASE_SECONDS * attempt
    print(f"Nuovo tentativo tra {seconds} secondi...")
    time.sleep(seconds)


def _download_batch_serial() -> pd.DataFrame:
    last_error: Exception | None = None

    for attempt in range(1, DOWNLOAD_ATTEMPTS + 1):
        try:
            raw = yf.download(
                list(TICKERS.values()),
                period="10d",
                interval="1d",
                auto_adjust=True,
                progress=False,
                group_by="ticker",
                threads=False,
                timeout=30,
            )

            if raw is not None and not raw.empty:
                return raw

            last_error = RuntimeError("download batch vuoto")
            print(f"Tentativo batch {attempt}/{DOWNLOAD_ATTEMPTS}: risultato vuoto.")
        except Exception as exc:
            last_error = exc
            print(
                f"Tentativo batch {attempt}/{DOWNLOAD_ATTEMPTS} fallito: "
                f"{type(exc).__name__}: {exc}"
            )

        if attempt < DOWNLOAD_ATTEMPTS:
            _sleep_before_retry(attempt)

    if last_error is not None:
        print(f"Download batch non riuscito: {type(last_error).__name__}: {last_error}")

    return pd.DataFrame()


def _download_single_ticker(ticker: str) -> pd.DataFrame:
    last_error: Exception | None = None

    for attempt in range(1, DOWNLOAD_ATTEMPTS + 1):
        try:
            raw = yf.download(
                ticker,
                period="10d",
                interval="1d",
                auto_adjust=True,
                progress=False,
                threads=False,
                timeout=30,
            )

            frame = _frame_for_ticker(raw, ticker)
            if not frame.empty and "Close" in frame.columns:
                return frame

            last_error = RuntimeError("download singolo vuoto o senza Close")
            print(
                f"{ticker}, tentativo {attempt}/{DOWNLOAD_ATTEMPTS}: "
                "risultato vuoto o senza Close."
            )
        except Exception as exc:
            last_error = exc
            print(
                f"{ticker}, tentativo {attempt}/{DOWNLOAD_ATTEMPTS} fallito: "
                f"{type(exc).__name__}: {exc}"
            )

        if attempt < DOWNLOAD_ATTEMPTS:
            _sleep_before_retry(attempt)

    if last_error is not None:
        print(
            f"{ticker}: download singolo non riuscito dopo "
            f"{DOWNLOAD_ATTEMPTS} tentativi: {type(last_error).__name__}: {last_error}"
        )

    return pd.DataFrame()


def download_market_snapshot() -> dict[str, Any]:
    _configure_private_yfinance_cache()

    frames: dict[str, pd.DataFrame] = {}

    # First try one serial batch request.
    raw = _download_batch_serial()
    if raw is not None and not raw.empty:
        for ticker in TICKERS.values():
            frame = _frame_for_ticker(raw, ticker)
            if not frame.empty:
                frames[ticker] = frame

    # Retry only missing assets one by one. This is the important fallback for
    # partial batch responses such as "DOGE missing".
    missing_tickers = [
        ticker
        for ticker in TICKERS.values()
        if ticker not in frames or frames[ticker].empty
    ]

    for ticker in missing_tickers:
        print(f"Fallback download singolo per {ticker}")
        frame = _download_single_ticker(ticker)
        if not frame.empty:
            frames[ticker] = frame

    snapshot = build_snapshot_from_frames(
        frames,
        source="Yahoo Finance daily shared snapshot",
    )

    missing_assets = sorted(set(TICKERS) - set(snapshot["assets"]))
    if missing_assets:
        raise RuntimeError(
            "Snapshot incompleto dopo batch seriale e fallback singoli. "
            f"Asset mancanti: {', '.join(missing_assets)}"
        )

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
