# -*- coding: utf-8 -*-
"""Apply the Exchange Microstructure v2.1.1 corrective patch.

This patch assumes v2.1 is already installed. It:
- removes the visible installer marker from Module Accuracy;
- calibrates the exchange candidate, while Global remains locked by its own gate;
- gives Exchange Microstructure a dedicated 0.20% price tolerance;
- adds the committed exchange source diagnostics file to Data Quality;
- fixes daily execution order: save snapshot -> update tracker -> refresh report;
- prepares daily.yml without collecting intraday data in the daily workflow.
"""

from __future__ import annotations

import py_compile
import re
from pathlib import Path

ROOT = Path(".")
WORKFLOW_PATH = ROOT / ".github/workflows/daily.yml"
MODULE_TRACKER_PATH = ROOT / "module_signal_tracker.py"
QUALITY_PATH = ROOT / "data_quality_coherence_report.py"

REQUIRED_FILES = (
    ROOT / "exchange_market_data.py",
    ROOT / "exchange_persistent_storage.py",
    ROOT / "exchange_microstructure_report.py",
    ROOT / "exchange_signal_tracker.py",
    ROOT / "exchange_external_collector.py",
    ROOT / "exchange_fallback_guard.py",
    ROOT / "requirements-exchange.txt",
    ROOT / "requirements-exchange-collector.txt",
    ROOT / "exchange_intraday_workflow.yml",
)


def read(path: Path) -> str:
    if not path.exists():
        raise RuntimeError(f"File mancante: {path}")
    return path.read_text(encoding="utf-8")


def write_if_changed(path: Path, original: str, updated: str, backup_suffix: str) -> bool:
    if updated == original:
        print(f"{path}: nessuna modifica necessaria.")
        return False
    backup = path.with_name(path.name + backup_suffix)
    if not backup.exists():
        backup.write_text(original, encoding="utf-8", newline="\n")
    path.write_text(updated, encoding="utf-8", newline="\n")
    print(f"{path}: aggiornato.")
    return True


def patch_module_tracker() -> bool:
    original = read(MODULE_TRACKER_PATH)
    text = original
    # Remove both the old source marker and any report line that prints it.
    text = re.sub(
        r'^\s*lines\.append\(["\']# EXCHANGE_MICROSTRUCTURE_TRACKER_PATCH_V[^"\']+["\']\)\s*\n',
        "",
        text,
        flags=re.MULTILINE,
    )
    # The generic accuracy tracker should measure the candidate, not the still-locked Global score.
    exchange_block = re.compile(
        r'("key"\s*:\s*"exchange_microstructure".*?"score_col"\s*:\s*)"[^"]+"',
        flags=re.DOTALL,
    )
    text, count = exchange_block.subn(r'\1"exchange_candidate_score_component"', text, count=1)
    if count == 0 and '"key": "exchange_microstructure"' not in text:
        raise RuntimeError("Modulo exchange non trovato in module_signal_tracker.py")
    return write_if_changed(MODULE_TRACKER_PATH, original, text, ".bak_exchange_v2_1_1")


def patch_quality() -> bool:
    original = read(QUALITY_PATH)
    text = original

    # Add per-module tolerance to Exchange Microstructure.
    exchange_spec = re.compile(
        r'("Exchange Microstructure"\s*:\s*\{.*?"price_columns"\s*:\s*\([^\n]+\),)(\n\s*\})',
        flags=re.DOTALL,
    )
    if '"tolerance_pct": 0.20' not in text:
        text, count = exchange_spec.subn(r'\1\n        "tolerance_pct": 0.20,\2', text, count=1)
        if count == 0:
            raise RuntimeError("Specifica Exchange Microstructure non trovata in Data Quality")

    old = 'status = "OK" if not np.isnan(diff) and abs(diff) <= PRICE_TOLERANCE_PCT else "WARN"'
    if old in text:
        new = (
            'tolerance_pct = safe_float(spec.get("tolerance_pct", PRICE_TOLERANCE_PCT))\n'
            '                if np.isnan(tolerance_pct):\n'
            '                    tolerance_pct = PRICE_TOLERANCE_PCT\n'
            '                status = "OK" if not np.isnan(diff) and abs(diff) <= tolerance_pct else "WARN"'
        )
        text = text.replace(old, new, 1)

    # Store tolerance in the diagnostic payload when the richer checker is present.
    field_anchor = '"field": column,\n                    }'
    if field_anchor in text and '"tolerance_pct": tolerance_pct' not in text:
        text = text.replace(
            field_anchor,
            '"field": column,\n                        "tolerance_pct": tolerance_pct,\n                    }',
            1,
        )

    text = re.sub(
        r'f"\{len\(bad_prices\)\} campi prezzo non coincidono con lo snapshot entro \{PRICE_TOLERANCE_PCT:\.2f\}%\."',
        'f"{len(bad_prices)} campi prezzo superano la tolleranza specifica del modulo."',
        text,
        count=1,
    )

    # Diagnostics is a permanent, readable report and should be part of the integrity check.
    if 'REPORTS_DIR / "exchange_source_diagnostics.md"' not in text:
        anchor = 'REPORTS_DIR / "exchange_prediction_overlay.csv",\n'
        if anchor in text:
            text = text.replace(anchor, anchor + '        REPORTS_DIR / "exchange_source_diagnostics.md",\n', 1)
        else:
            raise RuntimeError("Elenco file exchange non trovato in Data Quality")

    return write_if_changed(QUALITY_PATH, original, text, ".bak_exchange_v2_1_1")


def split_step_blocks(text: str):
    lines = text.splitlines(keepends=True)
    starts: list[int] = []
    step_indent = None
    for index, line in enumerate(lines):
        match = re.match(r"^(\s*)-\s+name:\s*", line)
        if match:
            indent = len(match.group(1))
            if step_indent is None:
                step_indent = indent
            if indent == step_indent:
                starts.append(index)
    if not starts:
        raise RuntimeError("Nessun blocco '- name:' trovato nel workflow daily.yml")
    preamble = "".join(lines[: starts[0]])
    blocks = []
    for pos, start in enumerate(starts):
        end = starts[pos + 1] if pos + 1 < len(starts) else len(lines)
        blocks.append("".join(lines[start:end]))
    return preamble, blocks, step_indent or 6


def new_step(indent: int, name: str, command: str) -> str:
    pad = " " * indent
    child = " " * (indent + 2)
    return f"{pad}- name: {name}\n{child}run: {command}\n\n"


def patch_workflow() -> bool:
    original = read(WORKFLOW_PATH)
    preamble, blocks, indent = split_step_blocks(original)
    managed = (
        "requirements-exchange.txt",
        "exchange_market_data.py",
        "exchange_persistent_storage.py",
        "exchange_signal_tracker.py",
        "exchange_microstructure_report.py",
    )
    clean = [block for block in blocks if not any(fragment in block for fragment in managed)]
    global_index = next((i for i, block in enumerate(clean) if "python global_confluence_report.py" in block), None)
    if global_index is None:
        raise RuntimeError("Step global_confluence_report.py non trovato")

    additions = [
        new_step(indent, "Install exchange microstructure dependencies", "python -m pip install -r requirements-exchange.txt"),
        new_step(
            indent,
            "Restore persistent exchange state",
            'GITHUB_TOKEN="${{ github.token }}" EXCHANGE_STORAGE_RELEASE_TAG="exchange-data-v2-1" python exchange_persistent_storage.py restore',
        ),
        new_step(
            indent,
            "Audit persistent exchange state",
            'GITHUB_TOKEN="${{ github.token }}" EXCHANGE_STORAGE_RELEASE_TAG="exchange-data-v2-1" python exchange_persistent_storage.py audit',
        ),
        new_step(
            indent,
            "Archive completed exchange months",
            'GITHUB_TOKEN="${{ github.token }}" EXCHANGE_STORAGE_RELEASE_TAG="exchange-data-v2-1" python exchange_persistent_storage.py archive-completed-months',
        ),
        new_step(indent, "Save current exchange daily snapshot", "python exchange_microstructure_report.py"),
        new_step(indent, "Update exchange signal tracker", "python exchange_signal_tracker.py"),
        new_step(indent, "Refresh exchange report after tracker", "python exchange_microstructure_report.py"),
    ]
    clean[global_index:global_index] = additions
    updated = preamble + "".join(clean)
    if not updated.endswith("\n"):
        updated += "\n"

    order = [
        "python exchange_persistent_storage.py restore",
        "python exchange_persistent_storage.py audit",
        "python exchange_persistent_storage.py archive-completed-months",
        "python exchange_microstructure_report.py",
        "python exchange_signal_tracker.py",
        "python exchange_microstructure_report.py",
        "python global_confluence_report.py",
    ]
    cursor = -1
    for item in order:
        cursor = updated.find(item, cursor + 1)
        if cursor < 0:
            raise RuntimeError(f"Ordine workflow non valido, manca: {item}")
    if "python exchange_market_data.py" in updated:
        raise RuntimeError("Il daily non deve raccogliere dati intraday")
    return write_if_changed(WORKFLOW_PATH, original, updated, ".bak_exchange_v2_1_1")


def validate() -> None:
    missing = [str(path) for path in REQUIRED_FILES if not path.exists()]
    if missing:
        raise RuntimeError("File v2.1.1 mancanti: " + ", ".join(missing))
    for path in (
        ROOT / "exchange_market_data.py",
        ROOT / "exchange_persistent_storage.py",
        ROOT / "exchange_microstructure_report.py",
        ROOT / "exchange_signal_tracker.py",
        ROOT / "exchange_external_collector.py",
        ROOT / "exchange_fallback_guard.py",
        MODULE_TRACKER_PATH,
        QUALITY_PATH,
    ):
        py_compile.compile(str(path), doraise=True)

    tracker = read(MODULE_TRACKER_PATH)
    quality = read(QUALITY_PATH)
    workflow = read(WORKFLOW_PATH)
    checks = {
        "marker removed": "lines.append(\"# EXCHANGE_MICROSTRUCTURE_TRACKER_PATCH" not in tracker,
        "candidate tracked": '"score_col": "exchange_candidate_score_component"' in tracker,
        "exchange tolerance": '"tolerance_pct": 0.20' in quality,
        "diagnostics quality": 'exchange_source_diagnostics.md' in quality,
        "report before tracker": workflow.find("python exchange_microstructure_report.py") < workflow.find("python exchange_signal_tracker.py"),
        "tracker before refresh": workflow.find("python exchange_signal_tracker.py") < workflow.rfind("python exchange_microstructure_report.py"),
        "no daily collector": "python exchange_market_data.py" not in workflow,
    }
    failed = [name for name, ok in checks.items() if not ok]
    if failed:
        raise RuntimeError("Validazione v2.1.1 fallita: " + ", ".join(failed))
    print("Validazione Exchange Microstructure v2.1.1: OK")


def main() -> None:
    for path in REQUIRED_FILES:
        if not path.exists():
            raise RuntimeError(f"Carica prima il file richiesto nella radice: {path.name}")
    changed = [patch_module_tracker(), patch_quality(), patch_workflow()]
    validate()
    print("Patch v2.1.1 completata." if any(changed) else "Patch v2.1.1 già installata.")


if __name__ == "__main__":
    main()
