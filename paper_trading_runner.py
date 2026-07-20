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
from paper_trading_diagnostics import (
    annotate_market_freshness,
    build_signal_diagnostics,
    finalize_signal_diagnostics,
    write_signal_diagnostics,
)
from paper_trading_config import load_config
from paper_trading_engine import (
    TRADE_FIELDS,
    TRADE_LOG_PATH,
    current_prices,
    load_state,
    portfolio_equity,
    risk_gate,
    run_execution_cycle,
    save_state,
    signal_log,
)
from paper_trading_trade_log_repair import (
    reconcile_state_counters,
    repair_trade_log,
)
from paper_trading_live_publish import publish_markdown
from paper_trading_event_enrichment import enrich_opened_positions
from paper_trading_notify import notify
from paper_trading_open_positions_notify import send_open_positions_report
from paper_trading_shadow_exit import run_shadow_exit_cycle
from paper_trading_shadow_evaluation import run_shadow_evaluation_cycle
from paper_trading_crash_guard import run_crash_guard_cycle
from paper_trading_candidate_engine import prepare_candidate_config
from paper_trading_candidate_validator import run_candidate_validation_cycle
from paper_trading_promotion_governor import run_promotion_governance_cycle
from paper_trading_post_promotion_watchdog import run_post_promotion_watchdog_cycle
from paper_trading_evolution_memory import run_evolution_memory_cycle
from paper_trading_regime_evolution import run_regime_evolution_cycle
from paper_trading_live_bridge import run_live_bridge_cycle
from paper_trading_evolution_control_tower import run_control_tower_cycle
from research_all_signals import run_research_cycle
from strategy_dual_validation import build_dual_validation_report
# DOGE_REJECTION_SHORT_IMPORT
from doge_rejection_short import run_doge_rejection_cycle
from doge_short_status_notify import send_doge_short_status
from paper_trading_report import (
    LATEST_REPORT_PATH,
    REPORT_PATH,
    portfolio_metrics,
    render_report,
    replace_block,
)
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
    base_config = load_config()
    try:
        candidate_result = prepare_candidate_config(
            base_config,
            datetime.now(timezone.utc),
        )
        config = candidate_result["config"]
    except Exception as exc:
        candidate_result = {
            "summary": {
                "status": "ERROR",
                "error": str(exc),
                "active_candidates": 0,
                "new_candidates": 0,
                "rejected_evidence": 0,
                "automatic_promotions": 0,
                "automatic_retirements": 0,
                "base_portfolios_modified": False,
                "live_modified": False,
                "orders_sent": False,
            },
            "report_markdown": "",
        }
        config = base_config
        print(f"Block 5 Candidate Engine non eseguito: {exc}")
    # TRADE_LOG_REPAIR_STARTUP_V1
    trade_log_repair = repair_trade_log(
        TRADE_LOG_PATH,
        TRADE_FIELDS,
    )
    bundle = annotate_market_freshness(
        collect_with_fallback(config),
        config,
    )
    raw_signals = generate_signals(bundle, config)
    state = load_state(config)
    trade_log_reconcile = reconcile_state_counters(
        state,
        list(trade_log_repair.get("records", [])),
    )
    signal_diagnostics = build_signal_diagnostics(
        bundle,
        config,
        raw_signals,
        state,
    )
    research_eligible_ids = {
        str(row.get("signal_id", ""))
        for row in signal_diagnostics.get("rows", [])
        if row.get("status") in {"READY", "RISK_GATE"}
        and row.get("signal_id")
    }
    research_signals = [
        signal
        for signal in raw_signals
        if signal.signal_id in research_eligible_ids
    ]
    research_result = run_research_cycle(
        research_signals,
        bundle,
        config,
    )
    executable_ids = set(
        signal_diagnostics.get(
            "executable_signal_ids",
            [],
        )
    )
    signals = [
        signal
        for signal in raw_signals
        if signal.signal_id in executable_ids
    ]

    # BLOCK4_5_CRASH_GUARD_START
    cycle_time = datetime.now(timezone.utc)
    try:
        crash_guard_result = run_crash_guard_cycle(
            state,
            signals,
            bundle,
            config,
            cycle_time,
        )
    except Exception as exc:
        crash_guard_result = {
            "enabled": True,
            "status": "ERROR",
            "error": str(exc),
            "allowed_signals": signals,
            "blocked_signal_objects": [],
            "blocked_signals": 0,
            "active_simulations": 0,
            "completed_simulations": 0,
            "level": "FAIL_OPEN",
            "direction": "NONE",
            "context": {
                "level": "NORMAL",
                "direction": "NONE",
                "risk_model_version": "block4_5_v1",
            },
            "report_markdown": "",
            "paper_positions_modified": False,
            "live_modified": False,
            "orders_sent": False,
        }
        print(
            f"Block 4.5 Crash Guard non eseguito: {exc}"
        )

    signals = list(
        crash_guard_result.get(
            "allowed_signals",
            signals,
        )
    )
    bundle["_crash_guard_context"] = dict(
        crash_guard_result.get(
            "context",
            {
                "level": "NORMAL",
                "direction": "NONE",
                "risk_model_version": "block4_5_v1",
            },
        )
    )
    for blocked_signal in crash_guard_result.get(
        "blocked_signal_objects",
        [],
    ):
        signal_log(
            blocked_signal,
            "REJECTED",
            "CRASH_GUARD_BLOCKED",
            cycle_time,
        )
    # BLOCK4_5_CRASH_GUARD_END

    before = _position_snapshot(state, bundle)
    summary = run_execution_cycle(
        state,
        signals,
        bundle,
        config,
        cycle_time,
    )
    summary["crash_guard"] = {
        key: value
        for key, value in crash_guard_result.items()
        if key not in {
            "allowed_signals",
            "blocked_signal_objects",
            "report_markdown",
            "decisions",
            "stress_test",
            "context",
        }
    }
    summary["evolution_candidates"] = dict(
        candidate_result.get("summary", {})
    )
    # BLOCK3_SHADOW_EXIT_START
    try:
        shadow_exit_result = run_shadow_exit_cycle(
            summary,
            state,
            bundle,
            config,
            datetime.now(timezone.utc),
        )
    except Exception as exc:
        shadow_exit_result = {
            "enabled": True,
            "status": "ERROR",
            "error": str(exc),
            "report_markdown": "",
            "paper_positions_modified": False,
            "orders_sent": False,
        }
        print(f"Block 3 Shadow Exit non eseguito: {exc}")
    summary["shadow_exit"] = {
        key: value
        for key, value in shadow_exit_result.items()
        if key != "report_markdown"
    }
    # BLOCK3_SHADOW_EXIT_END
    # BLOCK4_SHADOW_EVALUATION_START
    try:
        shadow_evaluation_result = run_shadow_evaluation_cycle(
            datetime.now(timezone.utc),
        )
    except Exception as exc:
        shadow_evaluation_result = {
            "enabled": True,
            "status": "ERROR",
            "error": str(exc),
            "report_markdown": "",
            "paper_positions_modified": False,
            "paper_exits_modified": False,
            "mutations_created": 0,
            "orders_sent": False,
        }
        print(f"Block 4 valutazione Shadow non eseguito: {exc}")
    summary["shadow_evaluation"] = {
        key: value
        for key, value in shadow_evaluation_result.items()
        if key != "report_markdown"
    }
    # BLOCK4_SHADOW_EVALUATION_END
    # BLOCK6_CANDIDATE_VALIDATION_START
    try:
        candidate_validation_result = (
            run_candidate_validation_cycle(
                datetime.now(timezone.utc)
            )
        )
    except Exception as exc:
        candidate_validation_result = {
            "enabled": True,
            "status": "ERROR",
            "error": str(exc),
            "evaluated_candidates": 0,
            "promotion_review_ready": 0,
            "status_counts": {},
            "registry_enriched": 0,
            "automatic_promotions": 0,
            "automatic_retirements": 0,
            "candidate_state_modified": False,
            "parent_state_modified": False,
            "live_modified": False,
            "orders_sent": False,
            "report_markdown": "",
        }
        print(
            "Block 6 Candidate Validation non eseguito: "
            f"{exc}"
        )
    summary["evolution_candidate_validation"] = {
        key: value
        for key, value in candidate_validation_result.items()
        if key != "report_markdown"
    }
    # BLOCK6_CANDIDATE_VALIDATION_END
    # BLOCK7_PROMOTION_GOVERNANCE_START
    try:
        promotion_governance_result = run_promotion_governance_cycle(
            datetime.now(timezone.utc)
        )
    except Exception as exc:
        promotion_governance_result = {
            "enabled": True, "status": "ERROR", "error": str(exc),
            "plans": 0, "pending_approval": 0, "approved_waiting_execute": 0,
            "active_promotions": 0, "automatic_promotions": 0,
            "automatic_rollbacks": 0, "candidate_state_modified": False,
            "parent_state_modified": False, "live_modified": False,
            "orders_sent": False, "report_markdown": "",
        }
        print(f"Block 7 Promotion Governance non eseguito: {exc}")
    summary["evolution_promotion_governance"] = {
        key: value for key, value in promotion_governance_result.items()
        if key != "report_markdown"
    }
    # BLOCK7_PROMOTION_GOVERNANCE_END
    # BLOCK8_POST_PROMOTION_WATCHDOG_START
    try:
        post_promotion_result = (
            run_post_promotion_watchdog_cycle(
                datetime.now(timezone.utc)
            )
        )
    except Exception as exc:
        post_promotion_result = {
            "enabled": True,
            "status": "ERROR",
            "error": str(exc),
            "active_promotions": 0,
            "monitored": 0,
            "waiting_sample": 0,
            "monitoring": 0,
            "healthy": 0,
            "watch": 0,
            "rollback_recommended": 0,
            "critical": 0,
            "rollback_window_expired": 0,
            "recommendation_count": 0,
            "automatic_rollbacks": 0,
            "automatic_promotions": 0,
            "automatic_retirements": 0,
            "promotion_state_modified": False,
            "master_state_modified": False,
            "ex_master_state_modified": False,
            "live_modified": False,
            "orders_sent": False,
            "report_markdown": "",
        }
        print(
            "Block 8 Post-Promotion Watchdog non "
            f"eseguito: {exc}"
        )
    summary["evolution_post_promotion"] = {
        key: value
        for key, value in post_promotion_result.items()
        if key != "report_markdown"
    }
    # BLOCK8_POST_PROMOTION_WATCHDOG_END
    # BLOCK9_EVOLUTION_MEMORY_START
    try:
        evolution_memory_result = (
            run_evolution_memory_cycle(
                datetime.now(timezone.utc)
            )
        )
    except Exception as exc:
        evolution_memory_result = {
            "enabled": True,
            "status": "ERROR",
            "error": str(exc),
            "scored_strategies": 0,
            "hall_of_fame": 0,
            "memory_records": 0,
            "favored_mutations": 0,
            "caution_mutations": 0,
            "avoided_mutations": 0,
            "blocked_mutations": 0,
            "registry_enriched": 0,
            "automatic_mutations": 0,
            "automatic_promotions": 0,
            "automatic_retirements": 0,
            "automatic_rollbacks": 0,
            "existing_strategies_modified": False,
            "candidate_state_modified": False,
            "promotion_state_modified": False,
            "live_modified": False,
            "orders_sent": False,
            "report_markdown": "",
        }
        print(
            "Block 9 Evolution Memory non eseguito: "
            f"{exc}"
        )
    summary["evolution_memory"] = {
        key: value
        for key, value in evolution_memory_result.items()
        if key != "report_markdown"
    }
    # BLOCK9_EVOLUTION_MEMORY_END
    # BLOCK10_REGIME_EVOLUTION_START
    try:
        regime_evolution_result = (
            run_regime_evolution_cycle(
                datetime.now(timezone.utc)
            )
        )
    except Exception as exc:
        regime_evolution_result = {
            "enabled": True,
            "status": "ERROR",
            "error": str(exc),
            "current_regime": "UNKNOWN",
            "regime_source": "ERROR",
            "timeline_rows": 0,
            "performance_rows": 0,
            "preferred": 0,
            "avoid": 0,
            "memory_records": 0,
            "candidate_blocks": 0,
            "registry_enriched": 0,
            "routing_mode": "ADVISORY_ONLY",
            "automatic_switches": 0,
            "automatic_position_changes": 0,
            "automatic_mutations": 0,
            "automatic_promotions": 0,
            "automatic_retirements": 0,
            "automatic_rollbacks": 0,
            "existing_strategies_modified": False,
            "candidate_state_modified": False,
            "live_modified": False,
            "orders_sent": False,
            "report_markdown": "",
        }
        print(
            "Block 10 Regime Evolution non eseguito: "
            f"{exc}"
        )
    summary["evolution_regime"] = {
        key: value
        for key, value in regime_evolution_result.items()
        if key != "report_markdown"
    }
    # BLOCK10_REGIME_EVOLUTION_END
    # BLOCK11_PROTECTED_LIVE_BRIDGE_START
    try:
        live_bridge_result = run_live_bridge_cycle(
            datetime.now(timezone.utc)
        )
    except Exception as exc:
        live_bridge_result = {
            "enabled": True,
            "status": "ERROR",
            "error": str(exc),
            "mode": "LOCKED_REVIEW_ONLY",
            "plans": 0,
            "review_ready": 0,
            "adapter_locked": 0,
            "approved": 0,
            "not_eligible": 0,
            "live_adapter_configured": False,
            "live_execution_enabled": False,
            "human_approval_required": True,
            "explicit_execution_required": True,
            "rollback_blueprint_required": True,
            "automatic_releases": 0,
            "automatic_strategy_switches": 0,
            "automatic_position_changes": 0,
            "live_modified": False,
            "orders_sent": False,
            "report_markdown": "",
        }
        print(f"Block 11 Protected Live Bridge non eseguito: {exc}")
    summary["evolution_live_bridge"] = {
        key: value
        for key, value in live_bridge_result.items()
        if key != "report_markdown"
    }
    # BLOCK11_PROTECTED_LIVE_BRIDGE_END
    # BLOCK12_EVOLUTION_CONTROL_TOWER_START
    try:
        control_tower_result = run_control_tower_cycle(
            summary=summary,
            market_bundle=bundle,
            when=cycle_time,
        )
    except Exception as exc:
        control_tower_result = {
            "enabled": True,
            "status": "ERROR",
            "error": str(exc),
            "mode": "OBSERVE_AUDIT_ONLY",
            "health": "CRITICAL",
            "check_count": 0,
            "warning_count": 0,
            "critical_count": 1,
            "pipeline_complete": False,
            "live_locked": True,
            "storage_complete": False,
            "audit_chain_valid": False,
            "recovery_status": "BLOCKED",
            "automatic_repairs": 0,
            "automatic_restarts": 0,
            "automatic_mutations": 0,
            "automatic_promotions": 0,
            "automatic_retirements": 0,
            "automatic_rollbacks": 0,
            "automatic_releases": 0,
            "live_modified": False,
            "orders_sent": False,
            "telegram_sent": False,
            "report_markdown": "",
        }
        print(f"Block 12 Evolution Control Tower non eseguito: {exc}")
    summary["evolution_control_tower"] = {
        key: value
        for key, value in control_tower_result.items()
        if key not in {"report_markdown", "checks", "systemd"}
    }
    # BLOCK12_EVOLUTION_CONTROL_TOWER_END
    after = _position_snapshot(state, bundle)
    summary["trailing_updates"] = _trailing_updates(before, after)
    # TELEGRAM_OPENING_PNL_ENRICHMENT_V1
    enrich_opened_positions(summary, bundle, config)
    risk_alerts, risk_recoveries = _risk_changes(state, bundle, config)
    summary["risk_alerts"] = risk_alerts
    summary["risk_recoveries"] = risk_recoveries
    signal_diagnostics = finalize_signal_diagnostics(
        signal_diagnostics,
        summary,
    )
    write_signal_diagnostics(signal_diagnostics)
    summary["signal_diagnostics"] = (
        signal_diagnostics.get("summary", {})
    )

    # DOGE_REJECTION_SHORT_CYCLE_START
    try:
        doge_rejection_result = run_doge_rejection_cycle(bundle, config)
    except Exception as exc:
        doge_rejection_result = {
            "report_markdown": "",
            "phase": "ERROR",
            "position_open": False,
            "error": str(exc),
        }
        print(f"DOGE rejection short non eseguito: {exc}")
    # DOGE_REJECTION_SHORT_CYCLE_END
    # DOGE_SHORT_STATUS_TELEGRAM_START
    try:
        doge_status_result = send_doge_short_status(bundle)
    except Exception as exc:
        doge_status_result = {
            "configured": True,
            "sent": False,
            "error": str(exc),
        }
        print(f"Stato Telegram DOGE non inviato: {exc}")
    # DOGE_SHORT_STATUS_TELEGRAM_END


    current = datetime.now(timezone.utc)
    report = render_report(state, config)
    dual_validation_result = build_dual_validation_report(
        portfolio_metrics(state, config),
        list(research_result.get("metrics", [])),
    )
    dual_validation_markdown = str(
        dual_validation_result.get("report_markdown", "")
    ).strip()
    if dual_validation_markdown:
        report = (
            report.rstrip()
            + "\n\n"
            + dual_validation_markdown
            + "\n"
        )
    # DOGE_REJECTION_SHORT_REPORT_START
    doge_rejection_markdown = str(
        doge_rejection_result.get("report_markdown", "")
    ).strip()
    if doge_rejection_markdown:
        report = report.rstrip() + "\n\n" + doge_rejection_markdown + "\n"
    # DOGE_REJECTION_SHORT_REPORT_END
    research_markdown = str(research_result.get("report_markdown", "")).strip()
    if research_markdown:
        report = report.rstrip() + "\n\n" + research_markdown + "\n"
    # BLOCK3_SHADOW_EXIT_REPORT_START
    shadow_exit_markdown = str(
        shadow_exit_result.get("report_markdown", "")
    ).strip()
    if shadow_exit_markdown:
        report = (
            report.rstrip()
            + "\n\n"
            + shadow_exit_markdown
            + "\n"
        )
    # BLOCK3_SHADOW_EXIT_REPORT_END
    # BLOCK4_SHADOW_EVALUATION_REPORT_START
    shadow_evaluation_markdown = str(
        shadow_evaluation_result.get("report_markdown", "")
    ).strip()
    if shadow_evaluation_markdown:
        report = (
            report.rstrip()
            + "\n\n"
            + shadow_evaluation_markdown
            + "\n"
        )
    # BLOCK4_SHADOW_EVALUATION_REPORT_END
    # BLOCK4_5_CRASH_GUARD_REPORT_START
    crash_guard_markdown = str(
        crash_guard_result.get("report_markdown", "")
    ).strip()
    if crash_guard_markdown:
        report = (
            report.rstrip()
            + "\n\n"
            + crash_guard_markdown
            + "\n"
        )
    # BLOCK4_5_CRASH_GUARD_REPORT_END
    # BLOCK5_EVOLUTION_CANDIDATE_REPORT_START
    candidate_markdown = str(
        candidate_result.get("report_markdown", "")
    ).strip()
    if candidate_markdown:
        report = report.rstrip() + "\n\n" + candidate_markdown + "\n"
    # BLOCK5_EVOLUTION_CANDIDATE_REPORT_END
    # BLOCK6_CANDIDATE_VALIDATION_REPORT_START
    candidate_validation_markdown = str(
        candidate_validation_result.get(
            "report_markdown",
            "",
        )
    ).strip()
    if candidate_validation_markdown:
        report = (
            report.rstrip()
            + "\n\n"
            + candidate_validation_markdown
            + "\n"
        )
    # BLOCK6_CANDIDATE_VALIDATION_REPORT_END
    # BLOCK7_PROMOTION_GOVERNANCE_REPORT_START
    promotion_governance_markdown = str(
        promotion_governance_result.get("report_markdown", "")
    ).strip()
    if promotion_governance_markdown:
        report = report.rstrip() + "\n\n" + promotion_governance_markdown + "\n"
    # BLOCK7_PROMOTION_GOVERNANCE_REPORT_END
    # BLOCK8_POST_PROMOTION_WATCHDOG_REPORT_START
    post_promotion_markdown = str(
        post_promotion_result.get(
            "report_markdown",
            "",
        )
    ).strip()
    if post_promotion_markdown:
        report = (
            report.rstrip()
            + "\n\n"
            + post_promotion_markdown
            + "\n"
        )
    # BLOCK8_POST_PROMOTION_WATCHDOG_REPORT_END
    # BLOCK9_EVOLUTION_MEMORY_REPORT_START
    evolution_memory_markdown = str(
        evolution_memory_result.get(
            "report_markdown",
            "",
        )
    ).strip()
    if evolution_memory_markdown:
        report = (
            report.rstrip()
            + "\n\n"
            + evolution_memory_markdown
            + "\n"
        )
    # BLOCK9_EVOLUTION_MEMORY_REPORT_END
    # BLOCK10_REGIME_EVOLUTION_REPORT_START
    regime_evolution_markdown = str(
        regime_evolution_result.get(
            "report_markdown",
            "",
        )
    ).strip()
    if regime_evolution_markdown:
        report = (
            report.rstrip()
            + "\n\n"
            + regime_evolution_markdown
            + "\n"
        )
    # BLOCK10_REGIME_EVOLUTION_REPORT_END
    # BLOCK11_PROTECTED_LIVE_BRIDGE_REPORT_START
    live_bridge_markdown = str(
        live_bridge_result.get("report_markdown", "")
    ).strip()
    if live_bridge_markdown:
        report = report.rstrip() + "\n\n" + live_bridge_markdown + "\n"
    # BLOCK11_PROTECTED_LIVE_BRIDGE_REPORT_END
    # BLOCK12_EVOLUTION_CONTROL_TOWER_REPORT_START
    control_tower_markdown = str(
        control_tower_result.get("report_markdown", "")
    ).strip()
    if control_tower_markdown:
        report = report.rstrip() + "\n\n" + control_tower_markdown + "\n"
    # BLOCK12_EVOLUTION_CONTROL_TOWER_REPORT_END
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

    # OPEN_POSITIONS_TELEGRAM_SEPARATE_V5
    open_positions_telegram_result = {
        "configured": False,
        "sent": False,
        "messages": 0,
        "skipped": True,
    }
    if telegram_result.get("account_summary_sent"):
        try:
            open_positions_telegram_result = (
                send_open_positions_report(
                    state,
                    config,
                    bundle,
                    current,
                )
            )
        except Exception as exc:
            open_positions_telegram_result = {
                "configured": True,
                "sent": False,
                "messages": 0,
                "error": str(exc),
            }
            print(
                "Telegram posizioni aperte non inviato: "
                f"{exc}"
            )

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
        "signals_generated": len(raw_signals),
        "signals_executable": len(signals),
        "market_freshness": bundle.get(
            "_paper_freshness",
            {},
        ),
        "research_all_signals": {
            "opened_this_cycle": research_result.get("opened_this_cycle", 0),
            "closed_this_cycle": research_result.get("closed_this_cycle", 0),
            "open_positions": research_result.get("open_positions", 0),
            "closed_trades": research_result.get("closed_trades", 0),
        },
        "strategy_dual_validation": {
            "ready_for_live_review": dual_validation_result.get(
                "ready_for_live_review", 0
            ),
            "status_counts": dual_validation_result.get(
                "status_counts", {}
            ),
            "thresholds": dual_validation_result.get(
                "thresholds", {}
            ),
        },
        # DOGE_REJECTION_SHORT_PAYLOAD
        "doge_rejection_short": {
            "phase": doge_rejection_result.get("phase"),
            "position_open": doge_rejection_result.get("position_open", False),
            "equity_eur": doge_rejection_result.get("equity_eur"),
            "opened_this_cycle": doge_rejection_result.get("opened_this_cycle", 0),
            "management_events": doge_rejection_result.get("management_events", 0),
            "telegram": doge_rejection_result.get("telegram", {}),
            "error": doge_rejection_result.get("error"),
        },
        "signal_diagnostics": signal_diagnostics.get(
            "summary",
            {},
        ),
        "shadow_exit": summary.get("shadow_exit", {}),
        "shadow_evaluation": summary.get("shadow_evaluation", {}),
        "crash_guard": summary.get("crash_guard", {}),
        "evolution_candidates": summary.get("evolution_candidates", {}),
        "evolution_candidate_validation": summary.get("evolution_candidate_validation", {}),
        "evolution_promotion_governance": summary.get("evolution_promotion_governance", {}),
        "evolution_post_promotion": summary.get("evolution_post_promotion", {}),
        "evolution_memory": summary.get("evolution_memory", {}),
        "evolution_regime": summary.get("evolution_regime", {}),
        "evolution_live_bridge": summary.get("evolution_live_bridge", {}),
        "evolution_control_tower": summary.get("evolution_control_tower", {}),
        "opened": summary.get("opened", []),
        "closed": summary.get("closed", []),
        "trailing_updates": summary.get("trailing_updates", []),
        "risk_alerts": summary.get("risk_alerts", []),
        "risk_recoveries": summary.get("risk_recoveries", []),
        "telegram_paper": telegram_result,
        "telegram_open_positions": open_positions_telegram_result,
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
                "signals_generated": len(raw_signals),
                "signals_executable": len(signals),
                "market_data_status": bundle.get(
                    "_paper_freshness",
                    {},
                ).get("status"),
                "opened": len(summary.get("opened", [])),
                "closed": len(summary.get("closed", [])),
                "trailing_updates": len(summary.get("trailing_updates", [])),
                "risk_alerts": len(summary.get("risk_alerts", [])),
                "shadow_exit_status": summary.get("shadow_exit", {}).get("status"),
                "shadow_exit_active_groups": summary.get("shadow_exit", {}).get("active_groups", 0),
                "shadow_exit_new_results": summary.get("shadow_exit", {}).get("new_results", 0),
                "shadow_evaluation_status": summary.get("shadow_evaluation", {}).get("status"),
                "shadow_evaluation_rows": summary.get("shadow_evaluation", {}).get("evaluation_rows", 0),
                "shadow_evaluation_robust": summary.get("shadow_evaluation", {}).get("robust_count", 0),
                "shadow_evaluation_eligible": summary.get("shadow_evaluation", {}).get("eligible_for_mutation", 0),
                "crash_guard_status": summary.get("crash_guard", {}).get("status"),
                "crash_guard_level": summary.get("crash_guard", {}).get("level"),
                "crash_guard_direction": summary.get("crash_guard", {}).get("direction"),
                "crash_guard_blocked": summary.get("crash_guard", {}).get("blocked_signals", 0),
                "crash_guard_active_simulations": summary.get("crash_guard", {}).get("active_simulations", 0),
                "crash_guard_completed_simulations": summary.get("crash_guard", {}).get("completed_simulations", 0),
                "evolution_candidate_status": summary.get("evolution_candidates", {}).get("status"),
                "evolution_candidate_active": summary.get("evolution_candidates", {}).get("active_candidates", 0),
                "evolution_candidate_new": summary.get("evolution_candidates", {}).get("new_candidates", 0),
                "evolution_candidate_rejected": summary.get("evolution_candidates", {}).get("rejected_evidence", 0),
                "evolution_candidate_promotions": summary.get("evolution_candidates", {}).get("automatic_promotions", 0),
                "evolution_validation_status": summary.get("evolution_candidate_validation", {}).get("status"),
                "evolution_validation_candidates": summary.get("evolution_candidate_validation", {}).get("evaluated_candidates", 0),
                "evolution_validation_review_ready": summary.get("evolution_candidate_validation", {}).get("promotion_review_ready", 0),
                "evolution_validation_promotions": summary.get("evolution_candidate_validation", {}).get("automatic_promotions", 0),
                "evolution_promotion_status": summary.get("evolution_promotion_governance", {}).get("status"),
                "evolution_promotion_plans": summary.get("evolution_promotion_governance", {}).get("plans", 0),
                "evolution_promotion_pending": summary.get("evolution_promotion_governance", {}).get("pending_approval", 0),
                "evolution_promotion_approved": summary.get("evolution_promotion_governance", {}).get("approved_waiting_execute", 0),
                "evolution_promotion_active": summary.get("evolution_promotion_governance", {}).get("active_promotions", 0),
                "evolution_promotion_automatic": summary.get("evolution_promotion_governance", {}).get("automatic_promotions", 0),
                "evolution_post_promotion_status": summary.get("evolution_post_promotion", {}).get("status"),
                "evolution_post_promotion_active": summary.get("evolution_post_promotion", {}).get("active_promotions", 0),
                "evolution_post_promotion_monitored": summary.get("evolution_post_promotion", {}).get("monitored", 0),
                "evolution_post_promotion_healthy": summary.get("evolution_post_promotion", {}).get("healthy", 0),
                "evolution_post_promotion_watch": summary.get("evolution_post_promotion", {}).get("watch", 0),
                "evolution_post_promotion_rollback": summary.get("evolution_post_promotion", {}).get("rollback_recommended", 0),
                "evolution_post_promotion_critical": summary.get("evolution_post_promotion", {}).get("critical", 0),
                "evolution_post_promotion_automatic": summary.get("evolution_post_promotion", {}).get("automatic_rollbacks", 0),
                "evolution_memory_status": summary.get("evolution_memory", {}).get("status"),
                "evolution_memory_scored": summary.get("evolution_memory", {}).get("scored_strategies", 0),
                "evolution_memory_hall_of_fame": summary.get("evolution_memory", {}).get("hall_of_fame", 0),
                "evolution_memory_records": summary.get("evolution_memory", {}).get("memory_records", 0),
                "evolution_memory_favored": summary.get("evolution_memory", {}).get("favored_mutations", 0),
                "evolution_memory_avoided": summary.get("evolution_memory", {}).get("avoided_mutations", 0),
                "evolution_memory_blocked": summary.get("evolution_memory", {}).get("blocked_mutations", 0),
                "evolution_memory_automatic": summary.get("evolution_memory", {}).get("automatic_mutations", 0),
                "evolution_regime_status": summary.get("evolution_regime", {}).get("status"),
                "evolution_regime_current": summary.get("evolution_regime", {}).get("current_regime"),
                "evolution_regime_rows": summary.get("evolution_regime", {}).get("performance_rows", 0),
                "evolution_regime_preferred": summary.get("evolution_regime", {}).get("preferred", 0),
                "evolution_regime_avoid": summary.get("evolution_regime", {}).get("avoid", 0),
                "evolution_regime_memory": summary.get("evolution_regime", {}).get("memory_records", 0),
                "evolution_regime_candidate_blocks": summary.get("evolution_regime", {}).get("candidate_blocks", 0),
                "evolution_regime_automatic": summary.get("evolution_regime", {}).get("automatic_switches", 0),
                "evolution_live_bridge_status": summary.get("evolution_live_bridge", {}).get("status"),
                "evolution_live_bridge_mode": summary.get("evolution_live_bridge", {}).get("mode"),
                "evolution_live_bridge_plans": summary.get("evolution_live_bridge", {}).get("plans", 0),
                "evolution_live_bridge_review_ready": summary.get("evolution_live_bridge", {}).get("review_ready", 0),
                "evolution_live_bridge_adapter_locked": summary.get("evolution_live_bridge", {}).get("adapter_locked", 0),
                "evolution_live_bridge_approved": summary.get("evolution_live_bridge", {}).get("approved", 0),
                "evolution_live_bridge_automatic": summary.get("evolution_live_bridge", {}).get("automatic_releases", 0),
                "evolution_control_tower_status": summary.get("evolution_control_tower", {}).get("status"),
                "evolution_control_tower_health": summary.get("evolution_control_tower", {}).get("health"),
                "evolution_control_tower_checks": summary.get("evolution_control_tower", {}).get("check_count", 0),
                "evolution_control_tower_warnings": summary.get("evolution_control_tower", {}).get("warning_count", 0),
                "evolution_control_tower_critical": summary.get("evolution_control_tower", {}).get("critical_count", 0),
                "evolution_control_tower_pipeline_complete": summary.get("evolution_control_tower", {}).get("pipeline_complete", False),
                "evolution_control_tower_live_locked": summary.get("evolution_control_tower", {}).get("live_locked", True),
                "evolution_control_tower_audit_valid": summary.get("evolution_control_tower", {}).get("audit_chain_valid", False),
                "evolution_control_tower_recovery": summary.get("evolution_control_tower", {}).get("recovery_status"),
                "evolution_control_tower_automatic": summary.get("evolution_control_tower", {}).get("automatic_releases", 0),
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
