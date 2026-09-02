# Paper trading automatico KuCoin

Generato: 2026-09-02T05:33:04+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-09-02T05:05:30+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-09-02T05:05:30+00:00 | 2026-09-02T05:05:30+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-09-02T04:45:00+00:00 | 2026-09-02T04:45:00+00:00 | 5,8 min | 25,0 min | OK |
| 60m | 12 | 2026-09-02T04:00:00+00:00 | 2026-09-02T04:00:00+00:00 | 5,8 min | 45,0 min | OK |
| 240m | 12 | 2026-09-02T00:00:00+00:00 | 2026-09-02T00:00:00+00:00 | 1,10 h | 1,00 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Combo Adaptive Side Regime Guard V1 | UNI | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Master Adaptive No Alt V1 | USELESS | 60m | LONG | 7,75 | 0,00 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top20 Long | USELESS | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top15 Long | USELESS | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Forza relativa 1H V2 | USELESS | 60m | LONG | 7,75 | 5,50 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Forza relativa 1H V1 | USELESS | 60m | LONG | 7,75 | 4,00 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Principale 4H | DOGE | 240m | SHORT | -5,58 | 6,00 | 0,42 | STALE_CANDLE | 1,10 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.8 minuti; tolleranza 60 minuti. |
| Principale 4H | ZEC | 240m | LONG | 5,50 | 6,00 | 0,50 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.8 minuti; tolleranza 60 minuti. |
| Principale 4H | SUI | 240m | SHORT | -4,74 | 6,00 | 1,26 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.8 minuti; tolleranza 60 minuti. |
| Principale 4H | HYPE | 240m | LONG | 4,46 | 6,00 | 1,54 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.8 minuti; tolleranza 60 minuti. |
| Principale 4H | XRP | 240m | SHORT | -2,33 | 6,00 | 3,67 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.8 minuti; tolleranza 60 minuti. |
| Principale 4H | PEPE | 240m | SHORT | -2,31 | 6,00 | 3,69 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.8 minuti; tolleranza 60 minuti. |
| Principale 4H | BTR | 240m | SHORT | -1,06 | 6,00 | 4,94 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.8 minuti; tolleranza 60 minuti. |
| Principale 4H | BTC | 240m | SHORT | -1,00 | 6,00 | 5,00 | STALE_CANDLE | 1,10 h | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.8 minuti; tolleranza 60 minuti. |
| Principale 4H | SOL | 240m | SHORT | -0,87 | 6,00 | 5,13 | STALE_CANDLE | 1,10 h | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.8 minuti; tolleranza 60 minuti. |
| Principale 4H | ETH | 240m | SHORT | -0,19 | 6,00 | 5,81 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.8 minuti; tolleranza 60 minuti. |
| Bilanciata 1H V1 | UNI | 60m | LONG | 7,75 | 5,00 | 0,00 | READY | 5,8 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Balanced Long No Rhv V1 | UNI | 60m | LONG | 7,75 | 5,00 | 0,00 | READY | 5,8 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Fast No Pepe V1 | UNI | 60m | LONG | 7,75 | 4,50 | 0,00 | READY | 5,8 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Fast Tp2 V1 | UNI | 60m | LONG | 7,75 | 4,50 | 0,00 | READY | 5,8 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Rapida 1H V3 Filtered | UNI | 60m | LONG | 7,75 | 4,50 | 0,00 | READY | 5,8 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Fast V3 Nohigh V1 | UNI | 60m | LONG | 7,75 | 4,50 | 0,00 | READY | 5,8 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Fast V3 No Esports V1 | UNI | 60m | LONG | 7,75 | 4,50 | 0,00 | READY | 5,8 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Fast V3 No Esports Mfe Lock V1 | UNI | 60m | LONG | 7,75 | 4,50 | 0,00 | READY | 5,8 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Benchmark Donchian breakout 1H | UNI | 60m | LONG | 7,75 | 5,00 | 0,00 | READY | 5,8 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Donchian 1H Gb20 120R V1 | UNI | 60m | LONG | 7,75 | 5,00 | 0,00 | READY | 5,8 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.811,21 | -1,89% | €2,65 | €3.000,00 | 0,09% | 6 | 56 | 41,07% | 0,87 | 6,86% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 56 | 2690 | PRIME INDICAZIONI | 100 (mancano 44) |

- Trade del Principale 4H chiusi: **56**; win rate **41,07%**; profit factor **0,87**.
- Expectancy: **€-3,30** per trade; P&L netto: **€-184,95**; max drawdown: **6,86%**.
- Valutazione: **Si può osservare la direzione, ma il risultato resta fragile.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 6 | €9.811,21 | €701,54 | €2.104,63 | €196,25 | €-2,72 |
| TEST | Benchmark Donchian breakout 1H | 6 | €11.231,18 | €4.071,45 | €8.142,91 | €225,68 | €5,43 |
| TEST | Donchian 1H Gb20 120R V1 | 6 | €10.966,75 | €3.975,60 | €7.951,19 | €220,37 | €5,30 |
| TEST | Main Side Regime Guard V1 | 6 | €10.964,56 | €751,96 | €2.255,89 | €218,34 | €-21,17 |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | 6 | €10.914,47 | €1.083,77 | €3.251,31 | €218,28 | €5,76 |
| TEST | Scanner Top 5 Long 1H | 6 | €10.852,64 | €1.133,45 | €2.266,91 | €217,07 | €0,00 |
| TEST | Combo Trend Side Regime Guard V1 | 6 | €10.788,53 | €2.851,37 | €5.702,75 | €111,46 | €40,76 |
| TEST | 1H Fast No Pepe V1 | 7 | €10.575,84 | €1.337,57 | €4.012,72 | €211,52 | €0,00 |
| TEST | Combo Adaptive Long Only V1 | 5 | €10.455,92 | €2.279,33 | €4.558,66 | €207,30 | €0,00 |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | 3 | €10.374,80 | €2.424,70 | €7.274,09 | €154,26 | €-3,20 |
| TEST | Rapida 1H V2 | 1 | €10.363,82 | €749,31 | €2.247,94 | €51,80 | €0,00 |
| TEST | Sol Donchian 1H | 1 | €10.331,04 | €1.019,77 | €3.059,30 | €51,67 | €-0,43 |
| TEST | Ampia 4H | 8 | €10.307,55 | €1.071,19 | €2.142,37 | €207,40 | €27,62 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 0 | €10.300,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | 5 | €10.282,66 | €2.160,68 | €6.482,05 | €205,36 | €-13,91 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 0 | €10.271,73 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | 5 | €10.246,90 | €1.220,23 | €3.660,70 | €204,95 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 0 | €10.239,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 0 | €10.235,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive | 7 | €10.226,17 | €945,51 | €1.891,02 | €155,75 | €4,59 |
| TEST | Btc Bollinger 1H | 0 | €10.209,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Nohigh Range Only V1 | 3 | €10.204,53 | €1.564,63 | €4.693,88 | €153,18 | €0,00 |
| TEST | Scanner Top5 Btc Tp3 V1 | 5 | €10.198,94 | €1.803,17 | €3.606,35 | €201,46 | €4,88 |
| TEST | Scanner Top5 Btc Runner25 V1 | 5 | €10.192,97 | €1.802,12 | €3.604,24 | €201,34 | €4,88 |
| TEST | Sol Adaptive 4H | 0 | €10.191,22 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 0 | €10.185,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V3 Filtered | 5 | €10.181,06 | €1.212,39 | €3.637,18 | €203,63 | €0,00 |
| TEST | Sol Donchian 4H | 1 | €10.159,24 | €449,62 | €899,24 | €50,98 | €-37,14 |
| TEST | Scanner Top 5 + forza BTC 1H | 6 | €10.154,80 | €1.063,56 | €2.127,11 | €203,11 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 0 | €10.145,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 1H | 1 | €10.121,32 | €888,04 | €2.664,11 | €50,62 | €-0,37 |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 0 | €10.099,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top10 Long | 5 | €10.087,45 | €2.258,24 | €4.516,48 | €200,07 | €0,00 |
| TEST | 1H Fast Score 6 75 Range Only V1 | 4 | €10.087,09 | €1.750,21 | €5.250,64 | €201,76 | €0,00 |
| TEST | Btc Bollinger 4H | 1 | €10.085,97 | €775,58 | €1.551,16 | €0,00 | €55,60 |
| TEST | Combo Adaptive Partial 1R V1 | 5 | €10.062,88 | €1.942,68 | €3.885,36 | €151,43 | €-1,87 |
| TEST | Doge Bollinger 1H | 1 | €10.058,84 | €1.204,04 | €3.612,13 | €0,00 | €39,96 |
| TEST | Main Dynamic Asset Selector V1 | 1 | €10.057,70 | €140,98 | €422,93 | €50,75 | €0,00 |
| TEST | Sol Ema 4H | 0 | €10.057,68 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Ema 1H | 0 | €10.057,57 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 0 | €10.048,77 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €10.045,08 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V1 | 0 | €10.043,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Balanced Short Trend Down Strict V1 | 0 | €10.035,46 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · prudente · 5x | 0 | €10.032,32 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Donchian 1H | 0 | €10.025,86 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €50 · 15x | 0 | €10.017,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 4H | 0 | €10.017,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €50 · 15x | 0 | €10.009,44 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 0 | €10.009,02 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 0 | €10.008,92 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €10 · 15x | 0 | €10.003,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 0 | €10.003,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €10 · 15x | 0 | €10.001,89 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 1H | 1 | €10.001,13 | €877,49 | €2.632,47 | €50,02 | €-0,37 |
| TEST | Scanner Bottom5 Short Continuation V1 | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €10 · 15x | 0 | €9.998,68 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €10 · 15x | 0 | €9.997,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 4H | 1 | €9.996,52 | €478,97 | €957,94 | €0,00 | €66,93 |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 0 | €9.995,23 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 No Esports Long Only V1 | 6 | €9.993,99 | €533,18 | €1.599,53 | €151,13 | €0,00 |
| TEST | Scalp RSI Long 20 · €50 · 15x | 0 | €9.993,42 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · prudente · 5x | 0 | €9.991,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €10 · 15x | 0 | €9.989,27 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €50 · 15x | 0 | €9.988,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top15 Long | 8 | €9.982,95 | €1.807,23 | €3.614,46 | €198,57 | €-0,11 |
| TEST | Scanner Top20 Long | 8 | €9.982,95 | €1.807,23 | €3.614,46 | €198,57 | €-0,11 |
| TEST | Scalp RSI Long 15 · prudente · 5x | 0 | €9.980,94 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 0 | €9.974,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Tp2 V1 | 5 | €9.968,62 | €720,81 | €2.162,44 | €149,09 | €0,00 |
| TEST | Btc Adaptive 1H | 0 | €9.968,58 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Side Regime Guard V1 | 5 | €9.967,91 | €1.319,98 | €2.639,95 | €147,39 | €3,54 |
| TEST | Btc Ema 4H | 0 | €9.966,88 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €50 · 15x | 0 | €9.946,36 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.939,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · prudente · 5x | 0 | €9.939,55 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 4H | 0 | €9.913,56 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Nohigh Cap75 V1 | 4 | €9.902,55 | €1.338,71 | €4.016,13 | €198,07 | €0,00 |
| TEST | Forza relativa 1H V2 | 7 | €9.893,74 | €925,48 | €1.850,95 | €149,79 | €-0,11 |
| TEST | Btc Donchian 1H | 1 | €9.888,28 | €1.289,36 | €3.868,07 | €49,51 | €-11,89 |
| TEST | Eth Ema 4H | 0 | €9.887,30 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Nohigh V1 | 6 | €9.862,15 | €1.217,21 | €3.651,63 | €197,24 | €0,00 |
| TEST | Eth Adaptive 1H | 0 | €9.857,66 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 1H | 1 | €9.857,56 | €1.037,93 | €3.113,80 | €49,30 | €-0,81 |
| TEST | Combo Scanner | 6 | €9.851,19 | €1.484,97 | €2.969,93 | €195,27 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 0 | €9.837,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 0 | €9.817,34 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Long Only V1 | 5 | €9.779,77 | €880,89 | €2.642,66 | €147,40 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 0 | €9.762,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Global Confluence puro 1H | 1 | €9.758,55 | €1.363,98 | €2.727,96 | €48,77 | €6,71 |
| TEST | Eth Donchian 1H | 0 | €9.747,26 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Ema 1H | 1 | €9.734,61 | €1.098,91 | €3.296,73 | €48,65 | €5,80 |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | 0 | €9.726,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 0 | €9.723,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | 4 | €9.656,13 | €1.305,40 | €3.916,19 | €193,14 | €0,00 |
| TEST | 1H Balanced Long No Rhv V1 | 5 | €9.653,19 | €1.124,13 | €3.372,38 | €193,06 | €0,00 |
| TEST | Eth Bollinger 1H | 0 | €9.649,49 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Quality7 Regime V1 | 0 | €9.603,78 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 0 | €9.579,83 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | 2 | €9.561,10 | €791,57 | €2.374,70 | €95,73 | €0,00 |
| TEST | Btc Ema 1H | 1 | €9.559,39 | €1.107,32 | €3.321,96 | €47,84 | €-6,05 |
| TEST | Bilanciata 1H V3 Filtered | 4 | €9.544,80 | €2.270,08 | €6.810,24 | €191,30 | €-42,85 |
| TEST | Combo Adaptive Regime V1 | 1 | €9.541,28 | €987,06 | €1.974,12 | €49,09 | €0,00 |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | 4 | €9.532,59 | €886,36 | €2.659,08 | €190,86 | €-15,23 |
| TEST | Scanner Top5 Btc Mfe V1 | 6 | €9.519,63 | €997,03 | €1.994,07 | €190,41 | €0,00 |
| TEST | Combo Adaptive Quality7 V1 | 4 | €9.514,37 | €1.438,51 | €2.877,02 | €190,29 | €0,00 |
| TEST | Scanner Top5 Btc Guard V1 | 5 | €9.491,50 | €1.103,75 | €2.207,51 | €189,83 | €0,00 |
| TEST | 1H Fast V3 No Esports V1 | 5 | €9.412,84 | €734,78 | €2.204,35 | €188,27 | €0,00 |
| TEST | Master Adaptive Gb20 Be V1 | 5 | €9.375,37 | €1.356,06 | €2.712,12 | €187,71 | €0,00 |
| TEST | Master Adaptive Expanded V1 | 4 | €9.370,06 | €1.563,30 | €3.126,60 | €186,75 | €0,00 |
| TEST | Master Adaptive Gb20 Partial V1 | 5 | €9.365,40 | €1.354,62 | €2.709,24 | €187,51 | €0,00 |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | 4 | €9.337,78 | €868,43 | €2.605,28 | €186,96 | €-14,99 |
| TEST | Master Adaptive V1 | 5 | €9.329,18 | €1.349,38 | €2.698,76 | €186,79 | €0,00 |
| TEST | Scanner Bottom10 Short | 4 | €9.320,74 | €1.261,36 | €2.522,73 | €140,86 | €0,00 |
| TEST | Scanner Bottom15 Short | 4 | €9.320,74 | €1.261,36 | €2.522,73 | €140,86 | €0,00 |
| TEST | Scanner Bottom20 Short | 4 | €9.320,74 | €1.261,36 | €2.522,73 | €140,86 | €0,00 |
| TEST | Scanner Top5 Btc Guard Mfe V1 | 5 | €9.270,76 | €1.078,08 | €2.156,17 | €185,42 | €0,00 |
| TEST | 1H Fast Score 6 75 V1 | 4 | €9.258,29 | €1.466,40 | €4.399,21 | €138,42 | €10,17 |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | 4 | €9.256,15 | €1.252,64 | €2.505,29 | €139,88 | €0,00 |
| TEST | Scanner Bottom5 Short Profit Lock V1 | 4 | €9.242,07 | €1.250,74 | €2.501,48 | €139,67 | €0,00 |
| TEST | Master Adaptive Runner25 V1 | 6 | €9.223,03 | €1.288,13 | €2.576,26 | €184,63 | €0,00 |
| TEST | Bilanciata 1H V2 | 5 | €9.206,59 | €955,13 | €2.865,38 | €140,57 | €-0,50 |
| TEST | Master Adaptive Gb20 V1 | 5 | €9.206,07 | €1.331,51 | €2.663,01 | €184,32 | €0,00 |
| TEST | Benchmark trend following EMA 1H | 6 | €9.176,14 | €616,44 | €1.232,88 | €96,72 | €-1,41 |
| TEST | Scanner Bottom 5 Short 1H | 4 | €9.170,95 | €1.241,11 | €2.482,23 | €138,60 | €0,00 |
| TEST | Master Adaptive Gb20 Loss Cap V1 | 6 | €9.157,30 | €1.263,51 | €2.527,01 | €183,20 | €0,00 |
| TEST | Master Adaptive No Alt V1 | 6 | €9.145,75 | €1.384,13 | €2.768,25 | €182,92 | €-0,10 |
| TEST | Combo Trend | 6 | €9.102,45 | €1.651,93 | €3.303,86 | €90,54 | €-17,36 |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | 5 | €9.102,17 | €1.091,72 | €2.183,43 | €182,04 | €0,00 |
| TEST | Combo Adaptive Mfe Trail | 7 | €9.072,43 | €804,70 | €1.609,39 | €137,16 | €-15,48 |
| TEST | 1H Balanced V3 Long Only V1 | 4 | €9.027,63 | €2.147,08 | €6.441,23 | €180,94 | €-40,53 |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | 4 | €9.012,14 | €1.427,41 | €4.282,24 | €134,74 | €9,90 |
| TEST | Bilanciata 1H V1 | 6 | €8.999,99 | €2.087,42 | €6.262,25 | €180,67 | €-8,07 |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | 2 | €8.959,01 | €1.370,15 | €2.740,30 | €91,08 | €0,00 |
| TEST | Combo Adaptive Runner25 V1 | 6 | €8.949,59 | €1.335,52 | €2.671,05 | €134,20 | €96,55 |
| TEST | 1H Fast V3 Cap75 V1 | 4 | €8.947,73 | €1.417,34 | €4.252,03 | €133,89 | €9,79 |
| TEST | Combo Mean Reversion | 4 | €8.804,50 | €5.439,63 | €10.879,27 | €131,04 | €34,43 |
| TEST | Combo Adaptive Tp3 V1 | 6 | €8.782,40 | €1.310,57 | €2.621,15 | €131,70 | €94,74 |
| TEST | Benchmark Bollinger mean reversion 1H | 2 | €8.735,32 | €2.952,41 | €5.904,81 | €43,73 | €34,05 |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | 5 | €8.728,44 | €754,09 | €1.508,19 | €131,28 | €2,68 |
| TEST | Master Adaptive Strict3 V1 | 4 | €8.704,25 | €1.184,13 | €2.368,27 | €173,50 | €0,00 |
| TEST | Scanner Top5 Btc Btc Le3 V1 | 4 | €8.612,89 | €1.990,67 | €3.981,33 | €172,29 | €0,00 |
| TEST | Forza relativa 1H V1 | 6 | €8.397,21 | €1.959,17 | €3.918,34 | €167,95 | €4,19 |

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
| PRINCIPALE | Principale 4H | Confluenza trend | €9.811,21 | €-184,95 | 56 | 56 | 41,07% | 0,87 | €-3,30 | 6,86% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €11.231,18 | €1.229,80 | 121 | 121 | 45,45% | 1,45 | €10,16 | 6,75% |
| TEST | Donchian 1H Gb20 120R V1 | Donchian breakout 20 barre | €10.966,75 | €965,41 | 89 | 89 | 43,82% | 1,53 | €10,85 | 6,75% |
| TEST | Main Side Regime Guard V1 | Confluenza trend | €10.964,56 | €987,59 | 42 | 42 | 57,14% | 2,39 | €23,51 | 3,82% |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | Momentum / breakout | €10.914,47 | €910,79 | 172 | 172 | 50,00% | 1,25 | €5,30 | 6,72% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.852,64 | €854,12 | 158 | 158 | 46,84% | 1,28 | €5,41 | 8,85% |
| TEST | Combo Trend Side Regime Guard V1 | Combo Trend | €10.788,53 | €749,20 | 133 | 133 | 51,13% | 1,29 | €5,63 | 8,10% |
| TEST | 1H Fast No Pepe V1 | Momentum / breakout | €10.575,84 | €578,07 | 258 | 258 | 44,57% | 1,13 | €2,24 | 7,89% |
| TEST | Combo Adaptive Long Only V1 | Combo Adaptive | €10.455,92 | €458,74 | 141 | 141 | 46,81% | 1,16 | €3,25 | 7,78% |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | Momentum / breakout V3 Filtered | €10.374,80 | €382,18 | 83 | 83 | 50,60% | 1,22 | €4,60 | 4,50% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €10.363,82 | €364,97 | 58 | 52 | 48,28% | 1,27 | €6,29 | 3,89% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €10.331,04 | €333,40 | 16 | 16 | 62,50% | 2,35 | €20,84 | 2,77% |
| TEST | Ampia 4H | Confluenza trend | €10.307,55 | €280,43 | 52 | 52 | 34,62% | 1,24 | €5,39 | 4,45% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | Momentum / breakout V3 Filtered | €10.300,05 | €300,05 | 33 | 33 | 48,48% | 2,04 | €9,09 | 2,01% |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | Momentum / breakout V3 Filtered | €10.282,66 | €300,29 | 95 | 95 | 46,32% | 1,16 | €3,16 | 5,24% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | Momentum / breakout V3 Filtered | €10.271,73 | €271,73 | 22 | 22 | 50,00% | 1,74 | €12,35 | 1,72% |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | Momentum / breakout V3 Filtered | €10.246,90 | €249,29 | 208 | 208 | 49,04% | 1,07 | €1,20 | 9,50% |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | Momentum / breakout V3 Filtered | €10.239,20 | €239,20 | 17 | 17 | 52,94% | 4,50 | €14,07 | 1,01% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | Momentum / breakout V3 Filtered | €10.235,18 | €235,18 | 20 | 20 | 50,00% | 1,90 | €11,76 | 2,73% |
| TEST | Combo Adaptive | Combo Adaptive | €10.226,17 | €222,72 | 180 | 180 | 44,44% | 1,07 | €1,24 | 7,91% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.209,20 | €209,20 | 6 | 6 | 83,33% | 4,66 | €34,87 | 0,85% |
| TEST | 1H Fast V3 Nohigh Range Only V1 | Momentum / breakout V3 Filtered | €10.204,53 | €207,25 | 62 | 62 | 46,77% | 1,14 | €3,34 | 4,19% |
| TEST | Scanner Top5 Btc Tp3 V1 | Scanner Top 5 + forza BTC | €10.198,94 | €196,31 | 123 | 123 | 40,65% | 1,07 | €1,60 | 11,78% |
| TEST | Scanner Top5 Btc Runner25 V1 | Scanner Top 5 + forza BTC | €10.192,97 | €190,34 | 127 | 127 | 40,94% | 1,07 | €1,50 | 12,06% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €10.191,22 | €191,22 | 9 | 9 | 55,56% | 2,16 | €21,25 | 1,01% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | Momentum / breakout V3 Filtered | €10.185,37 | €185,37 | 22 | 22 | 40,91% | 1,57 | €8,43 | 2,27% |
| TEST | Rapida 1H V3 Filtered | Momentum / breakout V3 Filtered | €10.181,06 | €183,45 | 252 | 252 | 44,05% | 1,04 | €0,73 | 9,48% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €10.159,24 | €196,46 | 6 | 6 | 50,00% | 2,73 | €32,74 | 1,18% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €10.154,80 | €156,19 | 141 | 141 | 43,97% | 1,05 | €1,11 | 11,27% |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | Momentum / breakout V3 Filtered | €10.145,12 | €145,12 | 44 | 44 | 45,45% | 1,20 | €3,30 | 2,91% |
| TEST | Sol Ema 1H | Trend following EMA | €10.121,32 | €123,38 | 18 | 18 | 44,44% | 1,25 | €6,85 | 3,33% |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | Momentum / breakout V3 Filtered | €10.099,04 | €99,04 | 55 | 55 | 54,55% | 1,12 | €1,80 | 3,59% |
| TEST | Scanner Top10 Long | Scanner Top10 Long | €10.087,45 | €90,24 | 153 | 153 | 47,06% | 1,03 | €0,59 | 10,31% |
| TEST | 1H Fast Score 6 75 Range Only V1 | Momentum / breakout | €10.087,09 | €90,14 | 47 | 47 | 42,55% | 1,07 | €1,92 | 4,60% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.085,97 | €29,45 | 2 | 2 | 50,00% | 1,54 | €14,72 | 0,91% |
| TEST | Combo Adaptive Partial 1R V1 | Combo Adaptive | €10.062,88 | €67,05 | 166 | 166 | 45,18% | 1,03 | €0,40 | 8,69% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €10.058,84 | €21,05 | 12 | 12 | 58,33% | 1,07 | €1,75 | 1,89% |
| TEST | Main Dynamic Asset Selector V1 | Confluenza trend | €10.057,70 | €58,16 | 15 | 15 | 33,33% | 1,13 | €3,88 | 3,39% |
| TEST | Sol Ema 4H | Trend following EMA | €10.057,68 | €57,68 | 10 | 10 | 40,00% | 1,22 | €5,77 | 2,27% |
| TEST | Doge Ema 1H | Trend following EMA | €10.057,57 | €57,57 | 21 | 21 | 61,90% | 1,13 | €2,74 | 2,77% |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | Momentum / breakout V3 Filtered | €10.048,77 | €48,77 | 23 | 23 | 43,48% | 1,12 | €2,12 | 3,05% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €10.045,08 | €45,08 | 28 | 28 | 46,43% | 1,40 | €1,61 | 0,33% |
| TEST | Rapida 1H V1 | Momentum / breakout | €10.043,28 | €43,28 | 78 | 78 | 34,62% | 1,02 | €0,55 | 6,76% |
| TEST | 1H Balanced Short Trend Down Strict V1 | Confluenza trend | €10.035,46 | €35,46 | 13 | 13 | 38,46% | 1,13 | €2,73 | 1,80% |
| TEST | Scalp RSI Long 20 · prudente · 5x | Inversione RSI estrema 15m | €10.032,32 | €32,32 | 11 | 11 | 54,55% | 1,85 | €2,94 | 0,36% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €10.025,86 | €25,86 | 15 | 15 | 60,00% | 1,07 | €1,72 | 3,08% |
| TEST | Scalp RSI Short 85 · €50 · 15x | Inversione RSI estrema 15m | €10.017,98 | €17,98 | 5 | 5 | 60,00% | 1,69 | €3,60 | 0,31% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €10.017,60 | €17,60 | 3 | 3 | 33,33% | 1,17 | €5,87 | 0,96% |
| TEST | Scalp RSI Short 80 · €50 · 15x | Inversione RSI estrema 15m | €10.009,44 | €9,44 | 17 | 17 | 41,18% | 1,17 | €0,56 | 0,53% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €10.009,02 | €9,02 | 28 | 28 | 46,43% | 1,40 | €0,32 | 0,07% |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | Momentum / breakout V3 Filtered | €10.008,92 | €8,92 | 30 | 30 | 36,67% | 1,02 | €0,30 | 4,84% |
| TEST | Scalp RSI Short 85 · €10 · 15x | Inversione RSI estrema 15m | €10.003,60 | €3,60 | 5 | 5 | 60,00% | 1,69 | €0,72 | 0,06% |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | Momentum / breakout V3 Filtered | €10.003,37 | €3,37 | 8 | 8 | 37,50% | 1,02 | €0,42 | 2,15% |
| TEST | Scalp RSI Short 80 · €10 · 15x | Inversione RSI estrema 15m | €10.001,89 | €1,89 | 17 | 17 | 41,18% | 1,17 | €0,11 | 0,11% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €10.001,13 | €3,16 | 20 | 20 | 45,00% | 1,01 | €0,16 | 4,59% |
| TEST | Scanner Bottom5 Short Continuation V1 | Scanner Bottom5 Short Continuation | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 20 · €10 · 15x | Inversione RSI estrema 15m | €9.998,68 | €-1,32 | 11 | 11 | 36,36% | 0,74 | €-0,12 | 0,04% |
| TEST | Scalp RSI Long 15 · €10 · 15x | Inversione RSI estrema 15m | €9.997,60 | €-2,40 | 3 | 3 | 33,33% | 0,13 | €-0,80 | 0,02% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €9.996,52 | €-69,33 | 4 | 4 | 25,00% | 0,56 | €-17,33 | 1,96% |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | Momentum / breakout V3 Filtered | €9.995,23 | €-4,77 | 15 | 15 | 46,67% | 0,99 | €-0,32 | 2,70% |
| TEST | 1H Fast V3 No Esports Long Only V1 | Momentum / breakout V3 Filtered | €9.993,99 | €-5,05 | 195 | 195 | 42,05% | 1,00 | €-0,03 | 10,60% |
| TEST | Scalp RSI Long 20 · €50 · 15x | Inversione RSI estrema 15m | €9.993,42 | €-6,58 | 11 | 11 | 36,36% | 0,74 | €-0,60 | 0,21% |
| TEST | Scalp RSI Short 85 · prudente · 5x | Inversione RSI estrema 15m | €9.991,38 | €-8,62 | 5 | 5 | 60,00% | 0,61 | €-1,72 | 0,30% |
| TEST | Scalp RSI Long 25 · €10 · 15x | Inversione RSI estrema 15m | €9.989,27 | €-10,73 | 17 | 17 | 35,29% | 0,33 | €-0,63 | 0,14% |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | €9.988,00 | €-12,00 | 3 | 3 | 33,33% | 0,13 | €-4,00 | 0,12% |
| TEST | Scanner Top15 Long | Scanner Top15 Long | €9.982,95 | €-14,66 | 152 | 152 | 46,71% | 0,99 | €-0,10 | 10,31% |
| TEST | Scanner Top20 Long | Scanner Top20 Long | €9.982,95 | €-14,66 | 152 | 152 | 46,71% | 0,99 | €-0,10 | 10,31% |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | €9.980,94 | €-19,06 | 3 | 3 | 33,33% | 0,19 | €-6,35 | 0,20% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €9.974,38 | €-25,62 | 17 | 17 | 35,29% | 0,71 | €-1,51 | 0,71% |
| TEST | 1H Fast Tp2 V1 | Momentum / breakout | €9.968,62 | €-30,00 | 247 | 247 | 38,87% | 0,99 | €-0,12 | 6,56% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €9.968,58 | €-31,42 | 9 | 9 | 44,44% | 0,86 | €-3,49 | 1,23% |
| TEST | Combo Adaptive Side Regime Guard V1 | Combo Adaptive | €9.967,91 | €-34,09 | 137 | 137 | 45,26% | 0,99 | €-0,25 | 10,02% |
| TEST | Btc Ema 4H | Trend following EMA | €9.966,88 | €-33,12 | 4 | 4 | 25,00% | 0,78 | €-8,28 | 1,76% |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | €9.946,36 | €-53,64 | 17 | 17 | 35,29% | 0,33 | €-3,16 | 0,72% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.939,62 | €-60,38 | 28 | 28 | 46,43% | 0,60 | €-2,16 | 0,84% |
| TEST | Scalp RSI Short 80 · prudente · 5x | Inversione RSI estrema 15m | €9.939,55 | €-60,45 | 17 | 17 | 35,29% | 0,39 | €-3,56 | 0,89% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €9.913,56 | €-86,44 | 5 | 5 | 20,00% | 0,61 | €-17,29 | 2,43% |
| TEST | 1H Fast Nohigh Cap75 V1 | Momentum / breakout | €9.902,55 | €-95,04 | 180 | 180 | 40,00% | 0,97 | €-0,53 | 8,83% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €9.893,74 | €-105,04 | 130 | 123 | 41,54% | 0,97 | €-0,81 | 10,88% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €9.888,28 | €-97,74 | 11 | 11 | 45,45% | 0,71 | €-8,89 | 1,82% |
| TEST | Eth Ema 4H | Trend following EMA | €9.887,30 | €-112,70 | 7 | 7 | 28,57% | 0,57 | €-16,10 | 1,83% |
| TEST | 1H Fast V3 Nohigh V1 | Momentum / breakout V3 Filtered | €9.862,15 | €-135,93 | 152 | 152 | 43,42% | 0,95 | €-0,89 | 7,10% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.857,66 | €-142,34 | 16 | 16 | 43,75% | 0,72 | €-8,90 | 3,14% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.857,56 | €-139,86 | 14 | 14 | 42,86% | 0,72 | €-9,99 | 2,91% |
| TEST | Combo Scanner | Combo Scanner | €9.851,19 | €-146,92 | 152 | 152 | 44,08% | 0,96 | €-0,97 | 11,38% |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | Momentum / breakout V3 Filtered | €9.837,38 | €-162,62 | 37 | 37 | 40,54% | 0,76 | €-4,40 | 3,08% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | Momentum / breakout V3 Filtered | €9.817,34 | €-182,66 | 24 | 24 | 41,67% | 0,64 | €-7,61 | 3,23% |
| TEST | 1H Fast V3 Long Only V1 | Momentum / breakout V3 Filtered | €9.779,77 | €-218,65 | 196 | 196 | 41,33% | 0,95 | €-1,12 | 12,52% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | Momentum / breakout V3 Filtered | €9.762,18 | €-237,82 | 7 | 7 | 14,29% | 0,02 | €-33,97 | 2,82% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.758,55 | €-246,75 | 19 | 19 | 36,84% | 0,55 | €-12,99 | 3,93% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.747,26 | €-252,74 | 16 | 16 | 31,25% | 0,58 | €-15,80 | 3,74% |
| TEST | Eth Ema 1H | Trend following EMA | €9.734,61 | €-269,38 | 23 | 23 | 39,13% | 0,66 | €-11,71 | 4,80% |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | Combo Adaptive | €9.726,12 | €-273,88 | 46 | 46 | 43,48% | 0,79 | €-5,95 | 4,21% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | Momentum / breakout V3 Filtered | €9.723,72 | €-276,28 | 31 | 31 | 32,26% | 0,62 | €-8,91 | 4,83% |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | Momentum / breakout | €9.656,13 | €-341,52 | 144 | 144 | 38,19% | 0,88 | €-2,37 | 8,83% |
| TEST | 1H Balanced Long No Rhv V1 | Confluenza trend | €9.653,19 | €-344,72 | 115 | 115 | 44,35% | 0,84 | €-3,00 | 9,26% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €9.649,49 | €-350,51 | 8 | 8 | 25,00% | 0,19 | €-43,81 | 4,16% |
| TEST | Combo Adaptive Quality7 Regime V1 | Combo Adaptive | €9.603,78 | €-396,22 | 46 | 46 | 39,13% | 0,69 | €-8,61 | 5,41% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | Momentum / breakout V3 Filtered | €9.579,83 | €-420,17 | 11 | 11 | 0,00% | 0,00 | €-38,20 | 4,20% |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | Momentum / breakout | €9.561,10 | €-437,48 | 99 | 99 | 38,38% | 0,82 | €-4,42 | 7,99% |
| TEST | Btc Ema 1H | Trend following EMA | €9.559,39 | €-432,76 | 18 | 18 | 22,22% | 0,38 | €-24,04 | 4,52% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €9.544,80 | €-408,45 | 176 | 176 | 40,34% | 0,89 | €-2,32 | 10,69% |
| TEST | Combo Adaptive Regime V1 | Combo Adaptive | €9.541,28 | €-457,54 | 77 | 77 | 45,45% | 0,76 | €-5,94 | 5,38% |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | Momentum / breakout V3 Filtered | €9.532,59 | €-450,49 | 115 | 115 | 40,87% | 0,85 | €-3,92 | 6,64% |
| TEST | Scanner Top5 Btc Mfe V1 | Scanner Top 5 + forza BTC | €9.519,63 | €-479,07 | 133 | 133 | 42,86% | 0,82 | €-3,60 | 12,28% |
| TEST | Combo Adaptive Quality7 V1 | Combo Adaptive | €9.514,37 | €-484,42 | 98 | 98 | 38,78% | 0,80 | €-4,94 | 8,88% |
| TEST | Scanner Top5 Btc Guard V1 | Scanner Top 5 + forza BTC | €9.491,50 | €-507,47 | 126 | 126 | 37,30% | 0,84 | €-4,03 | 7,34% |
| TEST | 1H Fast V3 No Esports V1 | Momentum / breakout V3 Filtered | €9.412,84 | €-585,64 | 220 | 220 | 41,82% | 0,87 | €-2,66 | 10,92% |
| TEST | Master Adaptive Gb20 Be V1 | Master Adaptive Consensus | €9.375,37 | €-623,94 | 83 | 83 | 28,92% | 0,74 | €-7,52 | 8,39% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €9.370,06 | €-629,27 | 82 | 82 | 34,15% | 0,73 | €-7,67 | 7,96% |
| TEST | Master Adaptive Gb20 Partial V1 | Master Adaptive Consensus | €9.365,40 | €-633,91 | 78 | 78 | 32,05% | 0,73 | €-8,13 | 7,98% |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | Momentum / breakout V3 Filtered | €9.337,78 | €-645,58 | 118 | 118 | 43,22% | 0,81 | €-5,47 | 8,24% |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | €9.329,18 | €-670,13 | 80 | 80 | 31,25% | 0,73 | €-8,38 | 7,80% |
| TEST | Scanner Bottom10 Short | Scanner Bottom10 Short | €9.320,74 | €-677,79 | 70 | 70 | 31,43% | 0,65 | €-9,68 | 9,06% |
| TEST | Scanner Bottom15 Short | Scanner Bottom15 Short | €9.320,74 | €-677,79 | 70 | 70 | 31,43% | 0,65 | €-9,68 | 9,06% |
| TEST | Scanner Bottom20 Short | Scanner Bottom20 Short | €9.320,74 | €-677,79 | 70 | 70 | 31,43% | 0,65 | €-9,68 | 9,06% |
| TEST | Scanner Top5 Btc Guard Mfe V1 | Scanner Top 5 + forza BTC | €9.270,76 | €-728,23 | 143 | 143 | 38,46% | 0,79 | €-5,09 | 8,78% |
| TEST | 1H Fast Score 6 75 V1 | Momentum / breakout | €9.258,29 | €-749,14 | 143 | 143 | 39,16% | 0,81 | €-5,24 | 14,70% |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | Scanner Bottom 5 Short | €9.256,15 | €-742,38 | 61 | 61 | 31,15% | 0,58 | €-12,17 | 9,08% |
| TEST | Scanner Bottom5 Short Profit Lock V1 | Scanner Bottom 5 Short | €9.242,07 | €-756,47 | 62 | 62 | 30,65% | 0,56 | €-12,20 | 9,08% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €9.223,03 | €-776,38 | 70 | 70 | 30,00% | 0,67 | €-11,09 | 8,25% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €9.206,59 | €-790,90 | 129 | 117 | 41,86% | 0,72 | €-6,13 | 11,21% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €9.206,07 | €-793,24 | 114 | 114 | 43,86% | 0,71 | €-6,96 | 9,02% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.176,14 | €-821,73 | 138 | 138 | 37,68% | 0,70 | €-5,95 | 12,31% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.170,95 | €-827,60 | 89 | 89 | 31,46% | 0,64 | €-9,30 | 10,17% |
| TEST | Master Adaptive Gb20 Loss Cap V1 | Master Adaptive Consensus | €9.157,30 | €-842,66 | 72 | 72 | 22,22% | 0,64 | €-11,70 | 11,41% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €9.145,75 | €-852,30 | 82 | 82 | 31,71% | 0,68 | €-10,39 | 9,97% |
| TEST | Combo Trend | Combo Trend | €9.102,45 | €-878,19 | 174 | 174 | 37,93% | 0,78 | €-5,05 | 11,90% |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | Scanner Top 5 + forza BTC | €9.102,17 | €-896,81 | 88 | 88 | 35,23% | 0,66 | €-10,19 | 11,79% |
| TEST | Combo Adaptive Mfe Trail | Combo Adaptive | €9.072,43 | €-911,13 | 189 | 189 | 40,74% | 0,75 | €-4,82 | 15,45% |
| TEST | 1H Balanced V3 Long Only V1 | Confluenza trend V3 Filtered | €9.027,63 | €-928,15 | 130 | 130 | 40,00% | 0,66 | €-7,14 | 10,43% |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | Momentum / breakout | €9.012,14 | €-995,10 | 101 | 101 | 39,60% | 0,69 | €-9,85 | 15,00% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €8.999,99 | €-988,63 | 127 | 127 | 35,43% | 0,65 | €-7,78 | 15,68% |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | Scanner Top 5 + forza BTC | €8.959,01 | €-1.039,15 | 41 | 41 | 19,51% | 0,28 | €-25,35 | 11,76% |
| TEST | Combo Adaptive Runner25 V1 | Combo Adaptive | €8.949,59 | €-1.145,20 | 99 | 99 | 30,30% | 0,51 | €-11,57 | 14,10% |
| TEST | 1H Fast V3 Cap75 V1 | Momentum / breakout V3 Filtered | €8.947,73 | €-1.059,41 | 146 | 146 | 34,93% | 0,72 | €-7,26 | 16,28% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €8.804,50 | €-1.223,12 | 51 | 51 | 33,33% | 0,43 | €-23,98 | 14,46% |
| TEST | Combo Adaptive Tp3 V1 | Combo Adaptive | €8.782,40 | €-1.310,62 | 80 | 80 | 28,75% | 0,36 | €-16,38 | 14,10% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €8.735,32 | €-1.295,27 | 85 | 85 | 38,82% | 0,55 | €-15,24 | 15,18% |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | Scanner Top 5 + forza BTC | €8.728,44 | €-1.273,76 | 104 | 104 | 33,65% | 0,59 | €-12,25 | 13,91% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €8.704,25 | €-1.294,33 | 71 | 71 | 25,35% | 0,56 | €-18,23 | 13,50% |
| TEST | Scanner Top5 Btc Btc Le3 V1 | Scanner Top 5 + forza BTC | €8.612,89 | €-1.384,66 | 84 | 84 | 29,76% | 0,46 | €-16,48 | 16,16% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €8.397,21 | €-1.604,88 | 109 | 109 | 27,52% | 0,48 | €-14,72 | 19,11% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | SPCX | LONG | Confluenza trend | 240m | 3,0x | 136,56189 | 136,56189 | 128,79610 | 91,72407 | 152,09346 | €285,50 | €856,50 | €48,71 | €0,00 |
| Principale 4H | VELVET | LONG | Confluenza trend | 240m | 3,0x | 0,55987 | 0,55987 | 0,49269 | 0,37605 | 0,69424 | €131,08 | €393,24 | €47,19 | €0,00 |
| Principale 4H | EDEN | LONG | Confluenza trend | 240m | 3,0x | 0,06195 | 0,06195 | 0,05451 | 0,04161 | 0,07681 | €130,34 | €391,02 | €46,92 | €0,00 |
| Principale 4H | TRUMP | LONG | Confluenza trend | 240m | 3,0x | 2,46049 | 2,46049 | 2,16523 | 1,65263 | 3,05101 | €134,98 | €404,95 | €48,59 | €0,00 |
| Principale 4H | XRP | LONG | Confluenza trend | 240m | 3,0x | 1,46057 | 1,34421 | 1,30460 | 0,98102 | 1,77252 | €8,58 | €25,73 | €2,75 | €-2,05 |
| Principale 4H | ZEC | LONG | Confluenza trend | 240m | 3,0x | 852,88054 | 835,72000 | 799,15184 | 572,85143 | 960,33794 | €11,06 | €33,19 | €2,09 | €-0,67 |
| Bilanciata 1H V1 | PEPE | SHORT | Confluenza trend | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €634,36 | €1.903,09 | €44,20 | €4,66 |
| Bilanciata 1H V1 | ARB | LONG | Confluenza trend | 60m | 3,0x | 0,10991 | 0,10991 | 0,10273 | 0,07382 | 0,12428 | €230,61 | €691,82 | €45,23 | €0,00 |
| Bilanciata 1H V1 | BTC | SHORT | Confluenza trend | 60m | 3,0x | 77204,03610 | 77443,87000 | 78315,77422 | 102552,69462 | 74980,55986 | €8,80 | €26,39 | €0,38 | €-0,08 |
| Bilanciata 1H V1 | USELESS | LONG | Confluenza trend | 60m | 3,0x | 0,11591 | 0,11096 | 0,10466 | 0,07786 | 0,13843 | €154,36 | €463,09 | €44,98 | €-19,79 |
| Bilanciata 1H V1 | ETH | SHORT | Confluenza trend | 60m | 3,0x | 2417,02650 | 2410,98000 | 2451,83168 | 3210,61686 | 2347,41613 | €1.041,05 | €3.123,14 | €44,97 | €7,81 |
| Bilanciata 1H V1 | DOGE | SHORT | Confluenza trend | 60m | 3,0x | 0,08051 | 0,08150 | 0,08185 | 0,10695 | 0,07783 | €18,24 | €54,72 | €0,91 | €-0,67 |
| 1H Balanced Long No Rhv V1 | SKHYNIX | LONG | Confluenza trend | 60m | 3,0x | 1214,11277 | 1214,11277 | 1170,18211 | 815,47908 | 1301,97411 | €413,43 | €1.240,28 | €44,88 | €0,00 |
| 1H Balanced Long No Rhv V1 | BOME | LONG | Confluenza trend | 60m | 3,0x | 0,00129 | 0,00129 | 0,00114 | 0,00087 | 0,00160 | €134,98 | €404,95 | €48,59 | €0,00 |
| 1H Balanced Long No Rhv V1 | TAO | LONG | Confluenza trend | 60m | 3,0x | 247,38947 | 247,38947 | 237,94346 | 166,16326 | 266,28148 | €428,20 | €1.284,61 | €49,05 | €0,00 |
| 1H Balanced Long No Rhv V1 | HEMI | LONG | Confluenza trend | 60m | 3,0x | 0,01177 | 0,01177 | 0,01036 | 0,00790 | 0,01459 | €131,93 | €395,78 | €47,49 | €0,00 |
| 1H Balanced Long No Rhv V1 | ARB | LONG | Confluenza trend | 60m | 3,0x | 0,11110 | 0,11110 | 0,10386 | 0,07462 | 0,12560 | €15,59 | €46,76 | €3,05 | €0,00 |
| Bilanciata 1H V2 | SKHYNIX | LONG | Confluenza trend V2 | 60m | 3,0x | 1214,11277 | 1214,11277 | 1170,18211 | 815,47908 | 1301,97411 | €422,38 | €1.267,15 | €45,85 | €0,00 |
| Bilanciata 1H V2 | XMR | LONG | Confluenza trend V2 | 60m | 3,0x | 520,62410 | 520,62410 | 498,16818 | 349,68586 | 565,53596 | €358,56 | €1.075,68 | €46,40 | €0,00 |
| Bilanciata 1H V2 | PEPE | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €9,49 | €28,46 | €0,69 | €0,34 |
| Bilanciata 1H V2 | USELESS | LONG | Confluenza trend V2 | 60m | 3,0x | 0,11116 | 0,11096 | 0,09999 | 0,07466 | 0,13351 | €152,70 | €458,10 | €46,04 | €-0,83 |
| Bilanciata 1H V2 | ENA | LONG | Confluenza trend V2 | 60m | 3,0x | 0,16057 | 0,16057 | 0,15346 | 0,10785 | 0,17479 | €12,00 | €35,99 | €1,59 | €0,00 |
| Bilanciata 1H V3 Filtered | SKHYNIX | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1220,85412 | 1220,85412 | 1177,63561 | 820,00702 | 1307,29117 | €460,42 | €1.381,27 | €48,90 | €0,00 |
| Bilanciata 1H V3 Filtered | ADA | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,20138 | 0,20138 | 0,20719 | 0,26750 | 0,18976 | €559,88 | €1.679,63 | €48,45 | €-0,00 |
| Bilanciata 1H V3 Filtered | USELESS | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,11591 | 0,11096 | 0,10466 | 0,07786 | 0,13843 | €161,07 | €483,22 | €46,93 | €-20,65 |
| Bilanciata 1H V3 Filtered | BTC | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 76920,91274 | 77443,87000 | 78028,57388 | 102176,61242 | 74705,59045 | €1.088,71 | €3.266,12 | €47,03 | €-22,21 |
| 1H Fast Score 6 75 V1 | ARB | LONG | Momentum / breakout | 60m | 3,0x | 0,10878 | 0,10878 | 0,10318 | 0,07307 | 0,11718 | €300,38 | €901,14 | €46,37 | €0,00 |
| 1H Fast Score 6 75 V1 | USELESS | LONG | Momentum / breakout | 60m | 3,0x | 0,11367 | 0,11096 | 0,10544 | 0,07635 | 0,12603 | €211,09 | €633,27 | €45,88 | €-15,11 |
| 1H Fast Score 6 75 V1 | ENA | LONG | Momentum / breakout | 60m | 3,0x | 0,16057 | 0,16057 | 0,15504 | 0,10785 | 0,16887 | €446,88 | €1.340,64 | €46,17 | €0,00 |
| 1H Fast Score 6 75 V1 | UNI | LONG | Momentum / breakout | 60m | 3,0x | 6,13623 | 6,23800 | 6,13623 | 4,12150 | 6,41501 | €508,05 | €1.524,15 | €0,00 | €25,28 |
| 1H Fast Score 6 75 No Trend Up V1 | ARB | LONG | Momentum / breakout | 60m | 3,0x | 0,10878 | 0,10878 | 0,10318 | 0,07307 | 0,11718 | €292,39 | €877,18 | €45,14 | €0,00 |
| 1H Fast Score 6 75 No Trend Up V1 | USELESS | LONG | Momentum / breakout | 60m | 3,0x | 0,11367 | 0,11096 | 0,10544 | 0,07635 | 0,12603 | €205,48 | €616,43 | €44,66 | €-14,71 |
| 1H Fast Score 6 75 No Trend Up V1 | ENA | LONG | Momentum / breakout | 60m | 3,0x | 0,16057 | 0,16057 | 0,15504 | 0,10785 | 0,16887 | €435,00 | €1.305,00 | €44,94 | €0,00 |
| 1H Fast Score 6 75 No Trend Up V1 | UNI | LONG | Momentum / breakout | 60m | 3,0x | 6,13623 | 6,23800 | 6,13623 | 4,12150 | 6,41501 | €494,54 | €1.483,63 | €0,00 | €24,61 |
| 1H Fast Score 6 75 Range Only V1 | ADA | SHORT | Momentum / breakout | 60m | 3,0x | 0,20260 | 0,20260 | 0,20707 | 0,26912 | 0,19589 | €765,21 | €2.295,64 | €50,71 | €-0,00 |
| 1H Fast Score 6 75 Range Only V1 | HEMI | LONG | Momentum / breakout | 60m | 3,0x | 0,01177 | 0,01177 | 0,01065 | 0,00790 | 0,01345 | €178,53 | €535,59 | €51,05 | €0,00 |
| 1H Fast Score 6 75 Range Only V1 | ARB | LONG | Momentum / breakout | 60m | 3,0x | 0,10878 | 0,10878 | 0,10318 | 0,07307 | 0,11718 | €326,57 | €979,72 | €50,41 | €0,00 |
| 1H Fast Score 6 75 Range Only V1 | ENA | LONG | Momentum / breakout | 60m | 3,0x | 0,16057 | 0,16057 | 0,15504 | 0,10785 | 0,16887 | €479,90 | €1.439,69 | €49,58 | €0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | BTW | LONG | Momentum / breakout | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €8,91 | €26,72 | €3,13 | €0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00086 | 0,00146 | €215,92 | €647,76 | €57,03 | €0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | NEAR | LONG | Momentum / breakout | 60m | 3,0x | 2,08142 | 2,08142 | 2,02315 | 1,39802 | 2,16882 | €42,86 | €128,59 | €3,60 | €0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €157,13 | €471,39 | €56,57 | €-0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | USELESS | LONG | Momentum / breakout | 60m | 3,0x | 0,11008 | 0,11096 | 0,10173 | 0,07394 | 0,12260 | €240,53 | €721,59 | €54,72 | €5,76 |
| 1H Fast Score 6 75 Cost Aware V1 | ENA | LONG | Momentum / breakout | 60m | 3,0x | 0,16057 | 0,16057 | 0,15504 | 0,10785 | 0,16887 | €418,42 | €1.255,26 | €43,23 | €0,00 |
| 1H Fast Nohigh Cap75 V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €139,29 | €417,86 | €50,14 | €-0,00 |
| 1H Fast Nohigh Cap75 V1 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €141,57 | €424,71 | €50,14 | €-0,00 |
| 1H Fast Nohigh Cap75 V1 | XMR | LONG | Momentum / breakout | 60m | 3,0x | 527,13541 | 527,13541 | 512,43358 | 354,05928 | 549,18814 | €585,79 | €1.757,38 | €49,01 | €0,00 |
| 1H Fast Nohigh Cap75 V1 | ENA | LONG | Momentum / breakout | 60m | 3,0x | 0,16057 | 0,16057 | 0,15504 | 0,10785 | 0,16887 | €472,06 | €1.416,18 | €48,77 | €0,00 |
| 1H Fast Long Btc 1 3 Cap75 V1 | PROM | LONG | Momentum / breakout | 60m | 3,0x | 6,93686 | 6,93686 | 6,39299 | 4,65926 | 7,75266 | €205,67 | €617,01 | €48,38 | €0,00 |
| 1H Fast Long Btc 1 3 Cap75 V1 | XMR | LONG | Momentum / breakout | 60m | 3,0x | 527,17541 | 527,17541 | 512,97206 | 354,08615 | 548,48045 | €585,90 | €1.757,69 | €47,36 | €0,00 |
| 1H Fast No Pepe V1 | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €172,22 | €516,67 | €49,86 | €0,00 |
| 1H Fast No Pepe V1 | TAO | LONG | Momentum / breakout | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €47,93 | €143,78 | €4,27 | €0,00 |
| 1H Fast No Pepe V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €136,27 | €408,80 | €49,06 | €-0,00 |
| 1H Fast No Pepe V1 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €9,48 | €28,43 | €3,41 | €-0,00 |
| 1H Fast No Pepe V1 | ADA | SHORT | Momentum / breakout | 60m | 3,0x | 0,20138 | 0,20138 | 0,20590 | 0,26750 | 0,19460 | €739,08 | €2.217,23 | €49,74 | €-0,00 |
| 1H Fast No Pepe V1 | 0G | LONG | Momentum / breakout | 60m | 3,0x | 0,23904 | 0,23904 | 0,21901 | 0,16056 | 0,26909 | €210,41 | €631,23 | €52,89 | €0,00 |
| 1H Fast No Pepe V1 | ENA | LONG | Momentum / breakout | 60m | 3,0x | 0,16057 | 0,16057 | 0,15504 | 0,10785 | 0,16887 | €22,20 | €66,59 | €2,29 | €0,00 |
| 1H Fast Tp2 V1 | BTW | LONG | Momentum / breakout | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,56752 | €142,85 | €428,56 | €50,25 | €0,00 |
| 1H Fast Tp2 V1 | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00132 | 0,00132 | 0,00119 | 0,00088 | 0,00158 | €18,87 | €56,62 | €5,59 | €0,00 |
| 1H Fast Tp2 V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,17246 | 0,17246 | 0,17246 | 0,22908 | 0,13107 | €139,71 | €419,14 | €0,00 | €-0,00 |
| 1H Fast Tp2 V1 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03379 | €141,13 | €423,40 | €50,81 | €-0,00 |
| 1H Fast Tp2 V1 | ARB | LONG | Momentum / breakout | 60m | 3,0x | 0,10991 | 0,10991 | 0,10432 | 0,07382 | 0,12109 | €278,24 | €834,72 | €42,44 | €0,00 |
| Rapida 1H V2 | ADA | SHORT | Momentum / breakout V2 | 60m | 3,0x | 0,20283 | 0,20283 | 0,20750 | 0,26943 | 0,19582 | €749,31 | €2.247,94 | €51,80 | €-0,00 |
| Rapida 1H V3 Filtered | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €172,00 | €515,99 | €49,79 | €0,00 |
| Rapida 1H V3 Filtered | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €589,98 | €1.769,95 | €52,56 | €0,00 |
| Rapida 1H V3 Filtered | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €140,02 | €420,06 | €50,41 | €-0,00 |
| Rapida 1H V3 Filtered | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €16,99 | €50,96 | €6,11 | €-0,00 |
| Rapida 1H V3 Filtered | ARB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,10991 | 0,10991 | 0,10432 | 0,07382 | 0,11829 | €293,41 | €880,24 | €44,76 | €0,00 |
| 1H Fast V3 Cap75 V1 | ARB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,10878 | 0,10878 | 0,10318 | 0,07307 | 0,11718 | €290,81 | €872,44 | €44,89 | €0,00 |
| 1H Fast V3 Cap75 V1 | USELESS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,11367 | 0,11096 | 0,10544 | 0,07635 | 0,12603 | €204,16 | €612,48 | €44,38 | €-14,62 |
| 1H Fast V3 Cap75 V1 | ENA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16057 | 0,16057 | 0,15504 | 0,10785 | 0,16887 | €431,89 | €1.295,68 | €44,62 | €0,00 |
| 1H Fast V3 Cap75 V1 | UNI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 6,13623 | 6,23800 | 6,13623 | 4,12150 | 6,41501 | €490,48 | €1.471,44 | €0,00 | €24,40 |
| 1H Fast V3 Nohigh V1 | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €131,05 | €393,14 | €47,18 | €-0,00 |
| 1H Fast V3 Nohigh V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €133,20 | €399,59 | €47,18 | €-0,00 |
| 1H Fast V3 Nohigh V1 | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,20138 | 0,20138 | 0,20590 | 0,26750 | 0,19460 | €719,57 | €2.158,72 | €48,43 | €-0,00 |
| 1H Fast V3 Nohigh V1 | 0G | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,23904 | 0,23904 | 0,21901 | 0,16056 | 0,26909 | €196,32 | €588,95 | €49,35 | €0,00 |
| 1H Fast V3 Nohigh V1 | ARB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,10991 | 0,10991 | 0,10432 | 0,07382 | 0,11829 | €26,13 | €78,40 | €3,99 | €0,00 |
| 1H Fast V3 Nohigh V1 | ENA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16057 | 0,16057 | 0,15504 | 0,10785 | 0,16887 | €10,94 | €32,83 | €1,13 | €0,00 |
| 1H Fast V3 Long Only V1 | BTW | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €126,57 | €379,72 | €44,52 | €0,00 |
| 1H Fast V3 Long Only V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00147 | €9,56 | €28,69 | €2,66 | €0,00 |
| 1H Fast V3 Long Only V1 | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €554,42 | €1.663,26 | €49,39 | €0,00 |
| 1H Fast V3 Long Only V1 | HEMI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01177 | 0,01177 | 0,01065 | 0,00790 | 0,01345 | €170,60 | €511,79 | €48,79 | €0,00 |
| 1H Fast V3 Long Only V1 | ENA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16057 | 0,16057 | 0,15504 | 0,10785 | 0,16887 | €19,73 | €59,20 | €2,04 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 V1 | HEMI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01177 | 0,01177 | 0,01065 | 0,00790 | 0,01345 | €166,97 | €500,92 | €47,75 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 V1 | PROM | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 6,92735 | 6,92735 | 6,35093 | 4,65287 | 7,79198 | €195,87 | €587,60 | €48,89 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 V1 | ARB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,10878 | 0,10878 | 0,10318 | 0,07307 | 0,11718 | €310,83 | €932,49 | €47,98 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 V1 | USELESS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,11367 | 0,11096 | 0,10544 | 0,07635 | 0,12603 | €212,69 | €638,08 | €46,23 | €-15,23 |
| 1H Fast V3 No Esports V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €169,36 | €508,09 | €49,03 | €0,00 |
| 1H Fast V3 No Esports V1 | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €27,04 | €81,13 | €2,41 | €0,00 |
| 1H Fast V3 No Esports V1 | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €133,96 | €401,88 | €48,23 | €-0,00 |
| 1H Fast V3 No Esports V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €129,73 | €389,20 | €46,70 | €-0,00 |
| 1H Fast V3 No Esports V1 | ARB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,10991 | 0,10991 | 0,10432 | 0,07382 | 0,11829 | €274,69 | €824,06 | €41,90 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | BTW | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €132,94 | €398,81 | €46,76 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00147 | €10,06 | €30,18 | €2,80 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | HEMI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01177 | 0,01177 | 0,01065 | 0,00790 | 0,01345 | €175,30 | €525,91 | €50,13 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | PROM | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 6,92735 | 6,92735 | 6,35093 | 4,65287 | 7,79198 | €9,71 | €29,12 | €2,42 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | 0G | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,23904 | 0,23904 | 0,21901 | 0,16056 | 0,26909 | €187,89 | €563,68 | €47,23 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | ENA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16057 | 0,16057 | 0,15504 | 0,10785 | 0,16887 | €17,27 | €51,82 | €1,78 | €0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €173,11 | €519,32 | €50,11 | €0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €593,79 | €1.781,38 | €52,90 | €0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €140,93 | €422,78 | €50,73 | €-0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €17,09 | €51,28 | €6,15 | €-0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | ARB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,10991 | 0,10991 | 0,10432 | 0,07382 | 0,11829 | €295,31 | €885,93 | €45,05 | €0,00 |
| 1H Fast V3 No Esports Stress Guard V1 | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,20283 | 0,20283 | 0,20750 | 0,26943 | 0,19582 | €739,04 | €2.217,11 | €51,09 | €-0,00 |
| 1H Fast V3 No Esports Stress Guard V1 | SOL | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 99,69706 | 99,78700 | 101,13696 | 132,43092 | 97,53720 | €1.183,21 | €3.549,63 | €51,27 | €-3,20 |
| 1H Fast V3 No Esports Stress Guard V1 | ENA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16057 | 0,16057 | 0,15504 | 0,10785 | 0,16887 | €502,45 | €1.507,35 | €51,91 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | HEMI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01177 | 0,01177 | 0,01065 | 0,00790 | 0,01345 | €163,25 | €489,75 | €46,69 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | PROM | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 6,92735 | 6,92735 | 6,35093 | 4,65287 | 7,79198 | €191,37 | €574,11 | €47,77 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | ARB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,10878 | 0,10878 | 0,10318 | 0,07307 | 0,11718 | €304,49 | €913,46 | €47,00 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | USELESS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,11367 | 0,11096 | 0,10544 | 0,07635 | 0,12603 | €209,32 | €627,96 | €45,50 | €-14,99 |
| Ampia 4H | SPCX | LONG | Confluenza trend | 240m | 2,0x | 136,56189 | 136,56189 | 126,46637 | 68,96375 | 164,82935 | €323,86 | €647,73 | €47,88 | €0,00 |
| Ampia 4H | VELVET | LONG | Confluenza trend | 240m | 2,0x | 0,55987 | 0,55987 | 0,49269 | 0,28274 | 0,74799 | €201,63 | €403,26 | €48,39 | €0,00 |
| Ampia 4H | LINK | LONG | Confluenza trend | 240m | 2,0x | 11,96839 | 11,96839 | 11,08055 | 6,04404 | 14,45436 | €14,07 | €28,15 | €2,09 | €0,00 |
| Ampia 4H | ETH | LONG | Confluenza trend | 240m | 2,0x | 2430,03591 | 2410,98000 | 2267,54364 | 1227,16813 | 2885,01426 | €18,82 | €37,65 | €2,52 | €-0,30 |
| Ampia 4H | HYPE | LONG | Confluenza trend | 240m | 2,0x | 79,31286 | 82,88000 | 70,73982 | 40,05299 | 103,31737 | €13,82 | €27,64 | €2,99 | €1,24 |
| Ampia 4H | TRUMP | LONG | Confluenza trend | 240m | 2,0x | 2,37347 | 2,37347 | 2,08866 | 1,19860 | 3,17096 | €210,83 | €421,66 | €50,60 | €0,00 |
| Ampia 4H | DOGE | SHORT | Confluenza trend | 240m | 2,0x | 0,08583 | 0,08150 | 0,09382 | 0,12832 | 0,06346 | €274,53 | €549,07 | €51,10 | €27,72 |
| Ampia 4H | SOL | LONG | Confluenza trend | 240m | 2,0x | 103,77875 | 99,78700 | 96,79200 | 52,40827 | 123,34165 | €13,62 | €27,23 | €1,83 | €-1,05 |
| Forza relativa 1H V1 | XMR | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 522,67451 | 522,67451 | 500,84717 | 263,95063 | 570,69467 | €505,06 | €1.010,12 | €42,18 | €0,00 |
| Forza relativa 1H V1 | PEPE | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00001 | 0,00000 | €869,59 | €1.739,17 | €40,40 | €4,26 |
| Forza relativa 1H V1 | ARB | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,10812 | 0,10812 | 0,10113 | 0,05460 | 0,12350 | €321,13 | €642,27 | €41,51 | €0,00 |
| Forza relativa 1H V1 | SOL | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 99,89102 | 99,78700 | 101,70108 | 149,33707 | 95,90889 | €13,28 | €26,56 | €0,48 | €0,03 |
| Forza relativa 1H V1 | ENA | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,16057 | 0,16057 | 0,15346 | 0,08109 | 0,17621 | €16,43 | €32,85 | €1,45 | €0,00 |
| Forza relativa 1H V1 | USELESS | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,11098 | 0,11096 | 0,10103 | 0,05605 | 0,13289 | €233,68 | €467,36 | €41,93 | €-0,09 |
| Forza relativa 1H V2 | BEAT | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,25984 | 0,25984 | 0,25657 | 0,38847 | 0,19125 | €200,38 | €400,75 | €0,00 | €-0,00 |
| Forza relativa 1H V2 | TUT | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,04452 | 0,04452 | 0,04986 | 0,06656 | 0,03277 | €204,64 | €409,28 | €49,11 | €-0,00 |
| Forza relativa 1H V2 | ADA | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,20283 | 0,20283 | 0,20884 | 0,30323 | 0,18961 | €17,52 | €35,04 | €1,04 | €-0,00 |
| Forza relativa 1H V2 | HEMI | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €200,86 | €401,72 | €48,21 | €0,00 |
| Forza relativa 1H V2 | XMR | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 520,62410 | 520,62410 | 498,16818 | 262,91517 | 570,02714 | €13,24 | €26,48 | €1,14 | €0,00 |
| Forza relativa 1H V2 | ENA | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,16057 | 0,16057 | 0,15346 | 0,08109 | 0,17621 | €16,83 | €33,66 | €1,49 | €0,00 |
| Forza relativa 1H V2 | USELESS | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,11098 | 0,11096 | 0,10103 | 0,05605 | 0,13289 | €272,01 | €544,03 | €48,80 | €-0,11 |
| Benchmark Donchian breakout 1H | SKHYNIX | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1174,33482 | 1174,33482 | 1128,44989 | 593,03908 | 1289,04713 | €641,25 | €1.282,50 | €50,11 | €0,00 |
| Benchmark Donchian breakout 1H | VELVET | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,14787 | 0,14787 | 0,16561 | 0,22107 | 0,10351 | €237,23 | €474,47 | €56,94 | €-0,00 |
| Benchmark Donchian breakout 1H | ADA | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,20283 | 0,20283 | 0,20951 | 0,30323 | 0,18614 | €72,87 | €145,74 | €4,80 | €-0,00 |
| Benchmark Donchian breakout 1H | ETH | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 2415,46681 | 2410,98000 | 2454,11428 | 3611,12288 | 2318,84814 | €1.754,61 | €3.509,21 | €56,15 | €6,52 |
| Benchmark Donchian breakout 1H | SOL | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 99,77304 | 99,78700 | 101,87931 | 149,16070 | 94,50736 | €1.329,55 | €2.659,09 | €56,14 | €-0,37 |
| Benchmark Donchian breakout 1H | XRP | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 1,33090 | 1,34421 | 1,35970 | 1,98970 | 1,25890 | €35,95 | €71,89 | €1,56 | €-0,72 |
| Donchian 1H Gb20 120R V1 | SKHYNIX | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1174,33482 | 1174,33482 | 1128,44989 | 593,03908 | 1289,04713 | €626,15 | €1.252,30 | €48,93 | €0,00 |
| Donchian 1H Gb20 120R V1 | VELVET | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,14787 | 0,14787 | 0,16561 | 0,22107 | 0,10351 | €231,65 | €463,30 | €55,60 | €-0,00 |
| Donchian 1H Gb20 120R V1 | ADA | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,20283 | 0,20283 | 0,20951 | 0,30323 | 0,18614 | €71,16 | €142,31 | €4,68 | €-0,00 |
| Donchian 1H Gb20 120R V1 | ETH | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 2415,46681 | 2410,98000 | 2454,11428 | 3611,12288 | 2318,84814 | €1.713,30 | €3.426,59 | €54,83 | €6,37 |
| Donchian 1H Gb20 120R V1 | SOL | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 99,77304 | 99,78700 | 101,87931 | 149,16070 | 94,50736 | €1.298,24 | €2.596,49 | €54,81 | €-0,36 |
| Donchian 1H Gb20 120R V1 | XRP | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 1,33090 | 1,34421 | 1,35970 | 1,98970 | 1,25890 | €35,10 | €70,20 | €1,52 | €-0,70 |
| Benchmark Bollinger mean reversion 1H | SOL | LONG | Bollinger mean reversion | 60m | 2,0x | 99,81296 | 99,78700 | 98,23262 | 50,40554 | 102,18346 | €1.381,04 | €2.762,08 | €43,73 | €-0,72 |
| Benchmark Bollinger mean reversion 1H | DOGE | LONG | Bollinger mean reversion | 60m | 2,0x | 0,08061 | 0,08150 | 0,08085 | 0,04071 | 0,08229 | €1.571,36 | €3.142,73 | €0,00 | €34,76 |
| Benchmark trend following EMA 1H | BEAT | SHORT | Trend following EMA | 60m | 2,0x | 0,28257 | 0,28257 | 0,25706 | 0,42244 | 0,20797 | €186,11 | €372,23 | €0,00 | €-0,00 |
| Benchmark trend following EMA 1H | TUT | SHORT | Trend following EMA | 60m | 2,0x | 0,04446 | 0,04446 | 0,04980 | 0,06647 | 0,03272 | €194,70 | €389,39 | €46,73 | €-0,00 |
| Benchmark trend following EMA 1H | VELVET | SHORT | Trend following EMA | 60m | 2,0x | 0,14786 | 0,14786 | 0,16560 | 0,22105 | 0,10883 | €187,91 | €375,83 | €45,10 | €-0,00 |
| Benchmark trend following EMA 1H | USELESS | LONG | Trend following EMA | 60m | 2,0x | 0,11591 | 0,11096 | 0,10340 | 0,05854 | 0,14343 | €17,31 | €34,63 | €3,74 | €-1,48 |
| Benchmark trend following EMA 1H | SOL | SHORT | Trend following EMA | 60m | 2,0x | 100,01299 | 99,78700 | 101,99785 | 149,51943 | 95,64631 | €16,08 | €32,17 | €0,64 | €0,07 |
| Benchmark trend following EMA 1H | DOGE | SHORT | Trend following EMA | 60m | 2,0x | 0,08148 | 0,08150 | 0,08296 | 0,12181 | 0,07823 | €14,32 | €28,63 | €0,52 | €-0,01 |
| Scanner Top 5 Long 1H | BOME | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00160 | €218,24 | €436,47 | €52,38 | €0,00 |
| Scanner Top 5 Long 1H | TRUMP | LONG | Scanner Top 5 Long | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,08367 | €238,89 | €477,78 | €55,13 | €0,00 |
| Scanner Top 5 Long 1H | SKHYNIX | LONG | Scanner Top 5 Long | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1331,36020 | €17,74 | €35,49 | €0,91 | €0,00 |
| Scanner Top 5 Long 1H | HEMI | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €228,24 | €456,48 | €54,78 | €0,00 |
| Scanner Top 5 Long 1H | XMR | LONG | Scanner Top 5 Long | 60m | 2,0x | 519,56389 | 519,56389 | 495,28598 | 262,37977 | 568,11972 | €14,50 | €28,99 | €1,35 | €0,00 |
| Scanner Top 5 Long 1H | ARB | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,10968 | 0,10968 | 0,10275 | 0,05539 | 0,12353 | €415,84 | €831,69 | €52,53 | €0,00 |
| Scanner Bottom 5 Short 1H | SOXL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €378,86 | €757,72 | €48,07 | €-0,00 |
| Scanner Bottom 5 Short 1H | SNDK | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €492,80 | €985,60 | €47,71 | €-0,00 |
| Scanner Bottom 5 Short 1H | VELVET | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €191,07 | €382,14 | €0,00 | €-0,00 |
| Scanner Bottom 5 Short 1H | TUT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €178,38 | €356,76 | €42,81 | €-0,00 |
| Scanner Top10 Long | TAO | LONG | Scanner Top10 Long | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €678,43 | €1.356,86 | €51,81 | €0,00 |
| Scanner Top10 Long | SKHYNIX | LONG | Scanner Top10 Long | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €972,86 | €1.945,72 | €48,38 | €0,00 |
| Scanner Top10 Long | HEMI | LONG | Scanner Top10 Long | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €207,88 | €415,77 | €49,89 | €0,00 |
| Scanner Top10 Long | XMR | LONG | Scanner Top10 Long | 60m | 2,0x | 519,56389 | 519,56389 | 495,28598 | 262,37977 | 568,11972 | €12,79 | €25,57 | €1,20 | €0,00 |
| Scanner Top10 Long | ARB | LONG | Scanner Top10 Long | 60m | 2,0x | 0,10968 | 0,10968 | 0,10275 | 0,05539 | 0,12353 | €386,28 | €772,56 | €48,79 | €0,00 |
| Scanner Bottom10 Short | SOXL | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom10 Short | SNDK | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Bottom10 Short | VELVET | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €194,19 | €388,38 | €0,00 | €-0,00 |
| Scanner Bottom10 Short | TUT | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €181,31 | €362,61 | €43,51 | €-0,00 |
| Scanner Top15 Long | NEAR | LONG | Scanner Top15 Long | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €16,79 | €33,59 | €1,21 | €0,00 |
| Scanner Top15 Long | TAO | LONG | Scanner Top15 Long | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €88,53 | €177,07 | €6,76 | €0,00 |
| Scanner Top15 Long | TRUMP | LONG | Scanner Top15 Long | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,08367 | €215,87 | €431,75 | €49,81 | €0,00 |
| Scanner Top15 Long | SKHYNIX | LONG | Scanner Top15 Long | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €787,36 | €1.574,72 | €39,16 | €0,00 |
| Scanner Top15 Long | XMR | LONG | Scanner Top15 Long | 60m | 2,0x | 522,24443 | 522,24443 | 497,48743 | 263,73344 | 571,75843 | €19,54 | €39,08 | €1,85 | €0,00 |
| Scanner Top15 Long | ARB | LONG | Scanner Top15 Long | 60m | 2,0x | 0,10968 | 0,10968 | 0,10275 | 0,05539 | 0,12353 | €379,03 | €758,05 | €47,87 | €0,00 |
| Scanner Top15 Long | ENA | LONG | Scanner Top15 Long | 60m | 2,0x | 0,15596 | 0,15596 | 0,14889 | 0,07876 | 0,17010 | €21,88 | €43,77 | €1,98 | €0,00 |
| Scanner Top15 Long | USELESS | LONG | Scanner Top15 Long | 60m | 2,0x | 0,11098 | 0,11096 | 0,10103 | 0,05605 | 0,13089 | €278,22 | €556,44 | €49,92 | €-0,11 |
| Scanner Bottom15 Short | SOXL | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom15 Short | SNDK | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Bottom15 Short | VELVET | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €194,19 | €388,38 | €0,00 | €-0,00 |
| Scanner Bottom15 Short | TUT | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €181,31 | €362,61 | €43,51 | €-0,00 |
| Scanner Top20 Long | NEAR | LONG | Scanner Top20 Long | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €16,79 | €33,59 | €1,21 | €0,00 |
| Scanner Top20 Long | TAO | LONG | Scanner Top20 Long | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €88,53 | €177,07 | €6,76 | €0,00 |
| Scanner Top20 Long | TRUMP | LONG | Scanner Top20 Long | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,08367 | €215,87 | €431,75 | €49,81 | €0,00 |
| Scanner Top20 Long | SKHYNIX | LONG | Scanner Top20 Long | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €787,36 | €1.574,72 | €39,16 | €0,00 |
| Scanner Top20 Long | XMR | LONG | Scanner Top20 Long | 60m | 2,0x | 522,24443 | 522,24443 | 497,48743 | 263,73344 | 571,75843 | €19,54 | €39,08 | €1,85 | €0,00 |
| Scanner Top20 Long | ARB | LONG | Scanner Top20 Long | 60m | 2,0x | 0,10968 | 0,10968 | 0,10275 | 0,05539 | 0,12353 | €379,03 | €758,05 | €47,87 | €0,00 |
| Scanner Top20 Long | ENA | LONG | Scanner Top20 Long | 60m | 2,0x | 0,15596 | 0,15596 | 0,14889 | 0,07876 | 0,17010 | €21,88 | €43,77 | €1,98 | €0,00 |
| Scanner Top20 Long | USELESS | LONG | Scanner Top20 Long | 60m | 2,0x | 0,11098 | 0,11096 | 0,10103 | 0,05605 | 0,13089 | €278,22 | €556,44 | €49,92 | €-0,11 |
| Scanner Bottom20 Short | SOXL | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom20 Short | SNDK | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Bottom20 Short | VELVET | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €194,19 | €388,38 | €0,00 | €-0,00 |
| Scanner Bottom20 Short | TUT | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €181,31 | €362,61 | €43,51 | €-0,00 |
| Scanner Top 5 + forza BTC 1H | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €203,45 | €406,91 | €48,83 | €0,00 |
| Scanner Top 5 + forza BTC 1H | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,14149 | €223,03 | €446,06 | €51,47 | €0,00 |
| Scanner Top 5 + forza BTC 1H | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €18,23 | €36,45 | €0,93 | €0,00 |
| Scanner Top 5 + forza BTC 1H | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €213,35 | €426,70 | €51,20 | €0,00 |
| Scanner Top 5 + forza BTC 1H | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 519,56389 | 519,56389 | 495,28598 | 262,37977 | 572,97530 | €16,38 | €32,76 | €1,53 | €0,00 |
| Scanner Top 5 + forza BTC 1H | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,10968 | 0,10968 | 0,10275 | 0,05539 | 0,12491 | €389,11 | €778,23 | €49,15 | €0,00 |
| Scanner Top5 Btc Mfe V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €190,73 | €381,46 | €45,77 | €0,00 |
| Scanner Top5 Btc Mfe V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,14149 | €209,08 | €418,16 | €48,25 | €0,00 |
| Scanner Top5 Btc Mfe V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €17,09 | €34,17 | €0,88 | €0,00 |
| Scanner Top5 Btc Mfe V1 | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €200,01 | €400,01 | €48,00 | €0,00 |
| Scanner Top5 Btc Mfe V1 | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 519,56389 | 519,56389 | 495,28598 | 262,37977 | 572,97530 | €15,36 | €30,72 | €1,44 | €0,00 |
| Scanner Top5 Btc Mfe V1 | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,10968 | 0,10968 | 0,10275 | 0,05539 | 0,12491 | €364,77 | €729,55 | €46,07 | €0,00 |
| Scanner Top5 Btc Guard V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €197,27 | €394,55 | €47,35 | €0,00 |
| Scanner Top5 Btc Guard V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,55551 | 2,55551 | 2,29388 | 1,29053 | 3,13109 | €13,03 | €26,06 | €2,67 | €0,00 |
| Scanner Top5 Btc Guard V1 | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €195,03 | €390,06 | €46,81 | €0,00 |
| Scanner Top5 Btc Guard V1 | ZORA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00942 | 0,00942 | 0,00829 | 0,00476 | 0,01191 | €192,06 | €384,12 | €46,09 | €0,00 |
| Scanner Top5 Btc Guard V1 | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 525,28504 | 525,28504 | 500,95080 | 265,26894 | 578,82035 | €506,36 | €1.012,72 | €46,92 | €0,00 |
| Scanner Top5 Btc Btc Le3 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €847,75 | €1.695,49 | €43,45 | €0,00 |
| Scanner Top5 Btc Btc Le3 V1 | 0G | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,24373 | 0,24373 | 0,21916 | 0,12308 | 0,29778 | €215,80 | €431,60 | €43,51 | €0,00 |
| Scanner Top5 Btc Btc Le3 V1 | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 524,45487 | 524,45487 | 505,31170 | 264,84971 | 566,56985 | €595,92 | €1.191,84 | €43,50 | €0,00 |
| Scanner Top5 Btc Btc Le3 V1 | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,10968 | 0,10968 | 0,10275 | 0,05539 | 0,12491 | €331,20 | €662,40 | €41,83 | €0,00 |
| Scanner Top5 Btc Btc 2 3 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €891,28 | €1.782,56 | €45,68 | €0,00 |
| Scanner Top5 Btc Btc 2 3 V1 | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 522,24443 | 522,24443 | 497,48743 | 263,73344 | 576,70983 | €478,87 | €957,73 | €45,40 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €192,69 | €385,37 | €46,24 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,55551 | 2,55551 | 2,29388 | 1,29053 | 3,13109 | €12,72 | €25,45 | €2,61 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €190,49 | €380,99 | €45,72 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | ZORA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00942 | 0,00942 | 0,00829 | 0,00476 | 0,01191 | €187,59 | €375,19 | €45,02 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 525,28504 | 525,28504 | 500,95080 | 265,26894 | 578,82035 | €494,59 | €989,17 | €45,82 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,55551 | 2,55551 | 2,29388 | 1,29053 | 3,13109 | €12,70 | €25,40 | €2,60 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €191,20 | €382,39 | €45,89 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | PROM | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 7,01991 | 7,01991 | 6,30832 | 3,54505 | 8,58541 | €213,89 | €427,78 | €43,36 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | ZORA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00942 | 0,00942 | 0,00829 | 0,00476 | 0,01191 | €188,34 | €376,68 | €45,20 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 525,28504 | 525,28504 | 500,95080 | 265,26894 | 578,82035 | €485,59 | €971,18 | €44,99 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | ZORA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00942 | 0,00942 | 0,00829 | 0,00476 | 0,01191 | €185,37 | €370,74 | €44,49 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,10968 | 0,10968 | 0,10275 | 0,05539 | 0,12491 | €325,70 | €651,40 | €41,14 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 525,90516 | 525,90516 | 508,26113 | 265,58211 | 564,72203 | €17,51 | €35,02 | €1,17 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | USELESS | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,11026 | 0,11096 | 0,09902 | 0,05568 | 0,13500 | €212,03 | €424,06 | €43,25 | €2,68 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | ENA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15596 | 0,15596 | 0,14889 | 0,07876 | 0,17152 | €13,48 | €26,97 | €1,22 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00176 | €210,95 | €421,90 | €50,63 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1363,81560 | €965,52 | €1.931,04 | €49,49 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01601 | €209,51 | €419,03 | €50,28 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,11110 | 0,11110 | 0,10386 | 0,05611 | 0,13284 | €390,51 | €781,02 | €50,94 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | UNI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 5,69614 | 6,23800 | 6,03348 | 2,87655 | 6,44709 | €25,63 | €51,25 | €0,00 | €4,88 |
| Scanner Top5 Btc Tp3 V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00176 | €211,07 | €422,14 | €50,66 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1363,81560 | €966,09 | €1.932,17 | €49,52 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01601 | €209,64 | €419,27 | €50,31 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,11110 | 0,11110 | 0,10386 | 0,05611 | 0,13284 | €390,74 | €781,47 | €50,97 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | UNI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 5,69614 | 6,23800 | 6,03348 | 2,87655 | 6,44709 | €25,64 | €51,28 | €0,00 | €4,88 |
| Global Confluence puro 1H | DOGE | SHORT | Global Confluence puro | 60m | 2,0x | 0,08170 | 0,08150 | 0,08316 | 0,12214 | 0,07805 | €1.363,98 | €2.727,96 | €48,77 | €6,71 |
| Combo Trend | BEAT | SHORT | Combo Trend | 60m | 2,0x | 0,25984 | 0,25984 | 0,25657 | 0,38847 | 0,19125 | €193,71 | €387,42 | €0,00 | €-0,00 |
| Combo Trend | ADA | SHORT | Combo Trend | 60m | 2,0x | 0,19986 | 0,19986 | 0,20356 | 0,29879 | 0,19173 | €1.205,82 | €2.411,64 | €44,61 | €-0,00 |
| Combo Trend | ETH | SHORT | Combo Trend | 60m | 2,0x | 2415,22686 | 2410,98000 | 2454,83114 | 3610,76415 | 2328,09740 | €14,37 | €28,74 | €0,47 | €0,05 |
| Combo Trend | USELESS | LONG | Combo Trend | 60m | 2,0x | 0,11591 | 0,11096 | 0,10340 | 0,05854 | 0,14343 | €204,72 | €409,44 | €44,18 | €-17,50 |
| Combo Trend | SOL | SHORT | Combo Trend | 60m | 2,0x | 100,01299 | 99,78700 | 101,99785 | 149,51943 | 95,64631 | €20,08 | €40,16 | €0,80 | €0,09 |
| Combo Trend | DOGE | SHORT | Combo Trend | 60m | 2,0x | 0,08148 | 0,08150 | 0,08296 | 0,12181 | 0,07823 | €13,24 | €26,47 | €0,48 | €-0,01 |
| Combo Mean Reversion | ADA | LONG | Combo Mean Reversion | 60m | 2,0x | 0,20284 | 0,20284 | 0,19804 | 0,10244 | 0,21052 | €942,00 | €1.883,99 | €44,59 | €0,00 |
| Combo Mean Reversion | SOL | LONG | Combo Mean Reversion | 60m | 2,0x | 99,81296 | 99,78700 | 98,23262 | 50,40554 | 102,34150 | €1.393,28 | €2.786,55 | €44,12 | €-0,72 |
| Combo Mean Reversion | BTC | LONG | Combo Mean Reversion | 60m | 2,0x | 77237,45440 | 77443,87000 | 76310,60495 | 39004,91447 | 78720,41353 | €1.763,77 | €3.527,53 | €42,33 | €9,43 |
| Combo Mean Reversion | XRP | LONG | Combo Mean Reversion | 60m | 2,0x | 1,33144 | 1,34421 | 1,33864 | 0,67238 | 1,36601 | €1.340,59 | €2.681,19 | €0,00 | €25,72 |
| Combo Scanner | BOME | LONG | Combo Scanner | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €195,20 | €390,40 | €46,85 | €0,00 |
| Combo Scanner | TRUMP | LONG | Combo Scanner | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,14149 | €213,98 | €427,96 | €49,38 | €0,00 |
| Combo Scanner | SKHYNIX | LONG | Combo Scanner | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €24,78 | €49,55 | €1,27 | €0,00 |
| Combo Scanner | XMR | LONG | Combo Scanner | 60m | 2,0x | 527,13541 | 527,13541 | 508,23306 | 266,20338 | 568,72055 | €660,18 | €1.320,37 | €47,35 | €0,00 |
| Combo Scanner | ARB | LONG | Combo Scanner | 60m | 2,0x | 0,11110 | 0,11110 | 0,10386 | 0,05611 | 0,12705 | €377,46 | €754,92 | €49,24 | €0,00 |
| Combo Scanner | ENA | LONG | Combo Scanner | 60m | 2,0x | 0,16057 | 0,16057 | 0,15346 | 0,08109 | 0,17621 | €13,38 | €26,75 | €1,18 | €0,00 |
| Combo Adaptive | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,01735 | 121,01735 | 128,90956 | 180,92093 | 105,23292 | €367,30 | €734,61 | €47,91 | €-0,00 |
| Combo Adaptive | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €40,89 | €81,77 | €3,12 | €0,00 |
| Combo Adaptive | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,52450 | 2,33981 | 1,27487 | 2,89389 | €18,69 | €37,37 | €2,73 | €0,00 |
| Combo Adaptive | 0G | LONG | Combo Adaptive | 60m | 2,0x | 0,23904 | 0,23904 | 0,21329 | 0,12072 | 0,29055 | €230,13 | €460,26 | €49,58 | €0,00 |
| Combo Adaptive | SOL | SHORT | Combo Adaptive | 60m | 2,0x | 99,77304 | 99,78700 | 101,66869 | 149,16070 | 95,98175 | €14,76 | €29,52 | €0,56 | €-0,00 |
| Combo Adaptive | USELESS | LONG | Combo Adaptive | 60m | 2,0x | 0,11008 | 0,11096 | 0,09935 | 0,05559 | 0,13155 | €260,60 | €521,20 | €50,82 | €4,16 |
| Combo Adaptive | UNI | LONG | Combo Adaptive | 60m | 2,0x | 6,13623 | 6,23800 | 5,89727 | 3,09879 | 6,61413 | €13,14 | €26,28 | €1,02 | €0,44 |
| Combo Adaptive Mfe Trail | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €54,29 | €108,58 | €4,15 | €0,00 |
| Combo Adaptive Mfe Trail | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,52450 | 2,33981 | 1,27487 | 2,89389 | €315,75 | €631,50 | €46,20 | €0,00 |
| Combo Adaptive Mfe Trail | TUT | SHORT | Combo Adaptive | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €190,04 | €380,09 | €45,61 | €-0,00 |
| Combo Adaptive Mfe Trail | PROM | LONG | Combo Adaptive | 60m | 2,0x | 7,01991 | 7,01991 | 6,30832 | 3,54505 | 8,44309 | €21,72 | €43,45 | €4,40 | €0,00 |
| Combo Adaptive Mfe Trail | USELESS | LONG | Combo Adaptive | 60m | 2,0x | 0,11591 | 0,11096 | 0,10466 | 0,05854 | 0,13843 | €182,25 | €364,50 | €35,40 | €-15,58 |
| Combo Adaptive Mfe Trail | SOL | SHORT | Combo Adaptive | 60m | 2,0x | 100,01299 | 99,78700 | 101,79936 | 149,51943 | 96,44025 | €23,91 | €47,81 | €0,85 | €0,11 |
| Combo Adaptive Mfe Trail | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,08148 | 0,08150 | 0,08281 | 0,12181 | 0,07882 | €16,73 | €33,46 | €0,55 | €-0,01 |
| Combo Adaptive Quality7 V1 | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €371,68 | €743,36 | €47,16 | €-0,00 |
| Combo Adaptive Quality7 V1 | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €646,78 | €1.293,57 | €49,39 | €0,00 |
| Combo Adaptive Quality7 V1 | ZORA | LONG | Combo Adaptive | 60m | 2,0x | 0,00942 | 0,00942 | 0,00829 | 0,00476 | 0,01169 | €199,23 | €398,46 | €47,81 | €0,00 |
| Combo Adaptive Quality7 V1 | 0G | LONG | Combo Adaptive | 60m | 2,0x | 0,24605 | 0,24605 | 0,22046 | 0,12425 | 0,29722 | €220,81 | €441,63 | €45,92 | €0,00 |
| Combo Adaptive Regime V1 | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €987,06 | €1.974,12 | €49,09 | €0,00 |
| Combo Adaptive Long Only V1 | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €645,48 | €1.290,95 | €46,47 | €0,00 |
| Combo Adaptive Long Only V1 | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,52450 | 2,33981 | 1,27487 | 2,89389 | €48,12 | €96,24 | €7,04 | €0,00 |
| Combo Adaptive Long Only V1 | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1331,36020 | €968,99 | €1.937,97 | €49,66 | €0,00 |
| Combo Adaptive Long Only V1 | HEMI | LONG | Combo Adaptive | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €216,09 | €432,18 | €51,86 | €0,00 |
| Combo Adaptive Long Only V1 | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,11110 | 0,11110 | 0,10386 | 0,05611 | 0,12560 | €400,65 | €801,31 | €52,27 | €0,00 |
| Combo Adaptive Partial 1R V1 | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,01735 | 121,01735 | 128,90956 | 180,92093 | 105,23292 | €352,70 | €705,40 | €46,00 | €-0,00 |
| Combo Adaptive Partial 1R V1 | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,52450 | 2,33981 | 1,27487 | 2,89389 | €347,19 | €694,38 | €50,80 | €0,00 |
| Combo Adaptive Partial 1R V1 | VELVET | SHORT | Combo Adaptive | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €207,76 | €415,52 | €0,00 | €-0,00 |
| Combo Adaptive Partial 1R V1 | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €1.013,20 | €2.026,40 | €50,39 | €0,00 |
| Combo Adaptive Partial 1R V1 | USELESS | LONG | Combo Adaptive | 60m | 2,0x | 0,11591 | 0,11096 | 0,10466 | 0,05854 | 0,13843 | €21,83 | €43,65 | €4,24 | €-1,87 |
| Combo Adaptive Runner25 V1 | 0G | LONG | Combo Adaptive | 60m | 2,0x | 0,23904 | 0,23904 | 0,21329 | 0,12072 | 0,31630 | €204,19 | €408,39 | €43,99 | €0,00 |
| Combo Adaptive Runner25 V1 | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,10968 | 0,10968 | 0,10275 | 0,05539 | 0,13046 | €350,40 | €700,80 | €44,26 | €0,00 |
| Combo Adaptive Runner25 V1 | UNI | LONG | Combo Adaptive | 60m | 2,0x | 5,69614 | 6,23800 | 6,04873 | 2,87655 | 6,44709 | €505,26 | €1.010,52 | €0,00 | €96,13 |
| Combo Adaptive Runner25 V1 | SOL | SHORT | Combo Adaptive | 60m | 2,0x | 99,61607 | 99,78700 | 101,40716 | 148,92603 | 94,24282 | €20,98 | €41,95 | €0,75 | €-0,07 |
| Combo Adaptive Runner25 V1 | PEPE | SHORT | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00001 | 0,00000 | €14,42 | €28,84 | €0,64 | €-0,24 |
| Combo Adaptive Runner25 V1 | USELESS | LONG | Combo Adaptive | 60m | 2,0x | 0,11079 | 0,11096 | 0,10052 | 0,05595 | 0,14161 | €240,28 | €480,55 | €44,56 | €0,73 |
| Combo Adaptive Tp3 V1 | 0G | LONG | Combo Adaptive | 60m | 2,0x | 0,23904 | 0,23904 | 0,21329 | 0,12072 | 0,31630 | €200,38 | €400,76 | €43,17 | €0,00 |
| Combo Adaptive Tp3 V1 | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,10968 | 0,10968 | 0,10275 | 0,05539 | 0,13046 | €343,85 | €687,70 | €43,43 | €0,00 |
| Combo Adaptive Tp3 V1 | UNI | LONG | Combo Adaptive | 60m | 2,0x | 5,69614 | 6,23800 | 6,04873 | 2,87655 | 6,44709 | €495,82 | €991,64 | €0,00 | €94,33 |
| Combo Adaptive Tp3 V1 | SOL | SHORT | Combo Adaptive | 60m | 2,0x | 99,61607 | 99,78700 | 101,40716 | 148,92603 | 94,24282 | €20,58 | €41,17 | €0,74 | €-0,07 |
| Combo Adaptive Tp3 V1 | PEPE | SHORT | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00001 | 0,00000 | €14,15 | €28,30 | €0,63 | €-0,23 |
| Combo Adaptive Tp3 V1 | USELESS | LONG | Combo Adaptive | 60m | 2,0x | 0,11079 | 0,11096 | 0,10052 | 0,05595 | 0,14161 | €235,79 | €471,58 | €43,73 | €0,71 |
| Btc Ema 1H | BTC | SHORT | Trend following EMA | 60m | 3,0x | 77303,06629 | 77443,87000 | 78416,23045 | 102684,23973 | 75076,73798 | €1.107,32 | €3.321,96 | €47,84 | €-6,05 |
| Btc Donchian 1H | BTC | SHORT | Donchian breakout 20 barre | 60m | 3,0x | 77206,56560 | 77443,87000 | 78194,80964 | 102556,05464 | 75230,07752 | €1.289,36 | €3.868,07 | €49,51 | €-11,89 |
| Btc Bollinger 4H | BTC | SHORT | Bollinger mean reversion | 240m | 2,0x | 80323,10217 | 77443,87000 | 78401,16314 | 120083,03774 | 75648,94663 | €775,58 | €1.551,16 | €0,00 | €55,60 |
| Sol Ema 1H | SOL | SHORT | Trend following EMA | 60m | 3,0x | 99,77304 | 99,78700 | 101,66869 | 132,53186 | 95,98175 | €888,04 | €2.664,11 | €50,62 | €-0,37 |
| Sol Donchian 1H | SOL | SHORT | Donchian breakout 20 barre | 60m | 3,0x | 99,77304 | 99,78700 | 101,45806 | 132,53186 | 96,40301 | €1.019,77 | €3.059,30 | €51,67 | €-0,43 |
| Sol Donchian 4H | SOL | LONG | Donchian breakout 20 barre | 240m | 2,0x | 104,08581 | 99,78700 | 98,18471 | 52,56334 | 120,60890 | €449,62 | €899,24 | €50,98 | €-37,14 |
| Sol Bollinger 1H | SOL | LONG | Bollinger mean reversion | 60m | 3,0x | 99,81296 | 99,78700 | 98,23262 | 67,04104 | 102,18346 | €1.037,93 | €3.113,80 | €49,30 | €-0,81 |
| Sol Bollinger 4H | SOL | SHORT | Bollinger mean reversion | 240m | 2,0x | 107,28254 | 99,78700 | 102,35930 | 160,38740 | 97,27311 | €478,97 | €957,94 | €0,00 | €66,93 |
| Sol Adaptive 1H | SOL | SHORT | Combo Adaptive | 60m | 3,0x | 99,77304 | 99,78700 | 101,66869 | 132,53186 | 95,98175 | €877,49 | €2.632,47 | €50,02 | €-0,37 |
| Eth Ema 1H | ETH | SHORT | Trend following EMA | 60m | 3,0x | 2415,22686 | 2410,98000 | 2450,87073 | 3208,22634 | 2343,93912 | €1.098,91 | €3.296,73 | €48,65 | €5,80 |
| Doge Bollinger 1H | DOGE | LONG | Bollinger mean reversion | 60m | 3,0x | 0,08061 | 0,08150 | 0,08077 | 0,05414 | 0,08229 | €1.204,04 | €3.612,13 | €0,00 | €39,96 |
| Master Adaptive V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99403 | 639,55695 | 1331,36019 | €22,75 | €45,50 | €1,17 | €0,00 |
| Master Adaptive V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €195,57 | €391,15 | €46,94 | €0,00 |
| Master Adaptive V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,20498 | 0,11491 | 0,27267 | €236,54 | €473,08 | €46,91 | €0,00 |
| Master Adaptive V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 520,62410 | 520,62410 | 498,16818 | 262,91517 | 565,53595 | €529,71 | €1.059,43 | €45,70 | €0,00 |
| Master Adaptive V1 | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,10968 | 0,10968 | 0,10275 | 0,05539 | 0,12353 | €364,80 | €729,60 | €46,08 | €0,00 |
| Master Adaptive No Alt V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1255,10261 | 1255,10261 | 1225,12158 | 633,82682 | 1315,06467 | €19,09 | €38,19 | €0,91 | €0,00 |
| Master Adaptive No Alt V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €183,81 | €367,62 | €44,11 | €0,00 |
| Master Adaptive No Alt V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 514,40286 | 514,40286 | 493,14790 | 259,77344 | 556,91277 | €554,63 | €1.109,27 | €45,83 | €0,00 |
| Master Adaptive No Alt V1 | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,10968 | 0,10968 | 0,10275 | 0,05539 | 0,12353 | €359,36 | €718,72 | €45,39 | €0,00 |
| Master Adaptive No Alt V1 | ENA | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,16077 | 0,16077 | 0,15357 | 0,08119 | 0,17517 | €14,18 | €28,36 | €1,27 | €0,00 |
| Master Adaptive No Alt V1 | USELESS | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,11098 | 0,11096 | 0,10103 | 0,05605 | 0,13089 | €253,05 | €506,09 | €45,40 | €-0,10 |
| Master Adaptive Strict3 V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €178,16 | €356,31 | €42,76 | €0,00 |
| Master Adaptive Strict3 V1 | PROM | LONG | Master Adaptive Consensus | 60m | 2,0x | 7,01991 | 7,01991 | 6,30832 | 3,54505 | 8,44309 | €215,49 | €430,99 | €43,69 | €0,00 |
| Master Adaptive Strict3 V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,24076 | 0,24076 | 0,21579 | 0,12159 | 0,29071 | €209,83 | €419,66 | €43,53 | €0,00 |
| Master Adaptive Strict3 V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 524,22482 | 524,22482 | 504,57786 | 264,73354 | 563,51875 | €580,65 | €1.161,30 | €43,52 | €0,00 |
| Master Adaptive Expanded V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03814 | 0,02188 | 0,05374 | €197,50 | €395,01 | €47,40 | €0,00 |
| Master Adaptive Expanded V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1261,89668 | 1261,89668 | 1231,08309 | 637,25783 | 1323,52387 | €934,21 | €1.868,43 | €45,62 | €0,00 |
| Master Adaptive Expanded V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01194 | 0,01194 | 0,01050 | 0,00603 | 0,01480 | €195,34 | €390,67 | €46,88 | €0,00 |
| Master Adaptive Expanded V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,20498 | 0,11491 | 0,27267 | €236,25 | €472,49 | €46,85 | €0,00 |
| Master Adaptive Gb20 V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99403 | 639,55695 | 1331,36019 | €22,45 | €44,90 | €1,15 | €0,00 |
| Master Adaptive Gb20 V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €193,03 | €386,06 | €46,33 | €0,00 |
| Master Adaptive Gb20 V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,20498 | 0,11491 | 0,27267 | €233,42 | €466,83 | €46,29 | €0,00 |
| Master Adaptive Gb20 V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 520,62410 | 520,62410 | 498,16818 | 262,91517 | 565,53595 | €522,62 | €1.045,25 | €45,08 | €0,00 |
| Master Adaptive Gb20 V1 | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,10968 | 0,10968 | 0,10275 | 0,05539 | 0,12353 | €359,99 | €719,98 | €45,47 | €0,00 |
| Master Adaptive Runner25 V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03814 | 0,02188 | 0,05894 | €34,77 | €69,54 | €8,34 | €0,00 |
| Master Adaptive Runner25 V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1255,10261 | 1255,10261 | 1225,12158 | 633,82682 | 1345,04570 | €27,05 | €54,10 | €1,29 | €0,00 |
| Master Adaptive Runner25 V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01601 | €185,86 | €371,72 | €44,61 | €0,00 |
| Master Adaptive Runner25 V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,20498 | 0,11491 | 0,29523 | €233,84 | €467,69 | €46,37 | €0,00 |
| Master Adaptive Runner25 V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 520,62410 | 520,62410 | 498,16818 | 262,91517 | 587,99187 | €446,15 | €892,30 | €38,49 | €0,00 |
| Master Adaptive Runner25 V1 | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,10968 | 0,10968 | 0,10275 | 0,05539 | 0,13046 | €360,46 | €720,91 | €45,53 | €0,00 |
| Combo Adaptive Side Regime Guard V1 | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €77,52 | €155,04 | €5,58 | €0,00 |
| Combo Adaptive Side Regime Guard V1 | VELVET | SHORT | Combo Adaptive | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €216,61 | €433,23 | €0,00 | €-0,00 |
| Combo Adaptive Side Regime Guard V1 | TUT | SHORT | Combo Adaptive | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €192,40 | €384,79 | €46,18 | €-0,00 |
| Combo Adaptive Side Regime Guard V1 | USELESS | LONG | Combo Adaptive | 60m | 2,0x | 0,11008 | 0,11096 | 0,09935 | 0,05559 | 0,13155 | €237,09 | €474,18 | €46,23 | €3,78 |
| Combo Adaptive Side Regime Guard V1 | UNI | LONG | Combo Adaptive | 60m | 2,0x | 6,23925 | 6,23800 | 5,98083 | 3,15082 | 6,75608 | €596,36 | €1.192,72 | €49,40 | €-0,24 |
| Master Adaptive Gb20 Be V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99403 | 639,55695 | 1331,36019 | €22,86 | €45,73 | €1,17 | €0,00 |
| Master Adaptive Gb20 Be V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €196,54 | €393,08 | €47,17 | €0,00 |
| Master Adaptive Gb20 Be V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,20498 | 0,11491 | 0,27267 | €237,71 | €475,42 | €47,14 | €0,00 |
| Master Adaptive Gb20 Be V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 520,62410 | 520,62410 | 498,16818 | 262,91517 | 565,53595 | €532,34 | €1.064,67 | €45,92 | €0,00 |
| Master Adaptive Gb20 Be V1 | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,10968 | 0,10968 | 0,10275 | 0,05539 | 0,12353 | €366,61 | €733,22 | €46,31 | €0,00 |
| Master Adaptive Gb20 Partial V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99403 | 639,55695 | 1331,36019 | €22,84 | €45,68 | €1,17 | €0,00 |
| Master Adaptive Gb20 Partial V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €196,33 | €392,67 | €47,12 | €0,00 |
| Master Adaptive Gb20 Partial V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,20498 | 0,11491 | 0,27267 | €237,46 | €474,91 | €47,09 | €0,00 |
| Master Adaptive Gb20 Partial V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 520,62410 | 520,62410 | 498,16818 | 262,91517 | 565,53595 | €531,77 | €1.063,54 | €45,87 | €0,00 |
| Master Adaptive Gb20 Partial V1 | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,10968 | 0,10968 | 0,10275 | 0,05539 | 0,12353 | €366,22 | €732,44 | €46,26 | €0,00 |
| Master Adaptive Gb20 Loss Cap V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03828 | 0,02188 | 0,05682 | €195,70 | €391,41 | €45,67 | €0,00 |
| Master Adaptive Gb20 Loss Cap V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01069 | 0,00594 | 0,01465 | €210,34 | €420,68 | €38,67 | €0,00 |
| Master Adaptive Gb20 Loss Cap V1 | PROM | LONG | Master Adaptive Consensus | 60m | 2,0x | 7,01991 | 7,01991 | 6,48622 | 3,54505 | 8,44309 | €34,75 | €69,51 | €5,28 | €0,00 |
| Master Adaptive Gb20 Loss Cap V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,21062 | 0,11491 | 0,27267 | €309,65 | €619,30 | €46,05 | €0,00 |
| Master Adaptive Gb20 Loss Cap V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 514,40286 | 514,40286 | 498,46164 | 259,77344 | 556,91277 | €32,91 | €65,81 | €2,04 | €0,00 |
| Master Adaptive Gb20 Loss Cap V1 | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,10968 | 0,10968 | 0,10448 | 0,05539 | 0,12353 | €480,15 | €960,31 | €45,49 | €0,00 |
| 1H Fast V3 Nohigh Range Only V1 | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,20283 | 0,20283 | 0,20750 | 0,26943 | 0,19582 | €740,69 | €2.222,07 | €51,20 | €-0,00 |
| 1H Fast V3 Nohigh Range Only V1 | ARB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,10878 | 0,10878 | 0,10318 | 0,07307 | 0,11718 | €330,06 | €990,17 | €50,95 | €0,00 |
| 1H Fast V3 Nohigh Range Only V1 | ENA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16057 | 0,16057 | 0,15504 | 0,10785 | 0,16887 | €493,88 | €1.481,64 | €51,02 | €0,00 |
| 1H Fast V3 Nohigh Regime Guard V1 | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €140,84 | €422,53 | €50,70 | €-0,00 |
| 1H Fast V3 Nohigh Regime Guard V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €143,15 | €429,46 | €50,70 | €-0,00 |
| 1H Fast V3 Nohigh Regime Guard V1 | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,20283 | 0,20283 | 0,20750 | 0,26943 | 0,19582 | €34,57 | €103,71 | €2,39 | €-0,00 |
| 1H Fast V3 Nohigh Regime Guard V1 | ARB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,10991 | 0,10991 | 0,10432 | 0,07382 | 0,11829 | €333,52 | €1.000,56 | €50,87 | €0,00 |
| 1H Fast V3 Nohigh Regime Guard V1 | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 77206,56560 | 77443,87000 | 78071,27913 | 102556,05464 | 75909,49530 | €1.508,59 | €4.525,78 | €50,69 | €-13,91 |
| Main Side Regime Guard V1 | VELVET | LONG | Confluenza trend | 240m | 3,0x | 0,55987 | 0,55987 | 0,49269 | 0,37605 | 0,69424 | €142,25 | €426,74 | €51,21 | €0,00 |
| Main Side Regime Guard V1 | AKE | LONG | Confluenza trend | 240m | 3,0x | 0,01021 | 0,01021 | 0,00899 | 0,00686 | 0,01266 | €145,97 | €437,90 | €52,55 | €0,00 |
| Main Side Regime Guard V1 | XRP | LONG | Confluenza trend | 240m | 3,0x | 1,47102 | 1,34421 | 1,31178 | 0,98804 | 1,78951 | €12,77 | €38,31 | €4,15 | €-3,30 |
| Main Side Regime Guard V1 | ETH | LONG | Confluenza trend | 240m | 3,0x | 2437,91749 | 2410,98000 | 2326,72117 | 1637,46791 | 2660,31012 | €9,94 | €29,83 | €1,36 | €-0,33 |
| Main Side Regime Guard V1 | ENA | LONG | Confluenza trend | 240m | 3,0x | 0,16108 | 0,16108 | 0,14175 | 0,10819 | 0,19974 | €150,44 | €451,33 | €54,16 | €0,00 |
| Main Side Regime Guard V1 | ZEC | LONG | Confluenza trend | 240m | 3,0x | 852,88054 | 835,72000 | 799,15184 | 572,85143 | 960,33794 | €290,60 | €871,79 | €54,92 | €-17,54 |
| Main Dynamic Asset Selector V1 | ENA | LONG | Confluenza trend | 240m | 3,0x | 0,16108 | 0,16108 | 0,14175 | 0,10819 | 0,19974 | €140,98 | €422,93 | €50,75 | €0,00 |
| Combo Trend Side Regime Guard V1 | VELVET | SHORT | Combo Trend | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,12693 | €217,86 | €435,73 | €0,00 | €-0,00 |
| Combo Trend Side Regime Guard V1 | TUT | SHORT | Combo Trend | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03364 | €12,81 | €25,62 | €3,07 | €-0,00 |
| Combo Trend Side Regime Guard V1 | SUI | SHORT | Combo Trend | 60m | 2,0x | 0,71926 | 0,72140 | 0,73823 | 1,07529 | 0,67752 | €1.029,16 | €2.058,32 | €54,29 | €-6,14 |
| Combo Trend Side Regime Guard V1 | DOGE | SHORT | Combo Trend | 60m | 2,0x | 0,08277 | 0,08150 | 0,08184 | 0,12375 | 0,07926 | €1.329,20 | €2.658,40 | €0,00 | €40,90 |
| Combo Trend Side Regime Guard V1 | UNI | LONG | Combo Trend | 60m | 2,0x | 5,77916 | 6,23800 | 6,03540 | 2,91847 | 6,35335 | €12,69 | €25,39 | €0,00 | €2,02 |
| Combo Trend Side Regime Guard V1 | USELESS | LONG | Combo Trend | 60m | 2,0x | 0,11008 | 0,11096 | 0,09816 | 0,05559 | 0,13632 | €249,64 | €499,29 | €54,09 | €3,98 |
| 1H Fast Nohigh Cap75 Short Only V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €135,82 | €407,46 | €48,90 | €-0,00 |
| 1H Fast Nohigh Cap75 Short Only V1 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €138,05 | €414,14 | €48,89 | €-0,00 |
| 1H Fast Nohigh Cap75 Short Only V1 | XMR | LONG | Momentum / breakout | 60m | 3,0x | 527,13541 | 527,13541 | 512,43358 | 354,05928 | 549,18814 | €571,22 | €1.713,65 | €47,79 | €0,00 |
| 1H Fast Nohigh Cap75 Short Only V1 | ENA | LONG | Momentum / breakout | 60m | 3,0x | 0,16057 | 0,16057 | 0,15504 | 0,10785 | 0,16887 | €460,31 | €1.380,94 | €47,56 | €0,00 |
| 1H Balanced V3 Long Only V1 | SKHYNIX | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1220,85412 | 1220,85412 | 1177,63561 | 820,00702 | 1307,29117 | €435,49 | €1.306,46 | €46,25 | €0,00 |
| 1H Balanced V3 Long Only V1 | ADA | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,20138 | 0,20138 | 0,20719 | 0,26750 | 0,18976 | €529,53 | €1.588,58 | €45,82 | €-0,00 |
| 1H Balanced V3 Long Only V1 | USELESS | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,11591 | 0,11096 | 0,10466 | 0,07786 | 0,13843 | €152,34 | €457,03 | €44,39 | €-19,53 |
| 1H Balanced V3 Long Only V1 | BTC | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 76920,91274 | 77443,87000 | 78028,57388 | 102176,61242 | 74705,59045 | €1.029,72 | €3.089,16 | €44,48 | €-21,00 |
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
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | UNI | LONG | 2026-09-02T04:45:00+00:00 | 6,22173 | €90,39 | 2,16 | TARGET |
| Forza relativa 1H V2 | UNI | LONG | 2026-09-02T04:45:00+00:00 | 6,27314 | €104,19 | 2,16 | TARGET |
| Forza relativa 1H V1 | UNI | LONG | 2026-09-02T04:45:00+00:00 | 6,22173 | €89,83 | 2,16 | TARGET |
| Benchmark trend following EMA 1H | UNI | LONG | 2026-09-02T04:45:00+00:00 | 6,32649 | €89,82 | 2,16 | TARGET |
| Combo Trend | UNI | LONG | 2026-09-02T04:45:00+00:00 | 6,32649 | €95,94 | 2,16 | TARGET |
| Combo Scanner | UNI | LONG | 2026-09-02T04:45:00+00:00 | 6,24559 | €3,77 | 2,16 | TARGET |
| Combo Adaptive Mfe Trail | UNI | LONG | 2026-09-02T04:45:00+00:00 | 6,22949 | €86,11 | 1,96 | TARGET |
| 1H Fast V3 Nohigh Range Only V1 | UNI | LONG | 2026-09-02T04:45:00+00:00 | 6,25777 | €1,43 | 1,45 | TARGET |
| Rapida 1H V2 | UNI | LONG | 2026-09-02T04:45:00+00:00 | 6,25777 | €74,22 | 1,45 | TARGET |
| Bilanciata 1H V2 | BTR | SHORT | 2026-09-02T04:45:00+00:00 | 0,09089 | €-0,21 | -0,00 | STOP_STRESS_SLIPPAGE |
| Scanner Top20 Long | UNI | LONG | 2026-09-02T04:15:00+00:00 | 6,19554 | €97,13 | 1,96 | TARGET |
| Scanner Top15 Long | UNI | LONG | 2026-09-02T04:15:00+00:00 | 6,19554 | €97,13 | 1,96 | TARGET |

## Regole invarianti

- Nessuna martingala e nessuna mediazione automatica in perdita.
- Il target mensile riduce il rischio quando viene avvicinato o raggiunto; non lo aumenta mai.
- Il portafoglio principale e le simulazioni di confronto hanno contabilità separata.
- Commissioni, slippage e funding sono inclusi nella simulazione secondo i parametri configurati.
- Quando stop e target risultano toccati nella stessa candela, prevale lo stop salvo modifica esplicita della configurazione.
