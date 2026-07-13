# -*- coding: utf-8 -*-
"""Repair and resiliently read the persistent paper-trading closed-trade CSV.

The repair is deliberately conservative:
- the original file is backed up before the first rewrite;
- balances and open positions are never changed;
- rows that cannot be mapped safely are quarantined instead of guessed;
- known historical schemas are normalized to the current TRADE_FIELDS schema.
"""

from __future__ import annotations

import csv
import json
import math
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

import pandas as pd


REPORTS_DIR = Path("reports")
BACKUP_PATH = REPORTS_DIR / "paper_trading_trade_log_before_repair.csv"
QUARANTINE_PATH = REPORTS_DIR / "paper_trading_trade_log_quarantine.csv"
STATUS_PATH = REPORTS_DIR / "paper_trading_trade_log_repair_status.json"

KNOWN_OPTIONAL_FIELDS = (
    "experiment_group_id",
    "liquidation_price",
)


def _iso_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _safe_float(value: Any, default: float = 0.0) -> float:
    try:
        number = float(value)
        return number if math.isfinite(number) else default
    except Exception:
        return default


def _write_status(payload: dict[str, Any]) -> None:
    STATUS_PATH.parent.mkdir(parents=True, exist_ok=True)
    STATUS_PATH.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def _candidate_schemas(
    canonical_fields: list[str],
    file_header: list[str],
) -> list[list[str]]:
    candidates: list[list[str]] = []

    def add(fields: Iterable[str]) -> None:
        candidate = list(fields)
        if candidate and candidate not in candidates:
            candidates.append(candidate)

    add(file_header)
    add(canonical_fields)

    for missing in KNOWN_OPTIONAL_FIELDS:
        add(field for field in canonical_fields if field != missing)

    add(
        field
        for field in canonical_fields
        if field not in set(KNOWN_OPTIONAL_FIELDS)
    )

    if set(file_header).issubset(set(canonical_fields)):
        add(file_header)

    return candidates


def _looks_like_header(row: list[str], canonical_fields: list[str]) -> bool:
    values = {str(value).strip() for value in row if str(value).strip()}
    return (
        "trade_id" in values
        and "portfolio" in values
        and ("net_pnl_eur" in values or "closed_at" in values)
        and len(values.intersection(canonical_fields)) >= 5
    )


def _map_row(
    row: list[str],
    file_header: list[str],
    canonical_fields: list[str],
) -> tuple[dict[str, str] | None, str]:
    candidates = _candidate_schemas(canonical_fields, file_header)
    exact = [schema for schema in candidates if len(schema) == len(row)]

    if len(row) == len(canonical_fields):
        schema = canonical_fields
        reason = "current_width"
    elif exact:
        schema = exact[0]
        reason = "matching_schema"
    elif len(row) < len(file_header):
        schema = file_header
        row = row + [""] * (len(schema) - len(row))
        reason = "padded_legacy_row"
    else:
        return None, "unsupported_width"

    mapped = {field: "" for field in canonical_fields}
    for field, value in zip(schema, row):
        if field in mapped:
            mapped[field] = value

    required = ("trade_id", "portfolio", "asset", "side", "closed_at")
    if any(not str(mapped.get(field, "")).strip() for field in required):
        return None, "missing_required_fields"

    side = str(mapped.get("side", "")).upper()
    if side not in {"LONG", "SHORT"}:
        return None, "invalid_side"

    return mapped, reason


def _dedupe_key(record: dict[str, str]) -> tuple[str, str, str]:
    return (
        str(record.get("trade_id", "")).strip(),
        str(record.get("portfolio", "")).strip(),
        str(record.get("closed_at", "")).strip(),
    )


def _write_canonical(
    path: Path,
    canonical_fields: list[str],
    records: list[dict[str, str]],
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_suffix(path.suffix + ".tmp")
    with temp.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=canonical_fields,
            extrasaction="ignore",
        )
        writer.writeheader()
        writer.writerows(records)
    temp.replace(path)


def _write_quarantine(rows: list[dict[str, Any]]) -> None:
    if not rows:
        if QUARANTINE_PATH.exists():
            QUARANTINE_PATH.unlink()
        return
    QUARANTINE_PATH.parent.mkdir(parents=True, exist_ok=True)
    with QUARANTINE_PATH.open(
        "w",
        encoding="utf-8",
        newline="",
    ) as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=("line_number", "reason", "raw_json"),
        )
        writer.writeheader()
        writer.writerows(rows)


def repair_trade_log(
    path: Path,
    canonical_fields: list[str],
) -> dict[str, Any]:
    """Normalize the trade log and return recovered records plus a summary."""
    path = Path(path)
    canonical_fields = list(canonical_fields)
    result: dict[str, Any] = {
        "generated_utc": _iso_now(),
        "path": str(path),
        "exists": path.exists(),
        "rewritten": False,
        "backup_created": False,
        "rows_before": 0,
        "rows_after": 0,
        "rows_recovered": 0,
        "rows_quarantined": 0,
        "duplicates_removed": 0,
        "header_before": [],
        "header_after": canonical_fields,
        "records": [],
    }

    if not path.exists() or path.stat().st_size == 0:
        _write_status({k: v for k, v in result.items() if k != "records"})
        return result

    raw_bytes = path.read_bytes()
    text = raw_bytes.decode("utf-8-sig", errors="replace")
    rows = list(csv.reader(text.splitlines()))
    nonempty = [
        (line_number, row)
        for line_number, row in enumerate(rows, start=1)
        if row and any(str(value).strip() for value in row)
    ]
    if not nonempty:
        _write_status({k: v for k, v in result.items() if k != "records"})
        return result

    _, file_header = nonempty[0]
    file_header = [str(value).strip() for value in file_header]
    result["header_before"] = file_header

    recovered: list[dict[str, str]] = []
    quarantine: list[dict[str, Any]] = []
    seen: set[tuple[str, str, str]] = set()

    for line_number, row in nonempty[1:]:
        if _looks_like_header(row, canonical_fields):
            continue

        mapped, reason = _map_row(
            [str(value) for value in row],
            file_header,
            canonical_fields,
        )
        if mapped is None:
            quarantine.append(
                {
                    "line_number": line_number,
                    "reason": reason,
                    "raw_json": json.dumps(row, ensure_ascii=False),
                }
            )
            continue

        key = _dedupe_key(mapped)
        if key in seen:
            result["duplicates_removed"] += 1
            continue
        seen.add(key)
        recovered.append(mapped)

    result["rows_before"] = max(0, len(nonempty) - 1)
    result["rows_after"] = len(recovered)
    result["rows_recovered"] = len(recovered)
    result["rows_quarantined"] = len(quarantine)
    result["records"] = recovered

    needs_rewrite = (
        file_header != canonical_fields
        or bool(quarantine)
        or result["duplicates_removed"] > 0
        or result["rows_before"] != result["rows_after"]
    )

    if needs_rewrite:
        if not BACKUP_PATH.exists():
            BACKUP_PATH.parent.mkdir(parents=True, exist_ok=True)
            BACKUP_PATH.write_bytes(raw_bytes)
            result["backup_created"] = True
        _write_canonical(path, canonical_fields, recovered)
        _write_quarantine(quarantine)
        result["rewritten"] = True

    _write_status({k: v for k, v in result.items() if k != "records"})
    return result


def ensure_trade_log_schema(
    path: Path,
    canonical_fields: list[str],
) -> dict[str, Any]:
    """Repair the file before appending another closed trade."""
    return repair_trade_log(path, canonical_fields)


def load_trade_frame_resilient(
    path: Path,
    canonical_fields: list[str],
) -> pd.DataFrame:
    result = repair_trade_log(path, canonical_fields)
    records = list(result.get("records", []))
    if not records:
        return pd.DataFrame(columns=list(canonical_fields))
    return pd.DataFrame(records, columns=list(canonical_fields))


def fallback_metrics_from_portfolio(
    portfolio: dict[str, Any],
) -> dict[str, Any]:
    closed = int(portfolio.get("closed_trades", 0) or 0)
    wins = int(portfolio.get("winning_trades", 0) or 0)
    gross_profit = _safe_float(portfolio.get("gross_profit_eur"), 0.0)
    gross_loss = _safe_float(portfolio.get("gross_loss_eur"), 0.0)
    net = gross_profit - gross_loss
    return {
        "closed_trades": closed,
        "winning_trades": wins,
        "net_pnl_eur": net,
        "expectancy_eur": net / closed if closed else 0.0,
        "win_rate_pct": wins / closed * 100.0 if closed else 0.0,
        "profit_factor": (
            gross_profit / gross_loss
            if gross_loss > 0
            else (math.inf if gross_profit > 0 else 0.0)
        ),
    }


def reconcile_state_counters(
    state: dict[str, Any],
    records: list[dict[str, Any]],
) -> dict[str, Any]:
    """Rebuild aggregate closed-trade counters without touching balances."""
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for record in records:
        grouped[str(record.get("portfolio", ""))].append(record)

    updated: list[str] = []
    skipped: list[str] = []
    for name, portfolio in state.get("portfolios", {}).items():
        rows = grouped.get(str(name), [])
        if not rows:
            skipped.append(str(name))
            continue

        existing_count = int(portfolio.get("closed_trades", 0) or 0)
        if len(rows) < existing_count:
            skipped.append(str(name))
            continue

        pnl = [_safe_float(row.get("net_pnl_eur"), 0.0) for row in rows]
        portfolio["closed_trades"] = len(rows)
        portfolio["winning_trades"] = sum(value > 0 for value in pnl)
        portfolio["gross_profit_eur"] = sum(value for value in pnl if value > 0)
        portfolio["gross_loss_eur"] = abs(
            sum(value for value in pnl if value < 0)
        )
        updated.append(str(name))

    return {
        "updated_portfolios": updated,
        "skipped_portfolios": skipped,
    }
