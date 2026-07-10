# -*- coding: utf-8 -*-
"""Applica in sicurezza l'upgrade strutturato al Global Confluence.

Uso dalla radice del repository:
    python apply_global_confluence_upgrade.py

La patch:
- conserva il vecchio parser Markdown come fallback;
- legge prima reports/latest_scanner_summary.csv/json;
- mantiene esattamente le soglie di punteggio già presenti;
- rende il parser Classic compatibile con la nuova etichetta
  "Volatilità tecnica locale";
- crea global_confluence_report.py.bak prima di scrivere.
"""

from __future__ import annotations

import py_compile
import re
import shutil
from pathlib import Path


TARGET = Path("global_confluence_report.py")
MARKER = "# STRUCTURED_SCANNER_PATCH_V1"

WRAPPER = r'''
# STRUCTURED_SCANNER_PATCH_V1
# Prima usa il riepilogo strutturato prodotto da scanner.py; il vecchio parser
# Markdown resta disponibile come fallback per non interrompere il workflow.
def parse_scanner_component(text: str, asset: str):
    structured = None
    try:
        from scanner_signal_reader import scanner_signal
        candidate = scanner_signal(asset)
        if candidate and candidate.get("available"):
            structured = candidate
    except Exception:
        structured = None

    if not structured:
        return _parse_scanner_component_markdown_fallback(text, asset)

    direction = clean_cell(structured.get("direction_30d") or "").upper() or None
    positive_rate = parse_number(structured.get("positive_cases_30d"))
    negative_rate = parse_number(structured.get("negative_cases_30d"))
    return_p50 = parse_number(structured.get("return_p50_pct"))
    price = parse_number(structured.get("current_price"))

    # Se il file strutturato esiste ma la riga è incompleta, non inventa dati:
    # torna al parser precedente.
    if positive_rate is None:
        return _parse_scanner_component_markdown_fallback(text, asset)

    if negative_rate is None:
        negative_rate = 100.0 - positive_rate

    score = 0
    if positive_rate is not None and return_p50 is not None:
        if positive_rate >= 65 and return_p50 > 0:
            score = 3
        elif positive_rate >= 58 and return_p50 >= 0:
            score = 2
        elif positive_rate >= 52 and return_p50 >= 0:
            score = 1
        elif positive_rate <= 20 and return_p50 < 0:
            score = -3
        elif positive_rate <= 35 and return_p50 < 0:
            score = -2
        elif positive_rate < 48 and return_p50 < 0:
            score = -1
    elif positive_rate is not None:
        if positive_rate >= 65:
            score = 1
        elif positive_rate <= 20:
            score = -3
        elif positive_rate <= 35:
            score = -2
        elif positive_rate < 48:
            score = -1

    detail = (
        f"Casi positivi {fmt_pct_plain(positive_rate)}, "
        f"return centrale 30g {fmt_pct(return_p50)}. "
        f"Direzione scanner: {direction or 'n/a'}. "
        "Fonte: latest_scanner_summary strutturato."
    )

    return component_template(
        score=score,
        detail=detail,
        data={
            "direction": direction,
            "positive_rate": positive_rate,
            "negative_rate": negative_rate,
            "return_p50": return_p50,
            "price": price,
            "structured_source": True,
        },
    )

'''


def patch_source(source: str) -> str:
    if MARKER in source:
        return source

    start_match = re.search(
        r"(?m)^def parse_scanner_component\(text: str, asset: str\):\s*\n",
        source,
    )
    next_match = re.search(
        r"(?m)^def parse_scanner_path_component\(block: str, asset: str\):\s*\n",
        source,
    )
    if not start_match or not next_match or next_match.start() <= start_match.start():
        raise RuntimeError(
            "Non trovo i confini di parse_scanner_component. "
            "Il file potrebbe essere cambiato: non è stato modificato."
        )

    old_block = source[start_match.start():next_match.start()]
    fallback_block = old_block.replace(
        "def parse_scanner_component(text: str, asset: str):",
        "def _parse_scanner_component_markdown_fallback(text: str, asset: str):",
        1,
    )

    patched = source[:start_match.start()] + fallback_block.rstrip() + "\n\n" + WRAPPER + source[next_match.start():]

    # Il Classic report può ora chiamare la misura locale "Volatilità tecnica locale".
    # Accetta sia la vecchia sia la nuova etichetta.
    patched = patched.replace(
        'r"Rischio:\\s*\\*\\*([^*]+)\\*\\*"',
        'r"(?:Rischio|Volatilità tecnica locale|Volatilità locale):\\s*\\*\\*([^*]+)\\*\\*"',
    )
    patched = patched.replace(
        "r'Rischio:\\s*\\*\\*([^*]+)\\*\\*'",
        "r'(?:Rischio|Volatilità tecnica locale|Volatilità locale):\\s*\\*\\*([^*]+)\\*\\*'",
    )
    patched = patched.replace(
        "f\"rischio {risk or 'n/a'}. \"",
        "f\"volatilità locale {risk or 'n/a'}. \"",
    )
    return patched


def main() -> None:
    if not TARGET.exists():
        raise SystemExit(f"File non trovato: {TARGET}")

    original = TARGET.read_text(encoding="utf-8")
    patched = patch_source(original)
    if patched == original:
        print("Global Confluence già aggiornato: nessuna modifica.")
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

    print(f"Aggiornato {TARGET}")
    print(f"Backup: {backup}")
    print("Il parser scanner usa ora il CSV/JSON strutturato con fallback Markdown.")


if __name__ == "__main__":
    main()
