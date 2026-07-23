# Paper trading automatico KuCoin

Generato: 2026-07-23T19:53:53+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-07-23T19:53:25+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-07-23T19:53:25+00:00 | 2026-07-23T19:53:25+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-07-23T19:30:00+00:00 | 2026-07-23T19:30:00+00:00 | 8,5 min | 25,0 min | OK |
| 60m | 12 | 2026-07-23T18:00:00+00:00 | 2026-07-23T18:00:00+00:00 | 53,5 min | 45,0 min | STALE_CANDLE |
| 240m | 12 | 2026-07-23T12:00:00+00:00 | 2026-07-23T12:00:00+00:00 | 3,89 h | 1,00 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | DOGE | 240m | SHORT | -10,00 | 6,00 | 0,00 | STALE_CANDLE | 3,89 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 233.5 minuti; tolleranza 60 minuti. |
| Principale 4H | AKE | 240m | LONG | 9,25 | 6,00 | 0,00 | STALE_CANDLE | 3,89 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 233.5 minuti; tolleranza 60 minuti. |
| Principale 4H | BANK | 240m | LONG | 7,75 | 6,00 | 0,00 | STALE_CANDLE | 3,89 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 233.5 minuti; tolleranza 60 minuti. |
| Principale 4H | TAO | 240m | SHORT | -6,54 | 6,00 | 0,00 | STALE_CANDLE | 3,89 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 233.5 minuti; tolleranza 60 minuti. |
| Principale 4H | HYPE | 240m | SHORT | -5,00 | 6,00 | 1,00 | STALE_CANDLE | 3,89 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 233.5 minuti; tolleranza 60 minuti. |
| Principale 4H | SOL | 240m | SHORT | -2,57 | 6,00 | 3,43 | STALE_CANDLE | 3,89 h | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 233.5 minuti; tolleranza 60 minuti. |
| Principale 4H | BTC | 240m | SHORT | -2,25 | 6,00 | 3,75 | STALE_CANDLE | 3,89 h | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 233.5 minuti; tolleranza 60 minuti. |
| Principale 4H | ZEC | 240m | SHORT | -2,16 | 6,00 | 3,84 | STALE_CANDLE | 3,89 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 233.5 minuti; tolleranza 60 minuti. |
| Principale 4H | PEPE | 240m | SHORT | -1,67 | 6,00 | 4,33 | STALE_CANDLE | 3,89 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 233.5 minuti; tolleranza 60 minuti. |
| Principale 4H | XRP | 240m | SHORT | -1,22 | 6,00 | 4,78 | STALE_CANDLE | 3,89 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 233.5 minuti; tolleranza 60 minuti. |
| Principale 4H | RIF | 240m | LONG | 0,75 | 6,00 | 5,25 | STALE_CANDLE | 3,89 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 233.5 minuti; tolleranza 60 minuti. |
| Principale 4H | ETH | 240m | LONG | 0,57 | 6,00 | 5,43 | STALE_CANDLE | 3,89 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 233.5 minuti; tolleranza 60 minuti. |
| Ampia 4H | DOGE | 240m | SHORT | -10,00 | 5,00 | 0,00 | STALE_CANDLE | 3,89 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 233.5 minuti; tolleranza 60 minuti. |
| Ampia 4H | AKE | 240m | LONG | 9,25 | 5,00 | 0,00 | STALE_CANDLE | 3,89 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 233.5 minuti; tolleranza 60 minuti. |
| Ampia 4H | BANK | 240m | LONG | 7,75 | 5,00 | 0,00 | STALE_CANDLE | 3,89 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 233.5 minuti; tolleranza 60 minuti. |
| Bilanciata 1H V1 | BANK | 60m | LONG | 7,00 | 5,00 | 0,00 | STALE_CANDLE | 53,5 min | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 53.5 minuti; tolleranza 45 minuti. |
| Bilanciata 1H V2 | BANK | 60m | LONG | 7,00 | 5,50 | 0,00 | STALE_CANDLE | 53,5 min | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 53.5 minuti; tolleranza 45 minuti. |
| Bilanciata 1H V3 Filtered | BANK | 60m | LONG | 7,00 | 6,00 | 0,00 | STALE_CANDLE | 53,5 min | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 53.5 minuti; tolleranza 45 minuti. |
| Rapida 1H V1 — madre | BANK | 60m | LONG | 7,00 | 4,50 | 0,00 | STALE_CANDLE | 53,5 min | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 53.5 minuti; tolleranza 45 minuti. |
| Rapida V1 — score 6–7,5 | BANK | 60m | LONG | 7,00 | 6,00 | 0,00 | STALE_CANDLE | 53,5 min | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 53.5 minuti; tolleranza 45 minuti. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.954,19 | -0,46% | €-45,81 | €3.000,00 | -1,53% | 4 | 18 | 33,33% | 0,91 | 4,26% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 18 | 417 | CAMPIONE INSUFFICIENTE | 30 (mancano 12) |

- Trade del Principale 4H chiusi: **18**; win rate **33,33%**; profit factor **0,91**.
- Expectancy: **€-2,94** per trade; P&L netto: **€-52,87**; max drawdown: **4,26%**.
- Valutazione: **Servono altri eventi indipendenti prima di trarre conclusioni.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 4 | €9.954,19 | €1.462,87 | €4.388,60 | €148,39 | €8,98 |
| TEST | Scanner Top 5 Long 1H | 3 | €10.596,81 | €1.268,81 | €2.537,62 | €158,46 | €-19,38 |
| TEST | Bilanciata 1H V1 | 4 | €10.378,09 | €2.468,00 | €7.404,00 | €204,31 | €88,19 |
| TEST | Scanner Top 5 + forza BTC 1H | 3 | €10.351,32 | €1.330,98 | €2.661,95 | €156,07 | €-7,28 |
| TEST | Combo Adaptive — madre | 3 | €10.309,82 | €2.169,96 | €4.339,92 | €153,94 | €72,08 |
| TEST | Bilanciata 1H V3 Filtered | 4 | €10.303,67 | €2.604,86 | €7.814,57 | €153,49 | €82,66 |
| TEST | Benchmark Donchian breakout 1H | 3 | €10.264,50 | €3.555,00 | €7.109,99 | €152,79 | €109,94 |
| TEST | Forza relativa 1H V2 | 4 | €10.253,51 | €1.814,75 | €3.629,50 | €102,03 | €89,03 |
| TEST | Rapida V1 — score 6–7,5 | 4 | €10.223,13 | €3.898,43 | €11.695,30 | €200,81 | €110,97 |
| TEST | Rapida 1H V3 Filtered — madre | 3 | €10.165,49 | €2.394,18 | €7.182,54 | €151,14 | €3,73 |
| TEST | Doge Ema 1H | 1 | €10.157,63 | €1.173,45 | €3.520,36 | €50,69 | €21,10 |
| TEST | Combo Scanner | 3 | €10.135,09 | €2.818,85 | €5.637,69 | €150,23 | €21,02 |
| TEST | Rapida V1 — senza PEPE | 4 | €10.121,74 | €3.279,84 | €9.839,52 | €99,86 | €138,90 |
| TEST | Benchmark Bollinger mean reversion 1H | 2 | €10.115,43 | €4.026,08 | €8.052,15 | €96,63 | €-36,49 |
| TEST | Top 5 + BTC — target pieno 3R | 3 | €10.111,12 | €1.281,30 | €2.562,59 | €150,64 | €-18,54 |
| TEST | Bilanciata 1H V2 | 4 | €10.107,94 | €2.219,92 | €6.659,76 | €149,98 | €59,79 |
| TEST | Rapida V3 — score <7,5 | 4 | €10.105,58 | €3.319,82 | €9.959,47 | €199,36 | €70,63 |
| TEST | Btc Bollinger 1H | 0 | €10.099,96 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 — senza ESPORTS | 4 | €10.073,97 | €3.312,27 | €9.936,82 | €198,80 | €77,48 |
| TEST | Sol Bollinger 4H | 1 | €10.072,04 | €968,56 | €1.937,11 | €0,00 | €73,63 |
| TEST | Btc Bollinger 4H | 1 | €10.070,93 | €1.313,84 | €2.627,69 | €0,00 | €74,58 |
| TEST | Top 5 + BTC — 75% a 2,2R + runner 3R | 3 | €10.065,01 | €1.280,33 | €2.560,66 | €150,41 | €-18,46 |
| TEST | Combo Adaptive — Quality7 | 3 | €10.051,00 | €2.176,87 | €4.353,75 | €99,74 | €56,69 |
| TEST | Rapida V3 — no volatilità HIGH | 4 | €10.046,78 | €3.300,38 | €9.901,14 | €198,06 | €77,27 |
| TEST | Combo Adaptive — target pieno 3R | 3 | €10.041,72 | €2.339,93 | €4.679,86 | €99,65 | €79,63 |
| TEST | Benchmark trend following EMA 1H | 3 | €10.031,19 | €2.181,37 | €4.362,74 | €149,06 | €85,55 |
| TEST | Ampia 4H | 4 | €10.030,30 | €2.235,83 | €4.471,66 | €151,27 | €-56,39 |
| TEST | Rapida V1 — no HIGH + score <7,5 | 4 | €10.030,02 | €3.283,52 | €9.850,57 | €148,57 | €93,75 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €10.028,40 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Bollinger 1H | 0 | €10.015,45 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Donchian 1H | 1 | €10.014,24 | €1.095,98 | €3.287,94 | €49,99 | €18,77 |
| TEST | Rapida V1 — target pieno 2R | 4 | €10.011,13 | €3.281,90 | €9.845,69 | €148,78 | €100,54 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 0 | €10.005,68 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Donchian 1H | 1 | €10.004,21 | €1.301,74 | €3.905,22 | €49,99 | €9,18 |
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
| TEST | Scalp RSI Long 15 · €10 · 15x | 0 | €9.998,50 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €50 · 15x | 0 | €9.992,50 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V2 | 1 | €9.990,07 | €1.485,87 | €4.457,60 | €49,93 | €15,43 |
| TEST | Combo Adaptive — Trend/Transition | 3 | €9.989,63 | €2.075,49 | €4.150,97 | €98,78 | €75,25 |
| TEST | Scalp RSI Long 15 · prudente · 5x | 0 | €9.988,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 1H | 1 | €9.986,99 | €1.156,05 | €3.468,15 | €49,94 | €0,81 |
| TEST | Eth Donchian 1H | 0 | €9.982,54 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 0 | €9.980,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 4H | 1 | €9.978,17 | €1.105,63 | €2.211,26 | €50,00 | €-24,07 |
| TEST | Btc Donchian 4H | 1 | €9.978,17 | €1.105,63 | €2.211,26 | €50,00 | €-24,07 |
| TEST | Forza relativa 1H V1 | 4 | €9.976,51 | €2.404,07 | €4.808,14 | €148,58 | €51,37 |
| TEST | Combo Mean Reversion | 2 | €9.969,75 | €3.924,92 | €7.849,84 | €98,30 | €-57,44 |
| TEST | Top 5 + BTC — Guard + BTC≤3 | 3 | €9.968,76 | €1.284,68 | €2.569,36 | €148,68 | €-18,23 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.964,86 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 4H | 1 | €9.954,46 | €1.047,40 | €2.094,81 | €50,00 | €-46,64 |
| TEST | Rapida V1 — Long + BTC 1–3 + score <7,5 | 1 | €9.954,22 | €783,06 | €2.349,19 | €50,00 | €0,00 |
| TEST | Combo Adaptive — 75% a 2R + runner 3R | 3 | €9.949,47 | €2.338,03 | €4.676,07 | €99,44 | €61,35 |
| TEST | Top 5 + BTC — BTC 2–3 | 2 | €9.948,72 | €1.092,52 | €2.185,03 | €100,07 | €0,00 |
| TEST | Btc Donchian 1H | 1 | €9.948,68 | €1.293,96 | €3.881,87 | €49,69 | €13,43 |
| TEST | Sol Adaptive 4H | 0 | €9.948,17 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 4H | 0 | €9.948,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Donchian 4H | 0 | €9.948,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Ema 4H | 0 | €9.947,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 1H | 1 | €9.943,38 | €1.150,16 | €3.450,47 | €49,69 | €8,11 |
| TEST | Top 5 + BTC — BTC≤3 | 3 | €9.941,48 | €1.299,81 | €2.599,63 | €149,82 | €-6,99 |
| TEST | Btc Ema 1H | 1 | €9.939,55 | €1.149,81 | €3.449,44 | €49,67 | €7,23 |
| TEST | Rapida 1H V1 — madre | 3 | €9.935,84 | €2.348,91 | €7.046,73 | €148,27 | €3,69 |
| TEST | Sol Bollinger 1H | 1 | €9.930,33 | €1.381,14 | €4.143,42 | €49,72 | €-11,39 |
| TEST | Doge Bollinger 1H | 1 | €9.915,24 | €1.381,14 | €4.143,42 | €49,72 | €-26,48 |
| TEST | Combo Adaptive — Quality7 + Regime | 2 | €9.913,65 | €1.973,66 | €3.947,32 | €49,61 | €75,14 |
| TEST | Combo Adaptive — Quality7 + Regime + parziale 1R | 2 | €9.912,80 | €1.418,97 | €2.837,93 | €49,61 | €37,57 |
| TEST | Eth Adaptive 1H | 0 | €9.907,79 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 1H | 1 | €9.889,23 | €1.149,09 | €3.447,26 | €49,64 | €-36,79 |
| TEST | Combo Adaptive — parziale 1R | 3 | €9.880,37 | €1.619,63 | €3.239,25 | €98,61 | €35,70 |
| TEST | Global Confluence puro 1H | 1 | €9.866,58 | €1.539,06 | €3.078,12 | €49,25 | €18,45 |
| TEST | Combo Adaptive — Long Only | 2 | €9.865,72 | €1.099,22 | €2.198,44 | €98,72 | €0,00 |
| TEST | Combo Trend | 2 | €9.852,38 | €415,30 | €830,60 | €99,67 | €-21,11 |
| TEST | Scanner Bottom 5 Short 1H | 3 | €9.843,81 | €2.992,04 | €5.984,07 | €48,75 | €92,65 |
| TEST | Rapida V3 — Long Only | 3 | €9.842,41 | €446,82 | €1.340,47 | €148,36 | €-25,82 |
| TEST | Top 5 + BTC — solo MFE | 3 | €9.837,80 | €2.554,89 | €5.109,79 | €149,29 | €-21,08 |
| TEST | Eth Ema 1H | 0 | €9.835,26 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Top 5 + BTC — Guard + BTC≤3 + MFE | 3 | €9.827,49 | €1.283,31 | €2.566,61 | €148,35 | €-28,76 |
| TEST | Top 5 + BTC — Guard | 3 | €9.805,68 | €1.163,48 | €2.326,96 | €146,77 | €-17,94 |
| TEST | Master Adaptive Expanded V1 | 3 | €9.759,43 | €1.240,15 | €2.480,31 | €146,90 | €-10,67 |
| TEST | Rapida V3 — Long + no HIGH + score <7,5 | 3 | €9.757,08 | €443,54 | €1.330,62 | €147,27 | €-25,60 |
| TEST | Master Adaptive V1 | 3 | €9.720,23 | €1.239,48 | €2.478,96 | €146,74 | €-6,84 |
| TEST | Master Adaptive No Alt V1 | 3 | €9.720,23 | €1.239,48 | €2.478,96 | €146,74 | €-6,84 |
| TEST | Master Adaptive Runner25 V1 | 3 | €9.720,23 | €1.239,48 | €2.478,96 | €146,74 | €-6,84 |
| TEST | Rapida V3 — qualità completa + profit lock | 3 | €9.718,02 | €440,85 | €1.322,54 | €146,37 | €-25,49 |
| TEST | Top 5 + BTC — Guard + MFE | 3 | €9.715,91 | €1.164,19 | €2.328,38 | €146,94 | €-28,43 |
| TEST | Combo Adaptive — MFE Trail esistente | 3 | €9.681,02 | €1.149,02 | €2.298,05 | €96,76 | €0,00 |
| TEST | Master Adaptive Gb20 V1 | 3 | €9.641,23 | €1.255,53 | €2.511,06 | €146,49 | €-38,69 |
| TEST | Master Adaptive Strict3 V1 | 3 | €9.629,23 | €1.290,58 | €2.581,16 | €145,87 | €1,59 |

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
| PRINCIPALE | Principale 4H | Confluenza trend | €9.954,19 | €-52,87 | 18 | 18 | 33,33% | 0,91 | €-2,94 | 4,26% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.596,81 | €617,80 | 29 | 29 | 51,72% | 2,16 | €21,30 | 2,70% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €10.378,09 | €293,37 | 35 | 35 | 48,57% | 1,40 | €8,38 | 2,30% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €10.351,32 | €360,50 | 21 | 21 | 47,62% | 1,91 | €17,17 | 2,01% |
| TEST | Combo Adaptive — madre | Combo Adaptive | €10.309,82 | €239,35 | 20 | 20 | 45,00% | 1,71 | €11,97 | 1,31% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €10.303,67 | €224,50 | 30 | 30 | 43,33% | 1,28 | €7,48 | 2,20% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €10.264,50 | €157,56 | 17 | 17 | 47,06% | 1,40 | €9,27 | 2,12% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €10.253,51 | €166,10 | 25 | 24 | 36,00% | 1,23 | €6,64 | 3,69% |
| TEST | Rapida V1 — score 6–7,5 | Momentum / breakout | €10.223,13 | €119,21 | 23 | 23 | 39,13% | 1,27 | €5,18 | 2,49% |
| TEST | Rapida 1H V3 Filtered — madre | Momentum / breakout V3 Filtered | €10.165,49 | €165,67 | 52 | 52 | 36,54% | 1,17 | €3,19 | 2,89% |
| TEST | Doge Ema 1H | Trend following EMA | €10.157,63 | €138,64 | 6 | 6 | 66,67% | 2,24 | €23,11 | 1,36% |
| TEST | Combo Scanner | Combo Scanner | €10.135,09 | €117,73 | 23 | 23 | 43,48% | 1,20 | €5,12 | 2,66% |
| TEST | Rapida V1 — senza PEPE | Momentum / breakout | €10.121,74 | €-12,32 | 19 | 19 | 31,58% | 0,97 | €-0,65 | 2,10% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €10.115,43 | €156,75 | 24 | 24 | 45,83% | 1,35 | €6,53 | 2,06% |
| TEST | Top 5 + BTC — target pieno 3R | Scanner Top 5 + forza BTC | €10.111,12 | €131,49 | 7 | 7 | 57,14% | 1,81 | €18,78 | 2,33% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €10.107,94 | €51,43 | 22 | 20 | 50,00% | 1,10 | €2,34 | 2,75% |
| TEST | Rapida V3 — score <7,5 | Momentum / breakout V3 Filtered | €10.105,58 | €40,55 | 20 | 20 | 35,00% | 1,09 | €2,03 | 2,49% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.099,96 | €99,96 | 2 | 2 | 100,00% | ∞ | €49,98 | 0,31% |
| TEST | Rapida V3 — senza ESPORTS | Momentum / breakout V3 Filtered | €10.073,97 | €2,07 | 23 | 23 | 34,78% | 1,00 | €0,09 | 2,49% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €10.072,04 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,40% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.070,93 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,27% |
| TEST | Top 5 + BTC — 75% a 2,2R + runner 3R | Scanner Top 5 + forza BTC | €10.065,01 | €85,30 | 7 | 7 | 57,14% | 1,52 | €12,19 | 2,33% |
| TEST | Combo Adaptive — Quality7 | Combo Adaptive | €10.051,00 | €-3,97 | 4 | 4 | 50,00% | 0,96 | €-0,99 | 1,51% |
| TEST | Rapida V3 — no volatilità HIGH | Momentum / breakout V3 Filtered | €10.046,78 | €-24,92 | 24 | 24 | 37,50% | 0,96 | €-1,04 | 2,96% |
| TEST | Combo Adaptive — target pieno 3R | Combo Adaptive | €10.041,72 | €-35,63 | 8 | 8 | 50,00% | 0,83 | €-4,45 | 1,41% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €10.031,19 | €-52,14 | 15 | 15 | 33,33% | 0,88 | €-3,48 | 2,25% |
| TEST | Ampia 4H | Confluenza trend | €10.030,30 | €88,72 | 12 | 12 | 25,00% | 1,27 | €7,39 | 2,56% |
| TEST | Rapida V1 — no HIGH + score <7,5 | Momentum / breakout | €10.030,02 | €-58,05 | 25 | 25 | 36,00% | 0,91 | €-2,32 | 2,83% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €10.028,40 | €28,40 | 6 | 6 | 33,33% | 1,98 | €4,73 | 0,25% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €10.015,45 | €15,45 | 1 | 1 | 100,00% | ∞ | €15,45 | 0,51% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €10.014,24 | €-2,55 | 3 | 3 | 66,67% | 0,96 | €-0,85 | 0,96% |
| TEST | Rapida V1 — target pieno 2R | Momentum / breakout | €10.011,13 | €-83,74 | 20 | 20 | 30,00% | 0,83 | €-4,19 | 2,58% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €10.005,68 | €5,68 | 6 | 6 | 33,33% | 1,98 | €0,95 | 0,05% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €10.004,21 | €-2,63 | 2 | 2 | 50,00% | 0,41 | €-1,31 | 0,58% |
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
| TEST | Scalp RSI Long 15 · €10 · 15x | Inversione RSI estrema 15m | €9.998,50 | €-1,50 | 1 | 1 | 0,00% | 0,00 | €-1,50 | 0,02% |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | €9.992,50 | €-7,50 | 1 | 1 | 0,00% | 0,00 | €-7,50 | 0,11% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €9.990,07 | €-22,68 | 6 | 5 | 33,33% | 0,82 | €-3,78 | 1,33% |
| TEST | Combo Adaptive — Trend/Transition | Combo Adaptive | €9.989,63 | €-83,93 | 8 | 8 | 37,50% | 0,70 | €-10,49 | 2,18% |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | €9.988,38 | €-11,62 | 1 | 1 | 0,00% | 0,00 | €-11,62 | 0,17% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €9.986,99 | €-11,74 | 2 | 2 | 50,00% | 0,78 | €-5,87 | 0,89% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.982,54 | €-17,46 | 3 | 3 | 33,33% | 0,84 | €-5,82 | 1,38% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €9.980,00 | €-20,00 | 4 | 4 | 25,00% | 0,22 | €-5,00 | 0,34% |
| TEST | Btc Ema 4H | Trend following EMA | €9.978,17 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,68% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €9.978,17 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,68% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €9.976,51 | €-72,58 | 22 | 22 | 27,27% | 0,83 | €-3,30 | 3,25% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €9.969,75 | €31,90 | 10 | 10 | 40,00% | 1,12 | €3,19 | 2,26% |
| TEST | Top 5 + BTC — Guard + BTC≤3 | Scanner Top 5 + forza BTC | €9.968,76 | €-11,09 | 3 | 3 | 33,33% | 0,91 | €-3,70 | 1,64% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.964,86 | €-35,14 | 6 | 6 | 16,67% | 0,18 | €-5,86 | 0,36% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €9.954,46 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,64% |
| TEST | Rapida V1 — Long + BTC 1–3 + score <7,5 | Momentum / breakout | €9.954,22 | €-44,37 | 6 | 6 | 16,67% | 0,62 | €-7,40 | 1,55% |
| TEST | Combo Adaptive — 75% a 2R + runner 3R | Combo Adaptive | €9.949,47 | €-109,80 | 11 | 11 | 36,36% | 0,71 | €-9,98 | 2,12% |
| TEST | Top 5 + BTC — BTC 2–3 | Scanner Top 5 + forza BTC | €9.948,72 | €-49,59 | 3 | 3 | 33,33% | 0,54 | €-16,53 | 2,17% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €9.948,68 | €-62,42 | 3 | 3 | 33,33% | 0,43 | €-20,81 | 1,49% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €9.948,17 | €-51,83 | 1 | 1 | 0,00% | 0,00 | €-51,83 | 0,54% |
| TEST | Sol Ema 4H | Trend following EMA | €9.948,00 | €-52,00 | 1 | 1 | 0,00% | 0,00 | €-52,00 | 0,56% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €9.948,00 | €-52,00 | 1 | 1 | 0,00% | 0,00 | €-52,00 | 0,56% |
| TEST | Eth Ema 4H | Trend following EMA | €9.947,12 | €-52,88 | 1 | 1 | 0,00% | 0,00 | €-52,88 | 0,68% |
| TEST | Sol Ema 1H | Trend following EMA | €9.943,38 | €-62,66 | 3 | 3 | 33,33% | 0,42 | €-20,89 | 1,49% |
| TEST | Top 5 + BTC — BTC≤3 | Scanner Top 5 + forza BTC | €9.941,48 | €-49,59 | 3 | 3 | 33,33% | 0,54 | €-16,53 | 2,20% |
| TEST | Btc Ema 1H | Trend following EMA | €9.939,55 | €-65,61 | 4 | 4 | 25,00% | 0,60 | €-16,40 | 1,56% |
| TEST | Rapida 1H V1 — madre | Momentum / breakout | €9.935,84 | €-64,02 | 60 | 60 | 33,33% | 0,95 | €-1,07 | 6,76% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.930,33 | €-55,79 | 1 | 1 | 0,00% | 0,00 | €-55,79 | 0,75% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €9.915,24 | €-55,79 | 1 | 1 | 0,00% | 0,00 | €-55,79 | 0,92% |
| TEST | Combo Adaptive — Quality7 + Regime | Combo Adaptive | €9.913,65 | €-160,00 | 3 | 3 | 0,00% | 0,00 | €-53,33 | 1,95% |
| TEST | Combo Adaptive — Quality7 + Regime + parziale 1R | Combo Adaptive | €9.912,80 | €-160,00 | 3 | 3 | 0,00% | 0,00 | €-53,33 | 1,95% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.907,79 | €-92,21 | 4 | 4 | 50,00% | 0,16 | €-23,05 | 1,03% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €9.889,23 | €-71,90 | 3 | 3 | 33,33% | 0,34 | €-23,97 | 1,81% |
| TEST | Combo Adaptive — parziale 1R | Combo Adaptive | €9.880,37 | €-187,92 | 10 | 10 | 30,00% | 0,51 | €-18,79 | 2,24% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.866,58 | €-150,03 | 8 | 8 | 37,50% | 0,45 | €-18,75 | 2,92% |
| TEST | Combo Adaptive — Long Only | Combo Adaptive | €9.865,72 | €-132,59 | 5 | 5 | 20,00% | 0,42 | €-26,52 | 2,34% |
| TEST | Combo Trend | Combo Trend | €9.852,38 | €-126,00 | 22 | 22 | 27,27% | 0,81 | €-5,73 | 3,58% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.843,81 | €-245,68 | 21 | 21 | 28,57% | 0,57 | €-11,70 | 5,48% |
| TEST | Rapida V3 — Long Only | Momentum / breakout V3 Filtered | €9.842,41 | €-130,94 | 15 | 15 | 26,67% | 0,68 | €-8,73 | 2,58% |
| TEST | Top 5 + BTC — solo MFE | Scanner Top 5 + forza BTC | €9.837,80 | €-138,36 | 8 | 8 | 25,00% | 0,26 | €-17,30 | 2,51% |
| TEST | Eth Ema 1H | Trend following EMA | €9.835,26 | €-164,74 | 6 | 6 | 33,33% | 0,25 | €-27,46 | 1,67% |
| TEST | Top 5 + BTC — Guard + BTC≤3 + MFE | Scanner Top 5 + forza BTC | €9.827,49 | €-142,22 | 8 | 8 | 25,00% | 0,46 | €-17,78 | 2,30% |
| TEST | Top 5 + BTC — Guard | Scanner Top 5 + forza BTC | €9.805,68 | €-174,75 | 6 | 6 | 16,67% | 0,38 | €-29,13 | 3,31% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €9.759,43 | €-227,96 | 7 | 7 | 14,29% | 0,29 | €-32,57 | 2,80% |
| TEST | Rapida V3 — Long + no HIGH + score <7,5 | Momentum / breakout V3 Filtered | €9.757,08 | €-216,50 | 13 | 13 | 30,77% | 0,50 | €-16,65 | 2,77% |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | €9.720,23 | €-271,00 | 5 | 5 | 0,00% | 0,00 | €-54,20 | 3,19% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €9.720,23 | €-271,00 | 5 | 5 | 0,00% | 0,00 | €-54,20 | 3,19% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €9.720,23 | €-271,00 | 5 | 5 | 0,00% | 0,00 | €-54,20 | 3,19% |
| TEST | Rapida V3 — qualità completa + profit lock | Momentum / breakout V3 Filtered | €9.718,02 | €-255,67 | 13 | 13 | 38,46% | 0,47 | €-19,67 | 3,16% |
| TEST | Top 5 + BTC — Guard + MFE | Scanner Top 5 + forza BTC | €9.715,91 | €-254,40 | 11 | 11 | 18,18% | 0,32 | €-23,13 | 3,47% |
| TEST | Combo Adaptive — MFE Trail esistente | Combo Adaptive | €9.681,02 | €-317,53 | 27 | 27 | 25,93% | 0,45 | €-11,76 | 4,11% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €9.641,23 | €-318,57 | 18 | 18 | 44,44% | 0,33 | €-17,70 | 3,86% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €9.629,23 | €-370,65 | 9 | 9 | 11,11% | 0,21 | €-41,18 | 3,91% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | LAB | SHORT | Confluenza trend | 240m | 3,0x | 0,17841 | 0,17841 | 0,17841 | 0,23699 | 0,13559 | €136,26 | €408,77 | €0,00 | €-0,00 |
| Principale 4H | SUI | LONG | Confluenza trend | 240m | 3,0x | 0,76296 | 0,76296 | 0,73998 | 0,51245 | 0,80891 | €547,52 | €1.642,56 | €49,46 | €0,00 |
| Principale 4H | ONDO | LONG | Confluenza trend | 240m | 3,0x | 0,40344 | 0,40344 | 0,37762 | 0,27098 | 0,45509 | €254,70 | €764,09 | €48,91 | €0,00 |
| Principale 4H | DOGE | SHORT | Confluenza trend | 240m | 3,0x | 0,06940 | 0,06900 | 0,07160 | 0,09218 | 0,06498 | €524,39 | €1.573,18 | €50,01 | €8,98 |
| Bilanciata 1H V1 | ONDO | LONG | Confluenza trend | 60m | 3,0x | 0,39694 | 0,39694 | 0,38539 | 0,26661 | 0,42004 | €581,76 | €1.745,29 | €50,78 | €0,00 |
| Bilanciata 1H V1 | ZEC | SHORT | Confluenza trend | 60m | 3,0x | 514,40710 | 498,03000 | 526,37866 | 683,30410 | 490,46397 | €731,22 | €2.193,66 | €51,05 | €69,84 |
| Bilanciata 1H V1 | BANK | LONG | Confluenza trend | 60m | 3,0x | 0,25232 | 0,24955 | 0,22204 | 0,16948 | 0,31288 | €141,48 | €424,43 | €50,93 | €-4,66 |
| Bilanciata 1H V1 | DOGE | SHORT | Confluenza trend | 60m | 3,0x | 0,06953 | 0,06900 | 0,07070 | 0,09235 | 0,06717 | €1.013,54 | €3.040,62 | €51,54 | €23,01 |
| Bilanciata 1H V2 | ESPORTS | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,02164 | 0,02164 | 0,02164 | 0,02874 | 0,01644 | €138,69 | €416,06 | €0,00 | €-0,00 |
| Bilanciata 1H V2 | ZEC | SHORT | Confluenza trend V2 | 60m | 3,0x | 512,43749 | 498,03000 | 523,41700 | 680,68780 | 490,47847 | €780,12 | €2.340,36 | €50,14 | €65,80 |
| Bilanciata 1H V2 | BANK | LONG | Confluenza trend V2 | 60m | 3,0x | 0,25388 | 0,24955 | 0,22342 | 0,17052 | 0,31481 | €137,71 | €413,13 | €49,58 | €-7,05 |
| Bilanciata 1H V2 | BTC | SHORT | Confluenza trend V2 | 60m | 3,0x | 64717,76386 | 64698,50000 | 65649,69966 | 85966,76299 | 62853,89226 | €1.163,40 | €3.490,20 | €50,26 | €1,04 |
| Bilanciata 1H V3 Filtered | ESPORTS | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,02126 | 0,02126 | 0,02126 | 0,02823 | 0,01615 | €141,51 | €424,52 | €0,00 | €-0,00 |
| Bilanciata 1H V3 Filtered | ONDO | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,40134 | 0,40134 | 0,38898 | 0,26957 | 0,42605 | €557,59 | €1.672,77 | €51,50 | €0,00 |
| Bilanciata 1H V3 Filtered | ZEC | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 514,40710 | 498,03000 | 526,37866 | 683,30410 | 490,46397 | €738,63 | €2.215,89 | €51,57 | €70,55 |
| Bilanciata 1H V3 Filtered | BTC | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 64923,19276 | 64698,50000 | 65858,08674 | 86239,64105 | 63053,40481 | €1.167,13 | €3.501,39 | €50,42 | €12,12 |
| Rapida 1H V1 — madre | ONDO | LONG | Momentum / breakout | 60m | 3,0x | 0,39924 | 0,39924 | 0,38995 | 0,26816 | 0,41318 | €708,01 | €2.124,02 | €49,43 | €0,00 |
| Rapida 1H V1 — madre | DOGE | SHORT | Momentum / breakout | 60m | 3,0x | 0,06942 | 0,06900 | 0,07019 | 0,09221 | 0,06825 | €1.468,34 | €4.405,01 | €49,34 | €26,41 |
| Rapida 1H V1 — madre | BANK | LONG | Momentum / breakout | 60m | 3,0x | 0,26100 | 0,24955 | 0,23604 | 0,17531 | 0,29844 | €172,56 | €517,69 | €49,51 | €-22,72 |
| Rapida V1 — score 6–7,5 | BANK | LONG | Momentum / breakout | 60m | 3,0x | 0,25017 | 0,24955 | 0,22200 | 0,16803 | 0,29242 | €146,51 | €439,52 | €49,49 | €-1,09 |
| Rapida V1 — score 6–7,5 | BTC | SHORT | Momentum / breakout | 60m | 3,0x | 65079,58148 | 64698,50000 | 65808,47279 | 86447,37740 | 63986,24451 | €1.483,09 | €4.449,28 | €49,83 | €26,05 |
| Rapida V1 — score 6–7,5 | DOGE | SHORT | Momentum / breakout | 60m | 3,0x | 0,06953 | 0,06900 | 0,07044 | 0,09235 | 0,06815 | €1.281,83 | €3.845,50 | €50,70 | €29,10 |
| Rapida V1 — score 6–7,5 | ZEC | SHORT | Momentum / breakout | 60m | 3,0x | 507,78842 | 498,03000 | 516,49964 | 674,51229 | 494,72159 | €987,00 | €2.960,99 | €50,80 | €56,90 |
| Rapida V1 — no HIGH + score <7,5 | ONDO | LONG | Momentum / breakout | 60m | 3,0x | 0,39924 | 0,39924 | 0,38995 | 0,26816 | 0,41318 | €704,39 | €2.113,17 | €49,18 | €0,00 |
| Rapida V1 — no HIGH + score <7,5 | BANK | LONG | Momentum / breakout | 60m | 3,0x | 0,23652 | 0,24955 | 0,23652 | 0,15886 | 0,27909 | €136,51 | €409,52 | €0,00 | €22,57 |
| Rapida V1 — no HIGH + score <7,5 | BTC | SHORT | Momentum / breakout | 60m | 3,0x | 64923,19276 | 64698,50000 | 65650,33252 | 86239,64105 | 63832,48313 | €1.473,17 | €4.419,52 | €49,50 | €15,30 |
| Rapida V1 — no HIGH + score <7,5 | ZEC | SHORT | Momentum / breakout | 60m | 3,0x | 507,78842 | 498,03000 | 516,49964 | 674,51229 | 494,72159 | €969,46 | €2.908,37 | €49,89 | €55,89 |
| Rapida V1 — Long + BTC 1–3 + score <7,5 | ONDO | LONG | Momentum / breakout | 60m | 3,0x | 0,39694 | 0,39694 | 0,38849 | 0,26661 | 0,40961 | €783,06 | €2.349,19 | €50,00 | €0,00 |
| Rapida V1 — senza PEPE | ONDO | LONG | Momentum / breakout | 60m | 3,0x | 0,39924 | 0,39924 | 0,38995 | 0,26816 | 0,41318 | €713,68 | €2.141,05 | €49,83 | €0,00 |
| Rapida V1 — senza PEPE | ZEC | SHORT | Momentum / breakout | 60m | 3,0x | 515,14695 | 498,03000 | 505,64588 | 684,28687 | 501,36109 | €935,01 | €2.805,03 | €0,00 | €93,20 |
| Rapida V1 — senza PEPE | BANK | LONG | Momentum / breakout | 60m | 3,0x | 0,23895 | 0,24955 | 0,23895 | 0,16049 | 0,28080 | €142,10 | €426,29 | €0,00 | €18,91 |
| Rapida V1 — senza PEPE | DOGE | SHORT | Momentum / breakout | 60m | 3,0x | 0,06942 | 0,06900 | 0,07019 | 0,09221 | 0,06825 | €1.489,05 | €4.467,14 | €50,03 | €26,78 |
| Rapida V1 — target pieno 2R | ONDO | LONG | Momentum / breakout | 60m | 3,0x | 0,39924 | 0,39924 | 0,38995 | 0,26816 | 0,41782 | €712,92 | €2.138,77 | €49,77 | €0,00 |
| Rapida V1 — target pieno 2R | BANK | LONG | Momentum / breakout | 60m | 3,0x | 0,23652 | 0,24955 | 0,23652 | 0,15886 | 0,29328 | €136,61 | €409,83 | €0,00 | €22,58 |
| Rapida V1 — target pieno 2R | DOGE | SHORT | Momentum / breakout | 60m | 3,0x | 0,06942 | 0,06900 | 0,07019 | 0,09221 | 0,06786 | €1.465,23 | €4.395,69 | €49,23 | €26,35 |
| Rapida V1 — target pieno 2R | ZEC | SHORT | Momentum / breakout | 60m | 3,0x | 507,04857 | 498,03000 | 515,74710 | 673,52952 | 489,65151 | €967,14 | €2.901,41 | €49,77 | €51,61 |
| Rapida 1H V2 | BTC | SHORT | Momentum / breakout V2 | 60m | 3,0x | 64923,19276 | 64698,50000 | 65650,33252 | 86239,64105 | 63832,48313 | €1.485,87 | €4.457,60 | €49,93 | €15,43 |
| Rapida 1H V3 Filtered — madre | ONDO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,39924 | 0,39924 | 0,38995 | 0,26816 | 0,41318 | €715,14 | €2.145,42 | €49,93 | €0,00 |
| Rapida 1H V3 Filtered — madre | DOGE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,06942 | 0,06900 | 0,07019 | 0,09221 | 0,06825 | €1.502,17 | €4.506,50 | €50,47 | €27,01 |
| Rapida 1H V3 Filtered — madre | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,26100 | 0,24955 | 0,23604 | 0,17531 | 0,29844 | €176,87 | €530,62 | €50,74 | €-23,28 |
| Rapida V3 — score <7,5 | ONDO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,39924 | 0,39924 | 0,38995 | 0,26816 | 0,41318 | €712,28 | €2.136,85 | €49,73 | €0,00 |
| Rapida V3 — score <7,5 | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,25017 | 0,24955 | 0,22200 | 0,16803 | 0,29242 | €146,51 | €439,52 | €49,49 | €-1,09 |
| Rapida V3 — score <7,5 | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 64923,19276 | 64698,50000 | 65650,33252 | 86239,64105 | 63832,48313 | €1.484,27 | €4.452,81 | €49,87 | €15,41 |
| Rapida V3 — score <7,5 | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 507,78842 | 498,03000 | 516,49964 | 674,51229 | 494,72159 | €976,76 | €2.930,29 | €50,27 | €56,31 |
| Rapida V3 — no volatilità HIGH | ONDO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,39924 | 0,39924 | 0,38995 | 0,26816 | 0,41318 | €707,41 | €2.122,22 | €49,39 | €0,00 |
| Rapida V3 — no volatilità HIGH | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,25017 | 0,24955 | 0,22200 | 0,16803 | 0,29242 | €145,33 | €435,98 | €49,09 | €-1,08 |
| Rapida V3 — no volatilità HIGH | DOGE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,06942 | 0,06900 | 0,07019 | 0,09221 | 0,06825 | €1.477,08 | €4.431,24 | €49,63 | €26,56 |
| Rapida V3 — no volatilità HIGH | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 507,04857 | 498,03000 | 515,74710 | 673,52952 | 494,00078 | €970,57 | €2.911,70 | €49,95 | €51,79 |
| Rapida V3 — Long Only | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,25017 | 0,24955 | 0,22200 | 0,16803 | 0,29242 | €146,49 | €439,47 | €49,48 | €-1,09 |
| Rapida V3 — Long Only | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00231 | 0,00219 | 0,00207 | 0,00155 | 0,00266 | €163,01 | €489,03 | €49,44 | €-25,09 |
| Rapida V3 — Long Only | RIF | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,10272 | 0,10281 | 0,09039 | 0,06899 | 0,12121 | €137,33 | €411,98 | €49,44 | €0,36 |
| Rapida V3 — Long + no HIGH + score <7,5 | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,25017 | 0,24955 | 0,22200 | 0,16803 | 0,29242 | €145,81 | €437,42 | €49,25 | €-1,08 |
| Rapida V3 — Long + no HIGH + score <7,5 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00231 | 0,00219 | 0,00207 | 0,00155 | 0,00266 | €161,60 | €484,79 | €49,01 | €-24,88 |
| Rapida V3 — Long + no HIGH + score <7,5 | RIF | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,10272 | 0,10281 | 0,09039 | 0,06899 | 0,12121 | €136,14 | €408,41 | €49,01 | €0,36 |
| Rapida V3 — senza ESPORTS | ONDO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,39924 | 0,39924 | 0,38995 | 0,26816 | 0,41318 | €712,28 | €2.136,85 | €49,73 | €0,00 |
| Rapida V3 — senza ESPORTS | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,25017 | 0,24955 | 0,22200 | 0,16803 | 0,29242 | €145,72 | €437,16 | €49,22 | €-1,08 |
| Rapida V3 — senza ESPORTS | DOGE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,06942 | 0,06900 | 0,07019 | 0,09221 | 0,06825 | €1.481,08 | €4.443,23 | €49,76 | €26,63 |
| Rapida V3 — senza ESPORTS | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 507,04857 | 498,03000 | 515,74710 | 673,52952 | 494,00078 | €973,19 | €2.919,58 | €50,09 | €51,93 |
| Rapida V3 — qualità completa + profit lock | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,25017 | 0,24955 | 0,22200 | 0,16803 | 0,29242 | €144,31 | €432,93 | €48,75 | €-1,07 |
| Rapida V3 — qualità completa + profit lock | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00231 | 0,00219 | 0,00207 | 0,00155 | 0,00266 | €160,95 | €482,84 | €48,81 | €-24,78 |
| Rapida V3 — qualità completa + profit lock | RIF | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,10272 | 0,10281 | 0,09039 | 0,06899 | 0,12121 | €135,59 | €406,77 | €48,81 | €0,36 |
| Ampia 4H | DOGE | SHORT | Confluenza trend | 240m | 2,0x | 0,07237 | 0,06900 | 0,07105 | 0,10819 | 0,06457 | €649,49 | €1.298,97 | €0,00 | €60,43 |
| Ampia 4H | ZEC | LONG | Confluenza trend | 240m | 2,0x | 522,36445 | 498,03000 | 483,09844 | 263,79405 | 632,30930 | €332,53 | €665,06 | €49,99 | €-30,98 |
| Ampia 4H | PEPE | LONG | Confluenza trend | 240m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €497,18 | €994,35 | €50,70 | €-37,22 |
| Ampia 4H | ETH | LONG | Confluenza trend | 240m | 2,0x | 1933,63665 | 1871,52000 | 1869,00475 | 976,48651 | 2114,60597 | €756,64 | €1.513,28 | €50,58 | €-48,61 |
| Forza relativa 1H V1 | ESPORTS | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,02126 | 0,02126 | 0,02126 | 0,03178 | 0,01564 | €208,05 | €416,10 | €0,00 | €-0,00 |
| Forza relativa 1H V1 | NIGHT | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,02031 | 0,02031 | 0,02210 | 0,03036 | 0,01637 | €285,91 | €571,83 | €50,45 | €-0,00 |
| Forza relativa 1H V1 | ONDO | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,42171 | €891,90 | €1.783,80 | €49,29 | €0,00 |
| Forza relativa 1H V1 | ZEC | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 510,91780 | 498,03000 | 523,17072 | 763,82211 | 483,96137 | €1.018,21 | €2.036,41 | €48,84 | €51,37 |
| Forza relativa 1H V2 | ESPORTS | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,02126 | 0,02126 | 0,02126 | 0,03178 | 0,01564 | €215,33 | €430,67 | €0,00 | €-0,00 |
| Forza relativa 1H V2 | ZEC | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 512,43749 | 498,03000 | 523,41700 | 766,09405 | 488,28257 | €1.188,35 | €2.376,70 | €50,92 | €66,82 |
| Forza relativa 1H V2 | BANK | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,23652 | 0,24955 | 0,23652 | 0,11944 | 0,29896 | €198,11 | €396,21 | €0,00 | €21,83 |
| Forza relativa 1H V2 | RIF | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,10272 | 0,10281 | 0,09039 | 0,05187 | 0,12984 | €212,96 | €425,92 | €51,11 | €0,37 |
| Benchmark Donchian breakout 1H | SUI | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,76606 | 0,76606 | 0,75182 | 0,38686 | 0,80165 | €1.377,00 | €2.754,00 | €51,18 | €0,00 |
| Benchmark Donchian breakout 1H | HYPE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 58,85923 | 57,69300 | 60,10965 | 87,99454 | 55,73317 | €1.195,13 | €2.390,27 | €50,78 | €47,36 |
| Benchmark Donchian breakout 1H | ZEC | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 514,40710 | 498,03000 | 527,70883 | 769,03861 | 481,15276 | €982,86 | €1.965,73 | €50,83 | €62,58 |
| Benchmark Bollinger mean reversion 1H | DOGE | LONG | Bollinger mean reversion | 60m | 2,0x | 0,06944 | 0,06900 | 0,06861 | 0,03507 | 0,07069 | €2.013,01 | €4.026,02 | €48,31 | €-25,73 |
| Benchmark Bollinger mean reversion 1H | SOL | LONG | Bollinger mean reversion | 60m | 2,0x | 75,67913 | 75,47700 | 74,77098 | 38,21796 | 77,04136 | €2.013,07 | €4.026,14 | €48,31 | €-10,75 |
| Benchmark trend following EMA 1H | LAB | LONG | Trend following EMA | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €207,05 | €414,10 | €49,69 | €0,00 |
| Benchmark trend following EMA 1H | ZEC | SHORT | Trend following EMA | 60m | 2,0x | 511,44769 | 498,03000 | 525,07617 | 764,61430 | 481,46504 | €934,35 | €1.868,69 | €49,79 | €49,02 |
| Benchmark trend following EMA 1H | HYPE | SHORT | Trend following EMA | 60m | 2,0x | 58,72425 | 57,69300 | 60,12400 | 87,79276 | 55,64481 | €1.039,97 | €2.079,94 | €49,58 | €36,53 |
| Scanner Top 5 Long 1H | ONDO | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,40114 | 0,40114 | 0,38834 | 0,20258 | 0,42673 | €828,91 | €1.657,82 | €52,88 | €0,00 |
| Scanner Top 5 Long 1H | LAB | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €219,03 | €438,05 | €52,57 | €0,00 |
| Scanner Top 5 Long 1H | BANK | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,26100 | 0,24955 | 0,22968 | 0,13181 | 0,32364 | €220,88 | €441,75 | €53,01 | €-19,38 |
| Scanner Bottom 5 Short 1H | ESPORTS | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,02150 | 0,02150 | 0,02150 | 0,03214 | 0,01634 | €207,40 | €414,80 | €0,00 | €-0,00 |
| Scanner Bottom 5 Short 1H | ZEC | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 515,09696 | 498,03000 | 515,09696 | 770,06996 | 492,18303 | €1.091,80 | €2.183,60 | €0,00 | €72,35 |
| Scanner Bottom 5 Short 1H | DOGE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,06942 | 0,06900 | 0,07042 | 0,10378 | 0,06742 | €1.692,83 | €3.385,67 | €48,75 | €20,30 |
| Scanner Top 5 + forza BTC 1H | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39694 | 0,39694 | 0,38539 | 0,20045 | 0,42235 | €898,57 | €1.797,15 | €52,29 | €0,00 |
| Scanner Top 5 + forza BTC 1H | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €216,56 | €433,12 | €51,97 | €0,00 |
| Scanner Top 5 + forza BTC 1H | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,25383 | 0,24955 | 0,22337 | 0,12818 | 0,32084 | €215,84 | €431,68 | €51,80 | €-7,28 |
| Top 5 + BTC — solo MFE | SUI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,76776 | 0,76776 | 0,75508 | 0,38772 | 0,79565 | €1.514,04 | €3.028,08 | €50,00 | €0,00 |
| Top 5 + BTC — solo MFE | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39924 | 0,39924 | 0,38729 | 0,20162 | 0,42552 | €835,46 | €1.670,91 | €50,00 | €0,00 |
| Top 5 + BTC — solo MFE | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00231 | 0,00219 | 0,00203 | 0,00117 | 0,00292 | €205,40 | €410,80 | €49,30 | €-21,08 |
| Top 5 + BTC — Guard | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39724 | 0,39724 | 0,38434 | 0,20061 | 0,42561 | €756,62 | €1.513,24 | €49,13 | €0,00 |
| Top 5 + BTC — Guard | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €202,47 | €404,95 | €48,59 | €0,00 |
| Top 5 + BTC — Guard | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,26100 | 0,24955 | 0,22968 | 0,13181 | 0,32991 | €204,39 | €408,77 | €49,05 | €-17,94 |
| Top 5 + BTC — BTC≤3 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39974 | 0,39974 | 0,38840 | 0,20187 | 0,42468 | €884,65 | €1.769,29 | €50,18 | €0,00 |
| Top 5 + BTC — BTC≤3 | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €207,87 | €415,74 | €49,89 | €0,00 |
| Top 5 + BTC — BTC≤3 | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,25383 | 0,24955 | 0,22337 | 0,12818 | 0,32084 | €207,30 | €414,59 | €49,75 | €-6,99 |
| Top 5 + BTC — BTC 2–3 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39974 | 0,39974 | 0,38840 | 0,20187 | 0,42468 | €884,65 | €1.769,29 | €50,18 | €0,00 |
| Top 5 + BTC — BTC 2–3 | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €207,87 | €415,74 | €49,89 | €0,00 |
| Top 5 + BTC — Guard + MFE | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39724 | 0,39724 | 0,38434 | 0,20061 | 0,42561 | €756,62 | €1.513,24 | €49,13 | €0,00 |
| Top 5 + BTC — Guard + MFE | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,25426 | 0,24955 | 0,22375 | 0,12840 | 0,32139 | €204,33 | €408,67 | €49,04 | €-7,57 |
| Top 5 + BTC — Guard + MFE | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00231 | 0,00219 | 0,00203 | 0,00117 | 0,00292 | €203,24 | €406,48 | €48,78 | €-20,86 |
| Top 5 + BTC — Guard + BTC≤3 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39974 | 0,39974 | 0,38840 | 0,20187 | 0,42468 | €871,05 | €1.742,11 | €49,41 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €205,84 | €411,68 | €49,40 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,26100 | 0,24955 | 0,22968 | 0,13181 | 0,32991 | €207,79 | €415,57 | €49,87 | €-18,23 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39974 | 0,39974 | 0,38840 | 0,20187 | 0,42468 | €871,05 | €1.742,11 | €49,41 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,25426 | 0,24955 | 0,22375 | 0,12840 | 0,32139 | €206,68 | €413,36 | €49,60 | €-7,66 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00231 | 0,00219 | 0,00203 | 0,00117 | 0,00292 | €205,57 | €411,14 | €49,34 | €-21,10 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39694 | 0,39694 | 0,38539 | 0,20045 | 0,43159 | €861,83 | €1.723,66 | €50,15 | €0,00 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,21338 | €207,96 | €415,92 | €49,91 | €0,00 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,26099 | 0,24955 | 0,22979 | 0,13180 | 0,35461 | €210,54 | €421,07 | €50,35 | €-18,46 |
| Top 5 + BTC — target pieno 3R | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39694 | 0,39694 | 0,38539 | 0,20045 | 0,43159 | €861,83 | €1.723,66 | €50,15 | €0,00 |
| Top 5 + BTC — target pieno 3R | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,21338 | €207,96 | €415,92 | €49,91 | €0,00 |
| Top 5 + BTC — target pieno 3R | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,26099 | 0,24955 | 0,22979 | 0,13180 | 0,35461 | €211,50 | €423,00 | €50,58 | €-18,54 |
| Global Confluence puro 1H | DOGE | SHORT | Global Confluence puro | 60m | 2,0x | 0,06942 | 0,06900 | 0,07053 | 0,10378 | 0,06664 | €1.539,06 | €3.078,12 | €49,25 | €18,45 |
| Combo Trend | ESPORTS | SHORT | Combo Trend | 60m | 2,0x | 0,01883 | 0,01883 | 0,02109 | 0,02815 | 0,01386 | €209,57 | €419,14 | €50,30 | €-0,00 |
| Combo Trend | AKE | LONG | Combo Trend | 60m | 2,0x | 0,00231 | 0,00219 | 0,00203 | 0,00117 | 0,00292 | €205,73 | €411,46 | €49,38 | €-21,11 |
| Combo Mean Reversion | BTC | LONG | Combo Mean Reversion | 60m | 2,0x | 64949,16724 | 64698,50000 | 64169,77723 | 32799,32945 | 66196,19125 | €2.006,38 | €4.012,76 | €48,15 | €-15,49 |
| Combo Mean Reversion | PEPE | LONG | Combo Mean Reversion | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.918,54 | €3.837,08 | €50,14 | €-41,95 |
| Combo Scanner | ONDO | LONG | Combo Scanner | 60m | 2,0x | 0,39694 | 0,39694 | 0,38539 | 0,20045 | 0,42235 | €857,88 | €1.715,77 | €49,92 | €0,00 |
| Combo Scanner | LAB | LONG | Combo Scanner | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €207,54 | €415,08 | €49,81 | €0,00 |
| Combo Scanner | DOGE | SHORT | Combo Scanner | 60m | 2,0x | 0,06942 | 0,06900 | 0,07042 | 0,10378 | 0,06722 | €1.753,42 | €3.506,85 | €50,50 | €21,02 |
| Combo Adaptive — madre | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,40114 | 0,40114 | 0,38834 | 0,20258 | 0,42673 | €809,25 | €1.618,50 | €51,63 | €0,00 |
| Combo Adaptive — madre | ZEC | SHORT | Combo Adaptive | 60m | 2,0x | 514,17714 | 498,03000 | 525,63928 | 768,69483 | 491,25287 | €1.147,58 | €2.295,16 | €51,16 | €72,08 |
| Combo Adaptive — madre | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15861 | 0,13958 | 0,08010 | 0,19668 | €213,13 | €426,26 | €51,15 | €0,00 |
| Combo Adaptive — MFE Trail esistente | ESPORTS | SHORT | Combo Adaptive | 60m | 2,0x | 0,02156 | 0,02156 | 0,02091 | 0,03223 | 0,01638 | €202,62 | €405,24 | €0,00 | €-0,00 |
| Combo Adaptive — MFE Trail esistente | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39784 | 0,39784 | 0,38492 | 0,20091 | 0,42367 | €744,71 | €1.489,41 | €48,35 | €0,00 |
| Combo Adaptive — MFE Trail esistente | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15861 | 0,13958 | 0,08010 | 0,19668 | €201,70 | €403,39 | €48,41 | €0,00 |
| Combo Adaptive — Quality7 | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,40304 | 0,40304 | 0,39140 | 0,20354 | 0,42632 | €859,15 | €1.718,30 | €49,62 | €0,00 |
| Combo Adaptive — Quality7 | ZEC | SHORT | Combo Adaptive | 60m | 2,0x | 515,48688 | 498,03000 | 515,31507 | 770,65289 | 492,50422 | €1.108,92 | €2.217,83 | €0,00 | €75,11 |
| Combo Adaptive — Quality7 | BANK | LONG | Combo Adaptive | 60m | 2,0x | 0,26106 | 0,24955 | 0,22973 | 0,13184 | 0,32372 | €208,81 | €417,62 | €50,11 | €-18,42 |
| Combo Adaptive — Trend/Transition | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39724 | 0,39724 | 0,38434 | 0,20061 | 0,42303 | €757,94 | €1.515,88 | €49,21 | €0,00 |
| Combo Adaptive — Trend/Transition | ZEC | SHORT | Combo Adaptive | 60m | 2,0x | 515,48688 | 498,03000 | 515,31507 | 770,65289 | 492,50422 | €1.111,03 | €2.222,05 | €0,00 | €75,25 |
| Combo Adaptive — Trend/Transition | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15861 | 0,13958 | 0,08010 | 0,19668 | €206,52 | €413,04 | €49,56 | €0,00 |
| Combo Adaptive — Quality7 + Regime | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,40554 | 0,40554 | 0,39390 | 0,20480 | 0,42882 | €864,27 | €1.728,54 | €49,61 | €0,00 |
| Combo Adaptive — Quality7 + Regime | ZEC | SHORT | Combo Adaptive | 60m | 2,0x | 515,48688 | 498,03000 | 515,31507 | 770,65289 | 492,50422 | €1.109,39 | €2.218,78 | €0,00 | €75,14 |
| Combo Adaptive — Long Only | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,41951 | €893,67 | €1.787,34 | €49,39 | €0,00 |
| Combo Adaptive — Long Only | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €205,55 | €411,10 | €49,33 | €0,00 |
| Combo Adaptive — parziale 1R | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,41951 | €893,02 | €1.786,04 | €49,36 | €0,00 |
| Combo Adaptive — parziale 1R | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €205,22 | €410,44 | €49,25 | €0,00 |
| Combo Adaptive — parziale 1R | ZEC | SHORT | Combo Adaptive | 60m | 2,0x | 515,68684 | 498,03000 | 515,68684 | 770,95183 | 491,41745 | €521,39 | €1.042,77 | €0,00 | €35,70 |
| Combo Adaptive — Quality7 + Regime + parziale 1R | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,40554 | 0,40554 | 0,39390 | 0,20480 | 0,42882 | €864,27 | €1.728,54 | €49,61 | €0,00 |
| Combo Adaptive — Quality7 + Regime + parziale 1R | ZEC | SHORT | Combo Adaptive | 60m | 2,0x | 515,48688 | 498,03000 | 515,31507 | 770,65289 | 492,50422 | €554,69 | €1.109,39 | €0,00 | €37,57 |
| Combo Adaptive — 75% a 2R + runner 3R | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,43050 | €902,18 | €1.804,37 | €49,86 | €0,00 |
| Combo Adaptive — 75% a 2R + runner 3R | ZEC | SHORT | Combo Adaptive | 60m | 2,0x | 514,68704 | 498,03000 | 514,57341 | 769,45713 | 483,39306 | €1.229,27 | €2.458,54 | €0,00 | €79,57 |
| Combo Adaptive — 75% a 2R + runner 3R | BANK | LONG | Combo Adaptive | 60m | 2,0x | 0,26106 | 0,24955 | 0,22973 | 0,13184 | 0,35504 | €206,58 | €413,16 | €49,58 | €-18,22 |
| Combo Adaptive — target pieno 3R | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,43050 | €902,18 | €1.804,37 | €49,86 | €0,00 |
| Combo Adaptive — target pieno 3R | ZEC | SHORT | Combo Adaptive | 60m | 2,0x | 514,68704 | 498,03000 | 514,57341 | 769,45713 | 483,39306 | €1.230,32 | €2.460,64 | €0,00 | €79,63 |
| Combo Adaptive — target pieno 3R | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15861 | 0,13958 | 0,08010 | 0,21571 | €207,43 | €414,86 | €49,78 | €0,00 |
| Btc Ema 1H | BTC | SHORT | Trend following EMA | 60m | 3,0x | 64834,39053 | 64698,50000 | 65768,00575 | 86121,68208 | 62967,16008 | €1.149,81 | €3.449,44 | €49,67 | €7,23 |
| Btc Ema 4H | BTC | LONG | Trend following EMA | 240m | 2,0x | 65410,57950 | 64698,50000 | 63931,54687 | 33032,34265 | 69108,16107 | €1.105,63 | €2.211,26 | €50,00 | €-24,07 |
| Btc Donchian 1H | BTC | SHORT | Donchian breakout 20 barre | 60m | 3,0x | 64923,19276 | 64698,50000 | 65754,20963 | 86239,64105 | 63261,15903 | €1.293,96 | €3.881,87 | €49,69 | €13,43 |
| Btc Donchian 4H | BTC | LONG | Donchian breakout 20 barre | 240m | 2,0x | 65410,57950 | 64698,50000 | 63931,54687 | 33032,34265 | 69551,87112 | €1.105,63 | €2.211,26 | €50,00 | €-24,07 |
| Btc Bollinger 4H | BTC | SHORT | Bollinger mean reversion | 240m | 2,0x | 66588,49964 | 64698,50000 | 65621,81812 | 99549,80696 | 64307,80290 | €1.313,84 | €2.627,69 | €0,00 | €74,58 |
| Btc Adaptive 1H | BTC | SHORT | Combo Adaptive | 60m | 3,0x | 64713,55470 | 64698,50000 | 65645,42989 | 85961,17183 | 62849,80432 | €1.156,05 | €3.468,15 | €49,94 | €0,81 |
| Btc Adaptive 4H | BTC | LONG | Combo Adaptive | 240m | 2,0x | 66171,85172 | 64698,50000 | 64592,42491 | 33416,78512 | 70120,41876 | €1.047,40 | €2.094,81 | €50,00 | €-46,64 |
| Sol Ema 1H | SOL | SHORT | Trend following EMA | 60m | 3,0x | 75,65487 | 75,47700 | 76,74430 | 100,49488 | 73,47601 | €1.150,16 | €3.450,47 | €49,69 | €8,11 |
| Sol Donchian 1H | SOL | SHORT | Donchian breakout 20 barre | 60m | 3,0x | 75,65487 | 75,47700 | 76,62325 | 100,49488 | 73,71810 | €1.301,74 | €3.905,22 | €49,99 | €9,18 |
| Sol Bollinger 1H | SOL | LONG | Bollinger mean reversion | 60m | 3,0x | 75,68513 | 75,47700 | 74,77691 | 50,83518 | 77,04747 | €1.381,14 | €4.143,42 | €49,72 | €-11,39 |
| Sol Bollinger 4H | SOL | SHORT | Bollinger mean reversion | 240m | 2,0x | 78,45931 | 75,47700 | 76,93814 | 117,29666 | 74,81402 | €968,56 | €1.937,11 | €0,00 | €73,63 |
| Sol Adaptive 1H | SOL | LONG | Combo Adaptive | 60m | 3,0x | 76,29126 | 75,47700 | 75,19266 | 51,24229 | 78,48844 | €1.149,09 | €3.447,26 | €49,64 | €-36,79 |
| Doge Ema 1H | DOGE | SHORT | Trend following EMA | 60m | 3,0x | 0,06942 | 0,06900 | 0,07042 | 0,09221 | 0,06742 | €1.173,45 | €3.520,36 | €50,69 | €21,10 |
| Doge Donchian 1H | DOGE | SHORT | Donchian breakout 20 barre | 60m | 3,0x | 0,06940 | 0,06900 | 0,07045 | 0,09218 | 0,06729 | €1.095,98 | €3.287,94 | €49,99 | €18,77 |
| Doge Bollinger 1H | DOGE | LONG | Bollinger mean reversion | 60m | 3,0x | 0,06944 | 0,06900 | 0,06861 | 0,04664 | 0,07069 | €1.381,14 | €4.143,42 | €49,72 | €-26,48 |
| Master Adaptive V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39854 | 0,39854 | 0,38677 | 0,20126 | 0,42207 | €833,00 | €1.665,99 | €49,19 | €0,00 |
| Master Adaptive V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €203,80 | €407,60 | €48,91 | €0,00 |
| Master Adaptive V1 | BANK | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,25383 | 0,24955 | 0,22337 | 0,12818 | 0,31475 | €202,68 | €405,37 | €48,64 | €-6,84 |
| Master Adaptive No Alt V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39854 | 0,39854 | 0,38677 | 0,20126 | 0,42207 | €833,00 | €1.665,99 | €49,19 | €0,00 |
| Master Adaptive No Alt V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €203,80 | €407,60 | €48,91 | €0,00 |
| Master Adaptive No Alt V1 | BANK | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,25383 | 0,24955 | 0,22337 | 0,12818 | 0,31475 | €202,68 | €405,37 | €48,64 | €-6,84 |
| Master Adaptive Strict3 V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,41951 | €887,07 | €1.774,14 | €49,03 | €0,00 |
| Master Adaptive Strict3 V1 | BANK | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,23652 | 0,24955 | 0,20814 | 0,11944 | 0,29328 | €202,06 | €404,12 | €48,49 | €22,27 |
| Master Adaptive Strict3 V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00231 | 0,00219 | 0,00203 | 0,00117 | 0,00286 | €201,45 | €402,91 | €48,35 | €-20,67 |
| Master Adaptive Expanded V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39854 | 0,39854 | 0,38677 | 0,20126 | 0,42207 | €833,00 | €1.665,99 | €49,19 | €0,00 |
| Master Adaptive Expanded V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €203,80 | €407,60 | €48,91 | €0,00 |
| Master Adaptive Expanded V1 | BANK | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,25627 | 0,24955 | 0,22552 | 0,12942 | 0,31778 | €203,36 | €406,71 | €48,81 | €-10,67 |
| Master Adaptive Gb20 V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,40304 | 0,40304 | 0,39140 | 0,20354 | 0,42632 | €848,64 | €1.697,27 | €49,02 | €0,00 |
| Master Adaptive Gb20 V1 | BANK | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,26099 | 0,24955 | 0,22979 | 0,13180 | 0,32340 | €205,22 | €410,45 | €49,08 | €-17,99 |
| Master Adaptive Gb20 V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00231 | 0,00219 | 0,00203 | 0,00117 | 0,00286 | €201,67 | €403,34 | €48,40 | €-20,70 |
| Master Adaptive Runner25 V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39854 | 0,39854 | 0,38677 | 0,20126 | 0,43384 | €833,00 | €1.665,99 | €49,19 | €0,00 |
| Master Adaptive Runner25 V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,21338 | €203,80 | €407,60 | €48,91 | €0,00 |
| Master Adaptive Runner25 V1 | BANK | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,25383 | 0,24955 | 0,22337 | 0,12818 | 0,34521 | €202,68 | €405,37 | €48,64 | €-6,84 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Combo Trend | ONDO | LONG | 2026-07-23T19:38:35+00:00 | 0,37260 | €-1,89 | -0,04 | TIME_EXIT_NO_CANDLES |
| Rapida 1H V3 Filtered — madre | SUI | LONG | 2026-07-23T19:38:35+00:00 | 0,76370 | €-6,85 | -0,14 | TIME_EXIT_NO_CANDLES |
| Rapida 1H V1 — madre | SUI | LONG | 2026-07-23T19:38:35+00:00 | 0,76370 | €-6,93 | -0,14 | TIME_EXIT_NO_CANDLES |
| Top 5 + BTC — solo MFE | AKE | LONG | 2026-07-23T18:38:36+00:00 | 0,00219 | €-64,53 | -1,30 | STOP_STRESS_SLIPPAGE |
| Top 5 + BTC — Guard + MFE | AKE | LONG | 2026-07-23T18:38:36+00:00 | 0,00219 | €-63,78 | -1,30 | STOP_STRESS_SLIPPAGE |
| Top 5 + BTC — Guard + BTC≤3 + MFE | AKE | LONG | 2026-07-23T18:38:36+00:00 | 0,00219 | €-64,51 | -1,30 | STOP_STRESS_SLIPPAGE |
| Master Adaptive Strict3 V1 | AKE | LONG | 2026-07-23T18:38:36+00:00 | 0,00225 | €-69,08 | -1,42 | STOP_STRESS_SLIPPAGE |
| Master Adaptive Gb20 V1 | AKE | LONG | 2026-07-23T18:38:36+00:00 | 0,00225 | €-69,17 | -1,42 | STOP_STRESS_SLIPPAGE |
| Combo Trend | AKE | LONG | 2026-07-23T18:38:36+00:00 | 0,00223 | €-66,68 | -1,34 | STOP_STRESS_SLIPPAGE |
| Combo Adaptive — 75% a 2R + runner 3R | AKE | LONG | 2026-07-23T18:38:36+00:00 | 0,00219 | €-64,96 | -1,30 | STOP_STRESS_SLIPPAGE |
| Benchmark Bollinger mean reversion 1H | AKE | SHORT | 2026-07-23T18:38:36+00:00 | 0,00229 | €74,72 | 1,48 | TARGET |
| Rapida V3 — Long Only | AKE | LONG | 2026-07-23T18:38:36+00:00 | 0,00223 | €-74,31 | -1,49 | STOP_STRESS_SLIPPAGE |

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
| MAIN | Principale 4H | 43/30 | 18/30 | 0,93 | 0,91 | -0,05R | €-2,94 | 4,26% | COERENTE − | BOCCIATA RESEARCH |
| RSI_EXTREME_LONG_15M | Scalp RSI Long 25 · prudente · 5x (riferimento tra 9 varianti) | 8/30 | 4/30 | 0,30 | 0,22 | -0,56R | €-5,00 | 0,34% | COERENTE − | RACCOLTA RESEARCH |
| RSI_EXTREME_SHORT_15M | Scalp RSI Short 75 · prudente · 5x (riferimento tra 9 varianti) | 7/30 | 6/30 | 0,62 | 0,18 | -0,24R | €-5,86 | 0,36% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_1H_BALANCED | Bilanciata 1H V1 | 142/30 | 35/30 | 0,94 | 1,40 | -0,04R | €8,38 | 2,30% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_BALANCED_V2 | Bilanciata 1H V2 | 24/30 | 20/30 | 1,57 | 1,10 | 0,31R | €2,34 | 2,75% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_1H_BALANCED_V3 | Bilanciata 1H V3 Filtered | 49/30 | 30/30 | 1,07 | 1,28 | 0,05R | €7,48 | 2,20% | COERENTE + | BOCCIATA RESEARCH |
| SHADOW_1H_FAST | Rapida 1H V1 — madre | 166/30 | 60/30 | 0,90 | 0,95 | -0,06R | €-1,07 | 6,76% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | Rapida V1 — Long + BTC 1–3 + score <7,5 | 7/30 | 6/30 | 1,82 | 0,62 | 0,38R | €-7,40 | 1,55% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | Rapida V1 — no HIGH + score <7,5 | 30/30 | 25/30 | 0,88 | 0,91 | -0,07R | €-2,32 | 2,83% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_NO_PEPE_V1 | Rapida V1 — senza PEPE | 34/30 | 19/30 | 0,82 | 0,97 | -0,12R | €-0,65 | 2,10% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_V1 | Rapida V1 — score 6–7,5 | 22/30 | 23/30 | 1,09 | 1,27 | 0,05R | €5,18 | 2,49% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_TP2_V1 | Rapida V1 — target pieno 2R | 28/30 | 20/30 | 0,59 | 0,83 | -0,33R | €-4,19 | 2,58% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V2 | Rapida 1H V2 | 5/30 | 5/30 | 0,61 | 0,82 | -0,29R | €-3,78 | 1,33% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3 | Rapida 1H V3 Filtered — madre | 76/30 | 52/30 | 1,02 | 1,17 | 0,01R | €3,19 | 2,89% | COERENTE + | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_CAP75_V1 | Rapida V3 — score <7,5 | 28/30 | 20/30 | 0,86 | 1,09 | -0,09R | €2,03 | 2,49% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | Rapida V3 — qualità completa + profit lock | 14/30 | 13/30 | 0,73 | 0,47 | -0,19R | €-19,67 | 3,16% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | Rapida V3 — Long + no HIGH + score <7,5 | 14/30 | 13/30 | 0,73 | 0,50 | -0,19R | €-16,65 | 2,77% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | Rapida V3 — Long Only | 17/30 | 15/30 | 0,55 | 0,68 | -0,35R | €-8,73 | 2,58% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | Rapida V3 — no volatilità HIGH | 31/30 | 24/30 | 0,84 | 0,96 | -0,11R | €-1,04 | 2,96% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | Rapida V3 — senza ESPORTS | 32/30 | 23/30 | 0,79 | 1,00 | -0,14R | €0,09 | 2,49% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_4H_WIDE | Ampia 4H | 39/30 | 12/30 | 0,82 | 1,27 | -0,14R | €7,39 | 2,56% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_BOLLINGER_MR_1H | Benchmark Bollinger mean reversion 1H | 33/30 | 24/30 | 0,97 | 1,35 | -0,02R | €6,53 | 2,06% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_BTC_ADAPTIVE_1H | Btc Adaptive 1H | 1/30 | 2/30 | 0,00 | 0,78 | -1,11R | €-5,87 | 0,89% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_ADAPTIVE_4H | Btc Adaptive 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,64% | n/a | RACCOLTA RESEARCH |
| SHADOW_BTC_BOLLINGER_1H | Btc Bollinger 1H | 2/30 | 2/30 | ∞ | ∞ | 1,37R | €49,98 | 0,31% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_BTC_BOLLINGER_4H | Btc Bollinger 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,27% | n/a | RACCOLTA RESEARCH |
| SHADOW_BTC_DONCHIAN_1H | Btc Donchian 1H | 2/30 | 3/30 | 0,00 | 0,43 | -1,12R | €-20,81 | 1,49% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_DONCHIAN_4H | Btc Donchian 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,68% | n/a | RACCOLTA RESEARCH |
| SHADOW_BTC_EMA_1H | Btc Ema 1H | 4/30 | 4/30 | 0,57 | 0,60 | -0,36R | €-16,40 | 1,56% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_EMA_4H | Btc Ema 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,68% | n/a | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE | Combo Adaptive — madre | 84/30 | 20/30 | 1,19 | 1,71 | 0,12R | €11,97 | 1,31% | COERENTE + | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | Combo Adaptive — Long Only | 18/30 | 5/30 | 0,52 | 0,42 | -0,40R | €-26,52 | 2,34% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | Combo Adaptive — MFE Trail esistente | 52/30 | 27/30 | 1,06 | 0,45 | 0,04R | €-11,76 | 4,11% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | Combo Adaptive — parziale 1R | 29/30 | 10/30 | 0,68 | 0,51 | -0,25R | €-18,79 | 2,24% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | Combo Adaptive — Quality7 + Regime + parziale 1R | 3/30 | 3/30 | 0,00 | 0,00 | -1,07R | €-53,33 | 1,95% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | Combo Adaptive — Quality7 + Regime | 3/30 | 3/30 | 0,00 | 0,00 | -1,07R | €-53,33 | 1,95% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | Combo Adaptive — Quality7 | 5/30 | 4/30 | 0,47 | 0,96 | -0,45R | €-0,99 | 1,51% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | Combo Adaptive — Trend/Transition | 23/30 | 8/30 | 0,27 | 0,70 | -0,68R | €-10,49 | 2,18% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | Combo Adaptive — 75% a 2R + runner 3R | 23/30 | 11/30 | 0,58 | 0,71 | -0,37R | €-9,98 | 2,12% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | Combo Adaptive — target pieno 3R | 23/30 | 8/30 | 0,58 | 0,83 | -0,37R | €-4,45 | 1,41% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_MEAN_REVERSION | Combo Mean Reversion | 11/30 | 10/30 | 1,18 | 1,12 | 0,10R | €3,19 | 2,26% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_COMBO_SCANNER | Combo Scanner | 53/30 | 23/30 | 1,51 | 1,20 | 0,31R | €5,12 | 2,66% | COERENTE + | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_COMBO_TREND | Combo Trend | 65/30 | 22/30 | 1,05 | 0,81 | 0,03R | €-5,73 | 3,58% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_DOGE_BOLLINGER_1H | Doge Bollinger 1H | 1/30 | 1/30 | 0,00 | 0,00 | -1,13R | €-55,79 | 0,92% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_DOGE_DONCHIAN_1H | Doge Donchian 1H | 2/30 | 3/30 | 1,67 | 0,96 | 0,38R | €-0,85 | 0,96% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_DOGE_EMA_1H | Doge Ema 1H | 3/30 | 6/30 | 3,40 | 2,24 | 0,89R | €23,11 | 1,36% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_DONCHIAN_1H | Benchmark Donchian breakout 1H | 38/30 | 17/30 | 1,05 | 1,40 | 0,04R | €9,27 | 2,12% | COERENTE + | BOCCIATA RESEARCH |
| SHADOW_EMA_TREND_1H | Benchmark trend following EMA 1H | 72/30 | 15/30 | 1,00 | 0,88 | 0,00R | €-3,48 | 2,25% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_ETH_ADAPTIVE_1H | Eth Adaptive 1H | 3/30 | 4/30 | 0,85 | 0,16 | -0,11R | €-23,05 | 1,03% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_BOLLINGER_1H | Eth Bollinger 1H | 1/30 | 1/30 | 0,00 | ∞ | -1,13R | €15,45 | 0,51% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_ETH_DONCHIAN_1H | Eth Donchian 1H | 3/30 | 3/30 | 0,84 | 0,84 | -0,12R | €-5,82 | 1,38% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_EMA_1H | Eth Ema 1H | 2/30 | 6/30 | 1,70 | 0,25 | 0,39R | €-27,46 | 1,67% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_ETH_EMA_4H | Eth Ema 4H | 0/30 | 1/30 | 0,00 | 0,00 | 0,00R | €-52,88 | 0,68% | n/a | RACCOLTA RESEARCH |
| SHADOW_GLOBAL_PURE | Global Confluence puro 1H | 3/30 | 8/30 | 3,47 | 0,45 | 0,91R | €-18,75 | 2,92% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | Master Adaptive Expanded V1 | 13/30 | 7/30 | 0,33 | 0,29 | -0,61R | €-32,57 | 2,80% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | Master Adaptive Gb20 V1 | 13/30 | 18/30 | 0,16 | 0,33 | -0,83R | €-17,70 | 3,86% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | Master Adaptive No Alt V1 | 13/30 | 5/30 | 0,16 | 0,00 | -0,83R | €-54,20 | 3,19% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | Master Adaptive Runner25 V1 | 12/30 | 5/30 | 0,25 | 0,00 | -0,73R | €-54,20 | 3,19% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | Master Adaptive Strict3 V1 | 12/30 | 9/30 | 0,17 | 0,21 | -0,81R | €-41,18 | 3,91% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_V1 | Master Adaptive V1 | 13/30 | 5/30 | 0,16 | 0,00 | -0,83R | €-54,20 | 3,19% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_RELATIVE_STRENGTH | Forza relativa 1H V1 | 101/30 | 22/30 | 0,93 | 0,83 | -0,05R | €-3,30 | 3,25% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_RELATIVE_STRENGTH_V2 | Forza relativa 1H V2 | 29/30 | 24/30 | 1,43 | 1,23 | 0,27R | €6,64 | 3,69% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT | Scanner Bottom 5 Short 1H | 36/30 | 21/30 | 0,69 | 0,57 | -0,21R | €-11,70 | 5,48% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC | Scanner Top 5 + forza BTC 1H | 52/30 | 21/30 | 1,44 | 1,91 | 0,27R | €17,17 | 2,01% | COERENTE + | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | Top 5 + BTC — BTC 2–3 | 9/30 | 3/30 | 0,57 | 0,54 | -0,36R | €-16,53 | 2,17% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | Top 5 + BTC — BTC≤3 | 11/30 | 3/30 | 0,45 | 0,54 | -0,48R | €-16,53 | 2,20% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | Top 5 + BTC — Guard + BTC≤3 + MFE | 6/30 | 8/30 | 0,43 | 0,46 | -0,49R | €-17,78 | 2,30% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | Top 5 + BTC — Guard + BTC≤3 | 6/30 | 3/30 | 0,43 | 0,91 | -0,49R | €-3,70 | 1,64% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | Top 5 + BTC — Guard + MFE | 9/30 | 11/30 | 0,26 | 0,32 | -0,69R | €-23,13 | 3,47% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | Top 5 + BTC — Guard | 9/30 | 6/30 | 0,26 | 0,38 | -0,69R | €-29,13 | 3,31% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | Top 5 + BTC — solo MFE | 13/30 | 8/30 | 0,60 | 0,26 | -0,32R | €-17,30 | 2,51% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | Top 5 + BTC — 75% a 2,2R + runner 3R | 12/30 | 7/30 | 0,56 | 1,52 | -0,39R | €12,19 | 2,33% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | Top 5 + BTC — target pieno 3R | 12/30 | 7/30 | 0,56 | 1,81 | -0,39R | €18,78 | 2,33% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_LONG | Scanner Top 5 Long 1H | 64/30 | 29/30 | 1,39 | 2,16 | 0,23R | €21,30 | 2,70% | COERENTE + | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_SOL_ADAPTIVE_1H | Sol Adaptive 1H | 3/30 | 3/30 | 0,86 | 0,34 | -0,11R | €-23,97 | 1,81% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_ADAPTIVE_4H | Sol Adaptive 4H | 1/30 | 1/30 | 0,00 | 0,00 | -1,05R | €-51,83 | 0,54% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_BOLLINGER_1H | Sol Bollinger 1H | 1/30 | 1/30 | 0,00 | 0,00 | -1,13R | €-55,79 | 0,75% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_BOLLINGER_4H | Sol Bollinger 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,40% | n/a | RACCOLTA RESEARCH |
| SHADOW_SOL_DONCHIAN_1H | Sol Donchian 1H | 2/30 | 2/30 | 0,00 | 0,41 | -1,12R | €-1,31 | 0,58% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_DONCHIAN_4H | Sol Donchian 4H | 1/30 | 1/30 | 0,00 | 0,00 | -1,06R | €-52,00 | 0,56% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_EMA_1H | Sol Ema 1H | 3/30 | 3/30 | 0,86 | 0,42 | -0,11R | €-20,89 | 1,49% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_EMA_4H | Sol Ema 4H | 1/30 | 1/30 | 0,00 | 0,00 | -1,06R | €-52,00 | 0,56% | COERENTE − | RACCOLTA RESEARCH |

Per le famiglie RSI con più configurazioni di leva o margine, il lato paper usa il conto con il maggior numero di eventi indipendenti; i conti duplicati non vengono aggregati.
`PRONTA PER REVISIONE LIVE` non invia ordini e non sposta capitale: abilita soltanto una revisione manuale finale.

## 🎯 DOGE Rejection Short — conto dedicato €3.600

Simulazione separata **paper only**: capitale/margine iniziale **€3.600**, leva **5x**, esposizione iniziale **€18.000**. Non modifica i conti paper da €10.000 e non invia ordini reali.

- Stato: **WAITING**
- Prezzo DOGE: **0.069**
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
| BTC sotto filtro | 64698.5 | OK |

### Ultima candela 15m valutata

- Rejection accettata: **NO**; motivo: **trigger_touched, entry_not_chased**
- High **0.06937**; close **0.06923**; wick alta **43.7%**; volume **x0.03**

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
- Motivo: Direzione poco definita: score BTC +0.0, breadth EMA50 25%, ADX 24.4.
- BTC trend score: **0,00**; ADX: **24,38**; breadth sopra EMA50: **25,00%**
- Mediana alt vs BTC: **-0,77%**; dispersione: **22,25%**

- Aperti in questo ciclo: **0**
- Chiusi in questo ciclo: **0**
- Posizioni research aperte: **440**
- Trade research chiusi: **1842**
- Eventi di mercato indipendenti chiusi: **546**
- Segnali sovrapposti saltati sullo stesso asset/profilo: **7223**
- Posizioni Research V1 senza regime scartate durante la migrazione: **28**

### Risultati complessivi per strategia

| Profilo | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| MAIN | 13 | 43 | 43 | 32,56% | 0,93 | -0,05R | €-20,57 |
| RSI_EXTREME_LONG_15M | 0 | 8 | 8 | 25,00% | 0,30 | -0,56R | €-45,05 |
| RSI_EXTREME_SHORT_15M | 0 | 7 | 7 | 28,57% | 0,62 | -0,24R | €-16,64 |
| Bilanciata 1H V1 | 16 | 142 | 142 | 33,10% | 0,94 | -0,04R | €-57,15 |
| Bilanciata 1H V2 | 8 | 27 | 24 | 44,44% | 1,57 | 0,31R | €84,83 |
| Bilanciata 1H V3 Filtered | 11 | 49 | 49 | 36,73% | 1,07 | 0,05R | €23,27 |
| Rapida 1H V1 | 12 | 166 | 166 | 38,55% | 0,90 | -0,06R | €-104,70 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | 2 | 7 | 7 | 57,14% | 1,82 | 0,38R | €26,35 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | 11 | 30 | 30 | 40,00% | 0,88 | -0,07R | €-22,11 |
| SHADOW_1H_FAST_NO_PEPE_V1 | 11 | 34 | 34 | 38,24% | 0,82 | -0,12R | €-41,18 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | 5 | 22 | 22 | 45,45% | 1,09 | 0,05R | €11,82 |
| SHADOW_1H_FAST_TP2_V1 | 12 | 28 | 28 | 25,00% | 0,59 | -0,33R | €-91,84 |
| Rapida 1H V2 | 1 | 6 | 5 | 33,33% | 0,61 | -0,29R | €-17,63 |
| Rapida 1H V3 Filtered | 7 | 76 | 76 | 42,11% | 1,02 | 0,01R | €7,58 |
| SHADOW_1H_FAST_V3_CAP75_V1 | 6 | 28 | 28 | 39,29% | 0,86 | -0,09R | €-26,21 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | 2 | 14 | 14 | 35,71% | 0,73 | -0,19R | €-26,19 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | 2 | 14 | 14 | 35,71% | 0,73 | -0,19R | €-26,19 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | 3 | 17 | 17 | 29,41% | 0,55 | -0,35R | €-58,95 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | 7 | 31 | 31 | 38,71% | 0,84 | -0,11R | €-33,27 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | 7 | 32 | 32 | 37,50% | 0,79 | -0,14R | €-44,78 |
| SHADOW_4H_WIDE | 18 | 39 | 39 | 23,08% | 0,82 | -0,14R | €-56,28 |
| SHADOW_BOLLINGER_MR_1H | 2 | 33 | 33 | 42,42% | 0,97 | -0,02R | €-5,66 |
| SHADOW_BTC_ADAPTIVE_1H | 2 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_BTC_ADAPTIVE_4H | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_BOLLINGER_1H | 0 | 2 | 2 | 100,00% | ∞ | 1,37R | €27,33 |
| SHADOW_BTC_BOLLINGER_4H | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_DONCHIAN_1H | 2 | 2 | 2 | 0,00% | 0,00 | -1,12R | €-22,50 |
| SHADOW_BTC_DONCHIAN_4H | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_EMA_1H | 1 | 4 | 4 | 25,00% | 0,57 | -0,36R | €-14,44 |
| SHADOW_BTC_EMA_4H | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_ADAPTIVE | 16 | 84 | 84 | 39,29% | 1,19 | 0,12R | €103,23 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | 6 | 18 | 18 | 22,22% | 0,52 | -0,40R | €-72,38 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | 15 | 52 | 52 | 36,54% | 1,06 | 0,04R | €20,67 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | 12 | 29 | 29 | 27,59% | 0,68 | -0,25R | €-71,26 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | 2 | 3 | 3 | 0,00% | 0,00 | -1,07R | €-32,05 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | 2 | 3 | 3 | 0,00% | 0,00 | -1,07R | €-32,05 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | 3 | 5 | 5 | 20,00% | 0,47 | -0,45R | €-22,39 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | 4 | 23 | 23 | 13,04% | 0,27 | -0,68R | €-156,60 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | 13 | 23 | 23 | 17,39% | 0,58 | -0,37R | €-85,11 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | 13 | 23 | 23 | 17,39% | 0,58 | -0,37R | €-85,11 |
| SHADOW_COMBO_MEAN_REVERSION | 4 | 11 | 11 | 45,45% | 1,18 | 0,10R | €11,40 |
| SHADOW_COMBO_SCANNER | 8 | 53 | 53 | 43,40% | 1,51 | 0,31R | €162,31 |
| SHADOW_COMBO_TREND | 15 | 65 | 65 | 33,85% | 1,05 | 0,03R | €22,28 |
| SHADOW_DOGE_BOLLINGER_1H | 1 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,33 |
| SHADOW_DOGE_DONCHIAN_1H | 1 | 2 | 2 | 50,00% | 1,67 | 0,38R | €7,50 |
| SHADOW_DOGE_EMA_1H | 1 | 3 | 3 | 66,67% | 3,40 | 0,89R | €26,67 |
| SHADOW_DONCHIAN_1H | 9 | 38 | 38 | 31,58% | 1,05 | 0,04R | €14,98 |
| SHADOW_EMA_TREND_1H | 15 | 72 | 72 | 31,94% | 1,00 | 0,00R | €1,20 |
| SHADOW_ETH_ADAPTIVE_1H | 0 | 3 | 3 | 33,33% | 0,85 | -0,11R | €-3,33 |
| SHADOW_ETH_BOLLINGER_1H | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,33 |
| SHADOW_ETH_DONCHIAN_1H | 0 | 3 | 3 | 33,33% | 0,84 | -0,12R | €-3,61 |
| SHADOW_ETH_EMA_1H | 1 | 2 | 2 | 50,00% | 1,70 | 0,39R | €7,78 |
| SHADOW_ETH_EMA_4H | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_GLOBAL_PURE | 1 | 3 | 3 | 66,67% | 3,47 | 0,91R | €27,17 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | 6 | 13 | 13 | 15,38% | 0,33 | -0,61R | €-79,00 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | 6 | 13 | 13 | 7,69% | 0,16 | -0,83R | €-108,20 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | 6 | 13 | 13 | 7,69% | 0,16 | -0,83R | €-108,06 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | 6 | 12 | 12 | 8,33% | 0,25 | -0,73R | €-88,02 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | 4 | 12 | 12 | 8,33% | 0,17 | -0,81R | €-97,76 |
| SHADOW_MASTER_ADAPTIVE_V1 | 6 | 13 | 13 | 7,69% | 0,16 | -0,83R | €-108,20 |
| Forza relativa 1H V1 | 12 | 101 | 101 | 29,70% | 0,93 | -0,05R | €-50,33 |
| Forza relativa 1H V2 | 6 | 32 | 29 | 40,62% | 1,43 | 0,27R | €85,24 |
| SHADOW_SCANNER_BOTTOM5_SHORT | 7 | 36 | 36 | 25,00% | 0,69 | -0,21R | €-76,25 |
| SHADOW_SCANNER_TOP5_BTC | 7 | 52 | 52 | 40,38% | 1,44 | 0,27R | €138,46 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | 4 | 9 | 9 | 22,22% | 0,57 | -0,36R | €-32,03 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | 6 | 11 | 11 | 18,18% | 0,45 | -0,48R | €-52,36 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | 5 | 6 | 6 | 16,67% | 0,43 | -0,49R | €-29,52 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | 5 | 6 | 6 | 16,67% | 0,43 | -0,49R | €-29,52 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | 5 | 9 | 9 | 11,11% | 0,26 | -0,69R | €-62,11 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | 5 | 9 | 9 | 11,11% | 0,26 | -0,69R | €-62,11 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | 8 | 13 | 13 | 23,08% | 0,60 | -0,32R | €-42,22 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | 7 | 12 | 12 | 16,67% | 0,56 | -0,39R | €-46,92 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | 7 | 12 | 12 | 16,67% | 0,56 | -0,39R | €-46,92 |
| SHADOW_SCANNER_TOP5_LONG | 8 | 64 | 64 | 42,19% | 1,39 | 0,23R | €147,62 |
| SHADOW_SOL_ADAPTIVE_1H | 2 | 3 | 3 | 33,33% | 0,86 | -0,11R | €-3,18 |
| SHADOW_SOL_ADAPTIVE_4H | 0 | 1 | 1 | 0,00% | 0,00 | -1,05R | €-10,52 |
| SHADOW_SOL_BOLLINGER_1H | 1 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,33 |
| SHADOW_SOL_BOLLINGER_4H | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SOL_DONCHIAN_1H | 1 | 2 | 2 | 0,00% | 0,00 | -1,12R | €-22,33 |
| SHADOW_SOL_DONCHIAN_4H | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,56 |
| SHADOW_SOL_EMA_1H | 1 | 3 | 3 | 33,33% | 0,86 | -0,11R | €-3,18 |
| SHADOW_SOL_EMA_4H | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,56 |

### Matrice strategia × regime all’entrata

| Profilo | Regime entrata | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| MAIN | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| MAIN | ALT_ROTATION_UP | 3 | 3 | 3 | 0,00% | 0,00 | -1,01R | €-30,40 |
| MAIN | RANGE | 3 | 14 | 14 | 28,57% | 0,77 | -0,17R | €-23,82 |
| MAIN | RANGE_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| MAIN | TRANSITION | 1 | 7 | 7 | 42,86% | 1,45 | 0,26R | €18,34 |
| MAIN | TREND_UP | 2 | 15 | 15 | 33,33% | 0,96 | -0,03R | €-4,16 |
| MAIN | TREND_UP_HIGH_VOL | 3 | 3 | 3 | 33,33% | 0,98 | -0,01R | €-0,40 |
| RSI_EXTREME_LONG_15M | RANGE | 0 | 6 | 6 | 0,00% | 0,00 | -1,07R | €-64,49 |
| RSI_EXTREME_LONG_15M | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,29R | €12,88 |
| RSI_EXTREME_LONG_15M | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 0,66R | €6,56 |
| RSI_EXTREME_SHORT_15M | ALT_ROTATION_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 1,47R | €14,67 |
| RSI_EXTREME_SHORT_15M | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,90 |
| RSI_EXTREME_SHORT_15M | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -0,41R | €-4,13 |
| RSI_EXTREME_SHORT_15M | TREND_UP | 0 | 4 | 4 | 25,00% | 0,44 | -0,41R | €-16,27 |
| Bilanciata 1H V1 | ALT_ROTATION_DOWN | 2 | 6 | 6 | 33,33% | 0,88 | -0,08R | €-5,07 |
| Bilanciata 1H V1 | ALT_ROTATION_UP | 0 | 14 | 14 | 50,00% | 1,84 | 0,44R | €61,99 |
| Bilanciata 1H V1 | RANGE | 8 | 31 | 31 | 32,26% | 0,92 | -0,06R | €-17,88 |
| Bilanciata 1H V1 | RANGE_HIGH_VOL | 0 | 11 | 11 | 0,00% | 0,00 | -1,07R | €-118,08 |
| Bilanciata 1H V1 | TRANSITION | 0 | 29 | 29 | 31,03% | 0,90 | -0,07R | €-19,92 |
| Bilanciata 1H V1 | TREND_UP | 3 | 41 | 41 | 39,02% | 1,23 | 0,14R | €58,42 |
| Bilanciata 1H V1 | TREND_UP_HIGH_VOL | 3 | 10 | 10 | 30,00% | 0,78 | -0,17R | €-16,62 |
| Bilanciata 1H V2 | ALT_ROTATION_UP | 0 | 6 | 5 | 66,67% | 3,52 | 0,92R | €55,11 |
| Bilanciata 1H V2 | RANGE | 4 | 7 | 6 | 42,86% | 1,75 | 0,36R | €25,14 |
| Bilanciata 1H V2 | TRANSITION | 4 | 14 | 13 | 35,71% | 1,05 | 0,03R | €4,59 |
| Bilanciata 1H V3 Filtered | ALT_ROTATION_DOWN | 1 | 4 | 4 | 50,00% | 1,82 | 0,43R | €17,15 |
| Bilanciata 1H V3 Filtered | ALT_ROTATION_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,05R | €-20,99 |
| Bilanciata 1H V3 Filtered | RANGE | 5 | 3 | 3 | 66,67% | 3,81 | 0,95R | €28,56 |
| Bilanciata 1H V3 Filtered | RANGE_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,83 |
| Bilanciata 1H V3 Filtered | TRANSITION | 1 | 7 | 7 | 28,57% | 0,74 | -0,20R | €-14,18 |
| Bilanciata 1H V3 Filtered | TREND_UP | 1 | 20 | 20 | 45,00% | 1,54 | 0,31R | €61,36 |
| Bilanciata 1H V3 Filtered | TREND_UP_HIGH_VOL | 3 | 11 | 11 | 27,27% | 0,68 | -0,25R | €-27,79 |
| Rapida 1H V1 | ALT_ROTATION_DOWN | 2 | 9 | 9 | 33,33% | 0,64 | -0,26R | €-23,06 |
| Rapida 1H V1 | ALT_ROTATION_UP | 0 | 13 | 13 | 53,85% | 1,58 | 0,29R | €37,18 |
| Rapida 1H V1 | RANGE | 10 | 39 | 39 | 41,03% | 1,07 | 0,04R | €14,73 |
| Rapida 1H V1 | RANGE_HIGH_VOL | 0 | 11 | 11 | 0,00% | 0,00 | -1,09R | €-119,90 |
| Rapida 1H V1 | TRANSITION | 0 | 25 | 25 | 48,00% | 1,45 | 0,22R | €54,11 |
| Rapida 1H V1 | TREND_UP | 0 | 48 | 48 | 41,67% | 0,97 | -0,02R | €-9,20 |
| Rapida 1H V1 | TREND_UP_HIGH_VOL | 0 | 21 | 21 | 28,57% | 0,59 | -0,28R | €-58,55 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | ALT_ROTATION_DOWN | 2 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,20 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,39R | €13,89 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 1,48R | €29,69 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TREND_UP | 0 | 3 | 3 | 33,33% | 0,68 | -0,23R | €-7,03 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | ALT_ROTATION_DOWN | 2 | 8 | 8 | 37,50% | 0,78 | -0,15R | €-11,63 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,39R | €13,89 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | RANGE | 9 | 3 | 3 | 66,67% | 2,78 | 0,60R | €18,14 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 1,48R | €29,69 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TREND_UP | 0 | 16 | 16 | 25,00% | 0,44 | -0,45R | €-72,21 |
| SHADOW_1H_FAST_NO_PEPE_V1 | ALT_ROTATION_DOWN | 2 | 8 | 8 | 37,50% | 0,78 | -0,15R | €-11,63 |
| SHADOW_1H_FAST_NO_PEPE_V1 | ALT_ROTATION_UP | 0 | 6 | 6 | 50,00% | 1,27 | 0,15R | €8,94 |
| SHADOW_1H_FAST_NO_PEPE_V1 | RANGE | 9 | 4 | 4 | 50,00% | 1,33 | 0,17R | €6,72 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 1,48R | €29,69 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_UP | 0 | 14 | 14 | 21,43% | 0,36 | -0,54R | €-74,90 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | ALT_ROTATION_DOWN | 0 | 5 | 5 | 60,00% | 1,93 | 0,40R | €20,14 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | ALT_ROTATION_UP | 0 | 4 | 4 | 50,00% | 1,23 | 0,13R | €5,07 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | RANGE | 5 | 4 | 4 | 75,00% | 4,23 | 0,82R | €32,91 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_UP | 0 | 8 | 8 | 12,50% | 0,18 | -0,76R | €-61,17 |
| SHADOW_1H_FAST_TP2_V1 | ALT_ROTATION_DOWN | 3 | 6 | 6 | 16,67% | 0,35 | -0,57R | €-34,33 |
| SHADOW_1H_FAST_TP2_V1 | ALT_ROTATION_UP | 0 | 4 | 4 | 25,00% | 0,55 | -0,37R | €-14,93 |
| SHADOW_1H_FAST_TP2_V1 | RANGE | 8 | 4 | 4 | 50,00% | 1,88 | 0,45R | €17,91 |
| SHADOW_1H_FAST_TP2_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,98R | €19,82 |
| SHADOW_1H_FAST_TP2_V1 | TREND_UP | 1 | 13 | 13 | 15,38% | 0,32 | -0,62R | €-80,32 |
| Rapida 1H V2 | ALT_ROTATION_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,10R | €-21,92 |
| Rapida 1H V2 | RANGE | 1 | 3 | 2 | 66,67% | 2,37 | 0,52R | €15,71 |
| Rapida 1H V2 | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -1,14R | €-11,43 |
| Rapida 1H V3 Filtered | ALT_ROTATION_DOWN | 0 | 9 | 9 | 33,33% | 0,66 | -0,24R | €-21,76 |
| Rapida 1H V3 Filtered | ALT_ROTATION_UP | 0 | 5 | 5 | 60,00% | 1,92 | 0,41R | €20,43 |
| Rapida 1H V3 Filtered | RANGE | 7 | 6 | 6 | 66,67% | 2,78 | 0,60R | €36,25 |
| Rapida 1H V3 Filtered | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| Rapida 1H V3 Filtered | TRANSITION | 0 | 6 | 6 | 50,00% | 1,37 | 0,20R | €12,10 |
| Rapida 1H V3 Filtered | TREND_UP | 0 | 29 | 29 | 48,28% | 1,27 | 0,15R | €43,00 |
| Rapida 1H V3 Filtered | TREND_UP_HIGH_VOL | 0 | 20 | 20 | 25,00% | 0,49 | -0,36R | €-72,31 |
| SHADOW_1H_FAST_V3_CAP75_V1 | ALT_ROTATION_DOWN | 0 | 8 | 8 | 37,50% | 0,80 | -0,13R | €-10,34 |
| SHADOW_1H_FAST_V3_CAP75_V1 | ALT_ROTATION_UP | 0 | 4 | 4 | 50,00% | 1,23 | 0,13R | €5,07 |
| SHADOW_1H_FAST_V3_CAP75_V1 | RANGE | 6 | 4 | 4 | 75,00% | 4,23 | 0,82R | €32,91 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_UP | 0 | 11 | 11 | 18,18% | 0,29 | -0,62R | €-68,73 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | ALT_ROTATION_DOWN | 0 | 2 | 2 | 0,00% | 0,00 | -1,08R | €-21,63 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,39R | €13,89 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | RANGE | 2 | 3 | 3 | 66,67% | 2,90 | 0,64R | €19,34 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TREND_UP | 0 | 7 | 7 | 14,29% | 0,20 | -0,75R | €-52,65 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | ALT_ROTATION_DOWN | 0 | 2 | 2 | 0,00% | 0,00 | -1,08R | €-21,63 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,39R | €13,89 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | RANGE | 2 | 3 | 3 | 66,67% | 2,90 | 0,64R | €19,34 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TREND_UP | 0 | 7 | 7 | 14,29% | 0,20 | -0,75R | €-52,65 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 0 | 2 | 2 | 0,00% | 0,00 | -1,08R | €-21,63 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | ALT_ROTATION_UP | 0 | 4 | 4 | 50,00% | 1,23 | 0,13R | €5,07 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | RANGE | 3 | 4 | 4 | 50,00% | 1,45 | 0,23R | €9,11 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_UP | 0 | 6 | 6 | 0,00% | 0,00 | -1,11R | €-66,36 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | ALT_ROTATION_DOWN | 0 | 8 | 8 | 37,50% | 0,80 | -0,13R | €-10,34 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | ALT_ROTATION_UP | 0 | 2 | 2 | 50,00% | 1,27 | 0,15R | €3,00 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | RANGE | 7 | 6 | 6 | 66,67% | 2,78 | 0,60R | €36,25 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TREND_UP | 0 | 14 | 14 | 21,43% | 0,35 | -0,55R | €-77,05 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | ALT_ROTATION_DOWN | 0 | 8 | 8 | 37,50% | 0,80 | -0,13R | €-10,34 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | ALT_ROTATION_UP | 0 | 5 | 5 | 40,00% | 0,83 | -0,12R | €-5,83 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | RANGE | 7 | 6 | 6 | 66,67% | 2,78 | 0,60R | €36,25 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_UP | 0 | 12 | 12 | 16,67% | 0,26 | -0,66R | €-79,74 |
| SHADOW_4H_WIDE | ALT_ROTATION_DOWN | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_4H_WIDE | ALT_ROTATION_UP | 2 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_4H_WIDE | RANGE | 2 | 15 | 15 | 26,67% | 0,98 | -0,01R | €-1,81 |
| SHADOW_4H_WIDE | TRANSITION | 3 | 7 | 7 | 14,29% | 0,46 | -0,47R | €-33,10 |
| SHADOW_4H_WIDE | TREND_UP | 5 | 11 | 11 | 36,36% | 1,55 | 0,36R | €39,44 |
| SHADOW_4H_WIDE | TREND_UP_HIGH_VOL | 4 | 4 | 4 | 0,00% | 0,00 | -1,01R | €-40,53 |
| SHADOW_BOLLINGER_MR_1H | ALT_ROTATION_DOWN | 0 | 3 | 3 | 33,33% | 0,63 | -0,27R | €-8,16 |
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
| SHADOW_COMBO_ADAPTIVE | ALT_ROTATION_DOWN | 2 | 4 | 4 | 50,00% | 1,77 | 0,42R | €16,61 |
| SHADOW_COMBO_ADAPTIVE | ALT_ROTATION_UP | 0 | 6 | 6 | 50,00% | 1,86 | 0,45R | €26,75 |
| SHADOW_COMBO_ADAPTIVE | RANGE | 8 | 16 | 16 | 31,25% | 0,82 | -0,13R | €-21,02 |
| SHADOW_COMBO_ADAPTIVE | RANGE_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,83 |
| SHADOW_COMBO_ADAPTIVE | TRANSITION | 1 | 18 | 18 | 44,44% | 1,48 | 0,28R | €50,23 |
| SHADOW_COMBO_ADAPTIVE | TREND_UP | 2 | 29 | 29 | 44,83% | 1,52 | 0,30R | €87,02 |
| SHADOW_COMBO_ADAPTIVE | TREND_UP_HIGH_VOL | 3 | 9 | 9 | 22,22% | 0,52 | -0,39R | €-35,52 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | ALT_ROTATION_UP | 0 | 4 | 4 | 75,00% | 5,34 | 1,17R | €46,86 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | RANGE | 3 | 2 | 2 | 0,00% | 0,00 | -1,02R | €-20,33 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_UP | 2 | 6 | 6 | 0,00% | 0,00 | -1,09R | €-65,26 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_UP_HIGH_VOL | 0 | 6 | 6 | 16,67% | 0,36 | -0,56R | €-33,65 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | ALT_ROTATION_DOWN | 2 | 4 | 4 | 50,00% | 1,77 | 0,42R | €16,61 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | ALT_ROTATION_UP | 0 | 7 | 7 | 42,86% | 1,37 | 0,22R | €15,64 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE | 8 | 4 | 4 | 50,00% | 1,86 | 0,44R | €17,45 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,83 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TRANSITION | 0 | 3 | 3 | 33,33% | 0,87 | -0,09R | €-2,74 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_UP | 2 | 21 | 21 | 42,86% | 1,42 | 0,25R | €52,12 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_UP_HIGH_VOL | 3 | 11 | 11 | 18,18% | 0,40 | -0,52R | €-57,58 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | ALT_ROTATION_DOWN | 2 | 4 | 4 | 50,00% | 1,77 | 0,42R | €16,61 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | ALT_ROTATION_UP | 0 | 4 | 4 | 75,00% | 5,34 | 1,17R | €46,86 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | RANGE | 8 | 4 | 4 | 50,00% | 1,86 | 0,44R | €17,45 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TRANSITION | 0 | 2 | 2 | 0,00% | 0,00 | -1,09R | €-21,86 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_UP | 2 | 8 | 8 | 0,00% | 0,00 | -1,07R | €-85,56 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_UP_HIGH_VOL | 0 | 7 | 7 | 14,29% | 0,30 | -0,64R | €-44,76 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TRANSITION | 1 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,86 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TREND_UP | 1 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,18 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TRANSITION | 1 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,86 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TREND_UP | 1 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,18 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | ALT_ROTATION_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,84 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | RANGE | 1 | 2 | 2 | 50,00% | 1,95 | 0,48R | €9,63 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TRANSITION | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,18 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TRANSITION | 1 | 3 | 3 | 0,00% | 0,00 | -1,09R | €-32,68 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TREND_UP | 3 | 12 | 12 | 16,67% | 0,36 | -0,57R | €-68,05 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TREND_UP_HIGH_VOL | 0 | 8 | 8 | 12,50% | 0,26 | -0,70R | €-55,87 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_DOWN | 2 | 3 | 3 | 33,33% | 1,35 | 0,25R | €7,43 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_UP | 1 | 4 | 4 | 50,00% | 2,72 | 0,93R | €37,35 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | RANGE | 8 | 3 | 3 | 33,33% | 1,42 | 0,29R | €8,56 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | TRANSITION | 0 | 2 | 2 | 0,00% | 0,00 | -1,09R | €-21,86 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | TREND_UP | 2 | 7 | 7 | 0,00% | 0,00 | -1,06R | €-74,11 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 0,00% | 0,00 | -1,06R | €-42,49 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | ALT_ROTATION_DOWN | 2 | 3 | 3 | 33,33% | 1,35 | 0,25R | €7,43 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | ALT_ROTATION_UP | 1 | 4 | 4 | 50,00% | 2,72 | 0,93R | €37,35 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | RANGE | 8 | 3 | 3 | 33,33% | 1,42 | 0,29R | €8,56 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | TRANSITION | 0 | 2 | 2 | 0,00% | 0,00 | -1,09R | €-21,86 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | TREND_UP | 2 | 7 | 7 | 0,00% | 0,00 | -1,06R | €-74,11 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 0,00% | 0,00 | -1,06R | €-42,49 |
| SHADOW_COMBO_MEAN_REVERSION | ALT_ROTATION_DOWN | 0 | 2 | 2 | 0,00% | 0,00 | -1,08R | €-21,65 |
| SHADOW_COMBO_MEAN_REVERSION | RANGE | 3 | 5 | 5 | 60,00% | 2,11 | 0,48R | €23,92 |
| SHADOW_COMBO_MEAN_REVERSION | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,94 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_UP | 1 | 2 | 2 | 50,00% | 1,50 | 0,25R | €5,04 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,85 |
| SHADOW_COMBO_SCANNER | ALT_ROTATION_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_COMBO_SCANNER | ALT_ROTATION_UP | 0 | 4 | 4 | 50,00% | 2,09 | 0,57R | €22,81 |
| SHADOW_COMBO_SCANNER | RANGE | 3 | 6 | 6 | 50,00% | 2,07 | 0,55R | €32,89 |
| SHADOW_COMBO_SCANNER | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,69 |
| SHADOW_COMBO_SCANNER | TRANSITION | 0 | 14 | 14 | 42,86% | 1,34 | 0,21R | €28,81 |
| SHADOW_COMBO_SCANNER | TREND_UP | 3 | 19 | 19 | 47,37% | 1,84 | 0,47R | €88,76 |
| SHADOW_COMBO_SCANNER | TREND_UP_HIGH_VOL | 1 | 8 | 8 | 37,50% | 1,20 | 0,14R | €10,84 |
| SHADOW_COMBO_TREND | ALT_ROTATION_DOWN | 3 | 2 | 2 | 50,00% | 1,91 | 0,50R | €10,05 |
| SHADOW_COMBO_TREND | ALT_ROTATION_UP | 0 | 5 | 5 | 40,00% | 1,39 | 0,24R | €12,22 |
| SHADOW_COMBO_TREND | RANGE | 6 | 12 | 12 | 25,00% | 0,68 | -0,26R | €-30,79 |
| SHADOW_COMBO_TREND | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,63 |
| SHADOW_COMBO_TREND | TRANSITION | 1 | 14 | 14 | 42,86% | 1,55 | 0,33R | €46,22 |
| SHADOW_COMBO_TREND | TREND_UP | 2 | 23 | 23 | 34,78% | 1,10 | 0,07R | €15,44 |
| SHADOW_COMBO_TREND | TREND_UP_HIGH_VOL | 3 | 8 | 8 | 25,00% | 0,68 | -0,25R | €-20,22 |
| SHADOW_DOGE_BOLLINGER_1H | RANGE | 1 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,33 |
| SHADOW_DOGE_DONCHIAN_1H | RANGE | 1 | 2 | 2 | 50,00% | 1,67 | 0,38R | €7,50 |
| SHADOW_DOGE_EMA_1H | RANGE | 1 | 3 | 3 | 66,67% | 3,40 | 0,89R | €26,67 |
| SHADOW_DONCHIAN_1H | ALT_ROTATION_DOWN | 2 | 2 | 2 | 50,00% | 2,19 | 0,65R | €13,05 |
| SHADOW_DONCHIAN_1H | ALT_ROTATION_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,85 |
| SHADOW_DONCHIAN_1H | RANGE | 3 | 12 | 12 | 25,00% | 0,76 | -0,19R | €-22,61 |
| SHADOW_DONCHIAN_1H | RANGE_HIGH_VOL | 1 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_DONCHIAN_1H | TRANSITION | 1 | 6 | 6 | 16,67% | 0,45 | -0,48R | €-28,95 |
| SHADOW_DONCHIAN_1H | TREND_UP | 0 | 11 | 11 | 45,45% | 1,89 | 0,53R | €57,82 |
| SHADOW_DONCHIAN_1H | TREND_UP_HIGH_VOL | 2 | 4 | 4 | 50,00% | 2,23 | 0,67R | €26,65 |
| SHADOW_EMA_TREND_1H | ALT_ROTATION_DOWN | 2 | 3 | 3 | 33,33% | 0,98 | -0,02R | €-0,50 |
| SHADOW_EMA_TREND_1H | ALT_ROTATION_UP | 0 | 5 | 5 | 20,00% | 0,52 | -0,40R | €-20,11 |
| SHADOW_EMA_TREND_1H | RANGE | 6 | 13 | 13 | 23,08% | 0,68 | -0,23R | €-30,49 |
| SHADOW_EMA_TREND_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,63 |
| SHADOW_EMA_TREND_1H | TRANSITION | 2 | 14 | 14 | 42,86% | 1,55 | 0,33R | €46,21 |
| SHADOW_EMA_TREND_1H | TREND_UP | 2 | 28 | 28 | 32,14% | 1,02 | 0,02R | €4,61 |
| SHADOW_EMA_TREND_1H | TREND_UP_HIGH_VOL | 3 | 8 | 8 | 37,50% | 1,23 | 0,15R | €12,10 |
| SHADOW_ETH_ADAPTIVE_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_ETH_ADAPTIVE_1H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,89R | €18,89 |
| SHADOW_ETH_ADAPTIVE_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_ETH_BOLLINGER_1H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,33 |
| SHADOW_ETH_DONCHIAN_1H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_ETH_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,68 | 0,38R | €7,64 |
| SHADOW_ETH_EMA_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_ETH_EMA_1H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,89R | €18,89 |
| SHADOW_ETH_EMA_1H | TREND_UP_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_ETH_EMA_4H | TREND_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_GLOBAL_PURE | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,10R | €-11,00 |
| SHADOW_GLOBAL_PURE | RANGE | 1 | 1 | 1 | 100,00% | ∞ | 2,40R | €24,00 |
| SHADOW_GLOBAL_PURE | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,42R | €14,17 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | ALT_ROTATION_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,79 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | RANGE | 2 | 2 | 2 | 0,00% | 0,00 | -1,02R | €-20,33 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 1,94R | €38,87 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TREND_UP | 3 | 7 | 7 | 0,00% | 0,00 | -1,08R | €-75,64 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,86 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | RANGE | 3 | 2 | 2 | 0,00% | 0,00 | -1,02R | €-20,33 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TREND_UP | 2 | 10 | 10 | 10,00% | 0,21 | -0,77R | €-77,01 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | RANGE | 3 | 2 | 2 | 0,00% | 0,00 | -1,02R | €-20,33 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TREND_UP | 2 | 11 | 11 | 9,09% | 0,18 | -0,80R | €-87,73 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,86 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | RANGE | 3 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,15 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | TREND_UP | 2 | 10 | 10 | 10,00% | 0,31 | -0,67R | €-67,01 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | RANGE | 3 | 2 | 2 | 50,00% | 1,95 | 0,48R | €9,67 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TREND_UP | 1 | 10 | 10 | 0,00% | 0,00 | -1,07R | €-107,43 |
| SHADOW_MASTER_ADAPTIVE_V1 | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_MASTER_ADAPTIVE_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,86 |
| SHADOW_MASTER_ADAPTIVE_V1 | RANGE | 3 | 2 | 2 | 0,00% | 0,00 | -1,02R | €-20,33 |
| SHADOW_MASTER_ADAPTIVE_V1 | TREND_UP | 2 | 10 | 10 | 10,00% | 0,21 | -0,77R | €-77,01 |
| Forza relativa 1H V1 | ALT_ROTATION_DOWN | 1 | 4 | 4 | 0,00% | 0,00 | -1,05R | €-42,19 |
| Forza relativa 1H V1 | ALT_ROTATION_UP | 0 | 13 | 13 | 30,77% | 0,90 | -0,07R | €-9,26 |
| Forza relativa 1H V1 | RANGE | 7 | 23 | 23 | 21,74% | 0,60 | -0,31R | €-70,55 |
| Forza relativa 1H V1 | RANGE_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -1,03R | €-31,02 |
| Forza relativa 1H V1 | TRANSITION | 0 | 15 | 15 | 46,67% | 1,84 | 0,46R | €69,26 |
| Forza relativa 1H V1 | TREND_UP | 3 | 35 | 35 | 37,14% | 1,43 | 0,24R | €84,59 |
| Forza relativa 1H V1 | TREND_UP_HIGH_VOL | 1 | 8 | 8 | 12,50% | 0,30 | -0,64R | €-51,15 |
| Forza relativa 1H V2 | ALT_ROTATION_DOWN | 2 | 1 | 1 | 100,00% | ∞ | 2,11R | €21,13 |
| Forza relativa 1H V2 | ALT_ROTATION_UP | 0 | 4 | 4 | 50,00% | 2,00 | 0,54R | €21,41 |
| Forza relativa 1H V2 | RANGE | 2 | 3 | 3 | 66,67% | 4,31 | 1,12R | €33,59 |
| Forza relativa 1H V2 | TRANSITION | 2 | 9 | 8 | 33,33% | 1,05 | 0,03R | €3,12 |
| Forza relativa 1H V2 | TREND_UP | 0 | 11 | 10 | 45,45% | 1,77 | 0,43R | €47,60 |
| Forza relativa 1H V2 | TREND_UP_HIGH_VOL | 0 | 4 | 3 | 0,00% | 0,00 | -1,04R | €-41,60 |
| SHADOW_SCANNER_BOTTOM5_SHORT | ALT_ROTATION_DOWN | 1 | 3 | 3 | 66,67% | 3,53 | 0,91R | €27,28 |
| SHADOW_SCANNER_BOTTOM5_SHORT | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| SHADOW_SCANNER_BOTTOM5_SHORT | RANGE | 5 | 9 | 9 | 22,22% | 0,50 | -0,42R | €-37,98 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TRANSITION | 0 | 14 | 14 | 28,57% | 0,85 | -0,09R | €-13,14 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP | 0 | 7 | 7 | 0,00% | 0,00 | -0,73R | €-51,04 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP_HIGH_VOL | 1 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,24 |
| SHADOW_SCANNER_TOP5_BTC | ALT_ROTATION_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_SCANNER_TOP5_BTC | ALT_ROTATION_UP | 0 | 5 | 5 | 40,00% | 1,39 | 0,25R | €12,28 |
| SHADOW_SCANNER_TOP5_BTC | RANGE | 2 | 7 | 7 | 42,86% | 2,05 | 0,47R | €32,91 |
| SHADOW_SCANNER_TOP5_BTC | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,69 |
| SHADOW_SCANNER_TOP5_BTC | TRANSITION | 0 | 12 | 12 | 41,67% | 1,49 | 0,30R | €36,18 |
| SHADOW_SCANNER_TOP5_BTC | TREND_UP | 3 | 18 | 18 | 44,44% | 1,64 | 0,38R | €68,05 |
| SHADOW_SCANNER_TOP5_BTC | TREND_UP_HIGH_VOL | 1 | 8 | 8 | 37,50% | 1,20 | 0,14R | €10,84 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | ALT_ROTATION_DOWN | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,86 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 2,19R | €21,87 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TREND_UP | 2 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TREND_UP_HIGH_VOL | 0 | 6 | 6 | 16,67% | 0,40 | -0,53R | €-31,93 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | ALT_ROTATION_DOWN | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,86 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | RANGE | 2 | 2 | 2 | 0,00% | 0,00 | -1,02R | €-20,33 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 2,19R | €21,87 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_UP | 2 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_UP_HIGH_VOL | 0 | 6 | 6 | 16,67% | 0,40 | -0,53R | €-31,93 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | ALT_ROTATION_DOWN | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,79 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | RANGE | 2 | 2 | 2 | 0,00% | 0,00 | -1,02R | €-20,33 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 2,19R | €21,87 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | ALT_ROTATION_DOWN | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,79 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | RANGE | 2 | 2 | 2 | 0,00% | 0,00 | -1,02R | €-20,33 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 2,19R | €21,87 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | ALT_ROTATION_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,79 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | RANGE | 2 | 2 | 2 | 0,00% | 0,00 | -1,02R | €-20,33 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 2,19R | €21,87 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_UP | 2 | 2 | 2 | 0,00% | 0,00 | -1,07R | €-21,47 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | ALT_ROTATION_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,79 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | RANGE | 2 | 2 | 2 | 0,00% | 0,00 | -1,02R | €-20,33 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 2,19R | €21,87 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_UP | 2 | 2 | 2 | 0,00% | 0,00 | -1,07R | €-21,47 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | ALT_ROTATION_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,79 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | RANGE | 2 | 2 | 2 | 0,00% | 0,00 | -1,02R | €-20,33 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 2,19R | €21,87 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_UP | 3 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_UP_HIGH_VOL | 2 | 7 | 7 | 28,57% | 0,80 | -0,15R | €-10,74 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | ALT_ROTATION_UP | 1 | 3 | 3 | 33,33% | 1,34 | 0,25R | €7,49 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | RANGE | 2 | 2 | 2 | 0,00% | 0,00 | -1,02R | €-20,33 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 2,99R | €29,87 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_UP | 3 | 3 | 3 | 0,00% | 0,00 | -1,09R | €-32,57 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -1,05R | €-31,38 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | ALT_ROTATION_UP | 1 | 3 | 3 | 33,33% | 1,34 | 0,25R | €7,49 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | RANGE | 2 | 2 | 2 | 0,00% | 0,00 | -1,02R | €-20,33 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 2,99R | €29,87 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_UP | 3 | 3 | 3 | 0,00% | 0,00 | -1,09R | €-32,57 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -1,05R | €-31,38 |
| SHADOW_SCANNER_TOP5_LONG | ALT_ROTATION_DOWN | 1 | 2 | 2 | 0,00% | 0,00 | -1,11R | €-22,22 |
| SHADOW_SCANNER_TOP5_LONG | ALT_ROTATION_UP | 0 | 6 | 6 | 33,33% | 0,92 | -0,06R | €-3,32 |
| SHADOW_SCANNER_TOP5_LONG | RANGE | 2 | 8 | 8 | 50,00% | 2,49 | 0,58R | €46,78 |
| SHADOW_SCANNER_TOP5_LONG | RANGE_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,83 |
| SHADOW_SCANNER_TOP5_LONG | TRANSITION | 0 | 12 | 12 | 41,67% | 1,36 | 0,22R | €26,18 |
| SHADOW_SCANNER_TOP5_LONG | TREND_UP | 3 | 27 | 27 | 48,15% | 1,71 | 0,39R | €105,70 |
| SHADOW_SCANNER_TOP5_LONG | TREND_UP_HIGH_VOL | 2 | 7 | 7 | 42,86% | 1,36 | 0,22R | €15,34 |
| SHADOW_SOL_ADAPTIVE_1H | RANGE | 2 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_SOL_ADAPTIVE_1H | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,89R | €18,89 |
| SHADOW_SOL_ADAPTIVE_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,10R | €-10,96 |
| SHADOW_SOL_ADAPTIVE_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,05R | €-10,52 |
| SHADOW_SOL_BOLLINGER_1H | RANGE | 1 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,33 |
| SHADOW_SOL_BOLLINGER_4H | TREND_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SOL_DONCHIAN_1H | RANGE | 1 | 1 | 1 | 0,00% | 0,00 | -1,12R | €-11,25 |
| SHADOW_SOL_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,08 |
| SHADOW_SOL_DONCHIAN_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,56 |
| SHADOW_SOL_EMA_1H | RANGE | 1 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_SOL_EMA_1H | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,89R | €18,89 |
| SHADOW_SOL_EMA_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,10R | €-10,96 |
| SHADOW_SOL_EMA_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,56 |

Il P&L è normalizzato a **€10 di rischio per evento**, così leva e size non falsano il confronto.
La matrice diventerà utilizzabile per una rotazione automatica soltanto dopo un campione sufficiente per ciascuna coppia strategia-regime.

# Block 3 — Shadow Exit Engine

Generato: 2026-07-23T19:53:43+00:00

> Motore esclusivamente osservativo e Paper-only. Non modifica le uscite reali. I confronti escludono il funding sia dall'uscita originale sia dalle varianti.

## Stato operativo

- Gruppi di trade ancora monitorati: **331**
- Scenari virtuali ancora attivi: **3175**
- Gruppi in attesa dell'uscita originale: **184**
- Gruppi con originale chiuso ma Shadow ancora attive: **147**
- Confronti completati: **13022**

## Classifica osservativa complessiva

| Scenario | Campione completo | Campione totale | Δ medio vs originale | Migliora | Troppo presto | Troppo tardi | Stato dati |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| GB20_R050 | 613 | 676 | +€6,42 | 46,7% | 167 | 1 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R050 | 613 | 676 | +€4,36 | 45,7% | 169 | 8 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R050 | 613 | 676 | +€2,19 | 44,7% | 171 | 13 | READY_FOR_BLOCK4_EVALUATION |
| TP_R050 | 613 | 676 | +€0,83 | 43,9% | 189 | 0 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R050 | 610 | 673 | +€0,83 | 43,2% | 167 | 22 | READY_FOR_BLOCK4_EVALUATION |
| GB20_R100 | 605 | 668 | +€3,99 | 38,2% | 144 | 19 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R100 | 605 | 668 | +€2,14 | 37,6% | 136 | 31 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R100 | 605 | 668 | +€1,30 | 37,7% | 112 | 52 | READY_FOR_BLOCK4_EVALUATION |
| TP_R100 | 605 | 668 | +€1,26 | 35,6% | 161 | 19 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R100 | 602 | 665 | +€1,35 | 34,9% | 79 | 99 | READY_FOR_BLOCK4_EVALUATION |
| ATR15_R100 | 597 | 660 | €-0,19 | 32,3% | 36 | 143 | READY_FOR_BLOCK4_EVALUATION |
| TIME_6H | 596 | 659 | +€0,63 | 51,0% | 126 | 83 | READY_FOR_BLOCK4_EVALUATION |
| ATR20_R100 | 591 | 654 | €-2,98 | 28,7% | 42 | 155 | READY_FOR_BLOCK4_EVALUATION |
| TP_R150 | 590 | 653 | +€0,46 | 27,0% | 72 | 72 | READY_FOR_BLOCK4_EVALUATION |
| TIME_12H | 568 | 631 | +€1,27 | 44,2% | 55 | 125 | READY_FOR_BLOCK4_EVALUATION |
| TP_R200 | 567 | 630 | +€0,22 | 32,2% | 33 | 106 | READY_FOR_BLOCK4_EVALUATION |
| ATR30_R100 | 566 | 629 | €-8,08 | 24,3% | 38 | 155 | READY_FOR_BLOCK4_EVALUATION |
| TIME_24H | 563 | 626 | €-2,77 | 31,5% | 32 | 167 | READY_FOR_BLOCK4_EVALUATION |
| BE_R050 | 535 | 598 | €-7,11 | 28,4% | 94 | 86 | READY_FOR_BLOCK4_EVALUATION |
| BE_R100 | 506 | 568 | €-14,48 | 18,5% | 37 | 139 | READY_FOR_BLOCK4_EVALUATION |

## Come leggere il controllo

- **EARLIER_BETTER**: la variante è uscita prima e ha conservato più profitto.
- **TOO_EARLY**: la variante è uscita prima ma ha tagliato un movimento migliore.
- **LATER_BETTER**: la variante ha continuato dopo l'uscita originale e ha guadagnato di più.
- **TOO_LATE**: la variante è rimasta aperta più a lungo e ha peggiorato il risultato.

## Limiti e protezioni

Le regole Shadow mantengono entrata, quantità, commissioni, stop protettivo iniziale e liquidazione. Le ambiguità all'interno della stessa candela vengono risolte scegliendo l'esito peggiore. Le posizioni già aperte al momento dell'installazione sono marcate come campione parziale e non saranno utilizzate dal futuro Blocco 4 come prova piena.

# Blocco 4 — Valutazione statistica Shadow

Generato: 2026-07-23T19:53:44+00:00

> Modulo esclusivamente valutativo. Non modifica strategie, uscite, posizioni o capitale. Le candidature vengono consegnate al futuro Blocco 5, senza applicazione automatica.

## Stato

- Risultati Block 3 disponibili: **13022**
- Valutazioni prodotte: **3984**
- Candidature al Blocco 5: **0**
- Mutazioni create automaticamente: **0**

## Classifica complessiva

| Scenario | Campione pieno | Δ medio (R) | Mediana (R) | CI bootstrap basso | Migliora | Score | Stato |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| ATR20_R100 | 26 | 0,317 | 0,408 | 0,190 | 92,3% | 84,1 | INSUFFICIENT_DATA |
| GB30_R100 | 27 | 0,664 | 0,477 | 0,489 | 100,0% | 83,8 | INSUFFICIENT_DATA |
| GB40_R100 | 27 | 0,588 | 0,477 | 0,429 | 92,6% | 83,8 | INSUFFICIENT_DATA |
| GB40_R050 | 27 | 0,543 | 0,477 | 0,336 | 88,9% | 83,8 | INSUFFICIENT_DATA |
| GB30_R050 | 27 | 0,611 | 0,477 | 0,396 | 96,3% | 83,8 | INSUFFICIENT_DATA |
| GB20_R100 | 27 | 0,729 | 0,477 | 0,543 | 100,0% | 83,7 | INSUFFICIENT_DATA |
| GB20_R050 | 27 | 0,680 | 0,477 | 0,452 | 96,3% | 83,7 | INSUFFICIENT_DATA |
| TP_R100 | 27 | 0,540 | 0,477 | 0,332 | 88,9% | 83,7 | INSUFFICIENT_DATA |
| ATR15_R100 | 26 | 0,375 | 0,408 | 0,290 | 92,3% | 83,5 | INSUFFICIENT_DATA |
| GB50_R100 | 27 | 0,598 | 0,477 | 0,424 | 92,6% | 83,3 | INSUFFICIENT_DATA |
| GB50_R050 | 27 | 0,560 | 0,477 | 0,349 | 92,6% | 83,3 | INSUFFICIENT_DATA |
| TP_R200 | 27 | 0,283 | 0,330 | 0,075 | 77,8% | 82,3 | INSUFFICIENT_DATA |
| TP_R150 | 27 | 0,190 | 0,287 | 0,002 | 66,7% | 80,2 | INSUFFICIENT_DATA |
| ATR30_R100 | 25 | 0,265 | 0,365 | 0,077 | 88,0% | 80,0 | INSUFFICIENT_DATA |
| BE_R050 | 25 | 0,265 | 0,365 | 0,087 | 88,0% | 80,0 | INSUFFICIENT_DATA |
| BE_R100 | 25 | 0,265 | 0,365 | 0,076 | 88,0% | 80,0 | INSUFFICIENT_DATA |
| TP_R050 | 27 | 0,337 | 0,408 | 0,119 | 88,9% | 78,9 | INSUFFICIENT_DATA |
| TIME_6H | 568 | 0,047 | 0,039 | -0,028 | 53,0% | 78,5 | VALIDATING |
| TIME_24H | 6 | 0,997 | 1,104 | 0,180 | 66,7% | 74,1 | INSUFFICIENT_DATA |
| GB30_R050 | 580 | 0,089 | 0,000 | 0,021 | 44,1% | 70,1 | VALIDATING |

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

Generato: 2026-07-23T19:53:52+00:00

Questi profili sono osservativi e Paper-only. Usano gli stessi trade della madre, ma applicano una specifica uscita Block 3 soltanto ai segnali aperti dopo la loro registrazione.
Nessuna promozione, modifica live o operazione reale viene eseguita automaticamente.

| Challenger | Madre | Scenario | Chiusi | Copertura | PF | PnL | Exp/trade | DD | Stato |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Rapida 1H V1 — giveback 20% dopo +0,5R | SHADOW_1H_FAST | GB20_R050 | 5 | 100,00% | 1,93 | +€101,13 | +€20,23 | 1,08% | COLLECTING |
| Rapida 1H V1 — giveback 30% dopo +0,5R | SHADOW_1H_FAST | GB30_R050 | 5 | 100,00% | 1,68 | +€73,85 | +€14,77 | 1,08% | COLLECTING |
| Relative Strength — giveback 20% dopo +0,5R | SHADOW_RELATIVE_STRENGTH | GB20_R050 | 1 | 100,00% | 0,00 | €-54,01 | €-54,01 | 0,54% | COLLECTING |
| Relative Strength — giveback 30% dopo +0,5R | SHADOW_RELATIVE_STRENGTH | GB30_R050 | 1 | 100,00% | 0,00 | €-54,01 | €-54,01 | 0,54% | COLLECTING |

## Regole di valutazione

- Prima fotografia a 30 trade indipendenti.
- Revisione per possibile promozione a 50 trade indipendenti.
- PF minimo 1,50, expectancy e PnL positivi, drawdown massimo 15%, copertura minima 90%.
- PF deve superare la madre e il drawdown non deve essere peggiore sulla stessa serie di trade.
- La promozione resta una decisione umana protetta; il rollback viene predisposto soltanto in fase di approvazione.

# Blocco 4.5 — Crash Cascade Guard

Generato: 2026-07-23T19:53:36+00:00

> Paper-only. In mercato NORMAL/WATCH non riduce i segnali. Le limitazioni iniziano soltanto in STRESS, RECOVERY, CRASH, EXTREME o con dati non affidabili.

## Stato corrente

- Livello: **NORMAL**
- Direzione: **NONE**
- Segnali bloccati nel ciclo: **0**
- Simulazioni bloccate attive: **25**
- Simulazioni completate nel ciclo: **0**
- Liquidazioni virtuali evitate totali: **0**
- Valore cumulato del filtro: **9.33 R**
- Profitto virtuale mancato: **11.92 R**

## Stress test portafogli Paper

| Scenario | Posizioni interessate | Liquidazioni stimate | Perdita stimata EUR |
| --- | ---: | ---: | ---: |
| DOWN_10 | 122 | 0 | 14506.12 |
| DOWN_20 | 122 | 0 | 29012.24 |
| DOWN_30 | 122 | 5 | 43601.86 |
| DOWN_40 | 122 | 36 | 54968.23 |
| UP_10 | 62 | 0 | 16474.99 |
| UP_20 | 62 | 0 | 32949.97 |
| UP_30 | 62 | 0 | 49424.96 |
| UP_40 | 62 | 35 | 58354.67 |

## Modello di esecuzione

Se una candela di cascata attraversa nello stesso intervallo sia lo stop sia il prezzo di liquidazione, il Paper usa il caso peggiore e registra una liquidazione intrabar. Gli stop in gap o in regime di stress ricevono slippage aggiuntivo.

## Requisiti prima del live futures

- modalità ISOLATED obbligatoria;
- stop nativo sull'exchange;
- conferma dello stop prima di accettare la posizione;
- cross margin vietato.

# Blocco 5 — Candidati evolutivi controllati

Generato: 2026-07-23T19:53:12+00:00

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

Generato: 2026-07-23T19:53:52+00:00

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

Generato: 2026-07-23T19:53:52+00:00

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

Generato: 2026-07-23T19:53:52+00:00

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

Generato: 2026-07-23T19:53:52+00:00

> Paper-only. La memoria può bloccare soltanto una futura proposta Block 5 classificata AVOID; non modifica strategie esistenti.

## Stato

- Strategie/portafogli valutati: **84**
- Hall of Fame: **4**
- Memorie genetiche: **0**
- Firme bloccate: **0**
- Azioni automatiche e live: **0**

## Hall of Fame

| Rank | Strategia | Stato | Score | Grade | Trade | PF | Expectancy R | DD R |
| ---: | --- | --- | ---: | --- | ---: | ---: | ---: | ---: |
| 1 | SHADOW_1H_BALANCED | BASELINE | 14.4 | E | 35 | 1.42 | 0.170 | 4.17 |
| 2 | SHADOW_1H_BALANCED_V3 | BASELINE | 12.7 | E | 30 | 1.29 | 0.156 | 3.23 |
| 3 | SHADOW_1H_FAST_V3 | BASELINE | 11.7 | E | 52 | 1.17 | 0.064 | 5.36 |
| 4 | SHADOW_1H_FAST | BASELINE | 7.3 | E | 60 | 0.96 | -0.020 | 13.48 |

## Memoria genetica

| Scope | Famiglia | Mutazione | Target | Stato | Score | Prove | Coppie | Blocco |
| --- | --- | --- | --- | --- | ---: | ---: | ---: | --- |
| — | — | Nessuna candidata ancora creata | — | INSUFFICIENT | 0 | 0 | 0 | NO |

## Sicurezza

- Nessuna strategia, posizione o promozione esistente viene modificata.
- Nessuna mutazione, promozione, pensionamento o rollback automatico.
- Nessun effetto live e nessun ordine reale.

# Blocco 10 — Regime Fitness e specializzazione

Generato: 2026-07-23T19:53:52+00:00

> Paper-only e advisory. Il blocco misura quali strategie funzionano nei diversi regimi, ma non cambia automaticamente strategia o posizione.

## Stato

- Regime corrente: **RANGE**
- Righe di performance: **306**
- Strategie preferite nel regime corrente: **0**
- Strategie da evitare nel regime corrente: **0**
- Memorie contestuali: **153**
- Routing automatico: **NO**

## Classifica del regime corrente

| Rank | Portafoglio | Famiglia | Stato | Fitness | Trade | PF | Expectancy R | DD R |
| ---: | --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| 1 | SHADOW_DOGE_DONCHIAN_1H | shadow-doge-donchian-1h | INSUFFICIENT | 80.8 | 2 | 99.00 | 0.548 | 0.00 |
| 2 | SHADOW_BTC_BOLLINGER_1H | shadow-btc-bollinger-1h | INSUFFICIENT | 80.8 | 2 | 99.00 | 0.997 | 0.00 |
| 3 | SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | shadow-scanner-top5-btc-guard-btc-le3-v1 | INSUFFICIENT | 80.4 | 1 | 99.00 | 2.181 | 0.00 |
| 4 | SHADOW_DOGE_EMA_1H | shadow-doge-ema-1h | INSUFFICIENT | 77.8 | 5 | 4.56 | 0.781 | 1.10 |
| 5 | SHADOW_COMBO_ADAPTIVE | shadow-combo-adaptive | OBSERVING | 77.8 | 18 | 2.10 | 0.333 | 1.10 |
| 6 | SHADOW_ETH_BOLLINGER_1H | shadow-eth-bollinger-1h | INSUFFICIENT | 76.6 | 1 | 99.00 | 0.309 | 0.00 |
| 7 | SHADOW_SCANNER_TOP5_LONG | shadow-scanner-top5-long | OBSERVING | 73.5 | 21 | 1.94 | 0.380 | 4.17 |
| 8 | SHADOW_SCANNER_TOP5_BTC | shadow-scanner-top5-btc | OBSERVING | 69.1 | 17 | 1.87 | 0.328 | 3.09 |
| 9 | SHADOW_SCANNER_TOP5_BTC_TP3_V1 | shadow-scanner-top5-btc-tp3-v1 | INSUFFICIENT | 66.0 | 4 | 1.84 | 0.449 | 2.15 |
| 10 | SHADOW_COMBO_SCANNER | shadow-combo-scanner | OBSERVING | 62.9 | 17 | 1.65 | 0.282 | 3.09 |

## Sicurezza

- Il regime viene assegnato usando solo l'ultimo record noto prima dell'entrata del trade.
- Nessun uso di dati futuri per classificare il trade.
- Il Candidate Regime Gate è advisory per impostazione predefinita.
- Nessun cambio automatico di MASTER, posizione o live.

# Blocco 11 — Collegamento protetto al live

Generato: 2026-07-23T19:53:52+00:00

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

Generato: 2026-07-23T19:53:36+00:00

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
