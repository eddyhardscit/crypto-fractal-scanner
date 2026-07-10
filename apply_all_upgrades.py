# -*- coding: utf-8 -*-
"""Applica tutte le patch conservative del pacchetto upgrade.

Eseguire dalla radice del repository dopo aver caricato i nuovi file:
    python apply_all_upgrades.py
"""

from __future__ import annotations

import py_compile
from pathlib import Path

import apply_classic_risk_label_upgrade
import apply_daily_workflow_upgrade
import apply_global_confluence_upgrade


FILES_TO_COMPILE = [
    "scanner.py",
    "market_snapshot.py",
    "scanner_signal_reader.py",
    "data_quality_coherence_report.py",
    "global_confluence_report.py",
    "classic_technical_confirmation_report.py",
]


def main() -> None:
    print("1/3 — Global Confluence")
    apply_global_confluence_upgrade.main()
    print("\n2/3 — Etichetta volatilità Classic")
    apply_classic_risk_label_upgrade.main()
    print("\n3/3 — Workflow giornaliero")
    apply_daily_workflow_upgrade.main()

    print("\nControllo sintassi Python...")
    for filename in FILES_TO_COMPILE:
        path = Path(filename)
        if not path.exists():
            raise SystemExit(f"File richiesto mancante: {filename}")
        py_compile.compile(str(path), doraise=True)
        print(f"OK: {filename}")

    print("\nUpgrade applicato. Ora esegui manualmente il workflow Daily Crypto Fractal Scanner.")


if __name__ == "__main__":
    main()
