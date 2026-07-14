# -*- coding: utf-8 -*-
"""Autonomous SOL Spot Adaptive Range paper cycle.

Collects KuCoin public data, runs the separate SOL spot paper portfolio,
writes its standalone report explicitly, and embeds it in latest_report.md.
No dependency on run_paper_trading.py.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from kucoin_public_data import CACHE_PATH, collect_market_bundle
from paper_trading_config import load_config
from paper_trading_diagnostics import annotate_market_freshness
from sol_spot_adaptive import run_sol_spot_adaptive_cycle

REPORTS_DIR = Path("reports")
SOL_REPORT_PATH = REPORTS_DIR / "sol_spot_adaptive_report.md"
LATEST_REPORT_PATH = REPORTS_DIR / "latest_report.md"
START_MARKER = "<!-- SOL_SPOT_ADAPTIVE_START -->"
END_MARKER = "<!-- SOL_SPOT_ADAPTIVE_END -->"


def replace_block(text: str, block: str) -> str:
    wrapped = f"{START_MARKER}\n{block.strip()}\n{END_MARKER}"
    start = text.find(START_MARKER)
    end = text.find(END_MARKER)

    if start >= 0 and end >= start:
        end += len(END_MARKER)
        before = text[:start].rstrip()
        after = text[end:].lstrip()
        return before + "\n\n" + wrapped + ("\n\n" + after if after else "\n")

    return text.rstrip() + "\n\n" + wrapped + "\n"


def collect_with_safe_fallback(config: dict[str, Any]) -> dict[str, Any]:
    try:
        return collect_market_bundle(config)
    except Exception as exc:
        if not CACHE_PATH.exists():
            raise
        bundle = json.loads(CACHE_PATH.read_text(encoding="utf-8"))
        bundle.setdefault("failures", []).append(
            f"SOL autonomous live collection failed; cache used: {exc}"
        )
        bundle["source"] = (
            str(bundle.get("source", "CACHE")) + ":STALE_FALLBACK"
        )
        return bundle


def run() -> dict[str, Any]:
    config = load_config()
    bundle = annotate_market_freshness(
        collect_with_safe_fallback(config),
        config,
    )

    result = run_sol_spot_adaptive_cycle(bundle)
    report = str(result.get("report_markdown", "")).strip()
    if not report:
        raise RuntimeError("Il modulo SOL non ha prodotto il report Markdown.")

    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    # Scrittura esplicita: non dipende dal side effect del modulo.
    SOL_REPORT_PATH.write_text(report + "\n", encoding="utf-8")

    current = (
        LATEST_REPORT_PATH.read_text(encoding="utf-8")
        if LATEST_REPORT_PATH.exists()
        else "# Crypto scanner report\n"
    )
    updated = replace_block(current, report)
    LATEST_REPORT_PATH.write_text(updated, encoding="utf-8")

    required = (
        "Capitale iniziale separato: **€40.000,00**",
        "Asset: **SOL spot**",
        "Leva: **nessuna (1x)**",
    )
    for text in required:
        if text not in updated:
            raise RuntimeError(f"Verifica contenuto fallita: {text}")

    if not SOL_REPORT_PATH.is_file():
        raise RuntimeError(f"Report separato non creato: {SOL_REPORT_PATH}")
    if not LATEST_REPORT_PATH.is_file():
        raise RuntimeError(f"Latest report non creato: {LATEST_REPORT_PATH}")

    print(f"SOL report scritto: {SOL_REPORT_PATH.resolve()}")
    print(f"Latest report aggiornato: {LATEST_REPORT_PATH.resolve()}")
    print(
        "SOL state: "
        f"equity={result.get('state', {}).get('equity_eur', 'n/a')} "
        f"action={result.get('state', {}).get('last_action', 'n/a')}"
    )
    return result


if __name__ == "__main__":
    run()
