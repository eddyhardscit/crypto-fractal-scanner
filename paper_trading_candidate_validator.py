# -*- coding: utf-8 -*-
"""Block 6 Champion/Challenger candidate validation.

Paper-only evaluation layer.

For every active Block 5 candidate, this module compares the candidate with
its parent on the exact same market events using ``experiment_group_id``.
Only closed, post-candidate, risk-model-consistent trades are eligible.

The module can mark a candidate as:
- INCUBATING
- VALIDATING
- EARLY_OUTPERFORMER
- PROMOTION_REVIEW_READY
- UNDERPERFORMING
- RISK_REJECTED

It never promotes, retires, disables, modifies or replaces a strategy.
A later block and explicit policy are required for promotion.
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
CONFIG_PATH = Path("config/evolution_validation_block6.json")

CANDIDATE_STATE_PATH = (
    REPORTS_DIR / "paper_trading_evolution_candidate_state.json"
)
CANDIDATE_REGISTRY_PATH = (
    REPORTS_DIR / "paper_trading_evolution_candidate_registry.json"
)
TRADE_LOG_PATH = REPORTS_DIR / "paper_trading_trade_log.csv"

STATE_PATH = (
    REPORTS_DIR
    / "paper_trading_evolution_candidate_validation_state.json"
)
EVALUATIONS_PATH = (
    REPORTS_DIR
    / "paper_trading_evolution_candidate_validations.csv"
)
HISTORY_PATH = (
    REPORTS_DIR
    / "paper_trading_evolution_candidate_validation_history.csv"
)
PROMOTION_REVIEW_PATH = (
    REPORTS_DIR
    / "paper_trading_evolution_promotion_review.json"
)
REPORT_PATH = (
    REPORTS_DIR
    / "paper_trading_evolution_candidate_validation_report.md"
)
CONFIG_SNAPSHOT_PATH = (
    REPORTS_DIR
    / "paper_trading_evolution_candidate_validation_config_snapshot.json"
)

SCHEMA_VERSION = 1
ENGINE_VERSION = "block6-champion-challenger-v1"

EVALUATION_FIELDS = [
    "generated_utc",
    "candidate_id",
    "candidate_portfolio",
    "parent_portfolio",
    "mutation_parameter",
    "mutation_old_value",
    "mutation_new_value",
    "status",
    "validation_score",
    "candidate_closed_eligible",
    "parent_closed_eligible",
    "matched_pairs",
    "match_rate",
    "distinct_assets",
    "mean_delta_r",
    "median_delta_r",
    "trimmed_mean_delta_r",
    "total_delta_r",
    "improved_fraction",
    "bootstrap_ci_low_r",
    "bootstrap_ci_high_r",
    "positive_folds",
    "latest_fold_mean_r",
    "top5_positive_dependency",
    "candidate_expectancy_r",
    "parent_expectancy_r",
    "candidate_profit_factor",
    "parent_profit_factor",
    "candidate_win_rate",
    "parent_win_rate",
    "candidate_max_drawdown_r",
    "parent_max_drawdown_r",
    "candidate_liquidations",
    "parent_liquidations",
    "risk_model_consistent",
    "full_from_entry_pairs",
    "decision_summary",
]

HISTORY_FIELDS = [
    "generated_utc",
    "candidate_id",
    "candidate_portfolio",
    "parent_portfolio",
    "previous_status",
    "current_status",
    "validation_score",
    "matched_pairs",
    "mean_delta_r",
    "bootstrap_ci_low_r",
    "reason",
]

DEFAULT_CONFIG: dict[str, Any] = {
    "schema_version": 1,
    "enabled": True,
    "paper_only": True,
    "automatic_promotion": False,
    "automatic_retirement": False,
    "modify_candidate_state": False,
    "modify_parent_state": False,
    "required_risk_model_version": "block4_5_v1",
    "require_full_from_entry": True,
    "minimum_incubation_pairs": 30,
    "minimum_early_outperformer_pairs": 80,
    "minimum_promotion_review_pairs": 150,
    "minimum_match_rate": 0.80,
    "minimum_distinct_assets": 2,
    "minimum_mean_delta_r": 0.05,
    "minimum_median_delta_r": 0.0,
    "minimum_trimmed_mean_delta_r": 0.03,
    "minimum_total_delta_r": 6.0,
    "minimum_improved_fraction": 0.55,
    "minimum_positive_folds": 3,
    "require_latest_fold_positive": True,
    "maximum_top5_positive_dependency": 0.50,
    "minimum_candidate_profit_factor": 1.10,
    "minimum_profit_factor_ratio": 1.03,
    "maximum_drawdown_ratio": 1.10,
    "maximum_drawdown_extra_r": 0.50,
    "minimum_validation_score": 80.0,
    "underperformance_minimum_pairs": 80,
    "underperformance_mean_delta_r": -0.05,
    "risk_reject_on_extra_liquidation": True,
    "bootstrap_iterations": 1000,
    "bootstrap_confidence": 0.95,
    "temporal_folds": 4,
    "trim_fraction": 0.10,
    "maximum_registry_validation_rows": 50,
}


def now_utc() -> datetime:
    return datetime.now(timezone.utc)


def iso_utc(value: datetime | None = None) -> str:
    return (value or now_utc()).astimezone(timezone.utc).isoformat(
        timespec="seconds"
    )


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
    parsed = datetime.fromisoformat(text.replace("Z", "+00:00"))
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
            output[key] = deep_merge(output[key], value)
        else:
            output[key] = copy.deepcopy(value)
    return output


def load_json(path: Path, default: Any) -> Any:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
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
                {field: row.get(field, "") for field in fields}
            )


def load_config() -> dict[str, Any]:
    config = copy.deepcopy(DEFAULT_CONFIG)
    custom = load_json(CONFIG_PATH, {})
    if isinstance(custom, dict):
        config = deep_merge(config, custom)
    config["bootstrap_iterations"] = max(
        200,
        integer(config.get("bootstrap_iterations"), 1000),
    )
    config["temporal_folds"] = max(
        2,
        integer(config.get("temporal_folds"), 4),
    )
    atomic_write_json(CONFIG_SNAPSHOT_PATH, config)
    return config


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


def empty_state() -> dict[str, Any]:
    return {
        "schema_version": SCHEMA_VERSION,
        "engine_version": ENGINE_VERSION,
        "created_utc": iso_utc(),
        "updated_utc": iso_utc(),
        "candidate_statuses": {},
        "totals": {
            "evaluated_cycles": 0,
            "promotion_review_ready": 0,
            "automatic_promotions": 0,
            "automatic_retirements": 0,
        },
    }


def load_state() -> dict[str, Any]:
    value = load_json(STATE_PATH, empty_state())
    if not isinstance(value, dict):
        value = empty_state()
    value.setdefault("candidate_statuses", {})
    value.setdefault("totals", empty_state()["totals"])
    value["schema_version"] = SCHEMA_VERSION
    value["engine_version"] = ENGINE_VERSION
    return value


def eligible_trade(
    row: dict[str, Any],
    created_at: datetime,
    config: dict[str, Any],
) -> bool:
    if parse_time(row.get("closed_at")) < created_at:
        return False
    required_risk = str(
        config.get("required_risk_model_version", "")
    )
    if required_risk and str(
        row.get("risk_model_version_at_exit", "")
    ) != required_risk:
        return False
    if truthy(config.get("require_full_from_entry")):
        if str(row.get("excursion_quality", "")).upper() != (
            "FULL_FROM_ENTRY"
        ):
            return False
    return bool(str(row.get("experiment_group_id", "")).strip())


def trade_index(
    rows: list[dict[str, Any]],
    portfolio: str,
    created_at: datetime,
    config: dict[str, Any],
) -> dict[str, dict[str, Any]]:
    selected = [
        row
        for row in rows
        if str(row.get("portfolio", "")) == portfolio
        and eligible_trade(row, created_at, config)
    ]
    selected.sort(
        key=lambda row: (
            parse_time(row.get("closed_at")),
            str(row.get("trade_id", "")),
        )
    )
    output: dict[str, dict[str, Any]] = {}
    for row in selected:
        group_id = str(row.get("experiment_group_id", ""))
        output.setdefault(group_id, row)
    return output


def paired_rows(
    trade_rows: list[dict[str, Any]],
    candidate: dict[str, Any],
    config: dict[str, Any],
) -> tuple[
    list[tuple[dict[str, Any], dict[str, Any]]],
    int,
    int,
]:
    created_at = parse_time(candidate.get("created_at"))
    candidate_index = trade_index(
        trade_rows,
        str(candidate.get("portfolio_name", "")),
        created_at,
        config,
    )
    parent_index = trade_index(
        trade_rows,
        str(candidate.get("parent_portfolio", "")),
        created_at,
        config,
    )
    common = sorted(
        set(candidate_index) & set(parent_index),
        key=lambda key: parse_time(
            candidate_index[key].get("closed_at")
        ),
    )
    pairs = [
        (candidate_index[key], parent_index[key])
        for key in common
        if str(candidate_index[key].get("asset", ""))
        == str(parent_index[key].get("asset", ""))
        and str(candidate_index[key].get("side", ""))
        == str(parent_index[key].get("side", ""))
    ]
    return pairs, len(candidate_index), len(parent_index)


def trimmed_mean(
    values: list[float],
    fraction: float,
) -> float:
    if not values:
        return 0.0
    ordered = sorted(values)
    trim = int(len(ordered) * max(0.0, min(0.40, fraction)))
    if trim * 2 >= len(ordered):
        return statistics.mean(ordered)
    return statistics.mean(ordered[trim:len(ordered) - trim])


def profit_factor(values: list[float]) -> float:
    gains = sum(value for value in values if value > 0)
    losses = abs(sum(value for value in values if value < 0))
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


def liquidation_count(rows: list[dict[str, Any]]) -> int:
    return sum(
        str(row.get("close_reason", "")).upper().startswith(
            "LIQUIDATION"
        )
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
    candidate_id: str,
    iterations: int,
    confidence: float,
) -> tuple[float, float]:
    if not values:
        return 0.0, 0.0
    if len(values) == 1:
        return values[0], values[0]
    seed_raw = (
        candidate_id
        + "|"
        + hashlib.sha256(
            json.dumps(values).encode("utf-8")
        ).hexdigest()
    )
    seed = int(
        hashlib.sha256(seed_raw.encode("utf-8")).hexdigest()[:16],
        16,
    )
    rng = random.Random(seed)
    means = []
    count = len(values)
    for _ in range(iterations):
        sample = [
            values[rng.randrange(count)]
            for _ in range(count)
        ]
        means.append(statistics.mean(sample))
    alpha = (1.0 - max(0.50, min(0.999, confidence))) / 2.0
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
        end = round(len(values) * (fold + 1) / folds)
        chunk = values[start:end]
        if chunk:
            output.append(statistics.mean(chunk))
    return output


def top_positive_dependency(values: list[float]) -> float:
    positives = sorted(
        [value for value in values if value > 0],
        reverse=True,
    )
    total = sum(positives)
    if total <= 1e-12:
        return 1.0
    count = max(1, math.ceil(len(values) * 0.05))
    return sum(positives[:count]) / total


def portfolio_metrics(
    rows: list[dict[str, Any]],
) -> dict[str, Any]:
    values = [finite(row.get("r_multiple")) for row in rows]
    return {
        "trades": len(rows),
        "expectancy_r": (
            statistics.mean(values) if values else 0.0
        ),
        "profit_factor": profit_factor(values),
        "win_rate": (
            sum(value > 0 for value in values) / len(values)
            if values
            else 0.0
        ),
        "max_drawdown_r": max_drawdown(values),
        "liquidations": liquidation_count(rows),
    }


def validation_score(
    metrics: dict[str, Any],
    config: dict[str, Any],
) -> float:
    matched = integer(metrics.get("matched_pairs"))
    promotion_pairs = max(
        1,
        integer(config.get("minimum_promotion_review_pairs"), 150),
    )
    sample_score = min(20.0, 20.0 * matched / promotion_pairs)

    mean_delta = finite(metrics.get("mean_delta_r"))
    delta_target = max(
        0.01,
        finite(config.get("minimum_mean_delta_r"), 0.05),
    )
    delta_score = max(
        0.0,
        min(20.0, 10.0 + 10.0 * mean_delta / delta_target),
    )

    ci_low = finite(metrics.get("bootstrap_ci_low_r"))
    ci_score = (
        20.0
        if ci_low > 0
        else 10.0
        if mean_delta > 0
        else 0.0
    )

    improved = finite(metrics.get("improved_fraction"))
    improved_score = max(
        0.0,
        min(10.0, (improved - 0.45) / 0.15 * 10.0),
    )

    positive_folds = integer(metrics.get("positive_folds"))
    fold_count = max(
        1,
        integer(config.get("temporal_folds"), 4),
    )
    fold_score = min(
        10.0,
        10.0 * positive_folds / fold_count,
    )

    candidate_pf = finite(metrics.get("candidate_profit_factor"))
    parent_pf = finite(metrics.get("parent_profit_factor"))
    pf_ratio = candidate_pf / max(parent_pf, 0.25)
    pf_score = max(
        0.0,
        min(10.0, (pf_ratio - 0.90) / 0.20 * 10.0),
    )

    candidate_dd = finite(metrics.get("candidate_max_drawdown_r"))
    parent_dd = finite(metrics.get("parent_max_drawdown_r"))
    drawdown_score = (
        10.0
        if candidate_dd <= parent_dd
        else max(
            0.0,
            10.0
            * (
                1.0
                - (candidate_dd - parent_dd)
                / max(parent_dd + 1.0, 1.0)
            ),
        )
    )

    return round(
        sample_score
        + delta_score
        + ci_score
        + improved_score
        + fold_score
        + pf_score
        + drawdown_score,
        2,
    )


def decide_status(
    metrics: dict[str, Any],
    config: dict[str, Any],
) -> tuple[str, str]:
    matched = integer(metrics.get("matched_pairs"))
    candidate_liq = integer(metrics.get("candidate_liquidations"))
    parent_liq = integer(metrics.get("parent_liquidations"))
    mean_delta = finite(metrics.get("mean_delta_r"))
    ci_low = finite(metrics.get("bootstrap_ci_low_r"))
    ci_high = finite(metrics.get("bootstrap_ci_high_r"))
    score = finite(metrics.get("validation_score"))

    if (
        truthy(config.get("risk_reject_on_extra_liquidation"))
        and matched >= integer(
            config.get("minimum_incubation_pairs"),
            30,
        )
        and candidate_liq > parent_liq
    ):
        return (
            "RISK_REJECTED",
            "Candidate has more liquidations than parent.",
        )

    if matched < integer(
        config.get("minimum_incubation_pairs"),
        30,
    ):
        return (
            "INCUBATING",
            "Insufficient matched post-creation pairs.",
        )

    under_minimum = integer(
        config.get("underperformance_minimum_pairs"),
        80,
    )
    if matched >= under_minimum and (
        ci_high < 0
        or (
            mean_delta
            <= finite(
                config.get(
                    "underperformance_mean_delta_r",
                    -0.05,
                )
            )
            and finite(
                metrics.get("candidate_profit_factor")
            )
            < finite(metrics.get("parent_profit_factor"))
        )
    ):
        return (
            "UNDERPERFORMING",
            "Robust or material underperformance versus parent.",
        )

    strict_checks = {
        "matched_pairs": matched
        >= integer(
            config.get("minimum_promotion_review_pairs"),
            150,
        ),
        "match_rate": finite(metrics.get("match_rate"))
        >= finite(config.get("minimum_match_rate"), 0.80),
        "distinct_assets": integer(metrics.get("distinct_assets"))
        >= integer(config.get("minimum_distinct_assets"), 2),
        "mean_delta": mean_delta
        >= finite(config.get("minimum_mean_delta_r"), 0.05),
        "median_delta": finite(metrics.get("median_delta_r"))
        > finite(config.get("minimum_median_delta_r"), 0.0),
        "trimmed_delta": finite(
            metrics.get("trimmed_mean_delta_r")
        )
        >= finite(
            config.get("minimum_trimmed_mean_delta_r"),
            0.03,
        ),
        "total_delta": finite(metrics.get("total_delta_r"))
        >= finite(config.get("minimum_total_delta_r"), 6.0),
        "improved_fraction": finite(
            metrics.get("improved_fraction")
        )
        >= finite(
            config.get("minimum_improved_fraction"),
            0.55,
        ),
        "bootstrap": ci_low > 0,
        "folds": integer(metrics.get("positive_folds"))
        >= integer(config.get("minimum_positive_folds"), 3),
        "latest_fold": (
            finite(metrics.get("latest_fold_mean_r")) > 0
            if truthy(
                config.get("require_latest_fold_positive")
            )
            else True
        ),
        "top5_dependency": finite(
            metrics.get("top5_positive_dependency"),
            1.0,
        )
        <= finite(
            config.get(
                "maximum_top5_positive_dependency",
                0.50,
            )
        ),
        "candidate_pf": finite(
            metrics.get("candidate_profit_factor")
        )
        >= finite(
            config.get("minimum_candidate_profit_factor"),
            1.10,
        ),
        "pf_ratio": finite(
            metrics.get("candidate_profit_factor")
        )
        >= finite(metrics.get("parent_profit_factor"))
        * finite(
            config.get("minimum_profit_factor_ratio"),
            1.03,
        ),
        "drawdown": finite(
            metrics.get("candidate_max_drawdown_r")
        )
        <= finite(metrics.get("parent_max_drawdown_r"))
        * finite(
            config.get("maximum_drawdown_ratio"),
            1.10,
        )
        + finite(
            config.get("maximum_drawdown_extra_r"),
            0.50,
        ),
        "liquidations": candidate_liq <= parent_liq,
        "score": score
        >= finite(config.get("minimum_validation_score"), 80.0),
        "risk_model": truthy(
            metrics.get("risk_model_consistent")
        ),
    }

    if all(strict_checks.values()):
        return (
            "PROMOTION_REVIEW_READY",
            "All Champion/Challenger review gates passed.",
        )

    early_pairs = integer(
        config.get("minimum_early_outperformer_pairs"),
        80,
    )
    if (
        matched >= early_pairs
        and mean_delta > 0
        and ci_low >= 0
        and finite(metrics.get("improved_fraction")) >= 0.52
        and integer(metrics.get("positive_folds")) >= 3
    ):
        return (
            "EARLY_OUTPERFORMER",
            "Positive early evidence; promotion sample not yet complete.",
        )

    return (
        "VALIDATING",
        "Candidate remains in controlled validation.",
    )


def evaluate_candidate(
    candidate: dict[str, Any],
    trade_rows: list[dict[str, Any]],
    config: dict[str, Any],
    when: datetime,
) -> dict[str, Any]:
    pairs, candidate_count, parent_count = paired_rows(
        trade_rows,
        candidate,
        config,
    )
    candidate_rows = [pair[0] for pair in pairs]
    parent_rows = [pair[1] for pair in pairs]
    candidate_r = [
        finite(row.get("r_multiple"))
        for row in candidate_rows
    ]
    parent_r = [
        finite(row.get("r_multiple"))
        for row in parent_rows
    ]
    deltas = [
        candidate_value - parent_value
        for candidate_value, parent_value in zip(
            candidate_r,
            parent_r,
        )
    ]

    candidate_metrics = portfolio_metrics(candidate_rows)
    parent_metrics = portfolio_metrics(parent_rows)
    matched = len(pairs)
    match_rate = (
        matched / max(candidate_count, parent_count, 1)
    )
    folds = temporal_fold_means(
        deltas,
        integer(config.get("temporal_folds"), 4),
    )
    ci_low, ci_high = bootstrap_ci(
        deltas,
        str(candidate.get("candidate_id", "")),
        integer(config.get("bootstrap_iterations"), 1000),
        finite(config.get("bootstrap_confidence"), 0.95),
    )
    mutation = candidate.get("mutation", {}) or {}

    risk_model = str(
        config.get("required_risk_model_version", "")
    )
    risk_consistent = all(
        str(row.get("risk_model_version_at_exit", ""))
        == risk_model
        for row in candidate_rows + parent_rows
    ) if pairs and risk_model else bool(pairs)

    result = {
        "generated_utc": iso_utc(when),
        "candidate_id": str(candidate.get("candidate_id", "")),
        "candidate_portfolio": str(
            candidate.get("portfolio_name", "")
        ),
        "parent_portfolio": str(
            candidate.get("parent_portfolio", "")
        ),
        "mutation_parameter": str(
            mutation.get("parameter", "")
        ),
        "mutation_old_value": mutation.get("old_value"),
        "mutation_new_value": mutation.get("new_value"),
        "candidate_closed_eligible": candidate_count,
        "parent_closed_eligible": parent_count,
        "matched_pairs": matched,
        "match_rate": match_rate,
        "distinct_assets": len(
            {
                str(row.get("asset", ""))
                for row in candidate_rows
                if row.get("asset")
            }
        ),
        "mean_delta_r": (
            statistics.mean(deltas) if deltas else 0.0
        ),
        "median_delta_r": (
            statistics.median(deltas) if deltas else 0.0
        ),
        "trimmed_mean_delta_r": trimmed_mean(
            deltas,
            finite(config.get("trim_fraction"), 0.10),
        ),
        "total_delta_r": sum(deltas),
        "improved_fraction": (
            sum(value > 0 for value in deltas) / matched
            if matched
            else 0.0
        ),
        "bootstrap_ci_low_r": ci_low,
        "bootstrap_ci_high_r": ci_high,
        "positive_folds": sum(value > 0 for value in folds),
        "fold_means_r": folds,
        "latest_fold_mean_r": folds[-1] if folds else 0.0,
        "top5_positive_dependency": top_positive_dependency(
            deltas
        ),
        "candidate_expectancy_r": candidate_metrics[
            "expectancy_r"
        ],
        "parent_expectancy_r": parent_metrics["expectancy_r"],
        "candidate_profit_factor": candidate_metrics[
            "profit_factor"
        ],
        "parent_profit_factor": parent_metrics["profit_factor"],
        "candidate_win_rate": candidate_metrics["win_rate"],
        "parent_win_rate": parent_metrics["win_rate"],
        "candidate_max_drawdown_r": candidate_metrics[
            "max_drawdown_r"
        ],
        "parent_max_drawdown_r": parent_metrics[
            "max_drawdown_r"
        ],
        "candidate_liquidations": candidate_metrics[
            "liquidations"
        ],
        "parent_liquidations": parent_metrics["liquidations"],
        "risk_model_consistent": risk_consistent,
        "full_from_entry_pairs": matched,
        "automatic_promotion": False,
        "automatic_retirement": False,
        "live_modified": False,
        "orders_sent": False,
    }
    result["validation_score"] = validation_score(
        result,
        config,
    )
    status, summary = decide_status(result, config)
    result["status"] = status
    result["decision_summary"] = summary
    return result


def validation_metadata(
    evaluation: dict[str, Any],
) -> dict[str, Any]:
    keys = [
        "generated_utc",
        "status",
        "validation_score",
        "matched_pairs",
        "match_rate",
        "distinct_assets",
        "mean_delta_r",
        "median_delta_r",
        "trimmed_mean_delta_r",
        "total_delta_r",
        "improved_fraction",
        "bootstrap_ci_low_r",
        "bootstrap_ci_high_r",
        "positive_folds",
        "latest_fold_mean_r",
        "candidate_expectancy_r",
        "parent_expectancy_r",
        "candidate_profit_factor",
        "parent_profit_factor",
        "candidate_max_drawdown_r",
        "parent_max_drawdown_r",
        "candidate_liquidations",
        "parent_liquidations",
        "decision_summary",
    ]
    return {
        key: evaluation.get(key)
        for key in keys
    } | {
        "human_approval_required": True,
        "automatic_promotion": False,
        "automatic_retirement": False,
    }


def enrich_candidate_registry(
    evaluations: list[dict[str, Any]],
    when: datetime,
) -> dict[str, Any]:
    registry = load_json(CANDIDATE_REGISTRY_PATH, {})
    if not isinstance(registry, dict):
        registry = {}
    by_id = {
        str(row.get("candidate_id", "")): row
        for row in evaluations
    }
    enriched = 0
    for row in registry.get("candidates", []):
        if not isinstance(row, dict):
            continue
        candidate_id = str(row.get("strategy_id", ""))
        evaluation = by_id.get(candidate_id)
        if evaluation is None:
            continue
        metadata = row.setdefault("metadata", {})
        if not isinstance(metadata, dict):
            metadata = {}
            row["metadata"] = metadata
        metadata["block6_validation"] = validation_metadata(
            evaluation
        )
        enriched += 1

    registry.update(
        {
            "block6_engine_version": ENGINE_VERSION,
            "block6_generated_utc": iso_utc(when),
            "block6_evaluated_candidates": len(evaluations),
            "block6_promotion_review_ready": sum(
                row.get("status")
                == "PROMOTION_REVIEW_READY"
                for row in evaluations
            ),
            "automatic_promotions": 0,
            "automatic_retirements": 0,
            "live_modified": False,
            "orders_sent": False,
        }
    )
    atomic_write_json(CANDIDATE_REGISTRY_PATH, registry)
    return {
        "registry_rows": len(
            registry.get("candidates", [])
        ),
        "enriched_rows": enriched,
    }


def render_report(
    evaluations: list[dict[str, Any]],
    when: datetime,
) -> str:
    lines = [
        "# Blocco 6 — Validazione Champion/Challenger",
        "",
        f"Generato: {iso_utc(when)}",
        "",
        "> Paper-only. Confronto sulle stesse entrate tramite "
        "`experiment_group_id`. Nessuna promozione, sostituzione, "
        "pensione o modifica live automatica.",
        "",
        "## Stato",
        "",
        f"- Candidati valutati: **{len(evaluations)}**",
        f"- Pronti per revisione promozione: **{sum(row.get('status') == 'PROMOTION_REVIEW_READY' for row in evaluations)}**",
        "- Promozioni automatiche: **0**",
        "- Pensionamenti automatici: **0**",
        "",
        "## Confronto",
        "",
        "| Candidato | Genitore | Stato | Coppie | Δ medio R | CI basso | PF cand. | PF gen. | DD cand. | DD gen. | Score |",
        "| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in evaluations:
        lines.append(
            f"| {row.get('candidate_portfolio')} | "
            f"{row.get('parent_portfolio')} | "
            f"{row.get('status')} | "
            f"{row.get('matched_pairs')} | "
            f"{finite(row.get('mean_delta_r')):.3f} | "
            f"{finite(row.get('bootstrap_ci_low_r')):.3f} | "
            f"{finite(row.get('candidate_profit_factor')):.2f} | "
            f"{finite(row.get('parent_profit_factor')):.2f} | "
            f"{finite(row.get('candidate_max_drawdown_r')):.2f} | "
            f"{finite(row.get('parent_max_drawdown_r')):.2f} | "
            f"{finite(row.get('validation_score')):.1f} |"
        )
    if not evaluations:
        lines.append(
            "| — | — | Nessun candidato attivo | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |"
        )
    lines.extend(
        [
            "",
            "## Gate di sicurezza",
            "",
            "- Solo trade chiusi dopo la creazione della candidata.",
            "- Solo coppie con lo stesso evento d’ingresso.",
            "- Solo dati `FULL_FROM_ENTRY` e risk model `block4_5_v1`.",
            "- Campione, bootstrap, stabilità temporale, dipendenza dai migliori trade, PF, drawdown e liquidazioni.",
            "- `PROMOTION_REVIEW_READY` è soltanto una raccomandazione: richiede approvazione umana e un blocco successivo.",
            "",
        ]
    )
    text = "\n".join(lines)
    atomic_write_text(REPORT_PATH, text)
    return text


def run_candidate_validation_cycle(
    when: datetime | None = None,
) -> dict[str, Any]:
    current = when or now_utc()
    config = load_config()
    if not truthy(config.get("enabled", True)):
        return {
            "enabled": False,
            "status": "DISABLED",
            "evaluated_candidates": 0,
            "promotion_review_ready": 0,
            "automatic_promotions": 0,
            "automatic_retirements": 0,
            "report_markdown": "",
        }

    candidate_state = load_json(CANDIDATE_STATE_PATH, {})
    candidates = [
        row
        for row in (
            candidate_state.get("candidates", {}).values()
            if isinstance(candidate_state, dict)
            else []
        )
        if isinstance(row, dict)
        and bool(row.get("active", True))
        and str(row.get("status", "CANDIDATE"))
        == "CANDIDATE"
    ]
    candidates.sort(
        key=lambda row: (
            str(row.get("created_at", "")),
            str(row.get("candidate_id", "")),
        )
    )
    trade_rows = read_csv(TRADE_LOG_PATH)
    evaluations = [
        evaluate_candidate(
            candidate,
            trade_rows,
            config,
            current,
        )
        for candidate in candidates
    ]

    state = load_state()
    history_rows = []
    statuses = state.setdefault("candidate_statuses", {})
    for evaluation in evaluations:
        candidate_id = evaluation["candidate_id"]
        previous = str(
            statuses.get(candidate_id, {}).get("status", "")
        )
        current_status = str(evaluation["status"])
        if previous != current_status:
            history_rows.append(
                {
                    "generated_utc": iso_utc(current),
                    "candidate_id": candidate_id,
                    "candidate_portfolio": evaluation[
                        "candidate_portfolio"
                    ],
                    "parent_portfolio": evaluation[
                        "parent_portfolio"
                    ],
                    "previous_status": previous or "NEW",
                    "current_status": current_status,
                    "validation_score": evaluation[
                        "validation_score"
                    ],
                    "matched_pairs": evaluation[
                        "matched_pairs"
                    ],
                    "mean_delta_r": evaluation[
                        "mean_delta_r"
                    ],
                    "bootstrap_ci_low_r": evaluation[
                        "bootstrap_ci_low_r"
                    ],
                    "reason": evaluation[
                        "decision_summary"
                    ],
                }
            )
        statuses[candidate_id] = {
            "status": current_status,
            "updated_utc": iso_utc(current),
            "validation_score": evaluation[
                "validation_score"
            ],
            "matched_pairs": evaluation["matched_pairs"],
        }

    append_csv(HISTORY_PATH, HISTORY_FIELDS, history_rows)

    # Current snapshot is replaced, not appended.
    EVALUATIONS_PATH.parent.mkdir(
        parents=True,
        exist_ok=True,
    )
    with EVALUATIONS_PATH.open(
        "w",
        encoding="utf-8",
        newline="",
    ) as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=EVALUATION_FIELDS,
            extrasaction="ignore",
        )
        writer.writeheader()
        for row in evaluations:
            writer.writerow(
                {
                    field: row.get(field, "")
                    for field in EVALUATION_FIELDS
                }
            )

    promotion_rows = [
        row
        for row in evaluations
        if row.get("status") == "PROMOTION_REVIEW_READY"
    ]
    promotion_payload = {
        "schema_version": SCHEMA_VERSION,
        "engine_version": ENGINE_VERSION,
        "generated_utc": iso_utc(current),
        "paper_only": True,
        "human_approval_required": True,
        "automatic_promotions": 0,
        "automatic_retirements": 0,
        "live_modified": False,
        "orders_sent": False,
        "candidate_count": len(promotion_rows),
        "candidates": promotion_rows,
    }
    atomic_write_json(
        PROMOTION_REVIEW_PATH,
        promotion_payload,
    )

    registry_result = enrich_candidate_registry(
        evaluations,
        current,
    )
    report = render_report(evaluations, current)

    state["updated_utc"] = iso_utc(current)
    totals = state.setdefault("totals", {})
    totals["evaluated_cycles"] = integer(
        totals.get("evaluated_cycles")
    ) + 1
    totals["promotion_review_ready"] = len(promotion_rows)
    totals["automatic_promotions"] = 0
    totals["automatic_retirements"] = 0
    atomic_write_json(STATE_PATH, state)

    status_counts: dict[str, int] = {}
    for row in evaluations:
        status = str(row.get("status", "UNKNOWN"))
        status_counts[status] = status_counts.get(status, 0) + 1

    return {
        "enabled": True,
        "status": "OK",
        "engine_version": ENGINE_VERSION,
        "evaluated_candidates": len(evaluations),
        "promotion_review_ready": len(promotion_rows),
        "status_counts": status_counts,
        "registry_enriched": registry_result[
            "enriched_rows"
        ],
        "automatic_promotions": 0,
        "automatic_retirements": 0,
        "candidate_state_modified": False,
        "parent_state_modified": False,
        "live_modified": False,
        "orders_sent": False,
        "report_markdown": report,
    }
