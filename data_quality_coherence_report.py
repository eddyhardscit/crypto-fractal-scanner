# -*- coding: utf-8 -*-
"""Final non-invasive quality check for the generated crypto reports.

It does not change trading scores. It checks encoding, structured scanner data,
shared-price consistency and a few common report contradictions, then appends a
small diagnostic block to reports/latest_report.md.
"""

from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

from market_snapshot import load_market_snapshot, get_snapshot_price
from scanner_signal_reader import load_scanner_summary, validate_scanner_summary


REPORTS_DIR = Path("reports")
LATEST_REPORT = REPORTS_DIR / "latest_report.md"
OUTPUT_REPORT = REPORTS_DIR / "data_quality_coherence_report.md"
OUTPUT_JSON = REPORTS_DIR / "data_quality_coherence.json"

START_MARKER = "<!-- DATA_QUALITY_COHERENCE_START -->"
END_MARKER = "<!-- DATA_QUALITY_COHERENCE_END -->"

ASSETS = ["BTC", "SOL", "DOGE"]
MOJIBAKE_TOKENS = ["Ã", "Â", "â€", "â†", "ðŸ", "�"]


def utc_now_text() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")


def safe_float(value: Any) -> float:
    try:
        value = float(value)
        return value if np.isfinite(value) else np.nan
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


def scanner_vs_snapshot_checks(summary: pd.DataFrame, snapshot: dict[str, Any]) -> list[dict[str, Any]]:
    checks = []
    if summary.empty or "asset" not in summary.columns:
        return checks

    for asset in ASSETS:
        row = summary[summary["asset"].astype(str).str.upper().str.replace("-USD", "", regex=False) == asset]
        scanner_price = safe_float(row.iloc[0].get("current_price")) if not row.empty else np.nan
        snapshot_price = safe_float(get_snapshot_price(snapshot, asset))

        if np.isnan(scanner_price) or np.isnan(snapshot_price) or snapshot_price == 0:
            checks.append({
                "asset": asset,
                "status": "WARN",
                "scanner_price": scanner_price,
                "snapshot_price": snapshot_price,
                "difference_pct": np.nan,
                "message": "Prezzo scanner o snapshot mancante.",
            })
            continue

        diff = (scanner_price / snapshot_price - 1) * 100
        status = "OK" if abs(diff) <= 0.25 else "WARN"
        checks.append({
            "asset": asset,
            "status": status,
            "scanner_price": scanner_price,
            "snapshot_price": snapshot_price,
            "difference_pct": diff,
            "message": "Prezzi coerenti." if status == "OK" else "Differenza oltre 0,25%: controllare l'uso dello snapshot condiviso.",
        })
    return checks


def detect_global_scanner_na(text: str, summary: pd.DataFrame) -> list[str]:
    if summary.empty:
        return []
    global_block = section(text, "<!-- GLOBAL_CONFLUENCE_START -->", "<!-- GLOBAL_CONFLUENCE_END -->")
    if not global_block:
        return ["Blocco Global Confluence non trovato nel report principale."]

    issues = []
    patterns = [
        r"return centrale 30g\s+n/?a",
        r"Direzione scanner:\s*n/?a",
    ]
    for pattern in patterns:
        if re.search(pattern, global_block, flags=re.IGNORECASE):
            issues.append(
                "Il Global Confluence mostra ancora dati scanner n/a nonostante latest_scanner_summary sia disponibile."
            )
            break
    return issues


def detect_risk_naming_ambiguity(text: str) -> list[str]:
    decision = section(text, "<!-- DECISION_REPORT_START -->", "<!-- DECISION_REPORT_END -->")
    classic = section(
        text,
        "<!-- CLASSIC_TECHNICAL_CONFIRMATION_START -->",
        "<!-- CLASSIC_TECHNICAL_CONFIRMATION_END -->",
    )
    if not decision or not classic:
        return []

    doge_decision_high = bool(re.search(r"DOGE.*?Rischio:\s*\*\*MOLTO ALTO\*\*", decision, re.I | re.S))
    doge_classic_low = bool(re.search(r"###\s+DOGE.*?Rischio:\s*\*\*BASSO\*\*", classic, re.I | re.S))

    if doge_decision_high and doge_classic_low:
        return [
            "DOGE ha rischio globale MOLTO ALTO ma rischio Classic BASSO. Non è per forza un errore: il secondo è volatilità/rischio tecnico locale. Va rinominato per evitare ambiguità."
        ]
    return []


def fmt_pct(value: Any) -> str:
    value = safe_float(value)
    if np.isnan(value):
        return "n/a"
    return f"{value:+.3f}%".replace(".", ",")


def fmt_price(asset: str, value: Any) -> str:
    value = safe_float(value)
    if np.isnan(value):
        return "n/a"
    if asset == "DOGE":
        return f"{value:.5f} $"
    if value >= 1000:
        return f"{value:,.0f} $".replace(",", ".")
    return f"{value:.2f} $".replace(".", ",")


def render(payload: dict[str, Any]) -> str:
    lines = [
        "# Data quality / coherence check",
        "",
        f"Generato: {payload['generated_at_utc']}",
        "",
        "Questo controllo non modifica punteggi o decisioni. Segnala soltanto problemi tecnici, dati mancanti e ambiguità di lettura.",
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

    lines += ["## Coerenza prezzi snapshot", ""]
    rows = []
    for item in payload["price_checks"]:
        rows.append({
            "Asset": item["asset"],
            "Stato": item["status"],
            "Snapshot": fmt_price(item["asset"], item["snapshot_price"]),
            "Scanner": fmt_price(item["asset"], item["scanner_price"]),
            "Differenza": fmt_pct(item["difference_pct"]),
        })
    if rows:
        lines.append(pd.DataFrame(rows).to_markdown(index=False))
    else:
        lines.append("_Dati prezzo non disponibili._")
    lines.append("")

    lines += ["## Controllo codifica UTF-8", ""]
    if payload["mojibake"]:
        total = sum(item["count"] for item in payload["mojibake"])
        lines.append(f"Trovati **{total}** possibili frammenti con codifica rotta nel report principale.")
        lines.append("")
        for item in payload["mojibake"]:
            lines.append(f"- Token `{item['token']}`: {item['count']} occorrenze")
    else:
        lines.append("Nessun indicatore comune di mojibake trovato.")
    lines.append("")

    lines += ["## File strutturati", ""]
    lines.append(f"- Snapshot condiviso: **{'OK' if payload['snapshot_available'] else 'MANCANTE'}**")
    lines.append(f"- Scanner summary: **{'OK' if payload['scanner_summary_available'] else 'MANCANTE'}**")
    lines.append("")

    if payload["overall_status"] == "OK":
        lines.append("Il workflow è tecnicamente coerente nei controlli disponibili.")
    elif payload["overall_status"] == "WARN":
        lines.append("Il workflow può continuare, ma gli avvisi sopra vanno sistemati per rendere il report più affidabile e leggibile.")
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
    snapshot = load_market_snapshot(max_age_hours=36)

    critical = []
    warnings = []

    scanner_validation = validate_scanner_summary()
    if scanner_validation:
        critical.extend(scanner_validation)

    if not snapshot:
        critical.append("Snapshot condiviso mancante, non leggibile o più vecchio di 36 ore.")

    mojibake = find_mojibake(text)
    if mojibake:
        warnings.append("Il report contiene ancora caratteri corrotti: verificare sorgente e scrittura UTF-8.")

    warnings.extend(detect_global_scanner_na(text, summary))
    warnings.extend(detect_risk_naming_ambiguity(text))

    price_checks = scanner_vs_snapshot_checks(summary, snapshot)
    if any(item["status"] != "OK" for item in price_checks):
        warnings.append("Almeno un prezzo scanner non coincide con lo snapshot condiviso entro la tolleranza dello 0,25%.")

    if critical:
        status = "ERROR"
    elif warnings:
        status = "WARN"
    else:
        status = "OK"

    payload = {
        "schema_version": 1,
        "generated_at_utc": utc_now_text(),
        "overall_status": status,
        "critical_issues": list(dict.fromkeys(critical)),
        "warnings": list(dict.fromkeys(warnings)),
        "snapshot_available": bool(snapshot),
        "scanner_summary_available": not summary.empty,
        "price_checks": price_checks,
        "mojibake": mojibake,
    }

    report = render(payload)
    atomic_write(OUTPUT_REPORT, report.rstrip() + "\n")
    atomic_write(OUTPUT_JSON, json.dumps(payload, ensure_ascii=False, indent=2, default=str) + "\n")
    inject(report)

    print(f"Creato {OUTPUT_REPORT}")
    print(f"Creato {OUTPUT_JSON}")
    print(f"Stato: {status}")


if __name__ == "__main__":
    main()
