# Paper trading automatico KuCoin

Generato: 2026-08-23T05:33:01+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-08-23T05:05:29+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-08-23T05:05:29+00:00 | 2026-08-23T05:05:29+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-08-23T04:45:00+00:00 | 2026-08-23T04:45:00+00:00 | 5,7 min | 25,0 min | OK |
| 60m | 12 | 2026-08-23T04:00:00+00:00 | 2026-08-23T04:00:00+00:00 | 5,7 min | 45,0 min | OK |
| 240m | 12 | 2026-08-23T00:00:00+00:00 | 2026-08-23T00:00:00+00:00 | 1,09 h | 1,00 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | PUMP | 240m | LONG | 7,75 | 6,00 | 0,00 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | HYPE | 240m | LONG | 6,25 | 6,00 | 0,00 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | XRP | 240m | LONG | 6,25 | 6,00 | 0,00 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | ZEC | 240m | LONG | 6,25 | 6,00 | 0,00 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | TRUMP | 240m | LONG | 5,75 | 6,00 | 0,25 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | ETH | 240m | LONG | 5,69 | 6,00 | 0,31 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | PEPE | 240m | LONG | 4,75 | 6,00 | 1,25 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | ADA | 240m | LONG | 4,68 | 6,00 | 1,32 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | DOGE | 240m | LONG | 4,25 | 6,00 | 1,75 | STALE_CANDLE | 1,09 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | SOL | 240m | LONG | 3,26 | 6,00 | 2,74 | STALE_CANDLE | 1,09 h | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | SUI | 240m | LONG | 2,07 | 6,00 | 3,93 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | BTC | 240m | LONG | 1,75 | 6,00 | 4,25 | STALE_CANDLE | 1,09 h | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| 1H Balanced Long No Rhv V1 | PUMP | 60m | LONG | 5,50 | 5,00 | 0,00 | READY | 5,7 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Fast Long Btc 1 3 Cap75 V1 | PUMP | 60m | LONG | 5,50 | 4,50 | 0,00 | OPENED | 5,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast No Pepe V1 | PUMP | 60m | LONG | 5,50 | 4,50 | 0,00 | OPENED | 5,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Tp2 V1 | PUMP | 60m | LONG | 5,50 | 4,50 | 0,00 | OPENED | 5,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top10 Long | PUMP | 60m | LONG | 5,50 | 5,00 | 0,00 | OPENED | 5,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top5 Btc Btc Le3 V1 | PUMP | 60m | LONG | 5,50 | 5,00 | 0,00 | READY | 5,7 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Scanner Top5 Btc Btc 2 3 V1 | PUMP | 60m | LONG | 5,50 | 5,00 | 0,00 | READY | 5,7 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Combo Adaptive | PUMP | 60m | LONG | 5,50 | 5,00 | 0,00 | READY | 5,7 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.777,56 | -2,22% | €29,21 | €3.000,00 | 0,97% | 5 | 51 | 37,25% | 0,87 | 6,39% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 51 | 2073 | PRIME INDICAZIONI | 100 (mancano 49) |

- Trade del Principale 4H chiusi: **51**; win rate **37,25%**; profit factor **0,87**.
- Expectancy: **€-3,76** per trade; P&L netto: **€-191,70**; max drawdown: **6,39%**.
- Valutazione: **Si può osservare la direzione, ma il risultato resta fragile.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 5 | €9.777,56 | €692,34 | €2.077,03 | €193,46 | €-29,73 |
| TEST | Benchmark Donchian breakout 1H | 1 | €11.568,07 | €641,25 | €1.282,50 | €50,11 | €0,00 |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | 6 | €11.320,66 | €845,88 | €2.537,64 | €176,21 | €-33,48 |
| TEST | Donchian 1H Gb20 120R V1 | 1 | €11.295,72 | €626,15 | €1.252,30 | €48,93 | €0,00 |
| TEST | Combo Trend Side Regime Guard V1 | 4 | €11.177,33 | €968,94 | €1.937,88 | €168,98 | €-63,84 |
| TEST | Scanner Top 5 Long 1H | 4 | €10.988,46 | €871,47 | €1.742,95 | €164,17 | €-60,18 |
| TEST | Main Side Regime Guard V1 | 5 | €10.798,34 | €667,39 | €2.002,16 | €215,82 | €7,13 |
| TEST | 1H Fast No Pepe V1 | 6 | €10.661,87 | €1.291,51 | €3.874,54 | €213,25 | €-51,62 |
| TEST | Combo Adaptive | 7 | €10.565,37 | €1.352,79 | €2.705,58 | €211,71 | €-47,37 |
| TEST | Combo Adaptive Long Only V1 | 5 | €10.556,64 | €1.580,07 | €3.160,14 | €205,48 | €-59,34 |
| TEST | Combo Adaptive Side Regime Guard V1 | 6 | €10.427,47 | €1.278,76 | €2.557,53 | €209,56 | €-68,26 |
| TEST | Scanner Top5 Btc Tp3 V1 | 5 | €10.411,45 | €1.122,20 | €2.244,40 | €209,07 | €-58,62 |
| TEST | Scanner Top5 Btc Runner25 V1 | 5 | €10.405,35 | €1.121,54 | €2.243,08 | €208,95 | €-58,59 |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | 4 | €10.389,26 | €1.094,98 | €3.284,95 | €156,36 | €-0,60 |
| TEST | Rapida 1H V3 Filtered | 4 | €10.322,51 | €1.087,95 | €3.263,85 | €155,36 | €-0,60 |
| TEST | Rapida 1H V2 | 0 | €10.322,19 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 0 | €10.300,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Ampia 4H | 7 | €10.276,40 | €998,50 | €1.997,00 | €206,18 | €-55,65 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 0 | €10.271,73 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top 5 + forza BTC 1H | 4 | €10.258,80 | €812,79 | €1.625,58 | €153,11 | €-56,18 |
| TEST | 1H Fast V3 Nohigh Range Only V1 | 0 | €10.247,95 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 0 | €10.239,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 0 | €10.235,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Main Dynamic Asset Selector V1 | 0 | €10.213,35 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Donchian 4H | 0 | €10.196,46 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top10 Long | 5 | €10.189,46 | €1.584,21 | €3.168,42 | €203,77 | €-24,07 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 0 | €10.185,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 4H | 1 | €10.160,35 | €330,98 | €661,97 | €50,82 | €-4,03 |
| TEST | Sol Donchian 1H | 0 | €10.156,88 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Score 6 75 Range Only V1 | 0 | €10.149,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 0 | €10.145,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | 0 | €10.140,84 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 1H | 0 | €10.138,40 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Tp2 V1 | 6 | €10.122,74 | €1.016,36 | €3.049,09 | €202,47 | €-4,81 |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 0 | €10.099,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 1H | 0 | €10.083,25 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Partial 1R V1 | 7 | €10.078,03 | €1.360,84 | €2.721,68 | €202,03 | €-63,01 |
| TEST | Btc Adaptive 4H | 0 | €10.070,19 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 1H | 0 | €10.067,96 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H V3 Filtered | 5 | €10.062,57 | €1.007,95 | €3.023,86 | €152,06 | €-22,88 |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 0 | €10.048,77 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 No Esports Long Only V1 | 6 | €10.047,37 | €774,44 | €2.323,33 | €151,93 | €-17,72 |
| TEST | Doge Bollinger 1H | 0 | €10.046,17 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €10.045,08 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V1 | 0 | €10.043,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Balanced Short Trend Down Strict V1 | 0 | €10.035,46 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 4H | 0 | €10.029,45 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · prudente · 5x | 0 | €10.028,67 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Nohigh Cap75 V1 | 0 | €10.028,66 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 4H | 1 | €10.019,90 | €356,10 | €712,19 | €50,12 | €-4,34 |
| TEST | Btc Ema 4H | 0 | €10.019,41 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €50 · 15x | 0 | €10.017,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €50 · 15x | 0 | €10.015,51 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 1H | 1 | €10.014,23 | €349,20 | €1.047,59 | €50,20 | €-24,46 |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | 0 | €10.013,82 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 0 | €10.009,02 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 0 | €10.008,92 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | 1 | €10.007,52 | €299,55 | €599,09 | €50,20 | €-32,20 |
| TEST | Scalp RSI Short 85 · €10 · 15x | 0 | €10.003,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 0 | €10.003,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €10 · 15x | 0 | €10.003,10 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Continuation V1 | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €10 · 15x | 0 | €9.999,33 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €10 · 15x | 0 | €9.997,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €50 · 15x | 0 | €9.996,64 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 0 | €9.995,23 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · prudente · 5x | 0 | €9.991,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Ema 1H | 1 | €9.991,09 | €248,90 | €746,70 | €50,09 | €-26,37 |
| TEST | Scalp RSI Long 25 · €10 · 15x | 0 | €9.990,45 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €50 · 15x | 0 | €9.988,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 0 | €9.987,48 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | 5 | €9.984,89 | €1.204,97 | €3.614,92 | €199,71 | €-39,06 |
| TEST | Sol Bollinger 4H | 0 | €9.981,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · prudente · 5x | 0 | €9.980,94 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 4H | 0 | €9.965,81 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · prudente · 5x | 0 | €9.952,43 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €50 · 15x | 0 | €9.952,25 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 1H | 0 | €9.941,95 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.939,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top15 Long | 5 | €9.928,57 | €909,52 | €1.819,04 | €147,99 | €-55,00 |
| TEST | Scanner Top20 Long | 5 | €9.928,57 | €909,52 | €1.819,04 | €147,99 | €-55,00 |
| TEST | Doge Donchian 1H | 0 | €9.911,95 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Ema 4H | 0 | €9.911,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Adaptive 1H | 0 | €9.897,54 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Quality7 Regime V1 | 1 | €9.881,64 | €295,78 | €591,56 | €49,57 | €-31,79 |
| TEST | Sol Bollinger 1H | 0 | €9.873,88 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 1H | 1 | €9.871,81 | €344,23 | €1.032,69 | €49,48 | €-24,11 |
| TEST | 1H Fast V3 No Esports V1 | 5 | €9.866,96 | €801,81 | €2.405,44 | €147,70 | €-20,12 |
| TEST | Eth Ema 1H | 0 | €9.844,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Scanner | 4 | €9.842,46 | €779,80 | €1.559,60 | €146,89 | €-53,90 |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 0 | €9.837,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 0 | €9.817,34 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Forza relativa 1H V2 | 4 | €9.811,28 | €1.119,43 | €2.238,85 | €148,55 | €-38,88 |
| TEST | Scanner Top5 Btc Guard V1 | 4 | €9.809,19 | €787,86 | €1.575,71 | €148,13 | €-32,51 |
| TEST | Combo Adaptive Regime V1 | 4 | €9.805,90 | €1.720,16 | €3.440,31 | €197,23 | €-78,08 |
| TEST | Eth Donchian 1H | 0 | €9.801,75 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | 0 | €9.779,10 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Quality7 V1 | 5 | €9.776,66 | €1.601,29 | €3.202,58 | €196,10 | €-23,82 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 0 | €9.762,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Balanced Long No Rhv V1 | 5 | €9.747,79 | €1.229,56 | €3.688,69 | €195,27 | €-17,67 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 0 | €9.723,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Bollinger 1H | 0 | €9.703,71 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Global Confluence puro 1H | 0 | €9.628,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Score 6 75 V1 | 0 | €9.626,87 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | 5 | €9.624,91 | €1.226,85 | €2.453,70 | €193,46 | €-31,88 |
| TEST | Scanner Top5 Btc Mfe V1 | 4 | €9.617,12 | €761,95 | €1.523,90 | €143,53 | €-52,67 |
| TEST | Scanner Top5 Btc Guard Mfe V1 | 4 | €9.581,06 | €769,53 | €1.539,07 | €144,68 | €-31,76 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 0 | €9.579,83 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H V2 | 5 | €9.546,79 | €984,94 | €2.954,81 | €191,58 | €-45,26 |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | 0 | €9.517,55 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Balanced V3 Long Only V1 | 5 | €9.516,59 | €963,67 | €2.891,00 | €144,39 | €-22,61 |
| TEST | 1H Fast V3 Long Only V1 | 5 | €9.497,03 | €990,46 | €2.971,37 | €145,34 | €-0,55 |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | 5 | €9.446,90 | €1.179,10 | €2.358,20 | €189,92 | €-44,35 |
| TEST | 1H Fast V3 Nohigh V1 | 0 | €9.435,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | 0 | €9.389,68 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom10 Short | 2 | €9.384,56 | €885,87 | €1.771,73 | €97,35 | €0,00 |
| TEST | Scanner Bottom15 Short | 2 | €9.384,56 | €885,87 | €1.771,73 | €97,35 | €0,00 |
| TEST | Scanner Bottom20 Short | 2 | €9.384,56 | €885,87 | €1.771,73 | €97,35 | €0,00 |
| TEST | Combo Trend | 4 | €9.379,28 | €954,15 | €1.908,30 | €142,10 | €-61,86 |
| TEST | Master Adaptive Runner25 V1 | 1 | €9.378,18 | €34,77 | €69,54 | €8,34 | €0,00 |
| TEST | Master Adaptive Gb20 Be V1 | 0 | €9.372,49 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | 0 | €9.370,91 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Gb20 Partial V1 | 0 | €9.362,52 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Cap75 V1 | 0 | €9.355,17 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive No Alt V1 | 0 | €9.354,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive V1 | 0 | €9.326,30 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Expanded V1 | 1 | €9.319,82 | €197,50 | €395,01 | €47,40 | €0,00 |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | 2 | €9.319,54 | €879,76 | €1.759,52 | €96,67 | €0,00 |
| TEST | Scanner Bottom5 Short Profit Lock V1 | 2 | €9.305,36 | €878,42 | €1.756,85 | €96,53 | €0,00 |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | 5 | €9.284,81 | €1.158,87 | €2.317,74 | €186,66 | €-43,59 |
| TEST | Master Adaptive Gb20 Loss Cap V1 | 1 | €9.252,08 | €195,70 | €391,41 | €45,67 | €0,00 |
| TEST | Scanner Bottom 5 Short 1H | 2 | €9.233,75 | €871,66 | €1.743,33 | €95,79 | €0,00 |
| TEST | Master Adaptive Gb20 V1 | 0 | €9.202,39 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Benchmark trend following EMA 1H | 5 | €9.160,68 | €1.703,36 | €3.406,72 | €138,80 | €-23,32 |
| TEST | Combo Adaptive Mfe Trail | 5 | €9.156,62 | €1.250,14 | €2.500,28 | €184,53 | €-82,49 |
| TEST | Scanner Top5 Btc Btc Le3 V1 | 5 | €9.154,77 | €1.166,92 | €2.333,84 | €184,01 | €-30,32 |
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
| PRINCIPALE | Principale 4H | Confluenza trend | €9.777,56 | €-191,70 | 51 | 51 | 37,25% | 0,87 | €-3,76 | 6,39% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €11.568,07 | €1.567,91 | 93 | 93 | 51,61% | 1,78 | €16,86 | 3,63% |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | Momentum / breakout | €11.320,66 | €1.355,95 | 124 | 124 | 56,45% | 1,54 | €10,94 | 4,41% |
| TEST | Donchian 1H Gb20 120R V1 | Donchian breakout 20 barre | €11.295,72 | €1.295,56 | 61 | 61 | 52,46% | 2,16 | €21,24 | 3,63% |
| TEST | Combo Trend Side Regime Guard V1 | Combo Trend | €11.177,33 | €1.242,60 | 97 | 97 | 57,73% | 1,73 | €12,81 | 4,47% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.988,46 | €1.049,82 | 126 | 126 | 50,00% | 1,41 | €8,33 | 8,85% |
| TEST | Main Side Regime Guard V1 | Confluenza trend | €10.798,34 | €792,57 | 33 | 33 | 54,55% | 2,27 | €24,02 | 2,40% |
| TEST | 1H Fast No Pepe V1 | Momentum / breakout | €10.661,87 | €715,81 | 184 | 184 | 50,54% | 1,20 | €3,89 | 6,39% |
| TEST | Combo Adaptive | Combo Adaptive | €10.565,37 | €614,62 | 137 | 137 | 45,26% | 1,27 | €4,49 | 7,91% |
| TEST | Combo Adaptive Long Only V1 | Combo Adaptive | €10.556,64 | €618,00 | 106 | 106 | 49,06% | 1,28 | €5,83 | 6,25% |
| TEST | Combo Adaptive Side Regime Guard V1 | Combo Adaptive | €10.427,47 | €497,51 | 104 | 104 | 49,04% | 1,24 | €4,78 | 8,68% |
| TEST | Scanner Top5 Btc Tp3 V1 | Scanner Top 5 + forza BTC | €10.411,45 | €471,58 | 92 | 92 | 44,57% | 1,22 | €5,13 | 11,78% |
| TEST | Scanner Top5 Btc Runner25 V1 | Scanner Top 5 + forza BTC | €10.405,35 | €465,45 | 96 | 96 | 44,79% | 1,22 | €4,85 | 12,06% |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | Momentum / breakout V3 Filtered | €10.389,26 | €391,83 | 169 | 169 | 51,48% | 1,13 | €2,32 | 9,50% |
| TEST | Rapida 1H V3 Filtered | Momentum / breakout V3 Filtered | €10.322,51 | €325,07 | 213 | 213 | 45,07% | 1,08 | €1,53 | 9,48% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €10.322,19 | €322,19 | 43 | 38 | 48,84% | 1,33 | €7,49 | 3,89% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | Momentum / breakout V3 Filtered | €10.300,05 | €300,05 | 33 | 33 | 48,48% | 2,04 | €9,09 | 2,01% |
| TEST | Ampia 4H | Confluenza trend | €10.276,40 | €333,13 | 51 | 51 | 35,29% | 1,29 | €6,53 | 4,45% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | Momentum / breakout V3 Filtered | €10.271,73 | €271,73 | 22 | 22 | 50,00% | 1,74 | €12,35 | 1,72% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €10.258,80 | €316,08 | 113 | 113 | 46,02% | 1,13 | €2,80 | 11,27% |
| TEST | 1H Fast V3 Nohigh Range Only V1 | Momentum / breakout V3 Filtered | €10.247,95 | €247,95 | 41 | 41 | 46,34% | 1,25 | €6,05 | 3,97% |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | Momentum / breakout V3 Filtered | €10.239,20 | €239,20 | 17 | 17 | 52,94% | 4,50 | €14,07 | 1,01% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | Momentum / breakout V3 Filtered | €10.235,18 | €235,18 | 20 | 20 | 50,00% | 1,90 | €11,76 | 2,73% |
| TEST | Main Dynamic Asset Selector V1 | Confluenza trend | €10.213,35 | €213,35 | 12 | 12 | 41,67% | 1,74 | €17,78 | 1,54% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €10.196,46 | €196,46 | 6 | 6 | 50,00% | 2,73 | €32,74 | 1,05% |
| TEST | Scanner Top10 Long | Scanner Top10 Long | €10.189,46 | €215,55 | 108 | 108 | 49,07% | 1,11 | €2,00 | 10,31% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | Momentum / breakout V3 Filtered | €10.185,37 | €185,37 | 22 | 22 | 40,91% | 1,57 | €8,43 | 2,27% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €10.160,35 | €164,84 | 6 | 6 | 50,00% | 2,46 | €27,47 | 1,01% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €10.156,88 | €156,88 | 12 | 12 | 50,00% | 1,63 | €13,07 | 2,77% |
| TEST | 1H Fast Score 6 75 Range Only V1 | Momentum / breakout | €10.149,62 | €149,62 | 38 | 38 | 44,74% | 1,14 | €3,94 | 3,35% |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | Momentum / breakout V3 Filtered | €10.145,12 | €145,12 | 44 | 44 | 45,45% | 1,20 | €3,30 | 2,91% |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | Momentum / breakout V3 Filtered | €10.140,84 | €140,84 | 63 | 63 | 44,44% | 1,10 | €2,24 | 5,24% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.138,40 | €138,40 | 5 | 5 | 80,00% | 3,42 | €27,68 | 0,85% |
| TEST | 1H Fast Tp2 V1 | Momentum / breakout | €10.122,74 | €129,47 | 197 | 197 | 40,10% | 1,03 | €0,66 | 6,56% |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | Momentum / breakout V3 Filtered | €10.099,04 | €99,04 | 55 | 55 | 54,55% | 1,12 | €1,80 | 3,59% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €10.083,25 | €83,25 | 6 | 6 | 66,67% | 1,77 | €13,88 | 1,13% |
| TEST | Combo Adaptive Partial 1R V1 | Combo Adaptive | €10.078,03 | €143,03 | 134 | 134 | 45,52% | 1,06 | €1,07 | 8,69% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €10.070,19 | €70,19 | 2 | 2 | 50,00% | 2,39 | €35,09 | 0,96% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €10.067,96 | €67,96 | 8 | 8 | 62,50% | 1,41 | €8,50 | 1,49% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €10.062,57 | €87,46 | 143 | 143 | 44,06% | 1,03 | €0,61 | 9,12% |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | Momentum / breakout V3 Filtered | €10.048,77 | €48,77 | 23 | 23 | 43,48% | 1,12 | €2,12 | 3,05% |
| TEST | 1H Fast V3 No Esports Long Only V1 | Momentum / breakout V3 Filtered | €10.047,37 | €66,57 | 127 | 127 | 45,67% | 1,02 | €0,52 | 10,60% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €10.046,17 | €46,17 | 9 | 9 | 55,56% | 1,19 | €5,13 | 1,89% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €10.045,08 | €45,08 | 28 | 28 | 46,43% | 1,40 | €1,61 | 0,33% |
| TEST | Rapida 1H V1 | Momentum / breakout | €10.043,28 | €43,28 | 78 | 78 | 34,62% | 1,02 | €0,55 | 6,76% |
| TEST | 1H Balanced Short Trend Down Strict V1 | Confluenza trend | €10.035,46 | €35,46 | 13 | 13 | 38,46% | 1,13 | €2,73 | 1,80% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.029,45 | €29,45 | 2 | 2 | 50,00% | 1,54 | €14,72 | 0,82% |
| TEST | Scalp RSI Long 20 · prudente · 5x | Inversione RSI estrema 15m | €10.028,67 | €28,67 | 9 | 9 | 55,56% | 1,80 | €3,19 | 0,36% |
| TEST | 1H Fast Nohigh Cap75 V1 | Momentum / breakout | €10.028,66 | €28,66 | 122 | 122 | 43,44% | 1,01 | €0,23 | 7,10% |
| TEST | Sol Ema 4H | Trend following EMA | €10.019,90 | €24,73 | 7 | 7 | 28,57% | 1,11 | €3,53 | 2,27% |
| TEST | Btc Ema 4H | Trend following EMA | €10.019,41 | €19,41 | 3 | 3 | 33,33% | 1,19 | €6,47 | 1,76% |
| TEST | Scalp RSI Short 85 · €50 · 15x | Inversione RSI estrema 15m | €10.017,98 | €17,98 | 5 | 5 | 60,00% | 1,69 | €3,60 | 0,31% |
| TEST | Scalp RSI Short 80 · €50 · 15x | Inversione RSI estrema 15m | €10.015,51 | €15,51 | 15 | 15 | 40,00% | 1,32 | €1,03 | 0,53% |
| TEST | Sol Ema 1H | Trend following EMA | €10.014,23 | €39,53 | 13 | 13 | 38,46% | 1,10 | €3,04 | 3,33% |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | Momentum / breakout V3 Filtered | €10.013,82 | €13,82 | 41 | 41 | 48,78% | 1,01 | €0,34 | 4,50% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €10.009,02 | €9,02 | 28 | 28 | 46,43% | 1,40 | €0,32 | 0,07% |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | Momentum / breakout V3 Filtered | €10.008,92 | €8,92 | 30 | 30 | 36,67% | 1,02 | €0,30 | 4,84% |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | Combo Adaptive | €10.007,52 | €40,08 | 35 | 35 | 48,57% | 1,05 | €1,15 | 4,21% |
| TEST | Scalp RSI Short 85 · €10 · 15x | Inversione RSI estrema 15m | €10.003,60 | €3,60 | 5 | 5 | 60,00% | 1,69 | €0,72 | 0,06% |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | Momentum / breakout V3 Filtered | €10.003,37 | €3,37 | 8 | 8 | 37,50% | 1,02 | €0,42 | 2,15% |
| TEST | Scalp RSI Short 80 · €10 · 15x | Inversione RSI estrema 15m | €10.003,10 | €3,10 | 15 | 15 | 40,00% | 1,32 | €0,21 | 0,11% |
| TEST | Scanner Bottom5 Short Continuation V1 | Scanner Bottom5 Short Continuation | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 20 · €10 · 15x | Inversione RSI estrema 15m | €9.999,33 | €-0,67 | 9 | 9 | 44,44% | 0,85 | €-0,07 | 0,04% |
| TEST | Scalp RSI Long 15 · €10 · 15x | Inversione RSI estrema 15m | €9.997,60 | €-2,40 | 3 | 3 | 33,33% | 0,13 | €-0,80 | 0,02% |
| TEST | Scalp RSI Long 20 · €50 · 15x | Inversione RSI estrema 15m | €9.996,64 | €-3,36 | 9 | 9 | 44,44% | 0,85 | €-0,37 | 0,21% |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | Momentum / breakout V3 Filtered | €9.995,23 | €-4,77 | 15 | 15 | 46,67% | 0,99 | €-0,32 | 2,70% |
| TEST | Scalp RSI Short 85 · prudente · 5x | Inversione RSI estrema 15m | €9.991,38 | €-8,62 | 5 | 5 | 60,00% | 0,61 | €-1,72 | 0,30% |
| TEST | Doge Ema 1H | Trend following EMA | €9.991,09 | €18,06 | 15 | 15 | 60,00% | 1,05 | €1,20 | 2,77% |
| TEST | Scalp RSI Long 25 · €10 · 15x | Inversione RSI estrema 15m | €9.990,45 | €-9,55 | 15 | 15 | 40,00% | 0,36 | €-0,64 | 0,14% |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | €9.988,00 | €-12,00 | 3 | 3 | 33,33% | 0,13 | €-4,00 | 0,12% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €9.987,48 | €-12,52 | 15 | 15 | 40,00% | 0,83 | €-0,83 | 0,71% |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | Momentum / breakout | €9.984,89 | €26,48 | 44 | 44 | 43,18% | 1,02 | €0,60 | 3,73% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €9.981,72 | €-18,28 | 3 | 3 | 33,33% | 0,83 | €-6,09 | 1,22% |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | €9.980,94 | €-19,06 | 3 | 3 | 33,33% | 0,19 | €-6,35 | 0,20% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €9.965,81 | €-34,19 | 4 | 4 | 25,00% | 0,80 | €-8,55 | 2,43% |
| TEST | Scalp RSI Short 80 · prudente · 5x | Inversione RSI estrema 15m | €9.952,43 | €-47,57 | 15 | 15 | 40,00% | 0,45 | €-3,17 | 0,89% |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | €9.952,25 | €-47,75 | 15 | 15 | 40,00% | 0,36 | €-3,18 | 0,72% |
| TEST | Btc Ema 1H | Trend following EMA | €9.941,95 | €-58,05 | 11 | 11 | 36,36% | 0,82 | €-5,28 | 1,94% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.939,62 | €-60,38 | 28 | 28 | 46,43% | 0,60 | €-2,16 | 0,84% |
| TEST | Scanner Top15 Long | Scanner Top15 Long | €9.928,57 | €-15,20 | 109 | 109 | 49,54% | 0,99 | €-0,14 | 10,31% |
| TEST | Scanner Top20 Long | Scanner Top20 Long | €9.928,57 | €-15,20 | 109 | 109 | 49,54% | 0,99 | €-0,14 | 10,31% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €9.911,95 | €-88,05 | 12 | 12 | 50,00% | 0,75 | €-7,34 | 3,08% |
| TEST | Eth Ema 4H | Trend following EMA | €9.911,28 | €-88,72 | 5 | 5 | 20,00% | 0,58 | €-17,74 | 1,83% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.897,54 | €-102,46 | 12 | 12 | 41,67% | 0,74 | €-8,54 | 3,14% |
| TEST | Combo Adaptive Quality7 Regime V1 | Combo Adaptive | €9.881,64 | €-86,21 | 35 | 35 | 42,86% | 0,90 | €-2,46 | 5,41% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.873,88 | €-126,12 | 10 | 10 | 40,00% | 0,69 | €-12,61 | 2,37% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €9.871,81 | €-103,26 | 14 | 14 | 35,71% | 0,77 | €-7,38 | 4,59% |
| TEST | 1H Fast V3 No Esports V1 | Momentum / breakout V3 Filtered | €9.866,96 | €-111,39 | 185 | 185 | 45,41% | 0,97 | €-0,60 | 9,00% |
| TEST | Eth Ema 1H | Trend following EMA | €9.844,98 | €-155,02 | 16 | 16 | 37,50% | 0,73 | €-9,69 | 4,80% |
| TEST | Combo Scanner | Combo Scanner | €9.842,46 | €-102,59 | 117 | 117 | 45,30% | 0,96 | €-0,88 | 11,38% |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | Momentum / breakout V3 Filtered | €9.837,38 | €-162,62 | 37 | 37 | 40,54% | 0,76 | €-4,40 | 3,08% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | Momentum / breakout V3 Filtered | €9.817,34 | €-182,66 | 24 | 24 | 41,67% | 0,64 | €-7,61 | 3,23% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €9.811,28 | €-148,36 | 100 | 95 | 42,00% | 0,95 | €-1,48 | 10,88% |
| TEST | Scanner Top5 Btc Guard V1 | Scanner Top 5 + forza BTC | €9.809,19 | €-157,34 | 94 | 94 | 40,43% | 0,93 | €-1,67 | 7,34% |
| TEST | Combo Adaptive Regime V1 | Combo Adaptive | €9.805,90 | €-113,96 | 49 | 49 | 46,94% | 0,91 | €-2,33 | 5,38% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.801,75 | €-198,25 | 11 | 11 | 27,27% | 0,59 | €-18,02 | 2,63% |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | Momentum / breakout | €9.779,10 | €-220,90 | 86 | 86 | 41,86% | 0,88 | €-2,57 | 7,10% |
| TEST | Combo Adaptive Quality7 V1 | Combo Adaptive | €9.776,66 | €-197,48 | 73 | 73 | 39,73% | 0,89 | €-2,71 | 8,88% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | Momentum / breakout V3 Filtered | €9.762,18 | €-237,82 | 7 | 7 | 14,29% | 0,02 | €-33,97 | 2,82% |
| TEST | 1H Balanced Long No Rhv V1 | Confluenza trend | €9.747,79 | €-232,25 | 88 | 88 | 46,59% | 0,88 | €-2,64 | 9,26% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | Momentum / breakout V3 Filtered | €9.723,72 | €-276,28 | 31 | 31 | 32,26% | 0,62 | €-8,91 | 4,83% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €9.703,71 | €-296,29 | 7 | 7 | 28,57% | 0,22 | €-42,33 | 4,16% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.628,04 | €-371,96 | 16 | 16 | 25,00% | 0,32 | €-23,25 | 3,92% |
| TEST | 1H Fast Score 6 75 V1 | Momentum / breakout | €9.626,87 | €-373,13 | 130 | 130 | 41,54% | 0,89 | €-2,87 | 10,36% |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | Scanner Top 5 + forza BTC | €9.624,91 | €-341,45 | 14 | 14 | 21,43% | 0,37 | €-24,39 | 5,41% |
| TEST | Scanner Top5 Btc Mfe V1 | Scanner Top 5 + forza BTC | €9.617,12 | €-329,18 | 105 | 105 | 44,76% | 0,85 | €-3,14 | 12,28% |
| TEST | Scanner Top5 Btc Guard Mfe V1 | Scanner Top 5 + forza BTC | €9.581,06 | €-386,25 | 111 | 111 | 41,44% | 0,85 | €-3,48 | 8,78% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | Momentum / breakout V3 Filtered | €9.579,83 | €-420,17 | 11 | 11 | 0,00% | 0,00 | €-38,20 | 4,20% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €9.546,79 | €-405,97 | 96 | 88 | 42,71% | 0,80 | €-4,23 | 8,84% |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | Momentum / breakout V3 Filtered | €9.517,55 | €-482,45 | 78 | 78 | 39,74% | 0,78 | €-6,19 | 6,59% |
| TEST | 1H Balanced V3 Long Only V1 | Confluenza trend V3 Filtered | €9.516,59 | €-458,87 | 99 | 99 | 44,44% | 0,77 | €-4,64 | 8,85% |
| TEST | 1H Fast V3 Long Only V1 | Momentum / breakout V3 Filtered | €9.497,03 | €-500,63 | 141 | 141 | 40,43% | 0,85 | €-3,55 | 12,52% |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | Scanner Top 5 + forza BTC | €9.446,90 | €-507,13 | 61 | 61 | 37,70% | 0,73 | €-8,31 | 7,99% |
| TEST | 1H Fast V3 Nohigh V1 | Momentum / breakout V3 Filtered | €9.435,38 | €-564,62 | 112 | 112 | 40,18% | 0,79 | €-5,04 | 6,91% |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | Momentum / breakout V3 Filtered | €9.389,68 | €-610,32 | 83 | 83 | 44,58% | 0,76 | €-7,35 | 7,69% |
| TEST | Scanner Bottom10 Short | Scanner Bottom10 Short | €9.384,56 | €-614,37 | 68 | 68 | 32,35% | 0,67 | €-9,03 | 8,29% |
| TEST | Scanner Bottom15 Short | Scanner Bottom15 Short | €9.384,56 | €-614,37 | 68 | 68 | 32,35% | 0,67 | €-9,03 | 8,29% |
| TEST | Scanner Bottom20 Short | Scanner Bottom20 Short | €9.384,56 | €-614,37 | 68 | 68 | 32,35% | 0,67 | €-9,03 | 8,29% |
| TEST | Combo Trend | Combo Trend | €9.379,28 | €-557,51 | 149 | 149 | 38,93% | 0,84 | €-3,74 | 10,85% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €9.378,18 | €-621,78 | 51 | 51 | 31,37% | 0,66 | €-12,19 | 8,18% |
| TEST | Master Adaptive Gb20 Be V1 | Master Adaptive Consensus | €9.372,49 | €-627,51 | 55 | 55 | 29,09% | 0,62 | €-11,41 | 8,39% |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | Momentum / breakout | €9.370,91 | €-629,09 | 88 | 88 | 43,18% | 0,78 | €-7,15 | 10,68% |
| TEST | Master Adaptive Gb20 Partial V1 | Master Adaptive Consensus | €9.362,52 | €-637,48 | 50 | 50 | 34,00% | 0,60 | €-12,75 | 7,98% |
| TEST | 1H Fast V3 Cap75 V1 | Momentum / breakout V3 Filtered | €9.355,17 | €-644,83 | 126 | 126 | 38,10% | 0,80 | €-5,12 | 11,75% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €9.354,60 | €-645,40 | 58 | 58 | 34,48% | 0,67 | €-11,13 | 7,26% |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | €9.326,30 | €-673,70 | 52 | 52 | 32,69% | 0,62 | €-12,96 | 7,80% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €9.319,82 | €-679,95 | 61 | 61 | 34,43% | 0,66 | €-11,15 | 7,96% |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | Scanner Bottom 5 Short | €9.319,54 | €-679,41 | 59 | 59 | 32,20% | 0,60 | €-11,52 | 8,31% |
| TEST | Scanner Bottom5 Short Profit Lock V1 | Scanner Bottom 5 Short | €9.305,36 | €-693,59 | 60 | 60 | 31,67% | 0,58 | €-11,56 | 8,31% |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | Scanner Top 5 + forza BTC | €9.284,81 | €-670,00 | 76 | 76 | 38,16% | 0,69 | €-8,82 | 7,27% |
| TEST | Master Adaptive Gb20 Loss Cap V1 | Master Adaptive Consensus | €9.252,08 | €-747,69 | 42 | 42 | 23,81% | 0,53 | €-17,80 | 11,41% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.233,75 | €-765,20 | 87 | 87 | 32,18% | 0,66 | €-8,80 | 9,41% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €9.202,39 | €-797,61 | 87 | 87 | 48,28% | 0,60 | €-9,17 | 9,02% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.160,68 | €-812,99 | 117 | 117 | 37,61% | 0,66 | €-6,95 | 12,31% |
| TEST | Combo Adaptive Mfe Trail | Combo Adaptive | €9.156,62 | €-759,18 | 146 | 146 | 41,78% | 0,75 | €-5,20 | 15,45% |
| TEST | Scanner Top5 Btc Btc Le3 V1 | Scanner Top 5 + forza BTC | €9.154,77 | €-813,24 | 60 | 60 | 33,33% | 0,55 | €-13,55 | 11,72% |
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
| Principale 4H | HYPE | LONG | Confluenza trend | 240m | 3,0x | 76,47929 | 77,62300 | 71,48477 | 51,36859 | 86,46833 | €10,44 | €31,32 | €2,05 | €0,47 |
| Principale 4H | TRUMP | LONG | Confluenza trend | 240m | 3,0x | 2,46049 | 2,27700 | 2,16523 | 1,65263 | 3,05101 | €134,98 | €404,95 | €48,59 | €-30,20 |
| 1H Balanced Long No Rhv V1 | SKHYNIX | LONG | Confluenza trend | 60m | 3,0x | 1214,11277 | 1214,11277 | 1170,18211 | 815,47908 | 1301,97411 | €413,43 | €1.240,28 | €44,88 | €0,00 |
| 1H Balanced Long No Rhv V1 | BOME | LONG | Confluenza trend | 60m | 3,0x | 0,00129 | 0,00129 | 0,00114 | 0,00087 | 0,00160 | €134,98 | €404,95 | €48,59 | €0,00 |
| 1H Balanced Long No Rhv V1 | TAO | LONG | Confluenza trend | 60m | 3,0x | 247,38947 | 247,38947 | 237,94346 | 166,16326 | 266,28148 | €428,20 | €1.284,61 | €49,05 | €0,00 |
| 1H Balanced Long No Rhv V1 | PEPE | LONG | Confluenza trend | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €21,51 | €64,54 | €5,62 | €-2,62 |
| 1H Balanced Long No Rhv V1 | ZEC | LONG | Confluenza trend | 60m | 3,0x | 797,24942 | 779,97000 | 743,12840 | 535,48586 | 905,49146 | €231,43 | €694,30 | €47,13 | €-15,05 |
| Bilanciata 1H V2 | SKHYNIX | LONG | Confluenza trend V2 | 60m | 3,0x | 1214,11277 | 1214,11277 | 1170,18211 | 815,47908 | 1301,97411 | €422,38 | €1.267,15 | €45,85 | €0,00 |
| Bilanciata 1H V2 | PEPE | LONG | Confluenza trend V2 | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €184,87 | €554,60 | €48,28 | €-22,54 |
| Bilanciata 1H V2 | ENA | LONG | Confluenza trend V2 | 60m | 3,0x | 0,15628 | 0,15628 | 0,14201 | 0,10497 | 0,18483 | €176,16 | €528,48 | €48,28 | €0,00 |
| Bilanciata 1H V2 | ZEC | LONG | Confluenza trend V2 | 60m | 3,0x | 798,37964 | 779,97000 | 733,89743 | 536,24499 | 927,34406 | €8,81 | €26,44 | €2,14 | €-0,61 |
| Bilanciata 1H V2 | PUMP | LONG | Confluenza trend V2 | 60m | 3,0x | 0,00494 | 0,00475 | 0,00454 | 0,00332 | 0,00575 | €192,72 | €578,15 | €47,04 | €-22,10 |
| Bilanciata 1H V3 Filtered | BEAT | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,25480 | 0,25480 | 0,25418 | 0,33846 | 0,19365 | €137,63 | €412,88 | €0,00 | €-0,00 |
| Bilanciata 1H V3 Filtered | SKHYNIX | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1220,85412 | 1220,85412 | 1177,63561 | 820,00702 | 1307,29117 | €460,42 | €1.381,27 | €48,90 | €0,00 |
| Bilanciata 1H V3 Filtered | ZEC | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 807,93155 | 779,97000 | 737,89694 | 542,66069 | 948,00078 | €195,29 | €585,88 | €50,79 | €-20,28 |
| Bilanciata 1H V3 Filtered | XRP | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1,47399 | 1,46792 | 1,35380 | 0,99003 | 1,71438 | €205,84 | €617,51 | €50,35 | €-2,54 |
| Bilanciata 1H V3 Filtered | PEPE | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €8,77 | €26,32 | €2,02 | €-0,06 |
| 1H Fast Score 6 75 Cost Aware V1 | BTW | LONG | Momentum / breakout | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €8,91 | €26,72 | €3,13 | €0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00086 | 0,00146 | €215,92 | €647,76 | €57,03 | €0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | NEAR | LONG | Momentum / breakout | 60m | 3,0x | 2,08142 | 2,08142 | 2,02315 | 1,39802 | 2,16882 | €42,86 | €128,59 | €3,60 | €0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | ZEC | LONG | Momentum / breakout | 60m | 3,0x | 807,93155 | 779,97000 | 753,46019 | 542,66069 | 889,63860 | €282,83 | €848,50 | €57,21 | €-29,37 |
| 1H Fast Score 6 75 Cost Aware V1 | XRP | LONG | Momentum / breakout | 60m | 3,0x | 1,47399 | 1,46792 | 1,38051 | 0,99003 | 1,61422 | €284,39 | €853,18 | €54,11 | €-3,52 |
| 1H Fast Score 6 75 Cost Aware V1 | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 79,06981 | 77,62300 | 76,33970 | 53,10856 | 83,16497 | €10,96 | €32,89 | €1,14 | €-0,60 |
| 1H Fast Long Btc 1 3 Cap75 V1 | XRP | LONG | Momentum / breakout | 60m | 3,0x | 1,49738 | 1,46792 | 1,40463 | 1,00574 | 1,63650 | €272,47 | €817,41 | €50,63 | €-16,08 |
| 1H Fast Long Btc 1 3 Cap75 V1 | PEPE | LONG | Momentum / breakout | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €264,23 | €792,68 | €50,63 | €1,43 |
| 1H Fast Long Btc 1 3 Cap75 V1 | DOGE | LONG | Momentum / breakout | 60m | 3,0x | 0,09162 | 0,08985 | 0,08782 | 0,06154 | 0,09732 | €406,05 | €1.218,14 | €50,55 | €-23,51 |
| 1H Fast Long Btc 1 3 Cap75 V1 | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 79,06981 | 77,62300 | 76,33970 | 53,10856 | 83,16497 | €13,51 | €40,52 | €1,40 | €-0,74 |
| 1H Fast Long Btc 1 3 Cap75 V1 | PUMP | LONG | Momentum / breakout | 60m | 3,0x | 0,00475 | 0,00475 | 0,00446 | 0,00319 | 0,00520 | €248,72 | €746,17 | €46,50 | €-0,15 |
| 1H Fast No Pepe V1 | SKHYNIX | LONG | Momentum / breakout | 60m | 3,0x | 1213,43264 | 1213,43264 | 1179,70743 | 815,02226 | 1264,02045 | €33,31 | €99,94 | €2,78 | €0,00 |
| 1H Fast No Pepe V1 | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €172,22 | €516,67 | €49,86 | €0,00 |
| 1H Fast No Pepe V1 | TAO | LONG | Momentum / breakout | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €47,93 | €143,78 | €4,27 | €0,00 |
| 1H Fast No Pepe V1 | XRP | LONG | Momentum / breakout | 60m | 3,0x | 1,49835 | 1,46792 | 1,43358 | 1,00639 | 1,59551 | €415,25 | €1.245,74 | €53,85 | €-25,30 |
| 1H Fast No Pepe V1 | ZEC | LONG | Momentum / breakout | 60m | 3,0x | 800,11999 | 779,97000 | 761,00009 | 537,41393 | 858,79985 | €346,13 | €1.038,39 | €50,77 | €-26,15 |
| 1H Fast No Pepe V1 | PUMP | LONG | Momentum / breakout | 60m | 3,0x | 0,00475 | 0,00475 | 0,00446 | 0,00319 | 0,00520 | €276,68 | €830,03 | €51,72 | €-0,17 |
| 1H Fast Tp2 V1 | BTW | LONG | Momentum / breakout | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,56752 | €142,85 | €428,56 | €50,25 | €0,00 |
| 1H Fast Tp2 V1 | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00132 | 0,00132 | 0,00119 | 0,00088 | 0,00158 | €18,87 | €56,62 | €5,59 | €0,00 |
| 1H Fast Tp2 V1 | PEPE | LONG | Momentum / breakout | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €283,85 | €851,56 | €47,41 | €-4,11 |
| 1H Fast Tp2 V1 | DOGE | LONG | Momentum / breakout | 60m | 3,0x | 0,09162 | 0,08985 | 0,08782 | 0,06154 | 0,09922 | €9,51 | €28,53 | €1,18 | €-0,55 |
| 1H Fast Tp2 V1 | ENA | LONG | Momentum / breakout | 60m | 3,0x | 0,15666 | 0,15666 | 0,14806 | 0,10522 | 0,17386 | €309,08 | €927,25 | €50,89 | €0,00 |
| 1H Fast Tp2 V1 | PUMP | LONG | Momentum / breakout | 60m | 3,0x | 0,00475 | 0,00475 | 0,00446 | 0,00319 | 0,00535 | €252,19 | €756,58 | €47,15 | €-0,15 |
| Rapida 1H V3 Filtered | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €172,00 | €515,99 | €49,79 | €0,00 |
| Rapida 1H V3 Filtered | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €589,98 | €1.769,95 | €52,56 | €0,00 |
| Rapida 1H V3 Filtered | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 79,06981 | 77,62300 | 76,33970 | 53,10856 | 83,16497 | €10,89 | €32,68 | €1,13 | €-0,60 |
| Rapida 1H V3 Filtered | ENA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,15666 | 0,15666 | 0,14806 | 0,10522 | 0,16956 | €315,08 | €945,23 | €51,87 | €0,00 |
| 1H Fast V3 Long Only V1 | BTW | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €126,57 | €379,72 | €44,52 | €0,00 |
| 1H Fast V3 Long Only V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00147 | €9,56 | €28,69 | €2,66 | €0,00 |
| 1H Fast V3 Long Only V1 | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €554,42 | €1.663,26 | €49,39 | €0,00 |
| 1H Fast V3 Long Only V1 | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 79,06981 | 77,62300 | 76,33970 | 53,10856 | 83,16497 | €10,05 | €30,14 | €1,04 | €-0,55 |
| 1H Fast V3 Long Only V1 | ENA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,15666 | 0,15666 | 0,14806 | 0,10522 | 0,16956 | €289,86 | €869,57 | €47,72 | €0,00 |
| 1H Fast V3 No Esports V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €169,36 | €508,09 | €49,03 | €0,00 |
| 1H Fast V3 No Esports V1 | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €27,04 | €81,13 | €2,41 | €0,00 |
| 1H Fast V3 No Esports V1 | PEPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €287,74 | €863,21 | €48,06 | €-4,16 |
| 1H Fast V3 No Esports V1 | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 79,06981 | 77,62300 | 76,33970 | 53,10856 | 83,16497 | €14,36 | €43,08 | €1,49 | €-0,79 |
| 1H Fast V3 No Esports V1 | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 793,19861 | 779,97000 | 752,47749 | 532,76507 | 854,28029 | €303,31 | €909,92 | €46,71 | €-15,18 |
| 1H Fast V3 No Esports Long Only V1 | BTW | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €132,94 | €398,81 | €46,76 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00147 | €10,06 | €30,18 | €2,80 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | ENA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,15628 | 0,15628 | 0,14518 | 0,10497 | 0,17294 | €9,50 | €28,50 | €2,02 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | PEPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €291,77 | €875,31 | €50,58 | €-1,09 |
| 1H Fast V3 No Esports Long Only V1 | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 79,06981 | 77,62300 | 76,33970 | 53,10856 | 83,16497 | €21,54 | €64,63 | €2,23 | €-1,18 |
| 1H Fast V3 No Esports Long Only V1 | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 793,19861 | 779,97000 | 752,47749 | 532,76507 | 854,28029 | €308,63 | €925,89 | €47,53 | €-15,44 |
| 1H Fast V3 No Esports Mfe Lock V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €173,11 | €519,32 | €50,11 | €0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €593,79 | €1.781,38 | €52,90 | €0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 79,06981 | 77,62300 | 76,33970 | 53,10856 | 83,16497 | €10,96 | €32,89 | €1,14 | €-0,60 |
| 1H Fast V3 No Esports Mfe Lock V1 | ENA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,15666 | 0,15666 | 0,14806 | 0,10522 | 0,16956 | €317,12 | €951,35 | €52,21 | €0,00 |
| Ampia 4H | SPCX | LONG | Confluenza trend | 240m | 2,0x | 136,56189 | 136,56189 | 126,46637 | 68,96375 | 164,82935 | €323,86 | €647,73 | €47,88 | €0,00 |
| Ampia 4H | VELVET | LONG | Confluenza trend | 240m | 2,0x | 0,55987 | 0,55987 | 0,49269 | 0,28274 | 0,74799 | €201,63 | €403,26 | €48,39 | €0,00 |
| Ampia 4H | LINK | LONG | Confluenza trend | 240m | 2,0x | 11,96839 | 11,96839 | 11,08055 | 6,04404 | 14,45436 | €14,07 | €28,15 | €2,09 | €0,00 |
| Ampia 4H | SUI | LONG | Confluenza trend | 240m | 2,0x | 0,86357 | 0,78920 | 0,75994 | 0,43610 | 1,15373 | €215,46 | €430,92 | €51,71 | €-37,11 |
| Ampia 4H | ETH | LONG | Confluenza trend | 240m | 2,0x | 2430,03591 | 2377,50000 | 2267,54364 | 1227,16813 | 2885,01426 | €18,82 | €37,65 | €2,52 | €-0,81 |
| Ampia 4H | HYPE | LONG | Confluenza trend | 240m | 2,0x | 79,31286 | 77,62300 | 70,73982 | 40,05299 | 103,31737 | €13,82 | €27,64 | €2,99 | €-0,59 |
| Ampia 4H | TRUMP | LONG | Confluenza trend | 240m | 2,0x | 2,37347 | 2,27700 | 2,08866 | 1,19860 | 3,17096 | €210,83 | €421,66 | €50,60 | €-17,14 |
| Forza relativa 1H V2 | BEAT | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,25984 | 0,25984 | 0,25657 | 0,38847 | 0,19125 | €200,38 | €400,75 | €0,00 | €-0,00 |
| Forza relativa 1H V2 | PEPE | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €286,19 | €572,37 | €49,83 | €-23,27 |
| Forza relativa 1H V2 | ENA | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,15628 | 0,15628 | 0,14201 | 0,07892 | 0,18769 | €272,71 | €545,42 | €49,82 | €0,00 |
| Forza relativa 1H V2 | ZEC | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 797,24942 | 779,97000 | 743,12840 | 402,61096 | 916,31566 | €360,15 | €720,31 | €48,90 | €-15,61 |
| Benchmark Donchian breakout 1H | SKHYNIX | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1174,33482 | 1174,33482 | 1128,44989 | 593,03908 | 1289,04713 | €641,25 | €1.282,50 | €50,11 | €0,00 |
| Donchian 1H Gb20 120R V1 | SKHYNIX | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1174,33482 | 1174,33482 | 1128,44989 | 593,03908 | 1289,04713 | €626,15 | €1.252,30 | €48,93 | €0,00 |
| Benchmark trend following EMA 1H | BEAT | SHORT | Trend following EMA | 60m | 2,0x | 0,28257 | 0,28257 | 0,25706 | 0,42244 | 0,20797 | €186,11 | €372,23 | €0,00 | €-0,00 |
| Benchmark trend following EMA 1H | BTC | LONG | Trend following EMA | 60m | 2,0x | 76719,31079 | 76635,11000 | 74671,22818 | 38743,25195 | 81225,09269 | €833,14 | €1.666,28 | €44,48 | €-1,83 |
| Benchmark trend following EMA 1H | SOL | LONG | Trend following EMA | 60m | 2,0x | 95,05001 | 92,83100 | 89,98943 | 48,00025 | 106,18327 | €434,46 | €868,92 | €46,26 | €-20,29 |
| Benchmark trend following EMA 1H | ZEC | LONG | Trend following EMA | 60m | 2,0x | 807,93155 | 779,97000 | 730,11531 | 408,00543 | 979,12728 | €17,42 | €34,84 | €3,36 | €-1,21 |
| Benchmark trend following EMA 1H | ENA | LONG | Trend following EMA | 60m | 2,0x | 0,14974 | 0,14974 | 0,13533 | 0,07562 | 0,18145 | €232,22 | €464,45 | €44,70 | €0,00 |
| Scanner Top 5 Long 1H | BOME | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00160 | €218,24 | €436,47 | €52,38 | €0,00 |
| Scanner Top 5 Long 1H | PEPE | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €322,02 | €644,04 | €56,06 | €-26,18 |
| Scanner Top 5 Long 1H | ENA | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,15628 | 0,15628 | 0,14201 | 0,07892 | 0,18483 | €14,91 | €29,82 | €2,72 | €0,00 |
| Scanner Top 5 Long 1H | PUMP | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,00502 | 0,00475 | 0,00460 | 0,00254 | 0,00587 | €316,31 | €632,61 | €53,01 | €-34,00 |
| Scanner Bottom 5 Short 1H | SOXL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €378,86 | €757,72 | €48,07 | €-0,00 |
| Scanner Bottom 5 Short 1H | SNDK | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €492,80 | €985,60 | €47,71 | €-0,00 |
| Scanner Top10 Long | TAO | LONG | Scanner Top10 Long | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €678,43 | €1.356,86 | €51,81 | €0,00 |
| Scanner Top10 Long | PEPE | LONG | Scanner Top10 Long | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €288,77 | €577,53 | €50,27 | €-23,48 |
| Scanner Top10 Long | ENA | LONG | Scanner Top10 Long | 60m | 2,0x | 0,14974 | 0,14974 | 0,13677 | 0,07562 | 0,17568 | €286,34 | €572,67 | €49,60 | €0,00 |
| Scanner Top10 Long | HYPE | LONG | Scanner Top10 Long | 60m | 2,0x | 79,06981 | 77,62300 | 75,55967 | 39,93025 | 86,09008 | €12,71 | €25,43 | €1,13 | €-0,47 |
| Scanner Top10 Long | PUMP | LONG | Scanner Top10 Long | 60m | 2,0x | 0,00475 | 0,00475 | 0,00437 | 0,00240 | 0,00552 | €317,96 | €635,92 | €50,95 | €-0,13 |
| Scanner Bottom10 Short | SOXL | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom10 Short | SNDK | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Top15 Long | NEAR | LONG | Scanner Top15 Long | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €16,79 | €33,59 | €1,21 | €0,00 |
| Scanner Top15 Long | TAO | LONG | Scanner Top15 Long | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €88,53 | €177,07 | €6,76 | €0,00 |
| Scanner Top15 Long | PEPE | LONG | Scanner Top15 Long | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €291,03 | €582,05 | €50,67 | €-23,66 |
| Scanner Top15 Long | ENA | LONG | Scanner Top15 Long | 60m | 2,0x | 0,15628 | 0,15628 | 0,14201 | 0,07892 | 0,18483 | €221,57 | €443,14 | €40,48 | €0,00 |
| Scanner Top15 Long | PUMP | LONG | Scanner Top15 Long | 60m | 2,0x | 0,00502 | 0,00475 | 0,00460 | 0,00254 | 0,00587 | €291,59 | €583,18 | €48,87 | €-31,34 |
| Scanner Bottom15 Short | SOXL | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom15 Short | SNDK | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Top20 Long | NEAR | LONG | Scanner Top20 Long | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €16,79 | €33,59 | €1,21 | €0,00 |
| Scanner Top20 Long | TAO | LONG | Scanner Top20 Long | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €88,53 | €177,07 | €6,76 | €0,00 |
| Scanner Top20 Long | PEPE | LONG | Scanner Top20 Long | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €291,03 | €582,05 | €50,67 | €-23,66 |
| Scanner Top20 Long | ENA | LONG | Scanner Top20 Long | 60m | 2,0x | 0,15628 | 0,15628 | 0,14201 | 0,07892 | 0,18483 | €221,57 | €443,14 | €40,48 | €0,00 |
| Scanner Top20 Long | PUMP | LONG | Scanner Top20 Long | 60m | 2,0x | 0,00502 | 0,00475 | 0,00460 | 0,00254 | 0,00587 | €291,59 | €583,18 | €48,87 | €-31,34 |
| Scanner Bottom20 Short | SOXL | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom20 Short | SNDK | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Top 5 + forza BTC 1H | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €203,45 | €406,91 | €48,83 | €0,00 |
| Scanner Top 5 + forza BTC 1H | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €300,64 | €601,28 | €52,34 | €-24,44 |
| Scanner Top 5 + forza BTC 1H | ENA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15628 | 0,15628 | 0,14201 | 0,07892 | 0,18769 | €13,39 | €26,78 | €2,45 | €0,00 |
| Scanner Top 5 + forza BTC 1H | PUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00502 | 0,00475 | 0,00460 | 0,00254 | 0,00595 | €295,30 | €590,60 | €49,49 | €-31,74 |
| Scanner Top5 Btc Mfe V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €190,73 | €381,46 | €45,77 | €0,00 |
| Scanner Top5 Btc Mfe V1 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €281,84 | €563,67 | €49,07 | €-22,91 |
| Scanner Top5 Btc Mfe V1 | ENA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15628 | 0,15628 | 0,14201 | 0,07892 | 0,18769 | €12,55 | €25,11 | €2,29 | €0,00 |
| Scanner Top5 Btc Mfe V1 | PUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00502 | 0,00475 | 0,00460 | 0,00254 | 0,00595 | €276,83 | €553,66 | €46,39 | €-29,76 |
| Scanner Top5 Btc Guard V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €197,27 | €394,55 | €47,35 | €0,00 |
| Scanner Top5 Btc Guard V1 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €34,88 | €69,75 | €6,07 | €-2,84 |
| Scanner Top5 Btc Guard V1 | ENA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,14974 | 0,14974 | 0,13677 | 0,07562 | 0,17827 | €279,61 | €559,22 | €48,44 | €0,00 |
| Scanner Top5 Btc Guard V1 | PUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00502 | 0,00475 | 0,00460 | 0,00254 | 0,00595 | €276,09 | €552,19 | €46,27 | €-29,68 |
| Scanner Top5 Btc Btc Le3 V1 | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 798,37964 | 779,97000 | 733,89743 | 403,18172 | 940,24050 | €285,92 | €571,84 | €46,19 | €-13,19 |
| Scanner Top5 Btc Btc Le3 V1 | ENA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15504 | 0,15504 | 0,14187 | 0,07830 | 0,18401 | €271,85 | €543,69 | €46,18 | €0,00 |
| Scanner Top5 Btc Btc Le3 V1 | XRP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,50701 | 1,46792 | 1,39078 | 0,76104 | 1,76273 | €297,64 | €595,28 | €45,91 | €-15,44 |
| Scanner Top5 Btc Btc Le3 V1 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €298,93 | €597,86 | €44,42 | €-0,75 |
| Scanner Top5 Btc Btc Le3 V1 | DOGE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,09338 | 0,08985 | 0,08853 | 0,04716 | 0,10406 | €12,59 | €25,17 | €1,31 | €-0,95 |
| Scanner Top5 Btc Btc 2 3 V1 | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 798,37964 | 779,97000 | 733,89743 | 403,18172 | 940,24050 | €300,60 | €601,20 | €48,56 | €-13,86 |
| Scanner Top5 Btc Btc 2 3 V1 | ENA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15504 | 0,15504 | 0,14187 | 0,07830 | 0,18401 | €285,81 | €571,61 | €48,55 | €0,00 |
| Scanner Top5 Btc Btc 2 3 V1 | XRP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,50701 | 1,46792 | 1,39078 | 0,76104 | 1,76273 | €312,93 | €625,85 | €48,27 | €-16,23 |
| Scanner Top5 Btc Btc 2 3 V1 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €314,28 | €628,56 | €46,70 | €-0,78 |
| Scanner Top5 Btc Btc 2 3 V1 | DOGE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,09338 | 0,08985 | 0,08853 | 0,04716 | 0,10406 | €13,23 | €26,47 | €1,38 | €-1,00 |
| Scanner Top5 Btc Guard Mfe V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €192,69 | €385,37 | €46,24 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €34,07 | €68,13 | €5,93 | €-2,77 |
| Scanner Top5 Btc Guard Mfe V1 | ENA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,14974 | 0,14974 | 0,13677 | 0,07562 | 0,17827 | €273,11 | €546,22 | €47,31 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | PUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00502 | 0,00475 | 0,00460 | 0,00254 | 0,00595 | €269,67 | €539,35 | €45,19 | €-28,99 |
| Scanner Top5 Btc Guard Btc Le3 V1 | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 798,37964 | 779,97000 | 733,89743 | 403,18172 | 940,24050 | €297,01 | €594,01 | €47,98 | €-13,70 |
| Scanner Top5 Btc Guard Btc Le3 V1 | ENA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15504 | 0,15504 | 0,14187 | 0,07830 | 0,18401 | €282,39 | €564,77 | €47,97 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €313,56 | €627,12 | €46,59 | €-0,78 |
| Scanner Top5 Btc Guard Btc Le3 V1 | XRP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,49793 | 1,46792 | 1,40541 | 0,75645 | 1,70147 | €13,15 | €26,30 | €1,62 | €-0,53 |
| Scanner Top5 Btc Guard Btc Le3 V1 | PUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00502 | 0,00475 | 0,00460 | 0,00254 | 0,00595 | €273,00 | €546,00 | €45,75 | €-29,34 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 798,37964 | 779,97000 | 733,89743 | 403,18172 | 940,24050 | €291,91 | €583,82 | €47,15 | €-13,46 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | ENA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15504 | 0,15504 | 0,14187 | 0,07830 | 0,18401 | €277,54 | €555,08 | €47,15 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €308,18 | €616,36 | €45,79 | €-0,77 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | XRP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,49793 | 1,46792 | 1,40541 | 0,75645 | 1,70147 | €12,92 | €25,84 | €1,60 | €-0,52 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | PUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00502 | 0,00475 | 0,00460 | 0,00254 | 0,00595 | €268,32 | €536,63 | €44,97 | €-28,84 |
| Scanner Top5 Btc Runner25 V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00176 | €210,95 | €421,90 | €50,63 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 818,21361 | 779,97000 | 764,43439 | 413,19787 | 979,55127 | €17,50 | €35,00 | €2,30 | €-1,64 |
| Scanner Top5 Btc Runner25 V1 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00001 | €303,79 | €607,58 | €52,89 | €-24,70 |
| Scanner Top5 Btc Runner25 V1 | ENA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15628 | 0,15628 | 0,14201 | 0,07892 | 0,19911 | €289,22 | €578,44 | €52,84 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | PUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00502 | 0,00475 | 0,00460 | 0,00254 | 0,00629 | €300,08 | €600,16 | €50,29 | €-32,25 |
| Scanner Top5 Btc Tp3 V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00176 | €211,07 | €422,14 | €50,66 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 818,21361 | 779,97000 | 764,43439 | 413,19787 | 979,55127 | €17,51 | €35,02 | €2,30 | €-1,64 |
| Scanner Top5 Btc Tp3 V1 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00001 | €303,97 | €607,94 | €52,92 | €-24,71 |
| Scanner Top5 Btc Tp3 V1 | ENA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15628 | 0,15628 | 0,14201 | 0,07892 | 0,19911 | €289,39 | €578,78 | €52,87 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | PUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00502 | 0,00475 | 0,00460 | 0,00254 | 0,00629 | €300,25 | €600,51 | €50,32 | €-32,27 |
| Combo Trend | BEAT | SHORT | Combo Trend | 60m | 2,0x | 0,25984 | 0,25984 | 0,25657 | 0,38847 | 0,19125 | €193,71 | €387,42 | €0,00 | €-0,00 |
| Combo Trend | ZEC | LONG | Combo Trend | 60m | 2,0x | 807,93155 | 779,97000 | 730,11531 | 408,00543 | 979,12728 | €247,61 | €495,23 | €47,70 | €-17,14 |
| Combo Trend | PEPE | LONG | Combo Trend | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00001 | €246,56 | €493,12 | €47,70 | €-20,04 |
| Combo Trend | PUMP | LONG | Combo Trend | 60m | 2,0x | 0,00498 | 0,00475 | 0,00455 | 0,00252 | 0,00595 | €266,27 | €532,54 | €46,71 | €-24,68 |
| Combo Scanner | BOME | LONG | Combo Scanner | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €195,20 | €390,40 | €46,85 | €0,00 |
| Combo Scanner | PEPE | LONG | Combo Scanner | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €288,44 | €576,88 | €50,22 | €-23,45 |
| Combo Scanner | ENA | LONG | Combo Scanner | 60m | 2,0x | 0,15628 | 0,15628 | 0,14201 | 0,07892 | 0,18769 | €12,85 | €25,70 | €2,35 | €0,00 |
| Combo Scanner | PUMP | LONG | Combo Scanner | 60m | 2,0x | 0,00502 | 0,00475 | 0,00460 | 0,00254 | 0,00595 | €283,32 | €566,63 | €47,48 | €-30,45 |
| Combo Adaptive | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,01735 | 121,01735 | 128,90956 | 180,92093 | 105,23292 | €367,30 | €734,61 | €47,91 | €-0,00 |
| Combo Adaptive | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €40,89 | €81,77 | €3,12 | €0,00 |
| Combo Adaptive | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 807,93155 | 779,97000 | 737,89694 | 408,00543 | 948,00078 | €307,94 | €615,88 | €53,39 | €-21,31 |
| Combo Adaptive | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €306,63 | €613,26 | €53,38 | €-24,93 |
| Combo Adaptive | ENA | LONG | Combo Adaptive | 60m | 2,0x | 0,14974 | 0,14974 | 0,13677 | 0,07562 | 0,17568 | €296,65 | €593,29 | €51,39 | €0,00 |
| Combo Adaptive | SOL | LONG | Combo Adaptive | 60m | 2,0x | 94,35487 | 92,83100 | 91,03919 | 47,64921 | 100,98622 | €14,11 | €28,23 | €0,99 | €-0,46 |
| Combo Adaptive | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 79,00580 | 77,62300 | 75,88394 | 39,89793 | 85,24952 | €19,27 | €38,55 | €1,52 | €-0,67 |
| Combo Adaptive Mfe Trail | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €54,29 | €108,58 | €4,15 | €0,00 |
| Combo Adaptive Mfe Trail | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 807,93155 | 779,97000 | 737,89694 | 408,00543 | 948,00078 | €270,67 | €541,33 | €46,92 | €-18,73 |
| Combo Adaptive Mfe Trail | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €269,51 | €539,03 | €46,92 | €-21,91 |
| Combo Adaptive Mfe Trail | PUMP | LONG | Combo Adaptive | 60m | 2,0x | 0,00498 | 0,00475 | 0,00459 | 0,00252 | 0,00577 | €292,23 | €584,46 | €46,13 | €-27,08 |
| Combo Adaptive Mfe Trail | XRP | LONG | Combo Adaptive | 60m | 2,0x | 1,49835 | 1,46792 | 1,41507 | 0,75667 | 1,66491 | €363,44 | €726,87 | €40,40 | €-14,76 |
| Combo Adaptive Quality7 V1 | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €371,68 | €743,36 | €47,16 | €-0,00 |
| Combo Adaptive Quality7 V1 | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €646,78 | €1.293,57 | €49,39 | €0,00 |
| Combo Adaptive Quality7 V1 | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €283,16 | €566,31 | €49,30 | €-23,02 |
| Combo Adaptive Quality7 V1 | ENA | LONG | Combo Adaptive | 60m | 2,0x | 0,15012 | 0,15012 | 0,13738 | 0,07581 | 0,17561 | €281,13 | €562,25 | €47,73 | €0,00 |
| Combo Adaptive Quality7 V1 | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 797,24942 | 779,97000 | 743,12840 | 402,61096 | 905,49146 | €18,54 | €37,09 | €2,52 | €-0,80 |
| Combo Adaptive Regime V1 | PUMP | LONG | Combo Adaptive | 60m | 2,0x | 0,00502 | 0,00475 | 0,00460 | 0,00254 | 0,00587 | €294,95 | €589,90 | €49,43 | €-31,70 |
| Combo Adaptive Regime V1 | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 793,19861 | 779,97000 | 740,84288 | 400,56530 | 897,91007 | €374,42 | €748,84 | €49,43 | €-12,49 |
| Combo Adaptive Regime V1 | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 79,00580 | 77,62300 | 75,88394 | 39,89793 | 85,24952 | €625,40 | €1.250,81 | €49,42 | €-21,89 |
| Combo Adaptive Regime V1 | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €425,38 | €850,76 | €48,95 | €-12,00 |
| Combo Adaptive Quality7 Regime V1 | PUMP | LONG | Combo Adaptive | 60m | 2,0x | 0,00502 | 0,00475 | 0,00460 | 0,00254 | 0,00587 | €295,78 | €591,56 | €49,57 | €-31,79 |
| Combo Adaptive Long Only V1 | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €645,48 | €1.290,95 | €46,47 | €0,00 |
| Combo Adaptive Long Only V1 | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €308,39 | €616,77 | €53,69 | €-25,07 |
| Combo Adaptive Long Only V1 | ENA | LONG | Combo Adaptive | 60m | 2,0x | 0,14974 | 0,14974 | 0,13677 | 0,07562 | 0,17568 | €298,14 | €596,28 | €51,65 | €0,00 |
| Combo Adaptive Long Only V1 | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 79,31286 | 77,62300 | 76,03495 | 40,05299 | 85,86867 | €15,39 | €30,77 | €1,27 | €-0,66 |
| Combo Adaptive Long Only V1 | PUMP | LONG | Combo Adaptive | 60m | 2,0x | 0,00502 | 0,00475 | 0,00460 | 0,00254 | 0,00587 | €312,68 | €625,36 | €52,40 | €-33,61 |
| Combo Adaptive Partial 1R V1 | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,01735 | 121,01735 | 128,90956 | 180,92093 | 105,23292 | €352,70 | €705,40 | €46,00 | €-0,00 |
| Combo Adaptive Partial 1R V1 | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 818,21361 | 779,97000 | 764,43439 | 413,19787 | 925,77205 | €390,17 | €780,34 | €51,29 | €-36,47 |
| Combo Adaptive Partial 1R V1 | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €292,79 | €585,58 | €50,97 | €-23,80 |
| Combo Adaptive Partial 1R V1 | ENA | LONG | Combo Adaptive | 60m | 2,0x | 0,14974 | 0,14974 | 0,13677 | 0,07562 | 0,17568 | €282,57 | €565,13 | €48,95 | €0,00 |
| Combo Adaptive Partial 1R V1 | SOL | LONG | Combo Adaptive | 60m | 2,0x | 94,24985 | 92,83100 | 90,79388 | 47,59617 | 101,16178 | €12,54 | €25,08 | €0,92 | €-0,38 |
| Combo Adaptive Partial 1R V1 | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 79,31286 | 77,62300 | 76,03495 | 40,05299 | 85,86867 | €13,50 | €27,00 | €1,12 | €-0,58 |
| Combo Adaptive Partial 1R V1 | PUMP | LONG | Combo Adaptive | 60m | 2,0x | 0,00502 | 0,00475 | 0,00460 | 0,00254 | 0,00587 | €16,58 | €33,16 | €2,78 | €-1,78 |
| Combo Adaptive Quality7 Regime Partial 1R V1 | PUMP | LONG | Combo Adaptive | 60m | 2,0x | 0,00502 | 0,00475 | 0,00460 | 0,00254 | 0,00587 | €299,55 | €599,09 | €50,20 | €-32,20 |
| Sol Ema 1H | SOL | LONG | Trend following EMA | 60m | 3,0x | 95,05001 | 92,83100 | 90,49549 | 63,84192 | 104,15904 | €349,20 | €1.047,59 | €50,20 | €-24,46 |
| Sol Ema 4H | SOL | LONG | Trend following EMA | 240m | 2,0x | 93,39968 | 92,83100 | 86,82624 | 47,16684 | 109,83325 | €356,10 | €712,19 | €50,12 | €-4,34 |
| Sol Adaptive 1H | SOL | LONG | Combo Adaptive | 60m | 3,0x | 95,05001 | 92,83100 | 90,49549 | 63,84192 | 104,15904 | €344,23 | €1.032,69 | €49,48 | €-24,11 |
| Sol Adaptive 4H | SOL | LONG | Combo Adaptive | 240m | 2,0x | 93,39968 | 92,83100 | 86,22866 | 47,16684 | 111,32722 | €330,98 | €661,97 | €50,82 | €-4,03 |
| Doge Ema 1H | DOGE | LONG | Trend following EMA | 60m | 3,0x | 0,09314 | 0,08985 | 0,08689 | 0,06256 | 0,10563 | €248,90 | €746,70 | €50,09 | €-26,37 |
| Master Adaptive Expanded V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03814 | 0,02188 | 0,05374 | €197,50 | €395,01 | €47,40 | €0,00 |
| Master Adaptive Runner25 V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03814 | 0,02188 | 0,05894 | €34,77 | €69,54 | €8,34 | €0,00 |
| Combo Adaptive Side Regime Guard V1 | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €77,52 | €155,04 | €5,58 | €0,00 |
| Combo Adaptive Side Regime Guard V1 | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 807,93155 | 779,97000 | 737,89694 | 408,00543 | 948,00078 | €305,89 | €611,78 | €53,03 | €-21,17 |
| Combo Adaptive Side Regime Guard V1 | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €304,59 | €609,17 | €53,03 | €-24,76 |
| Combo Adaptive Side Regime Guard V1 | ENA | LONG | Combo Adaptive | 60m | 2,0x | 0,14974 | 0,14974 | 0,13677 | 0,07562 | 0,17568 | €290,21 | €580,42 | €50,28 | €0,00 |
| Combo Adaptive Side Regime Guard V1 | SOL | LONG | Combo Adaptive | 60m | 2,0x | 94,24985 | 92,83100 | 90,79388 | 47,59617 | 101,16178 | €14,20 | €28,40 | €1,04 | €-0,43 |
| Combo Adaptive Side Regime Guard V1 | PUMP | LONG | Combo Adaptive | 60m | 2,0x | 0,00494 | 0,00475 | 0,00454 | 0,00250 | 0,00575 | €286,36 | €572,72 | €46,60 | €-21,90 |
| Master Adaptive Gb20 Loss Cap V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03828 | 0,02188 | 0,05682 | €195,70 | €391,41 | €45,67 | €0,00 |
| Main Side Regime Guard V1 | VELVET | LONG | Confluenza trend | 240m | 3,0x | 0,55987 | 0,55987 | 0,49269 | 0,37605 | 0,69424 | €142,25 | €426,74 | €51,21 | €0,00 |
| Main Side Regime Guard V1 | AKE | LONG | Confluenza trend | 240m | 3,0x | 0,01021 | 0,01021 | 0,00899 | 0,00686 | 0,01266 | €145,97 | €437,90 | €52,55 | €0,00 |
| Main Side Regime Guard V1 | PUMP | LONG | Confluenza trend | 240m | 3,0x | 0,00468 | 0,00475 | 0,00411 | 0,00314 | 0,00580 | €149,89 | €449,66 | €53,96 | €7,51 |
| Main Side Regime Guard V1 | HYPE | LONG | Confluenza trend | 240m | 3,0x | 77,65853 | 77,62300 | 71,20755 | 52,16065 | 90,56048 | €216,52 | €649,56 | €53,96 | €-0,30 |
| Main Side Regime Guard V1 | XRP | LONG | Confluenza trend | 240m | 3,0x | 1,47102 | 1,46792 | 1,31178 | 0,98804 | 1,78951 | €12,77 | €38,31 | €4,15 | €-0,08 |
| Combo Trend Side Regime Guard V1 | ZEC | LONG | Combo Trend | 60m | 2,0x | 822,67450 | 779,97000 | 761,05343 | 415,45062 | 958,24084 | €381,00 | €762,00 | €57,08 | €-39,56 |
| Combo Trend Side Regime Guard V1 | PEPE | LONG | Combo Trend | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00001 | €293,50 | €586,99 | €56,78 | €-23,86 |
| Combo Trend Side Regime Guard V1 | ENA | LONG | Combo Trend | 60m | 2,0x | 0,14974 | 0,14974 | 0,13533 | 0,07562 | 0,18145 | €280,47 | €560,95 | €53,99 | €0,00 |
| Combo Trend Side Regime Guard V1 | SOL | LONG | Combo Trend | 60m | 2,0x | 94,24985 | 92,83100 | 90,40989 | 47,59617 | 102,69776 | €13,97 | €27,94 | €1,14 | €-0,42 |
| 1H Balanced V3 Long Only V1 | BEAT | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,25480 | 0,25480 | 0,25418 | 0,33846 | 0,19365 | €130,17 | €390,52 | €0,00 | €-0,00 |
| 1H Balanced V3 Long Only V1 | SKHYNIX | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1220,85412 | 1220,85412 | 1177,63561 | 820,00702 | 1307,29117 | €435,49 | €1.306,46 | €46,25 | €0,00 |
| 1H Balanced V3 Long Only V1 | ZEC | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 807,93155 | 779,97000 | 737,89694 | 542,66069 | 948,00078 | €184,72 | €554,15 | €48,04 | €-19,18 |
| 1H Balanced V3 Long Only V1 | XRP | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1,47399 | 1,46792 | 1,35380 | 0,99003 | 1,71438 | €194,69 | €584,07 | €47,63 | €-2,41 |
| 1H Balanced V3 Long Only V1 | HYPE | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 79,06981 | 77,62300 | 75,55967 | 53,10856 | 86,09008 | €18,60 | €55,80 | €2,48 | €-1,02 |
| Scanner Bottom5 Short Profit Lock V1 | SOXL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €381,80 | €763,60 | €48,45 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | SNDK | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €496,62 | €993,25 | €48,08 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | SOXL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €382,38 | €764,76 | €48,52 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | SNDK | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €497,38 | €994,76 | €48,15 | €-0,00 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Scanner Top 5 Long 1H | ZEC | LONG | 2026-08-23T05:05:50+00:00 | 767,06210 | €-58,32 | -1,02 | STOP |
| Scanner Top5 Btc Mfe V1 | ZEC | LONG | 2026-08-23T05:05:50+00:00 | 767,06210 | €-51,20 | -1,02 | STOP |
| Scanner Top5 Btc Guard V1 | ZEC | LONG | 2026-08-23T05:05:50+00:00 | 767,06210 | €-50,27 | -1,02 | STOP |
| Scanner Top5 Btc Guard Mfe V1 | ZEC | LONG | 2026-08-23T05:05:50+00:00 | 767,06210 | €-49,10 | -1,02 | STOP |
| Scanner Top 5 + forza BTC 1H | ZEC | LONG | 2026-08-23T05:05:50+00:00 | 767,06210 | €-54,62 | -1,02 | STOP |
| Scanner Top20 Long | ZEC | LONG | 2026-08-23T05:05:50+00:00 | 767,06210 | €-53,07 | -1,02 | STOP |
| Scanner Top15 Long | ZEC | LONG | 2026-08-23T05:05:50+00:00 | 767,06210 | €-53,07 | -1,02 | STOP |
| Scanner Top10 Long | ZEC | LONG | 2026-08-23T05:05:50+00:00 | 767,06210 | €-53,81 | -1,02 | STOP |
| Eth Ema 4H | ETH | LONG | 2026-08-23T05:05:50+00:00 | 2383,39843 | €-51,46 | -1,03 | STOP |
| Combo Scanner | ZEC | LONG | 2026-08-23T05:05:50+00:00 | 767,06210 | €-52,40 | -1,02 | STOP |
| Combo Adaptive Long Only V1 | ZEC | LONG | 2026-08-23T05:05:50+00:00 | 767,06210 | €-6,74 | -1,02 | STOP |
| 1H Fast V3 No Esports V1 | SKHYNIX | LONG | 2026-08-23T05:05:50+00:00 | 1220,12161 | €-0,10 | -0,07 | TIME_EXIT_NO_CANDLES |

## Regole invarianti

- Nessuna martingala e nessuna mediazione automatica in perdita.
- Il target mensile riduce il rischio quando viene avvicinato o raggiunto; non lo aumenta mai.
- Il portafoglio principale e le simulazioni di confronto hanno contabilità separata.
- Commissioni, slippage e funding sono inclusi nella simulazione secondo i parametri configurati.
- Quando stop e target risultano toccati nella stessa candela, prevale lo stop salvo modifica esplicita della configurazione.
