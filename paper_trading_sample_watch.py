# -*- coding: utf-8 -*-
# Statistical sample milestones for automatic paper trading.
# Milestones are based on independent CLOSED market events in MAIN.

from __future__ import annotations

import math
from typing import Any

import pandas as pd

from paper_trading_engine import TRADE_LOG_PATH

DEFAULT_MILESTONES = [30, 100, 200, 300]


def _milestones(config: dict[str, Any]) -> list[int]:
    raw = config.get("notifications", {}).get(
        "sample_milestones",
        DEFAULT_MILESTONES,
    )
    values: set[int] = set()
    for item in raw:
        try:
            value = int(item)
        except (TypeError, ValueError):
            continue
        if value > 0:
            values.add(value)
    return sorted(values) or list(DEFAULT_MILESTONES)


def _main_name(state: dict[str, Any], config: dict[str, Any]) -> str:
    for name, portfolio in state.get("portfolios", {}).items():
        if portfolio.get("is_main"):
            return str(name)
    for portfolio in config.get("portfolios", []):
        if portfolio.get("enabled", True) and portfolio.get("is_main"):
            return str(portfolio.get("name", "MAIN"))
    return "MAIN"


def _load_trades() -> pd.DataFrame:
    if not TRADE_LOG_PATH.exists():
        return pd.DataFrame()
    try:
        return pd.read_csv(TRADE_LOG_PATH)
    except Exception:
        return pd.DataFrame()


def _event_ids(frame: pd.DataFrame) -> set[str]:
    if frame.empty or "experiment_group_id" not in frame.columns:
        return set()
    values = frame["experiment_group_id"].astype(str).str.strip()
    return {
        value
        for value in values
        if value and value.lower() not in {"nan", "none"}
    }


def _pnl_series(frame: pd.DataFrame) -> pd.Series:
    if frame.empty or "net_pnl_eur" not in frame.columns:
        return pd.Series(dtype=float)
    return pd.to_numeric(
        frame["net_pnl_eur"],
        errors="coerce",
    ).fillna(0.0)


def sample_snapshot(
    state: dict[str, Any],
    config: dict[str, Any],
) -> dict[str, Any]:
    milestones = _milestones(config)
    main_name = _main_name(state, config)
    trades = _load_trades()

    if trades.empty or "portfolio" not in trades.columns:
        main_trades = pd.DataFrame()
    else:
        main_trades = trades[
            trades["portfolio"].astype(str) == main_name
        ].copy()

    main_events = len(_event_ids(main_trades))
    system_events = len(_event_ids(trades))
    pnl = _pnl_series(main_trades)
    closed_trades = int(len(main_trades))
    wins = int((pnl > 0).sum()) if not pnl.empty else 0
    win_rate = (
        wins / closed_trades * 100.0
        if closed_trades
        else 0.0
    )
    gross_profit = (
        float(pnl[pnl > 0].sum())
        if not pnl.empty
        else 0.0
    )
    gross_loss = (
        abs(float(pnl[pnl < 0].sum()))
        if not pnl.empty
        else 0.0
    )
    profit_factor = (
        gross_profit / gross_loss
        if gross_loss > 0
        else (math.inf if gross_profit > 0 else 0.0)
    )
    net_pnl = float(pnl.sum()) if not pnl.empty else 0.0
    expectancy = float(pnl.mean()) if not pnl.empty else 0.0

    main_portfolio = state.get("portfolios", {}).get(
        main_name,
        {},
    )
    max_drawdown = float(
        main_portfolio.get("max_drawdown_pct", 0.0)
    )

    next_milestone = next(
        (
            value
            for value in milestones
            if value > main_events
        ),
        None,
    )
    if main_events < 30:
        status = "CAMPIONE INSUFFICIENTE"
        meaning = (
            "Servono altri eventi indipendenti prima "
            "di trarre conclusioni."
        )
    elif main_events < 100:
        status = "PRIME INDICAZIONI"
        meaning = (
            "Si può osservare la direzione, "
            "ma il risultato resta fragile."
        )
    elif main_events < 200:
        status = "PRIMA VALUTAZIONE SERIA"
        meaning = (
            "Campione sufficiente per una prima analisi completa, "
            "non per attivare automaticamente il live."
        )
    elif main_events < 300:
        status = "CAMPIONE FORTE"
        meaning = (
            "Affidabilità maggiore; resta necessario verificare "
            "regimi di mercato diversi."
        )
    else:
        status = "CAMPIONE ROBUSTO"
        meaning = (
            "Campione robusto per la valutazione; "
            "il passaggio al live richiede controllo umano."
        )

    remaining = (
        max(0, int(next_milestone - main_events))
        if next_milestone is not None
        else 0
    )
    return {
        "basis": "MAIN_INDEPENDENT_CLOSED_EVENTS",
        "main_portfolio": main_name,
        "main_independent_events": main_events,
        "system_independent_events": system_events,
        "closed_trades": closed_trades,
        "wins": wins,
        "win_rate_pct": win_rate,
        "profit_factor": profit_factor,
        "net_pnl_eur": net_pnl,
        "expectancy_eur": expectancy,
        "max_drawdown_pct": max_drawdown,
        "milestones": milestones,
        "next_milestone": next_milestone,
        "remaining_to_next": remaining,
        "status": status,
        "meaning": meaning,
    }


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


def _fmt_pct(value: Any) -> str:
    try:
        return f"{float(value):.2f}%".replace(".", ",")
    except Exception:
        return "n/a"


def _fmt_num(value: Any) -> str:
    try:
        number = float(value)
        if math.isinf(number):
            return "∞"
        return f"{number:.2f}".replace(".", ",")
    except Exception:
        return "n/a"


def pending_milestone_notification(
    state: dict[str, Any],
    config: dict[str, Any],
) -> tuple[str | None, list[int], dict[str, Any]]:
    snapshot = sample_snapshot(state, config)
    sent_raw = state.get("notifications", {}).get(
        "sample_milestones_sent",
        [],
    )
    sent = {
        int(value)
        for value in sent_raw
        if str(value).isdigit()
    }
    reached = [
        milestone
        for milestone in snapshot["milestones"]
        if (
            milestone
            <= snapshot["main_independent_events"]
            and milestone not in sent
        )
    ]
    if not reached:
        return None, [], snapshot

    highest = max(reached)
    next_milestone = snapshot.get("next_milestone")
    next_line = (
        f"Prossima soglia: {next_milestone} "
        f"(mancano {snapshot['remaining_to_next']})."
        if next_milestone is not None
        else "Tutte le soglie configurate sono state raggiunte."
    )
    message = "\n".join(
        [
            f"🎯 CAMPIONE STATISTICO — SOGLIA {highest}",
            "",
            (
                "MAIN ha raggiunto "
                f"{snapshot['main_independent_events']} "
                "eventi indipendenti chiusi."
            ),
            f"Stato: {snapshot['status']}",
            snapshot["meaning"],
            "",
            f"Trade chiusi: {snapshot['closed_trades']}",
            f"Win rate: {_fmt_pct(snapshot['win_rate_pct'])}",
            (
                "Profit factor: "
                f"{_fmt_num(snapshot['profit_factor'])}"
            ),
            (
                "Expectancy: "
                f"{_fmt_eur(snapshot['expectancy_eur'], signed=True)} "
                "per trade"
            ),
            (
                "P&L netto: "
                f"{_fmt_eur(snapshot['net_pnl_eur'], signed=True)}"
            ),
            (
                "Max drawdown: "
                f"{_fmt_pct(snapshot['max_drawdown_pct'])}"
            ),
            (
                "Eventi indipendenti complessivi del sistema: "
                f"{snapshot['system_independent_events']}"
            ),
            "",
            next_line,
            (
                "La soglia non abilita automaticamente il trading "
                "reale: segnala che è il momento di fare la "
                "valutazione."
            ),
        ]
    )
    return message, reached, snapshot


def mark_milestones_sent(
    state: dict[str, Any],
    reached: list[int],
) -> None:
    notifications = state.setdefault("notifications", {})
    current = {
        int(value)
        for value in notifications.get(
            "sample_milestones_sent",
            [],
        )
        if str(value).isdigit()
    }
    current.update(int(value) for value in reached)
    notifications["sample_milestones_sent"] = sorted(current)
