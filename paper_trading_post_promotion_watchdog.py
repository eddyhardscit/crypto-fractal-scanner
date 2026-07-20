# -*- coding: utf-8 -*-
"""Block 8 post-promotion Champion/Ex-Master watchdog.

Paper-only surveillance after a human-approved Block 7 promotion.

For each active executed promotion, the new MASTER and retained EX_MASTER are
compared on the same post-promotion experiment groups. The watchdog can issue:

- WAITING_SAMPLE
- MONITORING
- HEALTHY
- WATCH
- ROLLBACK_RECOMMENDED
- CRITICAL
- ROLLBACK_WINDOW_EXPIRED

It never performs a rollback, promotion, retirement, configuration mutation,
live change or order action. Block 7's explicit human rollback command remains
the only rollback mechanism.
"""

from __future__ import annotations

import copy
import csv
import hashlib
import json
import math
import random
import statistics
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

REPORTS_DIR = Path("reports")
CONFIG_PATH = Path(
    "config/evolution_post_promotion_block8.json"
)

PROMOTION_STATE_PATH = (
    REPORTS_DIR
    / "paper_trading_evolution_promotion_state.json"
)
TRADE_LOG_PATH = REPORTS_DIR / "paper_trading_trade_log.csv"

STATE_PATH = (
    REPORTS_DIR
    / "paper_trading_evolution_post_promotion_state.json"
)
COMPARISONS_PATH = (
    REPORTS_DIR
    / "paper_trading_evolution_post_promotion_comparisons.csv"
)
HISTORY_PATH = (
    REPORTS_DIR
    / "paper_trading_evolution_post_promotion_history.csv"
)
ROLLBACK_RECOMMENDATIONS_PATH = (
    REPORTS_DIR
    / "paper_trading_evolution_rollback_recommendations.json"
)
REPORT_PATH = (
    REPORTS_DIR
    / "paper_trading_evolution_post_promotion_report.md"
)
CONFIG_SNAPSHOT_PATH = (
    REPORTS_DIR
    / "paper_trading_evolution_post_promotion_config_snapshot.json"
)

SCHEMA_VERSION = 1
ENGINE_VERSION = "block8-post-promotion-watchdog-v1"

COMPARISON_FIELDS = [
    "generated_utc",
    "transaction_id",
    "plan_id",
    "family_id",
    "master_candidate_id",
    "master_portfolio",
    "ex_master_id",
    "ex_master_portfolio",
    "executed_utc",
    "rollback_deadline_utc",
    "rollback_window_open",
    "status",
    "severity",
    "health_score",
    "master_closed_eligible",
    "ex_master_closed_eligible",
    "matched_pairs",
    "match_rate",
    "distinct_assets",
    "mean_delta_r",
    "median_delta_r",
    "trimmed_mean_delta_r",
    "total_delta_r",
    "master_expectancy_r",
    "ex_master_expectancy_r",
    "master_profit_factor",
    "ex_master_profit_factor",
    "master_win_rate",
    "ex_master_win_rate",
    "master_max_drawdown_r",
    "ex_master_max_drawdown_r",
    "drawdown_ratio",
    "master_liquidations",
    "ex_master_liquidations",
    "bootstrap_ci_low_r",
    "bootstrap_ci_high_r",
    "positive_folds",
    "latest_fold_mean_r",
    "top5_positive_dependency",
    "recommendation",
    "reason",
]

HISTORY_FIELDS = [
    "generated_utc",
    "transaction_id",
    "family_id",
    "master_portfolio",
    "ex_master_portfolio",
    "previous_status",
    "current_status",
    "severity",
    "health_score",
    "matched_pairs",
    "mean_delta_r",
    "bootstrap_ci_high_r",
    "drawdown_ratio",
    "master_liquidations",
    "ex_master_liquidations",
    "reason",
]

DEFAULT_CONFIG: dict[str, Any] = {
    "schema_version": 1,
    "enabled": True,
    "paper_only": True,
    "automatic_rollback": False,
    "automatic_promotion": False,
    "automatic_retirement": False,
    "modify_promotion_state": False,
    "modify_master_state": False,
    "modify_ex_master_state": False,
    "live_side_effects_allowed": False,
    "orders_allowed": False,
    "required_risk_model_version": "block4_5_v1",
    "require_full_from_entry": True,
    "minimum_monitoring_pairs": 20,
    "minimum_health_pairs": 50,
    "minimum_rollback_pairs": 80,
    "minimum_match_rate": 0.75,
    "minimum_distinct_assets": 2,
    "watch_mean_delta_r": -0.03,
    "rollback_mean_delta_r": -0.08,
    "rollback_total_delta_r": -6.0,
    "watch_drawdown_ratio": 1.20,
    "rollback_drawdown_ratio": 1.50,
    "critical_drawdown_ratio": 2.00,
    "maximum_drawdown_extra_r": 1.00,
    "watch_profit_factor_ratio": 0.90,
    "rollback_profit_factor_ratio": 0.80,
    "risk_recommend_on_extra_liquidation": True,
    "critical_on_two_extra_liquidations": True,
    "minimum_positive_folds_for_health": 2,
    "bootstrap_iterations": 1000,
    "bootstrap_confidence": 0.95,
    "temporal_folds": 4,
    "trim_fraction": 0.10,
    "maximum_top5_positive_dependency": 0.60,
}


def now_utc() -> datetime:
    return datetime.now(timezone.utc)


def iso_utc(value: datetime | None = None) -> str:
    return (
        value or now_utc()
    ).astimezone(timezone.utc).isoformat(timespec="seconds")


def finite(value: Any, default: float = 0.0) -> float:
    try:
        number = float(value)
    except (TypeError, ValueError):
        return default
    return number if math.isfinite(number) else default


def integer(value: Any, default: int = 0) -> int:
    return int(finite(value, default))


def truthy(value: Any) -> bool:
    return str(value).strip().lower() in {
        "1",
        "true",
        "yes",
        "y",
    }


def parse_time(value: Any) -> datetime:
    text = str(value or "").strip()
    if not text:
        return datetime.min.replace(tzinfo=timezone.utc)
    parsed = datetime.fromisoformat(
        text.replace("Z", "+00:00")
    )
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def deep_merge(
    base: dict[str, Any],
    custom: dict[str, Any],
) -> dict[str, Any]:
    output = copy.deepcopy(base)
    for key, value in custom.items():
        if (
            isinstance(value, dict)
            and isinstance(output.get(key), dict)
        ):
            output[key] = deep_merge(
                output[key],
                value,
            )
        else:
            output[key] = copy.deepcopy(value)
    return output


def load_json(path: Path, default: Any) -> Any:
    try:
        value = json.loads(
            path.read_text(encoding="utf-8")
        )
    except (OSError, json.JSONDecodeError):
        return copy.deepcopy(default)
    return value


def atomic_write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(text, encoding="utf-8")
    temporary.replace(path)


def atomic_write_json(path: Path, value: Any) -> None:
    atomic_write_text(
        path,
        json.dumps(
            value,
            ensure_ascii=False,
            indent=2,
            sort_keys=True,
        )
        + "\n",
    )


def append_csv(
    path: Path,
    fields: list[str],
    rows: Iterable[dict[str, Any]],
) -> None:
    values = list(rows)
    if not values:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    exists = path.exists() and path.stat().st_size > 0
    with path.open(
        "a",
        encoding="utf-8",
        newline="",
    ) as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=fields,
            extrasaction="ignore",
        )
        if not exists:
            writer.writeheader()
        for row in values:
            writer.writerow(
                {
                    field: row.get(field, "")
                    for field in fields
                }
            )


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    try:
        with path.open(
            "r",
            encoding="utf-8",
            newline="",
        ) as handle:
            return list(csv.DictReader(handle))
    except (OSError, csv.Error):
        return []


def load_config() -> dict[str, Any]:
    custom = load_json(CONFIG_PATH, {})
    config = deep_merge(
        DEFAULT_CONFIG,
        custom if isinstance(custom, dict) else {},
    )
    config["bootstrap_iterations"] = max(
        200,
        integer(
            config.get("bootstrap_iterations"),
            1000,
        ),
    )
    config["temporal_folds"] = max(
        2,
        integer(config.get("temporal_folds"), 4),
    )
    atomic_write_json(CONFIG_SNAPSHOT_PATH, config)
    return config


def empty_state() -> dict[str, Any]:
    return {
        "schema_version": SCHEMA_VERSION,
        "engine_version": ENGINE_VERSION,
        "created_utc": iso_utc(),
        "updated_utc": iso_utc(),
        "transactions": {},
        "totals": {
            "cycles": 0,
            "monitored": 0,
            "rollback_recommended": 0,
            "critical": 0,
            "automatic_rollbacks": 0,
        },
    }


def load_state() -> dict[str, Any]:
    value = load_json(STATE_PATH, empty_state())
    if not isinstance(value, dict):
        value = empty_state()
    value.setdefault("transactions", {})
    value.setdefault("totals", empty_state()["totals"])
    value["schema_version"] = SCHEMA_VERSION
    value["engine_version"] = ENGINE_VERSION
    return value


def active_transactions(
    promotion_state: dict[str, Any],
) -> list[dict[str, Any]]:
    active = (
        promotion_state.get("active_by_family", {})
        if isinstance(promotion_state, dict)
        else {}
    )
    rows = [
        copy.deepcopy(row)
        for row in (
            active.values()
            if isinstance(active, dict)
            else []
        )
        if isinstance(row, dict)
        and str(row.get("status", "")) == "EXECUTED"
    ]
    rows.sort(
        key=lambda row: (
            str(row.get("executed_utc", "")),
            str(row.get("transaction_id", "")),
        )
    )
    return rows


def eligible_trade(
    row: dict[str, Any],
    executed_at: datetime,
    config: dict[str, Any],
) -> bool:
    if parse_time(row.get("closed_at")) < executed_at:
        return False
    required_risk = str(
        config.get("required_risk_model_version", "")
    )
    if required_risk and str(
        row.get("risk_model_version_at_exit", "")
    ) != required_risk:
        return False
    if truthy(config.get("require_full_from_entry")):
        if str(
            row.get("excursion_quality", "")
        ).upper() != "FULL_FROM_ENTRY":
            return False
    return bool(
        str(row.get("experiment_group_id", "")).strip()
    )


def trade_index(
    rows: list[dict[str, Any]],
    portfolio: str,
    executed_at: datetime,
    config: dict[str, Any],
) -> dict[str, dict[str, Any]]:
    selected = [
        row
        for row in rows
        if str(row.get("portfolio", "")) == portfolio
        and eligible_trade(row, executed_at, config)
    ]
    selected.sort(
        key=lambda row: (
            parse_time(row.get("closed_at")),
            str(row.get("trade_id", "")),
        )
    )
    output: dict[str, dict[str, Any]] = {}
    for row in selected:
        group = str(row.get("experiment_group_id", ""))
        output.setdefault(group, row)
    return output


def paired_rows(
    trade_rows: list[dict[str, Any]],
    transaction: dict[str, Any],
    config: dict[str, Any],
) -> tuple[
    list[tuple[dict[str, Any], dict[str, Any]]],
    int,
    int,
]:
    executed_at = parse_time(
        transaction.get("executed_utc")
    )
    master_index = trade_index(
        trade_rows,
        str(transaction.get("candidate_portfolio", "")),
        executed_at,
        config,
    )
    ex_master_index = trade_index(
        trade_rows,
        str(transaction.get("parent_portfolio", "")),
        executed_at,
        config,
    )
    common = sorted(
        set(master_index) & set(ex_master_index),
        key=lambda key: parse_time(
            master_index[key].get("closed_at")
        ),
    )
    pairs = [
        (master_index[key], ex_master_index[key])
        for key in common
        if str(master_index[key].get("asset", ""))
        == str(ex_master_index[key].get("asset", ""))
        and str(master_index[key].get("side", ""))
        == str(ex_master_index[key].get("side", ""))
    ]
    return (
        pairs,
        len(master_index),
        len(ex_master_index),
    )


def trimmed_mean(
    values: list[float],
    fraction: float,
) -> float:
    if not values:
        return 0.0
    ordered = sorted(values)
    trim = int(
        len(ordered)
        * max(0.0, min(0.40, fraction))
    )
    if trim * 2 >= len(ordered):
        return statistics.mean(ordered)
    return statistics.mean(
        ordered[trim:len(ordered) - trim]
    )


def profit_factor(values: list[float]) -> float:
    gains = sum(value for value in values if value > 0)
    losses = abs(
        sum(value for value in values if value < 0)
    )
    if losses <= 1e-12:
        return 99.0 if gains > 0 else 0.0
    return gains / losses


def max_drawdown(values: list[float]) -> float:
    cumulative = 0.0
    peak = 0.0
    worst = 0.0
    for value in values:
        cumulative += value
        peak = max(peak, cumulative)
        worst = max(worst, peak - cumulative)
    return worst


def liquidation_count(
    rows: list[dict[str, Any]],
) -> int:
    return sum(
        str(
            row.get("close_reason", "")
        ).upper().startswith("LIQUIDATION")
        for row in rows
    )


def percentile(
    values: list[float],
    quantile: float,
) -> float:
    if not values:
        return 0.0
    ordered = sorted(values)
    position = (len(ordered) - 1) * max(
        0.0,
        min(1.0, quantile),
    )
    lower = int(math.floor(position))
    upper = int(math.ceil(position))
    if lower == upper:
        return ordered[lower]
    weight = position - lower
    return (
        ordered[lower] * (1.0 - weight)
        + ordered[upper] * weight
    )


def bootstrap_ci(
    values: list[float],
    transaction_id: str,
    iterations: int,
    confidence: float,
) -> tuple[float, float]:
    if not values:
        return 0.0, 0.0
    if len(values) == 1:
        return values[0], values[0]
    raw = (
        transaction_id
        + "|"
        + hashlib.sha256(
            json.dumps(values).encode("utf-8")
        ).hexdigest()
    )
    seed = int(
        hashlib.sha256(
            raw.encode("utf-8")
        ).hexdigest()[:16],
        16,
    )
    rng = random.Random(seed)
    count = len(values)
    means = []
    for _ in range(iterations):
        sample = [
            values[rng.randrange(count)]
            for _ in range(count)
        ]
        means.append(statistics.mean(sample))
    alpha = (
        1.0
        - max(0.50, min(0.999, confidence))
    ) / 2.0
    return (
        percentile(means, alpha),
        percentile(means, 1.0 - alpha),
    )


def temporal_fold_means(
    values: list[float],
    folds: int,
) -> list[float]:
    if not values:
        return []
    output = []
    for fold in range(folds):
        start = round(len(values) * fold / folds)
        end = round(
            len(values) * (fold + 1) / folds
        )
        chunk = values[start:end]
        if chunk:
            output.append(statistics.mean(chunk))
    return output


def top_positive_dependency(
    values: list[float],
) -> float:
    positives = sorted(
        [
            value
            for value in values
            if value > 0
        ],
        reverse=True,
    )
    total = sum(positives)
    if total <= 1e-12:
        return 1.0
    count = max(
        1,
        math.ceil(len(values) * 0.05),
    )
    return sum(positives[:count]) / total


def portfolio_metrics(
    rows: list[dict[str, Any]],
) -> dict[str, Any]:
    values = [
        finite(row.get("r_multiple"))
        for row in rows
    ]
    return {
        "trades": len(rows),
        "expectancy_r": (
            statistics.mean(values)
            if values
            else 0.0
        ),
        "profit_factor": profit_factor(values),
        "win_rate": (
            sum(value > 0 for value in values)
            / len(values)
            if values
            else 0.0
        ),
        "max_drawdown_r": max_drawdown(values),
        "liquidations": liquidation_count(rows),
    }


def health_score(
    metrics: dict[str, Any],
    config: dict[str, Any],
) -> float:
    matched = integer(metrics.get("matched_pairs"))
    target = max(
        1,
        integer(
            config.get("minimum_rollback_pairs"),
            80,
        ),
    )
    sample = min(20.0, 20.0 * matched / target)

    mean_delta = finite(metrics.get("mean_delta_r"))
    delta = max(
        0.0,
        min(25.0, 15.0 + mean_delta * 100.0),
    )

    ci_high = finite(metrics.get("bootstrap_ci_high_r"))
    ci = (
        20.0
        if ci_high >= 0
        else max(0.0, 20.0 + ci_high * 100.0)
    )

    drawdown_ratio = finite(
        metrics.get("drawdown_ratio"),
        1.0,
    )
    drawdown = max(
        0.0,
        min(
            15.0,
            15.0
            * (
                1.5 - min(drawdown_ratio, 1.5)
            )
            / 0.5,
        ),
    )

    master_pf = finite(
        metrics.get("master_profit_factor")
    )
    ex_pf = finite(
        metrics.get("ex_master_profit_factor")
    )
    pf_ratio = master_pf / max(ex_pf, 0.25)
    pf = max(
        0.0,
        min(10.0, (pf_ratio - 0.70) / 0.40 * 10.0),
    )

    liquidation_penalty = max(
        0,
        integer(metrics.get("master_liquidations"))
        - integer(metrics.get("ex_master_liquidations")),
    )
    liquidation = max(
        0.0,
        10.0 - 5.0 * liquidation_penalty,
    )

    return round(
        sample + delta + ci + drawdown + pf + liquidation,
        2,
    )


def decide_status(
    metrics: dict[str, Any],
    config: dict[str, Any],
    when: datetime,
) -> tuple[str, int, str, str]:
    matched = integer(metrics.get("matched_pairs"))
    mean_delta = finite(metrics.get("mean_delta_r"))
    total_delta = finite(metrics.get("total_delta_r"))
    ci_high = finite(metrics.get("bootstrap_ci_high_r"))
    drawdown_ratio = finite(
        metrics.get("drawdown_ratio"),
        1.0,
    )
    master_liq = integer(
        metrics.get("master_liquidations")
    )
    ex_liq = integer(
        metrics.get("ex_master_liquidations")
    )
    extra_liq = master_liq - ex_liq
    master_pf = finite(
        metrics.get("master_profit_factor")
    )
    ex_pf = finite(
        metrics.get("ex_master_profit_factor")
    )
    pf_ratio = master_pf / max(ex_pf, 0.25)
    deadline = parse_time(
        metrics.get("rollback_deadline_utc")
    )
    window_open = (
        deadline == datetime.min.replace(tzinfo=timezone.utc)
        or when <= deadline
    )

    if (
        truthy(
            config.get(
                "critical_on_two_extra_liquidations"
            )
        )
        and extra_liq >= 2
    ) or drawdown_ratio >= finite(
        config.get("critical_drawdown_ratio"),
        2.0,
    ):
        status = "CRITICAL"
        severity = 5
        reason = (
            "Critical post-promotion risk deterioration."
        )
        recommendation = (
            "Immediate human review; execute explicit Block 7 "
            "rollback if still inside the rollback window."
        )
    elif matched >= integer(
        config.get("minimum_rollback_pairs"),
        80,
    ) and (
        ci_high < 0
        or mean_delta
        <= finite(
            config.get("rollback_mean_delta_r"),
            -0.08,
        )
        or total_delta
        <= finite(
            config.get("rollback_total_delta_r"),
            -6.0,
        )
        or drawdown_ratio
        >= finite(
            config.get("rollback_drawdown_ratio"),
            1.50,
        )
        or pf_ratio
        <= finite(
            config.get("rollback_profit_factor_ratio"),
            0.80,
        )
        or (
            truthy(
                config.get(
                    "risk_recommend_on_extra_liquidation"
                )
            )
            and extra_liq > 0
        )
    ):
        status = "ROLLBACK_RECOMMENDED"
        severity = 4
        reason = (
            "Robust or material deterioration versus retained "
            "EX_MASTER."
        )
        recommendation = (
            "Human rollback review required; no automatic action."
        )
    elif matched < integer(
        config.get("minimum_monitoring_pairs"),
        20,
    ):
        status = "WAITING_SAMPLE"
        severity = 0
        reason = (
            "Insufficient matched post-promotion pairs."
        )
        recommendation = (
            "Continue Paper monitoring."
        )
    elif matched < integer(
        config.get("minimum_health_pairs"),
        50,
    ):
        status = "MONITORING"
        severity = 1
        reason = (
            "Initial post-promotion sample is still maturing."
        )
        recommendation = (
            "Continue Paper monitoring."
        )
    elif (
        mean_delta
        <= finite(
            config.get("watch_mean_delta_r"),
            -0.03,
        )
        or drawdown_ratio
        >= finite(
            config.get("watch_drawdown_ratio"),
            1.20,
        )
        or pf_ratio
        <= finite(
            config.get("watch_profit_factor_ratio"),
            0.90,
        )
        or extra_liq > 0
        or integer(metrics.get("positive_folds"))
        < integer(
            config.get(
                "minimum_positive_folds_for_health",
                2,
            )
        )
    ):
        status = "WATCH"
        severity = 2
        reason = (
            "Early deterioration or unstable post-promotion "
            "performance."
        )
        recommendation = (
            "Do not mutate or promote this family until resolved."
        )
    else:
        status = "HEALTHY"
        severity = 0
        reason = (
            "New MASTER remains healthy versus retained EX_MASTER."
        )
        recommendation = (
            "No action."
        )

    if (
        status in {
            "ROLLBACK_RECOMMENDED",
            "CRITICAL",
        }
        and not window_open
    ):
        return (
            "ROLLBACK_WINDOW_EXPIRED",
            5,
            (
                "Rollback was recommended, but the configured "
                "Block 7 transaction window has expired."
            ),
            (
                "Human governance decision required; standard "
                "transactional rollback is no longer available."
            ),
        )

    return status, severity, reason, recommendation


def evaluate_transaction(
    transaction: dict[str, Any],
    trade_rows: list[dict[str, Any]],
    config: dict[str, Any],
    when: datetime,
) -> dict[str, Any]:
    pairs, master_count, ex_count = paired_rows(
        trade_rows,
        transaction,
        config,
    )
    master_rows = [pair[0] for pair in pairs]
    ex_rows = [pair[1] for pair in pairs]
    master_r = [
        finite(row.get("r_multiple"))
        for row in master_rows
    ]
    ex_r = [
        finite(row.get("r_multiple"))
        for row in ex_rows
    ]
    deltas = [
        master - ex
        for master, ex in zip(master_r, ex_r)
    ]

    master_metrics = portfolio_metrics(master_rows)
    ex_metrics = portfolio_metrics(ex_rows)
    matched = len(pairs)
    folds = temporal_fold_means(
        deltas,
        integer(config.get("temporal_folds"), 4),
    )
    ci_low, ci_high = bootstrap_ci(
        deltas,
        str(transaction.get("transaction_id", "")),
        integer(
            config.get("bootstrap_iterations"),
            1000,
        ),
        finite(
            config.get("bootstrap_confidence"),
            0.95,
        ),
    )
    ex_drawdown = finite(
        ex_metrics.get("max_drawdown_r")
    )
    master_drawdown = finite(
        master_metrics.get("max_drawdown_r")
    )
    drawdown_ratio = (
        master_drawdown / ex_drawdown
        if ex_drawdown > 1e-12
        else (
            1.0
            if master_drawdown <= 1e-12
            else 99.0
        )
    )
    deadline = str(
        transaction.get("rollback_deadline_utc", "")
    )
    deadline_time = parse_time(deadline)
    window_open = (
        deadline_time
        == datetime.min.replace(tzinfo=timezone.utc)
        or when <= deadline_time
    )

    result = {
        "generated_utc": iso_utc(when),
        "transaction_id": str(
            transaction.get("transaction_id", "")
        ),
        "plan_id": str(transaction.get("plan_id", "")),
        "family_id": str(
            transaction.get("family_id", "")
        ),
        "master_candidate_id": str(
            transaction.get("candidate_id", "")
        ),
        "master_portfolio": str(
            transaction.get("candidate_portfolio", "")
        ),
        "ex_master_id": str(
            transaction.get("parent_id", "")
        ),
        "ex_master_portfolio": str(
            transaction.get("parent_portfolio", "")
        ),
        "executed_utc": str(
            transaction.get("executed_utc", "")
        ),
        "rollback_deadline_utc": deadline,
        "rollback_window_open": window_open,
        "master_closed_eligible": master_count,
        "ex_master_closed_eligible": ex_count,
        "matched_pairs": matched,
        "match_rate": (
            matched / max(master_count, ex_count, 1)
        ),
        "distinct_assets": len(
            {
                str(row.get("asset", ""))
                for row in master_rows
                if row.get("asset")
            }
        ),
        "mean_delta_r": (
            statistics.mean(deltas)
            if deltas
            else 0.0
        ),
        "median_delta_r": (
            statistics.median(deltas)
            if deltas
            else 0.0
        ),
        "trimmed_mean_delta_r": trimmed_mean(
            deltas,
            finite(config.get("trim_fraction"), 0.10),
        ),
        "total_delta_r": sum(deltas),
        "master_expectancy_r": master_metrics[
            "expectancy_r"
        ],
        "ex_master_expectancy_r": ex_metrics[
            "expectancy_r"
        ],
        "master_profit_factor": master_metrics[
            "profit_factor"
        ],
        "ex_master_profit_factor": ex_metrics[
            "profit_factor"
        ],
        "master_win_rate": master_metrics[
            "win_rate"
        ],
        "ex_master_win_rate": ex_metrics[
            "win_rate"
        ],
        "master_max_drawdown_r": master_drawdown,
        "ex_master_max_drawdown_r": ex_drawdown,
        "drawdown_ratio": drawdown_ratio,
        "master_liquidations": master_metrics[
            "liquidations"
        ],
        "ex_master_liquidations": ex_metrics[
            "liquidations"
        ],
        "bootstrap_ci_low_r": ci_low,
        "bootstrap_ci_high_r": ci_high,
        "positive_folds": sum(
            value > 0
            for value in folds
        ),
        "fold_means_r": folds,
        "latest_fold_mean_r": (
            folds[-1]
            if folds
            else 0.0
        ),
        "top5_positive_dependency": (
            top_positive_dependency(deltas)
        ),
        "automatic_rollback": False,
        "promotion_state_modified": False,
        "master_state_modified": False,
        "ex_master_state_modified": False,
        "live_modified": False,
        "orders_sent": False,
    }
    result["health_score"] = health_score(
        result,
        config,
    )
    (
        result["status"],
        result["severity"],
        result["reason"],
        result["recommendation"],
    ) = decide_status(result, config, when)
    return result


def recommendation_payload(
    rows: list[dict[str, Any]],
    when: datetime,
) -> dict[str, Any]:
    actionable = [
        row
        for row in rows
        if row.get("status")
        in {
            "ROLLBACK_RECOMMENDED",
            "CRITICAL",
            "ROLLBACK_WINDOW_EXPIRED",
        }
    ]
    return {
        "schema_version": SCHEMA_VERSION,
        "engine_version": ENGINE_VERSION,
        "generated_utc": iso_utc(when),
        "paper_only": True,
        "human_review_required": True,
        "explicit_block7_rollback_required": True,
        "automatic_rollbacks": 0,
        "automatic_promotions": 0,
        "automatic_retirements": 0,
        "live_modified": False,
        "orders_sent": False,
        "recommendation_count": len(actionable),
        "recommendations": actionable,
    }


def render_report(
    rows: list[dict[str, Any]],
    when: datetime,
) -> str:
    lines = [
        "# Blocco 8 — Sorveglianza post-promozione",
        "",
        f"Generato: {iso_utc(when)}",
        "",
        "> Paper-only. Il nuovo MASTER viene confrontato con "
        "l’EX_MASTER sugli stessi eventi successivi alla "
        "promozione. Nessun rollback automatico.",
        "",
        "## Stato",
        "",
        f"- Promozioni attive monitorate: **{len(rows)}**",
        f"- Rollback raccomandati: **{sum(row.get('status') == 'ROLLBACK_RECOMMENDED' for row in rows)}**",
        f"- Critici: **{sum(row.get('status') == 'CRITICAL' for row in rows)}**",
        "- Rollback automatici: **0**",
        "",
        "## Confronto MASTER / EX_MASTER",
        "",
        "| Famiglia | MASTER | EX_MASTER | Stato | Coppie | Δ medio R | CI alto | PF M | PF EX | DD ratio | Liq M/EX | Score |",
        "| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in rows:
        lines.append(
            f"| {row.get('family_id')} | "
            f"{row.get('master_portfolio')} | "
            f"{row.get('ex_master_portfolio')} | "
            f"{row.get('status')} | "
            f"{row.get('matched_pairs')} | "
            f"{finite(row.get('mean_delta_r')):.3f} | "
            f"{finite(row.get('bootstrap_ci_high_r')):.3f} | "
            f"{finite(row.get('master_profit_factor')):.2f} | "
            f"{finite(row.get('ex_master_profit_factor')):.2f} | "
            f"{finite(row.get('drawdown_ratio')):.2f} | "
            f"{row.get('master_liquidations')}/"
            f"{row.get('ex_master_liquidations')} | "
            f"{finite(row.get('health_score')):.1f} |"
        )
    if not rows:
        lines.append(
            "| — | — | — | Nessuna promozione attiva | 0 | "
            "0 | 0 | 0 | 0 | 0 | 0/0 | 0 |"
        )
    lines.extend(
        [
            "",
            "## Sicurezza",
            "",
            "- Solo trade chiusi dopo l’esecuzione della promozione.",
            "- Solo coppie con lo stesso `experiment_group_id`, asset e lato.",
            "- Solo dati `FULL_FROM_ENTRY` con risk model `block4_5_v1`.",
            "- `ROLLBACK_RECOMMENDED` non esegue nulla: richiede il comando umano del Blocco 7.",
            "- MASTER, EX_MASTER, stato promozione e live non vengono modificati.",
            "",
        ]
    )
    text = "\n".join(lines)
    atomic_write_text(REPORT_PATH, text)
    return text


def run_post_promotion_watchdog_cycle(
    when: datetime | None = None,
) -> dict[str, Any]:
    current = when or now_utc()
    config = load_config()

    if not truthy(config.get("enabled", True)):
        return {
            "enabled": False,
            "status": "DISABLED",
            "active_promotions": 0,
            "monitored": 0,
            "healthy": 0,
            "watch": 0,
            "rollback_recommended": 0,
            "critical": 0,
            "automatic_rollbacks": 0,
            "report_markdown": "",
        }

    promotion_state = load_json(
        PROMOTION_STATE_PATH,
        {"active_by_family": {}},
    )
    transactions = active_transactions(
        promotion_state
        if isinstance(promotion_state, dict)
        else {}
    )
    trade_rows = read_csv(TRADE_LOG_PATH)

    rows = [
        evaluate_transaction(
            transaction,
            trade_rows,
            config,
            current,
        )
        for transaction in transactions
    ]

    COMPARISONS_PATH.parent.mkdir(
        parents=True,
        exist_ok=True,
    )
    with COMPARISONS_PATH.open(
        "w",
        encoding="utf-8",
        newline="",
    ) as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=COMPARISON_FIELDS,
            extrasaction="ignore",
        )
        writer.writeheader()
        for row in rows:
            writer.writerow(
                {
                    field: row.get(field, "")
                    for field in COMPARISON_FIELDS
                }
            )

    state = load_state()
    tracked = state.setdefault("transactions", {})
    history_rows = []

    for row in rows:
        transaction_id = str(
            row.get("transaction_id", "")
        )
        previous = str(
            tracked.get(transaction_id, {}).get(
                "status",
                "",
            )
        )
        current_status = str(row.get("status", ""))
        if previous != current_status:
            history_rows.append(
                {
                    "generated_utc": iso_utc(current),
                    "transaction_id": transaction_id,
                    "family_id": row.get("family_id"),
                    "master_portfolio": row.get(
                        "master_portfolio"
                    ),
                    "ex_master_portfolio": row.get(
                        "ex_master_portfolio"
                    ),
                    "previous_status": (
                        previous or "NEW"
                    ),
                    "current_status": current_status,
                    "severity": row.get("severity"),
                    "health_score": row.get(
                        "health_score"
                    ),
                    "matched_pairs": row.get(
                        "matched_pairs"
                    ),
                    "mean_delta_r": row.get(
                        "mean_delta_r"
                    ),
                    "bootstrap_ci_high_r": row.get(
                        "bootstrap_ci_high_r"
                    ),
                    "drawdown_ratio": row.get(
                        "drawdown_ratio"
                    ),
                    "master_liquidations": row.get(
                        "master_liquidations"
                    ),
                    "ex_master_liquidations": row.get(
                        "ex_master_liquidations"
                    ),
                    "reason": row.get("reason"),
                }
            )
        tracked[transaction_id] = {
            "status": current_status,
            "updated_utc": iso_utc(current),
            "severity": row.get("severity"),
            "health_score": row.get("health_score"),
            "matched_pairs": row.get("matched_pairs"),
        }

    append_csv(
        HISTORY_PATH,
        HISTORY_FIELDS,
        history_rows,
    )

    recommendations = recommendation_payload(
        rows,
        current,
    )
    atomic_write_json(
        ROLLBACK_RECOMMENDATIONS_PATH,
        recommendations,
    )

    state["updated_utc"] = iso_utc(current)
    totals = state.setdefault("totals", {})
    totals["cycles"] = integer(totals.get("cycles")) + 1
    totals["monitored"] = len(rows)
    totals["rollback_recommended"] = sum(
        row.get("status")
        == "ROLLBACK_RECOMMENDED"
        for row in rows
    )
    totals["critical"] = sum(
        row.get("status") == "CRITICAL"
        for row in rows
    )
    totals["automatic_rollbacks"] = 0
    atomic_write_json(STATE_PATH, state)

    report = render_report(rows, current)

    return {
        "enabled": True,
        "status": "OK",
        "engine_version": ENGINE_VERSION,
        "active_promotions": len(transactions),
        "monitored": len(rows),
        "waiting_sample": sum(
            row.get("status") == "WAITING_SAMPLE"
            for row in rows
        ),
        "monitoring": sum(
            row.get("status") == "MONITORING"
            for row in rows
        ),
        "healthy": sum(
            row.get("status") == "HEALTHY"
            for row in rows
        ),
        "watch": sum(
            row.get("status") == "WATCH"
            for row in rows
        ),
        "rollback_recommended": sum(
            row.get("status")
            == "ROLLBACK_RECOMMENDED"
            for row in rows
        ),
        "critical": sum(
            row.get("status") == "CRITICAL"
            for row in rows
        ),
        "rollback_window_expired": sum(
            row.get("status")
            == "ROLLBACK_WINDOW_EXPIRED"
            for row in rows
        ),
        "recommendation_count": recommendations[
            "recommendation_count"
        ],
        "automatic_rollbacks": 0,
        "automatic_promotions": 0,
        "automatic_retirements": 0,
        "promotion_state_modified": False,
        "master_state_modified": False,
        "ex_master_state_modified": False,
        "live_modified": False,
        "orders_sent": False,
        "report_markdown": report,
    }
