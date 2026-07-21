# Paper trading automatico KuCoin

Generato: 2026-07-21T12:08:44+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-07-21T12:08:25+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-07-21T12:08:25+00:00 | 2026-07-21T12:08:25+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-07-21T11:45:00+00:00 | 2026-07-21T11:45:00+00:00 | 8,5 min | 25,0 min | OK |
| 60m | 12 | 2026-07-21T11:00:00+00:00 | 2026-07-21T11:00:00+00:00 | 8,5 min | 45,0 min | OK |
| 240m | 12 | 2026-07-21T08:00:00+00:00 | 2026-07-21T08:00:00+00:00 | 8,5 min | 1,00 h | OK |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | NIGHT | 240m | SHORT | -6,75 | 6,00 | 0,00 | RISK_GATE | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro rischio/esecuzione: numero massimo posizioni. |
| Principale 4H | PEPE | 240m | LONG | 6,52 | 6,00 | 0,00 | RISK_GATE | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro rischio/esecuzione: numero massimo posizioni. |
| Principale 4H | BTC | 240m | LONG | 6,25 | 6,00 | 0,00 | RISK_GATE | 8,5 min | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Filtro rischio/esecuzione: numero massimo posizioni. |
| Principale 4H | ADA | 240m | LONG | 5,32 | 6,00 | 0,68 | BELOW_SCORE | 8,5 min | D: n/a | W: n/a | peso 0 | Punteggio +5.32; soglia ±6.00; mancano 0.68 punti. |
| Principale 4H | ETH | 240m | LONG | 5,20 | 6,00 | 0,80 | BELOW_SCORE | 8,5 min | D: n/a | W: n/a | peso 0 | Punteggio +5.20; soglia ±6.00; mancano 0.80 punti. |
| Rapida 1H V3 Filtered — madre | NIGHT | 60m | SHORT | -6,25 | 4,50 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Top 5 + BTC — 75% a 2,2R + runner 3R | XRP | 60m | LONG | 5,90 | 5,00 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Top 5 + BTC — target pieno 3R | XRP | 60m | LONG | 5,90 | 5,00 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Bilanciata 1H V2 | NIGHT | 60m | SHORT | -6,25 | 5,50 | 0,00 | STRATEGY_FILTER | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro V2 non superato: regime, EMA, ritorni e RSI; per Rapida V2 servono anche breakout reale, volume e ADX. |
| Rapida 1H V2 | NIGHT | 60m | SHORT | -6,25 | 5,00 | 0,00 | STRATEGY_FILTER | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro V2 non superato: regime, EMA, ritorni e RSI; per Rapida V2 servono anche breakout reale, volume e ADX. |
| Bilanciata 1H V2 | XRP | 60m | LONG | 5,90 | 5,50 | 0,00 | STRATEGY_FILTER | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro V2 non superato: regime, EMA, ritorni e RSI; per Rapida V2 servono anche breakout reale, volume e ADX. |
| Rapida 1H V1 — madre | XRP | 60m | LONG | 5,90 | 4,50 | 0,00 | STRATEGY_FILTER | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout UP oppure movimento breve ≥1,5%; breakout=NONE, movimento=+0.46%. |
| Rapida V1 — no HIGH + score <7,5 | XRP | 60m | LONG | 5,90 | 4,50 | 0,00 | STRATEGY_FILTER | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout UP oppure movimento breve ≥1,5%; breakout=NONE, movimento=+0.46%. |
| Rapida V1 — Long + BTC 1–3 + score <7,5 | XRP | 60m | LONG | 5,90 | 4,50 | 0,00 | STRATEGY_FILTER | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout UP oppure movimento breve ≥1,5%; breakout=NONE, movimento=+0.46%. |
| Rapida V1 — senza PEPE | XRP | 60m | LONG | 5,90 | 4,50 | 0,00 | STRATEGY_FILTER | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout UP oppure movimento breve ≥1,5%; breakout=NONE, movimento=+0.46%. |
| Rapida V1 — target pieno 2R | XRP | 60m | LONG | 5,90 | 4,50 | 0,00 | STRATEGY_FILTER | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout UP oppure movimento breve ≥1,5%; breakout=NONE, movimento=+0.46%. |
| Rapida 1H V2 | XRP | 60m | LONG | 5,90 | 5,00 | 0,00 | STRATEGY_FILTER | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro V2 non superato: regime, EMA, ritorni e RSI; per Rapida V2 servono anche breakout reale, volume e ADX. |
| Forza relativa 1H V1 | XRP | 60m | LONG | 5,90 | 4,00 | 0,00 | STRATEGY_FILTER | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro forza relativa: serve almeno ±2,0% contro BTC; valore=+0.73%. |
| Bilanciata 1H V2 | ETH | 60m | LONG | 5,87 | 5,50 | 0,00 | STRATEGY_FILTER | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro V2 non superato: regime, EMA, ritorni e RSI; per Rapida V2 servono anche breakout reale, volume e ADX. |
| Rapida 1H V1 — madre | ETH | 60m | LONG | 5,87 | 4,50 | 0,00 | STRATEGY_FILTER | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout UP oppure movimento breve ≥1,5%; breakout=NONE, movimento=+0.26%. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.860,68 | -1,39% | €-139,32 | €3.000,00 | -4,64% | 4 | 16 | 31,25% | 0,81 | 4,26% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 16 | 251 | CAMPIONE INSUFFICIENTE | 30 (mancano 14) |

- Trade del Principale 4H chiusi: **16**; win rate **31,25%**; profit factor **0,81**.
- Expectancy: **€-6,29** per trade; P&L netto: **€-100,68**; max drawdown: **4,26%**.
- Valutazione: **Servono altri eventi indipendenti prima di trarre conclusioni.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 4 | €9.860,68 | €1.552,19 | €4.656,58 | €197,65 | €-37,64 |
| TEST | Scanner Top 5 Long 1H | 3 | €10.487,42 | €3.540,41 | €7.080,81 | €104,19 | €63,91 |
| TEST | Scanner Top 5 + forza BTC 1H | 3 | €10.464,71 | €3.363,52 | €6.727,04 | €103,50 | €82,60 |
| TEST | Bilanciata 1H V3 Filtered | 4 | €10.270,74 | €3.152,26 | €9.456,78 | €51,19 | €157,00 |
| TEST | Combo Adaptive — madre | 3 | €10.246,76 | €2.743,84 | €5.487,67 | €153,54 | €4,33 |
| TEST | Combo Mean Reversion | 0 | €10.195,13 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Forza relativa 1H V2 | 4 | €10.171,52 | €2.419,26 | €4.838,52 | €151,48 | €10,25 |
| TEST | Benchmark Bollinger mean reversion 1H | 1 | €10.155,80 | €1.300,59 | €2.601,19 | €50,76 | €5,26 |
| TEST | Benchmark Donchian breakout 1H | 2 | €10.149,87 | €2.352,79 | €4.705,59 | €101,96 | €-4,72 |
| TEST | Bilanciata 1H V1 | 4 | €10.144,01 | €2.802,69 | €8.408,06 | €151,29 | €67,65 |
| TEST | Top 5 + BTC — 75% a 2,2R + runner 3R | 3 | €10.121,08 | €4.507,39 | €9.014,78 | €100,62 | €67,68 |
| TEST | Top 5 + BTC — target pieno 3R | 3 | €10.121,08 | €4.507,39 | €9.014,78 | €100,62 | €67,68 |
| TEST | Ampia 4H | 4 | €10.109,01 | €2.235,83 | €4.471,66 | €201,27 | €21,80 |
| TEST | Forza relativa 1H V1 | 4 | €10.097,38 | €2.508,00 | €5.016,01 | €151,36 | €4,27 |
| TEST | Top 5 + BTC — BTC≤3 | 2 | €10.088,98 | €2.798,33 | €5.596,65 | €99,98 | €33,81 |
| TEST | Top 5 + BTC — BTC 2–3 | 2 | €10.088,98 | €2.798,33 | €5.596,65 | €99,98 | €33,81 |
| TEST | Btc Bollinger 1H | 0 | €10.068,69 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Trend | 3 | €10.059,42 | €1.639,93 | €3.279,86 | €150,82 | €3,83 |
| TEST | Top 5 + BTC — solo MFE | 3 | €10.050,88 | €4.191,32 | €8.382,63 | €100,30 | €18,28 |
| TEST | Btc Ema 4H | 1 | €10.030,44 | €1.105,63 | €2.211,26 | €50,00 | €30,72 |
| TEST | Btc Donchian 4H | 1 | €10.030,44 | €1.105,63 | €2.211,26 | €50,00 | €30,72 |
| TEST | Sol Donchian 1H | 1 | €10.026,97 | €1.127,14 | €3.381,43 | €0,00 | €33,63 |
| TEST | Sol Ema 1H | 1 | €10.018,78 | €1.001,44 | €3.004,32 | €49,95 | €29,88 |
| TEST | Rapida V3 — Long Only | 2 | €10.016,46 | €2.975,30 | €8.925,90 | €50,00 | €26,03 |
| TEST | Eth Bollinger 1H | 0 | €10.015,45 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 1H | 1 | €10.009,47 | €1.000,51 | €3.001,52 | €49,91 | €29,85 |
| TEST | Combo Adaptive — Long Only | 2 | €10.005,63 | €2.785,91 | €5.571,82 | €100,29 | €-20,90 |
| TEST | Rapida 1H V2 | 0 | €10.004,31 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — 75% a 2R + runner 3R | 3 | €10.004,19 | €3.003,74 | €6.007,47 | €100,02 | €63,16 |
| TEST | Combo Adaptive — target pieno 3R | 3 | €10.004,19 | €3.003,74 | €6.007,47 | €100,02 | €63,16 |
| TEST | Btc Adaptive 4H | 1 | €10.003,41 | €1.047,40 | €2.094,81 | €50,00 | €4,67 |
| TEST | Sol Bollinger 4H | 1 | €10.001,88 | €968,56 | €1.937,11 | €50,00 | €3,04 |
| TEST | Rapida V1 — Long + BTC 1–3 + score <7,5 | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €10 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €10 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €10 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €50 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €50 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €50 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · prudente · 5x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · prudente · 5x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €10 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €10 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €50 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €50 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · prudente · 5x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · prudente · 5x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 4H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Bollinger 1H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Ema 4H | 1 | €9.999,14 | €883,93 | €1.767,86 | €50,00 | €0,20 |
| TEST | Sol Adaptive 4H | 1 | €9.995,85 | €807,13 | €1.614,26 | €50,00 | €-3,18 |
| TEST | Sol Ema 4H | 1 | €9.995,47 | €880,51 | €1.761,01 | €50,00 | €-3,47 |
| TEST | Sol Donchian 4H | 1 | €9.995,47 | €880,51 | €1.761,01 | €50,00 | €-3,47 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 0 | €9.995,13 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — Quality7 | 1 | €9.993,55 | €1.067,59 | €2.135,18 | €50,00 | €-5,17 |
| TEST | Combo Adaptive — Quality7 + Regime | 1 | €9.993,55 | €1.067,59 | €2.135,18 | €50,00 | €-5,17 |
| TEST | Combo Adaptive — Quality7 + Regime + parziale 1R | 1 | €9.993,55 | €1.067,59 | €2.135,18 | €50,00 | €-5,17 |
| TEST | Btc Adaptive 1H | 1 | €9.992,99 | €1.151,09 | €3.453,28 | €0,00 | €47,98 |
| TEST | Eth Adaptive 1H | 1 | €9.983,03 | €1.054,45 | €3.163,36 | €0,00 | €37,28 |
| TEST | Eth Donchian 1H | 0 | €9.982,54 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €9.975,63 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive V1 | 3 | €9.973,89 | €3.945,23 | €7.890,46 | €149,97 | €-21,37 |
| TEST | Master Adaptive No Alt V1 | 3 | €9.973,89 | €3.945,23 | €7.890,46 | €149,97 | €-21,37 |
| TEST | Master Adaptive Expanded V1 | 3 | €9.973,89 | €3.945,23 | €7.890,46 | €149,97 | €-21,37 |
| TEST | Master Adaptive Runner25 V1 | 3 | €9.973,89 | €3.945,23 | €7.890,46 | €149,97 | €-21,37 |
| TEST | Rapida V3 — Long + no HIGH + score <7,5 | 3 | €9.971,61 | €3.871,06 | €11.613,18 | €150,06 | €-21,42 |
| TEST | Rapida V3 — qualità completa + profit lock | 3 | €9.971,61 | €3.871,06 | €11.613,18 | €150,06 | €-21,42 |
| TEST | Bilanciata 1H V2 | 4 | €9.970,88 | €1.532,77 | €4.598,30 | €99,11 | €41,24 |
| TEST | Btc Ema 1H | 1 | €9.970,86 | €1.144,78 | €3.434,35 | €0,00 | €79,40 |
| TEST | Doge Donchian 1H | 0 | €9.968,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.968,09 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Strict3 V1 | 3 | €9.967,22 | €4.514,73 | €9.029,45 | €150,02 | €-27,36 |
| TEST | Combo Scanner | 2 | €9.963,95 | €1.577,94 | €3.155,88 | €99,71 | €4,24 |
| TEST | Master Adaptive Gb20 V1 | 3 | €9.953,24 | €4.008,73 | €8.017,46 | €149,87 | €-52,06 |
| TEST | Doge Ema 1H | 0 | €9.948,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — Trend/Transition | 3 | €9.945,50 | €3.023,78 | €6.047,55 | €149,68 | €-26,02 |
| TEST | Sol Bollinger 1H | 0 | €9.944,21 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 1H | 1 | €9.942,87 | €1.287,72 | €3.863,16 | €0,00 | €53,67 |
| TEST | Rapida V1 — senza PEPE | 3 | €9.939,22 | €3.201,60 | €9.604,79 | €99,45 | €19,28 |
| TEST | Rapida V1 — target pieno 2R | 3 | €9.939,22 | €3.201,60 | €9.604,79 | €99,45 | €19,28 |
| TEST | Benchmark trend following EMA 1H | 3 | €9.937,55 | €2.212,42 | €4.424,84 | €149,11 | €12,20 |
| TEST | Rapida V1 — score 6–7,5 | 3 | €9.930,41 | €3.200,79 | €9.602,37 | €99,27 | €19,31 |
| TEST | Rapida V3 — score <7,5 | 3 | €9.930,41 | €3.200,79 | €9.602,37 | €99,27 | €19,31 |
| TEST | Rapida V3 — senza ESPORTS | 3 | €9.930,41 | €3.200,79 | €9.602,37 | €99,27 | €19,31 |
| TEST | Combo Adaptive — parziale 1R | 3 | €9.922,83 | €3.016,88 | €6.033,77 | €149,34 | €-25,96 |
| TEST | Rapida 1H V3 Filtered — madre | 4 | €9.921,92 | €3.111,11 | €9.333,32 | €198,45 | €20,68 |
| TEST | Eth Ema 1H | 1 | €9.905,83 | €1.012,80 | €3.038,40 | €0,00 | €63,23 |
| TEST | Rapida V3 — no volatilità HIGH | 4 | €9.903,19 | €4.090,31 | €12.270,92 | €198,53 | €-11,37 |
| TEST | Rapida V1 — no HIGH + score <7,5 | 4 | €9.894,74 | €4.092,10 | €12.276,31 | €198,36 | €-28,02 |
| TEST | Top 5 + BTC — Guard + BTC≤3 | 0 | €9.881,42 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Top 5 + BTC — Guard + BTC≤3 + MFE | 0 | €9.881,42 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V1 — madre | 4 | €9.852,08 | €3.809,47 | €11.428,40 | €195,51 | €15,86 |
| TEST | Top 5 + BTC — Guard | 2 | €9.848,01 | €2.272,54 | €4.545,07 | €98,73 | €-29,17 |
| TEST | Top 5 + BTC — Guard + MFE | 2 | €9.848,01 | €2.272,54 | €4.545,07 | €98,73 | €-29,17 |
| TEST | Scanner Bottom 5 Short 1H | 3 | €9.780,17 | €659,56 | €1.319,12 | €97,90 | €6,07 |
| TEST | Global Confluence puro 1H | 0 | €9.773,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — MFE Trail esistente | 3 | €9.727,14 | €2.612,79 | €5.225,58 | €0,00 | €33,19 |

**Importante:** ogni riga è un conto virtuale separato da €10.000. I margini dei diversi portafogli non vanno sommati come se appartenessero a un unico conto.

**Rischio agli stop** è la perdita residua stimata usando gli stop correnti. Se uno stop protegge già un profitto, il rischio residuo viene mostrato come €0.

## Legenda portafogli

| Tipo | Nome leggibile | Metodo | Significato |
| --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | Confluenza trend | Riferimento principale: confluenza di trend su 4 ore, soglia più selettiva. |
| TEST | Bilanciata 1H V1 | Confluenza trend | Versione originale V1 a 1 ora basata sulla confluenza di trend. |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | Versione V2 selettiva: esclude i regimi storicamente peggiori, richiede trend e ritorni coerenti e limita i segnali correlati. |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | Versione V3 derivata dalla V1: accetta soltanto score assoluti da 6,0 a meno di 7,5, cioè la fascia BUONA risultata migliore nel confronto Paper vs Shadow. |
| TEST | Rapida 1H V1 — madre | Momentum / breakout | Madre Rapida 1H V1 originale, invariata. |
| TEST | Rapida V1 — score 6–7,5 | Momentum / breakout | Accetta soltanto score assoluti da 6,0 a meno di 7,5. |
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
| TEST | Combo Adaptive — 75% a 2R + runner 3R | Combo Adaptive | Chiude il 75% a 2R e lascia il 25% verso 3R con profit lock a 1,8R. |
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

## Confronto risultati

| Tipo | Portafoglio | Strategia | Equity | P&L chiuso | Trade | Eventi indip. | Win rate | PF | Expectancy | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | Confluenza trend | €9.860,68 | €-100,68 | 16 | 16 | 31,25% | 0,81 | €-6,29 | 4,26% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.487,42 | €428,53 | 24 | 24 | 50,00% | 2,02 | €17,86 | 2,70% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €10.464,71 | €386,68 | 17 | 17 | 47,06% | 2,37 | €22,75 | 1,62% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €10.270,74 | €120,58 | 23 | 23 | 39,13% | 1,19 | €5,24 | 2,20% |
| TEST | Combo Adaptive — madre | Combo Adaptive | €10.246,76 | €246,18 | 16 | 16 | 43,75% | 2,08 | €15,39 | 1,27% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €10.195,13 | €195,13 | 7 | 7 | 57,14% | 2,81 | €27,88 | 0,59% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €10.171,52 | €164,02 | 18 | 18 | 33,33% | 1,33 | €9,11 | 2,32% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €10.155,80 | €152,11 | 15 | 15 | 46,67% | 1,66 | €10,14 | 2,06% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €10.149,87 | €157,42 | 15 | 15 | 46,67% | 1,46 | €10,49 | 1,98% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €10.144,01 | €81,68 | 21 | 21 | 42,86% | 1,21 | €3,89 | 1,81% |
| TEST | Top 5 + BTC — 75% a 2,2R + runner 3R | Scanner Top 5 + forza BTC | €10.121,08 | €59,33 | 1 | 1 | 100,00% | ∞ | €59,33 | 0,53% |
| TEST | Top 5 + BTC — target pieno 3R | Scanner Top 5 + forza BTC | €10.121,08 | €59,33 | 1 | 1 | 100,00% | ∞ | €59,33 | 0,53% |
| TEST | Ampia 4H | Confluenza trend | €10.109,01 | €88,72 | 12 | 12 | 25,00% | 1,27 | €7,39 | 2,08% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €10.097,38 | €96,51 | 16 | 16 | 37,50% | 1,37 | €6,03 | 2,29% |
| TEST | Top 5 + BTC — BTC≤3 | Scanner Top 5 + forza BTC | €10.088,98 | €58,86 | 1 | 1 | 100,00% | ∞ | €58,86 | 0,73% |
| TEST | Top 5 + BTC — BTC 2–3 | Scanner Top 5 + forza BTC | €10.088,98 | €58,86 | 1 | 1 | 100,00% | ∞ | €58,86 | 0,73% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.068,69 | €68,69 | 1 | 1 | 100,00% | ∞ | €68,69 | 0,31% |
| TEST | Combo Trend | Combo Trend | €10.059,42 | €57,96 | 15 | 15 | 33,33% | 1,15 | €3,86 | 2,19% |
| TEST | Top 5 + BTC — solo MFE | Scanner Top 5 + forza BTC | €10.050,88 | €37,69 | 1 | 1 | 100,00% | ∞ | €37,69 | 0,59% |
| TEST | Btc Ema 4H | Trend following EMA | €10.030,44 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,19% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €10.030,44 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,19% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €10.026,97 | €-4,49 | 1 | 1 | 0,00% | 0,00 | €-4,49 | 0,55% |
| TEST | Sol Ema 1H | Trend following EMA | €10.018,78 | €-9,16 | 2 | 2 | 50,00% | 0,83 | €-4,58 | 0,98% |
| TEST | Rapida V3 — Long Only | Momentum / breakout V3 Filtered | €10.016,46 | €-4,22 | 1 | 1 | 0,00% | 0,00 | €-4,22 | 0,84% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €10.015,45 | €15,45 | 1 | 1 | 100,00% | ∞ | €15,45 | 0,51% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €10.009,47 | €-18,45 | 2 | 2 | 50,00% | 0,67 | €-9,23 | 0,99% |
| TEST | Combo Adaptive — Long Only | Combo Adaptive | €10.005,63 | €29,88 | 2 | 2 | 50,00% | 1,45 | €14,94 | 0,79% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €10.004,31 | €4,31 | 3 | 2 | 33,33% | 1,07 | €1,44 | 0,93% |
| TEST | Combo Adaptive — 75% a 2R + runner 3R | Combo Adaptive | €10.004,19 | €-54,84 | 1 | 1 | 0,00% | 0,00 | €-54,84 | 0,45% |
| TEST | Combo Adaptive — target pieno 3R | Combo Adaptive | €10.004,19 | €-54,84 | 1 | 1 | 0,00% | 0,00 | €-54,84 | 0,45% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €10.003,41 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,07% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €10.001,88 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,08% |
| TEST | Rapida V1 — Long + BTC 1–3 + score <7,5 | Momentum / breakout | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 15 · €10 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 20 · €10 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 25 · €10 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 20 · €50 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 20 · prudente · 5x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 85 · €10 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 80 · €10 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 85 · €50 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 80 · €50 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 85 · prudente · 5x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 80 · prudente · 5x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Eth Ema 4H | Trend following EMA | €9.999,14 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,17% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €9.995,85 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,11% |
| TEST | Sol Ema 4H | Trend following EMA | €9.995,47 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,11% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €9.995,47 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,11% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €9.995,13 | €-4,87 | 5 | 5 | 20,00% | 0,16 | €-0,97 | 0,05% |
| TEST | Combo Adaptive — Quality7 | Combo Adaptive | €9.993,55 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,32% |
| TEST | Combo Adaptive — Quality7 + Regime | Combo Adaptive | €9.993,55 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,32% |
| TEST | Combo Adaptive — Quality7 + Regime + parziale 1R | Combo Adaptive | €9.993,55 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,32% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €9.992,99 | €-54,55 | 1 | 1 | 0,00% | 0,00 | €-54,55 | 0,89% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.983,03 | €-51,89 | 2 | 2 | 50,00% | 0,05 | €-25,94 | 1,02% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.982,54 | €-17,46 | 3 | 3 | 33,33% | 0,84 | €-5,82 | 1,38% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €9.975,63 | €-24,37 | 5 | 5 | 20,00% | 0,16 | €-4,87 | 0,24% |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | €9.973,89 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,55% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €9.973,89 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,55% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €9.973,89 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,55% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €9.973,89 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,55% |
| TEST | Rapida V3 — Long + no HIGH + score <7,5 | Momentum / breakout V3 Filtered | €9.971,61 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 1,03% |
| TEST | Rapida V3 — qualità completa + profit lock | Momentum / breakout V3 Filtered | €9.971,61 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 1,03% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €9.970,88 | €-67,37 | 16 | 14 | 43,75% | 0,84 | €-4,21 | 2,75% |
| TEST | Btc Ema 1H | Trend following EMA | €9.970,86 | €-109,08 | 2 | 2 | 0,00% | 0,00 | €-54,54 | 1,56% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €9.968,98 | €-31,02 | 2 | 2 | 50,00% | 0,46 | €-15,51 | 0,93% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.968,09 | €-31,91 | 5 | 5 | 20,00% | 0,19 | €-6,38 | 0,32% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €9.967,22 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,73% |
| TEST | Combo Scanner | Combo Scanner | €9.963,95 | €-37,94 | 18 | 18 | 38,89% | 0,92 | €-2,11 | 2,00% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €9.953,24 | €10,11 | 1 | 1 | 100,00% | ∞ | €10,11 | 0,75% |
| TEST | Doge Ema 1H | Trend following EMA | €9.948,28 | €-51,72 | 4 | 4 | 50,00% | 0,54 | €-12,93 | 1,27% |
| TEST | Combo Adaptive — Trend/Transition | Combo Adaptive | €9.945,50 | €-24,85 | 3 | 3 | 33,33% | 0,80 | €-8,28 | 0,89% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.944,21 | €-55,79 | 1 | 1 | 0,00% | 0,00 | €-55,79 | 0,62% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €9.942,87 | €-110,32 | 2 | 2 | 0,00% | 0,00 | €-55,16 | 1,49% |
| TEST | Rapida V1 — senza PEPE | Momentum / breakout | €9.939,22 | €-74,30 | 2 | 2 | 0,00% | 0,00 | €-37,15 | 1,63% |
| TEST | Rapida V1 — target pieno 2R | Momentum / breakout | €9.939,22 | €-74,30 | 2 | 2 | 0,00% | 0,00 | €-37,15 | 1,63% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.937,55 | €-72,00 | 9 | 9 | 33,33% | 0,77 | €-8,00 | 2,25% |
| TEST | Rapida V1 — score 6–7,5 | Momentum / breakout | €9.930,41 | €-83,13 | 2 | 2 | 0,00% | 0,00 | €-41,57 | 1,71% |
| TEST | Rapida V3 — score <7,5 | Momentum / breakout V3 Filtered | €9.930,41 | €-83,13 | 2 | 2 | 0,00% | 0,00 | €-41,57 | 1,71% |
| TEST | Rapida V3 — senza ESPORTS | Momentum / breakout V3 Filtered | €9.930,41 | €-83,13 | 2 | 2 | 0,00% | 0,00 | €-41,57 | 1,71% |
| TEST | Combo Adaptive — parziale 1R | Combo Adaptive | €9.922,83 | €-47,59 | 3 | 3 | 33,33% | 0,61 | €-15,86 | 0,96% |
| TEST | Rapida 1H V3 Filtered — madre | Momentum / breakout V3 Filtered | €9.921,92 | €-93,16 | 38 | 38 | 34,21% | 0,89 | €-2,45 | 2,89% |
| TEST | Eth Ema 1H | Trend following EMA | €9.905,83 | €-155,12 | 4 | 4 | 25,00% | 0,05 | €-38,78 | 1,59% |
| TEST | Rapida V3 — no volatilità HIGH | Momentum / breakout V3 Filtered | €9.903,19 | €-78,08 | 1 | 1 | 0,00% | 0,00 | €-78,08 | 1,84% |
| TEST | Rapida V1 — no HIGH + score <7,5 | Momentum / breakout | €9.894,74 | €-69,88 | 1 | 1 | 0,00% | 0,00 | €-69,88 | 1,76% |
| TEST | Top 5 + BTC — Guard + BTC≤3 | Scanner Top 5 + forza BTC | €9.881,42 | €-118,58 | 2 | 2 | 0,00% | 0,00 | €-59,29 | 1,19% |
| TEST | Top 5 + BTC — Guard + BTC≤3 + MFE | Scanner Top 5 + forza BTC | €9.881,42 | €-118,58 | 2 | 2 | 0,00% | 0,00 | €-59,29 | 1,19% |
| TEST | Rapida 1H V1 — madre | Momentum / breakout | €9.852,08 | €-156,93 | 48 | 48 | 33,33% | 0,87 | €-3,27 | 5,79% |
| TEST | Top 5 + BTC — Guard | Scanner Top 5 + forza BTC | €9.848,01 | €-120,09 | 2 | 2 | 0,00% | 0,00 | €-60,05 | 1,59% |
| TEST | Top 5 + BTC — Guard + MFE | Scanner Top 5 + forza BTC | €9.848,01 | €-120,09 | 2 | 2 | 0,00% | 0,00 | €-60,05 | 1,59% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.780,17 | €-225,11 | 13 | 13 | 23,08% | 0,38 | €-17,32 | 4,15% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.773,98 | €-226,02 | 7 | 7 | 28,57% | 0,17 | €-32,29 | 2,46% |
| TEST | Combo Adaptive — MFE Trail esistente | Combo Adaptive | €9.727,14 | €-302,40 | 21 | 21 | 28,57% | 0,36 | €-14,40 | 3,44% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | DOGE | SHORT | Confluenza trend | 240m | 3,0x | 0,07292 | 0,07371 | 0,07500 | 0,09686 | 0,06875 | €574,44 | €1.723,33 | €49,28 | €-18,78 |
| Principale 4H | LAB | SHORT | Confluenza trend | 240m | 3,0x | 0,17841 | 0,17841 | 0,19982 | 0,23699 | 0,13559 | €136,26 | €408,77 | €49,05 | €-0,00 |
| Principale 4H | ZEC | LONG | Confluenza trend | 240m | 3,0x | 556,07119 | 544,18000 | 524,63715 | 373,49448 | 618,93927 | €293,97 | €881,92 | €49,85 | €-18,86 |
| Principale 4H | SUI | LONG | Confluenza trend | 240m | 3,0x | 0,76296 | 0,76296 | 0,73998 | 0,51245 | 0,80891 | €547,52 | €1.642,56 | €49,46 | €0,00 |
| Bilanciata 1H V1 | LAB | SHORT | Confluenza trend | 60m | 3,0x | 0,18667 | 0,18667 | 0,20845 | 0,24796 | 0,14311 | €143,84 | €431,52 | €50,35 | €-0,00 |
| Bilanciata 1H V1 | ONDO | LONG | Confluenza trend | 60m | 3,0x | 0,37613 | 0,37613 | 0,36189 | 0,25263 | 0,40460 | €442,89 | €1.328,68 | €50,30 | €0,00 |
| Bilanciata 1H V1 | ETH | LONG | Confluenza trend | 60m | 3,0x | 1894,43881 | 1933,86000 | 1921,86431 | 1272,43140 | 1955,82155 | €1.043,85 | €3.131,56 | €0,00 | €65,16 |
| Bilanciata 1H V1 | XRP | LONG | Confluenza trend | 60m | 3,0x | 1,13540 | 1,13620 | 1,11905 | 0,76261 | 1,16810 | €1.172,10 | €3.516,30 | €50,63 | €2,49 |
| Bilanciata 1H V2 | LAB | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,18667 | 0,18667 | 0,20845 | 0,24796 | 0,14311 | €139,69 | €419,08 | €48,90 | €-0,00 |
| Bilanciata 1H V2 | GRAM | SHORT | Confluenza trend V2 | 60m | 3,0x | 1,49240 | 1,49240 | 1,53621 | 1,98241 | 1,40478 | €570,19 | €1.710,58 | €50,21 | €-0,00 |
| Bilanciata 1H V2 | ESPORTS | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,02164 | 0,02164 | 0,02164 | 0,02874 | 0,01644 | €138,69 | €416,06 | €0,00 | €-0,00 |
| Bilanciata 1H V2 | PEPE | LONG | Confluenza trend V2 | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €684,20 | €2.052,59 | €0,00 | €41,24 |
| Bilanciata 1H V3 Filtered | ESPORTS | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,02126 | 0,02126 | 0,02126 | 0,02823 | 0,01615 | €141,51 | €424,52 | €0,00 | €-0,00 |
| Bilanciata 1H V3 Filtered | ETH | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1894,43881 | 1933,86000 | 1921,86431 | 1272,43140 | 1955,82155 | €1.047,36 | €3.142,08 | €0,00 | €65,38 |
| Bilanciata 1H V3 Filtered | XRP | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1,11148 | 1,13620 | 1,12430 | 0,74655 | 1,14349 | €1.163,70 | €3.491,09 | €0,00 | €77,64 |
| Bilanciata 1H V3 Filtered | ADA | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,17417 | 0,17519 | 0,17046 | 0,11699 | 0,18161 | €799,70 | €2.399,09 | €51,19 | €13,98 |
| Rapida 1H V1 — madre | ESPORTS | SHORT | Momentum / breakout | 60m | 3,0x | 0,01984 | 0,01984 | 0,02222 | 0,02635 | 0,01627 | €129,65 | €388,96 | €46,68 | €-0,00 |
| Rapida 1H V1 — madre | SUI | LONG | Momentum / breakout | 60m | 3,0x | 0,76416 | 0,76416 | 0,75422 | 0,51326 | 0,77907 | €1.284,19 | €3.852,58 | €50,12 | €0,00 |
| Rapida 1H V1 — madre | XRP | LONG | Momentum / breakout | 60m | 3,0x | 1,13540 | 1,13620 | 1,12268 | 0,76261 | 1,15447 | €1.476,35 | €4.429,06 | €49,61 | €3,13 |
| Rapida 1H V1 — madre | ADA | LONG | Momentum / breakout | 60m | 3,0x | 0,17438 | 0,17519 | 0,17128 | 0,11713 | 0,17904 | €919,27 | €2.757,80 | €49,11 | €12,73 |
| Rapida V1 — score 6–7,5 | XRP | LONG | Momentum / breakout | 60m | 3,0x | 1,13540 | 1,13620 | 1,12268 | 0,76261 | 1,15447 | €1.488,10 | €4.464,29 | €50,00 | €3,16 |
| Rapida V1 — score 6–7,5 | ETH | LONG | Momentum / breakout | 60m | 3,0x | 1923,99472 | 1933,86000 | 1924,83009 | 1292,28312 | 1956,31783 | €1.487,21 | €4.461,62 | €0,00 | €22,88 |
| Rapida V1 — score 6–7,5 | NIGHT | SHORT | Momentum / breakout | 60m | 3,0x | 0,01944 | 0,01964 | 0,02086 | 0,02583 | 0,01732 | €225,49 | €676,47 | €49,27 | €-6,73 |
| Rapida V1 — no HIGH + score <7,5 | ADA | LONG | Momentum / breakout | 60m | 3,0x | 0,17562 | 0,17519 | 0,17242 | 0,11795 | 0,18041 | €915,08 | €2.745,23 | €50,00 | €-6,65 |
| Rapida V1 — no HIGH + score <7,5 | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 62,98259 | 62,69400 | 62,26655 | 42,30331 | 64,05666 | €1.465,66 | €4.396,98 | €49,99 | €-20,15 |
| Rapida V1 — no HIGH + score <7,5 | XRP | LONG | Momentum / breakout | 60m | 3,0x | 1,13484 | 1,13620 | 1,12213 | 0,76223 | 1,15390 | €1.490,32 | €4.470,97 | €50,07 | €5,37 |
| Rapida V1 — no HIGH + score <7,5 | NIGHT | SHORT | Momentum / breakout | 60m | 3,0x | 0,01944 | 0,01964 | 0,02086 | 0,02583 | 0,01732 | €221,04 | €663,13 | €48,30 | €-6,60 |
| Rapida V1 — senza PEPE | XRP | LONG | Momentum / breakout | 60m | 3,0x | 1,13540 | 1,13620 | 1,12268 | 0,76261 | 1,15447 | €1.488,10 | €4.464,29 | €50,00 | €3,16 |
| Rapida V1 — senza PEPE | ETH | LONG | Momentum / breakout | 60m | 3,0x | 1923,99472 | 1933,86000 | 1924,83009 | 1292,28312 | 1956,31783 | €1.487,21 | €4.461,62 | €0,00 | €22,88 |
| Rapida V1 — senza PEPE | NIGHT | SHORT | Momentum / breakout | 60m | 3,0x | 0,01944 | 0,01964 | 0,02086 | 0,02583 | 0,01732 | €226,30 | €678,89 | €49,45 | €-6,75 |
| Rapida V1 — target pieno 2R | XRP | LONG | Momentum / breakout | 60m | 3,0x | 1,13540 | 1,13620 | 1,12268 | 0,76261 | 1,16083 | €1.488,10 | €4.464,29 | €50,00 | €3,16 |
| Rapida V1 — target pieno 2R | ETH | LONG | Momentum / breakout | 60m | 3,0x | 1923,99472 | 1933,86000 | 1924,83009 | 1292,28312 | 1967,09220 | €1.487,21 | €4.461,62 | €0,00 | €22,88 |
| Rapida V1 — target pieno 2R | NIGHT | SHORT | Momentum / breakout | 60m | 3,0x | 0,01944 | 0,01964 | 0,02086 | 0,02583 | 0,01661 | €226,30 | €678,89 | €49,45 | €-6,75 |
| Rapida 1H V3 Filtered — madre | ESPORTS | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01977 | 0,01977 | 0,02214 | 0,02626 | 0,01621 | €137,70 | €413,09 | €49,57 | €-0,00 |
| Rapida 1H V3 Filtered — madre | SUI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,76416 | 0,76416 | 0,75422 | 0,51326 | 0,77907 | €1.267,97 | €3.803,92 | €49,49 | €0,00 |
| Rapida 1H V3 Filtered — madre | XRP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,13084 | 1,13620 | 1,11817 | 0,75954 | 1,14983 | €1.481,92 | €4.445,76 | €49,79 | €21,09 |
| Rapida 1H V3 Filtered — madre | NIGHT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01962 | 0,01964 | 0,02108 | 0,02607 | 0,01745 | €223,52 | €670,55 | €49,60 | €-0,40 |
| Rapida V3 — score <7,5 | XRP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,13540 | 1,13620 | 1,12268 | 0,76261 | 1,15447 | €1.488,10 | €4.464,29 | €50,00 | €3,16 |
| Rapida V3 — score <7,5 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1923,99472 | 1933,86000 | 1924,83009 | 1292,28312 | 1956,31783 | €1.487,21 | €4.461,62 | €0,00 | €22,88 |
| Rapida V3 — score <7,5 | NIGHT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01944 | 0,01964 | 0,02086 | 0,02583 | 0,01732 | €225,49 | €676,47 | €49,27 | €-6,73 |
| Rapida V3 — no volatilità HIGH | XRP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,13062 | 1,13620 | 1,11795 | 0,75940 | 1,14961 | €1.488,10 | €4.464,29 | €50,00 | €22,05 |
| Rapida V3 — no volatilità HIGH | ADA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,17562 | 0,17519 | 0,17242 | 0,11795 | 0,18041 | €914,75 | €2.744,25 | €49,98 | €-6,64 |
| Rapida V3 — no volatilità HIGH | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 62,98259 | 62,69400 | 62,26655 | 42,30331 | 64,05666 | €1.465,14 | €4.395,41 | €49,97 | €-20,14 |
| Rapida V3 — no volatilità HIGH | NIGHT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01944 | 0,01964 | 0,02086 | 0,02583 | 0,01732 | €222,32 | €666,97 | €48,58 | €-6,63 |
| Rapida V3 — Long Only | XRP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,13540 | 1,13620 | 1,12268 | 0,76261 | 1,15447 | €1.488,10 | €4.464,29 | €50,00 | €3,16 |
| Rapida V3 — Long Only | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1923,99472 | 1933,86000 | 1924,83009 | 1292,28312 | 1956,31783 | €1.487,21 | €4.461,62 | €0,00 | €22,88 |
| Rapida V3 — Long + no HIGH + score <7,5 | ADA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,17562 | 0,17519 | 0,17242 | 0,11795 | 0,18041 | €915,08 | €2.745,23 | €50,00 | €-6,65 |
| Rapida V3 — Long + no HIGH + score <7,5 | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 62,98259 | 62,69400 | 62,26655 | 42,30331 | 64,05666 | €1.465,66 | €4.396,98 | €49,99 | €-20,15 |
| Rapida V3 — Long + no HIGH + score <7,5 | XRP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,13484 | 1,13620 | 1,12213 | 0,76223 | 1,15390 | €1.490,32 | €4.470,97 | €50,07 | €5,37 |
| Rapida V3 — senza ESPORTS | XRP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,13540 | 1,13620 | 1,12268 | 0,76261 | 1,15447 | €1.488,10 | €4.464,29 | €50,00 | €3,16 |
| Rapida V3 — senza ESPORTS | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1923,99472 | 1933,86000 | 1924,83009 | 1292,28312 | 1956,31783 | €1.487,21 | €4.461,62 | €0,00 | €22,88 |
| Rapida V3 — senza ESPORTS | NIGHT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01944 | 0,01964 | 0,02086 | 0,02583 | 0,01732 | €225,49 | €676,47 | €49,27 | €-6,73 |
| Rapida V3 — qualità completa + profit lock | ADA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,17562 | 0,17519 | 0,17242 | 0,11795 | 0,18041 | €915,08 | €2.745,23 | €50,00 | €-6,65 |
| Rapida V3 — qualità completa + profit lock | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 62,98259 | 62,69400 | 62,26655 | 42,30331 | 64,05666 | €1.465,66 | €4.396,98 | €49,99 | €-20,15 |
| Rapida V3 — qualità completa + profit lock | XRP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,13484 | 1,13620 | 1,12213 | 0,76223 | 1,15390 | €1.490,32 | €4.470,97 | €50,07 | €5,37 |
| Ampia 4H | DOGE | SHORT | Confluenza trend | 240m | 2,0x | 0,07237 | 0,07371 | 0,07515 | 0,10819 | 0,06457 | €649,49 | €1.298,97 | €50,00 | €-24,11 |
| Ampia 4H | ZEC | LONG | Confluenza trend | 240m | 2,0x | 522,36445 | 544,18000 | 483,09844 | 263,79405 | 632,30930 | €332,53 | €665,06 | €49,99 | €27,77 |
| Ampia 4H | PEPE | LONG | Confluenza trend | 240m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €497,18 | €994,35 | €50,70 | €17,97 |
| Ampia 4H | ETH | LONG | Confluenza trend | 240m | 2,0x | 1933,63665 | 1933,86000 | 1869,00475 | 976,48651 | 2114,60597 | €756,64 | €1.513,28 | €50,58 | €0,17 |
| Forza relativa 1H V1 | NEAR | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 2,02421 | 2,02421 | 1,97233 | 1,02223 | 2,13836 | €984,05 | €1.968,10 | €50,44 | €0,00 |
| Forza relativa 1H V1 | ALLO | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,37581 | 0,37581 | 0,40458 | 0,56184 | 0,31252 | €329,44 | €658,87 | €50,44 | €-0,00 |
| Forza relativa 1H V1 | ESPORTS | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,02126 | 0,02126 | 0,02126 | 0,03178 | 0,01564 | €208,05 | €416,10 | €0,00 | €-0,00 |
| Forza relativa 1H V1 | PEPE | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €986,47 | €1.972,93 | €50,47 | €4,27 |
| Forza relativa 1H V2 | LAB | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,18833 | 0,18833 | 0,20950 | 0,28155 | 0,14176 | €222,78 | €445,56 | €50,08 | €-0,00 |
| Forza relativa 1H V2 | GRAM | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 1,47771 | 1,47771 | 1,52060 | 2,20918 | 1,38336 | €871,54 | €1.743,07 | €50,59 | €-0,00 |
| Forza relativa 1H V2 | ESPORTS | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,02126 | 0,02126 | 0,02126 | 0,03178 | 0,01564 | €215,33 | €430,67 | €0,00 | €-0,00 |
| Forza relativa 1H V2 | ADA | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,17438 | 0,17519 | 0,17039 | 0,08806 | 0,18317 | €1.109,61 | €2.219,23 | €50,81 | €10,25 |
| Benchmark Donchian breakout 1H | SUI | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,76606 | 0,76606 | 0,75182 | 0,38686 | 0,80165 | €1.377,00 | €2.754,00 | €51,18 | €0,00 |
| Benchmark Donchian breakout 1H | ADA | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,17562 | 0,17519 | 0,17105 | 0,08869 | 0,18704 | €975,80 | €1.951,59 | €50,78 | €-4,72 |
| Benchmark Bollinger mean reversion 1H | ADA | SHORT | Bollinger mean reversion | 60m | 2,0x | 0,17554 | 0,17519 | 0,17897 | 0,26244 | 0,17041 | €1.300,59 | €2.601,19 | €50,76 | €5,26 |
| Benchmark trend following EMA 1H | NEAR | LONG | Trend following EMA | 60m | 2,0x | 2,02421 | 2,02421 | 1,96657 | 1,02223 | 2,15104 | €873,40 | €1.746,81 | €49,75 | €0,00 |
| Benchmark trend following EMA 1H | ALLO | SHORT | Trend following EMA | 60m | 2,0x | 0,37581 | 0,37581 | 0,40778 | 0,56184 | 0,30549 | €292,32 | €584,65 | €49,73 | €-0,00 |
| Benchmark trend following EMA 1H | ADA | LONG | Trend following EMA | 60m | 2,0x | 0,17417 | 0,17519 | 0,17005 | 0,08796 | 0,18326 | €1.046,69 | €2.093,39 | €49,63 | €12,20 |
| Scanner Top 5 Long 1H | ONDO | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,37282 | 0,37282 | 0,35738 | 0,18828 | 0,40370 | €625,48 | €1.250,97 | €51,81 | €0,00 |
| Scanner Top 5 Long 1H | XRP | LONG | Scanner Top 5 Long | 60m | 2,0x | 1,11469 | 1,13620 | 1,12469 | 0,56292 | 1,14680 | €1.796,54 | €3.593,08 | €0,00 | €69,33 |
| Scanner Top 5 Long 1H | ADA | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,17562 | 0,17519 | 0,17150 | 0,08869 | 0,18384 | €1.118,38 | €2.236,77 | €52,38 | €-5,41 |
| Scanner Bottom 5 Short 1H | ESPORTS | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,02150 | 0,02150 | 0,02150 | 0,03214 | 0,01634 | €207,40 | €414,80 | €0,00 | €-0,00 |
| Scanner Bottom 5 Short 1H | NIGHT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,01943 | 0,01964 | 0,02135 | 0,02905 | 0,01560 | €248,62 | €497,24 | €49,06 | €-5,14 |
| Scanner Bottom 5 Short 1H | AKE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,00168 | 0,00163 | 0,00188 | 0,00251 | 0,00127 | €203,54 | €407,07 | €48,85 | €11,21 |
| Scanner Top 5 + forza BTC 1H | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,37613 | 0,37613 | 0,36189 | 0,18994 | 0,40745 | €677,81 | €1.355,62 | €51,32 | €0,00 |
| Scanner Top 5 + forza BTC 1H | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.070,89 | €2.141,78 | €0,00 | €56,52 |
| Scanner Top 5 + forza BTC 1H | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 77,70854 | 78,33600 | 76,45304 | 39,24281 | 80,47063 | €1.614,82 | €3.229,64 | €52,18 | €26,08 |
| Top 5 + BTC — solo MFE | SUI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,76776 | 0,76776 | 0,75508 | 0,38772 | 0,79565 | €1.514,04 | €3.028,08 | €50,00 | €0,00 |
| Top 5 + BTC — solo MFE | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 77,76655 | 78,33600 | 77,76655 | 39,27211 | 80,43319 | €1.603,37 | €3.206,74 | €0,00 | €23,48 |
| Top 5 + BTC — solo MFE | ADA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,17562 | 0,17519 | 0,17150 | 0,08869 | 0,18466 | €1.073,91 | €2.147,81 | €50,30 | €-5,20 |
| Top 5 + BTC — Guard | ADA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,17562 | 0,17519 | 0,17150 | 0,08869 | 0,18466 | €1.054,77 | €2.109,54 | €49,40 | €-5,11 |
| Top 5 + BTC — Guard | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.217,77 | €2.435,54 | €49,33 | €-24,06 |
| Top 5 + BTC — BTC≤3 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.063,01 | €2.126,01 | €50,00 | €9,43 |
| Top 5 + BTC — BTC≤3 | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 77,78955 | 78,33600 | 76,66939 | 39,28373 | 80,25393 | €1.735,32 | €3.470,64 | €49,98 | €24,38 |
| Top 5 + BTC — BTC 2–3 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.063,01 | €2.126,01 | €50,00 | €9,43 |
| Top 5 + BTC — BTC 2–3 | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 77,78955 | 78,33600 | 76,66939 | 39,28373 | 80,25393 | €1.735,32 | €3.470,64 | €49,98 | €24,38 |
| Top 5 + BTC — Guard + MFE | ADA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,17562 | 0,17519 | 0,17150 | 0,08869 | 0,18466 | €1.054,77 | €2.109,54 | €49,40 | €-5,11 |
| Top 5 + BTC — Guard + MFE | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.217,77 | €2.435,54 | €49,33 | €-24,06 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.031,84 | €2.063,68 | €50,00 | €7,80 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | ETH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1900,34999 | 1933,86000 | 1924,36944 | 959,67675 | 1983,27732 | €1.717,93 | €3.435,85 | €0,00 | €60,59 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | XRP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,13643 | 1,13620 | 1,12006 | 0,57390 | 1,18552 | €1.757,62 | €3.515,24 | €50,62 | €-0,70 |
| Top 5 + BTC — target pieno 3R | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.031,84 | €2.063,68 | €50,00 | €7,80 |
| Top 5 + BTC — target pieno 3R | ETH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1900,34999 | 1933,86000 | 1924,36944 | 959,67675 | 1983,27732 | €1.717,93 | €3.435,85 | €0,00 | €60,59 |
| Top 5 + BTC — target pieno 3R | XRP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,13643 | 1,13620 | 1,12006 | 0,57390 | 1,18552 | €1.757,62 | €3.515,24 | €50,62 | €-0,70 |
| Combo Trend | ONDO | LONG | Combo Trend | 60m | 2,0x | 0,37282 | 0,37282 | 0,35567 | 0,18828 | 0,41057 | €545,86 | €1.091,71 | €50,24 | €0,00 |
| Combo Trend | ESPORTS | SHORT | Combo Trend | 60m | 2,0x | 0,01883 | 0,01883 | 0,02109 | 0,02815 | 0,01386 | €209,57 | €419,14 | €50,30 | €-0,00 |
| Combo Trend | PEPE | LONG | Combo Trend | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €884,51 | €1.769,01 | €50,29 | €3,83 |
| Combo Scanner | ONDO | LONG | Combo Scanner | 60m | 2,0x | 0,37282 | 0,37282 | 0,35738 | 0,18828 | 0,40679 | €599,14 | €1.198,28 | €49,63 | €0,00 |
| Combo Scanner | PEPE | LONG | Combo Scanner | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €978,80 | €1.957,60 | €50,08 | €4,24 |
| Combo Adaptive — madre | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,37282 | 0,37282 | 0,35738 | 0,18828 | 0,40370 | €613,42 | €1.226,85 | €50,81 | €0,00 |
| Combo Adaptive — madre | GRAM | SHORT | Combo Adaptive | 60m | 2,0x | 1,48181 | 1,48181 | 1,51561 | 2,21531 | 1,41422 | €1.129,35 | €2.258,70 | €51,51 | €-0,00 |
| Combo Adaptive — madre | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.001,06 | €2.002,12 | €51,22 | €4,33 |
| Combo Adaptive — MFE Trail esistente | ESPORTS | SHORT | Combo Adaptive | 60m | 2,0x | 0,02156 | 0,02156 | 0,02091 | 0,03223 | 0,01638 | €202,62 | €405,24 | €0,00 | €-0,00 |
| Combo Adaptive — MFE Trail esistente | SOL | LONG | Combo Adaptive | 60m | 2,0x | 77,56451 | 78,33600 | 77,65759 | 39,17008 | 80,14392 | €1.462,23 | €2.924,45 | €0,00 | €29,09 |
| Combo Adaptive — MFE Trail esistente | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €947,94 | €1.895,88 | €0,00 | €4,10 |
| Combo Adaptive — Quality7 | ADA | LONG | Combo Adaptive | 60m | 2,0x | 0,17562 | 0,17519 | 0,17150 | 0,08869 | 0,18384 | €1.067,59 | €2.135,18 | €50,00 | €-5,17 |
| Combo Adaptive — Trend/Transition | ADA | LONG | Combo Adaptive | 60m | 2,0x | 0,17562 | 0,17519 | 0,17150 | 0,08869 | 0,18384 | €1.064,94 | €2.129,87 | €49,88 | €-5,16 |
| Combo Adaptive — Trend/Transition | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 62,98259 | 62,69400 | 62,06196 | 31,80621 | 64,82385 | €1.705,77 | €3.411,54 | €49,87 | €-15,63 |
| Combo Adaptive — Trend/Transition | NIGHT | SHORT | Combo Adaptive | 60m | 2,0x | 0,01943 | 0,01964 | 0,02135 | 0,02905 | 0,01560 | €253,07 | €506,14 | €49,93 | €-5,23 |
| Combo Adaptive — Quality7 + Regime | ADA | LONG | Combo Adaptive | 60m | 2,0x | 0,17562 | 0,17519 | 0,17150 | 0,08869 | 0,18384 | €1.067,59 | €2.135,18 | €50,00 | €-5,17 |
| Combo Adaptive — Long Only | ADA | LONG | Combo Adaptive | 60m | 2,0x | 0,17562 | 0,17519 | 0,17150 | 0,08869 | 0,18384 | €1.070,78 | €2.141,56 | €50,15 | €-5,18 |
| Combo Adaptive — Long Only | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 62,98259 | 62,69400 | 62,06196 | 31,80621 | 64,82385 | €1.715,13 | €3.430,26 | €50,14 | €-15,72 |
| Combo Adaptive — parziale 1R | ADA | LONG | Combo Adaptive | 60m | 2,0x | 0,17562 | 0,17519 | 0,17150 | 0,08869 | 0,18384 | €1.062,51 | €2.125,02 | €49,76 | €-5,14 |
| Combo Adaptive — parziale 1R | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 62,98259 | 62,69400 | 62,06196 | 31,80621 | 64,82385 | €1.701,88 | €3.403,76 | €49,75 | €-15,60 |
| Combo Adaptive — parziale 1R | NIGHT | SHORT | Combo Adaptive | 60m | 2,0x | 0,01943 | 0,01964 | 0,02135 | 0,02905 | 0,01560 | €252,49 | €504,99 | €49,82 | €-5,22 |
| Combo Adaptive — Quality7 + Regime + parziale 1R | ADA | LONG | Combo Adaptive | 60m | 2,0x | 0,17562 | 0,17519 | 0,17150 | 0,08869 | 0,18384 | €1.067,59 | €2.135,18 | €50,00 | €-5,17 |
| Combo Adaptive — 75% a 2R + runner 3R | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.031,84 | €2.063,68 | €50,00 | €7,80 |
| Combo Adaptive — 75% a 2R + runner 3R | ETH | LONG | Combo Adaptive | 60m | 2,0x | 1900,34999 | 1933,86000 | 1925,94234 | 959,67675 | 1983,27732 | €1.718,41 | €3.436,81 | €0,00 | €60,60 |
| Combo Adaptive — 75% a 2R + runner 3R | NIGHT | SHORT | Combo Adaptive | 60m | 2,0x | 0,01943 | 0,01964 | 0,02135 | 0,02905 | 0,01368 | €253,49 | €506,98 | €50,02 | €-5,24 |
| Combo Adaptive — target pieno 3R | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.031,84 | €2.063,68 | €50,00 | €7,80 |
| Combo Adaptive — target pieno 3R | ETH | LONG | Combo Adaptive | 60m | 2,0x | 1900,34999 | 1933,86000 | 1925,94234 | 959,67675 | 1983,27732 | €1.718,41 | €3.436,81 | €0,00 | €60,60 |
| Combo Adaptive — target pieno 3R | NIGHT | SHORT | Combo Adaptive | 60m | 2,0x | 0,01943 | 0,01964 | 0,02135 | 0,02905 | 0,01368 | €253,49 | €506,98 | €50,02 | €-5,24 |
| Btc Ema 1H | BTC | LONG | Trend following EMA | 60m | 3,0x | 64820,68154 | 66319,38000 | 65901,17899 | 43537,89110 | 66687,51717 | €1.144,78 | €3.434,35 | €0,00 | €79,40 |
| Btc Ema 4H | BTC | LONG | Trend following EMA | 240m | 2,0x | 65410,57950 | 66319,38000 | 63931,54687 | 33032,34265 | 69108,16107 | €1.105,63 | €2.211,26 | €50,00 | €30,72 |
| Btc Donchian 1H | BTC | LONG | Donchian breakout 20 barre | 60m | 3,0x | 65410,57950 | 66319,38000 | 65797,56943 | 43934,10590 | 67085,09034 | €1.287,72 | €3.863,16 | €0,00 | €53,67 |
| Btc Donchian 4H | BTC | LONG | Donchian breakout 20 barre | 240m | 2,0x | 65410,57950 | 66319,38000 | 63931,54687 | 33032,34265 | 69551,87112 | €1.105,63 | €2.211,26 | €50,00 | €30,72 |
| Btc Adaptive 1H | BTC | LONG | Combo Adaptive | 60m | 3,0x | 65410,57950 | 66319,38000 | 65617,01786 | 43934,10590 | 67294,40419 | €1.151,09 | €3.453,28 | €0,00 | €47,98 |
| Btc Adaptive 4H | BTC | LONG | Combo Adaptive | 240m | 2,0x | 66171,85172 | 66319,38000 | 64592,42491 | 33416,78512 | 70120,41876 | €1.047,40 | €2.094,81 | €50,00 | €4,67 |
| Sol Ema 1H | SOL | LONG | Trend following EMA | 60m | 3,0x | 77,56451 | 78,33600 | 76,27481 | 52,09750 | 80,14392 | €1.001,44 | €3.004,32 | €49,95 | €29,88 |
| Sol Ema 4H | SOL | LONG | Trend following EMA | 240m | 2,0x | 78,49069 | 78,33600 | 76,26213 | 39,63780 | 84,06211 | €880,51 | €1.761,01 | €50,00 | €-3,47 |
| Sol Donchian 1H | SOL | LONG | Donchian breakout 20 barre | 60m | 3,0x | 77,56451 | 78,33600 | 77,71982 | 52,09750 | 79,85731 | €1.127,14 | €3.381,43 | €0,00 | €33,63 |
| Sol Donchian 4H | SOL | LONG | Donchian breakout 20 barre | 240m | 2,0x | 78,49069 | 78,33600 | 76,26213 | 39,63780 | 84,73068 | €880,51 | €1.761,01 | €50,00 | €-3,47 |
| Sol Bollinger 4H | SOL | SHORT | Bollinger mean reversion | 240m | 2,0x | 78,45931 | 78,33600 | 80,48446 | 117,29666 | 74,81402 | €968,56 | €1.937,11 | €50,00 | €3,04 |
| Sol Adaptive 1H | SOL | LONG | Combo Adaptive | 60m | 3,0x | 77,56451 | 78,33600 | 76,27481 | 52,09750 | 80,14392 | €1.000,51 | €3.001,52 | €49,91 | €29,85 |
| Sol Adaptive 4H | SOL | LONG | Combo Adaptive | 240m | 2,0x | 78,49069 | 78,33600 | 76,05953 | 39,63780 | 84,56860 | €807,13 | €1.614,26 | €50,00 | €-3,18 |
| Eth Ema 1H | ETH | LONG | Trend following EMA | 60m | 3,0x | 1894,43881 | 1933,86000 | 1925,36798 | 1272,43140 | 1955,82155 | €1.012,80 | €3.038,40 | €0,00 | €63,23 |
| Eth Ema 4H | ETH | LONG | Trend following EMA | 240m | 2,0x | 1933,63665 | 1933,86000 | 1878,94813 | 976,48651 | 2070,35799 | €883,93 | €1.767,86 | €50,00 | €0,20 |
| Eth Adaptive 1H | ETH | LONG | Combo Adaptive | 60m | 3,0x | 1911,33219 | 1933,86000 | 1921,69220 | 1283,77812 | 1971,43961 | €1.054,45 | €3.163,36 | €0,00 | €37,28 |
| Master Adaptive V1 | ADA | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,17603 | 0,17519 | 0,17190 | 0,08889 | 0,18427 | €1.067,59 | €2.135,18 | €50,00 | €-10,13 |
| Master Adaptive V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 62,99860 | 62,69400 | 62,07773 | 31,81429 | 64,84032 | €1.710,02 | €3.420,04 | €49,99 | €-16,54 |
| Master Adaptive V1 | PEPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.167,62 | €2.335,24 | €49,98 | €5,29 |
| Master Adaptive No Alt V1 | ADA | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,17603 | 0,17519 | 0,17190 | 0,08889 | 0,18427 | €1.067,59 | €2.135,18 | €50,00 | €-10,13 |
| Master Adaptive No Alt V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 62,99860 | 62,69400 | 62,07773 | 31,81429 | 64,84032 | €1.710,02 | €3.420,04 | €49,99 | €-16,54 |
| Master Adaptive No Alt V1 | PEPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.167,62 | €2.335,24 | €49,98 | €5,29 |
| Master Adaptive Strict3 V1 | ADA | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,17603 | 0,17519 | 0,17190 | 0,08889 | 0,18427 | €1.067,59 | €2.135,18 | €50,00 | €-10,13 |
| Master Adaptive Strict3 V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 62,99860 | 62,69400 | 62,07773 | 31,81429 | 64,84032 | €1.710,02 | €3.420,04 | €49,99 | €-16,54 |
| Master Adaptive Strict3 V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 1934,24677 | 1933,86000 | 1906,39362 | 976,79462 | 1989,95308 | €1.737,12 | €3.474,23 | €50,03 | €-0,69 |
| Master Adaptive Expanded V1 | ADA | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,17603 | 0,17519 | 0,17190 | 0,08889 | 0,18427 | €1.067,59 | €2.135,18 | €50,00 | €-10,13 |
| Master Adaptive Expanded V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 62,99860 | 62,69400 | 62,07773 | 31,81429 | 64,84032 | €1.710,02 | €3.420,04 | €49,99 | €-16,54 |
| Master Adaptive Expanded V1 | PEPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.167,62 | €2.335,24 | €49,98 | €5,29 |
| Master Adaptive Gb20 V1 | ADA | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,17603 | 0,17519 | 0,17190 | 0,08889 | 0,18427 | €1.067,59 | €2.135,18 | €50,00 | €-10,13 |
| Master Adaptive Gb20 V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 62,99860 | 62,69400 | 62,07773 | 31,81429 | 64,84032 | €1.710,02 | €3.420,04 | €49,99 | €-16,54 |
| Master Adaptive Gb20 V1 | PEPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.231,12 | €2.462,24 | €49,88 | €-25,40 |
| Master Adaptive Runner25 V1 | ADA | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,17603 | 0,17519 | 0,17190 | 0,08889 | 0,18839 | €1.067,59 | €2.135,18 | €50,00 | €-10,13 |
| Master Adaptive Runner25 V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 62,99860 | 62,69400 | 62,07773 | 31,81429 | 65,76119 | €1.710,02 | €3.420,04 | €49,99 | €-16,54 |
| Master Adaptive Runner25 V1 | PEPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.167,62 | €2.335,24 | €49,98 | €5,29 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Scalp RSI Short 75 · prudente · 5x | DOGE | SHORT | 2026-07-21T11:53:34+00:00 | 0,07396 | €-14,09 | -1,41 | STOP_GAP_STRESS |
| Scalp RSI Short 75 · €50 · 15x | DOGE | SHORT | 2026-07-21T11:53:34+00:00 | 0,07396 | €-4,24 | -1,41 | STOP_GAP_STRESS |
| Scalp RSI Short 75 · €10 · 15x | DOGE | SHORT | 2026-07-21T11:53:34+00:00 | 0,07396 | €-0,85 | -1,41 | STOP_GAP_STRESS |
| Top 5 + BTC — target pieno 3R | ADA | LONG | 2026-07-21T11:38:33+00:00 | 0,17418 | €59,33 | 1,19 | STOP |
| Top 5 + BTC — 75% a 2,2R + runner 3R | ADA | LONG | 2026-07-21T11:38:33+00:00 | 0,17418 | €59,33 | 1,19 | STOP |
| Rapida V3 — senza ESPORTS | ADA | LONG | 2026-07-21T11:38:33+00:00 | 0,17414 | €-4,22 | -0,08 | STOP |
| Rapida V3 — Long Only | ADA | LONG | 2026-07-21T11:38:33+00:00 | 0,17414 | €-4,22 | -0,08 | STOP |
| Rapida V3 — score <7,5 | ADA | LONG | 2026-07-21T11:38:33+00:00 | 0,17414 | €-4,22 | -0,08 | STOP |
| Rapida 1H V3 Filtered — madre | ADA | LONG | 2026-07-21T11:38:33+00:00 | 0,17414 | €-4,19 | -0,08 | STOP |
| Rapida V1 — target pieno 2R | ADA | LONG | 2026-07-21T11:38:33+00:00 | 0,17414 | €-4,22 | -0,08 | STOP |
| Rapida V1 — score 6–7,5 | ADA | LONG | 2026-07-21T11:38:33+00:00 | 0,17414 | €-4,22 | -0,08 | STOP |
| Rapida V1 — senza PEPE | ADA | LONG | 2026-07-21T11:38:33+00:00 | 0,17414 | €-4,22 | -0,08 | STOP |

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
| MAIN | Principale 4H | 34/30 | 16/30 | 0,92 | 0,81 | -0,05R | €-6,29 | 4,26% | COERENTE − | BOCCIATA RESEARCH |
| RSI_EXTREME_LONG_15M | Scalp RSI Long 25 · prudente · 5x (riferimento tra 9 varianti) | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| RSI_EXTREME_SHORT_15M | Scalp RSI Short 75 · prudente · 5x (riferimento tra 9 varianti) | 5/30 | 5/30 | 0,32 | 0,19 | -0,55R | €-6,38 | 0,32% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_1H_BALANCED | Bilanciata 1H V1 | 113/30 | 21/30 | 1,00 | 1,21 | 0,00R | €3,89 | 1,81% | COERENTE + | BOCCIATA RESEARCH |
| SHADOW_1H_BALANCED_V2 | Bilanciata 1H V2 | 17/30 | 14/30 | 1,51 | 0,84 | 0,30R | €-4,21 | 2,75% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_1H_BALANCED_V3 | Bilanciata 1H V3 Filtered | 31/30 | 23/30 | 1,35 | 1,19 | 0,21R | €5,24 | 2,20% | COERENTE + | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_1H_FAST | Rapida 1H V1 — madre | 129/30 | 48/30 | 0,91 | 0,87 | -0,06R | €-3,27 | 5,79% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | Rapida V1 — Long + BTC 1–3 + score <7,5 | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | Rapida V1 — no HIGH + score <7,5 | 2/30 | 1/30 | 0,00 | 0,00 | -1,05R | €-69,88 | 1,76% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_NO_PEPE_V1 | Rapida V1 — senza PEPE | 2/30 | 2/30 | 0,00 | 0,00 | -1,05R | €-37,15 | 1,63% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_V1 | Rapida V1 — score 6–7,5 | 1/30 | 2/30 | 0,00 | 0,00 | -1,02R | €-41,57 | 1,71% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_TP2_V1 | Rapida V1 — target pieno 2R | 2/30 | 2/30 | 0,00 | 0,00 | -1,05R | €-37,15 | 1,63% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V2 | Rapida 1H V2 | 2/30 | 2/30 | 0,59 | 1,07 | -0,31R | €1,44 | 0,93% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3 | Rapida 1H V3 Filtered — madre | 42/30 | 38/30 | 1,12 | 0,89 | 0,07R | €-2,45 | 2,89% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_1H_FAST_V3_CAP75_V1 | Rapida V3 — score <7,5 | 2/30 | 2/30 | 0,00 | 0,00 | -1,05R | €-41,57 | 1,71% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | Rapida V3 — qualità completa + profit lock | 1/30 | 0/30 | 0,00 | 0,00 | -1,09R | €0,00 | 1,03% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | Rapida V3 — Long + no HIGH + score <7,5 | 1/30 | 0/30 | 0,00 | 0,00 | -1,09R | €0,00 | 1,03% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | Rapida V3 — Long Only | 1/30 | 1/30 | 0,00 | 0,00 | -1,09R | €-4,22 | 0,84% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | Rapida V3 — no volatilità HIGH | 2/30 | 1/30 | 0,00 | 0,00 | -1,05R | €-78,08 | 1,84% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | Rapida V3 — senza ESPORTS | 2/30 | 2/30 | 0,00 | 0,00 | -1,05R | €-41,57 | 1,71% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_4H_WIDE | Ampia 4H | 33/30 | 12/30 | 0,87 | 1,27 | -0,10R | €7,39 | 2,08% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_BOLLINGER_MR_1H | Benchmark Bollinger mean reversion 1H | 23/30 | 15/30 | 0,86 | 1,66 | -0,09R | €10,14 | 2,06% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_BTC_ADAPTIVE_1H | Btc Adaptive 1H | 1/30 | 1/30 | 0,00 | 0,00 | -1,11R | €-54,55 | 0,89% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_ADAPTIVE_4H | Btc Adaptive 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,07% | n/a | RACCOLTA RESEARCH |
| SHADOW_BTC_BOLLINGER_1H | Btc Bollinger 1H | 1/30 | 1/30 | ∞ | ∞ | 1,37R | €68,69 | 0,31% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_BTC_BOLLINGER_4H | Btc Bollinger 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_BTC_DONCHIAN_1H | Btc Donchian 1H | 2/30 | 2/30 | 0,00 | 0,00 | -1,12R | €-55,16 | 1,49% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_DONCHIAN_4H | Btc Donchian 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,19% | n/a | RACCOLTA RESEARCH |
| SHADOW_BTC_EMA_1H | Btc Ema 1H | 2/30 | 2/30 | 0,00 | 0,00 | -1,11R | €-54,54 | 1,56% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_EMA_4H | Btc Ema 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,19% | n/a | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE | Combo Adaptive — madre | 58/30 | 16/30 | 1,62 | 2,08 | 0,35R | €15,39 | 1,27% | COERENTE + | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | Combo Adaptive — Long Only | 3/30 | 2/30 | 0,95 | 1,45 | -0,03R | €14,94 | 0,79% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | Combo Adaptive — MFE Trail esistente | 29/30 | 21/30 | 1,53 | 0,36 | 0,30R | €-14,40 | 3,44% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | Combo Adaptive — parziale 1R | 4/30 | 3/30 | 0,61 | 0,61 | -0,30R | €-15,86 | 0,96% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | Combo Adaptive — Quality7 + Regime + parziale 1R | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,32% | n/a | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | Combo Adaptive — Quality7 + Regime | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,32% | n/a | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | Combo Adaptive — Quality7 | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,32% | n/a | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | Combo Adaptive — Trend/Transition | 4/30 | 3/30 | 0,61 | 0,80 | -0,30R | €-8,28 | 0,89% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | Combo Adaptive — 75% a 2R + runner 3R | 3/30 | 1/30 | 0,00 | 0,00 | -1,05R | €-54,84 | 0,45% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | Combo Adaptive — target pieno 3R | 3/30 | 1/30 | 0,00 | 0,00 | -1,05R | €-54,84 | 0,45% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_MEAN_REVERSION | Combo Mean Reversion | 8/30 | 7/30 | 2,42 | 2,81 | 0,55R | €27,88 | 0,59% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_COMBO_SCANNER | Combo Scanner | 36/30 | 18/30 | 1,86 | 0,92 | 0,48R | €-2,11 | 2,00% | DIVERGENTE | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_COMBO_TREND | Combo Trend | 47/30 | 15/30 | 1,17 | 1,15 | 0,11R | €3,86 | 2,19% | COERENTE + | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_DOGE_BOLLINGER_1H | Doge Bollinger 1H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_DOGE_DONCHIAN_1H | Doge Donchian 1H | 1/30 | 2/30 | 0,00 | 0,46 | -1,12R | €-15,51 | 0,93% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_DOGE_EMA_1H | Doge Ema 1H | 1/30 | 4/30 | 0,00 | 0,54 | -1,11R | €-12,93 | 1,27% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_DONCHIAN_1H | Benchmark Donchian breakout 1H | 26/30 | 15/30 | 0,84 | 1,46 | -0,12R | €10,49 | 1,98% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_EMA_TREND_1H | Benchmark trend following EMA 1H | 51/30 | 9/30 | 1,13 | 0,77 | 0,09R | €-8,00 | 2,25% | DIVERGENTE | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_ETH_ADAPTIVE_1H | Eth Adaptive 1H | 2/30 | 2/30 | 1,70 | 0,05 | 0,39R | €-25,94 | 1,02% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_ETH_BOLLINGER_1H | Eth Bollinger 1H | 1/30 | 1/30 | 0,00 | ∞ | -1,13R | €15,45 | 0,51% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_ETH_DONCHIAN_1H | Eth Donchian 1H | 3/30 | 3/30 | 0,84 | 0,84 | -0,12R | €-5,82 | 1,38% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_EMA_1H | Eth Ema 1H | 2/30 | 4/30 | 1,70 | 0,05 | 0,39R | €-38,78 | 1,59% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_ETH_EMA_4H | Eth Ema 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,17% | n/a | RACCOLTA RESEARCH |
| SHADOW_GLOBAL_PURE | Global Confluence puro 1H | 1/30 | 7/30 | 0,00 | 0,17 | -1,10R | €-32,29 | 2,46% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | Master Adaptive Expanded V1 | 1/30 | 0/30 | 0,00 | 0,00 | -1,01R | €0,00 | 0,55% | n/a | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | Master Adaptive Gb20 V1 | 1/30 | 1/30 | 0,00 | ∞ | -1,01R | €10,11 | 0,75% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | Master Adaptive No Alt V1 | 1/30 | 0/30 | 0,00 | 0,00 | -1,01R | €0,00 | 0,55% | n/a | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | Master Adaptive Runner25 V1 | 1/30 | 0/30 | 0,00 | 0,00 | -1,01R | €0,00 | 0,55% | n/a | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | Master Adaptive Strict3 V1 | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,73% | n/a | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_V1 | Master Adaptive V1 | 1/30 | 0/30 | 0,00 | 0,00 | -1,01R | €0,00 | 0,55% | n/a | RACCOLTA RESEARCH |
| SHADOW_RELATIVE_STRENGTH | Forza relativa 1H V1 | 72/30 | 16/30 | 1,04 | 1,37 | 0,03R | €6,03 | 2,29% | COERENTE + | BOCCIATA RESEARCH |
| SHADOW_RELATIVE_STRENGTH_V2 | Forza relativa 1H V2 | 21/30 | 18/30 | 1,62 | 1,33 | 0,36R | €9,11 | 2,32% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT | Scanner Bottom 5 Short 1H | 24/30 | 13/30 | 0,55 | 0,38 | -0,32R | €-17,32 | 4,15% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC | Scanner Top 5 + forza BTC 1H | 39/30 | 17/30 | 1,87 | 2,37 | 0,47R | €22,75 | 1,62% | COERENTE + | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | Top 5 + BTC — BTC 2–3 | 2/30 | 1/30 | 0,00 | ∞ | -1,01R | €58,86 | 0,73% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | Top 5 + BTC — BTC≤3 | 2/30 | 1/30 | 0,00 | ∞ | -1,01R | €58,86 | 0,73% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | Top 5 + BTC — Guard + BTC≤3 + MFE | 2/30 | 2/30 | 0,00 | 0,00 | -1,01R | €-59,29 | 1,19% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | Top 5 + BTC — Guard + BTC≤3 | 2/30 | 2/30 | 0,00 | 0,00 | -1,01R | €-59,29 | 1,19% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | Top 5 + BTC — Guard + MFE | 2/30 | 2/30 | 0,00 | 0,00 | -1,01R | €-60,05 | 1,59% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | Top 5 + BTC — Guard | 2/30 | 2/30 | 0,00 | 0,00 | -1,01R | €-60,05 | 1,59% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | Top 5 + BTC — solo MFE | 2/30 | 1/30 | 0,00 | ∞ | -1,01R | €37,69 | 0,59% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | Top 5 + BTC — 75% a 2,2R + runner 3R | 2/30 | 1/30 | 0,00 | ∞ | -1,01R | €59,33 | 0,53% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | Top 5 + BTC — target pieno 3R | 2/30 | 1/30 | 0,00 | ∞ | -1,01R | €59,33 | 0,53% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_LONG | Scanner Top 5 Long 1H | 50/30 | 24/30 | 1,79 | 2,02 | 0,42R | €17,86 | 2,70% | COERENTE + | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_SOL_ADAPTIVE_1H | Sol Adaptive 1H | 2/30 | 2/30 | 1,70 | 0,67 | 0,39R | €-9,23 | 0,99% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SOL_ADAPTIVE_4H | Sol Adaptive 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,11% | n/a | RACCOLTA RESEARCH |
| SHADOW_SOL_BOLLINGER_1H | Sol Bollinger 1H | 1/30 | 1/30 | 0,00 | 0,00 | -1,13R | €-55,79 | 0,62% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_BOLLINGER_4H | Sol Bollinger 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,08% | n/a | RACCOLTA RESEARCH |
| SHADOW_SOL_DONCHIAN_1H | Sol Donchian 1H | 1/30 | 1/30 | 0,00 | 0,00 | -1,12R | €-4,49 | 0,55% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_DONCHIAN_4H | Sol Donchian 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,11% | n/a | RACCOLTA RESEARCH |
| SHADOW_SOL_EMA_1H | Sol Ema 1H | 2/30 | 2/30 | 1,70 | 0,83 | 0,39R | €-4,58 | 0,98% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SOL_EMA_4H | Sol Ema 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,11% | n/a | RACCOLTA RESEARCH |

Per le famiglie RSI con più configurazioni di leva o margine, il lato paper usa il conto con il maggior numero di eventi indipendenti; i conti duplicati non vengono aggregati.
`PRONTA PER REVISIONE LIVE` non invia ordini e non sposta capitale: abilita soltanto una revisione manuale finale.

## 🎯 DOGE Rejection Short — conto dedicato €3.600

Simulazione separata **paper only**: capitale/margine iniziale **€3.600**, leva **5x**, esposizione iniziale **€18.000**. Non modifica i conti paper da €10.000 e non invia ordini reali.

- Stato: **WAITING**
- Prezzo DOGE: **0.07371**
- Pre-allarme: **0.0765**; zona armata: **0.0775**; trigger rejection: **0.078**
- Invalidazione prima dell’entrata: chiusura 15m sopra **0.07966**

| Capitale iniziale | Balance | Equity | P&L aperto | Eventi chiusi | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- |
| €3.600,00 | €3.600,00 | €3.600,00 | €0,00 | 0 | 0,00% | 0,00 | 0,00% |

### Filtri correnti

| Filtro | Valore | Stato |
| --- | --- | --- |
| Dati mercato | FRESH | OK |
| Candela 15m | 23.7 min | OK |
| Global DOGE | -6.0 | OK |
| Classic raw | -11.0 | OK |
| DOGE/BTC raw | -6.0 | OK |
| Pattern ribassista | MATURO | OK |
| BTC sotto filtro | 66319.38 | NO |

### Ultima candela 15m valutata

- Rejection accettata: **NO**; motivo: **trigger_touched, entry_not_chased**
- High **0.07377**; close **0.07365**; wick alta **66.7%**; volume **x0.42**

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
- Confidenza: **79,90%**
- Volatilità: **NORMAL**
- Rotazione strategie: **SOLO OSSERVAZIONE — nessun peso operativo viene ancora modificato**
- Motivo: Trend BTC rialzista confermato dalla breadth: score +4.0, 75% sopra EMA50, ADX 26.5.
- BTC trend score: **4,00**; ADX: **26,46**; breadth sopra EMA50: **75,00%**
- Mediana alt vs BTC: **-0,49%**; dispersione: **16,76%**

- Aperti in questo ciclo: **6**
- Chiusi in questo ciclo: **2**
- Posizioni research aperte: **391**
- Trade research chiusi: **975**
- Eventi di mercato indipendenti chiusi: **359**
- Segnali sovrapposti saltati sullo stesso asset/profilo: **3726**
- Posizioni Research V1 senza regime scartate durante la migrazione: **28**

### Risultati complessivi per strategia

| Profilo | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| MAIN | 13 | 34 | 34 | 32,35% | 0,92 | -0,05R | €-18,10 |
| RSI_EXTREME_SHORT_15M | 1 | 5 | 5 | 20,00% | 0,32 | -0,55R | €-27,64 |
| Bilanciata 1H V1 | 15 | 113 | 113 | 34,51% | 1,00 | 0,00R | €2,71 |
| Bilanciata 1H V2 | 5 | 20 | 17 | 45,00% | 1,51 | 0,30R | €59,34 |
| Bilanciata 1H V3 Filtered | 10 | 31 | 31 | 41,94% | 1,35 | 0,21R | €66,06 |
| Rapida 1H V1 | 12 | 129 | 129 | 38,76% | 0,91 | -0,06R | €-75,14 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | 7 | 2 | 2 | 0,00% | 0,00 | -1,05R | €-21,08 |
| SHADOW_1H_FAST_NO_PEPE_V1 | 8 | 2 | 2 | 0,00% | 0,00 | -1,05R | €-21,08 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | 6 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,21 |
| SHADOW_1H_FAST_TP2_V1 | 9 | 2 | 2 | 0,00% | 0,00 | -1,05R | €-21,08 |
| Rapida 1H V2 | 0 | 3 | 2 | 33,33% | 0,59 | -0,31R | €-9,29 |
| Rapida 1H V3 Filtered | 11 | 42 | 42 | 45,24% | 1,12 | 0,07R | €29,72 |
| SHADOW_1H_FAST_V3_CAP75_V1 | 7 | 2 | 2 | 0,00% | 0,00 | -1,05R | €-21,08 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | 4 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,87 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | 4 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,87 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | 6 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,87 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | 7 | 2 | 2 | 0,00% | 0,00 | -1,05R | €-21,08 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | 8 | 2 | 2 | 0,00% | 0,00 | -1,05R | €-21,08 |
| SHADOW_4H_WIDE | 18 | 33 | 33 | 24,24% | 0,87 | -0,10R | €-32,97 |
| SHADOW_BOLLINGER_MR_1H | 1 | 23 | 23 | 39,13% | 0,86 | -0,09R | €-21,65 |
| SHADOW_BTC_ADAPTIVE_1H | 1 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_BTC_ADAPTIVE_4H | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_BOLLINGER_1H | 0 | 1 | 1 | 100,00% | ∞ | 1,37R | €13,67 |
| SHADOW_BTC_DONCHIAN_1H | 1 | 2 | 2 | 0,00% | 0,00 | -1,12R | €-22,50 |
| SHADOW_BTC_DONCHIAN_4H | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_EMA_1H | 1 | 2 | 2 | 0,00% | 0,00 | -1,11R | €-22,22 |
| SHADOW_BTC_EMA_4H | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_ADAPTIVE | 15 | 58 | 58 | 46,55% | 1,62 | 0,35R | €201,22 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | 7 | 3 | 3 | 33,33% | 0,95 | -0,03R | €-1,01 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | 11 | 29 | 29 | 44,83% | 1,53 | 0,30R | €87,53 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | 9 | 4 | 4 | 25,00% | 0,61 | -0,30R | €-12,13 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | 9 | 4 | 4 | 25,00% | 0,61 | -0,30R | €-12,13 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | 9 | 3 | 3 | 0,00% | 0,00 | -1,05R | €-31,38 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | 9 | 3 | 3 | 0,00% | 0,00 | -1,05R | €-31,38 |
| SHADOW_COMBO_MEAN_REVERSION | 0 | 8 | 8 | 62,50% | 2,42 | 0,55R | €44,38 |
| SHADOW_COMBO_SCANNER | 9 | 36 | 36 | 47,22% | 1,86 | 0,48R | €171,25 |
| SHADOW_COMBO_TREND | 13 | 47 | 47 | 36,17% | 1,17 | 0,11R | €53,30 |
| SHADOW_DOGE_DONCHIAN_1H | 0 | 1 | 1 | 0,00% | 0,00 | -1,12R | €-11,25 |
| SHADOW_DOGE_EMA_1H | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_DONCHIAN_1H | 9 | 26 | 26 | 26,92% | 0,84 | -0,12R | €-31,83 |
| SHADOW_EMA_TREND_1H | 16 | 51 | 51 | 35,29% | 1,13 | 0,09R | €43,52 |
| SHADOW_ETH_ADAPTIVE_1H | 1 | 2 | 2 | 50,00% | 1,70 | 0,39R | €7,78 |
| SHADOW_ETH_BOLLINGER_1H | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,33 |
| SHADOW_ETH_DONCHIAN_1H | 0 | 3 | 3 | 33,33% | 0,84 | -0,12R | €-3,61 |
| SHADOW_ETH_EMA_1H | 1 | 2 | 2 | 50,00% | 1,70 | 0,39R | €7,78 |
| SHADOW_ETH_EMA_4H | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_GLOBAL_PURE | 1 | 1 | 1 | 0,00% | 0,00 | -1,10R | €-11,00 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | 5 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | 5 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | 5 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | 5 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | 6 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_MASTER_ADAPTIVE_V1 | 5 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| Forza relativa 1H V1 | 14 | 72 | 72 | 33,33% | 1,04 | 0,03R | €22,09 |
| Forza relativa 1H V2 | 5 | 23 | 21 | 43,48% | 1,62 | 0,36R | €83,73 |
| SHADOW_SCANNER_BOTTOM5_SHORT | 5 | 24 | 24 | 20,83% | 0,55 | -0,32R | €-77,37 |
| SHADOW_SCANNER_TOP5_BTC | 8 | 39 | 39 | 46,15% | 1,87 | 0,47R | €181,81 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | 4 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | 4 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | 2 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | 2 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | 7 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | 6 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | 6 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_LONG | 9 | 50 | 50 | 48,00% | 1,79 | 0,42R | €208,18 |
| SHADOW_SOL_ADAPTIVE_1H | 1 | 2 | 2 | 50,00% | 1,70 | 0,39R | €7,78 |
| SHADOW_SOL_ADAPTIVE_4H | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SOL_BOLLINGER_1H | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,33 |
| SHADOW_SOL_BOLLINGER_4H | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SOL_DONCHIAN_1H | 1 | 1 | 1 | 0,00% | 0,00 | -1,12R | €-11,25 |
| SHADOW_SOL_DONCHIAN_4H | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SOL_EMA_1H | 1 | 2 | 2 | 50,00% | 1,70 | 0,39R | €7,78 |
| SHADOW_SOL_EMA_4H | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |

### Matrice strategia × regime all’entrata

| Profilo | Regime entrata | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| MAIN | ALT_ROTATION_UP | 3 | 3 | 3 | 0,00% | 0,00 | -1,01R | €-30,40 |
| MAIN | RANGE | 0 | 14 | 14 | 28,57% | 0,77 | -0,17R | €-23,82 |
| MAIN | RANGE_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| MAIN | TRANSITION | 4 | 4 | 4 | 25,00% | 0,65 | -0,27R | €-10,68 |
| MAIN | TREND_UP | 3 | 9 | 9 | 44,44% | 1,52 | 0,30R | €27,33 |
| MAIN | TREND_UP_HIGH_VOL | 3 | 3 | 3 | 33,33% | 0,98 | -0,01R | €-0,40 |
| RSI_EXTREME_SHORT_15M | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,90 |
| RSI_EXTREME_SHORT_15M | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -0,41R | €-4,13 |
| RSI_EXTREME_SHORT_15M | TREND_UP | 1 | 3 | 3 | 33,33% | 0,50 | -0,42R | €-12,61 |
| Bilanciata 1H V1 | ALT_ROTATION_UP | 0 | 13 | 13 | 53,85% | 2,16 | 0,56R | €72,85 |
| Bilanciata 1H V1 | RANGE | 2 | 26 | 26 | 30,77% | 0,86 | -0,10R | €-25,88 |
| Bilanciata 1H V1 | RANGE_HIGH_VOL | 1 | 10 | 10 | 0,00% | 0,00 | -1,07R | €-107,38 |
| Bilanciata 1H V1 | TRANSITION | 2 | 25 | 25 | 32,00% | 0,90 | -0,07R | €-17,37 |
| Bilanciata 1H V1 | TREND_UP | 5 | 31 | 31 | 41,94% | 1,42 | 0,24R | €75,22 |
| Bilanciata 1H V1 | TREND_UP_HIGH_VOL | 5 | 8 | 8 | 37,50% | 1,10 | 0,07R | €5,26 |
| Bilanciata 1H V2 | ALT_ROTATION_UP | 1 | 4 | 3 | 100,00% | ∞ | 1,93R | €77,01 |
| Bilanciata 1H V2 | RANGE | 1 | 5 | 4 | 40,00% | 1,19 | 0,13R | €6,40 |
| Bilanciata 1H V2 | TRANSITION | 3 | 11 | 10 | 27,27% | 0,71 | -0,22R | €-24,07 |
| Bilanciata 1H V3 Filtered | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| Bilanciata 1H V3 Filtered | RANGE_HIGH_VOL | 1 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| Bilanciata 1H V3 Filtered | TRANSITION | 0 | 6 | 6 | 33,33% | 0,92 | -0,06R | €-3,44 |
| Bilanciata 1H V3 Filtered | TREND_UP | 2 | 16 | 16 | 56,25% | 2,43 | 0,65R | €103,45 |
| Bilanciata 1H V3 Filtered | TREND_UP_HIGH_VOL | 7 | 7 | 7 | 28,57% | 0,74 | -0,20R | €-13,68 |
| Rapida 1H V1 | ALT_ROTATION_UP | 1 | 9 | 9 | 55,56% | 1,73 | 0,34R | €30,84 |
| Rapida 1H V1 | RANGE | 0 | 35 | 35 | 40,00% | 1,04 | 0,02R | €8,01 |
| Rapida 1H V1 | RANGE_HIGH_VOL | 0 | 11 | 11 | 0,00% | 0,00 | -1,09R | €-119,90 |
| Rapida 1H V1 | TRANSITION | 0 | 23 | 23 | 43,48% | 1,20 | 0,11R | €24,41 |
| Rapida 1H V1 | TREND_UP | 5 | 36 | 36 | 44,44% | 1,09 | 0,05R | €19,09 |
| Rapida 1H V1 | TREND_UP_HIGH_VOL | 6 | 15 | 15 | 33,33% | 0,65 | -0,25R | €-37,60 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TREND_UP | 7 | 2 | 2 | 0,00% | 0,00 | -1,05R | €-21,08 |
| SHADOW_1H_FAST_NO_PEPE_V1 | ALT_ROTATION_UP | 3 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_UP | 5 | 2 | 2 | 0,00% | 0,00 | -1,05R | €-21,08 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | ALT_ROTATION_UP | 3 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_UP | 3 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,21 |
| SHADOW_1H_FAST_TP2_V1 | ALT_ROTATION_UP | 3 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_1H_FAST_TP2_V1 | TREND_UP | 6 | 2 | 2 | 0,00% | 0,00 | -1,05R | €-21,08 |
| Rapida 1H V2 | RANGE | 0 | 2 | 1 | 50,00% | 1,19 | 0,11R | €2,14 |
| Rapida 1H V2 | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -1,14R | €-11,43 |
| Rapida 1H V3 Filtered | ALT_ROTATION_UP | 1 | 2 | 2 | 100,00% | ∞ | 1,44R | €28,86 |
| Rapida 1H V3 Filtered | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| Rapida 1H V3 Filtered | TRANSITION | 0 | 5 | 5 | 40,00% | 0,91 | -0,06R | €-2,77 |
| Rapida 1H V3 Filtered | TREND_UP | 4 | 20 | 20 | 55,00% | 1,70 | 0,33R | €65,12 |
| Rapida 1H V3 Filtered | TREND_UP_HIGH_VOL | 6 | 14 | 14 | 28,57% | 0,52 | -0,37R | €-51,36 |
| SHADOW_1H_FAST_V3_CAP75_V1 | ALT_ROTATION_UP | 3 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_UP | 4 | 2 | 2 | 0,00% | 0,00 | -1,05R | €-21,08 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TREND_UP | 4 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,87 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TREND_UP | 4 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,87 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | ALT_ROTATION_UP | 3 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_UP | 3 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,87 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TREND_UP | 7 | 2 | 2 | 0,00% | 0,00 | -1,05R | €-21,08 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | ALT_ROTATION_UP | 3 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_UP | 5 | 2 | 2 | 0,00% | 0,00 | -1,05R | €-21,08 |
| SHADOW_4H_WIDE | ALT_ROTATION_UP | 1 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_4H_WIDE | RANGE | 3 | 14 | 14 | 21,43% | 0,74 | -0,21R | €-29,68 |
| SHADOW_4H_WIDE | TRANSITION | 5 | 5 | 5 | 20,00% | 0,69 | -0,25R | €-12,67 |
| SHADOW_4H_WIDE | TREND_UP | 5 | 8 | 8 | 50,00% | 2,70 | 0,88R | €70,18 |
| SHADOW_4H_WIDE | TREND_UP_HIGH_VOL | 4 | 4 | 4 | 0,00% | 0,00 | -1,01R | €-40,53 |
| SHADOW_BOLLINGER_MR_1H | ALT_ROTATION_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,02R | €-20,30 |
| SHADOW_BOLLINGER_MR_1H | RANGE | 0 | 7 | 7 | 42,86% | 0,98 | -0,01R | €-0,83 |
| SHADOW_BOLLINGER_MR_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_BOLLINGER_MR_1H | TRANSITION | 0 | 3 | 3 | 33,33% | 0,71 | -0,20R | €-6,14 |
| SHADOW_BOLLINGER_MR_1H | TREND_UP | 1 | 8 | 8 | 37,50% | 0,77 | -0,16R | €-12,56 |
| SHADOW_BOLLINGER_MR_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,31 | 0,17R | €3,31 |
| SHADOW_BTC_ADAPTIVE_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_BTC_ADAPTIVE_1H | TREND_UP_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_ADAPTIVE_4H | TREND_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_BOLLINGER_1H | RANGE | 0 | 1 | 1 | 100,00% | ∞ | 1,37R | €13,67 |
| SHADOW_BTC_DONCHIAN_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,12R | €-11,25 |
| SHADOW_BTC_DONCHIAN_1H | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -1,12R | €-11,25 |
| SHADOW_BTC_DONCHIAN_1H | TREND_UP_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_DONCHIAN_4H | TREND_UP_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_EMA_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_BTC_EMA_1H | TREND_UP_HIGH_VOL | 1 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_BTC_EMA_4H | TREND_UP_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_ADAPTIVE | ALT_ROTATION_UP | 1 | 3 | 3 | 33,33% | 0,94 | -0,04R | €-1,21 |
| SHADOW_COMBO_ADAPTIVE | RANGE | 2 | 10 | 10 | 30,00% | 0,77 | -0,18R | €-17,90 |
| SHADOW_COMBO_ADAPTIVE | RANGE_HIGH_VOL | 1 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE | TRANSITION | 2 | 15 | 15 | 53,33% | 2,13 | 0,55R | €82,64 |
| SHADOW_COMBO_ADAPTIVE | TREND_UP | 3 | 23 | 23 | 56,52% | 2,44 | 0,65R | €150,35 |
| SHADOW_COMBO_ADAPTIVE | TREND_UP_HIGH_VOL | 6 | 6 | 6 | 33,33% | 0,94 | -0,04R | €-2,53 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | ALT_ROTATION_UP | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_UP | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_UP_HIGH_VOL | 3 | 3 | 3 | 33,33% | 0,95 | -0,03R | €-1,01 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | ALT_ROTATION_UP | 1 | 4 | 4 | 25,00% | 0,61 | -0,31R | €-12,32 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE_HIGH_VOL | 1 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,91R | €19,12 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_UP | 3 | 15 | 15 | 60,00% | 2,88 | 0,77R | €115,46 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_UP_HIGH_VOL | 6 | 8 | 8 | 25,00% | 0,61 | -0,31R | €-24,59 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | ALT_ROTATION_UP | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_UP | 4 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_UP_HIGH_VOL | 3 | 4 | 4 | 25,00% | 0,61 | -0,30R | €-12,13 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TREND_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TREND_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TREND_UP | 5 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TREND_UP_HIGH_VOL | 4 | 4 | 4 | 25,00% | 0,61 | -0,30R | €-12,13 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_UP | 4 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | TREND_UP | 4 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | TREND_UP_HIGH_VOL | 1 | 3 | 3 | 0,00% | 0,00 | -1,05R | €-31,38 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | ALT_ROTATION_UP | 4 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | TREND_UP | 4 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | TREND_UP_HIGH_VOL | 1 | 3 | 3 | 0,00% | 0,00 | -1,05R | €-31,38 |
| SHADOW_COMBO_MEAN_REVERSION | RANGE | 0 | 4 | 4 | 75,00% | 4,46 | 0,88R | €35,25 |
| SHADOW_COMBO_MEAN_REVERSION | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,94 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_UP | 0 | 2 | 2 | 50,00% | 1,50 | 0,25R | €5,04 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,85 |
| SHADOW_COMBO_SCANNER | ALT_ROTATION_UP | 0 | 3 | 3 | 66,67% | 4,32 | 1,12R | €33,60 |
| SHADOW_COMBO_SCANNER | RANGE | 1 | 1 | 1 | 100,00% | ∞ | 2,19R | €21,87 |
| SHADOW_COMBO_SCANNER | RANGE_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_SCANNER | TRANSITION | 1 | 11 | 11 | 36,36% | 1,20 | 0,13R | €14,31 |
| SHADOW_COMBO_SCANNER | TREND_UP | 0 | 18 | 18 | 50,00% | 2,05 | 0,55R | €99,87 |
| SHADOW_COMBO_SCANNER | TREND_UP_HIGH_VOL | 6 | 3 | 3 | 33,33% | 1,08 | 0,05R | €1,60 |
| SHADOW_COMBO_TREND | ALT_ROTATION_UP | 1 | 2 | 2 | 50,00% | 2,16 | 0,59R | €11,73 |
| SHADOW_COMBO_TREND | RANGE | 0 | 8 | 8 | 12,50% | 0,29 | -0,67R | €-53,33 |
| SHADOW_COMBO_TREND | RANGE_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_TREND | TRANSITION | 2 | 13 | 13 | 46,15% | 1,77 | 0,44R | €56,72 |
| SHADOW_COMBO_TREND | TREND_UP | 3 | 19 | 19 | 42,11% | 1,50 | 0,30R | €57,72 |
| SHADOW_COMBO_TREND | TREND_UP_HIGH_VOL | 6 | 5 | 5 | 20,00% | 0,53 | -0,39R | €-19,53 |
| SHADOW_DOGE_DONCHIAN_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,12R | €-11,25 |
| SHADOW_DOGE_EMA_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_DONCHIAN_1H | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_DONCHIAN_1H | RANGE | 0 | 8 | 8 | 12,50% | 0,32 | -0,64R | €-51,15 |
| SHADOW_DONCHIAN_1H | RANGE_HIGH_VOL | 1 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_DONCHIAN_1H | TRANSITION | 1 | 6 | 6 | 16,67% | 0,45 | -0,48R | €-28,95 |
| SHADOW_DONCHIAN_1H | TREND_UP | 1 | 10 | 10 | 50,00% | 2,27 | 0,69R | €68,53 |
| SHADOW_DONCHIAN_1H | TREND_UP_HIGH_VOL | 6 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_EMA_TREND_1H | ALT_ROTATION_UP | 1 | 2 | 2 | 50,00% | 2,16 | 0,59R | €11,73 |
| SHADOW_EMA_TREND_1H | RANGE | 2 | 8 | 8 | 12,50% | 0,29 | -0,66R | €-52,47 |
| SHADOW_EMA_TREND_1H | RANGE_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_EMA_TREND_1H | TRANSITION | 2 | 13 | 13 | 46,15% | 1,77 | 0,44R | €56,70 |
| SHADOW_EMA_TREND_1H | TREND_UP | 3 | 24 | 24 | 37,50% | 1,23 | 0,15R | €36,08 |
| SHADOW_EMA_TREND_1H | TREND_UP_HIGH_VOL | 7 | 4 | 4 | 25,00% | 0,72 | -0,21R | €-8,53 |
| SHADOW_ETH_ADAPTIVE_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_ETH_ADAPTIVE_1H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,89R | €18,89 |
| SHADOW_ETH_ADAPTIVE_1H | TREND_UP_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_ETH_BOLLINGER_1H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,33 |
| SHADOW_ETH_DONCHIAN_1H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_ETH_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,68 | 0,38R | €7,64 |
| SHADOW_ETH_EMA_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_ETH_EMA_1H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,89R | €18,89 |
| SHADOW_ETH_EMA_1H | TREND_UP_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_ETH_EMA_4H | TREND_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_GLOBAL_PURE | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,10R | €-11,00 |
| SHADOW_GLOBAL_PURE | TRANSITION | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TREND_UP | 5 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TREND_UP | 5 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TREND_UP | 5 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | TREND_UP | 5 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TREND_UP | 6 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_MASTER_ADAPTIVE_V1 | TREND_UP | 5 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| Forza relativa 1H V1 | ALT_ROTATION_UP | 2 | 10 | 10 | 30,00% | 0,88 | -0,09R | €-8,74 |
| Forza relativa 1H V1 | RANGE | 2 | 18 | 18 | 22,22% | 0,59 | -0,33R | €-60,04 |
| Forza relativa 1H V1 | RANGE_HIGH_VOL | 1 | 2 | 2 | 0,00% | 0,00 | -1,02R | €-20,33 |
| Forza relativa 1H V1 | TRANSITION | 1 | 12 | 12 | 50,00% | 2,12 | 0,57R | €68,69 |
| Forza relativa 1H V1 | TREND_UP | 7 | 22 | 22 | 45,45% | 1,75 | 0,43R | €93,66 |
| Forza relativa 1H V1 | TREND_UP_HIGH_VOL | 1 | 8 | 8 | 12,50% | 0,30 | -0,64R | €-51,15 |
| Forza relativa 1H V2 | ALT_ROTATION_UP | 1 | 1 | 1 | 100,00% | ∞ | 2,10R | €21,00 |
| Forza relativa 1H V2 | RANGE | 1 | 2 | 2 | 50,00% | 2,16 | 0,59R | €11,72 |
| Forza relativa 1H V2 | TRANSITION | 2 | 8 | 8 | 37,50% | 1,26 | 0,17R | €13,67 |
| Forza relativa 1H V2 | TREND_UP | 1 | 8 | 7 | 62,50% | 3,60 | 0,99R | €78,93 |
| Forza relativa 1H V2 | TREND_UP_HIGH_VOL | 0 | 4 | 3 | 0,00% | 0,00 | -1,04R | €-41,60 |
| SHADOW_SCANNER_BOTTOM5_SHORT | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| SHADOW_SCANNER_BOTTOM5_SHORT | RANGE | 0 | 7 | 7 | 0,00% | 0,00 | -1,08R | €-75,76 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TRANSITION | 2 | 10 | 10 | 40,00% | 1,37 | 0,20R | €20,38 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP | 2 | 4 | 4 | 0,00% | 0,00 | -0,52R | €-20,61 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP_HIGH_VOL | 1 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,24 |
| SHADOW_SCANNER_TOP5_BTC | ALT_ROTATION_UP | 0 | 4 | 4 | 50,00% | 2,12 | 0,58R | €23,08 |
| SHADOW_SCANNER_TOP5_BTC | RANGE | 1 | 4 | 4 | 75,00% | 102,98 | 1,59R | €63,66 |
| SHADOW_SCANNER_TOP5_BTC | RANGE_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC | TRANSITION | 0 | 11 | 11 | 36,36% | 1,20 | 0,13R | €14,31 |
| SHADOW_SCANNER_TOP5_BTC | TREND_UP | 0 | 17 | 17 | 47,06% | 1,84 | 0,47R | €79,16 |
| SHADOW_SCANNER_TOP5_BTC | TREND_UP_HIGH_VOL | 6 | 3 | 3 | 33,33% | 1,08 | 0,05R | €1,60 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TREND_UP_HIGH_VOL | 4 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_UP_HIGH_VOL | 4 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_UP | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_UP | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_UP_HIGH_VOL | 7 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | ALT_ROTATION_UP | 4 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_UP_HIGH_VOL | 1 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | ALT_ROTATION_UP | 4 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_UP_HIGH_VOL | 1 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_LONG | ALT_ROTATION_UP | 0 | 5 | 5 | 40,00% | 1,24 | 0,15R | €7,55 |
| SHADOW_SCANNER_TOP5_LONG | RANGE | 1 | 5 | 5 | 80,00% | 125,19 | 1,55R | €77,53 |
| SHADOW_SCANNER_TOP5_LONG | RANGE_HIGH_VOL | 1 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_LONG | TRANSITION | 0 | 11 | 11 | 36,36% | 1,09 | 0,06R | €6,31 |
| SHADOW_SCANNER_TOP5_LONG | TREND_UP | 2 | 24 | 24 | 50,00% | 1,85 | 0,45R | €108,60 |
| SHADOW_SCANNER_TOP5_LONG | TREND_UP_HIGH_VOL | 5 | 4 | 4 | 50,00% | 1,88 | 0,46R | €18,33 |
| SHADOW_SOL_ADAPTIVE_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_SOL_ADAPTIVE_1H | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,89R | €18,89 |
| SHADOW_SOL_ADAPTIVE_1H | TREND_UP_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SOL_ADAPTIVE_4H | TREND_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SOL_BOLLINGER_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,33 |
| SHADOW_SOL_BOLLINGER_4H | TREND_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SOL_DONCHIAN_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,12R | €-11,25 |
| SHADOW_SOL_DONCHIAN_1H | TREND_UP_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SOL_DONCHIAN_4H | TREND_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SOL_EMA_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_SOL_EMA_1H | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,89R | €18,89 |
| SHADOW_SOL_EMA_1H | TREND_UP_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SOL_EMA_4H | TREND_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |

Il P&L è normalizzato a **€10 di rischio per evento**, così leva e size non falsano il confronto.
La matrice diventerà utilizzabile per una rotazione automatica soltanto dopo un campione sufficiente per ciascuna coppia strategia-regime.

# Block 3 — Shadow Exit Engine

Generato: 2026-07-21T12:08:40+00:00

> Motore esclusivamente osservativo e Paper-only. Non modifica le uscite reali. I confronti escludono il funding sia dall'uscita originale sia dalle varianti.

## Stato operativo

- Gruppi di trade ancora monitorati: **197**
- Scenari virtuali ancora attivi: **2746**
- Gruppi in attesa dell'uscita originale: **161**
- Gruppi con originale chiuso ma Shadow ancora attive: **36**
- Confronti completati: **3501**

## Classifica osservativa complessiva

| Scenario | Campione completo | Campione totale | Δ medio vs originale | Migliora | Troppo presto | Troppo tardi | Stato dati |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| GB20_R050 | 144 | 182 | +€11,89 | 52,2% | 36 | 0 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R050 | 144 | 182 | +€10,11 | 51,6% | 36 | 1 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R050 | 144 | 182 | +€7,86 | 50,5% | 37 | 2 | READY_FOR_BLOCK4_EVALUATION |
| TP_R050 | 144 | 182 | +€7,05 | 52,2% | 36 | 0 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R050 | 144 | 182 | +€5,47 | 50,0% | 33 | 7 | READY_FOR_BLOCK4_EVALUATION |
| GB20_R100 | 143 | 181 | +€9,71 | 49,7% | 31 | 3 | READY_FOR_BLOCK4_EVALUATION |
| TP_R100 | 143 | 181 | +€7,80 | 49,2% | 32 | 3 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R100 | 143 | 181 | +€7,45 | 48,1% | 32 | 5 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R100 | 143 | 181 | +€4,99 | 48,6% | 23 | 11 | READY_FOR_BLOCK4_EVALUATION |
| BE_R050 | 141 | 179 | €-10,09 | 33,0% | 36 | 19 | READY_FOR_BLOCK4_EVALUATION |
| TIME_6H | 139 | 184 | +€0,31 | 51,6% | 35 | 11 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R100 | 132 | 170 | +€4,19 | 47,6% | 15 | 17 | READY_FOR_BLOCK4_EVALUATION |
| TP_R200 | 130 | 168 | +€7,41 | 41,1% | 9 | 23 | READY_FOR_BLOCK4_EVALUATION |
| TIME_12H | 130 | 175 | +€5,25 | 45,7% | 20 | 20 | READY_FOR_BLOCK4_EVALUATION |
| TP_R150 | 130 | 168 | +€2,05 | 36,9% | 20 | 20 | READY_FOR_BLOCK4_EVALUATION |
| ATR15_R100 | 128 | 166 | €-2,71 | 40,4% | 7 | 25 | READY_FOR_BLOCK4_EVALUATION |
| ATR20_R100 | 128 | 166 | €-3,55 | 39,8% | 4 | 28 | READY_FOR_BLOCK4_EVALUATION |
| ATR30_R100 | 127 | 164 | €-14,16 | 31,7% | 3 | 40 | READY_FOR_BLOCK4_EVALUATION |
| BE_R100 | 127 | 164 | €-14,40 | 31,7% | 2 | 41 | READY_FOR_BLOCK4_EVALUATION |
| TIME_24H | 118 | 163 | €-1,04 | 39,9% | 11 | 31 | READY_FOR_BLOCK4_EVALUATION |

## Come leggere il controllo

- **EARLIER_BETTER**: la variante è uscita prima e ha conservato più profitto.
- **TOO_EARLY**: la variante è uscita prima ma ha tagliato un movimento migliore.
- **LATER_BETTER**: la variante ha continuato dopo l'uscita originale e ha guadagnato di più.
- **TOO_LATE**: la variante è rimasta aperta più a lungo e ha peggiorato il risultato.

## Limiti e protezioni

Le regole Shadow mantengono entrata, quantità, commissioni, stop protettivo iniziale e liquidazione. Le ambiguità all'interno della stessa candela vengono risolte scegliendo l'esito peggiore. Le posizioni già aperte al momento dell'installazione sono marcate come campione parziale e non saranno utilizzate dal futuro Blocco 4 come prova piena.

# Blocco 4 — Valutazione statistica Shadow

Generato: 2026-07-21T12:08:41+00:00

> Modulo esclusivamente valutativo. Non modifica strategie, uscite, posizioni o capitale. Le candidature vengono consegnate al futuro Blocco 5, senza applicazione automatica.

## Stato

- Risultati Block 3 disponibili: **3501**
- Valutazioni prodotte: **2665**
- Candidature al Blocco 5: **0**
- Mutazioni create automaticamente: **0**

## Classifica complessiva

| Scenario | Campione pieno | Δ medio (R) | Mediana (R) | CI bootstrap basso | Migliora | Score | Stato |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| TIME_6H | 133 | 0,073 | 0,036 | -0,023 | 60,2% | 86,3 | VALIDATING |
| GB20_R050 | 138 | 0,321 | 0,068 | 0,173 | 53,6% | 83,7 | VALIDATING |
| TP_R050 | 138 | 0,238 | 0,075 | 0,096 | 53,6% | 83,6 | VALIDATING |
| GB30_R050 | 138 | 0,294 | 0,068 | 0,164 | 52,9% | 83,0 | VALIDATING |
| GB40_R050 | 138 | 0,250 | 0,068 | 0,101 | 52,9% | 83,0 | VALIDATING |
| GB50_R050 | 138 | 0,205 | 0,060 | 0,077 | 52,9% | 82,3 | VALIDATING |
| GB20_R100 | 137 | 0,226 | 0,033 | 0,109 | 51,1% | 80,6 | VALIDATING |
| GB50_R100 | 126 | 0,161 | 0,033 | 0,066 | 50,8% | 80,0 | VALIDATING |
| GB40_R100 | 137 | 0,152 | 0,033 | 0,054 | 50,4% | 79,8 | VALIDATING |
| TIME_24H | 6 | 0,997 | 1,104 | 0,180 | 66,7% | 74,1 | INSUFFICIENT_DATA |
| TP_R200 | 124 | 0,139 | 0,000 | 0,027 | 43,5% | 73,0 | VALIDATING |
| GB30_R100 | 137 | 0,193 | 0,000 | 0,085 | 49,6% | 69,5 | VALIDATING |
| TP_R100 | 137 | 0,205 | 0,000 | 0,091 | 49,6% | 69,5 | VALIDATING |
| TIME_12H | 124 | 0,154 | 0,000 | 0,049 | 49,2% | 68,3 | VALIDATING |
| TP_R200 | 6 | 0,472 | 0,250 | -0,017 | 50,0% | 58,7 | INSUFFICIENT_DATA |
| TP_R150 | 124 | 0,034 | 0,000 | -0,060 | 38,7% | 56,5 | VALIDATING |
| ATR15_R100 | 122 | 0,020 | 0,000 | -0,064 | 42,6% | 51,2 | VALIDATING |
| ATR20_R100 | 122 | -0,015 | 0,000 | -0,122 | 41,8% | 39,3 | VALIDATING |
| BE_R050 | 135 | -0,093 | 0,000 | -0,247 | 40,0% | 38,2 | VALIDATING |
| TIME_24H | 112 | -0,081 | 0,000 | -0,286 | 39,3% | 34,2 | VALIDATING |

## Stati di evidenza

- **INSUFFICIENT_DATA**: meno di 30 trade completi.
- **EARLY_SIGNAL**: da 30 a 49 trade completi.
- **VALIDATING**: campione maggiore, ma robustezza non ancora dimostrata.
- **ROBUST**: test di effetto, stabilità, qualità e outlier superati.
- **ELIGIBLE_FOR_MUTATION**: evidenza sufficiente per proporre una variante al Blocco 5.
- **UNDERPERFORMING**: intervallo statistico stabilmente negativo.

## Protezioni statistiche

Sono utilizzati solo trade osservati integralmente dall'entrata. Il controllo comprende media e mediana normalizzate per rischio, media tagliata, bootstrap deterministico, quattro segmenti temporali, concentrazione dei migliori outlier, ambiguità intrabar e gap di candele.

# Blocco 4.5 — Crash Cascade Guard

Generato: 2026-07-21T12:08:34+00:00

> Paper-only. In mercato NORMAL/WATCH non riduce i segnali. Le limitazioni iniziano soltanto in STRESS, RECOVERY, CRASH, EXTREME o con dati non affidabili.

## Stato corrente

- Livello: **NORMAL**
- Direzione: **NONE**
- Segnali bloccati nel ciclo: **0**
- Simulazioni bloccate attive: **1**
- Simulazioni completate nel ciclo: **0**
- Liquidazioni virtuali evitate totali: **0**
- Valore cumulato del filtro: **6.06 R**
- Profitto virtuale mancato: **0.00 R**

## Stress test portafogli Paper

| Scenario | Posizioni interessate | Liquidazioni stimate | Perdita stimata EUR |
| --- | ---: | ---: | ---: |
| DOWN_10 | 123 | 0 | 34871.01 |
| DOWN_20 | 123 | 0 | 69742.02 |
| DOWN_30 | 123 | 0 | 104613.02 |
| DOWN_40 | 123 | 46 | 128336.45 |
| UP_10 | 35 | 0 | 2759.67 |
| UP_20 | 35 | 0 | 5519.33 |
| UP_30 | 35 | 0 | 8279.00 |
| UP_40 | 35 | 16 | 10301.79 |

## Modello di esecuzione

Se una candela di cascata attraversa nello stesso intervallo sia lo stop sia il prezzo di liquidazione, il Paper usa il caso peggiore e registra una liquidazione intrabar. Gli stop in gap o in regime di stress ricevono slippage aggiuntivo.

## Requisiti prima del live futures

- modalità ISOLATED obbligatoria;
- stop nativo sull'exchange;
- conferma dello stop prima di accettare la posizione;
- cross margin vietato.

# Blocco 5 — Candidati evolutivi controllati

Generato: 2026-07-21T12:08:12+00:00

> Paper-only. Nessuna promozione, sostituzione del MASTER, modifica live o ordine reale.

## Stato

- Candidati attivi: **0**
- Nuovi candidati nel ciclo: **0**
- Evidenze rifiutate nel ciclo: **0**
- Promozioni automatiche: **0**
- Pensionamenti automatici: **0**

## Regola di mutazione

Ogni candidato è una copia indipendente del genitore e cambia un solo parametro scalare. Il file principale paper_trading_config.json non viene riscritto.

## Candidati attivi

| Candidato | Genitore | Parametro | Vecchio | Nuovo | Scenario |
| --- | --- | --- | ---: | ---: | --- |
| — | — | — | — | — | — |

## Vincoli v1

- Supportati: FIXED_R, TIME_EXIT e ATR_TRAIL solo quando richiede una singola variazione.
- MFE_GIVEBACK e BREAKEVEN non vengono approssimati: restano evidenze da implementare in una versione successiva.
- Nessun candidato può diventare MASTER nel Blocco 5.

# Blocco 6 — Validazione Champion/Challenger

Generato: 2026-07-21T12:08:43+00:00

> Paper-only. Confronto sulle stesse entrate tramite `experiment_group_id`. Nessuna promozione, sostituzione, pensione o modifica live automatica.

## Stato

- Candidati valutati: **0**
- Pronti per revisione promozione: **0**
- Promozioni automatiche: **0**
- Pensionamenti automatici: **0**

## Confronto

| Candidato | Genitore | Stato | Coppie | Δ medio R | CI basso | PF cand. | PF gen. | DD cand. | DD gen. | Score |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| — | — | Nessun candidato attivo | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

## Gate di sicurezza

- Solo trade chiusi dopo la creazione della candidata.
- Solo coppie con lo stesso evento d’ingresso.
- Solo dati `FULL_FROM_ENTRY` e risk model `block4_5_v1`.
- Campione, bootstrap, stabilità temporale, dipendenza dai migliori trade, PF, drawdown e liquidazioni.
- `PROMOTION_REVIEW_READY` è soltanto una raccomandazione: richiede approvazione umana e un blocco successivo.

# Blocco 7 — Governance promozioni Paper

Generato: 2026-07-21T12:08:43+00:00

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

Generato: 2026-07-21T12:08:43+00:00

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

Generato: 2026-07-21T12:08:43+00:00

> Paper-only. La memoria può bloccare soltanto una futura proposta Block 5 classificata AVOID; non modifica strategie esistenti.

## Stato

- Strategie/portafogli valutati: **62**
- Hall of Fame: **2**
- Memorie genetiche: **0**
- Firme bloccate: **0**
- Azioni automatiche e live: **0**

## Hall of Fame

| Rank | Strategia | Stato | Score | Grade | Trade | PF | Expectancy R | DD R |
| ---: | --- | --- | ---: | --- | ---: | ---: | ---: | ---: |
| 1 | SHADOW_1H_FAST_V3 | BASELINE | 7.1 | E | 38 | 0.89 | -0.048 | 5.36 |
| 2 | SHADOW_1H_FAST | BASELINE | 5.8 | E | 48 | 0.87 | -0.066 | 11.24 |

## Memoria genetica

| Scope | Famiglia | Mutazione | Target | Stato | Score | Prove | Coppie | Blocco |
| --- | --- | --- | --- | --- | ---: | ---: | ---: | --- |
| — | — | Nessuna candidata ancora creata | — | INSUFFICIENT | 0 | 0 | 0 | NO |

## Sicurezza

- Nessuna strategia, posizione o promozione esistente viene modificata.
- Nessuna mutazione, promozione, pensionamento o rollback automatico.
- Nessun effetto live e nessun ordine reale.

# Blocco 10 — Regime Fitness e specializzazione

Generato: 2026-07-21T12:08:43+00:00

> Paper-only e advisory. Il blocco misura quali strategie funzionano nei diversi regimi, ma non cambia automaticamente strategia o posizione.

## Stato

- Regime corrente: **RANGE**
- Righe di performance: **218**
- Strategie preferite nel regime corrente: **0**
- Strategie da evitare nel regime corrente: **0**
- Memorie contestuali: **109**
- Routing automatico: **NO**

## Classifica del regime corrente

| Rank | Portafoglio | Famiglia | Stato | Fitness | Trade | PF | Expectancy R | DD R |
| ---: | --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| 1 | SHADOW_DOGE_DONCHIAN_1H | shadow-doge-donchian-1h | INSUFFICIENT | 80.4 | 1 | 99.00 | 0.524 | 0.00 |
| 2 | SHADOW_BTC_BOLLINGER_1H | shadow-btc-bollinger-1h | INSUFFICIENT | 80.4 | 1 | 99.00 | 1.374 | 0.00 |
| 3 | SHADOW_ETH_BOLLINGER_1H | shadow-eth-bollinger-1h | INSUFFICIENT | 76.6 | 1 | 99.00 | 0.309 | 0.00 |
| 4 | SHADOW_COMBO_MEAN_REVERSION | shadow-combo-mean-reversion | INSUFFICIENT | 75.5 | 5 | 4.40 | 0.709 | 1.02 |
| 5 | SHADOW_COMBO_ADAPTIVE | shadow-combo-adaptive | OBSERVING | 73.3 | 15 | 2.15 | 0.334 | 1.10 |
| 6 | SHADOW_MASTER_ADAPTIVE_GB20_V1 | shadow-master-adaptive-gb20-v1 | INSUFFICIENT | 72.2 | 1 | 99.00 | 0.202 | 0.00 |
| 7 | SHADOW_SCANNER_TOP5_BTC | shadow-scanner-top5-btc | OBSERVING | 72.0 | 15 | 2.06 | 0.375 | 3.09 |
| 8 | SHADOW_SCANNER_TOP5_LONG | shadow-scanner-top5-long | OBSERVING | 72.0 | 17 | 1.98 | 0.365 | 4.17 |
| 9 | SHADOW_1H_FAST_V2 | shadow-1h-fast-v2 | INSUFFICIENT | 70.6 | 2 | 11.45 | 0.628 | 0.12 |
| 10 | SHADOW_RELATIVE_STRENGTH_V2 | shadow-relative-strength-v2 | OBSERVING | 58.4 | 12 | 1.70 | 0.299 | 4.12 |

## Sicurezza

- Il regime viene assegnato usando solo l'ultimo record noto prima dell'entrata del trade.
- Nessun uso di dati futuri per classificare il trade.
- Il Candidate Regime Gate è advisory per impostazione predefinita.
- Nessun cambio automatico di MASTER, posizione o live.

# Blocco 11 — Collegamento protetto al live

Generato: 2026-07-21T12:08:43+00:00

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

Generato: 2026-07-21T12:08:34+00:00

> Ultimo livello di osservabilità della pipeline. Non ripara, non riavvia, non modifica strategie o posizioni e non invia ordini.

## Stato generale

- Salute: **HEALTHY**
- Pipeline completa: **SI**
- Live bloccato: **SI**
- Persistenza completa: **SI**
- Catena audit valida: **SI**
- Recovery readiness: **READY**
- Controlli: **34**
- Warning: **0**
- Critici: **0**

## Controlli non superati

| Categoria | Controllo | Stato | Severità | Dettaglio |
| --- | --- | --- | --- | --- |
| — | Tutti i controlli | PASS | INFO | Nessuna anomalia |

## Sicurezza

- Riparazioni automatiche: **0**
- Riavvii automatici: **0**
- Mutazioni/promozioni/rollback/rilasci automatici: **0**
- Modifiche live: **NO**
- Ordini reali: **0**
