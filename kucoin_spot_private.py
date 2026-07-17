# -*- coding: utf-8 -*-
"""Minimal KuCoin Spot private REST client used by sol_spot_live_guarded.py."""

from __future__ import annotations

import base64
import hashlib
import hmac
import json
import os
import time
import urllib.parse
from decimal import Decimal, ROUND_DOWN
from typing import Any

import requests


class KuCoinAPIError(RuntimeError):
    pass


def decimal_text(value: Any) -> str:
    number = Decimal(str(value))
    text = format(number, "f")
    if "." in text:
        text = text.rstrip("0").rstrip(".")
    return text or "0"


def floor_to_increment(value: Decimal, increment: Decimal) -> Decimal:
    if increment <= 0:
        raise ValueError("Increment must be positive.")
    units = (value / increment).to_integral_value(rounding=ROUND_DOWN)
    return units * increment


class KuCoinSpotClient:
    def __init__(self) -> None:
        self.base_url = os.getenv("KUCOIN_SPOT_BASE_URL", "https://api.kucoin.com").rstrip("/")
        self.api_key = os.environ["KUCOIN_LIVE_API_KEY"].strip()
        self.api_secret = os.environ["KUCOIN_LIVE_API_SECRET"].strip()
        self.api_passphrase = os.environ["KUCOIN_LIVE_API_PASSPHRASE"].strip()
        self.api_key_version = os.getenv("KUCOIN_API_KEY_VERSION", "2").strip()
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": "crypto-fractal-scanner-sol-live/1.0"})

    def _headers(self, method: str, endpoint_with_query: str, body_text: str) -> dict[str, str]:
        timestamp = str(int(time.time() * 1000))
        prehash = f"{timestamp}{method.upper()}{endpoint_with_query}{body_text}"
        signature = base64.b64encode(
            hmac.new(self.api_secret.encode(), prehash.encode(), hashlib.sha256).digest()
        ).decode()
        passphrase = base64.b64encode(
            hmac.new(
                self.api_secret.encode(),
                self.api_passphrase.encode(),
                hashlib.sha256,
            ).digest()
        ).decode()
        return {
            "KC-API-KEY": self.api_key,
            "KC-API-SIGN": signature,
            "KC-API-TIMESTAMP": timestamp,
            "KC-API-PASSPHRASE": passphrase,
            "KC-API-KEY-VERSION": self.api_key_version,
            "Content-Type": "application/json",
        }

    def _request(
        self,
        method: str,
        endpoint: str,
        *,
        params: dict[str, Any] | None = None,
        payload: dict[str, Any] | None = None,
        private: bool = True,
    ) -> Any:
        query = urllib.parse.urlencode(params or {})
        endpoint_with_query = endpoint + (f"?{query}" if query else "")
        body_text = json.dumps(payload, separators=(",", ":"), ensure_ascii=False) if payload else ""
        headers = self._headers(method, endpoint_with_query, body_text) if private else {}
        response = self.session.request(
            method,
            self.base_url + endpoint_with_query,
            data=body_text or None,
            headers=headers,
            timeout=25,
        )
        try:
            data = response.json()
        except Exception as exc:
            raise KuCoinAPIError(f"Risposta KuCoin non JSON: HTTP {response.status_code}") from exc
        if response.status_code >= 400 or data.get("code") != "200000":
            raise KuCoinAPIError(
                f"KuCoin {method} {endpoint}: HTTP {response.status_code}, "
                f"code={data.get('code')}, msg={data.get('msg')}"
            )
        return data.get("data")

    def balances(self) -> dict[str, dict[str, Decimal]]:
        rows = self._request("GET", "/api/v1/accounts")
        result: dict[str, dict[str, Decimal]] = {}
        for row in rows or []:
            if str(row.get("type", "")).lower() != "trade":
                continue
            currency = str(row.get("currency", "")).upper()
            result[currency] = {
                "balance": Decimal(str(row.get("balance", "0"))),
                "available": Decimal(str(row.get("available", "0"))),
                "holds": Decimal(str(row.get("holds", "0"))),
            }
        return result

    def get_ticker(self, symbol: str) -> dict[str, Any]:
        return self._request(
            "GET",
            "/api/v1/market/orderbook/level1",
            params={"symbol": symbol},
            private=False,
        )

    def get_symbol(self, symbol: str) -> dict[str, Any]:
        rows = self._request("GET", "/api/v2/symbols", private=False)
        for row in rows or []:
            if row.get("symbol") == symbol:
                return row
        raise KuCoinAPIError(f"Metadati simbolo non trovati: {symbol}")

    # Alias retained for compatibility with different runner revisions.
    symbol = get_symbol
    symbol_info = get_symbol

    def _order_payload(
        self,
        *,
        symbol: str,
        side: str,
        funds: Any = None,
        size: Any = None,
        client_oid: str,
    ) -> dict[str, Any]:
        payload: dict[str, Any] = {
            "clientOid": client_oid,
            "symbol": symbol,
            "side": side.lower(),
            "type": "market",
        }
        if funds is not None:
            payload["funds"] = decimal_text(funds)
        if size is not None:
            payload["size"] = decimal_text(size)
        if ("funds" in payload) == ("size" in payload):
            raise KuCoinAPIError("Un ordine market deve avere esattamente uno tra funds e size.")
        return payload

    def test_market_order(self, **kwargs: Any) -> dict[str, Any]:
        payload = self._order_payload(**kwargs)
        return self._request("POST", "/api/v1/hf/orders/test", payload=payload)

    def place_market_order(self, **kwargs: Any) -> dict[str, Any]:
        payload = self._order_payload(**kwargs)
        return self._request("POST", "/api/v1/hf/orders", payload=payload)

    def get_order_by_client_oid(self, *, client_oid: str, symbol: str | None = None) -> dict[str, Any]:
        params = {"symbol": symbol} if symbol else None
        return self._request(
            "GET",
            f"/api/v1/hf/orders/client-order/{urllib.parse.quote(client_oid)}",
            params=params,
        )
