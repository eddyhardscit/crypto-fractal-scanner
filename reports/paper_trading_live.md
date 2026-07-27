# Paper trading automatico KuCoin

Generato: 2026-07-27T00:09:22+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-07-27T00:08:24+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-07-27T00:08:24+00:00 | 2026-07-27T00:08:24+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-07-26T23:45:00+00:00 | 2026-07-26T23:45:00+00:00 | 8,5 min | 25,0 min | OK |
| 60m | 12 | 2026-07-26T23:00:00+00:00 | 2026-07-26T23:00:00+00:00 | 8,5 min | 45,0 min | OK |
| 240m | 12 | 2026-07-26T20:00:00+00:00 | 2026-07-26T20:00:00+00:00 | 8,5 min | 1,00 h | OK |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | PEPE | 60m | LONG | 7,12 | 4,50 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Trend — Side × Regime Guard | ETH | 60m | LONG | 6,35 | 5,00 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Eth Ema 4H | ETH | 240m | LONG | 5,97 | 5,00 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive — parziale 1R | ETH | 60m | LONG | 6,35 | 5,00 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Top 5 + BTC — BTC 2–3 | PEPE | 60m | LONG | 7,12 | 5,00 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V3 senza ESPORTS — Stress Guard | PEPE | 60m | LONG | 7,12 | 4,50 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Principale 4H | PEPE | 240m | LONG | 7,16 | 6,00 | 0,00 | READY | 8,5 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Principale 4H | EUL | 240m | LONG | 6,75 | 6,00 | 0,00 | READY | 8,5 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Principale 4H | SHIB | 240m | LONG | 8,25 | 6,00 | 0,00 | RISK_GATE | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro rischio/esecuzione: asset già aperto nel portafoglio. |
| Principale 4H | BANK | 240m | LONG | 7,75 | 6,00 | 0,00 | RISK_GATE | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro rischio/esecuzione: asset già aperto nel portafoglio. |
| Principale 4H | ETH | 240m | LONG | 5,97 | 6,00 | 0,03 | BELOW_SCORE | 8,5 min | D: n/a | W: n/a | peso 0 | Punteggio +5.97; soglia ±6.00; mancano 0.03 punti. |
| Ampia 4H | SHIB | 240m | LONG | 8,25 | 5,00 | 0,00 | READY | 8,5 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Ampia 4H | BANK | 240m | LONG | 7,75 | 5,00 | 0,00 | READY | 8,5 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Bilanciata 1H — LONG senza Range High Vol | SHIB | 60m | LONG | 7,75 | 5,00 | 0,00 | READY | 8,5 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Bilanciata 1H V2 | SHIB | 60m | LONG | 7,75 | 5,50 | 0,00 | READY | 8,5 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Forza relativa 1H V2 | SHIB | 60m | LONG | 7,75 | 5,50 | 0,00 | READY | 8,5 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Top 5 + BTC — solo MFE | SHIB | 60m | LONG | 7,75 | 5,00 | 0,00 | READY | 8,5 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Top 5 + BTC — BTC 2–3 | SHIB | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive — madre | SHIB | 60m | LONG | 7,75 | 5,00 | 0,00 | READY | 8,5 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Combo Adaptive — MFE Trail esistente | SHIB | 60m | LONG | 7,75 | 5,00 | 0,00 | READY | 8,5 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Combo Adaptive — parziale 1R | SHIB | 60m | LONG | 7,75 | 5,00 | 0,00 | READY | 8,5 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | SHIB | 60m | LONG | 7,75 | 5,00 | 0,00 | READY | 8,5 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Combo Adaptive — target pieno 3R | SHIB | 60m | LONG | 7,75 | 5,00 | 0,00 | READY | 8,5 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Master Adaptive Gb20 V1 | SHIB | 60m | LONG | 7,75 | 0,00 | 0,00 | READY | 8,5 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Master Adaptive GB20 — 50% a 0,75R | SHIB | 60m | LONG | 7,75 | 0,00 | 0,00 | READY | 8,5 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Ampia 4H | PEPE | 240m | LONG | 7,16 | 5,00 | 0,00 | READY | 8,5 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.780,57 | -2,19% | €-219,43 | €3.000,00 | -7,31% | 5 | 21 | 28,57% | 0,68 | 4,49% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 21 | 716 | CAMPIONE INSUFFICIENTE | 30 (mancano 9) |

- Trade del Principale 4H chiusi: **21**; win rate **28,57%**; profit factor **0,68**.
- Expectancy: **€-11,50** per trade; P&L netto: **€-241,45**; max drawdown: **4,49%**.
- Valutazione: **Servono altri eventi indipendenti prima di trarre conclusioni.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 5 | €9.780,57 | €1.075,94 | €3.227,82 | €146,89 | €23,30 |
| TEST | Bilanciata 1H V3 Filtered | 7 | €10.604,75 | €706,14 | €2.118,41 | €212,00 | €24,76 |
| TEST | Scanner Top 5 Long 1H | 3 | €10.576,68 | €514,15 | €1.028,29 | €109,00 | €0,00 |
| TEST | Rapida V1 — no HIGH + score <7,5 | 5 | €10.492,49 | €803,29 | €2.409,86 | €206,74 | €-21,89 |
| TEST | Benchmark Donchian breakout 1H | 5 | €10.487,46 | €3.557,51 | €7.115,02 | €209,83 | €19,72 |
| TEST | Rapida V3 — score <7,5 | 5 | €10.412,66 | €861,02 | €2.583,07 | €208,63 | €-3,58 |
| TEST | Rapida V1 — score 6–7,5 | 5 | €10.374,75 | €729,46 | €2.188,39 | €157,20 | €41,71 |
| TEST | Rapida V3 NoHigh — Regime Guard | 5 | €10.373,10 | €680,76 | €2.042,29 | €156,17 | €17,50 |
| TEST | Bilanciata 1H V1 | 5 | €10.359,71 | €1.638,91 | €4.916,72 | €155,31 | €-0,39 |
| TEST | Scanner Top 5 + forza BTC 1H | 4 | €10.352,69 | €1.371,70 | €2.743,40 | €158,28 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 5 | €10.350,94 | €952,35 | €2.857,04 | €155,49 | €47,58 |
| TEST | Rapida score 6–7,5 — Range Only | 4 | €10.335,26 | €961,67 | €2.885,01 | €205,93 | €39,24 |
| TEST | Rapida score 6–7,5 — Cost Aware | 5 | €10.334,95 | €726,75 | €2.180,24 | €156,66 | €41,49 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 5 | €10.271,77 | €2.037,60 | €6.112,81 | €154,28 | €-11,29 |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 5 | €10.265,84 | €1.056,26 | €3.168,79 | €154,13 | €-2,25 |
| TEST | Rapida V3 NoHigh — Range Only | 4 | €10.262,94 | €716,35 | €2.149,06 | €204,77 | €-10,00 |
| TEST | Rapida V3 senza ESPORTS — MFE Lock | 6 | €10.249,48 | €2.147,55 | €6.442,65 | €202,54 | €-24,02 |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 5 | €10.237,33 | €743,67 | €2.231,02 | €106,53 | €123,09 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 5 | €10.220,49 | €905,14 | €2.715,43 | €153,15 | €40,06 |
| TEST | Rapida score 6–7,5 — senza Trend Up | 4 | €10.217,95 | €837,63 | €2.512,89 | €204,36 | €-4,22 |
| TEST | Combo Adaptive — Side × Regime Guard | 5 | €10.217,11 | €1.125,88 | €2.251,76 | €203,76 | €36,36 |
| TEST | Combo Adaptive — madre | 4 | €10.203,22 | €2.162,62 | €4.325,23 | €204,07 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 6 | €10.191,02 | €739,52 | €2.218,56 | €153,19 | €40,78 |
| TEST | Rapida V3 senza ESPORTS — Long Only | 5 | €10.185,93 | €753,15 | €2.259,44 | €153,31 | €17,53 |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 5 | €10.179,80 | €937,68 | €2.813,03 | €153,79 | €62,43 |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 4 | €10.171,61 | €911,20 | €2.733,59 | €203,12 | €15,24 |
| TEST | Rapida 1H V3 Filtered — madre | 5 | €10.170,26 | €2.715,21 | €8.145,64 | €203,41 | €11,55 |
| TEST | Btc Bollinger 1H | 0 | €10.168,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Trend — Side × Regime Guard | 7 | €10.166,68 | €874,11 | €1.748,21 | €153,94 | €53,42 |
| TEST | Rapida V1 — Long + BTC 1–3 + score <7,5 | 5 | €10.157,86 | €2.854,28 | €8.562,85 | €153,87 | €31,79 |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 4 | €10.148,88 | €4.340,07 | €13.020,21 | €203,02 | €-31,10 |
| TEST | FAST NoHigh <7,5 · SHORT only | 5 | €10.148,69 | €1.398,08 | €4.194,24 | €153,25 | €46,02 |
| TEST | MAIN — Dynamic Asset Selector | 1 | €10.142,99 | €140,56 | €421,69 | €50,60 | €0,00 |
| TEST | Combo Mean Reversion | 1 | €10.138,28 | €225,46 | €450,91 | €50,00 | €0,00 |
| TEST | Rapida V3 senza ESPORTS — Stress Guard | 4 | €10.120,99 | €4.328,14 | €12.984,42 | €202,46 | €-31,01 |
| TEST | Bilanciata 1H V2 | 6 | €10.115,83 | €1.688,01 | €5.064,04 | €152,55 | €22,73 |
| TEST | Rapida V1 — senza PEPE | 5 | €10.111,98 | €2.699,71 | €8.099,14 | €202,24 | €11,49 |
| TEST | Sol Donchian 1H | 0 | €10.092,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Ema 1H | 0 | €10.091,86 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | MAIN — Side × Regime Guard | 2 | €10.088,26 | €280,59 | €841,77 | €50,60 | €0,00 |
| TEST | Sol Bollinger 4H | 0 | €10.086,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 4H | 0 | €10.084,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — 75% a 2R + runner 25% a 3R | 5 | €10.073,28 | €2.266,98 | €4.533,96 | €201,30 | €0,00 |
| TEST | Top 5 + BTC — 75% a 2,2R + runner 3R | 4 | €10.069,33 | €1.353,72 | €2.707,43 | €153,82 | €0,00 |
| TEST | Combo Adaptive — Quality7 | 5 | €10.065,84 | €2.209,40 | €4.418,81 | €201,32 | €0,07 |
| TEST | Rapida 1H V2 | 4 | €10.053,39 | €4.620,29 | €13.860,88 | €201,21 | €-36,56 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 5 | €10.048,93 | €927,38 | €2.782,14 | €150,54 | €41,55 |
| TEST | Top 5 + BTC — target pieno 3R | 4 | €10.044,11 | €1.368,50 | €2.737,00 | €154,42 | €0,00 |
| TEST | Rapida V3 — Long + no HIGH + score <7,5 | 5 | €10.031,27 | €1.030,80 | €3.092,40 | €200,73 | €20,29 |
| TEST | Eth Bollinger 1H | 1 | €10.030,16 | €1.391,03 | €4.173,10 | €50,08 | €17,22 |
| TEST | Bilanciata V3 · LONG only | 5 | €10.028,32 | €1.377,13 | €4.131,39 | €151,02 | €73,97 |
| TEST | Rapida V1 — target pieno 2R | 6 | €10.026,44 | €2.057,79 | €6.173,38 | €200,85 | €12,54 |
| TEST | Btc Adaptive 1H | 0 | €10.013,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €10.010,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 0 | €10.002,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · prudente · 5x | 1 | €10.002,09 | €337,23 | €1.686,15 | €10,00 | €2,13 |
| TEST | Scalp RSI Short 85 · €50 · 15x | 1 | €10.001,92 | €50,00 | €750,00 | €4,45 | €0,95 |
| TEST | Scalp RSI Long 25 · €50 · 15x | 0 | €10.001,47 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €10 · 15x | 1 | €10.000,38 | €10,00 | €150,00 | €0,89 | €0,19 |
| TEST | Scalp RSI Long 25 · €10 · 15x | 0 | €10.000,29 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Continuation V1 | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €10 · 15x | 0 | €9.999,70 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €10 · 15x | 0 | €9.998,96 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Donchian 1H | 0 | €9.998,75 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €50 · 15x | 0 | €9.998,52 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €10 · 15x | 0 | €9.998,50 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H — SHORT Trend Down stretto | 0 | €9.995,87 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €50 · 15x | 0 | €9.994,81 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €50 · 15x | 0 | €9.992,50 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · prudente · 5x | 0 | €9.990,24 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 — qualità completa + profit lock | 5 | €9.988,44 | €2.083,00 | €6.248,99 | €150,51 | €11,95 |
| TEST | Scalp RSI Long 15 · prudente · 5x | 0 | €9.988,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · prudente · 5x | 0 | €9.983,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 1H | 0 | €9.980,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 1H | 0 | €9.977,09 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 0 | €9.976,99 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — Trend/Transition | 2 | €9.975,22 | €964,46 | €1.928,92 | €98,78 | €0,00 |
| TEST | Rapida 1H V1 — madre | 2 | €9.974,17 | €1.645,02 | €4.935,06 | €99,89 | €0,00 |
| TEST | Top 5 + BTC — Guard + BTC≤3 | 4 | €9.971,62 | €1.302,99 | €2.605,98 | €153,07 | €0,66 |
| TEST | Forza relativa 1H V2 | 5 | €9.966,00 | €2.775,20 | €5.550,40 | €199,21 | €28,21 |
| TEST | Combo Adaptive — Long Only | 5 | €9.964,84 | €2.701,47 | €5.402,94 | €199,28 | €0,75 |
| TEST | Rapida V3 — senza ESPORTS | 5 | €9.963,13 | €2.659,44 | €7.978,31 | €199,27 | €11,33 |
| TEST | Benchmark trend following EMA 1H | 5 | €9.962,86 | €1.028,81 | €2.057,63 | €199,83 | €-0,60 |
| TEST | Benchmark Bollinger mean reversion 1H | 3 | €9.959,21 | €5.960,33 | €11.920,66 | €143,05 | €28,24 |
| TEST | Scanner Bottom5 Short Profit Lock V1 | 3 | €9.952,41 | €1.371,54 | €2.743,08 | €99,39 | €74,40 |
| TEST | Btc Ema 4H | 0 | €9.950,68 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 4H | 0 | €9.950,68 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 4H | 0 | €9.949,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Ema 4H | 1 | €9.945,46 | €1.036,30 | €2.072,59 | €49,74 | €-0,41 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.944,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Top 5 + BTC — BTC≤3 | 4 | €9.942,96 | €1.340,87 | €2.681,73 | €152,01 | €0,00 |
| TEST | Sol Adaptive 4H | 1 | €9.937,14 | €761,04 | €1.522,08 | €49,74 | €-10,44 |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | 3 | €9.936,71 | €1.372,84 | €2.745,68 | €149,15 | €13,07 |
| TEST | Rapida V3 — no volatilità HIGH | 5 | €9.936,20 | €2.652,25 | €7.956,75 | €198,73 | €11,30 |
| TEST | Sol Donchian 4H | 1 | €9.935,97 | €830,21 | €1.660,43 | €49,74 | €-11,39 |
| TEST | Combo Scanner | 4 | €9.930,95 | €1.299,67 | €2.599,35 | €151,09 | €0,00 |
| TEST | Combo Adaptive — target pieno 3R | 4 | €9.929,58 | €2.226,41 | €4.452,81 | €198,61 | €0,00 |
| TEST | Top 5 + BTC — BTC 2–3 | 4 | €9.928,83 | €2.598,90 | €5.197,81 | €198,61 | €-0,60 |
| TEST | Ampia 4H | 4 | €9.927,52 | €1.734,53 | €3.469,06 | €199,10 | €-17,85 |
| TEST | Combo Adaptive — Quality7 + Regime + parziale 1R | 1 | €9.916,34 | €864,27 | €1.728,54 | €49,61 | €0,00 |
| TEST | Sol Ema 4H | 1 | €9.914,41 | €862,58 | €1.725,17 | €49,74 | €-32,82 |
| TEST | Btc Ema 1H | 0 | €9.911,86 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Donchian 1H | 1 | €9.907,44 | €1.292,62 | €3.877,86 | €49,64 | €-17,55 |
| TEST | Sol Bollinger 1H | 0 | €9.901,25 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Bollinger 1H | 0 | €9.888,87 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive GB20 — Breakeven 0,5R | 3 | €9.883,75 | €1.927,00 | €3.854,00 | €151,25 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 4 | €9.879,59 | €673,76 | €2.021,28 | €147,70 | €16,77 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 4 | €9.879,59 | €673,76 | €2.021,28 | €147,70 | €16,77 |
| TEST | Bilanciata 1H — LONG senza Range High Vol | 4 | €9.870,73 | €1.411,99 | €4.235,97 | €197,36 | €3,40 |
| TEST | Scanner Top10 Long | 4 | €9.863,83 | €1.807,73 | €3.615,45 | €151,67 | €10,45 |
| TEST | Scanner Top15 Long | 4 | €9.863,83 | €1.807,73 | €3.615,45 | €151,67 | €10,45 |
| TEST | Scanner Top20 Long | 4 | €9.863,83 | €1.807,73 | €3.615,45 | €151,67 | €10,45 |
| TEST | Master Adaptive GB20 — 50% a 0,75R | 4 | €9.862,49 | €2.097,17 | €4.194,35 | €197,11 | €7,47 |
| TEST | Combo Adaptive — Quality7 + Regime | 1 | €9.855,64 | €864,27 | €1.728,54 | €49,61 | €0,00 |
| TEST | Master Adaptive GB20 — Loss Cap 0,75R | 3 | €9.846,34 | €2.432,43 | €4.864,86 | €150,32 | €0,00 |
| TEST | Eth Adaptive 1H | 1 | €9.836,36 | €1.140,50 | €3.421,49 | €49,27 | €-15,48 |
| TEST | Sol Adaptive 1H | 0 | €9.835,19 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom10 Short | 3 | €9.825,21 | €2.159,38 | €4.318,77 | €98,62 | €73,45 |
| TEST | Scanner Bottom15 Short | 3 | €9.825,21 | €2.159,38 | €4.318,77 | €98,62 | €73,45 |
| TEST | Scanner Bottom20 Short | 3 | €9.825,21 | €2.159,38 | €4.318,77 | €98,62 | €73,45 |
| TEST | Rapida V3 — Long Only | 4 | €9.823,29 | €955,14 | €2.865,42 | €146,81 | €62,94 |
| TEST | Top 5 + BTC — Guard | 3 | €9.800,91 | €1.166,95 | €2.333,91 | €147,61 | €0,00 |
| TEST | Top 5 + BTC — solo MFE | 5 | €9.791,96 | €2.615,64 | €5.231,28 | €195,32 | €-14,25 |
| TEST | Global Confluence puro 1H | 0 | €9.790,66 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom 5 Short 1H | 3 | €9.778,76 | €1.786,26 | €3.572,51 | €48,61 | €73,16 |
| TEST | Eth Ema 1H | 1 | €9.764,35 | €1.132,15 | €3.396,44 | €48,91 | €-15,37 |
| TEST | Master Adaptive Gb20 V1 | 4 | €9.727,40 | €2.665,83 | €5.331,66 | €194,75 | €-17,36 |
| TEST | Master Adaptive Expanded V1 | 4 | €9.722,80 | €1.276,66 | €2.553,32 | €148,84 | €0,00 |
| TEST | Master Adaptive No Alt V1 | 5 | €9.713,26 | €1.518,39 | €3.036,78 | €194,60 | €-16,54 |
| TEST | Combo Adaptive — parziale 1R | 6 | €9.702,62 | €2.199,86 | €4.399,72 | €171,55 | €20,18 |
| TEST | Master Adaptive Runner25 V1 | 4 | €9.688,11 | €1.263,03 | €2.526,06 | €148,15 | €0,00 |
| TEST | Master Adaptive V1 | 4 | €9.678,90 | €1.263,75 | €2.527,51 | €148,19 | €0,00 |
| TEST | Top 5 + BTC — Guard + BTC≤3 + MFE | 4 | €9.678,61 | €1.697,46 | €3.394,92 | €144,66 | €48,11 |
| TEST | Forza relativa 1H V1 | 4 | €9.636,56 | €1.401,14 | €2.802,28 | €150,57 | €0,00 |
| TEST | Combo Trend | 4 | €9.572,47 | €1.541,40 | €3.082,80 | €191,83 | €-6,43 |
| TEST | Top 5 + BTC — Guard + MFE | 4 | €9.568,94 | €1.571,22 | €3.142,43 | €143,03 | €47,46 |
| TEST | Master Adaptive Strict3 V1 | 4 | €9.549,20 | €2.668,05 | €5.336,10 | €191,31 | €-16,14 |
| TEST | Combo Adaptive — MFE Trail esistente | 4 | €9.521,88 | €2.034,13 | €4.068,27 | €190,44 | €0,00 |

**Importante:** ogni riga è un conto virtuale separato da €10.000. I margini dei diversi portafogli non vanno sommati come se appartenessero a un unico conto.

**Rischio agli stop** è la perdita residua stimata usando gli stop correnti. Se uno stop protegge già un profitto, il rischio residuo viene mostrato come €0.

## Legenda portafogli

| Tipo | Nome leggibile | Metodo | Significato |
| --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | Confluenza trend | Riferimento principale: confluenza di trend su 4 ore, soglia più selettiva. |
| TEST | Bilanciata 1H V1 | Confluenza trend | Versione originale V1 a 1 ora basata sulla confluenza di trend. |
| TEST | Bilanciata 1H — LONG senza Range High Vol | Confluenza trend | Solo Long della Bilanciata 1H; esclude esattamente RANGE_HIGH_VOL. |
| TEST | Bilanciata 1H — SHORT Trend Down stretto | Confluenza trend | Solo Short con regime esatto TREND_DOWN, BTC trend score ≤ -2 e score minimo 6. |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | Versione V2 selettiva: esclude i regimi storicamente peggiori, richiede trend e ritorni coerenti e limita i segnali correlati. |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | Versione V3 derivata dalla V1: accetta soltanto score assoluti da 6,0 a meno di 7,5, cioè la fascia BUONA risultata migliore nel confronto Paper vs Shadow. |
| TEST | Rapida 1H V1 — madre | Momentum / breakout | Madre Rapida 1H V1 originale, invariata. |
| TEST | Rapida V1 — score 6–7,5 | Momentum / breakout | Accetta soltanto score assoluti da 6,0 a meno di 7,5. |
| TEST | Rapida score 6–7,5 — senza Trend Up | Momentum / breakout | Mantiene score 6–7,5 ma esclude TREND_UP e TREND_UP_HIGH_VOL. |
| TEST | Rapida score 6–7,5 — Range Only | Momentum / breakout | Opera solo nei regimi esatti RANGE e RANGE_LOW_VOL. |
| TEST | Rapida score 6–7,5 — Cost Aware | Momentum / breakout | Richiede target lordo almeno 2 volte i costi round-trip stimati e slippage massimo 2 bps. |
| TEST | Rapida V1 — no HIGH + score <7,5 | Momentum / breakout | Esclude volatilità HIGH e score assoluti almeno 7,5. |
| TEST | Rapida V1 — Long + BTC 1–3 + score <7,5 | Momentum / breakout | Solo Long, BTC trend score 1–3 e score assoluto sotto 7,5. |
| TEST | Rapida V1 — senza PEPE | Momentum / breakout | Stessa madre, ma esclude PEPE. |
| TEST | Rapida V1 — target pieno 2R | Momentum / breakout | Stessi ingressi della madre con target portato da 1,5R a 2R. |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | Versione V2 selettiva: richiede vero breakout, volume, ADX, trend tecnico coerente e limita i segnali correlati. |
| TEST | Rapida 1H V3 Filtered — madre | Momentum / breakout V3 Filtered | Madre Rapida 1H V3 Filtered originale, invariata. |
| TEST | Rapida V3 — score <7,5 | Momentum / breakout V3 Filtered | Mantiene il filtro V3 ed esclude score assoluti almeno 7,5. |
| TEST | Rapida V3 — no volatilità HIGH | Momentum / breakout V3 Filtered | Mantiene il filtro V3 ed esclude volatilità HIGH. |
| TEST | Rapida V3 — Long Only | Momentum / breakout V3 Filtered | Mantiene il filtro V3 e accetta soltanto segnali Long. |
| TEST | Rapida V3 — Long + no HIGH + score <7,5 | Momentum / breakout V3 Filtered | Combina Long Only, esclusione HIGH e score sotto 7,5. |
| TEST | Rapida V3 — senza ESPORTS | Momentum / breakout V3 Filtered | Mantiene il filtro V3 ed esclude ESPORTS. |
| TEST | Rapida V3 senza ESPORTS — Long Only | Momentum / breakout V3 Filtered | Replica la variante senza ESPORTS accettando soltanto segnali Long. |
| TEST | Rapida V3 senza ESPORTS — MFE Lock | Momentum / breakout V3 Filtered | Aggiunge breakeven a 0,75R, lock 0,25R da 1R e giveback dinamico dopo 1,25R. |
| TEST | Rapida V3 senza ESPORTS — Stress Guard | Momentum / breakout V3 Filtered | Esclude regimi e volatilità HIGH, ATR oltre 3% e asset con slippage stimato oltre 2 bps. |
| TEST | Rapida V3 — qualità completa + profit lock | Momentum / breakout V3 Filtered | Combina i filtri di qualità e protegge +0,25R dopo il raggiungimento di +1R, dalla candela successiva. |
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
| TEST | Scanner Top10 Long | Scanner Top10 Long | Portafoglio sperimentale separato. |
| TEST | Scanner Bottom10 Short | Scanner Bottom10 Short | Portafoglio sperimentale separato. |
| TEST | Scanner Top15 Long | Scanner Top15 Long | Portafoglio sperimentale separato. |
| TEST | Scanner Bottom15 Short | Scanner Bottom15 Short | Portafoglio sperimentale separato. |
| TEST | Scanner Top20 Long | Scanner Top20 Long | Portafoglio sperimentale separato. |
| TEST | Scanner Bottom20 Short | Scanner Bottom20 Short | Portafoglio sperimentale separato. |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | Top 5 live KuCoin con conferma tecnica e forza relativa positiva contro Bitcoin. |
| TEST | Top 5 + BTC — solo MFE | Scanner Top 5 + forza BTC | Stessi ingressi della madre; protegge progressivamente il profitto tramite MFE. |
| TEST | Top 5 + BTC — Guard | Scanner Top 5 + forza BTC | Scarta score sotto 7 fuori dai regimi Range. |
| TEST | Top 5 + BTC — BTC≤3 | Scanner Top 5 + forza BTC | Accetta soltanto contesti con BTC trend score non superiore a 3. |
| TEST | Top 5 + BTC — BTC 2–3 | Scanner Top 5 + forza BTC | Accetta soltanto BTC trend score compreso tra 2 e 3. |
| TEST | Top 5 + BTC — Guard + MFE | Scanner Top 5 + forza BTC | Combina filtro score/regime e protezione MFE. |
| TEST | Top 5 + BTC — Guard + BTC≤3 | Scanner Top 5 + forza BTC | Combina filtro score/regime e BTC trend score ≤3. |
| TEST | Top 5 + BTC — Guard + BTC≤3 + MFE | Scanner Top 5 + forza BTC | Combina Guard, BTC trend score ≤3 e protezione MFE. |
| TEST | Top 5 + BTC — 75% a 2,2R + runner 3R | Scanner Top 5 + forza BTC | Chiude il 75% a 2,2R e lascia il 25% verso 3R con profit lock a 2R. |
| TEST | Top 5 + BTC — target pieno 3R | Scanner Top 5 + forza BTC | Mantiene il 100% della posizione fino al target 3R. |
| TEST | Global Confluence puro 1H | Global Confluence puro | Opera soltanto quando Global Confluence, dati exchange e struttura tecnica sono allineati. |
| TEST | Combo Trend | Combo Trend | Portafoglio sperimentale separato. |
| TEST | Combo Mean Reversion | Combo Mean Reversion | Portafoglio sperimentale separato. |
| TEST | Combo Scanner | Combo Scanner | Portafoglio sperimentale separato. |
| TEST | Combo Adaptive — madre | Combo Adaptive | Madre Combo Adaptive originale, invariata. |
| TEST | Combo Adaptive — MFE Trail esistente | Combo Adaptive | Variante MFE trailing già esistente; resta come confronto storico separato. |
| TEST | Combo Adaptive — Quality7 | Combo Adaptive | Accetta soltanto segnali con score assoluto almeno 7. |
| TEST | Combo Adaptive — Trend/Transition | Combo Adaptive | Opera soltanto nei regimi TREND_UP e TRANSITION. |
| TEST | Combo Adaptive — Quality7 + Regime | Combo Adaptive | Combina score assoluto almeno 7 con regimi Trend/Transition. |
| TEST | Combo Adaptive — Long Only | Combo Adaptive | Accetta esclusivamente segnali Long. |
| TEST | Combo Adaptive — parziale 1R | Combo Adaptive | Realizza il 50% della posizione a +1R e lascia correre il residuo. |
| TEST | Combo Adaptive — Quality7 + Regime + parziale 1R | Combo Adaptive | Combina qualità, regime e presa parziale del 50% a +1R. |
| TEST | Combo Adaptive — 75% a 2R + runner 25% a 3R | Combo Adaptive | Chiude il 75% a 2R e lascia il 25% verso 3R con profit lock a 1,8R. |
| TEST | Combo Adaptive — target pieno 3R | Combo Adaptive | Mantiene il 100% della posizione fino al target 3R. |
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
| TEST | Master Adaptive V1 | Master Adaptive Consensus | Portafoglio sperimentale separato. |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | Portafoglio sperimentale separato. |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | Portafoglio sperimentale separato. |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | Portafoglio sperimentale separato. |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | Portafoglio sperimentale separato. |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | Portafoglio sperimentale separato. |
| TEST | Combo Adaptive — Side × Regime Guard | Combo Adaptive | Blocca soltanto i Long nei regimi ALT_ROTATION_DOWN, TREND_UP_HIGH_VOL e RANGE_HIGH_VOL; gli Short restano un controllo separato. Richiede target/costi almeno 2x. |
| TEST | Master Adaptive GB20 — Breakeven 0,5R | Master Adaptive Consensus | Stessa entrata GB20; dalla candela successiva porta lo stop a breakeven dopo un MFE di almeno +0,5R. |
| TEST | Master Adaptive GB20 — 50% a 0,75R | Master Adaptive Consensus | Stessa entrata GB20; realizza il 50% a +0,75R e protegge il residuo a breakeven dalla candela successiva. |
| TEST | Master Adaptive GB20 — Loss Cap 0,75R | Master Adaptive Consensus | Stessa entrata e target monetario teorico della GB20; stop iniziale ridotto al 75% della distanza originaria e reward/risk compensato. |
| TEST | Rapida V3 NoHigh — Range Only | Momentum / breakout V3 Filtered | Replica NoHigh ma accetta esclusivamente RANGE e RANGE_LOW_VOL, con filtro cost-aware. |
| TEST | Rapida V3 NoHigh — Regime Guard | Momentum / breakout V3 Filtered | Replica NoHigh; blocca i Long in TREND_UP, TREND_UP_HIGH_VOL e ALT_ROTATION_DOWN, mantenendo gli Short come campione separato. |
| TEST | MAIN — Side × Regime Guard | Confluenza trend | Replica MAIN e blocca soltanto LONG in ALT_ROTATION_UP e SHORT in RANGE; mantiene gli altri segmenti come controllo prospettico e applica un filtro cost-aware. |
| TEST | MAIN — Dynamic Asset Selector | Confluenza trend | Replica MAIN Side × Regime Guard e usa un ranking adattivo degli asset: storico, recente, regime BTC, alpha residuo, esecuzione, stabilità, liquidità, esplorazione e isteresi. AKE/BANK/LAB sono riferimenti storici, non una whitelist. |
| TEST | Combo Trend — Side × Regime Guard | Combo Trend | Replica Combo Trend; blocca LONG in ALT_ROTATION_DOWN e RANGE_HIGH_VOL e SHORT in RANGE. Mantiene LONG in RANGE/TRANSITION/TREND_UP e SHORT in TRANSITION come test prospettico. |
| TEST | FAST NoHigh <7,5 · SHORT only | Momentum / breakout | Challenger forward isolato: copia soltanto i segnali SHORT della variante FAST NoHigh score <7,5. Nessuna promozione automatica. |
| TEST | Bilanciata V3 · LONG only | Confluenza trend V3 Filtered | Challenger forward isolato: copia soltanto i segnali LONG della Bilanciata V3. Il regime viene registrato point-in-time, ma non viene usato come filtro finché il campione non è sufficiente. |
| TEST | Scanner Bottom5 Short Profit Lock V1 | Scanner Bottom 5 Short | Portafoglio sperimentale separato. |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | Scanner Bottom 5 Short | Portafoglio sperimentale separato. |
| TEST | Scanner Bottom5 Short Continuation V1 | Scanner Bottom5 Short Continuation | Portafoglio sperimentale separato. |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | Momentum / breakout V3 Filtered | Portafoglio sperimentale separato. |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | Momentum / breakout V3 Filtered | Portafoglio sperimentale separato. |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | Momentum / breakout V3 Filtered | Portafoglio sperimentale separato. |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | Momentum / breakout V3 Filtered | Portafoglio sperimentale separato. |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | Momentum / breakout V3 Filtered | Portafoglio sperimentale separato. |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | Momentum / breakout V3 Filtered | Portafoglio sperimentale separato. |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | Momentum / breakout V3 Filtered | Portafoglio sperimentale separato. |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | Momentum / breakout V3 Filtered | Portafoglio sperimentale separato. |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | Momentum / breakout V3 Filtered | Portafoglio sperimentale separato. |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | Momentum / breakout V3 Filtered | Portafoglio sperimentale separato. |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | Momentum / breakout V3 Filtered | Portafoglio sperimentale separato. |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | Momentum / breakout V3 Filtered | Portafoglio sperimentale separato. |

## Confronto risultati

| Tipo | Portafoglio | Strategia | Equity | P&L chiuso | Trade | Eventi indip. | Win rate | PF | Expectancy | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | Confluenza trend | €9.780,57 | €-241,45 | 21 | 21 | 28,57% | 0,68 | €-11,50 | 4,49% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €10.604,75 | €581,26 | 46 | 46 | 43,48% | 1,62 | €12,64 | 2,20% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.576,68 | €577,13 | 36 | 36 | 52,78% | 1,72 | €16,03 | 2,75% |
| TEST | Rapida V1 — no HIGH + score <7,5 | Momentum / breakout | €10.492,49 | €511,94 | 50 | 50 | 50,00% | 1,54 | €10,24 | 2,83% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €10.487,46 | €472,58 | 26 | 26 | 53,85% | 1,89 | €18,18 | 2,12% |
| TEST | Rapida V3 — score <7,5 | Momentum / breakout V3 Filtered | €10.412,66 | €417,96 | 45 | 45 | 48,89% | 1,55 | €9,29 | 2,49% |
| TEST | Rapida V1 — score 6–7,5 | Momentum / breakout | €10.374,75 | €334,68 | 48 | 48 | 45,83% | 1,36 | €6,97 | 2,49% |
| TEST | Rapida V3 NoHigh — Regime Guard | Momentum / breakout V3 Filtered | €10.373,10 | €353,20 | 14 | 14 | 71,43% | 4,13 | €25,23 | 1,39% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €10.359,71 | €366,36 | 47 | 47 | 51,06% | 1,39 | €7,79 | 2,76% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €10.352,69 | €354,08 | 28 | 28 | 50,00% | 1,54 | €12,65 | 2,74% |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | Momentum / breakout V3 Filtered | €10.350,94 | €305,23 | 10 | 10 | 70,00% | 6,04 | €30,52 | 1,23% |
| TEST | Rapida score 6–7,5 — Range Only | Momentum / breakout | €10.335,26 | €297,12 | 9 | 9 | 66,67% | 3,17 | €33,01 | 2,28% |
| TEST | Rapida score 6–7,5 — Cost Aware | Momentum / breakout | €10.334,95 | €294,48 | 12 | 12 | 66,67% | 2,34 | €24,54 | 1,95% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | Momentum / breakout V3 Filtered | €10.271,77 | €282,30 | 10 | 10 | 60,00% | 3,16 | €28,23 | 1,34% |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | Momentum / breakout V3 Filtered | €10.265,84 | €269,99 | 15 | 15 | 66,67% | 2,64 | €18,00 | 1,08% |
| TEST | Rapida V3 NoHigh — Range Only | Momentum / breakout V3 Filtered | €10.262,94 | €274,29 | 8 | 8 | 75,00% | 3,50 | €34,29 | 1,78% |
| TEST | Rapida V3 senza ESPORTS — MFE Lock | Momentum / breakout V3 Filtered | €10.249,48 | €277,80 | 22 | 22 | 59,09% | 2,15 | €12,63 | 2,05% |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | Momentum / breakout V3 Filtered | €10.237,33 | €116,52 | 11 | 11 | 54,55% | 2,91 | €10,59 | 1,01% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | Momentum / breakout V3 Filtered | €10.220,49 | €181,74 | 10 | 10 | 50,00% | 2,35 | €18,17 | 1,52% |
| TEST | Rapida score 6–7,5 — senza Trend Up | Momentum / breakout | €10.217,95 | €223,23 | 14 | 14 | 64,29% | 1,91 | €15,94 | 2,01% |
| TEST | Combo Adaptive — Side × Regime Guard | Combo Adaptive | €10.217,11 | €182,38 | 10 | 10 | 80,00% | 2,69 | €18,24 | 1,41% |
| TEST | Combo Adaptive — madre | Combo Adaptive | €10.203,22 | €206,62 | 25 | 25 | 48,00% | 1,52 | €8,26 | 1,49% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | Momentum / breakout V3 Filtered | €10.191,02 | €151,90 | 10 | 10 | 60,00% | 2,96 | €15,19 | 2,01% |
| TEST | Rapida V3 senza ESPORTS — Long Only | Momentum / breakout V3 Filtered | €10.185,93 | €165,76 | 15 | 15 | 60,00% | 1,74 | €11,05 | 1,32% |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | Momentum / breakout V3 Filtered | €10.179,80 | €119,15 | 13 | 13 | 46,15% | 1,51 | €9,17 | 1,60% |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | Momentum / breakout V3 Filtered | €10.171,61 | €158,01 | 4 | 4 | 75,00% | 414,09 | €39,50 | 0,78% |
| TEST | Rapida 1H V3 Filtered — madre | Momentum / breakout V3 Filtered | €10.170,26 | €163,64 | 74 | 74 | 39,19% | 1,11 | €2,21 | 2,89% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.168,12 | €168,12 | 3 | 3 | 100,00% | ∞ | €56,04 | 0,54% |
| TEST | Combo Trend — Side × Regime Guard | Combo Trend | €10.166,68 | €114,69 | 10 | 10 | 60,00% | 1,69 | €11,47 | 1,32% |
| TEST | Rapida V1 — Long + BTC 1–3 + score <7,5 | Momentum / breakout | €10.157,86 | €131,21 | 15 | 15 | 40,00% | 1,55 | €8,75 | 1,92% |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | Momentum / breakout V3 Filtered | €10.148,88 | €187,79 | 6 | 6 | 66,67% | 4,44 | €31,30 | 0,73% |
| TEST | FAST NoHigh <7,5 · SHORT only | Momentum / breakout | €10.148,69 | €105,34 | 15 | 15 | 60,00% | 1,44 | €7,02 | 1,76% |
| TEST | MAIN — Dynamic Asset Selector | Confluenza trend | €10.142,99 | €142,72 | 4 | 4 | 50,00% | 3,55 | €35,68 | 1,03% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €10.138,28 | €138,67 | 16 | 16 | 43,75% | 1,36 | €8,67 | 2,31% |
| TEST | Rapida V3 senza ESPORTS — Stress Guard | Momentum / breakout V3 Filtered | €10.120,99 | €159,79 | 11 | 11 | 54,55% | 1,73 | €14,53 | 1,29% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €10.115,83 | €95,91 | 34 | 32 | 50,00% | 1,13 | €2,82 | 2,75% |
| TEST | Rapida V1 — senza PEPE | Momentum / breakout | €10.111,98 | €105,40 | 42 | 42 | 42,86% | 1,12 | €2,51 | 2,15% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €10.092,12 | €92,12 | 3 | 3 | 66,67% | 21,53 | €30,71 | 0,79% |
| TEST | Doge Ema 1H | Trend following EMA | €10.091,86 | €91,86 | 8 | 8 | 62,50% | 1,55 | €11,48 | 1,36% |
| TEST | MAIN — Side × Regime Guard | Confluenza trend | €10.088,26 | €88,60 | 5 | 5 | 40,00% | 1,81 | €17,72 | 1,48% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €10.086,98 | €86,98 | 1 | 1 | 100,00% | ∞ | €86,98 | 0,40% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.084,12 | €84,12 | 1 | 1 | 100,00% | ∞ | €84,12 | 0,30% |
| TEST | Combo Adaptive — 75% a 2R + runner 25% a 3R | Combo Adaptive | €10.073,28 | €76,55 | 22 | 22 | 45,45% | 1,17 | €3,48 | 2,12% |
| TEST | Top 5 + BTC — 75% a 2,2R + runner 3R | Scanner Top 5 + forza BTC | €10.069,33 | €70,71 | 15 | 15 | 53,33% | 1,17 | €4,71 | 2,75% |
| TEST | Combo Adaptive — Quality7 | Combo Adaptive | €10.065,84 | €68,97 | 16 | 16 | 43,75% | 1,38 | €4,31 | 1,51% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €10.053,39 | €98,27 | 13 | 12 | 53,85% | 1,39 | €7,56 | 1,69% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | Momentum / breakout V3 Filtered | €10.048,93 | €5,64 | 11 | 11 | 54,55% | 1,02 | €0,51 | 1,92% |
| TEST | Top 5 + BTC — target pieno 3R | Scanner Top 5 + forza BTC | €10.044,11 | €45,50 | 11 | 11 | 54,55% | 1,11 | €4,14 | 2,73% |
| TEST | Rapida V3 — Long + no HIGH + score <7,5 | Momentum / breakout V3 Filtered | €10.031,27 | €12,40 | 35 | 35 | 42,86% | 1,02 | €0,35 | 2,86% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €10.030,16 | €15,45 | 1 | 1 | 100,00% | ∞ | €15,45 | 0,51% |
| TEST | Bilanciata V3 · LONG only | Confluenza trend V3 Filtered | €10.028,32 | €-43,30 | 7 | 7 | 28,57% | 0,74 | €-6,19 | 1,46% |
| TEST | Rapida V1 — target pieno 2R | Momentum / breakout | €10.026,44 | €17,67 | 47 | 47 | 36,17% | 1,02 | €0,38 | 2,58% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €10.013,28 | €13,28 | 3 | 3 | 66,67% | 1,24 | €4,43 | 0,89% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €10.010,98 | €10,98 | 9 | 9 | 33,33% | 1,23 | €1,22 | 0,25% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €10.002,20 | €2,20 | 9 | 9 | 33,33% | 1,23 | €0,24 | 0,05% |
| TEST | Scalp RSI Short 85 · prudente · 5x | Inversione RSI estrema 15m | €10.002,09 | €0,97 | 1 | 1 | 100,00% | ∞ | €0,97 | 0,10% |
| TEST | Scalp RSI Short 85 · €50 · 15x | Inversione RSI estrema 15m | €10.001,92 | €1,43 | 1 | 1 | 100,00% | ∞ | €1,43 | 0,07% |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | €10.001,47 | €1,47 | 5 | 5 | 40,00% | 1,12 | €0,29 | 0,13% |
| TEST | Scalp RSI Short 85 · €10 · 15x | Inversione RSI estrema 15m | €10.000,38 | €0,29 | 1 | 1 | 100,00% | ∞ | €0,29 | 0,01% |
| TEST | Scalp RSI Long 25 · €10 · 15x | Inversione RSI estrema 15m | €10.000,29 | €0,29 | 5 | 5 | 40,00% | 1,12 | €0,06 | 0,03% |
| TEST | Scanner Bottom5 Short Continuation V1 | Scanner Bottom5 Short Continuation | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 80 · €10 · 15x | Inversione RSI estrema 15m | €9.999,70 | €-0,30 | 3 | 3 | 66,67% | 0,63 | €-0,10 | 0,02% |
| TEST | Scalp RSI Long 20 · €10 · 15x | Inversione RSI estrema 15m | €9.998,96 | €-1,04 | 2 | 2 | 0,00% | 0,00 | €-0,52 | 0,02% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €9.998,75 | €-1,25 | 4 | 4 | 75,00% | 0,98 | €-0,31 | 0,96% |
| TEST | Scalp RSI Short 80 · €50 · 15x | Inversione RSI estrema 15m | €9.998,52 | €-1,48 | 3 | 3 | 66,67% | 0,63 | €-0,49 | 0,09% |
| TEST | Scalp RSI Long 15 · €10 · 15x | Inversione RSI estrema 15m | €9.998,50 | €-1,50 | 1 | 1 | 0,00% | 0,00 | €-1,50 | 0,02% |
| TEST | Bilanciata 1H — SHORT Trend Down stretto | Confluenza trend | €9.995,87 | €-4,13 | 1 | 1 | 0,00% | 0,00 | €-4,13 | 0,59% |
| TEST | Scalp RSI Long 20 · €50 · 15x | Inversione RSI estrema 15m | €9.994,81 | €-5,19 | 2 | 2 | 0,00% | 0,00 | €-2,59 | 0,08% |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | €9.992,50 | €-7,50 | 1 | 1 | 0,00% | 0,00 | €-7,50 | 0,11% |
| TEST | Scalp RSI Short 80 · prudente · 5x | Inversione RSI estrema 15m | €9.990,24 | €-9,76 | 3 | 3 | 66,67% | 0,28 | €-3,25 | 0,21% |
| TEST | Rapida V3 — qualità completa + profit lock | Momentum / breakout V3 Filtered | €9.988,44 | €-20,27 | 37 | 37 | 48,65% | 0,98 | €-0,55 | 3,21% |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | €9.988,38 | €-11,62 | 1 | 1 | 0,00% | 0,00 | €-11,62 | 0,17% |
| TEST | Scalp RSI Long 20 · prudente · 5x | Inversione RSI estrema 15m | €9.983,60 | €-16,40 | 2 | 2 | 0,00% | 0,00 | €-8,20 | 0,24% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €9.980,62 | €-19,38 | 4 | 4 | 50,00% | 0,82 | €-4,84 | 1,49% |
| TEST | Sol Ema 1H | Trend following EMA | €9.977,09 | €-22,91 | 5 | 5 | 40,00% | 0,86 | €-4,58 | 1,67% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €9.976,99 | €-23,01 | 5 | 5 | 20,00% | 0,20 | €-4,60 | 0,37% |
| TEST | Combo Adaptive — Trend/Transition | Combo Adaptive | €9.975,22 | €-23,53 | 10 | 10 | 50,00% | 0,92 | €-2,35 | 2,18% |
| TEST | Rapida 1H V1 — madre | Momentum / breakout | €9.974,17 | €-23,25 | 76 | 76 | 34,21% | 0,99 | €-0,31 | 6,76% |
| TEST | Top 5 + BTC — Guard + BTC≤3 | Scanner Top 5 + forza BTC | €9.971,62 | €-27,61 | 9 | 9 | 44,44% | 0,92 | €-3,07 | 2,77% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €9.966,00 | €-58,57 | 40 | 39 | 37,50% | 0,96 | €-1,46 | 5,10% |
| TEST | Combo Adaptive — Long Only | Combo Adaptive | €9.964,84 | €-32,81 | 10 | 10 | 40,00% | 0,86 | €-3,28 | 2,34% |
| TEST | Rapida V3 — senza ESPORTS | Momentum / breakout V3 Filtered | €9.963,13 | €-43,36 | 48 | 48 | 39,58% | 0,96 | €-0,90 | 2,49% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.962,86 | €-33,95 | 26 | 26 | 38,46% | 0,94 | €-1,31 | 2,25% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €9.959,21 | €-61,88 | 37 | 37 | 40,54% | 0,93 | €-1,67 | 4,19% |
| TEST | Scanner Bottom5 Short Profit Lock V1 | Scanner Bottom 5 Short | €9.952,41 | €-119,98 | 5 | 5 | 40,00% | 0,25 | €-24,00 | 1,53% |
| TEST | Btc Ema 4H | Trend following EMA | €9.950,68 | €-49,32 | 1 | 1 | 0,00% | 0,00 | €-49,32 | 0,96% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €9.950,68 | €-49,32 | 1 | 1 | 0,00% | 0,00 | €-49,32 | 0,96% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €9.949,62 | €-50,38 | 1 | 1 | 0,00% | 0,00 | €-50,38 | 0,74% |
| TEST | Eth Ema 4H | Trend following EMA | €9.945,46 | €-52,88 | 1 | 1 | 0,00% | 0,00 | €-52,88 | 0,70% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.944,12 | €-55,88 | 9 | 9 | 22,22% | 0,16 | €-6,21 | 0,56% |
| TEST | Top 5 + BTC — BTC≤3 | Scanner Top 5 + forza BTC | €9.942,96 | €-55,59 | 10 | 10 | 50,00% | 0,84 | €-5,56 | 2,74% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €9.937,14 | €-51,83 | 1 | 1 | 0,00% | 0,00 | €-51,83 | 0,73% |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | Scanner Bottom 5 Short | €9.936,71 | €-74,71 | 6 | 6 | 50,00% | 0,54 | €-12,45 | 1,38% |
| TEST | Rapida V3 — no volatilità HIGH | Momentum / breakout V3 Filtered | €9.936,20 | €-70,28 | 49 | 49 | 40,82% | 0,94 | €-1,43 | 2,96% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €9.935,97 | €-52,00 | 1 | 1 | 0,00% | 0,00 | €-52,00 | 0,75% |
| TEST | Combo Scanner | Combo Scanner | €9.930,95 | €-67,73 | 33 | 33 | 45,45% | 0,93 | €-2,05 | 2,75% |
| TEST | Combo Adaptive — target pieno 3R | Combo Adaptive | €9.929,58 | €-66,67 | 13 | 13 | 46,15% | 0,76 | €-5,13 | 1,41% |
| TEST | Top 5 + BTC — BTC 2–3 | Scanner Top 5 + forza BTC | €9.928,83 | €-67,07 | 4 | 4 | 25,00% | 0,47 | €-16,77 | 2,38% |
| TEST | Ampia 4H | Confluenza trend | €9.927,52 | €-53,35 | 17 | 17 | 23,53% | 0,89 | €-3,14 | 3,67% |
| TEST | Combo Adaptive — Quality7 + Regime + parziale 1R | Combo Adaptive | €9.916,34 | €-82,62 | 5 | 5 | 40,00% | 0,48 | €-16,52 | 1,95% |
| TEST | Sol Ema 4H | Trend following EMA | €9.914,41 | €-52,00 | 1 | 1 | 0,00% | 0,00 | €-52,00 | 0,97% |
| TEST | Btc Ema 1H | Trend following EMA | €9.911,86 | €-88,14 | 6 | 6 | 33,33% | 0,59 | €-14,69 | 1,56% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.907,44 | €-72,68 | 4 | 4 | 25,00% | 0,56 | €-18,17 | 1,38% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.901,25 | €-98,75 | 4 | 4 | 25,00% | 0,41 | €-24,69 | 1,89% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €9.888,87 | €-111,13 | 2 | 2 | 0,00% | 0,00 | €-55,56 | 1,26% |
| TEST | Master Adaptive GB20 — Breakeven 0,5R | Master Adaptive Consensus | €9.883,75 | €-113,94 | 11 | 11 | 18,18% | 0,64 | €-10,36 | 2,56% |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | Momentum / breakout V3 Filtered | €9.879,59 | €-139,39 | 9 | 9 | 55,56% | 0,46 | €-15,49 | 2,51% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | Momentum / breakout V3 Filtered | €9.879,59 | €-139,39 | 9 | 9 | 55,56% | 0,46 | €-15,49 | 2,51% |
| TEST | Bilanciata 1H — LONG senza Range High Vol | Confluenza trend | €9.870,73 | €-130,27 | 9 | 9 | 33,33% | 0,60 | €-14,47 | 2,37% |
| TEST | Scanner Top10 Long | Scanner Top10 Long | €9.863,83 | €-144,63 | 8 | 8 | 37,50% | 0,42 | €-18,08 | 3,30% |
| TEST | Scanner Top15 Long | Scanner Top15 Long | €9.863,83 | €-144,63 | 8 | 8 | 37,50% | 0,42 | €-18,08 | 3,30% |
| TEST | Scanner Top20 Long | Scanner Top20 Long | €9.863,83 | €-144,63 | 8 | 8 | 37,50% | 0,42 | €-18,08 | 3,30% |
| TEST | Master Adaptive GB20 — 50% a 0,75R | Master Adaptive Consensus | €9.862,49 | €-142,71 | 6 | 6 | 33,33% | 0,49 | €-23,78 | 2,42% |
| TEST | Combo Adaptive — Quality7 + Regime | Combo Adaptive | €9.855,64 | €-143,33 | 5 | 5 | 20,00% | 0,17 | €-28,67 | 1,95% |
| TEST | Master Adaptive GB20 — Loss Cap 0,75R | Master Adaptive Consensus | €9.846,34 | €-151,42 | 7 | 7 | 28,57% | 0,47 | €-21,63 | 2,99% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.836,36 | €-146,11 | 5 | 5 | 40,00% | 0,11 | €-29,22 | 1,68% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €9.835,19 | €-164,81 | 6 | 6 | 33,33% | 0,29 | €-27,47 | 2,34% |
| TEST | Scanner Bottom10 Short | Scanner Bottom10 Short | €9.825,21 | €-245,28 | 6 | 6 | 16,67% | 0,11 | €-40,88 | 2,72% |
| TEST | Scanner Bottom15 Short | Scanner Bottom15 Short | €9.825,21 | €-245,28 | 6 | 6 | 16,67% | 0,11 | €-40,88 | 2,72% |
| TEST | Scanner Bottom20 Short | Scanner Bottom20 Short | €9.825,21 | €-245,28 | 6 | 6 | 16,67% | 0,11 | €-40,88 | 2,72% |
| TEST | Rapida V3 — Long Only | Momentum / breakout V3 Filtered | €9.823,29 | €-237,79 | 39 | 39 | 33,33% | 0,76 | €-6,10 | 3,65% |
| TEST | Top 5 + BTC — Guard | Scanner Top 5 + forza BTC | €9.800,91 | €-197,97 | 14 | 14 | 28,57% | 0,63 | €-14,14 | 3,31% |
| TEST | Top 5 + BTC — solo MFE | Scanner Top 5 + forza BTC | €9.791,96 | €-191,30 | 17 | 17 | 35,29% | 0,51 | €-11,25 | 3,95% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.790,66 | €-209,34 | 10 | 10 | 30,00% | 0,37 | €-20,93 | 2,92% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.778,76 | €-288,92 | 29 | 29 | 31,03% | 0,61 | €-9,96 | 5,48% |
| TEST | Eth Ema 1H | Trend following EMA | €9.764,35 | €-218,24 | 7 | 7 | 28,57% | 0,20 | €-31,18 | 2,36% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €9.727,40 | €-252,04 | 45 | 45 | 60,00% | 0,67 | €-5,60 | 4,16% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €9.722,80 | €-275,74 | 12 | 12 | 33,33% | 0,51 | €-22,98 | 3,05% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €9.713,26 | €-268,44 | 8 | 8 | 25,00% | 0,42 | €-33,56 | 3,21% |
| TEST | Combo Adaptive — parziale 1R | Combo Adaptive | €9.702,62 | €-314,06 | 17 | 17 | 35,29% | 0,47 | €-18,47 | 3,32% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €9.688,11 | €-310,43 | 11 | 11 | 27,27% | 0,40 | €-28,22 | 3,40% |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | €9.678,90 | €-319,65 | 9 | 9 | 22,22% | 0,38 | €-35,52 | 3,49% |
| TEST | Top 5 + BTC — Guard + BTC≤3 + MFE | Scanner Top 5 + forza BTC | €9.678,61 | €-367,59 | 24 | 24 | 37,50% | 0,52 | €-15,32 | 3,57% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €9.636,56 | €-362,07 | 27 | 27 | 25,93% | 0,56 | €-13,41 | 5,74% |
| TEST | Combo Trend | Combo Trend | €9.572,47 | €-419,10 | 38 | 38 | 31,58% | 0,71 | €-11,03 | 7,02% |
| TEST | Top 5 + BTC — Guard + MFE | Scanner Top 5 + forza BTC | €9.568,94 | €-476,90 | 27 | 27 | 33,33% | 0,45 | €-17,66 | 4,72% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €9.549,20 | €-431,78 | 18 | 18 | 27,78% | 0,52 | €-23,99 | 4,77% |
| TEST | Combo Adaptive — MFE Trail esistente | Combo Adaptive | €9.521,88 | €-475,61 | 29 | 29 | 27,59% | 0,39 | €-16,40 | 5,33% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | LAB | SHORT | Confluenza trend | 240m | 3,0x | 0,17841 | 0,17841 | 0,17841 | 0,23699 | 0,13559 | €136,26 | €408,77 | €0,00 | €-0,00 |
| Principale 4H | SUI | LONG | Confluenza trend | 240m | 3,0x | 0,76296 | 0,76296 | 0,73998 | 0,51245 | 0,80891 | €547,52 | €1.642,56 | €49,46 | €0,00 |
| Principale 4H | ONDO | LONG | Confluenza trend | 240m | 3,0x | 0,40344 | 0,40344 | 0,37762 | 0,27098 | 0,45509 | €254,70 | €764,09 | €48,91 | €0,00 |
| Principale 4H | BANK | LONG | Confluenza trend | 240m | 3,0x | 0,36220 | 0,38400 | 0,31874 | 0,24328 | 0,44913 | €128,59 | €385,77 | €46,29 | €23,22 |
| Principale 4H | SHIB | LONG | Confluenza trend | 240m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €8,88 | €26,63 | €2,22 | €0,08 |
| Bilanciata 1H V1 | ADA | SHORT | Confluenza trend | 60m | 3,0x | 0,16703 | 0,16703 | 0,16365 | 0,22187 | 0,16112 | €978,72 | €2.936,17 | €0,00 | €-0,00 |
| Bilanciata 1H V1 | AKE | LONG | Confluenza trend | 60m | 3,0x | 0,00329 | 0,00329 | 0,00290 | 0,00221 | 0,00408 | €12,36 | €37,07 | €4,45 | €0,00 |
| Bilanciata 1H V1 | ALLO | SHORT | Confluenza trend | 60m | 3,0x | 0,36179 | 0,36179 | 0,40521 | 0,48058 | 0,27496 | €141,53 | €424,59 | €50,95 | €-0,00 |
| Bilanciata 1H V1 | BANK | LONG | Confluenza trend | 60m | 3,0x | 0,38137 | 0,38400 | 0,34474 | 0,25615 | 0,45462 | €172,02 | €516,05 | €49,56 | €3,56 |
| Bilanciata 1H V1 | SHIB | LONG | Confluenza trend | 60m | 3,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €334,28 | €1.002,84 | €50,35 | €-3,96 |
| Bilanciata 1H — LONG senza Range High Vol | AKE | LONG | Confluenza trend | 60m | 3,0x | 0,00320 | 0,00320 | 0,00282 | 0,00215 | 0,00397 | €138,85 | €416,55 | €49,99 | €0,00 |
| Bilanciata 1H — LONG senza Range High Vol | BEAT | LONG | Confluenza trend | 60m | 3,0x | 3,29017 | 3,29017 | 3,00714 | 2,20990 | 3,85623 | €193,69 | €581,07 | €49,98 | €0,00 |
| Bilanciata 1H — LONG senza Range High Vol | XMR | LONG | Confluenza trend | 60m | 3,0x | 366,72991 | 366,72991 | 360,04130 | 246,32025 | 380,10712 | €915,26 | €2.745,79 | €50,08 | €0,00 |
| Bilanciata 1H — LONG senza Range High Vol | BANK | LONG | Confluenza trend | 60m | 3,0x | 0,38137 | 0,38400 | 0,34474 | 0,25615 | 0,45462 | €164,19 | €492,56 | €47,31 | €3,40 |
| Bilanciata 1H V2 | ADA | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,16276 | 0,16276 | 0,16511 | 0,21620 | 0,15807 | €1.185,56 | €3.556,68 | €51,22 | €-0,00 |
| Bilanciata 1H V2 | AKE | LONG | Confluenza trend V2 | 60m | 3,0x | 0,00320 | 0,00320 | 0,00282 | 0,00215 | 0,00397 | €142,81 | €428,43 | €51,41 | €0,00 |
| Bilanciata 1H V2 | WLD | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,34349 | 0,34349 | 0,35287 | 0,45627 | 0,32475 | €26,53 | €79,60 | €2,17 | €-0,00 |
| Bilanciata 1H V2 | BANK | LONG | Confluenza trend V2 | 60m | 3,0x | 0,36742 | 0,38400 | 0,37126 | 0,24679 | 0,44120 | €161,71 | €485,13 | €0,00 | €21,89 |
| Bilanciata 1H V2 | ALLO | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,35543 | 0,35543 | 0,39400 | 0,47213 | 0,27829 | €146,68 | €440,04 | €47,75 | €-0,00 |
| Bilanciata 1H V2 | HYPE | LONG | Confluenza trend V2 | 60m | 3,0x | 58,92678 | 59,59600 | 59,20257 | 39,57916 | 60,62387 | €24,72 | €74,16 | €0,00 | €0,84 |
| Bilanciata 1H V3 Filtered | BEAT | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 3,31215 | 3,31215 | 3,02723 | 2,22466 | 3,88198 | €203,36 | €610,09 | €52,48 | €0,00 |
| Bilanciata 1H V3 Filtered | WLD | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,34349 | 0,34349 | 0,35287 | 0,45627 | 0,32475 | €23,43 | €70,29 | €1,92 | €-0,00 |
| Bilanciata 1H V3 Filtered | AKE | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,00330 | 0,00330 | 0,00293 | 0,00221 | 0,00403 | €158,25 | €474,75 | €52,90 | €0,00 |
| Bilanciata 1H V3 Filtered | ALLO | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,34255 | 0,34255 | 0,37914 | 0,45502 | 0,26938 | €160,61 | €481,84 | €51,46 | €-0,00 |
| Bilanciata 1H V3 Filtered | SHIB | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €8,58 | €25,73 | €1,38 | €0,32 |
| Bilanciata 1H V3 Filtered | ESPORTS | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,02905 | 0,02739 | 0,03254 | 0,03859 | 0,02208 | €142,96 | €428,87 | €51,46 | €24,57 |
| Bilanciata 1H V3 Filtered | ETH | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1958,25157 | 1949,39000 | 1930,05275 | 1315,29231 | 2014,64922 | €8,95 | €26,84 | €0,39 | €-0,12 |
| Rapida 1H V1 — madre | ADA | SHORT | Momentum / breakout | 60m | 3,0x | 0,16185 | 0,16185 | 0,16367 | 0,21499 | 0,15913 | €1.486,90 | €4.460,70 | €49,96 | €-0,00 |
| Rapida 1H V1 — madre | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00320 | 0,00320 | 0,00286 | 0,00215 | 0,00370 | €158,12 | €474,35 | €49,93 | €0,00 |
| Rapida V1 — score 6–7,5 | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00320 | 0,00320 | 0,00287 | 0,00215 | 0,00369 | €167,22 | €501,65 | €51,54 | €0,00 |
| Rapida V1 — score 6–7,5 | ALLO | SHORT | Momentum / breakout | 60m | 3,0x | 0,33713 | 0,33713 | 0,36471 | 0,44782 | 0,29576 | €212,67 | €638,01 | €52,19 | €-0,00 |
| Rapida V1 — score 6–7,5 | BANK | LONG | Momentum / breakout | 60m | 3,0x | 0,38680 | 0,38400 | 0,35294 | 0,25980 | 0,43759 | €197,79 | €593,37 | €51,94 | €-4,29 |
| Rapida V1 — score 6–7,5 | ESPORTS | SHORT | Momentum / breakout | 60m | 3,0x | 0,03069 | 0,02739 | 0,03069 | 0,04077 | 0,02517 | €140,09 | €420,28 | €0,00 | €45,24 |
| Rapida V1 — score 6–7,5 | SHIB | LONG | Momentum / breakout | 60m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €11,70 | €35,09 | €1,52 | €0,76 |
| Rapida score 6–7,5 — senza Trend Up | BEAT | LONG | Momentum / breakout | 60m | 3,0x | 3,29017 | 3,29017 | 3,07004 | 2,20990 | 3,62037 | €256,24 | €768,73 | €51,43 | €0,00 |
| Rapida score 6–7,5 — senza Trend Up | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00322 | 0,00322 | 0,00289 | 0,00216 | 0,00372 | €167,84 | €503,53 | €51,67 | €0,00 |
| Rapida score 6–7,5 — senza Trend Up | BANK | LONG | Momentum / breakout | 60m | 3,0x | 0,38680 | 0,38400 | 0,35294 | 0,25980 | 0,43759 | €194,63 | €583,90 | €51,12 | €-4,22 |
| Rapida score 6–7,5 — senza Trend Up | ALLO | SHORT | Momentum / breakout | 60m | 3,0x | 0,33808 | 0,33808 | 0,36389 | 0,44909 | 0,29937 | €218,91 | €656,73 | €50,14 | €-0,00 |
| Rapida score 6–7,5 — Range Only | BEAT | LONG | Momentum / breakout | 60m | 3,0x | 3,29017 | 3,29017 | 3,07004 | 2,20990 | 3,62037 | €256,24 | €768,73 | €51,43 | €0,00 |
| Rapida score 6–7,5 — Range Only | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00322 | 0,00322 | 0,00289 | 0,00216 | 0,00372 | €167,84 | €503,53 | €51,67 | €0,00 |
| Rapida score 6–7,5 — Range Only | ESPORTS | SHORT | Momentum / breakout | 60m | 3,0x | 0,02828 | 0,02739 | 0,03168 | 0,03757 | 0,02319 | €143,01 | €429,04 | €51,48 | €13,57 |
| Rapida score 6–7,5 — Range Only | SHIB | LONG | Momentum / breakout | 60m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €394,57 | €1.183,71 | €51,34 | €25,67 |
| Rapida score 6–7,5 — Cost Aware | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00322 | 0,00322 | 0,00289 | 0,00216 | 0,00372 | €167,51 | €502,54 | €51,57 | €0,00 |
| Rapida score 6–7,5 — Cost Aware | ALLO | SHORT | Momentum / breakout | 60m | 3,0x | 0,33713 | 0,33713 | 0,36471 | 0,44782 | 0,29576 | €211,20 | €633,59 | €51,83 | €-0,00 |
| Rapida score 6–7,5 — Cost Aware | BANK | LONG | Momentum / breakout | 60m | 3,0x | 0,38680 | 0,38400 | 0,35294 | 0,25980 | 0,43759 | €197,03 | €591,09 | €51,75 | €-4,27 |
| Rapida score 6–7,5 — Cost Aware | ESPORTS | SHORT | Momentum / breakout | 60m | 3,0x | 0,03069 | 0,02739 | 0,03069 | 0,04077 | 0,02517 | €139,36 | €418,09 | €0,00 | €45,00 |
| Rapida score 6–7,5 — Cost Aware | SHIB | LONG | Momentum / breakout | 60m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €11,64 | €34,93 | €1,52 | €0,76 |
| Rapida V1 — no HIGH + score <7,5 | BEAT | LONG | Momentum / breakout | 60m | 3,0x | 3,29017 | 3,29017 | 3,07004 | 2,20990 | 3,62037 | €257,44 | €772,31 | €51,67 | €0,00 |
| Rapida V1 — no HIGH + score <7,5 | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00320 | 0,00320 | 0,00287 | 0,00215 | 0,00369 | €165,85 | €497,54 | €51,12 | €0,00 |
| Rapida V1 — no HIGH + score <7,5 | EUL | LONG | Momentum / breakout | 60m | 3,0x | 2,41518 | 2,28360 | 2,12536 | 1,62220 | 2,84992 | €145,14 | €435,42 | €52,25 | €-23,72 |
| Rapida V1 — no HIGH + score <7,5 | ALLO | SHORT | Momentum / breakout | 60m | 3,0x | 0,33808 | 0,33808 | 0,36389 | 0,44909 | 0,29937 | €225,73 | €677,19 | €51,70 | €-0,00 |
| Rapida V1 — no HIGH + score <7,5 | ESPORTS | SHORT | Momentum / breakout | 60m | 3,0x | 0,02935 | 0,02739 | 0,02935 | 0,03899 | 0,02407 | €9,13 | €27,40 | €0,00 | €1,83 |
| Rapida V1 — Long + BTC 1–3 + score <7,5 | EUL | LONG | Momentum / breakout | 60m | 3,0x | 2,38098 | 2,28360 | 2,09526 | 1,59922 | 2,80955 | €139,67 | €419,02 | €50,28 | €-17,14 |
| Rapida V1 — Long + BTC 1–3 + score <7,5 | SHIB | LONG | Momentum / breakout | 60m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €385,88 | €1.157,65 | €50,21 | €25,11 |
| Rapida V1 — Long + BTC 1–3 + score <7,5 | PEPE | LONG | Momentum / breakout | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €740,22 | €2.220,65 | €0,00 | €45,06 |
| Rapida V1 — Long + BTC 1–3 + score <7,5 | ETH | LONG | Momentum / breakout | 60m | 3,0x | 1958,25157 | 1949,39000 | 1936,31915 | 1315,29231 | 1991,15020 | €1.517,93 | €4.553,78 | €51,00 | €-20,61 |
| Rapida V1 — Long + BTC 1–3 + score <7,5 | XRP | LONG | Momentum / breakout | 60m | 3,0x | 1,11443 | 1,11110 | 1,10195 | 0,74853 | 1,13316 | €70,58 | €211,74 | €2,37 | €-0,63 |
| Rapida V1 — senza PEPE | ADA | SHORT | Momentum / breakout | 60m | 3,0x | 0,16185 | 0,16185 | 0,16367 | 0,21499 | 0,15913 | €1.512,75 | €4.538,24 | €50,83 | €-0,00 |
| Rapida V1 — senza PEPE | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00320 | 0,00320 | 0,00286 | 0,00215 | 0,00370 | €160,87 | €482,60 | €50,80 | €0,00 |
| Rapida V1 — senza PEPE | WLD | SHORT | Momentum / breakout | 60m | 3,0x | 0,34959 | 0,34959 | 0,35668 | 0,46437 | 0,33896 | €838,72 | €2.516,16 | €51,00 | €-0,00 |
| Rapida V1 — senza PEPE | BANK | LONG | Momentum / breakout | 60m | 3,0x | 0,37568 | 0,38400 | 0,34052 | 0,25233 | 0,42842 | €175,27 | €525,81 | €49,21 | €11,65 |
| Rapida V1 — senza PEPE | ETH | LONG | Momentum / breakout | 60m | 3,0x | 1958,25157 | 1949,39000 | 1936,31915 | 1315,29231 | 1991,15020 | €12,11 | €36,33 | €0,41 | €-0,16 |
| Rapida V1 — target pieno 2R | ADA | SHORT | Momentum / breakout | 60m | 3,0x | 0,16185 | 0,16185 | 0,16367 | 0,21499 | 0,15823 | €1.482,83 | €4.448,49 | €49,82 | €-0,00 |
| Rapida V1 — target pieno 2R | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00320 | 0,00320 | 0,00286 | 0,00215 | 0,00387 | €157,69 | €473,06 | €49,80 | €0,00 |
| Rapida V1 — target pieno 2R | WLD | SHORT | Momentum / breakout | 60m | 3,0x | 0,34959 | 0,34959 | 0,35668 | 0,46437 | 0,33542 | €42,01 | €126,02 | €2,55 | €-0,00 |
| Rapida V1 — target pieno 2R | BANK | LONG | Momentum / breakout | 60m | 3,0x | 0,37568 | 0,38400 | 0,34052 | 0,25233 | 0,44600 | €177,34 | €532,02 | €49,79 | €11,79 |
| Rapida V1 — target pieno 2R | ALLO | SHORT | Momentum / breakout | 60m | 3,0x | 0,35543 | 0,35543 | 0,38543 | 0,47213 | 0,29543 | €187,33 | €561,99 | €47,43 | €-0,00 |
| Rapida V1 — target pieno 2R | SHIB | LONG | Momentum / breakout | 60m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €10,60 | €31,81 | €1,45 | €0,75 |
| Rapida 1H V2 | TAO | SHORT | Momentum / breakout V2 | 60m | 3,0x | 188,48684 | 188,48684 | 190,75481 | 250,37335 | 185,08488 | €1.390,02 | €4.170,07 | €50,18 | €-0,00 |
| Rapida 1H V2 | ADA | SHORT | Momentum / breakout V2 | 60m | 3,0x | 0,16185 | 0,16185 | 0,16367 | 0,21499 | 0,15913 | €1.494,54 | €4.483,63 | €50,22 | €-0,00 |
| Rapida 1H V2 | BANK | LONG | Momentum / breakout V2 | 60m | 3,0x | 0,39689 | 0,38400 | 0,36875 | 0,26658 | 0,43909 | €237,29 | €711,88 | €50,47 | €-23,12 |
| Rapida 1H V2 | XRP | LONG | Momentum / breakout V2 | 60m | 3,0x | 1,11443 | 1,11110 | 1,10195 | 0,74853 | 1,13316 | €1.498,43 | €4.495,30 | €50,35 | €-13,44 |
| Rapida 1H V3 Filtered — madre | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16185 | 0,16185 | 0,16367 | 0,21499 | 0,15913 | €1.521,20 | €4.563,60 | €51,11 | €-0,00 |
| Rapida 1H V3 Filtered — madre | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00320 | 0,00320 | 0,00286 | 0,00215 | 0,00370 | €161,77 | €485,30 | €51,08 | €0,00 |
| Rapida 1H V3 Filtered — madre | WLD | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,34959 | 0,34959 | 0,35668 | 0,46437 | 0,33896 | €843,41 | €2.530,22 | €51,28 | €-0,00 |
| Rapida 1H V3 Filtered — madre | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,37568 | 0,38400 | 0,34052 | 0,25233 | 0,42842 | €176,34 | €529,01 | €49,51 | €11,72 |
| Rapida 1H V3 Filtered — madre | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1958,25157 | 1949,39000 | 1936,31915 | 1315,29231 | 1991,15020 | €12,51 | €37,52 | €0,42 | €-0,17 |
| Rapida V3 — score <7,5 | BEAT | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 3,29017 | 3,29017 | 3,07004 | 2,20990 | 3,62037 | €258,77 | €776,32 | €51,94 | €0,00 |
| Rapida V3 — score <7,5 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00320 | 0,00320 | 0,00287 | 0,00215 | 0,00369 | €166,71 | €500,13 | €51,38 | €0,00 |
| Rapida V3 — score <7,5 | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,38680 | 0,38400 | 0,35294 | 0,25980 | 0,43759 | €197,36 | €592,09 | €51,83 | €-4,28 |
| Rapida V3 — score <7,5 | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,33808 | 0,33808 | 0,36389 | 0,44909 | 0,29937 | €227,32 | €681,96 | €52,06 | €-0,00 |
| Rapida V3 — score <7,5 | SHIB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €10,86 | €32,57 | €1,41 | €0,71 |
| Rapida V3 — no volatilità HIGH | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16185 | 0,16185 | 0,16367 | 0,21499 | 0,15913 | €1.485,86 | €4.457,58 | €49,92 | €-0,00 |
| Rapida V3 — no volatilità HIGH | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00320 | 0,00320 | 0,00286 | 0,00215 | 0,00370 | €158,01 | €474,02 | €49,90 | €0,00 |
| Rapida V3 — no volatilità HIGH | WLD | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,34959 | 0,34959 | 0,35668 | 0,46437 | 0,33896 | €823,75 | €2.471,25 | €50,08 | €-0,00 |
| Rapida V3 — no volatilità HIGH | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,37568 | 0,38400 | 0,34052 | 0,25233 | 0,42842 | €172,41 | €517,23 | €48,41 | €11,46 |
| Rapida V3 — no volatilità HIGH | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1958,25157 | 1949,39000 | 1936,31915 | 1315,29231 | 1991,15020 | €12,22 | €36,66 | €0,41 | €-0,17 |
| Rapida V3 — Long Only | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00320 | 0,00320 | 0,00286 | 0,00215 | 0,00370 | €155,06 | €465,19 | €48,97 | €0,00 |
| Rapida V3 — Long Only | BEAT | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 3,29017 | 3,29017 | 3,07004 | 2,20990 | 3,62037 | €243,96 | €731,87 | €48,97 | €0,00 |
| Rapida V3 — Long Only | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,35851 | 0,38400 | 0,37110 | 0,24080 | 0,40774 | €180,50 | €541,50 | €0,00 | €38,50 |
| Rapida V3 — Long Only | SHIB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €375,62 | €1.126,85 | €48,88 | €24,44 |
| Rapida V3 — Long + no HIGH + score <7,5 | BEAT | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 3,29017 | 3,29017 | 3,07004 | 2,20990 | 3,62037 | €246,62 | €739,85 | €49,50 | €0,00 |
| Rapida V3 — Long + no HIGH + score <7,5 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00322 | 0,00322 | 0,00289 | 0,00216 | 0,00372 | €160,75 | €482,24 | €49,49 | €0,00 |
| Rapida V3 — Long + no HIGH + score <7,5 | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,38680 | 0,38400 | 0,35294 | 0,25980 | 0,43759 | €190,39 | €571,16 | €50,00 | €-4,13 |
| Rapida V3 — Long + no HIGH + score <7,5 | SHIB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €385,28 | €1.155,84 | €50,13 | €25,07 |
| Rapida V3 — Long + no HIGH + score <7,5 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1958,25157 | 1949,39000 | 1936,31915 | 1315,29231 | 1991,15020 | €47,77 | €143,31 | €1,61 | €-0,65 |
| Rapida V3 — senza ESPORTS | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16185 | 0,16185 | 0,16367 | 0,21499 | 0,15913 | €1.489,89 | €4.469,66 | €50,06 | €-0,00 |
| Rapida V3 — senza ESPORTS | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00320 | 0,00320 | 0,00286 | 0,00215 | 0,00370 | €158,44 | €475,31 | €50,03 | €0,00 |
| Rapida V3 — senza ESPORTS | WLD | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,34959 | 0,34959 | 0,35668 | 0,46437 | 0,33896 | €825,98 | €2.477,95 | €50,22 | €-0,00 |
| Rapida V3 — senza ESPORTS | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,37568 | 0,38400 | 0,34052 | 0,25233 | 0,42842 | €172,88 | €518,63 | €48,54 | €11,49 |
| Rapida V3 — senza ESPORTS | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1958,25157 | 1949,39000 | 1936,31915 | 1315,29231 | 1991,15020 | €12,25 | €36,76 | €0,41 | €-0,17 |
| Rapida V3 senza ESPORTS — Long Only | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00320 | 0,00320 | 0,00286 | 0,00215 | 0,00370 | €158,13 | €474,39 | €49,94 | €0,00 |
| Rapida V3 senza ESPORTS — Long Only | BEAT | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 3,29017 | 3,29017 | 3,07004 | 2,20990 | 3,62037 | €248,78 | €746,34 | €49,93 | €0,00 |
| Rapida V3 senza ESPORTS — Long Only | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,35851 | 0,38400 | 0,37110 | 0,24080 | 0,40774 | €184,93 | €554,79 | €0,00 | €39,44 |
| Rapida V3 senza ESPORTS — Long Only | EUL | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,41608 | 2,28360 | 2,12615 | 1,62280 | 2,85098 | €141,16 | €423,48 | €50,82 | €-23,22 |
| Rapida V3 senza ESPORTS — Long Only | SHIB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €20,15 | €60,45 | €2,62 | €1,31 |
| Rapida V3 senza ESPORTS — MFE Lock | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16185 | 0,16185 | 0,16367 | 0,21499 | 0,15913 | €1.510,84 | €4.532,53 | €50,76 | €-0,00 |
| Rapida V3 senza ESPORTS — MFE Lock | WLD | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,34959 | 0,34959 | 0,35668 | 0,46437 | 0,33896 | €11,86 | €35,57 | €0,72 | €-0,00 |
| Rapida V3 senza ESPORTS — MFE Lock | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,33165 | 0,33165 | 0,36472 | 0,44055 | 0,28205 | €170,96 | €512,89 | €51,14 | €-0,00 |
| Rapida V3 senza ESPORTS — MFE Lock | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00317 | 0,00317 | 0,00290 | 0,00213 | 0,00358 | €199,03 | €597,09 | €50,62 | €0,00 |
| Rapida V3 senza ESPORTS — MFE Lock | SHIB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €22,69 | €68,06 | €0,00 | €1,48 |
| Rapida V3 senza ESPORTS — MFE Lock | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,39859 | 0,38400 | 0,37039 | 0,26772 | 0,44090 | €232,17 | €696,52 | €49,29 | €-25,49 |
| Rapida V3 senza ESPORTS — Stress Guard | SHIB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €429,11 | €1.287,32 | €50,80 | €3,62 |
| Rapida V3 senza ESPORTS — Stress Guard | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1958,25157 | 1949,39000 | 1936,31915 | 1315,29231 | 1991,15020 | €1.513,02 | €4.539,06 | €50,84 | €-20,54 |
| Rapida V3 senza ESPORTS — Stress Guard | XRP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,11443 | 1,11110 | 1,10195 | 0,74853 | 1,13316 | €1.512,48 | €4.537,44 | €50,82 | €-13,57 |
| Rapida V3 senza ESPORTS — Stress Guard | PEPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €873,54 | €2.620,61 | €50,01 | €-0,52 |
| Rapida V3 — qualità completa + profit lock | BEAT | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 3,29017 | 3,29017 | 3,07004 | 2,20990 | 3,62037 | €245,16 | €735,47 | €49,21 | €0,00 |
| Rapida V3 — qualità completa + profit lock | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00322 | 0,00322 | 0,00289 | 0,00216 | 0,00372 | €159,93 | €479,80 | €49,24 | €0,00 |
| Rapida V3 — qualità completa + profit lock | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,36220 | 0,38400 | 0,37087 | 0,24328 | 0,41423 | €172,68 | €518,03 | €0,00 | €31,18 |
| Rapida V3 — qualità completa + profit lock | SHIB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €15,43 | €46,28 | €2,01 | €1,00 |
| Rapida V3 — qualità completa + profit lock | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1958,25157 | 1949,39000 | 1936,31915 | 1315,29231 | 1991,15020 | €1.489,80 | €4.469,41 | €50,06 | €-20,23 |
| Ampia 4H | HYPE | SHORT | Confluenza trend | 240m | 2,0x | 58,36732 | 59,59600 | 61,80927 | 87,25915 | 48,72988 | €424,03 | €848,06 | €50,01 | €-17,85 |
| Ampia 4H | TAO | SHORT | Confluenza trend | 240m | 2,0x | 189,05650 | 189,05650 | 197,51338 | 282,63946 | 165,37722 | €558,68 | €1.117,36 | €49,98 | €-0,00 |
| Ampia 4H | AKE | LONG | Confluenza trend | 240m | 2,0x | 0,00328 | 0,00328 | 0,00288 | 0,00165 | 0,00438 | €207,40 | €414,80 | €49,78 | €0,00 |
| Ampia 4H | XMR | LONG | Confluenza trend | 240m | 2,0x | 364,45854 | 364,45854 | 347,94701 | 184,05156 | 410,69083 | €544,42 | €1.088,84 | €49,33 | €0,00 |
| Forza relativa 1H V1 | NIGHT | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,02031 | 0,02031 | 0,02210 | 0,03036 | 0,01637 | €285,91 | €571,83 | €50,45 | €-0,00 |
| Forza relativa 1H V1 | ONDO | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,42171 | €891,90 | €1.783,80 | €49,29 | €0,00 |
| Forza relativa 1H V1 | WLD | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,32287 | €14,97 | €29,93 | €0,82 | €-0,00 |
| Forza relativa 1H V1 | AKE | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,00327 | 0,00327 | 0,00287 | 0,00165 | 0,00413 | €208,36 | €416,72 | €50,01 | €0,00 |
| Forza relativa 1H V2 | AKE | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,00320 | 0,00320 | 0,00282 | 0,00162 | 0,00405 | €216,28 | €432,55 | €51,91 | €0,00 |
| Forza relativa 1H V2 | WLD | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,32287 | €47,70 | €95,39 | €2,60 | €-0,00 |
| Forza relativa 1H V2 | XMR | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 367,08012 | 367,08012 | 360,46822 | 185,37546 | 381,62629 | €1.446,12 | €2.892,24 | €52,10 | €0,00 |
| Forza relativa 1H V2 | BANK | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,36855 | 0,38400 | 0,33045 | 0,18612 | 0,45238 | €219,06 | €438,12 | €45,30 | €18,36 |
| Forza relativa 1H V2 | PEPE | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €846,05 | €1.692,10 | €47,31 | €9,85 |
| Scalp RSI Short 85 · €10 · 15x | SOL | SHORT | Inversione RSI estrema 15m | 15m | 15,0x | 76,58168 | 76,48500 | 77,03591 | 81,30422 | 75,90034 | €10,00 | €150,00 | €0,89 | €0,19 |
| Scalp RSI Short 85 · €50 · 15x | SOL | SHORT | Inversione RSI estrema 15m | 15m | 15,0x | 76,58168 | 76,48500 | 77,03591 | 81,30422 | 75,90034 | €50,00 | €750,00 | €4,45 | €0,95 |
| Scalp RSI Short 85 · prudente · 5x | SOL | SHORT | Inversione RSI estrema 15m | 15m | 5,0x | 76,58168 | 76,48500 | 77,03591 | 91,51511 | 75,67323 | €337,23 | €1.686,15 | €10,00 | €2,13 |
| Benchmark Donchian breakout 1H | SUI | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,76606 | 0,76606 | 0,75182 | 0,38686 | 0,80165 | €1.377,00 | €2.754,00 | €51,18 | €0,00 |
| Benchmark Donchian breakout 1H | ALLO | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,35678 | 0,35678 | 0,39959 | 0,53338 | 0,24974 | €215,19 | €430,38 | €51,65 | €-0,00 |
| Benchmark Donchian breakout 1H | HYPE | LONG | Donchian breakout 20 barre | 60m | 2,0x | 58,92678 | 59,59600 | 57,98395 | 29,75803 | 61,28385 | €1.635,95 | €3.271,90 | €52,35 | €37,16 |
| Benchmark Donchian breakout 1H | BANK | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,39689 | 0,38400 | 0,35670 | 0,20043 | 0,49737 | €258,64 | €517,28 | €52,39 | €-16,80 |
| Benchmark Donchian breakout 1H | ETH | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1958,25157 | 1949,39000 | 1926,91955 | 988,91704 | 2036,58163 | €70,73 | €141,45 | €2,26 | €-0,64 |
| Benchmark Bollinger mean reversion 1H | HYPE | SHORT | Bollinger mean reversion | 60m | 2,0x | 59,61921 | 59,59600 | 60,33464 | 89,13071 | 58,54606 | €1.987,62 | €3.975,25 | €47,70 | €1,55 |
| Benchmark Bollinger mean reversion 1H | ETH | SHORT | Bollinger mean reversion | 60m | 2,0x | 1957,46843 | 1949,39000 | 1980,95805 | 2926,41530 | 1922,23400 | €1.986,67 | €3.973,34 | €47,68 | €16,40 |
| Benchmark Bollinger mean reversion 1H | XRP | SHORT | Bollinger mean reversion | 60m | 2,0x | 1,11399 | 1,11110 | 1,12736 | 1,66541 | 1,09394 | €1.986,03 | €3.972,07 | €47,66 | €10,29 |
| Benchmark trend following EMA 1H | LAB | LONG | Trend following EMA | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €207,05 | €414,10 | €49,69 | €0,00 |
| Benchmark trend following EMA 1H | ALLO | SHORT | Trend following EMA | 60m | 2,0x | 0,35372 | 0,35372 | 0,39616 | 0,52881 | 0,26034 | €209,15 | €418,30 | €50,20 | €-0,00 |
| Benchmark trend following EMA 1H | XMR | LONG | Trend following EMA | 60m | 2,0x | 367,08012 | 367,08012 | 359,73357 | 185,37546 | 383,24253 | €17,91 | €35,83 | €0,72 | €0,00 |
| Benchmark trend following EMA 1H | BANK | LONG | Trend following EMA | 60m | 2,0x | 0,37568 | 0,38400 | 0,33059 | 0,18972 | 0,47485 | €205,19 | €410,38 | €49,25 | €9,09 |
| Benchmark trend following EMA 1H | SHIB | LONG | Trend following EMA | 60m | 2,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €389,51 | €779,03 | €49,98 | €-9,70 |
| Scanner Top 5 Long 1H | LAB | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €219,03 | €438,05 | €52,57 | €0,00 |
| Scanner Top 5 Long 1H | AKE | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,00319 | 0,00319 | 0,00281 | 0,00161 | 0,00396 | €224,41 | €448,82 | €53,86 | €0,00 |
| Scanner Top 5 Long 1H | XMR | LONG | Scanner Top 5 Long | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10712 | €70,71 | €141,42 | €2,58 | €0,00 |
| Scanner Bottom 5 Short 1H | ADA | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,16703 | 0,16703 | 0,16365 | 0,24971 | 0,16112 | €1.381,07 | €2.762,13 | €0,00 | €-0,00 |
| Scanner Bottom 5 Short 1H | ALLO | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,36179 | 0,36179 | 0,40521 | 0,54088 | 0,27496 | €202,53 | €405,06 | €48,61 | €-0,00 |
| Scanner Bottom 5 Short 1H | ESPORTS | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,03342 | 0,02739 | 0,03342 | 0,04997 | 0,02540 | €202,66 | €405,32 | €0,00 | €73,16 |
| Scanner Top10 Long | AKE | LONG | Scanner Top10 Long | 60m | 2,0x | 0,00319 | 0,00319 | 0,00281 | 0,00161 | 0,00396 | €208,33 | €416,67 | €50,00 | €0,00 |
| Scanner Top10 Long | XMR | LONG | Scanner Top10 Long | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10712 | €1.371,36 | €2.742,71 | €50,02 | €0,00 |
| Scanner Top10 Long | BANK | LONG | Scanner Top10 Long | 60m | 2,0x | 0,37568 | 0,38400 | 0,33059 | 0,18972 | 0,46584 | €203,89 | €407,78 | €48,93 | €9,04 |
| Scanner Top10 Long | SHIB | LONG | Scanner Top10 Long | 60m | 2,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €24,14 | €48,29 | €2,71 | €1,41 |
| Scanner Bottom10 Short | ADA | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,16193 | 0,16193 | 0,16426 | 0,24209 | 0,15727 | €1.731,26 | €3.462,51 | €49,86 | €-0,00 |
| Scanner Bottom10 Short | ALLO | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,35250 | 0,35250 | 0,39075 | 0,52699 | 0,27600 | €224,69 | €449,38 | €48,76 | €-0,00 |
| Scanner Bottom10 Short | ESPORTS | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,03342 | 0,02739 | 0,03342 | 0,04997 | 0,02540 | €203,44 | €406,87 | €0,00 | €73,45 |
| Scanner Top15 Long | AKE | LONG | Scanner Top15 Long | 60m | 2,0x | 0,00319 | 0,00319 | 0,00281 | 0,00161 | 0,00396 | €208,33 | €416,67 | €50,00 | €0,00 |
| Scanner Top15 Long | XMR | LONG | Scanner Top15 Long | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10712 | €1.371,36 | €2.742,71 | €50,02 | €0,00 |
| Scanner Top15 Long | BANK | LONG | Scanner Top15 Long | 60m | 2,0x | 0,37568 | 0,38400 | 0,33059 | 0,18972 | 0,46584 | €203,89 | €407,78 | €48,93 | €9,04 |
| Scanner Top15 Long | SHIB | LONG | Scanner Top15 Long | 60m | 2,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €24,14 | €48,29 | €2,71 | €1,41 |
| Scanner Bottom15 Short | ADA | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,16193 | 0,16193 | 0,16426 | 0,24209 | 0,15727 | €1.731,26 | €3.462,51 | €49,86 | €-0,00 |
| Scanner Bottom15 Short | ALLO | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,35250 | 0,35250 | 0,39075 | 0,52699 | 0,27600 | €224,69 | €449,38 | €48,76 | €-0,00 |
| Scanner Bottom15 Short | ESPORTS | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,03342 | 0,02739 | 0,03342 | 0,04997 | 0,02540 | €203,44 | €406,87 | €0,00 | €73,45 |
| Scanner Top20 Long | AKE | LONG | Scanner Top20 Long | 60m | 2,0x | 0,00319 | 0,00319 | 0,00281 | 0,00161 | 0,00396 | €208,33 | €416,67 | €50,00 | €0,00 |
| Scanner Top20 Long | XMR | LONG | Scanner Top20 Long | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10712 | €1.371,36 | €2.742,71 | €50,02 | €0,00 |
| Scanner Top20 Long | BANK | LONG | Scanner Top20 Long | 60m | 2,0x | 0,37568 | 0,38400 | 0,33059 | 0,18972 | 0,46584 | €203,89 | €407,78 | €48,93 | €9,04 |
| Scanner Top20 Long | SHIB | LONG | Scanner Top20 Long | 60m | 2,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €24,14 | €48,29 | €2,71 | €1,41 |
| Scanner Bottom20 Short | ADA | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,16193 | 0,16193 | 0,16426 | 0,24209 | 0,15727 | €1.731,26 | €3.462,51 | €49,86 | €-0,00 |
| Scanner Bottom20 Short | ALLO | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,35250 | 0,35250 | 0,39075 | 0,52699 | 0,27600 | €224,69 | €449,38 | €48,76 | €-0,00 |
| Scanner Bottom20 Short | ESPORTS | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,03342 | 0,02739 | 0,03342 | 0,04997 | 0,02540 | €203,44 | €406,87 | €0,00 | €73,45 |
| Scanner Top 5 + forza BTC 1H | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39694 | 0,39694 | 0,38539 | 0,20045 | 0,42235 | €898,57 | €1.797,15 | €52,29 | €0,00 |
| Scanner Top 5 + forza BTC 1H | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €216,56 | €433,12 | €51,97 | €0,00 |
| Scanner Top 5 + forza BTC 1H | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00319 | 0,00319 | 0,00281 | 0,00161 | 0,00403 | €219,41 | €438,82 | €52,66 | €0,00 |
| Scanner Top 5 + forza BTC 1H | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 381,44484 | €37,16 | €74,32 | €1,36 | €0,00 |
| Top 5 + BTC — solo MFE | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39924 | 0,39924 | 0,38729 | 0,20162 | 0,42552 | €835,46 | €1.670,91 | €50,00 | €0,00 |
| Top 5 + BTC — solo MFE | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 367,08012 | 367,08012 | 360,46822 | 185,37546 | 381,62629 | €1.363,71 | €2.727,43 | €49,13 | €0,00 |
| Top 5 + BTC — solo MFE | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00322 | 0,00322 | 0,00284 | 0,00163 | 0,00407 | €196,51 | €393,01 | €47,16 | €0,00 |
| Top 5 + BTC — solo MFE | EUL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,37027 | 2,28360 | 2,08584 | 1,19699 | 2,99603 | €204,30 | €408,60 | €49,03 | €-14,94 |
| Top 5 + BTC — solo MFE | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €15,66 | €31,33 | €0,00 | €0,69 |
| Top 5 + BTC — Guard | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39724 | 0,39724 | 0,38434 | 0,20061 | 0,42561 | €756,62 | €1.513,24 | €49,13 | €0,00 |
| Top 5 + BTC — Guard | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €202,47 | €404,95 | €48,59 | €0,00 |
| Top 5 + BTC — Guard | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00319 | 0,00319 | 0,00281 | 0,00161 | 0,00403 | €207,86 | €415,72 | €49,89 | €0,00 |
| Top 5 + BTC — BTC≤3 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39974 | 0,39974 | 0,38840 | 0,20187 | 0,42468 | €884,65 | €1.769,29 | €50,18 | €0,00 |
| Top 5 + BTC — BTC≤3 | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €207,87 | €415,74 | €49,89 | €0,00 |
| Top 5 + BTC — BTC≤3 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00319 | 0,00319 | 0,00281 | 0,00161 | 0,00403 | €210,72 | €421,44 | €50,57 | €0,00 |
| Top 5 + BTC — BTC≤3 | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 381,44484 | €37,63 | €75,26 | €1,37 | €0,00 |
| Top 5 + BTC — BTC 2–3 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39974 | 0,39974 | 0,38840 | 0,20187 | 0,42468 | €884,65 | €1.769,29 | €50,18 | €0,00 |
| Top 5 + BTC — BTC 2–3 | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €207,87 | €415,74 | €49,89 | €0,00 |
| Top 5 + BTC — BTC 2–3 | SHIB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €510,10 | €1.020,20 | €49,66 | €-0,20 |
| Top 5 + BTC — BTC 2–3 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €996,29 | €1.992,58 | €48,89 | €-0,40 |
| Top 5 + BTC — Guard + MFE | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39724 | 0,39724 | 0,38434 | 0,20061 | 0,42561 | €756,62 | €1.513,24 | €49,13 | €0,00 |
| Top 5 + BTC — Guard + MFE | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00322 | 0,00322 | 0,00284 | 0,00163 | 0,00407 | €201,88 | €403,77 | €48,45 | €0,00 |
| Top 5 + BTC — Guard + MFE | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,35802 | 0,38400 | 0,36856 | 0,18080 | 0,45073 | €205,20 | €410,40 | €0,00 | €29,78 |
| Top 5 + BTC — Guard + MFE | SHIB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €407,51 | €815,02 | €45,45 | €17,68 |
| Top 5 + BTC — Guard + BTC≤3 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39974 | 0,39974 | 0,38840 | 0,20187 | 0,42468 | €871,05 | €1.742,11 | €49,41 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €205,84 | €411,68 | €49,40 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00319 | 0,00319 | 0,00281 | 0,00161 | 0,00403 | €211,32 | €422,63 | €50,72 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,37568 | 0,38400 | 0,33059 | 0,18972 | 0,47485 | €14,78 | €29,56 | €3,55 | €0,66 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39974 | 0,39974 | 0,38840 | 0,20187 | 0,42468 | €871,05 | €1.742,11 | €49,41 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00322 | 0,00322 | 0,00284 | 0,00163 | 0,00407 | €204,20 | €408,41 | €49,01 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,35802 | 0,38400 | 0,36856 | 0,18080 | 0,45073 | €207,57 | €415,15 | €0,00 | €30,12 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | SHIB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €414,63 | €829,26 | €46,24 | €17,99 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39694 | 0,39694 | 0,38539 | 0,20045 | 0,43159 | €861,83 | €1.723,66 | €50,15 | €0,00 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,21338 | €207,96 | €415,92 | €49,91 | €0,00 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00319 | 0,00319 | 0,00281 | 0,00161 | 0,00434 | €213,22 | €426,44 | €51,17 | €0,00 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 386,79573 | €70,70 | €141,40 | €2,58 | €0,00 |
| Top 5 + BTC — target pieno 3R | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39694 | 0,39694 | 0,38539 | 0,20045 | 0,43159 | €861,83 | €1.723,66 | €50,15 | €0,00 |
| Top 5 + BTC — target pieno 3R | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,21338 | €207,96 | €415,92 | €49,91 | €0,00 |
| Top 5 + BTC — target pieno 3R | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00319 | 0,00319 | 0,00281 | 0,00161 | 0,00434 | €213,56 | €427,11 | €51,25 | €0,00 |
| Top 5 + BTC — target pieno 3R | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 386,79573 | €85,15 | €170,29 | €3,11 | €0,00 |
| Combo Trend | AKE | LONG | Combo Trend | 60m | 2,0x | 0,00329 | 0,00329 | 0,00290 | 0,00166 | 0,00416 | €208,78 | €417,57 | €50,11 | €0,00 |
| Combo Trend | ALLO | SHORT | Combo Trend | 60m | 2,0x | 0,35372 | 0,35372 | 0,39616 | 0,52881 | 0,26034 | €209,35 | €418,70 | €50,24 | €-0,00 |
| Combo Trend | PEPE | LONG | Combo Trend | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €784,30 | €1.568,61 | €47,99 | €2,01 |
| Combo Trend | SHIB | LONG | Combo Trend | 60m | 2,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €338,96 | €677,92 | €43,49 | €-8,44 |
| Combo Mean Reversion | AKE | SHORT | Combo Mean Reversion | 60m | 2,0x | 0,00320 | 0,00320 | 0,00356 | 0,00479 | 0,00263 | €225,46 | €450,91 | €50,00 | €-0,00 |
| Combo Scanner | ONDO | LONG | Combo Scanner | 60m | 2,0x | 0,39694 | 0,39694 | 0,38539 | 0,20045 | 0,42235 | €857,88 | €1.715,77 | €49,92 | €0,00 |
| Combo Scanner | LAB | LONG | Combo Scanner | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €207,54 | €415,08 | €49,81 | €0,00 |
| Combo Scanner | AKE | LONG | Combo Scanner | 60m | 2,0x | 0,00319 | 0,00319 | 0,00281 | 0,00161 | 0,00403 | €210,36 | €420,73 | €50,49 | €0,00 |
| Combo Scanner | XMR | LONG | Combo Scanner | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 381,44484 | €23,89 | €47,78 | €0,87 | €0,00 |
| Combo Adaptive — madre | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,40114 | 0,40114 | 0,38834 | 0,20258 | 0,42673 | €809,25 | €1.618,50 | €51,63 | €0,00 |
| Combo Adaptive — madre | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15861 | 0,13958 | 0,08010 | 0,19668 | €213,13 | €426,26 | €51,15 | €0,00 |
| Combo Adaptive — madre | WLD | SHORT | Combo Adaptive | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,32475 | €929,60 | €1.859,20 | €50,73 | €-0,00 |
| Combo Adaptive — madre | ALLO | SHORT | Combo Adaptive | 60m | 2,0x | 0,36179 | 0,36179 | 0,40521 | 0,54088 | 0,27496 | €210,64 | €421,27 | €50,55 | €-0,00 |
| Combo Adaptive — MFE Trail esistente | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39784 | 0,39784 | 0,38492 | 0,20091 | 0,42367 | €744,71 | €1.489,41 | €48,35 | €0,00 |
| Combo Adaptive — MFE Trail esistente | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15861 | 0,13958 | 0,08010 | 0,19668 | €201,70 | €403,39 | €48,41 | €0,00 |
| Combo Adaptive — MFE Trail esistente | WLD | SHORT | Combo Adaptive | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,32475 | €883,78 | €1.767,56 | €48,23 | €-0,00 |
| Combo Adaptive — MFE Trail esistente | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,00330 | 0,00330 | 0,00293 | 0,00166 | 0,00403 | €203,95 | €407,90 | €45,45 | €0,00 |
| Combo Adaptive — Quality7 | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,40304 | 0,40304 | 0,39140 | 0,20354 | 0,42632 | €859,15 | €1.718,30 | €49,62 | €0,00 |
| Combo Adaptive — Quality7 | WLD | SHORT | Combo Adaptive | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,32475 | €919,99 | €1.839,97 | €50,21 | €-0,00 |
| Combo Adaptive — Quality7 | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,00327 | 0,00327 | 0,00287 | 0,00165 | 0,00405 | €209,81 | €419,62 | €50,35 | €0,00 |
| Combo Adaptive — Quality7 | ALLO | SHORT | Combo Adaptive | 60m | 2,0x | 0,36179 | 0,36179 | 0,40521 | 0,54088 | 0,27496 | €207,61 | €415,23 | €49,83 | €-0,00 |
| Combo Adaptive — Quality7 | SHIB | LONG | Combo Adaptive | 60m | 2,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €12,84 | €25,69 | €1,30 | €0,07 |
| Combo Adaptive — Trend/Transition | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39724 | 0,39724 | 0,38434 | 0,20061 | 0,42303 | €757,94 | €1.515,88 | €49,21 | €0,00 |
| Combo Adaptive — Trend/Transition | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15861 | 0,13958 | 0,08010 | 0,19668 | €206,52 | €413,04 | €49,56 | €0,00 |
| Combo Adaptive — Quality7 + Regime | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,40554 | 0,40554 | 0,39390 | 0,20480 | 0,42882 | €864,27 | €1.728,54 | €49,61 | €0,00 |
| Combo Adaptive — Long Only | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,41951 | €893,67 | €1.787,34 | €49,39 | €0,00 |
| Combo Adaptive — Long Only | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €205,55 | €411,10 | €49,33 | €0,00 |
| Combo Adaptive — Long Only | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,00319 | 0,00319 | 0,00281 | 0,00161 | 0,00396 | €205,22 | €410,44 | €49,25 | €0,00 |
| Combo Adaptive — Long Only | XMR | LONG | Combo Adaptive | 60m | 2,0x | 367,08012 | 367,08012 | 360,46822 | 185,37546 | 380,30391 | €1.384,19 | €2.768,37 | €49,86 | €0,00 |
| Combo Adaptive — Long Only | SHIB | LONG | Combo Adaptive | 60m | 2,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €12,85 | €25,69 | €1,44 | €0,75 |
| Combo Adaptive — parziale 1R | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,41951 | €893,02 | €1.786,04 | €49,36 | €0,00 |
| Combo Adaptive — parziale 1R | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €205,22 | €410,44 | €49,25 | €0,00 |
| Combo Adaptive — parziale 1R | WLD | SHORT | Combo Adaptive | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,32475 | €895,30 | €1.790,60 | €48,86 | €-0,00 |
| Combo Adaptive — parziale 1R | ALLO | SHORT | Combo Adaptive | 60m | 2,0x | 0,36179 | 0,36179 | 0,40521 | 0,54088 | 0,27496 | €98,69 | €197,38 | €23,69 | €-0,00 |
| Combo Adaptive — parziale 1R | ESPORTS | SHORT | Combo Adaptive | 60m | 2,0x | 0,03069 | 0,02739 | 0,03069 | 0,04589 | 0,02333 | €93,74 | €187,49 | €0,00 | €20,18 |
| Combo Adaptive — parziale 1R | ETH | LONG | Combo Adaptive | 60m | 2,0x | 1949,77988 | 1949,39000 | 1921,70305 | 984,63884 | 2005,93354 | €13,89 | €27,78 | €0,40 | €-0,01 |
| Combo Adaptive — Quality7 + Regime + parziale 1R | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,40554 | 0,40554 | 0,39390 | 0,20480 | 0,42882 | €864,27 | €1.728,54 | €49,61 | €0,00 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,43050 | €902,18 | €1.804,37 | €49,86 | €0,00 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | WLD | SHORT | Combo Adaptive | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,31537 | €919,67 | €1.839,35 | €50,19 | €-0,00 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,00327 | 0,00327 | 0,00287 | 0,00165 | 0,00444 | €209,99 | €419,98 | €50,40 | €0,00 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | XMR | LONG | Combo Adaptive | 60m | 2,0x | 367,08012 | 367,08012 | 360,46822 | 185,37546 | 386,91580 | €27,35 | €54,70 | €0,99 | €0,00 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | ALLO | SHORT | Combo Adaptive | 60m | 2,0x | 0,36179 | 0,36179 | 0,40521 | 0,54088 | 0,23155 | €207,78 | €415,57 | €49,87 | €-0,00 |
| Combo Adaptive — target pieno 3R | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,43050 | €902,18 | €1.804,37 | €49,86 | €0,00 |
| Combo Adaptive — target pieno 3R | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15861 | 0,13958 | 0,08010 | 0,21571 | €207,43 | €414,86 | €49,78 | €0,00 |
| Combo Adaptive — target pieno 3R | WLD | SHORT | Combo Adaptive | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,31537 | €911,80 | €1.823,59 | €49,76 | €-0,00 |
| Combo Adaptive — target pieno 3R | ALLO | SHORT | Combo Adaptive | 60m | 2,0x | 0,36179 | 0,36179 | 0,40521 | 0,54088 | 0,23155 | €205,00 | €410,00 | €49,20 | €-0,00 |
| Sol Ema 4H | SOL | SHORT | Trend following EMA | 240m | 2,0x | 75,05699 | 76,48500 | 77,22103 | 112,21019 | 69,64688 | €862,58 | €1.725,17 | €49,74 | €-32,82 |
| Sol Donchian 4H | SOL | SHORT | Donchian breakout 20 barre | 240m | 2,0x | 75,96380 | 76,48500 | 78,23939 | 113,56589 | 69,59218 | €830,21 | €1.660,43 | €49,74 | €-11,39 |
| Sol Adaptive 4H | SOL | SHORT | Combo Adaptive | 240m | 2,0x | 75,96380 | 76,48500 | 78,44626 | 113,56589 | 69,75767 | €761,04 | €1.522,08 | €49,74 | €-10,44 |
| Eth Ema 1H | ETH | LONG | Trend following EMA | 60m | 3,0x | 1958,25157 | 1949,39000 | 1930,05275 | 1315,29231 | 2014,64922 | €1.132,15 | €3.396,44 | €48,91 | €-15,37 |
| Eth Ema 4H | ETH | LONG | Trend following EMA | 240m | 2,0x | 1949,77988 | 1949,39000 | 1902,99144 | 984,63884 | 2066,75096 | €1.036,30 | €2.072,59 | €49,74 | €-0,41 |
| Eth Donchian 1H | ETH | LONG | Donchian breakout 20 barre | 60m | 3,0x | 1958,25157 | 1949,39000 | 1933,18595 | 1315,29231 | 2008,38281 | €1.292,62 | €3.877,86 | €49,64 | €-17,55 |
| Eth Bollinger 1H | ETH | SHORT | Bollinger mean reversion | 60m | 3,0x | 1957,46843 | 1949,39000 | 1980,95805 | 2600,17056 | 1922,23400 | €1.391,03 | €4.173,10 | €50,08 | €17,22 |
| Eth Adaptive 1H | ETH | LONG | Combo Adaptive | 60m | 3,0x | 1958,25157 | 1949,39000 | 1930,05275 | 1315,29231 | 2014,64922 | €1.140,50 | €3.421,49 | €49,27 | €-15,48 |
| Master Adaptive V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39854 | 0,39854 | 0,38677 | 0,20126 | 0,42207 | €833,00 | €1.665,99 | €49,19 | €0,00 |
| Master Adaptive V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €203,80 | €407,60 | €48,91 | €0,00 |
| Master Adaptive V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00319 | 0,00319 | 0,00281 | 0,00161 | 0,00396 | €205,42 | €410,83 | €49,30 | €0,00 |
| Master Adaptive V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10713 | €21,54 | €43,08 | €0,79 | €0,00 |
| Master Adaptive No Alt V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39854 | 0,39854 | 0,38677 | 0,20126 | 0,42207 | €833,00 | €1.665,99 | €49,19 | €0,00 |
| Master Adaptive No Alt V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €203,80 | €407,60 | €48,91 | €0,00 |
| Master Adaptive No Alt V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00319 | 0,00319 | 0,00281 | 0,00161 | 0,00396 | €205,42 | €410,83 | €49,30 | €0,00 |
| Master Adaptive No Alt V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10713 | €21,54 | €43,08 | €0,79 | €0,00 |
| Master Adaptive No Alt V1 | BANK | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39689 | 0,38400 | 0,36072 | 0,20043 | 0,46924 | €254,64 | €509,27 | €46,42 | €-16,54 |
| Master Adaptive Strict3 V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,41951 | €887,07 | €1.774,14 | €49,03 | €0,00 |
| Master Adaptive Strict3 V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00320 | 0,00320 | 0,00282 | 0,00162 | 0,00397 | €201,87 | €403,75 | €48,45 | €0,00 |
| Master Adaptive Strict3 V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10713 | €1.330,61 | €2.661,21 | €48,54 | €0,00 |
| Master Adaptive Strict3 V1 | BANK | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39689 | 0,38400 | 0,36072 | 0,20043 | 0,46924 | €248,50 | €497,01 | €45,30 | €-16,14 |
| Master Adaptive Expanded V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39854 | 0,39854 | 0,38677 | 0,20126 | 0,42207 | €833,00 | €1.665,99 | €49,19 | €0,00 |
| Master Adaptive Expanded V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €203,80 | €407,60 | €48,91 | €0,00 |
| Master Adaptive Expanded V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00319 | 0,00319 | 0,00281 | 0,00161 | 0,00396 | €206,32 | €412,65 | €49,52 | €0,00 |
| Master Adaptive Expanded V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10713 | €33,54 | €67,08 | €1,22 | €0,00 |
| Master Adaptive Gb20 V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,40304 | 0,40304 | 0,39140 | 0,20354 | 0,42632 | €848,64 | €1.697,27 | €49,02 | €0,00 |
| Master Adaptive Gb20 V1 | RIF | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,10582 | 0,10582 | 0,09312 | 0,05344 | 0,13122 | €201,89 | €403,77 | €48,45 | €0,00 |
| Master Adaptive Gb20 V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 367,08012 | 367,08012 | 360,46822 | 185,37546 | 380,30391 | €1.348,01 | €2.696,02 | €48,56 | €0,00 |
| Master Adaptive Gb20 V1 | BANK | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39689 | 0,38400 | 0,36072 | 0,20043 | 0,46924 | €267,30 | €534,60 | €48,73 | €-17,36 |
| Master Adaptive Runner25 V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39854 | 0,39854 | 0,38677 | 0,20126 | 0,43384 | €833,00 | €1.665,99 | €49,19 | €0,00 |
| Master Adaptive Runner25 V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,21338 | €203,80 | €407,60 | €48,91 | €0,00 |
| Master Adaptive Runner25 V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00319 | 0,00319 | 0,00281 | 0,00161 | 0,00434 | €205,36 | €410,73 | €49,29 | €0,00 |
| Master Adaptive Runner25 V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 386,79573 | €20,87 | €41,74 | €0,76 | €0,00 |
| Combo Adaptive — Side × Regime Guard | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,00320 | 0,00320 | 0,00282 | 0,00162 | 0,00397 | €212,78 | €425,56 | €51,07 | €0,00 |
| Combo Adaptive — Side × Regime Guard | BANK | LONG | Combo Adaptive | 60m | 2,0x | 0,37568 | 0,38400 | 0,33059 | 0,18972 | 0,46584 | €212,08 | €424,15 | €50,90 | €9,40 |
| Combo Adaptive — Side × Regime Guard | ALLO | SHORT | Combo Adaptive | 60m | 2,0x | 0,35250 | 0,35250 | 0,39075 | 0,52699 | 0,27600 | €235,86 | €471,72 | €51,19 | €-0,00 |
| Combo Adaptive — Side × Regime Guard | SHIB | LONG | Combo Adaptive | 60m | 2,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €450,93 | €901,86 | €50,61 | €26,33 |
| Combo Adaptive — Side × Regime Guard | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €14,24 | €28,47 | €0,00 | €0,63 |
| Master Adaptive GB20 — Breakeven 0,5R | BEAT | LONG | Master Adaptive Consensus | 60m | 2,0x | 3,29017 | 3,29017 | 3,00714 | 1,66154 | 3,85623 | €291,32 | €582,63 | €50,12 | €0,00 |
| Master Adaptive GB20 — Breakeven 0,5R | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 367,86058 | 367,86058 | 361,23463 | 185,76959 | 381,11249 | €1.403,77 | €2.807,55 | €50,57 | €0,00 |
| Master Adaptive GB20 — Breakeven 0,5R | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00317 | 0,00317 | 0,00283 | 0,00160 | 0,00387 | €231,91 | €463,82 | €50,56 | €0,00 |
| Master Adaptive GB20 — 50% a 0,75R | BEAT | LONG | Master Adaptive Consensus | 60m | 2,0x | 3,29017 | 3,29017 | 3,00714 | 1,66154 | 3,85623 | €291,05 | €582,09 | €50,07 | €0,00 |
| Master Adaptive GB20 — 50% a 0,75R | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10713 | €1.376,47 | €2.752,95 | €50,21 | €0,00 |
| Master Adaptive GB20 — 50% a 0,75R | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00322 | 0,00322 | 0,00284 | 0,00163 | 0,00400 | €209,67 | €419,35 | €50,32 | €0,00 |
| Master Adaptive GB20 — 50% a 0,75R | BANK | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,37759 | 0,38400 | 0,33768 | 0,19068 | 0,45741 | €219,98 | €439,96 | €46,50 | €7,47 |
| Master Adaptive GB20 — Loss Cap 0,75R | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00275 | 0,00275 | 0,00242 | 0,00139 | 0,00362 | €208,32 | €416,65 | €50,00 | €0,00 |
| Master Adaptive GB20 — Loss Cap 0,75R | BEAT | LONG | Master Adaptive Consensus | 60m | 2,0x | 3,29017 | 3,29017 | 3,07790 | 1,66154 | 3,85623 | €388,25 | €776,50 | €50,10 | €0,00 |
| Master Adaptive GB20 — Loss Cap 0,75R | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 361,71345 | 185,19860 | 380,10713 | €1.835,86 | €3.671,71 | €50,22 | €0,00 |
| Rapida V3 NoHigh — Range Only | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00320 | 0,00320 | 0,00286 | 0,00215 | 0,00370 | €161,22 | €483,65 | €50,91 | €0,00 |
| Rapida V3 NoHigh — Range Only | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,33165 | 0,33165 | 0,36472 | 0,44055 | 0,28205 | €170,92 | €512,75 | €51,13 | €-0,00 |
| Rapida V3 NoHigh — Range Only | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,39689 | 0,38400 | 0,36875 | 0,26658 | 0,43909 | €241,54 | €724,62 | €51,37 | €-23,53 |
| Rapida V3 NoHigh — Range Only | ESPORTS | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,02828 | 0,02739 | 0,03168 | 0,03757 | 0,02319 | €142,68 | €428,04 | €51,37 | €13,53 |
| Rapida V3 NoHigh — Regime Guard | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00320 | 0,00320 | 0,00286 | 0,00215 | 0,00370 | €161,22 | €483,65 | €50,91 | €0,00 |
| Rapida V3 NoHigh — Regime Guard | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,33165 | 0,33165 | 0,36472 | 0,44055 | 0,28205 | €172,19 | €516,57 | €51,51 | €-0,00 |
| Rapida V3 NoHigh — Regime Guard | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,35851 | 0,38400 | 0,37110 | 0,24080 | 0,40774 | €188,19 | €564,57 | €0,00 | €40,14 |
| Rapida V3 NoHigh — Regime Guard | EUL | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,41608 | 2,28360 | 2,12615 | 1,62280 | 2,85098 | €143,73 | €431,18 | €51,74 | €-23,64 |
| Rapida V3 NoHigh — Regime Guard | SHIB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €15,44 | €46,31 | €2,01 | €1,00 |
| MAIN — Side × Regime Guard | AKE | LONG | Confluenza trend | 240m | 3,0x | 0,00322 | 0,00322 | 0,00284 | 0,00216 | 0,00400 | €140,56 | €421,69 | €50,60 | €0,00 |
| MAIN — Side × Regime Guard | ALLO | SHORT | Confluenza trend | 240m | 3,0x | 0,38070 | 0,38070 | 0,37357 | 0,50570 | 0,28933 | €140,03 | €420,08 | €0,00 | €-0,00 |
| MAIN — Dynamic Asset Selector | AKE | LONG | Confluenza trend | 240m | 3,0x | 0,00322 | 0,00322 | 0,00284 | 0,00216 | 0,00400 | €140,56 | €421,69 | €50,60 | €0,00 |
| Combo Trend — Side × Regime Guard | AKE | LONG | Combo Trend | 60m | 2,0x | 0,00320 | 0,00320 | 0,00282 | 0,00162 | 0,00405 | €211,52 | €423,03 | €50,76 | €0,00 |
| Combo Trend — Side × Regime Guard | BANK | LONG | Combo Trend | 60m | 2,0x | 0,37568 | 0,38400 | 0,33059 | 0,18972 | 0,47485 | €207,08 | €414,15 | €49,70 | €9,18 |
| Combo Trend — Side × Regime Guard | ALLO | SHORT | Combo Trend | 60m | 2,0x | 0,35250 | 0,35250 | 0,39480 | 0,52699 | 0,25944 | €209,77 | €419,55 | €50,35 | €-0,00 |
| Combo Trend — Side × Regime Guard | SHIB | LONG | Combo Trend | 60m | 2,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €14,70 | €29,40 | €1,89 | €-0,37 |
| Combo Trend — Side × Regime Guard | ESPORTS | SHORT | Combo Trend | 60m | 2,0x | 0,03069 | 0,02739 | 0,03069 | 0,04589 | 0,02259 | €205,79 | €411,58 | €0,00 | €44,30 |
| Combo Trend — Side × Regime Guard | PEPE | LONG | Combo Trend | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €12,55 | €25,09 | €0,84 | €0,31 |
| Combo Trend — Side × Regime Guard | ETH | LONG | Combo Trend | 60m | 2,0x | 1949,77988 | 1949,39000 | 1918,58340 | 984,63884 | 2018,41213 | €12,70 | €25,41 | €0,41 | €-0,01 |
| FAST NoHigh <7,5 · SHORT only | WLD | SHORT | Momentum / breakout | 60m | 3,0x | 0,34959 | 0,34959 | 0,35668 | 0,46437 | 0,33896 | €822,35 | €2.467,06 | €50,00 | €-0,00 |
| FAST NoHigh <7,5 · SHORT only | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00314 | 0,00314 | 0,00287 | 0,00211 | 0,00354 | €200,24 | €600,71 | €51,24 | €0,00 |
| FAST NoHigh <7,5 · SHORT only | ALLO | SHORT | Momentum / breakout | 60m | 3,0x | 0,33808 | 0,33808 | 0,36389 | 0,44909 | 0,29937 | €212,58 | €637,75 | €48,69 | €-0,00 |
| FAST NoHigh <7,5 · SHORT only | ESPORTS | SHORT | Momentum / breakout | 60m | 3,0x | 0,03069 | 0,02739 | 0,03069 | 0,04077 | 0,02517 | €137,37 | €412,10 | €0,00 | €44,36 |
| FAST NoHigh <7,5 · SHORT only | SHIB | LONG | Momentum / breakout | 60m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €25,54 | €76,62 | €3,32 | €1,66 |
| Bilanciata V3 · LONG only | XMR | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 366,72991 | 366,72991 | 360,04130 | 246,32025 | 380,10712 | €913,56 | €2.740,69 | €49,99 | €0,00 |
| Bilanciata V3 · LONG only | AKE | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,00328 | 0,00328 | 0,00288 | 0,00220 | 0,00406 | €137,93 | €413,80 | €49,66 | €0,00 |
| Bilanciata V3 · LONG only | ALLO | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,34255 | 0,34255 | 0,37914 | 0,45502 | 0,26938 | €156,01 | €468,04 | €49,99 | €-0,00 |
| Bilanciata V3 · LONG only | ESPORTS | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,03342 | 0,02739 | 0,03342 | 0,04440 | 0,02540 | €137,40 | €412,21 | €0,00 | €74,41 |
| Bilanciata V3 · LONG only | ETH | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1958,25157 | 1949,39000 | 1930,05275 | 1315,29231 | 2014,64922 | €32,22 | €96,65 | €1,39 | €-0,44 |
| Scanner Bottom5 Short Profit Lock V1 | WLD | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,34449 | 0,34449 | 0,35368 | 0,51502 | 0,32613 | €937,87 | €1.875,74 | €50,00 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | ALLO | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,35250 | 0,35250 | 0,39075 | 0,52699 | 0,27600 | €227,60 | €455,20 | €49,39 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | ESPORTS | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,03342 | 0,02739 | 0,03262 | 0,04997 | 0,02540 | €206,07 | €412,14 | €0,00 | €74,40 |
| Scanner Bottom5 Short Mfe Trail V1 | WLD | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,34449 | 0,34449 | 0,35368 | 0,51502 | 0,32613 | €937,87 | €1.875,74 | €50,00 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | ALLO | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,35653 | 0,35653 | 0,39522 | 0,53301 | 0,27915 | €228,22 | €456,45 | €49,53 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | ESPORTS | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,02828 | 0,02739 | 0,03168 | 0,04229 | 0,02150 | €206,75 | €413,50 | €49,62 | €13,07 |
| Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00323 | 0,00323 | 0,00290 | 0,00217 | 0,00390 | €162,23 | €486,68 | €50,00 | €0,00 |
| Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,36220 | 0,38400 | 0,36964 | 0,24328 | 0,43158 | €179,05 | €537,16 | €0,00 | €32,33 |
| Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | EUL | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,38098 | 2,28360 | 2,09526 | 1,59922 | 2,95241 | €141,90 | €425,69 | €51,08 | €-17,41 |
| Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | SHIB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €392,53 | €1.177,60 | €51,08 | €25,54 |
| Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1958,25157 | 1949,39000 | 1936,31915 | 1315,29231 | 2002,11641 | €29,43 | €88,30 | €0,99 | €-0,40 |
| Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00320 | 0,00320 | 0,00287 | 0,00215 | 0,00386 | €162,16 | €486,47 | €49,98 | €0,00 |
| Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,35851 | 0,38400 | 0,37110 | 0,24080 | 0,42415 | €182,46 | €547,38 | €0,00 | €38,92 |
| Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,35250 | 0,35250 | 0,38225 | 0,46824 | 0,29300 | €194,51 | €583,53 | €49,25 | €-0,00 |
| Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | EUL | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,41608 | 2,28360 | 2,12615 | 1,62280 | 2,99594 | €134,64 | €403,91 | €48,47 | €-22,15 |
| Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,39689 | 0,38400 | 0,36875 | 0,26658 | 0,45316 | €238,82 | €716,46 | €50,79 | €-23,27 |
| Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | ESPORTS | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,02828 | 0,02739 | 0,03168 | 0,03757 | 0,02150 | €141,08 | €423,23 | €50,79 | €13,38 |
| Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | SHIB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €390,30 | €1.170,89 | €50,79 | €25,40 |
| Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | EUL | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,28506 | 2,28360 | 2,01085 | 1,53480 | 2,83347 | €141,00 | €423,00 | €50,76 | €-0,27 |
| Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00323 | 0,00323 | 0,00290 | 0,00217 | 0,00390 | €162,03 | €486,10 | €49,94 | €0,00 |
| Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,35851 | 0,38400 | 0,37110 | 0,24080 | 0,42415 | €180,97 | €542,91 | €0,00 | €38,60 |
| Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,35250 | 0,35250 | 0,38225 | 0,46824 | 0,29300 | €190,72 | €572,15 | €48,29 | €-0,00 |
| Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | EUL | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,38098 | 2,28360 | 2,09526 | 1,59922 | 2,95241 | €13,07 | €39,20 | €4,70 | €-1,60 |
| Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | SHIB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €390,89 | €1.172,67 | €50,86 | €25,43 |
| Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00317 | 0,00317 | 0,00290 | 0,00213 | 0,00371 | €196,95 | €590,84 | €50,09 | €0,00 |
| Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,33808 | 0,33808 | 0,36389 | 0,44909 | 0,28646 | €211,10 | €633,31 | €48,35 | €-0,00 |
| Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | EUL | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,38098 | 2,28360 | 2,09526 | 1,59922 | 2,95241 | €13,29 | €39,86 | €4,78 | €-1,63 |
| Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | SHIB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €395,12 | €1.185,37 | €0,00 | €25,71 |
| Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,39859 | 0,38400 | 0,37039 | 0,26772 | 0,45500 | €239,80 | €719,40 | €50,91 | €-26,33 |
| Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00320 | 0,00320 | 0,00287 | 0,00215 | 0,00386 | €162,21 | €486,64 | €50,00 | €0,00 |
| Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,35851 | 0,38400 | 0,37110 | 0,24080 | 0,42415 | €184,35 | €553,05 | €0,00 | €39,32 |
| Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | EUL | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,41608 | 2,28360 | 2,12615 | 1,62280 | 2,99594 | €134,09 | €402,27 | €48,27 | €-22,06 |
| Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | SHIB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €386,01 | €1.158,04 | €50,23 | €25,12 |
| Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1958,25157 | 1949,39000 | 1936,31915 | 1315,29231 | 2002,11641 | €60,72 | €182,15 | €2,04 | €-0,82 |
| Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00319 | 0,00319 | 0,00287 | 0,00215 | 0,00385 | €162,18 | €486,55 | €49,99 | €0,00 |
| Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,35851 | 0,38400 | 0,37110 | 0,24080 | 0,42415 | €188,32 | €564,95 | €0,00 | €40,17 |
| Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | EUL | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,38098 | 2,28360 | 2,09526 | 1,59922 | 2,95241 | €143,72 | €431,16 | €51,74 | €-17,63 |
| Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | SHIB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €397,61 | €1.192,82 | €51,74 | €25,87 |
| Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1958,25157 | 1949,39000 | 1936,31915 | 1315,29231 | 2002,11641 | €60,52 | €181,56 | €2,03 | €-0,82 |
| Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00320 | 0,00320 | 0,00287 | 0,00215 | 0,00386 | €162,16 | €486,47 | €49,98 | €0,00 |
| Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,35851 | 0,38400 | 0,37110 | 0,24080 | 0,42415 | €182,46 | €547,38 | €0,00 | €38,92 |
| Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,35250 | 0,35250 | 0,38225 | 0,46824 | 0,29300 | €194,51 | €583,53 | €49,25 | €-0,00 |
| Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | EUL | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,41608 | 2,28360 | 2,12615 | 1,62280 | 2,99594 | €134,64 | €403,91 | €48,47 | €-22,15 |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00320 | 0,00320 | 0,00287 | 0,00215 | 0,00386 | €162,23 | €486,68 | €50,00 | €0,00 |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,33713 | 0,33713 | 0,36471 | 0,44782 | 0,28197 | €208,24 | €624,73 | €51,11 | €-0,00 |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,38680 | 0,38400 | 0,35294 | 0,25980 | 0,45452 | €193,81 | €581,44 | €50,90 | €-4,21 |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | ESPORTS | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,03069 | 0,02739 | 0,03069 | 0,04077 | 0,02333 | €140,11 | €420,32 | €0,00 | €45,24 |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | XRP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,11443 | 1,11110 | 1,10195 | 0,74853 | 1,13940 | €23,07 | €69,20 | €0,78 | €-0,21 |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1952,19036 | 1949,39000 | 1930,32583 | 1311,22119 | 1995,91942 | €12,06 | €36,18 | €0,41 | €-0,05 |
| Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | SHIB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €430,29 | €1.290,86 | €50,94 | €3,63 |
| Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1958,25157 | 1949,39000 | 1936,31915 | 1315,29231 | 2002,11641 | €1.517,19 | €4.551,57 | €50,98 | €-20,60 |
| Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | XRP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,11443 | 1,11110 | 1,10195 | 0,74853 | 1,13940 | €1.516,65 | €4.549,94 | €50,96 | €-13,61 |
| Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | PEPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €875,94 | €2.627,83 | €50,14 | €-0,53 |
| Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00320 | 0,00320 | 0,00289 | 0,00215 | 0,00382 | €172,57 | €517,70 | €50,00 | €0,00 |
| Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,36220 | 0,38400 | 0,37087 | 0,24328 | 0,43158 | €178,81 | €536,42 | €0,00 | €32,28 |
| Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | EUL | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,41608 | 2,28360 | 2,12615 | 1,62280 | 2,99594 | €142,69 | €428,08 | €51,37 | €-23,47 |
| Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | SHIB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €10,87 | €32,61 | €1,41 | €0,71 |
| Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1958,25157 | 1949,39000 | 1936,31915 | 1315,29231 | 2002,11641 | €1.532,67 | €4.598,01 | €51,50 | €-20,81 |
| Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00317 | 0,00317 | 0,00290 | 0,00213 | 0,00371 | €200,37 | €601,11 | €50,97 | €0,00 |
| Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,35250 | 0,35250 | 0,38225 | 0,46824 | 0,29300 | €200,65 | €601,96 | €50,80 | €-0,00 |
| Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,35159 | 0,38400 | 0,36930 | 0,23615 | 0,41964 | €169,91 | €509,73 | €0,00 | €46,99 |
| Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | ESPORTS | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,03342 | 0,02739 | 0,03342 | 0,04440 | 0,02540 | €136,12 | €408,37 | €0,00 | €73,72 |
| Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | SHIB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €36,61 | €109,84 | €4,76 | €2,38 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | ETH | LONG | 2026-07-26T23:23:38+00:00 | 1953,74498 | €0,96 | 1,87 | TARGET |
| Btc Bollinger 1H | BTC | LONG | 2026-07-26T22:53:38+00:00 | 65266,25771 | €68,16 | 1,35 | TARGET |
| Benchmark Bollinger mean reversion 1H | BTC | LONG | 2026-07-26T22:53:38+00:00 | 65266,25771 | €65,39 | 1,35 | TARGET |
| Rapida V3 — senza ESPORTS | ETH | LONG | 2026-07-26T22:53:38+00:00 | 1943,04371 | €0,58 | 1,37 | TARGET |
| Rapida V3 — no volatilità HIGH | ETH | LONG | 2026-07-26T22:53:38+00:00 | 1943,04371 | €0,58 | 1,37 | TARGET |
| Rapida 1H V3 Filtered — madre | ETH | LONG | 2026-07-26T22:53:38+00:00 | 1943,04371 | €0,59 | 1,37 | TARGET |
| Rapida V1 — Long + BTC 1–3 + score <7,5 | ETH | LONG | 2026-07-26T22:53:38+00:00 | 1943,04371 | €69,05 | 1,37 | TARGET |
| Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | ETH | LONG | 2026-07-26T22:53:38+00:00 | 1942,64171 | €94,95 | 1,87 | TARGET |
| Bilanciata 1H V1 | ONDO | LONG | 2026-07-26T22:38:37+00:00 | 0,39670 | €-3,05 | -0,06 | TIME_EXIT_NO_CANDLES |
| Combo Mean Reversion | BTC | LONG | 2026-07-26T22:23:37+00:00 | 64987,18585 | €69,56 | 1,45 | TARGET |
| Btc Ema 1H | BTC | SHORT | 2026-07-26T22:23:37+00:00 | 65056,81692 | €-53,81 | -1,08 | STOP |
| Rapida V3 — qualità completa + profit lock | ETH | LONG | 2026-07-26T22:23:37+00:00 | 1932,00127 | €68,14 | 1,37 | TARGET |

## Regole invarianti

- Nessuna martingala e nessuna mediazione automatica in perdita.
- Il target mensile riduce il rischio quando viene avvicinato o raggiunto; non lo aumenta mai.
- Il portafoglio principale e le simulazioni di confronto hanno contabilità separata.
- Commissioni, slippage e funding sono inclusi nella simulazione secondo i parametri configurati.
- Quando stop e target risultano toccati nella stessa candela, prevale lo stop salvo modifica esplicita della configurazione.

## 🧪 Validazione congiunta Research + Paper

I due campioni vengono letti insieme ma **non sommati**: il paper è normalmente un sottoinsieme dei segnali Research. La soglia usa gli **eventi di mercato indipendenti**.

Requisiti per la revisione live: almeno **30 eventi indipendenti per lato**, PF almeno **1,10**, expectancy positiva e max drawdown paper non superiore a **15,00%**.

| Profilo | Conto paper di riferimento | Research eventi | Paper eventi | PF Research | PF Paper | Exp. Research | Exp. Paper | DD Paper | Accordo | Stato |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 8/30 | 10/30 | 1,84 | 2,96 | 0,44R | €15,19 | 2,01% | COERENTE + | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 7/30 | 10/30 | 1,37 | 3,16 | 0,22R | €28,23 | 1,34% | COERENTE + | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 7/30 | 10/30 | 1,37 | 2,35 | 0,22R | €18,17 | 1,52% | COERENTE + | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 7/30 | 11/30 | 1,38 | 1,02 | 0,22R | €0,51 | 1,92% | COERENTE + | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 1/30 | 4/30 | ∞ | 414,09 | 1,96R | €39,50 | 0,78% | COERENTE + | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 6/30 | 11/30 | 3,71 | 2,91 | 0,94R | €10,59 | 1,01% | COERENTE + | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 10/30 | 9/30 | 1,87 | 0,46 | 0,45R | €-15,49 | 2,51% | DIVERGENTE | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 7/30 | 10/30 | 4,62 | 6,04 | 1,08R | €30,52 | 1,23% | COERENTE + | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 8/30 | 15/30 | 3,11 | 2,64 | 0,81R | €18,00 | 1,08% | COERENTE + | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 4/30 | 6/30 | 5,50 | 4,44 | 1,17R | €31,30 | 0,73% | COERENTE + | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 8/30 | 13/30 | 1,85 | 1,51 | 0,44R | €9,17 | 1,60% | COERENTE + | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 10/30 | 9/30 | 1,87 | 0,46 | 0,45R | €-15,49 | 2,51% | DIVERGENTE | RACCOLTA RESEARCH |
| MAIN | Principale 4H | 64/30 | 21/30 | 1,08 | 0,68 | 0,05R | €-11,50 | 4,49% | DIVERGENTE | BOCCIATA RESEARCH |
| MAIN_DYNAMIC_ASSET_SELECTOR_V1 | MAIN — Dynamic Asset Selector | 0/30 | 4/30 | 0,00 | 3,55 | 0,00R | €35,68 | 1,03% | n/a | RACCOLTA RESEARCH |
| MAIN_SIDE_REGIME_GUARD_V1 | MAIN — Side × Regime Guard | 0/30 | 5/30 | 0,00 | 1,81 | 0,00R | €17,72 | 1,48% | n/a | RACCOLTA RESEARCH |
| RSI_EXTREME_LONG_15M | Scalp RSI Long 25 · prudente · 5x (riferimento tra 9 varianti) | 10/30 | 5/30 | 0,31 | 0,20 | -0,54R | €-4,60 | 0,37% | COERENTE − | RACCOLTA RESEARCH |
| RSI_EXTREME_SHORT_15M | Scalp RSI Short 75 · prudente · 5x (riferimento tra 9 varianti) | 11/30 | 9/30 | 0,38 | 0,16 | -0,46R | €-6,21 | 0,56% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_1H_BALANCED | Bilanciata 1H V1 | 176/30 | 47/30 | 1,00 | 1,39 | 0,00R | €7,79 | 2,76% | COERENTE + | BOCCIATA RESEARCH |
| SHADOW_1H_BALANCED_LONG_NO_RHV_V1 | Bilanciata 1H — LONG senza Range High Vol | 0/30 | 9/30 | 0,00 | 0,60 | 0,00R | €-14,47 | 2,37% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_BALANCED_SHORT_TREND_DOWN_STRICT_V1 | Bilanciata 1H — SHORT Trend Down stretto | 0/30 | 1/30 | 0,00 | 0,00 | 0,00R | €-4,13 | 0,59% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_BALANCED_V2 | Bilanciata 1H V2 | 47/30 | 32/30 | 1,39 | 1,13 | 0,23R | €2,82 | 2,75% | COERENTE + | PRONTA PER REVISIONE LIVE |
| SHADOW_1H_BALANCED_V3 | Bilanciata 1H V3 Filtered | 79/30 | 46/30 | 1,13 | 1,62 | 0,08R | €12,64 | 2,20% | COERENTE + | PRONTA PER REVISIONE LIVE |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | Bilanciata V3 · LONG only | 4/30 | 7/30 | 0,62 | 0,74 | -0,30R | €-6,19 | 1,46% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_1H_FAST | Rapida 1H V1 — madre | 204/30 | 76/30 | 0,92 | 0,99 | -0,05R | €-0,31 | 6,76% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | Rapida V1 — Long + BTC 1–3 + score <7,5 | 16/30 | 15/30 | 2,08 | 1,55 | 0,43R | €8,75 | 1,92% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | FAST NoHigh <7,5 · SHORT only | 14/30 | 15/30 | 2,49 | 1,44 | 0,56R | €7,02 | 1,76% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | Rapida V1 — no HIGH + score <7,5 | 78/30 | 50/30 | 1,23 | 1,54 | 0,13R | €10,24 | 2,83% | COERENTE + | PRONTA PER REVISIONE LIVE |
| SHADOW_1H_FAST_NO_PEPE_V1 | Rapida V1 — senza PEPE | 81/30 | 42/30 | 1,04 | 1,12 | 0,02R | €2,51 | 2,15% | COERENTE + | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_COST_AWARE_V1 | Rapida score 6–7,5 — Cost Aware | 0/30 | 12/30 | 0,00 | 2,34 | 0,00R | €24,54 | 1,95% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_NO_TREND_UP_V1 | Rapida score 6–7,5 — senza Trend Up | 0/30 | 14/30 | 0,00 | 1,91 | 0,00R | €15,94 | 2,01% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_RANGE_ONLY_V1 | Rapida score 6–7,5 — Range Only | 0/30 | 9/30 | 0,00 | 3,17 | 0,00R | €33,01 | 2,28% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_V1 | Rapida V1 — score 6–7,5 | 57/30 | 48/30 | 1,29 | 1,36 | 0,16R | €6,97 | 2,49% | COERENTE + | PRONTA PER REVISIONE LIVE |
| SHADOW_1H_FAST_TP2_V1 | Rapida V1 — target pieno 2R | 76/30 | 47/30 | 0,99 | 1,02 | -0,01R | €0,38 | 2,58% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V2 | Rapida 1H V2 | 11/30 | 12/30 | 0,63 | 1,39 | -0,27R | €7,56 | 1,69% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3 | Rapida 1H V3 Filtered — madre | 123/30 | 74/30 | 1,15 | 1,11 | 0,09R | €2,21 | 2,89% | COERENTE + | PRONTA PER REVISIONE LIVE |
| SHADOW_1H_FAST_V3_CAP75_V1 | Rapida V3 — score <7,5 | 67/30 | 45/30 | 1,15 | 1,55 | 0,09R | €9,29 | 2,49% | COERENTE + | PRONTA PER REVISIONE LIVE |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | Rapida V3 — qualità completa + profit lock | 35/30 | 37/30 | 1,16 | 0,98 | 0,09R | €-0,55 | 3,21% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | Rapida V3 — Long + no HIGH + score <7,5 | 35/30 | 35/30 | 1,16 | 1,02 | 0,09R | €0,35 | 2,86% | COERENTE + | BOCCIATA PAPER |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | Rapida V3 — Long Only | 44/30 | 39/30 | 1,15 | 0,76 | 0,09R | €-6,10 | 3,65% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V1 | Rapida V3 NoHigh — Range Only | 0/30 | 8/30 | 0,00 | 3,50 | 0,00R | €34,29 | 1,78% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_V1 | Rapida V3 NoHigh — Regime Guard | 0/30 | 14/30 | 0,00 | 4,13 | 0,00R | €25,23 | 1,39% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | Rapida V3 — no volatilità HIGH | 78/30 | 49/30 | 1,15 | 0,94 | 0,08R | €-1,43 | 2,96% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONLY_V1 | Rapida V3 senza ESPORTS — Long Only | 0/30 | 15/30 | 0,00 | 1,74 | 0,00R | €11,05 | 1,32% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_V1 | Rapida V3 senza ESPORTS — MFE Lock | 0/30 | 22/30 | 0,00 | 2,15 | 0,00R | €12,63 | 2,05% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_GUARD_V1 | Rapida V3 senza ESPORTS — Stress Guard | 0/30 | 11/30 | 0,00 | 1,73 | 0,00R | €14,53 | 1,29% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | Rapida V3 — senza ESPORTS | 77/30 | 48/30 | 1,05 | 0,96 | 0,03R | €-0,90 | 2,49% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_4H_WIDE | Ampia 4H | 51/30 | 17/30 | 1,03 | 0,89 | 0,02R | €-3,14 | 3,67% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_BOLLINGER_MR_1H | Benchmark Bollinger mean reversion 1H | 49/30 | 37/30 | 1,16 | 0,93 | 0,09R | €-1,67 | 4,19% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_BTC_ADAPTIVE_1H | Btc Adaptive 1H | 4/30 | 3/30 | 0,00 | 1,24 | -1,11R | €4,43 | 0,89% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_BTC_ADAPTIVE_4H | Btc Adaptive 4H | 1/30 | 1/30 | 0,00 | 0,00 | -1,07R | €-50,38 | 0,74% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_BOLLINGER_1H | Btc Bollinger 1H | 3/30 | 3/30 | ∞ | ∞ | 1,37R | €56,04 | 0,54% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_BTC_BOLLINGER_4H | Btc Bollinger 4H | 1/30 | 1/30 | ∞ | ∞ | 1,72R | €84,12 | 0,30% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_BTC_DONCHIAN_1H | Btc Donchian 1H | 5/30 | 4/30 | 0,00 | 0,82 | -1,12R | €-4,84 | 1,49% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_DONCHIAN_4H | Btc Donchian 4H | 1/30 | 1/30 | 0,00 | 0,00 | -1,07R | €-49,32 | 0,96% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_EMA_1H | Btc Ema 1H | 4/30 | 6/30 | 0,57 | 0,59 | -0,36R | €-14,69 | 1,56% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_EMA_4H | Btc Ema 4H | 1/30 | 1/30 | 0,00 | 0,00 | -1,07R | €-49,32 | 0,96% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE | Combo Adaptive — madre | 123/30 | 25/30 | 1,13 | 1,52 | 0,08R | €8,26 | 1,49% | COERENTE + | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | Combo Adaptive — Long Only | 36/30 | 10/30 | 0,93 | 0,86 | -0,05R | €-3,28 | 2,34% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | Combo Adaptive — MFE Trail esistente | 90/30 | 29/30 | 1,03 | 0,39 | 0,02R | €-16,40 | 5,33% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | Combo Adaptive — parziale 1R | 64/30 | 17/30 | 0,89 | 0,47 | -0,08R | €-18,47 | 3,32% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | Combo Adaptive — Quality7 + Regime + parziale 1R | 5/30 | 5/30 | 0,46 | 0,48 | -0,46R | €-16,52 | 1,95% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | Combo Adaptive — Quality7 + Regime | 5/30 | 5/30 | 0,46 | 0,17 | -0,46R | €-28,67 | 1,95% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | Combo Adaptive — Quality7 | 18/30 | 16/30 | 1,20 | 1,38 | 0,13R | €4,31 | 1,51% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | Combo Adaptive — Trend/Transition | 29/30 | 10/30 | 0,38 | 0,92 | -0,55R | €-2,35 | 2,18% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | Combo Adaptive — 75% a 2R + runner 25% a 3R | 40/30 | 22/30 | 0,58 | 1,17 | -0,37R | €3,48 | 2,12% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_SIDE_REGIME_GUARD_V1 | Combo Adaptive — Side × Regime Guard | 0/30 | 10/30 | 0,00 | 2,69 | 0,00R | €18,24 | 1,41% | n/a | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | Combo Adaptive — target pieno 3R | 40/30 | 13/30 | 0,58 | 0,76 | -0,37R | €-5,13 | 1,41% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_MEAN_REVERSION | Combo Mean Reversion | 18/30 | 16/30 | 1,12 | 1,36 | 0,07R | €8,67 | 2,31% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_COMBO_SCANNER | Combo Scanner | 73/30 | 33/30 | 1,52 | 0,93 | 0,30R | €-2,05 | 2,75% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_COMBO_TREND | Combo Trend | 96/30 | 38/30 | 1,04 | 0,71 | 0,03R | €-11,03 | 7,02% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_COMBO_TREND_SIDE_REGIME_GUARD_V1 | Combo Trend — Side × Regime Guard | 0/30 | 10/30 | 0,00 | 1,69 | 0,00R | €11,47 | 1,32% | n/a | RACCOLTA RESEARCH |
| SHADOW_DOGE_BOLLINGER_1H | Doge Bollinger 1H | 2/30 | 2/30 | 0,00 | 0,00 | -1,12R | €-55,56 | 1,26% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_DOGE_DONCHIAN_1H | Doge Donchian 1H | 3/30 | 4/30 | 0,84 | 0,98 | -0,12R | €-0,31 | 0,96% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_DOGE_EMA_1H | Doge Ema 1H | 4/30 | 8/30 | 1,71 | 1,55 | 0,39R | €11,48 | 1,36% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_DONCHIAN_1H | Benchmark Donchian breakout 1H | 58/30 | 26/30 | 0,90 | 1,89 | -0,08R | €18,18 | 2,12% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_EMA_TREND_1H | Benchmark trend following EMA 1H | 100/30 | 26/30 | 1,06 | 0,94 | 0,04R | €-1,31 | 2,25% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_ETH_ADAPTIVE_1H | Eth Adaptive 1H | 5/30 | 5/30 | 0,42 | 0,11 | -0,51R | €-29,22 | 1,68% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_BOLLINGER_1H | Eth Bollinger 1H | 1/30 | 1/30 | 0,00 | ∞ | -1,13R | €15,45 | 0,51% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_ETH_DONCHIAN_1H | Eth Donchian 1H | 4/30 | 4/30 | 0,56 | 0,56 | -0,37R | €-18,17 | 1,38% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_EMA_1H | Eth Ema 1H | 5/30 | 7/30 | 0,43 | 0,20 | -0,51R | €-31,18 | 2,36% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_EMA_4H | Eth Ema 4H | 1/30 | 1/30 | 0,00 | 0,00 | -1,06R | €-52,88 | 0,70% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_GLOBAL_PURE | Global Confluence puro 1H | 4/30 | 10/30 | 1,75 | 0,37 | 0,41R | €-20,93 | 2,92% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | Master Adaptive Expanded V1 | 31/30 | 12/30 | 0,89 | 0,51 | -0,07R | €-22,98 | 3,05% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_BE_V1 | Master Adaptive GB20 — Breakeven 0,5R | 0/30 | 11/30 | 0,00 | 0,64 | 0,00R | €-10,36 | 2,56% | n/a | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_LOSS_CAP_V1 | Master Adaptive GB20 — Loss Cap 0,75R | 0/30 | 7/30 | 0,00 | 0,47 | 0,00R | €-21,63 | 2,99% | n/a | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_PARTIAL_V1 | Master Adaptive GB20 — 50% a 0,75R | 0/30 | 6/30 | 0,00 | 0,49 | 0,00R | €-23,78 | 2,42% | n/a | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | Master Adaptive Gb20 V1 | 31/30 | 45/30 | 0,77 | 0,67 | -0,17R | €-5,60 | 4,16% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | Master Adaptive No Alt V1 | 29/30 | 8/30 | 0,85 | 0,42 | -0,11R | €-33,56 | 3,21% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | Master Adaptive Runner25 V1 | 24/30 | 11/30 | 0,75 | 0,40 | -0,21R | €-28,22 | 3,40% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | Master Adaptive Strict3 V1 | 27/30 | 18/30 | 0,80 | 0,52 | -0,15R | €-23,99 | 4,77% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_V1 | Master Adaptive V1 | 31/30 | 9/30 | 0,77 | 0,38 | -0,17R | €-35,52 | 3,49% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_RELATIVE_STRENGTH | Forza relativa 1H V1 | 127/30 | 27/30 | 1,00 | 0,56 | -0,00R | €-13,41 | 5,74% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_RELATIVE_STRENGTH_V2 | Forza relativa 1H V2 | 46/30 | 39/30 | 1,52 | 0,96 | 0,31R | €-1,46 | 5,10% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_SCANNER_BOTTOM10_SHORT | Scanner Bottom10 Short | 6/30 | 6/30 | 0,00 | 0,11 | -1,11R | €-40,88 | 2,72% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_BOTTOM15_SHORT | Scanner Bottom15 Short | 6/30 | 6/30 | 0,00 | 0,11 | -1,11R | €-40,88 | 2,72% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_BOTTOM20_SHORT | Scanner Bottom20 Short | 6/30 | 6/30 | 0,00 | 0,11 | -1,11R | €-40,88 | 2,72% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT | Scanner Bottom 5 Short 1H | 50/30 | 29/30 | 0,80 | 0,61 | -0,14R | €-9,96 | 5,48% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT_CONTINUATION_V1 | Scanner Bottom5 Short Continuation V1 | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | Scanner Bottom5 Short Mfe Trail V1 | 2/30 | 6/30 | 0,00 | 0,54 | -1,10R | €-12,45 | 1,38% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | Scanner Bottom5 Short Profit Lock V1 | 2/30 | 5/30 | 0,00 | 0,25 | -1,10R | €-24,00 | 1,53% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP10_LONG | Scanner Top10 Long | 7/30 | 8/30 | 2,52 | 0,42 | 0,68R | €-18,08 | 3,30% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP15_LONG | Scanner Top15 Long | 7/30 | 8/30 | 2,52 | 0,42 | 0,68R | €-18,08 | 3,30% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP20_LONG | Scanner Top20 Long | 7/30 | 8/30 | 2,52 | 0,42 | 0,68R | €-18,08 | 3,30% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC | Scanner Top 5 + forza BTC 1H | 71/30 | 28/30 | 1,50 | 1,54 | 0,29R | €12,65 | 2,74% | COERENTE + | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | Top 5 + BTC — BTC 2–3 | 12/30 | 4/30 | 1,02 | 0,47 | 0,01R | €-16,77 | 2,38% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | Top 5 + BTC — BTC≤3 | 29/30 | 10/30 | 1,10 | 0,84 | 0,07R | €-5,56 | 2,74% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | Top 5 + BTC — Guard + BTC≤3 + MFE | 22/30 | 24/30 | 1,22 | 0,52 | 0,14R | €-15,32 | 3,57% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | Top 5 + BTC — Guard + BTC≤3 | 22/30 | 9/30 | 1,22 | 0,92 | 0,14R | €-3,07 | 2,77% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | Top 5 + BTC — Guard + MFE | 25/30 | 27/30 | 0,99 | 0,45 | -0,00R | €-17,66 | 4,72% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | Top 5 + BTC — Guard | 25/30 | 14/30 | 0,99 | 0,63 | -0,00R | €-14,14 | 3,31% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | Top 5 + BTC — solo MFE | 33/30 | 17/30 | 1,08 | 0,51 | 0,05R | €-11,25 | 3,95% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | Top 5 + BTC — 75% a 2,2R + runner 3R | 24/30 | 15/30 | 1,16 | 1,17 | 0,12R | €4,71 | 2,75% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | Top 5 + BTC — target pieno 3R | 24/30 | 11/30 | 1,16 | 1,11 | 0,12R | €4,14 | 2,73% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_LONG | Scanner Top 5 Long 1H | 85/30 | 36/30 | 1,38 | 1,72 | 0,22R | €16,03 | 2,75% | COERENTE + | PRONTA PER REVISIONE LIVE |
| SHADOW_SOL_ADAPTIVE_1H | Sol Adaptive 1H | 6/30 | 6/30 | 0,85 | 0,29 | -0,11R | €-27,47 | 2,34% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_ADAPTIVE_4H | Sol Adaptive 4H | 1/30 | 1/30 | 0,00 | 0,00 | -1,05R | €-51,83 | 0,73% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_BOLLINGER_1H | Sol Bollinger 1H | 3/30 | 4/30 | 0,60 | 0,41 | -0,30R | €-24,69 | 1,89% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_BOLLINGER_4H | Sol Bollinger 4H | 1/30 | 1/30 | ∞ | ∞ | 1,74R | €86,98 | 0,40% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_SOL_DONCHIAN_1H | Sol Donchian 1H | 3/30 | 3/30 | 0,84 | 21,53 | -0,12R | €30,71 | 0,79% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SOL_DONCHIAN_4H | Sol Donchian 4H | 1/30 | 1/30 | 0,00 | 0,00 | -1,06R | €-52,00 | 0,75% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_EMA_1H | Sol Ema 1H | 5/30 | 5/30 | 1,14 | 0,86 | 0,09R | €-4,58 | 1,67% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SOL_EMA_4H | Sol Ema 4H | 1/30 | 1/30 | 0,00 | 0,00 | -1,06R | €-52,00 | 0,97% | COERENTE − | RACCOLTA RESEARCH |

Per le famiglie RSI con più configurazioni di leva o margine, il lato paper usa il conto con il maggior numero di eventi indipendenti; i conti duplicati non vengono aggregati.
`PRONTA PER REVISIONE LIVE` non invia ordini e non sposta capitale: abilita soltanto una revisione manuale finale.

## 🎯 DOGE Rejection Short — conto dedicato €3.600

Simulazione separata **paper only**: capitale/margine iniziale **€3.600**, leva **5x**, esposizione iniziale **€18.000**. Non modifica i conti paper da €10.000 e non invia ordini reali.

- Stato: **WAITING**
- Prezzo DOGE: **0.07327**
- Pre-allarme: **0.0765**; zona armata: **0.0775**; trigger rejection: **0.078**
- Invalidazione prima dell’entrata: chiusura 15m sopra **0.07966**

| Capitale iniziale | Balance | Equity | P&L aperto | Eventi chiusi | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- |
| €3.600,00 | €3.600,00 | €3.600,00 | €0,00 | 0 | 0,00% | 0,00 | 0,00% |

### Filtri correnti

| Filtro | Valore | Stato |
| --- | --- | --- |
| Dati mercato | FRESH | OK |
| Candela 15m | 24.4 min | OK |
| Global DOGE | -6.0 | OK |
| Classic raw | -11.0 | OK |
| DOGE/BTC raw | -6.0 | OK |
| Pattern ribassista | MATURO | OK |
| BTC sotto filtro | 65194.7 | OK |

### Ultima candela 15m valutata

- Rejection accettata: **NO**; motivo: **trigger_touched, entry_not_chased, bearish_confirmation**
- High **0.07338**; close **0.07335**; wick alta **30.0%**; volume **x0.16**

### Gestione

- TP1 0,07107: chiude 25% e porta lo stop residuo al pareggio costi.
- TP2 0,06961: chiude 25% e porta lo stop residuo a TP1.
- TP3 0,06400: chiude 25% e porta lo stop residuo a TP2.
- TP4 0,06000: chiude l’ultimo 25%.
- Stop iniziale dinamico: almeno 0,08060, sopra il massimo della rejection con buffer 0,2%, mai oltre 0,08120.
- Politica conservativa: se stop e target sono toccati nella stessa candela, prevale lo stop.

## 🔬 Research All Signals

Registro parallelo senza limite globale di quattro posizioni. Considera soltanto segnali validi con dati freschi; non modifica i conti paper e non genera ordini reali.

### Regime di mercato osservato

- Regime: **ALT_ROTATION_UP**
- Famiglia: **ALT_ROTATION**
- Confidenza: **88,40%**
- Volatilità: **NORMAL**
- Rotazione strategie: **SOLO OSSERVAZIONE — nessun peso operativo viene ancora modificato**
- Motivo: Le altcoin stanno sovraperformando BTC: mediana relativa +2.66%, 64% oltre +1%.
- BTC trend score: **2,00**; ADX: **19,22**; breadth sopra EMA50: **91,67%**
- Mediana alt vs BTC: **2,66%**; dispersione: **18,95%**

- Aperti in questo ciclo: **26**
- Chiusi in questo ciclo: **7**
- Posizioni research aperte: **792**
- Trade research chiusi: **3257**
- Eventi di mercato indipendenti chiusi: **821**
- Segnali sovrapposti saltati sullo stesso asset/profilo: **16863**
- Posizioni Research V1 senza regime scartate durante la migrazione: **28**

### Risultati complessivi per strategia

| Profilo | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | 10 | 8 | 8 | 50,00% | 1,84 | 0,44R | €35,28 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | 8 | 7 | 7 | 42,86% | 1,37 | 0,22R | €15,41 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | 8 | 7 | 7 | 42,86% | 1,37 | 0,22R | €15,41 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | 8 | 7 | 7 | 42,86% | 1,38 | 0,22R | €15,67 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | 6 | 1 | 1 | 100,00% | ∞ | 1,96R | €19,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | 9 | 6 | 6 | 66,67% | 3,71 | 0,94R | €56,31 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | 10 | 10 | 10 | 50,00% | 1,87 | 0,45R | €45,16 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | 8 | 7 | 7 | 71,43% | 4,62 | 1,08R | €75,34 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | 9 | 8 | 8 | 62,50% | 3,11 | 0,81R | €65,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | 4 | 4 | 4 | 75,00% | 5,50 | 1,17R | €46,82 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | 9 | 8 | 8 | 50,00% | 1,85 | 0,44R | €35,43 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | 10 | 10 | 10 | 50,00% | 1,87 | 0,45R | €45,16 |
| MAIN | 17 | 64 | 64 | 35,94% | 1,08 | 0,05R | €33,73 |
| RSI_EXTREME_LONG_15M | 0 | 10 | 10 | 30,00% | 0,31 | -0,54R | €-54,33 |
| RSI_EXTREME_SHORT_15M | 1 | 11 | 11 | 27,27% | 0,38 | -0,46R | €-51,03 |
| Bilanciata 1H V1 | 19 | 176 | 176 | 34,09% | 1,00 | 0,00R | €4,61 |
| Bilanciata 1H V2 | 12 | 53 | 47 | 41,51% | 1,39 | 0,23R | €120,28 |
| Bilanciata 1H V3 Filtered | 16 | 79 | 79 | 36,71% | 1,13 | 0,08R | €66,02 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | 11 | 4 | 4 | 25,00% | 0,62 | -0,30R | €-12,02 |
| Rapida 1H V1 | 4 | 204 | 204 | 39,22% | 0,92 | -0,05R | €-103,35 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | 7 | 16 | 16 | 56,25% | 2,08 | 0,43R | €68,15 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | 11 | 14 | 14 | 64,29% | 2,49 | 0,56R | €78,08 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | 14 | 78 | 78 | 47,44% | 1,23 | 0,13R | €100,27 |
| SHADOW_1H_FAST_NO_PEPE_V1 | 13 | 81 | 81 | 43,21% | 1,04 | 0,02R | €19,60 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | 12 | 57 | 57 | 49,12% | 1,29 | 0,16R | €89,31 |
| SHADOW_1H_FAST_TP2_V1 | 14 | 76 | 76 | 35,53% | 0,99 | -0,01R | €-4,80 |
| Rapida 1H V2 | 5 | 12 | 11 | 33,33% | 0,63 | -0,27R | €-32,65 |
| Rapida 1H V3 Filtered | 14 | 123 | 123 | 45,53% | 1,15 | 0,09R | €106,39 |
| SHADOW_1H_FAST_V3_CAP75_V1 | 14 | 67 | 67 | 46,27% | 1,15 | 0,09R | €58,13 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | 9 | 35 | 35 | 45,71% | 1,16 | 0,09R | €32,10 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | 9 | 35 | 35 | 45,71% | 1,16 | 0,09R | €32,10 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | 9 | 44 | 44 | 45,45% | 1,15 | 0,09R | €37,73 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | 14 | 78 | 78 | 46,15% | 1,15 | 0,08R | €65,54 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | 13 | 77 | 77 | 44,16% | 1,05 | 0,03R | €24,30 |
| SHADOW_4H_WIDE | 26 | 51 | 51 | 27,45% | 1,03 | 0,02R | €11,67 |
| SHADOW_BOLLINGER_MR_1H | 5 | 49 | 49 | 46,94% | 1,16 | 0,09R | €46,29 |
| SHADOW_BTC_ADAPTIVE_1H | 0 | 4 | 4 | 0,00% | 0,00 | -1,11R | €-44,44 |
| SHADOW_BTC_ADAPTIVE_4H | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,67 |
| SHADOW_BTC_BOLLINGER_1H | 0 | 3 | 3 | 100,00% | ∞ | 1,37R | €41,00 |
| SHADOW_BTC_BOLLINGER_4H | 0 | 1 | 1 | 100,00% | ∞ | 1,72R | €17,16 |
| SHADOW_BTC_DONCHIAN_1H | 0 | 5 | 5 | 0,00% | 0,00 | -1,12R | €-56,25 |
| SHADOW_BTC_DONCHIAN_4H | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,71 |
| SHADOW_BTC_EMA_1H | 1 | 4 | 4 | 25,00% | 0,57 | -0,36R | €-14,44 |
| SHADOW_BTC_EMA_4H | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,71 |
| SHADOW_COMBO_ADAPTIVE | 19 | 123 | 123 | 37,40% | 1,13 | 0,08R | €99,85 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | 13 | 36 | 36 | 33,33% | 0,93 | -0,05R | €-16,58 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | 19 | 90 | 90 | 35,56% | 1,03 | 0,02R | €18,40 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | 19 | 64 | 64 | 32,81% | 0,89 | -0,08R | €-51,32 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | 1 | 5 | 5 | 20,00% | 0,46 | -0,46R | €-22,90 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | 1 | 5 | 5 | 20,00% | 0,46 | -0,46R | €-22,90 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | 8 | 18 | 18 | 38,89% | 1,20 | 0,13R | €22,96 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | 2 | 29 | 29 | 17,24% | 0,38 | -0,55R | €-159,95 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | 7 | 40 | 40 | 17,50% | 0,58 | -0,37R | €-147,89 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | 7 | 40 | 40 | 17,50% | 0,58 | -0,37R | €-147,89 |
| SHADOW_COMBO_MEAN_REVERSION | 2 | 18 | 18 | 44,44% | 1,12 | 0,07R | €12,92 |
| SHADOW_COMBO_SCANNER | 11 | 73 | 73 | 42,47% | 1,52 | 0,30R | €222,21 |
| SHADOW_COMBO_TREND | 20 | 96 | 96 | 33,33% | 1,04 | 0,03R | €27,18 |
| SHADOW_DOGE_BOLLINGER_1H | 0 | 2 | 2 | 0,00% | 0,00 | -1,12R | €-22,46 |
| SHADOW_DOGE_DONCHIAN_1H | 0 | 3 | 3 | 33,33% | 0,84 | -0,12R | €-3,55 |
| SHADOW_DOGE_EMA_1H | 0 | 4 | 4 | 50,00% | 1,71 | 0,39R | €15,73 |
| SHADOW_DONCHIAN_1H | 11 | 58 | 58 | 27,59% | 0,90 | -0,08R | €-45,52 |
| SHADOW_EMA_TREND_1H | 21 | 100 | 100 | 33,00% | 1,06 | 0,04R | €38,07 |
| SHADOW_ETH_ADAPTIVE_1H | 1 | 5 | 5 | 20,00% | 0,42 | -0,51R | €-25,56 |
| SHADOW_ETH_BOLLINGER_1H | 1 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,33 |
| SHADOW_ETH_DONCHIAN_1H | 1 | 4 | 4 | 25,00% | 0,56 | -0,37R | €-14,86 |
| SHADOW_ETH_EMA_1H | 1 | 5 | 5 | 20,00% | 0,43 | -0,51R | €-25,44 |
| SHADOW_ETH_EMA_4H | 1 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,57 |
| SHADOW_GLOBAL_PURE | 0 | 4 | 4 | 50,00% | 1,75 | 0,41R | €16,33 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | 12 | 31 | 31 | 32,26% | 0,89 | -0,07R | €-23,16 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | 12 | 31 | 31 | 29,03% | 0,77 | -0,17R | €-52,37 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | 10 | 29 | 29 | 31,03% | 0,85 | -0,11R | €-31,62 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | 13 | 24 | 24 | 20,83% | 0,75 | -0,21R | €-50,44 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | 7 | 27 | 27 | 29,63% | 0,80 | -0,15R | €-40,13 |
| SHADOW_MASTER_ADAPTIVE_V1 | 12 | 31 | 31 | 29,03% | 0,77 | -0,17R | €-52,37 |
| Forza relativa 1H V1 | 19 | 127 | 127 | 31,50% | 1,00 | -0,00R | €-0,92 |
| Forza relativa 1H V2 | 10 | 50 | 46 | 42,00% | 1,52 | 0,31R | €154,82 |
| SHADOW_SCANNER_BOTTOM10_SHORT | 4 | 6 | 6 | 0,00% | 0,00 | -1,11R | €-66,45 |
| SHADOW_SCANNER_BOTTOM15_SHORT | 4 | 6 | 6 | 0,00% | 0,00 | -1,11R | €-66,45 |
| SHADOW_SCANNER_BOTTOM20_SHORT | 4 | 6 | 6 | 0,00% | 0,00 | -1,11R | €-66,45 |
| SHADOW_SCANNER_BOTTOM5_SHORT | 6 | 50 | 50 | 28,00% | 0,80 | -0,14R | €-67,84 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | 3 | 2 | 2 | 0,00% | 0,00 | -1,10R | €-22,10 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | 3 | 2 | 2 | 0,00% | 0,00 | -1,10R | €-22,10 |
| SHADOW_SCANNER_TOP10_LONG | 8 | 7 | 7 | 57,14% | 2,52 | 0,68R | €47,25 |
| SHADOW_SCANNER_TOP15_LONG | 9 | 7 | 7 | 57,14% | 2,52 | 0,68R | €47,25 |
| SHADOW_SCANNER_TOP20_LONG | 9 | 7 | 7 | 57,14% | 2,52 | 0,68R | €47,25 |
| SHADOW_SCANNER_TOP5_BTC | 11 | 71 | 71 | 40,85% | 1,50 | 0,29R | €209,30 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | 6 | 12 | 12 | 33,33% | 1,02 | 0,01R | €1,57 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | 11 | 29 | 29 | 34,48% | 1,10 | 0,07R | €19,44 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | 9 | 22 | 22 | 36,36% | 1,22 | 0,14R | €31,68 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | 9 | 22 | 22 | 36,36% | 1,22 | 0,14R | €31,68 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | 9 | 25 | 25 | 32,00% | 0,99 | -0,00R | €-0,90 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | 9 | 25 | 25 | 32,00% | 0,99 | -0,00R | €-0,90 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | 11 | 33 | 33 | 33,33% | 1,08 | 0,05R | €17,60 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | 12 | 24 | 24 | 29,17% | 1,16 | 0,12R | €28,74 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | 12 | 24 | 24 | 29,17% | 1,16 | 0,12R | €28,74 |
| SHADOW_SCANNER_TOP5_LONG | 10 | 85 | 85 | 41,18% | 1,38 | 0,22R | €190,97 |
| SHADOW_SOL_ADAPTIVE_1H | 0 | 6 | 6 | 33,33% | 0,85 | -0,11R | €-6,52 |
| SHADOW_SOL_ADAPTIVE_4H | 1 | 1 | 1 | 0,00% | 0,00 | -1,05R | €-10,52 |
| SHADOW_SOL_BOLLINGER_1H | 0 | 3 | 3 | 33,33% | 0,60 | -0,30R | €-9,00 |
| SHADOW_SOL_BOLLINGER_4H | 0 | 1 | 1 | 100,00% | ∞ | 1,74R | €17,38 |
| SHADOW_SOL_DONCHIAN_1H | 0 | 3 | 3 | 33,33% | 0,84 | -0,12R | €-3,58 |
| SHADOW_SOL_DONCHIAN_4H | 1 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,56 |
| SHADOW_SOL_EMA_1H | 0 | 5 | 5 | 40,00% | 1,14 | 0,09R | €4,59 |
| SHADOW_SOL_EMA_4H | 1 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,56 |

### Matrice strategia × regime all’entrata

| Profilo | Regime entrata | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | ALT_ROTATION_UP | 6 | 6 | 6 | 50,00% | 1,82 | 0,43R | €26,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | RANGE | 3 | 2 | 2 | 50,00% | 1,88 | 0,46R | €9,28 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | ALT_ROTATION_UP | 5 | 5 | 5 | 40,00% | 1,19 | 0,12R | €6,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | RANGE | 2 | 2 | 2 | 50,00% | 1,88 | 0,46R | €9,28 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | ALT_ROTATION_UP | 5 | 5 | 5 | 40,00% | 1,19 | 0,12R | €6,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | RANGE | 2 | 2 | 2 | 50,00% | 1,88 | 0,46R | €9,28 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | ALT_ROTATION_UP | 4 | 4 | 4 | 50,00% | 1,81 | 0,42R | €16,89 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | RANGE | 3 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,77 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | RANGE_LOW_VOL | 1 | 1 | 1 | 100,00% | ∞ | 1,96R | €19,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | RANGE | 5 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | RANGE_LOW_VOL | 1 | 1 | 1 | 100,00% | ∞ | 1,96R | €19,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | ALT_ROTATION_UP | 5 | 5 | 5 | 60,00% | 2,77 | 0,74R | €36,76 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | RANGE | 3 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | RANGE_LOW_VOL | 1 | 1 | 1 | 100,00% | ∞ | 1,96R | €19,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | ALT_ROTATION_UP | 6 | 5 | 5 | 60,00% | 2,77 | 0,74R | €36,76 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | RANGE | 3 | 3 | 3 | 0,00% | 0,00 | -1,03R | €-30,94 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | RANGE_LOW_VOL | 1 | 2 | 2 | 100,00% | ∞ | 1,97R | €39,35 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | ALT_ROTATION_UP | 4 | 5 | 5 | 60,00% | 2,75 | 0,73R | €36,45 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | RANGE | 3 | 2 | 2 | 100,00% | ∞ | 1,94R | €38,89 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | ALT_ROTATION_UP | 5 | 5 | 5 | 60,00% | 2,75 | 0,73R | €36,45 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | RANGE | 3 | 3 | 3 | 66,67% | 3,82 | 0,96R | €28,72 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | ALT_ROTATION_UP | 4 | 3 | 3 | 66,67% | 3,62 | 0,91R | €27,27 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | RANGE_LOW_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,96R | €19,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | ALT_ROTATION_UP | 5 | 4 | 4 | 50,00% | 1,81 | 0,42R | €16,89 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | RANGE | 3 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,81 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | RANGE_LOW_VOL | 1 | 2 | 2 | 100,00% | ∞ | 1,97R | €39,35 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | ALT_ROTATION_UP | 6 | 5 | 5 | 60,00% | 2,77 | 0,74R | €36,76 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | RANGE | 3 | 3 | 3 | 0,00% | 0,00 | -1,03R | €-30,94 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | RANGE_LOW_VOL | 1 | 2 | 2 | 100,00% | ∞ | 1,97R | €39,35 |
| MAIN | ALT_ROTATION_DOWN | 1 | 3 | 3 | 33,33% | 0,96 | -0,03R | €-0,88 |
| MAIN | ALT_ROTATION_UP | 5 | 7 | 7 | 0,00% | 0,00 | -1,02R | €-71,59 |
| MAIN | RANGE | 8 | 24 | 24 | 37,50% | 1,15 | 0,10R | €23,95 |
| MAIN | RANGE_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| MAIN | RANGE_LOW_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| MAIN | TRANSITION | 0 | 8 | 8 | 50,00% | 1,93 | 0,47R | €37,99 |
| MAIN | TREND_UP | 1 | 16 | 16 | 37,50% | 1,15 | 0,10R | €15,71 |
| MAIN | TREND_UP_HIGH_VOL | 2 | 4 | 4 | 25,00% | 0,64 | -0,28R | €-11,18 |
| RSI_EXTREME_LONG_15M | RANGE | 0 | 8 | 8 | 12,50% | 0,06 | -0,92R | €-73,76 |
| RSI_EXTREME_LONG_15M | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,29R | €12,88 |
| RSI_EXTREME_LONG_15M | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 0,66R | €6,56 |
| RSI_EXTREME_SHORT_15M | ALT_ROTATION_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 1,47R | €14,67 |
| RSI_EXTREME_SHORT_15M | ALT_ROTATION_UP | 1 | 3 | 3 | 0,00% | 0,00 | -1,21R | €-36,31 |
| RSI_EXTREME_SHORT_15M | RANGE | 0 | 2 | 2 | 50,00% | 0,27 | -0,45R | €-8,98 |
| RSI_EXTREME_SHORT_15M | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -0,41R | €-4,13 |
| RSI_EXTREME_SHORT_15M | TREND_UP | 0 | 4 | 4 | 25,00% | 0,44 | -0,41R | €-16,27 |
| Bilanciata 1H V1 | ALT_ROTATION_DOWN | 3 | 12 | 12 | 25,00% | 0,60 | -0,32R | €-38,38 |
| Bilanciata 1H V1 | ALT_ROTATION_UP | 5 | 17 | 17 | 47,06% | 1,64 | 0,35R | €60,25 |
| Bilanciata 1H V1 | RANGE | 7 | 49 | 49 | 38,78% | 1,20 | 0,13R | €61,96 |
| Bilanciata 1H V1 | RANGE_HIGH_VOL | 0 | 11 | 11 | 0,00% | 0,00 | -1,07R | €-118,08 |
| Bilanciata 1H V1 | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| Bilanciata 1H V1 | TRANSITION | 0 | 30 | 30 | 33,33% | 1,00 | -0,00R | €-0,05 |
| Bilanciata 1H V1 | TREND_DOWN | 2 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| Bilanciata 1H V1 | TREND_UP | 1 | 43 | 43 | 39,53% | 1,31 | 0,18R | €77,80 |
| Bilanciata 1H V1 | TREND_UP_HIGH_VOL | 0 | 13 | 13 | 23,08% | 0,67 | -0,22R | €-28,71 |
| Bilanciata 1H V2 | ALT_ROTATION_UP | 6 | 7 | 6 | 57,14% | 2,39 | 0,64R | €44,82 |
| Bilanciata 1H V2 | RANGE | 6 | 26 | 24 | 34,62% | 1,02 | 0,01R | €2,97 |
| Bilanciata 1H V2 | TRANSITION | 0 | 20 | 17 | 45,00% | 1,69 | 0,36R | €72,49 |
| Bilanciata 1H V3 Filtered | ALT_ROTATION_DOWN | 1 | 11 | 11 | 36,36% | 1,04 | 0,03R | €3,17 |
| Bilanciata 1H V3 Filtered | ALT_ROTATION_UP | 7 | 3 | 3 | 0,00% | 0,00 | -1,04R | €-31,33 |
| Bilanciata 1H V3 Filtered | RANGE | 6 | 19 | 19 | 52,63% | 2,02 | 0,52R | €98,63 |
| Bilanciata 1H V3 Filtered | RANGE_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,83 |
| Bilanciata 1H V3 Filtered | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| Bilanciata 1H V3 Filtered | TRANSITION | 0 | 8 | 8 | 37,50% | 1,11 | 0,07R | €5,68 |
| Bilanciata 1H V3 Filtered | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,14 |
| Bilanciata 1H V3 Filtered | TREND_UP | 0 | 21 | 21 | 42,86% | 1,53 | 0,29R | €60,84 |
| Bilanciata 1H V3 Filtered | TREND_UP_HIGH_VOL | 0 | 14 | 14 | 21,43% | 0,59 | -0,29R | €-39,99 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | ALT_ROTATION_UP | 7 | 1 | 1 | 0,00% | 0,00 | -1,03R | €-10,33 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | RANGE | 2 | 1 | 1 | 100,00% | ∞ | 1,96R | €19,57 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TREND_DOWN | 1 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,25 |
| Rapida 1H V1 | ALT_ROTATION_DOWN | 1 | 21 | 21 | 23,81% | 0,43 | -0,43R | €-90,26 |
| Rapida 1H V1 | ALT_ROTATION_UP | 0 | 13 | 13 | 53,85% | 1,58 | 0,29R | €37,18 |
| Rapida 1H V1 | RANGE | 3 | 64 | 64 | 45,31% | 1,20 | 0,11R | €68,43 |
| Rapida 1H V1 | RANGE_HIGH_VOL | 0 | 11 | 11 | 0,00% | 0,00 | -1,09R | €-119,90 |
| Rapida 1H V1 | TRANSITION | 0 | 26 | 26 | 50,00% | 1,57 | 0,27R | €68,95 |
| Rapida 1H V1 | TREND_UP | 0 | 48 | 48 | 41,67% | 0,97 | -0,02R | €-9,20 |
| Rapida 1H V1 | TREND_UP_HIGH_VOL | 0 | 21 | 21 | 28,57% | 0,59 | -0,28R | €-58,55 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | ALT_ROTATION_DOWN | 0 | 5 | 5 | 0,00% | 0,00 | -0,83R | €-41,38 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | ALT_ROTATION_UP | 5 | 2 | 2 | 100,00% | ∞ | 1,37R | €27,46 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | RANGE | 2 | 4 | 4 | 100,00% | ∞ | 1,49R | €59,40 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 1,48R | €29,69 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TREND_UP | 0 | 3 | 3 | 33,33% | 0,68 | -0,23R | €-7,03 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | ALT_ROTATION_UP | 7 | 8 | 8 | 62,50% | 2,26 | 0,50R | €39,80 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | RANGE | 3 | 2 | 2 | 50,00% | 1,41 | 0,21R | €4,28 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 100,00% | ∞ | 1,47R | €44,18 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | ALT_ROTATION_DOWN | 0 | 18 | 18 | 22,22% | 0,40 | -0,46R | €-82,22 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | ALT_ROTATION_UP | 7 | 9 | 9 | 66,67% | 2,70 | 0,60R | €53,70 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | RANGE | 6 | 29 | 29 | 62,07% | 2,15 | 0,47R | €137,32 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 100,00% | ∞ | 1,47R | €44,18 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 1,48R | €29,69 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TREND_UP | 0 | 16 | 16 | 25,00% | 0,44 | -0,45R | €-72,21 |
| SHADOW_1H_FAST_NO_PEPE_V1 | ALT_ROTATION_DOWN | 1 | 19 | 19 | 21,05% | 0,38 | -0,49R | €-92,40 |
| SHADOW_1H_FAST_NO_PEPE_V1 | ALT_ROTATION_UP | 5 | 10 | 10 | 50,00% | 1,31 | 0,17R | €16,59 |
| SHADOW_1H_FAST_NO_PEPE_V1 | RANGE | 5 | 31 | 31 | 58,06% | 1,83 | 0,38R | €116,78 |
| SHADOW_1H_FAST_NO_PEPE_V1 | RANGE_LOW_VOL | 1 | 2 | 2 | 100,00% | ∞ | 1,47R | €29,42 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TRANSITION | 0 | 3 | 3 | 100,00% | ∞ | 1,48R | €44,53 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_DOWN | 1 | 2 | 2 | 0,00% | 0,00 | -1,02R | €-20,41 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_UP | 0 | 14 | 14 | 21,43% | 0,36 | -0,54R | €-74,90 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | ALT_ROTATION_DOWN | 0 | 12 | 12 | 33,33% | 0,65 | -0,25R | €-30,18 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | ALT_ROTATION_UP | 8 | 10 | 10 | 50,00% | 1,32 | 0,17R | €17,32 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | RANGE | 4 | 23 | 23 | 65,22% | 2,50 | 0,56R | €128,99 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | RANGE_LOW_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,48R | €29,66 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_UP | 0 | 8 | 8 | 12,50% | 0,18 | -0,76R | €-61,17 |
| SHADOW_1H_FAST_TP2_V1 | ALT_ROTATION_DOWN | 1 | 19 | 19 | 15,79% | 0,36 | -0,54R | €-102,47 |
| SHADOW_1H_FAST_TP2_V1 | ALT_ROTATION_UP | 5 | 12 | 12 | 50,00% | 1,76 | 0,41R | €49,61 |
| SHADOW_1H_FAST_TP2_V1 | RANGE | 5 | 25 | 25 | 44,00% | 1,34 | 0,20R | €50,77 |
| SHADOW_1H_FAST_TP2_V1 | RANGE_LOW_VOL | 2 | 1 | 1 | 100,00% | ∞ | 1,95R | €19,52 |
| SHADOW_1H_FAST_TP2_V1 | TRANSITION | 0 | 3 | 3 | 100,00% | ∞ | 1,95R | €58,62 |
| SHADOW_1H_FAST_TP2_V1 | TREND_DOWN | 1 | 2 | 2 | 0,00% | 0,00 | -1,02R | €-20,41 |
| SHADOW_1H_FAST_TP2_V1 | TREND_UP | 0 | 14 | 14 | 21,43% | 0,49 | -0,43R | €-60,45 |
| Rapida 1H V2 | ALT_ROTATION_UP | 2 | 2 | 2 | 0,00% | 0,00 | -1,10R | €-21,92 |
| Rapida 1H V2 | RANGE | 3 | 9 | 8 | 44,44% | 1,01 | 0,01R | €0,69 |
| Rapida 1H V2 | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -1,14R | €-11,43 |
| Rapida 1H V3 Filtered | ALT_ROTATION_DOWN | 1 | 21 | 21 | 28,57% | 0,52 | -0,36R | €-75,39 |
| Rapida 1H V3 Filtered | ALT_ROTATION_UP | 5 | 11 | 11 | 63,64% | 2,31 | 0,51R | €56,43 |
| Rapida 1H V3 Filtered | RANGE | 6 | 30 | 30 | 60,00% | 1,99 | 0,43R | €128,83 |
| Rapida 1H V3 Filtered | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| Rapida 1H V3 Filtered | RANGE_LOW_VOL | 1 | 2 | 2 | 100,00% | ∞ | 1,47R | €29,42 |
| Rapida 1H V3 Filtered | TRANSITION | 0 | 7 | 7 | 57,14% | 1,83 | 0,38R | €26,94 |
| Rapida 1H V3 Filtered | TREND_DOWN | 1 | 2 | 2 | 0,00% | 0,00 | -1,02R | €-20,41 |
| Rapida 1H V3 Filtered | TREND_UP | 0 | 29 | 29 | 48,28% | 1,27 | 0,15R | €43,00 |
| Rapida 1H V3 Filtered | TREND_UP_HIGH_VOL | 0 | 20 | 20 | 25,00% | 0,49 | -0,36R | €-72,31 |
| SHADOW_1H_FAST_V3_CAP75_V1 | ALT_ROTATION_DOWN | 0 | 16 | 16 | 25,00% | 0,44 | -0,44R | €-70,78 |
| SHADOW_1H_FAST_V3_CAP75_V1 | ALT_ROTATION_UP | 7 | 11 | 11 | 54,55% | 1,57 | 0,28R | €30,91 |
| SHADOW_1H_FAST_V3_CAP75_V1 | RANGE | 6 | 25 | 25 | 64,00% | 2,36 | 0,53R | €132,39 |
| SHADOW_1H_FAST_V3_CAP75_V1 | RANGE_LOW_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,48R | €29,66 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_UP | 0 | 11 | 11 | 18,18% | 0,29 | -0,62R | €-68,73 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | ALT_ROTATION_DOWN | 0 | 6 | 6 | 0,00% | 0,00 | -1,04R | €-62,18 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | ALT_ROTATION_UP | 6 | 7 | 7 | 57,14% | 1,79 | 0,36R | €24,86 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | RANGE | 3 | 13 | 13 | 69,23% | 3,24 | 0,71R | €92,34 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TREND_UP | 0 | 7 | 7 | 14,29% | 0,20 | -0,75R | €-52,65 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | ALT_ROTATION_DOWN | 0 | 6 | 6 | 0,00% | 0,00 | -1,04R | €-62,18 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | ALT_ROTATION_UP | 6 | 7 | 7 | 57,14% | 1,79 | 0,36R | €24,86 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | RANGE | 3 | 13 | 13 | 69,23% | 3,24 | 0,71R | €92,34 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TREND_UP | 0 | 7 | 7 | 14,29% | 0,20 | -0,75R | €-52,65 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 0 | 8 | 8 | 0,00% | 0,00 | -1,03R | €-82,50 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | ALT_ROTATION_UP | 5 | 9 | 9 | 55,56% | 1,61 | 0,29R | €26,20 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | RANGE | 4 | 16 | 16 | 68,75% | 3,19 | 0,70R | €111,49 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | RANGE_LOW_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,47R | €29,42 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 1,49R | €29,71 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,23 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_UP | 0 | 6 | 6 | 0,00% | 0,00 | -1,11R | €-66,36 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | ALT_ROTATION_DOWN | 1 | 20 | 20 | 30,00% | 0,56 | -0,32R | €-63,96 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | ALT_ROTATION_UP | 5 | 8 | 8 | 62,50% | 2,23 | 0,49R | €39,00 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | RANGE | 6 | 30 | 30 | 60,00% | 1,99 | 0,43R | €128,83 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | RANGE_LOW_VOL | 1 | 2 | 2 | 100,00% | ∞ | 1,47R | €29,42 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 1,49R | €29,71 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TREND_DOWN | 1 | 2 | 2 | 0,00% | 0,00 | -1,02R | €-20,41 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TREND_UP | 0 | 14 | 14 | 21,43% | 0,35 | -0,55R | €-77,05 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | ALT_ROTATION_DOWN | 1 | 20 | 20 | 30,00% | 0,56 | -0,32R | €-63,96 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | ALT_ROTATION_UP | 5 | 10 | 10 | 50,00% | 1,28 | 0,15R | €15,31 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | RANGE | 5 | 29 | 29 | 58,62% | 1,88 | 0,39R | €113,97 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | RANGE_LOW_VOL | 1 | 2 | 2 | 100,00% | ∞ | 1,47R | €29,42 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 1,49R | €29,71 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_DOWN | 1 | 2 | 2 | 0,00% | 0,00 | -1,02R | €-20,41 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_UP | 0 | 12 | 12 | 16,67% | 0,26 | -0,66R | €-79,74 |
| SHADOW_4H_WIDE | ALT_ROTATION_DOWN | 2 | 2 | 2 | 100,00% | ∞ | 2,79R | €55,73 |
| SHADOW_4H_WIDE | ALT_ROTATION_UP | 3 | 3 | 3 | 0,00% | 0,00 | -1,01R | €-30,40 |
| SHADOW_4H_WIDE | RANGE | 10 | 21 | 21 | 23,81% | 0,85 | -0,12R | €-24,87 |
| SHADOW_4H_WIDE | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_4H_WIDE | TRANSITION | 3 | 7 | 7 | 14,29% | 0,46 | -0,47R | €-33,10 |
| SHADOW_4H_WIDE | TREND_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_4H_WIDE | TREND_UP | 2 | 14 | 14 | 42,86% | 2,03 | 0,61R | €84,85 |
| SHADOW_4H_WIDE | TREND_UP_HIGH_VOL | 4 | 4 | 4 | 0,00% | 0,00 | -1,01R | €-40,53 |
| SHADOW_BOLLINGER_MR_1H | ALT_ROTATION_DOWN | 0 | 5 | 5 | 60,00% | 1,99 | 0,43R | €21,52 |
| SHADOW_BOLLINGER_MR_1H | ALT_ROTATION_UP | 3 | 5 | 5 | 20,00% | 0,35 | -0,55R | €-27,49 |
| SHADOW_BOLLINGER_MR_1H | RANGE | 2 | 19 | 19 | 47,37% | 1,16 | 0,09R | €17,24 |
| SHADOW_BOLLINGER_MR_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_BOLLINGER_MR_1H | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_BOLLINGER_MR_1H | TRANSITION | 0 | 3 | 3 | 33,33% | 0,71 | -0,20R | €-6,14 |
| SHADOW_BOLLINGER_MR_1H | TREND_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 1,48R | €14,79 |
| SHADOW_BOLLINGER_MR_1H | TREND_UP | 0 | 12 | 12 | 50,00% | 1,28 | 0,15R | €18,32 |
| SHADOW_BOLLINGER_MR_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,31 | 0,17R | €3,31 |
| SHADOW_BTC_ADAPTIVE_1H | RANGE | 0 | 3 | 3 | 0,00% | 0,00 | -1,11R | €-33,33 |
| SHADOW_BTC_ADAPTIVE_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_BTC_ADAPTIVE_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,67 |
| SHADOW_BTC_BOLLINGER_1H | RANGE | 0 | 2 | 2 | 100,00% | ∞ | 1,37R | €27,33 |
| SHADOW_BTC_BOLLINGER_1H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,37R | €13,67 |
| SHADOW_BTC_BOLLINGER_4H | ALT_ROTATION_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 1,72R | €17,16 |
| SHADOW_BTC_DONCHIAN_1H | RANGE | 0 | 3 | 3 | 0,00% | 0,00 | -1,12R | €-33,75 |
| SHADOW_BTC_DONCHIAN_1H | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -1,12R | €-11,25 |
| SHADOW_BTC_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_BTC_DONCHIAN_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,71 |
| SHADOW_BTC_EMA_1H | RANGE | 1 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_BTC_EMA_1H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_BTC_EMA_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,70 | 0,39R | €7,78 |
| SHADOW_BTC_EMA_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,71 |
| SHADOW_COMBO_ADAPTIVE | ALT_ROTATION_DOWN | 3 | 12 | 12 | 25,00% | 0,60 | -0,31R | €-37,55 |
| SHADOW_COMBO_ADAPTIVE | ALT_ROTATION_UP | 5 | 9 | 9 | 44,44% | 1,48 | 0,28R | €25,00 |
| SHADOW_COMBO_ADAPTIVE | RANGE | 6 | 38 | 38 | 39,47% | 1,18 | 0,12R | €45,13 |
| SHADOW_COMBO_ADAPTIVE | RANGE_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,83 |
| SHADOW_COMBO_ADAPTIVE | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_ADAPTIVE | TRANSITION | 0 | 20 | 20 | 45,00% | 1,65 | 0,34R | €68,99 |
| SHADOW_COMBO_ADAPTIVE | TREND_DOWN | 2 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_COMBO_ADAPTIVE | TREND_UP | 2 | 29 | 29 | 44,83% | 1,52 | 0,30R | €87,02 |
| SHADOW_COMBO_ADAPTIVE | TREND_UP_HIGH_VOL | 0 | 12 | 12 | 16,67% | 0,40 | -0,48R | €-57,73 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 1 | 4 | 4 | 0,00% | 0,00 | -1,01R | €-40,55 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | ALT_ROTATION_UP | 4 | 7 | 7 | 57,14% | 2,42 | 0,64R | €45,11 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | RANGE | 4 | 11 | 11 | 54,55% | 2,34 | 0,62R | €68,08 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_UP | 2 | 6 | 6 | 0,00% | 0,00 | -1,09R | €-65,26 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_UP_HIGH_VOL | 0 | 6 | 6 | 16,67% | 0,36 | -0,56R | €-33,65 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | ALT_ROTATION_DOWN | 3 | 12 | 12 | 25,00% | 0,60 | -0,31R | €-37,55 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | ALT_ROTATION_UP | 5 | 10 | 10 | 40,00% | 1,22 | 0,14R | €13,89 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE | 6 | 26 | 26 | 46,15% | 1,56 | 0,32R | €83,60 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,83 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TRANSITION | 0 | 4 | 4 | 50,00% | 1,78 | 0,43R | €17,13 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_DOWN | 2 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_UP | 2 | 21 | 21 | 42,86% | 1,42 | 0,25R | €52,12 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_UP_HIGH_VOL | 0 | 14 | 14 | 14,29% | 0,33 | -0,57R | €-79,79 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | ALT_ROTATION_DOWN | 3 | 12 | 12 | 25,00% | 0,60 | -0,31R | €-37,55 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | ALT_ROTATION_UP | 5 | 7 | 7 | 57,14% | 2,42 | 0,64R | €45,11 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | RANGE | 6 | 26 | 26 | 46,15% | 1,56 | 0,32R | €83,60 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TRANSITION | 0 | 3 | 3 | 33,33% | 0,91 | -0,07R | €-1,99 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_DOWN | 2 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_UP | 2 | 8 | 8 | 0,00% | 0,00 | -1,07R | €-85,56 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_UP_HIGH_VOL | 0 | 7 | 7 | 14,29% | 0,30 | -0,64R | €-44,76 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TRANSITION | 0 | 3 | 3 | 33,33% | 0,92 | -0,06R | €-1,72 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TREND_UP | 1 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,18 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TRANSITION | 0 | 3 | 3 | 33,33% | 0,92 | -0,06R | €-1,72 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TREND_UP | 1 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,18 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | ALT_ROTATION_DOWN | 1 | 2 | 2 | 0,00% | 0,00 | -1,10R | €-21,95 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | ALT_ROTATION_UP | 2 | 1 | 1 | 0,00% | 0,00 | -1,03R | €-10,34 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | RANGE | 4 | 10 | 10 | 60,00% | 2,88 | 0,77R | €77,46 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TRANSITION | 0 | 2 | 2 | 50,00% | 1,90 | 0,46R | €9,15 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,18 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TRANSITION | 0 | 8 | 8 | 25,00% | 0,60 | -0,32R | €-25,89 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TREND_UP | 2 | 13 | 13 | 15,38% | 0,33 | -0,60R | €-78,20 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TREND_UP_HIGH_VOL | 0 | 8 | 8 | 12,50% | 0,26 | -0,70R | €-55,87 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_DOWN | 3 | 7 | 7 | 28,57% | 1,07 | 0,05R | €3,83 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_UP | 0 | 5 | 5 | 40,00% | 1,80 | 0,52R | €26,25 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | RANGE | 2 | 15 | 15 | 20,00% | 0,69 | -0,26R | €-39,51 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | TRANSITION | 0 | 2 | 2 | 0,00% | 0,00 | -1,09R | €-21,86 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | TREND_UP | 2 | 7 | 7 | 0,00% | 0,00 | -1,06R | €-74,11 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 0,00% | 0,00 | -1,06R | €-42,49 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | ALT_ROTATION_DOWN | 3 | 7 | 7 | 28,57% | 1,07 | 0,05R | €3,83 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | ALT_ROTATION_UP | 0 | 5 | 5 | 40,00% | 1,80 | 0,52R | €26,25 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | RANGE | 2 | 15 | 15 | 20,00% | 0,69 | -0,26R | €-39,51 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | TRANSITION | 0 | 2 | 2 | 0,00% | 0,00 | -1,09R | €-21,86 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | TREND_UP | 2 | 7 | 7 | 0,00% | 0,00 | -1,06R | €-74,11 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 0,00% | 0,00 | -1,06R | €-42,49 |
| SHADOW_COMBO_MEAN_REVERSION | ALT_ROTATION_DOWN | 1 | 3 | 3 | 33,33% | 0,73 | -0,19R | €-5,83 |
| SHADOW_COMBO_MEAN_REVERSION | RANGE | 1 | 10 | 10 | 50,00% | 1,36 | 0,20R | €19,76 |
| SHADOW_COMBO_MEAN_REVERSION | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,94 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_UP | 0 | 3 | 3 | 33,33% | 0,75 | -0,17R | €-5,09 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,85 |
| SHADOW_COMBO_SCANNER | ALT_ROTATION_DOWN | 1 | 5 | 5 | 0,00% | 0,00 | -1,03R | €-51,66 |
| SHADOW_COMBO_SCANNER | ALT_ROTATION_UP | 2 | 7 | 7 | 42,86% | 1,55 | 0,33R | €23,06 |
| SHADOW_COMBO_SCANNER | RANGE | 4 | 15 | 15 | 53,33% | 2,39 | 0,67R | €100,50 |
| SHADOW_COMBO_SCANNER | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,69 |
| SHADOW_COMBO_SCANNER | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_SCANNER | TRANSITION | 0 | 15 | 15 | 46,67% | 1,60 | 0,34R | €50,68 |
| SHADOW_COMBO_SCANNER | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_COMBO_SCANNER | TREND_UP | 2 | 20 | 20 | 50,00% | 2,04 | 0,55R | €110,63 |
| SHADOW_COMBO_SCANNER | TREND_UP_HIGH_VOL | 0 | 9 | 9 | 33,33% | 1,18 | 0,11R | €9,88 |
| SHADOW_COMBO_TREND | ALT_ROTATION_DOWN | 4 | 8 | 8 | 25,00% | 0,67 | -0,26R | €-20,97 |
| SHADOW_COMBO_TREND | ALT_ROTATION_UP | 5 | 8 | 8 | 37,50% | 1,24 | 0,16R | €12,65 |
| SHADOW_COMBO_TREND | RANGE | 5 | 29 | 29 | 34,48% | 1,08 | 0,05R | €15,12 |
| SHADOW_COMBO_TREND | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,63 |
| SHADOW_COMBO_TREND | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_TREND | TRANSITION | 0 | 16 | 16 | 43,75% | 1,79 | 0,42R | €67,09 |
| SHADOW_COMBO_TREND | TREND_DOWN | 2 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,16 |
| SHADOW_COMBO_TREND | TREND_UP | 2 | 23 | 23 | 34,78% | 1,10 | 0,07R | €15,44 |
| SHADOW_COMBO_TREND | TREND_UP_HIGH_VOL | 1 | 10 | 10 | 20,00% | 0,51 | -0,41R | €-41,36 |
| SHADOW_DOGE_BOLLINGER_1H | RANGE | 0 | 2 | 2 | 0,00% | 0,00 | -1,12R | €-22,46 |
| SHADOW_DOGE_DONCHIAN_1H | RANGE | 0 | 3 | 3 | 33,33% | 0,84 | -0,12R | €-3,55 |
| SHADOW_DOGE_EMA_1H | RANGE | 0 | 4 | 4 | 50,00% | 1,71 | 0,39R | €15,73 |
| SHADOW_DONCHIAN_1H | ALT_ROTATION_DOWN | 3 | 8 | 8 | 25,00% | 0,76 | -0,19R | €-14,97 |
| SHADOW_DONCHIAN_1H | ALT_ROTATION_UP | 3 | 5 | 5 | 20,00% | 0,58 | -0,35R | €-17,42 |
| SHADOW_DONCHIAN_1H | RANGE | 2 | 19 | 19 | 26,32% | 0,82 | -0,14R | €-26,90 |
| SHADOW_DONCHIAN_1H | RANGE_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_DONCHIAN_1H | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_DONCHIAN_1H | TRANSITION | 0 | 7 | 7 | 14,29% | 0,45 | -0,42R | €-29,27 |
| SHADOW_DONCHIAN_1H | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,16 |
| SHADOW_DONCHIAN_1H | TREND_UP | 0 | 11 | 11 | 45,45% | 1,89 | 0,53R | €57,82 |
| SHADOW_DONCHIAN_1H | TREND_UP_HIGH_VOL | 1 | 5 | 5 | 40,00% | 1,48 | 0,31R | €15,65 |
| SHADOW_EMA_TREND_1H | ALT_ROTATION_DOWN | 3 | 9 | 9 | 22,22% | 0,57 | -0,35R | €-31,52 |
| SHADOW_EMA_TREND_1H | ALT_ROTATION_UP | 5 | 8 | 8 | 25,00% | 0,69 | -0,25R | €-19,68 |
| SHADOW_EMA_TREND_1H | RANGE | 6 | 27 | 27 | 37,04% | 1,28 | 0,18R | €47,40 |
| SHADOW_EMA_TREND_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,63 |
| SHADOW_EMA_TREND_1H | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_EMA_TREND_1H | TRANSITION | 1 | 16 | 16 | 43,75% | 1,79 | 0,42R | €67,07 |
| SHADOW_EMA_TREND_1H | TREND_DOWN | 2 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,16 |
| SHADOW_EMA_TREND_1H | TREND_UP | 2 | 28 | 28 | 32,14% | 1,02 | 0,02R | €4,61 |
| SHADOW_EMA_TREND_1H | TREND_UP_HIGH_VOL | 1 | 10 | 10 | 30,00% | 0,88 | -0,09R | €-9,03 |
| SHADOW_ETH_ADAPTIVE_1H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 0,00% | 0,00 | -1,11R | €-22,22 |
| SHADOW_ETH_ADAPTIVE_1H | ALT_ROTATION_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_ETH_ADAPTIVE_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_ETH_ADAPTIVE_1H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,89R | €18,89 |
| SHADOW_ETH_ADAPTIVE_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_ETH_BOLLINGER_1H | ALT_ROTATION_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_ETH_BOLLINGER_1H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,33 |
| SHADOW_ETH_DONCHIAN_1H | ALT_ROTATION_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_ETH_DONCHIAN_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,12R | €-11,25 |
| SHADOW_ETH_DONCHIAN_1H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_ETH_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,68 | 0,38R | €7,64 |
| SHADOW_ETH_EMA_1H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 0,00% | 0,00 | -1,11R | €-22,22 |
| SHADOW_ETH_EMA_1H | ALT_ROTATION_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_ETH_EMA_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_ETH_EMA_1H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,89R | €18,89 |
| SHADOW_ETH_EMA_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,10R | €-10,99 |
| SHADOW_ETH_EMA_4H | ALT_ROTATION_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_ETH_EMA_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,57 |
| SHADOW_GLOBAL_PURE | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,10R | €-11,00 |
| SHADOW_GLOBAL_PURE | RANGE | 0 | 2 | 2 | 50,00% | 2,21 | 0,66R | €13,16 |
| SHADOW_GLOBAL_PURE | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,42R | €14,17 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | ALT_ROTATION_DOWN | 1 | 7 | 7 | 14,29% | 0,32 | -0,60R | €-41,93 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | ALT_ROTATION_UP | 2 | 3 | 3 | 0,00% | 0,00 | -1,05R | €-31,39 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | RANGE | 5 | 8 | 8 | 50,00% | 1,95 | 0,48R | €38,48 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TRANSITION | 0 | 3 | 3 | 100,00% | ∞ | 1,96R | €58,74 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TREND_DOWN | 1 | 2 | 2 | 50,00% | 1,86 | 0,44R | €8,71 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TREND_UP | 2 | 8 | 8 | 12,50% | 0,26 | -0,70R | €-55,77 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | ALT_ROTATION_DOWN | 1 | 6 | 6 | 16,67% | 0,39 | -0,51R | €-30,82 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | ALT_ROTATION_UP | 2 | 4 | 4 | 25,00% | 0,60 | -0,31R | €-12,57 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | RANGE | 5 | 9 | 9 | 55,56% | 2,44 | 0,65R | €58,35 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TREND_UP | 2 | 10 | 10 | 10,00% | 0,21 | -0,77R | €-77,01 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | ALT_ROTATION_DOWN | 1 | 6 | 6 | 16,67% | 0,39 | -0,51R | €-30,82 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | RANGE | 5 | 9 | 9 | 55,56% | 2,44 | 0,65R | €58,35 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | RANGE_LOW_VOL | 1 | 1 | 1 | 100,00% | ∞ | 1,89R | €18,89 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TREND_UP | 2 | 11 | 11 | 9,09% | 0,18 | -0,80R | €-87,73 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_DOWN | 1 | 1 | 1 | 100,00% | ∞ | 2,99R | €29,87 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_UP | 3 | 3 | 3 | 0,00% | 0,00 | -1,05R | €-31,46 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | RANGE | 5 | 9 | 9 | 33,33% | 1,47 | 0,31R | €28,35 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | TREND_UP | 2 | 10 | 10 | 10,00% | 0,31 | -0,67R | €-67,01 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | ALT_ROTATION_DOWN | 0 | 4 | 4 | 0,00% | 0,00 | -1,01R | €-40,55 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | RANGE | 4 | 12 | 12 | 58,33% | 2,73 | 0,73R | €87,99 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TREND_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TREND_UP | 1 | 10 | 10 | 0,00% | 0,00 | -1,07R | €-107,43 |
| SHADOW_MASTER_ADAPTIVE_V1 | ALT_ROTATION_DOWN | 1 | 6 | 6 | 16,67% | 0,39 | -0,51R | €-30,82 |
| SHADOW_MASTER_ADAPTIVE_V1 | ALT_ROTATION_UP | 2 | 4 | 4 | 25,00% | 0,60 | -0,31R | €-12,57 |
| SHADOW_MASTER_ADAPTIVE_V1 | RANGE | 5 | 9 | 9 | 55,56% | 2,44 | 0,65R | €58,35 |
| SHADOW_MASTER_ADAPTIVE_V1 | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_MASTER_ADAPTIVE_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| SHADOW_MASTER_ADAPTIVE_V1 | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_MASTER_ADAPTIVE_V1 | TREND_UP | 2 | 10 | 10 | 10,00% | 0,21 | -0,77R | €-77,01 |
| Forza relativa 1H V1 | ALT_ROTATION_DOWN | 3 | 9 | 9 | 11,11% | 0,26 | -0,69R | €-61,85 |
| Forza relativa 1H V1 | ALT_ROTATION_UP | 3 | 17 | 17 | 29,41% | 0,85 | -0,11R | €-19,14 |
| Forza relativa 1H V1 | RANGE | 8 | 36 | 36 | 30,56% | 0,94 | -0,04R | €-15,02 |
| Forza relativa 1H V1 | RANGE_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -1,03R | €-31,02 |
| Forza relativa 1H V1 | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| Forza relativa 1H V1 | TRANSITION | 0 | 16 | 16 | 50,00% | 2,11 | 0,57R | €91,12 |
| Forza relativa 1H V1 | TREND_DOWN | 2 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| Forza relativa 1H V1 | TREND_UP | 2 | 36 | 36 | 38,89% | 1,54 | 0,30R | €106,45 |
| Forza relativa 1H V1 | TREND_UP_HIGH_VOL | 0 | 9 | 9 | 11,11% | 0,26 | -0,68R | €-61,28 |
| Forza relativa 1H V2 | ALT_ROTATION_DOWN | 1 | 6 | 6 | 50,00% | 2,02 | 0,53R | €32,04 |
| Forza relativa 1H V2 | ALT_ROTATION_UP | 4 | 5 | 5 | 40,00% | 1,35 | 0,22R | €11,12 |
| Forza relativa 1H V2 | RANGE | 3 | 11 | 11 | 54,55% | 2,55 | 0,73R | €79,78 |
| Forza relativa 1H V2 | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| Forza relativa 1H V2 | TRANSITION | 0 | 13 | 11 | 38,46% | 1,31 | 0,20R | €25,87 |
| Forza relativa 1H V2 | TREND_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| Forza relativa 1H V2 | TREND_UP | 0 | 11 | 10 | 45,45% | 1,77 | 0,43R | €47,60 |
| Forza relativa 1H V2 | TREND_UP_HIGH_VOL | 0 | 4 | 3 | 0,00% | 0,00 | -1,04R | €-41,60 |
| SHADOW_SCANNER_BOTTOM10_SHORT | ALT_ROTATION_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM10_SHORT | RANGE | 2 | 6 | 6 | 0,00% | 0,00 | -1,11R | €-66,45 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM15_SHORT | ALT_ROTATION_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM15_SHORT | RANGE | 2 | 6 | 6 | 0,00% | 0,00 | -1,11R | €-66,45 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM20_SHORT | ALT_ROTATION_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM20_SHORT | RANGE | 2 | 6 | 6 | 0,00% | 0,00 | -1,11R | €-66,45 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM5_SHORT | ALT_ROTATION_DOWN | 1 | 5 | 5 | 60,00% | 2,62 | 0,71R | €35,50 |
| SHADOW_SCANNER_BOTTOM5_SHORT | ALT_ROTATION_UP | 1 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| SHADOW_SCANNER_BOTTOM5_SHORT | RANGE | 3 | 20 | 20 | 30,00% | 0,75 | -0,19R | €-37,65 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TRANSITION | 0 | 14 | 14 | 28,57% | 0,85 | -0,09R | €-13,14 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP | 0 | 7 | 7 | 0,00% | 0,00 | -0,73R | €-51,04 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -0,71R | €-21,38 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | ALT_ROTATION_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_DOWN | 2 | 2 | 2 | 0,00% | 0,00 | -1,10R | €-22,10 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | ALT_ROTATION_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_DOWN | 2 | 2 | 2 | 0,00% | 0,00 | -1,10R | €-22,10 |
| SHADOW_SCANNER_TOP10_LONG | ALT_ROTATION_UP | 3 | 3 | 3 | 33,33% | 0,92 | -0,06R | €-1,75 |
| SHADOW_SCANNER_TOP10_LONG | RANGE | 3 | 3 | 3 | 100,00% | ∞ | 1,97R | €59,18 |
| SHADOW_SCANNER_TOP10_LONG | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP10_LONG | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_SCANNER_TOP15_LONG | ALT_ROTATION_UP | 4 | 3 | 3 | 33,33% | 0,92 | -0,06R | €-1,75 |
| SHADOW_SCANNER_TOP15_LONG | RANGE | 3 | 3 | 3 | 100,00% | ∞ | 1,97R | €59,18 |
| SHADOW_SCANNER_TOP15_LONG | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP15_LONG | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_SCANNER_TOP20_LONG | ALT_ROTATION_UP | 4 | 3 | 3 | 33,33% | 0,92 | -0,06R | €-1,75 |
| SHADOW_SCANNER_TOP20_LONG | RANGE | 3 | 3 | 3 | 100,00% | ∞ | 1,97R | €59,18 |
| SHADOW_SCANNER_TOP20_LONG | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP20_LONG | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_SCANNER_TOP5_BTC | ALT_ROTATION_DOWN | 1 | 5 | 5 | 0,00% | 0,00 | -1,03R | €-51,66 |
| SHADOW_SCANNER_TOP5_BTC | ALT_ROTATION_UP | 2 | 8 | 8 | 37,50% | 1,24 | 0,16R | €12,54 |
| SHADOW_SCANNER_TOP5_BTC | RANGE | 4 | 15 | 15 | 53,33% | 2,80 | 0,74R | €111,45 |
| SHADOW_SCANNER_TOP5_BTC | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,69 |
| SHADOW_SCANNER_TOP5_BTC | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC | TRANSITION | 0 | 13 | 13 | 46,15% | 1,79 | 0,45R | €58,04 |
| SHADOW_SCANNER_TOP5_BTC | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_SCANNER_TOP5_BTC | TREND_UP | 2 | 19 | 19 | 47,37% | 1,85 | 0,47R | €89,92 |
| SHADOW_SCANNER_TOP5_BTC | TREND_UP_HIGH_VOL | 0 | 9 | 9 | 33,33% | 1,18 | 0,11R | €9,88 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | ALT_ROTATION_DOWN | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | ALT_ROTATION_UP | 3 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,86 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TRANSITION | 0 | 3 | 3 | 66,67% | 4,32 | 1,12R | €33,60 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TREND_UP | 1 | 2 | 2 | 50,00% | 1,97 | 0,54R | €10,76 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TREND_UP_HIGH_VOL | 0 | 6 | 6 | 16,67% | 0,40 | -0,53R | €-31,93 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | ALT_ROTATION_DOWN | 2 | 4 | 4 | 0,00% | 0,00 | -1,01R | €-40,55 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | ALT_ROTATION_UP | 2 | 4 | 4 | 25,00% | 0,67 | -0,27R | €-10,61 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | RANGE | 4 | 10 | 10 | 50,00% | 2,15 | 0,58R | €58,21 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 2,19R | €43,73 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_UP | 1 | 2 | 2 | 50,00% | 1,97 | 0,54R | €10,76 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_UP_HIGH_VOL | 0 | 6 | 6 | 16,67% | 0,40 | -0,53R | €-31,93 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | ALT_ROTATION_DOWN | 2 | 4 | 4 | 0,00% | 0,00 | -1,01R | €-40,55 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | ALT_ROTATION_UP | 2 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,14 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | RANGE | 4 | 10 | 10 | 50,00% | 2,15 | 0,58R | €58,21 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 2,19R | €43,73 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 2,19R | €21,87 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | ALT_ROTATION_DOWN | 2 | 4 | 4 | 0,00% | 0,00 | -1,01R | €-40,55 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | ALT_ROTATION_UP | 2 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,14 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | RANGE | 4 | 10 | 10 | 50,00% | 2,15 | 0,58R | €58,21 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 2,19R | €43,73 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 2,19R | €21,87 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | ALT_ROTATION_DOWN | 1 | 5 | 5 | 0,00% | 0,00 | -1,03R | €-51,66 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | ALT_ROTATION_UP | 2 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,14 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | RANGE | 4 | 10 | 10 | 50,00% | 2,15 | 0,58R | €58,21 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 2,19R | €43,73 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_UP | 1 | 3 | 3 | 33,33% | 1,02 | 0,01R | €0,39 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | ALT_ROTATION_DOWN | 1 | 5 | 5 | 0,00% | 0,00 | -1,03R | €-51,66 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | ALT_ROTATION_UP | 2 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,14 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | RANGE | 4 | 10 | 10 | 50,00% | 2,15 | 0,58R | €58,21 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 2,19R | €43,73 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_UP | 1 | 3 | 3 | 33,33% | 1,02 | 0,01R | €0,39 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | ALT_ROTATION_DOWN | 1 | 5 | 5 | 0,00% | 0,00 | -1,03R | €-51,66 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | ALT_ROTATION_UP | 2 | 4 | 4 | 25,00% | 0,67 | -0,26R | €-10,54 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | RANGE | 4 | 10 | 10 | 50,00% | 2,15 | 0,58R | €58,21 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 2,19R | €43,73 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_UP | 2 | 2 | 2 | 50,00% | 1,97 | 0,54R | €10,76 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 9 | 9 | 22,22% | 0,65 | -0,25R | €-22,73 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | ALT_ROTATION_UP | 3 | 7 | 7 | 28,57% | 1,09 | 0,07R | €4,67 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | RANGE | 4 | 8 | 8 | 37,50% | 1,76 | 0,48R | €38,46 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 2,99R | €29,87 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_UP | 2 | 4 | 4 | 25,00% | 0,92 | -0,07R | €-2,70 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -1,05R | €-31,38 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | ALT_ROTATION_UP | 3 | 7 | 7 | 28,57% | 1,09 | 0,07R | €4,67 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | RANGE | 4 | 8 | 8 | 37,50% | 1,76 | 0,48R | €38,46 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 2,99R | €29,87 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_UP | 2 | 4 | 4 | 25,00% | 0,92 | -0,07R | €-2,70 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -1,05R | €-31,38 |
| SHADOW_SCANNER_TOP5_LONG | ALT_ROTATION_DOWN | 1 | 6 | 6 | 0,00% | 0,00 | -1,05R | €-62,77 |
| SHADOW_SCANNER_TOP5_LONG | ALT_ROTATION_UP | 2 | 9 | 9 | 33,33% | 0,92 | -0,06R | €-5,06 |
| SHADOW_SCANNER_TOP5_LONG | RANGE | 4 | 16 | 16 | 56,25% | 2,87 | 0,72R | €115,32 |
| SHADOW_SCANNER_TOP5_LONG | RANGE_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,83 |
| SHADOW_SCANNER_TOP5_LONG | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_LONG | TRANSITION | 0 | 13 | 13 | 46,15% | 1,63 | 0,35R | €46,04 |
| SHADOW_SCANNER_TOP5_LONG | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_SCANNER_TOP5_LONG | TREND_UP | 1 | 29 | 29 | 48,28% | 1,84 | 0,43R | €125,07 |
| SHADOW_SCANNER_TOP5_LONG | TREND_UP_HIGH_VOL | 0 | 9 | 9 | 33,33% | 1,06 | 0,04R | €3,38 |
| SHADOW_SOL_ADAPTIVE_1H | RANGE | 0 | 4 | 4 | 25,00% | 0,57 | -0,36R | €-14,44 |
| SHADOW_SOL_ADAPTIVE_1H | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,89R | €18,89 |
| SHADOW_SOL_ADAPTIVE_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,10R | €-10,96 |
| SHADOW_SOL_ADAPTIVE_4H | RANGE | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SOL_ADAPTIVE_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,05R | €-10,52 |
| SHADOW_SOL_BOLLINGER_1H | RANGE | 0 | 3 | 3 | 33,33% | 0,60 | -0,30R | €-9,00 |
| SHADOW_SOL_BOLLINGER_4H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,74R | €17,38 |
| SHADOW_SOL_DONCHIAN_1H | RANGE | 0 | 2 | 2 | 50,00% | 1,67 | 0,38R | €7,50 |
| SHADOW_SOL_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,08 |
| SHADOW_SOL_DONCHIAN_4H | RANGE | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SOL_DONCHIAN_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,56 |
| SHADOW_SOL_EMA_1H | RANGE | 0 | 3 | 3 | 33,33% | 0,85 | -0,11R | €-3,33 |
| SHADOW_SOL_EMA_1H | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,89R | €18,89 |
| SHADOW_SOL_EMA_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,10R | €-10,96 |
| SHADOW_SOL_EMA_4H | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SOL_EMA_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,56 |

Il P&L è normalizzato a **€10 di rischio per evento**, così leva e size non falsano il confronto.
La matrice diventerà utilizzabile per una rotazione automatica soltanto dopo un campione sufficiente per ciascuna coppia strategia-regime.

# Block 3 — Shadow Exit Engine

Generato: 2026-07-27T00:08:46+00:00

> Motore esclusivamente osservativo e Paper-only. Non modifica le uscite reali. I confronti escludono il funding sia dall'uscita originale sia dalle varianti.

## Stato operativo

- Gruppi di trade ancora monitorati: **793**
- Scenari virtuali ancora attivi: **12254**
- Gruppi in attesa dell'uscita originale: **403**
- Gruppi con originale chiuso ma Shadow ancora attive: **390**
- Confronti completati: **45494**

## Classifica osservativa complessiva

| Scenario | Campione completo | Campione totale | Δ medio vs originale | Migliora | Troppo presto | Troppo tardi | Stato dati |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| TIME_6H | 1669 | 1734 | €-0,77 | 44,8% | 392 | 305 | READY_FOR_BLOCK4_EVALUATION |
| GB20_R050 | 1666 | 1731 | +€6,74 | 49,3% | 535 | 2 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R050 | 1666 | 1731 | +€5,12 | 47,0% | 553 | 16 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R050 | 1666 | 1731 | +€3,07 | 45,5% | 562 | 38 | READY_FOR_BLOCK4_EVALUATION |
| TP_R050 | 1666 | 1731 | +€2,47 | 44,8% | 618 | 1 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R050 | 1665 | 1730 | +€1,86 | 45,4% | 516 | 87 | READY_FOR_BLOCK4_EVALUATION |
| TIME_12H | 1643 | 1708 | +€0,17 | 40,2% | 194 | 461 | READY_FOR_BLOCK4_EVALUATION |
| GB20_R100 | 1635 | 1700 | +€8,05 | 45,4% | 430 | 32 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R100 | 1635 | 1700 | +€6,22 | 44,6% | 418 | 58 | READY_FOR_BLOCK4_EVALUATION |
| TP_R100 | 1635 | 1700 | +€5,96 | 42,1% | 489 | 30 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R100 | 1624 | 1689 | +€5,11 | 44,4% | 343 | 115 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R100 | 1620 | 1685 | +€3,92 | 41,7% | 279 | 231 | READY_FOR_BLOCK4_EVALUATION |
| TP_R150 | 1588 | 1653 | +€6,73 | 31,9% | 232 | 178 | READY_FOR_BLOCK4_EVALUATION |
| ATR15_R100 | 1588 | 1653 | +€0,38 | 34,4% | 179 | 384 | READY_FOR_BLOCK4_EVALUATION |
| ATR20_R100 | 1543 | 1608 | €-3,96 | 29,0% | 159 | 451 | READY_FOR_BLOCK4_EVALUATION |
| BE_R050 | 1531 | 1596 | €-10,92 | 29,4% | 314 | 346 | READY_FOR_BLOCK4_EVALUATION |
| TIME_24H | 1525 | 1590 | €-0,79 | 36,7% | 90 | 468 | READY_FOR_BLOCK4_EVALUATION |
| ATR30_R100 | 1525 | 1590 | €-8,37 | 27,0% | 114 | 493 | READY_FOR_BLOCK4_EVALUATION |
| TP_R200 | 1519 | 1584 | +€7,06 | 38,8% | 102 | 271 | READY_FOR_BLOCK4_EVALUATION |
| BE_R100 | 1411 | 1476 | €-14,96 | 21,8% | 113 | 483 | READY_FOR_BLOCK4_EVALUATION |

## Come leggere il controllo

- **EARLIER_BETTER**: la variante è uscita prima e ha conservato più profitto.
- **TOO_EARLY**: la variante è uscita prima ma ha tagliato un movimento migliore.
- **LATER_BETTER**: la variante ha continuato dopo l'uscita originale e ha guadagnato di più.
- **TOO_LATE**: la variante è rimasta aperta più a lungo e ha peggiorato il risultato.

## Limiti e protezioni

Le regole Shadow mantengono entrata, quantità, commissioni, stop protettivo iniziale e liquidazione. Le ambiguità all'interno della stessa candela vengono risolte scegliendo l'esito peggiore. Le posizioni già aperte al momento dell'installazione sono marcate come campione parziale e non saranno utilizzate dal futuro Blocco 4 come prova piena.

# Blocco 4 — Valutazione statistica Shadow

Generato: 2026-07-27T00:08:49+00:00

> Modulo esclusivamente valutativo. Non modifica strategie, uscite, posizioni o capitale. Le candidature vengono consegnate al futuro Blocco 5, senza applicazione automatica.

## Stato

- Risultati Block 3 disponibili: **45494**
- Valutazioni prodotte: **14963**
- Candidature al Blocco 5: **0**
- Mutazioni create automaticamente: **0**

## Classifica complessiva

| Scenario | Campione pieno | Δ medio (R) | Mediana (R) | CI bootstrap basso | Migliora | Score | Stato |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| GB20_R050 | 38 | 3,902 | 4,831 | 3,381 | 92,1% | 87,0 | EARLY_SIGNAL |
| GB20_R075 | 38 | 3,902 | 4,831 | 3,408 | 92,1% | 87,0 | EARLY_SIGNAL |
| GB30_R050 | 38 | 3,879 | 4,818 | 3,340 | 92,1% | 87,0 | EARLY_SIGNAL |
| GB30_R075 | 38 | 3,879 | 4,818 | 3,335 | 92,1% | 87,0 | EARLY_SIGNAL |
| GB40_R050 | 38 | 3,769 | 4,678 | 3,263 | 92,1% | 87,0 | EARLY_SIGNAL |
| GB40_R075 | 38 | 3,769 | 4,678 | 3,258 | 92,1% | 87,0 | EARLY_SIGNAL |
| GB50_R050 | 38 | 3,651 | 4,538 | 3,100 | 92,1% | 87,0 | EARLY_SIGNAL |
| GB50_R075 | 38 | 3,651 | 4,538 | 3,108 | 92,1% | 87,0 | EARLY_SIGNAL |
| ATR15_R050 | 38 | 3,266 | 4,115 | 2,800 | 92,1% | 86,9 | EARLY_SIGNAL |
| GB30_R100 | 38 | 3,766 | 4,818 | 3,156 | 92,1% | 86,9 | EARLY_SIGNAL |
| TP_R075 | 38 | 3,732 | 4,587 | 3,212 | 92,1% | 86,9 | EARLY_SIGNAL |
| GB40_R100 | 38 | 3,654 | 4,678 | 3,048 | 92,1% | 86,9 | EARLY_SIGNAL |
| ATR10_R050 | 38 | 3,653 | 4,641 | 3,141 | 92,1% | 86,9 | EARLY_SIGNAL |
| TP_R060 | 38 | 3,598 | 4,437 | 3,093 | 92,1% | 86,9 | EARLY_SIGNAL |
| GB50_R100 | 38 | 3,542 | 4,538 | 2,989 | 92,1% | 86,9 | EARLY_SIGNAL |
| TP_R050 | 38 | 3,508 | 4,337 | 3,040 | 92,1% | 86,9 | EARLY_SIGNAL |
| TP_R040 | 38 | 3,419 | 4,238 | 2,952 | 92,1% | 86,9 | EARLY_SIGNAL |
| TP_R035 | 38 | 3,374 | 4,188 | 2,922 | 92,1% | 86,9 | EARLY_SIGNAL |
| GB20_R100 | 38 | 3,783 | 4,831 | 3,210 | 92,1% | 86,9 | EARLY_SIGNAL |
| ATR15_R100 | 38 | 3,187 | 4,115 | 2,696 | 92,1% | 86,9 | EARLY_SIGNAL |

## Stati di evidenza

- **INSUFFICIENT_DATA**: meno di 30 trade completi.
- **EARLY_SIGNAL**: da 30 a 49 trade completi.
- **VALIDATING**: campione maggiore, ma robustezza non ancora dimostrata.
- **ROBUST**: test di effetto, stabilità, qualità e outlier superati.
- **ELIGIBLE_FOR_MUTATION**: evidenza sufficiente per proporre una variante al Blocco 5.
- **UNDERPERFORMING**: intervallo statistico stabilmente negativo.

## Protezioni statistiche

Sono utilizzati solo trade osservati integralmente dall'entrata. Il controllo comprende media e mediana normalizzate per rischio, media tagliata, bootstrap deterministico, quattro segmenti temporali, concentrazione dei migliori outlier, ambiguità intrabar e gap di candele.

# Forward Exit Challengers — verifica pulita

Generato: 2026-07-27T00:09:19+00:00

Questi profili sono osservativi e Paper-only. Usano gli stessi trade della madre, ma applicano una specifica uscita Block 3 soltanto ai segnali aperti dopo la loro registrazione.
Nessuna promozione, modifica live o operazione reale viene eseguita automaticamente.

| Challenger | Madre | Scenario | Chiusi | Copertura | PF | PnL | Exp/trade | DD | Stato |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Rapida 1H V1 — giveback 20% dopo +0,5R | SHADOW_1H_FAST | GB20_R050 | 20 | 100,00% | 1,28 | +€103,11 | +€5,16 | 1,41% | COLLECTING |
| Rapida 1H V1 — giveback 30% dopo +0,5R | SHADOW_1H_FAST | GB30_R050 | 20 | 100,00% | 1,11 | +€40,98 | +€2,05 | 1,48% | COLLECTING |
| Relative Strength — giveback 20% dopo +0,5R | SHADOW_RELATIVE_STRENGTH | GB20_R050 | 5 | 100,00% | 2,52 | +€82,07 | +€16,41 | 0,54% | COLLECTING |
| Relative Strength — giveback 30% dopo +0,5R | SHADOW_RELATIVE_STRENGTH | GB30_R050 | 5 | 100,00% | 2,18 | +€63,95 | +€12,79 | 0,54% | COLLECTING |
| Scanner Top 5 BTC Strength — giveback 20% dopo +1,4R | SHADOW_SCANNER_TOP5_BTC | GB20_R140 | 0 | 0,00% | 0,00 | €0,00 | €0,00 | 0,00% | COLLECTING |
| Master Adaptive Consensus — breakeven dopo +0,2R | SHADOW_MASTER_ADAPTIVE_V1 | BE_A020 | 0 | 0,00% | 0,00 | €0,00 | €0,00 | 0,00% | COLLECTING |
| Momentum Breakout V3 Filtered — giveback 20% dopo +1,0R | SHADOW_1H_FAST_V3 | GB20_R100 | 0 | 0,00% | 0,00 | €0,00 | €0,00 | 0,00% | COLLECTING |
| Momentum Breakout — giveback 20% dopo +1,4R | SHADOW_1H_FAST | GB20_R140 | 0 | 0,00% | 0,00 | €0,00 | €0,00 | 0,00% | COLLECTING |

## Regole di valutazione

- Prima fotografia a 30 trade indipendenti.
- Revisione per possibile promozione a 50 trade indipendenti.
- PF minimo 1,50, expectancy e PnL positivi, drawdown massimo 15%, copertura minima 90%.
- PF deve superare la madre e il drawdown non deve essere peggiore sulla stessa serie di trade.
- La promozione resta una decisione umana protetta; il rollback viene predisposto soltanto in fase di approvazione.

# Blocco 4.5 — Crash Cascade Guard

Generato: 2026-07-27T00:08:36+00:00

> Paper-only. In mercato NORMAL/WATCH non riduce i segnali. Le limitazioni iniziano soltanto in STRESS, RECOVERY, CRASH, EXTREME o con dati non affidabili.

## Stato corrente

- Livello: **NORMAL**
- Direzione: **NONE**
- Segnali bloccati nel ciclo: **0**
- Simulazioni bloccate attive: **94**
- Simulazioni completate nel ciclo: **0**
- Liquidazioni virtuali evitate totali: **0**
- Valore cumulato del filtro: **12.22 R**
- Profitto virtuale mancato: **163.76 R**

## Stress test portafogli Paper

| Scenario | Posizioni interessate | Liquidazioni stimate | Perdita stimata EUR |
| --- | ---: | ---: | ---: |
| DOWN_10 | 291 | 0 | 24723.28 |
| DOWN_20 | 291 | 0 | 49446.56 |
| DOWN_30 | 291 | 12 | 74312.61 |
| DOWN_40 | 291 | 148 | 90762.50 |
| UP_10 | 105 | 2 | 13984.75 |
| UP_20 | 105 | 3 | 27909.50 |
| UP_30 | 105 | 3 | 41665.63 |
| UP_40 | 105 | 49 | 50084.13 |

## Modello di esecuzione

Se una candela di cascata attraversa nello stesso intervallo sia lo stop sia il prezzo di liquidazione, il Paper usa il caso peggiore e registra una liquidazione intrabar. Gli stop in gap o in regime di stress ricevono slippage aggiuntivo.

## Requisiti prima del live futures

- modalità ISOLATED obbligatoria;
- stop nativo sull'exchange;
- conferma dello stop prima di accettare la posizione;
- cross margin vietato.

# Blocco 5 — Candidati evolutivi controllati

Generato: 2026-07-27T00:08:12+00:00

> Paper-only. Nessuna promozione, sostituzione del MASTER, modifica live o ordine reale.

## Stato

- Candidati attivi: **12**
- Nuovi candidati nel ciclo: **0**
- Evidenze rifiutate nel ciclo: **0**
- Promozioni automatiche: **0**
- Pensionamenti automatici: **0**

## Regola di mutazione

Ogni candidato è una copia indipendente del genitore e cambia un solo parametro scalare. Il file principale paper_trading_config.json non viene riscritto.

## Candidati attivi

| Candidato | Genitore | Parametro | Vecchio | Nuovo | Scenario |
| --- | --- | --- | ---: | ---: | --- |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | reward_risk | 1.5 | 2.0 | TP_R200 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | SHADOW_1H_FAST_V3 | reward_risk | 1.5 | 2.0 | TP_R200 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V1 | reward_risk | 1.5 | 2.0 | TP_R200 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | reward_risk | 1.5 | 2.0 | TP_R200 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_V1 | reward_risk | 1.5 | 2.0 | TP_R200 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | SHADOW_1H_FAST_V3_LONG_ONLY_V1 | reward_risk | 1.5 | 2.0 | TP_R200 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONLY_V1 | reward_risk | 1.5 | 2.0 | TP_R200 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | SHADOW_1H_FAST_V3_NOHIGH_V1 | reward_risk | 1.5 | 2.0 | TP_R200 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | SHADOW_1H_FAST_V3_CAP75_V1 | reward_risk | 1.5 | 2.0 | TP_R200 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_GUARD_V1 | reward_risk | 1.5 | 2.0 | TP_R200 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | reward_risk | 1.5 | 2.0 | TP_R200 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_V1 | reward_risk | 1.5 | 2.0 | TP_R200 |

## Vincoli v1

- Supportati: FIXED_R, TIME_EXIT e ATR_TRAIL solo quando richiede una singola variazione.
- MFE_GIVEBACK e BREAKEVEN non vengono approssimati: restano evidenze da implementare in una versione successiva.
- Nessun candidato può diventare MASTER nel Blocco 5.

# Blocco 6 — Validazione Champion/Challenger

Generato: 2026-07-27T00:09:20+00:00

> Paper-only. Confronto sulle stesse entrate tramite `experiment_group_id`. Nessuna promozione, sostituzione, pensione o modifica live automatica.

## Stato

- Candidati valutati: **12**
- Pronti per revisione promozione: **0**
- Promozioni automatiche: **0**
- Pensionamenti automatici: **0**

## Confronto

| Candidato | Genitore | Stato | Coppie | Δ medio R | CI basso | PF cand. | PF gen. | DD cand. | DD gen. | Score |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | SHADOW_1H_FAST_V3 | INCUBATING | 0 | 0.000 | 0.000 | 0.00 | 0.00 | 0.00 | 0.00 | 20.0 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | SHADOW_1H_FAST_V3_CAP75_V1 | INCUBATING | 0 | 0.000 | 0.000 | 0.00 | 0.00 | 0.00 | 0.00 | 20.0 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | SHADOW_1H_FAST_V3_LONG_ONLY_V1 | INCUBATING | 0 | 0.000 | 0.000 | 0.00 | 0.00 | 0.00 | 0.00 | 20.0 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | SHADOW_1H_FAST_V3_NOHIGH_V1 | INCUBATING | 0 | 0.000 | 0.000 | 0.00 | 0.00 | 0.00 | 0.00 | 20.0 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | INCUBATING | 0 | 0.000 | 0.000 | 0.00 | 0.00 | 0.00 | 0.00 | 20.0 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | INCUBATING | 0 | 0.000 | 0.000 | 0.00 | 0.00 | 0.00 | 0.00 | 20.0 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_V1 | INCUBATING | 0 | 0.000 | 0.000 | 0.00 | 0.00 | 0.00 | 0.00 | 20.0 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONLY_V1 | INCUBATING | 0 | 0.000 | 0.000 | 0.00 | 0.00 | 0.00 | 0.00 | 20.0 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_GUARD_V1 | INCUBATING | 0 | 0.000 | 0.000 | 0.00 | 0.00 | 0.00 | 0.00 | 20.0 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | INCUBATING | 0 | 0.000 | 0.000 | 0.00 | 0.00 | 0.00 | 0.00 | 20.0 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V1 | INCUBATING | 0 | 0.000 | 0.000 | 0.00 | 0.00 | 0.00 | 0.00 | 20.0 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_V1 | INCUBATING | 0 | 0.000 | 0.000 | 0.00 | 0.00 | 0.00 | 0.00 | 20.0 |

## Gate di sicurezza

- Solo trade chiusi dopo la creazione della candidata.
- Solo coppie con lo stesso evento d’ingresso.
- Solo dati `FULL_FROM_ENTRY` e risk model `block4_5_v1`.
- Campione, bootstrap, stabilità temporale, dipendenza dai migliori trade, PF, drawdown e liquidazioni.
- `PROMOTION_REVIEW_READY` è soltanto una raccomandazione: richiede approvazione umana e un blocco successivo.

# Blocco 7 — Governance promozioni Paper

Generato: 2026-07-27T00:09:20+00:00

> Nessuna promozione automatica. Approvazione umana e comando di esecuzione separato sono obbligatori.

## Stato

- Piani totali: **0**
- In attesa di approvazione: **0**
- Approvati ma non eseguiti: **0**
- Promozioni Paper attive: **0**
- Promozioni automatiche: **0**
- Rollback automatici: **0**

## Piani

| Piano | Candidata | Genitore | Stato | Review hash |
| --- | --- | --- | --- | --- |
| — | — | — | Nessun piano | — |

## Sicurezza

- Il piano è legato all’hash esatto della valutazione Block 6.
- Approvazione e esecuzione sono due azioni manuali distinte.
- Prima della promozione candidata e genitore devono essere senza posizioni aperte.
- Il genitore diventa `EX_MASTER` ma resta attivo in Paper.
- Ogni transazione ha backup e rollback esplicito.

# Blocco 8 — Sorveglianza post-promozione

Generato: 2026-07-27T00:09:20+00:00

> Paper-only. Il nuovo MASTER viene confrontato con l’EX_MASTER sugli stessi eventi successivi alla promozione. Nessun rollback automatico.

## Stato

- Promozioni attive monitorate: **0**
- Rollback raccomandati: **0**
- Critici: **0**
- Rollback automatici: **0**

## Confronto MASTER / EX_MASTER

| Famiglia | MASTER | EX_MASTER | Stato | Coppie | Δ medio R | CI alto | PF M | PF EX | DD ratio | Liq M/EX | Score |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| — | — | — | Nessuna promozione attiva | 0 | 0 | 0 | 0 | 0 | 0 | 0/0 | 0 |

## Sicurezza

- Solo trade chiusi dopo l’esecuzione della promozione.
- Solo coppie con lo stesso `experiment_group_id`, asset e lato.
- Solo dati `FULL_FROM_ENTRY` con risk model `block4_5_v1`.
- `ROLLBACK_RECOMMENDED` non esegue nulla: richiede il comando umano del Blocco 7.
- MASTER, EX_MASTER, stato promozione e live non vengono modificati.

# Blocco 9 — Hall of Fame e memoria genetica

Generato: 2026-07-27T00:09:20+00:00

> Paper-only. La memoria può bloccare soltanto una futura proposta Block 5 classificata AVOID; non modifica strategie esistenti.

## Stato

- Strategie/portafogli valutati: **137**
- Hall of Fame: **20**
- Memorie genetiche: **2**
- Firme bloccate: **0**
- Azioni automatiche e live: **0**

## Hall of Fame

| Rank | Strategia | Stato | Score | Grade | Trade | PF | Expectancy R | DD R |
| ---: | --- | --- | ---: | --- | ---: | ---: | ---: | ---: |
| 1 | SHADOW_SCANNER_TOP5_LONG | BASELINE | 18.8 | E | 36 | 1.81 | 0.342 | 5.75 |
| 2 | SHADOW_1H_FAST_NOHIGH_CAP75_V1 | BASELINE | 16.8 | E | 50 | 1.52 | 0.210 | 5.40 |
| 3 | SHADOW_1H_BALANCED_V3 | BASELINE | 16.7 | E | 46 | 1.54 | 0.231 | 3.23 |
| 4 | SHADOW_1H_FAST_V3_CAP75_V1 | BASELINE | 16.0 | E | 45 | 1.47 | 0.179 | 3.68 |
| 5 | SHADOW_1H_FAST_V3 | BASELINE | 15.1 | E | 74 | 1.26 | 0.103 | 5.36 |
| 6 | SHADOW_1H_FAST_SCORE_6_75_V1 | BASELINE | 14.9 | E | 48 | 1.37 | 0.141 | 3.71 |
| 7 | SHADOW_1H_FAST_NO_PEPE_V1 | BASELINE | 13.4 | E | 42 | 1.30 | 0.123 | 3.55 |
| 8 | SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | BASELINE | 11.9 | E | 48 | 1.17 | 0.074 | 4.74 |
| 9 | SHADOW_1H_BALANCED | BASELINE | 11.8 | E | 47 | 1.51 | 0.198 | 4.17 |
| 10 | SHADOW_1H_FAST_V3_NOHIGH_V1 | BASELINE | 11.4 | E | 49 | 1.13 | 0.060 | 5.53 |

## Memoria genetica

| Scope | Famiglia | Mutazione | Target | Stato | Score | Prove | Coppie | Blocco |
| --- | --- | --- | --- | --- | ---: | ---: | ---: | --- |
| FAMILY | momentum_breakout_v3_filtered | reward_risk INCREASE | 2 | INSUFFICIENT | 62.5 | 12 | 0 | NO |
| GLOBAL | GLOBAL | reward_risk INCREASE | 2 | INSUFFICIENT | 62.5 | 12 | 0 | NO |

## Sicurezza

- Nessuna strategia, posizione o promozione esistente viene modificata.
- Nessuna mutazione, promozione, pensionamento o rollback automatico.
- Nessun effetto live e nessun ordine reale.

# Blocco 10 — Regime Fitness e specializzazione

Generato: 2026-07-27T00:09:20+00:00

> Paper-only e advisory. Il blocco misura quali strategie funzionano nei diversi regimi, ma non cambia automaticamente strategia o posizione.

## Stato

- Regime corrente: **RANGE**
- Righe di performance: **481**
- Strategie preferite nel regime corrente: **4**
- Strategie da evitare nel regime corrente: **2**
- Memorie contestuali: **230**
- Routing automatico: **NO**

## Classifica del regime corrente

| Rank | Portafoglio | Famiglia | Stato | Fitness | Trade | PF | Expectancy R | DD R |
| ---: | --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| 1 | SHADOW_BTC_BOLLINGER_1H | shadow-btc-bollinger-1h | INSUFFICIENT | 81.2 | 3 | 99.00 | 1.115 | 0.00 |
| 2 | SHADOW_SOL_BOLLINGER_4H | shadow-sol-bollinger-4h | INSUFFICIENT | 80.4 | 1 | 99.00 | 1.740 | 0.00 |
| 3 | SHADOW_BTC_BOLLINGER_4H | shadow-btc-bollinger-4h | INSUFFICIENT | 80.4 | 1 | 99.00 | 1.682 | 0.00 |
| 4 | SHADOW_DOGE_DONCHIAN_1H | shadow-doge-donchian-1h | INSUFFICIENT | 80.1 | 3 | 99.00 | 0.374 | 0.00 |
| 5 | SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V1 | shadow-1h-fast-v3-nohigh-range-only-v1 | INSUFFICIENT | 80.0 | 8 | 3.52 | 0.682 | 2.17 |
| 6 | EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | momentum_breakout_v3_filtered | INSUFFICIENT | 79.1 | 4 | 411.09 | 0.784 | 0.01 |
| 7 | SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_V1 | shadow-1h-fast-v3-nohigh-regime-guard-v1 | OBSERVING | 79.0 | 12 | 3.74 | 0.730 | 2.17 |
| 8 | EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | momentum_breakout_v3_filtered | INSUFFICIENT | 78.8 | 7 | 5.19 | 0.622 | 1.03 |
| 9 | EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | momentum_breakout_v3_filtered | INSUFFICIENT | 78.0 | 7 | 3.24 | 0.661 | 1.54 |
| 10 | EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | momentum_breakout_v3_filtered | INSUFFICIENT | 77.5 | 4 | 4.27 | 0.843 | 1.03 |

## Sicurezza

- Il regime viene assegnato usando solo l'ultimo record noto prima dell'entrata del trade.
- Nessun uso di dati futuri per classificare il trade.
- Il Candidate Regime Gate è advisory per impostazione predefinita.
- Nessun cambio automatico di MASTER, posizione o live.

# Blocco 11 — Collegamento protetto al live

Generato: 2026-07-27T00:09:20+00:00

> Modalità LOCKED_REVIEW_ONLY. Il blocco prepara piani immutabili, ma non può modificare il bot reale o inviare ordini.

## Stato

- Promozioni Paper esaminate: **0**
- Pronte per revisione live: **0**
- Evidenza pronta ma adattatore bloccato: **0**
- Approvate in attesa di esecuzione esplicita: **0**
- Adattatore live configurato: **NO**
- Esecuzione live automatica: **NO**
- Ordini inviati: **0**

## Target iniziale

- Profilo: **SOL_SPOT_100_EUR**
- Solo SOL/USDT Spot
- Capitale massimo 100 €
- Una sola posizione
- Ingressi 10–20 €
- Nessun reinvestimento automatico

## Piani

| Piano | Candidata | Stato | Dominio | Validation | Post | Score | SOL trade | Regime | Crash |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- |
| — | Nessuna promozione Paper eseguita | WAITING | — | 0 | 0 | 0 | 0 | — | — |

## Sicurezza

- Non vengono modificati `sol_spot_live_guarded.py`, `sol_spot_live_config.json`, `sol-live.service` o `sol-live.timer`.
- Un rilascio potrà cambiare un solo parametro e un solo dominio tra ENTRY, EXIT o RISK.
- Approvazione ed esecuzione sono due atti umani distinti.
- Prima dell’esecuzione saranno obbligatori backup transazionale, versione precedente e piano di rollback.
- L’adattatore reale resta bloccato finché non viene verificato separatamente sul codice live corrente.

# Blocco 12 — Evolution Control Tower

Generato: 2026-07-27T00:08:36+00:00

> Ultimo livello di osservabilità della pipeline. Non ripara, non riavvia, non modifica strategie o posizioni e non invia ordini.

## Stato generale

- Salute: **DEGRADED**
- Pipeline completa: **SI**
- Live bloccato: **SI**
- Persistenza completa: **SI**
- Catena audit valida: **SI**
- Recovery readiness: **READY**
- Controlli: **34**
- Warning: **1**
- Critici: **0**

## Controlli non superati

| Categoria | Controllo | Stato | Severità | Dettaglio |
| --- | --- | --- | --- | --- |
| SYSTEMD | sol_live_timer | WARN | WARN | Osservazione read-only: nessun servizio viene riavviato o modificato. |

## Sicurezza

- Riparazioni automatiche: **0**
- Riavvii automatici: **0**
- Mutazioni/promozioni/rollback/rilasci automatici: **0**
- Modifiche live: **NO**
- Ordini reali: **0**
