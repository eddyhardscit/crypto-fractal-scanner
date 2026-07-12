# -*- coding: utf-8 -*-
"""Public KuCoin market-data adapter used by the paper trader.

No API key is required. The module deliberately separates data collection from
trading logic and supports an offline JSON fixture for deterministic tests.
"""

from __future__ import annotations

import json
import math
import os
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

FUTURES_BASE = os.getenv("KUCOIN_FUTURES_BASE_URL", "https://api-futures.kucoin.com")
SPOT_BASE = os.getenv("KUCOIN_SPOT_BASE_URL", "https://api.kucoin.com")
CACHE_PATH = Path("reports/paper_trading_market_cache.json")

ASSET_ALIASES = {
    "XBT": "BTC",
}
SYMBOL_OVERRIDES = {
    "BTC": "XBTUSDTM",
}


@dataclass(frozen=True)
class Contract:
    asset: str
    symbol: str
    turnover_24h: float
    volume_24h: float
    mark_price: float
    multiplier: float
    funding_rate: float
    status: str


class MarketDataError(RuntimeError):
    pass


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def iso_utc(value: datetime | None = None) -> str:
    return (value or utc_now()).isoformat(timespec="seconds")


def safe_float(value: Any, default: float = math.nan) -> float:
    try:
        if value is None or value == "":
            return default
        number = float(value)
        return number if math.isfinite(number) else default
    except Exception:
        return default


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
    session.headers.update({"User-Agent": "crypto-fractal-scanner-paper-trading/1.0"})
    return session


def get_json(session: requests.Session, base: str, path: str, params: dict[str, Any] | None = None) -> Any:
    response = session.get(base + path, params=params or {}, timeout=20)
    response.raise_for_status()
    payload = response.json()
    if isinstance(payload, dict) and payload.get("code") not in (None, "200000"):
        raise MarketDataError(f"KuCoin {path}: code={payload.get('code')} msg={payload.get('msg')}")
    return payload.get("data") if isinstance(payload, dict) and "data" in payload else payload


def asset_from_symbol(symbol: str) -> str:
    raw = str(symbol).upper().strip()
    if raw.endswith("USDTM"):
        raw = raw[:-5]
    elif raw.endswith("USDM"):
        raw = raw[:-4]
    raw = ASSET_ALIASES.get(raw, raw)
    return raw


def parse_contract(row: dict[str, Any]) -> Contract | None:
    symbol = str(row.get("symbol", "")).upper().strip()
    if not symbol or not symbol.endswith("USDTM"):
        return None
    asset = asset_from_symbol(symbol)
    mark = safe_float(row.get("markPrice"), safe_float(row.get("lastTradePrice")))
    if not asset or not math.isfinite(mark) or mark <= 0:
        return None
    return Contract(
        asset=asset,
        symbol=symbol,
        turnover_24h=max(0.0, safe_float(row.get("turnoverOf24h"), 0.0)),
        volume_24h=max(0.0, safe_float(row.get("volumeOf24h"), 0.0)),
        mark_price=mark,
        multiplier=max(0.0, safe_float(row.get("multiplier"), 1.0)),
        funding_rate=safe_float(row.get("fundingFeeRate"), safe_float(row.get("fundingRate"), 0.0)),
        status=str(row.get("status", row.get("marketStage", ""))),
    )


def fetch_active_contracts(session: requests.Session) -> list[Contract]:
    data = get_json(session, FUTURES_BASE, "/api/v1/contracts/active")
    rows = data if isinstance(data, list) else []
    contracts = [parsed for row in rows if isinstance(row, dict) if (parsed := parse_contract(row))]
    if not contracts:
        raise MarketDataError("Nessun contratto KuCoin futures attivo ricevuto.")
    return contracts


def select_universe(contracts: list[Contract], config: dict[str, Any]) -> list[Contract]:
    universe = config["universe"]
    excluded = {str(x).upper() for x in universe.get("excluded_assets", [])}
    minimum_turnover = float(universe.get("minimum_turnover_24h_usdt", 0.0))
    maximum = int(universe.get("max_assets", 12))
    mandatory = [str(x).upper() for x in universe.get("mandatory_assets", [])]

    by_asset: dict[str, Contract] = {}
    for contract in contracts:
        if contract.asset in excluded:
            continue
        if contract.status and contract.status.lower() in {"closed", "settled", "pause", "paused"}:
            continue
        previous = by_asset.get(contract.asset)
        if previous is None or contract.turnover_24h > previous.turnover_24h:
            by_asset[contract.asset] = contract

    liquid = sorted(
        (c for c in by_asset.values() if c.turnover_24h >= minimum_turnover),
        key=lambda c: c.turnover_24h,
        reverse=True,
    )
    selected: list[Contract] = []
    for asset in mandatory:
        contract = by_asset.get(asset)
        if contract and contract not in selected:
            selected.append(contract)
    for contract in liquid:
        if contract not in selected:
            selected.append(contract)
        if len(selected) >= maximum:
            break
    return selected[:maximum]


def _normalize_kline_rows(rows: Any) -> pd.DataFrame:
    if not isinstance(rows, list) or not rows:
        return pd.DataFrame(columns=["open", "high", "low", "close", "volume"])

    normalized: list[dict[str, Any]] = []
    for row in rows:
        if not isinstance(row, (list, tuple)) or len(row) < 6:
            continue
        timestamp = safe_float(row[0])
        if not math.isfinite(timestamp):
            continue
        # KuCoin has returned both seconds and milliseconds across endpoints.
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
                "volume": 0.0 if not math.isfinite(volume) else max(0.0, volume),
            }
        )

    if not normalized:
        return pd.DataFrame(columns=["open", "high", "low", "close", "volume"])
    frame = pd.DataFrame(normalized).drop_duplicates("time").set_index("time").sort_index()
    return frame[["open", "high", "low", "close", "volume"]]


def drop_incomplete_candle(frame: pd.DataFrame, timeframe_minutes: int, now: datetime | None = None) -> pd.DataFrame:
    if frame.empty:
        return frame
    current = pd.Timestamp(now or utc_now())
    if current.tzinfo is None:
        current = current.tz_localize("UTC")
    last = frame.index[-1]
    if last.tzinfo is None:
        last = last.tz_localize("UTC")
    close_time = last + pd.Timedelta(minutes=timeframe_minutes)
    if close_time > current - pd.Timedelta(seconds=20):
        return frame.iloc[:-1].copy()
    return frame


def fetch_klines(
    session: requests.Session,
    symbol: str,
    timeframe_minutes: int,
    limit: int = 420,
    now: datetime | None = None,
) -> pd.DataFrame:
    current = now or utc_now()

    # KuCoin Futures expects `from` and `to` in milliseconds.
    # Unix seconds can return an empty kline payload even when
    # contracts and mark prices are available.
    end = int(current.timestamp() * 1000)
    # Add a buffer for missing intervals and exchange-side truncation.
    start = end - int(
        timeframe_minutes
        * 60_000
        * max(limit + 80, 200)
    )
    data = get_json(
        session,
        FUTURES_BASE,
        "/api/v1/kline/query",
        {
            "symbol": symbol,
            "granularity": int(timeframe_minutes),
            "from": start,
            "to": end,
        },
    )
    frame = _normalize_kline_rows(data)

    # Defensive retry without a time window if KuCoin returns
    # an empty payload for the requested interval.
    if frame.empty:
        fallback_data = get_json(
            session,
            FUTURES_BASE,
            "/api/v1/kline/query",
            {
                "symbol": symbol,
                "granularity": int(timeframe_minutes),
            },
        )
        frame = _normalize_kline_rows(fallback_data)

    frame = drop_incomplete_candle(
        frame,
        timeframe_minutes,
        now=current,
    )
    if len(frame) > limit:
        frame = frame.tail(limit)
    return frame


def fetch_eur_usdt_rate(session: requests.Session, fallback: float) -> tuple[float, str]:
    env = os.getenv("EUR_USDT_RATE")
    if env:
        value = safe_float(env)
        if math.isfinite(value) and value > 0:
            return value, "ENV:EUR_USDT_RATE"
    try:
        data = get_json(session, SPOT_BASE, "/api/v1/market/orderbook/level1", {"symbol": "EUR-USDT"})
        price = safe_float(data.get("price") if isinstance(data, dict) else None)
        if math.isfinite(price) and price > 0:
            return price, "KUCOIN:EUR-USDT"
    except Exception:
        pass
    return float(fallback), "CONFIG_FALLBACK"


def frame_to_records(frame: pd.DataFrame) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for index, row in frame.iterrows():
        timestamp = pd.Timestamp(index)
        if timestamp.tzinfo is None:
            timestamp = timestamp.tz_localize("UTC")
        rows.append(
            {
                "time": timestamp.isoformat(),
                "open": float(row["open"]),
                "high": float(row["high"]),
                "low": float(row["low"]),
                "close": float(row["close"]),
                "volume": float(row.get("volume", 0.0)),
            }
        )
    return rows


def records_to_frame(rows: list[dict[str, Any]]) -> pd.DataFrame:
    if not rows:
        return pd.DataFrame(columns=["open", "high", "low", "close", "volume"])
    frame = pd.DataFrame(rows)
    frame["time"] = pd.to_datetime(frame["time"], utc=True, errors="coerce")
    frame = frame.dropna(subset=["time"]).set_index("time").sort_index()
    for column in ("open", "high", "low", "close", "volume"):
        frame[column] = pd.to_numeric(frame.get(column), errors="coerce")
    return frame.dropna(subset=["open", "high", "low", "close"])


def _load_fixture(path: Path) -> dict[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    payload["source"] = f"FIXTURE:{path.name}"
    return payload


def collect_market_bundle(config: dict[str, Any], now: datetime | None = None) -> dict[str, Any]:
    fixture = os.getenv("PAPER_TRADING_FIXTURE")
    if fixture:
        return _load_fixture(Path(fixture))

    session = make_session()
    contracts = fetch_active_contracts(session)
    selected = select_universe(contracts, config)
    if not selected:
        raise MarketDataError("La watchlist dinamica KuCoin è vuota.")

    rate, rate_source = fetch_eur_usdt_rate(session, config.get("eur_usdt_fallback_rate", 1.0))
    requested_timeframes = sorted({int(x) for x in config["universe"].get("timeframes_minutes", [15, 60, 240])})
    minimum_candles = int(config["universe"].get("minimum_candles", 120))
    assets: dict[str, Any] = {}
    failures: list[str] = []

    for contract in selected:
        candles: dict[str, Any] = {}
        for timeframe in requested_timeframes:
            try:
                frame = fetch_klines(session, contract.symbol, timeframe, now=now)
                if len(frame) < minimum_candles:
                    failures.append(f"{contract.asset} {timeframe}m: solo {len(frame)} candele")
                candles[str(timeframe)] = frame_to_records(frame)
            except Exception as exc:
                failures.append(f"{contract.asset} {timeframe}m: {exc}")
                candles[str(timeframe)] = []
            time.sleep(0.04)
        assets[contract.asset] = {
            "symbol": contract.symbol,
            "mark_price": contract.mark_price,
            "turnover_24h": contract.turnover_24h,
            "volume_24h": contract.volume_24h,
            "multiplier": contract.multiplier,
            "funding_rate": contract.funding_rate,
            "candles": candles,
        }

    bundle = {
        "schema_version": 1,
        "generated_utc": iso_utc(now),
        "source": "KUCOIN_PUBLIC_API",
        "eur_usdt_rate": rate,
        "eur_usdt_rate_source": rate_source,
        "assets": assets,
        "failures": failures,
    }
    CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
    CACHE_PATH.write_text(json.dumps(bundle, ensure_ascii=False), encoding="utf-8")
    return bundle


def bundle_frames(bundle: dict[str, Any]) -> dict[str, dict[int, pd.DataFrame]]:
    output: dict[str, dict[int, pd.DataFrame]] = {}
    for asset, payload in bundle.get("assets", {}).items():
        output[asset] = {}
        for timeframe, rows in payload.get("candles", {}).items():
            output[asset][int(timeframe)] = records_to_frame(rows)
    return output
