# -*- coding: utf-8 -*-
"""Offline parser/math self-test for alternative_exchange_sources.py."""
from __future__ import annotations

from alternative_exchange_sources import (
    AssetProbe,
    base_capabilities,
    book_metrics,
    build_recommendation,
    classify_http_error,
    select_kraken_symbols,
    source_summary,
    trade_metrics,
)


def main() -> int:
    assert classify_http_error(451, "restricted location") == "GEO_BLOCKED"
    assert classify_http_error(403, "CloudFront country access denied") == "GEO_BLOCKED"
    assert classify_http_error(429, "too many") == "RATE_LIMITED"

    book = book_metrics(
        [[99.9, 2], [99.7, 3]],
        [[100.1, 1], [100.3, 4]],
        100.0,
    )
    assert book["levels_bid"] == 2
    assert book["levels_ask"] == 2
    assert book["spread_bps"] is not None and 19 < book["spread_bps"] < 21
    assert book["book_imbalance_0_5pct"] is not None

    rows = [
        {"side": "buy", "price": "100", "size": "2"},
        {"side": "sell", "price": "100", "size": "1"},
    ]
    trades = trade_metrics(
        rows,
        side_getter=lambda r: r["side"],
        price_getter=lambda r: r["price"],
        size_getter=lambda r: r["size"],
    )
    assert trades["trade_count"] == 2
    assert abs(trades["taker_buy_sell_ratio"] - 2.0) < 1e-9

    instruments = [
        {"symbol": "PI_XBTUSD", "base": "XBT", "quote": "USD", "type": "futures_inverse", "tradeable": True, "isExpired": False},
        {"symbol": "PF_XBTUSD", "base": "XBT", "quote": "USD", "type": "flexible_futures", "tradeable": True, "isExpired": False},
        {"symbol": "PF_SOLUSD", "base": "SOL", "quote": "USD", "type": "flexible_futures", "tradeable": True, "isExpired": False},
        {"symbol": "PF_DOGEUSD", "base": "DOGE", "quote": "USD", "type": "flexible_futures", "tradeable": True, "isExpired": False},
    ]
    selected = select_kraken_symbols(instruments)
    assert selected == {"BTC": "PF_XBTUSD", "SOL": "PF_SOLUSD", "DOGE": "PF_DOGEUSD"}

    probes = []
    for exchange in ("kraken", "bitget", "kucoin"):
        for asset in ("BTC", "SOL", "DOGE"):
            probe = AssetProbe(exchange, "perpetual", asset, symbol=f"{asset}-TEST", status="OK", reachable=True, market_exists=True)
            probe.capabilities = base_capabilities("perpetual")
            probe.capabilities.update({name: True for name in ("price", "mark_price", "index_price", "funding", "open_interest", "trades", "order_book")})
            probes.append(probe)
    summaries = source_summary(probes)
    rec = build_recommendation(summaries)
    assert rec["status"] == "PRONTO PER INTEGRAZIONE SENZA VPS"
    assert len(rec["selected_derivatives"]) == 2

    print("alternative_exchange_sources_selftest: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
