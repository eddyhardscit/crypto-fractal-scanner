# -*- coding: utf-8 -*-
"""Install the automatic paper-trading layer without replacing the scanner."""

from __future__ import annotations

import py_compile
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent
WORKFLOW_PATH = Path(".github/workflows/daily.yml")
INTRADAY_DEST = Path(".github/workflows/paper_trading_intraday.yml")
COMPACT_PATH = Path("compact_latest_report.py")
GITIGNORE_PATH = Path(".gitignore")

REQUIRED_FILES = (
    "paper_trading_config.json",
    "paper_trading_config.py",
    "kucoin_public_data.py",
    "paper_signal_engine.py",
    "paper_trading_engine.py",
    "paper_trading_report.py",
    "paper_trading_notify.py",
    "paper_trading_runner.py",
    "paper_trading_storage.py",
    "paper_trading_selftest.py",
    "requirements-paper-trading.txt",
    "paper_trading_intraday_workflow.yml",
)
PYTHON_FILES = tuple(name for name in REQUIRED_FILES if name.endswith(".py")) + ("install_paper_trading_upgrade.py",)
COMPACT_MARKER = "# PAPER_TRADING_COMPACT_V1"


def read(path: Path) -> str:
    if not path.exists():
        raise RuntimeError(f"File richiesto non trovato: {path}")
    return path.read_text(encoding="utf-8")


def write_if_changed(path: Path, text: str) -> bool:
    original = path.read_text(encoding="utf-8") if path.exists() else ""
    if original == text:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")
    return True


def validate_files() -> None:
    missing = [name for name in REQUIRED_FILES if not Path(name).exists()]
    if missing:
        raise RuntimeError("File package mancanti: " + ", ".join(missing))
    for name in PYTHON_FILES:
        py_compile.compile(name, doraise=True)


def split_steps(text: str):
    lines = text.splitlines(keepends=True)
    starts: list[int] = []
    indent = None
    for index, line in enumerate(lines):
        match = re.match(r"^(\s*)-\s+name:\s*", line)
        if match:
            current = len(match.group(1))
            if indent is None:
                indent = current
            if current == indent:
                starts.append(index)
    if not starts:
        raise RuntimeError("Nessuno step '- name:' trovato nel workflow daily.yml")
    preamble = "".join(lines[: starts[0]])
    blocks = []
    for pos, start in enumerate(starts):
        end = starts[pos + 1] if pos + 1 < len(starts) else len(lines)
        blocks.append("".join(lines[start:end]))
    return preamble, blocks, indent or 6


def step(indent: int, name: str, command: str, env: list[str] | None = None) -> str:
    pad = " " * indent
    child = " " * (indent + 2)
    output = [f"{pad}- name: {name}\n"]
    if env:
        output.append(f"{child}env:\n")
        for line in env:
            output.append(f"{child}  {line}\n")
    output.append(f"{child}run: {command}\n\n")
    return "".join(output)


def patch_daily_workflow() -> bool:
    original = read(WORKFLOW_PATH)
    preamble, blocks, indent = split_steps(original)
    managed = (
        "requirements-paper-trading.txt",
        "paper_trading_storage.py restore",
        "paper_trading_storage.py audit",
        "paper_trading_report.py",
    )
    blocks = [block for block in blocks if not any(fragment in block for fragment in managed)]

    insert_at = next((i for i, block in enumerate(blocks) if "python compact_latest_report.py" in block), None)
    if insert_at is None:
        insert_at = next((i for i, block in enumerate(blocks) if "Commit reports" in block or "git add reports" in block), len(blocks))

    env = [
        'GITHUB_TOKEN: ${{ github.token }}',
        "PAPER_TRADING_RELEASE_TAG: paper-trading-v1",
        "PAPER_TRADING_CONFIG: paper_trading_config.json",
    ]
    additions = [
        step(indent, "Install paper-trading report dependencies", "python -m pip install -r requirements-paper-trading.txt"),
        step(indent, "Restore paper-trading state for daily report", "python paper_trading_storage.py restore", env),
        step(indent, "Audit paper-trading state", "python paper_trading_storage.py audit", env),
        step(indent, "Build paper-trading daily report", "python paper_trading_report.py"),
    ]
    blocks[insert_at:insert_at] = additions
    updated = preamble + "".join(blocks)
    if not updated.endswith("\n"):
        updated += "\n"

    required_order = ["paper_trading_storage.py restore", "paper_trading_report.py"]
    positions = [updated.find(item) for item in required_order]
    if min(positions) < 0 or positions != sorted(positions):
        raise RuntimeError(f"Ordine paper trading nel daily non valido: {positions}")
    compact_pos = updated.find("python compact_latest_report.py")
    if compact_pos >= 0 and positions[-1] > compact_pos:
        raise RuntimeError("Il report paper trading deve precedere compact_latest_report.py")
    return write_if_changed(WORKFLOW_PATH, updated)


def patch_compact() -> bool:
    original = read(COMPACT_PATH)
    if COMPACT_MARKER in original and "PAPER_TRADING_START" in original:
        return False
    anchor = '''    (
        "module_accuracy",
        "<!-- MODULE_ACCURACY_START -->",
'''
    insert = '''    (
        "paper_trading",
        "<!-- PAPER_TRADING_START -->",
        "<!-- PAPER_TRADING_END -->",
        "🧪 Paper trading automatico KuCoin",
        True,
    ),
'''
    if anchor not in original:
        raise RuntimeError("Punto di inserimento paper trading non trovato in compact_latest_report.py")
    updated = original.replace(anchor, insert + anchor, 1)
    marker_anchor = 'SECTION_END = "<!-- COMPACT_SECTION_END:{key} -->"\n'
    if marker_anchor in updated:
        updated = updated.replace(marker_anchor, marker_anchor + COMPACT_MARKER + "\n", 1)
    else:
        updated = COMPACT_MARKER + "\n" + updated
    return write_if_changed(COMPACT_PATH, updated)


def install_intraday_workflow() -> bool:
    source = Path("paper_trading_intraday_workflow.yml")
    content = source.read_text(encoding="utf-8")
    return write_if_changed(INTRADAY_DEST, content)


def patch_gitignore() -> bool:
    original = GITIGNORE_PATH.read_text(encoding="utf-8") if GITIGNORE_PATH.exists() else ""
    block = '''
# Automatic paper-trading persistent state (stored in GitHub Release asset)
reports/paper_trading_state.json
reports/paper_trading_trade_log.csv
reports/paper_trading_signal_log.csv
reports/paper_trading_equity.csv
reports/paper_trading_open_positions.csv
reports/paper_trading_shadow_metrics.csv
reports/paper_trading_config_snapshot.json
reports/paper_trading_market_cache.json
reports/paper_trading_storage_status.json
'''
    if "reports/paper_trading_state.json" in original:
        return False
    updated = original.rstrip() + "\n" + block
    return write_if_changed(GITIGNORE_PATH, updated)


def validate_installation() -> None:
    daily = read(WORKFLOW_PATH)
    compact = read(COMPACT_PATH)
    intraday = read(INTRADAY_DEST)
    checks = {
        "daily restore": "paper_trading_storage.py restore" in daily,
        "daily report": "paper_trading_report.py" in daily,
        "compact section": "PAPER_TRADING_START" in compact,
        "intraday restore": "paper_trading_storage.py restore" in intraday,
        "intraday runner": "paper_trading_runner.py" in intraday,
        "intraday upload": "paper_trading_storage.py upload" in intraday,
        "intraday concurrency": "paper-trading-persistent-state" in intraday,
    }
    failed = [name for name, ok in checks.items() if not ok]
    if failed:
        raise RuntimeError("Validazione installazione fallita: " + ", ".join(failed))


def main() -> None:
    validate_files()
    results = {
        "daily": patch_daily_workflow(),
        "compact": patch_compact(),
        "intraday": install_intraday_workflow(),
        "gitignore": patch_gitignore(),
    }
    validate_installation()
    print("Paper Trading Upgrade v1 installato:", results)


if __name__ == "__main__":
    main()
