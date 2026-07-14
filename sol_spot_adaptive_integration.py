# -*- coding: utf-8 -*-
"""Run the separate SOL spot paper portfolio and embed it in latest_report.md."""
from __future__ import annotations

from pathlib import Path
from typing import Any

from kucoin_public_data import collect_market_bundle
from paper_trading_config import load_config
from paper_trading_diagnostics import annotate_market_freshness
from run_paper_trading import collect_with_fallback
from sol_spot_adaptive import run_sol_spot_adaptive_cycle

LATEST_REPORT_PATH = Path("reports/latest_report.md")
START_MARKER = "<!-- SOL_SPOT_ADAPTIVE_START -->"
END_MARKER = "<!-- SOL_SPOT_ADAPTIVE_END -->"


def replace_block(text: str, block: str) -> str:
    wrapped = f"{START_MARKER}\n{block.strip()}\n{END_MARKER}"
    start = text.find(START_MARKER)
    end = text.find(END_MARKER)
    if start >= 0 and end >= start:
        end += len(END_MARKER)
        return text[:start].rstrip() + "\n\n" + wrapped + "\n" + text[end:].lstrip()
    return text.rstrip() + "\n\n" + wrapped + "\n"


def run() -> dict[str, Any]:
    config = load_config()
    bundle = annotate_market_freshness(
        collect_with_fallback(config),
        config,
    )
    result = run_sol_spot_adaptive_cycle(bundle)
    report = str(result.get("report_markdown", "")).strip()
    if not report:
        raise RuntimeError("Il modulo SOL non ha prodotto il report Markdown.")

    LATEST_REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    current = (
        LATEST_REPORT_PATH.read_text(encoding="utf-8")
        if LATEST_REPORT_PATH.exists()
        else "# Crypto scanner report\n"
    )
    LATEST_REPORT_PATH.write_text(
        replace_block(current, report),
        encoding="utf-8",
    )
    return result


if __name__ == "__main__":
    run()
