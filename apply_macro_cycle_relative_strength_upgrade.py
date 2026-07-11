# -*- coding: utf-8 -*-
"""Install BTC macro-cycle and ALT/BTC relative-strength modules.

The installer is conservative and idempotent:
* it patches compact_latest_report.py with two collapsible sections;
* it prepares, but does not overwrite, .github/workflows/daily.yml;
* it compiles the new modules and validates marker/order integrity;
* it never changes Global Confluence weights.

Workflow files are delivered as an artifact because GitHub-hosted workflow
tokens may refuse to create or update another workflow file.
"""

from __future__ import annotations

import argparse
import py_compile
import re
import shutil
from pathlib import Path


ROOT = Path(".")
COMPACT_PATH = ROOT / "compact_latest_report.py"
DAILY_PATH = ROOT / ".github" / "workflows" / "daily.yml"
PREPARED_DIR = ROOT / "prepared_macro_cycle_workflow"
PREPARED_DAILY = PREPARED_DIR / "daily.yml"
STATUS_PATH = ROOT / "reports" / "macro_cycle_relative_strength_installation_status.md"

NEW_FILES = (
    ROOT / "relative_strength_btc_report.py",
    ROOT / "btc_macro_cycle_report.py",
    ROOT / "macro_cycle_relative_strength_selftest.py",
)

COMPACT_MARKER = "# MACRO_CYCLE_RELATIVE_STRENGTH_COMPACT_PATCH_V1"


def read(path: Path) -> str:
    if not path.exists():
        raise RuntimeError(f"File mancante: {path}")
    return path.read_text(encoding="utf-8")


def backup(path: Path, suffix: str) -> None:
    target = path.with_name(path.name + suffix)
    if not target.exists():
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, target)


def write_if_changed(path: Path, original: str, updated: str, suffix: str) -> bool:
    if original == updated:
        print(f"{path}: già aggiornato.")
        return False
    backup(path, suffix)
    path.write_text(updated, encoding="utf-8", newline="\n")
    print(f"{path}: aggiornato.")
    return True


def patch_compact() -> bool:
    original = read(COMPACT_PATH)
    if COMPACT_MARKER in original:
        print("Compact report: patch già presente.")
        return False

    insertion = '''    (
        "btc_macro_cycle",
        "<!-- BTC_MACRO_CYCLE_START -->",
        "<!-- BTC_MACRO_CYCLE_END -->",
        "🌀 Bitcoin Macro Cycle — Power Law e Spiral",
        False,
    ),
    (
        "relative_strength_btc",
        "<!-- RELATIVE_STRENGTH_BTC_START -->",
        "<!-- RELATIVE_STRENGTH_BTC_END -->",
        "₿ Forza relativa SOL/BTC e DOGE/BTC",
        False,
    ),
'''

    # Prefer placement immediately after Global Confluence. Fallback: before
    # the existing BTC/SOL fractal section.
    global_tuple = re.compile(
        r'(\s*\(\s*\n\s*"global_confluence",\s*\n\s*"<!-- GLOBAL_CONFLUENCE_START -->",.*?\n\s*\),\s*\n)',
        flags=re.DOTALL,
    )
    match = global_tuple.search(original)
    if match:
        updated = original[: match.end()] + insertion + original[match.end() :]
    else:
        anchor = '    (\n        "btc_sol_fractal",\n'
        if anchor not in original:
            raise RuntimeError("Punto patch compact non trovato.")
        updated = original.replace(anchor, insertion + anchor, 1)

    marker_anchor = 'SECTION_END = "<!-- COMPACT_SECTION_END:{key} -->"\n'
    if marker_anchor in updated:
        updated = updated.replace(marker_anchor, marker_anchor + COMPACT_MARKER + "\n", 1)
    else:
        updated = COMPACT_MARKER + "\n" + updated

    return write_if_changed(COMPACT_PATH, original, updated, ".bak_macro_cycle")


def split_step_blocks(text: str):
    lines = text.splitlines(keepends=True)
    starts = []
    step_indent = None
    for index, line in enumerate(lines):
        match = re.match(r"^(\s*)-\s+name:\s*", line)
        if not match:
            continue
        indent = len(match.group(1))
        if step_indent is None:
            step_indent = indent
        if indent == step_indent:
            starts.append(index)
    if not starts:
        raise RuntimeError("Nessun blocco '- name:' trovato in daily.yml.")
    preamble = "".join(lines[: starts[0]])
    blocks = []
    for position, start in enumerate(starts):
        end = starts[position + 1] if position + 1 < len(starts) else len(lines)
        blocks.append("".join(lines[start:end]))
    return preamble, blocks, step_indent or 6


def new_step(indent: int, name: str, command: str) -> str:
    pad = " " * indent
    child = " " * (indent + 2)
    return f"{pad}- name: {name}\n{child}run: {command}\n\n"


def prepare_daily_workflow() -> bool:
    original = read(DAILY_PATH)
    preamble, blocks, indent = split_step_blocks(original)
    managed = (
        "relative_strength_btc_report.py",
        "btc_macro_cycle_report.py",
    )
    clean = [block for block in blocks if not any(token in block for token in managed)]

    global_index = next((index for index, block in enumerate(clean) if "python global_confluence_report.py" in block), None)
    if global_index is None:
        raise RuntimeError("Step global_confluence_report.py non trovato nel daily workflow.")

    additions = [
        new_step(indent, "Build ALT/BTC relative-strength report", "python relative_strength_btc_report.py"),
        new_step(indent, "Build BTC macro cycle Power Law and Spiral", "python btc_macro_cycle_report.py"),
    ]
    clean[global_index:global_index] = additions
    updated = preamble + "".join(clean)
    if not updated.endswith("\n"):
        updated += "\n"

    order = [
        "python relative_strength_btc_report.py",
        "python btc_macro_cycle_report.py",
        "python global_confluence_report.py",
    ]
    positions = [updated.find(token) for token in order]
    if min(positions) < 0 or positions != sorted(positions):
        raise RuntimeError(f"Ordine daily non valido: {dict(zip(order, positions))}")

    PREPARED_DIR.mkdir(parents=True, exist_ok=True)
    old = PREPARED_DAILY.read_text(encoding="utf-8") if PREPARED_DAILY.exists() else ""
    PREPARED_DAILY.write_text(updated, encoding="utf-8", newline="\n")
    print(f"Workflow preparato: {PREPARED_DAILY}")
    return old != updated


def compile_files() -> None:
    missing = [str(path) for path in NEW_FILES if not path.exists()]
    if missing:
        raise RuntimeError("Nuovi file mancanti: " + ", ".join(missing))
    for path in (*NEW_FILES, COMPACT_PATH):
        py_compile.compile(str(path), doraise=True)


def validate() -> None:
    compact = read(COMPACT_PATH)
    daily = read(PREPARED_DAILY)
    checks = {
        "Compact macro marker": "BTC_MACRO_CYCLE_START" in compact,
        "Compact relative marker": "RELATIVE_STRENGTH_BTC_START" in compact,
        "Daily relative": "python relative_strength_btc_report.py" in daily,
        "Daily macro": "python btc_macro_cycle_report.py" in daily,
        "Global unchanged by weight": "global_confluence_report.py" in daily,
    }
    failed = [name for name, ok in checks.items() if not ok]
    if failed:
        raise RuntimeError("Validazione fallita: " + ", ".join(failed))


def write_status(compact_changed: bool, workflow_changed: bool) -> None:
    STATUS_PATH.parent.mkdir(parents=True, exist_ok=True)
    text = f"""# Stato installazione Macro Cycle + Relative Strength

- Nuovi moduli Python: **OK**
- Compact report: **{'AGGIORNATO' if compact_changed else 'GIÀ PRESENTE'}**
- Daily workflow preparato: **{'AGGIORNATO' if workflow_changed else 'GIÀ ALLINEATO'}**
- Peso Global Power Law/Spiral: **0**
- Peso Global SOL/BTC e DOGE/BTC: **0**
- File da sostituire manualmente: `.github/workflows/daily.yml`
- Artifact pronto: `prepared_macro_cycle_workflow/daily.yml`

I nuovi moduli non modificano i pesi correnti del Global Confluence e non toccano lo storico exchange V2.1.3.
"""
    STATUS_PATH.write_text(text, encoding="utf-8", newline="\n")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--apply-workflow",
        action="store_true",
        help="Apply the prepared daily.yml locally. Do not use from the one-time GitHub workflow.",
    )
    args = parser.parse_args()

    compile_files()
    compact_changed = patch_compact()
    workflow_changed = prepare_daily_workflow()
    compile_files()
    validate()
    if args.apply_workflow:
        original = read(DAILY_PATH)
        prepared = read(PREPARED_DAILY)
        write_if_changed(DAILY_PATH, original, prepared, ".bak_macro_cycle")
    write_status(compact_changed, workflow_changed)
    print("Upgrade Macro Cycle + Relative Strength completato.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
