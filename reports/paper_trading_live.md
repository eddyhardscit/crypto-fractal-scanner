# Paper trading automatico KuCoin

Generato: 2026-09-21T19:11:13+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-09-21T19:06:33+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-09-21T19:06:33+00:00 | 2026-09-21T19:06:33+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-09-21T18:45:00+00:00 | 2026-09-21T18:45:00+00:00 | 6,7 min | 25,0 min | OK |
| 60m | 12 | 2026-09-21T18:00:00+00:00 | 2026-09-21T18:00:00+00:00 | 6,7 min | 45,0 min | OK |
| 240m | 12 | 2026-09-21T12:00:00+00:00 | 2026-09-21T12:00:00+00:00 | 3,11 h | 1,00 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Doge Bollinger 1H | DOGE | 60m | LONG | 5,44 | 5,00 | 0,00 | OPENED | 6,7 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Doge Donchian 1H | DOGE | 60m | LONG | 5,44 | 5,00 | 0,00 | OPENED | 6,7 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Doge Ema 1H | DOGE | 60m | LONG | 5,44 | 5,00 | 0,00 | OPENED | 6,7 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive — target pieno 3R | DOGE | 60m | LONG | 5,44 | 5,00 | 0,00 | OPENED | 6,7 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | DOGE | 60m | LONG | 5,44 | 5,00 | 0,00 | OPENED | 6,7 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive — Trend/Transition | XRP | 60m | LONG | 5,10 | 5,00 | 0,00 | OPENED | 6,7 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive — Trend/Transition | DOGE | 60m | LONG | 5,44 | 5,00 | 0,00 | OPENED | 6,7 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Principale 4H | AKE | 240m | LONG | 8,25 | 6,00 | 0,00 | STALE_CANDLE | 3,11 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 186.7 minuti; tolleranza 60 minuti. |
| Principale 4H | NEAR | 240m | LONG | 7,75 | 6,00 | 0,00 | STALE_CANDLE | 3,11 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 186.7 minuti; tolleranza 60 minuti. |
| Principale 4H | PEPE | 240m | LONG | 7,75 | 6,00 | 0,00 | STALE_CANDLE | 3,11 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 186.7 minuti; tolleranza 60 minuti. |
| Principale 4H | ETH | 240m | LONG | 6,30 | 6,00 | 0,00 | STALE_CANDLE | 3,11 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 186.7 minuti; tolleranza 60 minuti. |
| Principale 4H | SUI | 240m | LONG | 6,25 | 6,00 | 0,00 | STALE_CANDLE | 3,11 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 186.7 minuti; tolleranza 60 minuti. |
| Principale 4H | SOL | 240m | LONG | 6,20 | 6,00 | 0,00 | STALE_CANDLE | 3,11 h | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 186.7 minuti; tolleranza 60 minuti. |
| Principale 4H | XMR | 240m | LONG | 6,06 | 6,00 | 0,00 | STALE_CANDLE | 3,11 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 186.7 minuti; tolleranza 60 minuti. |
| Principale 4H | HYPE | 240m | LONG | 5,88 | 6,00 | 0,12 | STALE_CANDLE | 3,11 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 186.7 minuti; tolleranza 60 minuti. |
| Principale 4H | ZEC | 240m | LONG | 4,98 | 6,00 | 1,02 | STALE_CANDLE | 3,11 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 186.7 minuti; tolleranza 60 minuti. |
| Principale 4H | BTC | 240m | LONG | 4,75 | 6,00 | 1,25 | STALE_CANDLE | 3,11 h | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 186.7 minuti; tolleranza 60 minuti. |
| Principale 4H | DOGE | 240m | LONG | 4,66 | 6,00 | 1,34 | STALE_CANDLE | 3,11 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 186.7 minuti; tolleranza 60 minuti. |
| Principale 4H | XRP | 240m | LONG | 4,31 | 6,00 | 1,69 | STALE_CANDLE | 3,11 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 186.7 minuti; tolleranza 60 minuti. |
| Forza relativa 1H V1 | SUI | 60m | LONG | 6,25 | 4,00 | 0,00 | READY | 6,7 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Scanner Top 5 Long 1H | SUI | 60m | LONG | 6,25 | 5,00 | 0,00 | READY | 6,7 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Bilanciata 1H — LONG senza Range High Vol | DOGE | 60m | LONG | 5,44 | 5,00 | 0,00 | READY | 6,7 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Rapida V1 — senza PEPE | DOGE | 60m | LONG | 5,44 | 4,50 | 0,00 | OPENED | 6,7 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Forza relativa 1H V1 | DOGE | 60m | LONG | 5,44 | 4,00 | 0,00 | READY | 6,7 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Scanner Top 5 Long 1H | DOGE | 60m | LONG | 5,44 | 5,00 | 0,00 | READY | 6,7 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Scanner Top15 Long | DOGE | 60m | LONG | 5,44 | 5,00 | 0,00 | READY | 6,7 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Scanner Top20 Long | DOGE | 60m | LONG | 5,44 | 5,00 | 0,00 | READY | 6,7 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Tutti i filtri del generatore sono stati superati. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €10.160,40 | +1,60% | €351,84 | €3.000,00 | 11,73% | 2 | 71 | 46,48% | 1,07 | 6,86% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 71 | 3945 | PRIME INDICAZIONI | 100 (mancano 29) |

- Trade del Principale 4H chiusi: **71**; win rate **46,48%**; profit factor **1,07**.
- Expectancy: **€1,66** per trade; P&L netto: **€117,93**; max drawdown: **6,86%**.
- Valutazione: **Si può osservare la direzione, ma il risultato resta fragile.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 2 | €10.160,40 | €189,87 | €569,60 | €5,84 | €42,82 |
| TEST | Benchmark Donchian breakout 1H | 1 | €12.675,04 | €21,82 | €43,64 | €2,77 | €0,00 |
| TEST | Donchian 1H Gb20 120R V1 | 1 | €12.376,62 | €21,31 | €42,62 | €2,71 | €0,00 |
| TEST | Rapida score 6–7,5 — Cost Aware | 2 | €11.623,91 | €930,32 | €2.790,95 | €116,07 | €16,38 |
| TEST | Combo Trend — Side × Regime Guard | 2 | €11.615,95 | €578,19 | €1.156,38 | €60,79 | €-2,13 |
| TEST | Rapida V3 senza ESPORTS — Stress Guard | 0 | €11.427,03 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 NoHigh — Regime Guard | 2 | €11.304,69 | €1.859,99 | €5.579,96 | €113,75 | €27,13 |
| TEST | Rapida V1 — senza PEPE | 3 | €11.304,47 | €1.690,45 | €5.071,35 | €170,05 | €4,54 |
| TEST | Scanner Top 5 Long 1H | 5 | €11.098,77 | €2.772,53 | €5.545,06 | €168,33 | €36,75 |
| TEST | Rapida V3 senza ESPORTS — MFE Lock | 4 | €11.044,40 | €2.690,87 | €8.072,62 | €220,28 | €41,93 |
| TEST | Rapida 1H V3 Filtered — madre | 4 | €10.973,44 | €2.673,58 | €8.020,75 | €218,87 | €41,66 |
| TEST | Rapida V1 — target pieno 2R | 0 | €10.941,17 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — madre | 5 | €10.927,25 | €2.083,53 | €4.167,05 | €218,27 | €-2,06 |
| TEST | MAIN — Side × Regime Guard | 0 | €10.894,47 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — Side × Regime Guard | 3 | €10.825,77 | €1.610,67 | €3.221,34 | €160,99 | €-36,17 |
| TEST | Combo Adaptive — Long Only | 2 | €10.813,09 | €1.086,83 | €2.173,65 | €105,61 | €11,12 |
| TEST | Scanner Top15 Long | 5 | €10.732,52 | €2.051,13 | €4.102,26 | €214,93 | €-15,91 |
| TEST | Scanner Top20 Long | 5 | €10.732,52 | €2.051,13 | €4.102,26 | €214,93 | €-15,91 |
| TEST | Rapida V3 — no volatilità HIGH | 2 | €10.690,32 | €1.758,90 | €5.276,71 | €107,57 | €25,66 |
| TEST | Rapida 1H V2 | 0 | €10.626,23 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — parziale 1R | 5 | €10.608,28 | €2.017,13 | €4.034,26 | €211,90 | €-6,90 |
| TEST | Rapida V3 senza ESPORTS — Long Only | 4 | €10.580,40 | €2.577,82 | €7.733,47 | €211,03 | €40,17 |
| TEST | Scanner Top 5 + forza BTC 1H | 5 | €10.549,91 | €2.632,09 | €5.264,17 | €160,54 | €37,60 |
| TEST | Rapida V1 — no HIGH + score <7,5 | 0 | €10.532,39 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Scanner | 3 | €10.518,84 | €1.598,60 | €3.197,21 | €155,54 | €10,76 |
| TEST | Scanner Top10 Long | 2 | €10.407,34 | €459,62 | €919,24 | €52,10 | €-0,84 |
| TEST | Sol Donchian 1H | 0 | €10.372,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H V3 Filtered | 2 | €10.362,64 | €358,63 | €1.075,89 | €50,98 | €-6,68 |
| TEST | Rapida V3 — senza ESPORTS | 4 | €10.355,64 | €2.523,06 | €7.569,18 | €206,55 | €39,31 |
| TEST | Ampia 4H | 2 | €10.313,10 | €447,56 | €895,11 | €100,79 | €72,93 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 0 | €10.300,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 0 | €10.271,73 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | FAST NoHigh <7,5 · SHORT only | 0 | €10.270,06 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | MAIN — Dynamic Asset Selector | 0 | €10.264,13 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Forza relativa 1H V2 | 4 | €10.249,19 | €1.850,08 | €3.700,15 | €204,08 | €-9,08 |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 0 | €10.239,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 0 | €10.235,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 — Long Only | 4 | €10.208,21 | €2.487,14 | €7.461,43 | €203,61 | €38,75 |
| TEST | Rapida V3 NoHigh — Range Only | 0 | €10.205,57 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 1H | 0 | €10.203,50 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Donchian 1H | 1 | €10.201,04 | €582,66 | €1.747,97 | €51,01 | €-0,35 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 0 | €10.185,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Ema 1H | 1 | €10.179,20 | €516,80 | €1.550,40 | €50,90 | €-0,31 |
| TEST | Rapida score 6–7,5 — Range Only | 0 | €10.175,88 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Benchmark trend following EMA 1H | 2 | €10.147,80 | €488,59 | €977,17 | €51,47 | €-1,87 |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 0 | €10.145,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 4H | 0 | €10.138,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 4H | 0 | €10.101,88 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 0 | €10.099,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €10.058,95 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 0 | €10.048,77 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V1 — madre | 0 | €10.043,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 1H | 0 | €10.040,81 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Donchian 4H | 0 | €10.040,14 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €50 · 15x | 0 | €10.020,29 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · prudente · 5x | 0 | €10.019,53 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 0 | €10.011,79 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €50 · 15x | 0 | €10.011,55 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 0 | €10.008,92 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 4H | 0 | €10.005,51 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €10 · 15x | 0 | €10.004,06 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 0 | €10.003,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 1H | 0 | €10.002,55 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €10 · 15x | 0 | €10.002,31 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H — SHORT Trend Down stretto | 0 | €10.002,17 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Continuation V1 | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €10 · 15x | 0 | €9.997,71 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 0 | €9.995,23 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €10 · 15x | 0 | €9.993,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · prudente · 5x | 0 | €9.991,19 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €50 · 15x | 0 | €9.988,57 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €10 · 15x | 0 | €9.985,57 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 4H | 0 | €9.980,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €50 · 15x | 0 | €9.966,02 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 4H | 0 | €9.964,84 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.956,17 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · prudente · 5x | 0 | €9.955,89 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · prudente · 5x | 0 | €9.951,01 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 0 | €9.940,92 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 1H | 0 | €9.939,78 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 1H | 0 | €9.934,84 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €50 · 15x | 0 | €9.927,87 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — Quality7 + Regime + parziale 1R | 1 | €9.927,86 | €476,08 | €952,17 | €49,68 | €-6,75 |
| TEST | Top 5 + BTC — target pieno 3R | 2 | €9.918,84 | €781,73 | €1.563,46 | €48,66 | €56,31 |
| TEST | Btc Ema 4H | 0 | €9.914,14 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Top 5 + BTC — 75% a 2,2R + runner 3R | 2 | €9.913,04 | €781,27 | €1.562,54 | €48,63 | €56,28 |
| TEST | Rapida score 6–7,5 — senza Trend Up | 0 | €9.902,86 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 — qualità completa + profit lock | 0 | €9.902,55 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 — Long + no HIGH + score <7,5 | 0 | €9.891,96 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Top 5 + BTC — solo MFE | 5 | €9.890,02 | €2.467,45 | €4.934,90 | €150,50 | €35,25 |
| TEST | Eth Bollinger 1H | 0 | €9.868,16 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V1 — score 6–7,5 | 0 | €9.862,02 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Trend | 2 | €9.840,70 | €473,80 | €947,60 | €49,91 | €-1,81 |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 0 | €9.837,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 0 | €9.817,34 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 4H | 0 | €9.808,89 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata V3 · LONG only | 2 | €9.804,15 | €339,30 | €1.017,91 | €48,23 | €-6,32 |
| TEST | Combo Adaptive — Quality7 + Regime | 1 | €9.802,98 | €470,10 | €940,19 | €49,05 | €-6,67 |
| TEST | Eth Ema 4H | 0 | €9.783,14 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Top 5 + BTC — Guard | 3 | €9.780,78 | €1.486,44 | €2.972,88 | €144,62 | €10,00 |
| TEST | Global Confluence puro 1H | 0 | €9.779,96 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 0 | €9.762,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Bollinger 1H | 1 | €9.759,64 | €594,61 | €1.783,84 | €48,81 | €-0,36 |
| TEST | Combo Adaptive — Quality7 | 3 | €9.745,73 | €1.433,99 | €2.867,98 | €145,42 | €-1,55 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 0 | €9.723,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — 75% a 2R + runner 25% a 3R | 6 | €9.720,99 | €1.811,46 | €3.622,93 | €194,42 | €-15,47 |
| TEST | Bilanciata 1H V2 | 3 | €9.692,97 | €859,62 | €2.578,87 | €144,93 | €-2,01 |
| TEST | Eth Donchian 1H | 0 | €9.676,47 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 1H | 0 | €9.668,82 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H — LONG senza Range High Vol | 5 | €9.637,16 | €1.255,80 | €3.767,40 | €192,59 | €19,13 |
| TEST | Master Adaptive GB20 — Breakeven 0,5R | 3 | €9.627,49 | €1.359,67 | €2.719,34 | €142,27 | €4,33 |
| TEST | Master Adaptive GB20 — 50% a 0,75R | 3 | €9.617,26 | €1.358,22 | €2.716,45 | €142,12 | €4,33 |
| TEST | Master Adaptive Runner25 V1 | 5 | €9.586,54 | €1.816,95 | €3.633,90 | €192,00 | €66,47 |
| TEST | Master Adaptive V1 | 3 | €9.580,06 | €1.352,97 | €2.705,94 | €141,57 | €4,31 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 0 | €9.579,83 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Top 5 + BTC — Guard + MFE | 4 | €9.543,10 | €1.467,43 | €2.934,85 | €143,60 | €9,77 |
| TEST | Combo Adaptive — Trend/Transition | 4 | €9.540,70 | €2.658,13 | €5.316,25 | €190,85 | €0,02 |
| TEST | Combo Adaptive — target pieno 3R | 6 | €9.539,13 | €1.777,58 | €3.555,15 | €190,78 | €-15,18 |
| TEST | Scanner Bottom10 Short | 0 | €9.530,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom15 Short | 0 | €9.530,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom20 Short | 0 | €9.530,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive GB20 — Loss Cap 0,75R | 3 | €9.473,23 | €1.774,50 | €3.549,00 | €139,23 | €5,67 |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | 0 | €9.464,68 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Ema 1H | 1 | €9.463,42 | €866,56 | €2.599,67 | €0,00 | €50,72 |
| TEST | Eth Adaptive 1H | 0 | €9.459,83 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 — score <7,5 | 0 | €9.454,76 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Gb20 V1 | 3 | €9.453,65 | €1.335,12 | €2.670,23 | €139,70 | €4,26 |
| TEST | Scanner Bottom5 Short Profit Lock V1 | 0 | €9.450,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Expanded V1 | 3 | €9.382,53 | €1.325,07 | €2.650,15 | €138,65 | €4,22 |
| TEST | Scanner Bottom 5 Short 1H | 0 | €9.377,56 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H V1 | 4 | €9.354,53 | €952,28 | €2.856,85 | €141,79 | €-24,32 |
| TEST | Btc Ema 1H | 0 | €9.353,69 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — MFE Trail esistente | 2 | €9.352,19 | €940,29 | €1.880,59 | €46,19 | €9,62 |
| TEST | Rapida V1 — Long + BTC 1–3 + score <7,5 | 0 | €9.205,17 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Top 5 + BTC — BTC 2–3 | 2 | €9.165,38 | €863,85 | €1.727,70 | €89,85 | €-6,12 |
| TEST | Top 5 + BTC — Guard + BTC≤3 | 1 | €9.075,88 | €387,55 | €775,09 | €44,34 | €0,00 |
| TEST | Forza relativa 1H V1 | 5 | €8.841,81 | €1.713,66 | €3.427,31 | €174,70 | €-7,44 |
| TEST | Top 5 + BTC — Guard + BTC≤3 + MFE | 1 | €8.647,30 | €369,38 | €738,77 | €42,26 | €0,00 |
| TEST | Top 5 + BTC — BTC≤3 | 1 | €8.614,01 | €367,75 | €735,49 | €42,07 | €0,00 |
| TEST | Combo Mean Reversion | 0 | €8.553,84 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Strict3 V1 | 0 | €8.448,19 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive No Alt V1 | 0 | €8.413,97 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Benchmark Bollinger mean reversion 1H | 0 | €7.569,99 | €0,00 | €0,00 | €0,00 | €0,00 |

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
| PRINCIPALE | Principale 4H | Confluenza trend | €10.160,40 | €117,93 | 71 | 71 | 46,48% | 1,07 | €1,66 | 6,86% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €12.675,04 | €2.675,07 | 178 | 178 | 46,63% | 1,74 | €15,03 | 6,75% |
| TEST | Donchian 1H Gb20 120R V1 | Donchian breakout 20 barre | €12.376,62 | €2.376,65 | 146 | 146 | 45,89% | 1,88 | €16,28 | 6,75% |
| TEST | Rapida score 6–7,5 — Cost Aware | Momentum / breakout | €11.623,91 | €1.609,21 | 227 | 227 | 50,66% | 1,37 | €7,09 | 7,95% |
| TEST | Combo Trend — Side × Regime Guard | Combo Trend | €11.615,95 | €1.618,77 | 171 | 171 | 52,05% | 1,54 | €9,47 | 10,10% |
| TEST | Rapida V3 senza ESPORTS — Stress Guard | Momentum / breakout V3 Filtered | €11.427,03 | €1.427,03 | 194 | 194 | 50,52% | 1,38 | €7,36 | 5,29% |
| TEST | Rapida V3 NoHigh — Regime Guard | Momentum / breakout V3 Filtered | €11.304,69 | €1.225,20 | 203 | 202 | 51,72% | 1,42 | €6,04 | 5,24% |
| TEST | Rapida V1 — senza PEPE | Momentum / breakout | €11.304,47 | €1.302,08 | 322 | 321 | 45,65% | 1,26 | €4,04 | 9,28% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €11.098,77 | €1.065,35 | 207 | 207 | 46,38% | 1,29 | €5,15 | 8,85% |
| TEST | Rapida V3 senza ESPORTS — MFE Lock | Momentum / breakout V3 Filtered | €11.044,40 | €1.007,31 | 257 | 257 | 51,36% | 1,25 | €3,92 | 9,50% |
| TEST | Rapida 1H V3 Filtered — madre | Momentum / breakout V3 Filtered | €10.973,44 | €936,59 | 301 | 301 | 46,84% | 1,18 | €3,11 | 9,48% |
| TEST | Rapida V1 — target pieno 2R | Momentum / breakout | €10.941,17 | €941,17 | 306 | 306 | 42,16% | 1,19 | €3,08 | 6,56% |
| TEST | Combo Adaptive — madre | Combo Adaptive | €10.927,25 | €931,81 | 244 | 244 | 47,95% | 1,26 | €3,82 | 8,17% |
| TEST | MAIN — Side × Regime Guard | Confluenza trend | €10.894,47 | €894,47 | 65 | 65 | 53,85% | 1,77 | €13,76 | 8,20% |
| TEST | Combo Adaptive — Side × Regime Guard | Combo Adaptive | €10.825,77 | €863,87 | 196 | 196 | 46,43% | 1,27 | €4,41 | 11,68% |
| TEST | Combo Adaptive — Long Only | Combo Adaptive | €10.813,09 | €803,27 | 200 | 200 | 46,00% | 1,24 | €4,02 | 7,78% |
| TEST | Scanner Top15 Long | Scanner Top15 Long | €10.732,52 | €750,89 | 233 | 233 | 49,36% | 1,21 | €3,22 | 10,31% |
| TEST | Scanner Top20 Long | Scanner Top20 Long | €10.732,52 | €750,89 | 233 | 233 | 49,36% | 1,21 | €3,22 | 10,31% |
| TEST | Rapida V3 — no volatilità HIGH | Momentum / breakout V3 Filtered | €10.690,32 | €663,61 | 228 | 227 | 47,37% | 1,21 | €2,91 | 7,10% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €10.626,23 | €626,23 | 95 | 85 | 48,42% | 1,28 | €6,59 | 3,89% |
| TEST | Combo Adaptive — parziale 1R | Combo Adaptive | €10.608,28 | €617,61 | 202 | 202 | 47,52% | 1,21 | €3,06 | 8,69% |
| TEST | Rapida V3 senza ESPORTS — Long Only | Momentum / breakout V3 Filtered | €10.580,40 | €544,88 | 291 | 291 | 44,33% | 1,10 | €1,87 | 10,60% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €10.549,91 | €515,46 | 172 | 172 | 46,51% | 1,15 | €3,00 | 11,27% |
| TEST | Rapida V1 — no HIGH + score <7,5 | Momentum / breakout | €10.532,39 | €532,39 | 241 | 241 | 44,81% | 1,13 | €2,21 | 10,86% |
| TEST | Combo Scanner | Combo Scanner | €10.518,84 | €510,00 | 204 | 204 | 45,10% | 1,13 | €2,50 | 11,38% |
| TEST | Scanner Top10 Long | Scanner Top10 Long | €10.407,34 | €408,74 | 214 | 214 | 46,73% | 1,13 | €1,91 | 10,31% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €10.372,12 | €372,12 | 25 | 25 | 60,00% | 1,88 | €14,88 | 2,77% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €10.362,64 | €369,97 | 237 | 237 | 43,04% | 1,09 | €1,56 | 14,04% |
| TEST | Rapida V3 — senza ESPORTS | Momentum / breakout V3 Filtered | €10.355,64 | €320,87 | 264 | 264 | 45,45% | 1,07 | €1,22 | 10,92% |
| TEST | Ampia 4H | Confluenza trend | €10.313,10 | €240,70 | 70 | 70 | 34,29% | 1,15 | €3,44 | 4,45% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | Momentum / breakout V3 Filtered | €10.300,05 | €300,05 | 33 | 33 | 48,48% | 2,04 | €9,09 | 2,01% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | Momentum / breakout V3 Filtered | €10.271,73 | €271,73 | 22 | 22 | 50,00% | 1,74 | €12,35 | 1,72% |
| TEST | FAST NoHigh <7,5 · SHORT only | Momentum / breakout | €10.270,06 | €270,06 | 204 | 204 | 44,12% | 1,08 | €1,32 | 10,86% |
| TEST | MAIN — Dynamic Asset Selector | Confluenza trend | €10.264,13 | €264,13 | 26 | 26 | 38,46% | 1,36 | €10,16 | 3,39% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €10.249,19 | €260,49 | 158 | 150 | 42,41% | 1,07 | €1,65 | 10,88% |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | Momentum / breakout V3 Filtered | €10.239,20 | €239,20 | 17 | 17 | 52,94% | 4,50 | €14,07 | 1,01% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | Momentum / breakout V3 Filtered | €10.235,18 | €235,18 | 20 | 20 | 50,00% | 1,90 | €11,76 | 2,73% |
| TEST | Rapida V3 — Long Only | Momentum / breakout V3 Filtered | €10.208,21 | €173,93 | 294 | 294 | 43,88% | 1,03 | €0,59 | 12,52% |
| TEST | Rapida V3 NoHigh — Range Only | Momentum / breakout V3 Filtered | €10.205,57 | €205,57 | 121 | 121 | 42,15% | 1,08 | €1,70 | 7,07% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.203,50 | €203,50 | 9 | 9 | 77,78% | 2,77 | €22,61 | 0,85% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €10.201,04 | €202,44 | 20 | 20 | 60,00% | 1,43 | €10,12 | 3,08% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | Momentum / breakout V3 Filtered | €10.185,37 | €185,37 | 22 | 22 | 40,91% | 1,57 | €8,43 | 2,27% |
| TEST | Doge Ema 1H | Trend following EMA | €10.179,20 | €180,44 | 31 | 31 | 61,29% | 1,28 | €5,82 | 2,77% |
| TEST | Rapida score 6–7,5 — Range Only | Momentum / breakout | €10.175,88 | €175,88 | 77 | 77 | 44,16% | 1,11 | €2,28 | 6,49% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €10.147,80 | €150,26 | 172 | 172 | 43,02% | 1,05 | €0,87 | 12,31% |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | Momentum / breakout V3 Filtered | €10.145,12 | €145,12 | 44 | 44 | 45,45% | 1,20 | €3,30 | 2,91% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €10.138,72 | €138,72 | 10 | 10 | 50,00% | 1,64 | €13,87 | 1,37% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.101,88 | €101,88 | 4 | 4 | 75,00% | 2,86 | €25,47 | 0,91% |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | Momentum / breakout V3 Filtered | €10.099,04 | €99,04 | 55 | 55 | 54,55% | 1,12 | €1,80 | 3,59% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €10.058,95 | €58,95 | 34 | 34 | 47,06% | 1,40 | €1,73 | 0,33% |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | Momentum / breakout V3 Filtered | €10.048,77 | €48,77 | 23 | 23 | 43,48% | 1,12 | €2,12 | 3,05% |
| TEST | Rapida 1H V1 — madre | Momentum / breakout | €10.043,28 | €43,28 | 78 | 78 | 34,62% | 1,02 | €0,55 | 6,76% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €10.040,81 | €40,81 | 31 | 31 | 48,39% | 1,05 | €1,32 | 4,59% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €10.040,14 | €40,14 | 9 | 9 | 33,33% | 1,15 | €4,46 | 2,25% |
| TEST | Scalp RSI Short 85 · €50 · 15x | Inversione RSI estrema 15m | €10.020,29 | €20,29 | 7 | 7 | 57,14% | 1,71 | €2,90 | 0,31% |
| TEST | Scalp RSI Long 20 · prudente · 5x | Inversione RSI estrema 15m | €10.019,53 | €19,53 | 12 | 12 | 50,00% | 1,39 | €1,63 | 0,36% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €10.011,79 | €11,79 | 34 | 34 | 47,06% | 1,40 | €0,35 | 0,07% |
| TEST | Scalp RSI Short 80 · €50 · 15x | Inversione RSI estrema 15m | €10.011,55 | €11,55 | 19 | 19 | 42,11% | 1,20 | €0,61 | 0,53% |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | Momentum / breakout V3 Filtered | €10.008,92 | €8,92 | 30 | 30 | 36,67% | 1,02 | €0,30 | 4,84% |
| TEST | Sol Ema 4H | Trend following EMA | €10.005,51 | €5,51 | 11 | 11 | 36,36% | 1,02 | €0,50 | 2,27% |
| TEST | Scalp RSI Short 85 · €10 · 15x | Inversione RSI estrema 15m | €10.004,06 | €4,06 | 7 | 7 | 57,14% | 1,71 | €0,58 | 0,06% |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | Momentum / breakout V3 Filtered | €10.003,37 | €3,37 | 8 | 8 | 37,50% | 1,02 | €0,42 | 2,15% |
| TEST | Sol Ema 1H | Trend following EMA | €10.002,55 | €2,55 | 33 | 33 | 42,42% | 1,00 | €0,08 | 4,45% |
| TEST | Scalp RSI Short 80 · €10 · 15x | Inversione RSI estrema 15m | €10.002,31 | €2,31 | 19 | 19 | 42,11% | 1,20 | €0,12 | 0,11% |
| TEST | Bilanciata 1H — SHORT Trend Down stretto | Confluenza trend | €10.002,17 | €2,17 | 15 | 15 | 40,00% | 1,01 | €0,14 | 1,80% |
| TEST | Scanner Bottom5 Short Continuation V1 | Scanner Bottom5 Short Continuation | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 20 · €10 · 15x | Inversione RSI estrema 15m | €9.997,71 | €-2,29 | 12 | 12 | 33,33% | 0,62 | €-0,19 | 0,04% |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | Momentum / breakout V3 Filtered | €9.995,23 | €-4,77 | 15 | 15 | 46,67% | 0,99 | €-0,32 | 2,70% |
| TEST | Scalp RSI Long 15 · €10 · 15x | Inversione RSI estrema 15m | €9.993,20 | €-6,80 | 5 | 5 | 20,00% | 0,05 | €-1,36 | 0,07% |
| TEST | Scalp RSI Short 85 · prudente · 5x | Inversione RSI estrema 15m | €9.991,19 | €-8,81 | 7 | 7 | 57,14% | 0,68 | €-1,26 | 0,30% |
| TEST | Scalp RSI Long 20 · €50 · 15x | Inversione RSI estrema 15m | €9.988,57 | €-11,43 | 12 | 12 | 33,33% | 0,62 | €-0,95 | 0,21% |
| TEST | Scalp RSI Long 25 · €10 · 15x | Inversione RSI estrema 15m | €9.985,57 | €-14,43 | 22 | 22 | 36,36% | 0,31 | €-0,66 | 0,17% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €9.980,98 | €-19,02 | 5 | 5 | 40,00% | 0,88 | €-3,80 | 1,96% |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | €9.966,02 | €-33,98 | 5 | 5 | 20,00% | 0,05 | €-6,80 | 0,34% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €9.964,84 | €-35,16 | 4 | 4 | 25,00% | 0,77 | €-8,79 | 1,10% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.956,17 | €-43,83 | 34 | 34 | 47,06% | 0,76 | €-1,29 | 0,84% |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | €9.955,89 | €-44,11 | 5 | 5 | 20,00% | 0,09 | €-8,82 | 0,45% |
| TEST | Scalp RSI Short 80 · prudente · 5x | Inversione RSI estrema 15m | €9.951,01 | €-48,99 | 19 | 19 | 36,84% | 0,53 | €-2,58 | 0,89% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €9.940,92 | €-59,08 | 22 | 22 | 31,82% | 0,53 | €-2,69 | 0,73% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €9.939,78 | €-60,22 | 16 | 16 | 50,00% | 0,85 | €-3,76 | 1,98% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €9.934,84 | €-65,16 | 14 | 14 | 50,00% | 0,80 | €-4,65 | 2,06% |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | €9.927,87 | €-72,13 | 22 | 22 | 36,36% | 0,31 | €-3,28 | 0,86% |
| TEST | Combo Adaptive — Quality7 + Regime + parziale 1R | Combo Adaptive | €9.927,86 | €-64,82 | 58 | 58 | 50,00% | 0,95 | €-1,12 | 4,27% |
| TEST | Top 5 + BTC — target pieno 3R | Scanner Top 5 + forza BTC | €9.918,84 | €-136,53 | 180 | 180 | 42,78% | 0,97 | €-0,76 | 11,91% |
| TEST | Btc Ema 4H | Trend following EMA | €9.914,14 | €-85,86 | 5 | 5 | 20,00% | 0,58 | €-17,17 | 1,76% |
| TEST | Top 5 + BTC — 75% a 2,2R + runner 3R | Scanner Top 5 + forza BTC | €9.913,04 | €-142,30 | 184 | 184 | 42,93% | 0,96 | €-0,77 | 12,06% |
| TEST | Rapida score 6–7,5 — senza Trend Up | Momentum / breakout | €9.902,86 | €-97,14 | 223 | 223 | 45,29% | 0,98 | €-0,44 | 15,94% |
| TEST | Rapida V3 — qualità completa + profit lock | Momentum / breakout V3 Filtered | €9.902,55 | €-97,45 | 206 | 206 | 47,09% | 0,98 | €-0,47 | 8,44% |
| TEST | Rapida V3 — Long + no HIGH + score <7,5 | Momentum / breakout V3 Filtered | €9.891,96 | €-108,04 | 208 | 208 | 44,71% | 0,98 | €-0,52 | 6,64% |
| TEST | Top 5 + BTC — solo MFE | Scanner Top 5 + forza BTC | €9.890,02 | €-142,27 | 164 | 164 | 45,73% | 0,95 | €-0,87 | 12,28% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €9.868,16 | €-131,84 | 12 | 12 | 50,00% | 0,70 | €-10,99 | 4,16% |
| TEST | Rapida V1 — score 6–7,5 | Momentum / breakout | €9.862,02 | €-137,98 | 261 | 261 | 43,68% | 0,98 | €-0,53 | 15,64% |
| TEST | Combo Trend | Combo Trend | €9.840,70 | €-156,93 | 206 | 206 | 42,72% | 0,96 | €-0,76 | 14,08% |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | Momentum / breakout V3 Filtered | €9.837,38 | €-162,62 | 37 | 37 | 40,54% | 0,76 | €-4,40 | 3,08% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | Momentum / breakout V3 Filtered | €9.817,34 | €-182,66 | 24 | 24 | 41,67% | 0,64 | €-7,61 | 3,23% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €9.808,89 | €-191,11 | 7 | 7 | 14,29% | 0,41 | €-27,30 | 2,43% |
| TEST | Bilanciata V3 · LONG only | Confluenza trend V3 Filtered | €9.804,15 | €-188,92 | 192 | 192 | 43,75% | 0,94 | €-0,98 | 13,79% |
| TEST | Combo Adaptive — Quality7 + Regime | Combo Adaptive | €9.802,98 | €-189,79 | 58 | 58 | 46,55% | 0,86 | €-3,27 | 5,41% |
| TEST | Eth Ema 4H | Trend following EMA | €9.783,14 | €-216,86 | 9 | 9 | 22,22% | 0,41 | €-24,10 | 2,32% |
| TEST | Top 5 + BTC — Guard | Scanner Top 5 + forza BTC | €9.780,78 | €-227,44 | 176 | 176 | 38,64% | 0,94 | €-1,29 | 7,34% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.779,96 | €-220,04 | 23 | 23 | 39,13% | 0,66 | €-9,57 | 3,93% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | Momentum / breakout V3 Filtered | €9.762,18 | €-237,82 | 7 | 7 | 14,29% | 0,02 | €-33,97 | 2,82% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €9.759,64 | €-238,93 | 19 | 19 | 47,37% | 0,58 | €-12,58 | 3,15% |
| TEST | Combo Adaptive — Quality7 | Combo Adaptive | €9.745,73 | €-251,00 | 116 | 116 | 41,38% | 0,91 | €-2,16 | 8,88% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | Momentum / breakout V3 Filtered | €9.723,72 | €-276,28 | 31 | 31 | 32,26% | 0,62 | €-8,91 | 4,83% |
| TEST | Combo Adaptive — 75% a 2R + runner 25% a 3R | Combo Adaptive | €9.720,99 | €-261,37 | 173 | 173 | 38,73% | 0,92 | €-1,51 | 14,10% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €9.692,97 | €-303,47 | 187 | 172 | 45,45% | 0,92 | €-1,62 | 11,82% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.676,47 | €-323,53 | 23 | 23 | 34,78% | 0,61 | €-14,07 | 4,65% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.668,82 | €-331,18 | 22 | 22 | 36,36% | 0,58 | €-15,05 | 3,69% |
| TEST | Bilanciata 1H — LONG senza Range High Vol | Confluenza trend | €9.637,16 | €-379,71 | 155 | 155 | 45,16% | 0,86 | €-2,45 | 9,26% |
| TEST | Master Adaptive GB20 — Breakeven 0,5R | Master Adaptive Consensus | €9.627,49 | €-375,21 | 130 | 130 | 33,85% | 0,89 | €-2,89 | 10,08% |
| TEST | Master Adaptive GB20 — 50% a 0,75R | Master Adaptive Consensus | €9.617,26 | €-385,44 | 125 | 125 | 36,00% | 0,88 | €-3,08 | 9,87% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €9.586,54 | €-477,75 | 114 | 114 | 33,33% | 0,85 | €-4,19 | 9,31% |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | €9.580,06 | €-422,63 | 127 | 127 | 35,43% | 0,88 | €-3,33 | 9,87% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | Momentum / breakout V3 Filtered | €9.579,83 | €-420,17 | 11 | 11 | 0,00% | 0,00 | €-38,20 | 4,20% |
| TEST | Top 5 + BTC — Guard + MFE | Scanner Top 5 + forza BTC | €9.543,10 | €-464,91 | 192 | 192 | 39,06% | 0,88 | €-2,42 | 8,78% |
| TEST | Combo Adaptive — Trend/Transition | Combo Adaptive | €9.540,70 | €-456,12 | 91 | 91 | 46,15% | 0,79 | €-5,01 | 6,28% |
| TEST | Combo Adaptive — target pieno 3R | Combo Adaptive | €9.539,13 | €-443,55 | 153 | 153 | 38,56% | 0,84 | €-2,90 | 14,10% |
| TEST | Scanner Bottom10 Short | Scanner Bottom10 Short | €9.530,72 | €-469,28 | 76 | 76 | 34,21% | 0,76 | €-6,17 | 9,06% |
| TEST | Scanner Bottom15 Short | Scanner Bottom15 Short | €9.530,72 | €-469,28 | 76 | 76 | 34,21% | 0,76 | €-6,17 | 9,06% |
| TEST | Scanner Bottom20 Short | Scanner Bottom20 Short | €9.530,72 | €-469,28 | 76 | 76 | 34,21% | 0,76 | €-6,17 | 9,06% |
| TEST | Master Adaptive GB20 — Loss Cap 0,75R | Master Adaptive Consensus | €9.473,23 | €-530,31 | 119 | 119 | 28,57% | 0,85 | €-4,46 | 12,05% |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | Scanner Bottom 5 Short | €9.464,68 | €-535,32 | 67 | 67 | 34,33% | 0,71 | €-7,99 | 9,08% |
| TEST | Eth Ema 1H | Trend following EMA | €9.463,42 | €-585,74 | 34 | 34 | 35,29% | 0,50 | €-17,23 | 5,88% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.459,83 | €-540,17 | 26 | 26 | 34,62% | 0,42 | €-20,78 | 5,44% |
| TEST | Rapida V3 — score <7,5 | Momentum / breakout V3 Filtered | €9.454,76 | €-545,24 | 281 | 281 | 42,35% | 0,91 | €-1,94 | 19,03% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €9.453,65 | €-549,00 | 161 | 161 | 43,48% | 0,85 | €-3,41 | 10,69% |
| TEST | Scanner Bottom5 Short Profit Lock V1 | Scanner Bottom 5 Short | €9.450,28 | €-549,72 | 68 | 68 | 33,82% | 0,69 | €-8,08 | 9,08% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €9.382,53 | €-620,10 | 105 | 105 | 36,19% | 0,78 | €-5,91 | 10,41% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.377,56 | €-622,44 | 95 | 95 | 33,68% | 0,73 | €-6,55 | 10,17% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €9.354,53 | €-619,44 | 226 | 226 | 42,04% | 0,85 | €-2,74 | 15,68% |
| TEST | Btc Ema 1H | Trend following EMA | €9.353,69 | €-646,31 | 28 | 28 | 25,00% | 0,36 | €-23,08 | 6,56% |
| TEST | Combo Adaptive — MFE Trail esistente | Combo Adaptive | €9.352,19 | €-656,30 | 247 | 247 | 42,11% | 0,84 | €-2,66 | 15,45% |
| TEST | Rapida V1 — Long + BTC 1–3 + score <7,5 | Momentum / breakout | €9.205,17 | €-794,83 | 167 | 167 | 40,12% | 0,81 | €-4,76 | 13,09% |
| TEST | Top 5 + BTC — BTC 2–3 | Scanner Top 5 + forza BTC | €9.165,38 | €-827,46 | 71 | 71 | 32,39% | 0,59 | €-11,65 | 12,43% |
| TEST | Top 5 + BTC — Guard + BTC≤3 | Scanner Top 5 + forza BTC | €9.075,88 | €-923,65 | 143 | 143 | 39,86% | 0,76 | €-6,46 | 16,24% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €8.841,81 | €-1.148,70 | 192 | 192 | 36,46% | 0,69 | €-5,98 | 19,11% |
| TEST | Top 5 + BTC — Guard + BTC≤3 + MFE | Scanner Top 5 + forza BTC | €8.647,30 | €-1.352,25 | 166 | 166 | 40,36% | 0,70 | €-8,15 | 18,17% |
| TEST | Top 5 + BTC — BTC≤3 | Scanner Top 5 + forza BTC | €8.614,01 | €-1.385,55 | 143 | 143 | 38,46% | 0,62 | €-9,69 | 20,25% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €8.553,84 | €-1.446,16 | 87 | 87 | 36,78% | 0,52 | €-16,62 | 16,26% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €8.448,19 | €-1.551,81 | 88 | 88 | 26,14% | 0,56 | €-17,63 | 15,70% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €8.413,97 | €-1.586,03 | 126 | 126 | 30,95% | 0,61 | €-12,59 | 16,10% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €7.569,99 | €-2.430,01 | 156 | 156 | 40,38% | 0,51 | €-15,58 | 26,04% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | ZEC | LONG | Confluenza trend | 240m | 3,0x | 1362,57246 | 1475,81000 | 1425,79382 | 915,19450 | 1590,97378 | €171,74 | €515,21 | €0,00 | €42,82 |
| Principale 4H | ARB | LONG | Confluenza trend | 240m | 3,0x | 0,22709 | 0,22709 | 0,20271 | 0,15253 | 0,27584 | €18,13 | €54,39 | €5,84 | €0,00 |
| Bilanciata 1H V1 | UNI | LONG | Confluenza trend | 60m | 3,0x | 8,65319 | 8,65319 | 8,15820 | 5,81206 | 9,64317 | €269,37 | €808,12 | €46,23 | €0,00 |
| Bilanciata 1H V1 | ZEC | LONG | Confluenza trend | 60m | 3,0x | 1518,19358 | 1475,81000 | 1455,64754 | 1019,72002 | 1643,28565 | €375,17 | €1.125,52 | €46,37 | €-31,42 |
| Bilanciata 1H V1 | AVAX | LONG | Confluenza trend | 60m | 3,0x | 11,18924 | 11,18924 | 10,58712 | 7,51544 | 12,39348 | €13,07 | €39,21 | €2,11 | €0,00 |
| Bilanciata 1H V1 | PEPE | LONG | Confluenza trend | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00001 | €294,67 | €884,01 | €47,09 | €7,11 |
| Bilanciata 1H — LONG senza Range High Vol | ZEC | LONG | Confluenza trend | 60m | 3,0x | 1462,70248 | 1475,81000 | 1401,11389 | 982,44850 | 1585,87967 | €370,14 | €1.110,42 | €46,76 | €9,95 |
| Bilanciata 1H — LONG senza Range High Vol | UNI | LONG | Confluenza trend | 60m | 3,0x | 8,65319 | 8,65319 | 8,15820 | 5,81206 | 9,64317 | €278,02 | €834,06 | €47,71 | €0,00 |
| Bilanciata 1H — LONG senza Range High Vol | AVAX | LONG | Confluenza trend | 60m | 3,0x | 11,18924 | 11,18924 | 10,58712 | 7,51544 | 12,39348 | €300,54 | €901,63 | €48,52 | €0,00 |
| Bilanciata 1H — LONG senza Range High Vol | SUI | LONG | Confluenza trend | 60m | 3,0x | 1,00840 | 1,00890 | 0,95579 | 0,67731 | 1,11362 | €11,30 | €33,91 | €1,77 | €0,02 |
| Bilanciata 1H — LONG senza Range High Vol | PEPE | LONG | Confluenza trend | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00001 | €295,79 | €887,38 | €47,83 | €9,16 |
| Bilanciata 1H V2 | ZEC | LONG | Confluenza trend V2 | 60m | 3,0x | 1478,71568 | 1475,81000 | 1409,80814 | 993,20403 | 1616,53079 | €341,14 | €1.023,41 | €47,69 | €-2,01 |
| Bilanciata 1H V2 | ARB | LONG | Confluenza trend V2 | 60m | 3,0x | 0,21346 | 0,21346 | 0,19751 | 0,14338 | 0,24536 | €215,90 | €647,70 | €48,39 | €0,00 |
| Bilanciata 1H V2 | AVAX | LONG | Confluenza trend V2 | 60m | 3,0x | 11,18924 | 11,18924 | 10,58712 | 7,51544 | 12,39348 | €302,59 | €907,76 | €48,85 | €0,00 |
| Bilanciata 1H V3 Filtered | ZEC | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1485,33701 | 1475,81000 | 1415,48789 | 997,65136 | 1625,03524 | €347,14 | €1.041,42 | €48,97 | €-6,68 |
| Bilanciata 1H V3 Filtered | UNI | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 8,44269 | 8,44269 | 7,95170 | 5,67067 | 9,42467 | €11,49 | €34,47 | €2,00 | €0,00 |
| Rapida score 6–7,5 — Cost Aware | PEPE | LONG | Momentum / breakout | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00001 | €467,05 | €1.401,16 | €58,05 | €11,26 |
| Rapida score 6–7,5 — Cost Aware | SUI | LONG | Momentum / breakout | 60m | 3,0x | 1,00520 | 1,00890 | 0,96323 | 0,67516 | 1,06815 | €463,26 | €1.389,79 | €58,02 | €5,11 |
| Rapida V1 — senza PEPE | AVAX | LONG | Momentum / breakout | 60m | 3,0x | 11,32426 | 11,32426 | 10,89502 | 7,60613 | 11,96813 | €501,34 | €1.504,03 | €57,01 | €0,00 |
| Rapida V1 — senza PEPE | SUI | LONG | Momentum / breakout | 60m | 3,0x | 1,00520 | 1,00890 | 0,96323 | 0,67516 | 1,06815 | €451,17 | €1.353,52 | €56,51 | €4,98 |
| Rapida V1 — senza PEPE | DOGE | LONG | Momentum / breakout | 60m | 3,0x | 0,09878 | 0,09876 | 0,09626 | 0,06635 | 0,10256 | €737,93 | €2.213,80 | €56,53 | €-0,44 |
| Rapida 1H V3 Filtered — madre | AVAX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 11,32426 | 11,32426 | 10,89502 | 7,60613 | 11,96813 | €484,93 | €1.454,78 | €55,14 | €0,00 |
| Rapida 1H V3 Filtered — madre | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2736,65722 | 2754,86000 | 2698,50381 | 1838,12143 | 2793,88732 | €1.318,29 | €3.954,87 | €55,14 | €26,31 |
| Rapida 1H V3 Filtered — madre | PEPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00001 | €439,33 | €1.317,98 | €54,60 | €10,59 |
| Rapida 1H V3 Filtered — madre | SUI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,00520 | 1,00890 | 0,96323 | 0,67516 | 1,06815 | €431,04 | €1.293,12 | €53,99 | €4,76 |
| Rapida V3 — no volatilità HIGH | AVAX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 11,32426 | 11,32426 | 10,89502 | 7,60613 | 11,96813 | €473,01 | €1.419,03 | €53,79 | €0,00 |
| Rapida V3 — no volatilità HIGH | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2736,65722 | 2754,86000 | 2698,50381 | 1838,12143 | 2793,88732 | €1.285,89 | €3.857,68 | €53,78 | €25,66 |
| Rapida V3 — Long Only | AVAX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 11,32426 | 11,32426 | 10,89502 | 7,60613 | 11,96813 | €451,11 | €1.353,33 | €51,30 | €0,00 |
| Rapida V3 — Long Only | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2736,65722 | 2754,86000 | 2698,50381 | 1838,12143 | 2793,88732 | €1.226,36 | €3.679,08 | €51,29 | €24,47 |
| Rapida V3 — Long Only | PEPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00001 | €408,69 | €1.226,07 | €50,79 | €9,86 |
| Rapida V3 — Long Only | SUI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,00520 | 1,00890 | 0,96323 | 0,67516 | 1,06815 | €400,98 | €1.202,95 | €50,22 | €4,43 |
| Rapida V3 — senza ESPORTS | AVAX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 11,32426 | 11,32426 | 10,89502 | 7,60613 | 11,96813 | €457,62 | €1.372,87 | €52,04 | €0,00 |
| Rapida V3 — senza ESPORTS | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2736,65722 | 2754,86000 | 2698,50381 | 1838,12143 | 2793,88732 | €1.244,07 | €3.732,21 | €52,03 | €24,82 |
| Rapida V3 — senza ESPORTS | PEPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00001 | €414,59 | €1.243,78 | €51,53 | €10,00 |
| Rapida V3 — senza ESPORTS | SUI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,00520 | 1,00890 | 0,96323 | 0,67516 | 1,06815 | €406,77 | €1.220,32 | €50,95 | €4,49 |
| Rapida V3 senza ESPORTS — Long Only | AVAX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 11,32426 | 11,32426 | 10,89502 | 7,60613 | 11,96813 | €467,56 | €1.402,67 | €53,17 | €0,00 |
| Rapida V3 senza ESPORTS — Long Only | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2736,65722 | 2754,86000 | 2698,50381 | 1838,12143 | 2793,88732 | €1.271,07 | €3.813,22 | €53,16 | €25,36 |
| Rapida V3 senza ESPORTS — Long Only | PEPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00001 | €423,59 | €1.270,77 | €52,64 | €10,21 |
| Rapida V3 senza ESPORTS — Long Only | SUI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,00520 | 1,00890 | 0,96323 | 0,67516 | 1,06815 | €415,60 | €1.246,80 | €52,05 | €4,59 |
| Rapida V3 senza ESPORTS — MFE Lock | AVAX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 11,32426 | 11,32426 | 10,89502 | 7,60613 | 11,96813 | €488,06 | €1.464,19 | €55,50 | €0,00 |
| Rapida V3 senza ESPORTS — MFE Lock | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2736,65722 | 2754,86000 | 2698,50381 | 1838,12143 | 2793,88732 | €1.326,82 | €3.980,45 | €55,49 | €26,48 |
| Rapida V3 senza ESPORTS — MFE Lock | PEPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00001 | €442,17 | €1.326,50 | €54,95 | €10,66 |
| Rapida V3 senza ESPORTS — MFE Lock | SUI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,00520 | 1,00890 | 0,96323 | 0,67516 | 1,06815 | €433,83 | €1.301,48 | €54,34 | €4,79 |
| Ampia 4H | NEAR | LONG | Confluenza trend | 240m | 2,0x | 3,50070 | 4,03800 | 3,12944 | 1,76785 | 4,54024 | €237,59 | €475,18 | €50,39 | €72,93 |
| Ampia 4H | ARB | LONG | Confluenza trend | 240m | 2,0x | 0,22709 | 0,22709 | 0,19984 | 0,11468 | 0,30339 | €209,97 | €419,94 | €50,39 | €0,00 |
| Forza relativa 1H V1 | ZEC | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 1478,71568 | 1475,81000 | 1409,80814 | 746,75142 | 1630,31230 | €463,14 | €926,28 | €43,16 | €-1,82 |
| Forza relativa 1H V1 | UNI | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 8,65319 | 8,65319 | 8,15820 | 4,36986 | 9,74217 | €379,70 | €759,40 | €43,44 | €0,00 |
| Forza relativa 1H V1 | AVAX | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 11,18924 | 11,18924 | 10,58712 | 5,65056 | 12,51390 | €412,08 | €824,17 | €44,35 | €0,00 |
| Forza relativa 1H V1 | XRP | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 1,47275 | 1,50211 | 1,48219 | 0,74374 | 1,54279 | €48,10 | €96,21 | €0,00 | €1,92 |
| Forza relativa 1H V1 | PEPE | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,00001 | 0,00000 | 0,00000 | 0,00000 | 0,00001 | €410,63 | €821,26 | €43,74 | €-7,54 |
| Forza relativa 1H V2 | ZEC | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 1478,71568 | 1475,81000 | 1409,80814 | 746,75142 | 1630,31230 | €535,87 | €1.071,75 | €49,94 | €-2,11 |
| Forza relativa 1H V2 | ARB | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,21346 | 0,21346 | 0,19751 | 0,10780 | 0,24855 | €342,38 | €684,76 | €51,16 | €0,00 |
| Forza relativa 1H V2 | AVAX | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 11,18924 | 11,18924 | 10,58712 | 5,65056 | 12,51390 | €480,26 | €960,53 | €51,69 | €0,00 |
| Forza relativa 1H V2 | SUI | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 1,01610 | 1,00890 | 0,96309 | 0,51313 | 1,13273 | €491,56 | €983,12 | €51,29 | €-6,97 |
| Benchmark Donchian breakout 1H | UNI | LONG | Donchian breakout 20 barre | 60m | 2,0x | 8,65319 | 8,65319 | 8,10320 | 4,36986 | 10,02816 | €21,82 | €43,64 | €2,77 | €0,00 |
| Donchian 1H Gb20 120R V1 | UNI | LONG | Donchian breakout 20 barre | 60m | 2,0x | 8,65319 | 8,65319 | 8,10320 | 4,36986 | 10,02816 | €21,31 | €42,62 | €2,71 | €0,00 |
| Benchmark trend following EMA 1H | ZEC | LONG | Trend following EMA | 60m | 2,0x | 1478,71568 | 1475,81000 | 1402,15173 | 746,75142 | 1647,15637 | €474,62 | €949,23 | €49,15 | €-1,87 |
| Benchmark trend following EMA 1H | ARB | LONG | Trend following EMA | 60m | 2,0x | 0,21346 | 0,21346 | 0,19574 | 0,10780 | 0,25245 | €13,97 | €27,94 | €2,32 | €0,00 |
| Scanner Top 5 Long 1H | UNI | LONG | Scanner Top 5 Long | 60m | 2,0x | 8,65319 | 8,65319 | 8,15820 | 4,36986 | 9,64317 | €472,31 | €944,62 | €54,04 | €0,00 |
| Scanner Top 5 Long 1H | ZEC | LONG | Scanner Top 5 Long | 60m | 2,0x | 1518,19358 | 1475,81000 | 1455,64754 | 766,68776 | 1643,28565 | €43,77 | €87,53 | €3,61 | €-2,44 |
| Scanner Top 5 Long 1H | AVAX | LONG | Scanner Top 5 Long | 60m | 2,0x | 11,18924 | 11,18924 | 10,58712 | 5,65056 | 12,39348 | €513,44 | €1.026,87 | €55,26 | €0,00 |
| Scanner Top 5 Long 1H | XRP | LONG | Scanner Top 5 Long | 60m | 2,0x | 1,47275 | 1,50211 | 1,48401 | 0,74374 | 1,53642 | €1.222,69 | €2.445,37 | €0,00 | €48,74 |
| Scanner Top 5 Long 1H | PEPE | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,00001 | 0,00000 | 0,00000 | 0,00000 | 0,00001 | €520,33 | €1.040,66 | €55,43 | €-9,55 |
| Scanner Top10 Long | UNI | LONG | Scanner Top10 Long | 60m | 2,0x | 8,65319 | 8,65319 | 8,15820 | 4,36986 | 9,64317 | €444,55 | €889,09 | €50,86 | €0,00 |
| Scanner Top10 Long | ZEC | LONG | Scanner Top10 Long | 60m | 2,0x | 1518,19358 | 1475,81000 | 1455,64754 | 766,68776 | 1643,28565 | €15,08 | €30,15 | €1,24 | €-0,84 |
| Scanner Top15 Long | ZEC | LONG | Scanner Top15 Long | 60m | 2,0x | 1485,33701 | 1475,81000 | 1415,48789 | 750,09519 | 1625,03524 | €557,51 | €1.115,02 | €52,43 | €-7,15 |
| Scanner Top15 Long | UNI | LONG | Scanner Top15 Long | 60m | 2,0x | 8,44269 | 8,44269 | 7,95170 | 4,26356 | 9,42467 | €456,25 | €912,49 | €53,07 | €0,00 |
| Scanner Top15 Long | AVAX | LONG | Scanner Top15 Long | 60m | 2,0x | 11,18924 | 11,18924 | 10,58712 | 5,65056 | 12,39348 | €24,58 | €49,17 | €2,65 | €0,00 |
| Scanner Top15 Long | PEPE | LONG | Scanner Top15 Long | 60m | 2,0x | 0,00001 | 0,00000 | 0,00000 | 0,00000 | 0,00001 | €504,43 | €1.008,86 | €53,74 | €-9,26 |
| Scanner Top15 Long | SUI | LONG | Scanner Top15 Long | 60m | 2,0x | 1,00840 | 1,00890 | 0,95579 | 0,50924 | 1,11362 | €508,36 | €1.016,72 | €53,04 | €0,50 |
| Scanner Top20 Long | ZEC | LONG | Scanner Top20 Long | 60m | 2,0x | 1485,33701 | 1475,81000 | 1415,48789 | 750,09519 | 1625,03524 | €557,51 | €1.115,02 | €52,43 | €-7,15 |
| Scanner Top20 Long | UNI | LONG | Scanner Top20 Long | 60m | 2,0x | 8,44269 | 8,44269 | 7,95170 | 4,26356 | 9,42467 | €456,25 | €912,49 | €53,07 | €0,00 |
| Scanner Top20 Long | AVAX | LONG | Scanner Top20 Long | 60m | 2,0x | 11,18924 | 11,18924 | 10,58712 | 5,65056 | 12,39348 | €24,58 | €49,17 | €2,65 | €0,00 |
| Scanner Top20 Long | PEPE | LONG | Scanner Top20 Long | 60m | 2,0x | 0,00001 | 0,00000 | 0,00000 | 0,00000 | 0,00001 | €504,43 | €1.008,86 | €53,74 | €-9,26 |
| Scanner Top20 Long | SUI | LONG | Scanner Top20 Long | 60m | 2,0x | 1,00840 | 1,00890 | 0,95579 | 0,50924 | 1,11362 | €508,36 | €1.016,72 | €53,04 | €0,50 |
| Scanner Top 5 + forza BTC 1H | UNI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 8,65319 | 8,65319 | 8,15820 | 4,36986 | 9,74217 | €444,91 | €889,82 | €50,90 | €0,00 |
| Scanner Top 5 + forza BTC 1H | AVAX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 11,18924 | 11,18924 | 10,58712 | 5,65056 | 12,51390 | €487,93 | €975,86 | €52,51 | €0,00 |
| Scanner Top 5 + forza BTC 1H | XRP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,47275 | 1,50211 | 1,48401 | 0,74374 | 1,54279 | €1.163,30 | €2.326,61 | €0,00 | €46,37 |
| Scanner Top 5 + forza BTC 1H | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00001 | 0,00000 | 0,00000 | 0,00000 | 0,00001 | €494,57 | €989,13 | €52,68 | €-9,08 |
| Scanner Top 5 + forza BTC 1H | SUI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,00520 | 1,00890 | 0,95124 | 0,50763 | 1,12391 | €41,38 | €82,75 | €4,44 | €0,30 |
| Top 5 + BTC — solo MFE | UNI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 8,65319 | 8,65319 | 8,15820 | 4,36986 | 9,74217 | €417,08 | €834,16 | €47,72 | €0,00 |
| Top 5 + BTC — solo MFE | AVAX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 11,18924 | 11,18924 | 10,58712 | 5,65056 | 12,51390 | €457,41 | €914,82 | €49,23 | €0,00 |
| Top 5 + BTC — solo MFE | XRP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,47275 | 1,50211 | 1,48401 | 0,74374 | 1,54279 | €1.090,54 | €2.181,08 | €0,00 | €43,47 |
| Top 5 + BTC — solo MFE | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00001 | 0,00000 | 0,00000 | 0,00000 | 0,00001 | €463,63 | €927,27 | €49,39 | €-8,51 |
| Top 5 + BTC — solo MFE | SUI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,00520 | 1,00890 | 0,95124 | 0,50763 | 1,12391 | €38,79 | €77,58 | €4,16 | €0,29 |
| Top 5 + BTC — Guard | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1462,70248 | 1475,81000 | 1401,11389 | 738,66475 | 1598,19740 | €558,11 | €1.116,22 | €47,00 | €10,00 |
| Top 5 + BTC — Guard | UNI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 8,65319 | 8,65319 | 8,15820 | 4,36986 | 9,74217 | €421,50 | €843,00 | €48,22 | €0,00 |
| Top 5 + BTC — Guard | AVAX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 11,32426 | 11,32426 | 10,77238 | 5,71875 | 12,53841 | €506,83 | €1.013,65 | €49,40 | €0,00 |
| Top 5 + BTC — BTC≤3 | UNI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 8,65319 | 8,65319 | 8,15820 | 4,36986 | 9,74217 | €367,75 | €735,49 | €42,07 | €0,00 |
| Top 5 + BTC — BTC 2–3 | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1485,33701 | 1475,81000 | 1415,48789 | 750,09519 | 1639,00507 | €477,40 | €954,81 | €44,90 | €-6,12 |
| Top 5 + BTC — BTC 2–3 | UNI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 8,44269 | 8,44269 | 7,95170 | 4,26356 | 9,52286 | €386,45 | €772,89 | €44,95 | €0,00 |
| Top 5 + BTC — Guard + MFE | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1462,70248 | 1475,81000 | 1401,11389 | 738,66475 | 1598,19740 | €545,13 | €1.090,26 | €45,91 | €9,77 |
| Top 5 + BTC — Guard + MFE | UNI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 8,65319 | 8,65319 | 8,15820 | 4,36986 | 9,74217 | €411,70 | €823,40 | €47,10 | €0,00 |
| Top 5 + BTC — Guard + MFE | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,21346 | 0,21346 | 0,19751 | 0,10780 | 0,24855 | €15,82 | €31,63 | €2,36 | €0,00 |
| Top 5 + BTC — Guard + MFE | AVAX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 11,32426 | 11,32426 | 10,77238 | 5,71875 | 12,53841 | €494,78 | €989,56 | €48,23 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 | UNI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 8,65319 | 8,65319 | 8,15820 | 4,36986 | 9,74217 | €387,55 | €775,09 | €44,34 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | UNI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 8,65319 | 8,65319 | 8,15820 | 4,36986 | 9,74217 | €369,38 | €738,77 | €42,26 | €0,00 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1367,76350 | 1475,81000 | 1457,33594 | 690,72057 | 1590,01389 | €356,23 | €712,46 | €0,00 | €56,28 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | UNI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 8,65319 | 8,65319 | 8,15820 | 4,36986 | 10,13816 | €425,04 | €850,08 | €48,63 | €0,00 |
| Top 5 + BTC — target pieno 3R | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1367,76350 | 1475,81000 | 1457,33594 | 690,72057 | 1590,01389 | €356,44 | €712,87 | €0,00 | €56,31 |
| Top 5 + BTC — target pieno 3R | UNI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 8,65319 | 8,65319 | 8,15820 | 4,36986 | 10,13816 | €425,29 | €850,58 | €48,66 | €0,00 |
| Combo Trend | ZEC | LONG | Combo Trend | 60m | 2,0x | 1478,71568 | 1475,81000 | 1402,15173 | 746,75142 | 1647,15637 | €460,25 | €920,51 | €47,66 | €-1,81 |
| Combo Trend | ARB | LONG | Combo Trend | 60m | 2,0x | 0,21346 | 0,21346 | 0,19574 | 0,10780 | 0,25245 | €13,55 | €27,09 | €2,25 | €0,00 |
| Combo Scanner | ZEC | LONG | Combo Scanner | 60m | 2,0x | 1462,70248 | 1475,81000 | 1401,11389 | 738,66475 | 1598,19740 | €600,23 | €1.200,45 | €50,55 | €10,76 |
| Combo Scanner | UNI | LONG | Combo Scanner | 60m | 2,0x | 8,65319 | 8,65319 | 8,15820 | 4,36986 | 9,74217 | €453,31 | €906,62 | €51,86 | €0,00 |
| Combo Scanner | AVAX | LONG | Combo Scanner | 60m | 2,0x | 11,32426 | 11,32426 | 10,77238 | 5,71875 | 12,53841 | €545,07 | €1.090,14 | €53,13 | €0,00 |
| Combo Adaptive — madre | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 1478,71568 | 1475,81000 | 1409,80814 | 746,75142 | 1616,53079 | €571,67 | €1.143,34 | €53,28 | €-2,25 |
| Combo Adaptive — madre | UNI | LONG | Combo Adaptive | 60m | 2,0x | 8,44269 | 8,44269 | 7,95170 | 4,26356 | 9,42467 | €462,24 | €924,48 | €53,76 | €0,00 |
| Combo Adaptive — madre | AVAX | LONG | Combo Adaptive | 60m | 2,0x | 11,18924 | 11,18924 | 10,58712 | 5,65056 | 12,39348 | €508,49 | €1.016,97 | €54,73 | €0,00 |
| Combo Adaptive — madre | SUI | LONG | Combo Adaptive | 60m | 2,0x | 1,00840 | 1,00890 | 0,95579 | 0,50924 | 1,11362 | €523,01 | €1.046,02 | €54,57 | €0,52 |
| Combo Adaptive — madre | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00001 | 0,00000 | 0,00000 | 0,00000 | 0,00001 | €18,12 | €36,24 | €1,93 | €-0,33 |
| Combo Adaptive — MFE Trail esistente | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 1462,70248 | 1475,81000 | 1464,45772 | 738,66475 | 1585,87967 | €536,54 | €1.073,07 | €0,00 | €9,62 |
| Combo Adaptive — MFE Trail esistente | UNI | LONG | Combo Adaptive | 60m | 2,0x | 8,65319 | 8,65319 | 8,15820 | 4,36986 | 9,64317 | €403,76 | €807,51 | €46,19 | €0,00 |
| Combo Adaptive — Quality7 | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 1478,71568 | 1475,81000 | 1409,80814 | 746,75142 | 1616,53079 | €511,68 | €1.023,36 | €47,69 | €-2,01 |
| Combo Adaptive — Quality7 | AVAX | LONG | Combo Adaptive | 60m | 2,0x | 11,18924 | 11,18924 | 10,58712 | 5,65056 | 12,39348 | €455,87 | €911,74 | €49,06 | €0,00 |
| Combo Adaptive — Quality7 | SUI | LONG | Combo Adaptive | 60m | 2,0x | 1,00840 | 1,00890 | 0,95579 | 0,50924 | 1,11362 | €466,44 | €932,88 | €48,67 | €0,46 |
| Combo Adaptive — Trend/Transition | SUI | LONG | Combo Adaptive | 60m | 2,0x | 1,01610 | 1,00890 | 0,96309 | 0,51313 | 1,12213 | €457,33 | €914,67 | €47,72 | €-6,48 |
| Combo Adaptive — Trend/Transition | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00001 | €447,92 | €895,84 | €47,72 | €7,20 |
| Combo Adaptive — Trend/Transition | DOGE | LONG | Combo Adaptive | 60m | 2,0x | 0,09878 | 0,09876 | 0,09554 | 0,04988 | 0,10527 | €726,70 | €1.453,40 | €47,72 | €-0,29 |
| Combo Adaptive — Trend/Transition | XRP | LONG | Combo Adaptive | 60m | 2,0x | 1,50241 | 1,50211 | 1,46750 | 0,75872 | 1,57224 | €1.026,17 | €2.052,34 | €47,69 | €-0,41 |
| Combo Adaptive — Quality7 + Regime | SUI | LONG | Combo Adaptive | 60m | 2,0x | 1,01610 | 1,00890 | 0,96309 | 0,51313 | 1,12213 | €470,10 | €940,19 | €49,05 | €-6,67 |
| Combo Adaptive — Long Only | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 1462,70248 | 1475,81000 | 1401,11389 | 738,66475 | 1585,87967 | €620,45 | €1.240,90 | €52,25 | €11,12 |
| Combo Adaptive — Long Only | UNI | LONG | Combo Adaptive | 60m | 2,0x | 8,65319 | 8,65319 | 8,15820 | 4,36986 | 9,64317 | €466,37 | €932,75 | €53,36 | €0,00 |
| Combo Adaptive — parziale 1R | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 1485,33701 | 1475,81000 | 1415,48789 | 750,09519 | 1625,03524 | €544,86 | €1.089,72 | €51,25 | €-6,99 |
| Combo Adaptive — parziale 1R | UNI | LONG | Combo Adaptive | 60m | 2,0x | 8,44269 | 8,44269 | 7,95170 | 4,26356 | 9,42467 | €448,18 | €896,36 | €52,13 | €0,00 |
| Combo Adaptive — parziale 1R | AVAX | LONG | Combo Adaptive | 60m | 2,0x | 11,18924 | 11,18924 | 10,58712 | 5,65056 | 12,39348 | €493,65 | €987,29 | €53,13 | €0,00 |
| Combo Adaptive — parziale 1R | SUI | LONG | Combo Adaptive | 60m | 2,0x | 1,00840 | 1,00890 | 0,95579 | 0,50924 | 1,11362 | €507,74 | €1.015,48 | €52,98 | €0,50 |
| Combo Adaptive — parziale 1R | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00001 | 0,00000 | 0,00000 | 0,00000 | 0,00001 | €22,70 | €45,41 | €2,42 | €-0,42 |
| Combo Adaptive — Quality7 + Regime + parziale 1R | SUI | LONG | Combo Adaptive | 60m | 2,0x | 1,01610 | 1,00890 | 0,96309 | 0,51313 | 1,12213 | €476,08 | €952,17 | €49,68 | €-6,75 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 1491,36821 | 1475,81000 | 1429,23993 | 753,14095 | 1677,75305 | €23,49 | €46,97 | €1,96 | €-0,49 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | UNI | LONG | Combo Adaptive | 60m | 2,0x | 8,65319 | 8,65319 | 8,15820 | 4,36986 | 10,13816 | €405,28 | €810,56 | €46,37 | €0,00 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | AVAX | LONG | Combo Adaptive | 60m | 2,0x | 11,18924 | 11,18924 | 10,58712 | 5,65056 | 12,99560 | €444,46 | €888,93 | €47,84 | €0,00 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | SUI | LONG | Combo Adaptive | 60m | 2,0x | 1,01610 | 1,00890 | 0,96309 | 0,51313 | 1,17514 | €466,01 | €932,01 | €48,62 | €-6,61 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00001 | 0,00000 | 0,00000 | 0,00000 | 0,00001 | €455,89 | €911,78 | €48,56 | €-8,37 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | DOGE | LONG | Combo Adaptive | 60m | 2,0x | 0,09878 | 0,09876 | 0,09554 | 0,04988 | 0,10851 | €16,34 | €32,68 | €1,07 | €-0,01 |
| Combo Adaptive — target pieno 3R | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 1491,36821 | 1475,81000 | 1429,23993 | 753,14095 | 1677,75305 | €23,05 | €46,09 | €1,92 | €-0,48 |
| Combo Adaptive — target pieno 3R | UNI | LONG | Combo Adaptive | 60m | 2,0x | 8,65319 | 8,65319 | 8,15820 | 4,36986 | 10,13816 | €397,70 | €795,39 | €45,50 | €0,00 |
| Combo Adaptive — target pieno 3R | AVAX | LONG | Combo Adaptive | 60m | 2,0x | 11,18924 | 11,18924 | 10,58712 | 5,65056 | 12,99560 | €436,15 | €872,30 | €46,94 | €0,00 |
| Combo Adaptive — target pieno 3R | SUI | LONG | Combo Adaptive | 60m | 2,0x | 1,01610 | 1,00890 | 0,96309 | 0,51313 | 1,17514 | €457,29 | €914,58 | €47,71 | €-6,48 |
| Combo Adaptive — target pieno 3R | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00001 | 0,00000 | 0,00000 | 0,00000 | 0,00001 | €447,36 | €894,72 | €47,66 | €-8,21 |
| Combo Adaptive — target pieno 3R | DOGE | LONG | Combo Adaptive | 60m | 2,0x | 0,09878 | 0,09876 | 0,09554 | 0,04988 | 0,10851 | €16,03 | €32,07 | €1,05 | €-0,01 |
| Eth Ema 1H | ETH | LONG | Trend following EMA | 60m | 3,0x | 2702,14032 | 2754,86000 | 2727,01966 | 1814,93758 | 2799,99371 | €866,56 | €2.599,67 | €0,00 | €50,72 |
| Doge Ema 1H | DOGE | LONG | Trend following EMA | 60m | 3,0x | 0,09878 | 0,09876 | 0,09554 | 0,06635 | 0,10527 | €516,80 | €1.550,40 | €50,90 | €-0,31 |
| Doge Donchian 1H | DOGE | LONG | Donchian breakout 20 barre | 60m | 3,0x | 0,09878 | 0,09876 | 0,09590 | 0,06635 | 0,10455 | €582,66 | €1.747,97 | €51,01 | €-0,35 |
| Doge Bollinger 1H | DOGE | SHORT | Bollinger mean reversion | 60m | 3,0x | 0,09874 | 0,09876 | 0,10144 | 0,13116 | 0,09469 | €594,61 | €1.783,84 | €48,81 | €-0,36 |
| Master Adaptive V1 | UNI | LONG | Master Adaptive Consensus | 60m | 2,0x | 8,65319 | 8,65319 | 8,15820 | 4,36986 | 9,64317 | €408,50 | €816,99 | €46,73 | €0,00 |
| Master Adaptive V1 | SUI | LONG | Master Adaptive Consensus | 60m | 2,0x | 1,00460 | 1,00890 | 0,95733 | 0,50732 | 1,09913 | €503,92 | €1.007,84 | €47,42 | €4,31 |
| Master Adaptive V1 | AVAX | LONG | Master Adaptive Consensus | 60m | 2,0x | 11,18924 | 11,18924 | 10,58712 | 5,65056 | 12,39348 | €440,55 | €881,10 | €47,41 | €0,00 |
| Master Adaptive Expanded V1 | UNI | LONG | Master Adaptive Consensus | 60m | 2,0x | 8,65319 | 8,65319 | 8,15820 | 4,36986 | 9,64317 | €400,07 | €800,15 | €45,77 | €0,00 |
| Master Adaptive Expanded V1 | SUI | LONG | Master Adaptive Consensus | 60m | 2,0x | 1,00460 | 1,00890 | 0,95733 | 0,50732 | 1,09913 | €493,53 | €987,06 | €46,44 | €4,22 |
| Master Adaptive Expanded V1 | AVAX | LONG | Master Adaptive Consensus | 60m | 2,0x | 11,18924 | 11,18924 | 10,58712 | 5,65056 | 12,39348 | €431,47 | €862,94 | €46,44 | €0,00 |
| Master Adaptive Gb20 V1 | UNI | LONG | Master Adaptive Consensus | 60m | 2,0x | 8,65319 | 8,65319 | 8,15820 | 4,36986 | 9,64317 | €403,11 | €806,21 | €46,12 | €0,00 |
| Master Adaptive Gb20 V1 | SUI | LONG | Master Adaptive Consensus | 60m | 2,0x | 1,00460 | 1,00890 | 0,95733 | 0,50732 | 1,09913 | €497,27 | €994,54 | €46,79 | €4,26 |
| Master Adaptive Gb20 V1 | AVAX | LONG | Master Adaptive Consensus | 60m | 2,0x | 11,18924 | 11,18924 | 10,58712 | 5,65056 | 12,39348 | €434,74 | €869,48 | €46,79 | €0,00 |
| Master Adaptive Runner25 V1 | ZEC | LONG | Master Adaptive Consensus | 60m | 2,0x | 1366,74329 | 1475,81000 | 1297,25468 | 690,20536 | 1575,20914 | €389,09 | €778,18 | €39,56 | €62,10 |
| Master Adaptive Runner25 V1 | UNI | LONG | Master Adaptive Consensus | 60m | 2,0x | 8,65319 | 8,65319 | 8,15820 | 4,36986 | 10,13816 | €411,69 | €823,38 | €47,10 | €0,00 |
| Master Adaptive Runner25 V1 | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,21346 | 0,21346 | 0,19751 | 0,10780 | 0,26131 | €68,73 | €137,46 | €10,27 | €0,00 |
| Master Adaptive Runner25 V1 | SUI | LONG | Master Adaptive Consensus | 60m | 2,0x | 1,00460 | 1,00890 | 0,95733 | 0,50732 | 1,14640 | €510,15 | €1.020,30 | €48,00 | €4,37 |
| Master Adaptive Runner25 V1 | AVAX | LONG | Master Adaptive Consensus | 60m | 2,0x | 11,18924 | 11,18924 | 10,58712 | 5,65056 | 12,99560 | €437,29 | €874,58 | €47,06 | €0,00 |
| Combo Adaptive — Side × Regime Guard | UNI | LONG | Combo Adaptive | 60m | 2,0x | 8,44269 | 8,44269 | 7,95170 | 4,26356 | 9,42467 | €458,97 | €917,93 | €53,38 | €0,00 |
| Combo Adaptive — Side × Regime Guard | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 1518,19358 | 1475,81000 | 1455,64754 | 766,68776 | 1643,28565 | €647,84 | €1.295,69 | €53,38 | €-36,17 |
| Combo Adaptive — Side × Regime Guard | AVAX | LONG | Combo Adaptive | 60m | 2,0x | 11,18924 | 11,18924 | 10,58712 | 5,65056 | 12,39348 | €503,86 | €1.007,72 | €54,23 | €0,00 |
| Master Adaptive GB20 — Breakeven 0,5R | UNI | LONG | Master Adaptive Consensus | 60m | 2,0x | 8,65319 | 8,65319 | 8,15820 | 4,36986 | 9,64317 | €410,52 | €821,04 | €46,97 | €0,00 |
| Master Adaptive GB20 — Breakeven 0,5R | SUI | LONG | Master Adaptive Consensus | 60m | 2,0x | 1,00460 | 1,00890 | 0,95733 | 0,50732 | 1,09913 | €506,42 | €1.012,83 | €47,65 | €4,33 |
| Master Adaptive GB20 — Breakeven 0,5R | AVAX | LONG | Master Adaptive Consensus | 60m | 2,0x | 11,18924 | 11,18924 | 10,58712 | 5,65056 | 12,39348 | €442,73 | €885,47 | €47,65 | €0,00 |
| Master Adaptive GB20 — 50% a 0,75R | UNI | LONG | Master Adaptive Consensus | 60m | 2,0x | 8,65319 | 8,65319 | 8,15820 | 4,36986 | 9,64317 | €410,08 | €820,17 | €46,92 | €0,00 |
| Master Adaptive GB20 — 50% a 0,75R | SUI | LONG | Master Adaptive Consensus | 60m | 2,0x | 1,00460 | 1,00890 | 0,95733 | 0,50732 | 1,09913 | €505,88 | €1.011,75 | €47,60 | €4,33 |
| Master Adaptive GB20 — 50% a 0,75R | AVAX | LONG | Master Adaptive Consensus | 60m | 2,0x | 11,18924 | 11,18924 | 10,58712 | 5,65056 | 12,39348 | €442,26 | €884,53 | €47,60 | €0,00 |
| Master Adaptive GB20 — Loss Cap 0,75R | UNI | LONG | Master Adaptive Consensus | 60m | 2,0x | 8,65319 | 8,65319 | 8,28195 | 4,36986 | 9,64317 | €533,46 | €1.066,92 | €45,77 | €0,00 |
| Master Adaptive GB20 — Loss Cap 0,75R | SUI | LONG | Master Adaptive Consensus | 60m | 2,0x | 1,00460 | 1,00890 | 0,96915 | 0,50732 | 1,09913 | €662,16 | €1.324,33 | €46,73 | €5,67 |
| Master Adaptive GB20 — Loss Cap 0,75R | AVAX | LONG | Master Adaptive Consensus | 60m | 2,0x | 11,18924 | 11,18924 | 10,73765 | 5,65056 | 12,39348 | €578,88 | €1.157,76 | €46,73 | €0,00 |
| Rapida V3 NoHigh — Regime Guard | AVAX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 11,32426 | 11,32426 | 10,89502 | 7,60613 | 11,96813 | €500,19 | €1.500,58 | €56,88 | €0,00 |
| Rapida V3 NoHigh — Regime Guard | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2736,65722 | 2754,86000 | 2698,50381 | 1838,12143 | 2793,88732 | €1.359,79 | €4.079,38 | €56,87 | €27,13 |
| Combo Trend — Side × Regime Guard | ZEC | LONG | Combo Trend | 60m | 2,0x | 1478,71568 | 1475,81000 | 1402,15173 | 746,75142 | 1647,15637 | €542,53 | €1.085,06 | €56,18 | €-2,13 |
| Combo Trend — Side × Regime Guard | UNI | LONG | Combo Trend | 60m | 2,0x | 8,44269 | 8,44269 | 7,89714 | 4,26356 | 9,64288 | €35,66 | €71,32 | €4,61 | €0,00 |
| Bilanciata V3 · LONG only | ZEC | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1485,33701 | 1475,81000 | 1415,48789 | 997,65136 | 1625,03524 | €328,43 | €985,30 | €46,33 | €-6,32 |
| Bilanciata V3 · LONG only | UNI | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 8,44269 | 8,44269 | 7,95170 | 5,67067 | 9,42467 | €10,87 | €32,61 | €1,90 | €0,00 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Combo Scanner | SUI | LONG | 2026-09-21T18:00:00+00:00 | 0,99905 | €-54,62 | -1,03 | STOP |
| Top 5 + BTC — Guard + MFE | SUI | LONG | 2026-09-21T18:00:00+00:00 | 0,99905 | €-49,58 | -1,03 | STOP |
| Top 5 + BTC — Guard | SUI | LONG | 2026-09-21T18:00:00+00:00 | 0,99905 | €-50,78 | -1,03 | STOP |
| Rapida V1 — senza PEPE | AKE | LONG | 2026-09-21T18:00:00+00:00 | 0,04969 | €-65,74 | -1,16 | STOP_STRESS_SLIPPAGE |
| Bilanciata 1H — LONG senza Range High Vol | AKE | LONG | 2026-09-21T18:00:00+00:00 | 0,04969 | €-56,22 | -1,16 | STOP_STRESS_SLIPPAGE |
| Bilanciata 1H V1 | AKE | LONG | 2026-09-21T18:00:00+00:00 | 0,04969 | €-54,01 | -1,16 | STOP_STRESS_SLIPPAGE |
| Top 5 + BTC — solo MFE | SUI | LONG | 2026-09-21T17:30:00+00:00 | 1,00440 | €-1,46 | -0,03 | STOP |
| Scanner Top 5 + forza BTC 1H | SUI | LONG | 2026-09-21T17:30:00+00:00 | 1,00440 | €-1,56 | -0,03 | STOP |
| Forza relativa 1H V1 | SUI | LONG | 2026-09-21T17:30:00+00:00 | 1,00440 | €-1,32 | -0,03 | STOP |
| Rapida V3 NoHigh — Regime Guard | XRP | LONG | 2026-09-21T13:45:00+00:00 | 1,47246 | €-4,67 | -0,08 | STOP |
| Rapida V3 NoHigh — Regime Guard | SUI | LONG | 2026-09-21T14:15:00+00:00 | 1,01822 | €18,91 | 0,34 | STOP |
| Master Adaptive GB20 — Loss Cap 0,75R | PEPE | LONG | 2026-09-21T15:00:00+00:00 | 0,00000 | €122,70 | 2,61 | TARGET |

## Regole invarianti

- Nessuna martingala e nessuna mediazione automatica in perdita.
- Il target mensile riduce il rischio quando viene avvicinato o raggiunto; non lo aumenta mai.
- Il portafoglio principale e le simulazioni di confronto hanno contabilità separata.
- Commissioni, slippage e funding sono inclusi nella simulazione secondo i parametri configurati.
- Quando stop e target risultano toccati nella stessa candela, prevale lo stop salvo modifica esplicita della configurazione.

## 🧪 Validazione congiunta Research + Paper

I due campioni vengono letti insieme ma **non sommati**: il paper è normalmente un sottoinsieme dei segnali Research. La soglia usa gli **eventi di mercato indipendenti**.
Research è HYPOTHESIS_SCREENING_ONLY: PF e numerosità non superano un gate di causalità/parità/integrità non PASS.

Requisiti per la revisione live: almeno **30 eventi indipendenti per lato**, PF almeno **1,10**, expectancy positiva e max drawdown paper non superiore a **15,00%**.

| Profilo | Conto paper di riferimento | Research eventi | Paper eventi | PF Research | PF Paper | Exp. Research | Exp. Paper | DD Paper | Accordo | Stato |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 895/30 | 33/30 | 0,91 | 2,04 | -0,05R | €9,09 | 2,01% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 842/30 | 20/30 | 0,87 | 1,90 | -0,06R | €11,76 | 2,73% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 417/30 | 22/30 | 1,05 | 1,74 | 0,02R | €12,35 | 1,72% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 427/30 | 22/30 | 0,99 | 1,57 | -0,01R | €8,43 | 2,27% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 763/30 | 31/30 | 0,97 | 0,62 | -0,01R | €-8,91 | 4,83% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 713/30 | 11/30 | 0,95 | 0,00 | -0,02R | €-38,20 | 4,20% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 244/30 | 8/30 | 0,90 | 1,02 | -0,05R | €0,42 | 2,15% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 586/30 | 17/30 | 0,88 | 4,50 | -0,06R | €14,07 | 1,01% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 814/30 | 24/30 | 0,86 | 0,64 | -0,07R | €-7,61 | 3,23% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 761/30 | 7/30 | 0,79 | 0,02 | -0,10R | €-33,97 | 2,82% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 763/30 | 30/30 | 0,99 | 1,02 | -0,00R | €0,30 | 4,84% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 1264/30 | 55/30 | 0,89 | 1,12 | -0,05R | €1,80 | 3,59% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 336/30 | 15/30 | 0,82 | 0,99 | -0,10R | €-0,32 | 2,70% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 1107/30 | 44/30 | 0,85 | 1,20 | -0,08R | €3,30 | 2,91% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 1111/30 | 37/30 | 0,85 | 0,76 | -0,08R | €-4,40 | 3,08% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 1040/30 | 23/30 | 0,81 | 1,12 | -0,10R | €2,12 | 3,05% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| MAIN | Principale 4H | 470/30 | 71/30 | 0,84 | 1,07 | -0,09R | €1,66 | 6,86% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| MAIN_DYNAMIC_ASSET_SELECTOR_V1 | MAIN — Dynamic Asset Selector | 0/30 | 26/30 | 0,00 | 1,36 | 0,00R | €10,16 | 3,39% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| MAIN_SIDE_REGIME_GUARD_V1 | MAIN — Side × Regime Guard | 0/30 | 65/30 | 0,00 | 1,77 | 0,00R | €13,76 | 8,20% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| RSI_EXTREME_LONG_15M | Scalp RSI Long 25 · prudente · 5x (riferimento tra 9 varianti) | 40/30 | 22/30 | 0,36 | 0,53 | -0,36R | €-2,69 | 0,73% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| RSI_EXTREME_SHORT_15M | Scalp RSI Short 75 · prudente · 5x (riferimento tra 9 varianti) | 57/30 | 34/30 | 0,82 | 0,76 | -0,09R | €-1,29 | 0,84% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_BALANCED | Bilanciata 1H V1 | 1249/30 | 226/30 | 0,91 | 0,85 | -0,05R | €-2,74 | 15,68% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_BALANCED_LONG_NO_RHV_V1 | Bilanciata 1H — LONG senza Range High Vol | 0/30 | 155/30 | 0,00 | 0,86 | 0,00R | €-2,45 | 9,26% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_BALANCED_SHORT_TREND_DOWN_STRICT_V1 | Bilanciata 1H — SHORT Trend Down stretto | 0/30 | 15/30 | 0,00 | 1,01 | 0,00R | €0,14 | 1,80% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_BALANCED_V2 | Bilanciata 1H V2 | 428/30 | 172/30 | 1,05 | 0,92 | 0,03R | €-1,62 | 11,82% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_BALANCED_V3 | Bilanciata 1H V3 Filtered | 811/30 | 237/30 | 0,96 | 1,09 | -0,02R | €1,56 | 14,04% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | Bilanciata V3 · LONG only | 732/30 | 192/30 | 0,92 | 0,94 | -0,04R | €-0,98 | 13,79% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST | Rapida 1H V1 — madre | 208/30 | 78/30 | 0,92 | 1,02 | -0,05R | €0,55 | 6,76% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | Rapida V1 — Long + BTC 1–3 + score <7,5 | 404/30 | 167/30 | 0,93 | 0,81 | -0,03R | €-4,76 | 13,09% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | FAST NoHigh <7,5 · SHORT only | 852/30 | 204/30 | 0,98 | 1,08 | -0,01R | €1,32 | 10,86% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | Rapida V1 — no HIGH + score <7,5 | 919/30 | 241/30 | 0,99 | 1,13 | -0,00R | €2,21 | 10,86% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_NO_PEPE_V1 | Rapida V1 — senza PEPE | 1428/30 | 321/30 | 0,88 | 1,26 | -0,06R | €4,04 | 9,28% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_SCORE_6_75_COST_AWARE_V1 | Rapida score 6–7,5 — Cost Aware | 0/30 | 227/30 | 0,00 | 1,37 | 0,00R | €7,09 | 7,95% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_SCORE_6_75_NO_TREND_UP_V1 | Rapida score 6–7,5 — senza Trend Up | 0/30 | 223/30 | 0,00 | 0,98 | 0,00R | €-0,44 | 15,94% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_SCORE_6_75_RANGE_ONLY_V1 | Rapida score 6–7,5 — Range Only | 0/30 | 77/30 | 0,00 | 1,11 | 0,00R | €2,28 | 6,49% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_SCORE_6_75_V1 | Rapida V1 — score 6–7,5 | 820/30 | 261/30 | 0,94 | 0,98 | -0,03R | €-0,53 | 15,64% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_TP2_V1 | Rapida V1 — target pieno 2R | 1377/30 | 306/30 | 0,86 | 1,19 | -0,07R | €3,08 | 6,56% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V2 | Rapida 1H V2 | 111/30 | 85/30 | 0,99 | 1,28 | -0,01R | €6,59 | 3,89% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3 | Rapida 1H V3 Filtered — madre | 1318/30 | 301/30 | 0,88 | 1,18 | -0,06R | €3,11 | 9,48% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_CAP75_V1 | Rapida V3 — score <7,5 | 1007/30 | 281/30 | 0,92 | 0,91 | -0,04R | €-1,94 | 19,03% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | Rapida V3 — qualità completa + profit lock | 475/30 | 206/30 | 1,08 | 0,98 | 0,04R | €-0,47 | 8,44% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | Rapida V3 — Long + no HIGH + score <7,5 | 483/30 | 208/30 | 1,03 | 0,98 | 0,01R | €-0,52 | 6,64% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | Rapida V3 — Long Only | 865/30 | 294/30 | 0,99 | 1,03 | -0,01R | €0,59 | 12,52% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V1 | Rapida V3 NoHigh — Range Only | 0/30 | 121/30 | 0,00 | 1,08 | 0,00R | €1,70 | 7,07% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_V1 | Rapida V3 NoHigh — Regime Guard | 0/30 | 202/30 | 0,00 | 1,42 | 0,00R | €6,04 | 5,24% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | Rapida V3 — no volatilità HIGH | 954/30 | 227/30 | 0,90 | 1,21 | -0,05R | €2,91 | 7,10% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONLY_V1 | Rapida V3 senza ESPORTS — Long Only | 0/30 | 291/30 | 0,00 | 1,10 | 0,00R | €1,87 | 10,60% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_V1 | Rapida V3 senza ESPORTS — MFE Lock | 0/30 | 257/30 | 0,00 | 1,25 | 0,00R | €3,92 | 9,50% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_GUARD_V1 | Rapida V3 senza ESPORTS — Stress Guard | 0/30 | 194/30 | 0,00 | 1,38 | 0,00R | €7,36 | 5,29% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | Rapida V3 — senza ESPORTS | 1271/30 | 264/30 | 0,86 | 1,07 | -0,07R | €1,22 | 10,92% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_4H_WIDE | Ampia 4H | 439/30 | 70/30 | 0,87 | 1,15 | -0,08R | €3,44 | 4,45% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_BOLLINGER_MR_1H | Benchmark Bollinger mean reversion 1H | 430/30 | 156/30 | 1,02 | 0,51 | 0,01R | €-15,58 | 26,04% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_BTC_ADAPTIVE_1H | Btc Adaptive 1H | 20/30 | 14/30 | 0,65 | 0,80 | -0,18R | €-4,65 | 2,06% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_BTC_ADAPTIVE_4H | Btc Adaptive 4H | 4/30 | 4/30 | 0,76 | 0,77 | -0,19R | €-8,79 | 1,10% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_BTC_BOLLINGER_1H | Btc Bollinger 1H | 12/30 | 9/30 | 2,57 | 2,77 | 0,45R | €22,61 | 0,85% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_BTC_BOLLINGER_4H | Btc Bollinger 4H | 4/30 | 4/30 | 2,81 | 2,86 | 0,50R | €25,47 | 0,91% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_BTC_DONCHIAN_1H | Btc Donchian 1H | 23/30 | 16/30 | 0,40 | 0,85 | -0,42R | €-3,76 | 1,98% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_BTC_DONCHIAN_4H | Btc Donchian 4H | 9/30 | 7/30 | 0,32 | 0,41 | -0,65R | €-27,30 | 2,43% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_BTC_EMA_1H | Btc Ema 1H | 34/30 | 28/30 | 0,52 | 0,36 | -0,32R | €-23,08 | 6,56% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_BTC_EMA_4H | Btc Ema 4H | 6/30 | 5/30 | 0,45 | 0,58 | -0,49R | €-17,17 | 1,76% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE | Combo Adaptive — madre | 1046/30 | 244/30 | 0,97 | 1,26 | -0,01R | €3,82 | 8,17% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | Combo Adaptive — Long Only | 680/30 | 200/30 | 1,03 | 1,24 | 0,01R | €4,02 | 7,78% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | Combo Adaptive — MFE Trail esistente | 1173/30 | 247/30 | 0,99 | 0,84 | -0,01R | €-2,66 | 15,45% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | Combo Adaptive — parziale 1R | 987/30 | 202/30 | 0,95 | 1,21 | -0,03R | €3,06 | 8,69% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | Combo Adaptive — Quality7 + Regime + parziale 1R | 102/30 | 58/30 | 1,37 | 0,95 | 0,16R | €-1,12 | 4,27% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | Combo Adaptive — Quality7 + Regime | 102/30 | 58/30 | 1,33 | 0,86 | 0,14R | €-3,27 | 5,41% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | Combo Adaptive — Quality7 | 372/30 | 116/30 | 0,92 | 0,91 | -0,04R | €-2,16 | 8,88% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | Combo Adaptive — Trend/Transition | 292/30 | 91/30 | 1,02 | 0,79 | 0,01R | €-5,01 | 6,28% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | Combo Adaptive — 75% a 2R + runner 25% a 3R | 47/30 | 173/30 | 0,74 | 0,92 | -0,20R | €-1,51 | 14,10% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_SIDE_REGIME_GUARD_V1 | Combo Adaptive — Side × Regime Guard | 0/30 | 196/30 | 0,00 | 1,27 | 0,00R | €4,41 | 11,68% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | Combo Adaptive — target pieno 3R | 47/30 | 153/30 | 0,74 | 0,84 | -0,20R | €-2,90 | 14,10% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_MEAN_REVERSION | Combo Mean Reversion | 163/30 | 87/30 | 1,01 | 0,52 | 0,00R | €-16,62 | 16,26% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_SCANNER | Combo Scanner | 668/30 | 204/30 | 1,03 | 1,13 | 0,02R | €2,50 | 11,38% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_TREND | Combo Trend | 864/30 | 206/30 | 0,98 | 0,96 | -0,01R | €-0,76 | 14,08% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_TREND_SIDE_REGIME_GUARD_V1 | Combo Trend — Side × Regime Guard | 0/30 | 171/30 | 0,00 | 1,54 | 0,00R | €9,47 | 10,10% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_DOGE_BOLLINGER_1H | Doge Bollinger 1H | 22/30 | 19/30 | 1,03 | 0,58 | 0,01R | €-12,58 | 3,15% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_DOGE_DONCHIAN_1H | Doge Donchian 1H | 26/30 | 20/30 | 0,80 | 1,43 | -0,13R | €10,12 | 3,08% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_DOGE_EMA_1H | Doge Ema 1H | 44/30 | 31/30 | 0,63 | 1,28 | -0,23R | €5,82 | 2,77% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_DONCHIAN_1H | Benchmark Donchian breakout 1H | 456/30 | 178/30 | 0,94 | 1,74 | -0,04R | €15,03 | 6,75% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | Donchian 1H Gb20 120R V1 | 386/30 | 146/30 | 0,96 | 1,88 | -0,02R | €16,28 | 6,75% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_EMA_TREND_1H | Benchmark trend following EMA 1H | 877/30 | 172/30 | 0,94 | 1,05 | -0,03R | €0,87 | 12,31% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_ETH_ADAPTIVE_1H | Eth Adaptive 1H | 36/30 | 26/30 | 0,58 | 0,42 | -0,29R | €-20,78 | 5,44% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_ETH_BOLLINGER_1H | Eth Bollinger 1H | 21/30 | 12/30 | 2,42 | 0,70 | 0,45R | €-10,99 | 4,16% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_ETH_DONCHIAN_1H | Eth Donchian 1H | 32/30 | 23/30 | 0,72 | 0,61 | -0,19R | €-14,07 | 4,65% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_ETH_EMA_1H | Eth Ema 1H | 49/30 | 34/30 | 0,46 | 0,50 | -0,38R | €-17,23 | 5,88% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_ETH_EMA_4H | Eth Ema 4H | 8/30 | 9/30 | 0,39 | 0,41 | -0,40R | €-24,10 | 2,32% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_GLOBAL_PURE | Global Confluence puro 1H | 21/30 | 23/30 | 1,00 | 0,66 | -0,00R | €-9,57 | 3,93% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | Master Adaptive Expanded V1 | 452/30 | 105/30 | 1,07 | 0,78 | 0,04R | €-5,91 | 10,41% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_MASTER_ADAPTIVE_GB20_BE_V1 | Master Adaptive GB20 — Breakeven 0,5R | 0/30 | 130/30 | 0,00 | 0,89 | 0,00R | €-2,89 | 10,08% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_MASTER_ADAPTIVE_GB20_LOSS_CAP_V1 | Master Adaptive GB20 — Loss Cap 0,75R | 0/30 | 119/30 | 0,00 | 0,85 | 0,00R | €-4,46 | 12,05% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_MASTER_ADAPTIVE_GB20_PARTIAL_V1 | Master Adaptive GB20 — 50% a 0,75R | 0/30 | 125/30 | 0,00 | 0,88 | 0,00R | €-3,08 | 9,87% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | Master Adaptive Gb20 V1 | 858/30 | 161/30 | 1,25 | 0,85 | 0,08R | €-3,41 | 10,69% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | Master Adaptive No Alt V1 | 360/30 | 126/30 | 1,02 | 0,61 | 0,01R | €-12,59 | 16,10% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | Master Adaptive Runner25 V1 | 414/30 | 114/30 | 1,09 | 0,85 | 0,06R | €-4,19 | 9,31% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | Master Adaptive Strict3 V1 | 256/30 | 88/30 | 0,91 | 0,56 | -0,06R | €-17,63 | 15,70% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_MASTER_ADAPTIVE_V1 | Master Adaptive V1 | 433/30 | 127/30 | 1,07 | 0,88 | 0,04R | €-3,33 | 9,87% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_RELATIVE_STRENGTH | Forza relativa 1H V1 | 1039/30 | 192/30 | 0,90 | 0,69 | -0,06R | €-5,98 | 19,11% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_RELATIVE_STRENGTH_V2 | Forza relativa 1H V2 | 408/30 | 150/30 | 1,04 | 1,07 | 0,02R | €1,65 | 10,88% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_BOTTOM10_SHORT | Scanner Bottom10 Short | 344/30 | 76/30 | 0,58 | 0,76 | -0,24R | €-6,17 | 9,06% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_BOTTOM15_SHORT | Scanner Bottom15 Short | 344/30 | 76/30 | 0,58 | 0,76 | -0,24R | €-6,17 | 9,06% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_BOTTOM20_SHORT | Scanner Bottom20 Short | 344/30 | 76/30 | 0,58 | 0,76 | -0,24R | €-6,17 | 9,06% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_BOTTOM5_SHORT | Scanner Bottom 5 Short 1H | 364/30 | 95/30 | 0,69 | 0,73 | -0,17R | €-6,55 | 10,17% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_BOTTOM5_SHORT_CONTINUATION_V1 | Scanner Bottom5 Short Continuation V1 | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | Scanner Bottom5 Short Mfe Trail V1 | 413/30 | 67/30 | 0,78 | 0,71 | -0,10R | €-7,99 | 9,08% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | Scanner Bottom5 Short Profit Lock V1 | 371/30 | 68/30 | 0,72 | 0,69 | -0,13R | €-8,08 | 9,08% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP10_LONG | Scanner Top10 Long | 688/30 | 214/30 | 1,00 | 1,13 | -0,00R | €1,91 | 10,31% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP15_LONG | Scanner Top15 Long | 691/30 | 233/30 | 1,00 | 1,21 | 0,00R | €3,22 | 10,31% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP20_LONG | Scanner Top20 Long | 691/30 | 233/30 | 1,00 | 1,21 | 0,00R | €3,22 | 10,31% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC | Scanner Top 5 + forza BTC 1H | 641/30 | 172/30 | 1,04 | 1,15 | 0,02R | €3,00 | 11,27% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | Top 5 + BTC — BTC 2–3 | 230/30 | 71/30 | 0,69 | 0,59 | -0,19R | €-11,65 | 12,43% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | Top 5 + BTC — BTC≤3 | 485/30 | 143/30 | 0,85 | 0,62 | -0,09R | €-9,69 | 20,25% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | Top 5 + BTC — Guard + BTC≤3 + MFE | 527/30 | 166/30 | 1,00 | 0,70 | 0,00R | €-8,15 | 18,17% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | Top 5 + BTC — Guard + BTC≤3 | 436/30 | 143/30 | 0,90 | 0,76 | -0,06R | €-6,46 | 16,24% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | Top 5 + BTC — Guard + MFE | 669/30 | 192/30 | 1,08 | 0,88 | 0,03R | €-2,42 | 8,78% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | Top 5 + BTC — Guard | 545/30 | 176/30 | 1,03 | 0,94 | 0,02R | €-1,29 | 7,34% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | Top 5 + BTC — solo MFE | 739/30 | 164/30 | 1,01 | 0,95 | 0,00R | €-0,87 | 12,28% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | Top 5 + BTC — 75% a 2,2R + runner 3R | 588/30 | 184/30 | 0,99 | 0,96 | -0,01R | €-0,77 | 12,06% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | Top 5 + BTC — target pieno 3R | 560/30 | 180/30 | 1,01 | 0,97 | 0,01R | €-0,76 | 11,91% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_LONG | Scanner Top 5 Long 1H | 701/30 | 207/30 | 1,05 | 1,29 | 0,03R | €5,15 | 8,85% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SOL_ADAPTIVE_1H | Sol Adaptive 1H | 48/30 | 31/30 | 0,98 | 1,05 | -0,01R | €1,32 | 4,59% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SOL_ADAPTIVE_4H | Sol Adaptive 4H | 12/30 | 10/30 | 1,78 | 1,64 | 0,34R | €13,87 | 1,37% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SOL_BOLLINGER_1H | Sol Bollinger 1H | 34/30 | 22/30 | 0,68 | 0,58 | -0,19R | €-15,05 | 3,69% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SOL_BOLLINGER_4H | Sol Bollinger 4H | 8/30 | 5/30 | 1,24 | 0,88 | 0,12R | €-3,80 | 1,96% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SOL_DONCHIAN_1H | Sol Donchian 1H | 39/30 | 25/30 | 1,25 | 1,88 | 0,12R | €14,88 | 2,77% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SOL_DONCHIAN_4H | Sol Donchian 4H | 10/30 | 9/30 | 0,73 | 1,15 | -0,20R | €4,46 | 2,25% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SOL_EMA_1H | Sol Ema 1H | 49/30 | 33/30 | 0,98 | 1,00 | -0,01R | €0,08 | 4,45% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SOL_EMA_4H | Sol Ema 4H | 13/30 | 11/30 | 0,80 | 1,02 | -0,13R | €0,50 | 2,27% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |

Per le famiglie RSI con più configurazioni di leva o margine, il lato paper usa il conto con il maggior numero di eventi indipendenti; i conti duplicati non vengono aggregati.
`PRONTA PER REVISIONE LIVE` non invia ordini e non sposta capitale: abilita soltanto una revisione manuale finale.

## 🎯 DOGE Rejection Short — conto dedicato €3.600

Simulazione separata **paper only**: capitale/margine iniziale **€3.600**, leva **5x**, esposizione iniziale **€18.000**. Non modifica i conti paper da €10.000 e non invia ordini reali.

- Stato: **INVALIDATED**
- Prezzo DOGE: **0.09876**
- Pre-allarme: **0.0765**; zona armata: **0.0775**; trigger rejection: **0.078**
- Invalidazione prima dell’entrata: chiusura 15m sopra **0.07966**

| Capitale iniziale | Balance | Equity | P&L aperto | Eventi chiusi | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- |
| €3.600,00 | €3.600,00 | €3.600,00 | €0,00 | 0 | 0,00% | 0,00 | 0,00% |

### Filtri correnti

| Filtro | Valore | Stato |
| --- | --- | --- |
| Dati mercato | FRESH | OK |
| Candela 15m | 26.2 min | OK |
| Global DOGE | -6.0 | OK |
| Classic raw | -11.0 | OK |
| DOGE/BTC raw | -6.0 | OK |
| Pattern ribassista | MATURO | OK |
| BTC sotto filtro | 85944.2 | NO |

### Ultima candela 15m valutata

- Rejection accettata: **NO**; motivo: **closed_back_below_trigger, close_below_invalidation, entry_not_chased, bearish_confirmation, stop_within_limit**
- High **0.09999**; close **0.09963**; wick alta **45.0%**; volume **x1.22**

### Gestione

- TP1 0,07107: chiude 25% e porta lo stop residuo al pareggio costi.
- TP2 0,06961: chiude 25% e porta lo stop residuo a TP1.
- TP3 0,06400: chiude 25% e porta lo stop residuo a TP2.
- TP4 0,06000: chiude l’ultimo 25%.
- Stop iniziale dinamico: almeno 0,08060, sopra il massimo della rejection con buffer 0,2%, mai oltre 0,08120.
- Politica conservativa: se stop e target sono toccati nella stessa candela, prevale lo stop.

## 🔬 Research All Signals

CAUSALITY= AFFECTED (storico) / CLEAN solo per LEGACY_RESEARCH_CAUSAL_V3
SEMANTIC_PARITY= REQUIRES_REVIEW · EVIDENCE_TIER=RESEARCH
PROMOTION_ELIGIBLE=NO · HYPOTHESIS_SCREENING_ONLY
⚠ Historical Research result — invalid for promotion evidence
Campioni separati per causal/evidence generation: LEGACY_PRE_CAUSAL_V3=539; LEGACY_RESEARCH_EVIDENCE_V3=21784; UNKNOWN_EVIDENCE_GENERATION=31764

Registro parallelo senza limite globale di quattro posizioni. Considera soltanto segnali validi con dati freschi; non modifica i conti paper e non genera ordini reali.

### Regime di mercato osservato

- Regime: **TREND_UP_HIGH_VOL**
- Famiglia: **TREND_UP**
- Confidenza: **85,20%**
- Volatilità: **HIGH**
- Rotazione strategie: **SOLO OSSERVAZIONE — nessun peso operativo viene ancora modificato**
- Motivo: Trend BTC rialzista confermato dalla breadth: score +4.0, 83% sopra EMA50, ADX 43.1.
- BTC trend score: **4,00**; ADX: **43,08**; breadth sopra EMA50: **83,33%**
- Mediana alt vs BTC: **-1,18%**; dispersione: **10,56%**

- Aperti in questo ciclo: **31**
- Chiusi in questo ciclo: **0**
- Posizioni research aperte: **1149**
- Trade research chiusi: **52778**
- Eventi di mercato indipendenti chiusi: **6946**
- Segnali sovrapposti saltati sullo stesso asset/profilo: **143997**
- Posizioni Research V1 senza regime scartate durante la migrazione: **28**

### Risultati complessivi per strategia

| Profilo | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | 18 | 895 | 895 | 37,88% | 0,91 | -0,05R | €-409,48 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | 17 | 842 | 842 | 37,41% | 0,87 | -0,06R | €-519,40 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | 7 | 417 | 417 | 51,08% | 1,05 | 0,02R | €93,83 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | 7 | 427 | 427 | 39,11% | 0,99 | -0,01R | €-29,72 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | 12 | 763 | 763 | 38,66% | 0,97 | -0,01R | €-96,58 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | 12 | 713 | 713 | 38,85% | 0,95 | -0,02R | €-153,39 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | 2 | 244 | 244 | 39,34% | 0,90 | -0,05R | €-116,28 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | 10 | 586 | 586 | 37,37% | 0,88 | -0,06R | €-371,14 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | 14 | 814 | 814 | 36,36% | 0,86 | -0,07R | €-562,73 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | 14 | 761 | 761 | 35,61% | 0,79 | -0,10R | €-798,52 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | 12 | 763 | 763 | 38,93% | 0,99 | -0,00R | €-36,91 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | 18 | 1264 | 1264 | 41,46% | 0,89 | -0,05R | €-616,10 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | 3 | 336 | 336 | 41,07% | 0,82 | -0,10R | €-333,33 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | 20 | 1107 | 1107 | 36,04% | 0,85 | -0,08R | €-838,37 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | 20 | 1111 | 1111 | 36,00% | 0,85 | -0,08R | €-838,91 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | 20 | 1040 | 1040 | 35,48% | 0,81 | -0,10R | €-1009,40 |
| MAIN | 25 | 470 | 470 | 31,70% | 0,84 | -0,09R | €-432,30 |
| RSI_EXTREME_LONG_15M | 0 | 40 | 40 | 37,50% | 0,36 | -0,36R | €-145,44 |
| RSI_EXTREME_SHORT_15M | 0 | 57 | 57 | 42,11% | 0,82 | -0,09R | €-52,44 |
| Bilanciata 1H V1 | 30 | 1249 | 1249 | 38,51% | 0,91 | -0,05R | €-594,96 |
| Bilanciata 1H V2 | 13 | 491 | 428 | 41,96% | 1,05 | 0,03R | €137,90 |
| Bilanciata 1H V3 Filtered | 21 | 811 | 811 | 39,58% | 0,96 | -0,02R | €-162,82 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | 21 | 732 | 732 | 39,62% | 0,92 | -0,04R | €-308,17 |
| Rapida 1H V1 | 0 | 208 | 208 | 38,94% | 0,92 | -0,05R | €-101,45 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | 2 | 404 | 404 | 39,60% | 0,93 | -0,03R | €-133,93 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | 16 | 852 | 852 | 40,14% | 0,98 | -0,01R | €-76,61 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | 16 | 919 | 919 | 40,37% | 0,99 | -0,00R | €-42,27 |
| SHADOW_1H_FAST_NO_PEPE_V1 | 24 | 1428 | 1428 | 38,31% | 0,88 | -0,06R | €-847,64 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | 14 | 820 | 820 | 40,00% | 0,94 | -0,03R | €-221,37 |
| SHADOW_1H_FAST_TP2_V1 | 25 | 1377 | 1377 | 36,24% | 0,86 | -0,07R | €-967,22 |
| Rapida 1H V2 | 0 | 126 | 111 | 45,24% | 0,99 | -0,01R | €-9,05 |
| Rapida 1H V3 Filtered | 20 | 1318 | 1318 | 38,39% | 0,88 | -0,06R | €-787,77 |
| SHADOW_1H_FAST_V3_CAP75_V1 | 17 | 1007 | 1007 | 39,92% | 0,92 | -0,04R | €-393,26 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | 6 | 475 | 475 | 51,37% | 1,08 | 0,04R | €194,22 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | 6 | 483 | 483 | 41,20% | 1,03 | 0,01R | €69,18 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | 12 | 865 | 865 | 40,69% | 0,99 | -0,01R | €-57,87 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | 14 | 954 | 954 | 38,47% | 0,90 | -0,05R | €-456,73 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | 20 | 1271 | 1271 | 38,08% | 0,86 | -0,07R | €-869,73 |
| SHADOW_4H_WIDE | 31 | 439 | 439 | 26,42% | 0,87 | -0,08R | €-359,16 |
| SHADOW_BOLLINGER_MR_1H | 3 | 430 | 430 | 47,91% | 1,02 | 0,01R | €42,24 |
| SHADOW_BTC_ADAPTIVE_1H | 0 | 20 | 20 | 50,00% | 0,65 | -0,18R | €-35,17 |
| SHADOW_BTC_ADAPTIVE_4H | 0 | 4 | 4 | 25,00% | 0,76 | -0,19R | €-7,44 |
| SHADOW_BTC_BOLLINGER_1H | 0 | 12 | 12 | 75,00% | 2,57 | 0,45R | €53,43 |
| SHADOW_BTC_BOLLINGER_4H | 0 | 4 | 4 | 75,00% | 2,81 | 0,50R | €19,94 |
| SHADOW_BTC_DONCHIAN_1H | 0 | 23 | 23 | 34,78% | 0,40 | -0,42R | €-95,85 |
| SHADOW_BTC_DONCHIAN_4H | 0 | 9 | 9 | 11,11% | 0,32 | -0,65R | €-58,49 |
| SHADOW_BTC_EMA_1H | 0 | 34 | 34 | 38,24% | 0,52 | -0,32R | €-109,09 |
| SHADOW_BTC_EMA_4H | 0 | 6 | 6 | 16,67% | 0,45 | -0,49R | €-29,19 |
| SHADOW_COMBO_ADAPTIVE | 25 | 1046 | 1046 | 41,11% | 0,97 | -0,01R | €-152,27 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | 16 | 680 | 680 | 42,50% | 1,03 | 0,01R | €91,01 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | 25 | 1173 | 1173 | 41,35% | 0,99 | -0,01R | €-75,96 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | 25 | 987 | 987 | 42,86% | 0,95 | -0,03R | €-276,41 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | 1 | 102 | 102 | 49,02% | 1,37 | 0,16R | €159,66 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | 1 | 102 | 102 | 44,12% | 1,33 | 0,14R | €140,93 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | 15 | 372 | 372 | 40,59% | 0,92 | -0,04R | €-147,32 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | 5 | 292 | 292 | 41,10% | 1,02 | 0,01R | €22,63 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | 0 | 47 | 47 | 19,15% | 0,74 | -0,20R | €-92,41 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | 0 | 47 | 47 | 19,15% | 0,74 | -0,20R | €-92,41 |
| SHADOW_COMBO_MEAN_REVERSION | 0 | 163 | 163 | 46,63% | 1,01 | 0,00R | €4,45 |
| SHADOW_COMBO_SCANNER | 18 | 668 | 668 | 40,12% | 1,03 | 0,02R | €125,04 |
| SHADOW_COMBO_TREND | 27 | 864 | 864 | 38,08% | 0,98 | -0,01R | €-108,05 |
| SHADOW_DOGE_BOLLINGER_1H | 1 | 22 | 22 | 54,55% | 1,03 | 0,01R | €2,87 |
| SHADOW_DOGE_DONCHIAN_1H | 1 | 26 | 26 | 42,31% | 0,80 | -0,13R | €-33,11 |
| SHADOW_DOGE_EMA_1H | 1 | 44 | 44 | 36,36% | 0,63 | -0,23R | €-100,13 |
| SHADOW_DONCHIAN_1H | 10 | 456 | 456 | 37,06% | 0,94 | -0,04R | €-160,83 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | 10 | 386 | 386 | 39,12% | 0,96 | -0,02R | €-95,75 |
| SHADOW_EMA_TREND_1H | 29 | 877 | 877 | 37,29% | 0,94 | -0,03R | €-306,66 |
| SHADOW_ETH_ADAPTIVE_1H | 0 | 36 | 36 | 36,11% | 0,58 | -0,29R | €-105,28 |
| SHADOW_ETH_BOLLINGER_1H | 0 | 21 | 21 | 66,67% | 2,42 | 0,45R | €94,65 |
| SHADOW_ETH_DONCHIAN_1H | 0 | 32 | 32 | 37,50% | 0,72 | -0,19R | €-60,39 |
| SHADOW_ETH_EMA_1H | 1 | 49 | 49 | 34,69% | 0,46 | -0,38R | €-184,70 |
| SHADOW_ETH_EMA_4H | 1 | 8 | 8 | 37,50% | 0,39 | -0,40R | €-31,92 |
| SHADOW_GLOBAL_PURE | 0 | 21 | 21 | 47,62% | 1,00 | -0,00R | €-0,01 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | 14 | 452 | 452 | 35,18% | 1,07 | 0,04R | €202,93 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | 11 | 858 | 858 | 66,08% | 1,25 | 0,08R | €697,81 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | 8 | 360 | 360 | 33,61% | 1,02 | 0,01R | €52,42 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | 14 | 414 | 414 | 34,78% | 1,09 | 0,06R | €231,70 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | 5 | 256 | 256 | 31,25% | 0,91 | -0,06R | €-149,06 |
| SHADOW_MASTER_ADAPTIVE_V1 | 14 | 433 | 433 | 35,10% | 1,07 | 0,04R | €183,70 |
| Forza relativa 1H V1 | 31 | 1039 | 1039 | 35,03% | 0,90 | -0,06R | €-576,20 |
| Forza relativa 1H V2 | 21 | 440 | 408 | 38,64% | 1,04 | 0,02R | €92,97 |
| SHADOW_SCANNER_BOTTOM10_SHORT | 10 | 344 | 344 | 31,40% | 0,58 | -0,24R | €-825,28 |
| SHADOW_SCANNER_BOTTOM15_SHORT | 10 | 344 | 344 | 31,40% | 0,58 | -0,24R | €-825,28 |
| SHADOW_SCANNER_BOTTOM20_SHORT | 10 | 344 | 344 | 31,40% | 0,58 | -0,24R | €-825,28 |
| SHADOW_SCANNER_BOTTOM5_SHORT | 10 | 364 | 364 | 32,14% | 0,69 | -0,17R | €-635,56 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | 10 | 413 | 413 | 54,00% | 0,78 | -0,10R | €-401,60 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | 10 | 371 | 371 | 53,10% | 0,72 | -0,13R | €-464,38 |
| SHADOW_SCANNER_TOP10_LONG | 18 | 688 | 688 | 41,28% | 1,00 | -0,00R | €-0,97 |
| SHADOW_SCANNER_TOP15_LONG | 18 | 691 | 691 | 41,39% | 1,00 | 0,00R | €5,05 |
| SHADOW_SCANNER_TOP20_LONG | 18 | 691 | 691 | 41,39% | 1,00 | 0,00R | €5,05 |
| SHADOW_SCANNER_TOP5_BTC | 18 | 641 | 641 | 39,63% | 1,04 | 0,02R | €122,32 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | 7 | 230 | 230 | 33,91% | 0,69 | -0,19R | €-432,00 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | 12 | 485 | 485 | 36,29% | 0,85 | -0,09R | €-419,69 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | 10 | 527 | 527 | 43,45% | 1,00 | 0,00R | €8,43 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | 11 | 436 | 436 | 37,84% | 0,90 | -0,06R | €-242,14 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | 16 | 669 | 669 | 44,54% | 1,08 | 0,03R | €225,46 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | 17 | 545 | 545 | 40,55% | 1,03 | 0,02R | €100,78 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | 18 | 739 | 739 | 43,44% | 1,01 | 0,00R | €30,97 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | 18 | 588 | 588 | 38,95% | 0,99 | -0,01R | €-43,64 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | 18 | 560 | 560 | 38,57% | 1,01 | 0,01R | €32,16 |
| SHADOW_SCANNER_TOP5_LONG | 17 | 701 | 701 | 40,80% | 1,05 | 0,03R | €179,70 |
| SHADOW_SOL_ADAPTIVE_1H | 0 | 48 | 48 | 43,75% | 0,98 | -0,01R | €-6,90 |
| SHADOW_SOL_ADAPTIVE_4H | 0 | 12 | 12 | 58,33% | 1,78 | 0,34R | €40,79 |
| SHADOW_SOL_BOLLINGER_1H | 0 | 34 | 34 | 44,12% | 0,68 | -0,19R | €-64,07 |
| SHADOW_SOL_BOLLINGER_4H | 0 | 8 | 8 | 50,00% | 1,24 | 0,12R | €9,94 |
| SHADOW_SOL_DONCHIAN_1H | 0 | 39 | 39 | 53,85% | 1,25 | 0,12R | €48,25 |
| SHADOW_SOL_DONCHIAN_4H | 1 | 10 | 10 | 30,00% | 0,73 | -0,20R | €-20,19 |
| SHADOW_SOL_EMA_1H | 0 | 49 | 49 | 40,82% | 0,98 | -0,01R | €-6,35 |
| SHADOW_SOL_EMA_4H | 0 | 13 | 13 | 38,46% | 0,80 | -0,13R | €-16,87 |

### Matrice strategia × regime all’entrata

| Profilo | Regime entrata | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | ALT_ROTATION_DOWN | 4 | 128 | 128 | 32,03% | 0,65 | -0,19R | €-244,37 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | ALT_ROTATION_UP | 6 | 260 | 260 | 45,38% | 1,15 | 0,07R | €171,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | RANGE | 4 | 208 | 208 | 41,35% | 0,98 | -0,01R | €-18,44 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | RANGE_HIGH_VOL | 1 | 49 | 49 | 26,53% | 0,30 | -0,45R | €-220,07 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | RANGE_LOW_VOL | 1 | 7 | 7 | 71,43% | 2,09 | 0,32R | €22,14 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TRANSITION | 0 | 68 | 68 | 36,76% | 1,38 | 0,16R | €105,93 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_DOWN | 0 | 60 | 60 | 26,67% | 0,55 | -0,26R | €-153,33 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_DOWN_HIGH_VOL | 1 | 6 | 6 | 16,67% | 0,14 | -0,47R | €-28,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_UP | 0 | 70 | 70 | 21,43% | 0,47 | -0,28R | €-198,89 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_UP_HIGH_VOL | 1 | 39 | 39 | 48,72% | 2,08 | 0,40R | €154,54 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | ALT_ROTATION_DOWN | 4 | 118 | 118 | 31,36% | 0,57 | -0,25R | €-297,32 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | ALT_ROTATION_UP | 5 | 241 | 241 | 43,98% | 1,15 | 0,07R | €166,14 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | RANGE | 4 | 199 | 199 | 40,70% | 0,86 | -0,07R | €-136,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | RANGE_HIGH_VOL | 1 | 47 | 47 | 25,53% | 0,28 | -0,47R | €-219,69 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | RANGE_LOW_VOL | 1 | 6 | 6 | 83,33% | 5,17 | 0,70R | €42,28 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TRANSITION | 0 | 67 | 67 | 37,31% | 1,37 | 0,15R | €99,32 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TREND_DOWN | 0 | 56 | 56 | 25,00% | 0,52 | -0,27R | €-151,45 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TREND_DOWN_HIGH_VOL | 1 | 6 | 6 | 16,67% | 0,14 | -0,47R | €-28,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TREND_UP | 0 | 66 | 66 | 24,24% | 0,51 | -0,27R | €-175,37 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TREND_UP_HIGH_VOL | 1 | 36 | 36 | 50,00% | 2,38 | 0,50R | €181,08 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | ALT_ROTATION_DOWN | 0 | 17 | 17 | 41,18% | 0,64 | -0,22R | €-37,79 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | ALT_ROTATION_UP | 4 | 156 | 156 | 56,41% | 1,28 | 0,13R | €196,68 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | RANGE | 2 | 113 | 113 | 46,02% | 0,83 | -0,09R | €-105,26 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | RANGE_LOW_VOL | 1 | 6 | 6 | 66,67% | 2,10 | 0,37R | €22,35 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | TRANSITION | 0 | 42 | 42 | 64,29% | 2,20 | 0,39R | €163,01 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | TREND_DOWN | 0 | 30 | 30 | 43,33% | 0,70 | -0,17R | €-49,70 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | TREND_UP | 0 | 53 | 53 | 41,51% | 0,66 | -0,18R | €-95,48 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | ALT_ROTATION_DOWN | 0 | 16 | 16 | 31,25% | 0,65 | -0,21R | €-33,15 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | ALT_ROTATION_UP | 4 | 161 | 161 | 42,86% | 1,09 | 0,04R | €63,49 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | RANGE | 2 | 118 | 118 | 41,53% | 0,91 | -0,05R | €-53,78 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | RANGE_LOW_VOL | 1 | 6 | 6 | 66,67% | 2,03 | 0,35R | €20,87 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | TRANSITION | 0 | 42 | 42 | 38,10% | 1,86 | 0,26R | €109,81 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | TREND_DOWN | 0 | 30 | 30 | 30,00% | 0,68 | -0,20R | €-58,87 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | TREND_UP | 0 | 54 | 54 | 27,78% | 0,70 | -0,14R | €-78,09 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | ALT_ROTATION_DOWN | 1 | 55 | 55 | 30,91% | 0,81 | -0,08R | €-45,71 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | ALT_ROTATION_UP | 7 | 303 | 303 | 41,25% | 0,95 | -0,02R | €-71,30 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | RANGE | 2 | 153 | 153 | 40,52% | 0,95 | -0,03R | €-39,89 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | RANGE_HIGH_VOL | 0 | 32 | 32 | 28,12% | 0,54 | -0,29R | €-91,25 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | RANGE_LOW_VOL | 1 | 7 | 7 | 57,14% | 1,96 | 0,42R | €29,27 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TRANSITION | 0 | 58 | 58 | 41,38% | 1,78 | 0,26R | €147,93 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TREND_DOWN | 0 | 41 | 41 | 34,15% | 0,81 | -0,10R | €-40,79 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TREND_DOWN_HIGH_VOL | 0 | 3 | 3 | 33,33% | 14,98 | 0,14R | €4,28 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TREND_UP | 0 | 74 | 74 | 31,08% | 0,75 | -0,12R | €-91,68 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TREND_UP_HIGH_VOL | 1 | 37 | 37 | 43,24% | 1,66 | 0,28R | €102,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | ALT_ROTATION_DOWN | 1 | 54 | 54 | 31,48% | 0,76 | -0,11R | €-57,43 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | ALT_ROTATION_UP | 7 | 281 | 281 | 40,57% | 0,96 | -0,02R | €-57,03 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | RANGE | 2 | 140 | 140 | 42,14% | 0,91 | -0,05R | €-63,04 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | RANGE_HIGH_VOL | 0 | 30 | 30 | 30,00% | 0,59 | -0,24R | €-73,45 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | RANGE_LOW_VOL | 1 | 5 | 5 | 60,00% | 2,47 | 0,60R | €29,85 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TRANSITION | 0 | 57 | 57 | 42,11% | 1,81 | 0,26R | €145,55 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TREND_DOWN | 0 | 38 | 38 | 31,58% | 0,61 | -0,21R | €-81,29 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TREND_DOWN_HIGH_VOL | 0 | 3 | 3 | 33,33% | 14,98 | 0,14R | €4,28 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TREND_UP | 0 | 68 | 68 | 32,35% | 0,68 | -0,16R | €-110,05 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TREND_UP_HIGH_VOL | 1 | 37 | 37 | 43,24% | 1,71 | 0,30R | €109,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | RANGE | 2 | 240 | 240 | 39,17% | 0,90 | -0,05R | €-116,52 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | RANGE_LOW_VOL | 0 | 4 | 4 | 50,00% | 1,01 | 0,01R | €0,24 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | ALT_ROTATION_DOWN | 3 | 58 | 58 | 37,93% | 0,62 | -0,24R | €-137,42 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | ALT_ROTATION_UP | 5 | 193 | 193 | 39,38% | 0,91 | -0,05R | €-93,85 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | RANGE | 2 | 210 | 210 | 40,48% | 0,97 | -0,02R | €-34,86 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | RANGE_LOW_VOL | 0 | 4 | 4 | 50,00% | 1,01 | 0,01R | €0,24 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | TRANSITION | 0 | 50 | 50 | 36,00% | 1,35 | 0,14R | €69,11 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | TREND_DOWN | 0 | 57 | 57 | 26,32% | 0,62 | -0,20R | €-116,81 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | TREND_UP | 0 | 14 | 14 | 7,14% | 0,26 | -0,41R | €-57,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | ALT_ROTATION_DOWN | 3 | 99 | 99 | 33,33% | 0,60 | -0,24R | €-241,67 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | ALT_ROTATION_UP | 5 | 206 | 206 | 39,81% | 0,95 | -0,03R | €-56,02 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | RANGE | 5 | 261 | 261 | 40,23% | 0,96 | -0,02R | €-46,49 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | RANGE_LOW_VOL | 1 | 9 | 9 | 66,67% | 2,65 | 0,56R | €50,33 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | TRANSITION | 0 | 68 | 68 | 33,82% | 1,20 | 0,08R | €53,09 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | TREND_DOWN | 0 | 80 | 80 | 28,75% | 0,64 | -0,19R | €-150,63 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | TREND_UP | 0 | 91 | 91 | 26,37% | 0,64 | -0,19R | €-171,34 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | ALT_ROTATION_DOWN | 3 | 93 | 93 | 31,18% | 0,53 | -0,30R | €-281,01 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | ALT_ROTATION_UP | 5 | 189 | 189 | 39,15% | 0,92 | -0,04R | €-77,34 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | RANGE | 5 | 247 | 247 | 39,68% | 0,87 | -0,06R | €-154,41 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | RANGE_LOW_VOL | 1 | 6 | 6 | 66,67% | 2,53 | 0,52R | €31,12 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | TRANSITION | 0 | 67 | 67 | 34,33% | 1,14 | 0,05R | €36,28 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | TREND_DOWN | 0 | 74 | 74 | 27,03% | 0,58 | -0,21R | €-158,45 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | TREND_UP | 0 | 85 | 85 | 27,06% | 0,57 | -0,23R | €-194,71 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | ALT_ROTATION_DOWN | 1 | 55 | 55 | 30,91% | 0,81 | -0,08R | €-45,71 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | ALT_ROTATION_UP | 7 | 304 | 304 | 41,45% | 0,97 | -0,02R | €-51,74 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | RANGE | 2 | 153 | 153 | 41,83% | 1,03 | 0,01R | €19,77 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | RANGE_HIGH_VOL | 0 | 32 | 32 | 28,12% | 0,54 | -0,29R | €-91,25 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | RANGE_LOW_VOL | 1 | 6 | 6 | 50,00% | 1,32 | 0,16R | €9,72 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TRANSITION | 0 | 58 | 58 | 41,38% | 1,78 | 0,26R | €147,93 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TREND_DOWN | 0 | 41 | 41 | 34,15% | 0,81 | -0,10R | €-40,79 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TREND_DOWN_HIGH_VOL | 0 | 3 | 3 | 33,33% | 14,98 | 0,14R | €4,28 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TREND_UP | 0 | 74 | 74 | 31,08% | 0,75 | -0,12R | €-91,68 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TREND_UP_HIGH_VOL | 1 | 37 | 37 | 43,24% | 1,66 | 0,28R | €102,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | ALT_ROTATION_DOWN | 4 | 196 | 196 | 37,24% | 0,63 | -0,19R | €-373,91 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | ALT_ROTATION_UP | 6 | 367 | 367 | 43,87% | 1,00 | -0,00R | €-5,55 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | RANGE | 4 | 290 | 290 | 41,72% | 0,99 | -0,00R | €-12,34 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | RANGE_HIGH_VOL | 1 | 67 | 67 | 38,81% | 0,48 | -0,29R | €-193,07 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | RANGE_LOW_VOL | 1 | 8 | 8 | 50,00% | 0,84 | -0,08R | €-6,57 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TRANSITION | 0 | 89 | 89 | 47,19% | 1,55 | 0,17R | €151,33 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_DOWN | 0 | 92 | 92 | 38,04% | 0,78 | -0,09R | €-85,87 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_DOWN_HIGH_VOL | 1 | 5 | 5 | 20,00% | 0,59 | -0,12R | €-5,97 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_UP | 0 | 103 | 103 | 38,83% | 0,72 | -0,14R | €-146,03 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_UP_HIGH_VOL | 1 | 47 | 47 | 44,68% | 1,31 | 0,13R | €61,89 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | ALT_ROTATION_DOWN | 1 | 64 | 64 | 43,75% | 0,82 | -0,11R | €-67,30 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | ALT_ROTATION_UP | 2 | 99 | 99 | 40,40% | 0,90 | -0,05R | €-54,06 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | RANGE | 0 | 109 | 109 | 44,04% | 0,82 | -0,09R | €-99,61 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | RANGE_LOW_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,96R | €19,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | TRANSITION | 0 | 15 | 15 | 60,00% | 1,97 | 0,42R | €63,22 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | TREND_DOWN | 0 | 15 | 15 | 33,33% | 0,56 | -0,20R | €-30,48 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | TREND_UP | 0 | 33 | 33 | 21,21% | 0,31 | -0,50R | €-164,66 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | ALT_ROTATION_DOWN | 4 | 166 | 166 | 28,92% | 0,56 | -0,25R | €-418,03 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | ALT_ROTATION_UP | 8 | 320 | 320 | 40,94% | 0,96 | -0,02R | €-61,51 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | RANGE | 4 | 253 | 253 | 39,53% | 0,94 | -0,03R | €-79,62 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | RANGE_HIGH_VOL | 1 | 66 | 66 | 31,82% | 0,46 | -0,31R | €-206,41 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | RANGE_LOW_VOL | 1 | 9 | 9 | 66,67% | 2,65 | 0,56R | €50,33 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TRANSITION | 0 | 80 | 80 | 37,50% | 1,43 | 0,17R | €133,54 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_DOWN | 0 | 80 | 80 | 28,75% | 0,64 | -0,19R | €-150,63 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_DOWN_HIGH_VOL | 1 | 4 | 4 | 25,00% | 0,39 | -0,18R | €-7,14 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_UP | 0 | 90 | 90 | 25,56% | 0,59 | -0,21R | €-191,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_UP_HIGH_VOL | 1 | 39 | 39 | 41,03% | 1,56 | 0,24R | €92,30 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | ALT_ROTATION_DOWN | 4 | 166 | 166 | 28,92% | 0,56 | -0,25R | €-418,03 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | ALT_ROTATION_UP | 8 | 322 | 322 | 40,99% | 0,97 | -0,02R | €-51,77 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | RANGE | 4 | 254 | 254 | 39,37% | 0,93 | -0,04R | €-89,75 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | RANGE_HIGH_VOL | 1 | 66 | 66 | 31,82% | 0,46 | -0,31R | €-206,41 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | RANGE_LOW_VOL | 1 | 9 | 9 | 66,67% | 2,65 | 0,56R | €50,33 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TRANSITION | 0 | 80 | 80 | 37,50% | 1,43 | 0,17R | €133,54 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_DOWN | 0 | 80 | 80 | 28,75% | 0,64 | -0,19R | €-150,63 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_DOWN_HIGH_VOL | 1 | 4 | 4 | 25,00% | 0,39 | -0,18R | €-7,14 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_UP | 0 | 90 | 90 | 25,56% | 0,59 | -0,21R | €-191,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_UP_HIGH_VOL | 1 | 40 | 40 | 40,00% | 1,56 | 0,23R | €92,16 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | ALT_ROTATION_DOWN | 4 | 156 | 156 | 28,21% | 0,53 | -0,28R | €-438,23 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | ALT_ROTATION_UP | 8 | 296 | 296 | 40,54% | 0,97 | -0,02R | €-49,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | RANGE | 4 | 241 | 241 | 38,59% | 0,81 | -0,09R | €-220,78 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | RANGE_HIGH_VOL | 1 | 61 | 61 | 31,15% | 0,49 | -0,29R | €-179,32 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | RANGE_LOW_VOL | 1 | 6 | 6 | 66,67% | 2,53 | 0,52R | €31,12 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TRANSITION | 0 | 79 | 79 | 37,97% | 1,45 | 0,17R | €133,59 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TREND_DOWN | 0 | 74 | 74 | 27,03% | 0,58 | -0,21R | €-158,45 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TREND_DOWN_HIGH_VOL | 1 | 4 | 4 | 25,00% | 0,39 | -0,18R | €-7,14 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TREND_UP | 0 | 84 | 84 | 26,19% | 0,51 | -0,26R | €-219,58 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TREND_UP_HIGH_VOL | 1 | 39 | 39 | 41,03% | 1,60 | 0,25R | €98,94 |
| MAIN | ALT_ROTATION_DOWN | 4 | 45 | 45 | 31,11% | 0,82 | -0,10R | €-46,65 |
| MAIN | ALT_ROTATION_UP | 10 | 131 | 131 | 32,82% | 0,72 | -0,18R | €-231,77 |
| MAIN | RANGE | 4 | 105 | 105 | 29,52% | 0,82 | -0,11R | €-114,02 |
| MAIN | RANGE_HIGH_VOL | 2 | 27 | 27 | 25,93% | 0,85 | -0,08R | €-20,96 |
| MAIN | RANGE_LOW_VOL | 1 | 5 | 5 | 60,00% | 2,01 | 0,41R | €20,46 |
| MAIN | TRANSITION | 2 | 43 | 43 | 30,23% | 0,83 | -0,10R | €-42,41 |
| MAIN | TREND_DOWN | 0 | 47 | 47 | 27,66% | 0,74 | -0,16R | €-74,94 |
| MAIN | TREND_DOWN_HIGH_VOL | 0 | 4 | 4 | 50,00% | 1,96 | 0,48R | €19,39 |
| MAIN | TREND_UP | 1 | 49 | 49 | 30,61% | 0,96 | -0,03R | €-12,61 |
| MAIN | TREND_UP_HIGH_VOL | 1 | 14 | 14 | 57,14% | 2,37 | 0,51R | €71,20 |
| RSI_EXTREME_LONG_15M | ALT_ROTATION_DOWN | 0 | 3 | 3 | 0,00% | 0,00 | -0,48R | €-14,27 |
| RSI_EXTREME_LONG_15M | ALT_ROTATION_UP | 0 | 3 | 3 | 33,33% | 0,63 | -0,21R | €-6,42 |
| RSI_EXTREME_LONG_15M | RANGE | 0 | 25 | 25 | 32,00% | 0,13 | -0,59R | €-146,37 |
| RSI_EXTREME_LONG_15M | TRANSITION | 0 | 2 | 2 | 50,00% | 1,14 | 0,08R | €1,56 |
| RSI_EXTREME_LONG_15M | TREND_DOWN | 0 | 5 | 5 | 80,00% | 6,42 | 0,48R | €23,84 |
| RSI_EXTREME_LONG_15M | TREND_UP | 0 | 2 | 2 | 50,00% | 0,63 | -0,19R | €-3,79 |
| RSI_EXTREME_SHORT_15M | ALT_ROTATION_DOWN | 0 | 3 | 3 | 100,00% | ∞ | 1,09R | €32,57 |
| RSI_EXTREME_SHORT_15M | ALT_ROTATION_UP | 0 | 25 | 25 | 44,00% | 0,92 | -0,04R | €-9,44 |
| RSI_EXTREME_SHORT_15M | RANGE | 0 | 12 | 12 | 41,67% | 0,85 | -0,08R | €-10,11 |
| RSI_EXTREME_SHORT_15M | RANGE_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,32R | €13,24 |
| RSI_EXTREME_SHORT_15M | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -0,41R | €-4,13 |
| RSI_EXTREME_SHORT_15M | TREND_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 0,31R | €3,08 |
| RSI_EXTREME_SHORT_15M | TREND_UP | 0 | 12 | 12 | 25,00% | 0,34 | -0,45R | €-53,48 |
| RSI_EXTREME_SHORT_15M | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,21R | €-24,16 |
| Bilanciata 1H V1 | ALT_ROTATION_DOWN | 5 | 159 | 159 | 30,19% | 0,56 | -0,28R | €-452,43 |
| Bilanciata 1H V1 | ALT_ROTATION_UP | 10 | 332 | 332 | 46,08% | 1,09 | 0,05R | €160,41 |
| Bilanciata 1H V1 | RANGE | 8 | 290 | 290 | 41,72% | 0,99 | -0,00R | €-10,92 |
| Bilanciata 1H V1 | RANGE_HIGH_VOL | 1 | 74 | 74 | 31,08% | 0,53 | -0,30R | €-219,07 |
| Bilanciata 1H V1 | RANGE_LOW_VOL | 2 | 10 | 10 | 30,00% | 0,95 | -0,03R | €-2,77 |
| Bilanciata 1H V1 | TRANSITION | 0 | 117 | 117 | 37,61% | 1,08 | 0,04R | €48,40 |
| Bilanciata 1H V1 | TREND_DOWN | 0 | 89 | 89 | 31,46% | 0,75 | -0,13R | €-113,61 |
| Bilanciata 1H V1 | TREND_DOWN_HIGH_VOL | 0 | 6 | 6 | 50,00% | 1,44 | 0,24R | €14,27 |
| Bilanciata 1H V1 | TREND_UP | 0 | 130 | 130 | 31,54% | 0,89 | -0,05R | €-70,07 |
| Bilanciata 1H V1 | TREND_UP_HIGH_VOL | 4 | 42 | 42 | 40,48% | 1,24 | 0,12R | €50,82 |
| Bilanciata 1H V2 | ALT_ROTATION_UP | 7 | 180 | 153 | 47,78% | 1,26 | 0,13R | €236,32 |
| Bilanciata 1H V2 | RANGE | 6 | 214 | 191 | 38,32% | 0,83 | -0,09R | €-201,04 |
| Bilanciata 1H V2 | TRANSITION | 0 | 97 | 84 | 39,18% | 1,21 | 0,11R | €102,62 |
| Bilanciata 1H V3 Filtered | ALT_ROTATION_DOWN | 4 | 117 | 117 | 28,21% | 0,49 | -0,33R | €-388,21 |
| Bilanciata 1H V3 Filtered | ALT_ROTATION_UP | 7 | 211 | 211 | 46,45% | 1,17 | 0,09R | €180,48 |
| Bilanciata 1H V3 Filtered | RANGE | 6 | 194 | 194 | 44,33% | 1,09 | 0,05R | €88,01 |
| Bilanciata 1H V3 Filtered | RANGE_HIGH_VOL | 2 | 37 | 37 | 27,03% | 0,41 | -0,37R | €-138,27 |
| Bilanciata 1H V3 Filtered | RANGE_LOW_VOL | 1 | 6 | 6 | 33,33% | 1,25 | 0,13R | €7,85 |
| Bilanciata 1H V3 Filtered | TRANSITION | 0 | 64 | 64 | 37,50% | 1,15 | 0,07R | €44,08 |
| Bilanciata 1H V3 Filtered | TREND_DOWN | 0 | 61 | 61 | 34,43% | 0,66 | -0,19R | €-114,28 |
| Bilanciata 1H V3 Filtered | TREND_DOWN_HIGH_VOL | 0 | 8 | 8 | 37,50% | 0,88 | -0,08R | €-6,12 |
| Bilanciata 1H V3 Filtered | TREND_UP | 0 | 77 | 77 | 35,06% | 1,15 | 0,07R | €56,45 |
| Bilanciata 1H V3 Filtered | TREND_UP_HIGH_VOL | 1 | 36 | 36 | 47,22% | 1,66 | 0,30R | €107,18 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 4 | 106 | 106 | 26,42% | 0,40 | -0,40R | €-421,59 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | ALT_ROTATION_UP | 7 | 209 | 209 | 46,89% | 1,19 | 0,10R | €201,47 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | RANGE | 6 | 172 | 172 | 43,60% | 0,97 | -0,02R | €-28,15 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | RANGE_HIGH_VOL | 2 | 35 | 35 | 28,57% | 0,45 | -0,34R | €-117,44 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | RANGE_LOW_VOL | 1 | 6 | 6 | 33,33% | 1,25 | 0,13R | €7,85 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TRANSITION | 0 | 56 | 56 | 37,50% | 1,16 | 0,07R | €38,40 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TREND_DOWN | 0 | 62 | 62 | 33,87% | 0,63 | -0,20R | €-125,39 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TREND_DOWN_HIGH_VOL | 0 | 8 | 8 | 37,50% | 0,88 | -0,08R | €-6,12 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TREND_UP | 0 | 56 | 56 | 32,14% | 0,98 | -0,01R | €-4,39 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TREND_UP_HIGH_VOL | 1 | 22 | 22 | 63,64% | 3,31 | 0,67R | €147,18 |
| Rapida 1H V1 | ALT_ROTATION_DOWN | 0 | 22 | 22 | 22,73% | 0,43 | -0,42R | €-91,69 |
| Rapida 1H V1 | ALT_ROTATION_UP | 0 | 13 | 13 | 53,85% | 1,58 | 0,29R | €37,18 |
| Rapida 1H V1 | RANGE | 0 | 67 | 67 | 44,78% | 1,20 | 0,11R | €71,76 |
| Rapida 1H V1 | RANGE_HIGH_VOL | 0 | 11 | 11 | 0,00% | 0,00 | -1,09R | €-119,90 |
| Rapida 1H V1 | TRANSITION | 0 | 26 | 26 | 50,00% | 1,57 | 0,27R | €68,95 |
| Rapida 1H V1 | TREND_UP | 0 | 48 | 48 | 41,67% | 0,97 | -0,02R | €-9,20 |
| Rapida 1H V1 | TREND_UP_HIGH_VOL | 0 | 21 | 21 | 28,57% | 0,59 | -0,28R | €-58,55 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | ALT_ROTATION_DOWN | 0 | 31 | 31 | 22,58% | 0,49 | -0,26R | €-80,47 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | ALT_ROTATION_UP | 1 | 152 | 152 | 44,08% | 1,03 | 0,01R | €18,42 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | RANGE | 0 | 82 | 82 | 43,90% | 1,05 | 0,03R | €20,62 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | RANGE_HIGH_VOL | 0 | 19 | 19 | 15,79% | 0,18 | -0,71R | €-135,38 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | RANGE_LOW_VOL | 1 | 9 | 9 | 55,56% | 1,36 | 0,17R | €15,33 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TRANSITION | 0 | 37 | 37 | 45,95% | 1,50 | 0,20R | €74,56 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TREND_UP | 0 | 63 | 63 | 33,33% | 0,87 | -0,06R | €-35,07 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TREND_UP_HIGH_VOL | 0 | 11 | 11 | 36,36% | 0,72 | -0,11R | €-11,94 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | ALT_ROTATION_DOWN | 4 | 86 | 86 | 40,70% | 0,97 | -0,01R | €-12,67 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | ALT_ROTATION_UP | 4 | 223 | 223 | 45,74% | 1,14 | 0,07R | €146,05 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | RANGE | 6 | 273 | 273 | 41,03% | 0,98 | -0,01R | €-22,58 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | RANGE_LOW_VOL | 2 | 11 | 11 | 72,73% | 2,81 | 0,52R | €57,56 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | TRANSITION | 0 | 78 | 78 | 39,74% | 1,13 | 0,05R | €41,79 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | TREND_DOWN | 0 | 82 | 82 | 29,27% | 0,62 | -0,22R | €-176,89 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | TREND_UP | 0 | 99 | 99 | 30,30% | 0,77 | -0,11R | €-109,88 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | ALT_ROTATION_DOWN | 4 | 104 | 104 | 37,50% | 0,83 | -0,09R | €-94,89 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | ALT_ROTATION_UP | 4 | 224 | 224 | 45,98% | 1,16 | 0,07R | €159,94 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | RANGE | 6 | 303 | 303 | 42,90% | 1,08 | 0,04R | €122,61 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | RANGE_LOW_VOL | 2 | 11 | 11 | 72,73% | 2,81 | 0,52R | €57,56 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TRANSITION | 0 | 80 | 80 | 41,25% | 1,23 | 0,09R | €71,48 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TREND_DOWN | 0 | 82 | 82 | 29,27% | 0,62 | -0,22R | €-176,89 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TREND_UP | 0 | 115 | 115 | 29,57% | 0,70 | -0,16R | €-182,09 |
| SHADOW_1H_FAST_NO_PEPE_V1 | ALT_ROTATION_DOWN | 5 | 204 | 204 | 30,39% | 0,61 | -0,23R | €-460,74 |
| SHADOW_1H_FAST_NO_PEPE_V1 | ALT_ROTATION_UP | 9 | 398 | 398 | 42,46% | 0,96 | -0,02R | €-86,46 |
| SHADOW_1H_FAST_NO_PEPE_V1 | RANGE | 5 | 343 | 343 | 41,40% | 1,00 | -0,00R | €-3,84 |
| SHADOW_1H_FAST_NO_PEPE_V1 | RANGE_HIGH_VOL | 1 | 75 | 75 | 38,67% | 0,66 | -0,19R | €-143,83 |
| SHADOW_1H_FAST_NO_PEPE_V1 | RANGE_LOW_VOL | 2 | 11 | 11 | 54,55% | 1,45 | 0,17R | €18,77 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TRANSITION | 0 | 109 | 109 | 42,20% | 1,33 | 0,13R | €141,25 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_DOWN | 0 | 104 | 104 | 29,81% | 0,64 | -0,19R | €-202,58 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_DOWN_HIGH_VOL | 1 | 5 | 5 | 20,00% | 0,66 | -0,15R | €-7,59 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_UP | 0 | 129 | 129 | 29,46% | 0,72 | -0,15R | €-189,99 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_UP_HIGH_VOL | 1 | 50 | 50 | 46,00% | 1,46 | 0,17R | €87,38 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | ALT_ROTATION_DOWN | 4 | 119 | 119 | 32,77% | 0,61 | -0,23R | €-274,27 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | ALT_ROTATION_UP | 4 | 234 | 234 | 43,59% | 1,06 | 0,03R | €62,66 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | RANGE | 3 | 190 | 190 | 45,79% | 1,24 | 0,11R | €210,60 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | RANGE_HIGH_VOL | 1 | 40 | 40 | 35,00% | 0,41 | -0,36R | €-143,00 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | RANGE_LOW_VOL | 1 | 7 | 7 | 100,00% | ∞ | 0,89R | €62,08 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TRANSITION | 0 | 61 | 61 | 42,62% | 1,60 | 0,20R | €120,86 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_DOWN | 0 | 59 | 59 | 27,12% | 0,55 | -0,25R | €-145,13 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_DOWN_HIGH_VOL | 0 | 6 | 6 | 16,67% | 0,34 | -0,47R | €-28,15 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_UP | 0 | 77 | 77 | 28,57% | 0,64 | -0,20R | €-155,05 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_UP_HIGH_VOL | 1 | 27 | 27 | 51,85% | 1,63 | 0,25R | €68,02 |
| SHADOW_1H_FAST_TP2_V1 | ALT_ROTATION_DOWN | 5 | 204 | 204 | 28,43% | 0,60 | -0,24R | €-479,73 |
| SHADOW_1H_FAST_TP2_V1 | ALT_ROTATION_UP | 9 | 388 | 388 | 42,27% | 1,00 | 0,00R | €5,82 |
| SHADOW_1H_FAST_TP2_V1 | RANGE | 5 | 319 | 319 | 40,13% | 0,98 | -0,01R | €-27,72 |
| SHADOW_1H_FAST_TP2_V1 | RANGE_HIGH_VOL | 1 | 77 | 77 | 32,47% | 0,53 | -0,26R | €-203,44 |
| SHADOW_1H_FAST_TP2_V1 | RANGE_LOW_VOL | 2 | 10 | 10 | 50,00% | 1,49 | 0,20R | €20,16 |
| SHADOW_1H_FAST_TP2_V1 | TRANSITION | 0 | 104 | 104 | 39,42% | 1,35 | 0,14R | €146,34 |
| SHADOW_1H_FAST_TP2_V1 | TREND_DOWN | 0 | 98 | 98 | 29,59% | 0,67 | -0,18R | €-179,94 |
| SHADOW_1H_FAST_TP2_V1 | TREND_DOWN_HIGH_VOL | 1 | 5 | 5 | 20,00% | 0,21 | -0,35R | €-17,65 |
| SHADOW_1H_FAST_TP2_V1 | TREND_UP | 0 | 120 | 120 | 23,33% | 0,53 | -0,26R | €-309,07 |
| SHADOW_1H_FAST_TP2_V1 | TREND_UP_HIGH_VOL | 2 | 52 | 52 | 38,46% | 1,37 | 0,15R | €78,01 |
| Rapida 1H V2 | ALT_ROTATION_UP | 0 | 42 | 38 | 45,24% | 0,93 | -0,04R | €-17,29 |
| Rapida 1H V2 | RANGE | 0 | 73 | 62 | 42,47% | 0,95 | -0,03R | €-19,03 |
| Rapida 1H V2 | TRANSITION | 0 | 11 | 11 | 63,64% | 1,79 | 0,25R | €27,27 |
| Rapida 1H V3 Filtered | ALT_ROTATION_DOWN | 4 | 195 | 195 | 30,26% | 0,56 | -0,26R | €-504,90 |
| Rapida 1H V3 Filtered | ALT_ROTATION_UP | 8 | 360 | 360 | 43,33% | 1,02 | 0,01R | €29,20 |
| Rapida 1H V3 Filtered | RANGE | 4 | 306 | 306 | 40,52% | 0,97 | -0,02R | €-47,86 |
| Rapida 1H V3 Filtered | RANGE_HIGH_VOL | 1 | 70 | 70 | 38,57% | 0,60 | -0,23R | €-158,07 |
| Rapida 1H V3 Filtered | RANGE_LOW_VOL | 1 | 10 | 10 | 60,00% | 1,91 | 0,29R | €28,95 |
| Rapida 1H V3 Filtered | TRANSITION | 0 | 94 | 94 | 40,43% | 1,27 | 0,11R | €104,32 |
| Rapida 1H V3 Filtered | TREND_DOWN | 0 | 91 | 91 | 28,57% | 0,63 | -0,19R | €-176,81 |
| Rapida 1H V3 Filtered | TREND_DOWN_HIGH_VOL | 1 | 4 | 4 | 25,00% | 1,25 | 0,07R | €2,92 |
| Rapida 1H V3 Filtered | TREND_UP | 0 | 127 | 127 | 37,01% | 0,96 | -0,02R | €-22,96 |
| Rapida 1H V3 Filtered | TREND_UP_HIGH_VOL | 1 | 61 | 61 | 36,07% | 0,87 | -0,07R | €-42,57 |
| SHADOW_1H_FAST_V3_CAP75_V1 | ALT_ROTATION_DOWN | 4 | 150 | 150 | 33,33% | 0,62 | -0,22R | €-324,13 |
| SHADOW_1H_FAST_V3_CAP75_V1 | ALT_ROTATION_UP | 5 | 284 | 284 | 46,48% | 1,14 | 0,06R | €179,90 |
| SHADOW_1H_FAST_V3_CAP75_V1 | RANGE | 4 | 240 | 240 | 42,08% | 1,05 | 0,02R | €56,58 |
| SHADOW_1H_FAST_V3_CAP75_V1 | RANGE_HIGH_VOL | 1 | 55 | 55 | 32,73% | 0,41 | -0,38R | €-206,58 |
| SHADOW_1H_FAST_V3_CAP75_V1 | RANGE_LOW_VOL | 1 | 8 | 8 | 87,50% | 6,12 | 0,65R | €51,94 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TRANSITION | 0 | 71 | 71 | 40,85% | 1,26 | 0,11R | €75,52 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_DOWN | 0 | 66 | 66 | 27,27% | 0,61 | -0,22R | €-144,01 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_DOWN_HIGH_VOL | 1 | 6 | 6 | 16,67% | 0,45 | -0,30R | €-18,15 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_UP | 0 | 88 | 88 | 29,55% | 0,65 | -0,19R | €-166,87 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_UP_HIGH_VOL | 1 | 39 | 39 | 51,28% | 1,72 | 0,26R | €102,56 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | ALT_ROTATION_DOWN | 0 | 24 | 24 | 29,17% | 0,29 | -0,52R | €-125,13 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | ALT_ROTATION_UP | 3 | 173 | 173 | 56,07% | 1,21 | 0,10R | €167,91 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | RANGE | 2 | 131 | 131 | 47,33% | 1,04 | 0,02R | €27,17 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | RANGE_LOW_VOL | 1 | 6 | 6 | 83,33% | 4,68 | 0,62R | €37,35 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TRANSITION | 0 | 43 | 43 | 65,12% | 2,22 | 0,36R | €154,71 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TREND_DOWN | 0 | 33 | 33 | 42,42% | 0,84 | -0,09R | €-30,17 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TREND_UP | 0 | 65 | 65 | 47,69% | 0,88 | -0,06R | €-37,62 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | ALT_ROTATION_DOWN | 0 | 23 | 23 | 21,74% | 0,28 | -0,52R | €-120,49 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | ALT_ROTATION_UP | 3 | 176 | 176 | 43,75% | 1,08 | 0,04R | €65,94 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | RANGE | 2 | 135 | 135 | 44,44% | 1,13 | 0,07R | €89,81 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | RANGE_LOW_VOL | 1 | 6 | 6 | 83,33% | 4,54 | 0,60R | €35,87 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TRANSITION | 0 | 43 | 43 | 44,19% | 1,85 | 0,26R | €109,67 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TREND_DOWN | 0 | 33 | 33 | 33,33% | 0,76 | -0,14R | €-46,76 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TREND_UP | 0 | 67 | 67 | 32,84% | 0,80 | -0,10R | €-64,87 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 1 | 66 | 66 | 25,76% | 0,48 | -0,27R | €-180,35 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | ALT_ROTATION_UP | 7 | 343 | 343 | 43,15% | 1,01 | 0,00R | €8,85 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | RANGE | 2 | 177 | 177 | 42,94% | 1,06 | 0,03R | €48,89 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | RANGE_HIGH_VOL | 0 | 33 | 33 | 36,36% | 0,66 | -0,20R | €-64,35 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | RANGE_LOW_VOL | 1 | 8 | 8 | 62,50% | 1,88 | 0,35R | €27,84 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TRANSITION | 0 | 62 | 62 | 46,77% | 1,73 | 0,25R | €153,48 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_DOWN | 0 | 48 | 48 | 35,42% | 0,81 | -0,10R | €-49,05 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_DOWN_HIGH_VOL | 0 | 3 | 3 | 33,33% | 47,80 | 0,48R | €14,34 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_UP | 0 | 86 | 86 | 34,88% | 0,87 | -0,07R | €-57,53 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_UP_HIGH_VOL | 1 | 39 | 39 | 43,59% | 1,23 | 0,10R | €40,01 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | ALT_ROTATION_DOWN | 3 | 122 | 122 | 33,61% | 0,60 | -0,24R | €-294,86 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | ALT_ROTATION_UP | 5 | 229 | 229 | 41,92% | 0,98 | -0,01R | €-20,17 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | RANGE | 5 | 315 | 315 | 41,90% | 1,03 | 0,01R | €46,93 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | RANGE_LOW_VOL | 1 | 10 | 10 | 60,00% | 1,91 | 0,29R | €28,95 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TRANSITION | 0 | 74 | 74 | 39,19% | 1,32 | 0,12R | €87,36 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TREND_DOWN | 0 | 91 | 91 | 28,57% | 0,63 | -0,19R | €-176,81 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TREND_UP | 0 | 113 | 113 | 32,74% | 0,79 | -0,11R | €-128,14 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | ALT_ROTATION_DOWN | 4 | 194 | 194 | 30,41% | 0,56 | -0,25R | €-493,47 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | ALT_ROTATION_UP | 8 | 359 | 359 | 42,90% | 0,99 | -0,00R | €-11,92 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | RANGE | 4 | 304 | 304 | 40,46% | 0,96 | -0,02R | €-62,60 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | RANGE_HIGH_VOL | 1 | 69 | 69 | 39,13% | 0,61 | -0,21R | €-147,94 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | RANGE_LOW_VOL | 1 | 10 | 10 | 60,00% | 1,91 | 0,29R | €28,95 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TRANSITION | 0 | 89 | 89 | 40,45% | 1,31 | 0,12R | €107,09 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_DOWN | 0 | 91 | 91 | 28,57% | 0,63 | -0,19R | €-176,81 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_DOWN_HIGH_VOL | 1 | 4 | 4 | 25,00% | 1,25 | 0,07R | €2,92 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_UP | 0 | 110 | 110 | 31,82% | 0,76 | -0,13R | €-145,70 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_UP_HIGH_VOL | 1 | 41 | 41 | 41,46% | 1,16 | 0,07R | €29,74 |
| SHADOW_4H_WIDE | ALT_ROTATION_DOWN | 4 | 45 | 45 | 26,67% | 0,93 | -0,05R | €-20,69 |
| SHADOW_4H_WIDE | ALT_ROTATION_UP | 11 | 109 | 109 | 34,86% | 0,92 | -0,05R | €-54,46 |
| SHADOW_4H_WIDE | RANGE | 5 | 98 | 98 | 20,41% | 0,75 | -0,16R | €-158,83 |
| SHADOW_4H_WIDE | RANGE_HIGH_VOL | 2 | 21 | 21 | 19,05% | 0,84 | -0,10R | €-21,46 |
| SHADOW_4H_WIDE | RANGE_LOW_VOL | 1 | 4 | 4 | 0,00% | 0,00 | -0,76R | €-30,53 |
| SHADOW_4H_WIDE | TRANSITION | 2 | 44 | 44 | 20,45% | 0,59 | -0,28R | €-121,03 |
| SHADOW_4H_WIDE | TREND_DOWN | 1 | 46 | 46 | 26,09% | 0,91 | -0,06R | €-28,84 |
| SHADOW_4H_WIDE | TREND_DOWN_HIGH_VOL | 0 | 5 | 5 | 40,00% | 2,73 | 0,71R | €35,33 |
| SHADOW_4H_WIDE | TREND_UP | 3 | 47 | 47 | 29,79% | 1,26 | 0,14R | €66,40 |
| SHADOW_4H_WIDE | TREND_UP_HIGH_VOL | 2 | 20 | 20 | 25,00% | 0,80 | -0,13R | €-25,04 |
| SHADOW_BOLLINGER_MR_1H | ALT_ROTATION_DOWN | 1 | 56 | 56 | 44,64% | 0,84 | -0,08R | €-45,66 |
| SHADOW_BOLLINGER_MR_1H | ALT_ROTATION_UP | 0 | 151 | 151 | 47,68% | 0,99 | -0,00R | €-5,25 |
| SHADOW_BOLLINGER_MR_1H | RANGE | 0 | 102 | 102 | 49,02% | 0,97 | -0,02R | €-16,51 |
| SHADOW_BOLLINGER_MR_1H | RANGE_HIGH_VOL | 0 | 16 | 16 | 50,00% | 1,36 | 0,15R | €23,95 |
| SHADOW_BOLLINGER_MR_1H | RANGE_LOW_VOL | 0 | 3 | 3 | 33,33% | 0,70 | -0,21R | €-6,33 |
| SHADOW_BOLLINGER_MR_1H | TRANSITION | 0 | 19 | 19 | 52,63% | 1,52 | 0,23R | €44,43 |
| SHADOW_BOLLINGER_MR_1H | TREND_DOWN | 0 | 18 | 18 | 66,67% | 2,87 | 0,45R | €80,90 |
| SHADOW_BOLLINGER_MR_1H | TREND_UP | 0 | 45 | 45 | 42,22% | 0,85 | -0,07R | €-33,39 |
| SHADOW_BOLLINGER_MR_1H | TREND_UP_HIGH_VOL | 2 | 20 | 20 | 45,00% | 1,00 | 0,00R | €0,09 |
| SHADOW_BTC_ADAPTIVE_1H | ALT_ROTATION_DOWN | 0 | 8 | 8 | 50,00% | 0,93 | -0,03R | €-2,49 |
| SHADOW_BTC_ADAPTIVE_1H | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 0,52R | €5,16 |
| SHADOW_BTC_ADAPTIVE_1H | RANGE | 0 | 8 | 8 | 50,00% | 0,45 | -0,31R | €-24,46 |
| SHADOW_BTC_ADAPTIVE_1H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_BTC_ADAPTIVE_1H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 0,88R | €8,85 |
| SHADOW_BTC_ADAPTIVE_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_BTC_ADAPTIVE_4H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 50,00% | 2,32 | 0,69R | €13,75 |
| SHADOW_BTC_ADAPTIVE_4H | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,05R | €-10,52 |
| SHADOW_BTC_ADAPTIVE_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,67 |
| SHADOW_BTC_BOLLINGER_1H | ALT_ROTATION_DOWN | 0 | 5 | 5 | 60,00% | 1,14 | 0,07R | €3,26 |
| SHADOW_BTC_BOLLINGER_1H | RANGE | 0 | 2 | 2 | 100,00% | ∞ | 1,37R | €27,33 |
| SHADOW_BTC_BOLLINGER_1H | RANGE_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,17 | -0,47R | €-9,40 |
| SHADOW_BTC_BOLLINGER_1H | TREND_DOWN | 0 | 2 | 2 | 100,00% | ∞ | 0,93R | €18,57 |
| SHADOW_BTC_BOLLINGER_1H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,37R | €13,67 |
| SHADOW_BTC_BOLLINGER_4H | ALT_ROTATION_DOWN | 0 | 3 | 3 | 66,67% | 2,22 | 0,45R | €13,43 |
| SHADOW_BTC_BOLLINGER_4H | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 0,65R | €6,51 |
| SHADOW_BTC_DONCHIAN_1H | ALT_ROTATION_DOWN | 0 | 8 | 8 | 37,50% | 0,45 | -0,38R | €-30,72 |
| SHADOW_BTC_DONCHIAN_1H | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 0,58R | €5,81 |
| SHADOW_BTC_DONCHIAN_1H | RANGE | 0 | 9 | 9 | 33,33% | 0,41 | -0,38R | €-34,16 |
| SHADOW_BTC_DONCHIAN_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,82R | €8,23 |
| SHADOW_BTC_DONCHIAN_1H | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -1,12R | €-11,25 |
| SHADOW_BTC_DONCHIAN_1H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_BTC_DONCHIAN_1H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_BTC_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_BTC_DONCHIAN_4H | ALT_ROTATION_DOWN | 0 | 4 | 4 | 25,00% | 0,85 | -0,12R | €-4,85 |
| SHADOW_BTC_DONCHIAN_4H | ALT_ROTATION_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,07R | €-21,38 |
| SHADOW_BTC_DONCHIAN_4H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,91 |
| SHADOW_BTC_DONCHIAN_4H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,64 |
| SHADOW_BTC_DONCHIAN_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,71 |
| SHADOW_BTC_EMA_1H | ALT_ROTATION_DOWN | 0 | 8 | 8 | 12,50% | 0,27 | -0,64R | €-51,33 |
| SHADOW_BTC_EMA_1H | ALT_ROTATION_UP | 0 | 5 | 5 | 40,00% | 0,27 | -0,48R | €-24,20 |
| SHADOW_BTC_EMA_1H | RANGE | 0 | 10 | 10 | 60,00% | 1,24 | 0,11R | €10,80 |
| SHADOW_BTC_EMA_1H | RANGE_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,66 | -0,18R | €-3,69 |
| SHADOW_BTC_EMA_1H | TREND_DOWN | 0 | 3 | 3 | 33,33% | 0,16 | -0,62R | €-18,67 |
| SHADOW_BTC_EMA_1H | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,10 |
| SHADOW_BTC_EMA_1H | TREND_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,11R | €-22,22 |
| SHADOW_BTC_EMA_1H | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 66,67% | 2,02 | 0,38R | €11,32 |
| SHADOW_BTC_EMA_4H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 50,00% | 2,31 | 0,68R | €13,64 |
| SHADOW_BTC_EMA_4H | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,57 |
| SHADOW_BTC_EMA_4H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,91 |
| SHADOW_BTC_EMA_4H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,64 |
| SHADOW_BTC_EMA_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,71 |
| SHADOW_COMBO_ADAPTIVE | ALT_ROTATION_DOWN | 6 | 138 | 138 | 32,61% | 0,68 | -0,20R | €-271,96 |
| SHADOW_COMBO_ADAPTIVE | ALT_ROTATION_UP | 8 | 282 | 282 | 46,45% | 1,15 | 0,08R | €219,96 |
| SHADOW_COMBO_ADAPTIVE | RANGE | 6 | 241 | 241 | 44,81% | 0,94 | -0,03R | €-73,87 |
| SHADOW_COMBO_ADAPTIVE | RANGE_HIGH_VOL | 1 | 58 | 58 | 34,48% | 0,53 | -0,26R | €-153,32 |
| SHADOW_COMBO_ADAPTIVE | RANGE_LOW_VOL | 1 | 10 | 10 | 40,00% | 0,95 | -0,03R | €-3,06 |
| SHADOW_COMBO_ADAPTIVE | TRANSITION | 0 | 92 | 92 | 42,39% | 1,23 | 0,11R | €98,46 |
| SHADOW_COMBO_ADAPTIVE | TREND_DOWN | 0 | 76 | 76 | 35,53% | 0,95 | -0,02R | €-18,40 |
| SHADOW_COMBO_ADAPTIVE | TREND_DOWN_HIGH_VOL | 0 | 4 | 4 | 75,00% | 4,61 | 0,91R | €36,57 |
| SHADOW_COMBO_ADAPTIVE | TREND_UP | 0 | 107 | 107 | 37,38% | 1,06 | 0,03R | €31,28 |
| SHADOW_COMBO_ADAPTIVE | TREND_UP_HIGH_VOL | 3 | 38 | 38 | 34,21% | 0,92 | -0,05R | €-17,94 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 1 | 47 | 47 | 31,91% | 0,81 | -0,11R | €-50,70 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | ALT_ROTATION_UP | 8 | 272 | 272 | 45,96% | 1,10 | 0,05R | €148,51 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | RANGE | 3 | 133 | 133 | 46,62% | 0,98 | -0,01R | €-14,79 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | RANGE_HIGH_VOL | 0 | 23 | 23 | 30,43% | 0,38 | -0,37R | €-86,15 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | RANGE_LOW_VOL | 1 | 9 | 9 | 44,44% | 1,14 | 0,08R | €7,09 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TRANSITION | 0 | 53 | 53 | 47,17% | 1,65 | 0,22R | €114,73 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_DOWN | 0 | 45 | 45 | 37,78% | 1,22 | 0,10R | €44,99 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_DOWN_HIGH_VOL | 0 | 3 | 3 | 66,67% | 3,88 | 0,97R | €29,16 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_UP | 0 | 66 | 66 | 31,82% | 0,66 | -0,16R | €-108,36 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_UP_HIGH_VOL | 3 | 29 | 29 | 37,93% | 1,04 | 0,02R | €6,54 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | ALT_ROTATION_DOWN | 5 | 166 | 166 | 35,54% | 0,72 | -0,14R | €-229,09 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | ALT_ROTATION_UP | 8 | 330 | 330 | 41,82% | 1,06 | 0,03R | €93,60 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE | 6 | 255 | 255 | 42,35% | 1,08 | 0,04R | €91,71 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE_HIGH_VOL | 1 | 66 | 66 | 34,85% | 0,49 | -0,26R | €-171,59 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE_LOW_VOL | 1 | 12 | 12 | 33,33% | 0,51 | -0,30R | €-35,58 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TRANSITION | 0 | 84 | 84 | 45,24% | 1,22 | 0,09R | €71,97 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_DOWN | 0 | 100 | 100 | 38,00% | 0,96 | -0,02R | €-16,64 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_DOWN_HIGH_VOL | 0 | 4 | 4 | 75,00% | 3,69 | 0,68R | €27,30 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_UP | 0 | 110 | 110 | 50,00% | 1,25 | 0,10R | €111,43 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_UP_HIGH_VOL | 4 | 46 | 46 | 41,30% | 0,92 | -0,04R | €-19,06 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | ALT_ROTATION_DOWN | 6 | 138 | 138 | 32,61% | 0,69 | -0,19R | €-263,36 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | ALT_ROTATION_UP | 8 | 280 | 280 | 46,79% | 1,10 | 0,05R | €144,55 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | RANGE | 6 | 229 | 229 | 47,16% | 1,00 | -0,00R | €-3,40 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | RANGE_HIGH_VOL | 1 | 56 | 56 | 37,50% | 0,63 | -0,20R | €-113,63 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | RANGE_LOW_VOL | 1 | 10 | 10 | 40,00% | 0,75 | -0,16R | €-15,75 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TRANSITION | 0 | 75 | 75 | 46,67% | 1,21 | 0,09R | €70,55 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_DOWN | 0 | 76 | 76 | 39,47% | 0,96 | -0,02R | €-14,90 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_DOWN_HIGH_VOL | 0 | 4 | 4 | 75,00% | 4,07 | 0,78R | €31,07 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_UP | 0 | 86 | 86 | 38,37% | 0,76 | -0,11R | €-97,49 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_UP_HIGH_VOL | 3 | 33 | 33 | 39,39% | 0,93 | -0,04R | €-14,05 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TRANSITION | 0 | 45 | 45 | 42,22% | 0,97 | -0,01R | €-6,60 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TREND_UP | 0 | 38 | 38 | 52,63% | 1,53 | 0,20R | €77,51 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TREND_UP_HIGH_VOL | 1 | 19 | 19 | 57,89% | 2,69 | 0,47R | €88,74 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TRANSITION | 0 | 45 | 45 | 42,22% | 0,88 | -0,06R | €-26,38 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TREND_UP | 0 | 38 | 38 | 42,11% | 1,37 | 0,14R | €54,94 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TREND_UP_HIGH_VOL | 1 | 19 | 19 | 52,63% | 3,13 | 0,59R | €112,36 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | ALT_ROTATION_DOWN | 4 | 43 | 43 | 37,21% | 0,74 | -0,14R | €-59,10 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | ALT_ROTATION_UP | 6 | 128 | 128 | 44,53% | 0,90 | -0,06R | €-71,09 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | RANGE | 2 | 76 | 76 | 36,84% | 0,79 | -0,13R | €-96,03 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | RANGE_HIGH_VOL | 2 | 15 | 15 | 46,67% | 1,19 | 0,08R | €11,47 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | RANGE_LOW_VOL | 0 | 4 | 4 | 75,00% | 2,67 | 0,42R | €16,87 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TRANSITION | 0 | 39 | 39 | 41,03% | 0,90 | -0,05R | €-19,83 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_DOWN | 0 | 28 | 28 | 25,00% | 0,63 | -0,18R | €-50,57 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_UP | 0 | 26 | 26 | 38,46% | 1,17 | 0,06R | €15,70 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_UP_HIGH_VOL | 1 | 12 | 12 | 58,33% | 6,33 | 0,96R | €115,39 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TRANSITION | 1 | 110 | 110 | 41,82% | 1,06 | 0,03R | €30,23 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TREND_UP | 0 | 131 | 131 | 37,40% | 0,82 | -0,09R | €-113,60 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TREND_UP_HIGH_VOL | 4 | 51 | 51 | 49,02% | 1,43 | 0,21R | €105,99 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_DOWN | 0 | 10 | 10 | 40,00% | 2,13 | 0,62R | €61,68 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_UP | 0 | 5 | 5 | 40,00% | 1,80 | 0,52R | €26,25 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | RANGE | 0 | 17 | 17 | 17,65% | 0,68 | -0,24R | €-40,76 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | TRANSITION | 0 | 2 | 2 | 0,00% | 0,00 | -1,09R | €-21,86 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | TREND_UP | 0 | 9 | 9 | 0,00% | 0,00 | -0,84R | €-75,23 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 0,00% | 0,00 | -1,06R | €-42,49 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | ALT_ROTATION_DOWN | 0 | 10 | 10 | 40,00% | 2,13 | 0,62R | €61,68 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | ALT_ROTATION_UP | 0 | 5 | 5 | 40,00% | 1,80 | 0,52R | €26,25 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | RANGE | 0 | 17 | 17 | 17,65% | 0,68 | -0,24R | €-40,76 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | TRANSITION | 0 | 2 | 2 | 0,00% | 0,00 | -1,09R | €-21,86 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | TREND_UP | 0 | 9 | 9 | 0,00% | 0,00 | -0,84R | €-75,23 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 0,00% | 0,00 | -1,06R | €-42,49 |
| SHADOW_COMBO_MEAN_REVERSION | ALT_ROTATION_DOWN | 0 | 34 | 34 | 38,24% | 0,74 | -0,12R | €-42,14 |
| SHADOW_COMBO_MEAN_REVERSION | ALT_ROTATION_UP | 0 | 23 | 23 | 47,83% | 1,12 | 0,06R | €14,11 |
| SHADOW_COMBO_MEAN_REVERSION | RANGE | 0 | 53 | 53 | 45,28% | 0,87 | -0,07R | €-37,33 |
| SHADOW_COMBO_MEAN_REVERSION | RANGE_HIGH_VOL | 0 | 10 | 10 | 20,00% | 0,44 | -0,38R | €-38,09 |
| SHADOW_COMBO_MEAN_REVERSION | TRANSITION | 0 | 8 | 8 | 62,50% | 2,67 | 0,46R | €36,75 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_DOWN | 0 | 14 | 14 | 64,29% | 1,44 | 0,17R | €23,50 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_UP | 0 | 17 | 17 | 58,82% | 1,72 | 0,23R | €38,61 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 50,00% | 1,42 | 0,23R | €9,02 |
| SHADOW_COMBO_SCANNER | ALT_ROTATION_DOWN | 2 | 50 | 50 | 26,00% | 0,48 | -0,36R | €-178,40 |
| SHADOW_COMBO_SCANNER | ALT_ROTATION_UP | 9 | 218 | 218 | 44,50% | 1,11 | 0,06R | €134,06 |
| SHADOW_COMBO_SCANNER | RANGE | 4 | 145 | 145 | 44,14% | 1,08 | 0,04R | €61,11 |
| SHADOW_COMBO_SCANNER | RANGE_HIGH_VOL | 0 | 25 | 25 | 40,00% | 0,56 | -0,24R | €-60,42 |
| SHADOW_COMBO_SCANNER | RANGE_LOW_VOL | 1 | 10 | 10 | 30,00% | 0,84 | -0,10R | €-9,67 |
| SHADOW_COMBO_SCANNER | TRANSITION | 0 | 72 | 72 | 43,06% | 1,49 | 0,22R | €160,17 |
| SHADOW_COMBO_SCANNER | TREND_DOWN | 0 | 45 | 45 | 31,11% | 0,82 | -0,10R | €-45,10 |
| SHADOW_COMBO_SCANNER | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 2,14 | 0,58R | €11,58 |
| SHADOW_COMBO_SCANNER | TREND_UP | 0 | 75 | 75 | 33,33% | 1,08 | 0,04R | €31,92 |
| SHADOW_COMBO_SCANNER | TREND_UP_HIGH_VOL | 2 | 26 | 26 | 38,46% | 1,14 | 0,08R | €19,78 |
| SHADOW_COMBO_TREND | ALT_ROTATION_DOWN | 6 | 107 | 107 | 28,97% | 0,54 | -0,30R | €-323,14 |
| SHADOW_COMBO_TREND | ALT_ROTATION_UP | 10 | 243 | 243 | 46,09% | 1,16 | 0,09R | €210,74 |
| SHADOW_COMBO_TREND | RANGE | 6 | 201 | 201 | 38,81% | 1,06 | 0,03R | €61,92 |
| SHADOW_COMBO_TREND | RANGE_HIGH_VOL | 1 | 44 | 44 | 40,91% | 1,03 | 0,01R | €6,54 |
| SHADOW_COMBO_TREND | RANGE_LOW_VOL | 2 | 8 | 8 | 37,50% | 1,00 | -0,00R | €-0,10 |
| SHADOW_COMBO_TREND | TRANSITION | 0 | 76 | 76 | 36,84% | 1,15 | 0,08R | €60,00 |
| SHADOW_COMBO_TREND | TREND_DOWN | 0 | 68 | 68 | 30,88% | 0,76 | -0,13R | €-86,73 |
| SHADOW_COMBO_TREND | TREND_DOWN_HIGH_VOL | 0 | 3 | 3 | 66,67% | 1,61 | 0,21R | €6,21 |
| SHADOW_COMBO_TREND | TREND_UP | 0 | 84 | 84 | 30,95% | 0,99 | -0,01R | €-5,46 |
| SHADOW_COMBO_TREND | TREND_UP_HIGH_VOL | 2 | 30 | 30 | 33,33% | 0,80 | -0,13R | €-38,03 |
| SHADOW_DOGE_BOLLINGER_1H | ALT_ROTATION_DOWN | 0 | 6 | 6 | 50,00% | 0,62 | -0,21R | €-12,31 |
| SHADOW_DOGE_BOLLINGER_1H | ALT_ROTATION_UP | 0 | 6 | 6 | 66,67% | 3,84 | 0,56R | €33,45 |
| SHADOW_DOGE_BOLLINGER_1H | RANGE | 0 | 9 | 9 | 55,56% | 0,84 | -0,08R | €-7,12 |
| SHADOW_DOGE_BOLLINGER_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,15 |
| SHADOW_DOGE_BOLLINGER_1H | TREND_UP_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_DOGE_DONCHIAN_1H | ALT_ROTATION_DOWN | 0 | 8 | 8 | 25,00% | 0,33 | -0,56R | €-44,78 |
| SHADOW_DOGE_DONCHIAN_1H | ALT_ROTATION_UP | 0 | 5 | 5 | 20,00% | 0,14 | -0,73R | €-36,57 |
| SHADOW_DOGE_DONCHIAN_1H | RANGE | 0 | 9 | 9 | 55,56% | 1,07 | 0,03R | €3,05 |
| SHADOW_DOGE_DONCHIAN_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,89R | €18,92 |
| SHADOW_DOGE_DONCHIAN_1H | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,88R | €18,76 |
| SHADOW_DOGE_DONCHIAN_1H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_DOGE_DONCHIAN_1H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,88R | €18,75 |
| SHADOW_DOGE_DONCHIAN_1H | TREND_UP_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_DOGE_EMA_1H | ALT_ROTATION_DOWN | 0 | 11 | 11 | 9,09% | 0,08 | -0,74R | €-81,45 |
| SHADOW_DOGE_EMA_1H | ALT_ROTATION_UP | 0 | 11 | 11 | 18,18% | 0,41 | -0,51R | €-56,27 |
| SHADOW_DOGE_EMA_1H | RANGE | 0 | 13 | 13 | 46,15% | 1,23 | 0,12R | €15,53 |
| SHADOW_DOGE_EMA_1H | RANGE_HIGH_VOL | 0 | 4 | 4 | 100,00% | ∞ | 0,81R | €32,50 |
| SHADOW_DOGE_EMA_1H | TRANSITION | 0 | 2 | 2 | 50,00% | 0,54 | -0,26R | €-5,10 |
| SHADOW_DOGE_EMA_1H | TREND_DOWN | 0 | 3 | 3 | 66,67% | 0,52 | -0,18R | €-5,34 |
| SHADOW_DOGE_EMA_1H | TREND_UP_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_DONCHIAN_1H | ALT_ROTATION_DOWN | 1 | 72 | 72 | 29,17% | 0,55 | -0,31R | €-225,72 |
| SHADOW_DONCHIAN_1H | ALT_ROTATION_UP | 3 | 134 | 134 | 36,57% | 0,82 | -0,12R | €-157,65 |
| SHADOW_DONCHIAN_1H | RANGE | 1 | 109 | 109 | 41,28% | 1,12 | 0,07R | €75,55 |
| SHADOW_DONCHIAN_1H | RANGE_HIGH_VOL | 1 | 16 | 16 | 50,00% | 1,82 | 0,38R | €60,21 |
| SHADOW_DONCHIAN_1H | RANGE_LOW_VOL | 1 | 3 | 3 | 33,33% | 0,58 | -0,29R | €-8,57 |
| SHADOW_DONCHIAN_1H | TRANSITION | 1 | 33 | 33 | 39,39% | 1,29 | 0,15R | €48,35 |
| SHADOW_DONCHIAN_1H | TREND_DOWN | 1 | 22 | 22 | 27,27% | 0,43 | -0,41R | €-89,96 |
| SHADOW_DONCHIAN_1H | TREND_UP | 0 | 43 | 43 | 30,23% | 1,15 | 0,07R | €32,24 |
| SHADOW_DONCHIAN_1H | TREND_UP_HIGH_VOL | 1 | 24 | 24 | 54,17% | 1,90 | 0,44R | €104,71 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | ALT_ROTATION_DOWN | 1 | 62 | 62 | 29,03% | 0,46 | -0,38R | €-234,20 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | ALT_ROTATION_UP | 3 | 126 | 126 | 38,10% | 0,87 | -0,09R | €-107,23 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | RANGE | 1 | 89 | 89 | 43,82% | 1,13 | 0,07R | €60,49 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | RANGE_HIGH_VOL | 1 | 14 | 14 | 57,14% | 2,52 | 0,57R | €80,48 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | RANGE_LOW_VOL | 1 | 2 | 2 | 50,00% | 1,15 | 0,08R | €1,56 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | TRANSITION | 1 | 26 | 26 | 46,15% | 1,68 | 0,30R | €77,62 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | TREND_DOWN | 1 | 20 | 20 | 30,00% | 0,46 | -0,40R | €-79,67 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | TREND_UP | 0 | 29 | 29 | 27,59% | 1,04 | 0,02R | €5,27 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | TREND_UP_HIGH_VOL | 1 | 18 | 18 | 61,11% | 2,36 | 0,56R | €99,93 |
| SHADOW_EMA_TREND_1H | ALT_ROTATION_DOWN | 6 | 114 | 114 | 28,07% | 0,50 | -0,34R | €-390,31 |
| SHADOW_EMA_TREND_1H | ALT_ROTATION_UP | 12 | 248 | 248 | 45,97% | 1,15 | 0,08R | €194,99 |
| SHADOW_EMA_TREND_1H | RANGE | 6 | 194 | 194 | 37,63% | 1,01 | 0,00R | €8,92 |
| SHADOW_EMA_TREND_1H | RANGE_HIGH_VOL | 1 | 46 | 46 | 41,30% | 1,16 | 0,08R | €37,87 |
| SHADOW_EMA_TREND_1H | RANGE_LOW_VOL | 2 | 8 | 8 | 37,50% | 1,00 | -0,00R | €-0,10 |
| SHADOW_EMA_TREND_1H | TRANSITION | 0 | 72 | 72 | 34,72% | 1,04 | 0,02R | €17,55 |
| SHADOW_EMA_TREND_1H | TREND_DOWN | 0 | 69 | 69 | 30,43% | 0,68 | -0,17R | €-115,23 |
| SHADOW_EMA_TREND_1H | TREND_DOWN_HIGH_VOL | 0 | 3 | 3 | 33,33% | 0,51 | -0,34R | €-10,34 |
| SHADOW_EMA_TREND_1H | TREND_UP | 0 | 91 | 91 | 28,57% | 0,83 | -0,10R | €-88,67 |
| SHADOW_EMA_TREND_1H | TREND_UP_HIGH_VOL | 2 | 32 | 32 | 40,62% | 1,21 | 0,12R | €38,66 |
| SHADOW_ETH_ADAPTIVE_1H | ALT_ROTATION_DOWN | 0 | 3 | 3 | 0,00% | 0,00 | -1,10R | €-33,02 |
| SHADOW_ETH_ADAPTIVE_1H | ALT_ROTATION_UP | 0 | 12 | 12 | 33,33% | 0,70 | -0,22R | €-26,02 |
| SHADOW_ETH_ADAPTIVE_1H | RANGE | 0 | 10 | 10 | 30,00% | 0,38 | -0,48R | €-48,41 |
| SHADOW_ETH_ADAPTIVE_1H | RANGE_HIGH_VOL | 0 | 3 | 3 | 33,33% | 0,00 | -0,71R | €-21,28 |
| SHADOW_ETH_ADAPTIVE_1H | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 0,54R | €10,89 |
| SHADOW_ETH_ADAPTIVE_1H | TREND_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 1,89R | €18,89 |
| SHADOW_ETH_ADAPTIVE_1H | TREND_UP | 0 | 3 | 3 | 66,67% | 2,41 | 0,52R | €15,63 |
| SHADOW_ETH_ADAPTIVE_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,10R | €-21,98 |
| SHADOW_ETH_BOLLINGER_1H | ALT_ROTATION_UP | 0 | 10 | 10 | 70,00% | 4,04 | 0,66R | €65,54 |
| SHADOW_ETH_BOLLINGER_1H | RANGE | 0 | 3 | 3 | 66,67% | 1,30 | 0,11R | €3,44 |
| SHADOW_ETH_BOLLINGER_1H | RANGE_HIGH_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,37R | €27,39 |
| SHADOW_ETH_BOLLINGER_1H | TREND_DOWN | 0 | 2 | 2 | 50,00% | 1,21 | 0,12R | €2,33 |
| SHADOW_ETH_BOLLINGER_1H | TREND_UP | 0 | 3 | 3 | 33,33% | 0,21 | -0,60R | €-18,01 |
| SHADOW_ETH_BOLLINGER_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,40R | €13,96 |
| SHADOW_ETH_DONCHIAN_1H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 50,00% | 0,64 | -0,20R | €-3,91 |
| SHADOW_ETH_DONCHIAN_1H | ALT_ROTATION_UP | 0 | 10 | 10 | 30,00% | 0,55 | -0,35R | €-34,58 |
| SHADOW_ETH_DONCHIAN_1H | RANGE | 0 | 9 | 9 | 33,33% | 0,77 | -0,15R | €-13,41 |
| SHADOW_ETH_DONCHIAN_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,12R | €-11,20 |
| SHADOW_ETH_DONCHIAN_1H | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 0,61R | €12,25 |
| SHADOW_ETH_DONCHIAN_1H | TREND_DOWN | 0 | 2 | 2 | 50,00% | 1,67 | 0,37R | €7,50 |
| SHADOW_ETH_DONCHIAN_1H | TREND_UP | 0 | 3 | 3 | 33,33% | 0,39 | -0,46R | €-13,71 |
| SHADOW_ETH_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 33,33% | 0,85 | -0,11R | €-3,34 |
| SHADOW_ETH_EMA_1H | ALT_ROTATION_DOWN | 0 | 4 | 4 | 0,00% | 0,00 | -1,10R | €-43,91 |
| SHADOW_ETH_EMA_1H | ALT_ROTATION_UP | 1 | 20 | 20 | 45,00% | 0,74 | -0,15R | €-29,21 |
| SHADOW_ETH_EMA_1H | RANGE | 0 | 9 | 9 | 33,33% | 0,25 | -0,55R | €-49,78 |
| SHADOW_ETH_EMA_1H | RANGE_HIGH_VOL | 0 | 5 | 5 | 20,00% | 0,43 | -0,49R | €-24,67 |
| SHADOW_ETH_EMA_1H | TRANSITION | 0 | 2 | 2 | 50,00% | 0,45 | -0,30R | €-6,08 |
| SHADOW_ETH_EMA_1H | TREND_DOWN | 0 | 2 | 2 | 50,00% | 0,75 | -0,14R | €-2,73 |
| SHADOW_ETH_EMA_1H | TREND_UP | 0 | 5 | 5 | 40,00% | 0,81 | -0,13R | €-6,46 |
| SHADOW_ETH_EMA_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,09R | €-21,86 |
| SHADOW_ETH_EMA_4H | ALT_ROTATION_UP | 1 | 4 | 4 | 50,00% | 0,64 | -0,19R | €-7,65 |
| SHADOW_ETH_EMA_4H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,72 |
| SHADOW_ETH_EMA_4H | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,04R | €-10,39 |
| SHADOW_ETH_EMA_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,57 |
| SHADOW_ETH_EMA_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,74R | €7,41 |
| SHADOW_GLOBAL_PURE | ALT_ROTATION_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 0,35R | €3,51 |
| SHADOW_GLOBAL_PURE | ALT_ROTATION_UP | 0 | 3 | 3 | 0,00% | 0,00 | -1,10R | €-33,00 |
| SHADOW_GLOBAL_PURE | RANGE | 0 | 10 | 10 | 40,00% | 0,80 | -0,13R | €-13,34 |
| SHADOW_GLOBAL_PURE | RANGE_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,59R | €15,85 |
| SHADOW_GLOBAL_PURE | TRANSITION | 0 | 4 | 4 | 75,00% | 4,43 | 0,94R | €37,75 |
| SHADOW_GLOBAL_PURE | TREND_DOWN | 0 | 2 | 2 | 50,00% | 0,02 | -0,54R | €-10,79 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | ALT_ROTATION_DOWN | 0 | 31 | 31 | 38,71% | 1,27 | 0,16R | €50,15 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | ALT_ROTATION_UP | 9 | 99 | 99 | 39,39% | 1,17 | 0,11R | €109,75 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | RANGE | 4 | 144 | 144 | 29,86% | 0,85 | -0,10R | €-149,95 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | RANGE_LOW_VOL | 1 | 9 | 9 | 33,33% | 0,95 | -0,04R | €-3,18 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TRANSITION | 0 | 46 | 46 | 47,83% | 1,97 | 0,46R | €212,56 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TREND_DOWN | 0 | 50 | 50 | 38,00% | 1,29 | 0,17R | €82,76 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TREND_UP | 0 | 73 | 73 | 28,77% | 0,81 | -0,14R | €-99,16 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | ALT_ROTATION_DOWN | 1 | 49 | 49 | 59,18% | 1,01 | 0,01R | €2,65 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | ALT_ROTATION_UP | 6 | 214 | 214 | 67,76% | 1,29 | 0,09R | €194,50 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | RANGE | 3 | 268 | 268 | 66,04% | 1,26 | 0,08R | €221,24 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | RANGE_LOW_VOL | 1 | 15 | 15 | 80,00% | 1,61 | 0,12R | €18,62 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TRANSITION | 0 | 100 | 100 | 73,00% | 1,75 | 0,18R | €181,85 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TREND_DOWN | 0 | 78 | 78 | 64,10% | 1,36 | 0,12R | €94,03 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TREND_UP | 0 | 134 | 134 | 60,45% | 0,97 | -0,01R | €-15,09 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | ALT_ROTATION_DOWN | 0 | 28 | 28 | 39,29% | 1,40 | 0,22R | €61,61 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | RANGE | 6 | 146 | 146 | 30,82% | 0,89 | -0,08R | €-110,85 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | RANGE_LOW_VOL | 1 | 9 | 9 | 44,44% | 1,51 | 0,29R | €26,16 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TRANSITION | 1 | 46 | 46 | 45,65% | 1,79 | 0,40R | €182,06 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TREND_DOWN | 0 | 45 | 45 | 40,00% | 1,37 | 0,21R | €96,58 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TREND_UP | 0 | 86 | 86 | 25,58% | 0,68 | -0,24R | €-203,14 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_DOWN | 0 | 25 | 25 | 48,00% | 1,99 | 0,49R | €123,26 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_UP | 9 | 100 | 100 | 37,00% | 1,07 | 0,05R | €46,13 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | RANGE | 4 | 129 | 129 | 31,01% | 0,97 | -0,02R | €-21,82 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | RANGE_LOW_VOL | 1 | 8 | 8 | 37,50% | 1,10 | 0,06R | €5,18 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | TRANSITION | 0 | 41 | 41 | 43,90% | 1,70 | 0,36R | €145,68 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | TREND_DOWN | 0 | 42 | 42 | 40,48% | 1,42 | 0,24R | €100,50 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | TREND_UP | 0 | 69 | 69 | 24,64% | 0,67 | -0,24R | €-167,24 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | ALT_ROTATION_DOWN | 0 | 19 | 19 | 26,32% | 0,73 | -0,19R | €-35,51 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | RANGE | 4 | 100 | 100 | 31,00% | 0,86 | -0,10R | €-101,93 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | RANGE_LOW_VOL | 1 | 7 | 7 | 28,57% | 0,75 | -0,19R | €-12,99 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TRANSITION | 0 | 36 | 36 | 47,22% | 2,12 | 0,49R | €176,16 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TREND_DOWN | 0 | 32 | 32 | 25,00% | 0,70 | -0,21R | €-67,12 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TREND_UP | 0 | 62 | 62 | 27,42% | 0,76 | -0,17R | €-107,67 |
| SHADOW_MASTER_ADAPTIVE_V1 | ALT_ROTATION_DOWN | 0 | 28 | 28 | 39,29% | 1,32 | 0,18R | €51,75 |
| SHADOW_MASTER_ADAPTIVE_V1 | ALT_ROTATION_UP | 9 | 101 | 101 | 39,60% | 1,17 | 0,12R | €117,22 |
| SHADOW_MASTER_ADAPTIVE_V1 | RANGE | 4 | 135 | 135 | 31,85% | 0,94 | -0,04R | €-53,96 |
| SHADOW_MASTER_ADAPTIVE_V1 | RANGE_LOW_VOL | 1 | 9 | 9 | 33,33% | 0,95 | -0,04R | €-3,19 |
| SHADOW_MASTER_ADAPTIVE_V1 | TRANSITION | 0 | 45 | 45 | 44,44% | 1,71 | 0,36R | €162,62 |
| SHADOW_MASTER_ADAPTIVE_V1 | TREND_DOWN | 0 | 43 | 43 | 39,53% | 1,35 | 0,20R | €86,84 |
| SHADOW_MASTER_ADAPTIVE_V1 | TREND_UP | 0 | 72 | 72 | 25,00% | 0,67 | -0,25R | €-177,57 |
| Forza relativa 1H V1 | ALT_ROTATION_DOWN | 8 | 132 | 132 | 31,82% | 0,61 | -0,24R | €-318,56 |
| Forza relativa 1H V1 | ALT_ROTATION_UP | 9 | 275 | 275 | 42,91% | 1,08 | 0,05R | €128,80 |
| Forza relativa 1H V1 | RANGE | 8 | 254 | 254 | 33,86% | 0,80 | -0,11R | €-280,42 |
| Forza relativa 1H V1 | RANGE_HIGH_VOL | 2 | 49 | 49 | 28,57% | 0,52 | -0,30R | €-148,31 |
| Forza relativa 1H V1 | RANGE_LOW_VOL | 1 | 11 | 11 | 27,27% | 0,72 | -0,18R | €-19,83 |
| Forza relativa 1H V1 | TRANSITION | 0 | 92 | 92 | 39,13% | 1,34 | 0,17R | €155,94 |
| Forza relativa 1H V1 | TREND_DOWN | 0 | 78 | 78 | 29,49% | 0,95 | -0,02R | €-19,05 |
| Forza relativa 1H V1 | TREND_DOWN_HIGH_VOL | 1 | 3 | 3 | 100,00% | ∞ | 1,66R | €49,91 |
| Forza relativa 1H V1 | TREND_UP | 0 | 111 | 111 | 27,03% | 0,88 | -0,07R | €-74,32 |
| Forza relativa 1H V1 | TREND_UP_HIGH_VOL | 2 | 34 | 34 | 26,47% | 0,77 | -0,15R | €-50,36 |
| Forza relativa 1H V2 | ALT_ROTATION_DOWN | 5 | 62 | 60 | 43,55% | 0,84 | -0,08R | €-50,02 |
| Forza relativa 1H V2 | ALT_ROTATION_UP | 7 | 112 | 102 | 43,75% | 1,17 | 0,10R | €112,85 |
| Forza relativa 1H V2 | RANGE | 7 | 113 | 107 | 31,86% | 0,73 | -0,16R | €-183,75 |
| Forza relativa 1H V2 | RANGE_LOW_VOL | 0 | 8 | 7 | 25,00% | 0,66 | -0,18R | €-14,36 |
| Forza relativa 1H V2 | TRANSITION | 0 | 49 | 44 | 40,82% | 1,54 | 0,25R | €122,15 |
| Forza relativa 1H V2 | TREND_DOWN | 0 | 36 | 35 | 27,78% | 0,89 | -0,05R | €-17,72 |
| Forza relativa 1H V2 | TREND_DOWN_HIGH_VOL | 0 | 6 | 6 | 33,33% | 0,69 | -0,21R | €-12,82 |
| Forza relativa 1H V2 | TREND_UP | 0 | 44 | 39 | 47,73% | 1,77 | 0,34R | €151,54 |
| Forza relativa 1H V2 | TREND_UP_HIGH_VOL | 2 | 10 | 8 | 30,00% | 0,76 | -0,15R | €-14,90 |
| SHADOW_SCANNER_BOTTOM10_SHORT | ALT_ROTATION_DOWN | 4 | 96 | 96 | 22,92% | 0,33 | -0,49R | €-470,21 |
| SHADOW_SCANNER_BOTTOM10_SHORT | ALT_ROTATION_UP | 0 | 18 | 18 | 44,44% | 1,47 | 0,19R | €35,01 |
| SHADOW_SCANNER_BOTTOM10_SHORT | RANGE | 3 | 104 | 104 | 37,50% | 0,70 | -0,14R | €-149,93 |
| SHADOW_SCANNER_BOTTOM10_SHORT | RANGE_HIGH_VOL | 1 | 31 | 31 | 41,94% | 0,91 | -0,04R | €-12,88 |
| SHADOW_SCANNER_BOTTOM10_SHORT | RANGE_LOW_VOL | 1 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,15 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TRANSITION | 0 | 26 | 26 | 42,31% | 1,15 | 0,08R | €21,58 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_DOWN | 0 | 45 | 45 | 26,67% | 0,37 | -0,37R | €-166,77 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_DOWN_HIGH_VOL | 0 | 3 | 3 | 33,33% | 0,31 | -0,51R | €-15,18 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_UP | 0 | 17 | 17 | 5,88% | 0,25 | -0,33R | €-56,36 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_UP_HIGH_VOL | 1 | 3 | 3 | 33,33% | 0,98 | -0,01R | €-0,40 |
| SHADOW_SCANNER_BOTTOM15_SHORT | ALT_ROTATION_DOWN | 4 | 96 | 96 | 22,92% | 0,33 | -0,49R | €-470,21 |
| SHADOW_SCANNER_BOTTOM15_SHORT | ALT_ROTATION_UP | 0 | 18 | 18 | 44,44% | 1,47 | 0,19R | €35,01 |
| SHADOW_SCANNER_BOTTOM15_SHORT | RANGE | 3 | 104 | 104 | 37,50% | 0,70 | -0,14R | €-149,93 |
| SHADOW_SCANNER_BOTTOM15_SHORT | RANGE_HIGH_VOL | 1 | 31 | 31 | 41,94% | 0,91 | -0,04R | €-12,88 |
| SHADOW_SCANNER_BOTTOM15_SHORT | RANGE_LOW_VOL | 1 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,15 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TRANSITION | 0 | 26 | 26 | 42,31% | 1,15 | 0,08R | €21,58 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_DOWN | 0 | 45 | 45 | 26,67% | 0,37 | -0,37R | €-166,77 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_DOWN_HIGH_VOL | 0 | 3 | 3 | 33,33% | 0,31 | -0,51R | €-15,18 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_UP | 0 | 17 | 17 | 5,88% | 0,25 | -0,33R | €-56,36 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_UP_HIGH_VOL | 1 | 3 | 3 | 33,33% | 0,98 | -0,01R | €-0,40 |
| SHADOW_SCANNER_BOTTOM20_SHORT | ALT_ROTATION_DOWN | 4 | 96 | 96 | 22,92% | 0,33 | -0,49R | €-470,21 |
| SHADOW_SCANNER_BOTTOM20_SHORT | ALT_ROTATION_UP | 0 | 18 | 18 | 44,44% | 1,47 | 0,19R | €35,01 |
| SHADOW_SCANNER_BOTTOM20_SHORT | RANGE | 3 | 104 | 104 | 37,50% | 0,70 | -0,14R | €-149,93 |
| SHADOW_SCANNER_BOTTOM20_SHORT | RANGE_HIGH_VOL | 1 | 31 | 31 | 41,94% | 0,91 | -0,04R | €-12,88 |
| SHADOW_SCANNER_BOTTOM20_SHORT | RANGE_LOW_VOL | 1 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,15 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TRANSITION | 0 | 26 | 26 | 42,31% | 1,15 | 0,08R | €21,58 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_DOWN | 0 | 45 | 45 | 26,67% | 0,37 | -0,37R | €-166,77 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_DOWN_HIGH_VOL | 0 | 3 | 3 | 33,33% | 0,31 | -0,51R | €-15,18 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_UP | 0 | 17 | 17 | 5,88% | 0,25 | -0,33R | €-56,36 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_UP_HIGH_VOL | 1 | 3 | 3 | 33,33% | 0,98 | -0,01R | €-0,40 |
| SHADOW_SCANNER_BOTTOM5_SHORT | ALT_ROTATION_DOWN | 4 | 83 | 83 | 24,10% | 0,40 | -0,43R | €-353,10 |
| SHADOW_SCANNER_BOTTOM5_SHORT | ALT_ROTATION_UP | 0 | 19 | 19 | 47,37% | 1,74 | 0,29R | €54,88 |
| SHADOW_SCANNER_BOTTOM5_SHORT | RANGE | 3 | 116 | 116 | 37,93% | 0,88 | -0,06R | €-68,89 |
| SHADOW_SCANNER_BOTTOM5_SHORT | RANGE_HIGH_VOL | 1 | 30 | 30 | 46,67% | 1,14 | 0,06R | €17,21 |
| SHADOW_SCANNER_BOTTOM5_SHORT | RANGE_LOW_VOL | 1 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,15 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TRANSITION | 0 | 42 | 42 | 38,10% | 1,01 | 0,01R | €2,87 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_DOWN | 0 | 41 | 41 | 26,83% | 0,37 | -0,35R | €-144,97 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,62 | -0,21R | €-4,24 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP | 0 | 24 | 24 | 4,17% | 0,15 | -0,45R | €-107,40 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP_HIGH_VOL | 1 | 6 | 6 | 16,67% | 0,48 | -0,36R | €-21,78 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | ALT_ROTATION_DOWN | 4 | 102 | 102 | 44,12% | 0,49 | -0,28R | €-288,70 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | ALT_ROTATION_UP | 0 | 14 | 14 | 50,00% | 1,32 | 0,15R | €20,41 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | RANGE | 3 | 132 | 132 | 62,88% | 0,99 | -0,00R | €-4,42 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | RANGE_HIGH_VOL | 1 | 35 | 35 | 62,86% | 1,17 | 0,07R | €23,75 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | RANGE_LOW_VOL | 1 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,26 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TRANSITION | 0 | 33 | 33 | 57,58% | 1,30 | 0,13R | €44,05 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_DOWN | 0 | 68 | 68 | 52,94% | 0,63 | -0,16R | €-108,67 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_DOWN_HIGH_VOL | 0 | 4 | 4 | 50,00% | 0,62 | -0,21R | €-8,36 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_UP | 0 | 20 | 20 | 40,00% | 0,58 | -0,20R | €-40,01 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_UP_HIGH_VOL | 1 | 3 | 3 | 33,33% | 0,09 | -0,61R | €-18,40 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | ALT_ROTATION_DOWN | 4 | 83 | 83 | 39,76% | 0,37 | -0,37R | €-307,11 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | ALT_ROTATION_UP | 0 | 17 | 17 | 52,94% | 1,61 | 0,23R | €38,54 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | RANGE | 3 | 120 | 120 | 64,17% | 0,92 | -0,03R | €-33,92 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | RANGE_HIGH_VOL | 1 | 34 | 34 | 58,82% | 0,96 | -0,02R | €-6,50 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | RANGE_LOW_VOL | 1 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,26 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TRANSITION | 0 | 32 | 32 | 59,38% | 1,50 | 0,21R | €67,96 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_DOWN | 0 | 57 | 57 | 50,88% | 0,60 | -0,18R | €-103,46 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_DOWN_HIGH_VOL | 0 | 4 | 4 | 50,00% | 0,37 | -0,35R | €-14,07 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_UP | 0 | 19 | 19 | 36,84% | 0,30 | -0,35R | €-66,17 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_UP_HIGH_VOL | 1 | 3 | 3 | 33,33% | 0,09 | -0,61R | €-18,40 |
| SHADOW_SCANNER_TOP10_LONG | ALT_ROTATION_DOWN | 1 | 44 | 44 | 36,36% | 0,88 | -0,07R | €-29,49 |
| SHADOW_SCANNER_TOP10_LONG | ALT_ROTATION_UP | 9 | 285 | 285 | 44,91% | 1,02 | 0,01R | €34,88 |
| SHADOW_SCANNER_TOP10_LONG | RANGE | 4 | 126 | 126 | 45,24% | 0,98 | -0,01R | €-11,25 |
| SHADOW_SCANNER_TOP10_LONG | RANGE_HIGH_VOL | 0 | 25 | 25 | 28,00% | 0,56 | -0,29R | €-71,85 |
| SHADOW_SCANNER_TOP10_LONG | RANGE_LOW_VOL | 1 | 10 | 10 | 30,00% | 0,95 | -0,03R | €-3,27 |
| SHADOW_SCANNER_TOP10_LONG | TRANSITION | 0 | 57 | 57 | 40,35% | 1,36 | 0,14R | €78,21 |
| SHADOW_SCANNER_TOP10_LONG | TREND_DOWN | 0 | 46 | 46 | 30,43% | 1,02 | 0,01R | €5,92 |
| SHADOW_SCANNER_TOP10_LONG | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,95 | 0,48R | €9,58 |
| SHADOW_SCANNER_TOP10_LONG | TREND_UP | 0 | 66 | 66 | 30,30% | 0,66 | -0,17R | €-111,00 |
| SHADOW_SCANNER_TOP10_LONG | TREND_UP_HIGH_VOL | 3 | 27 | 27 | 55,56% | 2,01 | 0,36R | €97,30 |
| SHADOW_SCANNER_TOP15_LONG | ALT_ROTATION_DOWN | 1 | 44 | 44 | 36,36% | 0,88 | -0,07R | €-29,43 |
| SHADOW_SCANNER_TOP15_LONG | ALT_ROTATION_UP | 9 | 290 | 290 | 45,52% | 1,03 | 0,02R | €48,07 |
| SHADOW_SCANNER_TOP15_LONG | RANGE | 4 | 126 | 126 | 45,24% | 0,98 | -0,01R | €-11,25 |
| SHADOW_SCANNER_TOP15_LONG | RANGE_HIGH_VOL | 0 | 25 | 25 | 28,00% | 0,56 | -0,29R | €-71,85 |
| SHADOW_SCANNER_TOP15_LONG | RANGE_LOW_VOL | 1 | 10 | 10 | 30,00% | 0,95 | -0,03R | €-3,27 |
| SHADOW_SCANNER_TOP15_LONG | TRANSITION | 0 | 57 | 57 | 40,35% | 1,36 | 0,14R | €78,21 |
| SHADOW_SCANNER_TOP15_LONG | TREND_DOWN | 0 | 46 | 46 | 30,43% | 1,02 | 0,01R | €5,92 |
| SHADOW_SCANNER_TOP15_LONG | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,95 | 0,48R | €9,58 |
| SHADOW_SCANNER_TOP15_LONG | TREND_UP | 0 | 66 | 66 | 30,30% | 0,66 | -0,17R | €-111,00 |
| SHADOW_SCANNER_TOP15_LONG | TREND_UP_HIGH_VOL | 3 | 25 | 25 | 52,00% | 1,93 | 0,36R | €90,06 |
| SHADOW_SCANNER_TOP20_LONG | ALT_ROTATION_DOWN | 1 | 44 | 44 | 36,36% | 0,88 | -0,07R | €-29,43 |
| SHADOW_SCANNER_TOP20_LONG | ALT_ROTATION_UP | 9 | 290 | 290 | 45,52% | 1,03 | 0,02R | €48,07 |
| SHADOW_SCANNER_TOP20_LONG | RANGE | 4 | 126 | 126 | 45,24% | 0,98 | -0,01R | €-11,25 |
| SHADOW_SCANNER_TOP20_LONG | RANGE_HIGH_VOL | 0 | 25 | 25 | 28,00% | 0,56 | -0,29R | €-71,85 |
| SHADOW_SCANNER_TOP20_LONG | RANGE_LOW_VOL | 1 | 10 | 10 | 30,00% | 0,95 | -0,03R | €-3,27 |
| SHADOW_SCANNER_TOP20_LONG | TRANSITION | 0 | 57 | 57 | 40,35% | 1,36 | 0,14R | €78,21 |
| SHADOW_SCANNER_TOP20_LONG | TREND_DOWN | 0 | 46 | 46 | 30,43% | 1,02 | 0,01R | €5,92 |
| SHADOW_SCANNER_TOP20_LONG | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,95 | 0,48R | €9,58 |
| SHADOW_SCANNER_TOP20_LONG | TREND_UP | 0 | 66 | 66 | 30,30% | 0,66 | -0,17R | €-111,00 |
| SHADOW_SCANNER_TOP20_LONG | TREND_UP_HIGH_VOL | 3 | 25 | 25 | 52,00% | 1,93 | 0,36R | €90,06 |
| SHADOW_SCANNER_TOP5_BTC | ALT_ROTATION_DOWN | 2 | 46 | 46 | 28,26% | 0,55 | -0,29R | €-134,71 |
| SHADOW_SCANNER_TOP5_BTC | ALT_ROTATION_UP | 9 | 216 | 216 | 44,44% | 1,11 | 0,06R | €124,70 |
| SHADOW_SCANNER_TOP5_BTC | RANGE | 4 | 134 | 134 | 44,03% | 1,10 | 0,05R | €70,86 |
| SHADOW_SCANNER_TOP5_BTC | RANGE_HIGH_VOL | 0 | 22 | 22 | 31,82% | 0,48 | -0,32R | €-71,39 |
| SHADOW_SCANNER_TOP5_BTC | RANGE_LOW_VOL | 1 | 10 | 10 | 30,00% | 0,84 | -0,10R | €-9,67 |
| SHADOW_SCANNER_TOP5_BTC | TRANSITION | 0 | 67 | 67 | 41,79% | 1,48 | 0,22R | €145,48 |
| SHADOW_SCANNER_TOP5_BTC | TREND_DOWN | 0 | 44 | 44 | 29,55% | 0,82 | -0,10R | €-45,52 |
| SHADOW_SCANNER_TOP5_BTC | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 2,14 | 0,58R | €11,58 |
| SHADOW_SCANNER_TOP5_BTC | TREND_UP | 0 | 74 | 74 | 32,43% | 1,03 | 0,02R | €11,21 |
| SHADOW_SCANNER_TOP5_BTC | TREND_UP_HIGH_VOL | 2 | 26 | 26 | 38,46% | 1,14 | 0,08R | €19,78 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | ALT_ROTATION_DOWN | 1 | 18 | 18 | 11,11% | 0,18 | -0,67R | €-119,88 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | ALT_ROTATION_UP | 5 | 94 | 94 | 37,23% | 0,61 | -0,26R | €-244,21 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | RANGE | 1 | 12 | 12 | 41,67% | 0,44 | -0,35R | €-41,60 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | RANGE_HIGH_VOL | 0 | 4 | 4 | 25,00% | 0,27 | -0,58R | €-23,05 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TRANSITION | 0 | 30 | 30 | 53,33% | 2,17 | 0,40R | €120,24 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TREND_UP | 0 | 58 | 58 | 29,31% | 0,86 | -0,07R | €-42,83 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TREND_UP_HIGH_VOL | 0 | 14 | 14 | 14,29% | 0,24 | -0,58R | €-80,67 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | ALT_ROTATION_DOWN | 1 | 40 | 40 | 27,50% | 0,53 | -0,30R | €-120,90 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | ALT_ROTATION_UP | 5 | 121 | 121 | 38,84% | 0,74 | -0,16R | €-190,35 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | RANGE | 5 | 130 | 130 | 43,08% | 1,01 | 0,00R | €5,12 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | RANGE_HIGH_VOL | 0 | 21 | 21 | 33,33% | 0,52 | -0,29R | €-60,69 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | RANGE_LOW_VOL | 1 | 10 | 10 | 30,00% | 0,84 | -0,10R | €-9,67 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TRANSITION | 0 | 51 | 51 | 47,06% | 2,10 | 0,38R | €193,93 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_DOWN | 0 | 44 | 44 | 29,55% | 0,82 | -0,10R | €-45,52 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 2,14 | 0,58R | €11,58 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_UP | 0 | 52 | 52 | 23,08% | 0,59 | -0,24R | €-122,50 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_UP_HIGH_VOL | 0 | 14 | 14 | 14,29% | 0,24 | -0,58R | €-80,67 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | ALT_ROTATION_DOWN | 1 | 37 | 37 | 32,43% | 0,69 | -0,14R | €-50,92 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | ALT_ROTATION_UP | 3 | 125 | 125 | 43,20% | 0,92 | -0,04R | €-46,75 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | RANGE | 5 | 156 | 156 | 43,59% | 1,08 | 0,04R | €58,79 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | RANGE_HIGH_VOL | 0 | 33 | 33 | 33,33% | 0,61 | -0,18R | €-60,32 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | RANGE_LOW_VOL | 1 | 12 | 12 | 33,33% | 0,56 | -0,26R | €-31,74 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TRANSITION | 0 | 51 | 51 | 47,06% | 1,28 | 0,11R | €54,83 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_DOWN | 0 | 51 | 51 | 47,06% | 0,98 | -0,01R | €-5,20 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 2,14 | 0,58R | €11,58 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_UP | 0 | 53 | 53 | 50,94% | 1,34 | 0,14R | €72,98 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 7 | 7 | 57,14% | 1,17 | 0,07R | €5,17 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | ALT_ROTATION_DOWN | 1 | 30 | 30 | 33,33% | 0,62 | -0,22R | €-67,08 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | ALT_ROTATION_UP | 4 | 100 | 100 | 42,00% | 0,87 | -0,08R | €-76,05 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | RANGE | 5 | 134 | 134 | 44,03% | 1,04 | 0,02R | €24,81 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | RANGE_HIGH_VOL | 0 | 25 | 25 | 32,00% | 0,44 | -0,35R | €-88,53 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | RANGE_LOW_VOL | 1 | 10 | 10 | 30,00% | 0,84 | -0,10R | €-9,67 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TRANSITION | 0 | 46 | 46 | 39,13% | 1,52 | 0,21R | €97,22 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_DOWN | 0 | 40 | 40 | 30,00% | 0,76 | -0,14R | €-57,22 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 2,14 | 0,58R | €11,58 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_UP | 0 | 41 | 41 | 26,83% | 0,78 | -0,12R | €-47,64 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_UP_HIGH_VOL | 0 | 8 | 8 | 12,50% | 0,42 | -0,37R | €-29,56 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | ALT_ROTATION_DOWN | 1 | 45 | 45 | 37,78% | 0,83 | -0,08R | €-35,16 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | ALT_ROTATION_UP | 7 | 228 | 228 | 45,18% | 1,09 | 0,04R | €95,13 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | RANGE | 4 | 157 | 157 | 43,95% | 1,10 | 0,05R | €71,67 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | RANGE_HIGH_VOL | 0 | 33 | 33 | 33,33% | 0,61 | -0,18R | €-60,32 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | RANGE_LOW_VOL | 1 | 12 | 12 | 33,33% | 0,56 | -0,26R | €-31,74 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TRANSITION | 0 | 57 | 57 | 43,86% | 1,25 | 0,09R | €51,57 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_DOWN | 0 | 51 | 51 | 47,06% | 0,98 | -0,01R | €-5,20 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 2,14 | 0,58R | €11,58 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_UP | 0 | 62 | 62 | 50,00% | 1,32 | 0,13R | €80,27 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_UP_HIGH_VOL | 3 | 22 | 22 | 59,09% | 1,65 | 0,22R | €47,66 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | ALT_ROTATION_DOWN | 2 | 36 | 36 | 33,33% | 0,67 | -0,20R | €-71,20 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | ALT_ROTATION_UP | 8 | 185 | 185 | 47,57% | 1,26 | 0,13R | €248,95 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | RANGE | 4 | 133 | 133 | 44,36% | 1,05 | 0,03R | €37,33 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | RANGE_HIGH_VOL | 0 | 25 | 25 | 32,00% | 0,44 | -0,35R | €-88,53 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | RANGE_LOW_VOL | 1 | 10 | 10 | 30,00% | 0,84 | -0,10R | €-9,67 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TRANSITION | 0 | 51 | 51 | 39,22% | 1,34 | 0,15R | €73,97 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_DOWN | 0 | 40 | 40 | 30,00% | 0,76 | -0,14R | €-57,22 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 2,14 | 0,58R | €11,58 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_UP | 0 | 48 | 48 | 27,08% | 0,81 | -0,10R | €-48,83 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_UP_HIGH_VOL | 2 | 15 | 15 | 33,33% | 1,05 | 0,03R | €4,41 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | ALT_ROTATION_DOWN | 1 | 56 | 56 | 35,71% | 0,70 | -0,14R | €-78,18 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | ALT_ROTATION_UP | 8 | 259 | 259 | 43,24% | 0,97 | -0,02R | €-41,43 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | RANGE | 4 | 148 | 148 | 44,59% | 1,11 | 0,05R | €73,98 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | RANGE_HIGH_VOL | 0 | 30 | 30 | 30,00% | 0,45 | -0,26R | €-78,43 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | RANGE_LOW_VOL | 1 | 12 | 12 | 33,33% | 0,56 | -0,26R | €-31,74 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TRANSITION | 0 | 65 | 65 | 44,62% | 1,28 | 0,10R | €67,21 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_DOWN | 0 | 58 | 58 | 44,83% | 1,01 | 0,00R | €1,84 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 2,14 | 0,58R | €11,58 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_UP | 0 | 76 | 76 | 50,00% | 1,29 | 0,11R | €81,78 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_UP_HIGH_VOL | 4 | 33 | 33 | 48,48% | 1,17 | 0,07R | €24,36 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | ALT_ROTATION_DOWN | 2 | 39 | 39 | 33,33% | 0,67 | -0,21R | €-80,85 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | ALT_ROTATION_UP | 9 | 217 | 217 | 43,78% | 1,09 | 0,05R | €110,27 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | RANGE | 4 | 125 | 125 | 42,40% | 1,04 | 0,02R | €25,66 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | RANGE_HIGH_VOL | 0 | 21 | 21 | 33,33% | 0,52 | -0,29R | €-61,69 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | RANGE_LOW_VOL | 1 | 9 | 9 | 33,33% | 0,99 | -0,01R | €-0,54 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TRANSITION | 0 | 55 | 55 | 40,00% | 1,41 | 0,18R | €99,29 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_DOWN | 0 | 43 | 43 | 30,23% | 0,87 | -0,07R | €-31,88 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 2,08 | 0,55R | €10,95 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_UP | 0 | 57 | 57 | 26,32% | 0,69 | -0,16R | €-91,38 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_UP_HIGH_VOL | 2 | 20 | 20 | 35,00% | 0,80 | -0,12R | €-23,47 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | ALT_ROTATION_DOWN | 2 | 37 | 37 | 32,43% | 0,69 | -0,20R | €-72,22 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | ALT_ROTATION_UP | 9 | 208 | 208 | 42,31% | 1,08 | 0,05R | €93,95 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | RANGE | 4 | 119 | 119 | 42,02% | 1,06 | 0,03R | €41,18 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | RANGE_HIGH_VOL | 0 | 21 | 21 | 33,33% | 0,54 | -0,28R | €-58,63 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | RANGE_LOW_VOL | 1 | 9 | 9 | 33,33% | 0,68 | -0,18R | €-16,36 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TRANSITION | 0 | 49 | 49 | 38,78% | 1,59 | 0,24R | €116,44 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_DOWN | 0 | 40 | 40 | 30,00% | 0,93 | -0,04R | €-14,25 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,23 | 0,12R | €2,31 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_UP | 0 | 56 | 56 | 28,57% | 0,75 | -0,13R | €-70,39 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_UP_HIGH_VOL | 2 | 19 | 19 | 42,11% | 1,11 | 0,05R | €10,13 |
| SHADOW_SCANNER_TOP5_LONG | ALT_ROTATION_DOWN | 1 | 53 | 53 | 32,08% | 0,69 | -0,18R | €-97,82 |
| SHADOW_SCANNER_TOP5_LONG | ALT_ROTATION_UP | 8 | 226 | 226 | 44,25% | 1,02 | 0,01R | €24,63 |
| SHADOW_SCANNER_TOP5_LONG | RANGE | 4 | 141 | 141 | 44,68% | 1,06 | 0,03R | €42,81 |
| SHADOW_SCANNER_TOP5_LONG | RANGE_HIGH_VOL | 0 | 27 | 27 | 25,93% | 0,49 | -0,34R | €-92,68 |
| SHADOW_SCANNER_TOP5_LONG | RANGE_LOW_VOL | 1 | 10 | 10 | 30,00% | 0,95 | -0,03R | €-3,27 |
| SHADOW_SCANNER_TOP5_LONG | TRANSITION | 0 | 70 | 70 | 41,43% | 1,43 | 0,18R | €124,25 |
| SHADOW_SCANNER_TOP5_LONG | TREND_DOWN | 0 | 46 | 46 | 30,43% | 1,02 | 0,01R | €5,92 |
| SHADOW_SCANNER_TOP5_LONG | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,95 | 0,48R | €9,58 |
| SHADOW_SCANNER_TOP5_LONG | TREND_UP | 0 | 95 | 95 | 38,95% | 1,16 | 0,07R | €69,95 |
| SHADOW_SCANNER_TOP5_LONG | TREND_UP_HIGH_VOL | 3 | 31 | 31 | 48,39% | 1,74 | 0,31R | €96,33 |
| SHADOW_SOL_ADAPTIVE_1H | ALT_ROTATION_DOWN | 0 | 9 | 9 | 11,11% | 0,10 | -0,84R | €-75,50 |
| SHADOW_SOL_ADAPTIVE_1H | ALT_ROTATION_UP | 0 | 17 | 17 | 64,71% | 2,63 | 0,63R | €106,34 |
| SHADOW_SOL_ADAPTIVE_1H | RANGE | 0 | 11 | 11 | 54,55% | 1,00 | -0,00R | €-0,06 |
| SHADOW_SOL_ADAPTIVE_1H | RANGE_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,09R | €-21,82 |
| SHADOW_SOL_ADAPTIVE_1H | TRANSITION | 0 | 3 | 3 | 33,33% | 0,86 | -0,10R | €-3,05 |
| SHADOW_SOL_ADAPTIVE_1H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_SOL_ADAPTIVE_1H | TREND_UP | 0 | 2 | 2 | 50,00% | 1,11 | 0,06R | €1,19 |
| SHADOW_SOL_ADAPTIVE_1H | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 33,33% | 0,87 | -0,10R | €-2,88 |
| SHADOW_SOL_ADAPTIVE_4H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 100,00% | ∞ | 1,70R | €33,99 |
| SHADOW_SOL_ADAPTIVE_4H | ALT_ROTATION_UP | 0 | 5 | 5 | 80,00% | 4,51 | 0,73R | €36,46 |
| SHADOW_SOL_ADAPTIVE_4H | RANGE | 0 | 1 | 1 | 100,00% | ∞ | 1,25R | €12,45 |
| SHADOW_SOL_ADAPTIVE_4H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,81 |
| SHADOW_SOL_ADAPTIVE_4H | TREND_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,77 |
| SHADOW_SOL_ADAPTIVE_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,05R | €-10,53 |
| SHADOW_SOL_BOLLINGER_1H | ALT_ROTATION_DOWN | 0 | 7 | 7 | 71,43% | 1,78 | 0,24R | €17,02 |
| SHADOW_SOL_BOLLINGER_1H | ALT_ROTATION_UP | 0 | 14 | 14 | 28,57% | 0,29 | -0,55R | €-77,66 |
| SHADOW_SOL_BOLLINGER_1H | RANGE | 0 | 8 | 8 | 37,50% | 0,53 | -0,33R | €-26,28 |
| SHADOW_SOL_BOLLINGER_1H | RANGE_HIGH_VOL | 0 | 2 | 2 | 50,00% | 11,45 | 0,62R | €12,47 |
| SHADOW_SOL_BOLLINGER_1H | TREND_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 1,37R | €13,67 |
| SHADOW_SOL_BOLLINGER_1H | TREND_UP | 0 | 2 | 2 | 50,00% | 0,71 | -0,16R | €-3,29 |
| SHADOW_SOL_BOLLINGER_4H | ALT_ROTATION_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,03R | €-10,28 |
| SHADOW_SOL_BOLLINGER_4H | ALT_ROTATION_UP | 0 | 4 | 4 | 25,00% | 0,33 | -0,53R | €-21,15 |
| SHADOW_SOL_BOLLINGER_4H | RANGE | 0 | 1 | 1 | 100,00% | ∞ | 0,66R | €6,63 |
| SHADOW_SOL_BOLLINGER_4H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,74R | €17,38 |
| SHADOW_SOL_BOLLINGER_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,74R | €17,36 |
| SHADOW_SOL_DONCHIAN_1H | ALT_ROTATION_DOWN | 0 | 7 | 7 | 28,57% | 0,26 | -0,59R | €-41,10 |
| SHADOW_SOL_DONCHIAN_1H | ALT_ROTATION_UP | 0 | 14 | 14 | 64,29% | 2,48 | 0,47R | €66,37 |
| SHADOW_SOL_DONCHIAN_1H | RANGE | 0 | 10 | 10 | 70,00% | 2,18 | 0,40R | €39,82 |
| SHADOW_SOL_DONCHIAN_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_SOL_DONCHIAN_1H | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,94 |
| SHADOW_SOL_DONCHIAN_1H | TREND_DOWN | 0 | 2 | 2 | 50,00% | 0,10 | -0,51R | €-10,17 |
| SHADOW_SOL_DONCHIAN_1H | TREND_UP | 0 | 2 | 2 | 50,00% | 1,67 | 0,38R | €7,50 |
| SHADOW_SOL_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,72 | 0,40R | €8,01 |
| SHADOW_SOL_DONCHIAN_4H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 50,00% | 2,62 | 0,84R | €16,82 |
| SHADOW_SOL_DONCHIAN_4H | ALT_ROTATION_UP | 1 | 3 | 3 | 33,33% | 0,60 | -0,28R | €-8,29 |
| SHADOW_SOL_DONCHIAN_4H | RANGE | 0 | 1 | 1 | 100,00% | ∞ | 1,36R | €13,58 |
| SHADOW_SOL_DONCHIAN_4H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,88 |
| SHADOW_SOL_DONCHIAN_4H | TREND_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,85 |
| SHADOW_SOL_DONCHIAN_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,58 |
| SHADOW_SOL_EMA_1H | ALT_ROTATION_DOWN | 0 | 9 | 9 | 11,11% | 0,08 | -0,85R | €-76,70 |
| SHADOW_SOL_EMA_1H | ALT_ROTATION_UP | 0 | 17 | 17 | 64,71% | 2,63 | 0,63R | €106,41 |
| SHADOW_SOL_EMA_1H | RANGE | 0 | 11 | 11 | 36,36% | 0,78 | -0,16R | €-17,14 |
| SHADOW_SOL_EMA_1H | RANGE_HIGH_VOL | 0 | 3 | 3 | 33,33% | 0,87 | -0,09R | €-2,82 |
| SHADOW_SOL_EMA_1H | TRANSITION | 0 | 3 | 3 | 33,33% | 0,85 | -0,11R | €-3,29 |
| SHADOW_SOL_EMA_1H | TREND_DOWN | 0 | 2 | 2 | 0,00% | 0,00 | -1,11R | €-22,22 |
| SHADOW_SOL_EMA_1H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,23R | €12,30 |
| SHADOW_SOL_EMA_1H | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 33,33% | 0,87 | -0,10R | €-2,88 |
| SHADOW_SOL_EMA_4H | ALT_ROTATION_DOWN | 0 | 4 | 4 | 50,00% | 1,65 | 0,34R | €13,75 |
| SHADOW_SOL_EMA_4H | ALT_ROTATION_UP | 0 | 5 | 5 | 60,00% | 1,56 | 0,23R | €11,68 |
| SHADOW_SOL_EMA_4H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,88 |
| SHADOW_SOL_EMA_4H | TREND_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,84 |
| SHADOW_SOL_EMA_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,58 |

Il P&L è normalizzato a **€10 di rischio per evento**, così leva e size non falsano il confronto.
La matrice diventerà utilizzabile per una rotazione automatica soltanto dopo un campione sufficiente per ciascuna coppia strategia-regime.

# Block 3 — Shadow Exit Engine

Generato: 2026-09-21T19:07:09+00:00

> Motore esclusivamente osservativo e Paper-only. Non modifica le uscite reali. I confronti escludono il funding sia dall'uscita originale sia dalle varianti.

## Stato operativo

- Gruppi di trade ancora monitorati: **305**
- Scenari virtuali ancora attivi: **9737**
- Gruppi in attesa dell'uscita originale: **177**
- Gruppi con originale chiuso ma Shadow ancora attive: **128**
- Confronti completati: **683123**

## Classifica osservativa complessiva

| Scenario | Campione completo | Campione totale | Δ medio vs originale | Migliora | Troppo presto | Troppo tardi | Stato dati |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| ATR10_R050 | 0 | 0 | €0,00 | 0,0% | 0 | 0 | WAITING_FULL_SAMPLE |
| ATR15_R050 | 0 | 0 | €0,00 | 0,0% | 0 | 0 | WAITING_FULL_SAMPLE |
| ATR15_R100 | 0 | 0 | €0,00 | 0,0% | 0 | 0 | WAITING_FULL_SAMPLE |
| ATR20_R050 | 0 | 0 | €0,00 | 0,0% | 0 | 0 | WAITING_FULL_SAMPLE |
| ATR20_R100 | 0 | 0 | €0,00 | 0,0% | 0 | 0 | WAITING_FULL_SAMPLE |
| ATR30_R100 | 0 | 0 | €0,00 | 0,0% | 0 | 0 | WAITING_FULL_SAMPLE |
| BE_A020 | 0 | 0 | €0,00 | 0,0% | 0 | 0 | WAITING_FULL_SAMPLE |
| BE_A030 | 0 | 0 | €0,00 | 0,0% | 0 | 0 | WAITING_FULL_SAMPLE |
| BE_A040 | 0 | 0 | €0,00 | 0,0% | 0 | 0 | WAITING_FULL_SAMPLE |
| BE_A050 | 0 | 0 | €0,00 | 0,0% | 0 | 0 | WAITING_FULL_SAMPLE |
| BE_A060 | 0 | 0 | €0,00 | 0,0% | 0 | 0 | WAITING_FULL_SAMPLE |
| BE_A075 | 0 | 0 | €0,00 | 0,0% | 0 | 0 | WAITING_FULL_SAMPLE |
| BE_A100 | 0 | 0 | €0,00 | 0,0% | 0 | 0 | WAITING_FULL_SAMPLE |
| BE_A125 | 0 | 0 | €0,00 | 0,0% | 0 | 0 | WAITING_FULL_SAMPLE |
| BE_R020_BALANCED_LONG | 0 | 0 | €0,00 | 0,0% | 0 | 0 | WAITING_FULL_SAMPLE |
| BE_R040 | 0 | 0 | €0,00 | 0,0% | 0 | 0 | WAITING_FULL_SAMPLE |
| BE_R050 | 0 | 0 | €0,00 | 0,0% | 0 | 0 | WAITING_FULL_SAMPLE |
| BE_R075 | 0 | 0 | €0,00 | 0,0% | 0 | 0 | WAITING_FULL_SAMPLE |
| BE_R100 | 0 | 0 | €0,00 | 0,0% | 0 | 0 | WAITING_FULL_SAMPLE |
| CH_MBV3_GB20_R100 | 0 | 0 | €0,00 | 0,0% | 0 | 0 | WAITING_FULL_SAMPLE |

## Come leggere il controllo

- **EARLIER_BETTER**: la variante è uscita prima e ha conservato più profitto.
- **TOO_EARLY**: la variante è uscita prima ma ha tagliato un movimento migliore.
- **LATER_BETTER**: la variante ha continuato dopo l'uscita originale e ha guadagnato di più.
- **TOO_LATE**: la variante è rimasta aperta più a lungo e ha peggiorato il risultato.

## Limiti e protezioni

Le regole Shadow mantengono entrata, quantità, commissioni, stop protettivo iniziale e liquidazione. Le ambiguità all'interno della stessa candela vengono risolte scegliendo l'esito peggiore. Le posizioni già aperte al momento dell'installazione sono marcate come campione parziale e non saranno utilizzate dal futuro Blocco 4 come prova piena.

# Blocco 4 — Valutazione statistica Shadow

Generato: 2026-09-21T19:08:13+00:00

> Modulo esclusivamente valutativo. Non modifica strategie, uscite, posizioni o capitale. Le candidature vengono consegnate al futuro Blocco 5, senza applicazione automatica.

## Stato

- Risultati Block 3 disponibili: **683123**
- Valutazioni prodotte: **29856**
- Candidature al Blocco 5: **15**
- Mutazioni create automaticamente: **0**

## Classifica complessiva

| Scenario | Campione pieno | Δ medio (R) | Mediana (R) | CI bootstrap basso | Migliora | Score | Stato |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| GB20_R050 | 41 | 3,520 | 4,831 | 2,865 | 85,4% | 87,5 | EARLY_SIGNAL |
| GB30_R050 | 41 | 3,496 | 4,818 | 2,778 | 85,4% | 87,5 | EARLY_SIGNAL |
| GB20_R075 | 41 | 3,451 | 4,831 | 2,743 | 85,4% | 87,5 | EARLY_SIGNAL |
| GB30_R075 | 41 | 3,429 | 4,818 | 2,683 | 85,4% | 87,5 | EARLY_SIGNAL |
| GB40_R050 | 41 | 3,392 | 4,678 | 2,694 | 85,4% | 87,5 | EARLY_SIGNAL |
| GB40_R075 | 41 | 3,328 | 4,678 | 2,680 | 85,4% | 87,5 | EARLY_SIGNAL |
| GB50_R050 | 41 | 3,280 | 4,538 | 2,626 | 85,4% | 87,5 | EARLY_SIGNAL |
| GB50_R075 | 41 | 3,219 | 4,538 | 2,439 | 85,4% | 87,5 | EARLY_SIGNAL |
| ATR15_R050 | 41 | 2,910 | 4,115 | 2,282 | 85,4% | 87,5 | EARLY_SIGNAL |
| GB30_R100 | 41 | 3,324 | 4,818 | 2,482 | 85,4% | 87,5 | EARLY_SIGNAL |
| TP_R075 | 41 | 3,293 | 4,587 | 2,616 | 85,4% | 87,5 | EARLY_SIGNAL |
| ATR10_R050 | 41 | 3,269 | 4,641 | 2,577 | 85,4% | 87,5 | EARLY_SIGNAL |
| GB40_R100 | 41 | 3,221 | 4,678 | 2,481 | 85,4% | 87,5 | EARLY_SIGNAL |
| TP_R060 | 41 | 3,169 | 4,437 | 2,482 | 85,4% | 87,5 | EARLY_SIGNAL |
| TP_R050 | 41 | 3,159 | 4,337 | 2,558 | 85,4% | 87,5 | EARLY_SIGNAL |
| GB50_R100 | 41 | 3,117 | 4,538 | 2,303 | 85,4% | 87,5 | EARLY_SIGNAL |
| TP_R040 | 41 | 3,071 | 4,238 | 2,505 | 85,4% | 87,5 | EARLY_SIGNAL |
| TP_R035 | 41 | 3,027 | 4,188 | 2,449 | 85,4% | 87,5 | EARLY_SIGNAL |
| GB20_R100 | 41 | 3,340 | 4,831 | 2,630 | 85,4% | 87,5 | EARLY_SIGNAL |
| ATR15_R100 | 41 | 2,788 | 4,115 | 2,074 | 85,4% | 87,5 | EARLY_SIGNAL |

## Stati di evidenza

- **INSUFFICIENT_DATA**: meno di 30 trade completi.
- **EARLY_SIGNAL**: da 30 a 49 trade completi.
- **VALIDATING**: campione maggiore, ma robustezza non ancora dimostrata.
- **ROBUST**: test di effetto, stabilità, qualità e outlier superati.
- **ELIGIBLE_FOR_MUTATION**: evidenza sufficiente per proporre una variante al Blocco 5.
- **UNDERPERFORMING**: intervallo statistico stabilmente negativo.

## Protezioni statistiche

Sono utilizzati solo trade osservati integralmente dall'entrata. Il controllo comprende media e mediana normalizzate per rischio, media tagliata, bootstrap deterministico, quattro segmenti temporali, concentrazione dei migliori outlier, ambiguità intrabar e gap di candele.

🏆 CHALLENGER CANDIDATE
Aggiornamento aggregazione UTC: 2026-09-21T19:10:55+00:00
Mother canonica simulata: stessi ingressi, osservazioni ed execution del challenger.
PnL al netto delle fee modellate, funding escluso da entrambi; FX congelato all'ingresso.
Osservazioni MARK discrete: nessuna certificazione del percorso intrabar tra quotazioni.
Ranking promozionale: INSUFFICIENT_CERTIFIED_DATA

Rapida 1H V1 — giveback 20% dopo +0,5R
CERTIFIED_POST_FIX · NOT_CERTIFIED
Certified pairs: 0 · Legacy/pre-fix: 22 (peso 0)
Promotional weight: 0 · INSUFFICIENT_CERTIFIED_DATA
Cutoff UTC: 2026-09-11T09:26:25.603672+00:00
First/last certified: N/D / N/D
PF N/D · PnL ex funding N/D € · Exp N/D €
Mother PF N/D · PnL N/D €
ΔPF N/D · ΔPnL N/D €
Causality: NOT_CERTIFIED

Rapida 1H V1 — giveback 30% dopo +0,5R
CERTIFIED_POST_FIX · NOT_CERTIFIED
Certified pairs: 0 · Legacy/pre-fix: 22 (peso 0)
Promotional weight: 0 · INSUFFICIENT_CERTIFIED_DATA
Cutoff UTC: 2026-09-11T09:26:25.603672+00:00
First/last certified: N/D / N/D
PF N/D · PnL ex funding N/D € · Exp N/D €
Mother PF N/D · PnL N/D €
ΔPF N/D · ΔPnL N/D €
Causality: NOT_CERTIFIED

Relative Strength — giveback 20% dopo +0,5R
CERTIFIED_POST_FIX · NOT_CERTIFIED
Certified pairs: 0 · Legacy/pre-fix: 81 (peso 0)
Promotional weight: 0 · INSUFFICIENT_CERTIFIED_DATA
Cutoff UTC: 2026-09-11T09:26:25.603672+00:00
First/last certified: N/D / N/D
PF N/D · PnL ex funding N/D € · Exp N/D €
Mother PF N/D · PnL N/D €
ΔPF N/D · ΔPnL N/D €
Causality: NOT_CERTIFIED

Relative Strength — giveback 30% dopo +0,5R
CERTIFIED_POST_FIX · NOT_CERTIFIED
Certified pairs: 0 · Legacy/pre-fix: 81 (peso 0)
Promotional weight: 0 · INSUFFICIENT_CERTIFIED_DATA
Cutoff UTC: 2026-09-11T09:26:25.603672+00:00
First/last certified: N/D / N/D
PF N/D · PnL ex funding N/D € · Exp N/D €
Mother PF N/D · PnL N/D €
ΔPF N/D · ΔPnL N/D €
Causality: NOT_CERTIFIED

Scanner Top 5 BTC Strength — giveback 20% dopo +1,4R
CERTIFIED_POST_FIX · NOT_CERTIFIED
Certified pairs: 0 · Legacy/pre-fix: 90 (peso 0)
Promotional weight: 0 · INSUFFICIENT_CERTIFIED_DATA
Cutoff UTC: 2026-09-11T09:26:25.603672+00:00
First/last certified: N/D / N/D
PF N/D · PnL ex funding N/D € · Exp N/D €
Mother PF N/D · PnL N/D €
ΔPF N/D · ΔPnL N/D €
Causality: NOT_CERTIFIED

Master Adaptive Consensus — breakeven dopo +0,2R
CERTIFIED_POST_FIX · NOT_CERTIFIED
Certified pairs: 0 · Legacy/pre-fix: 38 (peso 0)
Promotional weight: 0 · INSUFFICIENT_CERTIFIED_DATA
Cutoff UTC: 2026-09-11T09:26:25.603672+00:00
First/last certified: N/D / N/D
PF N/D · PnL ex funding N/D € · Exp N/D €
Mother PF N/D · PnL N/D €
ΔPF N/D · ΔPnL N/D €
Causality: NOT_CERTIFIED

Momentum Breakout V3 Filtered — giveback 20% dopo +1,0R
CERTIFIED_POST_FIX · NOT_CERTIFIED
Certified pairs: 0 · Legacy/pre-fix: 154 (peso 0)
Promotional weight: 0 · INSUFFICIENT_CERTIFIED_DATA
Cutoff UTC: 2026-09-11T09:26:25.603672+00:00
First/last certified: N/D / N/D
PF N/D · PnL ex funding N/D € · Exp N/D €
Mother PF N/D · PnL N/D €
ΔPF N/D · ΔPnL N/D €
Causality: NOT_CERTIFIED

Momentum Breakout — giveback 20% dopo +1,4R
CERTIFIED_POST_FIX · NOT_CERTIFIED
Certified pairs: 0 · Legacy/pre-fix: 0 (peso 0)
Promotional weight: 0 · INSUFFICIENT_CERTIFIED_DATA
Cutoff UTC: 2026-09-11T09:26:25.603672+00:00
First/last certified: N/D / N/D
PF N/D · PnL ex funding N/D € · Exp N/D €
Mother PF N/D · PnL N/D €
ΔPF N/D · ΔPnL N/D €
Causality: NOT_CERTIFIED

AUTO_PROMOTION=DISABLED · nessun ordine · revisione umana obbligatoria.

# Blocco 4.5 — Crash Cascade Guard

Generato: 2026-09-21T19:06:53+00:00

> Paper-only. In mercato NORMAL/WATCH non riduce i segnali. Le limitazioni iniziano soltanto in STRESS, RECOVERY, CRASH, EXTREME o con dati non affidabili.

## Stato corrente

- Livello: **NORMAL**
- Direzione: **NONE**
- Segnali bloccati nel ciclo: **0**
- Simulazioni bloccate attive: **20**
- Simulazioni completate nel ciclo: **0**
- Liquidazioni virtuali evitate totali: **2**
- Valore cumulato del filtro: **835.71 R**
- Profitto virtuale mancato: **1993.38 R**

## Stress test portafogli Paper

| Scenario | Posizioni interessate | Liquidazioni stimate | Perdita stimata EUR |
| --- | ---: | ---: | ---: |
| DOWN_10 | 169 | 0 | 17190.08 |
| DOWN_20 | 169 | 0 | 34380.15 |
| DOWN_30 | 169 | 0 | 51570.23 |
| DOWN_40 | 169 | 47 | 64105.05 |
| UP_10 | 0 | 0 | 0.00 |
| UP_20 | 0 | 0 | 0.00 |
| UP_30 | 0 | 0 | 0.00 |
| UP_40 | 0 | 0 | 0.00 |

## Modello di esecuzione

Se una candela di cascata attraversa nello stesso intervallo sia lo stop sia il prezzo di liquidazione, il Paper usa il caso peggiore e registra una liquidazione intrabar. Gli stop in gap o in regime di stress ricevono slippage aggiuntivo.

## Requisiti prima del live futures

- modalità ISOLATED obbligatoria;
- stop nativo sull'exchange;
- conferma dello stop prima di accettare la posizione;
- cross margin vietato.

# Blocco 5 — Candidati evolutivi controllati

Generato: 2026-09-21T19:06:19+00:00

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

Generato: 2026-09-21T19:11:02+00:00

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

Generato: 2026-09-21T19:11:02+00:00

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

Generato: 2026-09-21T19:11:02+00:00

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

Generato: 2026-09-21T19:11:02+00:00

> Paper-only. La memoria può bloccare soltanto una futura proposta Block 5 classificata AVOID; non modifica strategie esistenti.

## Stato

- Strategie/portafogli valutati: **142**
- Hall of Fame: **20**
- Memorie genetiche: **4**
- Firme bloccate: **0**
- Azioni automatiche e live: **0**

## Hall of Fame

| Rank | Strategia | Stato | Score | Grade | Trade | PF | Expectancy R | DD R |
| ---: | --- | --- | ---: | --- | ---: | ---: | ---: | ---: |
| 1 | SHADOW_COMBO_TREND_SIDE_REGIME_GUARD_V1 | BASELINE | 24.9 | E | 171 | 1.58 | 0.283 | 23.36 |
| 2 | SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_V1 | BASELINE | 23.2 | E | 202 | 1.46 | 0.195 | 14.92 |
| 3 | SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_GUARD_V1 | BASELINE | 22.5 | E | 194 | 1.27 | 0.123 | 10.66 |
| 4 | SHADOW_DONCHIAN_1H | BASELINE | 22.2 | E | 178 | 1.36 | 0.212 | 20.49 |
| 5 | SHADOW_DONCHIAN_1H_GB20_120R_V1 | BASELINE | 22.1 | E | 146 | 1.40 | 0.230 | 20.49 |
| 6 | SHADOW_1H_FAST_SCORE_6_75_COST_AWARE_V1 | BASELINE | 21.6 | E | 227 | 1.31 | 0.146 | 25.45 |
| 7 | SHADOW_COMBO_ADAPTIVE | BASELINE | 21.1 | E | 244 | 1.29 | 0.141 | 23.82 |
| 8 | SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_V1 | BASELINE | 20.7 | E | 257 | 1.22 | 0.107 | 30.08 |
| 9 | SHADOW_1H_FAST_V3_NOHIGH_V1 | BASELINE | 20.3 | E | 227 | 1.22 | 0.104 | 14.78 |
| 10 | SHADOW_COMBO_ADAPTIVE_SIDE_REGIME_GUARD_V1 | BASELINE | 19.9 | E | 196 | 1.19 | 0.104 | 25.62 |

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

Generato: 2026-09-21T19:11:03+00:00

> Paper-only e advisory. Il blocco misura quali strategie funzionano nei diversi regimi, ma non cambia automaticamente strategia o posizione.

## Stato

- Regime corrente: **HIGH_VOLATILITY**
- Righe di performance: **1126**
- Strategie preferite nel regime corrente: **5**
- Strategie da evitare nel regime corrente: **1**
- Memorie contestuali: **538**
- Routing automatico: **NO**

## Classifica del regime corrente

| Rank | Portafoglio | Famiglia | Stato | Fitness | Trade | PF | Expectancy R | DD R |
| ---: | --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| 1 | SHADOW_DONCHIAN_1H_GB20_120R_V1 | shadow-donchian-1h-gb20-120r-v1 | OBSERVING | 83.9 | 18 | 5.29 | 1.168 | 2.22 |
| 2 | SHADOW_COMBO_TREND_SIDE_REGIME_GUARD_V1 | shadow-combo-trend-side-regime-guard-v1 | OBSERVING | 83.7 | 17 | 5.18 | 1.097 | 2.07 |
| 3 | SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | shadow-combo-adaptive-partial-1r-v1 | COMPATIBLE | 82.4 | 33 | 1.97 | 0.409 | 4.37 |
| 4 | MAIN_SIDE_REGIME_GUARD_V1 | main-side-regime-guard-v1 | OBSERVING | 81.3 | 12 | 6.90 | 1.150 | 2.34 |
| 5 | SHADOW_SOL_DONCHIAN_1H | shadow-sol-donchian-1h | INSUFFICIENT | 80.8 | 2 | 99.00 | 0.973 | 0.00 |
| 6 | SHADOW_BTC_ADAPTIVE_1H | shadow-btc-adaptive-1h | INSUFFICIENT | 80.4 | 1 | 99.00 | 0.861 | 0.00 |
| 7 | SHADOW_BTC_DONCHIAN_1H | shadow-btc-donchian-1h | INSUFFICIENT | 80.4 | 1 | 99.00 | 0.969 | 0.00 |
| 8 | SHADOW_RSI_SHORT_15X_10_RSI80 | shadow-rsi-short-15x-10-rsi80 | INSUFFICIENT | 80.4 | 1 | 99.00 | 1.257 | 0.00 |
| 9 | SHADOW_RSI_SHORT_15X_50_RSI80 | shadow-rsi-short-15x-50-rsi80 | INSUFFICIENT | 80.4 | 1 | 99.00 | 1.257 | 0.00 |
| 10 | SHADOW_RSI_SHORT_5X_RSI80 | shadow-rsi-short-5x-rsi80 | INSUFFICIENT | 80.4 | 1 | 99.00 | 1.758 | 0.00 |

## Sicurezza

- Il regime viene assegnato usando solo l'ultimo record noto prima dell'entrata del trade.
- Nessun uso di dati futuri per classificare il trade.
- Il Candidate Regime Gate è advisory per impostazione predefinita.
- Nessun cambio automatico di MASTER, posizione o live.

# Blocco 11 — Collegamento protetto al live

Generato: 2026-09-21T19:11:03+00:00

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

Generato: 2026-09-21T19:06:53+00:00

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
