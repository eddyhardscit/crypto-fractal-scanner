# Paper trading automatico KuCoin

Generato: 2026-07-27T18:24:44+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-07-27T18:23:26+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-07-27T18:23:26+00:00 | 2026-07-27T18:23:26+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-07-27T18:00:00+00:00 | 2026-07-27T18:00:00+00:00 | 8,5 min | 25,0 min | OK |
| 60m | 12 | 2026-07-27T17:00:00+00:00 | 2026-07-27T17:00:00+00:00 | 23,5 min | 45,0 min | OK |
| 240m | 12 | 2026-07-27T12:00:00+00:00 | 2026-07-27T12:00:00+00:00 | 2,39 h | 1,00 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | HYPE | 240m | SHORT | -7,61 | 6,00 | 0,00 | STALE_CANDLE | 2,39 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 143.5 minuti; tolleranza 60 minuti. |
| Principale 4H | PEPE | 240m | LONG | 7,32 | 6,00 | 0,00 | STALE_CANDLE | 2,39 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 143.5 minuti; tolleranza 60 minuti. |
| Principale 4H | ENA | 240m | LONG | 6,67 | 6,00 | 0,00 | STALE_CANDLE | 2,39 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 143.5 minuti; tolleranza 60 minuti. |
| Principale 4H | ETH | 240m | LONG | 6,63 | 6,00 | 0,00 | STALE_CANDLE | 2,39 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 143.5 minuti; tolleranza 60 minuti. |
| Principale 4H | ZEC | 240m | SHORT | -6,50 | 6,00 | 0,00 | STALE_CANDLE | 2,39 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 143.5 minuti; tolleranza 60 minuti. |
| Principale 4H | AKE | 240m | LONG | 6,25 | 6,00 | 0,00 | STALE_CANDLE | 2,39 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 143.5 minuti; tolleranza 60 minuti. |
| Principale 4H | SHIB | 240m | LONG | 5,75 | 6,00 | 0,25 | STALE_CANDLE | 2,39 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 143.5 minuti; tolleranza 60 minuti. |
| Principale 4H | DOGE | 240m | SHORT | -4,58 | 6,00 | 1,42 | STALE_CANDLE | 2,39 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 143.5 minuti; tolleranza 60 minuti. |
| Principale 4H | XRP | 240m | SHORT | -4,39 | 6,00 | 1,61 | STALE_CANDLE | 2,39 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 143.5 minuti; tolleranza 60 minuti. |
| Principale 4H | SOL | 240m | SHORT | -3,75 | 6,00 | 2,25 | STALE_CANDLE | 2,39 h | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 143.5 minuti; tolleranza 60 minuti. |
| Principale 4H | BANK | 240m | LONG | 2,75 | 6,00 | 3,25 | STALE_CANDLE | 2,39 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 143.5 minuti; tolleranza 60 minuti. |
| Principale 4H | BTC | 240m | SHORT | 0,00 | 6,00 | 6,00 | STALE_CANDLE | 2,39 h | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 143.5 minuti; tolleranza 60 minuti. |
| Benchmark Bollinger mean reversion 1H | BANK | 60m | SHORT | -7,75 | 5,00 | 0,00 | READY | 23,5 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Benchmark trend following EMA 1H | BANK | 60m | SHORT | -7,75 | 5,00 | 0,00 | READY | 23,5 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Bilanciata 1H V2 | AKE | 60m | LONG | 7,75 | 5,50 | 0,00 | STRATEGY_FILTER | 23,5 min | D: n/a | W: n/a | peso 0 | Filtro V2 non superato: regime, EMA, ritorni e RSI; per Rapida V2 servono anche breakout reale, volume e ADX. |
| Rapida 1H V1 — madre | AKE | 60m | LONG | 7,75 | 4,50 | 0,00 | STRATEGY_FILTER | 23,5 min | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout UP oppure movimento breve ≥1,5%; breakout=NONE, movimento=+0.15%. |
| Rapida V1 — score 6–7,5 | AKE | 60m | LONG | 7,75 | 6,00 | 0,00 | STRATEGY_FILTER | 23,5 min | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout UP oppure movimento breve ≥1,5%; breakout=NONE, movimento=+0.15%. |
| Rapida score 6–7,5 — senza Trend Up | AKE | 60m | LONG | 7,75 | 6,00 | 0,00 | STRATEGY_FILTER | 23,5 min | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout UP oppure movimento breve ≥1,5%; breakout=NONE, movimento=+0.15%. |
| Rapida score 6–7,5 — Range Only | AKE | 60m | LONG | 7,75 | 6,00 | 0,00 | STRATEGY_FILTER | 23,5 min | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout UP oppure movimento breve ≥1,5%; breakout=NONE, movimento=+0.15%. |
| Rapida score 6–7,5 — Cost Aware | AKE | 60m | LONG | 7,75 | 6,00 | 0,00 | STRATEGY_FILTER | 23,5 min | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout UP oppure movimento breve ≥1,5%; breakout=NONE, movimento=+0.15%. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.756,81 | -2,43% | €-243,19 | €3.000,00 | -8,11% | 5 | 24 | 29,17% | 0,71 | 4,76% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 24 | 822 | CAMPIONE INSUFFICIENTE | 30 (mancano 6) |

- Trade del Principale 4H chiusi: **24**; win rate **29,17%**; profit factor **0,71**.
- Expectancy: **€-10,51** per trade; P&L netto: **€-252,20**; max drawdown: **4,76%**.
- Valutazione: **Servono altri eventi indipendenti prima di trarre conclusioni.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 5 | €9.756,81 | €1.366,40 | €4.099,20 | €145,85 | €10,75 |
| TEST | Benchmark Donchian breakout 1H | 6 | €10.704,17 | €4.746,56 | €9.493,11 | €160,54 | €66,13 |
| TEST | Bilanciata 1H V3 Filtered | 6 | €10.605,92 | €1.210,97 | €3.632,92 | €210,47 | €-19,97 |
| TEST | Scanner Top 5 Long 1H | 3 | €10.561,83 | €1.250,32 | €2.500,65 | €55,50 | €10,45 |
| TEST | Rapida V1 — no HIGH + score <7,5 | 3 | €10.538,06 | €629,70 | €1.889,10 | €156,12 | €-5,22 |
| TEST | Rapida V3 — score <7,5 | 4 | €10.502,99 | €661,37 | €1.984,12 | €157,85 | €-5,44 |
| TEST | Rapida V1 — score 6–7,5 | 3 | €10.477,01 | €1.329,71 | €3.989,14 | €156,74 | €-13,95 |
| TEST | Rapida score 6–7,5 — Cost Aware | 3 | €10.437,48 | €1.324,02 | €3.972,05 | €155,98 | €-13,89 |
| TEST | Scanner Top 5 + forza BTC 1H | 5 | €10.400,61 | €1.405,48 | €2.810,97 | €107,64 | €31,89 |
| TEST | Rapida V3 NoHigh — Regime Guard | 1 | €10.395,73 | €172,19 | €516,57 | €51,51 | €0,00 |
| TEST | Rapida score 6–7,5 — senza Trend Up | 3 | €10.364,58 | €1.436,40 | €4.309,21 | €153,39 | €-8,68 |
| TEST | Bilanciata 1H V1 | 6 | €10.344,64 | €2.239,37 | €6.718,11 | €105,39 | €67,61 |
| TEST | Rapida V3 senza ESPORTS — MFE Lock | 6 | €10.332,06 | €2.993,61 | €8.980,83 | €155,47 | €64,76 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 1 | €10.328,64 | €144,01 | €432,02 | €51,84 | €-5,13 |
| TEST | Rapida score 6–7,5 — Range Only | 2 | €10.320,70 | €399,26 | €1.197,78 | €102,92 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 5 | €10.314,90 | €2.549,45 | €7.648,36 | €155,32 | €55,01 |
| TEST | Rapida V3 NoHigh — Range Only | 2 | €10.296,85 | €313,60 | €940,79 | €102,49 | €0,00 |
| TEST | MAIN — Dynamic Asset Selector | 1 | €10.283,98 | €142,87 | €428,60 | €51,43 | €-2,24 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 5 | €10.283,80 | €1.776,35 | €5.329,06 | €104,48 | €92,85 |
| TEST | Rapida V1 — senza PEPE | 4 | €10.282,54 | €2.522,44 | €7.567,32 | €103,38 | €32,45 |
| TEST | Combo Adaptive — Side × Regime Guard | 5 | €10.260,29 | €2.379,24 | €4.758,48 | €103,40 | €80,28 |
| TEST | Rapida V3 senza ESPORTS — Long Only | 2 | €10.236,02 | €386,33 | €1.159,00 | €49,93 | €31,66 |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 2 | €10.235,71 | €336,78 | €1.010,33 | €50,80 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 1 | €10.226,57 | €142,59 | €427,78 | €51,33 | €13,41 |
| TEST | Bilanciata 1H V2 | 4 | €10.211,16 | €1.500,45 | €4.501,34 | €152,14 | €11,00 |
| TEST | Rapida 1H V3 Filtered — madre | 4 | €10.206,56 | €2.532,51 | €7.597,52 | €154,31 | €11,75 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 1 | €10.204,64 | €141,91 | €425,73 | €51,09 | €-5,06 |
| TEST | Combo Adaptive — madre | 4 | €10.203,22 | €2.162,62 | €4.325,23 | €204,07 | €0,00 |
| TEST | MAIN — Side × Regime Guard | 4 | €10.181,39 | €1.079,92 | €3.239,75 | €152,51 | €6,48 |
| TEST | FAST NoHigh <7,5 · SHORT only | 3 | €10.178,54 | €1.176,48 | €3.529,44 | €149,64 | €-5,05 |
| TEST | Btc Bollinger 1H | 0 | €10.168,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — 75% a 2R + runner 25% a 3R | 6 | €10.165,60 | €2.311,67 | €4.623,34 | €150,91 | €34,65 |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 5 | €10.151,34 | €2.583,06 | €7.749,18 | €152,32 | €101,16 |
| TEST | Combo Adaptive — Quality7 | 4 | €10.105,22 | €2.197,33 | €4.394,65 | €200,20 | €-2,20 |
| TEST | Combo Trend — Side × Regime Guard | 5 | €10.098,17 | €2.231,14 | €4.462,28 | €200,18 | €-18,91 |
| TEST | Sol Donchian 1H | 0 | €10.092,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Ema 1H | 0 | €10.091,86 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Top 5 + BTC — target pieno 3R | 5 | €10.089,23 | €1.382,11 | €2.764,22 | €154,26 | €-5,39 |
| TEST | Sol Bollinger 4H | 0 | €10.086,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 4H | 0 | €10.084,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Forza relativa 1H V2 | 3 | €10.083,35 | €1.704,09 | €3.408,19 | €54,70 | €32,26 |
| TEST | Top 5 + BTC — 75% a 2,2R + runner 3R | 5 | €10.083,31 | €1.367,97 | €2.735,93 | €153,72 | €-5,40 |
| TEST | Rapida V3 — qualità completa + profit lock | 2 | €10.076,71 | €385,11 | €1.155,33 | €99,59 | €-4,99 |
| TEST | Rapida V3 senza ESPORTS — Stress Guard | 0 | €10.071,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V1 — Long + BTC 1–3 + score <7,5 | 0 | €10.064,94 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V1 — target pieno 2R | 6 | €10.053,87 | €3.082,04 | €9.246,12 | €151,20 | €106,86 |
| TEST | Rapida 1H V1 — madre | 1 | €10.048,63 | €1.486,90 | €4.460,70 | €49,96 | €0,00 |
| TEST | Ampia 4H | 5 | €10.048,62 | €1.759,28 | €3.518,56 | €200,08 | €20,99 |
| TEST | Combo Adaptive — Long Only | 5 | €10.039,55 | €2.704,77 | €5.409,53 | €150,03 | €31,19 |
| TEST | Donchian 1H Gb20 120R V1 | 4 | €10.034,80 | €5.366,04 | €10.732,08 | €150,19 | €41,24 |
| TEST | Top 5 + BTC — BTC 2–3 | 3 | €10.020,88 | €1.301,34 | €2.602,67 | €150,18 | €-2,18 |
| TEST | Btc Adaptive 1H | 0 | €10.013,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €10.010,36 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Top 5 + BTC — BTC≤3 | 4 | €10.008,70 | €1.339,17 | €2.678,35 | €151,61 | €-2,19 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 4 | €10.007,29 | €3.765,99 | €11.297,96 | €149,76 | €70,57 |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 1 | €10.003,88 | €141,08 | €423,23 | €50,79 | €0,00 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 0 | €10.002,07 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €50 · 15x | 0 | €10.000,61 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €10 · 15x | 0 | €10.000,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Continuation V1 | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €10 · 15x | 0 | €9.999,70 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €10 · 15x | 0 | €9.998,96 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 — senza ESPORTS | 4 | €9.998,74 | €2.480,36 | €7.441,09 | €151,14 | €11,51 |
| TEST | Scalp RSI Short 85 · prudente · 5x | 0 | €9.998,64 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €50 · 15x | 0 | €9.998,52 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €10 · 15x | 0 | €9.998,50 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Mean Reversion | 1 | €9.996,35 | €1.998,97 | €3.997,94 | €47,98 | €3,90 |
| TEST | Bilanciata 1H — SHORT Trend Down stretto | 0 | €9.995,87 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | 5 | €9.995,82 | €2.797,31 | €5.594,62 | €150,05 | €73,99 |
| TEST | Scalp RSI Long 20 · €50 · 15x | 0 | €9.994,81 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €50 · 15x | 0 | €9.992,50 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €10 · 15x | 0 | €9.991,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 0 | €9.990,65 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · prudente · 5x | 0 | €9.990,24 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Benchmark Bollinger mean reversion 1H | 1 | €9.988,64 | €208,14 | €416,27 | €49,95 | €-13,22 |
| TEST | Scalp RSI Long 15 · prudente · 5x | 0 | €9.988,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Top 5 + BTC — Guard + BTC≤3 | 3 | €9.984,80 | €1.284,96 | €2.569,92 | €148,75 | €-2,18 |
| TEST | Scalp RSI Long 20 · prudente · 5x | 0 | €9.983,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 1H | 0 | €9.980,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V2 | 1 | €9.979,60 | €1.494,54 | €4.483,63 | €50,22 | €0,00 |
| TEST | Bilanciata V3 · LONG only | 5 | €9.978,09 | €1.826,05 | €5.478,14 | €149,15 | €-19,34 |
| TEST | Sol Ema 1H | 0 | €9.977,09 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Donchian 1H | 1 | €9.976,20 | €1.286,97 | €3.860,92 | €49,99 | €-20,24 |
| TEST | Rapida V3 — Long + no HIGH + score <7,5 | 2 | €9.974,60 | €385,32 | €1.155,95 | €99,43 | €-4,94 |
| TEST | Combo Adaptive — Trend/Transition | 4 | €9.959,98 | €1.857,37 | €3.714,73 | €98,93 | €86,33 |
| TEST | Eth Bollinger 1H | 0 | €9.959,49 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Donchian 4H | 1 | €9.957,03 | €830,21 | €1.660,43 | €49,74 | €9,44 |
| TEST | Sol Adaptive 4H | 1 | €9.956,45 | €761,04 | €1.522,08 | €49,74 | €8,65 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 0 | €9.955,61 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €50 · 15x | 0 | €9.955,59 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.951,70 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 4H | 0 | €9.950,68 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 4H | 0 | €9.950,68 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 4H | 0 | €9.949,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Profit Lock V1 | 5 | €9.949,10 | €2.778,15 | €5.556,30 | €100,28 | €73,06 |
| TEST | Combo Adaptive — Quality7 + Regime + parziale 1R | 2 | €9.935,47 | €1.071,47 | €2.142,94 | €49,61 | €31,79 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 1 | €9.935,16 | €138,53 | €415,58 | €49,87 | €13,02 |
| TEST | Eth Ema 4H | 1 | €9.930,30 | €1.036,30 | €2.072,59 | €49,74 | €-15,33 |
| TEST | Combo Adaptive — target pieno 3R | 4 | €9.929,58 | €2.226,41 | €4.452,81 | €198,61 | €0,00 |
| TEST | Master Adaptive GB20 — Breakeven 0,5R | 3 | €9.927,52 | €1.902,43 | €3.804,85 | €100,69 | €31,81 |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 4 | €9.921,84 | €3.734,68 | €11.204,03 | €99,16 | €106,56 |
| TEST | Combo Scanner | 6 | €9.915,28 | €2.945,47 | €5.890,93 | €198,49 | €-22,43 |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 5 | €9.911,95 | €1.704,75 | €5.114,24 | €100,77 | €106,06 |
| TEST | Btc Ema 1H | 0 | €9.911,86 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 — no volatilità HIGH | 3 | €9.904,03 | €2.446,43 | €7.339,28 | €149,26 | €11,73 |
| TEST | Bilanciata 1H — LONG senza Range High Vol | 3 | €9.901,50 | €1.245,83 | €3.737,50 | €100,06 | €31,50 |
| TEST | Sol Bollinger 1H | 0 | €9.901,25 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 4H | 0 | €9.896,31 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive GB20 — 50% a 0,75R | 3 | €9.895,08 | €1.770,78 | €3.541,56 | €100,28 | €15,84 |
| TEST | Doge Bollinger 1H | 0 | €9.888,87 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Donchian 1H | 0 | €9.871,99 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive GB20 — Loss Cap 0,75R | 3 | €9.869,09 | €2.431,87 | €4.863,75 | €150,19 | €31,87 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 2 | €9.843,92 | €330,74 | €992,21 | €98,29 | €12,81 |
| TEST | Combo Adaptive — Quality7 + Regime | 2 | €9.842,45 | €1.069,53 | €2.139,06 | €49,61 | €31,49 |
| TEST | Sol Adaptive 1H | 0 | €9.835,19 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom10 Short | 5 | €9.821,21 | €3.533,53 | €7.067,05 | €99,49 | €71,38 |
| TEST | Scanner Bottom15 Short | 5 | €9.821,21 | €3.533,53 | €7.067,05 | €99,49 | €71,38 |
| TEST | Scanner Bottom20 Short | 5 | €9.821,21 | €3.533,53 | €7.067,05 | €99,49 | €71,38 |
| TEST | Scanner Top10 Long | 4 | €9.803,32 | €2.434,72 | €4.869,44 | €147,74 | €-26,02 |
| TEST | Scanner Top15 Long | 4 | €9.803,32 | €2.434,72 | €4.869,44 | €147,74 | €-26,02 |
| TEST | Scanner Top20 Long | 4 | €9.803,32 | €2.434,72 | €4.869,44 | €147,74 | €-26,02 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 1 | €9.799,79 | €137,23 | €411,70 | €0,00 | €31,58 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 1 | €9.799,79 | €137,23 | €411,70 | €0,00 | €31,58 |
| TEST | Eth Adaptive 1H | 0 | €9.799,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Top 5 + BTC — Guard | 2 | €9.792,34 | €406,73 | €813,45 | €48,59 | €31,34 |
| TEST | Top 5 + BTC — solo MFE | 3 | €9.787,75 | €2.402,85 | €4.805,70 | €148,00 | €11,64 |
| TEST | Benchmark trend following EMA 1H | 5 | €9.776,32 | €2.076,29 | €4.152,58 | €195,47 | €14,24 |
| TEST | Scanner Bottom 5 Short 1H | 5 | €9.775,60 | €3.171,58 | €6.343,15 | €49,48 | €71,96 |
| TEST | Global Confluence puro 1H | 1 | €9.772,99 | €1.512,23 | €3.024,45 | €48,95 | €-15,85 |
| TEST | Top 5 + BTC — Guard + BTC≤3 + MFE | 2 | €9.753,67 | €1.074,59 | €2.149,17 | €98,26 | €-2,13 |
| TEST | Rapida V3 — Long Only | 2 | €9.752,65 | €379,78 | €1.139,33 | €97,86 | €12,77 |
| TEST | Master Adaptive Expanded V1 | 4 | €9.735,78 | €1.273,31 | €2.546,62 | €148,04 | €31,14 |
| TEST | Eth Ema 1H | 0 | €9.727,87 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Runner25 V1 | 4 | €9.723,50 | €1.260,39 | €2.520,78 | €147,51 | €31,10 |
| TEST | Combo Adaptive — parziale 1R | 6 | €9.714,68 | €2.194,00 | €4.388,01 | €171,15 | €14,78 |
| TEST | Master Adaptive No Alt V1 | 4 | €9.695,84 | €1.260,48 | €2.520,96 | €147,40 | €31,01 |
| TEST | Master Adaptive V1 | 4 | €9.691,84 | €1.260,39 | €2.520,79 | €147,38 | €31,00 |
| TEST | Master Adaptive Gb20 V1 | 4 | €9.617,73 | €2.591,96 | €5.183,92 | €192,45 | €-4,60 |
| TEST | Top 5 + BTC — Guard + MFE | 1 | €9.600,06 | €200,07 | €400,14 | €48,02 | €11,43 |
| TEST | Combo Adaptive — MFE Trail esistente | 3 | €9.582,67 | €1.279,15 | €2.558,30 | €143,12 | €11,07 |
| TEST | Combo Trend | 5 | €9.582,04 | €2.728,16 | €5.456,32 | €145,65 | €-15,95 |
| TEST | Forza relativa 1H V1 | 6 | €9.515,14 | €3.250,77 | €6.501,53 | €190,06 | €14,51 |
| TEST | Master Adaptive Strict3 V1 | 4 | €9.495,37 | €3.925,82 | €7.851,64 | €188,76 | €-18,08 |

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
| TEST | Donchian 1H Gb20 120R V1 | Donchian breakout 20 barre | Portafoglio sperimentale separato. |
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
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | Momentum / breakout V3 Filtered | Portafoglio sperimentale separato. |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | Momentum / breakout V3 Filtered | Portafoglio sperimentale separato. |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | Momentum / breakout V3 Filtered | Portafoglio sperimentale separato. |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | Momentum / breakout V3 Filtered | Portafoglio sperimentale separato. |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | Momentum / breakout V3 Filtered | Portafoglio sperimentale separato. |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | Momentum / breakout V3 Filtered | Portafoglio sperimentale separato. |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | Momentum / breakout V3 Filtered | Portafoglio sperimentale separato. |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | Momentum / breakout V3 Filtered | Portafoglio sperimentale separato. |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | Momentum / breakout V3 Filtered | Portafoglio sperimentale separato. |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | Momentum / breakout V3 Filtered | Portafoglio sperimentale separato. |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | Momentum / breakout V3 Filtered | Portafoglio sperimentale separato. |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | Momentum / breakout V3 Filtered | Portafoglio sperimentale separato. |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | Momentum / breakout V3 Filtered | Portafoglio sperimentale separato. |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | Momentum / breakout V3 Filtered | Portafoglio sperimentale separato. |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | Momentum / breakout V3 Filtered | Portafoglio sperimentale separato. |

## Confronto risultati

| Tipo | Portafoglio | Strategia | Equity | P&L chiuso | Trade | Eventi indip. | Win rate | PF | Expectancy | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | Confluenza trend | €9.756,81 | €-252,20 | 24 | 24 | 29,17% | 0,71 | €-10,51 | 4,76% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €10.704,17 | €644,32 | 30 | 30 | 53,33% | 2,20 | €21,48 | 2,12% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €10.605,92 | €628,35 | 50 | 50 | 42,00% | 1,63 | €12,57 | 2,20% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.561,83 | €553,16 | 44 | 44 | 50,00% | 1,57 | €12,57 | 3,57% |
| TEST | Rapida V1 — no HIGH + score <7,5 | Momentum / breakout | €10.538,06 | €544,42 | 58 | 58 | 48,28% | 1,51 | €9,39 | 2,83% |
| TEST | Rapida V3 — score <7,5 | Momentum / breakout V3 Filtered | €10.502,99 | €509,62 | 51 | 51 | 49,02% | 1,62 | €9,99 | 2,49% |
| TEST | Rapida V1 — score 6–7,5 | Momentum / breakout | €10.477,01 | €493,35 | 57 | 57 | 45,61% | 1,49 | €8,66 | 2,49% |
| TEST | Rapida score 6–7,5 — Cost Aware | Momentum / breakout | €10.437,48 | €453,75 | 20 | 20 | 60,00% | 2,61 | €22,69 | 1,96% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €10.400,61 | €370,80 | 33 | 33 | 48,48% | 1,49 | €11,24 | 3,23% |
| TEST | Rapida V3 NoHigh — Regime Guard | Momentum / breakout V3 Filtered | €10.395,73 | €396,49 | 18 | 18 | 66,67% | 3,42 | €22,03 | 1,39% |
| TEST | Rapida score 6–7,5 — senza Trend Up | Momentum / breakout | €10.364,58 | €375,85 | 17 | 17 | 70,59% | 2,53 | €22,11 | 2,01% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €10.344,64 | €284,23 | 54 | 54 | 50,00% | 1,27 | €5,26 | 3,56% |
| TEST | Rapida V3 senza ESPORTS — MFE Lock | Momentum / breakout V3 Filtered | €10.332,06 | €273,13 | 34 | 34 | 58,82% | 1,65 | €8,03 | 2,05% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | Momentum / breakout V3 Filtered | €10.328,64 | €334,04 | 21 | 21 | 52,38% | 2,10 | €15,91 | 1,62% |
| TEST | Rapida score 6–7,5 — Range Only | Momentum / breakout | €10.320,70 | €321,53 | 11 | 11 | 63,64% | 2,70 | €29,23 | 2,28% |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | Momentum / breakout V3 Filtered | €10.314,90 | €264,48 | 30 | 30 | 56,67% | 1,65 | €8,82 | 2,51% |
| TEST | Rapida V3 NoHigh — Range Only | Momentum / breakout V3 Filtered | €10.296,85 | €297,96 | 10 | 10 | 70,00% | 2,84 | €29,80 | 1,78% |
| TEST | MAIN — Dynamic Asset Selector | Confluenza trend | €10.283,98 | €286,48 | 7 | 7 | 57,14% | 3,51 | €40,93 | 1,06% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | Momentum / breakout V3 Filtered | €10.283,80 | €194,15 | 18 | 18 | 50,00% | 2,41 | €10,79 | 2,01% |
| TEST | Rapida V1 — senza PEPE | Momentum / breakout | €10.282,54 | €254,71 | 49 | 49 | 44,90% | 1,27 | €5,20 | 2,15% |
| TEST | Combo Adaptive — Side × Regime Guard | Combo Adaptive | €10.260,29 | €183,19 | 16 | 16 | 68,75% | 1,83 | €11,45 | 1,41% |
| TEST | Rapida V3 senza ESPORTS — Long Only | Momentum / breakout V3 Filtered | €10.236,02 | €205,14 | 28 | 28 | 46,43% | 1,49 | €7,33 | 1,61% |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | Momentum / breakout V3 Filtered | €10.235,71 | €236,97 | 14 | 14 | 57,14% | 4,59 | €16,93 | 1,01% |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | Momentum / breakout V3 Filtered | €10.226,57 | €213,49 | 24 | 24 | 45,83% | 1,60 | €8,90 | 2,97% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €10.211,16 | €202,87 | 37 | 35 | 54,05% | 1,27 | €5,48 | 2,75% |
| TEST | Rapida 1H V3 Filtered — madre | Momentum / breakout V3 Filtered | €10.206,56 | €199,36 | 84 | 84 | 39,29% | 1,12 | €2,37 | 2,89% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | Momentum / breakout V3 Filtered | €10.204,64 | €209,95 | 21 | 21 | 42,86% | 1,70 | €10,00 | 2,27% |
| TEST | Combo Adaptive — madre | Combo Adaptive | €10.203,22 | €206,62 | 25 | 25 | 48,00% | 1,52 | €8,26 | 1,49% |
| TEST | MAIN — Side × Regime Guard | Confluenza trend | €10.181,39 | €177,32 | 9 | 9 | 44,44% | 1,80 | €19,70 | 1,77% |
| TEST | FAST NoHigh <7,5 · SHORT only | Momentum / breakout | €10.178,54 | €185,70 | 22 | 22 | 50,00% | 1,62 | €8,44 | 1,76% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.168,12 | €168,12 | 3 | 3 | 100,00% | ∞ | €56,04 | 0,54% |
| TEST | Combo Adaptive — 75% a 2R + runner 25% a 3R | Combo Adaptive | €10.165,60 | €134,68 | 25 | 25 | 44,00% | 1,27 | €5,39 | 2,12% |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | Momentum / breakout V3 Filtered | €10.151,34 | €54,91 | 25 | 25 | 40,00% | 1,12 | €2,20 | 2,70% |
| TEST | Combo Adaptive — Quality7 | Combo Adaptive | €10.105,22 | €110,93 | 19 | 19 | 42,11% | 1,47 | €5,84 | 1,51% |
| TEST | Combo Trend — Side × Regime Guard | Combo Trend | €10.098,17 | €119,75 | 18 | 18 | 50,00% | 1,43 | €6,65 | 1,71% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €10.092,12 | €92,12 | 3 | 3 | 66,67% | 21,53 | €30,71 | 0,79% |
| TEST | Doge Ema 1H | Trend following EMA | €10.091,86 | €91,86 | 8 | 8 | 62,50% | 1,55 | €11,48 | 1,36% |
| TEST | Top 5 + BTC — target pieno 3R | Scanner Top 5 + forza BTC | €10.089,23 | €96,58 | 17 | 17 | 47,06% | 1,19 | €5,68 | 3,22% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €10.086,98 | €86,98 | 1 | 1 | 100,00% | ∞ | €86,98 | 0,40% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.084,12 | €84,12 | 1 | 1 | 100,00% | ∞ | €84,12 | 0,30% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €10.083,35 | €53,21 | 44 | 43 | 40,91% | 1,04 | €1,21 | 5,10% |
| TEST | Top 5 + BTC — 75% a 2,2R + runner 3R | Scanner Top 5 + forza BTC | €10.083,31 | €90,64 | 21 | 21 | 47,62% | 1,17 | €4,32 | 3,25% |
| TEST | Rapida V3 — qualità completa + profit lock | Momentum / breakout V3 Filtered | €10.076,71 | €82,40 | 47 | 47 | 48,94% | 1,08 | €1,75 | 3,21% |
| TEST | Rapida V3 senza ESPORTS — Stress Guard | Momentum / breakout V3 Filtered | €10.071,28 | €71,28 | 19 | 19 | 42,11% | 1,16 | €3,75 | 2,17% |
| TEST | Rapida V1 — Long + BTC 1–3 + score <7,5 | Momentum / breakout | €10.064,94 | €64,94 | 23 | 23 | 39,13% | 1,14 | €2,82 | 2,07% |
| TEST | Rapida V1 — target pieno 2R | Momentum / breakout | €10.053,87 | €-47,44 | 55 | 55 | 34,55% | 0,96 | €-0,86 | 2,58% |
| TEST | Rapida 1H V1 — madre | Momentum / breakout | €10.048,63 | €51,31 | 77 | 77 | 35,06% | 1,03 | €0,67 | 6,76% |
| TEST | Ampia 4H | Confluenza trend | €10.048,62 | €29,34 | 19 | 19 | 26,32% | 1,05 | €1,54 | 3,68% |
| TEST | Combo Adaptive — Long Only | Combo Adaptive | €10.039,55 | €12,07 | 13 | 13 | 38,46% | 1,04 | €0,93 | 2,34% |
| TEST | Donchian 1H Gb20 120R V1 | Donchian breakout 20 barre | €10.034,80 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 1,09% |
| TEST | Top 5 + BTC — BTC 2–3 | Scanner Top 5 + forza BTC | €10.020,88 | €25,00 | 7 | 7 | 42,86% | 1,14 | €3,57 | 2,84% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €10.013,28 | €13,28 | 3 | 3 | 66,67% | 1,24 | €4,43 | 0,89% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €10.010,36 | €10,36 | 10 | 10 | 30,00% | 1,22 | €1,04 | 0,25% |
| TEST | Top 5 + BTC — BTC≤3 | Scanner Top 5 + forza BTC | €10.008,70 | €12,87 | 14 | 14 | 50,00% | 1,03 | €0,92 | 3,23% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | Momentum / breakout V3 Filtered | €10.007,29 | €-56,50 | 2 | 2 | 0,00% | 0,00 | €-28,25 | 1,14% |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | Momentum / breakout V3 Filtered | €10.003,88 | €4,24 | 7 | 7 | 42,86% | 1,03 | €0,61 | 2,15% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €10.002,07 | €2,07 | 10 | 10 | 30,00% | 1,22 | €0,21 | 0,05% |
| TEST | Scalp RSI Short 85 · €50 · 15x | Inversione RSI estrema 15m | €10.000,61 | €0,61 | 2 | 2 | 50,00% | 1,74 | €0,30 | 0,07% |
| TEST | Scalp RSI Short 85 · €10 · 15x | Inversione RSI estrema 15m | €10.000,12 | €0,12 | 2 | 2 | 50,00% | 1,74 | €0,06 | 0,01% |
| TEST | Scanner Bottom5 Short Continuation V1 | Scanner Bottom5 Short Continuation | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 80 · €10 · 15x | Inversione RSI estrema 15m | €9.999,70 | €-0,30 | 3 | 3 | 66,67% | 0,63 | €-0,10 | 0,02% |
| TEST | Scalp RSI Long 20 · €10 · 15x | Inversione RSI estrema 15m | €9.998,96 | €-1,04 | 2 | 2 | 0,00% | 0,00 | €-0,52 | 0,02% |
| TEST | Rapida V3 — senza ESPORTS | Momentum / breakout V3 Filtered | €9.998,74 | €-8,31 | 58 | 58 | 39,66% | 0,99 | €-0,14 | 2,49% |
| TEST | Scalp RSI Short 85 · prudente · 5x | Inversione RSI estrema 15m | €9.998,64 | €-1,36 | 2 | 2 | 50,00% | 0,42 | €-0,68 | 0,11% |
| TEST | Scalp RSI Short 80 · €50 · 15x | Inversione RSI estrema 15m | €9.998,52 | €-1,48 | 3 | 3 | 66,67% | 0,63 | €-0,49 | 0,09% |
| TEST | Scalp RSI Long 15 · €10 · 15x | Inversione RSI estrema 15m | €9.998,50 | €-1,50 | 1 | 1 | 0,00% | 0,00 | €-1,50 | 0,02% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €9.996,35 | €-5,15 | 17 | 17 | 41,18% | 0,99 | €-0,30 | 2,31% |
| TEST | Bilanciata 1H — SHORT Trend Down stretto | Confluenza trend | €9.995,87 | €-4,13 | 1 | 1 | 0,00% | 0,00 | €-4,13 | 0,59% |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | Scanner Bottom 5 Short | €9.995,82 | €-74,71 | 6 | 6 | 50,00% | 0,54 | €-12,45 | 1,38% |
| TEST | Scalp RSI Long 20 · €50 · 15x | Inversione RSI estrema 15m | €9.994,81 | €-5,19 | 2 | 2 | 0,00% | 0,00 | €-2,59 | 0,08% |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | €9.992,50 | €-7,50 | 1 | 1 | 0,00% | 0,00 | €-7,50 | 0,11% |
| TEST | Scalp RSI Long 25 · €10 · 15x | Inversione RSI estrema 15m | €9.991,12 | €-8,88 | 7 | 7 | 28,57% | 0,24 | €-1,27 | 0,12% |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | Momentum / breakout V3 Filtered | €9.990,65 | €-9,35 | 14 | 14 | 42,86% | 0,97 | €-0,67 | 2,46% |
| TEST | Scalp RSI Short 80 · prudente · 5x | Inversione RSI estrema 15m | €9.990,24 | €-9,76 | 3 | 3 | 66,67% | 0,28 | €-3,25 | 0,21% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €9.988,64 | €2,04 | 42 | 42 | 42,86% | 1,00 | €0,05 | 4,19% |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | €9.988,38 | €-11,62 | 1 | 1 | 0,00% | 0,00 | €-11,62 | 0,17% |
| TEST | Top 5 + BTC — Guard + BTC≤3 | Scanner Top 5 + forza BTC | €9.984,80 | €-11,10 | 13 | 13 | 46,15% | 0,98 | €-0,85 | 3,23% |
| TEST | Scalp RSI Long 20 · prudente · 5x | Inversione RSI estrema 15m | €9.983,60 | €-16,40 | 2 | 2 | 0,00% | 0,00 | €-8,20 | 0,24% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €9.980,62 | €-19,38 | 4 | 4 | 50,00% | 0,82 | €-4,84 | 1,49% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €9.979,60 | €-17,71 | 16 | 14 | 43,75% | 0,95 | €-1,11 | 1,69% |
| TEST | Bilanciata V3 · LONG only | Confluenza trend V3 Filtered | €9.978,09 | €1,55 | 10 | 10 | 30,00% | 1,01 | €0,15 | 1,46% |
| TEST | Sol Ema 1H | Trend following EMA | €9.977,09 | €-22,91 | 5 | 5 | 40,00% | 0,86 | €-4,58 | 1,67% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €9.976,20 | €-1,25 | 4 | 4 | 75,00% | 0,98 | €-0,31 | 1,08% |
| TEST | Rapida V3 — Long + no HIGH + score <7,5 | Momentum / breakout V3 Filtered | €9.974,60 | €-19,76 | 42 | 42 | 42,86% | 0,98 | €-0,47 | 2,86% |
| TEST | Combo Adaptive — Trend/Transition | Combo Adaptive | €9.959,98 | €-123,83 | 18 | 18 | 44,44% | 0,72 | €-6,88 | 2,18% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €9.959,49 | €-40,51 | 2 | 2 | 50,00% | 0,28 | €-20,26 | 0,91% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €9.957,03 | €-52,00 | 1 | 1 | 0,00% | 0,00 | €-52,00 | 0,79% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €9.956,45 | €-51,83 | 1 | 1 | 0,00% | 0,00 | €-51,83 | 0,77% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €9.955,61 | €-44,39 | 7 | 7 | 14,29% | 0,12 | €-6,34 | 0,58% |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | €9.955,59 | €-44,41 | 7 | 7 | 28,57% | 0,24 | €-6,34 | 0,58% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.951,70 | €-48,30 | 10 | 10 | 30,00% | 0,27 | €-4,83 | 0,58% |
| TEST | Btc Ema 4H | Trend following EMA | €9.950,68 | €-49,32 | 1 | 1 | 0,00% | 0,00 | €-49,32 | 0,96% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €9.950,68 | €-49,32 | 1 | 1 | 0,00% | 0,00 | €-49,32 | 0,96% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €9.949,62 | €-50,38 | 1 | 1 | 0,00% | 0,00 | €-50,38 | 0,74% |
| TEST | Scanner Bottom5 Short Profit Lock V1 | Scanner Bottom 5 Short | €9.949,10 | €-119,98 | 5 | 5 | 40,00% | 0,25 | €-24,00 | 1,53% |
| TEST | Combo Adaptive — Quality7 + Regime + parziale 1R | Combo Adaptive | €9.935,47 | €-94,95 | 9 | 9 | 44,44% | 0,64 | €-10,55 | 1,95% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | Momentum / breakout V3 Filtered | €9.935,16 | €-77,54 | 25 | 25 | 40,00% | 0,85 | €-3,10 | 2,95% |
| TEST | Eth Ema 4H | Trend following EMA | €9.930,30 | €-52,88 | 1 | 1 | 0,00% | 0,00 | €-52,88 | 0,96% |
| TEST | Combo Adaptive — target pieno 3R | Combo Adaptive | €9.929,58 | €-66,67 | 13 | 13 | 46,15% | 0,76 | €-5,13 | 1,41% |
| TEST | Master Adaptive GB20 — Breakeven 0,5R | Master Adaptive Consensus | €9.927,52 | €-101,92 | 19 | 19 | 21,05% | 0,79 | €-5,36 | 3,15% |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | Momentum / breakout V3 Filtered | €9.921,84 | €-177,92 | 5 | 5 | 0,00% | 0,00 | €-35,58 | 1,99% |
| TEST | Combo Scanner | Combo Scanner | €9.915,28 | €-58,46 | 39 | 39 | 43,59% | 0,94 | €-1,50 | 3,25% |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | Momentum / breakout V3 Filtered | €9.911,95 | €-191,04 | 20 | 20 | 45,00% | 0,60 | €-9,55 | 3,08% |
| TEST | Btc Ema 1H | Trend following EMA | €9.911,86 | €-88,14 | 6 | 6 | 33,33% | 0,59 | €-14,69 | 1,56% |
| TEST | Rapida V3 — no volatilità HIGH | Momentum / breakout V3 Filtered | €9.904,03 | €-103,29 | 58 | 58 | 39,66% | 0,92 | €-1,78 | 2,96% |
| TEST | Bilanciata 1H — LONG senza Range High Vol | Confluenza trend | €9.901,50 | €-127,67 | 13 | 13 | 38,46% | 0,71 | €-9,82 | 2,47% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.901,25 | €-98,75 | 4 | 4 | 25,00% | 0,41 | €-24,69 | 1,89% |
| TEST | Sol Ema 4H | Trend following EMA | €9.896,31 | €-103,69 | 2 | 2 | 0,00% | 0,00 | €-51,84 | 1,06% |
| TEST | Master Adaptive GB20 — 50% a 0,75R | Master Adaptive Consensus | €9.895,08 | €-137,13 | 14 | 14 | 28,57% | 0,70 | €-9,79 | 2,50% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €9.888,87 | €-111,13 | 2 | 2 | 0,00% | 0,00 | €-55,56 | 1,26% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.871,99 | €-128,01 | 5 | 5 | 20,00% | 0,42 | €-25,60 | 1,62% |
| TEST | Master Adaptive GB20 — Loss Cap 0,75R | Master Adaptive Consensus | €9.869,09 | €-159,79 | 16 | 16 | 25,00% | 0,71 | €-9,99 | 3,63% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | Momentum / breakout V3 Filtered | €9.843,92 | €-168,22 | 21 | 21 | 42,86% | 0,65 | €-8,01 | 2,93% |
| TEST | Combo Adaptive — Quality7 + Regime | Combo Adaptive | €9.842,45 | €-187,67 | 9 | 9 | 33,33% | 0,32 | €-20,85 | 2,32% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €9.835,19 | €-164,81 | 6 | 6 | 33,33% | 0,29 | €-27,47 | 2,34% |
| TEST | Scanner Bottom10 Short | Scanner Bottom10 Short | €9.821,21 | €-245,28 | 6 | 6 | 16,67% | 0,11 | €-40,88 | 2,72% |
| TEST | Scanner Bottom15 Short | Scanner Bottom15 Short | €9.821,21 | €-245,28 | 6 | 6 | 16,67% | 0,11 | €-40,88 | 2,72% |
| TEST | Scanner Bottom20 Short | Scanner Bottom20 Short | €9.821,21 | €-245,28 | 6 | 6 | 16,67% | 0,11 | €-40,88 | 2,72% |
| TEST | Scanner Top10 Long | Scanner Top10 Long | €9.803,32 | €-167,56 | 14 | 14 | 42,86% | 0,59 | €-11,97 | 3,78% |
| TEST | Scanner Top15 Long | Scanner Top15 Long | €9.803,32 | €-167,56 | 14 | 14 | 42,86% | 0,59 | €-11,97 | 3,78% |
| TEST | Scanner Top20 Long | Scanner Top20 Long | €9.803,32 | €-167,56 | 14 | 14 | 42,86% | 0,59 | €-11,97 | 3,78% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | Momentum / breakout V3 Filtered | €9.799,79 | €-231,46 | 5 | 5 | 0,00% | 0,00 | €-46,29 | 2,20% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | Momentum / breakout V3 Filtered | €9.799,79 | €-231,46 | 5 | 5 | 0,00% | 0,00 | €-46,29 | 2,20% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.799,60 | €-200,40 | 6 | 6 | 33,33% | 0,08 | €-33,40 | 2,09% |
| TEST | Top 5 + BTC — Guard | Scanner Top 5 + forza BTC | €9.792,34 | €-238,06 | 20 | 20 | 30,00% | 0,65 | €-11,90 | 3,36% |
| TEST | Top 5 + BTC — solo MFE | Scanner Top 5 + forza BTC | €9.787,75 | €-221,32 | 25 | 25 | 40,00% | 0,59 | €-8,85 | 3,95% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.776,32 | €-234,50 | 31 | 31 | 35,48% | 0,71 | €-7,56 | 3,29% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.775,60 | €-288,92 | 29 | 29 | 31,03% | 0,61 | €-9,96 | 5,48% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.772,99 | €-209,34 | 10 | 10 | 30,00% | 0,37 | €-20,93 | 2,92% |
| TEST | Top 5 + BTC — Guard + BTC≤3 + MFE | Scanner Top 5 + forza BTC | €9.753,67 | €-242,91 | 28 | 28 | 42,86% | 0,70 | €-8,68 | 3,93% |
| TEST | Rapida V3 — Long Only | Momentum / breakout V3 Filtered | €9.752,65 | €-259,37 | 49 | 49 | 32,65% | 0,78 | €-5,29 | 3,67% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €9.735,78 | €-293,29 | 18 | 18 | 33,33% | 0,62 | €-16,29 | 3,64% |
| TEST | Eth Ema 1H | Trend following EMA | €9.727,87 | €-272,13 | 8 | 8 | 25,00% | 0,16 | €-34,02 | 2,76% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €9.723,50 | €-305,55 | 17 | 17 | 29,41% | 0,58 | €-17,97 | 3,98% |
| TEST | Combo Adaptive — parziale 1R | Combo Adaptive | €9.714,68 | €-296,93 | 22 | 22 | 36,36% | 0,51 | €-13,50 | 3,32% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €9.695,84 | €-333,13 | 15 | 15 | 26,67% | 0,53 | €-22,21 | 4,03% |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | €9.691,84 | €-337,11 | 15 | 15 | 26,67% | 0,53 | €-22,47 | 4,07% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €9.617,73 | €-374,57 | 50 | 50 | 58,00% | 0,59 | €-7,49 | 4,27% |
| TEST | Top 5 + BTC — Guard + MFE | Scanner Top 5 + forza BTC | €9.600,06 | €-411,13 | 35 | 35 | 37,14% | 0,58 | €-11,75 | 5,08% |
| TEST | Combo Adaptive — MFE Trail esistente | Combo Adaptive | €9.582,67 | €-426,65 | 33 | 33 | 30,30% | 0,49 | €-12,93 | 5,33% |
| TEST | Combo Trend | Combo Trend | €9.582,04 | €-397,95 | 43 | 43 | 32,56% | 0,74 | €-9,25 | 7,02% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €9.515,14 | €-495,46 | 35 | 35 | 25,71% | 0,54 | €-14,16 | 7,55% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €9.495,37 | €-481,54 | 23 | 23 | 26,09% | 0,54 | €-20,94 | 5,58% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | LAB | SHORT | Confluenza trend | 240m | 3,0x | 0,17841 | 0,17841 | 0,17841 | 0,23699 | 0,13559 | €136,26 | €408,77 | €0,00 | €-0,00 |
| Principale 4H | SUI | LONG | Confluenza trend | 240m | 3,0x | 0,76296 | 0,76296 | 0,73998 | 0,51245 | 0,80891 | €547,52 | €1.642,56 | €49,46 | €0,00 |
| Principale 4H | ONDO | LONG | Confluenza trend | 240m | 3,0x | 0,40344 | 0,40344 | 0,37762 | 0,27098 | 0,45509 | €254,70 | €764,09 | €48,91 | €0,00 |
| Principale 4H | SHIB | LONG | Confluenza trend | 240m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €8,88 | €26,63 | €2,22 | €-1,49 |
| Principale 4H | HYPE | SHORT | Confluenza trend | 240m | 3,0x | 57,27654 | 56,71900 | 59,33830 | 76,08234 | 53,15302 | €419,05 | €1.257,15 | €45,25 | €12,24 |
| Bilanciata 1H V1 | ADA | SHORT | Confluenza trend | 60m | 3,0x | 0,16703 | 0,16703 | 0,16365 | 0,22187 | 0,16112 | €978,72 | €2.936,17 | €0,00 | €-0,00 |
| Bilanciata 1H V1 | ALLO | SHORT | Confluenza trend | 60m | 3,0x | 0,36179 | 0,36179 | 0,40521 | 0,48058 | 0,27496 | €141,53 | €424,59 | €50,95 | €-0,00 |
| Bilanciata 1H V1 | PEPE | LONG | Confluenza trend | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €27,46 | €82,37 | €2,26 | €-0,97 |
| Bilanciata 1H V1 | AKE | LONG | Confluenza trend | 60m | 3,0x | 0,00443 | 0,00437 | 0,00389 | 0,00297 | 0,00549 | €141,56 | €424,68 | €50,96 | €-5,05 |
| Bilanciata 1H V1 | HYPE | SHORT | Confluenza trend | 60m | 3,0x | 58,25535 | 56,71900 | 57,49335 | 77,38252 | 56,21023 | €932,54 | €2.797,62 | €0,00 | €73,78 |
| Bilanciata 1H V1 | ZEC | SHORT | Confluenza trend | 60m | 3,0x | 483,74323 | 485,20000 | 494,91887 | 642,57226 | 461,39195 | €17,56 | €52,68 | €1,22 | €-0,16 |
| Bilanciata 1H — LONG senza Range High Vol | BEAT | LONG | Confluenza trend | 60m | 3,0x | 3,29017 | 3,29017 | 3,00714 | 2,20990 | 3,85623 | €193,69 | €581,07 | €49,98 | €0,00 |
| Bilanciata 1H — LONG senza Range High Vol | XMR | LONG | Confluenza trend | 60m | 3,0x | 366,72991 | 366,72991 | 360,04130 | 246,32025 | 380,10712 | €915,26 | €2.745,79 | €50,08 | €0,00 |
| Bilanciata 1H — LONG senza Range High Vol | AKE | LONG | Confluenza trend | 60m | 3,0x | 0,00406 | 0,00437 | 0,00406 | 0,00273 | 0,00504 | €136,88 | €410,64 | €0,00 | €31,50 |
| Bilanciata 1H V2 | ADA | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,16276 | 0,16276 | 0,16511 | 0,21620 | 0,15807 | €1.185,56 | €3.556,68 | €51,22 | €-0,00 |
| Bilanciata 1H V2 | WLD | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,34349 | 0,34349 | 0,35287 | 0,45627 | 0,32475 | €26,53 | €79,60 | €2,17 | €-0,00 |
| Bilanciata 1H V2 | ALLO | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,35543 | 0,35543 | 0,39400 | 0,47213 | 0,27829 | €146,68 | €440,04 | €47,75 | €-0,00 |
| Bilanciata 1H V2 | AKE | LONG | Confluenza trend V2 | 60m | 3,0x | 0,00426 | 0,00437 | 0,00375 | 0,00286 | 0,00529 | €141,67 | €425,02 | €51,00 | €11,00 |
| Bilanciata 1H V3 Filtered | BEAT | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 3,31215 | 3,31215 | 3,02723 | 2,22466 | 3,88198 | €203,36 | €610,09 | €52,48 | €0,00 |
| Bilanciata 1H V3 Filtered | WLD | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,34349 | 0,34349 | 0,35287 | 0,45627 | 0,32475 | €23,43 | €70,29 | €1,92 | €-0,00 |
| Bilanciata 1H V3 Filtered | ALLO | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,34255 | 0,34255 | 0,37914 | 0,45502 | 0,26938 | €160,61 | €481,84 | €51,46 | €-0,00 |
| Bilanciata 1H V3 Filtered | ESPORTS | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,02905 | 0,02905 | 0,03254 | 0,03859 | 0,02208 | €142,96 | €428,87 | €51,46 | €-0,00 |
| Bilanciata 1H V3 Filtered | PEPE | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €645,00 | €1.934,99 | €53,14 | €-22,79 |
| Bilanciata 1H V3 Filtered | HYPE | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 58,25535 | 56,71900 | 57,49335 | 77,38252 | 56,21023 | €35,61 | €106,84 | €0,00 | €2,82 |
| Rapida 1H V1 — madre | ADA | SHORT | Momentum / breakout | 60m | 3,0x | 0,16185 | 0,16185 | 0,16367 | 0,21499 | 0,15913 | €1.486,90 | €4.460,70 | €49,96 | €-0,00 |
| Rapida V1 — score 6–7,5 | ALLO | SHORT | Momentum / breakout | 60m | 3,0x | 0,33713 | 0,33713 | 0,36471 | 0,44782 | 0,29576 | €212,67 | €638,01 | €52,19 | €-0,00 |
| Rapida V1 — score 6–7,5 | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00443 | 0,00437 | 0,00389 | 0,00297 | 0,00522 | €144,83 | €434,48 | €52,14 | €-5,16 |
| Rapida V1 — score 6–7,5 | ZEC | SHORT | Momentum / breakout | 60m | 3,0x | 483,74323 | 485,20000 | 492,43540 | 642,57226 | 470,70499 | €972,21 | €2.916,64 | €52,41 | €-8,78 |
| Rapida score 6–7,5 — senza Trend Up | BEAT | LONG | Momentum / breakout | 60m | 3,0x | 3,29017 | 3,29017 | 3,07004 | 2,20990 | 3,62037 | €256,24 | €768,73 | €51,43 | €0,00 |
| Rapida score 6–7,5 — senza Trend Up | ALLO | SHORT | Momentum / breakout | 60m | 3,0x | 0,33808 | 0,33808 | 0,36389 | 0,44909 | 0,29937 | €218,91 | €656,73 | €50,14 | €-0,00 |
| Rapida score 6–7,5 — senza Trend Up | ZEC | SHORT | Momentum / breakout | 60m | 3,0x | 483,74323 | 485,20000 | 492,43540 | 642,57226 | 470,70499 | €961,25 | €2.883,74 | €51,82 | €-8,68 |
| Rapida score 6–7,5 — Range Only | BEAT | LONG | Momentum / breakout | 60m | 3,0x | 3,29017 | 3,29017 | 3,07004 | 2,20990 | 3,62037 | €256,24 | €768,73 | €51,43 | €0,00 |
| Rapida score 6–7,5 — Range Only | ESPORTS | SHORT | Momentum / breakout | 60m | 3,0x | 0,02828 | 0,02828 | 0,03168 | 0,03757 | 0,02319 | €143,01 | €429,04 | €51,48 | €-0,00 |
| Rapida score 6–7,5 — Cost Aware | ALLO | SHORT | Momentum / breakout | 60m | 3,0x | 0,33713 | 0,33713 | 0,36471 | 0,44782 | 0,29576 | €211,20 | €633,59 | €51,83 | €-0,00 |
| Rapida score 6–7,5 — Cost Aware | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00443 | 0,00437 | 0,00389 | 0,00297 | 0,00522 | €144,27 | €432,82 | €51,94 | €-5,14 |
| Rapida score 6–7,5 — Cost Aware | ZEC | SHORT | Momentum / breakout | 60m | 3,0x | 483,74323 | 485,20000 | 492,43540 | 642,57226 | 470,70499 | €968,54 | €2.905,63 | €52,21 | €-8,75 |
| Rapida V1 — no HIGH + score <7,5 | BEAT | LONG | Momentum / breakout | 60m | 3,0x | 3,29017 | 3,29017 | 3,07004 | 2,20990 | 3,62037 | €257,44 | €772,31 | €51,67 | €0,00 |
| Rapida V1 — no HIGH + score <7,5 | ALLO | SHORT | Momentum / breakout | 60m | 3,0x | 0,33808 | 0,33808 | 0,36389 | 0,44909 | 0,29937 | €225,73 | €677,19 | €51,70 | €-0,00 |
| Rapida V1 — no HIGH + score <7,5 | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00443 | 0,00437 | 0,00389 | 0,00297 | 0,00522 | €146,54 | €439,61 | €52,75 | €-5,22 |
| Rapida V1 — senza PEPE | ADA | SHORT | Momentum / breakout | 60m | 3,0x | 0,16185 | 0,16185 | 0,16367 | 0,21499 | 0,15913 | €1.512,75 | €4.538,24 | €50,83 | €-0,00 |
| Rapida V1 — senza PEPE | WLD | SHORT | Momentum / breakout | 60m | 3,0x | 0,34959 | 0,34959 | 0,35668 | 0,46437 | 0,33896 | €838,72 | €2.516,16 | €51,00 | €-0,00 |
| Rapida V1 — senza PEPE | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00406 | 0,00437 | 0,00406 | 0,00273 | 0,00479 | €142,15 | €426,46 | €0,00 | €32,71 |
| Rapida V1 — senza PEPE | ZEC | SHORT | Momentum / breakout | 60m | 3,0x | 483,74323 | 485,20000 | 492,43540 | 642,57226 | 470,70499 | €28,82 | €86,46 | €1,55 | €-0,26 |
| Rapida V1 — target pieno 2R | ADA | SHORT | Momentum / breakout | 60m | 3,0x | 0,16185 | 0,16185 | 0,16367 | 0,21499 | 0,15823 | €1.482,83 | €4.448,49 | €49,82 | €-0,00 |
| Rapida V1 — target pieno 2R | WLD | SHORT | Momentum / breakout | 60m | 3,0x | 0,34959 | 0,34959 | 0,35668 | 0,46437 | 0,33542 | €42,01 | €126,02 | €2,55 | €-0,00 |
| Rapida V1 — target pieno 2R | ALLO | SHORT | Momentum / breakout | 60m | 3,0x | 0,35543 | 0,35543 | 0,38543 | 0,47213 | 0,29543 | €187,33 | €561,99 | €47,43 | €-0,00 |
| Rapida V1 — target pieno 2R | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00425 | 0,00437 | 0,00374 | 0,00286 | 0,00527 | €138,61 | €415,82 | €49,90 | €11,88 |
| Rapida V1 — target pieno 2R | HYPE | SHORT | Momentum / breakout | 60m | 3,0x | 58,25535 | 56,71900 | 57,38273 | 77,38252 | 56,66470 | €1.203,65 | €3.610,96 | €0,00 | €95,23 |
| Rapida V1 — target pieno 2R | ZEC | SHORT | Momentum / breakout | 60m | 3,0x | 483,74323 | 485,20000 | 492,43540 | 642,57226 | 466,35890 | €27,61 | €82,84 | €1,49 | €-0,25 |
| Rapida 1H V2 | ADA | SHORT | Momentum / breakout V2 | 60m | 3,0x | 0,16185 | 0,16185 | 0,16367 | 0,21499 | 0,15913 | €1.494,54 | €4.483,63 | €50,22 | €-0,00 |
| Rapida 1H V3 Filtered — madre | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16185 | 0,16185 | 0,16367 | 0,21499 | 0,15913 | €1.521,20 | €4.563,60 | €51,11 | €-0,00 |
| Rapida 1H V3 Filtered — madre | WLD | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,34959 | 0,34959 | 0,35668 | 0,46437 | 0,33896 | €843,41 | €2.530,22 | €51,28 | €-0,00 |
| Rapida 1H V3 Filtered — madre | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00425 | 0,00437 | 0,00374 | 0,00286 | 0,00502 | €140,04 | €420,12 | €50,41 | €12,00 |
| Rapida 1H V3 Filtered — madre | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 483,74323 | 485,20000 | 492,43540 | 642,57226 | 470,70499 | €27,86 | €83,58 | €1,50 | €-0,25 |
| Rapida V3 — score <7,5 | BEAT | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 3,29017 | 3,29017 | 3,07004 | 2,20990 | 3,62037 | €258,77 | €776,32 | €51,94 | €0,00 |
| Rapida V3 — score <7,5 | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,33808 | 0,33808 | 0,36389 | 0,44909 | 0,29937 | €227,32 | €681,96 | €52,06 | €-0,00 |
| Rapida V3 — score <7,5 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00443 | 0,00437 | 0,00389 | 0,00297 | 0,00522 | €145,04 | €435,12 | €52,21 | €-5,17 |
| Rapida V3 — score <7,5 | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 483,74323 | 485,20000 | 492,43540 | 642,57226 | 470,70499 | €30,24 | €90,72 | €1,63 | €-0,27 |
| Rapida V3 — no volatilità HIGH | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16185 | 0,16185 | 0,16367 | 0,21499 | 0,15913 | €1.485,86 | €4.457,58 | €49,92 | €-0,00 |
| Rapida V3 — no volatilità HIGH | WLD | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,34959 | 0,34959 | 0,35668 | 0,46437 | 0,33896 | €823,75 | €2.471,25 | €50,08 | €-0,00 |
| Rapida V3 — no volatilità HIGH | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00425 | 0,00437 | 0,00374 | 0,00286 | 0,00502 | €136,82 | €410,45 | €49,25 | €11,73 |
| Rapida V3 — Long Only | BEAT | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 3,29017 | 3,29017 | 3,07004 | 2,20990 | 3,62037 | €243,96 | €731,87 | €48,97 | €0,00 |
| Rapida V3 — Long Only | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00424 | 0,00437 | 0,00373 | 0,00285 | 0,00500 | €135,82 | €407,45 | €48,89 | €12,77 |
| Rapida V3 — Long + no HIGH + score <7,5 | BEAT | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 3,29017 | 3,29017 | 3,07004 | 2,20990 | 3,62037 | €246,62 | €739,85 | €49,50 | €0,00 |
| Rapida V3 — Long + no HIGH + score <7,5 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00443 | 0,00437 | 0,00389 | 0,00297 | 0,00522 | €138,70 | €416,10 | €49,93 | €-4,94 |
| Rapida V3 — senza ESPORTS | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16185 | 0,16185 | 0,16367 | 0,21499 | 0,15913 | €1.489,89 | €4.469,66 | €50,06 | €-0,00 |
| Rapida V3 — senza ESPORTS | WLD | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,34959 | 0,34959 | 0,35668 | 0,46437 | 0,33896 | €825,98 | €2.477,95 | €50,22 | €-0,00 |
| Rapida V3 — senza ESPORTS | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00425 | 0,00437 | 0,00374 | 0,00286 | 0,00502 | €137,19 | €411,57 | €49,39 | €11,76 |
| Rapida V3 — senza ESPORTS | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 483,74323 | 485,20000 | 492,43540 | 642,57226 | 470,70499 | €27,30 | €81,91 | €1,47 | €-0,25 |
| Rapida V3 senza ESPORTS — Long Only | BEAT | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 3,29017 | 3,29017 | 3,07004 | 2,20990 | 3,62037 | €248,78 | €746,34 | €49,93 | €0,00 |
| Rapida V3 senza ESPORTS — Long Only | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00406 | 0,00437 | 0,00406 | 0,00273 | 0,00479 | €137,56 | €412,67 | €0,00 | €31,66 |
| Rapida V3 senza ESPORTS — MFE Lock | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16185 | 0,16185 | 0,16367 | 0,21499 | 0,15913 | €1.510,84 | €4.532,53 | €50,76 | €-0,00 |
| Rapida V3 senza ESPORTS — MFE Lock | WLD | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,34959 | 0,34959 | 0,35668 | 0,46437 | 0,33896 | €11,86 | €35,57 | €0,72 | €-0,00 |
| Rapida V3 senza ESPORTS — MFE Lock | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,33165 | 0,33165 | 0,36472 | 0,44055 | 0,28205 | €170,96 | €512,89 | €51,14 | €-0,00 |
| Rapida V3 senza ESPORTS — MFE Lock | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00425 | 0,00437 | 0,00374 | 0,00286 | 0,00502 | €142,50 | €427,49 | €51,30 | €12,21 |
| Rapida V3 senza ESPORTS — MFE Lock | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 483,74323 | 485,20000 | 492,43540 | 642,57226 | 470,70499 | €28,65 | €85,95 | €1,54 | €-0,26 |
| Rapida V3 senza ESPORTS — MFE Lock | HYPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 57,61747 | 56,71900 | 57,43863 | 76,53521 | 56,33818 | €1.128,80 | €3.386,41 | €0,00 | €52,81 |
| Rapida V3 — qualità completa + profit lock | BEAT | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 3,29017 | 3,29017 | 3,07004 | 2,20990 | 3,62037 | €245,16 | €735,47 | €49,21 | €0,00 |
| Rapida V3 — qualità completa + profit lock | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00443 | 0,00437 | 0,00389 | 0,00297 | 0,00522 | €139,96 | €419,87 | €50,38 | €-4,99 |
| Ampia 4H | HYPE | SHORT | Confluenza trend | 240m | 2,0x | 58,36732 | 56,71900 | 61,80927 | 87,25915 | 48,72988 | €424,03 | €848,06 | €50,01 | €23,95 |
| Ampia 4H | TAO | SHORT | Confluenza trend | 240m | 2,0x | 189,05650 | 189,05650 | 197,51338 | 282,63946 | 165,37722 | €558,68 | €1.117,36 | €49,98 | €-0,00 |
| Ampia 4H | XMR | LONG | Confluenza trend | 240m | 2,0x | 364,45854 | 364,45854 | 347,94701 | 184,05156 | 410,69083 | €544,42 | €1.088,84 | €49,33 | €0,00 |
| Ampia 4H | ETH | LONG | Confluenza trend | 240m | 2,0x | 1964,80288 | 1935,36000 | 1907,44021 | 992,22546 | 2125,41837 | €27,31 | €54,62 | €1,59 | €-0,82 |
| Ampia 4H | AKE | LONG | Confluenza trend | 240m | 2,0x | 0,00440 | 0,00437 | 0,00387 | 0,00222 | 0,00587 | €204,84 | €409,68 | €49,16 | €-2,14 |
| Forza relativa 1H V1 | NIGHT | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,02031 | 0,02031 | 0,02210 | 0,03036 | 0,01637 | €285,91 | €571,83 | €50,45 | €-0,00 |
| Forza relativa 1H V1 | ONDO | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,42171 | €891,90 | €1.783,80 | €49,29 | €0,00 |
| Forza relativa 1H V1 | WLD | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,32287 | €14,97 | €29,93 | €0,82 | €-0,00 |
| Forza relativa 1H V1 | AKE | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,00424 | 0,00437 | 0,00373 | 0,00214 | 0,00536 | €15,28 | €30,56 | €3,67 | €0,96 |
| Forza relativa 1H V1 | ZEC | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 483,74323 | 485,20000 | 494,91887 | 723,19613 | 459,15682 | €1.028,52 | €2.057,03 | €47,52 | €-6,19 |
| Forza relativa 1H V1 | HYPE | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 57,27654 | 56,71900 | 58,35818 | 85,62843 | 54,89695 | €1.014,19 | €2.028,38 | €38,30 | €19,74 |
| Forza relativa 1H V2 | WLD | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,32287 | €47,70 | €95,39 | €2,60 | €-0,00 |
| Forza relativa 1H V2 | XMR | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 367,08012 | 367,08012 | 360,46822 | 185,37546 | 381,62629 | €1.446,12 | €2.892,24 | €52,10 | €0,00 |
| Forza relativa 1H V2 | AKE | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,00406 | 0,00437 | 0,00406 | 0,00205 | 0,00513 | €210,28 | €420,56 | €0,00 | €32,26 |
| Benchmark Donchian breakout 1H | SUI | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,76606 | 0,76606 | 0,75182 | 0,38686 | 0,80165 | €1.377,00 | €2.754,00 | €51,18 | €0,00 |
| Benchmark Donchian breakout 1H | ALLO | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,35678 | 0,35678 | 0,39959 | 0,53338 | 0,24974 | €215,19 | €430,38 | €51,65 | €-0,00 |
| Benchmark Donchian breakout 1H | HYPE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 58,25535 | 56,71900 | 57,60397 | 87,09174 | 55,41491 | €1.364,10 | €2.728,20 | €0,00 | €71,95 |
| Benchmark Donchian breakout 1H | XRP | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 1,08939 | 1,09089 | 1,10682 | 1,62864 | 1,04582 | €1.662,45 | €3.324,89 | €53,20 | €-4,57 |
| Benchmark Donchian breakout 1H | DOGE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,07141 | 0,07178 | 0,07256 | 0,10675 | 0,06852 | €108,24 | €216,47 | €3,50 | €-1,13 |
| Benchmark Donchian breakout 1H | ZEC | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 483,74323 | 485,20000 | 496,16061 | 723,19613 | 452,69979 | €19,59 | €39,18 | €1,01 | €-0,12 |
| Donchian 1H Gb20 120R V1 | HYPE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 58,25535 | 56,71900 | 57,60397 | 87,09174 | 55,41491 | €1.281,83 | €2.563,66 | €0,00 | €67,61 |
| Donchian 1H Gb20 120R V1 | XRP | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 1,08939 | 1,09089 | 1,10682 | 1,62864 | 1,04582 | €1.562,18 | €3.124,36 | €49,99 | €-4,30 |
| Donchian 1H Gb20 120R V1 | DOGE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,07141 | 0,07178 | 0,07256 | 0,10675 | 0,06852 | €1.543,86 | €3.087,72 | €49,98 | €-16,18 |
| Donchian 1H Gb20 120R V1 | ZEC | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 483,74323 | 485,20000 | 496,16061 | 723,19613 | 452,69979 | €978,17 | €1.956,34 | €50,22 | €-5,89 |
| Benchmark Bollinger mean reversion 1H | AKE | SHORT | Bollinger mean reversion | 60m | 2,0x | 0,00424 | 0,00437 | 0,00475 | 0,00634 | 0,00348 | €208,14 | €416,27 | €49,95 | €-13,22 |
| Benchmark trend following EMA 1H | LAB | LONG | Trend following EMA | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €207,05 | €414,10 | €49,69 | €0,00 |
| Benchmark trend following EMA 1H | ALLO | SHORT | Trend following EMA | 60m | 2,0x | 0,35372 | 0,35372 | 0,39616 | 0,52881 | 0,26034 | €209,15 | €418,30 | €50,20 | €-0,00 |
| Benchmark trend following EMA 1H | XMR | LONG | Trend following EMA | 60m | 2,0x | 367,08012 | 367,08012 | 359,73357 | 185,37546 | 383,24253 | €17,91 | €35,83 | €0,72 | €0,00 |
| Benchmark trend following EMA 1H | AKE | LONG | Trend following EMA | 60m | 2,0x | 0,00426 | 0,00437 | 0,00375 | 0,00215 | 0,00539 | €203,42 | €406,84 | €48,82 | €10,53 |
| Benchmark trend following EMA 1H | XRP | SHORT | Trend following EMA | 60m | 2,0x | 1,09230 | 1,09089 | 1,10978 | 1,63299 | 1,05385 | €1.438,76 | €2.877,52 | €46,04 | €3,72 |
| Scanner Top 5 Long 1H | XMR | LONG | Scanner Top 5 Long | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10712 | €70,71 | €141,42 | €2,58 | €0,00 |
| Scanner Top 5 Long 1H | AKE | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,00406 | 0,00437 | 0,00406 | 0,00205 | 0,00504 | €216,04 | €432,09 | €0,00 | €33,14 |
| Scanner Top 5 Long 1H | PEPE | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €963,57 | €1.927,13 | €52,92 | €-22,70 |
| Scanner Bottom 5 Short 1H | ADA | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,16703 | 0,16703 | 0,16365 | 0,24971 | 0,16112 | €1.381,07 | €2.762,13 | €0,00 | €-0,00 |
| Scanner Bottom 5 Short 1H | ALLO | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,36179 | 0,36179 | 0,40521 | 0,54088 | 0,27496 | €202,53 | €405,06 | €48,61 | €-0,00 |
| Scanner Bottom 5 Short 1H | ESPORTS | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,03342 | 0,03342 | 0,03342 | 0,04997 | 0,02540 | €202,66 | €405,32 | €0,00 | €-0,00 |
| Scanner Bottom 5 Short 1H | HYPE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 58,25535 | 56,71900 | 57,49335 | 87,09174 | 56,21023 | €1.366,39 | €2.732,78 | €0,00 | €72,07 |
| Scanner Bottom 5 Short 1H | ZEC | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 483,74323 | 485,20000 | 494,91887 | 723,19613 | 461,39195 | €18,93 | €37,87 | €0,87 | €-0,11 |
| Scanner Top10 Long | XMR | LONG | Scanner Top10 Long | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10712 | €1.371,36 | €2.742,71 | €50,02 | €0,00 |
| Scanner Top10 Long | SHIB | LONG | Scanner Top10 Long | 60m | 2,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €24,14 | €48,29 | €2,71 | €-1,50 |
| Scanner Top10 Long | PEPE | LONG | Scanner Top10 Long | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €834,29 | €1.668,59 | €45,82 | €-19,65 |
| Scanner Top10 Long | AKE | LONG | Scanner Top10 Long | 60m | 2,0x | 0,00443 | 0,00437 | 0,00389 | 0,00224 | 0,00549 | €204,92 | €409,85 | €49,18 | €-4,87 |
| Scanner Bottom10 Short | ADA | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,16193 | 0,16193 | 0,16426 | 0,24209 | 0,15727 | €1.731,26 | €3.462,51 | €49,86 | €-0,00 |
| Scanner Bottom10 Short | ALLO | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,35250 | 0,35250 | 0,39075 | 0,52699 | 0,27600 | €224,69 | €449,38 | €48,76 | €-0,00 |
| Scanner Bottom10 Short | ESPORTS | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,03342 | 0,03342 | 0,03342 | 0,04997 | 0,02540 | €203,44 | €406,87 | €0,00 | €-0,00 |
| Scanner Bottom10 Short | HYPE | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 58,25535 | 56,71900 | 57,49335 | 87,09174 | 56,21023 | €1.355,36 | €2.710,73 | €0,00 | €71,49 |
| Scanner Bottom10 Short | ZEC | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 483,74323 | 485,20000 | 494,91887 | 723,19613 | 461,39195 | €18,78 | €37,56 | €0,87 | €-0,11 |
| Scanner Top15 Long | XMR | LONG | Scanner Top15 Long | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10712 | €1.371,36 | €2.742,71 | €50,02 | €0,00 |
| Scanner Top15 Long | SHIB | LONG | Scanner Top15 Long | 60m | 2,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €24,14 | €48,29 | €2,71 | €-1,50 |
| Scanner Top15 Long | PEPE | LONG | Scanner Top15 Long | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €834,29 | €1.668,59 | €45,82 | €-19,65 |
| Scanner Top15 Long | AKE | LONG | Scanner Top15 Long | 60m | 2,0x | 0,00443 | 0,00437 | 0,00389 | 0,00224 | 0,00549 | €204,92 | €409,85 | €49,18 | €-4,87 |
| Scanner Bottom15 Short | ADA | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,16193 | 0,16193 | 0,16426 | 0,24209 | 0,15727 | €1.731,26 | €3.462,51 | €49,86 | €-0,00 |
| Scanner Bottom15 Short | ALLO | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,35250 | 0,35250 | 0,39075 | 0,52699 | 0,27600 | €224,69 | €449,38 | €48,76 | €-0,00 |
| Scanner Bottom15 Short | ESPORTS | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,03342 | 0,03342 | 0,03342 | 0,04997 | 0,02540 | €203,44 | €406,87 | €0,00 | €-0,00 |
| Scanner Bottom15 Short | HYPE | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 58,25535 | 56,71900 | 57,49335 | 87,09174 | 56,21023 | €1.355,36 | €2.710,73 | €0,00 | €71,49 |
| Scanner Bottom15 Short | ZEC | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 483,74323 | 485,20000 | 494,91887 | 723,19613 | 461,39195 | €18,78 | €37,56 | €0,87 | €-0,11 |
| Scanner Top20 Long | XMR | LONG | Scanner Top20 Long | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10712 | €1.371,36 | €2.742,71 | €50,02 | €0,00 |
| Scanner Top20 Long | SHIB | LONG | Scanner Top20 Long | 60m | 2,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €24,14 | €48,29 | €2,71 | €-1,50 |
| Scanner Top20 Long | PEPE | LONG | Scanner Top20 Long | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €834,29 | €1.668,59 | €45,82 | €-19,65 |
| Scanner Top20 Long | AKE | LONG | Scanner Top20 Long | 60m | 2,0x | 0,00443 | 0,00437 | 0,00389 | 0,00224 | 0,00549 | €204,92 | €409,85 | €49,18 | €-4,87 |
| Scanner Bottom20 Short | ADA | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,16193 | 0,16193 | 0,16426 | 0,24209 | 0,15727 | €1.731,26 | €3.462,51 | €49,86 | €-0,00 |
| Scanner Bottom20 Short | ALLO | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,35250 | 0,35250 | 0,39075 | 0,52699 | 0,27600 | €224,69 | €449,38 | €48,76 | €-0,00 |
| Scanner Bottom20 Short | ESPORTS | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,03342 | 0,03342 | 0,03342 | 0,04997 | 0,02540 | €203,44 | €406,87 | €0,00 | €-0,00 |
| Scanner Bottom20 Short | HYPE | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 58,25535 | 56,71900 | 57,49335 | 87,09174 | 56,21023 | €1.355,36 | €2.710,73 | €0,00 | €71,49 |
| Scanner Bottom20 Short | ZEC | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 483,74323 | 485,20000 | 494,91887 | 723,19613 | 461,39195 | €18,78 | €37,56 | €0,87 | €-0,11 |
| Scanner Top 5 + forza BTC 1H | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39694 | 0,39694 | 0,38539 | 0,20045 | 0,42235 | €898,57 | €1.797,15 | €52,29 | €0,00 |
| Scanner Top 5 + forza BTC 1H | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €216,56 | €433,12 | €51,97 | €0,00 |
| Scanner Top 5 + forza BTC 1H | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 381,44484 | €37,16 | €74,32 | €1,36 | €0,00 |
| Scanner Top 5 + forza BTC 1H | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00406 | 0,00437 | 0,00406 | 0,00205 | 0,00513 | €216,37 | €432,74 | €0,00 | €33,19 |
| Scanner Top 5 + forza BTC 1H | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €36,82 | €73,64 | €2,02 | €-1,30 |
| Top 5 + BTC — solo MFE | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39924 | 0,39924 | 0,38729 | 0,20162 | 0,42552 | €835,46 | €1.670,91 | €50,00 | €0,00 |
| Top 5 + BTC — solo MFE | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 367,08012 | 367,08012 | 360,46822 | 185,37546 | 381,62629 | €1.363,71 | €2.727,43 | €49,13 | €0,00 |
| Top 5 + BTC — solo MFE | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00425 | 0,00437 | 0,00374 | 0,00215 | 0,00537 | €203,68 | €407,36 | €48,88 | €11,64 |
| Top 5 + BTC — Guard | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €202,47 | €404,95 | €48,59 | €0,00 |
| Top 5 + BTC — Guard | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00406 | 0,00437 | 0,00406 | 0,00205 | 0,00513 | €204,25 | €408,50 | €0,00 | €31,34 |
| Top 5 + BTC — BTC≤3 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39974 | 0,39974 | 0,38840 | 0,20187 | 0,42468 | €884,65 | €1.769,29 | €50,18 | €0,00 |
| Top 5 + BTC — BTC≤3 | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €207,87 | €415,74 | €49,89 | €0,00 |
| Top 5 + BTC — BTC≤3 | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 381,44484 | €37,63 | €75,26 | €1,37 | €0,00 |
| Top 5 + BTC — BTC≤3 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00440 | 0,00437 | 0,00387 | 0,00222 | 0,00556 | €209,03 | €418,06 | €50,17 | €-2,19 |
| Top 5 + BTC — BTC 2–3 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39974 | 0,39974 | 0,38840 | 0,20187 | 0,42468 | €884,65 | €1.769,29 | €50,18 | €0,00 |
| Top 5 + BTC — BTC 2–3 | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €207,87 | €415,74 | €49,89 | €0,00 |
| Top 5 + BTC — BTC 2–3 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00440 | 0,00437 | 0,00387 | 0,00222 | 0,00556 | €208,82 | €417,64 | €50,12 | €-2,18 |
| Top 5 + BTC — Guard + MFE | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00425 | 0,00437 | 0,00374 | 0,00215 | 0,00537 | €200,07 | €400,14 | €48,02 | €11,43 |
| Top 5 + BTC — Guard + BTC≤3 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39974 | 0,39974 | 0,38840 | 0,20187 | 0,42468 | €871,05 | €1.742,11 | €49,41 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €205,84 | €411,68 | €49,40 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00440 | 0,00437 | 0,00387 | 0,00222 | 0,00556 | €208,07 | €416,13 | €49,94 | €-2,18 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39974 | 0,39974 | 0,38840 | 0,20187 | 0,42468 | €871,05 | €1.742,11 | €49,41 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00440 | 0,00437 | 0,00387 | 0,00222 | 0,00556 | €203,53 | €407,07 | €48,85 | €-2,13 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39694 | 0,39694 | 0,38539 | 0,20045 | 0,43159 | €861,83 | €1.723,66 | €50,15 | €0,00 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,21338 | €207,96 | €415,92 | €49,91 | €0,00 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 386,79573 | €70,70 | €141,40 | €2,58 | €0,00 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €18,98 | €37,96 | €1,04 | €-0,45 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00443 | 0,00437 | 0,00389 | 0,00224 | 0,00602 | €208,49 | €416,98 | €50,04 | €-4,95 |
| Top 5 + BTC — target pieno 3R | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39694 | 0,39694 | 0,38539 | 0,20045 | 0,43159 | €861,83 | €1.723,66 | €50,15 | €0,00 |
| Top 5 + BTC — target pieno 3R | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,21338 | €207,96 | €415,92 | €49,91 | €0,00 |
| Top 5 + BTC — target pieno 3R | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 386,79573 | €85,15 | €170,29 | €3,11 | €0,00 |
| Top 5 + BTC — target pieno 3R | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €18,55 | €37,10 | €1,02 | €-0,44 |
| Top 5 + BTC — target pieno 3R | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00443 | 0,00437 | 0,00389 | 0,00224 | 0,00602 | €208,62 | €417,24 | €50,07 | €-4,96 |
| Global Confluence puro 1H | DOGE | SHORT | Global Confluence puro | 60m | 2,0x | 0,07141 | 0,07178 | 0,07256 | 0,10675 | 0,06852 | €1.512,23 | €3.024,45 | €48,95 | €-15,85 |
| Combo Trend | ALLO | SHORT | Combo Trend | 60m | 2,0x | 0,35372 | 0,35372 | 0,39616 | 0,52881 | 0,26034 | €209,35 | €418,70 | €50,24 | €-0,00 |
| Combo Trend | PEPE | LONG | Combo Trend | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €778,66 | €1.557,31 | €47,42 | €-32,14 |
| Combo Trend | AKE | LONG | Combo Trend | 60m | 2,0x | 0,00406 | 0,00437 | 0,00406 | 0,00205 | 0,00513 | €180,00 | €360,01 | €0,00 | €27,62 |
| Combo Trend | DOGE | SHORT | Combo Trend | 60m | 2,0x | 0,07141 | 0,07178 | 0,07256 | 0,10675 | 0,06886 | €1.482,27 | €2.964,54 | €47,98 | €-15,54 |
| Combo Trend | HYPE | SHORT | Combo Trend | 60m | 2,0x | 58,25535 | 56,71900 | 57,54866 | 87,09174 | 55,75576 | €77,88 | €155,76 | €0,00 | €4,11 |
| Combo Mean Reversion | XRP | LONG | Combo Mean Reversion | 60m | 2,0x | 1,08983 | 1,09089 | 1,07675 | 0,55036 | 1,11075 | €1.998,97 | €3.997,94 | €47,98 | €3,90 |
| Combo Scanner | ONDO | LONG | Combo Scanner | 60m | 2,0x | 0,39694 | 0,39694 | 0,38539 | 0,20045 | 0,42235 | €857,88 | €1.715,77 | €49,92 | €0,00 |
| Combo Scanner | LAB | LONG | Combo Scanner | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €207,54 | €415,08 | €49,81 | €0,00 |
| Combo Scanner | XMR | LONG | Combo Scanner | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 381,44484 | €23,89 | €47,78 | €0,87 | €0,00 |
| Combo Scanner | PEPE | LONG | Combo Scanner | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €18,96 | €37,93 | €1,04 | €-0,45 |
| Combo Scanner | AKE | LONG | Combo Scanner | 60m | 2,0x | 0,00443 | 0,00437 | 0,00389 | 0,00224 | 0,00559 | €205,41 | €410,83 | €49,30 | €-4,88 |
| Combo Scanner | DOGE | SHORT | Combo Scanner | 60m | 2,0x | 0,07141 | 0,07178 | 0,07245 | 0,10675 | 0,06912 | €1.631,78 | €3.263,56 | €47,54 | €-17,11 |
| Combo Adaptive — madre | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,40114 | 0,40114 | 0,38834 | 0,20258 | 0,42673 | €809,25 | €1.618,50 | €51,63 | €0,00 |
| Combo Adaptive — madre | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15861 | 0,13958 | 0,08010 | 0,19668 | €213,13 | €426,26 | €51,15 | €0,00 |
| Combo Adaptive — madre | WLD | SHORT | Combo Adaptive | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,32475 | €929,60 | €1.859,20 | €50,73 | €-0,00 |
| Combo Adaptive — madre | ALLO | SHORT | Combo Adaptive | 60m | 2,0x | 0,36179 | 0,36179 | 0,40521 | 0,54088 | 0,27496 | €210,64 | €421,27 | €50,55 | €-0,00 |
| Combo Adaptive — MFE Trail esistente | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15861 | 0,13958 | 0,08010 | 0,19668 | €201,70 | €403,39 | €48,41 | €0,00 |
| Combo Adaptive — MFE Trail esistente | WLD | SHORT | Combo Adaptive | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,32475 | €883,78 | €1.767,56 | €48,23 | €-0,00 |
| Combo Adaptive — MFE Trail esistente | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,00425 | 0,00437 | 0,00374 | 0,00215 | 0,00527 | €193,67 | €387,34 | €46,48 | €11,07 |
| Combo Adaptive — Quality7 | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,40304 | 0,40304 | 0,39140 | 0,20354 | 0,42632 | €859,15 | €1.718,30 | €49,62 | €0,00 |
| Combo Adaptive — Quality7 | WLD | SHORT | Combo Adaptive | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,32475 | €919,99 | €1.839,97 | €50,21 | €-0,00 |
| Combo Adaptive — Quality7 | ALLO | SHORT | Combo Adaptive | 60m | 2,0x | 0,36179 | 0,36179 | 0,40521 | 0,54088 | 0,27496 | €207,61 | €415,23 | €49,83 | €-0,00 |
| Combo Adaptive — Quality7 | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,00440 | 0,00437 | 0,00387 | 0,00222 | 0,00545 | €210,58 | €421,15 | €50,54 | €-2,20 |
| Combo Adaptive — Trend/Transition | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15861 | 0,13958 | 0,08010 | 0,19668 | €206,52 | €413,04 | €49,56 | €0,00 |
| Combo Adaptive — Trend/Transition | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,00424 | 0,00437 | 0,00373 | 0,00214 | 0,00526 | €200,45 | €400,89 | €48,11 | €12,56 |
| Combo Adaptive — Trend/Transition | HYPE | SHORT | Combo Adaptive | 60m | 2,0x | 58,25535 | 56,71900 | 57,43804 | 87,09174 | 56,21023 | €1.407,07 | €2.814,14 | €0,00 | €74,22 |
| Combo Adaptive — Trend/Transition | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,07141 | 0,07178 | 0,07245 | 0,10675 | 0,06933 | €43,33 | €86,66 | €1,26 | €-0,45 |
| Combo Adaptive — Quality7 + Regime | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,40554 | 0,40554 | 0,39390 | 0,20480 | 0,42882 | €864,27 | €1.728,54 | €49,61 | €0,00 |
| Combo Adaptive — Quality7 + Regime | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,00406 | 0,00437 | 0,00406 | 0,00205 | 0,00504 | €205,26 | €410,51 | €0,00 | €31,49 |
| Combo Adaptive — Long Only | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,41951 | €893,67 | €1.787,34 | €49,39 | €0,00 |
| Combo Adaptive — Long Only | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €205,55 | €411,10 | €49,33 | €0,00 |
| Combo Adaptive — Long Only | XMR | LONG | Combo Adaptive | 60m | 2,0x | 367,08012 | 367,08012 | 360,46822 | 185,37546 | 380,30391 | €1.384,19 | €2.768,37 | €49,86 | €0,00 |
| Combo Adaptive — Long Only | SHIB | LONG | Combo Adaptive | 60m | 2,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €12,85 | €25,69 | €1,44 | €-0,80 |
| Combo Adaptive — Long Only | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,00406 | 0,00437 | 0,00406 | 0,00205 | 0,00504 | €208,51 | €417,03 | €0,00 | €31,99 |
| Combo Adaptive — parziale 1R | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,41951 | €893,02 | €1.786,04 | €49,36 | €0,00 |
| Combo Adaptive — parziale 1R | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €205,22 | €410,44 | €49,25 | €0,00 |
| Combo Adaptive — parziale 1R | WLD | SHORT | Combo Adaptive | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,32475 | €895,30 | €1.790,60 | €48,86 | €-0,00 |
| Combo Adaptive — parziale 1R | ALLO | SHORT | Combo Adaptive | 60m | 2,0x | 0,36179 | 0,36179 | 0,40521 | 0,54088 | 0,27496 | €98,69 | €197,38 | €23,69 | €-0,00 |
| Combo Adaptive — parziale 1R | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,00406 | 0,00437 | 0,00406 | 0,00205 | 0,00504 | €93,51 | €187,03 | €0,00 | €14,35 |
| Combo Adaptive — parziale 1R | HYPE | SHORT | Combo Adaptive | 60m | 2,0x | 58,25535 | 56,71900 | 57,43804 | 87,09174 | 56,21023 | €8,26 | €16,52 | €0,00 | €0,44 |
| Combo Adaptive — Quality7 + Regime + parziale 1R | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,40554 | 0,40554 | 0,39390 | 0,20480 | 0,42882 | €864,27 | €1.728,54 | €49,61 | €0,00 |
| Combo Adaptive — Quality7 + Regime + parziale 1R | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,00406 | 0,00437 | 0,00406 | 0,00205 | 0,00504 | €207,20 | €414,39 | €0,00 | €31,79 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,43050 | €902,18 | €1.804,37 | €49,86 | €0,00 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | WLD | SHORT | Combo Adaptive | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,31537 | €919,67 | €1.839,35 | €50,19 | €-0,00 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | XMR | LONG | Combo Adaptive | 60m | 2,0x | 367,08012 | 367,08012 | 360,46822 | 185,37546 | 386,91580 | €27,35 | €54,70 | €0,99 | €0,00 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | ALLO | SHORT | Combo Adaptive | 60m | 2,0x | 0,36179 | 0,36179 | 0,40521 | 0,54088 | 0,23155 | €207,78 | €415,57 | €49,87 | €-0,00 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,00406 | 0,00437 | 0,00406 | 0,00205 | 0,00552 | €210,79 | €421,58 | €0,00 | €32,34 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | HYPE | SHORT | Combo Adaptive | 60m | 2,0x | 58,25535 | 56,71900 | 57,43804 | 87,09174 | 55,18767 | €43,89 | €87,77 | €0,00 | €2,31 |
| Combo Adaptive — target pieno 3R | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,43050 | €902,18 | €1.804,37 | €49,86 | €0,00 |
| Combo Adaptive — target pieno 3R | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15861 | 0,13958 | 0,08010 | 0,21571 | €207,43 | €414,86 | €49,78 | €0,00 |
| Combo Adaptive — target pieno 3R | WLD | SHORT | Combo Adaptive | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,31537 | €911,80 | €1.823,59 | €49,76 | €-0,00 |
| Combo Adaptive — target pieno 3R | ALLO | SHORT | Combo Adaptive | 60m | 2,0x | 0,36179 | 0,36179 | 0,40521 | 0,54088 | 0,23155 | €205,00 | €410,00 | €49,20 | €-0,00 |
| Sol Donchian 4H | SOL | SHORT | Donchian breakout 20 barre | 240m | 2,0x | 75,96380 | 75,53200 | 78,23939 | 113,56589 | 69,59218 | €830,21 | €1.660,43 | €49,74 | €9,44 |
| Sol Adaptive 4H | SOL | SHORT | Combo Adaptive | 240m | 2,0x | 75,96380 | 75,53200 | 78,44626 | 113,56589 | 69,75767 | €761,04 | €1.522,08 | €49,74 | €8,65 |
| Eth Ema 4H | ETH | LONG | Trend following EMA | 240m | 2,0x | 1949,77988 | 1935,36000 | 1902,99144 | 984,63884 | 2066,75096 | €1.036,30 | €2.072,59 | €49,74 | €-15,33 |
| Doge Donchian 1H | DOGE | SHORT | Donchian breakout 20 barre | 60m | 3,0x | 0,07141 | 0,07178 | 0,07233 | 0,09485 | 0,06956 | €1.286,97 | €3.860,92 | €49,99 | €-20,24 |
| Master Adaptive V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39854 | 0,39854 | 0,38677 | 0,20126 | 0,42207 | €833,00 | €1.665,99 | €49,19 | €0,00 |
| Master Adaptive V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €203,80 | €407,60 | €48,91 | €0,00 |
| Master Adaptive V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10713 | €21,54 | €43,08 | €0,79 | €0,00 |
| Master Adaptive V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00406 | 0,00437 | 0,00357 | 0,00205 | 0,00504 | €202,05 | €404,11 | €48,49 | €31,00 |
| Master Adaptive No Alt V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39854 | 0,39854 | 0,38677 | 0,20126 | 0,42207 | €833,00 | €1.665,99 | €49,19 | €0,00 |
| Master Adaptive No Alt V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €203,80 | €407,60 | €48,91 | €0,00 |
| Master Adaptive No Alt V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10713 | €21,54 | €43,08 | €0,79 | €0,00 |
| Master Adaptive No Alt V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00406 | 0,00437 | 0,00357 | 0,00205 | 0,00504 | €202,14 | €404,28 | €48,51 | €31,01 |
| Master Adaptive Strict3 V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,41951 | €887,07 | €1.774,14 | €49,03 | €0,00 |
| Master Adaptive Strict3 V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10713 | €1.330,61 | €2.661,21 | €48,54 | €0,00 |
| Master Adaptive Strict3 V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 1943,95871 | 1935,36000 | 1915,96571 | 981,69915 | 1999,94472 | €1.509,27 | €3.018,53 | €43,47 | €-13,35 |
| Master Adaptive Strict3 V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00443 | 0,00437 | 0,00389 | 0,00224 | 0,00549 | €198,88 | €397,76 | €47,73 | €-4,73 |
| Master Adaptive Expanded V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39854 | 0,39854 | 0,38677 | 0,20126 | 0,42207 | €833,00 | €1.665,99 | €49,19 | €0,00 |
| Master Adaptive Expanded V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €203,80 | €407,60 | €48,91 | €0,00 |
| Master Adaptive Expanded V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10713 | €33,54 | €67,08 | €1,22 | €0,00 |
| Master Adaptive Expanded V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00406 | 0,00437 | 0,00357 | 0,00205 | 0,00504 | €202,97 | €405,94 | €48,71 | €31,14 |
| Master Adaptive Gb20 V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,40304 | 0,40304 | 0,39140 | 0,20354 | 0,42632 | €848,64 | €1.697,27 | €49,02 | €0,00 |
| Master Adaptive Gb20 V1 | RIF | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,10582 | 0,10582 | 0,09312 | 0,05344 | 0,13122 | €201,89 | €403,77 | €48,45 | €0,00 |
| Master Adaptive Gb20 V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 367,08012 | 367,08012 | 360,46822 | 185,37546 | 380,30391 | €1.348,01 | €2.696,02 | €48,56 | €0,00 |
| Master Adaptive Gb20 V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00443 | 0,00437 | 0,00389 | 0,00224 | 0,00549 | €193,43 | €386,85 | €46,42 | €-4,60 |
| Master Adaptive Runner25 V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39854 | 0,39854 | 0,38677 | 0,20126 | 0,43384 | €833,00 | €1.665,99 | €49,19 | €0,00 |
| Master Adaptive Runner25 V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,21338 | €203,80 | €407,60 | €48,91 | €0,00 |
| Master Adaptive Runner25 V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 386,79573 | €20,87 | €41,74 | €0,76 | €0,00 |
| Master Adaptive Runner25 V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00406 | 0,00437 | 0,00357 | 0,00205 | 0,00552 | €202,72 | €405,45 | €48,65 | €31,10 |
| Combo Adaptive — Side × Regime Guard | ALLO | SHORT | Combo Adaptive | 60m | 2,0x | 0,35250 | 0,35250 | 0,39075 | 0,52699 | 0,27600 | €235,86 | €471,72 | €51,19 | €-0,00 |
| Combo Adaptive — Side × Regime Guard | SHIB | LONG | Combo Adaptive | 60m | 2,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €450,93 | €901,86 | €50,61 | €-28,09 |
| Combo Adaptive — Side × Regime Guard | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,00406 | 0,00437 | 0,00406 | 0,00205 | 0,00504 | €209,98 | €419,96 | €0,00 | €32,21 |
| Combo Adaptive — Side × Regime Guard | HYPE | SHORT | Combo Adaptive | 60m | 2,0x | 58,25535 | 56,71900 | 57,43804 | 87,09174 | 56,21023 | €1.447,79 | €2.895,59 | €0,00 | €76,36 |
| Combo Adaptive — Side × Regime Guard | ZEC | SHORT | Combo Adaptive | 60m | 2,0x | 483,74323 | 485,20000 | 494,91887 | 723,19613 | 461,39195 | €34,68 | €69,35 | €1,60 | €-0,21 |
| Master Adaptive GB20 — Breakeven 0,5R | BEAT | LONG | Master Adaptive Consensus | 60m | 2,0x | 3,29017 | 3,29017 | 3,00714 | 1,66154 | 3,85623 | €291,32 | €582,63 | €50,12 | €0,00 |
| Master Adaptive GB20 — Breakeven 0,5R | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 367,86058 | 367,86058 | 361,23463 | 185,76959 | 381,11249 | €1.403,77 | €2.807,55 | €50,57 | €0,00 |
| Master Adaptive GB20 — Breakeven 0,5R | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00406 | 0,00437 | 0,00406 | 0,00205 | 0,00504 | €207,34 | €414,67 | €0,00 | €31,81 |
| Master Adaptive GB20 — 50% a 0,75R | BEAT | LONG | Master Adaptive Consensus | 60m | 2,0x | 3,29017 | 3,29017 | 3,00714 | 1,66154 | 3,85623 | €291,05 | €582,09 | €50,07 | €0,00 |
| Master Adaptive GB20 — 50% a 0,75R | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10713 | €1.376,47 | €2.752,95 | €50,21 | €0,00 |
| Master Adaptive GB20 — 50% a 0,75R | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00406 | 0,00437 | 0,00406 | 0,00205 | 0,00504 | €103,26 | €206,52 | €0,00 | €15,84 |
| Master Adaptive GB20 — Loss Cap 0,75R | BEAT | LONG | Master Adaptive Consensus | 60m | 2,0x | 3,29017 | 3,29017 | 3,07790 | 1,66154 | 3,85623 | €388,25 | €776,50 | €50,10 | €0,00 |
| Master Adaptive GB20 — Loss Cap 0,75R | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 361,71345 | 185,19860 | 380,10713 | €1.835,86 | €3.671,71 | €50,22 | €0,00 |
| Master Adaptive GB20 — Loss Cap 0,75R | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00406 | 0,00437 | 0,00357 | 0,00205 | 0,00536 | €207,77 | €415,53 | €49,86 | €31,87 |
| Rapida V3 NoHigh — Range Only | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,33165 | 0,33165 | 0,36472 | 0,44055 | 0,28205 | €170,92 | €512,75 | €51,13 | €-0,00 |
| Rapida V3 NoHigh — Range Only | ESPORTS | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,02828 | 0,02828 | 0,03168 | 0,03757 | 0,02319 | €142,68 | €428,04 | €51,37 | €-0,00 |
| Rapida V3 NoHigh — Regime Guard | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,33165 | 0,33165 | 0,36472 | 0,44055 | 0,28205 | €172,19 | €516,57 | €51,51 | €-0,00 |
| MAIN — Side × Regime Guard | ALLO | SHORT | Confluenza trend | 240m | 3,0x | 0,38070 | 0,38070 | 0,37357 | 0,50570 | 0,28933 | €140,03 | €420,08 | €0,00 | €-0,00 |
| MAIN — Side × Regime Guard | PEPE | LONG | Confluenza trend | 240m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €326,47 | €979,41 | €50,44 | €-5,05 |
| MAIN — Side × Regime Guard | AKE | LONG | Confluenza trend | 240m | 3,0x | 0,00440 | 0,00437 | 0,00387 | 0,00295 | 0,00545 | €142,16 | €426,47 | €51,18 | €-2,23 |
| MAIN — Side × Regime Guard | HYPE | SHORT | Confluenza trend | 240m | 3,0x | 57,27654 | 56,71900 | 59,33830 | 76,08234 | 53,15302 | €471,26 | €1.413,79 | €50,89 | €13,76 |
| MAIN — Dynamic Asset Selector | AKE | LONG | Confluenza trend | 240m | 3,0x | 0,00440 | 0,00437 | 0,00387 | 0,00295 | 0,00545 | €142,87 | €428,60 | €51,43 | €-2,24 |
| Combo Trend — Side × Regime Guard | ALLO | SHORT | Combo Trend | 60m | 2,0x | 0,35250 | 0,35250 | 0,39480 | 0,52699 | 0,25944 | €209,77 | €419,55 | €50,35 | €-0,00 |
| Combo Trend — Side × Regime Guard | ESPORTS | SHORT | Combo Trend | 60m | 2,0x | 0,02845 | 0,02845 | 0,03187 | 0,04254 | 0,02094 | €202,36 | €404,73 | €48,57 | €-0,00 |
| Combo Trend — Side × Regime Guard | AKE | LONG | Combo Trend | 60m | 2,0x | 0,00443 | 0,00437 | 0,00389 | 0,00224 | 0,00559 | €211,47 | €422,95 | €50,75 | €-5,03 |
| Combo Trend — Side × Regime Guard | DOGE | SHORT | Combo Trend | 60m | 2,0x | 0,07141 | 0,07178 | 0,07256 | 0,10675 | 0,06886 | €1.560,52 | €3.121,05 | €50,52 | €-16,36 |
| Combo Trend — Side × Regime Guard | HYPE | SHORT | Combo Trend | 60m | 2,0x | 58,25535 | 56,71900 | 57,54866 | 87,09174 | 55,75576 | €47,00 | €94,00 | €0,00 | €2,48 |
| FAST NoHigh <7,5 · SHORT only | WLD | SHORT | Momentum / breakout | 60m | 3,0x | 0,34959 | 0,34959 | 0,35668 | 0,46437 | 0,33896 | €822,35 | €2.467,06 | €50,00 | €-0,00 |
| FAST NoHigh <7,5 · SHORT only | ALLO | SHORT | Momentum / breakout | 60m | 3,0x | 0,33808 | 0,33808 | 0,36389 | 0,44909 | 0,29937 | €212,58 | €637,75 | €48,69 | €-0,00 |
| FAST NoHigh <7,5 · SHORT only | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00443 | 0,00437 | 0,00389 | 0,00297 | 0,00522 | €141,55 | €424,64 | €50,96 | €-5,05 |
| Bilanciata V3 · LONG only | XMR | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 366,72991 | 366,72991 | 360,04130 | 246,32025 | 380,10712 | €913,56 | €2.740,69 | €49,99 | €0,00 |
| Bilanciata V3 · LONG only | ALLO | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,34255 | 0,34255 | 0,37914 | 0,45502 | 0,26938 | €156,01 | €468,04 | €49,99 | €-0,00 |
| Bilanciata V3 · LONG only | ESPORTS | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,03342 | 0,03342 | 0,03342 | 0,04440 | 0,02540 | €137,40 | €412,21 | €0,00 | €-0,00 |
| Bilanciata V3 · LONG only | PEPE | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €596,90 | €1.790,71 | €49,18 | €-21,09 |
| Bilanciata V3 · LONG only | HYPE | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 58,25535 | 56,71900 | 57,49335 | 77,38252 | 56,21023 | €22,17 | €66,50 | €0,00 | €1,75 |
| Scanner Bottom5 Short Profit Lock V1 | WLD | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,34449 | 0,34449 | 0,35368 | 0,51502 | 0,32613 | €937,87 | €1.875,74 | €50,00 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | ALLO | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,35250 | 0,35250 | 0,39075 | 0,52699 | 0,27600 | €227,60 | €455,20 | €49,39 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | ESPORTS | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,03342 | 0,03342 | 0,03262 | 0,04997 | 0,02540 | €206,07 | €412,14 | €0,00 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | HYPE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 58,25535 | 56,71900 | 57,49335 | 87,09174 | 56,21023 | €1.387,39 | €2.774,78 | €0,00 | €73,18 |
| Scanner Bottom5 Short Profit Lock V1 | ZEC | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 483,74323 | 485,20000 | 494,91887 | 723,19613 | 461,39195 | €19,22 | €38,45 | €0,89 | €-0,12 |
| Scanner Bottom5 Short Mfe Trail V1 | WLD | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,34449 | 0,34449 | 0,35368 | 0,51502 | 0,32613 | €937,87 | €1.875,74 | €50,00 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | ALLO | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,35653 | 0,35653 | 0,39522 | 0,53301 | 0,27915 | €228,22 | €456,45 | €49,53 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | ESPORTS | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,02828 | 0,02828 | 0,03168 | 0,04229 | 0,02150 | €206,75 | €413,50 | €49,62 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | HYPE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 58,25535 | 56,71900 | 57,39774 | 87,09174 | 56,21023 | €1.405,00 | €2.810,01 | €0,00 | €74,11 |
| Scanner Bottom5 Short Mfe Trail V1 | ZEC | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 483,74323 | 485,20000 | 494,91887 | 723,19613 | 461,39195 | €19,47 | €38,94 | €0,90 | €-0,12 |
| Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00443 | 0,00437 | 0,00389 | 0,00297 | 0,00549 | €141,91 | €425,73 | €51,09 | €-5,06 |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00443 | 0,00437 | 0,00389 | 0,00297 | 0,00575 | €138,20 | €414,59 | €49,75 | €-4,93 |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | HYPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 58,25535 | 56,71900 | 57,38273 | 77,38252 | 56,26704 | €1.211,99 | €3.635,97 | €0,00 | €95,89 |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 483,74323 | 485,20000 | 492,43540 | 642,57226 | 462,01282 | €927,74 | €2.783,21 | €50,01 | €-8,38 |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | XRP | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,08796 | 1,09089 | 1,10015 | 1,44518 | 1,05750 | €1.488,07 | €4.464,20 | €50,00 | €-12,01 |
| Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,35250 | 0,35250 | 0,38225 | 0,46824 | 0,29300 | €194,51 | €583,53 | €49,25 | €-0,00 |
| Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | ESPORTS | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,02998 | 0,02998 | 0,02998 | 0,03983 | 0,02279 | €132,90 | €398,69 | €0,00 | €-0,00 |
| Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00425 | 0,00437 | 0,00374 | 0,00286 | 0,00527 | €136,65 | €409,95 | €49,19 | €11,71 |
| Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | HYPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 58,25535 | 56,71900 | 57,38273 | 77,38252 | 56,66470 | €1.197,49 | €3.592,46 | €0,00 | €94,74 |
| Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 483,74323 | 485,20000 | 492,43540 | 642,57226 | 466,35890 | €43,20 | €129,60 | €2,33 | €-0,39 |
| Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | ESPORTS | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,02828 | 0,02828 | 0,03168 | 0,03757 | 0,02150 | €141,08 | €423,23 | €50,79 | €-0,00 |
| Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,35250 | 0,35250 | 0,38225 | 0,46824 | 0,29300 | €190,72 | €572,15 | €48,29 | €-0,00 |
| Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00424 | 0,00437 | 0,00373 | 0,00285 | 0,00526 | €140,36 | €421,09 | €50,53 | €13,20 |
| Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | HYPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 58,25535 | 56,71900 | 57,38273 | 77,38252 | 56,66470 | €1.227,68 | €3.683,05 | €0,00 | €97,13 |
| Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 483,74323 | 485,20000 | 492,43540 | 642,57226 | 466,35890 | €939,82 | €2.819,46 | €50,66 | €-8,49 |
| Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | XRP | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,08796 | 1,09089 | 1,10015 | 1,44518 | 1,06359 | €84,48 | €253,44 | €2,84 | €-0,68 |
| Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00406 | 0,00437 | 0,00406 | 0,00273 | 0,00528 | €137,82 | €413,47 | €0,00 | €31,72 |
| Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | HYPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 58,25535 | 56,71900 | 57,38273 | 77,38252 | 56,26704 | €1.201,53 | €3.604,59 | €0,00 | €95,06 |
| Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 483,74323 | 485,20000 | 492,43540 | 642,57226 | 462,01282 | €919,87 | €2.759,61 | €49,59 | €-8,31 |
| Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | XRP | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,08796 | 1,09089 | 1,10015 | 1,44518 | 1,05750 | €1.475,45 | €4.426,35 | €49,58 | €-11,91 |
| Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,33808 | 0,33808 | 0,36389 | 0,44909 | 0,28646 | €211,10 | €633,31 | €48,35 | €-0,00 |
| Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00425 | 0,00437 | 0,00374 | 0,00286 | 0,00527 | €142,68 | €428,05 | €51,37 | €12,23 |
| Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 483,74323 | 485,20000 | 492,43540 | 642,57226 | 466,35890 | €958,36 | €2.875,08 | €51,66 | €-8,66 |
| Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | XRP | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,08796 | 1,09089 | 1,10015 | 1,44518 | 1,06359 | €117,45 | €352,36 | €3,95 | €-0,95 |
| Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | HYPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 57,61747 | 56,71900 | 57,43863 | 76,53521 | 55,91174 | €1.119,85 | €3.359,56 | €0,00 | €52,39 |
| Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00424 | 0,00437 | 0,00373 | 0,00285 | 0,00526 | €138,53 | €415,58 | €49,87 | €13,02 |
| Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00424 | 0,00437 | 0,00373 | 0,00285 | 0,00526 | €142,59 | €427,78 | €51,33 | €13,41 |
| Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,35250 | 0,35250 | 0,38225 | 0,46824 | 0,29300 | €194,51 | €583,53 | €49,25 | €-0,00 |
| Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00424 | 0,00437 | 0,00373 | 0,00285 | 0,00526 | €136,23 | €408,68 | €49,04 | €12,81 |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,33713 | 0,33713 | 0,36471 | 0,44782 | 0,28197 | €208,24 | €624,73 | €51,11 | €-0,00 |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | ESPORTS | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,03070 | 0,03070 | 0,03070 | 0,04078 | 0,02333 | €138,06 | €414,17 | €0,00 | €-0,00 |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00443 | 0,00437 | 0,00389 | 0,00297 | 0,00549 | €141,35 | €424,04 | €50,88 | €-5,04 |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | HYPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 58,25535 | 56,71900 | 57,38273 | 77,38252 | 56,66470 | €1.242,47 | €3.727,41 | €0,00 | €98,30 |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 483,74323 | 485,20000 | 492,43540 | 642,57226 | 466,35890 | €46,24 | €138,72 | €2,49 | €-0,42 |
| Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00443 | 0,00437 | 0,00389 | 0,00297 | 0,00549 | €144,01 | €432,02 | €51,84 | €-5,13 |
| Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,35250 | 0,35250 | 0,38225 | 0,46824 | 0,29300 | €200,65 | €601,96 | €50,80 | €-0,00 |
| Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | ESPORTS | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,03342 | 0,03342 | 0,03342 | 0,04440 | 0,02540 | €136,12 | €408,37 | €0,00 | €-0,00 |
| Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00406 | 0,00437 | 0,00406 | 0,00273 | 0,00528 | €137,23 | €411,70 | €0,00 | €31,58 |
| Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00406 | 0,00437 | 0,00406 | 0,00273 | 0,00528 | €137,23 | €411,70 | €0,00 | €31,58 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Combo Adaptive — MFE Trail esistente | ONDO | LONG | 2026-07-27T18:23:38+00:00 | 0,39760 | €-2,53 | -0,05 | TIME_EXIT_NO_CANDLES |
| Rapida V3 — senza ESPORTS | HYPE | SHORT | 2026-07-27T18:23:38+00:00 | 57,07377 | €68,16 | 1,40 | TARGET |
| Rapida V3 — score <7,5 | HYPE | SHORT | 2026-07-27T18:23:38+00:00 | 57,07377 | €72,87 | 1,40 | TARGET |
| Rapida 1H V3 Filtered — madre | HYPE | SHORT | 2026-07-27T18:23:38+00:00 | 57,07377 | €69,54 | 1,40 | TARGET |
| Rapida V1 — senza PEPE | HYPE | SHORT | 2026-07-27T18:23:38+00:00 | 57,07377 | €71,33 | 1,40 | TARGET |
| Rapida score 6–7,5 — Cost Aware | HYPE | SHORT | 2026-07-27T18:23:38+00:00 | 57,07377 | €72,48 | 1,40 | TARGET |
| Rapida score 6–7,5 — senza Trend Up | HYPE | SHORT | 2026-07-27T18:23:38+00:00 | 57,07377 | €72,05 | 1,40 | TARGET |
| Rapida V1 — score 6–7,5 | HYPE | SHORT | 2026-07-27T18:23:38+00:00 | 57,07377 | €72,76 | 1,40 | TARGET |
| Top 5 + BTC — Guard | ONDO | LONG | 2026-07-27T18:08:40+00:00 | 0,39700 | €-2,59 | -0,05 | TIME_EXIT_NO_CANDLES |
| Top 5 + BTC — Guard + MFE | ONDO | LONG | 2026-07-27T18:08:40+00:00 | 0,39700 | €-2,59 | -0,05 | TIME_EXIT_NO_CANDLES |
| Combo Adaptive — Trend/Transition | ONDO | LONG | 2026-07-27T18:08:40+00:00 | 0,39700 | €-2,59 | -0,05 | TIME_EXIT_NO_CANDLES |
| Rapida V3 senza ESPORTS — MFE Lock | HYPE | SHORT | 2026-07-27T16:53:38+00:00 | 58,03183 | €9,91 | 0,19 | STOP_GAP_STRESS |

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
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 19/30 | 18/30 | 0,84 | 2,41 | -0,12R | €10,79 | 2,01% | DIVERGENTE | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 1/30 | 2/30 | 0,00 | 0,00 | -1,08R | €-28,25 | 1,14% | COERENTE − | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 17/30 | 21/30 | 0,75 | 2,10 | -0,19R | €15,91 | 1,62% | DIVERGENTE | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 17/30 | 21/30 | 0,75 | 1,70 | -0,19R | €10,00 | 2,27% | DIVERGENTE | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 21/30 | 25/30 | 0,57 | 0,85 | -0,35R | €-3,10 | 2,95% | COERENTE − | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 5/30 | 5/30 | 0,00 | 0,00 | -1,04R | €-46,29 | 2,20% | COERENTE − | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 5/30 | 7/30 | 1,28 | 1,03 | 0,17R | €0,61 | 2,15% | COERENTE + | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 14/30 | 14/30 | 1,38 | 4,59 | 0,23R | €16,93 | 1,01% | COERENTE + | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 25/30 | 21/30 | 0,71 | 0,65 | -0,22R | €-8,01 | 2,93% | COERENTE − | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 5/30 | 5/30 | 0,00 | 0,00 | -1,04R | €-46,29 | 2,20% | COERENTE − | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 21/30 | 24/30 | 0,91 | 1,60 | -0,07R | €8,90 | 2,97% | DIVERGENTE | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 22/30 | 30/30 | 0,85 | 1,65 | -0,11R | €8,82 | 2,51% | DIVERGENTE | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 11/30 | 14/30 | 1,00 | 0,97 | -0,00R | €-0,67 | 2,46% | COERENTE − | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 22/30 | 25/30 | 0,68 | 1,12 | -0,24R | €2,20 | 2,70% | DIVERGENTE | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 25/30 | 20/30 | 0,71 | 0,60 | -0,22R | €-9,55 | 3,08% | COERENTE − | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 5/30 | 5/30 | 0,00 | 0,00 | -1,04R | €-35,58 | 1,99% | COERENTE − | RACCOLTA RESEARCH |
| MAIN | Principale 4H | 70/30 | 24/30 | 1,07 | 0,71 | 0,05R | €-10,51 | 4,76% | DIVERGENTE | BOCCIATA RESEARCH |
| MAIN_DYNAMIC_ASSET_SELECTOR_V1 | MAIN — Dynamic Asset Selector | 0/30 | 7/30 | 0,00 | 3,51 | 0,00R | €40,93 | 1,06% | n/a | RACCOLTA RESEARCH |
| MAIN_SIDE_REGIME_GUARD_V1 | MAIN — Side × Regime Guard | 0/30 | 9/30 | 0,00 | 1,80 | 0,00R | €19,70 | 1,77% | n/a | RACCOLTA RESEARCH |
| RSI_EXTREME_LONG_15M | Scalp RSI Long 25 · prudente · 5x (riferimento tra 9 varianti) | 12/30 | 7/30 | 0,24 | 0,12 | -0,63R | €-6,34 | 0,58% | COERENTE − | RACCOLTA RESEARCH |
| RSI_EXTREME_SHORT_15M | Scalp RSI Short 75 · prudente · 5x (riferimento tra 9 varianti) | 13/30 | 10/30 | 0,40 | 0,27 | -0,39R | €-4,83 | 0,58% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_1H_BALANCED | Bilanciata 1H V1 | 188/30 | 54/30 | 0,97 | 1,27 | -0,02R | €5,26 | 3,56% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_BALANCED_LONG_NO_RHV_V1 | Bilanciata 1H — LONG senza Range High Vol | 0/30 | 13/30 | 0,00 | 0,71 | 0,00R | €-9,82 | 2,47% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_BALANCED_SHORT_TREND_DOWN_STRICT_V1 | Bilanciata 1H — SHORT Trend Down stretto | 0/30 | 1/30 | 0,00 | 0,00 | 0,00R | €-4,13 | 0,59% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_BALANCED_V2 | Bilanciata 1H V2 | 51/30 | 35/30 | 1,38 | 1,27 | 0,22R | €5,48 | 2,75% | COERENTE + | PRONTA PER REVISIONE LIVE |
| SHADOW_1H_BALANCED_V3 | Bilanciata 1H V3 Filtered | 88/30 | 50/30 | 1,05 | 1,63 | 0,03R | €12,57 | 2,20% | COERENTE + | BOCCIATA RESEARCH |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | Bilanciata V3 · LONG only | 13/30 | 10/30 | 0,55 | 1,01 | -0,36R | €0,15 | 1,46% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_1H_FAST | Rapida 1H V1 — madre | 207/30 | 77/30 | 0,91 | 1,03 | -0,06R | €0,67 | 6,76% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | Rapida V1 — Long + BTC 1–3 + score <7,5 | 26/30 | 23/30 | 1,46 | 1,14 | 0,23R | €2,82 | 2,07% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | FAST NoHigh <7,5 · SHORT only | 26/30 | 22/30 | 1,35 | 1,62 | 0,19R | €8,44 | 1,76% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | Rapida V1 — no HIGH + score <7,5 | 92/30 | 58/30 | 1,13 | 1,51 | 0,07R | €9,39 | 2,83% | COERENTE + | PRONTA PER REVISIONE LIVE |
| SHADOW_1H_FAST_NO_PEPE_V1 | Rapida V1 — senza PEPE | 99/30 | 49/30 | 0,91 | 1,27 | -0,06R | €5,20 | 2,15% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_COST_AWARE_V1 | Rapida score 6–7,5 — Cost Aware | 0/30 | 20/30 | 0,00 | 2,61 | 0,00R | €22,69 | 1,96% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_NO_TREND_UP_V1 | Rapida score 6–7,5 — senza Trend Up | 0/30 | 17/30 | 0,00 | 2,53 | 0,00R | €22,11 | 2,01% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_RANGE_ONLY_V1 | Rapida score 6–7,5 — Range Only | 0/30 | 11/30 | 0,00 | 2,70 | 0,00R | €29,23 | 2,28% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_V1 | Rapida V1 — score 6–7,5 | 69/30 | 57/30 | 1,11 | 1,49 | 0,06R | €8,66 | 2,49% | COERENTE + | PRONTA PER REVISIONE LIVE |
| SHADOW_1H_FAST_TP2_V1 | Rapida V1 — target pieno 2R | 95/30 | 55/30 | 0,84 | 0,96 | -0,12R | €-0,86 | 2,58% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V2 | Rapida 1H V2 | 14/30 | 14/30 | 0,62 | 0,95 | -0,26R | €-1,11 | 1,69% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3 | Rapida 1H V3 Filtered — madre | 141/30 | 84/30 | 1,04 | 1,12 | 0,02R | €2,37 | 2,89% | COERENTE + | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_CAP75_V1 | Rapida V3 — score <7,5 | 80/30 | 51/30 | 1,03 | 1,62 | 0,02R | €9,99 | 2,49% | COERENTE + | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | Rapida V3 — qualità completa + profit lock | 46/30 | 47/30 | 0,96 | 1,08 | -0,02R | €1,75 | 3,21% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | Rapida V3 — Long + no HIGH + score <7,5 | 46/30 | 42/30 | 0,96 | 0,98 | -0,02R | €-0,47 | 2,86% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | Rapida V3 — Long Only | 60/30 | 49/30 | 0,92 | 0,78 | -0,05R | €-5,29 | 3,67% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V1 | Rapida V3 NoHigh — Range Only | 0/30 | 10/30 | 0,00 | 2,84 | 0,00R | €29,80 | 1,78% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_V1 | Rapida V3 NoHigh — Regime Guard | 0/30 | 18/30 | 0,00 | 3,42 | 0,00R | €22,03 | 1,39% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | Rapida V3 — no volatilità HIGH | 96/30 | 58/30 | 0,99 | 0,92 | -0,01R | €-1,78 | 2,96% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONLY_V1 | Rapida V3 senza ESPORTS — Long Only | 0/30 | 28/30 | 0,00 | 1,49 | 0,00R | €7,33 | 1,61% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_V1 | Rapida V3 senza ESPORTS — MFE Lock | 0/30 | 34/30 | 0,00 | 1,65 | 0,00R | €8,03 | 2,05% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_GUARD_V1 | Rapida V3 senza ESPORTS — Stress Guard | 0/30 | 19/30 | 0,00 | 1,16 | 0,00R | €3,75 | 2,17% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | Rapida V3 — senza ESPORTS | 95/30 | 58/30 | 0,92 | 0,99 | -0,05R | €-0,14 | 2,49% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_4H_WIDE | Ampia 4H | 55/30 | 19/30 | 1,02 | 1,05 | 0,02R | €1,54 | 3,68% | COERENTE + | BOCCIATA RESEARCH |
| SHADOW_BOLLINGER_MR_1H | Benchmark Bollinger mean reversion 1H | 56/30 | 42/30 | 1,35 | 1,00 | 0,19R | €0,05 | 4,19% | COERENTE + | BOCCIATA PAPER |
| SHADOW_BTC_ADAPTIVE_1H | Btc Adaptive 1H | 4/30 | 3/30 | 0,00 | 1,24 | -1,11R | €4,43 | 0,89% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_BTC_ADAPTIVE_4H | Btc Adaptive 4H | 1/30 | 1/30 | 0,00 | 0,00 | -1,07R | €-50,38 | 0,74% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_BOLLINGER_1H | Btc Bollinger 1H | 3/30 | 3/30 | ∞ | ∞ | 1,37R | €56,04 | 0,54% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_BTC_BOLLINGER_4H | Btc Bollinger 4H | 1/30 | 1/30 | ∞ | ∞ | 1,72R | €84,12 | 0,30% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_BTC_DONCHIAN_1H | Btc Donchian 1H | 5/30 | 4/30 | 0,00 | 0,82 | -1,12R | €-4,84 | 1,49% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_DONCHIAN_4H | Btc Donchian 4H | 1/30 | 1/30 | 0,00 | 0,00 | -1,07R | €-49,32 | 0,96% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_EMA_1H | Btc Ema 1H | 4/30 | 6/30 | 0,57 | 0,59 | -0,36R | €-14,69 | 1,56% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_EMA_4H | Btc Ema 4H | 1/30 | 1/30 | 0,00 | 0,00 | -1,07R | €-49,32 | 0,96% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE | Combo Adaptive — madre | 135/30 | 25/30 | 1,08 | 1,52 | 0,06R | €8,26 | 1,49% | COERENTE + | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | Combo Adaptive — Long Only | 47/30 | 13/30 | 0,82 | 1,04 | -0,13R | €0,93 | 2,34% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | Combo Adaptive — MFE Trail esistente | 102/30 | 33/30 | 0,99 | 0,49 | -0,01R | €-12,93 | 5,33% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | Combo Adaptive — parziale 1R | 76/30 | 22/30 | 0,86 | 0,51 | -0,10R | €-13,50 | 3,32% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | Combo Adaptive — Quality7 + Regime + parziale 1R | 8/30 | 9/30 | 0,62 | 0,64 | -0,29R | €-10,55 | 1,95% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | Combo Adaptive — Quality7 + Regime | 8/30 | 9/30 | 0,62 | 0,32 | -0,29R | €-20,85 | 2,32% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | Combo Adaptive — Quality7 | 22/30 | 19/30 | 1,31 | 1,47 | 0,19R | €5,84 | 1,51% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | Combo Adaptive — Trend/Transition | 38/30 | 18/30 | 0,43 | 0,72 | -0,48R | €-6,88 | 2,18% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | Combo Adaptive — 75% a 2R + runner 25% a 3R | 41/30 | 25/30 | 0,58 | 1,27 | -0,36R | €5,39 | 2,12% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_SIDE_REGIME_GUARD_V1 | Combo Adaptive — Side × Regime Guard | 0/30 | 16/30 | 0,00 | 1,83 | 0,00R | €11,45 | 1,41% | n/a | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | Combo Adaptive — target pieno 3R | 41/30 | 13/30 | 0,58 | 0,76 | -0,36R | €-5,13 | 1,41% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_MEAN_REVERSION | Combo Mean Reversion | 21/30 | 17/30 | 1,14 | 0,99 | 0,08R | €-0,30 | 2,31% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_COMBO_SCANNER | Combo Scanner | 83/30 | 39/30 | 1,38 | 0,94 | 0,23R | €-1,50 | 3,25% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_COMBO_TREND | Combo Trend | 107/30 | 43/30 | 0,98 | 0,74 | -0,01R | €-9,25 | 7,02% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_TREND_SIDE_REGIME_GUARD_V1 | Combo Trend — Side × Regime Guard | 0/30 | 18/30 | 0,00 | 1,43 | 0,00R | €6,65 | 1,71% | n/a | RACCOLTA RESEARCH |
| SHADOW_DOGE_BOLLINGER_1H | Doge Bollinger 1H | 2/30 | 2/30 | 0,00 | 0,00 | -1,12R | €-55,56 | 1,26% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_DOGE_DONCHIAN_1H | Doge Donchian 1H | 3/30 | 4/30 | 0,84 | 0,98 | -0,12R | €-0,31 | 1,08% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_DOGE_EMA_1H | Doge Ema 1H | 4/30 | 8/30 | 1,71 | 1,55 | 0,39R | €11,48 | 1,36% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_DONCHIAN_1H | Benchmark Donchian breakout 1H | 67/30 | 30/30 | 0,80 | 2,20 | -0,16R | €21,48 | 2,12% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | Donchian 1H Gb20 120R V1 | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 1,09% | n/a | RACCOLTA RESEARCH |
| SHADOW_EMA_TREND_1H | Benchmark trend following EMA 1H | 111/30 | 31/30 | 1,00 | 0,71 | -0,00R | €-7,56 | 3,29% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_ETH_ADAPTIVE_1H | Eth Adaptive 1H | 6/30 | 6/30 | 0,34 | 0,08 | -0,61R | €-33,40 | 2,09% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_BOLLINGER_1H | Eth Bollinger 1H | 2/30 | 2/30 | 1,21 | 0,28 | 0,12R | €-20,26 | 0,91% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_ETH_DONCHIAN_1H | Eth Donchian 1H | 5/30 | 5/30 | 0,42 | 0,42 | -0,52R | €-25,60 | 1,62% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_EMA_1H | Eth Ema 1H | 6/30 | 8/30 | 0,34 | 0,16 | -0,61R | €-34,02 | 2,76% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_EMA_4H | Eth Ema 4H | 1/30 | 1/30 | 0,00 | 0,00 | -1,06R | €-52,88 | 0,96% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_GLOBAL_PURE | Global Confluence puro 1H | 4/30 | 10/30 | 1,75 | 0,37 | 0,41R | €-20,93 | 2,92% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | Master Adaptive Expanded V1 | 45/30 | 18/30 | 0,78 | 0,62 | -0,16R | €-16,29 | 3,64% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_BE_V1 | Master Adaptive GB20 — Breakeven 0,5R | 0/30 | 19/30 | 0,00 | 0,79 | 0,00R | €-5,36 | 3,15% | n/a | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_LOSS_CAP_V1 | Master Adaptive GB20 — Loss Cap 0,75R | 0/30 | 16/30 | 0,00 | 0,71 | 0,00R | €-9,99 | 3,63% | n/a | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_PARTIAL_V1 | Master Adaptive GB20 — 50% a 0,75R | 0/30 | 14/30 | 0,00 | 0,70 | 0,00R | €-9,79 | 2,50% | n/a | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | Master Adaptive Gb20 V1 | 45/30 | 50/30 | 0,70 | 0,59 | -0,22R | €-7,49 | 4,27% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | Master Adaptive No Alt V1 | 40/30 | 15/30 | 0,74 | 0,53 | -0,19R | €-22,21 | 4,03% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | Master Adaptive Runner25 V1 | 35/30 | 17/30 | 0,73 | 0,58 | -0,22R | €-17,97 | 3,98% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | Master Adaptive Strict3 V1 | 34/30 | 23/30 | 0,79 | 0,54 | -0,15R | €-20,94 | 5,58% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_V1 | Master Adaptive V1 | 45/30 | 15/30 | 0,70 | 0,53 | -0,22R | €-22,47 | 4,07% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_RELATIVE_STRENGTH | Forza relativa 1H V1 | 136/30 | 35/30 | 0,97 | 0,54 | -0,02R | €-14,16 | 7,55% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_RELATIVE_STRENGTH_V2 | Forza relativa 1H V2 | 51/30 | 43/30 | 1,46 | 1,04 | 0,28R | €1,21 | 5,10% | COERENTE + | BOCCIATA PAPER |
| SHADOW_SCANNER_BOTTOM10_SHORT | Scanner Bottom10 Short | 6/30 | 6/30 | 0,00 | 0,11 | -1,11R | €-40,88 | 2,72% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_BOTTOM15_SHORT | Scanner Bottom15 Short | 6/30 | 6/30 | 0,00 | 0,11 | -1,11R | €-40,88 | 2,72% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_BOTTOM20_SHORT | Scanner Bottom20 Short | 6/30 | 6/30 | 0,00 | 0,11 | -1,11R | €-40,88 | 2,72% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT | Scanner Bottom 5 Short 1H | 50/30 | 29/30 | 0,80 | 0,61 | -0,14R | €-9,96 | 5,48% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT_CONTINUATION_V1 | Scanner Bottom5 Short Continuation V1 | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | Scanner Bottom5 Short Mfe Trail V1 | 2/30 | 6/30 | 0,00 | 0,54 | -1,10R | €-12,45 | 1,38% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | Scanner Bottom5 Short Profit Lock V1 | 2/30 | 5/30 | 0,00 | 0,25 | -1,10R | €-24,00 | 1,53% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP10_LONG | Scanner Top10 Long | 16/30 | 14/30 | 1,13 | 0,59 | 0,09R | €-11,97 | 3,78% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP15_LONG | Scanner Top15 Long | 17/30 | 14/30 | 1,02 | 0,59 | 0,02R | €-11,97 | 3,78% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP20_LONG | Scanner Top20 Long | 17/30 | 14/30 | 1,02 | 0,59 | 0,02R | €-11,97 | 3,78% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC | Scanner Top 5 + forza BTC 1H | 81/30 | 33/30 | 1,36 | 1,49 | 0,22R | €11,24 | 3,23% | COERENTE + | PRONTA PER REVISIONE LIVE |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | Top 5 + BTC — BTC 2–3 | 18/30 | 7/30 | 0,79 | 1,14 | -0,16R | €3,57 | 2,84% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | Top 5 + BTC — BTC≤3 | 37/30 | 14/30 | 1,00 | 1,03 | 0,00R | €0,92 | 3,23% | COERENTE + | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | Top 5 + BTC — Guard + BTC≤3 + MFE | 31/30 | 28/30 | 1,17 | 0,70 | 0,11R | €-8,68 | 3,93% | DIVERGENTE | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | Top 5 + BTC — Guard + BTC≤3 | 31/30 | 13/30 | 1,17 | 0,98 | 0,11R | €-0,85 | 3,23% | DIVERGENTE | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | Top 5 + BTC — Guard + MFE | 36/30 | 35/30 | 0,96 | 0,58 | -0,02R | €-11,75 | 5,08% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | Top 5 + BTC — Guard | 36/30 | 20/30 | 0,96 | 0,65 | -0,02R | €-11,90 | 3,36% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | Top 5 + BTC — solo MFE | 43/30 | 25/30 | 0,96 | 0,59 | -0,03R | €-8,85 | 3,95% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | Top 5 + BTC — 75% a 2,2R + runner 3R | 33/30 | 21/30 | 1,10 | 1,17 | 0,08R | €4,32 | 3,25% | COERENTE + | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | Top 5 + BTC — target pieno 3R | 33/30 | 17/30 | 1,10 | 1,19 | 0,08R | €5,68 | 3,22% | COERENTE + | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_SCANNER_TOP5_LONG | Scanner Top 5 Long 1H | 96/30 | 44/30 | 1,28 | 1,57 | 0,16R | €12,57 | 3,57% | COERENTE + | PRONTA PER REVISIONE LIVE |
| SHADOW_SOL_ADAPTIVE_1H | Sol Adaptive 1H | 6/30 | 6/30 | 0,85 | 0,29 | -0,11R | €-27,47 | 2,34% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_ADAPTIVE_4H | Sol Adaptive 4H | 1/30 | 1/30 | 0,00 | 0,00 | -1,05R | €-51,83 | 0,77% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_BOLLINGER_1H | Sol Bollinger 1H | 3/30 | 4/30 | 0,60 | 0,41 | -0,30R | €-24,69 | 1,89% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_BOLLINGER_4H | Sol Bollinger 4H | 1/30 | 1/30 | ∞ | ∞ | 1,74R | €86,98 | 0,40% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_SOL_DONCHIAN_1H | Sol Donchian 1H | 3/30 | 3/30 | 0,84 | 21,53 | -0,12R | €30,71 | 0,79% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SOL_DONCHIAN_4H | Sol Donchian 4H | 1/30 | 1/30 | 0,00 | 0,00 | -1,06R | €-52,00 | 0,79% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_EMA_1H | Sol Ema 1H | 5/30 | 5/30 | 1,14 | 0,86 | 0,09R | €-4,58 | 1,67% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SOL_EMA_4H | Sol Ema 4H | 2/30 | 2/30 | 0,00 | 0,00 | -1,06R | €-51,84 | 1,06% | COERENTE − | RACCOLTA RESEARCH |

Per le famiglie RSI con più configurazioni di leva o margine, il lato paper usa il conto con il maggior numero di eventi indipendenti; i conti duplicati non vengono aggregati.
`PRONTA PER REVISIONE LIVE` non invia ordini e non sposta capitale: abilita soltanto una revisione manuale finale.

## 🎯 DOGE Rejection Short — conto dedicato €3.600

Simulazione separata **paper only**: capitale/margine iniziale **€3.600**, leva **5x**, esposizione iniziale **€18.000**. Non modifica i conti paper da €10.000 e non invia ordini reali.

- Stato: **WAITING**
- Prezzo DOGE: **0.07178**
- Pre-allarme: **0.0765**; zona armata: **0.0775**; trigger rejection: **0.078**
- Invalidazione prima dell’entrata: chiusura 15m sopra **0.07966**

| Capitale iniziale | Balance | Equity | P&L aperto | Eventi chiusi | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- |
| €3.600,00 | €3.600,00 | €3.600,00 | €0,00 | 0 | 0,00% | 0,00 | 0,00% |

### Filtri correnti

| Filtro | Valore | Stato |
| --- | --- | --- |
| Dati mercato | FRESH | OK |
| Candela 15m | 24.7 min | OK |
| Global DOGE | -6.0 | OK |
| Classic raw | -11.0 | OK |
| DOGE/BTC raw | -6.0 | OK |
| Pattern ribassista | MATURO | OK |
| BTC sotto filtro | 64833.7 | OK |

### Ultima candela 15m valutata

- Rejection accettata: **NO**; motivo: **trigger_touched, entry_not_chased, upper_wick**
- High **0.07212**; close **0.07192**; wick alta **10.0%**; volume **x0.74**

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

- Regime: **RANGE_HIGH_VOL**
- Famiglia: **RANGE**
- Confidenza: **63,60%**
- Volatilità: **HIGH**
- Rotazione strategie: **SOLO OSSERVAZIONE — nessun peso operativo viene ancora modificato**
- Motivo: Direzione poco definita: score BTC +1.0, breadth EMA50 50%, ADX 19.0.
- BTC trend score: **1,00**; ADX: **19,04**; breadth sopra EMA50: **50,00%**
- Mediana alt vs BTC: **-0,88%**; dispersione: **14,59%**

- Aperti in questo ciclo: **0**
- Chiusi in questo ciclo: **0**
- Posizioni research aperte: **533**
- Trade research chiusi: **3997**
- Eventi di mercato indipendenti chiusi: **922**
- Segnali sovrapposti saltati sullo stesso asset/profilo: **18211**
- Posizioni Research V1 senza regime scartate durante la migrazione: **28**

### Risultati complessivi per strategia

| Profilo | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | 6 | 19 | 19 | 31,58% | 0,84 | -0,12R | €-22,98 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | 4 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,75 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | 1 | 17 | 17 | 29,41% | 0,75 | -0,19R | €-32,73 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | 1 | 17 | 17 | 29,41% | 0,75 | -0,19R | €-32,72 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | 1 | 21 | 21 | 23,81% | 0,57 | -0,35R | €-73,65 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | 1 | 5 | 5 | 0,00% | 0,00 | -1,04R | €-51,94 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | 2 | 5 | 5 | 40,00% | 1,28 | 0,17R | €8,72 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | 1 | 14 | 14 | 42,86% | 1,38 | 0,23R | €31,73 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | 2 | 25 | 25 | 28,00% | 0,71 | -0,22R | €-54,29 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | 1 | 5 | 5 | 0,00% | 0,00 | -1,04R | €-51,94 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | 1 | 21 | 21 | 33,33% | 0,91 | -0,07R | €-13,98 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | 6 | 22 | 22 | 31,82% | 0,85 | -0,11R | €-24,15 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | 0 | 11 | 11 | 36,36% | 1,00 | -0,00R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | 6 | 22 | 22 | 27,27% | 0,68 | -0,24R | €-53,89 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | 7 | 25 | 25 | 28,00% | 0,71 | -0,22R | €-54,29 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | 5 | 5 | 5 | 0,00% | 0,00 | -1,04R | €-51,94 |
| MAIN | 15 | 70 | 70 | 35,71% | 1,07 | 0,05R | €32,21 |
| RSI_EXTREME_LONG_15M | 0 | 12 | 12 | 25,00% | 0,24 | -0,63R | €-75,99 |
| RSI_EXTREME_SHORT_15M | 0 | 13 | 13 | 30,77% | 0,40 | -0,39R | €-50,12 |
| Bilanciata 1H V1 | 16 | 188 | 188 | 32,98% | 0,97 | -0,02R | €-40,58 |
| Bilanciata 1H V2 | 8 | 58 | 51 | 41,38% | 1,38 | 0,22R | €128,47 |
| Bilanciata 1H V3 Filtered | 12 | 88 | 88 | 35,23% | 1,05 | 0,03R | €30,72 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | 7 | 13 | 13 | 23,08% | 0,55 | -0,36R | €-47,32 |
| Rapida 1H V1 | 1 | 207 | 207 | 38,65% | 0,91 | -0,06R | €-116,21 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | 0 | 26 | 26 | 50,00% | 1,46 | 0,23R | €59,32 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | 4 | 26 | 26 | 50,00% | 1,35 | 0,19R | €48,36 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | 5 | 92 | 92 | 44,57% | 1,13 | 0,07R | €67,94 |
| SHADOW_1H_FAST_NO_PEPE_V1 | 9 | 99 | 99 | 39,39% | 0,91 | -0,06R | €-54,80 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | 5 | 69 | 69 | 44,93% | 1,11 | 0,06R | €44,70 |
| SHADOW_1H_FAST_TP2_V1 | 10 | 95 | 95 | 31,58% | 0,84 | -0,12R | €-109,92 |
| Rapida 1H V2 | 1 | 16 | 14 | 31,25% | 0,62 | -0,26R | €-42,07 |
| Rapida 1H V3 Filtered | 9 | 141 | 141 | 42,55% | 1,04 | 0,02R | €33,83 |
| SHADOW_1H_FAST_V3_CAP75_V1 | 8 | 80 | 80 | 42,50% | 1,03 | 0,02R | €12,09 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | 2 | 46 | 46 | 41,30% | 0,96 | -0,02R | €-11,34 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | 2 | 46 | 46 | 41,30% | 0,96 | -0,02R | €-11,34 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | 2 | 60 | 60 | 40,00% | 0,92 | -0,05R | €-32,12 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | 5 | 96 | 96 | 41,67% | 0,99 | -0,01R | €-7,02 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | 8 | 95 | 95 | 40,00% | 0,92 | -0,05R | €-48,26 |
| SHADOW_4H_WIDE | 24 | 55 | 55 | 27,27% | 1,02 | 0,02R | €9,14 |
| SHADOW_BOLLINGER_MR_1H | 3 | 56 | 56 | 50,00% | 1,35 | 0,19R | €103,83 |
| SHADOW_BTC_ADAPTIVE_1H | 0 | 4 | 4 | 0,00% | 0,00 | -1,11R | €-44,44 |
| SHADOW_BTC_ADAPTIVE_4H | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,67 |
| SHADOW_BTC_BOLLINGER_1H | 0 | 3 | 3 | 100,00% | ∞ | 1,37R | €41,00 |
| SHADOW_BTC_BOLLINGER_4H | 0 | 1 | 1 | 100,00% | ∞ | 1,72R | €17,16 |
| SHADOW_BTC_DONCHIAN_1H | 0 | 5 | 5 | 0,00% | 0,00 | -1,12R | €-56,25 |
| SHADOW_BTC_DONCHIAN_4H | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,71 |
| SHADOW_BTC_EMA_1H | 1 | 4 | 4 | 25,00% | 0,57 | -0,36R | €-14,44 |
| SHADOW_BTC_EMA_4H | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,71 |
| SHADOW_COMBO_ADAPTIVE | 16 | 135 | 135 | 36,30% | 1,08 | 0,06R | €74,76 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | 6 | 47 | 47 | 29,79% | 0,82 | -0,13R | €-61,49 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | 16 | 102 | 102 | 34,31% | 0,99 | -0,01R | €-6,69 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | 16 | 76 | 76 | 31,58% | 0,86 | -0,10R | €-76,41 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | 3 | 8 | 8 | 25,00% | 0,62 | -0,29R | €-23,54 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | 3 | 8 | 8 | 25,00% | 0,62 | -0,29R | €-23,54 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | 6 | 22 | 22 | 40,91% | 1,31 | 0,19R | €42,26 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | 5 | 38 | 38 | 18,42% | 0,43 | -0,48R | €-183,75 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | 6 | 41 | 41 | 17,07% | 0,58 | -0,36R | €-148,38 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | 6 | 41 | 41 | 17,07% | 0,58 | -0,36R | €-148,38 |
| SHADOW_COMBO_MEAN_REVERSION | 1 | 21 | 21 | 42,86% | 1,14 | 0,08R | €17,24 |
| SHADOW_COMBO_SCANNER | 7 | 83 | 83 | 39,76% | 1,38 | 0,23R | €192,41 |
| SHADOW_COMBO_TREND | 17 | 107 | 107 | 31,78% | 0,98 | -0,01R | €-14,24 |
| SHADOW_DOGE_BOLLINGER_1H | 0 | 2 | 2 | 0,00% | 0,00 | -1,12R | €-22,46 |
| SHADOW_DOGE_DONCHIAN_1H | 1 | 3 | 3 | 33,33% | 0,84 | -0,12R | €-3,55 |
| SHADOW_DOGE_EMA_1H | 0 | 4 | 4 | 50,00% | 1,71 | 0,39R | €15,73 |
| SHADOW_DONCHIAN_1H | 10 | 67 | 67 | 25,37% | 0,80 | -0,16R | €-105,41 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | 5 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_EMA_TREND_1H | 15 | 111 | 111 | 31,53% | 1,00 | -0,00R | €-3,27 |
| SHADOW_ETH_ADAPTIVE_1H | 0 | 6 | 6 | 16,67% | 0,34 | -0,61R | €-36,67 |
| SHADOW_ETH_BOLLINGER_1H | 0 | 2 | 2 | 50,00% | 1,21 | 0,12R | €2,33 |
| SHADOW_ETH_DONCHIAN_1H | 0 | 5 | 5 | 20,00% | 0,42 | -0,52R | €-26,11 |
| SHADOW_ETH_EMA_1H | 0 | 6 | 6 | 16,67% | 0,34 | -0,61R | €-36,55 |
| SHADOW_ETH_EMA_4H | 1 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,57 |
| SHADOW_GLOBAL_PURE | 1 | 4 | 4 | 50,00% | 1,75 | 0,41R | €16,33 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | 7 | 45 | 45 | 28,89% | 0,78 | -0,16R | €-70,31 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | 7 | 45 | 45 | 26,67% | 0,70 | -0,22R | €-99,52 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | 7 | 40 | 40 | 27,50% | 0,74 | -0,19R | €-76,54 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | 8 | 35 | 35 | 20,00% | 0,73 | -0,22R | €-75,35 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | 6 | 34 | 34 | 29,41% | 0,79 | -0,15R | €-52,19 |
| SHADOW_MASTER_ADAPTIVE_V1 | 7 | 45 | 45 | 26,67% | 0,70 | -0,22R | €-99,52 |
| Forza relativa 1H V1 | 18 | 136 | 136 | 30,88% | 0,97 | -0,02R | €-30,23 |
| Forza relativa 1H V2 | 7 | 56 | 51 | 41,07% | 1,46 | 0,28R | €157,85 |
| SHADOW_SCANNER_BOTTOM10_SHORT | 9 | 6 | 6 | 0,00% | 0,00 | -1,11R | €-66,45 |
| SHADOW_SCANNER_BOTTOM15_SHORT | 9 | 6 | 6 | 0,00% | 0,00 | -1,11R | €-66,45 |
| SHADOW_SCANNER_BOTTOM20_SHORT | 9 | 6 | 6 | 0,00% | 0,00 | -1,11R | €-66,45 |
| SHADOW_SCANNER_BOTTOM5_SHORT | 11 | 50 | 50 | 28,00% | 0,80 | -0,14R | €-67,84 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | 8 | 2 | 2 | 0,00% | 0,00 | -1,10R | €-22,10 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | 8 | 2 | 2 | 0,00% | 0,00 | -1,10R | €-22,10 |
| SHADOW_SCANNER_TOP10_LONG | 3 | 16 | 16 | 37,50% | 1,13 | 0,09R | €13,94 |
| SHADOW_SCANNER_TOP15_LONG | 3 | 17 | 17 | 35,29% | 1,02 | 0,02R | €2,83 |
| SHADOW_SCANNER_TOP20_LONG | 3 | 17 | 17 | 35,29% | 1,02 | 0,02R | €2,83 |
| SHADOW_SCANNER_TOP5_BTC | 6 | 81 | 81 | 38,27% | 1,36 | 0,22R | €179,49 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | 5 | 18 | 18 | 27,78% | 0,79 | -0,16R | €-29,46 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | 7 | 37 | 37 | 32,43% | 1,00 | 0,00R | €0,26 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | 4 | 31 | 31 | 35,48% | 1,17 | 0,11R | €34,23 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | 4 | 31 | 31 | 35,48% | 1,17 | 0,11R | €34,23 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | 3 | 36 | 36 | 30,56% | 0,96 | -0,02R | €-8,98 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | 3 | 36 | 36 | 30,56% | 0,96 | -0,02R | €-8,98 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | 6 | 43 | 43 | 30,23% | 0,96 | -0,03R | €-12,21 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | 8 | 33 | 33 | 27,27% | 1,10 | 0,08R | €25,22 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | 8 | 33 | 33 | 27,27% | 1,10 | 0,08R | €25,22 |
| SHADOW_SCANNER_TOP5_LONG | 4 | 96 | 96 | 38,54% | 1,28 | 0,16R | €156,90 |
| SHADOW_SOL_ADAPTIVE_1H | 0 | 6 | 6 | 33,33% | 0,85 | -0,11R | €-6,52 |
| SHADOW_SOL_ADAPTIVE_4H | 1 | 1 | 1 | 0,00% | 0,00 | -1,05R | €-10,52 |
| SHADOW_SOL_BOLLINGER_1H | 0 | 3 | 3 | 33,33% | 0,60 | -0,30R | €-9,00 |
| SHADOW_SOL_BOLLINGER_4H | 0 | 1 | 1 | 100,00% | ∞ | 1,74R | €17,38 |
| SHADOW_SOL_DONCHIAN_1H | 0 | 3 | 3 | 33,33% | 0,84 | -0,12R | €-3,58 |
| SHADOW_SOL_DONCHIAN_4H | 1 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,56 |
| SHADOW_SOL_EMA_1H | 0 | 5 | 5 | 40,00% | 1,14 | 0,09R | €4,59 |
| SHADOW_SOL_EMA_4H | 0 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,12 |

### Matrice strategia × regime all’entrata

| Profilo | Regime entrata | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | ALT_ROTATION_DOWN | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | ALT_ROTATION_UP | 0 | 12 | 12 | 41,67% | 1,27 | 0,17R | €20,58 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | RANGE | 1 | 4 | 4 | 25,00% | 0,64 | -0,28R | €-11,25 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TRANSITION | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_UP | 1 | 2 | 2 | 0,00% | 0,00 | -1,11R | €-22,18 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_UP_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | ALT_ROTATION_DOWN | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TRANSITION | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TREND_UP | 1 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,75 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | ALT_ROTATION_UP | 0 | 10 | 10 | 40,00% | 1,16 | 0,11R | €10,84 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | RANGE | 0 | 4 | 4 | 25,00% | 0,64 | -0,28R | €-11,26 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | TREND_UP | 1 | 2 | 2 | 0,00% | 0,00 | -1,11R | €-22,18 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | ALT_ROTATION_UP | 0 | 10 | 10 | 40,00% | 1,16 | 0,11R | €10,84 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | RANGE | 0 | 4 | 4 | 25,00% | 0,64 | -0,28R | €-11,25 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | TREND_UP | 1 | 2 | 2 | 0,00% | 0,00 | -1,11R | €-22,18 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | ALT_ROTATION_UP | 0 | 8 | 8 | 37,50% | 1,03 | 0,02R | €1,85 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | RANGE | 0 | 5 | 5 | 20,00% | 0,48 | -0,43R | €-21,45 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | RANGE_LOW_VOL | 0 | 2 | 2 | 50,00% | 1,93 | 0,47R | €9,42 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TREND_UP | 1 | 6 | 6 | 0,00% | 0,00 | -1,06R | €-63,46 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TREND_UP | 1 | 5 | 5 | 0,00% | 0,00 | -1,04R | €-51,94 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | RANGE | 2 | 3 | 3 | 33,33% | 0,97 | -0,02R | €-0,70 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | RANGE_LOW_VOL | 0 | 2 | 2 | 50,00% | 1,93 | 0,47R | €9,42 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | ALT_ROTATION_UP | 1 | 9 | 9 | 44,44% | 1,43 | 0,26R | €23,01 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | RANGE | 0 | 3 | 3 | 33,33% | 0,97 | -0,02R | €-0,70 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | RANGE_LOW_VOL | 0 | 2 | 2 | 50,00% | 1,93 | 0,47R | €9,42 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | ALT_ROTATION_UP | 1 | 10 | 10 | 40,00% | 1,18 | 0,12R | €11,58 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | RANGE | 0 | 6 | 6 | 16,67% | 0,39 | -0,53R | €-31,62 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 3,88 | 0,97R | €29,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | TREND_UP | 1 | 6 | 6 | 0,00% | 0,00 | -1,06R | €-63,46 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | TREND_UP | 1 | 5 | 5 | 0,00% | 0,00 | -1,04R | €-51,94 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | ALT_ROTATION_UP | 0 | 9 | 9 | 44,44% | 1,39 | 0,24R | €21,41 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | RANGE | 0 | 5 | 5 | 60,00% | 2,86 | 0,76R | €38,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TREND_UP | 1 | 6 | 6 | 0,00% | 0,00 | -1,06R | €-63,46 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | ALT_ROTATION_DOWN | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | ALT_ROTATION_UP | 1 | 9 | 9 | 44,44% | 1,39 | 0,24R | €21,41 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | RANGE | 0 | 6 | 6 | 50,00% | 1,91 | 0,47R | €28,04 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | RANGE_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TRANSITION | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_UP | 1 | 6 | 6 | 0,00% | 0,00 | -1,06R | €-63,46 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | ALT_ROTATION_UP | 0 | 7 | 7 | 42,86% | 1,30 | 0,19R | €13,25 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | RANGE_LOW_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,96R | €19,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | TREND_UP | 0 | 3 | 3 | 0,00% | 0,00 | -1,10R | €-32,97 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | ALT_ROTATION_DOWN | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | ALT_ROTATION_UP | 1 | 8 | 8 | 37,50% | 1,03 | 0,02R | €1,85 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | RANGE | 0 | 5 | 5 | 20,00% | 0,48 | -0,43R | €-21,49 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | RANGE_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 3,88 | 0,97R | €29,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TRANSITION | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_UP | 1 | 6 | 6 | 0,00% | 0,00 | -1,06R | €-63,46 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | ALT_ROTATION_DOWN | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | ALT_ROTATION_UP | 1 | 10 | 10 | 40,00% | 1,18 | 0,12R | €11,58 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | RANGE | 0 | 6 | 6 | 16,67% | 0,39 | -0,53R | €-31,62 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | RANGE_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 3,88 | 0,97R | €29,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TRANSITION | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_UP | 1 | 6 | 6 | 0,00% | 0,00 | -1,06R | €-63,46 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_UP_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | ALT_ROTATION_DOWN | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | RANGE_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TRANSITION | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TREND_UP | 1 | 5 | 5 | 0,00% | 0,00 | -1,04R | €-51,94 |
| MAIN | ALT_ROTATION_DOWN | 2 | 3 | 3 | 33,33% | 0,96 | -0,03R | €-0,88 |
| MAIN | ALT_ROTATION_UP | 3 | 9 | 9 | 11,11% | 0,24 | -0,69R | €-61,86 |
| MAIN | RANGE | 6 | 26 | 26 | 34,62% | 1,02 | 0,01R | €3,46 |
| MAIN | RANGE_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| MAIN | RANGE_LOW_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| MAIN | TRANSITION | 0 | 8 | 8 | 50,00% | 1,93 | 0,47R | €37,99 |
| MAIN | TREND_UP | 3 | 17 | 17 | 35,29% | 1,05 | 0,03R | €5,57 |
| MAIN | TREND_UP_HIGH_VOL | 1 | 5 | 5 | 40,00% | 1,26 | 0,16R | €8,19 |
| RSI_EXTREME_LONG_15M | RANGE | 0 | 8 | 8 | 12,50% | 0,06 | -0,92R | €-73,76 |
| RSI_EXTREME_LONG_15M | TRANSITION | 0 | 2 | 2 | 50,00% | 1,14 | 0,08R | €1,56 |
| RSI_EXTREME_LONG_15M | TREND_UP | 0 | 2 | 2 | 50,00% | 0,63 | -0,19R | €-3,79 |
| RSI_EXTREME_SHORT_15M | ALT_ROTATION_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 1,47R | €14,67 |
| RSI_EXTREME_SHORT_15M | ALT_ROTATION_UP | 0 | 4 | 4 | 25,00% | 0,05 | -0,86R | €-34,43 |
| RSI_EXTREME_SHORT_15M | RANGE | 0 | 2 | 2 | 50,00% | 0,27 | -0,45R | €-8,98 |
| RSI_EXTREME_SHORT_15M | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -0,41R | €-4,13 |
| RSI_EXTREME_SHORT_15M | TREND_UP | 0 | 5 | 5 | 20,00% | 0,43 | -0,34R | €-17,24 |
| Bilanciata 1H V1 | ALT_ROTATION_DOWN | 3 | 13 | 13 | 23,08% | 0,60 | -0,30R | €-38,51 |
| Bilanciata 1H V1 | ALT_ROTATION_UP | 2 | 20 | 20 | 40,00% | 1,21 | 0,13R | €26,91 |
| Bilanciata 1H V1 | RANGE | 4 | 52 | 52 | 40,38% | 1,29 | 0,18R | €91,41 |
| Bilanciata 1H V1 | RANGE_HIGH_VOL | 1 | 11 | 11 | 0,00% | 0,00 | -1,07R | €-118,08 |
| Bilanciata 1H V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| Bilanciata 1H V1 | TRANSITION | 3 | 30 | 30 | 33,33% | 1,00 | -0,00R | €-0,05 |
| Bilanciata 1H V1 | TREND_DOWN | 2 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| Bilanciata 1H V1 | TREND_UP | 1 | 47 | 47 | 36,17% | 1,16 | 0,10R | €46,76 |
| Bilanciata 1H V1 | TREND_UP_HIGH_VOL | 0 | 13 | 13 | 23,08% | 0,67 | -0,22R | €-28,71 |
| Bilanciata 1H V2 | ALT_ROTATION_UP | 3 | 10 | 8 | 40,00% | 1,21 | 0,13R | €13,27 |
| Bilanciata 1H V2 | RANGE | 4 | 28 | 26 | 39,29% | 1,25 | 0,15R | €42,71 |
| Bilanciata 1H V2 | TRANSITION | 1 | 20 | 17 | 45,00% | 1,69 | 0,36R | €72,49 |
| Bilanciata 1H V3 Filtered | ALT_ROTATION_DOWN | 3 | 11 | 11 | 36,36% | 1,04 | 0,03R | €3,17 |
| Bilanciata 1H V3 Filtered | ALT_ROTATION_UP | 2 | 8 | 8 | 25,00% | 0,61 | -0,32R | €-25,49 |
| Bilanciata 1H V3 Filtered | RANGE | 4 | 21 | 21 | 47,62% | 1,67 | 0,37R | €78,21 |
| Bilanciata 1H V3 Filtered | RANGE_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,83 |
| Bilanciata 1H V3 Filtered | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| Bilanciata 1H V3 Filtered | TRANSITION | 1 | 8 | 8 | 37,50% | 1,11 | 0,07R | €5,68 |
| Bilanciata 1H V3 Filtered | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,14 |
| Bilanciata 1H V3 Filtered | TREND_UP | 1 | 22 | 22 | 40,91% | 1,40 | 0,23R | €50,25 |
| Bilanciata 1H V3 Filtered | TREND_UP_HIGH_VOL | 0 | 14 | 14 | 21,43% | 0,59 | -0,29R | €-39,99 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | ALT_ROTATION_UP | 2 | 6 | 6 | 33,33% | 0,90 | -0,07R | €-4,50 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | RANGE | 0 | 3 | 3 | 33,33% | 0,96 | -0,03R | €-0,85 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TRANSITION | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TREND_DOWN | 1 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,25 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TREND_UP | 1 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,58 |
| Rapida 1H V1 | ALT_ROTATION_DOWN | 0 | 22 | 22 | 22,73% | 0,43 | -0,42R | €-91,69 |
| Rapida 1H V1 | ALT_ROTATION_UP | 0 | 13 | 13 | 53,85% | 1,58 | 0,29R | €37,18 |
| Rapida 1H V1 | RANGE | 1 | 66 | 66 | 43,94% | 1,16 | 0,09R | €57,00 |
| Rapida 1H V1 | RANGE_HIGH_VOL | 0 | 11 | 11 | 0,00% | 0,00 | -1,09R | €-119,90 |
| Rapida 1H V1 | TRANSITION | 0 | 26 | 26 | 50,00% | 1,57 | 0,27R | €68,95 |
| Rapida 1H V1 | TREND_UP | 0 | 48 | 48 | 41,67% | 0,97 | -0,02R | €-9,20 |
| Rapida 1H V1 | TREND_UP_HIGH_VOL | 0 | 21 | 21 | 28,57% | 0,59 | -0,28R | €-58,55 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | ALT_ROTATION_DOWN | 0 | 5 | 5 | 0,00% | 0,00 | -0,83R | €-41,38 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | ALT_ROTATION_UP | 0 | 7 | 7 | 42,86% | 0,95 | -0,03R | €-2,21 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | RANGE | 0 | 6 | 6 | 83,33% | 7,11 | 1,06R | €63,32 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 1,48R | €29,69 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TREND_UP | 0 | 5 | 5 | 40,00% | 0,89 | -0,07R | €-3,68 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,36R | €13,57 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | ALT_ROTATION_UP | 1 | 14 | 14 | 42,86% | 1,00 | -0,00R | €-0,22 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | RANGE | 1 | 4 | 4 | 50,00% | 1,41 | 0,21R | €8,41 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 100,00% | ∞ | 1,47R | €44,18 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | TREND_UP | 1 | 4 | 4 | 50,00% | 1,28 | 0,15R | €6,17 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | ALT_ROTATION_DOWN | 0 | 18 | 18 | 22,22% | 0,40 | -0,46R | €-82,22 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | ALT_ROTATION_UP | 1 | 15 | 15 | 46,67% | 1,16 | 0,09R | €13,67 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | RANGE | 2 | 33 | 33 | 57,58% | 2,05 | 0,42R | €138,84 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 100,00% | ∞ | 1,47R | €44,18 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 1,48R | €29,69 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TREND_UP | 1 | 20 | 20 | 30,00% | 0,56 | -0,33R | €-66,04 |
| SHADOW_1H_FAST_NO_PEPE_V1 | ALT_ROTATION_DOWN | 1 | 21 | 21 | 19,05% | 0,35 | -0,50R | €-105,26 |
| SHADOW_1H_FAST_NO_PEPE_V1 | ALT_ROTATION_UP | 0 | 15 | 15 | 40,00% | 0,86 | -0,09R | €-13,18 |
| SHADOW_1H_FAST_NO_PEPE_V1 | RANGE | 2 | 34 | 34 | 52,94% | 1,59 | 0,28R | €95,12 |
| SHADOW_1H_FAST_NO_PEPE_V1 | RANGE_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_1H_FAST_NO_PEPE_V1 | RANGE_LOW_VOL | 1 | 2 | 2 | 100,00% | ∞ | 1,47R | €29,42 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TRANSITION | 2 | 4 | 4 | 75,00% | 3,90 | 0,83R | €33,12 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_DOWN | 1 | 2 | 2 | 0,00% | 0,00 | -1,02R | €-20,41 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_UP | 1 | 20 | 20 | 25,00% | 0,45 | -0,44R | €-87,18 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,36R | €13,57 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | ALT_ROTATION_DOWN | 1 | 12 | 12 | 33,33% | 0,65 | -0,25R | €-30,18 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | ALT_ROTATION_UP | 1 | 17 | 17 | 41,18% | 0,92 | -0,05R | €-8,25 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | RANGE | 1 | 26 | 26 | 57,69% | 1,99 | 0,41R | €107,14 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | RANGE_LOW_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,48R | €29,66 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TRANSITION | 1 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_UP | 1 | 10 | 10 | 20,00% | 0,32 | -0,58R | €-58,35 |
| SHADOW_1H_FAST_TP2_V1 | ALT_ROTATION_DOWN | 1 | 21 | 21 | 14,29% | 0,33 | -0,55R | €-115,33 |
| SHADOW_1H_FAST_TP2_V1 | ALT_ROTATION_UP | 0 | 17 | 17 | 41,18% | 1,23 | 0,15R | €24,85 |
| SHADOW_1H_FAST_TP2_V1 | RANGE | 2 | 28 | 28 | 46,43% | 1,50 | 0,28R | €79,75 |
| SHADOW_1H_FAST_TP2_V1 | RANGE_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_1H_FAST_TP2_V1 | RANGE_LOW_VOL | 1 | 2 | 2 | 50,00% | 1,93 | 0,47R | €9,39 |
| SHADOW_1H_FAST_TP2_V1 | TRANSITION | 2 | 4 | 4 | 75,00% | 5,14 | 1,18R | €47,21 |
| SHADOW_1H_FAST_TP2_V1 | TREND_DOWN | 1 | 2 | 2 | 0,00% | 0,00 | -1,02R | €-20,41 |
| SHADOW_1H_FAST_TP2_V1 | TREND_UP | 1 | 20 | 20 | 15,00% | 0,32 | -0,62R | €-123,95 |
| SHADOW_1H_FAST_TP2_V1 | TREND_UP_HIGH_VOL | 1 | 1 | 1 | 0,00% | 0,00 | -1,14R | €-11,43 |
| Rapida 1H V2 | ALT_ROTATION_UP | 0 | 4 | 4 | 25,00% | 0,41 | -0,49R | €-19,77 |
| Rapida 1H V2 | RANGE | 1 | 11 | 9 | 36,36% | 0,84 | -0,10R | €-10,86 |
| Rapida 1H V2 | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -1,14R | €-11,43 |
| Rapida 1H V3 Filtered | ALT_ROTATION_DOWN | 2 | 22 | 22 | 27,27% | 0,52 | -0,35R | €-76,81 |
| Rapida 1H V3 Filtered | ALT_ROTATION_UP | 0 | 16 | 16 | 50,00% | 1,30 | 0,16R | €26,17 |
| Rapida 1H V3 Filtered | RANGE | 2 | 34 | 34 | 52,94% | 1,60 | 0,28R | €96,81 |
| Rapida 1H V3 Filtered | RANGE_HIGH_VOL | 1 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| Rapida 1H V3 Filtered | RANGE_LOW_VOL | 1 | 2 | 2 | 100,00% | ∞ | 1,47R | €29,42 |
| Rapida 1H V3 Filtered | TRANSITION | 1 | 7 | 7 | 57,14% | 1,83 | 0,38R | €26,94 |
| Rapida 1H V3 Filtered | TREND_DOWN | 1 | 2 | 2 | 0,00% | 0,00 | -1,02R | €-20,41 |
| Rapida 1H V3 Filtered | TREND_UP | 1 | 37 | 37 | 45,95% | 1,16 | 0,09R | €34,15 |
| Rapida 1H V3 Filtered | TREND_UP_HIGH_VOL | 0 | 20 | 20 | 25,00% | 0,49 | -0,36R | €-72,31 |
| SHADOW_1H_FAST_V3_CAP75_V1 | ALT_ROTATION_DOWN | 2 | 16 | 16 | 25,00% | 0,44 | -0,44R | €-70,78 |
| SHADOW_1H_FAST_V3_CAP75_V1 | ALT_ROTATION_UP | 1 | 17 | 17 | 41,18% | 0,91 | -0,06R | €-9,61 |
| SHADOW_1H_FAST_V3_CAP75_V1 | RANGE | 2 | 29 | 29 | 55,17% | 1,91 | 0,38R | €109,26 |
| SHADOW_1H_FAST_V3_CAP75_V1 | RANGE_LOW_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,48R | €29,66 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TRANSITION | 1 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_UP | 1 | 14 | 14 | 28,57% | 0,52 | -0,37R | €-51,13 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | ALT_ROTATION_DOWN | 0 | 6 | 6 | 0,00% | 0,00 | -1,04R | €-62,18 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | ALT_ROTATION_UP | 0 | 13 | 13 | 38,46% | 0,82 | -0,12R | €-15,65 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | RANGE | 1 | 15 | 15 | 60,00% | 2,16 | 0,48R | €71,81 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TREND_UP | 1 | 10 | 10 | 30,00% | 0,54 | -0,35R | €-35,06 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | ALT_ROTATION_DOWN | 0 | 6 | 6 | 0,00% | 0,00 | -1,04R | €-62,18 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | ALT_ROTATION_UP | 0 | 13 | 13 | 38,46% | 0,82 | -0,12R | €-15,65 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | RANGE | 1 | 15 | 15 | 60,00% | 2,16 | 0,48R | €71,81 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TREND_UP | 1 | 10 | 10 | 30,00% | 0,54 | -0,35R | €-35,06 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 0 | 8 | 8 | 0,00% | 0,00 | -1,03R | €-82,50 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | ALT_ROTATION_UP | 0 | 14 | 14 | 42,86% | 0,95 | -0,03R | €-4,05 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | RANGE | 1 | 19 | 19 | 57,89% | 1,99 | 0,42R | €80,74 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | RANGE_LOW_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,47R | €29,42 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 1,49R | €29,71 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,23 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_UP | 1 | 14 | 14 | 21,43% | 0,36 | -0,54R | €-75,21 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | ALT_ROTATION_DOWN | 0 | 21 | 21 | 28,57% | 0,56 | -0,31R | €-65,39 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | ALT_ROTATION_UP | 0 | 13 | 13 | 46,15% | 1,11 | 0,07R | €8,74 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | RANGE | 2 | 34 | 34 | 52,94% | 1,60 | 0,28R | €96,81 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | RANGE_LOW_VOL | 1 | 2 | 2 | 100,00% | ∞ | 1,47R | €29,42 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 1,49R | €29,71 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TREND_DOWN | 1 | 2 | 2 | 0,00% | 0,00 | -1,02R | €-20,41 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TREND_UP | 1 | 22 | 22 | 27,27% | 0,50 | -0,39R | €-85,90 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | ALT_ROTATION_DOWN | 2 | 21 | 21 | 28,57% | 0,56 | -0,31R | €-65,39 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | ALT_ROTATION_UP | 0 | 15 | 15 | 40,00% | 0,85 | -0,10R | €-14,95 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | RANGE | 1 | 33 | 33 | 51,52% | 1,51 | 0,25R | €81,94 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | RANGE_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | RANGE_LOW_VOL | 1 | 2 | 2 | 100,00% | ∞ | 1,47R | €29,42 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TRANSITION | 1 | 2 | 2 | 100,00% | ∞ | 1,49R | €29,71 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_DOWN | 1 | 2 | 2 | 0,00% | 0,00 | -1,02R | €-20,41 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_UP | 1 | 20 | 20 | 25,00% | 0,45 | -0,44R | €-88,59 |
| SHADOW_4H_WIDE | ALT_ROTATION_DOWN | 2 | 2 | 2 | 100,00% | ∞ | 2,79R | €55,73 |
| SHADOW_4H_WIDE | ALT_ROTATION_UP | 3 | 3 | 3 | 0,00% | 0,00 | -1,01R | €-30,40 |
| SHADOW_4H_WIDE | RANGE | 9 | 22 | 22 | 27,27% | 1,02 | 0,01R | €2,99 |
| SHADOW_4H_WIDE | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_4H_WIDE | TRANSITION | 3 | 7 | 7 | 14,29% | 0,46 | -0,47R | €-33,10 |
| SHADOW_4H_WIDE | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_4H_WIDE | TREND_UP | 3 | 15 | 15 | 40,00% | 1,81 | 0,50R | €74,71 |
| SHADOW_4H_WIDE | TREND_UP_HIGH_VOL | 4 | 4 | 4 | 0,00% | 0,00 | -1,01R | €-40,53 |
| SHADOW_BOLLINGER_MR_1H | ALT_ROTATION_DOWN | 0 | 5 | 5 | 60,00% | 1,99 | 0,43R | €21,52 |
| SHADOW_BOLLINGER_MR_1H | ALT_ROTATION_UP | 0 | 8 | 8 | 37,50% | 0,79 | -0,14R | €-11,49 |
| SHADOW_BOLLINGER_MR_1H | RANGE | 1 | 20 | 20 | 45,00% | 1,14 | 0,08R | €16,00 |
| SHADOW_BOLLINGER_MR_1H | RANGE_HIGH_VOL | 1 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_BOLLINGER_MR_1H | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_BOLLINGER_MR_1H | TRANSITION | 0 | 3 | 3 | 33,33% | 0,71 | -0,20R | €-6,14 |
| SHADOW_BOLLINGER_MR_1H | TREND_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 1,48R | €14,79 |
| SHADOW_BOLLINGER_MR_1H | TREND_UP | 1 | 15 | 15 | 60,00% | 1,92 | 0,41R | €61,11 |
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
| SHADOW_COMBO_ADAPTIVE | ALT_ROTATION_DOWN | 4 | 12 | 12 | 25,00% | 0,60 | -0,31R | €-37,55 |
| SHADOW_COMBO_ADAPTIVE | ALT_ROTATION_UP | 2 | 12 | 12 | 33,33% | 0,90 | -0,07R | €-8,33 |
| SHADOW_COMBO_ADAPTIVE | RANGE | 3 | 41 | 41 | 41,46% | 1,29 | 0,18R | €74,57 |
| SHADOW_COMBO_ADAPTIVE | RANGE_HIGH_VOL | 1 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,83 |
| SHADOW_COMBO_ADAPTIVE | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE | TRANSITION | 2 | 20 | 20 | 45,00% | 1,65 | 0,34R | €68,99 |
| SHADOW_COMBO_ADAPTIVE | TREND_DOWN | 2 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_COMBO_ADAPTIVE | TREND_UP | 2 | 34 | 34 | 41,18% | 1,38 | 0,22R | €75,95 |
| SHADOW_COMBO_ADAPTIVE | TREND_UP_HIGH_VOL | 0 | 12 | 12 | 16,67% | 0,40 | -0,48R | €-57,73 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 1 | 4 | 4 | 0,00% | 0,00 | -1,01R | €-40,55 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | ALT_ROTATION_UP | 1 | 10 | 10 | 40,00% | 1,18 | 0,12R | €11,78 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | RANGE | 1 | 14 | 14 | 57,14% | 2,60 | 0,70R | €97,53 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_UP | 2 | 10 | 10 | 0,00% | 0,00 | -0,96R | €-96,15 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_UP_HIGH_VOL | 0 | 6 | 6 | 16,67% | 0,36 | -0,56R | €-33,65 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | ALT_ROTATION_DOWN | 4 | 12 | 12 | 25,00% | 0,60 | -0,31R | €-37,55 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | ALT_ROTATION_UP | 2 | 13 | 13 | 30,77% | 0,80 | -0,15R | €-19,44 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE | 3 | 29 | 29 | 48,28% | 1,71 | 0,39R | €113,05 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE_HIGH_VOL | 1 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,83 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TRANSITION | 2 | 4 | 4 | 50,00% | 1,78 | 0,43R | €17,13 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_DOWN | 2 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_UP | 2 | 26 | 26 | 38,46% | 1,26 | 0,16R | €41,06 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_UP_HIGH_VOL | 0 | 14 | 14 | 14,29% | 0,33 | -0,57R | €-79,79 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | ALT_ROTATION_DOWN | 4 | 12 | 12 | 25,00% | 0,60 | -0,31R | €-37,55 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | ALT_ROTATION_UP | 2 | 10 | 10 | 40,00% | 1,18 | 0,12R | €11,78 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | RANGE | 3 | 29 | 29 | 48,28% | 1,71 | 0,39R | €113,05 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | RANGE_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TRANSITION | 2 | 3 | 3 | 33,33% | 0,91 | -0,07R | €-1,99 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_DOWN | 2 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_UP | 2 | 13 | 13 | 7,69% | 0,17 | -0,74R | €-96,62 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_UP_HIGH_VOL | 0 | 7 | 7 | 14,29% | 0,30 | -0,64R | €-44,76 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TRANSITION | 0 | 3 | 3 | 33,33% | 0,92 | -0,06R | €-1,72 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TREND_UP | 3 | 5 | 5 | 20,00% | 0,48 | -0,44R | €-21,83 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TRANSITION | 0 | 3 | 3 | 33,33% | 0,92 | -0,06R | €-1,72 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TREND_UP | 3 | 5 | 5 | 20,00% | 0,48 | -0,44R | €-21,83 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | ALT_ROTATION_DOWN | 1 | 2 | 2 | 0,00% | 0,00 | -1,10R | €-21,95 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | ALT_ROTATION_UP | 1 | 2 | 2 | 0,00% | 0,00 | -1,03R | €-20,65 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | RANGE | 2 | 12 | 12 | 66,67% | 3,84 | 0,98R | €117,20 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TRANSITION | 0 | 2 | 2 | 50,00% | 1,90 | 0,46R | €9,15 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_UP | 1 | 3 | 3 | 0,00% | 0,00 | -1,04R | €-31,32 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TRANSITION | 2 | 8 | 8 | 25,00% | 0,60 | -0,32R | €-25,89 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TREND_UP | 3 | 22 | 22 | 18,18% | 0,43 | -0,46R | €-102,00 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TREND_UP_HIGH_VOL | 0 | 8 | 8 | 12,50% | 0,26 | -0,70R | €-55,87 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_DOWN | 3 | 7 | 7 | 28,57% | 1,07 | 0,05R | €3,83 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_UP | 0 | 5 | 5 | 40,00% | 1,80 | 0,52R | €26,25 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | RANGE | 2 | 15 | 15 | 20,00% | 0,69 | -0,26R | €-39,51 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | TRANSITION | 0 | 2 | 2 | 0,00% | 0,00 | -1,09R | €-21,86 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | TREND_UP | 1 | 8 | 8 | 0,00% | 0,00 | -0,93R | €-74,60 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 0,00% | 0,00 | -1,06R | €-42,49 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | ALT_ROTATION_DOWN | 3 | 7 | 7 | 28,57% | 1,07 | 0,05R | €3,83 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | ALT_ROTATION_UP | 0 | 5 | 5 | 40,00% | 1,80 | 0,52R | €26,25 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | RANGE | 2 | 15 | 15 | 20,00% | 0,69 | -0,26R | €-39,51 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | TRANSITION | 0 | 2 | 2 | 0,00% | 0,00 | -1,09R | €-21,86 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | TREND_UP | 1 | 8 | 8 | 0,00% | 0,00 | -0,93R | €-74,60 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 0,00% | 0,00 | -1,06R | €-42,49 |
| SHADOW_COMBO_MEAN_REVERSION | ALT_ROTATION_DOWN | 0 | 4 | 4 | 25,00% | 0,69 | -0,18R | €-7,17 |
| SHADOW_COMBO_MEAN_REVERSION | RANGE | 0 | 11 | 11 | 45,45% | 1,15 | 0,09R | €9,62 |
| SHADOW_COMBO_MEAN_REVERSION | TRANSITION | 1 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,94 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_UP | 0 | 4 | 4 | 50,00% | 1,53 | 0,27R | €10,70 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,85 |
| SHADOW_COMBO_SCANNER | ALT_ROTATION_DOWN | 1 | 5 | 5 | 0,00% | 0,00 | -1,03R | €-51,66 |
| SHADOW_COMBO_SCANNER | ALT_ROTATION_UP | 1 | 8 | 8 | 37,50% | 1,23 | 0,15R | €11,95 |
| SHADOW_COMBO_SCANNER | RANGE | 1 | 18 | 18 | 55,56% | 2,63 | 0,74R | €133,95 |
| SHADOW_COMBO_SCANNER | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,69 |
| SHADOW_COMBO_SCANNER | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_SCANNER | TRANSITION | 1 | 15 | 15 | 46,67% | 1,60 | 0,34R | €50,68 |
| SHADOW_COMBO_SCANNER | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_COMBO_SCANNER | TREND_UP | 2 | 25 | 25 | 40,00% | 1,46 | 0,27R | €68,62 |
| SHADOW_COMBO_SCANNER | TREND_UP_HIGH_VOL | 0 | 9 | 9 | 33,33% | 1,18 | 0,11R | €9,88 |
| SHADOW_COMBO_TREND | ALT_ROTATION_DOWN | 4 | 9 | 9 | 22,22% | 0,57 | -0,35R | €-31,72 |
| SHADOW_COMBO_TREND | ALT_ROTATION_UP | 2 | 11 | 11 | 27,27% | 0,76 | -0,19R | €-20,35 |
| SHADOW_COMBO_TREND | RANGE | 3 | 31 | 31 | 38,71% | 1,29 | 0,19R | €58,86 |
| SHADOW_COMBO_TREND | RANGE_HIGH_VOL | 1 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,63 |
| SHADOW_COMBO_TREND | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_TREND | TRANSITION | 2 | 16 | 16 | 43,75% | 1,79 | 0,42R | €67,09 |
| SHADOW_COMBO_TREND | TREND_DOWN | 2 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,16 |
| SHADOW_COMBO_TREND | TREND_UP | 3 | 26 | 26 | 30,77% | 0,92 | -0,06R | €-14,96 |
| SHADOW_COMBO_TREND | TREND_UP_HIGH_VOL | 0 | 11 | 11 | 18,18% | 0,50 | -0,38R | €-42,23 |
| SHADOW_DOGE_BOLLINGER_1H | RANGE | 0 | 2 | 2 | 0,00% | 0,00 | -1,12R | €-22,46 |
| SHADOW_DOGE_DONCHIAN_1H | RANGE | 0 | 3 | 3 | 33,33% | 0,84 | -0,12R | €-3,55 |
| SHADOW_DOGE_DONCHIAN_1H | TRANSITION | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_DOGE_EMA_1H | RANGE | 0 | 4 | 4 | 50,00% | 1,71 | 0,39R | €15,73 |
| SHADOW_DONCHIAN_1H | ALT_ROTATION_DOWN | 3 | 9 | 9 | 22,22% | 0,65 | -0,29R | €-25,72 |
| SHADOW_DONCHIAN_1H | ALT_ROTATION_UP | 0 | 8 | 8 | 12,50% | 0,32 | -0,63R | €-50,42 |
| SHADOW_DONCHIAN_1H | RANGE | 1 | 20 | 20 | 30,00% | 0,99 | -0,01R | €-2,06 |
| SHADOW_DONCHIAN_1H | RANGE_HIGH_VOL | 1 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_DONCHIAN_1H | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_DONCHIAN_1H | TRANSITION | 3 | 7 | 7 | 14,29% | 0,45 | -0,42R | €-29,27 |
| SHADOW_DONCHIAN_1H | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,16 |
| SHADOW_DONCHIAN_1H | TREND_UP | 0 | 14 | 14 | 35,71% | 1,28 | 0,19R | €26,97 |
| SHADOW_DONCHIAN_1H | TREND_UP_HIGH_VOL | 1 | 5 | 5 | 40,00% | 1,48 | 0,31R | €15,65 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | RANGE_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | TRANSITION | 3 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_EMA_TREND_1H | ALT_ROTATION_DOWN | 3 | 9 | 9 | 22,22% | 0,57 | -0,35R | €-31,52 |
| SHADOW_EMA_TREND_1H | ALT_ROTATION_UP | 2 | 11 | 11 | 18,18% | 0,45 | -0,48R | €-52,68 |
| SHADOW_EMA_TREND_1H | RANGE | 4 | 29 | 29 | 41,38% | 1,54 | 0,31R | €91,14 |
| SHADOW_EMA_TREND_1H | RANGE_HIGH_VOL | 1 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,63 |
| SHADOW_EMA_TREND_1H | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_EMA_TREND_1H | TRANSITION | 0 | 17 | 17 | 41,18% | 1,59 | 0,33R | €56,40 |
| SHADOW_EMA_TREND_1H | TREND_DOWN | 2 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,16 |
| SHADOW_EMA_TREND_1H | TREND_UP | 3 | 31 | 31 | 29,03% | 0,88 | -0,08R | €-25,79 |
| SHADOW_EMA_TREND_1H | TREND_UP_HIGH_VOL | 0 | 11 | 11 | 27,27% | 0,87 | -0,09R | €-9,90 |
| SHADOW_ETH_ADAPTIVE_1H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 0,00% | 0,00 | -1,11R | €-22,22 |
| SHADOW_ETH_ADAPTIVE_1H | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_ETH_ADAPTIVE_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_ETH_ADAPTIVE_1H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,89R | €18,89 |
| SHADOW_ETH_ADAPTIVE_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_ETH_BOLLINGER_1H | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,37R | €13,67 |
| SHADOW_ETH_BOLLINGER_1H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,33 |
| SHADOW_ETH_DONCHIAN_1H | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_ETH_DONCHIAN_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,12R | €-11,25 |
| SHADOW_ETH_DONCHIAN_1H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_ETH_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,68 | 0,38R | €7,64 |
| SHADOW_ETH_EMA_1H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 0,00% | 0,00 | -1,11R | €-22,22 |
| SHADOW_ETH_EMA_1H | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_ETH_EMA_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_ETH_EMA_1H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,89R | €18,89 |
| SHADOW_ETH_EMA_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,10R | €-10,99 |
| SHADOW_ETH_EMA_4H | ALT_ROTATION_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_ETH_EMA_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,57 |
| SHADOW_GLOBAL_PURE | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,10R | €-11,00 |
| SHADOW_GLOBAL_PURE | RANGE | 0 | 2 | 2 | 50,00% | 2,21 | 0,66R | €13,16 |
| SHADOW_GLOBAL_PURE | TRANSITION | 1 | 1 | 1 | 100,00% | ∞ | 1,42R | €14,17 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | ALT_ROTATION_DOWN | 1 | 7 | 7 | 14,29% | 0,32 | -0,60R | €-41,93 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | ALT_ROTATION_UP | 0 | 5 | 5 | 20,00% | 0,46 | -0,46R | €-23,01 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | RANGE | 2 | 11 | 11 | 54,55% | 2,33 | 0,62R | €67,93 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TRANSITION | 0 | 3 | 3 | 100,00% | ∞ | 1,96R | €58,74 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TREND_DOWN | 1 | 2 | 2 | 50,00% | 1,86 | 0,44R | €8,71 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TREND_UP | 3 | 16 | 16 | 6,25% | 0,13 | -0,82R | €-130,62 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | ALT_ROTATION_DOWN | 1 | 6 | 6 | 16,67% | 0,39 | -0,51R | €-30,82 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | ALT_ROTATION_UP | 0 | 6 | 6 | 33,33% | 0,90 | -0,07R | €-4,19 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | RANGE | 2 | 12 | 12 | 58,33% | 2,72 | 0,73R | €87,79 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TREND_UP | 3 | 18 | 18 | 5,56% | 0,12 | -0,84R | €-151,86 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | ALT_ROTATION_DOWN | 1 | 6 | 6 | 16,67% | 0,39 | -0,51R | €-30,82 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | RANGE | 2 | 12 | 12 | 58,33% | 2,72 | 0,73R | €87,79 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | RANGE_LOW_VOL | 0 | 2 | 2 | 50,00% | 1,86 | 0,44R | €8,76 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TREND_UP | 3 | 18 | 18 | 5,56% | 0,12 | -0,84R | €-151,96 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_DOWN | 1 | 1 | 1 | 100,00% | ∞ | 2,99R | €29,87 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_UP | 2 | 4 | 4 | 0,00% | 0,00 | -1,06R | €-42,57 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | RANGE | 2 | 12 | 12 | 41,67% | 2,09 | 0,65R | €77,79 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | TREND_UP | 2 | 16 | 16 | 6,25% | 0,20 | -0,75R | €-120,13 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | ALT_ROTATION_DOWN | 0 | 4 | 4 | 0,00% | 0,00 | -1,01R | €-40,55 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | RANGE | 1 | 15 | 15 | 60,00% | 2,92 | 0,78R | €117,44 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TREND_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TREND_UP | 4 | 13 | 13 | 0,00% | 0,00 | -1,07R | €-138,81 |
| SHADOW_MASTER_ADAPTIVE_V1 | ALT_ROTATION_DOWN | 1 | 6 | 6 | 16,67% | 0,39 | -0,51R | €-30,82 |
| SHADOW_MASTER_ADAPTIVE_V1 | ALT_ROTATION_UP | 0 | 6 | 6 | 33,33% | 0,90 | -0,07R | €-4,19 |
| SHADOW_MASTER_ADAPTIVE_V1 | RANGE | 2 | 12 | 12 | 58,33% | 2,72 | 0,73R | €87,79 |
| SHADOW_MASTER_ADAPTIVE_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| SHADOW_MASTER_ADAPTIVE_V1 | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_MASTER_ADAPTIVE_V1 | TREND_UP | 3 | 18 | 18 | 5,56% | 0,12 | -0,84R | €-151,86 |
| Forza relativa 1H V1 | ALT_ROTATION_DOWN | 5 | 9 | 9 | 11,11% | 0,26 | -0,69R | €-61,85 |
| Forza relativa 1H V1 | ALT_ROTATION_UP | 2 | 18 | 18 | 27,78% | 0,78 | -0,17R | €-30,25 |
| Forza relativa 1H V1 | RANGE | 5 | 39 | 39 | 33,33% | 1,07 | 0,05R | €18,42 |
| Forza relativa 1H V1 | RANGE_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -1,03R | €-31,02 |
| Forza relativa 1H V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| Forza relativa 1H V1 | TRANSITION | 1 | 16 | 16 | 50,00% | 2,11 | 0,57R | €91,12 |
| Forza relativa 1H V1 | TREND_DOWN | 2 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| Forza relativa 1H V1 | TREND_UP | 3 | 40 | 40 | 35,00% | 1,27 | 0,16R | €64,94 |
| Forza relativa 1H V1 | TREND_UP_HIGH_VOL | 0 | 9 | 9 | 11,11% | 0,26 | -0,68R | €-61,28 |
| Forza relativa 1H V2 | ALT_ROTATION_DOWN | 1 | 6 | 6 | 50,00% | 2,02 | 0,53R | €32,04 |
| Forza relativa 1H V2 | ALT_ROTATION_UP | 2 | 7 | 6 | 28,57% | 0,82 | -0,13R | €-9,32 |
| Forza relativa 1H V2 | RANGE | 1 | 13 | 13 | 61,54% | 3,40 | 0,95R | €123,51 |
| Forza relativa 1H V2 | RANGE_LOW_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| Forza relativa 1H V2 | TRANSITION | 0 | 13 | 11 | 38,46% | 1,31 | 0,20R | €25,87 |
| Forza relativa 1H V2 | TREND_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| Forza relativa 1H V2 | TREND_UP | 1 | 13 | 12 | 38,46% | 1,33 | 0,21R | €27,33 |
| Forza relativa 1H V2 | TREND_UP_HIGH_VOL | 0 | 4 | 3 | 0,00% | 0,00 | -1,04R | €-41,60 |
| SHADOW_SCANNER_BOTTOM10_SHORT | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM10_SHORT | ALT_ROTATION_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM10_SHORT | RANGE | 2 | 6 | 6 | 0,00% | 0,00 | -1,11R | €-66,45 |
| SHADOW_SCANNER_BOTTOM10_SHORT | RANGE_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TRANSITION | 3 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM15_SHORT | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM15_SHORT | ALT_ROTATION_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM15_SHORT | RANGE | 2 | 6 | 6 | 0,00% | 0,00 | -1,11R | €-66,45 |
| SHADOW_SCANNER_BOTTOM15_SHORT | RANGE_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TRANSITION | 3 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM20_SHORT | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM20_SHORT | ALT_ROTATION_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM20_SHORT | RANGE | 2 | 6 | 6 | 0,00% | 0,00 | -1,11R | €-66,45 |
| SHADOW_SCANNER_BOTTOM20_SHORT | RANGE_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TRANSITION | 3 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM5_SHORT | ALT_ROTATION_DOWN | 2 | 5 | 5 | 60,00% | 2,62 | 0,71R | €35,50 |
| SHADOW_SCANNER_BOTTOM5_SHORT | ALT_ROTATION_UP | 1 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| SHADOW_SCANNER_BOTTOM5_SHORT | RANGE | 3 | 20 | 20 | 30,00% | 0,75 | -0,19R | €-37,65 |
| SHADOW_SCANNER_BOTTOM5_SHORT | RANGE_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TRANSITION | 3 | 14 | 14 | 28,57% | 0,85 | -0,09R | €-13,14 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP | 0 | 7 | 7 | 0,00% | 0,00 | -0,73R | €-51,04 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -0,71R | €-21,38 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | ALT_ROTATION_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | RANGE_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TRANSITION | 3 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_DOWN | 2 | 2 | 2 | 0,00% | 0,00 | -1,10R | €-22,10 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | ALT_ROTATION_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | RANGE_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TRANSITION | 3 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_DOWN | 2 | 2 | 2 | 0,00% | 0,00 | -1,10R | €-22,10 |
| SHADOW_SCANNER_TOP10_LONG | ALT_ROTATION_UP | 1 | 5 | 5 | 20,00% | 0,44 | -0,48R | €-23,97 |
| SHADOW_SCANNER_TOP10_LONG | RANGE | 0 | 6 | 6 | 83,33% | 9,62 | 1,48R | €88,62 |
| SHADOW_SCANNER_TOP10_LONG | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP10_LONG | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_SCANNER_TOP10_LONG | TREND_UP | 1 | 3 | 3 | 0,00% | 0,00 | -1,01R | €-30,40 |
| SHADOW_SCANNER_TOP15_LONG | ALT_ROTATION_UP | 1 | 6 | 6 | 16,67% | 0,35 | -0,58R | €-35,08 |
| SHADOW_SCANNER_TOP15_LONG | RANGE | 0 | 6 | 6 | 83,33% | 9,62 | 1,48R | €88,62 |
| SHADOW_SCANNER_TOP15_LONG | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP15_LONG | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_SCANNER_TOP15_LONG | TREND_UP | 1 | 3 | 3 | 0,00% | 0,00 | -1,01R | €-30,40 |
| SHADOW_SCANNER_TOP20_LONG | ALT_ROTATION_UP | 1 | 6 | 6 | 16,67% | 0,35 | -0,58R | €-35,08 |
| SHADOW_SCANNER_TOP20_LONG | RANGE | 0 | 6 | 6 | 83,33% | 9,62 | 1,48R | €88,62 |
| SHADOW_SCANNER_TOP20_LONG | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP20_LONG | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_SCANNER_TOP20_LONG | TREND_UP | 1 | 3 | 3 | 0,00% | 0,00 | -1,01R | €-30,40 |
| SHADOW_SCANNER_TOP5_BTC | ALT_ROTATION_DOWN | 1 | 5 | 5 | 0,00% | 0,00 | -1,03R | €-51,66 |
| SHADOW_SCANNER_TOP5_BTC | ALT_ROTATION_UP | 1 | 9 | 9 | 33,33% | 1,02 | 0,02R | €1,43 |
| SHADOW_SCANNER_TOP5_BTC | RANGE | 1 | 18 | 18 | 55,56% | 3,01 | 0,80R | €144,90 |
| SHADOW_SCANNER_TOP5_BTC | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,69 |
| SHADOW_SCANNER_TOP5_BTC | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC | TRANSITION | 0 | 13 | 13 | 46,15% | 1,79 | 0,45R | €58,04 |
| SHADOW_SCANNER_TOP5_BTC | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_SCANNER_TOP5_BTC | TREND_UP | 2 | 24 | 24 | 37,50% | 1,32 | 0,20R | €47,91 |
| SHADOW_SCANNER_TOP5_BTC | TREND_UP_HIGH_VOL | 0 | 9 | 9 | 33,33% | 1,18 | 0,11R | €9,88 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | ALT_ROTATION_DOWN | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | ALT_ROTATION_UP | 1 | 3 | 3 | 0,00% | 0,00 | -1,08R | €-32,30 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TRANSITION | 0 | 3 | 3 | 66,67% | 4,32 | 1,12R | €33,60 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TREND_UP | 2 | 6 | 6 | 33,33% | 1,03 | 0,02R | €1,17 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TREND_UP_HIGH_VOL | 0 | 6 | 6 | 16,67% | 0,40 | -0,53R | €-31,93 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | ALT_ROTATION_DOWN | 2 | 4 | 4 | 0,00% | 0,00 | -1,01R | €-40,55 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | ALT_ROTATION_UP | 1 | 5 | 5 | 20,00% | 0,49 | -0,43R | €-21,72 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | RANGE | 1 | 13 | 13 | 53,85% | 2,50 | 0,71R | €91,66 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 2,19R | €43,73 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_UP | 2 | 5 | 5 | 20,00% | 0,51 | -0,41R | €-20,62 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_UP_HIGH_VOL | 0 | 6 | 6 | 16,67% | 0,40 | -0,53R | €-31,93 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | ALT_ROTATION_DOWN | 2 | 4 | 4 | 0,00% | 0,00 | -1,01R | €-40,55 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | ALT_ROTATION_UP | 0 | 4 | 4 | 25,00% | 0,66 | -0,27R | €-10,99 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | RANGE | 1 | 13 | 13 | 53,85% | 2,50 | 0,71R | €91,66 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 2,19R | €43,73 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_UP | 1 | 4 | 4 | 25,00% | 0,71 | -0,23R | €-9,04 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | ALT_ROTATION_DOWN | 2 | 4 | 4 | 0,00% | 0,00 | -1,01R | €-40,55 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | ALT_ROTATION_UP | 0 | 4 | 4 | 25,00% | 0,66 | -0,27R | €-10,99 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | RANGE | 1 | 13 | 13 | 53,85% | 2,50 | 0,71R | €91,66 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 2,19R | €43,73 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_UP | 1 | 4 | 4 | 25,00% | 0,71 | -0,23R | €-9,04 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | ALT_ROTATION_DOWN | 1 | 5 | 5 | 0,00% | 0,00 | -1,03R | €-51,66 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | ALT_ROTATION_UP | 0 | 4 | 4 | 25,00% | 0,66 | -0,27R | €-10,99 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | RANGE | 1 | 13 | 13 | 53,85% | 2,50 | 0,71R | €91,66 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 2,19R | €43,73 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_UP | 1 | 8 | 8 | 12,50% | 0,35 | -0,51R | €-41,14 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | ALT_ROTATION_DOWN | 1 | 5 | 5 | 0,00% | 0,00 | -1,03R | €-51,66 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | ALT_ROTATION_UP | 0 | 4 | 4 | 25,00% | 0,66 | -0,27R | €-10,99 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | RANGE | 1 | 13 | 13 | 53,85% | 2,50 | 0,71R | €91,66 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 2,19R | €43,73 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_UP | 1 | 8 | 8 | 12,50% | 0,35 | -0,51R | €-41,14 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | ALT_ROTATION_DOWN | 1 | 5 | 5 | 0,00% | 0,00 | -1,03R | €-51,66 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | ALT_ROTATION_UP | 1 | 5 | 5 | 20,00% | 0,49 | -0,43R | €-21,65 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | RANGE | 1 | 13 | 13 | 53,85% | 2,50 | 0,71R | €91,66 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 2,19R | €43,73 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_UP | 2 | 7 | 7 | 14,29% | 0,41 | -0,45R | €-31,25 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 9 | 9 | 22,22% | 0,65 | -0,25R | €-22,73 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | ALT_ROTATION_UP | 2 | 8 | 8 | 25,00% | 0,90 | -0,08R | €-6,44 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | RANGE | 2 | 10 | 10 | 50,00% | 2,93 | 0,98R | €98,19 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 2,99R | €29,87 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_UP | 2 | 9 | 9 | 11,11% | 0,40 | -0,50R | €-44,70 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -1,05R | €-31,38 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | ALT_ROTATION_UP | 2 | 8 | 8 | 25,00% | 0,90 | -0,08R | €-6,44 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | RANGE | 2 | 10 | 10 | 50,00% | 2,93 | 0,98R | €98,19 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 2,99R | €29,87 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_UP | 2 | 9 | 9 | 11,11% | 0,40 | -0,50R | €-44,70 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -1,05R | €-31,38 |
| SHADOW_SCANNER_TOP5_LONG | ALT_ROTATION_DOWN | 0 | 7 | 7 | 0,00% | 0,00 | -0,90R | €-62,91 |
| SHADOW_SCANNER_TOP5_LONG | ALT_ROTATION_UP | 1 | 10 | 10 | 30,00% | 0,78 | -0,16R | €-16,17 |
| SHADOW_SCANNER_TOP5_LONG | RANGE | 1 | 19 | 19 | 57,89% | 3,01 | 0,76R | €144,76 |
| SHADOW_SCANNER_TOP5_LONG | RANGE_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,83 |
| SHADOW_SCANNER_TOP5_LONG | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_LONG | TRANSITION | 0 | 13 | 13 | 46,15% | 1,63 | 0,35R | €46,04 |
| SHADOW_SCANNER_TOP5_LONG | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_SCANNER_TOP5_LONG | TREND_UP | 1 | 34 | 34 | 41,18% | 1,43 | 0,24R | €82,93 |
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
| SHADOW_SOL_EMA_4H | ALT_ROTATION_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,55 |
| SHADOW_SOL_EMA_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,56 |

Il P&L è normalizzato a **€10 di rischio per evento**, così leva e size non falsano il confronto.
La matrice diventerà utilizzabile per una rotazione automatica soltanto dopo un campione sufficiente per ciascuna coppia strategia-regime.

# Block 3 — Shadow Exit Engine

Generato: 2026-07-27T18:23:49+00:00

> Motore esclusivamente osservativo e Paper-only. Non modifica le uscite reali. I confronti escludono il funding sia dall'uscita originale sia dalle varianti.

## Stato operativo

- Gruppi di trade ancora monitorati: **732**
- Scenari virtuali ancora attivi: **11748**
- Gruppi in attesa dell'uscita originale: **342**
- Gruppi con originale chiuso ma Shadow ancora attive: **390**
- Confronti completati: **73018**

## Classifica osservativa complessiva

| Scenario | Campione completo | Campione totale | Δ medio vs originale | Migliora | Troppo presto | Troppo tardi | Stato dati |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| GB20_R050 | 2245 | 2310 | +€7,08 | 48,9% | 680 | 2 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R050 | 2245 | 2310 | +€5,25 | 47,2% | 696 | 17 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R050 | 2245 | 2310 | +€3,09 | 46,0% | 707 | 39 | READY_FOR_BLOCK4_EVALUATION |
| TP_R050 | 2245 | 2310 | +€2,29 | 45,3% | 768 | 1 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R050 | 2244 | 2309 | +€1,58 | 45,5% | 670 | 89 | READY_FOR_BLOCK4_EVALUATION |
| TIME_6H | 2240 | 2305 | €-4,09 | 42,5% | 492 | 416 | READY_FOR_BLOCK4_EVALUATION |
| GB20_R100 | 2224 | 2289 | +€4,44 | 43,0% | 549 | 67 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R100 | 2224 | 2289 | +€2,55 | 42,2% | 539 | 95 | READY_FOR_BLOCK4_EVALUATION |
| TP_R100 | 2224 | 2289 | +€1,79 | 40,1% | 619 | 65 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R100 | 2224 | 2289 | +€1,31 | 42,5% | 452 | 158 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R100 | 2222 | 2287 | €-0,28 | 39,9% | 381 | 299 | READY_FOR_BLOCK4_EVALUATION |
| ATR15_R100 | 2206 | 2271 | €-3,46 | 31,1% | 282 | 505 | READY_FOR_BLOCK4_EVALUATION |
| TIME_12H | 2204 | 2269 | €-4,35 | 37,4% | 288 | 579 | READY_FOR_BLOCK4_EVALUATION |
| ATR20_R100 | 2190 | 2255 | €-4,67 | 28,4% | 253 | 576 | READY_FOR_BLOCK4_EVALUATION |
| TIME_24H | 2167 | 2232 | €-5,81 | 32,5% | 160 | 668 | READY_FOR_BLOCK4_EVALUATION |
| TP_R150 | 2157 | 2222 | +€3,01 | 31,7% | 315 | 230 | READY_FOR_BLOCK4_EVALUATION |
| ATR30_R100 | 2152 | 2217 | €-10,12 | 26,3% | 206 | 620 | READY_FOR_BLOCK4_EVALUATION |
| BE_R050 | 2127 | 2192 | €-10,75 | 29,0% | 448 | 443 | READY_FOR_BLOCK4_EVALUATION |
| TP_R200 | 2115 | 2180 | +€3,92 | 37,4% | 165 | 361 | READY_FOR_BLOCK4_EVALUATION |
| BE_R100 | 2034 | 2099 | €-17,87 | 19,4% | 205 | 674 | READY_FOR_BLOCK4_EVALUATION |

## Come leggere il controllo

- **EARLIER_BETTER**: la variante è uscita prima e ha conservato più profitto.
- **TOO_EARLY**: la variante è uscita prima ma ha tagliato un movimento migliore.
- **LATER_BETTER**: la variante ha continuato dopo l'uscita originale e ha guadagnato di più.
- **TOO_LATE**: la variante è rimasta aperta più a lungo e ha peggiorato il risultato.

## Limiti e protezioni

Le regole Shadow mantengono entrata, quantità, commissioni, stop protettivo iniziale e liquidazione. Le ambiguità all'interno della stessa candela vengono risolte scegliendo l'esito peggiore. Le posizioni già aperte al momento dell'installazione sono marcate come campione parziale e non saranno utilizzate dal futuro Blocco 4 come prova piena.

# Blocco 4 — Valutazione statistica Shadow

Generato: 2026-07-27T18:23:53+00:00

> Modulo esclusivamente valutativo. Non modifica strategie, uscite, posizioni o capitale. Le candidature vengono consegnate al futuro Blocco 5, senza applicazione automatica.

## Stato

- Risultati Block 3 disponibili: **73018**
- Valutazioni prodotte: **16483**
- Candidature al Blocco 5: **0**
- Mutazioni create automaticamente: **0**

## Classifica complessiva

| Scenario | Campione pieno | Δ medio (R) | Mediana (R) | CI bootstrap basso | Migliora | Score | Stato |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| GB20_R050 | 40 | 3,608 | 4,831 | 2,939 | 87,5% | 87,3 | EARLY_SIGNAL |
| GB30_R050 | 40 | 3,583 | 4,818 | 2,878 | 87,5% | 87,3 | EARLY_SIGNAL |
| GB20_R075 | 40 | 3,537 | 4,831 | 2,811 | 87,5% | 87,3 | EARLY_SIGNAL |
| GB30_R075 | 40 | 3,515 | 4,818 | 2,779 | 87,5% | 87,3 | EARLY_SIGNAL |
| GB40_R050 | 40 | 3,477 | 4,678 | 2,797 | 87,5% | 87,3 | EARLY_SIGNAL |
| GB40_R075 | 40 | 3,411 | 4,678 | 2,753 | 87,5% | 87,3 | EARLY_SIGNAL |
| GB50_R050 | 40 | 3,362 | 4,538 | 2,736 | 87,5% | 87,3 | EARLY_SIGNAL |
| GB50_R075 | 40 | 3,299 | 4,538 | 2,515 | 87,5% | 87,3 | EARLY_SIGNAL |
| ATR15_R050 | 40 | 2,983 | 4,115 | 2,345 | 87,5% | 87,3 | EARLY_SIGNAL |
| GB30_R100 | 40 | 3,407 | 4,818 | 2,653 | 87,5% | 87,3 | EARLY_SIGNAL |
| TP_R075 | 40 | 3,375 | 4,587 | 2,659 | 87,5% | 87,3 | EARLY_SIGNAL |
| ATR10_R050 | 40 | 3,350 | 4,641 | 2,660 | 87,5% | 87,3 | EARLY_SIGNAL |
| GB40_R100 | 40 | 3,301 | 4,678 | 2,615 | 87,5% | 87,3 | EARLY_SIGNAL |
| TP_R060 | 40 | 3,248 | 4,437 | 2,550 | 87,5% | 87,3 | EARLY_SIGNAL |
| TP_R050 | 40 | 3,238 | 4,337 | 2,594 | 87,5% | 87,3 | EARLY_SIGNAL |
| GB50_R100 | 40 | 3,195 | 4,538 | 2,461 | 87,5% | 87,3 | EARLY_SIGNAL |
| TP_R040 | 40 | 3,148 | 4,238 | 2,598 | 87,5% | 87,3 | EARLY_SIGNAL |
| TP_R035 | 40 | 3,103 | 4,188 | 2,510 | 87,5% | 87,3 | EARLY_SIGNAL |
| GB20_R100 | 40 | 3,424 | 4,831 | 2,706 | 87,5% | 87,3 | EARLY_SIGNAL |
| ATR15_R100 | 40 | 2,858 | 4,115 | 2,143 | 87,5% | 87,3 | EARLY_SIGNAL |

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

Generato: 2026-07-27T18:24:40+00:00

Questi profili sono osservativi e Paper-only. Usano gli stessi trade della madre, ma applicano una specifica uscita Block 3 soltanto ai segnali aperti dopo la loro registrazione.
Nessuna promozione, modifica live o operazione reale viene eseguita automaticamente.

| Challenger | Madre | Scenario | Chiusi | Copertura | PF | PnL | Exp/trade | DD | Stato |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Rapida 1H V1 — giveback 20% dopo +0,5R | SHADOW_1H_FAST | GB20_R050 | 21 | 100,00% | 1,35 | +€125,64 | +€5,98 | 1,41% | COLLECTING |
| Rapida 1H V1 — giveback 30% dopo +0,5R | SHADOW_1H_FAST | GB30_R050 | 21 | 100,00% | 1,17 | +€60,61 | +€2,89 | 1,48% | COLLECTING |
| Relative Strength — giveback 20% dopo +0,5R | SHADOW_RELATIVE_STRENGTH | GB20_R050 | 13 | 100,00% | 1,24 | +€44,79 | +€3,45 | 0,91% | COLLECTING |
| Relative Strength — giveback 30% dopo +0,5R | SHADOW_RELATIVE_STRENGTH | GB30_R050 | 13 | 100,00% | 1,07 | +€13,30 | +€1,02 | 0,91% | COLLECTING |
| Scanner Top 5 BTC Strength — giveback 20% dopo +1,4R | SHADOW_SCANNER_TOP5_BTC | GB20_R140 | 3 | 75,00% | 0,00 | €-105,61 | €-35,20 | 1,06% | COLLECTING |
| Master Adaptive Consensus — breakeven dopo +0,2R | SHADOW_MASTER_ADAPTIVE_V1 | BE_A020 | 5 | 100,00% | 0,00 | €-104,23 | €-20,85 | 1,04% | COLLECTING |
| Momentum Breakout V3 Filtered — giveback 20% dopo +1,0R | SHADOW_1H_FAST_V3 | GB20_R100 | 8 | 100,00% | 0,39 | €-130,66 | €-16,33 | 2,13% | COLLECTING |
| Momentum Breakout — giveback 20% dopo +1,4R | SHADOW_1H_FAST | GB20_R140 | 0 | 0,00% | 0,00 | €0,00 | €0,00 | 0,00% | COLLECTING |

## Regole di valutazione

- Prima fotografia a 30 trade indipendenti.
- Revisione per possibile promozione a 50 trade indipendenti.
- PF minimo 1,50, expectancy e PnL positivi, drawdown massimo 15%, copertura minima 90%.
- PF deve superare la madre e il drawdown non deve essere peggiore sulla stessa serie di trade.
- La promozione resta una decisione umana protetta; il rollback viene predisposto soltanto in fase di approvazione.

# Blocco 4.5 — Crash Cascade Guard

Generato: 2026-07-27T18:23:38+00:00

> Paper-only. In mercato NORMAL/WATCH non riduce i segnali. Le limitazioni iniziano soltanto in STRESS, RECOVERY, CRASH, EXTREME o con dati non affidabili.

## Stato corrente

- Livello: **NORMAL**
- Direzione: **NONE**
- Segnali bloccati nel ciclo: **0**
- Simulazioni bloccate attive: **2**
- Simulazioni completate nel ciclo: **0**
- Liquidazioni virtuali evitate totali: **0**
- Valore cumulato del filtro: **165.03 R**
- Profitto virtuale mancato: **259.49 R**

## Stress test portafogli Paper

| Scenario | Posizioni interessate | Liquidazioni stimate | Perdita stimata EUR |
| --- | ---: | ---: | ---: |
| DOWN_10 | 182 | 0 | 15713.11 |
| DOWN_20 | 182 | 0 | 31426.21 |
| DOWN_30 | 182 | 1 | 47140.21 |
| DOWN_40 | 182 | 52 | 60596.93 |
| UP_10 | 168 | 0 | 26825.09 |
| UP_20 | 168 | 0 | 53650.17 |
| UP_30 | 168 | 0 | 80475.26 |
| UP_40 | 168 | 90 | 96276.75 |

## Modello di esecuzione

Se una candela di cascata attraversa nello stesso intervallo sia lo stop sia il prezzo di liquidazione, il Paper usa il caso peggiore e registra una liquidazione intrabar. Gli stop in gap o in regime di stress ricevono slippage aggiuntivo.

## Requisiti prima del live futures

- modalità ISOLATED obbligatoria;
- stop nativo sull'exchange;
- conferma dello stop prima di accettare la posizione;
- cross margin vietato.

# Blocco 5 — Candidati evolutivi controllati

Generato: 2026-07-27T18:23:13+00:00

> Paper-only. Nessuna promozione, sostituzione del MASTER, modifica live o ordine reale.

## Stato

- Candidati attivi: **16**
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
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | SHADOW_1H_FAST_V3_CAP75_V1 | reward_risk | 1.5 | 2.5 | TP_R250 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | SHADOW_1H_FAST_V3 | reward_risk | 1.5 | 2.0 | TP_R200 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V1 | reward_risk | 1.5 | 2.0 | TP_R200 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | reward_risk | 1.5 | 2.0 | TP_R200 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | SHADOW_1H_FAST_V3 | reward_risk | 1.5 | 2.5 | TP_R250 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_V1 | reward_risk | 1.5 | 2.0 | TP_R200 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | SHADOW_1H_FAST_V3_LONG_ONLY_V1 | reward_risk | 1.5 | 2.0 | TP_R200 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONLY_V1 | reward_risk | 1.5 | 2.0 | TP_R200 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | SHADOW_1H_FAST_V3_NOHIGH_V1 | reward_risk | 1.5 | 2.0 | TP_R200 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | SHADOW_1H_FAST_V3_CAP75_V1 | reward_risk | 1.5 | 2.0 | TP_R200 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_GUARD_V1 | reward_risk | 1.5 | 2.0 | TP_R200 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | reward_risk | 1.5 | 2.0 | TP_R200 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_V1 | reward_risk | 1.5 | 2.0 | TP_R200 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | SHADOW_1H_FAST_V3_LONG_ONLY_V1 | reward_risk | 1.5 | 2.5 | TP_R250 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | SHADOW_1H_FAST_V3_NOHIGH_V1 | reward_risk | 1.5 | 2.5 | TP_R250 |

## Vincoli v1

- Supportati: FIXED_R, TIME_EXIT e ATR_TRAIL solo quando richiede una singola variazione.
- MFE_GIVEBACK e BREAKEVEN non vengono approssimati: restano evidenze da implementare in una versione successiva.
- Nessun candidato può diventare MASTER nel Blocco 5.

# Blocco 6 — Validazione Champion/Challenger

Generato: 2026-07-27T18:24:41+00:00

> Paper-only. Confronto sulle stesse entrate tramite `experiment_group_id`. Nessuna promozione, sostituzione, pensione o modifica live automatica.

## Stato

- Candidati valutati: **16**
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
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | SHADOW_1H_FAST_V3_CAP75_V1 | INCUBATING | 0 | 0.000 | 0.000 | 0.00 | 0.00 | 0.00 | 0.00 | 20.0 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | SHADOW_1H_FAST_V3 | INCUBATING | 0 | 0.000 | 0.000 | 0.00 | 0.00 | 0.00 | 0.00 | 20.0 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | SHADOW_1H_FAST_V3_LONG_ONLY_V1 | INCUBATING | 0 | 0.000 | 0.000 | 0.00 | 0.00 | 0.00 | 0.00 | 20.0 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | SHADOW_1H_FAST_V3_NOHIGH_V1 | INCUBATING | 0 | 0.000 | 0.000 | 0.00 | 0.00 | 0.00 | 0.00 | 20.0 |

## Gate di sicurezza

- Solo trade chiusi dopo la creazione della candidata.
- Solo coppie con lo stesso evento d’ingresso.
- Solo dati `FULL_FROM_ENTRY` e risk model `block4_5_v1`.
- Campione, bootstrap, stabilità temporale, dipendenza dai migliori trade, PF, drawdown e liquidazioni.
- `PROMOTION_REVIEW_READY` è soltanto una raccomandazione: richiede approvazione umana e un blocco successivo.

# Blocco 7 — Governance promozioni Paper

Generato: 2026-07-27T18:24:41+00:00

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

Generato: 2026-07-27T18:24:41+00:00

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

Generato: 2026-07-27T18:24:41+00:00

> Paper-only. La memoria può bloccare soltanto una futura proposta Block 5 classificata AVOID; non modifica strategie esistenti.

## Stato

- Strategie/portafogli valutati: **141**
- Hall of Fame: **20**
- Memorie genetiche: **4**
- Firme bloccate: **0**
- Azioni automatiche e live: **0**

## Hall of Fame

| Rank | Strategia | Stato | Score | Grade | Trade | PF | Expectancy R | DD R |
| ---: | --- | --- | ---: | --- | ---: | ---: | ---: | ---: |
| 1 | SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_V1 | BASELINE | 20.2 | E | 34 | 1.95 | 0.259 | 3.00 |
| 2 | SHADOW_DONCHIAN_1H | BASELINE | 19.8 | E | 30 | 1.84 | 0.352 | 2.18 |
| 3 | SHADOW_1H_FAST_NOHIGH_CAP75_V1 | BASELINE | 17.5 | E | 58 | 1.54 | 0.210 | 5.40 |
| 4 | SHADOW_1H_FAST_V3_CAP75_V1 | BASELINE | 16.5 | E | 51 | 1.46 | 0.174 | 3.68 |
| 5 | SHADOW_SCANNER_TOP5_LONG | BASELINE | 16.4 | E | 44 | 1.55 | 0.245 | 6.47 |
| 6 | SHADOW_1H_FAST_V3 | BASELINE | 16.1 | E | 84 | 1.25 | 0.103 | 5.36 |
| 7 | SHADOW_1H_FAST_SCORE_6_75_V1 | BASELINE | 15.7 | E | 57 | 1.36 | 0.136 | 3.71 |
| 8 | SHADOW_1H_BALANCED_V3 | BASELINE | 15.7 | E | 50 | 1.42 | 0.189 | 3.23 |
| 9 | SHADOW_1H_FAST_NO_PEPE_V1 | BASELINE | 15.7 | E | 49 | 1.42 | 0.172 | 3.55 |
| 10 | SHADOW_SCANNER_TOP5_BTC | BASELINE | 14.0 | E | 33 | 1.41 | 0.200 | 5.51 |

## Memoria genetica

| Scope | Famiglia | Mutazione | Target | Stato | Score | Prove | Coppie | Blocco |
| --- | --- | --- | --- | --- | ---: | ---: | ---: | --- |
| FAMILY | momentum_breakout_v3_filtered | reward_risk INCREASE | 2 | INSUFFICIENT | 62.5 | 12 | 0 | NO |
| FAMILY | momentum_breakout_v3_filtered | reward_risk INCREASE | 2.5 | INSUFFICIENT | 47.5 | 4 | 0 | NO |
| GLOBAL | GLOBAL | reward_risk INCREASE | 2 | INSUFFICIENT | 62.5 | 12 | 0 | NO |
| GLOBAL | GLOBAL | reward_risk INCREASE | 2.5 | INSUFFICIENT | 47.5 | 4 | 0 | NO |

## Sicurezza

- Nessuna strategia, posizione o promozione esistente viene modificata.
- Nessuna mutazione, promozione, pensionamento o rollback automatico.
- Nessun effetto live e nessun ordine reale.

# Blocco 10 — Regime Fitness e specializzazione

Generato: 2026-07-27T18:24:41+00:00

> Paper-only e advisory. Il blocco misura quali strategie funzionano nei diversi regimi, ma non cambia automaticamente strategia o posizione.

## Stato

- Regime corrente: **HIGH_VOLATILITY**
- Righe di performance: **503**
- Strategie preferite nel regime corrente: **0**
- Strategie da evitare nel regime corrente: **0**
- Memorie contestuali: **239**
- Routing automatico: **NO**

## Classifica del regime corrente

| Rank | Portafoglio | Famiglia | Stato | Fitness | Trade | PF | Expectancy R | DD R |
| ---: | --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| 1 | SHADOW_BTC_ADAPTIVE_1H | shadow-btc-adaptive-1h | INSUFFICIENT | 80.4 | 1 | 99.00 | 0.861 | 0.00 |
| 2 | SHADOW_BTC_DONCHIAN_1H | shadow-btc-donchian-1h | INSUFFICIENT | 80.4 | 1 | 99.00 | 0.969 | 0.00 |
| 3 | SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | shadow-1h-fast-long-btc-1-3-cap75-v1 | INSUFFICIENT | 80.4 | 1 | 99.00 | 1.374 | 0.00 |
| 4 | SHADOW_ETH_ADAPTIVE_1H | shadow-eth-adaptive-1h | INSUFFICIENT | 75.7 | 1 | 99.00 | 0.286 | 0.00 |
| 5 | SHADOW_SCANNER_TOP5_LONG | shadow-scanner-top5-long | INSUFFICIENT | 72.9 | 7 | 4.66 | 0.664 | 1.12 |
| 6 | SHADOW_BOLLINGER_MR_1H | shadow-bollinger-mr-1h | INSUFFICIENT | 70.6 | 2 | 13.28 | 0.660 | 0.11 |
| 7 | SHADOW_BTC_EMA_1H | shadow-btc-ema-1h | INSUFFICIENT | 66.0 | 2 | 1.78 | 0.429 | 1.10 |
| 8 | SHADOW_SOL_DONCHIAN_1H | shadow-sol-donchian-1h | INSUFFICIENT | 65.3 | 1 | 99.00 | 0.037 | 0.00 |
| 9 | SHADOW_ETH_DONCHIAN_1H | shadow-eth-donchian-1h | INSUFFICIENT | 64.6 | 2 | 1.71 | 0.391 | 1.11 |
| 10 | SHADOW_SCANNER_TOP5_BTC_MFE_V1 | shadow-scanner-top5-btc-mfe-v1 | INSUFFICIENT | 62.0 | 4 | 4.53 | 0.176 | 0.20 |

## Sicurezza

- Il regime viene assegnato usando solo l'ultimo record noto prima dell'entrata del trade.
- Nessun uso di dati futuri per classificare il trade.
- Il Candidate Regime Gate è advisory per impostazione predefinita.
- Nessun cambio automatico di MASTER, posizione o live.

# Blocco 11 — Collegamento protetto al live

Generato: 2026-07-27T18:24:41+00:00

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

Generato: 2026-07-27T18:23:38+00:00

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
