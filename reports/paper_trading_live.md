# Paper trading automatico KuCoin

Generato: 2026-07-24T04:38:54+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-07-24T04:38:25+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-07-24T04:38:25+00:00 | 2026-07-24T04:38:25+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-07-24T04:15:00+00:00 | 2026-07-24T04:15:00+00:00 | 8,5 min | 25,0 min | OK |
| 60m | 12 | 2026-07-24T03:00:00+00:00 | 2026-07-24T03:00:00+00:00 | 38,5 min | 45,0 min | OK |
| 240m | 12 | 2026-07-24T00:00:00+00:00 | 2026-07-24T00:00:00+00:00 | 38,5 min | 1,00 h | OK |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | DOGE | 240m | SHORT | -8,73 | 6,00 | 0,00 | RISK_GATE | 38,5 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Filtro rischio/esecuzione: numero massimo posizioni. |
| Principale 4H | AKE | 240m | LONG | 8,25 | 6,00 | 0,00 | RISK_GATE | 38,5 min | D: n/a | W: n/a | peso 0 | Filtro rischio/esecuzione: numero massimo posizioni. |
| Principale 4H | BANK | 240m | LONG | 7,75 | 6,00 | 0,00 | RISK_GATE | 38,5 min | D: n/a | W: n/a | peso 0 | Filtro rischio/esecuzione: numero massimo posizioni. |
| Principale 4H | HYPE | 240m | SHORT | -7,41 | 6,00 | 0,00 | RISK_GATE | 38,5 min | D: n/a | W: n/a | peso 0 | Filtro rischio/esecuzione: numero massimo posizioni. |
| Principale 4H | TAO | 240m | SHORT | -6,56 | 6,00 | 0,00 | RISK_GATE | 38,5 min | D: n/a | W: n/a | peso 0 | Filtro rischio/esecuzione: numero massimo posizioni. |
| Bilanciata 1H V2 | DOGE | 60m | SHORT | -9,06 | 5,50 | 0,00 | OPENED | 38,5 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Bilanciata 1H V2 | SOL | 60m | SHORT | -7,21 | 5,50 | 0,00 | READY | 38,5 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Rapida 1H V1 — madre | DOGE | 60m | SHORT | -9,06 | 4,50 | 0,00 | STRATEGY_FILTER | 38,5 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Filtro momentum: serve breakout DOWN oppure movimento breve ≥1,5%; breakout=NONE, movimento=-0.14%. |
| Rapida V1 — score 6–7,5 | DOGE | 60m | SHORT | -9,06 | 6,00 | 0,00 | STRATEGY_FILTER | 38,5 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Filtro momentum: serve breakout DOWN oppure movimento breve ≥1,5%; breakout=NONE, movimento=-0.14%. |
| Rapida V1 — no HIGH + score <7,5 | DOGE | 60m | SHORT | -9,06 | 4,50 | 0,00 | STRATEGY_FILTER | 38,5 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Filtro momentum: serve breakout DOWN oppure movimento breve ≥1,5%; breakout=NONE, movimento=-0.14%. |
| Rapida V1 — senza PEPE | DOGE | 60m | SHORT | -9,06 | 4,50 | 0,00 | STRATEGY_FILTER | 38,5 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Filtro momentum: serve breakout DOWN oppure movimento breve ≥1,5%; breakout=NONE, movimento=-0.14%. |
| Rapida V1 — target pieno 2R | DOGE | 60m | SHORT | -9,06 | 4,50 | 0,00 | STRATEGY_FILTER | 38,5 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Filtro momentum: serve breakout DOWN oppure movimento breve ≥1,5%; breakout=NONE, movimento=-0.14%. |
| Rapida 1H V2 | DOGE | 60m | SHORT | -9,06 | 5,00 | 0,00 | STRATEGY_FILTER | 38,5 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Filtro V2 non superato: regime, EMA, ritorni e RSI; per Rapida V2 servono anche breakout reale, volume e ADX. |
| Rapida 1H V1 — madre | SOL | 60m | SHORT | -7,21 | 4,50 | 0,00 | STRATEGY_FILTER | 38,5 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Filtro momentum: serve breakout DOWN oppure movimento breve ≥1,5%; breakout=NONE, movimento=-0.26%. |
| Rapida V1 — score 6–7,5 | SOL | 60m | SHORT | -7,21 | 6,00 | 0,00 | STRATEGY_FILTER | 38,5 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Filtro momentum: serve breakout DOWN oppure movimento breve ≥1,5%; breakout=NONE, movimento=-0.26%. |
| Rapida V1 — no HIGH + score <7,5 | SOL | 60m | SHORT | -7,21 | 4,50 | 0,00 | STRATEGY_FILTER | 38,5 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Filtro momentum: serve breakout DOWN oppure movimento breve ≥1,5%; breakout=NONE, movimento=-0.26%. |
| Rapida V1 — senza PEPE | SOL | 60m | SHORT | -7,21 | 4,50 | 0,00 | STRATEGY_FILTER | 38,5 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Filtro momentum: serve breakout DOWN oppure movimento breve ≥1,5%; breakout=NONE, movimento=-0.26%. |
| Rapida V1 — target pieno 2R | SOL | 60m | SHORT | -7,21 | 4,50 | 0,00 | STRATEGY_FILTER | 38,5 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Filtro momentum: serve breakout DOWN oppure movimento breve ≥1,5%; breakout=NONE, movimento=-0.26%. |
| Rapida 1H V2 | SOL | 60m | SHORT | -7,21 | 5,00 | 0,00 | STRATEGY_FILTER | 38,5 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Filtro V2 non superato: regime, EMA, ritorni e RSI; per Rapida V2 servono anche breakout reale, volume e ADX. |
| Rapida 1H V1 — madre | TAO | 60m | SHORT | -5,91 | 4,50 | 0,00 | STRATEGY_FILTER | 38,5 min | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout DOWN oppure movimento breve ≥1,5%; breakout=NONE, movimento=-0.44%. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.951,34 | -0,49% | €-48,66 | €3.000,00 | -1,62% | 4 | 18 | 33,33% | 0,91 | 4,26% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 18 | 460 | CAMPIONE INSUFFICIENTE | 30 (mancano 12) |

- Trade del Principale 4H chiusi: **18**; win rate **33,33%**; profit factor **0,91**.
- Expectancy: **€-2,94** per trade; P&L netto: **€-52,87**; max drawdown: **4,26%**.
- Valutazione: **Servono altri eventi indipendenti prima di trarre conclusioni.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 4 | €9.951,34 | €1.462,87 | €4.388,60 | €148,39 | €6,26 |
| TEST | Scanner Top 5 Long 1H | 3 | €10.607,31 | €1.269,32 | €2.538,64 | €158,58 | €-18,97 |
| TEST | Scanner Top 5 + forza BTC 1H | 3 | €10.360,67 | €1.331,37 | €2.662,75 | €156,16 | €-18,53 |
| TEST | Bilanciata 1H V1 | 4 | €10.330,61 | €2.717,92 | €8.153,75 | €206,10 | €-0,73 |
| TEST | Combo Adaptive — madre | 3 | €10.270,66 | €2.803,92 | €5.607,85 | €154,09 | €11,11 |
| TEST | Bilanciata 1H V3 Filtered | 4 | €10.228,38 | €3.050,39 | €9.151,18 | €153,08 | €-10,52 |
| TEST | Forza relativa 1H V2 | 4 | €10.219,82 | €3.370,64 | €6.741,29 | €152,62 | €-46,19 |
| TEST | Benchmark Bollinger mean reversion 1H | 2 | €10.211,23 | €4.026,08 | €8.052,15 | €96,63 | €-16,60 |
| TEST | Benchmark Donchian breakout 1H | 2 | €10.195,16 | €2.359,86 | €4.719,72 | €51,18 | €22,38 |
| TEST | Doge Ema 1H | 1 | €10.151,15 | €1.173,45 | €3.520,36 | €50,69 | €15,02 |
| TEST | Combo Scanner | 3 | €10.128,64 | €2.818,85 | €5.637,69 | €150,23 | €14,96 |
| TEST | Top 5 + BTC — target pieno 3R | 3 | €10.121,88 | €1.281,05 | €2.562,10 | €150,77 | €-18,10 |
| TEST | Rapida V1 — score 6–7,5 | 3 | €10.120,97 | €4.266,19 | €12.798,57 | €151,57 | €0,50 |
| TEST | Btc Bollinger 1H | 0 | €10.099,96 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V3 Filtered — madre | 4 | €10.076,68 | €1.904,58 | €5.713,73 | €201,79 | €-90,26 |
| TEST | Top 5 + BTC — 75% a 2,2R + runner 3R | 3 | €10.075,72 | €1.280,09 | €2.560,17 | €150,53 | €-18,02 |
| TEST | Combo Mean Reversion | 1 | €10.074,70 | €2.006,38 | €4.012,76 | €48,15 | €23,13 |
| TEST | Sol Bollinger 4H | 1 | €10.065,97 | €968,56 | €1.937,11 | €0,00 | €67,63 |
| TEST | Bilanciata 1H V2 | 3 | €10.048,56 | €2.465,44 | €7.396,31 | €100,52 | €-33,37 |
| TEST | Btc Bollinger 4H | 1 | €10.046,21 | €1.313,84 | €2.627,69 | €0,00 | €49,91 |
| TEST | Combo Adaptive — Quality7 | 2 | €10.043,42 | €2.601,36 | €5.202,73 | €99,80 | €10,36 |
| TEST | Ampia 4H | 4 | €10.040,48 | €1.903,22 | €3.806,44 | €150,70 | €6,40 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €10.028,40 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Bollinger 1H | 0 | €10.015,45 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 — score <7,5 | 4 | €10.009,17 | €4.929,03 | €14.787,09 | €200,21 | €-32,69 |
| TEST | Doge Donchian 1H | 1 | €10.008,28 | €1.095,98 | €3.287,94 | €49,99 | €13,08 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 0 | €10.005,68 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €50 · 15x | 0 | €10.002,52 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €10 · 15x | 0 | €10.000,50 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €10 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €50 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · prudente · 5x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €10 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €10 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €50 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €50 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · prudente · 5x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · prudente · 5x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 4H | 1 | €9.999,35 | €1.105,63 | €2.211,26 | €50,00 | €-2,94 |
| TEST | Btc Donchian 4H | 1 | €9.999,35 | €1.105,63 | €2.211,26 | €50,00 | €-2,94 |
| TEST | Scalp RSI Long 15 · €10 · 15x | 0 | €9.998,50 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — target pieno 3R | 3 | €9.995,65 | €2.844,67 | €5.689,33 | €149,61 | €3,82 |
| TEST | Scalp RSI Long 15 · €50 · 15x | 0 | €9.992,50 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Donchian 1H | 1 | €9.991,60 | €1.301,74 | €3.905,22 | €49,99 | €-3,36 |
| TEST | Rapida V1 — senza PEPE | 3 | €9.990,63 | €1.720,45 | €5.161,35 | €149,99 | €-46,28 |
| TEST | Scalp RSI Long 15 · prudente · 5x | 0 | €9.988,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Donchian 1H | 0 | €9.982,54 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 0 | €9.980,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Top 5 + BTC — Guard + BTC≤3 | 3 | €9.978,64 | €1.285,16 | €2.570,32 | €148,79 | €-17,84 |
| TEST | Btc Adaptive 4H | 1 | €9.974,29 | €1.047,40 | €2.094,81 | €50,00 | €-26,85 |
| TEST | Rapida V3 — senza ESPORTS | 3 | €9.966,62 | €2.333,55 | €7.000,64 | €150,11 | €-30,21 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.964,86 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Benchmark trend following EMA 1H | 3 | €9.961,74 | €2.803,05 | €5.606,10 | €99,49 | €19,18 |
| TEST | Rapida V1 — no HIGH + score <7,5 | 4 | €9.958,19 | €4.884,63 | €14.653,90 | €198,72 | €-32,44 |
| TEST | Btc Adaptive 1H | 1 | €9.953,32 | €1.156,05 | €3.468,15 | €49,94 | €-32,69 |
| TEST | Sol Donchian 4H | 1 | €9.952,34 | €830,21 | €1.660,43 | €49,74 | €5,33 |
| TEST | Sol Adaptive 4H | 1 | €9.952,15 | €761,04 | €1.522,08 | €49,74 | €4,89 |
| TEST | Top 5 + BTC — BTC≤3 | 3 | €9.950,46 | €1.300,19 | €2.600,39 | €149,91 | €-17,79 |
| TEST | Top 5 + BTC — BTC 2–3 | 2 | €9.948,72 | €1.092,52 | €2.185,03 | €100,07 | €0,00 |
| TEST | Sol Ema 4H | 0 | €9.948,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Ema 4H | 0 | €9.947,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 1H | 1 | €9.943,70 | €1.381,14 | €4.143,42 | €49,72 | €1,91 |
| TEST | Combo Adaptive — Trend/Transition | 2 | €9.943,37 | €964,46 | €1.928,92 | €98,78 | €0,00 |
| TEST | Rapida V3 — no volatilità HIGH | 3 | €9.939,73 | €2.324,29 | €6.972,88 | €149,50 | €-30,13 |
| TEST | Sol Ema 1H | 1 | €9.932,24 | €1.150,16 | €3.450,47 | €49,69 | €-2,97 |
| TEST | Forza relativa 1H V1 | 4 | €9.931,76 | €3.080,20 | €6.160,40 | €148,54 | €10,08 |
| TEST | Rapida V1 — Long + BTC 1–3 + score <7,5 | 2 | €9.929,08 | €921,32 | €2.763,95 | €99,77 | €-24,89 |
| TEST | Doge Bollinger 1H | 1 | €9.922,86 | €1.381,14 | €4.143,42 | €49,72 | €-19,32 |
| TEST | Rapida 1H V2 | 2 | €9.921,69 | €2.348,51 | €7.045,53 | €99,77 | €-51,69 |
| TEST | Combo Adaptive — 75% a 2R + runner 3R | 3 | €9.915,46 | €2.840,61 | €5.681,22 | €149,40 | €-13,92 |
| TEST | Btc Donchian 1H | 1 | €9.911,33 | €1.293,96 | €3.881,87 | €49,69 | €-23,94 |
| TEST | Btc Ema 1H | 1 | €9.906,26 | €1.149,81 | €3.449,44 | €49,67 | €-26,03 |
| TEST | Rapida V1 — target pieno 2R | 3 | €9.906,04 | €2.324,32 | €6.972,95 | €149,55 | €-30,03 |
| TEST | Sol Adaptive 1H | 1 | €9.900,29 | €1.149,09 | €3.447,26 | €49,64 | €-25,81 |
| TEST | Eth Adaptive 1H | 1 | €9.898,12 | €1.146,74 | €3.440,21 | €49,54 | €-7,61 |
| TEST | Combo Adaptive — Quality7 + Regime + parziale 1R | 1 | €9.889,70 | €864,27 | €1.728,54 | €49,61 | €0,00 |
| TEST | Combo Trend | 3 | €9.868,68 | €1.962,11 | €3.924,22 | €149,14 | €10,08 |
| TEST | Combo Adaptive — Quality7 + Regime | 1 | €9.867,47 | €864,27 | €1.728,54 | €49,61 | €0,00 |
| TEST | Combo Adaptive — parziale 1R | 3 | €9.866,28 | €2.809,64 | €5.619,28 | €147,90 | €10,67 |
| TEST | Combo Adaptive — Long Only | 2 | €9.865,72 | €1.099,22 | €2.198,44 | €98,72 | €0,00 |
| TEST | Global Confluence puro 1H | 1 | €9.860,91 | €1.539,06 | €3.078,12 | €49,25 | €13,13 |
| TEST | Rapida 1H V1 — madre | 4 | €9.849,19 | €1.868,82 | €5.606,45 | €197,23 | €-87,91 |
| TEST | Rapida V3 — Long + no HIGH + score <7,5 | 1 | €9.846,03 | €137,10 | €411,29 | €49,35 | €-24,68 |
| TEST | Eth Ema 1H | 1 | €9.825,66 | €1.138,34 | €3.415,02 | €49,18 | €-7,56 |
| TEST | Top 5 + BTC — Guard | 3 | €9.815,40 | €1.163,95 | €2.327,90 | €146,88 | €-17,55 |
| TEST | Rapida V3 — qualità completa + profit lock | 1 | €9.810,79 | €136,61 | €409,82 | €49,18 | €-24,59 |
| TEST | Rapida V3 — Long Only | 1 | €9.806,53 | €136,55 | €409,64 | €49,16 | €-24,58 |
| TEST | Top 5 + BTC — Guard + BTC≤3 + MFE | 2 | €9.801,04 | €1.076,68 | €2.153,35 | €98,76 | €-32,39 |
| TEST | Scanner Bottom 5 Short 1H | 3 | €9.787,89 | €3.281,30 | €6.562,60 | €97,65 | €14,44 |
| TEST | Top 5 + BTC — solo MFE | 3 | €9.761,15 | €2.553,52 | €5.107,05 | €148,96 | €-31,92 |
| TEST | Master Adaptive Expanded V1 | 3 | €9.758,78 | €1.240,15 | €2.480,31 | €146,90 | €-11,25 |
| TEST | Master Adaptive V1 | 3 | €9.719,61 | €1.239,48 | €2.478,96 | €146,74 | €-7,43 |
| TEST | Master Adaptive No Alt V1 | 3 | €9.719,61 | €1.239,48 | €2.478,96 | €146,74 | €-7,43 |
| TEST | Master Adaptive Runner25 V1 | 3 | €9.719,61 | €1.239,48 | €2.478,96 | €146,74 | €-7,43 |
| TEST | Top 5 + BTC — Guard + MFE | 2 | €9.689,76 | €959,91 | €1.919,82 | €97,91 | €-32,02 |
| TEST | Combo Adaptive — MFE Trail esistente | 3 | €9.681,02 | €1.149,02 | €2.298,05 | €96,76 | €0,00 |
| TEST | Master Adaptive Gb20 V1 | 2 | €9.627,11 | €1.049,20 | €2.098,41 | €97,15 | €-14,84 |
| TEST | Master Adaptive Strict3 V1 | 2 | €9.563,45 | €1.086,96 | €2.173,93 | €97,00 | €-31,27 |

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
| PRINCIPALE | Principale 4H | Confluenza trend | €9.951,34 | €-52,87 | 18 | 18 | 33,33% | 0,91 | €-2,94 | 4,26% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.607,31 | €627,89 | 30 | 30 | 53,33% | 2,18 | €20,93 | 2,70% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €10.360,67 | €381,10 | 22 | 22 | 50,00% | 1,96 | €17,32 | 2,01% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €10.330,61 | €336,34 | 37 | 37 | 51,35% | 1,46 | €9,09 | 2,30% |
| TEST | Combo Adaptive — madre | Combo Adaptive | €10.270,66 | €262,84 | 21 | 21 | 47,62% | 1,78 | €12,52 | 1,31% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €10.228,38 | €244,07 | 31 | 31 | 45,16% | 1,30 | €7,87 | 2,20% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €10.219,82 | €270,05 | 30 | 29 | 40,00% | 1,32 | €9,00 | 3,69% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €10.211,23 | €232,16 | 25 | 25 | 48,00% | 1,52 | €9,29 | 2,06% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €10.195,16 | €174,63 | 18 | 18 | 50,00% | 1,44 | €9,70 | 2,12% |
| TEST | Doge Ema 1H | Trend following EMA | €10.151,15 | €138,64 | 6 | 6 | 66,67% | 2,24 | €23,11 | 1,36% |
| TEST | Combo Scanner | Combo Scanner | €10.128,64 | €117,73 | 23 | 23 | 43,48% | 1,20 | €5,12 | 2,66% |
| TEST | Top 5 + BTC — target pieno 3R | Scanner Top 5 + forza BTC | €10.121,88 | €141,80 | 8 | 8 | 62,50% | 1,87 | €17,72 | 2,33% |
| TEST | Rapida V1 — score 6–7,5 | Momentum / breakout | €10.120,97 | €128,30 | 26 | 26 | 38,46% | 1,25 | €4,93 | 2,49% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.099,96 | €99,96 | 2 | 2 | 100,00% | ∞ | €49,98 | 0,31% |
| TEST | Rapida 1H V3 Filtered — madre | Momentum / breakout V3 Filtered | €10.076,68 | €169,71 | 55 | 55 | 36,36% | 1,16 | €3,09 | 2,89% |
| TEST | Top 5 + BTC — 75% a 2,2R + runner 3R | Scanner Top 5 + forza BTC | €10.075,72 | €95,56 | 8 | 8 | 62,50% | 1,59 | €11,95 | 2,33% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €10.074,70 | €54,00 | 12 | 12 | 41,67% | 1,16 | €4,50 | 2,31% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €10.065,97 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,40% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €10.048,56 | €86,47 | 24 | 22 | 54,17% | 1,16 | €3,60 | 2,75% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.046,21 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,28% |
| TEST | Combo Adaptive — Quality7 | Combo Adaptive | €10.043,42 | €36,18 | 6 | 6 | 66,67% | 1,34 | €6,03 | 1,51% |
| TEST | Ampia 4H | Confluenza trend | €10.040,48 | €35,68 | 13 | 13 | 23,08% | 1,09 | €2,74 | 2,56% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €10.028,40 | €28,40 | 6 | 6 | 33,33% | 1,98 | €4,73 | 0,25% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €10.015,45 | €15,45 | 1 | 1 | 100,00% | ∞ | €15,45 | 0,51% |
| TEST | Rapida V3 — score <7,5 | Momentum / breakout V3 Filtered | €10.009,17 | €50,31 | 23 | 23 | 34,78% | 1,10 | €2,19 | 2,49% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €10.008,28 | €-2,55 | 3 | 3 | 66,67% | 0,96 | €-0,85 | 0,96% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €10.005,68 | €5,68 | 6 | 6 | 33,33% | 1,98 | €0,95 | 0,05% |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | €10.002,52 | €2,52 | 4 | 4 | 50,00% | 1,22 | €0,63 | 0,11% |
| TEST | Scalp RSI Long 25 · €10 · 15x | Inversione RSI estrema 15m | €10.000,50 | €0,50 | 4 | 4 | 50,00% | 1,22 | €0,13 | 0,02% |
| TEST | Scalp RSI Long 20 · €10 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 20 · €50 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 20 · prudente · 5x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 85 · €10 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 80 · €10 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 85 · €50 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 80 · €50 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 85 · prudente · 5x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 80 · prudente · 5x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Btc Ema 4H | Trend following EMA | €9.999,35 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,68% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €9.999,35 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,68% |
| TEST | Scalp RSI Long 15 · €10 · 15x | Inversione RSI estrema 15m | €9.998,50 | €-1,50 | 1 | 1 | 0,00% | 0,00 | €-1,50 | 0,02% |
| TEST | Combo Adaptive — target pieno 3R | Combo Adaptive | €9.995,65 | €-4,53 | 9 | 9 | 55,56% | 0,98 | €-0,50 | 1,41% |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | €9.992,50 | €-7,50 | 1 | 1 | 0,00% | 0,00 | €-7,50 | 0,11% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €9.991,60 | €-2,63 | 2 | 2 | 50,00% | 0,41 | €-1,31 | 0,79% |
| TEST | Rapida V1 — senza PEPE | Momentum / breakout | €9.990,63 | €39,35 | 24 | 24 | 37,50% | 1,08 | €1,64 | 2,10% |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | €9.988,38 | €-11,62 | 1 | 1 | 0,00% | 0,00 | €-11,62 | 0,17% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.982,54 | €-17,46 | 3 | 3 | 33,33% | 0,84 | €-5,82 | 1,38% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €9.980,00 | €-20,00 | 4 | 4 | 25,00% | 0,22 | €-5,00 | 0,34% |
| TEST | Top 5 + BTC — Guard + BTC≤3 | Scanner Top 5 + forza BTC | €9.978,64 | €-1,60 | 4 | 4 | 50,00% | 0,99 | €-0,40 | 1,64% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €9.974,29 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,64% |
| TEST | Rapida V3 — senza ESPORTS | Momentum / breakout V3 Filtered | €9.966,62 | €0,63 | 28 | 28 | 32,14% | 1,00 | €0,02 | 2,49% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.964,86 | €-35,14 | 6 | 6 | 16,67% | 0,18 | €-5,86 | 0,36% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.961,74 | €-54,01 | 16 | 16 | 31,25% | 0,87 | €-3,38 | 2,25% |
| TEST | Rapida V1 — no HIGH + score <7,5 | Momentum / breakout | €9.958,19 | €-1,00 | 28 | 28 | 35,71% | 1,00 | €-0,04 | 2,83% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €9.953,32 | €-11,74 | 2 | 2 | 50,00% | 0,78 | €-5,87 | 0,89% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €9.952,34 | €-52,00 | 1 | 1 | 0,00% | 0,00 | €-52,00 | 0,60% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €9.952,15 | €-51,83 | 1 | 1 | 0,00% | 0,00 | €-51,83 | 0,59% |
| TEST | Top 5 + BTC — BTC≤3 | Scanner Top 5 + forza BTC | €9.950,46 | €-29,80 | 4 | 4 | 50,00% | 0,73 | €-7,45 | 2,20% |
| TEST | Top 5 + BTC — BTC 2–3 | Scanner Top 5 + forza BTC | €9.948,72 | €-49,59 | 3 | 3 | 33,33% | 0,54 | €-16,53 | 2,22% |
| TEST | Sol Ema 4H | Trend following EMA | €9.948,00 | €-52,00 | 1 | 1 | 0,00% | 0,00 | €-52,00 | 0,56% |
| TEST | Eth Ema 4H | Trend following EMA | €9.947,12 | €-52,88 | 1 | 1 | 0,00% | 0,00 | €-52,88 | 0,68% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.943,70 | €-55,79 | 1 | 1 | 0,00% | 0,00 | €-55,79 | 0,81% |
| TEST | Combo Adaptive — Trend/Transition | Combo Adaptive | €9.943,37 | €-55,38 | 9 | 9 | 44,44% | 0,80 | €-6,15 | 2,18% |
| TEST | Rapida V3 — no volatilità HIGH | Momentum / breakout V3 Filtered | €9.939,73 | €-26,36 | 29 | 29 | 34,48% | 0,96 | €-0,91 | 2,96% |
| TEST | Sol Ema 1H | Trend following EMA | €9.932,24 | €-62,66 | 3 | 3 | 33,33% | 0,42 | €-20,89 | 1,67% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €9.931,76 | €-74,62 | 23 | 23 | 26,09% | 0,83 | €-3,24 | 3,25% |
| TEST | Rapida V1 — Long + BTC 1–3 + score <7,5 | Momentum / breakout | €9.929,08 | €-44,37 | 6 | 6 | 16,67% | 0,62 | €-7,40 | 1,55% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €9.922,86 | €-55,79 | 1 | 1 | 0,00% | 0,00 | €-55,79 | 0,93% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €9.921,69 | €-22,68 | 6 | 5 | 33,33% | 0,82 | €-3,78 | 1,69% |
| TEST | Combo Adaptive — 75% a 2R + runner 3R | Combo Adaptive | €9.915,46 | €-67,21 | 13 | 13 | 46,15% | 0,83 | €-5,17 | 2,12% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €9.911,33 | €-62,42 | 3 | 3 | 33,33% | 0,43 | €-20,81 | 1,49% |
| TEST | Btc Ema 1H | Trend following EMA | €9.906,26 | €-65,61 | 4 | 4 | 25,00% | 0,60 | €-16,40 | 1,56% |
| TEST | Rapida V1 — target pieno 2R | Momentum / breakout | €9.906,04 | €-60,15 | 25 | 25 | 28,00% | 0,89 | €-2,41 | 2,58% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €9.900,29 | €-71,90 | 3 | 3 | 33,33% | 0,34 | €-23,97 | 1,85% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.898,12 | €-92,21 | 4 | 4 | 50,00% | 0,16 | €-23,05 | 1,11% |
| TEST | Combo Adaptive — Quality7 + Regime + parziale 1R | Combo Adaptive | €9.889,70 | €-109,26 | 4 | 4 | 25,00% | 0,32 | €-27,31 | 1,95% |
| TEST | Combo Trend | Combo Trend | €9.868,68 | €-139,04 | 25 | 25 | 28,00% | 0,82 | €-5,56 | 3,58% |
| TEST | Combo Adaptive — Quality7 + Regime | Combo Adaptive | €9.867,47 | €-131,50 | 4 | 4 | 25,00% | 0,18 | €-32,87 | 1,95% |
| TEST | Combo Adaptive — parziale 1R | Combo Adaptive | €9.866,28 | €-140,65 | 11 | 11 | 36,36% | 0,64 | €-12,79 | 2,24% |
| TEST | Combo Adaptive — Long Only | Combo Adaptive | €9.865,72 | €-132,59 | 5 | 5 | 20,00% | 0,42 | €-26,52 | 2,34% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.860,91 | €-150,03 | 8 | 8 | 37,50% | 0,45 | €-18,75 | 2,92% |
| TEST | Rapida 1H V1 — madre | Momentum / breakout | €9.849,19 | €-60,19 | 63 | 63 | 33,33% | 0,96 | €-0,96 | 6,76% |
| TEST | Rapida V3 — Long + no HIGH + score <7,5 | Momentum / breakout V3 Filtered | €9.846,03 | €-129,04 | 17 | 17 | 35,29% | 0,74 | €-7,59 | 2,77% |
| TEST | Eth Ema 1H | Trend following EMA | €9.825,66 | €-164,74 | 6 | 6 | 33,33% | 0,25 | €-27,46 | 1,79% |
| TEST | Top 5 + BTC — Guard | Scanner Top 5 + forza BTC | €9.815,40 | €-165,42 | 7 | 7 | 28,57% | 0,41 | €-23,63 | 3,31% |
| TEST | Rapida V3 — qualità completa + profit lock | Momentum / breakout V3 Filtered | €9.810,79 | €-164,37 | 17 | 17 | 47,06% | 0,70 | €-9,67 | 3,16% |
| TEST | Rapida V3 — Long Only | Momentum / breakout V3 Filtered | €9.806,53 | €-168,65 | 22 | 22 | 27,27% | 0,72 | €-7,67 | 2,93% |
| TEST | Top 5 + BTC — Guard + BTC≤3 + MFE | Scanner Top 5 + forza BTC | €9.801,04 | €-165,28 | 11 | 11 | 36,36% | 0,50 | €-15,03 | 2,30% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.787,89 | €-222,24 | 22 | 22 | 31,82% | 0,61 | €-10,10 | 5,48% |
| TEST | Top 5 + BTC — solo MFE | Scanner Top 5 + forza BTC | €9.761,15 | €-204,18 | 10 | 10 | 30,00% | 0,21 | €-20,42 | 3,30% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €9.758,78 | €-227,96 | 7 | 7 | 14,29% | 0,29 | €-32,57 | 2,80% |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | €9.719,61 | €-271,00 | 5 | 5 | 0,00% | 0,00 | €-54,20 | 3,19% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €9.719,61 | €-271,00 | 5 | 5 | 0,00% | 0,00 | €-54,20 | 3,19% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €9.719,61 | €-271,00 | 5 | 5 | 0,00% | 0,00 | €-54,20 | 3,19% |
| TEST | Top 5 + BTC — Guard + MFE | Scanner Top 5 + forza BTC | €9.689,76 | €-277,20 | 14 | 14 | 28,57% | 0,37 | €-19,80 | 3,47% |
| TEST | Combo Adaptive — MFE Trail esistente | Combo Adaptive | €9.681,02 | €-317,53 | 27 | 27 | 25,93% | 0,45 | €-11,76 | 4,11% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €9.627,11 | €-356,79 | 27 | 27 | 51,85% | 0,44 | €-13,21 | 4,16% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €9.563,45 | €-403,98 | 12 | 12 | 16,67% | 0,32 | €-33,66 | 4,59% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | LAB | SHORT | Confluenza trend | 240m | 3,0x | 0,17841 | 0,17841 | 0,17841 | 0,23699 | 0,13559 | €136,26 | €408,77 | €0,00 | €-0,00 |
| Principale 4H | SUI | LONG | Confluenza trend | 240m | 3,0x | 0,76296 | 0,76296 | 0,73998 | 0,51245 | 0,80891 | €547,52 | €1.642,56 | €49,46 | €0,00 |
| Principale 4H | ONDO | LONG | Confluenza trend | 240m | 3,0x | 0,40344 | 0,40344 | 0,37762 | 0,27098 | 0,45509 | €254,70 | €764,09 | €48,91 | €0,00 |
| Principale 4H | DOGE | SHORT | Confluenza trend | 240m | 3,0x | 0,06940 | 0,06912 | 0,07160 | 0,09218 | 0,06498 | €524,39 | €1.573,18 | €50,01 | €6,26 |
| Bilanciata 1H V1 | ONDO | LONG | Confluenza trend | 60m | 3,0x | 0,39694 | 0,39694 | 0,38539 | 0,26661 | 0,42004 | €581,76 | €1.745,29 | €50,78 | €0,00 |
| Bilanciata 1H V1 | DOGE | SHORT | Confluenza trend | 60m | 3,0x | 0,06953 | 0,06912 | 0,07070 | 0,09235 | 0,06717 | €1.013,54 | €3.040,62 | €51,54 | €17,76 |
| Bilanciata 1H V1 | ADA | SHORT | Confluenza trend | 60m | 3,0x | 0,16703 | 0,16703 | 0,16999 | 0,22187 | 0,16112 | €978,72 | €2.936,17 | €51,97 | €-0,00 |
| Bilanciata 1H V1 | BANK | LONG | Confluenza trend | 60m | 3,0x | 0,26033 | 0,24918 | 0,22909 | 0,17486 | 0,32281 | €143,89 | €431,67 | €51,80 | €-18,49 |
| Bilanciata 1H V2 | ESPORTS | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,02164 | 0,02164 | 0,02164 | 0,02874 | 0,01644 | €138,69 | €416,06 | €0,00 | €-0,00 |
| Bilanciata 1H V2 | BTC | SHORT | Confluenza trend V2 | 60m | 3,0x | 64717,76386 | 65323,60000 | 65649,69966 | 85966,76299 | 62853,89226 | €1.163,40 | €3.490,20 | €50,26 | €-32,67 |
| Bilanciata 1H V2 | DOGE | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,06911 | 0,06912 | 0,07010 | 0,09180 | 0,06712 | €1.163,35 | €3.490,05 | €50,26 | €-0,70 |
| Bilanciata 1H V3 Filtered | ESPORTS | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,02126 | 0,02126 | 0,02126 | 0,02823 | 0,01615 | €141,51 | €424,52 | €0,00 | €-0,00 |
| Bilanciata 1H V3 Filtered | ONDO | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,40134 | 0,40134 | 0,38898 | 0,26957 | 0,42605 | €557,59 | €1.672,77 | €51,50 | €0,00 |
| Bilanciata 1H V3 Filtered | BTC | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 64923,19276 | 65323,60000 | 65858,08674 | 86239,64105 | 63053,40481 | €1.167,13 | €3.501,39 | €50,42 | €-21,59 |
| Bilanciata 1H V3 Filtered | DOGE | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,06934 | 0,06912 | 0,07033 | 0,09210 | 0,06734 | €1.184,17 | €3.552,50 | €51,16 | €11,07 |
| Rapida 1H V1 — madre | ONDO | LONG | Momentum / breakout | 60m | 3,0x | 0,39924 | 0,39924 | 0,38995 | 0,26816 | 0,41318 | €708,01 | €2.124,02 | €49,43 | €0,00 |
| Rapida 1H V1 — madre | ZEC | SHORT | Momentum / breakout | 60m | 3,0x | 503,83921 | 508,55000 | 513,54273 | 669,26642 | 489,28394 | €857,19 | €2.571,57 | €49,53 | €-24,04 |
| Rapida 1H V1 — madre | BANK | LONG | Momentum / breakout | 60m | 3,0x | 0,27032 | 0,24918 | 0,24378 | 0,18157 | 0,31014 | €168,54 | €505,62 | €49,65 | €-39,55 |
| Rapida 1H V1 — madre | RIF | LONG | Momentum / breakout | 60m | 3,0x | 0,11756 | 0,11051 | 0,10346 | 0,07896 | 0,13872 | €135,08 | €405,23 | €48,63 | €-24,32 |
| Rapida V1 — score 6–7,5 | BTC | SHORT | Momentum / breakout | 60m | 3,0x | 65079,58148 | 65323,60000 | 65808,47279 | 86447,37740 | 63986,24451 | €1.483,09 | €4.449,28 | €49,83 | €-16,68 |
| Rapida V1 — score 6–7,5 | DOGE | SHORT | Momentum / breakout | 60m | 3,0x | 0,06953 | 0,06912 | 0,07044 | 0,09235 | 0,06815 | €1.281,83 | €3.845,50 | €50,70 | €22,46 |
| Rapida V1 — score 6–7,5 | TAO | SHORT | Momentum / breakout | 60m | 3,0x | 192,24458 | 192,47000 | 194,42319 | 255,36489 | 188,97667 | €1.501,26 | €4.503,79 | €51,04 | €-5,28 |
| Rapida V1 — no HIGH + score <7,5 | ONDO | LONG | Momentum / breakout | 60m | 3,0x | 0,39924 | 0,39924 | 0,38995 | 0,26816 | 0,41318 | €704,39 | €2.113,17 | €49,18 | €0,00 |
| Rapida V1 — no HIGH + score <7,5 | BTC | SHORT | Momentum / breakout | 60m | 3,0x | 64923,19276 | 65323,60000 | 65650,33252 | 86239,64105 | 63832,48313 | €1.473,17 | €4.419,52 | €49,50 | €-27,26 |
| Rapida V1 — no HIGH + score <7,5 | TAO | SHORT | Momentum / breakout | 60m | 3,0x | 192,24458 | 192,47000 | 194,42319 | 255,36489 | 188,97667 | €1.474,44 | €4.423,31 | €50,13 | €-5,19 |
| Rapida V1 — no HIGH + score <7,5 | ADA | SHORT | Momentum / breakout | 60m | 3,0x | 0,16708 | 0,16708 | 0,16933 | 0,22194 | 0,16370 | €1.232,63 | €3.697,90 | €49,91 | €-0,00 |
| Rapida V1 — Long + BTC 1–3 + score <7,5 | ONDO | LONG | Momentum / breakout | 60m | 3,0x | 0,39694 | 0,39694 | 0,38849 | 0,26661 | 0,40961 | €783,06 | €2.349,19 | €50,00 | €0,00 |
| Rapida V1 — Long + BTC 1–3 + score <7,5 | RIF | LONG | Momentum / breakout | 60m | 3,0x | 0,11756 | 0,11051 | 0,10346 | 0,07896 | 0,13872 | €138,25 | €414,76 | €49,77 | €-24,89 |
| Rapida V1 — senza PEPE | ONDO | LONG | Momentum / breakout | 60m | 3,0x | 0,39924 | 0,39924 | 0,38995 | 0,26816 | 0,41318 | €713,68 | €2.141,05 | €49,83 | €0,00 |
| Rapida V1 — senza PEPE | ZEC | SHORT | Momentum / breakout | 60m | 3,0x | 504,42909 | 508,55000 | 514,14397 | 670,04998 | 489,85678 | €867,81 | €2.603,42 | €50,14 | €-21,27 |
| Rapida V1 — senza PEPE | RIF | LONG | Momentum / breakout | 60m | 3,0x | 0,11756 | 0,11051 | 0,10346 | 0,07896 | 0,13872 | €138,96 | €416,88 | €50,03 | €-25,02 |
| Rapida V1 — target pieno 2R | ONDO | LONG | Momentum / breakout | 60m | 3,0x | 0,39924 | 0,39924 | 0,38995 | 0,26816 | 0,41782 | €712,92 | €2.138,77 | €49,77 | €0,00 |
| Rapida V1 — target pieno 2R | TAO | SHORT | Momentum / breakout | 60m | 3,0x | 192,24458 | 192,47000 | 194,42319 | 255,36489 | 187,88737 | €1.473,39 | €4.420,17 | €50,09 | €-5,18 |
| Rapida V1 — target pieno 2R | RIF | LONG | Momentum / breakout | 60m | 3,0x | 0,11756 | 0,11051 | 0,10346 | 0,07896 | 0,14578 | €138,00 | €414,01 | €49,68 | €-24,84 |
| Rapida 1H V2 | BTC | SHORT | Momentum / breakout V2 | 60m | 3,0x | 64923,19276 | 65323,60000 | 65650,33252 | 86239,64105 | 63832,48313 | €1.485,87 | €4.457,60 | €49,93 | €-27,49 |
| Rapida 1H V2 | ZEC | SHORT | Momentum / breakout V2 | 60m | 3,0x | 503,83921 | 508,55000 | 513,54273 | 669,26642 | 489,28394 | €862,65 | €2.587,94 | €49,84 | €-24,20 |
| Rapida 1H V3 Filtered — madre | ONDO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,39924 | 0,39924 | 0,38995 | 0,26816 | 0,41318 | €715,14 | €2.145,42 | €49,93 | €0,00 |
| Rapida 1H V3 Filtered — madre | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 503,83921 | 508,55000 | 513,54273 | 669,26642 | 489,28394 | €877,00 | €2.631,00 | €50,67 | €-24,60 |
| Rapida 1H V3 Filtered — madre | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,27032 | 0,24918 | 0,24378 | 0,18157 | 0,31014 | €172,44 | €517,32 | €50,80 | €-40,46 |
| Rapida 1H V3 Filtered — madre | RIF | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,11756 | 0,11051 | 0,10346 | 0,07896 | 0,13872 | €140,00 | €419,99 | €50,40 | €-25,20 |
| Rapida V3 — score <7,5 | ONDO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,39924 | 0,39924 | 0,38995 | 0,26816 | 0,41318 | €712,28 | €2.136,85 | €49,73 | €0,00 |
| Rapida V3 — score <7,5 | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 64923,19276 | 65323,60000 | 65650,33252 | 86239,64105 | 63832,48313 | €1.484,27 | €4.452,81 | €49,87 | €-27,46 |
| Rapida V3 — score <7,5 | TAO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 192,24458 | 192,47000 | 194,42319 | 255,36489 | 188,97667 | €1.485,79 | €4.457,37 | €50,51 | €-5,23 |
| Rapida V3 — score <7,5 | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16732 | 0,16732 | 0,16956 | 0,22226 | 0,16396 | €1.246,68 | €3.740,05 | €50,10 | €-0,00 |
| Rapida V3 — no volatilità HIGH | ONDO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,39924 | 0,39924 | 0,38995 | 0,26816 | 0,41318 | €707,41 | €2.122,22 | €49,39 | €0,00 |
| Rapida V3 — no volatilità HIGH | TAO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 192,24458 | 192,47000 | 194,42319 | 255,36489 | 188,97667 | €1.478,41 | €4.435,24 | €50,26 | €-5,20 |
| Rapida V3 — no volatilità HIGH | RIF | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,11756 | 0,11051 | 0,10346 | 0,07896 | 0,13872 | €138,47 | €415,42 | €49,85 | €-24,93 |
| Rapida V3 — Long Only | RIF | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,11756 | 0,11051 | 0,10346 | 0,07896 | 0,13872 | €136,55 | €409,64 | €49,16 | €-24,58 |
| Rapida V3 — Long + no HIGH + score <7,5 | RIF | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,11756 | 0,11051 | 0,10346 | 0,07896 | 0,13872 | €137,10 | €411,29 | €49,35 | €-24,68 |
| Rapida V3 — senza ESPORTS | ONDO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,39924 | 0,39924 | 0,38995 | 0,26816 | 0,41318 | €712,28 | €2.136,85 | €49,73 | €0,00 |
| Rapida V3 — senza ESPORTS | TAO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 192,24458 | 192,47000 | 194,42319 | 255,36489 | 188,97667 | €1.482,41 | €4.447,24 | €50,40 | €-5,21 |
| Rapida V3 — senza ESPORTS | RIF | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,11756 | 0,11051 | 0,10346 | 0,07896 | 0,13872 | €138,85 | €416,54 | €49,99 | €-25,00 |
| Rapida V3 — qualità completa + profit lock | RIF | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,11756 | 0,11051 | 0,10346 | 0,07896 | 0,13872 | €136,61 | €409,82 | €49,18 | €-24,59 |
| Ampia 4H | DOGE | SHORT | Confluenza trend | 240m | 2,0x | 0,07237 | 0,06912 | 0,07105 | 0,10819 | 0,06457 | €649,49 | €1.298,97 | €0,00 | €58,28 |
| Ampia 4H | ZEC | LONG | Confluenza trend | 240m | 2,0x | 522,36445 | 508,55000 | 483,09844 | 263,79405 | 632,30930 | €332,53 | €665,06 | €49,99 | €-17,59 |
| Ampia 4H | PEPE | LONG | Confluenza trend | 240m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €497,18 | €994,35 | €50,70 | €-33,17 |
| Ampia 4H | HYPE | SHORT | Confluenza trend | 240m | 2,0x | 58,36732 | 58,44400 | 61,80927 | 87,25915 | 48,72988 | €424,03 | €848,06 | €50,01 | €-1,11 |
| Forza relativa 1H V1 | ESPORTS | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,02126 | 0,02126 | 0,02126 | 0,03178 | 0,01564 | €208,05 | €416,10 | €0,00 | €-0,00 |
| Forza relativa 1H V1 | NIGHT | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,02031 | 0,02031 | 0,02210 | 0,03036 | 0,01637 | €285,91 | €571,83 | €50,45 | €-0,00 |
| Forza relativa 1H V1 | ONDO | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,42171 | €891,90 | €1.783,80 | €49,29 | €0,00 |
| Forza relativa 1H V1 | DOGE | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,06933 | 0,06912 | 0,07032 | 0,10364 | 0,06713 | €1.694,34 | €3.388,67 | €48,80 | €10,08 |
| Forza relativa 1H V2 | ESPORTS | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,02126 | 0,02126 | 0,02126 | 0,03178 | 0,01564 | €215,33 | €430,67 | €0,00 | €-0,00 |
| Forza relativa 1H V2 | BANK | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,27032 | 0,24918 | 0,23789 | 0,13651 | 0,34169 | €214,28 | €428,56 | €51,43 | €-33,52 |
| Forza relativa 1H V2 | HYPE | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 57,89642 | 58,44400 | 59,12372 | 86,55515 | 55,19635 | €1.212,96 | €2.425,92 | €51,43 | €-22,94 |
| Forza relativa 1H V2 | DOGE | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,06933 | 0,06912 | 0,07032 | 0,10364 | 0,06713 | €1.728,07 | €3.456,14 | €49,77 | €10,28 |
| Benchmark Donchian breakout 1H | SUI | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,76606 | 0,76606 | 0,75182 | 0,38686 | 0,80165 | €1.377,00 | €2.754,00 | €51,18 | €0,00 |
| Benchmark Donchian breakout 1H | ZEC | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 514,40710 | 508,55000 | 514,36486 | 769,03861 | 481,15276 | €982,86 | €1.965,73 | €0,00 | €22,38 |
| Benchmark Bollinger mean reversion 1H | DOGE | LONG | Bollinger mean reversion | 60m | 2,0x | 0,06944 | 0,06912 | 0,06861 | 0,03507 | 0,07069 | €2.013,01 | €4.026,02 | €48,31 | €-18,78 |
| Benchmark Bollinger mean reversion 1H | SOL | LONG | Bollinger mean reversion | 60m | 2,0x | 75,67913 | 75,72000 | 74,77098 | 38,21796 | 77,04136 | €2.013,07 | €4.026,14 | €48,31 | €2,17 |
| Benchmark trend following EMA 1H | LAB | LONG | Trend following EMA | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €207,05 | €414,10 | €49,69 | €0,00 |
| Benchmark trend following EMA 1H | HYPE | SHORT | Trend following EMA | 60m | 2,0x | 58,72425 | 58,44400 | 58,54319 | 87,79276 | 55,64481 | €1.039,97 | €2.079,94 | €0,00 | €9,93 |
| Benchmark trend following EMA 1H | DOGE | SHORT | Trend following EMA | 60m | 2,0x | 0,06933 | 0,06912 | 0,07044 | 0,10364 | 0,06689 | €1.556,03 | €3.112,05 | €49,79 | €9,25 |
| Scanner Top 5 Long 1H | ONDO | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,40114 | 0,40114 | 0,38834 | 0,20258 | 0,42673 | €828,91 | €1.657,82 | €52,88 | €0,00 |
| Scanner Top 5 Long 1H | LAB | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €219,03 | €438,05 | €52,57 | €0,00 |
| Scanner Top 5 Long 1H | BANK | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,26033 | 0,24918 | 0,22909 | 0,13147 | 0,32281 | €221,39 | €442,77 | €53,13 | €-18,97 |
| Scanner Bottom 5 Short 1H | ESPORTS | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,02150 | 0,02150 | 0,02150 | 0,03214 | 0,01634 | €207,40 | €414,80 | €0,00 | €-0,00 |
| Scanner Bottom 5 Short 1H | DOGE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,06942 | 0,06912 | 0,07042 | 0,10378 | 0,06742 | €1.692,83 | €3.385,67 | €48,75 | €14,44 |
| Scanner Bottom 5 Short 1H | ADA | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,16703 | 0,16703 | 0,16999 | 0,24971 | 0,16112 | €1.381,07 | €2.762,13 | €48,89 | €-0,00 |
| Scanner Top 5 + forza BTC 1H | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39694 | 0,39694 | 0,38539 | 0,20045 | 0,42235 | €898,57 | €1.797,15 | €52,29 | €0,00 |
| Scanner Top 5 + forza BTC 1H | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €216,56 | €433,12 | €51,97 | €0,00 |
| Scanner Top 5 + forza BTC 1H | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,26033 | 0,24918 | 0,22909 | 0,13147 | 0,32906 | €216,24 | €432,48 | €51,90 | €-18,53 |
| Top 5 + BTC — solo MFE | SUI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,76776 | 0,76776 | 0,75508 | 0,38772 | 0,79565 | €1.514,04 | €3.028,08 | €50,00 | €0,00 |
| Top 5 + BTC — solo MFE | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39924 | 0,39924 | 0,38729 | 0,20162 | 0,42552 | €835,46 | €1.670,91 | €50,00 | €0,00 |
| Top 5 + BTC — solo MFE | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,27032 | 0,24918 | 0,23789 | 0,13651 | 0,34169 | €204,03 | €408,05 | €48,97 | €-31,92 |
| Top 5 + BTC — Guard | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39724 | 0,39724 | 0,38434 | 0,20061 | 0,42561 | €756,62 | €1.513,24 | €49,13 | €0,00 |
| Top 5 + BTC — Guard | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €202,47 | €404,95 | €48,59 | €0,00 |
| Top 5 + BTC — Guard | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,26033 | 0,24918 | 0,22909 | 0,13147 | 0,32906 | €204,86 | €409,72 | €49,17 | €-17,55 |
| Top 5 + BTC — BTC≤3 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39974 | 0,39974 | 0,38840 | 0,20187 | 0,42468 | €884,65 | €1.769,29 | €50,18 | €0,00 |
| Top 5 + BTC — BTC≤3 | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €207,87 | €415,74 | €49,89 | €0,00 |
| Top 5 + BTC — BTC≤3 | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,26033 | 0,24918 | 0,22909 | 0,13147 | 0,32906 | €207,68 | €415,35 | €49,84 | €-17,79 |
| Top 5 + BTC — BTC 2–3 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39974 | 0,39974 | 0,38840 | 0,20187 | 0,42468 | €884,65 | €1.769,29 | €50,18 | €0,00 |
| Top 5 + BTC — BTC 2–3 | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €207,87 | €415,74 | €49,89 | €0,00 |
| Top 5 + BTC — Guard + MFE | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39724 | 0,39724 | 0,38434 | 0,20061 | 0,42561 | €756,62 | €1.513,24 | €49,13 | €0,00 |
| Top 5 + BTC — Guard + MFE | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,27048 | 0,24918 | 0,23803 | 0,13659 | 0,34189 | €203,29 | €406,58 | €48,79 | €-32,02 |
| Top 5 + BTC — Guard + BTC≤3 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39974 | 0,39974 | 0,38840 | 0,20187 | 0,42468 | €871,05 | €1.742,11 | €49,41 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €205,84 | €411,68 | €49,40 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,26033 | 0,24918 | 0,22909 | 0,13147 | 0,32906 | €208,27 | €416,53 | €49,98 | €-17,84 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39974 | 0,39974 | 0,38840 | 0,20187 | 0,42468 | €871,05 | €1.742,11 | €49,41 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,27048 | 0,24918 | 0,23803 | 0,13659 | 0,34189 | €205,62 | €411,25 | €49,35 | €-32,39 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39694 | 0,39694 | 0,38539 | 0,20045 | 0,43159 | €861,83 | €1.723,66 | €50,15 | €0,00 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,21338 | €207,96 | €415,92 | €49,91 | €0,00 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,26033 | 0,24918 | 0,22909 | 0,13147 | 0,35405 | €210,29 | €420,58 | €50,47 | €-18,02 |
| Top 5 + BTC — target pieno 3R | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39694 | 0,39694 | 0,38539 | 0,20045 | 0,43159 | €861,83 | €1.723,66 | €50,15 | €0,00 |
| Top 5 + BTC — target pieno 3R | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,21338 | €207,96 | €415,92 | €49,91 | €0,00 |
| Top 5 + BTC — target pieno 3R | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,26033 | 0,24918 | 0,22909 | 0,13147 | 0,35405 | €211,25 | €422,51 | €50,70 | €-18,10 |
| Global Confluence puro 1H | DOGE | SHORT | Global Confluence puro | 60m | 2,0x | 0,06942 | 0,06912 | 0,07053 | 0,10378 | 0,06664 | €1.539,06 | €3.078,12 | €49,25 | €13,13 |
| Combo Trend | ESPORTS | SHORT | Combo Trend | 60m | 2,0x | 0,01883 | 0,01883 | 0,02109 | 0,02815 | 0,01386 | €209,57 | €419,14 | €50,30 | €-0,00 |
| Combo Trend | DOGE | SHORT | Combo Trend | 60m | 2,0x | 0,06929 | 0,06912 | 0,07039 | 0,10358 | 0,06685 | €1.546,95 | €3.093,91 | €49,50 | €7,42 |
| Combo Trend | BANK | LONG | Combo Trend | 60m | 2,0x | 0,24758 | 0,24918 | 0,21787 | 0,12503 | 0,31294 | €205,58 | €411,17 | €49,34 | €2,66 |
| Combo Mean Reversion | BTC | LONG | Combo Mean Reversion | 60m | 2,0x | 64949,16724 | 65323,60000 | 64169,77723 | 32799,32945 | 66196,19125 | €2.006,38 | €4.012,76 | €48,15 | €23,13 |
| Combo Scanner | ONDO | LONG | Combo Scanner | 60m | 2,0x | 0,39694 | 0,39694 | 0,38539 | 0,20045 | 0,42235 | €857,88 | €1.715,77 | €49,92 | €0,00 |
| Combo Scanner | LAB | LONG | Combo Scanner | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €207,54 | €415,08 | €49,81 | €0,00 |
| Combo Scanner | DOGE | SHORT | Combo Scanner | 60m | 2,0x | 0,06942 | 0,06912 | 0,07042 | 0,10378 | 0,06722 | €1.753,42 | €3.506,85 | €50,50 | €14,96 |
| Combo Adaptive — madre | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,40114 | 0,40114 | 0,38834 | 0,20258 | 0,42673 | €809,25 | €1.618,50 | €51,63 | €0,00 |
| Combo Adaptive — madre | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15861 | 0,13958 | 0,08010 | 0,19668 | €213,13 | €426,26 | €51,15 | €0,00 |
| Combo Adaptive — madre | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,06934 | 0,06912 | 0,07033 | 0,10366 | 0,06734 | €1.781,54 | €3.563,09 | €51,31 | €11,11 |
| Combo Adaptive — MFE Trail esistente | ESPORTS | SHORT | Combo Adaptive | 60m | 2,0x | 0,02156 | 0,02156 | 0,02091 | 0,03223 | 0,01638 | €202,62 | €405,24 | €0,00 | €-0,00 |
| Combo Adaptive — MFE Trail esistente | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39784 | 0,39784 | 0,38492 | 0,20091 | 0,42367 | €744,71 | €1.489,41 | €48,35 | €0,00 |
| Combo Adaptive — MFE Trail esistente | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15861 | 0,13958 | 0,08010 | 0,19668 | €201,70 | €403,39 | €48,41 | €0,00 |
| Combo Adaptive — Quality7 | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,40304 | 0,40304 | 0,39140 | 0,20354 | 0,42632 | €859,15 | €1.718,30 | €49,62 | €0,00 |
| Combo Adaptive — Quality7 | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,06933 | 0,06912 | 0,07032 | 0,10364 | 0,06733 | €1.742,21 | €3.484,43 | €50,18 | €10,36 |
| Combo Adaptive — Trend/Transition | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39724 | 0,39724 | 0,38434 | 0,20061 | 0,42303 | €757,94 | €1.515,88 | €49,21 | €0,00 |
| Combo Adaptive — Trend/Transition | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15861 | 0,13958 | 0,08010 | 0,19668 | €206,52 | €413,04 | €49,56 | €0,00 |
| Combo Adaptive — Quality7 + Regime | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,40554 | 0,40554 | 0,39390 | 0,20480 | 0,42882 | €864,27 | €1.728,54 | €49,61 | €0,00 |
| Combo Adaptive — Long Only | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,41951 | €893,67 | €1.787,34 | €49,39 | €0,00 |
| Combo Adaptive — Long Only | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €205,55 | €411,10 | €49,33 | €0,00 |
| Combo Adaptive — parziale 1R | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,41951 | €893,02 | €1.786,04 | €49,36 | €0,00 |
| Combo Adaptive — parziale 1R | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €205,22 | €410,44 | €49,25 | €0,00 |
| Combo Adaptive — parziale 1R | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,06934 | 0,06912 | 0,07033 | 0,10366 | 0,06734 | €1.711,40 | €3.422,80 | €49,29 | €10,67 |
| Combo Adaptive — Quality7 + Regime + parziale 1R | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,40554 | 0,40554 | 0,39390 | 0,20480 | 0,42882 | €864,27 | €1.728,54 | €49,61 | €0,00 |
| Combo Adaptive — 75% a 2R + runner 3R | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,43050 | €902,18 | €1.804,37 | €49,86 | €0,00 |
| Combo Adaptive — 75% a 2R + runner 3R | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,06920 | 0,06912 | 0,07019 | 0,10345 | 0,06621 | €1.731,45 | €3.462,90 | €49,87 | €3,81 |
| Combo Adaptive — 75% a 2R + runner 3R | BANK | LONG | Combo Adaptive | 60m | 2,0x | 0,26033 | 0,24918 | 0,22909 | 0,13147 | 0,35405 | €206,98 | €413,96 | €49,67 | €-17,73 |
| Combo Adaptive — target pieno 3R | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,43050 | €902,18 | €1.804,37 | €49,86 | €0,00 |
| Combo Adaptive — target pieno 3R | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15861 | 0,13958 | 0,08010 | 0,21571 | €207,43 | €414,86 | €49,78 | €0,00 |
| Combo Adaptive — target pieno 3R | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,06920 | 0,06912 | 0,07019 | 0,10345 | 0,06621 | €1.735,05 | €3.470,11 | €49,97 | €3,82 |
| Btc Ema 1H | BTC | SHORT | Trend following EMA | 60m | 3,0x | 64834,39053 | 65323,60000 | 65768,00575 | 86121,68208 | 62967,16008 | €1.149,81 | €3.449,44 | €49,67 | €-26,03 |
| Btc Ema 4H | BTC | LONG | Trend following EMA | 240m | 2,0x | 65410,57950 | 65323,60000 | 63931,54687 | 33032,34265 | 69108,16107 | €1.105,63 | €2.211,26 | €50,00 | €-2,94 |
| Btc Donchian 1H | BTC | SHORT | Donchian breakout 20 barre | 60m | 3,0x | 64923,19276 | 65323,60000 | 65754,20963 | 86239,64105 | 63261,15903 | €1.293,96 | €3.881,87 | €49,69 | €-23,94 |
| Btc Donchian 4H | BTC | LONG | Donchian breakout 20 barre | 240m | 2,0x | 65410,57950 | 65323,60000 | 63931,54687 | 33032,34265 | 69551,87112 | €1.105,63 | €2.211,26 | €50,00 | €-2,94 |
| Btc Bollinger 4H | BTC | SHORT | Bollinger mean reversion | 240m | 2,0x | 66588,49964 | 65323,60000 | 65621,81812 | 99549,80696 | 64307,80290 | €1.313,84 | €2.627,69 | €0,00 | €49,91 |
| Btc Adaptive 1H | BTC | SHORT | Combo Adaptive | 60m | 3,0x | 64713,55470 | 65323,60000 | 65645,42989 | 85961,17183 | 62849,80432 | €1.156,05 | €3.468,15 | €49,94 | €-32,69 |
| Btc Adaptive 4H | BTC | LONG | Combo Adaptive | 240m | 2,0x | 66171,85172 | 65323,60000 | 64592,42491 | 33416,78512 | 70120,41876 | €1.047,40 | €2.094,81 | €50,00 | €-26,85 |
| Sol Ema 1H | SOL | SHORT | Trend following EMA | 60m | 3,0x | 75,65487 | 75,72000 | 76,74430 | 100,49488 | 73,47601 | €1.150,16 | €3.450,47 | €49,69 | €-2,97 |
| Sol Donchian 1H | SOL | SHORT | Donchian breakout 20 barre | 60m | 3,0x | 75,65487 | 75,72000 | 76,62325 | 100,49488 | 73,71810 | €1.301,74 | €3.905,22 | €49,99 | €-3,36 |
| Sol Donchian 4H | SOL | SHORT | Donchian breakout 20 barre | 240m | 2,0x | 75,96380 | 75,72000 | 78,23939 | 113,56589 | 69,59218 | €830,21 | €1.660,43 | €49,74 | €5,33 |
| Sol Bollinger 1H | SOL | LONG | Bollinger mean reversion | 60m | 3,0x | 75,68513 | 75,72000 | 74,77691 | 50,83518 | 77,04747 | €1.381,14 | €4.143,42 | €49,72 | €1,91 |
| Sol Bollinger 4H | SOL | SHORT | Bollinger mean reversion | 240m | 2,0x | 78,45931 | 75,72000 | 76,84028 | 117,29666 | 74,81402 | €968,56 | €1.937,11 | €0,00 | €67,63 |
| Sol Adaptive 1H | SOL | LONG | Combo Adaptive | 60m | 3,0x | 76,29126 | 75,72000 | 75,19266 | 51,24229 | 78,48844 | €1.149,09 | €3.447,26 | €49,64 | €-25,81 |
| Sol Adaptive 4H | SOL | SHORT | Combo Adaptive | 240m | 2,0x | 75,96380 | 75,72000 | 78,44626 | 113,56589 | 69,75767 | €761,04 | €1.522,08 | €49,74 | €4,89 |
| Eth Ema 1H | ETH | SHORT | Trend following EMA | 60m | 3,0x | 1873,22528 | 1877,37000 | 1900,19972 | 2488,26758 | 1819,27639 | €1.138,34 | €3.415,02 | €49,18 | €-7,56 |
| Eth Adaptive 1H | ETH | SHORT | Combo Adaptive | 60m | 3,0x | 1873,22528 | 1877,37000 | 1900,19972 | 2488,26758 | 1819,27639 | €1.146,74 | €3.440,21 | €49,54 | €-7,61 |
| Doge Ema 1H | DOGE | SHORT | Trend following EMA | 60m | 3,0x | 0,06942 | 0,06912 | 0,07042 | 0,09221 | 0,06742 | €1.173,45 | €3.520,36 | €50,69 | €15,02 |
| Doge Donchian 1H | DOGE | SHORT | Donchian breakout 20 barre | 60m | 3,0x | 0,06940 | 0,06912 | 0,07045 | 0,09218 | 0,06729 | €1.095,98 | €3.287,94 | €49,99 | €13,08 |
| Doge Bollinger 1H | DOGE | LONG | Bollinger mean reversion | 60m | 3,0x | 0,06944 | 0,06912 | 0,06861 | 0,04664 | 0,07069 | €1.381,14 | €4.143,42 | €49,72 | €-19,32 |
| Master Adaptive V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39854 | 0,39854 | 0,38677 | 0,20126 | 0,42207 | €833,00 | €1.665,99 | €49,19 | €0,00 |
| Master Adaptive V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €203,80 | €407,60 | €48,91 | €0,00 |
| Master Adaptive V1 | BANK | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,25383 | 0,24918 | 0,22337 | 0,12818 | 0,31475 | €202,68 | €405,37 | €48,64 | €-7,43 |
| Master Adaptive No Alt V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39854 | 0,39854 | 0,38677 | 0,20126 | 0,42207 | €833,00 | €1.665,99 | €49,19 | €0,00 |
| Master Adaptive No Alt V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €203,80 | €407,60 | €48,91 | €0,00 |
| Master Adaptive No Alt V1 | BANK | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,25383 | 0,24918 | 0,22337 | 0,12818 | 0,31475 | €202,68 | €405,37 | €48,64 | €-7,43 |
| Master Adaptive Strict3 V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,41951 | €887,07 | €1.774,14 | €49,03 | €0,00 |
| Master Adaptive Strict3 V1 | BANK | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,27032 | 0,24918 | 0,23789 | 0,13651 | 0,33520 | €199,89 | €399,79 | €47,97 | €-31,27 |
| Master Adaptive Expanded V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39854 | 0,39854 | 0,38677 | 0,20126 | 0,42207 | €833,00 | €1.665,99 | €49,19 | €0,00 |
| Master Adaptive Expanded V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €203,80 | €407,60 | €48,91 | €0,00 |
| Master Adaptive Expanded V1 | BANK | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,25627 | 0,24918 | 0,22552 | 0,12942 | 0,31778 | €203,36 | €406,71 | €48,81 | €-11,25 |
| Master Adaptive Gb20 V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,40304 | 0,40304 | 0,39140 | 0,20354 | 0,42632 | €848,64 | €1.697,27 | €49,02 | €0,00 |
| Master Adaptive Gb20 V1 | BANK | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,25875 | 0,24918 | 0,22770 | 0,13067 | 0,32085 | €200,57 | €401,14 | €48,14 | €-14,84 |
| Master Adaptive Runner25 V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39854 | 0,39854 | 0,38677 | 0,20126 | 0,43384 | €833,00 | €1.665,99 | €49,19 | €0,00 |
| Master Adaptive Runner25 V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,21338 | €203,80 | €407,60 | €48,91 | €0,00 |
| Master Adaptive Runner25 V1 | BANK | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,25383 | 0,24918 | 0,22337 | 0,12818 | 0,34521 | €202,68 | €405,37 | €48,64 | €-7,43 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Master Adaptive Gb20 V1 | RIF | LONG | 2026-07-24T04:38:35+00:00 | 0,11359 | €22,95 | 0,48 | STOP_STRESS_SLIPPAGE |
| Combo Trend | BANK | LONG | 2026-07-24T04:08:34+00:00 | 0,24375 | €-51,35 | -1,03 | STOP_STRESS_SLIPPAGE |
| Rapida V1 — senza PEPE | BANK | LONG | 2026-07-24T04:08:34+00:00 | 0,24420 | €-53,07 | -1,05 | STOP_STRESS_SLIPPAGE |
| Benchmark Donchian breakout 1H | HYPE | SHORT | 2026-07-24T03:53:33+00:00 | 58,38314 | €17,07 | 0,34 | STOP |
| Rapida V3 — senza ESPORTS | BANK | LONG | 2026-07-24T03:53:33+00:00 | 0,25715 | €-7,20 | -0,14 | STOP_STRESS_SLIPPAGE |
| Rapida V3 — no volatilità HIGH | BANK | LONG | 2026-07-24T03:53:33+00:00 | 0,25715 | €-7,18 | -0,14 | STOP_STRESS_SLIPPAGE |
| Rapida V3 — Long Only | BANK | LONG | 2026-07-24T03:53:33+00:00 | 0,25715 | €-7,07 | -0,14 | STOP_STRESS_SLIPPAGE |
| Rapida V1 — target pieno 2R | BANK | LONG | 2026-07-24T03:53:33+00:00 | 0,25715 | €-7,16 | -0,14 | STOP_STRESS_SLIPPAGE |
| Forza relativa 1H V2 | ZEC | SHORT | 2026-07-24T03:38:34+00:00 | 510,60730 | €6,59 | 0,13 | STOP |
| Forza relativa 1H V1 | ZEC | SHORT | 2026-07-24T03:38:34+00:00 | 511,01998 | €-2,04 | -0,04 | STOP |
| Benchmark trend following EMA 1H | ZEC | SHORT | 2026-07-24T03:38:34+00:00 | 511,54998 | €-1,87 | -0,04 | STOP |
| Rapida V3 — senza ESPORTS | DOGE | SHORT | 2026-07-24T03:38:34+00:00 | 0,06943 | €-6,71 | -0,13 | STOP |

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
| MAIN | Principale 4H | 45/30 | 18/30 | 0,96 | 0,91 | -0,02R | €-2,94 | 4,26% | COERENTE − | BOCCIATA RESEARCH |
| RSI_EXTREME_LONG_15M | Scalp RSI Long 25 · prudente · 5x (riferimento tra 9 varianti) | 8/30 | 4/30 | 0,30 | 0,22 | -0,56R | €-5,00 | 0,34% | COERENTE − | RACCOLTA RESEARCH |
| RSI_EXTREME_SHORT_15M | Scalp RSI Short 75 · prudente · 5x (riferimento tra 9 varianti) | 7/30 | 6/30 | 0,62 | 0,18 | -0,24R | €-5,86 | 0,36% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_1H_BALANCED | Bilanciata 1H V1 | 148/30 | 37/30 | 0,97 | 1,46 | -0,02R | €9,09 | 2,30% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_BALANCED_V2 | Bilanciata 1H V2 | 28/30 | 22/30 | 1,52 | 1,16 | 0,29R | €3,60 | 2,75% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_1H_BALANCED_V3 | Bilanciata 1H V3 Filtered | 55/30 | 31/30 | 1,15 | 1,30 | 0,09R | €7,87 | 2,20% | COERENTE + | PRONTA PER REVISIONE LIVE |
| SHADOW_1H_FAST | Rapida 1H V1 — madre | 174/30 | 63/30 | 0,90 | 0,96 | -0,06R | €-0,96 | 6,76% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | Rapida V1 — Long + BTC 1–3 + score <7,5 | 8/30 | 6/30 | 1,38 | 0,62 | 0,20R | €-7,40 | 1,55% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | Rapida V1 — no HIGH + score <7,5 | 38/30 | 28/30 | 0,88 | 1,00 | -0,08R | €-0,04 | 2,83% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_NO_PEPE_V1 | Rapida V1 — senza PEPE | 41/30 | 24/30 | 0,77 | 1,08 | -0,15R | €1,64 | 2,10% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_V1 | Rapida V1 — score 6–7,5 | 27/30 | 26/30 | 1,07 | 1,25 | 0,04R | €4,93 | 2,49% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_TP2_V1 | Rapida V1 — target pieno 2R | 36/30 | 25/30 | 0,70 | 0,89 | -0,23R | €-2,41 | 2,58% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V2 | Rapida 1H V2 | 5/30 | 5/30 | 0,61 | 0,82 | -0,29R | €-3,78 | 1,69% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3 | Rapida 1H V3 Filtered — madre | 82/30 | 55/30 | 0,99 | 1,16 | -0,00R | €3,09 | 2,89% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_CAP75_V1 | Rapida V3 — score <7,5 | 33/30 | 23/30 | 0,87 | 1,10 | -0,08R | €2,19 | 2,49% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | Rapida V3 — qualità completa + profit lock | 19/30 | 17/30 | 0,79 | 0,70 | -0,14R | €-9,67 | 3,16% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | Rapida V3 — Long + no HIGH + score <7,5 | 19/30 | 17/30 | 0,79 | 0,74 | -0,14R | €-7,59 | 2,77% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | Rapida V3 — Long Only | 23/30 | 22/30 | 0,59 | 0,72 | -0,30R | €-7,67 | 2,93% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | Rapida V3 — no volatilità HIGH | 37/30 | 29/30 | 0,82 | 0,96 | -0,12R | €-0,91 | 2,96% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | Rapida V3 — senza ESPORTS | 38/30 | 28/30 | 0,78 | 1,00 | -0,15R | €0,02 | 2,49% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_4H_WIDE | Ampia 4H | 42/30 | 13/30 | 0,97 | 1,09 | -0,03R | €2,74 | 2,56% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_BOLLINGER_MR_1H | Benchmark Bollinger mean reversion 1H | 34/30 | 25/30 | 1,04 | 1,52 | 0,03R | €9,29 | 2,06% | COERENTE + | BOCCIATA RESEARCH |
| SHADOW_BTC_ADAPTIVE_1H | Btc Adaptive 1H | 1/30 | 2/30 | 0,00 | 0,78 | -1,11R | €-5,87 | 0,89% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_ADAPTIVE_4H | Btc Adaptive 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,64% | n/a | RACCOLTA RESEARCH |
| SHADOW_BTC_BOLLINGER_1H | Btc Bollinger 1H | 2/30 | 2/30 | ∞ | ∞ | 1,37R | €49,98 | 0,31% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_BTC_BOLLINGER_4H | Btc Bollinger 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,28% | n/a | RACCOLTA RESEARCH |
| SHADOW_BTC_DONCHIAN_1H | Btc Donchian 1H | 2/30 | 3/30 | 0,00 | 0,43 | -1,12R | €-20,81 | 1,49% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_DONCHIAN_4H | Btc Donchian 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,68% | n/a | RACCOLTA RESEARCH |
| SHADOW_BTC_EMA_1H | Btc Ema 1H | 4/30 | 4/30 | 0,57 | 0,60 | -0,36R | €-16,40 | 1,56% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_EMA_4H | Btc Ema 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,68% | n/a | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE | Combo Adaptive — madre | 89/30 | 21/30 | 1,20 | 1,78 | 0,13R | €12,52 | 1,31% | COERENTE + | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | Combo Adaptive — Long Only | 23/30 | 5/30 | 0,65 | 0,42 | -0,27R | €-26,52 | 2,34% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | Combo Adaptive — MFE Trail esistente | 57/30 | 27/30 | 1,08 | 0,45 | 0,05R | €-11,76 | 4,11% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | Combo Adaptive — parziale 1R | 34/30 | 11/30 | 0,76 | 0,64 | -0,18R | €-12,79 | 2,24% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | Combo Adaptive — Quality7 + Regime + parziale 1R | 3/30 | 4/30 | 0,00 | 0,32 | -1,07R | €-27,31 | 1,95% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | Combo Adaptive — Quality7 + Regime | 3/30 | 4/30 | 0,00 | 0,18 | -1,07R | €-32,87 | 1,95% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | Combo Adaptive — Quality7 | 6/30 | 6/30 | 0,38 | 1,34 | -0,54R | €6,03 | 1,51% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | Combo Adaptive — Trend/Transition | 24/30 | 9/30 | 0,26 | 0,80 | -0,69R | €-6,15 | 2,18% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | Combo Adaptive — 75% a 2R + runner 3R | 25/30 | 13/30 | 0,52 | 0,83 | -0,43R | €-5,17 | 2,12% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | Combo Adaptive — target pieno 3R | 25/30 | 9/30 | 0,52 | 0,98 | -0,43R | €-0,50 | 1,41% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_MEAN_REVERSION | Combo Mean Reversion | 14/30 | 12/30 | 1,07 | 1,16 | 0,04R | €4,50 | 2,31% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_COMBO_SCANNER | Combo Scanner | 58/30 | 23/30 | 1,51 | 1,20 | 0,30R | €5,12 | 2,66% | COERENTE + | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_COMBO_TREND | Combo Trend | 69/30 | 25/30 | 1,10 | 0,82 | 0,07R | €-5,56 | 3,58% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_DOGE_BOLLINGER_1H | Doge Bollinger 1H | 1/30 | 1/30 | 0,00 | 0,00 | -1,13R | €-55,79 | 0,93% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_DOGE_DONCHIAN_1H | Doge Donchian 1H | 2/30 | 3/30 | 1,67 | 0,96 | 0,38R | €-0,85 | 0,96% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_DOGE_EMA_1H | Doge Ema 1H | 3/30 | 6/30 | 3,40 | 2,24 | 0,89R | €23,11 | 1,36% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_DONCHIAN_1H | Benchmark Donchian breakout 1H | 39/30 | 18/30 | 1,02 | 1,44 | 0,01R | €9,70 | 2,12% | COERENTE + | BOCCIATA RESEARCH |
| SHADOW_EMA_TREND_1H | Benchmark trend following EMA 1H | 76/30 | 16/30 | 1,05 | 0,87 | 0,03R | €-3,38 | 2,25% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_ETH_ADAPTIVE_1H | Eth Adaptive 1H | 3/30 | 4/30 | 0,85 | 0,16 | -0,11R | €-23,05 | 1,11% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_BOLLINGER_1H | Eth Bollinger 1H | 1/30 | 1/30 | 0,00 | ∞ | -1,13R | €15,45 | 0,51% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_ETH_DONCHIAN_1H | Eth Donchian 1H | 3/30 | 3/30 | 0,84 | 0,84 | -0,12R | €-5,82 | 1,38% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_EMA_1H | Eth Ema 1H | 3/30 | 6/30 | 0,85 | 0,25 | -0,11R | €-27,46 | 1,79% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_EMA_4H | Eth Ema 4H | 1/30 | 1/30 | 0,00 | 0,00 | -1,06R | €-52,88 | 0,68% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_GLOBAL_PURE | Global Confluence puro 1H | 3/30 | 8/30 | 3,47 | 0,45 | 0,91R | €-18,75 | 2,92% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | Master Adaptive Expanded V1 | 18/30 | 7/30 | 0,53 | 0,29 | -0,39R | €-32,57 | 2,80% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | Master Adaptive Gb20 V1 | 18/30 | 27/30 | 0,38 | 0,44 | -0,55R | €-13,21 | 4,16% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | Master Adaptive No Alt V1 | 18/30 | 5/30 | 0,38 | 0,00 | -0,55R | €-54,20 | 3,19% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | Master Adaptive Runner25 V1 | 14/30 | 5/30 | 0,22 | 0,00 | -0,77R | €-54,20 | 3,19% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | Master Adaptive Strict3 V1 | 18/30 | 12/30 | 0,38 | 0,32 | -0,55R | €-33,66 | 4,59% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_V1 | Master Adaptive V1 | 18/30 | 5/30 | 0,38 | 0,00 | -0,55R | €-54,20 | 3,19% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_RELATIVE_STRENGTH | Forza relativa 1H V1 | 104/30 | 23/30 | 0,98 | 0,83 | -0,02R | €-3,24 | 3,25% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_RELATIVE_STRENGTH_V2 | Forza relativa 1H V2 | 33/30 | 29/30 | 1,50 | 1,32 | 0,30R | €9,00 | 3,69% | COERENTE + | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_SCANNER_BOTTOM5_SHORT | Scanner Bottom 5 Short 1H | 37/30 | 22/30 | 0,77 | 0,61 | -0,15R | €-10,10 | 5,48% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC | Scanner Top 5 + forza BTC 1H | 57/30 | 22/30 | 1,44 | 1,96 | 0,27R | €17,32 | 2,01% | COERENTE + | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | Top 5 + BTC — BTC 2–3 | 10/30 | 3/30 | 0,86 | 0,54 | -0,10R | €-16,53 | 2,22% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | Top 5 + BTC — BTC≤3 | 16/30 | 4/30 | 0,69 | 0,73 | -0,24R | €-7,45 | 2,20% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | Top 5 + BTC — Guard + BTC≤3 + MFE | 11/30 | 11/30 | 0,80 | 0,50 | -0,15R | €-15,03 | 2,30% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | Top 5 + BTC — Guard + BTC≤3 | 11/30 | 4/30 | 0,80 | 0,99 | -0,15R | €-0,40 | 1,64% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | Top 5 + BTC — Guard + MFE | 14/30 | 14/30 | 0,57 | 0,37 | -0,35R | €-19,80 | 3,47% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | Top 5 + BTC — Guard | 14/30 | 7/30 | 0,57 | 0,41 | -0,35R | €-23,63 | 3,31% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | Top 5 + BTC — solo MFE | 19/30 | 10/30 | 0,73 | 0,21 | -0,21R | €-20,42 | 3,30% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | Top 5 + BTC — 75% a 2,2R + runner 3R | 14/30 | 8/30 | 0,46 | 1,59 | -0,49R | €11,95 | 2,33% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | Top 5 + BTC — target pieno 3R | 14/30 | 8/30 | 0,46 | 1,87 | -0,49R | €17,72 | 2,33% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_LONG | Scanner Top 5 Long 1H | 70/30 | 30/30 | 1,34 | 2,18 | 0,21R | €20,93 | 2,70% | COERENTE + | PRONTA PER REVISIONE LIVE |
| SHADOW_SOL_ADAPTIVE_1H | Sol Adaptive 1H | 3/30 | 3/30 | 0,86 | 0,34 | -0,11R | €-23,97 | 1,85% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_ADAPTIVE_4H | Sol Adaptive 4H | 1/30 | 1/30 | 0,00 | 0,00 | -1,05R | €-51,83 | 0,59% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_BOLLINGER_1H | Sol Bollinger 1H | 1/30 | 1/30 | 0,00 | 0,00 | -1,13R | €-55,79 | 0,81% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_BOLLINGER_4H | Sol Bollinger 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,40% | n/a | RACCOLTA RESEARCH |
| SHADOW_SOL_DONCHIAN_1H | Sol Donchian 1H | 2/30 | 2/30 | 0,00 | 0,41 | -1,12R | €-1,31 | 0,79% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_DONCHIAN_4H | Sol Donchian 4H | 1/30 | 1/30 | 0,00 | 0,00 | -1,06R | €-52,00 | 0,60% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_EMA_1H | Sol Ema 1H | 3/30 | 3/30 | 0,86 | 0,42 | -0,11R | €-20,89 | 1,67% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_EMA_4H | Sol Ema 4H | 1/30 | 1/30 | 0,00 | 0,00 | -1,06R | €-52,00 | 0,56% | COERENTE − | RACCOLTA RESEARCH |

Per le famiglie RSI con più configurazioni di leva o margine, il lato paper usa il conto con il maggior numero di eventi indipendenti; i conti duplicati non vengono aggregati.
`PRONTA PER REVISIONE LIVE` non invia ordini e non sposta capitale: abilita soltanto una revisione manuale finale.

## 🎯 DOGE Rejection Short — conto dedicato €3.600

Simulazione separata **paper only**: capitale/margine iniziale **€3.600**, leva **5x**, esposizione iniziale **€18.000**. Non modifica i conti paper da €10.000 e non invia ordini reali.

- Stato: **WAITING**
- Prezzo DOGE: **0.06912**
- Pre-allarme: **0.0765**; zona armata: **0.0775**; trigger rejection: **0.078**
- Invalidazione prima dell’entrata: chiusura 15m sopra **0.07966**

| Capitale iniziale | Balance | Equity | P&L aperto | Eventi chiusi | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- |
| €3.600,00 | €3.600,00 | €3.600,00 | €0,00 | 0 | 0,00% | 0,00 | 0,00% |

### Filtri correnti

| Filtro | Valore | Stato |
| --- | --- | --- |
| Dati mercato | FRESH | OK |
| Candela 15m | 23.9 min | OK |
| Global DOGE | -6.0 | OK |
| Classic raw | -11.0 | OK |
| DOGE/BTC raw | -6.0 | OK |
| Pattern ribassista | MATURO | OK |
| BTC sotto filtro | 65323.6 | OK |

### Ultima candela 15m valutata

- Rejection accettata: **NO**; motivo: **trigger_touched, entry_not_chased, upper_wick, bearish_confirmation**
- High **0.0692**; close **0.06919**; wick alta **6.2%**; volume **x0.18**

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

- Regime: **RANGE**
- Famiglia: **RANGE**
- Confidenza: **79,60%**
- Volatilità: **NORMAL**
- Rotazione strategie: **SOLO OSSERVAZIONE — nessun peso operativo viene ancora modificato**
- Motivo: Direzione poco definita: score BTC +1.0, breadth EMA50 33%, ADX 21.4.
- BTC trend score: **1,00**; ADX: **21,40**; breadth sopra EMA50: **33,33%**
- Mediana alt vs BTC: **-1,20%**; dispersione: **15,09%**

- Aperti in questo ciclo: **2**
- Chiusi in questo ciclo: **0**
- Posizioni research aperte: **434**
- Trade research chiusi: **2069**
- Eventi di mercato indipendenti chiusi: **592**
- Segnali sovrapposti saltati sullo stesso asset/profilo: **8357**
- Posizioni Research V1 senza regime scartate durante la migrazione: **28**

### Risultati complessivi per strategia

| Profilo | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| MAIN | 14 | 45 | 45 | 33,33% | 0,96 | -0,02R | €-10,84 |
| RSI_EXTREME_LONG_15M | 0 | 8 | 8 | 25,00% | 0,30 | -0,56R | €-45,05 |
| RSI_EXTREME_SHORT_15M | 0 | 7 | 7 | 28,57% | 0,62 | -0,24R | €-16,64 |
| Bilanciata 1H V1 | 15 | 148 | 148 | 33,78% | 0,97 | -0,02R | €-29,36 |
| Bilanciata 1H V2 | 7 | 32 | 28 | 43,75% | 1,52 | 0,29R | €94,15 |
| Bilanciata 1H V3 Filtered | 12 | 55 | 55 | 38,18% | 1,15 | 0,09R | €51,91 |
| Rapida 1H V1 | 10 | 174 | 174 | 38,51% | 0,90 | -0,06R | €-112,09 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | 2 | 8 | 8 | 50,00% | 1,38 | 0,20R | €16,20 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | 10 | 38 | 38 | 39,47% | 0,88 | -0,08R | €-29,51 |
| SHADOW_1H_FAST_NO_PEPE_V1 | 10 | 41 | 41 | 36,59% | 0,77 | -0,15R | €-62,25 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | 6 | 27 | 27 | 44,44% | 1,07 | 0,04R | €11,04 |
| SHADOW_1H_FAST_TP2_V1 | 12 | 36 | 36 | 27,78% | 0,70 | -0,23R | €-83,80 |
| Rapida 1H V2 | 2 | 6 | 5 | 33,33% | 0,61 | -0,29R | €-17,63 |
| Rapida 1H V3 Filtered | 8 | 82 | 82 | 41,46% | 0,99 | -0,00R | €-3,34 |
| SHADOW_1H_FAST_V3_CAP75_V1 | 8 | 33 | 33 | 39,39% | 0,87 | -0,08R | €-26,99 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | 1 | 19 | 19 | 36,84% | 0,79 | -0,14R | €-26,97 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | 1 | 19 | 19 | 36,84% | 0,79 | -0,14R | €-26,97 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | 1 | 23 | 23 | 30,43% | 0,59 | -0,30R | €-69,86 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | 8 | 37 | 37 | 37,84% | 0,82 | -0,12R | €-44,18 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | 8 | 38 | 38 | 36,84% | 0,78 | -0,15R | €-55,70 |
| SHADOW_4H_WIDE | 20 | 42 | 42 | 26,19% | 0,97 | -0,03R | €-10,68 |
| SHADOW_BOLLINGER_MR_1H | 3 | 34 | 34 | 44,12% | 1,04 | 0,03R | €9,16 |
| SHADOW_BTC_ADAPTIVE_1H | 2 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_BTC_ADAPTIVE_4H | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_BOLLINGER_1H | 0 | 2 | 2 | 100,00% | ∞ | 1,37R | €27,33 |
| SHADOW_BTC_BOLLINGER_4H | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_DONCHIAN_1H | 2 | 2 | 2 | 0,00% | 0,00 | -1,12R | €-22,50 |
| SHADOW_BTC_DONCHIAN_4H | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_EMA_1H | 1 | 4 | 4 | 25,00% | 0,57 | -0,36R | €-14,44 |
| SHADOW_BTC_EMA_4H | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_ADAPTIVE | 18 | 89 | 89 | 39,33% | 1,20 | 0,13R | €112,55 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | 4 | 23 | 23 | 26,09% | 0,65 | -0,27R | €-63,06 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | 17 | 57 | 57 | 36,84% | 1,08 | 0,05R | €29,99 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | 14 | 34 | 34 | 29,41% | 0,76 | -0,18R | €-61,94 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | 2 | 3 | 3 | 0,00% | 0,00 | -1,07R | €-32,05 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | 2 | 3 | 3 | 0,00% | 0,00 | -1,07R | €-32,05 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | 4 | 6 | 6 | 16,67% | 0,38 | -0,54R | €-32,52 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | 3 | 24 | 24 | 12,50% | 0,26 | -0,69R | €-166,75 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | 15 | 25 | 25 | 16,00% | 0,52 | -0,43R | €-106,34 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | 15 | 25 | 25 | 16,00% | 0,52 | -0,43R | €-106,34 |
| SHADOW_COMBO_MEAN_REVERSION | 2 | 14 | 14 | 42,86% | 1,07 | 0,04R | €5,86 |
| SHADOW_COMBO_SCANNER | 6 | 58 | 58 | 43,10% | 1,51 | 0,30R | €175,63 |
| SHADOW_COMBO_TREND | 16 | 69 | 69 | 34,78% | 1,10 | 0,07R | €45,75 |
| SHADOW_DOGE_BOLLINGER_1H | 1 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,33 |
| SHADOW_DOGE_DONCHIAN_1H | 1 | 2 | 2 | 50,00% | 1,67 | 0,38R | €7,50 |
| SHADOW_DOGE_EMA_1H | 1 | 3 | 3 | 66,67% | 3,40 | 0,89R | €26,67 |
| SHADOW_DONCHIAN_1H | 12 | 39 | 39 | 30,77% | 1,02 | 0,01R | €4,85 |
| SHADOW_EMA_TREND_1H | 17 | 76 | 76 | 32,89% | 1,05 | 0,03R | €24,66 |
| SHADOW_ETH_ADAPTIVE_1H | 1 | 3 | 3 | 33,33% | 0,85 | -0,11R | €-3,33 |
| SHADOW_ETH_BOLLINGER_1H | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,33 |
| SHADOW_ETH_DONCHIAN_1H | 0 | 3 | 3 | 33,33% | 0,84 | -0,12R | €-3,61 |
| SHADOW_ETH_EMA_1H | 1 | 3 | 3 | 33,33% | 0,85 | -0,11R | €-3,22 |
| SHADOW_ETH_EMA_4H | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,57 |
| SHADOW_GLOBAL_PURE | 1 | 3 | 3 | 66,67% | 3,47 | 0,91R | €27,17 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | 6 | 18 | 18 | 22,22% | 0,53 | -0,39R | €-69,68 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | 6 | 18 | 18 | 16,67% | 0,38 | -0,55R | €-98,89 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | 6 | 18 | 18 | 16,67% | 0,38 | -0,55R | €-98,74 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | 6 | 14 | 14 | 7,14% | 0,22 | -0,77R | €-108,31 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | 2 | 18 | 18 | 16,67% | 0,38 | -0,55R | €-98,60 |
| SHADOW_MASTER_ADAPTIVE_V1 | 6 | 18 | 18 | 16,67% | 0,38 | -0,55R | €-98,89 |
| Forza relativa 1H V1 | 14 | 104 | 104 | 30,77% | 0,98 | -0,02R | €-16,73 |
| Forza relativa 1H V2 | 7 | 36 | 33 | 41,67% | 1,50 | 0,30R | €108,71 |
| SHADOW_SCANNER_BOTTOM5_SHORT | 9 | 37 | 37 | 27,03% | 0,77 | -0,15R | €-56,93 |
| SHADOW_SCANNER_TOP5_BTC | 5 | 57 | 57 | 40,35% | 1,44 | 0,27R | €151,77 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | 3 | 10 | 10 | 30,00% | 0,86 | -0,10R | €-10,17 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | 4 | 16 | 16 | 25,00% | 0,69 | -0,24R | €-39,05 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | 3 | 11 | 11 | 27,27% | 0,80 | -0,15R | €-16,21 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | 3 | 11 | 11 | 27,27% | 0,80 | -0,15R | €-16,21 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | 3 | 14 | 14 | 21,43% | 0,57 | -0,35R | €-48,79 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | 3 | 14 | 14 | 21,43% | 0,57 | -0,35R | €-48,79 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | 5 | 19 | 19 | 26,32% | 0,73 | -0,21R | €-39,92 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | 5 | 14 | 14 | 14,29% | 0,46 | -0,49R | €-68,15 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | 5 | 14 | 14 | 14,29% | 0,46 | -0,49R | €-68,15 |
| SHADOW_SCANNER_TOP5_LONG | 5 | 70 | 70 | 41,43% | 1,34 | 0,21R | €145,94 |
| SHADOW_SOL_ADAPTIVE_1H | 2 | 3 | 3 | 33,33% | 0,86 | -0,11R | €-3,18 |
| SHADOW_SOL_ADAPTIVE_4H | 1 | 1 | 1 | 0,00% | 0,00 | -1,05R | €-10,52 |
| SHADOW_SOL_BOLLINGER_1H | 1 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,33 |
| SHADOW_SOL_BOLLINGER_4H | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SOL_DONCHIAN_1H | 1 | 2 | 2 | 0,00% | 0,00 | -1,12R | €-22,33 |
| SHADOW_SOL_DONCHIAN_4H | 1 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,56 |
| SHADOW_SOL_EMA_1H | 1 | 3 | 3 | 33,33% | 0,86 | -0,11R | €-3,18 |
| SHADOW_SOL_EMA_4H | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,56 |

### Matrice strategia × regime all’entrata

| Profilo | Regime entrata | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| MAIN | ALT_ROTATION_DOWN | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| MAIN | ALT_ROTATION_UP | 3 | 3 | 3 | 0,00% | 0,00 | -1,01R | €-30,40 |
| MAIN | RANGE | 4 | 15 | 15 | 26,67% | 0,70 | -0,23R | €-33,95 |
| MAIN | RANGE_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| MAIN | TRANSITION | 1 | 7 | 7 | 42,86% | 1,45 | 0,26R | €18,34 |
| MAIN | TREND_UP | 1 | 16 | 16 | 37,50% | 1,15 | 0,10R | €15,71 |
| MAIN | TREND_UP_HIGH_VOL | 3 | 3 | 3 | 33,33% | 0,98 | -0,01R | €-0,40 |
| RSI_EXTREME_LONG_15M | RANGE | 0 | 6 | 6 | 0,00% | 0,00 | -1,07R | €-64,49 |
| RSI_EXTREME_LONG_15M | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,29R | €12,88 |
| RSI_EXTREME_LONG_15M | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 0,66R | €6,56 |
| RSI_EXTREME_SHORT_15M | ALT_ROTATION_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 1,47R | €14,67 |
| RSI_EXTREME_SHORT_15M | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,90 |
| RSI_EXTREME_SHORT_15M | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -0,41R | €-4,13 |
| RSI_EXTREME_SHORT_15M | TREND_UP | 0 | 4 | 4 | 25,00% | 0,44 | -0,41R | €-16,27 |
| Bilanciata 1H V1 | ALT_ROTATION_DOWN | 4 | 8 | 8 | 37,50% | 1,08 | 0,05R | €4,12 |
| Bilanciata 1H V1 | ALT_ROTATION_UP | 0 | 14 | 14 | 50,00% | 1,84 | 0,44R | €61,99 |
| Bilanciata 1H V1 | RANGE | 7 | 33 | 33 | 33,33% | 0,96 | -0,02R | €-8,15 |
| Bilanciata 1H V1 | RANGE_HIGH_VOL | 0 | 11 | 11 | 0,00% | 0,00 | -1,07R | €-118,08 |
| Bilanciata 1H V1 | TRANSITION | 0 | 29 | 29 | 31,03% | 0,90 | -0,07R | €-19,92 |
| Bilanciata 1H V1 | TREND_UP | 2 | 42 | 42 | 40,48% | 1,31 | 0,19R | €78,29 |
| Bilanciata 1H V1 | TREND_UP_HIGH_VOL | 2 | 11 | 11 | 27,27% | 0,68 | -0,25R | €-27,61 |
| Bilanciata 1H V2 | ALT_ROTATION_UP | 0 | 6 | 5 | 66,67% | 3,52 | 0,92R | €55,11 |
| Bilanciata 1H V2 | RANGE | 4 | 11 | 9 | 36,36% | 1,23 | 0,13R | €14,59 |
| Bilanciata 1H V2 | TRANSITION | 3 | 15 | 14 | 40,00% | 1,26 | 0,16R | €24,46 |
| Bilanciata 1H V3 Filtered | ALT_ROTATION_DOWN | 3 | 7 | 7 | 42,86% | 1,39 | 0,23R | €16,21 |
| Bilanciata 1H V3 Filtered | ALT_ROTATION_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,05R | €-20,99 |
| Bilanciata 1H V3 Filtered | RANGE | 5 | 5 | 5 | 60,00% | 2,88 | 0,77R | €38,27 |
| Bilanciata 1H V3 Filtered | RANGE_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,83 |
| Bilanciata 1H V3 Filtered | TRANSITION | 0 | 8 | 8 | 37,50% | 1,11 | 0,07R | €5,68 |
| Bilanciata 1H V3 Filtered | TREND_UP | 1 | 20 | 20 | 45,00% | 1,54 | 0,31R | €61,36 |
| Bilanciata 1H V3 Filtered | TREND_UP_HIGH_VOL | 3 | 11 | 11 | 27,27% | 0,68 | -0,25R | €-27,79 |
| Rapida 1H V1 | ALT_ROTATION_DOWN | 4 | 13 | 13 | 23,08% | 0,40 | -0,49R | €-63,66 |
| Rapida 1H V1 | ALT_ROTATION_UP | 0 | 13 | 13 | 53,85% | 1,58 | 0,29R | €37,18 |
| Rapida 1H V1 | RANGE | 6 | 43 | 43 | 44,19% | 1,22 | 0,11R | €47,94 |
| Rapida 1H V1 | RANGE_HIGH_VOL | 0 | 11 | 11 | 0,00% | 0,00 | -1,09R | €-119,90 |
| Rapida 1H V1 | TRANSITION | 0 | 25 | 25 | 48,00% | 1,45 | 0,22R | €54,11 |
| Rapida 1H V1 | TREND_UP | 0 | 48 | 48 | 41,67% | 0,97 | -0,02R | €-9,20 |
| Rapida 1H V1 | TREND_UP_HIGH_VOL | 0 | 21 | 21 | 28,57% | 0,59 | -0,28R | €-58,55 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | ALT_ROTATION_DOWN | 2 | 2 | 2 | 0,00% | 0,00 | -1,02R | €-20,36 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,39R | €13,89 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 1,48R | €29,69 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TREND_UP | 0 | 3 | 3 | 33,33% | 0,68 | -0,23R | €-7,03 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | ALT_ROTATION_DOWN | 4 | 12 | 12 | 25,00% | 0,44 | -0,44R | €-52,20 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,39R | €13,89 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | RANGE | 6 | 7 | 7 | 71,43% | 3,52 | 0,73R | €51,32 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 1,48R | €29,69 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TREND_UP | 0 | 16 | 16 | 25,00% | 0,44 | -0,45R | €-72,21 |
| SHADOW_1H_FAST_NO_PEPE_V1 | ALT_ROTATION_DOWN | 4 | 12 | 12 | 25,00% | 0,44 | -0,44R | €-52,23 |
| SHADOW_1H_FAST_NO_PEPE_V1 | ALT_ROTATION_UP | 0 | 6 | 6 | 50,00% | 1,27 | 0,15R | €8,94 |
| SHADOW_1H_FAST_NO_PEPE_V1 | RANGE | 6 | 7 | 7 | 57,14% | 1,86 | 0,38R | €26,26 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 1,48R | €29,69 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_UP | 0 | 14 | 14 | 21,43% | 0,36 | -0,54R | €-74,90 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | ALT_ROTATION_DOWN | 3 | 7 | 7 | 42,86% | 1,00 | -0,00R | €-0,14 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | ALT_ROTATION_UP | 0 | 4 | 4 | 50,00% | 1,23 | 0,13R | €5,07 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | RANGE | 3 | 7 | 7 | 71,43% | 3,57 | 0,75R | €52,41 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_UP | 0 | 8 | 8 | 12,50% | 0,18 | -0,76R | €-61,17 |
| SHADOW_1H_FAST_TP2_V1 | ALT_ROTATION_DOWN | 5 | 11 | 11 | 18,18% | 0,40 | -0,51R | €-55,86 |
| SHADOW_1H_FAST_TP2_V1 | ALT_ROTATION_UP | 0 | 4 | 4 | 25,00% | 0,55 | -0,37R | €-14,93 |
| SHADOW_1H_FAST_TP2_V1 | RANGE | 7 | 6 | 6 | 50,00% | 1,90 | 0,46R | €27,62 |
| SHADOW_1H_FAST_TP2_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,98R | €19,82 |
| SHADOW_1H_FAST_TP2_V1 | TREND_UP | 0 | 14 | 14 | 21,43% | 0,49 | -0,43R | €-60,45 |
| Rapida 1H V2 | ALT_ROTATION_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,10R | €-21,92 |
| Rapida 1H V2 | RANGE | 2 | 3 | 2 | 66,67% | 2,37 | 0,52R | €15,71 |
| Rapida 1H V2 | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -1,14R | €-11,43 |
| Rapida 1H V3 Filtered | ALT_ROTATION_DOWN | 4 | 12 | 12 | 25,00% | 0,44 | -0,44R | €-52,22 |
| Rapida 1H V3 Filtered | ALT_ROTATION_UP | 0 | 5 | 5 | 60,00% | 1,92 | 0,41R | €20,43 |
| Rapida 1H V3 Filtered | RANGE | 4 | 9 | 9 | 66,67% | 2,82 | 0,62R | €55,79 |
| Rapida 1H V3 Filtered | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| Rapida 1H V3 Filtered | TRANSITION | 0 | 6 | 6 | 50,00% | 1,37 | 0,20R | €12,10 |
| Rapida 1H V3 Filtered | TREND_UP | 0 | 29 | 29 | 48,28% | 1,27 | 0,15R | €43,00 |
| Rapida 1H V3 Filtered | TREND_UP_HIGH_VOL | 0 | 20 | 20 | 25,00% | 0,49 | -0,36R | €-72,31 |
| SHADOW_1H_FAST_V3_CAP75_V1 | ALT_ROTATION_DOWN | 4 | 10 | 10 | 30,00% | 0,58 | -0,31R | €-30,62 |
| SHADOW_1H_FAST_V3_CAP75_V1 | ALT_ROTATION_UP | 0 | 4 | 4 | 50,00% | 1,23 | 0,13R | €5,07 |
| SHADOW_1H_FAST_V3_CAP75_V1 | RANGE | 4 | 7 | 7 | 71,43% | 3,57 | 0,75R | €52,41 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_UP | 0 | 11 | 11 | 18,18% | 0,29 | -0,62R | €-68,73 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | ALT_ROTATION_DOWN | 1 | 4 | 4 | 0,00% | 0,00 | -1,05R | €-41,91 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,39R | €13,89 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | RANGE | 0 | 6 | 6 | 66,67% | 2,90 | 0,65R | €38,84 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TREND_UP | 0 | 7 | 7 | 14,29% | 0,20 | -0,75R | €-52,65 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | ALT_ROTATION_DOWN | 1 | 4 | 4 | 0,00% | 0,00 | -1,05R | €-41,91 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,39R | €13,89 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | RANGE | 0 | 6 | 6 | 66,67% | 2,90 | 0,65R | €38,84 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TREND_UP | 0 | 7 | 7 | 14,29% | 0,20 | -0,75R | €-52,65 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 1 | 5 | 5 | 0,00% | 0,00 | -1,04R | €-52,08 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | ALT_ROTATION_UP | 0 | 4 | 4 | 50,00% | 1,23 | 0,13R | €5,07 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | RANGE | 0 | 7 | 7 | 57,14% | 1,94 | 0,41R | €28,65 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_UP | 0 | 6 | 6 | 0,00% | 0,00 | -1,11R | €-66,36 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | ALT_ROTATION_DOWN | 4 | 11 | 11 | 27,27% | 0,51 | -0,37R | €-40,79 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | ALT_ROTATION_UP | 0 | 2 | 2 | 50,00% | 1,27 | 0,15R | €3,00 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | RANGE | 4 | 9 | 9 | 66,67% | 2,82 | 0,62R | €55,79 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TREND_UP | 0 | 14 | 14 | 21,43% | 0,35 | -0,55R | €-77,05 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | ALT_ROTATION_DOWN | 4 | 11 | 11 | 27,27% | 0,51 | -0,37R | €-40,79 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | ALT_ROTATION_UP | 0 | 5 | 5 | 40,00% | 0,83 | -0,12R | €-5,83 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | RANGE | 4 | 9 | 9 | 66,67% | 2,82 | 0,62R | €55,79 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_UP | 0 | 12 | 12 | 16,67% | 0,26 | -0,66R | €-79,74 |
| SHADOW_4H_WIDE | ALT_ROTATION_DOWN | 4 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_4H_WIDE | ALT_ROTATION_UP | 2 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_4H_WIDE | RANGE | 4 | 16 | 16 | 25,00% | 0,90 | -0,07R | €-11,95 |
| SHADOW_4H_WIDE | TRANSITION | 3 | 7 | 7 | 14,29% | 0,46 | -0,47R | €-33,10 |
| SHADOW_4H_WIDE | TREND_UP | 3 | 13 | 13 | 46,15% | 2,32 | 0,73R | €95,17 |
| SHADOW_4H_WIDE | TREND_UP_HIGH_VOL | 4 | 4 | 4 | 0,00% | 0,00 | -1,01R | €-40,53 |
| SHADOW_BOLLINGER_MR_1H | ALT_ROTATION_DOWN | 1 | 4 | 4 | 50,00% | 1,30 | 0,17R | €6,66 |
| SHADOW_BOLLINGER_MR_1H | ALT_ROTATION_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,02R | €-20,30 |
| SHADOW_BOLLINGER_MR_1H | RANGE | 2 | 10 | 10 | 40,00% | 0,88 | -0,08R | €-7,56 |
| SHADOW_BOLLINGER_MR_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_BOLLINGER_MR_1H | TRANSITION | 0 | 3 | 3 | 33,33% | 0,71 | -0,20R | €-6,14 |
| SHADOW_BOLLINGER_MR_1H | TREND_UP | 0 | 12 | 12 | 50,00% | 1,28 | 0,15R | €18,32 |
| SHADOW_BOLLINGER_MR_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,31 | 0,17R | €3,31 |
| SHADOW_BTC_ADAPTIVE_1H | RANGE | 1 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_BTC_ADAPTIVE_1H | TREND_UP_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_ADAPTIVE_4H | TREND_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_BOLLINGER_1H | RANGE | 0 | 1 | 1 | 100,00% | ∞ | 1,37R | €13,67 |
| SHADOW_BTC_BOLLINGER_1H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,37R | €13,67 |
| SHADOW_BTC_BOLLINGER_4H | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_DONCHIAN_1H | RANGE | 1 | 1 | 1 | 0,00% | 0,00 | -1,12R | €-11,25 |
| SHADOW_BTC_DONCHIAN_1H | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -1,12R | €-11,25 |
| SHADOW_BTC_DONCHIAN_1H | TREND_UP_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_DONCHIAN_4H | TREND_UP_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_EMA_1H | RANGE | 1 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_BTC_EMA_1H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_BTC_EMA_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,70 | 0,39R | €7,78 |
| SHADOW_BTC_EMA_4H | TREND_UP_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_ADAPTIVE | ALT_ROTATION_DOWN | 6 | 6 | 6 | 33,33% | 0,91 | -0,06R | €-3,68 |
| SHADOW_COMBO_ADAPTIVE | ALT_ROTATION_UP | 0 | 6 | 6 | 50,00% | 1,86 | 0,45R | €26,75 |
| SHADOW_COMBO_ADAPTIVE | RANGE | 6 | 19 | 19 | 36,84% | 1,07 | 0,05R | €8,58 |
| SHADOW_COMBO_ADAPTIVE | RANGE_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,83 |
| SHADOW_COMBO_ADAPTIVE | TRANSITION | 1 | 18 | 18 | 44,44% | 1,48 | 0,28R | €50,23 |
| SHADOW_COMBO_ADAPTIVE | TREND_UP | 2 | 29 | 29 | 44,83% | 1,52 | 0,30R | €87,02 |
| SHADOW_COMBO_ADAPTIVE | TREND_UP_HIGH_VOL | 3 | 9 | 9 | 22,22% | 0,52 | -0,39R | €-35,52 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 2 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,28 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | ALT_ROTATION_UP | 0 | 4 | 4 | 75,00% | 5,34 | 1,17R | €46,86 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | RANGE | 0 | 5 | 5 | 40,00% | 1,30 | 0,19R | €9,27 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_UP | 2 | 6 | 6 | 0,00% | 0,00 | -1,09R | €-65,26 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_UP_HIGH_VOL | 0 | 6 | 6 | 16,67% | 0,36 | -0,56R | €-33,65 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | ALT_ROTATION_DOWN | 6 | 6 | 6 | 33,33% | 0,91 | -0,06R | €-3,68 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | ALT_ROTATION_UP | 0 | 7 | 7 | 42,86% | 1,37 | 0,22R | €15,64 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE | 6 | 7 | 7 | 57,14% | 2,54 | 0,67R | €47,05 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,83 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TRANSITION | 0 | 3 | 3 | 33,33% | 0,87 | -0,09R | €-2,74 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_UP | 2 | 21 | 21 | 42,86% | 1,42 | 0,25R | €52,12 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_UP_HIGH_VOL | 3 | 11 | 11 | 18,18% | 0,40 | -0,52R | €-57,58 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | ALT_ROTATION_DOWN | 6 | 6 | 6 | 33,33% | 0,91 | -0,06R | €-3,68 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | ALT_ROTATION_UP | 0 | 4 | 4 | 75,00% | 5,34 | 1,17R | €46,86 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | RANGE | 6 | 7 | 7 | 57,14% | 2,54 | 0,67R | €47,05 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TRANSITION | 0 | 2 | 2 | 0,00% | 0,00 | -1,09R | €-21,86 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_UP | 2 | 8 | 8 | 0,00% | 0,00 | -1,07R | €-85,56 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_UP_HIGH_VOL | 0 | 7 | 7 | 14,29% | 0,30 | -0,64R | €-44,76 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TRANSITION | 1 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,86 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TREND_UP | 1 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,18 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TRANSITION | 1 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,86 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TREND_UP | 1 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,18 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | ALT_ROTATION_DOWN | 2 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,84 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | RANGE | 1 | 3 | 3 | 33,33% | 0,98 | -0,02R | €-0,50 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TRANSITION | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,18 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TRANSITION | 1 | 3 | 3 | 0,00% | 0,00 | -1,09R | €-32,68 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TREND_UP | 2 | 13 | 13 | 15,38% | 0,33 | -0,60R | €-78,20 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TREND_UP_HIGH_VOL | 0 | 8 | 8 | 12,50% | 0,26 | -0,70R | €-55,87 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_DOWN | 5 | 3 | 3 | 33,33% | 1,35 | 0,25R | €7,43 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_UP | 0 | 5 | 5 | 40,00% | 1,80 | 0,52R | €26,25 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | RANGE | 8 | 4 | 4 | 25,00% | 0,95 | -0,04R | €-1,57 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | TRANSITION | 0 | 2 | 2 | 0,00% | 0,00 | -1,09R | €-21,86 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | TREND_UP | 2 | 7 | 7 | 0,00% | 0,00 | -1,06R | €-74,11 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 0,00% | 0,00 | -1,06R | €-42,49 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | ALT_ROTATION_DOWN | 5 | 3 | 3 | 33,33% | 1,35 | 0,25R | €7,43 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | ALT_ROTATION_UP | 0 | 5 | 5 | 40,00% | 1,80 | 0,52R | €26,25 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | RANGE | 8 | 4 | 4 | 25,00% | 0,95 | -0,04R | €-1,57 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | TRANSITION | 0 | 2 | 2 | 0,00% | 0,00 | -1,09R | €-21,86 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | TREND_UP | 2 | 7 | 7 | 0,00% | 0,00 | -1,06R | €-74,11 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 0,00% | 0,00 | -1,06R | €-42,49 |
| SHADOW_COMBO_MEAN_REVERSION | ALT_ROTATION_DOWN | 0 | 3 | 3 | 33,33% | 0,73 | -0,19R | €-5,83 |
| SHADOW_COMBO_MEAN_REVERSION | RANGE | 2 | 6 | 6 | 50,00% | 1,39 | 0,21R | €12,69 |
| SHADOW_COMBO_MEAN_REVERSION | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,94 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_UP | 0 | 3 | 3 | 33,33% | 0,75 | -0,17R | €-5,09 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,85 |
| SHADOW_COMBO_SCANNER | ALT_ROTATION_DOWN | 2 | 3 | 3 | 0,00% | 0,00 | -1,05R | €-31,40 |
| SHADOW_COMBO_SCANNER | ALT_ROTATION_UP | 0 | 4 | 4 | 50,00% | 2,09 | 0,57R | €22,81 |
| SHADOW_COMBO_SCANNER | RANGE | 1 | 8 | 8 | 50,00% | 2,09 | 0,56R | €44,63 |
| SHADOW_COMBO_SCANNER | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,69 |
| SHADOW_COMBO_SCANNER | TRANSITION | 0 | 14 | 14 | 42,86% | 1,34 | 0,21R | €28,81 |
| SHADOW_COMBO_SCANNER | TREND_UP | 2 | 20 | 20 | 50,00% | 2,04 | 0,55R | €110,63 |
| SHADOW_COMBO_SCANNER | TREND_UP_HIGH_VOL | 1 | 8 | 8 | 37,50% | 1,20 | 0,14R | €10,84 |
| SHADOW_COMBO_TREND | ALT_ROTATION_DOWN | 6 | 3 | 3 | 33,33% | 1,00 | -0,00R | €-0,08 |
| SHADOW_COMBO_TREND | ALT_ROTATION_UP | 0 | 5 | 5 | 40,00% | 1,39 | 0,24R | €12,22 |
| SHADOW_COMBO_TREND | RANGE | 4 | 15 | 15 | 33,33% | 1,03 | 0,02R | €2,81 |
| SHADOW_COMBO_TREND | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,63 |
| SHADOW_COMBO_TREND | TRANSITION | 1 | 14 | 14 | 42,86% | 1,55 | 0,33R | €46,22 |
| SHADOW_COMBO_TREND | TREND_UP | 2 | 23 | 23 | 34,78% | 1,10 | 0,07R | €15,44 |
| SHADOW_COMBO_TREND | TREND_UP_HIGH_VOL | 3 | 8 | 8 | 25,00% | 0,68 | -0,25R | €-20,22 |
| SHADOW_DOGE_BOLLINGER_1H | RANGE | 1 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,33 |
| SHADOW_DOGE_DONCHIAN_1H | RANGE | 1 | 2 | 2 | 50,00% | 1,67 | 0,38R | €7,50 |
| SHADOW_DOGE_EMA_1H | RANGE | 1 | 3 | 3 | 66,67% | 3,40 | 0,89R | €26,67 |
| SHADOW_DONCHIAN_1H | ALT_ROTATION_DOWN | 5 | 3 | 3 | 33,33% | 1,14 | 0,10R | €2,92 |
| SHADOW_DONCHIAN_1H | ALT_ROTATION_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,85 |
| SHADOW_DONCHIAN_1H | RANGE | 3 | 12 | 12 | 25,00% | 0,76 | -0,19R | €-22,61 |
| SHADOW_DONCHIAN_1H | RANGE_HIGH_VOL | 1 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_DONCHIAN_1H | TRANSITION | 1 | 6 | 6 | 16,67% | 0,45 | -0,48R | €-28,95 |
| SHADOW_DONCHIAN_1H | TREND_UP | 0 | 11 | 11 | 45,45% | 1,89 | 0,53R | €57,82 |
| SHADOW_DONCHIAN_1H | TREND_UP_HIGH_VOL | 2 | 4 | 4 | 50,00% | 2,23 | 0,67R | €26,65 |
| SHADOW_EMA_TREND_1H | ALT_ROTATION_DOWN | 5 | 4 | 4 | 25,00% | 0,67 | -0,27R | €-10,63 |
| SHADOW_EMA_TREND_1H | ALT_ROTATION_UP | 0 | 5 | 5 | 20,00% | 0,52 | -0,40R | €-20,11 |
| SHADOW_EMA_TREND_1H | RANGE | 5 | 16 | 16 | 31,25% | 1,03 | 0,02R | €3,11 |
| SHADOW_EMA_TREND_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,63 |
| SHADOW_EMA_TREND_1H | TRANSITION | 2 | 14 | 14 | 42,86% | 1,55 | 0,33R | €46,21 |
| SHADOW_EMA_TREND_1H | TREND_UP | 2 | 28 | 28 | 32,14% | 1,02 | 0,02R | €4,61 |
| SHADOW_EMA_TREND_1H | TREND_UP_HIGH_VOL | 3 | 8 | 8 | 37,50% | 1,23 | 0,15R | €12,10 |
| SHADOW_ETH_ADAPTIVE_1H | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_ETH_ADAPTIVE_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_ETH_ADAPTIVE_1H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,89R | €18,89 |
| SHADOW_ETH_ADAPTIVE_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_ETH_BOLLINGER_1H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,33 |
| SHADOW_ETH_DONCHIAN_1H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_ETH_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,68 | 0,38R | €7,64 |
| SHADOW_ETH_EMA_1H | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_ETH_EMA_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_ETH_EMA_1H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,89R | €18,89 |
| SHADOW_ETH_EMA_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,10R | €-10,99 |
| SHADOW_ETH_EMA_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,57 |
| SHADOW_GLOBAL_PURE | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,10R | €-11,00 |
| SHADOW_GLOBAL_PURE | RANGE | 1 | 1 | 1 | 100,00% | ∞ | 2,40R | €24,00 |
| SHADOW_GLOBAL_PURE | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,42R | €14,17 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | ALT_ROTATION_DOWN | 4 | 3 | 3 | 0,00% | 0,00 | -1,05R | €-31,40 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,79 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | RANGE | 0 | 4 | 4 | 25,00% | 0,65 | -0,26R | €-10,60 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 1,94R | €38,87 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TREND_UP | 2 | 8 | 8 | 12,50% | 0,26 | -0,70R | €-55,77 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | ALT_ROTATION_DOWN | 4 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,28 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,86 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | RANGE | 0 | 5 | 5 | 40,00% | 1,30 | 0,19R | €9,27 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TREND_UP | 2 | 10 | 10 | 10,00% | 0,21 | -0,77R | €-77,01 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | ALT_ROTATION_DOWN | 4 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,28 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | RANGE | 0 | 5 | 5 | 40,00% | 1,30 | 0,19R | €9,27 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TREND_UP | 2 | 11 | 11 | 9,09% | 0,18 | -0,80R | €-87,73 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_DOWN | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,86 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | RANGE | 2 | 3 | 3 | 0,00% | 0,00 | -1,01R | €-30,44 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | TREND_UP | 2 | 10 | 10 | 10,00% | 0,31 | -0,67R | €-67,01 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | ALT_ROTATION_DOWN | 1 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,28 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | RANGE | 0 | 6 | 6 | 50,00% | 1,96 | 0,49R | €29,12 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TREND_UP | 1 | 10 | 10 | 0,00% | 0,00 | -1,07R | €-107,43 |
| SHADOW_MASTER_ADAPTIVE_V1 | ALT_ROTATION_DOWN | 4 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,28 |
| SHADOW_MASTER_ADAPTIVE_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,86 |
| SHADOW_MASTER_ADAPTIVE_V1 | RANGE | 0 | 5 | 5 | 40,00% | 1,30 | 0,19R | €9,27 |
| SHADOW_MASTER_ADAPTIVE_V1 | TREND_UP | 2 | 10 | 10 | 10,00% | 0,21 | -0,77R | €-77,01 |
| Forza relativa 1H V1 | ALT_ROTATION_DOWN | 6 | 4 | 4 | 0,00% | 0,00 | -1,05R | €-42,19 |
| Forza relativa 1H V1 | ALT_ROTATION_UP | 0 | 13 | 13 | 30,77% | 0,90 | -0,07R | €-9,26 |
| Forza relativa 1H V1 | RANGE | 5 | 25 | 25 | 24,00% | 0,69 | -0,24R | €-58,81 |
| Forza relativa 1H V1 | RANGE_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -1,03R | €-31,02 |
| Forza relativa 1H V1 | TRANSITION | 0 | 15 | 15 | 46,67% | 1,84 | 0,46R | €69,26 |
| Forza relativa 1H V1 | TREND_UP | 2 | 36 | 36 | 38,89% | 1,54 | 0,30R | €106,45 |
| Forza relativa 1H V1 | TREND_UP_HIGH_VOL | 1 | 8 | 8 | 12,50% | 0,30 | -0,64R | €-51,15 |
| Forza relativa 1H V2 | ALT_ROTATION_DOWN | 5 | 2 | 2 | 50,00% | 2,08 | 0,55R | €10,99 |
| Forza relativa 1H V2 | ALT_ROTATION_UP | 0 | 4 | 4 | 50,00% | 2,00 | 0,54R | €21,41 |
| Forza relativa 1H V2 | RANGE | 0 | 6 | 6 | 66,67% | 4,31 | 1,12R | €67,19 |
| Forza relativa 1H V2 | TRANSITION | 2 | 9 | 8 | 33,33% | 1,05 | 0,03R | €3,12 |
| Forza relativa 1H V2 | TREND_UP | 0 | 11 | 10 | 45,45% | 1,77 | 0,43R | €47,60 |
| Forza relativa 1H V2 | TREND_UP_HIGH_VOL | 0 | 4 | 3 | 0,00% | 0,00 | -1,04R | €-41,60 |
| SHADOW_SCANNER_BOTTOM5_SHORT | ALT_ROTATION_DOWN | 1 | 4 | 4 | 75,00% | 5,32 | 1,17R | €46,61 |
| SHADOW_SCANNER_BOTTOM5_SHORT | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| SHADOW_SCANNER_BOTTOM5_SHORT | RANGE | 7 | 9 | 9 | 22,22% | 0,50 | -0,42R | €-37,98 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TRANSITION | 0 | 14 | 14 | 28,57% | 0,85 | -0,09R | €-13,14 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP | 0 | 7 | 7 | 0,00% | 0,00 | -0,73R | €-51,04 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP_HIGH_VOL | 1 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,24 |
| SHADOW_SCANNER_TOP5_BTC | ALT_ROTATION_DOWN | 2 | 3 | 3 | 0,00% | 0,00 | -1,05R | €-31,40 |
| SHADOW_SCANNER_TOP5_BTC | ALT_ROTATION_UP | 0 | 5 | 5 | 40,00% | 1,39 | 0,25R | €12,28 |
| SHADOW_SCANNER_TOP5_BTC | RANGE | 0 | 9 | 9 | 44,44% | 2,08 | 0,50R | €44,64 |
| SHADOW_SCANNER_TOP5_BTC | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,69 |
| SHADOW_SCANNER_TOP5_BTC | TRANSITION | 0 | 12 | 12 | 41,67% | 1,49 | 0,30R | €36,18 |
| SHADOW_SCANNER_TOP5_BTC | TREND_UP | 2 | 19 | 19 | 47,37% | 1,85 | 0,47R | €89,92 |
| SHADOW_SCANNER_TOP5_BTC | TREND_UP_HIGH_VOL | 1 | 8 | 8 | 37,50% | 1,20 | 0,14R | €10,84 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | ALT_ROTATION_DOWN | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,86 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 2,19R | €21,87 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TREND_UP | 1 | 2 | 2 | 50,00% | 1,97 | 0,54R | €10,76 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TREND_UP_HIGH_VOL | 0 | 6 | 6 | 16,67% | 0,40 | -0,53R | €-31,93 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | ALT_ROTATION_DOWN | 3 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,28 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,86 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | RANGE | 0 | 4 | 4 | 25,00% | 0,72 | -0,21R | €-8,60 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 2,19R | €21,87 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_UP | 1 | 2 | 2 | 50,00% | 1,97 | 0,54R | €10,76 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_UP_HIGH_VOL | 0 | 6 | 6 | 16,67% | 0,40 | -0,53R | €-31,93 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | ALT_ROTATION_DOWN | 3 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,28 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,79 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | RANGE | 0 | 4 | 4 | 25,00% | 0,72 | -0,21R | €-8,60 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 2,19R | €21,87 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 2,19R | €21,87 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | ALT_ROTATION_DOWN | 3 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,28 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,79 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | RANGE | 0 | 4 | 4 | 25,00% | 0,72 | -0,21R | €-8,60 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 2,19R | €21,87 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 2,19R | €21,87 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | ALT_ROTATION_DOWN | 2 | 3 | 3 | 0,00% | 0,00 | -1,05R | €-31,40 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,79 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | RANGE | 0 | 4 | 4 | 25,00% | 0,72 | -0,21R | €-8,60 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 2,19R | €21,87 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_UP | 1 | 3 | 3 | 33,33% | 1,02 | 0,01R | €0,39 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | ALT_ROTATION_DOWN | 2 | 3 | 3 | 0,00% | 0,00 | -1,05R | €-31,40 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,79 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | RANGE | 0 | 4 | 4 | 25,00% | 0,72 | -0,21R | €-8,60 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 2,19R | €21,87 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_UP | 1 | 3 | 3 | 33,33% | 1,02 | 0,01R | €0,39 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | ALT_ROTATION_DOWN | 2 | 3 | 3 | 0,00% | 0,00 | -1,05R | €-31,40 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,79 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | RANGE | 0 | 4 | 4 | 25,00% | 0,72 | -0,21R | €-8,60 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 2,19R | €21,87 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_UP | 2 | 2 | 2 | 50,00% | 1,97 | 0,54R | €10,76 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_UP_HIGH_VOL | 1 | 8 | 8 | 25,00% | 0,66 | -0,27R | €-21,76 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | ALT_ROTATION_UP | 0 | 4 | 4 | 25,00% | 0,89 | -0,09R | €-3,61 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | RANGE | 1 | 3 | 3 | 0,00% | 0,00 | -1,02R | €-30,46 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 2,99R | €29,87 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_UP | 3 | 3 | 3 | 0,00% | 0,00 | -1,09R | €-32,57 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -1,05R | €-31,38 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | ALT_ROTATION_UP | 0 | 4 | 4 | 25,00% | 0,89 | -0,09R | €-3,61 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | RANGE | 1 | 3 | 3 | 0,00% | 0,00 | -1,02R | €-30,46 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 2,99R | €29,87 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_UP | 3 | 3 | 3 | 0,00% | 0,00 | -1,09R | €-32,57 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -1,05R | €-31,38 |
| SHADOW_SCANNER_TOP5_LONG | ALT_ROTATION_DOWN | 2 | 4 | 4 | 0,00% | 0,00 | -1,06R | €-42,51 |
| SHADOW_SCANNER_TOP5_LONG | ALT_ROTATION_UP | 0 | 6 | 6 | 33,33% | 0,92 | -0,06R | €-3,32 |
| SHADOW_SCANNER_TOP5_LONG | RANGE | 0 | 10 | 10 | 50,00% | 2,36 | 0,57R | €56,51 |
| SHADOW_SCANNER_TOP5_LONG | RANGE_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,83 |
| SHADOW_SCANNER_TOP5_LONG | TRANSITION | 0 | 12 | 12 | 41,67% | 1,36 | 0,22R | €26,18 |
| SHADOW_SCANNER_TOP5_LONG | TREND_UP | 2 | 28 | 28 | 50,00% | 1,84 | 0,45R | €125,56 |
| SHADOW_SCANNER_TOP5_LONG | TREND_UP_HIGH_VOL | 1 | 8 | 8 | 37,50% | 1,08 | 0,05R | €4,35 |
| SHADOW_SOL_ADAPTIVE_1H | RANGE | 2 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_SOL_ADAPTIVE_1H | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,89R | €18,89 |
| SHADOW_SOL_ADAPTIVE_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,10R | €-10,96 |
| SHADOW_SOL_ADAPTIVE_4H | RANGE | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SOL_ADAPTIVE_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,05R | €-10,52 |
| SHADOW_SOL_BOLLINGER_1H | RANGE | 1 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,33 |
| SHADOW_SOL_BOLLINGER_4H | TREND_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SOL_DONCHIAN_1H | RANGE | 1 | 1 | 1 | 0,00% | 0,00 | -1,12R | €-11,25 |
| SHADOW_SOL_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,08 |
| SHADOW_SOL_DONCHIAN_4H | RANGE | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SOL_DONCHIAN_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,56 |
| SHADOW_SOL_EMA_1H | RANGE | 1 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_SOL_EMA_1H | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,89R | €18,89 |
| SHADOW_SOL_EMA_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,10R | €-10,96 |
| SHADOW_SOL_EMA_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,56 |

Il P&L è normalizzato a **€10 di rischio per evento**, così leva e size non falsano il confronto.
La matrice diventerà utilizzabile per una rotazione automatica soltanto dopo un campione sufficiente per ciascuna coppia strategia-regime.

# Block 3 — Shadow Exit Engine

Generato: 2026-07-24T04:38:42+00:00

> Motore esclusivamente osservativo e Paper-only. Non modifica le uscite reali. I confronti escludono il funding sia dall'uscita originale sia dalle varianti.

## Stato operativo

- Gruppi di trade ancora monitorati: **355**
- Scenari virtuali ancora attivi: **3088**
- Gruppi in attesa dell'uscita originale: **171**
- Gruppi con originale chiuso ma Shadow ancora attive: **184**
- Confronti completati: **15058**

## Classifica osservativa complessiva

| Scenario | Campione completo | Campione totale | Δ medio vs originale | Migliora | Troppo presto | Troppo tardi | Stato dati |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| GB20_R050 | 721 | 784 | +€6,25 | 49,6% | 200 | 1 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R050 | 721 | 784 | +€4,14 | 48,3% | 205 | 8 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R050 | 721 | 784 | +€1,88 | 46,9% | 211 | 13 | READY_FOR_BLOCK4_EVALUATION |
| TP_R050 | 721 | 784 | +€0,94 | 47,1% | 223 | 0 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R050 | 718 | 781 | +€0,59 | 45,2% | 206 | 27 | READY_FOR_BLOCK4_EVALUATION |
| TIME_6H | 716 | 779 | €-0,64 | 50,6% | 165 | 105 | READY_FOR_BLOCK4_EVALUATION |
| GB20_R100 | 707 | 770 | +€5,03 | 42,5% | 169 | 22 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R100 | 707 | 770 | +€3,09 | 42,3% | 158 | 34 | READY_FOR_BLOCK4_EVALUATION |
| TP_R100 | 707 | 770 | +€2,91 | 40,5% | 184 | 22 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R100 | 707 | 770 | +€1,94 | 41,9% | 135 | 58 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R100 | 704 | 767 | +€1,62 | 38,6% | 99 | 115 | READY_FOR_BLOCK4_EVALUATION |
| ATR15_R100 | 703 | 766 | €-1,49 | 33,4% | 61 | 171 | READY_FOR_BLOCK4_EVALUATION |
| TIME_12H | 691 | 754 | +€0,80 | 44,7% | 84 | 160 | READY_FOR_BLOCK4_EVALUATION |
| TP_R150 | 678 | 741 | +€1,61 | 30,9% | 78 | 84 | READY_FOR_BLOCK4_EVALUATION |
| ATR20_R100 | 678 | 741 | €-4,32 | 29,7% | 44 | 196 | READY_FOR_BLOCK4_EVALUATION |
| BE_R050 | 656 | 719 | €-10,45 | 27,8% | 125 | 128 | READY_FOR_BLOCK4_EVALUATION |
| ATR30_R100 | 653 | 716 | €-9,26 | 25,6% | 40 | 198 | READY_FOR_BLOCK4_EVALUATION |
| TP_R200 | 646 | 709 | +€0,44 | 36,1% | 36 | 125 | READY_FOR_BLOCK4_EVALUATION |
| TIME_24H | 638 | 701 | €-5,45 | 32,8% | 46 | 194 | READY_FOR_BLOCK4_EVALUATION |
| BE_R100 | 605 | 668 | €-16,63 | 20,1% | 39 | 196 | READY_FOR_BLOCK4_EVALUATION |

## Come leggere il controllo

- **EARLIER_BETTER**: la variante è uscita prima e ha conservato più profitto.
- **TOO_EARLY**: la variante è uscita prima ma ha tagliato un movimento migliore.
- **LATER_BETTER**: la variante ha continuato dopo l'uscita originale e ha guadagnato di più.
- **TOO_LATE**: la variante è rimasta aperta più a lungo e ha peggiorato il risultato.

## Limiti e protezioni

Le regole Shadow mantengono entrata, quantità, commissioni, stop protettivo iniziale e liquidazione. Le ambiguità all'interno della stessa candela vengono risolte scegliendo l'esito peggiore. Le posizioni già aperte al momento dell'installazione sono marcate come campione parziale e non saranno utilizzate dal futuro Blocco 4 come prova piena.

# Blocco 4 — Valutazione statistica Shadow

Generato: 2026-07-24T04:38:43+00:00

> Modulo esclusivamente valutativo. Non modifica strategie, uscite, posizioni o capitale. Le candidature vengono consegnate al futuro Blocco 5, senza applicazione automatica.

## Stato

- Risultati Block 3 disponibili: **15058**
- Valutazioni prodotte: **4331**
- Candidature al Blocco 5: **0**
- Mutazioni create automaticamente: **0**

## Classifica complessiva

| Scenario | Campione pieno | Δ medio (R) | Mediana (R) | CI bootstrap basso | Migliora | Score | Stato |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| GB20_R050 | 94 | 0,434 | 0,374 | 0,287 | 87,2% | 97,1 | VALIDATING |
| GB30_R050 | 94 | 0,383 | 0,301 | 0,246 | 87,2% | 97,0 | VALIDATING |
| GB20_R100 | 92 | 0,468 | 0,412 | 0,335 | 85,9% | 96,9 | VALIDATING |
| TP_R100 | 92 | 0,430 | 0,408 | 0,296 | 84,8% | 96,8 | VALIDATING |
| GB40_R100 | 92 | 0,375 | 0,369 | 0,245 | 84,8% | 96,8 | VALIDATING |
| GB30_R100 | 92 | 0,436 | 0,372 | 0,315 | 89,1% | 96,6 | VALIDATING |
| GB50_R100 | 92 | 0,324 | 0,408 | 0,214 | 82,6% | 96,5 | VALIDATING |
| GB40_R050 | 94 | 0,324 | 0,287 | 0,187 | 84,0% | 93,5 | VALIDATING |
| GB50_R050 | 94 | 0,330 | 0,287 | 0,211 | 83,0% | 93,3 | VALIDATING |
| TP_R050 | 94 | 0,247 | 0,290 | 0,105 | 84,0% | 91,3 | VALIDATING |
| BE_R050 | 85 | 0,091 | 0,129 | -0,043 | 61,2% | 77,3 | VALIDATING |
| TIME_6H | 86 | 0,048 | 0,159 | -0,098 | 66,3% | 76,4 | VALIDATING |
| TIME_24H | 6 | 0,997 | 1,104 | 0,180 | 66,7% | 74,1 | INSUFFICIENT_DATA |
| GB20_R050 | 621 | 0,102 | 0,000 | 0,038 | 45,1% | 70,0 | VALIDATING |
| TP_R200 | 67 | 0,037 | 0,217 | -0,111 | 73,1% | 69,8 | VALIDATING |
| GB20_R100 | 609 | 0,061 | 0,000 | 0,013 | 36,5% | 69,7 | VALIDATING |
| TP_R150 | 599 | 0,058 | 0,000 | 0,009 | 27,4% | 69,7 | VALIDATING |
| GB30_R050 | 621 | 0,061 | 0,000 | -0,003 | 43,5% | 69,5 | VALIDATING |
| ATR15_R100 | 92 | 0,020 | 0,104 | -0,098 | 64,1% | 64,3 | VALIDATING |
| ATR30_R100 | 85 | 0,018 | 0,104 | -0,092 | 60,0% | 63,4 | VALIDATING |

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

Generato: 2026-07-24T04:38:52+00:00

Questi profili sono osservativi e Paper-only. Usano gli stessi trade della madre, ma applicano una specifica uscita Block 3 soltanto ai segnali aperti dopo la loro registrazione.
Nessuna promozione, modifica live o operazione reale viene eseguita automaticamente.

| Challenger | Madre | Scenario | Chiusi | Copertura | PF | PnL | Exp/trade | DD | Stato |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Rapida 1H V1 — giveback 20% dopo +0,5R | SHADOW_1H_FAST | GB20_R050 | 8 | 100,00% | 1,66 | +€104,96 | +€13,12 | 1,08% | COLLECTING |
| Rapida 1H V1 — giveback 30% dopo +0,5R | SHADOW_1H_FAST | GB30_R050 | 8 | 100,00% | 1,44 | +€70,02 | +€8,75 | 1,08% | COLLECTING |
| Relative Strength — giveback 20% dopo +0,5R | SHADOW_RELATIVE_STRENGTH | GB20_R050 | 2 | 100,00% | 0,39 | €-32,83 | €-16,42 | 0,54% | COLLECTING |
| Relative Strength — giveback 30% dopo +0,5R | SHADOW_RELATIVE_STRENGTH | GB30_R050 | 2 | 100,00% | 0,34 | €-35,84 | €-17,92 | 0,54% | COLLECTING |

## Regole di valutazione

- Prima fotografia a 30 trade indipendenti.
- Revisione per possibile promozione a 50 trade indipendenti.
- PF minimo 1,50, expectancy e PnL positivi, drawdown massimo 15%, copertura minima 90%.
- PF deve superare la madre e il drawdown non deve essere peggiore sulla stessa serie di trade.
- La promozione resta una decisione umana protetta; il rollback viene predisposto soltanto in fase di approvazione.

# Blocco 4.5 — Crash Cascade Guard

Generato: 2026-07-24T04:38:35+00:00

> Paper-only. In mercato NORMAL/WATCH non riduce i segnali. Le limitazioni iniziano soltanto in STRESS, RECOVERY, CRASH, EXTREME o con dati non affidabili.

## Stato corrente

- Livello: **NORMAL**
- Direzione: **NONE**
- Segnali bloccati nel ciclo: **0**
- Simulazioni bloccate attive: **32**
- Simulazioni completate nel ciclo: **0**
- Liquidazioni virtuali evitate totali: **0**
- Valore cumulato del filtro: **-19.32 R**
- Profitto virtuale mancato: **52.70 R**

## Stress test portafogli Paper

| Scenario | Posizioni interessate | Liquidazioni stimate | Perdita stimata EUR |
| --- | ---: | ---: | ---: |
| DOWN_10 | 108 | 0 | 13437.08 |
| DOWN_20 | 108 | 0 | 26874.15 |
| DOWN_30 | 108 | 13 | 40497.50 |
| DOWN_40 | 108 | 29 | 50911.34 |
| UP_10 | 63 | 0 | 17951.64 |
| UP_20 | 63 | 0 | 35903.27 |
| UP_30 | 63 | 0 | 53854.91 |
| UP_40 | 63 | 35 | 63986.16 |

## Modello di esecuzione

Se una candela di cascata attraversa nello stesso intervallo sia lo stop sia il prezzo di liquidazione, il Paper usa il caso peggiore e registra una liquidazione intrabar. Gli stop in gap o in regime di stress ricevono slippage aggiuntivo.

## Requisiti prima del live futures

- modalità ISOLATED obbligatoria;
- stop nativo sull'exchange;
- conferma dello stop prima di accettare la posizione;
- cross margin vietato.

# Blocco 5 — Candidati evolutivi controllati

Generato: 2026-07-24T04:38:12+00:00

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

Generato: 2026-07-24T04:38:52+00:00

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

Generato: 2026-07-24T04:38:52+00:00

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

Generato: 2026-07-24T04:38:52+00:00

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

Generato: 2026-07-24T04:38:52+00:00

> Paper-only. La memoria può bloccare soltanto una futura proposta Block 5 classificata AVOID; non modifica strategie esistenti.

## Stato

- Strategie/portafogli valutati: **84**
- Hall of Fame: **6**
- Memorie genetiche: **0**
- Firme bloccate: **0**
- Azioni automatiche e live: **0**

## Hall of Fame

| Rank | Strategia | Stato | Score | Grade | Trade | PF | Expectancy R | DD R |
| ---: | --- | --- | ---: | --- | ---: | ---: | ---: | ---: |
| 1 | SHADOW_SCANNER_TOP5_LONG | BASELINE | 20.2 | E | 30 | 2.21 | 0.412 | 5.75 |
| 2 | SHADOW_1H_BALANCED | BASELINE | 15.5 | E | 37 | 1.48 | 0.184 | 4.17 |
| 3 | SHADOW_1H_BALANCED_V3 | BASELINE | 13.2 | E | 31 | 1.32 | 0.163 | 3.23 |
| 4 | SHADOW_1H_FAST_V3 | BASELINE | 11.9 | E | 55 | 1.17 | 0.062 | 5.36 |
| 5 | SHADOW_RELATIVE_STRENGTH_V2 | BASELINE | 11.9 | E | 30 | 1.35 | 0.188 | 6.62 |
| 6 | SHADOW_1H_FAST | BASELINE | 7.6 | E | 63 | 0.96 | -0.018 | 13.48 |

## Memoria genetica

| Scope | Famiglia | Mutazione | Target | Stato | Score | Prove | Coppie | Blocco |
| --- | --- | --- | --- | --- | ---: | ---: | ---: | --- |
| — | — | Nessuna candidata ancora creata | — | INSUFFICIENT | 0 | 0 | 0 | NO |

## Sicurezza

- Nessuna strategia, posizione o promozione esistente viene modificata.
- Nessuna mutazione, promozione, pensionamento o rollback automatico.
- Nessun effetto live e nessun ordine reale.

# Blocco 10 — Regime Fitness e specializzazione

Generato: 2026-07-24T04:38:52+00:00

> Paper-only e advisory. Il blocco misura quali strategie funzionano nei diversi regimi, ma non cambia automaticamente strategia o posizione.

## Stato

- Regime corrente: **RANGE**
- Righe di performance: **308**
- Strategie preferite nel regime corrente: **1**
- Strategie da evitare nel regime corrente: **0**
- Memorie contestuali: **154**
- Routing automatico: **NO**

## Classifica del regime corrente

| Rank | Portafoglio | Famiglia | Stato | Fitness | Trade | PF | Expectancy R | DD R |
| ---: | --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| 1 | SHADOW_DOGE_DONCHIAN_1H | shadow-doge-donchian-1h | INSUFFICIENT | 80.8 | 2 | 99.00 | 0.548 | 0.00 |
| 2 | SHADOW_BTC_BOLLINGER_1H | shadow-btc-bollinger-1h | INSUFFICIENT | 80.8 | 2 | 99.00 | 0.997 | 0.00 |
| 3 | SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | shadow-scanner-top5-btc-guard-btc-le3-v1 | INSUFFICIENT | 80.8 | 2 | 99.00 | 1.186 | 0.00 |
| 4 | SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | shadow-scanner-top5-btc-btc-le3-v1 | INSUFFICIENT | 80.3 | 1 | 99.00 | 0.398 | 0.00 |
| 5 | SHADOW_COMBO_ADAPTIVE | shadow-combo-adaptive | OBSERVING | 79.1 | 19 | 2.19 | 0.339 | 1.10 |
| 6 | SHADOW_DOGE_EMA_1H | shadow-doge-ema-1h | INSUFFICIENT | 77.8 | 5 | 4.56 | 0.781 | 1.10 |
| 7 | SHADOW_ETH_BOLLINGER_1H | shadow-eth-bollinger-1h | INSUFFICIENT | 76.6 | 1 | 99.00 | 0.309 | 0.00 |
| 8 | SHADOW_SCANNER_TOP5_LONG | shadow-scanner-top5-long | OBSERVING | 74.4 | 22 | 1.96 | 0.371 | 4.17 |
| 9 | SHADOW_SCANNER_TOP5_BTC | shadow-scanner-top5-btc | OBSERVING | 71.2 | 18 | 1.93 | 0.332 | 3.09 |
| 10 | SHADOW_SCANNER_TOP5_BTC_TP3_V1 | shadow-scanner-top5-btc-tp3-v1 | INSUFFICIENT | 70.3 | 5 | 1.93 | 0.400 | 2.15 |

## Sicurezza

- Il regime viene assegnato usando solo l'ultimo record noto prima dell'entrata del trade.
- Nessun uso di dati futuri per classificare il trade.
- Il Candidate Regime Gate è advisory per impostazione predefinita.
- Nessun cambio automatico di MASTER, posizione o live.

# Blocco 11 — Collegamento protetto al live

Generato: 2026-07-24T04:38:53+00:00

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

Generato: 2026-07-24T04:38:35+00:00

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
