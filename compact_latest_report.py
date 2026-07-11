# -*- coding: utf-8 -*-
"""Rende reports/latest_report.md più leggibile senza eliminare dati.

Il file Markdown conserva tutto il contenuto originale. Le sezioni lunghe vengono
solo racchiuse in blocchi HTML <details>, quindi su GitHub si possono aprire e
chiudere. Copiando il file raw continuano a essere copiati tutti i dati.

La trasformazione è idempotente: può essere eseguita più volte senza annidare o
duplicare i blocchi richiudibili.
"""

from __future__ import annotations

import re
from pathlib import Path


DEFAULT_REPORT_PATH = Path("reports/latest_report.md")

HEADER_START = "<!-- COMPACT_REPORT_HEADER_START -->"
HEADER_END = "<!-- COMPACT_REPORT_HEADER_END -->"
SECTION_START = "<!-- COMPACT_SECTION_START:{key} -->"
SECTION_END = "<!-- COMPACT_SECTION_END:{key} -->"


# Le sezioni operative principali restano aperte. Tutte le altre sono chiuse,
# ma continuano a esistere integralmente nel Markdown raw.
MARKER_SECTIONS = (
    (
        "decision",
        "<!-- DECISION_REPORT_START -->",
        "<!-- DECISION_REPORT_END -->",
        "🧭 Decisione operativa — da leggere per prima",
        True,
    ),
    (
        "module_accuracy",
        "<!-- MODULE_ACCURACY_START -->",
        "<!-- MODULE_ACCURACY_END -->",
        "🧪 Accuratezza moduli e raccolta dati",
        False,
    ),
    (
        "global_weight_calibration",
        "<!-- GLOBAL_WEIGHT_CALIBRATION_START -->",
        "<!-- GLOBAL_WEIGHT_CALIBRATION_END -->",
        "⚖️ Calibrazione pesi Global Confluence",
        False,
    ),
    (
        "risk_calibration",
        "<!-- RISK_CALIBRATION_START -->",
        "<!-- RISK_CALIBRATION_END -->",
        "🛡️ Calibrazione rischio spot / leva",
        False,
    ),
    (
        "global_confluence",
        "<!-- GLOBAL_CONFLUENCE_START -->",
        "<!-- GLOBAL_CONFLUENCE_END -->",
        "🌐 Global Confluence — quadro finale",
        True,
    ),
    (
        "btc_sol_fractal",
        "<!-- BTC_SOL_FRACTAL_START -->",
        "<!-- BTC_SOL_FRACTAL_END -->",
        "🧬 Frattale mirato BTC 2022 / SOL 2026",
        False,
    ),
    (
        "rsi_top_cycle",
        "<!-- RSI_TOP_CYCLE_START -->",
        "<!-- RSI_TOP_CYCLE_END -->",
        "📈 RSI top-cycle SOL",
        False,
    ),
    (
        "sol_onchain",
        "<!-- SOL_ONCHAIN_METRICS_START -->",
        "<!-- SOL_ONCHAIN_METRICS_END -->",
        "⛓️ Metriche on-chain SOL",
        False,
    ),
    (
        "major_alt_lifecycle",
        "<!-- MAJOR_ALT_LIFECYCLE_SQUEEZE_START -->",
        "<!-- MAJOR_ALT_LIFECYCLE_SQUEEZE_END -->",
        "🔄 Lifecycle squeeze / EMA200 SOL",
        False,
    ),
    (
        "daily_change",
        "<!-- DAILY_CHANGE_START -->",
        "<!-- DAILY_CHANGE_END -->",
        "🗓️ Cambiamenti rispetto a ieri",
        True,
    ),
    (
        "bounce_after_drawdown",
        "<!-- BOUNCE_AFTER_DRAWDOWN_START -->",
        "<!-- BOUNCE_AFTER_DRAWDOWN_END -->",
        "↕️ Sequenze rimbalzo / dump",
        False,
    ),
    (
        "scanner_forecast",
        "<!-- SCANNER_FORECAST_TRACKER_START -->",
        "<!-- SCANNER_FORECAST_TRACKER_END -->",
        "🔭 Cono probabilistico dello scanner",
        False,
    ),
    (
        "extreme_cases",
        "<!-- EXTREME_CASES_PATH_START -->",
        "<!-- EXTREME_CASES_PATH_END -->",
        "⚠️ Percorso dei casi estremi",
        False,
    ),
    (
        "market_regime",
        "<!-- MARKET_REGIME_MATCH_START -->",
        "<!-- MARKET_REGIME_MATCH_END -->",
        "🌦️ Market Regime Match",
        False,
    ),
    (
        "classic_technical",
        "<!-- CLASSIC_TECHNICAL_CONFIRMATION_START -->",
        "<!-- CLASSIC_TECHNICAL_CONFIRMATION_END -->",
        "📐 Conferma tecnica classica",
        False,
    ),
    (
        "classic_visual",
        "<!-- CLASSIC_TECHNICAL_VISUAL_START -->",
        "<!-- CLASSIC_TECHNICAL_VISUAL_END -->",
        "🖼️ Grafici e pattern Classic Visual",
        False,
    ),
    (
        "fractal_path",
        "<!-- FRACTAL_PATH_TRACKER_START -->",
        "<!-- FRACTAL_PATH_TRACKER_END -->",
        "🛤️ Tracking percorso frattale SOL/BTC",
        False,
    ),
    (
        "liquidations",
        "<!-- LIQUIDATION_SUMMARY_START -->",
        "<!-- LIQUIDATION_SUMMARY_END -->",
        "💥 Futures e liquidazioni",
        False,
    ),
    (
        "technical_structure",
        "<!-- TECHNICAL_STRUCTURE_START -->",
        "<!-- TECHNICAL_STRUCTURE_END -->",
        "🧱 Struttura tecnica completa e Fibonacci",
        False,
    ),
    (
        "calibration_readable",
        "<!-- CALIBRATION_READABLE_START -->",
        "<!-- CALIBRATION_READABLE_END -->",
        "🎯 Stato leggibile accuratezza / calibrazione",
        False,
    ),
    (
        "data_quality",
        "<!-- DATA_QUALITY_COHERENCE_START -->",
        "<!-- DATA_QUALITY_COHERENCE_END -->",
        "✅ Controllo qualità e coerenza dati",
        False,
    ),
)


def atomic_write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(text, encoding="utf-8", newline="\n")
    tmp.replace(path)


def _strip_header(text: str) -> str:
    pattern = re.compile(
        re.escape(HEADER_START) + r".*?" + re.escape(HEADER_END) + r"\s*",
        flags=re.DOTALL,
    )
    return pattern.sub("", text, count=1)


def _strip_wrapper(text: str, key: str) -> str:
    start = SECTION_START.format(key=key)
    end = SECTION_END.format(key=key)
    pattern = re.compile(
        re.escape(start)
        + r"\s*<details(?:\s+open)?>\s*<summary>.*?</summary>\s*(.*?)\s*</details>\s*"
        + re.escape(end),
        flags=re.DOTALL,
    )
    return pattern.sub(lambda match: match.group(1).strip(), text)


def strip_existing_compaction(text: str) -> str:
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

    return "\n".join(cleaned_lines).strip() + "\n"


def _details_block(key: str, summary: str, content: str, open_by_default: bool) -> str:
    open_attr = " open" if open_by_default else ""
    return (
        f"{SECTION_START.format(key=key)}\n"
        f"<details{open_attr}>\n"
        f"<summary><strong>{summary}</strong></summary>\n\n"
        f"{content.strip()}\n\n"
        f"</details>\n"
        f"{SECTION_END.format(key=key)}"
    )


def _wrap_between_markers(
    text: str,
    key: str,
    start_marker: str,
    end_marker: str,
    summary: str,
    open_by_default: bool,
) -> str:
    start = text.find(start_marker)
    if start < 0:
        return text
    end_pos = text.find(end_marker, start)
    if end_pos < 0:
        return text
    end = end_pos + len(end_marker)
    content = text[start:end]
    wrapper = _details_block(key, summary, content, open_by_default)
    return text[:start].rstrip() + "\n\n" + wrapper + "\n\n" + text[end:].lstrip()


def _wrap_scanner_full_detail(text: str) -> str:
    """Compatta il lungo corpo statistico che non possiede marker propri."""
    start_heading = "# Come leggere questo report"
    end_marker = "<!-- MARKET_REGIME_MATCH_START -->"
    start = text.find(start_heading)
    end = text.find(end_marker, start if start >= 0 else 0)
    if start < 0 or end < 0 or end <= start:
        return text

    content = text[start:end].strip()
    wrapper = _details_block(
        "scanner_full_detail",
        "📚 Scanner statistico completo — percentili, mappe e 40 casi storici",
        content,
        False,
    )
    return text[:start].rstrip() + "\n\n" + wrapper + "\n\n" + text[end:].lstrip()


def _header() -> str:
    return (
        f"{HEADER_START}\n"
        "> **Vista compatta:** Decisione operativa, Global Confluence e cambiamenti giornalieri "
        "restano aperti. Tocca il titolo di una sezione per mostrare o nascondere i dettagli.  \n"
        "> Tutte le tabelle e tutti i dati restano nel file: copiando il Markdown raw viene copiato tutto.\n"
        f"{HEADER_END}"
    )


def validate_compact_structure(text: str) -> None:
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


def compact_text(text: str) -> str:
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

    compacted = _header() + "\n\n" + text.strip() + "\n"
    validate_compact_structure(compacted)
    return compacted


def compact_latest_report(path: Path = DEFAULT_REPORT_PATH) -> bool:
    if not path.exists():
        print(f"Vista compatta non applicata: file mancante {path}")
        return False

    original = path.read_text(encoding="utf-8")
    compacted = compact_text(original)
    changed = compacted != original
    if changed:
        atomic_write(path, compacted)
        print(f"Vista compatta applicata a {path}")
    else:
        print(f"Vista compatta già aggiornata in {path}")
    return changed


def main() -> None:
    compact_latest_report(DEFAULT_REPORT_PATH)


if __name__ == "__main__":
    main()
