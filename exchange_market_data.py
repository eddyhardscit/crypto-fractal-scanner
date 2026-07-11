# -*- coding: utf-8 -*-
"""Collect public derivatives and market-microstructure data for BTC/SOL/DOGE.

Sources (no API key required):
- Binance USDⓈ-M futures REST: funding/mark/index, open interest, historical OI,
  global and top-trader long/short ratios, taker buy/sell volume and order book.
- Bybit V5 public REST: ticker/funding, open interest, long/short ratio,
  order book and recent public trades.
- KuCoin USDT-margined futures REST: contract/mark/index/open interest,
  historical OI, funding, order book and recent public trades.
- Optional short public WebSocket sample from Binance and Bybit liquidation streams.
  KuCoin does not expose an equivalent public all-liquidations feed in the APIs
  used here, so it is included for OI/funding/flow/book but not liquidation events.

The collector intentionally does not pretend that exchanges publish every trader's
liquidation price. It stores actual liquidations observed during a short sample and
separately stores order-book/liquidity and leverage-pressure proxies.
"""

from __future__ import annotations

import csv
import json
import math
import os
import socket
import ssl
import threading
import time
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Iterable

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


REPORTS_DIR = Path("reports")
SCHEMA_VERSION = "2.1.1"
SNAPSHOT_PATH = REPORTS_DIR / "exchange_market_data_snapshot.json"
HEALTH_PATH = REPORTS_DIR / "exchange_market_data_health.json"
RAW_PATH = REPORTS_DIR / "exchange_market_data_raw.json"
INTRADAY_HISTORY_PATH = REPORTS_DIR / "exchange_market_data_intraday.csv"
SHARED_SNAPSHOT_PATH = REPORTS_DIR / "shared_market_snapshot.json"

ASSETS = ("BTC", "SOL", "DOGE")
SYMBOLS = {asset: f"{asset}USDT" for asset in ASSETS}
SYMBOL_TO_ASSET = {symbol: asset for asset, symbol in SYMBOLS.items()}
KUCOIN_SYMBOLS = {"BTC": "XBTUSDTM", "SOL": "SOLUSDTM", "DOGE": "DOGEUSDTM"}

BINANCE_BASE = "https://fapi.binance.com"
BYBIT_BASE = "https://api.bybit.com"
KUCOIN_FUTURES_BASE = "https://api-futures.kucoin.com"
KUCOIN_UA_BASE = "https://api.kucoin.com"

HTTP_TIMEOUT = float(os.getenv("EXCHANGE_HTTP_TIMEOUT", "15"))
LIQ_SAMPLE_SECONDS = max(0, min(90, int(os.getenv("EXCHANGE_LIQ_SAMPLE_SECONDS", "20"))))
INTRADAY_RETENTION_DAYS = max(30, min(730, int(os.getenv("EXCHANGE_INTRADAY_RETENTION_DAYS", "180"))))
SKIP_WEBSOCKET = os.getenv("EXCHANGE_SKIP_WEBSOCKET", "0").strip().lower() in {
    "1",
    "true",
    "yes",
    "y",
}

EXCHANGE_NAMES = ("binance", "bybit", "kucoin")
_enabled_raw = os.getenv("EXCHANGE_ENABLED_EXCHANGES", ",".join(EXCHANGE_NAMES))
ENABLED_EXCHANGES = tuple(
    name for name in EXCHANGE_NAMES if name in {item.strip().lower() for item in _enabled_raw.split(",") if item.strip()}
)
COLLECTOR_MODE = os.getenv("EXCHANGE_COLLECTOR_MODE", "github-hosted").strip() or "github-hosted"

# Current order-book depth is ephemeral. These windows are deliberately small
# enough to describe executable nearby liquidity rather than remote limit orders.
BOOK_WINDOWS_PCT = (0.25, 0.50, 1.00, 2.00)


@dataclass
class FetchResult:
    ok: bool
    data: Any = None
    error: str = ""
    url: str = ""
    status_code: int | None = None


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def utc_date() -> str:
    return datetime.now(timezone.utc).date().isoformat()


def safe_float(value: Any, default: float | None = None) -> float | None:
    try:
        number = float(value)
        return number if math.isfinite(number) else default
    except (TypeError, ValueError):
        return default


def safe_int(value: Any, default: int = 0) -> int:
    number = safe_float(value)
    return int(number) if number is not None else default


def pct_change(new: Any, old: Any) -> float | None:
    new_f = safe_float(new)
    old_f = safe_float(old)
    if new_f is None or old_f in (None, 0):
        return None
    return (new_f / old_f - 1.0) * 100.0


def mean(values: Iterable[Any]) -> float | None:
    valid = [safe_float(value) for value in values]
    valid = [value for value in valid if value is not None]
    return sum(valid) / len(valid) if valid else None


def median(values: Iterable[Any]) -> float | None:
    valid = sorted(value for value in (safe_float(item) for item in values) if value is not None)
    if not valid:
        return None
    middle = len(valid) // 2
    if len(valid) % 2:
        return valid[middle]
    return (valid[middle - 1] + valid[middle]) / 2.0


def weighted_mean(pairs: Iterable[tuple[Any, Any]]) -> float | None:
    parsed: list[tuple[float, float]] = []
    for value, weight in pairs:
        value_f = safe_float(value)
        weight_f = safe_float(weight)
        if value_f is None or weight_f is None or weight_f <= 0:
            continue
        parsed.append((value_f, weight_f))
    if not parsed:
        return None
    total_weight = sum(weight for _, weight in parsed)
    return sum(value * weight for value, weight in parsed) / total_weight if total_weight > 0 else None


def weighted_ratio(buy: Any, sell: Any) -> float | None:
    buy_f = safe_float(buy)
    sell_f = safe_float(sell)
    if buy_f is None or sell_f is None or sell_f <= 0:
        return None
    return buy_f / sell_f


def atomic_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(payload, ensure_ascii=False, indent=2, default=str) + "\n", encoding="utf-8")
    tmp.replace(path)


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
        return payload if isinstance(payload, dict) else {}
    except Exception:
        return {}


def build_session() -> requests.Session:
    retry = Retry(
        total=3,
        connect=3,
        read=3,
        backoff_factor=0.6,
        status_forcelist=(429, 500, 502, 503, 504),
        allowed_methods=frozenset({"GET"}),
        raise_on_status=False,
    )
    adapter = HTTPAdapter(max_retries=retry, pool_connections=10, pool_maxsize=10)
    session = requests.Session()
    session.headers.update(
        {
            "User-Agent": "crypto-scanner-exchange-microstructure/2.1.1",
            "Accept": "application/json",
        }
    )
    session.mount("https://", adapter)
    return session


def get_json(session: requests.Session, base: str, path: str, params: dict[str, Any]) -> FetchResult:
    url = base.rstrip("/") + path
    try:
        response = session.get(url, params=params, timeout=HTTP_TIMEOUT)
        status = response.status_code
        if status != 200:
            return FetchResult(False, error=f"HTTP {status}: {response.text[:250]}", url=response.url, status_code=status)
        payload = response.json()
        return FetchResult(True, data=payload, url=response.url, status_code=status)
    except Exception as exc:
        return FetchResult(False, error=f"{type(exc).__name__}: {exc}", url=url)


def unwrap_bybit(result: FetchResult) -> FetchResult:
    if not result.ok:
        return result
    payload = result.data
    if not isinstance(payload, dict):
        return FetchResult(False, error="Bybit payload non-object", url=result.url, status_code=result.status_code)
    if safe_int(payload.get("retCode"), -1) != 0:
        return FetchResult(
            False,
            error=f"Bybit retCode={payload.get('retCode')}: {payload.get('retMsg')}",
            url=result.url,
            status_code=result.status_code,
        )
    return FetchResult(True, data=payload.get("result", {}), url=result.url, status_code=result.status_code)


def unwrap_kucoin(result: FetchResult) -> FetchResult:
    if not result.ok:
        return result
    payload = result.data
    if not isinstance(payload, dict):
        return FetchResult(False, error="KuCoin payload non-object", url=result.url, status_code=result.status_code)
    if str(payload.get("code", "")) != "200000":
        return FetchResult(
            False,
            error=f"KuCoin code={payload.get('code')}: {payload.get('msg') or payload.get('message')}",
            url=result.url,
            status_code=result.status_code,
        )
    return FetchResult(True, data=payload.get("data"), url=result.url, status_code=result.status_code)


def classify_fetch_result(result: FetchResult) -> str:
    if result.ok:
        return "OK"
    error = (result.error or "").lower()
    if result.status_code == 451:
        return "GEO_BLOCKED"
    if result.status_code == 403 and any(
        token in error
        for token in (
            "restricted location",
            "block access from your country",
            "blocked access from your country",
            "eligibility",
            "country",
        )
    ):
        return "GEO_BLOCKED"
    if result.status_code == 429:
        return "RATE_LIMITED"
    if result.status_code is not None:
        return "HTTP_ERROR"
    if "timeout" in error:
        return "TIMEOUT"
    return "ERROR"


def endpoint_record(result: FetchResult) -> dict[str, Any]:
    return {
        "ok": result.ok,
        "state": classify_fetch_result(result),
        "url": result.url,
        "status_code": result.status_code,
        "error": result.error,
    }


def skipped_endpoint_record(state: str, reason: str, url: str = "") -> dict[str, Any]:
    return {
        "ok": False,
        "state": state,
        "url": url,
        "status_code": None,
        "error": reason,
        "skipped": True,
    }


def unavailable_exchange_payload(asset: str, exchange: str, state: str, reason: str) -> dict[str, Any]:
    symbol = KUCOIN_SYMBOLS[asset] if exchange == "kucoin" else SYMBOLS[asset]
    return {
        "parsed": {
            "available": False,
            "asset": asset,
            "exchange": exchange,
            "symbol": symbol,
            "source_state": state,
            "source_error": reason,
            "orderbook": {},
        },
        "raw": {},
    }


def health_state(health: dict[str, Any]) -> str:
    states = [str(row.get("state", "")) for row in health.values() if isinstance(row, dict)]
    if "OK" in states:
        return "OK"
    for candidate in ("GEO_BLOCKED", "RATE_LIMITED", "TIMEOUT", "HTTP_ERROR", "ERROR", "DISABLED"):
        if candidate in states:
            return candidate
    return "MISSING"


def latest_list_value(rows: Any, key: str) -> float | None:
    if not isinstance(rows, list) or not rows:
        return None
    return safe_float(rows[-1].get(key)) if isinstance(rows[-1], dict) else None


def list_change(rows: Any, key: str, periods_back: int) -> float | None:
    if not isinstance(rows, list) or len(rows) < 2:
        return None
    latest_index = len(rows) - 1
    old_index = max(0, latest_index - periods_back)
    latest = rows[latest_index].get(key) if isinstance(rows[latest_index], dict) else None
    old = rows[old_index].get(key) if isinstance(rows[old_index], dict) else None
    return pct_change(latest, old)


def sum_rows(rows: Any, key: str, last_n: int | None = None) -> float | None:
    if not isinstance(rows, list):
        return None
    selected = rows[-last_n:] if last_n else rows
    values = [safe_float(row.get(key)) for row in selected if isinstance(row, dict)]
    values = [value for value in values if value is not None]
    return sum(values) if values else None


def orderbook_metrics(bids: Any, asks: Any, reference_price: Any, qty_multiplier: Any = 1.0) -> dict[str, Any]:
    ref = safe_float(reference_price)
    multiplier = safe_float(qty_multiplier, 1.0) or 1.0
    parsed_bids: list[tuple[float, float]] = []
    parsed_asks: list[tuple[float, float]] = []

    for side, target in ((bids, parsed_bids), (asks, parsed_asks)):
        if not isinstance(side, list):
            continue
        for row in side:
            if not isinstance(row, (list, tuple)) or len(row) < 2:
                continue
            price = safe_float(row[0])
            qty = safe_float(row[1])
            if price is None or qty is None or price <= 0 or qty < 0:
                continue
            target.append((price, qty * multiplier))

    best_bid = max((price for price, _ in parsed_bids), default=None)
    best_ask = min((price for price, _ in parsed_asks), default=None)
    mid = None
    if best_bid is not None and best_ask is not None:
        mid = (best_bid + best_ask) / 2.0
    elif ref is not None:
        mid = ref

    if ref is None:
        ref = mid

    spread_bps = None
    if best_bid is not None and best_ask is not None and mid:
        spread_bps = (best_ask - best_bid) / mid * 10000.0

    result: dict[str, Any] = {
        "best_bid": best_bid,
        "best_ask": best_ask,
        "mid_price": mid,
        "spread_bps": spread_bps,
        "levels_bid": len(parsed_bids),
        "levels_ask": len(parsed_asks),
    }

    def notional(levels: list[tuple[float, float]], predicate) -> float:
        return sum(price * qty for price, qty in levels if predicate(price))

    for window in BOOK_WINDOWS_PCT:
        if ref is None:
            bid_notional = ask_notional = 0.0
        else:
            lower = ref * (1.0 - window / 100.0)
            upper = ref * (1.0 + window / 100.0)
            bid_notional = notional(parsed_bids, lambda price, lo=lower, r=ref: lo <= price <= r)
            ask_notional = notional(parsed_asks, lambda price, hi=upper, r=ref: r <= price <= hi)
        total = bid_notional + ask_notional
        imbalance = (bid_notional - ask_notional) / total if total > 0 else None
        key = str(window).replace(".", "_")
        result[f"bid_notional_{key}pct"] = bid_notional
        result[f"ask_notional_{key}pct"] = ask_notional
        result[f"imbalance_{key}pct"] = imbalance

    def wall(levels: list[tuple[float, float]], side: str) -> dict[str, Any]:
        if ref is None:
            return {"price": None, "notional": None, "distance_pct": None, "multiple_median": None}
        if side == "bid":
            candidates = [(price, qty) for price, qty in levels if ref * 0.98 <= price <= ref]
        else:
            candidates = [(price, qty) for price, qty in levels if ref <= price <= ref * 1.02]
        if not candidates:
            return {"price": None, "notional": None, "distance_pct": None, "multiple_median": None}
        notionals = sorted(price * qty for price, qty in candidates)
        median = notionals[len(notionals) // 2]
        wall_price, wall_qty = max(candidates, key=lambda item: item[0] * item[1])
        wall_notional = wall_price * wall_qty
        distance = (wall_price / ref - 1.0) * 100.0
        return {
            "price": wall_price,
            "notional": wall_notional,
            "distance_pct": distance,
            "multiple_median": wall_notional / median if median > 0 else None,
        }

    result["largest_bid_wall"] = wall(parsed_bids, "bid")
    result["largest_ask_wall"] = wall(parsed_asks, "ask")
    return result


def bybit_list(result: FetchResult) -> list[dict[str, Any]]:
    if not result.ok or not isinstance(result.data, dict):
        return []
    rows = result.data.get("list", [])
    return rows if isinstance(rows, list) else []


def fetch_binance_asset(session: requests.Session, asset: str) -> tuple[dict[str, Any], dict[str, Any]]:
    symbol = SYMBOLS[asset]
    premium_probe = get_json(session, BINANCE_BASE, "/fapi/v1/premiumIndex", {"symbol": symbol})
    if classify_fetch_result(premium_probe) == "GEO_BLOCKED":
        reason = premium_probe.error or "Binance geoblocked"
        health = {"premium": endpoint_record(premium_probe)}
        for name in (
            "ticker_24h", "open_interest", "open_interest_hist", "global_long_short",
            "top_account_ratio", "top_position_ratio", "taker_ratio", "depth",
        ):
            health[name] = skipped_endpoint_record("GEO_BLOCKED", "Saltato dopo il primo blocco geografico Binance.")
        return unavailable_exchange_payload(asset, "binance", "GEO_BLOCKED", reason), health

    calls = {
        "premium": premium_probe,
        "ticker_24h": get_json(session, BINANCE_BASE, "/fapi/v1/ticker/24hr", {"symbol": symbol}),
        "open_interest": get_json(session, BINANCE_BASE, "/fapi/v1/openInterest", {"symbol": symbol}),
        "open_interest_hist": get_json(
            session,
            BINANCE_BASE,
            "/futures/data/openInterestHist",
            {"symbol": symbol, "period": "1h", "limit": 30},
        ),
        "global_long_short": get_json(
            session,
            BINANCE_BASE,
            "/futures/data/globalLongShortAccountRatio",
            {"symbol": symbol, "period": "1h", "limit": 30},
        ),
        "top_account_ratio": get_json(
            session,
            BINANCE_BASE,
            "/futures/data/topLongShortAccountRatio",
            {"symbol": symbol, "period": "1h", "limit": 30},
        ),
        "top_position_ratio": get_json(
            session,
            BINANCE_BASE,
            "/futures/data/topLongShortPositionRatio",
            {"symbol": symbol, "period": "1h", "limit": 30},
        ),
        "taker_ratio": get_json(
            session,
            BINANCE_BASE,
            "/futures/data/takerlongshortRatio",
            {"symbol": symbol, "period": "1h", "limit": 30},
        ),
        "depth": get_json(session, BINANCE_BASE, "/fapi/v1/depth", {"symbol": symbol, "limit": 500}),
    }

    premium = calls["premium"].data if calls["premium"].ok and isinstance(calls["premium"].data, dict) else {}
    ticker = calls["ticker_24h"].data if calls["ticker_24h"].ok and isinstance(calls["ticker_24h"].data, dict) else {}
    oi_now = calls["open_interest"].data if calls["open_interest"].ok and isinstance(calls["open_interest"].data, dict) else {}
    oi_hist = calls["open_interest_hist"].data if calls["open_interest_hist"].ok else []
    global_ls = calls["global_long_short"].data if calls["global_long_short"].ok else []
    top_account = calls["top_account_ratio"].data if calls["top_account_ratio"].ok else []
    top_position = calls["top_position_ratio"].data if calls["top_position_ratio"].ok else []
    taker = calls["taker_ratio"].data if calls["taker_ratio"].ok else []
    depth = calls["depth"].data if calls["depth"].ok and isinstance(calls["depth"].data, dict) else {}

    mark = safe_float(premium.get("markPrice"))
    index = safe_float(premium.get("indexPrice"))
    last_price = safe_float(ticker.get("lastPrice"), mark)
    oi_base = safe_float(oi_now.get("openInterest"))
    oi_usd = oi_base * (mark or last_price) if oi_base is not None and (mark or last_price) else None

    buy_4h = sum_rows(taker, "buyVol", 4)
    sell_4h = sum_rows(taker, "sellVol", 4)
    buy_24h = sum_rows(taker, "buyVol", 24)
    sell_24h = sum_rows(taker, "sellVol", 24)

    orderbook = orderbook_metrics(depth.get("bids", []), depth.get("asks", []), mark or last_price)

    parsed = {
        "available": any(result.ok for result in calls.values()),
        "symbol": symbol,
        "last_price": last_price,
        "mark_price": mark,
        "index_price": index,
        "basis_pct": ((mark / index - 1.0) * 100.0) if mark is not None and index not in (None, 0) else None,
        "funding_rate_pct": safe_float(premium.get("lastFundingRate"), 0.0) * 100.0 if premium else None,
        "next_funding_time": premium.get("nextFundingTime"),
        "price_change_24h_pct": safe_float(ticker.get("priceChangePercent")),
        "quote_volume_24h": safe_float(ticker.get("quoteVolume")),
        "open_interest_base": oi_base,
        "open_interest_usd": oi_usd,
        "oi_change_4h_pct": list_change(oi_hist, "sumOpenInterestValue", 4),
        "oi_change_24h_pct": list_change(oi_hist, "sumOpenInterestValue", 24),
        "global_long_short_ratio": latest_list_value(global_ls, "longShortRatio"),
        "top_account_long_short_ratio": latest_list_value(top_account, "longShortRatio"),
        "top_position_long_short_ratio": latest_list_value(top_position, "longShortRatio"),
        "taker_buy_sell_ratio_1h": latest_list_value(taker, "buySellRatio"),
        "taker_buy_sell_ratio_4h": weighted_ratio(buy_4h, sell_4h),
        "taker_buy_sell_ratio_24h": weighted_ratio(buy_24h, sell_24h),
        "taker_buy_volume_24h": buy_24h,
        "taker_sell_volume_24h": sell_24h,
        "orderbook": orderbook,
    }
    health = {name: endpoint_record(result) for name, result in calls.items()}
    raw = {name: result.data if result.ok else None for name, result in calls.items()}
    return {"parsed": parsed, "raw": raw}, health


def fetch_bybit_asset(session: requests.Session, asset: str) -> tuple[dict[str, Any], dict[str, Any]]:
    symbol = SYMBOLS[asset]
    ticker_probe = get_json(session, BYBIT_BASE, "/v5/market/tickers", {"category": "linear", "symbol": symbol})
    if classify_fetch_result(ticker_probe) == "GEO_BLOCKED":
        reason = ticker_probe.error or "Bybit geoblocked"
        health = {"ticker": endpoint_record(ticker_probe)}
        for name in ("open_interest_hist", "long_short", "depth", "recent_trades", "funding_history"):
            health[name] = skipped_endpoint_record("GEO_BLOCKED", "Saltato dopo il primo blocco geografico Bybit.")
        return unavailable_exchange_payload(asset, "bybit", "GEO_BLOCKED", reason), health

    raw_calls = {
        "ticker": ticker_probe,
        "open_interest_hist": get_json(
            session,
            BYBIT_BASE,
            "/v5/market/open-interest",
            {"category": "linear", "symbol": symbol, "intervalTime": "1h", "limit": 30},
        ),
        "long_short": get_json(
            session,
            BYBIT_BASE,
            "/v5/market/account-ratio",
            {"category": "linear", "symbol": symbol, "period": "1h", "limit": 30},
        ),
        "depth": get_json(
            session,
            BYBIT_BASE,
            "/v5/market/orderbook",
            {"category": "linear", "symbol": symbol, "limit": 200},
        ),
        "recent_trades": get_json(
            session,
            BYBIT_BASE,
            "/v5/market/recent-trade",
            {"category": "linear", "symbol": symbol, "limit": 1000},
        ),
        "funding_history": get_json(
            session,
            BYBIT_BASE,
            "/v5/market/funding/history",
            {"category": "linear", "symbol": symbol, "limit": 10},
        ),
    }
    calls = {name: unwrap_bybit(result) for name, result in raw_calls.items()}

    ticker_rows = bybit_list(calls["ticker"])
    ticker = ticker_rows[0] if ticker_rows else {}
    oi_rows = bybit_list(calls["open_interest_hist"])
    # Bybit returns newest first; sort oldest -> newest for changes.
    oi_rows = sorted(oi_rows, key=lambda row: safe_int(row.get("timestamp")))
    ls_rows = bybit_list(calls["long_short"])
    ls_rows = sorted(ls_rows, key=lambda row: safe_int(row.get("timestamp")))
    depth_result = calls["depth"].data if calls["depth"].ok and isinstance(calls["depth"].data, dict) else {}
    trade_rows = bybit_list(calls["recent_trades"])
    funding_rows = bybit_list(calls["funding_history"])

    last = safe_float(ticker.get("lastPrice"))
    mark = safe_float(ticker.get("markPrice"), last)
    index = safe_float(ticker.get("indexPrice"), last)
    oi_base = safe_float(ticker.get("openInterest"))
    oi_usd = oi_base * (mark or last) if oi_base is not None and (mark or last) else None

    buy_notional = 0.0
    sell_notional = 0.0
    for row in trade_rows:
        if not isinstance(row, dict):
            continue
        price = safe_float(row.get("price", row.get("p")))
        size = safe_float(row.get("size", row.get("v")))
        if price is None or size is None:
            continue
        notional = price * size
        side = str(row.get("side", row.get("S", ""))).lower()
        if side == "buy":
            buy_notional += notional
        elif side == "sell":
            sell_notional += notional

    orderbook = orderbook_metrics(depth_result.get("b", []), depth_result.get("a", []), mark or last)
    latest_ls = ls_rows[-1] if ls_rows else {}
    buy_ratio = safe_float(latest_ls.get("buyRatio"))
    sell_ratio = safe_float(latest_ls.get("sellRatio"))
    ls_ratio = (buy_ratio / sell_ratio) if buy_ratio is not None and sell_ratio not in (None, 0) else None

    funding_pct = safe_float(ticker.get("fundingRate"))
    if funding_pct is not None:
        funding_pct *= 100.0
    elif funding_rows:
        funding_pct = safe_float(funding_rows[0].get("fundingRate"))
        funding_pct = funding_pct * 100.0 if funding_pct is not None else None

    # OI rows expose openInterest; use amount change. For linear USDT contracts
    # this is still a useful relative series even if contract units differ.
    parsed = {
        "available": any(result.ok for result in calls.values()),
        "symbol": symbol,
        "last_price": last,
        "mark_price": mark,
        "index_price": index,
        "basis_pct": ((mark / index - 1.0) * 100.0) if mark is not None and index not in (None, 0) else None,
        "funding_rate_pct": funding_pct,
        "next_funding_time": ticker.get("nextFundingTime"),
        "price_change_24h_pct": safe_float(ticker.get("price24hPcnt")) * 100.0 if safe_float(ticker.get("price24hPcnt")) is not None else None,
        "turnover_24h": safe_float(ticker.get("turnover24h")),
        "open_interest_base": oi_base,
        "open_interest_usd": oi_usd,
        "oi_change_4h_pct": list_change(oi_rows, "openInterest", 4),
        "oi_change_24h_pct": list_change(oi_rows, "openInterest", 24),
        "global_long_short_ratio": ls_ratio,
        "taker_buy_sell_ratio_recent": weighted_ratio(buy_notional, sell_notional),
        "taker_buy_notional_recent": buy_notional,
        "taker_sell_notional_recent": sell_notional,
        "recent_trade_count": len(trade_rows),
        "orderbook": orderbook,
    }
    health = {name: endpoint_record(result) for name, result in calls.items()}
    raw = {name: result.data if result.ok else None for name, result in calls.items()}
    return {"parsed": parsed, "raw": raw}, health


def fetch_kucoin_asset(session: requests.Session, asset: str) -> tuple[dict[str, Any], dict[str, Any]]:
    symbol = KUCOIN_SYMBOLS[asset]
    raw_calls = {
        "contract": get_json(session, KUCOIN_FUTURES_BASE, f"/api/v1/contracts/{symbol}", {}),
        "ticker": get_json(session, KUCOIN_FUTURES_BASE, "/api/v1/ticker", {"symbol": symbol}),
        "depth": get_json(session, KUCOIN_FUTURES_BASE, "/api/v1/level2/snapshot", {"symbol": symbol}),
        "recent_trades": get_json(session, KUCOIN_FUTURES_BASE, "/api/v1/trade/history", {"symbol": symbol}),
        "funding_current": get_json(session, KUCOIN_FUTURES_BASE, f"/api/v1/funding-rate/{symbol}/current", {}),
        "open_interest_hist": get_json(
            session,
            KUCOIN_UA_BASE,
            "/api/ua/v1/market/open-interest",
            {"symbol": symbol, "interval": "1hour", "pageSize": 30},
        ),
    }
    calls = {name: unwrap_kucoin(result) for name, result in raw_calls.items()}

    contract = calls["contract"].data if calls["contract"].ok and isinstance(calls["contract"].data, dict) else {}
    ticker = calls["ticker"].data if calls["ticker"].ok and isinstance(calls["ticker"].data, dict) else {}
    depth = calls["depth"].data if calls["depth"].ok and isinstance(calls["depth"].data, dict) else {}
    trades = calls["recent_trades"].data if calls["recent_trades"].ok and isinstance(calls["recent_trades"].data, list) else []
    funding = calls["funding_current"].data if calls["funding_current"].ok and isinstance(calls["funding_current"].data, dict) else {}
    oi_rows = calls["open_interest_hist"].data if calls["open_interest_hist"].ok and isinstance(calls["open_interest_hist"].data, list) else []
    oi_rows = sorted(oi_rows, key=lambda row: safe_int(row.get("ts")) if isinstance(row, dict) else 0)

    multiplier = safe_float(contract.get("multiplier"), 1.0) or 1.0
    last = safe_float(ticker.get("price"), safe_float(contract.get("lastTradePrice")))
    mark = safe_float(contract.get("markPrice"), last)
    index = safe_float(contract.get("indexPrice"), last)
    open_interest_contracts = safe_float(contract.get("openInterest"))
    open_interest_base = open_interest_contracts * multiplier if open_interest_contracts is not None else None
    open_interest_usd = open_interest_base * (mark or last) if open_interest_base is not None and (mark or last) else None

    buy_notional = 0.0
    sell_notional = 0.0
    for row in trades:
        if not isinstance(row, dict):
            continue
        price = safe_float(row.get("price"))
        size_contracts = safe_float(row.get("size"))
        if price is None or size_contracts is None:
            continue
        notional = price * size_contracts * multiplier
        side = str(row.get("side", "")).lower()
        if side == "buy":
            buy_notional += notional
        elif side == "sell":
            sell_notional += notional

    current_funding = safe_float(funding.get("value"))
    if current_funding is None:
        current_funding = safe_float(contract.get("fundingFeeRate"))

    orderbook = orderbook_metrics(
        depth.get("bids", []),
        depth.get("asks", []),
        mark or last,
        qty_multiplier=multiplier,
    )

    parsed = {
        "available": any(result.ok for result in calls.values()),
        "symbol": symbol,
        "last_price": last,
        "mark_price": mark,
        "index_price": index,
        "basis_pct": ((mark / index - 1.0) * 100.0) if mark is not None and index not in (None, 0) else None,
        "funding_rate_pct": current_funding * 100.0 if current_funding is not None else None,
        "next_funding_time": funding.get("fundingTime") or contract.get("nextFundingRateDateTime"),
        "price_change_24h_pct": safe_float(contract.get("priceChgPct")) * 100.0 if safe_float(contract.get("priceChgPct")) is not None else None,
        "turnover_24h": safe_float(contract.get("turnoverOf24h")),
        "volume_base_24h": safe_float(contract.get("volumeOf24h")),
        "contract_multiplier": multiplier,
        "open_interest_contracts": open_interest_contracts,
        "open_interest_base": open_interest_base,
        "open_interest_usd": open_interest_usd,
        "oi_change_4h_pct": list_change(oi_rows, "openInterest", 4),
        "oi_change_24h_pct": list_change(oi_rows, "openInterest", 24),
        "global_long_short_ratio": None,
        "top_account_long_short_ratio": None,
        "top_position_long_short_ratio": None,
        "taker_buy_sell_ratio_recent": weighted_ratio(buy_notional, sell_notional),
        "taker_buy_notional_recent": buy_notional,
        "taker_sell_notional_recent": sell_notional,
        "recent_trade_count": len(trades),
        "orderbook": orderbook,
        "capabilities": {
            "funding": True,
            "open_interest": True,
            "taker_flow": True,
            "orderbook": True,
            "long_short_ratio": False,
            "public_liquidations": False,
        },
    }
    health = {name: endpoint_record(result) for name, result in calls.items()}
    raw = {name: result.data if result.ok else None for name, result in calls.items()}
    return {"parsed": parsed, "raw": raw}, health


def liquidation_empty() -> dict[str, Any]:
    return {
        asset: {
            "events": 0,
            "long_liquidation_usd": 0.0,
            "short_liquidation_usd": 0.0,
            "total_liquidation_usd": 0.0,
            "largest_event_usd": 0.0,
            "largest_event_side": "",
            "largest_event_price": None,
            "by_exchange": {},
        }
        for asset in ASSETS
    }


def add_liquidation(
    totals: dict[str, Any],
    lock: threading.Lock,
    exchange: str,
    symbol: str,
    position_side: str,
    price: Any,
    size: Any,
) -> None:
    asset = SYMBOL_TO_ASSET.get(str(symbol).upper())
    p = safe_float(price)
    q = safe_float(size)
    if asset is None or p is None or q is None or p <= 0 or q <= 0:
        return
    notional = p * q
    side = position_side.lower()
    long_liq = side in {"long", "buy"}
    short_liq = side in {"short", "sell"}
    if not long_liq and not short_liq:
        return

    with lock:
        row = totals[asset]
        row["events"] += 1
        row["total_liquidation_usd"] += notional
        if long_liq:
            row["long_liquidation_usd"] += notional
        else:
            row["short_liquidation_usd"] += notional
        exchange_row = row["by_exchange"].setdefault(
            exchange,
            {"events": 0, "long_liquidation_usd": 0.0, "short_liquidation_usd": 0.0},
        )
        exchange_row["events"] += 1
        if long_liq:
            exchange_row["long_liquidation_usd"] += notional
        else:
            exchange_row["short_liquidation_usd"] += notional
        if notional > row["largest_event_usd"]:
            row["largest_event_usd"] = notional
            row["largest_event_side"] = "LONG" if long_liq else "SHORT"
            row["largest_event_price"] = p


def collect_binance_liquidations(
    totals: dict[str, Any], lock: threading.Lock, deadline: float, health: dict[str, Any]
) -> None:
    try:
        import websocket  # type: ignore

        streams = "/".join(f"{symbol.lower()}@forceOrder" for symbol in SYMBOLS.values())
        url = f"wss://fstream.binance.com/stream?streams={streams}"
        ws = websocket.create_connection(url, timeout=4, sslopt={"cert_reqs": ssl.CERT_REQUIRED})
        ws.settimeout(2)
        received = 0
        while time.monotonic() < deadline:
            try:
                message = ws.recv()
            except (socket.timeout, TimeoutError):
                continue
            if not message:
                continue
            payload = json.loads(message)
            data = payload.get("data", payload)
            order = data.get("o", {}) if isinstance(data, dict) else {}
            symbol = order.get("s")
            order_side = str(order.get("S", "")).upper()
            # A SELL forced order closes a long; a BUY forced order closes a short.
            position_side = "long" if order_side == "SELL" else "short" if order_side == "BUY" else ""
            price = order.get("ap") or order.get("p")
            size = order.get("z") or order.get("q")
            add_liquidation(totals, lock, "binance", symbol, position_side, price, size)
            received += 1
        ws.close()
        health["binance"] = {"ok": True, "state": "OK", "messages": received, "error": ""}
    except Exception as exc:
        health["binance"] = {"ok": False, "state": "TIMEOUT" if "timeout" in str(exc).lower() else "ERROR", "messages": 0, "error": f"{type(exc).__name__}: {exc}"}


def collect_bybit_liquidations(
    totals: dict[str, Any], lock: threading.Lock, deadline: float, health: dict[str, Any]
) -> None:
    try:
        import websocket  # type: ignore

        url = "wss://stream.bybit.com/v5/public/linear"
        ws = websocket.create_connection(url, timeout=4, sslopt={"cert_reqs": ssl.CERT_REQUIRED})
        ws.settimeout(2)
        args = [f"allLiquidation.{symbol}" for symbol in SYMBOLS.values()]
        ws.send(json.dumps({"op": "subscribe", "args": args}))
        received = 0
        while time.monotonic() < deadline:
            try:
                message = ws.recv()
            except (socket.timeout, TimeoutError):
                continue
            if not message:
                continue
            payload = json.loads(message)
            rows = payload.get("data", []) if isinstance(payload, dict) else []
            if isinstance(rows, dict):
                rows = [rows]
            if not isinstance(rows, list):
                continue
            for row in rows:
                if not isinstance(row, dict):
                    continue
                # Bybit docs: S=Buy means a long position has been liquidated.
                side = str(row.get("S", "")).lower()
                position_side = "long" if side == "buy" else "short" if side == "sell" else ""
                add_liquidation(
                    totals,
                    lock,
                    "bybit",
                    row.get("s"),
                    position_side,
                    row.get("p"),
                    row.get("v"),
                )
                received += 1
        ws.close()
        health["bybit"] = {"ok": True, "state": "OK", "messages": received, "error": ""}
    except Exception as exc:
        health["bybit"] = {"ok": False, "state": "TIMEOUT" if "timeout" in str(exc).lower() else "ERROR", "messages": 0, "error": f"{type(exc).__name__}: {exc}"}


def collect_liquidation_sample(exchange_states: dict[str, str] | None = None) -> tuple[dict[str, Any], dict[str, Any]]:
    totals = liquidation_empty()
    exchange_states = exchange_states or {}
    health: dict[str, Any] = {
        "sample_seconds": LIQ_SAMPLE_SECONDS,
        "skipped": SKIP_WEBSOCKET or LIQ_SAMPLE_SECONDS <= 0,
        "binance": {"ok": False, "state": "NOT_RUN", "messages": 0, "error": "not run"},
        "bybit": {"ok": False, "state": "NOT_RUN", "messages": 0, "error": "not run"},
    }
    for exchange in ("binance", "bybit"):
        state = exchange_states.get(exchange, "")
        if exchange not in ENABLED_EXCHANGES:
            health[exchange] = {"ok": False, "state": "DISABLED", "messages": 0, "error": "Exchange disabilitato dal collector."}
        elif state == "GEO_BLOCKED":
            health[exchange] = {"ok": False, "state": "GEO_BLOCKED", "messages": 0, "error": "WebSocket saltato: REST già bloccata geograficamente."}
    if health["skipped"]:
        return totals, health

    deadline = time.monotonic() + LIQ_SAMPLE_SECONDS
    lock = threading.Lock()
    threads = []
    if health["binance"].get("state") == "NOT_RUN":
        threads.append(threading.Thread(target=collect_binance_liquidations, args=(totals, lock, deadline, health), daemon=True))
    if health["bybit"].get("state") == "NOT_RUN":
        threads.append(threading.Thread(target=collect_bybit_liquidations, args=(totals, lock, deadline, health), daemon=True))
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join(timeout=LIQ_SAMPLE_SECONDS + 8)

    for asset, row in totals.items():
        total = row["total_liquidation_usd"]
        row["long_share_pct"] = row["long_liquidation_usd"] / total * 100.0 if total > 0 else None
        row["short_share_pct"] = row["short_liquidation_usd"] / total * 100.0 if total > 0 else None
        row["long_short_liquidation_ratio"] = weighted_ratio(
            row["long_liquidation_usd"], row["short_liquidation_usd"]
        )
    return totals, health


def shared_price(asset: str) -> float | None:
    payload = load_json(SHARED_SNAPSHOT_PATH)
    assets = payload.get("assets", {}) if isinstance(payload, dict) else {}
    row = assets.get(asset, {}) if isinstance(assets, dict) else {}
    if isinstance(row, dict):
        for key in ("price", "current_price", "close"):
            value = safe_float(row.get(key))
            if value is not None:
                return value
    # Support flat snapshots too.
    for key in (asset, f"{asset}_price", f"{asset.lower()}_price"):
        value = safe_float(payload.get(key)) if isinstance(payload, dict) else None
        if value is not None:
            return value
    return None


def _exchange_metric_values(exchanges: list[dict[str, Any]], key: str) -> list[float]:
    values: list[float] = []
    for exchange in exchanges:
        value = safe_float(exchange.get(key))
        if value is not None:
            values.append(value)
    return values


def _combined_book_metric(books: list[dict[str, Any]], key_suffix: str) -> tuple[float | None, float | None, float | None]:
    bids = [safe_float(book.get(f"bid_notional_{key_suffix}")) for book in books]
    asks = [safe_float(book.get(f"ask_notional_{key_suffix}")) for book in books]
    bid_total = sum(value for value in bids if value is not None)
    ask_total = sum(value for value in asks if value is not None)
    if bid_total == 0 and ask_total == 0:
        return None, None, None
    total = bid_total + ask_total
    imbalance = (bid_total - ask_total) / total if total > 0 else None
    return bid_total, ask_total, imbalance


def _direction_consensus(values: Iterable[Any], upper: float, lower: float) -> dict[str, Any]:
    parsed = [value for value in (safe_float(item) for item in values) if value is not None]
    bullish = sum(value >= upper for value in parsed)
    bearish = sum(value <= lower for value in parsed)
    neutral = len(parsed) - bullish - bearish
    if bullish >= 2 and bullish > bearish:
        label = "BULLISH_CONSENSUS"
    elif bearish >= 2 and bearish > bullish:
        label = "BEARISH_CONSENSUS"
    elif len(parsed) >= 2 and bullish and bearish:
        label = "DIVERGENT"
    else:
        label = "MIXED_OR_INSUFFICIENT"
    return {"available": len(parsed), "bullish": bullish, "bearish": bearish, "neutral": neutral, "label": label}


def combine_asset(
    asset: str,
    binance: dict[str, Any],
    bybit: dict[str, Any],
    kucoin: dict[str, Any],
    liquidation: dict[str, Any],
) -> dict[str, Any]:
    b = binance.get("parsed", {}) if isinstance(binance, dict) else {}
    y = bybit.get("parsed", {}) if isinstance(bybit, dict) else {}
    k = kucoin.get("parsed", {}) if isinstance(kucoin, dict) else {}
    exchanges = [b, y, k]
    price = shared_price(asset) or median(
        [
            b.get("mark_price"),
            y.get("mark_price"),
            k.get("mark_price"),
            b.get("last_price"),
            y.get("last_price"),
            k.get("last_price"),
        ]
    )

    b_book = b.get("orderbook", {}) if isinstance(b.get("orderbook"), dict) else {}
    y_book = y.get("orderbook", {}) if isinstance(y.get("orderbook"), dict) else {}
    k_book = k.get("orderbook", {}) if isinstance(k.get("orderbook"), dict) else {}
    books = [b_book, y_book, k_book]

    supported_slots = {
        "funding": 3,
        "basis": 3,
        "open_interest": 3,
        "taker_flow": 3,
        "orderbook": 3,
        "long_short": 2,
    }
    available_counts = {
        "funding": len(_exchange_metric_values(exchanges, "funding_rate_pct")),
        "basis": len(_exchange_metric_values(exchanges, "basis_pct")),
        "open_interest": len(_exchange_metric_values(exchanges, "open_interest_usd")),
        "taker_flow": len(
            [
                value
                for value in [
                    safe_float(b.get("taker_buy_sell_ratio_4h")),
                    safe_float(y.get("taker_buy_sell_ratio_recent")),
                    safe_float(k.get("taker_buy_sell_ratio_recent")),
                ]
                if value is not None
            ]
        ),
        "orderbook": len(
            [book for book in books if safe_float(book.get("imbalance_0_5pct")) is not None]
        ),
        "long_short": len(
            [value for value in [safe_float(b.get("global_long_short_ratio")), safe_float(y.get("global_long_short_ratio"))] if value is not None]
        ),
    }
    total_supported = sum(supported_slots.values())
    total_available = sum(min(available_counts[key], supported_slots[key]) for key in supported_slots)
    coverage = total_available / total_supported if total_supported else 0.0

    oi_weights = [safe_float(exchange.get("open_interest_usd"), 0.0) or 0.0 for exchange in exchanges]
    combined_oi_usd = sum(weight for weight in oi_weights if weight > 0) or None
    weighted_funding = weighted_mean(
        [(exchange.get("funding_rate_pct"), exchange.get("open_interest_usd")) for exchange in exchanges]
    ) or mean(_exchange_metric_values(exchanges, "funding_rate_pct"))
    weighted_basis = weighted_mean(
        [(exchange.get("basis_pct"), exchange.get("open_interest_usd")) for exchange in exchanges]
    ) or mean(_exchange_metric_values(exchanges, "basis_pct"))
    weighted_oi_4h = weighted_mean(
        [(exchange.get("oi_change_4h_pct"), exchange.get("open_interest_usd")) for exchange in exchanges]
    ) or mean(_exchange_metric_values(exchanges, "oi_change_4h_pct"))
    weighted_oi_24h = weighted_mean(
        [(exchange.get("oi_change_24h_pct"), exchange.get("open_interest_usd")) for exchange in exchanges]
    ) or mean(_exchange_metric_values(exchanges, "oi_change_24h_pct"))

    flow_values = [
        b.get("taker_buy_sell_ratio_4h"),
        y.get("taker_buy_sell_ratio_recent"),
        k.get("taker_buy_sell_ratio_recent"),
    ]
    flow_4h = median(flow_values)
    flow_24h = b.get("taker_buy_sell_ratio_24h")

    book_combined: dict[str, Any] = {}
    for suffix in ("0_25pct", "0_5pct", "1_0pct", "2_0pct"):
        bid, ask, imbalance = _combined_book_metric(books, suffix)
        book_combined[f"bid_notional_{suffix}"] = bid
        book_combined[f"ask_notional_{suffix}"] = ask
        book_combined[f"imbalance_{suffix}"] = imbalance

    exchange_available = {
        "binance": bool(b.get("available")),
        "bybit": bool(y.get("available")),
        "kucoin": bool(k.get("available")),
    }
    exchange_count = sum(exchange_available.values())
    consensus = {
        "funding": _direction_consensus(
            [-(safe_float(item.get("funding_rate_pct")) or 0.0) if safe_float(item.get("funding_rate_pct")) is not None else None for item in exchanges],
            0.01,
            -0.01,
        ),
        "oi_24h": _direction_consensus([item.get("oi_change_24h_pct") for item in exchanges], 2.0, -2.0),
        "taker_flow": _direction_consensus(flow_values, 1.05, 0.95),
        "orderbook": _direction_consensus([book.get("imbalance_0_5pct") for book in books], 0.05, -0.05),
    }
    labels = [item["label"] for item in consensus.values()]
    bullish_consensus_count = sum(label == "BULLISH_CONSENSUS" for label in labels)
    bearish_consensus_count = sum(label == "BEARISH_CONSENSUS" for label in labels)
    divergent_count = sum(label == "DIVERGENT" for label in labels)

    available_fields = {
        **exchange_available,
        "funding": available_counts["funding"] > 0,
        "open_interest": available_counts["open_interest"] > 0,
        "taker_flow": available_counts["taker_flow"] > 0,
        "long_short": available_counts["long_short"] > 0,
        "orderbook": available_counts["orderbook"] > 0,
        "liquidation_stream": liquidation.get("events", 0) > 0,
    }

    return {
        "asset": asset,
        "symbol": SYMBOLS[asset],
        "kucoin_symbol": KUCOIN_SYMBOLS[asset],
        "price": price,
        "generated_utc": utc_now_iso(),
        "data_coverage": coverage,
        "exchange_count": exchange_count,
        "exchange_available": exchange_available,
        "available_counts": available_counts,
        "available_fields": available_fields,
        "funding_rate_pct": weighted_funding,
        "basis_pct": weighted_basis,
        "price_change_24h_pct": median([item.get("price_change_24h_pct") for item in exchanges]),
        "open_interest_usd_combined": combined_oi_usd,
        "oi_change_4h_pct": weighted_oi_4h,
        "oi_change_24h_pct": weighted_oi_24h,
        "global_long_short_ratio": mean([b.get("global_long_short_ratio"), y.get("global_long_short_ratio")]),
        "top_account_long_short_ratio": b.get("top_account_long_short_ratio"),
        "top_position_long_short_ratio": b.get("top_position_long_short_ratio"),
        "taker_buy_sell_ratio_1h": b.get("taker_buy_sell_ratio_1h"),
        "taker_buy_sell_ratio_4h": flow_4h,
        "taker_buy_sell_ratio_24h": flow_24h,
        "orderbook_imbalance_0_25pct": book_combined.get("imbalance_0_25pct"),
        "orderbook_imbalance_0_5pct": book_combined.get("imbalance_0_5pct"),
        "orderbook_imbalance_1_0pct": book_combined.get("imbalance_1_0pct"),
        "orderbook_imbalance_2_0pct": book_combined.get("imbalance_2_0pct"),
        "orderbook_bid_notional_0_5pct": book_combined.get("bid_notional_0_5pct"),
        "orderbook_ask_notional_0_5pct": book_combined.get("ask_notional_0_5pct"),
        "spread_bps": median([b_book.get("spread_bps"), y_book.get("spread_bps"), k_book.get("spread_bps")]),
        "binance_bid_wall": b_book.get("largest_bid_wall", {}),
        "binance_ask_wall": b_book.get("largest_ask_wall", {}),
        "bybit_bid_wall": y_book.get("largest_bid_wall", {}),
        "bybit_ask_wall": y_book.get("largest_ask_wall", {}),
        "kucoin_bid_wall": k_book.get("largest_bid_wall", {}),
        "kucoin_ask_wall": k_book.get("largest_ask_wall", {}),
        "exchange_consensus": consensus,
        "bullish_consensus_count": bullish_consensus_count,
        "bearish_consensus_count": bearish_consensus_count,
        "divergent_metric_count": divergent_count,
        "liquidation_sample": liquidation,
        "exchanges": {
            "binance": b,
            "bybit": y,
            "kucoin": k,
        },
    }



INTRADAY_FIELDS = [
    "schema_version", "timestamp_utc", "snapshot_date", "asset", "price", "data_coverage", "exchange_count",
    "binance_available", "bybit_available", "kucoin_available",
    "funding_rate_pct", "basis_pct", "price_change_24h_pct", "open_interest_usd_combined",
    "oi_change_4h_pct", "oi_change_24h_pct", "global_long_short_ratio",
    "taker_buy_sell_ratio_1h", "taker_buy_sell_ratio_4h", "taker_buy_sell_ratio_24h",
    "orderbook_imbalance_0_25pct", "orderbook_imbalance_0_5pct", "orderbook_imbalance_1_0pct",
    "orderbook_bid_notional_0_5pct", "orderbook_ask_notional_0_5pct", "spread_bps",
    "long_liquidation_usd_sample", "short_liquidation_usd_sample", "liquidation_events_sample",
    "binance_funding_rate_pct", "bybit_funding_rate_pct", "kucoin_funding_rate_pct",
    "binance_open_interest_usd", "bybit_open_interest_usd", "kucoin_open_interest_usd",
    "binance_taker_ratio", "bybit_taker_ratio", "kucoin_taker_ratio",
    "binance_book_imbalance_0_5pct", "bybit_book_imbalance_0_5pct", "kucoin_book_imbalance_0_5pct",
]


def _iso_datetime(value: Any) -> datetime | None:
    text = str(value or "").strip().replace("Z", "+00:00")
    if not text:
        return None
    try:
        parsed = datetime.fromisoformat(text)
        if parsed.tzinfo is None:
            parsed = parsed.replace(tzinfo=timezone.utc)
        return parsed.astimezone(timezone.utc)
    except ValueError:
        return None


def _intraday_row(timestamp: str, snapshot_date: str, asset: str, row: dict[str, Any]) -> dict[str, Any]:
    exchanges = row.get("exchanges", {}) if isinstance(row.get("exchanges"), dict) else {}
    b = exchanges.get("binance", {}) if isinstance(exchanges.get("binance"), dict) else {}
    y = exchanges.get("bybit", {}) if isinstance(exchanges.get("bybit"), dict) else {}
    k = exchanges.get("kucoin", {}) if isinstance(exchanges.get("kucoin"), dict) else {}
    b_book = b.get("orderbook", {}) if isinstance(b.get("orderbook"), dict) else {}
    y_book = y.get("orderbook", {}) if isinstance(y.get("orderbook"), dict) else {}
    k_book = k.get("orderbook", {}) if isinstance(k.get("orderbook"), dict) else {}
    available = row.get("exchange_available", {}) if isinstance(row.get("exchange_available"), dict) else {}
    liq = row.get("liquidation_sample", {}) if isinstance(row.get("liquidation_sample"), dict) else {}
    return {
        "schema_version": SCHEMA_VERSION,
        "timestamp_utc": timestamp,
        "snapshot_date": snapshot_date,
        "asset": asset,
        "price": row.get("price"),
        "data_coverage": row.get("data_coverage"),
        "exchange_count": row.get("exchange_count"),
        "binance_available": bool(available.get("binance")),
        "bybit_available": bool(available.get("bybit")),
        "kucoin_available": bool(available.get("kucoin")),
        "funding_rate_pct": row.get("funding_rate_pct"),
        "basis_pct": row.get("basis_pct"),
        "price_change_24h_pct": row.get("price_change_24h_pct"),
        "open_interest_usd_combined": row.get("open_interest_usd_combined"),
        "oi_change_4h_pct": row.get("oi_change_4h_pct"),
        "oi_change_24h_pct": row.get("oi_change_24h_pct"),
        "global_long_short_ratio": row.get("global_long_short_ratio"),
        "taker_buy_sell_ratio_1h": row.get("taker_buy_sell_ratio_1h"),
        "taker_buy_sell_ratio_4h": row.get("taker_buy_sell_ratio_4h"),
        "taker_buy_sell_ratio_24h": row.get("taker_buy_sell_ratio_24h"),
        "orderbook_imbalance_0_25pct": row.get("orderbook_imbalance_0_25pct"),
        "orderbook_imbalance_0_5pct": row.get("orderbook_imbalance_0_5pct"),
        "orderbook_imbalance_1_0pct": row.get("orderbook_imbalance_1_0pct"),
        "orderbook_bid_notional_0_5pct": row.get("orderbook_bid_notional_0_5pct"),
        "orderbook_ask_notional_0_5pct": row.get("orderbook_ask_notional_0_5pct"),
        "spread_bps": row.get("spread_bps"),
        "long_liquidation_usd_sample": liq.get("long_liquidation_usd"),
        "short_liquidation_usd_sample": liq.get("short_liquidation_usd"),
        "liquidation_events_sample": liq.get("events"),
        "binance_funding_rate_pct": b.get("funding_rate_pct"),
        "bybit_funding_rate_pct": y.get("funding_rate_pct"),
        "kucoin_funding_rate_pct": k.get("funding_rate_pct"),
        "binance_open_interest_usd": b.get("open_interest_usd"),
        "bybit_open_interest_usd": y.get("open_interest_usd"),
        "kucoin_open_interest_usd": k.get("open_interest_usd"),
        "binance_taker_ratio": b.get("taker_buy_sell_ratio_4h"),
        "bybit_taker_ratio": y.get("taker_buy_sell_ratio_recent"),
        "kucoin_taker_ratio": k.get("taker_buy_sell_ratio_recent"),
        "binance_book_imbalance_0_5pct": b_book.get("imbalance_0_5pct"),
        "bybit_book_imbalance_0_5pct": y_book.get("imbalance_0_5pct"),
        "kucoin_book_imbalance_0_5pct": k_book.get("imbalance_0_5pct"),
    }


def append_intraday_history(snapshot: dict[str, Any]) -> None:
    timestamp = str(snapshot.get("generated_utc") or utc_now_iso())
    snapshot_date = str(snapshot.get("snapshot_date") or utc_date())
    assets = snapshot.get("assets", {}) if isinstance(snapshot.get("assets"), dict) else {}
    new_rows = [
        _intraday_row(timestamp, snapshot_date, asset, row)
        for asset, row in assets.items()
        if asset in ASSETS and isinstance(row, dict)
    ]
    if not new_rows:
        return

    existing: list[dict[str, Any]] = []
    if INTRADAY_HISTORY_PATH.exists():
        try:
            with INTRADAY_HISTORY_PATH.open("r", encoding="utf-8", newline="") as handle:
                existing = list(csv.DictReader(handle))
        except Exception:
            existing = []

    cutoff = datetime.now(timezone.utc) - timedelta(days=INTRADAY_RETENTION_DAYS)
    kept: list[dict[str, Any]] = []
    seen: set[tuple[str, str]] = set()
    for row in existing + new_rows:
        row_time = _iso_datetime(row.get("timestamp_utc"))
        if row_time is not None and row_time < cutoff:
            continue
        key = (str(row.get("timestamp_utc", "")), str(row.get("asset", "")))
        if key in seen:
            continue
        seen.add(key)
        projected = {field: row.get(field, "") for field in INTRADAY_FIELDS}
        if not projected.get("schema_version"):
            projected["schema_version"] = "2.0"
        kept.append(projected)

    kept.sort(key=lambda item: (str(item.get("timestamp_utc", "")), str(item.get("asset", ""))))
    INTRADAY_HISTORY_PATH.parent.mkdir(parents=True, exist_ok=True)
    tmp = INTRADAY_HISTORY_PATH.with_suffix(".csv.tmp")
    with tmp.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=INTRADAY_FIELDS)
        writer.writeheader()
        writer.writerows(kept)
    tmp.replace(INTRADAY_HISTORY_PATH)

def fixture_mode() -> dict[str, Any] | None:
    path_value = os.getenv("EXCHANGE_TEST_FIXTURE", "").strip()
    if not path_value:
        return None
    path = Path(path_value)
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise RuntimeError("EXCHANGE_TEST_FIXTURE must contain a JSON object")
    return payload


def main() -> None:
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    fixture = fixture_mode()
    if fixture is not None:
        atomic_json(SNAPSHOT_PATH, fixture)
        append_intraday_history(fixture)
        atomic_json(HEALTH_PATH, {"generated_utc": utc_now_iso(), "fixture": True, "status": "OK"})
        atomic_json(RAW_PATH, {"fixture": True})
        print(f"Fixture exchange scritto in {SNAPSHOT_PATH}")
        return

    session = build_session()
    parsed_assets: dict[str, Any] = {}
    raw_assets: dict[str, Any] = {}
    health_assets: dict[str, Any] = {}
    blocked_states: dict[str, str] = {}

    for asset in ASSETS:
        exchange_payloads: dict[str, dict[str, Any]] = {}
        exchange_health: dict[str, dict[str, Any]] = {}
        for exchange, fetcher in (
            ("binance", fetch_binance_asset),
            ("bybit", fetch_bybit_asset),
            ("kucoin", fetch_kucoin_asset),
        ):
            if exchange not in ENABLED_EXCHANGES:
                payload = unavailable_exchange_payload(asset, exchange, "DISABLED", "Exchange disabilitato da EXCHANGE_ENABLED_EXCHANGES.")
                health_row = {"collector": skipped_endpoint_record("DISABLED", "Exchange disabilitato da EXCHANGE_ENABLED_EXCHANGES.")}
            elif blocked_states.get(exchange) == "GEO_BLOCKED":
                payload = unavailable_exchange_payload(asset, exchange, "GEO_BLOCKED", "Saltato dopo blocco geografico rilevato sul primo asset.")
                health_row = {"collector": skipped_endpoint_record("GEO_BLOCKED", "Saltato dopo blocco geografico rilevato sul primo asset.")}
            else:
                payload, health_row = fetcher(session, asset)
                state = health_state(health_row)
                if state == "GEO_BLOCKED":
                    blocked_states[exchange] = state
            exchange_payloads[exchange] = payload
            exchange_health[exchange] = health_row

        binance = exchange_payloads["binance"]
        bybit = exchange_payloads["bybit"]
        kucoin = exchange_payloads["kucoin"]
        binance_health = exchange_health["binance"]
        bybit_health = exchange_health["bybit"]
        kucoin_health = exchange_health["kucoin"]
        parsed_assets[asset] = {"binance": binance, "bybit": bybit, "kucoin": kucoin}
        raw_assets[asset] = {
            "binance": binance.get("raw", {}),
            "bybit": bybit.get("raw", {}),
            "kucoin": kucoin.get("raw", {}),
        }
        health_assets[asset] = {
            "binance": binance_health,
            "bybit": bybit_health,
            "kucoin": kucoin_health,
        }

    exchange_states = {
        exchange: ("DISABLED" if exchange not in ENABLED_EXCHANGES else blocked_states.get(exchange, "OK"))
        for exchange in EXCHANGE_NAMES
    }
    liquidations, liquidation_health = collect_liquidation_sample(exchange_states)

    combined = {
        asset: combine_asset(
            asset,
            parsed_assets[asset]["binance"],
            parsed_assets[asset]["bybit"],
            parsed_assets[asset]["kucoin"],
            liquidations[asset],
        )
        for asset in ASSETS
    }

    snapshot = {
        "schema_version": SCHEMA_VERSION,
        "generated_utc": utc_now_iso(),
        "snapshot_date": utc_date(),
        "liquidation_sample_seconds": LIQ_SAMPLE_SECONDS,
        "collector_mode": COLLECTOR_MODE,
        "enabled_exchanges": list(ENABLED_EXCHANGES),
        "assets": combined,
        "notes": {
            "liquidation_scope": (
                "Actual liquidation events observed only during the short public WebSocket sample from Binance and Bybit; "
                "KuCoin has no equivalent public all-liquidations feed in this collector; this is not a complete 24h liquidation map."
            ),
            "kucoin_scope": (
                "KuCoin contributes contract/mark/index, funding, open interest, recent public trades and order book. "
                "Public global long/short ratio and public all-liquidation events are not assumed available."
            ),
            "liquidity_scope": (
                "Order-book liquidity is a current snapshot and can be cancelled; walls are context, not guaranteed support/resistance."
            ),
        },
    }

    health_ok = sum(
        1
        for asset in ASSETS
        for exchange in ("binance", "bybit", "kucoin")
        if parsed_assets[asset][exchange].get("parsed", {}).get("available")
    )
    exchange_status = {}
    for exchange in EXCHANGE_NAMES:
        states = [health_state(health_assets[asset].get(exchange, {})) for asset in ASSETS]
        if "OK" in states:
            exchange_status[exchange] = "OK"
        elif "GEO_BLOCKED" in states:
            exchange_status[exchange] = "GEO_BLOCKED"
        elif "DISABLED" in states:
            exchange_status[exchange] = "DISABLED"
        else:
            exchange_status[exchange] = next((state for state in states if state not in {"MISSING", ""}), "MISSING")

    health = {
        "schema_version": SCHEMA_VERSION,
        "generated_utc": utc_now_iso(),
        "collector_mode": COLLECTOR_MODE,
        "enabled_exchanges": list(ENABLED_EXCHANGES),
        "status": "OK" if health_ok >= 6 else "WARN",
        "available_exchange_asset_pairs": health_ok,
        "total_exchange_asset_pairs": len(ASSETS) * 3,
        "exchange_status": exchange_status,
        "assets": health_assets,
        "liquidation_streams": liquidation_health,
    }

    atomic_json(SNAPSHOT_PATH, snapshot)
    append_intraday_history(snapshot)
    atomic_json(HEALTH_PATH, health)
    atomic_json(RAW_PATH, {"schema_version": SCHEMA_VERSION, "generated_utc": utc_now_iso(), "assets": raw_assets})

    print(f"Exchange snapshot scritto in: {SNAPSHOT_PATH}")
    print(f"Exchange health scritto in: {HEALTH_PATH}")
    print(f"Exchange raw scritto in: {RAW_PATH}")
    print(f"Exchange intraday history scritto in: {INTRADAY_HISTORY_PATH}")
    print(f"Source health: {health['status']} ({health_ok}/{len(ASSETS) * 3} coppie exchange/asset)")


if __name__ == "__main__":
    main()
