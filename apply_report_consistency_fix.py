# -*- coding: utf-8 -*-
"""Applica due correzioni mirate allo scanner.

1) Vista compatta: evita wrapper HTML incrociati tra Scanner completo e Market Regime.
2) Frattale SOL/BTC: usa giorni di calendario e allinea report principale e tracker.

La patch è idempotente e non modifica punteggi, pesi o logiche operative.
"""

from __future__ import annotations

import py_compile
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def first_existing(*names: str) -> Path:
    """Restituisce il primo nome realmente presente nel repository."""
    for name in names:
        candidate = ROOT / name
        if candidate.exists():
            return candidate
    # Conserva il nome preferito nel messaggio di errore di require().
    return ROOT / names[0]


FILES = {
    "compact": first_existing("compact_latest_report.py"),
    # Il file reale del progetto termina con _report.py. Manteniamo il secondo
    # nome solo per compatibilità con eventuali vecchie copie del repository.
    "fractal": first_existing(
        "btc_2022_vs_sol_2026_report.py",
        "btc_2022_vs_sol_2026.py",
    ),
    "tracker": first_existing("fractal_path_tracker.py"),
}


def write(path: Path, text: str) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(text, encoding="utf-8", newline="\n")
    tmp.replace(path)


def require(path: Path) -> str:
    if not path.exists():
        raise FileNotFoundError(f"File richiesto mancante: {path.name}")
    return path.read_text(encoding="utf-8")


def patch_compact(path: Path) -> bool:
    text = require(path)
    original = text

    if "Rimuove anche wrapper compatti malformati" not in text:
        replacement = '''def strip_existing_compaction(text: str) -> str:
    """Rimuove anche wrapper compatti malformati o annidati male.

    La prima versione usava una regex per ogni sezione. Con wrapper HTML
    accidentalmente incrociati, quella strategia poteva lasciare marker orfani.
    Qui eliminiamo soltanto le righe generate dalla vista compatta, conservando
    integralmente il contenuto reale del report.
    """
    text = _strip_header(text)
    cleaned_lines = []
    compact_marker = re.compile(r"^<!-- COMPACT_SECTION_(?:START|END):[^>]+ -->$")
    generated_summary = re.compile(r"^<summary><strong>.*</strong></summary>$")

    for line in text.splitlines():
        stripped = line.strip()
        if compact_marker.fullmatch(stripped):
            continue
        if stripped in {"<details>", "<details open>", "</details>"}:
            continue
        if generated_summary.fullmatch(stripped):
            continue
        cleaned_lines.append(line)

    return "\\n".join(cleaned_lines).strip() + "\\n"


def _details_block'''
        text, count = re.subn(
            r"def strip_existing_compaction\(text: str\) -> str:\n.*?\n\n\ndef _details_block",
            lambda _match: replacement,
            text,
            flags=re.S,
        )
        if count != 1:
            raise RuntimeError("Impossibile aggiornare strip_existing_compaction().")

    if "def validate_compact_structure" not in text:
        validator = '''def validate_compact_structure(text: str) -> None:
    """Blocca la scrittura se i wrapper risultano incrociati o incompleti."""
    token_re = re.compile(r"<!-- COMPACT_SECTION_(START|END):([^>]+) -->")
    stack: list[str] = []
    seen_start: set[str] = set()
    seen_end: set[str] = set()

    for match in token_re.finditer(text):
        kind, key = match.group(1), match.group(2)
        if kind == "START":
            if key in seen_start:
                raise RuntimeError(f"Wrapper compatto duplicato: {key}")
            seen_start.add(key)
            stack.append(key)
        else:
            seen_end.add(key)
            if not stack:
                raise RuntimeError(f"Chiusura compatta senza apertura: {key}")
            current = stack.pop()
            if current != key:
                raise RuntimeError(
                    f"Wrapper compatti incrociati: attesa chiusura {current}, trovata {key}"
                )

    if stack:
        raise RuntimeError(f"Wrapper compatti non chiusi: {', '.join(stack)}")
    if seen_start != seen_end:
        missing = sorted(seen_start.symmetric_difference(seen_end))
        raise RuntimeError(f"Marker compatti incompleti: {', '.join(missing)}")

    for key, start_marker, end_marker, *_ in MARKER_SECTIONS:
        wrapper_start = SECTION_START.format(key=key)
        wrapper_end = SECTION_END.format(key=key)
        if start_marker not in text or end_marker not in text:
            continue
        ws = text.find(wrapper_start)
        we = text.find(wrapper_end, ws)
        ms = text.find(start_marker)
        me = text.find(end_marker, ms)
        if min(ws, we, ms, me) < 0 or not (ws < ms < me < we):
            raise RuntimeError(
                f"Sezione compatta {key} non contiene correttamente i propri marker."
            )


'''
        text = text.replace("def compact_text(text: str) -> str:\n", validator + "def compact_text(text: str) -> str:\n", 1)

    compact_body = '''def compact_text(text: str) -> str:
    text = strip_existing_compaction(text)

    # Prima separiamo il lungo corpo statistico. Va fatto PRIMA di avvolgere
    # Market Regime, altrimenti l'apertura del wrapper Market può finire dentro
    # Scanner Full Detail e produrre tag HTML incrociati.
    text = _wrap_scanner_full_detail(text)

    for key, start, end, summary, open_by_default in MARKER_SECTIONS:
        text = _wrap_between_markers(
            text,
            key,
            start,
            end,
            summary,
            open_by_default,
        )

    compacted = _header() + "\\n\\n" + text.strip() + "\\n"
    validate_compact_structure(compacted)
    return compacted


def compact_latest_report'''
    text, count = re.subn(
        r"def compact_text\(text: str\) -> str:\n.*?\n\n\ndef compact_latest_report",
        lambda _match: compact_body,
        text,
        flags=re.S,
    )
    if count != 1:
        raise RuntimeError("Impossibile aggiornare compact_text().")

    if text != original:
        write(path, text)
        return True
    return False


def patch_fractal(path: Path) -> bool:
    text = require(path)
    original = text

    if "def calendarize_path(path):" not in text:
        helper = '''def calendarize_path(path):
    """Rende il percorso realmente giornaliero, colmando eventuali buchi Yahoo.

    BTC e SOL trattano i giorni del frattale come giorni di calendario. Se Yahoo
    salta una candela, usare semplicemente ``len(path) - 1`` crea uno
    sfalsamento di un giorno tra report principale e tracker. Il forward-fill è
    coerente con la logica ``close on or before`` già usata dal tracker.
    """
    if path is None or path.empty:
        return pd.DataFrame()

    out = path.copy()
    out.index = pd.to_datetime(out.index, errors="coerce")
    try:
        out.index = out.index.tz_convert(None)
    except Exception:
        try:
            out.index = out.index.tz_localize(None)
        except Exception:
            pass

    out.index = out.index.normalize()
    out = out[~out.index.duplicated(keep="last")].sort_index()
    full_index = pd.date_range(out.index.min(), out.index.max(), freq="D")
    out = out.reindex(full_index)

    if "Volume" in out.columns:
        out["Volume"] = out["Volume"].fillna(0)

    other_cols = [col for col in out.columns if col != "Volume"]
    if other_cols:
        out[other_cols] = out[other_cols].ffill()

    out.index.name = path.index.name
    return out


'''
        text = text.replace("def to_numeric_series(values):\n", helper + "def to_numeric_series(values):\n", 1)

    text = text.replace(
        '''    btc_path = normalize_path(btc, btc_anchor_date, btc_anchor_price)\n    sol_path = normalize_path(sol, sol_anchor_date, sol_anchor_price)\n''',
        '''    btc_path = calendarize_path(normalize_path(btc, btc_anchor_date, btc_anchor_price))\n    sol_path = calendarize_path(normalize_path(sol, sol_anchor_date, sol_anchor_price))\n''',
        1,
    )

    if "expected_btc_equiv_date" not in text:
        old = '''    btc_equiv_date = btc_path.index[btc_equiv_idx]\n    btc_norm_equiv = safe_float(btc_path["norm"].iloc[btc_equiv_idx])\n'''
        new = '''    btc_equiv_date = btc_path.index[btc_equiv_idx]\n    expected_btc_equiv_date = pd.to_datetime(btc_anchor_date).normalize() + pd.Timedelta(days=sol_elapsed_days)\n    if pd.to_datetime(btc_equiv_date).normalize() != expected_btc_equiv_date:\n        raise RuntimeError(\n            "Allineamento frattale incoerente: la data BTC equivalente non "\n            "corrisponde ai giorni di calendario dal bottom SOL."\n        )\n    btc_norm_equiv = safe_float(btc_path["norm"].iloc[btc_equiv_idx])\n'''
        if old not in text:
            raise RuntimeError("Impossibile inserire il controllo della data BTC equivalente.")
        text = text.replace(old, new, 1)

    if text != original:
        write(path, text)
        return True
    return False


def patch_tracker(path: Path) -> bool:
    text = require(path)
    original = text

    if '"sol_current_date_from_report"' not in text:
        old = '''            "sol_day_from_report": int(safe_float(structured.get("sol_elapsed_days"), 0) or 0),\n            "btc_equiv_from_report": btc_equiv,\n'''
        new = '''            "sol_day_from_report": int(safe_float(structured.get("sol_elapsed_days"), 0) or 0),\n            "sol_current_date_from_report": parse_date_any(structured.get("sol_current_date")),\n            "sol_current_price_from_report": safe_float(structured.get("sol_current_price")),\n            "btc_equiv_from_report": btc_equiv,\n'''
        if old not in text:
            raise RuntimeError("Impossibile aggiungere data/prezzo autorevoli al tracker.")
        text = text.replace(old, new, 1)

        old_fb = '''        "sol_day_from_report": sol_day,\n        "btc_equiv_from_report": btc_equiv,\n'''
        new_fb = '''        "sol_day_from_report": sol_day,\n        "sol_current_date_from_report": None,\n        "sol_current_price_from_report": np.nan,\n        "btc_equiv_from_report": btc_equiv,\n'''
        if old_fb not in text:
            raise RuntimeError("Impossibile aggiornare il fallback del tracker.")
        text = text.replace(old_fb, new_fb, 1)

    old_date = '''    latest_sol_date = available_date_on_or_before(sol_df, sol_df.index.max())\n    if latest_sol_date is None:\n        raise RuntimeError("Nessuna data SOL disponibile.")\n\n    day_count = int((latest_sol_date - sol_bottom_date).days)\n    rows = []\n'''
    if old_date in text:
        new_date = '''    report_current_date = metadata.get("sol_current_date_from_report")\n    if report_current_date is not None:\n        latest_sol_date = available_date_on_or_before(sol_df, report_current_date)\n    else:\n        latest_sol_date = available_date_on_or_before(sol_df, sol_df.index.max())\n\n    if latest_sol_date is None:\n        raise RuntimeError("Nessuna data SOL disponibile.")\n\n    # Il giorno del frattale è sempre una distanza di calendario dal bottom.\n    # Non va ricavato dal numero di righe scaricate, perché Yahoo può saltare\n    # una candela e creare uno sfalsamento di un giorno.\n    day_count = int((latest_sol_date - sol_bottom_date).days)\n    rows = []\n'''
        text = text.replace(old_date, new_date, 1)

    old_price = '''        sol_price = close_on_or_before(sol_df, sol_date)\n        btc_price = close_on_or_before(btc_df, btc_date)\n\n        if pd.isna(sol_price) or pd.isna(btc_price):\n            continue\n'''
    if old_price in text:
        new_price = '''        sol_price = close_on_or_before(sol_df, sol_date)\n        btc_price = close_on_or_before(btc_df, btc_date)\n\n        if day == day_count:\n            report_price = safe_float(metadata.get("sol_current_price_from_report"))\n            if not pd.isna(report_price):\n                sol_price = report_price\n\n        if pd.isna(sol_price) or pd.isna(btc_price):\n            continue\n'''
        text = text.replace(old_price, new_price, 1)

    if "Tracker e frattale principale sfalsati" not in text:
        old_return = '''    tracking = pd.DataFrame(rows)\n    if tracking.empty:\n        raise RuntimeError("Tracking frattale vuoto.")\n    return tracking\n'''
        new_return = '''    tracking = pd.DataFrame(rows)\n    if tracking.empty:\n        raise RuntimeError("Tracking frattale vuoto.")\n\n    latest = tracking.iloc[-1]\n    expected_btc_date = btc_bottom_date + pd.Timedelta(days=int(latest["day"]))\n    actual_btc_date = pd.Timestamp(latest["btc_equiv_date"]).normalize()\n    if actual_btc_date != expected_btc_date:\n        raise RuntimeError(\n            "Tracker frattale incoerente: la data BTC equivalente non "\n            "corrisponde al giorno di calendario dal bottom."\n        )\n\n    report_day = int(safe_float(metadata.get("sol_day_from_report"), -1))\n    report_btc_date = metadata.get("btc_equiv_from_report")\n    if metadata.get("source") == "structured_csv":\n        if report_day >= 0 and int(latest["day"]) != report_day:\n            raise RuntimeError(\n                f"Tracker e frattale principale sfalsati: giorno tracker "\n                f"{int(latest['day'])}, giorno report {report_day}."\n            )\n        if report_btc_date is not None:\n            report_btc_date = pd.Timestamp(report_btc_date).normalize()\n            if actual_btc_date != report_btc_date:\n                raise RuntimeError(\n                    "Tracker e frattale principale usano date BTC equivalenti diverse."\n                )\n\n    return tracking\n'''
        if old_return not in text:
            raise RuntimeError("Impossibile inserire il controllo incrociato nel tracker.")
        text = text.replace(old_return, new_return, 1)

    text = text.replace(
        '''- Giorni controllati dal bottom: **{len(tracking)}**\n- Giorni controllati da inizio programma/scanner: **{len(from_program)}**\n''',
        '''- Giorno corrente dal bottom: **{int(latest["day"])}**\n- Osservazioni inclusive dal bottom: **{len(tracking)}**\n- Osservazioni da inizio programma/scanner: **{len(from_program)}**\n''',
        1,
    )

    if text != original:
        write(path, text)
        return True
    return False


def verify() -> None:
    for path in FILES.values():
        py_compile.compile(str(path), doraise=True)

    compact = require(FILES["compact"])
    required_compact = [
        "def validate_compact_structure",
        "text = _wrap_scanner_full_detail(text)",
        "compacted = _header()",
    ]
    for token in required_compact:
        if token not in compact:
            raise RuntimeError(f"Verifica vista compatta fallita: manca {token}")

    fractal = require(FILES["fractal"])
    for token in ["def calendarize_path(path):", "expected_btc_equiv_date"]:
        if token not in fractal:
            raise RuntimeError(f"Verifica frattale fallita: manca {token}")

    tracker = require(FILES["tracker"])
    for token in [
        "sol_current_date_from_report",
        "Tracker e frattale principale sfalsati",
        "Giorno corrente dal bottom",
    ]:
        if token not in tracker:
            raise RuntimeError(f"Verifica tracker fallita: manca {token}")


def main() -> None:
    changed = []
    if patch_compact(FILES["compact"]):
        changed.append(FILES["compact"].name)
    if patch_fractal(FILES["fractal"]):
        changed.append(FILES["fractal"].name)
    if patch_tracker(FILES["tracker"]):
        changed.append(FILES["tracker"].name)

    verify()
    print("Correzione report/frattale verificata.")
    if changed:
        print("File modificati:")
        for name in changed:
            print(f"- {name}")
    else:
        print("Correzione già presente: nessun file da modificare.")


if __name__ == "__main__":
    main()
