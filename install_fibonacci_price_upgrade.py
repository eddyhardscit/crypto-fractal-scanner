# -*- coding: utf-8 -*-
"""Install the Fibonacci / shared-price workflow upgrade once.

The full Python replacements are uploaded separately. This script only performs
one task that cannot be safely replaced without knowing the user's current
workflow: it updates ``.github/workflows/daily.yml`` while preserving every
existing custom step.
"""

from __future__ import annotations

import py_compile
import re
from pathlib import Path


WORKFLOW_PATH = Path(".github/workflows/daily.yml")

REQUIRED_ROOT_FILES = (
    "shared_market_snapshot.py",
    "price_coherence_sync.py",
    "technical_structure_report.py",
    "classic_technical_visual_report.py",
    "rsi_top_cycle_report.py",
    "btc_2022_vs_sol_2026_report.py",
    "fractal_path_tracker.py",
    "data_quality_coherence_report.py",
)


def compile_files() -> None:
    missing = [name for name in REQUIRED_ROOT_FILES if not Path(name).exists()]
    if missing:
        raise RuntimeError(
            "File mancanti nella radice del repository: " + ", ".join(missing)
        )
    for name in REQUIRED_ROOT_FILES:
        py_compile.compile(name, doraise=True)


def split_step_blocks(text: str):
    lines = text.splitlines(keepends=True)
    starts = []
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
        raise RuntimeError("Nessun blocco '- name:' trovato nel workflow daily.yml.")

    preamble = "".join(lines[: starts[0]])
    blocks = []
    for pos, start in enumerate(starts):
        end = starts[pos + 1] if pos + 1 < len(starts) else len(lines)
        blocks.append("".join(lines[start:end]))
    return preamble, blocks, step_indent or 6


def block_for_script(blocks: list[str], script: str) -> str | None:
    for block in blocks:
        if re.search(rf"\brun:\s*python\s+{re.escape(script)}\b", block):
            return block
    return None


def new_step(indent: int, name: str, command: str) -> str:
    pad = " " * indent
    child = " " * (indent + 2)
    return f"{pad}- name: {name}\n{child}run: {command}\n\n"


def insert_before(blocks: list[str], predicate, additions: list[str]) -> list[str]:
    for index, block in enumerate(blocks):
        if predicate(block):
            return blocks[:index] + additions + blocks[index:]
    return blocks + additions


def patch_workflow() -> bool:
    if not WORKFLOW_PATH.exists():
        raise RuntimeError(f"Workflow non trovato: {WORKFLOW_PATH}")

    original = WORKFLOW_PATH.read_text(encoding="utf-8")
    preamble, blocks, indent = split_step_blocks(original)

    technical = block_for_script(blocks, "technical_structure_report.py") or new_step(
        indent, "Run technical structure report", "python technical_structure_report.py"
    )
    visual = block_for_script(blocks, "classic_technical_visual_report.py") or new_step(
        indent, "Run classic technical visual report", "python classic_technical_visual_report.py"
    )
    data_quality = block_for_script(blocks, "data_quality_coherence_report.py") or new_step(
        indent, "Run data quality coherence report", "python data_quality_coherence_report.py"
    )
    sync = new_step(
        indent,
        "Synchronize shared market prices",
        "python price_coherence_sync.py",
    )

    # Remove old copies; reinsert in dependency-safe positions.
    managed_scripts = {
        "technical_structure_report.py",
        "classic_technical_visual_report.py",
        "price_coherence_sync.py",
        "data_quality_coherence_report.py",
    }
    clean_blocks = []
    for block in blocks:
        if any(
            re.search(rf"\brun:\s*python\s+{re.escape(script)}\b", block)
            for script in managed_scripts
        ):
            continue
        clean_blocks.append(block)

    # Technical is authoritative; Visual must run immediately after it. The
    # price synchroniser then freezes every current-price output before Global.
    global_index = next(
        (
            index
            for index, block in enumerate(clean_blocks)
            if re.search(r"\brun:\s*python\s+global_confluence_report\.py\b", block)
        ),
        None,
    )
    if global_index is None:
        raise RuntimeError(
            "Step global_confluence_report.py non trovato: non posso scegliere "
            "in sicurezza il punto di sincronizzazione."
        )

    clean_blocks[global_index:global_index] = [technical, visual, sync]

    # Data Quality must see the final reports and must run before reports are
    # committed/sent. Prefer the Commit reports step; otherwise before email.
    commit_index = next(
        (
            index
            for index, block in enumerate(clean_blocks)
            if "git add reports/" in block or re.search(r"name:\s*Commit reports", block, re.I)
        ),
        None,
    )
    if commit_index is None:
        commit_index = next(
            (
                index
                for index, block in enumerate(clean_blocks)
                if "send_email.py" in block or re.search(r"name:\s*Send email", block, re.I)
            ),
            len(clean_blocks),
        )
    clean_blocks[commit_index:commit_index] = [data_quality]

    updated = preamble + "".join(clean_blocks)
    if not updated.endswith("\n"):
        updated += "\n"

    # Structural validation.
    positions = {
        script: updated.find(f"python {script}")
        for script in (
            "technical_structure_report.py",
            "classic_technical_visual_report.py",
            "price_coherence_sync.py",
            "global_confluence_report.py",
            "data_quality_coherence_report.py",
        )
    }
    if any(value < 0 for value in positions.values()):
        raise RuntimeError(f"Validazione workflow fallita: {positions}")
    if not (
        positions["technical_structure_report.py"]
        < positions["classic_technical_visual_report.py"]
        < positions["price_coherence_sync.py"]
        < positions["global_confluence_report.py"]
    ):
        raise RuntimeError(f"Ordine moduli non valido: {positions}")

    if updated == original:
        print("daily.yml: upgrade già installato.")
        return False

    backup = WORKFLOW_PATH.with_suffix(".yml.bak_fibonacci_price")
    backup.parent.mkdir(parents=True, exist_ok=True)
    backup.write_text(original, encoding="utf-8", newline="\n")
    WORKFLOW_PATH.write_text(updated, encoding="utf-8", newline="\n")
    print(f"Workflow aggiornato: {WORKFLOW_PATH}")
    print(f"Backup creato: {backup}")
    return True


def validate_global_reader() -> None:
    path = Path("global_confluence_report.py")
    if not path.exists():
        raise RuntimeError("global_confluence_report.py mancante.")
    text = path.read_text(encoding="utf-8")
    if "technical_structure_metrics.csv" not in text:
        raise RuntimeError(
            "Il Global Confluence non sembra ancora leggere technical_structure_metrics.csv. "
            "Mantieni la versione corretta installata nell'upgrade precedente."
        )


def main() -> None:
    compile_files()
    validate_global_reader()
    changed = patch_workflow()
    print("Compilazione file: OK")
    print("Global structured reader: OK")
    print("Installazione completata." if changed else "Installazione già presente.")


if __name__ == "__main__":
    main()
