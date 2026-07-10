# -*- coding: utf-8 -*-
"""Rinomina la misura ATR del Classic report senza cambiarne il calcolo.

Uso dalla radice del repository:
    python apply_classic_risk_label_upgrade.py

La chiave interna `risk` resta invariata per compatibilità. Cambiano soltanto
le etichette mostrate nel Markdown: da "Rischio" a
"Volatilità tecnica locale". Viene creato un backup .bak.
"""

from __future__ import annotations

import py_compile
import shutil
from pathlib import Path


TARGET = Path("classic_technical_confirmation_report.py")
MARKER = "# CLASSIC_LOCAL_VOLATILITY_LABEL_PATCH_V1"


def patch_source(source: str) -> tuple[str, int]:
    if MARKER in source:
        return source, 0

    changed = 0
    patched = source

    # Etichette isolate usate nelle intestazioni delle tabelle.
    for old, new in [
        ('"Rischio"', '"Volatilità locale"'),
        ("'Rischio'", "'Volatilità locale'"),
    ]:
        count = patched.count(old)
        if count:
            patched = patched.replace(old, new)
            changed += count

    # Etichette nelle righe di dettaglio Markdown.
    replacements = [
        ("- Rischio: **", "- Volatilità tecnica locale: **"),
        ("Rischio tecnico locale: **", "Volatilità tecnica locale: **"),
        ("volatilità e rischio tramite ATR", "volatilità tecnica locale tramite ATR e distanza dai livelli"),
        ("rischio tramite ATR", "volatilità tecnica locale tramite ATR"),
    ]
    for old, new in replacements:
        count = patched.count(old)
        if count:
            patched = patched.replace(old, new)
            changed += count

    # Nota esplicativa inserita vicino alla funzione che calcola la misura.
    anchor = "def risk_label(asset: str, atr_pct, close, support, resistance):"
    if anchor not in patched:
        raise RuntimeError(
            "Non trovo risk_label: il file potrebbe essere cambiato. Nessuna modifica applicata."
        )
    note = (
        MARKER
        + "\n# Questa funzione misura solo volatilità ATR e distanza da supporto/resistenza.\n"
        + "# Non rappresenta il rischio operativo complessivo dell'asset o della leva.\n"
    )
    patched = patched.replace(anchor, note + anchor, 1)
    changed += 1

    return patched, changed


def main() -> None:
    if not TARGET.exists():
        raise SystemExit(f"File non trovato: {TARGET}")

    original = TARGET.read_text(encoding="utf-8")
    patched, changed = patch_source(original)
    if patched == original:
        print("Classic technical già aggiornato: nessuna modifica.")
        return

    backup = TARGET.with_suffix(TARGET.suffix + ".bak")
    if not backup.exists():
        shutil.copy2(TARGET, backup)

    TARGET.write_text(patched, encoding="utf-8", newline="\n")
    try:
        py_compile.compile(str(TARGET), doraise=True)
    except Exception:
        shutil.copy2(backup, TARGET)
        raise

    print(f"Aggiornato {TARGET} ({changed} sostituzioni controllate)")
    print(f"Backup: {backup}")
    print("Il calcolo non è cambiato; è cambiata solo l'etichetta mostrata.")


if __name__ == "__main__":
    main()
