# Paper trading automatico KuCoin

Generato: 2026-07-27T04:24:30+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-07-27T04:23:25+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-07-27T04:23:25+00:00 | 2026-07-27T04:23:25+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-07-27T04:00:00+00:00 | 2026-07-27T04:00:00+00:00 | 8,5 min | 25,0 min | OK |
| 60m | 12 | 2026-07-27T03:00:00+00:00 | 2026-07-27T03:00:00+00:00 | 23,5 min | 45,0 min | OK |
| 240m | 12 | 2026-07-27T00:00:00+00:00 | 2026-07-27T00:00:00+00:00 | 23,5 min | 1,00 h | OK |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | BANK | 240m | LONG | 6,25 | 6,00 | 0,00 | RISK_GATE | 23,5 min | D: n/a | W: n/a | peso 0 | Filtro rischio/esecuzione: asset già aperto nel portafoglio. |
| Principale 4H | EUL | 240m | LONG | 5,75 | 6,00 | 0,25 | BELOW_SCORE | 23,5 min | D: n/a | W: n/a | peso 0 | Punteggio +5.75; soglia ±6.00; mancano 0.25 punti. |
| Principale 4H | SHIB | 240m | LONG | 5,75 | 6,00 | 0,25 | BELOW_SCORE | 23,5 min | D: n/a | W: n/a | peso 0 | Punteggio +5.75; soglia ±6.00; mancano 0.25 punti. |
| Bilanciata 1H V2 | BANK | 60m | LONG | 7,00 | 5,50 | 0,00 | STRATEGY_FILTER | 23,5 min | D: n/a | W: n/a | peso 0 | Filtro V2 non superato: regime, EMA, ritorni e RSI; per Rapida V2 servono anche breakout reale, volume e ADX. |
| Rapida 1H V2 | BANK | 60m | LONG | 7,00 | 5,00 | 0,00 | STRATEGY_FILTER | 23,5 min | D: n/a | W: n/a | peso 0 | Filtro V2 non superato: regime, EMA, ritorni e RSI; per Rapida V2 servono anche breakout reale, volume e ADX. |
| Bilanciata 1H V2 | HYPE | 60m | LONG | 6,12 | 5,50 | 0,00 | STRATEGY_FILTER | 23,5 min | D: n/a | W: n/a | peso 0 | Filtro V2 non superato: regime, EMA, ritorni e RSI; per Rapida V2 servono anche breakout reale, volume e ADX. |
| Rapida 1H V2 | HYPE | 60m | LONG | 6,12 | 5,00 | 0,00 | STRATEGY_FILTER | 23,5 min | D: n/a | W: n/a | peso 0 | Filtro V2 non superato: regime, EMA, ritorni e RSI; per Rapida V2 servono anche breakout reale, volume e ADX. |
| Forza relativa 1H V1 | HYPE | 60m | LONG | 6,12 | 4,00 | 0,00 | STRATEGY_FILTER | 23,5 min | D: n/a | W: n/a | peso 0 | Filtro forza relativa: serve almeno ±2,0% contro BTC; valore=+1.87%. |
| Bilanciata 1H V2 | ESPORTS | 60m | SHORT | -5,50 | 5,50 | 0,00 | STRATEGY_FILTER | 23,5 min | D: n/a | W: n/a | peso 0 | Filtro V2 non superato: regime, EMA, ritorni e RSI; per Rapida V2 servono anche breakout reale, volume e ADX. |
| Rapida 1H V2 | ESPORTS | 60m | SHORT | -5,50 | 5,00 | 0,00 | STRATEGY_FILTER | 23,5 min | D: n/a | W: n/a | peso 0 | Filtro V2 non superato: regime, EMA, ritorni e RSI; per Rapida V2 servono anche breakout reale, volume e ADX. |
| Rapida 1H V1 — madre | ETH | 60m | LONG | 4,84 | 4,50 | 0,00 | STRATEGY_FILTER | 23,5 min | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout UP oppure movimento breve ≥1,5%; breakout=NONE, movimento=+1.25%. |
| Rapida V1 — no HIGH + score <7,5 | ETH | 60m | LONG | 4,84 | 4,50 | 0,00 | STRATEGY_FILTER | 23,5 min | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout UP oppure movimento breve ≥1,5%; breakout=NONE, movimento=+1.25%. |
| Rapida V1 — Long + BTC 1–3 + score <7,5 | ETH | 60m | LONG | 4,84 | 4,50 | 0,00 | STRATEGY_FILTER | 23,5 min | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout UP oppure movimento breve ≥1,5%; breakout=NONE, movimento=+1.25%. |
| Rapida V1 — senza PEPE | ETH | 60m | LONG | 4,84 | 4,50 | 0,00 | STRATEGY_FILTER | 23,5 min | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout UP oppure movimento breve ≥1,5%; breakout=NONE, movimento=+1.25%. |
| Rapida V1 — target pieno 2R | ETH | 60m | LONG | 4,84 | 4,50 | 0,00 | STRATEGY_FILTER | 23,5 min | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout UP oppure movimento breve ≥1,5%; breakout=NONE, movimento=+1.25%. |
| FAST NoHigh <7,5 · SHORT only | ETH | 60m | LONG | 4,84 | 4,50 | 0,00 | STRATEGY_FILTER | 23,5 min | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout UP oppure movimento breve ≥1,5%; breakout=NONE, movimento=+1.25%. |
| Rapida 1H V1 — madre | PEPE | 60m | LONG | 4,57 | 4,50 | 0,00 | STRATEGY_FILTER | 23,5 min | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout UP oppure movimento breve ≥1,5%; breakout=NONE, movimento=+0.87%. |
| Rapida V1 — no HIGH + score <7,5 | PEPE | 60m | LONG | 4,57 | 4,50 | 0,00 | STRATEGY_FILTER | 23,5 min | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout UP oppure movimento breve ≥1,5%; breakout=NONE, movimento=+0.87%. |
| Rapida V1 — Long + BTC 1–3 + score <7,5 | PEPE | 60m | LONG | 4,57 | 4,50 | 0,00 | STRATEGY_FILTER | 23,5 min | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout UP oppure movimento breve ≥1,5%; breakout=NONE, movimento=+0.87%. |
| Rapida V1 — senza PEPE | PEPE | 60m | LONG | 4,57 | 4,50 | 0,00 | STRATEGY_FILTER | 23,5 min | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout UP oppure movimento breve ≥1,5%; breakout=NONE, movimento=+0.87%. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.778,19 | -2,22% | €-221,81 | €3.000,00 | -7,39% | 5 | 21 | 28,57% | 0,68 | 4,52% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 21 | 741 | CAMPIONE INSUFFICIENTE | 30 (mancano 9) |

- Trade del Principale 4H chiusi: **21**; win rate **28,57%**; profit factor **0,68**.
- Expectancy: **€-11,50** per trade; P&L netto: **€-241,45**; max drawdown: **4,52%**.
- Valutazione: **Servono altri eventi indipendenti prima di trarre conclusioni.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 5 | €9.778,19 | €1.075,94 | €3.227,82 | €146,89 | €21,32 |
| TEST | Bilanciata 1H V3 Filtered | 7 | €10.594,16 | €706,14 | €2.118,41 | €212,00 | €14,26 |
| TEST | Scanner Top 5 Long 1H | 6 | €10.531,64 | €3.318,14 | €6.636,28 | €210,26 | €12,69 |
| TEST | Benchmark Donchian breakout 1H | 5 | €10.526,69 | €3.557,51 | €7.115,02 | €157,48 | €59,70 |
| TEST | Rapida V1 — no HIGH + score <7,5 | 5 | €10.454,85 | €1.645,11 | €4.935,33 | €208,71 | €-1,95 |
| TEST | Rapida V3 — score <7,5 | 5 | €10.409,36 | €861,02 | €2.583,07 | €208,63 | €-6,21 |
| TEST | Rapida V1 — score 6–7,5 | 6 | €10.358,35 | €2.070,61 | €6.211,82 | €206,97 | €28,99 |
| TEST | Bilanciata 1H V1 | 5 | €10.336,65 | €2.449,02 | €7.347,06 | €154,40 | €29,72 |
| TEST | Scanner Top 5 + forza BTC 1H | 6 | €10.327,05 | €3.043,10 | €6.086,20 | €206,42 | €26,50 |
| TEST | Rapida V3 NoHigh — Regime Guard | 3 | €10.320,97 | €348,84 | €1.046,53 | €104,43 | €-0,89 |
| TEST | Rapida score 6–7,5 — Cost Aware | 5 | €10.318,54 | €2.052,47 | €6.157,42 | €205,89 | €28,71 |
| TEST | Rapida score 6–7,5 — Range Only | 4 | €10.276,88 | €961,67 | €2.885,01 | €205,93 | €-19,03 |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 5 | €10.275,75 | €3.027,93 | €9.083,78 | €205,09 | €10,44 |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 6 | €10.239,14 | €2.874,96 | €8.624,87 | €204,28 | €32,57 |
| TEST | Rapida V3 NoHigh — Range Only | 3 | €10.224,63 | €474,81 | €1.424,44 | €153,41 | €3,70 |
| TEST | Rapida V3 senza ESPORTS — MFE Lock | 6 | €10.220,65 | €2.833,88 | €8.501,63 | €204,05 | €-1,30 |
| TEST | Rapida score 6–7,5 — senza Trend Up | 4 | €10.216,01 | €837,63 | €2.512,89 | €204,36 | €-5,51 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 6 | €10.205,05 | €2.854,25 | €8.562,74 | €203,56 | €22,79 |
| TEST | Combo Adaptive — madre | 4 | €10.203,22 | €2.162,62 | €4.325,23 | €204,07 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 4 | €10.203,15 | €573,76 | €1.721,28 | €106,53 | €63,66 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 7 | €10.179,48 | €754,54 | €2.263,61 | €203,46 | €30,51 |
| TEST | Combo Adaptive — Side × Regime Guard | 4 | €10.178,52 | €1.111,65 | €2.223,29 | €203,76 | €-2,38 |
| TEST | Rapida 1H V3 Filtered — madre | 5 | €10.169,13 | €2.718,68 | €8.156,04 | €203,52 | €10,91 |
| TEST | Btc Bollinger 1H | 0 | €10.168,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 senza ESPORTS — Long Only | 6 | €10.161,65 | €2.812,05 | €8.436,15 | €202,74 | €30,67 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 5 | €10.144,83 | €2.972,21 | €8.916,64 | €202,48 | €9,92 |
| TEST | MAIN — Dynamic Asset Selector | 2 | €10.143,99 | €281,44 | €844,31 | €101,32 | €1,25 |
| TEST | Combo Mean Reversion | 1 | €10.138,28 | €225,46 | €450,91 | €50,00 | €0,00 |
| TEST | FAST NoHigh <7,5 · SHORT only | 6 | €10.133,06 | €2.726,48 | €8.179,43 | €202,50 | €33,36 |
| TEST | Combo Trend — Side × Regime Guard | 7 | €10.125,62 | €870,68 | €1.741,36 | €202,51 | €12,93 |
| TEST | Rapida V1 — senza PEPE | 5 | €10.110,86 | €2.703,16 | €8.109,49 | €202,36 | €10,83 |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 5 | €10.105,26 | €1.713,96 | €5.141,89 | €201,85 | €-24,35 |
| TEST | Bilanciata 1H V2 | 4 | €10.098,02 | €1.501,59 | €4.504,76 | €152,55 | €0,00 |
| TEST | MAIN — Side × Regime Guard | 4 | €10.094,36 | €746,77 | €2.240,31 | €151,34 | €6,94 |
| TEST | Sol Donchian 1H | 0 | €10.092,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Ema 1H | 0 | €10.091,86 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 4H | 0 | €10.086,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 4H | 0 | €10.084,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 3 | €10.074,32 | €3.881,73 | €11.645,20 | €151,14 | €3,53 |
| TEST | Combo Adaptive — 75% a 2R + runner 25% a 3R | 5 | €10.073,28 | €2.266,98 | €4.533,96 | €201,30 | €0,00 |
| TEST | Combo Adaptive — Quality7 | 5 | €10.064,81 | €2.209,40 | €4.418,81 | €201,32 | €-0,96 |
| TEST | Rapida V3 senza ESPORTS — Stress Guard | 3 | €10.046,63 | €3.871,07 | €11.613,20 | €150,72 | €3,52 |
| TEST | Top 5 + BTC — 75% a 2,2R + runner 3R | 5 | €10.044,22 | €2.971,51 | €5.943,02 | €200,41 | €25,73 |
| TEST | Rapida V1 — Long + BTC 1–3 + score <7,5 | 5 | €10.040,61 | €3.596,92 | €10.790,75 | €200,34 | €15,10 |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 2 | €10.036,73 | €531,37 | €1.594,12 | €101,57 | €-18,84 |
| TEST | Rapida V1 — target pieno 2R | 6 | €10.023,94 | €2.057,79 | €6.173,38 | €200,85 | €10,03 |
| TEST | Bilanciata V3 · LONG only | 5 | €10.020,79 | €1.377,13 | €4.131,39 | €151,02 | €66,45 |
| TEST | Top 5 + BTC — target pieno 3R | 5 | €10.019,59 | €2.948,47 | €5.896,95 | €199,93 | €25,13 |
| TEST | Rapida 1H V2 | 3 | €10.018,77 | €4.383,00 | €13.149,00 | €150,74 | €-20,18 |
| TEST | Btc Adaptive 1H | 0 | €10.013,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €10.010,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Bollinger 1H | 1 | €10.008,78 | €1.391,03 | €4.173,10 | €50,08 | €-4,16 |
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
| TEST | Bilanciata 1H — SHORT Trend Down stretto | 0 | €9.995,87 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €50 · 15x | 0 | €9.994,81 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €50 · 15x | 0 | €9.992,50 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · prudente · 5x | 0 | €9.990,24 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · prudente · 5x | 0 | €9.988,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · prudente · 5x | 0 | €9.983,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 — Long + no HIGH + score <7,5 | 5 | €9.981,53 | €1.006,19 | €3.018,56 | €199,90 | €-27,04 |
| TEST | Btc Donchian 1H | 0 | €9.980,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 5 | €9.979,58 | €2.902,70 | €8.708,09 | €199,19 | €9,20 |
| TEST | Sol Ema 1H | 0 | €9.977,09 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 0 | €9.976,99 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V1 — madre | 2 | €9.974,17 | €1.645,02 | €4.935,06 | €99,89 | €0,00 |
| TEST | Combo Adaptive — Long Only | 5 | €9.963,78 | €2.701,47 | €5.402,94 | €199,28 | €-0,31 |
| TEST | Rapida V3 — senza ESPORTS | 5 | €9.962,03 | €2.662,83 | €7.988,50 | €199,38 | €10,69 |
| TEST | Rapida V3 — qualità completa + profit lock | 6 | €9.961,16 | €2.770,05 | €8.310,14 | €198,75 | €31,05 |
| TEST | Forza relativa 1H V2 | 5 | €9.957,12 | €2.775,20 | €5.550,40 | €199,21 | €20,05 |
| TEST | Eth Ema 4H | 1 | €9.956,12 | €1.036,30 | €2.072,59 | €49,74 | €10,25 |
| TEST | Btc Ema 4H | 0 | €9.950,68 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 4H | 0 | €9.950,68 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 4H | 0 | €9.949,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Profit Lock V1 | 3 | €9.944,39 | €1.371,54 | €2.743,08 | €99,39 | €66,38 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.944,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 4H | 1 | €9.936,18 | €761,04 | €1.522,08 | €49,74 | €-11,55 |
| TEST | Rapida V3 — no volatilità HIGH | 5 | €9.935,10 | €2.655,64 | €7.966,91 | €198,84 | €10,66 |
| TEST | Sol Donchian 4H | 1 | €9.934,92 | €830,21 | €1.660,43 | €49,74 | €-12,59 |
| TEST | Benchmark trend following EMA 1H | 5 | €9.931,14 | €1.028,81 | €2.057,63 | €199,83 | €-32,33 |
| TEST | Combo Adaptive — target pieno 3R | 4 | €9.929,58 | €2.226,41 | €4.452,81 | €198,61 | €0,00 |
| TEST | Eth Donchian 1H | 1 | €9.927,31 | €1.292,62 | €3.877,86 | €49,64 | €2,31 |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | 3 | €9.927,11 | €1.372,84 | €2.745,68 | €149,15 | €3,57 |
| TEST | Top 5 + BTC — Guard + BTC≤3 | 4 | €9.923,91 | €1.302,99 | €2.605,98 | €153,07 | €0,59 |
| TEST | Combo Adaptive — Trend/Transition | 5 | €9.921,75 | €2.294,73 | €4.589,46 | €198,16 | €-0,55 |
| TEST | Top 5 + BTC — BTC≤3 | 5 | €9.918,23 | €2.934,05 | €5.868,09 | €197,90 | €25,34 |
| TEST | Ampia 4H | 4 | €9.917,00 | €1.734,53 | €3.469,06 | €199,10 | €-28,42 |
| TEST | Sol Ema 4H | 1 | €9.913,15 | €862,58 | €1.725,17 | €49,74 | €-34,09 |
| TEST | Btc Ema 1H | 0 | €9.911,86 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Scanner | 5 | €9.905,86 | €2.916,01 | €5.832,02 | €197,64 | €25,71 |
| TEST | Sol Bollinger 1H | 0 | €9.901,25 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Benchmark Bollinger mean reversion 1H | 2 | €9.901,16 | €3.973,66 | €7.947,32 | €95,37 | €-30,68 |
| TEST | Doge Bollinger 1H | 0 | €9.888,87 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Top 5 + BTC — BTC 2–3 | 4 | €9.879,62 | €2.598,90 | €5.197,81 | €198,61 | €-49,81 |
| TEST | Bilanciata 1H — LONG senza Range High Vol | 4 | €9.869,63 | €1.411,99 | €4.235,97 | €197,36 | €2,30 |
| TEST | Combo Adaptive — Quality7 + Regime + parziale 1R | 3 | €9.862,84 | €2.159,53 | €4.319,06 | €148,43 | €-0,92 |
| TEST | Master Adaptive GB20 — 50% a 0,75R | 4 | €9.861,37 | €2.097,17 | €4.194,35 | €197,11 | €6,48 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 5 | €9.858,71 | €2.676,86 | €8.030,58 | €196,70 | €31,04 |
| TEST | Eth Adaptive 1H | 1 | €9.853,88 | €1.140,50 | €3.421,49 | €49,27 | €2,04 |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 5 | €9.853,00 | €1.383,14 | €4.149,41 | €196,60 | €23,00 |
| TEST | Scanner Top10 Long | 5 | €9.845,44 | €2.732,16 | €5.464,31 | €197,03 | €-6,84 |
| TEST | Scanner Top15 Long | 5 | €9.845,44 | €2.732,16 | €5.464,31 | €197,03 | €-6,84 |
| TEST | Scanner Top20 Long | 5 | €9.845,44 | €2.732,16 | €5.464,31 | €197,03 | €-6,84 |
| TEST | Sol Adaptive 1H | 0 | €9.835,19 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive GB20 — Breakeven 0,5R | 4 | €9.828,95 | €2.172,56 | €4.345,11 | €196,72 | €-6,79 |
| TEST | Scanner Bottom10 Short | 3 | €9.817,30 | €2.159,38 | €4.318,77 | €98,62 | €65,53 |
| TEST | Scanner Bottom15 Short | 3 | €9.817,30 | €2.159,38 | €4.318,77 | €98,62 | €65,53 |
| TEST | Scanner Bottom20 Short | 3 | €9.817,30 | €2.159,38 | €4.318,77 | €98,62 | €65,53 |
| TEST | Combo Adaptive — Quality7 + Regime | 3 | €9.802,47 | €2.151,60 | €4.303,20 | €147,83 | €-0,92 |
| TEST | Global Confluence puro 1H | 0 | €9.790,66 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive GB20 — Loss Cap 0,75R | 4 | €9.788,51 | €2.761,06 | €5.522,12 | €195,96 | €-9,08 |
| TEST | Eth Ema 1H | 1 | €9.781,75 | €1.132,15 | €3.396,44 | €48,91 | €2,03 |
| TEST | Scanner Bottom 5 Short 1H | 3 | €9.770,87 | €1.786,26 | €3.572,51 | €48,61 | €65,28 |
| TEST | Rapida V3 — Long Only | 4 | €9.752,58 | €1.654,74 | €4.964,21 | €195,84 | €-24,76 |
| TEST | Top 5 + BTC — Guard | 4 | €9.752,32 | €1.414,44 | €2.828,89 | €195,02 | €1,47 |
| TEST | Top 5 + BTC — solo MFE | 5 | €9.726,54 | €4.066,51 | €8.133,03 | €194,40 | €20,94 |
| TEST | Combo Adaptive — parziale 1R | 6 | €9.687,14 | €2.560,56 | €5.121,12 | €193,65 | €5,39 |
| TEST | Master Adaptive Expanded V1 | 5 | €9.668,95 | €1.517,94 | €3.035,87 | €193,52 | €-6,67 |
| TEST | Master Adaptive Gb20 V1 | 4 | €9.639,07 | €2.651,80 | €5.303,60 | €192,93 | €-7,00 |
| TEST | Master Adaptive Runner25 V1 | 5 | €9.634,27 | €1.504,30 | €3.008,60 | €192,82 | €-6,67 |
| TEST | Master Adaptive No Alt V1 | 5 | €9.629,28 | €1.504,28 | €3.008,56 | €192,72 | €-6,65 |
| TEST | Master Adaptive V1 | 5 | €9.625,31 | €1.503,85 | €3.007,70 | €192,64 | €-6,63 |
| TEST | Top 5 + BTC — Guard + BTC≤3 + MFE | 4 | €9.622,84 | €2.501,62 | €5.003,23 | €192,97 | €-18,31 |
| TEST | Forza relativa 1H V1 | 5 | €9.614,31 | €2.835,04 | €5.670,08 | €191,86 | €22,81 |
| TEST | Combo Trend | 4 | €9.538,90 | €1.541,40 | €3.082,80 | €191,83 | €-39,83 |
| TEST | Combo Adaptive — MFE Trail esistente | 4 | €9.521,88 | €2.034,13 | €4.068,27 | €190,44 | €0,00 |
| TEST | Top 5 + BTC — Guard + MFE | 4 | €9.514,00 | €2.366,28 | €4.732,55 | €190,79 | €-18,01 |
| TEST | Master Adaptive Strict3 V1 | 4 | €9.496,21 | €3.928,81 | €7.857,63 | €189,48 | €24,01 |

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
| PRINCIPALE | Principale 4H | Confluenza trend | €9.778,19 | €-241,45 | 21 | 21 | 28,57% | 0,68 | €-11,50 | 4,52% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €10.594,16 | €581,26 | 46 | 46 | 43,48% | 1,62 | €12,64 | 2,20% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.531,64 | €522,77 | 37 | 37 | 51,35% | 1,61 | €14,13 | 3,57% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €10.526,69 | €472,58 | 26 | 26 | 53,85% | 1,89 | €18,18 | 2,12% |
| TEST | Rapida V1 — no HIGH + score <7,5 | Momentum / breakout | €10.454,85 | €459,76 | 52 | 52 | 48,08% | 1,46 | €8,84 | 2,83% |
| TEST | Rapida V3 — score <7,5 | Momentum / breakout V3 Filtered | €10.409,36 | €417,96 | 45 | 45 | 48,89% | 1,55 | €9,29 | 2,49% |
| TEST | Rapida V1 — score 6–7,5 | Momentum / breakout | €10.358,35 | €333,93 | 49 | 49 | 44,90% | 1,36 | €6,81 | 2,49% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €10.336,65 | €314,65 | 48 | 48 | 50,00% | 1,32 | €6,56 | 3,25% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €10.327,05 | €303,94 | 29 | 29 | 48,28% | 1,43 | €10,48 | 3,23% |
| TEST | Rapida V3 NoHigh — Regime Guard | Momentum / breakout V3 Filtered | €10.320,97 | €322,54 | 16 | 16 | 68,75% | 2,99 | €20,16 | 1,39% |
| TEST | Rapida score 6–7,5 — Cost Aware | Momentum / breakout | €10.318,54 | €293,74 | 13 | 13 | 61,54% | 2,33 | €22,60 | 1,96% |
| TEST | Rapida score 6–7,5 — Range Only | Momentum / breakout | €10.276,88 | €297,12 | 9 | 9 | 66,67% | 3,17 | €33,01 | 2,28% |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | Momentum / breakout V3 Filtered | €10.275,75 | €270,39 | 13 | 13 | 61,54% | 3,37 | €20,80 | 1,97% |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | Momentum / breakout V3 Filtered | €10.239,14 | €211,74 | 18 | 18 | 55,56% | 1,95 | €11,76 | 1,14% |
| TEST | Rapida V3 NoHigh — Range Only | Momentum / breakout V3 Filtered | €10.224,63 | €221,94 | 9 | 9 | 66,67% | 2,37 | €24,66 | 1,78% |
| TEST | Rapida V3 senza ESPORTS — MFE Lock | Momentum / breakout V3 Filtered | €10.220,65 | €227,49 | 24 | 24 | 54,17% | 1,78 | €9,48 | 2,05% |
| TEST | Rapida score 6–7,5 — senza Trend Up | Momentum / breakout | €10.216,01 | €223,23 | 14 | 14 | 64,29% | 1,91 | €15,94 | 2,01% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | Momentum / breakout V3 Filtered | €10.205,05 | €187,05 | 13 | 13 | 53,85% | 1,79 | €14,39 | 1,62% |
| TEST | Combo Adaptive — madre | Combo Adaptive | €10.203,22 | €206,62 | 25 | 25 | 48,00% | 1,52 | €8,26 | 1,49% |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | Momentum / breakout V3 Filtered | €10.203,15 | €140,88 | 12 | 12 | 58,33% | 3,31 | €11,74 | 1,01% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | Momentum / breakout V3 Filtered | €10.179,48 | €151,15 | 11 | 11 | 54,55% | 2,93 | €13,74 | 2,01% |
| TEST | Combo Adaptive — Side × Regime Guard | Combo Adaptive | €10.178,52 | €182,53 | 11 | 11 | 81,82% | 2,69 | €16,59 | 1,41% |
| TEST | Rapida 1H V3 Filtered — madre | Momentum / breakout V3 Filtered | €10.169,13 | €163,17 | 75 | 75 | 38,67% | 1,11 | €2,18 | 2,89% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.168,12 | €168,12 | 3 | 3 | 100,00% | ∞ | €56,04 | 0,54% |
| TEST | Rapida V3 senza ESPORTS — Long Only | Momentum / breakout V3 Filtered | €10.161,65 | €135,66 | 17 | 17 | 58,82% | 1,50 | €7,98 | 1,32% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | Momentum / breakout V3 Filtered | €10.144,83 | €139,85 | 13 | 13 | 46,15% | 1,75 | €10,76 | 2,27% |
| TEST | MAIN — Dynamic Asset Selector | Confluenza trend | €10.143,99 | €142,72 | 4 | 4 | 50,00% | 3,55 | €35,68 | 1,03% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €10.138,28 | €138,67 | 16 | 16 | 43,75% | 1,36 | €8,67 | 2,31% |
| TEST | FAST NoHigh <7,5 · SHORT only | Momentum / breakout | €10.133,06 | €104,61 | 16 | 16 | 56,25% | 1,44 | €6,54 | 1,76% |
| TEST | Combo Trend — Side × Regime Guard | Combo Trend | €10.125,62 | €113,96 | 11 | 11 | 54,55% | 1,68 | €10,36 | 1,32% |
| TEST | Rapida V1 — senza PEPE | Momentum / breakout | €10.110,86 | €104,94 | 43 | 43 | 41,86% | 1,12 | €2,44 | 2,15% |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | Momentum / breakout V3 Filtered | €10.105,26 | €132,29 | 15 | 15 | 46,67% | 1,55 | €8,82 | 1,60% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €10.098,02 | €100,17 | 36 | 34 | 52,78% | 1,13 | €2,78 | 2,75% |
| TEST | MAIN — Side × Regime Guard | Confluenza trend | €10.094,36 | €88,60 | 5 | 5 | 40,00% | 1,81 | €17,72 | 1,49% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €10.092,12 | €92,12 | 3 | 3 | 66,67% | 21,53 | €30,71 | 0,79% |
| TEST | Doge Ema 1H | Trend following EMA | €10.091,86 | €91,86 | 8 | 8 | 62,50% | 1,55 | €11,48 | 1,36% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €10.086,98 | €86,98 | 1 | 1 | 100,00% | ∞ | €86,98 | 0,40% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.084,12 | €84,12 | 1 | 1 | 100,00% | ∞ | €84,12 | 0,30% |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | Momentum / breakout V3 Filtered | €10.074,32 | €77,77 | 8 | 8 | 50,00% | 1,47 | €9,72 | 2,06% |
| TEST | Combo Adaptive — 75% a 2R + runner 25% a 3R | Combo Adaptive | €10.073,28 | €76,55 | 22 | 22 | 45,45% | 1,17 | €3,48 | 2,12% |
| TEST | Combo Adaptive — Quality7 | Combo Adaptive | €10.064,81 | €68,97 | 16 | 16 | 43,75% | 1,38 | €4,31 | 1,51% |
| TEST | Rapida V3 senza ESPORTS — Stress Guard | Momentum / breakout V3 Filtered | €10.046,63 | €50,08 | 13 | 13 | 46,15% | 1,15 | €3,85 | 2,17% |
| TEST | Top 5 + BTC — 75% a 2,2R + runner 3R | Scanner Top 5 + forza BTC | €10.044,22 | €21,80 | 16 | 16 | 50,00% | 1,05 | €1,36 | 3,25% |
| TEST | Rapida V1 — Long + BTC 1–3 + score <7,5 | Momentum / breakout | €10.040,61 | €31,98 | 18 | 18 | 38,89% | 1,09 | €1,78 | 2,07% |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | Momentum / breakout V3 Filtered | €10.036,73 | €56,63 | 6 | 6 | 50,00% | 1,56 | €9,44 | 2,15% |
| TEST | Rapida V1 — target pieno 2R | Momentum / breakout | €10.023,94 | €17,67 | 47 | 47 | 36,17% | 1,02 | €0,38 | 2,58% |
| TEST | Bilanciata V3 · LONG only | Confluenza trend V3 Filtered | €10.020,79 | €-43,30 | 7 | 7 | 28,57% | 0,74 | €-6,19 | 1,46% |
| TEST | Top 5 + BTC — target pieno 3R | Scanner Top 5 + forza BTC | €10.019,59 | €-2,26 | 12 | 12 | 50,00% | 1,00 | €-0,19 | 3,22% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €10.018,77 | €46,84 | 14 | 13 | 50,00% | 1,15 | €3,35 | 1,69% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €10.013,28 | €13,28 | 3 | 3 | 66,67% | 1,24 | €4,43 | 0,89% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €10.010,98 | €10,98 | 9 | 9 | 33,33% | 1,23 | €1,22 | 0,25% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €10.008,78 | €15,45 | 1 | 1 | 100,00% | ∞ | €15,45 | 0,51% |
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
| TEST | Bilanciata 1H — SHORT Trend Down stretto | Confluenza trend | €9.995,87 | €-4,13 | 1 | 1 | 0,00% | 0,00 | €-4,13 | 0,59% |
| TEST | Scalp RSI Long 20 · €50 · 15x | Inversione RSI estrema 15m | €9.994,81 | €-5,19 | 2 | 2 | 0,00% | 0,00 | €-2,59 | 0,08% |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | €9.992,50 | €-7,50 | 1 | 1 | 0,00% | 0,00 | €-7,50 | 0,11% |
| TEST | Scalp RSI Short 80 · prudente · 5x | Inversione RSI estrema 15m | €9.990,24 | €-9,76 | 3 | 3 | 66,67% | 0,28 | €-3,25 | 0,21% |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | €9.988,38 | €-11,62 | 1 | 1 | 0,00% | 0,00 | €-11,62 | 0,17% |
| TEST | Scalp RSI Long 20 · prudente · 5x | Inversione RSI estrema 15m | €9.983,60 | €-16,40 | 2 | 2 | 0,00% | 0,00 | €-8,20 | 0,24% |
| TEST | Rapida V3 — Long + no HIGH + score <7,5 | Momentum / breakout V3 Filtered | €9.981,53 | €10,60 | 36 | 36 | 41,67% | 1,01 | €0,29 | 2,86% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €9.980,62 | €-19,38 | 4 | 4 | 50,00% | 0,82 | €-4,84 | 1,49% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | Momentum / breakout V3 Filtered | €9.979,58 | €-24,39 | 14 | 14 | 50,00% | 0,92 | €-1,74 | 2,38% |
| TEST | Sol Ema 1H | Trend following EMA | €9.977,09 | €-22,91 | 5 | 5 | 40,00% | 0,86 | €-4,58 | 1,67% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €9.976,99 | €-23,01 | 5 | 5 | 20,00% | 0,20 | €-4,60 | 0,37% |
| TEST | Rapida 1H V1 — madre | Momentum / breakout | €9.974,17 | €-23,25 | 76 | 76 | 34,21% | 0,99 | €-0,31 | 6,76% |
| TEST | Combo Adaptive — Long Only | Combo Adaptive | €9.963,78 | €-32,81 | 10 | 10 | 40,00% | 0,86 | €-3,28 | 2,34% |
| TEST | Rapida V3 — senza ESPORTS | Momentum / breakout V3 Filtered | €9.962,03 | €-43,83 | 49 | 49 | 38,78% | 0,96 | €-0,89 | 2,49% |
| TEST | Rapida V3 — qualità completa + profit lock | Momentum / breakout V3 Filtered | €9.961,16 | €-65,50 | 39 | 39 | 48,72% | 0,93 | €-1,68 | 3,21% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €9.957,12 | €-58,57 | 40 | 39 | 37,50% | 0,96 | €-1,46 | 5,10% |
| TEST | Eth Ema 4H | Trend following EMA | €9.956,12 | €-52,88 | 1 | 1 | 0,00% | 0,00 | €-52,88 | 0,80% |
| TEST | Btc Ema 4H | Trend following EMA | €9.950,68 | €-49,32 | 1 | 1 | 0,00% | 0,00 | €-49,32 | 0,96% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €9.950,68 | €-49,32 | 1 | 1 | 0,00% | 0,00 | €-49,32 | 0,96% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €9.949,62 | €-50,38 | 1 | 1 | 0,00% | 0,00 | €-50,38 | 0,74% |
| TEST | Scanner Bottom5 Short Profit Lock V1 | Scanner Bottom 5 Short | €9.944,39 | €-119,98 | 5 | 5 | 40,00% | 0,25 | €-24,00 | 1,53% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.944,12 | €-55,88 | 9 | 9 | 22,22% | 0,16 | €-6,21 | 0,56% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €9.936,18 | €-51,83 | 1 | 1 | 0,00% | 0,00 | €-51,83 | 0,73% |
| TEST | Rapida V3 — no volatilità HIGH | Momentum / breakout V3 Filtered | €9.935,10 | €-70,74 | 50 | 50 | 40,00% | 0,94 | €-1,41 | 2,96% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €9.934,92 | €-52,00 | 1 | 1 | 0,00% | 0,00 | €-52,00 | 0,75% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.931,14 | €-33,95 | 26 | 26 | 38,46% | 0,94 | €-1,31 | 2,25% |
| TEST | Combo Adaptive — target pieno 3R | Combo Adaptive | €9.929,58 | €-66,67 | 13 | 13 | 46,15% | 0,76 | €-5,13 | 1,41% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.927,31 | €-72,68 | 4 | 4 | 25,00% | 0,56 | €-18,17 | 1,38% |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | Scanner Bottom 5 Short | €9.927,11 | €-74,71 | 6 | 6 | 50,00% | 0,54 | €-12,45 | 1,38% |
| TEST | Top 5 + BTC — Guard + BTC≤3 | Scanner Top 5 + forza BTC | €9.923,91 | €-75,25 | 10 | 10 | 40,00% | 0,82 | €-7,52 | 3,23% |
| TEST | Combo Adaptive — Trend/Transition | Combo Adaptive | €9.921,75 | €-74,86 | 11 | 11 | 45,45% | 0,78 | €-6,81 | 2,18% |
| TEST | Top 5 + BTC — BTC≤3 | Scanner Top 5 + forza BTC | €9.918,23 | €-103,74 | 11 | 11 | 45,45% | 0,74 | €-9,43 | 3,23% |
| TEST | Ampia 4H | Confluenza trend | €9.917,00 | €-53,35 | 17 | 17 | 23,53% | 0,89 | €-3,14 | 3,67% |
| TEST | Sol Ema 4H | Trend following EMA | €9.913,15 | €-52,00 | 1 | 1 | 0,00% | 0,00 | €-52,00 | 0,97% |
| TEST | Btc Ema 1H | Trend following EMA | €9.911,86 | €-88,14 | 6 | 6 | 33,33% | 0,59 | €-14,69 | 1,56% |
| TEST | Combo Scanner | Combo Scanner | €9.905,86 | €-116,59 | 34 | 34 | 44,12% | 0,88 | €-3,43 | 3,25% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.901,25 | €-98,75 | 4 | 4 | 25,00% | 0,41 | €-24,69 | 1,89% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €9.901,16 | €-63,39 | 38 | 38 | 39,47% | 0,93 | €-1,67 | 4,19% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €9.888,87 | €-111,13 | 2 | 2 | 0,00% | 0,00 | €-55,56 | 1,26% |
| TEST | Top 5 + BTC — BTC 2–3 | Scanner Top 5 + forza BTC | €9.879,62 | €-67,07 | 4 | 4 | 25,00% | 0,47 | €-16,77 | 2,84% |
| TEST | Bilanciata 1H — LONG senza Range High Vol | Confluenza trend | €9.869,63 | €-130,27 | 9 | 9 | 33,33% | 0,60 | €-14,47 | 2,47% |
| TEST | Combo Adaptive — Quality7 + Regime + parziale 1R | Combo Adaptive | €9.862,84 | €-133,65 | 6 | 6 | 33,33% | 0,37 | €-22,27 | 1,95% |
| TEST | Master Adaptive GB20 — 50% a 0,75R | Master Adaptive Consensus | €9.861,37 | €-142,71 | 6 | 6 | 33,33% | 0,49 | €-23,78 | 2,50% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | Momentum / breakout V3 Filtered | €9.858,71 | €-167,51 | 11 | 11 | 54,55% | 0,45 | €-15,23 | 2,93% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.853,88 | €-146,11 | 5 | 5 | 40,00% | 0,11 | €-29,22 | 1,84% |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | Momentum / breakout V3 Filtered | €9.853,00 | €-167,51 | 11 | 11 | 54,55% | 0,45 | €-15,23 | 3,08% |
| TEST | Scanner Top10 Long | Scanner Top10 Long | €9.845,44 | €-144,63 | 8 | 8 | 37,50% | 0,42 | €-18,08 | 3,62% |
| TEST | Scanner Top15 Long | Scanner Top15 Long | €9.845,44 | €-144,63 | 8 | 8 | 37,50% | 0,42 | €-18,08 | 3,62% |
| TEST | Scanner Top20 Long | Scanner Top20 Long | €9.845,44 | €-144,63 | 8 | 8 | 37,50% | 0,42 | €-18,08 | 3,62% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €9.835,19 | €-164,81 | 6 | 6 | 33,33% | 0,29 | €-27,47 | 2,34% |
| TEST | Master Adaptive GB20 — Breakeven 0,5R | Master Adaptive Consensus | €9.828,95 | €-161,66 | 12 | 12 | 16,67% | 0,55 | €-13,47 | 3,13% |
| TEST | Scanner Bottom10 Short | Scanner Bottom10 Short | €9.817,30 | €-245,28 | 6 | 6 | 16,67% | 0,11 | €-40,88 | 2,72% |
| TEST | Scanner Bottom15 Short | Scanner Bottom15 Short | €9.817,30 | €-245,28 | 6 | 6 | 16,67% | 0,11 | €-40,88 | 2,72% |
| TEST | Scanner Bottom20 Short | Scanner Bottom20 Short | €9.817,30 | €-245,28 | 6 | 6 | 16,67% | 0,11 | €-40,88 | 2,72% |
| TEST | Combo Adaptive — Quality7 + Regime | Combo Adaptive | €9.802,47 | €-194,04 | 6 | 6 | 16,67% | 0,13 | €-32,34 | 2,32% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.790,66 | €-209,34 | 10 | 10 | 30,00% | 0,37 | €-20,93 | 2,92% |
| TEST | Master Adaptive GB20 — Loss Cap 0,75R | Master Adaptive Consensus | €9.788,51 | €-199,77 | 8 | 8 | 25,00% | 0,40 | €-24,97 | 3,61% |
| TEST | Eth Ema 1H | Trend following EMA | €9.781,75 | €-218,24 | 7 | 7 | 28,57% | 0,20 | €-31,18 | 2,52% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.770,87 | €-288,92 | 29 | 29 | 31,03% | 0,61 | €-9,96 | 5,48% |
| TEST | Rapida V3 — Long Only | Momentum / breakout V3 Filtered | €9.752,58 | €-220,06 | 40 | 40 | 35,00% | 0,78 | €-5,50 | 3,67% |
| TEST | Top 5 + BTC — Guard | Scanner Top 5 + forza BTC | €9.752,32 | €-247,74 | 15 | 15 | 26,67% | 0,57 | €-16,52 | 3,33% |
| TEST | Top 5 + BTC — solo MFE | Scanner Top 5 + forza BTC | €9.726,54 | €-290,16 | 20 | 20 | 35,00% | 0,41 | €-14,51 | 3,95% |
| TEST | Combo Adaptive — parziale 1R | Combo Adaptive | €9.687,14 | €-314,39 | 18 | 18 | 33,33% | 0,47 | €-17,47 | 3,32% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €9.668,95 | €-322,63 | 13 | 13 | 30,77% | 0,47 | €-24,82 | 3,62% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €9.639,07 | €-350,75 | 47 | 47 | 57,45% | 0,59 | €-7,46 | 4,16% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €9.634,27 | €-357,32 | 12 | 12 | 25,00% | 0,36 | €-29,78 | 3,97% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €9.629,28 | €-362,33 | 10 | 10 | 20,00% | 0,35 | €-36,23 | 4,02% |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | €9.625,31 | €-366,31 | 10 | 10 | 20,00% | 0,35 | €-36,63 | 4,06% |
| TEST | Top 5 + BTC — Guard + BTC≤3 + MFE | Scanner Top 5 + forza BTC | €9.622,84 | €-356,34 | 25 | 25 | 40,00% | 0,53 | €-14,25 | 3,93% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €9.614,31 | €-405,41 | 28 | 28 | 25,00% | 0,53 | €-14,48 | 6,18% |
| TEST | Combo Trend | Combo Trend | €9.538,90 | €-419,10 | 38 | 38 | 31,58% | 0,71 | €-11,03 | 7,02% |
| TEST | Combo Adaptive — MFE Trail esistente | Combo Adaptive | €9.521,88 | €-475,61 | 29 | 29 | 27,59% | 0,39 | €-16,40 | 5,33% |
| TEST | Top 5 + BTC — Guard + MFE | Scanner Top 5 + forza BTC | €9.514,00 | €-465,78 | 28 | 28 | 35,71% | 0,46 | €-16,63 | 5,08% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €9.496,21 | €-523,41 | 20 | 20 | 25,00% | 0,48 | €-26,17 | 5,48% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | LAB | SHORT | Confluenza trend | 240m | 3,0x | 0,17841 | 0,17841 | 0,17841 | 0,23699 | 0,13559 | €136,26 | €408,77 | €0,00 | €-0,00 |
| Principale 4H | SUI | LONG | Confluenza trend | 240m | 3,0x | 0,76296 | 0,76296 | 0,73998 | 0,51245 | 0,80891 | €547,52 | €1.642,56 | €49,46 | €0,00 |
| Principale 4H | ONDO | LONG | Confluenza trend | 240m | 3,0x | 0,40344 | 0,40344 | 0,37762 | 0,27098 | 0,45509 | €254,70 | €764,09 | €48,91 | €0,00 |
| Principale 4H | BANK | LONG | Confluenza trend | 240m | 3,0x | 0,36220 | 0,38315 | 0,31874 | 0,24328 | 0,44913 | €128,59 | €385,77 | €46,29 | €22,31 |
| Principale 4H | SHIB | LONG | Confluenza trend | 240m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €8,88 | €26,63 | €2,22 | €-0,99 |
| Bilanciata 1H V1 | ADA | SHORT | Confluenza trend | 60m | 3,0x | 0,16703 | 0,16703 | 0,16365 | 0,22187 | 0,16112 | €978,72 | €2.936,17 | €0,00 | €-0,00 |
| Bilanciata 1H V1 | AKE | LONG | Confluenza trend | 60m | 3,0x | 0,00329 | 0,00329 | 0,00290 | 0,00221 | 0,00408 | €12,36 | €37,07 | €4,45 | €0,00 |
| Bilanciata 1H V1 | ALLO | SHORT | Confluenza trend | 60m | 3,0x | 0,36179 | 0,36179 | 0,40521 | 0,48058 | 0,27496 | €141,53 | €424,59 | €50,95 | €-0,00 |
| Bilanciata 1H V1 | BANK | LONG | Confluenza trend | 60m | 3,0x | 0,38137 | 0,38315 | 0,34474 | 0,25615 | 0,45462 | €172,02 | €516,05 | €49,56 | €2,41 |
| Bilanciata 1H V1 | ETH | LONG | Confluenza trend | 60m | 3,0x | 1943,95871 | 1959,42000 | 1915,96571 | 1305,69227 | 1999,94472 | €1.144,39 | €3.433,17 | €49,44 | €27,31 |
| Bilanciata 1H — LONG senza Range High Vol | AKE | LONG | Confluenza trend | 60m | 3,0x | 0,00320 | 0,00320 | 0,00282 | 0,00215 | 0,00397 | €138,85 | €416,55 | €49,99 | €0,00 |
| Bilanciata 1H — LONG senza Range High Vol | BEAT | LONG | Confluenza trend | 60m | 3,0x | 3,29017 | 3,29017 | 3,00714 | 2,20990 | 3,85623 | €193,69 | €581,07 | €49,98 | €0,00 |
| Bilanciata 1H — LONG senza Range High Vol | XMR | LONG | Confluenza trend | 60m | 3,0x | 366,72991 | 366,72991 | 360,04130 | 246,32025 | 380,10712 | €915,26 | €2.745,79 | €50,08 | €0,00 |
| Bilanciata 1H — LONG senza Range High Vol | BANK | LONG | Confluenza trend | 60m | 3,0x | 0,38137 | 0,38315 | 0,34474 | 0,25615 | 0,45462 | €164,19 | €492,56 | €47,31 | €2,30 |
| Bilanciata 1H V2 | ADA | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,16276 | 0,16276 | 0,16511 | 0,21620 | 0,15807 | €1.185,56 | €3.556,68 | €51,22 | €-0,00 |
| Bilanciata 1H V2 | AKE | LONG | Confluenza trend V2 | 60m | 3,0x | 0,00320 | 0,00320 | 0,00282 | 0,00215 | 0,00397 | €142,81 | €428,43 | €51,41 | €0,00 |
| Bilanciata 1H V2 | WLD | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,34349 | 0,34349 | 0,35287 | 0,45627 | 0,32475 | €26,53 | €79,60 | €2,17 | €-0,00 |
| Bilanciata 1H V2 | ALLO | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,35543 | 0,35543 | 0,39400 | 0,47213 | 0,27829 | €146,68 | €440,04 | €47,75 | €-0,00 |
| Bilanciata 1H V3 Filtered | BEAT | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 3,31215 | 3,31215 | 3,02723 | 2,22466 | 3,88198 | €203,36 | €610,09 | €52,48 | €0,00 |
| Bilanciata 1H V3 Filtered | WLD | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,34349 | 0,34349 | 0,35287 | 0,45627 | 0,32475 | €23,43 | €70,29 | €1,92 | €-0,00 |
| Bilanciata 1H V3 Filtered | AKE | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,00330 | 0,00330 | 0,00293 | 0,00221 | 0,00403 | €158,25 | €474,75 | €52,90 | €0,00 |
| Bilanciata 1H V3 Filtered | ALLO | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,34255 | 0,34255 | 0,37914 | 0,45502 | 0,26938 | €160,61 | €481,84 | €51,46 | €-0,00 |
| Bilanciata 1H V3 Filtered | SHIB | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €8,58 | €25,73 | €1,38 | €-0,72 |
| Bilanciata 1H V3 Filtered | ESPORTS | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,02905 | 0,02804 | 0,03254 | 0,03859 | 0,02208 | €142,96 | €428,87 | €51,46 | €14,97 |
| Bilanciata 1H V3 Filtered | ETH | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1958,25157 | 1959,42000 | 1930,05275 | 1315,29231 | 2014,64922 | €8,95 | €26,84 | €0,39 | €0,02 |
| Rapida 1H V1 — madre | ADA | SHORT | Momentum / breakout | 60m | 3,0x | 0,16185 | 0,16185 | 0,16367 | 0,21499 | 0,15913 | €1.486,90 | €4.460,70 | €49,96 | €-0,00 |
| Rapida 1H V1 — madre | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00320 | 0,00320 | 0,00286 | 0,00215 | 0,00370 | €158,12 | €474,35 | €49,93 | €0,00 |
| Rapida V1 — score 6–7,5 | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00320 | 0,00320 | 0,00287 | 0,00215 | 0,00369 | €167,22 | €501,65 | €51,54 | €0,00 |
| Rapida V1 — score 6–7,5 | ALLO | SHORT | Momentum / breakout | 60m | 3,0x | 0,33713 | 0,33713 | 0,36471 | 0,44782 | 0,29576 | €212,67 | €638,01 | €52,19 | €-0,00 |
| Rapida V1 — score 6–7,5 | BANK | LONG | Momentum / breakout | 60m | 3,0x | 0,38680 | 0,38315 | 0,35294 | 0,25980 | 0,43759 | €197,79 | €593,37 | €51,94 | €-5,60 |
| Rapida V1 — score 6–7,5 | SHIB | LONG | Momentum / breakout | 60m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €11,70 | €35,09 | €1,52 | €-0,67 |
| Rapida V1 — score 6–7,5 | ETH | LONG | Momentum / breakout | 60m | 3,0x | 1943,95871 | 1959,42000 | 1922,18638 | 1305,69227 | 1976,61722 | €1.472,77 | €4.418,31 | €49,49 | €35,14 |
| Rapida V1 — score 6–7,5 | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 60,04501 | 60,32300 | 59,37250 | 40,33023 | 61,05376 | €8,47 | €25,40 | €0,28 | €0,12 |
| Rapida score 6–7,5 — senza Trend Up | BEAT | LONG | Momentum / breakout | 60m | 3,0x | 3,29017 | 3,29017 | 3,07004 | 2,20990 | 3,62037 | €256,24 | €768,73 | €51,43 | €0,00 |
| Rapida score 6–7,5 — senza Trend Up | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00322 | 0,00322 | 0,00289 | 0,00216 | 0,00372 | €167,84 | €503,53 | €51,67 | €0,00 |
| Rapida score 6–7,5 — senza Trend Up | BANK | LONG | Momentum / breakout | 60m | 3,0x | 0,38680 | 0,38315 | 0,35294 | 0,25980 | 0,43759 | €194,63 | €583,90 | €51,12 | €-5,51 |
| Rapida score 6–7,5 — senza Trend Up | ALLO | SHORT | Momentum / breakout | 60m | 3,0x | 0,33808 | 0,33808 | 0,36389 | 0,44909 | 0,29937 | €218,91 | €656,73 | €50,14 | €-0,00 |
| Rapida score 6–7,5 — Range Only | BEAT | LONG | Momentum / breakout | 60m | 3,0x | 3,29017 | 3,29017 | 3,07004 | 2,20990 | 3,62037 | €256,24 | €768,73 | €51,43 | €0,00 |
| Rapida score 6–7,5 — Range Only | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00322 | 0,00322 | 0,00289 | 0,00216 | 0,00372 | €167,84 | €503,53 | €51,67 | €0,00 |
| Rapida score 6–7,5 — Range Only | ESPORTS | SHORT | Momentum / breakout | 60m | 3,0x | 0,02828 | 0,02804 | 0,03168 | 0,03757 | 0,02319 | €143,01 | €429,04 | €51,48 | €3,71 |
| Rapida score 6–7,5 — Range Only | SHIB | LONG | Momentum / breakout | 60m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €394,57 | €1.183,71 | €51,34 | €-22,74 |
| Rapida score 6–7,5 — Cost Aware | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00322 | 0,00322 | 0,00289 | 0,00216 | 0,00372 | €167,51 | €502,54 | €51,57 | €0,00 |
| Rapida score 6–7,5 — Cost Aware | ALLO | SHORT | Momentum / breakout | 60m | 3,0x | 0,33713 | 0,33713 | 0,36471 | 0,44782 | 0,29576 | €211,20 | €633,59 | €51,83 | €-0,00 |
| Rapida score 6–7,5 — Cost Aware | BANK | LONG | Momentum / breakout | 60m | 3,0x | 0,38680 | 0,38315 | 0,35294 | 0,25980 | 0,43759 | €197,03 | €591,09 | €51,75 | €-5,57 |
| Rapida score 6–7,5 — Cost Aware | SHIB | LONG | Momentum / breakout | 60m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €11,64 | €34,93 | €1,52 | €-0,67 |
| Rapida score 6–7,5 — Cost Aware | ETH | LONG | Momentum / breakout | 60m | 3,0x | 1943,95871 | 1959,42000 | 1922,18638 | 1305,69227 | 1976,61722 | €1.465,09 | €4.395,27 | €49,23 | €34,96 |
| Rapida V1 — no HIGH + score <7,5 | BEAT | LONG | Momentum / breakout | 60m | 3,0x | 3,29017 | 3,29017 | 3,07004 | 2,20990 | 3,62037 | €257,44 | €772,31 | €51,67 | €0,00 |
| Rapida V1 — no HIGH + score <7,5 | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00320 | 0,00320 | 0,00287 | 0,00215 | 0,00369 | €165,85 | €497,54 | €51,12 | €0,00 |
| Rapida V1 — no HIGH + score <7,5 | ALLO | SHORT | Momentum / breakout | 60m | 3,0x | 0,33808 | 0,33808 | 0,36389 | 0,44909 | 0,29937 | €225,73 | €677,19 | €51,70 | €-0,00 |
| Rapida V1 — no HIGH + score <7,5 | PEPE | LONG | Momentum / breakout | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €938,65 | €2.815,95 | €52,29 | €-3,32 |
| Rapida V1 — no HIGH + score <7,5 | ETH | LONG | Momentum / breakout | 60m | 3,0x | 1943,95871 | 1959,42000 | 1922,18638 | 1305,69227 | 1976,61722 | €57,45 | €172,34 | €1,93 | €1,37 |
| Rapida V1 — Long + BTC 1–3 + score <7,5 | SHIB | LONG | Momentum / breakout | 60m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €385,88 | €1.157,65 | €50,21 | €-22,24 |
| Rapida V1 — Long + BTC 1–3 + score <7,5 | XRP | LONG | Momentum / breakout | 60m | 3,0x | 1,11443 | 1,10943 | 1,10195 | 0,74853 | 1,13316 | €70,58 | €211,74 | €2,37 | €-0,95 |
| Rapida V1 — Long + BTC 1–3 + score <7,5 | ETH | LONG | Momentum / breakout | 60m | 3,0x | 1947,14935 | 1959,42000 | 1925,34128 | 1307,83531 | 1979,86146 | €1.491,96 | €4.475,89 | €50,13 | €28,21 |
| Rapida V1 — Long + BTC 1–3 + score <7,5 | BANK | LONG | Momentum / breakout | 60m | 3,0x | 0,38852 | 0,38315 | 0,36054 | 0,26095 | 0,43048 | €231,50 | €694,50 | €50,01 | €-9,60 |
| Rapida V1 — Long + BTC 1–3 + score <7,5 | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 60,04501 | 60,32300 | 59,37250 | 40,33023 | 61,05376 | €1.416,99 | €4.250,97 | €47,61 | €19,68 |
| Rapida V1 — senza PEPE | ADA | SHORT | Momentum / breakout | 60m | 3,0x | 0,16185 | 0,16185 | 0,16367 | 0,21499 | 0,15913 | €1.512,75 | €4.538,24 | €50,83 | €-0,00 |
| Rapida V1 — senza PEPE | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00320 | 0,00320 | 0,00286 | 0,00215 | 0,00370 | €160,87 | €482,60 | €50,80 | €0,00 |
| Rapida V1 — senza PEPE | WLD | SHORT | Momentum / breakout | 60m | 3,0x | 0,34959 | 0,34959 | 0,35668 | 0,46437 | 0,33896 | €838,72 | €2.516,16 | €51,00 | €-0,00 |
| Rapida V1 — senza PEPE | BANK | LONG | Momentum / breakout | 60m | 3,0x | 0,37568 | 0,38315 | 0,34052 | 0,25233 | 0,42842 | €175,27 | €525,81 | €49,21 | €10,46 |
| Rapida V1 — senza PEPE | ETH | LONG | Momentum / breakout | 60m | 3,0x | 1943,95871 | 1959,42000 | 1922,18638 | 1305,69227 | 1976,61722 | €15,56 | €46,69 | €0,52 | €0,37 |
| Rapida V1 — target pieno 2R | ADA | SHORT | Momentum / breakout | 60m | 3,0x | 0,16185 | 0,16185 | 0,16367 | 0,21499 | 0,15823 | €1.482,83 | €4.448,49 | €49,82 | €-0,00 |
| Rapida V1 — target pieno 2R | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00320 | 0,00320 | 0,00286 | 0,00215 | 0,00387 | €157,69 | €473,06 | €49,80 | €0,00 |
| Rapida V1 — target pieno 2R | WLD | SHORT | Momentum / breakout | 60m | 3,0x | 0,34959 | 0,34959 | 0,35668 | 0,46437 | 0,33542 | €42,01 | €126,02 | €2,55 | €-0,00 |
| Rapida V1 — target pieno 2R | BANK | LONG | Momentum / breakout | 60m | 3,0x | 0,37568 | 0,38315 | 0,34052 | 0,25233 | 0,44600 | €177,34 | €532,02 | €49,79 | €10,59 |
| Rapida V1 — target pieno 2R | ALLO | SHORT | Momentum / breakout | 60m | 3,0x | 0,35543 | 0,35543 | 0,38543 | 0,47213 | 0,29543 | €187,33 | €561,99 | €47,43 | €-0,00 |
| Rapida V1 — target pieno 2R | SHIB | LONG | Momentum / breakout | 60m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €10,60 | €31,81 | €1,45 | €-0,55 |
| Rapida 1H V2 | TAO | SHORT | Momentum / breakout V2 | 60m | 3,0x | 188,48684 | 188,48684 | 190,75481 | 250,37335 | 185,08488 | €1.390,02 | €4.170,07 | €50,18 | €-0,00 |
| Rapida 1H V2 | ADA | SHORT | Momentum / breakout V2 | 60m | 3,0x | 0,16185 | 0,16185 | 0,16367 | 0,21499 | 0,15913 | €1.494,54 | €4.483,63 | €50,22 | €-0,00 |
| Rapida 1H V2 | XRP | LONG | Momentum / breakout V2 | 60m | 3,0x | 1,11443 | 1,10943 | 1,10195 | 0,74853 | 1,13316 | €1.498,43 | €4.495,30 | €50,35 | €-20,18 |
| Rapida 1H V3 Filtered — madre | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16185 | 0,16185 | 0,16367 | 0,21499 | 0,15913 | €1.521,20 | €4.563,60 | €51,11 | €-0,00 |
| Rapida 1H V3 Filtered — madre | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00320 | 0,00320 | 0,00286 | 0,00215 | 0,00370 | €161,77 | €485,30 | €51,08 | €0,00 |
| Rapida 1H V3 Filtered — madre | WLD | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,34959 | 0,34959 | 0,35668 | 0,46437 | 0,33896 | €843,41 | €2.530,22 | €51,28 | €-0,00 |
| Rapida 1H V3 Filtered — madre | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,37568 | 0,38315 | 0,34052 | 0,25233 | 0,42842 | €176,34 | €529,01 | €49,51 | €10,53 |
| Rapida 1H V3 Filtered — madre | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1943,95871 | 1959,42000 | 1922,18638 | 1305,69227 | 1976,61722 | €15,97 | €47,91 | €0,54 | €0,38 |
| Rapida V3 — score <7,5 | BEAT | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 3,29017 | 3,29017 | 3,07004 | 2,20990 | 3,62037 | €258,77 | €776,32 | €51,94 | €0,00 |
| Rapida V3 — score <7,5 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00320 | 0,00320 | 0,00287 | 0,00215 | 0,00369 | €166,71 | €500,13 | €51,38 | €0,00 |
| Rapida V3 — score <7,5 | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,38680 | 0,38315 | 0,35294 | 0,25980 | 0,43759 | €197,36 | €592,09 | €51,83 | €-5,58 |
| Rapida V3 — score <7,5 | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,33808 | 0,33808 | 0,36389 | 0,44909 | 0,29937 | €227,32 | €681,96 | €52,06 | €-0,00 |
| Rapida V3 — score <7,5 | SHIB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €10,86 | €32,57 | €1,41 | €-0,63 |
| Rapida V3 — no volatilità HIGH | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16185 | 0,16185 | 0,16367 | 0,21499 | 0,15913 | €1.485,86 | €4.457,58 | €49,92 | €-0,00 |
| Rapida V3 — no volatilità HIGH | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00320 | 0,00320 | 0,00286 | 0,00215 | 0,00370 | €158,01 | €474,02 | €49,90 | €0,00 |
| Rapida V3 — no volatilità HIGH | WLD | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,34959 | 0,34959 | 0,35668 | 0,46437 | 0,33896 | €823,75 | €2.471,25 | €50,08 | €-0,00 |
| Rapida V3 — no volatilità HIGH | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,37568 | 0,38315 | 0,34052 | 0,25233 | 0,42842 | €172,41 | €517,23 | €48,41 | €10,29 |
| Rapida V3 — no volatilità HIGH | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1943,95871 | 1959,42000 | 1922,18638 | 1305,69227 | 1976,61722 | €15,61 | €46,83 | €0,52 | €0,37 |
| Rapida V3 — Long Only | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00320 | 0,00320 | 0,00286 | 0,00215 | 0,00370 | €155,06 | €465,19 | €48,97 | €0,00 |
| Rapida V3 — Long Only | BEAT | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 3,29017 | 3,29017 | 3,07004 | 2,20990 | 3,62037 | €243,96 | €731,87 | €48,97 | €0,00 |
| Rapida V3 — Long Only | SHIB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €375,62 | €1.126,85 | €48,88 | €-21,65 |
| Rapida V3 — Long Only | PEPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €880,10 | €2.640,29 | €49,03 | €-3,11 |
| Rapida V3 — Long + no HIGH + score <7,5 | BEAT | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 3,29017 | 3,29017 | 3,07004 | 2,20990 | 3,62037 | €246,62 | €739,85 | €49,50 | €0,00 |
| Rapida V3 — Long + no HIGH + score <7,5 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00322 | 0,00322 | 0,00289 | 0,00216 | 0,00372 | €160,75 | €482,24 | €49,49 | €0,00 |
| Rapida V3 — Long + no HIGH + score <7,5 | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,38680 | 0,38315 | 0,35294 | 0,25980 | 0,43759 | €190,39 | €571,16 | €50,00 | €-5,39 |
| Rapida V3 — Long + no HIGH + score <7,5 | SHIB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €385,28 | €1.155,84 | €50,13 | €-22,20 |
| Rapida V3 — Long + no HIGH + score <7,5 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1943,95871 | 1959,42000 | 1922,18638 | 1305,69227 | 1976,61722 | €23,15 | €69,46 | €0,78 | €0,55 |
| Rapida V3 — senza ESPORTS | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16185 | 0,16185 | 0,16367 | 0,21499 | 0,15913 | €1.489,89 | €4.469,66 | €50,06 | €-0,00 |
| Rapida V3 — senza ESPORTS | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00320 | 0,00320 | 0,00286 | 0,00215 | 0,00370 | €158,44 | €475,31 | €50,03 | €0,00 |
| Rapida V3 — senza ESPORTS | WLD | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,34959 | 0,34959 | 0,35668 | 0,46437 | 0,33896 | €825,98 | €2.477,95 | €50,22 | €-0,00 |
| Rapida V3 — senza ESPORTS | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,37568 | 0,38315 | 0,34052 | 0,25233 | 0,42842 | €172,88 | €518,63 | €48,54 | €10,32 |
| Rapida V3 — senza ESPORTS | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1943,95871 | 1959,42000 | 1922,18638 | 1305,69227 | 1976,61722 | €15,65 | €46,96 | €0,53 | €0,37 |
| Rapida V3 senza ESPORTS — Long Only | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00320 | 0,00320 | 0,00286 | 0,00215 | 0,00370 | €158,13 | €474,39 | €49,94 | €0,00 |
| Rapida V3 senza ESPORTS — Long Only | BEAT | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 3,29017 | 3,29017 | 3,07004 | 2,20990 | 3,62037 | €248,78 | €746,34 | €49,93 | €0,00 |
| Rapida V3 senza ESPORTS — Long Only | SHIB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €20,15 | €60,45 | €2,62 | €-1,16 |
| Rapida V3 senza ESPORTS — Long Only | PEPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €909,76 | €2.729,29 | €50,68 | €-3,22 |
| Rapida V3 senza ESPORTS — Long Only | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1943,95871 | 1959,42000 | 1922,18638 | 1305,69227 | 1976,61722 | €1.460,27 | €4.380,80 | €49,06 | €34,84 |
| Rapida V3 senza ESPORTS — Long Only | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 60,04501 | 60,32300 | 59,37250 | 40,33023 | 61,05376 | €14,96 | €44,89 | €0,50 | €0,21 |
| Rapida V3 senza ESPORTS — MFE Lock | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16185 | 0,16185 | 0,16367 | 0,21499 | 0,15913 | €1.510,84 | €4.532,53 | €50,76 | €-0,00 |
| Rapida V3 senza ESPORTS — MFE Lock | WLD | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,34959 | 0,34959 | 0,35668 | 0,46437 | 0,33896 | €11,86 | €35,57 | €0,72 | €-0,00 |
| Rapida V3 senza ESPORTS — MFE Lock | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,33165 | 0,33165 | 0,36472 | 0,44055 | 0,28205 | €170,96 | €512,89 | €51,14 | €-0,00 |
| Rapida V3 senza ESPORTS — MFE Lock | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00317 | 0,00317 | 0,00290 | 0,00213 | 0,00358 | €199,03 | €597,09 | €50,62 | €0,00 |
| Rapida V3 senza ESPORTS — MFE Lock | PEPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €867,02 | €2.601,07 | €48,30 | €-3,07 |
| Rapida V3 senza ESPORTS — MFE Lock | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1943,95871 | 1959,42000 | 1922,18638 | 1305,69227 | 1976,61722 | €74,16 | €222,48 | €2,49 | €1,77 |
| Rapida V3 senza ESPORTS — Stress Guard | XRP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,11443 | 1,10943 | 1,10195 | 0,74853 | 1,13316 | €1.512,48 | €4.537,44 | €50,82 | €-20,37 |
| Rapida V3 senza ESPORTS — Stress Guard | PEPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €873,54 | €2.620,61 | €50,01 | €-11,54 |
| Rapida V3 senza ESPORTS — Stress Guard | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1943,95871 | 1959,42000 | 1922,18638 | 1305,69227 | 1976,61722 | €1.485,05 | €4.455,15 | €49,90 | €35,43 |
| Rapida V3 — qualità completa + profit lock | BEAT | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 3,29017 | 3,29017 | 3,07004 | 2,20990 | 3,62037 | €245,16 | €735,47 | €49,21 | €0,00 |
| Rapida V3 — qualità completa + profit lock | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00322 | 0,00322 | 0,00289 | 0,00216 | 0,00372 | €159,93 | €479,80 | €49,24 | €0,00 |
| Rapida V3 — qualità completa + profit lock | SHIB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €15,43 | €46,28 | €2,01 | €-0,89 |
| Rapida V3 — qualità completa + profit lock | PEPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €875,11 | €2.625,32 | €48,75 | €-3,09 |
| Rapida V3 — qualità completa + profit lock | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1943,95871 | 1959,42000 | 1922,18638 | 1305,69227 | 1976,61722 | €1.459,48 | €4.378,44 | €49,04 | €34,82 |
| Rapida V3 — qualità completa + profit lock | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 60,04501 | 60,32300 | 59,37250 | 40,33023 | 61,05376 | €14,94 | €44,83 | €0,50 | €0,21 |
| Ampia 4H | HYPE | SHORT | Confluenza trend | 240m | 2,0x | 58,36732 | 60,32300 | 61,80927 | 87,25915 | 48,72988 | €424,03 | €848,06 | €50,01 | €-28,42 |
| Ampia 4H | TAO | SHORT | Confluenza trend | 240m | 2,0x | 189,05650 | 189,05650 | 197,51338 | 282,63946 | 165,37722 | €558,68 | €1.117,36 | €49,98 | €-0,00 |
| Ampia 4H | AKE | LONG | Confluenza trend | 240m | 2,0x | 0,00328 | 0,00328 | 0,00288 | 0,00165 | 0,00438 | €207,40 | €414,80 | €49,78 | €0,00 |
| Ampia 4H | XMR | LONG | Confluenza trend | 240m | 2,0x | 364,45854 | 364,45854 | 347,94701 | 184,05156 | 410,69083 | €544,42 | €1.088,84 | €49,33 | €0,00 |
| Forza relativa 1H V1 | NIGHT | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,02031 | 0,02031 | 0,02210 | 0,03036 | 0,01637 | €285,91 | €571,83 | €50,45 | €-0,00 |
| Forza relativa 1H V1 | ONDO | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,42171 | €891,90 | €1.783,80 | €49,29 | €0,00 |
| Forza relativa 1H V1 | WLD | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,32287 | €14,97 | €29,93 | €0,82 | €-0,00 |
| Forza relativa 1H V1 | AKE | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,00327 | 0,00327 | 0,00287 | 0,00165 | 0,00413 | €208,36 | €416,72 | €50,01 | €0,00 |
| Forza relativa 1H V1 | ETH | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 1943,95871 | 1959,42000 | 1915,96571 | 981,69915 | 2005,54333 | €1.433,90 | €2.867,80 | €41,30 | €22,81 |
| Forza relativa 1H V2 | AKE | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,00320 | 0,00320 | 0,00282 | 0,00162 | 0,00405 | €216,28 | €432,55 | €51,91 | €0,00 |
| Forza relativa 1H V2 | WLD | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,32287 | €47,70 | €95,39 | €2,60 | €-0,00 |
| Forza relativa 1H V2 | XMR | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 367,08012 | 367,08012 | 360,46822 | 185,37546 | 381,62629 | €1.446,12 | €2.892,24 | €52,10 | €0,00 |
| Forza relativa 1H V2 | BANK | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,36855 | 0,38315 | 0,33045 | 0,18612 | 0,45238 | €219,06 | €438,12 | €45,30 | €17,35 |
| Forza relativa 1H V2 | PEPE | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €846,05 | €1.692,10 | €47,31 | €2,70 |
| Benchmark Donchian breakout 1H | SUI | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,76606 | 0,76606 | 0,75182 | 0,38686 | 0,80165 | €1.377,00 | €2.754,00 | €51,18 | €0,00 |
| Benchmark Donchian breakout 1H | ALLO | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,35678 | 0,35678 | 0,39959 | 0,53338 | 0,24974 | €215,19 | €430,38 | €51,65 | €-0,00 |
| Benchmark Donchian breakout 1H | HYPE | LONG | Donchian breakout 20 barre | 60m | 2,0x | 58,92678 | 60,32300 | 59,75087 | 29,75803 | 61,28385 | €1.635,95 | €3.271,90 | €0,00 | €77,52 |
| Benchmark Donchian breakout 1H | BANK | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,39689 | 0,38315 | 0,35670 | 0,20043 | 0,49737 | €258,64 | €517,28 | €52,39 | €-17,91 |
| Benchmark Donchian breakout 1H | ETH | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1958,25157 | 1959,42000 | 1926,91955 | 988,91704 | 2036,58163 | €70,73 | €141,45 | €2,26 | €0,08 |
| Benchmark Bollinger mean reversion 1H | HYPE | SHORT | Bollinger mean reversion | 60m | 2,0x | 59,61921 | 60,32300 | 60,33464 | 89,13071 | 58,54606 | €1.987,62 | €3.975,25 | €47,70 | €-46,93 |
| Benchmark Bollinger mean reversion 1H | XRP | SHORT | Bollinger mean reversion | 60m | 2,0x | 1,11399 | 1,10943 | 1,12736 | 1,66541 | 1,09394 | €1.986,03 | €3.972,07 | €47,66 | €16,25 |
| Benchmark trend following EMA 1H | LAB | LONG | Trend following EMA | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €207,05 | €414,10 | €49,69 | €0,00 |
| Benchmark trend following EMA 1H | ALLO | SHORT | Trend following EMA | 60m | 2,0x | 0,35372 | 0,35372 | 0,39616 | 0,52881 | 0,26034 | €209,15 | €418,30 | €50,20 | €-0,00 |
| Benchmark trend following EMA 1H | XMR | LONG | Trend following EMA | 60m | 2,0x | 367,08012 | 367,08012 | 359,73357 | 185,37546 | 383,24253 | €17,91 | €35,83 | €0,72 | €0,00 |
| Benchmark trend following EMA 1H | BANK | LONG | Trend following EMA | 60m | 2,0x | 0,37568 | 0,38315 | 0,33059 | 0,18972 | 0,47485 | €205,19 | €410,38 | €49,25 | €8,17 |
| Benchmark trend following EMA 1H | SHIB | LONG | Trend following EMA | 60m | 2,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €389,51 | €779,03 | €49,98 | €-40,49 |
| Scanner Top 5 Long 1H | LAB | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €219,03 | €438,05 | €52,57 | €0,00 |
| Scanner Top 5 Long 1H | AKE | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,00319 | 0,00319 | 0,00281 | 0,00161 | 0,00396 | €224,41 | €448,82 | €53,86 | €0,00 |
| Scanner Top 5 Long 1H | XMR | LONG | Scanner Top 5 Long | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10712 | €70,71 | €141,42 | €2,58 | €0,00 |
| Scanner Top 5 Long 1H | PEPE | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.011,45 | €2.022,90 | €49,63 | €-15,73 |
| Scanner Top 5 Long 1H | ETH | LONG | Scanner Top 5 Long | 60m | 2,0x | 1943,95871 | 1959,42000 | 1915,96571 | 981,69915 | 1999,94472 | €1.778,37 | €3.556,74 | €51,22 | €28,29 |
| Scanner Top 5 Long 1H | HYPE | LONG | Scanner Top 5 Long | 60m | 2,0x | 60,04501 | 60,32300 | 59,18036 | 30,32273 | 61,77430 | €14,18 | €28,35 | €0,41 | €0,13 |
| Scanner Bottom 5 Short 1H | ADA | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,16703 | 0,16703 | 0,16365 | 0,24971 | 0,16112 | €1.381,07 | €2.762,13 | €0,00 | €-0,00 |
| Scanner Bottom 5 Short 1H | ALLO | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,36179 | 0,36179 | 0,40521 | 0,54088 | 0,27496 | €202,53 | €405,06 | €48,61 | €-0,00 |
| Scanner Bottom 5 Short 1H | ESPORTS | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,03342 | 0,02804 | 0,03342 | 0,04997 | 0,02540 | €202,66 | €405,32 | €0,00 | €65,28 |
| Scanner Top10 Long | AKE | LONG | Scanner Top10 Long | 60m | 2,0x | 0,00319 | 0,00319 | 0,00281 | 0,00161 | 0,00396 | €208,33 | €416,67 | €50,00 | €0,00 |
| Scanner Top10 Long | XMR | LONG | Scanner Top10 Long | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10712 | €1.371,36 | €2.742,71 | €50,02 | €0,00 |
| Scanner Top10 Long | BANK | LONG | Scanner Top10 Long | 60m | 2,0x | 0,37568 | 0,38315 | 0,33059 | 0,18972 | 0,46584 | €203,89 | €407,78 | €48,93 | €8,11 |
| Scanner Top10 Long | SHIB | LONG | Scanner Top10 Long | 60m | 2,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €24,14 | €48,29 | €2,71 | €-0,58 |
| Scanner Top10 Long | PEPE | LONG | Scanner Top10 Long | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €924,43 | €1.848,86 | €45,36 | €-14,38 |
| Scanner Bottom10 Short | ADA | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,16193 | 0,16193 | 0,16426 | 0,24209 | 0,15727 | €1.731,26 | €3.462,51 | €49,86 | €-0,00 |
| Scanner Bottom10 Short | ALLO | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,35250 | 0,35250 | 0,39075 | 0,52699 | 0,27600 | €224,69 | €449,38 | €48,76 | €-0,00 |
| Scanner Bottom10 Short | ESPORTS | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,03342 | 0,02804 | 0,03342 | 0,04997 | 0,02540 | €203,44 | €406,87 | €0,00 | €65,53 |
| Scanner Top15 Long | AKE | LONG | Scanner Top15 Long | 60m | 2,0x | 0,00319 | 0,00319 | 0,00281 | 0,00161 | 0,00396 | €208,33 | €416,67 | €50,00 | €0,00 |
| Scanner Top15 Long | XMR | LONG | Scanner Top15 Long | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10712 | €1.371,36 | €2.742,71 | €50,02 | €0,00 |
| Scanner Top15 Long | BANK | LONG | Scanner Top15 Long | 60m | 2,0x | 0,37568 | 0,38315 | 0,33059 | 0,18972 | 0,46584 | €203,89 | €407,78 | €48,93 | €8,11 |
| Scanner Top15 Long | SHIB | LONG | Scanner Top15 Long | 60m | 2,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €24,14 | €48,29 | €2,71 | €-0,58 |
| Scanner Top15 Long | PEPE | LONG | Scanner Top15 Long | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €924,43 | €1.848,86 | €45,36 | €-14,38 |
| Scanner Bottom15 Short | ADA | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,16193 | 0,16193 | 0,16426 | 0,24209 | 0,15727 | €1.731,26 | €3.462,51 | €49,86 | €-0,00 |
| Scanner Bottom15 Short | ALLO | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,35250 | 0,35250 | 0,39075 | 0,52699 | 0,27600 | €224,69 | €449,38 | €48,76 | €-0,00 |
| Scanner Bottom15 Short | ESPORTS | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,03342 | 0,02804 | 0,03342 | 0,04997 | 0,02540 | €203,44 | €406,87 | €0,00 | €65,53 |
| Scanner Top20 Long | AKE | LONG | Scanner Top20 Long | 60m | 2,0x | 0,00319 | 0,00319 | 0,00281 | 0,00161 | 0,00396 | €208,33 | €416,67 | €50,00 | €0,00 |
| Scanner Top20 Long | XMR | LONG | Scanner Top20 Long | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10712 | €1.371,36 | €2.742,71 | €50,02 | €0,00 |
| Scanner Top20 Long | BANK | LONG | Scanner Top20 Long | 60m | 2,0x | 0,37568 | 0,38315 | 0,33059 | 0,18972 | 0,46584 | €203,89 | €407,78 | €48,93 | €8,11 |
| Scanner Top20 Long | SHIB | LONG | Scanner Top20 Long | 60m | 2,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €24,14 | €48,29 | €2,71 | €-0,58 |
| Scanner Top20 Long | PEPE | LONG | Scanner Top20 Long | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €924,43 | €1.848,86 | €45,36 | €-14,38 |
| Scanner Bottom20 Short | ADA | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,16193 | 0,16193 | 0,16426 | 0,24209 | 0,15727 | €1.731,26 | €3.462,51 | €49,86 | €-0,00 |
| Scanner Bottom20 Short | ALLO | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,35250 | 0,35250 | 0,39075 | 0,52699 | 0,27600 | €224,69 | €449,38 | €48,76 | €-0,00 |
| Scanner Bottom20 Short | ESPORTS | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,03342 | 0,02804 | 0,03342 | 0,04997 | 0,02540 | €203,44 | €406,87 | €0,00 | €65,53 |
| Scanner Top 5 + forza BTC 1H | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39694 | 0,39694 | 0,38539 | 0,20045 | 0,42235 | €898,57 | €1.797,15 | €52,29 | €0,00 |
| Scanner Top 5 + forza BTC 1H | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €216,56 | €433,12 | €51,97 | €0,00 |
| Scanner Top 5 + forza BTC 1H | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00319 | 0,00319 | 0,00281 | 0,00161 | 0,00403 | €219,41 | €438,82 | €52,66 | €0,00 |
| Scanner Top 5 + forza BTC 1H | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 381,44484 | €37,16 | €74,32 | €1,36 | €0,00 |
| Scanner Top 5 + forza BTC 1H | ETH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1943,95871 | 1959,42000 | 1915,96571 | 981,69915 | 2005,54333 | €1.658,75 | €3.317,49 | €47,77 | €26,39 |
| Scanner Top 5 + forza BTC 1H | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 60,04501 | 60,32300 | 59,18036 | 30,32273 | 61,94723 | €12,65 | €25,30 | €0,36 | €0,12 |
| Top 5 + BTC — solo MFE | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39924 | 0,39924 | 0,38729 | 0,20162 | 0,42552 | €835,46 | €1.670,91 | €50,00 | €0,00 |
| Top 5 + BTC — solo MFE | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 367,08012 | 367,08012 | 360,46822 | 185,37546 | 381,62629 | €1.363,71 | €2.727,43 | €49,13 | €0,00 |
| Top 5 + BTC — solo MFE | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00322 | 0,00322 | 0,00284 | 0,00163 | 0,00407 | €196,51 | €393,01 | €47,16 | €0,00 |
| Top 5 + BTC — solo MFE | ETH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1947,14935 | 1959,42000 | 1919,11040 | 983,31042 | 2008,83504 | €1.634,22 | €3.268,43 | €47,07 | €20,60 |
| Top 5 + BTC — solo MFE | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 60,04501 | 60,32300 | 59,18036 | 30,32273 | 61,94723 | €36,62 | €73,24 | €1,05 | €0,34 |
| Top 5 + BTC — Guard | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39724 | 0,39724 | 0,38434 | 0,20061 | 0,42561 | €756,62 | €1.513,24 | €49,13 | €0,00 |
| Top 5 + BTC — Guard | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €202,47 | €404,95 | €48,59 | €0,00 |
| Top 5 + BTC — Guard | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00319 | 0,00319 | 0,00281 | 0,00161 | 0,00403 | €207,86 | €415,72 | €49,89 | €0,00 |
| Top 5 + BTC — Guard | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,38202 | 0,38315 | 0,34542 | 0,19292 | 0,46253 | €247,49 | €494,98 | €47,42 | €1,47 |
| Top 5 + BTC — BTC≤3 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39974 | 0,39974 | 0,38840 | 0,20187 | 0,42468 | €884,65 | €1.769,29 | €50,18 | €0,00 |
| Top 5 + BTC — BTC≤3 | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €207,87 | €415,74 | €49,89 | €0,00 |
| Top 5 + BTC — BTC≤3 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00319 | 0,00319 | 0,00281 | 0,00161 | 0,00403 | €210,72 | €421,44 | €50,57 | €0,00 |
| Top 5 + BTC — BTC≤3 | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 381,44484 | €37,63 | €75,26 | €1,37 | €0,00 |
| Top 5 + BTC — BTC≤3 | ETH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1943,95871 | 1959,42000 | 1915,96571 | 981,69915 | 2005,54333 | €1.593,18 | €3.186,36 | €45,88 | €25,34 |
| Top 5 + BTC — BTC 2–3 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39974 | 0,39974 | 0,38840 | 0,20187 | 0,42468 | €884,65 | €1.769,29 | €50,18 | €0,00 |
| Top 5 + BTC — BTC 2–3 | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €207,87 | €415,74 | €49,89 | €0,00 |
| Top 5 + BTC — BTC 2–3 | SHIB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €510,10 | €1.020,20 | €49,66 | €-41,03 |
| Top 5 + BTC — BTC 2–3 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €996,29 | €1.992,58 | €48,89 | €-8,78 |
| Top 5 + BTC — Guard + MFE | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39724 | 0,39724 | 0,38434 | 0,20061 | 0,42561 | €756,62 | €1.513,24 | €49,13 | €0,00 |
| Top 5 + BTC — Guard + MFE | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00322 | 0,00322 | 0,00284 | 0,00163 | 0,00407 | €201,88 | €403,77 | €48,45 | €0,00 |
| Top 5 + BTC — Guard + MFE | SHIB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €407,51 | €815,02 | €45,45 | €-15,66 |
| Top 5 + BTC — Guard + MFE | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.000,26 | €2.000,52 | €47,76 | €-2,36 |
| Top 5 + BTC — Guard + BTC≤3 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39974 | 0,39974 | 0,38840 | 0,20187 | 0,42468 | €871,05 | €1.742,11 | €49,41 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €205,84 | €411,68 | €49,40 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00319 | 0,00319 | 0,00281 | 0,00161 | 0,00403 | €211,32 | €422,63 | €50,72 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,37568 | 0,38315 | 0,33059 | 0,18972 | 0,47485 | €14,78 | €29,56 | €3,55 | €0,59 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39974 | 0,39974 | 0,38840 | 0,20187 | 0,42468 | €871,05 | €1.742,11 | €49,41 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00322 | 0,00322 | 0,00284 | 0,00163 | 0,00407 | €204,20 | €408,41 | €49,01 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | SHIB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €414,63 | €829,26 | €46,24 | €-15,93 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.011,73 | €2.023,45 | €48,31 | €-2,38 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39694 | 0,39694 | 0,38539 | 0,20045 | 0,43159 | €861,83 | €1.723,66 | €50,15 | €0,00 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,21338 | €207,96 | €415,92 | €49,91 | €0,00 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00319 | 0,00319 | 0,00281 | 0,00161 | 0,00434 | €213,22 | €426,44 | €51,17 | €0,00 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 386,79573 | €70,70 | €141,40 | €2,58 | €0,00 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | ETH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1943,95871 | 1959,42000 | 1915,96571 | 981,69915 | 2027,93773 | €1.617,79 | €3.235,59 | €46,59 | €25,73 |
| Top 5 + BTC — target pieno 3R | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39694 | 0,39694 | 0,38539 | 0,20045 | 0,43159 | €861,83 | €1.723,66 | €50,15 | €0,00 |
| Top 5 + BTC — target pieno 3R | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,21338 | €207,96 | €415,92 | €49,91 | €0,00 |
| Top 5 + BTC — target pieno 3R | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00319 | 0,00319 | 0,00281 | 0,00161 | 0,00434 | €213,56 | €427,11 | €51,25 | €0,00 |
| Top 5 + BTC — target pieno 3R | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 386,79573 | €85,15 | €170,29 | €3,11 | €0,00 |
| Top 5 + BTC — target pieno 3R | ETH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1943,95871 | 1959,42000 | 1915,96571 | 981,69915 | 2027,93773 | €1.579,98 | €3.159,95 | €45,50 | €25,13 |
| Combo Trend | AKE | LONG | Combo Trend | 60m | 2,0x | 0,00329 | 0,00329 | 0,00290 | 0,00166 | 0,00416 | €208,78 | €417,57 | €50,11 | €0,00 |
| Combo Trend | ALLO | SHORT | Combo Trend | 60m | 2,0x | 0,35372 | 0,35372 | 0,39616 | 0,52881 | 0,26034 | €209,35 | €418,70 | €50,24 | €-0,00 |
| Combo Trend | PEPE | LONG | Combo Trend | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €784,30 | €1.568,61 | €47,99 | €-4,59 |
| Combo Trend | SHIB | LONG | Combo Trend | 60m | 2,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €338,96 | €677,92 | €43,49 | €-35,24 |
| Combo Mean Reversion | AKE | SHORT | Combo Mean Reversion | 60m | 2,0x | 0,00320 | 0,00320 | 0,00356 | 0,00479 | 0,00263 | €225,46 | €450,91 | €50,00 | €-0,00 |
| Combo Scanner | ONDO | LONG | Combo Scanner | 60m | 2,0x | 0,39694 | 0,39694 | 0,38539 | 0,20045 | 0,42235 | €857,88 | €1.715,77 | €49,92 | €0,00 |
| Combo Scanner | LAB | LONG | Combo Scanner | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €207,54 | €415,08 | €49,81 | €0,00 |
| Combo Scanner | AKE | LONG | Combo Scanner | 60m | 2,0x | 0,00319 | 0,00319 | 0,00281 | 0,00161 | 0,00403 | €210,36 | €420,73 | €50,49 | €0,00 |
| Combo Scanner | XMR | LONG | Combo Scanner | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 381,44484 | €23,89 | €47,78 | €0,87 | €0,00 |
| Combo Scanner | ETH | LONG | Combo Scanner | 60m | 2,0x | 1943,95871 | 1959,42000 | 1915,96571 | 981,69915 | 2005,54333 | €1.616,34 | €3.232,67 | €46,55 | €25,71 |
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
| Combo Adaptive — Quality7 | SHIB | LONG | Combo Adaptive | 60m | 2,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €12,84 | €25,69 | €1,30 | €-0,96 |
| Combo Adaptive — Trend/Transition | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39724 | 0,39724 | 0,38434 | 0,20061 | 0,42303 | €757,94 | €1.515,88 | €49,21 | €0,00 |
| Combo Adaptive — Trend/Transition | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15861 | 0,13958 | 0,08010 | 0,19668 | €206,52 | €413,04 | €49,56 | €0,00 |
| Combo Adaptive — Trend/Transition | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.044,39 | €2.088,78 | €49,87 | €-2,46 |
| Combo Adaptive — Trend/Transition | ETH | LONG | Combo Adaptive | 60m | 2,0x | 1947,28938 | 1959,42000 | 1919,24841 | 983,38114 | 2003,37131 | €32,32 | €64,64 | €0,93 | €0,40 |
| Combo Adaptive — Trend/Transition | BANK | LONG | Combo Adaptive | 60m | 2,0x | 0,38202 | 0,38315 | 0,34542 | 0,19292 | 0,45521 | €253,56 | €507,13 | €48,58 | €1,50 |
| Combo Adaptive — Quality7 + Regime | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,40554 | 0,40554 | 0,39390 | 0,20480 | 0,42882 | €864,27 | €1.728,54 | €49,61 | €0,00 |
| Combo Adaptive — Quality7 + Regime | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.031,87 | €2.063,74 | €49,27 | €-2,43 |
| Combo Adaptive — Quality7 + Regime | BANK | LONG | Combo Adaptive | 60m | 2,0x | 0,38202 | 0,38315 | 0,34542 | 0,19292 | 0,45521 | €255,46 | €510,92 | €48,94 | €1,52 |
| Combo Adaptive — Long Only | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,41951 | €893,67 | €1.787,34 | €49,39 | €0,00 |
| Combo Adaptive — Long Only | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €205,55 | €411,10 | €49,33 | €0,00 |
| Combo Adaptive — Long Only | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,00319 | 0,00319 | 0,00281 | 0,00161 | 0,00396 | €205,22 | €410,44 | €49,25 | €0,00 |
| Combo Adaptive — Long Only | XMR | LONG | Combo Adaptive | 60m | 2,0x | 367,08012 | 367,08012 | 360,46822 | 185,37546 | 380,30391 | €1.384,19 | €2.768,37 | €49,86 | €0,00 |
| Combo Adaptive — Long Only | SHIB | LONG | Combo Adaptive | 60m | 2,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €12,85 | €25,69 | €1,44 | €-0,31 |
| Combo Adaptive — parziale 1R | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,41951 | €893,02 | €1.786,04 | €49,36 | €0,00 |
| Combo Adaptive — parziale 1R | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €205,22 | €410,44 | €49,25 | €0,00 |
| Combo Adaptive — parziale 1R | WLD | SHORT | Combo Adaptive | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,32475 | €895,30 | €1.790,60 | €48,86 | €-0,00 |
| Combo Adaptive — parziale 1R | ALLO | SHORT | Combo Adaptive | 60m | 2,0x | 0,36179 | 0,36179 | 0,40521 | 0,54088 | 0,27496 | €98,69 | €197,38 | €23,69 | €-0,00 |
| Combo Adaptive — parziale 1R | ETH | LONG | Combo Adaptive | 60m | 2,0x | 1949,77988 | 1959,42000 | 1921,70305 | 984,63884 | 2005,93354 | €13,89 | €27,78 | €0,40 | €0,14 |
| Combo Adaptive — parziale 1R | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €454,44 | €908,89 | €22,09 | €5,25 |
| Combo Adaptive — Quality7 + Regime + parziale 1R | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,40554 | 0,40554 | 0,39390 | 0,20480 | 0,42882 | €864,27 | €1.728,54 | €49,61 | €0,00 |
| Combo Adaptive — Quality7 + Regime + parziale 1R | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.038,23 | €2.076,45 | €49,58 | €-2,45 |
| Combo Adaptive — Quality7 + Regime + parziale 1R | BANK | LONG | Combo Adaptive | 60m | 2,0x | 0,38202 | 0,38315 | 0,34542 | 0,19292 | 0,45521 | €257,03 | €514,07 | €49,25 | €1,53 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,43050 | €902,18 | €1.804,37 | €49,86 | €0,00 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | WLD | SHORT | Combo Adaptive | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,31537 | €919,67 | €1.839,35 | €50,19 | €-0,00 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,00327 | 0,00327 | 0,00287 | 0,00165 | 0,00444 | €209,99 | €419,98 | €50,40 | €0,00 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | XMR | LONG | Combo Adaptive | 60m | 2,0x | 367,08012 | 367,08012 | 360,46822 | 185,37546 | 386,91580 | €27,35 | €54,70 | €0,99 | €0,00 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | ALLO | SHORT | Combo Adaptive | 60m | 2,0x | 0,36179 | 0,36179 | 0,40521 | 0,54088 | 0,23155 | €207,78 | €415,57 | €49,87 | €-0,00 |
| Combo Adaptive — target pieno 3R | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,43050 | €902,18 | €1.804,37 | €49,86 | €0,00 |
| Combo Adaptive — target pieno 3R | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15861 | 0,13958 | 0,08010 | 0,21571 | €207,43 | €414,86 | €49,78 | €0,00 |
| Combo Adaptive — target pieno 3R | WLD | SHORT | Combo Adaptive | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,31537 | €911,80 | €1.823,59 | €49,76 | €-0,00 |
| Combo Adaptive — target pieno 3R | ALLO | SHORT | Combo Adaptive | 60m | 2,0x | 0,36179 | 0,36179 | 0,40521 | 0,54088 | 0,23155 | €205,00 | €410,00 | €49,20 | €-0,00 |
| Sol Ema 4H | SOL | SHORT | Trend following EMA | 240m | 2,0x | 75,05699 | 76,54000 | 77,22103 | 112,21019 | 69,64688 | €862,58 | €1.725,17 | €49,74 | €-34,09 |
| Sol Donchian 4H | SOL | SHORT | Donchian breakout 20 barre | 240m | 2,0x | 75,96380 | 76,54000 | 78,23939 | 113,56589 | 69,59218 | €830,21 | €1.660,43 | €49,74 | €-12,59 |
| Sol Adaptive 4H | SOL | SHORT | Combo Adaptive | 240m | 2,0x | 75,96380 | 76,54000 | 78,44626 | 113,56589 | 69,75767 | €761,04 | €1.522,08 | €49,74 | €-11,55 |
| Eth Ema 1H | ETH | LONG | Trend following EMA | 60m | 3,0x | 1958,25157 | 1959,42000 | 1930,05275 | 1315,29231 | 2014,64922 | €1.132,15 | €3.396,44 | €48,91 | €2,03 |
| Eth Ema 4H | ETH | LONG | Trend following EMA | 240m | 2,0x | 1949,77988 | 1959,42000 | 1902,99144 | 984,63884 | 2066,75096 | €1.036,30 | €2.072,59 | €49,74 | €10,25 |
| Eth Donchian 1H | ETH | LONG | Donchian breakout 20 barre | 60m | 3,0x | 1958,25157 | 1959,42000 | 1933,18595 | 1315,29231 | 2008,38281 | €1.292,62 | €3.877,86 | €49,64 | €2,31 |
| Eth Bollinger 1H | ETH | SHORT | Bollinger mean reversion | 60m | 3,0x | 1957,46843 | 1959,42000 | 1980,95805 | 2600,17056 | 1922,23400 | €1.391,03 | €4.173,10 | €50,08 | €-4,16 |
| Eth Adaptive 1H | ETH | LONG | Combo Adaptive | 60m | 3,0x | 1958,25157 | 1959,42000 | 1930,05275 | 1315,29231 | 2014,64922 | €1.140,50 | €3.421,49 | €49,27 | €2,04 |
| Master Adaptive V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39854 | 0,39854 | 0,38677 | 0,20126 | 0,42207 | €833,00 | €1.665,99 | €49,19 | €0,00 |
| Master Adaptive V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €203,80 | €407,60 | €48,91 | €0,00 |
| Master Adaptive V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00319 | 0,00319 | 0,00281 | 0,00161 | 0,00396 | €205,42 | €410,83 | €49,30 | €0,00 |
| Master Adaptive V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10713 | €21,54 | €43,08 | €0,79 | €0,00 |
| Master Adaptive V1 | BANK | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,38852 | 0,38315 | 0,35255 | 0,19620 | 0,46046 | €240,10 | €480,20 | €44,46 | €-6,63 |
| Master Adaptive No Alt V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39854 | 0,39854 | 0,38677 | 0,20126 | 0,42207 | €833,00 | €1.665,99 | €49,19 | €0,00 |
| Master Adaptive No Alt V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €203,80 | €407,60 | €48,91 | €0,00 |
| Master Adaptive No Alt V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00319 | 0,00319 | 0,00281 | 0,00161 | 0,00396 | €205,42 | €410,83 | €49,30 | €0,00 |
| Master Adaptive No Alt V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10713 | €21,54 | €43,08 | €0,79 | €0,00 |
| Master Adaptive No Alt V1 | BANK | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,38852 | 0,38315 | 0,35255 | 0,19620 | 0,46046 | €240,53 | €481,06 | €44,54 | €-6,65 |
| Master Adaptive Strict3 V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,41951 | €887,07 | €1.774,14 | €49,03 | €0,00 |
| Master Adaptive Strict3 V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00320 | 0,00320 | 0,00282 | 0,00162 | 0,00397 | €201,87 | €403,75 | €48,45 | €0,00 |
| Master Adaptive Strict3 V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10713 | €1.330,61 | €2.661,21 | €48,54 | €0,00 |
| Master Adaptive Strict3 V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 1943,95871 | 1959,42000 | 1915,96571 | 981,69915 | 1999,94472 | €1.509,27 | €3.018,53 | €43,47 | €24,01 |
| Master Adaptive Expanded V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39854 | 0,39854 | 0,38677 | 0,20126 | 0,42207 | €833,00 | €1.665,99 | €49,19 | €0,00 |
| Master Adaptive Expanded V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €203,80 | €407,60 | €48,91 | €0,00 |
| Master Adaptive Expanded V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00319 | 0,00319 | 0,00281 | 0,00161 | 0,00396 | €206,32 | €412,65 | €49,52 | €0,00 |
| Master Adaptive Expanded V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10713 | €33,54 | €67,08 | €1,22 | €0,00 |
| Master Adaptive Expanded V1 | BANK | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,38852 | 0,38315 | 0,35255 | 0,19620 | 0,46046 | €241,27 | €482,55 | €44,68 | €-6,67 |
| Master Adaptive Gb20 V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,40304 | 0,40304 | 0,39140 | 0,20354 | 0,42632 | €848,64 | €1.697,27 | €49,02 | €0,00 |
| Master Adaptive Gb20 V1 | RIF | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,10582 | 0,10582 | 0,09312 | 0,05344 | 0,13122 | €201,89 | €403,77 | €48,45 | €0,00 |
| Master Adaptive Gb20 V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 367,08012 | 367,08012 | 360,46822 | 185,37546 | 380,30391 | €1.348,01 | €2.696,02 | €48,56 | €0,00 |
| Master Adaptive Gb20 V1 | BANK | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,38852 | 0,38315 | 0,35255 | 0,19620 | 0,46046 | €253,27 | €506,54 | €46,90 | €-7,00 |
| Master Adaptive Runner25 V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39854 | 0,39854 | 0,38677 | 0,20126 | 0,43384 | €833,00 | €1.665,99 | €49,19 | €0,00 |
| Master Adaptive Runner25 V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,21338 | €203,80 | €407,60 | €48,91 | €0,00 |
| Master Adaptive Runner25 V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00319 | 0,00319 | 0,00281 | 0,00161 | 0,00434 | €205,36 | €410,73 | €49,29 | €0,00 |
| Master Adaptive Runner25 V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 386,79573 | €20,87 | €41,74 | €0,76 | €0,00 |
| Master Adaptive Runner25 V1 | BANK | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,38852 | 0,38315 | 0,35255 | 0,19620 | 0,49643 | €241,27 | €482,53 | €44,68 | €-6,67 |
| Combo Adaptive — Side × Regime Guard | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,00320 | 0,00320 | 0,00282 | 0,00162 | 0,00397 | €212,78 | €425,56 | €51,07 | €0,00 |
| Combo Adaptive — Side × Regime Guard | BANK | LONG | Combo Adaptive | 60m | 2,0x | 0,37568 | 0,38315 | 0,33059 | 0,18972 | 0,46584 | €212,08 | €424,15 | €50,90 | €8,44 |
| Combo Adaptive — Side × Regime Guard | ALLO | SHORT | Combo Adaptive | 60m | 2,0x | 0,35250 | 0,35250 | 0,39075 | 0,52699 | 0,27600 | €235,86 | €471,72 | €51,19 | €-0,00 |
| Combo Adaptive — Side × Regime Guard | SHIB | LONG | Combo Adaptive | 60m | 2,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €450,93 | €901,86 | €50,61 | €-10,82 |
| Master Adaptive GB20 — Breakeven 0,5R | BEAT | LONG | Master Adaptive Consensus | 60m | 2,0x | 3,29017 | 3,29017 | 3,00714 | 1,66154 | 3,85623 | €291,32 | €582,63 | €50,12 | €0,00 |
| Master Adaptive GB20 — Breakeven 0,5R | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 367,86058 | 367,86058 | 361,23463 | 185,76959 | 381,11249 | €1.403,77 | €2.807,55 | €50,57 | €0,00 |
| Master Adaptive GB20 — Breakeven 0,5R | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00317 | 0,00317 | 0,00283 | 0,00160 | 0,00387 | €231,91 | €463,82 | €50,56 | €0,00 |
| Master Adaptive GB20 — Breakeven 0,5R | BANK | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,38852 | 0,38315 | 0,35255 | 0,19620 | 0,46046 | €245,56 | €491,11 | €45,47 | €-6,79 |
| Master Adaptive GB20 — 50% a 0,75R | BEAT | LONG | Master Adaptive Consensus | 60m | 2,0x | 3,29017 | 3,29017 | 3,00714 | 1,66154 | 3,85623 | €291,05 | €582,09 | €50,07 | €0,00 |
| Master Adaptive GB20 — 50% a 0,75R | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10713 | €1.376,47 | €2.752,95 | €50,21 | €0,00 |
| Master Adaptive GB20 — 50% a 0,75R | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00322 | 0,00322 | 0,00284 | 0,00163 | 0,00400 | €209,67 | €419,35 | €50,32 | €0,00 |
| Master Adaptive GB20 — 50% a 0,75R | BANK | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,37759 | 0,38315 | 0,33768 | 0,19068 | 0,45741 | €219,98 | €439,96 | €46,50 | €6,48 |
| Master Adaptive GB20 — Loss Cap 0,75R | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00275 | 0,00275 | 0,00242 | 0,00139 | 0,00362 | €208,32 | €416,65 | €50,00 | €0,00 |
| Master Adaptive GB20 — Loss Cap 0,75R | BEAT | LONG | Master Adaptive Consensus | 60m | 2,0x | 3,29017 | 3,29017 | 3,07790 | 1,66154 | 3,85623 | €388,25 | €776,50 | €50,10 | €0,00 |
| Master Adaptive GB20 — Loss Cap 0,75R | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 361,71345 | 185,19860 | 380,10713 | €1.835,86 | €3.671,71 | €50,22 | €0,00 |
| Master Adaptive GB20 — Loss Cap 0,75R | BANK | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,38852 | 0,38315 | 0,36154 | 0,19620 | 0,46046 | €328,63 | €657,26 | €45,64 | €-9,08 |
| Rapida V3 NoHigh — Range Only | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00320 | 0,00320 | 0,00286 | 0,00215 | 0,00370 | €161,22 | €483,65 | €50,91 | €0,00 |
| Rapida V3 NoHigh — Range Only | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,33165 | 0,33165 | 0,36472 | 0,44055 | 0,28205 | €170,92 | €512,75 | €51,13 | €-0,00 |
| Rapida V3 NoHigh — Range Only | ESPORTS | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,02828 | 0,02804 | 0,03168 | 0,03757 | 0,02319 | €142,68 | €428,04 | €51,37 | €3,70 |
| Rapida V3 NoHigh — Regime Guard | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00320 | 0,00320 | 0,00286 | 0,00215 | 0,00370 | €161,22 | €483,65 | €50,91 | €0,00 |
| Rapida V3 NoHigh — Regime Guard | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,33165 | 0,33165 | 0,36472 | 0,44055 | 0,28205 | €172,19 | €516,57 | €51,51 | €-0,00 |
| Rapida V3 NoHigh — Regime Guard | SHIB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €15,44 | €46,31 | €2,01 | €-0,89 |
| MAIN — Side × Regime Guard | AKE | LONG | Confluenza trend | 240m | 3,0x | 0,00322 | 0,00322 | 0,00284 | 0,00216 | 0,00400 | €140,56 | €421,69 | €50,60 | €0,00 |
| MAIN — Side × Regime Guard | ALLO | SHORT | Confluenza trend | 240m | 3,0x | 0,38070 | 0,38070 | 0,37357 | 0,50570 | 0,28933 | €140,03 | €420,08 | €0,00 | €-0,00 |
| MAIN — Side × Regime Guard | PEPE | LONG | Confluenza trend | 240m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €326,47 | €979,41 | €50,44 | €5,69 |
| MAIN — Side × Regime Guard | BANK | LONG | Confluenza trend | 240m | 3,0x | 0,38202 | 0,38315 | 0,33617 | 0,25659 | 0,47370 | €139,71 | €419,14 | €50,30 | €1,24 |
| MAIN — Dynamic Asset Selector | AKE | LONG | Confluenza trend | 240m | 3,0x | 0,00322 | 0,00322 | 0,00284 | 0,00216 | 0,00400 | €140,56 | €421,69 | €50,60 | €0,00 |
| MAIN — Dynamic Asset Selector | BANK | LONG | Confluenza trend | 240m | 3,0x | 0,38202 | 0,38315 | 0,33617 | 0,25659 | 0,47370 | €140,87 | €422,62 | €50,71 | €1,25 |
| Combo Trend — Side × Regime Guard | AKE | LONG | Combo Trend | 60m | 2,0x | 0,00320 | 0,00320 | 0,00282 | 0,00162 | 0,00405 | €211,52 | €423,03 | €50,76 | €0,00 |
| Combo Trend — Side × Regime Guard | BANK | LONG | Combo Trend | 60m | 2,0x | 0,37568 | 0,38315 | 0,33059 | 0,18972 | 0,47485 | €207,08 | €414,15 | €49,70 | €8,24 |
| Combo Trend — Side × Regime Guard | ALLO | SHORT | Combo Trend | 60m | 2,0x | 0,35250 | 0,35250 | 0,39480 | 0,52699 | 0,25944 | €209,77 | €419,55 | €50,35 | €-0,00 |
| Combo Trend — Side × Regime Guard | SHIB | LONG | Combo Trend | 60m | 2,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €14,70 | €29,40 | €1,89 | €-1,53 |
| Combo Trend — Side × Regime Guard | PEPE | LONG | Combo Trend | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €12,55 | €25,09 | €0,84 | €0,20 |
| Combo Trend — Side × Regime Guard | ETH | LONG | Combo Trend | 60m | 2,0x | 1949,77988 | 1959,42000 | 1918,58340 | 984,63884 | 2018,41213 | €12,70 | €25,41 | €0,41 | €0,13 |
| Combo Trend — Side × Regime Guard | ESPORTS | SHORT | Combo Trend | 60m | 2,0x | 0,02845 | 0,02804 | 0,03187 | 0,04254 | 0,02094 | €202,36 | €404,73 | €48,57 | €5,89 |
| FAST NoHigh <7,5 · SHORT only | WLD | SHORT | Momentum / breakout | 60m | 3,0x | 0,34959 | 0,34959 | 0,35668 | 0,46437 | 0,33896 | €822,35 | €2.467,06 | €50,00 | €-0,00 |
| FAST NoHigh <7,5 · SHORT only | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00314 | 0,00314 | 0,00287 | 0,00211 | 0,00354 | €200,24 | €600,71 | €51,24 | €0,00 |
| FAST NoHigh <7,5 · SHORT only | ALLO | SHORT | Momentum / breakout | 60m | 3,0x | 0,33808 | 0,33808 | 0,36389 | 0,44909 | 0,29937 | €212,58 | €637,75 | €48,69 | €-0,00 |
| FAST NoHigh <7,5 · SHORT only | SHIB | LONG | Momentum / breakout | 60m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €25,54 | €76,62 | €3,32 | €-1,47 |
| FAST NoHigh <7,5 · SHORT only | ETH | LONG | Momentum / breakout | 60m | 3,0x | 1943,95871 | 1959,42000 | 1922,18638 | 1305,69227 | 1976,61722 | €1.451,62 | €4.354,85 | €48,77 | €34,64 |
| FAST NoHigh <7,5 · SHORT only | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 60,04501 | 60,32300 | 59,37250 | 40,33023 | 61,05376 | €14,15 | €42,44 | €0,48 | €0,20 |
| Bilanciata V3 · LONG only | XMR | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 366,72991 | 366,72991 | 360,04130 | 246,32025 | 380,10712 | €913,56 | €2.740,69 | €49,99 | €0,00 |
| Bilanciata V3 · LONG only | AKE | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,00328 | 0,00328 | 0,00288 | 0,00220 | 0,00406 | €137,93 | €413,80 | €49,66 | €0,00 |
| Bilanciata V3 · LONG only | ALLO | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,34255 | 0,34255 | 0,37914 | 0,45502 | 0,26938 | €156,01 | €468,04 | €49,99 | €-0,00 |
| Bilanciata V3 · LONG only | ESPORTS | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,03342 | 0,02804 | 0,03342 | 0,04440 | 0,02540 | €137,40 | €412,21 | €0,00 | €66,39 |
| Bilanciata V3 · LONG only | ETH | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1958,25157 | 1959,42000 | 1930,05275 | 1315,29231 | 2014,64922 | €32,22 | €96,65 | €1,39 | €0,06 |
| Scanner Bottom5 Short Profit Lock V1 | WLD | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,34449 | 0,34449 | 0,35368 | 0,51502 | 0,32613 | €937,87 | €1.875,74 | €50,00 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | ALLO | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,35250 | 0,35250 | 0,39075 | 0,52699 | 0,27600 | €227,60 | €455,20 | €49,39 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | ESPORTS | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,03342 | 0,02804 | 0,03262 | 0,04997 | 0,02540 | €206,07 | €412,14 | €0,00 | €66,38 |
| Scanner Bottom5 Short Mfe Trail V1 | WLD | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,34449 | 0,34449 | 0,35368 | 0,51502 | 0,32613 | €937,87 | €1.875,74 | €50,00 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | ALLO | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,35653 | 0,35653 | 0,39522 | 0,53301 | 0,27915 | €228,22 | €456,45 | €49,53 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | ESPORTS | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,02828 | 0,02804 | 0,03168 | 0,04229 | 0,02150 | €206,75 | €413,50 | €49,62 | €3,57 |
| Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00323 | 0,00323 | 0,00290 | 0,00217 | 0,00390 | €162,23 | €486,68 | €50,00 | €0,00 |
| Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | SHIB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €392,53 | €1.177,60 | €51,08 | €-22,62 |
| Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | PEPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €912,60 | €2.737,79 | €50,84 | €-3,23 |
| Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1943,95871 | 1959,42000 | 1922,18638 | 1305,69227 | 1987,50339 | €1.490,87 | €4.472,61 | €50,09 | €35,57 |
| Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 60,04501 | 60,32300 | 59,37250 | 40,33023 | 61,39001 | €13,99 | €41,96 | €0,47 | €0,19 |
| Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00320 | 0,00320 | 0,00287 | 0,00215 | 0,00386 | €162,16 | €486,47 | €49,98 | €0,00 |
| Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,35250 | 0,35250 | 0,38225 | 0,46824 | 0,29300 | €194,51 | €583,53 | €49,25 | €-0,00 |
| Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | PEPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €882,40 | €2.647,20 | €49,16 | €-3,12 |
| Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | ESPORTS | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,02998 | 0,02804 | 0,03358 | 0,03983 | 0,02279 | €132,90 | €398,69 | €47,84 | €25,85 |
| Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1943,95871 | 1959,42000 | 1922,18638 | 1305,69227 | 1987,50339 | €11,18 | €33,53 | €0,38 | €0,27 |
| Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | ESPORTS | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,02828 | 0,02804 | 0,03168 | 0,03757 | 0,02150 | €141,08 | €423,23 | €50,79 | €3,66 |
| Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | SHIB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €390,30 | €1.170,89 | €50,79 | €-22,49 |
| Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00323 | 0,00323 | 0,00290 | 0,00217 | 0,00390 | €162,03 | €486,10 | €49,94 | €0,00 |
| Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,35250 | 0,35250 | 0,38225 | 0,46824 | 0,29300 | €190,72 | €572,15 | €48,29 | €-0,00 |
| Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | SHIB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €390,89 | €1.172,67 | €50,86 | €-22,53 |
| Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | PEPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €911,83 | €2.735,48 | €50,80 | €-3,22 |
| Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1943,95871 | 1959,42000 | 1922,18638 | 1305,69227 | 1987,50339 | €58,50 | €175,50 | €1,97 | €1,40 |
| Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00317 | 0,00317 | 0,00290 | 0,00213 | 0,00371 | €196,95 | €590,84 | €50,09 | €0,00 |
| Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,33808 | 0,33808 | 0,36389 | 0,44909 | 0,28646 | €211,10 | €633,31 | €48,35 | €-0,00 |
| Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | PEPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €919,09 | €2.757,26 | €51,20 | €-3,25 |
| Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1943,95871 | 1959,42000 | 1922,18638 | 1305,69227 | 1987,50339 | €1.516,14 | €4.548,41 | €50,94 | €36,18 |
| Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,38852 | 0,38315 | 0,36054 | 0,26095 | 0,44447 | €14,38 | €43,13 | €3,11 | €-0,60 |
| Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 60,04501 | 60,32300 | 59,37250 | 40,33023 | 61,39001 | €17,30 | €51,91 | €0,58 | €0,24 |
| Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00320 | 0,00320 | 0,00287 | 0,00215 | 0,00386 | €162,21 | €486,64 | €50,00 | €0,00 |
| Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | SHIB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €386,01 | €1.158,04 | €50,23 | €-22,24 |
| Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | PEPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €897,83 | €2.693,49 | €50,02 | €-3,17 |
| Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1943,95871 | 1959,42000 | 1922,18638 | 1305,69227 | 1987,50339 | €1.443,11 | €4.329,34 | €48,49 | €34,43 |
| Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 60,04501 | 60,32300 | 59,37250 | 40,33023 | 61,39001 | €13,53 | €40,59 | €0,45 | €0,19 |
| Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00319 | 0,00319 | 0,00287 | 0,00215 | 0,00385 | €162,18 | €486,55 | €49,99 | €0,00 |
| Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | SHIB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €397,61 | €1.192,82 | €51,74 | €-22,91 |
| Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | PEPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €924,39 | €2.773,18 | €51,50 | €-3,27 |
| Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1943,95871 | 1959,42000 | 1922,18638 | 1305,69227 | 1987,50339 | €1.522,40 | €4.567,21 | €51,15 | €36,33 |
| Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 60,04501 | 60,32300 | 59,37250 | 40,33023 | 61,39001 | €21,34 | €64,03 | €0,72 | €0,30 |
| Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00320 | 0,00320 | 0,00287 | 0,00215 | 0,00386 | €162,16 | €486,47 | €49,98 | €0,00 |
| Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,35250 | 0,35250 | 0,38225 | 0,46824 | 0,29300 | €194,51 | €583,53 | €49,25 | €-0,00 |
| Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | PEPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €882,40 | €2.647,20 | €49,16 | €-3,12 |
| Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1943,95871 | 1959,42000 | 1922,18638 | 1305,69227 | 1987,50339 | €1.423,15 | €4.269,44 | €47,82 | €33,96 |
| Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 60,04501 | 60,32300 | 59,37250 | 40,33023 | 61,39001 | €14,65 | €43,94 | €0,49 | €0,20 |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00320 | 0,00320 | 0,00287 | 0,00215 | 0,00386 | €162,23 | €486,68 | €50,00 | €0,00 |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,33713 | 0,33713 | 0,36471 | 0,44782 | 0,28197 | €208,24 | €624,73 | €51,11 | €-0,00 |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,38680 | 0,38315 | 0,35294 | 0,25980 | 0,45452 | €193,81 | €581,44 | €50,90 | €-5,48 |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | XRP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,11443 | 1,10943 | 1,10195 | 0,74853 | 1,13940 | €23,07 | €69,20 | €0,78 | €-0,31 |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1952,19036 | 1959,42000 | 1930,32583 | 1311,22119 | 1995,91942 | €12,06 | €36,18 | €0,41 | €0,13 |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | ESPORTS | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,03070 | 0,02804 | 0,03439 | 0,04078 | 0,02333 | €138,06 | €414,17 | €49,70 | €35,93 |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 60,04501 | 60,32300 | 59,37250 | 40,33023 | 61,39001 | €17,07 | €51,20 | €0,57 | €0,24 |
| Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | XRP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,11443 | 1,10943 | 1,10195 | 0,74853 | 1,13940 | €1.516,65 | €4.549,94 | €50,96 | €-20,43 |
| Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | PEPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €875,94 | €2.627,83 | €50,14 | €-11,57 |
| Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1943,95871 | 1959,42000 | 1922,18638 | 1305,69227 | 1987,50339 | €1.489,14 | €4.467,43 | €50,04 | €35,53 |
| Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00320 | 0,00320 | 0,00289 | 0,00215 | 0,00382 | €172,57 | €517,70 | €50,00 | €0,00 |
| Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | SHIB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €10,87 | €32,61 | €1,41 | €-0,63 |
| Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | PEPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €916,91 | €2.750,72 | €51,08 | €-3,24 |
| Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1943,95871 | 1959,42000 | 1922,18638 | 1305,69227 | 1987,50339 | €1.512,51 | €4.537,54 | €50,82 | €36,09 |
| Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,38852 | 0,38315 | 0,36054 | 0,26095 | 0,44447 | €230,95 | €692,84 | €49,89 | €-9,57 |
| Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 60,04501 | 60,32300 | 59,37250 | 40,33023 | 61,39001 | €10,44 | €31,33 | €0,35 | €0,15 |
| Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00317 | 0,00317 | 0,00290 | 0,00213 | 0,00371 | €200,37 | €601,11 | €50,97 | €0,00 |
| Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,35250 | 0,35250 | 0,38225 | 0,46824 | 0,29300 | €200,65 | €601,96 | €50,80 | €-0,00 |
| Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | ESPORTS | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,03342 | 0,02804 | 0,03342 | 0,04440 | 0,02540 | €136,12 | €408,37 | €0,00 | €65,77 |
| Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | SHIB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €36,61 | €109,84 | €4,76 | €-2,11 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Benchmark Bollinger mean reversion 1H | ETH | SHORT | 2026-07-27T04:23:38+00:00 | 1955,86734 | €-1,52 | -0,03 | STOP |
| Scanner Top 5 Long 1H | SHIB | LONG | 2026-07-27T02:53:36+00:00 | 0,00001 | €-54,36 | -1,03 | STOP |
| Top 5 + BTC — target pieno 3R | SHIB | LONG | 2026-07-27T02:53:36+00:00 | 0,00001 | €-47,76 | -1,03 | STOP |
| Top 5 + BTC — 75% a 2,2R + runner 3R | SHIB | LONG | 2026-07-27T02:53:36+00:00 | 0,00001 | €-48,90 | -1,03 | STOP |
| Top 5 + BTC — solo MFE | PEPE | LONG | 2026-07-27T02:53:36+00:00 | 0,00000 | €0,16 | 0,20 | STOP |
| Top 5 + BTC — Guard | SHIB | LONG | 2026-07-27T02:53:36+00:00 | 0,00001 | €-49,77 | -1,03 | STOP |
| Top 5 + BTC — Guard + BTC≤3 | SHIB | LONG | 2026-07-27T02:53:36+00:00 | 0,00001 | €-47,64 | -1,03 | STOP |
| Top 5 + BTC — BTC≤3 | SHIB | LONG | 2026-07-27T02:53:36+00:00 | 0,00001 | €-48,16 | -1,03 | STOP |
| Scanner Top 5 + forza BTC 1H | SHIB | LONG | 2026-07-27T02:53:36+00:00 | 0,00001 | €-50,14 | -1,03 | STOP |
| Forza relativa 1H V1 | SHIB | LONG | 2026-07-27T02:53:36+00:00 | 0,00001 | €-43,34 | -1,03 | STOP |
| Master Adaptive V1 | SHIB | LONG | 2026-07-27T02:53:36+00:00 | 0,00001 | €-46,66 | -1,03 | STOP |
| Master Adaptive Runner25 V1 | SHIB | LONG | 2026-07-27T02:53:36+00:00 | 0,00001 | €-46,89 | -1,03 | STOP |

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
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 10/30 | 11/30 | 1,22 | 2,93 | 0,14R | €13,74 | 2,01% | COERENTE + | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 8/30 | 13/30 | 1,07 | 1,79 | 0,05R | €14,39 | 1,62% | COERENTE + | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 8/30 | 13/30 | 1,07 | 1,75 | 0,05R | €10,76 | 2,27% | COERENTE + | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 8/30 | 14/30 | 1,08 | 0,92 | 0,05R | €-1,74 | 2,38% | DIVERGENTE | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 1/30 | 6/30 | ∞ | 1,56 | 1,96R | €9,44 | 2,15% | COERENTE + | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 8/30 | 12/30 | 1,82 | 3,31 | 0,43R | €11,74 | 1,01% | COERENTE + | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 12/30 | 11/30 | 1,32 | 0,45 | 0,20R | €-15,23 | 2,93% | DIVERGENTE | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 8/30 | 13/30 | 2,98 | 3,37 | 0,80R | €20,80 | 1,97% | COERENTE + | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 9/30 | 18/30 | 2,27 | 1,95 | 0,60R | €11,76 | 1,14% | COERENTE + | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 6/30 | 8/30 | 1,77 | 1,47 | 0,42R | €9,72 | 2,06% | COERENTE + | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 9/30 | 15/30 | 1,45 | 1,55 | 0,27R | €8,82 | 1,60% | COERENTE + | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 12/30 | 11/30 | 1,32 | 0,45 | 0,20R | €-15,23 | 3,08% | DIVERGENTE | RACCOLTA RESEARCH |
| MAIN | Principale 4H | 65/30 | 21/30 | 1,05 | 0,68 | 0,04R | €-11,50 | 4,52% | DIVERGENTE | BOCCIATA RESEARCH |
| MAIN_DYNAMIC_ASSET_SELECTOR_V1 | MAIN — Dynamic Asset Selector | 0/30 | 4/30 | 0,00 | 3,55 | 0,00R | €35,68 | 1,03% | n/a | RACCOLTA RESEARCH |
| MAIN_SIDE_REGIME_GUARD_V1 | MAIN — Side × Regime Guard | 0/30 | 5/30 | 0,00 | 1,81 | 0,00R | €17,72 | 1,49% | n/a | RACCOLTA RESEARCH |
| RSI_EXTREME_LONG_15M | Scalp RSI Long 25 · prudente · 5x (riferimento tra 9 varianti) | 10/30 | 5/30 | 0,31 | 0,20 | -0,54R | €-4,60 | 0,37% | COERENTE − | RACCOLTA RESEARCH |
| RSI_EXTREME_SHORT_15M | Scalp RSI Short 75 · prudente · 5x (riferimento tra 9 varianti) | 12/30 | 9/30 | 0,40 | 0,16 | -0,41R | €-6,21 | 0,56% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_1H_BALANCED | Bilanciata 1H V1 | 176/30 | 48/30 | 1,00 | 1,32 | 0,00R | €6,56 | 3,25% | COERENTE + | BOCCIATA RESEARCH |
| SHADOW_1H_BALANCED_LONG_NO_RHV_V1 | Bilanciata 1H — LONG senza Range High Vol | 0/30 | 9/30 | 0,00 | 0,60 | 0,00R | €-14,47 | 2,47% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_BALANCED_SHORT_TREND_DOWN_STRICT_V1 | Bilanciata 1H — SHORT Trend Down stretto | 0/30 | 1/30 | 0,00 | 0,00 | 0,00R | €-4,13 | 0,59% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_BALANCED_V2 | Bilanciata 1H V2 | 47/30 | 34/30 | 1,35 | 1,13 | 0,20R | €2,78 | 2,75% | COERENTE + | PRONTA PER REVISIONE LIVE |
| SHADOW_1H_BALANCED_V3 | Bilanciata 1H V3 Filtered | 79/30 | 46/30 | 1,13 | 1,62 | 0,08R | €12,64 | 2,20% | COERENTE + | PRONTA PER REVISIONE LIVE |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | Bilanciata V3 · LONG only | 4/30 | 7/30 | 0,62 | 0,74 | -0,30R | €-6,19 | 1,46% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_1H_FAST | Rapida 1H V1 — madre | 204/30 | 76/30 | 0,92 | 0,99 | -0,05R | €-0,31 | 6,76% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | Rapida V1 — Long + BTC 1–3 + score <7,5 | 20/30 | 18/30 | 1,52 | 1,09 | 0,25R | €1,78 | 2,07% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | FAST NoHigh <7,5 · SHORT only | 18/30 | 16/30 | 1,71 | 1,44 | 0,33R | €6,54 | 1,76% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | Rapida V1 — no HIGH + score <7,5 | 82/30 | 52/30 | 1,18 | 1,46 | 0,10R | €8,84 | 2,83% | COERENTE + | PRONTA PER REVISIONE LIVE |
| SHADOW_1H_FAST_NO_PEPE_V1 | Rapida V1 — senza PEPE | 85/30 | 43/30 | 1,00 | 1,12 | 0,00R | €2,44 | 2,15% | COERENTE + | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_COST_AWARE_V1 | Rapida score 6–7,5 — Cost Aware | 0/30 | 13/30 | 0,00 | 2,33 | 0,00R | €22,60 | 1,96% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_NO_TREND_UP_V1 | Rapida score 6–7,5 — senza Trend Up | 0/30 | 14/30 | 0,00 | 1,91 | 0,00R | €15,94 | 2,01% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_RANGE_ONLY_V1 | Rapida score 6–7,5 — Range Only | 0/30 | 9/30 | 0,00 | 3,17 | 0,00R | €33,01 | 2,28% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_V1 | Rapida V1 — score 6–7,5 | 60/30 | 49/30 | 1,17 | 1,36 | 0,10R | €6,81 | 2,49% | COERENTE + | PRONTA PER REVISIONE LIVE |
| SHADOW_1H_FAST_TP2_V1 | Rapida V1 — target pieno 2R | 78/30 | 47/30 | 0,95 | 1,02 | -0,03R | €0,38 | 2,58% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V2 | Rapida 1H V2 | 13/30 | 13/30 | 0,70 | 1,15 | -0,21R | €3,35 | 1,69% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3 | Rapida 1H V3 Filtered — madre | 126/30 | 75/30 | 1,10 | 1,11 | 0,06R | €2,18 | 2,89% | COERENTE + | PRONTA PER REVISIONE LIVE |
| SHADOW_1H_FAST_V3_CAP75_V1 | Rapida V3 — score <7,5 | 70/30 | 45/30 | 1,06 | 1,55 | 0,04R | €9,29 | 2,49% | COERENTE + | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | Rapida V3 — qualità completa + profit lock | 38/30 | 39/30 | 1,00 | 0,93 | 0,00R | €-1,68 | 3,21% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | Rapida V3 — Long + no HIGH + score <7,5 | 38/30 | 36/30 | 1,00 | 1,01 | 0,00R | €0,29 | 2,86% | COERENTE + | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | Rapida V3 — Long Only | 47/30 | 40/30 | 1,02 | 0,78 | 0,01R | €-5,50 | 3,67% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V1 | Rapida V3 NoHigh — Range Only | 0/30 | 9/30 | 0,00 | 2,37 | 0,00R | €24,66 | 1,78% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_V1 | Rapida V3 NoHigh — Regime Guard | 0/30 | 16/30 | 0,00 | 2,99 | 0,00R | €20,16 | 1,39% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | Rapida V3 — no volatilità HIGH | 81/30 | 50/30 | 1,07 | 0,94 | 0,04R | €-1,41 | 2,96% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONLY_V1 | Rapida V3 senza ESPORTS — Long Only | 0/30 | 17/30 | 0,00 | 1,50 | 0,00R | €7,98 | 1,32% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_V1 | Rapida V3 senza ESPORTS — MFE Lock | 0/30 | 24/30 | 0,00 | 1,78 | 0,00R | €9,48 | 2,05% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_GUARD_V1 | Rapida V3 senza ESPORTS — Stress Guard | 0/30 | 13/30 | 0,00 | 1,15 | 0,00R | €3,85 | 2,17% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | Rapida V3 — senza ESPORTS | 80/30 | 49/30 | 0,98 | 0,96 | -0,01R | €-0,89 | 2,49% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_4H_WIDE | Ampia 4H | 51/30 | 17/30 | 1,03 | 0,89 | 0,02R | €-3,14 | 3,67% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_BOLLINGER_MR_1H | Benchmark Bollinger mean reversion 1H | 49/30 | 38/30 | 1,16 | 0,93 | 0,09R | €-1,67 | 4,19% | DIVERGENTE | BOCCIATA PAPER |
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
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | Combo Adaptive — parziale 1R | 64/30 | 18/30 | 0,89 | 0,47 | -0,08R | €-17,47 | 3,32% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | Combo Adaptive — Quality7 + Regime + parziale 1R | 6/30 | 6/30 | 0,37 | 0,37 | -0,55R | €-22,27 | 1,95% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | Combo Adaptive — Quality7 + Regime | 6/30 | 6/30 | 0,37 | 0,13 | -0,55R | €-32,34 | 2,32% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | Combo Adaptive — Quality7 | 18/30 | 16/30 | 1,20 | 1,38 | 0,13R | €4,31 | 1,51% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | Combo Adaptive — Trend/Transition | 30/30 | 11/30 | 0,36 | 0,78 | -0,57R | €-6,81 | 2,18% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | Combo Adaptive — 75% a 2R + runner 25% a 3R | 40/30 | 22/30 | 0,58 | 1,17 | -0,37R | €3,48 | 2,12% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_SIDE_REGIME_GUARD_V1 | Combo Adaptive — Side × Regime Guard | 0/30 | 11/30 | 0,00 | 2,69 | 0,00R | €16,59 | 1,41% | n/a | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | Combo Adaptive — target pieno 3R | 40/30 | 13/30 | 0,58 | 0,76 | -0,37R | €-5,13 | 1,41% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_MEAN_REVERSION | Combo Mean Reversion | 18/30 | 16/30 | 1,12 | 1,36 | 0,07R | €8,67 | 2,31% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_COMBO_SCANNER | Combo Scanner | 73/30 | 34/30 | 1,52 | 0,88 | 0,30R | €-3,43 | 3,25% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_COMBO_TREND | Combo Trend | 96/30 | 38/30 | 1,04 | 0,71 | 0,03R | €-11,03 | 7,02% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_COMBO_TREND_SIDE_REGIME_GUARD_V1 | Combo Trend — Side × Regime Guard | 0/30 | 11/30 | 0,00 | 1,68 | 0,00R | €10,36 | 1,32% | n/a | RACCOLTA RESEARCH |
| SHADOW_DOGE_BOLLINGER_1H | Doge Bollinger 1H | 2/30 | 2/30 | 0,00 | 0,00 | -1,12R | €-55,56 | 1,26% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_DOGE_DONCHIAN_1H | Doge Donchian 1H | 3/30 | 4/30 | 0,84 | 0,98 | -0,12R | €-0,31 | 0,96% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_DOGE_EMA_1H | Doge Ema 1H | 4/30 | 8/30 | 1,71 | 1,55 | 0,39R | €11,48 | 1,36% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_DONCHIAN_1H | Benchmark Donchian breakout 1H | 58/30 | 26/30 | 0,90 | 1,89 | -0,08R | €18,18 | 2,12% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_EMA_TREND_1H | Benchmark trend following EMA 1H | 100/30 | 26/30 | 1,06 | 0,94 | 0,04R | €-1,31 | 2,25% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_ETH_ADAPTIVE_1H | Eth Adaptive 1H | 5/30 | 5/30 | 0,42 | 0,11 | -0,51R | €-29,22 | 1,84% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_BOLLINGER_1H | Eth Bollinger 1H | 1/30 | 1/30 | 0,00 | ∞ | -1,13R | €15,45 | 0,51% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_ETH_DONCHIAN_1H | Eth Donchian 1H | 4/30 | 4/30 | 0,56 | 0,56 | -0,37R | €-18,17 | 1,38% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_EMA_1H | Eth Ema 1H | 5/30 | 7/30 | 0,43 | 0,20 | -0,51R | €-31,18 | 2,52% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_EMA_4H | Eth Ema 4H | 1/30 | 1/30 | 0,00 | 0,00 | -1,06R | €-52,88 | 0,80% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_GLOBAL_PURE | Global Confluence puro 1H | 4/30 | 10/30 | 1,75 | 0,37 | 0,41R | €-20,93 | 2,92% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | Master Adaptive Expanded V1 | 31/30 | 13/30 | 0,89 | 0,47 | -0,07R | €-24,82 | 3,62% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_BE_V1 | Master Adaptive GB20 — Breakeven 0,5R | 0/30 | 12/30 | 0,00 | 0,55 | 0,00R | €-13,47 | 3,13% | n/a | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_LOSS_CAP_V1 | Master Adaptive GB20 — Loss Cap 0,75R | 0/30 | 8/30 | 0,00 | 0,40 | 0,00R | €-24,97 | 3,61% | n/a | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_PARTIAL_V1 | Master Adaptive GB20 — 50% a 0,75R | 0/30 | 6/30 | 0,00 | 0,49 | 0,00R | €-23,78 | 2,50% | n/a | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | Master Adaptive Gb20 V1 | 31/30 | 47/30 | 0,77 | 0,59 | -0,17R | €-7,46 | 4,16% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | Master Adaptive No Alt V1 | 29/30 | 10/30 | 0,85 | 0,35 | -0,11R | €-36,23 | 4,02% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | Master Adaptive Runner25 V1 | 24/30 | 12/30 | 0,75 | 0,36 | -0,21R | €-29,78 | 3,97% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | Master Adaptive Strict3 V1 | 27/30 | 20/30 | 0,80 | 0,48 | -0,15R | €-26,17 | 5,48% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_V1 | Master Adaptive V1 | 31/30 | 10/30 | 0,77 | 0,35 | -0,17R | €-36,63 | 4,06% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_RELATIVE_STRENGTH | Forza relativa 1H V1 | 127/30 | 28/30 | 1,00 | 0,53 | -0,00R | €-14,48 | 6,18% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_RELATIVE_STRENGTH_V2 | Forza relativa 1H V2 | 46/30 | 39/30 | 1,47 | 0,96 | 0,28R | €-1,46 | 5,10% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_SCANNER_BOTTOM10_SHORT | Scanner Bottom10 Short | 6/30 | 6/30 | 0,00 | 0,11 | -1,11R | €-40,88 | 2,72% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_BOTTOM15_SHORT | Scanner Bottom15 Short | 6/30 | 6/30 | 0,00 | 0,11 | -1,11R | €-40,88 | 2,72% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_BOTTOM20_SHORT | Scanner Bottom20 Short | 6/30 | 6/30 | 0,00 | 0,11 | -1,11R | €-40,88 | 2,72% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT | Scanner Bottom 5 Short 1H | 50/30 | 29/30 | 0,80 | 0,61 | -0,14R | €-9,96 | 5,48% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT_CONTINUATION_V1 | Scanner Bottom5 Short Continuation V1 | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | Scanner Bottom5 Short Mfe Trail V1 | 2/30 | 6/30 | 0,00 | 0,54 | -1,10R | €-12,45 | 1,38% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | Scanner Bottom5 Short Profit Lock V1 | 2/30 | 5/30 | 0,00 | 0,25 | -1,10R | €-24,00 | 1,53% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP10_LONG | Scanner Top10 Long | 7/30 | 8/30 | 2,52 | 0,42 | 0,68R | €-18,08 | 3,62% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP15_LONG | Scanner Top15 Long | 7/30 | 8/30 | 2,52 | 0,42 | 0,68R | €-18,08 | 3,62% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP20_LONG | Scanner Top20 Long | 7/30 | 8/30 | 2,52 | 0,42 | 0,68R | €-18,08 | 3,62% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC | Scanner Top 5 + forza BTC 1H | 71/30 | 29/30 | 1,50 | 1,43 | 0,29R | €10,48 | 3,23% | COERENTE + | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | Top 5 + BTC — BTC 2–3 | 12/30 | 4/30 | 1,02 | 0,47 | 0,01R | €-16,77 | 2,84% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | Top 5 + BTC — BTC≤3 | 29/30 | 11/30 | 1,10 | 0,74 | 0,07R | €-9,43 | 3,23% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | Top 5 + BTC — Guard + BTC≤3 + MFE | 22/30 | 25/30 | 1,22 | 0,53 | 0,14R | €-14,25 | 3,93% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | Top 5 + BTC — Guard + BTC≤3 | 22/30 | 10/30 | 1,22 | 0,82 | 0,14R | €-7,52 | 3,23% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | Top 5 + BTC — Guard + MFE | 25/30 | 28/30 | 0,99 | 0,46 | -0,00R | €-16,63 | 5,08% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | Top 5 + BTC — Guard | 25/30 | 15/30 | 0,99 | 0,57 | -0,00R | €-16,52 | 3,33% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | Top 5 + BTC — solo MFE | 33/30 | 20/30 | 1,08 | 0,41 | 0,05R | €-14,51 | 3,95% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | Top 5 + BTC — 75% a 2,2R + runner 3R | 24/30 | 16/30 | 1,16 | 1,05 | 0,12R | €1,36 | 3,25% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | Top 5 + BTC — target pieno 3R | 24/30 | 12/30 | 1,16 | 1,00 | 0,12R | €-0,19 | 3,22% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_LONG | Scanner Top 5 Long 1H | 85/30 | 37/30 | 1,38 | 1,61 | 0,22R | €14,13 | 3,57% | COERENTE + | PRONTA PER REVISIONE LIVE |
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
- Prezzo DOGE: **0.07303**
- Pre-allarme: **0.0765**; zona armata: **0.0775**; trigger rejection: **0.078**
- Invalidazione prima dell’entrata: chiusura 15m sopra **0.07966**

| Capitale iniziale | Balance | Equity | P&L aperto | Eventi chiusi | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- |
| €3.600,00 | €3.600,00 | €3.600,00 | €0,00 | 0 | 0,00% | 0,00 | 0,00% |

### Filtri correnti

| Filtro | Valore | Stato |
| --- | --- | --- |
| Dati mercato | FRESH | OK |
| Candela 15m | 24.5 min | OK |
| Global DOGE | -6.0 | OK |
| Classic raw | -11.0 | OK |
| DOGE/BTC raw | -6.0 | OK |
| Pattern ribassista | MATURO | OK |
| BTC sotto filtro | 65451.1 | OK |

### Ultima candela 15m valutata

- Rejection accettata: **NO**; motivo: **trigger_touched, entry_not_chased**
- High **0.0729**; close **0.07281**; wick alta **41.2%**; volume **x0.44**

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

- Regime: **TREND_UP**
- Famiglia: **TREND_UP**
- Confidenza: **71,40%**
- Volatilità: **NORMAL**
- Rotazione strategie: **SOLO OSSERVAZIONE — nessun peso operativo viene ancora modificato**
- Motivo: Trend BTC rialzista confermato dalla breadth: score +2.0, 92% sopra EMA50, ADX 19.4.
- BTC trend score: **2,00**; ADX: **19,38**; breadth sopra EMA50: **91,67%**
- Mediana alt vs BTC: **-0,62%**; dispersione: **11,82%**

- Aperti in questo ciclo: **0**
- Chiusi in questo ciclo: **0**
- Posizioni research aperte: **799**
- Trade research chiusi: **3324**
- Eventi di mercato indipendenti chiusi: **834**
- Segnali sovrapposti saltati sullo stesso asset/profilo: **17200**
- Posizioni Research V1 senza regime scartate durante la migrazione: **28**

### Risultati complessivi per strategia

| Profilo | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | 10 | 10 | 10 | 40,00% | 1,22 | 0,14R | €13,71 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | 8 | 8 | 8 | 37,50% | 1,07 | 0,05R | €3,98 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | 8 | 8 | 8 | 37,50% | 1,07 | 0,05R | €3,98 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | 8 | 8 | 8 | 37,50% | 1,08 | 0,05R | €4,25 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | 6 | 1 | 1 | 100,00% | ∞ | 1,96R | €19,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | 7 | 8 | 8 | 50,00% | 1,82 | 0,43R | €34,75 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | 9 | 12 | 12 | 41,67% | 1,32 | 0,20R | €23,60 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | 8 | 8 | 8 | 62,50% | 2,98 | 0,80R | €63,91 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | 9 | 9 | 9 | 55,56% | 2,27 | 0,60R | €53,74 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | 3 | 6 | 6 | 50,00% | 1,77 | 0,42R | €24,99 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | 9 | 9 | 9 | 44,44% | 1,45 | 0,27R | €24,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | 10 | 12 | 12 | 41,67% | 1,32 | 0,20R | €23,60 |
| MAIN | 16 | 65 | 65 | 35,38% | 1,05 | 0,04R | €23,60 |
| RSI_EXTREME_LONG_15M | 0 | 10 | 10 | 30,00% | 0,31 | -0,54R | €-54,33 |
| RSI_EXTREME_SHORT_15M | 0 | 12 | 12 | 33,33% | 0,40 | -0,41R | €-49,15 |
| Bilanciata 1H V1 | 19 | 176 | 176 | 34,09% | 1,00 | 0,00R | €4,61 |
| Bilanciata 1H V2 | 11 | 54 | 47 | 40,74% | 1,35 | 0,20R | €110,15 |
| Bilanciata 1H V3 Filtered | 16 | 79 | 79 | 36,71% | 1,13 | 0,08R | €66,02 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | 11 | 4 | 4 | 25,00% | 0,62 | -0,30R | €-12,02 |
| Rapida 1H V1 | 4 | 204 | 204 | 39,22% | 0,92 | -0,05R | €-103,35 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | 6 | 20 | 20 | 50,00% | 1,52 | 0,25R | €49,91 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | 10 | 18 | 18 | 55,56% | 1,71 | 0,33R | €59,83 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | 13 | 82 | 82 | 46,34% | 1,18 | 0,10R | €82,02 |
| SHADOW_1H_FAST_NO_PEPE_V1 | 12 | 85 | 85 | 42,35% | 1,00 | 0,00R | €1,38 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | 10 | 60 | 60 | 46,67% | 1,17 | 0,10R | €57,62 |
| SHADOW_1H_FAST_TP2_V1 | 14 | 78 | 78 | 34,62% | 0,95 | -0,03R | €-26,37 |
| Rapida 1H V2 | 3 | 14 | 13 | 35,71% | 0,70 | -0,21R | €-29,31 |
| Rapida 1H V3 Filtered | 13 | 126 | 126 | 44,44% | 1,10 | 0,06R | €74,60 |
| SHADOW_1H_FAST_V3_CAP75_V1 | 13 | 70 | 70 | 44,29% | 1,06 | 0,04R | €26,32 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | 8 | 38 | 38 | 42,11% | 1,00 | 0,00R | €0,28 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | 8 | 38 | 38 | 42,11% | 1,00 | 0,00R | €0,28 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | 8 | 47 | 47 | 42,55% | 1,02 | 0,01R | €5,95 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | 13 | 81 | 81 | 44,44% | 1,07 | 0,04R | €33,76 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | 12 | 80 | 80 | 42,50% | 0,98 | -0,01R | €-7,49 |
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
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | 3 | 6 | 6 | 16,67% | 0,37 | -0,55R | €-33,24 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | 3 | 6 | 6 | 16,67% | 0,37 | -0,55R | €-33,24 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | 8 | 18 | 18 | 38,89% | 1,20 | 0,13R | €22,96 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | 6 | 30 | 30 | 16,67% | 0,36 | -0,57R | €-170,29 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | 7 | 40 | 40 | 17,50% | 0,58 | -0,37R | €-147,89 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | 7 | 40 | 40 | 17,50% | 0,58 | -0,37R | €-147,89 |
| SHADOW_COMBO_MEAN_REVERSION | 2 | 18 | 18 | 44,44% | 1,12 | 0,07R | €12,92 |
| SHADOW_COMBO_SCANNER | 12 | 73 | 73 | 42,47% | 1,52 | 0,30R | €222,21 |
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
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | 14 | 31 | 31 | 32,26% | 0,89 | -0,07R | €-23,16 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | 14 | 31 | 31 | 29,03% | 0,77 | -0,17R | €-52,37 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | 13 | 29 | 29 | 31,03% | 0,85 | -0,11R | €-31,62 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | 14 | 24 | 24 | 20,83% | 0,75 | -0,21R | €-50,44 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | 10 | 27 | 27 | 29,63% | 0,80 | -0,15R | €-40,13 |
| SHADOW_MASTER_ADAPTIVE_V1 | 14 | 31 | 31 | 29,03% | 0,77 | -0,17R | €-52,37 |
| Forza relativa 1H V1 | 19 | 127 | 127 | 31,50% | 1,00 | -0,00R | €-0,92 |
| Forza relativa 1H V2 | 9 | 51 | 46 | 41,18% | 1,47 | 0,28R | €144,68 |
| SHADOW_SCANNER_BOTTOM10_SHORT | 4 | 6 | 6 | 0,00% | 0,00 | -1,11R | €-66,45 |
| SHADOW_SCANNER_BOTTOM15_SHORT | 4 | 6 | 6 | 0,00% | 0,00 | -1,11R | €-66,45 |
| SHADOW_SCANNER_BOTTOM20_SHORT | 4 | 6 | 6 | 0,00% | 0,00 | -1,11R | €-66,45 |
| SHADOW_SCANNER_BOTTOM5_SHORT | 6 | 50 | 50 | 28,00% | 0,80 | -0,14R | €-67,84 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | 3 | 2 | 2 | 0,00% | 0,00 | -1,10R | €-22,10 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | 3 | 2 | 2 | 0,00% | 0,00 | -1,10R | €-22,10 |
| SHADOW_SCANNER_TOP10_LONG | 8 | 7 | 7 | 57,14% | 2,52 | 0,68R | €47,25 |
| SHADOW_SCANNER_TOP15_LONG | 9 | 7 | 7 | 57,14% | 2,52 | 0,68R | €47,25 |
| SHADOW_SCANNER_TOP20_LONG | 9 | 7 | 7 | 57,14% | 2,52 | 0,68R | €47,25 |
| SHADOW_SCANNER_TOP5_BTC | 12 | 71 | 71 | 40,85% | 1,50 | 0,29R | €209,30 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | 8 | 12 | 12 | 33,33% | 1,02 | 0,01R | €1,57 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | 12 | 29 | 29 | 34,48% | 1,10 | 0,07R | €19,44 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | 9 | 22 | 22 | 36,36% | 1,22 | 0,14R | €31,68 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | 9 | 22 | 22 | 36,36% | 1,22 | 0,14R | €31,68 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | 9 | 25 | 25 | 32,00% | 0,99 | -0,00R | €-0,90 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | 9 | 25 | 25 | 32,00% | 0,99 | -0,00R | €-0,90 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | 12 | 33 | 33 | 33,33% | 1,08 | 0,05R | €17,60 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | 13 | 24 | 24 | 29,17% | 1,16 | 0,12R | €28,74 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | 13 | 24 | 24 | 29,17% | 1,16 | 0,12R | €28,74 |
| SHADOW_SCANNER_TOP5_LONG | 11 | 85 | 85 | 41,18% | 1,38 | 0,22R | €190,97 |
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
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | ALT_ROTATION_UP | 4 | 8 | 8 | 37,50% | 1,08 | 0,06R | €4,44 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | RANGE | 3 | 2 | 2 | 50,00% | 1,88 | 0,46R | €9,28 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_UP_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | ALT_ROTATION_UP | 4 | 6 | 6 | 33,33% | 0,88 | -0,09R | €-5,30 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | RANGE | 2 | 2 | 2 | 50,00% | 1,88 | 0,46R | €9,28 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | TREND_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | ALT_ROTATION_UP | 4 | 6 | 6 | 33,33% | 0,88 | -0,09R | €-5,30 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | RANGE | 2 | 2 | 2 | 50,00% | 1,88 | 0,46R | €9,28 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | TREND_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | ALT_ROTATION_UP | 3 | 5 | 5 | 40,00% | 1,17 | 0,11R | €5,46 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | RANGE | 3 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,77 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | RANGE_LOW_VOL | 1 | 1 | 1 | 100,00% | ∞ | 1,96R | €19,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TREND_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | RANGE | 5 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | RANGE_LOW_VOL | 1 | 1 | 1 | 100,00% | ∞ | 1,96R | €19,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | ALT_ROTATION_UP | 3 | 7 | 7 | 42,86% | 1,36 | 0,22R | €15,20 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | RANGE | 3 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | RANGE_LOW_VOL | 1 | 1 | 1 | 100,00% | ∞ | 1,96R | €19,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | ALT_ROTATION_UP | 4 | 7 | 7 | 42,86% | 1,36 | 0,22R | €15,20 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | RANGE | 3 | 3 | 3 | 0,00% | 0,00 | -1,03R | €-30,94 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | RANGE_LOW_VOL | 1 | 2 | 2 | 100,00% | ∞ | 1,97R | €39,35 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | TREND_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | ALT_ROTATION_UP | 3 | 6 | 6 | 50,00% | 1,78 | 0,42R | €25,02 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | RANGE | 3 | 2 | 2 | 100,00% | ∞ | 1,94R | €38,89 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TREND_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | ALT_ROTATION_UP | 4 | 6 | 6 | 50,00% | 1,78 | 0,42R | €25,02 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | RANGE | 3 | 3 | 3 | 66,67% | 3,82 | 0,96R | €28,72 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | ALT_ROTATION_UP | 2 | 5 | 5 | 40,00% | 1,17 | 0,11R | €5,43 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | RANGE_LOW_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,96R | €19,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | TREND_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | ALT_ROTATION_UP | 4 | 5 | 5 | 40,00% | 1,17 | 0,11R | €5,46 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | RANGE | 3 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,81 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | RANGE_LOW_VOL | 1 | 2 | 2 | 100,00% | ∞ | 1,97R | €39,35 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | ALT_ROTATION_UP | 4 | 7 | 7 | 42,86% | 1,36 | 0,22R | €15,20 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | RANGE | 3 | 3 | 3 | 0,00% | 0,00 | -1,03R | €-30,94 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | RANGE_LOW_VOL | 1 | 2 | 2 | 100,00% | ∞ | 1,97R | €39,35 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_UP_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| MAIN | ALT_ROTATION_DOWN | 1 | 3 | 3 | 33,33% | 0,96 | -0,03R | €-0,88 |
| MAIN | ALT_ROTATION_UP | 4 | 8 | 8 | 0,00% | 0,00 | -1,02R | €-81,72 |
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
| RSI_EXTREME_SHORT_15M | ALT_ROTATION_UP | 0 | 4 | 4 | 25,00% | 0,05 | -0,86R | €-34,43 |
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
| Bilanciata 1H V2 | ALT_ROTATION_UP | 5 | 8 | 6 | 50,00% | 1,82 | 0,43R | €34,69 |
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
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | ALT_ROTATION_UP | 1 | 6 | 6 | 50,00% | 1,29 | 0,15R | €9,22 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | RANGE | 2 | 4 | 4 | 100,00% | ∞ | 1,49R | €59,40 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 1,48R | €29,69 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TREND_UP | 2 | 3 | 3 | 33,33% | 0,68 | -0,23R | €-7,03 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TREND_UP_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | ALT_ROTATION_UP | 3 | 12 | 12 | 50,00% | 1,34 | 0,18R | €21,56 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | RANGE | 3 | 2 | 2 | 50,00% | 1,41 | 0,21R | €4,28 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 100,00% | ∞ | 1,47R | €44,18 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | TREND_UP | 3 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | ALT_ROTATION_DOWN | 0 | 18 | 18 | 22,22% | 0,40 | -0,46R | €-82,22 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | ALT_ROTATION_UP | 3 | 13 | 13 | 53,85% | 1,56 | 0,27R | €35,45 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | RANGE | 6 | 29 | 29 | 62,07% | 2,15 | 0,47R | €137,32 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 100,00% | ∞ | 1,47R | €44,18 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 1,48R | €29,69 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TREND_UP | 3 | 16 | 16 | 25,00% | 0,44 | -0,45R | €-72,21 |
| SHADOW_1H_FAST_NO_PEPE_V1 | ALT_ROTATION_DOWN | 1 | 19 | 19 | 21,05% | 0,38 | -0,49R | €-92,40 |
| SHADOW_1H_FAST_NO_PEPE_V1 | ALT_ROTATION_UP | 2 | 13 | 13 | 46,15% | 1,11 | 0,07R | €8,60 |
| SHADOW_1H_FAST_NO_PEPE_V1 | RANGE | 4 | 32 | 32 | 56,25% | 1,71 | 0,33R | €106,55 |
| SHADOW_1H_FAST_NO_PEPE_V1 | RANGE_LOW_VOL | 1 | 2 | 2 | 100,00% | ∞ | 1,47R | €29,42 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TRANSITION | 0 | 3 | 3 | 100,00% | ∞ | 1,48R | €44,53 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_DOWN | 1 | 2 | 2 | 0,00% | 0,00 | -1,02R | €-20,41 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_UP | 2 | 14 | 14 | 21,43% | 0,36 | -0,54R | €-74,90 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_UP_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | ALT_ROTATION_DOWN | 0 | 12 | 12 | 33,33% | 0,65 | -0,25R | €-30,18 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | ALT_ROTATION_UP | 5 | 13 | 13 | 38,46% | 0,83 | -0,11R | €-14,38 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | RANGE | 4 | 23 | 23 | 65,22% | 2,50 | 0,56R | €128,99 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | RANGE_LOW_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,48R | €29,66 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_UP | 1 | 8 | 8 | 12,50% | 0,18 | -0,76R | €-61,17 |
| SHADOW_1H_FAST_TP2_V1 | ALT_ROTATION_DOWN | 1 | 19 | 19 | 15,79% | 0,36 | -0,54R | €-102,47 |
| SHADOW_1H_FAST_TP2_V1 | ALT_ROTATION_UP | 3 | 14 | 14 | 42,86% | 1,32 | 0,20R | €28,05 |
| SHADOW_1H_FAST_TP2_V1 | RANGE | 5 | 25 | 25 | 44,00% | 1,34 | 0,20R | €50,77 |
| SHADOW_1H_FAST_TP2_V1 | RANGE_LOW_VOL | 2 | 1 | 1 | 100,00% | ∞ | 1,95R | €19,52 |
| SHADOW_1H_FAST_TP2_V1 | TRANSITION | 0 | 3 | 3 | 100,00% | ∞ | 1,95R | €58,62 |
| SHADOW_1H_FAST_TP2_V1 | TREND_DOWN | 1 | 2 | 2 | 0,00% | 0,00 | -1,02R | €-20,41 |
| SHADOW_1H_FAST_TP2_V1 | TREND_UP | 0 | 14 | 14 | 21,43% | 0,49 | -0,43R | €-60,45 |
| SHADOW_1H_FAST_TP2_V1 | TREND_UP_HIGH_VOL | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| Rapida 1H V2 | ALT_ROTATION_UP | 1 | 3 | 3 | 33,33% | 0,62 | -0,28R | €-8,35 |
| Rapida 1H V2 | RANGE | 2 | 10 | 9 | 40,00% | 0,85 | -0,10R | €-9,53 |
| Rapida 1H V2 | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -1,14R | €-11,43 |
| Rapida 1H V3 Filtered | ALT_ROTATION_DOWN | 1 | 21 | 21 | 28,57% | 0,52 | -0,36R | €-75,39 |
| Rapida 1H V3 Filtered | ALT_ROTATION_UP | 3 | 13 | 13 | 53,85% | 1,54 | 0,27R | €34,87 |
| Rapida 1H V3 Filtered | RANGE | 5 | 31 | 31 | 58,06% | 1,84 | 0,38R | €118,61 |
| Rapida 1H V3 Filtered | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| Rapida 1H V3 Filtered | RANGE_LOW_VOL | 1 | 2 | 2 | 100,00% | ∞ | 1,47R | €29,42 |
| Rapida 1H V3 Filtered | TRANSITION | 0 | 7 | 7 | 57,14% | 1,83 | 0,38R | €26,94 |
| Rapida 1H V3 Filtered | TREND_DOWN | 1 | 2 | 2 | 0,00% | 0,00 | -1,02R | €-20,41 |
| Rapida 1H V3 Filtered | TREND_UP | 2 | 29 | 29 | 48,28% | 1,27 | 0,15R | €43,00 |
| Rapida 1H V3 Filtered | TREND_UP_HIGH_VOL | 0 | 20 | 20 | 25,00% | 0,49 | -0,36R | €-72,31 |
| SHADOW_1H_FAST_V3_CAP75_V1 | ALT_ROTATION_DOWN | 0 | 16 | 16 | 25,00% | 0,44 | -0,44R | €-70,78 |
| SHADOW_1H_FAST_V3_CAP75_V1 | ALT_ROTATION_UP | 4 | 14 | 14 | 42,86% | 0,99 | -0,01R | €-0,91 |
| SHADOW_1H_FAST_V3_CAP75_V1 | RANGE | 6 | 25 | 25 | 64,00% | 2,36 | 0,53R | €132,39 |
| SHADOW_1H_FAST_V3_CAP75_V1 | RANGE_LOW_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,48R | €29,66 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_UP | 2 | 11 | 11 | 18,18% | 0,29 | -0,62R | €-68,73 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | ALT_ROTATION_DOWN | 0 | 6 | 6 | 0,00% | 0,00 | -1,04R | €-62,18 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | ALT_ROTATION_UP | 3 | 10 | 10 | 40,00% | 0,89 | -0,07R | €-6,96 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | RANGE | 3 | 13 | 13 | 69,23% | 3,24 | 0,71R | €92,34 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TREND_UP | 2 | 7 | 7 | 14,29% | 0,20 | -0,75R | €-52,65 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | ALT_ROTATION_DOWN | 0 | 6 | 6 | 0,00% | 0,00 | -1,04R | €-62,18 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | ALT_ROTATION_UP | 3 | 10 | 10 | 40,00% | 0,89 | -0,07R | €-6,96 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | RANGE | 3 | 13 | 13 | 69,23% | 3,24 | 0,71R | €92,34 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TREND_UP | 2 | 7 | 7 | 14,29% | 0,20 | -0,75R | €-52,65 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 0 | 8 | 8 | 0,00% | 0,00 | -1,03R | €-82,50 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | ALT_ROTATION_UP | 3 | 11 | 11 | 45,45% | 1,07 | 0,04R | €4,64 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | RANGE | 3 | 17 | 17 | 64,71% | 2,66 | 0,60R | €101,26 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | RANGE_LOW_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,47R | €29,42 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 1,49R | €29,71 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,23 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_UP | 2 | 6 | 6 | 0,00% | 0,00 | -1,11R | €-66,36 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | ALT_ROTATION_DOWN | 1 | 20 | 20 | 30,00% | 0,56 | -0,32R | €-63,96 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | ALT_ROTATION_UP | 3 | 10 | 10 | 50,00% | 1,33 | 0,17R | €17,43 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | RANGE | 5 | 31 | 31 | 58,06% | 1,84 | 0,38R | €118,61 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | RANGE_LOW_VOL | 1 | 2 | 2 | 100,00% | ∞ | 1,47R | €29,42 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 1,49R | €29,71 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TREND_DOWN | 1 | 2 | 2 | 0,00% | 0,00 | -1,02R | €-20,41 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TREND_UP | 2 | 14 | 14 | 21,43% | 0,35 | -0,55R | €-77,05 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | ALT_ROTATION_DOWN | 1 | 20 | 20 | 30,00% | 0,56 | -0,32R | €-63,96 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | ALT_ROTATION_UP | 3 | 12 | 12 | 41,67% | 0,92 | -0,05R | €-6,25 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | RANGE | 4 | 30 | 30 | 56,67% | 1,74 | 0,35R | €103,74 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | RANGE_LOW_VOL | 1 | 2 | 2 | 100,00% | ∞ | 1,47R | €29,42 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 1,49R | €29,71 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_DOWN | 1 | 2 | 2 | 0,00% | 0,00 | -1,02R | €-20,41 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_UP | 2 | 12 | 12 | 16,67% | 0,26 | -0,66R | €-79,74 |
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
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TREND_UP | 3 | 3 | 3 | 0,00% | 0,00 | -1,05R | €-31,53 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TRANSITION | 0 | 3 | 3 | 33,33% | 0,92 | -0,06R | €-1,72 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TREND_UP | 3 | 3 | 3 | 0,00% | 0,00 | -1,05R | €-31,53 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | ALT_ROTATION_DOWN | 1 | 2 | 2 | 0,00% | 0,00 | -1,10R | €-21,95 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | ALT_ROTATION_UP | 2 | 1 | 1 | 0,00% | 0,00 | -1,03R | €-10,34 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | RANGE | 4 | 10 | 10 | 60,00% | 2,88 | 0,77R | €77,46 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TRANSITION | 0 | 2 | 2 | 50,00% | 1,90 | 0,46R | €9,15 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,18 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TRANSITION | 0 | 8 | 8 | 25,00% | 0,60 | -0,32R | €-25,89 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TREND_UP | 6 | 14 | 14 | 14,29% | 0,30 | -0,63R | €-88,54 |
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
| SHADOW_COMBO_SCANNER | TREND_UP | 3 | 20 | 20 | 50,00% | 2,04 | 0,55R | €110,63 |
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
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TREND_UP | 4 | 8 | 8 | 12,50% | 0,26 | -0,70R | €-55,77 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | ALT_ROTATION_DOWN | 1 | 6 | 6 | 16,67% | 0,39 | -0,51R | €-30,82 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | ALT_ROTATION_UP | 2 | 4 | 4 | 25,00% | 0,60 | -0,31R | €-12,57 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | RANGE | 5 | 9 | 9 | 55,56% | 2,44 | 0,65R | €58,35 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TREND_UP | 4 | 10 | 10 | 10,00% | 0,21 | -0,77R | €-77,01 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | ALT_ROTATION_DOWN | 1 | 6 | 6 | 16,67% | 0,39 | -0,51R | €-30,82 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | RANGE | 5 | 9 | 9 | 55,56% | 2,44 | 0,65R | €58,35 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | RANGE_LOW_VOL | 1 | 1 | 1 | 100,00% | ∞ | 1,89R | €18,89 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TREND_UP | 5 | 11 | 11 | 9,09% | 0,18 | -0,80R | €-87,73 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_DOWN | 1 | 1 | 1 | 100,00% | ∞ | 2,99R | €29,87 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_UP | 3 | 3 | 3 | 0,00% | 0,00 | -1,05R | €-31,46 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | RANGE | 5 | 9 | 9 | 33,33% | 1,47 | 0,31R | €28,35 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | TREND_UP | 3 | 10 | 10 | 10,00% | 0,31 | -0,67R | €-67,01 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | ALT_ROTATION_DOWN | 0 | 4 | 4 | 0,00% | 0,00 | -1,01R | €-40,55 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | RANGE | 4 | 12 | 12 | 58,33% | 2,73 | 0,73R | €87,99 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TREND_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TREND_UP | 4 | 10 | 10 | 0,00% | 0,00 | -1,07R | €-107,43 |
| SHADOW_MASTER_ADAPTIVE_V1 | ALT_ROTATION_DOWN | 1 | 6 | 6 | 16,67% | 0,39 | -0,51R | €-30,82 |
| SHADOW_MASTER_ADAPTIVE_V1 | ALT_ROTATION_UP | 2 | 4 | 4 | 25,00% | 0,60 | -0,31R | €-12,57 |
| SHADOW_MASTER_ADAPTIVE_V1 | RANGE | 5 | 9 | 9 | 55,56% | 2,44 | 0,65R | €58,35 |
| SHADOW_MASTER_ADAPTIVE_V1 | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_MASTER_ADAPTIVE_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| SHADOW_MASTER_ADAPTIVE_V1 | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_MASTER_ADAPTIVE_V1 | TREND_UP | 4 | 10 | 10 | 10,00% | 0,21 | -0,77R | €-77,01 |
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
| Forza relativa 1H V2 | ALT_ROTATION_UP | 3 | 6 | 5 | 33,33% | 1,02 | 0,02R | €0,99 |
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
| SHADOW_SCANNER_TOP5_BTC | TREND_UP | 3 | 19 | 19 | 47,37% | 1,85 | 0,47R | €89,92 |
| SHADOW_SCANNER_TOP5_BTC | TREND_UP_HIGH_VOL | 0 | 9 | 9 | 33,33% | 1,18 | 0,11R | €9,88 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | ALT_ROTATION_DOWN | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | ALT_ROTATION_UP | 3 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,86 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TRANSITION | 0 | 3 | 3 | 66,67% | 4,32 | 1,12R | €33,60 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TREND_UP | 3 | 2 | 2 | 50,00% | 1,97 | 0,54R | €10,76 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TREND_UP_HIGH_VOL | 0 | 6 | 6 | 16,67% | 0,40 | -0,53R | €-31,93 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | ALT_ROTATION_DOWN | 2 | 4 | 4 | 0,00% | 0,00 | -1,01R | €-40,55 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | ALT_ROTATION_UP | 2 | 4 | 4 | 25,00% | 0,67 | -0,27R | €-10,61 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | RANGE | 4 | 10 | 10 | 50,00% | 2,15 | 0,58R | €58,21 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 2,19R | €43,73 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_UP | 2 | 2 | 2 | 50,00% | 1,97 | 0,54R | €10,76 |
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
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_UP | 3 | 2 | 2 | 50,00% | 1,97 | 0,54R | €10,76 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 9 | 9 | 22,22% | 0,65 | -0,25R | €-22,73 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | ALT_ROTATION_UP | 3 | 7 | 7 | 28,57% | 1,09 | 0,07R | €4,67 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | RANGE | 4 | 8 | 8 | 37,50% | 1,76 | 0,48R | €38,46 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 2,99R | €29,87 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_UP | 3 | 4 | 4 | 25,00% | 0,92 | -0,07R | €-2,70 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -1,05R | €-31,38 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | ALT_ROTATION_UP | 3 | 7 | 7 | 28,57% | 1,09 | 0,07R | €4,67 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | RANGE | 4 | 8 | 8 | 37,50% | 1,76 | 0,48R | €38,46 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 2,99R | €29,87 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_UP | 3 | 4 | 4 | 25,00% | 0,92 | -0,07R | €-2,70 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -1,05R | €-31,38 |
| SHADOW_SCANNER_TOP5_LONG | ALT_ROTATION_DOWN | 1 | 6 | 6 | 0,00% | 0,00 | -1,05R | €-62,77 |
| SHADOW_SCANNER_TOP5_LONG | ALT_ROTATION_UP | 2 | 9 | 9 | 33,33% | 0,92 | -0,06R | €-5,06 |
| SHADOW_SCANNER_TOP5_LONG | RANGE | 4 | 16 | 16 | 56,25% | 2,87 | 0,72R | €115,32 |
| SHADOW_SCANNER_TOP5_LONG | RANGE_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,83 |
| SHADOW_SCANNER_TOP5_LONG | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_LONG | TRANSITION | 0 | 13 | 13 | 46,15% | 1,63 | 0,35R | €46,04 |
| SHADOW_SCANNER_TOP5_LONG | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_SCANNER_TOP5_LONG | TREND_UP | 2 | 29 | 29 | 48,28% | 1,84 | 0,43R | €125,07 |
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

Generato: 2026-07-27T04:23:47+00:00

> Motore esclusivamente osservativo e Paper-only. Non modifica le uscite reali. I confronti escludono il funding sia dall'uscita originale sia dalle varianti.

## Stato operativo

- Gruppi di trade ancora monitorati: **840**
- Scenari virtuali ancora attivi: **14138**
- Gruppi in attesa dell'uscita originale: **425**
- Gruppi con originale chiuso ma Shadow ancora attive: **415**
- Confronti completati: **49886**

## Classifica osservativa complessiva

| Scenario | Campione completo | Campione totale | Δ medio vs originale | Migliora | Troppo presto | Troppo tardi | Stato dati |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| GB20_R050 | 1757 | 1822 | +€6,94 | 49,0% | 536 | 2 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R050 | 1757 | 1822 | +€5,35 | 46,8% | 553 | 16 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R050 | 1757 | 1822 | +€3,35 | 45,4% | 562 | 38 | READY_FOR_BLOCK4_EVALUATION |
| TP_R050 | 1757 | 1822 | +€2,87 | 44,7% | 619 | 1 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R050 | 1756 | 1821 | +€2,14 | 44,9% | 524 | 87 | READY_FOR_BLOCK4_EVALUATION |
| TIME_6H | 1756 | 1821 | €-0,40 | 45,1% | 392 | 305 | READY_FOR_BLOCK4_EVALUATION |
| TIME_12H | 1741 | 1806 | +€1,19 | 40,5% | 195 | 462 | READY_FOR_BLOCK4_EVALUATION |
| GB20_R100 | 1724 | 1789 | +€8,07 | 45,2% | 430 | 33 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R100 | 1724 | 1789 | +€6,27 | 44,4% | 418 | 59 | READY_FOR_BLOCK4_EVALUATION |
| TP_R100 | 1724 | 1789 | +€6,12 | 42,0% | 489 | 31 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R100 | 1723 | 1788 | +€5,18 | 44,4% | 343 | 119 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R100 | 1717 | 1782 | +€3,98 | 41,6% | 279 | 237 | READY_FOR_BLOCK4_EVALUATION |
| ATR15_R100 | 1692 | 1757 | +€0,29 | 33,5% | 192 | 397 | READY_FOR_BLOCK4_EVALUATION |
| TP_R150 | 1656 | 1721 | +€6,43 | 31,3% | 232 | 183 | READY_FOR_BLOCK4_EVALUATION |
| ATR20_R100 | 1654 | 1719 | €-3,49 | 28,7% | 164 | 472 | READY_FOR_BLOCK4_EVALUATION |
| TIME_24H | 1635 | 1700 | €-1,77 | 35,5% | 90 | 506 | READY_FOR_BLOCK4_EVALUATION |
| ATR30_R100 | 1627 | 1692 | €-7,75 | 26,7% | 118 | 510 | READY_FOR_BLOCK4_EVALUATION |
| BE_R050 | 1617 | 1682 | €-10,25 | 28,4% | 329 | 349 | READY_FOR_BLOCK4_EVALUATION |
| TP_R200 | 1585 | 1650 | +€6,57 | 37,6% | 102 | 278 | READY_FOR_BLOCK4_EVALUATION |
| BE_R100 | 1497 | 1562 | €-14,35 | 21,1% | 117 | 499 | READY_FOR_BLOCK4_EVALUATION |

## Come leggere il controllo

- **EARLIER_BETTER**: la variante è uscita prima e ha conservato più profitto.
- **TOO_EARLY**: la variante è uscita prima ma ha tagliato un movimento migliore.
- **LATER_BETTER**: la variante ha continuato dopo l'uscita originale e ha guadagnato di più.
- **TOO_LATE**: la variante è rimasta aperta più a lungo e ha peggiorato il risultato.

## Limiti e protezioni

Le regole Shadow mantengono entrata, quantità, commissioni, stop protettivo iniziale e liquidazione. Le ambiguità all'interno della stessa candela vengono risolte scegliendo l'esito peggiore. Le posizioni già aperte al momento dell'installazione sono marcate come campione parziale e non saranno utilizzate dal futuro Blocco 4 come prova piena.

# Blocco 4 — Valutazione statistica Shadow

Generato: 2026-07-27T04:23:51+00:00

> Modulo esclusivamente valutativo. Non modifica strategie, uscite, posizioni o capitale. Le candidature vengono consegnate al futuro Blocco 5, senza applicazione automatica.

## Stato

- Risultati Block 3 disponibili: **49886**
- Valutazioni prodotte: **15502**
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

Generato: 2026-07-27T04:24:27+00:00

Questi profili sono osservativi e Paper-only. Usano gli stessi trade della madre, ma applicano una specifica uscita Block 3 soltanto ai segnali aperti dopo la loro registrazione.
Nessuna promozione, modifica live o operazione reale viene eseguita automaticamente.

| Challenger | Madre | Scenario | Chiusi | Copertura | PF | PnL | Exp/trade | DD | Stato |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Rapida 1H V1 — giveback 20% dopo +0,5R | SHADOW_1H_FAST | GB20_R050 | 20 | 100,00% | 1,28 | +€103,11 | +€5,16 | 1,41% | COLLECTING |
| Rapida 1H V1 — giveback 30% dopo +0,5R | SHADOW_1H_FAST | GB30_R050 | 20 | 100,00% | 1,11 | +€40,98 | +€2,05 | 1,48% | COLLECTING |
| Relative Strength — giveback 20% dopo +0,5R | SHADOW_RELATIVE_STRENGTH | GB20_R050 | 6 | 100,00% | 1,40 | +€38,72 | +€6,45 | 0,54% | COLLECTING |
| Relative Strength — giveback 30% dopo +0,5R | SHADOW_RELATIVE_STRENGTH | GB30_R050 | 6 | 100,00% | 1,21 | +€20,61 | +€3,43 | 0,54% | COLLECTING |
| Scanner Top 5 BTC Strength — giveback 20% dopo +1,4R | SHADOW_SCANNER_TOP5_BTC | GB20_R140 | 1 | 100,00% | 0,00 | €-50,14 | €-50,14 | 0,50% | COLLECTING |
| Master Adaptive Consensus — breakeven dopo +0,2R | SHADOW_MASTER_ADAPTIVE_V1 | BE_A020 | 1 | 100,00% | 0,00 | €-46,66 | €-46,66 | 0,47% | COLLECTING |
| Momentum Breakout V3 Filtered — giveback 20% dopo +1,0R | SHADOW_1H_FAST_V3 | GB20_R100 | 1 | 100,00% | 0,00 | €-0,47 | €-0,47 | 0,00% | COLLECTING |
| Momentum Breakout — giveback 20% dopo +1,4R | SHADOW_1H_FAST | GB20_R140 | 0 | 0,00% | 0,00 | €0,00 | €0,00 | 0,00% | COLLECTING |

## Regole di valutazione

- Prima fotografia a 30 trade indipendenti.
- Revisione per possibile promozione a 50 trade indipendenti.
- PF minimo 1,50, expectancy e PnL positivi, drawdown massimo 15%, copertura minima 90%.
- PF deve superare la madre e il drawdown non deve essere peggiore sulla stessa serie di trade.
- La promozione resta una decisione umana protetta; il rollback viene predisposto soltanto in fase di approvazione.

# Blocco 4.5 — Crash Cascade Guard

Generato: 2026-07-27T04:23:38+00:00

> Paper-only. In mercato NORMAL/WATCH non riduce i segnali. Le limitazioni iniziano soltanto in STRESS, RECOVERY, CRASH, EXTREME o con dati non affidabili.

## Stato corrente

- Livello: **NORMAL**
- Direzione: **NONE**
- Segnali bloccati nel ciclo: **0**
- Simulazioni bloccate attive: **63**
- Simulazioni completate nel ciclo: **0**
- Liquidazioni virtuali evitate totali: **0**
- Valore cumulato del filtro: **44.54 R**
- Profitto virtuale mancato: **163.76 R**

## Stress test portafogli Paper

| Scenario | Posizioni interessate | Liquidazioni stimate | Perdita stimata EUR |
| --- | ---: | ---: | ---: |
| DOWN_10 | 328 | 0 | 37178.29 |
| DOWN_20 | 328 | 0 | 74356.58 |
| DOWN_30 | 328 | 0 | 111534.87 |
| DOWN_40 | 328 | 154 | 135991.10 |
| UP_10 | 98 | 0 | 13648.17 |
| UP_20 | 98 | 0 | 27296.33 |
| UP_30 | 98 | 0 | 40944.50 |
| UP_40 | 98 | 47 | 49314.05 |

## Modello di esecuzione

Se una candela di cascata attraversa nello stesso intervallo sia lo stop sia il prezzo di liquidazione, il Paper usa il caso peggiore e registra una liquidazione intrabar. Gli stop in gap o in regime di stress ricevono slippage aggiuntivo.

## Requisiti prima del live futures

- modalità ISOLATED obbligatoria;
- stop nativo sull'exchange;
- conferma dello stop prima di accettare la posizione;
- cross margin vietato.

# Blocco 5 — Candidati evolutivi controllati

Generato: 2026-07-27T04:23:13+00:00

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

Generato: 2026-07-27T04:24:28+00:00

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

Generato: 2026-07-27T04:24:28+00:00

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

Generato: 2026-07-27T04:24:28+00:00

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

Generato: 2026-07-27T04:24:28+00:00

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
| 1 | SHADOW_SCANNER_TOP5_LONG | BASELINE | 17.6 | E | 37 | 1.70 | 0.305 | 5.96 |
| 2 | SHADOW_1H_BALANCED_V3 | BASELINE | 16.7 | E | 46 | 1.54 | 0.231 | 3.23 |
| 3 | SHADOW_1H_FAST_V3_CAP75_V1 | BASELINE | 16.0 | E | 45 | 1.47 | 0.179 | 3.68 |
| 4 | SHADOW_1H_FAST_NOHIGH_CAP75_V1 | BASELINE | 15.8 | E | 52 | 1.43 | 0.177 | 5.40 |
| 5 | SHADOW_1H_FAST_SCORE_6_75_V1 | BASELINE | 14.9 | E | 49 | 1.37 | 0.138 | 3.71 |
| 6 | SHADOW_1H_FAST_V3 | BASELINE | 14.7 | E | 75 | 1.21 | 0.086 | 5.36 |
| 7 | SHADOW_1H_FAST_NO_PEPE_V1 | BASELINE | 12.6 | E | 43 | 1.22 | 0.094 | 3.55 |
| 8 | SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | BASELINE | 11.2 | E | 49 | 1.11 | 0.050 | 4.74 |
| 9 | SHADOW_1H_BALANCED | BASELINE | 11.0 | E | 48 | 1.43 | 0.172 | 4.17 |
| 10 | SHADOW_1H_FAST_V3_NOHIGH_V1 | BASELINE | 10.9 | E | 50 | 1.08 | 0.037 | 5.53 |

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

Generato: 2026-07-27T04:24:28+00:00

> Paper-only e advisory. Il blocco misura quali strategie funzionano nei diversi regimi, ma non cambia automaticamente strategia o posizione.

## Stato

- Regime corrente: **RANGE**
- Righe di performance: **489**
- Strategie preferite nel regime corrente: **4**
- Strategie da evitare nel regime corrente: **2**
- Memorie contestuali: **234**
- Routing automatico: **NO**

## Classifica del regime corrente

| Rank | Portafoglio | Famiglia | Stato | Fitness | Trade | PF | Expectancy R | DD R |
| ---: | --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| 1 | EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | momentum_breakout_v3_filtered | INSUFFICIENT | 81.7 | 8 | 5.66 | 0.606 | 1.03 |
| 2 | SHADOW_BTC_BOLLINGER_1H | shadow-btc-bollinger-1h | INSUFFICIENT | 81.2 | 3 | 99.00 | 1.115 | 0.00 |
| 3 | SHADOW_SOL_BOLLINGER_4H | shadow-sol-bollinger-4h | INSUFFICIENT | 80.4 | 1 | 99.00 | 1.740 | 0.00 |
| 4 | SHADOW_BTC_BOLLINGER_4H | shadow-btc-bollinger-4h | INSUFFICIENT | 80.4 | 1 | 99.00 | 1.682 | 0.00 |
| 5 | SHADOW_DOGE_DONCHIAN_1H | shadow-doge-donchian-1h | INSUFFICIENT | 80.1 | 3 | 99.00 | 0.374 | 0.00 |
| 6 | SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V1 | shadow-1h-fast-v3-nohigh-range-only-v1 | INSUFFICIENT | 79.5 | 9 | 2.39 | 0.493 | 2.17 |
| 7 | SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_V1 | shadow-1h-fast-v3-nohigh-regime-guard-v1 | OBSERVING | 79.2 | 13 | 2.88 | 0.600 | 2.17 |
| 8 | SHADOW_1H_FAST_SCORE_6_75_NO_TREND_UP_V1 | shadow-1h-fast-score-6-75-no-trend-up-v1 | OBSERVING | 77.4 | 13 | 2.24 | 0.454 | 2.11 |
| 9 | SHADOW_COMBO_ADAPTIVE_SIDE_REGIME_GUARD_V1 | shadow-combo-adaptive-side-regime-guard-v1 | INSUFFICIENT | 77.0 | 9 | 3.41 | 0.567 | 1.09 |
| 10 | SHADOW_ETH_BOLLINGER_1H | shadow-eth-bollinger-1h | INSUFFICIENT | 76.6 | 1 | 99.00 | 0.309 | 0.00 |

## Sicurezza

- Il regime viene assegnato usando solo l'ultimo record noto prima dell'entrata del trade.
- Nessun uso di dati futuri per classificare il trade.
- Il Candidate Regime Gate è advisory per impostazione predefinita.
- Nessun cambio automatico di MASTER, posizione o live.

# Blocco 11 — Collegamento protetto al live

Generato: 2026-07-27T04:24:28+00:00

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

Generato: 2026-07-27T04:23:38+00:00

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
