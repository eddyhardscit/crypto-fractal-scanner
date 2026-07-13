# -*- coding: utf-8 -*-
"""Daily analytics and indicative operating plan for SOL spot paper trading."""

from __future__ import annotations

import json
import math
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
import requests

REPORTS_DIR = Path("reports")
CONFIG_PATH = Path("sol_spot_adaptive_config.json")
STATE_PATH = REPORTS_DIR / "sol_spot_adaptive_state.json"
LATEST_PATH = REPORTS_DIR / "sol_spot_adaptive_latest.json"
TRADES_PATH = REPORTS_DIR / "sol_spot_adaptive_trades.csv"
EQUITY_PATH = REPORTS_DIR / "sol_spot_adaptive_equity.csv"
DASHBOARD_MD = REPORTS_DIR / "sol_spot_adaptive_dashboard.md"
DASHBOARD_JSON = REPORTS_DIR / "sol_spot_adaptive_dashboard.json"


def safe_float(value: Any, default: float = math.nan) -> float:
    try:
        number = float(value)
    except Exception:
        return default
    return number if math.isfinite(number) else default


def read_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return default


def read_csv(path: Path) -> pd.DataFrame:
    if not path.exists() or path.stat().st_size == 0:
        return pd.DataFrame()
    try:
        return pd.read_csv(path)
    except Exception:
        return pd.DataFrame()


def fmt_eur(value: Any) -> str:
    number = safe_float(value, 0.0)
    return f"€{number:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def fmt_pct(value: Any, signed: bool = True) -> str:
    number = safe_float(value, 0.0)
    pattern = "{:+.2f}%" if signed else "{:.2f}%"
    return pattern.format(number).replace(".", ",")


def fmt_num(value: Any, digits: int = 2) -> str:
    return f"{safe_float(value, 0.0):.{digits}f}".replace(".", ",")


def optional_pct(value: Any) -> str:
    return "N/D" if value is None else fmt_pct(value)


def optional_ratio(value: Any) -> str:
    if value is None:
        return "N/D"
    number = safe_float(value)
    if math.isinf(number):
        return "∞"
    return fmt_num(number, 2)


def period_return(series: pd.Series, days: int) -> float | None:
    if series.empty:
        return None
    cutoff = series.index[-1] - pd.Timedelta(days=days)
    previous = series.loc[series.index <= cutoff]
    if previous.empty:
        return None
    base = safe_float(previous.iloc[-1], 0.0)
    latest = safe_float(series.iloc[-1], 0.0)
    return None if base <= 0 else (latest / base - 1.0) * 100.0


def build_operating_plan(
    config: dict[str, Any],
    state: dict[str, Any],
    latest: dict[str, Any],
) -> dict[str, Any]:
    portfolio = latest.get("portfolio", {}) or {}
    range_data = latest.get("range", {}) or {}

    equity = safe_float(portfolio.get("equity_eur"), 0.0)
    cash = safe_float(portfolio.get("cash_eur"), 0.0)
    sol_units = safe_float(portfolio.get("sol_units"), 0.0)
    sol_value = safe_float(portfolio.get("sol_value_eur"), 0.0)
    current_weight = safe_float(portfolio.get("sol_weight"), 0.0)
    target_weight = safe_float(
        range_data.get("target_sol_weight", portfolio.get("target_sol_weight")),
        current_weight,
    )
    price = safe_float(
        range_data.get("price_eur", state.get("last_price_eur")),
        0.0,
    )
    average_cost = safe_float(state.get("average_cost_eur"), 0.0)

    allocation = config.get("allocation", {}) or {}
    minimum_trade = safe_float(allocation.get("minimum_trade_eur"), 250.0)
    rebalance_band = safe_float(
        allocation.get("rebalance_band_fraction"), 0.04
    )
    maximum_trade_fraction = safe_float(
        allocation.get("maximum_trade_fraction_of_equity"), 0.15
    )
    reserve_fraction = safe_float(
        allocation.get("minimum_cash_reserve_fraction"), 0.10
    )

    target_value = target_weight * equity
    difference = target_value - sol_value
    threshold = max(minimum_trade, equity * rebalance_band)
    trade_limit = equity * maximum_trade_fraction
    reserve = equity * reserve_fraction

    action = "HOLD"
    amount = 0.0
    quantity = 0.0
    reason = "Posizione dentro la fascia di ribilanciamento."

    if difference > threshold:
        spendable = max(0.0, cash - reserve)
        amount = min(difference, trade_limit, spendable)
        if amount >= minimum_trade and price > 0:
            action = "BUY"
            quantity = amount / price
            reason = "Peso SOL inferiore al peso obiettivo."
    elif difference < -threshold:
        amount = min(-difference, trade_limit, sol_value)
        if amount >= minimum_trade and price > 0:
            action = "SELL"
            quantity = min(sol_units, amount / price)
            reason = "Peso SOL superiore al peso obiettivo."

    fee_rate = safe_float(
        (config.get("execution", {}) or {}).get("fee_bps"), 10.0
    ) / 10000.0
    slippage_rate = safe_float(
        (config.get("execution", {}) or {}).get("slippage_bps"), 2.0
    ) / 10000.0

    break_even = (
        average_cost * (1.0 + fee_rate + slippage_rate)
        if average_cost > 0
        else None
    )
    unrealized = (
        (price - average_cost) * sol_units
        if price > 0 and average_cost > 0 and sol_units > 0
        else 0.0
    )

    lower = safe_float(range_data.get("lower_eur"), 0.0)
    center = safe_float(range_data.get("center_eur"), 0.0)
    upper = safe_float(range_data.get("upper_eur"), 0.0)
    atr = safe_float(range_data.get("atr_eur"), 0.0)

    # Indicative only: no automatic stop is added to the strategy.
    defensive_price_1 = max(
        0.0,
        min(lower, price - max(atr * 1.5, price * 0.03))
        if price > 0
        else 0.0,
    )
    defensive_price_2 = max(
        0.0,
        min(
            defensive_price_1 - max(atr * 1.5, price * 0.03),
            price - max(atr * 3.0, price * 0.06),
        )
        if price > 0
        else 0.0,
    )

    defensive_quantity_1 = sol_units * 0.25
    defensive_quantity_2 = sol_units * 0.50

    def estimated_loss(exit_price: float, quantity_sol: float) -> float:
        if average_cost <= 0 or exit_price <= 0 or quantity_sol <= 0:
            return 0.0
        gross = exit_price * quantity_sol
        net = gross * (1.0 - fee_rate - slippage_rate)
        return net - average_cost * quantity_sol

    remaining_capacity = max(0.0, cash - reserve)
    remaining_tranches = (
        int(math.floor(remaining_capacity / trade_limit))
        if trade_limit > 0
        else 0
    )
    if remaining_capacity >= minimum_trade and (
        remaining_tranches == 0 or remaining_capacity % trade_limit >= minimum_trade
    ):
        remaining_tranches += 1

    return {
        "current_price_eur": price,
        "average_cost_eur": average_cost,
        "break_even_eur": break_even,
        "unrealized_pnl_eur": unrealized,
        "cash_eur": cash,
        "sol_units": sol_units,
        "sol_value_eur": sol_value,
        "capital_invested_eur": max(0.0, cash + sol_value - cash),
        "position_cost_basis_eur": max(0.0, average_cost * sol_units),
        "position_return_pct": (
            (price / average_cost - 1.0) * 100.0
            if price > 0 and average_cost > 0
            else 0.0
        ),
        "current_weight_pct": current_weight * 100.0,
        "target_weight_pct": target_weight * 100.0,
        "action": action,
        "reason": reason,
        "estimated_amount_eur": amount,
        "estimated_quantity_sol": quantity,
        "range_lower_eur": lower,
        "range_center_eur": center,
        "range_upper_eur": upper,
        "maximum_single_trade_eur": trade_limit,
        "minimum_cash_reserve_eur": reserve,
        "remaining_buying_capacity_eur": remaining_capacity,
        "estimated_remaining_tranches": remaining_tranches,
        "defensive_plan": {
            "automatic_stop_enabled": False,
            "level_1_price_eur": defensive_price_1,
            "level_1_quantity_sol": defensive_quantity_1,
            "level_1_estimated_pnl_eur": estimated_loss(
                defensive_price_1, defensive_quantity_1
            ),
            "level_2_price_eur": defensive_price_2,
            "level_2_quantity_sol": defensive_quantity_2,
            "level_2_estimated_pnl_eur": estimated_loss(
                defensive_price_2, defensive_quantity_2
            ),
            "note": (
                "Livelli puramente informativi. Non generano vendite automatiche "
                "e non modificano la strategia attuale."
            ),
        },
    }


def build_metrics() -> dict[str, Any]:
    config = read_json(CONFIG_PATH, {})
    state = read_json(STATE_PATH, {})
    latest = read_json(LATEST_PATH, {})
    trades = read_csv(TRADES_PATH)
    equity = read_csv(EQUITY_PATH)

    initial = safe_float(
        state.get("initial_capital_eur", config.get("initial_capital_eur")),
        40000.0,
    )

    if not equity.empty:
        equity["time_utc"] = pd.to_datetime(
            equity["time_utc"], utc=True, errors="coerce"
        )
        equity["equity_eur"] = pd.to_numeric(
            equity["equity_eur"], errors="coerce"
        )
        equity["price_eur"] = pd.to_numeric(
            equity["price_eur"], errors="coerce"
        )
        equity = equity.dropna(
            subset=["time_utc", "equity_eur", "price_eur"]
        ).sort_values("time_utc")

    latest_equity = (
        safe_float(equity.iloc[-1]["equity_eur"])
        if not equity.empty
        else safe_float((latest.get("portfolio") or {}).get("equity_eur"), initial)
    )
    total_return = (
        (latest_equity / initial - 1.0) * 100.0 if initial > 0 else 0.0
    )

    daily_return = weekly_return = monthly_return = None
    sharpe = buy_hold_return = buy_hold_equity = excess_vs_buy_hold = None
    max_drawdown = safe_float(state.get("maximum_drawdown_pct"), 0.0)
    observation_days = 0

    if not equity.empty:
        daily = (
            equity.set_index("time_utc")["equity_eur"]
            .resample("1D")
            .last()
            .dropna()
        )
        observation_days = len(daily)
        daily_return = period_return(daily, 1)
        weekly_return = period_return(daily, 7)
        monthly_return = period_return(daily, 30)

        returns = daily.pct_change().dropna()
        volatility = safe_float(returns.std(ddof=1), 0.0)
        if len(returns) >= 2 and volatility > 0:
            sharpe = safe_float(returns.mean(), 0.0) / volatility * math.sqrt(365)

        first_price = safe_float(equity.iloc[0]["price_eur"], 0.0)
        last_price = safe_float(equity.iloc[-1]["price_eur"], 0.0)
        if first_price > 0 and last_price > 0:
            buy_hold_equity = initial * last_price / first_price
            buy_hold_return = (buy_hold_equity / initial - 1.0) * 100.0
            excess_vs_buy_hold = total_return - buy_hold_return

        if "drawdown_pct" in equity.columns:
            dd = pd.to_numeric(equity["drawdown_pct"], errors="coerce").min()
            if pd.notna(dd):
                max_drawdown = min(max_drawdown, float(dd))

    wins = losses = 0
    win_rate = None
    average_profit = 0.0
    average_loss = 0.0
    profit_factor = None
    closed_count = 0

    if not trades.empty and "side" in trades.columns:
        sells = trades[trades["side"].astype(str).str.upper() == "SELL"].copy()
        closed_count = len(sells)
        if closed_count:
            pnl = pd.to_numeric(
                sells["realized_pnl_eur"], errors="coerce"
            ).fillna(0.0)
            positive = pnl[pnl > 0]
            negative = pnl[pnl < 0]
            wins = len(positive)
            losses = len(negative)
            win_rate = wins / closed_count * 100.0
            average_profit = float(positive.mean()) if wins else 0.0
            average_loss = float(negative.mean()) if losses else 0.0
            gross_profit = float(positive.sum()) if wins else 0.0
            gross_loss = abs(float(negative.sum())) if losses else 0.0
            if gross_loss > 0:
                profit_factor = gross_profit / gross_loss
            elif gross_profit > 0:
                profit_factor = math.inf

    return {
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "initial_capital_eur": initial,
        "equity_eur": latest_equity,
        "total_pnl_eur": latest_equity - initial,
        "total_return_pct": total_return,
        "trade_count": int(safe_float(state.get("trade_count"), len(trades))),
        "closed_sell_trades": closed_count,
        "wins": wins,
        "losses": losses,
        "win_rate_pct": win_rate,
        "average_profit_eur": average_profit,
        "average_loss_eur": average_loss,
        "profit_factor": profit_factor,
        "sharpe_ratio_daily_annualized": sharpe,
        "maximum_drawdown_pct": max_drawdown,
        "daily_return_pct": daily_return,
        "weekly_return_pct": weekly_return,
        "monthly_return_pct": monthly_return,
        "buy_hold_equity_eur": buy_hold_equity,
        "buy_hold_return_pct": buy_hold_return,
        "excess_vs_buy_hold_pct": excess_vs_buy_hold,
        "observation_days": observation_days,
        "fees_paid_eur": safe_float(state.get("fees_paid_eur"), 0.0),
        "realized_pnl_eur": safe_float(state.get("realized_pnl_eur"), 0.0),
        "plan": build_operating_plan(config, state, latest),
    }


def render_markdown(metrics: dict[str, Any]) -> str:
    plan = metrics["plan"]
    defense = plan["defensive_plan"]
    action = {
        "BUY": "Acquisto virtuale indicativo",
        "SELL": "Vendita virtuale indicativa",
        "HOLD": "Nessuna operazione indicata",
    }[plan["action"]]

    return "\n".join([
        "# SOL Spot Adaptive — dashboard giornaliera",
        "",
        f"Generato: {metrics['generated_utc']}",
        "",
        "## Prestazioni",
        "",
        "| Metrica | Valore |",
        "| --- | ---: |",
        f"| Equity | {fmt_eur(metrics['equity_eur'])} |",
        f"| P/L totale | {fmt_eur(metrics['total_pnl_eur'])} ({fmt_pct(metrics['total_return_pct'])}) |",
        f"| P/L realizzato | {fmt_eur(metrics['realized_pnl_eur'])} |",
        f"| Fee simulate | {fmt_eur(metrics['fees_paid_eur'])} |",
        f"| Operazioni | {metrics['trade_count']} |",
        f"| Vendite chiuse | {metrics['closed_sell_trades']} |",
        f"| Win rate | {optional_pct(metrics['win_rate_pct'])} |",
        f"| Profitto medio | {fmt_eur(metrics['average_profit_eur'])} |",
        f"| Perdita media | {fmt_eur(metrics['average_loss_eur'])} |",
        f"| Profit factor | {optional_ratio(metrics['profit_factor'])} |",
        f"| Sharpe | {optional_ratio(metrics['sharpe_ratio_daily_annualized'])} |",
        f"| Drawdown massimo | {fmt_pct(metrics['maximum_drawdown_pct'])} |",
        f"| Rendimento 1 giorno | {optional_pct(metrics['daily_return_pct'])} |",
        f"| Rendimento 7 giorni | {optional_pct(metrics['weekly_return_pct'])} |",
        f"| Rendimento 30 giorni | {optional_pct(metrics['monthly_return_pct'])} |",
        "",
        "## Confronto buy & hold SOL",
        "",
        "| Metrica | Valore |",
        "| --- | ---: |",
        f"| Equity buy & hold | {'N/D' if metrics['buy_hold_equity_eur'] is None else fmt_eur(metrics['buy_hold_equity_eur'])} |",
        f"| Rendimento buy & hold | {optional_pct(metrics['buy_hold_return_pct'])} |",
        f"| Differenza bot - buy & hold | {optional_pct(metrics['excess_vs_buy_hold_pct'])} |",
        "",
        "## Posizione attuale",
        "",
        "| Voce | Valore |",
        "| --- | ---: |",
        f"| SOL posseduti | {fmt_num(plan['sol_units'], 6)} SOL |",
        f"| Valore posizione | {fmt_eur(plan['sol_value_eur'])} |",
        f"| Capitale investito al costo medio | {fmt_eur(plan['position_cost_basis_eur'])} |",
        f"| Liquidità disponibile | {fmt_eur(plan['cash_eur'])} |",
        f"| Prezzo medio | {fmt_eur(plan['average_cost_eur'])} |",
        f"| Prezzo attuale | {fmt_eur(plan['current_price_eur'])} |",
        f"| P/L posizione | {fmt_eur(plan['unrealized_pnl_eur'])} ({fmt_pct(plan['position_return_pct'])}) |",
        f"| Capacità residua per acquisti | {fmt_eur(plan['remaining_buying_capacity_eur'])} |",
        f"| Tranche massima successiva | {fmt_eur(plan['maximum_single_trade_eur'])} |",
        f"| Tranche residue stimate | {plan['estimated_remaining_tranches']} |",
        "",
        "## Piano operativo corrente",
        "",
        "| Voce | Valore |",
        "| --- | ---: |",
        f"| Prezzo SOL | {fmt_eur(plan['current_price_eur'])} |",
        f"| Prezzo medio | {fmt_eur(plan['average_cost_eur'])} |",
        f"| Break-even stimato | {'N/D' if plan['break_even_eur'] is None else fmt_eur(plan['break_even_eur'])} |",
        f"| P/L non realizzato | {fmt_eur(plan['unrealized_pnl_eur'])} |",
        f"| Peso attuale | {fmt_num(plan['current_weight_pct'])}% |",
        f"| Peso obiettivo | {fmt_num(plan['target_weight_pct'])}% |",
        f"| Azione indicativa | **{action}** |",
        f"| Importo stimato | {fmt_eur(plan['estimated_amount_eur'])} |",
        f"| Quantità stimata | {fmt_num(plan['estimated_quantity_sol'], 6)} SOL |",
        f"| Motivo | {plan['reason']} |",
        f"| Range | {fmt_eur(plan['range_lower_eur'])} — {fmt_eur(plan['range_center_eur'])} — {fmt_eur(plan['range_upper_eur'])} |",
        "",
        "## Piano difensivo indicativo",
        "",
        "| Livello | Prezzo | Quantità indicativa | P/L stimato |",
        "| --- | ---: | ---: | ---: |",
        f"| Primo alleggerimento | {fmt_eur(defense['level_1_price_eur'])} | {fmt_num(defense['level_1_quantity_sol'], 6)} SOL | {fmt_eur(defense['level_1_estimated_pnl_eur'])} |",
        f"| Riduzione più forte | {fmt_eur(defense['level_2_price_eur'])} | {fmt_num(defense['level_2_quantity_sol'], 6)} SOL | {fmt_eur(defense['level_2_estimated_pnl_eur'])} |",
        "",
        "> Stop automatico non attivo. Questi livelli sono informativi e non modificano la strategia.",
        "",
    ])


def telegram_text(metrics: dict[str, Any]) -> str:
    plan = metrics["plan"]
    defense = plan["defensive_plan"]
    action = {
        "BUY": "🟢 possibile acquisto",
        "SELL": "🔴 possibile vendita",
        "HOLD": "⚪ attesa",
    }[plan["action"]]

    return "\n".join([
        "📈 <b>SOL Spot Adaptive — dashboard giornaliera</b>",
        "",
        f"Equity: <b>{fmt_eur(metrics['equity_eur'])}</b>",
        f"P/L totale: <b>{fmt_eur(metrics['total_pnl_eur'])} ({fmt_pct(metrics['total_return_pct'])})</b>",
        f"Win rate: <b>{optional_pct(metrics['win_rate_pct'])}</b>",
        f"Profit factor: <b>{optional_ratio(metrics['profit_factor'])}</b>",
        f"Sharpe: <b>{optional_ratio(metrics['sharpe_ratio_daily_annualized'])}</b>",
        f"Drawdown max: <b>{fmt_pct(metrics['maximum_drawdown_pct'])}</b>",
        "",
        f"1g: <b>{optional_pct(metrics['daily_return_pct'])}</b> | 7g: <b>{optional_pct(metrics['weekly_return_pct'])}</b> | 30g: <b>{optional_pct(metrics['monthly_return_pct'])}</b>",
        f"Buy & hold SOL: <b>{optional_pct(metrics['buy_hold_return_pct'])}</b>",
        f"Bot - buy & hold: <b>{optional_pct(metrics['excess_vs_buy_hold_pct'])}</b>",
        "",
        "📦 <b>Posizione attuale</b>",
        f"SOL posseduti: <b>{fmt_num(plan['sol_units'], 6)} SOL</b>",
        f"Valore posizione: <b>{fmt_eur(plan['sol_value_eur'])}</b>",
        f"Capitale investito: <b>{fmt_eur(plan['position_cost_basis_eur'])}</b>",
        f"Liquidità: <b>{fmt_eur(plan['cash_eur'])}</b>",
        f"Prezzo medio: <b>{fmt_eur(plan['average_cost_eur'])}</b>",
        f"Prezzo attuale: <b>{fmt_eur(plan['current_price_eur'])}</b>",
        f"P/L posizione: <b>{fmt_eur(plan['unrealized_pnl_eur'])} ({fmt_pct(plan['position_return_pct'])})</b>",
        "",
        "🎯 <b>Capitale ancora disponibile</b>",
        f"Capacità residua per acquisti: <b>{fmt_eur(plan['remaining_buying_capacity_eur'])}</b>",
        f"Tranche massima successiva: <b>{fmt_eur(plan['maximum_single_trade_eur'])}</b>",
        f"Tranche residue stimate: <b>{plan['estimated_remaining_tranches']}</b>",
        "",
        "📋 <b>Piano operativo</b>",
        f"Prezzo: <b>{fmt_eur(plan['current_price_eur'])}</b>",
        f"Carico medio: <b>{fmt_eur(plan['average_cost_eur'])}</b>",
        f"Break-even: <b>{'N/D' if plan['break_even_eur'] is None else fmt_eur(plan['break_even_eur'])}</b>",
        f"P/L non realizzato: <b>{fmt_eur(plan['unrealized_pnl_eur'])}</b>",
        f"Peso: <b>{fmt_num(plan['current_weight_pct'])}%</b> → <b>{fmt_num(plan['target_weight_pct'])}%</b>",
        f"Azione: <b>{action}</b>",
        f"Importo stimato: <b>{fmt_eur(plan['estimated_amount_eur'])}</b>",
        f"Quantità stimata: <b>{fmt_num(plan['estimated_quantity_sol'], 6)} SOL</b>",
        f"Motivo: {plan['reason']}",
        "",
        "🛡️ <b>Piano difensivo indicativo</b>",
        f"Livello 1: <b>{fmt_eur(defense['level_1_price_eur'])}</b> — {fmt_num(defense['level_1_quantity_sol'], 6)} SOL — P/L stimato {fmt_eur(defense['level_1_estimated_pnl_eur'])}",
        f"Livello 2: <b>{fmt_eur(defense['level_2_price_eur'])}</b> — {fmt_num(defense['level_2_quantity_sol'], 6)} SOL — P/L stimato {fmt_eur(defense['level_2_estimated_pnl_eur'])}",
        "",
        f"Range: {fmt_eur(plan['range_lower_eur'])} — {fmt_eur(plan['range_center_eur'])} — {fmt_eur(plan['range_upper_eur'])}",
        "Stop automatico: <b>NON ATTIVO</b>",
        "",
        "🧪 Solo paper trading. Livelli ricalcolati automaticamente.",
    ])


def send_telegram(text: str) -> None:
    token = os.getenv("TELEGRAM_BOT_TOKEN", "").strip()
    chat_id = os.getenv("TELEGRAM_CHAT_ID", "").strip()
    if not token or not chat_id:
        print("Telegram secrets missing; dashboard generated only.")
        return
    response = requests.post(
        f"https://api.telegram.org/bot{token}/sendMessage",
        json={
            "chat_id": chat_id,
            "text": text,
            "parse_mode": "HTML",
            "disable_web_page_preview": True,
        },
        timeout=25,
    )
    response.raise_for_status()
    payload = response.json()
    if not payload.get("ok"):
        raise RuntimeError(f"Telegram API error: {payload}")


def main() -> None:
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    metrics = build_metrics()
    DASHBOARD_JSON.write_text(
        json.dumps(metrics, ensure_ascii=False, indent=2, allow_nan=False),
        encoding="utf-8",
    )
    DASHBOARD_MD.write_text(
        render_markdown(metrics),
        encoding="utf-8",
    )
    send_telegram(telegram_text(metrics))
    print(json.dumps({
        "dashboard": "PASS",
        "equity_eur": metrics["equity_eur"],
        "plan_action": metrics["plan"]["action"],
    }))


if __name__ == "__main__":
    main()
