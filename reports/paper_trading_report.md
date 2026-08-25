# Paper trading automatico KuCoin

Generato: 2026-08-25T05:32:59+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-08-25T05:05:29+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-08-25T05:05:29+00:00 | 2026-08-25T05:05:29+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-08-25T04:45:00+00:00 | 2026-08-25T04:45:00+00:00 | 5,6 min | 25,0 min | OK |
| 60m | 12 | 2026-08-25T04:00:00+00:00 | 2026-08-25T04:00:00+00:00 | 5,6 min | 45,0 min | OK |
| 240m | 12 | 2026-08-25T00:00:00+00:00 | 2026-08-25T00:00:00+00:00 | 1,09 h | 1,00 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1H Fast V3 Long Only V1 | BTC | 60m | LONG | 4,75 | 4,50 | 0,00 | OPENED | 5,6 min | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Tp2 V1 | ZEC | 60m | LONG | 5,41 | 4,50 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Principale 4H | XRP | 240m | LONG | 7,75 | 6,00 | 0,00 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | HYPE | 240m | LONG | 7,38 | 6,00 | 0,00 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | ETH | 240m | LONG | 6,00 | 6,00 | 0,00 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | BTC | 240m | LONG | 5,25 | 6,00 | 0,75 | STALE_CANDLE | 1,09 h | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | VELVET | 240m | SHORT | -4,75 | 6,00 | 1,25 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | DOGE | 240m | LONG | 4,62 | 6,00 | 1,38 | STALE_CANDLE | 1,09 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | SOL | 240m | LONG | 4,50 | 6,00 | 1,50 | STALE_CANDLE | 1,09 h | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | SUI | 240m | LONG | 2,47 | 6,00 | 3,53 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | TUT | 240m | SHORT | -1,48 | 6,00 | 4,52 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Bilanciata 1H V3 Filtered | TUT | 60m | SHORT | -6,25 | 6,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Fast Score 6 75 Cost Aware V1 | TUT | 60m | SHORT | -6,25 | 6,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Forza relativa 1H V2 | TUT | 60m | SHORT | -6,25 | 5,50 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Combo Trend | TUT | 60m | SHORT | -6,25 | 5,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Combo Adaptive | TUT | 60m | SHORT | -6,25 | 5,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Combo Adaptive Partial 1R V1 | TUT | 60m | SHORT | -6,25 | 5,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Balanced V3 Long Only V1 | TUT | 60m | SHORT | -6,25 | 6,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Bilanciata 1H V3 Filtered | VELVET | 60m | SHORT | -6,25 | 6,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Benchmark trend following EMA 1H | VELVET | 60m | SHORT | -6,25 | 5,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Combo Trend | VELVET | 60m | SHORT | -6,25 | 5,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Combo Adaptive | VELVET | 60m | SHORT | -6,25 | 5,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.520,12 | -4,80% | €-228,23 | €3.000,00 | -7,61% | 6 | 52 | 38,46% | 0,87 | 6,85% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 52 | 2178 | PRIME INDICAZIONI | 100 (mancano 48) |

- Trade del Principale 4H chiusi: **52**; win rate **38,46%**; profit factor **0,87**.
- Expectancy: **€-3,67** per trade; P&L netto: **€-190,76**; max drawdown: **6,85%**.
- Valutazione: **Si può osservare la direzione, ma il risultato resta fragile.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 6 | €9.520,12 | €699,00 | €2.096,99 | €196,05 | €-288,04 |
| TEST | Benchmark Donchian breakout 1H | 5 | €11.448,76 | €2.408,61 | €4.817,22 | €172,42 | €63,30 |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | 7 | €11.342,35 | €984,32 | €2.952,95 | €226,58 | €27,64 |
| TEST | Combo Trend Side Regime Guard V1 | 5 | €11.256,90 | €1.200,01 | €2.400,03 | €172,08 | €96,73 |
| TEST | Donchian 1H Gb20 120R V1 | 5 | €11.179,21 | €2.351,90 | €4.703,81 | €168,36 | €61,81 |
| TEST | Scanner Top 5 Long 1H | 5 | €11.049,49 | €1.204,49 | €2.408,99 | €220,63 | €6,11 |
| TEST | Combo Adaptive | 7 | €10.754,46 | €1.410,55 | €2.821,10 | €215,28 | €38,06 |
| TEST | 1H Fast No Pepe V1 | 7 | €10.725,21 | €1.056,63 | €3.169,88 | €214,88 | €19,13 |
| TEST | Combo Adaptive Long Only V1 | 5 | €10.576,42 | €2.941,99 | €5.883,97 | €211,87 | €-9,65 |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | 5 | €10.554,59 | €1.189,19 | €3.567,56 | €211,33 | €2,04 |
| TEST | Combo Adaptive Side Regime Guard V1 | 5 | €10.546,82 | €1.097,00 | €2.194,01 | €157,82 | €123,46 |
| TEST | Main Side Regime Guard V1 | 6 | €10.507,27 | €677,33 | €2.031,99 | €163,22 | €-283,63 |
| TEST | Rapida 1H V3 Filtered | 5 | €10.486,78 | €1.181,55 | €3.544,64 | €209,97 | €2,03 |
| TEST | Scanner Top5 Btc Tp3 V1 | 5 | €10.428,40 | €1.695,19 | €3.390,38 | €208,31 | €13,82 |
| TEST | Scanner Top5 Btc Runner25 V1 | 5 | €10.422,30 | €1.694,20 | €3.388,39 | €208,19 | €13,81 |
| TEST | Scanner Top10 Long | 5 | €10.407,68 | €3.976,59 | €7.953,18 | €156,78 | €47,41 |
| TEST | 1H Fast Tp2 V1 | 7 | €10.355,73 | €737,92 | €2.213,75 | €156,82 | €74,50 |
| TEST | Scanner Top 5 + forza BTC 1H | 5 | €10.316,24 | €1.091,70 | €2.183,40 | €206,31 | €6,03 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 0 | €10.300,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 0 | €10.271,73 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Nohigh Range Only V1 | 0 | €10.247,95 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 0 | €10.239,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 0 | €10.235,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 4H | 1 | €10.223,23 | €330,98 | €661,97 | €0,00 | €59,25 |
| TEST | Main Dynamic Asset Selector V1 | 1 | €10.213,05 | €141,85 | €425,56 | €51,07 | €0,00 |
| TEST | Sol Donchian 4H | 0 | €10.196,46 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Donchian 1H | 0 | €10.192,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 0 | €10.185,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V2 | 0 | €10.182,21 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Partial 1R V1 | 7 | €10.160,77 | €1.277,19 | €2.554,37 | €153,58 | €66,88 |
| TEST | Btc Bollinger 1H | 1 | €10.152,40 | €1.262,52 | €3.787,57 | €50,69 | €16,27 |
| TEST | 1H Fast Score 6 75 Range Only V1 | 0 | €10.149,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 0 | €10.145,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | 0 | €10.140,84 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H V3 Filtered | 5 | €10.132,16 | €1.067,57 | €3.202,71 | €201,86 | €51,77 |
| TEST | Sol Ema 1H | 1 | €10.112,01 | €349,20 | €1.047,59 | €0,00 | €73,95 |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 0 | €10.099,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 4H | 1 | €10.087,55 | €356,10 | €712,19 | €0,00 | €63,75 |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | 3 | €10.084,59 | €687,89 | €2.063,66 | €102,66 | €21,60 |
| TEST | Btc Adaptive 4H | 1 | €10.071,10 | €648,94 | €1.297,88 | €50,35 | €1,69 |
| TEST | Btc Adaptive 1H | 1 | €10.061,74 | €1.045,87 | €3.137,61 | €50,39 | €-14,73 |
| TEST | Btc Donchian 1H | 1 | €10.049,29 | €1.175,39 | €3.526,17 | €50,34 | €-16,55 |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 0 | €10.048,77 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Bollinger 1H | 0 | €10.046,17 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €10.045,08 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V1 | 0 | €10.043,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Balanced Short Trend Down Strict V1 | 0 | €10.035,46 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · prudente · 5x | 0 | €10.028,67 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Nohigh Cap75 V1 | 0 | €10.028,66 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 4H | 1 | €10.025,87 | €775,58 | €1.551,16 | €50,15 | €-2,64 |
| TEST | Btc Ema 4H | 1 | €10.020,40 | €704,37 | €1.408,74 | €50,10 | €1,83 |
| TEST | Scalp RSI Short 85 · €50 · 15x | 0 | €10.017,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Ampia 4H | 7 | €10.016,21 | €998,50 | €1.997,00 | €206,18 | €-315,50 |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | 1 | €10.015,88 | €299,55 | €599,09 | €50,20 | €0,00 |
| TEST | Scalp RSI Short 80 · €50 · 15x | 0 | €10.015,51 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | 0 | €10.013,82 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Ema 1H | 1 | €10.010,45 | €248,90 | €746,70 | €50,09 | €-6,56 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 0 | €10.009,02 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 0 | €10.008,92 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 No Esports Long Only V1 | 4 | €10.006,39 | €1.737,79 | €5.213,38 | €148,29 | €5,25 |
| TEST | Scalp RSI Short 85 · €10 · 15x | 0 | €10.003,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 0 | €10.003,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €10 · 15x | 0 | €10.003,10 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Continuation V1 | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €10 · 15x | 0 | €9.999,33 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €10 · 15x | 0 | €9.997,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €50 · 15x | 0 | €9.996,64 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 0 | €9.995,23 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · prudente · 5x | 0 | €9.991,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €10 · 15x | 0 | €9.990,45 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €50 · 15x | 0 | €9.988,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 0 | €9.987,48 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 4H | 0 | €9.981,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · prudente · 5x | 0 | €9.980,94 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top15 Long | 7 | €9.973,26 | €1.841,32 | €3.682,65 | €195,72 | €11,20 |
| TEST | Scanner Top20 Long | 7 | €9.973,26 | €1.841,32 | €3.682,65 | €195,72 | €11,20 |
| TEST | Sol Adaptive 1H | 1 | €9.968,20 | €344,23 | €1.032,69 | €0,00 | €72,90 |
| TEST | Btc Donchian 4H | 1 | €9.966,79 | €700,60 | €1.401,20 | €49,83 | €1,82 |
| TEST | Eth Ema 4H | 1 | €9.954,71 | €487,73 | €975,47 | €49,56 | €44,44 |
| TEST | Scalp RSI Short 80 · prudente · 5x | 0 | €9.952,43 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €50 · 15x | 0 | €9.952,25 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.939,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 1H | 1 | €9.925,57 | €1.031,72 | €3.095,15 | €49,71 | €-14,53 |
| TEST | Combo Adaptive Regime V1 | 2 | €9.919,86 | €720,33 | €1.440,66 | €49,43 | €31,51 |
| TEST | Doge Donchian 1H | 0 | €9.911,95 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Quality7 V1 | 4 | €9.898,22 | €1.604,00 | €3.208,01 | €194,94 | €5,16 |
| TEST | Combo Scanner | 5 | €9.897,57 | €1.047,40 | €2.094,79 | €197,94 | €5,79 |
| TEST | Combo Adaptive Quality7 Regime V1 | 1 | €9.889,90 | €295,78 | €591,56 | €49,57 | €0,00 |
| TEST | Eth Ema 1H | 1 | €9.867,74 | €783,24 | €2.349,73 | €49,33 | €2,89 |
| TEST | Forza relativa 1H V2 | 4 | €9.856,05 | €1.806,95 | €3.613,90 | €97,62 | €65,82 |
| TEST | Eth Adaptive 1H | 0 | €9.844,63 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 0 | €9.837,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 1H | 0 | €9.821,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 0 | €9.817,34 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Guard V1 | 5 | €9.809,43 | €1.332,44 | €2.664,88 | €151,38 | €7,10 |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | 0 | €9.779,10 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 No Esports V1 | 5 | €9.778,68 | €713,06 | €2.139,17 | €195,60 | €12,44 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 0 | €9.762,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 0 | €9.723,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Balanced Long No Rhv V1 | 6 | €9.717,62 | €1.827,42 | €5.482,27 | €193,87 | €3,54 |
| TEST | Eth Bollinger 1H | 0 | €9.703,71 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | 3 | €9.693,56 | €642,23 | €1.284,46 | €97,32 | €37,12 |
| TEST | Eth Donchian 1H | 0 | €9.678,07 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Mfe V1 | 5 | €9.670,97 | €1.023,42 | €2.046,83 | €193,41 | €5,66 |
| TEST | 1H Fast V3 Long Only V1 | 6 | €9.640,32 | €1.651,50 | €4.954,51 | €192,81 | €-9,69 |
| TEST | Global Confluence puro 1H | 0 | €9.628,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Balanced V3 Long Only V1 | 5 | €9.584,43 | €1.049,33 | €3.147,98 | €191,35 | €48,63 |
| TEST | Scanner Top5 Btc Guard Mfe V1 | 5 | €9.581,30 | €1.301,45 | €2.602,90 | €147,85 | €6,93 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 0 | €9.579,83 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H V2 | 2 | €9.534,71 | €607,25 | €1.821,75 | €94,13 | €5,06 |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | 4 | €9.523,77 | €612,41 | €1.224,82 | €96,57 | €32,09 |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | 0 | €9.517,55 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Trend | 5 | €9.471,55 | €981,95 | €1.963,90 | €143,09 | €30,65 |
| TEST | 1H Fast V3 Nohigh V1 | 0 | €9.435,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Score 6 75 V1 | 0 | €9.415,87 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom10 Short | 4 | €9.398,18 | €1.261,36 | €2.522,73 | €140,86 | €77,46 |
| TEST | Scanner Bottom15 Short | 4 | €9.398,18 | €1.261,36 | €2.522,73 | €140,86 | €77,46 |
| TEST | Scanner Bottom20 Short | 4 | €9.398,18 | €1.261,36 | €2.522,73 | €140,86 | €77,46 |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | 0 | €9.389,68 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Runner25 V1 | 1 | €9.377,78 | €34,77 | €69,54 | €8,34 | €-0,39 |
| TEST | Master Adaptive Gb20 Be V1 | 0 | €9.372,49 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Gb20 Partial V1 | 0 | €9.362,52 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | 3 | €9.357,83 | €589,42 | €1.178,84 | €92,35 | €31,54 |
| TEST | Master Adaptive No Alt V1 | 0 | €9.354,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Benchmark trend following EMA 1H | 5 | €9.352,96 | €1.813,23 | €3.626,46 | €95,83 | €77,62 |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | 4 | €9.333,05 | €1.252,64 | €2.505,29 | €139,88 | €76,92 |
| TEST | Master Adaptive V1 | 0 | €9.326,30 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Profit Lock V1 | 4 | €9.318,86 | €1.250,74 | €2.501,48 | €139,67 | €76,80 |
| TEST | Master Adaptive Expanded V1 | 1 | €9.317,58 | €197,50 | €395,01 | €47,40 | €-2,24 |
| TEST | Master Adaptive Gb20 Loss Cap V1 | 1 | €9.249,86 | €195,70 | €391,41 | €45,67 | €-2,22 |
| TEST | Scanner Bottom 5 Short 1H | 4 | €9.247,14 | €1.241,11 | €2.482,23 | €138,60 | €76,21 |
| TEST | Scanner Top5 Btc Btc Le3 V1 | 3 | €9.220,07 | €610,86 | €1.221,72 | €92,56 | €35,30 |
| TEST | Combo Adaptive Mfe Trail | 6 | €9.205,93 | €1.214,43 | €2.428,87 | €183,97 | €36,86 |
| TEST | Master Adaptive Gb20 V1 | 0 | €9.202,39 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | 0 | €9.165,52 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H V1 | 0 | €9.150,69 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Cap75 V1 | 0 | €9.106,22 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Strict3 V1 | 0 | €9.056,84 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Mean Reversion | 1 | €9.029,57 | €1.684,34 | €3.368,67 | €45,09 | €14,47 |
| TEST | Combo Adaptive Runner25 V1 | 0 | €8.964,11 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Tp3 V1 | 0 | €8.796,64 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Benchmark Bollinger mean reversion 1H | 0 | €8.740,52 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Forza relativa 1H V1 | 0 | €8.445,51 | €0,00 | €0,00 | €0,00 | €0,00 |

**Importante:** ogni riga è un conto virtuale separato da €10.000. I margini dei diversi portafogli non vanno sommati come se appartenessero a un unico conto.

**Rischio agli stop** è la perdita residua stimata usando gli stop correnti. Se uno stop protegge già un profitto, il rischio residuo viene mostrato come €0.

## Legenda portafogli

| Tipo | Nome leggibile | Metodo | Significato |
| --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | Confluenza trend | Riferimento principale: confluenza di trend su 4 ore, soglia più selettiva. |
| TEST | Bilanciata 1H V1 | Confluenza trend | Versione originale V1 a 1 ora basata sulla confluenza di trend. |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | Versione V2 selettiva: esclude i regimi storicamente peggiori, richiede trend e ritorni coerenti e limita i segnali correlati. |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | Versione V3 derivata dalla V1: accetta soltanto score assoluti da 6,0 a meno di 7,5, cioè la fascia BUONA risultata migliore nel confronto Paper vs Shadow. |
| TEST | Rapida 1H V1 | Momentum / breakout | Versione originale V1 a 1 ora che cerca momentum e breakout. |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | Versione V2 selettiva: richiede vero breakout, volume, ADX, trend tecnico coerente e limita i segnali correlati. |
| TEST | Rapida 1H V3 Filtered | Momentum / breakout V3 Filtered | Versione V3 derivata dalla V1: mantiene la logica momentum originale ma esclude i segnali con score assoluto da 5,0 a meno di 6,0, fascia risultata negativa nel confronto Paper vs Shadow. |
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
| TEST | Global Confluence puro 1H | Global Confluence puro | Opera soltanto quando Global Confluence, dati exchange e struttura tecnica sono allineati. |
| TEST | Combo Trend | Combo Trend | Portafoglio sperimentale separato. |
| TEST | Combo Mean Reversion | Combo Mean Reversion | Portafoglio sperimentale separato. |
| TEST | Combo Scanner | Combo Scanner | Portafoglio sperimentale separato. |
| TEST | Combo Adaptive | Combo Adaptive | Portafoglio sperimentale separato. |
| TEST | Combo Adaptive Mfe Trail | Combo Adaptive | Portafoglio sperimentale separato. |
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

## Confronto risultati

| Tipo | Portafoglio | Strategia | Equity | P&L chiuso | Trade | Eventi indip. | Win rate | PF | Expectancy | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | Confluenza trend | €9.520,12 | €-190,76 | 52 | 52 | 38,46% | 0,87 | €-3,67 | 6,85% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €11.448,76 | €1.387,48 | 98 | 98 | 50,00% | 1,63 | €14,16 | 4,99% |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | Momentum / breakout | €11.342,35 | €1.317,19 | 137 | 137 | 54,01% | 1,50 | €9,61 | 4,41% |
| TEST | Combo Trend Side Regime Guard V1 | Combo Trend | €11.256,90 | €1.162,73 | 103 | 103 | 56,31% | 1,64 | €11,29 | 4,94% |
| TEST | Donchian 1H Gb20 120R V1 | Donchian breakout 20 barre | €11.179,21 | €1.119,37 | 66 | 66 | 50,00% | 1,85 | €16,96 | 4,99% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €11.049,49 | €1.045,48 | 131 | 131 | 50,38% | 1,41 | €7,98 | 8,85% |
| TEST | Combo Adaptive | Combo Adaptive | €10.754,46 | €719,14 | 140 | 140 | 46,43% | 1,31 | €5,14 | 7,91% |
| TEST | 1H Fast No Pepe V1 | Momentum / breakout | €10.725,21 | €708,81 | 201 | 201 | 48,76% | 1,19 | €3,53 | 6,80% |
| TEST | Combo Adaptive Long Only V1 | Combo Adaptive | €10.576,42 | €590,19 | 113 | 113 | 49,56% | 1,25 | €5,22 | 6,25% |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | Momentum / breakout V3 Filtered | €10.554,59 | €554,77 | 187 | 187 | 50,80% | 1,18 | €2,97 | 9,50% |
| TEST | Combo Adaptive Side Regime Guard V1 | Combo Adaptive | €10.546,82 | €425,63 | 112 | 112 | 48,21% | 1,19 | €3,80 | 8,68% |
| TEST | Main Side Regime Guard V1 | Confluenza trend | €10.507,27 | €792,57 | 33 | 33 | 54,55% | 2,27 | €24,02 | 3,82% |
| TEST | Rapida 1H V3 Filtered | Momentum / breakout V3 Filtered | €10.486,78 | €486,95 | 231 | 231 | 45,02% | 1,12 | €2,11 | 9,48% |
| TEST | Scanner Top5 Btc Tp3 V1 | Scanner Top 5 + forza BTC | €10.428,40 | €417,23 | 97 | 97 | 44,33% | 1,19 | €4,30 | 11,78% |
| TEST | Scanner Top5 Btc Runner25 V1 | Scanner Top 5 + forza BTC | €10.422,30 | €411,13 | 101 | 101 | 44,55% | 1,19 | €4,07 | 12,06% |
| TEST | Scanner Top10 Long | Scanner Top10 Long | €10.407,68 | €365,52 | 118 | 118 | 50,85% | 1,18 | €3,10 | 10,31% |
| TEST | 1H Fast Tp2 V1 | Momentum / breakout | €10.355,73 | €282,60 | 217 | 217 | 41,01% | 1,07 | €1,30 | 6,56% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €10.316,24 | €312,12 | 118 | 118 | 46,61% | 1,13 | €2,65 | 11,27% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | Momentum / breakout V3 Filtered | €10.300,05 | €300,05 | 33 | 33 | 48,48% | 2,04 | €9,09 | 2,01% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | Momentum / breakout V3 Filtered | €10.271,73 | €271,73 | 22 | 22 | 50,00% | 1,74 | €12,35 | 1,72% |
| TEST | 1H Fast V3 Nohigh Range Only V1 | Momentum / breakout V3 Filtered | €10.247,95 | €247,95 | 41 | 41 | 46,34% | 1,25 | €6,05 | 3,97% |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | Momentum / breakout V3 Filtered | €10.239,20 | €239,20 | 17 | 17 | 52,94% | 4,50 | €14,07 | 1,01% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | Momentum / breakout V3 Filtered | €10.235,18 | €235,18 | 20 | 20 | 50,00% | 1,90 | €11,76 | 2,73% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €10.223,23 | €164,84 | 6 | 6 | 50,00% | 2,46 | €27,47 | 1,01% |
| TEST | Main Dynamic Asset Selector V1 | Confluenza trend | €10.213,05 | €213,35 | 12 | 12 | 41,67% | 1,74 | €17,78 | 1,68% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €10.196,46 | €196,46 | 6 | 6 | 50,00% | 2,73 | €32,74 | 1,05% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €10.192,62 | €192,62 | 13 | 13 | 53,85% | 1,78 | €14,82 | 2,77% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | Momentum / breakout V3 Filtered | €10.185,37 | €185,37 | 22 | 22 | 40,91% | 1,57 | €8,43 | 2,27% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €10.182,21 | €182,21 | 45 | 40 | 46,67% | 1,16 | €4,05 | 3,89% |
| TEST | Combo Adaptive Partial 1R V1 | Combo Adaptive | €10.160,77 | €95,87 | 142 | 142 | 45,77% | 1,04 | €0,68 | 8,69% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.152,40 | €138,40 | 5 | 5 | 80,00% | 3,42 | €27,68 | 0,85% |
| TEST | 1H Fast Score 6 75 Range Only V1 | Momentum / breakout | €10.149,62 | €149,62 | 38 | 38 | 44,74% | 1,14 | €3,94 | 3,35% |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | Momentum / breakout V3 Filtered | €10.145,12 | €145,12 | 44 | 44 | 45,45% | 1,20 | €3,30 | 2,91% |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | Momentum / breakout V3 Filtered | €10.140,84 | €140,84 | 63 | 63 | 44,44% | 1,10 | €2,24 | 5,24% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €10.132,16 | €83,31 | 148 | 148 | 43,24% | 1,03 | €0,56 | 9,12% |
| TEST | Sol Ema 1H | Trend following EMA | €10.112,01 | €39,53 | 13 | 13 | 38,46% | 1,10 | €3,04 | 3,33% |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | Momentum / breakout V3 Filtered | €10.099,04 | €99,04 | 55 | 55 | 54,55% | 1,12 | €1,80 | 3,59% |
| TEST | Sol Ema 4H | Trend following EMA | €10.087,55 | €24,73 | 7 | 7 | 28,57% | 1,11 | €3,53 | 2,27% |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | Momentum / breakout | €10.084,59 | €65,65 | 53 | 53 | 45,28% | 1,06 | €1,24 | 3,73% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €10.071,10 | €70,19 | 2 | 2 | 50,00% | 2,39 | €35,09 | 0,96% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €10.061,74 | €78,35 | 7 | 7 | 57,14% | 1,69 | €11,19 | 1,13% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €10.049,29 | €67,96 | 8 | 8 | 62,50% | 1,41 | €8,50 | 1,49% |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | Momentum / breakout V3 Filtered | €10.048,77 | €48,77 | 23 | 23 | 43,48% | 1,12 | €2,12 | 3,05% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €10.046,17 | €46,17 | 9 | 9 | 55,56% | 1,19 | €5,13 | 1,89% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €10.045,08 | €45,08 | 28 | 28 | 46,43% | 1,40 | €1,61 | 0,33% |
| TEST | Rapida 1H V1 | Momentum / breakout | €10.043,28 | €43,28 | 78 | 78 | 34,62% | 1,02 | €0,55 | 6,76% |
| TEST | 1H Balanced Short Trend Down Strict V1 | Confluenza trend | €10.035,46 | €35,46 | 13 | 13 | 38,46% | 1,13 | €2,73 | 1,80% |
| TEST | Scalp RSI Long 20 · prudente · 5x | Inversione RSI estrema 15m | €10.028,67 | €28,67 | 9 | 9 | 55,56% | 1,80 | €3,19 | 0,36% |
| TEST | 1H Fast Nohigh Cap75 V1 | Momentum / breakout | €10.028,66 | €28,66 | 122 | 122 | 43,44% | 1,01 | €0,23 | 7,10% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.025,87 | €29,45 | 2 | 2 | 50,00% | 1,54 | €14,72 | 0,86% |
| TEST | Btc Ema 4H | Trend following EMA | €10.020,40 | €19,41 | 3 | 3 | 33,33% | 1,19 | €6,47 | 1,76% |
| TEST | Scalp RSI Short 85 · €50 · 15x | Inversione RSI estrema 15m | €10.017,98 | €17,98 | 5 | 5 | 60,00% | 1,69 | €3,60 | 0,31% |
| TEST | Ampia 4H | Confluenza trend | €10.016,21 | €333,13 | 51 | 51 | 35,29% | 1,29 | €6,53 | 4,45% |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | Combo Adaptive | €10.015,88 | €16,33 | 37 | 37 | 48,65% | 1,02 | €0,44 | 4,21% |
| TEST | Scalp RSI Short 80 · €50 · 15x | Inversione RSI estrema 15m | €10.015,51 | €15,51 | 15 | 15 | 40,00% | 1,32 | €1,03 | 0,53% |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | Momentum / breakout V3 Filtered | €10.013,82 | €13,82 | 41 | 41 | 48,78% | 1,01 | €0,34 | 4,50% |
| TEST | Doge Ema 1H | Trend following EMA | €10.010,45 | €18,06 | 15 | 15 | 60,00% | 1,05 | €1,20 | 2,77% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €10.009,02 | €9,02 | 28 | 28 | 46,43% | 1,40 | €0,32 | 0,07% |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | Momentum / breakout V3 Filtered | €10.008,92 | €8,92 | 30 | 30 | 36,67% | 1,02 | €0,30 | 4,84% |
| TEST | 1H Fast V3 No Esports Long Only V1 | Momentum / breakout V3 Filtered | €10.006,39 | €4,34 | 146 | 146 | 44,52% | 1,00 | €0,03 | 10,60% |
| TEST | Scalp RSI Short 85 · €10 · 15x | Inversione RSI estrema 15m | €10.003,60 | €3,60 | 5 | 5 | 60,00% | 1,69 | €0,72 | 0,06% |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | Momentum / breakout V3 Filtered | €10.003,37 | €3,37 | 8 | 8 | 37,50% | 1,02 | €0,42 | 2,15% |
| TEST | Scalp RSI Short 80 · €10 · 15x | Inversione RSI estrema 15m | €10.003,10 | €3,10 | 15 | 15 | 40,00% | 1,32 | €0,21 | 0,11% |
| TEST | Scanner Bottom5 Short Continuation V1 | Scanner Bottom5 Short Continuation | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 20 · €10 · 15x | Inversione RSI estrema 15m | €9.999,33 | €-0,67 | 9 | 9 | 44,44% | 0,85 | €-0,07 | 0,04% |
| TEST | Scalp RSI Long 15 · €10 · 15x | Inversione RSI estrema 15m | €9.997,60 | €-2,40 | 3 | 3 | 33,33% | 0,13 | €-0,80 | 0,02% |
| TEST | Scalp RSI Long 20 · €50 · 15x | Inversione RSI estrema 15m | €9.996,64 | €-3,36 | 9 | 9 | 44,44% | 0,85 | €-0,37 | 0,21% |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | Momentum / breakout V3 Filtered | €9.995,23 | €-4,77 | 15 | 15 | 46,67% | 0,99 | €-0,32 | 2,70% |
| TEST | Scalp RSI Short 85 · prudente · 5x | Inversione RSI estrema 15m | €9.991,38 | €-8,62 | 5 | 5 | 60,00% | 0,61 | €-1,72 | 0,30% |
| TEST | Scalp RSI Long 25 · €10 · 15x | Inversione RSI estrema 15m | €9.990,45 | €-9,55 | 15 | 15 | 40,00% | 0,36 | €-0,64 | 0,14% |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | €9.988,00 | €-12,00 | 3 | 3 | 33,33% | 0,13 | €-4,00 | 0,12% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €9.987,48 | €-12,52 | 15 | 15 | 40,00% | 0,83 | €-0,83 | 0,71% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €9.981,72 | €-18,28 | 3 | 3 | 33,33% | 0,83 | €-6,09 | 1,22% |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | €9.980,94 | €-19,06 | 3 | 3 | 33,33% | 0,19 | €-6,35 | 0,20% |
| TEST | Scanner Top15 Long | Scanner Top15 Long | €9.973,26 | €-35,08 | 115 | 115 | 50,43% | 0,98 | €-0,31 | 10,31% |
| TEST | Scanner Top20 Long | Scanner Top20 Long | €9.973,26 | €-35,08 | 115 | 115 | 50,43% | 0,98 | €-0,31 | 10,31% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €9.968,20 | €-103,26 | 14 | 14 | 35,71% | 0,77 | €-7,38 | 4,59% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €9.966,79 | €-34,19 | 4 | 4 | 25,00% | 0,80 | €-8,55 | 2,43% |
| TEST | Eth Ema 4H | Trend following EMA | €9.954,71 | €-88,72 | 5 | 5 | 20,00% | 0,58 | €-17,74 | 1,83% |
| TEST | Scalp RSI Short 80 · prudente · 5x | Inversione RSI estrema 15m | €9.952,43 | €-47,57 | 15 | 15 | 40,00% | 0,45 | €-3,17 | 0,89% |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | €9.952,25 | €-47,75 | 15 | 15 | 40,00% | 0,36 | €-3,18 | 0,72% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.939,62 | €-60,38 | 28 | 28 | 46,43% | 0,60 | €-2,16 | 0,84% |
| TEST | Btc Ema 1H | Trend following EMA | €9.925,57 | €-58,05 | 11 | 11 | 36,36% | 0,82 | €-5,28 | 1,94% |
| TEST | Combo Adaptive Regime V1 | Combo Adaptive | €9.919,86 | €-110,19 | 53 | 53 | 47,17% | 0,92 | €-2,08 | 5,38% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €9.911,95 | €-88,05 | 12 | 12 | 50,00% | 0,75 | €-7,34 | 3,08% |
| TEST | Combo Adaptive Quality7 V1 | Combo Adaptive | €9.898,22 | €-104,50 | 76 | 76 | 40,79% | 0,94 | €-1,38 | 8,88% |
| TEST | Combo Scanner | Combo Scanner | €9.897,57 | €-106,39 | 122 | 122 | 45,90% | 0,96 | €-0,87 | 11,38% |
| TEST | Combo Adaptive Quality7 Regime V1 | Combo Adaptive | €9.889,90 | €-109,66 | 37 | 37 | 43,24% | 0,88 | €-2,96 | 5,41% |
| TEST | Eth Ema 1H | Trend following EMA | €9.867,74 | €-133,67 | 17 | 17 | 41,18% | 0,77 | €-7,86 | 4,80% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €9.856,05 | €-207,15 | 105 | 100 | 41,90% | 0,93 | €-1,97 | 10,88% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.844,63 | €-155,37 | 13 | 13 | 38,46% | 0,66 | €-11,95 | 3,14% |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | Momentum / breakout V3 Filtered | €9.837,38 | €-162,62 | 37 | 37 | 40,54% | 0,76 | €-4,40 | 3,08% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.821,20 | €-178,80 | 11 | 11 | 36,36% | 0,61 | €-16,25 | 2,37% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | Momentum / breakout V3 Filtered | €9.817,34 | €-182,66 | 24 | 24 | 41,67% | 0,64 | €-7,61 | 3,23% |
| TEST | Scanner Top5 Btc Guard V1 | Scanner Top 5 + forza BTC | €9.809,43 | €-195,93 | 100 | 100 | 41,00% | 0,92 | €-1,96 | 7,34% |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | Momentum / breakout | €9.779,10 | €-220,90 | 86 | 86 | 41,86% | 0,88 | €-2,57 | 7,10% |
| TEST | 1H Fast V3 No Esports V1 | Momentum / breakout V3 Filtered | €9.778,68 | €-232,40 | 201 | 201 | 43,78% | 0,94 | €-1,16 | 9,00% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | Momentum / breakout V3 Filtered | €9.762,18 | €-237,82 | 7 | 7 | 14,29% | 0,02 | €-33,97 | 2,82% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | Momentum / breakout V3 Filtered | €9.723,72 | €-276,28 | 31 | 31 | 32,26% | 0,62 | €-8,91 | 4,83% |
| TEST | 1H Balanced Long No Rhv V1 | Confluenza trend | €9.717,62 | €-282,52 | 93 | 93 | 46,24% | 0,86 | €-3,04 | 9,26% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €9.703,71 | €-296,29 | 7 | 7 | 28,57% | 0,22 | €-42,33 | 4,16% |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | Scanner Top 5 + forza BTC | €9.693,56 | €-341,98 | 18 | 18 | 27,78% | 0,42 | €-19,00 | 5,46% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.678,07 | €-321,93 | 13 | 13 | 23,08% | 0,47 | €-24,76 | 3,44% |
| TEST | Scanner Top5 Btc Mfe V1 | Scanner Top 5 + forza BTC | €9.670,97 | €-332,89 | 110 | 110 | 45,45% | 0,85 | €-3,03 | 12,28% |
| TEST | 1H Fast V3 Long Only V1 | Momentum / breakout V3 Filtered | €9.640,32 | €-346,95 | 158 | 158 | 41,77% | 0,90 | €-2,20 | 12,52% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.628,04 | €-371,96 | 16 | 16 | 25,00% | 0,32 | €-23,25 | 3,92% |
| TEST | 1H Balanced V3 Long Only V1 | Confluenza trend V3 Filtered | €9.584,43 | €-461,37 | 103 | 103 | 43,69% | 0,77 | €-4,48 | 8,85% |
| TEST | Scanner Top5 Btc Guard Mfe V1 | Scanner Top 5 + forza BTC | €9.581,30 | €-423,94 | 117 | 117 | 41,88% | 0,84 | €-3,62 | 8,78% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | Momentum / breakout V3 Filtered | €9.579,83 | €-420,17 | 11 | 11 | 0,00% | 0,00 | €-38,20 | 4,20% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €9.534,71 | €-468,75 | 101 | 93 | 43,56% | 0,78 | €-4,64 | 8,84% |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | Scanner Top 5 + forza BTC | €9.523,77 | €-507,05 | 64 | 64 | 39,06% | 0,74 | €-7,92 | 7,99% |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | Momentum / breakout V3 Filtered | €9.517,55 | €-482,45 | 78 | 78 | 39,74% | 0,78 | €-6,19 | 6,59% |
| TEST | Combo Trend | Combo Trend | €9.471,55 | €-557,05 | 150 | 150 | 39,33% | 0,84 | €-3,71 | 10,85% |
| TEST | 1H Fast V3 Nohigh V1 | Momentum / breakout V3 Filtered | €9.435,38 | €-564,62 | 112 | 112 | 40,18% | 0,79 | €-5,04 | 6,91% |
| TEST | 1H Fast Score 6 75 V1 | Momentum / breakout | €9.415,87 | €-584,13 | 137 | 137 | 40,15% | 0,84 | €-4,26 | 12,33% |
| TEST | Scanner Bottom10 Short | Scanner Bottom10 Short | €9.398,18 | €-677,79 | 70 | 70 | 31,43% | 0,65 | €-9,68 | 8,91% |
| TEST | Scanner Bottom15 Short | Scanner Bottom15 Short | €9.398,18 | €-677,79 | 70 | 70 | 31,43% | 0,65 | €-9,68 | 8,91% |
| TEST | Scanner Bottom20 Short | Scanner Bottom20 Short | €9.398,18 | €-677,79 | 70 | 70 | 31,43% | 0,65 | €-9,68 | 8,91% |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | Momentum / breakout V3 Filtered | €9.389,68 | €-610,32 | 83 | 83 | 44,58% | 0,76 | €-7,35 | 7,69% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €9.377,78 | €-621,78 | 51 | 51 | 31,37% | 0,66 | €-12,19 | 8,18% |
| TEST | Master Adaptive Gb20 Be V1 | Master Adaptive Consensus | €9.372,49 | €-627,51 | 55 | 55 | 29,09% | 0,62 | €-11,41 | 8,39% |
| TEST | Master Adaptive Gb20 Partial V1 | Master Adaptive Consensus | €9.362,52 | €-637,48 | 50 | 50 | 34,00% | 0,60 | €-12,75 | 7,98% |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | Scanner Top 5 + forza BTC | €9.357,83 | €-672,47 | 80 | 80 | 38,75% | 0,70 | €-8,41 | 7,27% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €9.354,60 | €-645,40 | 58 | 58 | 34,48% | 0,67 | €-11,13 | 7,26% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.352,96 | €-721,74 | 122 | 122 | 38,52% | 0,71 | €-5,92 | 12,31% |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | Scanner Bottom 5 Short | €9.333,05 | €-742,38 | 61 | 61 | 31,15% | 0,58 | €-12,17 | 8,93% |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | €9.326,30 | €-673,70 | 52 | 52 | 32,69% | 0,62 | €-12,96 | 7,80% |
| TEST | Scanner Bottom5 Short Profit Lock V1 | Scanner Bottom 5 Short | €9.318,86 | €-756,47 | 62 | 62 | 30,65% | 0,56 | €-12,20 | 8,93% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €9.317,58 | €-679,95 | 61 | 61 | 34,43% | 0,66 | €-11,15 | 7,96% |
| TEST | Master Adaptive Gb20 Loss Cap V1 | Master Adaptive Consensus | €9.249,86 | €-747,69 | 42 | 42 | 23,81% | 0,53 | €-17,80 | 11,41% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.247,14 | €-827,60 | 89 | 89 | 31,46% | 0,64 | €-9,30 | 10,02% |
| TEST | Scanner Top5 Btc Btc Le3 V1 | Scanner Top 5 + forza BTC | €9.220,07 | €-813,73 | 64 | 64 | 34,38% | 0,56 | €-12,71 | 11,72% |
| TEST | Combo Adaptive Mfe Trail | Combo Adaptive | €9.205,93 | €-828,61 | 153 | 153 | 41,18% | 0,73 | €-5,42 | 15,45% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €9.202,39 | €-797,61 | 87 | 87 | 48,28% | 0,60 | €-9,17 | 9,02% |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | Momentum / breakout | €9.165,52 | €-834,48 | 95 | 95 | 41,05% | 0,72 | €-8,78 | 12,64% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €9.150,69 | €-849,31 | 121 | 121 | 36,36% | 0,69 | €-7,02 | 13,99% |
| TEST | 1H Fast V3 Cap75 V1 | Momentum / breakout V3 Filtered | €9.106,22 | €-893,78 | 136 | 136 | 36,03% | 0,75 | €-6,57 | 14,10% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €9.056,84 | €-943,16 | 53 | 53 | 28,30% | 0,59 | €-17,80 | 11,51% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €9.029,57 | €-982,88 | 42 | 42 | 35,71% | 0,46 | €-23,40 | 11,62% |
| TEST | Combo Adaptive Runner25 V1 | Combo Adaptive | €8.964,11 | €-1.035,89 | 94 | 94 | 30,85% | 0,53 | €-11,02 | 12,67% |
| TEST | Combo Adaptive Tp3 V1 | Combo Adaptive | €8.796,64 | €-1.203,36 | 75 | 75 | 29,33% | 0,38 | €-16,04 | 12,67% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €8.740,52 | €-1.259,48 | 81 | 81 | 38,27% | 0,55 | €-15,55 | 14,60% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €8.445,51 | €-1.554,49 | 105 | 105 | 27,62% | 0,47 | €-14,80 | 17,39% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | SPCX | LONG | Confluenza trend | 240m | 3,0x | 136,56189 | 136,56189 | 128,79610 | 91,72407 | 152,09346 | €285,50 | €856,50 | €48,71 | €0,00 |
| Principale 4H | VELVET | LONG | Confluenza trend | 240m | 3,0x | 0,55987 | 0,14726 | 0,49269 | 0,37605 | 0,69424 | €131,08 | €393,24 | €47,19 | €-289,81 |
| Principale 4H | EDEN | LONG | Confluenza trend | 240m | 3,0x | 0,06195 | 0,06195 | 0,05451 | 0,04161 | 0,07681 | €130,34 | €391,02 | €46,92 | €0,00 |
| Principale 4H | TRUMP | LONG | Confluenza trend | 240m | 3,0x | 2,46049 | 2,46049 | 2,16523 | 1,65263 | 3,05101 | €134,98 | €404,95 | €48,59 | €0,00 |
| Principale 4H | XRP | LONG | Confluenza trend | 240m | 3,0x | 1,46057 | 1,51986 | 1,30460 | 0,98102 | 1,77252 | €8,58 | €25,73 | €2,75 | €1,04 |
| Principale 4H | HYPE | LONG | Confluenza trend | 240m | 3,0x | 78,87277 | 81,10800 | 73,04357 | 52,97621 | 90,53117 | €8,52 | €25,56 | €1,89 | €0,72 |
| 1H Balanced Long No Rhv V1 | SKHYNIX | LONG | Confluenza trend | 60m | 3,0x | 1214,11277 | 1214,11277 | 1170,18211 | 815,47908 | 1301,97411 | €413,43 | €1.240,28 | €44,88 | €0,00 |
| 1H Balanced Long No Rhv V1 | BOME | LONG | Confluenza trend | 60m | 3,0x | 0,00129 | 0,00129 | 0,00114 | 0,00087 | 0,00160 | €134,98 | €404,95 | €48,59 | €0,00 |
| 1H Balanced Long No Rhv V1 | TAO | LONG | Confluenza trend | 60m | 3,0x | 247,38947 | 247,38947 | 237,94346 | 166,16326 | 266,28148 | €428,20 | €1.284,61 | €49,05 | €0,00 |
| 1H Balanced Long No Rhv V1 | PEPE | LONG | Confluenza trend | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €21,51 | €64,54 | €5,62 | €0,59 |
| 1H Balanced Long No Rhv V1 | BTC | LONG | Confluenza trend | 60m | 3,0x | 79476,50212 | 80459,88000 | 79941,98781 | 53381,71726 | 82107,82923 | €8,35 | €25,04 | €0,00 | €0,31 |
| 1H Balanced Long No Rhv V1 | ETH | LONG | Confluenza trend | 60m | 3,0x | 2496,21914 | 2498,90000 | 2449,86508 | 1676,62719 | 2588,92725 | €820,95 | €2.462,84 | €45,73 | €2,65 |
| Bilanciata 1H V2 | SKHYNIX | LONG | Confluenza trend V2 | 60m | 3,0x | 1214,11277 | 1214,11277 | 1170,18211 | 815,47908 | 1301,97411 | €422,38 | €1.267,15 | €45,85 | €0,00 |
| Bilanciata 1H V2 | PEPE | LONG | Confluenza trend V2 | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €184,87 | €554,60 | €48,28 | €5,06 |
| Bilanciata 1H V3 Filtered | SKHYNIX | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1220,85412 | 1220,85412 | 1177,63561 | 820,00702 | 1307,29117 | €460,42 | €1.381,27 | €48,90 | €0,00 |
| Bilanciata 1H V3 Filtered | ZEC | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 807,93155 | 851,02000 | 737,89694 | 542,66069 | 948,00078 | €195,29 | €585,88 | €50,79 | €31,25 |
| Bilanciata 1H V3 Filtered | XRP | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1,47399 | 1,51986 | 1,35380 | 0,99003 | 1,71438 | €205,84 | €617,51 | €50,35 | €19,21 |
| Bilanciata 1H V3 Filtered | PEPE | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €8,77 | €26,32 | €2,02 | €1,31 |
| Bilanciata 1H V3 Filtered | PUMP | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,00523 | 0,00523 | 0,00479 | 0,00351 | 0,00611 | €197,24 | €591,72 | €49,81 | €0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | BTW | LONG | Momentum / breakout | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €8,91 | €26,72 | €3,13 | €0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00086 | 0,00146 | €215,92 | €647,76 | €57,03 | €0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | NEAR | LONG | Momentum / breakout | 60m | 3,0x | 2,08142 | 2,08142 | 2,02315 | 1,39802 | 2,16882 | €42,86 | €128,59 | €3,60 | €0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | XRP | LONG | Momentum / breakout | 60m | 3,0x | 1,47399 | 1,51986 | 1,38051 | 0,99003 | 1,61422 | €284,39 | €853,18 | €54,11 | €26,55 |
| 1H Fast Score 6 75 Cost Aware V1 | PUMP | LONG | Momentum / breakout | 60m | 3,0x | 0,00523 | 0,00523 | 0,00489 | 0,00351 | 0,00574 | €260,23 | €780,70 | €51,11 | €0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14742 | 0,14726 | 0,16511 | 0,19582 | 0,12088 | €157,13 | €471,39 | €56,57 | €0,51 |
| 1H Fast Score 6 75 Cost Aware V1 | SOL | LONG | Momentum / breakout | 60m | 3,0x | 100,45609 | 101,76000 | 98,13142 | 67,47301 | 103,94309 | €14,87 | €44,62 | €1,03 | €0,58 |
| 1H Fast Long Btc 1 3 Cap75 V1 | XRP | LONG | Momentum / breakout | 60m | 3,0x | 1,49738 | 1,51986 | 1,40463 | 1,00574 | 1,63650 | €272,47 | €817,41 | €50,63 | €12,27 |
| 1H Fast Long Btc 1 3 Cap75 V1 | DOGE | LONG | Momentum / breakout | 60m | 3,0x | 0,09162 | 0,09232 | 0,08782 | 0,06154 | 0,09732 | €406,05 | €1.218,14 | €50,55 | €9,33 |
| 1H Fast Long Btc 1 3 Cap75 V1 | PUMP | LONG | Momentum / breakout | 60m | 3,0x | 0,00516 | 0,00516 | 0,00489 | 0,00347 | 0,00557 | €9,37 | €28,12 | €1,47 | €0,00 |
| 1H Fast No Pepe V1 | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €172,22 | €516,67 | €49,86 | €0,00 |
| 1H Fast No Pepe V1 | TAO | LONG | Momentum / breakout | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €47,93 | €143,78 | €4,27 | €0,00 |
| 1H Fast No Pepe V1 | XRP | LONG | Momentum / breakout | 60m | 3,0x | 1,49835 | 1,51986 | 1,43358 | 1,00639 | 1,59551 | €415,25 | €1.245,74 | €53,85 | €17,88 |
| 1H Fast No Pepe V1 | PUMP | LONG | Momentum / breakout | 60m | 3,0x | 0,00515 | 0,00515 | 0,00480 | 0,00346 | 0,00567 | €266,74 | €800,21 | €53,85 | €0,00 |
| 1H Fast No Pepe V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14742 | 0,14726 | 0,16511 | 0,19582 | 0,12088 | €136,27 | €408,80 | €49,06 | €0,45 |
| 1H Fast No Pepe V1 | SOL | LONG | Momentum / breakout | 60m | 3,0x | 102,05441 | 101,76000 | 99,81063 | 68,54654 | 105,42008 | €8,75 | €26,26 | €0,58 | €-0,08 |
| 1H Fast No Pepe V1 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04446 | 0,04309 | 0,04980 | 0,05906 | 0,03646 | €9,48 | €28,43 | €3,41 | €0,88 |
| 1H Fast Tp2 V1 | BTW | LONG | Momentum / breakout | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,56752 | €142,85 | €428,56 | €50,25 | €0,00 |
| 1H Fast Tp2 V1 | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00132 | 0,00132 | 0,00119 | 0,00088 | 0,00158 | €18,87 | €56,62 | €5,59 | €0,00 |
| 1H Fast Tp2 V1 | DOGE | LONG | Momentum / breakout | 60m | 3,0x | 0,09162 | 0,09232 | 0,08782 | 0,06154 | 0,09922 | €9,51 | €28,53 | €1,18 | €0,22 |
| 1H Fast Tp2 V1 | PUMP | LONG | Momentum / breakout | 60m | 3,0x | 0,00515 | 0,00515 | 0,00484 | 0,00346 | 0,00576 | €261,16 | €783,47 | €46,57 | €0,00 |
| 1H Fast Tp2 V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,17246 | 0,14726 | 0,17246 | 0,22908 | 0,13107 | €139,71 | €419,14 | €0,00 | €61,24 |
| 1H Fast Tp2 V1 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04446 | 0,04309 | 0,04980 | 0,05906 | 0,03379 | €141,13 | €423,40 | €50,81 | €13,06 |
| 1H Fast Tp2 V1 | ZEC | LONG | Momentum / breakout | 60m | 3,0x | 851,19020 | 851,02000 | 823,36650 | 571,71609 | 906,83762 | €24,68 | €74,03 | €2,42 | €-0,01 |
| Rapida 1H V3 Filtered | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €172,00 | €515,99 | €49,79 | €0,00 |
| Rapida 1H V3 Filtered | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €589,98 | €1.769,95 | €52,56 | €0,00 |
| Rapida 1H V3 Filtered | PUMP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00522 | 0,00522 | 0,00488 | 0,00351 | 0,00573 | €262,56 | €787,69 | €51,10 | €0,00 |
| Rapida 1H V3 Filtered | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14742 | 0,14726 | 0,16511 | 0,19582 | 0,12088 | €140,02 | €420,06 | €50,41 | €0,46 |
| Rapida 1H V3 Filtered | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04446 | 0,04309 | 0,04980 | 0,05906 | 0,03646 | €16,99 | €50,96 | €6,11 | €1,57 |
| 1H Fast V3 Long Only V1 | BTW | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €126,57 | €379,72 | €44,52 | €0,00 |
| 1H Fast V3 Long Only V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00147 | €9,56 | €28,69 | €2,66 | €0,00 |
| 1H Fast V3 Long Only V1 | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €554,42 | €1.663,26 | €49,39 | €0,00 |
| 1H Fast V3 Long Only V1 | PUMP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00522 | 0,00522 | 0,00488 | 0,00351 | 0,00573 | €229,21 | €687,62 | €44,60 | €0,00 |
| 1H Fast V3 Long Only V1 | XRP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,52803 | 1,51986 | 1,48824 | 1,02632 | 1,58771 | €599,35 | €1.798,06 | €46,82 | €-9,61 |
| 1H Fast V3 Long Only V1 | BTC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 80475,97198 | 80459,88000 | 79500,84060 | 54053,02784 | 81938,66944 | €132,39 | €397,17 | €4,81 | €-0,08 |
| 1H Fast V3 No Esports V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €169,36 | €508,09 | €49,03 | €0,00 |
| 1H Fast V3 No Esports V1 | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €27,04 | €81,13 | €2,41 | €0,00 |
| 1H Fast V3 No Esports V1 | PUMP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00522 | 0,00522 | 0,00488 | 0,00351 | 0,00573 | €252,96 | €758,88 | €49,23 | €0,00 |
| 1H Fast V3 No Esports V1 | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14742 | 0,14726 | 0,16511 | 0,19582 | 0,12088 | €133,96 | €401,88 | €48,23 | €0,44 |
| 1H Fast V3 No Esports V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04446 | 0,04309 | 0,04980 | 0,05906 | 0,03646 | €129,73 | €389,20 | €46,70 | €12,00 |
| 1H Fast V3 No Esports Long Only V1 | BTW | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €132,94 | €398,81 | €46,76 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00147 | €10,06 | €30,18 | €2,80 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | PUMP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00522 | 0,00522 | 0,00488 | 0,00351 | 0,00573 | €249,75 | €749,26 | €48,60 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | BTC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 80355,23783 | 80459,88000 | 79356,94052 | 53971,93475 | 81852,68421 | €1.345,04 | €4.035,12 | €50,13 | €5,25 |
| 1H Fast V3 No Esports Mfe Lock V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €173,11 | €519,32 | €50,11 | €0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €593,79 | €1.781,38 | €52,90 | €0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | PUMP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00522 | 0,00522 | 0,00488 | 0,00351 | 0,00573 | €264,26 | €792,79 | €51,43 | €0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14742 | 0,14726 | 0,16511 | 0,19582 | 0,12088 | €140,93 | €422,78 | €50,73 | €0,46 |
| 1H Fast V3 No Esports Mfe Lock V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04446 | 0,04309 | 0,04980 | 0,05906 | 0,03646 | €17,09 | €51,28 | €6,15 | €1,58 |
| Ampia 4H | SPCX | LONG | Confluenza trend | 240m | 2,0x | 136,56189 | 136,56189 | 126,46637 | 68,96375 | 164,82935 | €323,86 | €647,73 | €47,88 | €0,00 |
| Ampia 4H | VELVET | LONG | Confluenza trend | 240m | 2,0x | 0,55987 | 0,14726 | 0,49269 | 0,28274 | 0,74799 | €201,63 | €403,26 | €48,39 | €-297,19 |
| Ampia 4H | LINK | LONG | Confluenza trend | 240m | 2,0x | 11,96839 | 11,96839 | 11,08055 | 6,04404 | 14,45436 | €14,07 | €28,15 | €2,09 | €0,00 |
| Ampia 4H | SUI | LONG | Confluenza trend | 240m | 2,0x | 0,86357 | 0,82350 | 0,75994 | 0,43610 | 1,15373 | €215,46 | €430,92 | €51,71 | €-20,00 |
| Ampia 4H | ETH | LONG | Confluenza trend | 240m | 2,0x | 2430,03591 | 2498,90000 | 2267,54364 | 1227,16813 | 2885,01426 | €18,82 | €37,65 | €2,52 | €1,07 |
| Ampia 4H | HYPE | LONG | Confluenza trend | 240m | 2,0x | 79,31286 | 81,10800 | 70,73982 | 40,05299 | 103,31737 | €13,82 | €27,64 | €2,99 | €0,63 |
| Ampia 4H | TRUMP | LONG | Confluenza trend | 240m | 2,0x | 2,37347 | 2,37347 | 2,08866 | 1,19860 | 3,17096 | €210,83 | €421,66 | €50,60 | €0,00 |
| Forza relativa 1H V2 | BEAT | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,25984 | 0,25984 | 0,25657 | 0,38847 | 0,19125 | €200,38 | €400,75 | €0,00 | €-0,00 |
| Forza relativa 1H V2 | PEPE | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €286,19 | €572,37 | €49,83 | €5,22 |
| Forza relativa 1H V2 | PUMP | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,00510 | 0,00510 | 0,00476 | 0,00258 | 0,00586 | €356,70 | €713,40 | €47,79 | €0,00 |
| Forza relativa 1H V2 | SOL | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 98,65773 | 101,76000 | 100,09761 | 49,82215 | 104,16036 | €963,68 | €1.927,37 | €0,00 | €60,61 |
| Benchmark Donchian breakout 1H | SKHYNIX | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1174,33482 | 1174,33482 | 1128,44989 | 593,03908 | 1289,04713 | €641,25 | €1.282,50 | €50,11 | €0,00 |
| Benchmark Donchian breakout 1H | PUMP | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,00522 | 0,00522 | 0,00474 | 0,00264 | 0,00643 | €312,08 | €624,15 | €57,84 | €0,00 |
| Benchmark Donchian breakout 1H | VELVET | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,14787 | 0,14726 | 0,16561 | 0,22107 | 0,10351 | €237,23 | €474,47 | €56,94 | €1,96 |
| Benchmark Donchian breakout 1H | SOL | LONG | Donchian breakout 20 barre | 60m | 2,0x | 98,65773 | 101,76000 | 99,95358 | 49,82215 | 105,60549 | €1.006,88 | €2.013,76 | €0,00 | €63,32 |
| Benchmark Donchian breakout 1H | BTC | LONG | Donchian breakout 20 barre | 60m | 2,0x | 80839,33463 | 80459,88000 | 79396,75347 | 40823,86399 | 84445,78834 | €211,17 | €422,35 | €7,54 | €-1,98 |
| Donchian 1H Gb20 120R V1 | SKHYNIX | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1174,33482 | 1174,33482 | 1128,44989 | 593,03908 | 1289,04713 | €626,15 | €1.252,30 | €48,93 | €0,00 |
| Donchian 1H Gb20 120R V1 | PUMP | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,00522 | 0,00522 | 0,00474 | 0,00264 | 0,00643 | €304,73 | €609,46 | €56,48 | €0,00 |
| Donchian 1H Gb20 120R V1 | VELVET | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,14787 | 0,14726 | 0,16561 | 0,22107 | 0,10351 | €231,65 | €463,30 | €55,60 | €1,91 |
| Donchian 1H Gb20 120R V1 | SOL | LONG | Donchian breakout 20 barre | 60m | 2,0x | 98,65773 | 101,76000 | 99,95358 | 49,82215 | 105,60549 | €983,17 | €1.966,35 | €0,00 | €61,83 |
| Donchian 1H Gb20 120R V1 | BTC | LONG | Donchian breakout 20 barre | 60m | 2,0x | 80839,33463 | 80459,88000 | 79396,75347 | 40823,86399 | 84445,78834 | €206,20 | €412,40 | €7,36 | €-1,94 |
| Benchmark trend following EMA 1H | BEAT | SHORT | Trend following EMA | 60m | 2,0x | 0,28257 | 0,28257 | 0,25706 | 0,42244 | 0,20797 | €186,11 | €372,23 | €0,00 | €-0,00 |
| Benchmark trend following EMA 1H | SOL | LONG | Trend following EMA | 60m | 2,0x | 95,05001 | 101,76000 | 98,17475 | 48,00025 | 106,18327 | €434,46 | €868,92 | €0,00 | €61,34 |
| Benchmark trend following EMA 1H | ZEC | LONG | Trend following EMA | 60m | 2,0x | 807,93155 | 851,02000 | 730,11531 | 408,00543 | 979,12728 | €17,42 | €34,84 | €3,36 | €1,86 |
| Benchmark trend following EMA 1H | ETH | LONG | Trend following EMA | 60m | 2,0x | 2495,82907 | 2498,90000 | 2437,60814 | 1260,39368 | 2623,91511 | €980,54 | €1.961,08 | €45,75 | €2,41 |
| Benchmark trend following EMA 1H | TUT | SHORT | Trend following EMA | 60m | 2,0x | 0,04446 | 0,04309 | 0,04980 | 0,06647 | 0,03272 | €194,70 | €389,39 | €46,73 | €12,01 |
| Scanner Top 5 Long 1H | BOME | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00160 | €218,24 | €436,47 | €52,38 | €0,00 |
| Scanner Top 5 Long 1H | PEPE | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €322,02 | €644,04 | €56,06 | €5,87 |
| Scanner Top 5 Long 1H | PUMP | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,00502 | 0,00502 | 0,00460 | 0,00254 | 0,00587 | €316,31 | €632,61 | €53,01 | €0,00 |
| Scanner Top 5 Long 1H | TRUMP | LONG | Scanner Top 5 Long | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,08367 | €238,89 | €477,78 | €55,13 | €0,00 |
| Scanner Top 5 Long 1H | ETH | LONG | Scanner Top 5 Long | 60m | 2,0x | 2496,21914 | 2498,90000 | 2449,86508 | 1260,59067 | 2588,92725 | €109,04 | €218,08 | €4,05 | €0,23 |
| Scanner Bottom 5 Short 1H | SOXL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €378,86 | €757,72 | €48,07 | €-0,00 |
| Scanner Bottom 5 Short 1H | SNDK | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €492,80 | €985,60 | €47,71 | €-0,00 |
| Scanner Bottom 5 Short 1H | VELVET | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,17246 | 0,14726 | 0,17246 | 0,25782 | 0,13107 | €191,07 | €382,14 | €0,00 | €55,83 |
| Scanner Bottom 5 Short 1H | TUT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,04570 | 0,04309 | 0,05118 | 0,06832 | 0,03473 | €178,38 | €356,76 | €42,81 | €20,38 |
| Scanner Top10 Long | TAO | LONG | Scanner Top10 Long | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €678,43 | €1.356,86 | €51,81 | €0,00 |
| Scanner Top10 Long | PEPE | LONG | Scanner Top10 Long | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €288,77 | €577,53 | €50,27 | €5,26 |
| Scanner Top10 Long | BTC | LONG | Scanner Top10 Long | 60m | 2,0x | 79476,50212 | 80459,88000 | 79941,98781 | 40135,63357 | 82107,82923 | €1.566,56 | €3.133,13 | €0,00 | €38,77 |
| Scanner Top10 Long | ETH | LONG | Scanner Top10 Long | 60m | 2,0x | 2496,21914 | 2498,90000 | 2449,86508 | 1260,59067 | 2588,92725 | €1.395,14 | €2.790,29 | €51,81 | €3,00 |
| Scanner Top10 Long | SOL | LONG | Scanner Top10 Long | 60m | 2,0x | 101,35627 | 101,76000 | 98,29373 | 51,18491 | 107,48134 | €47,69 | €95,37 | €2,88 | €0,38 |
| Scanner Bottom10 Short | SOXL | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom10 Short | SNDK | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Bottom10 Short | VELVET | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,17246 | 0,14726 | 0,17246 | 0,25782 | 0,13107 | €194,19 | €388,38 | €0,00 | €56,74 |
| Scanner Bottom10 Short | TUT | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,04570 | 0,04309 | 0,05118 | 0,06832 | 0,03473 | €181,31 | €362,61 | €43,51 | €20,72 |
| Scanner Top15 Long | NEAR | LONG | Scanner Top15 Long | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €16,79 | €33,59 | €1,21 | €0,00 |
| Scanner Top15 Long | TAO | LONG | Scanner Top15 Long | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €88,53 | €177,07 | €6,76 | €0,00 |
| Scanner Top15 Long | PEPE | LONG | Scanner Top15 Long | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €291,03 | €582,05 | €50,67 | €5,31 |
| Scanner Top15 Long | PUMP | LONG | Scanner Top15 Long | 60m | 2,0x | 0,00502 | 0,00502 | 0,00460 | 0,00254 | 0,00587 | €291,59 | €583,18 | €48,87 | €0,00 |
| Scanner Top15 Long | TRUMP | LONG | Scanner Top15 Long | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,08367 | €215,87 | €431,75 | €49,81 | €0,00 |
| Scanner Top15 Long | BTC | LONG | Scanner Top15 Long | 60m | 2,0x | 79476,50212 | 80459,88000 | 79941,98781 | 40135,63357 | 82107,82923 | €100,15 | €200,30 | €0,00 | €2,48 |
| Scanner Top15 Long | ETH | LONG | Scanner Top15 Long | 60m | 2,0x | 2493,81866 | 2498,90000 | 2436,64076 | 1259,37843 | 2608,17446 | €837,36 | €1.674,71 | €38,40 | €3,41 |
| Scanner Bottom15 Short | SOXL | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom15 Short | SNDK | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Bottom15 Short | VELVET | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,17246 | 0,14726 | 0,17246 | 0,25782 | 0,13107 | €194,19 | €388,38 | €0,00 | €56,74 |
| Scanner Bottom15 Short | TUT | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,04570 | 0,04309 | 0,05118 | 0,06832 | 0,03473 | €181,31 | €362,61 | €43,51 | €20,72 |
| Scanner Top20 Long | NEAR | LONG | Scanner Top20 Long | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €16,79 | €33,59 | €1,21 | €0,00 |
| Scanner Top20 Long | TAO | LONG | Scanner Top20 Long | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €88,53 | €177,07 | €6,76 | €0,00 |
| Scanner Top20 Long | PEPE | LONG | Scanner Top20 Long | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €291,03 | €582,05 | €50,67 | €5,31 |
| Scanner Top20 Long | PUMP | LONG | Scanner Top20 Long | 60m | 2,0x | 0,00502 | 0,00502 | 0,00460 | 0,00254 | 0,00587 | €291,59 | €583,18 | €48,87 | €0,00 |
| Scanner Top20 Long | TRUMP | LONG | Scanner Top20 Long | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,08367 | €215,87 | €431,75 | €49,81 | €0,00 |
| Scanner Top20 Long | BTC | LONG | Scanner Top20 Long | 60m | 2,0x | 79476,50212 | 80459,88000 | 79941,98781 | 40135,63357 | 82107,82923 | €100,15 | €200,30 | €0,00 | €2,48 |
| Scanner Top20 Long | ETH | LONG | Scanner Top20 Long | 60m | 2,0x | 2493,81866 | 2498,90000 | 2436,64076 | 1259,37843 | 2608,17446 | €837,36 | €1.674,71 | €38,40 | €3,41 |
| Scanner Bottom20 Short | SOXL | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom20 Short | SNDK | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Bottom20 Short | VELVET | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,17246 | 0,14726 | 0,17246 | 0,25782 | 0,13107 | €194,19 | €388,38 | €0,00 | €56,74 |
| Scanner Bottom20 Short | TUT | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,04570 | 0,04309 | 0,05118 | 0,06832 | 0,03473 | €181,31 | €362,61 | €43,51 | €20,72 |
| Scanner Top 5 + forza BTC 1H | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €203,45 | €406,91 | €48,83 | €0,00 |
| Scanner Top 5 + forza BTC 1H | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €300,64 | €601,28 | €52,34 | €5,48 |
| Scanner Top 5 + forza BTC 1H | PUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00502 | 0,00502 | 0,00460 | 0,00254 | 0,00595 | €295,30 | €590,60 | €49,49 | €0,00 |
| Scanner Top 5 + forza BTC 1H | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,14149 | €223,03 | €446,06 | €51,47 | €0,00 |
| Scanner Top 5 + forza BTC 1H | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 101,35627 | 101,76000 | 98,29373 | 51,18491 | 108,09385 | €69,28 | €138,55 | €4,19 | €0,55 |
| Scanner Top5 Btc Mfe V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €190,73 | €381,46 | €45,77 | €0,00 |
| Scanner Top5 Btc Mfe V1 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €281,84 | €563,67 | €49,07 | €5,14 |
| Scanner Top5 Btc Mfe V1 | PUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00502 | 0,00502 | 0,00460 | 0,00254 | 0,00595 | €276,83 | €553,66 | €46,39 | €0,00 |
| Scanner Top5 Btc Mfe V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,14149 | €209,08 | €418,16 | €48,25 | €0,00 |
| Scanner Top5 Btc Mfe V1 | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 101,35627 | 101,76000 | 98,29373 | 51,18491 | 108,09385 | €64,94 | €129,89 | €3,92 | €0,52 |
| Scanner Top5 Btc Guard V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €197,27 | €394,55 | €47,35 | €0,00 |
| Scanner Top5 Btc Guard V1 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €34,88 | €69,75 | €6,07 | €0,64 |
| Scanner Top5 Btc Guard V1 | PUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00502 | 0,00502 | 0,00460 | 0,00254 | 0,00595 | €276,09 | €552,19 | €46,27 | €0,00 |
| Scanner Top5 Btc Guard V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,55551 | 2,55551 | 2,29388 | 1,29053 | 3,13109 | €13,03 | €26,06 | €2,67 | €0,00 |
| Scanner Top5 Btc Guard V1 | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 101,35627 | 101,76000 | 98,29373 | 51,18491 | 108,09385 | €811,17 | €1.622,33 | €49,02 | €6,46 |
| Scanner Top5 Btc Btc Le3 V1 | XRP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,50701 | 1,51986 | 1,39078 | 0,76104 | 1,76273 | €297,64 | €595,28 | €45,91 | €5,08 |
| Scanner Top5 Btc Btc Le3 V1 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €298,93 | €597,86 | €44,42 | €30,23 |
| Scanner Top5 Btc Btc Le3 V1 | PUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00527 | 0,00527 | 0,00486 | 0,00266 | 0,00618 | €14,29 | €28,58 | €2,23 | €0,00 |
| Scanner Top5 Btc Btc 2 3 V1 | XRP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,50701 | 1,51986 | 1,39078 | 0,76104 | 1,76273 | €312,93 | €625,85 | €48,27 | €5,34 |
| Scanner Top5 Btc Btc 2 3 V1 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €314,28 | €628,56 | €46,70 | €31,78 |
| Scanner Top5 Btc Btc 2 3 V1 | PUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00527 | 0,00527 | 0,00486 | 0,00266 | 0,00618 | €15,02 | €30,05 | €2,35 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €192,69 | €385,37 | €46,24 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €34,07 | €68,13 | €5,93 | €0,62 |
| Scanner Top5 Btc Guard Mfe V1 | PUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00502 | 0,00502 | 0,00460 | 0,00254 | 0,00595 | €269,67 | €539,35 | €45,19 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,55551 | 2,55551 | 2,29388 | 1,29053 | 3,13109 | €12,72 | €25,45 | €2,61 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 101,35627 | 101,76000 | 98,29373 | 51,18491 | 108,09385 | €792,30 | €1.584,60 | €47,88 | €6,31 |
| Scanner Top5 Btc Guard Btc Le3 V1 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €313,56 | €627,12 | €46,59 | €31,71 |
| Scanner Top5 Btc Guard Btc Le3 V1 | XRP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,49793 | 1,51986 | 1,40541 | 0,75645 | 1,70147 | €13,15 | €26,30 | €1,62 | €0,38 |
| Scanner Top5 Btc Guard Btc Le3 V1 | PUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00502 | 0,00502 | 0,00460 | 0,00254 | 0,00595 | €273,00 | €546,00 | €45,75 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,55551 | 2,55551 | 2,29388 | 1,29053 | 3,13109 | €12,70 | €25,40 | €2,60 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €308,18 | €616,36 | €45,79 | €31,16 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | XRP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,49793 | 1,51986 | 1,40541 | 0,75645 | 1,70147 | €12,92 | €25,84 | €1,60 | €0,38 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | PUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00502 | 0,00502 | 0,00460 | 0,00254 | 0,00595 | €268,32 | €536,63 | €44,97 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00176 | €210,95 | €421,90 | €50,63 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 818,21361 | 851,02000 | 764,43439 | 413,19787 | 979,55127 | €17,50 | €35,00 | €2,30 | €1,40 |
| Scanner Top5 Btc Runner25 V1 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00001 | €303,79 | €607,58 | €52,89 | €5,54 |
| Scanner Top5 Btc Runner25 V1 | PUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00502 | 0,00502 | 0,00460 | 0,00254 | 0,00629 | €300,08 | €600,16 | €50,29 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 101,35627 | 101,76000 | 98,29373 | 51,18491 | 110,54388 | €861,88 | €1.723,75 | €52,08 | €6,87 |
| Scanner Top5 Btc Tp3 V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00176 | €211,07 | €422,14 | €50,66 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 818,21361 | 851,02000 | 764,43439 | 413,19787 | 979,55127 | €17,51 | €35,02 | €2,30 | €1,40 |
| Scanner Top5 Btc Tp3 V1 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00001 | €303,97 | €607,94 | €52,92 | €5,54 |
| Scanner Top5 Btc Tp3 V1 | PUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00502 | 0,00502 | 0,00460 | 0,00254 | 0,00629 | €300,25 | €600,51 | €50,32 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 101,35627 | 101,76000 | 98,29373 | 51,18491 | 110,54388 | €862,38 | €1.724,76 | €52,11 | €6,87 |
| Combo Trend | BEAT | SHORT | Combo Trend | 60m | 2,0x | 0,25984 | 0,25984 | 0,25657 | 0,38847 | 0,19125 | €193,71 | €387,42 | €0,00 | €-0,00 |
| Combo Trend | ZEC | LONG | Combo Trend | 60m | 2,0x | 807,93155 | 851,02000 | 730,11531 | 408,00543 | 979,12728 | €247,61 | €495,23 | €47,70 | €26,41 |
| Combo Trend | PEPE | LONG | Combo Trend | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00001 | €246,56 | €493,12 | €47,70 | €4,50 |
| Combo Trend | PUMP | LONG | Combo Trend | 60m | 2,0x | 0,00498 | 0,00498 | 0,00455 | 0,00252 | 0,00595 | €266,27 | €532,54 | €46,71 | €0,00 |
| Combo Trend | BTC | LONG | Combo Trend | 60m | 2,0x | 80839,33463 | 80459,88000 | 79396,75347 | 40823,86399 | 84013,01416 | €27,80 | €55,60 | €0,99 | €-0,26 |
| Combo Mean Reversion | BTC | SHORT | Combo Mean Reversion | 60m | 2,0x | 80807,00537 | 80459,88000 | 81888,50855 | 120806,47302 | 79076,60011 | €1.684,34 | €3.368,67 | €45,09 | €14,47 |
| Combo Scanner | BOME | LONG | Combo Scanner | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €195,20 | €390,40 | €46,85 | €0,00 |
| Combo Scanner | PEPE | LONG | Combo Scanner | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €288,44 | €576,88 | €50,22 | €5,26 |
| Combo Scanner | PUMP | LONG | Combo Scanner | 60m | 2,0x | 0,00502 | 0,00502 | 0,00460 | 0,00254 | 0,00595 | €283,32 | €566,63 | €47,48 | €0,00 |
| Combo Scanner | TRUMP | LONG | Combo Scanner | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,14149 | €213,98 | €427,96 | €49,38 | €0,00 |
| Combo Scanner | SOL | LONG | Combo Scanner | 60m | 2,0x | 101,35627 | 101,76000 | 98,29373 | 51,18491 | 108,09385 | €66,47 | €132,93 | €4,02 | €0,53 |
| Combo Adaptive | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,01735 | 121,01735 | 128,90956 | 180,92093 | 105,23292 | €367,30 | €734,61 | €47,91 | €-0,00 |
| Combo Adaptive | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €40,89 | €81,77 | €3,12 | €0,00 |
| Combo Adaptive | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 807,93155 | 851,02000 | 737,89694 | 408,00543 | 948,00078 | €307,94 | €615,88 | €53,39 | €32,85 |
| Combo Adaptive | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €306,63 | €613,26 | €53,38 | €5,59 |
| Combo Adaptive | PUMP | LONG | Combo Adaptive | 60m | 2,0x | 0,00520 | 0,00520 | 0,00478 | 0,00262 | 0,00604 | €329,34 | €658,69 | €53,47 | €0,00 |
| Combo Adaptive | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,52450 | 2,33981 | 1,27487 | 2,89389 | €18,69 | €37,37 | €2,73 | €0,00 |
| Combo Adaptive | BTC | LONG | Combo Adaptive | 60m | 2,0x | 80839,33463 | 80459,88000 | 79541,01127 | 40823,86399 | 83435,98137 | €39,76 | €79,52 | €1,28 | €-0,37 |
| Combo Adaptive Mfe Trail | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €54,29 | €108,58 | €4,15 | €0,00 |
| Combo Adaptive Mfe Trail | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €269,51 | €539,03 | €46,92 | €4,91 |
| Combo Adaptive Mfe Trail | XRP | LONG | Combo Adaptive | 60m | 2,0x | 1,49835 | 1,51986 | 1,41507 | 0,75667 | 1,66491 | €363,44 | €726,87 | €40,40 | €10,44 |
| Combo Adaptive Mfe Trail | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,52450 | 2,33981 | 1,27487 | 2,89389 | €315,75 | €631,50 | €46,20 | €0,00 |
| Combo Adaptive Mfe Trail | TUT | SHORT | Combo Adaptive | 60m | 2,0x | 0,04570 | 0,04309 | 0,05118 | 0,06832 | 0,03473 | €190,04 | €380,09 | €45,61 | €21,71 |
| Combo Adaptive Mfe Trail | BTC | LONG | Combo Adaptive | 60m | 2,0x | 80839,33463 | 80459,88000 | 79541,01127 | 40823,86399 | 83435,98137 | €21,40 | €42,79 | €0,69 | €-0,20 |
| Combo Adaptive Quality7 V1 | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €371,68 | €743,36 | €47,16 | €-0,00 |
| Combo Adaptive Quality7 V1 | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €646,78 | €1.293,57 | €49,39 | €0,00 |
| Combo Adaptive Quality7 V1 | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €283,16 | €566,31 | €49,30 | €5,16 |
| Combo Adaptive Quality7 V1 | PUMP | LONG | Combo Adaptive | 60m | 2,0x | 0,00520 | 0,00520 | 0,00478 | 0,00262 | 0,00604 | €302,38 | €604,77 | €49,09 | €0,00 |
| Combo Adaptive Regime V1 | PUMP | LONG | Combo Adaptive | 60m | 2,0x | 0,00502 | 0,00502 | 0,00460 | 0,00254 | 0,00587 | €294,95 | €589,90 | €49,43 | €0,00 |
| Combo Adaptive Regime V1 | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €425,38 | €850,76 | €0,00 | €31,51 |
| Combo Adaptive Quality7 Regime V1 | PUMP | LONG | Combo Adaptive | 60m | 2,0x | 0,00502 | 0,00502 | 0,00460 | 0,00254 | 0,00587 | €295,78 | €591,56 | €49,57 | €0,00 |
| Combo Adaptive Long Only V1 | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €645,48 | €1.290,95 | €46,47 | €0,00 |
| Combo Adaptive Long Only V1 | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €308,39 | €616,77 | €53,69 | €5,62 |
| Combo Adaptive Long Only V1 | PUMP | LONG | Combo Adaptive | 60m | 2,0x | 0,00502 | 0,00502 | 0,00460 | 0,00254 | 0,00587 | €312,68 | €625,36 | €52,40 | €0,00 |
| Combo Adaptive Long Only V1 | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,52450 | 2,33981 | 1,27487 | 2,89389 | €48,12 | €96,24 | €7,04 | €0,00 |
| Combo Adaptive Long Only V1 | BTC | LONG | Combo Adaptive | 60m | 2,0x | 80839,33463 | 80459,88000 | 79541,01127 | 40823,86399 | 83435,98137 | €1.627,32 | €3.254,65 | €52,27 | €-15,28 |
| Combo Adaptive Partial 1R V1 | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,01735 | 121,01735 | 128,90956 | 180,92093 | 105,23292 | €352,70 | €705,40 | €46,00 | €-0,00 |
| Combo Adaptive Partial 1R V1 | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €292,79 | €585,58 | €50,97 | €5,34 |
| Combo Adaptive Partial 1R V1 | PUMP | LONG | Combo Adaptive | 60m | 2,0x | 0,00502 | 0,00502 | 0,00460 | 0,00254 | 0,00587 | €16,58 | €33,16 | €2,78 | €0,00 |
| Combo Adaptive Partial 1R V1 | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,52450 | 2,33981 | 1,27487 | 2,89389 | €347,19 | €694,38 | €50,80 | €0,00 |
| Combo Adaptive Partial 1R V1 | VELVET | SHORT | Combo Adaptive | 60m | 2,0x | 0,17246 | 0,14726 | 0,17246 | 0,25782 | 0,13107 | €207,76 | €415,52 | €0,00 | €60,71 |
| Combo Adaptive Partial 1R V1 | SOL | LONG | Combo Adaptive | 60m | 2,0x | 100,45609 | 101,76000 | 97,46723 | 50,73032 | 106,43381 | €39,62 | €79,24 | €2,36 | €1,03 |
| Combo Adaptive Partial 1R V1 | BTC | LONG | Combo Adaptive | 60m | 2,0x | 80839,33463 | 80459,88000 | 79541,01127 | 40823,86399 | 83435,98137 | €20,55 | €41,09 | €0,66 | €-0,19 |
| Combo Adaptive Quality7 Regime Partial 1R V1 | PUMP | LONG | Combo Adaptive | 60m | 2,0x | 0,00502 | 0,00502 | 0,00460 | 0,00254 | 0,00587 | €299,55 | €599,09 | €50,20 | €0,00 |
| Btc Ema 1H | BTC | LONG | Trend following EMA | 60m | 3,0x | 80839,33463 | 80459,88000 | 79541,01127 | 54297,08643 | 83435,98137 | €1.031,72 | €3.095,15 | €49,71 | €-14,53 |
| Btc Ema 4H | BTC | LONG | Trend following EMA | 240m | 2,0x | 80355,23783 | 80459,88000 | 77497,66656 | 40579,39511 | 87499,16561 | €704,37 | €1.408,74 | €50,10 | €1,83 |
| Btc Donchian 1H | BTC | LONG | Donchian breakout 20 barre | 60m | 3,0x | 80839,33463 | 80459,88000 | 79685,26906 | 54297,08643 | 83147,46498 | €1.175,39 | €3.526,17 | €50,34 | €-16,55 |
| Btc Donchian 4H | BTC | LONG | Donchian breakout 20 barre | 240m | 2,0x | 80355,23783 | 80459,88000 | 77497,66656 | 40579,39511 | 88356,43707 | €700,60 | €1.401,20 | €49,83 | €1,82 |
| Btc Bollinger 1H | BTC | SHORT | Bollinger mean reversion | 60m | 3,0x | 80807,00537 | 80459,88000 | 81888,50855 | 107338,63879 | 79184,74978 | €1.262,52 | €3.787,57 | €50,69 | €16,27 |
| Btc Bollinger 4H | BTC | SHORT | Bollinger mean reversion | 240m | 2,0x | 80323,10217 | 80459,88000 | 82919,85488 | 120083,03774 | 75648,94663 | €775,58 | €1.551,16 | €50,15 | €-2,64 |
| Btc Adaptive 1H | BTC | LONG | Combo Adaptive | 60m | 3,0x | 80839,33463 | 80459,88000 | 79541,01127 | 54297,08643 | 83435,98137 | €1.045,87 | €3.137,61 | €50,39 | €-14,73 |
| Btc Adaptive 4H | BTC | LONG | Combo Adaptive | 240m | 2,0x | 80355,23783 | 80459,88000 | 77237,88772 | 40579,39511 | 88148,61352 | €648,94 | €1.297,88 | €50,35 | €1,69 |
| Sol Ema 1H | SOL | LONG | Trend following EMA | 60m | 3,0x | 95,05001 | 101,76000 | 98,99140 | 63,84192 | 104,15904 | €349,20 | €1.047,59 | €0,00 | €73,95 |
| Sol Ema 4H | SOL | LONG | Trend following EMA | 240m | 2,0x | 93,39968 | 101,76000 | 97,35104 | 47,16684 | 109,83325 | €356,10 | €712,19 | €0,00 | €63,75 |
| Sol Adaptive 1H | SOL | LONG | Combo Adaptive | 60m | 3,0x | 95,05001 | 101,76000 | 98,99140 | 63,84192 | 104,15904 | €344,23 | €1.032,69 | €0,00 | €72,90 |
| Sol Adaptive 4H | SOL | LONG | Combo Adaptive | 240m | 2,0x | 93,39968 | 101,76000 | 97,18824 | 47,16684 | 111,32722 | €330,98 | €661,97 | €0,00 | €59,25 |
| Eth Ema 1H | ETH | LONG | Trend following EMA | 60m | 3,0x | 2495,82907 | 2498,90000 | 2443,43023 | 1676,36519 | 2600,62673 | €783,24 | €2.349,73 | €49,33 | €2,89 |
| Eth Ema 4H | ETH | LONG | Trend following EMA | 240m | 2,0x | 2390,02791 | 2498,90000 | 2268,60778 | 1206,96409 | 2693,57826 | €487,73 | €975,47 | €49,56 | €44,44 |
| Doge Ema 1H | DOGE | LONG | Trend following EMA | 60m | 3,0x | 0,09314 | 0,09232 | 0,08689 | 0,06256 | 0,10563 | €248,90 | €746,70 | €50,09 | €-6,56 |
| Master Adaptive Expanded V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04309 | 0,03814 | 0,02188 | 0,05374 | €197,50 | €395,01 | €47,40 | €-2,24 |
| Master Adaptive Runner25 V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04309 | 0,03814 | 0,02188 | 0,05894 | €34,77 | €69,54 | €8,34 | €-0,39 |
| Combo Adaptive Side Regime Guard V1 | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €77,52 | €155,04 | €5,58 | €0,00 |
| Combo Adaptive Side Regime Guard V1 | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 807,93155 | 851,02000 | 737,89694 | 408,00543 | 948,00078 | €305,89 | €611,78 | €53,03 | €32,63 |
| Combo Adaptive Side Regime Guard V1 | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €304,59 | €609,17 | €53,03 | €5,55 |
| Combo Adaptive Side Regime Guard V1 | VELVET | SHORT | Combo Adaptive | 60m | 2,0x | 0,17246 | 0,14726 | 0,17246 | 0,25782 | 0,13107 | €216,61 | €433,23 | €0,00 | €63,29 |
| Combo Adaptive Side Regime Guard V1 | TUT | SHORT | Combo Adaptive | 60m | 2,0x | 0,04570 | 0,04309 | 0,05118 | 0,06832 | 0,03473 | €192,40 | €384,79 | €46,18 | €21,98 |
| Master Adaptive Gb20 Loss Cap V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04309 | 0,03828 | 0,02188 | 0,05682 | €195,70 | €391,41 | €45,67 | €-2,22 |
| Main Side Regime Guard V1 | VELVET | LONG | Confluenza trend | 240m | 3,0x | 0,55987 | 0,14726 | 0,49269 | 0,37605 | 0,69424 | €142,25 | €426,74 | €51,21 | €-314,50 |
| Main Side Regime Guard V1 | AKE | LONG | Confluenza trend | 240m | 3,0x | 0,01021 | 0,01021 | 0,00899 | 0,00686 | 0,01266 | €145,97 | €437,90 | €52,55 | €0,00 |
| Main Side Regime Guard V1 | PUMP | LONG | Confluenza trend | 240m | 3,0x | 0,00468 | 0,00468 | 0,00481 | 0,00314 | 0,00580 | €149,89 | €449,66 | €0,00 | €0,00 |
| Main Side Regime Guard V1 | HYPE | LONG | Confluenza trend | 240m | 3,0x | 77,65853 | 81,10800 | 71,20755 | 52,16065 | 90,56048 | €216,52 | €649,56 | €53,96 | €28,85 |
| Main Side Regime Guard V1 | XRP | LONG | Confluenza trend | 240m | 3,0x | 1,47102 | 1,51986 | 1,31178 | 0,98804 | 1,78951 | €12,77 | €38,31 | €4,15 | €1,27 |
| Main Side Regime Guard V1 | ETH | LONG | Confluenza trend | 240m | 3,0x | 2437,91749 | 2498,90000 | 2326,72117 | 1637,46791 | 2660,31012 | €9,94 | €29,83 | €1,36 | €0,75 |
| Main Dynamic Asset Selector V1 | PUMP | LONG | Confluenza trend | 240m | 3,0x | 0,00515 | 0,00515 | 0,00453 | 0,00346 | 0,00638 | €141,85 | €425,56 | €51,07 | €0,00 |
| Combo Trend Side Regime Guard V1 | ZEC | LONG | Combo Trend | 60m | 2,0x | 822,67450 | 851,02000 | 761,05343 | 415,45062 | 958,24084 | €381,00 | €762,00 | €57,08 | €26,26 |
| Combo Trend Side Regime Guard V1 | PEPE | LONG | Combo Trend | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00001 | €293,50 | €586,99 | €56,78 | €5,35 |
| Combo Trend Side Regime Guard V1 | PUMP | LONG | Combo Trend | 60m | 2,0x | 0,00523 | 0,00523 | 0,00474 | 0,00264 | 0,00631 | €294,84 | €589,68 | €55,15 | €0,00 |
| Combo Trend Side Regime Guard V1 | VELVET | SHORT | Combo Trend | 60m | 2,0x | 0,17246 | 0,14726 | 0,17246 | 0,25782 | 0,12693 | €217,86 | €435,73 | €0,00 | €63,66 |
| Combo Trend Side Regime Guard V1 | TUT | SHORT | Combo Trend | 60m | 2,0x | 0,04570 | 0,04309 | 0,05118 | 0,06832 | 0,03364 | €12,81 | €25,62 | €3,07 | €1,46 |
| 1H Balanced V3 Long Only V1 | SKHYNIX | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1220,85412 | 1220,85412 | 1177,63561 | 820,00702 | 1307,29117 | €435,49 | €1.306,46 | €46,25 | €0,00 |
| 1H Balanced V3 Long Only V1 | ZEC | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 807,93155 | 851,02000 | 737,89694 | 542,66069 | 948,00078 | €184,72 | €554,15 | €48,04 | €29,55 |
| 1H Balanced V3 Long Only V1 | XRP | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1,47399 | 1,51986 | 1,35380 | 0,99003 | 1,71438 | €194,69 | €584,07 | €47,63 | €18,17 |
| 1H Balanced V3 Long Only V1 | PUMP | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,00523 | 0,00523 | 0,00479 | 0,00351 | 0,00611 | €184,35 | €553,04 | €46,55 | €0,00 |
| 1H Balanced V3 Long Only V1 | ETH | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 2484,05671 | 2498,90000 | 2436,27995 | 1668,45809 | 2579,61023 | €50,09 | €150,27 | €2,89 | €0,90 |
| Scanner Bottom5 Short Profit Lock V1 | SOXL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €381,80 | €763,60 | €48,45 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | SNDK | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €496,62 | €993,25 | €48,08 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | VELVET | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,17246 | 0,14726 | 0,17246 | 0,25782 | 0,13107 | €192,55 | €385,10 | €0,00 | €56,26 |
| Scanner Bottom5 Short Profit Lock V1 | TUT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,04570 | 0,04309 | 0,05118 | 0,06832 | 0,03473 | €179,76 | €359,53 | €43,14 | €20,54 |
| Scanner Bottom5 Short Mfe Trail V1 | SOXL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €382,38 | €764,76 | €48,52 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | SNDK | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €497,38 | €994,76 | €48,15 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | VELVET | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,17246 | 0,14726 | 0,17246 | 0,25782 | 0,13107 | €192,85 | €385,69 | €0,00 | €56,35 |
| Scanner Bottom5 Short Mfe Trail V1 | TUT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,04570 | 0,04309 | 0,05118 | 0,06832 | 0,03473 | €180,04 | €360,08 | €43,21 | €20,57 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1H Fast V3 No Esports Long Only V1 | PEPE | LONG | 2026-08-25T04:45:00+00:00 | 0,00000 | €7,20 | 0,14 | STOP |
| 1H Fast V3 Long Only V1 | PEPE | LONG | 2026-08-25T04:45:00+00:00 | 0,00000 | €0,73 | 0,14 | STOP |
| 1H Fast Tp2 V1 | PEPE | LONG | 2026-08-25T04:45:00+00:00 | 0,00000 | €0,35 | 0,14 | STOP |
| 1H Fast V3 No Esports Long Only V1 | XRP | LONG | 2026-08-25T04:00:00+00:00 | 1,51078 | €-0,12 | -0,05 | STOP |
| Benchmark trend following EMA 1H | BTC | LONG | 2026-08-25T02:45:00+00:00 | 81208,84767 | €94,01 | 2,11 | TARGET |
| 1H Fast V3 No Esports V1 | DOGE | SHORT | 2026-08-25T02:30:00+00:00 | 0,09187 | €-49,66 | -1,05 | STOP |
| 1H Fast V3 No Esports Mfe Lock V1 | BTC | LONG | 2026-08-25T02:30:00+00:00 | 80496,33500 | €6,06 | 1,40 | TARGET |
| 1H Fast V3 No Esports Mfe Lock V1 | DOGE | SHORT | 2026-08-25T02:30:00+00:00 | 0,09187 | €-1,49 | -1,05 | STOP |
| 1H Fast V3 No Esports Long Only V1 | BTC | LONG | 2026-08-25T02:30:00+00:00 | 80496,33500 | €68,63 | 1,40 | TARGET |
| 1H Fast V3 Long Only V1 | BTC | LONG | 2026-08-25T02:30:00+00:00 | 80854,53436 | €64,00 | 1,39 | TARGET |
| 1H Fast V3 Cap75 V1 | DOGE | SHORT | 2026-08-25T02:30:00+00:00 | 0,09187 | €-48,14 | -1,05 | STOP |
| Rapida 1H V3 Filtered | BTC | LONG | 2026-08-25T02:30:00+00:00 | 80496,33500 | €6,02 | 1,40 | TARGET |

## Regole invarianti

- Nessuna martingala e nessuna mediazione automatica in perdita.
- Il target mensile riduce il rischio quando viene avvicinato o raggiunto; non lo aumenta mai.
- Il portafoglio principale e le simulazioni di confronto hanno contabilità separata.
- Commissioni, slippage e funding sono inclusi nella simulazione secondo i parametri configurati.
- Quando stop e target risultano toccati nella stessa candela, prevale lo stop salvo modifica esplicita della configurazione.
