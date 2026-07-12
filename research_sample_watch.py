# -*- coding: utf-8 -*-
"""One-time Telegram milestones for Research All Signals and market regimes."""

from __future__ import annotations

import math
from pathlib import Path
from typing import Any

import pandas as pd

RESEARCH_TRADES_PATH = Path(
    "reports/research_all_signals_trades.csv"
)

CORE_PROFILES = [
    "MAIN",
    "SHADOW_1H_BALANCED",
    "SHADOW_1H_FAST",
    "SHADOW_4H_WIDE",
    "SHADOW_RELATIVE_STRENGTH",
]

PROFILE_LABELS = {
    "MAIN": "Principale 4H",
    "SHADOW_1H_BALANCED": "Bilanciata 1H",
    "SHADOW_1H_FAST": "Rapida 1H",
    "SHADOW_4H_WIDE": "Ampia 4H",
    "SHADOW_RELATIVE_STRENGTH": "Forza relativa 1H",
    "RSI_EXTREME_LONG_15M": "Scalp RSI Long 15m",
    "RSI_EXTREME_SHORT_15M": "Scalp RSI Short 15m",
}

DEFAULT_STRATEGY_MILESTONES = [30, 100, 200, 300]
DEFAULT_REGIME_MILESTONES = [30, 50, 100]


def _settings(config: dict[str, Any]) -> dict[str, Any]:
    return dict(config.get("notifications", {}))


def _positive_ints(
    values: Any,
    default: list[int],
) -> list[int]:
    raw = values if isinstance(values, list) else default
    output: set[int] = set()
    for item in raw:
        try:
            value = int(item)
        except (TypeError, ValueError):
            continue
        if value > 0:
            output.add(value)
    return sorted(output) or list(default)


def _load_trades() -> pd.DataFrame:
    if not RESEARCH_TRADES_PATH.exists():
        return pd.DataFrame()
    try:
        frame = pd.read_csv(RESEARCH_TRADES_PATH)
    except Exception:
        return pd.DataFrame()
    if frame.empty:
        return frame
    for column in (
        "profile",
        "entry_regime",
        "experiment_group_id",
        "asset",
    ):
        if column not in frame.columns:
            frame[column] = ""
        frame[column] = (
            frame[column]
            .fillna("")
            .astype(str)
            .str.strip()
        )
    for column in ("net_pnl_eur", "r_multiple"):
        frame[column] = pd.to_numeric(
            frame.get(column, 0.0),
            errors="coerce",
        ).fillna(0.0)
    return frame


def _event_ids(frame: pd.DataFrame) -> set[str]:
    if frame.empty:
        return set()
    values = (
        frame["experiment_group_id"]
        .fillna("")
        .astype(str)
        .str.strip()
    )
    return {
        value
        for value in values
        if value
        and value.lower() not in {"nan", "none"}
    }


def _metrics(frame: pd.DataFrame) -> dict[str, Any]:
    if frame.empty:
        return {
            "events": 0,
            "trades": 0,
            "win_rate_pct": 0.0,
            "profit_factor": 0.0,
            "expectancy_r": 0.0,
            "net_pnl_eur": 0.0,
        }

    pnl = pd.to_numeric(
        frame["net_pnl_eur"],
        errors="coerce",
    ).fillna(0.0)
    r_values = pd.to_numeric(
        frame["r_multiple"],
        errors="coerce",
    ).fillna(0.0)
    gross_profit = float(pnl[pnl > 0].sum())
    gross_loss = abs(float(pnl[pnl < 0].sum()))
    wins = int((pnl > 0).sum())
    trades = int(len(frame))
    profit_factor = (
        gross_profit / gross_loss
        if gross_loss > 0
        else (
            math.inf
            if gross_profit > 0
            else 0.0
        )
    )
    return {
        "events": len(_event_ids(frame)),
        "trades": trades,
        "win_rate_pct": (
            wins / trades * 100.0
            if trades
            else 0.0
        ),
        "profit_factor": profit_factor,
        "expectancy_r": (
            float(r_values.mean())
            if trades
            else 0.0
        ),
        "net_pnl_eur": float(pnl.sum()),
    }


def _fmt_num(value: Any) -> str:
    try:
        number = float(value)
        if math.isinf(number):
            return "∞"
        return f"{number:.2f}".replace(".", ",")
    except Exception:
        return "n/a"


def _fmt_eur(value: Any) -> str:
    try:
        number = float(value)
        prefix = "+" if number > 0 else ""
        rendered = f"{prefix}€{number:,.2f}"
        return (
            rendered.replace(",", "X")
            .replace(".", ",")
            .replace("X", ".")
        )
    except Exception:
        return "n/a"


def _label(profile: str) -> str:
    return PROFILE_LABELS.get(profile, profile)


def _strategy_status(milestone: int) -> str:
    if milestone >= 300:
        return "CAMPIONE ROBUSTO"
    if milestone >= 200:
        return "CAMPIONE FORTE"
    if milestone >= 100:
        return "PRIMA VALUTAZIONE SERIA"
    return "PRIME INDICAZIONI"


def _regime_status(milestone: int) -> str:
    if milestone >= 100:
        return "EVIDENZA PIÙ ROBUSTA"
    if milestone >= 50:
        return "UTILIZZABILE NEL META PAPER"
    return "PRIMA INDICAZIONE"


def _chunks(
    lines: list[str],
    max_chars: int = 3500,
) -> list[str]:
    output: list[str] = []
    current: list[str] = []
    length = 0
    for line in lines:
        extra = len(line) + (1 if current else 0)
        if current and length + extra > max_chars:
            output.append("\n".join(current))
            current = [line]
            length = len(line)
        else:
            current.append(line)
            length += extra
    if current:
        output.append("\n".join(current))
    return output


def _sent_strategy(
    state: dict[str, Any],
) -> dict[str, set[int]]:
    raw = (
        state.get("notifications", {})
        .get(
            "research_strategy_milestones_sent",
            {},
        )
    )
    output: dict[str, set[int]] = {}
    if isinstance(raw, dict):
        for profile, values in raw.items():
            output[str(profile)] = {
                int(value)
                for value in (
                    values
                    if isinstance(values, list)
                    else []
                )
                if str(value).isdigit()
            }
    return output


def _sent_regime(
    state: dict[str, Any],
) -> dict[str, set[int]]:
    raw = (
        state.get("notifications", {})
        .get(
            "research_regime_milestones_sent",
            {},
        )
    )
    output: dict[str, set[int]] = {}
    if isinstance(raw, dict):
        for key, values in raw.items():
            output[str(key)] = {
                int(value)
                for value in (
                    values
                    if isinstance(values, list)
                    else []
                )
                if str(value).isdigit()
            }
    return output


def _reached_unsent(
    count: int,
    milestones: list[int],
    sent: set[int],
) -> list[int]:
    return [
        value
        for value in milestones
        if value <= count and value not in sent
    ]


def _asset_diversity(
    frame: pd.DataFrame,
) -> dict[str, Any]:
    if frame.empty:
        return {
            "unique_events": 0,
            "assets": 0,
            "max_asset_share_pct": 100.0,
            "largest_asset": "n/a",
        }

    clean = frame[
        frame["experiment_group_id"].astype(str).str.len()
        > 0
    ].copy()
    if clean.empty:
        return {
            "unique_events": 0,
            "assets": 0,
            "max_asset_share_pct": 100.0,
            "largest_asset": "n/a",
        }

    events = clean.drop_duplicates(
        subset=["experiment_group_id"],
        keep="first",
    )
    counts = events["asset"].replace("", "UNKNOWN").value_counts()
    total = int(len(events))
    largest_asset = (
        str(counts.index[0])
        if not counts.empty
        else "n/a"
    )
    largest_count = (
        int(counts.iloc[0])
        if not counts.empty
        else 0
    )
    return {
        "unique_events": total,
        "assets": int(len(counts)),
        "max_asset_share_pct": (
            largest_count / total * 100.0
            if total
            else 100.0
        ),
        "largest_asset": largest_asset,
    }


def pending_research_notifications(
    state: dict[str, Any],
    config: dict[str, Any],
) -> tuple[
    list[str],
    dict[str, Any],
    dict[str, Any],
]:
    frame = _load_trades()
    settings = _settings(config)
    strategy_milestones = _positive_ints(
        settings.get(
            "research_strategy_milestones",
        ),
        DEFAULT_STRATEGY_MILESTONES,
    )
    regime_milestones = _positive_ints(
        settings.get(
            "research_regime_milestones",
        ),
        DEFAULT_REGIME_MILESTONES,
    )

    sent_strategy = _sent_strategy(state)
    sent_regime = _sent_regime(state)

    marks: dict[str, Any] = {
        "strategy": {},
        "regime": {},
        "meta_ready": False,
    }
    messages: list[str] = []
    strategy_snapshot: dict[str, Any] = {}
    regime_snapshot: dict[str, Any] = {}

    strategy_lines = [
        "📊 CAMPIONE RESEARCH — STRATEGIE",
        "",
    ]
    strategy_alerts = 0

    for profile in CORE_PROFILES:
        subset = (
            frame[
                frame["profile"] == profile
            ]
            if not frame.empty
            else pd.DataFrame()
        )
        metrics = _metrics(subset)
        strategy_snapshot[profile] = metrics
        reached = _reached_unsent(
            int(metrics["events"]),
            strategy_milestones,
            sent_strategy.get(profile, set()),
        )
        if not reached:
            continue

        highest = max(reached)
        marks["strategy"][profile] = reached
        strategy_alerts += 1
        strategy_lines.extend(
            [
                (
                    f"🎯 {_label(profile)} — "
                    f"soglia {highest}"
                ),
                (
                    f"{metrics['events']} eventi indipendenti · "
                    f"{_strategy_status(highest)}"
                ),
                (
                    f"Win rate {_fmt_num(metrics['win_rate_pct'])}% · "
                    f"PF {_fmt_num(metrics['profit_factor'])} · "
                    f"Expectancy {_fmt_num(metrics['expectancy_r'])}R"
                ),
                (
                    f"P&L normalizzato "
                    f"{_fmt_eur(metrics['net_pnl_eur'])}"
                ),
                "",
            ]
        )

    if strategy_alerts:
        strategy_lines.append(
            (
                "Le soglie indicano quando analizzare i "
                "risultati; non abilitano denaro reale."
            )
        )
        messages.extend(_chunks(strategy_lines))

    regime_lines = [
        "🔄 CAMPIONE STRATEGIA × REGIME",
        "",
    ]
    regime_alerts = 0

    if not frame.empty:
        usable = frame[
            ~frame["entry_regime"].isin(
                [
                    "",
                    "UNKNOWN",
                    "LEGACY_UNKNOWN",
                ]
            )
        ]
        for (profile, regime), subset in usable.groupby(
            ["profile", "entry_regime"],
            dropna=False,
        ):
            profile = str(profile)
            regime = str(regime)
            metrics = _metrics(subset)
            key = f"{profile}|{regime}"
            regime_snapshot[key] = metrics
            reached = _reached_unsent(
                int(metrics["events"]),
                regime_milestones,
                sent_regime.get(key, set()),
            )
            if not reached:
                continue

            highest = max(reached)
            marks["regime"][key] = reached
            regime_alerts += 1
            regime_lines.extend(
                [
                    (
                        f"🎯 {_label(profile)} × {regime} "
                        f"— soglia {highest}"
                    ),
                    (
                        f"{metrics['events']} eventi indipendenti · "
                        f"{_regime_status(highest)}"
                    ),
                    (
                        f"Win rate {_fmt_num(metrics['win_rate_pct'])}% · "
                        f"PF {_fmt_num(metrics['profit_factor'])} · "
                        f"Expectancy {_fmt_num(metrics['expectancy_r'])}R"
                    ),
                    (
                        f"P&L normalizzato "
                        f"{_fmt_eur(metrics['net_pnl_eur'])}"
                    ),
                    "",
                ]
            )

    if regime_alerts:
        regime_lines.append(
            (
                "Il dato descrive il regime presente "
                "all’apertura del segnale."
            )
        )
        messages.extend(_chunks(regime_lines))

    minimum_strategy_events = int(
        settings.get(
            "research_meta_min_strategy_events",
            30,
        )
    )
    minimum_pair_events = int(
        settings.get(
            "research_meta_min_pair_events",
            50,
        )
    )
    minimum_pairs = int(
        settings.get(
            "research_meta_min_regime_pairs",
            3,
        )
    )
    minimum_assets = int(
        settings.get(
            "research_meta_min_assets",
            5,
        )
    )
    maximum_asset_share = float(
        settings.get(
            "research_meta_max_single_asset_share_pct",
            40.0,
        )
    )

    strategies_ready = sum(
        int(
            strategy_snapshot.get(
                profile,
                {},
            ).get("events", 0)
        )
        >= minimum_strategy_events
        for profile in CORE_PROFILES
    )
    qualifying_pairs = sum(
        int(metrics.get("events", 0))
        >= minimum_pair_events
        for metrics in regime_snapshot.values()
    )
    diversity = _asset_diversity(frame)
    meta_ready = (
        strategies_ready == len(CORE_PROFILES)
        and qualifying_pairs >= minimum_pairs
        and diversity["assets"] >= minimum_assets
        and diversity["max_asset_share_pct"]
        <= maximum_asset_share
    )
    meta_already_sent = bool(
        state.get("notifications", {}).get(
            "research_meta_ready_sent",
            False,
        )
    )

    if meta_ready and not meta_already_sent:
        marks["meta_ready"] = True
        messages.append(
            "\n".join(
                [
                    (
                        "🧠 DATI SUFFICIENTI PER TESTARE "
                        "IL META-PORTAFOGLIO"
                    ),
                    "",
                    (
                        f"Strategie con almeno "
                        f"{minimum_strategy_events} eventi: "
                        f"{strategies_ready}/{len(CORE_PROFILES)}"
                    ),
                    (
                        f"Coppie strategia-regime con almeno "
                        f"{minimum_pair_events} eventi: "
                        f"{qualifying_pairs}"
                    ),
                    (
                        f"Asset rappresentati: "
                        f"{diversity['assets']}"
                    ),
                    (
                        f"Concentrazione massima: "
                        f"{diversity['largest_asset']} "
                        f"{_fmt_num(diversity['max_asset_share_pct'])}%"
                    ),
                    "",
                    (
                        "È il momento di progettare e testare "
                        "la rotazione automatica, ancora "
                        "esclusivamente in paper trading."
                    ),
                    (
                        "Questo messaggio non autorizza il "
                        "passaggio al trading reale."
                    ),
                ]
            )
        )

    snapshot = {
        "strategy": strategy_snapshot,
        "regime": regime_snapshot,
        "meta_ready": meta_ready,
        "strategies_ready": strategies_ready,
        "qualifying_regime_pairs": qualifying_pairs,
        "asset_diversity": diversity,
    }
    return messages, marks, snapshot


def mark_research_notifications_sent(
    state: dict[str, Any],
    marks: dict[str, Any],
) -> None:
    notifications = state.setdefault(
        "notifications",
        {},
    )

    strategy_store = notifications.setdefault(
        "research_strategy_milestones_sent",
        {},
    )
    for profile, reached in marks.get(
        "strategy",
        {},
    ).items():
        current = {
            int(value)
            for value in strategy_store.get(
                profile,
                [],
            )
            if str(value).isdigit()
        }
        current.update(int(value) for value in reached)
        strategy_store[profile] = sorted(current)

    regime_store = notifications.setdefault(
        "research_regime_milestones_sent",
        {},
    )
    for key, reached in marks.get(
        "regime",
        {},
    ).items():
        current = {
            int(value)
            for value in regime_store.get(
                key,
                [],
            )
            if str(value).isdigit()
        }
        current.update(int(value) for value in reached)
        regime_store[key] = sorted(current)

    if marks.get("meta_ready"):
        notifications[
            "research_meta_ready_sent"
        ] = True
