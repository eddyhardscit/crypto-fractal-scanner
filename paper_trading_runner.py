# -*- coding: utf-8 -*-
"""One complete automatic paper-trading cycle."""

from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from pathlib import Path

from kucoin_public_data import CACHE_PATH, collect_market_bundle
from paper_signal_engine import generate_signals
from paper_trading_config import load_config
from paper_trading_engine import load_state, run_execution_cycle
from paper_trading_notify import notify
from paper_trading_report import render_report, REPORT_PATH, LATEST_REPORT_PATH, replace_block


def _load_cache() -> dict:
    return json.loads(CACHE_PATH.read_text(encoding="utf-8"))


def collect_with_fallback(config: dict) -> dict:
    try:
        bundle = collect_market_bundle(config)
    except Exception as exc:
        if not CACHE_PATH.exists():
            raise
        bundle = _load_cache()
        bundle.setdefault("failures", []).append(f"Live collection failed, cache used: {exc}")
        bundle["source"] = str(bundle.get("source", "CACHE")) + ":STALE_FALLBACK"
    CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
    CACHE_PATH.write_text(json.dumps(bundle, ensure_ascii=False), encoding="utf-8")
    return bundle


def main() -> None:
    config = load_config()
    bundle = collect_with_fallback(config)
    signals = generate_signals(bundle, config)
    state = load_state(config)
    summary = run_execution_cycle(state, signals, bundle, config)

    report = render_report(state, config)
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(report, encoding="utf-8")
    if LATEST_REPORT_PATH.exists():
        latest = LATEST_REPORT_PATH.read_text(encoding="utf-8")
        LATEST_REPORT_PATH.write_text(replace_block(latest, report), encoding="utf-8")

    notified = False
    try:
        notified = notify(summary)
    except Exception as exc:
        print(f"Telegram non inviato: {exc}")

    print(
        json.dumps(
            {
                "generated_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                "market_source": bundle.get("source"),
                "assets": len(bundle.get("assets", {})),
                "signals": len(signals),
                "opened": len(summary.get("opened", [])),
                "closed": len(summary.get("closed", [])),
                "telegram": notified,
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
