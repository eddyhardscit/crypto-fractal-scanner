# Paper trading automatico KuCoin

Generato: 2026-07-21T20:08:45+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-07-21T20:08:25+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-07-21T20:08:25+00:00 | 2026-07-21T20:08:25+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-07-21T19:45:00+00:00 | 2026-07-21T19:45:00+00:00 | 8,5 min | 25,0 min | OK |
| 60m | 12 | 2026-07-21T19:00:00+00:00 | 2026-07-21T19:00:00+00:00 | 8,5 min | 45,0 min | OK |
| 240m | 12 | 2026-07-21T16:00:00+00:00 | 2026-07-21T16:00:00+00:00 | 8,5 min | 1,00 h | OK |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | ONDO | 240m | LONG | 8,16 | 6,00 | 0,00 | RISK_GATE | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro rischio/esecuzione: numero massimo posizioni. |
| Principale 4H | AKE | 240m | LONG | 7,75 | 6,00 | 0,00 | RISK_GATE | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro rischio/esecuzione: numero massimo posizioni. |
| Principale 4H | HYPE | 240m | SHORT | -7,00 | 6,00 | 0,00 | RISK_GATE | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro rischio/esecuzione: numero massimo posizioni. |
| Principale 4H | XRP | 240m | LONG | 6,62 | 6,00 | 0,00 | RISK_GATE | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro rischio/esecuzione: numero massimo posizioni. |
| Principale 4H | PEPE | 240m | LONG | 6,38 | 6,00 | 0,00 | RISK_GATE | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro rischio/esecuzione: numero massimo posizioni. |
| Principale 4H | ETH | 240m | LONG | 6,21 | 6,00 | 0,00 | RISK_GATE | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro rischio/esecuzione: numero massimo posizioni. |
| Principale 4H | ADA | 240m | LONG | 5,89 | 6,00 | 0,11 | BELOW_SCORE | 8,5 min | D: n/a | W: n/a | peso 0 | Punteggio +5.89; soglia ±6.00; mancano 0.11 punti. |
| Principale 4H | SOL | 240m | LONG | 4,88 | 6,00 | 1,12 | BELOW_SCORE | 8,5 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Punteggio +4.88; soglia ±6.00; mancano 1.12 punti. |
| Principale 4H | BTC | 240m | LONG | 4,75 | 6,00 | 1,25 | BELOW_SCORE | 8,5 min | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Punteggio +4.75; soglia ±6.00; mancano 1.25 punti. |
| Bilanciata 1H V3 Filtered | ONDO | 60m | LONG | 6,25 | 6,00 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V1 — score 6–7,5 | ONDO | 60m | LONG | 6,25 | 6,00 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V3 — Long Only | ONDO | 60m | LONG | 6,25 | 4,50 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V3 — Long + no HIGH + score <7,5 | ONDO | 60m | LONG | 6,25 | 4,50 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V3 — qualità completa + profit lock | ONDO | 60m | LONG | 6,25 | 4,50 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Bilanciata 1H V2 | ONDO | 60m | LONG | 6,25 | 5,50 | 0,00 | STRATEGY_FILTER | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro V2 non superato: regime, EMA, ritorni e RSI; per Rapida V2 servono anche breakout reale, volume e ADX. |
| Rapida 1H V2 | ONDO | 60m | LONG | 6,25 | 5,00 | 0,00 | STRATEGY_FILTER | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro V2 non superato: regime, EMA, ritorni e RSI; per Rapida V2 servono anche breakout reale, volume e ADX. |
| Rapida 1H V1 — madre | BANK | 60m | SHORT | -5,48 | 4,50 | 0,00 | STRATEGY_FILTER | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout DOWN oppure movimento breve ≥1,5%; breakout=NONE, movimento=+1.02%. |
| Rapida V1 — no HIGH + score <7,5 | BANK | 60m | SHORT | -5,48 | 4,50 | 0,00 | STRATEGY_FILTER | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout DOWN oppure movimento breve ≥1,5%; breakout=NONE, movimento=+1.02%. |
| Rapida V1 — senza PEPE | BANK | 60m | SHORT | -5,48 | 4,50 | 0,00 | STRATEGY_FILTER | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout DOWN oppure movimento breve ≥1,5%; breakout=NONE, movimento=+1.02%. |
| Rapida V1 — target pieno 2R | BANK | 60m | SHORT | -5,48 | 4,50 | 0,00 | STRATEGY_FILTER | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout DOWN oppure movimento breve ≥1,5%; breakout=NONE, movimento=+1.02%. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.846,25 | -1,54% | €-153,75 | €3.000,00 | -5,12% | 4 | 16 | 31,25% | 0,81 | 4,26% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 16 | 278 | CAMPIONE INSUFFICIENTE | 30 (mancano 14) |

- Trade del Principale 4H chiusi: **16**; win rate **31,25%**; profit factor **0,81**.
- Expectancy: **€-6,29** per trade; P&L netto: **€-100,68**; max drawdown: **4,26%**.
- Valutazione: **Servono altri eventi indipendenti prima di trarre conclusioni.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 4 | €9.846,25 | €1.552,19 | €4.656,58 | €197,65 | €-52,15 |
| TEST | Scanner Top 5 Long 1H | 3 | €10.579,58 | €3.774,91 | €7.549,81 | €157,90 | €-43,03 |
| TEST | Scanner Top 5 + forza BTC 1H | 3 | €10.530,42 | €4.103,28 | €8.206,56 | €104,33 | €115,34 |
| TEST | Combo Adaptive — madre | 3 | €10.324,33 | €2.939,66 | €5.879,32 | €154,36 | €-16,95 |
| TEST | Bilanciata 1H V3 Filtered | 4 | €10.298,06 | €2.442,27 | €7.326,82 | €154,18 | €11,85 |
| TEST | Bilanciata 1H V1 | 4 | €10.258,26 | €2.717,14 | €8.151,42 | €153,08 | €90,50 |
| TEST | Benchmark Donchian breakout 1H | 3 | €10.218,61 | €3.858,22 | €7.716,44 | €101,96 | €66,02 |
| TEST | Combo Mean Reversion | 0 | €10.195,13 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Benchmark Bollinger mean reversion 1H | 3 | €10.170,68 | €5.014,38 | €10.028,76 | €51,04 | €24,33 |
| TEST | Forza relativa 1H V2 | 4 | €10.156,28 | €2.419,26 | €4.838,52 | €151,48 | €-4,77 |
| TEST | Combo Trend | 3 | €10.123,32 | €1.639,93 | €3.279,86 | €100,58 | €67,96 |
| TEST | Top 5 + BTC — 75% a 2,2R + runner 3R | 3 | €10.104,07 | €3.110,27 | €6.220,54 | €151,22 | €-37,88 |
| TEST | Top 5 + BTC — target pieno 3R | 3 | €10.104,07 | €3.110,27 | €6.220,54 | €151,22 | €-37,88 |
| TEST | Btc Bollinger 1H | 1 | €10.087,77 | €1.398,43 | €4.195,29 | €50,34 | €21,60 |
| TEST | Forza relativa 1H V1 | 4 | €10.076,93 | €3.216,05 | €6.432,10 | €150,91 | €-10,40 |
| TEST | Ampia 4H | 4 | €10.076,74 | €2.235,83 | €4.471,66 | €201,27 | €-10,29 |
| TEST | Rapida V3 — Long Only | 3 | €10.048,79 | €3.694,31 | €11.082,93 | €100,60 | €-4,06 |
| TEST | Top 5 + BTC — BTC≤3 | 2 | €10.045,56 | €2.798,33 | €5.596,65 | €99,98 | €-9,37 |
| TEST | Top 5 + BTC — BTC 2–3 | 2 | €10.045,56 | €2.798,33 | €5.596,65 | €99,98 | €-9,37 |
| TEST | Combo Scanner | 2 | €10.033,92 | €1.577,94 | €3.155,88 | €50,08 | €74,47 |
| TEST | Btc Ema 4H | 1 | €10.033,77 | €1.105,63 | €2.211,26 | €50,00 | €33,31 |
| TEST | Btc Donchian 4H | 1 | €10.033,77 | €1.105,63 | €2.211,26 | €50,00 | €33,31 |
| TEST | Top 5 + BTC — solo MFE | 3 | €10.025,98 | €4.328,60 | €8.657,19 | €100,30 | €-1,81 |
| TEST | Rapida 1H V3 Filtered — madre | 4 | €10.024,53 | €4.064,80 | €12.194,41 | €149,17 | €39,18 |
| TEST | Eth Bollinger 1H | 0 | €10.015,45 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 4H | 1 | €10.013,35 | €968,56 | €1.937,11 | €50,00 | €14,50 |
| TEST | Btc Adaptive 4H | 1 | €10.006,53 | €1.047,40 | €2.094,81 | €50,00 | €7,09 |
| TEST | Btc Bollinger 4H | 1 | €10.006,03 | €1.313,84 | €2.627,69 | €50,00 | €7,60 |
| TEST | Rapida V1 — score 6–7,5 | 4 | €10.004,63 | €4.835,85 | €14.507,56 | €149,91 | €14,80 |
| TEST | Rapida 1H V2 | 0 | €10.004,31 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 1H | 1 | €10.000,79 | €1.001,44 | €3.004,32 | €49,95 | €11,91 |
| TEST | Rapida V1 — Long + BTC 1–3 + score <7,5 | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €10 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €10 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €50 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €50 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · prudente · 5x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · prudente · 5x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €10 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €10 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €50 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €50 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · prudente · 5x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · prudente · 5x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Bollinger 1H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €10 · 15x | 1 | €9.999,92 | €10,00 | €150,00 | €2,01 | €0,01 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 1 | €9.999,60 | €149,55 | €747,73 | €10,00 | €0,05 |
| TEST | Scalp RSI Long 25 · €50 · 15x | 1 | €9.999,60 | €50,00 | €750,00 | €10,03 | €0,05 |
| TEST | Sol Donchian 1H | 0 | €9.997,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 0 | €9.995,13 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 1H | 1 | €9.991,49 | €1.000,51 | €3.001,52 | €49,91 | €11,90 |
| TEST | Rapida V1 — senza PEPE | 4 | €9.989,93 | €4.276,51 | €12.829,53 | €148,58 | €-9,62 |
| TEST | Btc Adaptive 1H | 0 | €9.988,26 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Ema 4H | 1 | €9.987,78 | €883,93 | €1.767,86 | €50,00 | €-10,99 |
| TEST | Sol Adaptive 4H | 1 | €9.986,30 | €807,13 | €1.614,26 | €50,00 | €-12,72 |
| TEST | Rapida V1 — target pieno 2R | 4 | €9.985,85 | €4.321,77 | €12.965,31 | €198,68 | €-63,41 |
| TEST | Sol Ema 4H | 1 | €9.985,05 | €880,51 | €1.761,01 | €50,00 | €-13,88 |
| TEST | Sol Donchian 4H | 1 | €9.985,05 | €880,51 | €1.761,01 | €50,00 | €-13,88 |
| TEST | Eth Donchian 1H | 0 | €9.982,54 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 — score <7,5 | 4 | €9.977,58 | €4.274,99 | €12.824,96 | €149,34 | €-13,26 |
| TEST | Rapida V3 — senza ESPORTS | 4 | €9.977,58 | €4.274,99 | €12.824,96 | €149,34 | €-13,26 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €9.975,63 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 1H | 1 | €9.971,94 | €1.155,97 | €3.467,90 | €49,94 | €-13,53 |
| TEST | Doge Donchian 1H | 0 | €9.968,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.968,09 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — Quality7 | 2 | €9.967,06 | €1.848,71 | €3.697,42 | €99,83 | €-30,51 |
| TEST | Combo Adaptive — Quality7 + Regime | 2 | €9.967,06 | €1.848,71 | €3.697,42 | €99,83 | €-30,51 |
| TEST | Combo Adaptive — Quality7 + Regime + parziale 1R | 2 | €9.967,06 | €1.848,71 | €3.697,42 | €99,83 | €-30,51 |
| TEST | Eth Adaptive 1H | 0 | €9.962,36 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 — Long + no HIGH + score <7,5 | 2 | €9.960,89 | €2.181,13 | €6.543,40 | €49,82 | €6,65 |
| TEST | Rapida V3 — qualità completa + profit lock | 2 | €9.960,89 | €2.181,13 | €6.543,40 | €99,80 | €6,65 |
| TEST | Combo Adaptive — 75% a 2R + runner 3R | 2 | €9.950,89 | €2.755,02 | €5.510,05 | €99,63 | €-23,28 |
| TEST | Combo Adaptive — target pieno 3R | 2 | €9.950,89 | €2.755,02 | €5.510,05 | €99,63 | €-23,28 |
| TEST | Bilanciata 1H V2 | 3 | €9.950,43 | €848,57 | €2.545,72 | €99,11 | €0,00 |
| TEST | Doge Ema 1H | 0 | €9.948,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 1H | 0 | €9.944,21 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — Long Only | 2 | €9.937,66 | €2.802,01 | €5.604,02 | €100,01 | €-33,57 |
| TEST | Btc Donchian 1H | 0 | €9.937,58 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Strict3 V1 | 3 | €9.907,81 | €4.527,63 | €9.055,25 | €149,65 | €-31,39 |
| TEST | Rapida V3 — no volatilità HIGH | 4 | €9.907,73 | €3.649,55 | €10.948,66 | €148,37 | €15,80 |
| TEST | Rapida 1H V1 — madre | 4 | €9.905,54 | €3.808,21 | €11.424,64 | €145,91 | €1,90 |
| TEST | Benchmark trend following EMA 1H | 2 | €9.899,44 | €2.600,35 | €5.200,71 | €99,35 | €-21,04 |
| TEST | Eth Ema 1H | 0 | €9.889,74 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive V1 | 3 | €9.882,18 | €3.957,47 | €7.914,95 | €149,58 | €-57,71 |
| TEST | Master Adaptive No Alt V1 | 3 | €9.882,18 | €3.957,47 | €7.914,95 | €149,58 | €-57,71 |
| TEST | Master Adaptive Expanded V1 | 3 | €9.882,18 | €3.957,47 | €7.914,95 | €149,58 | €-57,71 |
| TEST | Master Adaptive Runner25 V1 | 3 | €9.882,18 | €3.957,47 | €7.914,95 | €149,58 | €-57,71 |
| TEST | Top 5 + BTC — Guard + BTC≤3 | 0 | €9.881,42 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Top 5 + BTC — Guard + BTC≤3 + MFE | 0 | €9.881,42 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — Trend/Transition | 3 | €9.874,54 | €3.175,32 | €6.350,65 | €148,29 | €9,72 |
| TEST | Combo Adaptive — parziale 1R | 2 | €9.858,32 | €2.774,59 | €5.549,18 | €99,07 | €-33,26 |
| TEST | Rapida V1 — no HIGH + score <7,5 | 4 | €9.852,28 | €3.618,15 | €10.854,45 | €147,01 | €7,40 |
| TEST | Top 5 + BTC — Guard | 3 | €9.833,79 | €3.518,03 | €7.036,06 | €147,68 | €11,02 |
| TEST | Top 5 + BTC — Guard + MFE | 3 | €9.833,79 | €3.518,03 | €7.036,06 | €98,52 | €11,02 |
| TEST | Master Adaptive Gb20 V1 | 3 | €9.833,34 | €3.556,46 | €7.112,92 | €148,64 | €-49,18 |
| TEST | Scanner Bottom 5 Short 1H | 3 | €9.790,16 | €2.006,41 | €4.012,83 | €48,85 | €68,29 |
| TEST | Global Confluence puro 1H | 0 | €9.773,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — MFE Trail esistente | 3 | €9.654,81 | €2.625,04 | €5.250,09 | €96,67 | €11,48 |

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
| PRINCIPALE | Principale 4H | Confluenza trend | €9.846,25 | €-100,68 | 16 | 16 | 31,25% | 0,81 | €-6,29 | 4,26% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.579,58 | €627,36 | 26 | 26 | 53,85% | 2,50 | €24,13 | 2,70% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €10.530,42 | €420,03 | 18 | 18 | 50,00% | 2,49 | €23,33 | 1,62% |
| TEST | Combo Adaptive — madre | Combo Adaptive | €10.324,33 | €345,41 | 17 | 17 | 47,06% | 2,52 | €20,32 | 1,27% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €10.298,06 | €290,85 | 26 | 26 | 46,15% | 1,45 | €11,19 | 2,20% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €10.258,26 | €172,46 | 23 | 23 | 47,83% | 1,44 | €7,50 | 1,81% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €10.218,61 | €157,42 | 15 | 15 | 46,67% | 1,46 | €10,49 | 1,98% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €10.195,13 | €195,13 | 7 | 7 | 57,14% | 2,81 | €27,88 | 0,59% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €10.170,68 | €152,11 | 15 | 15 | 46,67% | 1,66 | €10,14 | 2,06% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €10.156,28 | €164,02 | 18 | 18 | 33,33% | 1,33 | €9,11 | 2,41% |
| TEST | Combo Trend | Combo Trend | €10.123,32 | €57,96 | 15 | 15 | 33,33% | 1,15 | €3,86 | 2,19% |
| TEST | Top 5 + BTC — 75% a 2,2R + runner 3R | Scanner Top 5 + forza BTC | €10.104,07 | €146,10 | 3 | 3 | 100,00% | ∞ | €48,70 | 0,79% |
| TEST | Top 5 + BTC — target pieno 3R | Scanner Top 5 + forza BTC | €10.104,07 | €146,10 | 3 | 3 | 100,00% | ∞ | €48,70 | 0,79% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.087,77 | €68,69 | 1 | 1 | 100,00% | ∞ | €68,69 | 0,31% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €10.076,93 | €91,78 | 18 | 18 | 33,33% | 1,35 | €5,10 | 2,29% |
| TEST | Ampia 4H | Confluenza trend | €10.076,74 | €88,72 | 12 | 12 | 25,00% | 1,27 | €7,39 | 2,13% |
| TEST | Rapida V3 — Long Only | Momentum / breakout V3 Filtered | €10.048,79 | €59,51 | 3 | 3 | 33,33% | 7,81 | €19,84 | 0,84% |
| TEST | Top 5 + BTC — BTC≤3 | Scanner Top 5 + forza BTC | €10.045,56 | €58,86 | 1 | 1 | 100,00% | ∞ | €58,86 | 1,22% |
| TEST | Top 5 + BTC — BTC 2–3 | Scanner Top 5 + forza BTC | €10.045,56 | €58,86 | 1 | 1 | 100,00% | ∞ | €58,86 | 1,22% |
| TEST | Combo Scanner | Combo Scanner | €10.033,92 | €-37,94 | 18 | 18 | 38,89% | 0,92 | €-2,11 | 2,18% |
| TEST | Btc Ema 4H | Trend following EMA | €10.033,77 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,20% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €10.033,77 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,20% |
| TEST | Top 5 + BTC — solo MFE | Scanner Top 5 + forza BTC | €10.025,98 | €33,20 | 2 | 2 | 50,00% | 8,40 | €16,60 | 0,87% |
| TEST | Rapida 1H V3 Filtered — madre | Momentum / breakout V3 Filtered | €10.024,53 | €-7,33 | 41 | 41 | 36,59% | 0,99 | €-0,18 | 2,89% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €10.015,45 | €15,45 | 1 | 1 | 100,00% | ∞ | €15,45 | 0,51% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €10.013,35 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,12% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €10.006,53 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,19% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.006,03 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,10% |
| TEST | Rapida V1 — score 6–7,5 | Momentum / breakout | €10.004,63 | €-1,46 | 6 | 6 | 33,33% | 0,99 | €-0,24 | 1,80% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €10.004,31 | €4,31 | 3 | 2 | 33,33% | 1,07 | €1,44 | 0,93% |
| TEST | Sol Ema 1H | Trend following EMA | €10.000,79 | €-9,16 | 2 | 2 | 50,00% | 0,83 | €-4,58 | 0,98% |
| TEST | Rapida V1 — Long + BTC 1–3 + score <7,5 | Momentum / breakout | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 15 · €10 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 20 · €10 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 20 · €50 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 20 · prudente · 5x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 85 · €10 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 80 · €10 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 85 · €50 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 80 · €50 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 85 · prudente · 5x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 80 · prudente · 5x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 25 · €10 · 15x | Inversione RSI estrema 15m | €9.999,92 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €9.999,60 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,01% |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | €9.999,60 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,01% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €9.997,37 | €-2,63 | 2 | 2 | 50,00% | 0,41 | €-1,31 | 0,55% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €9.995,13 | €-4,87 | 5 | 5 | 20,00% | 0,16 | €-0,97 | 0,05% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €9.991,49 | €-18,45 | 2 | 2 | 50,00% | 0,67 | €-9,23 | 0,99% |
| TEST | Rapida V1 — senza PEPE | Momentum / breakout | €9.989,93 | €7,25 | 6 | 6 | 33,33% | 1,06 | €1,21 | 2,00% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €9.988,26 | €-11,74 | 2 | 2 | 50,00% | 0,78 | €-5,87 | 0,89% |
| TEST | Eth Ema 4H | Trend following EMA | €9.987,78 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,25% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €9.986,30 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,18% |
| TEST | Rapida V1 — target pieno 2R | Momentum / breakout | €9.985,85 | €57,04 | 6 | 6 | 33,33% | 1,44 | €9,51 | 2,01% |
| TEST | Sol Ema 4H | Trend following EMA | €9.985,05 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,20% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €9.985,05 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,20% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.982,54 | €-17,46 | 3 | 3 | 33,33% | 0,84 | €-5,82 | 1,38% |
| TEST | Rapida V3 — score <7,5 | Momentum / breakout V3 Filtered | €9.977,58 | €-1,46 | 6 | 6 | 33,33% | 0,99 | €-0,24 | 2,11% |
| TEST | Rapida V3 — senza ESPORTS | Momentum / breakout V3 Filtered | €9.977,58 | €-1,46 | 6 | 6 | 33,33% | 0,99 | €-0,24 | 2,11% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €9.975,63 | €-24,37 | 5 | 5 | 20,00% | 0,16 | €-4,87 | 0,24% |
| TEST | Btc Ema 1H | Trend following EMA | €9.971,94 | €-12,46 | 3 | 3 | 33,33% | 0,89 | €-4,15 | 1,56% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €9.968,98 | €-31,02 | 2 | 2 | 50,00% | 0,46 | €-15,51 | 0,93% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.968,09 | €-31,91 | 5 | 5 | 20,00% | 0,19 | €-6,38 | 0,32% |
| TEST | Combo Adaptive — Quality7 | Combo Adaptive | €9.967,06 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,54% |
| TEST | Combo Adaptive — Quality7 + Regime | Combo Adaptive | €9.967,06 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,54% |
| TEST | Combo Adaptive — Quality7 + Regime + parziale 1R | Combo Adaptive | €9.967,06 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,54% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.962,36 | €-37,64 | 3 | 3 | 66,67% | 0,31 | €-12,55 | 1,02% |
| TEST | Rapida V3 — Long + no HIGH + score <7,5 | Momentum / breakout V3 Filtered | €9.960,89 | €-41,84 | 3 | 3 | 33,33% | 0,62 | €-13,95 | 1,03% |
| TEST | Rapida V3 — qualità completa + profit lock | Momentum / breakout V3 Filtered | €9.960,89 | €-41,84 | 3 | 3 | 33,33% | 0,62 | €-13,95 | 1,03% |
| TEST | Combo Adaptive — 75% a 2R + runner 3R | Combo Adaptive | €9.950,89 | €-22,11 | 4 | 4 | 50,00% | 0,79 | €-5,53 | 1,41% |
| TEST | Combo Adaptive — target pieno 3R | Combo Adaptive | €9.950,89 | €-22,11 | 4 | 4 | 50,00% | 0,79 | €-5,53 | 1,41% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €9.950,43 | €-48,22 | 17 | 15 | 47,06% | 0,89 | €-2,84 | 2,75% |
| TEST | Doge Ema 1H | Trend following EMA | €9.948,28 | €-51,72 | 4 | 4 | 50,00% | 0,54 | €-12,93 | 1,27% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.944,21 | €-55,79 | 1 | 1 | 0,00% | 0,00 | €-55,79 | 0,62% |
| TEST | Combo Adaptive — Long Only | Combo Adaptive | €9.937,66 | €-25,20 | 3 | 3 | 33,33% | 0,79 | €-8,40 | 1,54% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €9.937,58 | €-62,42 | 3 | 3 | 33,33% | 0,43 | €-20,81 | 1,49% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €9.907,81 | €-54,91 | 1 | 1 | 0,00% | 0,00 | €-54,91 | 1,27% |
| TEST | Rapida V3 — no volatilità HIGH | Momentum / breakout V3 Filtered | €9.907,73 | €-101,49 | 6 | 6 | 33,33% | 0,57 | €-16,92 | 2,37% |
| TEST | Rapida 1H V1 — madre | Momentum / breakout | €9.905,54 | €-89,23 | 49 | 49 | 34,69% | 0,92 | €-1,82 | 5,79% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.899,44 | €-76,19 | 11 | 11 | 27,27% | 0,76 | €-6,93 | 2,25% |
| TEST | Eth Ema 1H | Trend following EMA | €9.889,74 | €-110,26 | 5 | 5 | 40,00% | 0,33 | €-22,05 | 1,59% |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | €9.882,18 | €-54,91 | 1 | 1 | 0,00% | 0,00 | €-54,91 | 1,78% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €9.882,18 | €-54,91 | 1 | 1 | 0,00% | 0,00 | €-54,91 | 1,78% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €9.882,18 | €-54,91 | 1 | 1 | 0,00% | 0,00 | €-54,91 | 1,78% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €9.882,18 | €-54,91 | 1 | 1 | 0,00% | 0,00 | €-54,91 | 1,78% |
| TEST | Top 5 + BTC — Guard + BTC≤3 | Scanner Top 5 + forza BTC | €9.881,42 | €-118,58 | 2 | 2 | 0,00% | 0,00 | €-59,29 | 1,19% |
| TEST | Top 5 + BTC — Guard + BTC≤3 + MFE | Scanner Top 5 + forza BTC | €9.881,42 | €-118,58 | 2 | 2 | 0,00% | 0,00 | €-59,29 | 1,19% |
| TEST | Combo Adaptive — Trend/Transition | Combo Adaptive | €9.874,54 | €-131,16 | 5 | 5 | 20,00% | 0,42 | €-26,23 | 1,86% |
| TEST | Combo Adaptive — parziale 1R | Combo Adaptive | €9.858,32 | €-104,88 | 6 | 6 | 33,33% | 0,54 | €-17,48 | 2,05% |
| TEST | Rapida V1 — no HIGH + score <7,5 | Momentum / breakout | €9.852,28 | €-148,61 | 7 | 7 | 28,57% | 0,48 | €-21,23 | 2,52% |
| TEST | Top 5 + BTC — Guard | Scanner Top 5 + forza BTC | €9.833,79 | €-172,80 | 3 | 3 | 0,00% | 0,00 | €-57,60 | 2,08% |
| TEST | Top 5 + BTC — Guard + MFE | Scanner Top 5 + forza BTC | €9.833,79 | €-172,80 | 3 | 3 | 0,00% | 0,00 | €-57,60 | 2,08% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €9.833,34 | €-113,00 | 4 | 4 | 25,00% | 0,08 | €-28,25 | 2,05% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.790,16 | €-275,74 | 14 | 14 | 21,43% | 0,33 | €-19,70 | 4,68% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.773,98 | €-226,02 | 7 | 7 | 28,57% | 0,17 | €-32,29 | 2,46% |
| TEST | Combo Adaptive — MFE Trail esistente | Combo Adaptive | €9.654,81 | €-353,52 | 24 | 24 | 25,00% | 0,32 | €-14,73 | 3,59% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | DOGE | SHORT | Confluenza trend | 240m | 3,0x | 0,07292 | 0,07351 | 0,07500 | 0,09686 | 0,06875 | €574,44 | €1.723,33 | €49,28 | €-14,05 |
| Principale 4H | LAB | SHORT | Confluenza trend | 240m | 3,0x | 0,17841 | 0,17841 | 0,19982 | 0,23699 | 0,13559 | €136,26 | €408,77 | €49,05 | €-0,00 |
| Principale 4H | ZEC | LONG | Confluenza trend | 240m | 3,0x | 556,07119 | 532,05000 | 524,63715 | 373,49448 | 618,93927 | €293,97 | €881,92 | €49,85 | €-38,10 |
| Principale 4H | SUI | LONG | Confluenza trend | 240m | 3,0x | 0,76296 | 0,76296 | 0,73998 | 0,51245 | 0,80891 | €547,52 | €1.642,56 | €49,46 | €0,00 |
| Bilanciata 1H V1 | LAB | SHORT | Confluenza trend | 60m | 3,0x | 0,18667 | 0,18667 | 0,20845 | 0,24796 | 0,14311 | €143,84 | €431,52 | €50,35 | €-0,00 |
| Bilanciata 1H V1 | ONDO | LONG | Confluenza trend | 60m | 3,0x | 0,37613 | 0,40110 | 0,39181 | 0,25263 | 0,40460 | €442,89 | €1.328,68 | €0,00 | €88,22 |
| Bilanciata 1H V1 | HYPE | SHORT | Confluenza trend | 60m | 3,0x | 60,62787 | 60,30400 | 61,73069 | 80,53402 | 58,42224 | €940,38 | €2.821,13 | €51,32 | €15,07 |
| Bilanciata 1H V1 | XRP | LONG | Confluenza trend | 60m | 3,0x | 1,15887 | 1,15472 | 1,14218 | 0,77838 | 1,19225 | €1.190,03 | €3.570,09 | €51,41 | €-12,79 |
| Bilanciata 1H V2 | LAB | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,18667 | 0,18667 | 0,20845 | 0,24796 | 0,14311 | €139,69 | €419,08 | €48,90 | €-0,00 |
| Bilanciata 1H V2 | GRAM | SHORT | Confluenza trend V2 | 60m | 3,0x | 1,49240 | 1,49240 | 1,53621 | 1,98241 | 1,40478 | €570,19 | €1.710,58 | €50,21 | €-0,00 |
| Bilanciata 1H V2 | ESPORTS | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,02164 | 0,02164 | 0,02164 | 0,02874 | 0,01644 | €138,69 | €416,06 | €0,00 | €-0,00 |
| Bilanciata 1H V3 Filtered | ESPORTS | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,02126 | 0,02126 | 0,02126 | 0,02823 | 0,01615 | €141,51 | €424,52 | €0,00 | €-0,00 |
| Bilanciata 1H V3 Filtered | ADA | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,17417 | 0,17401 | 0,17046 | 0,11699 | 0,18161 | €799,70 | €2.399,09 | €51,19 | €-2,27 |
| Bilanciata 1H V3 Filtered | HYPE | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 60,62787 | 60,30400 | 61,73069 | 80,53402 | 58,42224 | €943,48 | €2.830,45 | €51,49 | €15,12 |
| Bilanciata 1H V3 Filtered | ONDO | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,40134 | 0,40110 | 0,38898 | 0,26957 | 0,42605 | €557,59 | €1.672,77 | €51,50 | €-1,00 |
| Rapida 1H V1 — madre | ESPORTS | SHORT | Momentum / breakout | 60m | 3,0x | 0,01984 | 0,01984 | 0,02222 | 0,02635 | 0,01627 | €129,65 | €388,96 | €46,68 | €-0,00 |
| Rapida 1H V1 — madre | SUI | LONG | Momentum / breakout | 60m | 3,0x | 0,76416 | 0,76416 | 0,75422 | 0,51326 | 0,77907 | €1.284,19 | €3.852,58 | €50,12 | €0,00 |
| Rapida 1H V1 — madre | ADA | LONG | Momentum / breakout | 60m | 3,0x | 0,17438 | 0,17401 | 0,17128 | 0,11713 | 0,17904 | €919,27 | €2.757,80 | €49,11 | €-5,93 |
| Rapida 1H V1 — madre | XRP | LONG | Momentum / breakout | 60m | 3,0x | 1,15268 | 1,15472 | 1,15268 | 0,77422 | 1,17205 | €1.475,10 | €4.425,30 | €0,00 | €7,83 |
| Rapida V1 — score 6–7,5 | BTC | LONG | Momentum / breakout | 60m | 3,0x | 66554,96833 | 66395,81000 | 65809,55269 | 44702,75373 | 67673,09180 | €1.485,18 | €4.455,53 | €49,90 | €-10,65 |
| Rapida V1 — score 6–7,5 | XRP | LONG | Momentum / breakout | 60m | 3,0x | 1,15268 | 1,15472 | 1,15268 | 0,77422 | 1,17205 | €1.476,66 | €4.429,97 | €0,00 | €7,84 |
| Rapida V1 — score 6–7,5 | HYPE | SHORT | Momentum / breakout | 60m | 3,0x | 60,62787 | 60,30400 | 61,48562 | 80,53402 | 59,34125 | €1.177,50 | €3.532,51 | €49,98 | €18,87 |
| Rapida V1 — score 6–7,5 | ONDO | LONG | Momentum / breakout | 60m | 3,0x | 0,40134 | 0,40110 | 0,39173 | 0,26957 | 0,41576 | €696,51 | €2.089,54 | €50,04 | €-1,25 |
| Rapida V1 — no HIGH + score <7,5 | AKE | SHORT | Momentum / breakout | 60m | 3,0x | 0,00159 | 0,00170 | 0,00177 | 0,00211 | 0,00131 | €138,51 | €415,54 | €48,47 | €-28,58 |
| Rapida V1 — no HIGH + score <7,5 | XRP | LONG | Momentum / breakout | 60m | 3,0x | 1,15170 | 1,15472 | 1,15170 | 0,77356 | 1,17105 | €1.453,67 | €4.361,00 | €0,00 | €11,43 |
| Rapida V1 — no HIGH + score <7,5 | HYPE | SHORT | Momentum / breakout | 60m | 3,0x | 60,62787 | 60,30400 | 61,48562 | 80,53402 | 59,34125 | €1.159,88 | €3.479,64 | €49,23 | €18,59 |
| Rapida V1 — no HIGH + score <7,5 | ZEC | SHORT | Momentum / breakout | 60m | 3,0x | 533,27332 | 532,05000 | 543,39504 | 708,36473 | 518,09076 | €866,09 | €2.598,27 | €49,32 | €5,96 |
| Rapida V1 — senza PEPE | BTC | LONG | Momentum / breakout | 60m | 3,0x | 66554,96833 | 66395,81000 | 65809,55269 | 44702,75373 | 67673,09180 | €1.486,49 | €4.459,46 | €49,95 | €-10,66 |
| Rapida V1 — senza PEPE | AKE | SHORT | Momentum / breakout | 60m | 3,0x | 0,00160 | 0,00170 | 0,00179 | 0,00212 | 0,00131 | €135,40 | €406,19 | €48,74 | €-25,64 |
| Rapida V1 — senza PEPE | XRP | LONG | Momentum / breakout | 60m | 3,0x | 1,15268 | 1,15472 | 1,15268 | 0,77422 | 1,17205 | €1.479,06 | €4.437,17 | €0,00 | €7,85 |
| Rapida V1 — senza PEPE | HYPE | SHORT | Momentum / breakout | 60m | 3,0x | 60,62787 | 60,30400 | 61,48562 | 80,53402 | 59,34125 | €1.175,57 | €3.526,72 | €49,90 | €18,84 |
| Rapida V1 — target pieno 2R | BTC | LONG | Momentum / breakout | 60m | 3,0x | 66554,96833 | 66395,81000 | 65809,55269 | 44702,75373 | 68045,79962 | €1.486,49 | €4.459,46 | €49,95 | €-10,66 |
| Rapida V1 — target pieno 2R | AKE | SHORT | Momentum / breakout | 60m | 3,0x | 0,00160 | 0,00170 | 0,00179 | 0,00212 | 0,00121 | €135,40 | €406,19 | €48,74 | €-25,64 |
| Rapida V1 — target pieno 2R | XRP | LONG | Momentum / breakout | 60m | 3,0x | 1,16418 | 1,15472 | 1,15114 | 0,78194 | 1,19026 | €1.486,69 | €4.460,07 | €49,95 | €-36,25 |
| Rapida V1 — target pieno 2R | HYPE | SHORT | Momentum / breakout | 60m | 3,0x | 60,45591 | 60,30400 | 61,28705 | 80,30560 | 58,79362 | €1.213,20 | €3.639,60 | €50,04 | €9,15 |
| Rapida 1H V3 Filtered — madre | ESPORTS | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01977 | 0,01977 | 0,02214 | 0,02626 | 0,01621 | €137,70 | €413,09 | €49,57 | €-0,00 |
| Rapida 1H V3 Filtered — madre | SUI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,76416 | 0,76416 | 0,75422 | 0,51326 | 0,77907 | €1.267,97 | €3.803,92 | €49,49 | €0,00 |
| Rapida 1H V3 Filtered — madre | XRP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,14947 | 1,15472 | 1,15095 | 0,77206 | 1,16878 | €1.478,54 | €4.435,62 | €0,00 | €20,26 |
| Rapida 1H V3 Filtered — madre | HYPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 60,62787 | 60,30400 | 61,48562 | 80,53402 | 59,34125 | €1.180,59 | €3.541,78 | €50,11 | €18,92 |
| Rapida V3 — score <7,5 | BTC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 66554,96833 | 66395,81000 | 65809,55269 | 44702,75373 | 67673,09180 | €1.485,18 | €4.455,53 | €49,90 | €-10,65 |
| Rapida V3 — score <7,5 | AKE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00159 | 0,00170 | 0,00177 | 0,00211 | 0,00131 | €141,76 | €425,29 | €49,61 | €-29,25 |
| Rapida V3 — score <7,5 | XRP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,15268 | 1,15472 | 1,15268 | 0,77422 | 1,17205 | €1.473,93 | €4.421,78 | €0,00 | €7,82 |
| Rapida V3 — score <7,5 | HYPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 60,62787 | 60,30400 | 61,48562 | 80,53402 | 59,34125 | €1.174,12 | €3.522,36 | €49,83 | €18,82 |
| Rapida V3 — no volatilità HIGH | XRP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,14947 | 1,15472 | 1,15095 | 0,77206 | 1,16878 | €1.471,35 | €4.414,06 | €0,00 | €20,16 |
| Rapida V3 — no volatilità HIGH | AKE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00159 | 0,00170 | 0,00177 | 0,00211 | 0,00131 | €140,80 | €422,39 | €49,27 | €-29,05 |
| Rapida V3 — no volatilità HIGH | HYPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 60,62787 | 60,30400 | 61,48562 | 80,53402 | 59,34125 | €1.166,42 | €3.499,27 | €49,51 | €18,69 |
| Rapida V3 — no volatilità HIGH | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 533,27332 | 532,05000 | 543,39504 | 708,36473 | 518,09076 | €870,98 | €2.612,94 | €49,59 | €5,99 |
| Rapida V3 — Long Only | BTC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 66554,96833 | 66395,81000 | 65809,55269 | 44702,75373 | 67673,09180 | €1.498,33 | €4.495,00 | €50,34 | €-10,75 |
| Rapida V3 — Long Only | XRP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,15268 | 1,15472 | 1,15268 | 0,77422 | 1,17205 | €1.496,39 | €4.489,16 | €0,00 | €7,94 |
| Rapida V3 — Long Only | ONDO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,40134 | 0,40110 | 0,39173 | 0,26957 | 0,41576 | €699,59 | €2.098,77 | €50,26 | €-1,26 |
| Rapida V3 — Long + no HIGH + score <7,5 | XRP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,15268 | 1,15472 | 1,15268 | 0,77422 | 1,17205 | €1.487,67 | €4.463,00 | €0,00 | €7,90 |
| Rapida V3 — Long + no HIGH + score <7,5 | ONDO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,40134 | 0,40110 | 0,39173 | 0,26957 | 0,41576 | €693,47 | €2.080,41 | €49,82 | €-1,25 |
| Rapida V3 — senza ESPORTS | BTC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 66554,96833 | 66395,81000 | 65809,55269 | 44702,75373 | 67673,09180 | €1.485,18 | €4.455,53 | €49,90 | €-10,65 |
| Rapida V3 — senza ESPORTS | AKE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00159 | 0,00170 | 0,00177 | 0,00211 | 0,00131 | €141,76 | €425,29 | €49,61 | €-29,25 |
| Rapida V3 — senza ESPORTS | XRP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,15268 | 1,15472 | 1,15268 | 0,77422 | 1,17205 | €1.473,93 | €4.421,78 | €0,00 | €7,82 |
| Rapida V3 — senza ESPORTS | HYPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 60,62787 | 60,30400 | 61,48562 | 80,53402 | 59,34125 | €1.174,12 | €3.522,36 | €49,83 | €18,82 |
| Rapida V3 — qualità completa + profit lock | XRP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,15268 | 1,15472 | 1,13977 | 0,77422 | 1,17205 | €1.487,67 | €4.463,00 | €49,99 | €7,90 |
| Rapida V3 — qualità completa + profit lock | ONDO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,40134 | 0,40110 | 0,39173 | 0,26957 | 0,41576 | €693,47 | €2.080,41 | €49,82 | €-1,25 |
| Ampia 4H | DOGE | SHORT | Confluenza trend | 240m | 2,0x | 0,07237 | 0,07351 | 0,07515 | 0,10819 | 0,06457 | €649,49 | €1.298,97 | €50,00 | €-20,52 |
| Ampia 4H | ZEC | LONG | Confluenza trend | 240m | 2,0x | 522,36445 | 532,05000 | 483,09844 | 263,79405 | 632,30930 | €332,53 | €665,06 | €49,99 | €12,33 |
| Ampia 4H | PEPE | LONG | Confluenza trend | 240m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €497,18 | €994,35 | €50,70 | €7,31 |
| Ampia 4H | ETH | LONG | Confluenza trend | 240m | 2,0x | 1933,63665 | 1921,62000 | 1869,00475 | 976,48651 | 2114,60597 | €756,64 | €1.513,28 | €50,58 | €-9,40 |
| Forza relativa 1H V1 | ESPORTS | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,02126 | 0,02126 | 0,02126 | 0,03178 | 0,01564 | €208,05 | €416,10 | €0,00 | €-0,00 |
| Forza relativa 1H V1 | PEPE | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €986,47 | €1.972,93 | €50,47 | €-16,55 |
| Forza relativa 1H V1 | NIGHT | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,02031 | 0,02031 | 0,02210 | 0,03036 | 0,01637 | €285,91 | €571,83 | €50,45 | €-0,00 |
| Forza relativa 1H V1 | XRP | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 1,15268 | 1,15472 | 1,13608 | 0,58210 | 1,18920 | €1.735,62 | €3.471,23 | €49,99 | €6,14 |
| Forza relativa 1H V2 | LAB | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,18833 | 0,18833 | 0,20950 | 0,28155 | 0,14176 | €222,78 | €445,56 | €50,08 | €-0,00 |
| Forza relativa 1H V2 | GRAM | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 1,47771 | 1,47771 | 1,52060 | 2,20918 | 1,38336 | €871,54 | €1.743,07 | €50,59 | €-0,00 |
| Forza relativa 1H V2 | ESPORTS | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,02126 | 0,02126 | 0,02126 | 0,03178 | 0,01564 | €215,33 | €430,67 | €0,00 | €-0,00 |
| Forza relativa 1H V2 | ADA | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,17438 | 0,17401 | 0,17039 | 0,08806 | 0,18317 | €1.109,61 | €2.219,23 | €50,81 | €-4,77 |
| Scalp RSI Long 25 · €10 · 15x | HYPE | LONG | Inversione RSI estrema 15m | 15m | 15,0x | 60,30006 | 60,30400 | 59,49362 | 56,58155 | 61,50972 | €10,00 | €150,00 | €2,01 | €0,01 |
| Scalp RSI Long 25 · €50 · 15x | HYPE | LONG | Inversione RSI estrema 15m | 15m | 15,0x | 60,30006 | 60,30400 | 59,49362 | 56,58155 | 61,50972 | €50,00 | €750,00 | €10,03 | €0,05 |
| Scalp RSI Long 25 · prudente · 5x | HYPE | LONG | Inversione RSI estrema 15m | 15m | 5,0x | 60,30006 | 60,30400 | 59,49362 | 48,54155 | 61,91294 | €149,55 | €747,73 | €10,00 | €0,05 |
| Benchmark Donchian breakout 1H | SUI | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,76606 | 0,76606 | 0,75182 | 0,38686 | 0,80165 | €1.377,00 | €2.754,00 | €51,18 | €0,00 |
| Benchmark Donchian breakout 1H | ADA | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,17562 | 0,17401 | 0,17105 | 0,08869 | 0,18704 | €975,80 | €1.951,59 | €50,78 | €-17,84 |
| Benchmark Donchian breakout 1H | HYPE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 62,03159 | 60,30400 | 60,88432 | 92,73723 | 59,41682 | €1.505,42 | €3.010,85 | €0,00 | €83,85 |
| Benchmark Bollinger mean reversion 1H | ADA | SHORT | Bollinger mean reversion | 60m | 2,0x | 0,17554 | 0,17401 | 0,17554 | 0,26244 | 0,17041 | €1.300,59 | €2.601,19 | €0,00 | €22,74 |
| Benchmark Bollinger mean reversion 1H | BTC | SHORT | Bollinger mean reversion | 60m | 2,0x | 66739,44944 | 66395,81000 | 66634,73588 | 99775,47691 | 65538,13935 | €2.030,38 | €4.060,77 | €0,00 | €20,91 |
| Benchmark Bollinger mean reversion 1H | HYPE | LONG | Bollinger mean reversion | 60m | 2,0x | 60,65213 | 60,30400 | 59,73275 | 30,62932 | 62,03120 | €1.683,41 | €3.366,81 | €51,04 | €-19,32 |
| Benchmark trend following EMA 1H | ADA | LONG | Trend following EMA | 60m | 2,0x | 0,17417 | 0,17401 | 0,17005 | 0,08796 | 0,18326 | €1.046,69 | €2.093,39 | €49,63 | €-1,98 |
| Benchmark trend following EMA 1H | BTC | LONG | Trend following EMA | 60m | 2,0x | 66805,45842 | 66395,81000 | 65736,57109 | 33736,75650 | 69157,01056 | €1.553,66 | €3.107,32 | €49,72 | €-19,05 |
| Scanner Top 5 Long 1H | ADA | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,17562 | 0,17401 | 0,17150 | 0,08869 | 0,18384 | €1.118,38 | €2.236,77 | €52,38 | €-20,44 |
| Scanner Top 5 Long 1H | BTC | LONG | Scanner Top 5 Long | 60m | 2,0x | 66805,45842 | 66395,81000 | 65843,45982 | 33736,75650 | 68729,45562 | €1.827,61 | €3.655,23 | €52,64 | €-22,41 |
| Scanner Top 5 Long 1H | ONDO | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,40114 | 0,40110 | 0,38834 | 0,20258 | 0,42673 | €828,91 | €1.657,82 | €52,88 | €-0,17 |
| Scanner Bottom 5 Short 1H | ESPORTS | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,02150 | 0,02150 | 0,02150 | 0,03214 | 0,01634 | €207,40 | €414,80 | €0,00 | €-0,00 |
| Scanner Bottom 5 Short 1H | AKE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,00168 | 0,00170 | 0,00188 | 0,00251 | 0,00127 | €203,54 | €407,07 | €48,85 | €-4,95 |
| Scanner Bottom 5 Short 1H | HYPE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 61,72065 | 60,30400 | 60,78747 | 92,27238 | 59,83572 | €1.595,48 | €3.190,95 | €0,00 | €73,24 |
| Scanner Top 5 + forza BTC 1H | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,37613 | 0,40110 | 0,39181 | 0,18994 | 0,40745 | €677,81 | €1.355,62 | €0,00 | €90,01 |
| Scanner Top 5 + forza BTC 1H | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 77,70854 | 77,87200 | 76,45304 | 39,24281 | 80,47063 | €1.614,82 | €3.229,64 | €52,18 | €6,79 |
| Scanner Top 5 + forza BTC 1H | XRP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,14884 | 1,15472 | 1,13230 | 0,58016 | 1,18523 | €1.810,65 | €3.621,30 | €52,15 | €18,54 |
| Top 5 + BTC — solo MFE | SUI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,76776 | 0,76776 | 0,75508 | 0,38772 | 0,79565 | €1.514,04 | €3.028,08 | €50,00 | €0,00 |
| Top 5 + BTC — solo MFE | ADA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,17562 | 0,17401 | 0,17150 | 0,08869 | 0,18466 | €1.073,91 | €2.147,81 | €50,30 | €-19,63 |
| Top 5 + BTC — solo MFE | XRP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,14884 | 1,15472 | 1,14884 | 0,58016 | 1,18523 | €1.740,65 | €3.481,30 | €0,00 | €17,82 |
| Top 5 + BTC — Guard | ADA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,17562 | 0,17401 | 0,17150 | 0,08869 | 0,18466 | €1.054,77 | €2.109,54 | €49,40 | €-19,28 |
| Top 5 + BTC — Guard | XRP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,14947 | 1,15472 | 1,13292 | 0,58048 | 1,18589 | €1.706,64 | €3.413,29 | €49,15 | €15,59 |
| Top 5 + BTC — Guard | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39724 | 0,40110 | 0,38434 | 0,20061 | 0,42561 | €756,62 | €1.513,24 | €49,13 | €14,71 |
| Top 5 + BTC — BTC≤3 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.063,01 | €2.126,01 | €50,00 | €-13,05 |
| Top 5 + BTC — BTC≤3 | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 77,78955 | 77,87200 | 76,66939 | 39,28373 | 80,25393 | €1.735,32 | €3.470,64 | €49,98 | €3,68 |
| Top 5 + BTC — BTC 2–3 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.063,01 | €2.126,01 | €50,00 | €-13,05 |
| Top 5 + BTC — BTC 2–3 | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 77,78955 | 77,87200 | 76,66939 | 39,28373 | 80,25393 | €1.735,32 | €3.470,64 | €49,98 | €3,68 |
| Top 5 + BTC — Guard + MFE | ADA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,17562 | 0,17401 | 0,17150 | 0,08869 | 0,18466 | €1.054,77 | €2.109,54 | €49,40 | €-19,28 |
| Top 5 + BTC — Guard + MFE | XRP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,14947 | 1,15472 | 1,14947 | 0,58048 | 1,18589 | €1.706,64 | €3.413,29 | €0,00 | €15,59 |
| Top 5 + BTC — Guard + MFE | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39724 | 0,40110 | 0,38434 | 0,20061 | 0,42561 | €756,62 | €1.513,24 | €49,13 | €14,71 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.031,84 | €2.063,68 | €50,00 | €-14,01 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | ADA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,17487 | 0,17401 | 0,17143 | 0,08831 | 0,18521 | €1.286,71 | €2.573,42 | €50,71 | €-12,73 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,40394 | 0,40110 | 0,39106 | 0,20399 | 0,44260 | €791,72 | €1.583,44 | €50,51 | €-11,14 |
| Top 5 + BTC — target pieno 3R | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.031,84 | €2.063,68 | €50,00 | €-14,01 |
| Top 5 + BTC — target pieno 3R | ADA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,17487 | 0,17401 | 0,17143 | 0,08831 | 0,18521 | €1.286,71 | €2.573,42 | €50,71 | €-12,73 |
| Top 5 + BTC — target pieno 3R | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,40394 | 0,40110 | 0,39106 | 0,20399 | 0,44260 | €791,72 | €1.583,44 | €50,51 | €-11,14 |
| Combo Trend | ONDO | LONG | Combo Trend | 60m | 2,0x | 0,37282 | 0,40110 | 0,38977 | 0,18828 | 0,41057 | €545,86 | €1.091,71 | €0,00 | €82,80 |
| Combo Trend | ESPORTS | SHORT | Combo Trend | 60m | 2,0x | 0,01883 | 0,01883 | 0,02109 | 0,02815 | 0,01386 | €209,57 | €419,14 | €50,30 | €-0,00 |
| Combo Trend | PEPE | LONG | Combo Trend | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €884,51 | €1.769,01 | €50,29 | €-14,84 |
| Combo Scanner | ONDO | LONG | Combo Scanner | 60m | 2,0x | 0,37282 | 0,40110 | 0,39070 | 0,18828 | 0,40679 | €599,14 | €1.198,28 | €0,00 | €90,88 |
| Combo Scanner | PEPE | LONG | Combo Scanner | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €978,80 | €1.957,60 | €50,08 | €-16,42 |
| Combo Adaptive — madre | GRAM | SHORT | Combo Adaptive | 60m | 2,0x | 1,48181 | 1,48181 | 1,51561 | 2,21531 | 1,41422 | €1.129,35 | €2.258,70 | €51,51 | €-0,00 |
| Combo Adaptive — madre | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.001,06 | €2.002,12 | €51,22 | €-16,79 |
| Combo Adaptive — madre | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,40114 | 0,40110 | 0,38834 | 0,20258 | 0,42673 | €809,25 | €1.618,50 | €51,63 | €-0,16 |
| Combo Adaptive — MFE Trail esistente | ESPORTS | SHORT | Combo Adaptive | 60m | 2,0x | 0,02156 | 0,02156 | 0,02091 | 0,03223 | 0,01638 | €202,62 | €405,24 | €0,00 | €-0,00 |
| Combo Adaptive — MFE Trail esistente | XRP | LONG | Combo Adaptive | 60m | 2,0x | 1,15497 | 1,15472 | 1,13834 | 0,58326 | 1,18823 | €1.677,72 | €3.355,43 | €48,32 | €-0,73 |
| Combo Adaptive — MFE Trail esistente | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39784 | 0,40110 | 0,38492 | 0,20091 | 0,42367 | €744,71 | €1.489,41 | €48,35 | €12,21 |
| Combo Adaptive — Quality7 | ADA | LONG | Combo Adaptive | 60m | 2,0x | 0,17562 | 0,17401 | 0,17150 | 0,08869 | 0,18384 | €1.067,59 | €2.135,18 | €50,00 | €-19,52 |
| Combo Adaptive — Quality7 | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,40394 | 0,40110 | 0,39106 | 0,20399 | 0,42971 | €781,12 | €1.562,25 | €49,83 | €-10,99 |
| Combo Adaptive — Trend/Transition | ADA | LONG | Combo Adaptive | 60m | 2,0x | 0,17562 | 0,17401 | 0,17150 | 0,08869 | 0,18384 | €1.064,94 | €2.129,87 | €49,88 | €-19,47 |
| Combo Adaptive — Trend/Transition | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39724 | 0,40110 | 0,38434 | 0,20061 | 0,42303 | €757,94 | €1.515,88 | €49,21 | €14,74 |
| Combo Adaptive — Trend/Transition | HYPE | SHORT | Combo Adaptive | 60m | 2,0x | 60,62787 | 60,30400 | 61,73069 | 90,63867 | 58,42224 | €1.352,45 | €2.704,89 | €49,20 | €14,45 |
| Combo Adaptive — Quality7 + Regime | ADA | LONG | Combo Adaptive | 60m | 2,0x | 0,17562 | 0,17401 | 0,17150 | 0,08869 | 0,18384 | €1.067,59 | €2.135,18 | €50,00 | €-19,52 |
| Combo Adaptive — Quality7 + Regime | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,40394 | 0,40110 | 0,39106 | 0,20399 | 0,42971 | €781,12 | €1.562,25 | €49,83 | €-10,99 |
| Combo Adaptive — Long Only | ADA | LONG | Combo Adaptive | 60m | 2,0x | 0,17562 | 0,17401 | 0,17150 | 0,08869 | 0,18384 | €1.070,78 | €2.141,56 | €50,15 | €-19,57 |
| Combo Adaptive — Long Only | BTC | LONG | Combo Adaptive | 60m | 2,0x | 66665,25038 | 66395,81000 | 65705,27078 | 33665,95144 | 68585,20960 | €1.731,23 | €3.462,46 | €49,86 | €-13,99 |
| Combo Adaptive — parziale 1R | ADA | LONG | Combo Adaptive | 60m | 2,0x | 0,17562 | 0,17401 | 0,17150 | 0,08869 | 0,18384 | €1.062,51 | €2.125,02 | €49,76 | €-19,42 |
| Combo Adaptive — parziale 1R | BTC | LONG | Combo Adaptive | 60m | 2,0x | 66665,25038 | 66395,81000 | 65705,27078 | 33665,95144 | 68585,20960 | €1.712,08 | €3.424,17 | €49,31 | €-13,84 |
| Combo Adaptive — Quality7 + Regime + parziale 1R | ADA | LONG | Combo Adaptive | 60m | 2,0x | 0,17562 | 0,17401 | 0,17150 | 0,08869 | 0,18384 | €1.067,59 | €2.135,18 | €50,00 | €-19,52 |
| Combo Adaptive — Quality7 + Regime + parziale 1R | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,40394 | 0,40110 | 0,39106 | 0,20399 | 0,42971 | €781,12 | €1.562,25 | €49,83 | €-10,99 |
| Combo Adaptive — 75% a 2R + runner 3R | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.031,84 | €2.063,68 | €50,00 | €-14,01 |
| Combo Adaptive — 75% a 2R + runner 3R | BTC | LONG | Combo Adaptive | 60m | 2,0x | 66575,01234 | 66395,81000 | 65616,33216 | 33620,38123 | 69451,05287 | €1.723,18 | €3.446,36 | €49,63 | €-9,28 |
| Combo Adaptive — target pieno 3R | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.031,84 | €2.063,68 | €50,00 | €-14,01 |
| Combo Adaptive — target pieno 3R | BTC | LONG | Combo Adaptive | 60m | 2,0x | 66575,01234 | 66395,81000 | 65616,33216 | 33620,38123 | 69451,05287 | €1.723,18 | €3.446,36 | €49,63 | €-9,28 |
| Btc Ema 1H | BTC | LONG | Trend following EMA | 60m | 3,0x | 66655,79849 | 66395,81000 | 65695,95500 | 44770,47799 | 68575,48549 | €1.155,97 | €3.467,90 | €49,94 | €-13,53 |
| Btc Ema 4H | BTC | LONG | Trend following EMA | 240m | 2,0x | 65410,57950 | 66395,81000 | 63931,54687 | 33032,34265 | 69108,16107 | €1.105,63 | €2.211,26 | €50,00 | €33,31 |
| Btc Donchian 4H | BTC | LONG | Donchian breakout 20 barre | 240m | 2,0x | 65410,57950 | 66395,81000 | 63931,54687 | 33032,34265 | 69551,87112 | €1.105,63 | €2.211,26 | €50,00 | €33,31 |
| Btc Bollinger 1H | BTC | SHORT | Bollinger mean reversion | 60m | 3,0x | 66739,44944 | 66395,81000 | 67540,32283 | 88652,23534 | 65538,13935 | €1.398,43 | €4.195,29 | €50,34 | €21,60 |
| Btc Bollinger 4H | BTC | SHORT | Bollinger mean reversion | 240m | 2,0x | 66588,49964 | 66395,81000 | 67855,55360 | 99549,80696 | 64307,80290 | €1.313,84 | €2.627,69 | €50,00 | €7,60 |
| Btc Adaptive 4H | BTC | LONG | Combo Adaptive | 240m | 2,0x | 66171,85172 | 66395,81000 | 64592,42491 | 33416,78512 | 70120,41876 | €1.047,40 | €2.094,81 | €50,00 | €7,09 |
| Sol Ema 1H | SOL | LONG | Trend following EMA | 60m | 3,0x | 77,56451 | 77,87200 | 76,27481 | 52,09750 | 80,14392 | €1.001,44 | €3.004,32 | €49,95 | €11,91 |
| Sol Ema 4H | SOL | LONG | Trend following EMA | 240m | 2,0x | 78,49069 | 77,87200 | 76,26213 | 39,63780 | 84,06211 | €880,51 | €1.761,01 | €50,00 | €-13,88 |
| Sol Donchian 4H | SOL | LONG | Donchian breakout 20 barre | 240m | 2,0x | 78,49069 | 77,87200 | 76,26213 | 39,63780 | 84,73068 | €880,51 | €1.761,01 | €50,00 | €-13,88 |
| Sol Bollinger 4H | SOL | SHORT | Bollinger mean reversion | 240m | 2,0x | 78,45931 | 77,87200 | 80,48446 | 117,29666 | 74,81402 | €968,56 | €1.937,11 | €50,00 | €14,50 |
| Sol Adaptive 1H | SOL | LONG | Combo Adaptive | 60m | 3,0x | 77,56451 | 77,87200 | 76,27481 | 52,09750 | 80,14392 | €1.000,51 | €3.001,52 | €49,91 | €11,90 |
| Sol Adaptive 4H | SOL | LONG | Combo Adaptive | 240m | 2,0x | 78,49069 | 77,87200 | 76,05953 | 39,63780 | 84,56860 | €807,13 | €1.614,26 | €50,00 | €-12,72 |
| Eth Ema 4H | ETH | LONG | Trend following EMA | 240m | 2,0x | 1933,63665 | 1921,62000 | 1878,94813 | 976,48651 | 2070,35799 | €883,93 | €1.767,86 | €50,00 | €-10,99 |
| Master Adaptive V1 | ADA | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,17603 | 0,17401 | 0,17190 | 0,08889 | 0,18427 | €1.067,59 | €2.135,18 | €50,00 | €-24,44 |
| Master Adaptive V1 | PEPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.167,62 | €2.335,24 | €49,98 | €-19,35 |
| Master Adaptive V1 | BTC | LONG | Master Adaptive Consensus | 60m | 2,0x | 66665,25038 | 66395,81000 | 65705,27078 | 33665,95144 | 68585,20960 | €1.722,26 | €3.444,53 | €49,60 | €-13,92 |
| Master Adaptive No Alt V1 | ADA | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,17603 | 0,17401 | 0,17190 | 0,08889 | 0,18427 | €1.067,59 | €2.135,18 | €50,00 | €-24,44 |
| Master Adaptive No Alt V1 | PEPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.167,62 | €2.335,24 | €49,98 | €-19,35 |
| Master Adaptive No Alt V1 | BTC | LONG | Master Adaptive Consensus | 60m | 2,0x | 66665,25038 | 66395,81000 | 65705,27078 | 33665,95144 | 68585,20960 | €1.722,26 | €3.444,53 | €49,60 | €-13,92 |
| Master Adaptive Strict3 V1 | ADA | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,17603 | 0,17401 | 0,17190 | 0,08889 | 0,18427 | €1.067,59 | €2.135,18 | €50,00 | €-24,44 |
| Master Adaptive Strict3 V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 1934,24677 | 1921,62000 | 1906,39362 | 976,79462 | 1989,95308 | €1.737,12 | €3.474,23 | €50,03 | €-22,68 |
| Master Adaptive Strict3 V1 | XRP | LONG | Master Adaptive Consensus | 60m | 2,0x | 1,14947 | 1,15472 | 1,13292 | 0,58048 | 1,18257 | €1.722,92 | €3.445,84 | €49,62 | €15,74 |
| Master Adaptive Expanded V1 | ADA | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,17603 | 0,17401 | 0,17190 | 0,08889 | 0,18427 | €1.067,59 | €2.135,18 | €50,00 | €-24,44 |
| Master Adaptive Expanded V1 | PEPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.167,62 | €2.335,24 | €49,98 | €-19,35 |
| Master Adaptive Expanded V1 | BTC | LONG | Master Adaptive Consensus | 60m | 2,0x | 66665,25038 | 66395,81000 | 65705,27078 | 33665,95144 | 68585,20960 | €1.722,26 | €3.444,53 | €49,60 | €-13,92 |
| Master Adaptive Gb20 V1 | ADA | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,17603 | 0,17401 | 0,17190 | 0,08889 | 0,18427 | €1.067,59 | €2.135,18 | €50,00 | €-24,44 |
| Master Adaptive Gb20 V1 | BTC | LONG | Master Adaptive Consensus | 60m | 2,0x | 66665,25038 | 66395,81000 | 65705,27078 | 33665,95144 | 68585,20960 | €1.718,57 | €3.437,14 | €49,49 | €-13,89 |
| Master Adaptive Gb20 V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,40394 | 0,40110 | 0,39106 | 0,20399 | 0,42971 | €770,30 | €1.540,60 | €49,14 | €-10,84 |
| Master Adaptive Runner25 V1 | ADA | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,17603 | 0,17401 | 0,17190 | 0,08889 | 0,18839 | €1.067,59 | €2.135,18 | €50,00 | €-24,44 |
| Master Adaptive Runner25 V1 | PEPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.167,62 | €2.335,24 | €49,98 | €-19,35 |
| Master Adaptive Runner25 V1 | BTC | LONG | Master Adaptive Consensus | 60m | 2,0x | 66665,25038 | 66395,81000 | 65705,27078 | 33665,95144 | 69545,18920 | €1.722,26 | €3.444,53 | €49,60 | €-13,92 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Combo Adaptive — target pieno 3R | HYPE | SHORT | 2026-07-21T19:53:34+00:00 | 60,74453 | €43,43 | 0,88 | STOP |
| Combo Adaptive — 75% a 2R + runner 3R | HYPE | SHORT | 2026-07-21T19:53:34+00:00 | 60,74453 | €43,43 | 0,88 | STOP |
| Combo Adaptive — parziale 1R | HYPE | SHORT | 2026-07-21T19:53:34+00:00 | 60,74866 | €48,78 | 0,99 | STOP |
| Scanner Top 5 Long 1H | ONDO | LONG | 2026-07-21T19:23:33+00:00 | 0,40346 | €101,18 | 1,95 | TARGET |
| Combo Adaptive — madre | ONDO | LONG | 2026-07-21T19:23:33+00:00 | 0,40346 | €99,23 | 1,95 | TARGET |
| Rapida V1 — target pieno 2R | HYPE | SHORT | 2026-07-21T19:23:33+00:00 | 60,19376 | €93,37 | 1,88 | TARGET |
| Top 5 + BTC — target pieno 3R | XRP | LONG | 2026-07-21T18:53:34+00:00 | 1,15355 | €48,70 | 0,96 | STOP |
| Top 5 + BTC — 75% a 2,2R + runner 3R | XRP | LONG | 2026-07-21T18:53:34+00:00 | 1,15355 | €48,70 | 0,96 | STOP |
| Master Adaptive Gb20 V1 | XRP | LONG | 2026-07-21T18:53:34+00:00 | 1,15133 | €-14,92 | -0,30 | STOP_GAP_STRESS |
| Bilanciata 1H V3 Filtered | XRP | LONG | 2026-07-21T18:53:34+00:00 | 1,15360 | €35,11 | 0,68 | STOP |
| Bilanciata 1H V1 | XRP | LONG | 2026-07-21T18:53:34+00:00 | 1,15323 | €50,63 | 1,00 | STOP |
| Sol Donchian 1H | SOL | LONG | 2026-07-21T18:08:35+00:00 | 77,70428 | €1,86 | 0,04 | STOP |

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
| MAIN | Principale 4H | 36/30 | 16/30 | 0,85 | 0,81 | -0,11R | €-6,29 | 4,26% | COERENTE − | BOCCIATA RESEARCH |
| RSI_EXTREME_LONG_15M | Scalp RSI Long 25 · prudente · 5x (riferimento tra 9 varianti) | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,01% | n/a | RACCOLTA RESEARCH |
| RSI_EXTREME_SHORT_15M | Scalp RSI Short 75 · prudente · 5x (riferimento tra 9 varianti) | 6/30 | 5/30 | 0,29 | 0,19 | -0,52R | €-6,38 | 0,32% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_1H_BALANCED | Bilanciata 1H V1 | 119/30 | 23/30 | 1,04 | 1,44 | 0,02R | €7,50 | 1,81% | COERENTE + | BOCCIATA RESEARCH |
| SHADOW_1H_BALANCED_V2 | Bilanciata 1H V2 | 17/30 | 15/30 | 1,51 | 0,89 | 0,30R | €-2,84 | 2,75% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_1H_BALANCED_V3 | Bilanciata 1H V3 Filtered | 35/30 | 26/30 | 1,39 | 1,45 | 0,24R | €11,19 | 2,20% | COERENTE + | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_1H_FAST | Rapida 1H V1 — madre | 136/30 | 49/30 | 0,91 | 0,92 | -0,06R | €-1,82 | 5,79% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | Rapida V1 — Long + BTC 1–3 + score <7,5 | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | Rapida V1 — no HIGH + score <7,5 | 8/30 | 7/30 | 0,42 | 0,48 | -0,47R | €-21,23 | 2,52% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_NO_PEPE_V1 | Rapida V1 — senza PEPE | 7/30 | 6/30 | 0,51 | 1,06 | -0,38R | €1,21 | 2,00% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_V1 | Rapida V1 — score 6–7,5 | 5/30 | 6/30 | 0,85 | 0,99 | -0,09R | €-0,24 | 1,80% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_TP2_V1 | Rapida V1 — target pieno 2R | 8/30 | 6/30 | 0,58 | 1,44 | -0,34R | €9,51 | 2,01% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V2 | Rapida 1H V2 | 2/30 | 2/30 | 0,59 | 1,07 | -0,31R | €1,44 | 0,93% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3 | Rapida 1H V3 Filtered — madre | 49/30 | 41/30 | 1,10 | 0,99 | 0,06R | €-0,18 | 2,89% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_CAP75_V1 | Rapida V3 — score <7,5 | 7/30 | 6/30 | 0,51 | 0,99 | -0,38R | €-0,24 | 2,11% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | Rapida V3 — qualità completa + profit lock | 4/30 | 3/30 | 0,41 | 0,62 | -0,49R | €-13,95 | 1,03% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | Rapida V3 — Long + no HIGH + score <7,5 | 4/30 | 3/30 | 0,41 | 0,62 | -0,49R | €-13,95 | 1,03% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | Rapida V3 — Long Only | 4/30 | 3/30 | 0,41 | 7,81 | -0,49R | €19,84 | 0,84% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | Rapida V3 — no volatilità HIGH | 9/30 | 6/30 | 0,36 | 0,57 | -0,54R | €-16,92 | 2,37% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | Rapida V3 — senza ESPORTS | 8/30 | 6/30 | 0,42 | 0,99 | -0,47R | €-0,24 | 2,11% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_4H_WIDE | Ampia 4H | 36/30 | 12/30 | 0,78 | 1,27 | -0,18R | €7,39 | 2,13% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_BOLLINGER_MR_1H | Benchmark Bollinger mean reversion 1H | 23/30 | 15/30 | 0,86 | 1,66 | -0,09R | €10,14 | 2,06% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_BTC_ADAPTIVE_1H | Btc Adaptive 1H | 1/30 | 2/30 | 0,00 | 0,78 | -1,11R | €-5,87 | 0,89% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_ADAPTIVE_4H | Btc Adaptive 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,19% | n/a | RACCOLTA RESEARCH |
| SHADOW_BTC_BOLLINGER_1H | Btc Bollinger 1H | 1/30 | 1/30 | ∞ | ∞ | 1,37R | €68,69 | 0,31% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_BTC_BOLLINGER_4H | Btc Bollinger 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,10% | n/a | RACCOLTA RESEARCH |
| SHADOW_BTC_DONCHIAN_1H | Btc Donchian 1H | 2/30 | 3/30 | 0,00 | 0,43 | -1,12R | €-20,81 | 1,49% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_DONCHIAN_4H | Btc Donchian 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,20% | n/a | RACCOLTA RESEARCH |
| SHADOW_BTC_EMA_1H | Btc Ema 1H | 3/30 | 3/30 | 0,85 | 0,89 | -0,11R | €-4,15 | 1,56% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_EMA_4H | Btc Ema 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,20% | n/a | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE | Combo Adaptive — madre | 63/30 | 17/30 | 1,58 | 2,52 | 0,33R | €20,32 | 1,27% | COERENTE + | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | Combo Adaptive — Long Only | 5/30 | 3/30 | 1,22 | 0,79 | 0,14R | €-8,40 | 1,54% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | Combo Adaptive — MFE Trail esistente | 33/30 | 24/30 | 1,56 | 0,32 | 0,32R | €-14,73 | 3,59% | DIVERGENTE | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | Combo Adaptive — parziale 1R | 8/30 | 6/30 | 1,09 | 0,54 | 0,06R | €-17,48 | 2,05% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | Combo Adaptive — Quality7 + Regime + parziale 1R | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,54% | n/a | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | Combo Adaptive — Quality7 + Regime | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,54% | n/a | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | Combo Adaptive — Quality7 | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,54% | n/a | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | Combo Adaptive — Trend/Transition | 7/30 | 5/30 | 0,73 | 0,42 | -0,20R | €-26,23 | 1,86% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | Combo Adaptive — 75% a 2R + runner 3R | 5/30 | 4/30 | 0,00 | 0,79 | -1,05R | €-5,53 | 1,41% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | Combo Adaptive — target pieno 3R | 5/30 | 4/30 | 0,00 | 0,79 | -1,05R | €-5,53 | 1,41% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_MEAN_REVERSION | Combo Mean Reversion | 8/30 | 7/30 | 2,42 | 2,81 | 0,55R | €27,88 | 0,59% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_COMBO_SCANNER | Combo Scanner | 39/30 | 18/30 | 1,78 | 0,92 | 0,44R | €-2,11 | 2,18% | DIVERGENTE | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_COMBO_TREND | Combo Trend | 50/30 | 15/30 | 1,16 | 1,15 | 0,11R | €3,86 | 2,19% | COERENTE + | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_DOGE_BOLLINGER_1H | Doge Bollinger 1H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_DOGE_DONCHIAN_1H | Doge Donchian 1H | 1/30 | 2/30 | 0,00 | 0,46 | -1,12R | €-15,51 | 0,93% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_DOGE_EMA_1H | Doge Ema 1H | 1/30 | 4/30 | 0,00 | 0,54 | -1,11R | €-12,93 | 1,27% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_DONCHIAN_1H | Benchmark Donchian breakout 1H | 29/30 | 15/30 | 0,87 | 1,46 | -0,10R | €10,49 | 1,98% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_EMA_TREND_1H | Benchmark trend following EMA 1H | 56/30 | 11/30 | 1,12 | 0,76 | 0,08R | €-6,93 | 2,25% | DIVERGENTE | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_ETH_ADAPTIVE_1H | Eth Adaptive 1H | 2/30 | 3/30 | 1,70 | 0,31 | 0,39R | €-12,55 | 1,02% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_ETH_BOLLINGER_1H | Eth Bollinger 1H | 1/30 | 1/30 | 0,00 | ∞ | -1,13R | €15,45 | 0,51% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_ETH_DONCHIAN_1H | Eth Donchian 1H | 3/30 | 3/30 | 0,84 | 0,84 | -0,12R | €-5,82 | 1,38% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_EMA_1H | Eth Ema 1H | 2/30 | 5/30 | 1,70 | 0,33 | 0,39R | €-22,05 | 1,59% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_ETH_EMA_4H | Eth Ema 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,25% | n/a | RACCOLTA RESEARCH |
| SHADOW_GLOBAL_PURE | Global Confluence puro 1H | 1/30 | 7/30 | 0,00 | 0,17 | -1,10R | €-32,29 | 2,46% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | Master Adaptive Expanded V1 | 2/30 | 1/30 | 0,00 | 0,00 | -1,06R | €-54,91 | 1,78% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | Master Adaptive Gb20 V1 | 2/30 | 4/30 | 0,00 | 0,08 | -1,06R | €-28,25 | 2,05% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | Master Adaptive No Alt V1 | 2/30 | 1/30 | 0,00 | 0,00 | -1,06R | €-54,91 | 1,78% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | Master Adaptive Runner25 V1 | 2/30 | 1/30 | 0,00 | 0,00 | -1,06R | €-54,91 | 1,78% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | Master Adaptive Strict3 V1 | 1/30 | 1/30 | 0,00 | 0,00 | -1,11R | €-54,91 | 1,27% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_V1 | Master Adaptive V1 | 2/30 | 1/30 | 0,00 | 0,00 | -1,06R | €-54,91 | 1,78% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_RELATIVE_STRENGTH | Forza relativa 1H V1 | 78/30 | 18/30 | 0,96 | 1,35 | -0,03R | €5,10 | 2,29% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_RELATIVE_STRENGTH_V2 | Forza relativa 1H V2 | 21/30 | 18/30 | 1,62 | 1,33 | 0,36R | €9,11 | 2,41% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT | Scanner Bottom 5 Short 1H | 26/30 | 14/30 | 0,63 | 0,33 | -0,26R | €-19,70 | 4,68% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC | Scanner Top 5 + forza BTC 1H | 42/30 | 18/30 | 1,79 | 2,49 | 0,43R | €23,33 | 1,62% | COERENTE + | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | Top 5 + BTC — BTC 2–3 | 2/30 | 1/30 | 0,00 | ∞ | -1,01R | €58,86 | 1,22% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | Top 5 + BTC — BTC≤3 | 2/30 | 1/30 | 0,00 | ∞ | -1,01R | €58,86 | 1,22% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | Top 5 + BTC — Guard + BTC≤3 + MFE | 2/30 | 2/30 | 0,00 | 0,00 | -1,01R | €-59,29 | 1,19% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | Top 5 + BTC — Guard + BTC≤3 | 2/30 | 2/30 | 0,00 | 0,00 | -1,01R | €-59,29 | 1,19% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | Top 5 + BTC — Guard + MFE | 3/30 | 3/30 | 0,00 | 0,00 | -1,04R | €-57,60 | 2,08% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | Top 5 + BTC — Guard | 3/30 | 3/30 | 0,00 | 0,00 | -1,04R | €-57,60 | 2,08% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | Top 5 + BTC — solo MFE | 4/30 | 2/30 | 0,67 | 8,40 | -0,26R | €16,60 | 0,87% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | Top 5 + BTC — 75% a 2,2R + runner 3R | 3/30 | 3/30 | 0,00 | ∞ | -1,05R | €48,70 | 0,79% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | Top 5 + BTC — target pieno 3R | 3/30 | 3/30 | 0,00 | ∞ | -1,05R | €48,70 | 0,79% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_LONG | Scanner Top 5 Long 1H | 54/30 | 26/30 | 1,79 | 2,50 | 0,42R | €24,13 | 2,70% | COERENTE + | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_SOL_ADAPTIVE_1H | Sol Adaptive 1H | 2/30 | 2/30 | 1,70 | 0,67 | 0,39R | €-9,23 | 0,99% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SOL_ADAPTIVE_4H | Sol Adaptive 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,18% | n/a | RACCOLTA RESEARCH |
| SHADOW_SOL_BOLLINGER_1H | Sol Bollinger 1H | 1/30 | 1/30 | 0,00 | 0,00 | -1,13R | €-55,79 | 0,62% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_BOLLINGER_4H | Sol Bollinger 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,12% | n/a | RACCOLTA RESEARCH |
| SHADOW_SOL_DONCHIAN_1H | Sol Donchian 1H | 1/30 | 2/30 | 0,00 | 0,41 | -1,12R | €-1,31 | 0,55% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_DONCHIAN_4H | Sol Donchian 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,20% | n/a | RACCOLTA RESEARCH |
| SHADOW_SOL_EMA_1H | Sol Ema 1H | 2/30 | 2/30 | 1,70 | 0,83 | 0,39R | €-4,58 | 0,98% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SOL_EMA_4H | Sol Ema 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,20% | n/a | RACCOLTA RESEARCH |

Per le famiglie RSI con più configurazioni di leva o margine, il lato paper usa il conto con il maggior numero di eventi indipendenti; i conti duplicati non vengono aggregati.
`PRONTA PER REVISIONE LIVE` non invia ordini e non sposta capitale: abilita soltanto una revisione manuale finale.

## 🎯 DOGE Rejection Short — conto dedicato €3.600

Simulazione separata **paper only**: capitale/margine iniziale **€3.600**, leva **5x**, esposizione iniziale **€18.000**. Non modifica i conti paper da €10.000 e non invia ordini reali.

- Stato: **WAITING**
- Prezzo DOGE: **0.07351**
- Pre-allarme: **0.0765**; zona armata: **0.0775**; trigger rejection: **0.078**
- Invalidazione prima dell’entrata: chiusura 15m sopra **0.07966**

| Capitale iniziale | Balance | Equity | P&L aperto | Eventi chiusi | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- |
| €3.600,00 | €3.600,00 | €3.600,00 | €0,00 | 0 | 0,00% | 0,00 | 0,00% |

### Filtri correnti

| Filtro | Valore | Stato |
| --- | --- | --- |
| Dati mercato | FRESH | OK |
| Candela 15m | 23.8 min | OK |
| Global DOGE | -6.0 | OK |
| Classic raw | -11.0 | OK |
| DOGE/BTC raw | -6.0 | OK |
| Pattern ribassista | MATURO | OK |
| BTC sotto filtro | 66395.81 | NO |

### Ultima candela 15m valutata

- Rejection accettata: **NO**; motivo: **trigger_touched, entry_not_chased, upper_wick**
- High **0.07353**; close **0.0735**; wick alta **25.0%**; volume **x0.57**

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
- Confidenza: **81,00%**
- Volatilità: **NORMAL**
- Rotazione strategie: **SOLO OSSERVAZIONE — nessun peso operativo viene ancora modificato**
- Motivo: Trend BTC rialzista confermato dalla breadth: score +4.0, 75% sopra EMA50, ADX 29.7.
- BTC trend score: **4,00**; ADX: **29,73**; breadth sopra EMA50: **75,00%**
- Mediana alt vs BTC: **-1,13%**; dispersione: **12,60%**

- Aperti in questo ciclo: **20**
- Chiusi in questo ciclo: **6**
- Posizioni research aperte: **389**
- Trade research chiusi: **1117**
- Eventi di mercato indipendenti chiusi: **386**
- Segnali sovrapposti saltati sullo stesso asset/profilo: **4261**
- Posizioni Research V1 senza regime scartate durante la migrazione: **28**

### Risultati complessivi per strategia

| Profilo | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| MAIN | 15 | 36 | 36 | 30,56% | 0,85 | -0,11R | €-38,37 |
| RSI_EXTREME_LONG_15M | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| RSI_EXTREME_SHORT_15M | 0 | 6 | 6 | 16,67% | 0,29 | -0,52R | €-31,30 |
| Bilanciata 1H V1 | 14 | 119 | 119 | 35,29% | 1,04 | 0,02R | €27,93 |
| Bilanciata 1H V2 | 5 | 20 | 17 | 45,00% | 1,51 | 0,30R | €59,34 |
| Bilanciata 1H V3 Filtered | 9 | 35 | 35 | 42,86% | 1,39 | 0,24R | €82,81 |
| Rapida 1H V1 | 11 | 136 | 136 | 38,97% | 0,91 | -0,06R | €-77,40 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | 6 | 8 | 8 | 25,00% | 0,42 | -0,47R | €-37,20 |
| SHADOW_1H_FAST_NO_PEPE_V1 | 8 | 7 | 7 | 28,57% | 0,51 | -0,38R | €-26,32 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | 6 | 5 | 5 | 40,00% | 0,85 | -0,09R | €-4,62 |
| SHADOW_1H_FAST_TP2_V1 | 8 | 8 | 8 | 25,00% | 0,58 | -0,34R | €-27,34 |
| Rapida 1H V2 | 0 | 3 | 2 | 33,33% | 0,59 | -0,31R | €-9,29 |
| Rapida 1H V3 Filtered | 11 | 49 | 49 | 44,90% | 1,10 | 0,06R | €27,45 |
| SHADOW_1H_FAST_V3_CAP75_V1 | 8 | 7 | 7 | 28,57% | 0,51 | -0,38R | €-26,33 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | 3 | 4 | 4 | 25,00% | 0,41 | -0,49R | €-19,59 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | 3 | 4 | 4 | 25,00% | 0,41 | -0,49R | €-19,59 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | 5 | 4 | 4 | 25,00% | 0,41 | -0,49R | €-19,72 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | 6 | 9 | 9 | 22,22% | 0,36 | -0,54R | €-48,23 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | 8 | 8 | 8 | 25,00% | 0,42 | -0,47R | €-37,35 |
| SHADOW_4H_WIDE | 18 | 36 | 36 | 22,22% | 0,78 | -0,18R | €-63,44 |
| SHADOW_BOLLINGER_MR_1H | 4 | 23 | 23 | 39,13% | 0,86 | -0,09R | €-21,65 |
| SHADOW_BTC_ADAPTIVE_1H | 1 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_BTC_ADAPTIVE_4H | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_BOLLINGER_1H | 1 | 1 | 1 | 100,00% | ∞ | 1,37R | €13,67 |
| SHADOW_BTC_BOLLINGER_4H | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_DONCHIAN_1H | 1 | 2 | 2 | 0,00% | 0,00 | -1,12R | €-22,50 |
| SHADOW_BTC_DONCHIAN_4H | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_EMA_1H | 1 | 3 | 3 | 33,33% | 0,85 | -0,11R | €-3,33 |
| SHADOW_BTC_EMA_4H | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_ADAPTIVE | 13 | 63 | 63 | 46,03% | 1,58 | 0,33R | €207,55 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | 7 | 5 | 5 | 40,00% | 1,22 | 0,14R | €6,96 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | 10 | 33 | 33 | 45,45% | 1,56 | 0,32R | €104,29 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | 8 | 8 | 8 | 37,50% | 1,09 | 0,06R | €4,63 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | 9 | 7 | 7 | 28,57% | 0,73 | -0,20R | €-14,32 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | 9 | 5 | 5 | 0,00% | 0,00 | -1,05R | €-52,63 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | 9 | 5 | 5 | 0,00% | 0,00 | -1,05R | €-52,63 |
| SHADOW_COMBO_MEAN_REVERSION | 0 | 8 | 8 | 62,50% | 2,42 | 0,55R | €44,38 |
| SHADOW_COMBO_SCANNER | 8 | 39 | 39 | 46,15% | 1,78 | 0,44R | €170,80 |
| SHADOW_COMBO_TREND | 13 | 50 | 50 | 36,00% | 1,16 | 0,11R | €53,33 |
| SHADOW_DOGE_DONCHIAN_1H | 0 | 1 | 1 | 0,00% | 0,00 | -1,12R | €-11,25 |
| SHADOW_DOGE_EMA_1H | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_DONCHIAN_1H | 8 | 29 | 29 | 27,59% | 0,87 | -0,10R | €-29,37 |
| SHADOW_EMA_TREND_1H | 13 | 56 | 56 | 33,93% | 1,12 | 0,08R | €42,79 |
| SHADOW_ETH_ADAPTIVE_1H | 1 | 2 | 2 | 50,00% | 1,70 | 0,39R | €7,78 |
| SHADOW_ETH_BOLLINGER_1H | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,33 |
| SHADOW_ETH_DONCHIAN_1H | 0 | 3 | 3 | 33,33% | 0,84 | -0,12R | €-3,61 |
| SHADOW_ETH_EMA_1H | 1 | 2 | 2 | 50,00% | 1,70 | 0,39R | €7,78 |
| SHADOW_ETH_EMA_4H | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_GLOBAL_PURE | 1 | 1 | 1 | 0,00% | 0,00 | -1,10R | €-11,00 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | 6 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,23 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | 6 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,23 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | 6 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,23 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | 6 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,23 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | 6 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,09 |
| SHADOW_MASTER_ADAPTIVE_V1 | 6 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,23 |
| Forza relativa 1H V1 | 13 | 78 | 78 | 30,77% | 0,96 | -0,03R | €-21,06 |
| Forza relativa 1H V2 | 6 | 23 | 21 | 43,48% | 1,62 | 0,36R | €83,73 |
| SHADOW_SCANNER_BOTTOM5_SHORT | 5 | 26 | 26 | 23,08% | 0,63 | -0,26R | €-68,58 |
| SHADOW_SCANNER_TOP5_BTC | 7 | 42 | 42 | 45,24% | 1,79 | 0,43R | €181,36 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | 4 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | 4 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | 3 | 3 | 3 | 0,00% | 0,00 | -1,04R | €-31,06 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | 3 | 3 | 3 | 0,00% | 0,00 | -1,04R | €-31,06 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | 7 | 4 | 4 | 25,00% | 0,67 | -0,26R | €-10,30 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | 6 | 3 | 3 | 0,00% | 0,00 | -1,05R | €-31,36 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | 6 | 3 | 3 | 0,00% | 0,00 | -1,05R | €-31,36 |
| SHADOW_SCANNER_TOP5_LONG | 8 | 54 | 54 | 48,15% | 1,79 | 0,42R | €224,62 |
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
| MAIN | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| MAIN | ALT_ROTATION_UP | 3 | 3 | 3 | 0,00% | 0,00 | -1,01R | €-30,40 |
| MAIN | RANGE | 0 | 14 | 14 | 28,57% | 0,77 | -0,17R | €-23,82 |
| MAIN | RANGE_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| MAIN | TRANSITION | 4 | 4 | 4 | 25,00% | 0,65 | -0,27R | €-10,68 |
| MAIN | TREND_UP | 4 | 11 | 11 | 36,36% | 1,10 | 0,06R | €7,06 |
| MAIN | TREND_UP_HIGH_VOL | 3 | 3 | 3 | 33,33% | 0,98 | -0,01R | €-0,40 |
| RSI_EXTREME_LONG_15M | TREND_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| RSI_EXTREME_SHORT_15M | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,90 |
| RSI_EXTREME_SHORT_15M | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -0,41R | €-4,13 |
| RSI_EXTREME_SHORT_15M | TREND_UP | 0 | 4 | 4 | 25,00% | 0,44 | -0,41R | €-16,27 |
| Bilanciata 1H V1 | ALT_ROTATION_DOWN | 1 | 1 | 1 | 100,00% | ∞ | 1,89R | €18,95 |
| Bilanciata 1H V1 | ALT_ROTATION_UP | 0 | 13 | 13 | 53,85% | 2,16 | 0,56R | €72,85 |
| Bilanciata 1H V1 | RANGE | 1 | 27 | 27 | 29,63% | 0,81 | -0,13R | €-36,30 |
| Bilanciata 1H V1 | RANGE_HIGH_VOL | 1 | 10 | 10 | 0,00% | 0,00 | -1,07R | €-107,38 |
| Bilanciata 1H V1 | TRANSITION | 2 | 25 | 25 | 32,00% | 0,90 | -0,07R | €-17,37 |
| Bilanciata 1H V1 | TREND_UP | 5 | 34 | 34 | 44,12% | 1,54 | 0,30R | €102,84 |
| Bilanciata 1H V1 | TREND_UP_HIGH_VOL | 4 | 9 | 9 | 33,33% | 0,91 | -0,06R | €-5,65 |
| Bilanciata 1H V2 | ALT_ROTATION_UP | 1 | 4 | 3 | 100,00% | ∞ | 1,93R | €77,01 |
| Bilanciata 1H V2 | RANGE | 1 | 5 | 4 | 40,00% | 1,19 | 0,13R | €6,40 |
| Bilanciata 1H V2 | TRANSITION | 3 | 11 | 10 | 27,27% | 0,71 | -0,22R | €-24,07 |
| Bilanciata 1H V3 Filtered | ALT_ROTATION_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 1,89R | €18,95 |
| Bilanciata 1H V3 Filtered | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| Bilanciata 1H V3 Filtered | RANGE_HIGH_VOL | 1 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| Bilanciata 1H V3 Filtered | TRANSITION | 0 | 6 | 6 | 33,33% | 0,92 | -0,06R | €-3,44 |
| Bilanciata 1H V3 Filtered | TREND_UP | 3 | 17 | 17 | 52,94% | 2,13 | 0,55R | €93,28 |
| Bilanciata 1H V3 Filtered | TREND_UP_HIGH_VOL | 5 | 9 | 9 | 33,33% | 0,91 | -0,06R | €-5,71 |
| Rapida 1H V1 | ALT_ROTATION_DOWN | 2 | 1 | 1 | 100,00% | ∞ | 1,36R | €13,64 |
| Rapida 1H V1 | ALT_ROTATION_UP | 1 | 9 | 9 | 55,56% | 1,73 | 0,34R | €30,84 |
| Rapida 1H V1 | RANGE | 0 | 35 | 35 | 40,00% | 1,04 | 0,02R | €8,01 |
| Rapida 1H V1 | RANGE_HIGH_VOL | 0 | 11 | 11 | 0,00% | 0,00 | -1,09R | €-119,90 |
| Rapida 1H V1 | TRANSITION | 0 | 23 | 23 | 43,48% | 1,20 | 0,11R | €24,41 |
| Rapida 1H V1 | TREND_UP | 4 | 40 | 40 | 42,50% | 1,00 | 0,00R | €0,73 |
| Rapida 1H V1 | TREND_UP_HIGH_VOL | 4 | 17 | 17 | 35,29% | 0,70 | -0,21R | €-35,14 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | ALT_ROTATION_DOWN | 1 | 1 | 1 | 100,00% | ∞ | 1,36R | €13,64 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TREND_UP | 5 | 7 | 7 | 14,29% | 0,21 | -0,73R | €-50,85 |
| SHADOW_1H_FAST_NO_PEPE_V1 | ALT_ROTATION_DOWN | 1 | 1 | 1 | 100,00% | ∞ | 1,36R | €13,64 |
| SHADOW_1H_FAST_NO_PEPE_V1 | ALT_ROTATION_UP | 2 | 1 | 1 | 100,00% | ∞ | 1,36R | €13,57 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_UP | 5 | 5 | 5 | 0,00% | 0,00 | -1,07R | €-53,54 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | ALT_ROTATION_DOWN | 1 | 1 | 1 | 100,00% | ∞ | 1,36R | €13,64 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | ALT_ROTATION_UP | 2 | 1 | 1 | 100,00% | ∞ | 1,36R | €13,57 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_UP | 3 | 3 | 3 | 0,00% | 0,00 | -1,06R | €-31,83 |
| SHADOW_1H_FAST_TP2_V1 | ALT_ROTATION_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 1,86R | €18,64 |
| SHADOW_1H_FAST_TP2_V1 | ALT_ROTATION_UP | 2 | 1 | 1 | 100,00% | ∞ | 1,86R | €18,57 |
| SHADOW_1H_FAST_TP2_V1 | TREND_UP | 6 | 6 | 6 | 0,00% | 0,00 | -1,08R | €-64,55 |
| Rapida 1H V2 | RANGE | 0 | 2 | 1 | 50,00% | 1,19 | 0,11R | €2,14 |
| Rapida 1H V2 | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -1,14R | €-11,43 |
| Rapida 1H V3 Filtered | ALT_ROTATION_DOWN | 3 | 1 | 1 | 100,00% | ∞ | 1,36R | €13,64 |
| Rapida 1H V3 Filtered | ALT_ROTATION_UP | 1 | 2 | 2 | 100,00% | ∞ | 1,44R | €28,86 |
| Rapida 1H V3 Filtered | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| Rapida 1H V3 Filtered | TRANSITION | 0 | 5 | 5 | 40,00% | 0,91 | -0,06R | €-2,77 |
| Rapida 1H V3 Filtered | TREND_UP | 3 | 24 | 24 | 50,00% | 1,37 | 0,19R | €46,75 |
| Rapida 1H V3 Filtered | TREND_UP_HIGH_VOL | 4 | 16 | 16 | 31,25% | 0,59 | -0,31R | €-48,91 |
| SHADOW_1H_FAST_V3_CAP75_V1 | ALT_ROTATION_DOWN | 2 | 1 | 1 | 100,00% | ∞ | 1,36R | €13,64 |
| SHADOW_1H_FAST_V3_CAP75_V1 | ALT_ROTATION_UP | 2 | 1 | 1 | 100,00% | ∞ | 1,36R | €13,57 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_UP | 4 | 5 | 5 | 0,00% | 0,00 | -1,07R | €-53,55 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TREND_UP | 2 | 4 | 4 | 25,00% | 0,41 | -0,49R | €-19,59 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TREND_UP | 2 | 4 | 4 | 25,00% | 0,41 | -0,49R | €-19,59 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | ALT_ROTATION_UP | 2 | 1 | 1 | 100,00% | ∞ | 1,36R | €13,57 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_UP | 2 | 3 | 3 | 0,00% | 0,00 | -1,11R | €-33,29 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | ALT_ROTATION_DOWN | 2 | 1 | 1 | 100,00% | ∞ | 1,36R | €13,64 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TREND_UP | 4 | 8 | 8 | 12,50% | 0,18 | -0,77R | €-61,87 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | ALT_ROTATION_DOWN | 2 | 1 | 1 | 100,00% | ∞ | 1,36R | €13,64 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | ALT_ROTATION_UP | 2 | 1 | 1 | 100,00% | ∞ | 1,36R | €13,57 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_UP | 4 | 6 | 6 | 0,00% | 0,00 | -1,08R | €-64,56 |
| SHADOW_4H_WIDE | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_4H_WIDE | ALT_ROTATION_UP | 1 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_4H_WIDE | RANGE | 3 | 14 | 14 | 21,43% | 0,74 | -0,21R | €-29,68 |
| SHADOW_4H_WIDE | TRANSITION | 4 | 6 | 6 | 16,67% | 0,55 | -0,38R | €-22,88 |
| SHADOW_4H_WIDE | TREND_UP | 5 | 10 | 10 | 40,00% | 1,81 | 0,50R | €49,91 |
| SHADOW_4H_WIDE | TREND_UP_HIGH_VOL | 4 | 4 | 4 | 0,00% | 0,00 | -1,01R | €-40,53 |
| SHADOW_BOLLINGER_MR_1H | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BOLLINGER_MR_1H | ALT_ROTATION_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,02R | €-20,30 |
| SHADOW_BOLLINGER_MR_1H | RANGE | 0 | 7 | 7 | 42,86% | 0,98 | -0,01R | €-0,83 |
| SHADOW_BOLLINGER_MR_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_BOLLINGER_MR_1H | TRANSITION | 0 | 3 | 3 | 33,33% | 0,71 | -0,20R | €-6,14 |
| SHADOW_BOLLINGER_MR_1H | TREND_UP | 3 | 8 | 8 | 37,50% | 0,77 | -0,16R | €-12,56 |
| SHADOW_BOLLINGER_MR_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,31 | 0,17R | €3,31 |
| SHADOW_BTC_ADAPTIVE_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_BTC_ADAPTIVE_1H | TREND_UP_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_ADAPTIVE_4H | TREND_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_BOLLINGER_1H | RANGE | 0 | 1 | 1 | 100,00% | ∞ | 1,37R | €13,67 |
| SHADOW_BTC_BOLLINGER_1H | TREND_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_BOLLINGER_4H | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_DONCHIAN_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,12R | €-11,25 |
| SHADOW_BTC_DONCHIAN_1H | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -1,12R | €-11,25 |
| SHADOW_BTC_DONCHIAN_1H | TREND_UP_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_DONCHIAN_4H | TREND_UP_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_EMA_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_BTC_EMA_1H | TREND_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_EMA_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,70 | 0,39R | €7,78 |
| SHADOW_BTC_EMA_4H | TREND_UP_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_ADAPTIVE | ALT_ROTATION_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 1,89R | €18,95 |
| SHADOW_COMBO_ADAPTIVE | ALT_ROTATION_UP | 0 | 4 | 4 | 50,00% | 1,87 | 0,44R | €17,68 |
| SHADOW_COMBO_ADAPTIVE | RANGE | 1 | 11 | 11 | 27,27% | 0,68 | -0,26R | €-28,32 |
| SHADOW_COMBO_ADAPTIVE | RANGE_HIGH_VOL | 1 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE | TRANSITION | 2 | 15 | 15 | 53,33% | 2,13 | 0,55R | €82,64 |
| SHADOW_COMBO_ADAPTIVE | TREND_UP | 4 | 24 | 24 | 54,17% | 2,22 | 0,58R | €140,19 |
| SHADOW_COMBO_ADAPTIVE | TREND_UP_HIGH_VOL | 5 | 7 | 7 | 28,57% | 0,74 | -0,19R | €-13,44 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | ALT_ROTATION_UP | 1 | 1 | 1 | 100,00% | ∞ | 1,89R | €18,89 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_UP | 4 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_UP_HIGH_VOL | 2 | 4 | 4 | 25,00% | 0,62 | -0,30R | €-11,93 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | ALT_ROTATION_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 1,89R | €18,95 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | ALT_ROTATION_UP | 0 | 5 | 5 | 40,00% | 1,21 | 0,13R | €6,57 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE_HIGH_VOL | 1 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,91R | €19,12 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_UP | 4 | 16 | 16 | 56,25% | 2,47 | 0,66R | €105,30 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_UP_HIGH_VOL | 5 | 9 | 9 | 22,22% | 0,52 | -0,39R | €-35,51 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | ALT_ROTATION_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 1,89R | €18,95 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | ALT_ROTATION_UP | 1 | 1 | 1 | 100,00% | ∞ | 1,89R | €18,89 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_UP | 5 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,16 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_UP_HIGH_VOL | 2 | 5 | 5 | 20,00% | 0,46 | -0,46R | €-23,04 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TREND_UP | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TREND_UP | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_UP | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TREND_UP | 6 | 2 | 2 | 50,00% | 1,86 | 0,44R | €8,73 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TREND_UP_HIGH_VOL | 3 | 5 | 5 | 20,00% | 0,46 | -0,46R | €-23,04 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_UP | 4 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | TREND_UP | 3 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,26 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | TREND_UP_HIGH_VOL | 1 | 3 | 3 | 0,00% | 0,00 | -1,05R | €-31,38 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | ALT_ROTATION_UP | 4 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | TREND_UP | 3 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,26 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | TREND_UP_HIGH_VOL | 1 | 3 | 3 | 0,00% | 0,00 | -1,05R | €-31,38 |
| SHADOW_COMBO_MEAN_REVERSION | RANGE | 0 | 4 | 4 | 75,00% | 4,46 | 0,88R | €35,25 |
| SHADOW_COMBO_MEAN_REVERSION | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,94 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_UP | 0 | 2 | 2 | 50,00% | 1,50 | 0,25R | €5,04 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,85 |
| SHADOW_COMBO_SCANNER | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_SCANNER | ALT_ROTATION_UP | 0 | 3 | 3 | 66,67% | 4,32 | 1,12R | €33,60 |
| SHADOW_COMBO_SCANNER | RANGE | 0 | 2 | 2 | 50,00% | 2,10 | 0,57R | €11,44 |
| SHADOW_COMBO_SCANNER | RANGE_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_SCANNER | TRANSITION | 1 | 11 | 11 | 36,36% | 1,20 | 0,13R | €14,31 |
| SHADOW_COMBO_SCANNER | TREND_UP | 1 | 18 | 18 | 50,00% | 2,05 | 0,55R | €99,87 |
| SHADOW_COMBO_SCANNER | TREND_UP_HIGH_VOL | 4 | 5 | 5 | 40,00% | 1,37 | 0,23R | €11,57 |
| SHADOW_COMBO_TREND | ALT_ROTATION_DOWN | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_TREND | ALT_ROTATION_UP | 1 | 2 | 2 | 50,00% | 2,16 | 0,59R | €11,73 |
| SHADOW_COMBO_TREND | RANGE | 0 | 8 | 8 | 12,50% | 0,29 | -0,67R | €-53,33 |
| SHADOW_COMBO_TREND | RANGE_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_TREND | TRANSITION | 2 | 13 | 13 | 46,15% | 1,77 | 0,44R | €56,72 |
| SHADOW_COMBO_TREND | TREND_UP | 3 | 20 | 20 | 40,00% | 1,38 | 0,24R | €47,57 |
| SHADOW_COMBO_TREND | TREND_UP_HIGH_VOL | 4 | 7 | 7 | 28,57% | 0,82 | -0,13R | €-9,36 |
| SHADOW_DOGE_DONCHIAN_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,12R | €-11,25 |
| SHADOW_DOGE_EMA_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_DONCHIAN_1H | ALT_ROTATION_DOWN | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_DONCHIAN_1H | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_DONCHIAN_1H | RANGE | 0 | 8 | 8 | 12,50% | 0,32 | -0,64R | €-51,15 |
| SHADOW_DONCHIAN_1H | RANGE_HIGH_VOL | 1 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_DONCHIAN_1H | TRANSITION | 1 | 6 | 6 | 16,67% | 0,45 | -0,48R | €-28,95 |
| SHADOW_DONCHIAN_1H | TREND_UP | 0 | 11 | 11 | 45,45% | 1,89 | 0,53R | €57,82 |
| SHADOW_DONCHIAN_1H | TREND_UP_HIGH_VOL | 4 | 2 | 2 | 50,00% | 2,22 | 0,66R | €13,17 |
| SHADOW_EMA_TREND_1H | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_EMA_TREND_1H | ALT_ROTATION_UP | 1 | 2 | 2 | 50,00% | 2,16 | 0,59R | €11,73 |
| SHADOW_EMA_TREND_1H | RANGE | 1 | 9 | 9 | 11,11% | 0,29 | -0,59R | €-53,03 |
| SHADOW_EMA_TREND_1H | RANGE_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_EMA_TREND_1H | TRANSITION | 2 | 13 | 13 | 46,15% | 1,77 | 0,44R | €56,70 |
| SHADOW_EMA_TREND_1H | TREND_UP | 2 | 26 | 26 | 34,62% | 1,15 | 0,10R | €25,74 |
| SHADOW_EMA_TREND_1H | TREND_UP_HIGH_VOL | 5 | 6 | 6 | 33,33% | 1,04 | 0,03R | €1,64 |
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
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TREND_UP | 5 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,23 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TREND_UP | 6 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,23 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TREND_UP | 6 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,23 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | TREND_UP | 6 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,23 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TREND_UP | 6 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,09 |
| SHADOW_MASTER_ADAPTIVE_V1 | TREND_UP | 6 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,23 |
| Forza relativa 1H V1 | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| Forza relativa 1H V1 | ALT_ROTATION_UP | 1 | 11 | 11 | 27,27% | 0,77 | -0,18R | €-19,81 |
| Forza relativa 1H V1 | RANGE | 0 | 20 | 20 | 20,00% | 0,55 | -0,36R | €-71,11 |
| Forza relativa 1H V1 | RANGE_HIGH_VOL | 1 | 2 | 2 | 0,00% | 0,00 | -1,02R | €-20,33 |
| Forza relativa 1H V1 | TRANSITION | 1 | 12 | 12 | 50,00% | 2,12 | 0,57R | €68,69 |
| Forza relativa 1H V1 | TREND_UP | 8 | 25 | 25 | 40,00% | 1,50 | 0,29R | €72,64 |
| Forza relativa 1H V1 | TREND_UP_HIGH_VOL | 1 | 8 | 8 | 12,50% | 0,30 | -0,64R | €-51,15 |
| Forza relativa 1H V2 | ALT_ROTATION_UP | 1 | 1 | 1 | 100,00% | ∞ | 2,10R | €21,00 |
| Forza relativa 1H V2 | RANGE | 1 | 2 | 2 | 50,00% | 2,16 | 0,59R | €11,72 |
| Forza relativa 1H V2 | TRANSITION | 2 | 8 | 8 | 37,50% | 1,26 | 0,17R | €13,67 |
| Forza relativa 1H V2 | TREND_UP | 2 | 8 | 7 | 62,50% | 3,60 | 0,99R | €78,93 |
| Forza relativa 1H V2 | TREND_UP_HIGH_VOL | 0 | 4 | 3 | 0,00% | 0,00 | -1,04R | €-41,60 |
| SHADOW_SCANNER_BOTTOM5_SHORT | ALT_ROTATION_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 1,89R | €18,95 |
| SHADOW_SCANNER_BOTTOM5_SHORT | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| SHADOW_SCANNER_BOTTOM5_SHORT | RANGE | 0 | 7 | 7 | 0,00% | 0,00 | -1,08R | €-75,76 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TRANSITION | 2 | 10 | 10 | 40,00% | 1,37 | 0,20R | €20,38 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP | 2 | 5 | 5 | 0,00% | 0,00 | -0,62R | €-30,77 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP_HIGH_VOL | 1 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,24 |
| SHADOW_SCANNER_TOP5_BTC | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC | ALT_ROTATION_UP | 0 | 4 | 4 | 50,00% | 2,12 | 0,58R | €23,08 |
| SHADOW_SCANNER_TOP5_BTC | RANGE | 0 | 5 | 5 | 60,00% | 5,82 | 1,06R | €53,24 |
| SHADOW_SCANNER_TOP5_BTC | RANGE_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC | TRANSITION | 0 | 11 | 11 | 36,36% | 1,20 | 0,13R | €14,31 |
| SHADOW_SCANNER_TOP5_BTC | TREND_UP | 1 | 17 | 17 | 47,06% | 1,84 | 0,47R | €79,16 |
| SHADOW_SCANNER_TOP5_BTC | TREND_UP_HIGH_VOL | 4 | 5 | 5 | 40,00% | 1,37 | 0,23R | €11,57 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TREND_UP_HIGH_VOL | 4 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_UP_HIGH_VOL | 4 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_UP | 2 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,79 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_UP | 2 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,79 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_UP_HIGH_VOL | 5 | 4 | 4 | 25,00% | 0,67 | -0,26R | €-10,30 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | ALT_ROTATION_UP | 4 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_UP | 1 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,09 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_UP_HIGH_VOL | 1 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | ALT_ROTATION_UP | 4 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_UP | 1 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,09 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_UP_HIGH_VOL | 1 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_LONG | ALT_ROTATION_DOWN | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_LONG | ALT_ROTATION_UP | 0 | 5 | 5 | 40,00% | 1,24 | 0,15R | €7,55 |
| SHADOW_SCANNER_TOP5_LONG | RANGE | 0 | 6 | 6 | 66,67% | 7,07 | 1,12R | €67,10 |
| SHADOW_SCANNER_TOP5_LONG | RANGE_HIGH_VOL | 1 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_LONG | TRANSITION | 0 | 11 | 11 | 36,36% | 1,09 | 0,06R | €6,31 |
| SHADOW_SCANNER_TOP5_LONG | TREND_UP | 2 | 25 | 25 | 52,00% | 2,00 | 0,51R | €127,49 |
| SHADOW_SCANNER_TOP5_LONG | TREND_UP_HIGH_VOL | 3 | 6 | 6 | 50,00% | 1,83 | 0,44R | €26,30 |
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

Generato: 2026-07-21T20:08:41+00:00

> Motore esclusivamente osservativo e Paper-only. Non modifica le uscite reali. I confronti escludono il funding sia dall'uscita originale sia dalle varianti.

## Stato operativo

- Gruppi di trade ancora monitorati: **255**
- Scenari virtuali ancora attivi: **3082**
- Gruppi in attesa dell'uscita originale: **168**
- Gruppi con originale chiuso ma Shadow ancora attive: **87**
- Confronti completati: **5125**

## Classifica osservativa complessiva

| Scenario | Campione completo | Campione totale | Δ medio vs originale | Migliora | Troppo presto | Troppo tardi | Stato dati |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| GB20_R050 | 232 | 278 | +€6,27 | 46,0% | 70 | 0 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R050 | 232 | 278 | +€4,23 | 43,9% | 69 | 7 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R050 | 232 | 278 | +€2,21 | 42,8% | 70 | 9 | READY_FOR_BLOCK4_EVALUATION |
| TP_R050 | 232 | 278 | +€1,31 | 42,8% | 79 | 0 | READY_FOR_BLOCK4_EVALUATION |
| GB20_R100 | 227 | 273 | +€5,00 | 42,1% | 58 | 3 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R100 | 227 | 273 | +€2,95 | 38,8% | 58 | 12 | READY_FOR_BLOCK4_EVALUATION |
| TP_R100 | 227 | 273 | +€2,90 | 39,9% | 64 | 3 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R100 | 227 | 273 | +€0,84 | 40,7% | 44 | 19 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R050 | 222 | 268 | +€0,24 | 42,9% | 66 | 7 | READY_FOR_BLOCK4_EVALUATION |
| TIME_6H | 220 | 271 | €-2,98 | 48,7% | 67 | 12 | READY_FOR_BLOCK4_EVALUATION |
| TIME_12H | 213 | 264 | +€1,91 | 37,5% | 31 | 40 | READY_FOR_BLOCK4_EVALUATION |
| TP_R150 | 209 | 255 | +€1,64 | 32,5% | 28 | 20 | READY_FOR_BLOCK4_EVALUATION |
| ATR15_R100 | 207 | 253 | €-4,88 | 29,6% | 14 | 57 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R100 | 196 | 242 | +€1,84 | 40,5% | 22 | 25 | READY_FOR_BLOCK4_EVALUATION |
| BE_R050 | 195 | 241 | €-8,53 | 29,5% | 48 | 27 | READY_FOR_BLOCK4_EVALUATION |
| TP_R200 | 192 | 238 | +€6,02 | 38,2% | 12 | 23 | READY_FOR_BLOCK4_EVALUATION |
| ATR20_R100 | 187 | 233 | €-6,56 | 28,3% | 10 | 49 | READY_FOR_BLOCK4_EVALUATION |
| TIME_24H | 172 | 223 | €-0,67 | 35,0% | 14 | 36 | READY_FOR_BLOCK4_EVALUATION |
| ATR30_R100 | 171 | 217 | €-12,42 | 24,4% | 7 | 48 | READY_FOR_BLOCK4_EVALUATION |
| BE_R100 | 171 | 216 | €-12,83 | 24,1% | 6 | 49 | READY_FOR_BLOCK4_EVALUATION |

## Come leggere il controllo

- **EARLIER_BETTER**: la variante è uscita prima e ha conservato più profitto.
- **TOO_EARLY**: la variante è uscita prima ma ha tagliato un movimento migliore.
- **LATER_BETTER**: la variante ha continuato dopo l'uscita originale e ha guadagnato di più.
- **TOO_LATE**: la variante è rimasta aperta più a lungo e ha peggiorato il risultato.

## Limiti e protezioni

Le regole Shadow mantengono entrata, quantità, commissioni, stop protettivo iniziale e liquidazione. Le ambiguità all'interno della stessa candela vengono risolte scegliendo l'esito peggiore. Le posizioni già aperte al momento dell'installazione sono marcate come campione parziale e non saranno utilizzate dal futuro Blocco 4 come prova piena.

# Blocco 4 — Valutazione statistica Shadow

Generato: 2026-07-21T20:08:41+00:00

> Modulo esclusivamente valutativo. Non modifica strategie, uscite, posizioni o capitale. Le candidature vengono consegnate al futuro Blocco 5, senza applicazione automatica.

## Stato

- Risultati Block 3 disponibili: **5125**
- Valutazioni prodotte: **2986**
- Candidature al Blocco 5: **0**
- Mutazioni create automaticamente: **0**

## Classifica complessiva

| Scenario | Campione pieno | Δ medio (R) | Mediana (R) | CI bootstrap basso | Migliora | Score | Stato |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| TIME_24H | 6 | 0,997 | 1,104 | 0,180 | 66,7% | 74,1 | INSUFFICIENT_DATA |
| TP_R200 | 186 | 0,196 | 0,000 | 0,103 | 40,9% | 72,7 | VALIDATING |
| GB40_R050 | 226 | 0,113 | 0,000 | 0,006 | 44,2% | 70,1 | VALIDATING |
| GB20_R050 | 226 | 0,191 | 0,000 | 0,087 | 47,3% | 70,0 | VALIDATING |
| GB30_R050 | 226 | 0,153 | 0,000 | 0,046 | 44,7% | 70,0 | VALIDATING |
| GB20_R100 | 221 | 0,138 | 0,000 | 0,053 | 43,0% | 69,5 | VALIDATING |
| GB30_R100 | 221 | 0,103 | 0,000 | 0,029 | 39,4% | 69,5 | VALIDATING |
| GB50_R100 | 190 | 0,116 | 0,000 | 0,049 | 42,6% | 69,2 | VALIDATING |
| TP_R150 | 203 | 0,098 | 0,000 | 0,022 | 34,0% | 69,0 | VALIDATING |
| TIME_12H | 207 | 0,072 | 0,000 | 0,006 | 38,6% | 68,9 | VALIDATING |
| TP_R050 | 226 | 0,096 | 0,000 | -0,008 | 43,4% | 68,9 | VALIDATING |
| GB50_R050 | 216 | 0,079 | 0,000 | -0,022 | 44,9% | 66,5 | VALIDATING |
| TP_R100 | 221 | 0,103 | 0,000 | 0,022 | 39,8% | 65,6 | VALIDATING |
| GB40_R100 | 221 | 0,066 | 0,000 | -0,008 | 41,6% | 64,4 | VALIDATING |
| TP_R200 | 6 | 0,472 | 0,250 | -0,017 | 50,0% | 58,7 | INSUFFICIENT_DATA |
| TIME_6H | 214 | 0,012 | 0,036 | -0,089 | 54,7% | 56,1 | VALIDATING |
| BE_R050 | 189 | -0,055 | 0,000 | -0,183 | 34,9% | 39,0 | VALIDATING |
| ATR15_R100 | 201 | -0,030 | 0,000 | -0,081 | 29,9% | 37,9 | VALIDATING |
| TIME_24H | 166 | -0,028 | 0,000 | -0,155 | 34,3% | 34,9 | VALIDATING |
| ATR20_R100 | 181 | -0,074 | 0,000 | -0,147 | 28,2% | 31,8 | UNDERPERFORMING |

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

Generato: 2026-07-21T20:08:34+00:00

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
| DOWN_10 | 117 | 2 | 30993.26 |
| DOWN_20 | 117 | 3 | 61926.52 |
| DOWN_30 | 117 | 4 | 92814.40 |
| DOWN_40 | 117 | 32 | 116329.30 |
| UP_10 | 46 | 0 | 8110.37 |
| UP_20 | 46 | 0 | 16220.74 |
| UP_30 | 46 | 6 | 24414.48 |
| UP_40 | 46 | 28 | 28964.21 |

## Modello di esecuzione

Se una candela di cascata attraversa nello stesso intervallo sia lo stop sia il prezzo di liquidazione, il Paper usa il caso peggiore e registra una liquidazione intrabar. Gli stop in gap o in regime di stress ricevono slippage aggiuntivo.

## Requisiti prima del live futures

- modalità ISOLATED obbligatoria;
- stop nativo sull'exchange;
- conferma dello stop prima di accettare la posizione;
- cross margin vietato.

# Blocco 5 — Candidati evolutivi controllati

Generato: 2026-07-21T20:08:12+00:00

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

Generato: 2026-07-21T20:08:44+00:00

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

Generato: 2026-07-21T20:08:44+00:00

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

Generato: 2026-07-21T20:08:44+00:00

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

Generato: 2026-07-21T20:08:44+00:00

> Paper-only. La memoria può bloccare soltanto una futura proposta Block 5 classificata AVOID; non modifica strategie esistenti.

## Stato

- Strategie/portafogli valutati: **69**
- Hall of Fame: **2**
- Memorie genetiche: **0**
- Firme bloccate: **0**
- Azioni automatiche e live: **0**

## Hall of Fame

| Rank | Strategia | Stato | Score | Grade | Trade | PF | Expectancy R | DD R |
| ---: | --- | --- | ---: | --- | ---: | ---: | ---: | ---: |
| 1 | SHADOW_1H_FAST_V3 | BASELINE | 8.7 | E | 41 | 0.99 | -0.003 | 5.36 |
| 2 | SHADOW_1H_FAST | BASELINE | 6.5 | E | 49 | 0.92 | -0.036 | 11.24 |

## Memoria genetica

| Scope | Famiglia | Mutazione | Target | Stato | Score | Prove | Coppie | Blocco |
| --- | --- | --- | --- | --- | ---: | ---: | ---: | --- |
| — | — | Nessuna candidata ancora creata | — | INSUFFICIENT | 0 | 0 | 0 | NO |

## Sicurezza

- Nessuna strategia, posizione o promozione esistente viene modificata.
- Nessuna mutazione, promozione, pensionamento o rollback automatico.
- Nessun effetto live e nessun ordine reale.

# Blocco 10 — Regime Fitness e specializzazione

Generato: 2026-07-21T20:08:44+00:00

> Paper-only e advisory. Il blocco misura quali strategie funzionano nei diversi regimi, ma non cambia automaticamente strategia o posizione.

## Stato

- Regime corrente: **RANGE**
- Righe di performance: **264**
- Strategie preferite nel regime corrente: **0**
- Strategie da evitare nel regime corrente: **0**
- Memorie contestuali: **132**
- Routing automatico: **NO**

## Classifica del regime corrente

| Rank | Portafoglio | Famiglia | Stato | Fitness | Trade | PF | Expectancy R | DD R |
| ---: | --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| 1 | SHADOW_DOGE_DONCHIAN_1H | shadow-doge-donchian-1h | INSUFFICIENT | 80.4 | 1 | 99.00 | 0.524 | 0.00 |
| 2 | SHADOW_BTC_BOLLINGER_1H | shadow-btc-bollinger-1h | INSUFFICIENT | 80.4 | 1 | 99.00 | 1.374 | 0.00 |
| 3 | SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | shadow-scanner-top5-btc-runner25-v1 | INSUFFICIENT | 80.4 | 1 | 99.00 | 0.962 | 0.00 |
| 4 | SHADOW_SCANNER_TOP5_BTC_TP3_V1 | shadow-scanner-top5-btc-tp3-v1 | INSUFFICIENT | 80.4 | 1 | 99.00 | 0.962 | 0.00 |
| 5 | SHADOW_COMBO_ADAPTIVE | shadow-combo-adaptive | OBSERVING | 79.8 | 16 | 2.60 | 0.436 | 1.10 |
| 6 | SHADOW_ETH_BOLLINGER_1H | shadow-eth-bollinger-1h | INSUFFICIENT | 76.6 | 1 | 99.00 | 0.309 | 0.00 |
| 7 | SHADOW_COMBO_MEAN_REVERSION | shadow-combo-mean-reversion | INSUFFICIENT | 75.5 | 5 | 4.40 | 0.709 | 1.02 |
| 8 | SHADOW_SCANNER_TOP5_LONG | shadow-scanner-top5-long | OBSERVING | 74.8 | 18 | 2.28 | 0.453 | 4.17 |
| 9 | SHADOW_SCANNER_TOP5_BTC | shadow-scanner-top5-btc | OBSERVING | 72.0 | 15 | 2.06 | 0.375 | 3.09 |
| 10 | SHADOW_1H_FAST_V2 | shadow-1h-fast-v2 | INSUFFICIENT | 70.6 | 2 | 11.45 | 0.628 | 0.12 |

## Sicurezza

- Il regime viene assegnato usando solo l'ultimo record noto prima dell'entrata del trade.
- Nessun uso di dati futuri per classificare il trade.
- Il Candidate Regime Gate è advisory per impostazione predefinita.
- Nessun cambio automatico di MASTER, posizione o live.

# Blocco 11 — Collegamento protetto al live

Generato: 2026-07-21T20:08:44+00:00

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

Generato: 2026-07-21T20:08:34+00:00

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
