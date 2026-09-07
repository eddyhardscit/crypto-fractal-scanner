# Paper trading automatico KuCoin

Generato: 2026-09-07T05:33:13+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-09-07T05:05:32+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-09-07T05:05:32+00:00 | 2026-09-07T05:05:32+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-09-07T04:45:00+00:00 | 2026-09-07T04:45:00+00:00 | 5,8 min | 25,0 min | OK |
| 60m | 12 | 2026-09-07T04:00:00+00:00 | 2026-09-07T04:00:00+00:00 | 5,8 min | 45,0 min | OK |
| 240m | 12 | 2026-09-07T00:00:00+00:00 | 2026-09-07T00:00:00+00:00 | 1,10 h | 1,00 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1H Fast V3 Nohigh Range Only V1 | TAO | 60m | LONG | 7,75 | 4,50 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive Side Regime Guard V1 | TAO | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Master Adaptive Strict3 V1 | TAO | 60m | LONG | 7,75 | 0,00 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | TAO | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top10 Long | NEAR | 60m | LONG | 6,25 | 5,00 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 No Esports Mfe Lock V1 | ZEC | 60m | LONG | 6,25 | 4,50 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida 1H V3 Filtered | ZEC | 60m | LONG | 6,25 | 4,50 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Balanced Long No Rhv V1 | NEAR | 60m | LONG | 6,25 | 5,00 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Principale 4H | TAO | 240m | LONG | 6,75 | 6,00 | 0,00 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.8 minuti; tolleranza 60 minuti. |
| Principale 4H | UNI | 240m | LONG | 6,25 | 6,00 | 0,00 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.8 minuti; tolleranza 60 minuti. |
| Principale 4H | ETH | 240m | LONG | 5,24 | 6,00 | 0,76 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.8 minuti; tolleranza 60 minuti. |
| Principale 4H | HYPE | 240m | LONG | 4,16 | 6,00 | 1,84 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.8 minuti; tolleranza 60 minuti. |
| Principale 4H | SOL | 240m | LONG | 4,03 | 6,00 | 1,97 | STALE_CANDLE | 1,10 h | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.8 minuti; tolleranza 60 minuti. |
| Principale 4H | DOGE | 240m | LONG | 3,14 | 6,00 | 2,86 | STALE_CANDLE | 1,10 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.8 minuti; tolleranza 60 minuti. |
| Principale 4H | XRP | 240m | LONG | 1,36 | 6,00 | 4,64 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.8 minuti; tolleranza 60 minuti. |
| Principale 4H | BTC | 240m | LONG | 0,50 | 6,00 | 5,50 | STALE_CANDLE | 1,10 h | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.8 minuti; tolleranza 60 minuti. |
| Bilanciata 1H V1 | TAO | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Bilanciata 1H V2 | TAO | 60m | LONG | 7,75 | 5,50 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Tp2 V1 | TAO | 60m | LONG | 7,75 | 4,50 | 0,00 | READY | 5,8 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Fast V3 Nohigh V1 | TAO | 60m | LONG | 7,75 | 4,50 | 0,00 | READY | 5,8 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Fast V3 No Esports Long Only V1 | TAO | 60m | LONG | 7,75 | 4,50 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 No Esports Stress Guard V1 | TAO | 60m | LONG | 7,75 | 4,50 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Forza relativa 1H V1 | TAO | 60m | LONG | 7,75 | 4,00 | 0,00 | READY | 5,8 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Forza relativa 1H V2 | TAO | 60m | LONG | 7,75 | 5,50 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Benchmark trend following EMA 1H | TAO | 60m | LONG | 7,75 | 5,00 | 0,00 | READY | 5,8 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Scanner Top 5 Long 1H | TAO | 60m | LONG | 7,75 | 5,00 | 0,00 | READY | 5,8 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Scanner Top 5 + forza BTC 1H | TAO | 60m | LONG | 7,75 | 5,00 | 0,00 | READY | 5,8 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Scanner Top5 Btc Mfe V1 | TAO | 60m | LONG | 7,75 | 5,00 | 0,00 | READY | 5,8 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.816,71 | -1,83% | €8,15 | €3.000,00 | 0,27% | 5 | 60 | 41,67% | 0,88 | 6,86% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 60 | 3170 | PRIME INDICAZIONI | 100 (mancano 40) |

- Trade del Principale 4H chiusi: **60**; win rate **41,67%**; profit factor **0,88**.
- Expectancy: **€-3,05** per trade; P&L netto: **€-182,77**; max drawdown: **6,86%**.
- Valutazione: **Si può osservare la direzione, ma il risultato resta fragile.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 5 | €9.816,71 | €700,63 | €2.101,90 | €196,32 | €0,56 |
| TEST | Benchmark Donchian breakout 1H | 6 | €11.553,24 | €3.519,85 | €7.039,69 | €226,86 | €20,87 |
| TEST | Donchian 1H Gb20 120R V1 | 6 | €11.281,23 | €3.436,97 | €6.873,95 | €221,52 | €20,38 |
| TEST | Scanner Top 5 Long 1H | 7 | €11.240,58 | €1.431,12 | €2.862,24 | €226,81 | €281,77 |
| TEST | Main Side Regime Guard V1 | 6 | €11.183,96 | €628,60 | €1.885,81 | €223,51 | €8,47 |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | 6 | €11.090,92 | €716,47 | €2.149,41 | €167,48 | €21,35 |
| TEST | Combo Adaptive Long Only V1 | 9 | €11.038,39 | €2.472,42 | €4.944,83 | €223,40 | €484,84 |
| TEST | Combo Trend Side Regime Guard V1 | 8 | €11.036,19 | €1.496,97 | €2.993,94 | €170,70 | €235,98 |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | 5 | €10.744,26 | €2.373,95 | €7.121,85 | €213,34 | €29,44 |
| TEST | Scanner Top15 Long | 9 | €10.705,85 | €2.026,14 | €4.052,27 | €215,77 | €298,19 |
| TEST | Scanner Top20 Long | 9 | €10.705,85 | €2.026,14 | €4.052,27 | €215,77 | €298,19 |
| TEST | Combo Adaptive | 8 | €10.645,54 | €1.392,20 | €2.784,40 | €163,09 | €270,51 |
| TEST | Scanner Top10 Long | 8 | €10.623,32 | €2.420,01 | €4.840,03 | €212,47 | €407,56 |
| TEST | Rapida 1H V2 | 1 | €10.621,79 | €749,31 | €2.247,94 | €51,80 | €0,00 |
| TEST | 1H Fast No Pepe V1 | 7 | €10.593,78 | €1.338,00 | €4.014,01 | €211,55 | €16,17 |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | 6 | €10.584,54 | €1.600,08 | €4.800,25 | €211,69 | €187,56 |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | 7 | €10.557,76 | €1.019,18 | €3.057,55 | €160,55 | €28,16 |
| TEST | Scanner Top 5 + forza BTC 1H | 7 | €10.531,31 | €1.170,86 | €2.341,73 | €211,83 | €266,57 |
| TEST | Combo Scanner | 7 | €10.528,06 | €1.538,63 | €3.077,25 | €211,77 | €246,47 |
| TEST | Rapida 1H V3 Filtered | 6 | €10.516,54 | €1.589,80 | €4.769,41 | €210,33 | €186,36 |
| TEST | Scanner Top5 Btc Tp3 V1 | 6 | €10.315,19 | €1.981,44 | €3.962,88 | €205,93 | €39,63 |
| TEST | Scanner Top5 Btc Runner25 V1 | 6 | €10.309,15 | €1.980,28 | €3.960,56 | €205,81 | €39,60 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 0 | €10.300,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Donchian 1H | 0 | €10.293,89 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 0 | €10.271,73 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 No Esports Long Only V1 | 8 | €10.245,85 | €1.002,78 | €3.008,34 | €204,92 | €20,86 |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 0 | €10.239,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Nohigh Range Only V1 | 6 | €10.238,74 | €1.851,73 | €5.555,19 | €156,02 | €52,05 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 0 | €10.235,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Main Dynamic Asset Selector V1 | 2 | €10.210,22 | €344,54 | €1.033,63 | €101,76 | €9,25 |
| TEST | Btc Bollinger 1H | 0 | €10.209,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Ampia 4H | 9 | €10.198,96 | €1.023,36 | €2.046,73 | €203,96 | €5,38 |
| TEST | Sol Adaptive 4H | 1 | €10.189,10 | €613,63 | €1.227,27 | €50,96 | €-1,35 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 0 | €10.185,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Side Regime Guard V1 | 9 | €10.166,48 | €1.157,98 | €2.315,96 | €104,41 | €264,78 |
| TEST | 1H Fast Score 6 75 Range Only V1 | 4 | €10.155,20 | €1.531,50 | €4.594,51 | €152,42 | €25,46 |
| TEST | Sol Donchian 4H | 1 | €10.155,15 | €574,98 | €1.149,96 | €50,72 | €11,27 |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 0 | €10.145,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 0 | €10.099,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 4H | 1 | €10.093,26 | €985,68 | €1.971,36 | €50,34 | €25,68 |
| TEST | 1H Fast V3 Long Only V1 | 6 | €10.087,82 | €1.310,73 | €3.932,19 | €196,71 | €196,11 |
| TEST | Doge Donchian 1H | 0 | €10.066,52 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 1H | 1 | €10.051,27 | €1.165,90 | €3.497,71 | €50,37 | €-19,54 |
| TEST | Combo Adaptive Partial 1R V1 | 5 | €10.050,43 | €1.946,29 | €3.892,58 | €151,20 | €-2,73 |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 0 | €10.048,77 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Tp2 V1 | 6 | €10.048,74 | €598,29 | €1.794,87 | €150,72 | €-2,10 |
| TEST | Rapida 1H V1 | 0 | €10.043,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 4H | 1 | €10.042,02 | €667,02 | €1.334,05 | €50,29 | €-14,78 |
| TEST | 1H Balanced Short Trend Down Strict V1 | 0 | €10.035,46 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · prudente · 5x | 0 | €10.032,32 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €50 · 15x | 0 | €10.022,70 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €10.014,08 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €50 · 15x | 0 | €10.009,44 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 0 | €10.008,92 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €10 · 15x | 0 | €10.004,54 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 0 | €10.003,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 0 | €10.002,82 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €10 · 15x | 0 | €10.001,89 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Continuation V1 | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €10 · 15x | 0 | €9.998,68 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €10 · 15x | 0 | €9.997,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · prudente · 5x | 0 | €9.996,83 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 0 | €9.995,23 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 4H | 1 | €9.994,27 | €817,27 | €1.634,54 | €50,09 | €-21,94 |
| TEST | Scalp RSI Long 20 · €50 · 15x | 0 | €9.993,42 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Ema 1H | 0 | €9.989,46 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €50 · 15x | 0 | €9.988,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €10 · 15x | 0 | €9.987,54 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 1H | 1 | €9.987,29 | €1.158,48 | €3.475,45 | €50,05 | €-19,41 |
| TEST | Sol Bollinger 4H | 0 | €9.980,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · prudente · 5x | 0 | €9.980,94 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Bollinger 1H | 0 | €9.979,42 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 1H | 0 | €9.968,58 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 0 | €9.963,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Gb20 Be V1 | 7 | €9.959,49 | €1.520,36 | €3.040,71 | €200,33 | €276,93 |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | 0 | €9.959,32 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Gb20 Partial V1 | 7 | €9.948,90 | €1.518,74 | €3.037,48 | €200,11 | €276,64 |
| TEST | Scanner Top5 Btc Guard V1 | 7 | €9.947,39 | €1.075,40 | €2.150,81 | €199,99 | €249,95 |
| TEST | Btc Ema 4H | 1 | €9.941,56 | €887,05 | €1.774,10 | €49,83 | €-23,81 |
| TEST | Scalp RSI Short 80 · prudente · 5x | 0 | €9.939,55 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €50 · 15x | 0 | €9.937,70 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | 6 | €9.930,97 | €1.021,43 | €3.064,29 | €198,11 | €26,30 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.917,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive V1 | 7 | €9.910,42 | €1.512,86 | €3.025,73 | €199,34 | €275,57 |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | 5 | €9.903,76 | €1.275,14 | €3.825,42 | €192,09 | €24,63 |
| TEST | Btc Donchian 1H | 0 | €9.897,46 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 4H | 1 | €9.888,37 | €882,31 | €1.764,61 | €49,57 | €-23,68 |
| TEST | Eth Ema 4H | 1 | €9.887,35 | €690,19 | €1.380,39 | €49,44 | €1,44 |
| TEST | 1H Fast V3 Nohigh V1 | 5 | €9.882,55 | €1.233,36 | €3.700,08 | €197,60 | €2,42 |
| TEST | Master Adaptive Runner25 V1 | 9 | €9.873,79 | €1.584,35 | €3.168,69 | €199,15 | €319,70 |
| TEST | Scanner Top5 Btc Mfe V1 | 7 | €9.872,59 | €1.097,63 | €2.195,25 | €198,58 | €249,90 |
| TEST | Forza relativa 1H V2 | 6 | €9.839,17 | €842,73 | €1.685,47 | €99,49 | €-0,01 |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 0 | €9.837,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Quality7 Regime V1 | 0 | €9.834,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 0 | €9.817,34 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Balanced Long No Rhv V1 | 6 | €9.794,29 | €1.151,65 | €3.454,96 | €195,89 | €135,29 |
| TEST | Master Adaptive Gb20 V1 | 7 | €9.779,61 | €1.492,84 | €2.985,67 | €196,71 | €271,93 |
| TEST | Eth Adaptive 1H | 0 | €9.771,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 1H | 0 | €9.765,13 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 0 | €9.762,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | 4 | €9.756,32 | €1.108,11 | €3.324,34 | €194,32 | €35,11 |
| TEST | Eth Bollinger 1H | 0 | €9.731,13 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 0 | €9.723,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Nohigh Cap75 V1 | 4 | €9.719,02 | €1.004,71 | €3.014,12 | €145,58 | €0,00 |
| TEST | Eth Ema 1H | 1 | €9.716,07 | €1.125,12 | €3.375,35 | €48,61 | €-2,74 |
| TEST | Scanner Top5 Btc Guard Mfe V1 | 7 | €9.716,06 | €1.050,39 | €2.100,79 | €195,34 | €244,13 |
| TEST | Eth Donchian 1H | 0 | €9.711,11 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Quality7 V1 | 4 | €9.650,59 | €1.438,51 | €2.877,02 | €190,29 | €136,22 |
| TEST | Global Confluence puro 1H | 0 | €9.647,46 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H V3 Filtered | 5 | €9.630,67 | €2.419,44 | €7.258,32 | €194,73 | €231,29 |
| TEST | 1H Fast Score 6 75 V1 | 5 | €9.600,71 | €727,34 | €2.182,02 | €97,60 | €44,95 |
| TEST | Bilanciata 1H V1 | 9 | €9.590,69 | €1.147,60 | €3.442,79 | €146,55 | €256,77 |
| TEST | Combo Adaptive Regime V1 | 1 | €9.587,02 | €987,06 | €1.974,12 | €49,09 | €0,00 |
| TEST | Master Adaptive Gb20 Loss Cap V1 | 7 | €9.584,46 | €1.548,47 | €3.096,94 | €191,21 | €46,43 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 0 | €9.579,83 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | 5 | €9.572,18 | €727,29 | €2.181,88 | €97,41 | €44,00 |
| TEST | 1H Fast V3 No Esports V1 | 5 | €9.561,05 | €1.053,15 | €3.159,44 | €191,07 | €8,54 |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | 4 | €9.476,95 | €979,65 | €2.938,95 | €141,95 | €0,00 |
| TEST | Btc Ema 1H | 0 | €9.463,59 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Runner25 V1 | 7 | €9.412,71 | €1.528,53 | €3.057,07 | €146,56 | €236,86 |
| TEST | Benchmark trend following EMA 1H | 5 | €9.397,98 | €981,82 | €1.963,65 | €144,18 | €210,85 |
| TEST | Master Adaptive Expanded V1 | 4 | €9.371,11 | €1.563,30 | €3.126,60 | €186,75 | €0,00 |
| TEST | Master Adaptive No Alt V1 | 6 | €9.353,07 | €1.707,75 | €3.415,51 | €186,48 | €35,32 |
| TEST | Scanner Bottom10 Short | 4 | €9.320,74 | €1.261,36 | €2.522,73 | €140,86 | €0,00 |
| TEST | Scanner Bottom15 Short | 4 | €9.320,74 | €1.261,36 | €2.522,73 | €140,86 | €0,00 |
| TEST | Scanner Bottom20 Short | 4 | €9.320,74 | €1.261,36 | €2.522,73 | €140,86 | €0,00 |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | 7 | €9.311,76 | €1.160,62 | €2.321,24 | €185,91 | €16,31 |
| TEST | Combo Adaptive Mfe Trail | 7 | €9.286,88 | €1.162,48 | €2.324,96 | €151,54 | €241,74 |
| TEST | Combo Trend | 6 | €9.278,35 | €2.003,10 | €4.006,21 | €95,46 | €202,09 |
| TEST | Bilanciata 1H V2 | 5 | €9.262,32 | €1.119,75 | €3.359,24 | €138,17 | €26,93 |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | 4 | €9.256,15 | €1.252,64 | €2.505,29 | €139,88 | €0,00 |
| TEST | Scanner Bottom5 Short Profit Lock V1 | 4 | €9.242,07 | €1.250,74 | €2.501,48 | €139,67 | €0,00 |
| TEST | Combo Adaptive Tp3 V1 | 7 | €9.236,63 | €1.499,98 | €2.999,97 | €143,82 | €232,43 |
| TEST | Scanner Bottom 5 Short 1H | 4 | €9.170,95 | €1.241,11 | €2.482,23 | €138,60 | €0,00 |
| TEST | 1H Balanced V3 Long Only V1 | 5 | €9.108,85 | €2.288,34 | €6.865,03 | €184,18 | €218,76 |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | 4 | €9.096,93 | €1.570,62 | €3.141,23 | €136,01 | €19,67 |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | 5 | €9.073,03 | €1.427,94 | €2.855,87 | €181,48 | €0,15 |
| TEST | Master Adaptive Strict3 V1 | 6 | €9.023,57 | €1.120,46 | €2.240,91 | €180,47 | €19,29 |
| TEST | 1H Fast V3 Cap75 V1 | 4 | €9.015,82 | €1.081,14 | €3.243,43 | €134,32 | €44,93 |
| TEST | Forza relativa 1H V1 | 7 | €8.840,11 | €1.785,85 | €3.571,70 | €135,52 | €237,21 |
| TEST | Scanner Top5 Btc Btc Le3 V1 | 6 | €8.781,38 | €2.035,43 | €4.070,86 | €175,01 | €34,22 |
| TEST | Combo Mean Reversion | 1 | €8.636,37 | €942,00 | €1.883,99 | €44,59 | €0,00 |
| TEST | Benchmark Bollinger mean reversion 1H | 0 | €8.194,49 | €0,00 | €0,00 | €0,00 | €0,00 |

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
| PRINCIPALE | Principale 4H | Confluenza trend | €9.816,71 | €-182,77 | 60 | 60 | 41,67% | 0,88 | €-3,05 | 6,86% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €11.553,24 | €1.536,83 | 139 | 139 | 45,32% | 1,50 | €11,06 | 6,75% |
| TEST | Donchian 1H Gb20 120R V1 | Donchian breakout 20 barre | €11.281,23 | €1.265,21 | 107 | 107 | 43,93% | 1,59 | €11,82 | 6,75% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €11.240,58 | €960,56 | 174 | 174 | 47,70% | 1,31 | €5,52 | 8,85% |
| TEST | Main Side Regime Guard V1 | Confluenza trend | €11.183,96 | €1.177,18 | 51 | 51 | 60,78% | 2,53 | €23,08 | 3,82% |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | Momentum / breakout | €11.090,92 | €1.070,99 | 192 | 192 | 50,00% | 1,27 | €5,58 | 7,95% |
| TEST | Combo Adaptive Long Only V1 | Combo Adaptive | €11.038,39 | €556,50 | 161 | 161 | 48,45% | 1,19 | €3,46 | 7,78% |
| TEST | Combo Trend Side Regime Guard V1 | Combo Trend | €11.036,19 | €802,25 | 152 | 152 | 51,32% | 1,27 | €5,28 | 10,10% |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | Momentum / breakout V3 Filtered | €10.744,26 | €719,09 | 124 | 124 | 49,19% | 1,28 | €5,80 | 4,50% |
| TEST | Scanner Top15 Long | Scanner Top15 Long | €10.705,85 | €409,97 | 194 | 194 | 47,94% | 1,14 | €2,11 | 10,31% |
| TEST | Scanner Top20 Long | Scanner Top20 Long | €10.705,85 | €409,97 | 194 | 194 | 47,94% | 1,14 | €2,11 | 10,31% |
| TEST | Combo Adaptive | Combo Adaptive | €10.645,54 | €376,88 | 204 | 204 | 46,57% | 1,11 | €1,85 | 8,17% |
| TEST | Scanner Top10 Long | Scanner Top10 Long | €10.623,32 | €218,67 | 176 | 176 | 48,30% | 1,08 | €1,24 | 10,31% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €10.621,79 | €622,95 | 74 | 65 | 50,00% | 1,36 | €8,42 | 3,89% |
| TEST | 1H Fast No Pepe V1 | Momentum / breakout | €10.593,78 | €579,84 | 270 | 270 | 44,44% | 1,13 | €2,15 | 9,28% |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | Momentum / breakout V3 Filtered | €10.584,54 | €399,98 | 213 | 213 | 49,30% | 1,11 | €1,88 | 9,50% |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | Momentum / breakout V3 Filtered | €10.557,76 | €531,56 | 132 | 132 | 49,24% | 1,25 | €4,03 | 5,24% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €10.531,31 | €266,19 | 155 | 155 | 45,16% | 1,09 | €1,72 | 11,27% |
| TEST | Combo Scanner | Combo Scanner | €10.528,06 | €283,55 | 186 | 186 | 44,09% | 1,08 | €1,52 | 11,38% |
| TEST | Rapida 1H V3 Filtered | Momentum / breakout V3 Filtered | €10.516,54 | €333,16 | 257 | 257 | 44,36% | 1,07 | €1,30 | 9,48% |
| TEST | Scanner Top5 Btc Tp3 V1 | Scanner Top 5 + forza BTC | €10.315,19 | €278,05 | 150 | 150 | 44,00% | 1,09 | €1,85 | 11,78% |
| TEST | Scanner Top5 Btc Runner25 V1 | Scanner Top 5 + forza BTC | €10.309,15 | €272,04 | 154 | 154 | 44,16% | 1,09 | €1,77 | 12,06% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | Momentum / breakout V3 Filtered | €10.300,05 | €300,05 | 33 | 33 | 48,48% | 2,04 | €9,09 | 2,01% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €10.293,89 | €293,89 | 19 | 19 | 57,89% | 1,95 | €15,47 | 2,77% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | Momentum / breakout V3 Filtered | €10.271,73 | €271,73 | 22 | 22 | 50,00% | 1,74 | €12,35 | 1,72% |
| TEST | 1H Fast V3 No Esports Long Only V1 | Momentum / breakout V3 Filtered | €10.245,85 | €226,81 | 231 | 231 | 43,29% | 1,05 | €0,98 | 10,60% |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | Momentum / breakout V3 Filtered | €10.239,20 | €239,20 | 17 | 17 | 52,94% | 4,50 | €14,07 | 1,01% |
| TEST | 1H Fast V3 Nohigh Range Only V1 | Momentum / breakout V3 Filtered | €10.238,74 | €189,83 | 76 | 76 | 44,74% | 1,10 | €2,50 | 6,05% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | Momentum / breakout V3 Filtered | €10.235,18 | €235,18 | 20 | 20 | 50,00% | 1,90 | €11,76 | 2,73% |
| TEST | Main Dynamic Asset Selector V1 | Confluenza trend | €10.210,22 | €201,95 | 18 | 18 | 38,89% | 1,40 | €11,22 | 3,39% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.209,20 | €209,20 | 6 | 6 | 83,33% | 4,66 | €34,87 | 0,85% |
| TEST | Ampia 4H | Confluenza trend | €10.198,96 | €194,83 | 55 | 55 | 34,55% | 1,15 | €3,54 | 4,45% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €10.189,10 | €191,22 | 9 | 9 | 55,56% | 2,16 | €21,25 | 1,01% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | Momentum / breakout V3 Filtered | €10.185,37 | €185,37 | 22 | 22 | 40,91% | 1,57 | €8,43 | 2,27% |
| TEST | Combo Adaptive Side Regime Guard V1 | Combo Adaptive | €10.166,48 | €-96,66 | 159 | 159 | 44,03% | 0,97 | €-0,61 | 11,68% |
| TEST | 1H Fast Score 6 75 Range Only V1 | Momentum / breakout | €10.155,20 | €132,30 | 51 | 51 | 43,14% | 1,10 | €2,59 | 6,49% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €10.155,15 | €144,72 | 7 | 7 | 42,86% | 1,87 | €20,67 | 1,61% |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | Momentum / breakout V3 Filtered | €10.145,12 | €145,12 | 44 | 44 | 45,45% | 1,20 | €3,30 | 2,91% |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | Momentum / breakout V3 Filtered | €10.099,04 | €99,04 | 55 | 55 | 54,55% | 1,12 | €1,80 | 3,59% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.093,26 | €68,27 | 3 | 3 | 66,67% | 2,25 | €22,76 | 0,91% |
| TEST | 1H Fast V3 Long Only V1 | Momentum / breakout V3 Filtered | €10.087,82 | €-105,92 | 231 | 231 | 42,86% | 0,98 | €-0,46 | 12,52% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €10.066,52 | €66,52 | 17 | 17 | 58,82% | 1,16 | €3,91 | 3,08% |
| TEST | Sol Ema 1H | Trend following EMA | €10.051,27 | €73,41 | 23 | 23 | 43,48% | 1,11 | €3,19 | 3,33% |
| TEST | Combo Adaptive Partial 1R V1 | Combo Adaptive | €10.050,43 | €55,48 | 177 | 177 | 44,63% | 1,02 | €0,31 | 8,69% |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | Momentum / breakout V3 Filtered | €10.048,77 | €48,77 | 23 | 23 | 43,48% | 1,12 | €2,12 | 3,05% |
| TEST | 1H Fast Tp2 V1 | Momentum / breakout | €10.048,74 | €51,91 | 267 | 267 | 39,70% | 1,01 | €0,19 | 6,56% |
| TEST | Rapida 1H V1 | Momentum / breakout | €10.043,28 | €43,28 | 78 | 78 | 34,62% | 1,02 | €0,55 | 6,76% |
| TEST | Sol Ema 4H | Trend following EMA | €10.042,02 | €57,68 | 10 | 10 | 40,00% | 1,22 | €5,77 | 2,27% |
| TEST | 1H Balanced Short Trend Down Strict V1 | Confluenza trend | €10.035,46 | €35,46 | 13 | 13 | 38,46% | 1,13 | €2,73 | 1,80% |
| TEST | Scalp RSI Long 20 · prudente · 5x | Inversione RSI estrema 15m | €10.032,32 | €32,32 | 11 | 11 | 54,55% | 1,85 | €2,94 | 0,36% |
| TEST | Scalp RSI Short 85 · €50 · 15x | Inversione RSI estrema 15m | €10.022,70 | €22,70 | 6 | 6 | 66,67% | 1,87 | €3,78 | 0,31% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €10.014,08 | €14,08 | 30 | 30 | 43,33% | 1,10 | €0,47 | 0,33% |
| TEST | Scalp RSI Short 80 · €50 · 15x | Inversione RSI estrema 15m | €10.009,44 | €9,44 | 17 | 17 | 41,18% | 1,17 | €0,56 | 0,53% |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | Momentum / breakout V3 Filtered | €10.008,92 | €8,92 | 30 | 30 | 36,67% | 1,02 | €0,30 | 4,84% |
| TEST | Scalp RSI Short 85 · €10 · 15x | Inversione RSI estrema 15m | €10.004,54 | €4,54 | 6 | 6 | 66,67% | 1,87 | €0,76 | 0,06% |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | Momentum / breakout V3 Filtered | €10.003,37 | €3,37 | 8 | 8 | 37,50% | 1,02 | €0,42 | 2,15% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €10.002,82 | €2,82 | 30 | 30 | 43,33% | 1,10 | €0,09 | 0,07% |
| TEST | Scalp RSI Short 80 · €10 · 15x | Inversione RSI estrema 15m | €10.001,89 | €1,89 | 17 | 17 | 41,18% | 1,17 | €0,11 | 0,11% |
| TEST | Scanner Bottom5 Short Continuation V1 | Scanner Bottom5 Short Continuation | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 20 · €10 · 15x | Inversione RSI estrema 15m | €9.998,68 | €-1,32 | 11 | 11 | 36,36% | 0,74 | €-0,12 | 0,04% |
| TEST | Scalp RSI Long 15 · €10 · 15x | Inversione RSI estrema 15m | €9.997,60 | €-2,40 | 3 | 3 | 33,33% | 0,13 | €-0,80 | 0,02% |
| TEST | Scalp RSI Short 85 · prudente · 5x | Inversione RSI estrema 15m | €9.996,83 | €-3,17 | 6 | 6 | 66,67% | 0,86 | €-0,53 | 0,30% |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | Momentum / breakout V3 Filtered | €9.995,23 | €-4,77 | 15 | 15 | 46,67% | 0,99 | €-0,32 | 2,70% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €9.994,27 | €17,60 | 3 | 3 | 33,33% | 1,17 | €5,87 | 0,96% |
| TEST | Scalp RSI Long 20 · €50 · 15x | Inversione RSI estrema 15m | €9.993,42 | €-6,58 | 11 | 11 | 36,36% | 0,74 | €-0,60 | 0,21% |
| TEST | Doge Ema 1H | Trend following EMA | €9.989,46 | €-10,54 | 26 | 26 | 57,69% | 0,98 | €-0,41 | 2,77% |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | €9.988,00 | €-12,00 | 3 | 3 | 33,33% | 0,13 | €-4,00 | 0,12% |
| TEST | Scalp RSI Long 25 · €10 · 15x | Inversione RSI estrema 15m | €9.987,54 | €-12,46 | 18 | 18 | 33,33% | 0,30 | €-0,69 | 0,15% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €9.987,29 | €9,29 | 24 | 24 | 45,83% | 1,01 | €0,39 | 4,59% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €9.980,98 | €-19,02 | 5 | 5 | 40,00% | 0,88 | €-3,80 | 1,96% |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | €9.980,94 | €-19,06 | 3 | 3 | 33,33% | 0,19 | €-6,35 | 0,20% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €9.979,42 | €-20,58 | 15 | 15 | 60,00% | 0,94 | €-1,37 | 1,89% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €9.968,58 | €-31,42 | 9 | 9 | 44,44% | 0,86 | €-3,49 | 1,23% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €9.963,04 | €-36,96 | 18 | 18 | 33,33% | 0,63 | €-2,05 | 0,71% |
| TEST | Master Adaptive Gb20 Be V1 | Master Adaptive Consensus | €9.959,49 | €-316,68 | 103 | 103 | 33,01% | 0,88 | €-3,07 | 8,39% |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | Combo Adaptive | €9.959,32 | €-40,68 | 55 | 55 | 49,09% | 0,97 | €-0,74 | 4,27% |
| TEST | Master Adaptive Gb20 Partial V1 | Master Adaptive Consensus | €9.948,90 | €-326,97 | 98 | 98 | 35,71% | 0,87 | €-3,34 | 7,98% |
| TEST | Scanner Top5 Btc Guard V1 | Scanner Top 5 + forza BTC | €9.947,39 | €-301,77 | 143 | 143 | 39,16% | 0,90 | €-2,11 | 7,34% |
| TEST | Btc Ema 4H | Trend following EMA | €9.941,56 | €-33,12 | 4 | 4 | 25,00% | 0,78 | €-8,28 | 1,76% |
| TEST | Scalp RSI Short 80 · prudente · 5x | Inversione RSI estrema 15m | €9.939,55 | €-60,45 | 17 | 17 | 35,29% | 0,39 | €-3,56 | 0,89% |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | €9.937,70 | €-62,30 | 18 | 18 | 33,33% | 0,30 | €-3,46 | 0,76% |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | Momentum / breakout V3 Filtered | €9.930,97 | €-93,49 | 151 | 151 | 44,37% | 0,97 | €-0,62 | 6,64% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.917,05 | €-82,95 | 30 | 30 | 43,33% | 0,52 | €-2,77 | 0,84% |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | €9.910,42 | €-364,39 | 100 | 100 | 35,00% | 0,87 | €-3,64 | 7,80% |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | Momentum / breakout V3 Filtered | €9.903,76 | €-118,51 | 154 | 154 | 47,40% | 0,97 | €-0,77 | 8,44% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €9.897,46 | €-102,54 | 12 | 12 | 41,67% | 0,70 | €-8,55 | 1,91% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €9.888,37 | €-86,44 | 5 | 5 | 20,00% | 0,61 | €-17,29 | 2,43% |
| TEST | Eth Ema 4H | Trend following EMA | €9.887,35 | €-112,70 | 7 | 7 | 28,57% | 0,57 | €-16,10 | 1,83% |
| TEST | 1H Fast V3 Nohigh V1 | Momentum / breakout V3 Filtered | €9.882,55 | €-117,93 | 171 | 171 | 45,03% | 0,96 | €-0,69 | 7,10% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €9.873,79 | €-444,69 | 84 | 84 | 32,14% | 0,82 | €-5,29 | 8,44% |
| TEST | Scanner Top5 Btc Mfe V1 | Scanner Top 5 + forza BTC | €9.872,59 | €-375,95 | 147 | 147 | 44,22% | 0,86 | €-2,56 | 12,28% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €9.839,17 | €-159,53 | 138 | 131 | 40,58% | 0,95 | €-1,16 | 10,88% |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | Momentum / breakout V3 Filtered | €9.837,38 | €-162,62 | 37 | 37 | 40,54% | 0,76 | €-4,40 | 3,08% |
| TEST | Combo Adaptive Quality7 Regime V1 | Combo Adaptive | €9.834,05 | €-165,95 | 55 | 55 | 45,45% | 0,88 | €-3,02 | 5,41% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | Momentum / breakout V3 Filtered | €9.817,34 | €-182,66 | 24 | 24 | 41,67% | 0,64 | €-7,61 | 3,23% |
| TEST | 1H Balanced Long No Rhv V1 | Confluenza trend | €9.794,29 | €-338,86 | 122 | 122 | 45,08% | 0,85 | €-2,78 | 9,26% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €9.779,61 | €-491,56 | 134 | 134 | 44,78% | 0,83 | €-3,67 | 9,02% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.771,60 | €-228,40 | 19 | 19 | 42,11% | 0,63 | €-12,02 | 3,14% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.765,13 | €-234,87 | 17 | 17 | 41,18% | 0,62 | €-13,82 | 2,91% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | Momentum / breakout V3 Filtered | €9.762,18 | €-237,82 | 7 | 7 | 14,29% | 0,02 | €-33,97 | 2,82% |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | Momentum / breakout | €9.756,32 | €-276,80 | 135 | 135 | 40,74% | 0,91 | €-2,05 | 7,99% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €9.731,13 | €-268,87 | 10 | 10 | 40,00% | 0,38 | €-26,89 | 4,16% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | Momentum / breakout V3 Filtered | €9.723,72 | €-276,28 | 31 | 31 | 32,26% | 0,62 | €-8,91 | 4,83% |
| TEST | 1H Fast Nohigh Cap75 V1 | Momentum / breakout | €9.719,02 | €-279,18 | 199 | 199 | 40,20% | 0,93 | €-1,40 | 10,60% |
| TEST | Eth Ema 1H | Trend following EMA | €9.716,07 | €-279,00 | 27 | 27 | 40,74% | 0,67 | €-10,33 | 4,80% |
| TEST | Scanner Top5 Btc Guard Mfe V1 | Scanner Top 5 + forza BTC | €9.716,06 | €-527,30 | 160 | 160 | 40,00% | 0,85 | €-3,30 | 8,78% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.711,11 | €-288,89 | 18 | 18 | 33,33% | 0,56 | €-16,05 | 3,74% |
| TEST | Combo Adaptive Quality7 V1 | Combo Adaptive | €9.650,59 | €-484,42 | 98 | 98 | 38,78% | 0,80 | €-4,94 | 8,88% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.647,46 | €-352,54 | 21 | 21 | 33,33% | 0,46 | €-16,79 | 3,93% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €9.630,67 | €-596,48 | 201 | 201 | 40,80% | 0,85 | €-2,97 | 12,68% |
| TEST | 1H Fast Score 6 75 V1 | Momentum / breakout | €9.600,71 | €-442,93 | 186 | 186 | 41,40% | 0,91 | €-2,38 | 15,64% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €9.590,69 | €-663,77 | 173 | 173 | 39,88% | 0,79 | €-3,84 | 15,68% |
| TEST | Combo Adaptive Regime V1 | Combo Adaptive | €9.587,02 | €-411,80 | 84 | 84 | 46,43% | 0,80 | €-4,90 | 6,28% |
| TEST | Master Adaptive Gb20 Loss Cap V1 | Master Adaptive Consensus | €9.584,46 | €-461,55 | 90 | 90 | 26,67% | 0,81 | €-5,13 | 11,41% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | Momentum / breakout V3 Filtered | €9.579,83 | €-420,17 | 11 | 11 | 0,00% | 0,00 | €-38,20 | 4,20% |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | Momentum / breakout | €9.572,18 | €-470,51 | 145 | 145 | 42,76% | 0,88 | €-3,24 | 15,94% |
| TEST | 1H Fast V3 No Esports V1 | Momentum / breakout V3 Filtered | €9.561,05 | €-445,48 | 225 | 225 | 42,22% | 0,91 | €-1,98 | 10,92% |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | Momentum / breakout | €9.476,95 | €-521,29 | 162 | 162 | 38,27% | 0,84 | €-3,22 | 10,60% |
| TEST | Btc Ema 1H | Trend following EMA | €9.463,59 | €-536,41 | 20 | 20 | 20,00% | 0,33 | €-26,82 | 5,46% |
| TEST | Combo Adaptive Runner25 V1 | Combo Adaptive | €9.412,71 | €-822,18 | 142 | 142 | 36,62% | 0,70 | €-5,79 | 14,10% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.397,98 | €-811,71 | 158 | 158 | 39,24% | 0,71 | €-5,14 | 12,31% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €9.371,11 | €-628,22 | 86 | 86 | 34,88% | 0,73 | €-7,30 | 7,96% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €9.353,07 | €-679,95 | 97 | 97 | 35,05% | 0,77 | €-7,01 | 10,13% |
| TEST | Scanner Bottom10 Short | Scanner Bottom10 Short | €9.320,74 | €-677,79 | 70 | 70 | 31,43% | 0,65 | €-9,68 | 9,06% |
| TEST | Scanner Bottom15 Short | Scanner Bottom15 Short | €9.320,74 | €-677,79 | 70 | 70 | 31,43% | 0,65 | €-9,68 | 9,06% |
| TEST | Scanner Bottom20 Short | Scanner Bottom20 Short | €9.320,74 | €-677,79 | 70 | 70 | 31,43% | 0,65 | €-9,68 | 9,06% |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | Scanner Top 5 + forza BTC | €9.311,76 | €-703,63 | 105 | 105 | 38,10% | 0,76 | €-6,70 | 11,79% |
| TEST | Combo Adaptive Mfe Trail | Combo Adaptive | €9.286,88 | €-953,49 | 220 | 220 | 40,91% | 0,76 | €-4,33 | 15,45% |
| TEST | Combo Trend | Combo Trend | €9.278,35 | €-921,05 | 191 | 191 | 39,79% | 0,78 | €-4,82 | 14,08% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €9.262,32 | €-761,93 | 159 | 145 | 42,14% | 0,78 | €-4,79 | 11,82% |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | Scanner Bottom 5 Short | €9.256,15 | €-742,38 | 61 | 61 | 31,15% | 0,58 | €-12,17 | 9,08% |
| TEST | Scanner Bottom5 Short Profit Lock V1 | Scanner Bottom 5 Short | €9.242,07 | €-756,47 | 62 | 62 | 30,65% | 0,56 | €-12,20 | 9,08% |
| TEST | Combo Adaptive Tp3 V1 | Combo Adaptive | €9.236,63 | €-993,87 | 122 | 122 | 36,07% | 0,60 | €-8,15 | 14,10% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.170,95 | €-827,60 | 89 | 89 | 31,46% | 0,64 | €-9,30 | 10,17% |
| TEST | 1H Balanced V3 Long Only V1 | Confluenza trend V3 Filtered | €9.108,85 | €-1.105,99 | 155 | 155 | 40,65% | 0,64 | €-7,14 | 12,43% |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | Scanner Top 5 + forza BTC | €9.096,93 | €-920,75 | 52 | 52 | 26,92% | 0,44 | €-17,71 | 12,23% |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | Scanner Top 5 + forza BTC | €9.073,03 | €-925,85 | 129 | 129 | 37,98% | 0,72 | €-7,18 | 13,91% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €9.023,57 | €-994,35 | 78 | 78 | 29,49% | 0,67 | €-12,75 | 13,60% |
| TEST | 1H Fast V3 Cap75 V1 | Momentum / breakout V3 Filtered | €9.015,82 | €-1.027,16 | 195 | 195 | 38,46% | 0,78 | €-5,27 | 17,41% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €8.840,11 | €-1.394,62 | 149 | 149 | 33,56% | 0,60 | €-9,36 | 19,11% |
| TEST | Scanner Top5 Btc Btc Le3 V1 | Scanner Top 5 + forza BTC | €8.781,38 | €-1.250,32 | 107 | 107 | 36,45% | 0,56 | €-11,69 | 16,19% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €8.636,37 | €-1.362,34 | 60 | 60 | 33,33% | 0,44 | €-22,71 | 16,00% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €8.194,49 | €-1.805,51 | 110 | 110 | 38,18% | 0,51 | €-16,41 | 19,95% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | SPCX | LONG | Confluenza trend | 240m | 3,0x | 136,56189 | 136,56189 | 128,79610 | 91,72407 | 152,09346 | €285,50 | €856,50 | €48,71 | €0,00 |
| Principale 4H | VELVET | LONG | Confluenza trend | 240m | 3,0x | 0,55987 | 0,55987 | 0,49269 | 0,37605 | 0,69424 | €131,08 | €393,24 | €47,19 | €0,00 |
| Principale 4H | EDEN | LONG | Confluenza trend | 240m | 3,0x | 0,06195 | 0,06195 | 0,05451 | 0,04161 | 0,07681 | €130,34 | €391,02 | €46,92 | €0,00 |
| Principale 4H | TRUMP | LONG | Confluenza trend | 240m | 3,0x | 2,46049 | 2,46049 | 2,16523 | 1,65263 | 3,05101 | €134,98 | €404,95 | €48,59 | €0,00 |
| Principale 4H | UNI | LONG | Confluenza trend | 240m | 3,0x | 6,93739 | 7,00700 | 6,33086 | 4,65961 | 8,15044 | €18,73 | €56,20 | €4,91 | €0,56 |
| Bilanciata 1H V1 | BTR | SHORT | Confluenza trend | 60m | 3,0x | 0,05109 | 0,05109 | 0,05109 | 0,06786 | 0,03883 | €125,78 | €377,33 | €0,00 | €-0,00 |
| Bilanciata 1H V1 | ARB | LONG | Confluenza trend | 60m | 3,0x | 0,13283 | 0,17410 | 0,12480 | 0,08922 | 0,14889 | €256,10 | €768,31 | €46,46 | €238,74 |
| Bilanciata 1H V1 | PEPE | SHORT | Confluenza trend | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €18,46 | €55,39 | €1,83 | €-0,00 |
| Bilanciata 1H V1 | XRP | LONG | Confluenza trend | 60m | 3,0x | 1,41290 | 1,40809 | 1,39256 | 0,94900 | 1,45359 | €9,02 | €27,05 | €0,39 | €-0,09 |
| Bilanciata 1H V1 | DASH | LONG | Confluenza trend | 60m | 3,0x | 70,61412 | 70,79000 | 64,59923 | 47,42915 | 82,64391 | €24,96 | €74,87 | €6,38 | €0,19 |
| Bilanciata 1H V1 | NEAR | LONG | Confluenza trend | 60m | 3,0x | 2,40748 | 2,42700 | 2,29716 | 1,61703 | 2,62812 | €10,93 | €32,80 | €1,50 | €0,27 |
| Bilanciata 1H V1 | ETH | LONG | Confluenza trend | 60m | 3,0x | 2503,97069 | 2501,94000 | 2467,91352 | 1681,83365 | 2576,08505 | €14,30 | €42,91 | €0,62 | €-0,03 |
| Bilanciata 1H V1 | ZEC | LONG | Confluenza trend | 60m | 3,0x | 1186,35722 | 1208,44000 | 1129,86589 | 796,83660 | 1299,33988 | €321,10 | €963,30 | €45,87 | €17,93 |
| Bilanciata 1H V1 | TAO | LONG | Confluenza trend | 60m | 3,0x | 273,49469 | 273,44000 | 262,68503 | 183,69727 | 295,11399 | €366,94 | €1.100,83 | €43,51 | €-0,22 |
| 1H Balanced Long No Rhv V1 | SKHYNIX | LONG | Confluenza trend | 60m | 3,0x | 1214,11277 | 1214,11277 | 1170,18211 | 815,47908 | 1301,97411 | €413,43 | €1.240,28 | €44,88 | €0,00 |
| 1H Balanced Long No Rhv V1 | BOME | LONG | Confluenza trend | 60m | 3,0x | 0,00129 | 0,00129 | 0,00114 | 0,00087 | 0,00160 | €134,98 | €404,95 | €48,59 | €0,00 |
| 1H Balanced Long No Rhv V1 | TAO | LONG | Confluenza trend | 60m | 3,0x | 247,38947 | 273,44000 | 237,94346 | 166,16326 | 266,28148 | €428,20 | €1.284,61 | €49,05 | €135,27 |
| 1H Balanced Long No Rhv V1 | HEMI | LONG | Confluenza trend | 60m | 3,0x | 0,01177 | 0,01177 | 0,01036 | 0,00790 | 0,01459 | €131,93 | €395,78 | €47,49 | €0,00 |
| 1H Balanced Long No Rhv V1 | ZEC | LONG | Confluenza trend | 60m | 3,0x | 1207,83152 | 1208,44000 | 1150,42638 | 811,26017 | 1322,64180 | €22,21 | €66,63 | €3,17 | €0,03 |
| 1H Balanced Long No Rhv V1 | NEAR | LONG | Confluenza trend | 60m | 3,0x | 2,42749 | 2,42700 | 2,32276 | 1,63046 | 2,63693 | €20,90 | €62,71 | €2,71 | €-0,01 |
| Bilanciata 1H V2 | SKHYNIX | LONG | Confluenza trend V2 | 60m | 3,0x | 1214,11277 | 1214,11277 | 1170,18211 | 815,47908 | 1301,97411 | €422,38 | €1.267,15 | €45,85 | €0,00 |
| Bilanciata 1H V2 | BTR | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,05545 | 0,05545 | 0,05545 | 0,07365 | 0,04214 | €126,95 | €380,86 | €0,00 | €-0,00 |
| Bilanciata 1H V2 | ARB | LONG | Confluenza trend V2 | 60m | 3,0x | 0,13495 | 0,17410 | 0,12685 | 0,09064 | 0,15116 | €19,71 | €59,12 | €3,55 | €17,15 |
| Bilanciata 1H V2 | DASH | LONG | Confluenza trend V2 | 60m | 3,0x | 69,34387 | 70,79000 | 63,21411 | 46,57596 | 81,60338 | €160,09 | €480,27 | €42,45 | €10,02 |
| Bilanciata 1H V2 | TAO | LONG | Confluenza trend V2 | 60m | 3,0x | 273,49469 | 273,44000 | 262,68503 | 183,69727 | 295,11399 | €390,62 | €1.171,85 | €46,32 | €-0,23 |
| Bilanciata 1H V3 Filtered | SKHYNIX | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1220,85412 | 1220,85412 | 1177,63561 | 820,00702 | 1307,29117 | €460,42 | €1.381,27 | €48,90 | €0,00 |
| Bilanciata 1H V3 Filtered | ADA | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,20138 | 0,20138 | 0,20719 | 0,26750 | 0,18976 | €559,88 | €1.679,63 | €48,45 | €-0,00 |
| Bilanciata 1H V3 Filtered | ARB | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,13283 | 0,17410 | 0,12480 | 0,08922 | 0,14889 | €262,61 | €787,82 | €47,64 | €244,80 |
| Bilanciata 1H V3 Filtered | UNI | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 7,14143 | 7,00700 | 6,87560 | 4,79666 | 7,67309 | €9,58 | €28,74 | €1,07 | €-0,54 |
| Bilanciata 1H V3 Filtered | ETH | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 2511,57221 | 2501,94000 | 2475,40557 | 1686,93934 | 2583,90549 | €1.126,95 | €3.380,86 | €48,68 | €-12,97 |
| 1H Fast Score 6 75 V1 | BTR | SHORT | Momentum / breakout | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €126,75 | €380,26 | €0,00 | €-0,00 |
| 1H Fast Score 6 75 V1 | ARB | LONG | Momentum / breakout | 60m | 3,0x | 0,13189 | 0,17410 | 0,12574 | 0,08858 | 0,14110 | €21,85 | €65,56 | €3,05 | €20,98 |
| 1H Fast Score 6 75 V1 | BTC | LONG | Momentum / breakout | 60m | 3,0x | 80028,10242 | 79715,87000 | 79131,78767 | 53752,20879 | 81372,57454 | €18,39 | €55,17 | €0,62 | €-0,22 |
| 1H Fast Score 6 75 V1 | MARSCOIN | LONG | Momentum / breakout | 60m | 3,0x | 0,23626 | 0,23626 | 0,20791 | 0,15869 | 0,27878 | €127,25 | €381,75 | €45,81 | €0,00 |
| 1H Fast Score 6 75 V1 | ZEC | LONG | Momentum / breakout | 60m | 3,0x | 1186,35722 | 1208,44000 | 1142,41952 | 796,83660 | 1252,26377 | €433,10 | €1.299,29 | €48,12 | €24,18 |
| 1H Fast Score 6 75 No Trend Up V1 | BTR | SHORT | Momentum / breakout | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €123,38 | €370,15 | €0,00 | €-0,00 |
| 1H Fast Score 6 75 No Trend Up V1 | ARB | LONG | Momentum / breakout | 60m | 3,0x | 0,13189 | 0,17410 | 0,12574 | 0,08858 | 0,14110 | €21,27 | €63,82 | €2,97 | €20,43 |
| 1H Fast Score 6 75 No Trend Up V1 | MARSCOIN | LONG | Momentum / breakout | 60m | 3,0x | 0,23626 | 0,23626 | 0,20791 | 0,15869 | 0,27878 | €126,82 | €380,47 | €45,66 | €0,00 |
| 1H Fast Score 6 75 No Trend Up V1 | BTC | LONG | Momentum / breakout | 60m | 3,0x | 80317,26024 | 79715,87000 | 79417,70693 | 53946,42646 | 81666,59021 | €24,01 | €72,04 | €0,81 | €-0,54 |
| 1H Fast Score 6 75 No Trend Up V1 | ZEC | LONG | Momentum / breakout | 60m | 3,0x | 1186,35722 | 1208,44000 | 1142,41952 | 796,83660 | 1252,26377 | €431,80 | €1.295,41 | €47,98 | €24,11 |
| 1H Fast Score 6 75 Range Only V1 | ADA | SHORT | Momentum / breakout | 60m | 3,0x | 0,20260 | 0,20260 | 0,20707 | 0,26912 | 0,19589 | €765,21 | €2.295,64 | €50,71 | €-0,00 |
| 1H Fast Score 6 75 Range Only V1 | HEMI | LONG | Momentum / breakout | 60m | 3,0x | 0,01177 | 0,01177 | 0,01065 | 0,00790 | 0,01345 | €178,53 | €535,59 | €51,05 | €0,00 |
| 1H Fast Score 6 75 Range Only V1 | BTR | SHORT | Momentum / breakout | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €131,87 | €395,61 | €0,00 | €-0,00 |
| 1H Fast Score 6 75 Range Only V1 | ZEC | LONG | Momentum / breakout | 60m | 3,0x | 1186,35722 | 1208,44000 | 1142,41952 | 796,83660 | 1252,26377 | €455,89 | €1.367,67 | €50,65 | €25,46 |
| 1H Fast Score 6 75 Cost Aware V1 | BTW | LONG | Momentum / breakout | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €8,91 | €26,72 | €3,13 | €0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00086 | 0,00146 | €215,92 | €647,76 | €57,03 | €0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | NEAR | LONG | Momentum / breakout | 60m | 3,0x | 2,08142 | 2,42700 | 2,02315 | 1,39802 | 2,16882 | €42,86 | €128,59 | €3,60 | €21,35 |
| 1H Fast Score 6 75 Cost Aware V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €157,13 | €471,39 | €56,57 | €-0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | BTR | SHORT | Momentum / breakout | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €150,22 | €450,66 | €0,00 | €-0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | MARSCOIN | LONG | Momentum / breakout | 60m | 3,0x | 0,25201 | 0,25201 | 0,22400 | 0,16927 | 0,29402 | €141,43 | €424,29 | €47,15 | €0,00 |
| 1H Fast Nohigh Cap75 V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €139,29 | €417,86 | €50,14 | €-0,00 |
| 1H Fast Nohigh Cap75 V1 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €141,57 | €424,71 | €50,14 | €-0,00 |
| 1H Fast Nohigh Cap75 V1 | BTR | SHORT | Momentum / breakout | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €135,62 | €406,85 | €0,00 | €-0,00 |
| 1H Fast Nohigh Cap75 V1 | PEPE | SHORT | Momentum / breakout | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €588,23 | €1.764,70 | €45,30 | €-0,00 |
| 1H Fast Long Btc 1 3 Cap75 V1 | PROM | LONG | Momentum / breakout | 60m | 3,0x | 6,93686 | 6,93686 | 6,39299 | 4,65926 | 7,75266 | €205,67 | €617,01 | €48,38 | €0,00 |
| 1H Fast Long Btc 1 3 Cap75 V1 | MARSCOIN | LONG | Momentum / breakout | 60m | 3,0x | 0,23626 | 0,23626 | 0,20791 | 0,15869 | 0,27878 | €138,86 | €416,57 | €49,99 | €0,00 |
| 1H Fast Long Btc 1 3 Cap75 V1 | ZEC | LONG | Momentum / breakout | 60m | 3,0x | 1191,60827 | 1208,44000 | 1147,31771 | 800,36356 | 1258,04412 | €432,44 | €1.297,33 | €48,22 | €18,33 |
| 1H Fast Long Btc 1 3 Cap75 V1 | DASH | LONG | Momentum / breakout | 60m | 3,0x | 69,61392 | 70,79000 | 66,26910 | 46,75735 | 74,63116 | €331,14 | €993,42 | €47,73 | €16,78 |
| 1H Fast No Pepe V1 | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €172,22 | €516,67 | €49,86 | €0,00 |
| 1H Fast No Pepe V1 | TAO | LONG | Momentum / breakout | 60m | 3,0x | 247,38947 | 273,44000 | 240,04257 | 166,16326 | 258,40981 | €47,93 | €143,78 | €4,27 | €15,14 |
| 1H Fast No Pepe V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €136,27 | €408,80 | €49,06 | €-0,00 |
| 1H Fast No Pepe V1 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €9,48 | €28,43 | €3,41 | €-0,00 |
| 1H Fast No Pepe V1 | ADA | SHORT | Momentum / breakout | 60m | 3,0x | 0,20138 | 0,20138 | 0,20590 | 0,26750 | 0,19460 | €739,08 | €2.217,23 | €49,74 | €-0,00 |
| 1H Fast No Pepe V1 | 0G | LONG | Momentum / breakout | 60m | 3,0x | 0,23904 | 0,23904 | 0,21901 | 0,16056 | 0,26909 | €210,41 | €631,23 | €52,89 | €0,00 |
| 1H Fast No Pepe V1 | ZEC | LONG | Momentum / breakout | 60m | 3,0x | 1190,40803 | 1208,44000 | 1149,56911 | 799,55740 | 1251,66642 | €22,62 | €67,87 | €2,33 | €1,03 |
| 1H Fast Tp2 V1 | BTW | LONG | Momentum / breakout | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,56752 | €142,85 | €428,56 | €50,25 | €0,00 |
| 1H Fast Tp2 V1 | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00132 | 0,00132 | 0,00119 | 0,00088 | 0,00158 | €18,87 | €56,62 | €5,59 | €0,00 |
| 1H Fast Tp2 V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,17246 | 0,17246 | 0,17246 | 0,22908 | 0,13107 | €139,71 | €419,14 | €0,00 | €-0,00 |
| 1H Fast Tp2 V1 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03379 | €141,13 | €423,40 | €50,81 | €-0,00 |
| 1H Fast Tp2 V1 | 4 | LONG | Momentum / breakout | 60m | 3,0x | 0,03351 | 0,03351 | 0,03024 | 0,02251 | 0,04003 | €142,67 | €428,01 | €41,68 | €0,00 |
| 1H Fast Tp2 V1 | ARB | LONG | Momentum / breakout | 60m | 3,0x | 0,18396 | 0,17410 | 0,17269 | 0,12356 | 0,20650 | €13,04 | €39,13 | €2,40 | €-2,10 |
| Rapida 1H V2 | ADA | SHORT | Momentum / breakout V2 | 60m | 3,0x | 0,20283 | 0,20283 | 0,20750 | 0,26943 | 0,19582 | €749,31 | €2.247,94 | €51,80 | €-0,00 |
| Rapida 1H V3 Filtered | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €172,00 | €515,99 | €49,79 | €0,00 |
| Rapida 1H V3 Filtered | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 273,44000 | 240,04257 | 166,16326 | 258,40981 | €589,98 | €1.769,95 | €52,56 | €186,38 |
| Rapida 1H V3 Filtered | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €140,02 | €420,06 | €50,41 | €-0,00 |
| Rapida 1H V3 Filtered | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €16,99 | €50,96 | €6,11 | €-0,00 |
| Rapida 1H V3 Filtered | PEPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €633,48 | €1.900,43 | €47,75 | €-0,00 |
| Rapida 1H V3 Filtered | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1208,68169 | 1208,44000 | 1168,71362 | 811,83120 | 1268,63379 | €37,35 | €112,04 | €3,70 | €-0,02 |
| 1H Fast V3 Cap75 V1 | BTR | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €122,50 | €367,49 | €0,00 | €-0,00 |
| 1H Fast V3 Cap75 V1 | MARSCOIN | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,23626 | 0,23626 | 0,20791 | 0,15869 | 0,27878 | €125,88 | €377,63 | €45,32 | €0,00 |
| 1H Fast V3 Cap75 V1 | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1186,35722 | 1208,44000 | 1142,41952 | 796,83660 | 1252,26377 | €397,18 | €1.191,54 | €44,13 | €22,18 |
| 1H Fast V3 Cap75 V1 | NEAR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,38548 | 2,42700 | 2,30355 | 1,60225 | 2,50836 | €435,59 | €1.306,77 | €44,88 | €22,75 |
| 1H Fast V3 Nohigh V1 | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €131,05 | €393,14 | €47,18 | €-0,00 |
| 1H Fast V3 Nohigh V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €133,20 | €399,59 | €47,18 | €-0,00 |
| 1H Fast V3 Nohigh V1 | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,20138 | 0,20138 | 0,20590 | 0,26750 | 0,19460 | €719,57 | €2.158,72 | €48,43 | €-0,00 |
| 1H Fast V3 Nohigh V1 | 0G | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,23904 | 0,23904 | 0,21901 | 0,16056 | 0,26909 | €196,32 | €588,95 | €49,35 | €0,00 |
| 1H Fast V3 Nohigh V1 | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1190,40803 | 1208,44000 | 1149,56911 | 799,55740 | 1251,66642 | €53,23 | €159,68 | €5,48 | €2,42 |
| 1H Fast V3 Long Only V1 | BTW | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €126,57 | €379,72 | €44,52 | €0,00 |
| 1H Fast V3 Long Only V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00147 | €9,56 | €28,69 | €2,66 | €0,00 |
| 1H Fast V3 Long Only V1 | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 273,44000 | 240,04257 | 166,16326 | 258,40981 | €554,42 | €1.663,26 | €49,39 | €175,14 |
| 1H Fast V3 Long Only V1 | HEMI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01177 | 0,01177 | 0,01065 | 0,00790 | 0,01345 | €170,60 | €511,79 | €48,79 | €0,00 |
| 1H Fast V3 Long Only V1 | ARB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,18396 | 0,17410 | 0,17269 | 0,12356 | 0,20086 | €19,13 | €57,39 | €3,52 | €-3,07 |
| 1H Fast V3 Long Only V1 | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1186,35722 | 1208,44000 | 1142,41952 | 796,83660 | 1252,26377 | €430,45 | €1.291,35 | €47,83 | €24,04 |
| 1H Fast V3 Long Nohigh Cap75 V1 | HEMI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01177 | 0,01177 | 0,01065 | 0,00790 | 0,01345 | €166,97 | €500,92 | €47,75 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 V1 | PROM | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 6,92735 | 6,92735 | 6,35093 | 4,65287 | 7,79198 | €195,87 | €587,60 | €48,89 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 V1 | MARSCOIN | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,23626 | 0,23626 | 0,20791 | 0,15869 | 0,27878 | €134,15 | €402,44 | €48,29 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 V1 | BTC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 80317,26024 | 79715,87000 | 79417,70693 | 53946,42646 | 81666,59021 | €16,11 | €48,34 | €0,54 | €-0,36 |
| 1H Fast V3 Long Nohigh Cap75 V1 | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1186,35722 | 1208,44000 | 1142,41952 | 796,83660 | 1252,26377 | €31,85 | €95,56 | €3,54 | €1,78 |
| 1H Fast V3 Long Nohigh Cap75 V1 | NEAR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,38548 | 2,42700 | 2,30355 | 1,60225 | 2,50836 | €476,47 | €1.429,42 | €49,09 | €24,88 |
| 1H Fast V3 No Esports V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €169,36 | €508,09 | €49,03 | €0,00 |
| 1H Fast V3 No Esports V1 | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 273,44000 | 240,04257 | 166,16326 | 258,40981 | €27,04 | €81,13 | €2,41 | €8,54 |
| 1H Fast V3 No Esports V1 | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €133,96 | €401,88 | €48,23 | €-0,00 |
| 1H Fast V3 No Esports V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €129,73 | €389,20 | €46,70 | €-0,00 |
| 1H Fast V3 No Esports V1 | PEPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €593,05 | €1.779,15 | €44,70 | €-0,00 |
| 1H Fast V3 No Esports Long Only V1 | BTW | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €132,94 | €398,81 | €46,76 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00147 | €10,06 | €30,18 | €2,80 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | HEMI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01177 | 0,01177 | 0,01065 | 0,00790 | 0,01345 | €175,30 | €525,91 | €50,13 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | PROM | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 6,92735 | 6,92735 | 6,35093 | 4,65287 | 7,79198 | €9,71 | €29,12 | €2,42 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | 0G | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,23904 | 0,23904 | 0,21901 | 0,16056 | 0,26909 | €187,89 | €563,68 | €47,23 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | ARB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,18396 | 0,17410 | 0,17269 | 0,12356 | 0,20086 | €24,76 | €74,28 | €4,55 | €-3,98 |
| 1H Fast V3 No Esports Long Only V1 | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1186,35722 | 1208,44000 | 1142,41952 | 796,83660 | 1252,26377 | €444,95 | €1.334,85 | €49,44 | €24,85 |
| 1H Fast V3 No Esports Long Only V1 | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 273,49469 | 273,44000 | 265,08718 | 183,69727 | 286,10595 | €17,17 | €51,50 | €1,58 | €-0,01 |
| 1H Fast V3 No Esports Mfe Lock V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €173,11 | €519,32 | €50,11 | €0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 273,44000 | 240,04257 | 166,16326 | 258,40981 | €593,79 | €1.781,38 | €52,90 | €187,58 |
| 1H Fast V3 No Esports Mfe Lock V1 | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €140,93 | €422,78 | €50,73 | €-0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €17,09 | €51,28 | €6,15 | €-0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | PEPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €637,57 | €1.912,72 | €48,06 | €-0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1208,68169 | 1208,44000 | 1168,71362 | 811,83120 | 1268,63379 | €37,59 | €112,76 | €3,73 | €-0,02 |
| 1H Fast V3 No Esports Stress Guard V1 | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,20283 | 0,20283 | 0,20750 | 0,26943 | 0,19582 | €739,04 | €2.217,11 | €51,09 | €-0,00 |
| 1H Fast V3 No Esports Stress Guard V1 | BTC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 80028,10242 | 79715,87000 | 79131,78767 | 53752,20879 | 81372,57454 | €77,79 | €233,37 | €2,61 | €-0,91 |
| 1H Fast V3 No Esports Stress Guard V1 | NEAR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,41948 | 2,42700 | 2,33363 | 1,62509 | 2,54827 | €509,84 | €1.529,52 | €54,28 | €4,75 |
| 1H Fast V3 No Esports Stress Guard V1 | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1186,35722 | 1208,44000 | 1142,41952 | 796,83660 | 1252,26377 | €464,69 | €1.394,07 | €51,63 | €25,95 |
| 1H Fast V3 No Esports Stress Guard V1 | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 273,49469 | 273,44000 | 265,08718 | 183,69727 | 286,10595 | €582,59 | €1.747,77 | €53,73 | €-0,35 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | HEMI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01177 | 0,01177 | 0,01065 | 0,00790 | 0,01345 | €163,25 | €489,75 | €46,69 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | PROM | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 6,92735 | 6,92735 | 6,35093 | 4,65287 | 7,79198 | €191,37 | €574,11 | €47,77 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1207,83152 | 1208,44000 | 1163,18307 | 811,26017 | 1274,80418 | €447,04 | €1.341,11 | €49,58 | €0,68 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | BTC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 80317,26024 | 79715,87000 | 79417,70693 | 53946,42646 | 81666,59021 | €10,38 | €31,14 | €0,35 | €-0,23 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | NEAR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,38548 | 2,42700 | 2,30355 | 1,60225 | 2,50836 | €463,10 | €1.389,30 | €47,71 | €24,18 |
| Ampia 4H | SPCX | LONG | Confluenza trend | 240m | 2,0x | 136,56189 | 136,56189 | 126,46637 | 68,96375 | 164,82935 | €323,86 | €647,73 | €47,88 | €0,00 |
| Ampia 4H | VELVET | LONG | Confluenza trend | 240m | 2,0x | 0,55987 | 0,55987 | 0,49269 | 0,28274 | 0,74799 | €201,63 | €403,26 | €48,39 | €0,00 |
| Ampia 4H | LINK | LONG | Confluenza trend | 240m | 2,0x | 11,96839 | 11,96839 | 11,08055 | 6,04404 | 14,45436 | €14,07 | €28,15 | €2,09 | €0,00 |
| Ampia 4H | ETH | LONG | Confluenza trend | 240m | 2,0x | 2430,03591 | 2501,94000 | 2267,54364 | 1227,16813 | 2885,01426 | €18,82 | €37,65 | €2,52 | €1,11 |
| Ampia 4H | HYPE | LONG | Confluenza trend | 240m | 2,0x | 79,31286 | 86,35400 | 70,73982 | 40,05299 | 103,31737 | €13,82 | €27,64 | €2,99 | €2,45 |
| Ampia 4H | TRUMP | LONG | Confluenza trend | 240m | 2,0x | 2,37347 | 2,37347 | 2,08866 | 1,19860 | 3,17096 | €210,83 | €421,66 | €50,60 | €0,00 |
| Ampia 4H | SOL | LONG | Confluenza trend | 240m | 2,0x | 103,77875 | 105,25300 | 96,79200 | 52,40827 | 123,34165 | €13,62 | €27,23 | €1,83 | €0,39 |
| Ampia 4H | XRP | LONG | Confluenza trend | 240m | 2,0x | 1,42001 | 1,40809 | 1,35851 | 0,71711 | 1,59222 | €12,52 | €25,04 | €1,08 | €-0,21 |
| Ampia 4H | UNI | LONG | Confluenza trend | 240m | 2,0x | 6,98040 | 7,00700 | 6,22147 | 3,52510 | 9,10539 | €214,19 | €428,38 | €46,57 | €1,63 |
| Forza relativa 1H V1 | BTR | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,05109 | 0,05109 | 0,05109 | 0,07638 | 0,03760 | €174,72 | €349,43 | €0,00 | €-0,00 |
| Forza relativa 1H V1 | ARB | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,13283 | 0,17410 | 0,12480 | 0,06708 | 0,15050 | €352,71 | €705,43 | €42,65 | €219,20 |
| Forza relativa 1H V1 | PEPE | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00001 | 0,00000 | €661,53 | €1.323,06 | €41,35 | €-0,00 |
| Forza relativa 1H V1 | DASH | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 69,34387 | 70,79000 | 63,21411 | 35,01865 | 82,82933 | €20,72 | €41,45 | €3,66 | €0,86 |
| Forza relativa 1H V1 | NEAR | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 2,37648 | 2,42700 | 2,26708 | 1,20012 | 2,61715 | €474,73 | €949,47 | €43,71 | €20,19 |
| Forza relativa 1H V1 | HYPE | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 87,57151 | 86,35400 | 85,96029 | 44,22361 | 91,11620 | €88,01 | €176,03 | €3,24 | €-2,45 |
| Forza relativa 1H V1 | UNI | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 7,16543 | 7,00700 | 6,92567 | 3,61854 | 7,69291 | €13,42 | €26,84 | €0,90 | €-0,59 |
| Forza relativa 1H V2 | BEAT | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,25984 | 0,25984 | 0,25657 | 0,38847 | 0,19125 | €200,38 | €400,75 | €0,00 | €-0,00 |
| Forza relativa 1H V2 | TUT | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,04452 | 0,04452 | 0,04986 | 0,06656 | 0,03277 | €204,64 | €409,28 | €49,11 | €-0,00 |
| Forza relativa 1H V2 | ADA | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,20283 | 0,20283 | 0,20884 | 0,30323 | 0,18961 | €17,52 | €35,04 | €1,04 | €-0,00 |
| Forza relativa 1H V2 | HEMI | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €200,86 | €401,72 | €48,21 | €0,00 |
| Forza relativa 1H V2 | BTR | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,05109 | 0,05109 | 0,05109 | 0,07638 | 0,03760 | €205,02 | €410,03 | €0,00 | €-0,00 |
| Forza relativa 1H V2 | TAO | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 273,49469 | 273,44000 | 262,68503 | 138,11482 | 297,27592 | €14,32 | €28,64 | €1,13 | €-0,01 |
| Benchmark Donchian breakout 1H | SKHYNIX | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1174,33482 | 1174,33482 | 1128,44989 | 593,03908 | 1289,04713 | €641,25 | €1.282,50 | €50,11 | €0,00 |
| Benchmark Donchian breakout 1H | VELVET | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,14787 | 0,14787 | 0,16561 | 0,22107 | 0,10351 | €237,23 | €474,47 | €56,94 | €-0,00 |
| Benchmark Donchian breakout 1H | ADA | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,20283 | 0,20283 | 0,20951 | 0,30323 | 0,18614 | €72,87 | €145,74 | €4,80 | €-0,00 |
| Benchmark Donchian breakout 1H | PEPE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00001 | 0,00000 | €794,09 | €1.588,18 | €58,23 | €-0,00 |
| Benchmark Donchian breakout 1H | ETH | LONG | Donchian breakout 20 barre | 60m | 2,0x | 2486,95729 | 2501,94000 | 2447,16598 | 1255,91343 | 2586,43558 | €1.753,97 | €3.507,94 | €56,13 | €21,13 |
| Benchmark Donchian breakout 1H | SOL | LONG | Donchian breakout 20 barre | 60m | 2,0x | 105,92618 | 105,25300 | 104,23136 | 53,49272 | 110,16323 | €20,43 | €40,86 | €0,65 | €-0,26 |
| Donchian 1H Gb20 120R V1 | SKHYNIX | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1174,33482 | 1174,33482 | 1128,44989 | 593,03908 | 1289,04713 | €626,15 | €1.252,30 | €48,93 | €0,00 |
| Donchian 1H Gb20 120R V1 | VELVET | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,14787 | 0,14787 | 0,16561 | 0,22107 | 0,10351 | €231,65 | €463,30 | €55,60 | €-0,00 |
| Donchian 1H Gb20 120R V1 | ADA | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,20283 | 0,20283 | 0,20951 | 0,30323 | 0,18614 | €71,16 | €142,31 | €4,68 | €-0,00 |
| Donchian 1H Gb20 120R V1 | PEPE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00001 | 0,00000 | €775,40 | €1.550,79 | €56,86 | €-0,00 |
| Donchian 1H Gb20 120R V1 | ETH | LONG | Donchian breakout 20 barre | 60m | 2,0x | 2486,95729 | 2501,94000 | 2447,16598 | 1255,91343 | 2586,43558 | €1.712,67 | €3.425,35 | €54,81 | €20,64 |
| Donchian 1H Gb20 120R V1 | SOL | LONG | Donchian breakout 20 barre | 60m | 2,0x | 105,92618 | 105,25300 | 104,23136 | 53,49272 | 110,16323 | €19,95 | €39,90 | €0,64 | €-0,25 |
| Benchmark trend following EMA 1H | BEAT | SHORT | Trend following EMA | 60m | 2,0x | 0,28257 | 0,28257 | 0,25706 | 0,42244 | 0,20797 | €186,11 | €372,23 | €0,00 | €-0,00 |
| Benchmark trend following EMA 1H | TUT | SHORT | Trend following EMA | 60m | 2,0x | 0,04446 | 0,04446 | 0,04980 | 0,06647 | 0,03272 | €194,70 | €389,39 | €46,73 | €-0,00 |
| Benchmark trend following EMA 1H | VELVET | SHORT | Trend following EMA | 60m | 2,0x | 0,14786 | 0,14786 | 0,16560 | 0,22105 | 0,10883 | €187,91 | €375,83 | €45,10 | €-0,00 |
| Benchmark trend following EMA 1H | ARB | LONG | Trend following EMA | 60m | 2,0x | 0,13283 | 0,17410 | 0,12390 | 0,06708 | 0,15246 | €341,57 | €683,14 | €45,90 | €212,27 |
| Benchmark trend following EMA 1H | UNI | LONG | Trend following EMA | 60m | 2,0x | 7,07742 | 7,00700 | 6,75804 | 3,57409 | 7,78005 | €71,53 | €143,05 | €6,46 | €-1,42 |
| Scanner Top 5 Long 1H | BOME | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00160 | €218,24 | €436,47 | €52,38 | €0,00 |
| Scanner Top 5 Long 1H | TRUMP | LONG | Scanner Top 5 Long | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,08367 | €238,89 | €477,78 | €55,13 | €0,00 |
| Scanner Top 5 Long 1H | SKHYNIX | LONG | Scanner Top 5 Long | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1331,36020 | €17,74 | €35,49 | €0,91 | €0,00 |
| Scanner Top 5 Long 1H | HEMI | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €228,24 | €456,48 | €54,78 | €0,00 |
| Scanner Top 5 Long 1H | ARB | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,13283 | 0,17410 | 0,12480 | 0,06708 | 0,14889 | €453,65 | €907,29 | €54,86 | €281,93 |
| Scanner Top 5 Long 1H | ZEC | LONG | Scanner Top 5 Long | 60m | 2,0x | 1215,33302 | 1208,44000 | 1158,91544 | 613,74317 | 1328,16817 | €13,38 | €26,76 | €1,24 | €-0,15 |
| Scanner Top 5 Long 1H | ETH | LONG | Scanner Top 5 Long | 60m | 2,0x | 2501,94029 | 2501,94000 | 2465,91235 | 1263,47985 | 2573,99617 | €260,98 | €521,97 | €7,52 | €-0,00 |
| Scanner Bottom 5 Short 1H | SOXL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €378,86 | €757,72 | €48,07 | €-0,00 |
| Scanner Bottom 5 Short 1H | SNDK | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €492,80 | €985,60 | €47,71 | €-0,00 |
| Scanner Bottom 5 Short 1H | VELVET | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €191,07 | €382,14 | €0,00 | €-0,00 |
| Scanner Bottom 5 Short 1H | TUT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €178,38 | €356,76 | €42,81 | €-0,00 |
| Scanner Top10 Long | TAO | LONG | Scanner Top10 Long | 60m | 2,0x | 247,38947 | 273,44000 | 237,94346 | 124,93168 | 266,28148 | €678,43 | €1.356,86 | €51,81 | €142,88 |
| Scanner Top10 Long | SKHYNIX | LONG | Scanner Top10 Long | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €972,86 | €1.945,72 | €48,38 | €0,00 |
| Scanner Top10 Long | HEMI | LONG | Scanner Top10 Long | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €207,88 | €415,77 | €49,89 | €0,00 |
| Scanner Top10 Long | ARB | LONG | Scanner Top10 Long | 60m | 2,0x | 0,13283 | 0,17410 | 0,12480 | 0,06708 | 0,14889 | €422,09 | €844,19 | €51,04 | €262,32 |
| Scanner Top10 Long | UNI | LONG | Scanner Top10 Long | 60m | 2,0x | 7,14143 | 7,00700 | 6,87560 | 3,60642 | 7,67309 | €15,10 | €30,20 | €1,12 | €-0,57 |
| Scanner Top10 Long | SOL | LONG | Scanner Top10 Long | 60m | 2,0x | 105,69714 | 105,25300 | 104,13756 | 53,37705 | 108,81629 | €21,20 | €42,41 | €0,63 | €-0,18 |
| Scanner Top10 Long | ZEC | LONG | Scanner Top10 Long | 60m | 2,0x | 1186,35722 | 1208,44000 | 1129,86589 | 599,11040 | 1299,33988 | €83,79 | €167,58 | €7,98 | €3,12 |
| Scanner Top10 Long | NEAR | LONG | Scanner Top10 Long | 60m | 2,0x | 2,42749 | 2,42700 | 2,32276 | 1,22588 | 2,63693 | €18,65 | €37,30 | €1,61 | €-0,01 |
| Scanner Bottom10 Short | SOXL | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom10 Short | SNDK | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Bottom10 Short | VELVET | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €194,19 | €388,38 | €0,00 | €-0,00 |
| Scanner Bottom10 Short | TUT | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €181,31 | €362,61 | €43,51 | €-0,00 |
| Scanner Top15 Long | NEAR | LONG | Scanner Top15 Long | 60m | 2,0x | 2,08142 | 2,42700 | 2,00650 | 1,05112 | 2,23125 | €16,79 | €33,59 | €1,21 | €5,58 |
| Scanner Top15 Long | TAO | LONG | Scanner Top15 Long | 60m | 2,0x | 247,38947 | 273,44000 | 237,94346 | 124,93168 | 266,28148 | €88,53 | €177,07 | €6,76 | €18,65 |
| Scanner Top15 Long | TRUMP | LONG | Scanner Top15 Long | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,08367 | €215,87 | €431,75 | €49,81 | €0,00 |
| Scanner Top15 Long | SKHYNIX | LONG | Scanner Top15 Long | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €787,36 | €1.574,72 | €39,16 | €0,00 |
| Scanner Top15 Long | ARB | LONG | Scanner Top15 Long | 60m | 2,0x | 0,13283 | 0,17410 | 0,12480 | 0,06708 | 0,14889 | €426,02 | €852,04 | €51,52 | €264,76 |
| Scanner Top15 Long | DASH | LONG | Scanner Top15 Long | 60m | 2,0x | 69,34387 | 70,79000 | 63,21411 | 35,01865 | 81,60338 | €295,33 | €590,66 | €52,21 | €12,32 |
| Scanner Top15 Long | ZEC | LONG | Scanner Top15 Long | 60m | 2,0x | 1207,83152 | 1208,44000 | 1150,42638 | 609,95492 | 1322,64180 | €84,93 | €169,86 | €8,07 | €0,09 |
| Scanner Top15 Long | UNI | LONG | Scanner Top15 Long | 60m | 2,0x | 7,12843 | 7,00700 | 6,87194 | 3,59985 | 7,64140 | €88,01 | €176,02 | €6,33 | €-3,00 |
| Scanner Top15 Long | SOL | LONG | Scanner Top15 Long | 60m | 2,0x | 105,69714 | 105,25300 | 104,13756 | 53,37705 | 108,81629 | €23,28 | €46,56 | €0,69 | €-0,20 |
| Scanner Bottom15 Short | SOXL | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom15 Short | SNDK | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Bottom15 Short | VELVET | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €194,19 | €388,38 | €0,00 | €-0,00 |
| Scanner Bottom15 Short | TUT | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €181,31 | €362,61 | €43,51 | €-0,00 |
| Scanner Top20 Long | NEAR | LONG | Scanner Top20 Long | 60m | 2,0x | 2,08142 | 2,42700 | 2,00650 | 1,05112 | 2,23125 | €16,79 | €33,59 | €1,21 | €5,58 |
| Scanner Top20 Long | TAO | LONG | Scanner Top20 Long | 60m | 2,0x | 247,38947 | 273,44000 | 237,94346 | 124,93168 | 266,28148 | €88,53 | €177,07 | €6,76 | €18,65 |
| Scanner Top20 Long | TRUMP | LONG | Scanner Top20 Long | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,08367 | €215,87 | €431,75 | €49,81 | €0,00 |
| Scanner Top20 Long | SKHYNIX | LONG | Scanner Top20 Long | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €787,36 | €1.574,72 | €39,16 | €0,00 |
| Scanner Top20 Long | ARB | LONG | Scanner Top20 Long | 60m | 2,0x | 0,13283 | 0,17410 | 0,12480 | 0,06708 | 0,14889 | €426,02 | €852,04 | €51,52 | €264,76 |
| Scanner Top20 Long | DASH | LONG | Scanner Top20 Long | 60m | 2,0x | 69,34387 | 70,79000 | 63,21411 | 35,01865 | 81,60338 | €295,33 | €590,66 | €52,21 | €12,32 |
| Scanner Top20 Long | ZEC | LONG | Scanner Top20 Long | 60m | 2,0x | 1207,83152 | 1208,44000 | 1150,42638 | 609,95492 | 1322,64180 | €84,93 | €169,86 | €8,07 | €0,09 |
| Scanner Top20 Long | UNI | LONG | Scanner Top20 Long | 60m | 2,0x | 7,12843 | 7,00700 | 6,87194 | 3,59985 | 7,64140 | €88,01 | €176,02 | €6,33 | €-3,00 |
| Scanner Top20 Long | SOL | LONG | Scanner Top20 Long | 60m | 2,0x | 105,69714 | 105,25300 | 104,13756 | 53,37705 | 108,81629 | €23,28 | €46,56 | €0,69 | €-0,20 |
| Scanner Bottom20 Short | SOXL | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom20 Short | SNDK | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Bottom20 Short | VELVET | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €194,19 | €388,38 | €0,00 | €-0,00 |
| Scanner Bottom20 Short | TUT | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €181,31 | €362,61 | €43,51 | €-0,00 |
| Scanner Top 5 + forza BTC 1H | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €203,45 | €406,91 | €48,83 | €0,00 |
| Scanner Top 5 + forza BTC 1H | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,14149 | €223,03 | €446,06 | €51,47 | €0,00 |
| Scanner Top 5 + forza BTC 1H | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €18,23 | €36,45 | €0,93 | €0,00 |
| Scanner Top 5 + forza BTC 1H | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €213,35 | €426,70 | €51,20 | €0,00 |
| Scanner Top 5 + forza BTC 1H | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,13283 | 0,17410 | 0,12480 | 0,06708 | 0,15050 | €424,88 | €849,77 | €51,38 | €264,05 |
| Scanner Top 5 + forza BTC 1H | UNI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 7,09542 | 7,00700 | 6,78408 | 3,58319 | 7,78036 | €17,99 | €35,98 | €1,58 | €-0,45 |
| Scanner Top 5 + forza BTC 1H | NEAR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,37648 | 2,42700 | 2,26708 | 1,20012 | 2,61715 | €69,93 | €139,86 | €6,44 | €2,97 |
| Scanner Top5 Btc Mfe V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €190,73 | €381,46 | €45,77 | €0,00 |
| Scanner Top5 Btc Mfe V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,14149 | €209,08 | €418,16 | €48,25 | €0,00 |
| Scanner Top5 Btc Mfe V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €17,09 | €34,17 | €0,88 | €0,00 |
| Scanner Top5 Btc Mfe V1 | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €200,01 | €400,01 | €48,00 | €0,00 |
| Scanner Top5 Btc Mfe V1 | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,13283 | 0,17410 | 0,12480 | 0,06708 | 0,15050 | €398,31 | €796,61 | €48,17 | €247,53 |
| Scanner Top5 Btc Mfe V1 | UNI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 7,09542 | 7,00700 | 6,78408 | 3,58319 | 7,78036 | €16,86 | €33,73 | €1,48 | €-0,42 |
| Scanner Top5 Btc Mfe V1 | NEAR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,37648 | 2,42700 | 2,26708 | 1,20012 | 2,61715 | €65,55 | €131,11 | €6,04 | €2,79 |
| Scanner Top5 Btc Guard V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €197,27 | €394,55 | €47,35 | €0,00 |
| Scanner Top5 Btc Guard V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,55551 | 2,55551 | 2,29388 | 1,29053 | 3,13109 | €13,03 | €26,06 | €2,67 | €0,00 |
| Scanner Top5 Btc Guard V1 | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €195,03 | €390,06 | €46,81 | €0,00 |
| Scanner Top5 Btc Guard V1 | ZORA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00942 | 0,00942 | 0,00829 | 0,00476 | 0,01191 | €192,06 | €384,12 | €46,09 | €0,00 |
| Scanner Top5 Btc Guard V1 | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,13283 | 0,17410 | 0,12480 | 0,06708 | 0,15050 | €401,05 | €802,11 | €48,50 | €249,24 |
| Scanner Top5 Btc Guard V1 | DASH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 69,34387 | 70,79000 | 63,21411 | 35,01865 | 82,82933 | €15,44 | €30,88 | €2,73 | €0,64 |
| Scanner Top5 Btc Guard V1 | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1207,83152 | 1208,44000 | 1150,42638 | 609,95492 | 1334,12283 | €61,52 | €123,04 | €5,85 | €0,06 |
| Scanner Top5 Btc Btc Le3 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €847,75 | €1.695,49 | €43,45 | €0,00 |
| Scanner Top5 Btc Btc Le3 V1 | 0G | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,24373 | 0,24373 | 0,21916 | 0,12308 | 0,29778 | €215,80 | €431,60 | €43,51 | €0,00 |
| Scanner Top5 Btc Btc Le3 V1 | NEAR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,37648 | 2,42700 | 2,26708 | 1,20012 | 2,61715 | €466,33 | €932,66 | €42,93 | €19,83 |
| Scanner Top5 Btc Btc Le3 V1 | DASH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 68,88377 | 70,79000 | 63,76753 | 34,78631 | 80,13952 | €14,76 | €29,52 | €2,19 | €0,82 |
| Scanner Top5 Btc Btc Le3 V1 | UNI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 7,16543 | 7,00700 | 6,92567 | 3,61854 | 7,69291 | €17,38 | €34,75 | €1,16 | €-0,77 |
| Scanner Top5 Btc Btc Le3 V1 | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1190,40803 | 1208,44000 | 1137,90085 | 601,15606 | 1305,92385 | €473,42 | €946,84 | €41,76 | €14,34 |
| Scanner Top5 Btc Btc 2 3 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €891,28 | €1.782,56 | €45,68 | €0,00 |
| Scanner Top5 Btc Btc 2 3 V1 | MARSCOIN | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,25201 | 0,25201 | 0,22177 | 0,12727 | 0,31854 | €188,32 | €376,64 | €45,20 | €0,00 |
| Scanner Top5 Btc Btc 2 3 V1 | UNI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 7,09542 | 7,00700 | 6,78408 | 3,58319 | 7,78036 | €17,98 | €35,96 | €1,58 | €-0,45 |
| Scanner Top5 Btc Btc 2 3 V1 | NEAR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,37648 | 2,42700 | 2,26708 | 1,20012 | 2,61715 | €473,04 | €946,07 | €43,55 | €20,11 |
| Scanner Top5 Btc Guard Mfe V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €192,69 | €385,37 | €46,24 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,55551 | 2,55551 | 2,29388 | 1,29053 | 3,13109 | €12,72 | €25,45 | €2,61 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €190,49 | €380,99 | €45,72 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | ZORA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00942 | 0,00942 | 0,00829 | 0,00476 | 0,01191 | €187,59 | €375,19 | €45,02 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,13283 | 0,17410 | 0,12480 | 0,06708 | 0,15050 | €391,73 | €783,45 | €47,37 | €243,44 |
| Scanner Top5 Btc Guard Mfe V1 | DASH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 69,34387 | 70,79000 | 63,21411 | 35,01865 | 82,82933 | €15,08 | €30,17 | €2,67 | €0,63 |
| Scanner Top5 Btc Guard Mfe V1 | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1207,83152 | 1208,44000 | 1150,42638 | 609,95492 | 1334,12283 | €60,09 | €120,18 | €5,71 | €0,06 |
| Scanner Top5 Btc Guard Btc Le3 V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,55551 | 2,55551 | 2,29388 | 1,29053 | 3,13109 | €12,70 | €25,40 | €2,60 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €191,20 | €382,39 | €45,89 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | PROM | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 7,01991 | 7,01991 | 6,30832 | 3,54505 | 8,58541 | €213,89 | €427,78 | €43,36 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | ZORA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00942 | 0,00942 | 0,00829 | 0,00476 | 0,01191 | €188,34 | €376,68 | €45,20 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | NEAR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,37648 | 2,42700 | 2,26708 | 1,20012 | 2,61715 | €32,15 | €64,31 | €2,96 | €1,37 |
| Scanner Top5 Btc Guard Btc Le3 V1 | UNI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 7,14143 | 7,00700 | 6,87560 | 3,60642 | 7,72626 | €12,97 | €25,94 | €0,97 | €-0,49 |
| Scanner Top5 Btc Guard Btc Le3 V1 | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1190,40803 | 1208,44000 | 1137,90085 | 601,15606 | 1305,92385 | €509,37 | €1.018,74 | €44,94 | €15,43 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | ZORA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00942 | 0,00942 | 0,00829 | 0,00476 | 0,01191 | €185,37 | €370,74 | €44,49 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | MARSCOIN | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,25201 | 0,25201 | 0,22177 | 0,12727 | 0,31854 | €186,87 | €373,73 | €44,85 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1207,83152 | 1208,44000 | 1150,42638 | 609,95492 | 1334,12283 | €469,07 | €938,15 | €44,59 | €0,47 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | DASH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 70,93418 | 70,79000 | 66,36043 | 35,82176 | 80,99644 | €23,68 | €47,37 | €3,05 | €-0,10 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | TAO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 273,49469 | 273,44000 | 262,68503 | 138,11482 | 297,27592 | €562,94 | €1.125,89 | €44,50 | €-0,23 |
| Scanner Top5 Btc Runner25 V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00176 | €210,95 | €421,90 | €50,63 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1363,81560 | €965,52 | €1.931,04 | €49,49 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01601 | €209,51 | €419,03 | €50,28 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,13283 | 0,17410 | 0,12480 | 0,06708 | 0,15692 | €27,23 | €54,45 | €3,29 | €16,92 |
| Scanner Top5 Btc Runner25 V1 | UNI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 7,09542 | 7,00700 | 6,78408 | 3,58319 | 8,02944 | €21,18 | €42,36 | €1,86 | €-0,53 |
| Scanner Top5 Btc Runner25 V1 | NEAR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,37648 | 2,42700 | 2,26708 | 1,20012 | 2,70466 | €545,89 | €1.091,78 | €50,26 | €23,21 |
| Scanner Top5 Btc Tp3 V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00176 | €211,07 | €422,14 | €50,66 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1363,81560 | €966,09 | €1.932,17 | €49,52 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01601 | €209,64 | €419,27 | €50,31 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,13283 | 0,17410 | 0,12480 | 0,06708 | 0,15692 | €27,24 | €54,49 | €3,29 | €16,93 |
| Scanner Top5 Btc Tp3 V1 | UNI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 7,09542 | 7,00700 | 6,78408 | 3,58319 | 8,02944 | €21,19 | €42,39 | €1,86 | €-0,53 |
| Scanner Top5 Btc Tp3 V1 | NEAR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,37648 | 2,42700 | 2,26708 | 1,20012 | 2,70466 | €546,21 | €1.092,42 | €50,29 | €23,23 |
| Combo Trend | BEAT | SHORT | Combo Trend | 60m | 2,0x | 0,25984 | 0,25984 | 0,25657 | 0,38847 | 0,19125 | €193,71 | €387,42 | €0,00 | €-0,00 |
| Combo Trend | ADA | SHORT | Combo Trend | 60m | 2,0x | 0,19986 | 0,19986 | 0,20356 | 0,29879 | 0,19173 | €1.205,82 | €2.411,64 | €44,61 | €-0,00 |
| Combo Trend | BTR | SHORT | Combo Trend | 60m | 2,0x | 0,05109 | 0,05109 | 0,05109 | 0,07638 | 0,03760 | €188,04 | €376,08 | €0,00 | €-0,00 |
| Combo Trend | ARB | LONG | Combo Trend | 60m | 2,0x | 0,13283 | 0,17410 | 0,12390 | 0,06708 | 0,15246 | €327,77 | €655,53 | €44,04 | €203,69 |
| Combo Trend | SOL | LONG | Combo Trend | 60m | 2,0x | 105,92618 | 105,25300 | 104,23136 | 53,49272 | 109,65478 | €19,15 | €38,30 | €0,61 | €-0,24 |
| Combo Trend | UNI | LONG | Combo Trend | 60m | 2,0x | 7,07742 | 7,00700 | 6,75804 | 3,57409 | 7,78005 | €68,62 | €137,24 | €6,19 | €-1,37 |
| Combo Mean Reversion | ADA | LONG | Combo Mean Reversion | 60m | 2,0x | 0,20284 | 0,20284 | 0,19804 | 0,10244 | 0,21052 | €942,00 | €1.883,99 | €44,59 | €0,00 |
| Combo Scanner | BOME | LONG | Combo Scanner | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €195,20 | €390,40 | €46,85 | €0,00 |
| Combo Scanner | TRUMP | LONG | Combo Scanner | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,14149 | €213,98 | €427,96 | €49,38 | €0,00 |
| Combo Scanner | SKHYNIX | LONG | Combo Scanner | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €24,78 | €49,55 | €1,27 | €0,00 |
| Combo Scanner | ARB | LONG | Combo Scanner | 60m | 2,0x | 0,13283 | 0,17410 | 0,12480 | 0,06708 | 0,15050 | €419,07 | €838,14 | €50,68 | €260,44 |
| Combo Scanner | UNI | LONG | Combo Scanner | 60m | 2,0x | 7,09542 | 7,00700 | 6,78408 | 3,58319 | 7,78036 | €583,31 | €1.166,62 | €51,19 | €-14,54 |
| Combo Scanner | NEAR | LONG | Combo Scanner | 60m | 2,0x | 2,37648 | 2,42700 | 2,26708 | 1,20012 | 2,61715 | €21,23 | €42,45 | €1,95 | €0,90 |
| Combo Scanner | DASH | LONG | Combo Scanner | 60m | 2,0x | 70,93418 | 70,79000 | 66,36043 | 35,82176 | 80,99644 | €81,07 | €162,13 | €10,45 | €-0,33 |
| Combo Adaptive | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,01735 | 121,01735 | 128,90956 | 180,92093 | 105,23292 | €367,30 | €734,61 | €47,91 | €-0,00 |
| Combo Adaptive | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 273,44000 | 237,94346 | 124,93168 | 266,28148 | €40,89 | €81,77 | €3,12 | €8,61 |
| Combo Adaptive | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,52450 | 2,33981 | 1,27487 | 2,89389 | €18,69 | €37,37 | €2,73 | €0,00 |
| Combo Adaptive | 0G | LONG | Combo Adaptive | 60m | 2,0x | 0,23904 | 0,23904 | 0,21329 | 0,12072 | 0,29055 | €230,13 | €460,26 | €49,58 | €0,00 |
| Combo Adaptive | BTR | SHORT | Combo Adaptive | 60m | 2,0x | 0,04853 | 0,04853 | 0,04853 | 0,07255 | 0,03688 | €212,51 | €425,02 | €0,00 | €-0,00 |
| Combo Adaptive | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,13283 | 0,17410 | 0,12480 | 0,06708 | 0,14889 | €420,61 | €841,21 | €50,86 | €261,39 |
| Combo Adaptive | UNI | LONG | Combo Adaptive | 60m | 2,0x | 7,16543 | 7,00700 | 6,92567 | 3,61854 | 7,64496 | €12,79 | €25,58 | €0,86 | €-0,57 |
| Combo Adaptive | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 2,41248 | 2,42700 | 2,30417 | 1,21830 | 2,62911 | €89,29 | €178,57 | €8,02 | €1,07 |
| Combo Adaptive Mfe Trail | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 273,44000 | 237,94346 | 124,93168 | 266,28148 | €54,29 | €108,58 | €4,15 | €11,43 |
| Combo Adaptive Mfe Trail | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,52450 | 2,33981 | 1,27487 | 2,89389 | €315,75 | €631,50 | €46,20 | €0,00 |
| Combo Adaptive Mfe Trail | TUT | SHORT | Combo Adaptive | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €190,04 | €380,09 | €45,61 | €-0,00 |
| Combo Adaptive Mfe Trail | PROM | LONG | Combo Adaptive | 60m | 2,0x | 7,01991 | 7,01991 | 6,30832 | 3,54505 | 8,44309 | €21,72 | €43,45 | €4,40 | €0,00 |
| Combo Adaptive Mfe Trail | BTR | SHORT | Combo Adaptive | 60m | 2,0x | 0,04991 | 0,04991 | 0,04841 | 0,07462 | 0,03793 | €142,63 | €285,27 | €0,00 | €-0,00 |
| Combo Adaptive Mfe Trail | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,13283 | 0,17410 | 0,12480 | 0,06708 | 0,14889 | €367,37 | €734,74 | €44,43 | €228,31 |
| Combo Adaptive Mfe Trail | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 1191,60827 | 1208,44000 | 1134,66326 | 601,76218 | 1305,49830 | €70,67 | €141,33 | €6,75 | €2,00 |
| Combo Adaptive Quality7 V1 | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €371,68 | €743,36 | €47,16 | €-0,00 |
| Combo Adaptive Quality7 V1 | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 273,44000 | 237,94346 | 124,93168 | 266,28148 | €646,78 | €1.293,57 | €49,39 | €136,22 |
| Combo Adaptive Quality7 V1 | ZORA | LONG | Combo Adaptive | 60m | 2,0x | 0,00942 | 0,00942 | 0,00829 | 0,00476 | 0,01169 | €199,23 | €398,46 | €47,81 | €0,00 |
| Combo Adaptive Quality7 V1 | 0G | LONG | Combo Adaptive | 60m | 2,0x | 0,24605 | 0,24605 | 0,22046 | 0,12425 | 0,29722 | €220,81 | €441,63 | €45,92 | €0,00 |
| Combo Adaptive Regime V1 | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €987,06 | €1.974,12 | €49,09 | €0,00 |
| Combo Adaptive Long Only V1 | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 2,08142 | 2,42700 | 2,00650 | 1,05112 | 2,23125 | €645,48 | €1.290,95 | €46,47 | €214,34 |
| Combo Adaptive Long Only V1 | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,52450 | 2,33981 | 1,27487 | 2,89389 | €48,12 | €96,24 | €7,04 | €0,00 |
| Combo Adaptive Long Only V1 | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1331,36020 | €968,99 | €1.937,97 | €49,66 | €0,00 |
| Combo Adaptive Long Only V1 | HEMI | LONG | Combo Adaptive | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €216,09 | €432,18 | €51,86 | €0,00 |
| Combo Adaptive Long Only V1 | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,13283 | 0,17410 | 0,12480 | 0,06708 | 0,14889 | €436,65 | €873,31 | €52,81 | €271,36 |
| Combo Adaptive Long Only V1 | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 1207,83152 | 1208,44000 | 1150,42638 | 609,95492 | 1322,64180 | €82,44 | €164,87 | €7,84 | €0,08 |
| Combo Adaptive Long Only V1 | DASH | LONG | Combo Adaptive | 60m | 2,0x | 70,98419 | 70,79000 | 65,99178 | 35,84702 | 80,96902 | €44,54 | €89,07 | €6,26 | €-0,24 |
| Combo Adaptive Long Only V1 | ETH | LONG | Combo Adaptive | 60m | 2,0x | 2503,97069 | 2501,94000 | 2467,91352 | 1264,50520 | 2576,08505 | €14,64 | €29,28 | €0,42 | €-0,02 |
| Combo Adaptive Long Only V1 | UNI | LONG | Combo Adaptive | 60m | 2,0x | 7,16543 | 7,00700 | 6,92567 | 3,61854 | 7,64496 | €15,48 | €30,96 | €1,04 | €-0,68 |
| Combo Adaptive Partial 1R V1 | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,01735 | 121,01735 | 128,90956 | 180,92093 | 105,23292 | €352,70 | €705,40 | €46,00 | €-0,00 |
| Combo Adaptive Partial 1R V1 | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,52450 | 2,33981 | 1,27487 | 2,89389 | €347,19 | €694,38 | €50,80 | €0,00 |
| Combo Adaptive Partial 1R V1 | VELVET | SHORT | Combo Adaptive | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €207,76 | €415,52 | €0,00 | €-0,00 |
| Combo Adaptive Partial 1R V1 | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €1.013,20 | €2.026,40 | €50,39 | €0,00 |
| Combo Adaptive Partial 1R V1 | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,18396 | 0,17410 | 0,16947 | 0,09290 | 0,21294 | €25,44 | €50,88 | €4,01 | €-2,73 |
| Combo Adaptive Runner25 V1 | 0G | LONG | Combo Adaptive | 60m | 2,0x | 0,23904 | 0,23904 | 0,21329 | 0,12072 | 0,31630 | €204,19 | €408,39 | €43,99 | €0,00 |
| Combo Adaptive Runner25 V1 | BTR | SHORT | Combo Adaptive | 60m | 2,0x | 0,04991 | 0,04991 | 0,04991 | 0,07462 | 0,03194 | €182,83 | €365,66 | €0,00 | €-0,00 |
| Combo Adaptive Runner25 V1 | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,13283 | 0,17410 | 0,12480 | 0,06708 | 0,15692 | €376,21 | €752,41 | €45,50 | €233,80 |
| Combo Adaptive Runner25 V1 | SOL | LONG | Combo Adaptive | 60m | 2,0x | 105,34306 | 105,25300 | 103,60820 | 53,19825 | 110,54767 | €199,12 | €398,24 | €6,56 | €-0,34 |
| Combo Adaptive Runner25 V1 | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 1207,83152 | 1208,44000 | 1150,42638 | 609,95492 | 1380,04694 | €24,90 | €49,79 | €2,37 | €0,03 |
| Combo Adaptive Runner25 V1 | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 2,41748 | 2,42700 | 2,30912 | 1,22083 | 2,74258 | €524,28 | €1.048,57 | €47,00 | €4,13 |
| Combo Adaptive Runner25 V1 | UNI | LONG | Combo Adaptive | 60m | 2,0x | 7,16543 | 7,00700 | 6,92567 | 3,61854 | 7,88472 | €17,00 | €34,01 | €1,14 | €-0,75 |
| Combo Adaptive Tp3 V1 | 0G | LONG | Combo Adaptive | 60m | 2,0x | 0,23904 | 0,23904 | 0,21329 | 0,12072 | 0,31630 | €200,38 | €400,76 | €43,17 | €0,00 |
| Combo Adaptive Tp3 V1 | BTR | SHORT | Combo Adaptive | 60m | 2,0x | 0,04991 | 0,04991 | 0,04991 | 0,07462 | 0,03194 | €179,40 | €358,80 | €0,00 | €-0,00 |
| Combo Adaptive Tp3 V1 | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,13283 | 0,17410 | 0,12480 | 0,06708 | 0,15692 | €369,17 | €738,34 | €44,64 | €229,42 |
| Combo Adaptive Tp3 V1 | SOL | LONG | Combo Adaptive | 60m | 2,0x | 105,34306 | 105,25300 | 103,60820 | 53,19825 | 110,54767 | €195,44 | €390,89 | €6,44 | €-0,33 |
| Combo Adaptive Tp3 V1 | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 1207,83152 | 1208,44000 | 1150,42638 | 609,95492 | 1380,04694 | €24,43 | €48,86 | €2,32 | €0,02 |
| Combo Adaptive Tp3 V1 | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 2,41748 | 2,42700 | 2,30912 | 1,22083 | 2,74258 | €514,48 | €1.028,95 | €46,12 | €4,05 |
| Combo Adaptive Tp3 V1 | UNI | LONG | Combo Adaptive | 60m | 2,0x | 7,16543 | 7,00700 | 6,92567 | 3,61854 | 7,88472 | €16,69 | €33,37 | €1,12 | €-0,74 |
| Btc Ema 4H | BTC | LONG | Trend following EMA | 240m | 2,0x | 80800,35684 | 79715,87000 | 78530,68128 | 40804,18020 | 86474,54655 | €887,05 | €1.774,10 | €49,83 | €-23,81 |
| Btc Donchian 4H | BTC | LONG | Donchian breakout 20 barre | 240m | 2,0x | 80800,35684 | 79715,87000 | 78530,68128 | 40804,18020 | 87155,44873 | €882,31 | €1.764,61 | €49,57 | €-23,68 |
| Btc Bollinger 4H | BTC | SHORT | Bollinger mean reversion | 240m | 2,0x | 80768,04316 | 79715,87000 | 82830,55933 | 120748,22452 | 77055,51340 | €985,68 | €1.971,36 | €50,34 | €25,68 |
| Btc Adaptive 4H | BTC | LONG | Combo Adaptive | 240m | 2,0x | 80800,35684 | 79715,87000 | 78324,34707 | 40804,18020 | 86990,38168 | €817,27 | €1.634,54 | €50,09 | €-21,94 |
| Sol Ema 1H | SOL | LONG | Trend following EMA | 60m | 3,0x | 105,84416 | 105,25300 | 104,32001 | 71,09200 | 108,89248 | €1.165,90 | €3.497,71 | €50,37 | €-19,54 |
| Sol Ema 4H | SOL | LONG | Trend following EMA | 240m | 2,0x | 106,43228 | 105,25300 | 102,42020 | 53,74830 | 116,46248 | €667,02 | €1.334,05 | €50,29 | €-14,78 |
| Sol Donchian 4H | SOL | LONG | Donchian breakout 20 barre | 240m | 2,0x | 104,23184 | 105,25300 | 99,63427 | 52,63708 | 117,10505 | €574,98 | €1.149,96 | €50,72 | €11,27 |
| Sol Adaptive 1H | SOL | LONG | Combo Adaptive | 60m | 3,0x | 105,84416 | 105,25300 | 104,32001 | 71,09200 | 108,89248 | €1.158,48 | €3.475,45 | €50,05 | €-19,41 |
| Sol Adaptive 4H | SOL | LONG | Combo Adaptive | 240m | 2,0x | 105,36907 | 105,25300 | 100,99415 | 53,21138 | 116,30636 | €613,63 | €1.227,27 | €50,96 | €-1,35 |
| Eth Ema 1H | ETH | LONG | Trend following EMA | 60m | 3,0x | 2503,97069 | 2501,94000 | 2467,91352 | 1681,83365 | 2576,08505 | €1.125,12 | €3.375,35 | €48,61 | €-2,74 |
| Eth Ema 4H | ETH | LONG | Trend following EMA | 240m | 2,0x | 2499,33977 | 2501,94000 | 2409,82951 | 1262,16658 | 2723,11538 | €690,19 | €1.380,39 | €49,44 | €1,44 |
| Master Adaptive V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99403 | 639,55695 | 1331,36019 | €22,75 | €45,50 | €1,17 | €0,00 |
| Master Adaptive V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €195,57 | €391,15 | €46,94 | €0,00 |
| Master Adaptive V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,20498 | 0,11491 | 0,27267 | €236,54 | €473,08 | €46,91 | €0,00 |
| Master Adaptive V1 | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,13517 | 0,17410 | 0,12719 | 0,06826 | 0,15112 | €410,30 | €820,61 | €48,44 | €236,36 |
| Master Adaptive V1 | MARSCOIN | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,24056 | 0,24056 | 0,21169 | 0,12148 | 0,29829 | €22,47 | €44,95 | €5,39 | €0,00 |
| Master Adaptive V1 | ZEC | LONG | Master Adaptive Consensus | 60m | 2,0x | 1171,00415 | 1208,44000 | 1123,88657 | 591,35710 | 1265,23933 | €609,04 | €1.218,08 | €49,01 | €38,94 |
| Master Adaptive V1 | NEAR | LONG | Master Adaptive Consensus | 60m | 2,0x | 2,40748 | 2,42700 | 2,29716 | 1,21578 | 2,62812 | €16,19 | €32,38 | €1,48 | €0,26 |
| Master Adaptive No Alt V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1255,10261 | 1255,10261 | 1225,12158 | 633,82682 | 1315,06467 | €19,09 | €38,19 | €0,91 | €0,00 |
| Master Adaptive No Alt V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €183,81 | €367,62 | €44,11 | €0,00 |
| Master Adaptive No Alt V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 530,08600 | 530,08600 | 509,10047 | 267,69343 | 572,05705 | €589,91 | €1.179,82 | €46,71 | €0,00 |
| Master Adaptive No Alt V1 | DASH | LONG | Master Adaptive Consensus | 60m | 2,0x | 68,92378 | 70,79000 | 64,01551 | 34,80651 | 78,74032 | €315,67 | €631,34 | €44,96 | €17,09 |
| Master Adaptive No Alt V1 | ZEC | LONG | Master Adaptive Consensus | 60m | 2,0x | 1186,35722 | 1208,44000 | 1129,86589 | 599,11040 | 1299,33988 | €489,56 | €979,12 | €46,62 | €18,23 |
| Master Adaptive No Alt V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 2501,94029 | 2501,94000 | 2465,91235 | 1263,47985 | 2573,99617 | €109,70 | €219,41 | €3,16 | €-0,00 |
| Master Adaptive Strict3 V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €178,16 | €356,31 | €42,76 | €0,00 |
| Master Adaptive Strict3 V1 | PROM | LONG | Master Adaptive Consensus | 60m | 2,0x | 7,01991 | 7,01991 | 6,30832 | 3,54505 | 8,44309 | €215,49 | €430,99 | €43,69 | €0,00 |
| Master Adaptive Strict3 V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,24076 | 0,24076 | 0,21579 | 0,12159 | 0,29071 | €209,83 | €419,66 | €43,53 | €0,00 |
| Master Adaptive Strict3 V1 | DASH | LONG | Master Adaptive Consensus | 60m | 2,0x | 68,92378 | 70,79000 | 64,01551 | 34,80651 | 78,74032 | €31,26 | €62,52 | €4,45 | €1,69 |
| Master Adaptive Strict3 V1 | ZEC | LONG | Master Adaptive Consensus | 60m | 2,0x | 1186,35722 | 1208,44000 | 1129,86589 | 599,11040 | 1299,33988 | €472,80 | €945,61 | €45,03 | €17,60 |
| Master Adaptive Strict3 V1 | TAO | LONG | Master Adaptive Consensus | 60m | 2,0x | 273,49469 | 273,44000 | 262,68503 | 138,11482 | 295,11400 | €12,91 | €25,82 | €1,02 | €-0,01 |
| Master Adaptive Expanded V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03814 | 0,02188 | 0,05374 | €197,50 | €395,01 | €47,40 | €0,00 |
| Master Adaptive Expanded V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1261,89668 | 1261,89668 | 1231,08309 | 637,25783 | 1323,52387 | €934,21 | €1.868,43 | €45,62 | €0,00 |
| Master Adaptive Expanded V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01194 | 0,01194 | 0,01050 | 0,00603 | 0,01480 | €195,34 | €390,67 | €46,88 | €0,00 |
| Master Adaptive Expanded V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,20498 | 0,11491 | 0,27267 | €236,25 | €472,49 | €46,85 | €0,00 |
| Master Adaptive Gb20 V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99403 | 639,55695 | 1331,36019 | €22,45 | €44,90 | €1,15 | €0,00 |
| Master Adaptive Gb20 V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €193,03 | €386,06 | €46,33 | €0,00 |
| Master Adaptive Gb20 V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,20498 | 0,11491 | 0,27267 | €233,42 | €466,83 | €46,29 | €0,00 |
| Master Adaptive Gb20 V1 | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,13517 | 0,17410 | 0,12719 | 0,06826 | 0,15112 | €404,89 | €809,78 | €47,80 | €233,24 |
| Master Adaptive Gb20 V1 | MARSCOIN | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,24056 | 0,24056 | 0,21169 | 0,12148 | 0,29829 | €22,18 | €44,35 | €5,32 | €0,00 |
| Master Adaptive Gb20 V1 | ZEC | LONG | Master Adaptive Consensus | 60m | 2,0x | 1171,00415 | 1208,44000 | 1123,88657 | 591,35710 | 1265,23933 | €601,00 | €1.202,00 | €48,36 | €38,43 |
| Master Adaptive Gb20 V1 | NEAR | LONG | Master Adaptive Consensus | 60m | 2,0x | 2,40748 | 2,42700 | 2,29716 | 1,21578 | 2,62812 | €15,88 | €31,75 | €1,45 | €0,26 |
| Master Adaptive Runner25 V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03814 | 0,02188 | 0,05894 | €34,77 | €69,54 | €8,34 | €0,00 |
| Master Adaptive Runner25 V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1255,10261 | 1255,10261 | 1225,12158 | 633,82682 | 1345,04570 | €27,05 | €54,10 | €1,29 | €0,00 |
| Master Adaptive Runner25 V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01601 | €185,86 | €371,72 | €44,61 | €0,00 |
| Master Adaptive Runner25 V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,20498 | 0,11491 | 0,29523 | €233,84 | €467,69 | €46,37 | €0,00 |
| Master Adaptive Runner25 V1 | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,13517 | 0,17410 | 0,12719 | 0,06826 | 0,15910 | €399,89 | €799,78 | €47,21 | €230,37 |
| Master Adaptive Runner25 V1 | NEAR | LONG | Master Adaptive Consensus | 60m | 2,0x | 2,22144 | 2,42700 | 2,12346 | 1,12183 | 2,51541 | €477,69 | €955,38 | €42,14 | €88,40 |
| Master Adaptive Runner25 V1 | ZEC | LONG | Master Adaptive Consensus | 60m | 2,0x | 1142,68849 | 1208,44000 | 1099,52971 | 577,05769 | 1272,16483 | €18,41 | €36,81 | €1,39 | €2,12 |
| Master Adaptive Runner25 V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 86,72534 | 86,35400 | 85,46149 | 43,79630 | 90,51689 | €188,43 | €376,86 | €5,49 | €-1,61 |
| Master Adaptive Runner25 V1 | DASH | LONG | Master Adaptive Consensus | 60m | 2,0x | 69,97399 | 70,79000 | 65,60770 | 35,33687 | 83,07286 | €18,41 | €36,82 | €2,30 | €0,43 |
| Combo Adaptive Side Regime Guard V1 | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 2,08142 | 2,42700 | 2,00650 | 1,05112 | 2,23125 | €77,52 | €155,04 | €5,58 | €25,74 |
| Combo Adaptive Side Regime Guard V1 | VELVET | SHORT | Combo Adaptive | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €216,61 | €433,23 | €0,00 | €-0,00 |
| Combo Adaptive Side Regime Guard V1 | TUT | SHORT | Combo Adaptive | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €192,40 | €384,79 | €46,18 | €-0,00 |
| Combo Adaptive Side Regime Guard V1 | BTR | SHORT | Combo Adaptive | 60m | 2,0x | 0,05109 | 0,05109 | 0,05109 | 0,07638 | 0,03883 | €195,57 | €391,13 | €0,00 | €-0,00 |
| Combo Adaptive Side Regime Guard V1 | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,13283 | 0,17410 | 0,12480 | 0,06708 | 0,14889 | €385,18 | €770,35 | €46,58 | €239,37 |
| Combo Adaptive Side Regime Guard V1 | SOL | LONG | Combo Adaptive | 60m | 2,0x | 105,92618 | 105,25300 | 104,40084 | 53,49272 | 108,97686 | €23,43 | €46,87 | €0,67 | €-0,30 |
| Combo Adaptive Side Regime Guard V1 | UNI | LONG | Combo Adaptive | 60m | 2,0x | 7,16543 | 7,00700 | 6,92567 | 3,61854 | 7,64496 | €12,54 | €25,08 | €0,84 | €-0,55 |
| Combo Adaptive Side Regime Guard V1 | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 1186,35722 | 1208,44000 | 1129,86589 | 599,11040 | 1299,33988 | €14,29 | €28,58 | €1,36 | €0,53 |
| Combo Adaptive Side Regime Guard V1 | TAO | LONG | Combo Adaptive | 60m | 2,0x | 273,49469 | 273,44000 | 262,68503 | 138,11482 | 295,11399 | €40,44 | €80,89 | €3,20 | €-0,02 |
| Master Adaptive Gb20 Be V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99403 | 639,55695 | 1331,36019 | €22,86 | €45,73 | €1,17 | €0,00 |
| Master Adaptive Gb20 Be V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €196,54 | €393,08 | €47,17 | €0,00 |
| Master Adaptive Gb20 Be V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,20498 | 0,11491 | 0,27267 | €237,71 | €475,42 | €47,14 | €0,00 |
| Master Adaptive Gb20 Be V1 | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,13517 | 0,17410 | 0,12719 | 0,06826 | 0,15112 | €412,34 | €824,67 | €48,68 | €237,53 |
| Master Adaptive Gb20 Be V1 | MARSCOIN | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,24056 | 0,24056 | 0,21169 | 0,12148 | 0,29829 | €22,58 | €45,17 | €5,42 | €0,00 |
| Master Adaptive Gb20 Be V1 | ZEC | LONG | Master Adaptive Consensus | 60m | 2,0x | 1171,00415 | 1208,44000 | 1123,88657 | 591,35710 | 1265,23933 | €612,05 | €1.224,11 | €49,25 | €39,13 |
| Master Adaptive Gb20 Be V1 | NEAR | LONG | Master Adaptive Consensus | 60m | 2,0x | 2,40748 | 2,42700 | 2,29716 | 1,21578 | 2,62812 | €16,27 | €32,54 | €1,49 | €0,26 |
| Master Adaptive Gb20 Partial V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99403 | 639,55695 | 1331,36019 | €22,84 | €45,68 | €1,17 | €0,00 |
| Master Adaptive Gb20 Partial V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €196,33 | €392,67 | €47,12 | €0,00 |
| Master Adaptive Gb20 Partial V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,20498 | 0,11491 | 0,27267 | €237,46 | €474,91 | €47,09 | €0,00 |
| Master Adaptive Gb20 Partial V1 | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,13517 | 0,17410 | 0,12719 | 0,06826 | 0,15112 | €411,90 | €823,79 | €48,63 | €237,28 |
| Master Adaptive Gb20 Partial V1 | MARSCOIN | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,24056 | 0,24056 | 0,21169 | 0,12148 | 0,29829 | €22,56 | €45,12 | €5,41 | €0,00 |
| Master Adaptive Gb20 Partial V1 | ZEC | LONG | Master Adaptive Consensus | 60m | 2,0x | 1171,00415 | 1208,44000 | 1123,88657 | 591,35710 | 1265,23933 | €611,40 | €1.222,81 | €49,20 | €39,09 |
| Master Adaptive Gb20 Partial V1 | NEAR | LONG | Master Adaptive Consensus | 60m | 2,0x | 2,40748 | 2,42700 | 2,29716 | 1,21578 | 2,62812 | €16,25 | €32,50 | €1,49 | €0,26 |
| Master Adaptive Gb20 Loss Cap V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03828 | 0,02188 | 0,05682 | €195,70 | €391,41 | €45,67 | €0,00 |
| Master Adaptive Gb20 Loss Cap V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01069 | 0,00594 | 0,01465 | €210,34 | €420,68 | €38,67 | €0,00 |
| Master Adaptive Gb20 Loss Cap V1 | PROM | LONG | Master Adaptive Consensus | 60m | 2,0x | 7,01991 | 7,01991 | 6,48622 | 3,54505 | 8,44309 | €34,75 | €69,51 | €5,28 | €0,00 |
| Master Adaptive Gb20 Loss Cap V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,21062 | 0,11491 | 0,27267 | €309,65 | €619,30 | €46,05 | €0,00 |
| Master Adaptive Gb20 Loss Cap V1 | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,13517 | 0,17410 | 0,12918 | 0,06826 | 0,15112 | €19,32 | €38,65 | €1,71 | €11,13 |
| Master Adaptive Gb20 Loss Cap V1 | NEAR | LONG | Master Adaptive Consensus | 60m | 2,0x | 2,37648 | 2,42700 | 2,29443 | 1,20012 | 2,59527 | €691,76 | €1.383,52 | €47,77 | €29,41 |
| Master Adaptive Gb20 Loss Cap V1 | ZEC | LONG | Master Adaptive Consensus | 60m | 2,0x | 1168,87373 | 1208,44000 | 1128,11099 | 590,28123 | 1277,57438 | €86,94 | €173,88 | €6,06 | €5,89 |
| 1H Fast V3 Nohigh Range Only V1 | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,20283 | 0,20283 | 0,20750 | 0,26943 | 0,19582 | €740,69 | €2.222,07 | €51,20 | €-0,00 |
| 1H Fast V3 Nohigh Range Only V1 | BTR | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €135,43 | €406,30 | €0,00 | €-0,00 |
| 1H Fast V3 Nohigh Range Only V1 | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1186,35722 | 1208,44000 | 1142,41952 | 796,83660 | 1252,26377 | €460,83 | €1.382,48 | €51,20 | €25,73 |
| 1H Fast V3 Nohigh Range Only V1 | DASH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 69,61392 | 70,79000 | 66,26910 | 46,75735 | 74,63116 | €16,79 | €50,37 | €2,42 | €0,85 |
| 1H Fast V3 Nohigh Range Only V1 | NEAR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,38548 | 2,42700 | 2,30355 | 1,60225 | 2,50836 | €487,86 | €1.463,59 | €50,26 | €25,48 |
| 1H Fast V3 Nohigh Range Only V1 | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 273,49469 | 273,44000 | 265,08718 | 183,69727 | 286,10595 | €10,13 | €30,38 | €0,93 | €-0,01 |
| 1H Fast V3 Nohigh Regime Guard V1 | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €140,84 | €422,53 | €50,70 | €-0,00 |
| 1H Fast V3 Nohigh Regime Guard V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €143,15 | €429,46 | €50,70 | €-0,00 |
| 1H Fast V3 Nohigh Regime Guard V1 | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,20283 | 0,20283 | 0,20750 | 0,26943 | 0,19582 | €34,57 | €103,71 | €2,39 | €-0,00 |
| 1H Fast V3 Nohigh Regime Guard V1 | BTR | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,05154 | 0,05154 | 0,05154 | 0,06846 | 0,04226 | €139,06 | €417,17 | €0,00 | €-0,00 |
| 1H Fast V3 Nohigh Regime Guard V1 | BTC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 80028,10242 | 79715,87000 | 79131,78767 | 53752,20879 | 81372,57454 | €20,36 | €61,08 | €0,68 | €-0,24 |
| 1H Fast V3 Nohigh Regime Guard V1 | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1186,35722 | 1208,44000 | 1142,41952 | 796,83660 | 1252,26377 | €38,56 | €115,68 | €4,28 | €2,15 |
| 1H Fast V3 Nohigh Regime Guard V1 | NEAR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,38548 | 2,42700 | 2,30355 | 1,60225 | 2,50836 | €502,64 | €1.507,91 | €51,79 | €26,25 |
| Main Side Regime Guard V1 | VELVET | LONG | Confluenza trend | 240m | 3,0x | 0,55987 | 0,55987 | 0,49269 | 0,37605 | 0,69424 | €142,25 | €426,74 | €51,21 | €0,00 |
| Main Side Regime Guard V1 | AKE | LONG | Confluenza trend | 240m | 3,0x | 0,01021 | 0,01021 | 0,00899 | 0,00686 | 0,01266 | €145,97 | €437,90 | €52,55 | €0,00 |
| Main Side Regime Guard V1 | ENA | LONG | Confluenza trend | 240m | 3,0x | 0,16108 | 0,16108 | 0,14175 | 0,10819 | 0,19974 | €150,44 | €451,33 | €54,16 | €0,00 |
| Main Side Regime Guard V1 | BTR | SHORT | Confluenza trend | 240m | 3,0x | 0,04853 | 0,04853 | 0,05435 | 0,06446 | 0,03688 | €12,76 | €38,29 | €4,59 | €-0,00 |
| Main Side Regime Guard V1 | DASH | LONG | Confluenza trend | 240m | 3,0x | 69,69394 | 70,79000 | 61,33066 | 46,81109 | 86,42048 | €155,22 | €465,66 | €55,88 | €7,32 |
| Main Side Regime Guard V1 | NEAR | LONG | Confluenza trend | 240m | 3,0x | 2,38548 | 2,42700 | 2,20016 | 1,60225 | 2,75612 | €21,97 | €65,90 | €5,12 | €1,15 |
| Main Dynamic Asset Selector V1 | ENA | LONG | Confluenza trend | 240m | 3,0x | 0,16108 | 0,16108 | 0,14175 | 0,10819 | 0,19974 | €140,98 | €422,93 | €50,75 | €0,00 |
| Main Dynamic Asset Selector V1 | ZEC | LONG | Confluenza trend | 240m | 3,0x | 1190,40803 | 1208,44000 | 1090,98250 | 799,55740 | 1389,25911 | €203,57 | €610,70 | €51,01 | €9,25 |
| Combo Trend Side Regime Guard V1 | VELVET | SHORT | Combo Trend | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,12693 | €217,86 | €435,73 | €0,00 | €-0,00 |
| Combo Trend Side Regime Guard V1 | TUT | SHORT | Combo Trend | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03364 | €12,81 | €25,62 | €3,07 | €-0,00 |
| Combo Trend Side Regime Guard V1 | BTR | SHORT | Combo Trend | 60m | 2,0x | 0,04853 | 0,04853 | 0,05435 | 0,07255 | 0,03572 | €222,18 | €444,37 | €53,32 | €-0,00 |
| Combo Trend Side Regime Guard V1 | ARB | LONG | Combo Trend | 60m | 2,0x | 0,13283 | 0,17410 | 0,12390 | 0,06708 | 0,15246 | €399,57 | €799,13 | €53,69 | €248,32 |
| Combo Trend Side Regime Guard V1 | XRP | LONG | Combo Trend | 60m | 2,0x | 1,41420 | 1,40809 | 1,39158 | 0,71417 | 1,46398 | €20,70 | €41,41 | €0,66 | €-0,18 |
| Combo Trend Side Regime Guard V1 | UNI | LONG | Combo Trend | 60m | 2,0x | 7,09542 | 7,00700 | 6,74949 | 3,58319 | 7,85647 | €523,05 | €1.046,10 | €51,00 | €-13,04 |
| Combo Trend Side Regime Guard V1 | SOL | LONG | Combo Trend | 60m | 2,0x | 105,69714 | 105,25300 | 103,96427 | 53,37705 | 109,50944 | €16,60 | €33,19 | €0,54 | €-0,14 |
| Combo Trend Side Regime Guard V1 | NEAR | LONG | Combo Trend | 60m | 2,0x | 2,41248 | 2,42700 | 2,29213 | 1,21830 | 2,67725 | €84,20 | €168,39 | €8,40 | €1,01 |
| 1H Fast Nohigh Cap75 Short Only V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €135,82 | €407,46 | €48,90 | €-0,00 |
| 1H Fast Nohigh Cap75 Short Only V1 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €138,05 | €414,14 | €48,89 | €-0,00 |
| 1H Fast Nohigh Cap75 Short Only V1 | BTR | SHORT | Momentum / breakout | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €132,24 | €396,72 | €0,00 | €-0,00 |
| 1H Fast Nohigh Cap75 Short Only V1 | PEPE | SHORT | Momentum / breakout | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €573,54 | €1.720,62 | €44,16 | €-0,00 |
| 1H Balanced V3 Long Only V1 | SKHYNIX | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1220,85412 | 1220,85412 | 1177,63561 | 820,00702 | 1307,29117 | €435,49 | €1.306,46 | €46,25 | €0,00 |
| 1H Balanced V3 Long Only V1 | ADA | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,20138 | 0,20138 | 0,20719 | 0,26750 | 0,18976 | €529,53 | €1.588,58 | €45,82 | €-0,00 |
| 1H Balanced V3 Long Only V1 | ARB | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,13283 | 0,17410 | 0,12480 | 0,08922 | 0,14889 | €248,38 | €745,13 | €45,06 | €231,54 |
| 1H Balanced V3 Long Only V1 | UNI | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 7,14143 | 7,00700 | 6,87560 | 4,79666 | 7,67309 | €9,06 | €27,18 | €1,01 | €-0,51 |
| 1H Balanced V3 Long Only V1 | ETH | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 2511,57221 | 2501,94000 | 2475,40557 | 1686,93934 | 2583,90549 | €1.065,89 | €3.197,67 | €46,05 | €-12,26 |
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
| 1H Fast V3 No Esports Stress Guard V1 | UNI | LONG | 2026-09-07T04:15:00+00:00 | 6,93328 | €-57,04 | -1,05 | STOP |
| 1H Fast V3 No Esports Long Only V1 | UNI | LONG | 2026-09-07T04:15:00+00:00 | 6,97756 | €-0,75 | -1,05 | STOP |
| 1H Fast V3 Long Only V1 | UNI | LONG | 2026-09-07T04:15:00+00:00 | 6,97756 | €-0,71 | -1,05 | STOP |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | UNI | LONG | 2026-09-07T04:15:00+00:00 | 6,93328 | €-5,39 | -1,05 | STOP |
| 1H Fast V3 Cap75 V1 | UNI | LONG | 2026-09-07T04:15:00+00:00 | 6,93328 | €-1,05 | -1,05 | STOP |
| 1H Fast Score 6 75 V1 | UNI | LONG | 2026-09-07T04:15:00+00:00 | 6,93328 | €-51,01 | -1,05 | STOP |
| 1H Fast Score 6 75 No Trend Up V1 | UNI | LONG | 2026-09-07T04:15:00+00:00 | 6,93328 | €-50,86 | -1,05 | STOP |
| Scanner Top5 Btc Guard Btc Le3 V1 | ARB | LONG | 2026-09-07T03:45:00+00:00 | 0,17683 | €-46,90 | -1,02 | STOP |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | ARB | LONG | 2026-09-07T03:45:00+00:00 | 0,17833 | €-46,50 | -1,02 | STOP |
| Scanner Top5 Btc Btc Le3 V1 | ARB | LONG | 2026-09-07T03:45:00+00:00 | 0,17683 | €-43,81 | -1,02 | STOP |
| Scanner Top5 Btc Btc 2 3 V1 | ARB | LONG | 2026-09-07T03:45:00+00:00 | 0,17833 | €-46,80 | -1,02 | STOP |
| 1H Fast V3 Nohigh V1 | ARB | LONG | 2026-09-07T03:45:00+00:00 | 0,17944 | €-5,75 | -1,03 | STOP |

## Regole invarianti

- Nessuna martingala e nessuna mediazione automatica in perdita.
- Il target mensile riduce il rischio quando viene avvicinato o raggiunto; non lo aumenta mai.
- Il portafoglio principale e le simulazioni di confronto hanno contabilità separata.
- Commissioni, slippage e funding sono inclusi nella simulazione secondo i parametri configurati.
- Quando stop e target risultano toccati nella stessa candela, prevale lo stop salvo modifica esplicita della configurazione.
