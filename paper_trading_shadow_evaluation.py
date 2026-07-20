# -*- coding: utf-8 -*-
"""Block 4 statistical evaluation and robustness engine for Shadow Exit results.

This module is observational and Paper-only. It reads completed counterfactual
results produced by Block 3 and determines whether an exit rule has enough
evidence to be considered:

- INSUFFICIENT_DATA
- EARLY_SIGNAL
- VALIDATING
- ROBUST
- ELIGIBLE_FOR_MUTATION
- UNDERPERFORMING

It never changes a Paper strategy, position, exit, risk rule or live setting.
Only FULL_FROM_ENTRY Block 3 samples are used as primary evidence. Partial
samples remain visible in coverage counts but cannot support a mutation
candidate.
"""

from __future__ import annotations

import csv
import hashlib
import json
import math
import random
import statistics
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable


REPORTS_DIR = Path("reports")
RESULTS_PATH = REPORTS_DIR / "paper_trading_shadow_exit_results.csv"

STATE_PATH = REPORTS_DIR / "paper_trading_shadow_evaluation_state.json"
EVALUATIONS_PATH = REPORTS_DIR / "paper_trading_shadow_evaluations.csv"
HISTORY_PATH = REPORTS_DIR / "paper_trading_shadow_evaluation_history.csv"
CANDIDATES_PATH = REPORTS_DIR / "paper_trading_shadow_evaluation_candidates.json"
REPORT_PATH = REPORTS_DIR / "paper_trading_shadow_evaluation_report.md"
CONFIG_SNAPSHOT_PATH = REPORTS_DIR / "paper_trading_shadow_evaluation_config_snapshot.json"
CONFIG_PATH = Path("config/shadow_evaluation_block4.json")

ENGINE_VERSION = "block4-shadow-evaluation-v1"
SCHEMA_VERSION = 1

EVALUATION_FIELDS = [
    "generated_utc",
    "schema_version",
    "engine_version",
    "scope",
    "scope_value",
    "portfolio",
    "strategy",
    "asset",
    "scenario_set_version",
    "scenario_id",
    "scenario_kind",
    "scenario_parameters_json",
    "sample_total",
    "sample_full_from_entry",
    "sample_partial",
    "sample_eligible",
    "sample_excluded_quality",
    "sample_ambiguous",
    "sample_with_gaps",
    "ambiguity_pct",
    "gap_pct",
    "average_actual_pnl_eur",
    "average_shadow_pnl_eur",
    "average_delta_eur",
    "median_delta_eur",
    "trimmed_mean_delta_eur",
    "total_delta_eur",
    "average_delta_r",
    "median_delta_r",
    "trimmed_mean_delta_r",
    "total_delta_r",
    "delta_r_stddev",
    "worst_delta_r",
    "best_delta_r",
    "improved_count",
    "worsened_count",
    "equal_count",
    "improved_pct",
    "actual_win_rate_pct",
    "shadow_win_rate_pct",
    "win_rate_lift_pct_points",
    "actual_profit_factor",
    "shadow_profit_factor",
    "profit_factor_lift",
    "bootstrap_ci_low_delta_r",
    "bootstrap_ci_high_delta_r",
    "temporal_fold_count",
    "positive_temporal_folds",
    "last_temporal_fold_delta_r",
    "temporal_fold_means_json",
    "top_positive_5pct_contribution_pct",
    "recent_half_average_delta_r",
    "evidence_score",
    "direction",
    "status",
    "eligible_for_mutation",
    "blockers_json",
    "decision_summary",
]

HISTORY_FIELDS = [
    "generated_utc",
    "evaluation_key",
    "scope",
    "scope_value",
    "scenario_id",
    "previous_status",
    "current_status",
    "previous_eligible",
    "current_eligible",
    "sample_eligible",
    "average_delta_r",
    "median_delta_r",
    "bootstrap_ci_low_delta_r",
    "improved_pct",
    "evidence_score",
    "decision_summary",
]

DEFAULT_CONFIG: dict[str, Any] = {
    "schema_version": 1,
    "enabled": True,
    "primary_evidence": "FULL_FROM_ENTRY_ONLY",
    "comparison_tolerance_eur": 0.01,
    "minimum_initial_risk_eur": 0.01,
    "trim_fraction": 0.10,
    "bootstrap_iterations": 1000,
    "bootstrap_confidence": 0.95,
    "bootstrap_seed": 4004,
    "temporal_folds": 4,
    "top_outlier_fraction": 0.05,
    "scopes": ["ALL", "PORTFOLIO", "STRATEGY", "ASSET"],
    "candidate_scopes": ["STRATEGY", "PORTFOLIO"],
    "thresholds": {
        "early_signal_min_samples": 30,
        "validating_min_samples": 50,
        "robust_min_samples": 100,
        "mutation_min_samples": 120,
        "minimum_average_delta_r": 0.03,
        "minimum_median_delta_r": 0.00,
        "minimum_trimmed_mean_delta_r": 0.02,
        "minimum_total_delta_r": 3.0,
        "minimum_improved_pct": 55.0,
        "minimum_positive_temporal_folds": 3,
        "require_last_temporal_fold_positive": True,
        "minimum_bootstrap_ci_low_delta_r": 0.0,
        "maximum_ambiguity_pct": 10.0,
        "maximum_gap_pct": 10.0,
        "maximum_top_positive_5pct_contribution_pct": 50.0,
        "minimum_evidence_score_for_robust": 70.0,
        "minimum_evidence_score_for_mutation": 78.0,
    },
}


def now_utc() -> datetime:
    return datetime.now(timezone.utc)


def iso_utc(value: datetime | None = None) -> str:
    return (value or now_utc()).astimezone(timezone.utc).isoformat(
        timespec="seconds"
    )


def finite_float(value: Any, default: float = 0.0) -> float:
    try:
        number = float(value)
    except (TypeError, ValueError):
        return default
    return number if math.isfinite(number) else default


def finite_optional(value: Any) -> float | None:
    if value in (None, ""):
        return None
    try:
        number = float(value)
    except (TypeError, ValueError):
        return None
    return number if math.isfinite(number) else None


def truthy(value: Any) -> bool:
    return str(value).strip().lower() in {"1", "true", "yes", "y"}


def atomic_write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(text, encoding="utf-8")
    temporary.replace(path)


def atomic_write_json(path: Path, payload: Any) -> None:
    atomic_write_text(
        path,
        json.dumps(
            payload,
            ensure_ascii=False,
            indent=2,
            sort_keys=True,
        )
        + "\n",
    )


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists() or path.stat().st_size == 0:
        return []
    try:
        with path.open(
            "r",
            encoding="utf-8-sig",
            newline="",
        ) as handle:
            return list(csv.DictReader(handle))
    except Exception:
        return []


def write_csv(
    path: Path,
    fields: list[str],
    rows: Iterable[dict[str, Any]],
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    with temporary.open(
        "w",
        encoding="utf-8",
        newline="",
    ) as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=fields,
            extrasaction="ignore",
        )
        writer.writeheader()
        for row in rows:
            writer.writerow(
                {field: row.get(field, "") for field in fields}
            )
    temporary.replace(path)


def deep_merge(
    base: dict[str, Any],
    custom: dict[str, Any],
) -> dict[str, Any]:
    output = json.loads(json.dumps(base))
    for key, value in custom.items():
        if (
            isinstance(value, dict)
            and isinstance(output.get(key), dict)
        ):
            output[key] = deep_merge(output[key], value)
        else:
            output[key] = value
    return output


def load_config() -> dict[str, Any]:
    config = json.loads(json.dumps(DEFAULT_CONFIG))
    if CONFIG_PATH.exists():
        try:
            custom = json.loads(
                CONFIG_PATH.read_text(encoding="utf-8")
            )
            if isinstance(custom, dict):
                config = deep_merge(config, custom)
        except Exception as exc:
            print(
                "Configurazione Block 4 non valida, uso default: "
                f"{exc}"
            )

    scopes = []
    for value in config.get("scopes", []):
        scope = str(value).strip().upper()
        if scope in {"ALL", "PORTFOLIO", "STRATEGY", "ASSET"}:
            if scope not in scopes:
                scopes.append(scope)
    config["scopes"] = scopes or list(DEFAULT_CONFIG["scopes"])

    candidates = []
    for value in config.get("candidate_scopes", []):
        scope = str(value).strip().upper()
        if scope in config["scopes"] and scope != "ALL":
            if scope not in candidates:
                candidates.append(scope)
    config["candidate_scopes"] = (
        candidates
        or list(DEFAULT_CONFIG["candidate_scopes"])
    )

    atomic_write_json(CONFIG_SNAPSHOT_PATH, config)
    return config


def load_state() -> dict[str, Any]:
    if not STATE_PATH.exists():
        return {
            "schema_version": SCHEMA_VERSION,
            "engine_version": ENGINE_VERSION,
            "created_utc": iso_utc(),
            "updated_utc": iso_utc(),
            "evaluations": {},
        }
    try:
        value = json.loads(
            STATE_PATH.read_text(encoding="utf-8")
        )
        if not isinstance(value, dict):
            raise ValueError("state root is not object")
    except Exception:
        return {
            "schema_version": SCHEMA_VERSION,
            "engine_version": ENGINE_VERSION,
            "created_utc": iso_utc(),
            "updated_utc": iso_utc(),
            "evaluations": {},
        }
    value.setdefault("evaluations", {})
    value["schema_version"] = SCHEMA_VERSION
    value["engine_version"] = ENGINE_VERSION
    return value


def stable_seed(base: int, key: str) -> int:
    digest = hashlib.sha256(key.encode("utf-8")).hexdigest()
    return int(base) + int(digest[:8], 16)


def percentile(values: list[float], probability: float) -> float:
    if not values:
        return 0.0
    ordered = sorted(values)
    if len(ordered) == 1:
        return ordered[0]
    position = min(max(probability, 0.0), 1.0) * (
        len(ordered) - 1
    )
    lower = math.floor(position)
    upper = math.ceil(position)
    if lower == upper:
        return ordered[lower]
    fraction = position - lower
    return (
        ordered[lower] * (1.0 - fraction)
        + ordered[upper] * fraction
    )


def bootstrap_mean_interval(
    values: list[float],
    *,
    iterations: int,
    confidence: float,
    seed: int,
) -> tuple[float, float]:
    if not values:
        return 0.0, 0.0
    if len(values) == 1 or iterations <= 0:
        return values[0], values[0]

    generator = random.Random(seed)
    size = len(values)
    means = []
    for _ in range(iterations):
        sample = [
            values[generator.randrange(size)]
            for _ in range(size)
        ]
        means.append(statistics.fmean(sample))

    alpha = max(0.0, min(1.0, 1.0 - confidence))
    return (
        percentile(means, alpha / 2.0),
        percentile(means, 1.0 - alpha / 2.0),
    )


def trimmed_mean(
    values: list[float],
    fraction: float,
) -> float:
    if not values:
        return 0.0
    ordered = sorted(values)
    trim = int(len(ordered) * max(0.0, min(fraction, 0.40)))
    if trim <= 0 or len(ordered) - 2 * trim <= 0:
        return statistics.fmean(ordered)
    return statistics.fmean(ordered[trim:-trim])


def profit_factor(values: list[float]) -> float:
    gains = sum(value for value in values if value > 0)
    losses = abs(sum(value for value in values if value < 0))
    if losses > 0:
        return gains / losses
    return math.inf if gains > 0 else 0.0


def sortable_time(row: dict[str, Any]) -> str:
    return str(
        row.get("actual_closed_at")
        or row.get("shadow_closed_at")
        or row.get("opened_at")
        or ""
    )


def temporal_fold_means(
    rows: list[dict[str, Any]],
    folds: int,
) -> list[float]:
    if not rows:
        return []
    ordered = sorted(rows, key=sortable_time)
    count = max(1, min(int(folds), len(ordered)))
    output: list[float] = []
    for index in range(count):
        start = math.floor(index * len(ordered) / count)
        end = math.floor((index + 1) * len(ordered) / count)
        subset = ordered[start:end]
        values = [finite_float(row.get("_delta_r")) for row in subset]
        output.append(
            statistics.fmean(values) if values else 0.0
        )
    return output


def top_positive_contribution_pct(
    values: list[float],
    fraction: float,
) -> float:
    positive = sorted(
        (value for value in values if value > 0),
        reverse=True,
    )
    total = sum(positive)
    if total <= 0 or not positive:
        return 0.0
    count = max(
        1,
        math.ceil(
            len(positive)
            * max(0.0, min(float(fraction), 1.0))
        ),
    )
    return sum(positive[:count]) / total * 100.0


def eligible_result_row(
    row: dict[str, Any],
    config: dict[str, Any],
) -> tuple[bool, str]:
    if not truthy(row.get("full_from_entry")):
        return False, "PARTIAL_FROM_ENTRY"
    if not str(row.get("result_quality", "")).startswith("FULL"):
        return False, "NOT_FULL_QUALITY"
    risk = finite_optional(row.get("initial_risk_eur"))
    minimum = finite_float(
        config.get("minimum_initial_risk_eur"),
        0.01,
    )
    if risk is None or risk < minimum:
        return False, "INVALID_INITIAL_RISK"
    delta = finite_optional(row.get("delta_vs_actual_eur"))
    actual = finite_optional(
        row.get("actual_comparable_pnl_eur")
    )
    shadow = finite_optional(
        row.get("shadow_comparable_pnl_eur")
    )
    if delta is None or actual is None or shadow is None:
        return False, "MISSING_COMPARABLE_PNL"
    return True, ""


def prepare_rows(
    raw_rows: list[dict[str, Any]],
    config: dict[str, Any],
) -> list[dict[str, Any]]:
    output = []
    for raw in raw_rows:
        row = dict(raw)
        eligible, reason = eligible_result_row(row, config)
        row["_eligible"] = eligible
        row["_exclusion_reason"] = reason

        risk = max(
            finite_float(row.get("initial_risk_eur"), 0.0),
            1e-12,
        )
        row["_delta_r"] = (
            finite_float(row.get("delta_vs_actual_eur")) / risk
        )
        row["_actual_r"] = (
            finite_float(
                row.get("actual_comparable_pnl_eur")
            )
            / risk
        )
        row["_shadow_r"] = (
            finite_float(
                row.get("shadow_comparable_pnl_eur")
            )
            / risk
        )
        output.append(row)
    return output


def scope_identity(
    scope: str,
    row: dict[str, Any],
) -> tuple[str, str, str, str]:
    if scope == "ALL":
        return "ALL", "ALL", "", ""
    if scope == "PORTFOLIO":
        value = str(row.get("portfolio", "")).strip() or "UNKNOWN"
        return value, value, str(row.get("strategy", "")), str(row.get("asset", ""))
    if scope == "STRATEGY":
        value = str(row.get("strategy", "")).strip() or str(
            row.get("portfolio", "")
        ).strip() or "UNKNOWN"
        return value, str(row.get("portfolio", "")), value, str(row.get("asset", ""))
    if scope == "ASSET":
        value = str(row.get("asset", "")).strip() or "UNKNOWN"
        return value, str(row.get("portfolio", "")), str(row.get("strategy", "")), value
    raise ValueError(f"Scope non supportato: {scope}")


def group_rows(
    rows: list[dict[str, Any]],
    scopes: list[str],
) -> dict[tuple[str, str, str, str], list[dict[str, Any]]]:
    groups: dict[
        tuple[str, str, str, str],
        list[dict[str, Any]],
    ] = defaultdict(list)
    for row in rows:
        scenario_set = str(
            row.get("scenario_set_version", "")
        )
        scenario_id = str(row.get("scenario_id", ""))
        if not scenario_id:
            continue
        for scope in scopes:
            value, _, _, _ = scope_identity(scope, row)
            groups[
                (scope, value, scenario_set, scenario_id)
            ].append(row)
    return groups


def threshold(
    config: dict[str, Any],
    name: str,
    default: float,
) -> float:
    return finite_float(
        config.get("thresholds", {}).get(name),
        default,
    )


def evidence_score(
    *,
    sample: int,
    average_delta_r: float,
    median_delta_r: float,
    improved_pct: float,
    ci_low: float,
    positive_folds: int,
    fold_count: int,
    ambiguity_pct: float,
    gap_pct: float,
    outlier_pct: float,
    config: dict[str, Any],
) -> float:
    robust_min = max(
        threshold(config, "robust_min_samples", 100.0),
        1.0,
    )
    sample_score = min(sample / robust_min, 1.0) * 20.0

    mean_target = max(
        threshold(config, "minimum_average_delta_r", 0.03),
        1e-9,
    )
    effect_score = min(
        max(average_delta_r, 0.0) / mean_target,
        1.5,
    ) / 1.5 * 15.0

    median_target = max(
        threshold(config, "minimum_trimmed_mean_delta_r", 0.02),
        1e-9,
    )
    median_score = min(
        max(median_delta_r, 0.0) / median_target,
        1.5,
    ) / 1.5 * 10.0

    improvement_score = min(
        max(improved_pct - 50.0, 0.0) / 15.0,
        1.0,
    ) * 15.0

    ci_score = (
        15.0
        if ci_low > 0
        else max(0.0, 15.0 * (1.0 + ci_low / 0.10))
    )

    temporal_score = (
        positive_folds / fold_count * 15.0
        if fold_count
        else 0.0
    )

    quality_penalty = min(
        ambiguity_pct + gap_pct,
        20.0,
    ) / 20.0
    quality_score = (1.0 - quality_penalty) * 5.0

    concentration_limit = max(
        threshold(
            config,
            "maximum_top_positive_5pct_contribution_pct",
            50.0,
        ),
        1.0,
    )
    concentration_score = max(
        0.0,
        1.0 - outlier_pct / concentration_limit,
    ) * 5.0

    return round(
        max(
            0.0,
            min(
                100.0,
                sample_score
                + effect_score
                + median_score
                + improvement_score
                + ci_score
                + temporal_score
                + quality_score
                + concentration_score,
            ),
        ),
        2,
    )


def decision(
    *,
    sample: int,
    average_delta_r: float,
    median_delta_r: float,
    trimmed_delta_r: float,
    total_delta_r: float,
    improved_pct: float,
    ci_low: float,
    ci_high: float,
    positive_folds: int,
    fold_count: int,
    last_fold: float,
    ambiguity_pct: float,
    gap_pct: float,
    outlier_pct: float,
    score: float,
    config: dict[str, Any],
) -> tuple[str, bool, list[str], str, str]:
    early = int(
        threshold(config, "early_signal_min_samples", 30)
    )
    validating = int(
        threshold(config, "validating_min_samples", 50)
    )
    robust = int(
        threshold(config, "robust_min_samples", 100)
    )
    mutation = int(
        threshold(config, "mutation_min_samples", 120)
    )

    direction = (
        "IMPROVING"
        if average_delta_r > 0
        else "HARMFUL"
        if average_delta_r < 0
        else "NEUTRAL"
    )

    if sample < early:
        return (
            "INSUFFICIENT_DATA",
            False,
            ["SAMPLE_BELOW_EARLY_THRESHOLD"],
            direction,
            f"{sample}/{early} campioni completi richiesti per il primo segnale.",
        )

    if sample < validating:
        return (
            "EARLY_SIGNAL",
            False,
            [],
            direction,
            "Segnale preliminare: non utilizzabile per mutazioni.",
        )

    if sample < robust:
        return (
            "VALIDATING",
            False,
            [],
            direction,
            "Campione in validazione; serve maggiore profondità temporale.",
        )

    blockers: list[str] = []

    checks = [
        (
            average_delta_r
            >= threshold(config, "minimum_average_delta_r", 0.03),
            "AVERAGE_DELTA_R_TOO_LOW",
        ),
        (
            median_delta_r
            > threshold(config, "minimum_median_delta_r", 0.0),
            "MEDIAN_DELTA_R_NOT_POSITIVE",
        ),
        (
            trimmed_delta_r
            >= threshold(
                config,
                "minimum_trimmed_mean_delta_r",
                0.02,
            ),
            "TRIMMED_MEAN_DELTA_R_TOO_LOW",
        ),
        (
            total_delta_r
            >= threshold(config, "minimum_total_delta_r", 3.0),
            "TOTAL_DELTA_R_TOO_LOW",
        ),
        (
            improved_pct
            >= threshold(config, "minimum_improved_pct", 55.0),
            "IMPROVEMENT_RATE_TOO_LOW",
        ),
        (
            ci_low
            > threshold(
                config,
                "minimum_bootstrap_ci_low_delta_r",
                0.0,
            ),
            "BOOTSTRAP_CI_NOT_POSITIVE",
        ),
        (
            positive_folds
            >= int(
                threshold(
                    config,
                    "minimum_positive_temporal_folds",
                    3,
                )
            ),
            "TEMPORAL_STABILITY_TOO_LOW",
        ),
        (
            not bool(
                config.get("thresholds", {}).get(
                    "require_last_temporal_fold_positive",
                    True,
                )
            )
            or last_fold > 0,
            "LATEST_TEMPORAL_FOLD_NOT_POSITIVE",
        ),
        (
            ambiguity_pct
            <= threshold(
                config,
                "maximum_ambiguity_pct",
                10.0,
            ),
            "AMBIGUITY_RATE_TOO_HIGH",
        ),
        (
            gap_pct
            <= threshold(config, "maximum_gap_pct", 10.0),
            "CANDLE_GAP_RATE_TOO_HIGH",
        ),
        (
            outlier_pct
            <= threshold(
                config,
                "maximum_top_positive_5pct_contribution_pct",
                50.0,
            ),
            "OUTLIER_CONCENTRATION_TOO_HIGH",
        ),
        (
            score
            >= threshold(
                config,
                "minimum_evidence_score_for_robust",
                70.0,
            ),
            "EVIDENCE_SCORE_TOO_LOW",
        ),
    ]

    blockers.extend(
        code for passed, code in checks if not passed
    )

    if not blockers:
        mutation_blockers = []
        if sample < mutation:
            mutation_blockers.append(
                "SAMPLE_BELOW_MUTATION_THRESHOLD"
            )
        if score < threshold(
            config,
            "minimum_evidence_score_for_mutation",
            78.0,
        ):
            mutation_blockers.append(
                "MUTATION_EVIDENCE_SCORE_TOO_LOW"
            )

        if not mutation_blockers:
            return (
                "ELIGIBLE_FOR_MUTATION",
                True,
                [],
                direction,
                "Evidenza robusta: candidatura disponibile al Blocco 5.",
            )
        return (
            "ROBUST",
            False,
            mutation_blockers,
            direction,
            "Evidenza robusta, ma non ancora sufficiente per una mutazione.",
        )

    if average_delta_r < 0 and ci_high < 0:
        return (
            "UNDERPERFORMING",
            False,
            blockers,
            direction,
            "La variante risulta stabilmente peggiore dell'uscita originale.",
        )

    return (
        "VALIDATING",
        False,
        blockers,
        direction,
        "Campione ampio ma i controlli di robustezza non sono ancora tutti superati.",
    )


def evaluation_key(row: dict[str, Any]) -> str:
    return "|".join(
        [
            str(row.get("scope", "")),
            str(row.get("scope_value", "")),
            str(row.get("scenario_set_version", "")),
            str(row.get("scenario_id", "")),
        ]
    )


def evaluate_group(
    key: tuple[str, str, str, str],
    rows: list[dict[str, Any]],
    config: dict[str, Any],
    generated: str,
) -> dict[str, Any]:
    scope, scope_value, scenario_set, scenario_id = key
    total = len(rows)
    eligible = [row for row in rows if row.get("_eligible")]
    partial = sum(
        not truthy(row.get("full_from_entry")) for row in rows
    )
    excluded = total - len(eligible) - partial
    ambiguous = sum(
        finite_float(
            row.get("same_candle_ambiguity_count")
        )
        > 0
        for row in eligible
    )
    gaps = sum(
        finite_float(row.get("candle_gap_count")) > 0
        for row in eligible
    )

    delta_eur = [
        finite_float(row.get("delta_vs_actual_eur"))
        for row in eligible
    ]
    delta_r = [
        finite_float(row.get("_delta_r"))
        for row in eligible
    ]
    actual = [
        finite_float(
            row.get("actual_comparable_pnl_eur")
        )
        for row in eligible
    ]
    shadow = [
        finite_float(
            row.get("shadow_comparable_pnl_eur")
        )
        for row in eligible
    ]

    tolerance = max(
        finite_float(
            config.get("comparison_tolerance_eur"),
            0.01,
        ),
        0.0,
    )
    improved = sum(value > tolerance for value in delta_eur)
    worsened = sum(value < -tolerance for value in delta_eur)
    equal = len(delta_eur) - improved - worsened

    trim_fraction = finite_float(
        config.get("trim_fraction"),
        0.10,
    )
    average_delta = (
        statistics.fmean(delta_eur) if delta_eur else 0.0
    )
    median_delta = (
        statistics.median(delta_eur) if delta_eur else 0.0
    )
    trimmed_delta = trimmed_mean(delta_eur, trim_fraction)

    average_delta_r = (
        statistics.fmean(delta_r) if delta_r else 0.0
    )
    median_delta_r = (
        statistics.median(delta_r) if delta_r else 0.0
    )
    trimmed_delta_r = trimmed_mean(
        delta_r,
        trim_fraction,
    )

    seed = stable_seed(
        int(finite_float(config.get("bootstrap_seed"), 4004)),
        "|".join(key),
    )
    ci_low, ci_high = bootstrap_mean_interval(
        delta_r,
        iterations=max(
            int(
                finite_float(
                    config.get("bootstrap_iterations"),
                    1000,
                )
            ),
            0,
        ),
        confidence=max(
            0.50,
            min(
                finite_float(
                    config.get("bootstrap_confidence"),
                    0.95,
                ),
                0.999,
            ),
        ),
        seed=seed,
    )

    folds = temporal_fold_means(
        eligible,
        int(
            finite_float(
                config.get("temporal_folds"),
                4,
            )
        ),
    )
    positive_folds = sum(value > 0 for value in folds)
    last_fold = folds[-1] if folds else 0.0

    outlier_pct = top_positive_contribution_pct(
        delta_r,
        finite_float(
            config.get("top_outlier_fraction"),
            0.05,
        ),
    )
    ambiguity_pct = (
        ambiguous / len(eligible) * 100.0
        if eligible
        else 0.0
    )
    gap_pct = (
        gaps / len(eligible) * 100.0
        if eligible
        else 0.0
    )

    recent_half = (
        sorted(eligible, key=sortable_time)[
            len(eligible) // 2 :
        ]
        if eligible
        else []
    )
    recent_half_mean = (
        statistics.fmean(
            finite_float(row.get("_delta_r"))
            for row in recent_half
        )
        if recent_half
        else 0.0
    )

    improved_pct = (
        improved / len(eligible) * 100.0
        if eligible
        else 0.0
    )
    score = evidence_score(
        sample=len(eligible),
        average_delta_r=average_delta_r,
        median_delta_r=median_delta_r,
        improved_pct=improved_pct,
        ci_low=ci_low,
        positive_folds=positive_folds,
        fold_count=len(folds),
        ambiguity_pct=ambiguity_pct,
        gap_pct=gap_pct,
        outlier_pct=outlier_pct,
        config=config,
    )
    status, mutation_eligible, blockers, direction, summary = decision(
        sample=len(eligible),
        average_delta_r=average_delta_r,
        median_delta_r=median_delta_r,
        trimmed_delta_r=trimmed_delta_r,
        total_delta_r=sum(delta_r),
        improved_pct=improved_pct,
        ci_low=ci_low,
        ci_high=ci_high,
        positive_folds=positive_folds,
        fold_count=len(folds),
        last_fold=last_fold,
        ambiguity_pct=ambiguity_pct,
        gap_pct=gap_pct,
        outlier_pct=outlier_pct,
        score=score,
        config=config,
    )

    first = rows[0] if rows else {}
    _, portfolio, strategy, asset = scope_identity(
        scope,
        first,
    )

    actual_pf = profit_factor(actual)
    shadow_pf = profit_factor(shadow)
    pf_lift = (
        shadow_pf - actual_pf
        if math.isfinite(shadow_pf)
        and math.isfinite(actual_pf)
        else ""
    )

    return {
        "generated_utc": generated,
        "schema_version": SCHEMA_VERSION,
        "engine_version": ENGINE_VERSION,
        "scope": scope,
        "scope_value": scope_value,
        "portfolio": portfolio,
        "strategy": strategy,
        "asset": asset,
        "scenario_set_version": scenario_set,
        "scenario_id": scenario_id,
        "scenario_kind": str(
            first.get("scenario_kind", "")
        ),
        "scenario_parameters_json": str(
            first.get("scenario_parameters_json", "")
        ),
        "sample_total": total,
        "sample_full_from_entry": sum(
            truthy(row.get("full_from_entry")) for row in rows
        ),
        "sample_partial": partial,
        "sample_eligible": len(eligible),
        "sample_excluded_quality": excluded,
        "sample_ambiguous": ambiguous,
        "sample_with_gaps": gaps,
        "ambiguity_pct": ambiguity_pct,
        "gap_pct": gap_pct,
        "average_actual_pnl_eur": (
            statistics.fmean(actual) if actual else 0.0
        ),
        "average_shadow_pnl_eur": (
            statistics.fmean(shadow) if shadow else 0.0
        ),
        "average_delta_eur": average_delta,
        "median_delta_eur": median_delta,
        "trimmed_mean_delta_eur": trimmed_delta,
        "total_delta_eur": sum(delta_eur),
        "average_delta_r": average_delta_r,
        "median_delta_r": median_delta_r,
        "trimmed_mean_delta_r": trimmed_delta_r,
        "total_delta_r": sum(delta_r),
        "delta_r_stddev": (
            statistics.pstdev(delta_r)
            if len(delta_r) > 1
            else 0.0
        ),
        "worst_delta_r": min(delta_r) if delta_r else 0.0,
        "best_delta_r": max(delta_r) if delta_r else 0.0,
        "improved_count": improved,
        "worsened_count": worsened,
        "equal_count": equal,
        "improved_pct": improved_pct,
        "actual_win_rate_pct": (
            sum(value > 0 for value in actual)
            / len(actual)
            * 100.0
            if actual
            else 0.0
        ),
        "shadow_win_rate_pct": (
            sum(value > 0 for value in shadow)
            / len(shadow)
            * 100.0
            if shadow
            else 0.0
        ),
        "win_rate_lift_pct_points": (
            (
                sum(value > 0 for value in shadow)
                / len(shadow)
                * 100.0
            )
            - (
                sum(value > 0 for value in actual)
                / len(actual)
                * 100.0
            )
            if actual and shadow
            else 0.0
        ),
        "actual_profit_factor": (
            "inf" if math.isinf(actual_pf) else actual_pf
        ),
        "shadow_profit_factor": (
            "inf" if math.isinf(shadow_pf) else shadow_pf
        ),
        "profit_factor_lift": pf_lift,
        "bootstrap_ci_low_delta_r": ci_low,
        "bootstrap_ci_high_delta_r": ci_high,
        "temporal_fold_count": len(folds),
        "positive_temporal_folds": positive_folds,
        "last_temporal_fold_delta_r": last_fold,
        "temporal_fold_means_json": json.dumps(
            folds,
            separators=(",", ":"),
        ),
        "top_positive_5pct_contribution_pct": outlier_pct,
        "recent_half_average_delta_r": recent_half_mean,
        "evidence_score": score,
        "direction": direction,
        "status": status,
        "eligible_for_mutation": mutation_eligible,
        "blockers_json": json.dumps(
            blockers,
            separators=(",", ":"),
        ),
        "decision_summary": summary,
    }


def build_evaluations(
    rows: list[dict[str, Any]],
    config: dict[str, Any],
    when: datetime,
) -> list[dict[str, Any]]:
    prepared = prepare_rows(rows, config)
    grouped = group_rows(
        prepared,
        list(config.get("scopes", [])),
    )
    generated = iso_utc(when)
    evaluations = [
        evaluate_group(key, group, config, generated)
        for key, group in sorted(grouped.items())
    ]
    return sorted(
        evaluations,
        key=lambda row: (
            str(row.get("scope", "")),
            str(row.get("scope_value", "")),
            str(row.get("scenario_id", "")),
        ),
    )


def append_history(
    evaluations: list[dict[str, Any]],
    state: dict[str, Any],
    when: datetime,
) -> int:
    existing = read_csv(HISTORY_PATH)
    previous = state.setdefault("evaluations", {})
    new_rows: list[dict[str, Any]] = []

    for row in evaluations:
        key = evaluation_key(row)
        old = previous.get(key, {})
        old_status = str(old.get("status", ""))
        old_eligible = bool(old.get("eligible_for_mutation", False))
        current_status = str(row.get("status", ""))
        current_eligible = bool(row.get("eligible_for_mutation"))

        if (
            old_status != current_status
            or old_eligible != current_eligible
        ):
            new_rows.append(
                {
                    "generated_utc": iso_utc(when),
                    "evaluation_key": key,
                    "scope": row.get("scope", ""),
                    "scope_value": row.get("scope_value", ""),
                    "scenario_id": row.get("scenario_id", ""),
                    "previous_status": old_status,
                    "current_status": current_status,
                    "previous_eligible": old_eligible,
                    "current_eligible": current_eligible,
                    "sample_eligible": row.get("sample_eligible", 0),
                    "average_delta_r": row.get("average_delta_r", 0.0),
                    "median_delta_r": row.get("median_delta_r", 0.0),
                    "bootstrap_ci_low_delta_r": row.get(
                        "bootstrap_ci_low_delta_r",
                        0.0,
                    ),
                    "improved_pct": row.get("improved_pct", 0.0),
                    "evidence_score": row.get("evidence_score", 0.0),
                    "decision_summary": row.get(
                        "decision_summary",
                        "",
                    ),
                }
            )

        previous[key] = {
            "status": current_status,
            "eligible_for_mutation": current_eligible,
            "sample_eligible": int(
                finite_float(row.get("sample_eligible"))
            ),
            "evidence_score": finite_float(
                row.get("evidence_score")
            ),
            "updated_utc": iso_utc(when),
        }

    if new_rows:
        write_csv(
            HISTORY_PATH,
            HISTORY_FIELDS,
            [*existing, *new_rows],
        )
    elif not HISTORY_PATH.exists():
        write_csv(HISTORY_PATH, HISTORY_FIELDS, [])

    return len(new_rows)


def candidate_payload(
    evaluations: list[dict[str, Any]],
    config: dict[str, Any],
    when: datetime,
) -> dict[str, Any]:
    candidate_scopes = set(
        str(value).upper()
        for value in config.get("candidate_scopes", [])
    )
    candidates = [
        row
        for row in evaluations
        if bool(row.get("eligible_for_mutation"))
        and str(row.get("scope", "")).upper()
        in candidate_scopes
    ]
    candidates.sort(
        key=lambda row: (
            finite_float(row.get("evidence_score")),
            int(finite_float(row.get("sample_eligible"))),
            finite_float(row.get("average_delta_r")),
        ),
        reverse=True,
    )
    return {
        "schema_version": SCHEMA_VERSION,
        "engine_version": ENGINE_VERSION,
        "generated_utc": iso_utc(when),
        "automatic_mutations_created": 0,
        "automatic_promotions": 0,
        "paper_positions_modified": False,
        "paper_exits_modified": False,
        "live_modified": False,
        "candidate_count": len(candidates),
        "candidates": [
            {
                "rank": index,
                "scope": row["scope"],
                "scope_value": row["scope_value"],
                "portfolio": row["portfolio"],
                "strategy": row["strategy"],
                "asset": row["asset"],
                "scenario_set_version": row[
                    "scenario_set_version"
                ],
                "scenario_id": row["scenario_id"],
                "scenario_kind": row["scenario_kind"],
                "scenario_parameters_json": row[
                    "scenario_parameters_json"
                ],
                "sample_eligible": row["sample_eligible"],
                "average_delta_r": row["average_delta_r"],
                "median_delta_r": row["median_delta_r"],
                "bootstrap_ci_low_delta_r": row[
                    "bootstrap_ci_low_delta_r"
                ],
                "improved_pct": row["improved_pct"],
                "evidence_score": row["evidence_score"],
                "status": row["status"],
                "decision_summary": row["decision_summary"],
            }
            for index, row in enumerate(candidates, start=1)
        ],
    }


def fmt_number(value: Any, digits: int = 2) -> str:
    return f"{finite_float(value):.{digits}f}".replace(".", ",")


def render_report(
    evaluations: list[dict[str, Any]],
    candidates: dict[str, Any],
    raw_result_count: int,
    when: datetime,
) -> str:
    all_scope = [
        row for row in evaluations if row.get("scope") == "ALL"
    ]
    ranked = sorted(
        all_scope,
        key=lambda row: (
            finite_float(row.get("evidence_score")),
            int(finite_float(row.get("sample_eligible"))),
            finite_float(row.get("average_delta_r")),
        ),
        reverse=True,
    )
    status_counts: dict[str, int] = defaultdict(int)
    for row in evaluations:
        status_counts[str(row.get("status", ""))] += 1

    lines = [
        "# Blocco 4 — Valutazione statistica Shadow",
        "",
        f"Generato: {iso_utc(when)}",
        "",
        "> Modulo esclusivamente valutativo. Non modifica strategie, "
        "uscite, posizioni o capitale. Le candidature vengono consegnate "
        "al futuro Blocco 5, senza applicazione automatica.",
        "",
        "## Stato",
        "",
        f"- Risultati Block 3 disponibili: **{raw_result_count}**",
        f"- Valutazioni prodotte: **{len(evaluations)}**",
        f"- Candidature al Blocco 5: **{candidates['candidate_count']}**",
        f"- Mutazioni create automaticamente: **0**",
        "",
        "## Classifica complessiva",
        "",
        "| Scenario | Campione pieno | Δ medio (R) | Mediana (R) | CI bootstrap basso | Migliora | Score | Stato |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    if not ranked:
        lines.append(
            "| — | 0 | — | — | — | — | — | INSUFFICIENT_DATA |"
        )
    else:
        for row in ranked[:20]:
            lines.append(
                "| {scenario} | {sample} | {mean} | {median} | "
                "{ci} | {improved}% | {score} | {status} |".format(
                    scenario=row["scenario_id"],
                    sample=row["sample_eligible"],
                    mean=fmt_number(row["average_delta_r"], 3),
                    median=fmt_number(row["median_delta_r"], 3),
                    ci=fmt_number(
                        row["bootstrap_ci_low_delta_r"],
                        3,
                    ),
                    improved=fmt_number(row["improved_pct"], 1),
                    score=fmt_number(row["evidence_score"], 1),
                    status=row["status"],
                )
            )

    lines.extend(
        [
            "",
            "## Stati di evidenza",
            "",
            "- **INSUFFICIENT_DATA**: meno di 30 trade completi.",
            "- **EARLY_SIGNAL**: da 30 a 49 trade completi.",
            "- **VALIDATING**: campione maggiore, ma robustezza non ancora dimostrata.",
            "- **ROBUST**: test di effetto, stabilità, qualità e outlier superati.",
            "- **ELIGIBLE_FOR_MUTATION**: evidenza sufficiente per proporre una variante al Blocco 5.",
            "- **UNDERPERFORMING**: intervallo statistico stabilmente negativo.",
            "",
            "## Protezioni statistiche",
            "",
            "Sono utilizzati solo trade osservati integralmente dall'entrata. "
            "Il controllo comprende media e mediana normalizzate per rischio, "
            "media tagliata, bootstrap deterministico, quattro segmenti temporali, "
            "concentrazione dei migliori outlier, ambiguità intrabar e gap di candele.",
            "",
        ]
    )
    atomic_write_text(REPORT_PATH, "\n".join(lines))
    return "\n".join(lines)


def run_shadow_evaluation_cycle(
    when: datetime | None = None,
) -> dict[str, Any]:
    current = when or now_utc()
    config = load_config()
    if not config.get("enabled", True):
        return {
            "enabled": False,
            "status": "DISABLED",
            "report_markdown": "",
            "paper_positions_modified": False,
            "paper_exits_modified": False,
            "orders_sent": False,
        }

    raw_rows = read_csv(RESULTS_PATH)
    evaluations = build_evaluations(
        raw_rows,
        config,
        current,
    )
    write_csv(
        EVALUATIONS_PATH,
        EVALUATION_FIELDS,
        evaluations,
    )

    state = load_state()
    history_events = append_history(
        evaluations,
        state,
        current,
    )
    state["updated_utc"] = iso_utc(current)
    atomic_write_json(STATE_PATH, state)

    candidates = candidate_payload(
        evaluations,
        config,
        current,
    )
    atomic_write_json(CANDIDATES_PATH, candidates)

    report_markdown = render_report(
        evaluations,
        candidates,
        len(raw_rows),
        current,
    )

    robust_count = sum(
        row.get("status") in {
            "ROBUST",
            "ELIGIBLE_FOR_MUTATION",
        }
        for row in evaluations
    )
    underperforming_count = sum(
        row.get("status") == "UNDERPERFORMING"
        for row in evaluations
    )

    return {
        "enabled": True,
        "status": "OK",
        "engine_version": ENGINE_VERSION,
        "raw_results": len(raw_rows),
        "evaluation_rows": len(evaluations),
        "history_events": history_events,
        "robust_count": robust_count,
        "eligible_for_mutation": candidates["candidate_count"],
        "underperforming_count": underperforming_count,
        "report_path": str(REPORT_PATH),
        "report_markdown": report_markdown,
        "paper_positions_modified": False,
        "paper_exits_modified": False,
        "mutations_created": 0,
        "promotions_executed": 0,
        "orders_sent": False,
    }
