# Paper trading automatico KuCoin

Generato: 2026-07-27T05:15:04+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-07-27T05:08:24+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-07-27T05:08:24+00:00 | 2026-07-27T05:08:25+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-07-27T04:45:00+00:00 | 2026-07-27T04:45:00+00:00 | 8,5 min | 25,0 min | OK |
| 60m | 12 | 2026-07-27T04:00:00+00:00 | 2026-07-27T04:00:00+00:00 | 8,5 min | 45,0 min | OK |
| 240m | 12 | 2026-07-27T00:00:00+00:00 | 2026-07-27T00:00:00+00:00 | 1,14 h | 1,00 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | HYPE | 60m | LONG | 6,69 | 4,50 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Master Adaptive Gb20 Partial V1 | ETH | 60m | LONG | 5,35 | 0,00 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive Regime V1 | HYPE | 60m | LONG | 6,69 | 5,00 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Benchmark Bollinger mean reversion 1H | HYPE | 60m | LONG | 6,69 | 5,00 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Bilanciata 1H V1 | HYPE | 60m | LONG | 6,69 | 5,00 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Principale 4H | PEPE | 240m | LONG | 6,53 | 6,00 | 0,00 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | BANK | 240m | LONG | 6,25 | 6,00 | 0,00 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | ETH | 240m | LONG | 6,24 | 6,00 | 0,00 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | EUL | 240m | LONG | 5,75 | 6,00 | 0,25 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | SHIB | 240m | LONG | 5,75 | 6,00 | 0,25 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | BTC | 240m | LONG | 2,00 | 6,00 | 4,00 | STALE_CANDLE | 1,14 h | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | SOL | 240m | LONG | 1,70 | 6,00 | 4,30 | STALE_CANDLE | 1,14 h | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | HYPE | 240m | LONG | 1,69 | 6,00 | 4,31 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | ZEC | 240m | LONG | 1,34 | 6,00 | 4,66 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | DOGE | 240m | SHORT | -1,25 | 6,00 | 4,75 | STALE_CANDLE | 1,14 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | ESPORTS | 240m | LONG | 1,25 | 6,00 | 4,75 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | XRP | 240m | LONG | 1,24 | 6,00 | 4,76 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Forza relativa 1H V1 | BANK | 60m | LONG | 7,50 | 4,00 | 0,00 | READY | 8,5 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Scanner Top 5 Long 1H | BANK | 60m | LONG | 7,50 | 5,00 | 0,00 | READY | 8,5 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Scanner Top 5 + forza BTC 1H | BANK | 60m | LONG | 7,50 | 5,00 | 0,00 | READY | 8,5 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Scanner Top5 Btc Mfe V1 | BANK | 60m | LONG | 7,50 | 5,00 | 0,00 | READY | 8,5 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Scanner Top5 Btc Btc Le3 V1 | BANK | 60m | LONG | 7,50 | 5,00 | 0,00 | READY | 8,5 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Scanner Top5 Btc Btc 2 3 V1 | BANK | 60m | LONG | 7,50 | 5,00 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top5 Btc Guard Mfe V1 | BANK | 60m | LONG | 7,50 | 5,00 | 0,00 | READY | 8,5 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | BANK | 60m | LONG | 7,50 | 5,00 | 0,00 | READY | 8,5 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.790,74 | -2,09% | €-209,26 | €3.000,00 | -6,98% | 5 | 21 | 28,57% | 0,68 | 4,52% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 21 | 742 | CAMPIONE INSUFFICIENTE | 30 (mancano 9) |

- Trade del Principale 4H chiusi: **21**; win rate **28,57%**; profit factor **0,68**.
- Expectancy: **€-11,50** per trade; P&L netto: **€-241,45**; max drawdown: **4,52%**.
- Valutazione: **Servono altri eventi indipendenti prima di trarre conclusioni.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 5 | €9.790,74 | €1.075,94 | €3.227,82 | €146,89 | €33,87 |
| TEST | Bilanciata 1H V3 Filtered | 7 | €10.611,62 | €706,14 | €2.118,41 | €212,00 | €31,72 |
| TEST | Benchmark Donchian breakout 1H | 5 | €10.544,87 | €3.557,51 | €7.115,02 | €157,48 | €77,88 |
| TEST | Scanner Top 5 Long 1H | 6 | €10.518,54 | €3.318,14 | €6.636,28 | €210,26 | €-0,41 |
| TEST | 1H Fast Nohigh Cap75 V1 | 5 | €10.447,88 | €1.645,11 | €4.935,33 | €208,71 | €-8,91 |
| TEST | 1H Fast V3 Cap75 V1 | 5 | €10.427,40 | €861,02 | €2.583,07 | €208,63 | €11,83 |
| TEST | 1H Fast Score 6 75 V1 | 6 | €10.365,95 | €2.070,61 | €6.211,82 | €206,97 | €36,58 |
| TEST | Bilanciata 1H V1 | 6 | €10.344,44 | €2.461,02 | €7.383,06 | €154,92 | €37,53 |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | 5 | €10.326,10 | €2.052,47 | €6.157,42 | €205,89 | €36,27 |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | 3 | €10.320,89 | €348,84 | €1.046,53 | €104,43 | €-0,97 |
| TEST | Scanner Top 5 + forza BTC 1H | 6 | €10.319,19 | €3.043,10 | €6.086,20 | €206,42 | €18,64 |
| TEST | 1H Fast Score 6 75 Range Only V1 | 4 | €10.292,88 | €961,67 | €2.885,01 | €205,93 | €-3,03 |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 5 | €10.256,44 | €3.027,93 | €9.083,78 | €205,09 | €-8,87 |
| TEST | 1H Fast V3 Nohigh Range Only V1 | 3 | €10.242,63 | €474,81 | €1.424,44 | €153,41 | €21,71 |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | 4 | €10.233,85 | €837,63 | €2.512,89 | €204,36 | €12,34 |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 6 | €10.223,27 | €2.874,96 | €8.624,87 | €153,34 | €16,70 |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 4 | €10.217,49 | €573,76 | €1.721,28 | €106,53 | €78,01 |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | 6 | €10.214,06 | €2.833,88 | €8.501,63 | €201,55 | €-7,88 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 7 | €10.213,14 | €754,54 | €2.263,61 | €153,76 | €64,17 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 6 | €10.208,92 | €2.854,25 | €8.562,74 | €203,56 | €26,66 |
| TEST | Combo Adaptive | 4 | €10.203,22 | €2.162,62 | €4.325,23 | €204,07 | €0,00 |
| TEST | Combo Adaptive Side Regime Guard V1 | 4 | €10.190,30 | €1.111,65 | €2.223,29 | €203,76 | €9,39 |
| TEST | Rapida 1H V3 Filtered | 5 | €10.185,66 | €2.718,68 | €8.156,04 | €203,52 | €27,44 |
| TEST | Btc Bollinger 1H | 0 | €10.168,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Main Dynamic Asset Selector V1 | 2 | €10.157,07 | €281,44 | €844,31 | €101,32 | €14,33 |
| TEST | Combo Trend Side Regime Guard V1 | 7 | €10.155,41 | €870,68 | €1.741,36 | €202,51 | €42,72 |
| TEST | 1H Fast V3 No Esports Long Only V1 | 6 | €10.144,83 | €2.812,05 | €8.436,15 | €202,74 | €13,84 |
| TEST | Combo Mean Reversion | 1 | €10.138,28 | €225,46 | €450,91 | €50,00 | €0,00 |
| TEST | 1H Fast No Pepe V1 | 5 | €10.127,29 | €2.703,16 | €8.109,49 | €202,36 | €27,27 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 5 | €10.125,83 | €2.972,21 | €8.916,64 | €202,48 | €-9,08 |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | 6 | €10.122,62 | €2.726,48 | €8.179,43 | €202,50 | €22,92 |
| TEST | Main Side Regime Guard V1 | 4 | €10.105,03 | €746,77 | €2.240,31 | €151,34 | €17,61 |
| TEST | Bilanciata 1H V2 | 4 | €10.098,02 | €1.501,59 | €4.504,76 | €152,55 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 5 | €10.096,45 | €1.713,96 | €5.141,89 | €201,85 | €-33,17 |
| TEST | Sol Donchian 1H | 0 | €10.092,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Ema 1H | 0 | €10.091,86 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 4H | 0 | €10.086,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 4H | 0 | €10.084,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Runner25 V1 | 5 | €10.073,28 | €2.266,98 | €4.533,96 | €201,30 | €0,00 |
| TEST | Combo Adaptive Quality7 V1 | 5 | €10.064,76 | €2.209,40 | €4.418,81 | €201,32 | €-1,00 |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | 5 | €10.052,72 | €3.596,92 | €10.790,75 | €200,34 | €27,22 |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 2 | €10.052,51 | €531,37 | €1.594,12 | €101,57 | €-3,05 |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 3 | €10.049,85 | €3.881,73 | €11.645,20 | €151,14 | €-20,94 |
| TEST | 1H Fast Tp2 V1 | 6 | €10.040,62 | €2.057,79 | €6.173,38 | €200,85 | €26,72 |
| TEST | Scanner Top5 Btc Runner25 V1 | 5 | €10.036,53 | €2.971,51 | €5.943,02 | €200,41 | €18,04 |
| TEST | 1H Balanced V3 Long Only V1 | 5 | €10.035,24 | €1.377,13 | €4.131,39 | €151,02 | €80,90 |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | 3 | €10.022,23 | €3.871,07 | €11.613,20 | €150,72 | €-20,88 |
| TEST | Eth Bollinger 1H | 1 | €10.018,63 | €1.391,03 | €4.173,10 | €50,08 | €5,69 |
| TEST | Btc Adaptive 1H | 0 | €10.013,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Tp3 V1 | 5 | €10.012,08 | €2.948,47 | €5.896,95 | €199,93 | €17,62 |
| TEST | Rapida 1H V2 | 3 | €10.011,11 | €4.383,00 | €13.149,00 | €150,74 | €-27,84 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €10.010,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 0 | €10.002,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €50 · 15x | 0 | €10.001,47 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €50 · 15x | 0 | €10.000,61 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €10 · 15x | 0 | €10.000,29 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €10 · 15x | 0 | €10.000,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Continuation V1 | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €10 · 15x | 0 | €9.999,70 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €10 · 15x | 0 | €9.998,96 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Donchian 1H | 0 | €9.998,75 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · prudente · 5x | 0 | €9.998,64 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €50 · 15x | 0 | €9.998,52 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €10 · 15x | 0 | €9.998,50 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | 5 | €9.996,82 | €1.006,19 | €3.018,56 | €199,90 | €-11,74 |
| TEST | 1H Balanced Short Trend Down Strict V1 | 0 | €9.995,87 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €50 · 15x | 0 | €9.994,81 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €50 · 15x | 0 | €9.992,50 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · prudente · 5x | 0 | €9.990,24 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · prudente · 5x | 0 | €9.988,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · prudente · 5x | 0 | €9.983,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 1H | 0 | €9.980,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 No Esports V1 | 5 | €9.978,23 | €2.662,83 | €7.988,50 | €199,38 | €26,90 |
| TEST | Sol Ema 1H | 0 | €9.977,09 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 0 | €9.976,99 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V1 | 2 | €9.974,17 | €1.645,02 | €4.935,06 | €99,89 | €0,00 |
| TEST | Forza relativa 1H V2 | 5 | €9.967,22 | €2.775,20 | €5.550,40 | €199,21 | €30,15 |
| TEST | Combo Adaptive Long Only V1 | 5 | €9.963,73 | €2.701,47 | €5.402,94 | €199,28 | €-0,35 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 5 | €9.961,06 | €2.902,70 | €8.708,09 | €199,19 | €-9,32 |
| TEST | Scanner Bottom5 Short Profit Lock V1 | 3 | €9.959,07 | €1.371,54 | €2.743,08 | €99,39 | €81,06 |
| TEST | 1H Fast V3 Nohigh V1 | 5 | €9.951,26 | €2.655,64 | €7.966,91 | €198,84 | €26,83 |
| TEST | Eth Ema 4H | 1 | €9.951,21 | €1.036,30 | €2.072,59 | €49,74 | €5,34 |
| TEST | Btc Ema 4H | 0 | €9.950,68 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 4H | 0 | €9.950,68 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 4H | 0 | €9.949,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | 6 | €9.944,60 | €2.770,05 | €8.310,14 | €198,75 | €14,49 |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | 3 | €9.944,51 | €1.372,84 | €2.745,68 | €149,15 | €20,97 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.944,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Benchmark trend following EMA 1H | 5 | €9.942,75 | €1.028,81 | €2.057,63 | €199,83 | €-20,72 |
| TEST | Sol Adaptive 4H | 1 | €9.940,47 | €761,04 | €1.522,08 | €49,74 | €-7,26 |
| TEST | Sol Donchian 4H | 1 | €9.939,60 | €830,21 | €1.660,43 | €49,74 | €-7,92 |
| TEST | Combo Adaptive Regime V1 | 6 | €9.932,38 | €2.311,72 | €4.623,45 | €198,65 | €10,10 |
| TEST | Combo Adaptive Tp3 V1 | 4 | €9.929,58 | €2.226,41 | €4.452,81 | €198,61 | €0,00 |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | 4 | €9.924,84 | €1.302,99 | €2.605,98 | €153,07 | €1,52 |
| TEST | Sol Ema 4H | 1 | €9.918,24 | €862,58 | €1.725,17 | €49,74 | €-29,17 |
| TEST | Eth Donchian 1H | 1 | €9.918,16 | €1.292,62 | €3.877,86 | €49,64 | €-6,84 |
| TEST | Ampia 4H | 4 | €9.916,19 | €1.734,53 | €3.469,06 | €199,10 | €-29,23 |
| TEST | Btc Ema 1H | 0 | €9.911,86 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Btc Le3 V1 | 5 | €9.910,66 | €2.934,05 | €5.868,09 | €197,90 | €17,77 |
| TEST | Sol Bollinger 1H | 0 | €9.901,25 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Scanner | 5 | €9.898,18 | €2.916,01 | €5.832,02 | €197,64 | €18,03 |
| TEST | Benchmark Bollinger mean reversion 1H | 2 | €9.897,58 | €3.966,50 | €7.933,00 | €95,20 | €20,65 |
| TEST | Doge Bollinger 1H | 0 | €9.888,87 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Balanced Long No Rhv V1 | 4 | €9.884,90 | €1.411,99 | €4.235,97 | €197,36 | €17,57 |
| TEST | Master Adaptive Gb20 Partial V1 | 5 | €9.875,12 | €2.110,88 | €4.221,76 | €197,50 | €20,25 |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | 3 | €9.873,91 | €2.159,53 | €4.319,06 | €148,43 | €10,15 |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | 4 | €9.865,20 | €2.341,17 | €4.682,34 | €197,31 | €-13,50 |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 6 | €9.862,51 | €1.402,41 | €4.207,24 | €149,41 | €32,54 |
| TEST | Scanner Top10 Long | 5 | €9.853,91 | €2.732,16 | €5.464,31 | €197,03 | €1,63 |
| TEST | Scanner Top15 Long | 5 | €9.853,91 | €2.732,16 | €5.464,31 | €197,03 | €1,63 |
| TEST | Scanner Top20 Long | 5 | €9.853,91 | €2.732,16 | €5.464,31 | €197,03 | €1,63 |
| TEST | Eth Adaptive 1H | 1 | €9.845,81 | €1.140,50 | €3.421,49 | €49,27 | €-6,03 |
| TEST | Master Adaptive Gb20 Be V1 | 4 | €9.843,89 | €2.172,56 | €4.345,11 | €196,72 | €8,16 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 5 | €9.842,45 | €2.676,86 | €8.030,58 | €196,70 | €14,77 |
| TEST | Sol Adaptive 1H | 0 | €9.835,19 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom10 Short | 3 | €9.831,79 | €2.159,38 | €4.318,77 | €98,62 | €80,02 |
| TEST | Scanner Bottom15 Short | 3 | €9.831,79 | €2.159,38 | €4.318,77 | €98,62 | €80,02 |
| TEST | Scanner Bottom20 Short | 3 | €9.831,79 | €2.159,38 | €4.318,77 | €98,62 | €80,02 |
| TEST | Combo Adaptive Quality7 Regime V1 | 3 | €9.813,47 | €2.151,60 | €4.303,20 | €147,83 | €10,09 |
| TEST | Master Adaptive Gb20 Loss Cap V1 | 4 | €9.808,51 | €2.761,06 | €5.522,12 | €195,96 | €10,92 |
| TEST | Global Confluence puro 1H | 0 | €9.790,66 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom 5 Short 1H | 3 | €9.785,30 | €1.786,26 | €3.572,51 | €48,61 | €79,71 |
| TEST | Eth Ema 1H | 1 | €9.773,73 | €1.132,15 | €3.396,44 | €48,91 | €-5,99 |
| TEST | Scanner Top5 Btc Guard V1 | 4 | €9.767,63 | €1.414,44 | €2.828,89 | €195,02 | €16,78 |
| TEST | 1H Fast V3 Long Only V1 | 4 | €9.744,48 | €1.654,74 | €4.964,21 | €195,84 | €-32,85 |
| TEST | Scanner Top5 Btc Mfe V1 | 5 | €9.718,85 | €4.066,51 | €8.133,03 | €194,40 | €13,25 |
| TEST | Combo Adaptive Partial 1R V1 | 6 | €9.684,94 | €2.560,56 | €5.121,12 | €193,65 | €3,19 |
| TEST | Master Adaptive Expanded V1 | 5 | €9.683,63 | €1.517,94 | €3.035,87 | €193,52 | €8,01 |
| TEST | Master Adaptive Gb20 V1 | 4 | €9.654,48 | €2.651,80 | €5.303,60 | €192,93 | €8,41 |
| TEST | Master Adaptive Runner25 V1 | 5 | €9.648,95 | €1.504,30 | €3.008,60 | €192,82 | €8,01 |
| TEST | Master Adaptive No Alt V1 | 5 | €9.643,92 | €1.504,28 | €3.008,56 | €192,72 | €7,99 |
| TEST | Master Adaptive V1 | 5 | €9.639,92 | €1.503,85 | €3.007,70 | €192,64 | €7,97 |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | 4 | €9.616,70 | €2.501,62 | €5.003,23 | €192,97 | €-24,46 |
| TEST | Forza relativa 1H V1 | 5 | €9.607,49 | €2.835,04 | €5.670,08 | €191,86 | €15,99 |
| TEST | Combo Trend | 4 | €9.534,13 | €1.541,40 | €3.082,80 | €191,83 | €-44,61 |
| TEST | Combo Adaptive Mfe Trail | 4 | €9.521,88 | €2.034,13 | €4.068,27 | €190,44 | €0,00 |
| TEST | Scanner Top5 Btc Guard Mfe V1 | 4 | €9.507,94 | €2.366,28 | €4.732,55 | €190,79 | €-24,08 |
| TEST | Master Adaptive Strict3 V1 | 4 | €9.489,03 | €3.928,81 | €7.857,63 | €189,48 | €16,83 |

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
| PRINCIPALE | Principale 4H | Confluenza trend | €9.790,74 | €-241,45 | 21 | 21 | 28,57% | 0,68 | €-11,50 | 4,52% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €10.611,62 | €581,26 | 46 | 46 | 43,48% | 1,62 | €12,64 | 2,20% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €10.544,87 | €472,58 | 26 | 26 | 53,85% | 1,89 | €18,18 | 2,12% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.518,54 | €522,77 | 37 | 37 | 51,35% | 1,61 | €14,13 | 3,57% |
| TEST | 1H Fast Nohigh Cap75 V1 | Momentum / breakout | €10.447,88 | €459,76 | 52 | 52 | 48,08% | 1,46 | €8,84 | 2,83% |
| TEST | 1H Fast V3 Cap75 V1 | Momentum / breakout V3 Filtered | €10.427,40 | €417,96 | 45 | 45 | 48,89% | 1,55 | €9,29 | 2,49% |
| TEST | 1H Fast Score 6 75 V1 | Momentum / breakout | €10.365,95 | €333,93 | 49 | 49 | 44,90% | 1,36 | €6,81 | 2,49% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €10.344,44 | €314,65 | 48 | 48 | 50,00% | 1,32 | €6,56 | 3,25% |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | Momentum / breakout | €10.326,10 | €293,74 | 13 | 13 | 61,54% | 2,33 | €22,60 | 1,96% |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | Momentum / breakout V3 Filtered | €10.320,89 | €322,54 | 16 | 16 | 68,75% | 2,99 | €20,16 | 1,39% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €10.319,19 | €303,94 | 29 | 29 | 48,28% | 1,43 | €10,48 | 3,23% |
| TEST | 1H Fast Score 6 75 Range Only V1 | Momentum / breakout | €10.292,88 | €297,12 | 9 | 9 | 66,67% | 3,17 | €33,01 | 2,28% |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | Momentum / breakout V3 Filtered | €10.256,44 | €270,39 | 13 | 13 | 61,54% | 3,37 | €20,80 | 1,97% |
| TEST | 1H Fast V3 Nohigh Range Only V1 | Momentum / breakout V3 Filtered | €10.242,63 | €221,94 | 9 | 9 | 66,67% | 2,37 | €24,66 | 1,78% |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | Momentum / breakout | €10.233,85 | €223,23 | 14 | 14 | 64,29% | 1,91 | €15,94 | 2,01% |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | Momentum / breakout V3 Filtered | €10.223,27 | €211,74 | 18 | 18 | 55,56% | 1,95 | €11,76 | 1,14% |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | Momentum / breakout V3 Filtered | €10.217,49 | €140,88 | 12 | 12 | 58,33% | 3,31 | €11,74 | 1,01% |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | Momentum / breakout V3 Filtered | €10.214,06 | €227,49 | 24 | 24 | 54,17% | 1,78 | €9,48 | 2,05% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | Momentum / breakout V3 Filtered | €10.213,14 | €151,15 | 11 | 11 | 54,55% | 2,93 | €13,74 | 2,01% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | Momentum / breakout V3 Filtered | €10.208,92 | €187,05 | 13 | 13 | 53,85% | 1,79 | €14,39 | 1,62% |
| TEST | Combo Adaptive | Combo Adaptive | €10.203,22 | €206,62 | 25 | 25 | 48,00% | 1,52 | €8,26 | 1,49% |
| TEST | Combo Adaptive Side Regime Guard V1 | Combo Adaptive | €10.190,30 | €182,53 | 11 | 11 | 81,82% | 2,69 | €16,59 | 1,41% |
| TEST | Rapida 1H V3 Filtered | Momentum / breakout V3 Filtered | €10.185,66 | €163,17 | 75 | 75 | 38,67% | 1,11 | €2,18 | 2,89% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.168,12 | €168,12 | 3 | 3 | 100,00% | ∞ | €56,04 | 0,54% |
| TEST | Main Dynamic Asset Selector V1 | Confluenza trend | €10.157,07 | €142,72 | 4 | 4 | 50,00% | 3,55 | €35,68 | 1,06% |
| TEST | Combo Trend Side Regime Guard V1 | Combo Trend | €10.155,41 | €113,96 | 11 | 11 | 54,55% | 1,68 | €10,36 | 1,32% |
| TEST | 1H Fast V3 No Esports Long Only V1 | Momentum / breakout V3 Filtered | €10.144,83 | €135,66 | 17 | 17 | 58,82% | 1,50 | €7,98 | 1,32% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €10.138,28 | €138,67 | 16 | 16 | 43,75% | 1,36 | €8,67 | 2,31% |
| TEST | 1H Fast No Pepe V1 | Momentum / breakout | €10.127,29 | €104,94 | 43 | 43 | 41,86% | 1,12 | €2,44 | 2,15% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | Momentum / breakout V3 Filtered | €10.125,83 | €139,85 | 13 | 13 | 46,15% | 1,75 | €10,76 | 2,27% |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | Momentum / breakout | €10.122,62 | €104,61 | 16 | 16 | 56,25% | 1,44 | €6,54 | 1,76% |
| TEST | Main Side Regime Guard V1 | Confluenza trend | €10.105,03 | €88,60 | 5 | 5 | 40,00% | 1,81 | €17,72 | 1,49% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €10.098,02 | €100,17 | 36 | 34 | 52,78% | 1,13 | €2,78 | 2,75% |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | Momentum / breakout V3 Filtered | €10.096,45 | €132,29 | 15 | 15 | 46,67% | 1,55 | €8,82 | 1,60% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €10.092,12 | €92,12 | 3 | 3 | 66,67% | 21,53 | €30,71 | 0,79% |
| TEST | Doge Ema 1H | Trend following EMA | €10.091,86 | €91,86 | 8 | 8 | 62,50% | 1,55 | €11,48 | 1,36% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €10.086,98 | €86,98 | 1 | 1 | 100,00% | ∞ | €86,98 | 0,40% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.084,12 | €84,12 | 1 | 1 | 100,00% | ∞ | €84,12 | 0,30% |
| TEST | Combo Adaptive Runner25 V1 | Combo Adaptive | €10.073,28 | €76,55 | 22 | 22 | 45,45% | 1,17 | €3,48 | 2,12% |
| TEST | Combo Adaptive Quality7 V1 | Combo Adaptive | €10.064,76 | €68,97 | 16 | 16 | 43,75% | 1,38 | €4,31 | 1,51% |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | Momentum / breakout | €10.052,72 | €31,98 | 18 | 18 | 38,89% | 1,09 | €1,78 | 2,07% |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | Momentum / breakout V3 Filtered | €10.052,51 | €56,63 | 6 | 6 | 50,00% | 1,56 | €9,44 | 2,15% |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | Momentum / breakout V3 Filtered | €10.049,85 | €77,77 | 8 | 8 | 50,00% | 1,47 | €9,72 | 2,06% |
| TEST | 1H Fast Tp2 V1 | Momentum / breakout | €10.040,62 | €17,67 | 47 | 47 | 36,17% | 1,02 | €0,38 | 2,58% |
| TEST | Scanner Top5 Btc Runner25 V1 | Scanner Top 5 + forza BTC | €10.036,53 | €21,80 | 16 | 16 | 50,00% | 1,05 | €1,36 | 3,25% |
| TEST | 1H Balanced V3 Long Only V1 | Confluenza trend V3 Filtered | €10.035,24 | €-43,30 | 7 | 7 | 28,57% | 0,74 | €-6,19 | 1,46% |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | Momentum / breakout V3 Filtered | €10.022,23 | €50,08 | 13 | 13 | 46,15% | 1,15 | €3,85 | 2,17% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €10.018,63 | €15,45 | 1 | 1 | 100,00% | ∞ | €15,45 | 0,51% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €10.013,28 | €13,28 | 3 | 3 | 66,67% | 1,24 | €4,43 | 0,89% |
| TEST | Scanner Top5 Btc Tp3 V1 | Scanner Top 5 + forza BTC | €10.012,08 | €-2,26 | 12 | 12 | 50,00% | 1,00 | €-0,19 | 3,22% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €10.011,11 | €46,84 | 14 | 13 | 50,00% | 1,15 | €3,35 | 1,69% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €10.010,98 | €10,98 | 9 | 9 | 33,33% | 1,23 | €1,22 | 0,25% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €10.002,20 | €2,20 | 9 | 9 | 33,33% | 1,23 | €0,24 | 0,05% |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | €10.001,47 | €1,47 | 5 | 5 | 40,00% | 1,12 | €0,29 | 0,13% |
| TEST | Scalp RSI Short 85 · €50 · 15x | Inversione RSI estrema 15m | €10.000,61 | €0,61 | 2 | 2 | 50,00% | 1,74 | €0,30 | 0,07% |
| TEST | Scalp RSI Long 25 · €10 · 15x | Inversione RSI estrema 15m | €10.000,29 | €0,29 | 5 | 5 | 40,00% | 1,12 | €0,06 | 0,03% |
| TEST | Scalp RSI Short 85 · €10 · 15x | Inversione RSI estrema 15m | €10.000,12 | €0,12 | 2 | 2 | 50,00% | 1,74 | €0,06 | 0,01% |
| TEST | Scanner Bottom5 Short Continuation V1 | Scanner Bottom5 Short Continuation | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 80 · €10 · 15x | Inversione RSI estrema 15m | €9.999,70 | €-0,30 | 3 | 3 | 66,67% | 0,63 | €-0,10 | 0,02% |
| TEST | Scalp RSI Long 20 · €10 · 15x | Inversione RSI estrema 15m | €9.998,96 | €-1,04 | 2 | 2 | 0,00% | 0,00 | €-0,52 | 0,02% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €9.998,75 | €-1,25 | 4 | 4 | 75,00% | 0,98 | €-0,31 | 0,96% |
| TEST | Scalp RSI Short 85 · prudente · 5x | Inversione RSI estrema 15m | €9.998,64 | €-1,36 | 2 | 2 | 50,00% | 0,42 | €-0,68 | 0,11% |
| TEST | Scalp RSI Short 80 · €50 · 15x | Inversione RSI estrema 15m | €9.998,52 | €-1,48 | 3 | 3 | 66,67% | 0,63 | €-0,49 | 0,09% |
| TEST | Scalp RSI Long 15 · €10 · 15x | Inversione RSI estrema 15m | €9.998,50 | €-1,50 | 1 | 1 | 0,00% | 0,00 | €-1,50 | 0,02% |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | Momentum / breakout V3 Filtered | €9.996,82 | €10,60 | 36 | 36 | 41,67% | 1,01 | €0,29 | 2,86% |
| TEST | 1H Balanced Short Trend Down Strict V1 | Confluenza trend | €9.995,87 | €-4,13 | 1 | 1 | 0,00% | 0,00 | €-4,13 | 0,59% |
| TEST | Scalp RSI Long 20 · €50 · 15x | Inversione RSI estrema 15m | €9.994,81 | €-5,19 | 2 | 2 | 0,00% | 0,00 | €-2,59 | 0,08% |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | €9.992,50 | €-7,50 | 1 | 1 | 0,00% | 0,00 | €-7,50 | 0,11% |
| TEST | Scalp RSI Short 80 · prudente · 5x | Inversione RSI estrema 15m | €9.990,24 | €-9,76 | 3 | 3 | 66,67% | 0,28 | €-3,25 | 0,21% |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | €9.988,38 | €-11,62 | 1 | 1 | 0,00% | 0,00 | €-11,62 | 0,17% |
| TEST | Scalp RSI Long 20 · prudente · 5x | Inversione RSI estrema 15m | €9.983,60 | €-16,40 | 2 | 2 | 0,00% | 0,00 | €-8,20 | 0,24% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €9.980,62 | €-19,38 | 4 | 4 | 50,00% | 0,82 | €-4,84 | 1,49% |
| TEST | 1H Fast V3 No Esports V1 | Momentum / breakout V3 Filtered | €9.978,23 | €-43,83 | 49 | 49 | 38,78% | 0,96 | €-0,89 | 2,49% |
| TEST | Sol Ema 1H | Trend following EMA | €9.977,09 | €-22,91 | 5 | 5 | 40,00% | 0,86 | €-4,58 | 1,67% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €9.976,99 | €-23,01 | 5 | 5 | 20,00% | 0,20 | €-4,60 | 0,37% |
| TEST | Rapida 1H V1 | Momentum / breakout | €9.974,17 | €-23,25 | 76 | 76 | 34,21% | 0,99 | €-0,31 | 6,76% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €9.967,22 | €-58,57 | 40 | 39 | 37,50% | 0,96 | €-1,46 | 5,10% |
| TEST | Combo Adaptive Long Only V1 | Combo Adaptive | €9.963,73 | €-32,81 | 10 | 10 | 40,00% | 0,86 | €-3,28 | 2,34% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | Momentum / breakout V3 Filtered | €9.961,06 | €-24,39 | 14 | 14 | 50,00% | 0,92 | €-1,74 | 2,38% |
| TEST | Scanner Bottom5 Short Profit Lock V1 | Scanner Bottom 5 Short | €9.959,07 | €-119,98 | 5 | 5 | 40,00% | 0,25 | €-24,00 | 1,53% |
| TEST | 1H Fast V3 Nohigh V1 | Momentum / breakout V3 Filtered | €9.951,26 | €-70,74 | 50 | 50 | 40,00% | 0,94 | €-1,41 | 2,96% |
| TEST | Eth Ema 4H | Trend following EMA | €9.951,21 | €-52,88 | 1 | 1 | 0,00% | 0,00 | €-52,88 | 0,80% |
| TEST | Btc Ema 4H | Trend following EMA | €9.950,68 | €-49,32 | 1 | 1 | 0,00% | 0,00 | €-49,32 | 0,96% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €9.950,68 | €-49,32 | 1 | 1 | 0,00% | 0,00 | €-49,32 | 0,96% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €9.949,62 | €-50,38 | 1 | 1 | 0,00% | 0,00 | €-50,38 | 0,74% |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | Momentum / breakout V3 Filtered | €9.944,60 | €-65,50 | 39 | 39 | 48,72% | 0,93 | €-1,68 | 3,21% |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | Scanner Bottom 5 Short | €9.944,51 | €-74,71 | 6 | 6 | 50,00% | 0,54 | €-12,45 | 1,38% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.944,12 | €-55,88 | 9 | 9 | 22,22% | 0,16 | €-6,21 | 0,56% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.942,75 | €-33,95 | 26 | 26 | 38,46% | 0,94 | €-1,31 | 2,25% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €9.940,47 | €-51,83 | 1 | 1 | 0,00% | 0,00 | €-51,83 | 0,73% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €9.939,60 | €-52,00 | 1 | 1 | 0,00% | 0,00 | €-52,00 | 0,75% |
| TEST | Combo Adaptive Regime V1 | Combo Adaptive | €9.932,38 | €-74,86 | 11 | 11 | 45,45% | 0,78 | €-6,81 | 2,18% |
| TEST | Combo Adaptive Tp3 V1 | Combo Adaptive | €9.929,58 | €-66,67 | 13 | 13 | 46,15% | 0,76 | €-5,13 | 1,41% |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | Scanner Top 5 + forza BTC | €9.924,84 | €-75,25 | 10 | 10 | 40,00% | 0,82 | €-7,52 | 3,23% |
| TEST | Sol Ema 4H | Trend following EMA | €9.918,24 | €-52,00 | 1 | 1 | 0,00% | 0,00 | €-52,00 | 0,97% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.918,16 | €-72,68 | 4 | 4 | 25,00% | 0,56 | €-18,17 | 1,38% |
| TEST | Ampia 4H | Confluenza trend | €9.916,19 | €-53,35 | 17 | 17 | 23,53% | 0,89 | €-3,14 | 3,68% |
| TEST | Btc Ema 1H | Trend following EMA | €9.911,86 | €-88,14 | 6 | 6 | 33,33% | 0,59 | €-14,69 | 1,56% |
| TEST | Scanner Top5 Btc Btc Le3 V1 | Scanner Top 5 + forza BTC | €9.910,66 | €-103,74 | 11 | 11 | 45,45% | 0,74 | €-9,43 | 3,23% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.901,25 | €-98,75 | 4 | 4 | 25,00% | 0,41 | €-24,69 | 1,89% |
| TEST | Combo Scanner | Combo Scanner | €9.898,18 | €-116,59 | 34 | 34 | 44,12% | 0,88 | €-3,43 | 3,25% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €9.897,58 | €-118,31 | 39 | 39 | 38,46% | 0,88 | €-3,03 | 4,19% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €9.888,87 | €-111,13 | 2 | 2 | 0,00% | 0,00 | €-55,56 | 1,26% |
| TEST | 1H Balanced Long No Rhv V1 | Confluenza trend | €9.884,90 | €-130,27 | 9 | 9 | 33,33% | 0,60 | €-14,47 | 2,47% |
| TEST | Master Adaptive Gb20 Partial V1 | Master Adaptive Consensus | €9.875,12 | €-142,71 | 6 | 6 | 33,33% | 0,49 | €-23,78 | 2,50% |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | Combo Adaptive | €9.873,91 | €-133,65 | 6 | 6 | 33,33% | 0,37 | €-22,27 | 1,95% |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | Scanner Top 5 + forza BTC | €9.865,20 | €-118,11 | 5 | 5 | 20,00% | 0,33 | €-23,62 | 2,84% |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | Momentum / breakout V3 Filtered | €9.862,51 | €-167,51 | 11 | 11 | 54,55% | 0,45 | €-15,23 | 3,08% |
| TEST | Scanner Top10 Long | Scanner Top10 Long | €9.853,91 | €-144,63 | 8 | 8 | 37,50% | 0,42 | €-18,08 | 3,62% |
| TEST | Scanner Top15 Long | Scanner Top15 Long | €9.853,91 | €-144,63 | 8 | 8 | 37,50% | 0,42 | €-18,08 | 3,62% |
| TEST | Scanner Top20 Long | Scanner Top20 Long | €9.853,91 | €-144,63 | 8 | 8 | 37,50% | 0,42 | €-18,08 | 3,62% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.845,81 | €-146,11 | 5 | 5 | 40,00% | 0,11 | €-29,22 | 1,84% |
| TEST | Master Adaptive Gb20 Be V1 | Master Adaptive Consensus | €9.843,89 | €-161,66 | 12 | 12 | 16,67% | 0,55 | €-13,47 | 3,15% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | Momentum / breakout V3 Filtered | €9.842,45 | €-167,51 | 11 | 11 | 54,55% | 0,45 | €-15,23 | 2,93% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €9.835,19 | €-164,81 | 6 | 6 | 33,33% | 0,29 | €-27,47 | 2,34% |
| TEST | Scanner Bottom10 Short | Scanner Bottom10 Short | €9.831,79 | €-245,28 | 6 | 6 | 16,67% | 0,11 | €-40,88 | 2,72% |
| TEST | Scanner Bottom15 Short | Scanner Bottom15 Short | €9.831,79 | €-245,28 | 6 | 6 | 16,67% | 0,11 | €-40,88 | 2,72% |
| TEST | Scanner Bottom20 Short | Scanner Bottom20 Short | €9.831,79 | €-245,28 | 6 | 6 | 16,67% | 0,11 | €-40,88 | 2,72% |
| TEST | Combo Adaptive Quality7 Regime V1 | Combo Adaptive | €9.813,47 | €-194,04 | 6 | 6 | 16,67% | 0,13 | €-32,34 | 2,32% |
| TEST | Master Adaptive Gb20 Loss Cap V1 | Master Adaptive Consensus | €9.808,51 | €-199,77 | 8 | 8 | 25,00% | 0,40 | €-24,97 | 3,63% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.790,66 | €-209,34 | 10 | 10 | 30,00% | 0,37 | €-20,93 | 2,92% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.785,30 | €-288,92 | 29 | 29 | 31,03% | 0,61 | €-9,96 | 5,48% |
| TEST | Eth Ema 1H | Trend following EMA | €9.773,73 | €-218,24 | 7 | 7 | 28,57% | 0,20 | €-31,18 | 2,52% |
| TEST | Scanner Top5 Btc Guard V1 | Scanner Top 5 + forza BTC | €9.767,63 | €-247,74 | 15 | 15 | 26,67% | 0,57 | €-16,52 | 3,36% |
| TEST | 1H Fast V3 Long Only V1 | Momentum / breakout V3 Filtered | €9.744,48 | €-220,06 | 40 | 40 | 35,00% | 0,78 | €-5,50 | 3,67% |
| TEST | Scanner Top5 Btc Mfe V1 | Scanner Top 5 + forza BTC | €9.718,85 | €-290,16 | 20 | 20 | 35,00% | 0,41 | €-14,51 | 3,95% |
| TEST | Combo Adaptive Partial 1R V1 | Combo Adaptive | €9.684,94 | €-314,39 | 18 | 18 | 33,33% | 0,47 | €-17,47 | 3,32% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €9.683,63 | €-322,63 | 13 | 13 | 30,77% | 0,47 | €-24,82 | 3,64% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €9.654,48 | €-350,75 | 47 | 47 | 57,45% | 0,59 | €-7,46 | 4,16% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €9.648,95 | €-357,32 | 12 | 12 | 25,00% | 0,36 | €-29,78 | 3,98% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €9.643,92 | €-362,33 | 10 | 10 | 20,00% | 0,35 | €-36,23 | 4,03% |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | €9.639,92 | €-366,31 | 10 | 10 | 20,00% | 0,35 | €-36,63 | 4,07% |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | Scanner Top 5 + forza BTC | €9.616,70 | €-356,34 | 25 | 25 | 40,00% | 0,53 | €-14,25 | 3,93% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €9.607,49 | €-405,41 | 28 | 28 | 25,00% | 0,53 | €-14,48 | 6,18% |
| TEST | Combo Trend | Combo Trend | €9.534,13 | €-419,10 | 38 | 38 | 31,58% | 0,71 | €-11,03 | 7,02% |
| TEST | Combo Adaptive Mfe Trail | Combo Adaptive | €9.521,88 | €-475,61 | 29 | 29 | 27,59% | 0,39 | €-16,40 | 5,33% |
| TEST | Scanner Top5 Btc Guard Mfe V1 | Scanner Top 5 + forza BTC | €9.507,94 | €-465,78 | 28 | 28 | 35,71% | 0,46 | €-16,63 | 5,08% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €9.489,03 | €-523,41 | 20 | 20 | 25,00% | 0,48 | €-26,17 | 5,48% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | LAB | SHORT | Confluenza trend | 240m | 3,0x | 0,17841 | 0,17841 | 0,17841 | 0,23699 | 0,13559 | €136,26 | €408,77 | €0,00 | €-0,00 |
| Principale 4H | SUI | LONG | Confluenza trend | 240m | 3,0x | 0,76296 | 0,76296 | 0,73998 | 0,51245 | 0,80891 | €547,52 | €1.642,56 | €49,46 | €0,00 |
| Principale 4H | ONDO | LONG | Confluenza trend | 240m | 3,0x | 0,40344 | 0,40344 | 0,37762 | 0,27098 | 0,45509 | €254,70 | €764,09 | €48,91 | €0,00 |
| Principale 4H | BANK | LONG | Confluenza trend | 240m | 3,0x | 0,36220 | 0,39497 | 0,31874 | 0,24328 | 0,44913 | €128,59 | €385,77 | €46,29 | €34,90 |
| Principale 4H | SHIB | LONG | Confluenza trend | 240m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €8,88 | €26,63 | €2,22 | €-1,03 |
| Bilanciata 1H V1 | ADA | SHORT | Confluenza trend | 60m | 3,0x | 0,16703 | 0,16703 | 0,16365 | 0,22187 | 0,16112 | €978,72 | €2.936,17 | €0,00 | €-0,00 |
| Bilanciata 1H V1 | AKE | LONG | Confluenza trend | 60m | 3,0x | 0,00329 | 0,00329 | 0,00290 | 0,00221 | 0,00408 | €12,36 | €37,07 | €4,45 | €0,00 |
| Bilanciata 1H V1 | ALLO | SHORT | Confluenza trend | 60m | 3,0x | 0,36179 | 0,36179 | 0,40521 | 0,48058 | 0,27496 | €141,53 | €424,59 | €50,95 | €-0,00 |
| Bilanciata 1H V1 | BANK | LONG | Confluenza trend | 60m | 3,0x | 0,38137 | 0,39497 | 0,34474 | 0,25615 | 0,45462 | €172,02 | €516,05 | €49,56 | €18,41 |
| Bilanciata 1H V1 | ETH | LONG | Confluenza trend | 60m | 3,0x | 1943,95871 | 1954,80000 | 1915,96571 | 1305,69227 | 1999,94472 | €1.144,39 | €3.433,17 | €49,44 | €19,15 |
| Bilanciata 1H V1 | HYPE | LONG | Confluenza trend | 60m | 3,0x | 60,41523 | 60,37900 | 59,54525 | 40,57889 | 62,15519 | €12,00 | €36,00 | €0,52 | €-0,02 |
| 1H Balanced Long No Rhv V1 | AKE | LONG | Confluenza trend | 60m | 3,0x | 0,00320 | 0,00320 | 0,00282 | 0,00215 | 0,00397 | €138,85 | €416,55 | €49,99 | €0,00 |
| 1H Balanced Long No Rhv V1 | BEAT | LONG | Confluenza trend | 60m | 3,0x | 3,29017 | 3,29017 | 3,00714 | 2,20990 | 3,85623 | €193,69 | €581,07 | €49,98 | €0,00 |
| 1H Balanced Long No Rhv V1 | XMR | LONG | Confluenza trend | 60m | 3,0x | 366,72991 | 366,72991 | 360,04130 | 246,32025 | 380,10712 | €915,26 | €2.745,79 | €50,08 | €0,00 |
| 1H Balanced Long No Rhv V1 | BANK | LONG | Confluenza trend | 60m | 3,0x | 0,38137 | 0,39497 | 0,34474 | 0,25615 | 0,45462 | €164,19 | €492,56 | €47,31 | €17,57 |
| Bilanciata 1H V2 | ADA | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,16276 | 0,16276 | 0,16511 | 0,21620 | 0,15807 | €1.185,56 | €3.556,68 | €51,22 | €-0,00 |
| Bilanciata 1H V2 | AKE | LONG | Confluenza trend V2 | 60m | 3,0x | 0,00320 | 0,00320 | 0,00282 | 0,00215 | 0,00397 | €142,81 | €428,43 | €51,41 | €0,00 |
| Bilanciata 1H V2 | WLD | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,34349 | 0,34349 | 0,35287 | 0,45627 | 0,32475 | €26,53 | €79,60 | €2,17 | €-0,00 |
| Bilanciata 1H V2 | ALLO | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,35543 | 0,35543 | 0,39400 | 0,47213 | 0,27829 | €146,68 | €440,04 | €47,75 | €-0,00 |
| Bilanciata 1H V3 Filtered | BEAT | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 3,31215 | 3,31215 | 3,02723 | 2,22466 | 3,88198 | €203,36 | €610,09 | €52,48 | €0,00 |
| Bilanciata 1H V3 Filtered | WLD | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,34349 | 0,34349 | 0,35287 | 0,45627 | 0,32475 | €23,43 | €70,29 | €1,92 | €-0,00 |
| Bilanciata 1H V3 Filtered | AKE | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,00330 | 0,00330 | 0,00293 | 0,00221 | 0,00403 | €158,25 | €474,75 | €52,90 | €0,00 |
| Bilanciata 1H V3 Filtered | ALLO | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,34255 | 0,34255 | 0,37914 | 0,45502 | 0,26938 | €160,61 | €481,84 | €51,46 | €-0,00 |
| Bilanciata 1H V3 Filtered | SHIB | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €8,58 | €25,73 | €1,38 | €-0,77 |
| Bilanciata 1H V3 Filtered | ESPORTS | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,02905 | 0,02685 | 0,03254 | 0,03859 | 0,02208 | €142,96 | €428,87 | €51,46 | €32,54 |
| Bilanciata 1H V3 Filtered | ETH | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1958,25157 | 1954,80000 | 1930,05275 | 1315,29231 | 2014,64922 | €8,95 | €26,84 | €0,39 | €-0,05 |
| Rapida 1H V1 | ADA | SHORT | Momentum / breakout | 60m | 3,0x | 0,16185 | 0,16185 | 0,16367 | 0,21499 | 0,15913 | €1.486,90 | €4.460,70 | €49,96 | €-0,00 |
| Rapida 1H V1 | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00320 | 0,00320 | 0,00286 | 0,00215 | 0,00370 | €158,12 | €474,35 | €49,93 | €0,00 |
| 1H Fast Score 6 75 V1 | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00320 | 0,00320 | 0,00287 | 0,00215 | 0,00369 | €167,22 | €501,65 | €51,54 | €0,00 |
| 1H Fast Score 6 75 V1 | ALLO | SHORT | Momentum / breakout | 60m | 3,0x | 0,33713 | 0,33713 | 0,36471 | 0,44782 | 0,29576 | €212,67 | €638,01 | €52,19 | €-0,00 |
| 1H Fast Score 6 75 V1 | BANK | LONG | Momentum / breakout | 60m | 3,0x | 0,38680 | 0,39497 | 0,35294 | 0,25980 | 0,43759 | €197,79 | €593,37 | €51,94 | €12,54 |
| 1H Fast Score 6 75 V1 | SHIB | LONG | Momentum / breakout | 60m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €11,70 | €35,09 | €1,52 | €-0,73 |
| 1H Fast Score 6 75 V1 | ETH | LONG | Momentum / breakout | 60m | 3,0x | 1943,95871 | 1954,80000 | 1922,18638 | 1305,69227 | 1976,61722 | €1.472,77 | €4.418,31 | €49,49 | €24,64 |
| 1H Fast Score 6 75 V1 | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 60,04501 | 60,37900 | 59,37250 | 40,33023 | 61,05376 | €8,47 | €25,40 | €0,28 | €0,14 |
| 1H Fast Score 6 75 No Trend Up V1 | BEAT | LONG | Momentum / breakout | 60m | 3,0x | 3,29017 | 3,29017 | 3,07004 | 2,20990 | 3,62037 | €256,24 | €768,73 | €51,43 | €0,00 |
| 1H Fast Score 6 75 No Trend Up V1 | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00322 | 0,00322 | 0,00289 | 0,00216 | 0,00372 | €167,84 | €503,53 | €51,67 | €0,00 |
| 1H Fast Score 6 75 No Trend Up V1 | BANK | LONG | Momentum / breakout | 60m | 3,0x | 0,38680 | 0,39497 | 0,35294 | 0,25980 | 0,43759 | €194,63 | €583,90 | €51,12 | €12,34 |
| 1H Fast Score 6 75 No Trend Up V1 | ALLO | SHORT | Momentum / breakout | 60m | 3,0x | 0,33808 | 0,33808 | 0,36389 | 0,44909 | 0,29937 | €218,91 | €656,73 | €50,14 | €-0,00 |
| 1H Fast Score 6 75 Range Only V1 | BEAT | LONG | Momentum / breakout | 60m | 3,0x | 3,29017 | 3,29017 | 3,07004 | 2,20990 | 3,62037 | €256,24 | €768,73 | €51,43 | €0,00 |
| 1H Fast Score 6 75 Range Only V1 | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00322 | 0,00322 | 0,00289 | 0,00216 | 0,00372 | €167,84 | €503,53 | €51,67 | €0,00 |
| 1H Fast Score 6 75 Range Only V1 | ESPORTS | SHORT | Momentum / breakout | 60m | 3,0x | 0,02828 | 0,02685 | 0,03168 | 0,03757 | 0,02319 | €143,01 | €429,04 | €51,48 | €21,76 |
| 1H Fast Score 6 75 Range Only V1 | SHIB | LONG | Momentum / breakout | 60m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €394,57 | €1.183,71 | €51,34 | €-24,78 |
| 1H Fast Score 6 75 Cost Aware V1 | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00322 | 0,00322 | 0,00289 | 0,00216 | 0,00372 | €167,51 | €502,54 | €51,57 | €0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | ALLO | SHORT | Momentum / breakout | 60m | 3,0x | 0,33713 | 0,33713 | 0,36471 | 0,44782 | 0,29576 | €211,20 | €633,59 | €51,83 | €-0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | BANK | LONG | Momentum / breakout | 60m | 3,0x | 0,38680 | 0,39497 | 0,35294 | 0,25980 | 0,43759 | €197,03 | €591,09 | €51,75 | €12,49 |
| 1H Fast Score 6 75 Cost Aware V1 | SHIB | LONG | Momentum / breakout | 60m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €11,64 | €34,93 | €1,52 | €-0,73 |
| 1H Fast Score 6 75 Cost Aware V1 | ETH | LONG | Momentum / breakout | 60m | 3,0x | 1943,95871 | 1954,80000 | 1922,18638 | 1305,69227 | 1976,61722 | €1.465,09 | €4.395,27 | €49,23 | €24,51 |
| 1H Fast Nohigh Cap75 V1 | BEAT | LONG | Momentum / breakout | 60m | 3,0x | 3,29017 | 3,29017 | 3,07004 | 2,20990 | 3,62037 | €257,44 | €772,31 | €51,67 | €0,00 |
| 1H Fast Nohigh Cap75 V1 | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00320 | 0,00320 | 0,00287 | 0,00215 | 0,00369 | €165,85 | €497,54 | €51,12 | €0,00 |
| 1H Fast Nohigh Cap75 V1 | ALLO | SHORT | Momentum / breakout | 60m | 3,0x | 0,33808 | 0,33808 | 0,36389 | 0,44909 | 0,29937 | €225,73 | €677,19 | €51,70 | €-0,00 |
| 1H Fast Nohigh Cap75 V1 | PEPE | LONG | Momentum / breakout | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €938,65 | €2.815,95 | €52,29 | €-9,87 |
| 1H Fast Nohigh Cap75 V1 | ETH | LONG | Momentum / breakout | 60m | 3,0x | 1943,95871 | 1954,80000 | 1922,18638 | 1305,69227 | 1976,61722 | €57,45 | €172,34 | €1,93 | €0,96 |
| 1H Fast Long Btc 1 3 Cap75 V1 | SHIB | LONG | Momentum / breakout | 60m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €385,88 | €1.157,65 | €50,21 | €-24,24 |
| 1H Fast Long Btc 1 3 Cap75 V1 | XRP | LONG | Momentum / breakout | 60m | 3,0x | 1,11443 | 1,10753 | 1,10195 | 0,74853 | 1,13316 | €70,58 | €211,74 | €2,37 | €-1,31 |
| 1H Fast Long Btc 1 3 Cap75 V1 | ETH | LONG | Momentum / breakout | 60m | 3,0x | 1947,14935 | 1954,80000 | 1925,34128 | 1307,83531 | 1979,86146 | €1.491,96 | €4.475,89 | €50,13 | €17,59 |
| 1H Fast Long Btc 1 3 Cap75 V1 | BANK | LONG | Momentum / breakout | 60m | 3,0x | 0,38852 | 0,39497 | 0,36054 | 0,26095 | 0,43048 | €231,50 | €694,50 | €50,01 | €11,53 |
| 1H Fast Long Btc 1 3 Cap75 V1 | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 60,04501 | 60,37900 | 59,37250 | 40,33023 | 61,05376 | €1.416,99 | €4.250,97 | €47,61 | €23,65 |
| 1H Fast No Pepe V1 | ADA | SHORT | Momentum / breakout | 60m | 3,0x | 0,16185 | 0,16185 | 0,16367 | 0,21499 | 0,15913 | €1.512,75 | €4.538,24 | €50,83 | €-0,00 |
| 1H Fast No Pepe V1 | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00320 | 0,00320 | 0,00286 | 0,00215 | 0,00370 | €160,87 | €482,60 | €50,80 | €0,00 |
| 1H Fast No Pepe V1 | WLD | SHORT | Momentum / breakout | 60m | 3,0x | 0,34959 | 0,34959 | 0,35668 | 0,46437 | 0,33896 | €838,72 | €2.516,16 | €51,00 | €-0,00 |
| 1H Fast No Pepe V1 | BANK | LONG | Momentum / breakout | 60m | 3,0x | 0,37568 | 0,39497 | 0,34052 | 0,25233 | 0,42842 | €175,27 | €525,81 | €49,21 | €27,01 |
| 1H Fast No Pepe V1 | ETH | LONG | Momentum / breakout | 60m | 3,0x | 1943,95871 | 1954,80000 | 1922,18638 | 1305,69227 | 1976,61722 | €15,56 | €46,69 | €0,52 | €0,26 |
| 1H Fast Tp2 V1 | ADA | SHORT | Momentum / breakout | 60m | 3,0x | 0,16185 | 0,16185 | 0,16367 | 0,21499 | 0,15823 | €1.482,83 | €4.448,49 | €49,82 | €-0,00 |
| 1H Fast Tp2 V1 | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00320 | 0,00320 | 0,00286 | 0,00215 | 0,00387 | €157,69 | €473,06 | €49,80 | €0,00 |
| 1H Fast Tp2 V1 | WLD | SHORT | Momentum / breakout | 60m | 3,0x | 0,34959 | 0,34959 | 0,35668 | 0,46437 | 0,33542 | €42,01 | €126,02 | €2,55 | €-0,00 |
| 1H Fast Tp2 V1 | BANK | LONG | Momentum / breakout | 60m | 3,0x | 0,37568 | 0,39497 | 0,34052 | 0,25233 | 0,44600 | €177,34 | €532,02 | €49,79 | €27,32 |
| 1H Fast Tp2 V1 | ALLO | SHORT | Momentum / breakout | 60m | 3,0x | 0,35543 | 0,35543 | 0,38543 | 0,47213 | 0,29543 | €187,33 | €561,99 | €47,43 | €-0,00 |
| 1H Fast Tp2 V1 | SHIB | LONG | Momentum / breakout | 60m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €10,60 | €31,81 | €1,45 | €-0,61 |
| Rapida 1H V2 | TAO | SHORT | Momentum / breakout V2 | 60m | 3,0x | 188,48684 | 188,48684 | 190,75481 | 250,37335 | 185,08488 | €1.390,02 | €4.170,07 | €50,18 | €-0,00 |
| Rapida 1H V2 | ADA | SHORT | Momentum / breakout V2 | 60m | 3,0x | 0,16185 | 0,16185 | 0,16367 | 0,21499 | 0,15913 | €1.494,54 | €4.483,63 | €50,22 | €-0,00 |
| Rapida 1H V2 | XRP | LONG | Momentum / breakout V2 | 60m | 3,0x | 1,11443 | 1,10753 | 1,10195 | 0,74853 | 1,13316 | €1.498,43 | €4.495,30 | €50,35 | €-27,84 |
| Rapida 1H V3 Filtered | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16185 | 0,16185 | 0,16367 | 0,21499 | 0,15913 | €1.521,20 | €4.563,60 | €51,11 | €-0,00 |
| Rapida 1H V3 Filtered | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00320 | 0,00320 | 0,00286 | 0,00215 | 0,00370 | €161,77 | €485,30 | €51,08 | €0,00 |
| Rapida 1H V3 Filtered | WLD | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,34959 | 0,34959 | 0,35668 | 0,46437 | 0,33896 | €843,41 | €2.530,22 | €51,28 | €-0,00 |
| Rapida 1H V3 Filtered | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,37568 | 0,39497 | 0,34052 | 0,25233 | 0,42842 | €176,34 | €529,01 | €49,51 | €27,17 |
| Rapida 1H V3 Filtered | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1943,95871 | 1954,80000 | 1922,18638 | 1305,69227 | 1976,61722 | €15,97 | €47,91 | €0,54 | €0,27 |
| 1H Fast V3 Cap75 V1 | BEAT | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 3,29017 | 3,29017 | 3,07004 | 2,20990 | 3,62037 | €258,77 | €776,32 | €51,94 | €0,00 |
| 1H Fast V3 Cap75 V1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00320 | 0,00320 | 0,00287 | 0,00215 | 0,00369 | €166,71 | €500,13 | €51,38 | €0,00 |
| 1H Fast V3 Cap75 V1 | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,38680 | 0,39497 | 0,35294 | 0,25980 | 0,43759 | €197,36 | €592,09 | €51,83 | €12,51 |
| 1H Fast V3 Cap75 V1 | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,33808 | 0,33808 | 0,36389 | 0,44909 | 0,29937 | €227,32 | €681,96 | €52,06 | €-0,00 |
| 1H Fast V3 Cap75 V1 | SHIB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €10,86 | €32,57 | €1,41 | €-0,68 |
| 1H Fast V3 Nohigh V1 | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16185 | 0,16185 | 0,16367 | 0,21499 | 0,15913 | €1.485,86 | €4.457,58 | €49,92 | €-0,00 |
| 1H Fast V3 Nohigh V1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00320 | 0,00320 | 0,00286 | 0,00215 | 0,00370 | €158,01 | €474,02 | €49,90 | €0,00 |
| 1H Fast V3 Nohigh V1 | WLD | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,34959 | 0,34959 | 0,35668 | 0,46437 | 0,33896 | €823,75 | €2.471,25 | €50,08 | €-0,00 |
| 1H Fast V3 Nohigh V1 | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,37568 | 0,39497 | 0,34052 | 0,25233 | 0,42842 | €172,41 | €517,23 | €48,41 | €26,57 |
| 1H Fast V3 Nohigh V1 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1943,95871 | 1954,80000 | 1922,18638 | 1305,69227 | 1976,61722 | €15,61 | €46,83 | €0,52 | €0,26 |
| 1H Fast V3 Long Only V1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00320 | 0,00320 | 0,00286 | 0,00215 | 0,00370 | €155,06 | €465,19 | €48,97 | €0,00 |
| 1H Fast V3 Long Only V1 | BEAT | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 3,29017 | 3,29017 | 3,07004 | 2,20990 | 3,62037 | €243,96 | €731,87 | €48,97 | €0,00 |
| 1H Fast V3 Long Only V1 | SHIB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €375,62 | €1.126,85 | €48,88 | €-23,59 |
| 1H Fast V3 Long Only V1 | PEPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €880,10 | €2.640,29 | €49,03 | €-9,26 |
| 1H Fast V3 Long Nohigh Cap75 V1 | BEAT | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 3,29017 | 3,29017 | 3,07004 | 2,20990 | 3,62037 | €246,62 | €739,85 | €49,50 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 V1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00322 | 0,00322 | 0,00289 | 0,00216 | 0,00372 | €160,75 | €482,24 | €49,49 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 V1 | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,38680 | 0,39497 | 0,35294 | 0,25980 | 0,43759 | €190,39 | €571,16 | €50,00 | €12,07 |
| 1H Fast V3 Long Nohigh Cap75 V1 | SHIB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €385,28 | €1.155,84 | €50,13 | €-24,20 |
| 1H Fast V3 Long Nohigh Cap75 V1 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1943,95871 | 1954,80000 | 1922,18638 | 1305,69227 | 1976,61722 | €23,15 | €69,46 | €0,78 | €0,39 |
| 1H Fast V3 No Esports V1 | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16185 | 0,16185 | 0,16367 | 0,21499 | 0,15913 | €1.489,89 | €4.469,66 | €50,06 | €-0,00 |
| 1H Fast V3 No Esports V1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00320 | 0,00320 | 0,00286 | 0,00215 | 0,00370 | €158,44 | €475,31 | €50,03 | €0,00 |
| 1H Fast V3 No Esports V1 | WLD | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,34959 | 0,34959 | 0,35668 | 0,46437 | 0,33896 | €825,98 | €2.477,95 | €50,22 | €-0,00 |
| 1H Fast V3 No Esports V1 | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,37568 | 0,39497 | 0,34052 | 0,25233 | 0,42842 | €172,88 | €518,63 | €48,54 | €26,64 |
| 1H Fast V3 No Esports V1 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1943,95871 | 1954,80000 | 1922,18638 | 1305,69227 | 1976,61722 | €15,65 | €46,96 | €0,53 | €0,26 |
| 1H Fast V3 No Esports Long Only V1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00320 | 0,00320 | 0,00286 | 0,00215 | 0,00370 | €158,13 | €474,39 | €49,94 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | BEAT | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 3,29017 | 3,29017 | 3,07004 | 2,20990 | 3,62037 | €248,78 | €746,34 | €49,93 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | SHIB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €20,15 | €60,45 | €2,62 | €-1,27 |
| 1H Fast V3 No Esports Long Only V1 | PEPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €909,76 | €2.729,29 | €50,68 | €-9,57 |
| 1H Fast V3 No Esports Long Only V1 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1943,95871 | 1954,80000 | 1922,18638 | 1305,69227 | 1976,61722 | €1.460,27 | €4.380,80 | €49,06 | €24,43 |
| 1H Fast V3 No Esports Long Only V1 | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 60,04501 | 60,37900 | 59,37250 | 40,33023 | 61,05376 | €14,96 | €44,89 | €0,50 | €0,25 |
| 1H Fast V3 No Esports Mfe Lock V1 | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16185 | 0,16185 | 0,16367 | 0,21499 | 0,15913 | €1.510,84 | €4.532,53 | €50,76 | €-0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | WLD | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,34959 | 0,34959 | 0,35668 | 0,46437 | 0,33896 | €11,86 | €35,57 | €0,72 | €-0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,33165 | 0,33165 | 0,36472 | 0,44055 | 0,28205 | €170,96 | €512,89 | €51,14 | €-0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00317 | 0,00317 | 0,00290 | 0,00213 | 0,00358 | €199,03 | €597,09 | €50,62 | €0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | PEPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €867,02 | €2.601,07 | €48,30 | €-9,12 |
| 1H Fast V3 No Esports Mfe Lock V1 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1943,95871 | 1954,80000 | 1943,95871 | 1305,69227 | 1976,61722 | €74,16 | €222,48 | €0,00 | €1,24 |
| 1H Fast V3 No Esports Stress Guard V1 | XRP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,11443 | 1,10753 | 1,10195 | 0,74853 | 1,13316 | €1.512,48 | €4.537,44 | €50,82 | €-28,11 |
| 1H Fast V3 No Esports Stress Guard V1 | PEPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €873,54 | €2.620,61 | €50,01 | €-17,62 |
| 1H Fast V3 No Esports Stress Guard V1 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1943,95871 | 1954,80000 | 1922,18638 | 1305,69227 | 1976,61722 | €1.485,05 | €4.455,15 | €49,90 | €24,85 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | BEAT | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 3,29017 | 3,29017 | 3,07004 | 2,20990 | 3,62037 | €245,16 | €735,47 | €49,21 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00322 | 0,00322 | 0,00289 | 0,00216 | 0,00372 | €159,93 | €479,80 | €49,24 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | SHIB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €15,43 | €46,28 | €2,01 | €-0,97 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | PEPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €875,11 | €2.625,32 | €48,75 | €-9,21 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1943,95871 | 1954,80000 | 1922,18638 | 1305,69227 | 1976,61722 | €1.459,48 | €4.378,44 | €49,04 | €24,42 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 60,04501 | 60,37900 | 59,37250 | 40,33023 | 61,05376 | €14,94 | €44,83 | €0,50 | €0,25 |
| Ampia 4H | HYPE | SHORT | Confluenza trend | 240m | 2,0x | 58,36732 | 60,37900 | 61,80927 | 87,25915 | 48,72988 | €424,03 | €848,06 | €50,01 | €-29,23 |
| Ampia 4H | TAO | SHORT | Confluenza trend | 240m | 2,0x | 189,05650 | 189,05650 | 197,51338 | 282,63946 | 165,37722 | €558,68 | €1.117,36 | €49,98 | €-0,00 |
| Ampia 4H | AKE | LONG | Confluenza trend | 240m | 2,0x | 0,00328 | 0,00328 | 0,00288 | 0,00165 | 0,00438 | €207,40 | €414,80 | €49,78 | €0,00 |
| Ampia 4H | XMR | LONG | Confluenza trend | 240m | 2,0x | 364,45854 | 364,45854 | 347,94701 | 184,05156 | 410,69083 | €544,42 | €1.088,84 | €49,33 | €0,00 |
| Forza relativa 1H V1 | NIGHT | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,02031 | 0,02031 | 0,02210 | 0,03036 | 0,01637 | €285,91 | €571,83 | €50,45 | €-0,00 |
| Forza relativa 1H V1 | ONDO | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,42171 | €891,90 | €1.783,80 | €49,29 | €0,00 |
| Forza relativa 1H V1 | WLD | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,32287 | €14,97 | €29,93 | €0,82 | €-0,00 |
| Forza relativa 1H V1 | AKE | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,00327 | 0,00327 | 0,00287 | 0,00165 | 0,00413 | €208,36 | €416,72 | €50,01 | €0,00 |
| Forza relativa 1H V1 | ETH | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 1943,95871 | 1954,80000 | 1915,96571 | 981,69915 | 2005,54333 | €1.433,90 | €2.867,80 | €41,30 | €15,99 |
| Forza relativa 1H V2 | AKE | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,00320 | 0,00320 | 0,00282 | 0,00162 | 0,00405 | €216,28 | €432,55 | €51,91 | €0,00 |
| Forza relativa 1H V2 | WLD | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,32287 | €47,70 | €95,39 | €2,60 | €-0,00 |
| Forza relativa 1H V2 | XMR | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 367,08012 | 367,08012 | 360,46822 | 185,37546 | 381,62629 | €1.446,12 | €2.892,24 | €52,10 | €0,00 |
| Forza relativa 1H V2 | BANK | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,36855 | 0,39497 | 0,33045 | 0,18612 | 0,45238 | €219,06 | €438,12 | €45,30 | €31,40 |
| Forza relativa 1H V2 | PEPE | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €846,05 | €1.692,10 | €47,31 | €-1,25 |
| Benchmark Donchian breakout 1H | SUI | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,76606 | 0,76606 | 0,75182 | 0,38686 | 0,80165 | €1.377,00 | €2.754,00 | €51,18 | €0,00 |
| Benchmark Donchian breakout 1H | ALLO | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,35678 | 0,35678 | 0,39959 | 0,53338 | 0,24974 | €215,19 | €430,38 | €51,65 | €-0,00 |
| Benchmark Donchian breakout 1H | HYPE | LONG | Donchian breakout 20 barre | 60m | 2,0x | 58,92678 | 60,37900 | 59,85884 | 29,75803 | 61,28385 | €1.635,95 | €3.271,90 | €0,00 | €80,63 |
| Benchmark Donchian breakout 1H | BANK | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,39689 | 0,39497 | 0,35670 | 0,20043 | 0,49737 | €258,64 | €517,28 | €52,39 | €-2,50 |
| Benchmark Donchian breakout 1H | ETH | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1958,25157 | 1954,80000 | 1926,91955 | 988,91704 | 2036,58163 | €70,73 | €141,45 | €2,26 | €-0,25 |
| Benchmark Bollinger mean reversion 1H | XRP | SHORT | Bollinger mean reversion | 60m | 2,0x | 1,11399 | 1,10753 | 1,12736 | 1,66541 | 1,09394 | €1.986,03 | €3.972,07 | €47,66 | €23,02 |
| Benchmark Bollinger mean reversion 1H | HYPE | SHORT | Bollinger mean reversion | 60m | 2,0x | 60,34277 | 60,37900 | 61,06689 | 90,21245 | 59,25660 | €1.980,47 | €3.960,93 | €47,53 | €-2,38 |
| Benchmark trend following EMA 1H | LAB | LONG | Trend following EMA | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €207,05 | €414,10 | €49,69 | €0,00 |
| Benchmark trend following EMA 1H | ALLO | SHORT | Trend following EMA | 60m | 2,0x | 0,35372 | 0,35372 | 0,39616 | 0,52881 | 0,26034 | €209,15 | €418,30 | €50,20 | €-0,00 |
| Benchmark trend following EMA 1H | XMR | LONG | Trend following EMA | 60m | 2,0x | 367,08012 | 367,08012 | 359,73357 | 185,37546 | 383,24253 | €17,91 | €35,83 | €0,72 | €0,00 |
| Benchmark trend following EMA 1H | BANK | LONG | Trend following EMA | 60m | 2,0x | 0,37568 | 0,39497 | 0,33059 | 0,18972 | 0,47485 | €205,19 | €410,38 | €49,25 | €21,08 |
| Benchmark trend following EMA 1H | SHIB | LONG | Trend following EMA | 60m | 2,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €389,51 | €779,03 | €49,98 | €-41,80 |
| Scanner Top 5 Long 1H | LAB | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €219,03 | €438,05 | €52,57 | €0,00 |
| Scanner Top 5 Long 1H | AKE | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,00319 | 0,00319 | 0,00281 | 0,00161 | 0,00396 | €224,41 | €448,82 | €53,86 | €0,00 |
| Scanner Top 5 Long 1H | XMR | LONG | Scanner Top 5 Long | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10712 | €70,71 | €141,42 | €2,58 | €0,00 |
| Scanner Top 5 Long 1H | PEPE | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.011,45 | €2.022,90 | €49,63 | €-20,41 |
| Scanner Top 5 Long 1H | ETH | LONG | Scanner Top 5 Long | 60m | 2,0x | 1943,95871 | 1954,80000 | 1915,96571 | 981,69915 | 1999,94472 | €1.778,37 | €3.556,74 | €51,22 | €19,84 |
| Scanner Top 5 Long 1H | HYPE | LONG | Scanner Top 5 Long | 60m | 2,0x | 60,04501 | 60,37900 | 59,18036 | 30,32273 | 61,77430 | €14,18 | €28,35 | €0,41 | €0,16 |
| Scanner Bottom 5 Short 1H | ADA | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,16703 | 0,16703 | 0,16365 | 0,24971 | 0,16112 | €1.381,07 | €2.762,13 | €0,00 | €-0,00 |
| Scanner Bottom 5 Short 1H | ALLO | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,36179 | 0,36179 | 0,40521 | 0,54088 | 0,27496 | €202,53 | €405,06 | €48,61 | €-0,00 |
| Scanner Bottom 5 Short 1H | ESPORTS | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,03342 | 0,02685 | 0,03342 | 0,04997 | 0,02540 | €202,66 | €405,32 | €0,00 | €79,71 |
| Scanner Top10 Long | AKE | LONG | Scanner Top10 Long | 60m | 2,0x | 0,00319 | 0,00319 | 0,00281 | 0,00161 | 0,00396 | €208,33 | €416,67 | €50,00 | €0,00 |
| Scanner Top10 Long | XMR | LONG | Scanner Top10 Long | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10712 | €1.371,36 | €2.742,71 | €50,02 | €0,00 |
| Scanner Top10 Long | BANK | LONG | Scanner Top10 Long | 60m | 2,0x | 0,37568 | 0,39497 | 0,33059 | 0,18972 | 0,46584 | €203,89 | €407,78 | €48,93 | €20,94 |
| Scanner Top10 Long | SHIB | LONG | Scanner Top10 Long | 60m | 2,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €24,14 | €48,29 | €2,71 | €-0,66 |
| Scanner Top10 Long | PEPE | LONG | Scanner Top10 Long | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €924,43 | €1.848,86 | €45,36 | €-18,65 |
| Scanner Bottom10 Short | ADA | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,16193 | 0,16193 | 0,16426 | 0,24209 | 0,15727 | €1.731,26 | €3.462,51 | €49,86 | €-0,00 |
| Scanner Bottom10 Short | ALLO | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,35250 | 0,35250 | 0,39075 | 0,52699 | 0,27600 | €224,69 | €449,38 | €48,76 | €-0,00 |
| Scanner Bottom10 Short | ESPORTS | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,03342 | 0,02685 | 0,03342 | 0,04997 | 0,02540 | €203,44 | €406,87 | €0,00 | €80,02 |
| Scanner Top15 Long | AKE | LONG | Scanner Top15 Long | 60m | 2,0x | 0,00319 | 0,00319 | 0,00281 | 0,00161 | 0,00396 | €208,33 | €416,67 | €50,00 | €0,00 |
| Scanner Top15 Long | XMR | LONG | Scanner Top15 Long | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10712 | €1.371,36 | €2.742,71 | €50,02 | €0,00 |
| Scanner Top15 Long | BANK | LONG | Scanner Top15 Long | 60m | 2,0x | 0,37568 | 0,39497 | 0,33059 | 0,18972 | 0,46584 | €203,89 | €407,78 | €48,93 | €20,94 |
| Scanner Top15 Long | SHIB | LONG | Scanner Top15 Long | 60m | 2,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €24,14 | €48,29 | €2,71 | €-0,66 |
| Scanner Top15 Long | PEPE | LONG | Scanner Top15 Long | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €924,43 | €1.848,86 | €45,36 | €-18,65 |
| Scanner Bottom15 Short | ADA | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,16193 | 0,16193 | 0,16426 | 0,24209 | 0,15727 | €1.731,26 | €3.462,51 | €49,86 | €-0,00 |
| Scanner Bottom15 Short | ALLO | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,35250 | 0,35250 | 0,39075 | 0,52699 | 0,27600 | €224,69 | €449,38 | €48,76 | €-0,00 |
| Scanner Bottom15 Short | ESPORTS | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,03342 | 0,02685 | 0,03342 | 0,04997 | 0,02540 | €203,44 | €406,87 | €0,00 | €80,02 |
| Scanner Top20 Long | AKE | LONG | Scanner Top20 Long | 60m | 2,0x | 0,00319 | 0,00319 | 0,00281 | 0,00161 | 0,00396 | €208,33 | €416,67 | €50,00 | €0,00 |
| Scanner Top20 Long | XMR | LONG | Scanner Top20 Long | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10712 | €1.371,36 | €2.742,71 | €50,02 | €0,00 |
| Scanner Top20 Long | BANK | LONG | Scanner Top20 Long | 60m | 2,0x | 0,37568 | 0,39497 | 0,33059 | 0,18972 | 0,46584 | €203,89 | €407,78 | €48,93 | €20,94 |
| Scanner Top20 Long | SHIB | LONG | Scanner Top20 Long | 60m | 2,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €24,14 | €48,29 | €2,71 | €-0,66 |
| Scanner Top20 Long | PEPE | LONG | Scanner Top20 Long | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €924,43 | €1.848,86 | €45,36 | €-18,65 |
| Scanner Bottom20 Short | ADA | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,16193 | 0,16193 | 0,16426 | 0,24209 | 0,15727 | €1.731,26 | €3.462,51 | €49,86 | €-0,00 |
| Scanner Bottom20 Short | ALLO | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,35250 | 0,35250 | 0,39075 | 0,52699 | 0,27600 | €224,69 | €449,38 | €48,76 | €-0,00 |
| Scanner Bottom20 Short | ESPORTS | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,03342 | 0,02685 | 0,03342 | 0,04997 | 0,02540 | €203,44 | €406,87 | €0,00 | €80,02 |
| Scanner Top 5 + forza BTC 1H | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39694 | 0,39694 | 0,38539 | 0,20045 | 0,42235 | €898,57 | €1.797,15 | €52,29 | €0,00 |
| Scanner Top 5 + forza BTC 1H | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €216,56 | €433,12 | €51,97 | €0,00 |
| Scanner Top 5 + forza BTC 1H | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00319 | 0,00319 | 0,00281 | 0,00161 | 0,00403 | €219,41 | €438,82 | €52,66 | €0,00 |
| Scanner Top 5 + forza BTC 1H | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 381,44484 | €37,16 | €74,32 | €1,36 | €0,00 |
| Scanner Top 5 + forza BTC 1H | ETH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1943,95871 | 1954,80000 | 1915,96571 | 981,69915 | 2005,54333 | €1.658,75 | €3.317,49 | €47,77 | €18,50 |
| Scanner Top 5 + forza BTC 1H | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 60,04501 | 60,37900 | 59,18036 | 30,32273 | 61,94723 | €12,65 | €25,30 | €0,36 | €0,14 |
| Scanner Top5 Btc Mfe V1 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39924 | 0,39924 | 0,38729 | 0,20162 | 0,42552 | €835,46 | €1.670,91 | €50,00 | €0,00 |
| Scanner Top5 Btc Mfe V1 | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 367,08012 | 367,08012 | 360,46822 | 185,37546 | 381,62629 | €1.363,71 | €2.727,43 | €49,13 | €0,00 |
| Scanner Top5 Btc Mfe V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00322 | 0,00322 | 0,00284 | 0,00163 | 0,00407 | €196,51 | €393,01 | €47,16 | €0,00 |
| Scanner Top5 Btc Mfe V1 | ETH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1947,14935 | 1954,80000 | 1919,11040 | 983,31042 | 2008,83504 | €1.634,22 | €3.268,43 | €47,07 | €12,84 |
| Scanner Top5 Btc Mfe V1 | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 60,04501 | 60,37900 | 59,18036 | 30,32273 | 61,94723 | €36,62 | €73,24 | €1,05 | €0,41 |
| Scanner Top5 Btc Guard V1 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39724 | 0,39724 | 0,38434 | 0,20061 | 0,42561 | €756,62 | €1.513,24 | €49,13 | €0,00 |
| Scanner Top5 Btc Guard V1 | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €202,47 | €404,95 | €48,59 | €0,00 |
| Scanner Top5 Btc Guard V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00319 | 0,00319 | 0,00281 | 0,00161 | 0,00403 | €207,86 | €415,72 | €49,89 | €0,00 |
| Scanner Top5 Btc Guard V1 | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,38202 | 0,39497 | 0,34542 | 0,19292 | 0,46253 | €247,49 | €494,98 | €47,42 | €16,78 |
| Scanner Top5 Btc Btc Le3 V1 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39974 | 0,39974 | 0,38840 | 0,20187 | 0,42468 | €884,65 | €1.769,29 | €50,18 | €0,00 |
| Scanner Top5 Btc Btc Le3 V1 | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €207,87 | €415,74 | €49,89 | €0,00 |
| Scanner Top5 Btc Btc Le3 V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00319 | 0,00319 | 0,00281 | 0,00161 | 0,00403 | €210,72 | €421,44 | €50,57 | €0,00 |
| Scanner Top5 Btc Btc Le3 V1 | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 381,44484 | €37,63 | €75,26 | €1,37 | €0,00 |
| Scanner Top5 Btc Btc Le3 V1 | ETH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1943,95871 | 1954,80000 | 1915,96571 | 981,69915 | 2005,54333 | €1.593,18 | €3.186,36 | €45,88 | €17,77 |
| Scanner Top5 Btc Btc 2 3 V1 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39974 | 0,39974 | 0,38840 | 0,20187 | 0,42468 | €884,65 | €1.769,29 | €50,18 | €0,00 |
| Scanner Top5 Btc Btc 2 3 V1 | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €207,87 | €415,74 | €49,89 | €0,00 |
| Scanner Top5 Btc Btc 2 3 V1 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €996,29 | €1.992,58 | €48,89 | €-13,40 |
| Scanner Top5 Btc Btc 2 3 V1 | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39505 | 0,39497 | 0,35720 | 0,19950 | 0,47832 | €252,36 | €504,73 | €48,36 | €-0,10 |
| Scanner Top5 Btc Guard Mfe V1 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39724 | 0,39724 | 0,38434 | 0,20061 | 0,42561 | €756,62 | €1.513,24 | €49,13 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00322 | 0,00322 | 0,00284 | 0,00163 | 0,00407 | €201,88 | €403,77 | €48,45 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | SHIB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €407,51 | €815,02 | €45,45 | €-17,06 |
| Scanner Top5 Btc Guard Mfe V1 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.000,26 | €2.000,52 | €47,76 | €-7,02 |
| Scanner Top5 Btc Guard Btc Le3 V1 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39974 | 0,39974 | 0,38840 | 0,20187 | 0,42468 | €871,05 | €1.742,11 | €49,41 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €205,84 | €411,68 | €49,40 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00319 | 0,00319 | 0,00281 | 0,00161 | 0,00403 | €211,32 | €422,63 | €50,72 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,37568 | 0,39497 | 0,33059 | 0,18972 | 0,47485 | €14,78 | €29,56 | €3,55 | €1,52 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39974 | 0,39974 | 0,38840 | 0,20187 | 0,42468 | €871,05 | €1.742,11 | €49,41 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00322 | 0,00322 | 0,00284 | 0,00163 | 0,00407 | €204,20 | €408,41 | €49,01 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | SHIB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €414,63 | €829,26 | €46,24 | €-17,36 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.011,73 | €2.023,45 | €48,31 | €-7,10 |
| Scanner Top5 Btc Runner25 V1 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39694 | 0,39694 | 0,38539 | 0,20045 | 0,43159 | €861,83 | €1.723,66 | €50,15 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,21338 | €207,96 | €415,92 | €49,91 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00319 | 0,00319 | 0,00281 | 0,00161 | 0,00434 | €213,22 | €426,44 | €51,17 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 386,79573 | €70,70 | €141,40 | €2,58 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | ETH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1943,95871 | 1954,80000 | 1915,96571 | 981,69915 | 2027,93773 | €1.617,79 | €3.235,59 | €46,59 | €18,04 |
| Scanner Top5 Btc Tp3 V1 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39694 | 0,39694 | 0,38539 | 0,20045 | 0,43159 | €861,83 | €1.723,66 | €50,15 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,21338 | €207,96 | €415,92 | €49,91 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00319 | 0,00319 | 0,00281 | 0,00161 | 0,00434 | €213,56 | €427,11 | €51,25 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 386,79573 | €85,15 | €170,29 | €3,11 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | ETH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1943,95871 | 1954,80000 | 1915,96571 | 981,69915 | 2027,93773 | €1.579,98 | €3.159,95 | €45,50 | €17,62 |
| Combo Trend | AKE | LONG | Combo Trend | 60m | 2,0x | 0,00329 | 0,00329 | 0,00290 | 0,00166 | 0,00416 | €208,78 | €417,57 | €50,11 | €0,00 |
| Combo Trend | ALLO | SHORT | Combo Trend | 60m | 2,0x | 0,35372 | 0,35372 | 0,39616 | 0,52881 | 0,26034 | €209,35 | €418,70 | €50,24 | €-0,00 |
| Combo Trend | PEPE | LONG | Combo Trend | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €784,30 | €1.568,61 | €47,99 | €-8,24 |
| Combo Trend | SHIB | LONG | Combo Trend | 60m | 2,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €338,96 | €677,92 | €43,49 | €-36,37 |
| Combo Mean Reversion | AKE | SHORT | Combo Mean Reversion | 60m | 2,0x | 0,00320 | 0,00320 | 0,00356 | 0,00479 | 0,00263 | €225,46 | €450,91 | €50,00 | €-0,00 |
| Combo Scanner | ONDO | LONG | Combo Scanner | 60m | 2,0x | 0,39694 | 0,39694 | 0,38539 | 0,20045 | 0,42235 | €857,88 | €1.715,77 | €49,92 | €0,00 |
| Combo Scanner | LAB | LONG | Combo Scanner | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €207,54 | €415,08 | €49,81 | €0,00 |
| Combo Scanner | AKE | LONG | Combo Scanner | 60m | 2,0x | 0,00319 | 0,00319 | 0,00281 | 0,00161 | 0,00403 | €210,36 | €420,73 | €50,49 | €0,00 |
| Combo Scanner | XMR | LONG | Combo Scanner | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 381,44484 | €23,89 | €47,78 | €0,87 | €0,00 |
| Combo Scanner | ETH | LONG | Combo Scanner | 60m | 2,0x | 1943,95871 | 1954,80000 | 1915,96571 | 981,69915 | 2005,54333 | €1.616,34 | €3.232,67 | €46,55 | €18,03 |
| Combo Adaptive | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,40114 | 0,40114 | 0,38834 | 0,20258 | 0,42673 | €809,25 | €1.618,50 | €51,63 | €0,00 |
| Combo Adaptive | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15861 | 0,13958 | 0,08010 | 0,19668 | €213,13 | €426,26 | €51,15 | €0,00 |
| Combo Adaptive | WLD | SHORT | Combo Adaptive | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,32475 | €929,60 | €1.859,20 | €50,73 | €-0,00 |
| Combo Adaptive | ALLO | SHORT | Combo Adaptive | 60m | 2,0x | 0,36179 | 0,36179 | 0,40521 | 0,54088 | 0,27496 | €210,64 | €421,27 | €50,55 | €-0,00 |
| Combo Adaptive Mfe Trail | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39784 | 0,39784 | 0,38492 | 0,20091 | 0,42367 | €744,71 | €1.489,41 | €48,35 | €0,00 |
| Combo Adaptive Mfe Trail | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15861 | 0,13958 | 0,08010 | 0,19668 | €201,70 | €403,39 | €48,41 | €0,00 |
| Combo Adaptive Mfe Trail | WLD | SHORT | Combo Adaptive | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,32475 | €883,78 | €1.767,56 | €48,23 | €-0,00 |
| Combo Adaptive Mfe Trail | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,00330 | 0,00330 | 0,00293 | 0,00166 | 0,00403 | €203,95 | €407,90 | €45,45 | €0,00 |
| Combo Adaptive Quality7 V1 | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,40304 | 0,40304 | 0,39140 | 0,20354 | 0,42632 | €859,15 | €1.718,30 | €49,62 | €0,00 |
| Combo Adaptive Quality7 V1 | WLD | SHORT | Combo Adaptive | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,32475 | €919,99 | €1.839,97 | €50,21 | €-0,00 |
| Combo Adaptive Quality7 V1 | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,00327 | 0,00327 | 0,00287 | 0,00165 | 0,00405 | €209,81 | €419,62 | €50,35 | €0,00 |
| Combo Adaptive Quality7 V1 | ALLO | SHORT | Combo Adaptive | 60m | 2,0x | 0,36179 | 0,36179 | 0,40521 | 0,54088 | 0,27496 | €207,61 | €415,23 | €49,83 | €-0,00 |
| Combo Adaptive Quality7 V1 | SHIB | LONG | Combo Adaptive | 60m | 2,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €12,84 | €25,69 | €1,30 | €-1,00 |
| Combo Adaptive Regime V1 | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39724 | 0,39724 | 0,38434 | 0,20061 | 0,42303 | €757,94 | €1.515,88 | €49,21 | €0,00 |
| Combo Adaptive Regime V1 | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15861 | 0,13958 | 0,08010 | 0,19668 | €206,52 | €413,04 | €49,56 | €0,00 |
| Combo Adaptive Regime V1 | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.044,39 | €2.088,78 | €49,87 | €-7,32 |
| Combo Adaptive Regime V1 | ETH | LONG | Combo Adaptive | 60m | 2,0x | 1947,28938 | 1954,80000 | 1919,24841 | 983,38114 | 2003,37131 | €32,32 | €64,64 | €0,93 | €0,25 |
| Combo Adaptive Regime V1 | BANK | LONG | Combo Adaptive | 60m | 2,0x | 0,38202 | 0,39497 | 0,34542 | 0,19292 | 0,45521 | €253,56 | €507,13 | €48,58 | €17,20 |
| Combo Adaptive Regime V1 | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 60,41523 | 60,37900 | 59,54525 | 30,50969 | 62,15519 | €16,99 | €33,99 | €0,49 | €-0,02 |
| Combo Adaptive Quality7 Regime V1 | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,40554 | 0,40554 | 0,39390 | 0,20480 | 0,42882 | €864,27 | €1.728,54 | €49,61 | €0,00 |
| Combo Adaptive Quality7 Regime V1 | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.031,87 | €2.063,74 | €49,27 | €-7,24 |
| Combo Adaptive Quality7 Regime V1 | BANK | LONG | Combo Adaptive | 60m | 2,0x | 0,38202 | 0,39497 | 0,34542 | 0,19292 | 0,45521 | €255,46 | €510,92 | €48,94 | €17,32 |
| Combo Adaptive Long Only V1 | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,41951 | €893,67 | €1.787,34 | €49,39 | €0,00 |
| Combo Adaptive Long Only V1 | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €205,55 | €411,10 | €49,33 | €0,00 |
| Combo Adaptive Long Only V1 | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,00319 | 0,00319 | 0,00281 | 0,00161 | 0,00396 | €205,22 | €410,44 | €49,25 | €0,00 |
| Combo Adaptive Long Only V1 | XMR | LONG | Combo Adaptive | 60m | 2,0x | 367,08012 | 367,08012 | 360,46822 | 185,37546 | 380,30391 | €1.384,19 | €2.768,37 | €49,86 | €0,00 |
| Combo Adaptive Long Only V1 | SHIB | LONG | Combo Adaptive | 60m | 2,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €12,85 | €25,69 | €1,44 | €-0,35 |
| Combo Adaptive Partial 1R V1 | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,41951 | €893,02 | €1.786,04 | €49,36 | €0,00 |
| Combo Adaptive Partial 1R V1 | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €205,22 | €410,44 | €49,25 | €0,00 |
| Combo Adaptive Partial 1R V1 | WLD | SHORT | Combo Adaptive | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,32475 | €895,30 | €1.790,60 | €48,86 | €-0,00 |
| Combo Adaptive Partial 1R V1 | ALLO | SHORT | Combo Adaptive | 60m | 2,0x | 0,36179 | 0,36179 | 0,40521 | 0,54088 | 0,27496 | €98,69 | €197,38 | €23,69 | €-0,00 |
| Combo Adaptive Partial 1R V1 | ETH | LONG | Combo Adaptive | 60m | 2,0x | 1949,77988 | 1954,80000 | 1921,70305 | 984,63884 | 2005,93354 | €13,89 | €27,78 | €0,40 | €0,07 |
| Combo Adaptive Partial 1R V1 | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €454,44 | €908,89 | €22,09 | €3,12 |
| Combo Adaptive Quality7 Regime Partial 1R V1 | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,40554 | 0,40554 | 0,39390 | 0,20480 | 0,42882 | €864,27 | €1.728,54 | €49,61 | €0,00 |
| Combo Adaptive Quality7 Regime Partial 1R V1 | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.038,23 | €2.076,45 | €49,58 | €-7,28 |
| Combo Adaptive Quality7 Regime Partial 1R V1 | BANK | LONG | Combo Adaptive | 60m | 2,0x | 0,38202 | 0,39497 | 0,34542 | 0,19292 | 0,45521 | €257,03 | €514,07 | €49,25 | €17,43 |
| Combo Adaptive Runner25 V1 | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,43050 | €902,18 | €1.804,37 | €49,86 | €0,00 |
| Combo Adaptive Runner25 V1 | WLD | SHORT | Combo Adaptive | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,31537 | €919,67 | €1.839,35 | €50,19 | €-0,00 |
| Combo Adaptive Runner25 V1 | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,00327 | 0,00327 | 0,00287 | 0,00165 | 0,00444 | €209,99 | €419,98 | €50,40 | €0,00 |
| Combo Adaptive Runner25 V1 | XMR | LONG | Combo Adaptive | 60m | 2,0x | 367,08012 | 367,08012 | 360,46822 | 185,37546 | 386,91580 | €27,35 | €54,70 | €0,99 | €0,00 |
| Combo Adaptive Runner25 V1 | ALLO | SHORT | Combo Adaptive | 60m | 2,0x | 0,36179 | 0,36179 | 0,40521 | 0,54088 | 0,23155 | €207,78 | €415,57 | €49,87 | €-0,00 |
| Combo Adaptive Tp3 V1 | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,43050 | €902,18 | €1.804,37 | €49,86 | €0,00 |
| Combo Adaptive Tp3 V1 | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15861 | 0,13958 | 0,08010 | 0,21571 | €207,43 | €414,86 | €49,78 | €0,00 |
| Combo Adaptive Tp3 V1 | WLD | SHORT | Combo Adaptive | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,31537 | €911,80 | €1.823,59 | €49,76 | €-0,00 |
| Combo Adaptive Tp3 V1 | ALLO | SHORT | Combo Adaptive | 60m | 2,0x | 0,36179 | 0,36179 | 0,40521 | 0,54088 | 0,23155 | €205,00 | €410,00 | €49,20 | €-0,00 |
| Sol Ema 4H | SOL | SHORT | Trend following EMA | 240m | 2,0x | 75,05699 | 76,32600 | 77,22103 | 112,21019 | 69,64688 | €862,58 | €1.725,17 | €49,74 | €-29,17 |
| Sol Donchian 4H | SOL | SHORT | Donchian breakout 20 barre | 240m | 2,0x | 75,96380 | 76,32600 | 78,23939 | 113,56589 | 69,59218 | €830,21 | €1.660,43 | €49,74 | €-7,92 |
| Sol Adaptive 4H | SOL | SHORT | Combo Adaptive | 240m | 2,0x | 75,96380 | 76,32600 | 78,44626 | 113,56589 | 69,75767 | €761,04 | €1.522,08 | €49,74 | €-7,26 |
| Eth Ema 1H | ETH | LONG | Trend following EMA | 60m | 3,0x | 1958,25157 | 1954,80000 | 1930,05275 | 1315,29231 | 2014,64922 | €1.132,15 | €3.396,44 | €48,91 | €-5,99 |
| Eth Ema 4H | ETH | LONG | Trend following EMA | 240m | 2,0x | 1949,77988 | 1954,80000 | 1902,99144 | 984,63884 | 2066,75096 | €1.036,30 | €2.072,59 | €49,74 | €5,34 |
| Eth Donchian 1H | ETH | LONG | Donchian breakout 20 barre | 60m | 3,0x | 1958,25157 | 1954,80000 | 1933,18595 | 1315,29231 | 2008,38281 | €1.292,62 | €3.877,86 | €49,64 | €-6,84 |
| Eth Bollinger 1H | ETH | SHORT | Bollinger mean reversion | 60m | 3,0x | 1957,46843 | 1954,80000 | 1980,95805 | 2600,17056 | 1922,23400 | €1.391,03 | €4.173,10 | €50,08 | €5,69 |
| Eth Adaptive 1H | ETH | LONG | Combo Adaptive | 60m | 3,0x | 1958,25157 | 1954,80000 | 1930,05275 | 1315,29231 | 2014,64922 | €1.140,50 | €3.421,49 | €49,27 | €-6,03 |
| Master Adaptive V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39854 | 0,39854 | 0,38677 | 0,20126 | 0,42207 | €833,00 | €1.665,99 | €49,19 | €0,00 |
| Master Adaptive V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €203,80 | €407,60 | €48,91 | €0,00 |
| Master Adaptive V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00319 | 0,00319 | 0,00281 | 0,00161 | 0,00396 | €205,42 | €410,83 | €49,30 | €0,00 |
| Master Adaptive V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10713 | €21,54 | €43,08 | €0,79 | €0,00 |
| Master Adaptive V1 | BANK | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,38852 | 0,39497 | 0,35255 | 0,19620 | 0,46046 | €240,10 | €480,20 | €44,46 | €7,97 |
| Master Adaptive No Alt V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39854 | 0,39854 | 0,38677 | 0,20126 | 0,42207 | €833,00 | €1.665,99 | €49,19 | €0,00 |
| Master Adaptive No Alt V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €203,80 | €407,60 | €48,91 | €0,00 |
| Master Adaptive No Alt V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00319 | 0,00319 | 0,00281 | 0,00161 | 0,00396 | €205,42 | €410,83 | €49,30 | €0,00 |
| Master Adaptive No Alt V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10713 | €21,54 | €43,08 | €0,79 | €0,00 |
| Master Adaptive No Alt V1 | BANK | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,38852 | 0,39497 | 0,35255 | 0,19620 | 0,46046 | €240,53 | €481,06 | €44,54 | €7,99 |
| Master Adaptive Strict3 V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,41951 | €887,07 | €1.774,14 | €49,03 | €0,00 |
| Master Adaptive Strict3 V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00320 | 0,00320 | 0,00282 | 0,00162 | 0,00397 | €201,87 | €403,75 | €48,45 | €0,00 |
| Master Adaptive Strict3 V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10713 | €1.330,61 | €2.661,21 | €48,54 | €0,00 |
| Master Adaptive Strict3 V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 1943,95871 | 1954,80000 | 1915,96571 | 981,69915 | 1999,94472 | €1.509,27 | €3.018,53 | €43,47 | €16,83 |
| Master Adaptive Expanded V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39854 | 0,39854 | 0,38677 | 0,20126 | 0,42207 | €833,00 | €1.665,99 | €49,19 | €0,00 |
| Master Adaptive Expanded V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €203,80 | €407,60 | €48,91 | €0,00 |
| Master Adaptive Expanded V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00319 | 0,00319 | 0,00281 | 0,00161 | 0,00396 | €206,32 | €412,65 | €49,52 | €0,00 |
| Master Adaptive Expanded V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10713 | €33,54 | €67,08 | €1,22 | €0,00 |
| Master Adaptive Expanded V1 | BANK | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,38852 | 0,39497 | 0,35255 | 0,19620 | 0,46046 | €241,27 | €482,55 | €44,68 | €8,01 |
| Master Adaptive Gb20 V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,40304 | 0,40304 | 0,39140 | 0,20354 | 0,42632 | €848,64 | €1.697,27 | €49,02 | €0,00 |
| Master Adaptive Gb20 V1 | RIF | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,10582 | 0,10582 | 0,09312 | 0,05344 | 0,13122 | €201,89 | €403,77 | €48,45 | €0,00 |
| Master Adaptive Gb20 V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 367,08012 | 367,08012 | 360,46822 | 185,37546 | 380,30391 | €1.348,01 | €2.696,02 | €48,56 | €0,00 |
| Master Adaptive Gb20 V1 | BANK | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,38852 | 0,39497 | 0,35255 | 0,19620 | 0,46046 | €253,27 | €506,54 | €46,90 | €8,41 |
| Master Adaptive Runner25 V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39854 | 0,39854 | 0,38677 | 0,20126 | 0,43384 | €833,00 | €1.665,99 | €49,19 | €0,00 |
| Master Adaptive Runner25 V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,21338 | €203,80 | €407,60 | €48,91 | €0,00 |
| Master Adaptive Runner25 V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00319 | 0,00319 | 0,00281 | 0,00161 | 0,00434 | €205,36 | €410,73 | €49,29 | €0,00 |
| Master Adaptive Runner25 V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 386,79573 | €20,87 | €41,74 | €0,76 | €0,00 |
| Master Adaptive Runner25 V1 | BANK | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,38852 | 0,39497 | 0,35255 | 0,19620 | 0,49643 | €241,27 | €482,53 | €44,68 | €8,01 |
| Combo Adaptive Side Regime Guard V1 | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,00320 | 0,00320 | 0,00282 | 0,00162 | 0,00397 | €212,78 | €425,56 | €51,07 | €0,00 |
| Combo Adaptive Side Regime Guard V1 | BANK | LONG | Combo Adaptive | 60m | 2,0x | 0,37568 | 0,39497 | 0,33059 | 0,18972 | 0,46584 | €212,08 | €424,15 | €50,90 | €21,78 |
| Combo Adaptive Side Regime Guard V1 | ALLO | SHORT | Combo Adaptive | 60m | 2,0x | 0,35250 | 0,35250 | 0,39075 | 0,52699 | 0,27600 | €235,86 | €471,72 | €51,19 | €-0,00 |
| Combo Adaptive Side Regime Guard V1 | SHIB | LONG | Combo Adaptive | 60m | 2,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €450,93 | €901,86 | €50,61 | €-12,39 |
| Master Adaptive Gb20 Be V1 | BEAT | LONG | Master Adaptive Consensus | 60m | 2,0x | 3,29017 | 3,29017 | 3,00714 | 1,66154 | 3,85623 | €291,32 | €582,63 | €50,12 | €0,00 |
| Master Adaptive Gb20 Be V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 367,86058 | 367,86058 | 361,23463 | 185,76959 | 381,11249 | €1.403,77 | €2.807,55 | €50,57 | €0,00 |
| Master Adaptive Gb20 Be V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00317 | 0,00317 | 0,00283 | 0,00160 | 0,00387 | €231,91 | €463,82 | €50,56 | €0,00 |
| Master Adaptive Gb20 Be V1 | BANK | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,38852 | 0,39497 | 0,35255 | 0,19620 | 0,46046 | €245,56 | €491,11 | €45,47 | €8,16 |
| Master Adaptive Gb20 Partial V1 | BEAT | LONG | Master Adaptive Consensus | 60m | 2,0x | 3,29017 | 3,29017 | 3,00714 | 1,66154 | 3,85623 | €291,05 | €582,09 | €50,07 | €0,00 |
| Master Adaptive Gb20 Partial V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10713 | €1.376,47 | €2.752,95 | €50,21 | €0,00 |
| Master Adaptive Gb20 Partial V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00322 | 0,00322 | 0,00284 | 0,00163 | 0,00400 | €209,67 | €419,35 | €50,32 | €0,00 |
| Master Adaptive Gb20 Partial V1 | BANK | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,37759 | 0,39497 | 0,33768 | 0,19068 | 0,45741 | €219,98 | €439,96 | €46,50 | €20,26 |
| Master Adaptive Gb20 Partial V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 1955,19096 | 1954,80000 | 1927,03621 | 987,37143 | 2011,50046 | €13,71 | €27,42 | €0,39 | €-0,01 |
| Master Adaptive Gb20 Loss Cap V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00275 | 0,00275 | 0,00242 | 0,00139 | 0,00362 | €208,32 | €416,65 | €50,00 | €0,00 |
| Master Adaptive Gb20 Loss Cap V1 | BEAT | LONG | Master Adaptive Consensus | 60m | 2,0x | 3,29017 | 3,29017 | 3,07790 | 1,66154 | 3,85623 | €388,25 | €776,50 | €50,10 | €0,00 |
| Master Adaptive Gb20 Loss Cap V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 361,71345 | 185,19860 | 380,10713 | €1.835,86 | €3.671,71 | €50,22 | €0,00 |
| Master Adaptive Gb20 Loss Cap V1 | BANK | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,38852 | 0,39497 | 0,36154 | 0,19620 | 0,46046 | €328,63 | €657,26 | €45,64 | €10,92 |
| 1H Fast V3 Nohigh Range Only V1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00320 | 0,00320 | 0,00286 | 0,00215 | 0,00370 | €161,22 | €483,65 | €50,91 | €0,00 |
| 1H Fast V3 Nohigh Range Only V1 | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,33165 | 0,33165 | 0,36472 | 0,44055 | 0,28205 | €170,92 | €512,75 | €51,13 | €-0,00 |
| 1H Fast V3 Nohigh Range Only V1 | ESPORTS | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,02828 | 0,02685 | 0,03168 | 0,03757 | 0,02319 | €142,68 | €428,04 | €51,37 | €21,71 |
| 1H Fast V3 Nohigh Regime Guard V1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00320 | 0,00320 | 0,00286 | 0,00215 | 0,00370 | €161,22 | €483,65 | €50,91 | €0,00 |
| 1H Fast V3 Nohigh Regime Guard V1 | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,33165 | 0,33165 | 0,36472 | 0,44055 | 0,28205 | €172,19 | €516,57 | €51,51 | €-0,00 |
| 1H Fast V3 Nohigh Regime Guard V1 | SHIB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €15,44 | €46,31 | €2,01 | €-0,97 |
| Main Side Regime Guard V1 | AKE | LONG | Confluenza trend | 240m | 3,0x | 0,00322 | 0,00322 | 0,00284 | 0,00216 | 0,00400 | €140,56 | €421,69 | €50,60 | €0,00 |
| Main Side Regime Guard V1 | ALLO | SHORT | Confluenza trend | 240m | 3,0x | 0,38070 | 0,38070 | 0,37357 | 0,50570 | 0,28933 | €140,03 | €420,08 | €0,00 | €-0,00 |
| Main Side Regime Guard V1 | PEPE | LONG | Confluenza trend | 240m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €326,47 | €979,41 | €50,44 | €3,40 |
| Main Side Regime Guard V1 | BANK | LONG | Confluenza trend | 240m | 3,0x | 0,38202 | 0,39497 | 0,33617 | 0,25659 | 0,47370 | €139,71 | €419,14 | €50,30 | €14,21 |
| Main Dynamic Asset Selector V1 | AKE | LONG | Confluenza trend | 240m | 3,0x | 0,00322 | 0,00322 | 0,00284 | 0,00216 | 0,00400 | €140,56 | €421,69 | €50,60 | €0,00 |
| Main Dynamic Asset Selector V1 | BANK | LONG | Confluenza trend | 240m | 3,0x | 0,38202 | 0,39497 | 0,33617 | 0,25659 | 0,47370 | €140,87 | €422,62 | €50,71 | €14,33 |
| Combo Trend Side Regime Guard V1 | AKE | LONG | Combo Trend | 60m | 2,0x | 0,00320 | 0,00320 | 0,00282 | 0,00162 | 0,00405 | €211,52 | €423,03 | €50,76 | €0,00 |
| Combo Trend Side Regime Guard V1 | BANK | LONG | Combo Trend | 60m | 2,0x | 0,37568 | 0,39497 | 0,33059 | 0,18972 | 0,47485 | €207,08 | €414,15 | €49,70 | €21,27 |
| Combo Trend Side Regime Guard V1 | ALLO | SHORT | Combo Trend | 60m | 2,0x | 0,35250 | 0,35250 | 0,39480 | 0,52699 | 0,25944 | €209,77 | €419,55 | €50,35 | €-0,00 |
| Combo Trend Side Regime Guard V1 | SHIB | LONG | Combo Trend | 60m | 2,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €14,70 | €29,40 | €1,89 | €-1,58 |
| Combo Trend Side Regime Guard V1 | PEPE | LONG | Combo Trend | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €12,55 | €25,09 | €0,84 | €0,14 |
| Combo Trend Side Regime Guard V1 | ETH | LONG | Combo Trend | 60m | 2,0x | 1949,77988 | 1954,80000 | 1918,58340 | 984,63884 | 2018,41213 | €12,70 | €25,41 | €0,41 | €0,07 |
| Combo Trend Side Regime Guard V1 | ESPORTS | SHORT | Combo Trend | 60m | 2,0x | 0,02845 | 0,02685 | 0,03187 | 0,04254 | 0,02094 | €202,36 | €404,73 | €48,57 | €22,82 |
| 1H Fast Nohigh Cap75 Short Only V1 | WLD | SHORT | Momentum / breakout | 60m | 3,0x | 0,34959 | 0,34959 | 0,35668 | 0,46437 | 0,33896 | €822,35 | €2.467,06 | €50,00 | €-0,00 |
| 1H Fast Nohigh Cap75 Short Only V1 | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00314 | 0,00314 | 0,00287 | 0,00211 | 0,00354 | €200,24 | €600,71 | €51,24 | €0,00 |
| 1H Fast Nohigh Cap75 Short Only V1 | ALLO | SHORT | Momentum / breakout | 60m | 3,0x | 0,33808 | 0,33808 | 0,36389 | 0,44909 | 0,29937 | €212,58 | €637,75 | €48,69 | €-0,00 |
| 1H Fast Nohigh Cap75 Short Only V1 | SHIB | LONG | Momentum / breakout | 60m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €25,54 | €76,62 | €3,32 | €-1,60 |
| 1H Fast Nohigh Cap75 Short Only V1 | ETH | LONG | Momentum / breakout | 60m | 3,0x | 1943,95871 | 1954,80000 | 1922,18638 | 1305,69227 | 1976,61722 | €1.451,62 | €4.354,85 | €48,77 | €24,29 |
| 1H Fast Nohigh Cap75 Short Only V1 | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 60,04501 | 60,37900 | 59,37250 | 40,33023 | 61,05376 | €14,15 | €42,44 | €0,48 | €0,24 |
| 1H Balanced V3 Long Only V1 | XMR | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 366,72991 | 366,72991 | 360,04130 | 246,32025 | 380,10712 | €913,56 | €2.740,69 | €49,99 | €0,00 |
| 1H Balanced V3 Long Only V1 | AKE | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,00328 | 0,00328 | 0,00288 | 0,00220 | 0,00406 | €137,93 | €413,80 | €49,66 | €0,00 |
| 1H Balanced V3 Long Only V1 | ALLO | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,34255 | 0,34255 | 0,37914 | 0,45502 | 0,26938 | €156,01 | €468,04 | €49,99 | €-0,00 |
| 1H Balanced V3 Long Only V1 | ESPORTS | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,03342 | 0,02685 | 0,03342 | 0,04440 | 0,02540 | €137,40 | €412,21 | €0,00 | €81,07 |
| 1H Balanced V3 Long Only V1 | ETH | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1958,25157 | 1954,80000 | 1930,05275 | 1315,29231 | 2014,64922 | €32,22 | €96,65 | €1,39 | €-0,17 |
| Scanner Bottom5 Short Profit Lock V1 | WLD | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,34449 | 0,34449 | 0,35368 | 0,51502 | 0,32613 | €937,87 | €1.875,74 | €50,00 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | ALLO | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,35250 | 0,35250 | 0,39075 | 0,52699 | 0,27600 | €227,60 | €455,20 | €49,39 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | ESPORTS | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,03342 | 0,02685 | 0,03262 | 0,04997 | 0,02540 | €206,07 | €412,14 | €0,00 | €81,06 |
| Scanner Bottom5 Short Mfe Trail V1 | WLD | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,34449 | 0,34449 | 0,35368 | 0,51502 | 0,32613 | €937,87 | €1.875,74 | €50,00 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | ALLO | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,35653 | 0,35653 | 0,39522 | 0,53301 | 0,27915 | €228,22 | €456,45 | €49,53 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | ESPORTS | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,02828 | 0,02685 | 0,03168 | 0,04229 | 0,02150 | €206,75 | €413,50 | €49,62 | €20,97 |
| Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00323 | 0,00323 | 0,00290 | 0,00217 | 0,00390 | €162,23 | €486,68 | €50,00 | €0,00 |
| Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | SHIB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €392,53 | €1.177,60 | €51,08 | €-24,66 |
| Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | PEPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €912,60 | €2.737,79 | €50,84 | €-9,60 |
| Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1943,95871 | 1954,80000 | 1922,18638 | 1305,69227 | 1987,50339 | €1.490,87 | €4.472,61 | €50,09 | €24,94 |
| Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 60,04501 | 60,37900 | 59,37250 | 40,33023 | 61,39001 | €13,99 | €41,96 | €0,47 | €0,23 |
| Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00320 | 0,00320 | 0,00287 | 0,00215 | 0,00386 | €162,16 | €486,47 | €49,98 | €0,00 |
| Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,35250 | 0,35250 | 0,38225 | 0,46824 | 0,29300 | €194,51 | €583,53 | €49,25 | €-0,00 |
| Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | PEPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €882,40 | €2.647,20 | €49,16 | €-9,28 |
| Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | ESPORTS | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,02998 | 0,02685 | 0,02998 | 0,03983 | 0,02279 | €132,90 | €398,69 | €0,00 | €41,67 |
| Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1943,95871 | 1954,80000 | 1922,18638 | 1305,69227 | 1987,50339 | €11,18 | €33,53 | €0,38 | €0,19 |
| Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 60,41523 | 60,37900 | 59,73858 | 40,57889 | 61,76853 | €19,28 | €57,83 | €0,65 | €-0,03 |
| Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | ESPORTS | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,02828 | 0,02685 | 0,03168 | 0,03757 | 0,02150 | €141,08 | €423,23 | €50,79 | €21,46 |
| Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | SHIB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €390,30 | €1.170,89 | €50,79 | €-24,52 |
| Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00323 | 0,00323 | 0,00290 | 0,00217 | 0,00390 | €162,03 | €486,10 | €49,94 | €0,00 |
| Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,35250 | 0,35250 | 0,38225 | 0,46824 | 0,29300 | €190,72 | €572,15 | €48,29 | €-0,00 |
| Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | SHIB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €390,89 | €1.172,67 | €50,86 | €-24,55 |
| Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | PEPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €911,83 | €2.735,48 | €50,80 | €-9,59 |
| Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1943,95871 | 1954,80000 | 1922,18638 | 1305,69227 | 1987,50339 | €58,50 | €175,50 | €1,97 | €0,98 |
| Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00317 | 0,00317 | 0,00290 | 0,00213 | 0,00371 | €196,95 | €590,84 | €50,09 | €0,00 |
| Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,33808 | 0,33808 | 0,36389 | 0,44909 | 0,28646 | €211,10 | €633,31 | €48,35 | €-0,00 |
| Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | PEPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €919,09 | €2.757,26 | €51,20 | €-9,67 |
| Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1943,95871 | 1954,80000 | 1943,95871 | 1305,69227 | 1987,50339 | €1.516,14 | €4.548,41 | €0,00 | €25,37 |
| Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,38852 | 0,39497 | 0,36054 | 0,26095 | 0,44447 | €14,38 | €43,13 | €3,11 | €0,72 |
| Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 60,04501 | 60,37900 | 59,37250 | 40,33023 | 61,39001 | €17,30 | €51,91 | €0,58 | €0,29 |
| Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00320 | 0,00320 | 0,00287 | 0,00215 | 0,00386 | €162,21 | €486,64 | €50,00 | €0,00 |
| Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | SHIB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €386,01 | €1.158,04 | €50,23 | €-24,25 |
| Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | PEPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €897,83 | €2.693,49 | €50,02 | €-9,45 |
| Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1943,95871 | 1954,80000 | 1922,18638 | 1305,69227 | 1987,50339 | €1.443,11 | €4.329,34 | €48,49 | €24,14 |
| Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 60,04501 | 60,37900 | 59,37250 | 40,33023 | 61,39001 | €13,53 | €40,59 | €0,45 | €0,23 |
| Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00319 | 0,00319 | 0,00287 | 0,00215 | 0,00385 | €162,18 | €486,55 | €49,99 | €0,00 |
| Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | SHIB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €397,61 | €1.192,82 | €51,74 | €-24,97 |
| Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | PEPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €924,39 | €2.773,18 | €51,50 | €-9,72 |
| Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1943,95871 | 1954,80000 | 1922,18638 | 1305,69227 | 1987,50339 | €1.522,40 | €4.567,21 | €51,15 | €25,47 |
| Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 60,04501 | 60,37900 | 59,37250 | 40,33023 | 61,39001 | €21,34 | €64,03 | €0,72 | €0,36 |
| Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00320 | 0,00320 | 0,00287 | 0,00215 | 0,00386 | €162,16 | €486,47 | €49,98 | €0,00 |
| Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,35250 | 0,35250 | 0,38225 | 0,46824 | 0,29300 | €194,51 | €583,53 | €49,25 | €-0,00 |
| Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | PEPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €882,40 | €2.647,20 | €49,16 | €-9,28 |
| Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1943,95871 | 1954,80000 | 1922,18638 | 1305,69227 | 1987,50339 | €1.423,15 | €4.269,44 | €47,82 | €23,81 |
| Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 60,04501 | 60,37900 | 59,37250 | 40,33023 | 61,39001 | €14,65 | €43,94 | €0,49 | €0,24 |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00320 | 0,00320 | 0,00287 | 0,00215 | 0,00386 | €162,23 | €486,68 | €50,00 | €0,00 |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,33713 | 0,33713 | 0,36471 | 0,44782 | 0,28197 | €208,24 | €624,73 | €51,11 | €-0,00 |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,38680 | 0,39497 | 0,35294 | 0,25980 | 0,45452 | €193,81 | €581,44 | €50,90 | €12,29 |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | XRP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,11443 | 1,10753 | 1,10195 | 0,74853 | 1,13940 | €23,07 | €69,20 | €0,78 | €-0,43 |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1952,19036 | 1954,80000 | 1930,32583 | 1311,22119 | 1995,91942 | €12,06 | €36,18 | €0,41 | €0,05 |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | ESPORTS | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,03070 | 0,02685 | 0,03070 | 0,04078 | 0,02333 | €138,06 | €414,17 | €0,00 | €51,99 |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 60,04501 | 60,37900 | 59,37250 | 40,33023 | 61,39001 | €17,07 | €51,20 | €0,57 | €0,28 |
| Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | XRP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,11443 | 1,10753 | 1,10195 | 0,74853 | 1,13940 | €1.516,65 | €4.549,94 | €50,96 | €-28,18 |
| Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | PEPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €875,94 | €2.627,83 | €50,14 | €-17,67 |
| Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1943,95871 | 1954,80000 | 1922,18638 | 1305,69227 | 1987,50339 | €1.489,14 | €4.467,43 | €50,04 | €24,91 |
| Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00320 | 0,00320 | 0,00289 | 0,00215 | 0,00382 | €172,57 | €517,70 | €50,00 | €0,00 |
| Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | SHIB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €10,87 | €32,61 | €1,41 | €-0,68 |
| Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | PEPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €916,91 | €2.750,72 | €51,08 | €-9,65 |
| Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1943,95871 | 1954,80000 | 1922,18638 | 1305,69227 | 1987,50339 | €1.512,51 | €4.537,54 | €50,82 | €25,31 |
| Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,38852 | 0,39497 | 0,36054 | 0,26095 | 0,44447 | €230,95 | €692,84 | €49,89 | €11,51 |
| Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 60,04501 | 60,37900 | 59,37250 | 40,33023 | 61,39001 | €10,44 | €31,33 | €0,35 | €0,17 |
| Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00317 | 0,00317 | 0,00290 | 0,00213 | 0,00371 | €200,37 | €601,11 | €50,97 | €0,00 |
| Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,35250 | 0,35250 | 0,38225 | 0,46824 | 0,29300 | €200,65 | €601,96 | €50,80 | €-0,00 |
| Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | ESPORTS | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,03342 | 0,02685 | 0,03342 | 0,04440 | 0,02540 | €136,12 | €408,37 | €0,00 | €80,31 |
| Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | SHIB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €36,61 | €109,84 | €4,76 | €-2,30 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Scanner Top5 Btc Btc 2 3 V1 | SHIB | LONG | 2026-07-27T04:53:37+00:00 | 0,00001 | €-51,04 | -1,03 | STOP |
| Benchmark Bollinger mean reversion 1H | HYPE | SHORT | 2026-07-27T04:38:37+00:00 | 60,37084 | €-54,92 | -1,15 | STOP |
| Benchmark Bollinger mean reversion 1H | ETH | SHORT | 2026-07-27T04:23:38+00:00 | 1955,86734 | €-1,52 | -0,03 | STOP |
| Scanner Top 5 Long 1H | SHIB | LONG | 2026-07-27T02:53:36+00:00 | 0,00001 | €-54,36 | -1,03 | STOP |
| Scanner Top5 Btc Tp3 V1 | SHIB | LONG | 2026-07-27T02:53:36+00:00 | 0,00001 | €-47,76 | -1,03 | STOP |
| Scanner Top5 Btc Runner25 V1 | SHIB | LONG | 2026-07-27T02:53:36+00:00 | 0,00001 | €-48,90 | -1,03 | STOP |
| Scanner Top5 Btc Mfe V1 | PEPE | LONG | 2026-07-27T02:53:36+00:00 | 0,00000 | €0,16 | 0,20 | STOP |
| Scanner Top5 Btc Guard V1 | SHIB | LONG | 2026-07-27T02:53:36+00:00 | 0,00001 | €-49,77 | -1,03 | STOP |
| Scanner Top5 Btc Guard Btc Le3 V1 | SHIB | LONG | 2026-07-27T02:53:36+00:00 | 0,00001 | €-47,64 | -1,03 | STOP |
| Scanner Top5 Btc Btc Le3 V1 | SHIB | LONG | 2026-07-27T02:53:36+00:00 | 0,00001 | €-48,16 | -1,03 | STOP |
| Scanner Top 5 + forza BTC 1H | SHIB | LONG | 2026-07-27T02:53:36+00:00 | 0,00001 | €-50,14 | -1,03 | STOP |
| Forza relativa 1H V1 | SHIB | LONG | 2026-07-27T02:53:36+00:00 | 0,00001 | €-43,34 | -1,03 | STOP |

## Regole invarianti

- Nessuna martingala e nessuna mediazione automatica in perdita.
- Il target mensile riduce il rischio quando viene avvicinato o raggiunto; non lo aumenta mai.
- Il portafoglio principale e le simulazioni di confronto hanno contabilità separata.
- Commissioni, slippage e funding sono inclusi nella simulazione secondo i parametri configurati.
- Quando stop e target risultano toccati nella stessa candela, prevale lo stop salvo modifica esplicita della configurazione.
