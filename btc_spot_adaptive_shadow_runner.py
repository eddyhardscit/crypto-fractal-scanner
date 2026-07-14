# -*- coding: utf-8 -*-
from __future__ import annotations
import json
from typing import Any
from kucoin_public_data import CACHE_PATH, collect_market_bundle
from paper_trading_config import load_config
from paper_trading_diagnostics import annotate_market_freshness
from btc_spot_adaptive_shadow import run_btc_spot_adaptive_shadow_cycle

def collect_with_fallback(config: dict[str, Any]) -> dict[str, Any]:
    try: return collect_market_bundle(config)
    except Exception as exc:
        if not CACHE_PATH.exists(): raise
        bundle=json.loads(CACHE_PATH.read_text(encoding='utf-8')); bundle.setdefault('failures',[]).append(f'BTC shadow live collection failed; cache used: {exc}'); bundle['source']=str(bundle.get('source','CACHE'))+':STALE_FALLBACK'; return bundle

def main():
    config=load_config(); bundle=annotate_market_freshness(collect_with_fallback(config),config); result=run_btc_spot_adaptive_shadow_cycle(bundle); state=result['state']; print(f"BTC shadow completed: action={state.get('last_action')} equity={state.get('equity_eur'):.2f} alpha={state.get('alpha_vs_buy_hold_pct'):+.2f}%")
if __name__=='__main__': main()
