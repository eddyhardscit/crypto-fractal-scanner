# -*- coding: utf-8 -*-
"""Diagnostic and integration-ready adapters for alternative public exchange data.

Version 2.1.2 (diagnostic stage)

Purpose
-------
Test, from the real GitHub-hosted runner, whether Kraken Futures, Bitget Futures,
OKX perpetual swaps and Coinbase spot can provide usable public data for BTC,
SOL and DOGE. KuCoin Futures is included as a control because it is already used
by the scanner.

This file does not modify Global Confluence, predictions or trading decisions.
It writes only diagnostic/sample files under ``reports/``.

No account API keys, passwords, seed phrases or trading permissions are used.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import os
import re
import sys
import time
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


VERSION = "2.1.2b"
REPORTS_DIR = Path("reports")
JSON_PATH = REPORTS_DIR / "alternative_exchange_source_diagnostics.json"
SAMPLES_PATH = REPORTS_DIR / "alternative_exchange_source_samples.json"
CSV_PATH = REPORTS_DIR / "alternative_exchange_source_capabilities.csv"
MD_PATH = REPORTS_DIR / "alternative_exchange_source_diagnostics.md"

ASSETS = ("BTC", "SOL", "DOGE")
HTTP_TIMEOUT = max(4.0, min(30.0, float(os.getenv("ALT_EXCHANGE_HTTP_TIMEOUT", "12"))))
USER_AGENT = f"crypto-fractal-scanner-alt-exchange-probe/{VERSION}"
BOOK_WINDOW_PCT = 0.50

KRAKEN_BASE = "https://futures.kraken.com/derivatives/api/v3"
BITGET_BASE = "https://api.bitget.com"
OKX_BASE = "https://www.okx.com"
COINBASE_BASE = "https://api.exchange.coinbase.com"
KUCOIN_FUTURES_BASE = "https://api-futures.kucoin.com"
KUCOIN_UA_BASE = "https://api.kucoin.com"

BITGET_SYMBOLS = {asset: f"{asset}USDT" for asset in ASSETS}
OKX_SYMBOLS = {asset: f"{asset}-USDT-SWAP" for asset in ASSETS}
COINBASE_SYMBOLS = {asset: f"{asset}-USD" for asset in ASSETS}
KUCOIN_SYMBOLS = {"BTC": "XBTUSDTM", "SOL": "SOLUSDTM", "DOGE": "DOGEUSDTM"}
KRAKEN_PREFERRED_SYMBOLS = {"BTC": "PF_XBTUSD", "SOL": "PF_SOLUSD", "DOGE": "PF_DOGEUSD"}


@dataclass
class HTTPResult:
    ok: bool
    url: str
    status_code: int | None = None
    latency_ms: float | None = None
    data: Any = None
    error_kind: str = ""
    error: str = ""
    response_snippet: str = ""


@dataclass
class AssetProbe:
    exchange: str
    market_type: str
    asset: str
    symbol: str = ""
    status: str = "MANCANTE"
    reachable: bool = False
    market_exists: bool = False
    capabilities: dict[str, bool] = field(default_factory=dict)
    sample: dict[str, Any] = field(default_factory=dict)
    endpoints: dict[str, dict[str, Any]] = field(default_factory=dict)
    notes: list[str] = field(default_factory=list)

    def capability_count(self) -> tuple[int, int]:
        relevant = [
            "price",
            "mark_price",
            "index_price",
            "funding",
            "open_interest",
            "trades",
            "order_book",
        ]
        values = [bool(self.capabilities.get(name)) for name in relevant]
        return sum(values), len(values)

    def as_dict(self) -> dict[str, Any]:
        got, total = self.capability_count()
        return {
            "exchange": self.exchange,
            "market_type": self.market_type,
            "asset": self.asset,
            "symbol": self.symbol,
            "status": self.status,
            "reachable": self.reachable,
            "market_exists": self.market_exists,
            "capability_count": got,
            "capability_total": total,
            "coverage_pct": round(got / total * 100.0, 2) if total else 0.0,
            "capabilities": self.capabilities,
            "sample": self.sample,
            "endpoints": self.endpoints,
            "notes": self.notes,
        }


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def safe_float(value: Any, default: float | None = None) -> float | None:
    try:
        number = float(value)
        return number if math.isfinite(number) else default
    except (TypeError, ValueError):
        return default


def first_number(*values: Any) -> float | None:
    for value in values:
        number = safe_float(value)
        if number is not None:
            return number
    return None


def sanitize_text(value: Any, limit: int = 220) -> str:
    text = re.sub(r"\s+", " ", str(value or "")).strip()
    # Avoid leaking arbitrary HTML or oversized CDN error pages into the repository.
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text[:limit]


def classify_http_error(status: int | None, body: str) -> str:
    text = (body or "").lower()
    if status == 451:
        return "GEO_BLOCKED"
    if status == 403 and any(
        token in text
        for token in (
            "country",
            "region",
            "location",
            "restricted",
            "not available",
            "cloudfront",
            "access denied",
        )
    ):
        return "GEO_BLOCKED"
    if status == 403:
        return "FORBIDDEN"
    if status == 404:
        return "NOT_FOUND"
    if status == 429:
        return "RATE_LIMITED"
    if status is not None and status >= 500:
        return "SERVER_ERROR"
    if status is not None:
        return "HTTP_ERROR"
    return "NETWORK_ERROR"


def build_session() -> requests.Session:
    retry = Retry(
        total=2,
        connect=2,
        read=2,
        backoff_factor=0.5,
        status_forcelist=(429, 500, 502, 503, 504),
        allowed_methods=frozenset({"GET"}),
        raise_on_status=False,
    )
    adapter = HTTPAdapter(max_retries=retry, pool_connections=8, pool_maxsize=8)
    session = requests.Session()
    session.headers.update({"User-Agent": USER_AGENT, "Accept": "application/json"})
    session.mount("https://", adapter)
    return session


def get_json(
    session: requests.Session,
    base: str,
    path: str,
    params: dict[str, Any] | None = None,
) -> HTTPResult:
    url = base.rstrip("/") + path
    started = time.perf_counter()
    try:
        response = session.get(url, params=params or {}, timeout=HTTP_TIMEOUT)
        latency_ms = (time.perf_counter() - started) * 1000.0
        snippet = sanitize_text(response.text)
        if response.status_code != 200:
            return HTTPResult(
                False,
                response.url,
                response.status_code,
                latency_ms,
                error_kind=classify_http_error(response.status_code, response.text),
                error=f"HTTP {response.status_code}",
                response_snippet=snippet,
            )
        try:
            payload = response.json()
        except Exception as exc:
            return HTTPResult(
                False,
                response.url,
                response.status_code,
                latency_ms,
                error_kind="INVALID_JSON",
                error=f"{type(exc).__name__}: {exc}",
                response_snippet=snippet,
            )
        return HTTPResult(True, response.url, response.status_code, latency_ms, data=payload)
    except requests.Timeout as exc:
        return HTTPResult(
            False,
            url,
            latency_ms=(time.perf_counter() - started) * 1000.0,
            error_kind="TIMEOUT",
            error=f"{type(exc).__name__}: {exc}",
        )
    except requests.RequestException as exc:
        return HTTPResult(
            False,
            url,
            latency_ms=(time.perf_counter() - started) * 1000.0,
            error_kind="NETWORK_ERROR",
            error=f"{type(exc).__name__}: {exc}",
        )
    except Exception as exc:
        return HTTPResult(
            False,
            url,
            latency_ms=(time.perf_counter() - started) * 1000.0,
            error_kind="UNEXPECTED_ERROR",
            error=f"{type(exc).__name__}: {exc}",
        )


def endpoint_record(result: HTTPResult) -> dict[str, Any]:
    return {
        "ok": result.ok,
        "status_code": result.status_code,
        "latency_ms": round(result.latency_ms, 1) if result.latency_ms is not None else None,
        "error_kind": result.error_kind,
        "error": sanitize_text(result.error),
        "response_snippet": sanitize_text(result.response_snippet),
        "url": result.url,
    }


def api_payload_ok(result: HTTPResult, code: Any, success_values: set[str]) -> bool:
    return result.ok and str(code) in success_values


def weighted_ratio(buy: float, sell: float) -> float | None:
    return buy / sell if sell > 0 else None


def book_metrics(
    bids: Iterable[Any],
    asks: Iterable[Any],
    mid: float | None,
    quantity_multiplier: float = 1.0,
) -> dict[str, Any]:
    parsed_bids: list[tuple[float, float]] = []
    parsed_asks: list[tuple[float, float]] = []
    for row in bids or []:
        try:
            price = safe_float(row[0])
            qty = safe_float(row[1])
        except Exception:
            continue
        if price is not None and qty is not None and price > 0 and qty >= 0:
            parsed_bids.append((price, qty * quantity_multiplier))
    for row in asks or []:
        try:
            price = safe_float(row[0])
            qty = safe_float(row[1])
        except Exception:
            continue
        if price is not None and qty is not None and price > 0 and qty >= 0:
            parsed_asks.append((price, qty * quantity_multiplier))

    best_bid = max((price for price, _ in parsed_bids), default=None)
    best_ask = min((price for price, _ in parsed_asks), default=None)
    if mid is None and best_bid is not None and best_ask is not None:
        mid = (best_bid + best_ask) / 2.0

    spread_bps = None
    if best_bid is not None and best_ask is not None and mid not in (None, 0):
        spread_bps = (best_ask - best_bid) / mid * 10000.0

    bid_notional = 0.0
    ask_notional = 0.0
    if mid not in (None, 0):
        lower = mid * (1.0 - BOOK_WINDOW_PCT / 100.0)
        upper = mid * (1.0 + BOOK_WINDOW_PCT / 100.0)
        bid_notional = sum(price * qty for price, qty in parsed_bids if lower <= price <= mid)
        ask_notional = sum(price * qty for price, qty in parsed_asks if mid <= price <= upper)
    total = bid_notional + ask_notional
    imbalance = (bid_notional - ask_notional) / total if total > 0 else None

    return {
        "levels_bid": len(parsed_bids),
        "levels_ask": len(parsed_asks),
        "best_bid": best_bid,
        "best_ask": best_ask,
        "spread_bps": spread_bps,
        "bid_depth_0_5pct_usd": bid_notional,
        "ask_depth_0_5pct_usd": ask_notional,
        "book_imbalance_0_5pct": imbalance,
    }


def trade_metrics(
    rows: Iterable[Any],
    *,
    side_getter,
    price_getter,
    size_getter,
    multiplier: float = 1.0,
    invert_reported_side: bool = False,
) -> dict[str, Any]:
    buy = 0.0
    sell = 0.0
    count = 0
    for row in rows or []:
        try:
            side = str(side_getter(row) or "").lower()
            price = safe_float(price_getter(row))
            size = safe_float(size_getter(row))
        except Exception:
            continue
        if price is None or size is None or price <= 0 or size < 0:
            continue
        if invert_reported_side:
            side = "sell" if side == "buy" else "buy" if side == "sell" else side
        notional = price * size * multiplier
        if side == "buy":
            buy += notional
        elif side == "sell":
            sell += notional
        else:
            continue
        count += 1
    return {
        "trade_count": count,
        "taker_buy_notional": buy,
        "taker_sell_notional": sell,
        "taker_buy_sell_ratio": weighted_ratio(buy, sell),
    }


def base_capabilities(market_type: str) -> dict[str, bool]:
    return {
        "price": False,
        "mark_price": False,
        "index_price": False,
        "funding": False,
        "open_interest": False,
        "trades": False,
        "order_book": False,
        "spot_only": market_type == "spot",
        "public_liquidations": False,
        "long_short_ratio": False,
    }


def source_blocked_result(exchange: str, market_type: str, assets: Iterable[str], endpoint: HTTPResult) -> list[AssetProbe]:
    probes: list[AssetProbe] = []
    for asset in assets:
        probe = AssetProbe(exchange, market_type, asset, status=endpoint.error_kind or "MANCANTE")
        probe.capabilities = base_capabilities(market_type)
        probe.endpoints["preflight"] = endpoint_record(endpoint)
        probe.notes.append("La fonte è stata fermata dopo il preflight per evitare richieste ripetute inutili.")
        probes.append(probe)
    return probes


def finalize_probe(probe: AssetProbe) -> AssetProbe:
    endpoint_values = list(probe.endpoints.values())
    probe.reachable = any(bool(item.get("status_code")) for item in endpoint_values)
    errors = {str(item.get("error_kind") or "") for item in endpoint_values if not item.get("ok")}
    got, _ = probe.capability_count()
    if "GEO_BLOCKED" in errors:
        probe.status = "GEO_BLOCKED"
    elif probe.market_exists and got >= 5:
        probe.status = "OK"
    elif probe.market_exists and got > 0:
        probe.status = "PARZIALE"
    elif "RATE_LIMITED" in errors:
        probe.status = "RATE_LIMITED"
    elif "TIMEOUT" in errors:
        probe.status = "TIMEOUT"
    elif "FORBIDDEN" in errors:
        probe.status = "FORBIDDEN"
    elif probe.reachable:
        probe.status = "MERCATO/ENDPOINT MANCANTE"
    else:
        probe.status = "NON RAGGIUNGIBILE"
    return probe


def select_kraken_symbols(instruments: list[dict[str, Any]]) -> dict[str, str]:
    """Select exact Kraken perpetual symbols without substring collisions.

    Critical example: PF_SOLVUSD is Solv Protocol (SOLV), not Solana (SOL).
    Prefer the official exact symbols, then fall back only to exact base/pair tokens.
    """
    aliases = {"BTC": {"BTC", "XBT"}, "SOL": {"SOL"}, "DOGE": {"DOGE"}}
    normalized = {
        str(row.get("symbol") or "").upper(): row
        for row in instruments
        if isinstance(row, dict) and str(row.get("symbol") or "").strip()
    }
    selected: dict[str, str] = {}
    for asset in ASSETS:
        preferred = KRAKEN_PREFERRED_SYMBOLS[asset]
        row = normalized.get(preferred)
        if row and bool(row.get("tradeable", True)) and not bool(row.get("isExpired", False)):
            selected[asset] = preferred
            continue

        candidates: list[tuple[int, str]] = []
        for symbol, row in normalized.items():
            base = str(row.get("base") or "").upper().strip()
            pair = str(row.get("pair") or "").upper().replace("/", ":").strip()
            pair_base = pair.split(":", 1)[0] if ":" in pair else ""
            if not bool(row.get("tradeable", True)) or bool(row.get("isExpired", False)):
                continue
            # Exact matching only: never use substring matching such as SOL in SOLV.
            if base not in aliases[asset] and pair_base not in aliases[asset]:
                continue
            score = 0
            if symbol.startswith("PF_"):
                score += 50
            if str(row.get("type") or "") == "flexible_futures":
                score += 30
            if str(row.get("quote") or "").upper() in {"USD", "USDT"}:
                score += 10
            if symbol.endswith("USD") or symbol.endswith("USDT"):
                score += 5
            if row.get("lastTradingTime"):
                score -= 50
            candidates.append((score, symbol))
        if candidates:
            selected[asset] = sorted(candidates, reverse=True)[0][1]
    return selected


def probe_kraken(session: requests.Session) -> list[AssetProbe]:
    instruments_result = get_json(session, KRAKEN_BASE, "/instruments")
    if not instruments_result.ok:
        return source_blocked_result("kraken", "perpetual", ASSETS, instruments_result)
    payload = instruments_result.data if isinstance(instruments_result.data, dict) else {}
    if str(payload.get("result")) != "success":
        instruments_result.ok = False
        instruments_result.error_kind = "API_ERROR"
        instruments_result.error = f"Kraken result={payload.get('result')}"
        return source_blocked_result("kraken", "perpetual", ASSETS, instruments_result)
    instruments = payload.get("instruments") if isinstance(payload.get("instruments"), list) else []
    symbols = select_kraken_symbols(instruments)

    tickers_result = get_json(session, KRAKEN_BASE, "/tickers")
    ticker_rows: list[dict[str, Any]] = []
    if tickers_result.ok and isinstance(tickers_result.data, dict):
        ticker_rows = tickers_result.data.get("tickers") if isinstance(tickers_result.data.get("tickers"), list) else []
    ticker_map = {str(row.get("symbol") or "").upper(): row for row in ticker_rows if isinstance(row, dict)}
    instrument_map = {str(row.get("symbol") or "").upper(): row for row in instruments if isinstance(row, dict)}

    probes: list[AssetProbe] = []
    for asset in ASSETS:
        symbol = symbols.get(asset, "")
        probe = AssetProbe("kraken", "perpetual", asset, symbol=symbol)
        probe.capabilities = base_capabilities("perpetual")
        probe.endpoints["instruments"] = endpoint_record(instruments_result)
        probe.endpoints["tickers"] = endpoint_record(tickers_result)
        if not symbol:
            probe.notes.append("Nessun perpetual Kraken compatibile trovato dinamicamente.")
            probes.append(finalize_probe(probe))
            continue
        probe.market_exists = True
        ticker = ticker_map.get(symbol, {})
        last = first_number(ticker.get("last"), ticker.get("lastPrice"), ticker.get("bid"), ticker.get("ask"))
        mark = first_number(ticker.get("markPrice"), ticker.get("mark"))
        index = first_number(ticker.get("index"), ticker.get("indexPrice"))
        funding = first_number(ticker.get("fundingRate"), ticker.get("funding_rate"))
        oi = first_number(ticker.get("openInterest"), ticker.get("open_interest"))
        instrument = instrument_map.get(symbol, {})
        contract_size = first_number(
            instrument.get("contractSize"),
            instrument.get("contract_size"),
            instrument.get("contractValue"),
            instrument.get("contract_value"),
        )
        oi_base = oi * contract_size if oi is not None and contract_size is not None else None
        oi_usd = oi_base * (mark or last) if oi_base is not None and (mark or last) is not None else None
        probe.capabilities.update(
            {
                "price": last is not None,
                "mark_price": mark is not None,
                "index_price": index is not None,
                "funding": funding is not None,
                "open_interest": oi is not None,
            }
        )
        probe.sample.update(
            {
                "last_price": last,
                "mark_price": mark,
                "index_price": index,
                "funding_rate_raw": funding,
                "funding_rate_prediction_raw": first_number(ticker.get("fundingRatePrediction")),
                "open_interest_contracts_raw": oi,
                "contract_size": contract_size,
                "open_interest_base_raw": oi_base,
                "open_interest_usd": oi_usd,
                "volume_24h_raw": first_number(ticker.get("volume24h"), ticker.get("volume")),
            }
        )

        book_result = get_json(session, KRAKEN_BASE, "/orderbook", {"symbol": symbol})
        history_result = get_json(session, KRAKEN_BASE, "/history", {"symbol": symbol})
        probe.endpoints["orderbook"] = endpoint_record(book_result)
        probe.endpoints["trades"] = endpoint_record(history_result)

        if book_result.ok and isinstance(book_result.data, dict):
            book = book_result.data.get("orderBook") if isinstance(book_result.data.get("orderBook"), dict) else {}
            metrics = book_metrics(book.get("bids", []), book.get("asks", []), mark or last)
            probe.sample.update(metrics)
            probe.capabilities["order_book"] = metrics.get("levels_bid", 0) > 0 and metrics.get("levels_ask", 0) > 0
        if history_result.ok and isinstance(history_result.data, dict):
            rows = history_result.data.get("history") if isinstance(history_result.data.get("history"), list) else []
            metrics = trade_metrics(
                rows,
                side_getter=lambda r: r.get("side") if isinstance(r, dict) else None,
                price_getter=lambda r: r.get("price") if isinstance(r, dict) else None,
                size_getter=lambda r: r.get("size") if isinstance(r, dict) else None,
            )
            probe.sample.update(metrics)
            probe.capabilities["trades"] = metrics.get("trade_count", 0) > 0
        probes.append(finalize_probe(probe))
    return probes


def unwrap_bitget(result: HTTPResult) -> tuple[bool, Any, str]:
    if not result.ok or not isinstance(result.data, dict):
        return False, None, result.error_kind or "HTTP_ERROR"
    if str(result.data.get("code")) != "00000":
        return False, None, f"API_{result.data.get('code')}"
    return True, result.data.get("data"), ""


def probe_bitget(session: requests.Session) -> list[AssetProbe]:
    preflight = get_json(
        session,
        BITGET_BASE,
        "/api/v2/mix/market/contracts",
        {"productType": "usdt-futures"},
    )
    if not preflight.ok:
        return source_blocked_result("bitget", "perpetual", ASSETS, preflight)

    probes: list[AssetProbe] = []
    for asset in ASSETS:
        symbol = BITGET_SYMBOLS[asset]
        probe = AssetProbe("bitget", "perpetual", asset, symbol=symbol)
        probe.capabilities = base_capabilities("perpetual")
        probe.endpoints["contracts"] = endpoint_record(preflight)
        calls = {
            "price": get_json(session, BITGET_BASE, "/api/v2/mix/market/symbol-price", {"productType": "usdt-futures", "symbol": symbol}),
            "funding": get_json(session, BITGET_BASE, "/api/v2/mix/market/current-fund-rate", {"productType": "usdt-futures", "symbol": symbol}),
            "open_interest": get_json(session, BITGET_BASE, "/api/v2/mix/market/open-interest", {"productType": "usdt-futures", "symbol": symbol}),
            "orderbook": get_json(session, BITGET_BASE, "/api/v2/mix/market/merge-depth", {"productType": "usdt-futures", "symbol": symbol, "precision": "scale0", "limit": "100"}),
            "trades": get_json(session, BITGET_BASE, "/api/v2/mix/market/fills", {"productType": "usdt-futures", "symbol": symbol, "limit": "100"}),
        }
        for name, result in calls.items():
            probe.endpoints[name] = endpoint_record(result)

        price_ok, price_data, _ = unwrap_bitget(calls["price"])
        funding_ok, funding_data, _ = unwrap_bitget(calls["funding"])
        oi_ok, oi_data, _ = unwrap_bitget(calls["open_interest"])
        book_ok, book_data, _ = unwrap_bitget(calls["orderbook"])
        trades_ok, trades_data, _ = unwrap_bitget(calls["trades"])

        price_row = price_data[0] if price_ok and isinstance(price_data, list) and price_data else {}
        funding_row = funding_data[0] if funding_ok and isinstance(funding_data, list) and funding_data else {}
        oi_rows = oi_data.get("openInterestList", []) if oi_ok and isinstance(oi_data, dict) else []
        oi_row = oi_rows[0] if isinstance(oi_rows, list) and oi_rows else {}
        last = first_number(price_row.get("price"))
        mark = first_number(price_row.get("markPrice"))
        index = first_number(price_row.get("indexPrice"))
        funding = first_number(funding_row.get("fundingRate"))
        oi = first_number(oi_row.get("size"))
        probe.market_exists = any((last is not None, mark is not None, oi is not None, funding is not None))
        probe.capabilities.update(
            {
                "price": last is not None,
                "mark_price": mark is not None,
                "index_price": index is not None,
                "funding": funding is not None,
                "open_interest": oi is not None,
            }
        )
        probe.sample.update(
            {
                "last_price": last,
                "mark_price": mark,
                "index_price": index,
                "funding_rate_raw": funding,
                "open_interest_base_raw": oi,
                "open_interest_usd": oi * (mark or last) if oi is not None and (mark or last) is not None else None,
            }
        )
        if book_ok and isinstance(book_data, dict):
            metrics = book_metrics(book_data.get("bids", []), book_data.get("asks", []), mark or last)
            probe.sample.update(metrics)
            probe.capabilities["order_book"] = metrics.get("levels_bid", 0) > 0 and metrics.get("levels_ask", 0) > 0
        if trades_ok and isinstance(trades_data, list):
            metrics = trade_metrics(
                trades_data,
                side_getter=lambda r: r.get("side") if isinstance(r, dict) else None,
                price_getter=lambda r: r.get("price") if isinstance(r, dict) else None,
                size_getter=lambda r: r.get("size") if isinstance(r, dict) else None,
            )
            probe.sample.update(metrics)
            probe.capabilities["trades"] = metrics.get("trade_count", 0) > 0
        probes.append(finalize_probe(probe))
    return probes


def unwrap_okx(result: HTTPResult) -> tuple[bool, list[Any], str]:
    if not result.ok or not isinstance(result.data, dict):
        return False, [], result.error_kind or "HTTP_ERROR"
    if str(result.data.get("code")) != "0":
        return False, [], f"API_{result.data.get('code')}"
    data = result.data.get("data")
    return True, data if isinstance(data, list) else [], ""


def probe_okx(session: requests.Session) -> list[AssetProbe]:
    preflight = get_json(session, OKX_BASE, "/api/v5/public/instruments", {"instType": "SWAP"})
    if not preflight.ok:
        return source_blocked_result("okx", "perpetual", ASSETS, preflight)
    preflight_ok, instrument_rows, _ = unwrap_okx(preflight)
    available = {str(row.get("instId") or "") for row in instrument_rows if isinstance(row, dict)} if preflight_ok else set()

    probes: list[AssetProbe] = []
    for asset in ASSETS:
        symbol = OKX_SYMBOLS[asset]
        probe = AssetProbe("okx", "perpetual", asset, symbol=symbol)
        probe.capabilities = base_capabilities("perpetual")
        probe.endpoints["instruments"] = endpoint_record(preflight)
        probe.market_exists = symbol in available
        calls = {
            "ticker": get_json(session, OKX_BASE, "/api/v5/market/ticker", {"instId": symbol}),
            "mark_price": get_json(session, OKX_BASE, "/api/v5/public/mark-price", {"instType": "SWAP", "instId": symbol}),
            "funding": get_json(session, OKX_BASE, "/api/v5/public/funding-rate", {"instId": symbol}),
            "open_interest": get_json(session, OKX_BASE, "/api/v5/public/open-interest", {"instType": "SWAP", "instId": symbol}),
            "orderbook": get_json(session, OKX_BASE, "/api/v5/market/books", {"instId": symbol, "sz": "100"}),
            "trades": get_json(session, OKX_BASE, "/api/v5/market/trades", {"instId": symbol, "limit": "100"}),
        }
        for name, result in calls.items():
            probe.endpoints[name] = endpoint_record(result)

        ticker_ok, ticker_rows, _ = unwrap_okx(calls["ticker"])
        mark_ok, mark_rows, _ = unwrap_okx(calls["mark_price"])
        funding_ok, funding_rows, _ = unwrap_okx(calls["funding"])
        oi_ok, oi_rows, _ = unwrap_okx(calls["open_interest"])
        book_ok, book_rows, _ = unwrap_okx(calls["orderbook"])
        trades_ok, trades_rows, _ = unwrap_okx(calls["trades"])

        ticker = ticker_rows[0] if ticker_ok and ticker_rows else {}
        mark_row = mark_rows[0] if mark_ok and mark_rows else {}
        funding_row = funding_rows[0] if funding_ok and funding_rows else {}
        oi_row = oi_rows[0] if oi_ok and oi_rows else {}
        last = first_number(ticker.get("last"))
        mark = first_number(mark_row.get("markPx"))
        funding = first_number(funding_row.get("fundingRate"))
        oi_base = first_number(oi_row.get("oiCcy"), oi_row.get("oi"))
        oi_usd = first_number(oi_row.get("oiUsd"))
        probe.market_exists = probe.market_exists or any((last is not None, mark is not None, oi_base is not None, funding is not None))
        probe.capabilities.update(
            {
                "price": last is not None,
                "mark_price": mark is not None,
                "index_price": False,
                "funding": funding is not None,
                "open_interest": oi_base is not None or oi_usd is not None,
            }
        )
        probe.sample.update(
            {
                "last_price": last,
                "mark_price": mark,
                "index_price": None,
                "funding_rate_raw": funding,
                "open_interest_base_raw": oi_base,
                "open_interest_usd": oi_usd,
            }
        )
        if book_ok and book_rows and isinstance(book_rows[0], dict):
            book = book_rows[0]
            metrics = book_metrics(book.get("bids", []), book.get("asks", []), mark or last)
            probe.sample.update(metrics)
            probe.capabilities["order_book"] = metrics.get("levels_bid", 0) > 0 and metrics.get("levels_ask", 0) > 0
        if trades_ok:
            metrics = trade_metrics(
                trades_rows,
                side_getter=lambda r: r.get("side") if isinstance(r, dict) else None,
                price_getter=lambda r: r.get("px") if isinstance(r, dict) else None,
                size_getter=lambda r: r.get("sz") if isinstance(r, dict) else None,
            )
            probe.sample.update(metrics)
            probe.capabilities["trades"] = metrics.get("trade_count", 0) > 0
        probes.append(finalize_probe(probe))
    return probes


def probe_coinbase(session: requests.Session) -> list[AssetProbe]:
    preflight = get_json(session, COINBASE_BASE, "/products")
    if not preflight.ok:
        return source_blocked_result("coinbase", "spot", ASSETS, preflight)
    products = preflight.data if isinstance(preflight.data, list) else []
    available = {str(row.get("id") or "") for row in products if isinstance(row, dict)}

    probes: list[AssetProbe] = []
    for asset in ASSETS:
        symbol = COINBASE_SYMBOLS[asset]
        probe = AssetProbe("coinbase", "spot", asset, symbol=symbol)
        probe.capabilities = base_capabilities("spot")
        probe.endpoints["products"] = endpoint_record(preflight)
        probe.market_exists = symbol in available
        calls = {
            "ticker": get_json(session, COINBASE_BASE, f"/products/{symbol}/ticker"),
            "orderbook": get_json(session, COINBASE_BASE, f"/products/{symbol}/book", {"level": "2"}),
            "trades": get_json(session, COINBASE_BASE, f"/products/{symbol}/trades", {"limit": "100"}),
        }
        for name, result in calls.items():
            probe.endpoints[name] = endpoint_record(result)
        ticker = calls["ticker"].data if calls["ticker"].ok and isinstance(calls["ticker"].data, dict) else {}
        last = first_number(ticker.get("price"))
        probe.market_exists = probe.market_exists or last is not None
        probe.capabilities["price"] = last is not None
        probe.sample.update({"last_price": last, "mark_price": None, "index_price": None, "funding_rate_raw": None, "open_interest_base_raw": None})

        if calls["orderbook"].ok and isinstance(calls["orderbook"].data, dict):
            book = calls["orderbook"].data
            metrics = book_metrics(book.get("bids", []), book.get("asks", []), last)
            probe.sample.update(metrics)
            probe.capabilities["order_book"] = metrics.get("levels_bid", 0) > 0 and metrics.get("levels_ask", 0) > 0
        if calls["trades"].ok and isinstance(calls["trades"].data, list):
            # Coinbase Exchange REST reports the maker side. Taker aggression is the opposite side.
            metrics = trade_metrics(
                calls["trades"].data,
                side_getter=lambda r: r.get("side") if isinstance(r, dict) else None,
                price_getter=lambda r: r.get("price") if isinstance(r, dict) else None,
                size_getter=lambda r: r.get("size") if isinstance(r, dict) else None,
                invert_reported_side=True,
            )
            probe.sample.update(metrics)
            probe.sample["trade_side_semantics"] = "maker side inverted to estimate taker aggression"
            probe.capabilities["trades"] = metrics.get("trade_count", 0) > 0
        probe.notes.append("Conferma spot: non fornisce funding o open interest dei perpetual.")
        probes.append(finalize_probe(probe))
    return probes


def unwrap_kucoin(result: HTTPResult) -> tuple[bool, Any, str]:
    if not result.ok or not isinstance(result.data, dict):
        return False, None, result.error_kind or "HTTP_ERROR"
    if str(result.data.get("code")) != "200000":
        return False, None, f"API_{result.data.get('code')}"
    return True, result.data.get("data"), ""


def probe_kucoin_control(session: requests.Session) -> list[AssetProbe]:
    preflight = get_json(session, KUCOIN_FUTURES_BASE, "/api/v1/contracts/active")
    if not preflight.ok:
        return source_blocked_result("kucoin", "perpetual-control", ASSETS, preflight)
    probes: list[AssetProbe] = []
    for asset in ASSETS:
        symbol = KUCOIN_SYMBOLS[asset]
        probe = AssetProbe("kucoin", "perpetual-control", asset, symbol=symbol)
        probe.capabilities = base_capabilities("perpetual")
        probe.endpoints["contracts_active"] = endpoint_record(preflight)
        calls = {
            "contract": get_json(session, KUCOIN_FUTURES_BASE, f"/api/v1/contracts/{symbol}"),
            "ticker": get_json(session, KUCOIN_FUTURES_BASE, "/api/v1/ticker", {"symbol": symbol}),
            "funding": get_json(session, KUCOIN_FUTURES_BASE, f"/api/v1/funding-rate/{symbol}/current"),
            "orderbook": get_json(session, KUCOIN_FUTURES_BASE, "/api/v1/level2/snapshot", {"symbol": symbol}),
            "trades": get_json(session, KUCOIN_FUTURES_BASE, "/api/v1/trade/history", {"symbol": symbol}),
        }
        for name, result in calls.items():
            probe.endpoints[name] = endpoint_record(result)
        contract_ok, contract, _ = unwrap_kucoin(calls["contract"])
        ticker_ok, ticker, _ = unwrap_kucoin(calls["ticker"])
        funding_ok, funding, _ = unwrap_kucoin(calls["funding"])
        book_ok, book, _ = unwrap_kucoin(calls["orderbook"])
        trades_ok, trades, _ = unwrap_kucoin(calls["trades"])
        contract = contract if contract_ok and isinstance(contract, dict) else {}
        ticker = ticker if ticker_ok and isinstance(ticker, dict) else {}
        funding = funding if funding_ok and isinstance(funding, dict) else {}
        multiplier = first_number(contract.get("multiplier")) or 1.0
        last = first_number(ticker.get("price"), contract.get("lastTradePrice"))
        mark = first_number(contract.get("markPrice"), last)
        index = first_number(contract.get("indexPrice"), last)
        oi_contracts = first_number(contract.get("openInterest"))
        oi_base = oi_contracts * multiplier if oi_contracts is not None else None
        funding_rate = first_number(funding.get("value"), contract.get("fundingFeeRate"))
        probe.market_exists = contract_ok or ticker_ok
        probe.capabilities.update(
            {
                "price": last is not None,
                "mark_price": mark is not None,
                "index_price": index is not None,
                "funding": funding_rate is not None,
                "open_interest": oi_base is not None,
            }
        )
        probe.sample.update(
            {
                "last_price": last,
                "mark_price": mark,
                "index_price": index,
                "funding_rate_raw": funding_rate,
                "open_interest_base_raw": oi_base,
                "open_interest_usd": oi_base * (mark or last) if oi_base is not None and (mark or last) is not None else None,
                "contract_multiplier": multiplier,
            }
        )
        if book_ok and isinstance(book, dict):
            metrics = book_metrics(book.get("bids", []), book.get("asks", []), mark or last, multiplier)
            probe.sample.update(metrics)
            probe.capabilities["order_book"] = metrics.get("levels_bid", 0) > 0 and metrics.get("levels_ask", 0) > 0
        if trades_ok and isinstance(trades, list):
            metrics = trade_metrics(
                trades,
                side_getter=lambda r: r.get("side") if isinstance(r, dict) else None,
                price_getter=lambda r: r.get("price") if isinstance(r, dict) else None,
                size_getter=lambda r: r.get("size") if isinstance(r, dict) else None,
                multiplier=multiplier,
            )
            probe.sample.update(metrics)
            probe.capabilities["trades"] = metrics.get("trade_count", 0) > 0
        probes.append(finalize_probe(probe))
    return probes


def apply_cross_source_price_sanity(probes: list[AssetProbe], max_deviation_pct: float = 5.0) -> None:
    """Reject accidental symbol collisions using the cross-source price median."""
    for asset in ASSETS:
        rows = [probe for probe in probes if probe.asset == asset]
        prices = sorted(
            price
            for price in (safe_float(probe.sample.get("last_price")) for probe in rows)
            if price is not None and price > 0
        )
        if len(prices) < 3:
            continue
        middle = len(prices) // 2
        median_price = prices[middle] if len(prices) % 2 else (prices[middle - 1] + prices[middle]) / 2.0
        for probe in rows:
            price = safe_float(probe.sample.get("last_price"))
            if price is None or price <= 0 or median_price <= 0:
                continue
            deviation = abs(price / median_price - 1.0) * 100.0
            probe.sample["cross_source_price_median"] = median_price
            probe.sample["cross_source_price_deviation_pct"] = deviation
            if deviation > max_deviation_pct:
                probe.status = "PREZZO/SIMBOLO NON COERENTE"
                probe.capabilities["price"] = False
                probe.market_exists = False
                probe.notes.append(
                    f"Prezzo distante {deviation:.2f}% dalla mediana multi-fonte: possibile simbolo errato."
                )


def source_summary(probes: list[AssetProbe]) -> list[dict[str, Any]]:
    summaries: list[dict[str, Any]] = []
    for exchange in ("kraken", "bitget", "okx", "coinbase", "kucoin"):
        rows = [probe for probe in probes if probe.exchange == exchange]
        if not rows:
            continue
        total_caps = 0
        got_caps = 0
        all_assets_ok = True
        for row in rows:
            got, total = row.capability_count()
            got_caps += got
            total_caps += total
            all_assets_ok = all_assets_ok and row.status == "OK"
        statuses = sorted({row.status for row in rows})
        summaries.append(
            {
                "exchange": exchange,
                "market_type": rows[0].market_type,
                "assets_found": sum(1 for row in rows if row.market_exists),
                "assets_total": len(rows),
                "capabilities_ok": got_caps,
                "capabilities_total": total_caps,
                "coverage_pct": round(got_caps / total_caps * 100.0, 2) if total_caps else 0.0,
                "all_assets_ok": all_assets_ok,
                "statuses": statuses,
            }
        )
    return summaries


def build_recommendation(summaries: list[dict[str, Any]]) -> dict[str, Any]:
    derivative = [
        row
        for row in summaries
        if row["exchange"] in {"kraken", "bitget", "okx"} and row["assets_found"] == row["assets_total"]
    ]
    derivative.sort(key=lambda row: (row["coverage_pct"], row["all_assets_ok"]), reverse=True)
    selected = [row["exchange"] for row in derivative if row["coverage_pct"] >= 70.0 and row["all_assets_ok"]][:2]
    coinbase = next((row for row in summaries if row["exchange"] == "coinbase"), None)
    kucoin = next((row for row in summaries if row["exchange"] == "kucoin"), None)
    if len(selected) >= 2:
        status = "PRONTO PER INTEGRAZIONE SENZA VPS"
        message = f"Nucleo proposto: KuCoin + {selected[0].title()} + {selected[1].title()}."
    elif len(selected) == 1:
        status = "INTEGRAZIONE PARZIALE"
        message = f"KuCoin può essere affiancato da {selected[0].title()}, ma manca ancora una terza fonte derivati completa."
    else:
        status = "TEST INSUFFICIENTE / VPS ANCORA POSSIBILE"
        message = "Nessuna coppia di nuove fonti derivati ha superato la soglia prudente su tutti e tre gli asset."
    return {
        "status": status,
        "message": message,
        "selected_derivatives": selected,
        "coinbase_spot_usable": bool(coinbase and coinbase["assets_found"] == coinbase["assets_total"] and coinbase["coverage_pct"] >= 30.0),
        "kucoin_control_ok": bool(kucoin and kucoin["assets_found"] == kucoin["assets_total"]),
        "important_note": "Coinbase è una conferma spot e non sostituisce funding/open interest dei perpetual.",
    }


def format_number(value: Any, decimals: int = 4) -> str:
    number = safe_float(value)
    if number is None:
        return "n/a"
    if abs(number) >= 1_000_000_000:
        return f"{number / 1_000_000_000:.2f} mld"
    if abs(number) >= 1_000_000:
        return f"{number / 1_000_000:.2f} mln"
    if abs(number) >= 1_000:
        return f"{number:,.2f}"
    return f"{number:.{decimals}f}"


def yes_no(value: Any) -> str:
    return "SI" if bool(value) else "NO"


def write_outputs(probes: list[AssetProbe], started_at: str, finished_at: str) -> dict[str, Any]:
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    summaries = source_summary(probes)
    recommendation = build_recommendation(summaries)
    payload = {
        "schema_version": VERSION,
        "started_at": started_at,
        "finished_at": finished_at,
        "runner_context": {
            "github_actions": os.getenv("GITHUB_ACTIONS", "false"),
            "runner_os": os.getenv("RUNNER_OS", "unknown"),
            "runner_arch": os.getenv("RUNNER_ARCH", "unknown"),
            "repository": os.getenv("GITHUB_REPOSITORY", "unknown"),
        },
        "sources": summaries,
        "recommendation": recommendation,
        "assets": [probe.as_dict() for probe in probes],
    }
    JSON_PATH.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    samples = {
        "schema_version": VERSION,
        "generated_at": finished_at,
        "samples": [
            {
                "exchange": probe.exchange,
                "market_type": probe.market_type,
                "asset": probe.asset,
                "symbol": probe.symbol,
                "status": probe.status,
                "sample": probe.sample,
            }
            for probe in probes
        ],
    }
    SAMPLES_PATH.write_text(json.dumps(samples, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    csv_fields = [
        "exchange",
        "market_type",
        "asset",
        "symbol",
        "status",
        "reachable",
        "market_exists",
        "coverage_pct",
        "price",
        "mark_price",
        "index_price",
        "funding",
        "open_interest",
        "trades",
        "order_book",
        "last_price",
        "funding_rate_raw",
        "open_interest_base_raw",
        "open_interest_usd",
        "taker_buy_sell_ratio",
        "book_imbalance_0_5pct",
        "spread_bps",
    ]
    with CSV_PATH.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=csv_fields)
        writer.writeheader()
        for probe in probes:
            got, total = probe.capability_count()
            writer.writerow(
                {
                    "exchange": probe.exchange,
                    "market_type": probe.market_type,
                    "asset": probe.asset,
                    "symbol": probe.symbol,
                    "status": probe.status,
                    "reachable": probe.reachable,
                    "market_exists": probe.market_exists,
                    "coverage_pct": round(got / total * 100.0, 2) if total else 0.0,
                    "price": probe.capabilities.get("price"),
                    "mark_price": probe.capabilities.get("mark_price"),
                    "index_price": probe.capabilities.get("index_price"),
                    "funding": probe.capabilities.get("funding"),
                    "open_interest": probe.capabilities.get("open_interest"),
                    "trades": probe.capabilities.get("trades"),
                    "order_book": probe.capabilities.get("order_book"),
                    "last_price": probe.sample.get("last_price"),
                    "funding_rate_raw": probe.sample.get("funding_rate_raw"),
                    "open_interest_base_raw": probe.sample.get("open_interest_base_raw"),
                    "open_interest_usd": probe.sample.get("open_interest_usd"),
                    "taker_buy_sell_ratio": probe.sample.get("taker_buy_sell_ratio"),
                    "book_imbalance_0_5pct": probe.sample.get("book_imbalance_0_5pct"),
                    "spread_bps": probe.sample.get("spread_bps"),
                }
            )

    lines: list[str] = []
    lines.append("# Diagnostica fonti exchange alternative — V2.1.2b")
    lines.append("")
    lines.append(f"Generato: **{finished_at}**")
    lines.append("")
    lines.append("Questo test non modifica Global Confluence, Decision Report o previsioni. Verifica soltanto accessibilità, mercati e campi pubblici dal runner GitHub reale.")
    lines.append("")
    lines.append("## Verdetto automatico")
    lines.append("")
    lines.append(f"**{recommendation['status']}** — {recommendation['message']}")
    if recommendation["coinbase_spot_usable"]:
        lines.append("Coinbase spot è utilizzabile come conferma aggiuntiva di book e flusso eseguito.")
    lines.append("")
    lines.append("## Sintesi per fonte")
    lines.append("")
    lines.append("| Fonte | Mercato | Asset trovati | Copertura campi | Stato asset | Lettura |")
    lines.append("| --- | --- | ---: | ---: | --- | --- |")
    for row in summaries:
        reading = "candidato derivati" if row["exchange"] in {"kraken", "bitget", "okx", "kucoin"} else "conferma spot"
        lines.append(
            f"| {row['exchange'].title()} | {row['market_type']} | {row['assets_found']}/{row['assets_total']} | {row['coverage_pct']:.0f}% | {', '.join(row['statuses'])} | {reading} |"
        )
    lines.append("")
    lines.append("## Matrice asset / capacità")
    lines.append("")
    lines.append("| Fonte | Asset | Simbolo | Stato | Prezzo | Mark | Index | Funding | OI | Trade | Book | Copertura |")
    lines.append("| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---: |")
    for probe in probes:
        got, total = probe.capability_count()
        lines.append(
            "| {exchange} | {asset} | {symbol} | {status} | {price} | {mark} | {index} | {funding} | {oi} | {trades} | {book} | {coverage:.0f}% |".format(
                exchange=probe.exchange.title(),
                asset=probe.asset,
                symbol=probe.symbol or "n/a",
                status=probe.status,
                price=yes_no(probe.capabilities.get("price")),
                mark=yes_no(probe.capabilities.get("mark_price")),
                index=yes_no(probe.capabilities.get("index_price")),
                funding=yes_no(probe.capabilities.get("funding")),
                oi=yes_no(probe.capabilities.get("open_interest")),
                trades=yes_no(probe.capabilities.get("trades")),
                book=yes_no(probe.capabilities.get("order_book")),
                coverage=(got / total * 100.0 if total else 0.0),
            )
        )
    lines.append("")
    lines.append("## Campioni principali")
    lines.append("")
    lines.append("| Fonte | Asset | Prezzo | Funding raw | OI base/raw | OI USD normalizzato | Taker B/S | Book 0,5% | Spread bps |")
    lines.append("| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |")
    for probe in probes:
        oi_base = probe.sample.get("open_interest_base_raw")
        if oi_base is None:
            oi_base = probe.sample.get("open_interest_contracts_raw")
        oi_usd = probe.sample.get("open_interest_usd")
        lines.append(
            f"| {probe.exchange.title()} | {probe.asset} | {format_number(probe.sample.get('last_price'), 6)} | {format_number(probe.sample.get('funding_rate_raw'), 8)} | {format_number(oi_base, 4)} | {format_number(oi_usd, 2)} | {format_number(probe.sample.get('taker_buy_sell_ratio'), 3)} | {format_number(probe.sample.get('book_imbalance_0_5pct'), 3)} | {format_number(probe.sample.get('spread_bps'), 2)} |"
        )
    lines.append("")
    lines.append("## Errori e blocchi")
    lines.append("")
    error_rows = []
    for probe in probes:
        for endpoint, info in probe.endpoints.items():
            if not info.get("ok"):
                error_rows.append((probe.exchange, probe.asset, endpoint, info))
    if not error_rows:
        lines.append("Nessun errore HTTP/API rilevato nei test eseguiti.")
    else:
        lines.append("| Fonte | Asset | Endpoint | HTTP | Tipo | Messaggio |")
        lines.append("| --- | --- | --- | ---: | --- | --- |")
        for exchange, asset, endpoint, info in error_rows:
            message = info.get("response_snippet") or info.get("error") or "n/a"
            lines.append(
                f"| {exchange.title()} | {asset} | {endpoint} | {info.get('status_code') or 'n/a'} | {info.get('error_kind') or 'n/a'} | {sanitize_text(message, 120)} |"
            )
    lines.append("")
    lines.append("## Regole per la scelta finale")
    lines.append("")
    lines.append("- Una fonte derivati è candidata soltanto se trova BTC, SOL e DOGE e restituisce almeno prezzo, funding, OI, trade e order book.")
    lines.append("- Kraken, Bitget e OKX possono sostituire Binance/Bybit solo dopo questo test reale sul runner GitHub.")
    lines.append("- Coinbase resta una conferma spot: non viene contato come fonte di funding o open interest.")
    lines.append("- KuCoin è il controllo già operativo.")
    lines.append("- Nessun peso exchange viene attivato da questo workflow diagnostico.")
    lines.append("")
    lines.append("File tecnici: `alternative_exchange_source_diagnostics.json`, `alternative_exchange_source_capabilities.csv`, `alternative_exchange_source_samples.json`.")
    MD_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return payload


def run_probe() -> dict[str, Any]:
    started = utc_now_iso()
    session = build_session()
    probes: list[AssetProbe] = []
    source_functions = [
        ("Kraken", probe_kraken),
        ("Bitget", probe_bitget),
        ("OKX", probe_okx),
        ("Coinbase", probe_coinbase),
        ("KuCoin control", probe_kucoin_control),
    ]
    for label, function in source_functions:
        print(f"[probe] {label}...", flush=True)
        try:
            probes.extend(function(session))
        except Exception as exc:
            print(f"[probe] {label} fatal parser error: {type(exc).__name__}: {exc}", file=sys.stderr, flush=True)
            market_type = "spot" if label == "Coinbase" else "perpetual"
            exchange = label.lower().split()[0]
            for asset in ASSETS:
                probe = AssetProbe(exchange, market_type, asset, status="PARSER_ERROR")
                probe.capabilities = base_capabilities(market_type)
                probe.notes.append(f"{type(exc).__name__}: {exc}")
                probes.append(probe)
    apply_cross_source_price_sanity(probes)
    finished = utc_now_iso()
    return write_outputs(probes, started, finished)


def main() -> int:
    parser = argparse.ArgumentParser(description="Probe alternative public exchange data sources.")
    parser.add_argument("--strict", action="store_true", help="Return non-zero if fewer than two alternative derivatives sources qualify.")
    args = parser.parse_args()
    payload = run_probe()
    recommendation = payload.get("recommendation", {})
    print("\n=== VERDETTO ===")
    print(recommendation.get("status"))
    print(recommendation.get("message"))
    print(f"Report: {MD_PATH}")
    if args.strict and len(recommendation.get("selected_derivatives", [])) < 2:
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
