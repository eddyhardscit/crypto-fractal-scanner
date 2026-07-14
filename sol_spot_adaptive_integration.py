# -*- coding: utf-8 -*-
"""Autonomous SOL Spot Adaptive Range paper cycle.

Collects fresh KuCoin public data, runs the separate SOL spot paper portfolio,
and replaces its dedicated block inside reports/latest_report.md.
It does not import or modify run_paper_trading.py.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from kucoin_public_data import CACHE_PATH, collect_market_bundle
from paper_trading_config import load_config
from paper_trading_diagnostics import annotate_market_freshness
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
    bundle = collect_with_safe_fallback(config)
    bundle = annotate_market_freshness(bundle, config)

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
    updated = replace_block(current, report)
    LATEST_REPORT_PATH.write_text(updated, encoding="utf-8")

    if "Capitale iniziale separato: **€40.000,00**" not in updated:
        raise RuntimeError("Verifica capitale SOL €40.000 fallita.")
    if "Asset: **SOL spot**" not in updated:
        raise RuntimeError("Verifica asset SOL spot fallita.")
    if "Leva: **nessuna (1x)**" not in updated:
        raise RuntimeError("Verifica assenza leva fallita.")

    return result


if __name__ == "__main__":
    run()
