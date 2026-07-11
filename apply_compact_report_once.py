# -*- coding: utf-8 -*-
"""Collega la vista compatta al controllo qualità finale dello scanner.

La patch è idempotente e non modifica punteggi, dati, tabelle o workflow.
Aggiunge soltanto una chiamata finale a compact_latest_report.py, dopo che
Data Quality ha scritto il suo blocco in reports/latest_report.md.
"""

from __future__ import annotations

import py_compile
import shutil
from pathlib import Path


QUALITY_PATH = Path("data_quality_coherence_report.py")
COMPACTOR_PATH = Path("compact_latest_report.py")
BACKUP_PATH = Path("data_quality_coherence_report.py.bak_compact_ui")

IMPORT_LINE = "from compact_latest_report import compact_latest_report"
CALL_LINE = "    compact_latest_report(LATEST_REPORT)"
PATCH_MARKER = "# COMPACT_REPORT_UI_PATCH_V1"


def read(path: Path) -> str:
    if not path.exists():
        raise FileNotFoundError(f"File mancante nella radice del repository: {path}")
    return path.read_text(encoding="utf-8")


def patch_quality_report() -> bool:
    original = read(QUALITY_PATH)
    updated = original

    if IMPORT_LINE not in updated:
        anchor = '\n\nREPORTS_DIR = Path("reports")'
        if anchor not in updated:
            raise RuntimeError(
                "Punto di inserimento import non trovato in data_quality_coherence_report.py"
            )
        updated = updated.replace(
            anchor,
            f"\n{IMPORT_LINE}\n\nREPORTS_DIR = Path(\"reports\")",
            1,
        )

    if CALL_LINE not in updated:
        anchor = "    inject(report)\n"
        if anchor not in updated:
            raise RuntimeError(
                "Chiamata inject(report) non trovata in data_quality_coherence_report.py"
            )
        updated = updated.replace(
            anchor,
            anchor + f"    {PATCH_MARKER}\n{CALL_LINE}\n",
            1,
        )

    if updated == original:
        print("data_quality_coherence_report.py: vista compatta già collegata.")
        return False

    if not BACKUP_PATH.exists():
        shutil.copy2(QUALITY_PATH, BACKUP_PATH)
    QUALITY_PATH.write_text(updated, encoding="utf-8", newline="\n")
    print(f"data_quality_coherence_report.py aggiornato; backup: {BACKUP_PATH}")
    return True


def validate() -> None:
    for path in (QUALITY_PATH, COMPACTOR_PATH):
        py_compile.compile(str(path), doraise=True)

    quality = read(QUALITY_PATH)
    compact = read(COMPACTOR_PATH)

    required_quality = (IMPORT_LINE, PATCH_MARKER, CALL_LINE)
    missing_quality = [item for item in required_quality if item not in quality]
    if missing_quality:
        raise RuntimeError("Patch incompleta nel Data Quality: " + ", ".join(missing_quality))

    required_compact = (
        "def compact_latest_report",
        "<details",
        "COMPACT_REPORT_HEADER_START",
        "SCANNER_FORECAST_TRACKER_START",
        "DATA_QUALITY_COHERENCE_START",
    )
    missing_compact = [item for item in required_compact if item not in compact]
    if missing_compact:
        raise RuntimeError("Compactor incompleto: " + ", ".join(missing_compact))

    # Prova rapida: la trasformazione deve essere idempotente e conservare i marker.
    namespace: dict[str, object] = {}
    exec(compile(compact, str(COMPACTOR_PATH), "exec"), namespace)
    sample = """<!-- DECISION_REPORT_START -->\n# Decisione\n| A | B |\n|---|---|\n|1|2|\n<!-- DECISION_REPORT_END -->\n\n# Come leggere questo report\nDati completi\n\n<!-- MARKET_REGIME_MATCH_START -->\n# Regime\n<!-- MARKET_REGIME_MATCH_END -->\n\n<!-- DATA_QUALITY_COHERENCE_START -->\n# Quality\n<!-- DATA_QUALITY_COHERENCE_END -->\n"""
    compact_text = namespace["compact_text"]
    first = compact_text(sample)  # type: ignore[operator]
    second = compact_text(first)  # type: ignore[operator]
    if first != second:
        raise RuntimeError("La vista compatta non è idempotente.")
    for marker in (
        "<!-- DECISION_REPORT_START -->",
        "<!-- DECISION_REPORT_END -->",
        "<!-- MARKET_REGIME_MATCH_START -->",
        "<!-- DATA_QUALITY_COHERENCE_END -->",
    ):
        if marker not in first:
            raise RuntimeError(f"Marker perso durante la prova: {marker}")

    print("Compilazione, conservazione marker e idempotenza: OK")


def main() -> None:
    read(COMPACTOR_PATH)
    patch_quality_report()
    validate()
    print("Vista compatta installata con successo.")


if __name__ == "__main__":
    main()
