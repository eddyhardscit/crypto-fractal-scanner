# -*- coding: utf-8 -*-
"""Final non-invasive quality check for the generated crypto reports.

Checks:
- shared snapshot availability;
- scanner and downstream module current-price identity;
- structured Technical/Fibonacci fields;
- candidate-pattern progress is not misreported as a negative target progress;
- Classic Visual uses Technical Structure as lifecycle authority;
- common UTF-8/mojibake problems;
- Global structured scanner data is available.

The module never changes trading scores or historical logs.
"""

from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

from scanner_signal_reader import load_scanner_summary, validate_scanner_summary
from shared_market_snapshot import load_snapshot, normalize_asset, snapshot_price

from compact_latest_report import compact_latest_report

REPORTS_DIR = Path("reports")
LATEST_REPORT = REPORTS_DIR / "latest_report.md"
OUTPUT_REPORT = REPORTS_DIR / "data_quality_coherence_report.md"
OUTPUT_JSON = REPORTS_DIR / "data_quality_coherence.json"

START_MARKER = "<!-- DATA_QUALITY_COHERENCE_START -->"
END_MARKER = "<!-- DATA_QUALITY_COHERENCE_END -->"

ASSETS = ("BTC", "SOL", "DOGE")
# EXCHANGE_MICROSTRUCTURE_QUALITY_PATCH_V2_1
MOJIBAKE_TOKENS = ("Ã", "Â", "â€", "â†", "ðŸ", "�")
# STRICT_SHARED_PRICE_CHECK_V1
PRICE_TOLERANCE_PCT = 0.000001

MODULE_PRICE_SPECS: dict[str, dict[str, Any]] = {
    "Scanner": {
        "path": REPORTS_DIR / "latest_scanner_summary.csv",
        "asset_columns": ("asset", "ticker"),
        "price_columns": ("current_price", "price"),
    },
        "Scanner Forecast": {
        "path": REPORTS_DIR / "scanner_forecast_latest.csv",
        "asset_columns": ("asset", "target_ticker"),
        "price_columns": ("current_price",),
    },
"Technical Structure": {
        "path": REPORTS_DIR / "technical_structure_metrics.csv",
        "asset_columns": ("asset", "ticker"),
        "price_columns": ("price",),
    },
    "Classic Technical": {
        "path": REPORTS_DIR / "classic_technical_confirmation_metrics.csv",
        "asset_columns": ("asset", "ticker"),
        "price_columns": ("price", "current_price"),
    },
    "Classic Visual": {
        "path": REPORTS_DIR / "classic_technical_visual_metrics.csv",
        "asset_columns": ("asset", "ticker"),
        "price_columns": ("price",),
    },
    "Exchange Microstructure": {
        "path": REPORTS_DIR / "exchange_microstructure_metrics.csv",
        "asset_columns": ("asset",),
        "price_columns": ("price",),
    },
    "RSI top-cycle": {
        "path": REPORTS_DIR / "rsi_top_cycle_metrics.csv",
        "fixed_asset": "SOL",
        "price_columns": ("current_price",),
        "row_filter": ("row_type", "period_summary"),
    },
    "Frattale BTC/SOL": {
        "path": REPORTS_DIR / "btc_2022_vs_sol_2026_metrics.csv",
        "fixed_asset": "SOL",
        "price_columns": ("sol_current_price",),
        "row_filter": ("row_type", "summary"),
    },
    "Fractal path": {
        "path": REPORTS_DIR / "fractal_path_tracker_metrics.csv",
        "fixed_asset": "SOL",
        "price_columns": ("current_price", "start_price"),
    },
}


def utc_now_text() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")


def safe_float(value: Any) -> float:
    try:
        number = float(value)
        return number if np.isfinite(number) else np.nan
    except (TypeError, ValueError):
        return np.nan


def atomic_write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(text, encoding="utf-8", newline="\n")
    tmp.replace(path)


def read_text(path: Path) -> str:
    if not path.exists():
        return ""
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return path.read_text(encoding="utf-8", errors="replace")


def section(text: str, start: str, end: str) -> str:
    if start not in text or end not in text:
        return ""
    a = text.find(start) + len(start)
    b = text.find(end, a)
    return text[a:b] if b >= a else ""


def find_mojibake(text: str) -> list[dict[str, Any]]:
    issues = []
    for token in MOJIBAKE_TOKENS:
        count = text.count(token)
        if count:
            examples = []
            for line_no, line in enumerate(text.splitlines(), start=1):
                if token in line:
                    examples.append({"line": line_no, "text": line[:180]})
                    if len(examples) >= 3:
                        break
            issues.append({"token": token, "count": count, "examples": examples})
    return issues


def snapshot_prices() -> dict[str, float]:
    out: dict[str, float] = {}
    for asset in ASSETS:
        value = safe_float(snapshot_price(asset, np.nan))
        if not np.isnan(value):
            out[asset] = value
    return out


def _module_rows(spec: dict[str, Any]) -> pd.DataFrame:
    path: Path = spec["path"]
    if not path.exists():
        return pd.DataFrame()
    try:
        df = pd.read_csv(path)
    except Exception:
        return pd.DataFrame()
    if df.empty:
        return df
    row_filter = spec.get("row_filter")
    if row_filter:
        column, expected = row_filter
        if column not in df.columns:
            return pd.DataFrame()
        df = df[df[column].astype(str).str.strip().str.lower() == str(expected).lower()]
    return df


def collect_module_price_checks(prices: dict[str, float]) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []
    for module, spec in MODULE_PRICE_SPECS.items():
        df = _module_rows(spec)
        if df.empty:
            checks.append(
                {
                    "module": module,
                    "asset": spec.get("fixed_asset", "n/a"),
                    "status": "MISSING",
                    "module_price": np.nan,
                    "snapshot_price": prices.get(spec.get("fixed_asset", ""), np.nan),
                    "difference_pct": np.nan,
                    "field": "n/a",
                }
            )
            continue

        price_columns = [column for column in spec.get("price_columns", ()) if column in df.columns]
        if not price_columns:
            checks.append(
                {
                    "module": module,
                    "asset": spec.get("fixed_asset", "n/a"),
                    "status": "MISSING_FIELD",
                    "module_price": np.nan,
                    "snapshot_price": prices.get(spec.get("fixed_asset", ""), np.nan),
                    "difference_pct": np.nan,
                    "field": "n/a",
                }
            )
            continue

        for _, row in df.iterrows():
            asset = spec.get("fixed_asset")
            if not asset:
                asset = ""
                for column in spec.get("asset_columns", ()):
                    if column in df.columns:
                        candidate = normalize_asset(row.get(column))
                        if candidate in prices:
                            asset = candidate
                            break
            if asset not in prices:
                continue

            # One check for every explicitly available current-price field.
            for column in price_columns:
                value = safe_float(row.get(column))
                snap = prices[asset]
                diff = (value / snap - 1.0) * 100.0 if not np.isnan(value) and snap else np.nan
                status = "OK" if not np.isnan(diff) and abs(diff) <= PRICE_TOLERANCE_PCT else "WARN"
                checks.append(
                    {
                        "module": module,
                        "asset": asset,
                        "status": status,
                        "module_price": value,
                        "snapshot_price": snap,
                        "difference_pct": diff,
                        "field": column,
                    }
                )
    return checks


def detect_global_scanner_na(text: str, summary: pd.DataFrame) -> list[str]:
    if summary.empty:
        return []
    global_block = section(text, "<!-- GLOBAL_CONFLUENCE_START -->", "<!-- GLOBAL_CONFLUENCE_END -->")
    if not global_block:
        return ["Blocco Global Confluence non trovato nel report principale."]
    for pattern in (r"return centrale 30g\s+n/?a", r"Direzione scanner:\s*n/?a"):
        if re.search(pattern, global_block, flags=re.IGNORECASE):
            return [
                "Il Global Confluence mostra ancora dati scanner n/a nonostante latest_scanner_summary sia disponibile."
            ]
    return []


def technical_integrity_checks() -> tuple[list[str], list[str], dict[str, Any]]:
    critical: list[str] = []
    warnings: list[str] = []
    details: dict[str, Any] = {
        "fibonacci_available": False,
        "candidate_progress_ok": False,
        "classic_visual_authority_ok": False,
    }

    technical_path = REPORTS_DIR / "technical_structure_metrics.csv"
    visual_path = REPORTS_DIR / "classic_technical_visual_metrics.csv"

    if not technical_path.exists():
        critical.append("technical_structure_metrics.csv mancante.")
        return critical, warnings, details

    try:
        technical = pd.read_csv(technical_path)
    except Exception:
        critical.append("technical_structure_metrics.csv non leggibile.")
        return critical, warnings, details

    required_fib = {
        "fib_score",
        "fib_state",
        "fib_nearest_ratio",
        "fib_nearest_level",
        "fib_confluence",
    }
    missing_fib = sorted(required_fib - set(technical.columns))
    if missing_fib:
        critical.append("Campi Fibonacci mancanti nel Technical Structure: " + ", ".join(missing_fib))
    else:
        details["fibonacci_available"] = True

    progress_issues: list[str] = []
    for prefix in (
        "double_bottom",
        "triple_bottom",
        "adam_eve_bottom",
        "double_top",
        "triple_top",
        "adam_eve_top",
    ):
        status_col = prefix
        progress_col = f"{prefix}_target_progress_pct"
        distance_col = f"{prefix}_distance_to_neckline_pct"
        if status_col not in technical.columns:
            continue
        if distance_col not in technical.columns:
            progress_issues.append(f"{distance_col} mancante")
        if progress_col in technical.columns:
            candidate = technical[technical[status_col].astype(str).str.upper() == "CANDIDATO"]
            finite = pd.to_numeric(candidate[progress_col], errors="coerce").notna()
            if finite.any():
                assets = ", ".join(candidate.loc[finite, "asset"].astype(str).tolist())
                progress_issues.append(f"{prefix}: progresso target ancora valorizzato per candidati ({assets})")

    if progress_issues:
        warnings.extend(progress_issues)
    else:
        details["candidate_progress_ok"] = True

    if not visual_path.exists():
        warnings.append("classic_technical_visual_metrics.csv mancante.")
        return critical, warnings, details

    try:
        visual = pd.read_csv(visual_path)
    except Exception:
        warnings.append("classic_technical_visual_metrics.csv non leggibile.")
        return critical, warnings, details

    required_visual = {
        "technical_lifecycle_source",
        "pattern_distance_to_neckline_pct",
        "fib_state",
        "fib_score",
    }
    missing_visual = sorted(required_visual - set(visual.columns))
    if missing_visual:
        warnings.append("Campi correttivi mancanti nel Classic Visual: " + ", ".join(missing_visual))
    else:
        source_ok = visual["technical_lifecycle_source"].astype(str).str.contains(
            "technical_structure_metrics.csv", case=False, na=False
        )
        if source_ok.all() and len(source_ok) >= 1:
            details["classic_visual_authority_ok"] = True
        else:
            warnings.append("Classic Visual non usa Technical Structure come fonte lifecycle per tutti gli asset.")

        candidate = visual[visual["pattern_state"].astype(str).str.upper() == "CANDIDATO"]
        if "pattern_target_progress_pct" in visual.columns:
            bad = pd.to_numeric(candidate["pattern_target_progress_pct"], errors="coerce").notna()
            if bad.any():
                warnings.append("Classic Visual mostra ancora un progresso target numerico per pattern CANDIDATO.")

    return critical, warnings, details


def fmt_pct(value: Any) -> str:
    number = safe_float(value)
    if np.isnan(number):
        return "n/a"
    return f"{number:+.4f}%".replace(".", ",")


def fmt_price(asset: str, value: Any) -> str:
    number = safe_float(value)
    if np.isnan(number):
        return "n/a"
    if asset == "DOGE":
        return f"{number:.5f} $"
    if asset == "BTC":
        return f"{number:,.0f} $".replace(",", ".")
    return f"{number:.2f} $".replace(".", ",")


def render(payload: dict[str, Any]) -> str:
    lines = [
        "# Data quality / coherence check",
        "",
        f"Generato: {payload['generated_at_utc']}",
        "",
        "Questo controllo non modifica punteggi o decisioni. Verifica che tutti i moduli usino lo stesso prezzo corrente e che le nuove regole Technical/Classic Visual siano integre.",
        "",
        f"## Stato finale: **{payload['overall_status']}**",
        "",
    ]

    if payload["critical_issues"]:
        lines += ["## Problemi da correggere", ""]
        lines += [f"- {item}" for item in payload["critical_issues"]]
        lines.append("")

    if payload["warnings"]:
        lines += ["## Avvisi", ""]
        lines += [f"- {item}" for item in payload["warnings"]]
        lines.append("")

    lines += ["## Prezzo unico per modulo", ""]
    rows = []
    for item in payload["module_price_checks"]:
        rows.append(
            {
                "Modulo": item["module"],
                "Asset": item["asset"],
                "Campo": item["field"],
                "Stato": item["status"],
                "Snapshot": fmt_price(item["asset"], item["snapshot_price"]),
                "Modulo": fmt_price(item["asset"], item["module_price"]),
                "Differenza": fmt_pct(item["difference_pct"]),
            }
        )
    if rows:
        # Avoid duplicate key label by constructing explicit DataFrame columns.
        table = pd.DataFrame(
            [
                {
                    "Modulo": item["module"],
                    "Asset": item["asset"],
                    "Campo": item["field"],
                    "Stato": item["status"],
                    "Prezzo snapshot": fmt_price(item["asset"], item["snapshot_price"]),
                    "Prezzo modulo": fmt_price(item["asset"], item["module_price"]),
                    "Differenza": fmt_pct(item["difference_pct"]),
                }
                for item in payload["module_price_checks"]
            ]
        )
        lines.append(table.to_markdown(index=False))
    else:
        lines.append("_Nessun file strutturato disponibile._")
    lines.append("")

    lines += ["## Integrità Technical / Classic Visual", ""]
    integrity = payload["technical_integrity"]
    lines.append(f"- Fibonacci strutturato: **{'OK' if integrity['fibonacci_available'] else 'MANCANTE'}**")
    lines.append(f"- Candidati senza falso progresso target: **{'OK' if integrity['candidate_progress_ok'] else 'DA CONTROLLARE'}**")
    lines.append(f"- Classic Visual allineato al lifecycle Technical: **{'OK' if integrity['classic_visual_authority_ok'] else 'DA CONTROLLARE'}**")
    lines.append("")

    lines += ["## Controllo codifica UTF-8", ""]
    if payload["mojibake"]:
        total = sum(item["count"] for item in payload["mojibake"])
        lines.append(f"Trovati **{total}** possibili frammenti con codifica rotta nel report principale.")
    else:
        lines.append("Nessun indicatore comune di mojibake trovato.")
    lines.append("")

    lines += ["## File strutturati", ""]
    lines.append(f"- Snapshot condiviso completo: **{'OK' if payload['snapshot_complete'] else 'MANCANTE'}**")
    lines.append(f"- Scanner summary: **{'OK' if payload['scanner_summary_available'] else 'MANCANTE'}**")
    lines.append(f"- Price coherence sync: **{'OK' if payload['price_sync_available'] else 'MANCANTE'}**")
    lines.append(f"- Dati exchange / microstruttura: **{'OK' if payload.get('exchange_data_available') else 'MANCANTE'}**")
    lines.append("")

    if payload["overall_status"] == "OK":
        lines.append("Il workflow è tecnicamente coerente nei controlli disponibili.")
    elif payload["overall_status"] == "WARN":
        lines.append("Il workflow può continuare, ma gli avvisi sopra vanno verificati.")
    else:
        lines.append("Ci sono problemi tecnici che possono rendere incompleto o incoerente il report.")
    lines.append("")
    return "\n".join(lines)


def inject(text: str) -> None:
    if not LATEST_REPORT.exists():
        return
    old = read_text(LATEST_REPORT)
    block = START_MARKER + "\n" + text.strip() + "\n" + END_MARKER
    if START_MARKER in old and END_MARKER in old:
        a = old.find(START_MARKER)
        b = old.find(END_MARKER, a) + len(END_MARKER)
        new = old[:a] + block + old[b:]
    else:
        new = old.rstrip() + "\n\n" + block + "\n"
    atomic_write(LATEST_REPORT, new)


def main() -> None:
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    text = read_text(LATEST_REPORT)
    summary = load_scanner_summary()
    snapshot = load_snapshot()
    prices = snapshot_prices()

    critical: list[str] = []
    warnings: list[str] = []

    scanner_validation = validate_scanner_summary()
    if scanner_validation:
        critical.extend(scanner_validation)

    missing_assets = [asset for asset in ASSETS if asset not in prices]
    if missing_assets:
        critical.append("Snapshot condiviso incompleto: " + ", ".join(missing_assets))

    mojibake = find_mojibake(text)
    if mojibake:
        warnings.append("Il report contiene ancora caratteri corrotti: verificare sorgente e scrittura UTF-8.")

    warnings.extend(detect_global_scanner_na(text, summary))

    module_price_checks = collect_module_price_checks(prices)
    bad_prices = [item for item in module_price_checks if item["status"] not in {"OK", "MISSING"}]
    if bad_prices:
        warnings.append(
            f"{len(bad_prices)} campi prezzo non coincidono con lo snapshot entro {PRICE_TOLERANCE_PCT:.2f}%."
        )

    tech_critical, tech_warnings, integrity = technical_integrity_checks()
    critical.extend(tech_critical)
    warnings.extend(tech_warnings)

    price_sync_available = (REPORTS_DIR / "price_coherence_sync_metrics.csv").exists()
    if not price_sync_available:
        warnings.append("price_coherence_sync.py non risulta eseguito in questo workflow.")

    exchange_required_files = (
        REPORTS_DIR / "exchange_market_data_snapshot.json",
        REPORTS_DIR / "exchange_market_data_intraday.csv",
        REPORTS_DIR / "exchange_storage_status.json",
        REPORTS_DIR / "exchange_microstructure_metrics.csv",
        REPORTS_DIR / "exchange_microstructure_history.csv",
        REPORTS_DIR / "exchange_signal_tracker_metrics.csv",
        REPORTS_DIR / "exchange_prediction_overlay.csv",
    )
    exchange_missing_files = [path.name for path in exchange_required_files if not path.exists()]
    exchange_data_available = not exchange_missing_files
    if exchange_missing_files:
        warnings.append("File exchange mancanti: " + ", ".join(exchange_missing_files))
    else:
        try:
            exchange_metrics = pd.read_csv(REPORTS_DIR / "exchange_microstructure_metrics.csv")
            required_exchange_columns = {
                "asset", "price", "raw_score", "candidate_global_score", "global_score", "data_coverage",
                "exchange_count", "kucoin_available", "global_activation_status",
                "funding_rate_pct", "oi_change_24h_pct", "taker_buy_sell_ratio_4h",
                "orderbook_imbalance_0_5pct",
            }
            missing_exchange_columns = sorted(required_exchange_columns - set(exchange_metrics.columns))
            if missing_exchange_columns:
                warnings.append("Campi exchange mancanti: " + ", ".join(missing_exchange_columns))
                exchange_data_available = False
            if "global_score" in exchange_metrics.columns:
                exchange_scores = pd.to_numeric(exchange_metrics["global_score"], errors="coerce").dropna()
                if (exchange_scores.abs() > 1).any():
                    critical.append("Exchange Global score supera il limite prudente ±1.")
        except Exception:
            warnings.append("exchange_microstructure_metrics.csv non leggibile.")
            exchange_data_available = False

    critical = list(dict.fromkeys(critical))
    warnings = list(dict.fromkeys(warnings))
    status = "ERROR" if critical else ("WARN" if warnings else "OK")

    payload = {
        "schema_version": 2,
        "generated_at_utc": utc_now_text(),
        "overall_status": status,
        "critical_issues": critical,
        "warnings": warnings,
        "snapshot_complete": len(prices) == len(ASSETS),
        "scanner_summary_available": not summary.empty,
        "price_sync_available": price_sync_available,
        "exchange_data_available": exchange_data_available,
        "exchange_missing_files": exchange_missing_files,
        "snapshot_metadata": snapshot,
        "module_price_checks": module_price_checks,
        "technical_integrity": integrity,
        "mojibake": mojibake,
    }

    report = render(payload)
    atomic_write(OUTPUT_REPORT, report.rstrip() + "\n")
    atomic_write(OUTPUT_JSON, json.dumps(payload, ensure_ascii=False, indent=2, default=str) + "\n")
    inject(report)
    # COMPACT_REPORT_UI_PATCH_V1
    compact_latest_report(LATEST_REPORT)

    print(f"Creato {OUTPUT_REPORT}")
    print(f"Creato {OUTPUT_JSON}")
    print(f"Stato: {status}")


if __name__ == "__main__":
    main()
