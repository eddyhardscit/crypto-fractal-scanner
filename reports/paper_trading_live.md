# Paper trading automatico KuCoin

Generato: 2026-08-21T05:32:52+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-08-21T05:05:28+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-08-21T05:05:28+00:00 | 2026-08-21T05:05:28+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-08-21T04:45:00+00:00 | 2026-08-21T04:45:00+00:00 | 5,6 min | 25,0 min | OK |
| 60m | 12 | 2026-08-21T04:00:00+00:00 | 2026-08-21T04:00:00+00:00 | 5,6 min | 45,0 min | OK |
| 240m | 12 | 2026-08-21T00:00:00+00:00 | 2026-08-21T00:00:00+00:00 | 1,09 h | 1,00 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Combo Trend Side Regime Guard V1 | ENA | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive Side Regime Guard V1 | ENA | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive Long Only V1 | ENA | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive Quality7 V1 | ENA | 60m | LONG | 7,75 | 7,00 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive Mfe Trail | ENA | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top5 Btc Tp3 V1 | ENA | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top5 Btc Runner25 V1 | ENA | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top5 Btc Guard Mfe V1 | ENA | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top5 Btc Guard V1 | ENA | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 No Esports Mfe Lock V1 | ENA | 60m | LONG | 7,75 | 4,50 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 No Esports V1 | ENA | 60m | LONG | 7,75 | 4,50 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Score 6 75 Cost Aware V1 | XRP | 60m | LONG | 6,25 | 6,00 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Principale 4H | BOME | 240m | LONG | 8,25 | 6,00 | 0,00 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | BTW | 240m | LONG | 7,75 | 6,00 | 0,00 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | ENA | 240m | LONG | 7,75 | 6,00 | 0,00 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | HYPE | 240m | LONG | 6,56 | 6,00 | 0,00 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | XRP | 240m | LONG | 6,25 | 6,00 | 0,00 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | ETH | 240m | LONG | 5,50 | 6,00 | 0,50 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | ADA | 240m | LONG | 5,07 | 6,00 | 0,93 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | SOL | 240m | LONG | 4,99 | 6,00 | 1,01 | STALE_CANDLE | 1,09 h | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | PEPE | 240m | LONG | 4,94 | 6,00 | 1,06 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | BTC | 240m | LONG | 4,75 | 6,00 | 1,25 | STALE_CANDLE | 1,09 h | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | ZEC | 240m | LONG | 4,29 | 6,00 | 1,71 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | DOGE | 240m | LONG | 2,25 | 6,00 | 3,75 | STALE_CANDLE | 1,09 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| 1H Balanced Long No Rhv V1 | BOME | 60m | LONG | 7,75 | 5,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Benchmark trend following EMA 1H | BOME | 60m | LONG | 7,75 | 5,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Combo Trend | BOME | 60m | LONG | 7,75 | 5,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Combo Adaptive Quality7 V1 | BOME | 60m | LONG | 7,75 | 7,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Balanced Long No Rhv V1 | ENA | 60m | LONG | 7,75 | 5,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Fast No Pepe V1 | ENA | 60m | LONG | 7,75 | 4,50 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Tp2 V1 | ENA | 60m | LONG | 7,75 | 4,50 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida 1H V3 Filtered | ENA | 60m | LONG | 7,75 | 4,50 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.715,38 | -2,85% | €-32,97 | €3.000,00 | -1,10% | 5 | 46 | 34,78% | 0,76 | 6,39% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 46 | 1818 | PRIME INDICAZIONI | 100 (mancano 54) |

- Trade del Principale 4H chiusi: **46**; win rate **34,78%**; profit factor **0,76**.
- Expectancy: **€-7,25** per trade; P&L netto: **€-333,55**; max drawdown: **6,39%**.
- Valutazione: **Si può osservare la direzione, ma il risultato resta fragile.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 5 | €9.715,38 | €979,58 | €2.938,74 | €144,97 | €50,80 |
| TEST | Benchmark Donchian breakout 1H | 6 | €11.103,69 | €3.892,32 | €7.784,65 | €167,38 | €133,86 |
| TEST | Donchian 1H Gb20 120R V1 | 6 | €10.842,27 | €3.800,68 | €7.601,36 | €163,44 | €130,71 |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | 6 | €10.802,41 | €3.506,79 | €10.520,36 | €162,98 | €54,80 |
| TEST | Combo Trend Side Regime Guard V1 | 8 | €10.744,90 | €2.237,24 | €4.474,49 | €107,49 | €158,90 |
| TEST | Scanner Top 5 Long 1H | 7 | €10.565,59 | €2.073,05 | €4.146,10 | €151,80 | €104,59 |
| TEST | Main Side Regime Guard V1 | 4 | €10.491,38 | €721,94 | €2.165,83 | €208,62 | €15,37 |
| TEST | 1H Fast No Pepe V1 | 9 | €10.400,20 | €2.598,70 | €7.796,10 | €106,62 | €102,50 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 0 | €10.300,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 0 | €10.271,73 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Nohigh Range Only V1 | 0 | €10.247,95 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 0 | €10.239,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 0 | €10.235,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Main Dynamic Asset Selector V1 | 0 | €10.213,35 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 0 | €10.185,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Side Regime Guard V1 | 7 | €10.179,84 | €2.219,42 | €4.438,83 | €103,95 | €125,56 |
| TEST | Combo Adaptive | 7 | €10.167,39 | €1.919,17 | €3.838,34 | €102,75 | €166,26 |
| TEST | 1H Fast Score 6 75 Range Only V1 | 0 | €10.149,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 0 | €10.145,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | 0 | €10.140,84 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 1H | 0 | €10.138,40 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Long Only V1 | 7 | €10.131,57 | €2.671,57 | €5.343,15 | €99,47 | €147,96 |
| TEST | Sol Donchian 4H | 1 | €10.130,32 | €727,07 | €1.454,13 | €0,00 | €65,29 |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | 0 | €10.126,53 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 4H | 1 | €10.107,65 | €665,34 | €1.330,67 | €0,00 | €59,75 |
| TEST | Ampia 4H | 6 | €10.102,33 | €1.636,79 | €3.273,57 | €153,31 | €43,90 |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 0 | €10.099,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 1H | 0 | €10.083,25 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 4H | 0 | €10.070,19 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 1H | 0 | €10.067,96 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 0 | €10.048,77 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Bollinger 1H | 0 | €10.046,94 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V1 | 0 | €10.043,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Tp2 V1 | 9 | €10.035,93 | €877,84 | €2.633,53 | €198,82 | €-9,40 |
| TEST | 1H Balanced Short Trend Down Strict V1 | 0 | €10.035,46 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 4H | 0 | €10.029,45 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Nohigh Cap75 V1 | 1 | €10.029,22 | €155,86 | €467,58 | €51,44 | €0,00 |
| TEST | Scalp RSI Long 20 · prudente · 5x | 0 | €10.028,67 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 1 | €10.022,40 | €50,00 | €750,00 | €8,72 | €-1,65 |
| TEST | Sol Donchian 1H | 1 | €10.022,21 | €937,37 | €2.812,11 | €0,00 | €59,96 |
| TEST | Btc Ema 4H | 0 | €10.019,41 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | 0 | €10.013,82 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 0 | €10.008,92 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 1 | €10.004,48 | €10,00 | €150,00 | €1,74 | €-0,33 |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 0 | €10.003,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €50 · 15x | 0 | €10.001,42 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €10 · 15x | 0 | €10.000,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Continuation V1 | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · prudente · 5x | 0 | €9.999,47 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €10 · 15x | 0 | €9.999,33 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €10 · 15x | 0 | €9.997,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €50 · 15x | 0 | €9.996,64 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 0 | €9.995,23 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €10 · 15x | 0 | €9.994,76 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €10 · 15x | 0 | €9.990,45 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €50 · 15x | 0 | €9.988,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 0 | €9.987,48 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H V3 Filtered | 6 | €9.983,99 | €1.329,18 | €3.987,53 | €100,07 | €80,28 |
| TEST | Sol Bollinger 4H | 0 | €9.981,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · prudente · 5x | 0 | €9.980,94 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 4H | 1 | €9.974,31 | €715,87 | €1.431,74 | €0,00 | €64,29 |
| TEST | Scalp RSI Short 80 · €50 · 15x | 0 | €9.973,79 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 4H | 0 | €9.965,81 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €50 · 15x | 0 | €9.952,25 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V2 | 1 | €9.951,64 | €333,06 | €999,18 | €49,31 | €0,00 |
| TEST | Eth Donchian 1H | 0 | €9.949,57 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 1 | €9.947,73 | €171,19 | €855,93 | €9,95 | €-1,88 |
| TEST | Btc Ema 1H | 0 | €9.942,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · prudente · 5x | 0 | €9.940,80 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Ema 1H | 0 | €9.920,90 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top 5 + forza BTC 1H | 6 | €9.900,93 | €2.728,82 | €5.457,64 | €147,98 | €115,78 |
| TEST | Sol Ema 1H | 1 | €9.899,48 | €823,54 | €2.470,62 | €0,00 | €52,68 |
| TEST | Sol Bollinger 1H | 0 | €9.892,99 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Ema 4H | 1 | €9.887,99 | €577,20 | €1.154,41 | €0,00 | €47,03 |
| TEST | Eth Adaptive 1H | 0 | €9.878,92 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 0 | €9.837,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Tp3 V1 | 9 | €9.826,58 | €2.441,58 | €4.883,17 | €58,16 | €227,03 |
| TEST | Scanner Top5 Btc Runner25 V1 | 9 | €9.820,83 | €2.440,16 | €4.880,31 | €58,12 | €226,90 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 0 | €9.817,34 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Donchian 1H | 0 | €9.816,06 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | 9 | €9.813,01 | €1.808,45 | €5.425,34 | €146,75 | €38,43 |
| TEST | Eth Ema 1H | 1 | €9.793,37 | €563,60 | €1.690,79 | €0,00 | €62,97 |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | 1 | €9.779,65 | €151,98 | €455,94 | €50,16 | €0,00 |
| TEST | Combo Adaptive Partial 1R V1 | 7 | €9.767,15 | €1.864,76 | €3.729,52 | €96,61 | €160,28 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 0 | €9.762,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 1H | 1 | €9.758,68 | €811,83 | €2.435,48 | €0,00 | €51,93 |
| TEST | Rapida 1H V3 Filtered | 9 | €9.749,93 | €1.796,76 | €5.390,27 | €145,80 | €38,19 |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | 5 | €9.742,29 | €1.771,28 | €3.542,56 | €97,21 | €65,13 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 0 | €9.723,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Bollinger 1H | 1 | €9.718,69 | €770,02 | €2.310,06 | €48,65 | €-10,95 |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | 0 | €9.711,41 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Score 6 75 V1 | 0 | €9.702,33 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Guard V1 | 7 | €9.651,39 | €2.301,69 | €4.603,38 | €144,55 | €93,47 |
| TEST | Global Confluence puro 1H | 0 | €9.628,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 No Esports Long Only V1 | 7 | €9.620,52 | €1.598,12 | €4.794,36 | €142,92 | €22,32 |
| TEST | Combo Adaptive Quality7 Regime V1 | 5 | €9.619,75 | €1.749,00 | €3.498,00 | €95,99 | €64,31 |
| TEST | 1H Fast V3 No Esports V1 | 9 | €9.599,92 | €1.772,63 | €5.317,88 | €143,56 | €37,41 |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | 1 | €9.595,22 | €199,19 | €398,38 | €47,81 | €0,00 |
| TEST | Combo Adaptive Regime V1 | 6 | €9.591,75 | €2.910,43 | €5.820,86 | €99,24 | €51,90 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 0 | €9.579,83 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top10 Long | 7 | €9.578,52 | €2.000,27 | €4.000,55 | €184,15 | €10,45 |
| TEST | Scanner Top15 Long | 7 | €9.578,52 | €2.000,27 | €4.000,55 | €184,15 | €10,45 |
| TEST | Scanner Top20 Long | 7 | €9.578,52 | €2.000,27 | €4.000,55 | €184,15 | €10,45 |
| TEST | Forza relativa 1H V2 | 5 | €9.574,86 | €1.970,15 | €3.940,29 | €49,78 | €158,81 |
| TEST | 1H Balanced Long No Rhv V1 | 8 | €9.557,05 | €1.387,75 | €4.163,24 | €93,50 | €146,50 |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | 0 | €9.517,55 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Scanner | 6 | €9.499,11 | €2.618,07 | €5.236,15 | €141,98 | €111,08 |
| TEST | Combo Adaptive Quality7 V1 | 6 | €9.470,56 | €2.208,05 | €4.416,09 | €97,32 | €82,46 |
| TEST | Bilanciata 1H V2 | 5 | €9.454,94 | €872,37 | €2.617,11 | €142,69 | €17,40 |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | 0 | €9.447,55 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | 0 | €9.444,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Balanced V3 Long Only V1 | 6 | €9.443,26 | €1.257,19 | €3.771,56 | €94,65 | €75,94 |
| TEST | 1H Fast V3 Nohigh V1 | 1 | €9.435,91 | €146,77 | €440,31 | €48,44 | €0,00 |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | 1 | €9.430,59 | €195,77 | €391,54 | €46,99 | €0,00 |
| TEST | Scanner Top5 Btc Guard Mfe V1 | 7 | €9.426,93 | €2.248,16 | €4.496,32 | €141,18 | €91,30 |
| TEST | Scanner Bottom10 Short | 3 | €9.385,05 | €1.090,11 | €2.180,22 | €97,35 | €0,00 |
| TEST | Scanner Bottom15 Short | 3 | €9.385,05 | €1.090,11 | €2.180,22 | €97,35 | €0,00 |
| TEST | Scanner Bottom20 Short | 3 | €9.385,05 | €1.090,11 | €2.180,22 | €97,35 | €0,00 |
| TEST | Master Adaptive Runner25 V1 | 1 | €9.378,18 | €34,77 | €69,54 | €8,34 | €0,00 |
| TEST | Master Adaptive Gb20 Be V1 | 0 | €9.372,49 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Gb20 Partial V1 | 0 | €9.362,52 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Cap75 V1 | 0 | €9.355,17 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive No Alt V1 | 0 | €9.354,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive V1 | 0 | €9.326,30 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | 3 | €9.320,02 | €1.082,57 | €2.165,15 | €96,67 | €0,00 |
| TEST | Master Adaptive Expanded V1 | 1 | €9.319,82 | €197,50 | €395,01 | €47,40 | €0,00 |
| TEST | Scanner Bottom5 Short Profit Lock V1 | 3 | €9.305,85 | €1.080,93 | €2.161,86 | €96,53 | €0,00 |
| TEST | Combo Trend | 6 | €9.296,18 | €1.914,73 | €3.829,45 | €0,48 | €162,78 |
| TEST | Scanner Top5 Btc Mfe V1 | 6 | €9.281,63 | €2.558,13 | €5.116,27 | €138,73 | €108,53 |
| TEST | Master Adaptive Gb20 Loss Cap V1 | 1 | €9.252,08 | €195,70 | €391,41 | €45,67 | €0,00 |
| TEST | Scanner Top5 Btc Btc Le3 V1 | 0 | €9.237,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom 5 Short 1H | 3 | €9.234,23 | €1.072,61 | €2.145,22 | €95,79 | €0,00 |
| TEST | Master Adaptive Gb20 V1 | 0 | €9.202,39 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Long Only V1 | 7 | €9.159,78 | €1.521,58 | €4.564,75 | €136,08 | €21,25 |
| TEST | Bilanciata 1H V1 | 1 | €9.151,18 | €135,05 | €405,16 | €0,00 | €0,00 |
| TEST | Combo Mean Reversion | 1 | €9.114,86 | €225,41 | €450,83 | €48,50 | €0,00 |
| TEST | Master Adaptive Strict3 V1 | 0 | €9.056,84 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Benchmark trend following EMA 1H | 8 | €9.022,11 | €1.879,85 | €3.759,69 | €2,63 | €155,98 |
| TEST | Combo Adaptive Runner25 V1 | 0 | €8.964,11 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Mfe Trail | 8 | €8.901,85 | €1.858,66 | €3.717,31 | €44,65 | €142,98 |
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
| PRINCIPALE | Principale 4H | Confluenza trend | €9.715,38 | €-333,55 | 46 | 46 | 34,78% | 0,76 | €-7,25 | 6,39% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €11.103,69 | €974,86 | 78 | 78 | 48,72% | 1,56 | €12,50 | 3,63% |
| TEST | Donchian 1H Gb20 120R V1 | Donchian breakout 20 barre | €10.842,27 | €716,47 | 46 | 46 | 47,83% | 1,82 | €15,58 | 3,63% |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | Momentum / breakout | €10.802,41 | €754,20 | 95 | 95 | 52,63% | 1,37 | €7,94 | 4,41% |
| TEST | Combo Trend Side Regime Guard V1 | Combo Trend | €10.744,90 | €589,31 | 69 | 69 | 50,72% | 1,43 | €8,54 | 4,33% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.565,59 | €463,96 | 100 | 100 | 46,00% | 1,21 | €4,64 | 8,85% |
| TEST | Main Side Regime Guard V1 | Confluenza trend | €10.491,38 | €477,55 | 29 | 29 | 48,28% | 1,77 | €16,47 | 2,40% |
| TEST | 1H Fast No Pepe V1 | Momentum / breakout | €10.400,20 | €302,56 | 148 | 148 | 46,62% | 1,11 | €2,04 | 4,46% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | Momentum / breakout V3 Filtered | €10.300,05 | €300,05 | 33 | 33 | 48,48% | 2,04 | €9,09 | 2,01% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | Momentum / breakout V3 Filtered | €10.271,73 | €271,73 | 22 | 22 | 50,00% | 1,74 | €12,35 | 1,72% |
| TEST | 1H Fast V3 Nohigh Range Only V1 | Momentum / breakout V3 Filtered | €10.247,95 | €247,95 | 41 | 41 | 46,34% | 1,25 | €6,05 | 3,97% |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | Momentum / breakout V3 Filtered | €10.239,20 | €239,20 | 17 | 17 | 52,94% | 4,50 | €14,07 | 1,01% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | Momentum / breakout V3 Filtered | €10.235,18 | €235,18 | 20 | 20 | 50,00% | 1,90 | €11,76 | 2,73% |
| TEST | Main Dynamic Asset Selector V1 | Confluenza trend | €10.213,35 | €213,35 | 12 | 12 | 41,67% | 1,74 | €17,78 | 1,54% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | Momentum / breakout V3 Filtered | €10.185,37 | €185,37 | 22 | 22 | 40,91% | 1,57 | €8,43 | 2,27% |
| TEST | Combo Adaptive Side Regime Guard V1 | Combo Adaptive | €10.179,84 | €57,08 | 79 | 79 | 43,04% | 1,04 | €0,72 | 8,68% |
| TEST | Combo Adaptive | Combo Adaptive | €10.167,39 | €3,59 | 108 | 108 | 40,74% | 1,00 | €0,03 | 7,91% |
| TEST | 1H Fast Score 6 75 Range Only V1 | Momentum / breakout | €10.149,62 | €149,62 | 38 | 38 | 44,74% | 1,14 | €3,94 | 3,35% |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | Momentum / breakout V3 Filtered | €10.145,12 | €145,12 | 44 | 44 | 45,45% | 1,20 | €3,30 | 2,91% |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | Momentum / breakout V3 Filtered | €10.140,84 | €140,84 | 63 | 63 | 44,44% | 1,10 | €2,24 | 5,24% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.138,40 | €138,40 | 5 | 5 | 80,00% | 3,42 | €27,68 | 0,85% |
| TEST | Combo Adaptive Long Only V1 | Combo Adaptive | €10.131,57 | €-12,68 | 75 | 75 | 42,67% | 0,99 | €-0,17 | 6,25% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €10.130,32 | €66,34 | 4 | 4 | 50,00% | 1,63 | €16,58 | 1,05% |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | Momentum / breakout | €10.126,53 | €126,53 | 40 | 40 | 45,00% | 1,13 | €3,16 | 3,73% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €10.107,65 | €49,10 | 4 | 4 | 50,00% | 1,47 | €12,27 | 1,01% |
| TEST | Ampia 4H | Confluenza trend | €10.102,33 | €60,72 | 45 | 45 | 26,67% | 1,05 | €1,35 | 4,45% |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | Momentum / breakout V3 Filtered | €10.099,04 | €99,04 | 55 | 55 | 54,55% | 1,12 | €1,80 | 3,59% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €10.083,25 | €83,25 | 6 | 6 | 66,67% | 1,77 | €13,88 | 1,13% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €10.070,19 | €70,19 | 2 | 2 | 50,00% | 2,39 | €35,09 | 0,96% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €10.067,96 | €67,96 | 8 | 8 | 62,50% | 1,41 | €8,50 | 1,49% |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | Momentum / breakout V3 Filtered | €10.048,77 | €48,77 | 23 | 23 | 43,48% | 1,12 | €2,12 | 3,05% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €10.046,94 | €46,94 | 7 | 7 | 57,14% | 1,28 | €6,71 | 1,89% |
| TEST | Rapida 1H V1 | Momentum / breakout | €10.043,28 | €43,28 | 78 | 78 | 34,62% | 1,02 | €0,55 | 6,76% |
| TEST | 1H Fast Tp2 V1 | Momentum / breakout | €10.035,93 | €-9,50 | 168 | 167 | 36,90% | 1,00 | €-0,06 | 6,56% |
| TEST | 1H Balanced Short Trend Down Strict V1 | Confluenza trend | €10.035,46 | €35,46 | 13 | 13 | 38,46% | 1,13 | €2,73 | 1,80% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.029,45 | €29,45 | 2 | 2 | 50,00% | 1,54 | €14,72 | 0,82% |
| TEST | 1H Fast Nohigh Cap75 V1 | Momentum / breakout | €10.029,22 | €29,50 | 121 | 121 | 43,80% | 1,01 | €0,24 | 7,10% |
| TEST | Scalp RSI Long 20 · prudente · 5x | Inversione RSI estrema 15m | €10.028,67 | €28,67 | 9 | 9 | 55,56% | 1,80 | €3,19 | 0,36% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €10.022,40 | €24,50 | 25 | 25 | 48,00% | 1,27 | €0,98 | 0,33% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €10.022,21 | €-35,50 | 10 | 10 | 40,00% | 0,86 | €-3,55 | 2,77% |
| TEST | Btc Ema 4H | Trend following EMA | €10.019,41 | €19,41 | 3 | 3 | 33,33% | 1,19 | €6,47 | 1,76% |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | Momentum / breakout V3 Filtered | €10.013,82 | €13,82 | 41 | 41 | 48,78% | 1,01 | €0,34 | 4,50% |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | Momentum / breakout V3 Filtered | €10.008,92 | €8,92 | 30 | 30 | 36,67% | 1,02 | €0,30 | 4,84% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €10.004,48 | €4,90 | 25 | 25 | 48,00% | 1,27 | €0,20 | 0,07% |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | Momentum / breakout V3 Filtered | €10.003,37 | €3,37 | 8 | 8 | 37,50% | 1,02 | €0,42 | 2,15% |
| TEST | Scalp RSI Short 85 · €50 · 15x | Inversione RSI estrema 15m | €10.001,42 | €1,42 | 3 | 3 | 66,67% | 2,74 | €0,47 | 0,08% |
| TEST | Scalp RSI Short 85 · €10 · 15x | Inversione RSI estrema 15m | €10.000,28 | €0,28 | 3 | 3 | 66,67% | 2,74 | €0,09 | 0,02% |
| TEST | Scanner Bottom5 Short Continuation V1 | Scanner Bottom5 Short Continuation | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 85 · prudente · 5x | Inversione RSI estrema 15m | €9.999,47 | €-0,53 | 3 | 3 | 66,67% | 0,77 | €-0,18 | 0,16% |
| TEST | Scalp RSI Long 20 · €10 · 15x | Inversione RSI estrema 15m | €9.999,33 | €-0,67 | 9 | 9 | 44,44% | 0,85 | €-0,07 | 0,04% |
| TEST | Scalp RSI Long 15 · €10 · 15x | Inversione RSI estrema 15m | €9.997,60 | €-2,40 | 3 | 3 | 33,33% | 0,13 | €-0,80 | 0,02% |
| TEST | Scalp RSI Long 20 · €50 · 15x | Inversione RSI estrema 15m | €9.996,64 | €-3,36 | 9 | 9 | 44,44% | 0,85 | €-0,37 | 0,21% |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | Momentum / breakout V3 Filtered | €9.995,23 | €-4,77 | 15 | 15 | 46,67% | 0,99 | €-0,32 | 2,70% |
| TEST | Scalp RSI Short 80 · €10 · 15x | Inversione RSI estrema 15m | €9.994,76 | €-5,24 | 14 | 14 | 35,71% | 0,47 | €-0,37 | 0,11% |
| TEST | Scalp RSI Long 25 · €10 · 15x | Inversione RSI estrema 15m | €9.990,45 | €-9,55 | 15 | 15 | 40,00% | 0,36 | €-0,64 | 0,14% |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | €9.988,00 | €-12,00 | 3 | 3 | 33,33% | 0,13 | €-4,00 | 0,12% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €9.987,48 | €-12,52 | 15 | 15 | 40,00% | 0,83 | €-0,83 | 0,71% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €9.983,99 | €-93,54 | 122 | 122 | 40,16% | 0,97 | €-0,77 | 9,12% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €9.981,72 | €-18,28 | 3 | 3 | 33,33% | 0,83 | €-6,09 | 1,22% |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | €9.980,94 | €-19,06 | 3 | 3 | 33,33% | 0,19 | €-6,35 | 0,20% |
| TEST | Sol Ema 4H | Trend following EMA | €9.974,31 | €-88,69 | 5 | 5 | 20,00% | 0,57 | €-17,74 | 2,27% |
| TEST | Scalp RSI Short 80 · €50 · 15x | Inversione RSI estrema 15m | €9.973,79 | €-26,21 | 14 | 14 | 35,71% | 0,47 | €-1,87 | 0,53% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €9.965,81 | €-34,19 | 4 | 4 | 25,00% | 0,80 | €-8,55 | 2,43% |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | €9.952,25 | €-47,75 | 15 | 15 | 40,00% | 0,36 | €-3,18 | 0,72% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €9.951,64 | €-47,76 | 35 | 31 | 42,86% | 0,95 | €-1,36 | 3,89% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.949,57 | €-50,43 | 9 | 9 | 33,33% | 0,85 | €-5,60 | 2,63% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.947,73 | €-49,88 | 25 | 25 | 48,00% | 0,61 | €-2,00 | 0,84% |
| TEST | Btc Ema 1H | Trend following EMA | €9.942,20 | €-57,80 | 10 | 10 | 40,00% | 0,82 | €-5,78 | 1,94% |
| TEST | Scalp RSI Short 80 · prudente · 5x | Inversione RSI estrema 15m | €9.940,80 | €-59,20 | 14 | 14 | 35,71% | 0,32 | €-4,23 | 0,89% |
| TEST | Doge Ema 1H | Trend following EMA | €9.920,90 | €-79,10 | 14 | 14 | 57,14% | 0,77 | €-5,65 | 2,61% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €9.900,93 | €-210,81 | 89 | 89 | 39,33% | 0,90 | €-2,37 | 11,27% |
| TEST | Sol Ema 1H | Trend following EMA | €9.899,48 | €-151,22 | 11 | 11 | 27,27% | 0,61 | €-13,75 | 3,33% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.892,99 | €-107,01 | 8 | 8 | 37,50% | 0,66 | €-13,38 | 1,89% |
| TEST | Eth Ema 4H | Trend following EMA | €9.887,99 | €-158,00 | 3 | 3 | 0,00% | 0,00 | €-52,67 | 1,83% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.878,92 | €-121,08 | 10 | 10 | 40,00% | 0,63 | €-12,11 | 3,14% |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | Momentum / breakout V3 Filtered | €9.837,38 | €-162,62 | 37 | 37 | 40,54% | 0,76 | €-4,40 | 3,08% |
| TEST | Scanner Top5 Btc Tp3 V1 | Scanner Top 5 + forza BTC | €9.826,58 | €-396,77 | 71 | 71 | 35,21% | 0,80 | €-5,59 | 11,78% |
| TEST | Scanner Top5 Btc Runner25 V1 | Scanner Top 5 + forza BTC | €9.820,83 | €-402,38 | 75 | 75 | 36,00% | 0,80 | €-5,37 | 12,06% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | Momentum / breakout V3 Filtered | €9.817,34 | €-182,66 | 24 | 24 | 41,67% | 0,64 | €-7,61 | 3,23% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €9.816,06 | €-183,94 | 11 | 11 | 45,45% | 0,49 | €-16,72 | 2,90% |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | Momentum / breakout V3 Filtered | €9.813,01 | €-227,71 | 129 | 128 | 47,29% | 0,91 | €-1,77 | 9,50% |
| TEST | Eth Ema 1H | Trend following EMA | €9.793,37 | €-268,16 | 13 | 13 | 30,77% | 0,47 | €-20,63 | 4,80% |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | Momentum / breakout | €9.779,65 | €-220,08 | 85 | 85 | 42,35% | 0,88 | €-2,59 | 7,10% |
| TEST | Combo Adaptive Partial 1R V1 | Combo Adaptive | €9.767,15 | €-390,71 | 107 | 107 | 39,25% | 0,81 | €-3,65 | 8,69% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | Momentum / breakout V3 Filtered | €9.762,18 | €-237,82 | 7 | 7 | 14,29% | 0,02 | €-33,97 | 2,82% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €9.758,68 | €-291,30 | 12 | 12 | 25,00% | 0,35 | €-24,27 | 4,59% |
| TEST | Rapida 1H V3 Filtered | Momentum / breakout V3 Filtered | €9.749,93 | €-290,53 | 173 | 172 | 40,46% | 0,92 | €-1,68 | 9,48% |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | Combo Adaptive | €9.742,29 | €-320,36 | 27 | 27 | 40,74% | 0,61 | €-11,87 | 4,21% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | Momentum / breakout V3 Filtered | €9.723,72 | €-276,28 | 31 | 31 | 32,26% | 0,62 | €-8,91 | 4,83% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €9.718,69 | €-269,20 | 5 | 5 | 20,00% | 0,05 | €-53,84 | 3,32% |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | Scanner Top 5 + forza BTC | €9.711,41 | €-288,59 | 13 | 13 | 23,08% | 0,41 | €-22,20 | 4,35% |
| TEST | 1H Fast Score 6 75 V1 | Momentum / breakout | €9.702,33 | €-365,26 | 131 | 130 | 41,98% | 0,90 | €-2,79 | 9,66% |
| TEST | Scanner Top5 Btc Guard V1 | Scanner Top 5 + forza BTC | €9.651,39 | €-438,59 | 72 | 72 | 34,72% | 0,77 | €-6,09 | 7,34% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.628,04 | €-371,96 | 16 | 16 | 25,00% | 0,32 | €-23,25 | 3,92% |
| TEST | 1H Fast V3 No Esports Long Only V1 | Momentum / breakout V3 Filtered | €9.620,52 | €-398,92 | 89 | 89 | 38,20% | 0,82 | €-4,48 | 10,60% |
| TEST | Combo Adaptive Quality7 Regime V1 | Combo Adaptive | €9.619,75 | €-442,11 | 27 | 27 | 33,33% | 0,47 | €-16,37 | 5,41% |
| TEST | 1H Fast V3 No Esports V1 | Momentum / breakout V3 Filtered | €9.599,92 | €-488,85 | 145 | 144 | 40,69% | 0,84 | €-3,37 | 9,00% |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | Scanner Top 5 + forza BTC | €9.595,22 | €-404,43 | 58 | 58 | 39,66% | 0,78 | €-6,97 | 7,74% |
| TEST | Combo Adaptive Regime V1 | Combo Adaptive | €9.591,75 | €-456,52 | 39 | 39 | 41,03% | 0,63 | €-11,71 | 5,38% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | Momentum / breakout V3 Filtered | €9.579,83 | €-420,17 | 11 | 11 | 0,00% | 0,00 | €-38,20 | 4,20% |
| TEST | Scanner Top10 Long | Scanner Top10 Long | €9.578,52 | €-429,13 | 77 | 77 | 41,56% | 0,76 | €-5,57 | 10,31% |
| TEST | Scanner Top15 Long | Scanner Top15 Long | €9.578,52 | €-429,13 | 77 | 77 | 41,56% | 0,76 | €-5,57 | 10,31% |
| TEST | Scanner Top20 Long | Scanner Top20 Long | €9.578,52 | €-429,13 | 77 | 77 | 41,56% | 0,76 | €-5,57 | 10,31% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €9.574,86 | €-581,26 | 88 | 84 | 37,50% | 0,80 | €-6,61 | 10,88% |
| TEST | 1H Balanced Long No Rhv V1 | Confluenza trend | €9.557,05 | €-586,71 | 67 | 67 | 38,81% | 0,68 | €-8,76 | 9,26% |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | Momentum / breakout V3 Filtered | €9.517,55 | €-482,45 | 78 | 78 | 39,74% | 0,78 | €-6,19 | 6,59% |
| TEST | Combo Scanner | Combo Scanner | €9.499,11 | €-608,10 | 93 | 93 | 38,71% | 0,76 | €-6,54 | 11,38% |
| TEST | Combo Adaptive Quality7 V1 | Combo Adaptive | €9.470,56 | €-609,07 | 54 | 54 | 31,48% | 0,63 | €-11,28 | 8,88% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €9.454,94 | €-560,73 | 81 | 74 | 39,51% | 0,71 | €-6,92 | 8,84% |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | Momentum / breakout V3 Filtered | €9.447,55 | €-615,90 | 84 | 83 | 44,05% | 0,76 | €-7,33 | 7,69% |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | Momentum / breakout | €9.444,37 | €-621,42 | 89 | 88 | 43,82% | 0,78 | €-6,98 | 9,98% |
| TEST | 1H Balanced V3 Long Only V1 | Confluenza trend V3 Filtered | €9.443,26 | €-630,07 | 78 | 78 | 38,46% | 0,64 | €-8,08 | 8,85% |
| TEST | 1H Fast V3 Nohigh V1 | Momentum / breakout V3 Filtered | €9.435,91 | €-563,83 | 111 | 111 | 40,54% | 0,80 | €-5,08 | 6,91% |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | Scanner Top 5 + forza BTC | €9.430,59 | €-569,07 | 73 | 73 | 39,73% | 0,73 | €-7,80 | 7,02% |
| TEST | Scanner Top5 Btc Guard Mfe V1 | Scanner Top 5 + forza BTC | €9.426,93 | €-660,96 | 89 | 89 | 37,08% | 0,71 | €-7,43 | 8,78% |
| TEST | Scanner Bottom10 Short | Scanner Bottom10 Short | €9.385,05 | €-613,68 | 67 | 67 | 32,84% | 0,67 | €-9,16 | 8,28% |
| TEST | Scanner Bottom15 Short | Scanner Bottom15 Short | €9.385,05 | €-613,68 | 67 | 67 | 32,84% | 0,67 | €-9,16 | 8,28% |
| TEST | Scanner Bottom20 Short | Scanner Bottom20 Short | €9.385,05 | €-613,68 | 67 | 67 | 32,84% | 0,67 | €-9,16 | 8,28% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €9.378,18 | €-621,78 | 51 | 51 | 31,37% | 0,66 | €-12,19 | 8,18% |
| TEST | Master Adaptive Gb20 Be V1 | Master Adaptive Consensus | €9.372,49 | €-627,51 | 55 | 55 | 29,09% | 0,62 | €-11,41 | 8,39% |
| TEST | Master Adaptive Gb20 Partial V1 | Master Adaptive Consensus | €9.362,52 | €-637,48 | 50 | 50 | 34,00% | 0,60 | €-12,75 | 7,98% |
| TEST | 1H Fast V3 Cap75 V1 | Momentum / breakout V3 Filtered | €9.355,17 | €-644,83 | 126 | 126 | 38,10% | 0,80 | €-5,12 | 11,75% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €9.354,60 | €-645,40 | 58 | 58 | 34,48% | 0,67 | €-11,13 | 7,26% |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | €9.326,30 | €-673,70 | 52 | 52 | 32,69% | 0,62 | €-12,96 | 7,80% |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | Scanner Bottom 5 Short | €9.320,02 | €-678,72 | 58 | 58 | 32,76% | 0,60 | €-11,70 | 8,30% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €9.319,82 | €-679,95 | 61 | 61 | 34,43% | 0,66 | €-11,15 | 7,96% |
| TEST | Scanner Bottom5 Short Profit Lock V1 | Scanner Bottom 5 Short | €9.305,85 | €-692,90 | 59 | 59 | 32,20% | 0,58 | €-11,74 | 8,30% |
| TEST | Combo Trend | Combo Trend | €9.296,18 | €-863,69 | 129 | 129 | 34,11% | 0,74 | €-6,70 | 10,85% |
| TEST | Scanner Top5 Btc Mfe V1 | Scanner Top 5 + forza BTC | €9.281,63 | €-823,12 | 81 | 81 | 37,04% | 0,58 | €-10,16 | 12,28% |
| TEST | Master Adaptive Gb20 Loss Cap V1 | Master Adaptive Consensus | €9.252,08 | €-747,69 | 42 | 42 | 23,81% | 0,53 | €-17,80 | 11,41% |
| TEST | Scanner Top5 Btc Btc Le3 V1 | Scanner Top 5 + forza BTC | €9.237,05 | €-762,95 | 59 | 59 | 33,90% | 0,57 | €-12,93 | 11,72% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.234,23 | €-764,52 | 86 | 86 | 32,56% | 0,66 | €-8,89 | 9,40% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €9.202,39 | €-797,61 | 87 | 87 | 48,28% | 0,60 | €-9,17 | 9,02% |
| TEST | 1H Fast V3 Long Only V1 | Momentum / breakout V3 Filtered | €9.159,78 | €-858,72 | 109 | 109 | 33,03% | 0,70 | €-7,88 | 12,52% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €9.151,18 | €-848,58 | 120 | 120 | 36,67% | 0,69 | €-7,07 | 13,99% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €9.114,86 | €-884,87 | 37 | 37 | 37,84% | 0,48 | €-23,92 | 10,64% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €9.056,84 | €-943,16 | 53 | 53 | 28,30% | 0,59 | €-17,80 | 11,51% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.022,11 | €-1.131,04 | 94 | 94 | 28,72% | 0,49 | €-12,03 | 12,31% |
| TEST | Combo Adaptive Runner25 V1 | Combo Adaptive | €8.964,11 | €-1.035,89 | 94 | 94 | 30,85% | 0,53 | €-11,02 | 12,67% |
| TEST | Combo Adaptive Mfe Trail | Combo Adaptive | €8.901,85 | €-1.238,63 | 112 | 112 | 33,04% | 0,51 | €-11,06 | 15,45% |
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
| Principale 4H | ETH | LONG | Confluenza trend | 240m | 3,0x | 2258,11153 | 2350,10000 | 2283,06760 | 1516,69825 | 2433,12687 | €415,70 | €1.247,11 | €0,00 | €50,80 |
| Principale 4H | LINK | LONG | Confluenza trend | 240m | 3,0x | 10,58112 | 10,58112 | 10,13407 | 7,10698 | 11,47522 | €16,96 | €50,87 | €2,15 | €0,00 |
| Bilanciata 1H V1 | CYS | SHORT | Confluenza trend | 60m | 3,0x | 0,76314 | 0,76314 | 0,70300 | 1,01371 | 0,57999 | €135,05 | €405,16 | €0,00 | €-0,00 |
| 1H Balanced Long No Rhv V1 | AKE | LONG | Confluenza trend | 60m | 3,0x | 0,01042 | 0,01042 | 0,00943 | 0,00700 | 0,01242 | €161,02 | €483,05 | €46,21 | €0,00 |
| 1H Balanced Long No Rhv V1 | ETH | LONG | Confluenza trend | 60m | 3,0x | 2265,72305 | 2350,10000 | 2298,77683 | 1521,81065 | 2396,13352 | €43,23 | €129,69 | €0,00 | €4,83 |
| 1H Balanced Long No Rhv V1 | SKHYNIX | LONG | Confluenza trend | 60m | 3,0x | 1214,11277 | 1214,11277 | 1170,18211 | 815,47908 | 1301,97411 | €413,43 | €1.240,28 | €44,88 | €0,00 |
| 1H Balanced Long No Rhv V1 | XRP | LONG | Confluenza trend | 60m | 3,0x | 1,23032 | 1,30921 | 1,27542 | 0,82636 | 1,33685 | €362,43 | €1.087,28 | €0,00 | €69,72 |
| 1H Balanced Long No Rhv V1 | PEPE | LONG | Confluenza trend | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €372,21 | €1.116,62 | €0,00 | €71,54 |
| 1H Balanced Long No Rhv V1 | HYPE | LONG | Confluenza trend | 60m | 3,0x | 72,76855 | 72,50200 | 70,17618 | 48,87621 | 77,95329 | €16,05 | €48,15 | €1,72 | €-0,18 |
| 1H Balanced Long No Rhv V1 | ADA | LONG | Confluenza trend | 60m | 3,0x | 0,20285 | 0,20671 | 0,20393 | 0,13625 | 0,21614 | €10,30 | €30,89 | €0,00 | €0,59 |
| 1H Balanced Long No Rhv V1 | SUI | LONG | Confluenza trend | 60m | 3,0x | 0,74725 | 0,74725 | 0,72830 | 0,50190 | 0,78515 | €9,09 | €27,27 | €0,69 | €0,00 |
| Bilanciata 1H V2 | AKE | LONG | Confluenza trend V2 | 60m | 3,0x | 0,01007 | 0,01007 | 0,00886 | 0,00676 | 0,01249 | €135,82 | €407,45 | €48,89 | €0,00 |
| Bilanciata 1H V2 | CYS | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,73666 | 0,73666 | 0,70420 | 0,97853 | 0,55986 | €127,95 | €383,85 | €0,00 | €-0,00 |
| Bilanciata 1H V2 | SKHYNIX | LONG | Confluenza trend V2 | 60m | 3,0x | 1214,11277 | 1214,11277 | 1170,18211 | 815,47908 | 1301,97411 | €422,38 | €1.267,15 | €45,85 | €0,00 |
| Bilanciata 1H V2 | LINK | LONG | Confluenza trend V2 | 60m | 3,0x | 10,70214 | 10,70214 | 10,45333 | 7,18827 | 11,19976 | €19,07 | €57,20 | €1,33 | €0,00 |
| Bilanciata 1H V2 | BOME | LONG | Confluenza trend V2 | 60m | 3,0x | 0,00115 | 0,00119 | 0,00104 | 0,00077 | 0,00136 | €167,15 | €501,46 | €46,62 | €17,40 |
| Bilanciata 1H V3 Filtered | BEAT | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,25480 | 0,25480 | 0,25418 | 0,33846 | 0,19365 | €137,63 | €412,88 | €0,00 | €-0,00 |
| Bilanciata 1H V3 Filtered | ETH | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 2248,80967 | 2350,10000 | 2296,55064 | 1510,45050 | 2383,72136 | €531,07 | €1.593,21 | €0,00 | €71,76 |
| Bilanciata 1H V3 Filtered | SKHYNIX | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1220,85412 | 1220,85412 | 1177,63561 | 820,00702 | 1307,29117 | €460,42 | €1.381,27 | €48,90 | €0,00 |
| Bilanciata 1H V3 Filtered | PEPE | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €14,62 | €43,87 | €0,00 | €1,53 |
| Bilanciata 1H V3 Filtered | BOME | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,00117 | 0,00119 | 0,00106 | 0,00079 | 0,00140 | €172,42 | €517,27 | €49,79 | €7,13 |
| Bilanciata 1H V3 Filtered | HYPE | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 72,76855 | 72,50200 | 70,17618 | 48,87621 | 77,95329 | €13,01 | €39,02 | €1,39 | €-0,14 |
| 1H Fast Score 6 75 Cost Aware V1 | SKHYNIX | LONG | Momentum / breakout | 60m | 3,0x | 1220,85412 | 1220,85412 | 1187,23972 | 820,00702 | 1271,27573 | €624,93 | €1.874,80 | €51,62 | €0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | ETH | LONG | Momentum / breakout | 60m | 3,0x | 2339,94790 | 2350,10000 | 2293,95002 | 1571,66500 | 2408,94470 | €907,70 | €2.723,10 | €53,53 | €11,81 |
| 1H Fast Score 6 75 Cost Aware V1 | SOL | LONG | Momentum / breakout | 60m | 3,0x | 88,28565 | 89,31100 | 88,39211 | 59,29853 | 90,06165 | €1.319,73 | €3.959,19 | €0,00 | €45,98 |
| 1H Fast Score 6 75 Cost Aware V1 | ADA | LONG | Momentum / breakout | 60m | 3,0x | 0,20843 | 0,20671 | 0,20302 | 0,14000 | 0,21655 | €18,83 | €56,50 | €1,47 | €-0,47 |
| 1H Fast Score 6 75 Cost Aware V1 | BTW | LONG | Momentum / breakout | 60m | 3,0x | 0,45972 | 0,42263 | 0,40581 | 0,30878 | 0,54057 | €8,91 | €26,72 | €3,13 | €-2,16 |
| 1H Fast Score 6 75 Cost Aware V1 | XRP | LONG | Momentum / breakout | 60m | 3,0x | 1,30947 | 1,30921 | 1,27240 | 0,87953 | 1,36509 | €626,69 | €1.880,06 | €53,23 | €-0,38 |
| 1H Fast Nohigh Cap75 V1 | BEAT | SHORT | Momentum / breakout | 60m | 3,0x | 0,24163 | 0,24163 | 0,26822 | 0,32097 | 0,20176 | €155,86 | €467,58 | €51,44 | €-0,00 |
| 1H Fast No Pepe V1 | BEAT | SHORT | Momentum / breakout | 60m | 3,0x | 0,24163 | 0,24163 | 0,26822 | 0,32097 | 0,20176 | €155,45 | €466,36 | €51,31 | €-0,00 |
| 1H Fast No Pepe V1 | SKHYNIX | LONG | Momentum / breakout | 60m | 3,0x | 1213,43264 | 1213,43264 | 1179,70743 | 815,02226 | 1264,02045 | €33,31 | €99,94 | €2,78 | €0,00 |
| 1H Fast No Pepe V1 | LINK | LONG | Momentum / breakout | 60m | 3,0x | 10,64413 | 10,64413 | 10,46121 | 7,14931 | 10,91851 | €17,86 | €53,58 | €0,92 | €0,00 |
| 1H Fast No Pepe V1 | ETH | LONG | Momentum / breakout | 60m | 3,0x | 2319,13373 | 2350,10000 | 2319,13373 | 1557,68482 | 2385,82358 | €863,99 | €2.591,96 | €0,00 | €34,61 |
| 1H Fast No Pepe V1 | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00114 | 0,00119 | 0,00105 | 0,00077 | 0,00128 | €202,87 | €608,61 | €48,19 | €23,44 |
| 1H Fast No Pepe V1 | SOL | LONG | Momentum / breakout | 60m | 3,0x | 88,28565 | 89,31100 | 88,39211 | 59,29853 | 90,06165 | €1.285,00 | €3.855,00 | €0,00 | €44,77 |
| 1H Fast No Pepe V1 | SUI | LONG | Momentum / breakout | 60m | 3,0x | 0,73835 | 0,73835 | 0,72383 | 0,49592 | 0,76013 | €10,95 | €32,86 | €0,65 | €0,00 |
| 1H Fast No Pepe V1 | ADA | LONG | Momentum / breakout | 60m | 3,0x | 0,20843 | 0,20671 | 0,20302 | 0,14000 | 0,21655 | €12,19 | €36,56 | €0,95 | €-0,30 |
| 1H Fast No Pepe V1 | ENA | LONG | Momentum / breakout | 60m | 3,0x | 0,12646 | 0,12643 | 0,12196 | 0,08494 | 0,13320 | €17,08 | €51,23 | €1,82 | €-0,01 |
| 1H Fast Tp2 V1 | BEAT | SHORT | Momentum / breakout | 60m | 3,0x | 0,24163 | 0,24163 | 0,26822 | 0,32097 | 0,18847 | €147,24 | €441,73 | €48,60 | €-0,00 |
| 1H Fast Tp2 V1 | SOXL | SHORT | Momentum / breakout | 60m | 3,0x | 121,01735 | 121,01735 | 127,15573 | 160,75137 | 108,74057 | €315,49 | €946,48 | €48,01 | €-0,00 |
| 1H Fast Tp2 V1 | SKHYNIX | LONG | Momentum / breakout | 60m | 3,0x | 1204,83092 | 1204,83092 | 1170,97389 | 809,24477 | 1272,54496 | €18,91 | €56,74 | €1,59 | €0,00 |
| 1H Fast Tp2 V1 | ETH | LONG | Momentum / breakout | 60m | 3,0x | 2319,13373 | 2350,10000 | 2319,13373 | 1557,68482 | 2408,05354 | €10,04 | €30,11 | €0,00 | €0,40 |
| 1H Fast Tp2 V1 | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00114 | 0,00119 | 0,00105 | 0,00077 | 0,00133 | €205,81 | €617,44 | €48,89 | €23,78 |
| 1H Fast Tp2 V1 | ADA | LONG | Momentum / breakout | 60m | 3,0x | 0,20285 | 0,20671 | 0,20469 | 0,13625 | 0,21319 | €17,28 | €51,83 | €0,00 | €0,99 |
| 1H Fast Tp2 V1 | SOL | LONG | Momentum / breakout | 60m | 3,0x | 89,26385 | 89,31100 | 88,02436 | 59,95555 | 91,74282 | €10,38 | €31,15 | €0,43 | €0,02 |
| 1H Fast Tp2 V1 | BTW | LONG | Momentum / breakout | 60m | 3,0x | 0,45972 | 0,42263 | 0,40581 | 0,30878 | 0,56752 | €142,85 | €428,56 | €50,25 | €-34,58 |
| 1H Fast Tp2 V1 | ENA | LONG | Momentum / breakout | 60m | 3,0x | 0,12646 | 0,12643 | 0,12196 | 0,08494 | 0,13544 | €9,83 | €29,49 | €1,05 | €-0,01 |
| Rapida 1H V2 | SOXL | SHORT | Momentum / breakout V2 | 60m | 3,0x | 121,15726 | 121,15726 | 127,13595 | 160,93723 | 112,18923 | €333,06 | €999,18 | €49,31 | €-0,00 |
| Rapida 1H V3 Filtered | BEAT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,24163 | 0,24163 | 0,26822 | 0,32097 | 0,20176 | €146,76 | €440,28 | €48,44 | €-0,00 |
| Rapida 1H V3 Filtered | SKHYNIX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1220,85412 | 1220,85412 | 1187,23972 | 820,00702 | 1271,27573 | €21,81 | €65,43 | €1,80 | €0,00 |
| Rapida 1H V3 Filtered | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2324,84488 | 2350,10000 | 2324,84488 | 1561,52081 | 2390,91922 | €9,36 | €28,08 | €0,00 | €0,31 |
| Rapida 1H V3 Filtered | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 74,02180 | 72,50200 | 72,01459 | 49,71798 | 77,03262 | €14,34 | €43,03 | €1,17 | €-0,88 |
| Rapida 1H V3 Filtered | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00116 | 0,00119 | 0,00109 | 0,00078 | 0,00128 | €10,13 | €30,39 | €1,98 | €0,65 |
| Rapida 1H V3 Filtered | XRP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,27028 | 1,30921 | 1,28767 | 0,85321 | 1,32452 | €564,49 | €1.693,47 | €0,00 | €51,89 |
| Rapida 1H V3 Filtered | SOL | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 88,28565 | 89,31100 | 88,39211 | 59,29853 | 90,06165 | €12,05 | €36,16 | €0,00 | €0,42 |
| Rapida 1H V3 Filtered | ADA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,20843 | 0,20671 | 0,20302 | 0,14000 | 0,21655 | €561,67 | €1.685,00 | €43,78 | €-13,92 |
| Rapida 1H V3 Filtered | ENA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,12646 | 0,12643 | 0,12196 | 0,08494 | 0,13320 | €456,14 | €1.368,43 | €48,63 | €-0,27 |
| 1H Fast V3 Nohigh V1 | BEAT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,24163 | 0,24163 | 0,26822 | 0,32097 | 0,20176 | €146,77 | €440,31 | €48,44 | €-0,00 |
| 1H Fast V3 Long Only V1 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2339,94790 | 2350,10000 | 2293,95002 | 1571,66500 | 2408,94470 | €11,60 | €34,80 | €0,68 | €0,15 |
| 1H Fast V3 Long Only V1 | PEPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €17,63 | €52,90 | €0,00 | €1,59 |
| 1H Fast V3 Long Only V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00116 | 0,00119 | 0,00109 | 0,00078 | 0,00128 | €231,87 | €695,60 | €45,44 | €14,80 |
| 1H Fast V3 Long Only V1 | XRP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,27028 | 1,30921 | 1,28767 | 0,85321 | 1,32452 | €535,74 | €1.607,21 | €0,00 | €49,25 |
| 1H Fast V3 Long Only V1 | SOL | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 88,28565 | 89,31100 | 88,39211 | 59,29853 | 90,06165 | €15,23 | €45,70 | €0,00 | €0,53 |
| 1H Fast V3 Long Only V1 | ADA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,20843 | 0,20671 | 0,20302 | 0,14000 | 0,21655 | €582,94 | €1.748,82 | €45,43 | €-14,45 |
| 1H Fast V3 Long Only V1 | BTW | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,45972 | 0,42263 | 0,40581 | 0,30878 | 0,54057 | €126,57 | €379,72 | €44,52 | €-30,63 |
| 1H Fast V3 No Esports V1 | BEAT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,24163 | 0,24163 | 0,26822 | 0,32097 | 0,20176 | €143,48 | €430,45 | €47,36 | €-0,00 |
| 1H Fast V3 No Esports V1 | SKHYNIX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1220,85412 | 1220,85412 | 1187,23972 | 820,00702 | 1271,27573 | €18,11 | €54,34 | €1,50 | €0,00 |
| 1H Fast V3 No Esports V1 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2324,84488 | 2350,10000 | 2324,84488 | 1561,52081 | 2390,91922 | €9,21 | €27,62 | €0,00 | €0,30 |
| 1H Fast V3 No Esports V1 | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 74,02180 | 72,50200 | 72,01459 | 49,71798 | 77,03262 | €14,15 | €42,45 | €1,15 | €-0,87 |
| 1H Fast V3 No Esports V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00116 | 0,00119 | 0,00109 | 0,00078 | 0,00128 | €10,02 | €30,05 | €1,96 | €0,64 |
| 1H Fast V3 No Esports V1 | XRP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,27028 | 1,30921 | 1,28767 | 0,85321 | 1,32452 | €555,79 | €1.667,38 | €0,00 | €51,09 |
| 1H Fast V3 No Esports V1 | SOL | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 88,28565 | 89,31100 | 88,39211 | 59,29853 | 90,06165 | €11,99 | €35,98 | €0,00 | €0,42 |
| 1H Fast V3 No Esports V1 | ADA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,20843 | 0,20671 | 0,20302 | 0,14000 | 0,21655 | €560,81 | €1.682,44 | €43,71 | €-13,90 |
| 1H Fast V3 No Esports V1 | ENA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,12646 | 0,12643 | 0,12196 | 0,08494 | 0,13320 | €449,06 | €1.347,18 | €47,88 | €-0,27 |
| 1H Fast V3 No Esports Long Only V1 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2339,94790 | 2350,10000 | 2293,95002 | 1571,66500 | 2408,94470 | €12,18 | €36,55 | €0,72 | €0,16 |
| 1H Fast V3 No Esports Long Only V1 | PEPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €18,52 | €55,56 | €0,00 | €1,67 |
| 1H Fast V3 No Esports Long Only V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00116 | 0,00119 | 0,00109 | 0,00078 | 0,00128 | €243,53 | €730,59 | €47,72 | €15,55 |
| 1H Fast V3 No Esports Long Only V1 | XRP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,27028 | 1,30921 | 1,28767 | 0,85321 | 1,32452 | €562,69 | €1.688,06 | €0,00 | €51,73 |
| 1H Fast V3 No Esports Long Only V1 | SOL | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 88,28565 | 89,31100 | 88,39211 | 59,29853 | 90,06165 | €16,00 | €48,00 | €0,00 | €0,56 |
| 1H Fast V3 No Esports Long Only V1 | ADA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,20843 | 0,20671 | 0,20302 | 0,14000 | 0,21655 | €612,26 | €1.836,79 | €47,72 | €-15,17 |
| 1H Fast V3 No Esports Long Only V1 | BTW | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,45972 | 0,42263 | 0,40581 | 0,30878 | 0,54057 | €132,94 | €398,81 | €46,76 | €-32,18 |
| 1H Fast V3 No Esports Mfe Lock V1 | BEAT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,24163 | 0,24163 | 0,26822 | 0,32097 | 0,20176 | €147,73 | €443,18 | €48,76 | €-0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | SKHYNIX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1220,85412 | 1220,85412 | 1187,23972 | 820,00702 | 1271,27573 | €21,95 | €65,86 | €1,81 | €0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2324,84488 | 2350,10000 | 2324,84488 | 1561,52081 | 2390,91922 | €9,42 | €28,26 | €0,00 | €0,31 |
| 1H Fast V3 No Esports Mfe Lock V1 | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 74,02180 | 72,50200 | 72,01459 | 49,71798 | 77,03262 | €14,44 | €43,31 | €1,17 | €-0,89 |
| 1H Fast V3 No Esports Mfe Lock V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00116 | 0,00119 | 0,00109 | 0,00078 | 0,00128 | €10,12 | €30,35 | €1,98 | €0,65 |
| 1H Fast V3 No Esports Mfe Lock V1 | XRP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,27028 | 1,30921 | 1,28767 | 0,85321 | 1,32452 | €568,14 | €1.704,43 | €0,00 | €52,23 |
| 1H Fast V3 No Esports Mfe Lock V1 | SOL | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 88,28565 | 89,31100 | 88,39211 | 59,29853 | 90,06165 | €12,13 | €36,40 | €0,00 | €0,42 |
| 1H Fast V3 No Esports Mfe Lock V1 | ADA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,20843 | 0,20671 | 0,20302 | 0,14000 | 0,21655 | €565,43 | €1.696,28 | €44,07 | €-14,01 |
| 1H Fast V3 No Esports Mfe Lock V1 | ENA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,12646 | 0,12643 | 0,12196 | 0,08494 | 0,13320 | €459,09 | €1.377,28 | €48,95 | €-0,28 |
| Ampia 4H | SPCX | LONG | Confluenza trend | 240m | 2,0x | 136,56189 | 136,56189 | 126,46637 | 68,96375 | 164,82935 | €323,86 | €647,73 | €47,88 | €0,00 |
| Ampia 4H | VELVET | LONG | Confluenza trend | 240m | 2,0x | 0,55987 | 0,55987 | 0,49269 | 0,28274 | 0,74799 | €201,63 | €403,26 | €48,39 | €0,00 |
| Ampia 4H | LINK | LONG | Confluenza trend | 240m | 2,0x | 9,97398 | 9,97398 | 10,38253 | 5,03686 | 11,21104 | €560,46 | €1.120,91 | €0,00 | €0,00 |
| Ampia 4H | ETH | LONG | Confluenza trend | 240m | 2,0x | 2258,11153 | 2350,10000 | 2144,35158 | 1140,34632 | 2576,63943 | €502,94 | €1.005,89 | €50,68 | €40,98 |
| Ampia 4H | ZEC | LONG | Confluenza trend | 240m | 2,0x | 565,27303 | 589,61000 | 531,45855 | 285,46288 | 659,95358 | €31,20 | €62,41 | €3,73 | €2,69 |
| Ampia 4H | HYPE | LONG | Confluenza trend | 240m | 2,0x | 71,99640 | 72,50200 | 66,32059 | 36,35818 | 87,88866 | €16,69 | €33,38 | €2,63 | €0,23 |
| Forza relativa 1H V2 | BEAT | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,25984 | 0,25984 | 0,25657 | 0,38847 | 0,19125 | €200,38 | €400,75 | €0,00 | €-0,00 |
| Forza relativa 1H V2 | PEPE | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €581,93 | €1.163,86 | €0,00 | €86,98 |
| Forza relativa 1H V2 | HYPE | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 72,36547 | 72,50200 | 69,70054 | 36,54456 | 78,22831 | €640,11 | €1.280,23 | €47,15 | €2,42 |
| Forza relativa 1H V2 | XRP | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 1,23032 | 1,30921 | 1,27225 | 0,62131 | 1,34751 | €533,57 | €1.067,14 | €0,00 | €68,43 |
| Forza relativa 1H V2 | BOME | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,00115 | 0,00119 | 0,00104 | 0,00058 | 0,00138 | €14,16 | €28,32 | €2,63 | €0,98 |
| Scalp RSI Short 75 · €10 · 15x | SOL | SHORT | Inversione RSI estrema 15m | 15m | 15,0x | 89,11517 | 89,31100 | 90,15113 | 94,61061 | 87,56124 | €10,00 | €150,00 | €1,74 | €-0,33 |
| Scalp RSI Short 75 · €50 · 15x | SOL | SHORT | Inversione RSI estrema 15m | 15m | 15,0x | 89,11517 | 89,31100 | 90,15113 | 94,61061 | 87,56124 | €50,00 | €750,00 | €8,72 | €-1,65 |
| Scalp RSI Short 75 · prudente · 5x | SOL | SHORT | Inversione RSI estrema 15m | 15m | 5,0x | 89,11517 | 89,31100 | 90,15113 | 106,49263 | 87,04326 | €171,19 | €855,93 | €9,95 | €-1,88 |
| Benchmark Donchian breakout 1H | SKHYNIX | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1174,33482 | 1174,33482 | 1128,44989 | 593,03908 | 1289,04713 | €641,25 | €1.282,50 | €50,11 | €0,00 |
| Benchmark Donchian breakout 1H | ETH | LONG | Donchian breakout 20 barre | 60m | 2,0x | 2256,83128 | 2350,10000 | 2300,60626 | 1139,69979 | 2409,20720 | €999,19 | €1.998,39 | €0,00 | €82,59 |
| Benchmark Donchian breakout 1H | LINK | LONG | Donchian breakout 20 barre | 60m | 2,0x | 10,71314 | 10,71314 | 10,39356 | 5,41014 | 11,51209 | €910,44 | €1.820,87 | €54,32 | €0,00 |
| Benchmark Donchian breakout 1H | SOL | LONG | Donchian breakout 20 barre | 60m | 2,0x | 87,44649 | 89,31100 | 85,50986 | 44,16048 | 92,28805 | €1.243,00 | €2.485,99 | €55,06 | €53,01 |
| Benchmark Donchian breakout 1H | HYPE | LONG | Donchian breakout 20 barre | 60m | 2,0x | 73,54771 | 72,50200 | 70,54476 | 37,14159 | 81,05509 | €82,39 | €164,78 | €6,73 | €-2,34 |
| Benchmark Donchian breakout 1H | ADA | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,20285 | 0,20671 | 0,19547 | 0,10244 | 0,22131 | €16,05 | €32,11 | €1,17 | €0,61 |
| Donchian 1H Gb20 120R V1 | SKHYNIX | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1174,33482 | 1174,33482 | 1128,44989 | 593,03908 | 1289,04713 | €626,15 | €1.252,30 | €48,93 | €0,00 |
| Donchian 1H Gb20 120R V1 | ETH | LONG | Donchian breakout 20 barre | 60m | 2,0x | 2256,83128 | 2350,10000 | 2300,60626 | 1139,69979 | 2409,20720 | €975,67 | €1.951,34 | €0,00 | €80,64 |
| Donchian 1H Gb20 120R V1 | LINK | LONG | Donchian breakout 20 barre | 60m | 2,0x | 10,71314 | 10,71314 | 10,39356 | 5,41014 | 11,51209 | €889,00 | €1.778,00 | €53,04 | €0,00 |
| Donchian 1H Gb20 120R V1 | SOL | LONG | Donchian breakout 20 barre | 60m | 2,0x | 87,44649 | 89,31100 | 85,50986 | 44,16048 | 92,28805 | €1.213,73 | €2.427,46 | €53,76 | €51,76 |
| Donchian 1H Gb20 120R V1 | HYPE | LONG | Donchian breakout 20 barre | 60m | 2,0x | 73,54771 | 72,50200 | 70,54476 | 37,14159 | 81,05509 | €80,45 | €160,90 | €6,57 | €-2,29 |
| Donchian 1H Gb20 120R V1 | ADA | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,20285 | 0,20671 | 0,19547 | 0,10244 | 0,22131 | €15,68 | €31,35 | €1,14 | €0,60 |
| Benchmark trend following EMA 1H | BEAT | SHORT | Trend following EMA | 60m | 2,0x | 0,28257 | 0,28257 | 0,25706 | 0,42244 | 0,20797 | €186,11 | €372,23 | €0,00 | €-0,00 |
| Benchmark trend following EMA 1H | HYPE | LONG | Trend following EMA | 60m | 2,0x | 69,29086 | 72,50200 | 72,11451 | 34,99188 | 76,51998 | €468,29 | €936,58 | €0,00 | €43,40 |
| Benchmark trend following EMA 1H | ETH | LONG | Trend following EMA | 60m | 2,0x | 2264,89289 | 2350,10000 | 2296,53215 | 1143,77091 | 2419,94510 | €713,61 | €1.427,21 | €0,00 | €53,69 |
| Benchmark trend following EMA 1H | SOL | LONG | Trend following EMA | 60m | 2,0x | 87,44649 | 89,31100 | 87,65252 | 44,16048 | 91,70706 | €26,87 | €53,74 | €0,00 | €1,15 |
| Benchmark trend following EMA 1H | LINK | LONG | Trend following EMA | 60m | 2,0x | 10,64413 | 10,64413 | 10,38282 | 5,37528 | 11,21901 | €12,99 | €25,97 | €0,64 | €0,00 |
| Benchmark trend following EMA 1H | SUI | LONG | Trend following EMA | 60m | 2,0x | 0,73965 | 0,73965 | 0,71894 | 0,37352 | 0,78521 | €14,44 | €28,87 | €0,81 | €0,00 |
| Benchmark trend following EMA 1H | XRP | LONG | Trend following EMA | 60m | 2,0x | 1,23032 | 1,30921 | 1,27225 | 0,62131 | 1,36053 | €443,18 | €886,36 | €0,00 | €56,84 |
| Benchmark trend following EMA 1H | PEPE | LONG | Trend following EMA | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €14,36 | €28,72 | €1,19 | €0,89 |
| Scanner Top 5 Long 1H | AKE | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01255 | €204,03 | €408,06 | €48,97 | €0,00 |
| Scanner Top 5 Long 1H | ETH | LONG | Scanner Top 5 Long | 60m | 2,0x | 2265,72305 | 2350,10000 | 2298,77683 | 1144,19014 | 2396,13352 | €95,49 | €190,98 | €0,00 | €7,11 |
| Scanner Top 5 Long 1H | LINK | LONG | Scanner Top 5 Long | 60m | 2,0x | 10,57611 | 10,57611 | 10,27850 | 5,34094 | 11,17135 | €897,38 | €1.794,76 | €50,51 | €0,00 |
| Scanner Top 5 Long 1H | PEPE | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €19,21 | €38,43 | €0,00 | €2,26 |
| Scanner Top 5 Long 1H | BOME | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,00114 | 0,00119 | 0,00103 | 0,00058 | 0,00138 | €257,00 | €514,01 | €52,33 | €19,79 |
| Scanner Top 5 Long 1H | XRP | LONG | Scanner Top 5 Long | 60m | 2,0x | 1,23032 | 1,30921 | 1,27542 | 0,62131 | 1,33685 | €583,16 | €1.166,31 | €0,00 | €74,79 |
| Scanner Top 5 Long 1H | ADA | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,20285 | 0,20671 | 0,20393 | 0,10244 | 0,21614 | €16,77 | €33,55 | €0,00 | €0,64 |
| Scanner Bottom 5 Short 1H | BEAT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,28257 | 0,28257 | 0,25514 | 0,42244 | 0,21475 | €200,95 | €401,89 | €0,00 | €-0,00 |
| Scanner Bottom 5 Short 1H | SOXL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €378,86 | €757,72 | €48,07 | €-0,00 |
| Scanner Bottom 5 Short 1H | SNDK | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €492,80 | €985,60 | €47,71 | €-0,00 |
| Scanner Top10 Long | AKE | LONG | Scanner Top10 Long | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01255 | €187,94 | €375,88 | €45,11 | €0,00 |
| Scanner Top10 Long | ETH | LONG | Scanner Top10 Long | 60m | 2,0x | 2265,72305 | 2350,10000 | 2298,77683 | 1144,19014 | 2396,13352 | €78,65 | €157,31 | €0,00 | €5,86 |
| Scanner Top10 Long | LINK | LONG | Scanner Top10 Long | 60m | 2,0x | 10,57611 | 10,57611 | 10,27850 | 5,34094 | 11,17135 | €817,83 | €1.635,66 | €46,03 | €0,00 |
| Scanner Top10 Long | PEPE | LONG | Scanner Top10 Long | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €19,09 | €38,18 | €0,00 | €1,34 |
| Scanner Top10 Long | BOME | LONG | Scanner Top10 Long | 60m | 2,0x | 0,00114 | 0,00119 | 0,00103 | 0,00058 | 0,00138 | €234,16 | €468,32 | €47,68 | €18,03 |
| Scanner Top10 Long | XRP | LONG | Scanner Top10 Long | 60m | 2,0x | 1,27028 | 1,30921 | 1,28230 | 0,64149 | 1,36326 | €18,94 | €37,87 | €0,00 | €1,16 |
| Scanner Top10 Long | ADA | LONG | Scanner Top10 Long | 60m | 2,0x | 0,20930 | 0,20671 | 0,20193 | 0,10570 | 0,22405 | €643,66 | €1.287,32 | €45,34 | €-15,94 |
| Scanner Bottom10 Short | BEAT | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,28257 | 0,28257 | 0,25514 | 0,42244 | 0,21475 | €204,24 | €408,48 | €0,00 | €-0,00 |
| Scanner Bottom10 Short | SOXL | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom10 Short | SNDK | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Top15 Long | AKE | LONG | Scanner Top15 Long | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01255 | €187,94 | €375,88 | €45,11 | €0,00 |
| Scanner Top15 Long | ETH | LONG | Scanner Top15 Long | 60m | 2,0x | 2265,72305 | 2350,10000 | 2298,77683 | 1144,19014 | 2396,13352 | €78,65 | €157,31 | €0,00 | €5,86 |
| Scanner Top15 Long | LINK | LONG | Scanner Top15 Long | 60m | 2,0x | 10,57611 | 10,57611 | 10,27850 | 5,34094 | 11,17135 | €817,83 | €1.635,66 | €46,03 | €0,00 |
| Scanner Top15 Long | PEPE | LONG | Scanner Top15 Long | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €19,09 | €38,18 | €0,00 | €1,34 |
| Scanner Top15 Long | BOME | LONG | Scanner Top15 Long | 60m | 2,0x | 0,00114 | 0,00119 | 0,00103 | 0,00058 | 0,00138 | €234,16 | €468,32 | €47,68 | €18,03 |
| Scanner Top15 Long | XRP | LONG | Scanner Top15 Long | 60m | 2,0x | 1,27028 | 1,30921 | 1,28230 | 0,64149 | 1,36326 | €18,94 | €37,87 | €0,00 | €1,16 |
| Scanner Top15 Long | ADA | LONG | Scanner Top15 Long | 60m | 2,0x | 0,20930 | 0,20671 | 0,20193 | 0,10570 | 0,22405 | €643,66 | €1.287,32 | €45,34 | €-15,94 |
| Scanner Bottom15 Short | BEAT | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,28257 | 0,28257 | 0,25514 | 0,42244 | 0,21475 | €204,24 | €408,48 | €0,00 | €-0,00 |
| Scanner Bottom15 Short | SOXL | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom15 Short | SNDK | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Top20 Long | AKE | LONG | Scanner Top20 Long | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01255 | €187,94 | €375,88 | €45,11 | €0,00 |
| Scanner Top20 Long | ETH | LONG | Scanner Top20 Long | 60m | 2,0x | 2265,72305 | 2350,10000 | 2298,77683 | 1144,19014 | 2396,13352 | €78,65 | €157,31 | €0,00 | €5,86 |
| Scanner Top20 Long | LINK | LONG | Scanner Top20 Long | 60m | 2,0x | 10,57611 | 10,57611 | 10,27850 | 5,34094 | 11,17135 | €817,83 | €1.635,66 | €46,03 | €0,00 |
| Scanner Top20 Long | PEPE | LONG | Scanner Top20 Long | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €19,09 | €38,18 | €0,00 | €1,34 |
| Scanner Top20 Long | BOME | LONG | Scanner Top20 Long | 60m | 2,0x | 0,00114 | 0,00119 | 0,00103 | 0,00058 | 0,00138 | €234,16 | €468,32 | €47,68 | €18,03 |
| Scanner Top20 Long | XRP | LONG | Scanner Top20 Long | 60m | 2,0x | 1,27028 | 1,30921 | 1,28230 | 0,64149 | 1,36326 | €18,94 | €37,87 | €0,00 | €1,16 |
| Scanner Top20 Long | ADA | LONG | Scanner Top20 Long | 60m | 2,0x | 0,20930 | 0,20671 | 0,20193 | 0,10570 | 0,22405 | €643,66 | €1.287,32 | €45,34 | €-15,94 |
| Scanner Bottom20 Short | BEAT | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,28257 | 0,28257 | 0,25514 | 0,42244 | 0,21475 | €204,24 | €408,48 | €0,00 | €-0,00 |
| Scanner Bottom20 Short | SOXL | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom20 Short | SNDK | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Top 5 + forza BTC 1H | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 86,00620 | 89,31100 | 87,93321 | 43,43313 | 90,05113 | €1.131,85 | €2.263,69 | €0,00 | €86,98 |
| Scanner Top 5 + forza BTC 1H | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 73,54771 | 72,50200 | 70,84505 | 37,14159 | 79,49355 | €663,04 | €1.326,08 | €48,73 | €-18,85 |
| Scanner Top 5 + forza BTC 1H | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00114 | 0,00119 | 0,00103 | 0,00058 | 0,00140 | €239,15 | €478,30 | €48,69 | €18,42 |
| Scanner Top 5 + forza BTC 1H | XRP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,23713 | 1,30921 | 1,27656 | 0,62475 | 1,35194 | €14,19 | €28,38 | €0,00 | €1,65 |
| Scanner Top 5 + forza BTC 1H | ADA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,20285 | 0,20671 | 0,19621 | 0,10244 | 0,21747 | €15,99 | €31,99 | €1,05 | €0,61 |
| Scanner Top 5 + forza BTC 1H | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €664,60 | €1.329,20 | €49,51 | €26,97 |
| Scanner Top5 Btc Mfe V1 | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 86,00620 | 89,31100 | 87,93321 | 43,43313 | 90,05113 | €1.061,05 | €2.122,10 | €0,00 | €81,54 |
| Scanner Top5 Btc Mfe V1 | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 73,54771 | 72,50200 | 70,84505 | 37,14159 | 79,49355 | €621,57 | €1.243,14 | €45,68 | €-17,67 |
| Scanner Top5 Btc Mfe V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00114 | 0,00119 | 0,00103 | 0,00058 | 0,00140 | €224,19 | €448,38 | €45,65 | €17,27 |
| Scanner Top5 Btc Mfe V1 | XRP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,23713 | 1,30921 | 1,27656 | 0,62475 | 1,35194 | €13,30 | €26,61 | €0,00 | €1,55 |
| Scanner Top5 Btc Mfe V1 | ADA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,20285 | 0,20671 | 0,19621 | 0,10244 | 0,21747 | €14,99 | €29,99 | €0,98 | €0,57 |
| Scanner Top5 Btc Mfe V1 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €623,03 | €1.246,06 | €46,42 | €25,28 |
| Scanner Top5 Btc Guard V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01279 | €196,77 | €393,54 | €47,23 | €0,00 |
| Scanner Top5 Btc Guard V1 | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 86,00620 | 89,31100 | 87,93321 | 43,43313 | 90,05113 | €1.108,06 | €2.216,13 | €0,00 | €85,15 |
| Scanner Top5 Btc Guard V1 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €14,28 | €28,57 | €0,00 | €1,54 |
| Scanner Top5 Btc Guard V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00114 | 0,00119 | 0,00103 | 0,00058 | 0,00140 | €228,27 | €456,55 | €46,48 | €17,58 |
| Scanner Top5 Btc Guard V1 | XRP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,27028 | 1,30921 | 1,22380 | 0,64149 | 1,37255 | €18,48 | €36,95 | €1,35 | €1,13 |
| Scanner Top5 Btc Guard V1 | ADA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,20843 | 0,20671 | 0,20147 | 0,10526 | 0,22375 | €722,36 | €1.444,72 | €48,26 | €-11,93 |
| Scanner Top5 Btc Guard V1 | ENA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,12646 | 0,12643 | 0,12068 | 0,06386 | 0,13917 | €13,46 | €26,92 | €1,23 | €-0,01 |
| Scanner Top5 Btc Guard Mfe V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01279 | €192,20 | €384,39 | €46,13 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 86,00620 | 89,31100 | 87,93321 | 43,43313 | 90,05113 | €1.082,29 | €2.164,59 | €0,00 | €83,17 |
| Scanner Top5 Btc Guard Mfe V1 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €13,95 | €27,90 | €0,00 | €1,51 |
| Scanner Top5 Btc Guard Mfe V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00114 | 0,00119 | 0,00103 | 0,00058 | 0,00140 | €222,97 | €445,93 | €45,40 | €17,17 |
| Scanner Top5 Btc Guard Mfe V1 | XRP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,27028 | 1,30921 | 1,22380 | 0,64149 | 1,37255 | €18,05 | €36,09 | €1,32 | €1,11 |
| Scanner Top5 Btc Guard Mfe V1 | ADA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,20843 | 0,20671 | 0,20147 | 0,10526 | 0,22375 | €705,56 | €1.411,12 | €47,14 | €-11,66 |
| Scanner Top5 Btc Guard Mfe V1 | ENA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,12646 | 0,12643 | 0,12068 | 0,06386 | 0,13917 | €13,15 | €26,29 | €1,20 | €-0,01 |
| Scanner Top5 Btc Guard Btc Le3 V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01279 | €199,19 | €398,38 | €47,81 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01279 | €195,77 | €391,54 | €46,99 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | ETH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2256,83128 | 2350,10000 | 2306,95673 | 1139,69979 | 2421,39727 | €964,53 | €1.929,06 | €0,00 | €79,72 |
| Scanner Top5 Btc Runner25 V1 | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 86,00620 | 89,31100 | 87,93321 | 43,43313 | 91,52201 | €12,51 | €25,03 | €0,00 | €0,96 |
| Scanner Top5 Btc Runner25 V1 | LINK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 10,55211 | 10,55211 | 10,31704 | 5,32882 | 11,25731 | €17,19 | €34,38 | €0,77 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 73,54771 | 72,50200 | 70,84505 | 37,14159 | 81,65567 | €64,00 | €127,99 | €4,70 | €-1,82 |
| Scanner Top5 Btc Runner25 V1 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €569,98 | €1.139,95 | €0,00 | €67,04 |
| Scanner Top5 Btc Runner25 V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00116 | 0,00119 | 0,00104 | 0,00059 | 0,00153 | €229,96 | €459,93 | €48,84 | €11,65 |
| Scanner Top5 Btc Runner25 V1 | XRP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,23032 | 1,30921 | 1,27542 | 0,62131 | 1,39012 | €530,99 | €1.061,99 | €0,00 | €68,10 |
| Scanner Top5 Btc Runner25 V1 | ADA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,20285 | 0,20671 | 0,19621 | 0,10244 | 0,22278 | €32,84 | €65,68 | €2,15 | €1,25 |
| Scanner Top5 Btc Runner25 V1 | ENA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,12646 | 0,12643 | 0,12068 | 0,06386 | 0,14379 | €18,15 | €36,30 | €1,66 | €-0,01 |
| Scanner Top5 Btc Tp3 V1 | ETH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2256,83128 | 2350,10000 | 2306,95673 | 1139,69979 | 2421,39727 | €965,10 | €1.930,19 | €0,00 | €79,77 |
| Scanner Top5 Btc Tp3 V1 | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 86,00620 | 89,31100 | 87,93321 | 43,43313 | 91,52201 | €12,52 | €25,04 | €0,00 | €0,96 |
| Scanner Top5 Btc Tp3 V1 | LINK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 10,55211 | 10,55211 | 10,31704 | 5,32882 | 11,25731 | €17,20 | €34,40 | €0,77 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 73,54771 | 72,50200 | 70,84505 | 37,14159 | 81,65567 | €64,03 | €128,07 | €4,71 | €-1,82 |
| Scanner Top5 Btc Tp3 V1 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €570,31 | €1.140,62 | €0,00 | €67,08 |
| Scanner Top5 Btc Tp3 V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00116 | 0,00119 | 0,00104 | 0,00059 | 0,00153 | €230,10 | €460,19 | €48,87 | €11,66 |
| Scanner Top5 Btc Tp3 V1 | XRP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,23032 | 1,30921 | 1,27542 | 0,62131 | 1,39012 | €531,30 | €1.062,61 | €0,00 | €68,14 |
| Scanner Top5 Btc Tp3 V1 | ADA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,20285 | 0,20671 | 0,19621 | 0,10244 | 0,22278 | €32,86 | €65,72 | €2,15 | €1,25 |
| Scanner Top5 Btc Tp3 V1 | ENA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,12646 | 0,12643 | 0,12068 | 0,06386 | 0,14379 | €18,16 | €36,32 | €1,66 | €-0,01 |
| Combo Trend | BEAT | SHORT | Combo Trend | 60m | 2,0x | 0,25984 | 0,25984 | 0,25657 | 0,38847 | 0,19125 | €193,71 | €387,42 | €0,00 | €-0,00 |
| Combo Trend | HYPE | LONG | Combo Trend | 60m | 2,0x | 69,29086 | 72,50200 | 72,11451 | 34,99188 | 76,51998 | €482,28 | €964,56 | €0,00 | €44,70 |
| Combo Trend | ETH | LONG | Combo Trend | 60m | 2,0x | 2264,89289 | 2350,10000 | 2296,53215 | 1143,77091 | 2419,94510 | €734,93 | €1.469,85 | €0,00 | €55,30 |
| Combo Trend | XRP | LONG | Combo Trend | 60m | 2,0x | 1,23032 | 1,30921 | 1,27225 | 0,62131 | 1,36053 | €478,56 | €957,11 | €0,00 | €61,37 |
| Combo Trend | ADA | LONG | Combo Trend | 60m | 2,0x | 0,19795 | 0,20671 | 0,20358 | 0,09996 | 0,21370 | €12,65 | €25,29 | €0,00 | €1,12 |
| Combo Trend | SOL | LONG | Combo Trend | 60m | 2,0x | 88,28565 | 89,31100 | 86,59423 | 44,58426 | 92,00679 | €12,61 | €25,21 | €0,48 | €0,29 |
| Combo Mean Reversion | BEAT | LONG | Combo Mean Reversion | 60m | 2,0x | 0,22830 | 0,22830 | 0,20373 | 0,11529 | 0,26760 | €225,41 | €450,83 | €48,50 | €0,00 |
| Combo Scanner | SOL | LONG | Combo Scanner | 60m | 2,0x | 86,00620 | 89,31100 | 87,93321 | 43,43313 | 90,05113 | €1.085,91 | €2.171,82 | €0,00 | €83,45 |
| Combo Scanner | HYPE | LONG | Combo Scanner | 60m | 2,0x | 73,54771 | 72,50200 | 70,84505 | 37,14159 | 79,49355 | €636,13 | €1.272,26 | €46,75 | €-18,09 |
| Combo Scanner | BOME | LONG | Combo Scanner | 60m | 2,0x | 0,00114 | 0,00119 | 0,00103 | 0,00058 | 0,00140 | €229,44 | €458,89 | €46,72 | €17,67 |
| Combo Scanner | XRP | LONG | Combo Scanner | 60m | 2,0x | 1,23713 | 1,30921 | 1,27656 | 0,62475 | 1,35194 | €13,62 | €27,23 | €0,00 | €1,59 |
| Combo Scanner | ADA | LONG | Combo Scanner | 60m | 2,0x | 0,20285 | 0,20671 | 0,19621 | 0,10244 | 0,21747 | €15,34 | €30,69 | €1,01 | €0,58 |
| Combo Scanner | PEPE | LONG | Combo Scanner | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €637,63 | €1.275,26 | €47,50 | €25,87 |
| Combo Adaptive | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,01735 | 121,01735 | 128,90956 | 180,92093 | 105,23292 | €367,30 | €734,61 | €47,91 | €-0,00 |
| Combo Adaptive | XRP | LONG | Combo Adaptive | 60m | 2,0x | 1,23032 | 1,30921 | 1,27860 | 0,62131 | 1,33685 | €574,74 | €1.149,48 | €0,00 | €73,71 |
| Combo Adaptive | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €616,14 | €1.232,28 | €0,00 | €78,95 |
| Combo Adaptive | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 74,02180 | 72,50200 | 71,44110 | 37,38101 | 79,18321 | €17,24 | €34,48 | €1,20 | €-0,71 |
| Combo Adaptive | SOL | LONG | Combo Adaptive | 60m | 2,0x | 88,28565 | 89,31100 | 86,76337 | 44,58426 | 91,33022 | €24,80 | €49,59 | €0,86 | €0,58 |
| Combo Adaptive | BOME | LONG | Combo Adaptive | 60m | 2,0x | 0,00116 | 0,00119 | 0,00106 | 0,00059 | 0,00137 | €286,94 | €573,88 | €50,57 | €13,22 |
| Combo Adaptive | ADA | LONG | Combo Adaptive | 60m | 2,0x | 0,20506 | 0,20671 | 0,19795 | 0,10356 | 0,21928 | €32,01 | €64,01 | €2,22 | €0,51 |
| Combo Adaptive Mfe Trail | SOL | LONG | Combo Adaptive | 60m | 2,0x | 87,44649 | 89,31100 | 88,80519 | 44,16048 | 90,93241 | €53,92 | €107,83 | €0,00 | €2,30 |
| Combo Adaptive Mfe Trail | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €564,25 | €1.128,50 | €0,00 | €52,69 |
| Combo Adaptive Mfe Trail | SUI | LONG | Combo Adaptive | 60m | 2,0x | 0,73965 | 0,73965 | 0,72101 | 0,37352 | 0,77693 | €17,77 | €35,54 | €0,90 | €0,00 |
| Combo Adaptive Mfe Trail | BOME | LONG | Combo Adaptive | 60m | 2,0x | 0,00113 | 0,00119 | 0,00113 | 0,00057 | 0,00136 | €198,74 | €397,49 | €0,00 | €21,61 |
| Combo Adaptive Mfe Trail | XRP | LONG | Combo Adaptive | 60m | 2,0x | 1,23032 | 1,30921 | 1,28405 | 0,62131 | 1,33685 | €505,43 | €1.010,86 | €0,00 | €64,82 |
| Combo Adaptive Mfe Trail | ETH | LONG | Combo Adaptive | 60m | 2,0x | 2324,84488 | 2350,10000 | 2327,63469 | 1174,04666 | 2438,11520 | €26,46 | €52,93 | €0,00 | €0,57 |
| Combo Adaptive Mfe Trail | ADA | LONG | Combo Adaptive | 60m | 2,0x | 0,19795 | 0,20671 | 0,20522 | 0,09996 | 0,21084 | €13,30 | €26,60 | €0,00 | €1,18 |
| Combo Adaptive Mfe Trail | ENA | LONG | Combo Adaptive | 60m | 2,0x | 0,12646 | 0,12643 | 0,12068 | 0,06386 | 0,13801 | €478,78 | €957,55 | €43,76 | €-0,19 |
| Combo Adaptive Quality7 V1 | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €371,68 | €743,36 | €47,16 | €-0,00 |
| Combo Adaptive Quality7 V1 | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 73,54771 | 72,50200 | 70,84505 | 37,14159 | 78,95302 | €638,10 | €1.276,19 | €46,90 | €-18,14 |
| Combo Adaptive Quality7 V1 | ETH | LONG | Combo Adaptive | 60m | 2,0x | 2339,94790 | 2350,10000 | 2280,80777 | 1181,67369 | 2458,22812 | €39,02 | €78,04 | €1,97 | €0,34 |
| Combo Adaptive Quality7 V1 | XRP | LONG | Combo Adaptive | 60m | 2,0x | 1,23713 | 1,30921 | 1,27966 | 0,62475 | 1,34151 | €555,60 | €1.111,20 | €0,00 | €64,75 |
| Combo Adaptive Quality7 V1 | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €589,54 | €1.179,07 | €0,00 | €35,52 |
| Combo Adaptive Quality7 V1 | ENA | LONG | Combo Adaptive | 60m | 2,0x | 0,12646 | 0,12643 | 0,12068 | 0,06386 | 0,13801 | €14,11 | €28,23 | €1,29 | €-0,01 |
| Combo Adaptive Regime V1 | CYS | SHORT | Combo Adaptive | 60m | 2,0x | 0,73555 | 0,73555 | 0,73555 | 1,09965 | 0,55902 | €202,91 | €405,83 | €0,00 | €-0,00 |
| Combo Adaptive Regime V1 | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 73,54771 | 72,50200 | 70,84505 | 37,14159 | 78,95302 | €680,15 | €1.360,29 | €49,99 | €-19,34 |
| Combo Adaptive Regime V1 | ETH | LONG | Combo Adaptive | 60m | 2,0x | 2278,66564 | 2350,10000 | 2311,06677 | 1150,72615 | 2386,92910 | €48,22 | €96,44 | €0,00 | €3,02 |
| Combo Adaptive Regime V1 | SOL | LONG | Combo Adaptive | 60m | 2,0x | 88,28565 | 89,31100 | 86,76337 | 44,58426 | 91,33022 | €1.383,29 | €2.766,57 | €47,70 | €32,13 |
| Combo Adaptive Regime V1 | XRP | LONG | Combo Adaptive | 60m | 2,0x | 1,27028 | 1,30921 | 1,28499 | 0,64149 | 1,36326 | €575,06 | €1.150,12 | €0,00 | €35,24 |
| Combo Adaptive Regime V1 | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €20,80 | €41,61 | €1,55 | €0,84 |
| Combo Adaptive Quality7 Regime V1 | CYS | SHORT | Combo Adaptive | 60m | 2,0x | 0,73555 | 0,73555 | 0,73555 | 1,09965 | 0,55902 | €199,19 | €398,38 | €0,00 | €-0,00 |
| Combo Adaptive Quality7 Regime V1 | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 73,54771 | 72,50200 | 70,84505 | 37,14159 | 78,95302 | €653,66 | €1.307,32 | €48,04 | €-18,59 |
| Combo Adaptive Quality7 Regime V1 | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €591,47 | €1.182,95 | €0,00 | €69,57 |
| Combo Adaptive Quality7 Regime V1 | BOME | LONG | Combo Adaptive | 60m | 2,0x | 0,00116 | 0,00119 | 0,00107 | 0,00059 | 0,00136 | €285,49 | €570,98 | €47,95 | €12,15 |
| Combo Adaptive Quality7 Regime V1 | XRP | LONG | Combo Adaptive | 60m | 2,0x | 1,27028 | 1,30921 | 1,28499 | 0,64149 | 1,36326 | €19,19 | €38,38 | €0,00 | €1,18 |
| Combo Adaptive Long Only V1 | SOL | LONG | Combo Adaptive | 60m | 2,0x | 87,44649 | 89,31100 | 88,13278 | 44,16048 | 90,93241 | €1.247,44 | €2.494,88 | €0,00 | €53,20 |
| Combo Adaptive Long Only V1 | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €29,71 | €59,42 | €0,00 | €3,49 |
| Combo Adaptive Long Only V1 | XRP | LONG | Combo Adaptive | 60m | 2,0x | 1,23032 | 1,30921 | 1,27860 | 0,62131 | 1,33685 | €573,33 | €1.146,66 | €0,00 | €73,53 |
| Combo Adaptive Long Only V1 | BOME | LONG | Combo Adaptive | 60m | 2,0x | 0,00114 | 0,00119 | 0,00103 | 0,00058 | 0,00138 | €233,67 | €467,34 | €47,58 | €18,00 |
| Combo Adaptive Long Only V1 | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 73,71874 | 72,50200 | 71,23745 | 37,22796 | 78,68131 | €18,24 | €36,48 | €1,23 | €-0,60 |
| Combo Adaptive Long Only V1 | ADA | LONG | Combo Adaptive | 60m | 2,0x | 0,20285 | 0,20671 | 0,20431 | 0,10244 | 0,21614 | €14,83 | €29,66 | €0,00 | €0,56 |
| Combo Adaptive Long Only V1 | ENA | LONG | Combo Adaptive | 60m | 2,0x | 0,12646 | 0,12643 | 0,12068 | 0,06386 | 0,13801 | €554,36 | €1.108,71 | €50,66 | €-0,22 |
| Combo Adaptive Partial 1R V1 | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,01735 | 121,01735 | 128,90956 | 180,92093 | 105,23292 | €352,70 | €705,40 | €46,00 | €-0,00 |
| Combo Adaptive Partial 1R V1 | SOL | LONG | Combo Adaptive | 60m | 2,0x | 87,44649 | 89,31100 | 88,13278 | 44,16048 | 90,93241 | €72,80 | €145,59 | €0,00 | €3,10 |
| Combo Adaptive Partial 1R V1 | XRP | LONG | Combo Adaptive | 60m | 2,0x | 1,23032 | 1,30921 | 1,27860 | 0,62131 | 1,33685 | €552,27 | €1.104,54 | €0,00 | €70,83 |
| Combo Adaptive Partial 1R V1 | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €581,64 | €1.163,27 | €0,00 | €74,53 |
| Combo Adaptive Partial 1R V1 | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 74,02180 | 72,50200 | 71,44110 | 37,38101 | 79,18321 | €16,14 | €32,28 | €1,13 | €-0,66 |
| Combo Adaptive Partial 1R V1 | BOME | LONG | Combo Adaptive | 60m | 2,0x | 0,00116 | 0,00119 | 0,00106 | 0,00059 | 0,00137 | €275,68 | €551,35 | €48,58 | €12,70 |
| Combo Adaptive Partial 1R V1 | ADA | LONG | Combo Adaptive | 60m | 2,0x | 0,20843 | 0,20671 | 0,20147 | 0,10526 | 0,22236 | €13,54 | €27,09 | €0,90 | €-0,22 |
| Combo Adaptive Quality7 Regime Partial 1R V1 | CYS | SHORT | Combo Adaptive | 60m | 2,0x | 0,73555 | 0,73555 | 0,73555 | 1,09965 | 0,55902 | €201,73 | €403,45 | €0,00 | €-0,00 |
| Combo Adaptive Quality7 Regime Partial 1R V1 | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 73,54771 | 72,50200 | 70,84505 | 37,14159 | 78,95302 | €661,99 | €1.323,97 | €48,65 | €-18,82 |
| Combo Adaptive Quality7 Regime Partial 1R V1 | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €599,01 | €1.198,02 | €0,00 | €70,46 |
| Combo Adaptive Quality7 Regime Partial 1R V1 | BOME | LONG | Combo Adaptive | 60m | 2,0x | 0,00116 | 0,00119 | 0,00107 | 0,00059 | 0,00136 | €289,12 | €578,25 | €48,56 | €12,31 |
| Combo Adaptive Quality7 Regime Partial 1R V1 | XRP | LONG | Combo Adaptive | 60m | 2,0x | 1,27028 | 1,30921 | 1,28499 | 0,64149 | 1,36326 | €19,43 | €38,87 | €0,00 | €1,19 |
| Sol Ema 1H | SOL | LONG | Trend following EMA | 60m | 3,0x | 87,44649 | 89,31100 | 88,23180 | 58,73489 | 90,93241 | €823,54 | €2.470,62 | €0,00 | €52,68 |
| Sol Ema 4H | SOL | LONG | Trend following EMA | 240m | 2,0x | 85,47309 | 89,31100 | 87,30972 | 43,16391 | 92,86927 | €715,87 | €1.431,74 | €0,00 | €64,29 |
| Sol Donchian 1H | SOL | LONG | Donchian breakout 20 barre | 60m | 3,0x | 87,44649 | 89,31100 | 88,23180 | 58,73489 | 90,54509 | €937,37 | €2.812,11 | €0,00 | €59,96 |
| Sol Donchian 4H | SOL | LONG | Donchian breakout 20 barre | 240m | 2,0x | 85,47309 | 89,31100 | 87,30972 | 43,16391 | 93,75681 | €727,07 | €1.454,13 | €0,00 | €65,29 |
| Sol Adaptive 1H | SOL | LONG | Combo Adaptive | 60m | 3,0x | 87,44649 | 89,31100 | 88,23180 | 58,73489 | 90,93241 | €811,83 | €2.435,48 | €0,00 | €51,93 |
| Sol Adaptive 4H | SOL | LONG | Combo Adaptive | 240m | 2,0x | 85,47309 | 89,31100 | 87,30972 | 43,16391 | 93,54165 | €665,34 | €1.330,67 | €0,00 | €59,75 |
| Eth Ema 1H | ETH | LONG | Trend following EMA | 60m | 3,0x | 2265,72305 | 2350,10000 | 2306,29586 | 1521,81065 | 2396,13352 | €563,60 | €1.690,79 | €0,00 | €62,97 |
| Eth Ema 4H | ETH | LONG | Trend following EMA | 240m | 2,0x | 2258,11153 | 2350,10000 | 2283,06760 | 1140,34632 | 2498,75762 | €577,20 | €1.154,41 | €0,00 | €47,03 |
| Eth Bollinger 1H | ETH | SHORT | Bollinger mean reversion | 60m | 3,0x | 2339,01210 | 2350,10000 | 2388,27582 | 3106,98774 | 2265,11654 | €770,02 | €2.310,06 | €48,65 | €-10,95 |
| Master Adaptive Expanded V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03814 | 0,02188 | 0,05374 | €197,50 | €395,01 | €47,40 | €0,00 |
| Master Adaptive Runner25 V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03814 | 0,02188 | 0,05894 | €34,77 | €69,54 | €8,34 | €0,00 |
| Combo Adaptive Side Regime Guard V1 | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €632,92 | €1.265,84 | €0,00 | €44,27 |
| Combo Adaptive Side Regime Guard V1 | SUI | LONG | Combo Adaptive | 60m | 2,0x | 0,73965 | 0,73965 | 0,72101 | 0,37352 | 0,77693 | €13,14 | €26,29 | €0,66 | €0,00 |
| Combo Adaptive Side Regime Guard V1 | BOME | LONG | Combo Adaptive | 60m | 2,0x | 0,00113 | 0,00119 | 0,00101 | 0,00057 | 0,00136 | €233,88 | €467,76 | €49,14 | €25,42 |
| Combo Adaptive Side Regime Guard V1 | XRP | LONG | Combo Adaptive | 60m | 2,0x | 1,23032 | 1,30921 | 1,27860 | 0,62131 | 1,33685 | €576,40 | €1.152,79 | €0,00 | €73,92 |
| Combo Adaptive Side Regime Guard V1 | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 72,76855 | 72,50200 | 70,17618 | 36,74812 | 77,95329 | €23,38 | €46,77 | €1,67 | €-0,17 |
| Combo Adaptive Side Regime Guard V1 | ADA | LONG | Combo Adaptive | 60m | 2,0x | 0,20930 | 0,20671 | 0,20193 | 0,10570 | 0,22405 | €721,85 | €1.443,70 | €50,85 | €-17,88 |
| Combo Adaptive Side Regime Guard V1 | ENA | LONG | Combo Adaptive | 60m | 2,0x | 0,12646 | 0,12643 | 0,12068 | 0,06386 | 0,13801 | €17,85 | €35,69 | €1,63 | €-0,01 |
| Master Adaptive Gb20 Loss Cap V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03828 | 0,02188 | 0,05682 | €195,70 | €391,41 | €45,67 | €0,00 |
| Main Side Regime Guard V1 | VELVET | LONG | Confluenza trend | 240m | 3,0x | 0,55987 | 0,55987 | 0,49269 | 0,37605 | 0,69424 | €142,25 | €426,74 | €51,21 | €0,00 |
| Main Side Regime Guard V1 | AKE | LONG | Confluenza trend | 240m | 3,0x | 0,01021 | 0,01021 | 0,00899 | 0,00686 | 0,01266 | €145,97 | €437,90 | €52,55 | €0,00 |
| Main Side Regime Guard V1 | HYPE | LONG | Confluenza trend | 240m | 3,0x | 71,99640 | 72,50200 | 67,63039 | 48,35758 | 80,72841 | €287,94 | €863,83 | €52,38 | €6,07 |
| Main Side Regime Guard V1 | BOME | LONG | Confluenza trend | 240m | 3,0x | 0,00116 | 0,00119 | 0,00102 | 0,00078 | 0,00144 | €145,79 | €437,37 | €52,48 | €9,31 |
| Combo Trend Side Regime Guard V1 | ETH | LONG | Combo Trend | 60m | 2,0x | 2265,72305 | 2350,10000 | 2295,01732 | 1144,19014 | 2425,11361 | €812,72 | €1.625,45 | €0,00 | €60,53 |
| Combo Trend Side Regime Guard V1 | LINK | LONG | Combo Trend | 60m | 2,0x | 10,71314 | 10,71314 | 10,39356 | 5,41014 | 11,41622 | €12,55 | €25,10 | €0,75 | €0,00 |
| Combo Trend Side Regime Guard V1 | PEPE | LONG | Combo Trend | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €584,95 | €1.169,89 | €0,00 | €68,80 |
| Combo Trend Side Regime Guard V1 | SUI | LONG | Combo Trend | 60m | 2,0x | 0,73965 | 0,73965 | 0,71894 | 0,37352 | 0,78521 | €36,53 | €73,06 | €2,05 | €0,00 |
| Combo Trend Side Regime Guard V1 | BOME | LONG | Combo Trend | 60m | 2,0x | 0,00113 | 0,00119 | 0,00100 | 0,00057 | 0,00142 | €223,08 | €446,17 | €52,08 | €24,25 |
| Combo Trend Side Regime Guard V1 | XRP | LONG | Combo Trend | 60m | 2,0x | 1,23032 | 1,30921 | 1,27225 | 0,62131 | 1,36053 | €29,14 | €58,28 | €0,00 | €3,74 |
| Combo Trend Side Regime Guard V1 | ADA | LONG | Combo Trend | 60m | 2,0x | 0,19795 | 0,20671 | 0,20358 | 0,09996 | 0,21370 | €20,16 | €40,31 | €0,00 | €1,78 |
| Combo Trend Side Regime Guard V1 | ENA | LONG | Combo Trend | 60m | 2,0x | 0,12646 | 0,12643 | 0,12003 | 0,06386 | 0,14058 | €518,11 | €1.036,23 | €52,61 | €-0,21 |
| 1H Fast Nohigh Cap75 Short Only V1 | BEAT | SHORT | Momentum / breakout | 60m | 3,0x | 0,24163 | 0,24163 | 0,26822 | 0,32097 | 0,20176 | €151,98 | €455,94 | €50,16 | €-0,00 |
| 1H Balanced V3 Long Only V1 | BEAT | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,25480 | 0,25480 | 0,25418 | 0,33846 | 0,19365 | €130,17 | €390,52 | €0,00 | €-0,00 |
| 1H Balanced V3 Long Only V1 | ETH | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 2248,80967 | 2350,10000 | 2296,55064 | 1510,45050 | 2383,72136 | €502,31 | €1.506,93 | €0,00 | €67,87 |
| 1H Balanced V3 Long Only V1 | SKHYNIX | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1220,85412 | 1220,85412 | 1177,63561 | 820,00702 | 1307,29117 | €435,49 | €1.306,46 | €46,25 | €0,00 |
| 1H Balanced V3 Long Only V1 | PEPE | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €13,83 | €41,49 | €0,00 | €1,45 |
| 1H Balanced V3 Long Only V1 | BOME | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,00117 | 0,00119 | 0,00106 | 0,00079 | 0,00140 | €163,09 | €489,26 | €47,09 | €6,75 |
| 1H Balanced V3 Long Only V1 | HYPE | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 72,76855 | 72,50200 | 70,17618 | 48,87621 | 77,95329 | €12,30 | €36,91 | €1,31 | €-0,14 |
| Scanner Bottom5 Short Profit Lock V1 | BEAT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,28257 | 0,28257 | 0,25514 | 0,42244 | 0,21475 | €202,51 | €405,01 | €0,00 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | SOXL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €381,80 | €763,60 | €48,45 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | SNDK | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €496,62 | €993,25 | €48,08 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | BEAT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,28257 | 0,28257 | 0,25514 | 0,42244 | 0,21475 | €202,81 | €405,63 | €0,00 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | SOXL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €382,38 | €764,76 | €48,52 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | SNDK | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €497,38 | €994,76 | €48,15 | €-0,00 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1H Fast V3 No Esports V1 | PEPE | LONG | 2026-08-21T05:05:45+00:00 | 0,00000 | €68,19 | 1,45 | TARGET |
| 1H Fast V3 No Esports Mfe Lock V1 | PEPE | LONG | 2026-08-21T05:05:45+00:00 | 0,00000 | €69,71 | 1,45 | TARGET |
| Rapida 1H V3 Filtered | PEPE | LONG | 2026-08-21T05:05:45+00:00 | 0,00000 | €69,26 | 1,45 | TARGET |
| 1H Fast Score 6 75 Cost Aware V1 | PEPE | LONG | 2026-08-21T05:05:45+00:00 | 0,00000 | €76,31 | 1,45 | TARGET |
| Scanner Top5 Btc Guard V1 | HYPE | LONG | 2026-08-21T04:06:25+00:00 | 71,96264 | €-0,07 | -0,07 | STOP_GAP_STRESS |
| Scanner Top5 Btc Guard Mfe V1 | HYPE | LONG | 2026-08-21T04:06:25+00:00 | 71,96264 | €-0,07 | -0,07 | STOP_GAP_STRESS |
| Scanner Top20 Long | HYPE | LONG | 2026-08-21T04:06:25+00:00 | 71,96264 | €-53,98 | -1,16 | STOP_GAP_STRESS |
| Scanner Top15 Long | HYPE | LONG | 2026-08-21T04:06:25+00:00 | 71,96264 | €-53,98 | -1,16 | STOP_GAP_STRESS |
| Scanner Top10 Long | HYPE | LONG | 2026-08-21T04:06:25+00:00 | 71,96264 | €-53,98 | -1,16 | STOP_GAP_STRESS |
| Combo Trend Side Regime Guard V1 | HYPE | LONG | 2026-08-21T04:06:25+00:00 | 71,96264 | €16,79 | 0,32 | STOP_GAP_STRESS |
| Combo Adaptive Mfe Trail | HYPE | LONG | 2026-08-21T04:06:25+00:00 | 71,96264 | €-5,55 | -0,13 | STOP_GAP_STRESS |
| 1H Fast V3 No Esports Long Only V1 | HYPE | LONG | 2026-08-21T04:06:25+00:00 | 71,96264 | €-27,42 | -0,58 | STOP_GAP_STRESS |

## Regole invarianti

- Nessuna martingala e nessuna mediazione automatica in perdita.
- Il target mensile riduce il rischio quando viene avvicinato o raggiunto; non lo aumenta mai.
- Il portafoglio principale e le simulazioni di confronto hanno contabilità separata.
- Commissioni, slippage e funding sono inclusi nella simulazione secondo i parametri configurati.
- Quando stop e target risultano toccati nella stessa candela, prevale lo stop salvo modifica esplicita della configurazione.
