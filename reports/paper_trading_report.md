# Paper trading automatico KuCoin

Generato: 2026-08-22T05:32:55+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-08-22T05:05:28+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-08-22T05:05:28+00:00 | 2026-08-22T05:05:28+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-08-22T04:45:00+00:00 | 2026-08-22T04:45:00+00:00 | 6,0 min | 25,0 min | OK |
| 60m | 12 | 2026-08-22T04:00:00+00:00 | 2026-08-22T04:00:00+00:00 | 6,0 min | 45,0 min | OK |
| 240m | 12 | 2026-08-22T00:00:00+00:00 | 2026-08-22T00:00:00+00:00 | 1,10 h | 1,00 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1H Balanced V3 Long Only V1 | PEPE | 60m | LONG | 6,25 | 6,00 | 0,00 | OPENED | 6,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Balanced V3 Long Only V1 | ENA | 60m | LONG | 7,25 | 6,00 | 0,00 | OPENED | 6,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Trend Side Regime Guard V1 | ZEC | 60m | LONG | 5,75 | 5,00 | 0,00 | OPENED | 6,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Trend Side Regime Guard V1 | XRP | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 6,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive Side Regime Guard V1 | SOL | 60m | LONG | 6,05 | 5,00 | 0,00 | OPENED | 6,0 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Doge Bollinger 1H | DOGE | 60m | LONG | 5,75 | 5,00 | 0,00 | OPENED | 6,0 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Sol Bollinger 1H | SOL | 60m | LONG | 6,05 | 5,00 | 0,00 | OPENED | 6,0 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive Partial 1R V1 | XRP | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 6,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive Partial 1R V1 | SOL | 60m | LONG | 6,05 | 5,00 | 0,00 | OPENED | 6,0 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive Long Only V1 | ZEC | 60m | LONG | 5,75 | 5,00 | 0,00 | OPENED | 6,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive Long Only V1 | SOL | 60m | LONG | 6,05 | 5,00 | 0,00 | OPENED | 6,0 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive Quality7 V1 | SUI | 60m | LONG | 7,75 | 7,00 | 0,00 | OPENED | 6,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive Mfe Trail | SUI | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 6,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive Mfe Trail | SOL | 60m | LONG | 6,05 | 5,00 | 0,00 | OPENED | 6,0 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive | SUI | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 6,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive | SOL | 60m | LONG | 6,05 | 5,00 | 0,00 | OPENED | 6,0 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Scanner | ZEC | 60m | LONG | 5,75 | 5,00 | 0,00 | OPENED | 6,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Scanner | PEPE | 60m | LONG | 6,25 | 5,00 | 0,00 | OPENED | 6,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Trend | SOL | 60m | LONG | 6,05 | 5,00 | 0,00 | OPENED | 6,0 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top5 Btc Guard Mfe V1 | ZEC | 60m | LONG | 5,75 | 5,00 | 0,00 | OPENED | 6,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top5 Btc Guard Mfe V1 | DOGE | 60m | LONG | 5,75 | 5,00 | 0,00 | OPENED | 6,0 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top5 Btc Guard V1 | ZEC | 60m | LONG | 5,75 | 5,00 | 0,00 | OPENED | 6,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top5 Btc Guard V1 | DOGE | 60m | LONG | 5,75 | 5,00 | 0,00 | OPENED | 6,0 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top5 Btc Mfe V1 | ZEC | 60m | LONG | 5,75 | 5,00 | 0,00 | OPENED | 6,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top5 Btc Mfe V1 | PEPE | 60m | LONG | 6,25 | 5,00 | 0,00 | OPENED | 6,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top 5 + forza BTC 1H | ZEC | 60m | LONG | 5,75 | 5,00 | 0,00 | OPENED | 6,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top 5 + forza BTC 1H | PEPE | 60m | LONG | 6,25 | 5,00 | 0,00 | OPENED | 6,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top20 Long | ZEC | 60m | LONG | 5,75 | 5,00 | 0,00 | OPENED | 6,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top20 Long | PEPE | 60m | LONG | 6,25 | 5,00 | 0,00 | OPENED | 6,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top15 Long | ZEC | 60m | LONG | 5,75 | 5,00 | 0,00 | OPENED | 6,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top15 Long | PEPE | 60m | LONG | 6,25 | 5,00 | 0,00 | OPENED | 6,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top10 Long | ZEC | 60m | LONG | 5,75 | 5,00 | 0,00 | OPENED | 6,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top10 Long | PEPE | 60m | LONG | 6,25 | 5,00 | 0,00 | OPENED | 6,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top 5 Long 1H | ZEC | 60m | LONG | 5,75 | 5,00 | 0,00 | OPENED | 6,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top 5 Long 1H | PEPE | 60m | LONG | 6,25 | 5,00 | 0,00 | OPENED | 6,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Benchmark trend following EMA 1H | XRP | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 6,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Donchian 1H Gb20 120R V1 | DOGE | 60m | LONG | 5,75 | 5,00 | 0,00 | OPENED | 6,0 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Benchmark Donchian breakout 1H | DOGE | 60m | LONG | 5,75 | 5,00 | 0,00 | OPENED | 6,0 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scalp RSI Short 75 · prudente · 5x | SOL | 15m | SHORT | 10,00 | 8,00 | 0,00 | OPENED | 6,0 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scalp RSI Short 80 · prudente · 5x | SOL | 15m | SHORT | 10,00 | 8,00 | 0,00 | OPENED | 6,0 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scalp RSI Short 85 · prudente · 5x | SOL | 15m | SHORT | 10,00 | 8,00 | 0,00 | OPENED | 6,0 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scalp RSI Short 75 · €50 · 15x | SOL | 15m | SHORT | 10,00 | 8,00 | 0,00 | OPENED | 6,0 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 No Esports Mfe Lock V1 | XRP | 60m | LONG | 7,75 | 4,50 | 0,00 | OPENED | 6,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 No Esports Mfe Lock V1 | SUI | 60m | LONG | 7,75 | 4,50 | 0,00 | OPENED | 6,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 No Esports Long Only V1 | SUI | 60m | LONG | 7,75 | 4,50 | 0,00 | OPENED | 6,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 No Esports Long Only V1 | PEPE | 60m | LONG | 6,25 | 4,50 | 0,00 | OPENED | 6,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 No Esports Long Only V1 | ENA | 60m | LONG | 7,25 | 4,50 | 0,00 | OPENED | 6,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 No Esports V1 | XRP | 60m | LONG | 7,75 | 4,50 | 0,00 | OPENED | 6,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 No Esports V1 | SUI | 60m | LONG | 7,75 | 4,50 | 0,00 | OPENED | 6,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 Long Only V1 | SUI | 60m | LONG | 7,75 | 4,50 | 0,00 | OPENED | 6,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida 1H V3 Filtered | XRP | 60m | LONG | 7,75 | 4,50 | 0,00 | OPENED | 6,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida 1H V3 Filtered | SUI | 60m | LONG | 7,75 | 4,50 | 0,00 | OPENED | 6,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Tp2 V1 | XRP | 60m | LONG | 7,75 | 4,50 | 0,00 | OPENED | 6,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast No Pepe V1 | SUI | 60m | LONG | 7,75 | 4,50 | 0,00 | OPENED | 6,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast No Pepe V1 | SOL | 60m | LONG | 6,05 | 4,50 | 0,00 | OPENED | 6,0 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast No Pepe V1 | ADA | 60m | LONG | 7,75 | 4,50 | 0,00 | OPENED | 6,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Score 6 75 Cost Aware V1 | SOL | 60m | LONG | 6,05 | 6,00 | 0,00 | OPENED | 6,0 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Score 6 75 Cost Aware V1 | ENA | 60m | LONG | 7,25 | 6,00 | 0,00 | OPENED | 6,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Bilanciata 1H V3 Filtered | PEPE | 60m | LONG | 6,25 | 6,00 | 0,00 | OPENED | 6,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Bilanciata 1H V3 Filtered | ENA | 60m | LONG | 7,25 | 6,00 | 0,00 | OPENED | 6,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Principale 4H | ADA | 240m | LONG | 7,75 | 6,00 | 0,00 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 66.0 minuti; tolleranza 60 minuti. |
| Principale 4H | ENA | 240m | LONG | 7,75 | 6,00 | 0,00 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 66.0 minuti; tolleranza 60 minuti. |
| Principale 4H | HYPE | 240m | LONG | 7,75 | 6,00 | 0,00 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 66.0 minuti; tolleranza 60 minuti. |
| Principale 4H | SUI | 240m | LONG | 7,75 | 6,00 | 0,00 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 66.0 minuti; tolleranza 60 minuti. |
| Principale 4H | XRP | 240m | LONG | 7,75 | 6,00 | 0,00 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 66.0 minuti; tolleranza 60 minuti. |
| Principale 4H | ZEC | 240m | LONG | 7,75 | 6,00 | 0,00 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 66.0 minuti; tolleranza 60 minuti. |
| Principale 4H | PEPE | 240m | LONG | 6,25 | 6,00 | 0,00 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 66.0 minuti; tolleranza 60 minuti. |
| Principale 4H | SOL | 240m | LONG | 5,94 | 6,00 | 0,06 | STALE_CANDLE | 1,10 h | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 66.0 minuti; tolleranza 60 minuti. |
| Principale 4H | DOGE | 240m | LONG | 5,75 | 6,00 | 0,25 | STALE_CANDLE | 1,10 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 66.0 minuti; tolleranza 60 minuti. |
| Principale 4H | ETH | 240m | LONG | 5,75 | 6,00 | 0,25 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 66.0 minuti; tolleranza 60 minuti. |
| Principale 4H | LINK | 240m | LONG | 5,75 | 6,00 | 0,25 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 66.0 minuti; tolleranza 60 minuti. |
| Principale 4H | BTC | 240m | LONG | 2,75 | 6,00 | 3,25 | STALE_CANDLE | 1,10 h | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 66.0 minuti; tolleranza 60 minuti. |
| Scalp RSI Short 75 · €10 · 15x | DOGE | 15m | SHORT | 10,00 | 8,00 | 0,00 | READY | 6,0 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Scalp RSI Short 75 · €50 · 15x | DOGE | 15m | SHORT | 10,00 | 8,00 | 0,00 | READY | 6,0 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Scalp RSI Short 75 · prudente · 5x | DOGE | 15m | SHORT | 10,00 | 8,00 | 0,00 | READY | 6,0 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Scalp RSI Short 85 · €10 · 15x | SOL | 15m | SHORT | 10,00 | 8,00 | 0,00 | OPENED | 6,0 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scalp RSI Short 80 · €10 · 15x | SOL | 15m | SHORT | 10,00 | 8,00 | 0,00 | OPENED | 6,0 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scalp RSI Short 75 · €10 · 15x | SOL | 15m | SHORT | 10,00 | 8,00 | 0,00 | OPENED | 6,0 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scalp RSI Short 85 · €50 · 15x | SOL | 15m | SHORT | 10,00 | 8,00 | 0,00 | OPENED | 6,0 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scalp RSI Short 80 · €50 · 15x | SOL | 15m | SHORT | 10,00 | 8,00 | 0,00 | OPENED | 6,0 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.908,56 | -0,91% | €160,22 | €3.000,00 | 5,34% | 6 | 49 | 38,78% | 0,90 | 6,39% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 49 | 2013 | PRIME INDICAZIONI | 100 (mancano 51) |

- Trade del Principale 4H chiusi: **49**; win rate **38,78%**; profit factor **0,90**.
- Expectancy: **€-2,83** per trade; P&L netto: **€-138,62**; max drawdown: **6,39%**.
- Valutazione: **Si può osservare la direzione, ma il risultato resta fragile.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 6 | €9.908,56 | €797,60 | €2.392,80 | €196,89 | €48,36 |
| TEST | Benchmark Donchian breakout 1H | 5 | €11.938,79 | €3.442,55 | €6.885,10 | €121,81 | €127,12 |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | 7 | €11.698,39 | €2.056,29 | €6.168,86 | €176,27 | €57,51 |
| TEST | Combo Trend Side Regime Guard V1 | 6 | €11.696,40 | €2.573,40 | €5.146,79 | €119,09 | €140,94 |
| TEST | Donchian 1H Gb20 120R V1 | 5 | €11.657,70 | €3.361,50 | €6.722,99 | €118,95 | €124,13 |
| TEST | Scanner Top 5 Long 1H | 5 | €11.401,55 | €1.535,12 | €3.070,24 | €158,04 | €105,62 |
| TEST | 1H Fast No Pepe V1 | 7 | €11.389,39 | €1.950,66 | €5.851,99 | €227,79 | €-3,01 |
| TEST | Combo Adaptive Long Only V1 | 8 | €11.141,94 | €2.858,38 | €5.716,77 | €169,02 | €94,80 |
| TEST | Combo Adaptive Side Regime Guard V1 | 5 | €11.077,72 | €2.927,88 | €5.855,76 | €113,41 | €155,49 |
| TEST | Combo Adaptive | 8 | €11.053,36 | €2.515,55 | €5.031,11 | €111,99 | €127,51 |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | 6 | €10.821,44 | €1.848,77 | €5.546,30 | €216,43 | €-2,54 |
| TEST | Main Side Regime Guard V1 | 2 | €10.791,89 | €288,21 | €864,64 | €103,76 | €0,00 |
| TEST | Rapida 1H V3 Filtered | 6 | €10.751,91 | €1.836,89 | €5.510,67 | €215,04 | €-2,52 |
| TEST | 1H Fast V3 No Esports Long Only V1 | 6 | €10.687,48 | €1.597,92 | €4.793,76 | €213,75 | €-2,70 |
| TEST | Scanner Top 5 + forza BTC 1H | 5 | €10.678,54 | €1.500,41 | €3.000,83 | €109,12 | €170,53 |
| TEST | Scanner Top5 Btc Tp3 V1 | 5 | €10.671,88 | €626,24 | €1.252,48 | €52,96 | €107,48 |
| TEST | Scanner Top5 Btc Runner25 V1 | 5 | €10.665,63 | €625,87 | €1.251,75 | €52,93 | €107,42 |
| TEST | 1H Fast V3 No Esports V1 | 6 | €10.536,56 | €1.728,02 | €5.184,06 | €210,40 | €-2,75 |
| TEST | 1H Fast Tp2 V1 | 7 | €10.535,62 | €1.737,71 | €5.213,12 | €164,04 | €44,48 |
| TEST | Scanner Top10 Long | 6 | €10.519,56 | €2.040,96 | €4.081,91 | €157,68 | €73,68 |
| TEST | Combo Adaptive Partial 1R V1 | 6 | €10.437,24 | €2.450,79 | €4.901,58 | €205,04 | €36,96 |
| TEST | Ampia 4H | 6 | €10.397,69 | €1.333,22 | €2.666,45 | €98,36 | €182,72 |
| TEST | Rapida 1H V2 | 2 | €10.397,11 | €894,86 | €2.684,59 | €101,20 | €7,69 |
| TEST | Scanner Top15 Long | 7 | €10.375,67 | €2.024,39 | €4.048,77 | €155,33 | €71,22 |
| TEST | Scanner Top20 Long | 7 | €10.375,67 | €2.024,39 | €4.048,77 | €155,33 | €71,22 |
| TEST | Bilanciata 1H V3 Filtered | 5 | €10.339,88 | €1.420,78 | €4.262,34 | €157,25 | €30,58 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 0 | €10.300,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Donchian 4H | 1 | €10.271,77 | €569,88 | €1.139,76 | €0,00 | €68,06 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 0 | €10.271,73 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Nohigh Range Only V1 | 0 | €10.247,95 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Scanner | 5 | €10.245,16 | €1.439,52 | €2.879,04 | €104,69 | €163,61 |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 0 | €10.239,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 0 | €10.235,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 4H | 1 | €10.233,65 | €520,73 | €1.041,47 | €0,00 | €62,19 |
| TEST | Main Dynamic Asset Selector V1 | 0 | €10.213,35 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 0 | €10.185,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Donchian 1H | 0 | €10.156,88 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Score 6 75 Range Only V1 | 0 | €10.149,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 0 | €10.145,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | 0 | €10.140,84 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 1H | 0 | €10.138,40 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | 0 | €10.126,53 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Guard V1 | 6 | €10.125,27 | €1.407,79 | €2.815,58 | €194,35 | €11,43 |
| TEST | Combo Adaptive Quality7 V1 | 6 | €10.117,63 | €2.182,80 | €4.365,60 | €101,70 | €137,46 |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 0 | €10.099,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 4H | 1 | €10.098,77 | €560,28 | €1.120,56 | €0,00 | €66,91 |
| TEST | Btc Adaptive 1H | 0 | €10.083,25 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 4H | 0 | €10.070,19 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 1H | 0 | €10.067,96 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Forza relativa 1H V2 | 4 | €10.062,05 | €1.238,28 | €2.476,56 | €49,90 | €92,78 |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 0 | €10.048,77 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V1 | 0 | €10.043,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | 1 | €10.040,56 | €201,73 | €403,45 | €0,00 | €0,00 |
| TEST | Sol Ema 1H | 0 | €10.039,53 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Balanced Short Trend Down Strict V1 | 0 | €10.035,46 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 4H | 0 | €10.029,45 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · prudente · 5x | 0 | €10.028,67 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Nohigh Cap75 V1 | 0 | €10.028,66 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 4H | 0 | €10.019,41 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Ema 1H | 0 | €10.018,06 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | 0 | €10.013,82 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Mfe V1 | 5 | €10.010,60 | €1.406,56 | €2.813,13 | €102,30 | €159,86 |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 0 | €10.008,92 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 0 | €10.003,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 1 | €10.002,76 | €50,00 | €750,00 | €28,50 | €-0,15 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 1 | €10.000,55 | €10,00 | €150,00 | €5,70 | €-0,03 |
| TEST | Scanner Bottom5 Short Continuation V1 | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €10 · 15x | 0 | €9.999,33 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €10 · 15x | 0 | €9.997,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €50 · 15x | 0 | €9.996,64 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 0 | €9.995,23 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €10 · 15x | 1 | €9.995,13 | €10,00 | €150,00 | €5,70 | €-0,03 |
| TEST | Scalp RSI Short 80 · €10 · 15x | 1 | €9.994,64 | €10,00 | €150,00 | €5,70 | €-0,03 |
| TEST | 1H Fast V3 Long Only V1 | 6 | €9.993,87 | €1.885,78 | €5.657,34 | €151,31 | €49,14 |
| TEST | Scalp RSI Long 25 · €10 · 15x | 0 | €9.990,45 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €50 · 15x | 0 | €9.988,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 0 | €9.987,48 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 1H | 1 | €9.987,23 | €689,68 | €2.069,03 | €0,00 | €46,69 |
| TEST | Sol Bollinger 4H | 0 | €9.981,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · prudente · 5x | 0 | €9.980,94 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · prudente · 5x | 1 | €9.979,50 | €52,53 | €262,67 | €9,98 | €-0,05 |
| TEST | Scalp RSI Short 85 · €50 · 15x | 1 | €9.975,65 | €50,00 | €750,00 | €28,50 | €-0,15 |
| TEST | Scalp RSI Short 80 · €50 · 15x | 1 | €9.973,19 | €50,00 | €750,00 | €28,50 | €-0,15 |
| TEST | Doge Bollinger 1H | 1 | €9.972,13 | €452,53 | €1.357,60 | €49,87 | €-0,27 |
| TEST | Eth Adaptive 1H | 1 | €9.971,41 | €646,30 | €1.938,91 | €49,87 | €-1,78 |
| TEST | Btc Donchian 4H | 0 | €9.965,81 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Ema 4H | 1 | €9.964,20 | €495,92 | €991,85 | €49,81 | €2,05 |
| TEST | Scalp RSI Long 25 · €50 · 15x | 0 | €9.952,25 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · prudente · 5x | 1 | €9.940,59 | €52,33 | €261,65 | €9,94 | €-0,05 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 1 | €9.927,80 | €52,26 | €261,31 | €9,93 | €-0,05 |
| TEST | Eth Ema 1H | 1 | €9.918,45 | €642,87 | €1.928,61 | €49,61 | €-1,77 |
| TEST | Combo Adaptive Quality7 Regime V1 | 1 | €9.914,27 | €199,19 | €398,38 | €0,00 | €0,00 |
| TEST | Doge Donchian 1H | 0 | €9.911,95 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Balanced Long No Rhv V1 | 6 | €9.908,51 | €1.447,06 | €4.341,18 | €196,00 | €9,08 |
| TEST | Sol Adaptive 1H | 0 | €9.896,74 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Guard Mfe V1 | 6 | €9.889,79 | €1.375,05 | €2.750,10 | €189,83 | €11,16 |
| TEST | Combo Adaptive Regime V1 | 1 | €9.886,53 | €202,91 | €405,83 | €0,00 | €0,00 |
| TEST | Eth Donchian 1H | 1 | €9.884,75 | €727,11 | €2.181,32 | €49,48 | €-10,34 |
| TEST | Combo Adaptive Mfe Trail | 6 | €9.850,81 | €2.520,33 | €5.040,66 | €98,08 | €138,40 |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 0 | €9.837,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Trend | 6 | €9.821,93 | €2.387,82 | €4.775,65 | €51,78 | €142,93 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 0 | €9.817,34 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 1H | 1 | €9.801,38 | €603,90 | €1.811,71 | €49,01 | €-0,36 |
| TEST | 1H Balanced V3 Long Only V1 | 5 | €9.779,87 | €1.343,83 | €4.031,50 | €148,74 | €28,92 |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | 0 | €9.779,10 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 0 | €9.762,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H V2 | 4 | €9.741,78 | €1.174,69 | €3.524,08 | €52,02 | €79,39 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 0 | €9.723,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | 0 | €9.711,41 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Bollinger 1H | 1 | €9.642,81 | €755,04 | €2.265,13 | €48,17 | €9,83 |
| TEST | Global Confluence puro 1H | 0 | €9.628,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Score 6 75 V1 | 0 | €9.626,87 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | 1 | €9.595,22 | €199,19 | €398,38 | €47,81 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 0 | €9.579,83 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | 0 | €9.517,55 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Benchmark trend following EMA 1H | 8 | €9.469,38 | €2.020,42 | €4.040,84 | €92,88 | €82,81 |
| TEST | 1H Fast V3 Nohigh V1 | 0 | €9.435,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | 1 | €9.430,59 | €195,77 | €391,54 | €46,99 | €0,00 |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | 0 | €9.389,68 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom10 Short | 3 | €9.385,05 | €1.090,11 | €2.180,22 | €97,35 | €0,00 |
| TEST | Scanner Bottom15 Short | 3 | €9.385,05 | €1.090,11 | €2.180,22 | €97,35 | €0,00 |
| TEST | Scanner Bottom20 Short | 3 | €9.385,05 | €1.090,11 | €2.180,22 | €97,35 | €0,00 |
| TEST | Master Adaptive Runner25 V1 | 1 | €9.378,18 | €34,77 | €69,54 | €8,34 | €0,00 |
| TEST | Master Adaptive Gb20 Be V1 | 0 | €9.372,49 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | 0 | €9.370,91 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Gb20 Partial V1 | 0 | €9.362,52 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Cap75 V1 | 0 | €9.355,17 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive No Alt V1 | 0 | €9.354,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive V1 | 0 | €9.326,30 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | 3 | €9.320,02 | €1.082,57 | €2.165,15 | €96,67 | €0,00 |
| TEST | Master Adaptive Expanded V1 | 1 | €9.319,82 | €197,50 | €395,01 | €47,40 | €0,00 |
| TEST | Scanner Bottom5 Short Profit Lock V1 | 3 | €9.305,85 | €1.080,93 | €2.161,86 | €96,53 | €0,00 |
| TEST | Master Adaptive Gb20 Loss Cap V1 | 1 | €9.252,08 | €195,70 | €391,41 | €45,67 | €0,00 |
| TEST | Scanner Top5 Btc Btc Le3 V1 | 0 | €9.237,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom 5 Short 1H | 3 | €9.234,23 | €1.072,61 | €2.145,22 | €95,79 | €0,00 |
| TEST | Master Adaptive Gb20 V1 | 0 | €9.202,39 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H V1 | 0 | €9.150,69 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Mean Reversion | 0 | €9.114,32 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Strict3 V1 | 0 | €9.056,84 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Runner25 V1 | 0 | €8.964,11 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Tp3 V1 | 0 | €8.796,64 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Benchmark Bollinger mean reversion 1H | 0 | €8.740,52 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Forza relativa 1H V1 | 0 | €8.445,51 | €0,00 | €0,00 | €0,00 | €0,00 |

**Importante:** ogni riga è un conto virtuale separato da €10.000. I margini dei diversi portafogli non vanno sommati come se appartenessero a un unico conto.

**Rischio agli stop** è la perdita residua stimata usando gli stop correnti. Se uno stop protegge già un profitto, il rischio residuo viene mostrato come €0.

## Legenda portafogli

| Tipo | Nome leggibile | Metodo | Significato |
| --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | Confluenza trend | Riferimento principale: confluenza di trend su 4 ore, soglia più selettiva. |
| TEST | Bilanciata 1H V1 | Confluenza trend | Versione originale V1 a 1 ora basata sulla confluenza di trend. |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | Versione V2 selettiva: esclude i regimi storicamente peggiori, richiede trend e ritorni coerenti e limita i segnali correlati. |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | Versione V3 derivata dalla V1: accetta soltanto score assoluti da 6,0 a meno di 7,5, cioè la fascia BUONA risultata migliore nel confronto Paper vs Shadow. |
| TEST | Rapida 1H V1 | Momentum / breakout | Versione originale V1 a 1 ora che cerca momentum e breakout. |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | Versione V2 selettiva: richiede vero breakout, volume, ADX, trend tecnico coerente e limita i segnali correlati. |
| TEST | Rapida 1H V3 Filtered | Momentum / breakout V3 Filtered | Versione V3 derivata dalla V1: mantiene la logica momentum originale ma esclude i segnali con score assoluto da 5,0 a meno di 6,0, fascia risultata negativa nel confronto Paper vs Shadow. |
| TEST | Ampia 4H | Confluenza trend | Test a 4 ore con stop più ampio, leva inferiore e durata maggiore. |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | Versione originale V1 a 1 ora basata sulla forza o debolezza rispetto a Bitcoin. |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | Versione V2 più selettiva: forza vs BTC, trend USDT, RSI, ADX, regime e massimo due segnali per direzione nella stessa candela. |
| TEST | Scalp RSI Long 15 · €10 · 15x | Inversione RSI estrema 15m | Scalp long 15m: RSI scende fino a 15 e conferma il recupero verso 20. Margine fisso €10, leva paper 15x. |
| TEST | Scalp RSI Long 20 · €10 · 15x | Inversione RSI estrema 15m | Scalp long 15m: RSI scende fino a 20 e conferma il recupero verso 25. Margine fisso €10, leva paper 15x. |
| TEST | Scalp RSI Long 25 · €10 · 15x | Inversione RSI estrema 15m | Scalp long 15m: RSI scende fino a 25 e conferma il recupero verso 30. Margine fisso €10, leva paper 15x. |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | Scalp long 15m: RSI scende fino a 15 e conferma il recupero verso 20. Margine fisso €50, leva paper 15x. |
| TEST | Scalp RSI Long 20 · €50 · 15x | Inversione RSI estrema 15m | Scalp long 15m: RSI scende fino a 20 e conferma il recupero verso 25. Margine fisso €50, leva paper 15x. |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | Scalp long 15m: RSI scende fino a 25 e conferma il recupero verso 30. Margine fisso €50, leva paper 15x. |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | Scalp long 15m: RSI scende fino a 15 e conferma il recupero verso 20. Versione prudente, leva 5x e rischio ridotto. |
| TEST | Scalp RSI Long 20 · prudente · 5x | Inversione RSI estrema 15m | Scalp long 15m: RSI scende fino a 20 e conferma il recupero verso 25. Versione prudente, leva 5x e rischio ridotto. |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | Scalp long 15m: RSI scende fino a 25 e conferma il recupero verso 30. Versione prudente, leva 5x e rischio ridotto. |
| TEST | Scalp RSI Short 85 · €10 · 15x | Inversione RSI estrema 15m | Scalp short 15m: RSI sale fino a 85 e conferma il rientro verso 80. Margine fisso €10, leva paper 15x. |
| TEST | Scalp RSI Short 80 · €10 · 15x | Inversione RSI estrema 15m | Scalp short 15m: RSI sale fino a 80 e conferma il rientro verso 75. Margine fisso €10, leva paper 15x. |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | Scalp short 15m: RSI sale fino a 75 e conferma il rientro verso 70. Margine fisso €10, leva paper 15x. |
| TEST | Scalp RSI Short 85 · €50 · 15x | Inversione RSI estrema 15m | Scalp short 15m: RSI sale fino a 85 e conferma il rientro verso 80. Margine fisso €50, leva paper 15x. |
| TEST | Scalp RSI Short 80 · €50 · 15x | Inversione RSI estrema 15m | Scalp short 15m: RSI sale fino a 80 e conferma il rientro verso 75. Margine fisso €50, leva paper 15x. |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | Scalp short 15m: RSI sale fino a 75 e conferma il rientro verso 70. Margine fisso €50, leva paper 15x. |
| TEST | Scalp RSI Short 85 · prudente · 5x | Inversione RSI estrema 15m | Scalp short 15m: RSI sale fino a 85 e conferma il rientro verso 80. Versione prudente, leva 5x e rischio ridotto. |
| TEST | Scalp RSI Short 80 · prudente · 5x | Inversione RSI estrema 15m | Scalp short 15m: RSI sale fino a 80 e conferma il rientro verso 75. Versione prudente, leva 5x e rischio ridotto. |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | Scalp short 15m: RSI sale fino a 75 e conferma il rientro verso 70. Versione prudente, leva 5x e rischio ridotto. |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | Benchmark puro: breakout o breakdown dei massimi/minimi delle 20 barre precedenti, con filtro ADX. |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | Benchmark puro: ritorno verso la media dopo uscita dalle Bollinger e conferma RSI estrema. |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | Benchmark puro: trend following con prezzo, EMA20, EMA50 e filtro ADX. |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | Opera long solo sulle cinque crypto più forti della classifica live KuCoin, con conferma tecnica. |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | Opera short solo sulle cinque crypto più deboli della classifica live KuCoin, con conferma tecnica. |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | Top 5 live KuCoin con conferma tecnica e forza relativa positiva contro Bitcoin. |
| TEST | Global Confluence puro 1H | Global Confluence puro | Opera soltanto quando Global Confluence, dati exchange e struttura tecnica sono allineati. |
| TEST | Combo Trend | Combo Trend | Portafoglio sperimentale separato. |
| TEST | Combo Mean Reversion | Combo Mean Reversion | Portafoglio sperimentale separato. |
| TEST | Combo Scanner | Combo Scanner | Portafoglio sperimentale separato. |
| TEST | Combo Adaptive | Combo Adaptive | Portafoglio sperimentale separato. |
| TEST | Combo Adaptive Mfe Trail | Combo Adaptive | Portafoglio sperimentale separato. |
| TEST | Btc Ema 1H | Trend following EMA | Portafoglio sperimentale separato. |
| TEST | Btc Ema 4H | Trend following EMA | Portafoglio sperimentale separato. |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | Portafoglio sperimentale separato. |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | Portafoglio sperimentale separato. |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | Portafoglio sperimentale separato. |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | Portafoglio sperimentale separato. |
| TEST | Btc Adaptive 1H | Combo Adaptive | Portafoglio sperimentale separato. |
| TEST | Btc Adaptive 4H | Combo Adaptive | Portafoglio sperimentale separato. |
| TEST | Sol Ema 1H | Trend following EMA | Portafoglio sperimentale separato. |
| TEST | Sol Ema 4H | Trend following EMA | Portafoglio sperimentale separato. |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | Portafoglio sperimentale separato. |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | Portafoglio sperimentale separato. |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | Portafoglio sperimentale separato. |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | Portafoglio sperimentale separato. |
| TEST | Sol Adaptive 1H | Combo Adaptive | Portafoglio sperimentale separato. |
| TEST | Sol Adaptive 4H | Combo Adaptive | Portafoglio sperimentale separato. |
| TEST | Eth Ema 1H | Trend following EMA | Portafoglio sperimentale separato. |
| TEST | Eth Ema 4H | Trend following EMA | Portafoglio sperimentale separato. |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | Portafoglio sperimentale separato. |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | Portafoglio sperimentale separato. |
| TEST | Eth Adaptive 1H | Combo Adaptive | Portafoglio sperimentale separato. |
| TEST | Doge Ema 1H | Trend following EMA | Portafoglio sperimentale separato. |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | Portafoglio sperimentale separato. |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | Portafoglio sperimentale separato. |

## Confronto risultati

| Tipo | Portafoglio | Strategia | Equity | P&L chiuso | Trade | Eventi indip. | Win rate | PF | Expectancy | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | Confluenza trend | €9.908,56 | €-138,62 | 49 | 49 | 38,78% | 0,90 | €-2,83 | 6,39% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €11.938,79 | €1.814,87 | 89 | 89 | 53,93% | 2,04 | €20,39 | 3,63% |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | Momentum / breakout | €11.698,39 | €1.644,58 | 119 | 119 | 58,82% | 1,74 | €13,82 | 4,41% |
| TEST | Combo Trend Side Regime Guard V1 | Combo Trend | €11.696,40 | €1.558,76 | 90 | 90 | 61,11% | 2,14 | €17,32 | 4,33% |
| TEST | Donchian 1H Gb20 120R V1 | Donchian breakout 20 barre | €11.657,70 | €1.536,70 | 57 | 57 | 56,14% | 2,75 | €26,96 | 3,63% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €11.401,55 | €1.297,78 | 120 | 120 | 51,67% | 1,57 | €10,81 | 8,85% |
| TEST | 1H Fast No Pepe V1 | Momentum / breakout | €11.389,39 | €1.395,91 | 176 | 176 | 52,84% | 1,49 | €7,93 | 4,46% |
| TEST | Combo Adaptive Long Only V1 | Combo Adaptive | €11.141,94 | €1.050,57 | 97 | 97 | 53,61% | 1,58 | €10,83 | 6,25% |
| TEST | Combo Adaptive Side Regime Guard V1 | Combo Adaptive | €11.077,72 | €925,75 | 98 | 98 | 52,04% | 1,57 | €9,45 | 8,68% |
| TEST | Combo Adaptive | Combo Adaptive | €11.053,36 | €928,87 | 129 | 129 | 48,06% | 1,47 | €7,20 | 7,91% |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | Momentum / breakout V3 Filtered | €10.821,44 | €827,31 | 160 | 160 | 53,75% | 1,32 | €5,17 | 9,50% |
| TEST | Main Side Regime Guard V1 | Confluenza trend | €10.791,89 | €792,57 | 33 | 33 | 54,55% | 2,27 | €24,02 | 2,40% |
| TEST | Rapida 1H V3 Filtered | Momentum / breakout V3 Filtered | €10.751,91 | €757,74 | 204 | 204 | 46,57% | 1,21 | €3,71 | 9,48% |
| TEST | 1H Fast V3 No Esports Long Only V1 | Momentum / breakout V3 Filtered | €10.687,48 | €693,06 | 117 | 117 | 48,72% | 1,31 | €5,92 | 10,60% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €10.678,54 | €509,85 | 107 | 107 | 47,66% | 1,23 | €4,76 | 11,27% |
| TEST | Scanner Top5 Btc Tp3 V1 | Scanner Top 5 + forza BTC | €10.671,88 | €565,19 | 87 | 87 | 45,98% | 1,29 | €6,50 | 11,78% |
| TEST | Scanner Top5 Btc Runner25 V1 | Scanner Top 5 + forza BTC | €10.665,63 | €559,01 | 91 | 91 | 46,15% | 1,28 | €6,14 | 12,06% |
| TEST | 1H Fast V3 No Esports V1 | Momentum / breakout V3 Filtered | €10.536,56 | €542,42 | 175 | 175 | 47,43% | 1,17 | €3,10 | 9,00% |
| TEST | 1H Fast Tp2 V1 | Momentum / breakout | €10.535,62 | €494,26 | 187 | 187 | 41,71% | 1,15 | €2,64 | 6,56% |
| TEST | Scanner Top10 Long | Scanner Top10 Long | €10.519,56 | €448,33 | 102 | 102 | 51,96% | 1,25 | €4,40 | 10,31% |
| TEST | Combo Adaptive Partial 1R V1 | Combo Adaptive | €10.437,24 | €403,22 | 128 | 128 | 47,66% | 1,19 | €3,15 | 8,69% |
| TEST | Ampia 4H | Confluenza trend | €10.397,69 | €216,96 | 48 | 48 | 31,25% | 1,19 | €4,52 | 4,45% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €10.397,11 | €391,03 | 41 | 36 | 51,22% | 1,43 | €9,54 | 3,89% |
| TEST | Scanner Top15 Long | Scanner Top15 Long | €10.375,67 | €306,88 | 102 | 102 | 51,96% | 1,17 | €3,01 | 10,31% |
| TEST | Scanner Top20 Long | Scanner Top20 Long | €10.375,67 | €306,88 | 102 | 102 | 51,96% | 1,17 | €3,01 | 10,31% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €10.339,88 | €311,86 | 139 | 139 | 45,32% | 1,11 | €2,24 | 9,12% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | Momentum / breakout V3 Filtered | €10.300,05 | €300,05 | 33 | 33 | 48,48% | 2,04 | €9,09 | 2,01% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €10.271,77 | €204,39 | 5 | 5 | 60,00% | 2,93 | €40,88 | 1,05% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | Momentum / breakout V3 Filtered | €10.271,73 | €271,73 | 22 | 22 | 50,00% | 1,74 | €12,35 | 1,72% |
| TEST | 1H Fast V3 Nohigh Range Only V1 | Momentum / breakout V3 Filtered | €10.247,95 | €247,95 | 41 | 41 | 46,34% | 1,25 | €6,05 | 3,97% |
| TEST | Combo Scanner | Combo Scanner | €10.245,16 | €83,32 | 111 | 111 | 46,85% | 1,03 | €0,75 | 11,38% |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | Momentum / breakout V3 Filtered | €10.239,20 | €239,20 | 17 | 17 | 52,94% | 4,50 | €14,07 | 1,01% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | Momentum / breakout V3 Filtered | €10.235,18 | €235,18 | 20 | 20 | 50,00% | 1,90 | €11,76 | 2,73% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €10.233,65 | €172,08 | 5 | 5 | 60,00% | 2,63 | €34,42 | 1,01% |
| TEST | Main Dynamic Asset Selector V1 | Confluenza trend | €10.213,35 | €213,35 | 12 | 12 | 41,67% | 1,74 | €17,78 | 1,54% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | Momentum / breakout V3 Filtered | €10.185,37 | €185,37 | 22 | 22 | 40,91% | 1,57 | €8,43 | 2,27% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €10.156,88 | €156,88 | 12 | 12 | 50,00% | 1,63 | €13,07 | 2,77% |
| TEST | 1H Fast Score 6 75 Range Only V1 | Momentum / breakout | €10.149,62 | €149,62 | 38 | 38 | 44,74% | 1,14 | €3,94 | 3,35% |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | Momentum / breakout V3 Filtered | €10.145,12 | €145,12 | 44 | 44 | 45,45% | 1,20 | €3,30 | 2,91% |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | Momentum / breakout V3 Filtered | €10.140,84 | €140,84 | 63 | 63 | 44,44% | 1,10 | €2,24 | 5,24% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.138,40 | €138,40 | 5 | 5 | 80,00% | 3,42 | €27,68 | 0,85% |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | Momentum / breakout | €10.126,53 | €126,53 | 40 | 40 | 45,00% | 1,13 | €3,16 | 3,73% |
| TEST | Scanner Top5 Btc Guard V1 | Scanner Top 5 + forza BTC | €10.125,27 | €115,64 | 87 | 87 | 42,53% | 1,06 | €1,33 | 7,34% |
| TEST | Combo Adaptive Quality7 V1 | Combo Adaptive | €10.117,63 | €-17,21 | 67 | 67 | 43,28% | 0,99 | €-0,26 | 8,88% |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | Momentum / breakout V3 Filtered | €10.099,04 | €99,04 | 55 | 55 | 54,55% | 1,12 | €1,80 | 3,59% |
| TEST | Sol Ema 4H | Trend following EMA | €10.098,77 | €32,52 | 6 | 6 | 33,33% | 1,16 | €5,42 | 2,27% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €10.083,25 | €83,25 | 6 | 6 | 66,67% | 1,77 | €13,88 | 1,13% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €10.070,19 | €70,19 | 2 | 2 | 50,00% | 2,39 | €35,09 | 0,96% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €10.067,96 | €67,96 | 8 | 8 | 62,50% | 1,41 | €8,50 | 1,49% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €10.062,05 | €-29,24 | 96 | 91 | 42,71% | 0,99 | €-0,30 | 10,88% |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | Momentum / breakout V3 Filtered | €10.048,77 | €48,77 | 23 | 23 | 43,48% | 1,12 | €2,12 | 3,05% |
| TEST | Rapida 1H V1 | Momentum / breakout | €10.043,28 | €43,28 | 78 | 78 | 34,62% | 1,02 | €0,55 | 6,76% |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | Combo Adaptive | €10.040,56 | €40,78 | 34 | 34 | 50,00% | 1,05 | €1,20 | 4,21% |
| TEST | Sol Ema 1H | Trend following EMA | €10.039,53 | €39,53 | 13 | 13 | 38,46% | 1,10 | €3,04 | 3,33% |
| TEST | 1H Balanced Short Trend Down Strict V1 | Confluenza trend | €10.035,46 | €35,46 | 13 | 13 | 38,46% | 1,13 | €2,73 | 1,80% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.029,45 | €29,45 | 2 | 2 | 50,00% | 1,54 | €14,72 | 0,82% |
| TEST | Scalp RSI Long 20 · prudente · 5x | Inversione RSI estrema 15m | €10.028,67 | €28,67 | 9 | 9 | 55,56% | 1,80 | €3,19 | 0,36% |
| TEST | 1H Fast Nohigh Cap75 V1 | Momentum / breakout | €10.028,66 | €28,66 | 122 | 122 | 43,44% | 1,01 | €0,23 | 7,10% |
| TEST | Btc Ema 4H | Trend following EMA | €10.019,41 | €19,41 | 3 | 3 | 33,33% | 1,19 | €6,47 | 1,76% |
| TEST | Doge Ema 1H | Trend following EMA | €10.018,06 | €18,06 | 15 | 15 | 60,00% | 1,05 | €1,20 | 2,77% |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | Momentum / breakout V3 Filtered | €10.013,82 | €13,82 | 41 | 41 | 48,78% | 1,01 | €0,34 | 4,50% |
| TEST | Scanner Top5 Btc Mfe V1 | Scanner Top 5 + forza BTC | €10.010,60 | €-147,53 | 99 | 99 | 46,46% | 0,93 | €-1,49 | 12,28% |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | Momentum / breakout V3 Filtered | €10.008,92 | €8,92 | 30 | 30 | 36,67% | 1,02 | €0,30 | 4,84% |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | Momentum / breakout V3 Filtered | €10.003,37 | €3,37 | 8 | 8 | 37,50% | 1,02 | €0,42 | 2,15% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €10.002,76 | €3,36 | 27 | 27 | 44,44% | 1,03 | €0,12 | 0,33% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €10.000,55 | €0,67 | 27 | 27 | 44,44% | 1,03 | €0,02 | 0,07% |
| TEST | Scanner Bottom5 Short Continuation V1 | Scanner Bottom5 Short Continuation | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 20 · €10 · 15x | Inversione RSI estrema 15m | €9.999,33 | €-0,67 | 9 | 9 | 44,44% | 0,85 | €-0,07 | 0,04% |
| TEST | Scalp RSI Long 15 · €10 · 15x | Inversione RSI estrema 15m | €9.997,60 | €-2,40 | 3 | 3 | 33,33% | 0,13 | €-0,80 | 0,02% |
| TEST | Scalp RSI Long 20 · €50 · 15x | Inversione RSI estrema 15m | €9.996,64 | €-3,36 | 9 | 9 | 44,44% | 0,85 | €-0,37 | 0,21% |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | Momentum / breakout V3 Filtered | €9.995,23 | €-4,77 | 15 | 15 | 46,67% | 0,99 | €-0,32 | 2,70% |
| TEST | Scalp RSI Short 85 · €10 · 15x | Inversione RSI estrema 15m | €9.995,13 | €-4,75 | 4 | 4 | 50,00% | 0,09 | €-1,19 | 0,06% |
| TEST | Scalp RSI Short 80 · €10 · 15x | Inversione RSI estrema 15m | €9.994,64 | €-5,24 | 14 | 14 | 35,71% | 0,47 | €-0,37 | 0,11% |
| TEST | 1H Fast V3 Long Only V1 | Momentum / breakout V3 Filtered | €9.993,87 | €-51,88 | 133 | 133 | 42,11% | 0,98 | €-0,39 | 12,52% |
| TEST | Scalp RSI Long 25 · €10 · 15x | Inversione RSI estrema 15m | €9.990,45 | €-9,55 | 15 | 15 | 40,00% | 0,36 | €-0,64 | 0,14% |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | €9.988,00 | €-12,00 | 3 | 3 | 33,33% | 0,13 | €-4,00 | 0,12% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €9.987,48 | €-12,52 | 15 | 15 | 40,00% | 0,83 | €-0,83 | 0,71% |
| TEST | Btc Ema 1H | Trend following EMA | €9.987,23 | €-57,80 | 10 | 10 | 40,00% | 0,82 | €-5,78 | 1,94% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €9.981,72 | €-18,28 | 3 | 3 | 33,33% | 0,83 | €-6,09 | 1,22% |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | €9.980,94 | €-19,06 | 3 | 3 | 33,33% | 0,19 | €-6,35 | 0,20% |
| TEST | Scalp RSI Short 85 · prudente · 5x | Inversione RSI estrema 15m | €9.979,50 | €-20,29 | 4 | 4 | 50,00% | 0,08 | €-5,07 | 0,30% |
| TEST | Scalp RSI Short 85 · €50 · 15x | Inversione RSI estrema 15m | €9.975,65 | €-23,75 | 4 | 4 | 50,00% | 0,09 | €-5,94 | 0,31% |
| TEST | Scalp RSI Short 80 · €50 · 15x | Inversione RSI estrema 15m | €9.973,19 | €-26,21 | 14 | 14 | 35,71% | 0,47 | €-1,87 | 0,53% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €9.972,13 | €-26,79 | 8 | 8 | 50,00% | 0,89 | €-3,35 | 1,89% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.971,41 | €-25,65 | 11 | 11 | 45,45% | 0,92 | €-2,33 | 3,14% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €9.965,81 | €-34,19 | 4 | 4 | 25,00% | 0,80 | €-8,55 | 2,43% |
| TEST | Eth Ema 4H | Trend following EMA | €9.964,20 | €-37,26 | 4 | 4 | 25,00% | 0,76 | €-9,32 | 1,83% |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | €9.952,25 | €-47,75 | 15 | 15 | 40,00% | 0,36 | €-3,18 | 0,72% |
| TEST | Scalp RSI Short 80 · prudente · 5x | Inversione RSI estrema 15m | €9.940,59 | €-59,20 | 14 | 14 | 35,71% | 0,32 | €-4,23 | 0,89% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.927,80 | €-71,99 | 27 | 27 | 44,44% | 0,52 | €-2,67 | 0,84% |
| TEST | Eth Ema 1H | Trend following EMA | €9.918,45 | €-78,62 | 15 | 15 | 40,00% | 0,84 | €-5,24 | 4,80% |
| TEST | Combo Adaptive Quality7 Regime V1 | Combo Adaptive | €9.914,27 | €-85,51 | 34 | 34 | 44,12% | 0,90 | €-2,52 | 5,41% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €9.911,95 | €-88,05 | 12 | 12 | 50,00% | 0,75 | €-7,34 | 3,08% |
| TEST | 1H Balanced Long No Rhv V1 | Confluenza trend | €9.908,51 | €-97,90 | 84 | 84 | 48,81% | 0,95 | €-1,17 | 9,26% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €9.896,74 | €-103,26 | 14 | 14 | 35,71% | 0,77 | €-7,38 | 4,59% |
| TEST | Scanner Top5 Btc Guard Mfe V1 | Scanner Top 5 + forza BTC | €9.889,79 | €-119,62 | 104 | 104 | 43,27% | 0,95 | €-1,15 | 8,78% |
| TEST | Combo Adaptive Regime V1 | Combo Adaptive | €9.886,53 | €-113,24 | 48 | 48 | 47,92% | 0,91 | €-2,36 | 5,38% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.884,75 | €-103,61 | 10 | 10 | 30,00% | 0,73 | €-10,36 | 2,63% |
| TEST | Combo Adaptive Mfe Trail | Combo Adaptive | €9.850,81 | €-284,57 | 138 | 138 | 44,20% | 0,89 | €-2,06 | 15,45% |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | Momentum / breakout V3 Filtered | €9.837,38 | €-162,62 | 37 | 37 | 40,54% | 0,76 | €-4,40 | 3,08% |
| TEST | Combo Trend | Combo Trend | €9.821,93 | €-317,97 | 142 | 142 | 40,14% | 0,90 | €-2,24 | 10,85% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | Momentum / breakout V3 Filtered | €9.817,34 | €-182,66 | 24 | 24 | 41,67% | 0,64 | €-7,61 | 3,23% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.801,38 | €-197,17 | 9 | 9 | 33,33% | 0,51 | €-21,91 | 2,37% |
| TEST | 1H Balanced V3 Long Only V1 | Confluenza trend V3 Filtered | €9.779,87 | €-246,63 | 95 | 95 | 46,32% | 0,86 | €-2,60 | 8,85% |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | Momentum / breakout | €9.779,10 | €-220,90 | 86 | 86 | 41,86% | 0,88 | €-2,57 | 7,10% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | Momentum / breakout V3 Filtered | €9.762,18 | €-237,82 | 7 | 7 | 14,29% | 0,02 | €-33,97 | 2,82% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €9.741,78 | €-335,22 | 92 | 85 | 44,57% | 0,83 | €-3,64 | 8,84% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | Momentum / breakout V3 Filtered | €9.723,72 | €-276,28 | 31 | 31 | 32,26% | 0,62 | €-8,91 | 4,83% |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | Scanner Top 5 + forza BTC | €9.711,41 | €-288,59 | 13 | 13 | 23,08% | 0,41 | €-22,20 | 4,35% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €9.642,81 | €-365,67 | 6 | 6 | 16,67% | 0,04 | €-60,94 | 4,16% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.628,04 | €-371,96 | 16 | 16 | 25,00% | 0,32 | €-23,25 | 3,92% |
| TEST | 1H Fast Score 6 75 V1 | Momentum / breakout | €9.626,87 | €-373,13 | 130 | 130 | 41,54% | 0,89 | €-2,87 | 10,36% |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | Scanner Top 5 + forza BTC | €9.595,22 | €-404,43 | 58 | 58 | 39,66% | 0,78 | €-6,97 | 7,74% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | Momentum / breakout V3 Filtered | €9.579,83 | €-420,17 | 11 | 11 | 0,00% | 0,00 | €-38,20 | 4,20% |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | Momentum / breakout V3 Filtered | €9.517,55 | €-482,45 | 78 | 78 | 39,74% | 0,78 | €-6,19 | 6,59% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.469,38 | €-610,71 | 110 | 110 | 38,18% | 0,72 | €-5,55 | 12,31% |
| TEST | 1H Fast V3 Nohigh V1 | Momentum / breakout V3 Filtered | €9.435,38 | €-564,62 | 112 | 112 | 40,18% | 0,79 | €-5,04 | 6,91% |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | Scanner Top 5 + forza BTC | €9.430,59 | €-569,07 | 73 | 73 | 39,73% | 0,73 | €-7,80 | 7,02% |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | Momentum / breakout V3 Filtered | €9.389,68 | €-610,32 | 83 | 83 | 44,58% | 0,76 | €-7,35 | 7,69% |
| TEST | Scanner Bottom10 Short | Scanner Bottom10 Short | €9.385,05 | €-613,68 | 67 | 67 | 32,84% | 0,67 | €-9,16 | 8,28% |
| TEST | Scanner Bottom15 Short | Scanner Bottom15 Short | €9.385,05 | €-613,68 | 67 | 67 | 32,84% | 0,67 | €-9,16 | 8,28% |
| TEST | Scanner Bottom20 Short | Scanner Bottom20 Short | €9.385,05 | €-613,68 | 67 | 67 | 32,84% | 0,67 | €-9,16 | 8,28% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €9.378,18 | €-621,78 | 51 | 51 | 31,37% | 0,66 | €-12,19 | 8,18% |
| TEST | Master Adaptive Gb20 Be V1 | Master Adaptive Consensus | €9.372,49 | €-627,51 | 55 | 55 | 29,09% | 0,62 | €-11,41 | 8,39% |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | Momentum / breakout | €9.370,91 | €-629,09 | 88 | 88 | 43,18% | 0,78 | €-7,15 | 10,68% |
| TEST | Master Adaptive Gb20 Partial V1 | Master Adaptive Consensus | €9.362,52 | €-637,48 | 50 | 50 | 34,00% | 0,60 | €-12,75 | 7,98% |
| TEST | 1H Fast V3 Cap75 V1 | Momentum / breakout V3 Filtered | €9.355,17 | €-644,83 | 126 | 126 | 38,10% | 0,80 | €-5,12 | 11,75% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €9.354,60 | €-645,40 | 58 | 58 | 34,48% | 0,67 | €-11,13 | 7,26% |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | €9.326,30 | €-673,70 | 52 | 52 | 32,69% | 0,62 | €-12,96 | 7,80% |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | Scanner Bottom 5 Short | €9.320,02 | €-678,72 | 58 | 58 | 32,76% | 0,60 | €-11,70 | 8,30% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €9.319,82 | €-679,95 | 61 | 61 | 34,43% | 0,66 | €-11,15 | 7,96% |
| TEST | Scanner Bottom5 Short Profit Lock V1 | Scanner Bottom 5 Short | €9.305,85 | €-692,90 | 59 | 59 | 32,20% | 0,58 | €-11,74 | 8,30% |
| TEST | Master Adaptive Gb20 Loss Cap V1 | Master Adaptive Consensus | €9.252,08 | €-747,69 | 42 | 42 | 23,81% | 0,53 | €-17,80 | 11,41% |
| TEST | Scanner Top5 Btc Btc Le3 V1 | Scanner Top 5 + forza BTC | €9.237,05 | €-762,95 | 59 | 59 | 33,90% | 0,57 | €-12,93 | 11,72% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.234,23 | €-764,52 | 86 | 86 | 32,56% | 0,66 | €-8,89 | 9,40% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €9.202,39 | €-797,61 | 87 | 87 | 48,28% | 0,60 | €-9,17 | 9,02% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €9.150,69 | €-849,31 | 121 | 121 | 36,36% | 0,69 | €-7,02 | 13,99% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €9.114,32 | €-885,68 | 38 | 38 | 36,84% | 0,48 | €-23,31 | 10,65% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €9.056,84 | €-943,16 | 53 | 53 | 28,30% | 0,59 | €-17,80 | 11,51% |
| TEST | Combo Adaptive Runner25 V1 | Combo Adaptive | €8.964,11 | €-1.035,89 | 94 | 94 | 30,85% | 0,53 | €-11,02 | 12,67% |
| TEST | Combo Adaptive Tp3 V1 | Combo Adaptive | €8.796,64 | €-1.203,36 | 75 | 75 | 29,33% | 0,38 | €-16,04 | 12,67% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €8.740,52 | €-1.259,48 | 81 | 81 | 38,27% | 0,55 | €-15,55 | 14,60% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €8.445,51 | €-1.554,49 | 105 | 105 | 27,62% | 0,47 | €-14,80 | 17,39% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | SPCX | LONG | Confluenza trend | 240m | 3,0x | 136,56189 | 136,56189 | 128,79610 | 91,72407 | 152,09346 | €285,50 | €856,50 | €48,71 | €0,00 |
| Principale 4H | VELVET | LONG | Confluenza trend | 240m | 3,0x | 0,55987 | 0,55987 | 0,49269 | 0,37605 | 0,69424 | €131,08 | €393,24 | €47,19 | €0,00 |
| Principale 4H | EDEN | LONG | Confluenza trend | 240m | 3,0x | 0,06195 | 0,06195 | 0,05451 | 0,04161 | 0,07681 | €130,34 | €391,02 | €46,92 | €0,00 |
| Principale 4H | HYPE | LONG | Confluenza trend | 240m | 3,0x | 76,47929 | 81,62700 | 71,48477 | 51,36859 | 86,46833 | €10,44 | €31,32 | €2,05 | €2,11 |
| Principale 4H | ETH | LONG | Confluenza trend | 240m | 3,0x | 2509,93189 | 2515,13000 | 2395,33490 | 1685,83758 | 2739,12586 | €19,82 | €59,45 | €2,71 | €0,12 |
| Principale 4H | XRP | LONG | Confluenza trend | 240m | 3,0x | 1,56312 | 1,67216 | 1,44655 | 1,04990 | 1,79626 | €220,42 | €661,27 | €49,31 | €46,13 |
| 1H Balanced Long No Rhv V1 | SKHYNIX | LONG | Confluenza trend | 60m | 3,0x | 1214,11277 | 1214,11277 | 1170,18211 | 815,47908 | 1301,97411 | €413,43 | €1.240,28 | €44,88 | €0,00 |
| 1H Balanced Long No Rhv V1 | BOME | LONG | Confluenza trend | 60m | 3,0x | 0,00129 | 0,00129 | 0,00114 | 0,00087 | 0,00160 | €134,98 | €404,95 | €48,59 | €0,00 |
| 1H Balanced Long No Rhv V1 | LINK | LONG | Confluenza trend | 60m | 3,0x | 12,23945 | 12,46900 | 11,85665 | 8,22083 | 13,00504 | €43,30 | €129,89 | €4,06 | €2,44 |
| 1H Balanced Long No Rhv V1 | HYPE | LONG | Confluenza trend | 60m | 3,0x | 81,25625 | 81,62700 | 78,03969 | 54,57711 | 87,68937 | €416,12 | €1.248,35 | €49,42 | €5,70 |
| 1H Balanced Long No Rhv V1 | SUI | LONG | Confluenza trend | 60m | 3,0x | 0,91318 | 0,93920 | 0,91318 | 0,61335 | 0,98923 | €11,03 | €33,10 | €0,00 | €0,94 |
| 1H Balanced Long No Rhv V1 | TAO | LONG | Confluenza trend | 60m | 3,0x | 247,38947 | 247,38947 | 237,94346 | 166,16326 | 266,28148 | €428,20 | €1.284,61 | €49,05 | €0,00 |
| Bilanciata 1H V2 | SKHYNIX | LONG | Confluenza trend V2 | 60m | 3,0x | 1214,11277 | 1214,11277 | 1170,18211 | 815,47908 | 1301,97411 | €422,38 | €1.267,15 | €45,85 | €0,00 |
| Bilanciata 1H V2 | ETH | LONG | Confluenza trend V2 | 60m | 3,0x | 2424,26476 | 2515,13000 | 2481,29397 | 1628,29783 | 2536,04729 | €690,68 | €2.072,04 | €0,00 | €77,66 |
| Bilanciata 1H V2 | LINK | LONG | Confluenza trend V2 | 60m | 3,0x | 12,04941 | 12,46900 | 12,15501 | 8,09319 | 12,82965 | €9,69 | €29,06 | €0,00 | €1,01 |
| Bilanciata 1H V2 | HYPE | LONG | Confluenza trend V2 | 60m | 3,0x | 81,25625 | 81,62700 | 78,03969 | 54,57711 | 87,68937 | €51,94 | €155,82 | €6,17 | €0,71 |
| Bilanciata 1H V3 Filtered | BEAT | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,25480 | 0,25480 | 0,25418 | 0,33846 | 0,19365 | €137,63 | €412,88 | €0,00 | €-0,00 |
| Bilanciata 1H V3 Filtered | SKHYNIX | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1220,85412 | 1220,85412 | 1177,63561 | 820,00702 | 1307,29117 | €460,42 | €1.381,27 | €48,90 | €0,00 |
| Bilanciata 1H V3 Filtered | LINK | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 12,23945 | 12,46900 | 11,85665 | 8,22083 | 13,00504 | €546,46 | €1.639,38 | €51,27 | €30,75 |
| Bilanciata 1H V3 Filtered | ENA | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,16026 | 0,16023 | 0,14912 | 0,10764 | 0,18254 | €247,96 | €743,89 | €51,70 | €-0,15 |
| Bilanciata 1H V3 Filtered | PEPE | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €28,31 | €84,92 | €5,38 | €-0,02 |
| 1H Fast Score 6 75 Cost Aware V1 | SKHYNIX | LONG | Momentum / breakout | 60m | 3,0x | 1220,85412 | 1220,85412 | 1187,23972 | 820,00702 | 1271,27573 | €624,93 | €1.874,80 | €51,62 | €0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | BTW | LONG | Momentum / breakout | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €8,91 | €26,72 | €3,13 | €0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00086 | 0,00146 | €215,92 | €647,76 | €57,03 | €0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | LINK | LONG | Momentum / breakout | 60m | 3,0x | 12,16543 | 12,46900 | 12,20252 | 8,17112 | 12,62042 | €771,34 | €2.314,02 | €0,00 | €57,74 |
| 1H Fast Score 6 75 Cost Aware V1 | NEAR | LONG | Momentum / breakout | 60m | 3,0x | 2,08142 | 2,08142 | 2,02315 | 1,39802 | 2,16882 | €42,86 | €128,59 | €3,60 | €0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | ENA | LONG | Momentum / breakout | 60m | 3,0x | 0,16026 | 0,16023 | 0,15160 | 0,10764 | 0,17326 | €360,70 | €1.082,11 | €58,50 | €-0,22 |
| 1H Fast Score 6 75 Cost Aware V1 | SOL | LONG | Momentum / breakout | 60m | 3,0x | 99,31486 | 99,29500 | 96,80711 | 66,70648 | 103,07649 | €31,62 | €94,86 | €2,40 | €-0,02 |
| 1H Fast No Pepe V1 | SKHYNIX | LONG | Momentum / breakout | 60m | 3,0x | 1213,43264 | 1213,43264 | 1179,70743 | 815,02226 | 1264,02045 | €33,31 | €99,94 | €2,78 | €0,00 |
| 1H Fast No Pepe V1 | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €172,22 | €516,67 | €49,86 | €0,00 |
| 1H Fast No Pepe V1 | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 81,73234 | 81,62700 | 79,21443 | 54,89689 | 85,50921 | €608,50 | €1.825,51 | €56,24 | €-2,35 |
| 1H Fast No Pepe V1 | TAO | LONG | Momentum / breakout | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €47,93 | €143,78 | €4,27 | €0,00 |
| 1H Fast No Pepe V1 | SUI | LONG | Momentum / breakout | 60m | 3,0x | 0,93939 | 0,93920 | 0,90768 | 0,63096 | 0,98696 | €562,42 | €1.687,26 | €56,96 | €-0,34 |
| 1H Fast No Pepe V1 | ADA | LONG | Momentum / breakout | 60m | 3,0x | 0,25509 | 0,25504 | 0,24572 | 0,17134 | 0,26915 | €516,62 | €1.549,87 | €56,95 | €-0,31 |
| 1H Fast No Pepe V1 | SOL | LONG | Momentum / breakout | 60m | 3,0x | 99,31486 | 99,29500 | 96,80711 | 66,70648 | 103,07649 | €9,65 | €28,96 | €0,73 | €-0,01 |
| 1H Fast Tp2 V1 | SOXL | SHORT | Momentum / breakout | 60m | 3,0x | 121,01735 | 121,01735 | 127,15573 | 160,75137 | 108,74057 | €315,49 | €946,48 | €48,01 | €-0,00 |
| 1H Fast Tp2 V1 | SKHYNIX | LONG | Momentum / breakout | 60m | 3,0x | 1204,83092 | 1204,83092 | 1170,97389 | 809,24477 | 1272,54496 | €18,91 | €56,74 | €1,59 | €0,00 |
| 1H Fast Tp2 V1 | BTW | LONG | Momentum / breakout | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,56752 | €142,85 | €428,56 | €50,25 | €0,00 |
| 1H Fast Tp2 V1 | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00132 | 0,00132 | 0,00119 | 0,00088 | 0,00158 | €18,87 | €56,62 | €5,59 | €0,00 |
| 1H Fast Tp2 V1 | LINK | LONG | Momentum / breakout | 60m | 3,0x | 12,16543 | 12,46900 | 12,20252 | 8,17112 | 12,77208 | €623,94 | €1.871,81 | €0,00 | €46,71 |
| 1H Fast Tp2 V1 | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 81,73234 | 81,62700 | 79,21443 | 54,89689 | 86,76817 | €567,22 | €1.701,67 | €52,42 | €-2,19 |
| 1H Fast Tp2 V1 | XRP | LONG | Momentum / breakout | 60m | 3,0x | 1,67249 | 1,67216 | 1,60414 | 1,12336 | 1,80920 | €50,41 | €151,24 | €6,18 | €-0,03 |
| Rapida 1H V2 | SOXL | SHORT | Momentum / breakout V2 | 60m | 3,0x | 121,15726 | 121,15726 | 127,13595 | 160,93723 | 112,18923 | €333,06 | €999,18 | €49,31 | €-0,00 |
| Rapida 1H V2 | HYPE | LONG | Momentum / breakout V2 | 60m | 3,0x | 81,25625 | 81,62700 | 78,75448 | 54,57711 | 85,00890 | €561,80 | €1.685,41 | €51,89 | €7,69 |
| Rapida 1H V3 Filtered | SKHYNIX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1220,85412 | 1220,85412 | 1187,23972 | 820,00702 | 1271,27573 | €21,81 | €65,43 | €1,80 | €0,00 |
| Rapida 1H V3 Filtered | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €172,00 | €515,99 | €49,79 | €0,00 |
| Rapida 1H V3 Filtered | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 81,73234 | 81,62700 | 79,21443 | 54,89689 | 85,50921 | €578,88 | €1.736,64 | €53,50 | €-2,24 |
| Rapida 1H V3 Filtered | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €589,98 | €1.769,95 | €52,56 | €0,00 |
| Rapida 1H V3 Filtered | XRP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,67249 | 1,67216 | 1,60414 | 1,12336 | 1,77503 | €438,51 | €1.315,52 | €53,77 | €-0,26 |
| Rapida 1H V3 Filtered | SUI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,93939 | 0,93920 | 0,90768 | 0,63096 | 0,98696 | €35,72 | €107,15 | €3,62 | €-0,02 |
| 1H Fast V3 Long Only V1 | BTW | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €126,57 | €379,72 | €44,52 | €0,00 |
| 1H Fast V3 Long Only V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00147 | €9,56 | €28,69 | €2,66 | €0,00 |
| 1H Fast V3 Long Only V1 | LINK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 12,16543 | 12,46900 | 12,20252 | 8,17112 | 12,62042 | €649,56 | €1.948,68 | €0,00 | €48,63 |
| 1H Fast V3 Long Only V1 | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 81,25625 | 81,62700 | 78,75448 | 54,57711 | 85,00890 | €59,15 | €177,44 | €5,46 | €0,81 |
| 1H Fast V3 Long Only V1 | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €554,42 | €1.663,26 | €49,39 | €0,00 |
| 1H Fast V3 Long Only V1 | SUI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,93939 | 0,93920 | 0,90768 | 0,63096 | 0,98696 | €486,52 | €1.459,56 | €49,27 | €-0,29 |
| 1H Fast V3 No Esports V1 | SKHYNIX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1220,85412 | 1220,85412 | 1187,23972 | 820,00702 | 1271,27573 | €18,11 | €54,34 | €1,50 | €0,00 |
| 1H Fast V3 No Esports V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €169,36 | €508,09 | €49,03 | €0,00 |
| 1H Fast V3 No Esports V1 | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 81,73234 | 81,62700 | 79,21443 | 54,89689 | 85,50921 | €563,48 | €1.690,45 | €52,08 | €-2,18 |
| 1H Fast V3 No Esports V1 | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €27,04 | €81,13 | €2,41 | €0,00 |
| 1H Fast V3 No Esports V1 | XRP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,67249 | 1,67216 | 1,60414 | 1,12336 | 1,77503 | €429,77 | €1.289,31 | €52,69 | €-0,26 |
| 1H Fast V3 No Esports V1 | SUI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,93939 | 0,93920 | 0,90768 | 0,63096 | 0,98696 | €520,25 | €1.560,75 | €52,69 | €-0,31 |
| 1H Fast V3 No Esports Long Only V1 | BTW | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €132,94 | €398,81 | €46,76 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00147 | €10,06 | €30,18 | €2,80 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 81,73234 | 81,62700 | 79,21443 | 54,89689 | 85,50921 | €560,36 | €1.681,09 | €51,79 | €-2,17 |
| 1H Fast V3 No Esports Long Only V1 | SUI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,93939 | 0,93920 | 0,90768 | 0,63096 | 0,98696 | €527,74 | €1.583,23 | €53,45 | €-0,32 |
| 1H Fast V3 No Esports Long Only V1 | ENA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16026 | 0,16023 | 0,15160 | 0,10764 | 0,17326 | €329,54 | €988,61 | €53,44 | €-0,20 |
| 1H Fast V3 No Esports Long Only V1 | PEPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €37,28 | €111,84 | €5,51 | €-0,02 |
| 1H Fast V3 No Esports Mfe Lock V1 | SKHYNIX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1220,85412 | 1220,85412 | 1187,23972 | 820,00702 | 1271,27573 | €21,95 | €65,86 | €1,81 | €0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €173,11 | €519,32 | €50,11 | €0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 81,73234 | 81,62700 | 79,21443 | 54,89689 | 85,50921 | €582,62 | €1.747,87 | €53,85 | €-2,25 |
| 1H Fast V3 No Esports Mfe Lock V1 | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €593,79 | €1.781,38 | €52,90 | €0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | XRP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,67249 | 1,67216 | 1,60414 | 1,12336 | 1,77503 | €441,34 | €1.324,02 | €54,11 | €-0,26 |
| 1H Fast V3 No Esports Mfe Lock V1 | SUI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,93939 | 0,93920 | 0,90768 | 0,63096 | 0,98696 | €35,95 | €107,84 | €3,64 | €-0,02 |
| Ampia 4H | SPCX | LONG | Confluenza trend | 240m | 2,0x | 136,56189 | 136,56189 | 126,46637 | 68,96375 | 164,82935 | €323,86 | €647,73 | €47,88 | €0,00 |
| Ampia 4H | VELVET | LONG | Confluenza trend | 240m | 2,0x | 0,55987 | 0,55987 | 0,49269 | 0,28274 | 0,74799 | €201,63 | €403,26 | €48,39 | €0,00 |
| Ampia 4H | ETH | LONG | Confluenza trend | 240m | 2,0x | 2258,11153 | 2515,13000 | 2438,47896 | 1140,34632 | 2576,63943 | €502,94 | €1.005,89 | €0,00 | €114,49 |
| Ampia 4H | HYPE | LONG | Confluenza trend | 240m | 2,0x | 71,99640 | 81,62700 | 77,25612 | 36,35818 | 87,88866 | €16,69 | €33,38 | €0,00 | €4,47 |
| Ampia 4H | ZEC | LONG | Confluenza trend | 240m | 2,0x | 738,20761 | 822,51000 | 764,71329 | 372,79484 | 932,87076 | €274,02 | €548,05 | €0,00 | €62,59 |
| Ampia 4H | LINK | LONG | Confluenza trend | 240m | 2,0x | 11,96839 | 12,46900 | 11,08055 | 6,04404 | 14,45436 | €14,07 | €28,15 | €2,09 | €1,18 |
| Forza relativa 1H V2 | BEAT | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,25984 | 0,25984 | 0,25657 | 0,38847 | 0,19125 | €200,38 | €400,75 | €0,00 | €-0,00 |
| Forza relativa 1H V2 | ENA | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,14320 | 0,16023 | 0,15076 | 0,07232 | 0,16554 | €348,56 | €697,12 | €0,00 | €82,91 |
| Forza relativa 1H V2 | LINK | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 12,04941 | 12,46900 | 12,13258 | 6,08495 | 12,90767 | €59,04 | €118,08 | €0,00 | €4,11 |
| Forza relativa 1H V2 | HYPE | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 81,25625 | 81,62700 | 78,03969 | 41,03441 | 88,33268 | €630,31 | €1.260,61 | €49,90 | €5,75 |
| Scalp RSI Short 85 · €10 · 15x | SOL | SHORT | Inversione RSI estrema 15m | 15m | 15,0x | 99,27514 | 99,29500 | 103,04694 | 105,39711 | 93,61744 | €10,00 | €150,00 | €5,70 | €-0,03 |
| Scalp RSI Short 80 · €10 · 15x | SOL | SHORT | Inversione RSI estrema 15m | 15m | 15,0x | 99,27514 | 99,29500 | 103,04694 | 105,39711 | 93,61744 | €10,00 | €150,00 | €5,70 | €-0,03 |
| Scalp RSI Short 75 · €10 · 15x | SOL | SHORT | Inversione RSI estrema 15m | 15m | 15,0x | 99,27514 | 99,29500 | 103,04694 | 105,39711 | 93,61744 | €10,00 | €150,00 | €5,70 | €-0,03 |
| Scalp RSI Short 85 · €50 · 15x | SOL | SHORT | Inversione RSI estrema 15m | 15m | 15,0x | 99,27514 | 99,29500 | 103,04694 | 105,39711 | 93,61744 | €50,00 | €750,00 | €28,50 | €-0,15 |
| Scalp RSI Short 80 · €50 · 15x | SOL | SHORT | Inversione RSI estrema 15m | 15m | 15,0x | 99,27514 | 99,29500 | 103,04694 | 105,39711 | 93,61744 | €50,00 | €750,00 | €28,50 | €-0,15 |
| Scalp RSI Short 75 · €50 · 15x | SOL | SHORT | Inversione RSI estrema 15m | 15m | 15,0x | 99,27514 | 99,29500 | 103,04694 | 105,39711 | 93,61744 | €50,00 | €750,00 | €28,50 | €-0,15 |
| Scalp RSI Short 85 · prudente · 5x | SOL | SHORT | Inversione RSI estrema 15m | 15m | 5,0x | 99,27514 | 99,29500 | 103,04694 | 118,63379 | 91,73154 | €52,53 | €262,67 | €9,98 | €-0,05 |
| Scalp RSI Short 80 · prudente · 5x | SOL | SHORT | Inversione RSI estrema 15m | 15m | 5,0x | 99,27514 | 99,29500 | 103,04694 | 118,63379 | 91,73154 | €52,33 | €261,65 | €9,94 | €-0,05 |
| Scalp RSI Short 75 · prudente · 5x | SOL | SHORT | Inversione RSI estrema 15m | 15m | 5,0x | 99,27514 | 99,29500 | 103,04694 | 118,63379 | 91,73154 | €52,26 | €261,31 | €9,93 | €-0,05 |
| Benchmark Donchian breakout 1H | SKHYNIX | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1174,33482 | 1174,33482 | 1128,44989 | 593,03908 | 1289,04713 | €641,25 | €1.282,50 | €50,11 | €0,00 |
| Benchmark Donchian breakout 1H | ETH | LONG | Donchian breakout 20 barre | 60m | 2,0x | 2527,10532 | 2515,13000 | 2455,44799 | 1276,18819 | 2706,24863 | €1.023,39 | €2.046,77 | €58,04 | €-9,70 |
| Benchmark Donchian breakout 1H | ADA | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,24139 | 0,25504 | 0,24541 | 0,12190 | 0,26988 | €624,55 | €1.249,09 | €0,00 | €70,64 |
| Benchmark Donchian breakout 1H | SOL | LONG | Donchian breakout 20 barre | 60m | 2,0x | 96,15423 | 99,29500 | 97,02348 | 48,55788 | 103,02819 | €1.013,85 | €2.027,70 | €0,00 | €66,23 |
| Benchmark Donchian breakout 1H | DOGE | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,09885 | 0,09883 | 0,09401 | 0,04992 | 0,11095 | €139,52 | €279,03 | €13,67 | €-0,06 |
| Donchian 1H Gb20 120R V1 | SKHYNIX | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1174,33482 | 1174,33482 | 1128,44989 | 593,03908 | 1289,04713 | €626,15 | €1.252,30 | €48,93 | €0,00 |
| Donchian 1H Gb20 120R V1 | ETH | LONG | Donchian breakout 20 barre | 60m | 2,0x | 2527,10532 | 2515,13000 | 2455,44799 | 1276,18819 | 2706,24863 | €999,29 | €1.998,58 | €56,67 | €-9,47 |
| Donchian 1H Gb20 120R V1 | ADA | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,24139 | 0,25504 | 0,24541 | 0,12190 | 0,26988 | €609,84 | €1.219,68 | €0,00 | €68,98 |
| Donchian 1H Gb20 120R V1 | SOL | LONG | Donchian breakout 20 barre | 60m | 2,0x | 96,15423 | 99,29500 | 97,02348 | 48,55788 | 103,02819 | €989,98 | €1.979,96 | €0,00 | €64,67 |
| Donchian 1H Gb20 120R V1 | DOGE | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,09885 | 0,09883 | 0,09401 | 0,04992 | 0,11095 | €136,23 | €272,46 | €13,34 | €-0,05 |
| Benchmark trend following EMA 1H | BEAT | SHORT | Trend following EMA | 60m | 2,0x | 0,28257 | 0,28257 | 0,25706 | 0,42244 | 0,20797 | €186,11 | €372,23 | €0,00 | €-0,00 |
| Benchmark trend following EMA 1H | ETH | LONG | Trend following EMA | 60m | 2,0x | 2396,47920 | 2515,13000 | 2474,82250 | 1210,22200 | 2540,53801 | €28,74 | €57,48 | €0,00 | €2,85 |
| Benchmark trend following EMA 1H | BTC | LONG | Trend following EMA | 60m | 2,0x | 76719,31079 | 78450,74000 | 74671,22818 | 38743,25195 | 81225,09269 | €833,14 | €1.666,28 | €44,48 | €37,61 |
| Benchmark trend following EMA 1H | ENA | LONG | Trend following EMA | 60m | 2,0x | 0,14122 | 0,16023 | 0,14959 | 0,07132 | 0,16872 | €12,82 | €25,65 | €0,00 | €3,45 |
| Benchmark trend following EMA 1H | LINK | LONG | Trend following EMA | 60m | 2,0x | 12,11942 | 12,46900 | 12,12605 | 6,12031 | 13,09722 | €12,84 | €25,68 | €0,00 | €0,74 |
| Benchmark trend following EMA 1H | DOGE | LONG | Trend following EMA | 60m | 2,0x | 0,09541 | 0,09883 | 0,09554 | 0,04818 | 0,10474 | €529,56 | €1.059,13 | €0,00 | €37,98 |
| Benchmark trend following EMA 1H | SUI | LONG | Trend following EMA | 60m | 2,0x | 0,92699 | 0,93920 | 0,88400 | 0,46813 | 1,02155 | €13,49 | €26,97 | €1,25 | €0,36 |
| Benchmark trend following EMA 1H | XRP | LONG | Trend following EMA | 60m | 2,0x | 1,67249 | 1,67216 | 1,57484 | 0,84461 | 1,88732 | €403,71 | €807,43 | €47,14 | €-0,16 |
| Scanner Top 5 Long 1H | BOME | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00160 | €218,24 | €436,47 | €52,38 | €0,00 |
| Scanner Top 5 Long 1H | ENA | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,14324 | 0,16023 | 0,15064 | 0,07234 | 0,16528 | €355,74 | €711,48 | €0,00 | €84,40 |
| Scanner Top 5 Long 1H | XRP | LONG | Scanner Top 5 Long | 60m | 2,0x | 1,56312 | 1,67216 | 1,60787 | 0,78938 | 1,71766 | €154,42 | €308,83 | €0,00 | €21,54 |
| Scanner Top 5 Long 1H | ZEC | LONG | Scanner Top 5 Long | 60m | 2,0x | 822,67450 | 822,51000 | 767,21555 | 415,45062 | 933,59241 | €422,87 | €845,75 | €57,01 | €-0,17 |
| Scanner Top 5 Long 1H | PEPE | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €383,86 | €767,72 | €48,65 | €-0,15 |
| Scanner Bottom 5 Short 1H | BEAT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,28257 | 0,28257 | 0,25514 | 0,42244 | 0,21475 | €200,95 | €401,89 | €0,00 | €-0,00 |
| Scanner Bottom 5 Short 1H | SOXL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €378,86 | €757,72 | €48,07 | €-0,00 |
| Scanner Bottom 5 Short 1H | SNDK | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €492,80 | €985,60 | €47,71 | €-0,00 |
| Scanner Top10 Long | LINK | LONG | Scanner Top10 Long | 60m | 2,0x | 12,11942 | 12,46900 | 12,14891 | 6,12031 | 12,91944 | €13,86 | €27,72 | €0,00 | €0,80 |
| Scanner Top10 Long | ETH | LONG | Scanner Top10 Long | 60m | 2,0x | 2510,43199 | 2515,13000 | 2447,53198 | 1267,76815 | 2636,23199 | €23,39 | €46,79 | €1,17 | €0,09 |
| Scanner Top10 Long | XRP | LONG | Scanner Top10 Long | 60m | 2,0x | 1,56312 | 1,67216 | 1,60787 | 0,78938 | 1,71766 | €524,07 | €1.048,14 | €0,00 | €73,11 |
| Scanner Top10 Long | TAO | LONG | Scanner Top10 Long | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €678,43 | €1.356,86 | €51,81 | €0,00 |
| Scanner Top10 Long | ZEC | LONG | Scanner Top10 Long | 60m | 2,0x | 822,67450 | 822,51000 | 767,21555 | 415,45062 | 933,59241 | €390,16 | €780,33 | €52,60 | €-0,16 |
| Scanner Top10 Long | PEPE | LONG | Scanner Top10 Long | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €411,04 | €822,07 | €52,09 | €-0,16 |
| Scanner Bottom10 Short | BEAT | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,28257 | 0,28257 | 0,25514 | 0,42244 | 0,21475 | €204,24 | €408,48 | €0,00 | €-0,00 |
| Scanner Bottom10 Short | SOXL | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom10 Short | SNDK | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Top15 Long | BTC | LONG | Scanner Top15 Long | 60m | 2,0x | 76719,31079 | 78450,74000 | 76984,72631 | 38743,25195 | 80405,85934 | €20,59 | €41,19 | €0,00 | €0,93 |
| Scanner Top15 Long | NEAR | LONG | Scanner Top15 Long | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €16,79 | €33,59 | €1,21 | €0,00 |
| Scanner Top15 Long | HYPE | LONG | Scanner Top15 Long | 60m | 2,0x | 81,73234 | 81,62700 | 78,49502 | 41,27483 | 88,20698 | €646,42 | €1.292,84 | €51,21 | €-1,67 |
| Scanner Top15 Long | XRP | LONG | Scanner Top15 Long | 60m | 2,0x | 1,56312 | 1,67216 | 1,60787 | 0,78938 | 1,71766 | €517,90 | €1.035,79 | €0,00 | €72,25 |
| Scanner Top15 Long | TAO | LONG | Scanner Top15 Long | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €88,53 | €177,07 | €6,76 | €0,00 |
| Scanner Top15 Long | ZEC | LONG | Scanner Top15 Long | 60m | 2,0x | 822,67450 | 822,51000 | 767,21555 | 415,45062 | 933,59241 | €384,82 | €769,65 | €51,88 | €-0,15 |
| Scanner Top15 Long | PEPE | LONG | Scanner Top15 Long | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €349,33 | €698,65 | €44,27 | €-0,14 |
| Scanner Bottom15 Short | BEAT | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,28257 | 0,28257 | 0,25514 | 0,42244 | 0,21475 | €204,24 | €408,48 | €0,00 | €-0,00 |
| Scanner Bottom15 Short | SOXL | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom15 Short | SNDK | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Top20 Long | BTC | LONG | Scanner Top20 Long | 60m | 2,0x | 76719,31079 | 78450,74000 | 76984,72631 | 38743,25195 | 80405,85934 | €20,59 | €41,19 | €0,00 | €0,93 |
| Scanner Top20 Long | NEAR | LONG | Scanner Top20 Long | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €16,79 | €33,59 | €1,21 | €0,00 |
| Scanner Top20 Long | HYPE | LONG | Scanner Top20 Long | 60m | 2,0x | 81,73234 | 81,62700 | 78,49502 | 41,27483 | 88,20698 | €646,42 | €1.292,84 | €51,21 | €-1,67 |
| Scanner Top20 Long | XRP | LONG | Scanner Top20 Long | 60m | 2,0x | 1,56312 | 1,67216 | 1,60787 | 0,78938 | 1,71766 | €517,90 | €1.035,79 | €0,00 | €72,25 |
| Scanner Top20 Long | TAO | LONG | Scanner Top20 Long | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €88,53 | €177,07 | €6,76 | €0,00 |
| Scanner Top20 Long | ZEC | LONG | Scanner Top20 Long | 60m | 2,0x | 822,67450 | 822,51000 | 767,21555 | 415,45062 | 933,59241 | €384,82 | €769,65 | €51,88 | €-0,15 |
| Scanner Top20 Long | PEPE | LONG | Scanner Top20 Long | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €349,33 | €698,65 | €44,27 | €-0,14 |
| Scanner Bottom20 Short | BEAT | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,28257 | 0,28257 | 0,25514 | 0,42244 | 0,21475 | €204,24 | €408,48 | €0,00 | €-0,00 |
| Scanner Bottom20 Short | SOXL | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom20 Short | SNDK | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Top 5 + forza BTC 1H | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €203,45 | €406,91 | €48,83 | €0,00 |
| Scanner Top 5 + forza BTC 1H | ENA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,13881 | 0,16023 | 0,14991 | 0,07010 | 0,16409 | €311,03 | €622,07 | €0,00 | €96,00 |
| Scanner Top 5 + forza BTC 1H | XRP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,56312 | 1,67216 | 1,60787 | 0,78938 | 1,73312 | €535,48 | €1.070,95 | €0,00 | €74,71 |
| Scanner Top 5 + forza BTC 1H | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 822,67450 | 822,51000 | 767,21555 | 415,45062 | 944,68421 | €396,04 | €792,08 | €53,40 | €-0,16 |
| Scanner Top 5 + forza BTC 1H | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €54,41 | €108,83 | €6,90 | €-0,02 |
| Scanner Top5 Btc Mfe V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €190,73 | €381,46 | €45,77 | €0,00 |
| Scanner Top5 Btc Mfe V1 | ENA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,13881 | 0,16023 | 0,14991 | 0,07010 | 0,16409 | €291,58 | €583,16 | €0,00 | €90,00 |
| Scanner Top5 Btc Mfe V1 | XRP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,56312 | 1,67216 | 1,60787 | 0,78938 | 1,73312 | €501,98 | €1.003,96 | €0,00 | €70,03 |
| Scanner Top5 Btc Mfe V1 | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 822,67450 | 822,51000 | 767,21555 | 415,45062 | 944,68421 | €371,27 | €742,53 | €50,06 | €-0,15 |
| Scanner Top5 Btc Mfe V1 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €51,01 | €102,02 | €6,46 | €-0,02 |
| Scanner Top5 Btc Guard V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01279 | €196,77 | €393,54 | €47,23 | €0,00 |
| Scanner Top5 Btc Guard V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €197,27 | €394,55 | €47,35 | €0,00 |
| Scanner Top5 Btc Guard V1 | ENA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,14324 | 0,16023 | 0,15064 | 0,07234 | 0,16748 | €13,92 | €27,84 | €0,00 | €3,30 |
| Scanner Top5 Btc Guard V1 | XRP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,56312 | 1,67216 | 1,60787 | 0,78938 | 1,73312 | €60,94 | €121,88 | €0,00 | €8,50 |
| Scanner Top5 Btc Guard V1 | DOGE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,09885 | 0,09883 | 0,09449 | 0,04992 | 0,10844 | €574,38 | €1.148,75 | €50,63 | €-0,23 |
| Scanner Top5 Btc Guard V1 | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 822,67450 | 822,51000 | 767,21555 | 415,45062 | 944,68421 | €364,51 | €729,02 | €49,15 | €-0,15 |
| Scanner Top5 Btc Guard Mfe V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01279 | €192,20 | €384,39 | €46,13 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €192,69 | €385,37 | €46,24 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | ENA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,14324 | 0,16023 | 0,15064 | 0,07234 | 0,16748 | €13,59 | €27,19 | €0,00 | €3,23 |
| Scanner Top5 Btc Guard Mfe V1 | XRP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,56312 | 1,67216 | 1,60787 | 0,78938 | 1,73312 | €59,52 | €119,05 | €0,00 | €8,30 |
| Scanner Top5 Btc Guard Mfe V1 | DOGE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,09885 | 0,09883 | 0,09449 | 0,04992 | 0,10844 | €561,02 | €1.122,04 | €49,46 | €-0,22 |
| Scanner Top5 Btc Guard Mfe V1 | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 822,67450 | 822,51000 | 767,21555 | 415,45062 | 944,68421 | €356,03 | €712,07 | €48,00 | €-0,14 |
| Scanner Top5 Btc Guard Btc Le3 V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01279 | €199,19 | €398,38 | €47,81 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01279 | €195,77 | €391,54 | €46,99 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00176 | €210,95 | €421,90 | €50,63 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | ENA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,13881 | 0,16023 | 0,14991 | 0,07010 | 0,17329 | €293,50 | €587,01 | €0,00 | €90,59 |
| Scanner Top5 Btc Runner25 V1 | DOGE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,09222 | 0,09883 | 0,09613 | 0,04657 | 0,10194 | €40,59 | €81,17 | €0,00 | €5,82 |
| Scanner Top5 Btc Runner25 V1 | SUI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,86527 | 0,93920 | 0,91071 | 0,43696 | 0,96652 | €63,34 | €126,67 | €0,00 | €10,82 |
| Scanner Top5 Btc Runner25 V1 | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 818,21361 | 822,51000 | 764,43439 | 413,19787 | 979,55127 | €17,50 | €35,00 | €2,30 | €0,18 |
| Scanner Top5 Btc Tp3 V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00176 | €211,07 | €422,14 | €50,66 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | ENA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,13881 | 0,16023 | 0,14991 | 0,07010 | 0,17329 | €293,67 | €587,35 | €0,00 | €90,65 |
| Scanner Top5 Btc Tp3 V1 | DOGE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,09222 | 0,09883 | 0,09613 | 0,04657 | 0,10194 | €40,61 | €81,22 | €0,00 | €5,82 |
| Scanner Top5 Btc Tp3 V1 | SUI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,86527 | 0,93920 | 0,91071 | 0,43696 | 0,96652 | €63,37 | €126,75 | €0,00 | €10,83 |
| Scanner Top5 Btc Tp3 V1 | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 818,21361 | 822,51000 | 764,43439 | 413,19787 | 979,55127 | €17,51 | €35,02 | €2,30 | €0,18 |
| Combo Trend | BEAT | SHORT | Combo Trend | 60m | 2,0x | 0,25984 | 0,25984 | 0,25657 | 0,38847 | 0,19125 | €193,71 | €387,42 | €0,00 | €-0,00 |
| Combo Trend | ETH | LONG | Combo Trend | 60m | 2,0x | 2409,96190 | 2515,13000 | 2476,15639 | 1217,03076 | 2551,09900 | €853,83 | €1.707,65 | €0,00 | €74,52 |
| Combo Trend | LINK | LONG | Combo Trend | 60m | 2,0x | 12,23945 | 12,46900 | 11,81412 | 6,18092 | 13,17517 | €38,36 | €76,72 | €2,67 | €1,44 |
| Combo Trend | DOGE | LONG | Combo Trend | 60m | 2,0x | 0,09382 | 0,09883 | 0,09583 | 0,04738 | 0,10217 | €588,05 | €1.176,11 | €0,00 | €62,82 |
| Combo Trend | ENA | LONG | Combo Trend | 60m | 2,0x | 0,15019 | 0,16023 | 0,15131 | 0,07585 | 0,17472 | €33,09 | €66,18 | €0,00 | €4,42 |
| Combo Trend | SOL | LONG | Combo Trend | 60m | 2,0x | 99,31486 | 99,29500 | 95,73235 | 50,15400 | 107,19637 | €680,79 | €1.361,58 | €49,12 | €-0,27 |
| Combo Scanner | BOME | LONG | Combo Scanner | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €195,20 | €390,40 | €46,85 | €0,00 |
| Combo Scanner | ENA | LONG | Combo Scanner | 60m | 2,0x | 0,13881 | 0,16023 | 0,14991 | 0,07010 | 0,16409 | €298,41 | €596,82 | €0,00 | €92,11 |
| Combo Scanner | XRP | LONG | Combo Scanner | 60m | 2,0x | 1,56312 | 1,67216 | 1,60787 | 0,78938 | 1,73312 | €513,74 | €1.027,49 | €0,00 | €71,67 |
| Combo Scanner | ZEC | LONG | Combo Scanner | 60m | 2,0x | 822,67450 | 822,51000 | 767,21555 | 415,45062 | 944,68421 | €379,97 | €759,93 | €51,23 | €-0,15 |
| Combo Scanner | PEPE | LONG | Combo Scanner | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €52,20 | €104,41 | €6,62 | €-0,02 |
| Combo Adaptive | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,01735 | 121,01735 | 128,90956 | 180,92093 | 105,23292 | €367,30 | €734,61 | €47,91 | €-0,00 |
| Combo Adaptive | LINK | LONG | Combo Adaptive | 60m | 2,0x | 12,23945 | 12,46900 | 11,85665 | 6,18092 | 13,00504 | €55,31 | €110,62 | €3,46 | €2,07 |
| Combo Adaptive | ETH | LONG | Combo Adaptive | 60m | 2,0x | 2526,20514 | 2515,13000 | 2461,52067 | 1275,73360 | 2655,57408 | €13,07 | €26,15 | €0,67 | €-0,11 |
| Combo Adaptive | ADA | LONG | Combo Adaptive | 60m | 2,0x | 0,24533 | 0,25504 | 0,24691 | 0,12389 | 0,26698 | €618,16 | €1.236,31 | €0,00 | €48,94 |
| Combo Adaptive | XRP | LONG | Combo Adaptive | 60m | 2,0x | 1,56312 | 1,67216 | 1,61246 | 0,78938 | 1,71766 | €551,63 | €1.103,26 | €0,00 | €76,96 |
| Combo Adaptive | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €40,89 | €81,77 | €3,12 | €0,00 |
| Combo Adaptive | SOL | LONG | Combo Adaptive | 60m | 2,0x | 99,31486 | 99,29500 | 96,09061 | 50,15400 | 105,76337 | €851,28 | €1.702,57 | €55,27 | €-0,34 |
| Combo Adaptive | SUI | LONG | Combo Adaptive | 60m | 2,0x | 0,93939 | 0,93920 | 0,89861 | 0,47439 | 1,02093 | €17,91 | €35,82 | €1,55 | €-0,01 |
| Combo Adaptive Mfe Trail | LINK | LONG | Combo Adaptive | 60m | 2,0x | 12,23945 | 12,46900 | 12,25413 | 6,18092 | 13,00504 | €65,32 | €130,63 | €0,00 | €2,45 |
| Combo Adaptive Mfe Trail | DOGE | LONG | Combo Adaptive | 60m | 2,0x | 0,09382 | 0,09883 | 0,09783 | 0,04738 | 0,10065 | €637,16 | €1.274,32 | €0,00 | €68,07 |
| Combo Adaptive Mfe Trail | XRP | LONG | Combo Adaptive | 60m | 2,0x | 1,56312 | 1,67216 | 1,62966 | 0,78938 | 1,71766 | €490,26 | €980,52 | €0,00 | €68,40 |
| Combo Adaptive Mfe Trail | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €54,29 | €108,58 | €4,15 | €0,00 |
| Combo Adaptive Mfe Trail | SOL | LONG | Combo Adaptive | 60m | 2,0x | 99,31486 | 99,29500 | 96,09061 | 50,15400 | 105,76337 | €758,73 | €1.517,46 | €49,26 | €-0,30 |
| Combo Adaptive Mfe Trail | SUI | LONG | Combo Adaptive | 60m | 2,0x | 0,93939 | 0,93920 | 0,89861 | 0,47439 | 1,02093 | €514,57 | €1.029,15 | €44,67 | €-0,21 |
| Combo Adaptive Quality7 V1 | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €371,68 | €743,36 | €47,16 | €-0,00 |
| Combo Adaptive Quality7 V1 | LINK | LONG | Combo Adaptive | 60m | 2,0x | 12,16543 | 12,46900 | 12,18031 | 6,14354 | 12,94540 | €13,73 | €27,46 | €0,00 | €0,69 |
| Combo Adaptive Quality7 V1 | ADA | LONG | Combo Adaptive | 60m | 2,0x | 0,24139 | 0,25504 | 0,24721 | 0,12190 | 0,26191 | €585,67 | €1.171,34 | €0,00 | €66,24 |
| Combo Adaptive Quality7 V1 | XRP | LONG | Combo Adaptive | 60m | 2,0x | 1,56312 | 1,67216 | 1,61246 | 0,78938 | 1,71766 | €505,70 | €1.011,40 | €0,00 | €70,55 |
| Combo Adaptive Quality7 V1 | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €646,78 | €1.293,57 | €49,39 | €0,00 |
| Combo Adaptive Quality7 V1 | SUI | LONG | Combo Adaptive | 60m | 2,0x | 0,93939 | 0,93920 | 0,89861 | 0,47439 | 1,02093 | €59,24 | €118,48 | €5,14 | €-0,02 |
| Combo Adaptive Regime V1 | CYS | SHORT | Combo Adaptive | 60m | 2,0x | 0,73555 | 0,73555 | 0,73555 | 1,09965 | 0,55902 | €202,91 | €405,83 | €0,00 | €-0,00 |
| Combo Adaptive Quality7 Regime V1 | CYS | SHORT | Combo Adaptive | 60m | 2,0x | 0,73555 | 0,73555 | 0,73555 | 1,09965 | 0,55902 | €199,19 | €398,38 | €0,00 | €-0,00 |
| Combo Adaptive Long Only V1 | LINK | LONG | Combo Adaptive | 60m | 2,0x | 12,23945 | 12,46900 | 11,85665 | 6,18092 | 13,00504 | €39,66 | €79,32 | €2,48 | €1,49 |
| Combo Adaptive Long Only V1 | DOGE | LONG | Combo Adaptive | 60m | 2,0x | 0,09382 | 0,09883 | 0,09623 | 0,04738 | 0,10065 | €31,85 | €63,70 | €0,00 | €3,40 |
| Combo Adaptive Long Only V1 | ETH | LONG | Combo Adaptive | 60m | 2,0x | 2510,43199 | 2515,13000 | 2447,53198 | 1267,76815 | 2636,23199 | €53,51 | €107,02 | €2,68 | €0,20 |
| Combo Adaptive Long Only V1 | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €645,48 | €1.290,95 | €46,47 | €0,00 |
| Combo Adaptive Long Only V1 | SUI | LONG | Combo Adaptive | 60m | 2,0x | 0,92699 | 0,93920 | 0,88830 | 0,46813 | 1,00436 | €659,97 | €1.319,94 | €55,08 | €17,39 |
| Combo Adaptive Long Only V1 | XRP | LONG | Combo Adaptive | 60m | 2,0x | 1,56312 | 1,67216 | 1,61246 | 0,78938 | 1,71766 | €520,95 | €1.041,89 | €0,00 | €72,68 |
| Combo Adaptive Long Only V1 | SOL | LONG | Combo Adaptive | 60m | 2,0x | 99,31486 | 99,29500 | 96,09061 | 50,15400 | 105,76337 | €858,11 | €1.716,22 | €55,72 | €-0,34 |
| Combo Adaptive Long Only V1 | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 822,67450 | 822,51000 | 767,21555 | 415,45062 | 933,59241 | €48,86 | €97,72 | €6,59 | €-0,02 |
| Combo Adaptive Partial 1R V1 | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,01735 | 121,01735 | 128,90956 | 180,92093 | 105,23292 | €352,70 | €705,40 | €46,00 | €-0,00 |
| Combo Adaptive Partial 1R V1 | LINK | LONG | Combo Adaptive | 60m | 2,0x | 12,23945 | 12,46900 | 11,85665 | 6,18092 | 13,00504 | €817,60 | €1.635,20 | €51,14 | €30,67 |
| Combo Adaptive Partial 1R V1 | SUI | LONG | Combo Adaptive | 60m | 2,0x | 0,91318 | 0,93920 | 0,91318 | 0,46116 | 0,98923 | €44,50 | €89,00 | €0,00 | €2,54 |
| Combo Adaptive Partial 1R V1 | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 818,21361 | 822,51000 | 764,43439 | 413,19787 | 925,77205 | €390,17 | €780,34 | €51,29 | €4,10 |
| Combo Adaptive Partial 1R V1 | SOL | LONG | Combo Adaptive | 60m | 2,0x | 99,31486 | 99,29500 | 96,09061 | 50,15400 | 105,76337 | €803,84 | €1.607,67 | €52,19 | €-0,32 |
| Combo Adaptive Partial 1R V1 | XRP | LONG | Combo Adaptive | 60m | 2,0x | 1,67249 | 1,67216 | 1,58461 | 0,84461 | 1,84826 | €41,98 | €83,96 | €4,41 | €-0,02 |
| Combo Adaptive Quality7 Regime Partial 1R V1 | CYS | SHORT | Combo Adaptive | 60m | 2,0x | 0,73555 | 0,73555 | 0,73555 | 1,09965 | 0,55902 | €201,73 | €403,45 | €0,00 | €-0,00 |
| Btc Ema 1H | BTC | LONG | Trend following EMA | 60m | 3,0x | 76719,31079 | 78450,74000 | 77194,15684 | 51529,80375 | 80405,85934 | €689,68 | €2.069,03 | €0,00 | €46,69 |
| Sol Ema 4H | SOL | LONG | Trend following EMA | 240m | 2,0x | 93,69974 | 99,29500 | 96,26431 | 47,31837 | 104,18607 | €560,28 | €1.120,56 | €0,00 | €66,91 |
| Sol Donchian 4H | SOL | LONG | Donchian breakout 20 barre | 240m | 2,0x | 93,69974 | 99,29500 | 96,26431 | 47,31837 | 105,44443 | €569,88 | €1.139,76 | €0,00 | €68,06 |
| Sol Bollinger 1H | SOL | SHORT | Bollinger mean reversion | 60m | 3,0x | 99,27514 | 99,29500 | 101,96094 | 131,87048 | 95,24644 | €603,90 | €1.811,71 | €49,01 | €-0,36 |
| Sol Adaptive 4H | SOL | LONG | Combo Adaptive | 240m | 2,0x | 93,69974 | 99,29500 | 96,26431 | 47,31837 | 105,13937 | €520,73 | €1.041,47 | €0,00 | €62,19 |
| Eth Ema 1H | ETH | LONG | Trend following EMA | 60m | 3,0x | 2517,44339 | 2515,13000 | 2452,69072 | 1690,88281 | 2646,94876 | €642,87 | €1.928,61 | €49,61 | €-1,77 |
| Eth Ema 4H | ETH | LONG | Trend following EMA | 240m | 2,0x | 2509,93189 | 2515,13000 | 2383,87520 | 1267,51560 | 2825,07361 | €495,92 | €991,85 | €49,81 | €2,05 |
| Eth Donchian 1H | ETH | LONG | Donchian breakout 20 barre | 60m | 3,0x | 2527,10532 | 2515,13000 | 2469,77945 | 1697,37241 | 2641,75703 | €727,11 | €2.181,32 | €49,48 | €-10,34 |
| Eth Bollinger 1H | ETH | SHORT | Bollinger mean reversion | 60m | 3,0x | 2526,09468 | 2515,13000 | 2579,81618 | 3355,49577 | 2445,51244 | €755,04 | €2.265,13 | €48,17 | €9,83 |
| Eth Adaptive 1H | ETH | LONG | Combo Adaptive | 60m | 3,0x | 2517,44339 | 2515,13000 | 2452,69072 | 1690,88281 | 2646,94876 | €646,30 | €1.938,91 | €49,87 | €-1,78 |
| Doge Bollinger 1H | DOGE | SHORT | Bollinger mean reversion | 60m | 3,0x | 0,09881 | 0,09883 | 0,10244 | 0,13125 | 0,09337 | €452,53 | €1.357,60 | €49,87 | €-0,27 |
| Master Adaptive Expanded V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03814 | 0,02188 | 0,05374 | €197,50 | €395,01 | €47,40 | €0,00 |
| Master Adaptive Runner25 V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03814 | 0,02188 | 0,05894 | €34,77 | €69,54 | €8,34 | €0,00 |
| Combo Adaptive Side Regime Guard V1 | LINK | LONG | Combo Adaptive | 60m | 2,0x | 12,23945 | 12,46900 | 11,85665 | 6,18092 | 13,00504 | €838,31 | €1.676,62 | €52,44 | €31,45 |
| Combo Adaptive Side Regime Guard V1 | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €77,52 | €155,04 | €5,58 | €0,00 |
| Combo Adaptive Side Regime Guard V1 | ADA | LONG | Combo Adaptive | 60m | 2,0x | 0,24533 | 0,25504 | 0,24691 | 0,12389 | 0,26698 | €618,04 | €1.236,07 | €0,00 | €48,93 |
| Combo Adaptive Side Regime Guard V1 | XRP | LONG | Combo Adaptive | 60m | 2,0x | 1,56312 | 1,67216 | 1,61246 | 0,78938 | 1,71766 | €540,86 | €1.081,72 | €0,00 | €75,46 |
| Combo Adaptive Side Regime Guard V1 | SOL | LONG | Combo Adaptive | 60m | 2,0x | 99,31486 | 99,29500 | 96,09061 | 50,15400 | 105,76337 | €853,16 | €1.706,31 | €55,40 | €-0,34 |
| Master Adaptive Gb20 Loss Cap V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03828 | 0,02188 | 0,05682 | €195,70 | €391,41 | €45,67 | €0,00 |
| Main Side Regime Guard V1 | VELVET | LONG | Confluenza trend | 240m | 3,0x | 0,55987 | 0,55987 | 0,49269 | 0,37605 | 0,69424 | €142,25 | €426,74 | €51,21 | €0,00 |
| Main Side Regime Guard V1 | AKE | LONG | Confluenza trend | 240m | 3,0x | 0,01021 | 0,01021 | 0,00899 | 0,00686 | 0,01266 | €145,97 | €437,90 | €52,55 | €0,00 |
| Combo Trend Side Regime Guard V1 | ETH | LONG | Combo Trend | 60m | 2,0x | 2409,96190 | 2515,13000 | 2476,15639 | 1217,03076 | 2551,09900 | €1.041,25 | €2.082,50 | €0,00 | €90,88 |
| Combo Trend Side Regime Guard V1 | LINK | LONG | Combo Trend | 60m | 2,0x | 12,04941 | 12,46900 | 12,13258 | 6,08495 | 13,00303 | €23,07 | €46,14 | €0,00 | €1,61 |
| Combo Trend Side Regime Guard V1 | SUI | LONG | Combo Trend | 60m | 2,0x | 0,91318 | 0,93920 | 0,87093 | 0,46116 | 1,00613 | €38,14 | €76,28 | €3,53 | €2,17 |
| Combo Trend Side Regime Guard V1 | ADA | LONG | Combo Trend | 60m | 2,0x | 0,24533 | 0,25504 | 0,24566 | 0,12389 | 0,27179 | €589,06 | €1.178,11 | €0,00 | €46,63 |
| Combo Trend Side Regime Guard V1 | XRP | LONG | Combo Trend | 60m | 2,0x | 1,67249 | 1,67216 | 1,57484 | 0,84461 | 1,88732 | €500,88 | €1.001,77 | €58,49 | €-0,20 |
| Combo Trend Side Regime Guard V1 | ZEC | LONG | Combo Trend | 60m | 2,0x | 822,67450 | 822,51000 | 761,05343 | 415,45062 | 958,24084 | €381,00 | €762,00 | €57,08 | €-0,15 |
| 1H Balanced V3 Long Only V1 | BEAT | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,25480 | 0,25480 | 0,25418 | 0,33846 | 0,19365 | €130,17 | €390,52 | €0,00 | €-0,00 |
| 1H Balanced V3 Long Only V1 | SKHYNIX | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1220,85412 | 1220,85412 | 1177,63561 | 820,00702 | 1307,29117 | €435,49 | €1.306,46 | €46,25 | €0,00 |
| 1H Balanced V3 Long Only V1 | LINK | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 12,23945 | 12,46900 | 11,85665 | 8,22083 | 13,00504 | €516,86 | €1.550,59 | €48,50 | €29,08 |
| 1H Balanced V3 Long Only V1 | ENA | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,16026 | 0,16023 | 0,14912 | 0,10764 | 0,18254 | €234,53 | €703,60 | €48,90 | €-0,14 |
| 1H Balanced V3 Long Only V1 | PEPE | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €26,77 | €80,32 | €5,09 | €-0,02 |
| Scanner Bottom5 Short Profit Lock V1 | BEAT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,28257 | 0,28257 | 0,25514 | 0,42244 | 0,21475 | €202,51 | €405,01 | €0,00 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | SOXL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €381,80 | €763,60 | €48,45 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | SNDK | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €496,62 | €993,25 | €48,08 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | BEAT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,28257 | 0,28257 | 0,25514 | 0,42244 | 0,21475 | €202,81 | €405,63 | €0,00 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | SOXL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €382,38 | €764,76 | €48,52 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | SNDK | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €497,38 | €994,76 | €48,15 | €-0,00 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Sol Ema 1H | SOL | LONG | 2026-08-22T05:07:22+00:00 | 98,56217 | €96,54 | 1,94 | TARGET |
| Sol Donchian 1H | SOL | LONG | 2026-08-22T05:07:22+00:00 | 98,04492 | €97,32 | 1,93 | TARGET |
| Sol Adaptive 1H | SOL | LONG | 2026-08-22T05:07:22+00:00 | 98,56217 | €95,17 | 1,94 | TARGET |
| Scanner Top 5 Long 1H | DOGE | LONG | 2026-08-22T05:07:22+00:00 | 0,09868 | €94,57 | 1,96 | TARGET |
| Scanner Top 5 Long 1H | SUI | LONG | 2026-08-22T05:07:22+00:00 | 0,93258 | €109,06 | 1,96 | TARGET |
| Scanner Top5 Btc Tp3 V1 | PEPE | LONG | 2026-08-22T05:07:22+00:00 | 0,00000 | €151,87 | 2,97 | TARGET |
| Scanner Top5 Btc Tp3 V1 | XRP | LONG | 2026-08-22T05:07:22+00:00 | 1,59503 | €151,15 | 2,96 | TARGET |
| Scanner Top5 Btc Runner25 V1 | XRP | LONG | 2026-08-22T05:07:22+00:00 | 1,59503 | €151,07 | 2,96 | TARGET |
| Scanner Top5 Btc Runner25 V1 | PEPE | LONG | 2026-08-22T05:07:22+00:00 | 0,00000 | €151,78 | 2,97 | TARGET |
| Scanner Top5 Btc Mfe V1 | DOGE | LONG | 2026-08-22T05:07:22+00:00 | 0,09933 | €7,51 | 2,16 | TARGET |
| Scanner Top5 Btc Mfe V1 | SUI | LONG | 2026-08-22T05:07:22+00:00 | 0,93933 | €5,81 | 2,16 | TARGET |
| Scanner Top5 Btc Guard V1 | PEPE | LONG | 2026-08-22T05:07:22+00:00 | 0,00000 | €106,46 | 2,17 | TARGET |

## Regole invarianti

- Nessuna martingala e nessuna mediazione automatica in perdita.
- Il target mensile riduce il rischio quando viene avvicinato o raggiunto; non lo aumenta mai.
- Il portafoglio principale e le simulazioni di confronto hanno contabilità separata.
- Commissioni, slippage e funding sono inclusi nella simulazione secondo i parametri configurati.
- Quando stop e target risultano toccati nella stessa candela, prevale lo stop salvo modifica esplicita della configurazione.
