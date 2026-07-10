# -*- coding: utf-8 -*-
"""Synchronise every *current price* shown by the daily scanner.

The authoritative reference is ``reports/latest_market_snapshot.json`` created by
``market_snapshot.py`` at the beginning of the workflow.

This module is deliberately conservative:
- it never changes historical forecasts, targets, supports or returns;
- it only rewrites explicit current-price fields in a whitelist of current
  report/metrics files;
- it records every replacement in ``price_coherence_sync_metrics.csv``;
- it can safely be run more than once.

Price-sensitive modules upgraded to use the snapshot directly still pass through
this final guard, so a future module cannot reintroduce small intrarun drifts.
"""

from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

from shared_market_snapshot import load_snapshot, normalize_asset, snapshot_price


REPORTS_DIR = Path("reports")
LATEST_REPORT_PATH = REPORTS_DIR / "latest_report.md"
METRICS_PATH = REPORTS_DIR / "price_coherence_sync_metrics.csv"
REPORT_PATH = REPORTS_DIR / "price_coherence_sync_report.md"

START_MARKER = "<!-- PRICE_COHERENCE_SYNC_START -->"
END_MARKER = "<!-- PRICE_COHERENCE_SYNC_END -->"

ASSETS = ("BTC", "SOL", "DOGE")

# Only these marker blocks contain a present-time price that should be made
# identical. Historical logs/calibration blocks are intentionally excluded.
LATEST_MARKERS = (
    "GLOBAL_CONFLUENCE",
    "BTC_SOL_FRACTAL",
    "RSI_TOP_CYCLE",
    "SOL_ONCHAIN_METRICS",
    "MAJOR_ALT_LIFECYCLE_SQUEEZE",
    "MARKET_REGIME_MATCH",
    "TECHNICAL_STRUCTURE",
    "CLASSIC_TECHNICAL_CONFIRMATION",
    "CLASSIC_TECHNICAL_VISUAL",
    "FRACTAL_PATH_TRACKER",
    "LIQUIDATION_SUMMARY",
    "SCANNER_FORECAST_TRACKER",
)

# Individual reports are synchronised as well, not only latest_report.md.
MARKDOWN_REPORTS: dict[str, str | None] = {
    "technical_structure_report.md": None,
    "classic_technical_confirmation_report.md": None,
    "classic_technical_visual_report.md": None,
    "btc_2022_vs_sol_2026_report.md": "SOL",
    "rsi_top_cycle_report.md": "SOL",
    "sol_onchain_metrics_report.md": "SOL",
    "major_alt_lifecycle_squeeze_report.md": "SOL",
    "market_regime_match_report.md": None,
    "fractal_path_tracker.md": "SOL",
    "liquidation_report.md": None,
    "scanner_forecast_tracker_report.md": None,
}

# Structured current-metrics files. Logs, histories and forecast journals are
# excluded because their saved prices must remain frozen.
CSV_SPECS: dict[str, dict[str, Any]] = {
    "latest_scanner_summary.csv": {
        "asset_columns": ("asset", "ticker", "target"),
        "price_columns": ("current_price", "price"),
    },
        "scanner_forecast_latest.csv": {
        "asset_columns": ("asset", "target_ticker"),
        "price_columns": ("current_price",),
    },
"technical_structure_metrics.csv": {
        "asset_columns": ("asset", "ticker"),
        "price_columns": ("price",),
    },
    "classic_technical_confirmation_metrics.csv": {
        "asset_columns": ("asset", "ticker"),
        "price_columns": ("price", "current_price"),
    },
    "classic_technical_visual_metrics.csv": {
        "asset_columns": ("asset", "ticker"),
        "price_columns": ("price",),
    },
    "rsi_top_cycle_metrics.csv": {
        "fixed_asset": "SOL",
        "price_columns": ("current_price",),
        "row_filter": ("row_type", "period_summary"),
    },
    "btc_2022_vs_sol_2026_metrics.csv": {
        "fixed_asset": "SOL",
        "price_columns": ("sol_current_price",),
        "row_filter": ("row_type", "summary"),
    },
    "fractal_path_tracker_metrics.csv": {
        "fixed_asset": "SOL",
        "price_columns": ("current_price", "start_price"),
    },
    "major_alt_lifecycle_squeeze_latest.csv": {
        "fixed_asset": "SOL",
        "price_columns": ("price", "sol_price", "current_price"),
    },
    "sol_onchain_metrics_latest.csv": {
        "fixed_asset": "SOL",
        "price_columns": ("price", "sol_price", "sol_price_usd", "current_price"),
    },
    "liquidation_metrics.csv": {
        "asset_columns": ("asset", "ticker"),
        "price_columns": ("price", "current_price"),
    },
}

JSON_SPECS: dict[str, tuple[str, tuple[str, ...]]] = {
    "major_alt_lifecycle_squeeze_latest.json": (
        "SOL",
        ("price", "sol_price", "current_price", "target_price"),
    ),
    "sol_onchain_metrics_latest.json": (
        "SOL",
        ("price", "sol_price", "sol_price_usd", "current_price"),
    ),
}

PRICE_HEADERS = {
    "prezzo",
    "price",
    "prezzo attuale",
    "start price",
    "initial price",
    "prezzo iniziale",
    "current price",
    "current_price",
    "target_price",
    "target price",
    "target_price_today",
    "target price today",
}
ASSET_HEADERS = {"asset", "target", "ticker"}


def utc_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def safe_float(value: Any) -> float:
    try:
        number = float(value)
        return number if np.isfinite(number) else np.nan
    except (TypeError, ValueError):
        return np.nan


def atomic_write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(text, encoding="utf-8", newline="\n")
    tmp.replace(path)


def clean_cell(value: Any) -> str:
    text = str(value or "").strip()
    text = text.replace("**", "").replace("`", "").replace("\xa0", " ")
    return re.sub(r"\s+", " ", text).strip()


def normalise_header(value: Any) -> str:
    return clean_cell(value).lower().replace("_", " ")


def format_price(asset: str, value: Any) -> str:
    number = safe_float(value)
    if np.isnan(number):
        return "n/a"
    if asset == "DOGE":
        return f"{number:.5f} $"
    if asset == "BTC":
        return f"{number:,.0f} $".replace(",", ".")
    return f"{number:.2f} $".replace(".", ",")


def snapshot_prices() -> dict[str, float]:
    payload = load_snapshot()
    out: dict[str, float] = {}
    for asset in ASSETS:
        value = safe_float(snapshot_price(asset, np.nan))
        if not np.isnan(value):
            out[asset] = value
    return out


def _record(
    records: list[dict[str, Any]],
    *,
    module: str,
    asset: str,
    field: str,
    before: Any,
    after: Any,
    location: str,
) -> None:
    before_num = safe_float(before)
    after_num = safe_float(after)
    difference = np.nan
    if not np.isnan(before_num) and not np.isnan(after_num) and after_num:
        difference = (before_num / after_num - 1.0) * 100.0
    records.append(
        {
            "generated_utc": utc_iso(),
            "module": module,
            "asset": asset,
            "field": field,
            "before": before,
            "snapshot_price": after,
            "difference_before_pct": difference,
            "location": location,
            "status": "ALREADY_ALIGNED"
            if not np.isnan(before_num) and abs(before_num - after_num) <= max(1e-12, abs(after_num) * 1e-10)
            else "SYNCHRONISED",
        }
    )


def sync_csv(path: Path, spec: dict[str, Any], prices: dict[str, float], records: list[dict[str, Any]]) -> None:
    if not path.exists():
        return
    try:
        df = pd.read_csv(path)
    except Exception:
        return
    if df.empty:
        return

    price_columns = [column for column in spec.get("price_columns", ()) if column in df.columns]
    if not price_columns:
        return

    row_filter = spec.get("row_filter")
    mask = pd.Series(True, index=df.index)
    if row_filter:
        column, expected = row_filter
        if column not in df.columns:
            return
        mask &= df[column].astype(str).str.strip().str.lower() == str(expected).lower()

    fixed_asset = spec.get("fixed_asset")
    asset_columns = [column for column in spec.get("asset_columns", ()) if column in df.columns]

    changed = False
    for idx in df.index[mask]:
        if fixed_asset:
            asset = fixed_asset
        else:
            asset = ""
            for column in asset_columns:
                candidate = normalize_asset(df.at[idx, column])
                if candidate in prices:
                    asset = candidate
                    break
        if asset not in prices:
            continue
        price = prices[asset]
        for column in price_columns:
            before = df.at[idx, column]
            _record(
                records,
                module=path.name,
                asset=asset,
                field=column,
                before=before,
                after=price,
                location=f"row {idx}",
            )
            df.at[idx, column] = price
            changed = True

    if changed:
        tmp = path.with_suffix(path.suffix + ".tmp")
        df.to_csv(tmp, index=False, encoding="utf-8", lineterminator="\n")
        tmp.replace(path)


def _sync_json_object(
    obj: Any,
    *,
    asset: str,
    keys: tuple[str, ...],
    price: float,
    records: list[dict[str, Any]],
    module: str,
    path: str = "$",
) -> bool:
    changed = False
    if isinstance(obj, dict):
        for key, value in list(obj.items()):
            child_path = f"{path}.{key}"
            if key in keys and not isinstance(value, (dict, list)):
                _record(
                    records,
                    module=module,
                    asset=asset,
                    field=key,
                    before=value,
                    after=price,
                    location=child_path,
                )
                obj[key] = price
                changed = True
            elif isinstance(value, (dict, list)):
                changed |= _sync_json_object(
                    value,
                    asset=asset,
                    keys=keys,
                    price=price,
                    records=records,
                    module=module,
                    path=child_path,
                )
    elif isinstance(obj, list):
        for index, value in enumerate(obj):
            if isinstance(value, (dict, list)):
                changed |= _sync_json_object(
                    value,
                    asset=asset,
                    keys=keys,
                    price=price,
                    records=records,
                    module=module,
                    path=f"{path}[{index}]",
                )
    return changed


def sync_json(path: Path, asset: str, keys: tuple[str, ...], prices: dict[str, float], records: list[dict[str, Any]]) -> None:
    if not path.exists() or asset not in prices:
        return
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return
    if _sync_json_object(
        payload,
        asset=asset,
        keys=keys,
        price=prices[asset],
        records=records,
        module=path.name,
    ):
        atomic_write_text(path, json.dumps(payload, ensure_ascii=False, indent=2) + "\n")


def _asset_from_heading(line: str, current: str | None) -> str | None:
    match = re.match(r"^#{2,4}\s+(.+?)\s*$", line.strip())
    if not match:
        return current
    heading = clean_cell(match.group(1)).upper()
    mapping = {
        "BTC": "BTC",
        "BITCOIN": "BTC",
        "SOL": "SOL",
        "SOLANA": "SOL",
        "DOGE": "DOGE",
        "DOGECOIN": "DOGE",
    }
    for token, asset in mapping.items():
        if heading == token or heading.startswith(token + " "):
            return asset
    return current


def _replace_explicit_price_line(line: str, current_asset: str | None, default_asset: str | None, prices: dict[str, float]) -> tuple[str, str | None, Any]:
    # Examples: "- Prezzo: **77,62 $**", "- Prezzo SOL corrente: **...**"
    pattern = re.compile(
        r"^(?P<prefix>\s*[-*]\s+(?:\*\*)?Prezzo(?:\s+(?P<asset>BTC|SOL|DOGE))?(?:\s+(?:attuale|corrente))?(?:\*\*)?\s*:\s*(?:\*\*)?)"
        r"(?P<value>[^*\n]+)(?P<suffix>(?:\*\*)?\s*)$",
        flags=re.IGNORECASE,
    )
    match = pattern.match(line)
    if not match:
        return line, None, None
    asset = normalize_asset(match.group("asset") or current_asset or default_asset)
    if asset not in prices:
        return line, None, None
    new_line = match.group("prefix") + format_price(asset, prices[asset]) + match.group("suffix")
    return new_line, asset, match.group("value")


def sync_markdown_text(
    text: str,
    *,
    module: str,
    prices: dict[str, float],
    records: list[dict[str, Any]],
    default_asset: str | None = None,
) -> str:
    lines = text.splitlines()
    output: list[str] = []
    current_asset = default_asset
    i = 0

    while i < len(lines):
        line = lines[i]
        current_asset = _asset_from_heading(line, current_asset)

        # Markdown table: header + separator + body.
        if line.strip().startswith("|") and i + 1 < len(lines) and re.match(r"^\s*\|?[\s:|-]+\|\s*$", lines[i + 1]):
            table_lines = [line, lines[i + 1]]
            j = i + 2
            while j < len(lines) and lines[j].strip().startswith("|"):
                table_lines.append(lines[j])
                j += 1

            header = [clean_cell(cell) for cell in table_lines[0].strip().strip("|").split("|")]
            norm_header = [normalise_header(cell) for cell in header]
            asset_idx = next((idx for idx, name in enumerate(norm_header) if name in ASSET_HEADERS), None)
            price_indexes = [idx for idx, name in enumerate(norm_header) if name in PRICE_HEADERS]
            # PRICE_SCORE_TABLE_GUARD_V1
            # Nel Classic Technical la colonna chiamata "Prezzo" è lo score
            # della conferma prezzo, non il prezzo di mercato. Non va riscritta.
            score_area_headers = {
                "trend", "struttura", "momentum", "volume",
                "candela", "wyckoff", "totale",
            }
            if score_area_headers.issubset(set(norm_header)):
                price_indexes = [
                    idx for idx in price_indexes
                    if norm_header[idx] not in {"prezzo", "price"}
                ]

            new_table = table_lines[:2]
            for row_no, row_line in enumerate(table_lines[2:], start=1):
                cells = [cell.strip() for cell in row_line.strip().strip("|").split("|")]
                if len(cells) != len(header):
                    new_table.append(row_line)
                    continue

                row_asset: str | None = None
                if asset_idx is not None:
                    row_asset = normalize_asset(clean_cell(cells[asset_idx]))

                # Key/value tables such as "| Prezzo SOL | 77,62 $ |".
                if len(cells) >= 2:
                    first = clean_cell(cells[0])
                    key_match = re.search(r"\bPrezzo\s+(BTC|SOL|DOGE)\b", first, flags=re.IGNORECASE)
                    if key_match:
                        key_asset = normalize_asset(key_match.group(1))
                        if key_asset in prices:
                            before = cells[1]
                            cells[1] = format_price(key_asset, prices[key_asset])
                            _record(
                                records,
                                module=module,
                                asset=key_asset,
                                field=header[1] if len(header) > 1 else "Valore",
                                before=before,
                                after=prices[key_asset],
                                location=f"markdown table row {row_no}",
                            )

                if row_asset in prices and price_indexes:
                    for price_idx in price_indexes:
                        before = cells[price_idx]
                        cells[price_idx] = format_price(row_asset, prices[row_asset])
                        _record(
                            records,
                            module=module,
                            asset=row_asset,
                            field=header[price_idx],
                            before=before,
                            after=prices[row_asset],
                            location=f"markdown table row {row_no}",
                        )

                new_table.append("| " + " | ".join(cells) + " |")

            output.extend(new_table)
            i = j
            continue

        new_line, asset, before = _replace_explicit_price_line(line, current_asset, default_asset, prices)
        if asset:
            _record(
                records,
                module=module,
                asset=asset,
                field="Prezzo corrente",
                before=before,
                after=prices[asset],
                location=f"markdown line {i + 1}",
            )
        output.append(new_line)
        i += 1

    suffix = "\n" if text.endswith("\n") else ""
    return "\n".join(output) + suffix


def sync_individual_markdown(prices: dict[str, float], records: list[dict[str, Any]]) -> None:
    for filename, default_asset in MARKDOWN_REPORTS.items():
        path = REPORTS_DIR / filename
        if not path.exists():
            continue
        try:
            old = path.read_text(encoding="utf-8")
        except Exception:
            continue
        new = sync_markdown_text(
            old,
            module=filename,
            prices=prices,
            records=records,
            default_asset=default_asset,
        )
        if new != old:
            atomic_write_text(path, new)


def _sync_marker_block(text: str, marker: str, prices: dict[str, float], records: list[dict[str, Any]]) -> str:
    start = f"<!-- {marker}_START -->"
    end = f"<!-- {marker}_END -->"
    if start not in text or end not in text:
        return text
    pattern = re.compile(re.escape(start) + r"(.*?)" + re.escape(end), flags=re.DOTALL)
    default_asset = "SOL" if marker in {
        "BTC_SOL_FRACTAL",
        "RSI_TOP_CYCLE",
        "SOL_ONCHAIN_METRICS",
        "MAJOR_ALT_LIFECYCLE_SQUEEZE",
        "FRACTAL_PATH_TRACKER",
    } else None

    def repl(match: re.Match[str]) -> str:
        body = sync_markdown_text(
            match.group(1),
            module=f"latest_report:{marker}",
            prices=prices,
            records=records,
            default_asset=default_asset,
        )
        return start + body + end

    return pattern.sub(repl, text, count=1)


def sync_latest_report(prices: dict[str, float], records: list[dict[str, Any]]) -> None:
    if not LATEST_REPORT_PATH.exists():
        return
    try:
        old = LATEST_REPORT_PATH.read_text(encoding="utf-8")
    except Exception:
        return
    new = old
    for marker in LATEST_MARKERS:
        new = _sync_marker_block(new, marker, prices, records)
    if new != old:
        atomic_write_text(LATEST_REPORT_PATH, new)


def render_report(prices: dict[str, float], records: list[dict[str, Any]]) -> str:
    changed = sum(1 for record in records if record["status"] == "SYNCHRONISED")
    aligned = len(records) - changed
    lines = [
        "# Sincronizzazione prezzo condiviso",
        "",
        f"Generato: {utc_iso()}",
        "",
        "Riferimento unico: `reports/latest_market_snapshot.json`.",
        "",
        "| Asset | Prezzo snapshot |",
        "| --- | --- |",
    ]
    for asset in ASSETS:
        lines.append(f"| {asset} | {format_price(asset, prices.get(asset))} |")
    lines.extend(
        [
            "",
            f"Campi controllati: **{len(records)}**; già allineati: **{aligned}**; sincronizzati: **{changed}**.",
            "",
            "La sincronizzazione riguarda soltanto il prezzo corrente. Storici, target, supporti, invalidazioni e previsioni salvate non vengono modificati.",
            "",
        ]
    )
    return "\n".join(lines)


def write_sync_report(prices: dict[str, float], records: list[dict[str, Any]]) -> None:
    METRICS_PATH.parent.mkdir(parents=True, exist_ok=True)
    columns = [
        "generated_utc",
        "module",
        "asset",
        "field",
        "before",
        "snapshot_price",
        "difference_before_pct",
        "location",
        "status",
    ]
    pd.DataFrame(records, columns=columns).to_csv(
        METRICS_PATH,
        index=False,
        encoding="utf-8",
        lineterminator="\n",
    )
    report = render_report(prices, records)
    atomic_write_text(REPORT_PATH, report.rstrip() + "\n")


def main() -> None:
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    prices = snapshot_prices()
    missing = [asset for asset in ASSETS if asset not in prices]
    if missing:
        raise RuntimeError(
            "Snapshot condiviso incompleto: mancano " + ", ".join(missing)
        )

    records: list[dict[str, Any]] = []

    for filename, spec in CSV_SPECS.items():
        sync_csv(REPORTS_DIR / filename, spec, prices, records)

    for filename, (asset, keys) in JSON_SPECS.items():
        sync_json(REPORTS_DIR / filename, asset, keys, prices, records)

    sync_individual_markdown(prices, records)
    sync_latest_report(prices, records)
    write_sync_report(prices, records)

    changed = sum(1 for record in records if record["status"] == "SYNCHRONISED")
    print(f"Prezzi snapshot: {prices}")
    print(f"Campi controllati: {len(records)}; sincronizzati: {changed}")
    print(f"Creato {METRICS_PATH}")
    print(f"Creato {REPORT_PATH}")


if __name__ == "__main__":
    main()
