# -*- coding: utf-8 -*-
"""Separate, paper-only SOL spot adaptive-range portfolio."""
from __future__ import annotations
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
import pandas as pd
from kucoin_public_data import bundle_frames

STATE_PATH = Path("reports/sol_spot_adaptive_state.json")
REPORT_PATH = Path("reports/sol_spot_adaptive_report.md")
INITIAL_CAPITAL_EUR = 40000.0
FEE_RATE = 0.001
MAX_ALLOCATION = 0.90
TRANCHE = 0.15

def _now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")

def _load() -> dict[str, Any]:
    if STATE_PATH.exists():
        try:
            return json.loads(STATE_PATH.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {"schema_version":1,"created_utc":_now(),"cash_eur":INITIAL_CAPITAL_EUR,"sol_qty":0.0,"cost_basis_eur":0.0,"realized_pnl_eur":0.0,"fees_eur":0.0,"trades":0,"peak_equity_eur":INITIAL_CAPITAL_EUR,"max_drawdown_pct":0.0,"last_candle_time":"","last_action":"INIT"}

def _save(state: dict[str, Any]) -> None:
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    STATE_PATH.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")

def _fmt_eur(value: float) -> str:
    return f"€{value:,.2f}".replace(",","X").replace(".",",").replace("X",".")

def run_sol_spot_adaptive_cycle(bundle: dict[str, Any]) -> dict[str, Any]:
    state = _load()
    frames = bundle_frames(bundle)
    frame = frames.get("SOL", {}).get(240)
    source = str(bundle.get("source", "UNKNOWN"))
    freshness = dict(bundle.get("_paper_freshness", {}))
    allowed = bool(freshness.get("new_entries_allowed", False))
    if frame is None or len(frame) < 60:
        action, reason = "HOLD", "Dati SOL 4H insufficienti"
        price = float(bundle.get("assets", {}).get("SOL", {}).get("mark_price", 0.0) or 0.0)
    else:
        close = pd.to_numeric(frame.copy().sort_index()["close"], errors="coerce").dropna()
        price = float(close.iloc[-1])
        candle_time = pd.Timestamp(close.index[-1]).isoformat()
        mid = float(close.rolling(30, min_periods=20).mean().iloc[-1])
        vol = float(close.pct_change().rolling(30, min_periods=20).std().iloc[-1])
        width = max(0.035, min(0.18, 2.2 * vol))
        lower1, lower2 = mid*(1-width), mid*(1-1.8*width)
        upper1, upper2 = mid*(1+width), mid*(1+1.8*width)
        equity = float(state["cash_eur"]) + float(state["sol_qty"])*price
        allocation = float(state["sol_qty"])*price/equity if equity > 0 else 0.0
        action, reason = "HOLD", "Prezzo dentro la fascia neutrale"
        if candle_time != state.get("last_candle_time"):
            if allowed and price <= lower2 and allocation < MAX_ALLOCATION:
                amount = min(equity*TRANCHE*1.5, float(state["cash_eur"]))
                fee = amount*FEE_RATE
                state["cash_eur"] -= amount; state["sol_qty"] += (amount-fee)/price
                state["cost_basis_eur"] += amount; state["fees_eur"] += fee; state["trades"] += 1
                action, reason = "BUY_1.5_TRANCHE", "SOL sotto la seconda banda adattiva"
            elif allowed and price <= lower1 and allocation < MAX_ALLOCATION:
                amount = min(equity*TRANCHE, float(state["cash_eur"]))
                fee = amount*FEE_RATE
                state["cash_eur"] -= amount; state["sol_qty"] += (amount-fee)/price
                state["cost_basis_eur"] += amount; state["fees_eur"] += fee; state["trades"] += 1
                action, reason = "BUY_TRANCHE", "SOL sotto la prima banda adattiva"
            elif price >= upper2 and state["sol_qty"] > 0:
                fraction = 0.40; qty = state["sol_qty"]*fraction; gross = qty*price; fee = gross*FEE_RATE
                state["sol_qty"] -= qty; state["cash_eur"] += gross-fee; state["fees_eur"] += fee
                state["realized_pnl_eur"] += gross-fee-state["cost_basis_eur"]*fraction
                state["cost_basis_eur"] *= 1-fraction; state["trades"] += 1
                action, reason = "SELL_40_PERCENT", "SOL sopra la seconda banda adattiva"
            elif price >= upper1 and state["sol_qty"] > 0:
                fraction = 0.20; qty = state["sol_qty"]*fraction; gross = qty*price; fee = gross*FEE_RATE
                state["sol_qty"] -= qty; state["cash_eur"] += gross-fee; state["fees_eur"] += fee
                state["realized_pnl_eur"] += gross-fee-state["cost_basis_eur"]*fraction
                state["cost_basis_eur"] *= 1-fraction; state["trades"] += 1
                action, reason = "SELL_20_PERCENT", "SOL sopra la prima banda adattiva"
            state["last_candle_time"] = candle_time
        state["bands"] = {"mid":mid,"lower1":lower1,"lower2":lower2,"upper1":upper1,"upper2":upper2}
    equity = float(state["cash_eur"]) + float(state["sol_qty"])*price
    state["peak_equity_eur"] = max(float(state.get("peak_equity_eur", equity)), equity)
    peak = state["peak_equity_eur"]
    dd = max(0.0, (peak-equity)/peak*100.0) if peak else 0.0
    state["max_drawdown_pct"] = max(float(state.get("max_drawdown_pct",0.0)), dd)
    state.update({"updated_utc":_now(),"last_action":action,"last_reason":reason,"last_price":price,"equity_eur":equity,"return_pct":(equity/INITIAL_CAPITAL_EUR-1)*100})
    _save(state)
    bands = state.get("bands", {})
    report = "\n".join(["# SOL Spot Adaptive Range — paper trading separato","",f"Generato: {state['updated_utc']}","","- Modalità: **SOLO PAPER TRADING**","- Asset: **SOL spot**","- Leva: **nessuna (1x)**",f"- Capitale iniziale separato: **{_fmt_eur(INITIAL_CAPITAL_EUR)}**",f"- Fonte mercato: **{source}**; nuove entrate: **{'CONSENTITE' if allowed else 'BLOCCATE'}**","","| Equity | Cash | SOL | Prezzo | Rendimento | Realizzato | Commissioni | Max DD | Operazioni |","| --- | --- | --- | --- | --- | --- | --- | --- | --- |",f"| {_fmt_eur(equity)} | {_fmt_eur(float(state['cash_eur']))} | {float(state['sol_qty']):.6f} | {price:.4f} | {state['return_pct']:+.2f}% | {_fmt_eur(float(state['realized_pnl_eur']))} | {_fmt_eur(float(state['fees_eur']))} | {state['max_drawdown_pct']:.2f}% | {state['trades']} |","",f"**Ultima decisione:** {action} — {reason}.","",f"Bande 4H: L2 {bands.get('lower2',0):.4f} · L1 {bands.get('lower1',0):.4f} · media {bands.get('mid',0):.4f} · U1 {bands.get('upper1',0):.4f} · U2 {bands.get('upper2',0):.4f}.","","> Questo portafoglio non condivide capitale, posizioni o statistiche con il paper trading da €10.000."])
    REPORT_PATH.write_text(report+"\n", encoding="utf-8")
    return {"state":state,"report_markdown":report}
