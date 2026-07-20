# -*- coding: utf-8 -*-
"""Block 9: Hall of Fame, Evolution Score and genetic memory.

Paper-only. It scores strategies, records mutation outcomes and exposes a
policy used by Block 5 on the following cycle. It never changes an existing
strategy, promotes, retires, rolls back, touches live or sends orders.
"""
from __future__ import annotations

import copy
import csv
import hashlib
import json
import math
import re
import statistics
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

REPORTS = Path("reports")
CONFIG_PATH = Path("config/evolution_memory_block9.json")
CANDIDATE_STATE = REPORTS / "paper_trading_evolution_candidate_state.json"
CANDIDATE_REGISTRY = REPORTS / "paper_trading_evolution_candidate_registry.json"
VALIDATIONS = REPORTS / "paper_trading_evolution_candidate_validations.csv"
PROMOTIONS = REPORTS / "paper_trading_evolution_promotion_state.json"
POST_PROMOTION = REPORTS / "paper_trading_evolution_post_promotion_comparisons.csv"
TRADE_LOG = REPORTS / "paper_trading_trade_log.csv"

STATE = REPORTS / "paper_trading_evolution_memory_state.json"
SCORES = REPORTS / "paper_trading_evolution_scores.csv"
HALL_JSON = REPORTS / "paper_trading_evolution_hall_of_fame.json"
HALL_CSV = REPORTS / "paper_trading_evolution_hall_of_fame.csv"
MEMORY_JSON = REPORTS / "paper_trading_evolution_genetic_memory.json"
MEMORY_CSV = REPORTS / "paper_trading_evolution_genetic_memory.csv"
HISTORY = REPORTS / "paper_trading_evolution_memory_history.csv"
REPORT = REPORTS / "paper_trading_evolution_memory_report.md"
CONFIG_SNAPSHOT = REPORTS / "paper_trading_evolution_memory_config_snapshot.json"

SCHEMA_VERSION = 1
ENGINE_VERSION = "block9-evolution-memory-v1"

DEFAULT_CONFIG = {
    "schema_version": 1,
    "enabled": True,
    "paper_only": True,
    "candidate_policy_enabled": True,
    "block_avoid_status": True,
    "block_single_critical": True,
    "allow_global_fallback": True,
    "minimum_baseline_trades_for_hall": 30,
    "minimum_candidate_pairs_for_hall": 80,
    "hall_of_fame_limit": 20,
    "minimum_memory_trials": 2,
    "minimum_memory_pairs": 80,
    "minimum_trials_to_block": 2,
    "minimum_pairs_to_block": 120,
    "favor_score": 70.0,
    "caution_score": 40.0,
    "avoid_score": 25.0,
    "automatic_mutation": False,
    "automatic_promotion": False,
    "automatic_retirement": False,
    "automatic_rollback": False,
    "modify_existing_strategy": False,
    "modify_candidate_state": False,
    "modify_promotion_state": False,
    "live_side_effects_allowed": False,
    "orders_allowed": False,
}

SCORE_FIELDS = [
    "generated_utc", "strategy_id", "family_id", "portfolio",
    "lifecycle_status", "record_kind", "evolution_score", "grade",
    "hall_eligible", "closed_trades", "matched_pairs", "expectancy_r",
    "profit_factor", "win_rate", "max_drawdown_r", "liquidations",
    "validation_status", "post_promotion_status", "source_evidence_score",
    "validation_score",
]
MEMORY_FIELDS = [
    "generated_utc", "signature", "scope", "family_id", "scenario_kind",
    "parameter", "direction", "target_bucket", "status", "memory_score",
    "block_new_candidates", "trials", "validated_trials",
    "total_matched_pairs", "mean_validation_delta_r",
    "mean_validation_score", "promotion_ready", "promoted",
    "healthy_post_promotion", "watch_post_promotion",
    "rollback_recommended", "critical", "rolled_back",
    "underperforming", "risk_rejected", "posterior_success", "reason",
]
HALL_FIELDS = [
    "generated_utc", "category", "rank", "strategy_id", "family_id",
    "portfolio", "lifecycle_status", "evolution_score", "grade",
    "closed_trades", "matched_pairs", "profit_factor", "expectancy_r",
    "max_drawdown_r",
]
HISTORY_FIELDS = [
    "generated_utc", "entity_type", "entity_id", "previous_status",
    "current_status", "previous_score", "current_score", "reason",
]


def now_utc() -> datetime:
    return datetime.now(timezone.utc)


def iso(value: datetime | None = None) -> str:
    return (value or now_utc()).astimezone(timezone.utc).isoformat(timespec="seconds")


def finite(value: Any, default: float = 0.0) -> float:
    try:
        number = float(value)
    except (TypeError, ValueError):
        return default
    return number if math.isfinite(number) else default


def integer(value: Any, default: int = 0) -> int:
    return int(finite(value, default))


def truthy(value: Any) -> bool:
    return str(value).strip().lower() in {"1", "true", "yes", "y"}


def clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def slug(value: Any) -> str:
    text = re.sub(r"[^A-Za-z0-9]+", "-", str(value or "").strip()).strip("-").lower()
    return text or "unknown"


def stable_id(prefix: str, value: str) -> str:
    return f"{prefix}-{hashlib.sha256(value.encode()).hexdigest()[:20]}"


def deep_merge(base: dict[str, Any], custom: dict[str, Any]) -> dict[str, Any]:
    output = copy.deepcopy(base)
    for key, value in custom.items():
        if isinstance(value, dict) and isinstance(output.get(key), dict):
            output[key] = deep_merge(output[key], value)
        else:
            output[key] = copy.deepcopy(value)
    return output


def load_json(path: Path, default: Any) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return copy.deepcopy(default)


def atomic_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(text, encoding="utf-8")
    temporary.replace(path)


def atomic_json(path: Path, value: Any) -> None:
    atomic_text(path, json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n")


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    try:
        with path.open("r", encoding="utf-8", newline="") as handle:
            return list(csv.DictReader(handle))
    except (OSError, csv.Error):
        return []


def write_csv(path: Path, fields: list[str], rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fields})


def append_csv(path: Path, fields: list[str], rows: list[dict[str, Any]]) -> None:
    if not rows:
        return
    exists = path.exists() and path.stat().st_size > 0
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        if not exists:
            writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fields})


def load_config(write_snapshot: bool = True) -> dict[str, Any]:
    custom = load_json(CONFIG_PATH, {})
    config = deep_merge(DEFAULT_CONFIG, custom if isinstance(custom, dict) else {})
    if write_snapshot:
        atomic_json(CONFIG_SNAPSHOT, config)
    return config


def direction(old: Any, new: Any) -> str:
    try:
        old_number, new_number = float(old), float(new)
    except (TypeError, ValueError):
        return "CHANGE"
    if math.isclose(old_number, new_number, rel_tol=1e-9, abs_tol=1e-9):
        return "UNCHANGED"
    return "INCREASE" if new_number > old_number else "DECREASE"


def target_bucket(parameter: str, value: Any) -> str:
    try:
        number = float(value)
    except (TypeError, ValueError):
        return slug(value)
    if parameter == "reward_risk":
        number = round(number * 2) / 2
    elif parameter == "max_holding_hours":
        number = round(number)
    elif parameter in {"trailing_at_r", "trailing_atr_multiple"}:
        number = round(number * 4) / 4
    else:
        number = round(number, 4)
    return f"{number:g}"


def mutation_signature(
    family_id: str, scenario_kind: str, parameter: str, old: Any, new: Any
) -> str:
    return "|".join([
        slug(family_id), str(scenario_kind or "UNKNOWN").upper(),
        str(parameter or "unknown"), direction(old, new),
        target_bucket(parameter, new),
    ])


def latest_by(rows: list[dict[str, Any]], key: str) -> dict[str, dict[str, Any]]:
    return {
        str(row.get(key, "")): row
        for row in rows
        if str(row.get(key, "")).strip()
    }


def promotion_indexes(document: dict[str, Any]) -> tuple[dict[str, dict[str, Any]], set[str]]:
    rows = list(document.get("transactions", []) or [])
    active = document.get("active_by_family", {}) or {}
    if isinstance(active, dict):
        rows.extend(row for row in active.values() if isinstance(row, dict))
    by_candidate, rolled_back = {}, set()
    for row in rows:
        if not isinstance(row, dict):
            continue
        candidate_id = str(row.get("candidate_id", "")).strip()
        if not candidate_id:
            continue
        by_candidate[candidate_id] = row
        if str(row.get("status", "")).upper() in {"ROLLED_BACK", "ROLLBACK_EXECUTED"}:
            rolled_back.add(candidate_id)
    return by_candidate, rolled_back


def profit_factor(values: list[float]) -> float:
    gains = sum(value for value in values if value > 0)
    losses = abs(sum(value for value in values if value < 0))
    return (99.0 if gains > 0 else 0.0) if losses <= 1e-12 else gains / losses


def max_drawdown(values: list[float]) -> float:
    total = peak = worst = 0.0
    for value in values:
        total += value
        peak = max(peak, total)
        worst = max(worst, peak - total)
    return worst


def portfolio_metrics(rows: list[dict[str, Any]]) -> dict[str, Any]:
    closed = [row for row in rows if str(row.get("closed_at", "")).strip()]
    values = [finite(row.get("r_multiple")) for row in closed]
    return {
        "closed_trades": len(values),
        "expectancy_r": statistics.mean(values) if values else 0.0,
        "profit_factor": profit_factor(values),
        "win_rate": sum(value > 0 for value in values) / len(values) if values else 0.0,
        "max_drawdown_r": max_drawdown(values),
        "liquidations": sum(
            str(row.get("close_reason", "")).upper().startswith("LIQUIDATION")
            for row in closed
        ),
    }


def score_grade(score: float) -> str:
    if score >= 90:
        return "S"
    if score >= 80:
        return "A"
    if score >= 70:
        return "B"
    if score >= 55:
        return "C"
    if score >= 40:
        return "D"
    return "E"


def score_strategy(
    strategy_id: str,
    family_id: str,
    portfolio: str,
    lifecycle: str,
    kind: str,
    evidence_score: float,
    validation: dict[str, Any] | None,
    post: dict[str, Any] | None,
    metrics: dict[str, Any],
    config: dict[str, Any],
    when: datetime,
) -> dict[str, Any]:
    validation = validation or {}
    post = post or {}
    pairs = integer(validation.get("matched_pairs"))
    trades = max(integer(metrics.get("closed_trades")), pairs)
    expectancy = finite(validation.get("candidate_expectancy_r")) if pairs else finite(metrics.get("expectancy_r"))
    pf = finite(validation.get("candidate_profit_factor")) if pairs else finite(metrics.get("profit_factor"))
    win = finite(validation.get("candidate_win_rate")) if pairs else finite(metrics.get("win_rate"))
    drawdown = finite(validation.get("candidate_max_drawdown_r")) if pairs else finite(metrics.get("max_drawdown_r"))
    liquidations = max(integer(validation.get("candidate_liquidations")), integer(metrics.get("liquidations")))

    score = 0.0
    score += clamp(evidence_score / 100) * 15
    score += clamp(finite(validation.get("validation_score")) / 100) * 20
    score += clamp(max(trades, pairs) / 150) * 15
    score += clamp((expectancy + 0.25) / 0.75) * 8
    score += clamp((pf - 0.75) / 1.25) * 8
    score += clamp((win - 0.35) / 0.35) * 4
    if pairs:
        score += 5 if finite(validation.get("bootstrap_ci_low_r")) > 0 else 0
        score += clamp(integer(validation.get("positive_folds")) / 4) * 5
    score += {
        "MASTER": 10, "EX_MASTER": 7, "SHADOW": 3,
        "CANDIDATE": 0, "BACKGROUND": 1, "BASELINE": 2,
    }.get(lifecycle.upper(), 0)
    score += {
        "HEALTHY": 10, "MONITORING": 5, "WAITING_SAMPLE": 2,
        "WATCH": -5, "ROLLBACK_RECOMMENDED": -15,
        "CRITICAL": -25, "ROLLBACK_WINDOW_EXPIRED": -20,
    }.get(str(post.get("status", "")).upper(), 0)
    penalty = min(20, liquidations * 5) + clamp(drawdown / 15) * 5
    if str(validation.get("status", "")).upper() == "RISK_REJECTED":
        penalty += 15
    elif str(validation.get("status", "")).upper() == "UNDERPERFORMING":
        penalty += 10
    score = round(clamp((score - penalty) / 100) * 100, 2)

    lifecycle_upper = lifecycle.upper()
    hall = (
        lifecycle_upper in {"MASTER", "EX_MASTER"}
        or (
            lifecycle_upper in {"CANDIDATE", "SHADOW"}
            and pairs >= integer(config.get("minimum_candidate_pairs_for_hall"), 80)
        )
        or (
            lifecycle_upper in {"BASELINE", "BACKGROUND"}
            and trades >= integer(config.get("minimum_baseline_trades_for_hall"), 30)
        )
    )
    return {
        "generated_utc": iso(when), "strategy_id": strategy_id,
        "family_id": family_id, "portfolio": portfolio,
        "lifecycle_status": lifecycle_upper, "record_kind": kind,
        "evolution_score": score, "grade": score_grade(score),
        "hall_eligible": hall, "closed_trades": trades, "matched_pairs": pairs,
        "expectancy_r": expectancy, "profit_factor": pf, "win_rate": win,
        "max_drawdown_r": drawdown, "liquidations": liquidations,
        "validation_status": str(validation.get("status", "")).upper(),
        "post_promotion_status": str(post.get("status", "")).upper(),
        "source_evidence_score": evidence_score,
        "validation_score": finite(validation.get("validation_score")),
    }


def build_scores(
    candidate_state: dict[str, Any],
    validations: dict[str, dict[str, Any]],
    promotions: dict[str, dict[str, Any]],
    posts: dict[str, dict[str, Any]],
    trade_rows: list[dict[str, Any]],
    config: dict[str, Any],
    when: datetime,
) -> list[dict[str, Any]]:
    trades_by_portfolio: dict[str, list[dict[str, Any]]] = {}
    for row in trade_rows:
        portfolio = str(row.get("portfolio", "")).strip()
        if portfolio:
            trades_by_portfolio.setdefault(portfolio, []).append(row)

    output, seen = [], set()
    candidates = candidate_state.get("candidates", {}) if isinstance(candidate_state, dict) else {}
    for row in candidates.values() if isinstance(candidates, dict) else []:
        if not isinstance(row, dict):
            continue
        candidate_id = str(row.get("candidate_id", "")).strip()
        portfolio = str(row.get("portfolio_name", "")).strip()
        if not candidate_id or not portfolio:
            continue
        output.append(score_strategy(
            candidate_id, str(row.get("family_id", "unknown")), portfolio,
            str(row.get("status", "CANDIDATE")), "EVOLUTION_STRATEGY",
            finite((row.get("source_evidence", {}) or {}).get("evidence_score")),
            validations.get(candidate_id), posts.get(candidate_id),
            portfolio_metrics(trades_by_portfolio.get(portfolio, [])),
            config, when,
        ))
        seen.add(portfolio)

    for candidate_id, tx in promotions.items():
        parent = str(tx.get("parent_portfolio", "")).strip()
        if not parent or parent in seen:
            continue
        post = posts.get(candidate_id, {})
        metrics = {
            "closed_trades": integer(post.get("matched_pairs")),
            "expectancy_r": finite(post.get("ex_master_expectancy_r")),
            "profit_factor": finite(post.get("ex_master_profit_factor")),
            "win_rate": finite(post.get("ex_master_win_rate")),
            "max_drawdown_r": finite(post.get("ex_master_max_drawdown_r")),
            "liquidations": integer(post.get("ex_master_liquidations")),
        }
        output.append(score_strategy(
            str(tx.get("parent_id") or stable_id("portfolio", parent)),
            str(tx.get("family_id", "unknown")), parent, "EX_MASTER",
            "RETAINED_EX_MASTER", 0, None, None, metrics, config, when,
        ))
        seen.add(parent)

    for portfolio, rows in trades_by_portfolio.items():
        if portfolio not in seen:
            output.append(score_strategy(
                stable_id("portfolio", portfolio), slug(portfolio), portfolio,
                "BASELINE", "PAPER_PORTFOLIO", 0, None, None,
                portfolio_metrics(rows), config, when,
            ))
    output.sort(
        key=lambda row: (
            finite(row.get("evolution_score")),
            integer(row.get("matched_pairs")),
            integer(row.get("closed_trades")),
        ),
        reverse=True,
    )
    return output


def memory_template(signature: str, scope: str, family: str, kind: str, parameter: str, old: Any, new: Any) -> dict[str, Any]:
    return {
        "signature": signature, "scope": scope, "family_id": family,
        "scenario_kind": kind, "parameter": parameter,
        "direction": direction(old, new), "target_bucket": target_bucket(parameter, new),
        "trials": 0, "validated_trials": 0, "total_matched_pairs": 0,
        "_weighted_delta": 0.0, "_weighted_score": 0.0,
        "promotion_ready": 0, "promoted": 0, "healthy_post_promotion": 0,
        "watch_post_promotion": 0, "rollback_recommended": 0,
        "critical": 0, "rolled_back": 0, "underperforming": 0,
        "risk_rejected": 0, "early_outperformer": 0,
    }


def finalize_memory(row: dict[str, Any], config: dict[str, Any], when: datetime) -> dict[str, Any]:
    pairs = integer(row.get("total_matched_pairs"))
    delta = finite(row.get("_weighted_delta")) / pairs if pairs else 0.0
    validation_score = finite(row.get("_weighted_score")) / pairs if pairs else 0.0
    successes = (
        0.5 * integer(row.get("early_outperformer"))
        + 1.5 * integer(row.get("promotion_ready"))
        + 2 * integer(row.get("promoted"))
        + 2.5 * integer(row.get("healthy_post_promotion"))
    )
    failures = (
        1.5 * integer(row.get("underperforming"))
        + 2 * integer(row.get("risk_rejected"))
        + integer(row.get("watch_post_promotion"))
        + 2.5 * integer(row.get("rollback_recommended"))
        + 4 * integer(row.get("critical"))
        + 3 * integer(row.get("rolled_back"))
    )
    posterior = (1 + successes) / (2 + successes + failures)
    depth = clamp(pairs / 300 + integer(row.get("trials")) / 10)
    delta_signal = clamp(0.5 + delta / 0.2)
    score = 100 * (0.5 * posterior + 0.25 * depth + 0.25 * delta_signal)
    score -= min(
        35,
        12 * integer(row.get("critical"))
        + 8 * integer(row.get("rollback_recommended"))
        + 10 * integer(row.get("rolled_back")),
    )
    score = round(clamp(score / 100) * 100, 2)

    trials = integer(row.get("trials"))
    critical = integer(row.get("critical"))
    rolled_back = integer(row.get("rolled_back"))
    if critical or rolled_back or (
        score <= finite(config.get("avoid_score"), 25)
        and trials >= integer(config.get("minimum_memory_trials"), 2)
    ):
        status, reason = "AVOID", "Critical, rolled-back or strongly negative history."
    elif (
        trials < integer(config.get("minimum_memory_trials"), 2)
        or pairs < integer(config.get("minimum_memory_pairs"), 80)
        or integer(row.get("validated_trials")) == 0
    ):
        status, reason = "INSUFFICIENT", "Mutation history is not deep enough."
    elif (
        score >= finite(config.get("favor_score"), 70)
        and (
            integer(row.get("promotion_ready"))
            + integer(row.get("promoted"))
            + integer(row.get("healthy_post_promotion"))
        ) > 0
    ):
        status, reason = "FAVOR", "Repeated positive validation or promotion outcomes."
    elif (
        score < finite(config.get("caution_score"), 40)
        or integer(row.get("rollback_recommended"))
        or integer(row.get("risk_rejected"))
    ):
        status, reason = "CAUTION", "Negative or unstable evidence."
    else:
        status, reason = "NEUTRAL", "Mixed or ordinary mutation history."

    block = (
        status == "AVOID"
        and truthy(config.get("block_avoid_status", True))
        and (
            (
                trials >= integer(config.get("minimum_trials_to_block"), 2)
                and pairs >= integer(config.get("minimum_pairs_to_block"), 120)
            )
            or (
                critical > 0
                and truthy(config.get("block_single_critical", True))
            )
        )
    )
    output = {key: value for key, value in row.items() if not key.startswith("_")}
    output.update({
        "generated_utc": iso(when), "status": status, "memory_score": score,
        "block_new_candidates": block, "mean_validation_delta_r": delta,
        "mean_validation_score": validation_score,
        "posterior_success": posterior, "reason": reason,
    })
    return output


def build_memory(
    candidate_state: dict[str, Any],
    validations: dict[str, dict[str, Any]],
    promotions: dict[str, dict[str, Any]],
    rolled_back: set[str],
    posts: dict[str, dict[str, Any]],
    config: dict[str, Any],
    when: datetime,
) -> list[dict[str, Any]]:
    aggregates: dict[str, dict[str, Any]] = {}
    candidates = candidate_state.get("candidates", {}) if isinstance(candidate_state, dict) else {}
    for candidate in candidates.values() if isinstance(candidates, dict) else []:
        if not isinstance(candidate, dict):
            continue
        cid = str(candidate.get("candidate_id", ""))
        mutation = candidate.get("mutation", {}) or {}
        source = candidate.get("source_evidence", {}) or {}
        family = str(candidate.get("family_id", "unknown"))
        kind = str(source.get("scenario_kind", "UNKNOWN")).upper()
        parameter = str(mutation.get("parameter", "unknown"))
        old, new = mutation.get("old_value"), mutation.get("new_value")
        validation = validations.get(cid, {})
        post = posts.get(cid, {})
        tx = promotions.get(cid, {})

        for scope, memory_family in (("FAMILY", family), ("GLOBAL", "GLOBAL")):
            signature = mutation_signature(memory_family, kind, parameter, old, new)
            row = aggregates.setdefault(
                signature,
                memory_template(signature, scope, memory_family, kind, parameter, old, new),
            )
            row["trials"] += 1
            pairs = integer(validation.get("matched_pairs"))
            if pairs:
                row["validated_trials"] += 1
                row["total_matched_pairs"] += pairs
                row["_weighted_delta"] += finite(validation.get("mean_delta_r")) * pairs
                row["_weighted_score"] += finite(validation.get("validation_score")) * pairs

            validation_status = str(validation.get("status", "")).upper()
            mapping = {
                "PROMOTION_REVIEW_READY": "promotion_ready",
                "EARLY_OUTPERFORMER": "early_outperformer",
                "UNDERPERFORMING": "underperforming",
                "RISK_REJECTED": "risk_rejected",
            }
            if validation_status in mapping:
                row[mapping[validation_status]] += 1
            if str(tx.get("status", "")).upper() in {"EXECUTED", "ROLLED_BACK", "ROLLBACK_EXECUTED"}:
                row["promoted"] += 1
            if cid in rolled_back:
                row["rolled_back"] += 1
            post_status = str(post.get("status", "")).upper()
            post_mapping = {
                "HEALTHY": "healthy_post_promotion",
                "WATCH": "watch_post_promotion",
                "ROLLBACK_RECOMMENDED": "rollback_recommended",
                "ROLLBACK_WINDOW_EXPIRED": "rollback_recommended",
                "CRITICAL": "critical",
            }
            if post_status in post_mapping:
                row[post_mapping[post_status]] += 1

    rows = [finalize_memory(row, config, when) for row in aggregates.values()]
    rows.sort(
        key=lambda row: (
            row.get("scope") == "FAMILY",
            finite(row.get("memory_score")),
            integer(row.get("total_matched_pairs")),
        ),
        reverse=True,
    )
    return rows


def mutation_policy_decision(
    parent: dict[str, Any],
    mutation: dict[str, Any],
    evidence: dict[str, Any] | None = None,
) -> dict[str, Any]:
    config = load_config(write_snapshot=False)
    if not truthy(config.get("candidate_policy_enabled", True)):
        return {
            "allow": True, "reason": "GENETIC_MEMORY_POLICY_DISABLED",
            "status": "DISABLED", "memory_score": None, "signature": "", "scope": "",
        }
    document = load_json(MEMORY_JSON, {"records": {}})
    records = document.get("records", {}) if isinstance(document, dict) else {}
    family = slug(
        parent.get("strategy")
        or parent.get("evolution_family_id")
        or parent.get("name")
    )
    kind = str(
        mutation.get("scenario_kind")
        or (evidence or {}).get("scenario_kind")
        or "UNKNOWN"
    ).upper()
    parameter = str(mutation.get("parameter", "unknown"))
    old, new = mutation.get("old_value"), mutation.get("new_value")
    signatures = [mutation_signature(family, kind, parameter, old, new)]
    if truthy(config.get("allow_global_fallback", True)):
        signatures.append(mutation_signature("GLOBAL", kind, parameter, old, new))

    selected = None
    for signature in signatures:
        if isinstance(records.get(signature), dict):
            selected = records[signature]
            break
    if selected is None:
        return {
            "allow": True, "reason": "GENETIC_MEMORY_NO_HISTORY",
            "status": "NO_HISTORY", "memory_score": None,
            "signature": signatures[0], "scope": "FAMILY",
        }
    blocked = truthy(selected.get("block_new_candidates"))
    return {
        "allow": not blocked,
        "reason": "GENETIC_MEMORY_AVOID" if blocked else "GENETIC_MEMORY_ALLOW",
        "status": str(selected.get("status", "UNKNOWN")),
        "memory_score": finite(selected.get("memory_score")),
        "signature": str(selected.get("signature", "")),
        "scope": str(selected.get("scope", "")),
        "trials": integer(selected.get("trials")),
        "total_matched_pairs": integer(selected.get("total_matched_pairs")),
    }


def hall_categories(
    scores: list[dict[str, Any]], config: dict[str, Any], when: datetime
) -> tuple[dict[str, list[dict[str, Any]]], list[dict[str, Any]]]:
    eligible = [row for row in scores if truthy(row.get("hall_eligible"))]
    limit = integer(config.get("hall_of_fame_limit"), 20)

    def top(statuses: set[str] | None = None) -> list[dict[str, Any]]:
        return [
            row for row in eligible
            if statuses is None or str(row.get("lifecycle_status", "")).upper() in statuses
        ][:limit]

    categories = {
        "ALL_TIME": top(),
        "MASTER": top({"MASTER"}),
        "EX_MASTER": top({"EX_MASTER"}),
        "CANDIDATE": top({"CANDIDATE", "SHADOW"}),
        "BASELINE": top({"BASELINE", "BACKGROUND"}),
    }
    rows = []
    for category, values in categories.items():
        for rank, row in enumerate(values, 1):
            rows.append({"generated_utc": iso(when), "category": category, "rank": rank, **row})
    return categories, rows


def enrich_registry(scores: list[dict[str, Any]], memories: list[dict[str, Any]], when: datetime) -> int:
    registry = load_json(CANDIDATE_REGISTRY, {})
    if not isinstance(registry, dict):
        return 0
    score_index = {str(row.get("strategy_id", "")): row for row in scores}
    memory_index = {str(row.get("signature", "")): row for row in memories}
    enriched = 0
    for row in registry.get("candidates", []):
        if not isinstance(row, dict):
            continue
        score = score_index.get(str(row.get("strategy_id", "")))
        if not score:
            continue
        metadata = row.setdefault("metadata", {})
        mutation = row.get("mutation", {}) or {}
        source = metadata.get("source_evidence", {}) or {}
        signature = mutation_signature(
            str(row.get("family_id", "unknown")),
            str(source.get("scenario_kind", "UNKNOWN")),
            str(mutation.get("parameter", "unknown")),
            mutation.get("old_value"), mutation.get("new_value"),
        )
        remembered = memory_index.get(signature, {})
        metadata["block9_evolution"] = {
            "generated_utc": iso(when),
            "evolution_score": score.get("evolution_score"),
            "grade": score.get("grade"),
            "hall_eligible": score.get("hall_eligible"),
            "genetic_memory": {
                "signature": signature,
                "status": remembered.get("status", "NO_HISTORY"),
                "memory_score": remembered.get("memory_score"),
                "block_new_candidates": remembered.get("block_new_candidates", False),
            },
            "automatic_promotion": False,
            "automatic_retirement": False,
            "live_modified": False,
        }
        enriched += 1
    registry.update({
        "block9_engine_version": ENGINE_VERSION,
        "block9_generated_utc": iso(when),
        "block9_scored_candidates": enriched,
        "automatic_promotions": 0,
        "automatic_retirements": 0,
        "live_modified": False,
        "orders_sent": False,
    })
    atomic_json(CANDIDATE_REGISTRY, registry)
    return enriched


def load_state() -> dict[str, Any]:
    default = {
        "schema_version": SCHEMA_VERSION, "engine_version": ENGINE_VERSION,
        "created_utc": iso(), "updated_utc": iso(),
        "strategies": {}, "memories": {}, "totals": {"cycles": 0},
    }
    state = load_json(STATE, default)
    if not isinstance(state, dict):
        state = default
    state.setdefault("strategies", {})
    state.setdefault("memories", {})
    state.setdefault("totals", {"cycles": 0})
    return state


def update_history(
    state: dict[str, Any],
    scores: list[dict[str, Any]],
    memories: list[dict[str, Any]],
    when: datetime,
) -> None:
    events = []
    for kind, rows, identity_key, status_key, score_key, store_key in (
        ("STRATEGY", scores, "strategy_id", "grade", "evolution_score", "strategies"),
        ("MUTATION_MEMORY", memories, "signature", "status", "memory_score", "memories"),
    ):
        store = state.setdefault(store_key, {})
        threshold = 5 if kind == "STRATEGY" else 10
        for row in rows:
            identity = str(row.get(identity_key, ""))
            previous = store.get(identity, {})
            old_status = str(previous.get("status", ""))
            new_status = str(row.get(status_key, ""))
            old_score = finite(previous.get("score"))
            new_score = finite(row.get(score_key))
            if not previous or old_status != new_status or abs(old_score - new_score) >= threshold:
                events.append({
                    "generated_utc": iso(when), "entity_type": kind,
                    "entity_id": identity, "previous_status": old_status or "NEW",
                    "current_status": new_status,
                    "previous_score": old_score if previous else "",
                    "current_score": new_score,
                    "reason": "EVOLUTION_MEMORY_UPDATE",
                })
            store[identity] = {
                "status": new_status, "score": new_score, "updated_utc": iso(when)
            }
    append_csv(HISTORY, HISTORY_FIELDS, events)


def render_report(
    scores: list[dict[str, Any]],
    memories: list[dict[str, Any]],
    categories: dict[str, list[dict[str, Any]]],
    when: datetime,
) -> str:
    lines = [
        "# Blocco 9 — Hall of Fame e memoria genetica", "",
        f"Generato: {iso(when)}", "",
        "> Paper-only. La memoria può bloccare soltanto una futura proposta "
        "Block 5 classificata AVOID; non modifica strategie esistenti.", "",
        "## Stato", "",
        f"- Strategie/portafogli valutati: **{len(scores)}**",
        f"- Hall of Fame: **{len(categories.get('ALL_TIME', []))}**",
        f"- Memorie genetiche: **{len(memories)}**",
        f"- Firme bloccate: **{sum(truthy(row.get('block_new_candidates')) for row in memories)}**",
        "- Azioni automatiche e live: **0**", "",
        "## Hall of Fame", "",
        "| Rank | Strategia | Stato | Score | Grade | Trade | PF | Expectancy R | DD R |",
        "| ---: | --- | --- | ---: | --- | ---: | ---: | ---: | ---: |",
    ]
    for rank, row in enumerate(categories.get("ALL_TIME", [])[:10], 1):
        lines.append(
            f"| {rank} | {row.get('portfolio')} | {row.get('lifecycle_status')} | "
            f"{finite(row.get('evolution_score')):.1f} | {row.get('grade')} | "
            f"{row.get('closed_trades')} | {finite(row.get('profit_factor')):.2f} | "
            f"{finite(row.get('expectancy_r')):.3f} | "
            f"{finite(row.get('max_drawdown_r')):.2f} |"
        )
    if not categories.get("ALL_TIME"):
        lines.append("| — | Nessun record ancora eleggibile | — | 0 | — | 0 | 0 | 0 | 0 |")
    lines.extend([
        "", "## Memoria genetica", "",
        "| Scope | Famiglia | Mutazione | Target | Stato | Score | Prove | Coppie | Blocco |",
        "| --- | --- | --- | --- | --- | ---: | ---: | ---: | --- |",
    ])
    for row in memories[:20]:
        lines.append(
            f"| {row.get('scope')} | {row.get('family_id')} | "
            f"{row.get('parameter')} {row.get('direction')} | "
            f"{row.get('target_bucket')} | {row.get('status')} | "
            f"{finite(row.get('memory_score')):.1f} | {row.get('trials')} | "
            f"{row.get('total_matched_pairs')} | "
            f"{'SI' if truthy(row.get('block_new_candidates')) else 'NO'} |"
        )
    if not memories:
        lines.append("| — | — | Nessuna candidata ancora creata | — | INSUFFICIENT | 0 | 0 | 0 | NO |")
    lines.extend([
        "", "## Sicurezza", "",
        "- Nessuna strategia, posizione o promozione esistente viene modificata.",
        "- Nessuna mutazione, promozione, pensionamento o rollback automatico.",
        "- Nessun effetto live e nessun ordine reale.", "",
    ])
    text = "\n".join(lines)
    atomic_text(REPORT, text)
    return text


def run_evolution_memory_cycle(when: datetime | None = None) -> dict[str, Any]:
    current = when or now_utc()
    config = load_config()
    if not truthy(config.get("enabled", True)):
        return {
            "enabled": False, "status": "DISABLED", "scored_strategies": 0,
            "hall_of_fame": 0, "memory_records": 0, "favored_mutations": 0,
            "avoided_mutations": 0, "blocked_mutations": 0,
            "automatic_mutations": 0, "automatic_promotions": 0,
            "report_markdown": "",
        }

    candidate_state = load_json(CANDIDATE_STATE, {"candidates": {}})
    validations = latest_by(read_csv(VALIDATIONS), "candidate_id")
    promotion_doc = load_json(PROMOTIONS, {"transactions": [], "active_by_family": {}})
    promotions, rolled_back = promotion_indexes(
        promotion_doc if isinstance(promotion_doc, dict) else {}
    )
    posts = latest_by(read_csv(POST_PROMOTION), "master_candidate_id")
    trade_rows = read_csv(TRADE_LOG)

    scores = build_scores(
        candidate_state if isinstance(candidate_state, dict) else {"candidates": {}},
        validations, promotions, posts, trade_rows, config, current,
    )
    memories = build_memory(
        candidate_state if isinstance(candidate_state, dict) else {"candidates": {}},
        validations, promotions, rolled_back, posts, config, current,
    )

    write_csv(SCORES, SCORE_FIELDS, scores)
    write_csv(MEMORY_CSV, MEMORY_FIELDS, memories)

    categories, hall_rows = hall_categories(scores, config, current)
    atomic_json(HALL_JSON, {
        "schema_version": SCHEMA_VERSION, "engine_version": ENGINE_VERSION,
        "generated_utc": iso(current), "paper_only": True,
        "automatic_promotions": 0, "automatic_retirements": 0,
        "live_modified": False, "orders_sent": False, "categories": categories,
    })
    write_csv(HALL_CSV, HALL_FIELDS, hall_rows)

    memory_doc = {
        "schema_version": SCHEMA_VERSION, "engine_version": ENGINE_VERSION,
        "generated_utc": iso(current), "paper_only": True,
        "candidate_policy_enabled": True, "automatic_mutations": 0,
        "automatic_promotions": 0, "automatic_retirements": 0,
        "automatic_rollbacks": 0, "existing_strategies_modified": False,
        "live_modified": False, "orders_sent": False,
        "record_count": len(memories),
        "blocked_signature_count": sum(
            truthy(row.get("block_new_candidates")) for row in memories
        ),
        "records": {str(row["signature"]): row for row in memories},
    }
    atomic_json(MEMORY_JSON, memory_doc)

    state = load_state()
    update_history(state, scores, memories, current)
    state["updated_utc"] = iso(current)
    state.setdefault("totals", {})["cycles"] = integer(
        state.get("totals", {}).get("cycles")
    ) + 1
    for key in (
        "automatic_mutations", "automatic_promotions",
        "automatic_retirements", "automatic_rollbacks",
    ):
        state["totals"][key] = 0
    atomic_json(STATE, state)

    enriched = enrich_registry(scores, memories, current)
    report = render_report(scores, memories, categories, current)

    return {
        "enabled": True, "status": "OK", "engine_version": ENGINE_VERSION,
        "scored_strategies": len(scores),
        "hall_of_fame": len(categories.get("ALL_TIME", [])),
        "memory_records": len(memories),
        "favored_mutations": sum(row.get("status") == "FAVOR" for row in memories),
        "caution_mutations": sum(row.get("status") == "CAUTION" for row in memories),
        "avoided_mutations": sum(row.get("status") == "AVOID" for row in memories),
        "blocked_mutations": sum(
            truthy(row.get("block_new_candidates")) for row in memories
        ),
        "registry_enriched": enriched,
        "automatic_mutations": 0, "automatic_promotions": 0,
        "automatic_retirements": 0, "automatic_rollbacks": 0,
        "existing_strategies_modified": False,
        "candidate_state_modified": False, "promotion_state_modified": False,
        "live_modified": False, "orders_sent": False,
        "report_markdown": report,
    }
