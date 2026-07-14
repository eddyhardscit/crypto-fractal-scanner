# -*- coding: utf-8 -*-
"""BTC Spot Adaptive Shadow: paper-only, no leverage, no Telegram."""
from __future__ import annotations
import csv, json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
import pandas as pd
from kucoin_public_data import bundle_frames

REPORTS_DIR = Path('reports')
STATE_PATH = REPORTS_DIR / 'btc_spot_adaptive_shadow_state.json'
REPORT_PATH = REPORTS_DIR / 'btc_spot_adaptive_shadow_report.md'
HISTORY_PATH = REPORTS_DIR / 'btc_spot_adaptive_shadow_history.csv'
INITIAL_CAPITAL_EUR = 40000.0
FEE_RATE = 0.001
MAX_ALLOCATION = 0.80
MIN_CASH_FRACTION = 0.20
BASE_TRANCHE = 0.10

def _now(): return datetime.now(timezone.utc).isoformat(timespec='seconds')
def _fmt_eur(v): return f'€{v:,.2f}'.replace(',','X').replace('.',',').replace('X','.')

def _load_state() -> dict[str, Any]:
    if STATE_PATH.exists():
        try: return json.loads(STATE_PATH.read_text(encoding='utf-8'))
        except Exception: pass
    return {'schema_version':1,'created_utc':_now(),'cash_eur':INITIAL_CAPITAL_EUR,'btc_qty':0.0,'cost_basis_eur':0.0,'realized_pnl_eur':0.0,'fees_eur':0.0,'trades':0,'buy_count':0,'sell_count':0,'peak_equity_eur':INITIAL_CAPITAL_EUR,'max_drawdown_pct':0.0,'last_candle_time':'','last_action':'INIT','last_reason':'Strategia inizializzata','buy_hold_start_price':0.0,'buy_hold_btc_qty':0.0}

def _save(state):
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    STATE_PATH.write_text(json.dumps(state,ensure_ascii=False,indent=2),encoding='utf-8')

def _append_history(row):
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    exists = HISTORY_PATH.exists()
    with HISTORY_PATH.open('a',encoding='utf-8',newline='') as h:
        w=csv.DictWriter(h,fieldnames=list(row))
        if not exists: w.writeheader()
        w.writerow(row)

def run_btc_spot_adaptive_shadow_cycle(bundle: dict[str, Any]) -> dict[str, Any]:
    state=_load_state(); frames=bundle_frames(bundle); frame=frames.get('BTC',{}).get(240)
    source=str(bundle.get('source','UNKNOWN')); fresh=dict(bundle.get('_paper_freshness',{})); allowed=bool(fresh.get('new_entries_allowed',False))
    price=float(bundle.get('assets',{}).get('BTC',{}).get('mark_price',0.0) or 0.0); action='HOLD'; reason='Nessuna nuova candela BTC 4H'
    if frame is None or len(frame)<220:
        reason='Dati BTC 4H insufficienti: servono almeno 220 candele'; metrics={}
    else:
        close=pd.to_numeric(frame.copy().sort_index()['close'],errors='coerce').dropna(); price=float(close.iloc[-1]); candle_time=pd.Timestamp(close.index[-1]).isoformat()
        mid=float(close.rolling(40,min_periods=30).mean().iloc[-1]); vol=float(close.pct_change().rolling(40,min_periods=30).std().iloc[-1]); width=max(0.035,min(0.14,2.0*vol))
        lower1,lower2=mid*(1-width),mid*(1-1.8*width); upper1,upper2=mid*(1+width),mid*(1+1.8*width)
        ema200=float(close.ewm(span=200,adjust=False).mean().iloc[-1]); ema50=float(close.ewm(span=50,adjust=False).mean().iloc[-1])
        if float(state.get('buy_hold_start_price',0.0))<=0 and price>0:
            state['buy_hold_start_price']=price; state['buy_hold_btc_qty']=INITIAL_CAPITAL_EUR/price
        equity=float(state['cash_eur'])+float(state['btc_qty'])*price; allocation=float(state['btc_qty'])*price/equity if equity else 0.0
        cash_floor=equity*MIN_CASH_FRACTION; available=max(0.0,float(state['cash_eur'])-cash_floor); trend_bull=price>=ema200 and ema50>=ema200; trend_weak=price<ema200
        if candle_time!=state.get('last_candle_time'):
            if allowed and price<=lower2 and allocation<MAX_ALLOCATION and available>0:
                amount=min(equity*BASE_TRANCHE*(1.5 if trend_bull else 0.75),available)
                if amount>0:
                    fee=amount*FEE_RATE; state['cash_eur']-=amount; state['btc_qty']+=(amount-fee)/price; state['cost_basis_eur']+=amount; state['fees_eur']+=fee; state['trades']+=1; state['buy_count']+=1
                    action='BUY_DEEP_PULLBACK'; reason='BTC sotto L2; tranche maggiore in trend rialzista' if trend_bull else 'BTC sotto L2; tranche ridotta sotto EMA200'
            elif allowed and price<=lower1 and allocation<MAX_ALLOCATION and available>0 and not trend_weak:
                amount=min(equity*BASE_TRANCHE,available)
                if amount>0:
                    fee=amount*FEE_RATE; state['cash_eur']-=amount; state['btc_qty']+=(amount-fee)/price; state['cost_basis_eur']+=amount; state['fees_eur']+=fee; state['trades']+=1; state['buy_count']+=1
                    action='BUY_PULLBACK'; reason='BTC sotto L1 con trend sopra EMA200'
            elif price>=upper2 and float(state['btc_qty'])>0:
                fraction=.25; qty=float(state['btc_qty'])*fraction; gross=qty*price; fee=gross*FEE_RATE; state['btc_qty']-=qty; state['cash_eur']+=gross-fee; state['fees_eur']+=fee; state['realized_pnl_eur']+=gross-fee-float(state['cost_basis_eur'])*fraction; state['cost_basis_eur']*=1-fraction; state['trades']+=1; state['sell_count']+=1
                action='SELL_25_PERCENT'; reason='BTC sopra U2: alleggerimento progressivo'
            elif price>=upper1 and float(state['btc_qty'])>0:
                fraction=.10; qty=float(state['btc_qty'])*fraction; gross=qty*price; fee=gross*FEE_RATE; state['btc_qty']-=qty; state['cash_eur']+=gross-fee; state['fees_eur']+=fee; state['realized_pnl_eur']+=gross-fee-float(state['cost_basis_eur'])*fraction; state['cost_basis_eur']*=1-fraction; state['trades']+=1; state['sell_count']+=1
                action='SELL_10_PERCENT'; reason='BTC sopra U1: presa di profitto parziale'
            else:
                action='HOLD'; reason='Sotto EMA200: acquisti ordinari sospesi, attivo solo L2' if price<ema200 else 'Prezzo dentro la fascia operativa neutrale'
            state['last_candle_time']=candle_time
        state['bands']={'mid':mid,'lower1':lower1,'lower2':lower2,'upper1':upper1,'upper2':upper2}; state['trend']={'ema50':ema50,'ema200':ema200,'above_ema200':price>=ema200}; metrics=state['bands']|state['trend']
    equity=float(state['cash_eur'])+float(state['btc_qty'])*price; state['peak_equity_eur']=max(float(state.get('peak_equity_eur',equity)),equity); peak=float(state['peak_equity_eur']); dd=max(0.0,(peak-equity)/peak*100.0) if peak else 0.0; state['max_drawdown_pct']=max(float(state.get('max_drawdown_pct',0.0)),dd)
    bh_qty=float(state.get('buy_hold_btc_qty',0.0)); bh_equity=bh_qty*price if bh_qty>0 else INITIAL_CAPITAL_EUR; bh_return=(bh_equity/INITIAL_CAPITAL_EUR-1)*100; strategy_return=(equity/INITIAL_CAPITAL_EUR-1)*100; alpha=strategy_return-bh_return; alloc=float(state['btc_qty'])*price/equity*100 if equity else 0.0
    state.update({'updated_utc':_now(),'last_action':action,'last_reason':reason,'last_price':price,'equity_eur':equity,'return_pct':strategy_return,'buy_hold_equity_eur':bh_equity,'buy_hold_return_pct':bh_return,'alpha_vs_buy_hold_pct':alpha,'allocation_pct':alloc,'market_source':source,'new_entries_allowed':allowed}); _save(state)
    _append_history({'generated_utc':state['updated_utc'],'candle_time':state.get('last_candle_time',''),'price':price,'action':action,'equity_eur':equity,'cash_eur':float(state['cash_eur']),'btc_qty':float(state['btc_qty']),'allocation_pct':alloc,'return_pct':strategy_return,'buy_hold_return_pct':bh_return,'alpha_vs_buy_hold_pct':alpha,'max_drawdown_pct':float(state['max_drawdown_pct'])})
    b=state.get('bands',{}); t=state.get('trend',{})
    report='\n'.join(['# BTC Spot Adaptive Shadow — raccolta dati','',f"Generato: {state['updated_utc']}",'','- Modalità: **SOLO PAPER / SHADOW**','- Asset: **BTC spot**','- Leva: **nessuna (1x)**','- Short: **disabilitato**','- Telegram: **disabilitato**',f'- Capitale iniziale separato: **{_fmt_eur(INITIAL_CAPITAL_EUR)}**',f"- Fonte mercato: **{source}**; nuove entrate: **{'CONSENTITE' if allowed else 'BLOCCATE'}**",'', '| Equity bot | Cash | BTC | Allocazione | Rendimento bot | Buy & Hold | Alpha | Max DD | Operazioni |','| --- | --- | --- | --- | --- | --- | --- | --- | --- |',f"| {_fmt_eur(equity)} | {_fmt_eur(float(state['cash_eur']))} | {float(state['btc_qty']):.8f} | {alloc:.2f}% | {strategy_return:+.2f}% | {bh_return:+.2f}% | {alpha:+.2f}% | {float(state['max_drawdown_pct']):.2f}% | {int(state['trades'])} |",'',f'**Ultima decisione:** {action} — {reason}.','',f"Bande 4H: L2 {float(b.get('lower2',0)):.2f} · L1 {float(b.get('lower1',0)):.2f} · MID {float(b.get('mid',0)):.2f} · U1 {float(b.get('upper1',0)):.2f} · U2 {float(b.get('upper2',0)):.2f}.",f"Trend: EMA50 {float(t.get('ema50',0)):.2f} · EMA200 {float(t.get('ema200',0)):.2f} · prezzo sopra EMA200: **{'SÌ' if t.get('above_ema200') else 'NO'}**.",'', '> Questo esperimento è separato da SOL e dal paper trading multi-strategy.'])
    REPORT_PATH.write_text(report+'\n',encoding='utf-8'); return {'state':state,'report_markdown':report,'metrics':metrics}
