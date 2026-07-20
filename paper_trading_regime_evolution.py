# -*- coding: utf-8 -*-
"""Block 10 regime fitness and strategy-specialisation memory.

Paper-only and advisory by default. It maps closed Paper trades to the market
regime that was known at entry, builds per-regime fitness tables and exposes a
context decision to Block 5. It never switches an existing strategy, changes a
position, promotes, retires, rolls back, touches live or sends orders.
"""
from __future__ import annotations

import copy
import csv
import json
import math
import re
import statistics
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

REPORTS = Path("reports")
CONFIG_PATH = Path("config/evolution_regime_block10.json")
MARKET_LATEST = REPORTS / "market_regime_latest.json"
MARKET_HISTORY = REPORTS / "market_regime_history.csv"
TRADE_LOG = REPORTS / "paper_trading_trade_log.csv"
CANDIDATE_STATE = REPORTS / "paper_trading_evolution_candidate_state.json"
CANDIDATE_REGISTRY = REPORTS / "paper_trading_evolution_candidate_registry.json"
EVOLUTION_SCORES = REPORTS / "paper_trading_evolution_scores.csv"

STATE = REPORTS / "paper_trading_evolution_regime_state.json"
PERFORMANCE = REPORTS / "paper_trading_evolution_regime_performance.csv"
LEADERBOARD = REPORTS / "paper_trading_evolution_regime_leaderboard.json"
MEMORY = REPORTS / "paper_trading_evolution_regime_memory.json"
HISTORY = REPORTS / "paper_trading_evolution_regime_history.csv"
REPORT = REPORTS / "paper_trading_evolution_regime_report.md"
CONFIG_SNAPSHOT = REPORTS / "paper_trading_evolution_regime_config_snapshot.json"

SCHEMA_VERSION = 1
ENGINE_VERSION = "block10-regime-fitness-v1"
REGIMES = (
    "BULL_TREND",
    "BEAR_TREND",
    "RANGE",
    "HIGH_VOLATILITY",
    "CRASH",
    "RECOVERY",
    "UNKNOWN",
)

DEFAULT_CONFIG: dict[str, Any] = {
    "schema_version": 1,
    "enabled": True,
    "paper_only": True,
    "routing_mode": "ADVISORY_ONLY",
    "candidate_policy_enabled": True,
    "candidate_blocking_enabled": False,
    "automatic_strategy_switching": False,
    "automatic_position_changes": False,
    "automatic_mutation": False,
    "automatic_promotion": False,
    "automatic_retirement": False,
    "automatic_rollback": False,
    "live_side_effects_allowed": False,
    "orders_allowed": False,
    "minimum_observing_trades": 10,
    "minimum_compatible_trades": 30,
    "minimum_specialist_trades": 50,
    "minimum_block_samples": 60,
    "specialist_fitness": 70.0,
    "compatible_fitness": 55.0,
    "avoid_fitness": 30.0,
    "leaderboard_limit": 20,
    "unknown_regime_is_permissive": True,
}

PERFORMANCE_FIELDS = [
    "generated_utc", "scope", "scope_value", "family_id", "portfolio",
    "regime", "status", "fitness_score", "closed_trades", "expectancy_r",
    "profit_factor", "win_rate", "max_drawdown_r", "liquidations",
    "positive_folds", "total_folds", "first_entry_utc", "last_entry_utc",
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
    config["routing_mode"] = "ADVISORY_ONLY"
    config["automatic_strategy_switching"] = False
    config["automatic_position_changes"] = False
    if write_snapshot:
        atomic_json(CONFIG_SNAPSHOT, config)
    return config


def parse_time(value: Any) -> datetime | None:
    text = str(value or "").strip()
    if not text:
        return None
    if text.endswith("Z"):
        text = text[:-1] + "+00:00"
    try:
        parsed = datetime.fromisoformat(text)
    except ValueError:
        for fmt in ("%Y-%m-%d %H:%M:%S", "%Y-%m-%d", "%d/%m/%Y %H:%M:%S"):
            try:
                parsed = datetime.strptime(text, fmt)
                break
            except ValueError:
                parsed = None
        if parsed is None:
            return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def timestamp_from(row: dict[str, Any], keys: tuple[str, ...]) -> datetime | None:
    for key in keys:
        parsed = parse_time(row.get(key))
        if parsed is not None:
            return parsed
    return None


def flatten_text(value: Any) -> str:
    parts: list[str] = []
    if isinstance(value, dict):
        for key, item in value.items():
            parts.append(str(key))
            parts.append(flatten_text(item))
    elif isinstance(value, (list, tuple)):
        for item in value:
            parts.append(flatten_text(item))
    elif value is not None:
        parts.append(str(value))
    return " ".join(parts).upper()


def canonical_regime(value: Any) -> str:
    text = flatten_text(value)
    compact = re.sub(r"[^A-Z0-9]+", "_", text)
    if any(token in compact for token in ("CRASH", "PANIC", "CAPITULATION", "MELTDOWN")):
        return "CRASH"
    if any(token in compact for token in ("RECOVERY", "REBOUND", "RELIEF_RALLY", "REACCUMULATION")):
        return "RECOVERY"
    if any(token in compact for token in ("HIGH_VOL", "EXTREME_VOL", "VOLATILITY_SPIKE", "STRESS")):
        return "HIGH_VOLATILITY"
    if any(token in compact for token in ("BULL", "UPTREND", "RISK_ON", "MARKUP")):
        return "BULL_TREND"
    if any(token in compact for token in ("BEAR", "DOWNTREND", "RISK_OFF", "MARKDOWN")):
        return "BEAR_TREND"
    if any(token in compact for token in ("RANGE", "SIDEWAYS", "NEUTRAL", "NORMAL", "CONSOLIDATION")):
        return "RANGE"
    direction = ""
    if isinstance(value, dict):
        direction = str(value.get("direction") or value.get("market_direction") or "").upper()
    if direction in {"UP", "LONG"}:
        return "BULL_TREND"
    if direction in {"DOWN", "SHORT"}:
        return "BEAR_TREND"
    return "UNKNOWN"


def load_timeline() -> list[dict[str, Any]]:
    rows = []
    for row in read_csv(MARKET_HISTORY):
        moment = timestamp_from(
            row,
            ("generated_utc", "timestamp", "datetime", "date", "as_of", "updated_utc", "created_at"),
        )
        if moment is None:
            continue
        rows.append({"timestamp": moment, "regime": canonical_regime(row), "raw": row})
    rows.sort(key=lambda row: row["timestamp"])
    deduped: dict[str, dict[str, Any]] = {}
    for row in rows:
        deduped[row["timestamp"].isoformat()] = row
    return list(deduped.values())


def current_regime_snapshot(timeline: list[dict[str, Any]] | None = None) -> dict[str, Any]:
    latest = load_json(MARKET_LATEST, {})
    if isinstance(latest, dict) and latest:
        moment = timestamp_from(
            latest,
            ("generated_utc", "timestamp", "datetime", "date", "as_of", "updated_utc", "created_at"),
        )
        return {
            "regime": canonical_regime(latest),
            "as_of_utc": iso(moment) if moment else "",
            "source": MARKET_LATEST.name,
            "raw": latest,
        }
    values = timeline if timeline is not None else load_timeline()
    if values:
        last = values[-1]
        return {
            "regime": last["regime"],
            "as_of_utc": iso(last["timestamp"]),
            "source": MARKET_HISTORY.name,
            "raw": last.get("raw", {}),
        }
    return {"regime": "UNKNOWN", "as_of_utc": "", "source": "NONE", "raw": {}}


def regime_at(moment: datetime | None, timeline: list[dict[str, Any]]) -> str:
    if moment is None:
        return "UNKNOWN"
    selected = "UNKNOWN"
    for row in timeline:
        if row["timestamp"] > moment:
            break
        selected = row["regime"]
    return selected


def trade_entry_time(row: dict[str, Any]) -> datetime | None:
    return timestamp_from(
        row,
        ("opened_at", "entry_time", "opened_utc", "entry_utc", "created_at", "opened_time", "timestamp"),
    )


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


def temporal_folds(values: list[float], fold_count: int = 4) -> tuple[int, int]:
    if not values:
        return 0, 0
    folds = min(fold_count, len(values))
    positive = 0
    for index in range(folds):
        start = index * len(values) // folds
        end = (index + 1) * len(values) // folds
        part = values[start:end]
        if part and statistics.mean(part) > 0:
            positive += 1
    return positive, folds


def fitness(values: list[float], liquidations: int) -> dict[str, Any]:
    count = len(values)
    expectancy = statistics.mean(values) if values else 0.0
    pf = profit_factor(values)
    win = sum(value > 0 for value in values) / count if count else 0.0
    drawdown = max_drawdown(values)
    positive_folds, folds = temporal_folds(values)
    score = 0.0
    score += clamp(count / 50) * 20
    score += clamp((expectancy + 0.20) / 0.60) * 25
    score += clamp((pf - 0.60) / 1.40) * 20
    score += clamp((win - 0.30) / 0.40) * 10
    score += clamp(1 - drawdown / 10) * 15
    score += (positive_folds / folds * 10) if folds else 0
    score -= min(30, liquidations * 10)
    return {
        "fitness_score": round(clamp(score / 100) * 100, 2),
        "closed_trades": count,
        "expectancy_r": expectancy,
        "profit_factor": pf,
        "win_rate": win,
        "max_drawdown_r": drawdown,
        "liquidations": liquidations,
        "positive_folds": positive_folds,
        "total_folds": folds,
    }


def classify(metrics: dict[str, Any], config: dict[str, Any]) -> str:
    count = integer(metrics.get("closed_trades"))
    score = finite(metrics.get("fitness_score"))
    expectancy = finite(metrics.get("expectancy_r"))
    pf = finite(metrics.get("profit_factor"))
    liquidations = integer(metrics.get("liquidations"))
    if count < integer(config.get("minimum_observing_trades"), 10):
        return "INSUFFICIENT"
    if count < integer(config.get("minimum_compatible_trades"), 30):
        return "OBSERVING"
    if liquidations >= 2 or (expectancy <= -0.12 and pf < 0.75):
        return "AVOID"
    if (
        count >= integer(config.get("minimum_specialist_trades"), 50)
        and score >= finite(config.get("specialist_fitness"), 70)
        and expectancy > 0.05
        and pf >= 1.20
        and integer(metrics.get("positive_folds")) >= 3
    ):
        return "SPECIALIST"
    if score >= finite(config.get("compatible_fitness"), 55) and expectancy > 0 and pf >= 1.0:
        return "COMPATIBLE"
    if score <= finite(config.get("avoid_fitness"), 30) or expectancy < 0:
        return "CAUTION"
    return "NEUTRAL"


def portfolio_family_index() -> dict[str, str]:
    output: dict[str, str] = {}
    state = load_json(CANDIDATE_STATE, {"candidates": {}})
    candidates = state.get("candidates", {}) if isinstance(state, dict) else {}
    if isinstance(candidates, dict):
        for row in candidates.values():
            if isinstance(row, dict) and row.get("portfolio_name"):
                output[str(row["portfolio_name"])] = str(row.get("family_id", "unknown"))
    for row in read_csv(EVOLUTION_SCORES):
        portfolio = str(row.get("portfolio", "")).strip()
        if portfolio:
            output.setdefault(portfolio, str(row.get("family_id", slug(portfolio))))
    return output


def build_performance(
    trades: list[dict[str, Any]], timeline: list[dict[str, Any]], config: dict[str, Any], when: datetime
) -> list[dict[str, Any]]:
    family_index = portfolio_family_index()
    grouped: dict[tuple[str, str], list[dict[str, Any]]] = {}
    for row in trades:
        if not str(row.get("closed_at", "")).strip():
            continue
        portfolio = str(row.get("portfolio", "")).strip()
        if not portfolio:
            continue
        entry = trade_entry_time(row)
        regime = regime_at(entry, timeline)
        grouped.setdefault((portfolio, regime), []).append({"row": row, "entry": entry})

    portfolio_rows: list[dict[str, Any]] = []
    for (portfolio, regime), items in grouped.items():
        values = [finite(item["row"].get("r_multiple")) for item in items]
        liquidations = sum(
            str(item["row"].get("close_reason", "")).upper().startswith("LIQUIDATION")
            for item in items
        )
        metrics = fitness(values, liquidations)
        entries = [item["entry"] for item in items if item["entry"] is not None]
        portfolio_rows.append({
            "generated_utc": iso(when),
            "scope": "PORTFOLIO",
            "scope_value": portfolio,
            "family_id": family_index.get(portfolio, slug(portfolio)),
            "portfolio": portfolio,
            "regime": regime,
            "status": classify(metrics, config),
            **metrics,
            "first_entry_utc": iso(min(entries)) if entries else "",
            "last_entry_utc": iso(max(entries)) if entries else "",
        })

    family_groups: dict[tuple[str, str], list[dict[str, Any]]] = {}
    for row in portfolio_rows:
        family_groups.setdefault((str(row["family_id"]), str(row["regime"])), []).append(row)
    family_rows: list[dict[str, Any]] = []
    for (family, regime), rows in family_groups.items():
        total = sum(integer(row.get("closed_trades")) for row in rows)
        if total <= 0:
            continue
        def weighted(key: str) -> float:
            return sum(finite(row.get(key)) * integer(row.get("closed_trades")) for row in rows) / total
        combined = {
            "fitness_score": weighted("fitness_score"),
            "closed_trades": total,
            "expectancy_r": weighted("expectancy_r"),
            "profit_factor": weighted("profit_factor"),
            "win_rate": weighted("win_rate"),
            "max_drawdown_r": sum(finite(row.get("max_drawdown_r")) for row in rows),
            "liquidations": sum(integer(row.get("liquidations")) for row in rows),
            "positive_folds": sum(integer(row.get("positive_folds")) for row in rows),
            "total_folds": sum(integer(row.get("total_folds")) for row in rows),
        }
        family_rows.append({
            "generated_utc": iso(when),
            "scope": "FAMILY",
            "scope_value": family,
            "family_id": family,
            "portfolio": "",
            "regime": regime,
            "status": classify(combined, config),
            **combined,
            "first_entry_utc": min((str(row.get("first_entry_utc", "")) for row in rows if row.get("first_entry_utc")), default=""),
            "last_entry_utc": max((str(row.get("last_entry_utc", "")) for row in rows if row.get("last_entry_utc")), default=""),
        })
    rows = portfolio_rows + family_rows
    rows.sort(
        key=lambda row: (
            row.get("scope") == "FAMILY",
            row.get("regime"),
            finite(row.get("fitness_score")),
            integer(row.get("closed_trades")),
        ),
        reverse=True,
    )
    return rows


def build_regime_memory(rows: list[dict[str, Any]], current_regime: str, config: dict[str, Any], when: datetime) -> dict[str, Any]:
    records: dict[str, dict[str, Any]] = {}
    for row in rows:
        if row.get("scope") != "FAMILY":
            continue
        family = str(row.get("family_id", "unknown"))
        regime = str(row.get("regime", "UNKNOWN"))
        status = str(row.get("status", "INSUFFICIENT"))
        memory_status = {
            "SPECIALIST": "FAVOR",
            "COMPATIBLE": "FAVOR",
            "NEUTRAL": "NEUTRAL",
            "OBSERVING": "INSUFFICIENT",
            "INSUFFICIENT": "INSUFFICIENT",
            "CAUTION": "CAUTION",
            "AVOID": "AVOID",
        }.get(status, "NEUTRAL")
        samples = integer(row.get("closed_trades"))
        blocked = (
            truthy(config.get("candidate_blocking_enabled", False))
            and memory_status == "AVOID"
            and samples >= integer(config.get("minimum_block_samples"), 60)
        )
        key = f"{slug(family)}|{regime}"
        records[key] = {
            "generated_utc": iso(when),
            "signature": key,
            "family_id": family,
            "regime": regime,
            "status": memory_status,
            "source_status": status,
            "fitness_score": finite(row.get("fitness_score")),
            "closed_trades": samples,
            "expectancy_r": finite(row.get("expectancy_r")),
            "profit_factor": finite(row.get("profit_factor")),
            "block_new_candidates": blocked,
            "advisory_only": not truthy(config.get("candidate_blocking_enabled", False)),
        }
    return {
        "schema_version": SCHEMA_VERSION,
        "engine_version": ENGINE_VERSION,
        "generated_utc": iso(when),
        "current_regime": current_regime,
        "routing_mode": "ADVISORY_ONLY",
        "candidate_blocking_enabled": truthy(config.get("candidate_blocking_enabled", False)),
        "automatic_strategy_switching": False,
        "automatic_position_changes": False,
        "automatic_mutations": 0,
        "automatic_promotions": 0,
        "live_modified": False,
        "orders_sent": False,
        "record_count": len(records),
        "blocked_record_count": sum(truthy(row.get("block_new_candidates")) for row in records.values()),
        "records": records,
    }


def regime_candidate_policy_decision(
    parent: dict[str, Any], evidence: dict[str, Any] | None = None
) -> dict[str, Any]:
    config = load_config(write_snapshot=False)
    snapshot = current_regime_snapshot()
    regime = str(snapshot.get("regime", "UNKNOWN"))
    family = slug(
        parent.get("strategy")
        or parent.get("evolution_family_id")
        or parent.get("name")
    )
    if not truthy(config.get("candidate_policy_enabled", True)):
        return {
            "allow": True, "reason": "REGIME_POLICY_DISABLED", "status": "DISABLED",
            "family_id": family, "regime": regime, "fitness_score": None,
            "closed_trades": 0, "advisory_only": True,
        }
    if regime == "UNKNOWN" and truthy(config.get("unknown_regime_is_permissive", True)):
        return {
            "allow": True, "reason": "REGIME_UNKNOWN_PERMISSIVE", "status": "UNKNOWN",
            "family_id": family, "regime": regime, "fitness_score": None,
            "closed_trades": 0, "advisory_only": True,
        }
    document = load_json(MEMORY, {"records": {}})
    records = document.get("records", {}) if isinstance(document, dict) else {}
    record = records.get(f"{family}|{regime}") if isinstance(records, dict) else None
    if not isinstance(record, dict):
        return {
            "allow": True, "reason": "REGIME_MEMORY_NO_HISTORY", "status": "NO_HISTORY",
            "family_id": family, "regime": regime, "fitness_score": None,
            "closed_trades": 0, "advisory_only": True,
        }
    blocked = truthy(record.get("block_new_candidates"))
    return {
        "allow": not blocked,
        "reason": "REGIME_MEMORY_AVOID" if blocked else "REGIME_MEMORY_ALLOW",
        "status": str(record.get("status", "UNKNOWN")),
        "family_id": family,
        "regime": regime,
        "fitness_score": finite(record.get("fitness_score")),
        "closed_trades": integer(record.get("closed_trades")),
        "advisory_only": not truthy(config.get("candidate_blocking_enabled", False)),
    }


def leaderboard_document(rows: list[dict[str, Any]], snapshot: dict[str, Any], config: dict[str, Any], when: datetime) -> dict[str, Any]:
    current = str(snapshot.get("regime", "UNKNOWN"))
    limit = integer(config.get("leaderboard_limit"), 20)
    portfolio_rows = [
        row for row in rows
        if row.get("scope") == "PORTFOLIO" and row.get("regime") == current
    ]
    portfolio_rows.sort(
        key=lambda row: (finite(row.get("fitness_score")), integer(row.get("closed_trades"))),
        reverse=True,
    )
    preferred = [row for row in portfolio_rows if row.get("status") in {"SPECIALIST", "COMPATIBLE"}]
    avoid = [row for row in portfolio_rows if row.get("status") == "AVOID"]
    return {
        "schema_version": SCHEMA_VERSION,
        "engine_version": ENGINE_VERSION,
        "generated_utc": iso(when),
        "current_regime": current,
        "current_regime_as_of_utc": snapshot.get("as_of_utc", ""),
        "current_regime_source": snapshot.get("source", ""),
        "routing_mode": "ADVISORY_ONLY",
        "automatic_strategy_switching": False,
        "positions_modified": False,
        "live_modified": False,
        "orders_sent": False,
        "ranked": portfolio_rows[:limit],
        "preferred": preferred[:limit],
        "avoid": avoid[:limit],
    }


def enrich_registry(rows: list[dict[str, Any]], snapshot: dict[str, Any], when: datetime) -> int:
    registry = load_json(CANDIDATE_REGISTRY, {})
    if not isinstance(registry, dict):
        return 0
    index = {
        (str(row.get("portfolio", "")), str(row.get("regime", ""))): row
        for row in rows if row.get("scope") == "PORTFOLIO"
    }
    current = str(snapshot.get("regime", "UNKNOWN"))
    enriched = 0
    for candidate in registry.get("candidates", []):
        if not isinstance(candidate, dict):
            continue
        portfolio = str(candidate.get("portfolio_name") or candidate.get("name") or "")
        row = index.get((portfolio, current))
        metadata = candidate.setdefault("metadata", {})
        metadata["block10_regime"] = {
            "generated_utc": iso(when),
            "current_regime": current,
            "status": row.get("status") if row else "NO_HISTORY",
            "fitness_score": row.get("fitness_score") if row else None,
            "closed_trades": row.get("closed_trades") if row else 0,
            "routing_mode": "ADVISORY_ONLY",
            "automatic_switching": False,
            "live_modified": False,
        }
        enriched += 1
    registry.update({
        "block10_engine_version": ENGINE_VERSION,
        "block10_generated_utc": iso(when),
        "block10_current_regime": current,
        "block10_enriched_candidates": enriched,
        "automatic_strategy_switching": False,
        "live_modified": False,
        "orders_sent": False,
    })
    atomic_json(CANDIDATE_REGISTRY, registry)
    return enriched


def load_state() -> dict[str, Any]:
    default = {
        "schema_version": SCHEMA_VERSION,
        "engine_version": ENGINE_VERSION,
        "created_utc": iso(),
        "updated_utc": iso(),
        "current_regime": "UNKNOWN",
        "entities": {},
        "totals": {"cycles": 0},
    }
    value = load_json(STATE, default)
    if not isinstance(value, dict):
        value = default
    value.setdefault("entities", {})
    value.setdefault("totals", {"cycles": 0})
    return value


def update_history(state: dict[str, Any], rows: list[dict[str, Any]], snapshot: dict[str, Any], when: datetime) -> None:
    events: list[dict[str, Any]] = []
    previous_regime = str(state.get("current_regime", "UNKNOWN"))
    current_regime = str(snapshot.get("regime", "UNKNOWN"))
    if previous_regime != current_regime:
        events.append({
            "generated_utc": iso(when), "entity_type": "MARKET_REGIME",
            "entity_id": "GLOBAL", "previous_status": previous_regime,
            "current_status": current_regime, "previous_score": "",
            "current_score": "", "reason": "REGIME_CHANGE",
        })
    state["current_regime"] = current_regime
    entities = state.setdefault("entities", {})
    for row in rows:
        identity = f"{row.get('scope')}|{row.get('scope_value')}|{row.get('regime')}"
        previous = entities.get(identity, {})
        old_status = str(previous.get("status", ""))
        new_status = str(row.get("status", ""))
        old_score = finite(previous.get("fitness_score"))
        new_score = finite(row.get("fitness_score"))
        if not previous or old_status != new_status or abs(old_score - new_score) >= 10:
            events.append({
                "generated_utc": iso(when), "entity_type": "REGIME_FITNESS",
                "entity_id": identity, "previous_status": old_status or "NEW",
                "current_status": new_status,
                "previous_score": old_score if previous else "",
                "current_score": new_score, "reason": "REGIME_FITNESS_UPDATE",
            })
        entities[identity] = {
            "status": new_status,
            "fitness_score": new_score,
            "updated_utc": iso(when),
        }
    append_csv(HISTORY, HISTORY_FIELDS, events)


def render_report(rows: list[dict[str, Any]], leaderboard: dict[str, Any], memory: dict[str, Any], when: datetime) -> str:
    current = str(leaderboard.get("current_regime", "UNKNOWN"))
    lines = [
        "# Blocco 10 — Regime Fitness e specializzazione", "",
        f"Generato: {iso(when)}", "",
        "> Paper-only e advisory. Il blocco misura quali strategie funzionano nei "
        "diversi regimi, ma non cambia automaticamente strategia o posizione.", "",
        "## Stato", "",
        f"- Regime corrente: **{current}**",
        f"- Righe di performance: **{len(rows)}**",
        f"- Strategie preferite nel regime corrente: **{len(leaderboard.get('preferred', []))}**",
        f"- Strategie da evitare nel regime corrente: **{len(leaderboard.get('avoid', []))}**",
        f"- Memorie contestuali: **{memory.get('record_count', 0)}**",
        "- Routing automatico: **NO**", "",
        "## Classifica del regime corrente", "",
        "| Rank | Portafoglio | Famiglia | Stato | Fitness | Trade | PF | Expectancy R | DD R |",
        "| ---: | --- | --- | --- | ---: | ---: | ---: | ---: | ---: |",
    ]
    for rank, row in enumerate(leaderboard.get("ranked", [])[:10], 1):
        lines.append(
            f"| {rank} | {row.get('portfolio')} | {row.get('family_id')} | "
            f"{row.get('status')} | {finite(row.get('fitness_score')):.1f} | "
            f"{row.get('closed_trades')} | {finite(row.get('profit_factor')):.2f} | "
            f"{finite(row.get('expectancy_r')):.3f} | "
            f"{finite(row.get('max_drawdown_r')):.2f} |"
        )
    if not leaderboard.get("ranked"):
        lines.append("| — | Nessun campione nel regime corrente | — | INSUFFICIENT | 0 | 0 | 0 | 0 | 0 |")
    lines.extend([
        "", "## Sicurezza", "",
        "- Il regime viene assegnato usando solo l'ultimo record noto prima dell'entrata del trade.",
        "- Nessun uso di dati futuri per classificare il trade.",
        "- Il Candidate Regime Gate è advisory per impostazione predefinita.",
        "- Nessun cambio automatico di MASTER, posizione o live.", "",
    ])
    text = "\n".join(lines)
    atomic_text(REPORT, text)
    return text


def run_regime_evolution_cycle(when: datetime | None = None) -> dict[str, Any]:
    current = when or now_utc()
    config = load_config()
    if not truthy(config.get("enabled", True)):
        return {
            "enabled": False, "status": "DISABLED", "current_regime": "UNKNOWN",
            "performance_rows": 0, "preferred": 0, "avoid": 0,
            "memory_records": 0, "candidate_blocks": 0,
            "automatic_switches": 0, "automatic_mutations": 0,
            "report_markdown": "",
        }
    timeline = load_timeline()
    snapshot = current_regime_snapshot(timeline)
    rows = build_performance(read_csv(TRADE_LOG), timeline, config, current)
    write_csv(PERFORMANCE, PERFORMANCE_FIELDS, rows)
    memory = build_regime_memory(rows, str(snapshot.get("regime", "UNKNOWN")), config, current)
    atomic_json(MEMORY, memory)
    leaderboard = leaderboard_document(rows, snapshot, config, current)
    atomic_json(LEADERBOARD, leaderboard)

    state = load_state()
    update_history(state, rows, snapshot, current)
    state["updated_utc"] = iso(current)
    state["latest_snapshot"] = snapshot
    state["totals"]["cycles"] = integer(state["totals"].get("cycles")) + 1
    state["totals"].update({
        "automatic_switches": 0, "automatic_position_changes": 0,
        "automatic_mutations": 0, "automatic_promotions": 0,
    })
    atomic_json(STATE, state)
    enriched = enrich_registry(rows, snapshot, current)
    report = render_report(rows, leaderboard, memory, current)
    return {
        "enabled": True,
        "status": "OK",
        "engine_version": ENGINE_VERSION,
        "current_regime": str(snapshot.get("regime", "UNKNOWN")),
        "regime_source": str(snapshot.get("source", "NONE")),
        "timeline_rows": len(timeline),
        "performance_rows": len(rows),
        "preferred": len(leaderboard.get("preferred", [])),
        "avoid": len(leaderboard.get("avoid", [])),
        "memory_records": integer(memory.get("record_count")),
        "candidate_blocks": integer(memory.get("blocked_record_count")),
        "registry_enriched": enriched,
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
        "report_markdown": report,
    }
