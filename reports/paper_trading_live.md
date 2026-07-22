# Paper trading automatico KuCoin

Generato: 2026-07-22T05:15:00+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-07-22T05:08:24+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-07-22T05:08:24+00:00 | 2026-07-22T05:08:24+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-07-22T04:45:00+00:00 | 2026-07-22T04:45:00+00:00 | 8,5 min | 25,0 min | OK |
| 60m | 12 | 2026-07-22T04:00:00+00:00 | 2026-07-22T04:00:00+00:00 | 8,5 min | 45,0 min | OK |
| 240m | 12 | 2026-07-22T00:00:00+00:00 | 2026-07-22T00:00:00+00:00 | 1,14 h | 1,00 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | ONDO | 240m | LONG | 7,36 | 6,00 | 0,00 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | HYPE | 240m | SHORT | -6,43 | 6,00 | 0,00 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | ETH | 240m | LONG | 6,25 | 6,00 | 0,00 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | XRP | 240m | LONG | 5,85 | 6,00 | 0,15 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | ADA | 240m | LONG | 5,74 | 6,00 | 0,26 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | BTC | 240m | LONG | 4,75 | 6,00 | 1,25 | STALE_CANDLE | 1,14 h | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | BANK | 240m | LONG | 4,25 | 6,00 | 1,75 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | DOGE | 240m | SHORT | -3,65 | 6,00 | 2,35 | STALE_CANDLE | 1,14 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | SOL | 240m | LONG | 2,89 | 6,00 | 3,11 | STALE_CANDLE | 1,14 h | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | AKE | 240m | LONG | 2,75 | 6,00 | 3,25 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | ZEC | 240m | SHORT | -2,38 | 6,00 | 3,62 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | PEPE | 240m | LONG | 1,12 | 6,00 | 4,88 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Bilanciata 1H V2 | ONDO | 60m | LONG | 7,75 | 5,50 | 0,00 | STRATEGY_FILTER | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro V2 non superato: regime, EMA, ritorni e RSI; per Rapida V2 servono anche breakout reale, volume e ADX. |
| Rapida 1H V1 | ONDO | 60m | LONG | 7,75 | 4,50 | 0,00 | STRATEGY_FILTER | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout UP oppure movimento breve ≥1,5%; breakout=NONE, movimento=+0.65%. |
| 1H Fast Score 6 75 V1 | ONDO | 60m | LONG | 7,75 | 6,00 | 0,00 | STRATEGY_FILTER | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout UP oppure movimento breve ≥1,5%; breakout=NONE, movimento=+0.65%. |
| 1H Fast Nohigh Cap75 V1 | ONDO | 60m | LONG | 7,75 | 4,50 | 0,00 | STRATEGY_FILTER | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout UP oppure movimento breve ≥1,5%; breakout=NONE, movimento=+0.65%. |
| 1H Fast Long Btc 1 3 Cap75 V1 | ONDO | 60m | LONG | 7,75 | 4,50 | 0,00 | STRATEGY_FILTER | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout UP oppure movimento breve ≥1,5%; breakout=NONE, movimento=+0.65%. |
| 1H Fast No Pepe V1 | ONDO | 60m | LONG | 7,75 | 4,50 | 0,00 | STRATEGY_FILTER | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout UP oppure movimento breve ≥1,5%; breakout=NONE, movimento=+0.65%. |
| 1H Fast Tp2 V1 | ONDO | 60m | LONG | 7,75 | 4,50 | 0,00 | STRATEGY_FILTER | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout UP oppure movimento breve ≥1,5%; breakout=NONE, movimento=+0.65%. |
| Rapida 1H V2 | ONDO | 60m | LONG | 7,75 | 5,00 | 0,00 | STRATEGY_FILTER | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro V2 non superato: regime, EMA, ritorni e RSI; per Rapida V2 servono anche breakout reale, volume e ADX. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.832,12 | -1,68% | €-167,88 | €3.000,00 | -5,60% | 4 | 17 | 29,41% | 0,73 | 4,26% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 17 | 300 | CAMPIONE INSUFFICIENTE | 30 (mancano 13) |

- Trade del Principale 4H chiusi: **17**; win rate **29,41%**; profit factor **0,73**.
- Expectancy: **€-8,97** per trade; P&L netto: **€-152,45**; max drawdown: **4,26%**.
- Valutazione: **Servono altri eventi indipendenti prima di trarre conclusioni.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 4 | €9.832,12 | €1.512,92 | €4.538,75 | €196,71 | €-15,56 |
| TEST | Scanner Top 5 Long 1H | 3 | €10.565,56 | €3.774,91 | €7.549,81 | €157,90 | €-58,18 |
| TEST | Scanner Top 5 + forza BTC 1H | 3 | €10.462,09 | €4.324,05 | €8.648,09 | €156,62 | €-6,78 |
| TEST | Combo Adaptive | 3 | €10.301,73 | €2.939,66 | €5.879,32 | €154,36 | €-39,65 |
| TEST | Bilanciata 1H V3 Filtered | 4 | €10.300,67 | €2.442,27 | €7.326,82 | €154,18 | €14,24 |
| TEST | Bilanciata 1H V1 | 4 | €10.201,94 | €2.639,56 | €7.918,67 | €203,34 | €37,31 |
| TEST | Combo Mean Reversion | 1 | €10.198,70 | €1.289,42 | €2.578,84 | €50,98 | €5,12 |
| TEST | Benchmark Donchian breakout 1H | 2 | €10.191,24 | €2.352,79 | €4.705,59 | €101,96 | €-17,73 |
| TEST | Forza relativa 1H V2 | 4 | €10.156,40 | €2.419,26 | €4.838,52 | €151,48 | €-4,64 |
| TEST | Benchmark Bollinger mean reversion 1H | 1 | €10.124,69 | €1.683,41 | €3.366,81 | €51,04 | €-30,43 |
| TEST | Combo Trend | 3 | €10.104,36 | €1.639,93 | €3.279,86 | €100,58 | €48,99 |
| TEST | Btc Bollinger 1H | 1 | €10.096,11 | €1.398,43 | €4.195,29 | €50,34 | €31,08 |
| TEST | Ampia 4H | 4 | €10.070,36 | €2.235,83 | €4.471,66 | €201,27 | €-16,55 |
| TEST | Scanner Top5 Btc Runner25 V1 | 3 | €10.055,97 | €3.180,38 | €6.360,76 | €150,87 | €-32,25 |
| TEST | Scanner Top5 Btc Tp3 V1 | 3 | €10.055,97 | €3.180,38 | €6.360,76 | €150,87 | €-32,25 |
| TEST | Btc Ema 4H | 1 | €10.029,13 | €1.105,63 | €2.211,26 | €50,00 | €28,21 |
| TEST | Btc Donchian 4H | 1 | €10.029,13 | €1.105,63 | €2.211,26 | €50,00 | €28,21 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €10.028,40 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Btc Le3 V1 | 3 | €10.025,02 | €3.682,97 | €7.365,95 | €150,16 | €-29,03 |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | 3 | €10.025,02 | €3.682,97 | €7.365,95 | €150,16 | €-29,03 |
| TEST | Rapida 1H V3 Filtered | 4 | €10.024,89 | €3.285,85 | €9.857,56 | €148,99 | €43,19 |
| TEST | Forza relativa 1H V1 | 4 | €10.020,60 | €3.216,05 | €6.432,10 | €150,91 | €-66,19 |
| TEST | Eth Bollinger 1H | 0 | €10.015,45 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 4H | 1 | €10.013,85 | €968,56 | €1.937,11 | €50,00 | €15,22 |
| TEST | Btc Bollinger 4H | 1 | €10.011,45 | €1.313,84 | €2.627,69 | €50,00 | €13,56 |
| TEST | Scalp RSI Long 25 · €50 · 15x | 0 | €10.006,57 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 0 | €10.005,77 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 0 | €10.005,68 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Mfe V1 | 3 | €10.005,37 | €3.423,40 | €6.846,81 | €150,29 | €-18,84 |
| TEST | Rapida 1H V2 | 0 | €10.004,31 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 4H | 1 | €10.002,18 | €1.047,40 | €2.094,81 | €50,00 | €2,32 |
| TEST | Scalp RSI Long 25 · €10 · 15x | 0 | €10.001,31 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 1H | 1 | €10.000,01 | €1.001,44 | €3.004,32 | €49,95 | €10,79 |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
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
| TEST | Eth Ema 4H | 1 | €9.997,78 | €883,93 | €1.767,86 | €50,00 | €-0,90 |
| TEST | Sol Donchian 1H | 0 | €9.997,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Scanner | 2 | €9.992,91 | €1.836,68 | €3.673,37 | €100,00 | €-21,26 |
| TEST | 1H Fast No Pepe V1 | 4 | €9.991,25 | €3.498,52 | €10.495,56 | €148,51 | €-1,23 |
| TEST | Sol Adaptive 1H | 1 | €9.990,71 | €1.000,51 | €3.001,52 | €49,91 | €10,78 |
| TEST | Btc Adaptive 1H | 0 | €9.988,26 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 4H | 1 | €9.985,88 | €807,13 | €1.614,26 | €50,00 | €-13,32 |
| TEST | Sol Ema 4H | 1 | €9.984,60 | €880,51 | €1.761,01 | €50,00 | €-14,53 |
| TEST | Sol Donchian 4H | 1 | €9.984,60 | €880,51 | €1.761,01 | €50,00 | €-14,53 |
| TEST | Eth Donchian 1H | 0 | €9.982,54 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Long Only V1 | 1 | €9.976,56 | €1.498,33 | €4.495,00 | €50,34 | €-20,93 |
| TEST | 1H Fast Tp2 V1 | 4 | €9.970,98 | €3.548,00 | €10.644,01 | €198,50 | €-26,37 |
| TEST | Doge Donchian 1H | 0 | €9.968,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 1H | 1 | €9.964,99 | €1.155,97 | €3.467,90 | €49,94 | €-21,37 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.964,86 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Adaptive 1H | 0 | €9.962,36 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Runner25 V1 | 3 | €9.958,48 | €4.110,62 | €8.221,24 | €149,28 | €-14,61 |
| TEST | Combo Adaptive Tp3 V1 | 3 | €9.958,48 | €4.110,62 | €8.221,24 | €149,28 | €-14,61 |
| TEST | Bilanciata 1H V2 | 3 | €9.950,43 | €848,57 | €2.545,72 | €99,11 | €0,00 |
| TEST | Doge Ema 1H | 0 | €9.948,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 1H | 0 | €9.944,21 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 1H | 0 | €9.937,58 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Long Only V1 | 2 | €9.930,69 | €2.802,01 | €5.604,02 | €100,01 | €-41,28 |
| TEST | Benchmark trend following EMA 1H | 3 | €9.921,08 | €3.814,18 | €7.628,36 | €148,75 | €1,47 |
| TEST | Combo Adaptive Quality7 V1 | 2 | €9.909,86 | €1.926,74 | €3.853,48 | €99,62 | €-34,92 |
| TEST | Combo Adaptive Quality7 Regime V1 | 2 | €9.899,19 | €1.931,86 | €3.863,72 | €99,61 | €-45,58 |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | 2 | €9.899,19 | €1.931,86 | €3.863,72 | €99,61 | €-45,58 |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | 0 | €9.897,23 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V1 | 4 | €9.894,29 | €3.041,12 | €9.123,37 | €195,34 | €-4,92 |
| TEST | 1H Fast V3 Cap75 V1 | 4 | €9.889,85 | €4.227,81 | €12.683,44 | €148,64 | €15,36 |
| TEST | 1H Fast V3 No Esports V1 | 4 | €9.889,85 | €4.227,81 | €12.683,44 | €148,64 | €15,36 |
| TEST | 1H Fast Score 6 75 V1 | 3 | €9.887,99 | €3.539,21 | €10.617,62 | €99,28 | €15,08 |
| TEST | Master Adaptive Strict3 V1 | 3 | €9.887,09 | €4.527,63 | €9.055,25 | €149,65 | €-51,44 |
| TEST | Eth Ema 1H | 1 | €9.882,54 | €1.144,65 | €3.433,94 | €49,45 | €-5,14 |
| TEST | Combo Adaptive Partial 1R V1 | 3 | €9.882,34 | €4.117,58 | €8.235,15 | €148,26 | €-8,36 |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | 1 | €9.878,89 | €871,05 | €1.742,11 | €49,41 | €-1,48 |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | 1 | €9.878,89 | €871,05 | €1.742,11 | €49,41 | €-1,48 |
| TEST | Combo Adaptive Regime V1 | 3 | €9.877,26 | €3.175,32 | €6.350,65 | €148,29 | €12,28 |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | 0 | €9.856,85 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive V1 | 3 | €9.844,24 | €3.622,85 | €7.245,70 | €148,79 | €-42,44 |
| TEST | Master Adaptive No Alt V1 | 3 | €9.844,24 | €3.622,85 | €7.245,70 | €148,79 | €-42,44 |
| TEST | Master Adaptive Expanded V1 | 3 | €9.844,24 | €3.622,85 | €7.245,70 | €148,79 | €-42,44 |
| TEST | Master Adaptive Runner25 V1 | 3 | €9.844,24 | €3.622,85 | €7.245,70 | €148,79 | €-42,44 |
| TEST | 1H Fast V3 Nohigh V1 | 3 | €9.832,08 | €2.729,57 | €8.188,70 | €98,57 | €37,45 |
| TEST | Scanner Top5 Btc Guard Mfe V1 | 2 | €9.809,14 | €1.811,39 | €3.622,78 | €98,52 | €-10,93 |
| TEST | 1H Fast Nohigh Cap75 V1 | 3 | €9.793,59 | €2.736,40 | €8.209,19 | €98,21 | €41,55 |
| TEST | Scanner Top5 Btc Guard V1 | 3 | €9.787,51 | €3.518,03 | €7.036,06 | €147,68 | €-34,95 |
| TEST | Global Confluence puro 1H | 0 | €9.773,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Gb20 V1 | 3 | €9.769,97 | €3.634,80 | €7.269,59 | €148,51 | €-61,33 |
| TEST | Scanner Bottom 5 Short 1H | 3 | €9.741,50 | €1.440,21 | €2.880,42 | €97,68 | €-11,78 |
| TEST | Combo Adaptive Mfe Trail | 3 | €9.622,22 | €2.314,06 | €4.628,12 | €96,32 | €31,34 |

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
| PRINCIPALE | Principale 4H | Confluenza trend | €9.832,12 | €-152,45 | 17 | 17 | 29,41% | 0,73 | €-8,97 | 4,26% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.565,56 | €627,36 | 26 | 26 | 53,85% | 2,50 | €24,13 | 2,70% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €10.462,09 | €474,06 | 19 | 19 | 52,63% | 2,68 | €24,95 | 1,62% |
| TEST | Combo Adaptive | Combo Adaptive | €10.301,73 | €345,41 | 17 | 17 | 47,06% | 2,52 | €20,32 | 1,27% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €10.300,67 | €290,85 | 26 | 26 | 46,15% | 1,45 | €11,19 | 2,20% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €10.201,94 | €169,06 | 25 | 25 | 48,00% | 1,38 | €6,76 | 1,81% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €10.198,70 | €195,13 | 7 | 7 | 57,14% | 2,81 | €27,88 | 0,59% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €10.191,24 | €212,08 | 16 | 16 | 50,00% | 1,63 | €13,26 | 1,98% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €10.156,40 | €164,02 | 18 | 18 | 33,33% | 1,33 | €9,11 | 2,48% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €10.124,69 | €157,30 | 17 | 17 | 47,06% | 1,68 | €9,25 | 2,06% |
| TEST | Combo Trend | Combo Trend | €10.104,36 | €57,96 | 15 | 15 | 33,33% | 1,15 | €3,86 | 2,19% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.096,11 | €68,69 | 1 | 1 | 100,00% | ∞ | €68,69 | 0,31% |
| TEST | Ampia 4H | Confluenza trend | €10.070,36 | €88,72 | 12 | 12 | 25,00% | 1,27 | €7,39 | 2,22% |
| TEST | Scanner Top5 Btc Runner25 V1 | Scanner Top 5 + forza BTC | €10.055,97 | €92,80 | 4 | 4 | 75,00% | 2,74 | €23,20 | 1,53% |
| TEST | Scanner Top5 Btc Tp3 V1 | Scanner Top 5 + forza BTC | €10.055,97 | €92,80 | 4 | 4 | 75,00% | 2,74 | €23,20 | 1,53% |
| TEST | Btc Ema 4H | Trend following EMA | €10.029,13 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,20% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €10.029,13 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,20% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €10.028,40 | €28,40 | 6 | 6 | 33,33% | 1,98 | €4,73 | 0,25% |
| TEST | Scanner Top5 Btc Btc Le3 V1 | Scanner Top 5 + forza BTC | €10.025,02 | €58,86 | 1 | 1 | 100,00% | ∞ | €58,86 | 1,33% |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | Scanner Top 5 + forza BTC | €10.025,02 | €58,86 | 1 | 1 | 100,00% | ∞ | €58,86 | 1,33% |
| TEST | Rapida 1H V3 Filtered | Momentum / breakout V3 Filtered | €10.024,89 | €-12,79 | 43 | 43 | 34,88% | 0,99 | €-0,30 | 2,89% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €10.020,60 | €91,78 | 18 | 18 | 33,33% | 1,35 | €5,10 | 2,29% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €10.015,45 | €15,45 | 1 | 1 | 100,00% | ∞ | €15,45 | 0,51% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €10.013,85 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,18% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.011,45 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,19% |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | €10.006,57 | €6,57 | 1 | 1 | 100,00% | ∞ | €6,57 | 0,04% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €10.005,77 | €5,77 | 1 | 1 | 100,00% | ∞ | €5,77 | 0,05% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €10.005,68 | €5,68 | 6 | 6 | 33,33% | 1,98 | €0,95 | 0,05% |
| TEST | Scanner Top5 Btc Mfe V1 | Scanner Top 5 + forza BTC | €10.005,37 | €28,33 | 3 | 3 | 33,33% | 4,03 | €9,44 | 1,23% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €10.004,31 | €4,31 | 3 | 2 | 33,33% | 1,07 | €1,44 | 0,93% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €10.002,18 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,19% |
| TEST | Scalp RSI Long 25 · €10 · 15x | Inversione RSI estrema 15m | €10.001,31 | €1,31 | 1 | 1 | 100,00% | ∞ | €1,31 | 0,01% |
| TEST | Sol Ema 1H | Trend following EMA | €10.000,01 | €-9,16 | 2 | 2 | 50,00% | 0,83 | €-4,58 | 0,98% |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | Momentum / breakout | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
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
| TEST | Eth Ema 4H | Trend following EMA | €9.997,78 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,26% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €9.997,37 | €-2,63 | 2 | 2 | 50,00% | 0,41 | €-1,31 | 0,55% |
| TEST | Combo Scanner | Combo Scanner | €9.992,91 | €17,16 | 19 | 19 | 42,11% | 1,03 | €0,90 | 2,18% |
| TEST | 1H Fast No Pepe V1 | Momentum / breakout | €9.991,25 | €-3,90 | 8 | 8 | 25,00% | 0,97 | €-0,49 | 2,00% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €9.990,71 | €-18,45 | 2 | 2 | 50,00% | 0,67 | €-9,23 | 0,99% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €9.988,26 | €-11,74 | 2 | 2 | 50,00% | 0,78 | €-5,87 | 0,89% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €9.985,88 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,18% |
| TEST | Sol Ema 4H | Trend following EMA | €9.984,60 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,20% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €9.984,60 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,20% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.982,54 | €-17,46 | 3 | 3 | 33,33% | 0,84 | €-5,82 | 1,38% |
| TEST | 1H Fast V3 Long Only V1 | Momentum / breakout V3 Filtered | €9.976,56 | €-1,94 | 6 | 6 | 16,67% | 0,97 | €-0,32 | 1,17% |
| TEST | 1H Fast Tp2 V1 | Momentum / breakout | €9.970,98 | €0,88 | 7 | 7 | 28,57% | 1,00 | €0,13 | 2,01% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €9.968,98 | €-31,02 | 2 | 2 | 50,00% | 0,46 | €-15,51 | 0,93% |
| TEST | Btc Ema 1H | Trend following EMA | €9.964,99 | €-12,46 | 3 | 3 | 33,33% | 0,89 | €-4,15 | 1,56% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.964,86 | €-35,14 | 6 | 6 | 16,67% | 0,18 | €-5,86 | 0,36% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.962,36 | €-37,64 | 3 | 3 | 66,67% | 0,31 | €-12,55 | 1,02% |
| TEST | Combo Adaptive Runner25 V1 | Combo Adaptive | €9.958,48 | €-22,11 | 4 | 4 | 50,00% | 0,79 | €-5,53 | 1,41% |
| TEST | Combo Adaptive Tp3 V1 | Combo Adaptive | €9.958,48 | €-22,11 | 4 | 4 | 50,00% | 0,79 | €-5,53 | 1,41% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €9.950,43 | €-48,22 | 17 | 15 | 47,06% | 0,89 | €-2,84 | 2,75% |
| TEST | Doge Ema 1H | Trend following EMA | €9.948,28 | €-51,72 | 4 | 4 | 50,00% | 0,54 | €-12,93 | 1,27% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.944,21 | €-55,79 | 1 | 1 | 0,00% | 0,00 | €-55,79 | 0,62% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €9.937,58 | €-62,42 | 3 | 3 | 33,33% | 0,43 | €-20,81 | 1,49% |
| TEST | Combo Adaptive Long Only V1 | Combo Adaptive | €9.930,69 | €-25,20 | 3 | 3 | 33,33% | 0,79 | €-8,40 | 1,58% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.921,08 | €-76,19 | 11 | 11 | 27,27% | 0,76 | €-6,93 | 2,25% |
| TEST | Combo Adaptive Quality7 V1 | Combo Adaptive | €9.909,86 | €-52,59 | 1 | 1 | 0,00% | 0,00 | €-52,59 | 1,18% |
| TEST | Combo Adaptive Quality7 Regime V1 | Combo Adaptive | €9.899,19 | €-52,59 | 1 | 1 | 0,00% | 0,00 | €-52,59 | 1,29% |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | Combo Adaptive | €9.899,19 | €-52,59 | 1 | 1 | 0,00% | 0,00 | €-52,59 | 1,29% |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | Momentum / breakout V3 Filtered | €9.897,23 | €-102,77 | 6 | 6 | 16,67% | 0,40 | €-17,13 | 1,38% |
| TEST | Rapida 1H V1 | Momentum / breakout | €9.894,29 | €-95,42 | 50 | 50 | 34,00% | 0,92 | €-1,91 | 5,79% |
| TEST | 1H Fast V3 Cap75 V1 | Momentum / breakout V3 Filtered | €9.889,85 | €-120,42 | 10 | 10 | 20,00% | 0,53 | €-12,04 | 2,11% |
| TEST | 1H Fast V3 No Esports V1 | Momentum / breakout V3 Filtered | €9.889,85 | €-120,42 | 10 | 10 | 20,00% | 0,53 | €-12,04 | 2,11% |
| TEST | 1H Fast Score 6 75 V1 | Momentum / breakout | €9.887,99 | €-122,84 | 11 | 11 | 18,18% | 0,53 | €-11,17 | 2,00% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €9.887,09 | €-54,91 | 1 | 1 | 0,00% | 0,00 | €-54,91 | 1,88% |
| TEST | Eth Ema 1H | Trend following EMA | €9.882,54 | €-110,26 | 5 | 5 | 40,00% | 0,33 | €-22,05 | 1,59% |
| TEST | Combo Adaptive Partial 1R V1 | Combo Adaptive | €9.882,34 | €-104,88 | 6 | 6 | 33,33% | 0,54 | €-17,48 | 2,05% |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | Scanner Top 5 + forza BTC | €9.878,89 | €-118,58 | 2 | 2 | 0,00% | 0,00 | €-59,29 | 1,21% |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | Scanner Top 5 + forza BTC | €9.878,89 | €-118,58 | 2 | 2 | 0,00% | 0,00 | €-59,29 | 1,21% |
| TEST | Combo Adaptive Regime V1 | Combo Adaptive | €9.877,26 | €-131,16 | 5 | 5 | 20,00% | 0,42 | €-26,23 | 2,18% |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | Momentum / breakout V3 Filtered | €9.856,85 | €-143,15 | 6 | 6 | 33,33% | 0,35 | €-23,86 | 1,88% |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | €9.844,24 | €-109,50 | 2 | 2 | 0,00% | 0,00 | €-54,75 | 2,05% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €9.844,24 | €-109,50 | 2 | 2 | 0,00% | 0,00 | €-54,75 | 2,05% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €9.844,24 | €-109,50 | 2 | 2 | 0,00% | 0,00 | €-54,75 | 2,05% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €9.844,24 | €-109,50 | 2 | 2 | 0,00% | 0,00 | €-54,75 | 2,05% |
| TEST | 1H Fast V3 Nohigh V1 | Momentum / breakout V3 Filtered | €9.832,08 | €-200,85 | 12 | 12 | 25,00% | 0,51 | €-16,74 | 2,96% |
| TEST | Scanner Top5 Btc Guard Mfe V1 | Scanner Top 5 + forza BTC | €9.809,14 | €-177,58 | 4 | 4 | 0,00% | 0,00 | €-44,39 | 2,33% |
| TEST | 1H Fast Nohigh Cap75 V1 | Momentum / breakout | €9.793,59 | €-243,42 | 13 | 13 | 23,08% | 0,46 | €-18,72 | 2,83% |
| TEST | Scanner Top5 Btc Guard V1 | Scanner Top 5 + forza BTC | €9.787,51 | €-172,80 | 3 | 3 | 0,00% | 0,00 | €-57,60 | 2,54% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.773,98 | €-226,02 | 7 | 7 | 28,57% | 0,17 | €-32,29 | 2,46% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €9.769,97 | €-164,86 | 5 | 5 | 20,00% | 0,06 | €-32,97 | 2,72% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.741,50 | €-245,04 | 16 | 16 | 25,00% | 0,48 | €-15,31 | 4,68% |
| TEST | Combo Adaptive Mfe Trail | Combo Adaptive | €9.622,22 | €-406,49 | 25 | 25 | 24,00% | 0,29 | €-16,26 | 4,11% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | DOGE | SHORT | Confluenza trend | 240m | 3,0x | 0,07292 | 0,07325 | 0,07500 | 0,09686 | 0,06875 | €574,44 | €1.723,33 | €49,28 | €-7,91 |
| Principale 4H | LAB | SHORT | Confluenza trend | 240m | 3,0x | 0,17841 | 0,17841 | 0,19982 | 0,23699 | 0,13559 | €136,26 | €408,77 | €49,05 | €-0,00 |
| Principale 4H | SUI | LONG | Confluenza trend | 240m | 3,0x | 0,76296 | 0,76296 | 0,73998 | 0,51245 | 0,80891 | €547,52 | €1.642,56 | €49,46 | €0,00 |
| Principale 4H | ONDO | LONG | Confluenza trend | 240m | 3,0x | 0,40344 | 0,39940 | 0,37762 | 0,27098 | 0,45509 | €254,70 | €764,09 | €48,91 | €-7,66 |
| Bilanciata 1H V1 | LAB | SHORT | Confluenza trend | 60m | 3,0x | 0,18667 | 0,18667 | 0,20845 | 0,24796 | 0,14311 | €143,84 | €431,52 | €50,35 | €-0,00 |
| Bilanciata 1H V1 | HYPE | SHORT | Confluenza trend | 60m | 3,0x | 60,62787 | 60,10400 | 61,73069 | 80,53402 | 58,42224 | €940,38 | €2.821,13 | €51,32 | €24,38 |
| Bilanciata 1H V1 | ONDO | LONG | Confluenza trend | 60m | 3,0x | 0,39694 | 0,39940 | 0,38539 | 0,26661 | 0,42004 | €581,76 | €1.745,29 | €50,78 | €10,83 |
| Bilanciata 1H V1 | ADA | LONG | Confluenza trend | 60m | 3,0x | 0,17389 | 0,17402 | 0,17086 | 0,11680 | 0,17996 | €973,58 | €2.920,73 | €50,89 | €2,10 |
| Bilanciata 1H V2 | LAB | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,18667 | 0,18667 | 0,20845 | 0,24796 | 0,14311 | €139,69 | €419,08 | €48,90 | €-0,00 |
| Bilanciata 1H V2 | GRAM | SHORT | Confluenza trend V2 | 60m | 3,0x | 1,49240 | 1,49240 | 1,53621 | 1,98241 | 1,40478 | €570,19 | €1.710,58 | €50,21 | €-0,00 |
| Bilanciata 1H V2 | ESPORTS | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,02164 | 0,02164 | 0,02164 | 0,02874 | 0,01644 | €138,69 | €416,06 | €0,00 | €-0,00 |
| Bilanciata 1H V3 Filtered | ESPORTS | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,02126 | 0,02126 | 0,02126 | 0,02823 | 0,01615 | €141,51 | €424,52 | €0,00 | €-0,00 |
| Bilanciata 1H V3 Filtered | ADA | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,17417 | 0,17402 | 0,17046 | 0,11699 | 0,18161 | €799,70 | €2.399,09 | €51,19 | €-2,13 |
| Bilanciata 1H V3 Filtered | HYPE | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 60,62787 | 60,10400 | 61,73069 | 80,53402 | 58,42224 | €943,48 | €2.830,45 | €51,49 | €24,46 |
| Bilanciata 1H V3 Filtered | ONDO | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,40134 | 0,39940 | 0,38898 | 0,26957 | 0,42605 | €557,59 | €1.672,77 | €51,50 | €-8,09 |
| Rapida 1H V1 | ESPORTS | SHORT | Momentum / breakout | 60m | 3,0x | 0,01984 | 0,01984 | 0,02222 | 0,02635 | 0,01627 | €129,65 | €388,96 | €46,68 | €-0,00 |
| Rapida 1H V1 | SUI | LONG | Momentum / breakout | 60m | 3,0x | 0,76416 | 0,76416 | 0,75422 | 0,51326 | 0,77907 | €1.284,19 | €3.852,58 | €50,12 | €0,00 |
| Rapida 1H V1 | ADA | LONG | Momentum / breakout | 60m | 3,0x | 0,17438 | 0,17402 | 0,17128 | 0,11713 | 0,17904 | €919,27 | €2.757,80 | €49,11 | €-5,77 |
| Rapida 1H V1 | ONDO | LONG | Momentum / breakout | 60m | 3,0x | 0,39924 | 0,39940 | 0,38995 | 0,26816 | 0,41318 | €708,01 | €2.124,02 | €49,43 | €0,85 |
| 1H Fast Score 6 75 V1 | BTC | LONG | Momentum / breakout | 60m | 3,0x | 66554,96833 | 66245,00000 | 65809,55269 | 44702,75373 | 67673,09180 | €1.485,18 | €4.455,53 | €49,90 | €-20,75 |
| 1H Fast Score 6 75 V1 | HYPE | SHORT | Momentum / breakout | 60m | 3,0x | 60,84083 | 60,10400 | 60,84083 | 80,81690 | 59,54085 | €1.161,85 | €3.485,54 | €0,00 | €42,21 |
| 1H Fast Score 6 75 V1 | ZEC | SHORT | Momentum / breakout | 60m | 3,0x | 521,71564 | 522,96000 | 531,34084 | 693,01227 | 507,27783 | €892,18 | €2.676,55 | €49,38 | €-6,38 |
| 1H Fast Nohigh Cap75 V1 | ONDO | LONG | Momentum / breakout | 60m | 3,0x | 0,39924 | 0,39940 | 0,38995 | 0,26816 | 0,41318 | €704,39 | €2.113,17 | €49,18 | €0,85 |
| 1H Fast Nohigh Cap75 V1 | HYPE | SHORT | Momentum / breakout | 60m | 3,0x | 60,91282 | 60,10400 | 60,91282 | 80,91252 | 59,60809 | €1.146,17 | €3.438,50 | €0,00 | €45,66 |
| 1H Fast Nohigh Cap75 V1 | ZEC | SHORT | Momentum / breakout | 60m | 3,0x | 521,98558 | 522,96000 | 531,61577 | 693,37085 | 507,54030 | €885,84 | €2.657,52 | €49,03 | €-4,96 |
| 1H Fast No Pepe V1 | BTC | LONG | Momentum / breakout | 60m | 3,0x | 66554,96833 | 66245,00000 | 65809,55269 | 44702,75373 | 67673,09180 | €1.486,49 | €4.459,46 | €49,95 | €-20,77 |
| 1H Fast No Pepe V1 | AKE | SHORT | Momentum / breakout | 60m | 3,0x | 0,00160 | 0,00171 | 0,00179 | 0,00212 | 0,00131 | €135,40 | €406,19 | €48,74 | €-27,65 |
| 1H Fast No Pepe V1 | ONDO | LONG | Momentum / breakout | 60m | 3,0x | 0,39924 | 0,39940 | 0,38995 | 0,26816 | 0,41318 | €713,68 | €2.141,05 | €49,83 | €0,86 |
| 1H Fast No Pepe V1 | HYPE | SHORT | Momentum / breakout | 60m | 3,0x | 60,91282 | 60,10400 | 60,91282 | 80,91252 | 59,60809 | €1.162,96 | €3.488,87 | €0,00 | €46,33 |
| 1H Fast Tp2 V1 | BTC | LONG | Momentum / breakout | 60m | 3,0x | 66554,96833 | 66245,00000 | 65809,55269 | 44702,75373 | 68045,79962 | €1.486,49 | €4.459,46 | €49,95 | €-20,77 |
| 1H Fast Tp2 V1 | AKE | SHORT | Momentum / breakout | 60m | 3,0x | 0,00160 | 0,00171 | 0,00179 | 0,00212 | 0,00121 | €135,40 | €406,19 | €48,74 | €-27,65 |
| 1H Fast Tp2 V1 | HYPE | SHORT | Momentum / breakout | 60m | 3,0x | 60,45591 | 60,10400 | 61,28705 | 80,30560 | 58,79362 | €1.213,20 | €3.639,60 | €50,04 | €21,19 |
| 1H Fast Tp2 V1 | ONDO | LONG | Momentum / breakout | 60m | 3,0x | 0,39924 | 0,39940 | 0,38995 | 0,26816 | 0,41782 | €712,92 | €2.138,77 | €49,77 | €0,86 |
| Rapida 1H V3 Filtered | ESPORTS | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01977 | 0,01977 | 0,02214 | 0,02626 | 0,01621 | €137,70 | €413,09 | €49,57 | €-0,00 |
| Rapida 1H V3 Filtered | SUI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,76416 | 0,76416 | 0,75422 | 0,51326 | 0,77907 | €1.267,97 | €3.803,92 | €49,49 | €0,00 |
| Rapida 1H V3 Filtered | ONDO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,39924 | 0,39940 | 0,38995 | 0,26816 | 0,41318 | €715,14 | €2.145,42 | €49,93 | €0,86 |
| Rapida 1H V3 Filtered | HYPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 60,84083 | 60,10400 | 60,84083 | 80,81690 | 59,54085 | €1.165,04 | €3.495,13 | €0,00 | €42,33 |
| 1H Fast V3 Cap75 V1 | BTC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 66554,96833 | 66245,00000 | 65809,55269 | 44702,75373 | 67673,09180 | €1.485,18 | €4.455,53 | €49,90 | €-20,75 |
| 1H Fast V3 Cap75 V1 | ONDO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,39924 | 0,39940 | 0,38995 | 0,26816 | 0,41318 | €712,28 | €2.136,85 | €49,73 | €0,86 |
| 1H Fast V3 Cap75 V1 | HYPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 60,84083 | 60,10400 | 60,84083 | 80,81690 | 59,54085 | €1.144,77 | €3.434,32 | €0,00 | €41,59 |
| 1H Fast V3 Cap75 V1 | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 521,71564 | 522,96000 | 531,34084 | 693,01227 | 507,27783 | €885,58 | €2.656,73 | €49,01 | €-6,34 |
| 1H Fast V3 Nohigh V1 | ONDO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,39924 | 0,39940 | 0,38995 | 0,26816 | 0,41318 | €707,41 | €2.122,22 | €49,39 | €0,85 |
| 1H Fast V3 Nohigh V1 | HYPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 60,84783 | 60,10400 | 60,84783 | 80,82620 | 59,54769 | €1.133,62 | €3.400,85 | €0,00 | €41,57 |
| 1H Fast V3 Nohigh V1 | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 521,98558 | 522,96000 | 531,61577 | 693,37085 | 507,54030 | €888,54 | €2.665,63 | €49,18 | €-4,98 |
| 1H Fast V3 Long Only V1 | BTC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 66554,96833 | 66245,00000 | 65809,55269 | 44702,75373 | 67673,09180 | €1.498,33 | €4.495,00 | €50,34 | €-20,93 |
| 1H Fast V3 No Esports V1 | BTC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 66554,96833 | 66245,00000 | 65809,55269 | 44702,75373 | 67673,09180 | €1.485,18 | €4.455,53 | €49,90 | €-20,75 |
| 1H Fast V3 No Esports V1 | ONDO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,39924 | 0,39940 | 0,38995 | 0,26816 | 0,41318 | €712,28 | €2.136,85 | €49,73 | €0,86 |
| 1H Fast V3 No Esports V1 | HYPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 60,84083 | 60,10400 | 60,84083 | 80,81690 | 59,54085 | €1.144,77 | €3.434,32 | €0,00 | €41,59 |
| 1H Fast V3 No Esports V1 | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 521,71564 | 522,96000 | 531,34084 | 693,01227 | 507,27783 | €885,58 | €2.656,73 | €49,01 | €-6,34 |
| Ampia 4H | DOGE | SHORT | Confluenza trend | 240m | 2,0x | 0,07237 | 0,07325 | 0,07515 | 0,10819 | 0,06457 | €649,49 | €1.298,97 | €50,00 | €-15,86 |
| Ampia 4H | ZEC | LONG | Confluenza trend | 240m | 2,0x | 522,36445 | 522,96000 | 483,09844 | 263,79405 | 632,30930 | €332,53 | €665,06 | €49,99 | €0,76 |
| Ampia 4H | PEPE | LONG | Confluenza trend | 240m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €497,18 | €994,35 | €50,70 | €-0,68 |
| Ampia 4H | ETH | LONG | Confluenza trend | 240m | 2,0x | 1933,63665 | 1932,65000 | 1869,00475 | 976,48651 | 2114,60597 | €756,64 | €1.513,28 | €50,58 | €-0,77 |
| Forza relativa 1H V1 | ESPORTS | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,02126 | 0,02126 | 0,02126 | 0,03178 | 0,01564 | €208,05 | €416,10 | €0,00 | €-0,00 |
| Forza relativa 1H V1 | PEPE | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €986,47 | €1.972,93 | €50,47 | €-32,16 |
| Forza relativa 1H V1 | NIGHT | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,02031 | 0,02031 | 0,02210 | 0,03036 | 0,01637 | €285,91 | €571,83 | €50,45 | €-0,00 |
| Forza relativa 1H V1 | XRP | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 1,15268 | 1,14138 | 1,13608 | 0,58210 | 1,18920 | €1.735,62 | €3.471,23 | €49,99 | €-34,03 |
| Forza relativa 1H V2 | LAB | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,18833 | 0,18833 | 0,20950 | 0,28155 | 0,14176 | €222,78 | €445,56 | €50,08 | €-0,00 |
| Forza relativa 1H V2 | GRAM | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 1,47771 | 1,47771 | 1,52060 | 2,20918 | 1,38336 | €871,54 | €1.743,07 | €50,59 | €-0,00 |
| Forza relativa 1H V2 | ESPORTS | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,02126 | 0,02126 | 0,02126 | 0,03178 | 0,01564 | €215,33 | €430,67 | €0,00 | €-0,00 |
| Forza relativa 1H V2 | ADA | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,17438 | 0,17402 | 0,17039 | 0,08806 | 0,18317 | €1.109,61 | €2.219,23 | €50,81 | €-4,64 |
| Benchmark Donchian breakout 1H | SUI | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,76606 | 0,76606 | 0,75182 | 0,38686 | 0,80165 | €1.377,00 | €2.754,00 | €51,18 | €0,00 |
| Benchmark Donchian breakout 1H | ADA | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,17562 | 0,17402 | 0,17105 | 0,08869 | 0,18704 | €975,80 | €1.951,59 | €50,78 | €-17,73 |
| Benchmark Bollinger mean reversion 1H | HYPE | LONG | Bollinger mean reversion | 60m | 2,0x | 60,65213 | 60,10400 | 59,73275 | 30,62932 | 62,03120 | €1.683,41 | €3.366,81 | €51,04 | €-30,43 |
| Benchmark trend following EMA 1H | ADA | LONG | Trend following EMA | 60m | 2,0x | 0,17417 | 0,17402 | 0,17005 | 0,08796 | 0,18326 | €1.046,69 | €2.093,39 | €49,63 | €-1,86 |
| Benchmark trend following EMA 1H | BTC | LONG | Trend following EMA | 60m | 2,0x | 66805,45842 | 66245,00000 | 65736,57109 | 33736,75650 | 69157,01056 | €1.553,66 | €3.107,32 | €49,72 | €-26,07 |
| Benchmark trend following EMA 1H | HYPE | SHORT | Trend following EMA | 60m | 2,0x | 60,84083 | 60,10400 | 62,07891 | 90,95704 | 58,11705 | €1.213,82 | €2.427,65 | €49,40 | €29,40 |
| Scanner Top 5 Long 1H | ADA | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,17562 | 0,17402 | 0,17150 | 0,08869 | 0,18384 | €1.118,38 | €2.236,77 | €52,38 | €-20,32 |
| Scanner Top 5 Long 1H | BTC | LONG | Scanner Top 5 Long | 60m | 2,0x | 66805,45842 | 66245,00000 | 65843,45982 | 33736,75650 | 68729,45562 | €1.827,61 | €3.655,23 | €52,64 | €-30,67 |
| Scanner Top 5 Long 1H | ONDO | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,40114 | 0,39940 | 0,38834 | 0,20258 | 0,42673 | €828,91 | €1.657,82 | €52,88 | €-7,19 |
| Scanner Bottom 5 Short 1H | ESPORTS | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,02150 | 0,02150 | 0,02150 | 0,03214 | 0,01634 | €207,40 | €414,80 | €0,00 | €-0,00 |
| Scanner Bottom 5 Short 1H | AKE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,00168 | 0,00171 | 0,00188 | 0,00251 | 0,00127 | €203,54 | €407,07 | €48,85 | €-6,87 |
| Scanner Bottom 5 Short 1H | ZEC | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 521,71564 | 522,96000 | 534,09090 | 779,96488 | 496,96511 | €1.029,27 | €2.058,54 | €48,83 | €-4,91 |
| Scanner Top 5 + forza BTC 1H | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 77,70854 | 77,84300 | 76,45304 | 39,24281 | 80,47063 | €1.614,82 | €3.229,64 | €52,18 | €5,59 |
| Scanner Top 5 + forza BTC 1H | XRP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,14884 | 1,14138 | 1,13230 | 0,58016 | 1,18523 | €1.810,65 | €3.621,30 | €52,15 | €-23,51 |
| Scanner Top 5 + forza BTC 1H | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39694 | 0,39940 | 0,38539 | 0,20045 | 0,42235 | €898,57 | €1.797,15 | €52,29 | €11,15 |
| Scanner Top5 Btc Mfe V1 | SUI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,76776 | 0,76776 | 0,75508 | 0,38772 | 0,79565 | €1.514,04 | €3.028,08 | €50,00 | €0,00 |
| Scanner Top5 Btc Mfe V1 | ADA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,17562 | 0,17402 | 0,17150 | 0,08869 | 0,18466 | €1.073,91 | €2.147,81 | €50,30 | €-19,51 |
| Scanner Top5 Btc Mfe V1 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39924 | 0,39940 | 0,38729 | 0,20162 | 0,42552 | €835,46 | €1.670,91 | €50,00 | €0,67 |
| Scanner Top5 Btc Guard V1 | ADA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,17562 | 0,17402 | 0,17150 | 0,08869 | 0,18466 | €1.054,77 | €2.109,54 | €49,40 | €-19,16 |
| Scanner Top5 Btc Guard V1 | XRP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,14947 | 1,14138 | 1,13292 | 0,58048 | 1,18589 | €1.706,64 | €3.413,29 | €49,15 | €-24,02 |
| Scanner Top5 Btc Guard V1 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39724 | 0,39940 | 0,38434 | 0,20061 | 0,42561 | €756,62 | €1.513,24 | €49,13 | €8,24 |
| Scanner Top5 Btc Btc Le3 V1 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.063,01 | €2.126,01 | €50,00 | €-29,91 |
| Scanner Top5 Btc Btc Le3 V1 | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 77,78955 | 77,84300 | 76,66939 | 39,28373 | 80,25393 | €1.735,32 | €3.470,64 | €49,98 | €2,38 |
| Scanner Top5 Btc Btc Le3 V1 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39974 | 0,39940 | 0,38840 | 0,20187 | 0,42468 | €884,65 | €1.769,29 | €50,18 | €-1,50 |
| Scanner Top5 Btc Btc 2 3 V1 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.063,01 | €2.126,01 | €50,00 | €-29,91 |
| Scanner Top5 Btc Btc 2 3 V1 | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 77,78955 | 77,84300 | 76,66939 | 39,28373 | 80,25393 | €1.735,32 | €3.470,64 | €49,98 | €2,38 |
| Scanner Top5 Btc Btc 2 3 V1 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39974 | 0,39940 | 0,38840 | 0,20187 | 0,42468 | €884,65 | €1.769,29 | €50,18 | €-1,50 |
| Scanner Top5 Btc Guard Mfe V1 | ADA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,17562 | 0,17402 | 0,17150 | 0,08869 | 0,18466 | €1.054,77 | €2.109,54 | €49,40 | €-19,16 |
| Scanner Top5 Btc Guard Mfe V1 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39724 | 0,39940 | 0,38434 | 0,20061 | 0,42561 | €756,62 | €1.513,24 | €49,13 | €8,24 |
| Scanner Top5 Btc Guard Btc Le3 V1 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39974 | 0,39940 | 0,38840 | 0,20187 | 0,42468 | €871,05 | €1.742,11 | €49,41 | €-1,48 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39974 | 0,39940 | 0,38840 | 0,20187 | 0,42468 | €871,05 | €1.742,11 | €49,41 | €-1,48 |
| Scanner Top5 Btc Runner25 V1 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.031,84 | €2.063,68 | €50,00 | €-30,36 |
| Scanner Top5 Btc Runner25 V1 | ADA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,17487 | 0,17402 | 0,17143 | 0,08831 | 0,18521 | €1.286,71 | €2.573,42 | €50,71 | €-12,58 |
| Scanner Top5 Btc Runner25 V1 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39694 | 0,39940 | 0,38539 | 0,20045 | 0,43159 | €861,83 | €1.723,66 | €50,15 | €10,69 |
| Scanner Top5 Btc Tp3 V1 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.031,84 | €2.063,68 | €50,00 | €-30,36 |
| Scanner Top5 Btc Tp3 V1 | ADA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,17487 | 0,17402 | 0,17143 | 0,08831 | 0,18521 | €1.286,71 | €2.573,42 | €50,71 | €-12,58 |
| Scanner Top5 Btc Tp3 V1 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39694 | 0,39940 | 0,38539 | 0,20045 | 0,43159 | €861,83 | €1.723,66 | €50,15 | €10,69 |
| Combo Trend | ONDO | LONG | Combo Trend | 60m | 2,0x | 0,37282 | 0,39940 | 0,39131 | 0,18828 | 0,41057 | €545,86 | €1.091,71 | €0,00 | €77,82 |
| Combo Trend | ESPORTS | SHORT | Combo Trend | 60m | 2,0x | 0,01883 | 0,01883 | 0,02109 | 0,02815 | 0,01386 | €209,57 | €419,14 | €50,30 | €-0,00 |
| Combo Trend | PEPE | LONG | Combo Trend | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €884,51 | €1.769,01 | €50,29 | €-28,83 |
| Combo Mean Reversion | ZEC | LONG | Combo Mean Reversion | 60m | 2,0x | 521,92436 | 522,96000 | 511,60752 | 263,57180 | 538,43131 | €1.289,42 | €2.578,84 | €50,98 | €5,12 |
| Combo Scanner | PEPE | LONG | Combo Scanner | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €978,80 | €1.957,60 | €50,08 | €-31,91 |
| Combo Scanner | ONDO | LONG | Combo Scanner | 60m | 2,0x | 0,39694 | 0,39940 | 0,38539 | 0,20045 | 0,42235 | €857,88 | €1.715,77 | €49,92 | €10,64 |
| Combo Adaptive | GRAM | SHORT | Combo Adaptive | 60m | 2,0x | 1,48181 | 1,48181 | 1,51561 | 2,21531 | 1,41422 | €1.129,35 | €2.258,70 | €51,51 | €-0,00 |
| Combo Adaptive | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.001,06 | €2.002,12 | €51,22 | €-32,63 |
| Combo Adaptive | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,40114 | 0,39940 | 0,38834 | 0,20258 | 0,42673 | €809,25 | €1.618,50 | €51,63 | €-7,02 |
| Combo Adaptive Mfe Trail | ESPORTS | SHORT | Combo Adaptive | 60m | 2,0x | 0,02156 | 0,02156 | 0,02091 | 0,03223 | 0,01638 | €202,62 | €405,24 | €0,00 | €-0,00 |
| Combo Adaptive Mfe Trail | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39784 | 0,39940 | 0,38492 | 0,20091 | 0,42367 | €744,71 | €1.489,41 | €48,35 | €5,85 |
| Combo Adaptive Mfe Trail | HYPE | SHORT | Combo Adaptive | 60m | 2,0x | 60,66986 | 60,10400 | 61,73458 | 90,70145 | 58,54043 | €1.366,73 | €2.733,47 | €47,97 | €25,49 |
| Combo Adaptive Quality7 V1 | ADA | LONG | Combo Adaptive | 60m | 2,0x | 0,17562 | 0,17402 | 0,17150 | 0,08869 | 0,18384 | €1.067,59 | €2.135,18 | €50,00 | €-19,39 |
| Combo Adaptive Quality7 V1 | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,40304 | 0,39940 | 0,39140 | 0,20354 | 0,42632 | €859,15 | €1.718,30 | €49,62 | €-15,53 |
| Combo Adaptive Regime V1 | ADA | LONG | Combo Adaptive | 60m | 2,0x | 0,17562 | 0,17402 | 0,17150 | 0,08869 | 0,18384 | €1.064,94 | €2.129,87 | €49,88 | €-19,35 |
| Combo Adaptive Regime V1 | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39724 | 0,39940 | 0,38434 | 0,20061 | 0,42303 | €757,94 | €1.515,88 | €49,21 | €8,25 |
| Combo Adaptive Regime V1 | HYPE | SHORT | Combo Adaptive | 60m | 2,0x | 60,62787 | 60,10400 | 61,73069 | 90,63867 | 58,42224 | €1.352,45 | €2.704,89 | €49,20 | €23,37 |
| Combo Adaptive Quality7 Regime V1 | ADA | LONG | Combo Adaptive | 60m | 2,0x | 0,17562 | 0,17402 | 0,17150 | 0,08869 | 0,18384 | €1.067,59 | €2.135,18 | €50,00 | €-19,39 |
| Combo Adaptive Quality7 Regime V1 | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,40554 | 0,39940 | 0,39390 | 0,20480 | 0,42882 | €864,27 | €1.728,54 | €49,61 | €-26,18 |
| Combo Adaptive Long Only V1 | ADA | LONG | Combo Adaptive | 60m | 2,0x | 0,17562 | 0,17402 | 0,17150 | 0,08869 | 0,18384 | €1.070,78 | €2.141,56 | €50,15 | €-19,45 |
| Combo Adaptive Long Only V1 | BTC | LONG | Combo Adaptive | 60m | 2,0x | 66665,25038 | 66245,00000 | 65705,27078 | 33665,95144 | 68585,20960 | €1.731,23 | €3.462,46 | €49,86 | €-21,83 |
| Combo Adaptive Partial 1R V1 | ADA | LONG | Combo Adaptive | 60m | 2,0x | 0,17562 | 0,17402 | 0,17150 | 0,08869 | 0,18384 | €1.062,51 | €2.125,02 | €49,76 | €-19,30 |
| Combo Adaptive Partial 1R V1 | BTC | LONG | Combo Adaptive | 60m | 2,0x | 66665,25038 | 66245,00000 | 65705,27078 | 33665,95144 | 68585,20960 | €1.712,08 | €3.424,17 | €49,31 | €-21,59 |
| Combo Adaptive Partial 1R V1 | HYPE | SHORT | Combo Adaptive | 60m | 2,0x | 60,84083 | 60,10400 | 61,95510 | 90,95704 | 58,61229 | €1.342,99 | €2.685,97 | €49,19 | €32,53 |
| Combo Adaptive Quality7 Regime Partial 1R V1 | ADA | LONG | Combo Adaptive | 60m | 2,0x | 0,17562 | 0,17402 | 0,17150 | 0,08869 | 0,18384 | €1.067,59 | €2.135,18 | €50,00 | €-19,39 |
| Combo Adaptive Quality7 Regime Partial 1R V1 | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,40554 | 0,39940 | 0,39390 | 0,20480 | 0,42882 | €864,27 | €1.728,54 | €49,61 | €-26,18 |
| Combo Adaptive Runner25 V1 | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.031,84 | €2.063,68 | €50,00 | €-30,36 |
| Combo Adaptive Runner25 V1 | BTC | LONG | Combo Adaptive | 60m | 2,0x | 66575,01234 | 66245,00000 | 65616,33216 | 33620,38123 | 69451,05287 | €1.723,18 | €3.446,36 | €49,63 | €-17,08 |
| Combo Adaptive Runner25 V1 | HYPE | SHORT | Combo Adaptive | 60m | 2,0x | 60,84083 | 60,10400 | 61,95510 | 90,95704 | 57,49801 | €1.355,59 | €2.711,19 | €49,65 | €32,83 |
| Combo Adaptive Tp3 V1 | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.031,84 | €2.063,68 | €50,00 | €-30,36 |
| Combo Adaptive Tp3 V1 | BTC | LONG | Combo Adaptive | 60m | 2,0x | 66575,01234 | 66245,00000 | 65616,33216 | 33620,38123 | 69451,05287 | €1.723,18 | €3.446,36 | €49,63 | €-17,08 |
| Combo Adaptive Tp3 V1 | HYPE | SHORT | Combo Adaptive | 60m | 2,0x | 60,84083 | 60,10400 | 61,95510 | 90,95704 | 57,49801 | €1.355,59 | €2.711,19 | €49,65 | €32,83 |
| Btc Ema 1H | BTC | LONG | Trend following EMA | 60m | 3,0x | 66655,79849 | 66245,00000 | 65695,95500 | 44770,47799 | 68575,48549 | €1.155,97 | €3.467,90 | €49,94 | €-21,37 |
| Btc Ema 4H | BTC | LONG | Trend following EMA | 240m | 2,0x | 65410,57950 | 66245,00000 | 63931,54687 | 33032,34265 | 69108,16107 | €1.105,63 | €2.211,26 | €50,00 | €28,21 |
| Btc Donchian 4H | BTC | LONG | Donchian breakout 20 barre | 240m | 2,0x | 65410,57950 | 66245,00000 | 63931,54687 | 33032,34265 | 69551,87112 | €1.105,63 | €2.211,26 | €50,00 | €28,21 |
| Btc Bollinger 1H | BTC | SHORT | Bollinger mean reversion | 60m | 3,0x | 66739,44944 | 66245,00000 | 67540,32283 | 88652,23534 | 65538,13935 | €1.398,43 | €4.195,29 | €50,34 | €31,08 |
| Btc Bollinger 4H | BTC | SHORT | Bollinger mean reversion | 240m | 2,0x | 66588,49964 | 66245,00000 | 67855,55360 | 99549,80696 | 64307,80290 | €1.313,84 | €2.627,69 | €50,00 | €13,56 |
| Btc Adaptive 4H | BTC | LONG | Combo Adaptive | 240m | 2,0x | 66171,85172 | 66245,00000 | 64592,42491 | 33416,78512 | 70120,41876 | €1.047,40 | €2.094,81 | €50,00 | €2,32 |
| Sol Ema 1H | SOL | LONG | Trend following EMA | 60m | 3,0x | 77,56451 | 77,84300 | 76,27481 | 52,09750 | 80,14392 | €1.001,44 | €3.004,32 | €49,95 | €10,79 |
| Sol Ema 4H | SOL | LONG | Trend following EMA | 240m | 2,0x | 78,49069 | 77,84300 | 76,26213 | 39,63780 | 84,06211 | €880,51 | €1.761,01 | €50,00 | €-14,53 |
| Sol Donchian 4H | SOL | LONG | Donchian breakout 20 barre | 240m | 2,0x | 78,49069 | 77,84300 | 76,26213 | 39,63780 | 84,73068 | €880,51 | €1.761,01 | €50,00 | €-14,53 |
| Sol Bollinger 4H | SOL | SHORT | Bollinger mean reversion | 240m | 2,0x | 78,45931 | 77,84300 | 80,48446 | 117,29666 | 74,81402 | €968,56 | €1.937,11 | €50,00 | €15,22 |
| Sol Adaptive 1H | SOL | LONG | Combo Adaptive | 60m | 3,0x | 77,56451 | 77,84300 | 76,27481 | 52,09750 | 80,14392 | €1.000,51 | €3.001,52 | €49,91 | €10,78 |
| Sol Adaptive 4H | SOL | LONG | Combo Adaptive | 240m | 2,0x | 78,49069 | 77,84300 | 76,05953 | 39,63780 | 84,56860 | €807,13 | €1.614,26 | €50,00 | €-13,32 |
| Eth Ema 1H | ETH | LONG | Trend following EMA | 60m | 3,0x | 1935,54703 | 1932,65000 | 1907,67515 | 1300,04242 | 1991,29079 | €1.144,65 | €3.433,94 | €49,45 | €-5,14 |
| Eth Ema 4H | ETH | LONG | Trend following EMA | 240m | 2,0x | 1933,63665 | 1932,65000 | 1878,94813 | 976,48651 | 2070,35799 | €883,93 | €1.767,86 | €50,00 | €-0,90 |
| Master Adaptive V1 | ADA | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,17603 | 0,17402 | 0,17190 | 0,08889 | 0,18427 | €1.067,59 | €2.135,18 | €50,00 | €-24,32 |
| Master Adaptive V1 | BTC | LONG | Master Adaptive Consensus | 60m | 2,0x | 66665,25038 | 66245,00000 | 65705,27078 | 33665,95144 | 68585,20960 | €1.722,26 | €3.444,53 | €49,60 | €-21,71 |
| Master Adaptive V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39854 | 0,39940 | 0,38677 | 0,20126 | 0,42207 | €833,00 | €1.665,99 | €49,19 | €3,60 |
| Master Adaptive No Alt V1 | ADA | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,17603 | 0,17402 | 0,17190 | 0,08889 | 0,18427 | €1.067,59 | €2.135,18 | €50,00 | €-24,32 |
| Master Adaptive No Alt V1 | BTC | LONG | Master Adaptive Consensus | 60m | 2,0x | 66665,25038 | 66245,00000 | 65705,27078 | 33665,95144 | 68585,20960 | €1.722,26 | €3.444,53 | €49,60 | €-21,71 |
| Master Adaptive No Alt V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39854 | 0,39940 | 0,38677 | 0,20126 | 0,42207 | €833,00 | €1.665,99 | €49,19 | €3,60 |
| Master Adaptive Strict3 V1 | ADA | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,17603 | 0,17402 | 0,17190 | 0,08889 | 0,18427 | €1.067,59 | €2.135,18 | €50,00 | €-24,32 |
| Master Adaptive Strict3 V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 1934,24677 | 1932,65000 | 1906,39362 | 976,79462 | 1989,95308 | €1.737,12 | €3.474,23 | €50,03 | €-2,87 |
| Master Adaptive Strict3 V1 | XRP | LONG | Master Adaptive Consensus | 60m | 2,0x | 1,14947 | 1,14138 | 1,13292 | 0,58048 | 1,18257 | €1.722,92 | €3.445,84 | €49,62 | €-24,25 |
| Master Adaptive Expanded V1 | ADA | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,17603 | 0,17402 | 0,17190 | 0,08889 | 0,18427 | €1.067,59 | €2.135,18 | €50,00 | €-24,32 |
| Master Adaptive Expanded V1 | BTC | LONG | Master Adaptive Consensus | 60m | 2,0x | 66665,25038 | 66245,00000 | 65705,27078 | 33665,95144 | 68585,20960 | €1.722,26 | €3.444,53 | €49,60 | €-21,71 |
| Master Adaptive Expanded V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39854 | 0,39940 | 0,38677 | 0,20126 | 0,42207 | €833,00 | €1.665,99 | €49,19 | €3,60 |
| Master Adaptive Gb20 V1 | ADA | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,17603 | 0,17402 | 0,17190 | 0,08889 | 0,18427 | €1.067,59 | €2.135,18 | €50,00 | €-24,32 |
| Master Adaptive Gb20 V1 | BTC | LONG | Master Adaptive Consensus | 60m | 2,0x | 66665,25038 | 66245,00000 | 65705,27078 | 33665,95144 | 68585,20960 | €1.718,57 | €3.437,14 | €49,49 | €-21,67 |
| Master Adaptive Gb20 V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,40304 | 0,39940 | 0,39140 | 0,20354 | 0,42632 | €848,64 | €1.697,27 | €49,02 | €-15,34 |
| Master Adaptive Runner25 V1 | ADA | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,17603 | 0,17402 | 0,17190 | 0,08889 | 0,18839 | €1.067,59 | €2.135,18 | €50,00 | €-24,32 |
| Master Adaptive Runner25 V1 | BTC | LONG | Master Adaptive Consensus | 60m | 2,0x | 66665,25038 | 66245,00000 | 65705,27078 | 33665,95144 | 69545,18920 | €1.722,26 | €3.444,53 | €49,60 | €-21,71 |
| Master Adaptive Runner25 V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39854 | 0,39940 | 0,38677 | 0,20126 | 0,43384 | €833,00 | €1.665,99 | €49,19 | €3,60 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1H Fast Nohigh Cap75 V1 | AKE | SHORT | 2026-07-22T04:38:33+00:00 | 0,00171 | €-48,97 | -1,02 | STOP |
| 1H Fast V3 Nohigh V1 | ZEC | SHORT | 2026-07-22T04:08:33+00:00 | 518,19437 | €71,05 | 1,43 | TARGET |
| 1H Fast Nohigh Cap75 V1 | ZEC | SHORT | 2026-07-22T04:08:33+00:00 | 518,19437 | €70,66 | 1,43 | TARGET |
| Principale 4H | ZEC | LONG | 2026-07-22T04:08:33+00:00 | 524,53223 | €-51,77 | -1,04 | STOP |
| 1H Fast V3 Long Only V1 | ONDO | LONG | 2026-07-22T03:53:33+00:00 | 0,39720 | €-1,19 | -0,02 | STOP |
| 1H Fast V3 Long Nohigh Cap75 V1 | ONDO | LONG | 2026-07-22T03:53:33+00:00 | 0,39720 | €-1,18 | -0,02 | STOP |
| 1H Fast Score 6 75 V1 | ONDO | LONG | 2026-07-22T03:53:33+00:00 | 0,39720 | €-1,19 | -0,02 | STOP |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | ONDO | LONG | 2026-07-22T03:38:33+00:00 | 0,39894 | €8,38 | 0,17 | STOP |
| 1H Fast V3 No Esports V1 | BANK | SHORT | 2026-07-22T03:23:33+00:00 | 0,18208 | €-55,29 | -1,11 | STOP_STRESS_SLIPPAGE |
| 1H Fast V3 Nohigh V1 | BANK | SHORT | 2026-07-22T03:23:33+00:00 | 0,18208 | €-54,13 | -1,11 | STOP_STRESS_SLIPPAGE |
| 1H Fast V3 Cap75 V1 | BANK | SHORT | 2026-07-22T03:23:33+00:00 | 0,18208 | €-55,29 | -1,11 | STOP_STRESS_SLIPPAGE |
| 1H Fast Score 6 75 V1 | BANK | SHORT | 2026-07-22T03:23:33+00:00 | 0,18208 | €-55,31 | -1,11 | STOP_STRESS_SLIPPAGE |

## Regole invarianti

- Nessuna martingala e nessuna mediazione automatica in perdita.
- Il target mensile riduce il rischio quando viene avvicinato o raggiunto; non lo aumenta mai.
- Il portafoglio principale e le simulazioni di confronto hanno contabilità separata.
- Commissioni, slippage e funding sono inclusi nella simulazione secondo i parametri configurati.
- Quando stop e target risultano toccati nella stessa candela, prevale lo stop salvo modifica esplicita della configurazione.
