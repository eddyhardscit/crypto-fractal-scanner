from __future__ import annotations

import argparse
import csv
import math
import os
import tempfile
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

import pandas as pd

from kucoin_public_data import (
    fetch_active_contracts,
    fetch_klines,
    make_session,
)


ROOT = Path(__file__).resolve().parent
INPUT_PATH = ROOT / "reports" / "research_all_signals_trades.csv"
OUTPUT_PATH = ROOT / "reports" / "research_all_signals_excursions.csv"

TARGET_STRATEGY = "combo_adaptive"
ALGORITHM_VERSION = "HISTORICAL_OHLC_1H_CONSERVATIVE_V1"

OUTPUT_FIELDS = [
    "source_row",
    "strategy",
    "asset",
    "symbol",
    "side",
    "opened_at",
    "closed_at",
    "timeframe_minutes",
    "entry_price",
    "exit_price",
    "max_favorable_price",
    "max_adverse_price",
    "mfe_gross_eur",
    "mae_gross_eur",
    "mfe_net_eur",
    "mae_net_eur",
    "mfe_at_utc",
    "mae_at_utc",
    "full_candles_used",
    "excursion_quality",
    "algorithm_version",
    "generated_utc",
]


def number(value: Any) -> float | None:
    try:
        result = float(str(value).strip())
    except Exception:
        return None

    return result if math.isfinite(result) else None


def utc_timestamp(value: Any) -> pd.Timestamp:
    result = pd.Timestamp(value)

    if result.tzinfo is None:
        return result.tz_localize("UTC")

    return result.tz_convert("UTC")


def iso(value: pd.Timestamp) -> str:
    return value.tz_convert("UTC").isoformat()


def normalize_frame(frame: pd.DataFrame) -> pd.DataFrame:
    if frame is None or frame.empty:
        return pd.DataFrame()

    result = frame.copy()
    lower = {str(column).lower(): column for column in result.columns}

    high_column = next(
        (
            lower[name]
            for name in ("high", "high_price", "maximum")
            if name in lower
        ),
        None,
    )
    low_column = next(
        (
            lower[name]
            for name in ("low", "low_price", "minimum")
            if name in lower
        ),
        None,
    )

    if high_column is None or low_column is None:
        raise RuntimeError(
            f"Colonne OHLC non riconosciute: {list(result.columns)}"
        )

    if isinstance(result.index, pd.DatetimeIndex):
        timestamps = pd.to_datetime(
            result.index,
            utc=True,
            errors="coerce",
        )
    else:
        time_column = next(
            (
                lower[name]
                for name in (
                    "timestamp",
                    "time",
                    "datetime",
                    "open_time",
                    "started_at",
                )
                if name in lower
            ),
            None,
        )

        if time_column is None:
            raise RuntimeError(
                "Nessun indice temporale o colonna timestamp nel frame."
            )

        raw = result[time_column]

        if pd.api.types.is_numeric_dtype(raw):
            numeric = pd.to_numeric(raw, errors="coerce")
            maximum = numeric.dropna().abs().max()

            if maximum > 10**14:
                unit = "us"
            elif maximum > 10**11:
                unit = "ms"
            else:
                unit = "s"

            timestamps = pd.to_datetime(
                numeric,
                unit=unit,
                utc=True,
                errors="coerce",
            )
        else:
            timestamps = pd.to_datetime(
                raw,
                utc=True,
                errors="coerce",
            )

    result.index = timestamps
    result = result.loc[~result.index.isna()].copy()

    result["__high"] = pd.to_numeric(
        result[high_column],
        errors="coerce",
    )
    result["__low"] = pd.to_numeric(
        result[low_column],
        errors="coerce",
    )

    result = result.dropna(subset=["__high", "__low"])
    result = result.sort_index()

    return result[["__high", "__low"]]


def build_symbol_map(session: Any) -> dict[str, str]:
    mapping: dict[str, str] = {}

    for contract in fetch_active_contracts(session):
        asset = str(getattr(contract, "asset", "") or "").strip().upper()
        symbol = str(getattr(contract, "symbol", "") or "").strip()

        if asset and symbol:
            mapping[asset] = symbol

    return mapping


def fallback_symbol(asset: str) -> str:
    if asset.upper() == "BTC":
        return "XBTUSDTM"

    return f"{asset.upper()}USDTM"


def load_target_trades() -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []

    with INPUT_PATH.open(
        "r",
        encoding="utf-8-sig",
        errors="replace",
        newline="",
    ) as handle:
        reader = csv.DictReader(handle)

        for source_row, record in enumerate(reader, start=2):
            strategy = str(record.get("strategy") or "").strip().lower()

            if strategy != TARGET_STRATEGY:
                continue

            enriched = dict(record)
            enriched["source_row"] = source_row
            rows.append(enriched)

    return rows


def load_existing() -> dict[int, dict[str, str]]:
    if not OUTPUT_PATH.exists():
        return {}

    existing: dict[int, dict[str, str]] = {}

    with OUTPUT_PATH.open(
        "r",
        encoding="utf-8-sig",
        errors="replace",
        newline="",
    ) as handle:
        for record in csv.DictReader(handle):
            try:
                source_row = int(str(record.get("source_row") or ""))
            except Exception:
                continue

            existing[source_row] = record

    return existing


def infer_fee_rate(
    entry_price: float,
    exit_price: float,
    notional_eur: float,
    costs_eur: float,
) -> float:
    if entry_price <= 0 or notional_eur <= 0 or costs_eur <= 0:
        return 0.0

    exit_notional = notional_eur * exit_price / entry_price
    denominator = notional_eur + exit_notional

    if denominator <= 0:
        return 0.0

    rate = costs_eur / denominator

    # Limite difensivo: massimo 50 bps per lato equivalente.
    return max(0.0, min(rate, 0.005))


def pnl_at_price(
    *,
    entry_price: float,
    evaluated_price: float,
    exit_price: float,
    side: str,
    notional_eur: float,
    costs_eur: float,
) -> tuple[float, float]:
    direction = 1.0 if side == "LONG" else -1.0

    gross = (
        notional_eur
        * direction
        * (evaluated_price - entry_price)
        / entry_price
    )

    fee_rate = infer_fee_rate(
        entry_price,
        exit_price,
        notional_eur,
        costs_eur,
    )

    evaluated_exit_notional = (
        notional_eur * evaluated_price / entry_price
    )

    estimated_costs = fee_rate * (
        notional_eur + evaluated_exit_notional
    )

    return gross, gross - estimated_costs


def calculate_trade(
    record: dict[str, Any],
    frame: pd.DataFrame,
    symbol: str,
) -> dict[str, Any]:
    source_row = int(record["source_row"])
    side = str(record.get("side") or "").strip().upper()

    if side not in {"LONG", "SHORT"}:
        raise ValueError(f"side non valido: {side!r}")

    timeframe = int(
        number(record.get("timeframe_minutes")) or 60
    )

    if timeframe != 60:
        raise ValueError(
            f"timeframe inatteso alla riga {source_row}: {timeframe}"
        )

    opened_at = utc_timestamp(record.get("opened_at"))
    closed_at = utc_timestamp(record.get("closed_at"))

    if closed_at < opened_at:
        raise ValueError("closed_at precedente a opened_at")

    entry_price = number(record.get("entry_price"))
    exit_price = number(record.get("exit_price"))
    notional_eur = number(record.get("normalized_notional_eur"))
    costs_eur = number(record.get("costs_eur")) or 0.0

    if (
        entry_price is None
        or exit_price is None
        or notional_eur is None
        or entry_price <= 0
        or exit_price <= 0
        or notional_eur <= 0
    ):
        raise ValueError("campi economici mancanti o non validi")

    candle_duration = pd.to_timedelta(timeframe, unit="min")

    # Usiamo high/low soltanto quando la candela è interamente
    # compresa fra apertura e chiusura. Per le candele parziali
    # conserviamo solo entry ed exit, evitando look-ahead intrabar.
    window = frame.loc[
        (frame.index >= opened_at.floor("h"))
        & (frame.index <= closed_at.floor("h"))
    ]

    price_points: list[tuple[float, pd.Timestamp, str]] = [
        (entry_price, opened_at, "ENTRY"),
        (exit_price, closed_at, "EXIT"),
    ]

    full_candles = 0

    for candle_time, candle in window.iterrows():
        candle_end = candle_time + candle_duration

        if candle_time < opened_at or candle_end > closed_at:
            continue

        high = number(candle["__high"])
        low = number(candle["__low"])

        if high is None or low is None:
            continue

        full_candles += 1
        price_points.append((high, candle_time, "HIGH"))
        price_points.append((low, candle_time, "LOW"))

    if side == "LONG":
        favorable = max(price_points, key=lambda item: item[0])
        adverse = min(price_points, key=lambda item: item[0])
    else:
        favorable = min(price_points, key=lambda item: item[0])
        adverse = max(price_points, key=lambda item: item[0])

    mfe_gross, mfe_net = pnl_at_price(
        entry_price=entry_price,
        evaluated_price=favorable[0],
        exit_price=exit_price,
        side=side,
        notional_eur=notional_eur,
        costs_eur=costs_eur,
    )

    mae_gross, mae_net = pnl_at_price(
        entry_price=entry_price,
        evaluated_price=adverse[0],
        exit_price=exit_price,
        side=side,
        notional_eur=notional_eur,
        costs_eur=costs_eur,
    )

    return {
        "source_row": source_row,
        "strategy": TARGET_STRATEGY,
        "asset": str(record.get("asset") or "").strip().upper(),
        "symbol": symbol,
        "side": side,
        "opened_at": iso(opened_at),
        "closed_at": iso(closed_at),
        "timeframe_minutes": timeframe,
        "entry_price": entry_price,
        "exit_price": exit_price,
        "max_favorable_price": favorable[0],
        "max_adverse_price": adverse[0],
        "mfe_gross_eur": mfe_gross,
        "mae_gross_eur": mae_gross,
        "mfe_net_eur": mfe_net,
        "mae_net_eur": mae_net,
        "mfe_at_utc": iso(favorable[1]),
        "mae_at_utc": iso(adverse[1]),
        "full_candles_used": full_candles,
        "excursion_quality": (
            "HISTORICAL_OHLC_1H_CONSERVATIVE_PARTIAL_CANDLES"
        ),
        "algorithm_version": ALGORITHM_VERSION,
        "generated_utc": datetime.now(timezone.utc).isoformat(),
    }


def atomic_write(rows: list[dict[str, Any]]) -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    descriptor, temporary_name = tempfile.mkstemp(
        prefix=OUTPUT_PATH.name + ".",
        suffix=".tmp",
        dir=str(OUTPUT_PATH.parent),
    )

    try:
        with os.fdopen(
            descriptor,
            "w",
            encoding="utf-8",
            newline="",
        ) as handle:
            writer = csv.DictWriter(
                handle,
                fieldnames=OUTPUT_FIELDS,
            )
            writer.writeheader()
            writer.writerows(rows)

        import shutil
        shutil.chown(
            temporary_name,
            user="cryptobot",
            group="cryptobot",
        )
        os.chmod(temporary_name, 0o664)
        os.replace(temporary_name, OUTPUT_PATH)
    finally:
        if os.path.exists(temporary_name):
            os.unlink(temporary_name)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--write",
        action="store_true",
        help="Scrive il CSV dedicato.",
    )
    parser.add_argument(
        "--require-complete",
        action="store_true",
        help="Non scrive se la copertura non è completa.",
    )
    args = parser.parse_args()

    trades = load_target_trades()
    existing = load_existing()

    missing = [
        row
        for row in trades
        if int(row["source_row"]) not in existing
    ]

    print(f"Trade Combo Adaptive: {len(trades)}")
    print(f"Già presenti nel registro escursioni: {len(existing)}")
    print(f"Da ricostruire: {len(missing)}")

    errors: list[str] = []
    generated: dict[int, dict[str, Any]] = {}

    if missing:
        session = make_session()
        symbol_map = build_symbol_map(session)

        by_asset: dict[str, list[dict[str, Any]]] = defaultdict(list)

        for row in missing:
            asset = str(row.get("asset") or "").strip().upper()
            by_asset[asset].append(row)

        for asset, asset_rows in sorted(by_asset.items()):
            symbol = symbol_map.get(asset) or fallback_symbol(asset)

            closes = [
                utc_timestamp(row.get("closed_at"))
                for row in asset_rows
            ]

            fetch_now = max(closes) + pd.Timedelta("2h")

            print(
                f"{asset}: {len(asset_rows)} trade · "
                f"simbolo {symbol} · fino a {fetch_now.isoformat()}"
            )

            try:
                raw_frame = fetch_klines(
                    session,
                    symbol,
                    60,
                    limit=420,
                    now=fetch_now.to_pydatetime(),
                )
                frame = normalize_frame(raw_frame)
            except Exception as exc:
                errors.append(
                    f"{asset}: download/normalizzazione fallita: {exc}"
                )
                continue

            if frame.empty:
                errors.append(f"{asset}: frame vuoto")
                continue

            for row in asset_rows:
                source_row = int(row["source_row"])

                try:
                    generated[source_row] = calculate_trade(
                        row,
                        frame,
                        symbol,
                    )
                except Exception as exc:
                    errors.append(
                        f"riga {source_row} {asset}: {exc}"
                    )

    merged: dict[int, dict[str, Any]] = dict(existing)
    merged.update(generated)

    target_rows = {
        int(row["source_row"])
        for row in trades
    }

    covered = len(target_rows.intersection(merged))
    total = len(target_rows)

    print()
    print(f"Copertura finale: {covered}/{total}")
    print(f"Nuove righe ricostruite: {len(generated)}")
    print(f"Errori: {len(errors)}")

    for error in errors[:30]:
        print("ERRORE:", error)

    if args.require_complete and covered != total:
        print(
            "Scrittura annullata: è stata richiesta "
            "copertura completa."
        )
        return 2

    if args.write:
        output_rows = [
            merged[source_row]
            for source_row in sorted(target_rows)
            if source_row in merged
        ]

        atomic_write(output_rows)
        print(f"CSV scritto: {OUTPUT_PATH}")
    else:
        print("Dry-run: nessun file scritto.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
