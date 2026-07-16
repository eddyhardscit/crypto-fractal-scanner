# -*- coding: utf-8 -*-
"""One-time Telegram milestones for every official shadow portfolio."""

from __future__ import annotations

import math
from typing import Any

import pandas as pd

from paper_trading_display import portfolio_label
from paper_trading_engine import TRADE_FIELDS, TRADE_LOG_PATH
from paper_trading_trade_log_repair import load_trade_frame_resilient


DEFAULT_PORTFOLIO_MILESTONES = [30, 100, 200, 300]


def _milestones(config: dict[str, Any]) -> list[int]:
    raw = config.get("notifications", {}).get(
        "portfolio_trade_milestones",
        DEFAULT_PORTFOLIO_MILESTONES,
    )
    values: set[int] = set()
    for item in raw if isinstance(raw, list) else []:
        try:
            value = int(item)
        except (TypeError, ValueError):
            continue
        if value > 0:
            values.add(value)
    return sorted(values) or list(DEFAULT_PORTFOLIO_MILESTONES)


def _load_trades() -> pd.DataFrame:
    return load_trade_frame_resilient(
        TRADE_LOG_PATH,
        TRADE_FIELDS,
    )


def _event_ids(frame: pd.DataFrame) -> set[str]:
    if frame.empty or "experiment_group_id" not in frame.columns:
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
        if value and value.lower() not in {"nan", "none"}
    }


def _numbers(frame: pd.DataFrame, column: str) -> pd.Series:
    if frame.empty or column not in frame.columns:
        return pd.Series(dtype=float)
    return pd.to_numeric(
        frame[column],
        errors="coerce",
    ).fillna(0.0)


def _metrics(
    frame: pd.DataFrame,
    state_portfolio: dict[str, Any],
) -> dict[str, Any]:
    pnl = _numbers(frame, "net_pnl_eur")
    r_values = _numbers(frame, "r_multiple")
    mfe = _numbers(frame, "mfe_net_eur")
    mae = _numbers(frame, "mae_net_eur")

    trades = int(len(frame))
    wins = int((pnl > 0).sum()) if trades else 0
    gross_profit = float(pnl[pnl > 0].sum()) if trades else 0.0
    gross_loss = abs(float(pnl[pnl < 0].sum())) if trades else 0.0
    profit_factor = (
        gross_profit / gross_loss
        if gross_loss > 0
        else (math.inf if gross_profit > 0 else 0.0)
    )

    return {
        "trades": trades,
        "events": len(_event_ids(frame)),
        "wins": wins,
        "win_rate_pct": wins / trades * 100.0 if trades else 0.0,
        "profit_factor": profit_factor,
        "expectancy_eur": float(pnl.mean()) if trades else 0.0,
        "expectancy_r": float(r_values.mean()) if trades else 0.0,
        "net_pnl_eur": float(pnl.sum()) if trades else 0.0,
        "average_mfe_net_eur": float(mfe.mean()) if trades else 0.0,
        "average_mae_net_eur": float(mae.mean()) if trades else 0.0,
        "max_drawdown_pct": float(
            state_portfolio.get("max_drawdown_pct", 0.0)
        ),
    }


def _sent(state: dict[str, Any]) -> dict[str, set[int]]:
    raw = (
        state.get("notifications", {})
        .get("portfolio_trade_milestones_sent", {})
    )
    output: dict[str, set[int]] = {}
    if not isinstance(raw, dict):
        return output
    for portfolio, values in raw.items():
        output[str(portfolio)] = {
            int(value)
            for value in (values if isinstance(values, list) else [])
            if str(value).isdigit()
        }
    return output


def _fmt_num(value: Any) -> str:
    try:
        number = float(value)
        if math.isinf(number):
            return "∞"
        return f"{number:.2f}".replace(".", ",")
    except Exception:
        return "n/a"


def _fmt_pct(value: Any) -> str:
    try:
        return f"{float(value):.2f}%".replace(".", ",")
    except Exception:
        return "n/a"


def _fmt_eur(value: Any, signed: bool = False) -> str:
    try:
        number = float(value)
        prefix = "+" if signed and number > 0 else ""
        rendered = f"{prefix}€{number:,.2f}"
        return (
            rendered.replace(",", "X")
            .replace(".", ",")
            .replace("X", ".")
        )
    except Exception:
        return "n/a"


def _status(milestone: int) -> str:
    if milestone >= 300:
        return "CAMPIONE ROBUSTO"
    if milestone >= 200:
        return "CAMPIONE FORTE"
    if milestone >= 100:
        return "PRIMA VALUTAZIONE SERIA"
    return "PRIME INDICAZIONI"


def _chunks(lines: list[str], max_chars: int = 3500) -> list[str]:
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


def pending_portfolio_notifications(
    state: dict[str, Any],
    config: dict[str, Any],
) -> tuple[list[str], dict[str, list[int]], dict[str, Any]]:
    milestones = _milestones(config)
    sent = _sent(state)
    trades = _load_trades()

    enabled = [
        definition
        for definition in config.get("portfolios", [])
        if definition.get("enabled", True)
        and not definition.get("is_main", False)
    ]

    marks: dict[str, list[int]] = {}
    snapshot: dict[str, Any] = {}
    lines = ["🎯 CAMPIONE STRATEGIE SHADOW", ""]
    alerts = 0

    for definition in enabled:
        name = str(definition.get("name", "")).strip()
        if not name:
            continue

        if trades.empty or "portfolio" not in trades.columns:
            subset = pd.DataFrame()
        else:
            subset = trades[
                trades["portfolio"].astype(str) == name
            ].copy()

        metrics = _metrics(
            subset,
            state.get("portfolios", {}).get(name, {}),
        )
        snapshot[name] = metrics

        reached = [
            milestone
            for milestone in milestones
            if milestone <= metrics["trades"]
            and milestone not in sent.get(name, set())
        ]
        if not reached:
            continue

        highest = max(reached)
        marks[name] = reached
        alerts += 1
        lines.extend(
            [
                f"📊 {portfolio_label(name)} — soglia {highest}",
                (
                    f"{metrics['trades']} trade chiusi · "
                    f"{metrics['events']} eventi indipendenti"
                ),
                f"Stato: {_status(highest)}",
                (
                    f"Win rate {_fmt_pct(metrics['win_rate_pct'])} · "
                    f"PF {_fmt_num(metrics['profit_factor'])}"
                ),
                (
                    f"Expectancy "
                    f"{_fmt_eur(metrics['expectancy_eur'], signed=True)} "
                    f"per trade · {_fmt_num(metrics['expectancy_r'])}R"
                ),
                (
                    f"P&L netto "
                    f"{_fmt_eur(metrics['net_pnl_eur'], signed=True)} · "
                    f"Max DD {_fmt_pct(metrics['max_drawdown_pct'])}"
                ),
                (
                    f"MFE medio "
                    f"{_fmt_eur(metrics['average_mfe_net_eur'], signed=True)} · "
                    f"MAE medio "
                    f"{_fmt_eur(metrics['average_mae_net_eur'], signed=True)}"
                ),
                (
                    "È il momento di fare una revisione della strategia. "
                    "La soglia non abilita automaticamente il trading reale."
                ),
                "",
            ]
        )

    if not alerts:
        return [], {}, snapshot
    return _chunks(lines), marks, snapshot


def mark_portfolio_notifications_sent(
    state: dict[str, Any],
    marks: dict[str, list[int]],
) -> None:
    notifications = state.setdefault("notifications", {})
    raw = notifications.setdefault(
        "portfolio_trade_milestones_sent",
        {},
    )
    if not isinstance(raw, dict):
        raw = {}
        notifications["portfolio_trade_milestones_sent"] = raw

    for portfolio, reached in marks.items():
        current = {
            int(value)
            for value in raw.get(portfolio, [])
            if str(value).isdigit()
        }
        current.update(int(value) for value in reached)
        raw[portfolio] = sorted(current)
