# Paper trading automatico KuCoin

Generato: 2026-07-27T20:39:45+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-07-27T20:38:26+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-07-27T20:38:26+00:00 | 2026-07-27T20:38:26+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-07-27T20:15:00+00:00 | 2026-07-27T20:15:00+00:00 | 8,5 min | 25,0 min | OK |
| 60m | 12 | 2026-07-27T19:00:00+00:00 | 2026-07-27T19:00:00+00:00 | 38,5 min | 45,0 min | OK |
| 240m | 12 | 2026-07-27T16:00:00+00:00 | 2026-07-27T16:00:00+00:00 | 38,5 min | 1,00 h | OK |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | HYPE | 240m | SHORT | -7,43 | 6,00 | 0,00 | RISK_GATE | 38,5 min | D: n/a | W: n/a | peso 0 | Filtro rischio/esecuzione: asset già aperto nel portafoglio. |
| Principale 4H | SHIB | 240m | LONG | 5,75 | 6,00 | 0,25 | BELOW_SCORE | 38,5 min | D: n/a | W: n/a | peso 0 | Punteggio +5.75; soglia ±6.00; mancano 0.25 punti. |
| Principale 4H | PEPE | 240m | LONG | 5,22 | 6,00 | 0,78 | BELOW_SCORE | 38,5 min | D: n/a | W: n/a | peso 0 | Punteggio +5.22; soglia ±6.00; mancano 0.78 punti. |
| Principale 4H | ENA | 240m | LONG | 5,14 | 6,00 | 0,86 | BELOW_SCORE | 38,5 min | D: n/a | W: n/a | peso 0 | Punteggio +5.14; soglia ±6.00; mancano 0.86 punti. |
| Bilanciata 1H V2 | HYPE | 60m | SHORT | -6,87 | 5,50 | 0,00 | STRATEGY_FILTER | 38,5 min | D: n/a | W: n/a | peso 0 | Filtro V2 non superato: regime, EMA, ritorni e RSI; per Rapida V2 servono anche breakout reale, volume e ADX. |
| Rapida 1H V2 | HYPE | 60m | SHORT | -6,87 | 5,00 | 0,00 | STRATEGY_FILTER | 38,5 min | D: n/a | W: n/a | peso 0 | Filtro V2 non superato: regime, EMA, ritorni e RSI; per Rapida V2 servono anche breakout reale, volume e ADX. |
| Bilanciata 1H V2 | AKE | 60m | LONG | 6,25 | 5,50 | 0,00 | STRATEGY_FILTER | 38,5 min | D: n/a | W: n/a | peso 0 | Filtro V2 non superato: regime, EMA, ritorni e RSI; per Rapida V2 servono anche breakout reale, volume e ADX. |
| Rapida 1H V1 — madre | AKE | 60m | LONG | 6,25 | 4,50 | 0,00 | STRATEGY_FILTER | 38,5 min | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout UP oppure movimento breve ≥1,5%; breakout=NONE, movimento=-1.16%. |
| Rapida V1 — score 6–7,5 | AKE | 60m | LONG | 6,25 | 6,00 | 0,00 | STRATEGY_FILTER | 38,5 min | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout UP oppure movimento breve ≥1,5%; breakout=NONE, movimento=-1.16%. |
| Rapida score 6–7,5 — senza Trend Up | AKE | 60m | LONG | 6,25 | 6,00 | 0,00 | STRATEGY_FILTER | 38,5 min | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout UP oppure movimento breve ≥1,5%; breakout=NONE, movimento=-1.16%. |
| Rapida score 6–7,5 — Range Only | AKE | 60m | LONG | 6,25 | 6,00 | 0,00 | STRATEGY_FILTER | 38,5 min | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout UP oppure movimento breve ≥1,5%; breakout=NONE, movimento=-1.16%. |
| Rapida score 6–7,5 — Cost Aware | AKE | 60m | LONG | 6,25 | 6,00 | 0,00 | STRATEGY_FILTER | 38,5 min | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout UP oppure movimento breve ≥1,5%; breakout=NONE, movimento=-1.16%. |
| Rapida V1 — no HIGH + score <7,5 | AKE | 60m | LONG | 6,25 | 4,50 | 0,00 | STRATEGY_FILTER | 38,5 min | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout UP oppure movimento breve ≥1,5%; breakout=NONE, movimento=-1.16%. |
| Rapida V1 — Long + BTC 1–3 + score <7,5 | AKE | 60m | LONG | 6,25 | 4,50 | 0,00 | STRATEGY_FILTER | 38,5 min | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout UP oppure movimento breve ≥1,5%; breakout=NONE, movimento=-1.16%. |
| Rapida V1 — senza PEPE | AKE | 60m | LONG | 6,25 | 4,50 | 0,00 | STRATEGY_FILTER | 38,5 min | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout UP oppure movimento breve ≥1,5%; breakout=NONE, movimento=-1.16%. |
| Rapida V1 — target pieno 2R | AKE | 60m | LONG | 6,25 | 4,50 | 0,00 | STRATEGY_FILTER | 38,5 min | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout UP oppure movimento breve ≥1,5%; breakout=NONE, movimento=-1.16%. |
| Rapida 1H V2 | AKE | 60m | LONG | 6,25 | 5,00 | 0,00 | STRATEGY_FILTER | 38,5 min | D: n/a | W: n/a | peso 0 | Filtro V2 non superato: regime, EMA, ritorni e RSI; per Rapida V2 servono anche breakout reale, volume e ADX. |
| FAST NoHigh <7,5 · SHORT only | AKE | 60m | LONG | 6,25 | 4,50 | 0,00 | STRATEGY_FILTER | 38,5 min | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout UP oppure movimento breve ≥1,5%; breakout=NONE, movimento=-1.16%. |
| Bilanciata 1H V2 | ZEC | 60m | SHORT | -6,06 | 5,50 | 0,00 | STRATEGY_FILTER | 38,5 min | D: n/a | W: n/a | peso 0 | Filtro V2 non superato: regime, EMA, ritorni e RSI; per Rapida V2 servono anche breakout reale, volume e ADX. |
| Rapida 1H V2 | ZEC | 60m | SHORT | -6,06 | 5,00 | 0,00 | STRATEGY_FILTER | 38,5 min | D: n/a | W: n/a | peso 0 | Filtro V2 non superato: regime, EMA, ritorni e RSI; per Rapida V2 servono anche breakout reale, volume e ADX. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.745,66 | -2,54% | €-254,34 | €3.000,00 | -8,48% | 5 | 24 | 29,17% | 0,71 | 4,76% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 24 | 823 | CAMPIONE INSUFFICIENTE | 30 (mancano 6) |

- Trade del Principale 4H chiusi: **24**; win rate **29,17%**; profit factor **0,71**.
- Expectancy: **€-10,51** per trade; P&L netto: **€-252,20**; max drawdown: **4,76%**.
- Valutazione: **Servono altri eventi indipendenti prima di trarre conclusioni.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 5 | €9.745,66 | €1.366,40 | €4.099,20 | €145,85 | €-0,39 |
| TEST | Benchmark Donchian breakout 1H | 6 | €10.676,74 | €4.746,56 | €9.493,11 | €160,54 | €38,69 |
| TEST | Bilanciata 1H V3 Filtered | 6 | €10.568,40 | €1.764,99 | €5.294,98 | €211,33 | €-2,23 |
| TEST | Rapida V1 — no HIGH + score <7,5 | 3 | €10.538,89 | €629,70 | €1.889,10 | €156,12 | €-4,31 |
| TEST | Scanner Top 5 Long 1H | 2 | €10.531,09 | €286,76 | €573,51 | €2,58 | €34,13 |
| TEST | Rapida V3 — score <7,5 | 5 | €10.471,29 | €1.749,25 | €5.247,76 | €209,83 | €-35,09 |
| TEST | Rapida V1 — score 6–7,5 | 4 | €10.424,20 | €2.424,29 | €7.272,86 | €209,04 | €-64,69 |
| TEST | Scanner Top 5 + forza BTC 1H | 4 | €10.400,82 | €1.368,67 | €2.737,33 | €105,62 | €34,18 |
| TEST | Rapida V3 NoHigh — Regime Guard | 1 | €10.395,73 | €172,19 | €516,57 | €51,51 | €0,00 |
| TEST | Rapida score 6–7,5 — Cost Aware | 4 | €10.384,87 | €2.414,46 | €7.243,38 | €208,09 | €-64,45 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 1 | €10.329,45 | €144,01 | €432,02 | €51,84 | €-4,23 |
| TEST | Rapida score 6–7,5 — Range Only | 2 | €10.320,70 | €399,26 | €1.197,78 | €102,92 | €0,00 |
| TEST | Rapida V3 senza ESPORTS — MFE Lock | 6 | €10.320,63 | €2.939,10 | €8.817,31 | €206,81 | €-17,27 |
| TEST | Rapida score 6–7,5 — senza Trend Up | 4 | €10.311,51 | €2.520,39 | €7.561,16 | €205,19 | €-59,80 |
| TEST | Bilanciata 1H V1 | 6 | €10.303,89 | €2.121,92 | €6.365,75 | €154,09 | €-11,19 |
| TEST | Rapida V3 NoHigh — Range Only | 2 | €10.296,85 | €313,60 | €940,79 | €102,49 | €0,00 |
| TEST | MAIN — Dynamic Asset Selector | 1 | €10.284,81 | €142,87 | €428,60 | €51,43 | €-1,34 |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 5 | €10.274,60 | €2.477,27 | €7.431,81 | €205,39 | €-26,85 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 5 | €10.252,73 | €1.607,06 | €4.821,19 | €155,77 | €-35,08 |
| TEST | Rapida V1 — senza PEPE | 5 | €10.251,71 | €3.586,77 | €10.760,32 | €154,24 | €3,54 |
| TEST | Rapida V3 senza ESPORTS — Long Only | 2 | €10.236,96 | €386,33 | €1.159,00 | €49,93 | €32,59 |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 2 | €10.235,71 | €336,78 | €1.010,33 | €50,80 | €0,00 |
| TEST | Combo Adaptive — Side × Regime Guard | 5 | €10.234,44 | €2.690,57 | €5.381,13 | €154,06 | €10,34 |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 1 | €10.227,50 | €142,59 | €427,78 | €51,33 | €14,34 |
| TEST | Combo Adaptive — madre | 5 | €10.214,26 | €1.579,88 | €3.159,76 | €204,02 | €13,25 |
| TEST | Bilanciata 1H V2 | 4 | €10.212,08 | €1.500,45 | €4.501,34 | €152,14 | €11,92 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 1 | €10.205,44 | €141,91 | €425,73 | €51,09 | €-4,17 |
| TEST | FAST NoHigh <7,5 · SHORT only | 3 | €10.179,33 | €1.176,48 | €3.529,44 | €149,64 | €-4,16 |
| TEST | Rapida 1H V3 Filtered — madre | 5 | €10.176,47 | €3.570,42 | €10.711,27 | €203,91 | €-16,47 |
| TEST | Btc Bollinger 1H | 0 | €10.168,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | MAIN — Side × Regime Guard | 4 | €10.167,19 | €1.079,92 | €3.239,75 | €152,51 | €-7,68 |
| TEST | Combo Adaptive — 75% a 2R + runner 25% a 3R | 6 | €10.165,57 | €2.300,48 | €4.600,96 | €152,44 | €33,26 |
| TEST | Combo Adaptive — Quality7 | 4 | €10.106,04 | €2.197,33 | €4.394,65 | €200,20 | €-1,32 |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 5 | €10.100,92 | €2.410,07 | €7.230,21 | €202,72 | €-45,06 |
| TEST | Sol Donchian 1H | 0 | €10.092,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Ema 1H | 0 | €10.091,86 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Top 5 + BTC — target pieno 3R | 4 | €10.089,41 | €1.363,56 | €2.727,12 | €153,24 | €-4,09 |
| TEST | Sol Bollinger 4H | 0 | €10.086,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Trend — Side × Regime Guard | 5 | €10.085,02 | €2.231,14 | €4.462,28 | €200,18 | €-31,97 |
| TEST | Forza relativa 1H V2 | 3 | €10.084,30 | €1.704,09 | €3.408,19 | €54,70 | €33,22 |
| TEST | Btc Bollinger 4H | 0 | €10.084,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Top 5 + BTC — 75% a 2,2R + runner 3R | 4 | €10.083,47 | €1.348,99 | €2.697,97 | €152,68 | €-4,08 |
| TEST | Rapida V3 — qualità completa + profit lock | 2 | €10.077,50 | €385,11 | €1.155,33 | €99,59 | €-4,11 |
| TEST | Rapida V3 senza ESPORTS — Stress Guard | 0 | €10.071,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V1 — Long + BTC 1–3 + score <7,5 | 0 | €10.064,94 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V1 — madre | 1 | €10.048,63 | €1.486,90 | €4.460,70 | €49,96 | €0,00 |
| TEST | Ampia 4H | 5 | €10.042,28 | €1.759,28 | €3.518,56 | €200,08 | €14,67 |
| TEST | Combo Adaptive — Long Only | 5 | €10.040,64 | €2.704,77 | €5.409,53 | €150,03 | €32,28 |
| TEST | Rapida V1 — target pieno 2R | 6 | €10.024,29 | €2.917,83 | €8.753,50 | €200,87 | €-16,64 |
| TEST | Top 5 + BTC — BTC 2–3 | 3 | €10.021,69 | €1.301,34 | €2.602,67 | €150,18 | €-1,31 |
| TEST | Btc Adaptive 1H | 0 | €10.013,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Benchmark Bollinger mean reversion 1H | 2 | €10.011,62 | €1.672,98 | €3.345,96 | €99,95 | €11,52 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €10.010,36 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Top 5 + BTC — BTC≤3 | 4 | €10.009,50 | €1.339,17 | €2.678,35 | €151,61 | €-1,31 |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 1 | €10.003,88 | €141,08 | €423,23 | €50,79 | €0,00 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 0 | €10.002,07 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €50 · 15x | 0 | €10.000,61 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €10 · 15x | 0 | €10.000,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Continuation V1 | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €10 · 15x | 0 | €9.999,70 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €10 · 15x | 0 | €9.998,96 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Mean Reversion | 1 | €9.998,95 | €1.998,97 | €3.997,94 | €47,98 | €6,50 |
| TEST | Scalp RSI Short 85 · prudente · 5x | 0 | €9.998,64 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €50 · 15x | 0 | €9.998,52 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €10 · 15x | 0 | €9.998,50 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H — SHORT Trend Down stretto | 0 | €9.995,87 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €50 · 15x | 0 | €9.994,81 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €50 · 15x | 0 | €9.992,50 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €10 · 15x | 0 | €9.991,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 0 | €9.990,65 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · prudente · 5x | 0 | €9.990,24 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · prudente · 5x | 0 | €9.988,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Top 5 + BTC — Guard + BTC≤3 | 3 | €9.985,61 | €1.284,96 | €2.569,92 | €148,75 | €-1,30 |
| TEST | Scalp RSI Long 20 · prudente · 5x | 0 | €9.983,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Donchian 1H Gb20 120R V1 | 4 | €9.982,69 | €5.366,04 | €10.732,08 | €150,19 | €-10,87 |
| TEST | Btc Donchian 1H | 0 | €9.980,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V2 | 1 | €9.979,60 | €1.494,54 | €4.483,63 | €50,22 | €0,00 |
| TEST | Sol Ema 1H | 0 | €9.977,09 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 — Long + no HIGH + score <7,5 | 2 | €9.975,38 | €385,32 | €1.155,95 | €99,43 | €-4,08 |
| TEST | Rapida V3 — senza ESPORTS | 5 | €9.969,25 | €3.497,69 | €10.493,07 | €199,75 | €-16,15 |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | 6 | €9.961,03 | €2.600,26 | €5.200,52 | €199,52 | €-13,73 |
| TEST | Doge Donchian 1H | 1 | €9.959,98 | €1.286,97 | €3.860,92 | €49,99 | €-36,46 |
| TEST | Eth Bollinger 1H | 0 | €9.959,49 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 0 | €9.955,61 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €50 · 15x | 0 | €9.955,59 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.951,70 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 4H | 0 | €9.950,68 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 4H | 0 | €9.950,68 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 4H | 0 | €9.949,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 4H | 1 | €9.947,16 | €761,04 | €1.522,08 | €49,74 | €-0,63 |
| TEST | Sol Donchian 4H | 1 | €9.946,90 | €830,21 | €1.660,43 | €49,74 | €-0,68 |
| TEST | Bilanciata V3 · LONG only | 5 | €9.943,76 | €2.341,20 | €7.023,61 | €149,38 | €-2,05 |
| TEST | Eth Ema 4H | 1 | €9.941,53 | €1.036,30 | €2.072,59 | €49,74 | €-4,09 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 4 | €9.939,93 | €3.581,90 | €10.745,69 | €199,10 | €-56,31 |
| TEST | Combo Adaptive — Quality7 + Regime + parziale 1R | 2 | €9.936,41 | €1.071,47 | €2.142,94 | €49,61 | €32,73 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 1 | €9.936,07 | €138,53 | €415,58 | €49,87 | €13,93 |
| TEST | Combo Adaptive — Trend/Transition | 3 | €9.931,17 | €450,30 | €900,60 | €98,93 | €12,62 |
| TEST | Combo Adaptive — target pieno 3R | 4 | €9.929,58 | €2.226,41 | €4.452,81 | €198,61 | €0,00 |
| TEST | Master Adaptive GB20 — Breakeven 0,5R | 3 | €9.928,46 | €1.902,43 | €3.804,85 | €100,69 | €32,75 |
| TEST | Btc Ema 1H | 0 | €9.911,86 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Profit Lock V1 | 6 | €9.909,51 | €2.577,78 | €5.155,57 | €148,89 | €-6,75 |
| TEST | Rapida V3 — no volatilità HIGH | 3 | €9.904,92 | €2.446,43 | €7.339,28 | €149,26 | €12,62 |
| TEST | Bilanciata 1H — LONG senza Range High Vol | 3 | €9.902,43 | €1.245,83 | €3.737,50 | €100,06 | €32,43 |
| TEST | Combo Scanner | 5 | €9.901,71 | €2.926,50 | €5.853,00 | €197,44 | €-34,84 |
| TEST | Sol Bollinger 1H | 0 | €9.901,25 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 4H | 0 | €9.896,31 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive GB20 — 50% a 0,75R | 3 | €9.895,55 | €1.770,78 | €3.541,56 | €100,28 | €16,31 |
| TEST | Doge Bollinger 1H | 0 | €9.888,87 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 5 | €9.882,17 | €1.541,34 | €4.624,01 | €150,19 | €-17,16 |
| TEST | Eth Donchian 1H | 0 | €9.871,99 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive GB20 — Loss Cap 0,75R | 3 | €9.870,03 | €2.431,87 | €4.863,75 | €150,19 | €32,82 |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 4 | €9.855,29 | €3.545,79 | €10.637,38 | €147,77 | €-19,10 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 2 | €9.844,81 | €330,74 | €992,21 | €98,29 | €13,70 |
| TEST | Combo Adaptive — Quality7 + Regime | 2 | €9.843,39 | €1.069,53 | €2.139,06 | €49,61 | €32,42 |
| TEST | Sol Adaptive 1H | 0 | €9.835,19 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 1 | €9.800,72 | €137,23 | €411,70 | €0,00 | €32,52 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 1 | €9.800,72 | €137,23 | €411,70 | €0,00 | €32,52 |
| TEST | Eth Adaptive 1H | 0 | €9.799,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Top 5 + BTC — Guard | 2 | €9.793,27 | €406,73 | €813,45 | €48,59 | €32,26 |
| TEST | Top 5 + BTC — solo MFE | 3 | €9.788,63 | €2.402,85 | €4.805,70 | €148,00 | €12,52 |
| TEST | Scanner Bottom10 Short | 6 | €9.782,53 | €3.337,78 | €6.675,57 | €146,98 | €-6,59 |
| TEST | Scanner Bottom15 Short | 6 | €9.782,53 | €3.337,78 | €6.675,57 | €146,98 | €-6,59 |
| TEST | Scanner Bottom20 Short | 6 | €9.782,53 | €3.337,78 | €6.675,57 | €146,98 | €-6,59 |
| TEST | Scanner Top10 Long | 3 | €9.776,88 | €1.600,42 | €3.200,85 | €101,91 | €-5,26 |
| TEST | Scanner Top15 Long | 3 | €9.776,88 | €1.600,42 | €3.200,85 | €101,91 | €-5,26 |
| TEST | Scanner Top20 Long | 3 | €9.776,88 | €1.600,42 | €3.200,85 | €101,91 | €-5,26 |
| TEST | Benchmark trend following EMA 1H | 5 | €9.775,33 | €2.076,29 | €4.152,58 | €195,47 | €13,25 |
| TEST | Global Confluence puro 1H | 1 | €9.760,29 | €1.512,23 | €3.024,45 | €48,95 | €-28,56 |
| TEST | Top 5 + BTC — Guard + BTC≤3 + MFE | 2 | €9.754,46 | €1.074,59 | €2.149,17 | €98,26 | €-1,27 |
| TEST | Rapida V3 — Long Only | 2 | €9.753,54 | €379,78 | €1.139,33 | €97,86 | €13,66 |
| TEST | Master Adaptive Expanded V1 | 4 | €9.736,70 | €1.273,31 | €2.546,62 | €148,04 | €32,06 |
| TEST | Scanner Bottom 5 Short 1H | 6 | €9.736,61 | €2.974,24 | €5.948,48 | €97,36 | €-6,64 |
| TEST | Eth Ema 1H | 0 | €9.727,87 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Runner25 V1 | 4 | €9.724,42 | €1.260,39 | €2.520,78 | €147,51 | €32,02 |
| TEST | Combo Adaptive — parziale 1R | 6 | €9.714,92 | €2.205,76 | €4.411,53 | €171,73 | €14,78 |
| TEST | Master Adaptive No Alt V1 | 4 | €9.696,76 | €1.260,48 | €2.520,96 | €147,40 | €31,93 |
| TEST | Master Adaptive V1 | 4 | €9.692,76 | €1.260,39 | €2.520,79 | €147,38 | €31,92 |
| TEST | Master Adaptive Gb20 V1 | 4 | €9.618,45 | €2.591,96 | €5.183,92 | €192,45 | €-3,79 |
| TEST | Top 5 + BTC — Guard + MFE | 1 | €9.600,93 | €200,07 | €400,14 | €48,02 | €12,30 |
| TEST | Combo Adaptive — MFE Trail esistente | 5 | €9.560,67 | €2.462,55 | €4.925,09 | €191,41 | €-9,51 |
| TEST | Combo Trend | 5 | €9.549,04 | €3.403,78 | €6.807,55 | €144,76 | €1,42 |
| TEST | Master Adaptive Strict3 V1 | 4 | €9.512,44 | €3.925,82 | €7.851,64 | €188,76 | €-0,84 |
| TEST | Forza relativa 1H V1 | 6 | €9.481,79 | €3.250,77 | €6.501,53 | €190,06 | €-18,85 |

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
| PRINCIPALE | Principale 4H | Confluenza trend | €9.745,66 | €-252,20 | 24 | 24 | 29,17% | 0,71 | €-10,51 | 4,76% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €10.676,74 | €644,32 | 30 | 30 | 53,33% | 2,20 | €21,48 | 2,12% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €10.568,40 | €573,89 | 52 | 52 | 42,31% | 1,55 | €11,04 | 2,20% |
| TEST | Rapida V1 — no HIGH + score <7,5 | Momentum / breakout | €10.538,89 | €544,42 | 58 | 58 | 48,28% | 1,51 | €9,39 | 2,83% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.531,09 | €497,39 | 45 | 45 | 48,89% | 1,49 | €11,05 | 3,57% |
| TEST | Rapida V3 — score <7,5 | Momentum / breakout V3 Filtered | €10.471,29 | €509,62 | 51 | 51 | 49,02% | 1,62 | €9,99 | 2,49% |
| TEST | Rapida V1 — score 6–7,5 | Momentum / breakout | €10.424,20 | €493,35 | 57 | 57 | 45,61% | 1,49 | €8,66 | 2,49% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €10.400,82 | €368,66 | 34 | 34 | 47,06% | 1,49 | €10,84 | 3,23% |
| TEST | Rapida V3 NoHigh — Regime Guard | Momentum / breakout V3 Filtered | €10.395,73 | €396,49 | 18 | 18 | 66,67% | 3,42 | €22,03 | 1,39% |
| TEST | Rapida score 6–7,5 — Cost Aware | Momentum / breakout | €10.384,87 | €453,75 | 20 | 20 | 60,00% | 2,61 | €22,69 | 1,96% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | Momentum / breakout V3 Filtered | €10.329,45 | €334,04 | 21 | 21 | 52,38% | 2,10 | €15,91 | 1,62% |
| TEST | Rapida score 6–7,5 — Range Only | Momentum / breakout | €10.320,70 | €321,53 | 11 | 11 | 63,64% | 2,70 | €29,23 | 2,28% |
| TEST | Rapida V3 senza ESPORTS — MFE Lock | Momentum / breakout V3 Filtered | €10.320,63 | €343,63 | 35 | 35 | 60,00% | 1,82 | €9,82 | 2,05% |
| TEST | Rapida score 6–7,5 — senza Trend Up | Momentum / breakout | €10.311,51 | €375,85 | 17 | 17 | 70,59% | 2,53 | €22,11 | 2,01% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €10.303,89 | €322,16 | 56 | 56 | 50,00% | 1,31 | €5,75 | 3,56% |
| TEST | Rapida V3 NoHigh — Range Only | Momentum / breakout V3 Filtered | €10.296,85 | €297,96 | 10 | 10 | 70,00% | 2,84 | €29,80 | 1,78% |
| TEST | MAIN — Dynamic Asset Selector | Confluenza trend | €10.284,81 | €286,48 | 7 | 7 | 57,14% | 3,51 | €40,93 | 1,06% |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | Momentum / breakout V3 Filtered | €10.274,60 | €305,90 | 31 | 31 | 58,06% | 1,75 | €9,87 | 2,51% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | Momentum / breakout V3 Filtered | €10.252,73 | €290,79 | 19 | 19 | 52,63% | 3,11 | €15,30 | 2,01% |
| TEST | Rapida V1 — senza PEPE | Momentum / breakout | €10.251,71 | €254,71 | 49 | 49 | 44,90% | 1,27 | €5,20 | 2,15% |
| TEST | Rapida V3 senza ESPORTS — Long Only | Momentum / breakout V3 Filtered | €10.236,96 | €205,14 | 28 | 28 | 46,43% | 1,49 | €7,33 | 1,61% |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | Momentum / breakout V3 Filtered | €10.235,71 | €236,97 | 14 | 14 | 57,14% | 4,59 | €16,93 | 1,01% |
| TEST | Combo Adaptive — Side × Regime Guard | Combo Adaptive | €10.234,44 | €227,65 | 17 | 17 | 70,59% | 2,03 | €13,39 | 1,41% |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | Momentum / breakout V3 Filtered | €10.227,50 | €213,49 | 24 | 24 | 45,83% | 1,60 | €8,90 | 2,97% |
| TEST | Combo Adaptive — madre | Combo Adaptive | €10.214,26 | €204,02 | 26 | 26 | 46,15% | 1,51 | €7,85 | 1,49% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €10.212,08 | €202,87 | 37 | 35 | 54,05% | 1,27 | €5,48 | 2,75% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | Momentum / breakout V3 Filtered | €10.205,44 | €209,95 | 21 | 21 | 42,86% | 1,70 | €10,00 | 2,27% |
| TEST | FAST NoHigh <7,5 · SHORT only | Momentum / breakout | €10.179,33 | €185,70 | 22 | 22 | 50,00% | 1,62 | €8,44 | 1,76% |
| TEST | Rapida 1H V3 Filtered — madre | Momentum / breakout V3 Filtered | €10.176,47 | €199,36 | 84 | 84 | 39,29% | 1,12 | €2,37 | 2,89% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.168,12 | €168,12 | 3 | 3 | 100,00% | ∞ | €56,04 | 0,54% |
| TEST | MAIN — Side × Regime Guard | Confluenza trend | €10.167,19 | €177,32 | 9 | 9 | 44,44% | 1,80 | €19,70 | 1,82% |
| TEST | Combo Adaptive — 75% a 2R + runner 25% a 3R | Combo Adaptive | €10.165,57 | €136,02 | 26 | 26 | 46,15% | 1,27 | €5,23 | 2,12% |
| TEST | Combo Adaptive — Quality7 | Combo Adaptive | €10.106,04 | €110,93 | 19 | 19 | 42,11% | 1,47 | €5,84 | 1,51% |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | Momentum / breakout V3 Filtered | €10.100,92 | €150,39 | 26 | 26 | 42,31% | 1,32 | €5,78 | 2,70% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €10.092,12 | €92,12 | 3 | 3 | 66,67% | 21,53 | €30,71 | 0,79% |
| TEST | Doge Ema 1H | Trend following EMA | €10.091,86 | €91,86 | 8 | 8 | 62,50% | 1,55 | €11,48 | 1,36% |
| TEST | Top 5 + BTC — target pieno 3R | Scanner Top 5 + forza BTC | €10.089,41 | €95,50 | 18 | 18 | 44,44% | 1,18 | €5,31 | 3,22% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €10.086,98 | €86,98 | 1 | 1 | 100,00% | ∞ | €86,98 | 0,40% |
| TEST | Combo Trend — Side × Regime Guard | Combo Trend | €10.085,02 | €119,75 | 18 | 18 | 50,00% | 1,43 | €6,65 | 1,73% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €10.084,30 | €53,21 | 44 | 43 | 40,91% | 1,04 | €1,21 | 5,10% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.084,12 | €84,12 | 1 | 1 | 100,00% | ∞ | €84,12 | 0,30% |
| TEST | Top 5 + BTC — 75% a 2,2R + runner 3R | Scanner Top 5 + forza BTC | €10.083,47 | €89,54 | 22 | 22 | 45,45% | 1,17 | €4,07 | 3,25% |
| TEST | Rapida V3 — qualità completa + profit lock | Momentum / breakout V3 Filtered | €10.077,50 | €82,40 | 47 | 47 | 48,94% | 1,08 | €1,75 | 3,21% |
| TEST | Rapida V3 senza ESPORTS — Stress Guard | Momentum / breakout V3 Filtered | €10.071,28 | €71,28 | 19 | 19 | 42,11% | 1,16 | €3,75 | 2,17% |
| TEST | Rapida V1 — Long + BTC 1–3 + score <7,5 | Momentum / breakout | €10.064,94 | €64,94 | 23 | 23 | 39,13% | 1,14 | €2,82 | 2,07% |
| TEST | Rapida 1H V1 — madre | Momentum / breakout | €10.048,63 | €51,31 | 77 | 77 | 35,06% | 1,03 | €0,67 | 6,76% |
| TEST | Ampia 4H | Confluenza trend | €10.042,28 | €29,34 | 19 | 19 | 26,32% | 1,05 | €1,54 | 3,68% |
| TEST | Combo Adaptive — Long Only | Combo Adaptive | €10.040,64 | €12,07 | 13 | 13 | 38,46% | 1,04 | €0,93 | 2,34% |
| TEST | Rapida V1 — target pieno 2R | Momentum / breakout | €10.024,29 | €46,18 | 56 | 56 | 35,71% | 1,04 | €0,82 | 2,58% |
| TEST | Top 5 + BTC — BTC 2–3 | Scanner Top 5 + forza BTC | €10.021,69 | €25,00 | 7 | 7 | 42,86% | 1,14 | €3,57 | 2,84% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €10.013,28 | €13,28 | 3 | 3 | 66,67% | 1,24 | €4,43 | 0,89% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €10.011,62 | €2,04 | 42 | 42 | 42,86% | 1,00 | €0,05 | 4,19% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €10.010,36 | €10,36 | 10 | 10 | 30,00% | 1,22 | €1,04 | 0,25% |
| TEST | Top 5 + BTC — BTC≤3 | Scanner Top 5 + forza BTC | €10.009,50 | €12,87 | 14 | 14 | 50,00% | 1,03 | €0,92 | 3,23% |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | Momentum / breakout V3 Filtered | €10.003,88 | €4,24 | 7 | 7 | 42,86% | 1,03 | €0,61 | 2,15% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €10.002,07 | €2,07 | 10 | 10 | 30,00% | 1,22 | €0,21 | 0,05% |
| TEST | Scalp RSI Short 85 · €50 · 15x | Inversione RSI estrema 15m | €10.000,61 | €0,61 | 2 | 2 | 50,00% | 1,74 | €0,30 | 0,07% |
| TEST | Scalp RSI Short 85 · €10 · 15x | Inversione RSI estrema 15m | €10.000,12 | €0,12 | 2 | 2 | 50,00% | 1,74 | €0,06 | 0,01% |
| TEST | Scanner Bottom5 Short Continuation V1 | Scanner Bottom5 Short Continuation | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 80 · €10 · 15x | Inversione RSI estrema 15m | €9.999,70 | €-0,30 | 3 | 3 | 66,67% | 0,63 | €-0,10 | 0,02% |
| TEST | Scalp RSI Long 20 · €10 · 15x | Inversione RSI estrema 15m | €9.998,96 | €-1,04 | 2 | 2 | 0,00% | 0,00 | €-0,52 | 0,02% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €9.998,95 | €-5,15 | 17 | 17 | 41,18% | 0,99 | €-0,30 | 2,31% |
| TEST | Scalp RSI Short 85 · prudente · 5x | Inversione RSI estrema 15m | €9.998,64 | €-1,36 | 2 | 2 | 50,00% | 0,42 | €-0,68 | 0,11% |
| TEST | Scalp RSI Short 80 · €50 · 15x | Inversione RSI estrema 15m | €9.998,52 | €-1,48 | 3 | 3 | 66,67% | 0,63 | €-0,49 | 0,09% |
| TEST | Scalp RSI Long 15 · €10 · 15x | Inversione RSI estrema 15m | €9.998,50 | €-1,50 | 1 | 1 | 0,00% | 0,00 | €-1,50 | 0,02% |
| TEST | Bilanciata 1H — SHORT Trend Down stretto | Confluenza trend | €9.995,87 | €-4,13 | 1 | 1 | 0,00% | 0,00 | €-4,13 | 0,59% |
| TEST | Scalp RSI Long 20 · €50 · 15x | Inversione RSI estrema 15m | €9.994,81 | €-5,19 | 2 | 2 | 0,00% | 0,00 | €-2,59 | 0,08% |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | €9.992,50 | €-7,50 | 1 | 1 | 0,00% | 0,00 | €-7,50 | 0,11% |
| TEST | Scalp RSI Long 25 · €10 · 15x | Inversione RSI estrema 15m | €9.991,12 | €-8,88 | 7 | 7 | 28,57% | 0,24 | €-1,27 | 0,12% |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | Momentum / breakout V3 Filtered | €9.990,65 | €-9,35 | 14 | 14 | 42,86% | 0,97 | €-0,67 | 2,46% |
| TEST | Scalp RSI Short 80 · prudente · 5x | Inversione RSI estrema 15m | €9.990,24 | €-9,76 | 3 | 3 | 66,67% | 0,28 | €-3,25 | 0,21% |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | €9.988,38 | €-11,62 | 1 | 1 | 0,00% | 0,00 | €-11,62 | 0,17% |
| TEST | Top 5 + BTC — Guard + BTC≤3 | Scanner Top 5 + forza BTC | €9.985,61 | €-11,10 | 13 | 13 | 46,15% | 0,98 | €-0,85 | 3,23% |
| TEST | Scalp RSI Long 20 · prudente · 5x | Inversione RSI estrema 15m | €9.983,60 | €-16,40 | 2 | 2 | 0,00% | 0,00 | €-8,20 | 0,24% |
| TEST | Donchian 1H Gb20 120R V1 | Donchian breakout 20 barre | €9.982,69 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 1,09% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €9.980,62 | €-19,38 | 4 | 4 | 50,00% | 0,82 | €-4,84 | 1,49% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €9.979,60 | €-17,71 | 16 | 14 | 43,75% | 0,95 | €-1,11 | 1,69% |
| TEST | Sol Ema 1H | Trend following EMA | €9.977,09 | €-22,91 | 5 | 5 | 40,00% | 0,86 | €-4,58 | 1,67% |
| TEST | Rapida V3 — Long + no HIGH + score <7,5 | Momentum / breakout V3 Filtered | €9.975,38 | €-19,76 | 42 | 42 | 42,86% | 0,98 | €-0,47 | 2,86% |
| TEST | Rapida V3 — senza ESPORTS | Momentum / breakout V3 Filtered | €9.969,25 | €-8,31 | 58 | 58 | 39,66% | 0,99 | €-0,14 | 2,49% |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | Scanner Bottom 5 Short | €9.961,03 | €-22,01 | 7 | 7 | 57,14% | 0,86 | €-3,14 | 1,38% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €9.959,98 | €-1,25 | 4 | 4 | 75,00% | 0,98 | €-0,31 | 1,08% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €9.959,49 | €-40,51 | 2 | 2 | 50,00% | 0,28 | €-20,26 | 0,91% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €9.955,61 | €-44,39 | 7 | 7 | 14,29% | 0,12 | €-6,34 | 0,58% |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | €9.955,59 | €-44,41 | 7 | 7 | 28,57% | 0,24 | €-6,34 | 0,58% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.951,70 | €-48,30 | 10 | 10 | 30,00% | 0,27 | €-4,83 | 0,58% |
| TEST | Btc Ema 4H | Trend following EMA | €9.950,68 | €-49,32 | 1 | 1 | 0,00% | 0,00 | €-49,32 | 0,96% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €9.950,68 | €-49,32 | 1 | 1 | 0,00% | 0,00 | €-49,32 | 0,96% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €9.949,62 | €-50,38 | 1 | 1 | 0,00% | 0,00 | €-50,38 | 0,74% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €9.947,16 | €-51,83 | 1 | 1 | 0,00% | 0,00 | €-51,83 | 0,77% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €9.946,90 | €-52,00 | 1 | 1 | 0,00% | 0,00 | €-52,00 | 0,79% |
| TEST | Bilanciata V3 · LONG only | Confluenza trend V3 Filtered | €9.943,76 | €-49,32 | 12 | 12 | 33,33% | 0,82 | €-4,11 | 1,46% |
| TEST | Eth Ema 4H | Trend following EMA | €9.941,53 | €-52,88 | 1 | 1 | 0,00% | 0,00 | €-52,88 | 0,96% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | Momentum / breakout V3 Filtered | €9.939,93 | €2,77 | 3 | 3 | 33,33% | 1,05 | €0,92 | 1,14% |
| TEST | Combo Adaptive — Quality7 + Regime + parziale 1R | Combo Adaptive | €9.936,41 | €-94,95 | 9 | 9 | 44,44% | 0,64 | €-10,55 | 1,95% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | Momentum / breakout V3 Filtered | €9.936,07 | €-77,54 | 25 | 25 | 40,00% | 0,85 | €-3,10 | 2,95% |
| TEST | Combo Adaptive — Trend/Transition | Combo Adaptive | €9.931,17 | €-80,62 | 19 | 19 | 47,37% | 0,82 | €-4,24 | 2,18% |
| TEST | Combo Adaptive — target pieno 3R | Combo Adaptive | €9.929,58 | €-66,67 | 13 | 13 | 46,15% | 0,76 | €-5,13 | 1,41% |
| TEST | Master Adaptive GB20 — Breakeven 0,5R | Master Adaptive Consensus | €9.928,46 | €-101,92 | 19 | 19 | 21,05% | 0,79 | €-5,36 | 3,15% |
| TEST | Btc Ema 1H | Trend following EMA | €9.911,86 | €-88,14 | 6 | 6 | 33,33% | 0,59 | €-14,69 | 1,56% |
| TEST | Scanner Bottom5 Short Profit Lock V1 | Scanner Bottom 5 Short | €9.909,51 | €-80,00 | 6 | 6 | 50,00% | 0,50 | €-13,33 | 1,53% |
| TEST | Rapida V3 — no volatilità HIGH | Momentum / breakout V3 Filtered | €9.904,92 | €-103,29 | 58 | 58 | 39,66% | 0,92 | €-1,78 | 2,96% |
| TEST | Bilanciata 1H — LONG senza Range High Vol | Confluenza trend | €9.902,43 | €-127,67 | 13 | 13 | 38,46% | 0,71 | €-9,82 | 2,47% |
| TEST | Combo Scanner | Combo Scanner | €9.901,71 | €-59,56 | 40 | 40 | 42,50% | 0,94 | €-1,49 | 3,25% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.901,25 | €-98,75 | 4 | 4 | 25,00% | 0,41 | €-24,69 | 1,89% |
| TEST | Sol Ema 4H | Trend following EMA | €9.896,31 | €-103,69 | 2 | 2 | 0,00% | 0,00 | €-51,84 | 1,06% |
| TEST | Master Adaptive GB20 — 50% a 0,75R | Master Adaptive Consensus | €9.895,55 | €-137,13 | 14 | 14 | 28,57% | 0,70 | €-9,79 | 2,50% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €9.888,87 | €-111,13 | 2 | 2 | 0,00% | 0,00 | €-55,56 | 1,26% |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | Momentum / breakout V3 Filtered | €9.882,17 | €-97,90 | 21 | 21 | 47,62% | 0,80 | €-4,66 | 3,08% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.871,99 | €-128,01 | 5 | 5 | 20,00% | 0,42 | €-25,60 | 1,62% |
| TEST | Master Adaptive GB20 — Loss Cap 0,75R | Master Adaptive Consensus | €9.870,03 | €-159,79 | 16 | 16 | 25,00% | 0,71 | €-9,99 | 3,63% |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | Momentum / breakout V3 Filtered | €9.855,29 | €-119,15 | 6 | 6 | 16,67% | 0,33 | €-19,86 | 1,99% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | Momentum / breakout V3 Filtered | €9.844,81 | €-168,22 | 21 | 21 | 42,86% | 0,65 | €-8,01 | 2,93% |
| TEST | Combo Adaptive — Quality7 + Regime | Combo Adaptive | €9.843,39 | €-187,67 | 9 | 9 | 33,33% | 0,32 | €-20,85 | 2,32% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €9.835,19 | €-164,81 | 6 | 6 | 33,33% | 0,29 | €-27,47 | 2,34% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | Momentum / breakout V3 Filtered | €9.800,72 | €-231,46 | 5 | 5 | 0,00% | 0,00 | €-46,29 | 2,20% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | Momentum / breakout V3 Filtered | €9.800,72 | €-231,46 | 5 | 5 | 0,00% | 0,00 | €-46,29 | 2,20% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.799,60 | €-200,40 | 6 | 6 | 33,33% | 0,08 | €-33,40 | 2,09% |
| TEST | Top 5 + BTC — Guard | Scanner Top 5 + forza BTC | €9.793,27 | €-238,06 | 20 | 20 | 30,00% | 0,65 | €-11,90 | 3,36% |
| TEST | Top 5 + BTC — solo MFE | Scanner Top 5 + forza BTC | €9.788,63 | €-221,32 | 25 | 25 | 40,00% | 0,59 | €-8,85 | 3,95% |
| TEST | Scanner Bottom10 Short | Scanner Bottom10 Short | €9.782,53 | €-206,23 | 7 | 7 | 28,57% | 0,25 | €-29,46 | 2,72% |
| TEST | Scanner Bottom15 Short | Scanner Bottom15 Short | €9.782,53 | €-206,23 | 7 | 7 | 28,57% | 0,25 | €-29,46 | 2,72% |
| TEST | Scanner Bottom20 Short | Scanner Bottom20 Short | €9.782,53 | €-206,23 | 7 | 7 | 28,57% | 0,25 | €-29,46 | 2,72% |
| TEST | Scanner Top10 Long | Scanner Top10 Long | €9.776,88 | €-215,85 | 15 | 15 | 40,00% | 0,53 | €-14,39 | 4,14% |
| TEST | Scanner Top15 Long | Scanner Top15 Long | €9.776,88 | €-215,85 | 15 | 15 | 40,00% | 0,53 | €-14,39 | 4,14% |
| TEST | Scanner Top20 Long | Scanner Top20 Long | €9.776,88 | €-215,85 | 15 | 15 | 40,00% | 0,53 | €-14,39 | 4,14% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.775,33 | €-234,50 | 31 | 31 | 35,48% | 0,71 | €-7,56 | 3,34% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.760,29 | €-209,34 | 10 | 10 | 30,00% | 0,37 | €-20,93 | 2,92% |
| TEST | Top 5 + BTC — Guard + BTC≤3 + MFE | Scanner Top 5 + forza BTC | €9.754,46 | €-242,91 | 28 | 28 | 42,86% | 0,70 | €-8,68 | 3,93% |
| TEST | Rapida V3 — Long Only | Momentum / breakout V3 Filtered | €9.753,54 | €-259,37 | 49 | 49 | 32,65% | 0,78 | €-5,29 | 3,67% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €9.736,70 | €-293,29 | 18 | 18 | 33,33% | 0,62 | €-16,29 | 3,64% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.736,61 | €-249,55 | 30 | 30 | 33,33% | 0,66 | €-8,32 | 5,48% |
| TEST | Eth Ema 1H | Trend following EMA | €9.727,87 | €-272,13 | 8 | 8 | 25,00% | 0,16 | €-34,02 | 2,76% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €9.724,42 | €-305,55 | 17 | 17 | 29,41% | 0,58 | €-17,97 | 3,98% |
| TEST | Combo Adaptive — parziale 1R | Combo Adaptive | €9.714,92 | €-296,40 | 23 | 23 | 39,13% | 0,52 | €-12,89 | 3,32% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €9.696,76 | €-333,13 | 15 | 15 | 26,67% | 0,53 | €-22,21 | 4,03% |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | €9.692,76 | €-337,11 | 15 | 15 | 26,67% | 0,53 | €-22,47 | 4,07% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €9.618,45 | €-374,57 | 50 | 50 | 58,00% | 0,59 | €-7,49 | 4,27% |
| TEST | Top 5 + BTC — Guard + MFE | Scanner Top 5 + forza BTC | €9.600,93 | €-411,13 | 35 | 35 | 37,14% | 0,58 | €-11,75 | 5,08% |
| TEST | Combo Adaptive — MFE Trail esistente | Combo Adaptive | €9.560,67 | €-426,65 | 33 | 33 | 30,30% | 0,49 | €-12,93 | 5,33% |
| TEST | Combo Trend | Combo Trend | €9.549,04 | €-447,67 | 44 | 44 | 31,82% | 0,72 | €-10,17 | 7,02% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €9.512,44 | €-481,54 | 23 | 23 | 26,09% | 0,54 | €-20,94 | 5,58% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €9.481,79 | €-495,46 | 35 | 35 | 25,71% | 0,54 | €-14,16 | 7,55% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | LAB | SHORT | Confluenza trend | 240m | 3,0x | 0,17841 | 0,17841 | 0,17841 | 0,23699 | 0,13559 | €136,26 | €408,77 | €0,00 | €-0,00 |
| Principale 4H | SUI | LONG | Confluenza trend | 240m | 3,0x | 0,76296 | 0,76296 | 0,73998 | 0,51245 | 0,80891 | €547,52 | €1.642,56 | €49,46 | €0,00 |
| Principale 4H | ONDO | LONG | Confluenza trend | 240m | 3,0x | 0,40344 | 0,40344 | 0,37762 | 0,27098 | 0,45509 | €254,70 | €764,09 | €48,91 | €0,00 |
| Principale 4H | SHIB | LONG | Confluenza trend | 240m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €8,88 | €26,63 | €2,22 | €-1,35 |
| Principale 4H | HYPE | SHORT | Confluenza trend | 240m | 3,0x | 57,27654 | 57,23300 | 59,33830 | 76,08234 | 53,15302 | €419,05 | €1.257,15 | €45,25 | €0,96 |
| Bilanciata 1H V1 | ADA | SHORT | Confluenza trend | 60m | 3,0x | 0,16703 | 0,16703 | 0,16365 | 0,22187 | 0,16112 | €978,72 | €2.936,17 | €0,00 | €-0,00 |
| Bilanciata 1H V1 | ALLO | SHORT | Confluenza trend | 60m | 3,0x | 0,36179 | 0,36179 | 0,40521 | 0,48058 | 0,27496 | €141,53 | €424,59 | €50,95 | €-0,00 |
| Bilanciata 1H V1 | AKE | LONG | Confluenza trend | 60m | 3,0x | 0,00443 | 0,00438 | 0,00389 | 0,00297 | 0,00549 | €141,56 | €424,68 | €50,96 | €-4,16 |
| Bilanciata 1H V1 | ZEC | SHORT | Confluenza trend | 60m | 3,0x | 483,74323 | 488,78000 | 494,91887 | 642,57226 | 461,39195 | €17,56 | €52,68 | €1,22 | €-0,55 |
| Bilanciata 1H V1 | XRP | SHORT | Confluenza trend | 60m | 3,0x | 1,09094 | 1,09160 | 1,10665 | 1,44913 | 1,05952 | €56,30 | €168,89 | €2,43 | €-0,10 |
| Bilanciata 1H V1 | HYPE | SHORT | Confluenza trend | 60m | 3,0x | 57,07858 | 57,23300 | 58,25281 | 75,81938 | 54,73013 | €786,25 | €2.358,74 | €48,52 | €-6,38 |
| Bilanciata 1H — LONG senza Range High Vol | BEAT | LONG | Confluenza trend | 60m | 3,0x | 3,29017 | 3,29017 | 3,00714 | 2,20990 | 3,85623 | €193,69 | €581,07 | €49,98 | €0,00 |
| Bilanciata 1H — LONG senza Range High Vol | XMR | LONG | Confluenza trend | 60m | 3,0x | 366,72991 | 366,72991 | 360,04130 | 246,32025 | 380,10712 | €915,26 | €2.745,79 | €50,08 | €0,00 |
| Bilanciata 1H — LONG senza Range High Vol | AKE | LONG | Confluenza trend | 60m | 3,0x | 0,00406 | 0,00438 | 0,00406 | 0,00273 | 0,00504 | €136,88 | €410,64 | €0,00 | €32,43 |
| Bilanciata 1H V2 | ADA | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,16276 | 0,16276 | 0,16511 | 0,21620 | 0,15807 | €1.185,56 | €3.556,68 | €51,22 | €-0,00 |
| Bilanciata 1H V2 | WLD | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,34349 | 0,34349 | 0,35287 | 0,45627 | 0,32475 | €26,53 | €79,60 | €2,17 | €-0,00 |
| Bilanciata 1H V2 | ALLO | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,35543 | 0,35543 | 0,39400 | 0,47213 | 0,27829 | €146,68 | €440,04 | €47,75 | €-0,00 |
| Bilanciata 1H V2 | AKE | LONG | Confluenza trend V2 | 60m | 3,0x | 0,00426 | 0,00438 | 0,00375 | 0,00286 | 0,00529 | €141,67 | €425,02 | €51,00 | €11,92 |
| Bilanciata 1H V3 Filtered | BEAT | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 3,31215 | 3,31215 | 3,02723 | 2,22466 | 3,88198 | €203,36 | €610,09 | €52,48 | €0,00 |
| Bilanciata 1H V3 Filtered | WLD | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,34349 | 0,34349 | 0,35287 | 0,45627 | 0,32475 | €23,43 | €70,29 | €1,92 | €-0,00 |
| Bilanciata 1H V3 Filtered | ALLO | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,34255 | 0,34255 | 0,37914 | 0,45502 | 0,26938 | €160,61 | €481,84 | €51,46 | €-0,00 |
| Bilanciata 1H V3 Filtered | ESPORTS | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,02905 | 0,02905 | 0,03254 | 0,03859 | 0,02208 | €142,96 | €428,87 | €51,46 | €-0,00 |
| Bilanciata 1H V3 Filtered | XRP | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 1,09094 | 1,09160 | 1,10665 | 1,44913 | 1,05952 | €1.210,12 | €3.630,37 | €52,28 | €-2,19 |
| Bilanciata 1H V3 Filtered | ZEC | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 488,51228 | 488,78000 | 499,98639 | 648,90714 | 465,56407 | €24,50 | €73,51 | €1,73 | €-0,04 |
| Rapida 1H V1 — madre | ADA | SHORT | Momentum / breakout | 60m | 3,0x | 0,16185 | 0,16185 | 0,16367 | 0,21499 | 0,15913 | €1.486,90 | €4.460,70 | €49,96 | €-0,00 |
| Rapida V1 — score 6–7,5 | ALLO | SHORT | Momentum / breakout | 60m | 3,0x | 0,33713 | 0,33713 | 0,36471 | 0,44782 | 0,29576 | €212,67 | €638,01 | €52,19 | €-0,00 |
| Rapida V1 — score 6–7,5 | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00443 | 0,00438 | 0,00389 | 0,00297 | 0,00522 | €144,83 | €434,48 | €52,14 | €-4,26 |
| Rapida V1 — score 6–7,5 | ZEC | SHORT | Momentum / breakout | 60m | 3,0x | 483,74323 | 488,78000 | 492,43540 | 642,57226 | 470,70499 | €972,21 | €2.916,64 | €52,41 | €-30,37 |
| Rapida V1 — score 6–7,5 | HYPE | SHORT | Momentum / breakout | 60m | 3,0x | 56,71366 | 57,23300 | 57,61702 | 75,33464 | 55,35861 | €1.094,57 | €3.283,72 | €52,30 | €-30,07 |
| Rapida score 6–7,5 — senza Trend Up | BEAT | LONG | Momentum / breakout | 60m | 3,0x | 3,29017 | 3,29017 | 3,07004 | 2,20990 | 3,62037 | €256,24 | €768,73 | €51,43 | €0,00 |
| Rapida score 6–7,5 — senza Trend Up | ALLO | SHORT | Momentum / breakout | 60m | 3,0x | 0,33808 | 0,33808 | 0,36389 | 0,44909 | 0,29937 | €218,91 | €656,73 | €50,14 | €-0,00 |
| Rapida score 6–7,5 — senza Trend Up | ZEC | SHORT | Momentum / breakout | 60m | 3,0x | 483,74323 | 488,78000 | 492,43540 | 642,57226 | 470,70499 | €961,25 | €2.883,74 | €51,82 | €-30,03 |
| Rapida score 6–7,5 — senza Trend Up | HYPE | SHORT | Momentum / breakout | 60m | 3,0x | 56,71366 | 57,23300 | 57,61702 | 75,33464 | 55,35861 | €1.083,98 | €3.251,95 | €51,80 | €-29,78 |
| Rapida score 6–7,5 — Range Only | BEAT | LONG | Momentum / breakout | 60m | 3,0x | 3,29017 | 3,29017 | 3,07004 | 2,20990 | 3,62037 | €256,24 | €768,73 | €51,43 | €0,00 |
| Rapida score 6–7,5 — Range Only | ESPORTS | SHORT | Momentum / breakout | 60m | 3,0x | 0,02828 | 0,02828 | 0,03168 | 0,03757 | 0,02319 | €143,01 | €429,04 | €51,48 | €-0,00 |
| Rapida score 6–7,5 — Cost Aware | ALLO | SHORT | Momentum / breakout | 60m | 3,0x | 0,33713 | 0,33713 | 0,36471 | 0,44782 | 0,29576 | €211,20 | €633,59 | €51,83 | €-0,00 |
| Rapida score 6–7,5 — Cost Aware | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00443 | 0,00438 | 0,00389 | 0,00297 | 0,00522 | €144,27 | €432,82 | €51,94 | €-4,24 |
| Rapida score 6–7,5 — Cost Aware | ZEC | SHORT | Momentum / breakout | 60m | 3,0x | 483,74323 | 488,78000 | 492,43540 | 642,57226 | 470,70499 | €968,54 | €2.905,63 | €52,21 | €-30,25 |
| Rapida score 6–7,5 — Cost Aware | HYPE | SHORT | Momentum / breakout | 60m | 3,0x | 56,71366 | 57,23300 | 57,61702 | 75,33464 | 55,35861 | €1.090,44 | €3.271,33 | €52,11 | €-29,96 |
| Rapida V1 — no HIGH + score <7,5 | BEAT | LONG | Momentum / breakout | 60m | 3,0x | 3,29017 | 3,29017 | 3,07004 | 2,20990 | 3,62037 | €257,44 | €772,31 | €51,67 | €0,00 |
| Rapida V1 — no HIGH + score <7,5 | ALLO | SHORT | Momentum / breakout | 60m | 3,0x | 0,33808 | 0,33808 | 0,36389 | 0,44909 | 0,29937 | €225,73 | €677,19 | €51,70 | €-0,00 |
| Rapida V1 — no HIGH + score <7,5 | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00443 | 0,00438 | 0,00389 | 0,00297 | 0,00522 | €146,54 | €439,61 | €52,75 | €-4,31 |
| Rapida V1 — senza PEPE | ADA | SHORT | Momentum / breakout | 60m | 3,0x | 0,16185 | 0,16185 | 0,16367 | 0,21499 | 0,15913 | €1.512,75 | €4.538,24 | €50,83 | €-0,00 |
| Rapida V1 — senza PEPE | WLD | SHORT | Momentum / breakout | 60m | 3,0x | 0,34959 | 0,34959 | 0,35668 | 0,46437 | 0,33896 | €838,72 | €2.516,16 | €51,00 | €-0,00 |
| Rapida V1 — senza PEPE | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00406 | 0,00438 | 0,00406 | 0,00273 | 0,00479 | €142,15 | €426,46 | €0,00 | €33,68 |
| Rapida V1 — senza PEPE | ZEC | SHORT | Momentum / breakout | 60m | 3,0x | 483,74323 | 488,78000 | 492,43540 | 642,57226 | 470,70499 | €28,82 | €86,46 | €1,55 | €-0,90 |
| Rapida V1 — senza PEPE | HYPE | SHORT | Momentum / breakout | 60m | 3,0x | 56,71366 | 57,23300 | 57,61702 | 75,33464 | 55,35861 | €1.064,33 | €3.192,99 | €50,86 | €-29,24 |
| Rapida V1 — target pieno 2R | ADA | SHORT | Momentum / breakout | 60m | 3,0x | 0,16185 | 0,16185 | 0,16367 | 0,21499 | 0,15823 | €1.482,83 | €4.448,49 | €49,82 | €-0,00 |
| Rapida V1 — target pieno 2R | WLD | SHORT | Momentum / breakout | 60m | 3,0x | 0,34959 | 0,34959 | 0,35668 | 0,46437 | 0,33542 | €42,01 | €126,02 | €2,55 | €-0,00 |
| Rapida V1 — target pieno 2R | ALLO | SHORT | Momentum / breakout | 60m | 3,0x | 0,35543 | 0,35543 | 0,38543 | 0,47213 | 0,29543 | €187,33 | €561,99 | €47,43 | €-0,00 |
| Rapida V1 — target pieno 2R | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00425 | 0,00438 | 0,00374 | 0,00286 | 0,00527 | €138,61 | €415,82 | €49,90 | €12,78 |
| Rapida V1 — target pieno 2R | ZEC | SHORT | Momentum / breakout | 60m | 3,0x | 483,74323 | 488,78000 | 492,43540 | 642,57226 | 466,35890 | €27,61 | €82,84 | €1,49 | €-0,86 |
| Rapida V1 — target pieno 2R | HYPE | SHORT | Momentum / breakout | 60m | 3,0x | 56,71366 | 57,23300 | 57,61702 | 75,33464 | 54,90694 | €1.039,45 | €3.118,34 | €49,67 | €-28,56 |
| Rapida 1H V2 | ADA | SHORT | Momentum / breakout V2 | 60m | 3,0x | 0,16185 | 0,16185 | 0,16367 | 0,21499 | 0,15913 | €1.494,54 | €4.483,63 | €50,22 | €-0,00 |
| Rapida 1H V3 Filtered — madre | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16185 | 0,16185 | 0,16367 | 0,21499 | 0,15913 | €1.521,20 | €4.563,60 | €51,11 | €-0,00 |
| Rapida 1H V3 Filtered — madre | WLD | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,34959 | 0,34959 | 0,35668 | 0,46437 | 0,33896 | €843,41 | €2.530,22 | €51,28 | €-0,00 |
| Rapida 1H V3 Filtered — madre | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00425 | 0,00438 | 0,00374 | 0,00286 | 0,00502 | €140,04 | €420,12 | €50,41 | €12,91 |
| Rapida 1H V3 Filtered — madre | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 483,74323 | 488,78000 | 492,43540 | 642,57226 | 470,70499 | €27,86 | €83,58 | €1,50 | €-0,87 |
| Rapida 1H V3 Filtered — madre | HYPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 56,71366 | 57,23300 | 57,61702 | 75,33464 | 55,35861 | €1.037,92 | €3.113,75 | €49,60 | €-28,51 |
| Rapida V3 — score <7,5 | BEAT | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 3,29017 | 3,29017 | 3,07004 | 2,20990 | 3,62037 | €258,77 | €776,32 | €51,94 | €0,00 |
| Rapida V3 — score <7,5 | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,33808 | 0,33808 | 0,36389 | 0,44909 | 0,29937 | €227,32 | €681,96 | €52,06 | €-0,00 |
| Rapida V3 — score <7,5 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00443 | 0,00438 | 0,00389 | 0,00297 | 0,00522 | €145,04 | €435,12 | €52,21 | €-4,26 |
| Rapida V3 — score <7,5 | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 483,74323 | 488,78000 | 492,43540 | 642,57226 | 470,70499 | €30,24 | €90,72 | €1,63 | €-0,94 |
| Rapida V3 — score <7,5 | HYPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 56,71366 | 57,23300 | 57,61702 | 75,33464 | 55,35861 | €1.087,88 | €3.263,64 | €51,98 | €-29,89 |
| Rapida V3 — no volatilità HIGH | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16185 | 0,16185 | 0,16367 | 0,21499 | 0,15913 | €1.485,86 | €4.457,58 | €49,92 | €-0,00 |
| Rapida V3 — no volatilità HIGH | WLD | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,34959 | 0,34959 | 0,35668 | 0,46437 | 0,33896 | €823,75 | €2.471,25 | €50,08 | €-0,00 |
| Rapida V3 — no volatilità HIGH | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00425 | 0,00438 | 0,00374 | 0,00286 | 0,00502 | €136,82 | €410,45 | €49,25 | €12,62 |
| Rapida V3 — Long Only | BEAT | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 3,29017 | 3,29017 | 3,07004 | 2,20990 | 3,62037 | €243,96 | €731,87 | €48,97 | €0,00 |
| Rapida V3 — Long Only | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00424 | 0,00438 | 0,00373 | 0,00285 | 0,00500 | €135,82 | €407,45 | €48,89 | €13,66 |
| Rapida V3 — Long + no HIGH + score <7,5 | BEAT | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 3,29017 | 3,29017 | 3,07004 | 2,20990 | 3,62037 | €246,62 | €739,85 | €49,50 | €0,00 |
| Rapida V3 — Long + no HIGH + score <7,5 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00443 | 0,00438 | 0,00389 | 0,00297 | 0,00522 | €138,70 | €416,10 | €49,93 | €-4,08 |
| Rapida V3 — senza ESPORTS | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16185 | 0,16185 | 0,16367 | 0,21499 | 0,15913 | €1.489,89 | €4.469,66 | €50,06 | €-0,00 |
| Rapida V3 — senza ESPORTS | WLD | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,34959 | 0,34959 | 0,35668 | 0,46437 | 0,33896 | €825,98 | €2.477,95 | €50,22 | €-0,00 |
| Rapida V3 — senza ESPORTS | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00425 | 0,00438 | 0,00374 | 0,00286 | 0,00502 | €137,19 | €411,57 | €49,39 | €12,65 |
| Rapida V3 — senza ESPORTS | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 483,74323 | 488,78000 | 492,43540 | 642,57226 | 470,70499 | €27,30 | €81,91 | €1,47 | €-0,85 |
| Rapida V3 — senza ESPORTS | HYPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 56,71366 | 57,23300 | 57,61702 | 75,33464 | 55,35861 | €1.017,33 | €3.051,98 | €48,61 | €-27,95 |
| Rapida V3 senza ESPORTS — Long Only | BEAT | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 3,29017 | 3,29017 | 3,07004 | 2,20990 | 3,62037 | €248,78 | €746,34 | €49,93 | €0,00 |
| Rapida V3 senza ESPORTS — Long Only | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00406 | 0,00438 | 0,00406 | 0,00273 | 0,00479 | €137,56 | €412,67 | €0,00 | €32,59 |
| Rapida V3 senza ESPORTS — MFE Lock | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16185 | 0,16185 | 0,16367 | 0,21499 | 0,15913 | €1.510,84 | €4.532,53 | €50,76 | €-0,00 |
| Rapida V3 senza ESPORTS — MFE Lock | WLD | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,34959 | 0,34959 | 0,35668 | 0,46437 | 0,33896 | €11,86 | €35,57 | €0,72 | €-0,00 |
| Rapida V3 senza ESPORTS — MFE Lock | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,33165 | 0,33165 | 0,36472 | 0,44055 | 0,28205 | €170,96 | €512,89 | €51,14 | €-0,00 |
| Rapida V3 senza ESPORTS — MFE Lock | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00425 | 0,00438 | 0,00374 | 0,00286 | 0,00502 | €142,50 | €427,49 | €51,30 | €13,14 |
| Rapida V3 senza ESPORTS — MFE Lock | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 483,74323 | 488,78000 | 492,43540 | 642,57226 | 470,70499 | €28,65 | €85,95 | €1,54 | €-0,89 |
| Rapida V3 senza ESPORTS — MFE Lock | HYPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 56,71366 | 57,23300 | 57,61702 | 75,33464 | 55,35861 | €1.074,29 | €3.222,88 | €51,34 | €-29,51 |
| Rapida V3 — qualità completa + profit lock | BEAT | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 3,29017 | 3,29017 | 3,07004 | 2,20990 | 3,62037 | €245,16 | €735,47 | €49,21 | €0,00 |
| Rapida V3 — qualità completa + profit lock | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00443 | 0,00438 | 0,00389 | 0,00297 | 0,00522 | €139,96 | €419,87 | €50,38 | €-4,11 |
| Ampia 4H | HYPE | SHORT | Confluenza trend | 240m | 2,0x | 58,36732 | 57,23300 | 61,80927 | 87,25915 | 48,72988 | €424,03 | €848,06 | €50,01 | €16,48 |
| Ampia 4H | TAO | SHORT | Confluenza trend | 240m | 2,0x | 189,05650 | 189,05650 | 197,51338 | 282,63946 | 165,37722 | €558,68 | €1.117,36 | €49,98 | €-0,00 |
| Ampia 4H | XMR | LONG | Confluenza trend | 240m | 2,0x | 364,45854 | 364,45854 | 347,94701 | 184,05156 | 410,69083 | €544,42 | €1.088,84 | €49,33 | €0,00 |
| Ampia 4H | ETH | LONG | Confluenza trend | 240m | 2,0x | 1964,80288 | 1945,93000 | 1907,44021 | 992,22546 | 2125,41837 | €27,31 | €54,62 | €1,59 | €-0,52 |
| Ampia 4H | AKE | LONG | Confluenza trend | 240m | 2,0x | 0,00440 | 0,00438 | 0,00387 | 0,00222 | 0,00587 | €204,84 | €409,68 | €49,16 | €-1,28 |
| Forza relativa 1H V1 | NIGHT | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,02031 | 0,02031 | 0,02210 | 0,03036 | 0,01637 | €285,91 | €571,83 | €50,45 | €-0,00 |
| Forza relativa 1H V1 | ONDO | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,42171 | €891,90 | €1.783,80 | €49,29 | €0,00 |
| Forza relativa 1H V1 | WLD | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,32287 | €14,97 | €29,93 | €0,82 | €-0,00 |
| Forza relativa 1H V1 | AKE | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,00424 | 0,00438 | 0,00373 | 0,00214 | 0,00536 | €15,28 | €30,56 | €3,67 | €1,02 |
| Forza relativa 1H V1 | ZEC | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 483,74323 | 488,78000 | 494,91887 | 723,19613 | 459,15682 | €1.028,52 | €2.057,03 | €47,52 | €-21,42 |
| Forza relativa 1H V1 | HYPE | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 57,27654 | 57,23300 | 58,35818 | 85,62843 | 54,89695 | €1.014,19 | €2.028,38 | €38,30 | €1,54 |
| Forza relativa 1H V2 | WLD | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,32287 | €47,70 | €95,39 | €2,60 | €-0,00 |
| Forza relativa 1H V2 | XMR | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 367,08012 | 367,08012 | 360,46822 | 185,37546 | 381,62629 | €1.446,12 | €2.892,24 | €52,10 | €0,00 |
| Forza relativa 1H V2 | AKE | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,00406 | 0,00438 | 0,00406 | 0,00205 | 0,00513 | €210,28 | €420,56 | €0,00 | €33,22 |
| Benchmark Donchian breakout 1H | SUI | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,76606 | 0,76606 | 0,75182 | 0,38686 | 0,80165 | €1.377,00 | €2.754,00 | €51,18 | €0,00 |
| Benchmark Donchian breakout 1H | ALLO | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,35678 | 0,35678 | 0,39959 | 0,53338 | 0,24974 | €215,19 | €430,38 | €51,65 | €-0,00 |
| Benchmark Donchian breakout 1H | HYPE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 58,25535 | 57,23300 | 57,44554 | 87,09174 | 55,41491 | €1.364,10 | €2.728,20 | €0,00 | €47,88 |
| Benchmark Donchian breakout 1H | XRP | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 1,08939 | 1,09160 | 1,10682 | 1,62864 | 1,04582 | €1.662,45 | €3.324,89 | €53,20 | €-6,74 |
| Benchmark Donchian breakout 1H | DOGE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,07141 | 0,07208 | 0,07256 | 0,10675 | 0,06852 | €108,24 | €216,47 | €3,50 | €-2,04 |
| Benchmark Donchian breakout 1H | ZEC | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 483,74323 | 488,78000 | 496,16061 | 723,19613 | 452,69979 | €19,59 | €39,18 | €1,01 | €-0,41 |
| Donchian 1H Gb20 120R V1 | HYPE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 58,25535 | 57,23300 | 57,44554 | 87,09174 | 55,41491 | €1.281,83 | €2.563,66 | €0,00 | €44,99 |
| Donchian 1H Gb20 120R V1 | XRP | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 1,08939 | 1,09160 | 1,10682 | 1,62864 | 1,04582 | €1.562,18 | €3.124,36 | €49,99 | €-6,33 |
| Donchian 1H Gb20 120R V1 | DOGE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,07141 | 0,07208 | 0,07256 | 0,10675 | 0,06852 | €1.543,86 | €3.087,72 | €49,98 | €-29,16 |
| Donchian 1H Gb20 120R V1 | ZEC | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 483,74323 | 488,78000 | 496,16061 | 723,19613 | 452,69979 | €978,17 | €1.956,34 | €50,22 | €-20,37 |
| Benchmark Bollinger mean reversion 1H | AKE | SHORT | Bollinger mean reversion | 60m | 2,0x | 0,00424 | 0,00438 | 0,00475 | 0,00634 | 0,00348 | €208,14 | €416,27 | €49,95 | €-14,12 |
| Benchmark Bollinger mean reversion 1H | HYPE | LONG | Bollinger mean reversion | 60m | 2,0x | 56,73635 | 57,23300 | 55,76807 | 28,65185 | 58,18875 | €1.464,84 | €2.929,68 | €50,00 | €25,65 |
| Benchmark trend following EMA 1H | LAB | LONG | Trend following EMA | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €207,05 | €414,10 | €49,69 | €0,00 |
| Benchmark trend following EMA 1H | ALLO | SHORT | Trend following EMA | 60m | 2,0x | 0,35372 | 0,35372 | 0,39616 | 0,52881 | 0,26034 | €209,15 | €418,30 | €50,20 | €-0,00 |
| Benchmark trend following EMA 1H | XMR | LONG | Trend following EMA | 60m | 2,0x | 367,08012 | 367,08012 | 359,73357 | 185,37546 | 383,24253 | €17,91 | €35,83 | €0,72 | €0,00 |
| Benchmark trend following EMA 1H | AKE | LONG | Trend following EMA | 60m | 2,0x | 0,00426 | 0,00438 | 0,00375 | 0,00215 | 0,00539 | €203,42 | €406,84 | €48,82 | €11,41 |
| Benchmark trend following EMA 1H | XRP | SHORT | Trend following EMA | 60m | 2,0x | 1,09230 | 1,09160 | 1,10978 | 1,63299 | 1,05385 | €1.438,76 | €2.877,52 | €46,04 | €1,85 |
| Scanner Top 5 Long 1H | XMR | LONG | Scanner Top 5 Long | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10712 | €70,71 | €141,42 | €2,58 | €0,00 |
| Scanner Top 5 Long 1H | AKE | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,00406 | 0,00438 | 0,00406 | 0,00205 | 0,00504 | €216,04 | €432,09 | €0,00 | €34,13 |
| Scanner Bottom 5 Short 1H | ADA | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,16703 | 0,16703 | 0,16365 | 0,24971 | 0,16112 | €1.381,07 | €2.762,13 | €0,00 | €-0,00 |
| Scanner Bottom 5 Short 1H | ALLO | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,36179 | 0,36179 | 0,40521 | 0,54088 | 0,27496 | €202,53 | €405,06 | €48,61 | €-0,00 |
| Scanner Bottom 5 Short 1H | ESPORTS | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,03342 | 0,03342 | 0,03342 | 0,04997 | 0,02540 | €202,66 | €405,32 | €0,00 | €-0,00 |
| Scanner Bottom 5 Short 1H | ZEC | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 483,74323 | 488,78000 | 494,91887 | 723,19613 | 461,39195 | €18,93 | €37,87 | €0,87 | €-0,39 |
| Scanner Bottom 5 Short 1H | XRP | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1,09094 | 1,09160 | 1,10665 | 1,63096 | 1,05952 | €18,20 | €36,40 | €0,52 | €-0,02 |
| Scanner Bottom 5 Short 1H | HYPE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 57,07858 | 57,23300 | 58,25281 | 85,33248 | 54,73013 | €1.150,85 | €2.301,70 | €47,35 | €-6,23 |
| Scanner Top10 Long | XMR | LONG | Scanner Top10 Long | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10712 | €1.371,36 | €2.742,71 | €50,02 | €0,00 |
| Scanner Top10 Long | SHIB | LONG | Scanner Top10 Long | 60m | 2,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €24,14 | €48,29 | €2,71 | €-1,24 |
| Scanner Top10 Long | AKE | LONG | Scanner Top10 Long | 60m | 2,0x | 0,00443 | 0,00438 | 0,00389 | 0,00224 | 0,00549 | €204,92 | €409,85 | €49,18 | €-4,01 |
| Scanner Bottom10 Short | ADA | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,16193 | 0,16193 | 0,16426 | 0,24209 | 0,15727 | €1.731,26 | €3.462,51 | €49,86 | €-0,00 |
| Scanner Bottom10 Short | ALLO | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,35250 | 0,35250 | 0,39075 | 0,52699 | 0,27600 | €224,69 | €449,38 | €48,76 | €-0,00 |
| Scanner Bottom10 Short | ESPORTS | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,03342 | 0,03342 | 0,03342 | 0,04997 | 0,02540 | €203,44 | €406,87 | €0,00 | €-0,00 |
| Scanner Bottom10 Short | ZEC | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 483,74323 | 488,78000 | 494,91887 | 723,19613 | 461,39195 | €18,78 | €37,56 | €0,87 | €-0,39 |
| Scanner Bottom10 Short | XRP | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 1,09094 | 1,09160 | 1,10665 | 1,63096 | 1,05952 | €18,05 | €36,11 | €0,52 | €-0,02 |
| Scanner Bottom10 Short | HYPE | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 57,07858 | 57,23300 | 58,25281 | 85,33248 | 54,73013 | €1.141,57 | €2.283,13 | €46,97 | €-6,18 |
| Scanner Top15 Long | XMR | LONG | Scanner Top15 Long | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10712 | €1.371,36 | €2.742,71 | €50,02 | €0,00 |
| Scanner Top15 Long | SHIB | LONG | Scanner Top15 Long | 60m | 2,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €24,14 | €48,29 | €2,71 | €-1,24 |
| Scanner Top15 Long | AKE | LONG | Scanner Top15 Long | 60m | 2,0x | 0,00443 | 0,00438 | 0,00389 | 0,00224 | 0,00549 | €204,92 | €409,85 | €49,18 | €-4,01 |
| Scanner Bottom15 Short | ADA | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,16193 | 0,16193 | 0,16426 | 0,24209 | 0,15727 | €1.731,26 | €3.462,51 | €49,86 | €-0,00 |
| Scanner Bottom15 Short | ALLO | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,35250 | 0,35250 | 0,39075 | 0,52699 | 0,27600 | €224,69 | €449,38 | €48,76 | €-0,00 |
| Scanner Bottom15 Short | ESPORTS | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,03342 | 0,03342 | 0,03342 | 0,04997 | 0,02540 | €203,44 | €406,87 | €0,00 | €-0,00 |
| Scanner Bottom15 Short | ZEC | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 483,74323 | 488,78000 | 494,91887 | 723,19613 | 461,39195 | €18,78 | €37,56 | €0,87 | €-0,39 |
| Scanner Bottom15 Short | XRP | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 1,09094 | 1,09160 | 1,10665 | 1,63096 | 1,05952 | €18,05 | €36,11 | €0,52 | €-0,02 |
| Scanner Bottom15 Short | HYPE | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 57,07858 | 57,23300 | 58,25281 | 85,33248 | 54,73013 | €1.141,57 | €2.283,13 | €46,97 | €-6,18 |
| Scanner Top20 Long | XMR | LONG | Scanner Top20 Long | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10712 | €1.371,36 | €2.742,71 | €50,02 | €0,00 |
| Scanner Top20 Long | SHIB | LONG | Scanner Top20 Long | 60m | 2,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €24,14 | €48,29 | €2,71 | €-1,24 |
| Scanner Top20 Long | AKE | LONG | Scanner Top20 Long | 60m | 2,0x | 0,00443 | 0,00438 | 0,00389 | 0,00224 | 0,00549 | €204,92 | €409,85 | €49,18 | €-4,01 |
| Scanner Bottom20 Short | ADA | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,16193 | 0,16193 | 0,16426 | 0,24209 | 0,15727 | €1.731,26 | €3.462,51 | €49,86 | €-0,00 |
| Scanner Bottom20 Short | ALLO | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,35250 | 0,35250 | 0,39075 | 0,52699 | 0,27600 | €224,69 | €449,38 | €48,76 | €-0,00 |
| Scanner Bottom20 Short | ESPORTS | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,03342 | 0,03342 | 0,03342 | 0,04997 | 0,02540 | €203,44 | €406,87 | €0,00 | €-0,00 |
| Scanner Bottom20 Short | ZEC | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 483,74323 | 488,78000 | 494,91887 | 723,19613 | 461,39195 | €18,78 | €37,56 | €0,87 | €-0,39 |
| Scanner Bottom20 Short | XRP | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 1,09094 | 1,09160 | 1,10665 | 1,63096 | 1,05952 | €18,05 | €36,11 | €0,52 | €-0,02 |
| Scanner Bottom20 Short | HYPE | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 57,07858 | 57,23300 | 58,25281 | 85,33248 | 54,73013 | €1.141,57 | €2.283,13 | €46,97 | €-6,18 |
| Scanner Top 5 + forza BTC 1H | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39694 | 0,39694 | 0,38539 | 0,20045 | 0,42235 | €898,57 | €1.797,15 | €52,29 | €0,00 |
| Scanner Top 5 + forza BTC 1H | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €216,56 | €433,12 | €51,97 | €0,00 |
| Scanner Top 5 + forza BTC 1H | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 381,44484 | €37,16 | €74,32 | €1,36 | €0,00 |
| Scanner Top 5 + forza BTC 1H | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00406 | 0,00438 | 0,00406 | 0,00205 | 0,00513 | €216,37 | €432,74 | €0,00 | €34,18 |
| Top 5 + BTC — solo MFE | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39924 | 0,39924 | 0,38729 | 0,20162 | 0,42552 | €835,46 | €1.670,91 | €50,00 | €0,00 |
| Top 5 + BTC — solo MFE | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 367,08012 | 367,08012 | 360,46822 | 185,37546 | 381,62629 | €1.363,71 | €2.727,43 | €49,13 | €0,00 |
| Top 5 + BTC — solo MFE | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00425 | 0,00438 | 0,00374 | 0,00215 | 0,00537 | €203,68 | €407,36 | €48,88 | €12,52 |
| Top 5 + BTC — Guard | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €202,47 | €404,95 | €48,59 | €0,00 |
| Top 5 + BTC — Guard | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00406 | 0,00438 | 0,00406 | 0,00205 | 0,00513 | €204,25 | €408,50 | €0,00 | €32,26 |
| Top 5 + BTC — BTC≤3 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39974 | 0,39974 | 0,38840 | 0,20187 | 0,42468 | €884,65 | €1.769,29 | €50,18 | €0,00 |
| Top 5 + BTC — BTC≤3 | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €207,87 | €415,74 | €49,89 | €0,00 |
| Top 5 + BTC — BTC≤3 | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 381,44484 | €37,63 | €75,26 | €1,37 | €0,00 |
| Top 5 + BTC — BTC≤3 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00440 | 0,00438 | 0,00387 | 0,00222 | 0,00556 | €209,03 | €418,06 | €50,17 | €-1,31 |
| Top 5 + BTC — BTC 2–3 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39974 | 0,39974 | 0,38840 | 0,20187 | 0,42468 | €884,65 | €1.769,29 | €50,18 | €0,00 |
| Top 5 + BTC — BTC 2–3 | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €207,87 | €415,74 | €49,89 | €0,00 |
| Top 5 + BTC — BTC 2–3 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00440 | 0,00438 | 0,00387 | 0,00222 | 0,00556 | €208,82 | €417,64 | €50,12 | €-1,31 |
| Top 5 + BTC — Guard + MFE | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00425 | 0,00438 | 0,00374 | 0,00215 | 0,00537 | €200,07 | €400,14 | €48,02 | €12,30 |
| Top 5 + BTC — Guard + BTC≤3 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39974 | 0,39974 | 0,38840 | 0,20187 | 0,42468 | €871,05 | €1.742,11 | €49,41 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €205,84 | €411,68 | €49,40 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00440 | 0,00438 | 0,00387 | 0,00222 | 0,00556 | €208,07 | €416,13 | €49,94 | €-1,30 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39974 | 0,39974 | 0,38840 | 0,20187 | 0,42468 | €871,05 | €1.742,11 | €49,41 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00440 | 0,00438 | 0,00387 | 0,00222 | 0,00556 | €203,53 | €407,07 | €48,85 | €-1,27 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39694 | 0,39694 | 0,38539 | 0,20045 | 0,43159 | €861,83 | €1.723,66 | €50,15 | €0,00 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,21338 | €207,96 | €415,92 | €49,91 | €0,00 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 386,79573 | €70,70 | €141,40 | €2,58 | €0,00 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00443 | 0,00438 | 0,00389 | 0,00224 | 0,00602 | €208,49 | €416,98 | €50,04 | €-4,08 |
| Top 5 + BTC — target pieno 3R | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39694 | 0,39694 | 0,38539 | 0,20045 | 0,43159 | €861,83 | €1.723,66 | €50,15 | €0,00 |
| Top 5 + BTC — target pieno 3R | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,21338 | €207,96 | €415,92 | €49,91 | €0,00 |
| Top 5 + BTC — target pieno 3R | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 386,79573 | €85,15 | €170,29 | €3,11 | €0,00 |
| Top 5 + BTC — target pieno 3R | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00443 | 0,00438 | 0,00389 | 0,00224 | 0,00602 | €208,62 | €417,24 | €50,07 | €-4,09 |
| Global Confluence puro 1H | DOGE | SHORT | Global Confluence puro | 60m | 2,0x | 0,07141 | 0,07208 | 0,07256 | 0,10675 | 0,06852 | €1.512,23 | €3.024,45 | €48,95 | €-28,56 |
| Combo Trend | ALLO | SHORT | Combo Trend | 60m | 2,0x | 0,35372 | 0,35372 | 0,39616 | 0,52881 | 0,26034 | €209,35 | €418,70 | €50,24 | €-0,00 |
| Combo Trend | AKE | LONG | Combo Trend | 60m | 2,0x | 0,00406 | 0,00438 | 0,00406 | 0,00205 | 0,00513 | €180,00 | €360,01 | €0,00 | €28,43 |
| Combo Trend | DOGE | SHORT | Combo Trend | 60m | 2,0x | 0,07141 | 0,07208 | 0,07256 | 0,10675 | 0,06886 | €1.482,27 | €2.964,54 | €47,98 | €-27,99 |
| Combo Trend | HYPE | SHORT | Combo Trend | 60m | 2,0x | 58,25535 | 57,23300 | 57,39038 | 87,09174 | 55,75576 | €77,88 | €155,76 | €0,00 | €2,73 |
| Combo Trend | XRP | SHORT | Combo Trend | 60m | 2,0x | 1,09094 | 1,09160 | 1,10840 | 1,63096 | 1,05254 | €1.454,27 | €2.908,55 | €46,54 | €-1,75 |
| Combo Mean Reversion | XRP | LONG | Combo Mean Reversion | 60m | 2,0x | 1,08983 | 1,09160 | 1,07675 | 0,55036 | 1,11075 | €1.998,97 | €3.997,94 | €47,98 | €6,50 |
| Combo Scanner | ONDO | LONG | Combo Scanner | 60m | 2,0x | 0,39694 | 0,39694 | 0,38539 | 0,20045 | 0,42235 | €857,88 | €1.715,77 | €49,92 | €0,00 |
| Combo Scanner | LAB | LONG | Combo Scanner | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €207,54 | €415,08 | €49,81 | €0,00 |
| Combo Scanner | XMR | LONG | Combo Scanner | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 381,44484 | €23,89 | €47,78 | €0,87 | €0,00 |
| Combo Scanner | AKE | LONG | Combo Scanner | 60m | 2,0x | 0,00443 | 0,00438 | 0,00389 | 0,00224 | 0,00559 | €205,41 | €410,83 | €49,30 | €-4,02 |
| Combo Scanner | DOGE | SHORT | Combo Scanner | 60m | 2,0x | 0,07141 | 0,07208 | 0,07245 | 0,10675 | 0,06912 | €1.631,78 | €3.263,56 | €47,54 | €-30,82 |
| Combo Adaptive — madre | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15861 | 0,13958 | 0,08010 | 0,19668 | €213,13 | €426,26 | €51,15 | €0,00 |
| Combo Adaptive — madre | WLD | SHORT | Combo Adaptive | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,32475 | €929,60 | €1.859,20 | €50,73 | €-0,00 |
| Combo Adaptive — madre | ALLO | SHORT | Combo Adaptive | 60m | 2,0x | 0,36179 | 0,36179 | 0,40521 | 0,54088 | 0,27496 | €210,64 | €421,27 | €50,55 | €-0,00 |
| Combo Adaptive — madre | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,00425 | 0,00438 | 0,00374 | 0,00215 | 0,00527 | €212,53 | €425,05 | €51,01 | €13,41 |
| Combo Adaptive — madre | HYPE | SHORT | Combo Adaptive | 60m | 2,0x | 56,91461 | 57,23300 | 58,08547 | 85,08735 | 54,57291 | €13,99 | €27,97 | €0,58 | €-0,16 |
| Combo Adaptive — MFE Trail esistente | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15861 | 0,13958 | 0,08010 | 0,19668 | €201,70 | €403,39 | €48,41 | €0,00 |
| Combo Adaptive — MFE Trail esistente | WLD | SHORT | Combo Adaptive | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,32475 | €883,78 | €1.767,56 | €48,23 | €-0,00 |
| Combo Adaptive — MFE Trail esistente | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,00425 | 0,00438 | 0,00374 | 0,00215 | 0,00527 | €193,67 | €387,34 | €46,48 | €11,91 |
| Combo Adaptive — MFE Trail esistente | HYPE | SHORT | Combo Adaptive | 60m | 2,0x | 56,71366 | 57,23300 | 57,87512 | 84,78691 | 54,39073 | €1.168,54 | €2.337,08 | €47,86 | €-21,40 |
| Combo Adaptive — MFE Trail esistente | XRP | SHORT | Combo Adaptive | 60m | 2,0x | 1,09094 | 1,09160 | 1,10665 | 1,63096 | 1,05952 | €14,86 | €29,71 | €0,43 | €-0,02 |
| Combo Adaptive — Quality7 | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,40304 | 0,40304 | 0,39140 | 0,20354 | 0,42632 | €859,15 | €1.718,30 | €49,62 | €0,00 |
| Combo Adaptive — Quality7 | WLD | SHORT | Combo Adaptive | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,32475 | €919,99 | €1.839,97 | €50,21 | €-0,00 |
| Combo Adaptive — Quality7 | ALLO | SHORT | Combo Adaptive | 60m | 2,0x | 0,36179 | 0,36179 | 0,40521 | 0,54088 | 0,27496 | €207,61 | €415,23 | €49,83 | €-0,00 |
| Combo Adaptive — Quality7 | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,00440 | 0,00438 | 0,00387 | 0,00222 | 0,00545 | €210,58 | €421,15 | €50,54 | €-1,32 |
| Combo Adaptive — Trend/Transition | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15861 | 0,13958 | 0,08010 | 0,19668 | €206,52 | €413,04 | €49,56 | €0,00 |
| Combo Adaptive — Trend/Transition | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,00424 | 0,00438 | 0,00373 | 0,00214 | 0,00526 | €200,45 | €400,89 | €48,11 | €13,44 |
| Combo Adaptive — Trend/Transition | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,07141 | 0,07208 | 0,07245 | 0,10675 | 0,06933 | €43,33 | €86,66 | €1,26 | €-0,82 |
| Combo Adaptive — Quality7 + Regime | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,40554 | 0,40554 | 0,39390 | 0,20480 | 0,42882 | €864,27 | €1.728,54 | €49,61 | €0,00 |
| Combo Adaptive — Quality7 + Regime | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,00406 | 0,00438 | 0,00406 | 0,00205 | 0,00504 | €205,26 | €410,51 | €0,00 | €32,42 |
| Combo Adaptive — Long Only | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,41951 | €893,67 | €1.787,34 | €49,39 | €0,00 |
| Combo Adaptive — Long Only | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €205,55 | €411,10 | €49,33 | €0,00 |
| Combo Adaptive — Long Only | XMR | LONG | Combo Adaptive | 60m | 2,0x | 367,08012 | 367,08012 | 360,46822 | 185,37546 | 380,30391 | €1.384,19 | €2.768,37 | €49,86 | €0,00 |
| Combo Adaptive — Long Only | SHIB | LONG | Combo Adaptive | 60m | 2,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €12,85 | €25,69 | €1,44 | €-0,66 |
| Combo Adaptive — Long Only | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,00406 | 0,00438 | 0,00406 | 0,00205 | 0,00504 | €208,51 | €417,03 | €0,00 | €32,94 |
| Combo Adaptive — parziale 1R | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,41951 | €893,02 | €1.786,04 | €49,36 | €0,00 |
| Combo Adaptive — parziale 1R | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €205,22 | €410,44 | €49,25 | €0,00 |
| Combo Adaptive — parziale 1R | WLD | SHORT | Combo Adaptive | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,32475 | €895,30 | €1.790,60 | €48,86 | €-0,00 |
| Combo Adaptive — parziale 1R | ALLO | SHORT | Combo Adaptive | 60m | 2,0x | 0,36179 | 0,36179 | 0,40521 | 0,54088 | 0,27496 | €98,69 | €197,38 | €23,69 | €-0,00 |
| Combo Adaptive — parziale 1R | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,00406 | 0,00438 | 0,00406 | 0,00205 | 0,00504 | €93,51 | €187,03 | €0,00 | €14,77 |
| Combo Adaptive — parziale 1R | XRP | SHORT | Combo Adaptive | 60m | 2,0x | 1,09194 | 1,09160 | 1,10767 | 1,63245 | 1,06049 | €20,02 | €40,04 | €0,58 | €0,01 |
| Combo Adaptive — Quality7 + Regime + parziale 1R | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,40554 | 0,40554 | 0,39390 | 0,20480 | 0,42882 | €864,27 | €1.728,54 | €49,61 | €0,00 |
| Combo Adaptive — Quality7 + Regime + parziale 1R | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,00406 | 0,00438 | 0,00406 | 0,00205 | 0,00504 | €207,20 | €414,39 | €0,00 | €32,73 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,43050 | €902,18 | €1.804,37 | €49,86 | €0,00 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | WLD | SHORT | Combo Adaptive | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,31537 | €919,67 | €1.839,35 | €50,19 | €-0,00 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | XMR | LONG | Combo Adaptive | 60m | 2,0x | 367,08012 | 367,08012 | 360,46822 | 185,37546 | 386,91580 | €27,35 | €54,70 | €0,99 | €0,00 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | ALLO | SHORT | Combo Adaptive | 60m | 2,0x | 0,36179 | 0,36179 | 0,40521 | 0,54088 | 0,23155 | €207,78 | €415,57 | €49,87 | €-0,00 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,00406 | 0,00438 | 0,00406 | 0,00205 | 0,00552 | €210,79 | €421,58 | €0,00 | €33,30 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | ZEC | SHORT | Combo Adaptive | 60m | 2,0x | 488,51228 | 488,78000 | 499,98639 | 730,32586 | 454,08996 | €32,69 | €65,39 | €1,54 | €-0,04 |
| Combo Adaptive — target pieno 3R | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,43050 | €902,18 | €1.804,37 | €49,86 | €0,00 |
| Combo Adaptive — target pieno 3R | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15861 | 0,13958 | 0,08010 | 0,21571 | €207,43 | €414,86 | €49,78 | €0,00 |
| Combo Adaptive — target pieno 3R | WLD | SHORT | Combo Adaptive | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,31537 | €911,80 | €1.823,59 | €49,76 | €-0,00 |
| Combo Adaptive — target pieno 3R | ALLO | SHORT | Combo Adaptive | 60m | 2,0x | 0,36179 | 0,36179 | 0,40521 | 0,54088 | 0,23155 | €205,00 | €410,00 | €49,20 | €-0,00 |
| Sol Donchian 4H | SOL | SHORT | Donchian breakout 20 barre | 240m | 2,0x | 75,96380 | 75,99500 | 78,23939 | 113,56589 | 69,59218 | €830,21 | €1.660,43 | €49,74 | €-0,68 |
| Sol Adaptive 4H | SOL | SHORT | Combo Adaptive | 240m | 2,0x | 75,96380 | 75,99500 | 78,44626 | 113,56589 | 69,75767 | €761,04 | €1.522,08 | €49,74 | €-0,63 |
| Eth Ema 4H | ETH | LONG | Trend following EMA | 240m | 2,0x | 1949,77988 | 1945,93000 | 1902,99144 | 984,63884 | 2066,75096 | €1.036,30 | €2.072,59 | €49,74 | €-4,09 |
| Doge Donchian 1H | DOGE | SHORT | Donchian breakout 20 barre | 60m | 3,0x | 0,07141 | 0,07208 | 0,07233 | 0,09485 | 0,06956 | €1.286,97 | €3.860,92 | €49,99 | €-36,46 |
| Master Adaptive V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39854 | 0,39854 | 0,38677 | 0,20126 | 0,42207 | €833,00 | €1.665,99 | €49,19 | €0,00 |
| Master Adaptive V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €203,80 | €407,60 | €48,91 | €0,00 |
| Master Adaptive V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10713 | €21,54 | €43,08 | €0,79 | €0,00 |
| Master Adaptive V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00406 | 0,00438 | 0,00357 | 0,00205 | 0,00504 | €202,05 | €404,11 | €48,49 | €31,92 |
| Master Adaptive No Alt V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39854 | 0,39854 | 0,38677 | 0,20126 | 0,42207 | €833,00 | €1.665,99 | €49,19 | €0,00 |
| Master Adaptive No Alt V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €203,80 | €407,60 | €48,91 | €0,00 |
| Master Adaptive No Alt V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10713 | €21,54 | €43,08 | €0,79 | €0,00 |
| Master Adaptive No Alt V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00406 | 0,00438 | 0,00357 | 0,00205 | 0,00504 | €202,14 | €404,28 | €48,51 | €31,93 |
| Master Adaptive Strict3 V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,41951 | €887,07 | €1.774,14 | €49,03 | €0,00 |
| Master Adaptive Strict3 V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10713 | €1.330,61 | €2.661,21 | €48,54 | €0,00 |
| Master Adaptive Strict3 V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 1943,95871 | 1945,93000 | 1915,96571 | 981,69915 | 1999,94472 | €1.509,27 | €3.018,53 | €43,47 | €3,06 |
| Master Adaptive Strict3 V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00443 | 0,00438 | 0,00389 | 0,00224 | 0,00549 | €198,88 | €397,76 | €47,73 | €-3,90 |
| Master Adaptive Expanded V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39854 | 0,39854 | 0,38677 | 0,20126 | 0,42207 | €833,00 | €1.665,99 | €49,19 | €0,00 |
| Master Adaptive Expanded V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €203,80 | €407,60 | €48,91 | €0,00 |
| Master Adaptive Expanded V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10713 | €33,54 | €67,08 | €1,22 | €0,00 |
| Master Adaptive Expanded V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00406 | 0,00438 | 0,00357 | 0,00205 | 0,00504 | €202,97 | €405,94 | €48,71 | €32,06 |
| Master Adaptive Gb20 V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,40304 | 0,40304 | 0,39140 | 0,20354 | 0,42632 | €848,64 | €1.697,27 | €49,02 | €0,00 |
| Master Adaptive Gb20 V1 | RIF | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,10582 | 0,10582 | 0,09312 | 0,05344 | 0,13122 | €201,89 | €403,77 | €48,45 | €0,00 |
| Master Adaptive Gb20 V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 367,08012 | 367,08012 | 360,46822 | 185,37546 | 380,30391 | €1.348,01 | €2.696,02 | €48,56 | €0,00 |
| Master Adaptive Gb20 V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00443 | 0,00438 | 0,00389 | 0,00224 | 0,00549 | €193,43 | €386,85 | €46,42 | €-3,79 |
| Master Adaptive Runner25 V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39854 | 0,39854 | 0,38677 | 0,20126 | 0,43384 | €833,00 | €1.665,99 | €49,19 | €0,00 |
| Master Adaptive Runner25 V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,21338 | €203,80 | €407,60 | €48,91 | €0,00 |
| Master Adaptive Runner25 V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 386,79573 | €20,87 | €41,74 | €0,76 | €0,00 |
| Master Adaptive Runner25 V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00406 | 0,00438 | 0,00357 | 0,00205 | 0,00552 | €202,72 | €405,45 | €48,65 | €32,02 |
| Combo Adaptive — Side × Regime Guard | ALLO | SHORT | Combo Adaptive | 60m | 2,0x | 0,35250 | 0,35250 | 0,39075 | 0,52699 | 0,27600 | €235,86 | €471,72 | €51,19 | €-0,00 |
| Combo Adaptive — Side × Regime Guard | SHIB | LONG | Combo Adaptive | 60m | 2,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €450,93 | €901,86 | €50,61 | €-23,21 |
| Combo Adaptive — Side × Regime Guard | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,00406 | 0,00438 | 0,00406 | 0,00205 | 0,00504 | €209,98 | €419,96 | €0,00 | €33,17 |
| Combo Adaptive — Side × Regime Guard | ZEC | SHORT | Combo Adaptive | 60m | 2,0x | 483,74323 | 488,78000 | 494,91887 | 723,19613 | 461,39195 | €34,68 | €69,35 | €1,60 | €-0,72 |
| Combo Adaptive — Side × Regime Guard | XRP | SHORT | Combo Adaptive | 60m | 2,0x | 1,09194 | 1,09160 | 1,10767 | 1,63245 | 1,06049 | €1.759,12 | €3.518,24 | €50,66 | €1,10 |
| Master Adaptive GB20 — Breakeven 0,5R | BEAT | LONG | Master Adaptive Consensus | 60m | 2,0x | 3,29017 | 3,29017 | 3,00714 | 1,66154 | 3,85623 | €291,32 | €582,63 | €50,12 | €0,00 |
| Master Adaptive GB20 — Breakeven 0,5R | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 367,86058 | 367,86058 | 361,23463 | 185,76959 | 381,11249 | €1.403,77 | €2.807,55 | €50,57 | €0,00 |
| Master Adaptive GB20 — Breakeven 0,5R | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00406 | 0,00438 | 0,00406 | 0,00205 | 0,00504 | €207,34 | €414,67 | €0,00 | €32,75 |
| Master Adaptive GB20 — 50% a 0,75R | BEAT | LONG | Master Adaptive Consensus | 60m | 2,0x | 3,29017 | 3,29017 | 3,00714 | 1,66154 | 3,85623 | €291,05 | €582,09 | €50,07 | €0,00 |
| Master Adaptive GB20 — 50% a 0,75R | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10713 | €1.376,47 | €2.752,95 | €50,21 | €0,00 |
| Master Adaptive GB20 — 50% a 0,75R | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00406 | 0,00438 | 0,00406 | 0,00205 | 0,00504 | €103,26 | €206,52 | €0,00 | €16,31 |
| Master Adaptive GB20 — Loss Cap 0,75R | BEAT | LONG | Master Adaptive Consensus | 60m | 2,0x | 3,29017 | 3,29017 | 3,07790 | 1,66154 | 3,85623 | €388,25 | €776,50 | €50,10 | €0,00 |
| Master Adaptive GB20 — Loss Cap 0,75R | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 361,71345 | 185,19860 | 380,10713 | €1.835,86 | €3.671,71 | €50,22 | €0,00 |
| Master Adaptive GB20 — Loss Cap 0,75R | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00406 | 0,00438 | 0,00357 | 0,00205 | 0,00536 | €207,77 | €415,53 | €49,86 | €32,82 |
| Rapida V3 NoHigh — Range Only | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,33165 | 0,33165 | 0,36472 | 0,44055 | 0,28205 | €170,92 | €512,75 | €51,13 | €-0,00 |
| Rapida V3 NoHigh — Range Only | ESPORTS | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,02828 | 0,02828 | 0,03168 | 0,03757 | 0,02319 | €142,68 | €428,04 | €51,37 | €-0,00 |
| Rapida V3 NoHigh — Regime Guard | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,33165 | 0,33165 | 0,36472 | 0,44055 | 0,28205 | €172,19 | €516,57 | €51,51 | €-0,00 |
| MAIN — Side × Regime Guard | ALLO | SHORT | Confluenza trend | 240m | 3,0x | 0,38070 | 0,38070 | 0,37357 | 0,50570 | 0,28933 | €140,03 | €420,08 | €0,00 | €-0,00 |
| MAIN — Side × Regime Guard | PEPE | LONG | Confluenza trend | 240m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €326,47 | €979,41 | €50,44 | €-7,42 |
| MAIN — Side × Regime Guard | AKE | LONG | Confluenza trend | 240m | 3,0x | 0,00440 | 0,00438 | 0,00387 | 0,00295 | 0,00545 | €142,16 | €426,47 | €51,18 | €-1,33 |
| MAIN — Side × Regime Guard | HYPE | SHORT | Confluenza trend | 240m | 3,0x | 57,27654 | 57,23300 | 59,33830 | 76,08234 | 53,15302 | €471,26 | €1.413,79 | €50,89 | €1,07 |
| MAIN — Dynamic Asset Selector | AKE | LONG | Confluenza trend | 240m | 3,0x | 0,00440 | 0,00438 | 0,00387 | 0,00295 | 0,00545 | €142,87 | €428,60 | €51,43 | €-1,34 |
| Combo Trend — Side × Regime Guard | ALLO | SHORT | Combo Trend | 60m | 2,0x | 0,35250 | 0,35250 | 0,39480 | 0,52699 | 0,25944 | €209,77 | €419,55 | €50,35 | €-0,00 |
| Combo Trend — Side × Regime Guard | ESPORTS | SHORT | Combo Trend | 60m | 2,0x | 0,02845 | 0,02845 | 0,03187 | 0,04254 | 0,02094 | €202,36 | €404,73 | €48,57 | €-0,00 |
| Combo Trend — Side × Regime Guard | AKE | LONG | Combo Trend | 60m | 2,0x | 0,00443 | 0,00438 | 0,00389 | 0,00224 | 0,00559 | €211,47 | €422,95 | €50,75 | €-4,14 |
| Combo Trend — Side × Regime Guard | DOGE | SHORT | Combo Trend | 60m | 2,0x | 0,07141 | 0,07208 | 0,07256 | 0,10675 | 0,06886 | €1.560,52 | €3.121,05 | €50,52 | €-29,47 |
| Combo Trend — Side × Regime Guard | HYPE | SHORT | Combo Trend | 60m | 2,0x | 58,25535 | 57,23300 | 57,39038 | 87,09174 | 55,75576 | €47,00 | €94,00 | €0,00 | €1,65 |
| FAST NoHigh <7,5 · SHORT only | WLD | SHORT | Momentum / breakout | 60m | 3,0x | 0,34959 | 0,34959 | 0,35668 | 0,46437 | 0,33896 | €822,35 | €2.467,06 | €50,00 | €-0,00 |
| FAST NoHigh <7,5 · SHORT only | ALLO | SHORT | Momentum / breakout | 60m | 3,0x | 0,33808 | 0,33808 | 0,36389 | 0,44909 | 0,29937 | €212,58 | €637,75 | €48,69 | €-0,00 |
| FAST NoHigh <7,5 · SHORT only | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00443 | 0,00438 | 0,00389 | 0,00297 | 0,00522 | €141,55 | €424,64 | €50,96 | €-4,16 |
| Bilanciata V3 · LONG only | XMR | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 366,72991 | 366,72991 | 360,04130 | 246,32025 | 380,10712 | €913,56 | €2.740,69 | €49,99 | €0,00 |
| Bilanciata V3 · LONG only | ALLO | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,34255 | 0,34255 | 0,37914 | 0,45502 | 0,26938 | €156,01 | €468,04 | €49,99 | €-0,00 |
| Bilanciata V3 · LONG only | ESPORTS | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,03342 | 0,03342 | 0,03342 | 0,04440 | 0,02540 | €137,40 | €412,21 | €0,00 | €-0,00 |
| Bilanciata V3 · LONG only | XRP | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 1,09094 | 1,09160 | 1,10665 | 1,44913 | 1,05952 | €1.119,51 | €3.358,52 | €48,36 | €-2,03 |
| Bilanciata V3 · LONG only | ZEC | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 488,51228 | 488,78000 | 499,98639 | 648,90714 | 465,56407 | €14,72 | €44,15 | €1,04 | €-0,02 |
| Scanner Bottom5 Short Profit Lock V1 | WLD | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,34449 | 0,34449 | 0,35368 | 0,51502 | 0,32613 | €937,87 | €1.875,74 | €50,00 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | ALLO | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,35250 | 0,35250 | 0,39075 | 0,52699 | 0,27600 | €227,60 | €455,20 | €49,39 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | ESPORTS | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,03342 | 0,03342 | 0,03262 | 0,04997 | 0,02540 | €206,07 | €412,14 | €0,00 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | ZEC | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 483,74323 | 488,78000 | 494,91887 | 723,19613 | 461,39195 | €19,22 | €38,45 | €0,89 | €-0,40 |
| Scanner Bottom5 Short Profit Lock V1 | XRP | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1,09094 | 1,09160 | 1,10665 | 1,63096 | 1,05952 | €18,48 | €36,96 | €0,53 | €-0,02 |
| Scanner Bottom5 Short Profit Lock V1 | HYPE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 57,07858 | 57,23300 | 58,25281 | 85,33248 | 54,73013 | €1.168,54 | €2.337,08 | €48,08 | €-6,32 |
| Scanner Bottom5 Short Mfe Trail V1 | WLD | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,34449 | 0,34449 | 0,35368 | 0,51502 | 0,32613 | €937,87 | €1.875,74 | €50,00 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | ALLO | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,35653 | 0,35653 | 0,39522 | 0,53301 | 0,27915 | €228,22 | €456,45 | €49,53 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | ESPORTS | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,02828 | 0,02828 | 0,03168 | 0,04229 | 0,02150 | €206,75 | €413,50 | €49,62 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | ZEC | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 483,74323 | 488,78000 | 494,91887 | 723,19613 | 461,39195 | €19,47 | €38,94 | €0,90 | €-0,41 |
| Scanner Bottom5 Short Mfe Trail V1 | XRP | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1,09094 | 1,09160 | 1,10665 | 1,63096 | 1,05952 | €18,72 | €37,43 | €0,54 | €-0,02 |
| Scanner Bottom5 Short Mfe Trail V1 | HYPE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 56,91461 | 57,23300 | 58,08547 | 85,08735 | 54,57291 | €1.189,24 | €2.378,47 | €48,93 | €-13,31 |
| Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00443 | 0,00438 | 0,00389 | 0,00297 | 0,00549 | €141,91 | €425,73 | €51,09 | €-4,17 |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00443 | 0,00438 | 0,00389 | 0,00297 | 0,00575 | €138,20 | €414,59 | €49,75 | €-4,06 |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 483,74323 | 488,78000 | 492,43540 | 642,57226 | 462,01282 | €927,74 | €2.783,21 | €50,01 | €-28,98 |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | XRP | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,08796 | 1,09160 | 1,10015 | 1,44518 | 1,05750 | €1.488,07 | €4.464,20 | €50,00 | €-14,93 |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | HYPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 57,07858 | 57,23300 | 57,99187 | 75,81938 | 54,79537 | €1.027,90 | €3.083,70 | €49,34 | €-8,34 |
| Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,35250 | 0,35250 | 0,38225 | 0,46824 | 0,29300 | €194,51 | €583,53 | €49,25 | €-0,00 |
| Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | ESPORTS | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,02998 | 0,02998 | 0,02998 | 0,03983 | 0,02279 | €132,90 | €398,69 | €0,00 | €-0,00 |
| Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00425 | 0,00438 | 0,00374 | 0,00286 | 0,00527 | €136,65 | €409,95 | €49,19 | €12,60 |
| Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 483,74323 | 488,78000 | 492,43540 | 642,57226 | 466,35890 | €43,20 | €129,60 | €2,33 | €-1,35 |
| Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | HYPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 56,71366 | 57,23300 | 57,61702 | 75,33464 | 54,90694 | €1.034,08 | €3.102,24 | €49,41 | €-28,41 |
| Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | ESPORTS | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,02828 | 0,02828 | 0,03168 | 0,03757 | 0,02150 | €141,08 | €423,23 | €50,79 | €-0,00 |
| Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,35250 | 0,35250 | 0,38225 | 0,46824 | 0,29300 | €190,72 | €572,15 | €48,29 | €-0,00 |
| Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00424 | 0,00438 | 0,00373 | 0,00285 | 0,00526 | €140,36 | €421,09 | €50,53 | €14,11 |
| Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 483,74323 | 488,78000 | 492,43540 | 642,57226 | 466,35890 | €939,82 | €2.819,46 | €50,66 | €-29,36 |
| Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | XRP | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,08796 | 1,09160 | 1,10015 | 1,44518 | 1,06359 | €84,48 | €253,44 | €2,84 | €-0,85 |
| Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | HYPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 56,71366 | 57,23300 | 57,61702 | 75,33464 | 54,90694 | €1.054,69 | €3.164,08 | €50,40 | €-28,97 |
| Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00406 | 0,00438 | 0,00406 | 0,00273 | 0,00528 | €137,82 | €413,47 | €0,00 | €32,66 |
| Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 483,74323 | 488,78000 | 492,43540 | 642,57226 | 462,01282 | €919,87 | €2.759,61 | €49,59 | €-28,73 |
| Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | XRP | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,08796 | 1,09160 | 1,10015 | 1,44518 | 1,05750 | €1.475,45 | €4.426,35 | €49,58 | €-14,80 |
| Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | HYPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 57,07858 | 57,23300 | 57,99187 | 75,81938 | 54,79537 | €1.012,65 | €3.037,94 | €48,61 | €-8,22 |
| Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,33808 | 0,33808 | 0,36389 | 0,44909 | 0,28646 | €211,10 | €633,31 | €48,35 | €-0,00 |
| Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00425 | 0,00438 | 0,00374 | 0,00286 | 0,00527 | €142,68 | €428,05 | €51,37 | €13,16 |
| Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 483,74323 | 488,78000 | 492,43540 | 642,57226 | 466,35890 | €958,36 | €2.875,08 | €51,66 | €-29,94 |
| Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | XRP | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,08796 | 1,09160 | 1,10015 | 1,44518 | 1,06359 | €117,45 | €352,36 | €3,95 | €-1,18 |
| Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | HYPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 57,07158 | 57,23300 | 57,98064 | 75,81009 | 55,25346 | €1.047,67 | €3.143,01 | €50,06 | €-8,89 |
| Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00424 | 0,00438 | 0,00373 | 0,00285 | 0,00526 | €138,53 | €415,58 | €49,87 | €13,93 |
| Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00424 | 0,00438 | 0,00373 | 0,00285 | 0,00526 | €142,59 | €427,78 | €51,33 | €14,34 |
| Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,35250 | 0,35250 | 0,38225 | 0,46824 | 0,29300 | €194,51 | €583,53 | €49,25 | €-0,00 |
| Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00424 | 0,00438 | 0,00373 | 0,00285 | 0,00526 | €136,23 | €408,68 | €49,04 | €13,70 |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,33713 | 0,33713 | 0,36471 | 0,44782 | 0,28197 | €208,24 | €624,73 | €51,11 | €-0,00 |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | ESPORTS | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,03070 | 0,03070 | 0,03070 | 0,04078 | 0,02333 | €138,06 | €414,17 | €0,00 | €-0,00 |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00443 | 0,00438 | 0,00389 | 0,00297 | 0,00549 | €141,35 | €424,04 | €50,88 | €-4,15 |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 483,74323 | 488,78000 | 492,43540 | 642,57226 | 466,35890 | €46,24 | €138,72 | €2,49 | €-1,44 |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | HYPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 56,71366 | 57,23300 | 57,61702 | 75,33464 | 54,90694 | €1.073,18 | €3.219,54 | €51,28 | €-29,48 |
| Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00443 | 0,00438 | 0,00389 | 0,00297 | 0,00549 | €144,01 | €432,02 | €51,84 | €-4,23 |
| Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,35250 | 0,35250 | 0,38225 | 0,46824 | 0,29300 | €200,65 | €601,96 | €50,80 | €-0,00 |
| Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | ESPORTS | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,03342 | 0,03342 | 0,03342 | 0,04440 | 0,02540 | €136,12 | €408,37 | €0,00 | €-0,00 |
| Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00406 | 0,00438 | 0,00406 | 0,00273 | 0,00528 | €137,23 | €411,70 | €0,00 | €32,52 |
| Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00406 | 0,00438 | 0,00406 | 0,00273 | 0,00528 | €137,23 | €411,70 | €0,00 | €32,52 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Scanner Bottom5 Short Profit Lock V1 | HYPE | SHORT | 2026-07-27T20:08:40+00:00 | 57,34669 | €39,98 | 0,82 | STOP |
| Scanner Bottom 5 Short 1H | HYPE | SHORT | 2026-07-27T20:08:40+00:00 | 57,34669 | €39,37 | 0,82 | STOP |
| Scanner Bottom20 Short | HYPE | SHORT | 2026-07-27T20:08:40+00:00 | 57,34669 | €39,05 | 0,82 | STOP |
| Scanner Bottom15 Short | HYPE | SHORT | 2026-07-27T20:08:40+00:00 | 57,34669 | €39,05 | 0,82 | STOP |
| Scanner Bottom10 Short | HYPE | SHORT | 2026-07-27T20:08:40+00:00 | 57,34669 | €39,05 | 0,82 | STOP |
| Combo Adaptive — Side × Regime Guard | HYPE | SHORT | 2026-07-27T20:08:40+00:00 | 57,29152 | €44,46 | 0,87 | STOP |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | HYPE | SHORT | 2026-07-27T20:08:40+00:00 | 57,29152 | €1,35 | 0,87 | STOP |
| Combo Adaptive — Trend/Transition | HYPE | SHORT | 2026-07-27T20:08:40+00:00 | 57,29152 | €43,21 | 0,87 | STOP |
| Combo Adaptive — parziale 1R | HYPE | SHORT | 2026-07-27T20:08:40+00:00 | 57,29152 | €0,53 | 0,91 | STOP |
| Bilanciata V3 · LONG only | HYPE | SHORT | 2026-07-27T20:08:40+00:00 | 57,34669 | €0,96 | 0,82 | STOP |
| Bilanciata 1H V3 Filtered | HYPE | SHORT | 2026-07-27T20:08:40+00:00 | 57,34669 | €1,54 | 0,82 | STOP |
| Bilanciata 1H V1 | HYPE | SHORT | 2026-07-27T20:08:40+00:00 | 57,34669 | €40,31 | 0,82 | STOP |

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
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 20/30 | 19/30 | 0,97 | 3,11 | -0,02R | €15,30 | 2,01% | DIVERGENTE | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 1/30 | 3/30 | 0,00 | 1,05 | -1,08R | €0,92 | 1,14% | DIVERGENTE | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 17/30 | 21/30 | 0,75 | 2,10 | -0,19R | €15,91 | 1,62% | DIVERGENTE | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 17/30 | 21/30 | 0,75 | 1,70 | -0,19R | €10,00 | 2,27% | DIVERGENTE | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 21/30 | 25/30 | 0,57 | 0,85 | -0,35R | €-3,10 | 2,95% | COERENTE − | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 5/30 | 5/30 | 0,00 | 0,00 | -1,04R | €-46,29 | 2,20% | COERENTE − | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 5/30 | 7/30 | 1,28 | 1,03 | 0,17R | €0,61 | 2,15% | COERENTE + | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 14/30 | 14/30 | 1,38 | 4,59 | 0,23R | €16,93 | 1,01% | COERENTE + | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 25/30 | 21/30 | 0,71 | 0,65 | -0,22R | €-8,01 | 2,93% | COERENTE − | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 5/30 | 5/30 | 0,00 | 0,00 | -1,04R | €-46,29 | 2,20% | COERENTE − | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 21/30 | 24/30 | 0,91 | 1,60 | -0,07R | €8,90 | 2,97% | DIVERGENTE | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 24/30 | 31/30 | 0,91 | 1,75 | -0,06R | €9,87 | 2,51% | DIVERGENTE | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 11/30 | 14/30 | 1,00 | 0,97 | -0,00R | €-0,67 | 2,46% | COERENTE − | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 24/30 | 26/30 | 0,75 | 1,32 | -0,19R | €5,78 | 2,70% | DIVERGENTE | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 27/30 | 21/30 | 0,77 | 0,80 | -0,17R | €-4,66 | 3,08% | COERENTE − | RACCOLTA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 6/30 | 6/30 | 0,00 | 0,33 | -1,03R | €-19,86 | 1,99% | COERENTE − | RACCOLTA RESEARCH |
| MAIN | Principale 4H | 70/30 | 24/30 | 1,07 | 0,71 | 0,05R | €-10,51 | 4,76% | DIVERGENTE | BOCCIATA RESEARCH |
| MAIN_DYNAMIC_ASSET_SELECTOR_V1 | MAIN — Dynamic Asset Selector | 0/30 | 7/30 | 0,00 | 3,51 | 0,00R | €40,93 | 1,06% | n/a | RACCOLTA RESEARCH |
| MAIN_SIDE_REGIME_GUARD_V1 | MAIN — Side × Regime Guard | 0/30 | 9/30 | 0,00 | 1,80 | 0,00R | €19,70 | 1,82% | n/a | RACCOLTA RESEARCH |
| RSI_EXTREME_LONG_15M | Scalp RSI Long 25 · prudente · 5x (riferimento tra 9 varianti) | 12/30 | 7/30 | 0,24 | 0,12 | -0,63R | €-6,34 | 0,58% | COERENTE − | RACCOLTA RESEARCH |
| RSI_EXTREME_SHORT_15M | Scalp RSI Short 75 · prudente · 5x (riferimento tra 9 varianti) | 13/30 | 10/30 | 0,40 | 0,27 | -0,39R | €-4,83 | 0,58% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_1H_BALANCED | Bilanciata 1H V1 | 189/30 | 56/30 | 0,96 | 1,31 | -0,03R | €5,75 | 3,56% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_BALANCED_LONG_NO_RHV_V1 | Bilanciata 1H — LONG senza Range High Vol | 0/30 | 13/30 | 0,00 | 0,71 | 0,00R | €-9,82 | 2,47% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_BALANCED_SHORT_TREND_DOWN_STRICT_V1 | Bilanciata 1H — SHORT Trend Down stretto | 0/30 | 1/30 | 0,00 | 0,00 | 0,00R | €-4,13 | 0,59% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_BALANCED_V2 | Bilanciata 1H V2 | 51/30 | 35/30 | 1,38 | 1,27 | 0,22R | €5,48 | 2,75% | COERENTE + | PRONTA PER REVISIONE LIVE |
| SHADOW_1H_BALANCED_V3 | Bilanciata 1H V3 Filtered | 88/30 | 52/30 | 1,05 | 1,55 | 0,03R | €11,04 | 2,20% | COERENTE + | BOCCIATA RESEARCH |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | Bilanciata V3 · LONG only | 13/30 | 12/30 | 0,55 | 0,82 | -0,36R | €-4,11 | 1,46% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_1H_FAST | Rapida 1H V1 — madre | 207/30 | 77/30 | 0,91 | 1,03 | -0,06R | €0,67 | 6,76% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | Rapida V1 — Long + BTC 1–3 + score <7,5 | 26/30 | 23/30 | 1,46 | 1,14 | 0,23R | €2,82 | 2,07% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | FAST NoHigh <7,5 · SHORT only | 26/30 | 22/30 | 1,35 | 1,62 | 0,19R | €8,44 | 1,76% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | Rapida V1 — no HIGH + score <7,5 | 92/30 | 58/30 | 1,13 | 1,51 | 0,07R | €9,39 | 2,83% | COERENTE + | PRONTA PER REVISIONE LIVE |
| SHADOW_1H_FAST_NO_PEPE_V1 | Rapida V1 — senza PEPE | 101/30 | 49/30 | 0,92 | 1,27 | -0,05R | €5,20 | 2,15% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_COST_AWARE_V1 | Rapida score 6–7,5 — Cost Aware | 0/30 | 20/30 | 0,00 | 2,61 | 0,00R | €22,69 | 1,96% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_NO_TREND_UP_V1 | Rapida score 6–7,5 — senza Trend Up | 0/30 | 17/30 | 0,00 | 2,53 | 0,00R | €22,11 | 2,01% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_RANGE_ONLY_V1 | Rapida score 6–7,5 — Range Only | 0/30 | 11/30 | 0,00 | 2,70 | 0,00R | €29,23 | 2,28% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_V1 | Rapida V1 — score 6–7,5 | 70/30 | 57/30 | 1,15 | 1,49 | 0,08R | €8,66 | 2,49% | COERENTE + | PRONTA PER REVISIONE LIVE |
| SHADOW_1H_FAST_TP2_V1 | Rapida V1 — target pieno 2R | 97/30 | 56/30 | 0,85 | 1,04 | -0,10R | €0,82 | 2,58% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V2 | Rapida 1H V2 | 14/30 | 14/30 | 0,62 | 0,95 | -0,26R | €-1,11 | 1,69% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3 | Rapida 1H V3 Filtered — madre | 143/30 | 84/30 | 1,05 | 1,12 | 0,03R | €2,37 | 2,89% | COERENTE + | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_CAP75_V1 | Rapida V3 — score <7,5 | 81/30 | 51/30 | 1,05 | 1,62 | 0,03R | €9,99 | 2,49% | COERENTE + | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | Rapida V3 — qualità completa + profit lock | 46/30 | 47/30 | 0,96 | 1,08 | -0,02R | €1,75 | 3,21% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | Rapida V3 — Long + no HIGH + score <7,5 | 46/30 | 42/30 | 0,96 | 0,98 | -0,02R | €-0,47 | 2,86% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | Rapida V3 — Long Only | 60/30 | 49/30 | 0,92 | 0,78 | -0,05R | €-5,29 | 3,67% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V1 | Rapida V3 NoHigh — Range Only | 0/30 | 10/30 | 0,00 | 2,84 | 0,00R | €29,80 | 1,78% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_V1 | Rapida V3 NoHigh — Regime Guard | 0/30 | 18/30 | 0,00 | 3,42 | 0,00R | €22,03 | 1,39% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | Rapida V3 — no volatilità HIGH | 96/30 | 58/30 | 0,99 | 0,92 | -0,01R | €-1,78 | 2,96% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONLY_V1 | Rapida V3 senza ESPORTS — Long Only | 0/30 | 28/30 | 0,00 | 1,49 | 0,00R | €7,33 | 1,61% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_V1 | Rapida V3 senza ESPORTS — MFE Lock | 0/30 | 35/30 | 0,00 | 1,82 | 0,00R | €9,82 | 2,05% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_GUARD_V1 | Rapida V3 senza ESPORTS — Stress Guard | 0/30 | 19/30 | 0,00 | 1,16 | 0,00R | €3,75 | 2,17% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | Rapida V3 — senza ESPORTS | 97/30 | 58/30 | 0,93 | 0,99 | -0,05R | €-0,14 | 2,49% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_4H_WIDE | Ampia 4H | 55/30 | 19/30 | 1,02 | 1,05 | 0,02R | €1,54 | 3,68% | COERENTE + | BOCCIATA RESEARCH |
| SHADOW_BOLLINGER_MR_1H | Benchmark Bollinger mean reversion 1H | 57/30 | 42/30 | 1,40 | 1,00 | 0,21R | €0,05 | 4,19% | COERENTE + | BOCCIATA PAPER |
| SHADOW_BTC_ADAPTIVE_1H | Btc Adaptive 1H | 4/30 | 3/30 | 0,00 | 1,24 | -1,11R | €4,43 | 0,89% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_BTC_ADAPTIVE_4H | Btc Adaptive 4H | 1/30 | 1/30 | 0,00 | 0,00 | -1,07R | €-50,38 | 0,74% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_BOLLINGER_1H | Btc Bollinger 1H | 3/30 | 3/30 | ∞ | ∞ | 1,37R | €56,04 | 0,54% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_BTC_BOLLINGER_4H | Btc Bollinger 4H | 1/30 | 1/30 | ∞ | ∞ | 1,72R | €84,12 | 0,30% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_BTC_DONCHIAN_1H | Btc Donchian 1H | 5/30 | 4/30 | 0,00 | 0,82 | -1,12R | €-4,84 | 1,49% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_DONCHIAN_4H | Btc Donchian 4H | 1/30 | 1/30 | 0,00 | 0,00 | -1,07R | €-49,32 | 0,96% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_EMA_1H | Btc Ema 1H | 4/30 | 6/30 | 0,57 | 0,59 | -0,36R | €-14,69 | 1,56% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_EMA_4H | Btc Ema 4H | 1/30 | 1/30 | 0,00 | 0,00 | -1,07R | €-49,32 | 0,96% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE | Combo Adaptive — madre | 136/30 | 26/30 | 1,07 | 1,51 | 0,05R | €7,85 | 1,49% | COERENTE + | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | Combo Adaptive — Long Only | 47/30 | 13/30 | 0,82 | 1,04 | -0,13R | €0,93 | 2,34% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | Combo Adaptive — MFE Trail esistente | 103/30 | 33/30 | 0,98 | 0,49 | -0,02R | €-12,93 | 5,33% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | Combo Adaptive — parziale 1R | 77/30 | 23/30 | 0,84 | 0,52 | -0,11R | €-12,89 | 3,32% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | Combo Adaptive — Quality7 + Regime + parziale 1R | 9/30 | 9/30 | 0,53 | 0,64 | -0,38R | €-10,55 | 1,95% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | Combo Adaptive — Quality7 + Regime | 9/30 | 9/30 | 0,53 | 0,32 | -0,38R | €-20,85 | 2,32% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | Combo Adaptive — Quality7 | 22/30 | 19/30 | 1,31 | 1,47 | 0,19R | €5,84 | 1,51% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | Combo Adaptive — Trend/Transition | 39/30 | 19/30 | 0,41 | 0,82 | -0,50R | €-4,24 | 2,18% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | Combo Adaptive — 75% a 2R + runner 25% a 3R | 41/30 | 26/30 | 0,58 | 1,27 | -0,36R | €5,23 | 2,12% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_SIDE_REGIME_GUARD_V1 | Combo Adaptive — Side × Regime Guard | 0/30 | 17/30 | 0,00 | 2,03 | 0,00R | €13,39 | 1,41% | n/a | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | Combo Adaptive — target pieno 3R | 41/30 | 13/30 | 0,58 | 0,76 | -0,36R | €-5,13 | 1,41% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_MEAN_REVERSION | Combo Mean Reversion | 21/30 | 17/30 | 1,14 | 0,99 | 0,08R | €-0,30 | 2,31% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_COMBO_SCANNER | Combo Scanner | 83/30 | 40/30 | 1,38 | 0,94 | 0,23R | €-1,49 | 3,25% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_COMBO_TREND | Combo Trend | 108/30 | 44/30 | 0,97 | 0,72 | -0,02R | €-10,17 | 7,02% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_TREND_SIDE_REGIME_GUARD_V1 | Combo Trend — Side × Regime Guard | 0/30 | 18/30 | 0,00 | 1,43 | 0,00R | €6,65 | 1,73% | n/a | RACCOLTA RESEARCH |
| SHADOW_DOGE_BOLLINGER_1H | Doge Bollinger 1H | 2/30 | 2/30 | 0,00 | 0,00 | -1,12R | €-55,56 | 1,26% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_DOGE_DONCHIAN_1H | Doge Donchian 1H | 3/30 | 4/30 | 0,84 | 0,98 | -0,12R | €-0,31 | 1,08% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_DOGE_EMA_1H | Doge Ema 1H | 4/30 | 8/30 | 1,71 | 1,55 | 0,39R | €11,48 | 1,36% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_DONCHIAN_1H | Benchmark Donchian breakout 1H | 68/30 | 30/30 | 0,78 | 2,20 | -0,17R | €21,48 | 2,12% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | Donchian 1H Gb20 120R V1 | 1/30 | 0/30 | 0,00 | 0,00 | -1,01R | €0,00 | 1,09% | n/a | RACCOLTA RESEARCH |
| SHADOW_EMA_TREND_1H | Benchmark trend following EMA 1H | 112/30 | 31/30 | 0,98 | 0,71 | -0,01R | €-7,56 | 3,34% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_ETH_ADAPTIVE_1H | Eth Adaptive 1H | 6/30 | 6/30 | 0,34 | 0,08 | -0,61R | €-33,40 | 2,09% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_BOLLINGER_1H | Eth Bollinger 1H | 2/30 | 2/30 | 1,21 | 0,28 | 0,12R | €-20,26 | 0,91% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_ETH_DONCHIAN_1H | Eth Donchian 1H | 5/30 | 5/30 | 0,42 | 0,42 | -0,52R | €-25,60 | 1,62% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_EMA_1H | Eth Ema 1H | 6/30 | 8/30 | 0,34 | 0,16 | -0,61R | €-34,02 | 2,76% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_EMA_4H | Eth Ema 4H | 1/30 | 1/30 | 0,00 | 0,00 | -1,06R | €-52,88 | 0,96% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_GLOBAL_PURE | Global Confluence puro 1H | 4/30 | 10/30 | 1,75 | 0,37 | 0,41R | €-20,93 | 2,92% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | Master Adaptive Expanded V1 | 46/30 | 18/30 | 0,76 | 0,62 | -0,18R | €-16,29 | 3,64% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_BE_V1 | Master Adaptive GB20 — Breakeven 0,5R | 0/30 | 19/30 | 0,00 | 0,79 | 0,00R | €-5,36 | 3,15% | n/a | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_LOSS_CAP_V1 | Master Adaptive GB20 — Loss Cap 0,75R | 0/30 | 16/30 | 0,00 | 0,71 | 0,00R | €-9,99 | 3,63% | n/a | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_PARTIAL_V1 | Master Adaptive GB20 — 50% a 0,75R | 0/30 | 14/30 | 0,00 | 0,70 | 0,00R | €-9,79 | 2,50% | n/a | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | Master Adaptive Gb20 V1 | 46/30 | 50/30 | 0,68 | 0,59 | -0,24R | €-7,49 | 4,27% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | Master Adaptive No Alt V1 | 41/30 | 15/30 | 0,71 | 0,53 | -0,21R | €-22,21 | 4,03% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | Master Adaptive Runner25 V1 | 35/30 | 17/30 | 0,73 | 0,58 | -0,22R | €-17,97 | 3,98% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | Master Adaptive Strict3 V1 | 35/30 | 23/30 | 0,76 | 0,54 | -0,18R | €-20,94 | 5,58% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_V1 | Master Adaptive V1 | 46/30 | 15/30 | 0,68 | 0,53 | -0,24R | €-22,47 | 4,07% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_RELATIVE_STRENGTH | Forza relativa 1H V1 | 137/30 | 35/30 | 0,96 | 0,54 | -0,03R | €-14,16 | 7,55% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_RELATIVE_STRENGTH_V2 | Forza relativa 1H V2 | 51/30 | 43/30 | 1,46 | 1,04 | 0,28R | €1,21 | 5,10% | COERENTE + | BOCCIATA PAPER |
| SHADOW_SCANNER_BOTTOM10_SHORT | Scanner Bottom10 Short | 7/30 | 7/30 | 0,00 | 0,25 | -1,09R | €-29,46 | 2,72% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_BOTTOM15_SHORT | Scanner Bottom15 Short | 7/30 | 7/30 | 0,00 | 0,25 | -1,09R | €-29,46 | 2,72% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_BOTTOM20_SHORT | Scanner Bottom20 Short | 7/30 | 7/30 | 0,00 | 0,25 | -1,09R | €-29,46 | 2,72% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT | Scanner Bottom 5 Short 1H | 51/30 | 30/30 | 0,77 | 0,66 | -0,15R | €-8,32 | 5,48% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT_CONTINUATION_V1 | Scanner Bottom5 Short Continuation V1 | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | Scanner Bottom5 Short Mfe Trail V1 | 3/30 | 7/30 | 0,00 | 0,86 | -1,07R | €-3,14 | 1,38% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | Scanner Bottom5 Short Profit Lock V1 | 3/30 | 6/30 | 0,00 | 0,50 | -1,07R | €-13,33 | 1,53% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP10_LONG | Scanner Top10 Long | 16/30 | 15/30 | 1,13 | 0,53 | 0,09R | €-14,39 | 4,14% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP15_LONG | Scanner Top15 Long | 17/30 | 15/30 | 1,02 | 0,53 | 0,02R | €-14,39 | 4,14% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP20_LONG | Scanner Top20 Long | 17/30 | 15/30 | 1,02 | 0,53 | 0,02R | €-14,39 | 4,14% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC | Scanner Top 5 + forza BTC 1H | 81/30 | 34/30 | 1,36 | 1,49 | 0,22R | €10,84 | 3,23% | COERENTE + | PRONTA PER REVISIONE LIVE |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | Top 5 + BTC — BTC 2–3 | 19/30 | 7/30 | 0,73 | 1,14 | -0,21R | €3,57 | 2,84% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | Top 5 + BTC — BTC≤3 | 37/30 | 14/30 | 1,00 | 1,03 | 0,00R | €0,92 | 3,23% | COERENTE + | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | Top 5 + BTC — Guard + BTC≤3 + MFE | 31/30 | 28/30 | 1,17 | 0,70 | 0,11R | €-8,68 | 3,93% | DIVERGENTE | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | Top 5 + BTC — Guard + BTC≤3 | 31/30 | 13/30 | 1,17 | 0,98 | 0,11R | €-0,85 | 3,23% | DIVERGENTE | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | Top 5 + BTC — Guard + MFE | 36/30 | 35/30 | 0,96 | 0,58 | -0,02R | €-11,75 | 5,08% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | Top 5 + BTC — Guard | 36/30 | 20/30 | 0,96 | 0,65 | -0,02R | €-11,90 | 3,36% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | Top 5 + BTC — solo MFE | 43/30 | 25/30 | 0,96 | 0,59 | -0,03R | €-8,85 | 3,95% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | Top 5 + BTC — 75% a 2,2R + runner 3R | 33/30 | 22/30 | 1,10 | 1,17 | 0,08R | €4,07 | 3,25% | COERENTE + | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | Top 5 + BTC — target pieno 3R | 33/30 | 18/30 | 1,10 | 1,18 | 0,08R | €5,31 | 3,22% | COERENTE + | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_SCANNER_TOP5_LONG | Scanner Top 5 Long 1H | 96/30 | 45/30 | 1,28 | 1,49 | 0,16R | €11,05 | 3,57% | COERENTE + | PRONTA PER REVISIONE LIVE |
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
- Prezzo DOGE: **0.07208**
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
| BTC sotto filtro | 64984.5 | OK |

### Ultima candela 15m valutata

- Rejection accettata: **NO**; motivo: **trigger_touched, entry_not_chased, upper_wick, bearish_confirmation**
- High **0.07207**; close **0.07207**; wick alta **0.0%**; volume **x0.66**

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
- Confidenza: **78,80%**
- Volatilità: **HIGH**
- Rotazione strategie: **SOLO OSSERVAZIONE — nessun peso operativo viene ancora modificato**
- Motivo: Direzione poco definita: score BTC +3.0, breadth EMA50 42%, ADX 17.8.
- BTC trend score: **3,00**; ADX: **17,80**; breadth sopra EMA50: **41,67%**
- Mediana alt vs BTC: **-1,01%**; dispersione: **10,81%**

- Aperti in questo ciclo: **0**
- Chiusi in questo ciclo: **0**
- Posizioni research aperte: **509**
- Trade research chiusi: **4040**
- Eventi di mercato indipendenti chiusi: **929**
- Segnali sovrapposti saltati sullo stesso asset/profilo: **18377**
- Posizioni Research V1 senza regime scartate durante la migrazione: **28**

### Risultati complessivi per strategia

| Profilo | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | 7 | 20 | 20 | 35,00% | 0,97 | -0,02R | €-4,16 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | 5 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,75 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | 1 | 17 | 17 | 29,41% | 0,75 | -0,19R | €-32,73 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | 1 | 17 | 17 | 29,41% | 0,75 | -0,19R | €-32,72 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | 1 | 21 | 21 | 23,81% | 0,57 | -0,35R | €-73,65 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | 1 | 5 | 5 | 0,00% | 0,00 | -1,04R | €-51,94 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | 2 | 5 | 5 | 40,00% | 1,28 | 0,17R | €8,72 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | 1 | 14 | 14 | 42,86% | 1,38 | 0,23R | €31,73 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | 2 | 25 | 25 | 28,00% | 0,71 | -0,22R | €-54,29 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | 1 | 5 | 5 | 0,00% | 0,00 | -1,04R | €-51,94 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | 1 | 21 | 21 | 33,33% | 0,91 | -0,07R | €-13,98 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | 5 | 24 | 24 | 33,33% | 0,91 | -0,06R | €-15,46 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | 0 | 11 | 11 | 36,36% | 1,00 | -0,00R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | 5 | 24 | 24 | 29,17% | 0,75 | -0,19R | €-45,20 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | 6 | 27 | 27 | 29,63% | 0,77 | -0,17R | €-45,60 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | 4 | 6 | 6 | 0,00% | 0,00 | -1,03R | €-62,08 |
| MAIN | 15 | 70 | 70 | 35,71% | 1,07 | 0,05R | €32,21 |
| RSI_EXTREME_LONG_15M | 0 | 12 | 12 | 25,00% | 0,24 | -0,63R | €-75,99 |
| RSI_EXTREME_SHORT_15M | 0 | 13 | 13 | 30,77% | 0,40 | -0,39R | €-50,12 |
| Bilanciata 1H V1 | 15 | 189 | 189 | 32,80% | 0,96 | -0,03R | €-50,71 |
| Bilanciata 1H V2 | 8 | 58 | 51 | 41,38% | 1,38 | 0,22R | €128,47 |
| Bilanciata 1H V3 Filtered | 12 | 88 | 88 | 35,23% | 1,05 | 0,03R | €30,72 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | 7 | 13 | 13 | 23,08% | 0,55 | -0,36R | €-47,32 |
| Rapida 1H V1 | 1 | 207 | 207 | 38,65% | 0,91 | -0,06R | €-116,21 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | 0 | 26 | 26 | 50,00% | 1,46 | 0,23R | €59,32 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | 4 | 26 | 26 | 50,00% | 1,35 | 0,19R | €48,36 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | 5 | 92 | 92 | 44,57% | 1,13 | 0,07R | €67,94 |
| SHADOW_1H_FAST_NO_PEPE_V1 | 9 | 101 | 101 | 39,60% | 0,92 | -0,05R | €-51,10 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | 5 | 70 | 70 | 45,71% | 1,15 | 0,08R | €58,53 |
| SHADOW_1H_FAST_TP2_V1 | 10 | 97 | 97 | 31,96% | 0,85 | -0,10R | €-101,22 |
| Rapida 1H V2 | 1 | 16 | 14 | 31,25% | 0,62 | -0,26R | €-42,07 |
| Rapida 1H V3 Filtered | 8 | 143 | 143 | 42,66% | 1,05 | 0,03R | €37,52 |
| SHADOW_1H_FAST_V3_CAP75_V1 | 9 | 81 | 81 | 43,21% | 1,05 | 0,03R | €25,91 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | 2 | 46 | 46 | 41,30% | 0,96 | -0,02R | €-11,34 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | 2 | 46 | 46 | 41,30% | 0,96 | -0,02R | €-11,34 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | 2 | 60 | 60 | 40,00% | 0,92 | -0,05R | €-32,12 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | 5 | 96 | 96 | 41,67% | 0,99 | -0,01R | €-7,02 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | 7 | 97 | 97 | 40,21% | 0,93 | -0,05R | €-44,57 |
| SHADOW_4H_WIDE | 25 | 55 | 55 | 27,27% | 1,02 | 0,02R | €9,14 |
| SHADOW_BOLLINGER_MR_1H | 3 | 57 | 57 | 50,88% | 1,40 | 0,21R | €118,70 |
| SHADOW_BTC_ADAPTIVE_1H | 0 | 4 | 4 | 0,00% | 0,00 | -1,11R | €-44,44 |
| SHADOW_BTC_ADAPTIVE_4H | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,67 |
| SHADOW_BTC_BOLLINGER_1H | 0 | 3 | 3 | 100,00% | ∞ | 1,37R | €41,00 |
| SHADOW_BTC_BOLLINGER_4H | 0 | 1 | 1 | 100,00% | ∞ | 1,72R | €17,16 |
| SHADOW_BTC_DONCHIAN_1H | 0 | 5 | 5 | 0,00% | 0,00 | -1,12R | €-56,25 |
| SHADOW_BTC_DONCHIAN_4H | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,71 |
| SHADOW_BTC_EMA_1H | 1 | 4 | 4 | 25,00% | 0,57 | -0,36R | €-14,44 |
| SHADOW_BTC_EMA_4H | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,71 |
| SHADOW_COMBO_ADAPTIVE | 15 | 136 | 136 | 36,03% | 1,07 | 0,05R | €64,63 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | 6 | 47 | 47 | 29,79% | 0,82 | -0,13R | €-61,49 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | 15 | 103 | 103 | 33,98% | 0,98 | -0,02R | €-16,83 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | 15 | 77 | 77 | 31,17% | 0,84 | -0,11R | €-86,54 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | 2 | 9 | 9 | 22,22% | 0,53 | -0,38R | €-34,21 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | 2 | 9 | 9 | 22,22% | 0,53 | -0,38R | €-34,21 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | 6 | 22 | 22 | 40,91% | 1,31 | 0,19R | €42,26 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | 4 | 39 | 39 | 17,95% | 0,41 | -0,50R | €-194,42 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | 6 | 41 | 41 | 17,07% | 0,58 | -0,36R | €-148,38 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | 6 | 41 | 41 | 17,07% | 0,58 | -0,36R | €-148,38 |
| SHADOW_COMBO_MEAN_REVERSION | 1 | 21 | 21 | 42,86% | 1,14 | 0,08R | €17,24 |
| SHADOW_COMBO_SCANNER | 7 | 83 | 83 | 39,76% | 1,38 | 0,23R | €192,41 |
| SHADOW_COMBO_TREND | 16 | 108 | 108 | 31,48% | 0,97 | -0,02R | €-24,37 |
| SHADOW_DOGE_BOLLINGER_1H | 0 | 2 | 2 | 0,00% | 0,00 | -1,12R | €-22,46 |
| SHADOW_DOGE_DONCHIAN_1H | 1 | 3 | 3 | 33,33% | 0,84 | -0,12R | €-3,55 |
| SHADOW_DOGE_EMA_1H | 0 | 4 | 4 | 50,00% | 1,71 | 0,39R | €15,73 |
| SHADOW_DONCHIAN_1H | 9 | 68 | 68 | 25,00% | 0,78 | -0,17R | €-115,54 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | 4 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_EMA_TREND_1H | 16 | 112 | 112 | 31,25% | 0,98 | -0,01R | €-13,40 |
| SHADOW_ETH_ADAPTIVE_1H | 0 | 6 | 6 | 16,67% | 0,34 | -0,61R | €-36,67 |
| SHADOW_ETH_BOLLINGER_1H | 0 | 2 | 2 | 50,00% | 1,21 | 0,12R | €2,33 |
| SHADOW_ETH_DONCHIAN_1H | 0 | 5 | 5 | 20,00% | 0,42 | -0,52R | €-26,11 |
| SHADOW_ETH_EMA_1H | 0 | 6 | 6 | 16,67% | 0,34 | -0,61R | €-36,55 |
| SHADOW_ETH_EMA_4H | 1 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,57 |
| SHADOW_GLOBAL_PURE | 1 | 4 | 4 | 50,00% | 1,75 | 0,41R | €16,33 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | 6 | 46 | 46 | 28,26% | 0,76 | -0,18R | €-80,90 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | 6 | 46 | 46 | 26,09% | 0,68 | -0,24R | €-110,10 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | 6 | 41 | 41 | 26,83% | 0,71 | -0,21R | €-87,21 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | 8 | 35 | 35 | 20,00% | 0,73 | -0,22R | €-75,35 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | 5 | 35 | 35 | 28,57% | 0,76 | -0,18R | €-62,86 |
| SHADOW_MASTER_ADAPTIVE_V1 | 6 | 46 | 46 | 26,09% | 0,68 | -0,24R | €-110,10 |
| Forza relativa 1H V1 | 17 | 137 | 137 | 30,66% | 0,96 | -0,03R | €-40,37 |
| Forza relativa 1H V2 | 7 | 56 | 51 | 41,07% | 1,46 | 0,28R | €157,85 |
| SHADOW_SCANNER_BOTTOM10_SHORT | 8 | 7 | 7 | 0,00% | 0,00 | -1,09R | €-76,59 |
| SHADOW_SCANNER_BOTTOM15_SHORT | 8 | 7 | 7 | 0,00% | 0,00 | -1,09R | €-76,59 |
| SHADOW_SCANNER_BOTTOM20_SHORT | 8 | 7 | 7 | 0,00% | 0,00 | -1,09R | €-76,59 |
| SHADOW_SCANNER_BOTTOM5_SHORT | 10 | 51 | 51 | 27,45% | 0,77 | -0,15R | €-77,97 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | 7 | 3 | 3 | 0,00% | 0,00 | -1,07R | €-32,23 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | 7 | 3 | 3 | 0,00% | 0,00 | -1,07R | €-32,23 |
| SHADOW_SCANNER_TOP10_LONG | 3 | 16 | 16 | 37,50% | 1,13 | 0,09R | €13,94 |
| SHADOW_SCANNER_TOP15_LONG | 3 | 17 | 17 | 35,29% | 1,02 | 0,02R | €2,83 |
| SHADOW_SCANNER_TOP20_LONG | 3 | 17 | 17 | 35,29% | 1,02 | 0,02R | €2,83 |
| SHADOW_SCANNER_TOP5_BTC | 6 | 81 | 81 | 38,27% | 1,36 | 0,22R | €179,49 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | 4 | 19 | 19 | 26,32% | 0,73 | -0,21R | €-40,11 |
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
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | ALT_ROTATION_DOWN | 4 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | ALT_ROTATION_UP | 0 | 12 | 12 | 41,67% | 1,27 | 0,17R | €20,58 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | RANGE | 1 | 4 | 4 | 25,00% | 0,64 | -0,28R | €-11,25 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,88R | €18,83 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_UP | 1 | 2 | 2 | 0,00% | 0,00 | -1,11R | €-22,18 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_UP_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | ALT_ROTATION_DOWN | 3 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
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
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | ALT_ROTATION_DOWN | 3 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | ALT_ROTATION_UP | 1 | 9 | 9 | 44,44% | 1,39 | 0,24R | €21,41 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | RANGE | 0 | 6 | 6 | 50,00% | 1,91 | 0,47R | €28,04 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,88R | €18,83 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_UP | 1 | 6 | 6 | 0,00% | 0,00 | -1,06R | €-63,46 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | ALT_ROTATION_UP | 0 | 7 | 7 | 42,86% | 1,30 | 0,19R | €13,25 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | RANGE_LOW_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,96R | €19,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | TREND_UP | 0 | 3 | 3 | 0,00% | 0,00 | -1,10R | €-32,97 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | ALT_ROTATION_DOWN | 3 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | ALT_ROTATION_UP | 1 | 8 | 8 | 37,50% | 1,03 | 0,02R | €1,85 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | RANGE | 0 | 5 | 5 | 20,00% | 0,48 | -0,43R | €-21,49 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 3,88 | 0,97R | €29,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,88R | €18,83 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_UP | 1 | 6 | 6 | 0,00% | 0,00 | -1,06R | €-63,46 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | ALT_ROTATION_DOWN | 3 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | ALT_ROTATION_UP | 1 | 10 | 10 | 40,00% | 1,18 | 0,12R | €11,58 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | RANGE | 0 | 6 | 6 | 16,67% | 0,39 | -0,53R | €-31,62 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 3,88 | 0,97R | €29,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,88R | €18,83 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_UP | 1 | 6 | 6 | 0,00% | 0,00 | -1,06R | €-63,46 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_UP_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | ALT_ROTATION_DOWN | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
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
| Bilanciata 1H V1 | RANGE_HIGH_VOL | 0 | 12 | 12 | 0,00% | 0,00 | -1,07R | €-128,21 |
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
| SHADOW_1H_FAST_NO_PEPE_V1 | ALT_ROTATION_DOWN | 3 | 21 | 21 | 19,05% | 0,35 | -0,50R | €-105,26 |
| SHADOW_1H_FAST_NO_PEPE_V1 | ALT_ROTATION_UP | 0 | 15 | 15 | 40,00% | 0,86 | -0,09R | €-13,18 |
| SHADOW_1H_FAST_NO_PEPE_V1 | RANGE | 2 | 34 | 34 | 52,94% | 1,59 | 0,28R | €95,12 |
| SHADOW_1H_FAST_NO_PEPE_V1 | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_1H_FAST_NO_PEPE_V1 | RANGE_LOW_VOL | 1 | 2 | 2 | 100,00% | ∞ | 1,47R | €29,42 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TRANSITION | 1 | 5 | 5 | 80,00% | 5,11 | 0,94R | €46,95 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_DOWN | 1 | 2 | 2 | 0,00% | 0,00 | -1,02R | €-20,41 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_UP | 1 | 20 | 20 | 25,00% | 0,45 | -0,44R | €-87,18 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,36R | €13,57 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | ALT_ROTATION_DOWN | 2 | 12 | 12 | 33,33% | 0,65 | -0,25R | €-30,18 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | ALT_ROTATION_UP | 1 | 17 | 17 | 41,18% | 0,92 | -0,05R | €-8,25 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | RANGE | 1 | 26 | 26 | 57,69% | 1,99 | 0,41R | €107,14 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | RANGE_LOW_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,48R | €29,66 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 1,43R | €28,69 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_UP | 1 | 10 | 10 | 20,00% | 0,32 | -0,58R | €-58,35 |
| SHADOW_1H_FAST_TP2_V1 | ALT_ROTATION_DOWN | 3 | 21 | 21 | 14,29% | 0,33 | -0,55R | €-115,33 |
| SHADOW_1H_FAST_TP2_V1 | ALT_ROTATION_UP | 0 | 17 | 17 | 41,18% | 1,23 | 0,15R | €24,85 |
| SHADOW_1H_FAST_TP2_V1 | RANGE | 2 | 28 | 28 | 46,43% | 1,50 | 0,28R | €79,75 |
| SHADOW_1H_FAST_TP2_V1 | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_1H_FAST_TP2_V1 | RANGE_LOW_VOL | 1 | 2 | 2 | 50,00% | 1,93 | 0,47R | €9,39 |
| SHADOW_1H_FAST_TP2_V1 | TRANSITION | 1 | 5 | 5 | 80,00% | 6,79 | 1,32R | €66,04 |
| SHADOW_1H_FAST_TP2_V1 | TREND_DOWN | 1 | 2 | 2 | 0,00% | 0,00 | -1,02R | €-20,41 |
| SHADOW_1H_FAST_TP2_V1 | TREND_UP | 1 | 20 | 20 | 15,00% | 0,32 | -0,62R | €-123,95 |
| SHADOW_1H_FAST_TP2_V1 | TREND_UP_HIGH_VOL | 1 | 1 | 1 | 0,00% | 0,00 | -1,14R | €-11,43 |
| Rapida 1H V2 | ALT_ROTATION_UP | 0 | 4 | 4 | 25,00% | 0,41 | -0,49R | €-19,77 |
| Rapida 1H V2 | RANGE | 1 | 11 | 9 | 36,36% | 0,84 | -0,10R | €-10,86 |
| Rapida 1H V2 | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -1,14R | €-11,43 |
| Rapida 1H V3 Filtered | ALT_ROTATION_DOWN | 3 | 22 | 22 | 27,27% | 0,52 | -0,35R | €-76,81 |
| Rapida 1H V3 Filtered | ALT_ROTATION_UP | 0 | 16 | 16 | 50,00% | 1,30 | 0,16R | €26,17 |
| Rapida 1H V3 Filtered | RANGE | 2 | 34 | 34 | 52,94% | 1,60 | 0,28R | €96,81 |
| Rapida 1H V3 Filtered | RANGE_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| Rapida 1H V3 Filtered | RANGE_LOW_VOL | 1 | 2 | 2 | 100,00% | ∞ | 1,47R | €29,42 |
| Rapida 1H V3 Filtered | TRANSITION | 0 | 8 | 8 | 62,50% | 2,25 | 0,51R | €40,77 |
| Rapida 1H V3 Filtered | TREND_DOWN | 1 | 2 | 2 | 0,00% | 0,00 | -1,02R | €-20,41 |
| Rapida 1H V3 Filtered | TREND_UP | 1 | 37 | 37 | 45,95% | 1,16 | 0,09R | €34,15 |
| Rapida 1H V3 Filtered | TREND_UP_HIGH_VOL | 0 | 20 | 20 | 25,00% | 0,49 | -0,36R | €-72,31 |
| SHADOW_1H_FAST_V3_CAP75_V1 | ALT_ROTATION_DOWN | 4 | 16 | 16 | 25,00% | 0,44 | -0,44R | €-70,78 |
| SHADOW_1H_FAST_V3_CAP75_V1 | ALT_ROTATION_UP | 1 | 17 | 17 | 41,18% | 0,91 | -0,06R | €-9,61 |
| SHADOW_1H_FAST_V3_CAP75_V1 | RANGE | 2 | 29 | 29 | 55,17% | 1,91 | 0,38R | €109,26 |
| SHADOW_1H_FAST_V3_CAP75_V1 | RANGE_LOW_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,48R | €29,66 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 1,43R | €28,69 |
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
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | ALT_ROTATION_DOWN | 3 | 21 | 21 | 28,57% | 0,56 | -0,31R | €-65,39 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | ALT_ROTATION_UP | 0 | 15 | 15 | 40,00% | 0,85 | -0,10R | €-14,95 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | RANGE | 1 | 33 | 33 | 51,52% | 1,51 | 0,25R | €81,94 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | RANGE_LOW_VOL | 1 | 2 | 2 | 100,00% | ∞ | 1,47R | €29,42 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TRANSITION | 0 | 3 | 3 | 100,00% | ∞ | 1,45R | €43,53 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_DOWN | 1 | 2 | 2 | 0,00% | 0,00 | -1,02R | €-20,41 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_UP | 1 | 20 | 20 | 25,00% | 0,45 | -0,44R | €-88,59 |
| SHADOW_4H_WIDE | ALT_ROTATION_DOWN | 2 | 2 | 2 | 100,00% | ∞ | 2,79R | €55,73 |
| SHADOW_4H_WIDE | ALT_ROTATION_UP | 3 | 3 | 3 | 0,00% | 0,00 | -1,01R | €-30,40 |
| SHADOW_4H_WIDE | RANGE | 9 | 22 | 22 | 27,27% | 1,02 | 0,01R | €2,99 |
| SHADOW_4H_WIDE | RANGE_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_4H_WIDE | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_4H_WIDE | TRANSITION | 3 | 7 | 7 | 14,29% | 0,46 | -0,47R | €-33,10 |
| SHADOW_4H_WIDE | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_4H_WIDE | TREND_UP | 3 | 15 | 15 | 40,00% | 1,81 | 0,50R | €74,71 |
| SHADOW_4H_WIDE | TREND_UP_HIGH_VOL | 4 | 4 | 4 | 0,00% | 0,00 | -1,01R | €-40,53 |
| SHADOW_BOLLINGER_MR_1H | ALT_ROTATION_DOWN | 1 | 5 | 5 | 60,00% | 1,99 | 0,43R | €21,52 |
| SHADOW_BOLLINGER_MR_1H | ALT_ROTATION_UP | 0 | 8 | 8 | 37,50% | 0,79 | -0,14R | €-11,49 |
| SHADOW_BOLLINGER_MR_1H | RANGE | 1 | 20 | 20 | 45,00% | 1,14 | 0,08R | €16,00 |
| SHADOW_BOLLINGER_MR_1H | RANGE_HIGH_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,49R | €29,73 |
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
| SHADOW_COMBO_ADAPTIVE | RANGE_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -1,03R | €-30,96 |
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
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -1,03R | €-30,96 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TRANSITION | 2 | 4 | 4 | 50,00% | 1,78 | 0,43R | €17,13 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_DOWN | 2 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_UP | 2 | 26 | 26 | 38,46% | 1,26 | 0,16R | €41,06 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_UP_HIGH_VOL | 0 | 14 | 14 | 14,29% | 0,33 | -0,57R | €-79,79 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | ALT_ROTATION_DOWN | 4 | 12 | 12 | 25,00% | 0,60 | -0,31R | €-37,55 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | ALT_ROTATION_UP | 2 | 10 | 10 | 40,00% | 1,18 | 0,12R | €11,78 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | RANGE | 3 | 29 | 29 | 48,28% | 1,71 | 0,39R | €113,05 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TRANSITION | 2 | 3 | 3 | 33,33% | 0,91 | -0,07R | €-1,99 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_DOWN | 2 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_UP | 2 | 13 | 13 | 7,69% | 0,17 | -0,74R | €-96,62 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_UP_HIGH_VOL | 0 | 7 | 7 | 14,29% | 0,30 | -0,64R | €-44,76 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TRANSITION | 0 | 3 | 3 | 33,33% | 0,92 | -0,06R | €-1,72 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TREND_UP | 2 | 6 | 6 | 16,67% | 0,38 | -0,54R | €-32,50 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TRANSITION | 0 | 3 | 3 | 33,33% | 0,92 | -0,06R | €-1,72 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TREND_UP | 2 | 6 | 6 | 16,67% | 0,38 | -0,54R | €-32,50 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | ALT_ROTATION_DOWN | 1 | 2 | 2 | 0,00% | 0,00 | -1,10R | €-21,95 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | ALT_ROTATION_UP | 1 | 2 | 2 | 0,00% | 0,00 | -1,03R | €-20,65 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | RANGE | 2 | 12 | 12 | 66,67% | 3,84 | 0,98R | €117,20 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TRANSITION | 0 | 2 | 2 | 50,00% | 1,90 | 0,46R | €9,15 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_UP | 1 | 3 | 3 | 0,00% | 0,00 | -1,04R | €-31,32 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TRANSITION | 2 | 8 | 8 | 25,00% | 0,60 | -0,32R | €-25,89 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TREND_UP | 2 | 23 | 23 | 17,39% | 0,41 | -0,49R | €-112,67 |
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
| SHADOW_COMBO_TREND | RANGE_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,76 |
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
| SHADOW_DONCHIAN_1H | RANGE_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -1,01R | €-30,40 |
| SHADOW_DONCHIAN_1H | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_DONCHIAN_1H | TRANSITION | 3 | 7 | 7 | 14,29% | 0,45 | -0,42R | €-29,27 |
| SHADOW_DONCHIAN_1H | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,16 |
| SHADOW_DONCHIAN_1H | TREND_UP | 0 | 14 | 14 | 35,71% | 1,28 | 0,19R | €26,97 |
| SHADOW_DONCHIAN_1H | TREND_UP_HIGH_VOL | 1 | 5 | 5 | 40,00% | 1,48 | 0,31R | €15,65 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | TRANSITION | 3 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_EMA_TREND_1H | ALT_ROTATION_DOWN | 4 | 9 | 9 | 22,22% | 0,57 | -0,35R | €-31,52 |
| SHADOW_EMA_TREND_1H | ALT_ROTATION_UP | 2 | 11 | 11 | 18,18% | 0,45 | -0,48R | €-52,68 |
| SHADOW_EMA_TREND_1H | RANGE | 4 | 29 | 29 | 41,38% | 1,54 | 0,31R | €91,14 |
| SHADOW_EMA_TREND_1H | RANGE_HIGH_VOL | 1 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,76 |
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
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TREND_UP | 2 | 17 | 17 | 5,88% | 0,12 | -0,83R | €-141,20 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | ALT_ROTATION_DOWN | 1 | 6 | 6 | 16,67% | 0,39 | -0,51R | €-30,82 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | ALT_ROTATION_UP | 0 | 6 | 6 | 33,33% | 0,90 | -0,07R | €-4,19 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | RANGE | 2 | 12 | 12 | 58,33% | 2,72 | 0,73R | €87,79 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TREND_UP | 2 | 19 | 19 | 5,26% | 0,11 | -0,85R | €-162,45 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | ALT_ROTATION_DOWN | 1 | 6 | 6 | 16,67% | 0,39 | -0,51R | €-30,82 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | RANGE | 2 | 12 | 12 | 58,33% | 2,72 | 0,73R | €87,79 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | RANGE_LOW_VOL | 0 | 2 | 2 | 50,00% | 1,86 | 0,44R | €8,76 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TREND_UP | 2 | 19 | 19 | 5,26% | 0,11 | -0,86R | €-162,63 |
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
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TREND_UP | 3 | 14 | 14 | 0,00% | 0,00 | -1,07R | €-149,48 |
| SHADOW_MASTER_ADAPTIVE_V1 | ALT_ROTATION_DOWN | 1 | 6 | 6 | 16,67% | 0,39 | -0,51R | €-30,82 |
| SHADOW_MASTER_ADAPTIVE_V1 | ALT_ROTATION_UP | 0 | 6 | 6 | 33,33% | 0,90 | -0,07R | €-4,19 |
| SHADOW_MASTER_ADAPTIVE_V1 | RANGE | 2 | 12 | 12 | 58,33% | 2,72 | 0,73R | €87,79 |
| SHADOW_MASTER_ADAPTIVE_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| SHADOW_MASTER_ADAPTIVE_V1 | TREND_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,18 |
| SHADOW_MASTER_ADAPTIVE_V1 | TREND_UP | 2 | 19 | 19 | 5,26% | 0,11 | -0,85R | €-162,45 |
| Forza relativa 1H V1 | ALT_ROTATION_DOWN | 5 | 9 | 9 | 11,11% | 0,26 | -0,69R | €-61,85 |
| Forza relativa 1H V1 | ALT_ROTATION_UP | 2 | 18 | 18 | 27,78% | 0,78 | -0,17R | €-30,25 |
| Forza relativa 1H V1 | RANGE | 5 | 39 | 39 | 33,33% | 1,07 | 0,05R | €18,42 |
| Forza relativa 1H V1 | RANGE_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -1,03R | €-31,02 |
| Forza relativa 1H V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| Forza relativa 1H V1 | TRANSITION | 0 | 17 | 17 | 47,06% | 1,88 | 0,48R | €80,99 |
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
| SHADOW_SCANNER_BOTTOM10_SHORT | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TRANSITION | 3 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM15_SHORT | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM15_SHORT | ALT_ROTATION_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM15_SHORT | RANGE | 2 | 6 | 6 | 0,00% | 0,00 | -1,11R | €-66,45 |
| SHADOW_SCANNER_BOTTOM15_SHORT | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TRANSITION | 3 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM20_SHORT | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM20_SHORT | ALT_ROTATION_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM20_SHORT | RANGE | 2 | 6 | 6 | 0,00% | 0,00 | -1,11R | €-66,45 |
| SHADOW_SCANNER_BOTTOM20_SHORT | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TRANSITION | 3 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM5_SHORT | ALT_ROTATION_DOWN | 2 | 5 | 5 | 60,00% | 2,62 | 0,71R | €35,50 |
| SHADOW_SCANNER_BOTTOM5_SHORT | ALT_ROTATION_UP | 1 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| SHADOW_SCANNER_BOTTOM5_SHORT | RANGE | 3 | 20 | 20 | 30,00% | 0,75 | -0,19R | €-37,65 |
| SHADOW_SCANNER_BOTTOM5_SHORT | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TRANSITION | 3 | 14 | 14 | 28,57% | 0,85 | -0,09R | €-13,14 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP | 0 | 7 | 7 | 0,00% | 0,00 | -0,73R | €-51,04 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -0,71R | €-21,38 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | ALT_ROTATION_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TRANSITION | 3 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_DOWN | 2 | 2 | 2 | 0,00% | 0,00 | -1,10R | €-22,10 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | ALT_ROTATION_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
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
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | ALT_ROTATION_UP | 0 | 4 | 4 | 0,00% | 0,00 | -1,07R | €-42,95 |
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

Generato: 2026-07-27T20:38:48+00:00

> Motore esclusivamente osservativo e Paper-only. Non modifica le uscite reali. I confronti escludono il funding sia dall'uscita originale sia dalle varianti.

## Stato operativo

- Gruppi di trade ancora monitorati: **664**
- Scenari virtuali ancora attivi: **12671**
- Gruppi in attesa dell'uscita originale: **350**
- Gruppi con originale chiuso ma Shadow ancora attive: **314**
- Confronti completati: **74747**

## Classifica osservativa complessiva

| Scenario | Campione completo | Campione totale | Δ medio vs originale | Migliora | Troppo presto | Troppo tardi | Stato dati |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| GB20_R050 | 2279 | 2344 | +€6,91 | 48,6% | 701 | 2 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R050 | 2279 | 2344 | +€5,08 | 47,0% | 717 | 17 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R050 | 2279 | 2344 | +€2,94 | 45,8% | 726 | 40 | READY_FOR_BLOCK4_EVALUATION |
| TP_R050 | 2279 | 2344 | +€2,17 | 45,1% | 789 | 1 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R050 | 2278 | 2343 | +€1,42 | 45,3% | 690 | 90 | READY_FOR_BLOCK4_EVALUATION |
| GB20_R100 | 2258 | 2323 | +€4,39 | 43,0% | 556 | 67 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R100 | 2258 | 2323 | +€2,47 | 42,2% | 546 | 95 | READY_FOR_BLOCK4_EVALUATION |
| TP_R100 | 2258 | 2323 | +€1,67 | 40,0% | 627 | 65 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R100 | 2258 | 2323 | +€1,18 | 42,4% | 458 | 159 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R100 | 2256 | 2321 | €-0,44 | 39,7% | 390 | 300 | READY_FOR_BLOCK4_EVALUATION |
| TIME_6H | 2253 | 2318 | €-3,97 | 42,8% | 493 | 416 | READY_FOR_BLOCK4_EVALUATION |
| ATR15_R100 | 2249 | 2314 | €-3,50 | 31,1% | 286 | 518 | READY_FOR_BLOCK4_EVALUATION |
| TIME_12H | 2247 | 2312 | €-4,82 | 36,9% | 288 | 605 | READY_FOR_BLOCK4_EVALUATION |
| TIME_24H | 2230 | 2295 | €-7,31 | 31,7% | 160 | 717 | READY_FOR_BLOCK4_EVALUATION |
| TP_R150 | 2217 | 2282 | +€2,43 | 31,6% | 319 | 256 | READY_FOR_BLOCK4_EVALUATION |
| ATR20_R100 | 2204 | 2269 | €-4,57 | 28,3% | 253 | 576 | READY_FOR_BLOCK4_EVALUATION |
| TP_R200 | 2179 | 2244 | +€2,99 | 36,8% | 165 | 397 | READY_FOR_BLOCK4_EVALUATION |
| ATR30_R100 | 2165 | 2230 | €-10,06 | 26,1% | 206 | 620 | READY_FOR_BLOCK4_EVALUATION |
| BE_R050 | 2143 | 2208 | €-10,54 | 29,3% | 448 | 446 | READY_FOR_BLOCK4_EVALUATION |
| BE_R100 | 2059 | 2124 | €-16,78 | 19,6% | 205 | 677 | READY_FOR_BLOCK4_EVALUATION |

## Come leggere il controllo

- **EARLIER_BETTER**: la variante è uscita prima e ha conservato più profitto.
- **TOO_EARLY**: la variante è uscita prima ma ha tagliato un movimento migliore.
- **LATER_BETTER**: la variante ha continuato dopo l'uscita originale e ha guadagnato di più.
- **TOO_LATE**: la variante è rimasta aperta più a lungo e ha peggiorato il risultato.

## Limiti e protezioni

Le regole Shadow mantengono entrata, quantità, commissioni, stop protettivo iniziale e liquidazione. Le ambiguità all'interno della stessa candela vengono risolte scegliendo l'esito peggiore. Le posizioni già aperte al momento dell'installazione sono marcate come campione parziale e non saranno utilizzate dal futuro Blocco 4 come prova piena.

# Blocco 4 — Valutazione statistica Shadow

Generato: 2026-07-27T20:38:52+00:00

> Modulo esclusivamente valutativo. Non modifica strategie, uscite, posizioni o capitale. Le candidature vengono consegnate al futuro Blocco 5, senza applicazione automatica.

## Stato

- Risultati Block 3 disponibili: **74747**
- Valutazioni prodotte: **16526**
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

Generato: 2026-07-27T20:39:41+00:00

Questi profili sono osservativi e Paper-only. Usano gli stessi trade della madre, ma applicano una specifica uscita Block 3 soltanto ai segnali aperti dopo la loro registrazione.
Nessuna promozione, modifica live o operazione reale viene eseguita automaticamente.

| Challenger | Madre | Scenario | Chiusi | Copertura | PF | PnL | Exp/trade | DD | Stato |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Rapida 1H V1 — giveback 20% dopo +0,5R | SHADOW_1H_FAST | GB20_R050 | 21 | 100,00% | 1,35 | +€125,64 | +€5,98 | 1,41% | COLLECTING |
| Rapida 1H V1 — giveback 30% dopo +0,5R | SHADOW_1H_FAST | GB30_R050 | 21 | 100,00% | 1,17 | +€60,61 | +€2,89 | 1,48% | COLLECTING |
| Relative Strength — giveback 20% dopo +0,5R | SHADOW_RELATIVE_STRENGTH | GB20_R050 | 13 | 100,00% | 1,24 | +€44,79 | +€3,45 | 0,91% | COLLECTING |
| Relative Strength — giveback 30% dopo +0,5R | SHADOW_RELATIVE_STRENGTH | GB30_R050 | 13 | 100,00% | 1,07 | +€13,30 | +€1,02 | 0,91% | COLLECTING |
| Scanner Top 5 BTC Strength — giveback 20% dopo +1,4R | SHADOW_SCANNER_TOP5_BTC | GB20_R140 | 4 | 80,00% | 0,00 | €-107,74 | €-26,93 | 1,08% | COLLECTING |
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

Generato: 2026-07-27T20:38:39+00:00

> Paper-only. In mercato NORMAL/WATCH non riduce i segnali. Le limitazioni iniziano soltanto in STRESS, RECOVERY, CRASH, EXTREME o con dati non affidabili.

## Stato corrente

- Livello: **NORMAL**
- Direzione: **NONE**
- Segnali bloccati nel ciclo: **0**
- Simulazioni bloccate attive: **14**
- Simulazioni completate nel ciclo: **0**
- Liquidazioni virtuali evitate totali: **0**
- Valore cumulato del filtro: **163.54 R**
- Profitto virtuale mancato: **260.98 R**

## Stress test portafogli Paper

| Scenario | Posizioni interessate | Liquidazioni stimate | Perdita stimata EUR |
| --- | ---: | ---: | ---: |
| DOWN_10 | 170 | 0 | 14489.30 |
| DOWN_20 | 170 | 0 | 28978.60 |
| DOWN_30 | 170 | 1 | 43468.79 |
| DOWN_40 | 170 | 49 | 55955.57 |
| UP_10 | 180 | 0 | 26844.12 |
| UP_20 | 180 | 0 | 53688.24 |
| UP_30 | 180 | 0 | 80532.35 |
| UP_40 | 180 | 93 | 96390.11 |

## Modello di esecuzione

Se una candela di cascata attraversa nello stesso intervallo sia lo stop sia il prezzo di liquidazione, il Paper usa il caso peggiore e registra una liquidazione intrabar. Gli stop in gap o in regime di stress ricevono slippage aggiuntivo.

## Requisiti prima del live futures

- modalità ISOLATED obbligatoria;
- stop nativo sull'exchange;
- conferma dello stop prima di accettare la posizione;
- cross margin vietato.

# Blocco 5 — Candidati evolutivi controllati

Generato: 2026-07-27T20:38:13+00:00

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

Generato: 2026-07-27T20:39:42+00:00

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

Generato: 2026-07-27T20:39:42+00:00

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

Generato: 2026-07-27T20:39:42+00:00

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

Generato: 2026-07-27T20:39:42+00:00

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
| 1 | SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_V1 | BASELINE | 21.1 | E | 35 | 2.10 | 0.292 | 3.00 |
| 2 | SHADOW_DONCHIAN_1H | BASELINE | 19.8 | E | 30 | 1.84 | 0.352 | 2.18 |
| 3 | SHADOW_1H_FAST_NOHIGH_CAP75_V1 | BASELINE | 17.5 | E | 58 | 1.54 | 0.210 | 5.40 |
| 4 | SHADOW_1H_FAST_V3_CAP75_V1 | BASELINE | 16.5 | E | 51 | 1.46 | 0.174 | 3.68 |
| 5 | SHADOW_1H_FAST_V3 | BASELINE | 16.1 | E | 84 | 1.25 | 0.103 | 5.36 |
| 6 | SHADOW_1H_FAST_SCORE_6_75_V1 | BASELINE | 15.7 | E | 57 | 1.36 | 0.136 | 3.71 |
| 7 | SHADOW_1H_FAST_NO_PEPE_V1 | BASELINE | 15.7 | E | 49 | 1.42 | 0.172 | 3.55 |
| 8 | SHADOW_1H_BALANCED_V3 | BASELINE | 15.2 | E | 52 | 1.39 | 0.177 | 4.23 |
| 9 | SHADOW_SCANNER_TOP5_LONG | BASELINE | 15.2 | E | 45 | 1.47 | 0.216 | 7.52 |
| 10 | SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | BASELINE | 13.0 | E | 58 | 1.18 | 0.079 | 4.74 |

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

Generato: 2026-07-27T20:39:42+00:00

> Paper-only e advisory. Il blocco misura quali strategie funzionano nei diversi regimi, ma non cambia automaticamente strategia o posizione.

## Stato

- Regime corrente: **HIGH_VOLATILITY**
- Righe di performance: **517**
- Strategie preferite nel regime corrente: **0**
- Strategie da evitare nel regime corrente: **0**
- Memorie contestuali: **245**
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

Generato: 2026-07-27T20:39:42+00:00

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

Generato: 2026-07-27T20:38:39+00:00

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
