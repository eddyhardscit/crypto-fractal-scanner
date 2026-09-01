# Paper trading automatico KuCoin

Generato: 2026-09-01T05:33:34+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-09-01T05:05:31+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-09-01T05:05:31+00:00 | 2026-09-01T05:05:31+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-09-01T04:45:00+00:00 | 2026-09-01T04:45:00+00:00 | 5,8 min | 25,0 min | OK |
| 60m | 12 | 2026-09-01T04:00:00+00:00 | 2026-09-01T04:00:00+00:00 | 5,8 min | 45,0 min | OK |
| 240m | 12 | 2026-09-01T00:00:00+00:00 | 2026-09-01T00:00:00+00:00 | 1,10 h | 1,00 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1H Fast Nohigh Cap75 Short Only V1 | BTR | 60m | LONG | 6,25 | 4,50 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 Nohigh Regime Guard V1 | BTR | 60m | LONG | 6,25 | 4,50 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive Tp3 V1 | BTR | 60m | LONG | 6,25 | 5,00 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive Runner25 V1 | BTR | 60m | LONG | 6,25 | 5,00 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive Quality7 V1 | 0G | 60m | LONG | 7,75 | 7,00 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive | BTR | 60m | LONG | 6,25 | 5,00 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Benchmark Bollinger mean reversion 1H | BTR | 60m | LONG | 6,25 | 5,00 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Donchian 1H Gb20 120R V1 | BTR | 60m | LONG | 6,25 | 5,00 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Benchmark Donchian breakout 1H | BTR | 60m | LONG | 6,25 | 5,00 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | BTR | 60m | LONG | 6,25 | 4,50 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 No Esports Long Only V1 | BTR | 60m | LONG | 6,25 | 4,50 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 Long Nohigh Cap75 V1 | BTR | 60m | LONG | 6,25 | 4,50 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 Nohigh V1 | BTR | 60m | LONG | 6,25 | 4,50 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 Cap75 V1 | BTR | 60m | LONG | 6,25 | 4,50 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast No Pepe V1 | BTR | 60m | LONG | 6,25 | 4,50 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Nohigh Cap75 V1 | BTR | 60m | LONG | 6,25 | 4,50 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Score 6 75 No Trend Up V1 | BTR | 60m | LONG | 6,25 | 6,00 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Score 6 75 V1 | BTR | 60m | LONG | 6,25 | 6,00 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Principale 4H | BTR | 240m | LONG | 8,25 | 6,00 | 0,00 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.8 minuti; tolleranza 60 minuti. |
| Principale 4H | 0G | 240m | LONG | 6,75 | 6,00 | 0,00 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.8 minuti; tolleranza 60 minuti. |
| Principale 4H | HYPE | 240m | LONG | 5,83 | 6,00 | 0,17 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.8 minuti; tolleranza 60 minuti. |
| Principale 4H | DOGE | 240m | SHORT | -4,67 | 6,00 | 1,33 | STALE_CANDLE | 1,10 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.8 minuti; tolleranza 60 minuti. |
| Principale 4H | SKR | 240m | LONG | 4,25 | 6,00 | 1,75 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.8 minuti; tolleranza 60 minuti. |
| Principale 4H | ETH | 240m | LONG | 3,32 | 6,00 | 2,68 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.8 minuti; tolleranza 60 minuti. |
| Principale 4H | SOL | 240m | LONG | 2,92 | 6,00 | 3,08 | STALE_CANDLE | 1,10 h | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.8 minuti; tolleranza 60 minuti. |
| Principale 4H | BTC | 240m | LONG | 2,50 | 6,00 | 3,50 | STALE_CANDLE | 1,10 h | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.8 minuti; tolleranza 60 minuti. |
| Principale 4H | XRP | 240m | LONG | 2,20 | 6,00 | 3,80 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.8 minuti; tolleranza 60 minuti. |
| Principale 4H | PEPE | 240m | SHORT | -2,11 | 6,00 | 3,89 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.8 minuti; tolleranza 60 minuti. |
| Bilanciata 1H V1 | 0G | 60m | LONG | 7,75 | 5,00 | 0,00 | READY | 5,8 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Balanced Long No Rhv V1 | 0G | 60m | LONG | 7,75 | 5,00 | 0,00 | READY | 5,8 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Bilanciata 1H V2 | 0G | 60m | LONG | 7,75 | 5,50 | 0,00 | READY | 5,8 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Fast Tp2 V1 | 0G | 60m | LONG | 7,75 | 4,50 | 0,00 | READY | 5,8 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Rapida 1H V3 Filtered | 0G | 60m | LONG | 7,75 | 4,50 | 0,00 | READY | 5,8 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Fast V3 Long Only V1 | 0G | 60m | LONG | 7,75 | 4,50 | 0,00 | READY | 5,8 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Fast V3 No Esports V1 | 0G | 60m | LONG | 7,75 | 4,50 | 0,00 | READY | 5,8 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Fast V3 No Esports Mfe Lock V1 | 0G | 60m | LONG | 7,75 | 4,50 | 0,00 | READY | 5,8 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Forza relativa 1H V1 | 0G | 60m | LONG | 7,75 | 4,00 | 0,00 | READY | 5,8 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Forza relativa 1H V2 | 0G | 60m | LONG | 7,75 | 5,50 | 0,00 | READY | 5,8 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.808,64 | -1,91% | €0,08 | €3.000,00 | 0,00% | 6 | 55 | 40,00% | 0,87 | 6,86% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 55 | 2614 | PRIME INDICAZIONI | 100 (mancano 45) |

- Trade del Principale 4H chiusi: **55**; win rate **40,00%**; profit factor **0,87**.
- Expectancy: **€-3,43** per trade; P&L netto: **€-188,91**; max drawdown: **6,86%**.
- Valutazione: **Si può osservare la direzione, ma il risultato resta fragile.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 6 | €9.808,64 | €699,80 | €2.099,39 | €196,16 | €-1,34 |
| TEST | Benchmark Donchian breakout 1H | 6 | €11.279,15 | €1.455,42 | €2.910,84 | €225,59 | €-26,93 |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | 6 | €11.052,85 | €1.066,62 | €3.199,87 | €221,33 | €-13,23 |
| TEST | Donchian 1H Gb20 120R V1 | 6 | €11.013,60 | €1.421,15 | €2.842,31 | €220,28 | €-26,30 |
| TEST | Scanner Top 5 Long 1H | 6 | €10.896,46 | €1.961,65 | €3.923,29 | €218,22 | €-12,39 |
| TEST | Main Side Regime Guard V1 | 6 | €10.878,60 | €709,59 | €2.128,78 | €216,87 | €-1,81 |
| TEST | Combo Trend Side Regime Guard V1 | 5 | €10.783,49 | €3.117,35 | €6.234,69 | €163,40 | €-18,52 |
| TEST | 1H Fast No Pepe V1 | 7 | €10.585,67 | €1.291,70 | €3.875,10 | €210,35 | €-0,11 |
| TEST | Combo Adaptive Long Only V1 | 5 | €10.351,35 | €2.522,24 | €5.044,48 | €206,79 | €0,00 |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | 5 | €10.340,45 | €633,51 | €1.900,53 | €206,82 | €-16,33 |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | 5 | €10.339,03 | €1.055,97 | €3.167,91 | €207,08 | €-14,79 |
| TEST | Combo Adaptive | 8 | €10.334,40 | €2.393,01 | €4.786,01 | €206,69 | €-0,51 |
| TEST | Sol Donchian 1H | 0 | €10.333,40 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 0 | €10.300,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Nohigh Range Only V1 | 2 | €10.299,65 | €883,96 | €2.651,87 | €102,78 | €-15,27 |
| TEST | Ampia 4H | 8 | €10.298,05 | €1.071,19 | €2.142,37 | €207,40 | €18,27 |
| TEST | Rapida 1H V2 | 1 | €10.282,28 | €749,31 | €2.247,94 | €51,80 | €0,00 |
| TEST | Rapida 1H V3 Filtered | 5 | €10.272,61 | €1.049,19 | €3.147,56 | €205,75 | €-14,69 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 0 | €10.271,73 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 0 | €10.239,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 0 | €10.235,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 4H | 1 | €10.228,19 | €407,92 | €815,83 | €51,22 | €-14,80 |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | 1 | €10.222,39 | €739,04 | €2.217,11 | €51,09 | €0,00 |
| TEST | Btc Bollinger 1H | 0 | €10.209,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Score 6 75 Range Only V1 | 3 | €10.201,86 | €1.085,65 | €3.256,95 | €152,85 | €-15,13 |
| TEST | Scanner Top 5 + forza BTC 1H | 6 | €10.195,75 | €1.838,51 | €3.677,03 | €204,19 | €-11,64 |
| TEST | Sol Donchian 4H | 1 | €10.194,94 | €449,62 | €899,24 | €50,98 | €-1,25 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 0 | €10.185,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 0 | €10.145,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 1H | 0 | €10.123,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top10 Long | 6 | €10.121,84 | €3.047,06 | €6.094,13 | €202,70 | €-11,49 |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 0 | €10.099,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 4H | 1 | €10.092,89 | €439,17 | €878,34 | €50,55 | €-15,93 |
| TEST | Combo Adaptive Side Regime Guard V1 | 5 | €10.065,35 | €2.132,62 | €4.265,23 | €149,20 | €0,00 |
| TEST | 1H Fast Nohigh Cap75 V1 | 4 | €10.061,24 | €587,08 | €1.761,25 | €200,36 | €-15,70 |
| TEST | Combo Adaptive Partial 1R V1 | 5 | €10.060,82 | €2.047,93 | €4.095,87 | €151,40 | €-2,18 |
| TEST | Main Dynamic Asset Selector V1 | 1 | €10.057,80 | €140,98 | €422,93 | €50,75 | €0,00 |
| TEST | Btc Bollinger 4H | 1 | €10.057,49 | €775,58 | €1.551,16 | €0,00 | €27,42 |
| TEST | 1H Fast Tp2 V1 | 5 | €10.055,44 | €566,04 | €1.698,13 | €151,10 | €-13,93 |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 0 | €10.048,77 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Tp3 V1 | 4 | €10.045,44 | €2.011,34 | €4.022,68 | €200,72 | €0,00 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €10.045,08 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V1 | 0 | €10.043,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Runner25 V1 | 4 | €10.039,57 | €2.010,16 | €4.020,33 | €200,60 | €0,00 |
| TEST | 1H Balanced Short Trend Down Strict V1 | 0 | €10.035,46 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · prudente · 5x | 0 | €10.034,19 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Donchian 1H | 0 | €10.021,07 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Bollinger 1H | 0 | €10.021,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €50 · 15x | 0 | €10.017,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 4H | 0 | €10.017,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €50 · 15x | 0 | €10.009,44 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 0 | €10.009,02 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 0 | €10.008,92 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €10 · 15x | 0 | €10.003,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 0 | €10.003,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 1H | 0 | €10.003,16 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €10 · 15x | 0 | €10.001,89 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Ema 1H | 1 | €10.001,40 | €1.077,39 | €3.232,18 | €50,16 | €-28,15 |
| TEST | Scanner Bottom5 Short Continuation V1 | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €10 · 15x | 0 | €9.999,08 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €10 · 15x | 0 | €9.997,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €50 · 15x | 0 | €9.995,41 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 0 | €9.995,23 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · prudente · 5x | 0 | €9.991,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €10 · 15x | 0 | €9.989,49 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €50 · 15x | 0 | €9.988,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · prudente · 5x | 0 | €9.980,94 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 0 | €9.974,70 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 1H | 0 | €9.968,58 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 4H | 0 | €9.966,88 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 4H | 1 | €9.959,61 | €478,97 | €957,94 | €0,00 | €29,84 |
| TEST | 1H Fast V3 No Esports Long Only V1 | 6 | €9.959,32 | €1.015,89 | €3.047,66 | €199,19 | €-0,09 |
| TEST | Scalp RSI Long 25 · €50 · 15x | 0 | €9.947,46 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.939,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · prudente · 5x | 0 | €9.939,55 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 4H | 0 | €9.913,56 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 1H | 0 | €9.902,26 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Ema 4H | 0 | €9.887,30 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Nohigh V1 | 5 | €9.876,33 | €1.160,67 | €3.482,00 | €196,46 | €-1,45 |
| TEST | Sol Bollinger 1H | 0 | €9.860,14 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Adaptive 1H | 0 | €9.857,66 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Forza relativa 1H V2 | 6 | €9.839,71 | €1.164,39 | €2.328,78 | €148,71 | €-0,29 |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 0 | €9.837,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top15 Long | 7 | €9.829,07 | €2.872,90 | €5.745,81 | €196,85 | €-11,60 |
| TEST | Scanner Top20 Long | 7 | €9.829,07 | €2.872,90 | €5.745,81 | €196,85 | €-11,60 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 0 | €9.817,34 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | 4 | €9.810,87 | €572,47 | €1.717,42 | €195,37 | €-15,31 |
| TEST | Combo Scanner | 7 | €9.780,82 | €1.273,80 | €2.547,61 | €147,50 | €22,40 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 0 | €9.762,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Donchian 1H | 0 | €9.752,59 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Long Only V1 | 5 | €9.737,87 | €1.380,10 | €4.140,29 | €194,06 | €0,00 |
| TEST | Eth Ema 1H | 0 | €9.730,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | 0 | €9.726,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 0 | €9.723,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Global Confluence puro 1H | 1 | €9.716,42 | €1.335,17 | €2.670,35 | €48,67 | €-17,08 |
| TEST | Eth Bollinger 1H | 0 | €9.649,49 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Balanced Long No Rhv V1 | 5 | €9.647,44 | €1.132,87 | €3.398,61 | €192,95 | €0,00 |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | 4 | €9.645,79 | €655,02 | €1.965,07 | €192,08 | €-14,89 |
| TEST | Combo Adaptive Quality7 Regime V1 | 0 | €9.603,78 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H V3 Filtered | 4 | €9.598,72 | €2.292,58 | €6.877,75 | €192,22 | €-19,78 |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | 2 | €9.580,90 | €728,45 | €2.185,35 | €97,43 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 0 | €9.579,83 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 1H | 0 | €9.567,24 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Mfe V1 | 6 | €9.558,01 | €1.723,52 | €3.447,03 | €191,41 | €-10,91 |
| TEST | Combo Adaptive Regime V1 | 1 | €9.541,28 | €987,06 | €1.974,12 | €49,09 | €0,00 |
| TEST | Combo Adaptive Quality7 V1 | 4 | €9.514,11 | €1.438,51 | €2.877,02 | €190,29 | €-0,26 |
| TEST | 1H Fast V3 No Esports V1 | 5 | €9.498,54 | €581,99 | €1.745,97 | €190,25 | €-13,75 |
| TEST | Scanner Top5 Btc Guard V1 | 5 | €9.471,54 | €1.103,75 | €2.207,51 | €189,83 | €-20,06 |
| TEST | Master Adaptive Gb20 Be V1 | 5 | €9.452,15 | €1.185,85 | €2.371,71 | €188,54 | €25,41 |
| TEST | Master Adaptive Gb20 Partial V1 | 5 | €9.442,09 | €1.184,59 | €2.369,19 | €188,34 | €25,39 |
| TEST | Master Adaptive Expanded V1 | 5 | €9.407,63 | €1.578,98 | €3.157,97 | €187,39 | €38,11 |
| TEST | Master Adaptive V1 | 5 | €9.405,57 | €1.180,01 | €2.360,02 | €187,61 | €25,29 |
| TEST | 1H Fast Score 6 75 V1 | 2 | €9.400,50 | €287,74 | €863,21 | €94,08 | €-14,85 |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | 4 | €9.371,20 | €636,91 | €1.910,74 | €186,61 | €-14,29 |
| TEST | Scanner Bottom10 Short | 4 | €9.320,74 | €1.261,36 | €2.522,73 | €140,86 | €0,00 |
| TEST | Scanner Bottom15 Short | 4 | €9.320,74 | €1.261,36 | €2.522,73 | €140,86 | €0,00 |
| TEST | Scanner Bottom20 Short | 4 | €9.320,74 | €1.261,36 | €2.522,73 | €140,86 | €0,00 |
| TEST | Master Adaptive Runner25 V1 | 6 | €9.300,22 | €1.120,88 | €2.241,76 | €185,47 | €26,71 |
| TEST | Master Adaptive Gb20 V1 | 5 | €9.281,47 | €1.164,37 | €2.328,75 | €185,14 | €24,96 |
| TEST | Bilanciata 1H V2 | 4 | €9.264,49 | €1.673,84 | €5.021,51 | €185,13 | €-12,95 |
| TEST | Master Adaptive Gb20 Loss Cap V1 | 7 | €9.256,43 | €989,92 | €1.979,84 | €184,20 | €48,82 |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | 4 | €9.256,15 | €1.252,64 | €2.505,29 | €139,88 | €0,00 |
| TEST | Scanner Top5 Btc Guard Mfe V1 | 5 | €9.251,26 | €1.078,08 | €2.156,17 | €185,42 | €-19,59 |
| TEST | Scanner Bottom5 Short Profit Lock V1 | 4 | €9.242,07 | €1.250,74 | €2.501,48 | €139,67 | €0,00 |
| TEST | Scanner Bottom 5 Short 1H | 4 | €9.170,95 | €1.241,11 | €2.482,23 | €138,60 | €0,00 |
| TEST | Master Adaptive No Alt V1 | 5 | €9.157,28 | €2.116,02 | €4.232,05 | €182,50 | €-4,23 |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | 2 | €9.150,56 | €280,09 | €840,26 | €91,58 | €-14,46 |
| TEST | Benchmark trend following EMA 1H | 5 | €9.128,05 | €1.163,49 | €2.326,98 | €138,04 | €-1,79 |
| TEST | Bilanciata 1H V1 | 4 | €9.116,51 | €2.435,53 | €7.306,59 | €182,90 | €-29,80 |
| TEST | 1H Fast V3 Cap75 V1 | 2 | €9.091,36 | €278,27 | €834,82 | €90,99 | €-14,36 |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | 5 | €9.083,03 | €1.091,72 | €2.183,43 | €182,04 | €-19,24 |
| TEST | 1H Balanced V3 Long Only V1 | 4 | €9.078,64 | €2.168,36 | €6.505,09 | €181,81 | €-18,71 |
| TEST | Combo Adaptive Mfe Trail | 6 | €9.068,08 | €1.313,44 | €2.626,88 | €181,59 | €-11,29 |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | 4 | €9.044,42 | €3.073,30 | €6.146,60 | €181,46 | €-7,78 |
| TEST | Combo Trend | 4 | €9.037,34 | €3.046,93 | €6.093,86 | €134,65 | €-20,72 |
| TEST | Combo Adaptive Runner25 V1 | 4 | €8.936,19 | €3.002,02 | €6.004,04 | €178,73 | €-24,32 |
| TEST | Combo Mean Reversion | 1 | €8.823,89 | €942,00 | €1.883,99 | €44,59 | €0,00 |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | 3 | €8.819,14 | €1.876,41 | €3.752,81 | €132,48 | €5,13 |
| TEST | Combo Adaptive Tp3 V1 | 4 | €8.769,24 | €2.945,94 | €5.891,87 | €175,39 | €-23,87 |
| TEST | Benchmark Bollinger mean reversion 1H | 1 | €8.740,20 | €204,31 | €408,62 | €43,70 | €-0,08 |
| TEST | Master Adaptive Strict3 V1 | 2 | €8.705,20 | €393,65 | €787,30 | €86,45 | €0,00 |
| TEST | Scanner Top5 Btc Btc Le3 V1 | 1 | €8.701,51 | €847,75 | €1.695,49 | €43,45 | €0,00 |
| TEST | Forza relativa 1H V1 | 4 | €8.409,69 | €2.440,42 | €4.880,85 | €168,85 | €-32,89 |

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
| PRINCIPALE | Principale 4H | Confluenza trend | €9.808,64 | €-188,91 | 55 | 55 | 40,00% | 0,87 | €-3,43 | 6,86% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €11.279,15 | €1.307,01 | 118 | 118 | 46,61% | 1,50 | €11,08 | 6,75% |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | Momentum / breakout | €11.052,85 | €1.068,37 | 166 | 166 | 51,20% | 1,31 | €6,44 | 5,52% |
| TEST | Donchian 1H Gb20 120R V1 | Donchian breakout 20 barre | €11.013,60 | €1.040,80 | 86 | 86 | 45,35% | 1,60 | €12,10 | 6,75% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.896,46 | €911,36 | 157 | 157 | 47,13% | 1,30 | €5,80 | 8,85% |
| TEST | Main Side Regime Guard V1 | Confluenza trend | €10.878,60 | €882,05 | 41 | 41 | 56,10% | 2,24 | €21,51 | 3,82% |
| TEST | Combo Trend Side Regime Guard V1 | Combo Trend | €10.783,49 | €805,52 | 132 | 132 | 51,52% | 1,32 | €6,10 | 8,10% |
| TEST | 1H Fast No Pepe V1 | Momentum / breakout | €10.585,67 | €587,94 | 252 | 252 | 44,84% | 1,13 | €2,33 | 7,89% |
| TEST | Combo Adaptive Long Only V1 | Combo Adaptive | €10.351,35 | €354,38 | 139 | 139 | 46,04% | 1,12 | €2,55 | 7,78% |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | Momentum / breakout V3 Filtered | €10.340,45 | €357,91 | 90 | 90 | 47,78% | 1,20 | €3,98 | 5,24% |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | Momentum / breakout V3 Filtered | €10.339,03 | €355,83 | 206 | 206 | 49,51% | 1,10 | €1,73 | 9,50% |
| TEST | Combo Adaptive | Combo Adaptive | €10.334,40 | €337,64 | 174 | 174 | 45,40% | 1,11 | €1,94 | 7,91% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €10.333,40 | €333,40 | 16 | 16 | 62,50% | 2,35 | €20,84 | 2,77% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | Momentum / breakout V3 Filtered | €10.300,05 | €300,05 | 33 | 33 | 48,48% | 2,04 | €9,09 | 2,01% |
| TEST | 1H Fast V3 Nohigh Range Only V1 | Momentum / breakout V3 Filtered | €10.299,65 | €316,33 | 52 | 52 | 48,08% | 1,26 | €6,08 | 3,97% |
| TEST | Ampia 4H | Confluenza trend | €10.298,05 | €280,43 | 52 | 52 | 34,62% | 1,24 | €5,39 | 4,45% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €10.282,28 | €283,43 | 54 | 49 | 48,15% | 1,22 | €5,25 | 3,89% |
| TEST | Rapida 1H V3 Filtered | Momentum / breakout V3 Filtered | €10.272,61 | €289,30 | 250 | 250 | 44,40% | 1,06 | €1,16 | 9,48% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | Momentum / breakout V3 Filtered | €10.271,73 | €271,73 | 22 | 22 | 50,00% | 1,74 | €12,35 | 1,72% |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | Momentum / breakout V3 Filtered | €10.239,20 | €239,20 | 17 | 17 | 52,94% | 4,50 | €14,07 | 1,01% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | Momentum / breakout V3 Filtered | €10.235,18 | €235,18 | 20 | 20 | 50,00% | 1,90 | €11,76 | 2,73% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €10.228,19 | €243,28 | 8 | 8 | 62,50% | 3,16 | €30,41 | 1,01% |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | Momentum / breakout V3 Filtered | €10.222,39 | €223,53 | 77 | 77 | 49,35% | 1,13 | €2,90 | 4,50% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.209,20 | €209,20 | 6 | 6 | 83,33% | 4,66 | €34,87 | 0,85% |
| TEST | 1H Fast Score 6 75 Range Only V1 | Momentum / breakout | €10.201,86 | €218,75 | 42 | 42 | 45,24% | 1,21 | €5,21 | 3,79% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €10.195,75 | €209,75 | 140 | 140 | 44,29% | 1,07 | €1,50 | 11,27% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €10.194,94 | €196,46 | 6 | 6 | 50,00% | 2,73 | €32,74 | 1,05% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | Momentum / breakout V3 Filtered | €10.185,37 | €185,37 | 22 | 22 | 40,91% | 1,57 | €8,43 | 2,27% |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | Momentum / breakout V3 Filtered | €10.145,12 | €145,12 | 44 | 44 | 45,45% | 1,20 | €3,30 | 2,91% |
| TEST | Sol Ema 1H | Trend following EMA | €10.123,38 | €123,38 | 18 | 18 | 44,44% | 1,25 | €6,85 | 3,33% |
| TEST | Scanner Top10 Long | Scanner Top10 Long | €10.121,84 | €137,10 | 150 | 150 | 46,67% | 1,05 | €0,91 | 10,31% |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | Momentum / breakout V3 Filtered | €10.099,04 | €99,04 | 55 | 55 | 54,55% | 1,12 | €1,80 | 3,59% |
| TEST | Sol Ema 4H | Trend following EMA | €10.092,89 | €109,13 | 9 | 9 | 44,44% | 1,51 | €12,13 | 2,27% |
| TEST | Combo Adaptive Side Regime Guard V1 | Combo Adaptive | €10.065,35 | €67,74 | 135 | 135 | 45,93% | 1,02 | €0,50 | 9,42% |
| TEST | 1H Fast Nohigh Cap75 V1 | Momentum / breakout | €10.061,24 | €78,00 | 173 | 173 | 41,04% | 1,02 | €0,45 | 7,43% |
| TEST | Combo Adaptive Partial 1R V1 | Combo Adaptive | €10.060,82 | €65,41 | 165 | 165 | 44,85% | 1,03 | €0,40 | 8,69% |
| TEST | Main Dynamic Asset Selector V1 | Confluenza trend | €10.057,80 | €58,16 | 15 | 15 | 33,33% | 1,13 | €3,88 | 3,39% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.057,49 | €29,45 | 2 | 2 | 50,00% | 1,54 | €14,72 | 0,91% |
| TEST | 1H Fast Tp2 V1 | Momentum / breakout | €10.055,44 | €70,38 | 245 | 245 | 39,18% | 1,02 | €0,29 | 6,56% |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | Momentum / breakout V3 Filtered | €10.048,77 | €48,77 | 23 | 23 | 43,48% | 1,12 | €2,12 | 3,05% |
| TEST | Scanner Top5 Btc Tp3 V1 | Scanner Top 5 + forza BTC | €10.045,44 | €47,86 | 122 | 122 | 40,16% | 1,02 | €0,39 | 11,78% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €10.045,08 | €45,08 | 28 | 28 | 46,43% | 1,40 | €1,61 | 0,33% |
| TEST | Rapida 1H V1 | Momentum / breakout | €10.043,28 | €43,28 | 78 | 78 | 34,62% | 1,02 | €0,55 | 6,76% |
| TEST | Scanner Top5 Btc Runner25 V1 | Scanner Top 5 + forza BTC | €10.039,57 | €41,98 | 126 | 126 | 40,48% | 1,02 | €0,33 | 12,06% |
| TEST | 1H Balanced Short Trend Down Strict V1 | Confluenza trend | €10.035,46 | €35,46 | 13 | 13 | 38,46% | 1,13 | €2,73 | 1,80% |
| TEST | Scalp RSI Long 20 · prudente · 5x | Inversione RSI estrema 15m | €10.034,19 | €34,19 | 10 | 10 | 60,00% | 1,95 | €3,42 | 0,36% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €10.021,07 | €21,07 | 14 | 14 | 57,14% | 1,06 | €1,51 | 3,08% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €10.021,05 | €21,05 | 12 | 12 | 58,33% | 1,07 | €1,75 | 1,89% |
| TEST | Scalp RSI Short 85 · €50 · 15x | Inversione RSI estrema 15m | €10.017,98 | €17,98 | 5 | 5 | 60,00% | 1,69 | €3,60 | 0,31% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €10.017,60 | €17,60 | 3 | 3 | 33,33% | 1,17 | €5,87 | 0,96% |
| TEST | Scalp RSI Short 80 · €50 · 15x | Inversione RSI estrema 15m | €10.009,44 | €9,44 | 17 | 17 | 41,18% | 1,17 | €0,56 | 0,53% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €10.009,02 | €9,02 | 28 | 28 | 46,43% | 1,40 | €0,32 | 0,07% |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | Momentum / breakout V3 Filtered | €10.008,92 | €8,92 | 30 | 30 | 36,67% | 1,02 | €0,30 | 4,84% |
| TEST | Scalp RSI Short 85 · €10 · 15x | Inversione RSI estrema 15m | €10.003,60 | €3,60 | 5 | 5 | 60,00% | 1,69 | €0,72 | 0,06% |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | Momentum / breakout V3 Filtered | €10.003,37 | €3,37 | 8 | 8 | 37,50% | 1,02 | €0,42 | 2,15% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €10.003,16 | €3,16 | 20 | 20 | 45,00% | 1,01 | €0,16 | 4,59% |
| TEST | Scalp RSI Short 80 · €10 · 15x | Inversione RSI estrema 15m | €10.001,89 | €1,89 | 17 | 17 | 41,18% | 1,17 | €0,11 | 0,11% |
| TEST | Doge Ema 1H | Trend following EMA | €10.001,40 | €31,49 | 19 | 19 | 57,89% | 1,07 | €1,66 | 2,77% |
| TEST | Scanner Bottom5 Short Continuation V1 | Scanner Bottom5 Short Continuation | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 20 · €10 · 15x | Inversione RSI estrema 15m | €9.999,08 | €-0,92 | 10 | 10 | 40,00% | 0,80 | €-0,09 | 0,04% |
| TEST | Scalp RSI Long 15 · €10 · 15x | Inversione RSI estrema 15m | €9.997,60 | €-2,40 | 3 | 3 | 33,33% | 0,13 | €-0,80 | 0,02% |
| TEST | Scalp RSI Long 20 · €50 · 15x | Inversione RSI estrema 15m | €9.995,41 | €-4,59 | 10 | 10 | 40,00% | 0,80 | €-0,46 | 0,21% |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | Momentum / breakout V3 Filtered | €9.995,23 | €-4,77 | 15 | 15 | 46,67% | 0,99 | €-0,32 | 2,70% |
| TEST | Scalp RSI Short 85 · prudente · 5x | Inversione RSI estrema 15m | €9.991,38 | €-8,62 | 5 | 5 | 60,00% | 0,61 | €-1,72 | 0,30% |
| TEST | Scalp RSI Long 25 · €10 · 15x | Inversione RSI estrema 15m | €9.989,49 | €-10,51 | 16 | 16 | 37,50% | 0,33 | €-0,66 | 0,14% |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | €9.988,00 | €-12,00 | 3 | 3 | 33,33% | 0,13 | €-4,00 | 0,12% |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | €9.980,94 | €-19,06 | 3 | 3 | 33,33% | 0,19 | €-6,35 | 0,20% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €9.974,70 | €-25,30 | 16 | 16 | 37,50% | 0,71 | €-1,58 | 0,71% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €9.968,58 | €-31,42 | 9 | 9 | 44,44% | 0,86 | €-3,49 | 1,23% |
| TEST | Btc Ema 4H | Trend following EMA | €9.966,88 | €-33,12 | 4 | 4 | 25,00% | 0,78 | €-8,28 | 1,76% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €9.959,61 | €-69,33 | 4 | 4 | 25,00% | 0,56 | €-17,33 | 1,96% |
| TEST | 1H Fast V3 No Esports Long Only V1 | Momentum / breakout V3 Filtered | €9.959,32 | €-38,75 | 190 | 190 | 42,11% | 0,99 | €-0,20 | 10,60% |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | €9.947,46 | €-52,54 | 16 | 16 | 37,50% | 0,33 | €-3,28 | 0,72% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.939,62 | €-60,38 | 28 | 28 | 46,43% | 0,60 | €-2,16 | 0,84% |
| TEST | Scalp RSI Short 80 · prudente · 5x | Inversione RSI estrema 15m | €9.939,55 | €-60,45 | 17 | 17 | 35,29% | 0,39 | €-3,56 | 0,89% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €9.913,56 | €-86,44 | 5 | 5 | 20,00% | 0,61 | €-17,29 | 2,43% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €9.902,26 | €-97,74 | 11 | 11 | 45,45% | 0,71 | €-8,89 | 1,66% |
| TEST | Eth Ema 4H | Trend following EMA | €9.887,30 | €-112,70 | 7 | 7 | 28,57% | 0,57 | €-16,10 | 1,83% |
| TEST | 1H Fast V3 Nohigh V1 | Momentum / breakout V3 Filtered | €9.876,33 | €-120,41 | 146 | 146 | 43,84% | 0,96 | €-0,82 | 7,10% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.860,14 | €-139,86 | 14 | 14 | 42,86% | 0,72 | €-9,99 | 2,91% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.857,66 | €-142,34 | 16 | 16 | 43,75% | 0,72 | €-8,90 | 3,14% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €9.839,71 | €-158,44 | 128 | 121 | 41,41% | 0,95 | €-1,24 | 10,88% |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | Momentum / breakout V3 Filtered | €9.837,38 | €-162,62 | 37 | 37 | 40,54% | 0,76 | €-4,40 | 3,08% |
| TEST | Scanner Top15 Long | Scanner Top15 Long | €9.829,07 | €-155,74 | 149 | 149 | 46,31% | 0,94 | €-1,05 | 10,31% |
| TEST | Scanner Top20 Long | Scanner Top20 Long | €9.829,07 | €-155,74 | 149 | 149 | 46,31% | 0,94 | €-1,05 | 10,31% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | Momentum / breakout V3 Filtered | €9.817,34 | €-182,66 | 24 | 24 | 41,67% | 0,64 | €-7,61 | 3,23% |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | Momentum / breakout | €9.810,87 | €-172,79 | 137 | 137 | 39,42% | 0,93 | €-1,26 | 7,43% |
| TEST | Combo Scanner | Combo Scanner | €9.780,82 | €-241,33 | 146 | 146 | 43,84% | 0,93 | €-1,65 | 11,38% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | Momentum / breakout V3 Filtered | €9.762,18 | €-237,82 | 7 | 7 | 14,29% | 0,02 | €-33,97 | 2,82% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.752,59 | €-247,41 | 15 | 15 | 33,33% | 0,59 | €-16,49 | 3,74% |
| TEST | 1H Fast V3 Long Only V1 | Momentum / breakout V3 Filtered | €9.737,87 | €-259,65 | 192 | 192 | 41,15% | 0,93 | €-1,35 | 12,52% |
| TEST | Eth Ema 1H | Trend following EMA | €9.730,62 | €-269,38 | 23 | 23 | 39,13% | 0,66 | €-11,71 | 4,80% |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | Combo Adaptive | €9.726,12 | €-273,88 | 46 | 46 | 43,48% | 0,79 | €-5,95 | 4,21% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | Momentum / breakout V3 Filtered | €9.723,72 | €-276,28 | 31 | 31 | 32,26% | 0,62 | €-8,91 | 4,83% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.716,42 | €-265,30 | 18 | 18 | 33,33% | 0,51 | €-14,74 | 3,93% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €9.649,49 | €-350,51 | 8 | 8 | 25,00% | 0,19 | €-43,81 | 4,16% |
| TEST | 1H Balanced Long No Rhv V1 | Confluenza trend | €9.647,44 | €-350,46 | 114 | 114 | 43,86% | 0,84 | €-3,07 | 9,26% |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | Momentum / breakout V3 Filtered | €9.645,79 | €-338,14 | 112 | 112 | 41,96% | 0,88 | €-3,02 | 6,64% |
| TEST | Combo Adaptive Quality7 Regime V1 | Combo Adaptive | €9.603,78 | €-396,22 | 46 | 46 | 39,13% | 0,69 | €-8,61 | 5,41% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €9.598,72 | €-377,84 | 173 | 173 | 39,88% | 0,90 | €-2,18 | 10,21% |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | Momentum / breakout | €9.580,90 | €-417,79 | 95 | 95 | 37,89% | 0,82 | €-4,40 | 6,41% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | Momentum / breakout V3 Filtered | €9.579,83 | €-420,17 | 11 | 11 | 0,00% | 0,00 | €-38,20 | 4,20% |
| TEST | Btc Ema 1H | Trend following EMA | €9.567,24 | €-432,76 | 18 | 18 | 22,22% | 0,38 | €-24,04 | 4,43% |
| TEST | Scanner Top5 Btc Mfe V1 | Scanner Top 5 + forza BTC | €9.558,01 | €-428,86 | 132 | 132 | 43,18% | 0,84 | €-3,25 | 12,28% |
| TEST | Combo Adaptive Regime V1 | Combo Adaptive | €9.541,28 | €-457,54 | 77 | 77 | 45,45% | 0,76 | €-5,94 | 5,38% |
| TEST | Combo Adaptive Quality7 V1 | Combo Adaptive | €9.514,11 | €-484,42 | 98 | 98 | 38,78% | 0,80 | €-4,94 | 8,88% |
| TEST | 1H Fast V3 No Esports V1 | Momentum / breakout V3 Filtered | €9.498,54 | €-486,54 | 218 | 218 | 42,20% | 0,89 | €-2,23 | 9,85% |
| TEST | Scanner Top5 Btc Guard V1 | Scanner Top 5 + forza BTC | €9.471,54 | €-507,47 | 126 | 126 | 37,30% | 0,84 | €-4,03 | 7,34% |
| TEST | Master Adaptive Gb20 Be V1 | Master Adaptive Consensus | €9.452,15 | €-571,84 | 81 | 81 | 29,63% | 0,76 | €-7,06 | 8,39% |
| TEST | Master Adaptive Gb20 Partial V1 | Master Adaptive Consensus | €9.442,09 | €-581,87 | 76 | 76 | 32,89% | 0,75 | €-7,66 | 7,98% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €9.407,63 | €-628,59 | 81 | 81 | 34,57% | 0,73 | €-7,76 | 7,96% |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | €9.405,57 | €-618,30 | 78 | 78 | 32,05% | 0,75 | €-7,93 | 7,80% |
| TEST | 1H Fast Score 6 75 V1 | Momentum / breakout | €9.400,50 | €-584,13 | 137 | 137 | 40,15% | 0,84 | €-4,26 | 12,47% |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | Momentum / breakout V3 Filtered | €9.371,20 | €-613,36 | 115 | 115 | 43,48% | 0,82 | €-5,33 | 8,24% |
| TEST | Scanner Bottom10 Short | Scanner Bottom10 Short | €9.320,74 | €-677,79 | 70 | 70 | 31,43% | 0,65 | €-9,68 | 9,06% |
| TEST | Scanner Bottom15 Short | Scanner Bottom15 Short | €9.320,74 | €-677,79 | 70 | 70 | 31,43% | 0,65 | €-9,68 | 9,06% |
| TEST | Scanner Bottom20 Short | Scanner Bottom20 Short | €9.320,74 | €-677,79 | 70 | 70 | 31,43% | 0,65 | €-9,68 | 9,06% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €9.300,22 | €-725,14 | 68 | 68 | 30,88% | 0,68 | €-10,66 | 8,18% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €9.281,47 | €-742,09 | 112 | 112 | 44,64% | 0,72 | €-6,63 | 9,02% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €9.264,49 | €-719,48 | 124 | 112 | 41,94% | 0,74 | €-5,80 | 10,39% |
| TEST | Master Adaptive Gb20 Loss Cap V1 | Master Adaptive Consensus | €9.256,43 | €-791,20 | 69 | 69 | 23,19% | 0,65 | €-11,47 | 11,41% |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | Scanner Bottom 5 Short | €9.256,15 | €-742,38 | 61 | 61 | 31,15% | 0,58 | €-12,17 | 9,08% |
| TEST | Scanner Top5 Btc Guard Mfe V1 | Scanner Top 5 + forza BTC | €9.251,26 | €-728,23 | 143 | 143 | 38,46% | 0,79 | €-5,09 | 8,78% |
| TEST | Scanner Bottom5 Short Profit Lock V1 | Scanner Bottom 5 Short | €9.242,07 | €-756,47 | 62 | 62 | 30,65% | 0,56 | €-12,20 | 9,08% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.170,95 | €-827,60 | 89 | 89 | 31,46% | 0,64 | €-9,30 | 10,17% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €9.157,28 | €-835,95 | 79 | 79 | 31,65% | 0,68 | €-10,58 | 8,69% |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | Momentum / breakout | €9.150,56 | €-834,48 | 95 | 95 | 41,05% | 0,72 | €-8,78 | 12,78% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.128,05 | €-868,82 | 135 | 135 | 37,04% | 0,67 | €-6,44 | 12,31% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €9.116,51 | €-849,31 | 121 | 121 | 36,36% | 0,69 | €-7,02 | 14,31% |
| TEST | 1H Fast V3 Cap75 V1 | Momentum / breakout V3 Filtered | €9.091,36 | €-893,78 | 136 | 136 | 36,03% | 0,75 | €-6,57 | 14,24% |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | Scanner Top 5 + forza BTC | €9.083,03 | €-896,81 | 88 | 88 | 35,23% | 0,66 | €-10,19 | 11,79% |
| TEST | 1H Balanced V3 Long Only V1 | Confluenza trend V3 Filtered | €9.078,64 | €-899,20 | 127 | 127 | 39,37% | 0,66 | €-7,08 | 9,95% |
| TEST | Combo Adaptive Mfe Trail | Combo Adaptive | €9.068,08 | €-919,07 | 185 | 185 | 40,54% | 0,74 | €-4,97 | 15,45% |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | Scanner Top 5 + forza BTC | €9.044,42 | €-943,78 | 39 | 39 | 20,51% | 0,30 | €-24,20 | 11,03% |
| TEST | Combo Trend | Combo Trend | €9.037,34 | €-938,38 | 171 | 171 | 37,43% | 0,77 | €-5,49 | 11,60% |
| TEST | Combo Adaptive Runner25 V1 | Combo Adaptive | €8.936,19 | €-1.035,89 | 94 | 94 | 30,85% | 0,53 | €-11,02 | 12,94% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €8.823,89 | €-1.174,82 | 50 | 50 | 34,00% | 0,44 | €-23,50 | 13,49% |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | Scanner Top 5 + forza BTC | €8.819,14 | €-1.184,06 | 100 | 100 | 34,00% | 0,60 | €-11,84 | 12,29% |
| TEST | Combo Adaptive Tp3 V1 | Combo Adaptive | €8.769,24 | €-1.203,36 | 75 | 75 | 29,33% | 0,38 | €-16,04 | 12,94% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €8.740,20 | €-1.259,48 | 81 | 81 | 38,27% | 0,55 | €-15,55 | 14,61% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €8.705,20 | €-1.294,33 | 71 | 71 | 25,35% | 0,56 | €-18,23 | 13,24% |
| TEST | Scanner Top5 Btc Btc Le3 V1 | Scanner Top 5 + forza BTC | €8.701,51 | €-1.297,48 | 83 | 83 | 30,12% | 0,48 | €-15,63 | 14,88% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €8.409,69 | €-1.554,49 | 105 | 105 | 27,62% | 0,47 | €-14,80 | 17,74% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | SPCX | LONG | Confluenza trend | 240m | 3,0x | 136,56189 | 136,56189 | 128,79610 | 91,72407 | 152,09346 | €285,50 | €856,50 | €48,71 | €0,00 |
| Principale 4H | VELVET | LONG | Confluenza trend | 240m | 3,0x | 0,55987 | 0,55987 | 0,49269 | 0,37605 | 0,69424 | €131,08 | €393,24 | €47,19 | €0,00 |
| Principale 4H | EDEN | LONG | Confluenza trend | 240m | 3,0x | 0,06195 | 0,06195 | 0,05451 | 0,04161 | 0,07681 | €130,34 | €391,02 | €46,92 | €0,00 |
| Principale 4H | TRUMP | LONG | Confluenza trend | 240m | 3,0x | 2,46049 | 2,46049 | 2,16523 | 1,65263 | 3,05101 | €134,98 | €404,95 | €48,59 | €0,00 |
| Principale 4H | XRP | LONG | Confluenza trend | 240m | 3,0x | 1,46057 | 1,38478 | 1,30460 | 0,98102 | 1,77252 | €8,58 | €25,73 | €2,75 | €-1,34 |
| Principale 4H | UNI | LONG | Confluenza trend | 240m | 3,0x | 5,15403 | 5,15403 | 4,78412 | 3,46179 | 5,89386 | €9,32 | €27,96 | €2,01 | €0,00 |
| Bilanciata 1H V1 | HYPE | LONG | Confluenza trend | 60m | 3,0x | 84,10682 | 84,11000 | 82,40110 | 56,49175 | 87,51826 | €752,01 | €2.256,04 | €45,75 | €0,09 |
| Bilanciata 1H V1 | DOGE | SHORT | Confluenza trend | 60m | 3,0x | 0,08307 | 0,08335 | 0,08429 | 0,11034 | 0,08063 | €1.038,40 | €3.115,19 | €45,74 | €-10,50 |
| Bilanciata 1H V1 | SKR | LONG | Confluenza trend | 60m | 3,0x | 0,02975 | 0,02863 | 0,02618 | 0,01998 | 0,03689 | €127,02 | €381,05 | €45,73 | €-14,33 |
| Bilanciata 1H V1 | ZEC | LONG | Confluenza trend | 60m | 3,0x | 858,17160 | 855,38000 | 832,95428 | 576,40526 | 908,60625 | €518,10 | €1.554,31 | €45,67 | €-5,06 |
| 1H Balanced Long No Rhv V1 | SKHYNIX | LONG | Confluenza trend | 60m | 3,0x | 1214,11277 | 1214,11277 | 1170,18211 | 815,47908 | 1301,97411 | €413,43 | €1.240,28 | €44,88 | €0,00 |
| 1H Balanced Long No Rhv V1 | BOME | LONG | Confluenza trend | 60m | 3,0x | 0,00129 | 0,00129 | 0,00114 | 0,00087 | 0,00160 | €134,98 | €404,95 | €48,59 | €0,00 |
| 1H Balanced Long No Rhv V1 | TAO | LONG | Confluenza trend | 60m | 3,0x | 247,38947 | 247,38947 | 237,94346 | 166,16326 | 266,28148 | €428,20 | €1.284,61 | €49,05 | €0,00 |
| 1H Balanced Long No Rhv V1 | HEMI | LONG | Confluenza trend | 60m | 3,0x | 0,01177 | 0,01177 | 0,01036 | 0,00790 | 0,01459 | €131,93 | €395,78 | €47,49 | €0,00 |
| 1H Balanced Long No Rhv V1 | UNI | LONG | Confluenza trend | 60m | 3,0x | 5,12502 | 5,12502 | 4,91893 | 3,44231 | 5,53722 | €24,33 | €72,99 | €2,94 | €0,00 |
| Bilanciata 1H V2 | SKHYNIX | LONG | Confluenza trend V2 | 60m | 3,0x | 1214,11277 | 1214,11277 | 1170,18211 | 815,47908 | 1301,97411 | €422,38 | €1.267,15 | €45,85 | €0,00 |
| Bilanciata 1H V2 | SKR | LONG | Confluenza trend V2 | 60m | 3,0x | 0,02872 | 0,02863 | 0,02527 | 0,01929 | 0,03561 | €128,88 | €386,65 | €46,40 | €-1,17 |
| Bilanciata 1H V2 | XMR | LONG | Confluenza trend V2 | 60m | 3,0x | 520,62410 | 514,88000 | 498,16818 | 349,68586 | 565,53596 | €358,56 | €1.075,68 | €46,40 | €-11,87 |
| Bilanciata 1H V2 | HYPE | LONG | Confluenza trend V2 | 60m | 3,0x | 84,10682 | 84,11000 | 82,40110 | 56,49175 | 87,51826 | €764,01 | €2.292,03 | €46,48 | €0,09 |
| Bilanciata 1H V3 Filtered | SKHYNIX | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1220,85412 | 1220,85412 | 1177,63561 | 820,00702 | 1307,29117 | €460,42 | €1.381,27 | €48,90 | €0,00 |
| Bilanciata 1H V3 Filtered | ADA | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,20138 | 0,20138 | 0,20719 | 0,26750 | 0,18976 | €559,88 | €1.679,63 | €48,45 | €-0,00 |
| Bilanciata 1H V3 Filtered | ENA | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,14884 | 0,14884 | 0,15578 | 0,19771 | 0,13496 | €346,84 | €1.040,52 | €48,51 | €-0,00 |
| Bilanciata 1H V3 Filtered | DOGE | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,08276 | 0,08335 | 0,08414 | 0,10993 | 0,08000 | €925,44 | €2.776,33 | €46,37 | €-19,78 |
| 1H Fast Score 6 75 V1 | SKR | LONG | Momentum / breakout | 60m | 3,0x | 0,02975 | 0,02863 | 0,02618 | 0,01998 | 0,03510 | €130,78 | €392,33 | €47,08 | €-14,76 |
| 1H Fast Score 6 75 V1 | BTR | LONG | Momentum / breakout | 60m | 3,0x | 0,17599 | 0,17595 | 0,15842 | 0,11820 | 0,20234 | €156,96 | €470,88 | €47,00 | €-0,09 |
| 1H Fast Score 6 75 No Trend Up V1 | SKR | LONG | Momentum / breakout | 60m | 3,0x | 0,02975 | 0,02863 | 0,02618 | 0,01998 | 0,03510 | €127,30 | €381,90 | €45,83 | €-14,36 |
| 1H Fast Score 6 75 No Trend Up V1 | BTR | LONG | Momentum / breakout | 60m | 3,0x | 0,17599 | 0,17595 | 0,15842 | 0,11820 | 0,20234 | €152,79 | €458,36 | €45,75 | €-0,09 |
| 1H Fast Score 6 75 Range Only V1 | ADA | SHORT | Momentum / breakout | 60m | 3,0x | 0,20260 | 0,20260 | 0,20707 | 0,26912 | 0,19589 | €765,21 | €2.295,64 | €50,71 | €-0,00 |
| 1H Fast Score 6 75 Range Only V1 | HEMI | LONG | Momentum / breakout | 60m | 3,0x | 0,01177 | 0,01177 | 0,01065 | 0,00790 | 0,01345 | €178,53 | €535,59 | €51,05 | €0,00 |
| 1H Fast Score 6 75 Range Only V1 | SKR | LONG | Momentum / breakout | 60m | 3,0x | 0,02969 | 0,02863 | 0,02612 | 0,01994 | 0,03503 | €141,91 | €425,72 | €51,09 | €-15,13 |
| 1H Fast Score 6 75 Cost Aware V1 | BTW | LONG | Momentum / breakout | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €8,91 | €26,72 | €3,13 | €0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00086 | 0,00146 | €215,92 | €647,76 | €57,03 | €0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | NEAR | LONG | Momentum / breakout | 60m | 3,0x | 2,08142 | 2,08142 | 2,02315 | 1,39802 | 2,16882 | €42,86 | €128,59 | €3,60 | €0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €157,13 | €471,39 | €56,57 | €-0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | ENA | SHORT | Momentum / breakout | 60m | 3,0x | 0,14884 | 0,14884 | 0,15424 | 0,19771 | 0,14074 | €517,69 | €1.553,08 | €56,32 | €-0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | SKR | LONG | Momentum / breakout | 60m | 3,0x | 0,02969 | 0,02863 | 0,02612 | 0,01994 | 0,03503 | €124,11 | €372,34 | €44,68 | €-13,23 |
| 1H Fast Nohigh Cap75 V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €139,29 | €417,86 | €50,14 | €-0,00 |
| 1H Fast Nohigh Cap75 V1 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €141,57 | €424,71 | €50,14 | €-0,00 |
| 1H Fast Nohigh Cap75 V1 | SKR | LONG | Momentum / breakout | 60m | 3,0x | 0,02975 | 0,02863 | 0,02618 | 0,01998 | 0,03510 | €138,23 | €414,69 | €49,76 | €-15,60 |
| 1H Fast Nohigh Cap75 V1 | BTR | LONG | Momentum / breakout | 60m | 3,0x | 0,17599 | 0,17595 | 0,15842 | 0,11820 | 0,20234 | €167,99 | €503,98 | €50,31 | €-0,10 |
| 1H Fast Long Btc 1 3 Cap75 V1 | PROM | LONG | Momentum / breakout | 60m | 3,0x | 6,93686 | 6,93686 | 6,39299 | 4,65926 | 7,75266 | €205,67 | €617,01 | €48,38 | €0,00 |
| 1H Fast Long Btc 1 3 Cap75 V1 | UNI | LONG | Momentum / breakout | 60m | 3,0x | 5,12502 | 5,12502 | 4,96473 | 3,44231 | 5,36547 | €522,78 | €1.568,34 | €49,05 | €0,00 |
| 1H Fast No Pepe V1 | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €172,22 | €516,67 | €49,86 | €0,00 |
| 1H Fast No Pepe V1 | TAO | LONG | Momentum / breakout | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €47,93 | €143,78 | €4,27 | €0,00 |
| 1H Fast No Pepe V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €136,27 | €408,80 | €49,06 | €-0,00 |
| 1H Fast No Pepe V1 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €9,48 | €28,43 | €3,41 | €-0,00 |
| 1H Fast No Pepe V1 | ADA | SHORT | Momentum / breakout | 60m | 3,0x | 0,20138 | 0,20138 | 0,20590 | 0,26750 | 0,19460 | €739,08 | €2.217,23 | €49,74 | €-0,00 |
| 1H Fast No Pepe V1 | ENA | SHORT | Momentum / breakout | 60m | 3,0x | 0,14884 | 0,14884 | 0,15424 | 0,19771 | 0,14074 | €9,98 | €29,94 | €1,09 | €-0,00 |
| 1H Fast No Pepe V1 | BTR | LONG | Momentum / breakout | 60m | 3,0x | 0,17599 | 0,17595 | 0,15842 | 0,11820 | 0,20234 | €176,75 | €530,25 | €52,93 | €-0,11 |
| 1H Fast Tp2 V1 | BTW | LONG | Momentum / breakout | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,56752 | €142,85 | €428,56 | €50,25 | €0,00 |
| 1H Fast Tp2 V1 | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00132 | 0,00132 | 0,00119 | 0,00088 | 0,00158 | €18,87 | €56,62 | €5,59 | €0,00 |
| 1H Fast Tp2 V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,17246 | 0,17246 | 0,17246 | 0,22908 | 0,13107 | €139,71 | €419,14 | €0,00 | €-0,00 |
| 1H Fast Tp2 V1 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03379 | €141,13 | €423,40 | €50,81 | €-0,00 |
| 1H Fast Tp2 V1 | SKR | LONG | Momentum / breakout | 60m | 3,0x | 0,02975 | 0,02863 | 0,02618 | 0,01998 | 0,03689 | €123,47 | €370,41 | €44,45 | €-13,93 |
| Rapida 1H V2 | ADA | SHORT | Momentum / breakout V2 | 60m | 3,0x | 0,20283 | 0,20283 | 0,20750 | 0,26943 | 0,19582 | €749,31 | €2.247,94 | €51,80 | €-0,00 |
| Rapida 1H V3 Filtered | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €172,00 | €515,99 | €49,79 | €0,00 |
| Rapida 1H V3 Filtered | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €589,98 | €1.769,95 | €52,56 | €0,00 |
| Rapida 1H V3 Filtered | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €140,02 | €420,06 | €50,41 | €-0,00 |
| Rapida 1H V3 Filtered | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €16,99 | €50,96 | €6,11 | €-0,00 |
| Rapida 1H V3 Filtered | SKR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,02975 | 0,02863 | 0,02618 | 0,01998 | 0,03510 | €130,20 | €390,61 | €46,87 | €-14,69 |
| 1H Fast V3 Cap75 V1 | SKR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,02975 | 0,02863 | 0,02618 | 0,01998 | 0,03510 | €126,48 | €379,43 | €45,53 | €-14,27 |
| 1H Fast V3 Cap75 V1 | BTR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,17599 | 0,17595 | 0,15842 | 0,11820 | 0,20234 | €151,80 | €455,40 | €45,46 | €-0,09 |
| 1H Fast V3 Nohigh V1 | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €131,05 | €393,14 | €47,18 | €-0,00 |
| 1H Fast V3 Nohigh V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €133,20 | €399,59 | €47,18 | €-0,00 |
| 1H Fast V3 Nohigh V1 | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,20138 | 0,20138 | 0,20590 | 0,26750 | 0,19460 | €719,57 | €2.158,72 | €48,43 | €-0,00 |
| 1H Fast V3 Nohigh V1 | SKR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,02975 | 0,02863 | 0,02618 | 0,01998 | 0,03510 | €11,94 | €35,83 | €4,30 | €-1,35 |
| 1H Fast V3 Nohigh V1 | BTR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,17599 | 0,17595 | 0,15842 | 0,11820 | 0,20234 | €164,91 | €494,72 | €49,38 | €-0,10 |
| 1H Fast V3 Long Only V1 | BTW | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €126,57 | €379,72 | €44,52 | €0,00 |
| 1H Fast V3 Long Only V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00147 | €9,56 | €28,69 | €2,66 | €0,00 |
| 1H Fast V3 Long Only V1 | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €554,42 | €1.663,26 | €49,39 | €0,00 |
| 1H Fast V3 Long Only V1 | HEMI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01177 | 0,01177 | 0,01065 | 0,00790 | 0,01345 | €170,60 | €511,79 | €48,79 | €0,00 |
| 1H Fast V3 Long Only V1 | UNI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 5,12502 | 5,12502 | 4,96473 | 3,44231 | 5,36547 | €518,95 | €1.556,84 | €48,69 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 V1 | HEMI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01177 | 0,01177 | 0,01065 | 0,00790 | 0,01345 | €166,97 | €500,92 | €47,75 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 V1 | PROM | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 6,92735 | 6,92735 | 6,35093 | 4,65287 | 7,79198 | €195,87 | €587,60 | €48,89 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 V1 | SKR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,02975 | 0,02863 | 0,02618 | 0,01998 | 0,03510 | €131,13 | €393,38 | €47,21 | €-14,80 |
| 1H Fast V3 Long Nohigh Cap75 V1 | BTR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,17599 | 0,17595 | 0,15842 | 0,11820 | 0,20234 | €161,06 | €483,17 | €48,23 | €-0,10 |
| 1H Fast V3 No Esports V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €169,36 | €508,09 | €49,03 | €0,00 |
| 1H Fast V3 No Esports V1 | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €27,04 | €81,13 | €2,41 | €0,00 |
| 1H Fast V3 No Esports V1 | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €133,96 | €401,88 | €48,23 | €-0,00 |
| 1H Fast V3 No Esports V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €129,73 | €389,20 | €46,70 | €-0,00 |
| 1H Fast V3 No Esports V1 | SKR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,02975 | 0,02863 | 0,02618 | 0,01998 | 0,03510 | €121,89 | €365,68 | €43,88 | €-13,75 |
| 1H Fast V3 No Esports Long Only V1 | BTW | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €132,94 | €398,81 | €46,76 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00147 | €10,06 | €30,18 | €2,80 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | HEMI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01177 | 0,01177 | 0,01065 | 0,00790 | 0,01345 | €175,30 | €525,91 | €50,13 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | PROM | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 6,92735 | 6,92735 | 6,35093 | 4,65287 | 7,79198 | €9,71 | €29,12 | €2,42 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | UNI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 5,12502 | 5,12502 | 4,96473 | 3,44231 | 5,36547 | €529,67 | €1.589,01 | €49,70 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | BTR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,17599 | 0,17595 | 0,15842 | 0,11820 | 0,20234 | €158,21 | €474,62 | €47,38 | €-0,09 |
| 1H Fast V3 No Esports Mfe Lock V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €173,11 | €519,32 | €50,11 | €0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €593,79 | €1.781,38 | €52,90 | €0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €140,93 | €422,78 | €50,73 | €-0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €17,09 | €51,28 | €6,15 | €-0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | SKR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,02975 | 0,02863 | 0,02618 | 0,01998 | 0,03510 | €131,05 | €393,14 | €47,18 | €-14,79 |
| 1H Fast V3 No Esports Stress Guard V1 | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,20283 | 0,20283 | 0,20750 | 0,26943 | 0,19582 | €739,04 | €2.217,11 | €51,09 | €-0,00 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | HEMI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01177 | 0,01177 | 0,01065 | 0,00790 | 0,01345 | €163,25 | €489,75 | €46,69 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | PROM | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 6,92735 | 6,92735 | 6,35093 | 4,65287 | 7,79198 | €191,37 | €574,11 | €47,77 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | SKR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,02975 | 0,02863 | 0,02618 | 0,01998 | 0,03510 | €125,82 | €377,46 | €45,30 | €-14,20 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | BTR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,17599 | 0,17595 | 0,15842 | 0,11820 | 0,20234 | €156,47 | €469,42 | €46,86 | €-0,09 |
| Ampia 4H | SPCX | LONG | Confluenza trend | 240m | 2,0x | 136,56189 | 136,56189 | 126,46637 | 68,96375 | 164,82935 | €323,86 | €647,73 | €47,88 | €0,00 |
| Ampia 4H | VELVET | LONG | Confluenza trend | 240m | 2,0x | 0,55987 | 0,55987 | 0,49269 | 0,28274 | 0,74799 | €201,63 | €403,26 | €48,39 | €0,00 |
| Ampia 4H | LINK | LONG | Confluenza trend | 240m | 2,0x | 11,96839 | 11,96839 | 11,08055 | 6,04404 | 14,45436 | €14,07 | €28,15 | €2,09 | €0,00 |
| Ampia 4H | ETH | LONG | Confluenza trend | 240m | 2,0x | 2430,03591 | 2473,50000 | 2267,54364 | 1227,16813 | 2885,01426 | €18,82 | €37,65 | €2,52 | €0,67 |
| Ampia 4H | HYPE | LONG | Confluenza trend | 240m | 2,0x | 79,31286 | 84,11000 | 70,73982 | 40,05299 | 103,31737 | €13,82 | €27,64 | €2,99 | €1,67 |
| Ampia 4H | TRUMP | LONG | Confluenza trend | 240m | 2,0x | 2,37347 | 2,37347 | 2,08866 | 1,19860 | 3,17096 | €210,83 | €421,66 | €50,60 | €0,00 |
| Ampia 4H | DOGE | SHORT | Confluenza trend | 240m | 2,0x | 0,08583 | 0,08335 | 0,09382 | 0,12832 | 0,06346 | €274,53 | €549,07 | €51,10 | €15,88 |
| Ampia 4H | SOL | LONG | Confluenza trend | 240m | 2,0x | 103,77875 | 103,94100 | 96,79200 | 52,40827 | 123,34165 | €13,62 | €27,23 | €1,83 | €0,04 |
| Forza relativa 1H V1 | HYPE | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 84,10682 | 84,11000 | 82,40110 | 42,47394 | 87,85940 | €1.041,09 | €2.082,18 | €42,23 | €0,08 |
| Forza relativa 1H V1 | SKR | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,02975 | 0,02863 | 0,02618 | 0,01502 | 0,03760 | €175,91 | €351,83 | €42,22 | €-13,23 |
| Forza relativa 1H V1 | ZEC | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 858,17160 | 855,38000 | 832,95428 | 433,37666 | 913,64972 | €718,36 | €1.436,72 | €42,22 | €-4,67 |
| Forza relativa 1H V1 | XMR | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 522,67451 | 514,88000 | 500,84717 | 263,95063 | 570,69467 | €505,06 | €1.010,12 | €42,18 | €-15,06 |
| Forza relativa 1H V2 | BEAT | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,25984 | 0,25984 | 0,25657 | 0,38847 | 0,19125 | €200,38 | €400,75 | €0,00 | €-0,00 |
| Forza relativa 1H V2 | TUT | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,04452 | 0,04452 | 0,04986 | 0,06656 | 0,03277 | €204,64 | €409,28 | €49,11 | €-0,00 |
| Forza relativa 1H V2 | ADA | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,20283 | 0,20283 | 0,20884 | 0,30323 | 0,18961 | €17,52 | €35,04 | €1,04 | €-0,00 |
| Forza relativa 1H V2 | HEMI | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €200,86 | €401,72 | €48,21 | €0,00 |
| Forza relativa 1H V2 | ENA | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,14884 | 0,14884 | 0,15578 | 0,22252 | 0,13357 | €527,76 | €1.055,51 | €49,21 | €-0,00 |
| Forza relativa 1H V2 | XMR | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 520,62410 | 514,88000 | 498,16818 | 262,91517 | 570,02714 | €13,24 | €26,48 | €1,14 | €-0,29 |
| Benchmark Donchian breakout 1H | SKHYNIX | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1174,33482 | 1174,33482 | 1128,44989 | 593,03908 | 1289,04713 | €641,25 | €1.282,50 | €50,11 | €0,00 |
| Benchmark Donchian breakout 1H | VELVET | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,14787 | 0,14787 | 0,16561 | 0,22107 | 0,10351 | €237,23 | €474,47 | €56,94 | €-0,00 |
| Benchmark Donchian breakout 1H | ADA | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,20283 | 0,20283 | 0,20951 | 0,30323 | 0,18614 | €72,87 | €145,74 | €4,80 | €-0,00 |
| Benchmark Donchian breakout 1H | HYPE | LONG | Donchian breakout 20 barre | 60m | 2,0x | 83,90778 | 84,11000 | 81,81383 | 42,37343 | 89,14264 | €38,03 | €76,07 | €1,90 | €0,18 |
| Benchmark Donchian breakout 1H | SKR | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,03037 | 0,02863 | 0,02673 | 0,01534 | 0,03948 | €235,56 | €471,12 | €56,53 | €-27,02 |
| Benchmark Donchian breakout 1H | BTR | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,17599 | 0,17595 | 0,15487 | 0,08887 | 0,22878 | €230,47 | €460,94 | €55,31 | €-0,09 |
| Donchian 1H Gb20 120R V1 | SKHYNIX | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1174,33482 | 1174,33482 | 1128,44989 | 593,03908 | 1289,04713 | €626,15 | €1.252,30 | €48,93 | €0,00 |
| Donchian 1H Gb20 120R V1 | VELVET | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,14787 | 0,14787 | 0,16561 | 0,22107 | 0,10351 | €231,65 | €463,30 | €55,60 | €-0,00 |
| Donchian 1H Gb20 120R V1 | ADA | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,20283 | 0,20283 | 0,20951 | 0,30323 | 0,18614 | €71,16 | €142,31 | €4,68 | €-0,00 |
| Donchian 1H Gb20 120R V1 | HYPE | LONG | Donchian breakout 20 barre | 60m | 2,0x | 83,90778 | 84,11000 | 81,81383 | 42,37343 | 89,14264 | €37,14 | €74,28 | €1,85 | €0,18 |
| Donchian 1H Gb20 120R V1 | SKR | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,03037 | 0,02863 | 0,02673 | 0,01534 | 0,03948 | €230,01 | €460,03 | €55,20 | €-26,39 |
| Donchian 1H Gb20 120R V1 | BTR | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,17599 | 0,17595 | 0,15487 | 0,08887 | 0,22878 | €225,04 | €450,09 | €54,01 | €-0,09 |
| Benchmark Bollinger mean reversion 1H | BTR | SHORT | Bollinger mean reversion | 60m | 2,0x | 0,17591 | 0,17595 | 0,19473 | 0,26299 | 0,14769 | €204,31 | €408,62 | €43,70 | €-0,08 |
| Benchmark trend following EMA 1H | BEAT | SHORT | Trend following EMA | 60m | 2,0x | 0,28257 | 0,28257 | 0,25706 | 0,42244 | 0,20797 | €186,11 | €372,23 | €0,00 | €-0,00 |
| Benchmark trend following EMA 1H | TUT | SHORT | Trend following EMA | 60m | 2,0x | 0,04446 | 0,04446 | 0,04980 | 0,06647 | 0,03272 | €194,70 | €389,39 | €46,73 | €-0,00 |
| Benchmark trend following EMA 1H | VELVET | SHORT | Trend following EMA | 60m | 2,0x | 0,14786 | 0,14786 | 0,16560 | 0,22105 | 0,10883 | €187,91 | €375,83 | €45,10 | €-0,00 |
| Benchmark trend following EMA 1H | ENA | SHORT | Trend following EMA | 60m | 2,0x | 0,15004 | 0,15004 | 0,15652 | 0,22431 | 0,13579 | €490,79 | €981,58 | €42,39 | €-0,00 |
| Benchmark trend following EMA 1H | DOGE | SHORT | Trend following EMA | 60m | 2,0x | 0,08264 | 0,08335 | 0,08416 | 0,12355 | 0,07930 | €103,98 | €207,95 | €3,82 | €-1,79 |
| Scanner Top 5 Long 1H | BOME | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00160 | €218,24 | €436,47 | €52,38 | €0,00 |
| Scanner Top 5 Long 1H | TRUMP | LONG | Scanner Top 5 Long | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,08367 | €238,89 | €477,78 | €55,13 | €0,00 |
| Scanner Top 5 Long 1H | SKHYNIX | LONG | Scanner Top 5 Long | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1331,36020 | €17,74 | €35,49 | €0,91 | €0,00 |
| Scanner Top 5 Long 1H | HEMI | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €228,24 | €456,48 | €54,78 | €0,00 |
| Scanner Top 5 Long 1H | XMR | LONG | Scanner Top 5 Long | 60m | 2,0x | 519,56389 | 514,88000 | 495,28598 | 262,37977 | 568,11972 | €14,50 | €28,99 | €1,35 | €-0,26 |
| Scanner Top 5 Long 1H | HYPE | LONG | Scanner Top 5 Long | 60m | 2,0x | 84,52190 | 84,11000 | 82,69867 | 42,68356 | 88,16835 | €1.244,04 | €2.488,07 | €53,67 | €-12,13 |
| Scanner Bottom 5 Short 1H | SOXL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €378,86 | €757,72 | €48,07 | €-0,00 |
| Scanner Bottom 5 Short 1H | SNDK | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €492,80 | €985,60 | €47,71 | €-0,00 |
| Scanner Bottom 5 Short 1H | VELVET | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €191,07 | €382,14 | €0,00 | €-0,00 |
| Scanner Bottom 5 Short 1H | TUT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €178,38 | €356,76 | €42,81 | €-0,00 |
| Scanner Top10 Long | TAO | LONG | Scanner Top10 Long | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €678,43 | €1.356,86 | €51,81 | €0,00 |
| Scanner Top10 Long | SKHYNIX | LONG | Scanner Top10 Long | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €972,86 | €1.945,72 | €48,38 | €0,00 |
| Scanner Top10 Long | HEMI | LONG | Scanner Top10 Long | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €207,88 | €415,77 | €49,89 | €0,00 |
| Scanner Top10 Long | UNI | LONG | Scanner Top10 Long | 60m | 2,0x | 5,12502 | 5,12502 | 4,91893 | 2,58814 | 5,53722 | €19,51 | €39,02 | €1,57 | €0,00 |
| Scanner Top10 Long | XMR | LONG | Scanner Top10 Long | 60m | 2,0x | 519,56389 | 514,88000 | 495,28598 | 262,37977 | 568,11972 | €12,79 | €25,57 | €1,20 | €-0,23 |
| Scanner Top10 Long | HYPE | LONG | Scanner Top10 Long | 60m | 2,0x | 84,52190 | 84,11000 | 82,69867 | 42,68356 | 88,16835 | €1.155,59 | €2.311,18 | €49,85 | €-11,26 |
| Scanner Bottom10 Short | SOXL | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom10 Short | SNDK | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Bottom10 Short | VELVET | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €194,19 | €388,38 | €0,00 | €-0,00 |
| Scanner Bottom10 Short | TUT | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €181,31 | €362,61 | €43,51 | €-0,00 |
| Scanner Top15 Long | NEAR | LONG | Scanner Top15 Long | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €16,79 | €33,59 | €1,21 | €0,00 |
| Scanner Top15 Long | TAO | LONG | Scanner Top15 Long | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €88,53 | €177,07 | €6,76 | €0,00 |
| Scanner Top15 Long | TRUMP | LONG | Scanner Top15 Long | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,08367 | €215,87 | €431,75 | €49,81 | €0,00 |
| Scanner Top15 Long | SKHYNIX | LONG | Scanner Top15 Long | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €787,36 | €1.574,72 | €39,16 | €0,00 |
| Scanner Top15 Long | UNI | LONG | Scanner Top15 Long | 60m | 2,0x | 5,12502 | 5,12502 | 4,91893 | 2,58814 | 5,53722 | €610,91 | €1.221,82 | €49,13 | €0,00 |
| Scanner Top15 Long | XMR | LONG | Scanner Top15 Long | 60m | 2,0x | 522,24443 | 514,88000 | 497,48743 | 263,73344 | 571,75843 | €19,54 | €39,08 | €1,85 | €-0,55 |
| Scanner Top15 Long | HYPE | LONG | Scanner Top15 Long | 60m | 2,0x | 84,52190 | 84,11000 | 82,69867 | 42,68356 | 88,16835 | €1.133,90 | €2.267,79 | €48,92 | €-11,05 |
| Scanner Bottom15 Short | SOXL | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom15 Short | SNDK | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Bottom15 Short | VELVET | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €194,19 | €388,38 | €0,00 | €-0,00 |
| Scanner Bottom15 Short | TUT | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €181,31 | €362,61 | €43,51 | €-0,00 |
| Scanner Top20 Long | NEAR | LONG | Scanner Top20 Long | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €16,79 | €33,59 | €1,21 | €0,00 |
| Scanner Top20 Long | TAO | LONG | Scanner Top20 Long | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €88,53 | €177,07 | €6,76 | €0,00 |
| Scanner Top20 Long | TRUMP | LONG | Scanner Top20 Long | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,08367 | €215,87 | €431,75 | €49,81 | €0,00 |
| Scanner Top20 Long | SKHYNIX | LONG | Scanner Top20 Long | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €787,36 | €1.574,72 | €39,16 | €0,00 |
| Scanner Top20 Long | UNI | LONG | Scanner Top20 Long | 60m | 2,0x | 5,12502 | 5,12502 | 4,91893 | 2,58814 | 5,53722 | €610,91 | €1.221,82 | €49,13 | €0,00 |
| Scanner Top20 Long | XMR | LONG | Scanner Top20 Long | 60m | 2,0x | 522,24443 | 514,88000 | 497,48743 | 263,73344 | 571,75843 | €19,54 | €39,08 | €1,85 | €-0,55 |
| Scanner Top20 Long | HYPE | LONG | Scanner Top20 Long | 60m | 2,0x | 84,52190 | 84,11000 | 82,69867 | 42,68356 | 88,16835 | €1.133,90 | €2.267,79 | €48,92 | €-11,05 |
| Scanner Bottom20 Short | SOXL | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom20 Short | SNDK | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Bottom20 Short | VELVET | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €194,19 | €388,38 | €0,00 | €-0,00 |
| Scanner Bottom20 Short | TUT | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €181,31 | €362,61 | €43,51 | €-0,00 |
| Scanner Top 5 + forza BTC 1H | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €203,45 | €406,91 | €48,83 | €0,00 |
| Scanner Top 5 + forza BTC 1H | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,14149 | €223,03 | €446,06 | €51,47 | €0,00 |
| Scanner Top 5 + forza BTC 1H | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €18,23 | €36,45 | €0,93 | €0,00 |
| Scanner Top 5 + forza BTC 1H | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €213,35 | €426,70 | €51,20 | €0,00 |
| Scanner Top 5 + forza BTC 1H | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 519,56389 | 514,88000 | 495,28598 | 262,37977 | 572,97530 | €16,38 | €32,76 | €1,53 | €-0,30 |
| Scanner Top 5 + forza BTC 1H | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 84,52190 | 84,11000 | 82,69867 | 42,68356 | 88,53300 | €1.164,07 | €2.328,14 | €50,22 | €-11,35 |
| Scanner Top5 Btc Mfe V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €190,73 | €381,46 | €45,77 | €0,00 |
| Scanner Top5 Btc Mfe V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,14149 | €209,08 | €418,16 | €48,25 | €0,00 |
| Scanner Top5 Btc Mfe V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €17,09 | €34,17 | €0,88 | €0,00 |
| Scanner Top5 Btc Mfe V1 | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €200,01 | €400,01 | €48,00 | €0,00 |
| Scanner Top5 Btc Mfe V1 | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 519,56389 | 514,88000 | 495,28598 | 262,37977 | 572,97530 | €15,36 | €30,72 | €1,44 | €-0,28 |
| Scanner Top5 Btc Mfe V1 | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 84,52190 | 84,11000 | 82,69867 | 42,68356 | 88,53300 | €1.091,26 | €2.182,52 | €47,08 | €-10,64 |
| Scanner Top5 Btc Guard V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €197,27 | €394,55 | €47,35 | €0,00 |
| Scanner Top5 Btc Guard V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,55551 | 2,55551 | 2,29388 | 1,29053 | 3,13109 | €13,03 | €26,06 | €2,67 | €0,00 |
| Scanner Top5 Btc Guard V1 | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €195,03 | €390,06 | €46,81 | €0,00 |
| Scanner Top5 Btc Guard V1 | ZORA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00942 | 0,00942 | 0,00829 | 0,00476 | 0,01191 | €192,06 | €384,12 | €46,09 | €0,00 |
| Scanner Top5 Btc Guard V1 | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 525,28504 | 514,88000 | 500,95080 | 265,26894 | 578,82035 | €506,36 | €1.012,72 | €46,92 | €-20,06 |
| Scanner Top5 Btc Btc Le3 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €847,75 | €1.695,49 | €43,45 | €0,00 |
| Scanner Top5 Btc Btc 2 3 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €891,28 | €1.782,56 | €45,68 | €0,00 |
| Scanner Top5 Btc Btc 2 3 V1 | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 522,24443 | 514,88000 | 497,48743 | 263,73344 | 576,70983 | €478,87 | €957,73 | €45,40 | €-13,51 |
| Scanner Top5 Btc Btc 2 3 V1 | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 83,90778 | 84,11000 | 82,02323 | 42,37343 | 88,05379 | €1.009,97 | €2.019,94 | €45,37 | €4,87 |
| Scanner Top5 Btc Btc 2 3 V1 | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 854,85094 | 855,38000 | 827,09609 | 431,69972 | 915,91159 | €693,18 | €1.386,37 | €45,01 | €0,86 |
| Scanner Top5 Btc Guard Mfe V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €192,69 | €385,37 | €46,24 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,55551 | 2,55551 | 2,29388 | 1,29053 | 3,13109 | €12,72 | €25,45 | €2,61 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €190,49 | €380,99 | €45,72 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | ZORA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00942 | 0,00942 | 0,00829 | 0,00476 | 0,01191 | €187,59 | €375,19 | €45,02 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 525,28504 | 514,88000 | 500,95080 | 265,26894 | 578,82035 | €494,59 | €989,17 | €45,82 | €-19,59 |
| Scanner Top5 Btc Guard Btc Le3 V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,55551 | 2,55551 | 2,29388 | 1,29053 | 3,13109 | €12,70 | €25,40 | €2,60 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €191,20 | €382,39 | €45,89 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | PROM | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 7,01991 | 7,01991 | 6,30832 | 3,54505 | 8,58541 | €213,89 | €427,78 | €43,36 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | ZORA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00942 | 0,00942 | 0,00829 | 0,00476 | 0,01191 | €188,34 | €376,68 | €45,20 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 525,28504 | 514,88000 | 500,95080 | 265,26894 | 578,82035 | €485,59 | €971,18 | €44,99 | €-19,24 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | ZORA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00942 | 0,00942 | 0,00829 | 0,00476 | 0,01191 | €185,37 | €370,74 | €44,49 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 83,93178 | 84,11000 | 82,11476 | 42,38555 | 87,92924 | €1.008,26 | €2.016,51 | €43,66 | €4,28 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 854,85094 | 855,38000 | 827,09609 | 431,69972 | 915,91159 | €682,78 | €1.365,56 | €44,34 | €0,85 |
| Scanner Top5 Btc Runner25 V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00176 | €210,95 | €421,90 | €50,63 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1363,81560 | €965,52 | €1.931,04 | €49,49 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01601 | €209,51 | €419,03 | €50,28 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | UNI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 5,12502 | 5,12502 | 4,91893 | 2,58814 | 5,74332 | €624,18 | €1.248,36 | €50,20 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00176 | €211,07 | €422,14 | €50,66 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1363,81560 | €966,09 | €1.932,17 | €49,52 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01601 | €209,64 | €419,27 | €50,31 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | UNI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 5,12502 | 5,12502 | 4,91893 | 2,58814 | 5,74332 | €624,55 | €1.249,09 | €50,23 | €0,00 |
| Global Confluence puro 1H | DOGE | SHORT | Global Confluence puro | 60m | 2,0x | 0,08282 | 0,08335 | 0,08433 | 0,12382 | 0,07905 | €1.335,17 | €2.670,35 | €48,67 | €-17,08 |
| Combo Trend | BEAT | SHORT | Combo Trend | 60m | 2,0x | 0,25984 | 0,25984 | 0,25657 | 0,38847 | 0,19125 | €193,71 | €387,42 | €0,00 | €-0,00 |
| Combo Trend | ADA | SHORT | Combo Trend | 60m | 2,0x | 0,19986 | 0,19986 | 0,20356 | 0,29879 | 0,19173 | €1.205,82 | €2.411,64 | €44,61 | €-0,00 |
| Combo Trend | ENA | SHORT | Combo Trend | 60m | 2,0x | 0,14884 | 0,14884 | 0,15655 | 0,22252 | 0,13188 | €440,69 | €881,38 | €45,66 | €-0,00 |
| Combo Trend | DOGE | SHORT | Combo Trend | 60m | 2,0x | 0,08264 | 0,08335 | 0,08416 | 0,12355 | 0,07930 | €1.206,71 | €2.413,43 | €44,39 | €-20,72 |
| Combo Mean Reversion | ADA | LONG | Combo Mean Reversion | 60m | 2,0x | 0,20284 | 0,20284 | 0,19804 | 0,10244 | 0,21052 | €942,00 | €1.883,99 | €44,59 | €0,00 |
| Combo Scanner | BOME | LONG | Combo Scanner | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €195,20 | €390,40 | €46,85 | €0,00 |
| Combo Scanner | TRUMP | LONG | Combo Scanner | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,14149 | €213,98 | €427,96 | €49,38 | €0,00 |
| Combo Scanner | SKHYNIX | LONG | Combo Scanner | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €24,78 | €49,55 | €1,27 | €0,00 |
| Combo Scanner | UNI | LONG | Combo Scanner | 60m | 2,0x | 5,12502 | 5,12502 | 4,91893 | 2,58814 | 5,57844 | €609,76 | €1.219,51 | €49,04 | €0,00 |
| Combo Scanner | SKR | LONG | Combo Scanner | 60m | 2,0x | 0,02711 | 0,02863 | 0,02711 | 0,01369 | 0,03427 | €202,55 | €405,10 | €0,00 | €22,69 |
| Combo Scanner | DOGE | SHORT | Combo Scanner | 60m | 2,0x | 0,08263 | 0,08335 | 0,08391 | 0,12353 | 0,07981 | €14,84 | €29,68 | €0,46 | €-0,26 |
| Combo Scanner | HYPE | LONG | Combo Scanner | 60m | 2,0x | 84,21884 | 84,11000 | 82,54219 | 42,53051 | 87,90746 | €12,71 | €25,41 | €0,51 | €-0,03 |
| Combo Adaptive | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,01735 | 121,01735 | 128,90956 | 180,92093 | 105,23292 | €367,30 | €734,61 | €47,91 | €-0,00 |
| Combo Adaptive | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €40,89 | €81,77 | €3,12 | €0,00 |
| Combo Adaptive | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,52450 | 2,33981 | 1,27487 | 2,89389 | €18,69 | €37,37 | €2,73 | €0,00 |
| Combo Adaptive | ENA | SHORT | Combo Adaptive | 60m | 2,0x | 0,15004 | 0,15004 | 0,15587 | 0,22431 | 0,13838 | €667,09 | €1.334,17 | €51,85 | €-0,00 |
| Combo Adaptive | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,08276 | 0,08335 | 0,08414 | 0,12373 | 0,08000 | €29,77 | €59,54 | €0,99 | €-0,42 |
| Combo Adaptive | SUI | SHORT | Combo Adaptive | 60m | 2,0x | 0,71926 | 0,71926 | 0,73633 | 1,07529 | 0,68511 | €1.048,34 | €2.096,69 | €49,77 | €-0,00 |
| Combo Adaptive | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 84,10682 | 84,11000 | 82,40110 | 42,47394 | 87,51826 | €13,61 | €27,22 | €0,55 | €0,00 |
| Combo Adaptive | BTR | LONG | Combo Adaptive | 60m | 2,0x | 0,17599 | 0,17595 | 0,15487 | 0,08887 | 0,21822 | €207,32 | €414,65 | €49,76 | €-0,08 |
| Combo Adaptive Mfe Trail | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €54,29 | €108,58 | €4,15 | €0,00 |
| Combo Adaptive Mfe Trail | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,52450 | 2,33981 | 1,27487 | 2,89389 | €315,75 | €631,50 | €46,20 | €0,00 |
| Combo Adaptive Mfe Trail | TUT | SHORT | Combo Adaptive | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €190,04 | €380,09 | €45,61 | €-0,00 |
| Combo Adaptive Mfe Trail | PROM | LONG | Combo Adaptive | 60m | 2,0x | 7,01991 | 7,01991 | 6,30832 | 3,54505 | 8,44309 | €21,72 | €43,45 | €4,40 | €0,00 |
| Combo Adaptive Mfe Trail | ENA | SHORT | Combo Adaptive | 60m | 2,0x | 0,15004 | 0,15004 | 0,15587 | 0,22431 | 0,13838 | €581,51 | €1.163,02 | €45,20 | €-0,00 |
| Combo Adaptive Mfe Trail | SKR | LONG | Combo Adaptive | 60m | 2,0x | 0,02975 | 0,02863 | 0,02618 | 0,01502 | 0,03689 | €150,12 | €300,24 | €36,03 | €-11,29 |
| Combo Adaptive Quality7 V1 | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €371,68 | €743,36 | €47,16 | €-0,00 |
| Combo Adaptive Quality7 V1 | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €646,78 | €1.293,57 | €49,39 | €0,00 |
| Combo Adaptive Quality7 V1 | ZORA | LONG | Combo Adaptive | 60m | 2,0x | 0,00942 | 0,00942 | 0,00829 | 0,00476 | 0,01169 | €199,23 | €398,46 | €47,81 | €0,00 |
| Combo Adaptive Quality7 V1 | 0G | LONG | Combo Adaptive | 60m | 2,0x | 0,24605 | 0,24590 | 0,22046 | 0,12425 | 0,29722 | €220,81 | €441,63 | €45,92 | €-0,26 |
| Combo Adaptive Regime V1 | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €987,06 | €1.974,12 | €49,09 | €0,00 |
| Combo Adaptive Long Only V1 | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €645,48 | €1.290,95 | €46,47 | €0,00 |
| Combo Adaptive Long Only V1 | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,52450 | 2,33981 | 1,27487 | 2,89389 | €48,12 | €96,24 | €7,04 | €0,00 |
| Combo Adaptive Long Only V1 | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1331,36020 | €968,99 | €1.937,97 | €49,66 | €0,00 |
| Combo Adaptive Long Only V1 | HEMI | LONG | Combo Adaptive | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €216,09 | €432,18 | €51,86 | €0,00 |
| Combo Adaptive Long Only V1 | UNI | LONG | Combo Adaptive | 60m | 2,0x | 5,12502 | 5,12502 | 4,91893 | 2,58814 | 5,53722 | €643,56 | €1.287,13 | €51,76 | €0,00 |
| Combo Adaptive Partial 1R V1 | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,01735 | 121,01735 | 128,90956 | 180,92093 | 105,23292 | €352,70 | €705,40 | €46,00 | €-0,00 |
| Combo Adaptive Partial 1R V1 | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,52450 | 2,33981 | 1,27487 | 2,89389 | €347,19 | €694,38 | €50,80 | €0,00 |
| Combo Adaptive Partial 1R V1 | VELVET | SHORT | Combo Adaptive | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €207,76 | €415,52 | €0,00 | €-0,00 |
| Combo Adaptive Partial 1R V1 | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €1.013,20 | €2.026,40 | €50,39 | €0,00 |
| Combo Adaptive Partial 1R V1 | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,08264 | 0,08335 | 0,08401 | 0,12355 | 0,07990 | €127,08 | €254,16 | €4,21 | €-2,18 |
| Combo Adaptive Runner25 V1 | SKR | LONG | Combo Adaptive | 60m | 2,0x | 0,02975 | 0,02863 | 0,02618 | 0,01502 | 0,04046 | €186,75 | €373,50 | €44,82 | €-14,05 |
| Combo Adaptive Runner25 V1 | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 84,10682 | 84,11000 | 82,40110 | 42,47394 | 89,22398 | €1.104,98 | €2.209,97 | €44,82 | €0,08 |
| Combo Adaptive Runner25 V1 | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,08307 | 0,08335 | 0,08429 | 0,12419 | 0,07941 | €1.525,78 | €3.051,57 | €44,81 | €-10,28 |
| Combo Adaptive Runner25 V1 | BTR | LONG | Combo Adaptive | 60m | 2,0x | 0,17599 | 0,17595 | 0,15487 | 0,08887 | 0,23934 | €184,50 | €369,00 | €44,28 | €-0,07 |
| Combo Adaptive Tp3 V1 | SKR | LONG | Combo Adaptive | 60m | 2,0x | 0,02975 | 0,02863 | 0,02618 | 0,01502 | 0,04046 | €183,26 | €366,53 | €43,98 | €-13,79 |
| Combo Adaptive Tp3 V1 | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 84,10682 | 84,11000 | 82,40110 | 42,47394 | 89,22398 | €1.084,34 | €2.168,68 | €43,98 | €0,08 |
| Combo Adaptive Tp3 V1 | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,08307 | 0,08335 | 0,08429 | 0,12419 | 0,07941 | €1.497,28 | €2.994,56 | €43,97 | €-10,09 |
| Combo Adaptive Tp3 V1 | BTR | LONG | Combo Adaptive | 60m | 2,0x | 0,17599 | 0,17595 | 0,15487 | 0,08887 | 0,23934 | €181,05 | €362,11 | €43,45 | €-0,07 |
| Btc Bollinger 4H | BTC | SHORT | Bollinger mean reversion | 240m | 2,0x | 80323,10217 | 78903,40000 | 79375,01684 | 120083,03774 | 75648,94663 | €775,58 | €1.551,16 | €0,00 | €27,42 |
| Sol Ema 4H | SOL | LONG | Trend following EMA | 240m | 2,0x | 105,86117 | 103,94100 | 99,76922 | 53,45989 | 121,09104 | €439,17 | €878,34 | €50,55 | €-15,93 |
| Sol Donchian 4H | SOL | LONG | Donchian breakout 20 barre | 240m | 2,0x | 104,08581 | 103,94100 | 98,18471 | 52,56334 | 120,60890 | €449,62 | €899,24 | €50,98 | €-1,25 |
| Sol Bollinger 4H | SOL | SHORT | Bollinger mean reversion | 240m | 2,0x | 107,28254 | 103,94100 | 105,65046 | 160,38740 | 97,27311 | €478,97 | €957,94 | €0,00 | €29,84 |
| Sol Adaptive 4H | SOL | LONG | Combo Adaptive | 240m | 2,0x | 105,86117 | 103,94100 | 99,21540 | 53,45989 | 122,47558 | €407,92 | €815,83 | €51,22 | €-14,80 |
| Doge Ema 1H | DOGE | SHORT | Trend following EMA | 60m | 3,0x | 0,08263 | 0,08335 | 0,08391 | 0,10976 | 0,08007 | €1.077,39 | €3.232,18 | €50,16 | €-28,15 |
| Master Adaptive V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99403 | 639,55695 | 1331,36019 | €22,75 | €45,50 | €1,17 | €0,00 |
| Master Adaptive V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €195,57 | €391,15 | €46,94 | €0,00 |
| Master Adaptive V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,24590 | 0,20498 | 0,11491 | 0,27267 | €236,54 | €473,08 | €46,91 | €38,16 |
| Master Adaptive V1 | SKR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,02872 | 0,02863 | 0,02527 | 0,01450 | 0,03561 | €195,43 | €390,87 | €46,90 | €-1,18 |
| Master Adaptive V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 520,62410 | 514,88000 | 498,16818 | 262,91517 | 565,53595 | €529,71 | €1.059,43 | €45,70 | €-11,69 |
| Master Adaptive No Alt V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1255,10261 | 1255,10261 | 1225,12158 | 633,82682 | 1315,06467 | €19,09 | €38,19 | €0,91 | €0,00 |
| Master Adaptive No Alt V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €183,81 | €367,62 | €44,11 | €0,00 |
| Master Adaptive No Alt V1 | SKR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,02969 | 0,02863 | 0,02612 | 0,01499 | 0,03681 | €190,91 | €381,83 | €45,82 | €-13,57 |
| Master Adaptive No Alt V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 83,81176 | 84,11000 | 82,16730 | 42,32494 | 87,10068 | €1.167,57 | €2.335,14 | €45,82 | €8,31 |
| Master Adaptive No Alt V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 514,40286 | 514,88000 | 493,14790 | 259,77344 | 556,91277 | €554,63 | €1.109,27 | €45,83 | €1,03 |
| Master Adaptive Strict3 V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €178,16 | €356,31 | €42,76 | €0,00 |
| Master Adaptive Strict3 V1 | PROM | LONG | Master Adaptive Consensus | 60m | 2,0x | 7,01991 | 7,01991 | 6,30832 | 3,54505 | 8,44309 | €215,49 | €430,99 | €43,69 | €0,00 |
| Master Adaptive Expanded V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03814 | 0,02188 | 0,05374 | €197,50 | €395,01 | €47,40 | €0,00 |
| Master Adaptive Expanded V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1261,89668 | 1261,89668 | 1231,08309 | 637,25783 | 1323,52387 | €934,21 | €1.868,43 | €45,62 | €0,00 |
| Master Adaptive Expanded V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01194 | 0,01194 | 0,01050 | 0,00603 | 0,01480 | €195,34 | €390,67 | €46,88 | €0,00 |
| Master Adaptive Expanded V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,24590 | 0,20498 | 0,11491 | 0,27267 | €236,25 | €472,49 | €46,85 | €38,11 |
| Master Adaptive Expanded V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 84,10682 | 84,11000 | 82,40110 | 42,47394 | 87,51826 | €15,68 | €31,37 | €0,64 | €0,00 |
| Master Adaptive Gb20 V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99403 | 639,55695 | 1331,36019 | €22,45 | €44,90 | €1,15 | €0,00 |
| Master Adaptive Gb20 V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €193,03 | €386,06 | €46,33 | €0,00 |
| Master Adaptive Gb20 V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,24590 | 0,20498 | 0,11491 | 0,27267 | €233,42 | €466,83 | €46,29 | €37,65 |
| Master Adaptive Gb20 V1 | SKR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,02872 | 0,02863 | 0,02527 | 0,01450 | 0,03561 | €192,86 | €385,71 | €46,29 | €-1,17 |
| Master Adaptive Gb20 V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 520,62410 | 514,88000 | 498,16818 | 262,91517 | 565,53595 | €522,62 | €1.045,25 | €45,08 | €-11,53 |
| Master Adaptive Runner25 V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03814 | 0,02188 | 0,05894 | €34,77 | €69,54 | €8,34 | €0,00 |
| Master Adaptive Runner25 V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1255,10261 | 1255,10261 | 1225,12158 | 633,82682 | 1345,04570 | €27,05 | €54,10 | €1,29 | €0,00 |
| Master Adaptive Runner25 V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01601 | €185,86 | €371,72 | €44,61 | €0,00 |
| Master Adaptive Runner25 V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,24590 | 0,20498 | 0,11491 | 0,29523 | €233,84 | €467,69 | €46,37 | €37,72 |
| Master Adaptive Runner25 V1 | SKR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,02872 | 0,02863 | 0,02527 | 0,01450 | 0,03906 | €193,21 | €386,42 | €46,37 | €-1,17 |
| Master Adaptive Runner25 V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 520,62410 | 514,88000 | 498,16818 | 262,91517 | 587,99187 | €446,15 | €892,30 | €38,49 | €-9,84 |
| Combo Adaptive Side Regime Guard V1 | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €77,52 | €155,04 | €5,58 | €0,00 |
| Combo Adaptive Side Regime Guard V1 | VELVET | SHORT | Combo Adaptive | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €216,61 | €433,23 | €0,00 | €-0,00 |
| Combo Adaptive Side Regime Guard V1 | TUT | SHORT | Combo Adaptive | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €192,40 | €384,79 | €46,18 | €-0,00 |
| Combo Adaptive Side Regime Guard V1 | ENA | SHORT | Combo Adaptive | 60m | 2,0x | 0,15023 | 0,15023 | 0,15627 | 0,22459 | 0,13814 | €585,15 | €1.170,29 | €47,08 | €-0,00 |
| Combo Adaptive Side Regime Guard V1 | SUI | SHORT | Combo Adaptive | 60m | 2,0x | 0,71926 | 0,71926 | 0,73633 | 1,07529 | 0,68511 | €1.060,94 | €2.121,88 | €50,37 | €-0,00 |
| Master Adaptive Gb20 Be V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99403 | 639,55695 | 1331,36019 | €22,86 | €45,73 | €1,17 | €0,00 |
| Master Adaptive Gb20 Be V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €196,54 | €393,08 | €47,17 | €0,00 |
| Master Adaptive Gb20 Be V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,24590 | 0,20498 | 0,11491 | 0,27267 | €237,71 | €475,42 | €47,14 | €38,35 |
| Master Adaptive Gb20 Be V1 | SKR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,02872 | 0,02863 | 0,02527 | 0,01450 | 0,03561 | €196,40 | €392,81 | €47,14 | €-1,19 |
| Master Adaptive Gb20 Be V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 520,62410 | 514,88000 | 498,16818 | 262,91517 | 565,53595 | €532,34 | €1.064,67 | €45,92 | €-11,75 |
| Master Adaptive Gb20 Partial V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99403 | 639,55695 | 1331,36019 | €22,84 | €45,68 | €1,17 | €0,00 |
| Master Adaptive Gb20 Partial V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €196,33 | €392,67 | €47,12 | €0,00 |
| Master Adaptive Gb20 Partial V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,24590 | 0,20498 | 0,11491 | 0,27267 | €237,46 | €474,91 | €47,09 | €38,31 |
| Master Adaptive Gb20 Partial V1 | SKR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,02872 | 0,02863 | 0,02527 | 0,01450 | 0,03561 | €196,19 | €392,39 | €47,09 | €-1,19 |
| Master Adaptive Gb20 Partial V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 520,62410 | 514,88000 | 498,16818 | 262,91517 | 565,53595 | €531,77 | €1.063,54 | €45,87 | €-11,73 |
| Master Adaptive Gb20 Loss Cap V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03828 | 0,02188 | 0,05682 | €195,70 | €391,41 | €45,67 | €0,00 |
| Master Adaptive Gb20 Loss Cap V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01069 | 0,00594 | 0,01465 | €210,34 | €420,68 | €38,67 | €0,00 |
| Master Adaptive Gb20 Loss Cap V1 | PROM | LONG | Master Adaptive Consensus | 60m | 2,0x | 7,01991 | 7,01991 | 6,48622 | 3,54505 | 8,44309 | €34,75 | €69,51 | €5,28 | €0,00 |
| Master Adaptive Gb20 Loss Cap V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,24590 | 0,21062 | 0,11491 | 0,27267 | €309,65 | €619,30 | €46,05 | €49,95 |
| Master Adaptive Gb20 Loss Cap V1 | SKR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,02872 | 0,02863 | 0,02527 | 0,01450 | 0,03791 | €191,88 | €383,75 | €46,05 | €-1,16 |
| Master Adaptive Gb20 Loss Cap V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 84,21884 | 84,11000 | 82,96136 | 42,53051 | 87,57213 | €14,69 | €29,38 | €0,44 | €-0,04 |
| Master Adaptive Gb20 Loss Cap V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 514,40286 | 514,88000 | 498,46164 | 259,77344 | 556,91277 | €32,91 | €65,81 | €2,04 | €0,06 |
| 1H Fast V3 Nohigh Range Only V1 | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,20283 | 0,20283 | 0,20750 | 0,26943 | 0,19582 | €740,69 | €2.222,07 | €51,20 | €-0,00 |
| 1H Fast V3 Nohigh Range Only V1 | SKR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,02969 | 0,02863 | 0,02612 | 0,01994 | 0,03503 | €143,27 | €429,80 | €51,58 | €-15,27 |
| 1H Fast V3 Nohigh Regime Guard V1 | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €140,84 | €422,53 | €50,70 | €-0,00 |
| 1H Fast V3 Nohigh Regime Guard V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €143,15 | €429,46 | €50,70 | €-0,00 |
| 1H Fast V3 Nohigh Regime Guard V1 | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,20283 | 0,20283 | 0,20750 | 0,26943 | 0,19582 | €34,57 | €103,71 | €2,39 | €-0,00 |
| 1H Fast V3 Nohigh Regime Guard V1 | SKR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,02975 | 0,02863 | 0,02618 | 0,01998 | 0,03510 | €143,85 | €431,56 | €51,79 | €-16,23 |
| 1H Fast V3 Nohigh Regime Guard V1 | BTR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,17599 | 0,17595 | 0,15842 | 0,11820 | 0,20234 | €171,09 | €513,26 | €51,23 | €-0,10 |
| Main Side Regime Guard V1 | VELVET | LONG | Confluenza trend | 240m | 3,0x | 0,55987 | 0,55987 | 0,49269 | 0,37605 | 0,69424 | €142,25 | €426,74 | €51,21 | €0,00 |
| Main Side Regime Guard V1 | AKE | LONG | Confluenza trend | 240m | 3,0x | 0,01021 | 0,01021 | 0,00899 | 0,00686 | 0,01266 | €145,97 | €437,90 | €52,55 | €0,00 |
| Main Side Regime Guard V1 | XRP | LONG | Confluenza trend | 240m | 3,0x | 1,47102 | 1,38478 | 1,31178 | 0,98804 | 1,78951 | €12,77 | €38,31 | €4,15 | €-2,25 |
| Main Side Regime Guard V1 | ETH | LONG | Confluenza trend | 240m | 3,0x | 2437,91749 | 2473,50000 | 2326,72117 | 1637,46791 | 2660,31012 | €9,94 | €29,83 | €1,36 | €0,44 |
| Main Side Regime Guard V1 | ENA | LONG | Confluenza trend | 240m | 3,0x | 0,16108 | 0,16108 | 0,14175 | 0,10819 | 0,19974 | €150,44 | €451,33 | €54,16 | €0,00 |
| Main Side Regime Guard V1 | UNI | LONG | Confluenza trend | 240m | 3,0x | 5,15403 | 5,15403 | 4,78412 | 3,46179 | 5,89386 | €248,23 | €744,68 | €53,45 | €0,00 |
| Main Dynamic Asset Selector V1 | ENA | LONG | Confluenza trend | 240m | 3,0x | 0,16108 | 0,16108 | 0,14175 | 0,10819 | 0,19974 | €140,98 | €422,93 | €50,75 | €0,00 |
| Combo Trend Side Regime Guard V1 | VELVET | SHORT | Combo Trend | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,12693 | €217,86 | €435,73 | €0,00 | €-0,00 |
| Combo Trend Side Regime Guard V1 | TUT | SHORT | Combo Trend | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03364 | €12,81 | €25,62 | €3,07 | €-0,00 |
| Combo Trend Side Regime Guard V1 | ENA | SHORT | Combo Trend | 60m | 2,0x | 0,14884 | 0,14884 | 0,15655 | 0,22252 | 0,13188 | €528,31 | €1.056,62 | €54,74 | €-0,00 |
| Combo Trend Side Regime Guard V1 | SUI | SHORT | Combo Trend | 60m | 2,0x | 0,71926 | 0,71926 | 0,73823 | 1,07529 | 0,67752 | €1.029,16 | €2.058,32 | €54,29 | €-0,00 |
| Combo Trend Side Regime Guard V1 | DOGE | SHORT | Combo Trend | 60m | 2,0x | 0,08277 | 0,08335 | 0,08437 | 0,12375 | 0,07926 | €1.329,20 | €2.658,40 | €51,29 | €-18,52 |
| 1H Fast Nohigh Cap75 Short Only V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €135,82 | €407,46 | €48,90 | €-0,00 |
| 1H Fast Nohigh Cap75 Short Only V1 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €138,05 | €414,14 | €48,89 | €-0,00 |
| 1H Fast Nohigh Cap75 Short Only V1 | SKR | LONG | Momentum / breakout | 60m | 3,0x | 0,02975 | 0,02863 | 0,02618 | 0,01998 | 0,03510 | €134,79 | €404,37 | €48,52 | €-15,21 |
| 1H Fast Nohigh Cap75 Short Only V1 | BTR | LONG | Momentum / breakout | 60m | 3,0x | 0,17599 | 0,17595 | 0,15842 | 0,11820 | 0,20234 | €163,81 | €491,44 | €49,06 | €-0,10 |
| 1H Balanced V3 Long Only V1 | SKHYNIX | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1220,85412 | 1220,85412 | 1177,63561 | 820,00702 | 1307,29117 | €435,49 | €1.306,46 | €46,25 | €0,00 |
| 1H Balanced V3 Long Only V1 | ADA | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,20138 | 0,20138 | 0,20719 | 0,26750 | 0,18976 | €529,53 | €1.588,58 | €45,82 | €-0,00 |
| 1H Balanced V3 Long Only V1 | ENA | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,14884 | 0,14884 | 0,15578 | 0,19771 | 0,13496 | €328,05 | €984,14 | €45,88 | €-0,00 |
| 1H Balanced V3 Long Only V1 | DOGE | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,08276 | 0,08335 | 0,08414 | 0,10993 | 0,08000 | €875,30 | €2.625,90 | €43,86 | €-18,71 |
| Scanner Bottom5 Short Profit Lock V1 | SOXL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €381,80 | €763,60 | €48,45 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | SNDK | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €496,62 | €993,25 | €48,08 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | VELVET | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €192,55 | €385,10 | €0,00 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | TUT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €179,76 | €359,53 | €43,14 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | SOXL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €382,38 | €764,76 | €48,52 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | SNDK | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €497,38 | €994,76 | €48,15 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | VELVET | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €192,85 | €385,69 | €0,00 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | TUT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €180,04 | €360,08 | €43,21 | €-0,00 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | XMR | LONG | 2026-09-01T02:30:00+00:00 | 502,97424 | €-45,73 | -1,03 | STOP |
| Master Adaptive Gb20 Loss Cap V1 | XMR | LONG | 2026-09-01T02:30:00+00:00 | 503,68141 | €-2,58 | -1,04 | STOP |
| Combo Adaptive Quality7 V1 | XMR | LONG | 2026-09-01T02:30:00+00:00 | 502,97424 | €-48,59 | -1,03 | STOP |
| 1H Fast V3 No Esports Long Only V1 | 0G | LONG | 2026-09-01T02:30:00+00:00 | 0,25372 | €66,85 | 1,47 | TARGET |
| 1H Fast V3 Nohigh V1 | 0G | LONG | 2026-09-01T02:30:00+00:00 | 0,25372 | €72,31 | 1,47 | TARGET |
| 1H Fast V3 Long Nohigh Cap75 V1 | 0G | LONG | 2026-09-01T02:30:00+00:00 | 0,25372 | €70,72 | 1,47 | TARGET |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | 0G | LONG | 2026-09-01T02:30:00+00:00 | 0,25372 | €68,71 | 1,47 | TARGET |
| 1H Fast Score 6 75 Cost Aware V1 | XMR | LONG | 2026-09-01T02:30:00+00:00 | 506,25714 | €-47,36 | -1,04 | STOP |
| 1H Fast No Pepe V1 | XMR | LONG | 2026-09-01T02:30:00+00:00 | 502,88839 | €-1,64 | -1,04 | STOP |
| 1H Fast No Pepe V1 | 0G | LONG | 2026-09-01T02:30:00+00:00 | 0,25372 | €74,71 | 1,47 | TARGET |
| 1H Fast Nohigh Cap75 V1 | 0G | LONG | 2026-09-01T02:30:00+00:00 | 0,25372 | €73,77 | 1,47 | TARGET |
| 1H Fast Nohigh Cap75 Short Only V1 | 0G | LONG | 2026-09-01T02:30:00+00:00 | 0,25372 | €71,93 | 1,47 | TARGET |

## Regole invarianti

- Nessuna martingala e nessuna mediazione automatica in perdita.
- Il target mensile riduce il rischio quando viene avvicinato o raggiunto; non lo aumenta mai.
- Il portafoglio principale e le simulazioni di confronto hanno contabilità separata.
- Commissioni, slippage e funding sono inclusi nella simulazione secondo i parametri configurati.
- Quando stop e target risultano toccati nella stessa candela, prevale lo stop salvo modifica esplicita della configurazione.
