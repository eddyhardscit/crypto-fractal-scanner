# -*- coding: utf-8 -*-
"""Collect public exchange microstructure data without account credentials.

Primary derivative sources used by the scoring model:
- Kraken Futures
- Bitget Futures
- KuCoin Futures

Auxiliary, non-scoring confirmations:
- OKX perpetual swaps
- Coinbase spot

All funding rates are normalized to an 8-hour percentage before aggregation.
The first recent-trade observation is only a sample; the report replaces it with
rolling 4h/24h averages after enough intraday snapshots have accumulated.
"""

from __future__ import annotations

import csv
import json
import math
import os
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Iterable

import alternative_exchange_sources as alt

REPORTS_DIR = Path("reports")
SCHEMA_VERSION = "2.1.3"
SNAPSHOT_PATH = REPORTS_DIR / "exchange_market_data_snapshot.json"
HEALTH_PATH = REPORTS_DIR / "exchange_market_data_health.json"
RAW_PATH = REPORTS_DIR / "exchange_market_data_raw.json"
INTRADAY_HISTORY_PATH = REPORTS_DIR / "exchange_market_data_intraday.csv"
SHARED_SNAPSHOT_PATH = REPORTS_DIR / "shared_market_snapshot.json"

ASSETS = ("BTC", "SOL", "DOGE")
PRIMARY_EXCHANGES = ("kraken", "bitget", "kucoin")
AUXILIARY_EXCHANGES = ("okx", "coinbase")
INTRADAY_RETENTION_DAYS = max(30, min(730, int(os.getenv("EXCHANGE_INTRADAY_RETENTION_DAYS", "180"))))
COLLECTOR_MODE = os.getenv("EXCHANGE_COLLECTOR_MODE", "github-hosted-alternative-sources").strip() or "github-hosted-alternative-sources"


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


def mean(values: Iterable[Any]) -> float | None:
    parsed = [safe_float(value) for value in values]
    parsed = [value for value in parsed if value is not None]
    return sum(parsed) / len(parsed) if parsed else None


def median(values: Iterable[Any]) -> float | None:
    parsed = sorted(value for value in (safe_float(item) for item in values) if value is not None)
    if not parsed:
        return None
    middle = len(parsed) // 2
    return parsed[middle] if len(parsed) % 2 else (parsed[middle - 1] + parsed[middle]) / 2.0


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
    total = sum(weight for _, weight in parsed)
    return sum(value * weight for value, weight in parsed) / total if total > 0 else None


def pct_change(new: Any, old: Any) -> float | None:
    new_f = safe_float(new)
    old_f = safe_float(old)
    if new_f is None or old_f in (None, 0):
        return None
    return (new_f / old_f - 1.0) * 100.0


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


def shared_price(asset: str) -> float | None:
    payload = load_json(SHARED_SNAPSHOT_PATH)
    assets = payload.get("assets") if isinstance(payload.get("assets"), dict) else {}
    row = assets.get(asset) if isinstance(assets, dict) else None
    if isinstance(row, dict):
        return safe_float(row.get("price") or row.get("current_price") or row.get("close"))
    # Backward-compatible fallback for flat snapshots.
    for key in (asset, f"{asset}-USD", f"{asset}USDT"):
        row = payload.get(key)
        if isinstance(row, dict):
            value = safe_float(row.get("price") or row.get("current_price") or row.get("close"))
            if value is not None:
                return value
    return None


def normalize_funding_8h_pct(exchange: str, sample: dict[str, Any]) -> float | None:
    raw = safe_float(sample.get("funding_rate_raw"))
    if raw is None:
        return None
    if exchange == "kraken":
        # Kraken REST ticker exposes an absolute USD funding amount per one base
        # unit per hour. Divide by index/mark to obtain the relative hourly rate,
        # then standardize to an 8-hour percentage.
        reference = safe_float(sample.get("index_price")) or safe_float(sample.get("mark_price")) or safe_float(sample.get("last_price"))
        if reference in (None, 0):
            return None
        return raw / reference * 8.0 * 100.0
    interval = safe_float(sample.get("funding_interval_hours")) or 8.0
    if interval <= 0:
        interval = 8.0
    # Bitget and KuCoin return decimal rates for their settlement interval.
    return raw * (8.0 / interval) * 100.0


def probe_to_parsed(probe: alt.AssetProbe) -> dict[str, Any]:
    sample = probe.sample if isinstance(probe.sample, dict) else {}
    last = safe_float(sample.get("last_price"))
    mark = safe_float(sample.get("mark_price")) or last
    index = safe_float(sample.get("index_price"))
    oi_usd = safe_float(sample.get("open_interest_usd"))
    bid_depth = safe_float(sample.get("bid_depth_0_5pct_usd"))
    ask_depth = safe_float(sample.get("ask_depth_0_5pct_usd"))
    imbalance = safe_float(sample.get("book_imbalance_0_5pct"))
    funding_8h_pct = normalize_funding_8h_pct(probe.exchange, sample)
    basis = (mark / index - 1.0) * 100.0 if mark is not None and index not in (None, 0) else None
    return {
        "available": probe.status == "OK",
        "source_state": probe.status,
        "symbol": probe.symbol,
        "market_type": probe.market_type,
        "last_price": last,
        "mark_price": mark,
        "index_price": index,
        "basis_pct": basis,
        "funding_rate_pct": funding_8h_pct,
        "funding_rate_raw": safe_float(sample.get("funding_rate_raw")),
        "funding_interval_hours": safe_float(sample.get("funding_interval_hours")),
        "price_change_24h_pct": safe_float(sample.get("price_change_24h_pct")),
        "open_interest_base": safe_float(sample.get("open_interest_base_raw")),
        "open_interest_usd": oi_usd,
        "oi_change_4h_pct": None,
        "oi_change_24h_pct": None,
        "global_long_short_ratio": None,
        "top_account_long_short_ratio": None,
        "top_position_long_short_ratio": None,
        "taker_buy_sell_ratio_recent": safe_float(sample.get("taker_buy_sell_ratio")),
        "taker_buy_notional_recent": safe_float(sample.get("taker_buy_notional")),
        "taker_sell_notional_recent": safe_float(sample.get("taker_sell_notional")),
        "recent_trade_count": safe_int(sample.get("trade_count")),
        "orderbook": {
            "imbalance_0_25pct": None,
            "imbalance_0_5pct": imbalance,
            "imbalance_1_0pct": None,
            "imbalance_2_0pct": None,
            "bid_notional_0_5pct": bid_depth,
            "ask_notional_0_5pct": ask_depth,
            "spread_bps": safe_float(sample.get("spread_bps")),
            "largest_bid_wall": {},
            "largest_ask_wall": {},
        },
        "capabilities": dict(probe.capabilities),
        "notes": list(probe.notes),
    }


def direction_consensus(values: Iterable[Any], bullish_threshold: float, bearish_threshold: float) -> dict[str, Any]:
    parsed = [safe_float(value) for value in values]
    parsed = [value for value in parsed if value is not None]
    bullish = sum(value >= bullish_threshold for value in parsed)
    bearish = sum(value <= bearish_threshold for value in parsed)
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


def combined_book(exchanges: list[dict[str, Any]]) -> dict[str, Any]:
    books = [row.get("orderbook", {}) for row in exchanges if isinstance(row.get("orderbook"), dict)]
    bid = sum(value for value in (safe_float(book.get("bid_notional_0_5pct")) for book in books) if value is not None)
    ask = sum(value for value in (safe_float(book.get("ask_notional_0_5pct")) for book in books) if value is not None)
    total = bid + ask
    return {
        "bid_notional_0_5pct": bid or None,
        "ask_notional_0_5pct": ask or None,
        "imbalance_0_5pct": (bid - ask) / total if total > 0 else None,
        "spread_bps": median(book.get("spread_bps") for book in books),
    }


def spot_confirmation(coinbase: dict[str, Any]) -> dict[str, Any]:
    book = coinbase.get("orderbook", {}) if isinstance(coinbase.get("orderbook"), dict) else {}
    ratio = safe_float(coinbase.get("taker_buy_sell_ratio_recent"))
    imbalance = safe_float(book.get("imbalance_0_5pct"))
    votes = []
    if ratio is not None:
        votes.append(1 if ratio >= 1.08 else -1 if ratio <= 0.92 else 0)
    if imbalance is not None:
        votes.append(1 if imbalance >= 0.08 else -1 if imbalance <= -0.08 else 0)
    score = sum(votes)
    label = "POSITIVA" if score >= 1 else "NEGATIVA" if score <= -1 else "MISTA / NEUTRALE"
    return {"label": label, "score": score, "taker_ratio": ratio, "book_imbalance_0_5pct": imbalance}


def combine_asset(asset: str, source_rows: dict[str, dict[str, Any]]) -> dict[str, Any]:
    primary = [source_rows[name] for name in PRIMARY_EXCHANGES]
    auxiliary = {name: source_rows[name] for name in AUXILIARY_EXCHANGES}
    price = shared_price(asset) or median(
        [row.get("mark_price") or row.get("last_price") for row in primary if row.get("available")]
    )
    book = combined_book(primary)
    available = {name: bool(source_rows[name].get("available")) for name in PRIMARY_EXCHANGES}
    exchange_count = sum(available.values())

    supported_slots = {"funding": 3, "basis": 3, "open_interest": 3, "taker_flow": 3, "orderbook": 3}
    available_counts = {
        "funding": sum(safe_float(row.get("funding_rate_pct")) is not None for row in primary),
        "basis": sum(safe_float(row.get("basis_pct")) is not None for row in primary),
        "open_interest": sum(safe_float(row.get("open_interest_usd")) is not None for row in primary),
        "taker_flow": sum(safe_float(row.get("taker_buy_sell_ratio_recent")) is not None for row in primary),
        "orderbook": sum(safe_float((row.get("orderbook") or {}).get("imbalance_0_5pct")) is not None for row in primary),
        "long_short": 0,
    }
    total_slots = sum(supported_slots.values())
    coverage = sum(min(available_counts[key], slots) for key, slots in supported_slots.items()) / total_slots

    combined_oi = sum(value for value in (safe_float(row.get("open_interest_usd")) for row in primary) if value is not None and value > 0) or None
    funding = weighted_mean((row.get("funding_rate_pct"), row.get("open_interest_usd")) for row in primary)
    if funding is None:
        funding = mean(row.get("funding_rate_pct") for row in primary)
    basis = weighted_mean((row.get("basis_pct"), row.get("open_interest_usd")) for row in primary)
    if basis is None:
        basis = mean(row.get("basis_pct") for row in primary)
    flow_values = [row.get("taker_buy_sell_ratio_recent") for row in primary]

    consensus = {
        # Positive funding is a crowding headwind, hence the sign inversion.
        "funding": direction_consensus(
            [-(safe_float(row.get("funding_rate_pct")) or 0.0) if safe_float(row.get("funding_rate_pct")) is not None else None for row in primary],
            0.01,
            -0.01,
        ),
        "oi_24h": direction_consensus([row.get("oi_change_24h_pct") for row in primary], 2.0, -2.0),
        "taker_flow": direction_consensus(flow_values, 1.05, 0.95),
        "orderbook": direction_consensus([(row.get("orderbook") or {}).get("imbalance_0_5pct") for row in primary], 0.05, -0.05),
    }
    labels = [value["label"] for value in consensus.values()]
    coinbase_confirmation = spot_confirmation(auxiliary["coinbase"])

    return {
        "asset": asset,
        "price": price,
        "generated_utc": utc_now_iso(),
        "data_coverage": coverage,
        "exchange_count": exchange_count,
        "exchange_available": available,
        "available_counts": available_counts,
        "available_fields": {
            **available,
            "funding": available_counts["funding"] > 0,
            "open_interest": available_counts["open_interest"] > 0,
            "taker_flow": available_counts["taker_flow"] > 0,
            "long_short": False,
            "orderbook": available_counts["orderbook"] > 0,
            "liquidation_stream": False,
        },
        "funding_rate_pct": funding,
        "funding_normalization": "8h_equivalent_pct",
        "basis_pct": basis,
        "price_change_24h_pct": median(row.get("price_change_24h_pct") for row in primary),
        "open_interest_usd_combined": combined_oi,
        "oi_change_4h_pct": None,
        "oi_change_24h_pct": None,
        "global_long_short_ratio": None,
        "top_account_long_short_ratio": None,
        "top_position_long_short_ratio": None,
        "taker_buy_sell_ratio_1h": None,
        "taker_buy_sell_ratio_4h": median(flow_values),
        "taker_buy_sell_ratio_24h": None,
        "orderbook_imbalance_0_25pct": None,
        "orderbook_imbalance_0_5pct": book.get("imbalance_0_5pct"),
        "orderbook_imbalance_1_0pct": None,
        "orderbook_imbalance_2_0pct": None,
        "orderbook_bid_notional_0_5pct": book.get("bid_notional_0_5pct"),
        "orderbook_ask_notional_0_5pct": book.get("ask_notional_0_5pct"),
        "spread_bps": book.get("spread_bps"),
        "exchange_consensus": consensus,
        "bullish_consensus_count": sum(label == "BULLISH_CONSENSUS" for label in labels),
        "bearish_consensus_count": sum(label == "BEARISH_CONSENSUS" for label in labels),
        "divergent_metric_count": sum(label == "DIVERGENT" for label in labels),
        "liquidation_sample": {
            "events": 0,
            "long_liquidation_usd": 0.0,
            "short_liquidation_usd": 0.0,
            "total_liquidation_usd": 0.0,
            "largest_event_usd": 0.0,
        },
        "exchanges": {name: source_rows[name] for name in PRIMARY_EXCHANGES},
        "auxiliary_sources": auxiliary,
        "spot_confirmation": coinbase_confirmation,
    }


# Keep old fields so the existing rolling CSV is migrated without deleting its
# first few historical Binance/Bybit observations.
INTRADAY_FIELDS = [
    "schema_version", "timestamp_utc", "snapshot_date", "asset", "price", "data_coverage", "exchange_count",
    "kraken_available", "bitget_available", "kucoin_available", "okx_available", "coinbase_available",
    "funding_rate_pct", "basis_pct", "price_change_24h_pct", "open_interest_usd_combined",
    "oi_change_4h_pct", "oi_change_24h_pct", "global_long_short_ratio",
    "taker_buy_sell_ratio_1h", "taker_buy_sell_ratio_4h", "taker_buy_sell_ratio_24h",
    "orderbook_imbalance_0_25pct", "orderbook_imbalance_0_5pct", "orderbook_imbalance_1_0pct",
    "orderbook_bid_notional_0_5pct", "orderbook_ask_notional_0_5pct", "spread_bps",
    "long_liquidation_usd_sample", "short_liquidation_usd_sample", "liquidation_events_sample",
    "kraken_funding_rate_pct", "bitget_funding_rate_pct", "kucoin_funding_rate_pct",
    "kraken_open_interest_usd", "bitget_open_interest_usd", "kucoin_open_interest_usd",
    "kraken_taker_ratio", "bitget_taker_ratio", "kucoin_taker_ratio",
    "kraken_book_imbalance_0_5pct", "bitget_book_imbalance_0_5pct", "kucoin_book_imbalance_0_5pct",
    "okx_taker_ratio", "okx_book_imbalance_0_5pct", "coinbase_taker_ratio", "coinbase_book_imbalance_0_5pct",
    # Legacy columns retained during migration.
    "binance_available", "bybit_available", "binance_funding_rate_pct", "bybit_funding_rate_pct",
    "binance_open_interest_usd", "bybit_open_interest_usd", "binance_taker_ratio", "bybit_taker_ratio",
    "binance_book_imbalance_0_5pct", "bybit_book_imbalance_0_5pct",
]


def iso_datetime(value: Any) -> datetime | None:
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


def intraday_row(timestamp: str, snapshot_date: str, asset: str, row: dict[str, Any]) -> dict[str, Any]:
    exchanges = row.get("exchanges", {}) if isinstance(row.get("exchanges"), dict) else {}
    auxiliary = row.get("auxiliary_sources", {}) if isinstance(row.get("auxiliary_sources"), dict) else {}
    available = row.get("exchange_available", {}) if isinstance(row.get("exchange_available"), dict) else {}
    liq = row.get("liquidation_sample", {}) if isinstance(row.get("liquidation_sample"), dict) else {}
    output: dict[str, Any] = {
        "schema_version": SCHEMA_VERSION,
        "timestamp_utc": timestamp,
        "snapshot_date": snapshot_date,
        "asset": asset,
        "price": row.get("price"),
        "data_coverage": row.get("data_coverage"),
        "exchange_count": row.get("exchange_count"),
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
    }
    for exchange in PRIMARY_EXCHANGES:
        ex = exchanges.get(exchange, {}) if isinstance(exchanges.get(exchange), dict) else {}
        book = ex.get("orderbook", {}) if isinstance(ex.get("orderbook"), dict) else {}
        output[f"{exchange}_available"] = bool(available.get(exchange))
        output[f"{exchange}_funding_rate_pct"] = ex.get("funding_rate_pct")
        output[f"{exchange}_open_interest_usd"] = ex.get("open_interest_usd")
        output[f"{exchange}_taker_ratio"] = ex.get("taker_buy_sell_ratio_recent")
        output[f"{exchange}_book_imbalance_0_5pct"] = book.get("imbalance_0_5pct")
    for exchange in AUXILIARY_EXCHANGES:
        ex = auxiliary.get(exchange, {}) if isinstance(auxiliary.get(exchange), dict) else {}
        book = ex.get("orderbook", {}) if isinstance(ex.get("orderbook"), dict) else {}
        output[f"{exchange}_available"] = bool(ex.get("available"))
        output[f"{exchange}_taker_ratio"] = ex.get("taker_buy_sell_ratio_recent")
        output[f"{exchange}_book_imbalance_0_5pct"] = book.get("imbalance_0_5pct")
    return output


def append_intraday_history(snapshot: dict[str, Any]) -> None:
    timestamp = str(snapshot.get("generated_utc") or utc_now_iso())
    snapshot_date = str(snapshot.get("snapshot_date") or utc_date())
    assets = snapshot.get("assets", {}) if isinstance(snapshot.get("assets"), dict) else {}
    new_rows = [intraday_row(timestamp, snapshot_date, asset, row) for asset, row in assets.items() if asset in ASSETS and isinstance(row, dict)]
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
    seen: set[tuple[str, str]] = set()
    kept: list[dict[str, Any]] = []
    for row in existing + new_rows:
        row_time = iso_datetime(row.get("timestamp_utc"))
        if row_time is not None and row_time < cutoff:
            continue
        key = (str(row.get("timestamp_utc", "")), str(row.get("asset", "")))
        if key in seen:
            continue
        seen.add(key)
        kept.append({field: row.get(field, "") for field in INTRADAY_FIELDS})
    kept.sort(key=lambda item: (str(item.get("timestamp_utc", "")), str(item.get("asset", ""))))
    INTRADAY_HISTORY_PATH.parent.mkdir(parents=True, exist_ok=True)
    tmp = INTRADAY_HISTORY_PATH.with_suffix(".csv.tmp")
    with tmp.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=INTRADAY_FIELDS)
        writer.writeheader()
        writer.writerows(kept)
    tmp.replace(INTRADAY_HISTORY_PATH)


def fixture_mode() -> dict[str, Any] | None:
    value = os.getenv("EXCHANGE_TEST_FIXTURE", "").strip()
    if not value:
        return None
    payload = json.loads(Path(value).read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise RuntimeError("EXCHANGE_TEST_FIXTURE must contain a JSON object")
    return payload


def probe_health(probe: alt.AssetProbe) -> dict[str, Any]:
    return {name: dict(record) for name, record in probe.endpoints.items()}


def main() -> None:
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    fixture = fixture_mode()
    if fixture is not None:
        atomic_json(SNAPSHOT_PATH, fixture)
        append_intraday_history(fixture)
        atomic_json(HEALTH_PATH, {"schema_version": SCHEMA_VERSION, "generated_utc": utc_now_iso(), "fixture": True, "status": "OK"})
        atomic_json(RAW_PATH, {"fixture": True})
        print(f"Fixture exchange scritto in {SNAPSHOT_PATH}")
        return

    session = alt.build_session()
    probes = (
        alt.probe_kraken(session)
        + alt.probe_bitget(session)
        + alt.probe_kucoin_control(session)
        + alt.probe_okx(session)
        + alt.probe_coinbase(session)
    )
    alt.apply_cross_source_price_sanity(probes)
    probe_map = {(probe.exchange, probe.asset): probe for probe in probes}

    assets: dict[str, Any] = {}
    health_assets: dict[str, Any] = {}
    raw_assets: dict[str, Any] = {}
    for asset in ASSETS:
        source_rows: dict[str, dict[str, Any]] = {}
        health_assets[asset] = {}
        raw_assets[asset] = {}
        for exchange in PRIMARY_EXCHANGES + AUXILIARY_EXCHANGES:
            probe = probe_map[(exchange, asset)]
            source_rows[exchange] = probe_to_parsed(probe)
            health_assets[asset][exchange] = probe_health(probe)
            raw_assets[asset][exchange] = probe.as_dict()
        assets[asset] = combine_asset(asset, source_rows)

    primary_pairs = sum(
        1 for asset in ASSETS for exchange in PRIMARY_EXCHANGES
        if assets[asset]["exchange_available"].get(exchange)
    )
    auxiliary_pairs = sum(
        1 for asset in ASSETS for exchange in AUXILIARY_EXCHANGES
        if assets[asset]["auxiliary_sources"].get(exchange, {}).get("available")
    )
    exchange_status: dict[str, str] = {}
    for exchange in PRIMARY_EXCHANGES + AUXILIARY_EXCHANGES:
        states = [probe_map[(exchange, asset)].status for asset in ASSETS]
        exchange_status[exchange] = "OK" if all(state == "OK" for state in states) else ("PARZIALE" if any(state in {"OK", "PARZIALE"} for state in states) else states[0])

    snapshot = {
        "schema_version": SCHEMA_VERSION,
        "generated_utc": utc_now_iso(),
        "snapshot_date": utc_date(),
        "liquidation_sample_seconds": 0,
        "collector_mode": COLLECTOR_MODE,
        "primary_derivative_exchanges": list(PRIMARY_EXCHANGES),
        "auxiliary_exchanges": list(AUXILIARY_EXCHANGES),
        "assets": assets,
        "notes": {
            "funding": "All primary funding rates are normalized to an 8-hour percentage before aggregation.",
            "taker_flow": "Recent public trades are a sample; rolling intraday averages replace the first sample after enough observations.",
            "liquidations": "No complete public all-market liquidation stream is assumed for these sources; liquidation score remains neutral.",
            "auxiliary": "OKX and Coinbase are collected for diagnostics/confirmation and are not counted in the initial Global candidate.",
        },
    }
    health = {
        "schema_version": SCHEMA_VERSION,
        "generated_utc": utc_now_iso(),
        "collector_mode": COLLECTOR_MODE,
        "status": "OK" if primary_pairs == len(ASSETS) * len(PRIMARY_EXCHANGES) else "WARN",
        "available_exchange_asset_pairs": primary_pairs,
        "total_exchange_asset_pairs": len(ASSETS) * len(PRIMARY_EXCHANGES),
        "available_auxiliary_asset_pairs": auxiliary_pairs,
        "total_auxiliary_asset_pairs": len(ASSETS) * len(AUXILIARY_EXCHANGES),
        "exchange_status": exchange_status,
        "assets": health_assets,
        "liquidation_streams": {
            "kraken": {"ok": False, "state": "NOT_USED", "messages": 0, "error": "Feed completo non assunto disponibile nel collector V2.1.3."},
            "bitget": {"ok": False, "state": "NOT_USED", "messages": 0, "error": "Feed completo non assunto disponibile nel collector V2.1.3."},
        },
    }

    atomic_json(SNAPSHOT_PATH, snapshot)
    append_intraday_history(snapshot)
    atomic_json(HEALTH_PATH, health)
    atomic_json(RAW_PATH, {"schema_version": SCHEMA_VERSION, "generated_utc": utc_now_iso(), "assets": raw_assets})

    print(f"Exchange snapshot scritto in: {SNAPSHOT_PATH}")
    print(f"Exchange health scritto in: {HEALTH_PATH}")
    print(f"Exchange raw scritto in: {RAW_PATH}")
    print(f"Exchange intraday history scritto in: {INTRADAY_HISTORY_PATH}")
    print(f"Primary source health: {health['status']} ({primary_pairs}/{len(ASSETS) * len(PRIMARY_EXCHANGES)} coppie)")
    print(f"Auxiliary source health: {auxiliary_pairs}/{len(ASSETS) * len(AUXILIARY_EXCHANGES)} coppie")


if __name__ == "__main__":
    main()
