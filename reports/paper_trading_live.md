# Paper trading automatico KuCoin

Generato: 2026-07-24T17:53:54+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-07-24T17:53:25+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-07-24T17:53:25+00:00 | 2026-07-24T17:53:26+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-07-24T17:30:00+00:00 | 2026-07-24T17:30:00+00:00 | 8,5 min | 25,0 min | OK |
| 60m | 12 | 2026-07-24T16:00:00+00:00 | 2026-07-24T16:00:00+00:00 | 53,5 min | 45,0 min | STALE_CANDLE |
| 240m | 12 | 2026-07-24T12:00:00+00:00 | 2026-07-24T12:00:00+00:00 | 1,89 h | 1,00 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | DOGE | 240m | SHORT | -9,11 | 6,00 | 0,00 | STALE_CANDLE | 1,89 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 113.5 minuti; tolleranza 60 minuti. |
| Principale 4H | AKE | 240m | LONG | 7,75 | 6,00 | 0,00 | STALE_CANDLE | 1,89 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 113.5 minuti; tolleranza 60 minuti. |
| Principale 4H | BANK | 240m | LONG | 7,75 | 6,00 | 0,00 | STALE_CANDLE | 1,89 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 113.5 minuti; tolleranza 60 minuti. |
| Principale 4H | HYPE | 240m | SHORT | -7,57 | 6,00 | 0,00 | STALE_CANDLE | 1,89 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 113.5 minuti; tolleranza 60 minuti. |
| Principale 4H | SOL | 240m | SHORT | -7,38 | 6,00 | 0,00 | STALE_CANDLE | 1,89 h | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 113.5 minuti; tolleranza 60 minuti. |
| Principale 4H | ZEC | 240m | SHORT | -6,15 | 6,00 | 0,00 | STALE_CANDLE | 1,89 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 113.5 minuti; tolleranza 60 minuti. |
| Principale 4H | RIF | 240m | SHORT | -4,75 | 6,00 | 1,25 | STALE_CANDLE | 1,89 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 113.5 minuti; tolleranza 60 minuti. |
| Principale 4H | PEPE | 240m | SHORT | -4,33 | 6,00 | 1,67 | STALE_CANDLE | 1,89 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 113.5 minuti; tolleranza 60 minuti. |
| Principale 4H | XRP | 240m | SHORT | -3,51 | 6,00 | 2,49 | STALE_CANDLE | 1,89 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 113.5 minuti; tolleranza 60 minuti. |
| Principale 4H | BTC | 240m | SHORT | -3,00 | 6,00 | 3,00 | STALE_CANDLE | 1,89 h | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 113.5 minuti; tolleranza 60 minuti. |
| Principale 4H | ADA | 240m | SHORT | -2,86 | 6,00 | 3,14 | STALE_CANDLE | 1,89 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 113.5 minuti; tolleranza 60 minuti. |
| Principale 4H | ETH | 240m | SHORT | -0,31 | 6,00 | 5,69 | STALE_CANDLE | 1,89 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 113.5 minuti; tolleranza 60 minuti. |
| Ampia 4H | DOGE | 240m | SHORT | -9,11 | 5,00 | 0,00 | STALE_CANDLE | 1,89 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 113.5 minuti; tolleranza 60 minuti. |
| Bilanciata 1H V1 | ZEC | 60m | SHORT | -8,50 | 5,00 | 0,00 | STALE_CANDLE | 53,5 min | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 53.5 minuti; tolleranza 45 minuti. |
| Bilanciata 1H V2 | ZEC | 60m | SHORT | -8,50 | 5,50 | 0,00 | STALE_CANDLE | 53,5 min | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 53.5 minuti; tolleranza 45 minuti. |
| Bilanciata 1H V3 Filtered | ZEC | 60m | SHORT | -8,50 | 6,00 | 0,00 | STALE_CANDLE | 53,5 min | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 53.5 minuti; tolleranza 45 minuti. |
| Rapida 1H V1 — madre | ZEC | 60m | SHORT | -8,50 | 4,50 | 0,00 | STALE_CANDLE | 53,5 min | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 53.5 minuti; tolleranza 45 minuti. |
| Rapida V1 — score 6–7,5 | ZEC | 60m | SHORT | -8,50 | 6,00 | 0,00 | STALE_CANDLE | 53,5 min | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 53.5 minuti; tolleranza 45 minuti. |
| Rapida V1 — no HIGH + score <7,5 | ZEC | 60m | SHORT | -8,50 | 4,50 | 0,00 | STALE_CANDLE | 53,5 min | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 53.5 minuti; tolleranza 45 minuti. |
| Rapida V1 — Long + BTC 1–3 + score <7,5 | ZEC | 60m | SHORT | -8,50 | 4,50 | 0,00 | STALE_CANDLE | 53,5 min | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 53.5 minuti; tolleranza 45 minuti. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.950,83 | -0,49% | €-49,17 | €3.000,00 | -1,64% | 4 | 18 | 33,33% | 0,91 | 4,26% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 18 | 505 | CAMPIONE INSUFFICIENTE | 30 (mancano 12) |

- Trade del Principale 4H chiusi: **18**; win rate **33,33%**; profit factor **0,91**.
- Expectancy: **€-2,94** per trade; P&L netto: **€-52,87**; max drawdown: **4,26%**.
- Valutazione: **Servono altri eventi indipendenti prima di trarre conclusioni.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 4 | €9.950,83 | €1.462,87 | €4.388,60 | €148,39 | €5,58 |
| TEST | Scanner Top 5 Long 1H | 3 | €10.691,44 | €1.269,32 | €2.538,64 | €105,45 | €65,19 |
| TEST | Bilanciata 1H V1 | 4 | €10.471,14 | €2.717,92 | €8.153,75 | €50,78 | €140,29 |
| TEST | Scanner Top 5 + forza BTC 1H | 3 | €10.442,85 | €1.331,37 | €2.662,75 | €104,27 | €63,67 |
| TEST | Bilanciata 1H V3 Filtered | 4 | €10.398,71 | €1.661,13 | €4.983,38 | €102,89 | €122,19 |
| TEST | Benchmark Donchian breakout 1H | 3 | €10.307,27 | €2.572,85 | €5.145,70 | €102,30 | €134,35 |
| TEST | Rapida V1 — score 6–7,5 | 3 | €10.301,90 | €4.155,61 | €12.466,82 | €102,32 | €28,94 |
| TEST | Combo Adaptive — madre | 3 | €10.257,14 | €2.757,41 | €5.514,81 | €154,10 | €-4,71 |
| TEST | Forza relativa 1H V2 | 4 | €10.217,50 | €1.846,37 | €3.692,74 | €151,67 | €68,56 |
| TEST | Top 5 + BTC — target pieno 3R | 3 | €10.202,16 | €1.281,05 | €2.562,10 | €100,06 | €62,20 |
| TEST | Rapida V3 — score <7,5 | 4 | €10.190,68 | €3.497,77 | €10.493,31 | €151,43 | €14,77 |
| TEST | Bilanciata 1H V2 | 4 | €10.171,76 | €1.221,60 | €3.664,80 | €100,66 | €70,22 |
| TEST | Rapida 1H V3 Filtered — madre | 4 | €10.160,37 | €2.066,06 | €6.198,19 | €150,82 | €59,40 |
| TEST | Top 5 + BTC — 75% a 2,2R + runner 3R | 3 | €10.155,64 | €1.280,09 | €2.560,17 | €100,06 | €61,92 |
| TEST | Doge Ema 1H | 1 | €10.141,52 | €1.143,65 | €3.430,94 | €50,74 | €-4,66 |
| TEST | Rapida V1 — no HIGH + score <7,5 | 4 | €10.138,00 | €3.475,44 | €10.426,31 | €150,35 | €14,69 |
| TEST | Combo Scanner | 3 | €10.113,65 | €2.776,18 | €5.552,36 | €150,33 | €-4,65 |
| TEST | Rapida V1 — senza PEPE | 4 | €10.103,93 | €2.057,50 | €6.172,50 | €150,26 | €59,10 |
| TEST | Btc Bollinger 1H | 1 | €10.098,42 | €1.402,77 | €4.208,32 | €50,50 | €0,99 |
| TEST | Combo Adaptive — Quality7 | 3 | €10.097,56 | €2.758,10 | €5.516,20 | €99,62 | €61,95 |
| TEST | Sol Donchian 1H | 0 | €10.092,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 4H | 0 | €10.086,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 4H | 0 | €10.084,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Benchmark Bollinger mean reversion 1H | 2 | €10.078,42 | €4.030,03 | €8.060,05 | €96,72 | €13,18 |
| TEST | Rapida V3 — senza ESPORTS | 4 | €10.062,53 | €2.500,00 | €7.500,00 | €98,60 | €95,95 |
| TEST | Top 5 + BTC — Guard + BTC≤3 | 3 | €10.057,79 | €1.285,16 | €2.570,32 | €98,81 | €61,32 |
| TEST | Combo Trend | 3 | €10.054,27 | €622,29 | €1.244,59 | €50,30 | €198,20 |
| TEST | Rapida V3 — no volatilità HIGH | 4 | €10.035,34 | €2.490,98 | €7.472,94 | €98,34 | €95,71 |
| TEST | Top 5 + BTC — BTC≤3 | 3 | €10.029,39 | €1.300,19 | €2.600,39 | €100,07 | €61,15 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €10.028,40 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V2 | 3 | €10.027,01 | €3.914,85 | €11.744,55 | €150,58 | €-44,76 |
| TEST | Eth Bollinger 1H | 0 | €10.015,45 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Top 5 + BTC — BTC 2–3 | 3 | €10.014,62 | €1.299,78 | €2.599,56 | €149,81 | €66,15 |
| TEST | Combo Mean Reversion | 1 | €10.013,71 | €1.998,65 | €3.997,31 | €47,97 | €22,84 |
| TEST | Btc Adaptive 1H | 0 | €10.013,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 1H | 1 | €10.010,70 | €1.150,16 | €3.450,47 | €0,00 | €75,29 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 0 | €10.005,68 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €50 · 15x | 0 | €10.001,47 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V1 — target pieno 2R | 4 | €10.001,44 | €2.488,63 | €7.465,88 | €98,01 | €95,35 |
| TEST | Benchmark trend following EMA 1H | 3 | €10.001,34 | €3.285,79 | €6.571,59 | €99,75 | €60,11 |
| TEST | Scalp RSI Long 25 · €10 · 15x | 0 | €10.000,29 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €10 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €10 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €50 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €50 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · prudente · 5x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · prudente · 5x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €10 · 15x | 0 | €9.999,79 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €50 · 15x | 0 | €9.998,95 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Donchian 1H | 0 | €9.998,75 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €10 · 15x | 0 | €9.998,50 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · prudente · 5x | 0 | €9.996,99 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Ampia 4H | 4 | €9.994,22 | €1.964,72 | €3.929,45 | €149,98 | €12,24 |
| TEST | Scalp RSI Long 15 · €50 · 15x | 0 | €9.992,50 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Donchian 4H | 1 | €9.989,93 | €830,21 | €1.660,43 | €49,74 | €42,84 |
| TEST | Scalp RSI Long 15 · prudente · 5x | 0 | €9.988,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 4H | 1 | €9.986,61 | €761,04 | €1.522,08 | €49,74 | €39,27 |
| TEST | Combo Adaptive — target pieno 3R | 3 | €9.982,70 | €2.798,22 | €5.596,43 | €149,59 | €-4,59 |
| TEST | Combo Adaptive — 75% a 2R + runner 3R | 3 | €9.981,18 | €2.797,77 | €5.595,53 | €99,81 | €56,36 |
| TEST | Btc Donchian 1H | 0 | €9.980,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 0 | €9.976,99 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — Trend/Transition | 2 | €9.975,22 | €964,46 | €1.928,92 | €98,78 | €0,00 |
| TEST | Sol Ema 4H | 1 | €9.971,16 | €862,58 | €1.725,17 | €49,74 | €24,20 |
| TEST | Eth Donchian 1H | 1 | €9.965,52 | €1.299,81 | €3.899,43 | €49,91 | €-14,68 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.964,86 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 1H | 1 | €9.962,53 | €1.153,43 | €3.460,30 | €49,83 | €-1,06 |
| TEST | Combo Adaptive — Quality7 + Regime + parziale 1R | 2 | €9.955,02 | €967,29 | €1.934,58 | €49,61 | €32,88 |
| TEST | Btc Ema 4H | 0 | €9.950,68 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 4H | 0 | €9.950,68 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 4H | 0 | €9.949,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Ema 4H | 0 | €9.947,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — Quality7 + Regime | 2 | €9.932,83 | €1.069,84 | €2.139,69 | €49,61 | €65,61 |
| TEST | Rapida 1H V1 — madre | 4 | €9.931,27 | €2.026,40 | €6.079,20 | €147,42 | €58,02 |
| TEST | Eth Adaptive 1H | 1 | €9.922,86 | €1.146,74 | €3.440,21 | €49,54 | €17,05 |
| TEST | Forza relativa 1H V1 | 4 | €9.917,58 | €1.590,83 | €3.181,66 | €148,45 | €-1,38 |
| TEST | Rapida V1 — Long + BTC 1–3 + score <7,5 | 1 | €9.911,67 | €783,06 | €2.349,19 | €50,00 | €0,00 |
| TEST | Top 5 + BTC — Guard | 3 | €9.893,25 | €1.163,95 | €2.327,90 | €97,72 | €60,32 |
| TEST | Sol Adaptive 1H | 1 | €9.891,15 | €1.144,60 | €3.433,80 | €49,45 | €3,86 |
| TEST | Doge Bollinger 1H | 0 | €9.888,87 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — Long Only | 2 | €9.865,72 | €1.099,22 | €2.198,44 | €98,72 | €0,00 |
| TEST | Global Confluence puro 1H | 1 | €9.859,88 | €1.539,06 | €3.078,12 | €0,00 | €11,80 |
| TEST | Combo Adaptive — parziale 1R | 3 | €9.853,28 | €2.764,95 | €5.529,91 | €147,91 | €-4,53 |
| TEST | Eth Ema 1H | 1 | €9.850,22 | €1.138,34 | €3.415,02 | €49,18 | €16,93 |
| TEST | Sol Bollinger 1H | 1 | €9.843,38 | €1.365,75 | €4.097,24 | €49,17 | €12,45 |
| TEST | Rapida V3 — Long + no HIGH + score <7,5 | 2 | €9.839,67 | €387,39 | €1.162,17 | €97,97 | €11,60 |
| TEST | Scanner Bottom 5 Short 1H | 3 | €9.839,17 | €2.757,78 | €5.515,56 | €48,90 | €61,49 |
| TEST | Master Adaptive Expanded V1 | 3 | €9.837,27 | €1.240,15 | €2.480,31 | €146,90 | €67,27 |
| TEST | Top 5 + BTC — Guard + BTC≤3 + MFE | 3 | €9.830,94 | €1.277,87 | €2.555,74 | €98,22 | €67,60 |
| TEST | Rapida V3 — qualità completa + profit lock | 2 | €9.804,45 | €386,00 | €1.158,01 | €97,62 | €11,56 |
| TEST | Top 5 + BTC — solo MFE | 3 | €9.801,10 | €2.552,34 | €5.104,68 | €100,00 | €64,74 |
| TEST | Master Adaptive V1 | 3 | €9.798,45 | €1.239,48 | €2.478,96 | €146,74 | €71,59 |
| TEST | Master Adaptive No Alt V1 | 3 | €9.798,45 | €1.239,48 | €2.478,96 | €146,74 | €71,59 |
| TEST | Master Adaptive Runner25 V1 | 3 | €9.798,45 | €1.239,48 | €2.478,96 | €146,74 | €71,59 |
| TEST | Rapida V3 — Long Only | 0 | €9.769,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Gb20 V1 | 3 | €9.754,85 | €1.253,25 | €2.506,50 | €97,61 | €37,95 |
| TEST | Top 5 + BTC — Guard + MFE | 3 | €9.719,33 | €1.158,82 | €2.317,64 | €97,39 | €66,83 |
| TEST | Combo Adaptive — MFE Trail esistente | 3 | €9.681,02 | €1.149,02 | €2.298,05 | €96,76 | €0,00 |
| TEST | Master Adaptive Strict3 V1 | 2 | €9.636,25 | €1.086,89 | €2.173,78 | €96,98 | €2,63 |

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
| PRINCIPALE | Principale 4H | Confluenza trend | €9.950,83 | €-52,87 | 18 | 18 | 33,33% | 0,91 | €-2,94 | 4,26% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.691,44 | €627,89 | 30 | 30 | 53,33% | 2,18 | €20,93 | 2,70% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €10.471,14 | €336,34 | 37 | 37 | 51,35% | 1,46 | €9,09 | 2,30% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €10.442,85 | €381,10 | 22 | 22 | 50,00% | 1,96 | €17,32 | 2,01% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €10.398,71 | €279,21 | 33 | 33 | 45,45% | 1,35 | €8,46 | 2,20% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €10.307,27 | €174,63 | 18 | 18 | 50,00% | 1,44 | €9,70 | 2,12% |
| TEST | Rapida V1 — score 6–7,5 | Momentum / breakout | €10.301,90 | €280,44 | 32 | 32 | 43,75% | 1,48 | €8,76 | 2,49% |
| TEST | Combo Adaptive — madre | Combo Adaptive | €10.257,14 | €265,08 | 22 | 22 | 50,00% | 1,78 | €12,05 | 1,31% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €10.217,50 | €151,15 | 33 | 32 | 36,36% | 1,16 | €4,58 | 3,69% |
| TEST | Top 5 + BTC — target pieno 3R | Scanner Top 5 + forza BTC | €10.202,16 | €141,80 | 8 | 8 | 62,50% | 1,87 | €17,72 | 2,33% |
| TEST | Rapida V3 — score <7,5 | Momentum / breakout V3 Filtered | €10.190,68 | €181,81 | 26 | 26 | 42,31% | 1,36 | €6,99 | 2,49% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €10.171,76 | €103,73 | 26 | 24 | 53,85% | 1,19 | €3,99 | 2,75% |
| TEST | Rapida 1H V3 Filtered — madre | Momentum / breakout V3 Filtered | €10.160,37 | €104,29 | 59 | 59 | 35,59% | 1,09 | €1,77 | 2,89% |
| TEST | Top 5 + BTC — 75% a 2,2R + runner 3R | Scanner Top 5 + forza BTC | €10.155,64 | €95,56 | 8 | 8 | 62,50% | 1,59 | €11,95 | 2,33% |
| TEST | Doge Ema 1H | Trend following EMA | €10.141,52 | €148,24 | 7 | 7 | 71,43% | 2,33 | €21,18 | 1,36% |
| TEST | Rapida V1 — no HIGH + score <7,5 | Momentum / breakout | €10.138,00 | €129,17 | 31 | 31 | 41,94% | 1,19 | €4,17 | 2,83% |
| TEST | Combo Scanner | Combo Scanner | €10.113,65 | €121,92 | 24 | 24 | 45,83% | 1,20 | €5,08 | 2,66% |
| TEST | Rapida V1 — senza PEPE | Momentum / breakout | €10.103,93 | €48,13 | 27 | 27 | 37,04% | 1,09 | €1,78 | 2,10% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.098,42 | €99,96 | 2 | 2 | 100,00% | ∞ | €49,98 | 0,54% |
| TEST | Combo Adaptive — Quality7 | Combo Adaptive | €10.097,56 | €38,91 | 7 | 7 | 71,43% | 1,36 | €5,56 | 1,51% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €10.092,12 | €92,12 | 3 | 3 | 66,67% | 21,53 | €30,71 | 0,79% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €10.086,98 | €86,98 | 1 | 1 | 100,00% | ∞ | €86,98 | 0,40% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.084,12 | €84,12 | 1 | 1 | 100,00% | ∞ | €84,12 | 0,30% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €10.078,42 | €70,07 | 28 | 28 | 42,86% | 1,11 | €2,50 | 2,06% |
| TEST | Rapida V3 — senza ESPORTS | Momentum / breakout V3 Filtered | €10.062,53 | €-29,32 | 31 | 31 | 32,26% | 0,96 | €-0,95 | 2,49% |
| TEST | Top 5 + BTC — Guard + BTC≤3 | Scanner Top 5 + forza BTC | €10.057,79 | €-1,60 | 4 | 4 | 50,00% | 0,99 | €-0,40 | 1,64% |
| TEST | Combo Trend | Combo Trend | €10.054,27 | €-143,16 | 26 | 26 | 26,92% | 0,82 | €-5,51 | 3,58% |
| TEST | Rapida V3 — no volatilità HIGH | Momentum / breakout V3 Filtered | €10.035,34 | €-56,28 | 32 | 32 | 34,38% | 0,93 | €-1,76 | 2,96% |
| TEST | Top 5 + BTC — BTC≤3 | Scanner Top 5 + forza BTC | €10.029,39 | €-29,80 | 4 | 4 | 50,00% | 0,73 | €-7,45 | 2,20% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €10.028,40 | €28,40 | 6 | 6 | 33,33% | 1,98 | €4,73 | 0,25% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €10.027,01 | €78,81 | 8 | 7 | 50,00% | 1,64 | €9,85 | 1,69% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €10.015,45 | €15,45 | 1 | 1 | 100,00% | ∞ | €15,45 | 0,51% |
| TEST | Top 5 + BTC — BTC 2–3 | Scanner Top 5 + forza BTC | €10.014,62 | €-49,59 | 3 | 3 | 33,33% | 0,54 | €-16,53 | 2,38% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €10.013,71 | €-6,74 | 14 | 14 | 35,71% | 0,98 | €-0,48 | 2,31% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €10.013,28 | €13,28 | 3 | 3 | 66,67% | 1,24 | €4,43 | 0,89% |
| TEST | Sol Ema 1H | Trend following EMA | €10.010,70 | €-62,66 | 3 | 3 | 33,33% | 0,42 | €-20,89 | 1,67% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €10.005,68 | €5,68 | 6 | 6 | 33,33% | 1,98 | €0,95 | 0,05% |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | €10.001,47 | €1,47 | 5 | 5 | 40,00% | 1,12 | €0,29 | 0,13% |
| TEST | Rapida V1 — target pieno 2R | Momentum / breakout | €10.001,44 | €-89,83 | 28 | 28 | 28,57% | 0,86 | €-3,21 | 2,58% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €10.001,34 | €-54,33 | 18 | 18 | 33,33% | 0,87 | €-3,02 | 2,25% |
| TEST | Scalp RSI Long 25 · €10 · 15x | Inversione RSI estrema 15m | €10.000,29 | €0,29 | 5 | 5 | 40,00% | 1,12 | €0,06 | 0,03% |
| TEST | Scalp RSI Short 85 · €10 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 80 · €10 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 85 · €50 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 80 · €50 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 85 · prudente · 5x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 80 · prudente · 5x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 20 · €10 · 15x | Inversione RSI estrema 15m | €9.999,79 | €-0,21 | 1 | 1 | 0,00% | 0,00 | €-0,21 | 0,01% |
| TEST | Scalp RSI Long 20 · €50 · 15x | Inversione RSI estrema 15m | €9.998,95 | €-1,05 | 1 | 1 | 0,00% | 0,00 | €-1,05 | 0,04% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €9.998,75 | €-1,25 | 4 | 4 | 75,00% | 0,98 | €-0,31 | 0,96% |
| TEST | Scalp RSI Long 15 · €10 · 15x | Inversione RSI estrema 15m | €9.998,50 | €-1,50 | 1 | 1 | 0,00% | 0,00 | €-1,50 | 0,02% |
| TEST | Scalp RSI Long 20 · prudente · 5x | Inversione RSI estrema 15m | €9.996,99 | €-3,01 | 1 | 1 | 0,00% | 0,00 | €-3,01 | 0,11% |
| TEST | Ampia 4H | Confluenza trend | €9.994,22 | €-17,59 | 14 | 14 | 21,43% | 0,96 | €-1,26 | 2,94% |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | €9.992,50 | €-7,50 | 1 | 1 | 0,00% | 0,00 | €-7,50 | 0,11% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €9.989,93 | €-52,00 | 1 | 1 | 0,00% | 0,00 | €-52,00 | 0,60% |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | €9.988,38 | €-11,62 | 1 | 1 | 0,00% | 0,00 | €-11,62 | 0,17% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €9.986,61 | €-51,83 | 1 | 1 | 0,00% | 0,00 | €-51,83 | 0,59% |
| TEST | Combo Adaptive — target pieno 3R | Combo Adaptive | €9.982,70 | €-9,13 | 10 | 10 | 50,00% | 0,96 | €-0,91 | 1,41% |
| TEST | Combo Adaptive — 75% a 2R + runner 3R | Combo Adaptive | €9.981,18 | €-71,80 | 14 | 14 | 42,86% | 0,82 | €-5,13 | 2,12% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €9.980,62 | €-19,38 | 4 | 4 | 50,00% | 0,82 | €-4,84 | 1,49% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €9.976,99 | €-23,01 | 5 | 5 | 20,00% | 0,20 | €-4,60 | 0,37% |
| TEST | Combo Adaptive — Trend/Transition | Combo Adaptive | €9.975,22 | €-23,53 | 10 | 10 | 50,00% | 0,92 | €-2,35 | 2,18% |
| TEST | Sol Ema 4H | Trend following EMA | €9.971,16 | €-52,00 | 1 | 1 | 0,00% | 0,00 | €-52,00 | 0,56% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.965,52 | €-17,46 | 3 | 3 | 33,33% | 0,84 | €-5,82 | 1,38% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.964,86 | €-35,14 | 6 | 6 | 16,67% | 0,18 | €-5,86 | 0,36% |
| TEST | Btc Ema 1H | Trend following EMA | €9.962,53 | €-34,33 | 5 | 5 | 40,00% | 0,79 | €-6,87 | 1,56% |
| TEST | Combo Adaptive — Quality7 + Regime + parziale 1R | Combo Adaptive | €9.955,02 | €-109,26 | 4 | 4 | 25,00% | 0,32 | €-27,31 | 1,95% |
| TEST | Btc Ema 4H | Trend following EMA | €9.950,68 | €-49,32 | 1 | 1 | 0,00% | 0,00 | €-49,32 | 0,96% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €9.950,68 | €-49,32 | 1 | 1 | 0,00% | 0,00 | €-49,32 | 0,96% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €9.949,62 | €-50,38 | 1 | 1 | 0,00% | 0,00 | €-50,38 | 0,74% |
| TEST | Eth Ema 4H | Trend following EMA | €9.947,12 | €-52,88 | 1 | 1 | 0,00% | 0,00 | €-52,88 | 0,68% |
| TEST | Combo Adaptive — Quality7 + Regime | Combo Adaptive | €9.932,83 | €-131,50 | 4 | 4 | 25,00% | 0,18 | €-32,87 | 1,95% |
| TEST | Rapida 1H V1 — madre | Momentum / breakout | €9.931,27 | €-123,50 | 67 | 67 | 32,84% | 0,92 | €-1,84 | 6,76% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.922,86 | €-92,21 | 4 | 4 | 50,00% | 0,16 | €-23,05 | 1,24% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €9.917,58 | €-79,13 | 24 | 24 | 25,00% | 0,82 | €-3,30 | 3,25% |
| TEST | Rapida V1 — Long + BTC 1–3 + score <7,5 | Momentum / breakout | €9.911,67 | €-86,92 | 10 | 10 | 20,00% | 0,63 | €-8,69 | 1,92% |
| TEST | Top 5 + BTC — Guard | Scanner Top 5 + forza BTC | €9.893,25 | €-165,42 | 7 | 7 | 28,57% | 0,41 | €-23,63 | 3,31% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €9.891,15 | €-110,64 | 5 | 5 | 40,00% | 0,38 | €-22,13 | 2,14% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €9.888,87 | €-111,13 | 2 | 2 | 0,00% | 0,00 | €-55,56 | 1,26% |
| TEST | Combo Adaptive — Long Only | Combo Adaptive | €9.865,72 | €-132,59 | 5 | 5 | 20,00% | 0,42 | €-26,52 | 2,34% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.859,88 | €-150,03 | 8 | 8 | 37,50% | 0,45 | €-18,75 | 2,92% |
| TEST | Combo Adaptive — parziale 1R | Combo Adaptive | €9.853,28 | €-138,49 | 12 | 12 | 41,67% | 0,64 | €-11,54 | 2,24% |
| TEST | Eth Ema 1H | Trend following EMA | €9.850,22 | €-164,74 | 6 | 6 | 33,33% | 0,25 | €-27,46 | 1,92% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.843,38 | €-166,62 | 3 | 3 | 0,00% | 0,00 | €-55,54 | 1,79% |
| TEST | Rapida V3 — Long + no HIGH + score <7,5 | Momentum / breakout V3 Filtered | €9.839,67 | €-171,24 | 21 | 21 | 33,33% | 0,72 | €-8,15 | 2,86% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.839,17 | €-218,20 | 23 | 23 | 34,78% | 0,62 | €-9,49 | 5,48% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €9.837,27 | €-227,96 | 7 | 7 | 14,29% | 0,29 | €-32,57 | 2,80% |
| TEST | Top 5 + BTC — Guard + BTC≤3 + MFE | Scanner Top 5 + forza BTC | €9.830,94 | €-235,12 | 13 | 13 | 30,77% | 0,41 | €-18,09 | 2,70% |
| TEST | Rapida V3 — qualità completa + profit lock | Momentum / breakout V3 Filtered | €9.804,45 | €-206,41 | 21 | 21 | 42,86% | 0,68 | €-9,83 | 3,21% |
| TEST | Top 5 + BTC — solo MFE | Scanner Top 5 + forza BTC | €9.801,10 | €-260,88 | 11 | 11 | 27,27% | 0,17 | €-23,72 | 3,88% |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | €9.798,45 | €-271,00 | 5 | 5 | 0,00% | 0,00 | €-54,20 | 3,19% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €9.798,45 | €-271,00 | 5 | 5 | 0,00% | 0,00 | €-54,20 | 3,19% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €9.798,45 | €-271,00 | 5 | 5 | 0,00% | 0,00 | €-54,20 | 3,19% |
| TEST | Rapida V3 — Long Only | Momentum / breakout V3 Filtered | €9.769,04 | €-230,96 | 24 | 24 | 25,00% | 0,65 | €-9,62 | 3,31% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €9.754,85 | €-281,60 | 30 | 30 | 53,33% | 0,56 | €-9,39 | 4,16% |
| TEST | Top 5 + BTC — Guard + MFE | Scanner Top 5 + forza BTC | €9.719,33 | €-346,25 | 16 | 16 | 25,00% | 0,32 | €-21,64 | 3,87% |
| TEST | Combo Adaptive — MFE Trail esistente | Combo Adaptive | €9.681,02 | €-317,53 | 27 | 27 | 25,93% | 0,45 | €-11,76 | 4,11% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €9.636,25 | €-365,07 | 14 | 14 | 21,43% | 0,44 | €-26,08 | 4,66% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | LAB | SHORT | Confluenza trend | 240m | 3,0x | 0,17841 | 0,17841 | 0,17841 | 0,23699 | 0,13559 | €136,26 | €408,77 | €0,00 | €-0,00 |
| Principale 4H | SUI | LONG | Confluenza trend | 240m | 3,0x | 0,76296 | 0,76296 | 0,73998 | 0,51245 | 0,80891 | €547,52 | €1.642,56 | €49,46 | €0,00 |
| Principale 4H | ONDO | LONG | Confluenza trend | 240m | 3,0x | 0,40344 | 0,40344 | 0,37762 | 0,27098 | 0,45509 | €254,70 | €764,09 | €48,91 | €0,00 |
| Principale 4H | DOGE | SHORT | Confluenza trend | 240m | 3,0x | 0,06940 | 0,06915 | 0,07160 | 0,09218 | 0,06498 | €524,39 | €1.573,18 | €50,01 | €5,58 |
| Bilanciata 1H V1 | ONDO | LONG | Confluenza trend | 60m | 3,0x | 0,39694 | 0,39694 | 0,38539 | 0,26661 | 0,42004 | €581,76 | €1.745,29 | €50,78 | €0,00 |
| Bilanciata 1H V1 | DOGE | SHORT | Confluenza trend | 60m | 3,0x | 0,06953 | 0,06915 | 0,06939 | 0,09235 | 0,06717 | €1.013,54 | €3.040,62 | €0,00 | €16,45 |
| Bilanciata 1H V1 | ADA | SHORT | Confluenza trend | 60m | 3,0x | 0,16703 | 0,16360 | 0,16501 | 0,22187 | 0,16112 | €978,72 | €2.936,17 | €0,00 | €60,29 |
| Bilanciata 1H V1 | BANK | LONG | Confluenza trend | 60m | 3,0x | 0,26033 | 0,29866 | 0,27587 | 0,17486 | 0,32281 | €143,89 | €431,67 | €0,00 | €63,55 |
| Bilanciata 1H V2 | ESPORTS | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,02164 | 0,02164 | 0,02164 | 0,02874 | 0,01644 | €138,69 | €416,06 | €0,00 | €-0,00 |
| Bilanciata 1H V2 | AKE | LONG | Confluenza trend V2 | 60m | 3,0x | 0,00271 | 0,00314 | 0,00277 | 0,00182 | 0,00336 | €139,38 | €418,14 | €0,00 | €66,73 |
| Bilanciata 1H V2 | BANK | LONG | Confluenza trend V2 | 60m | 3,0x | 0,29967 | 0,29866 | 0,26406 | 0,20128 | 0,37088 | €141,19 | €423,58 | €50,33 | €-1,43 |
| Bilanciata 1H V2 | ZEC | SHORT | Confluenza trend V2 | 60m | 3,0x | 494,80102 | 493,79000 | 505,14655 | 657,26069 | 474,10997 | €802,34 | €2.407,01 | €50,33 | €4,92 |
| Bilanciata 1H V3 Filtered | ESPORTS | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,02126 | 0,02126 | 0,02126 | 0,02823 | 0,01615 | €141,51 | €424,52 | €0,00 | €-0,00 |
| Bilanciata 1H V3 Filtered | ONDO | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,40134 | 0,40134 | 0,38898 | 0,26957 | 0,42605 | €557,59 | €1.672,77 | €51,50 | €0,00 |
| Bilanciata 1H V3 Filtered | ZEC | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 494,80102 | 493,79000 | 505,14655 | 657,26069 | 474,10997 | €819,31 | €2.457,92 | €51,39 | €5,02 |
| Bilanciata 1H V3 Filtered | AKE | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,00247 | 0,00314 | 0,00278 | 0,00166 | 0,00306 | €142,73 | €428,18 | €0,00 | €117,17 |
| Rapida 1H V1 — madre | ONDO | LONG | Momentum / breakout | 60m | 3,0x | 0,39924 | 0,39924 | 0,38995 | 0,26816 | 0,41318 | €708,01 | €2.124,02 | €49,43 | €0,00 |
| Rapida 1H V1 — madre | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00271 | 0,00314 | 0,00283 | 0,00182 | 0,00319 | €139,05 | €417,14 | €0,00 | €66,57 |
| Rapida 1H V1 — madre | BANK | LONG | Momentum / breakout | 60m | 3,0x | 0,29671 | 0,29866 | 0,26700 | 0,19929 | 0,34127 | €161,18 | €483,53 | €48,41 | €3,18 |
| Rapida 1H V1 — madre | ZEC | SHORT | Momentum / breakout | 60m | 3,0x | 491,90160 | 493,79000 | 499,88678 | 653,40929 | 479,92384 | €1.018,17 | €3.054,50 | €49,58 | €-11,73 |
| Rapida V1 — score 6–7,5 | ZEC | SHORT | Momentum / breakout | 60m | 3,0x | 498,39030 | 493,79000 | 496,69649 | 662,02845 | 486,88556 | €1.110,29 | €3.330,88 | €0,00 | €30,75 |
| Rapida V1 — score 6–7,5 | XRP | SHORT | Momentum / breakout | 60m | 3,0x | 1,09458 | 1,08834 | 1,10684 | 1,45397 | 1,07619 | €1.525,19 | €4.575,56 | €51,25 | €26,09 |
| Rapida V1 — score 6–7,5 | BTC | SHORT | Momentum / breakout | 60m | 3,0x | 63750,18741 | 64140,17000 | 64464,18951 | 84681,49895 | 62679,18426 | €1.520,13 | €4.560,38 | €51,08 | €-27,90 |
| Rapida V1 — no HIGH + score <7,5 | ONDO | LONG | Momentum / breakout | 60m | 3,0x | 0,39924 | 0,39924 | 0,38995 | 0,26816 | 0,41318 | €704,39 | €2.113,17 | €49,18 | €0,00 |
| Rapida V1 — no HIGH + score <7,5 | ZEC | SHORT | Momentum / breakout | 60m | 3,0x | 498,39030 | 493,79000 | 496,69649 | 662,02845 | 486,88556 | €1.089,87 | €3.269,62 | €0,00 | €30,18 |
| Rapida V1 — no HIGH + score <7,5 | BTC | SHORT | Momentum / breakout | 60m | 3,0x | 63750,18741 | 64140,17000 | 64464,18951 | 84681,49895 | 62679,18426 | €1.499,07 | €4.497,20 | €50,37 | €-27,51 |
| Rapida V1 — no HIGH + score <7,5 | BANK | LONG | Momentum / breakout | 60m | 3,0x | 0,29223 | 0,29866 | 0,26505 | 0,19628 | 0,33299 | €182,11 | €546,32 | €50,81 | €12,02 |
| Rapida V1 — Long + BTC 1–3 + score <7,5 | ONDO | LONG | Momentum / breakout | 60m | 3,0x | 0,39694 | 0,39694 | 0,38849 | 0,26661 | 0,40961 | €783,06 | €2.349,19 | €50,00 | €0,00 |
| Rapida V1 — senza PEPE | ONDO | LONG | Momentum / breakout | 60m | 3,0x | 0,39924 | 0,39924 | 0,38995 | 0,26816 | 0,41318 | €713,68 | €2.141,05 | €49,83 | €0,00 |
| Rapida V1 — senza PEPE | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00271 | 0,00314 | 0,00283 | 0,00182 | 0,00319 | €141,51 | €424,53 | €0,00 | €67,75 |
| Rapida V1 — senza PEPE | BANK | LONG | Momentum / breakout | 60m | 3,0x | 0,29671 | 0,29866 | 0,26700 | 0,19929 | 0,34127 | €166,45 | €499,35 | €49,99 | €3,28 |
| Rapida V1 — senza PEPE | ZEC | SHORT | Momentum / breakout | 60m | 3,0x | 491,90160 | 493,79000 | 499,88678 | 653,40929 | 479,92384 | €1.035,86 | €3.107,57 | €50,45 | €-11,93 |
| Rapida V1 — target pieno 2R | ONDO | LONG | Momentum / breakout | 60m | 3,0x | 0,39924 | 0,39924 | 0,38995 | 0,26816 | 0,41782 | €712,92 | €2.138,77 | €49,77 | €0,00 |
| Rapida V1 — target pieno 2R | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00271 | 0,00314 | 0,00283 | 0,00182 | 0,00335 | €139,74 | €419,22 | €0,00 | €66,90 |
| Rapida V1 — target pieno 2R | BANK | LONG | Momentum / breakout | 60m | 3,0x | 0,29671 | 0,29866 | 0,26700 | 0,19929 | 0,35612 | €160,59 | €481,78 | €48,23 | €3,17 |
| Rapida V1 — target pieno 2R | SOL | SHORT | Momentum / breakout | 60m | 3,0x | 74,42911 | 74,00400 | 74,28695 | 98,86667 | 72,76190 | €1.475,37 | €4.426,11 | €0,00 | €25,28 |
| Rapida 1H V2 | DOGE | SHORT | Momentum / breakout V2 | 60m | 3,0x | 0,06865 | 0,06915 | 0,06942 | 0,09119 | 0,06749 | €1.493,88 | €4.481,64 | €50,19 | €-32,89 |
| Rapida 1H V2 | TAO | SHORT | Momentum / breakout V2 | 60m | 3,0x | 188,48684 | 188,48684 | 190,75481 | 250,37335 | 185,08488 | €1.390,02 | €4.170,07 | €50,18 | €-0,00 |
| Rapida 1H V2 | ZEC | SHORT | Momentum / breakout V2 | 60m | 3,0x | 491,90160 | 493,79000 | 499,88678 | 653,40929 | 479,92384 | €1.030,95 | €3.092,84 | €50,21 | €-11,87 |
| Rapida 1H V3 Filtered — madre | ONDO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,39924 | 0,39924 | 0,38995 | 0,26816 | 0,41318 | €715,14 | €2.145,42 | €49,93 | €0,00 |
| Rapida 1H V3 Filtered — madre | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00271 | 0,00314 | 0,00283 | 0,00182 | 0,00319 | €142,26 | €426,77 | €0,00 | €68,10 |
| Rapida 1H V3 Filtered — madre | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,29671 | 0,29866 | 0,26700 | 0,19929 | 0,34127 | €167,02 | €501,07 | €50,17 | €3,29 |
| Rapida 1H V3 Filtered — madre | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 491,90160 | 493,79000 | 499,88678 | 653,40929 | 479,92384 | €1.041,65 | €3.124,94 | €50,73 | €-12,00 |
| Rapida V3 — score <7,5 | ONDO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,39924 | 0,39924 | 0,38995 | 0,26816 | 0,41318 | €712,28 | €2.136,85 | €49,73 | €0,00 |
| Rapida V3 — score <7,5 | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 498,39030 | 493,79000 | 496,69649 | 662,02845 | 486,88556 | €1.095,55 | €3.286,66 | €0,00 | €30,34 |
| Rapida V3 — score <7,5 | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 63750,18741 | 64140,17000 | 64464,18951 | 84681,49895 | 62679,18426 | €1.506,88 | €4.520,63 | €50,63 | €-27,65 |
| Rapida V3 — score <7,5 | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,29223 | 0,29866 | 0,26505 | 0,19628 | 0,33299 | €183,05 | €549,16 | €51,07 | €12,09 |
| Rapida V3 — no volatilità HIGH | ONDO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,39924 | 0,39924 | 0,38995 | 0,26816 | 0,41318 | €707,41 | €2.122,22 | €49,39 | €0,00 |
| Rapida V3 — no volatilità HIGH | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00271 | 0,00314 | 0,00283 | 0,00182 | 0,00319 | €140,21 | €420,64 | €0,00 | €67,13 |
| Rapida V3 — no volatilità HIGH | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,29671 | 0,29866 | 0,26700 | 0,19929 | 0,34127 | €162,98 | €488,93 | €48,95 | €3,21 |
| Rapida V3 — no volatilità HIGH | SOL | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 74,42911 | 74,00400 | 74,28695 | 98,86667 | 73,17870 | €1.480,38 | €4.441,15 | €0,00 | €25,37 |
| Rapida V3 — Long + no HIGH + score <7,5 | BEAT | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 3,33512 | 3,33512 | 3,07807 | 2,24009 | 3,72069 | €211,65 | €634,94 | €48,94 | €0,00 |
| Rapida V3 — Long + no HIGH + score <7,5 | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,29223 | 0,29866 | 0,26505 | 0,19628 | 0,33299 | €175,74 | €527,22 | €49,03 | €11,60 |
| Rapida V3 — senza ESPORTS | ONDO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,39924 | 0,39924 | 0,38995 | 0,26816 | 0,41318 | €712,28 | €2.136,85 | €49,73 | €0,00 |
| Rapida V3 — senza ESPORTS | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00271 | 0,00314 | 0,00283 | 0,00182 | 0,00319 | €140,59 | €421,78 | €0,00 | €67,31 |
| Rapida V3 — senza ESPORTS | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,29671 | 0,29866 | 0,26700 | 0,19929 | 0,34127 | €162,73 | €488,20 | €48,88 | €3,21 |
| Rapida V3 — senza ESPORTS | SOL | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 74,42911 | 74,00400 | 74,28695 | 98,86667 | 73,17870 | €1.484,39 | €4.453,17 | €0,00 | €25,43 |
| Rapida V3 — qualità completa + profit lock | BEAT | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 3,33512 | 3,33512 | 3,07807 | 2,24009 | 3,72069 | €210,89 | €632,67 | €48,76 | €0,00 |
| Rapida V3 — qualità completa + profit lock | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,29223 | 0,29866 | 0,26505 | 0,19628 | 0,33299 | €175,11 | €525,34 | €48,86 | €11,56 |
| Ampia 4H | DOGE | SHORT | Confluenza trend | 240m | 2,0x | 0,07237 | 0,06915 | 0,07077 | 0,10819 | 0,06457 | €649,49 | €1.298,97 | €0,00 | €57,74 |
| Ampia 4H | ZEC | LONG | Confluenza trend | 240m | 2,0x | 522,36445 | 493,79000 | 483,09844 | 263,79405 | 632,30930 | €332,53 | €665,06 | €49,99 | €-36,38 |
| Ampia 4H | HYPE | SHORT | Confluenza trend | 240m | 2,0x | 58,36732 | 58,99500 | 61,80927 | 87,25915 | 48,72988 | €424,03 | €848,06 | €50,01 | €-9,12 |
| Ampia 4H | TAO | SHORT | Confluenza trend | 240m | 2,0x | 189,05650 | 189,05650 | 197,51338 | 282,63946 | 165,37722 | €558,68 | €1.117,36 | €49,98 | €-0,00 |
| Forza relativa 1H V1 | ESPORTS | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,02126 | 0,02126 | 0,02126 | 0,03178 | 0,01564 | €208,05 | €416,10 | €0,00 | €-0,00 |
| Forza relativa 1H V1 | NIGHT | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,02031 | 0,02031 | 0,02210 | 0,03036 | 0,01637 | €285,91 | €571,83 | €50,45 | €-0,00 |
| Forza relativa 1H V1 | ONDO | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,42171 | €891,90 | €1.783,80 | €49,29 | €0,00 |
| Forza relativa 1H V1 | BANK | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,29967 | 0,29866 | 0,26406 | 0,15133 | 0,37800 | €204,97 | €409,93 | €48,71 | €-1,38 |
| Forza relativa 1H V2 | ESPORTS | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,02126 | 0,02126 | 0,02126 | 0,03178 | 0,01564 | €215,33 | €430,67 | €0,00 | €-0,00 |
| Forza relativa 1H V2 | AKE | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,00271 | 0,00314 | 0,00239 | 0,00137 | 0,00343 | €209,76 | €419,52 | €50,34 | €66,95 |
| Forza relativa 1H V2 | BANK | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,29683 | 0,29866 | 0,26156 | 0,14990 | 0,37442 | €213,94 | €427,88 | €50,84 | €2,64 |
| Forza relativa 1H V2 | ZEC | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 493,58126 | 493,79000 | 503,90129 | 737,90399 | 470,87721 | €1.207,34 | €2.414,67 | €50,49 | €-1,02 |
| Benchmark Donchian breakout 1H | SUI | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,76606 | 0,76606 | 0,75182 | 0,38686 | 0,80165 | €1.377,00 | €2.754,00 | €51,18 | €0,00 |
| Benchmark Donchian breakout 1H | ZEC | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 514,40710 | 493,79000 | 500,37124 | 769,03861 | 481,15276 | €982,86 | €1.965,73 | €0,00 | €78,78 |
| Benchmark Donchian breakout 1H | AKE | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,00278 | 0,00314 | 0,00245 | 0,00140 | 0,00362 | €212,99 | €425,98 | €51,12 | €55,57 |
| Benchmark Bollinger mean reversion 1H | BTC | LONG | Bollinger mean reversion | 60m | 2,0x | 64125,06245 | 64140,17000 | 63355,56170 | 32383,15654 | 65279,31357 | €2.018,75 | €4.037,51 | €48,45 | €0,95 |
| Benchmark Bollinger mean reversion 1H | SOL | LONG | Bollinger mean reversion | 60m | 2,0x | 73,77975 | 74,00400 | 72,89440 | 37,25878 | 75,10779 | €2.011,27 | €4.022,55 | €48,27 | €12,23 |
| Benchmark trend following EMA 1H | LAB | LONG | Trend following EMA | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €207,05 | €414,10 | €49,69 | €0,00 |
| Benchmark trend following EMA 1H | PEPE | SHORT | Trend following EMA | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.555,71 | €3.111,43 | €0,00 | €64,25 |
| Benchmark trend following EMA 1H | DOGE | SHORT | Trend following EMA | 60m | 2,0x | 0,06906 | 0,06915 | 0,07019 | 0,10324 | 0,06656 | €1.523,03 | €3.046,06 | €50,05 | €-4,14 |
| Scanner Top 5 Long 1H | ONDO | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,40114 | 0,40114 | 0,38834 | 0,20258 | 0,42673 | €828,91 | €1.657,82 | €52,88 | €0,00 |
| Scanner Top 5 Long 1H | LAB | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €219,03 | €438,05 | €52,57 | €0,00 |
| Scanner Top 5 Long 1H | BANK | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,26033 | 0,29866 | 0,27587 | 0,13147 | 0,32281 | €221,39 | €442,77 | €0,00 | €65,19 |
| Scanner Bottom 5 Short 1H | ESPORTS | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,02150 | 0,02150 | 0,02150 | 0,03214 | 0,01634 | €207,40 | €414,80 | €0,00 | €-0,00 |
| Scanner Bottom 5 Short 1H | ADA | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,16703 | 0,16360 | 0,16501 | 0,24971 | 0,16112 | €1.381,07 | €2.762,13 | €0,00 | €56,72 |
| Scanner Bottom 5 Short 1H | ZEC | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 494,80102 | 493,79000 | 505,14655 | 739,72752 | 474,10997 | €1.169,31 | €2.338,62 | €48,90 | €4,78 |
| Scanner Top 5 + forza BTC 1H | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39694 | 0,39694 | 0,38539 | 0,20045 | 0,42235 | €898,57 | €1.797,15 | €52,29 | €0,00 |
| Scanner Top 5 + forza BTC 1H | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €216,56 | €433,12 | €51,97 | €0,00 |
| Scanner Top 5 + forza BTC 1H | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,26033 | 0,29866 | 0,27587 | 0,13147 | 0,32906 | €216,24 | €432,48 | €0,00 | €63,67 |
| Top 5 + BTC — solo MFE | SUI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,76776 | 0,76776 | 0,75508 | 0,38772 | 0,79565 | €1.514,04 | €3.028,08 | €50,00 | €0,00 |
| Top 5 + BTC — solo MFE | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39924 | 0,39924 | 0,38729 | 0,20162 | 0,42552 | €835,46 | €1.670,91 | €50,00 | €0,00 |
| Top 5 + BTC — solo MFE | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00271 | 0,00314 | 0,00279 | 0,00137 | 0,00343 | €202,85 | €405,69 | €0,00 | €64,74 |
| Top 5 + BTC — Guard | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39724 | 0,39724 | 0,38434 | 0,20061 | 0,42561 | €756,62 | €1.513,24 | €49,13 | €0,00 |
| Top 5 + BTC — Guard | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €202,47 | €404,95 | €48,59 | €0,00 |
| Top 5 + BTC — Guard | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,26033 | 0,29866 | 0,27587 | 0,13147 | 0,32906 | €204,86 | €409,72 | €0,00 | €60,32 |
| Top 5 + BTC — BTC≤3 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39974 | 0,39974 | 0,38840 | 0,20187 | 0,42468 | €884,65 | €1.769,29 | €50,18 | €0,00 |
| Top 5 + BTC — BTC≤3 | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €207,87 | €415,74 | €49,89 | €0,00 |
| Top 5 + BTC — BTC≤3 | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,26033 | 0,29866 | 0,27587 | 0,13147 | 0,32906 | €207,68 | €415,35 | €0,00 | €61,15 |
| Top 5 + BTC — BTC 2–3 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39974 | 0,39974 | 0,38840 | 0,20187 | 0,42468 | €884,65 | €1.769,29 | €50,18 | €0,00 |
| Top 5 + BTC — BTC 2–3 | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €207,87 | €415,74 | €49,89 | €0,00 |
| Top 5 + BTC — BTC 2–3 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00271 | 0,00314 | 0,00239 | 0,00137 | 0,00343 | €207,27 | €414,53 | €49,74 | €66,15 |
| Top 5 + BTC — Guard + MFE | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39724 | 0,39724 | 0,38434 | 0,20061 | 0,42561 | €756,62 | €1.513,24 | €49,13 | €0,00 |
| Top 5 + BTC — Guard + MFE | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00271 | 0,00314 | 0,00279 | 0,00137 | 0,00343 | €201,10 | €402,21 | €0,00 | €64,18 |
| Top 5 + BTC — Guard + MFE | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,29671 | 0,29866 | 0,26110 | 0,14984 | 0,37504 | €201,10 | €402,19 | €48,26 | €2,64 |
| Top 5 + BTC — Guard + BTC≤3 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39974 | 0,39974 | 0,38840 | 0,20187 | 0,42468 | €871,05 | €1.742,11 | €49,41 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €205,84 | €411,68 | €49,40 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,26033 | 0,29866 | 0,27587 | 0,13147 | 0,32906 | €208,27 | €416,53 | €0,00 | €61,32 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39974 | 0,39974 | 0,38840 | 0,20187 | 0,42468 | €871,05 | €1.742,11 | €49,41 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00271 | 0,00314 | 0,00279 | 0,00137 | 0,00343 | €203,41 | €406,83 | €0,00 | €64,92 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,29671 | 0,29866 | 0,26110 | 0,14984 | 0,37504 | €203,41 | €406,81 | €48,82 | €2,67 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39694 | 0,39694 | 0,38539 | 0,20045 | 0,43159 | €861,83 | €1.723,66 | €50,15 | €0,00 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,21338 | €207,96 | €415,92 | €49,91 | €0,00 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,26033 | 0,29866 | 0,27587 | 0,13147 | 0,35405 | €210,29 | €420,58 | €0,00 | €61,92 |
| Top 5 + BTC — target pieno 3R | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39694 | 0,39694 | 0,38539 | 0,20045 | 0,43159 | €861,83 | €1.723,66 | €50,15 | €0,00 |
| Top 5 + BTC — target pieno 3R | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,21338 | €207,96 | €415,92 | €49,91 | €0,00 |
| Top 5 + BTC — target pieno 3R | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,26033 | 0,29866 | 0,27587 | 0,13147 | 0,35405 | €211,25 | €422,51 | €0,00 | €62,20 |
| Global Confluence puro 1H | DOGE | SHORT | Global Confluence puro | 60m | 2,0x | 0,06942 | 0,06915 | 0,06942 | 0,10378 | 0,06664 | €1.539,06 | €3.078,12 | €0,00 | €11,80 |
| Combo Trend | ESPORTS | SHORT | Combo Trend | 60m | 2,0x | 0,01883 | 0,01883 | 0,02109 | 0,02815 | 0,01386 | €209,57 | €419,14 | €50,30 | €-0,00 |
| Combo Trend | BANK | LONG | Combo Trend | 60m | 2,0x | 0,24758 | 0,29866 | 0,26731 | 0,12503 | 0,31294 | €205,58 | €411,17 | €0,00 | €84,83 |
| Combo Trend | AKE | LONG | Combo Trend | 60m | 2,0x | 0,00247 | 0,00314 | 0,00275 | 0,00125 | 0,00312 | €207,14 | €414,28 | €0,00 | €113,36 |
| Combo Mean Reversion | BTC | LONG | Combo Mean Reversion | 60m | 2,0x | 63775,69259 | 64140,17000 | 63010,38428 | 32206,72476 | 65000,18589 | €1.998,65 | €3.997,31 | €47,97 | €22,84 |
| Combo Scanner | ONDO | LONG | Combo Scanner | 60m | 2,0x | 0,39694 | 0,39694 | 0,38539 | 0,20045 | 0,42235 | €857,88 | €1.715,77 | €49,92 | €0,00 |
| Combo Scanner | LAB | LONG | Combo Scanner | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €207,54 | €415,08 | €49,81 | €0,00 |
| Combo Scanner | DOGE | SHORT | Combo Scanner | 60m | 2,0x | 0,06906 | 0,06915 | 0,07008 | 0,10324 | 0,06681 | €1.710,76 | €3.421,51 | €50,60 | €-4,65 |
| Combo Adaptive — madre | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,40114 | 0,40114 | 0,38834 | 0,20258 | 0,42673 | €809,25 | €1.618,50 | €51,63 | €0,00 |
| Combo Adaptive — madre | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15861 | 0,13958 | 0,08010 | 0,19668 | €213,13 | €426,26 | €51,15 | €0,00 |
| Combo Adaptive — madre | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,06906 | 0,06915 | 0,07008 | 0,10324 | 0,06701 | €1.735,03 | €3.470,05 | €51,32 | €-4,71 |
| Combo Adaptive — MFE Trail esistente | ESPORTS | SHORT | Combo Adaptive | 60m | 2,0x | 0,02156 | 0,02156 | 0,02091 | 0,03223 | 0,01638 | €202,62 | €405,24 | €0,00 | €-0,00 |
| Combo Adaptive — MFE Trail esistente | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39784 | 0,39784 | 0,38492 | 0,20091 | 0,42367 | €744,71 | €1.489,41 | €48,35 | €0,00 |
| Combo Adaptive — MFE Trail esistente | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15861 | 0,13958 | 0,08010 | 0,19668 | €201,70 | €403,39 | €48,41 | €0,00 |
| Combo Adaptive — Quality7 | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,40304 | 0,40304 | 0,39140 | 0,20354 | 0,42632 | €859,15 | €1.718,30 | €49,62 | €0,00 |
| Combo Adaptive — Quality7 | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,00271 | 0,00314 | 0,00280 | 0,00137 | 0,00336 | €208,50 | €417,01 | €0,00 | €66,55 |
| Combo Adaptive — Quality7 | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,06906 | 0,06915 | 0,07008 | 0,10324 | 0,06701 | €1.690,45 | €3.380,89 | €50,00 | €-4,59 |
| Combo Adaptive — Trend/Transition | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39724 | 0,39724 | 0,38434 | 0,20061 | 0,42303 | €757,94 | €1.515,88 | €49,21 | €0,00 |
| Combo Adaptive — Trend/Transition | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15861 | 0,13958 | 0,08010 | 0,19668 | €206,52 | €413,04 | €49,56 | €0,00 |
| Combo Adaptive — Quality7 + Regime | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,40554 | 0,40554 | 0,39390 | 0,20480 | 0,42882 | €864,27 | €1.728,54 | €49,61 | €0,00 |
| Combo Adaptive — Quality7 + Regime | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,00271 | 0,00314 | 0,00280 | 0,00137 | 0,00336 | €205,57 | €411,14 | €0,00 | €65,61 |
| Combo Adaptive — Long Only | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,41951 | €893,67 | €1.787,34 | €49,39 | €0,00 |
| Combo Adaptive — Long Only | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €205,55 | €411,10 | €49,33 | €0,00 |
| Combo Adaptive — parziale 1R | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,41951 | €893,02 | €1.786,04 | €49,36 | €0,00 |
| Combo Adaptive — parziale 1R | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €205,22 | €410,44 | €49,25 | €0,00 |
| Combo Adaptive — parziale 1R | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,06906 | 0,06915 | 0,07008 | 0,10324 | 0,06701 | €1.666,71 | €3.333,43 | €49,30 | €-4,53 |
| Combo Adaptive — Quality7 + Regime + parziale 1R | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,40554 | 0,40554 | 0,39390 | 0,20480 | 0,42882 | €864,27 | €1.728,54 | €49,61 | €0,00 |
| Combo Adaptive — Quality7 + Regime + parziale 1R | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,00271 | 0,00314 | 0,00280 | 0,00137 | 0,00336 | €103,02 | €206,04 | €0,00 | €32,88 |
| Combo Adaptive — 75% a 2R + runner 3R | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,43050 | €902,18 | €1.804,37 | €49,86 | €0,00 |
| Combo Adaptive — 75% a 2R + runner 3R | BANK | LONG | Combo Adaptive | 60m | 2,0x | 0,26033 | 0,29866 | 0,27790 | 0,13147 | 0,35405 | €206,98 | €413,96 | €0,00 | €60,95 |
| Combo Adaptive — 75% a 2R + runner 3R | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,06906 | 0,06915 | 0,07008 | 0,10324 | 0,06599 | €1.688,60 | €3.377,21 | €49,95 | €-4,59 |
| Combo Adaptive — target pieno 3R | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,43050 | €902,18 | €1.804,37 | €49,86 | €0,00 |
| Combo Adaptive — target pieno 3R | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15861 | 0,13958 | 0,08010 | 0,21571 | €207,43 | €414,86 | €49,78 | €0,00 |
| Combo Adaptive — target pieno 3R | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,06906 | 0,06915 | 0,07008 | 0,10324 | 0,06599 | €1.688,61 | €3.377,21 | €49,95 | €-4,59 |
| Btc Ema 1H | BTC | SHORT | Trend following EMA | 60m | 3,0x | 64120,47334 | 64140,17000 | 65043,80816 | 85173,36209 | 62273,80371 | €1.153,43 | €3.460,30 | €49,83 | €-1,06 |
| Btc Bollinger 1H | BTC | LONG | Bollinger mean reversion | 60m | 3,0x | 64125,06245 | 64140,17000 | 63355,56170 | 43070,66694 | 65279,31357 | €1.402,77 | €4.208,32 | €50,50 | €0,99 |
| Sol Ema 1H | SOL | SHORT | Trend following EMA | 60m | 3,0x | 75,65487 | 74,00400 | 74,29918 | 100,49488 | 73,47601 | €1.150,16 | €3.450,47 | €0,00 | €75,29 |
| Sol Ema 4H | SOL | SHORT | Trend following EMA | 240m | 2,0x | 75,05699 | 74,00400 | 77,22103 | 112,21019 | 69,64688 | €862,58 | €1.725,17 | €49,74 | €24,20 |
| Sol Donchian 4H | SOL | SHORT | Donchian breakout 20 barre | 240m | 2,0x | 75,96380 | 74,00400 | 78,23939 | 113,56589 | 69,59218 | €830,21 | €1.660,43 | €49,74 | €42,84 |
| Sol Bollinger 1H | SOL | LONG | Bollinger mean reversion | 60m | 3,0x | 73,77975 | 74,00400 | 72,89440 | 49,55540 | 75,10779 | €1.365,75 | €4.097,24 | €49,17 | €12,45 |
| Sol Adaptive 1H | SOL | SHORT | Combo Adaptive | 60m | 3,0x | 74,08718 | 74,00400 | 75,15403 | 98,41247 | 71,95347 | €1.144,60 | €3.433,80 | €49,45 | €3,86 |
| Sol Adaptive 4H | SOL | SHORT | Combo Adaptive | 240m | 2,0x | 75,96380 | 74,00400 | 78,44626 | 113,56589 | 69,75767 | €761,04 | €1.522,08 | €49,74 | €39,27 |
| Eth Ema 1H | ETH | SHORT | Trend following EMA | 60m | 3,0x | 1873,22528 | 1863,94000 | 1900,19972 | 2488,26758 | 1819,27639 | €1.138,34 | €3.415,02 | €49,18 | €16,93 |
| Eth Donchian 1H | ETH | SHORT | Donchian breakout 20 barre | 60m | 3,0x | 1856,94854 | 1863,94000 | 1880,71748 | 2466,64664 | 1809,41065 | €1.299,81 | €3.899,43 | €49,91 | €-14,68 |
| Eth Adaptive 1H | ETH | SHORT | Combo Adaptive | 60m | 3,0x | 1873,22528 | 1863,94000 | 1900,19972 | 2488,26758 | 1819,27639 | €1.146,74 | €3.440,21 | €49,54 | €17,05 |
| Doge Ema 1H | DOGE | SHORT | Trend following EMA | 60m | 3,0x | 0,06906 | 0,06915 | 0,07008 | 0,09173 | 0,06701 | €1.143,65 | €3.430,94 | €50,74 | €-4,66 |
| Master Adaptive V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39854 | 0,39854 | 0,38677 | 0,20126 | 0,42207 | €833,00 | €1.665,99 | €49,19 | €0,00 |
| Master Adaptive V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €203,80 | €407,60 | €48,91 | €0,00 |
| Master Adaptive V1 | BANK | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,25383 | 0,29866 | 0,22337 | 0,12818 | 0,31475 | €202,68 | €405,37 | €48,64 | €71,59 |
| Master Adaptive No Alt V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39854 | 0,39854 | 0,38677 | 0,20126 | 0,42207 | €833,00 | €1.665,99 | €49,19 | €0,00 |
| Master Adaptive No Alt V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €203,80 | €407,60 | €48,91 | €0,00 |
| Master Adaptive No Alt V1 | BANK | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,25383 | 0,29866 | 0,22337 | 0,12818 | 0,31475 | €202,68 | €405,37 | €48,64 | €71,59 |
| Master Adaptive Strict3 V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,41951 | €887,07 | €1.774,14 | €49,03 | €0,00 |
| Master Adaptive Strict3 V1 | BANK | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,29671 | 0,29866 | 0,26110 | 0,14984 | 0,36792 | €199,82 | €399,64 | €47,96 | €2,63 |
| Master Adaptive Expanded V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39854 | 0,39854 | 0,38677 | 0,20126 | 0,42207 | €833,00 | €1.665,99 | €49,19 | €0,00 |
| Master Adaptive Expanded V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €203,80 | €407,60 | €48,91 | €0,00 |
| Master Adaptive Expanded V1 | BANK | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,25627 | 0,29866 | 0,22552 | 0,12942 | 0,31778 | €203,36 | €406,71 | €48,81 | €67,27 |
| Master Adaptive Gb20 V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,40304 | 0,40304 | 0,39140 | 0,20354 | 0,42632 | €848,64 | €1.697,27 | €49,02 | €0,00 |
| Master Adaptive Gb20 V1 | BANK | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,30297 | 0,29866 | 0,26661 | 0,15300 | 0,37568 | €202,48 | €404,95 | €48,59 | €-5,76 |
| Master Adaptive Gb20 V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00284 | 0,00314 | 0,00301 | 0,00143 | 0,00352 | €202,14 | €404,28 | €0,00 | €43,71 |
| Master Adaptive Runner25 V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39854 | 0,39854 | 0,38677 | 0,20126 | 0,43384 | €833,00 | €1.665,99 | €49,19 | €0,00 |
| Master Adaptive Runner25 V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,21338 | €203,80 | €407,60 | €48,91 | €0,00 |
| Master Adaptive Runner25 V1 | BANK | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,25383 | 0,29866 | 0,22337 | 0,12818 | 0,34521 | €202,68 | €405,37 | €48,64 | €71,59 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Master Adaptive Strict3 V1 | AKE | LONG | 2026-07-24T17:38:34+00:00 | 0,00297 | €94,47 | 1,98 | TARGET |
| Rapida V3 — Long + no HIGH + score <7,5 | AKE | LONG | 2026-07-24T17:38:34+00:00 | 0,00297 | €72,54 | 1,49 | TARGET |
| Rapida V3 — qualità completa + profit lock | AKE | LONG | 2026-07-24T17:38:34+00:00 | 0,00297 | €72,28 | 1,49 | TARGET |
| Rapida V1 — score 6–7,5 | AKE | LONG | 2026-07-24T17:38:34+00:00 | 0,00297 | €74,99 | 1,49 | TARGET |
| Rapida V1 — Long + BTC 1–3 + score <7,5 | AKE | LONG | 2026-07-24T17:38:34+00:00 | 0,00297 | €73,16 | 1,49 | TARGET |
| Rapida 1H V3 Filtered — madre | ZEC | SHORT | 2026-07-24T17:23:35+00:00 | 489,38180 | €72,91 | 1,44 | TARGET |
| Rapida 1H V2 | ZEC | SHORT | 2026-07-24T17:23:35+00:00 | 489,38180 | €71,72 | 1,44 | TARGET |
| Rapida V1 — senza PEPE | ZEC | SHORT | 2026-07-24T17:23:35+00:00 | 489,95475 | €72,15 | 1,44 | TARGET |
| Rapida 1H V1 — madre | ZEC | SHORT | 2026-07-24T17:23:35+00:00 | 489,38180 | €71,26 | 1,44 | TARGET |
| Scalp RSI Long 25 · prudente · 5x | BTC | LONG | 2026-07-24T16:53:36+00:00 | 63945,79744 | €-3,01 | -0,30 | STOP |
| Scalp RSI Long 20 · prudente · 5x | BTC | LONG | 2026-07-24T16:53:36+00:00 | 63945,79744 | €-3,01 | -0,30 | STOP |
| Scalp RSI Long 25 · €50 · 15x | BTC | LONG | 2026-07-24T16:53:36+00:00 | 63945,79744 | €-1,05 | -0,30 | STOP |

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
| MAIN | Principale 4H | 49/30 | 18/30 | 0,93 | 0,91 | -0,05R | €-2,94 | 4,26% | COERENTE − | BOCCIATA RESEARCH |
| RSI_EXTREME_LONG_15M | Scalp RSI Long 25 · prudente · 5x (riferimento tra 9 varianti) | 8/30 | 5/30 | 0,30 | 0,20 | -0,56R | €-4,60 | 0,37% | COERENTE − | RACCOLTA RESEARCH |
| RSI_EXTREME_SHORT_15M | Scalp RSI Short 75 · prudente · 5x (riferimento tra 9 varianti) | 7/30 | 6/30 | 0,62 | 0,18 | -0,24R | €-5,86 | 0,36% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_1H_BALANCED | Bilanciata 1H V1 | 154/30 | 37/30 | 1,00 | 1,46 | -0,00R | €9,09 | 2,30% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_BALANCED_V2 | Bilanciata 1H V2 | 32/30 | 24/30 | 1,73 | 1,19 | 0,39R | €3,99 | 2,75% | COERENTE + | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_1H_BALANCED_V3 | Bilanciata 1H V3 Filtered | 61/30 | 33/30 | 1,20 | 1,35 | 0,13R | €8,46 | 2,20% | COERENTE + | PRONTA PER REVISIONE LIVE |
| SHADOW_1H_FAST | Rapida 1H V1 — madre | 185/30 | 67/30 | 0,93 | 0,92 | -0,04R | €-1,84 | 6,76% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | Rapida V1 — Long + BTC 1–3 + score <7,5 | 11/30 | 10/30 | 1,17 | 0,63 | 0,10R | €-8,69 | 1,92% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | Rapida V1 — no HIGH + score <7,5 | 48/30 | 31/30 | 1,04 | 1,19 | 0,02R | €4,17 | 2,83% | COERENTE + | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_NO_PEPE_V1 | Rapida V1 — senza PEPE | 52/30 | 27/30 | 0,90 | 1,09 | -0,06R | €1,78 | 2,10% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_V1 | Rapida V1 — score 6–7,5 | 35/30 | 32/30 | 1,25 | 1,48 | 0,14R | €8,76 | 2,49% | COERENTE + | PRONTA PER REVISIONE LIVE |
| SHADOW_1H_FAST_TP2_V1 | Rapida V1 — target pieno 2R | 44/30 | 28/30 | 0,67 | 0,86 | -0,25R | €-3,21 | 2,58% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V2 | Rapida 1H V2 | 7/30 | 7/30 | 0,40 | 1,64 | -0,50R | €9,85 | 1,69% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3 | Rapida 1H V3 Filtered — madre | 94/30 | 59/30 | 1,03 | 1,09 | 0,02R | €1,77 | 2,89% | COERENTE + | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_CAP75_V1 | Rapida V3 — score <7,5 | 43/30 | 26/30 | 0,96 | 1,36 | -0,03R | €6,99 | 2,49% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | Rapida V3 — qualità completa + profit lock | 22/30 | 21/30 | 0,78 | 0,68 | -0,15R | €-9,83 | 3,21% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | Rapida V3 — Long + no HIGH + score <7,5 | 22/30 | 21/30 | 0,78 | 0,72 | -0,15R | €-8,15 | 2,86% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | Rapida V3 — Long Only | 27/30 | 24/30 | 0,58 | 0,65 | -0,32R | €-9,62 | 3,31% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | Rapida V3 — no volatilità HIGH | 49/30 | 32/30 | 0,92 | 0,93 | -0,05R | €-1,76 | 2,96% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | Rapida V3 — senza ESPORTS | 50/30 | 31/30 | 0,89 | 0,96 | -0,07R | €-0,95 | 2,49% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_4H_WIDE | Ampia 4H | 42/30 | 14/30 | 0,97 | 0,96 | -0,03R | €-1,26 | 2,94% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_BOLLINGER_MR_1H | Benchmark Bollinger mean reversion 1H | 38/30 | 28/30 | 0,96 | 1,11 | -0,03R | €2,50 | 2,06% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_BTC_ADAPTIVE_1H | Btc Adaptive 1H | 3/30 | 3/30 | 0,00 | 1,24 | -1,11R | €4,43 | 0,89% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_BTC_ADAPTIVE_4H | Btc Adaptive 4H | 1/30 | 1/30 | 0,00 | 0,00 | -1,07R | €-50,38 | 0,74% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_BOLLINGER_1H | Btc Bollinger 1H | 2/30 | 2/30 | ∞ | ∞ | 1,37R | €49,98 | 0,54% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_BTC_BOLLINGER_4H | Btc Bollinger 4H | 1/30 | 1/30 | ∞ | ∞ | 1,72R | €84,12 | 0,30% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_BTC_DONCHIAN_1H | Btc Donchian 1H | 4/30 | 4/30 | 0,00 | 0,82 | -1,12R | €-4,84 | 1,49% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_DONCHIAN_4H | Btc Donchian 4H | 1/30 | 1/30 | 0,00 | 0,00 | -1,07R | €-49,32 | 0,96% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_EMA_1H | Btc Ema 1H | 4/30 | 5/30 | 0,57 | 0,79 | -0,36R | €-6,87 | 1,56% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_EMA_4H | Btc Ema 4H | 1/30 | 1/30 | 0,00 | 0,00 | -1,07R | €-49,32 | 0,96% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE | Combo Adaptive — madre | 101/30 | 22/30 | 1,13 | 1,78 | 0,08R | €12,05 | 1,31% | COERENTE + | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | Combo Adaptive — Long Only | 25/30 | 5/30 | 0,58 | 0,42 | -0,33R | €-26,52 | 2,34% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | Combo Adaptive — MFE Trail esistente | 68/30 | 27/30 | 1,00 | 0,45 | 0,00R | €-11,76 | 4,11% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | Combo Adaptive — parziale 1R | 44/30 | 12/30 | 0,76 | 0,64 | -0,18R | €-11,54 | 2,24% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | Combo Adaptive — Quality7 + Regime + parziale 1R | 4/30 | 4/30 | 0,60 | 0,32 | -0,32R | €-27,31 | 1,95% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | Combo Adaptive — Quality7 + Regime | 4/30 | 4/30 | 0,60 | 0,18 | -0,32R | €-32,87 | 1,95% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | Combo Adaptive — Quality7 | 7/30 | 7/30 | 0,75 | 1,36 | -0,19R | €5,56 | 1,51% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | Combo Adaptive — Trend/Transition | 25/30 | 10/30 | 0,34 | 0,92 | -0,59R | €-2,35 | 2,18% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | Combo Adaptive — 75% a 2R + runner 3R | 30/30 | 14/30 | 0,42 | 0,82 | -0,54R | €-5,13 | 2,12% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | Combo Adaptive — target pieno 3R | 30/30 | 10/30 | 0,42 | 0,96 | -0,54R | €-0,91 | 1,41% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_MEAN_REVERSION | Combo Mean Reversion | 16/30 | 14/30 | 0,84 | 0,98 | -0,11R | €-0,48 | 2,31% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_SCANNER | Combo Scanner | 60/30 | 24/30 | 1,42 | 1,20 | 0,26R | €5,08 | 2,66% | COERENTE + | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_COMBO_TREND | Combo Trend | 74/30 | 26/30 | 0,99 | 0,82 | -0,01R | €-5,51 | 3,58% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_DOGE_BOLLINGER_1H | Doge Bollinger 1H | 2/30 | 2/30 | 0,00 | 0,00 | -1,12R | €-55,56 | 1,26% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_DOGE_DONCHIAN_1H | Doge Donchian 1H | 2/30 | 4/30 | 1,67 | 0,98 | 0,38R | €-0,31 | 0,96% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_DOGE_EMA_1H | Doge Ema 1H | 3/30 | 7/30 | 3,40 | 2,33 | 0,89R | €21,18 | 1,36% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_DONCHIAN_1H | Benchmark Donchian breakout 1H | 41/30 | 18/30 | 0,95 | 1,44 | -0,04R | €9,70 | 2,12% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_EMA_TREND_1H | Benchmark trend following EMA 1H | 80/30 | 18/30 | 0,97 | 0,87 | -0,02R | €-3,02 | 2,25% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_ETH_ADAPTIVE_1H | Eth Adaptive 1H | 4/30 | 4/30 | 0,57 | 0,16 | -0,36R | €-23,05 | 1,24% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_BOLLINGER_1H | Eth Bollinger 1H | 1/30 | 1/30 | 0,00 | ∞ | -1,13R | €15,45 | 0,51% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_ETH_DONCHIAN_1H | Eth Donchian 1H | 3/30 | 3/30 | 0,84 | 0,84 | -0,12R | €-5,82 | 1,38% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_EMA_1H | Eth Ema 1H | 4/30 | 6/30 | 0,57 | 0,25 | -0,36R | €-27,46 | 1,92% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_EMA_4H | Eth Ema 4H | 1/30 | 1/30 | 0,00 | 0,00 | -1,06R | €-52,88 | 0,68% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_GLOBAL_PURE | Global Confluence puro 1H | 3/30 | 8/30 | 3,47 | 0,45 | 0,91R | €-18,75 | 2,92% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | Master Adaptive Expanded V1 | 21/30 | 7/30 | 0,58 | 0,29 | -0,33R | €-32,57 | 2,80% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | Master Adaptive Gb20 V1 | 21/30 | 30/30 | 0,44 | 0,56 | -0,47R | €-9,39 | 4,16% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | Master Adaptive No Alt V1 | 21/30 | 5/30 | 0,44 | 0,00 | -0,47R | €-54,20 | 3,19% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | Master Adaptive Runner25 V1 | 14/30 | 5/30 | 0,22 | 0,00 | -0,77R | €-54,20 | 3,19% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | Master Adaptive Strict3 V1 | 20/30 | 14/30 | 0,33 | 0,44 | -0,59R | €-26,08 | 4,66% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_V1 | Master Adaptive V1 | 21/30 | 5/30 | 0,44 | 0,00 | -0,47R | €-54,20 | 3,19% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_RELATIVE_STRENGTH | Forza relativa 1H V1 | 108/30 | 24/30 | 1,01 | 0,82 | 0,01R | €-3,30 | 3,25% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_RELATIVE_STRENGTH_V2 | Forza relativa 1H V2 | 35/30 | 32/30 | 1,52 | 1,16 | 0,31R | €4,58 | 3,69% | COERENTE + | PRONTA PER REVISIONE LIVE |
| SHADOW_SCANNER_BOTTOM5_SHORT | Scanner Bottom 5 Short 1H | 40/30 | 23/30 | 1,00 | 0,62 | -0,00R | €-9,49 | 5,48% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC | Scanner Top 5 + forza BTC 1H | 59/30 | 22/30 | 1,36 | 1,96 | 0,22R | €17,32 | 2,01% | COERENTE + | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | Top 5 + BTC — BTC 2–3 | 10/30 | 3/30 | 0,86 | 0,54 | -0,10R | €-16,53 | 2,38% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | Top 5 + BTC — BTC≤3 | 18/30 | 4/30 | 0,59 | 0,73 | -0,33R | €-7,45 | 2,20% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | Top 5 + BTC — Guard + BTC≤3 + MFE | 13/30 | 13/30 | 0,64 | 0,41 | -0,28R | €-18,09 | 2,70% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | Top 5 + BTC — Guard + BTC≤3 | 13/30 | 4/30 | 0,64 | 0,99 | -0,28R | €-0,40 | 1,64% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | Top 5 + BTC — Guard + MFE | 16/30 | 16/30 | 0,49 | 0,32 | -0,43R | €-21,64 | 3,87% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | Top 5 + BTC — Guard | 16/30 | 7/30 | 0,49 | 0,41 | -0,43R | €-23,63 | 3,31% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | Top 5 + BTC — solo MFE | 21/30 | 11/30 | 0,64 | 0,17 | -0,29R | €-23,72 | 3,88% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | Top 5 + BTC — 75% a 2,2R + runner 3R | 14/30 | 8/30 | 0,46 | 1,59 | -0,49R | €11,95 | 2,33% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | Top 5 + BTC — target pieno 3R | 14/30 | 8/30 | 0,46 | 1,87 | -0,49R | €17,72 | 2,33% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_LONG | Scanner Top 5 Long 1H | 72/30 | 30/30 | 1,28 | 2,18 | 0,17R | €20,93 | 2,70% | COERENTE + | PRONTA PER REVISIONE LIVE |
| SHADOW_SOL_ADAPTIVE_1H | Sol Adaptive 1H | 4/30 | 5/30 | 0,57 | 0,38 | -0,36R | €-22,13 | 2,14% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_ADAPTIVE_4H | Sol Adaptive 4H | 1/30 | 1/30 | 0,00 | 0,00 | -1,05R | €-51,83 | 0,59% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_BOLLINGER_1H | Sol Bollinger 1H | 2/30 | 3/30 | 0,00 | 0,00 | -1,13R | €-55,54 | 1,79% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_BOLLINGER_4H | Sol Bollinger 4H | 1/30 | 1/30 | ∞ | ∞ | 1,74R | €86,98 | 0,40% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_SOL_DONCHIAN_1H | Sol Donchian 1H | 3/30 | 3/30 | 0,84 | 21,53 | -0,12R | €30,71 | 0,79% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SOL_DONCHIAN_4H | Sol Donchian 4H | 1/30 | 1/30 | 0,00 | 0,00 | -1,06R | €-52,00 | 0,60% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_EMA_1H | Sol Ema 1H | 3/30 | 3/30 | 0,86 | 0,42 | -0,11R | €-20,89 | 1,67% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_EMA_4H | Sol Ema 4H | 1/30 | 1/30 | 0,00 | 0,00 | -1,06R | €-52,00 | 0,56% | COERENTE − | RACCOLTA RESEARCH |

Per le famiglie RSI con più configurazioni di leva o margine, il lato paper usa il conto con il maggior numero di eventi indipendenti; i conti duplicati non vengono aggregati.
`PRONTA PER REVISIONE LIVE` non invia ordini e non sposta capitale: abilita soltanto una revisione manuale finale.

## 🎯 DOGE Rejection Short — conto dedicato €3.600

Simulazione separata **paper only**: capitale/margine iniziale **€3.600**, leva **5x**, esposizione iniziale **€18.000**. Non modifica i conti paper da €10.000 e non invia ordini reali.

- Stato: **WAITING**
- Prezzo DOGE: **0.06915**
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
| BTC sotto filtro | 64140.17 | OK |

### Ultima candela 15m valutata

- Rejection accettata: **NO**; motivo: **trigger_touched, entry_not_chased**
- High **0.06919**; close **0.06909**; wick alta **58.3%**; volume **x0.66**

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
- Confidenza: **80,40%**
- Volatilità: **NORMAL**
- Rotazione strategie: **SOLO OSSERVAZIONE — nessun peso operativo viene ancora modificato**
- Motivo: Direzione poco definita: score BTC +0.0, breadth EMA50 17%, ADX 19.9.
- BTC trend score: **0,00**; ADX: **19,88**; breadth sopra EMA50: **16,67%**
- Mediana alt vs BTC: **-0,73%**; dispersione: **8,68%**

- Aperti in questo ciclo: **0**
- Chiusi in questo ciclo: **0**
- Posizioni research aperte: **523**
- Trade research chiusi: **2320**
- Eventi di mercato indipendenti chiusi: **646**
- Segnali sovrapposti saltati sullo stesso asset/profilo: **9574**
- Posizioni Research V1 senza regime scartate durante la migrazione: **28**

### Risultati complessivi per strategia

| Profilo | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| MAIN | 14 | 49 | 49 | 32,65% | 0,93 | -0,05R | €-22,57 |
| RSI_EXTREME_LONG_15M | 1 | 8 | 8 | 25,00% | 0,30 | -0,56R | €-45,05 |
| RSI_EXTREME_SHORT_15M | 0 | 7 | 7 | 28,57% | 0,62 | -0,24R | €-16,64 |
| Bilanciata 1H V1 | 19 | 154 | 154 | 34,42% | 1,00 | -0,00R | €-4,00 |
| Bilanciata 1H V2 | 8 | 36 | 32 | 47,22% | 1,73 | 0,39R | €140,18 |
| Bilanciata 1H V3 Filtered | 14 | 61 | 61 | 39,34% | 1,20 | 0,13R | €76,78 |
| Rapida 1H V1 | 15 | 185 | 185 | 39,46% | 0,93 | -0,04R | €-81,63 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | 2 | 11 | 11 | 45,45% | 1,17 | 0,10R | €10,80 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | 13 | 48 | 48 | 43,75% | 1,04 | 0,02R | €10,87 |
| SHADOW_1H_FAST_NO_PEPE_V1 | 14 | 52 | 52 | 40,38% | 0,90 | -0,06R | €-31,79 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | 8 | 35 | 35 | 48,57% | 1,25 | 0,14R | €48,51 |
| SHADOW_1H_FAST_TP2_V1 | 15 | 44 | 44 | 27,27% | 0,67 | -0,25R | €-110,65 |
| Rapida 1H V2 | 3 | 8 | 7 | 25,00% | 0,40 | -0,50R | €-39,89 |
| Rapida 1H V3 Filtered | 11 | 94 | 94 | 42,55% | 1,03 | 0,02R | €16,22 |
| SHADOW_1H_FAST_V3_CAP75_V1 | 9 | 43 | 43 | 41,86% | 0,96 | -0,03R | €-11,08 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | 3 | 22 | 22 | 36,36% | 0,78 | -0,15R | €-32,37 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | 3 | 22 | 22 | 36,36% | 0,78 | -0,15R | €-32,37 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | 3 | 27 | 27 | 29,63% | 0,58 | -0,32R | €-85,41 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | 11 | 49 | 49 | 40,82% | 0,92 | -0,05R | €-24,62 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | 11 | 50 | 50 | 40,00% | 0,89 | -0,07R | €-36,14 |
| SHADOW_4H_WIDE | 21 | 42 | 42 | 26,19% | 0,97 | -0,03R | €-10,68 |
| SHADOW_BOLLINGER_MR_1H | 4 | 38 | 38 | 42,11% | 0,96 | -0,03R | €-9,68 |
| SHADOW_BTC_ADAPTIVE_1H | 1 | 3 | 3 | 0,00% | 0,00 | -1,11R | €-33,33 |
| SHADOW_BTC_ADAPTIVE_4H | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,67 |
| SHADOW_BTC_BOLLINGER_1H | 1 | 2 | 2 | 100,00% | ∞ | 1,37R | €27,33 |
| SHADOW_BTC_BOLLINGER_4H | 0 | 1 | 1 | 100,00% | ∞ | 1,72R | €17,16 |
| SHADOW_BTC_DONCHIAN_1H | 1 | 4 | 4 | 0,00% | 0,00 | -1,12R | €-45,00 |
| SHADOW_BTC_DONCHIAN_4H | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,71 |
| SHADOW_BTC_EMA_1H | 1 | 4 | 4 | 25,00% | 0,57 | -0,36R | €-14,44 |
| SHADOW_BTC_EMA_4H | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,71 |
| SHADOW_COMBO_ADAPTIVE | 18 | 101 | 101 | 37,62% | 1,13 | 0,08R | €82,23 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | 6 | 25 | 25 | 24,00% | 0,58 | -0,33R | €-83,33 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | 18 | 68 | 68 | 35,29% | 1,00 | 0,00R | €0,78 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | 16 | 44 | 44 | 29,55% | 0,76 | -0,18R | €-80,04 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | 2 | 4 | 4 | 25,00% | 0,60 | -0,32R | €-12,77 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | 2 | 4 | 4 | 25,00% | 0,60 | -0,32R | €-12,77 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | 4 | 7 | 7 | 28,57% | 0,75 | -0,19R | €-13,24 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | 6 | 25 | 25 | 16,00% | 0,34 | -0,59R | €-147,47 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | 17 | 30 | 30 | 13,33% | 0,42 | -0,54R | €-161,39 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | 17 | 30 | 30 | 13,33% | 0,42 | -0,54R | €-161,39 |
| SHADOW_COMBO_MEAN_REVERSION | 2 | 16 | 16 | 37,50% | 0,84 | -0,11R | €-16,81 |
| SHADOW_COMBO_SCANNER | 8 | 60 | 60 | 41,67% | 1,42 | 0,26R | €155,36 |
| SHADOW_COMBO_TREND | 20 | 74 | 74 | 32,43% | 0,99 | -0,01R | €-7,52 |
| SHADOW_DOGE_BOLLINGER_1H | 0 | 2 | 2 | 0,00% | 0,00 | -1,12R | €-22,46 |
| SHADOW_DOGE_DONCHIAN_1H | 1 | 2 | 2 | 50,00% | 1,67 | 0,38R | €7,50 |
| SHADOW_DOGE_EMA_1H | 1 | 3 | 3 | 66,67% | 3,40 | 0,89R | €26,67 |
| SHADOW_DONCHIAN_1H | 15 | 41 | 41 | 29,27% | 0,95 | -0,04R | €-16,29 |
| SHADOW_EMA_TREND_1H | 19 | 80 | 80 | 31,25% | 0,97 | -0,02R | €-17,60 |
| SHADOW_ETH_ADAPTIVE_1H | 1 | 4 | 4 | 25,00% | 0,57 | -0,36R | €-14,44 |
| SHADOW_ETH_BOLLINGER_1H | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,33 |
| SHADOW_ETH_DONCHIAN_1H | 1 | 3 | 3 | 33,33% | 0,84 | -0,12R | €-3,61 |
| SHADOW_ETH_EMA_1H | 1 | 4 | 4 | 25,00% | 0,57 | -0,36R | €-14,33 |
| SHADOW_ETH_EMA_4H | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,57 |
| SHADOW_GLOBAL_PURE | 1 | 3 | 3 | 66,67% | 3,47 | 0,91R | €27,17 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | 6 | 21 | 21 | 23,81% | 0,58 | -0,33R | €-70,08 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | 6 | 21 | 21 | 19,05% | 0,44 | -0,47R | €-99,29 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | 6 | 21 | 21 | 19,05% | 0,44 | -0,47R | €-99,14 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | 7 | 14 | 14 | 7,14% | 0,22 | -0,77R | €-108,31 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | 4 | 20 | 20 | 15,00% | 0,33 | -0,59R | €-118,87 |
| SHADOW_MASTER_ADAPTIVE_V1 | 6 | 21 | 21 | 19,05% | 0,44 | -0,47R | €-99,29 |
| Forza relativa 1H V1 | 16 | 108 | 108 | 31,48% | 1,01 | 0,01R | €5,86 |
| Forza relativa 1H V2 | 7 | 38 | 35 | 42,11% | 1,52 | 0,31R | €119,56 |
| SHADOW_SCANNER_BOTTOM5_SHORT | 11 | 40 | 40 | 32,50% | 1,00 | -0,00R | €-0,13 |
| SHADOW_SCANNER_TOP5_BTC | 7 | 59 | 59 | 38,98% | 1,36 | 0,22R | €131,51 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | 5 | 10 | 10 | 30,00% | 0,86 | -0,10R | €-10,17 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | 6 | 18 | 18 | 22,22% | 0,59 | -0,33R | €-59,31 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | 5 | 13 | 13 | 23,08% | 0,64 | -0,28R | €-36,47 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | 5 | 13 | 13 | 23,08% | 0,64 | -0,28R | €-36,47 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | 5 | 16 | 16 | 18,75% | 0,49 | -0,43R | €-69,06 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | 5 | 16 | 16 | 18,75% | 0,49 | -0,43R | €-69,06 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | 7 | 21 | 21 | 23,81% | 0,64 | -0,29R | €-60,19 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | 7 | 14 | 14 | 14,29% | 0,46 | -0,49R | €-68,15 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | 7 | 14 | 14 | 14,29% | 0,46 | -0,49R | €-68,15 |
| SHADOW_SCANNER_TOP5_LONG | 7 | 72 | 72 | 40,28% | 1,28 | 0,17R | €125,68 |
| SHADOW_SOL_ADAPTIVE_1H | 1 | 4 | 4 | 25,00% | 0,57 | -0,36R | €-14,30 |
| SHADOW_SOL_ADAPTIVE_4H | 1 | 1 | 1 | 0,00% | 0,00 | -1,05R | €-10,52 |
| SHADOW_SOL_BOLLINGER_1H | 1 | 2 | 2 | 0,00% | 0,00 | -1,13R | €-22,67 |
| SHADOW_SOL_BOLLINGER_4H | 0 | 1 | 1 | 100,00% | ∞ | 1,74R | €17,38 |
| SHADOW_SOL_DONCHIAN_1H | 0 | 3 | 3 | 33,33% | 0,84 | -0,12R | €-3,58 |
| SHADOW_SOL_DONCHIAN_4H | 1 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,56 |
| SHADOW_SOL_EMA_1H | 1 | 3 | 3 | 33,33% | 0,86 | -0,11R | €-3,18 |
| SHADOW_SOL_EMA_4H | 1 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,56 |

### Matrice strategia × regime all’entrata

| Profilo | Regime entrata | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| MAIN | ALT_ROTATION_DOWN | 3 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| MAIN | ALT_ROTATION_UP | 1 | 5 | 5 | 0,00% | 0,00 | -1,02R | €-51,22 |
| MAIN | RANGE | 6 | 15 | 15 | 26,67% | 0,70 | -0,23R | €-33,95 |
| MAIN | RANGE_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| MAIN | TRANSITION | 1 | 7 | 7 | 42,86% | 1,45 | 0,26R | €18,34 |
| MAIN | TREND_UP | 1 | 16 | 16 | 37,50% | 1,15 | 0,10R | €15,71 |
| MAIN | TREND_UP_HIGH_VOL | 2 | 4 | 4 | 25,00% | 0,64 | -0,28R | €-11,18 |
| RSI_EXTREME_LONG_15M | RANGE | 1 | 6 | 6 | 0,00% | 0,00 | -1,07R | €-64,49 |
| RSI_EXTREME_LONG_15M | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,29R | €12,88 |
| RSI_EXTREME_LONG_15M | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 0,66R | €6,56 |
| RSI_EXTREME_SHORT_15M | ALT_ROTATION_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 1,47R | €14,67 |
| RSI_EXTREME_SHORT_15M | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,90 |
| RSI_EXTREME_SHORT_15M | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -0,41R | €-4,13 |
| RSI_EXTREME_SHORT_15M | TREND_UP | 0 | 4 | 4 | 25,00% | 0,44 | -0,41R | €-16,27 |
| Bilanciata 1H V1 | ALT_ROTATION_DOWN | 4 | 11 | 11 | 27,27% | 0,68 | -0,25R | €-27,27 |
| Bilanciata 1H V1 | ALT_ROTATION_UP | 0 | 14 | 14 | 50,00% | 1,84 | 0,44R | €61,99 |
| Bilanciata 1H V1 | RANGE | 10 | 36 | 36 | 38,89% | 1,22 | 0,13R | €48,60 |
| Bilanciata 1H V1 | RANGE_HIGH_VOL | 0 | 11 | 11 | 0,00% | 0,00 | -1,07R | €-118,08 |
| Bilanciata 1H V1 | TRANSITION | 1 | 29 | 29 | 31,03% | 0,90 | -0,07R | €-19,92 |
| Bilanciata 1H V1 | TREND_UP | 2 | 42 | 42 | 40,48% | 1,31 | 0,19R | €78,29 |
| Bilanciata 1H V1 | TREND_UP_HIGH_VOL | 2 | 11 | 11 | 27,27% | 0,68 | -0,25R | €-27,61 |
| Bilanciata 1H V2 | ALT_ROTATION_UP | 0 | 6 | 5 | 66,67% | 3,52 | 0,92R | €55,11 |
| Bilanciata 1H V2 | RANGE | 4 | 14 | 12 | 42,86% | 1,55 | 0,30R | €41,34 |
| Bilanciata 1H V2 | TRANSITION | 4 | 16 | 15 | 43,75% | 1,46 | 0,27R | €43,74 |
| Bilanciata 1H V3 Filtered | ALT_ROTATION_DOWN | 2 | 10 | 10 | 40,00% | 1,23 | 0,14R | €14,28 |
| Bilanciata 1H V3 Filtered | ALT_ROTATION_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,05R | €-20,99 |
| Bilanciata 1H V3 Filtered | RANGE | 9 | 7 | 7 | 71,43% | 4,75 | 1,09R | €76,18 |
| Bilanciata 1H V3 Filtered | RANGE_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,83 |
| Bilanciata 1H V3 Filtered | TRANSITION | 0 | 8 | 8 | 37,50% | 1,11 | 0,07R | €5,68 |
| Bilanciata 1H V3 Filtered | TREND_UP | 1 | 20 | 20 | 45,00% | 1,54 | 0,31R | €61,36 |
| Bilanciata 1H V3 Filtered | TREND_UP_HIGH_VOL | 2 | 12 | 12 | 25,00% | 0,60 | -0,32R | €-38,90 |
| Rapida 1H V1 | ALT_ROTATION_DOWN | 4 | 18 | 18 | 22,22% | 0,38 | -0,51R | €-91,65 |
| Rapida 1H V1 | ALT_ROTATION_UP | 0 | 13 | 13 | 53,85% | 1,58 | 0,29R | €37,18 |
| Rapida 1H V1 | RANGE | 10 | 49 | 49 | 48,98% | 1,45 | 0,22R | €106,39 |
| Rapida 1H V1 | RANGE_HIGH_VOL | 0 | 11 | 11 | 0,00% | 0,00 | -1,09R | €-119,90 |
| Rapida 1H V1 | TRANSITION | 1 | 25 | 25 | 48,00% | 1,45 | 0,22R | €54,11 |
| Rapida 1H V1 | TREND_UP | 0 | 48 | 48 | 41,67% | 0,97 | -0,02R | €-9,20 |
| Rapida 1H V1 | TREND_UP_HIGH_VOL | 0 | 21 | 21 | 28,57% | 0,59 | -0,28R | €-58,55 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | ALT_ROTATION_DOWN | 1 | 4 | 4 | 0,00% | 0,00 | -1,02R | €-40,63 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,39R | €13,89 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | RANGE | 1 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 1,48R | €29,69 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TREND_UP | 0 | 3 | 3 | 33,33% | 0,68 | -0,23R | €-7,03 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | ALT_ROTATION_DOWN | 2 | 16 | 16 | 25,00% | 0,44 | -0,44R | €-70,04 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,39R | €13,89 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | RANGE | 11 | 13 | 13 | 76,92% | 4,44 | 0,84R | €109,54 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 1,48R | €29,69 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TREND_UP | 0 | 16 | 16 | 25,00% | 0,44 | -0,45R | €-72,21 |
| SHADOW_1H_FAST_NO_PEPE_V1 | ALT_ROTATION_DOWN | 3 | 17 | 17 | 23,53% | 0,41 | -0,47R | €-80,22 |
| SHADOW_1H_FAST_NO_PEPE_V1 | ALT_ROTATION_UP | 0 | 6 | 6 | 50,00% | 1,27 | 0,15R | €8,94 |
| SHADOW_1H_FAST_NO_PEPE_V1 | RANGE | 10 | 13 | 13 | 69,23% | 3,02 | 0,65R | €84,70 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TRANSITION | 1 | 2 | 2 | 100,00% | ∞ | 1,48R | €29,69 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_UP | 0 | 14 | 14 | 21,43% | 0,36 | -0,54R | €-74,90 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | ALT_ROTATION_DOWN | 1 | 11 | 11 | 36,36% | 0,75 | -0,17R | €-18,75 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | ALT_ROTATION_UP | 0 | 4 | 4 | 50,00% | 1,23 | 0,13R | €5,07 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | RANGE | 7 | 11 | 11 | 81,82% | 6,32 | 0,99R | €108,49 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_UP | 0 | 8 | 8 | 12,50% | 0,18 | -0,76R | €-61,17 |
| SHADOW_1H_FAST_TP2_V1 | ALT_ROTATION_DOWN | 5 | 15 | 15 | 13,33% | 0,28 | -0,65R | €-97,70 |
| SHADOW_1H_FAST_TP2_V1 | ALT_ROTATION_UP | 0 | 4 | 4 | 25,00% | 0,55 | -0,37R | €-14,93 |
| SHADOW_1H_FAST_TP2_V1 | RANGE | 8 | 10 | 10 | 50,00% | 1,81 | 0,43R | €42,61 |
| SHADOW_1H_FAST_TP2_V1 | TRANSITION | 2 | 1 | 1 | 100,00% | ∞ | 1,98R | €19,82 |
| SHADOW_1H_FAST_TP2_V1 | TREND_UP | 0 | 14 | 14 | 21,43% | 0,49 | -0,43R | €-60,45 |
| Rapida 1H V2 | ALT_ROTATION_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,10R | €-21,92 |
| Rapida 1H V2 | RANGE | 3 | 5 | 4 | 40,00% | 0,81 | -0,13R | €-6,55 |
| Rapida 1H V2 | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -1,14R | €-11,43 |
| Rapida 1H V3 Filtered | ALT_ROTATION_DOWN | 3 | 19 | 19 | 26,32% | 0,47 | -0,41R | €-77,53 |
| Rapida 1H V3 Filtered | ALT_ROTATION_UP | 0 | 5 | 5 | 60,00% | 1,92 | 0,41R | €20,43 |
| Rapida 1H V3 Filtered | RANGE | 7 | 14 | 14 | 71,43% | 3,40 | 0,72R | €100,66 |
| Rapida 1H V3 Filtered | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| Rapida 1H V3 Filtered | TRANSITION | 1 | 6 | 6 | 50,00% | 1,37 | 0,20R | €12,10 |
| Rapida 1H V3 Filtered | TREND_UP | 0 | 29 | 29 | 48,28% | 1,27 | 0,15R | €43,00 |
| Rapida 1H V3 Filtered | TREND_UP_HIGH_VOL | 0 | 20 | 20 | 25,00% | 0,49 | -0,36R | €-72,31 |
| SHADOW_1H_FAST_V3_CAP75_V1 | ALT_ROTATION_DOWN | 1 | 15 | 15 | 26,67% | 0,48 | -0,40R | €-59,35 |
| SHADOW_1H_FAST_V3_CAP75_V1 | ALT_ROTATION_UP | 0 | 4 | 4 | 50,00% | 1,23 | 0,13R | €5,07 |
| SHADOW_1H_FAST_V3_CAP75_V1 | RANGE | 8 | 12 | 12 | 75,00% | 4,05 | 0,81R | €97,06 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_UP | 0 | 11 | 11 | 18,18% | 0,29 | -0,62R | €-68,73 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | ALT_ROTATION_DOWN | 0 | 6 | 6 | 0,00% | 0,00 | -1,04R | €-62,18 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,39R | €13,89 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | RANGE | 3 | 7 | 7 | 71,43% | 3,63 | 0,77R | €53,71 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TREND_UP | 0 | 7 | 7 | 14,29% | 0,20 | -0,75R | €-52,65 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | ALT_ROTATION_DOWN | 0 | 6 | 6 | 0,00% | 0,00 | -1,04R | €-62,18 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,39R | €13,89 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | RANGE | 3 | 7 | 7 | 71,43% | 3,63 | 0,77R | €53,71 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TREND_UP | 0 | 7 | 7 | 14,29% | 0,20 | -0,75R | €-52,65 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 0 | 8 | 8 | 0,00% | 0,00 | -1,03R | €-82,50 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | ALT_ROTATION_UP | 0 | 4 | 4 | 50,00% | 1,23 | 0,13R | €5,07 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | RANGE | 2 | 8 | 8 | 62,50% | 2,42 | 0,54R | €43,51 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TRANSITION | 1 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_UP | 0 | 6 | 6 | 0,00% | 0,00 | -1,11R | €-66,36 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | ALT_ROTATION_DOWN | 3 | 18 | 18 | 27,78% | 0,51 | -0,37R | €-66,10 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | ALT_ROTATION_UP | 0 | 2 | 2 | 50,00% | 1,27 | 0,15R | €3,00 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | RANGE | 7 | 14 | 14 | 71,43% | 3,40 | 0,72R | €100,66 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TRANSITION | 1 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TREND_UP | 0 | 14 | 14 | 21,43% | 0,35 | -0,55R | €-77,05 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | ALT_ROTATION_DOWN | 3 | 18 | 18 | 27,78% | 0,51 | -0,37R | €-66,10 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | ALT_ROTATION_UP | 0 | 5 | 5 | 40,00% | 0,83 | -0,12R | €-5,83 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | RANGE | 7 | 14 | 14 | 71,43% | 3,40 | 0,72R | €100,66 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TRANSITION | 1 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_UP | 0 | 12 | 12 | 16,67% | 0,26 | -0,66R | €-79,74 |
| SHADOW_4H_WIDE | ALT_ROTATION_DOWN | 4 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_4H_WIDE | ALT_ROTATION_UP | 2 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_4H_WIDE | RANGE | 5 | 16 | 16 | 25,00% | 0,90 | -0,07R | €-11,95 |
| SHADOW_4H_WIDE | TRANSITION | 3 | 7 | 7 | 14,29% | 0,46 | -0,47R | €-33,10 |
| SHADOW_4H_WIDE | TREND_UP | 3 | 13 | 13 | 46,15% | 2,32 | 0,73R | €95,17 |
| SHADOW_4H_WIDE | TREND_UP_HIGH_VOL | 4 | 4 | 4 | 0,00% | 0,00 | -1,01R | €-40,53 |
| SHADOW_BOLLINGER_MR_1H | ALT_ROTATION_DOWN | 0 | 5 | 5 | 60,00% | 1,99 | 0,43R | €21,52 |
| SHADOW_BOLLINGER_MR_1H | ALT_ROTATION_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,02R | €-20,30 |
| SHADOW_BOLLINGER_MR_1H | RANGE | 4 | 13 | 13 | 30,77% | 0,58 | -0,32R | €-41,26 |
| SHADOW_BOLLINGER_MR_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_BOLLINGER_MR_1H | TRANSITION | 0 | 3 | 3 | 33,33% | 0,71 | -0,20R | €-6,14 |
| SHADOW_BOLLINGER_MR_1H | TREND_UP | 0 | 12 | 12 | 50,00% | 1,28 | 0,15R | €18,32 |
| SHADOW_BOLLINGER_MR_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,31 | 0,17R | €3,31 |
| SHADOW_BTC_ADAPTIVE_1H | RANGE | 1 | 2 | 2 | 0,00% | 0,00 | -1,11R | €-22,22 |
| SHADOW_BTC_ADAPTIVE_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_BTC_ADAPTIVE_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,67 |
| SHADOW_BTC_BOLLINGER_1H | RANGE | 1 | 1 | 1 | 100,00% | ∞ | 1,37R | €13,67 |
| SHADOW_BTC_BOLLINGER_1H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,37R | €13,67 |
| SHADOW_BTC_BOLLINGER_4H | ALT_ROTATION_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 1,72R | €17,16 |
| SHADOW_BTC_DONCHIAN_1H | RANGE | 1 | 2 | 2 | 0,00% | 0,00 | -1,12R | €-22,50 |
| SHADOW_BTC_DONCHIAN_1H | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -1,12R | €-11,25 |
| SHADOW_BTC_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_BTC_DONCHIAN_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,71 |
| SHADOW_BTC_EMA_1H | RANGE | 1 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_BTC_EMA_1H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_BTC_EMA_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,70 | 0,39R | €7,78 |
| SHADOW_BTC_EMA_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,71 |
| SHADOW_COMBO_ADAPTIVE | ALT_ROTATION_DOWN | 4 | 11 | 11 | 27,27% | 0,68 | -0,24R | €-26,44 |
| SHADOW_COMBO_ADAPTIVE | ALT_ROTATION_UP | 0 | 6 | 6 | 50,00% | 1,86 | 0,45R | €26,75 |
| SHADOW_COMBO_ADAPTIVE | RANGE | 9 | 24 | 24 | 37,50% | 1,08 | 0,06R | €13,24 |
| SHADOW_COMBO_ADAPTIVE | RANGE_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,83 |
| SHADOW_COMBO_ADAPTIVE | TRANSITION | 1 | 19 | 19 | 42,11% | 1,46 | 0,26R | €49,12 |
| SHADOW_COMBO_ADAPTIVE | TREND_UP | 2 | 29 | 29 | 44,83% | 1,52 | 0,30R | €87,02 |
| SHADOW_COMBO_ADAPTIVE | TREND_UP_HIGH_VOL | 2 | 10 | 10 | 20,00% | 0,46 | -0,47R | €-46,63 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 1 | 4 | 4 | 0,00% | 0,00 | -1,01R | €-40,55 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | ALT_ROTATION_UP | 0 | 4 | 4 | 75,00% | 5,34 | 1,17R | €46,86 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | RANGE | 2 | 5 | 5 | 40,00% | 1,30 | 0,19R | €9,27 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TRANSITION | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_UP | 2 | 6 | 6 | 0,00% | 0,00 | -1,09R | €-65,26 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_UP_HIGH_VOL | 0 | 6 | 6 | 16,67% | 0,36 | -0,56R | €-33,65 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | ALT_ROTATION_DOWN | 4 | 11 | 11 | 27,27% | 0,68 | -0,24R | €-26,44 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | ALT_ROTATION_UP | 0 | 7 | 7 | 42,86% | 1,37 | 0,22R | €15,64 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE | 9 | 12 | 12 | 50,00% | 1,81 | 0,43R | €51,72 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,83 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TRANSITION | 1 | 3 | 3 | 33,33% | 0,87 | -0,09R | €-2,74 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_UP | 2 | 21 | 21 | 42,86% | 1,42 | 0,25R | €52,12 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_UP_HIGH_VOL | 2 | 12 | 12 | 16,67% | 0,36 | -0,57R | €-68,69 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | ALT_ROTATION_DOWN | 4 | 11 | 11 | 27,27% | 0,68 | -0,24R | €-26,44 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | ALT_ROTATION_UP | 0 | 4 | 4 | 75,00% | 5,34 | 1,17R | €46,86 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | RANGE | 9 | 12 | 12 | 50,00% | 1,81 | 0,43R | €51,72 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TRANSITION | 1 | 2 | 2 | 0,00% | 0,00 | -1,09R | €-21,86 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_UP | 2 | 8 | 8 | 0,00% | 0,00 | -1,07R | €-85,56 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_UP_HIGH_VOL | 0 | 7 | 7 | 14,29% | 0,30 | -0,64R | €-44,76 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TRANSITION | 1 | 2 | 2 | 50,00% | 1,77 | 0,42R | €8,42 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TREND_UP | 1 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,18 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TRANSITION | 1 | 2 | 2 | 50,00% | 1,77 | 0,42R | €8,42 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TREND_UP | 1 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,18 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | ALT_ROTATION_DOWN | 2 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,84 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | RANGE | 1 | 3 | 3 | 33,33% | 0,98 | -0,02R | €-0,50 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TRANSITION | 1 | 1 | 1 | 100,00% | ∞ | 1,93R | €19,28 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,18 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TRANSITION | 4 | 4 | 4 | 25,00% | 0,59 | -0,33R | €-13,40 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TREND_UP | 2 | 13 | 13 | 15,38% | 0,33 | -0,60R | €-78,20 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TREND_UP_HIGH_VOL | 0 | 8 | 8 | 12,50% | 0,26 | -0,70R | €-55,87 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_DOWN | 5 | 5 | 5 | 20,00% | 0,67 | -0,29R | €-14,37 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_UP | 0 | 5 | 5 | 40,00% | 1,80 | 0,52R | €26,25 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | RANGE | 10 | 7 | 7 | 14,29% | 0,45 | -0,50R | €-34,82 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | TRANSITION | 0 | 2 | 2 | 0,00% | 0,00 | -1,09R | €-21,86 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | TREND_UP | 2 | 7 | 7 | 0,00% | 0,00 | -1,06R | €-74,11 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 0,00% | 0,00 | -1,06R | €-42,49 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | ALT_ROTATION_DOWN | 5 | 5 | 5 | 20,00% | 0,67 | -0,29R | €-14,37 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | ALT_ROTATION_UP | 0 | 5 | 5 | 40,00% | 1,80 | 0,52R | €26,25 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | RANGE | 10 | 7 | 7 | 14,29% | 0,45 | -0,50R | €-34,82 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | TRANSITION | 0 | 2 | 2 | 0,00% | 0,00 | -1,09R | €-21,86 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | TREND_UP | 2 | 7 | 7 | 0,00% | 0,00 | -1,06R | €-74,11 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 0,00% | 0,00 | -1,06R | €-42,49 |
| SHADOW_COMBO_MEAN_REVERSION | ALT_ROTATION_DOWN | 1 | 3 | 3 | 33,33% | 0,73 | -0,19R | €-5,83 |
| SHADOW_COMBO_MEAN_REVERSION | RANGE | 1 | 8 | 8 | 37,50% | 0,82 | -0,12R | €-9,97 |
| SHADOW_COMBO_MEAN_REVERSION | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,94 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_UP | 0 | 3 | 3 | 33,33% | 0,75 | -0,17R | €-5,09 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,85 |
| SHADOW_COMBO_SCANNER | ALT_ROTATION_DOWN | 1 | 5 | 5 | 0,00% | 0,00 | -1,03R | €-51,66 |
| SHADOW_COMBO_SCANNER | ALT_ROTATION_UP | 0 | 4 | 4 | 50,00% | 2,09 | 0,57R | €22,81 |
| SHADOW_COMBO_SCANNER | RANGE | 3 | 8 | 8 | 50,00% | 2,09 | 0,56R | €44,63 |
| SHADOW_COMBO_SCANNER | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,69 |
| SHADOW_COMBO_SCANNER | TRANSITION | 1 | 14 | 14 | 42,86% | 1,34 | 0,21R | €28,81 |
| SHADOW_COMBO_SCANNER | TREND_UP | 2 | 20 | 20 | 50,00% | 2,04 | 0,55R | €110,63 |
| SHADOW_COMBO_SCANNER | TREND_UP_HIGH_VOL | 1 | 8 | 8 | 37,50% | 1,20 | 0,14R | €10,84 |
| SHADOW_COMBO_TREND | ALT_ROTATION_DOWN | 6 | 6 | 6 | 16,67% | 0,40 | -0,52R | €-31,35 |
| SHADOW_COMBO_TREND | ALT_ROTATION_UP | 0 | 5 | 5 | 40,00% | 1,39 | 0,24R | €12,22 |
| SHADOW_COMBO_TREND | RANGE | 8 | 16 | 16 | 31,25% | 0,93 | -0,05R | €-8,19 |
| SHADOW_COMBO_TREND | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,63 |
| SHADOW_COMBO_TREND | TRANSITION | 2 | 14 | 14 | 42,86% | 1,55 | 0,33R | €46,22 |
| SHADOW_COMBO_TREND | TREND_UP | 2 | 23 | 23 | 34,78% | 1,10 | 0,07R | €15,44 |
| SHADOW_COMBO_TREND | TREND_UP_HIGH_VOL | 2 | 9 | 9 | 22,22% | 0,58 | -0,35R | €-31,22 |
| SHADOW_DOGE_BOLLINGER_1H | RANGE | 0 | 2 | 2 | 0,00% | 0,00 | -1,12R | €-22,46 |
| SHADOW_DOGE_DONCHIAN_1H | RANGE | 1 | 2 | 2 | 50,00% | 1,67 | 0,38R | €7,50 |
| SHADOW_DOGE_EMA_1H | RANGE | 1 | 3 | 3 | 66,67% | 3,40 | 0,89R | €26,67 |
| SHADOW_DONCHIAN_1H | ALT_ROTATION_DOWN | 7 | 4 | 4 | 25,00% | 0,77 | -0,18R | €-7,22 |
| SHADOW_DONCHIAN_1H | ALT_ROTATION_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,85 |
| SHADOW_DONCHIAN_1H | RANGE | 5 | 12 | 12 | 25,00% | 0,76 | -0,19R | €-22,61 |
| SHADOW_DONCHIAN_1H | RANGE_HIGH_VOL | 1 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_DONCHIAN_1H | TRANSITION | 1 | 6 | 6 | 16,67% | 0,45 | -0,48R | €-28,95 |
| SHADOW_DONCHIAN_1H | TREND_UP | 0 | 11 | 11 | 45,45% | 1,89 | 0,53R | €57,82 |
| SHADOW_DONCHIAN_1H | TREND_UP_HIGH_VOL | 1 | 5 | 5 | 40,00% | 1,48 | 0,31R | €15,65 |
| SHADOW_EMA_TREND_1H | ALT_ROTATION_DOWN | 5 | 7 | 7 | 14,29% | 0,34 | -0,60R | €-41,90 |
| SHADOW_EMA_TREND_1H | ALT_ROTATION_UP | 0 | 5 | 5 | 20,00% | 0,52 | -0,40R | €-20,11 |
| SHADOW_EMA_TREND_1H | RANGE | 7 | 16 | 16 | 31,25% | 1,03 | 0,02R | €3,11 |
| SHADOW_EMA_TREND_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,63 |
| SHADOW_EMA_TREND_1H | TRANSITION | 3 | 14 | 14 | 42,86% | 1,55 | 0,33R | €46,21 |
| SHADOW_EMA_TREND_1H | TREND_UP | 2 | 28 | 28 | 32,14% | 1,02 | 0,02R | €4,61 |
| SHADOW_EMA_TREND_1H | TREND_UP_HIGH_VOL | 2 | 9 | 9 | 33,33% | 1,02 | 0,01R | €1,10 |
| SHADOW_ETH_ADAPTIVE_1H | ALT_ROTATION_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_ETH_ADAPTIVE_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_ETH_ADAPTIVE_1H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,89R | €18,89 |
| SHADOW_ETH_ADAPTIVE_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_ETH_BOLLINGER_1H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,33 |
| SHADOW_ETH_DONCHIAN_1H | RANGE | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_ETH_DONCHIAN_1H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_ETH_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,68 | 0,38R | €7,64 |
| SHADOW_ETH_EMA_1H | ALT_ROTATION_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_ETH_EMA_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_ETH_EMA_1H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,89R | €18,89 |
| SHADOW_ETH_EMA_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,10R | €-10,99 |
| SHADOW_ETH_EMA_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,57 |
| SHADOW_GLOBAL_PURE | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,10R | €-11,00 |
| SHADOW_GLOBAL_PURE | RANGE | 1 | 1 | 1 | 100,00% | ∞ | 2,40R | €24,00 |
| SHADOW_GLOBAL_PURE | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,42R | €14,17 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | ALT_ROTATION_DOWN | 2 | 6 | 6 | 16,67% | 0,38 | -0,53R | €-31,80 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,79 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | RANGE | 1 | 4 | 4 | 25,00% | 0,65 | -0,26R | €-10,60 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TRANSITION | 1 | 2 | 2 | 100,00% | ∞ | 1,94R | €38,87 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TREND_UP | 2 | 8 | 8 | 12,50% | 0,26 | -0,70R | €-55,77 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | ALT_ROTATION_DOWN | 2 | 5 | 5 | 20,00% | 0,49 | -0,41R | €-20,68 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,86 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | RANGE | 1 | 5 | 5 | 40,00% | 1,30 | 0,19R | €9,27 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TRANSITION | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TREND_UP | 2 | 10 | 10 | 10,00% | 0,21 | -0,77R | €-77,01 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | ALT_ROTATION_DOWN | 2 | 5 | 5 | 20,00% | 0,49 | -0,41R | €-20,68 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | RANGE | 1 | 5 | 5 | 40,00% | 1,30 | 0,19R | €9,27 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TRANSITION | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TREND_UP | 2 | 11 | 11 | 9,09% | 0,18 | -0,80R | €-87,73 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_DOWN | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,86 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | RANGE | 3 | 3 | 3 | 0,00% | 0,00 | -1,01R | €-30,44 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | TREND_UP | 2 | 10 | 10 | 10,00% | 0,31 | -0,67R | €-67,01 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | ALT_ROTATION_DOWN | 0 | 4 | 4 | 0,00% | 0,00 | -1,01R | €-40,55 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | RANGE | 2 | 6 | 6 | 50,00% | 1,96 | 0,49R | €29,12 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TRANSITION | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TREND_UP | 1 | 10 | 10 | 0,00% | 0,00 | -1,07R | €-107,43 |
| SHADOW_MASTER_ADAPTIVE_V1 | ALT_ROTATION_DOWN | 2 | 5 | 5 | 20,00% | 0,49 | -0,41R | €-20,68 |
| SHADOW_MASTER_ADAPTIVE_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,86 |
| SHADOW_MASTER_ADAPTIVE_V1 | RANGE | 1 | 5 | 5 | 40,00% | 1,30 | 0,19R | €9,27 |
| SHADOW_MASTER_ADAPTIVE_V1 | TRANSITION | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_MASTER_ADAPTIVE_V1 | TREND_UP | 2 | 10 | 10 | 10,00% | 0,21 | -0,77R | €-77,01 |
| Forza relativa 1H V1 | ALT_ROTATION_DOWN | 5 | 7 | 7 | 14,29% | 0,35 | -0,58R | €-40,61 |
| Forza relativa 1H V1 | ALT_ROTATION_UP | 0 | 13 | 13 | 30,77% | 0,90 | -0,07R | €-9,26 |
| Forza relativa 1H V1 | RANGE | 7 | 26 | 26 | 26,92% | 0,80 | -0,15R | €-37,81 |
| Forza relativa 1H V1 | RANGE_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -1,03R | €-31,02 |
| Forza relativa 1H V1 | TRANSITION | 1 | 15 | 15 | 46,67% | 1,84 | 0,46R | €69,26 |
| Forza relativa 1H V1 | TREND_UP | 2 | 36 | 36 | 38,89% | 1,54 | 0,30R | €106,45 |
| Forza relativa 1H V1 | TREND_UP_HIGH_VOL | 1 | 8 | 8 | 12,50% | 0,30 | -0,64R | €-51,15 |
| Forza relativa 1H V2 | ALT_ROTATION_DOWN | 3 | 4 | 4 | 50,00% | 2,08 | 0,55R | €21,84 |
| Forza relativa 1H V2 | ALT_ROTATION_UP | 0 | 4 | 4 | 50,00% | 2,00 | 0,54R | €21,41 |
| Forza relativa 1H V2 | RANGE | 0 | 6 | 6 | 66,67% | 4,31 | 1,12R | €67,19 |
| Forza relativa 1H V2 | TRANSITION | 4 | 9 | 8 | 33,33% | 1,05 | 0,03R | €3,12 |
| Forza relativa 1H V2 | TREND_UP | 0 | 11 | 10 | 45,45% | 1,77 | 0,43R | €47,60 |
| Forza relativa 1H V2 | TREND_UP_HIGH_VOL | 0 | 4 | 3 | 0,00% | 0,00 | -1,04R | €-41,60 |
| SHADOW_SCANNER_BOTTOM5_SHORT | ALT_ROTATION_DOWN | 2 | 4 | 4 | 75,00% | 5,32 | 1,17R | €46,61 |
| SHADOW_SCANNER_BOTTOM5_SHORT | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| SHADOW_SCANNER_BOTTOM5_SHORT | RANGE | 8 | 12 | 12 | 41,67% | 1,25 | 0,16R | €18,82 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TRANSITION | 0 | 14 | 14 | 28,57% | 0,85 | -0,09R | €-13,14 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP | 0 | 7 | 7 | 0,00% | 0,00 | -0,73R | €-51,04 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP_HIGH_VOL | 1 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,24 |
| SHADOW_SCANNER_TOP5_BTC | ALT_ROTATION_DOWN | 1 | 5 | 5 | 0,00% | 0,00 | -1,03R | €-51,66 |
| SHADOW_SCANNER_TOP5_BTC | ALT_ROTATION_UP | 0 | 5 | 5 | 40,00% | 1,39 | 0,25R | €12,28 |
| SHADOW_SCANNER_TOP5_BTC | RANGE | 2 | 9 | 9 | 44,44% | 2,08 | 0,50R | €44,64 |
| SHADOW_SCANNER_TOP5_BTC | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,69 |
| SHADOW_SCANNER_TOP5_BTC | TRANSITION | 1 | 12 | 12 | 41,67% | 1,49 | 0,30R | €36,18 |
| SHADOW_SCANNER_TOP5_BTC | TREND_UP | 2 | 19 | 19 | 47,37% | 1,85 | 0,47R | €89,92 |
| SHADOW_SCANNER_TOP5_BTC | TREND_UP_HIGH_VOL | 1 | 8 | 8 | 37,50% | 1,20 | 0,14R | €10,84 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | ALT_ROTATION_DOWN | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,86 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TRANSITION | 2 | 1 | 1 | 100,00% | ∞ | 2,19R | €21,87 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TREND_UP | 1 | 2 | 2 | 50,00% | 1,97 | 0,54R | €10,76 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TREND_UP_HIGH_VOL | 0 | 6 | 6 | 16,67% | 0,40 | -0,53R | €-31,93 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | ALT_ROTATION_DOWN | 2 | 4 | 4 | 0,00% | 0,00 | -1,01R | €-40,55 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,86 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | RANGE | 2 | 4 | 4 | 25,00% | 0,72 | -0,21R | €-8,60 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TRANSITION | 1 | 1 | 1 | 100,00% | ∞ | 2,19R | €21,87 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_UP | 1 | 2 | 2 | 50,00% | 1,97 | 0,54R | €10,76 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_UP_HIGH_VOL | 0 | 6 | 6 | 16,67% | 0,40 | -0,53R | €-31,93 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | ALT_ROTATION_DOWN | 2 | 4 | 4 | 0,00% | 0,00 | -1,01R | €-40,55 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,79 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | RANGE | 2 | 4 | 4 | 25,00% | 0,72 | -0,21R | €-8,60 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TRANSITION | 1 | 1 | 1 | 100,00% | ∞ | 2,19R | €21,87 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 2,19R | €21,87 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | ALT_ROTATION_DOWN | 2 | 4 | 4 | 0,00% | 0,00 | -1,01R | €-40,55 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,79 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | RANGE | 2 | 4 | 4 | 25,00% | 0,72 | -0,21R | €-8,60 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TRANSITION | 1 | 1 | 1 | 100,00% | ∞ | 2,19R | €21,87 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 2,19R | €21,87 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | ALT_ROTATION_DOWN | 1 | 5 | 5 | 0,00% | 0,00 | -1,03R | €-51,66 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,79 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | RANGE | 2 | 4 | 4 | 25,00% | 0,72 | -0,21R | €-8,60 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TRANSITION | 1 | 1 | 1 | 100,00% | ∞ | 2,19R | €21,87 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_UP | 1 | 3 | 3 | 33,33% | 1,02 | 0,01R | €0,39 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | ALT_ROTATION_DOWN | 1 | 5 | 5 | 0,00% | 0,00 | -1,03R | €-51,66 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,79 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | RANGE | 2 | 4 | 4 | 25,00% | 0,72 | -0,21R | €-8,60 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TRANSITION | 1 | 1 | 1 | 100,00% | ∞ | 2,19R | €21,87 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_UP | 1 | 3 | 3 | 33,33% | 1,02 | 0,01R | €0,39 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | ALT_ROTATION_DOWN | 1 | 5 | 5 | 0,00% | 0,00 | -1,03R | €-51,66 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,79 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | RANGE | 2 | 4 | 4 | 25,00% | 0,72 | -0,21R | €-8,60 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TRANSITION | 1 | 1 | 1 | 100,00% | ∞ | 2,19R | €21,87 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_UP | 2 | 2 | 2 | 50,00% | 1,97 | 0,54R | €10,76 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_UP_HIGH_VOL | 1 | 8 | 8 | 25,00% | 0,66 | -0,27R | €-21,76 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | ALT_ROTATION_UP | 0 | 4 | 4 | 25,00% | 0,89 | -0,09R | €-3,61 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | RANGE | 3 | 3 | 3 | 0,00% | 0,00 | -1,02R | €-30,46 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 2,99R | €29,87 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_UP | 3 | 3 | 3 | 0,00% | 0,00 | -1,09R | €-32,57 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -1,05R | €-31,38 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | ALT_ROTATION_UP | 0 | 4 | 4 | 25,00% | 0,89 | -0,09R | €-3,61 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | RANGE | 3 | 3 | 3 | 0,00% | 0,00 | -1,02R | €-30,46 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 2,99R | €29,87 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_UP | 3 | 3 | 3 | 0,00% | 0,00 | -1,09R | €-32,57 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -1,05R | €-31,38 |
| SHADOW_SCANNER_TOP5_LONG | ALT_ROTATION_DOWN | 1 | 6 | 6 | 0,00% | 0,00 | -1,05R | €-62,77 |
| SHADOW_SCANNER_TOP5_LONG | ALT_ROTATION_UP | 0 | 6 | 6 | 33,33% | 0,92 | -0,06R | €-3,32 |
| SHADOW_SCANNER_TOP5_LONG | RANGE | 2 | 10 | 10 | 50,00% | 2,36 | 0,57R | €56,51 |
| SHADOW_SCANNER_TOP5_LONG | RANGE_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,83 |
| SHADOW_SCANNER_TOP5_LONG | TRANSITION | 1 | 12 | 12 | 41,67% | 1,36 | 0,22R | €26,18 |
| SHADOW_SCANNER_TOP5_LONG | TREND_UP | 2 | 28 | 28 | 50,00% | 1,84 | 0,45R | €125,56 |
| SHADOW_SCANNER_TOP5_LONG | TREND_UP_HIGH_VOL | 1 | 8 | 8 | 37,50% | 1,08 | 0,05R | €4,35 |
| SHADOW_SOL_ADAPTIVE_1H | RANGE | 1 | 2 | 2 | 0,00% | 0,00 | -1,11R | €-22,22 |
| SHADOW_SOL_ADAPTIVE_1H | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,89R | €18,89 |
| SHADOW_SOL_ADAPTIVE_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,10R | €-10,96 |
| SHADOW_SOL_ADAPTIVE_4H | RANGE | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SOL_ADAPTIVE_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,05R | €-10,52 |
| SHADOW_SOL_BOLLINGER_1H | RANGE | 1 | 2 | 2 | 0,00% | 0,00 | -1,13R | €-22,67 |
| SHADOW_SOL_BOLLINGER_4H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,74R | €17,38 |
| SHADOW_SOL_DONCHIAN_1H | RANGE | 0 | 2 | 2 | 50,00% | 1,67 | 0,38R | €7,50 |
| SHADOW_SOL_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,08 |
| SHADOW_SOL_DONCHIAN_4H | RANGE | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SOL_DONCHIAN_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,56 |
| SHADOW_SOL_EMA_1H | RANGE | 1 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_SOL_EMA_1H | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,89R | €18,89 |
| SHADOW_SOL_EMA_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,10R | €-10,96 |
| SHADOW_SOL_EMA_4H | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SOL_EMA_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,56 |

Il P&L è normalizzato a **€10 di rischio per evento**, così leva e size non falsano il confronto.
La matrice diventerà utilizzabile per una rotazione automatica soltanto dopo un campione sufficiente per ciascuna coppia strategia-regime.

# Block 3 — Shadow Exit Engine

Generato: 2026-07-24T17:53:41+00:00

> Motore esclusivamente osservativo e Paper-only. Non modifica le uscite reali. I confronti escludono il funding sia dall'uscita originale sia dalle varianti.

## Stato operativo

- Gruppi di trade ancora monitorati: **369**
- Scenari virtuali ancora attivi: **2883**
- Gruppi in attesa dell'uscita originale: **178**
- Gruppi con originale chiuso ma Shadow ancora attive: **191**
- Confronti completati: **17231**

## Classifica osservativa complessiva

| Scenario | Campione completo | Campione totale | Δ medio vs originale | Migliora | Troppo presto | Troppo tardi | Stato dati |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| GB20_R050 | 826 | 889 | +€6,03 | 49,9% | 234 | 1 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R050 | 826 | 889 | +€3,90 | 48,8% | 239 | 8 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R050 | 826 | 889 | +€1,61 | 47,6% | 245 | 13 | READY_FOR_BLOCK4_EVALUATION |
| TP_R050 | 826 | 889 | +€0,70 | 47,7% | 257 | 0 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R050 | 821 | 884 | +€0,31 | 46,0% | 239 | 27 | READY_FOR_BLOCK4_EVALUATION |
| TP_R100 | 820 | 883 | +€2,96 | 42,2% | 214 | 23 | READY_FOR_BLOCK4_EVALUATION |
| GB20_R100 | 819 | 882 | +€4,97 | 43,8% | 200 | 23 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R100 | 819 | 882 | +€2,93 | 43,8% | 188 | 35 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R100 | 817 | 880 | +€1,63 | 43,4% | 164 | 59 | READY_FOR_BLOCK4_EVALUATION |
| TIME_6H | 816 | 879 | €-1,18 | 48,7% | 209 | 113 | READY_FOR_BLOCK4_EVALUATION |
| TIME_12H | 813 | 876 | €-0,82 | 43,6% | 115 | 191 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R100 | 809 | 872 | +€1,02 | 40,5% | 125 | 116 | READY_FOR_BLOCK4_EVALUATION |
| ATR15_R100 | 807 | 870 | €-2,96 | 34,8% | 83 | 178 | READY_FOR_BLOCK4_EVALUATION |
| TP_R150 | 790 | 853 | +€2,56 | 32,8% | 99 | 91 | READY_FOR_BLOCK4_EVALUATION |
| ATR20_R100 | 789 | 852 | €-6,60 | 29,0% | 67 | 223 | READY_FOR_BLOCK4_EVALUATION |
| TIME_24H | 769 | 832 | €-3,63 | 35,8% | 66 | 217 | READY_FOR_BLOCK4_EVALUATION |
| ATR30_R100 | 761 | 824 | €-10,98 | 25,8% | 62 | 220 | READY_FOR_BLOCK4_EVALUATION |
| BE_R050 | 759 | 822 | €-11,22 | 28,2% | 156 | 139 | READY_FOR_BLOCK4_EVALUATION |
| TP_R200 | 749 | 812 | +€1,18 | 37,6% | 53 | 136 | READY_FOR_BLOCK4_EVALUATION |
| BE_R100 | 709 | 772 | €-17,81 | 20,7% | 61 | 218 | READY_FOR_BLOCK4_EVALUATION |

## Come leggere il controllo

- **EARLIER_BETTER**: la variante è uscita prima e ha conservato più profitto.
- **TOO_EARLY**: la variante è uscita prima ma ha tagliato un movimento migliore.
- **LATER_BETTER**: la variante ha continuato dopo l'uscita originale e ha guadagnato di più.
- **TOO_LATE**: la variante è rimasta aperta più a lungo e ha peggiorato il risultato.

## Limiti e protezioni

Le regole Shadow mantengono entrata, quantità, commissioni, stop protettivo iniziale e liquidazione. Le ambiguità all'interno della stessa candela vengono risolte scegliendo l'esito peggiore. Le posizioni già aperte al momento dell'installazione sono marcate come campione parziale e non saranno utilizzate dal futuro Blocco 4 come prova piena.

# Blocco 4 — Valutazione statistica Shadow

Generato: 2026-07-24T17:53:42+00:00

> Modulo esclusivamente valutativo. Non modifica strategie, uscite, posizioni o capitale. Le candidature vengono consegnate al futuro Blocco 5, senza applicazione automatica.

## Stato

- Risultati Block 3 disponibili: **17231**
- Valutazioni prodotte: **5039**
- Candidature al Blocco 5: **0**
- Mutazioni create automaticamente: **0**

## Classifica complessiva

| Scenario | Campione pieno | Δ medio (R) | Mediana (R) | CI bootstrap basso | Migliora | Score | Stato |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| GB20_R050 | 178 | 0,311 | 0,322 | 0,191 | 70,8% | 94,9 | VALIDATING |
| TP_R100 | 178 | 0,267 | 0,269 | 0,139 | 69,1% | 94,8 | VALIDATING |
| GB20_R100 | 177 | 0,293 | 0,287 | 0,160 | 69,5% | 94,8 | VALIDATING |
| GB30_R050 | 178 | 0,255 | 0,279 | 0,145 | 70,8% | 94,8 | VALIDATING |
| GB30_R100 | 177 | 0,244 | 0,258 | 0,122 | 71,2% | 94,8 | VALIDATING |
| GB40_R100 | 176 | 0,187 | 0,248 | 0,074 | 69,3% | 94,7 | VALIDATING |
| GB40_R050 | 178 | 0,195 | 0,229 | 0,087 | 69,1% | 94,7 | VALIDATING |
| GB50_R100 | 173 | 0,139 | 0,258 | 0,014 | 68,8% | 94,7 | VALIDATING |
| GB50_R050 | 177 | 0,184 | 0,213 | 0,087 | 68,4% | 94,5 | VALIDATING |
| TP_R050 | 178 | 0,143 | 0,264 | 0,041 | 69,1% | 93,3 | VALIDATING |
| TIME_24H | 6 | 0,997 | 1,104 | 0,180 | 66,7% | 74,1 | INSUFFICIENT_DATA |
| TP_R200 | 136 | 0,043 | 0,104 | -0,141 | 57,4% | 71,3 | VALIDATING |
| GB20_R050 | 642 | 0,096 | 0,000 | 0,032 | 45,3% | 70,0 | VALIDATING |
| TP_R150 | 626 | 0,065 | 0,000 | 0,015 | 28,1% | 69,8 | VALIDATING |
| GB20_R100 | 636 | 0,069 | 0,000 | 0,023 | 37,3% | 69,7 | VALIDATING |
| TP_R150 | 158 | 0,081 | 0,046 | -0,065 | 53,2% | 69,3 | VALIDATING |
| GB30_R050 | 642 | 0,056 | 0,000 | -0,010 | 43,8% | 68,5 | VALIDATING |
| GB30_R100 | 636 | 0,031 | 0,000 | -0,021 | 36,9% | 61,9 | VALIDATING |
| TP_R100 | 636 | 0,036 | 0,000 | -0,018 | 35,1% | 60,2 | VALIDATING |
| TP_R200 | 6 | 0,472 | 0,250 | -0,017 | 50,0% | 58,7 | INSUFFICIENT_DATA |

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

Generato: 2026-07-24T17:53:53+00:00

Questi profili sono osservativi e Paper-only. Usano gli stessi trade della madre, ma applicano una specifica uscita Block 3 soltanto ai segnali aperti dopo la loro registrazione.
Nessuna promozione, modifica live o operazione reale viene eseguita automaticamente.

| Challenger | Madre | Scenario | Chiusi | Copertura | PF | PnL | Exp/trade | DD | Stato |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Rapida 1H V1 — giveback 20% dopo +0,5R | SHADOW_1H_FAST | GB20_R050 | 12 | 100,00% | 1,23 | +€58,60 | +€4,88 | 1,14% | COLLECTING |
| Rapida 1H V1 — giveback 30% dopo +0,5R | SHADOW_1H_FAST | GB30_R050 | 12 | 100,00% | 1,06 | +€16,50 | +€1,37 | 1,19% | COLLECTING |
| Relative Strength — giveback 20% dopo +0,5R | SHADOW_RELATIVE_STRENGTH | GB20_R050 | 3 | 100,00% | 1,26 | +€13,93 | +€4,64 | 0,54% | COLLECTING |
| Relative Strength — giveback 30% dopo +0,5R | SHADOW_RELATIVE_STRENGTH | GB30_R050 | 3 | 100,00% | 1,08 | +€4,49 | +€1,50 | 0,54% | COLLECTING |

## Regole di valutazione

- Prima fotografia a 30 trade indipendenti.
- Revisione per possibile promozione a 50 trade indipendenti.
- PF minimo 1,50, expectancy e PnL positivi, drawdown massimo 15%, copertura minima 90%.
- PF deve superare la madre e il drawdown non deve essere peggiore sulla stessa serie di trade.
- La promozione resta una decisione umana protetta; il rollback viene predisposto soltanto in fase di approvazione.

# Blocco 4.5 — Crash Cascade Guard

Generato: 2026-07-24T17:53:34+00:00

> Paper-only. In mercato NORMAL/WATCH non riduce i segnali. Le limitazioni iniziano soltanto in STRESS, RECOVERY, CRASH, EXTREME o con dati non affidabili.

## Stato corrente

- Livello: **NORMAL**
- Direzione: **NONE**
- Segnali bloccati nel ciclo: **0**
- Simulazioni bloccate attive: **0**
- Simulazioni completate nel ciclo: **0**
- Liquidazioni virtuali evitate totali: **0**
- Valore cumulato del filtro: **-21.28 R**
- Profitto virtuale mancato: **77.89 R**

## Stress test portafogli Paper

| Scenario | Posizioni interessate | Liquidazioni stimate | Perdita stimata EUR |
| --- | ---: | ---: | ---: |
| DOWN_10 | 122 | 0 | 13255.39 |
| DOWN_20 | 122 | 0 | 26510.77 |
| DOWN_30 | 122 | 0 | 39766.16 |
| DOWN_40 | 122 | 28 | 50079.68 |
| UP_10 | 56 | 0 | 15049.43 |
| UP_20 | 56 | 0 | 30098.85 |
| UP_30 | 56 | 0 | 45148.28 |
| UP_40 | 56 | 31 | 53491.88 |

## Modello di esecuzione

Se una candela di cascata attraversa nello stesso intervallo sia lo stop sia il prezzo di liquidazione, il Paper usa il caso peggiore e registra una liquidazione intrabar. Gli stop in gap o in regime di stress ricevono slippage aggiuntivo.

## Requisiti prima del live futures

- modalità ISOLATED obbligatoria;
- stop nativo sull'exchange;
- conferma dello stop prima di accettare la posizione;
- cross margin vietato.

# Blocco 5 — Candidati evolutivi controllati

Generato: 2026-07-24T17:53:13+00:00

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

Generato: 2026-07-24T17:53:53+00:00

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

Generato: 2026-07-24T17:53:53+00:00

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

Generato: 2026-07-24T17:53:53+00:00

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

Generato: 2026-07-24T17:53:53+00:00

> Paper-only. La memoria può bloccare soltanto una futura proposta Block 5 classificata AVOID; non modifica strategie esistenti.

## Stato

- Strategie/portafogli valutati: **92**
- Hall of Fame: **11**
- Memorie genetiche: **0**
- Firme bloccate: **0**
- Azioni automatiche e live: **0**

## Hall of Fame

| Rank | Strategia | Stato | Score | Grade | Trade | PF | Expectancy R | DD R |
| ---: | --- | --- | ---: | --- | ---: | ---: | ---: | ---: |
| 1 | SHADOW_SCANNER_TOP5_LONG | BASELINE | 20.2 | E | 30 | 2.21 | 0.412 | 5.75 |
| 2 | SHADOW_1H_BALANCED | BASELINE | 15.5 | E | 37 | 1.48 | 0.184 | 4.17 |
| 3 | SHADOW_1H_FAST_SCORE_6_75_V1 | BASELINE | 14.3 | E | 32 | 1.49 | 0.177 | 3.71 |
| 4 | SHADOW_1H_BALANCED_V3 | BASELINE | 13.8 | E | 33 | 1.36 | 0.174 | 3.23 |
| 5 | SHADOW_1H_FAST_V3 | BASELINE | 11.4 | E | 59 | 1.09 | 0.036 | 5.36 |
| 6 | SHADOW_1H_FAST_NOHIGH_CAP75_V1 | BASELINE | 10.4 | E | 31 | 1.18 | 0.084 | 5.40 |
| 7 | SHADOW_RELATIVE_STRENGTH_V2 | BASELINE | 9.7 | E | 33 | 1.18 | 0.101 | 6.62 |
| 8 | SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | BASELINE | 7.7 | E | 31 | 0.96 | -0.016 | 3.68 |
| 9 | SHADOW_1H_FAST | BASELINE | 7.6 | E | 67 | 0.92 | -0.036 | 13.48 |
| 10 | SHADOW_1H_FAST_V3_NOHIGH_V1 | BASELINE | 6.8 | E | 32 | 0.93 | -0.034 | 5.53 |

## Memoria genetica

| Scope | Famiglia | Mutazione | Target | Stato | Score | Prove | Coppie | Blocco |
| --- | --- | --- | --- | --- | ---: | ---: | ---: | --- |
| — | — | Nessuna candidata ancora creata | — | INSUFFICIENT | 0 | 0 | 0 | NO |

## Sicurezza

- Nessuna strategia, posizione o promozione esistente viene modificata.
- Nessuna mutazione, promozione, pensionamento o rollback automatico.
- Nessun effetto live e nessun ordine reale.

# Blocco 10 — Regime Fitness e specializzazione

Generato: 2026-07-24T17:53:53+00:00

> Paper-only e advisory. Il blocco misura quali strategie funzionano nei diversi regimi, ma non cambia automaticamente strategia o posizione.

## Stato

- Regime corrente: **RANGE**
- Righe di performance: **326**
- Strategie preferite nel regime corrente: **0**
- Strategie da evitare nel regime corrente: **1**
- Memorie contestuali: **163**
- Routing automatico: **NO**

## Classifica del regime corrente

| Rank | Portafoglio | Famiglia | Stato | Fitness | Trade | PF | Expectancy R | DD R |
| ---: | --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| 1 | SHADOW_BTC_BOLLINGER_1H | shadow-btc-bollinger-1h | INSUFFICIENT | 80.8 | 2 | 99.00 | 0.997 | 0.00 |
| 2 | SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | shadow-scanner-top5-btc-guard-btc-le3-v1 | INSUFFICIENT | 80.8 | 2 | 99.00 | 1.186 | 0.00 |
| 3 | SHADOW_SOL_BOLLINGER_4H | shadow-sol-bollinger-4h | INSUFFICIENT | 80.4 | 1 | 99.00 | 1.740 | 0.00 |
| 4 | SHADOW_BTC_BOLLINGER_4H | shadow-btc-bollinger-4h | INSUFFICIENT | 80.4 | 1 | 99.00 | 1.682 | 0.00 |
| 5 | SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | shadow-scanner-top5-btc-btc-le3-v1 | INSUFFICIENT | 80.3 | 1 | 99.00 | 0.398 | 0.00 |
| 6 | SHADOW_DOGE_DONCHIAN_1H | shadow-doge-donchian-1h | INSUFFICIENT | 80.1 | 3 | 99.00 | 0.374 | 0.00 |
| 7 | SHADOW_COMBO_ADAPTIVE | shadow-combo-adaptive | OBSERVING | 79.5 | 20 | 2.19 | 0.325 | 1.10 |
| 8 | SHADOW_DOGE_EMA_1H | shadow-doge-ema-1h | INSUFFICIENT | 78.2 | 6 | 4.73 | 0.683 | 1.10 |
| 9 | SHADOW_ETH_BOLLINGER_1H | shadow-eth-bollinger-1h | INSUFFICIENT | 76.6 | 1 | 99.00 | 0.309 | 0.00 |
| 10 | SHADOW_SCANNER_TOP5_LONG | shadow-scanner-top5-long | OBSERVING | 74.4 | 22 | 1.96 | 0.371 | 4.17 |

## Sicurezza

- Il regime viene assegnato usando solo l'ultimo record noto prima dell'entrata del trade.
- Nessun uso di dati futuri per classificare il trade.
- Il Candidate Regime Gate è advisory per impostazione predefinita.
- Nessun cambio automatico di MASTER, posizione o live.

# Blocco 11 — Collegamento protetto al live

Generato: 2026-07-24T17:53:53+00:00

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

Generato: 2026-07-24T17:53:34+00:00

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
