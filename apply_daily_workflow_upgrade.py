# -*- coding: utf-8 -*-
"""Aggiorna il workflow GitHub Actions conservando tutti gli step esistenti.

Uso dalla radice del repository:
    python apply_daily_workflow_upgrade.py

Aggiunge:
- modalità UTF-8 esplicita per tutti gli script Python;
- market_snapshot.py prima di scanner.py;
- data_quality_coherence_report.py subito prima del commit.
"""

from __future__ import annotations

import re
import shutil
from pathlib import Path


TARGET = Path(".github/workflows/daily.yml")


def patch_source(source: str) -> tuple[str, list[str]]:
    patched = source
    actions: list[str] = []

    if "PYTHONUTF8:" not in patched:
        match = re.search(r"(?m)^(\s{4})runs-on:\s*ubuntu-latest\s*$", patched)
        if not match:
            raise RuntimeError("Non trovo `runs-on: ubuntu-latest` nel job.")
        indent = match.group(1)
        block = (
            match.group(0)
            + "\n"
            + indent
            + "env:\n"
            + indent
            + '  PYTHONUTF8: "1"\n'
            + indent
            + '  PYTHONIOENCODING: "utf-8"'
        )
        patched = patched[:match.start()] + block + patched[match.end():]
        actions.append("UTF-8 globale")

    if "Run shared market snapshot" not in patched:
        scanner_step = re.search(r"(?m)^\s{6}- name:\s*Run scanner\s*$", patched)
        if not scanner_step:
            raise RuntimeError("Non trovo lo step `Run scanner`.")
        block = (
            "      - name: Run shared market snapshot\n"
            "        run: python market_snapshot.py\n\n"
        )
        patched = patched[:scanner_step.start()] + block + patched[scanner_step.start():]
        actions.append("snapshot condiviso")

    if "Run data quality coherence report" not in patched:
        commit_step = re.search(r"(?m)^\s{6}- name:\s*Commit reports\s*$", patched)
        if not commit_step:
            raise RuntimeError("Non trovo lo step `Commit reports`.")
        block = (
            "      - name: Run data quality coherence report\n"
            "        run: python data_quality_coherence_report.py\n\n"
        )
        patched = patched[:commit_step.start()] + block + patched[commit_step.start():]
        actions.append("controllo qualità finale")

    return patched, actions


def basic_validate(text: str) -> None:
    required = [
        'PYTHONUTF8: "1"',
        "run: python market_snapshot.py",
        "run: python scanner.py",
        "run: python data_quality_coherence_report.py",
        "- name: Commit reports",
    ]
    missing = [item for item in required if item not in text]
    if missing:
        raise RuntimeError("Workflow incompleto dopo la patch: " + ", ".join(missing))

    if text.index("run: python market_snapshot.py") > text.index("run: python scanner.py"):
        raise RuntimeError("market_snapshot.py deve essere eseguito prima di scanner.py")
    if text.index("run: python data_quality_coherence_report.py") > text.index("- name: Commit reports"):
        raise RuntimeError("Il controllo qualità deve essere eseguito prima del commit")


def main() -> None:
    if not TARGET.exists():
        raise SystemExit(f"File non trovato: {TARGET}")

    original = TARGET.read_text(encoding="utf-8")
    patched, actions = patch_source(original)
    basic_validate(patched)

    if patched == original:
        print("Workflow già aggiornato: nessuna modifica.")
        return

    backup = TARGET.with_suffix(TARGET.suffix + ".bak")
    if not backup.exists():
        backup.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(TARGET, backup)

    TARGET.write_text(patched, encoding="utf-8", newline="\n")
    print(f"Aggiornato {TARGET}")
    print(f"Backup: {backup}")
    print("Aggiunto: " + ", ".join(actions))


if __name__ == "__main__":
    main()
