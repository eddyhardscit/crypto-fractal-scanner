# -*- coding: utf-8 -*-
# Applica due correzioni logiche conservative e idempotenti:
# 1) RSI top-cycle SOL: BASSO/MEDIO=0, ALTO=-1, MOLTO ALTO=-2.
# 2) BTC leva: nessun long a leva finché lo snapshot non supera 67.248 $.

from __future__ import annotations

import py_compile
import re
import shutil
from pathlib import Path


GLOBAL_PATH = Path("global_confluence_report.py")
DECISION_PATH = Path("decision_report.py")

BTC_LONG_CONFIRMATION_PRICE = 67_248.0


def replace_once(text: str, pattern: str, replacement: str, label: str) -> str:
    updated, count = re.subn(pattern, replacement, text, count=1, flags=re.DOTALL)
    if count != 1:
        raise RuntimeError(f"Patch non applicata a {label}: blocco atteso non trovato.")
    return updated


def patch_global() -> bool:
    if not GLOBAL_PATH.exists():
        raise FileNotFoundError(GLOBAL_PATH)

    original = GLOBAL_PATH.read_text(encoding="utf-8")

    if '"MOLTO ALTO": -2' in original and '"BASSO": 0' in original:
        print("global_confluence_report.py: patch RSI già presente.")
        return False

    replacement = '''def parse_rsi_component(block: str, asset: str):
    if asset != "SOL":
        return component_template(0, "Non applicabile a questo asset.")

    risk = None
    for line in block.splitlines():
        cells = split_md_row(line)
        if not cells or len(cells) < 2:
            continue
        if "Rischio top-cycle RSI" in cells[0]:
            risk = clean_cell(cells[1]).upper()
            break

    # Questo modulo misura il rischio di top, non la forza rialzista.
    # Un rischio BASSO o MEDIO non deve aggiungere punti al Global.
    score_by_risk = {
        "BASSO": 0,
        "MEDIO": 0,
        "ALTO": -1,
        "MOLTO ALTO": -2,
    }
    score = score_by_risk.get(risk, 0)

    return component_template(
        score,
        f"Rischio top-cycle RSI: {risk or 'n/a'}.",
        {"risk": risk},
    )


'''

    updated = replace_once(
        original,
        r"def parse_rsi_component\(block: str, asset: str\):.*?(?=def parse_lifecycle_component\(block: str, asset: str\):)",
        replacement,
        "parse_rsi_component",
    )

    backup = GLOBAL_PATH.with_suffix(".py.bak_final_logic")
    shutil.copy2(GLOBAL_PATH, backup)
    GLOBAL_PATH.write_text(updated, encoding="utf-8", newline="\n")
    print("global_confluence_report.py: RSI top-cycle corretto.")
    return True


def patch_decision() -> bool:
    if not DECISION_PATH.exists():
        raise FileNotFoundError(DECISION_PATH)

    original = DECISION_PATH.read_text(encoding="utf-8")
    updated = original
    changed = False

    if "MARKET_SNAPSHOT_CSV_PATH" not in updated:
        anchor = 'RISK_CALIBRATION_METRICS_PATH = REPORTS_DIR / "risk_calibration_metrics.csv"'
        if anchor not in updated:
            raise RuntimeError("Costante RISK_CALIBRATION_METRICS_PATH non trovata.")
        updated = updated.replace(
            anchor,
            anchor
            + '\nMARKET_SNAPSHOT_CSV_PATH = REPORTS_DIR / "latest_market_snapshot.csv"'
            + f"\nBTC_LONG_CONFIRMATION_PRICE = {BTC_LONG_CONFIRMATION_PRICE:.1f}",
            1,
        )
        changed = True

    if "def read_snapshot_prices():" not in updated:
        snapshot_function = '''def read_snapshot_prices():
    # Legge i prezzi coerenti creati da market_snapshot.py.
    rows = read_csv_rows(MARKET_SNAPSHOT_CSV_PATH)
    out = {}
    for row in rows:
        asset = clean_cell(row.get("asset") or row.get("Asset")).upper()
        if asset not in ASSETS:
            continue
        price = parse_number(
            row.get("price")
            or row.get("close")
            or row.get("current_price"),
            None,
        )
        if price is not None:
            out[asset] = float(price)
    return out


'''
        marker = "def read_global_from_csv():"
        if marker not in updated:
            raise RuntimeError("Funzione read_global_from_csv non trovata.")
        updated = updated.replace(marker, snapshot_function + marker, 1)
        changed = True

    desired_long_function = '''def long_action(asset: str, score: int, direction: str, risk: str, current_price=None):
    risk_u = clean_cell(risk).upper()

    if asset == "BTC":
        # Lo score statistico può giustificare accumulo spot, ma non basta
        # per autorizzare leva durante Stage 4 / struttura non confermata.
        price = parse_number(current_price, None)
        if price is None:
            return "NO LONG A LEVA / SNAPSHOT NON DISPONIBILE"
        if price < BTC_LONG_CONFIRMATION_PRICE:
            return "NO LONG A LEVA / ATTENDI SOPRA 67.248 $"
        if score >= 3 and "MOLTO ALTO" not in risk_u:
            return "LONG PRUDENTE"
        return "NO LONG A LEVA"

    if asset == "SOL":
        if score >= 7 and risk_u not in {"MOLTO ALTO", "ALTO"}:
            return "LONG SOLO SU CONFERMA"
        return "NO LONG A LEVA"

    if asset == "DOGE":
        return "NO LONG A LEVA"

    return "NO LONG A LEVA"


'''

    current_long_match = re.search(
        r"def long_action\(asset: str, score: int, direction: str, risk: str(?:, current_price=None)?\):.*?(?=def short_action\(asset: str, score: int, direction: str\):)",
        updated,
        flags=re.DOTALL,
    )
    if not current_long_match:
        raise RuntimeError("Funzione long_action non trovata.")

    current_long = current_long_match.group(0)
    if "ATTENDI SOPRA 67.248" not in current_long:
        updated = (
            updated[: current_long_match.start()]
            + desired_long_function
            + updated[current_long_match.end() :]
        )
        changed = True

    build_marker = '''def build_decisions(global_data: dict, risk_data: dict):
    rows = []
    details = {}
'''
    build_replacement = '''def build_decisions(global_data: dict, risk_data: dict):
    rows = []
    details = {}
    snapshot_prices = read_snapshot_prices()
'''
    if "snapshot_prices = read_snapshot_prices()" not in updated:
        if build_marker not in updated:
            raise RuntimeError("Inizio build_decisions non trovato.")
        updated = updated.replace(build_marker, build_replacement, 1)
        changed = True

    old_call = "long_sig = long_action(asset, score, direction, risk)"
    new_call = "long_sig = long_action(asset, score, direction, risk, snapshot_prices.get(asset))"
    if old_call in updated:
        updated = updated.replace(old_call, new_call, 1)
        changed = True
    elif new_call not in updated:
        raise RuntimeError("Chiamata long_action non trovata.")

    note_line = (
        '    lines.append("- **BTC leva** = nessun long a leva finché il prezzo snapshot '
        'non supera **67.248 $**; sotto quella soglia resta solo accumulo spot prudente.")\n'
    )
    if "**BTC leva**" not in updated:
        note_anchor = (
            '    lines.append("- **Zona bassa storica** = zona di rischio; '
            'con leva la liquidazione non dovrebbe stare lì vicino.")\n'
        )
        if note_anchor not in updated:
            raise RuntimeError("Punto di inserimento nota BTC leva non trovato.")
        updated = updated.replace(note_anchor, note_anchor + note_line, 1)
        changed = True

    if not changed:
        print("decision_report.py: patch BTC leva già presente.")
        return False

    backup = DECISION_PATH.with_suffix(".py.bak_final_logic")
    shutil.copy2(DECISION_PATH, backup)
    DECISION_PATH.write_text(updated, encoding="utf-8", newline="\n")
    print("decision_report.py: filtro BTC leva sopra 67.248 $ applicato.")
    return True


def validate() -> None:
    py_compile.compile(str(GLOBAL_PATH), doraise=True)
    py_compile.compile(str(DECISION_PATH), doraise=True)

    global_text = GLOBAL_PATH.read_text(encoding="utf-8")
    decision_text = DECISION_PATH.read_text(encoding="utf-8")

    required = [
        ('"BASSO": 0', global_text),
        ('"MEDIO": 0', global_text),
        ('"ALTO": -1', global_text),
        ('"MOLTO ALTO": -2', global_text),
        ("BTC_LONG_CONFIRMATION_PRICE = 67248.0", decision_text),
        ("ATTENDI SOPRA 67.248", decision_text),
        ("snapshot_prices = read_snapshot_prices()", decision_text),
    ]
    missing = [needle for needle, haystack in required if needle not in haystack]
    if missing:
        raise RuntimeError("Validazione patch fallita: " + ", ".join(missing))

    print("Validazione finale: OK.")


def main() -> None:
    patch_global()
    patch_decision()
    validate()


if __name__ == "__main__":
    main()
