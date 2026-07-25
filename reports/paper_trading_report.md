# Paper trading automatico KuCoin

Generato: 2026-07-25T05:15:19+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-07-25T05:08:25+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-07-25T05:08:25+00:00 | 2026-07-25T05:08:25+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-07-25T04:45:00+00:00 | 2026-07-25T04:45:00+00:00 | 8,5 min | 25,0 min | OK |
| 60m | 12 | 2026-07-25T04:00:00+00:00 | 2026-07-25T04:00:00+00:00 | 8,5 min | 45,0 min | OK |
| 240m | 12 | 2026-07-25T00:00:00+00:00 | 2026-07-25T00:00:00+00:00 | 1,14 h | 1,00 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | AKE | 240m | LONG | 7,75 | 6,00 | 0,00 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | BANK | 240m | LONG | 7,75 | 6,00 | 0,00 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | BEAT | 240m | LONG | 7,75 | 6,00 | 0,00 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | HYPE | 240m | SHORT | -7,66 | 6,00 | 0,00 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | DOGE | 240m | SHORT | -6,90 | 6,00 | 0,00 | STALE_CANDLE | 1,14 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | ZEC | 240m | SHORT | -6,02 | 6,00 | 0,00 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | SOL | 240m | SHORT | -5,93 | 6,00 | 0,07 | STALE_CANDLE | 1,14 h | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | PEPE | 240m | SHORT | -5,17 | 6,00 | 0,83 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | ADA | 240m | SHORT | -3,78 | 6,00 | 2,22 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | XRP | 240m | SHORT | -3,60 | 6,00 | 2,40 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | BTC | 240m | SHORT | -1,00 | 6,00 | 5,00 | STALE_CANDLE | 1,14 h | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | ETH | 240m | SHORT | -0,00 | 6,00 | 6,00 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Scanner Top5 Btc Guard Mfe V1 | BEAT | 60m | LONG | 7,75 | 5,00 | 0,00 | READY | 8,5 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | BEAT | 60m | LONG | 7,75 | 5,00 | 0,00 | READY | 8,5 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Scanner Top5 Btc Guard Mfe V1 | AKE | 60m | LONG | 5,50 | 5,00 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | AKE | 60m | LONG | 5,50 | 5,00 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida 1H V1 | BEAT | 60m | LONG | 7,75 | 4,50 | 0,00 | STRATEGY_FILTER | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout UP oppure movimento breve ≥1,5%; breakout=NONE, movimento=+0.65%. |
| 1H Fast Score 6 75 V1 | BEAT | 60m | LONG | 7,75 | 6,00 | 0,00 | STRATEGY_FILTER | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout UP oppure movimento breve ≥1,5%; breakout=NONE, movimento=+0.65%. |
| 1H Fast Score 6 75 No Trend Up V1 | BEAT | 60m | LONG | 7,75 | 6,00 | 0,00 | STRATEGY_FILTER | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout UP oppure movimento breve ≥1,5%; breakout=NONE, movimento=+0.65%. |
| 1H Fast Score 6 75 Range Only V1 | BEAT | 60m | LONG | 7,75 | 6,00 | 0,00 | STRATEGY_FILTER | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout UP oppure movimento breve ≥1,5%; breakout=NONE, movimento=+0.65%. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.939,87 | -0,60% | €-60,13 | €3.000,00 | -2,00% | 4 | 18 | 33,33% | 0,91 | 4,26% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 18 | 532 | CAMPIONE INSUFFICIENTE | 30 (mancano 12) |

- Trade del Principale 4H chiusi: **18**; win rate **33,33%**; profit factor **0,91**.
- Expectancy: **€-2,94** per trade; P&L netto: **€-52,87**; max drawdown: **4,26%**.
- Valutazione: **Servono altri eventi indipendenti prima di trarre conclusioni.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 4 | €9.939,87 | €1.462,87 | €4.388,60 | €148,39 | €-5,53 |
| TEST | Scanner Top 5 Long 1H | 3 | €10.744,02 | €1.312,86 | €2.625,71 | €159,11 | €12,28 |
| TEST | Bilanciata 1H V1 | 4 | €10.508,80 | €2.588,10 | €7.764,31 | €155,73 | €74,09 |
| TEST | Scanner Top 5 + forza BTC 1H | 3 | €10.504,59 | €1.374,15 | €2.748,31 | €156,73 | €12,00 |
| TEST | Bilanciata 1H V3 Filtered | 4 | €10.448,05 | €1.671,12 | €5.013,37 | €51,50 | €69,81 |
| TEST | 1H Fast Score 6 75 V1 | 4 | €10.334,28 | €4.307,29 | €12.921,88 | €153,78 | €54,51 |
| TEST | Benchmark Donchian breakout 1H | 3 | €10.261,19 | €2.587,51 | €5.175,01 | €102,42 | €118,00 |
| TEST | 1H Fast V3 Cap75 V1 | 4 | €10.260,36 | €2.857,87 | €8.573,61 | €101,51 | €80,66 |
| TEST | Combo Adaptive | 3 | €10.232,84 | €2.757,41 | €5.514,81 | €154,10 | €-29,34 |
| TEST | Scanner Top5 Btc Tp3 V1 | 3 | €10.224,92 | €1.281,05 | €2.562,10 | €100,06 | €85,49 |
| TEST | Scanner Top5 Btc Runner25 V1 | 3 | €10.208,39 | €1.321,51 | €2.643,02 | €151,05 | €11,67 |
| TEST | 1H Fast Nohigh Cap75 V1 | 4 | €10.207,34 | €2.843,08 | €8.529,23 | €100,98 | €80,24 |
| TEST | Forza relativa 1H V2 | 4 | €10.196,25 | €1.845,37 | €3.690,73 | €151,43 | €67,90 |
| TEST | Bilanciata 1H V2 | 4 | €10.156,87 | €2.109,13 | €6.327,39 | €100,71 | €71,56 |
| TEST | Rapida 1H V3 Filtered | 3 | €10.118,55 | €1.402,30 | €4.206,89 | €100,70 | €80,34 |
| TEST | Doge Ema 1H | 1 | €10.117,49 | €1.143,65 | €3.430,94 | €50,74 | €-29,01 |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | 3 | €10.117,25 | €1.326,36 | €2.652,73 | €149,34 | €11,56 |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | 4 | €10.116,41 | €2.595,88 | €7.787,65 | €99,70 | €121,08 |
| TEST | 1H Fast Score 6 75 Range Only V1 | 4 | €10.116,41 | €2.595,88 | €7.787,65 | €99,70 | €121,08 |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | 4 | €10.116,41 | €2.595,88 | €7.787,65 | €99,70 | €121,08 |
| TEST | Btc Bollinger 1H | 1 | €10.098,18 | €1.402,77 | €4.208,32 | €50,50 | €1,17 |
| TEST | Sol Donchian 1H | 0 | €10.092,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Benchmark Bollinger mean reversion 1H | 2 | €10.092,09 | €4.030,03 | €8.060,05 | €96,72 | €27,20 |
| TEST | Combo Scanner | 3 | €10.089,69 | €2.776,18 | €5.552,36 | €150,33 | €-28,93 |
| TEST | Scanner Top5 Btc Btc Le3 V1 | 3 | €10.088,68 | €1.341,28 | €2.682,56 | €150,45 | €11,53 |
| TEST | Sol Bollinger 4H | 0 | €10.086,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 4H | 0 | €10.084,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast No Pepe V1 | 3 | €10.062,32 | €1.394,50 | €4.183,51 | €100,14 | €79,89 |
| TEST | Combo Mean Reversion | 2 | €10.042,25 | €3.457,67 | €6.915,35 | €47,97 | €53,53 |
| TEST | 1H Fast V3 Nohigh Range Only V1 | 4 | €10.038,93 | €2.524,68 | €7.574,05 | €200,00 | €43,48 |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | 4 | €10.038,93 | €2.524,68 | €7.574,05 | €200,00 | €43,48 |
| TEST | Master Adaptive Gb20 Loss Cap V1 | 3 | €10.035,62 | €986,43 | €1.972,86 | €149,99 | €36,80 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €10.028,40 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Gb20 Be V1 | 3 | €10.026,29 | €791,91 | €1.583,82 | €99,99 | €27,24 |
| TEST | Master Adaptive Gb20 Partial V1 | 3 | €10.026,29 | €791,91 | €1.583,82 | €149,99 | €27,24 |
| TEST | Combo Adaptive Side Regime Guard V1 | 3 | €10.022,34 | €1.715,54 | €3.431,08 | €149,99 | €24,40 |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | 3 | €10.019,71 | €2.517,28 | €7.551,83 | €150,02 | €32,93 |
| TEST | Combo Trend Side Regime Guard V1 | 2 | €10.015,88 | €435,97 | €871,95 | €100,00 | €16,41 |
| TEST | Main Side Regime Guard V1 | 2 | €10.015,57 | €277,77 | €833,32 | €100,00 | €16,07 |
| TEST | Main Dynamic Asset Selector V1 | 2 | €10.015,57 | €277,77 | €833,32 | €100,00 | €16,07 |
| TEST | Eth Bollinger 1H | 0 | €10.015,45 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 1H | 0 | €10.013,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | 2 | €10.006,64 | €920,72 | €2.762,16 | €99,56 | €21,81 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 0 | €10.005,68 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | 2 | €10.004,56 | €2.268,80 | €6.806,39 | €49,99 | €62,54 |
| TEST | Combo Adaptive Quality7 V1 | 3 | €10.004,50 | €2.804,41 | €5.608,82 | €149,61 | €-18,73 |
| TEST | Sol Ema 1H | 1 | €10.003,31 | €1.161,12 | €3.483,35 | €50,16 | €-26,65 |
| TEST | Combo Adaptive Runner25 V1 | 3 | €10.001,97 | €2.837,64 | €5.675,27 | €149,81 | €-17,11 |
| TEST | Scalp RSI Long 25 · €50 · 15x | 0 | €10.001,47 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €10 · 15x | 0 | €10.000,29 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Balanced Short Trend Down Strict V1 | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
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
| TEST | Ampia 4H | 4 | €9.998,35 | €1.964,72 | €3.929,45 | €149,98 | €16,25 |
| TEST | Scalp RSI Long 20 · prudente · 5x | 0 | €9.996,99 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Balanced Long No Rhv V1 | 3 | €9.996,52 | €504,12 | €1.512,37 | €99,55 | €67,81 |
| TEST | 1H Fast V3 No Esports Long Only V1 | 3 | €9.996,19 | €627,47 | €1.882,42 | €99,47 | €71,56 |
| TEST | Rapida 1H V2 | 3 | €9.993,10 | €2.631,95 | €7.895,85 | €100,03 | €49,95 |
| TEST | Scalp RSI Long 15 · €50 · 15x | 0 | €9.992,50 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Trend | 3 | €9.989,11 | €1.989,63 | €3.979,25 | €150,09 | €-7,89 |
| TEST | Scalp RSI Long 15 · prudente · 5x | 0 | €9.988,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Donchian 4H | 1 | €9.984,38 | €830,21 | €1.660,43 | €49,74 | €37,29 |
| TEST | Sol Adaptive 4H | 1 | €9.981,52 | €761,04 | €1.522,08 | €49,74 | €34,18 |
| TEST | Btc Donchian 1H | 0 | €9.980,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 No Esports V1 | 4 | €9.979,03 | €1.767,37 | €5.302,10 | €197,91 | €58,39 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 0 | €9.976,99 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Regime V1 | 2 | €9.975,22 | €964,46 | €1.928,92 | €98,78 | €0,00 |
| TEST | Eth Donchian 1H | 1 | €9.971,68 | €1.299,81 | €3.899,43 | €49,91 | €-8,55 |
| TEST | Sol Ema 4H | 1 | €9.965,31 | €862,58 | €1.725,17 | €49,74 | €18,36 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.964,86 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 1H | 1 | €9.962,71 | €1.153,43 | €3.460,30 | €49,83 | €-1,21 |
| TEST | Combo Adaptive Tp3 V1 | 3 | €9.959,05 | €2.798,22 | €5.596,43 | €149,59 | €-28,55 |
| TEST | Benchmark trend following EMA 1H | 3 | €9.953,50 | €3.291,34 | €6.582,68 | €149,71 | €-43,80 |
| TEST | 1H Fast V3 Nohigh V1 | 4 | €9.952,06 | €1.762,59 | €5.287,77 | €197,38 | €58,23 |
| TEST | Scanner Top5 Btc Guard V1 | 3 | €9.951,74 | €1.204,48 | €2.408,96 | €147,42 | €11,37 |
| TEST | Btc Ema 4H | 0 | €9.950,68 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 4H | 0 | €9.950,68 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 4H | 0 | €9.949,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Ema 4H | 0 | €9.947,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Forza relativa 1H V1 | 4 | €9.936,63 | €1.590,83 | €3.181,66 | €148,45 | €18,25 |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | 2 | €9.931,24 | €1.092,52 | €2.185,03 | €100,07 | €0,00 |
| TEST | Eth Adaptive 1H | 1 | €9.928,26 | €1.146,74 | €3.440,21 | €49,54 | €22,42 |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | 1 | €9.916,34 | €864,27 | €1.728,54 | €49,61 | €0,00 |
| TEST | 1H Fast Tp2 V1 | 4 | €9.913,55 | €1.755,77 | €5.267,30 | €196,61 | €58,01 |
| TEST | Rapida 1H V1 | 3 | €9.890,40 | €1.370,69 | €4.112,06 | €98,42 | €78,53 |
| TEST | Doge Bollinger 1H | 0 | €9.888,87 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | 3 | €9.880,02 | €523,94 | €1.571,81 | €98,09 | €53,04 |
| TEST | Sol Adaptive 1H | 1 | €9.879,34 | €1.144,60 | €3.433,80 | €49,45 | €-7,92 |
| TEST | Master Adaptive Expanded V1 | 3 | €9.878,20 | €1.280,37 | €2.560,75 | €147,44 | €11,29 |
| TEST | Scanner Bottom 5 Short 1H | 3 | €9.870,60 | €2.757,78 | €5.515,56 | €0,00 | €93,47 |
| TEST | Combo Adaptive Long Only V1 | 2 | €9.865,72 | €1.099,22 | €2.198,44 | €98,72 | €0,00 |
| TEST | Sol Bollinger 1H | 1 | €9.857,54 | €1.365,75 | €4.097,24 | €49,17 | €26,56 |
| TEST | Combo Adaptive Quality7 Regime V1 | 1 | €9.855,64 | €864,27 | €1.728,54 | €49,61 | €0,00 |
| TEST | Eth Ema 1H | 1 | €9.855,58 | €1.138,34 | €3.415,02 | €49,18 | €22,25 |
| TEST | Global Confluence puro 1H | 0 | €9.845,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | 3 | €9.843,89 | €559,79 | €1.679,37 | €146,83 | €39,87 |
| TEST | Master Adaptive V1 | 3 | €9.834,67 | €1.279,30 | €2.558,60 | €147,22 | €11,24 |
| TEST | Master Adaptive No Alt V1 | 3 | €9.834,67 | €1.279,30 | €2.558,60 | €147,22 | €11,24 |
| TEST | Master Adaptive Runner25 V1 | 3 | €9.832,23 | €1.279,24 | €2.558,48 | €147,21 | €11,24 |
| TEST | Combo Adaptive Partial 1R V1 | 3 | €9.829,94 | €2.764,95 | €5.529,91 | €147,91 | €-28,18 |
| TEST | 1H Fast V3 Long Only V1 | 3 | €9.800,45 | €642,03 | €1.926,09 | €146,54 | €32,57 |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | 3 | €9.731,03 | €1.321,79 | €2.643,57 | €146,72 | €9,51 |
| TEST | Scanner Top5 Btc Mfe V1 | 3 | €9.717,12 | €2.589,20 | €5.178,41 | €148,55 | €6,88 |
| TEST | Master Adaptive Gb20 V1 | 3 | €9.701,43 | €1.289,74 | €2.579,49 | €145,92 | €11,09 |
| TEST | Combo Adaptive Mfe Trail | 3 | €9.681,02 | €1.149,02 | €2.298,05 | €96,76 | €0,00 |
| TEST | Scanner Top5 Btc Guard Mfe V1 | 3 | €9.620,54 | €1.202,24 | €2.404,47 | €145,33 | €9,40 |
| TEST | Master Adaptive Strict3 V1 | 3 | €9.606,88 | €1.286,08 | €2.572,16 | €144,79 | €42,99 |

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
| PRINCIPALE | Principale 4H | Confluenza trend | €9.939,87 | €-52,87 | 18 | 18 | 33,33% | 0,91 | €-2,94 | 4,26% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.744,02 | €733,40 | 31 | 31 | 54,84% | 2,38 | €23,66 | 2,70% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €10.508,80 | €440,97 | 39 | 39 | 53,85% | 1,61 | €11,31 | 2,30% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €10.504,59 | €494,53 | 23 | 23 | 52,17% | 2,25 | €21,50 | 2,01% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €10.448,05 | €381,29 | 34 | 34 | 47,06% | 1,47 | €11,21 | 2,20% |
| TEST | 1H Fast Score 6 75 V1 | Momentum / breakout | €10.334,28 | €286,29 | 34 | 34 | 44,12% | 1,49 | €8,42 | 2,49% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €10.261,19 | €144,73 | 19 | 19 | 47,37% | 1,34 | €7,62 | 2,12% |
| TEST | 1H Fast V3 Cap75 V1 | Momentum / breakout V3 Filtered | €10.260,36 | €184,94 | 28 | 28 | 42,86% | 1,36 | €6,61 | 2,49% |
| TEST | Combo Adaptive | Combo Adaptive | €10.232,84 | €265,08 | 22 | 22 | 50,00% | 1,78 | €12,05 | 1,31% |
| TEST | Scanner Top5 Btc Tp3 V1 | Scanner Top 5 + forza BTC | €10.224,92 | €141,80 | 8 | 8 | 62,50% | 1,87 | €17,72 | 2,33% |
| TEST | Scanner Top5 Btc Runner25 V1 | Scanner Top 5 + forza BTC | €10.208,39 | €198,60 | 9 | 9 | 66,67% | 2,22 | €22,07 | 2,33% |
| TEST | 1H Fast Nohigh Cap75 V1 | Momentum / breakout | €10.207,34 | €132,31 | 33 | 33 | 42,42% | 1,19 | €4,01 | 2,83% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €10.196,25 | €130,93 | 34 | 33 | 35,29% | 1,13 | €3,85 | 3,69% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €10.156,87 | €89,16 | 27 | 25 | 51,85% | 1,16 | €3,30 | 2,75% |
| TEST | Rapida 1H V3 Filtered | Momentum / breakout V3 Filtered | €10.118,55 | €40,42 | 64 | 64 | 34,38% | 1,03 | €0,63 | 2,89% |
| TEST | Doge Ema 1H | Trend following EMA | €10.117,49 | €148,24 | 7 | 7 | 71,43% | 2,33 | €21,18 | 1,36% |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | Scanner Top 5 + forza BTC | €10.117,25 | €107,65 | 5 | 5 | 60,00% | 1,91 | €21,53 | 1,64% |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | Momentum / breakout | €10.116,41 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,39% |
| TEST | 1H Fast Score 6 75 Range Only V1 | Momentum / breakout | €10.116,41 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,39% |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | Momentum / breakout | €10.116,41 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,39% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.098,18 | €99,96 | 2 | 2 | 100,00% | ∞ | €49,98 | 0,54% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €10.092,12 | €92,12 | 3 | 3 | 66,67% | 21,53 | €30,71 | 0,79% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €10.092,09 | €70,07 | 28 | 28 | 42,86% | 1,11 | €2,50 | 2,06% |
| TEST | Combo Scanner | Combo Scanner | €10.089,69 | €121,92 | 24 | 24 | 45,83% | 1,20 | €5,08 | 2,66% |
| TEST | Scanner Top5 Btc Btc Le3 V1 | Scanner Top 5 + forza BTC | €10.088,68 | €79,14 | 5 | 5 | 60,00% | 1,73 | €15,83 | 2,20% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €10.086,98 | €86,98 | 1 | 1 | 100,00% | ∞ | €86,98 | 0,40% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.084,12 | €84,12 | 1 | 1 | 100,00% | ∞ | €84,12 | 0,30% |
| TEST | 1H Fast No Pepe V1 | Momentum / breakout | €10.062,32 | €-15,37 | 32 | 32 | 34,38% | 0,98 | €-0,48 | 2,10% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €10.042,25 | €-6,74 | 14 | 14 | 35,71% | 0,98 | €-0,48 | 2,31% |
| TEST | 1H Fast V3 Nohigh Range Only V1 | Momentum / breakout V3 Filtered | €10.038,93 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,41% |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | Momentum / breakout V3 Filtered | €10.038,93 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,41% |
| TEST | Master Adaptive Gb20 Loss Cap V1 | Master Adaptive Consensus | €10.035,62 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,35% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €10.028,40 | €28,40 | 6 | 6 | 33,33% | 1,98 | €4,73 | 0,25% |
| TEST | Master Adaptive Gb20 Be V1 | Master Adaptive Consensus | €10.026,29 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,31% |
| TEST | Master Adaptive Gb20 Partial V1 | Master Adaptive Consensus | €10.026,29 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,31% |
| TEST | Combo Adaptive Side Regime Guard V1 | Combo Adaptive | €10.022,34 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,29% |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | Momentum / breakout V3 Filtered | €10.019,71 | €-9,06 | 4 | 4 | 50,00% | 0,88 | €-2,27 | 0,98% |
| TEST | Combo Trend Side Regime Guard V1 | Combo Trend | €10.015,88 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,13% |
| TEST | Main Side Regime Guard V1 | Confluenza trend | €10.015,57 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,07% |
| TEST | Main Dynamic Asset Selector V1 | Confluenza trend | €10.015,57 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,07% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €10.015,45 | €15,45 | 1 | 1 | 100,00% | ∞ | €15,45 | 0,51% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €10.013,28 | €13,28 | 3 | 3 | 66,67% | 1,24 | €4,43 | 0,89% |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | Momentum / breakout | €10.006,64 | €-13,51 | 11 | 11 | 27,27% | 0,94 | €-1,23 | 1,92% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €10.005,68 | €5,68 | 6 | 6 | 33,33% | 1,98 | €0,95 | 0,05% |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | Momentum / breakout V3 Filtered | €10.004,56 | €-54,58 | 1 | 1 | 0,00% | 0,00 | €-54,58 | 0,67% |
| TEST | Combo Adaptive Quality7 V1 | Combo Adaptive | €10.004,50 | €26,28 | 9 | 9 | 55,56% | 1,22 | €2,92 | 1,51% |
| TEST | Sol Ema 1H | Trend following EMA | €10.003,31 | €32,05 | 4 | 4 | 50,00% | 1,29 | €8,01 | 1,67% |
| TEST | Combo Adaptive Runner25 V1 | Combo Adaptive | €10.001,97 | €22,17 | 15 | 15 | 46,67% | 1,06 | €1,48 | 2,12% |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | €10.001,47 | €1,47 | 5 | 5 | 40,00% | 1,12 | €0,29 | 0,13% |
| TEST | Scalp RSI Long 25 · €10 · 15x | Inversione RSI estrema 15m | €10.000,29 | €0,29 | 5 | 5 | 40,00% | 1,12 | €0,06 | 0,03% |
| TEST | 1H Balanced Short Trend Down Strict V1 | Confluenza trend | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
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
| TEST | Ampia 4H | Confluenza trend | €9.998,35 | €-17,59 | 14 | 14 | 21,43% | 0,96 | €-1,26 | 2,94% |
| TEST | Scalp RSI Long 20 · prudente · 5x | Inversione RSI estrema 15m | €9.996,99 | €-3,01 | 1 | 1 | 0,00% | 0,00 | €-3,01 | 0,11% |
| TEST | 1H Balanced Long No Rhv V1 | Confluenza trend | €9.996,52 | €-69,85 | 1 | 1 | 0,00% | 0,00 | €-69,85 | 0,88% |
| TEST | 1H Fast V3 No Esports Long Only V1 | Momentum / breakout V3 Filtered | €9.996,19 | €-73,56 | 1 | 1 | 0,00% | 0,00 | €-73,56 | 0,94% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €9.993,10 | €-52,42 | 10 | 9 | 40,00% | 0,79 | €-5,24 | 1,69% |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | €9.992,50 | €-7,50 | 1 | 1 | 0,00% | 0,00 | €-7,50 | 0,11% |
| TEST | Combo Trend | Combo Trend | €9.989,11 | €-0,85 | 29 | 29 | 31,03% | 1,00 | €-0,03 | 3,58% |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | €9.988,38 | €-11,62 | 1 | 1 | 0,00% | 0,00 | €-11,62 | 0,17% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €9.984,38 | €-52,00 | 1 | 1 | 0,00% | 0,00 | €-52,00 | 0,60% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €9.981,52 | €-51,83 | 1 | 1 | 0,00% | 0,00 | €-51,83 | 0,59% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €9.980,62 | €-19,38 | 4 | 4 | 50,00% | 0,82 | €-4,84 | 1,49% |
| TEST | 1H Fast V3 No Esports V1 | Momentum / breakout V3 Filtered | €9.979,03 | €-76,18 | 37 | 37 | 32,43% | 0,90 | €-2,06 | 2,49% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €9.976,99 | €-23,01 | 5 | 5 | 20,00% | 0,20 | €-4,60 | 0,37% |
| TEST | Combo Adaptive Regime V1 | Combo Adaptive | €9.975,22 | €-23,53 | 10 | 10 | 50,00% | 0,92 | €-2,35 | 2,18% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.971,68 | €-17,46 | 3 | 3 | 33,33% | 0,84 | €-5,82 | 1,38% |
| TEST | Sol Ema 4H | Trend following EMA | €9.965,31 | €-52,00 | 1 | 1 | 0,00% | 0,00 | €-52,00 | 0,56% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.964,86 | €-35,14 | 6 | 6 | 16,67% | 0,18 | €-5,86 | 0,36% |
| TEST | Btc Ema 1H | Trend following EMA | €9.962,71 | €-34,33 | 5 | 5 | 40,00% | 0,79 | €-6,87 | 1,56% |
| TEST | Combo Adaptive Tp3 V1 | Combo Adaptive | €9.959,05 | €-9,13 | 10 | 10 | 50,00% | 0,96 | €-0,91 | 1,41% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.953,50 | €1,30 | 19 | 19 | 36,84% | 1,00 | €0,07 | 2,25% |
| TEST | 1H Fast V3 Nohigh V1 | Momentum / breakout V3 Filtered | €9.952,06 | €-103,00 | 38 | 38 | 34,21% | 0,88 | €-2,71 | 2,96% |
| TEST | Scanner Top5 Btc Guard V1 | Scanner Top 5 + forza BTC | €9.951,74 | €-57,95 | 8 | 8 | 37,50% | 0,79 | €-7,24 | 3,31% |
| TEST | Btc Ema 4H | Trend following EMA | €9.950,68 | €-49,32 | 1 | 1 | 0,00% | 0,00 | €-49,32 | 0,96% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €9.950,68 | €-49,32 | 1 | 1 | 0,00% | 0,00 | €-49,32 | 0,96% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €9.949,62 | €-50,38 | 1 | 1 | 0,00% | 0,00 | €-50,38 | 0,74% |
| TEST | Eth Ema 4H | Trend following EMA | €9.947,12 | €-52,88 | 1 | 1 | 0,00% | 0,00 | €-52,88 | 0,68% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €9.936,63 | €-79,13 | 24 | 24 | 25,00% | 0,82 | €-3,30 | 3,25% |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | Scanner Top 5 + forza BTC | €9.931,24 | €-67,07 | 4 | 4 | 25,00% | 0,47 | €-16,77 | 2,38% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.928,26 | €-92,21 | 4 | 4 | 50,00% | 0,16 | €-23,05 | 1,24% |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | Combo Adaptive | €9.916,34 | €-82,62 | 5 | 5 | 40,00% | 0,48 | €-16,52 | 1,95% |
| TEST | 1H Fast Tp2 V1 | Momentum / breakout | €9.913,55 | €-141,30 | 33 | 33 | 27,27% | 0,80 | €-4,28 | 2,58% |
| TEST | Rapida 1H V1 | Momentum / breakout | €9.890,40 | €-185,96 | 72 | 72 | 31,94% | 0,89 | €-2,58 | 6,76% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €9.888,87 | €-111,13 | 2 | 2 | 0,00% | 0,00 | €-55,56 | 1,26% |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | Momentum / breakout V3 Filtered | €9.880,02 | €-171,24 | 21 | 21 | 33,33% | 0,72 | €-8,15 | 2,86% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €9.879,34 | €-110,64 | 5 | 5 | 40,00% | 0,38 | €-22,13 | 2,14% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €9.878,20 | €-131,10 | 8 | 8 | 25,00% | 0,59 | €-16,39 | 2,80% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.870,60 | €-218,20 | 23 | 23 | 34,78% | 0,62 | €-9,49 | 5,48% |
| TEST | Combo Adaptive Long Only V1 | Combo Adaptive | €9.865,72 | €-132,59 | 5 | 5 | 20,00% | 0,42 | €-26,52 | 2,34% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.857,54 | €-166,62 | 3 | 3 | 0,00% | 0,00 | €-55,54 | 1,89% |
| TEST | Combo Adaptive Quality7 Regime V1 | Combo Adaptive | €9.855,64 | €-143,33 | 5 | 5 | 20,00% | 0,17 | €-28,67 | 1,95% |
| TEST | Eth Ema 1H | Trend following EMA | €9.855,58 | €-164,74 | 6 | 6 | 33,33% | 0,25 | €-27,46 | 1,92% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.845,62 | €-154,38 | 9 | 9 | 33,33% | 0,44 | €-17,15 | 2,92% |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | Momentum / breakout V3 Filtered | €9.843,89 | €-194,94 | 22 | 22 | 45,45% | 0,70 | €-8,86 | 3,21% |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | €9.834,67 | €-174,58 | 6 | 6 | 16,67% | 0,36 | €-29,10 | 3,19% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €9.834,67 | €-174,58 | 6 | 6 | 16,67% | 0,36 | €-29,10 | 3,19% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €9.832,23 | €-177,01 | 6 | 6 | 16,67% | 0,35 | €-29,50 | 3,19% |
| TEST | Combo Adaptive Partial 1R V1 | Combo Adaptive | €9.829,94 | €-138,49 | 12 | 12 | 41,67% | 0,64 | €-11,54 | 2,24% |
| TEST | 1H Fast V3 Long Only V1 | Momentum / breakout V3 Filtered | €9.800,45 | €-230,96 | 24 | 24 | 25,00% | 0,65 | €-9,62 | 3,65% |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | Scanner Top 5 + forza BTC | €9.731,03 | €-276,90 | 17 | 17 | 29,41% | 0,42 | €-16,29 | 2,88% |
| TEST | Scanner Top5 Btc Mfe V1 | Scanner Top 5 + forza BTC | €9.717,12 | €-286,96 | 14 | 14 | 35,71% | 0,25 | €-20,50 | 3,95% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €9.701,43 | €-308,11 | 34 | 34 | 55,88% | 0,57 | €-9,06 | 4,16% |
| TEST | Combo Adaptive Mfe Trail | Combo Adaptive | €9.681,02 | €-317,53 | 27 | 27 | 25,93% | 0,45 | €-11,76 | 4,11% |
| TEST | Scanner Top5 Btc Guard Mfe V1 | Scanner Top 5 + forza BTC | €9.620,54 | €-387,55 | 20 | 20 | 25,00% | 0,33 | €-19,38 | 4,05% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €9.606,88 | €-434,08 | 15 | 15 | 20,00% | 0,40 | €-28,94 | 4,69% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | LAB | SHORT | Confluenza trend | 240m | 3,0x | 0,17841 | 0,17841 | 0,17841 | 0,23699 | 0,13559 | €136,26 | €408,77 | €0,00 | €-0,00 |
| Principale 4H | SUI | LONG | Confluenza trend | 240m | 3,0x | 0,76296 | 0,76296 | 0,73998 | 0,51245 | 0,80891 | €547,52 | €1.642,56 | €49,46 | €0,00 |
| Principale 4H | ONDO | LONG | Confluenza trend | 240m | 3,0x | 0,40344 | 0,40344 | 0,37762 | 0,27098 | 0,45509 | €254,70 | €764,09 | €48,91 | €0,00 |
| Principale 4H | DOGE | SHORT | Confluenza trend | 240m | 3,0x | 0,06940 | 0,06964 | 0,07160 | 0,09218 | 0,06498 | €524,39 | €1.573,18 | €50,01 | €-5,53 |
| Bilanciata 1H V1 | ONDO | LONG | Confluenza trend | 60m | 3,0x | 0,39694 | 0,39694 | 0,38539 | 0,26661 | 0,42004 | €581,76 | €1.745,29 | €50,78 | €0,00 |
| Bilanciata 1H V1 | ADA | SHORT | Confluenza trend | 60m | 3,0x | 0,16703 | 0,16381 | 0,16501 | 0,22187 | 0,16112 | €978,72 | €2.936,17 | €0,00 | €56,60 |
| Bilanciata 1H V1 | BANK | LONG | Confluenza trend | 60m | 3,0x | 0,30592 | 0,31301 | 0,27494 | 0,20548 | 0,36789 | €172,71 | €518,13 | €52,47 | €12,01 |
| Bilanciata 1H V1 | ZEC | SHORT | Confluenza trend | 60m | 3,0x | 487,33251 | 486,29000 | 497,30283 | 647,34002 | 467,39189 | €854,91 | €2.564,72 | €52,47 | €5,49 |
| 1H Balanced Long No Rhv V1 | BANK | LONG | Confluenza trend | 60m | 3,0x | 0,29401 | 0,31301 | 0,29401 | 0,19748 | 0,36064 | €147,07 | €441,21 | €0,00 | €28,51 |
| 1H Balanced Long No Rhv V1 | AKE | LONG | Confluenza trend | 60m | 3,0x | 0,00260 | 0,00274 | 0,00229 | 0,00175 | 0,00322 | €137,92 | €413,75 | €49,65 | €21,85 |
| 1H Balanced Long No Rhv V1 | BEAT | LONG | Confluenza trend | 60m | 3,0x | 3,21779 | 3,30317 | 2,97356 | 2,16128 | 3,70625 | €219,14 | €657,41 | €49,90 | €17,44 |
| Bilanciata 1H V2 | ESPORTS | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,02164 | 0,02164 | 0,02164 | 0,02874 | 0,01644 | €138,69 | €416,06 | €0,00 | €-0,00 |
| Bilanciata 1H V2 | BANK | LONG | Confluenza trend V2 | 60m | 3,0x | 0,29967 | 0,31301 | 0,26406 | 0,20128 | 0,37088 | €141,19 | €423,58 | €50,33 | €18,86 |
| Bilanciata 1H V2 | ZEC | SHORT | Confluenza trend V2 | 60m | 3,0x | 494,80102 | 486,29000 | 492,41965 | 657,26069 | 474,10997 | €802,34 | €2.407,01 | €0,00 | €41,40 |
| Bilanciata 1H V2 | PEPE | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.026,91 | €3.080,73 | €50,38 | €11,30 |
| Bilanciata 1H V3 Filtered | ESPORTS | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,02126 | 0,02126 | 0,02126 | 0,02823 | 0,01615 | €141,51 | €424,52 | €0,00 | €-0,00 |
| Bilanciata 1H V3 Filtered | ONDO | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,40134 | 0,40134 | 0,38898 | 0,26957 | 0,42605 | €557,59 | €1.672,77 | €51,50 | €0,00 |
| Bilanciata 1H V3 Filtered | ZEC | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 494,80102 | 486,29000 | 492,41965 | 657,26069 | 474,10997 | €819,31 | €2.457,92 | €0,00 | €42,28 |
| Bilanciata 1H V3 Filtered | BANK | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,29527 | 0,31301 | 0,29527 | 0,19832 | 0,36219 | €152,72 | €458,16 | €0,00 | €27,53 |
| Rapida 1H V1 | ZEC | SHORT | Momentum / breakout | 60m | 3,0x | 491,90160 | 486,29000 | 491,28201 | 653,40929 | 479,92384 | €1.018,17 | €3.054,50 | €0,00 | €34,85 |
| Rapida 1H V1 | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00260 | 0,00274 | 0,00229 | 0,00175 | 0,00307 | €136,66 | €409,99 | €49,20 | €21,65 |
| Rapida 1H V1 | BANK | LONG | Momentum / breakout | 60m | 3,0x | 0,30271 | 0,31301 | 0,27970 | 0,20332 | 0,33723 | €215,86 | €647,57 | €49,23 | €22,03 |
| 1H Fast Score 6 75 V1 | XRP | SHORT | Momentum / breakout | 60m | 3,0x | 1,09458 | 1,09349 | 1,10684 | 1,45397 | 1,07619 | €1.525,19 | €4.575,56 | €51,25 | €4,56 |
| 1H Fast Score 6 75 V1 | BTC | SHORT | Momentum / breakout | 60m | 3,0x | 63750,18741 | 64142,90000 | 64464,18951 | 84681,49895 | 62679,18426 | €1.520,13 | €4.560,38 | €51,08 | €-28,09 |
| 1H Fast Score 6 75 V1 | ZEC | SHORT | Momentum / breakout | 60m | 3,0x | 494,62106 | 486,29000 | 491,39128 | 657,02164 | 482,38187 | €1.038,85 | €3.116,56 | €0,00 | €52,49 |
| 1H Fast Score 6 75 V1 | BANK | LONG | Momentum / breakout | 60m | 3,0x | 0,30150 | 0,31301 | 0,27832 | 0,20251 | 0,33627 | €223,13 | €669,39 | €51,46 | €25,55 |
| 1H Fast Score 6 75 No Trend Up V1 | BANK | LONG | Momentum / breakout | 60m | 3,0x | 0,29401 | 0,31301 | 0,29401 | 0,19748 | 0,33288 | €189,10 | €567,29 | €0,00 | €36,66 |
| 1H Fast Score 6 75 No Trend Up V1 | ZEC | SHORT | Momentum / breakout | 60m | 3,0x | 494,62106 | 486,29000 | 491,39128 | 657,02164 | 482,38187 | €1.010,28 | €3.030,83 | €0,00 | €51,05 |
| 1H Fast Score 6 75 No Trend Up V1 | PEPE | SHORT | Momentum / breakout | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.258,42 | €3.775,25 | €49,99 | €11,49 |
| 1H Fast Score 6 75 No Trend Up V1 | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00260 | 0,00274 | 0,00229 | 0,00175 | 0,00307 | €138,10 | €414,29 | €49,71 | €21,88 |
| 1H Fast Score 6 75 Range Only V1 | BANK | LONG | Momentum / breakout | 60m | 3,0x | 0,29401 | 0,31301 | 0,29401 | 0,19748 | 0,33288 | €189,10 | €567,29 | €0,00 | €36,66 |
| 1H Fast Score 6 75 Range Only V1 | ZEC | SHORT | Momentum / breakout | 60m | 3,0x | 494,62106 | 486,29000 | 491,39128 | 657,02164 | 482,38187 | €1.010,28 | €3.030,83 | €0,00 | €51,05 |
| 1H Fast Score 6 75 Range Only V1 | PEPE | SHORT | Momentum / breakout | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.258,42 | €3.775,25 | €49,99 | €11,49 |
| 1H Fast Score 6 75 Range Only V1 | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00260 | 0,00274 | 0,00229 | 0,00175 | 0,00307 | €138,10 | €414,29 | €49,71 | €21,88 |
| 1H Fast Score 6 75 Cost Aware V1 | BANK | LONG | Momentum / breakout | 60m | 3,0x | 0,29401 | 0,31301 | 0,29401 | 0,19748 | 0,33288 | €189,10 | €567,29 | €0,00 | €36,66 |
| 1H Fast Score 6 75 Cost Aware V1 | ZEC | SHORT | Momentum / breakout | 60m | 3,0x | 494,62106 | 486,29000 | 491,39128 | 657,02164 | 482,38187 | €1.010,28 | €3.030,83 | €0,00 | €51,05 |
| 1H Fast Score 6 75 Cost Aware V1 | PEPE | SHORT | Momentum / breakout | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.258,42 | €3.775,25 | €49,99 | €11,49 |
| 1H Fast Score 6 75 Cost Aware V1 | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00260 | 0,00274 | 0,00229 | 0,00175 | 0,00307 | €138,10 | €414,29 | €49,71 | €21,88 |
| 1H Fast Nohigh Cap75 V1 | BTC | SHORT | Momentum / breakout | 60m | 3,0x | 63750,18741 | 64142,90000 | 64464,18951 | 84681,49895 | 62679,18426 | €1.499,07 | €4.497,20 | €50,37 | €-27,70 |
| 1H Fast Nohigh Cap75 V1 | BANK | LONG | Momentum / breakout | 60m | 3,0x | 0,29223 | 0,31301 | 0,29223 | 0,19628 | 0,33299 | €182,11 | €546,32 | €0,00 | €38,85 |
| 1H Fast Nohigh Cap75 V1 | ZEC | SHORT | Momentum / breakout | 60m | 3,0x | 494,62106 | 486,29000 | 491,39128 | 657,02164 | 482,38187 | €1.021,31 | €3.063,92 | €0,00 | €51,61 |
| 1H Fast Nohigh Cap75 V1 | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00263 | 0,00274 | 0,00231 | 0,00176 | 0,00310 | €140,60 | €421,79 | €50,61 | €17,49 |
| 1H Fast Long Btc 1 3 Cap75 V1 | ONDO | LONG | Momentum / breakout | 60m | 3,0x | 0,39694 | 0,39694 | 0,38849 | 0,26661 | 0,40961 | €783,06 | €2.349,19 | €50,00 | €0,00 |
| 1H Fast Long Btc 1 3 Cap75 V1 | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00260 | 0,00274 | 0,00229 | 0,00175 | 0,00307 | €137,66 | €412,97 | €49,56 | €21,81 |
| 1H Fast No Pepe V1 | ZEC | SHORT | Momentum / breakout | 60m | 3,0x | 491,90160 | 486,29000 | 491,28201 | 653,40929 | 479,92384 | €1.035,86 | €3.107,57 | €0,00 | €35,45 |
| 1H Fast No Pepe V1 | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00260 | 0,00274 | 0,00229 | 0,00175 | 0,00307 | €139,04 | €417,11 | €50,05 | €22,03 |
| 1H Fast No Pepe V1 | BANK | LONG | Momentum / breakout | 60m | 3,0x | 0,30271 | 0,31301 | 0,27970 | 0,20332 | 0,33723 | €219,61 | €658,83 | €50,08 | €22,42 |
| 1H Fast Tp2 V1 | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00260 | 0,00274 | 0,00229 | 0,00175 | 0,00322 | €138,00 | €414,01 | €49,68 | €21,86 |
| 1H Fast Tp2 V1 | BEAT | LONG | Momentum / breakout | 60m | 3,0x | 3,25601 | 3,30317 | 3,07600 | 2,18696 | 3,61603 | €298,76 | €896,29 | €49,55 | €12,98 |
| 1H Fast Tp2 V1 | ZEC | SHORT | Momentum / breakout | 60m | 3,0x | 486,53267 | 486,29000 | 493,75197 | 646,27757 | 472,09408 | €1.108,33 | €3.325,00 | €49,34 | €1,66 |
| 1H Fast Tp2 V1 | BANK | LONG | Momentum / breakout | 60m | 3,0x | 0,30271 | 0,31301 | 0,27970 | 0,20332 | 0,34873 | €210,67 | €632,01 | €48,04 | €21,50 |
| Rapida 1H V2 | TAO | SHORT | Momentum / breakout V2 | 60m | 3,0x | 188,48684 | 188,48684 | 190,75481 | 250,37335 | 185,08488 | €1.390,02 | €4.170,07 | €50,18 | €-0,00 |
| Rapida 1H V2 | ZEC | SHORT | Momentum / breakout V2 | 60m | 3,0x | 491,90160 | 486,29000 | 491,28201 | 653,40929 | 479,92384 | €1.030,95 | €3.092,84 | €0,00 | €35,28 |
| Rapida 1H V2 | BANK | LONG | Momentum / breakout V2 | 60m | 3,0x | 0,30592 | 0,31301 | 0,28182 | 0,20548 | 0,34207 | €210,98 | €632,95 | €49,86 | €14,67 |
| Rapida 1H V3 Filtered | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 491,90160 | 486,29000 | 491,28201 | 653,40929 | 479,92384 | €1.041,65 | €3.124,94 | €0,00 | €35,65 |
| Rapida 1H V3 Filtered | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00260 | 0,00274 | 0,00229 | 0,00175 | 0,00307 | €139,81 | €419,44 | €50,33 | €22,15 |
| Rapida 1H V3 Filtered | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,30271 | 0,31301 | 0,27970 | 0,20332 | 0,33723 | €220,84 | €662,51 | €50,36 | €22,54 |
| 1H Fast V3 Cap75 V1 | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 63750,18741 | 64142,90000 | 64464,18951 | 84681,49895 | 62679,18426 | €1.506,88 | €4.520,63 | €50,63 | €-27,85 |
| 1H Fast V3 Cap75 V1 | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,29223 | 0,31301 | 0,29223 | 0,19628 | 0,33299 | €183,05 | €549,16 | €0,00 | €39,05 |
| 1H Fast V3 Cap75 V1 | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 494,62106 | 486,29000 | 491,39128 | 657,02164 | 482,38187 | €1.026,61 | €3.079,84 | €0,00 | €51,87 |
| 1H Fast V3 Cap75 V1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00263 | 0,00274 | 0,00231 | 0,00176 | 0,00310 | €141,33 | €423,98 | €50,88 | €17,58 |
| 1H Fast V3 Nohigh V1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00260 | 0,00274 | 0,00229 | 0,00175 | 0,00307 | €138,54 | €415,61 | €49,87 | €21,95 |
| 1H Fast V3 Nohigh V1 | BEAT | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 3,25601 | 3,30317 | 3,07600 | 2,18696 | 3,52603 | €299,93 | €899,78 | €49,74 | €13,03 |
| 1H Fast V3 Nohigh V1 | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 486,53267 | 486,29000 | 493,75197 | 646,27757 | 475,70373 | €1.112,64 | €3.337,92 | €49,53 | €1,66 |
| 1H Fast V3 Nohigh V1 | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,30271 | 0,31301 | 0,27970 | 0,20332 | 0,33723 | €211,49 | €634,46 | €48,23 | €21,59 |
| 1H Fast V3 Long Only V1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00277 | 0,00274 | 0,00243 | 0,00186 | 0,00326 | €135,68 | €407,04 | €48,85 | €-4,48 |
| 1H Fast V3 Long Only V1 | BEAT | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 3,25601 | 3,30317 | 3,07600 | 2,18696 | 3,52603 | €294,54 | €883,63 | €48,85 | €12,80 |
| 1H Fast V3 Long Only V1 | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,30150 | 0,31301 | 0,27832 | 0,20251 | 0,33627 | €211,81 | €635,42 | €48,85 | €24,26 |
| 1H Fast V3 Long Nohigh Cap75 V1 | BEAT | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 3,33512 | 3,30317 | 3,07807 | 2,24009 | 3,72069 | €211,65 | €634,94 | €48,94 | €-6,08 |
| 1H Fast V3 Long Nohigh Cap75 V1 | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,29223 | 0,31301 | 0,29223 | 0,19628 | 0,33299 | €175,74 | €527,22 | €0,00 | €37,49 |
| 1H Fast V3 Long Nohigh Cap75 V1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00260 | 0,00274 | 0,00229 | 0,00175 | 0,00307 | €136,55 | €409,64 | €49,16 | €21,63 |
| 1H Fast V3 No Esports V1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00260 | 0,00274 | 0,00229 | 0,00175 | 0,00307 | €138,91 | €416,74 | €50,01 | €22,01 |
| 1H Fast V3 No Esports V1 | BEAT | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 3,25601 | 3,30317 | 3,07600 | 2,18696 | 3,52603 | €300,74 | €902,21 | €49,88 | €13,07 |
| 1H Fast V3 No Esports V1 | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 486,53267 | 486,29000 | 493,75197 | 646,27757 | 475,70373 | €1.115,66 | €3.346,97 | €49,66 | €1,67 |
| 1H Fast V3 No Esports V1 | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,30271 | 0,31301 | 0,27970 | 0,20332 | 0,33723 | €212,06 | €636,18 | €48,36 | €21,65 |
| 1H Fast V3 No Esports Long Only V1 | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,29401 | 0,31301 | 0,29401 | 0,19748 | 0,33288 | €189,09 | €567,26 | €0,00 | €36,66 |
| 1H Fast V3 No Esports Long Only V1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00260 | 0,00274 | 0,00229 | 0,00175 | 0,00307 | €137,86 | €413,59 | €49,63 | €21,84 |
| 1H Fast V3 No Esports Long Only V1 | BEAT | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 3,25601 | 3,30317 | 3,07600 | 2,18696 | 3,52603 | €300,52 | €901,56 | €49,84 | €13,06 |
| 1H Fast V3 No Esports Mfe Lock V1 | PEPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.257,30 | €3.771,89 | €49,94 | €11,48 |
| 1H Fast V3 No Esports Mfe Lock V1 | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,30592 | 0,31301 | 0,28182 | 0,20548 | 0,34207 | €211,77 | €635,30 | €50,04 | €14,72 |
| 1H Fast V3 No Esports Mfe Lock V1 | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 487,33251 | 486,29000 | 495,08720 | 647,34002 | 475,70048 | €1.048,22 | €3.144,65 | €50,04 | €6,73 |
| 1H Fast V3 No Esports Stress Guard V1 | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 494,62106 | 486,29000 | 491,39128 | 657,02164 | 482,38187 | €1.010,32 | €3.030,97 | €0,00 | €51,05 |
| 1H Fast V3 No Esports Stress Guard V1 | PEPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.258,47 | €3.775,42 | €49,99 | €11,49 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | BEAT | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 3,33512 | 3,30317 | 3,07807 | 2,24009 | 3,72069 | €210,89 | €632,67 | €48,76 | €-6,06 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00260 | 0,00274 | 0,00229 | 0,00175 | 0,00307 | €136,06 | €408,18 | €48,98 | €21,56 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,30150 | 0,31301 | 0,27832 | 0,20251 | 0,33627 | €212,84 | €638,52 | €49,08 | €24,38 |
| Ampia 4H | DOGE | SHORT | Confluenza trend | 240m | 2,0x | 0,07237 | 0,06964 | 0,07077 | 0,10819 | 0,06457 | €649,49 | €1.298,97 | €0,00 | €48,94 |
| Ampia 4H | ZEC | LONG | Confluenza trend | 240m | 2,0x | 522,36445 | 486,29000 | 483,09844 | 263,79405 | 632,30930 | €332,53 | €665,06 | €49,99 | €-45,93 |
| Ampia 4H | HYPE | SHORT | Confluenza trend | 240m | 2,0x | 58,36732 | 57,45600 | 61,80927 | 87,25915 | 48,72988 | €424,03 | €848,06 | €50,01 | €13,24 |
| Ampia 4H | TAO | SHORT | Confluenza trend | 240m | 2,0x | 189,05650 | 189,05650 | 197,51338 | 282,63946 | 165,37722 | €558,68 | €1.117,36 | €49,98 | €-0,00 |
| Forza relativa 1H V1 | ESPORTS | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,02126 | 0,02126 | 0,02126 | 0,03178 | 0,01564 | €208,05 | €416,10 | €0,00 | €-0,00 |
| Forza relativa 1H V1 | NIGHT | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,02031 | 0,02031 | 0,02210 | 0,03036 | 0,01637 | €285,91 | €571,83 | €50,45 | €-0,00 |
| Forza relativa 1H V1 | ONDO | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,42171 | €891,90 | €1.783,80 | €49,29 | €0,00 |
| Forza relativa 1H V1 | BANK | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,29967 | 0,31301 | 0,26406 | 0,15133 | 0,37800 | €204,97 | €409,93 | €48,71 | €18,25 |
| Forza relativa 1H V2 | ESPORTS | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,02126 | 0,02126 | 0,02126 | 0,03178 | 0,01564 | €215,33 | €430,67 | €0,00 | €-0,00 |
| Forza relativa 1H V2 | BANK | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,29683 | 0,31301 | 0,26156 | 0,14990 | 0,37442 | €213,94 | €427,88 | €50,84 | €23,32 |
| Forza relativa 1H V2 | ZEC | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 493,58126 | 486,29000 | 503,90129 | 737,90399 | 470,87721 | €1.207,34 | €2.414,67 | €50,49 | €35,67 |
| Forza relativa 1H V2 | AKE | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,00268 | 0,00274 | 0,00236 | 0,00135 | 0,00339 | €208,76 | €417,52 | €50,10 | €8,90 |
| Benchmark Donchian breakout 1H | SUI | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,76606 | 0,76606 | 0,75182 | 0,38686 | 0,80165 | €1.377,00 | €2.754,00 | €51,18 | €0,00 |
| Benchmark Donchian breakout 1H | ZEC | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 514,40710 | 486,29000 | 494,56354 | 769,03861 | 481,15276 | €982,86 | €1.965,73 | €0,00 | €107,45 |
| Benchmark Donchian breakout 1H | BANK | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,30592 | 0,31301 | 0,27150 | 0,15449 | 0,39198 | €227,65 | €455,29 | €51,23 | €10,55 |
| Benchmark Bollinger mean reversion 1H | BTC | LONG | Bollinger mean reversion | 60m | 2,0x | 64125,06245 | 64142,90000 | 63355,56170 | 32383,15654 | 65279,31357 | €2.018,75 | €4.037,51 | €48,45 | €1,12 |
| Benchmark Bollinger mean reversion 1H | SOL | LONG | Bollinger mean reversion | 60m | 2,0x | 73,77975 | 74,25800 | 72,89440 | 37,25878 | 75,10779 | €2.011,27 | €4.022,55 | €48,27 | €26,07 |
| Benchmark trend following EMA 1H | LAB | LONG | Trend following EMA | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €207,05 | €414,10 | €49,69 | €0,00 |
| Benchmark trend following EMA 1H | DOGE | SHORT | Trend following EMA | 60m | 2,0x | 0,06906 | 0,06964 | 0,07019 | 0,10324 | 0,06656 | €1.523,03 | €3.046,06 | €50,05 | €-25,75 |
| Benchmark trend following EMA 1H | SOL | SHORT | Trend following EMA | 60m | 2,0x | 73,83123 | 74,25800 | 75,01253 | 110,37769 | 71,23237 | €1.561,26 | €3.122,52 | €49,96 | €-18,05 |
| Scanner Top 5 Long 1H | ONDO | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,40114 | 0,40114 | 0,38834 | 0,20258 | 0,42673 | €828,91 | €1.657,82 | €52,88 | €0,00 |
| Scanner Top 5 Long 1H | LAB | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €219,03 | €438,05 | €52,57 | €0,00 |
| Scanner Top 5 Long 1H | BANK | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,30592 | 0,31301 | 0,27494 | 0,15449 | 0,36789 | €264,92 | €529,85 | €53,66 | €12,28 |
| Scanner Bottom 5 Short 1H | ESPORTS | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,02150 | 0,02150 | 0,02150 | 0,03214 | 0,01634 | €207,40 | €414,80 | €0,00 | €-0,00 |
| Scanner Bottom 5 Short 1H | ADA | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,16703 | 0,16381 | 0,16501 | 0,24971 | 0,16112 | €1.381,07 | €2.762,13 | €0,00 | €53,24 |
| Scanner Bottom 5 Short 1H | ZEC | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 494,80102 | 486,29000 | 492,41965 | 739,72752 | 474,10997 | €1.169,31 | €2.338,62 | €0,00 | €40,23 |
| Scanner Top 5 + forza BTC 1H | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39694 | 0,39694 | 0,38539 | 0,20045 | 0,42235 | €898,57 | €1.797,15 | €52,29 | €0,00 |
| Scanner Top 5 + forza BTC 1H | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €216,56 | €433,12 | €51,97 | €0,00 |
| Scanner Top 5 + forza BTC 1H | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,30592 | 0,31301 | 0,27494 | 0,15449 | 0,37408 | €259,02 | €518,04 | €52,46 | €12,00 |
| Scanner Top5 Btc Mfe V1 | SUI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,76776 | 0,76776 | 0,75508 | 0,38772 | 0,79565 | €1.514,04 | €3.028,08 | €50,00 | €0,00 |
| Scanner Top5 Btc Mfe V1 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39924 | 0,39924 | 0,38729 | 0,20162 | 0,42552 | €835,46 | €1.670,91 | €50,00 | €0,00 |
| Scanner Top5 Btc Mfe V1 | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,30858 | 0,31301 | 0,27733 | 0,15583 | 0,37734 | €239,71 | €479,42 | €48,55 | €6,88 |
| Scanner Top5 Btc Guard V1 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39724 | 0,39724 | 0,38434 | 0,20061 | 0,42561 | €756,62 | €1.513,24 | €49,13 | €0,00 |
| Scanner Top5 Btc Guard V1 | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €202,47 | €404,95 | €48,59 | €0,00 |
| Scanner Top5 Btc Guard V1 | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,30592 | 0,31301 | 0,27494 | 0,15449 | 0,37408 | €245,39 | €490,78 | €49,70 | €11,37 |
| Scanner Top5 Btc Btc Le3 V1 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39974 | 0,39974 | 0,38840 | 0,20187 | 0,42468 | €884,65 | €1.769,29 | €50,18 | €0,00 |
| Scanner Top5 Btc Btc Le3 V1 | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €207,87 | €415,74 | €49,89 | €0,00 |
| Scanner Top5 Btc Btc Le3 V1 | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,30592 | 0,31301 | 0,27494 | 0,15449 | 0,37408 | €248,77 | €497,53 | €50,39 | €11,53 |
| Scanner Top5 Btc Btc 2 3 V1 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39974 | 0,39974 | 0,38840 | 0,20187 | 0,42468 | €884,65 | €1.769,29 | €50,18 | €0,00 |
| Scanner Top5 Btc Btc 2 3 V1 | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €207,87 | €415,74 | €49,89 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39724 | 0,39724 | 0,38434 | 0,20061 | 0,42561 | €756,62 | €1.513,24 | €49,13 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,30707 | 0,31301 | 0,27695 | 0,15507 | 0,37334 | €245,18 | €490,36 | €48,10 | €9,48 |
| Scanner Top5 Btc Guard Mfe V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00274 | 0,00274 | 0,00241 | 0,00138 | 0,00346 | €200,43 | €400,87 | €48,10 | €-0,08 |
| Scanner Top5 Btc Guard Btc Le3 V1 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39974 | 0,39974 | 0,38840 | 0,20187 | 0,42468 | €871,05 | €1.742,11 | €49,41 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €205,84 | €411,68 | €49,40 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,30592 | 0,31301 | 0,27494 | 0,15449 | 0,37408 | €249,47 | €498,94 | €50,53 | €11,56 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39974 | 0,39974 | 0,38840 | 0,20187 | 0,42468 | €871,05 | €1.742,11 | €49,41 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,30707 | 0,31301 | 0,27695 | 0,15507 | 0,37334 | €248,00 | €495,99 | €48,65 | €9,59 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00274 | 0,00274 | 0,00241 | 0,00138 | 0,00346 | €202,74 | €405,47 | €48,66 | €-0,08 |
| Scanner Top5 Btc Runner25 V1 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39694 | 0,39694 | 0,38539 | 0,20045 | 0,43159 | €861,83 | €1.723,66 | €50,15 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,21338 | €207,96 | €415,92 | €49,91 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,30592 | 0,31301 | 0,27494 | 0,15449 | 0,39887 | €251,72 | €503,43 | €50,99 | €11,67 |
| Scanner Top5 Btc Tp3 V1 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39694 | 0,39694 | 0,38539 | 0,20045 | 0,43159 | €861,83 | €1.723,66 | €50,15 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,21338 | €207,96 | €415,92 | €49,91 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,26033 | 0,31301 | 0,28497 | 0,13147 | 0,35405 | €211,25 | €422,51 | €0,00 | €85,49 |
| Combo Trend | ESPORTS | SHORT | Combo Trend | 60m | 2,0x | 0,01883 | 0,01883 | 0,02109 | 0,02815 | 0,01386 | €209,57 | €419,14 | €50,30 | €-0,00 |
| Combo Trend | DOGE | SHORT | Combo Trend | 60m | 2,0x | 0,06924 | 0,06964 | 0,07034 | 0,10351 | 0,06680 | €1.558,17 | €3.116,34 | €49,86 | €-18,18 |
| Combo Trend | BANK | LONG | Combo Trend | 60m | 2,0x | 0,30592 | 0,31301 | 0,27150 | 0,15449 | 0,38166 | €221,89 | €443,78 | €49,94 | €10,28 |
| Combo Mean Reversion | BTC | LONG | Combo Mean Reversion | 60m | 2,0x | 63775,69259 | 64142,90000 | 63010,38428 | 32206,72476 | 65000,18589 | €1.998,65 | €3.997,31 | €47,97 | €23,02 |
| Combo Mean Reversion | HYPE | LONG | Combo Mean Reversion | 60m | 2,0x | 56,86137 | 57,45600 | 56,86137 | 28,71499 | 58,42218 | €1.459,02 | €2.918,04 | €0,00 | €30,52 |
| Combo Scanner | ONDO | LONG | Combo Scanner | 60m | 2,0x | 0,39694 | 0,39694 | 0,38539 | 0,20045 | 0,42235 | €857,88 | €1.715,77 | €49,92 | €0,00 |
| Combo Scanner | LAB | LONG | Combo Scanner | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €207,54 | €415,08 | €49,81 | €0,00 |
| Combo Scanner | DOGE | SHORT | Combo Scanner | 60m | 2,0x | 0,06906 | 0,06964 | 0,07008 | 0,10324 | 0,06681 | €1.710,76 | €3.421,51 | €50,60 | €-28,93 |
| Combo Adaptive | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,40114 | 0,40114 | 0,38834 | 0,20258 | 0,42673 | €809,25 | €1.618,50 | €51,63 | €0,00 |
| Combo Adaptive | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15861 | 0,13958 | 0,08010 | 0,19668 | €213,13 | €426,26 | €51,15 | €0,00 |
| Combo Adaptive | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,06906 | 0,06964 | 0,07008 | 0,10324 | 0,06701 | €1.735,03 | €3.470,05 | €51,32 | €-29,34 |
| Combo Adaptive Mfe Trail | ESPORTS | SHORT | Combo Adaptive | 60m | 2,0x | 0,02156 | 0,02156 | 0,02091 | 0,03223 | 0,01638 | €202,62 | €405,24 | €0,00 | €-0,00 |
| Combo Adaptive Mfe Trail | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39784 | 0,39784 | 0,38492 | 0,20091 | 0,42367 | €744,71 | €1.489,41 | €48,35 | €0,00 |
| Combo Adaptive Mfe Trail | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15861 | 0,13958 | 0,08010 | 0,19668 | €201,70 | €403,39 | €48,41 | €0,00 |
| Combo Adaptive Quality7 V1 | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,40304 | 0,40304 | 0,39140 | 0,20354 | 0,42632 | €859,15 | €1.718,30 | €49,62 | €0,00 |
| Combo Adaptive Quality7 V1 | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,06906 | 0,06964 | 0,07008 | 0,10324 | 0,06701 | €1.690,45 | €3.380,89 | €50,00 | €-28,58 |
| Combo Adaptive Quality7 V1 | BANK | LONG | Combo Adaptive | 60m | 2,0x | 0,30707 | 0,31301 | 0,27695 | 0,15507 | 0,36731 | €254,82 | €509,63 | €49,99 | €9,86 |
| Combo Adaptive Regime V1 | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39724 | 0,39724 | 0,38434 | 0,20061 | 0,42303 | €757,94 | €1.515,88 | €49,21 | €0,00 |
| Combo Adaptive Regime V1 | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15861 | 0,13958 | 0,08010 | 0,19668 | €206,52 | €413,04 | €49,56 | €0,00 |
| Combo Adaptive Quality7 Regime V1 | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,40554 | 0,40554 | 0,39390 | 0,20480 | 0,42882 | €864,27 | €1.728,54 | €49,61 | €0,00 |
| Combo Adaptive Long Only V1 | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,41951 | €893,67 | €1.787,34 | €49,39 | €0,00 |
| Combo Adaptive Long Only V1 | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €205,55 | €411,10 | €49,33 | €0,00 |
| Combo Adaptive Partial 1R V1 | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,41951 | €893,02 | €1.786,04 | €49,36 | €0,00 |
| Combo Adaptive Partial 1R V1 | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €205,22 | €410,44 | €49,25 | €0,00 |
| Combo Adaptive Partial 1R V1 | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,06906 | 0,06964 | 0,07008 | 0,10324 | 0,06701 | €1.666,71 | €3.333,43 | €49,30 | €-28,18 |
| Combo Adaptive Quality7 Regime Partial 1R V1 | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,40554 | 0,40554 | 0,39390 | 0,20480 | 0,42882 | €864,27 | €1.728,54 | €49,61 | €0,00 |
| Combo Adaptive Runner25 V1 | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,43050 | €902,18 | €1.804,37 | €49,86 | €0,00 |
| Combo Adaptive Runner25 V1 | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,06906 | 0,06964 | 0,07008 | 0,10324 | 0,06599 | €1.688,60 | €3.377,21 | €49,95 | €-28,55 |
| Combo Adaptive Runner25 V1 | BANK | LONG | Combo Adaptive | 60m | 2,0x | 0,30592 | 0,31301 | 0,27494 | 0,15449 | 0,39887 | €246,85 | €493,70 | €50,00 | €11,44 |
| Combo Adaptive Tp3 V1 | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,43050 | €902,18 | €1.804,37 | €49,86 | €0,00 |
| Combo Adaptive Tp3 V1 | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15861 | 0,13958 | 0,08010 | 0,21571 | €207,43 | €414,86 | €49,78 | €0,00 |
| Combo Adaptive Tp3 V1 | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,06906 | 0,06964 | 0,07008 | 0,10324 | 0,06599 | €1.688,61 | €3.377,21 | €49,95 | €-28,55 |
| Btc Ema 1H | BTC | SHORT | Trend following EMA | 60m | 3,0x | 64120,47334 | 64142,90000 | 65043,80816 | 85173,36209 | 62273,80371 | €1.153,43 | €3.460,30 | €49,83 | €-1,21 |
| Btc Bollinger 1H | BTC | LONG | Bollinger mean reversion | 60m | 3,0x | 64125,06245 | 64142,90000 | 63355,56170 | 43070,66694 | 65279,31357 | €1.402,77 | €4.208,32 | €50,50 | €1,17 |
| Sol Ema 1H | SOL | SHORT | Trend following EMA | 60m | 3,0x | 73,69426 | 74,25800 | 74,75546 | 97,89054 | 71,57186 | €1.161,12 | €3.483,35 | €50,16 | €-26,65 |
| Sol Ema 4H | SOL | SHORT | Trend following EMA | 240m | 2,0x | 75,05699 | 74,25800 | 77,22103 | 112,21019 | 69,64688 | €862,58 | €1.725,17 | €49,74 | €18,36 |
| Sol Donchian 4H | SOL | SHORT | Donchian breakout 20 barre | 240m | 2,0x | 75,96380 | 74,25800 | 78,23939 | 113,56589 | 69,59218 | €830,21 | €1.660,43 | €49,74 | €37,29 |
| Sol Bollinger 1H | SOL | LONG | Bollinger mean reversion | 60m | 3,0x | 73,77975 | 74,25800 | 72,89440 | 49,55540 | 75,10779 | €1.365,75 | €4.097,24 | €49,17 | €26,56 |
| Sol Adaptive 1H | SOL | SHORT | Combo Adaptive | 60m | 3,0x | 74,08718 | 74,25800 | 75,15403 | 98,41247 | 71,95347 | €1.144,60 | €3.433,80 | €49,45 | €-7,92 |
| Sol Adaptive 4H | SOL | SHORT | Combo Adaptive | 240m | 2,0x | 75,96380 | 74,25800 | 78,44626 | 113,56589 | 69,75767 | €761,04 | €1.522,08 | €49,74 | €34,18 |
| Eth Ema 1H | ETH | SHORT | Trend following EMA | 60m | 3,0x | 1873,22528 | 1861,02000 | 1900,19972 | 2488,26758 | 1819,27639 | €1.138,34 | €3.415,02 | €49,18 | €22,25 |
| Eth Donchian 1H | ETH | SHORT | Donchian breakout 20 barre | 60m | 3,0x | 1856,94854 | 1861,02000 | 1880,71748 | 2466,64664 | 1809,41065 | €1.299,81 | €3.899,43 | €49,91 | €-8,55 |
| Eth Adaptive 1H | ETH | SHORT | Combo Adaptive | 60m | 3,0x | 1873,22528 | 1861,02000 | 1900,19972 | 2488,26758 | 1819,27639 | €1.146,74 | €3.440,21 | €49,54 | €22,42 |
| Doge Ema 1H | DOGE | SHORT | Trend following EMA | 60m | 3,0x | 0,06906 | 0,06964 | 0,07008 | 0,09173 | 0,06701 | €1.143,65 | €3.430,94 | €50,74 | €-29,01 |
| Master Adaptive V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39854 | 0,39854 | 0,38677 | 0,20126 | 0,42207 | €833,00 | €1.665,99 | €49,19 | €0,00 |
| Master Adaptive V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €203,80 | €407,60 | €48,91 | €0,00 |
| Master Adaptive V1 | BANK | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,30592 | 0,31301 | 0,27494 | 0,15449 | 0,36789 | €242,50 | €485,00 | €49,12 | €11,24 |
| Master Adaptive No Alt V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39854 | 0,39854 | 0,38677 | 0,20126 | 0,42207 | €833,00 | €1.665,99 | €49,19 | €0,00 |
| Master Adaptive No Alt V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €203,80 | €407,60 | €48,91 | €0,00 |
| Master Adaptive No Alt V1 | BANK | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,30592 | 0,31301 | 0,27494 | 0,15449 | 0,36789 | €242,50 | €485,00 | €49,12 | €11,24 |
| Master Adaptive Strict3 V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,41951 | €887,07 | €1.774,14 | €49,03 | €0,00 |
| Master Adaptive Strict3 V1 | BANK | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,29671 | 0,31301 | 0,26110 | 0,14984 | 0,36792 | €199,82 | €399,64 | €47,96 | €21,96 |
| Master Adaptive Strict3 V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00260 | 0,00274 | 0,00229 | 0,00131 | 0,00322 | €199,19 | €398,38 | €47,81 | €21,04 |
| Master Adaptive Expanded V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39854 | 0,39854 | 0,38677 | 0,20126 | 0,42207 | €833,00 | €1.665,99 | €49,19 | €0,00 |
| Master Adaptive Expanded V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €203,80 | €407,60 | €48,91 | €0,00 |
| Master Adaptive Expanded V1 | BANK | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,30592 | 0,31301 | 0,27494 | 0,15449 | 0,36789 | €243,58 | €487,15 | €49,34 | €11,29 |
| Master Adaptive Gb20 V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,40304 | 0,40304 | 0,39140 | 0,20354 | 0,42632 | €848,64 | €1.697,27 | €49,02 | €0,00 |
| Master Adaptive Gb20 V1 | BANK | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,30592 | 0,31301 | 0,27494 | 0,15449 | 0,36789 | €239,22 | €478,44 | €48,45 | €11,09 |
| Master Adaptive Gb20 V1 | RIF | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,10582 | 0,10582 | 0,09312 | 0,05344 | 0,13122 | €201,89 | €403,77 | €48,45 | €0,00 |
| Master Adaptive Runner25 V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39854 | 0,39854 | 0,38677 | 0,20126 | 0,43384 | €833,00 | €1.665,99 | €49,19 | €0,00 |
| Master Adaptive Runner25 V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,21338 | €203,80 | €407,60 | €48,91 | €0,00 |
| Master Adaptive Runner25 V1 | BANK | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,30592 | 0,31301 | 0,27494 | 0,15449 | 0,39887 | €242,44 | €484,88 | €49,11 | €11,24 |
| Combo Adaptive Side Regime Guard V1 | BANK | LONG | Combo Adaptive | 60m | 2,0x | 0,30139 | 0,31301 | 0,27038 | 0,15220 | 0,36342 | €242,95 | €485,90 | €50,00 | €18,73 |
| Combo Adaptive Side Regime Guard V1 | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,00275 | 0,00274 | 0,00242 | 0,00139 | 0,00340 | €208,33 | €416,65 | €50,00 | €-1,45 |
| Combo Adaptive Side Regime Guard V1 | ZEC | SHORT | Combo Adaptive | 60m | 2,0x | 487,66245 | 486,29000 | 497,30495 | 729,05536 | 468,37744 | €1.264,26 | €2.528,53 | €50,00 | €7,12 |
| Master Adaptive Gb20 Be V1 | BANK | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,30139 | 0,31301 | 0,30139 | 0,15220 | 0,36342 | €242,95 | €485,90 | €0,00 | €18,73 |
| Master Adaptive Gb20 Be V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00275 | 0,00274 | 0,00242 | 0,00139 | 0,00340 | €208,33 | €416,65 | €50,00 | €-1,45 |
| Master Adaptive Gb20 Be V1 | BEAT | LONG | Master Adaptive Consensus | 60m | 2,0x | 3,25560 | 3,30317 | 3,01668 | 1,64408 | 3,73344 | €340,63 | €681,27 | €50,00 | €9,95 |
| Master Adaptive Gb20 Partial V1 | BANK | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,30139 | 0,31301 | 0,27038 | 0,15220 | 0,36342 | €242,95 | €485,90 | €50,00 | €18,73 |
| Master Adaptive Gb20 Partial V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00275 | 0,00274 | 0,00242 | 0,00139 | 0,00340 | €208,33 | €416,65 | €50,00 | €-1,45 |
| Master Adaptive Gb20 Partial V1 | BEAT | LONG | Master Adaptive Consensus | 60m | 2,0x | 3,25560 | 3,30317 | 3,01668 | 1,64408 | 3,73344 | €340,63 | €681,27 | €50,00 | €9,95 |
| Master Adaptive Gb20 Loss Cap V1 | BANK | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,30139 | 0,31301 | 0,27813 | 0,15220 | 0,36342 | €323,93 | €647,87 | €50,00 | €24,98 |
| Master Adaptive Gb20 Loss Cap V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00275 | 0,00274 | 0,00242 | 0,00139 | 0,00362 | €208,32 | €416,65 | €50,00 | €-1,45 |
| Master Adaptive Gb20 Loss Cap V1 | BEAT | LONG | Master Adaptive Consensus | 60m | 2,0x | 3,25560 | 3,30317 | 3,07641 | 1,64408 | 3,73344 | €454,17 | €908,35 | €50,00 | €13,27 |
| 1H Fast V3 Nohigh Range Only V1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00275 | 0,00274 | 0,00242 | 0,00184 | 0,00324 | €138,89 | €416,67 | €50,00 | €-1,45 |
| 1H Fast V3 Nohigh Range Only V1 | HYPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 57,47950 | 57,45600 | 58,38711 | 76,35194 | 56,11809 | €1.055,48 | €3.166,43 | €50,00 | €1,29 |
| 1H Fast V3 Nohigh Range Only V1 | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,30150 | 0,31301 | 0,27832 | 0,20251 | 0,33627 | €216,82 | €650,47 | €50,00 | €24,83 |
| 1H Fast V3 Nohigh Range Only V1 | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 489,04217 | 486,29000 | 496,36223 | 649,61102 | 478,06209 | €1.113,49 | €3.340,48 | €50,00 | €18,80 |
| 1H Fast V3 Nohigh Regime Guard V1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00275 | 0,00274 | 0,00242 | 0,00184 | 0,00324 | €138,89 | €416,67 | €50,00 | €-1,45 |
| 1H Fast V3 Nohigh Regime Guard V1 | HYPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 57,47950 | 57,45600 | 58,38711 | 76,35194 | 56,11809 | €1.055,48 | €3.166,43 | €50,00 | €1,29 |
| 1H Fast V3 Nohigh Regime Guard V1 | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,30150 | 0,31301 | 0,27832 | 0,20251 | 0,33627 | €216,82 | €650,47 | €50,00 | €24,83 |
| 1H Fast V3 Nohigh Regime Guard V1 | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 489,04217 | 486,29000 | 496,36223 | 649,61102 | 478,06209 | €1.113,49 | €3.340,48 | €50,00 | €18,80 |
| Main Side Regime Guard V1 | AKE | LONG | Confluenza trend | 240m | 3,0x | 0,00268 | 0,00274 | 0,00236 | 0,00180 | 0,00333 | €138,89 | €416,67 | €50,00 | €8,33 |
| Main Side Regime Guard V1 | BANK | LONG | Confluenza trend | 240m | 3,0x | 0,30730 | 0,31301 | 0,27043 | 0,20640 | 0,38105 | €138,88 | €416,65 | €50,00 | €7,74 |
| Main Dynamic Asset Selector V1 | AKE | LONG | Confluenza trend | 240m | 3,0x | 0,00268 | 0,00274 | 0,00236 | 0,00180 | 0,00333 | €138,89 | €416,67 | €50,00 | €8,33 |
| Main Dynamic Asset Selector V1 | BANK | LONG | Confluenza trend | 240m | 3,0x | 0,30730 | 0,31301 | 0,27043 | 0,20640 | 0,38105 | €138,88 | €416,65 | €50,00 | €7,74 |
| Combo Trend Side Regime Guard V1 | AKE | LONG | Combo Trend | 60m | 2,0x | 0,00275 | 0,00274 | 0,00242 | 0,00139 | 0,00347 | €208,33 | €416,67 | €50,00 | €-1,93 |
| Combo Trend Side Regime Guard V1 | BANK | LONG | Combo Trend | 60m | 2,0x | 0,30089 | 0,31301 | 0,26785 | 0,15195 | 0,37359 | €227,64 | €455,28 | €50,00 | €18,34 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Scanner Top5 Btc Guard Mfe V1 | AKE | LONG | 2026-07-25T04:38:35+00:00 | 0,00258 | €-3,47 | -0,07 | STOP_STRESS_SLIPPAGE |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | AKE | LONG | 2026-07-25T04:38:35+00:00 | 0,00258 | €-3,51 | -0,07 | STOP_STRESS_SLIPPAGE |
| 1H Fast V3 No Esports Mfe Lock V1 | AKE | LONG | 2026-07-25T04:38:35+00:00 | 0,00258 | €-3,49 | -0,07 | STOP_STRESS_SLIPPAGE |
| Scanner Top5 Btc Guard Mfe V1 | BANK | LONG | 2026-07-25T02:23:39+00:00 | 0,29665 | €-0,61 | -0,01 | STOP |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | BANK | LONG | 2026-07-25T02:23:39+00:00 | 0,29665 | €-0,61 | -0,01 | STOP |
| Combo Adaptive Quality7 V1 | BANK | LONG | 2026-07-25T02:23:39+00:00 | 0,29665 | €-0,64 | -0,01 | STOP |
| 1H Fast V3 No Esports V1 | BANK | LONG | 2026-07-25T02:23:39+00:00 | 0,29665 | €-0,74 | -0,02 | STOP |
| 1H Fast V3 Nohigh V1 | BANK | LONG | 2026-07-25T02:23:39+00:00 | 0,29665 | €-0,74 | -0,02 | STOP |
| Rapida 1H V3 Filtered | BANK | LONG | 2026-07-25T02:23:39+00:00 | 0,29665 | €-0,75 | -0,02 | STOP |
| 1H Fast Tp2 V1 | BANK | LONG | 2026-07-25T02:23:39+00:00 | 0,29665 | €-0,73 | -0,02 | STOP |
| 1H Fast No Pepe V1 | BANK | LONG | 2026-07-25T02:23:39+00:00 | 0,29665 | €-0,75 | -0,02 | STOP |
| Rapida 1H V1 | BANK | LONG | 2026-07-25T02:23:39+00:00 | 0,29665 | €-0,73 | -0,02 | STOP |

## Regole invarianti

- Nessuna martingala e nessuna mediazione automatica in perdita.
- Il target mensile riduce il rischio quando viene avvicinato o raggiunto; non lo aumenta mai.
- Il portafoglio principale e le simulazioni di confronto hanno contabilità separata.
- Commissioni, slippage e funding sono inclusi nella simulazione secondo i parametri configurati.
- Quando stop e target risultano toccati nella stessa candela, prevale lo stop salvo modifica esplicita della configurazione.
