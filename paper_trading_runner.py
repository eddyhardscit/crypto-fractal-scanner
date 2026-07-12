# -*- coding: utf-8 -*-
"""One complete automatic paper-trading cycle."""

from __future__ import annotations

import json
import math
import os
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

from kucoin_public_data import CACHE_PATH, collect_market_bundle
from paper_signal_engine import generate_signals
from paper_trading_config import load_config
from paper_trading_engine import (
    current_prices,
    load_state,
    portfolio_equity,
    risk_gate,
    run_execution_cycle,
    save_state,
)
from paper_trading_live_publish import publish_markdown
from paper_trading_notify import notify
from paper_trading_report import LATEST_REPORT_PATH, REPORT_PATH, render_report, replace_block
from telegram_scanner_notify import send_if_changed as send_scanner_if_changed

LIVE_REPORT_PATH = Path("reports/paper_trading_live.md")
CYCLE_SUMMARY_PATH = Path("reports/paper_trading_cycle_summary.json")


def _parse_iso(value: Any) -> datetime | None:
    if not value:
        return None
    try:
        parsed = datetime.fromisoformat(str(value).replace("Z", "+00:00"))
        if parsed.tzinfo is None:
            parsed = parsed.replace(tzinfo=timezone.utc)
        return parsed.astimezone(timezone.utc)
    except Exception:
        return None


def _position_snapshot(state: dict[str, Any], bundle: dict[str, Any]) -> dict[str, dict[str, Any]]:
    prices = current_prices(bundle)
    snapshot: dict[str, dict[str, Any]] = {}
    for portfolio_name, portfolio in state.get("portfolios", {}).items():
        for position in portfolio.get("open_positions", []):
            key = f"{portfolio_name}:{position.get('trade_id', '')}"
            snapshot[key] = {
                "portfolio": portfolio_name,
                "trade_id": position.get("trade_id", ""),
                "asset": position.get("asset", ""),
                "side": position.get("side", ""),
                "stop_price": float(position.get("stop_price", 0.0)),
                "mark_price": float(prices.get(position.get("asset", ""), position.get("entry_price", 0.0))),
            }
    return snapshot


def _trailing_updates(
    before: dict[str, dict[str, Any]],
    after: dict[str, dict[str, Any]],
) -> list[dict[str, Any]]:
    updates: list[dict[str, Any]] = []
    for key in sorted(set(before).intersection(after)):
        old = float(before[key].get("stop_price", 0.0))
        new = float(after[key].get("stop_price", 0.0))
        tolerance = max(1e-12, abs(old) * 1e-10)
        if math.isclose(old, new, rel_tol=0.0, abs_tol=tolerance):
            continue
        updates.append({**after[key], "old_stop_price": old, "new_stop_price": new})
    return updates


def _risk_changes(
    state: dict[str, Any],
    bundle: dict[str, Any],
    config: dict[str, Any],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    prices = current_prices(bundle)
    rate = float(bundle.get("eur_usdt_rate", config.get("eur_usdt_fallback_rate", 1.0)))
    notifications = state.setdefault("notifications", {})
    previous_status = dict(notifications.get("risk_status", {}))
    current_status: dict[str, str] = {}
    alerts: list[dict[str, Any]] = []
    recoveries: list[dict[str, Any]] = []

    for name, portfolio in state.get("portfolios", {}).items():
        equity, _ = portfolio_equity(portfolio, prices, rate)
        allowed, reason = risk_gate(portfolio, equity, config)
        status = "OK" if allowed else reason
        previous = str(previous_status.get(name, "OK"))
        current_status[name] = status
        if status == previous:
            continue
        payload = {"portfolio": name, "equity_eur": equity, "reason": status}
        if status == "OK":
            recoveries.append(payload)
        else:
            alerts.append(payload)

    notifications["risk_status"] = current_status
    return alerts, recoveries


def _publication_due(
    state: dict[str, Any],
    config: dict[str, Any],
    summary: dict[str, Any],
    current: datetime,
) -> tuple[bool, list[str]]:
    event_activity = bool(
        summary.get("opened")
        or summary.get("closed")
        or summary.get("trailing_updates")
        or summary.get("risk_alerts")
        or summary.get("risk_recoveries")
    )
    manual = os.getenv("GITHUB_EVENT_NAME", "").strip() == "workflow_dispatch"
    interval = float(config.get("notifications", {}).get("live_report_interval_hours", 4.0))
    last = _parse_iso(state.get("notifications", {}).get("live_report_last_publish_utc"))
    periodic = interval > 0 and (last is None or current - last >= timedelta(hours=interval))
    reasons = [
        name
        for name, enabled in (
            ("market_event", event_activity),
            ("periodic_snapshot", periodic),
            ("manual_run", manual),
        )
        if enabled
    ]
    return bool(reasons), reasons


def _load_cache() -> dict[str, Any]:
    return json.loads(CACHE_PATH.read_text(encoding="utf-8"))


def collect_with_fallback(config: dict[str, Any]) -> dict[str, Any]:
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

    before = _position_snapshot(state, bundle)
    summary = run_execution_cycle(state, signals, bundle, config)
    after = _position_snapshot(state, bundle)
    summary["trailing_updates"] = _trailing_updates(before, after)
    risk_alerts, risk_recoveries = _risk_changes(state, bundle, config)
    summary["risk_alerts"] = risk_alerts
    summary["risk_recoveries"] = risk_recoveries

    current = datetime.now(timezone.utc)
    report = render_report(state, config)
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(report, encoding="utf-8")
    LIVE_REPORT_PATH.write_text(report, encoding="utf-8")
    if LATEST_REPORT_PATH.exists():
        latest = LATEST_REPORT_PATH.read_text(encoding="utf-8")
        LATEST_REPORT_PATH.write_text(replace_block(latest, report), encoding="utf-8")

    publish_due, publish_reasons = _publication_due(state, config, summary, current)
    publish_result: dict[str, Any] = {
        "configured": False,
        "published": False,
        "reasons": publish_reasons,
    }
    if publish_due:
        try:
            live_branch = str(config.get("notifications", {}).get("live_report_branch", "paper-trading-live"))
            publish_result = publish_markdown(
                "reports/paper_trading_live.md",
                report,
                "Update live paper trading dashboard",
                branch=live_branch,
            )
            publish_result["reasons"] = publish_reasons
            if publish_result.get("published") or publish_result.get("unchanged"):
                state.setdefault("notifications", {})["live_report_last_publish_utc"] = current.isoformat(timespec="seconds")
        except Exception as exc:
            publish_result = {"configured": True, "published": False, "error": str(exc), "reasons": publish_reasons}
            print(f"Dashboard live non pubblicata: {exc}")

    try:
        telegram_result = notify(summary, state, config, current)
    except Exception as exc:
        telegram_result = {"configured": True, "sent": False, "error": str(exc)}
        print(f"Telegram paper trading non inviato: {exc}")

    try:
        scanner_telegram_result = send_scanner_if_changed(state, config, current)
    except Exception as exc:
        scanner_telegram_result = {"configured": True, "sent": False, "error": str(exc)}
        print(f"Telegram scanner non inviato: {exc}")

    # run_execution_cycle saves first; save again to persist notifications and publication state.
    save_state(state, config, current)
    cycle_payload = {
        "generated_utc": current.isoformat(timespec="seconds"),
        "market_source": bundle.get("source"),
        "assets": len(bundle.get("assets", {})),
        "signals": len(signals),
        "opened": summary.get("opened", []),
        "closed": summary.get("closed", []),
        "trailing_updates": summary.get("trailing_updates", []),
        "risk_alerts": summary.get("risk_alerts", []),
        "risk_recoveries": summary.get("risk_recoveries", []),
        "telegram_paper": telegram_result,
        "telegram_scanner": scanner_telegram_result,
        "live_publication": publish_result,
    }
    CYCLE_SUMMARY_PATH.write_text(json.dumps(cycle_payload, ensure_ascii=False, indent=2), encoding="utf-8")

    print(
        json.dumps(
            {
                "generated_utc": current.isoformat(timespec="seconds"),
                "market_source": bundle.get("source"),
                "assets": len(bundle.get("assets", {})),
                "signals": len(signals),
                "opened": len(summary.get("opened", [])),
                "closed": len(summary.get("closed", [])),
                "trailing_updates": len(summary.get("trailing_updates", [])),
                "risk_alerts": len(summary.get("risk_alerts", [])),
                "telegram_paper": bool(telegram_result.get("sent")),
                "telegram_scanner": bool(scanner_telegram_result.get("sent")),
                "live_published": bool(publish_result.get("published")),
                "live_unchanged": bool(publish_result.get("unchanged")),
                "publish_reasons": publish_reasons,
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
