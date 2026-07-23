# Paper trading automatico KuCoin

Generato: 2026-07-23T01:08:50+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-07-23T01:08:24+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-07-23T01:08:24+00:00 | 2026-07-23T01:08:24+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-07-23T00:45:00+00:00 | 2026-07-23T00:45:00+00:00 | 8,5 min | 25,0 min | OK |
| 60m | 12 | 2026-07-23T00:00:00+00:00 | 2026-07-23T00:00:00+00:00 | 8,5 min | 45,0 min | OK |
| 240m | 12 | 2026-07-22T20:00:00+00:00 | 2026-07-22T20:00:00+00:00 | 1,14 h | 1,00 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | BANK | 240m | LONG | 7,75 | 6,00 | 0,00 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | HYPE | 240m | SHORT | -7,25 | 6,00 | 0,00 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | ETH | 240m | LONG | 6,32 | 6,00 | 0,00 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | AKE | 240m | LONG | 6,25 | 6,00 | 0,00 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | LAB | 240m | SHORT | -6,25 | 6,00 | 0,00 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | ADA | 240m | LONG | 6,21 | 6,00 | 0,00 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | PEPE | 240m | LONG | 6,12 | 6,00 | 0,00 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | XRP | 240m | LONG | 4,62 | 6,00 | 1,38 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | ZEC | 240m | SHORT | -3,99 | 6,00 | 2,01 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | DOGE | 240m | SHORT | -3,98 | 6,00 | 2,02 | STALE_CANDLE | 1,14 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | BTC | 240m | LONG | 3,25 | 6,00 | 2,75 | STALE_CANDLE | 1,14 h | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | SOL | 240m | LONG | 2,70 | 6,00 | 3,30 | STALE_CANDLE | 1,14 h | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Forza relativa 1H V2 | BANK | 60m | LONG | 5,50 | 5,50 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Mean Reversion | BANK | 60m | LONG | 5,50 | 5,00 | 0,00 | READY | 8,5 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Master Adaptive Strict3 V1 | BANK | 60m | LONG | 5,50 | 0,00 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Bottom 5 Short 1H | ZEC | 60m | SHORT | -5,14 | 5,00 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Bilanciata 1H V2 | BANK | 60m | LONG | 5,50 | 5,50 | 0,00 | STRATEGY_FILTER | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro V2 non superato: regime, EMA, ritorni e RSI; per Rapida V2 servono anche breakout reale, volume e ADX. |
| Rapida 1H V2 | BANK | 60m | LONG | 5,50 | 5,00 | 0,00 | STRATEGY_FILTER | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro V2 non superato: regime, EMA, ritorni e RSI; per Rapida V2 servono anche breakout reale, volume e ADX. |
| Rapida 1H V1 — madre | ZEC | 60m | SHORT | -5,14 | 4,50 | 0,00 | STRATEGY_FILTER | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout DOWN oppure movimento breve ≥1,5%; breakout=NONE, movimento=+0.59%. |
| Rapida V1 — no HIGH + score <7,5 | ZEC | 60m | SHORT | -5,14 | 4,50 | 0,00 | STRATEGY_FILTER | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout DOWN oppure movimento breve ≥1,5%; breakout=NONE, movimento=+0.59%. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.908,51 | -0,91% | €-91,49 | €3.000,00 | -3,05% | 4 | 17 | 29,41% | 0,73 | 4,26% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 17 | 359 | CAMPIONE INSUFFICIENTE | 30 (mancano 13) |

- Trade del Principale 4H chiusi: **17**; win rate **29,41%**; profit factor **0,73**.
- Expectancy: **€-8,97** per trade; P&L netto: **€-152,45**; max drawdown: **4,26%**.
- Valutazione: **Servono altri eventi indipendenti prima di trarre conclusioni.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 4 | €9.908,51 | €1.512,92 | €4.538,75 | €147,66 | €60,24 |
| TEST | Scanner Top 5 Long 1H | 3 | €10.478,02 | €1.266,43 | €2.532,86 | €157,89 | €-34,51 |
| TEST | Scanner Top 5 + forza BTC 1H | 3 | €10.422,66 | €2.729,95 | €5.459,91 | €156,45 | €9,00 |
| TEST | Bilanciata 1H V3 Filtered | 3 | €10.273,87 | €1.437,73 | €4.313,18 | €103,07 | €-3,42 |
| TEST | Combo Adaptive — madre | 3 | €10.212,93 | €2.169,96 | €4.339,92 | €153,94 | €-24,35 |
| TEST | Bilanciata 1H V1 | 4 | €10.197,77 | €3.258,29 | €9.774,87 | €203,95 | €-6,45 |
| TEST | Benchmark Donchian breakout 1H | 3 | €10.135,15 | €3.555,00 | €7.109,99 | €152,79 | €-18,78 |
| TEST | Benchmark Bollinger mean reversion 1H | 1 | €10.117,57 | €1.299,75 | €2.599,50 | €50,41 | €2,97 |
| TEST | Btc Bollinger 1H | 0 | €10.099,96 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Mean Reversion | 0 | €10.085,92 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Forza relativa 1H V2 | 4 | €10.083,17 | €1.822,67 | €3.645,34 | €149,99 | €-31,23 |
| TEST | Ampia 4H | 4 | €10.071,99 | €2.235,83 | €4.471,66 | €201,27 | €-14,82 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €10.028,40 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 4H | 1 | €10.025,19 | €1.105,63 | €2.211,26 | €50,00 | €23,22 |
| TEST | Btc Donchian 4H | 1 | €10.025,19 | €1.105,63 | €2.211,26 | €50,00 | €23,22 |
| TEST | Sol Ema 1H | 1 | €10.017,92 | €1.001,44 | €3.004,32 | €49,95 | €28,49 |
| TEST | Btc Bollinger 4H | 1 | €10.016,05 | €1.313,84 | €2.627,69 | €50,00 | €19,38 |
| TEST | Eth Bollinger 1H | 0 | €10.015,45 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €50 · 15x | 0 | €10.014,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Top 5 + BTC — BTC≤3 | 3 | €10.009,24 | €2.827,84 | €5.655,68 | €150,04 | €7,82 |
| TEST | Top 5 + BTC — BTC 2–3 | 3 | €10.009,24 | €2.827,84 | €5.655,68 | €150,04 | €7,82 |
| TEST | Sol Adaptive 1H | 1 | €10.008,60 | €1.000,51 | €3.001,52 | €49,91 | €28,46 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 0 | €10.005,68 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 0 | €10.005,24 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €10 · 15x | 0 | €10.002,80 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 4H | 1 | €10.002,45 | €968,56 | €1.937,11 | €50,00 | €3,93 |
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
| TEST | Eth Ema 4H | 1 | €9.999,11 | €883,93 | €1.767,86 | €50,00 | €0,55 |
| TEST | Btc Adaptive 4H | 1 | €9.998,48 | €1.047,40 | €2.094,81 | €50,00 | €-2,35 |
| TEST | Sol Donchian 1H | 0 | €9.997,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 4H | 1 | €9.995,38 | €807,13 | €1.614,26 | €50,00 | €-3,92 |
| TEST | Sol Ema 4H | 1 | €9.994,96 | €880,51 | €1.761,01 | €50,00 | €-4,28 |
| TEST | Sol Donchian 4H | 1 | €9.994,96 | €880,51 | €1.761,01 | €50,00 | €-4,28 |
| TEST | Rapida 1H V3 Filtered — madre | 3 | €9.989,20 | €2.120,81 | €6.362,43 | €148,99 | €0,00 |
| TEST | Btc Adaptive 1H | 0 | €9.988,26 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H V2 | 3 | €9.985,10 | €1.062,51 | €3.187,53 | €100,42 | €-17,41 |
| TEST | Eth Donchian 1H | 0 | €9.982,54 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V1 — senza PEPE | 4 | €9.978,82 | €2.738,86 | €8.216,59 | €149,59 | €81,61 |
| TEST | Doge Donchian 1H | 0 | €9.968,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.964,86 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Adaptive 1H | 1 | €9.953,86 | €1.153,05 | €3.459,15 | €49,81 | €-6,48 |
| TEST | Top 5 + BTC — 75% a 2,2R + runner 3R | 3 | €9.948,74 | €1.277,26 | €2.554,51 | €149,85 | €-32,76 |
| TEST | Top 5 + BTC — target pieno 3R | 3 | €9.948,74 | €1.277,26 | €2.554,51 | €149,85 | €-32,76 |
| TEST | Doge Ema 1H | 0 | €9.948,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V2 | 0 | €9.944,87 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 1H | 0 | €9.944,21 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — target pieno 3R | 3 | €9.940,10 | €2.339,93 | €4.679,86 | €149,52 | €-21,71 |
| TEST | Btc Donchian 1H | 0 | €9.937,58 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 1H | 0 | €9.934,39 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V1 — target pieno 2R | 3 | €9.933,14 | €1.796,67 | €5.390,01 | €99,08 | €72,70 |
| TEST | Top 5 + BTC — solo MFE | 3 | €9.928,50 | €2.576,61 | €5.153,21 | €149,81 | €-33,65 |
| TEST | Combo Trend | 3 | €9.925,48 | €1.698,61 | €3.397,22 | €100,04 | €-22,98 |
| TEST | Rapida V1 — no HIGH + score <7,5 | 3 | €9.924,96 | €1.790,11 | €5.370,33 | €147,89 | €60,83 |
| TEST | Benchmark trend following EMA 1H | 2 | €9.917,75 | €1.141,40 | €2.282,79 | €99,49 | €-28,61 |
| TEST | Rapida V1 — Long + BTC 1–3 + score <7,5 | 3 | €9.915,69 | €1.942,95 | €5.828,84 | €149,35 | €-19,39 |
| TEST | Combo Adaptive — 75% a 2R + runner 3R | 3 | €9.914,80 | €3.243,15 | €6.486,31 | €149,32 | €7,79 |
| TEST | Forza relativa 1H V1 | 4 | €9.907,47 | €2.404,07 | €4.808,14 | €148,58 | €-17,07 |
| TEST | Rapida V3 — score <7,5 | 1 | €9.898,20 | €712,28 | €2.136,85 | €49,73 | €0,00 |
| TEST | Rapida V1 — score 6–7,5 | 0 | €9.898,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — Quality7 | 2 | €9.897,35 | €1.968,07 | €3.936,13 | €99,06 | €1,23 |
| TEST | Rapida V3 — Long Only | 0 | €9.897,06 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — Trend/Transition | 3 | €9.896,00 | €2.075,49 | €4.150,97 | €148,31 | €-17,93 |
| TEST | Combo Scanner | 2 | €9.892,02 | €1.065,42 | €2.130,85 | €99,73 | €-14,93 |
| TEST | Eth Ema 1H | 1 | €9.885,14 | €1.144,65 | €3.433,94 | €49,45 | €-2,32 |
| TEST | Combo Adaptive — Long Only | 2 | €9.851,17 | €1.099,22 | €2.198,44 | €98,72 | €-14,79 |
| TEST | Rapida V3 — Long + no HIGH + score <7,5 | 0 | €9.850,91 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Top 5 + BTC — Guard + BTC≤3 | 3 | €9.847,30 | €1.282,24 | €2.564,48 | €148,09 | €-32,43 |
| TEST | Rapida V3 — senza ESPORTS | 1 | €9.845,03 | €712,28 | €2.136,85 | €49,73 | €0,00 |
| TEST | Combo Adaptive — Quality7 + Regime | 2 | €9.839,09 | €1.973,66 | €3.947,32 | €99,07 | €1,23 |
| TEST | Combo Adaptive — Quality7 + Regime + parziale 1R | 2 | €9.839,09 | €1.973,66 | €3.947,32 | €99,07 | €1,23 |
| TEST | Master Adaptive Expanded V1 | 3 | €9.835,70 | €2.227,72 | €4.455,45 | €147,21 | €13,27 |
| TEST | Top 5 + BTC — Guard + BTC≤3 + MFE | 3 | €9.819,98 | €1.301,48 | €2.602,97 | €148,06 | €-50,97 |
| TEST | Rapida V3 — no volatilità HIGH | 1 | €9.818,47 | €707,41 | €2.122,22 | €49,39 | €0,00 |
| TEST | Combo Adaptive — parziale 1R | 3 | €9.796,59 | €2.141,01 | €4.282,03 | €147,68 | €-12,80 |
| TEST | Rapida 1H V1 — madre | 4 | €9.785,33 | €3.061,12 | €9.183,36 | €195,14 | €3,29 |
| TEST | Master Adaptive V1 | 3 | €9.778,79 | €2.731,68 | €5.463,37 | €146,91 | €-0,92 |
| TEST | Master Adaptive No Alt V1 | 3 | €9.778,79 | €2.731,68 | €5.463,37 | €146,91 | €-0,92 |
| TEST | Master Adaptive Runner25 V1 | 3 | €9.778,79 | €2.731,68 | €5.463,37 | €146,91 | €-0,92 |
| TEST | Master Adaptive Strict3 V1 | 3 | €9.778,56 | €2.827,91 | €5.655,82 | €147,95 | €-0,09 |
| TEST | Rapida V3 — qualità completa + profit lock | 0 | €9.749,89 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Global Confluence puro 1H | 1 | €9.746,10 | €1.527,19 | €3.054,37 | €48,87 | €-26,35 |
| TEST | Scanner Bottom 5 Short 1H | 2 | €9.711,95 | €1.299,20 | €2.598,41 | €48,57 | €-0,44 |
| TEST | Top 5 + BTC — Guard + MFE | 3 | €9.708,49 | €1.182,17 | €2.364,33 | €146,66 | €-50,39 |
| TEST | Top 5 + BTC — Guard | 3 | €9.686,21 | €1.161,08 | €2.322,16 | €146,20 | €-31,90 |
| TEST | Combo Adaptive — MFE Trail esistente | 3 | €9.662,52 | €1.149,02 | €2.298,05 | €96,76 | €-18,72 |
| TEST | Master Adaptive Gb20 V1 | 3 | €9.655,49 | €1.258,76 | €2.517,53 | €146,00 | €-36,73 |

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
| PRINCIPALE | Principale 4H | Confluenza trend | €9.908,51 | €-152,45 | 17 | 17 | 29,41% | 0,73 | €-8,97 | 4,26% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.478,02 | €513,90 | 28 | 28 | 50,00% | 1,96 | €18,35 | 2,70% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €10.422,66 | €416,52 | 20 | 20 | 50,00% | 2,23 | €20,83 | 1,74% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €10.273,87 | €279,12 | 29 | 29 | 44,83% | 1,37 | €9,62 | 2,20% |
| TEST | Combo Adaptive — madre | Combo Adaptive | €10.212,93 | €239,35 | 20 | 20 | 45,00% | 1,71 | €11,97 | 1,31% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €10.197,77 | €209,55 | 31 | 31 | 48,39% | 1,34 | €6,76 | 1,81% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €10.135,15 | €157,56 | 17 | 17 | 47,06% | 1,40 | €9,27 | 2,05% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €10.117,57 | €116,68 | 20 | 20 | 45,00% | 1,34 | €5,83 | 2,06% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.099,96 | €99,96 | 2 | 2 | 100,00% | ∞ | €49,98 | 0,31% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €10.085,92 | €85,92 | 9 | 9 | 44,44% | 1,40 | €9,55 | 1,12% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €10.083,17 | €116,37 | 23 | 22 | 34,78% | 1,18 | €5,06 | 3,21% |
| TEST | Ampia 4H | Confluenza trend | €10.071,99 | €88,72 | 12 | 12 | 25,00% | 1,27 | €7,39 | 2,37% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €10.028,40 | €28,40 | 6 | 6 | 33,33% | 1,98 | €4,73 | 0,25% |
| TEST | Btc Ema 4H | Trend following EMA | €10.025,19 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,40% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €10.025,19 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,40% |
| TEST | Sol Ema 1H | Trend following EMA | €10.017,92 | €-9,16 | 2 | 2 | 50,00% | 0,83 | €-4,58 | 1,10% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.016,05 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,27% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €10.015,45 | €15,45 | 1 | 1 | 100,00% | ∞ | €15,45 | 0,51% |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | €10.014,00 | €14,00 | 2 | 2 | 100,00% | ∞ | €7,00 | 0,04% |
| TEST | Top 5 + BTC — BTC≤3 | Scanner Top 5 + forza BTC | €10.009,24 | €4,45 | 2 | 2 | 50,00% | 1,08 | €2,23 | 1,99% |
| TEST | Top 5 + BTC — BTC 2–3 | Scanner Top 5 + forza BTC | €10.009,24 | €4,45 | 2 | 2 | 50,00% | 1,08 | €2,23 | 1,99% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €10.008,60 | €-18,45 | 2 | 2 | 50,00% | 0,67 | €-9,23 | 1,12% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €10.005,68 | €5,68 | 6 | 6 | 33,33% | 1,98 | €0,95 | 0,05% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €10.005,24 | €5,24 | 2 | 2 | 50,00% | 10,75 | €2,62 | 0,09% |
| TEST | Scalp RSI Long 25 · €10 · 15x | Inversione RSI estrema 15m | €10.002,80 | €2,80 | 2 | 2 | 100,00% | ∞ | €1,40 | 0,01% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €10.002,45 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,40% |
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
| TEST | Eth Ema 4H | Trend following EMA | €9.999,11 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,32% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €9.998,48 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,37% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €9.997,37 | €-2,63 | 2 | 2 | 50,00% | 0,41 | €-1,31 | 0,55% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €9.995,38 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,32% |
| TEST | Sol Ema 4H | Trend following EMA | €9.994,96 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,35% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €9.994,96 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,35% |
| TEST | Rapida 1H V3 Filtered — madre | Momentum / breakout V3 Filtered | €9.989,20 | €-7,38 | 47 | 47 | 34,04% | 0,99 | €-0,16 | 2,89% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €9.988,26 | €-11,74 | 2 | 2 | 50,00% | 0,78 | €-5,87 | 0,89% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €9.985,10 | €4,32 | 20 | 18 | 50,00% | 1,01 | €0,22 | 2,75% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.982,54 | €-17,46 | 3 | 3 | 33,33% | 0,84 | €-5,82 | 1,38% |
| TEST | Rapida V1 — senza PEPE | Momentum / breakout | €9.978,82 | €-98,53 | 16 | 16 | 25,00% | 0,74 | €-6,16 | 2,10% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €9.968,98 | €-31,02 | 2 | 2 | 50,00% | 0,46 | €-15,51 | 0,93% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.964,86 | €-35,14 | 6 | 6 | 16,67% | 0,18 | €-5,86 | 0,36% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.953,86 | €-37,64 | 3 | 3 | 66,67% | 0,31 | €-12,55 | 1,02% |
| TEST | Top 5 + BTC — 75% a 2,2R + runner 3R | Scanner Top 5 + forza BTC | €9.948,74 | €-16,90 | 6 | 6 | 50,00% | 0,90 | €-2,82 | 2,33% |
| TEST | Top 5 + BTC — target pieno 3R | Scanner Top 5 + forza BTC | €9.948,74 | €-16,90 | 6 | 6 | 50,00% | 0,90 | €-2,82 | 2,33% |
| TEST | Doge Ema 1H | Trend following EMA | €9.948,28 | €-51,72 | 4 | 4 | 50,00% | 0,54 | €-12,93 | 1,27% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €9.944,87 | €-55,13 | 5 | 4 | 20,00% | 0,56 | €-11,03 | 1,30% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.944,21 | €-55,79 | 1 | 1 | 0,00% | 0,00 | €-55,79 | 0,62% |
| TEST | Combo Adaptive — target pieno 3R | Combo Adaptive | €9.940,10 | €-35,63 | 8 | 8 | 50,00% | 0,83 | €-4,45 | 1,41% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €9.937,58 | €-62,42 | 3 | 3 | 33,33% | 0,43 | €-20,81 | 1,49% |
| TEST | Btc Ema 1H | Trend following EMA | €9.934,39 | €-65,61 | 4 | 4 | 25,00% | 0,60 | €-16,40 | 1,56% |
| TEST | Rapida V1 — target pieno 2R | Momentum / breakout | €9.933,14 | €-136,72 | 15 | 15 | 26,67% | 0,68 | €-9,11 | 2,45% |
| TEST | Top 5 + BTC — solo MFE | Scanner Top 5 + forza BTC | €9.928,50 | €-35,06 | 5 | 5 | 20,00% | 0,52 | €-7,01 | 1,61% |
| TEST | Combo Trend | Combo Trend | €9.925,48 | €-49,58 | 17 | 17 | 29,41% | 0,90 | €-2,92 | 3,02% |
| TEST | Rapida V1 — no HIGH + score <7,5 | Momentum / breakout | €9.924,96 | €-133,04 | 21 | 21 | 33,33% | 0,78 | €-6,34 | 2,83% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.917,75 | €-52,14 | 15 | 15 | 33,33% | 0,88 | €-3,48 | 2,25% |
| TEST | Rapida V1 — Long + BTC 1–3 + score <7,5 | Momentum / breakout | €9.915,69 | €-61,41 | 3 | 3 | 0,00% | 0,00 | €-20,47 | 1,28% |
| TEST | Combo Adaptive — 75% a 2R + runner 3R | Combo Adaptive | €9.914,80 | €-89,34 | 8 | 8 | 37,50% | 0,67 | €-11,17 | 1,56% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €9.907,47 | €-72,58 | 22 | 22 | 27,27% | 0,83 | €-3,30 | 3,25% |
| TEST | Rapida V3 — score <7,5 | Momentum / breakout V3 Filtered | €9.898,20 | €-100,92 | 18 | 18 | 27,78% | 0,77 | €-5,61 | 2,49% |
| TEST | Rapida V1 — score 6–7,5 | Momentum / breakout | €9.898,20 | €-101,80 | 19 | 19 | 26,32% | 0,77 | €-5,36 | 2,49% |
| TEST | Combo Adaptive — Quality7 | Combo Adaptive | €9.897,35 | €-101,74 | 3 | 3 | 33,33% | 0,05 | €-33,91 | 1,51% |
| TEST | Rapida V3 — Long Only | Momentum / breakout V3 Filtered | €9.897,06 | €-102,94 | 10 | 10 | 20,00% | 0,57 | €-10,29 | 2,11% |
| TEST | Combo Adaptive — Trend/Transition | Combo Adaptive | €9.896,00 | €-83,93 | 8 | 8 | 37,50% | 0,70 | €-10,49 | 2,18% |
| TEST | Combo Scanner | Combo Scanner | €9.892,02 | €-91,73 | 21 | 21 | 38,10% | 0,85 | €-4,37 | 2,61% |
| TEST | Eth Ema 1H | Trend following EMA | €9.885,14 | €-110,26 | 5 | 5 | 40,00% | 0,33 | €-22,05 | 1,59% |
| TEST | Combo Adaptive — Long Only | Combo Adaptive | €9.851,17 | €-132,59 | 5 | 5 | 20,00% | 0,42 | €-26,52 | 2,34% |
| TEST | Rapida V3 — Long + no HIGH + score <7,5 | Momentum / breakout V3 Filtered | €9.850,91 | €-149,09 | 9 | 9 | 22,22% | 0,48 | €-16,57 | 2,00% |
| TEST | Top 5 + BTC — Guard + BTC≤3 | Scanner Top 5 + forza BTC | €9.847,30 | €-118,58 | 2 | 2 | 0,00% | 0,00 | €-59,29 | 1,64% |
| TEST | Rapida V3 — senza ESPORTS | Momentum / breakout V3 Filtered | €9.845,03 | €-154,08 | 19 | 19 | 26,32% | 0,69 | €-8,11 | 2,49% |
| TEST | Combo Adaptive — Quality7 + Regime | Combo Adaptive | €9.839,09 | €-160,00 | 3 | 3 | 0,00% | 0,00 | €-53,33 | 1,95% |
| TEST | Combo Adaptive — Quality7 + Regime + parziale 1R | Combo Adaptive | €9.839,09 | €-160,00 | 3 | 3 | 0,00% | 0,00 | €-53,33 | 1,95% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €9.835,70 | €-174,68 | 6 | 6 | 16,67% | 0,34 | €-29,11 | 2,79% |
| TEST | Top 5 + BTC — Guard + BTC≤3 + MFE | Scanner Top 5 + forza BTC | €9.819,98 | €-127,46 | 3 | 3 | 0,00% | 0,00 | €-42,49 | 1,90% |
| TEST | Rapida V3 — no volatilità HIGH | Momentum / breakout V3 Filtered | €9.818,47 | €-180,65 | 20 | 20 | 30,00% | 0,70 | €-9,03 | 2,96% |
| TEST | Combo Adaptive — parziale 1R | Combo Adaptive | €9.796,59 | €-187,92 | 10 | 10 | 30,00% | 0,51 | €-18,79 | 2,24% |
| TEST | Rapida 1H V1 — madre | Momentum / breakout | €9.785,33 | €-212,84 | 54 | 54 | 31,48% | 0,84 | €-3,94 | 6,46% |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | €9.778,79 | €-216,46 | 4 | 4 | 0,00% | 0,00 | €-54,11 | 2,77% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €9.778,79 | €-216,46 | 4 | 4 | 0,00% | 0,00 | €-54,11 | 2,77% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €9.778,79 | €-216,46 | 4 | 4 | 0,00% | 0,00 | €-54,11 | 2,77% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €9.778,56 | €-217,20 | 4 | 4 | 0,00% | 0,00 | €-54,30 | 2,60% |
| TEST | Rapida V3 — qualità completa + profit lock | Momentum / breakout V3 Filtered | €9.749,89 | €-250,11 | 9 | 9 | 33,33% | 0,25 | €-27,79 | 2,84% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.746,10 | €-226,02 | 7 | 7 | 28,57% | 0,17 | €-32,29 | 2,92% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.711,95 | €-286,05 | 19 | 19 | 26,32% | 0,46 | €-15,06 | 4,81% |
| TEST | Top 5 + BTC — Guard + MFE | Scanner Top 5 + forza BTC | €9.708,49 | €-239,81 | 6 | 6 | 0,00% | 0,00 | €-39,97 | 3,08% |
| TEST | Top 5 + BTC — Guard | Scanner Top 5 + forza BTC | €9.686,21 | €-280,49 | 5 | 5 | 0,00% | 0,00 | €-56,10 | 3,31% |
| TEST | Combo Adaptive — MFE Trail esistente | Combo Adaptive | €9.662,52 | €-317,53 | 27 | 27 | 25,93% | 0,45 | €-11,76 | 4,11% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €9.655,49 | €-306,25 | 10 | 10 | 20,00% | 0,10 | €-30,62 | 3,84% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | DOGE | SHORT | Confluenza trend | 240m | 3,0x | 0,07292 | 0,07300 | 0,07500 | 0,09686 | 0,06875 | €574,44 | €1.723,33 | €49,28 | €-2,00 |
| Principale 4H | LAB | SHORT | Confluenza trend | 240m | 3,0x | 0,17841 | 0,15125 | 0,17841 | 0,23699 | 0,13559 | €136,26 | €408,77 | €0,00 | €62,23 |
| Principale 4H | SUI | LONG | Confluenza trend | 240m | 3,0x | 0,76296 | 0,76296 | 0,73998 | 0,51245 | 0,80891 | €547,52 | €1.642,56 | €49,46 | €0,00 |
| Principale 4H | ONDO | LONG | Confluenza trend | 240m | 3,0x | 0,40344 | 0,40344 | 0,37762 | 0,27098 | 0,45509 | €254,70 | €764,09 | €48,91 | €0,00 |
| Bilanciata 1H V1 | ONDO | LONG | Confluenza trend | 60m | 3,0x | 0,39694 | 0,39694 | 0,38539 | 0,26661 | 0,42004 | €581,76 | €1.745,29 | €50,78 | €0,00 |
| Bilanciata 1H V1 | ZEC | SHORT | Confluenza trend | 60m | 3,0x | 514,40710 | 515,20000 | 526,37866 | 683,30410 | 490,46397 | €731,22 | €2.193,66 | €51,05 | €-3,38 |
| Bilanciata 1H V1 | ETH | LONG | Confluenza trend | 60m | 3,0x | 1937,36740 | 1934,24000 | 1909,46931 | 1301,26510 | 1993,16358 | €1.184,41 | €3.553,24 | €51,17 | €-5,74 |
| Bilanciata 1H V1 | ADA | LONG | Confluenza trend | 60m | 3,0x | 0,17542 | 0,17562 | 0,17150 | 0,11782 | 0,18325 | €760,90 | €2.282,69 | €50,95 | €2,67 |
| Bilanciata 1H V2 | ESPORTS | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,02164 | 0,02164 | 0,02164 | 0,02874 | 0,01644 | €138,69 | €416,06 | €0,00 | €-0,00 |
| Bilanciata 1H V2 | AKE | LONG | Confluenza trend V2 | 60m | 3,0x | 0,00180 | 0,00178 | 0,00159 | 0,00121 | 0,00222 | €143,70 | €431,11 | €50,27 | €-4,80 |
| Bilanciata 1H V2 | ZEC | SHORT | Confluenza trend V2 | 60m | 3,0x | 512,43749 | 515,20000 | 523,41700 | 680,68780 | 490,47847 | €780,12 | €2.340,36 | €50,14 | €-12,62 |
| Bilanciata 1H V3 Filtered | ESPORTS | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,02126 | 0,02126 | 0,02126 | 0,02823 | 0,01615 | €141,51 | €424,52 | €0,00 | €-0,00 |
| Bilanciata 1H V3 Filtered | ONDO | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,40134 | 0,40134 | 0,38898 | 0,26957 | 0,42605 | €557,59 | €1.672,77 | €51,50 | €0,00 |
| Bilanciata 1H V3 Filtered | ZEC | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 514,40710 | 515,20000 | 526,37866 | 683,30410 | 490,46397 | €738,63 | €2.215,89 | €51,57 | €-3,42 |
| Rapida 1H V1 — madre | ESPORTS | SHORT | Momentum / breakout | 60m | 3,0x | 0,01984 | 0,01984 | 0,02222 | 0,02635 | 0,01627 | €129,65 | €388,96 | €46,68 | €-0,00 |
| Rapida 1H V1 — madre | SUI | LONG | Momentum / breakout | 60m | 3,0x | 0,76416 | 0,76416 | 0,75422 | 0,51326 | 0,77907 | €1.284,19 | €3.852,58 | €50,12 | €0,00 |
| Rapida 1H V1 — madre | ONDO | LONG | Momentum / breakout | 60m | 3,0x | 0,39924 | 0,39924 | 0,38995 | 0,26816 | 0,41318 | €708,01 | €2.124,02 | €49,43 | €0,00 |
| Rapida 1H V1 — madre | ADA | LONG | Momentum / breakout | 60m | 3,0x | 0,17542 | 0,17562 | 0,17237 | 0,11782 | 0,17998 | €939,27 | €2.817,80 | €48,92 | €3,29 |
| Rapida V1 — no HIGH + score <7,5 | ONDO | LONG | Momentum / breakout | 60m | 3,0x | 0,39924 | 0,39924 | 0,38995 | 0,26816 | 0,41318 | €704,39 | €2.113,17 | €49,18 | €0,00 |
| Rapida V1 — no HIGH + score <7,5 | ADA | LONG | Momentum / breakout | 60m | 3,0x | 0,17542 | 0,17562 | 0,17237 | 0,11782 | 0,17998 | €948,77 | €2.846,32 | €49,41 | €3,32 |
| Rapida V1 — no HIGH + score <7,5 | BANK | LONG | Momentum / breakout | 60m | 3,0x | 0,22386 | 0,25520 | 0,19700 | 0,15036 | 0,26416 | €136,95 | €410,84 | €49,30 | €57,51 |
| Rapida V1 — Long + BTC 1–3 + score <7,5 | ONDO | LONG | Momentum / breakout | 60m | 3,0x | 0,39694 | 0,39694 | 0,38849 | 0,26661 | 0,40961 | €783,06 | €2.349,19 | €50,00 | €0,00 |
| Rapida V1 — Long + BTC 1–3 + score <7,5 | ADA | LONG | Momentum / breakout | 60m | 3,0x | 0,17580 | 0,17562 | 0,17285 | 0,11808 | 0,18022 | €988,05 | €2.964,14 | €49,69 | €-2,96 |
| Rapida V1 — Long + BTC 1–3 + score <7,5 | LAB | LONG | Momentum / breakout | 60m | 3,0x | 0,15623 | 0,15125 | 0,14118 | 0,10494 | 0,17881 | €171,84 | €515,51 | €49,67 | €-16,44 |
| Rapida V1 — senza PEPE | ONDO | LONG | Momentum / breakout | 60m | 3,0x | 0,39924 | 0,39924 | 0,38995 | 0,26816 | 0,41318 | €713,68 | €2.141,05 | €49,83 | €0,00 |
| Rapida V1 — senza PEPE | ZEC | SHORT | Momentum / breakout | 60m | 3,0x | 515,14695 | 515,20000 | 524,33753 | 684,28687 | 501,36109 | €935,01 | €2.805,03 | €50,04 | €-0,29 |
| Rapida V1 — senza PEPE | BANK | LONG | Momentum / breakout | 60m | 3,0x | 0,21832 | 0,25520 | 0,22472 | 0,14664 | 0,25762 | €135,59 | €406,77 | €0,00 | €68,71 |
| Rapida V1 — senza PEPE | ADA | LONG | Momentum / breakout | 60m | 3,0x | 0,17481 | 0,17562 | 0,17178 | 0,11742 | 0,17937 | €954,58 | €2.863,74 | €49,72 | €13,19 |
| Rapida V1 — target pieno 2R | ONDO | LONG | Momentum / breakout | 60m | 3,0x | 0,39924 | 0,39924 | 0,38995 | 0,26816 | 0,41782 | €712,92 | €2.138,77 | €49,77 | €0,00 |
| Rapida V1 — target pieno 2R | ADA | LONG | Momentum / breakout | 60m | 3,0x | 0,17542 | 0,17562 | 0,17237 | 0,11782 | 0,18151 | €946,82 | €2.840,45 | €49,31 | €3,32 |
| Rapida V1 — target pieno 2R | BANK | LONG | Momentum / breakout | 60m | 3,0x | 0,21832 | 0,25520 | 0,22472 | 0,14664 | 0,27072 | €136,93 | €410,79 | €0,00 | €69,39 |
| Rapida 1H V3 Filtered — madre | ESPORTS | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01977 | 0,01977 | 0,02214 | 0,02626 | 0,01621 | €137,70 | €413,09 | €49,57 | €-0,00 |
| Rapida 1H V3 Filtered — madre | SUI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,76416 | 0,76416 | 0,75422 | 0,51326 | 0,77907 | €1.267,97 | €3.803,92 | €49,49 | €0,00 |
| Rapida 1H V3 Filtered — madre | ONDO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,39924 | 0,39924 | 0,38995 | 0,26816 | 0,41318 | €715,14 | €2.145,42 | €49,93 | €0,00 |
| Rapida V3 — score <7,5 | ONDO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,39924 | 0,39924 | 0,38995 | 0,26816 | 0,41318 | €712,28 | €2.136,85 | €49,73 | €0,00 |
| Rapida V3 — no volatilità HIGH | ONDO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,39924 | 0,39924 | 0,38995 | 0,26816 | 0,41318 | €707,41 | €2.122,22 | €49,39 | €0,00 |
| Rapida V3 — senza ESPORTS | ONDO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,39924 | 0,39924 | 0,38995 | 0,26816 | 0,41318 | €712,28 | €2.136,85 | €49,73 | €0,00 |
| Ampia 4H | DOGE | SHORT | Confluenza trend | 240m | 2,0x | 0,07237 | 0,07300 | 0,07515 | 0,10819 | 0,06457 | €649,49 | €1.298,97 | €50,00 | €-11,37 |
| Ampia 4H | ZEC | LONG | Confluenza trend | 240m | 2,0x | 522,36445 | 515,20000 | 483,09844 | 263,79405 | 632,30930 | €332,53 | €665,06 | €49,99 | €-9,12 |
| Ampia 4H | PEPE | LONG | Confluenza trend | 240m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €497,18 | €994,35 | €50,70 | €5,20 |
| Ampia 4H | ETH | LONG | Confluenza trend | 240m | 2,0x | 1933,63665 | 1934,24000 | 1869,00475 | 976,48651 | 2114,60597 | €756,64 | €1.513,28 | €50,58 | €0,47 |
| Forza relativa 1H V1 | ESPORTS | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,02126 | 0,02126 | 0,02126 | 0,03178 | 0,01564 | €208,05 | €416,10 | €0,00 | €-0,00 |
| Forza relativa 1H V1 | NIGHT | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,02031 | 0,02031 | 0,02210 | 0,03036 | 0,01637 | €285,91 | €571,83 | €50,45 | €-0,00 |
| Forza relativa 1H V1 | ONDO | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,42171 | €891,90 | €1.783,80 | €49,29 | €0,00 |
| Forza relativa 1H V1 | ZEC | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 510,91780 | 515,20000 | 523,17072 | 763,82211 | 483,96137 | €1.018,21 | €2.036,41 | €48,84 | €-17,07 |
| Forza relativa 1H V2 | ESPORTS | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,02126 | 0,02126 | 0,02126 | 0,03178 | 0,01564 | €215,33 | €430,67 | €0,00 | €-0,00 |
| Forza relativa 1H V2 | ZEC | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 512,43749 | 515,20000 | 523,41700 | 766,09405 | 488,28257 | €1.188,35 | €2.376,70 | €50,92 | €-12,81 |
| Forza relativa 1H V2 | AKE | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,00186 | 0,00178 | 0,00164 | 0,00094 | 0,00234 | €214,82 | €429,64 | €50,07 | €-18,34 |
| Forza relativa 1H V2 | BANK | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,25525 | 0,25520 | 0,22462 | 0,12890 | 0,32264 | €204,16 | €408,32 | €49,00 | €-0,08 |
| Benchmark Donchian breakout 1H | SUI | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,76606 | 0,76606 | 0,75182 | 0,38686 | 0,80165 | €1.377,00 | €2.754,00 | €51,18 | €0,00 |
| Benchmark Donchian breakout 1H | HYPE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 58,85923 | 59,24700 | 60,10965 | 87,99454 | 55,73317 | €1.195,13 | €2.390,27 | €50,78 | €-15,75 |
| Benchmark Donchian breakout 1H | ZEC | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 514,40710 | 515,20000 | 527,70883 | 769,03861 | 481,15276 | €982,86 | €1.965,73 | €50,83 | €-3,03 |
| Benchmark Bollinger mean reversion 1H | ZEC | LONG | Bollinger mean reversion | 60m | 2,0x | 514,61290 | 515,20000 | 504,63261 | 259,87952 | 529,58334 | €1.299,75 | €2.599,50 | €50,41 | €2,97 |
| Benchmark trend following EMA 1H | LAB | LONG | Trend following EMA | 60m | 2,0x | 0,15689 | 0,15125 | 0,13807 | 0,07923 | 0,19831 | €207,05 | €414,10 | €49,69 | €-14,90 |
| Benchmark trend following EMA 1H | ZEC | SHORT | Trend following EMA | 60m | 2,0x | 511,44769 | 515,20000 | 525,07617 | 764,61430 | 481,46504 | €934,35 | €1.868,69 | €49,79 | €-13,71 |
| Scanner Top 5 Long 1H | ONDO | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,40114 | 0,40114 | 0,38834 | 0,20258 | 0,42673 | €828,91 | €1.657,82 | €52,88 | €0,00 |
| Scanner Top 5 Long 1H | LAB | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,15689 | 0,15125 | 0,13807 | 0,07923 | 0,19455 | €219,03 | €438,05 | €52,57 | €-15,76 |
| Scanner Top 5 Long 1H | AKE | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,00186 | 0,00178 | 0,00164 | 0,00094 | 0,00231 | €218,50 | €437,00 | €52,44 | €-18,75 |
| Scanner Bottom 5 Short 1H | ESPORTS | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,02150 | 0,02150 | 0,02150 | 0,03214 | 0,01634 | €207,40 | €414,80 | €0,00 | €-0,00 |
| Scanner Bottom 5 Short 1H | ZEC | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 515,09696 | 515,20000 | 526,55393 | 770,06996 | 492,18303 | €1.091,80 | €2.183,60 | €48,57 | €-0,44 |
| Scanner Top 5 + forza BTC 1H | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 77,70854 | 78,30000 | 76,45304 | 39,24281 | 80,47063 | €1.614,82 | €3.229,64 | €52,18 | €24,58 |
| Scanner Top 5 + forza BTC 1H | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39694 | 0,39694 | 0,38539 | 0,20045 | 0,42235 | €898,57 | €1.797,15 | €52,29 | €0,00 |
| Scanner Top 5 + forza BTC 1H | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15125 | 0,13807 | 0,07923 | 0,19831 | €216,56 | €433,12 | €51,97 | €-15,58 |
| Top 5 + BTC — solo MFE | SUI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,76776 | 0,76776 | 0,75508 | 0,38772 | 0,79565 | €1.514,04 | €3.028,08 | €50,00 | €0,00 |
| Top 5 + BTC — solo MFE | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39924 | 0,39924 | 0,38729 | 0,20162 | 0,42552 | €835,46 | €1.670,91 | €50,00 | €0,00 |
| Top 5 + BTC — solo MFE | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,16335 | 0,15125 | 0,14544 | 0,08249 | 0,20276 | €227,11 | €454,22 | €49,81 | €-33,65 |
| Top 5 + BTC — Guard | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39724 | 0,39724 | 0,38434 | 0,20061 | 0,42561 | €756,62 | €1.513,24 | €49,13 | €0,00 |
| Top 5 + BTC — Guard | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15125 | 0,13807 | 0,07923 | 0,19831 | €202,47 | €404,95 | €48,59 | €-14,57 |
| Top 5 + BTC — Guard | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00186 | 0,00178 | 0,00164 | 0,00094 | 0,00235 | €201,99 | €403,97 | €48,48 | €-17,33 |
| Top 5 + BTC — BTC≤3 | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 77,78955 | 78,30000 | 76,66939 | 39,28373 | 80,25393 | €1.735,32 | €3.470,64 | €49,98 | €22,77 |
| Top 5 + BTC — BTC≤3 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39974 | 0,39974 | 0,38840 | 0,20187 | 0,42468 | €884,65 | €1.769,29 | €50,18 | €0,00 |
| Top 5 + BTC — BTC≤3 | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15125 | 0,13807 | 0,07923 | 0,19831 | €207,87 | €415,74 | €49,89 | €-14,96 |
| Top 5 + BTC — BTC 2–3 | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 77,78955 | 78,30000 | 76,66939 | 39,28373 | 80,25393 | €1.735,32 | €3.470,64 | €49,98 | €22,77 |
| Top 5 + BTC — BTC 2–3 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39974 | 0,39974 | 0,38840 | 0,20187 | 0,42468 | €884,65 | €1.769,29 | €50,18 | €0,00 |
| Top 5 + BTC — BTC 2–3 | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15125 | 0,13807 | 0,07923 | 0,19831 | €207,87 | €415,74 | €49,89 | €-14,96 |
| Top 5 + BTC — Guard + MFE | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39724 | 0,39724 | 0,38434 | 0,20061 | 0,42561 | €756,62 | €1.513,24 | €49,13 | €0,00 |
| Top 5 + BTC — Guard + MFE | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00186 | 0,00178 | 0,00164 | 0,00094 | 0,00235 | €203,02 | €406,03 | €48,72 | €-17,42 |
| Top 5 + BTC — Guard + MFE | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,16335 | 0,15125 | 0,14544 | 0,08249 | 0,20276 | €222,53 | €445,06 | €48,81 | €-32,97 |
| Top 5 + BTC — Guard + BTC≤3 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39974 | 0,39974 | 0,38840 | 0,20187 | 0,42468 | €871,05 | €1.742,11 | €49,41 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15125 | 0,13807 | 0,07923 | 0,19831 | €205,84 | €411,68 | €49,40 | €-14,81 |
| Top 5 + BTC — Guard + BTC≤3 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00186 | 0,00178 | 0,00164 | 0,00094 | 0,00235 | €205,35 | €410,69 | €49,28 | €-17,62 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39974 | 0,39974 | 0,38840 | 0,20187 | 0,42468 | €871,05 | €1.742,11 | €49,41 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00186 | 0,00178 | 0,00164 | 0,00094 | 0,00235 | €205,35 | €410,69 | €49,28 | €-17,62 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,16335 | 0,15125 | 0,14544 | 0,08249 | 0,20276 | €225,09 | €450,17 | €49,37 | €-33,35 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39694 | 0,39694 | 0,38539 | 0,20045 | 0,43159 | €861,83 | €1.723,66 | €50,15 | €0,00 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15125 | 0,13807 | 0,07923 | 0,21338 | €207,96 | €415,92 | €49,91 | €-14,96 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00186 | 0,00178 | 0,00164 | 0,00094 | 0,00253 | €207,46 | €414,92 | €49,79 | €-17,80 |
| Top 5 + BTC — target pieno 3R | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39694 | 0,39694 | 0,38539 | 0,20045 | 0,43159 | €861,83 | €1.723,66 | €50,15 | €0,00 |
| Top 5 + BTC — target pieno 3R | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15125 | 0,13807 | 0,07923 | 0,21338 | €207,96 | €415,92 | €49,91 | €-14,96 |
| Top 5 + BTC — target pieno 3R | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00186 | 0,00178 | 0,00164 | 0,00094 | 0,00253 | €207,46 | €414,92 | €49,79 | €-17,80 |
| Global Confluence puro 1H | DOGE | SHORT | Global Confluence puro | 60m | 2,0x | 0,07238 | 0,07300 | 0,07353 | 0,10820 | 0,06948 | €1.527,19 | €3.054,37 | €48,87 | €-26,35 |
| Combo Trend | ONDO | LONG | Combo Trend | 60m | 2,0x | 0,37282 | 0,37282 | 0,39131 | 0,18828 | 0,41057 | €545,86 | €1.091,71 | €0,00 | €0,00 |
| Combo Trend | ESPORTS | SHORT | Combo Trend | 60m | 2,0x | 0,01883 | 0,01883 | 0,02109 | 0,02815 | 0,01386 | €209,57 | €419,14 | €50,30 | €-0,00 |
| Combo Trend | ZEC | SHORT | Combo Trend | 60m | 2,0x | 508,99818 | 515,20000 | 522,42162 | 760,95228 | 479,46661 | €943,19 | €1.886,37 | €49,75 | €-22,98 |
| Combo Scanner | ONDO | LONG | Combo Scanner | 60m | 2,0x | 0,39694 | 0,39694 | 0,38539 | 0,20045 | 0,42235 | €857,88 | €1.715,77 | €49,92 | €0,00 |
| Combo Scanner | LAB | LONG | Combo Scanner | 60m | 2,0x | 0,15689 | 0,15125 | 0,13807 | 0,07923 | 0,19831 | €207,54 | €415,08 | €49,81 | €-14,93 |
| Combo Adaptive — madre | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,40114 | 0,40114 | 0,38834 | 0,20258 | 0,42673 | €809,25 | €1.618,50 | €51,63 | €0,00 |
| Combo Adaptive — madre | ZEC | SHORT | Combo Adaptive | 60m | 2,0x | 514,17714 | 515,20000 | 525,63928 | 768,69483 | 491,25287 | €1.147,58 | €2.295,16 | €51,16 | €-4,57 |
| Combo Adaptive — madre | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15125 | 0,13958 | 0,08010 | 0,19668 | €213,13 | €426,26 | €51,15 | €-19,78 |
| Combo Adaptive — MFE Trail esistente | ESPORTS | SHORT | Combo Adaptive | 60m | 2,0x | 0,02156 | 0,02156 | 0,02091 | 0,03223 | 0,01638 | €202,62 | €405,24 | €0,00 | €-0,00 |
| Combo Adaptive — MFE Trail esistente | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39784 | 0,39784 | 0,38492 | 0,20091 | 0,42367 | €744,71 | €1.489,41 | €48,35 | €0,00 |
| Combo Adaptive — MFE Trail esistente | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15125 | 0,13958 | 0,08010 | 0,19668 | €201,70 | €403,39 | €48,41 | €-18,72 |
| Combo Adaptive — Quality7 | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,40304 | 0,40304 | 0,39140 | 0,20354 | 0,42632 | €859,15 | €1.718,30 | €49,62 | €0,00 |
| Combo Adaptive — Quality7 | ZEC | SHORT | Combo Adaptive | 60m | 2,0x | 515,48688 | 515,20000 | 526,97821 | 770,65289 | 492,50422 | €1.108,92 | €2.217,83 | €49,44 | €1,23 |
| Combo Adaptive — Trend/Transition | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39724 | 0,39724 | 0,38434 | 0,20061 | 0,42303 | €757,94 | €1.515,88 | €49,21 | €0,00 |
| Combo Adaptive — Trend/Transition | ZEC | SHORT | Combo Adaptive | 60m | 2,0x | 515,48688 | 515,20000 | 526,97821 | 770,65289 | 492,50422 | €1.111,03 | €2.222,05 | €49,53 | €1,24 |
| Combo Adaptive — Trend/Transition | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15125 | 0,13958 | 0,08010 | 0,19668 | €206,52 | €413,04 | €49,56 | €-19,17 |
| Combo Adaptive — Quality7 + Regime | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,40554 | 0,40554 | 0,39390 | 0,20480 | 0,42882 | €864,27 | €1.728,54 | €49,61 | €0,00 |
| Combo Adaptive — Quality7 + Regime | ZEC | SHORT | Combo Adaptive | 60m | 2,0x | 515,48688 | 515,20000 | 526,97821 | 770,65289 | 492,50422 | €1.109,39 | €2.218,78 | €49,46 | €1,23 |
| Combo Adaptive — Long Only | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,41951 | €893,67 | €1.787,34 | €49,39 | €0,00 |
| Combo Adaptive — Long Only | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15689 | 0,15125 | 0,13807 | 0,07923 | 0,19455 | €205,55 | €411,10 | €49,33 | €-14,79 |
| Combo Adaptive — parziale 1R | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,41951 | €893,02 | €1.786,04 | €49,36 | €0,00 |
| Combo Adaptive — parziale 1R | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15689 | 0,15125 | 0,13807 | 0,07923 | 0,19455 | €205,22 | €410,44 | €49,25 | €-14,76 |
| Combo Adaptive — parziale 1R | ZEC | SHORT | Combo Adaptive | 60m | 2,0x | 515,68684 | 515,20000 | 527,82154 | 770,95183 | 491,41745 | €1.042,77 | €2.085,55 | €49,08 | €1,97 |
| Combo Adaptive — Quality7 + Regime + parziale 1R | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,40554 | 0,40554 | 0,39390 | 0,20480 | 0,42882 | €864,27 | €1.728,54 | €49,61 | €0,00 |
| Combo Adaptive — Quality7 + Regime + parziale 1R | ZEC | SHORT | Combo Adaptive | 60m | 2,0x | 515,48688 | 515,20000 | 526,97821 | 770,65289 | 492,50422 | €1.109,39 | €2.218,78 | €49,46 | €1,23 |
| Combo Adaptive — 75% a 2R + runner 3R | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,43050 | €902,18 | €1.804,37 | €49,86 | €0,00 |
| Combo Adaptive — 75% a 2R + runner 3R | ZEC | SHORT | Combo Adaptive | 60m | 2,0x | 514,68704 | 515,20000 | 525,11837 | 769,45713 | 483,39306 | €1.229,27 | €2.458,54 | €49,83 | €-2,45 |
| Combo Adaptive — 75% a 2R + runner 3R | ADA | LONG | Combo Adaptive | 60m | 2,0x | 0,17481 | 0,17562 | 0,17091 | 0,08828 | 0,18652 | €1.111,70 | €2.223,40 | €49,63 | €10,24 |
| Combo Adaptive — target pieno 3R | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,43050 | €902,18 | €1.804,37 | €49,86 | €0,00 |
| Combo Adaptive — target pieno 3R | ZEC | SHORT | Combo Adaptive | 60m | 2,0x | 514,68704 | 515,20000 | 525,11837 | 769,45713 | 483,39306 | €1.230,32 | €2.460,64 | €49,87 | €-2,45 |
| Combo Adaptive — target pieno 3R | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15125 | 0,13958 | 0,08010 | 0,21571 | €207,43 | €414,86 | €49,78 | €-19,25 |
| Btc Ema 4H | BTC | LONG | Trend following EMA | 240m | 2,0x | 65410,57950 | 66097,49000 | 63931,54687 | 33032,34265 | 69108,16107 | €1.105,63 | €2.211,26 | €50,00 | €23,22 |
| Btc Donchian 4H | BTC | LONG | Donchian breakout 20 barre | 240m | 2,0x | 65410,57950 | 66097,49000 | 63931,54687 | 33032,34265 | 69551,87112 | €1.105,63 | €2.211,26 | €50,00 | €23,22 |
| Btc Bollinger 4H | BTC | SHORT | Bollinger mean reversion | 240m | 2,0x | 66588,49964 | 66097,49000 | 67855,55360 | 99549,80696 | 64307,80290 | €1.313,84 | €2.627,69 | €50,00 | €19,38 |
| Btc Adaptive 4H | BTC | LONG | Combo Adaptive | 240m | 2,0x | 66171,85172 | 66097,49000 | 64592,42491 | 33416,78512 | 70120,41876 | €1.047,40 | €2.094,81 | €50,00 | €-2,35 |
| Sol Ema 1H | SOL | LONG | Trend following EMA | 60m | 3,0x | 77,56451 | 78,30000 | 76,27481 | 52,09750 | 80,14392 | €1.001,44 | €3.004,32 | €49,95 | €28,49 |
| Sol Ema 4H | SOL | LONG | Trend following EMA | 240m | 2,0x | 78,49069 | 78,30000 | 76,26213 | 39,63780 | 84,06211 | €880,51 | €1.761,01 | €50,00 | €-4,28 |
| Sol Donchian 4H | SOL | LONG | Donchian breakout 20 barre | 240m | 2,0x | 78,49069 | 78,30000 | 76,26213 | 39,63780 | 84,73068 | €880,51 | €1.761,01 | €50,00 | €-4,28 |
| Sol Bollinger 4H | SOL | SHORT | Bollinger mean reversion | 240m | 2,0x | 78,45931 | 78,30000 | 80,48446 | 117,29666 | 74,81402 | €968,56 | €1.937,11 | €50,00 | €3,93 |
| Sol Adaptive 1H | SOL | LONG | Combo Adaptive | 60m | 3,0x | 77,56451 | 78,30000 | 76,27481 | 52,09750 | 80,14392 | €1.000,51 | €3.001,52 | €49,91 | €28,46 |
| Sol Adaptive 4H | SOL | LONG | Combo Adaptive | 240m | 2,0x | 78,49069 | 78,30000 | 76,05953 | 39,63780 | 84,56860 | €807,13 | €1.614,26 | €50,00 | €-3,92 |
| Eth Ema 1H | ETH | LONG | Trend following EMA | 60m | 3,0x | 1935,54703 | 1934,24000 | 1907,67515 | 1300,04242 | 1991,29079 | €1.144,65 | €3.433,94 | €49,45 | €-2,32 |
| Eth Ema 4H | ETH | LONG | Trend following EMA | 240m | 2,0x | 1933,63665 | 1934,24000 | 1878,94813 | 976,48651 | 2070,35799 | €883,93 | €1.767,86 | €50,00 | €0,55 |
| Eth Adaptive 1H | ETH | LONG | Combo Adaptive | 60m | 3,0x | 1937,86750 | 1934,24000 | 1909,96220 | 1301,60100 | 1993,67808 | €1.153,05 | €3.459,15 | €49,81 | €-6,48 |
| Master Adaptive V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39854 | 0,39854 | 0,38677 | 0,20126 | 0,42207 | €833,00 | €1.665,99 | €49,19 | €0,00 |
| Master Adaptive V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15689 | 0,15125 | 0,13807 | 0,07923 | 0,19455 | €203,80 | €407,60 | €48,91 | €-14,66 |
| Master Adaptive V1 | XRP | LONG | Master Adaptive Consensus | 60m | 2,0x | 1,13781 | 1,14242 | 1,12142 | 0,57459 | 1,17058 | €1.694,88 | €3.389,77 | €48,81 | €13,74 |
| Master Adaptive No Alt V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39854 | 0,39854 | 0,38677 | 0,20126 | 0,42207 | €833,00 | €1.665,99 | €49,19 | €0,00 |
| Master Adaptive No Alt V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15689 | 0,15125 | 0,13807 | 0,07923 | 0,19455 | €203,80 | €407,60 | €48,91 | €-14,66 |
| Master Adaptive No Alt V1 | XRP | LONG | Master Adaptive Consensus | 60m | 2,0x | 1,13781 | 1,14242 | 1,12142 | 0,57459 | 1,17058 | €1.694,88 | €3.389,77 | €48,81 | €13,74 |
| Master Adaptive Strict3 V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 1934,24677 | 1934,24000 | 1906,39362 | 976,79462 | 1989,95308 | €1.737,12 | €3.474,23 | €50,03 | €-0,01 |
| Master Adaptive Strict3 V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,41951 | €887,07 | €1.774,14 | €49,03 | €0,00 |
| Master Adaptive Strict3 V1 | BANK | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,25525 | 0,25520 | 0,22462 | 0,12890 | 0,31651 | €203,73 | €407,45 | €48,89 | €-0,08 |
| Master Adaptive Expanded V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39854 | 0,39854 | 0,38677 | 0,20126 | 0,42207 | €833,00 | €1.665,99 | €49,19 | €0,00 |
| Master Adaptive Expanded V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15689 | 0,15125 | 0,13807 | 0,07923 | 0,19455 | €203,80 | €407,60 | €48,91 | €-14,66 |
| Master Adaptive Expanded V1 | ADA | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,17358 | 0,17562 | 0,17000 | 0,08766 | 0,18074 | €1.190,93 | €2.381,85 | €49,11 | €27,94 |
| Master Adaptive Gb20 V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,40304 | 0,40304 | 0,39140 | 0,20354 | 0,42632 | €848,64 | €1.697,27 | €49,02 | €0,00 |
| Master Adaptive Gb20 V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00186 | 0,00178 | 0,00164 | 0,00094 | 0,00229 | €208,66 | €417,31 | €48,63 | €-17,81 |
| Master Adaptive Gb20 V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15870 | 0,15125 | 0,13966 | 0,08014 | 0,19679 | €201,47 | €402,94 | €48,35 | €-18,92 |
| Master Adaptive Runner25 V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39854 | 0,39854 | 0,38677 | 0,20126 | 0,43384 | €833,00 | €1.665,99 | €49,19 | €0,00 |
| Master Adaptive Runner25 V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15689 | 0,15125 | 0,13807 | 0,07923 | 0,21338 | €203,80 | €407,60 | €48,91 | €-14,66 |
| Master Adaptive Runner25 V1 | XRP | LONG | Master Adaptive Consensus | 60m | 2,0x | 1,13781 | 1,14242 | 1,12142 | 0,57459 | 1,18696 | €1.694,88 | €3.389,77 | €48,81 | €13,74 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Scanner Bottom 5 Short 1H | ZEC | SHORT | 2026-07-23T00:38:33+00:00 | 518,59616 | €10,26 | 0,21 | STOP |
| Rapida V3 — senza ESPORTS | ZEC | SHORT | 2026-07-23T00:38:33+00:00 | 520,04532 | €-53,30 | -1,07 | STOP |
| Rapida V3 — no volatilità HIGH | ZEC | SHORT | 2026-07-23T00:38:33+00:00 | 520,04532 | €-53,16 | -1,07 | STOP |
| Rapida 1H V2 | ZEC | SHORT | 2026-07-23T00:38:33+00:00 | 520,09621 | €-53,71 | -1,07 | STOP |
| Master Adaptive Expanded V1 | AKE | LONG | 2026-07-22T23:08:34+00:00 | 0,00166 | €-50,19 | -1,02 | STOP |
| Rapida V1 — no HIGH + score <7,5 | AKE | LONG | 2026-07-22T20:53:33+00:00 | 0,00171 | €-50,72 | -1,02 | STOP |
| Benchmark trend following EMA 1H | HYPE | SHORT | 2026-07-22T19:38:33+00:00 | 59,89035 | €-52,72 | -1,06 | STOP |
| Combo Trend | HYPE | SHORT | 2026-07-22T19:38:33+00:00 | 59,89035 | €-53,43 | -1,06 | STOP |
| Forza relativa 1H V2 | ADA | LONG | 2026-07-22T19:23:35+00:00 | 0,17420 | €-54,42 | -1,08 | STOP |
| Forza relativa 1H V1 | ADA | LONG | 2026-07-22T19:23:35+00:00 | 0,17420 | €-54,01 | -1,08 | STOP |
| Combo Adaptive — 75% a 2R + runner 3R | HYPE | SHORT | 2026-07-22T19:23:35+00:00 | 59,75862 | €-53,24 | -1,07 | STOP |
| Benchmark Bollinger mean reversion 1H | ADA | SHORT | 2026-07-22T19:23:35+00:00 | 0,17485 | €70,31 | 1,40 | TARGET |

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
| MAIN | Principale 4H | 39/30 | 17/30 | 0,86 | 0,73 | -0,10R | €-8,97 | 4,26% | COERENTE − | BOCCIATA RESEARCH |
| RSI_EXTREME_LONG_15M | Scalp RSI Long 25 · prudente · 5x (riferimento tra 9 varianti) | 2/30 | 2/30 | ∞ | 10,75 | 0,97R | €2,62 | 0,09% | COERENTE + | RACCOLTA RESEARCH |
| RSI_EXTREME_SHORT_15M | Scalp RSI Short 75 · prudente · 5x (riferimento tra 9 varianti) | 7/30 | 6/30 | 0,62 | 0,18 | -0,24R | €-5,86 | 0,36% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_1H_BALANCED | Bilanciata 1H V1 | 132/30 | 31/30 | 0,94 | 1,34 | -0,04R | €6,76 | 1,81% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_BALANCED_V2 | Bilanciata 1H V2 | 20/30 | 18/30 | 1,53 | 1,01 | 0,30R | €0,22 | 2,75% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_1H_BALANCED_V3 | Bilanciata 1H V3 Filtered | 41/30 | 29/30 | 1,19 | 1,37 | 0,12R | €9,62 | 2,20% | COERENTE + | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_1H_FAST | Rapida 1H V1 — madre | 153/30 | 54/30 | 0,86 | 0,84 | -0,09R | €-3,94 | 6,46% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | Rapida V1 — Long + BTC 1–3 + score <7,5 | 3/30 | 3/30 | 0,66 | 0,00 | -0,24R | €-20,47 | 1,28% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | Rapida V1 — no HIGH + score <7,5 | 22/30 | 21/30 | 0,61 | 0,78 | -0,28R | €-6,34 | 2,83% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_NO_PEPE_V1 | Rapida V1 — senza PEPE | 23/30 | 16/30 | 0,57 | 0,74 | -0,32R | €-6,16 | 2,10% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_V1 | Rapida V1 — score 6–7,5 | 15/30 | 19/30 | 0,86 | 0,77 | -0,09R | €-5,36 | 2,49% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_TP2_V1 | Rapida V1 — target pieno 2R | 21/30 | 15/30 | 0,41 | 0,68 | -0,51R | €-9,11 | 2,45% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V2 | Rapida 1H V2 | 4/30 | 4/30 | 0,30 | 0,56 | -0,62R | €-11,03 | 1,30% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3 | Rapida 1H V3 Filtered — madre | 65/30 | 47/30 | 0,95 | 0,99 | -0,03R | €-0,16 | 2,89% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_CAP75_V1 | Rapida V3 — score <7,5 | 21/30 | 18/30 | 0,66 | 0,77 | -0,24R | €-5,61 | 2,49% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | Rapida V3 — qualità completa + profit lock | 9/30 | 9/30 | 0,36 | 0,25 | -0,54R | €-27,79 | 2,84% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | Rapida V3 — Long + no HIGH + score <7,5 | 9/30 | 9/30 | 0,36 | 0,48 | -0,54R | €-16,57 | 2,00% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | Rapida V3 — Long Only | 10/30 | 10/30 | 0,31 | 0,57 | -0,60R | €-10,29 | 2,11% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | Rapida V3 — no volatilità HIGH | 23/30 | 20/30 | 0,57 | 0,70 | -0,32R | €-9,03 | 2,96% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | Rapida V3 — senza ESPORTS | 23/30 | 19/30 | 0,57 | 0,69 | -0,32R | €-8,11 | 2,49% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_4H_WIDE | Ampia 4H | 38/30 | 12/30 | 0,85 | 1,27 | -0,12R | €7,39 | 2,37% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_BOLLINGER_MR_1H | Benchmark Bollinger mean reversion 1H | 29/30 | 20/30 | 1,07 | 1,34 | 0,04R | €5,83 | 2,06% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_BTC_ADAPTIVE_1H | Btc Adaptive 1H | 1/30 | 2/30 | 0,00 | 0,78 | -1,11R | €-5,87 | 0,89% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_ADAPTIVE_4H | Btc Adaptive 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,37% | n/a | RACCOLTA RESEARCH |
| SHADOW_BTC_BOLLINGER_1H | Btc Bollinger 1H | 2/30 | 2/30 | ∞ | ∞ | 1,37R | €49,98 | 0,31% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_BTC_BOLLINGER_4H | Btc Bollinger 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,27% | n/a | RACCOLTA RESEARCH |
| SHADOW_BTC_DONCHIAN_1H | Btc Donchian 1H | 2/30 | 3/30 | 0,00 | 0,43 | -1,12R | €-20,81 | 1,49% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_DONCHIAN_4H | Btc Donchian 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,40% | n/a | RACCOLTA RESEARCH |
| SHADOW_BTC_EMA_1H | Btc Ema 1H | 4/30 | 4/30 | 0,57 | 0,60 | -0,36R | €-16,40 | 1,56% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_EMA_4H | Btc Ema 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,40% | n/a | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE | Combo Adaptive — madre | 73/30 | 20/30 | 1,29 | 1,71 | 0,18R | €11,97 | 1,31% | COERENTE + | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | Combo Adaptive — Long Only | 11/30 | 5/30 | 0,67 | 0,42 | -0,26R | €-26,52 | 2,34% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | Combo Adaptive — MFE Trail esistente | 41/30 | 27/30 | 1,18 | 0,45 | 0,12R | €-11,76 | 4,11% | DIVERGENTE | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | Combo Adaptive — parziale 1R | 19/30 | 10/30 | 0,64 | 0,51 | -0,29R | €-18,79 | 2,24% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | Combo Adaptive — Quality7 + Regime + parziale 1R | 3/30 | 3/30 | 0,00 | 0,00 | -1,07R | €-53,33 | 1,95% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | Combo Adaptive — Quality7 + Regime | 3/30 | 3/30 | 0,00 | 0,00 | -1,07R | €-53,33 | 1,95% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | Combo Adaptive — Quality7 | 3/30 | 3/30 | 0,00 | 0,05 | -1,07R | €-33,91 | 1,51% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | Combo Adaptive — Trend/Transition | 16/30 | 8/30 | 0,42 | 0,70 | -0,50R | €-10,49 | 2,18% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | Combo Adaptive — 75% a 2R + runner 3R | 13/30 | 8/30 | 0,50 | 0,67 | -0,45R | €-11,17 | 1,56% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | Combo Adaptive — target pieno 3R | 13/30 | 8/30 | 0,50 | 0,83 | -0,45R | €-4,45 | 1,41% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_MEAN_REVERSION | Combo Mean Reversion | 10/30 | 9/30 | 1,43 | 1,40 | 0,23R | €9,55 | 1,12% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_COMBO_SCANNER | Combo Scanner | 44/30 | 21/30 | 1,64 | 0,85 | 0,37R | €-4,37 | 2,61% | DIVERGENTE | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_COMBO_TREND | Combo Trend | 57/30 | 17/30 | 1,11 | 0,90 | 0,08R | €-2,92 | 3,02% | DIVERGENTE | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_DOGE_BOLLINGER_1H | Doge Bollinger 1H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_DOGE_DONCHIAN_1H | Doge Donchian 1H | 1/30 | 2/30 | 0,00 | 0,46 | -1,12R | €-15,51 | 0,93% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_DOGE_EMA_1H | Doge Ema 1H | 1/30 | 4/30 | 0,00 | 0,54 | -1,11R | €-12,93 | 1,27% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_DONCHIAN_1H | Benchmark Donchian breakout 1H | 33/30 | 17/30 | 0,99 | 1,40 | -0,01R | €9,27 | 2,05% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_EMA_TREND_1H | Benchmark trend following EMA 1H | 64/30 | 15/30 | 1,05 | 0,88 | 0,03R | €-3,48 | 2,25% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_ETH_ADAPTIVE_1H | Eth Adaptive 1H | 2/30 | 3/30 | 1,70 | 0,31 | 0,39R | €-12,55 | 1,02% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_ETH_BOLLINGER_1H | Eth Bollinger 1H | 1/30 | 1/30 | 0,00 | ∞ | -1,13R | €15,45 | 0,51% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_ETH_DONCHIAN_1H | Eth Donchian 1H | 3/30 | 3/30 | 0,84 | 0,84 | -0,12R | €-5,82 | 1,38% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_EMA_1H | Eth Ema 1H | 2/30 | 5/30 | 1,70 | 0,33 | 0,39R | €-22,05 | 1,59% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_ETH_EMA_4H | Eth Ema 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,32% | n/a | RACCOLTA RESEARCH |
| SHADOW_GLOBAL_PURE | Global Confluence puro 1H | 1/30 | 7/30 | 0,00 | 0,17 | -1,10R | €-32,29 | 2,92% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | Master Adaptive Expanded V1 | 7/30 | 6/30 | 0,29 | 0,34 | -0,65R | €-29,11 | 2,79% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | Master Adaptive Gb20 V1 | 6/30 | 10/30 | 0,00 | 0,10 | -1,08R | €-30,62 | 3,84% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | Master Adaptive No Alt V1 | 6/30 | 4/30 | 0,00 | 0,00 | -1,08R | €-54,11 | 2,77% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | Master Adaptive Runner25 V1 | 6/30 | 4/30 | 0,00 | 0,00 | -1,08R | €-54,11 | 2,77% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | Master Adaptive Strict3 V1 | 6/30 | 4/30 | 0,00 | 0,00 | -1,07R | €-54,30 | 2,60% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_V1 | Master Adaptive V1 | 6/30 | 4/30 | 0,00 | 0,00 | -1,08R | €-54,11 | 2,77% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_RELATIVE_STRENGTH | Forza relativa 1H V1 | 93/30 | 22/30 | 0,95 | 0,83 | -0,03R | €-3,30 | 3,25% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_RELATIVE_STRENGTH_V2 | Forza relativa 1H V2 | 27/30 | 22/30 | 1,39 | 1,18 | 0,25R | €5,06 | 3,21% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT | Scanner Bottom 5 Short 1H | 32/30 | 19/30 | 0,57 | 0,46 | -0,32R | €-15,06 | 4,81% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC | Scanner Top 5 + forza BTC 1H | 45/30 | 20/30 | 1,71 | 2,23 | 0,40R | €20,83 | 1,74% | COERENTE + | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | Top 5 + BTC — BTC 2–3 | 5/30 | 2/30 | 0,51 | 1,08 | -0,41R | €2,23 | 1,99% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | Top 5 + BTC — BTC≤3 | 5/30 | 2/30 | 0,51 | 1,08 | -0,41R | €2,23 | 1,99% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | Top 5 + BTC — Guard + BTC≤3 + MFE | 3/30 | 3/30 | 0,00 | 0,00 | -1,04R | €-42,49 | 1,90% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | Top 5 + BTC — Guard + BTC≤3 | 3/30 | 2/30 | 0,00 | 0,00 | -1,04R | €-59,29 | 1,64% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | Top 5 + BTC — Guard + MFE | 6/30 | 6/30 | 0,00 | 0,00 | -1,06R | €-39,97 | 3,08% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | Top 5 + BTC — Guard | 6/30 | 5/30 | 0,00 | 0,00 | -1,06R | €-56,10 | 3,31% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | Top 5 + BTC — solo MFE | 8/30 | 5/30 | 0,66 | 0,52 | -0,27R | €-7,01 | 1,61% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | Top 5 + BTC — 75% a 2,2R + runner 3R | 6/30 | 6/30 | 0,55 | 0,90 | -0,39R | €-2,82 | 2,33% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | Top 5 + BTC — target pieno 3R | 6/30 | 6/30 | 0,55 | 0,90 | -0,39R | €-2,82 | 2,33% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_LONG | Scanner Top 5 Long 1H | 58/30 | 28/30 | 1,55 | 1,96 | 0,31R | €18,35 | 2,70% | COERENTE + | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_SOL_ADAPTIVE_1H | Sol Adaptive 1H | 2/30 | 2/30 | 1,70 | 0,67 | 0,39R | €-9,23 | 1,12% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SOL_ADAPTIVE_4H | Sol Adaptive 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,32% | n/a | RACCOLTA RESEARCH |
| SHADOW_SOL_BOLLINGER_1H | Sol Bollinger 1H | 1/30 | 1/30 | 0,00 | 0,00 | -1,13R | €-55,79 | 0,62% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_BOLLINGER_4H | Sol Bollinger 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,40% | n/a | RACCOLTA RESEARCH |
| SHADOW_SOL_DONCHIAN_1H | Sol Donchian 1H | 1/30 | 2/30 | 0,00 | 0,41 | -1,12R | €-1,31 | 0,55% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_DONCHIAN_4H | Sol Donchian 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,35% | n/a | RACCOLTA RESEARCH |
| SHADOW_SOL_EMA_1H | Sol Ema 1H | 2/30 | 2/30 | 1,70 | 0,83 | 0,39R | €-4,58 | 1,10% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SOL_EMA_4H | Sol Ema 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,35% | n/a | RACCOLTA RESEARCH |

Per le famiglie RSI con più configurazioni di leva o margine, il lato paper usa il conto con il maggior numero di eventi indipendenti; i conti duplicati non vengono aggregati.
`PRONTA PER REVISIONE LIVE` non invia ordini e non sposta capitale: abilita soltanto una revisione manuale finale.

## 🎯 DOGE Rejection Short — conto dedicato €3.600

Simulazione separata **paper only**: capitale/margine iniziale **€3.600**, leva **5x**, esposizione iniziale **€18.000**. Non modifica i conti paper da €10.000 e non invia ordini reali.

- Stato: **WAITING**
- Prezzo DOGE: **0.073**
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
| BTC sotto filtro | 66097.49 | NO |

### Ultima candela 15m valutata

- Rejection accettata: **NO**; motivo: **trigger_touched, entry_not_chased**
- High **0.07312**; close **0.07296**; wick alta **43.7%**; volume **x0.83**

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
- Confidenza: **73,10%**
- Volatilità: **NORMAL**
- Rotazione strategie: **SOLO OSSERVAZIONE — nessun peso operativo viene ancora modificato**
- Motivo: Trend BTC rialzista confermato dalla breadth: score +3.0, 67% sopra EMA50, ADX 29.3.
- BTC trend score: **3,00**; ADX: **29,34**; breadth sopra EMA50: **66,67%**
- Mediana alt vs BTC: **0,60%**; dispersione: **8,57%**

- Aperti in questo ciclo: **17**
- Chiusi in questo ciclo: **6**
- Posizioni research aperte: **397**
- Trade research chiusi: **1485**
- Eventi di mercato indipendenti chiusi: **469**
- Segnali sovrapposti saltati sullo stesso asset/profilo: **5865**
- Posizioni Research V1 senza regime scartate durante la migrazione: **28**

### Risultati complessivi per strategia

| Profilo | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| MAIN | 14 | 39 | 39 | 30,77% | 0,86 | -0,10R | €-39,07 |
| RSI_EXTREME_LONG_15M | 0 | 2 | 2 | 100,00% | ∞ | 0,97R | €19,43 |
| RSI_EXTREME_SHORT_15M | 0 | 7 | 7 | 28,57% | 0,62 | -0,24R | €-16,64 |
| Bilanciata 1H V1 | 14 | 132 | 132 | 33,33% | 0,94 | -0,04R | €-49,84 |
| Bilanciata 1H V2 | 6 | 23 | 20 | 43,48% | 1,53 | 0,30R | €67,85 |
| Bilanciata 1H V3 Filtered | 9 | 41 | 41 | 39,02% | 1,19 | 0,12R | €49,34 |
| Rapida 1H V1 | 9 | 153 | 153 | 37,91% | 0,86 | -0,09R | €-135,78 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | 5 | 3 | 3 | 33,33% | 0,66 | -0,24R | €-7,28 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | 6 | 22 | 22 | 31,82% | 0,61 | -0,28R | €-62,46 |
| SHADOW_1H_FAST_NO_PEPE_V1 | 7 | 23 | 23 | 30,43% | 0,57 | -0,32R | €-73,44 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | 2 | 15 | 15 | 40,00% | 0,86 | -0,09R | €-13,10 |
| SHADOW_1H_FAST_TP2_V1 | 7 | 21 | 21 | 19,05% | 0,41 | -0,51R | €-106,72 |
| Rapida 1H V2 | 0 | 5 | 4 | 20,00% | 0,30 | -0,62R | €-31,20 |
| Rapida 1H V3 Filtered | 4 | 65 | 65 | 41,54% | 0,95 | -0,03R | €-19,50 |
| SHADOW_1H_FAST_V3_CAP75_V1 | 2 | 21 | 21 | 33,33% | 0,66 | -0,24R | €-51,13 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | 1 | 9 | 9 | 22,22% | 0,36 | -0,54R | €-48,97 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | 1 | 9 | 9 | 22,22% | 0,36 | -0,54R | €-48,97 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | 2 | 10 | 10 | 20,00% | 0,31 | -0,60R | €-60,07 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | 1 | 23 | 23 | 30,43% | 0,57 | -0,32R | €-72,96 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | 2 | 23 | 23 | 30,43% | 0,57 | -0,32R | €-73,04 |
| SHADOW_4H_WIDE | 19 | 38 | 38 | 23,68% | 0,85 | -0,12R | €-45,80 |
| SHADOW_BOLLINGER_MR_1H | 1 | 29 | 29 | 44,83% | 1,07 | 0,04R | €11,89 |
| SHADOW_BTC_ADAPTIVE_1H | 1 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_BTC_ADAPTIVE_4H | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_BOLLINGER_1H | 0 | 2 | 2 | 100,00% | ∞ | 1,37R | €27,33 |
| SHADOW_BTC_BOLLINGER_4H | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_DONCHIAN_1H | 1 | 2 | 2 | 0,00% | 0,00 | -1,12R | €-22,50 |
| SHADOW_BTC_DONCHIAN_4H | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_EMA_1H | 0 | 4 | 4 | 25,00% | 0,57 | -0,36R | €-14,44 |
| SHADOW_BTC_EMA_4H | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_ADAPTIVE | 14 | 73 | 73 | 41,10% | 1,29 | 0,18R | €130,68 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | 8 | 11 | 11 | 27,27% | 0,67 | -0,26R | €-28,51 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | 13 | 41 | 41 | 39,02% | 1,18 | 0,12R | €48,12 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | 9 | 19 | 19 | 26,32% | 0,64 | -0,29R | €-54,42 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | 2 | 3 | 3 | 0,00% | 0,00 | -1,07R | €-32,05 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | 2 | 3 | 3 | 0,00% | 0,00 | -1,07R | €-32,05 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | 2 | 3 | 3 | 0,00% | 0,00 | -1,07R | €-32,02 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | 10 | 16 | 16 | 18,75% | 0,42 | -0,50R | €-80,62 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | 11 | 13 | 13 | 15,38% | 0,50 | -0,45R | €-58,60 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | 11 | 13 | 13 | 15,38% | 0,50 | -0,45R | €-58,60 |
| SHADOW_COMBO_MEAN_REVERSION | 1 | 10 | 10 | 50,00% | 1,43 | 0,23R | €22,73 |
| SHADOW_COMBO_SCANNER | 10 | 44 | 44 | 45,45% | 1,64 | 0,37R | €162,78 |
| SHADOW_COMBO_TREND | 13 | 57 | 57 | 35,09% | 1,11 | 0,08R | €43,23 |
| SHADOW_DOGE_DONCHIAN_1H | 0 | 1 | 1 | 0,00% | 0,00 | -1,12R | €-11,25 |
| SHADOW_DOGE_EMA_1H | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_DONCHIAN_1H | 7 | 33 | 33 | 30,30% | 0,99 | -0,01R | €-2,69 |
| SHADOW_EMA_TREND_1H | 13 | 64 | 64 | 32,81% | 1,05 | 0,03R | €22,15 |
| SHADOW_ETH_ADAPTIVE_1H | 1 | 2 | 2 | 50,00% | 1,70 | 0,39R | €7,78 |
| SHADOW_ETH_BOLLINGER_1H | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,33 |
| SHADOW_ETH_DONCHIAN_1H | 0 | 3 | 3 | 33,33% | 0,84 | -0,12R | €-3,61 |
| SHADOW_ETH_EMA_1H | 1 | 2 | 2 | 50,00% | 1,70 | 0,39R | €7,78 |
| SHADOW_ETH_EMA_4H | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_GLOBAL_PURE | 1 | 1 | 1 | 0,00% | 0,00 | -1,10R | €-11,00 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | 8 | 7 | 7 | 14,29% | 0,29 | -0,65R | €-45,56 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | 8 | 6 | 6 | 0,00% | 0,00 | -1,08R | €-64,63 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | 8 | 6 | 6 | 0,00% | 0,00 | -1,08R | €-64,53 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | 8 | 6 | 6 | 0,00% | 0,00 | -1,08R | €-64,63 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | 5 | 6 | 6 | 0,00% | 0,00 | -1,07R | €-63,97 |
| SHADOW_MASTER_ADAPTIVE_V1 | 8 | 6 | 6 | 0,00% | 0,00 | -1,08R | €-64,63 |
| Forza relativa 1H V1 | 9 | 93 | 93 | 30,11% | 0,95 | -0,03R | €-29,90 |
| Forza relativa 1H V2 | 6 | 30 | 27 | 40,00% | 1,39 | 0,25R | €73,52 |
| SHADOW_SCANNER_BOTTOM5_SHORT | 3 | 32 | 32 | 21,88% | 0,57 | -0,32R | €-102,18 |
| SHADOW_SCANNER_TOP5_BTC | 10 | 45 | 45 | 44,44% | 1,71 | 0,40R | €180,71 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | 8 | 5 | 5 | 20,00% | 0,51 | -0,41R | €-20,57 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | 8 | 5 | 5 | 20,00% | 0,51 | -0,41R | €-20,57 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | 4 | 3 | 3 | 0,00% | 0,00 | -1,04R | €-31,06 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | 4 | 3 | 3 | 0,00% | 0,00 | -1,04R | €-31,06 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | 4 | 6 | 6 | 0,00% | 0,00 | -1,06R | €-63,64 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | 4 | 6 | 6 | 0,00% | 0,00 | -1,06R | €-63,64 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | 9 | 8 | 8 | 25,00% | 0,66 | -0,27R | €-21,62 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | 9 | 6 | 6 | 16,67% | 0,55 | -0,39R | €-23,52 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | 9 | 6 | 6 | 16,67% | 0,55 | -0,39R | €-23,52 |
| SHADOW_SCANNER_TOP5_LONG | 10 | 58 | 58 | 44,83% | 1,55 | 0,31R | €180,85 |
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
| MAIN | TRANSITION | 2 | 6 | 6 | 33,33% | 0,97 | -0,02R | €-1,10 |
| MAIN | TREND_UP | 5 | 12 | 12 | 33,33% | 0,96 | -0,03R | €-3,22 |
| MAIN | TREND_UP_HIGH_VOL | 3 | 3 | 3 | 33,33% | 0,98 | -0,01R | €-0,40 |
| RSI_EXTREME_LONG_15M | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,29R | €12,88 |
| RSI_EXTREME_LONG_15M | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 0,66R | €6,56 |
| RSI_EXTREME_SHORT_15M | ALT_ROTATION_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 1,47R | €14,67 |
| RSI_EXTREME_SHORT_15M | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,90 |
| RSI_EXTREME_SHORT_15M | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -0,41R | €-4,13 |
| RSI_EXTREME_SHORT_15M | TREND_UP | 0 | 4 | 4 | 25,00% | 0,44 | -0,41R | €-16,27 |
| Bilanciata 1H V1 | ALT_ROTATION_DOWN | 2 | 6 | 6 | 33,33% | 0,88 | -0,08R | €-5,07 |
| Bilanciata 1H V1 | ALT_ROTATION_UP | 0 | 14 | 14 | 50,00% | 1,84 | 0,44R | €61,99 |
| Bilanciata 1H V1 | RANGE | 0 | 28 | 28 | 32,14% | 0,91 | -0,06R | €-16,44 |
| Bilanciata 1H V1 | RANGE_HIGH_VOL | 1 | 10 | 10 | 0,00% | 0,00 | -1,07R | €-107,38 |
| Bilanciata 1H V1 | TRANSITION | 2 | 26 | 26 | 30,77% | 0,85 | -0,11R | €-27,93 |
| Bilanciata 1H V1 | TREND_UP | 5 | 39 | 39 | 38,46% | 1,21 | 0,13R | €50,64 |
| Bilanciata 1H V1 | TREND_UP_HIGH_VOL | 4 | 9 | 9 | 33,33% | 0,91 | -0,06R | €-5,65 |
| Bilanciata 1H V2 | ALT_ROTATION_UP | 1 | 5 | 4 | 80,00% | 7,13 | 1,32R | €66,22 |
| Bilanciata 1H V2 | RANGE | 0 | 6 | 5 | 33,33% | 1,19 | 0,10R | €6,25 |
| Bilanciata 1H V2 | TRANSITION | 5 | 12 | 11 | 33,33% | 0,94 | -0,04R | €-4,62 |
| Bilanciata 1H V3 Filtered | ALT_ROTATION_DOWN | 1 | 4 | 4 | 50,00% | 1,82 | 0,43R | €17,15 |
| Bilanciata 1H V3 Filtered | ALT_ROTATION_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,05R | €-20,99 |
| Bilanciata 1H V3 Filtered | RANGE_HIGH_VOL | 1 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| Bilanciata 1H V3 Filtered | TRANSITION | 0 | 6 | 6 | 33,33% | 0,92 | -0,06R | €-3,44 |
| Bilanciata 1H V3 Filtered | TREND_UP | 2 | 19 | 19 | 47,37% | 1,70 | 0,38R | €72,47 |
| Bilanciata 1H V3 Filtered | TREND_UP_HIGH_VOL | 5 | 9 | 9 | 33,33% | 0,91 | -0,06R | €-5,71 |
| Rapida 1H V1 | ALT_ROTATION_DOWN | 2 | 9 | 9 | 33,33% | 0,64 | -0,26R | €-23,06 |
| Rapida 1H V1 | ALT_ROTATION_UP | 1 | 11 | 11 | 54,55% | 1,64 | 0,31R | €33,84 |
| Rapida 1H V1 | RANGE | 0 | 35 | 35 | 40,00% | 1,04 | 0,02R | €8,01 |
| Rapida 1H V1 | RANGE_HIGH_VOL | 0 | 11 | 11 | 0,00% | 0,00 | -1,09R | €-119,90 |
| Rapida 1H V1 | TRANSITION | 1 | 23 | 23 | 43,48% | 1,20 | 0,11R | €24,41 |
| Rapida 1H V1 | TREND_UP | 2 | 46 | 46 | 41,30% | 0,95 | -0,03R | €-13,15 |
| Rapida 1H V1 | TREND_UP_HIGH_VOL | 3 | 18 | 18 | 33,33% | 0,65 | -0,26R | €-45,94 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | ALT_ROTATION_DOWN | 2 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,20 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,39R | €13,89 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TRANSITION | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TREND_UP | 2 | 1 | 1 | 0,00% | 0,00 | -1,10R | €-10,97 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | ALT_ROTATION_DOWN | 2 | 8 | 8 | 37,50% | 0,78 | -0,15R | €-11,63 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,39R | €13,89 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TRANSITION | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TREND_UP | 3 | 13 | 13 | 23,08% | 0,39 | -0,50R | €-64,73 |
| SHADOW_1H_FAST_NO_PEPE_V1 | ALT_ROTATION_DOWN | 2 | 8 | 8 | 37,50% | 0,78 | -0,15R | €-11,63 |
| SHADOW_1H_FAST_NO_PEPE_V1 | ALT_ROTATION_UP | 1 | 4 | 4 | 50,00% | 1,26 | 0,14R | €5,60 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TRANSITION | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_UP | 3 | 11 | 11 | 18,18% | 0,29 | -0,61R | €-67,42 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | ALT_ROTATION_DOWN | 0 | 5 | 5 | 60,00% | 1,93 | 0,40R | €20,14 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | ALT_ROTATION_UP | 1 | 3 | 3 | 66,67% | 2,50 | 0,55R | €16,50 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_UP | 1 | 7 | 7 | 14,29% | 0,22 | -0,71R | €-49,74 |
| SHADOW_1H_FAST_TP2_V1 | ALT_ROTATION_DOWN | 3 | 6 | 6 | 16,67% | 0,35 | -0,57R | €-34,33 |
| SHADOW_1H_FAST_TP2_V1 | ALT_ROTATION_UP | 1 | 3 | 3 | 33,33% | 0,84 | -0,12R | €-3,50 |
| SHADOW_1H_FAST_TP2_V1 | TRANSITION | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_1H_FAST_TP2_V1 | TREND_UP | 2 | 12 | 12 | 16,67% | 0,36 | -0,57R | €-68,89 |
| Rapida 1H V2 | ALT_ROTATION_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,10R | €-21,92 |
| Rapida 1H V2 | RANGE | 0 | 2 | 1 | 50,00% | 1,19 | 0,11R | €2,14 |
| Rapida 1H V2 | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -1,14R | €-11,43 |
| Rapida 1H V3 Filtered | ALT_ROTATION_DOWN | 0 | 9 | 9 | 33,33% | 0,66 | -0,24R | €-21,76 |
| Rapida 1H V3 Filtered | ALT_ROTATION_UP | 1 | 4 | 4 | 75,00% | 3,92 | 0,80R | €31,86 |
| Rapida 1H V3 Filtered | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| Rapida 1H V3 Filtered | TRANSITION | 0 | 5 | 5 | 40,00% | 0,91 | -0,06R | €-2,77 |
| Rapida 1H V3 Filtered | TREND_UP | 0 | 29 | 29 | 48,28% | 1,27 | 0,15R | €43,00 |
| Rapida 1H V3 Filtered | TREND_UP_HIGH_VOL | 3 | 17 | 17 | 29,41% | 0,54 | -0,35R | €-59,70 |
| SHADOW_1H_FAST_V3_CAP75_V1 | ALT_ROTATION_DOWN | 0 | 8 | 8 | 37,50% | 0,80 | -0,13R | €-10,34 |
| SHADOW_1H_FAST_V3_CAP75_V1 | ALT_ROTATION_UP | 1 | 3 | 3 | 66,67% | 2,50 | 0,55R | €16,50 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_UP | 1 | 10 | 10 | 20,00% | 0,33 | -0,57R | €-57,30 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | ALT_ROTATION_DOWN | 0 | 2 | 2 | 0,00% | 0,00 | -1,08R | €-21,63 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,39R | €13,89 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TREND_UP | 1 | 6 | 6 | 16,67% | 0,25 | -0,69R | €-41,23 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | ALT_ROTATION_DOWN | 0 | 2 | 2 | 0,00% | 0,00 | -1,08R | €-21,63 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,39R | €13,89 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TREND_UP | 1 | 6 | 6 | 16,67% | 0,25 | -0,69R | €-41,23 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 0 | 2 | 2 | 0,00% | 0,00 | -1,08R | €-21,63 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | ALT_ROTATION_UP | 1 | 3 | 3 | 66,67% | 2,50 | 0,55R | €16,50 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_UP | 1 | 5 | 5 | 0,00% | 0,00 | -1,10R | €-54,93 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | ALT_ROTATION_DOWN | 0 | 8 | 8 | 37,50% | 0,80 | -0,13R | €-10,34 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | ALT_ROTATION_UP | 0 | 2 | 2 | 50,00% | 1,27 | 0,15R | €3,00 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TREND_UP | 1 | 13 | 13 | 23,08% | 0,39 | -0,50R | €-65,62 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | ALT_ROTATION_DOWN | 0 | 8 | 8 | 37,50% | 0,80 | -0,13R | €-10,34 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | ALT_ROTATION_UP | 1 | 4 | 4 | 50,00% | 1,26 | 0,14R | €5,60 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_UP | 1 | 11 | 11 | 18,18% | 0,29 | -0,62R | €-68,31 |
| SHADOW_4H_WIDE | ALT_ROTATION_DOWN | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_4H_WIDE | ALT_ROTATION_UP | 2 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_4H_WIDE | RANGE | 2 | 15 | 15 | 26,67% | 0,98 | -0,01R | €-1,81 |
| SHADOW_4H_WIDE | TRANSITION | 3 | 7 | 7 | 14,29% | 0,46 | -0,47R | €-33,10 |
| SHADOW_4H_WIDE | TREND_UP | 6 | 10 | 10 | 40,00% | 1,81 | 0,50R | €49,91 |
| SHADOW_4H_WIDE | TREND_UP_HIGH_VOL | 4 | 4 | 4 | 0,00% | 0,00 | -1,01R | €-40,53 |
| SHADOW_BOLLINGER_MR_1H | ALT_ROTATION_DOWN | 1 | 2 | 2 | 50,00% | 1,24 | 0,13R | €2,66 |
| SHADOW_BOLLINGER_MR_1H | ALT_ROTATION_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,02R | €-20,30 |
| SHADOW_BOLLINGER_MR_1H | RANGE | 0 | 7 | 7 | 42,86% | 0,98 | -0,01R | €-0,83 |
| SHADOW_BOLLINGER_MR_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_BOLLINGER_MR_1H | TRANSITION | 0 | 3 | 3 | 33,33% | 0,71 | -0,20R | €-6,14 |
| SHADOW_BOLLINGER_MR_1H | TREND_UP | 0 | 12 | 12 | 50,00% | 1,28 | 0,15R | €18,32 |
| SHADOW_BOLLINGER_MR_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,31 | 0,17R | €3,31 |
| SHADOW_BTC_ADAPTIVE_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_BTC_ADAPTIVE_1H | TREND_UP_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_ADAPTIVE_4H | TREND_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_BOLLINGER_1H | RANGE | 0 | 1 | 1 | 100,00% | ∞ | 1,37R | €13,67 |
| SHADOW_BTC_BOLLINGER_1H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,37R | €13,67 |
| SHADOW_BTC_BOLLINGER_4H | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_DONCHIAN_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,12R | €-11,25 |
| SHADOW_BTC_DONCHIAN_1H | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -1,12R | €-11,25 |
| SHADOW_BTC_DONCHIAN_1H | TREND_UP_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_DONCHIAN_4H | TREND_UP_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_EMA_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_BTC_EMA_1H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_BTC_EMA_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,70 | 0,39R | €7,78 |
| SHADOW_BTC_EMA_4H | TREND_UP_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_ADAPTIVE | ALT_ROTATION_DOWN | 2 | 4 | 4 | 50,00% | 1,77 | 0,42R | €16,61 |
| SHADOW_COMBO_ADAPTIVE | ALT_ROTATION_UP | 1 | 5 | 5 | 40,00% | 1,22 | 0,14R | €6,88 |
| SHADOW_COMBO_ADAPTIVE | RANGE | 0 | 12 | 12 | 25,00% | 0,60 | -0,32R | €-38,47 |
| SHADOW_COMBO_ADAPTIVE | RANGE_HIGH_VOL | 1 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE | TRANSITION | 1 | 17 | 17 | 47,06% | 1,64 | 0,36R | €60,98 |
| SHADOW_COMBO_ADAPTIVE | TREND_UP | 4 | 27 | 27 | 48,15% | 1,74 | 0,40R | €108,26 |
| SHADOW_COMBO_ADAPTIVE | TREND_UP_HIGH_VOL | 5 | 7 | 7 | 28,57% | 0,74 | -0,19R | €-13,44 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | ALT_ROTATION_UP | 1 | 3 | 3 | 66,67% | 3,50 | 0,90R | €27,00 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_UP | 5 | 3 | 3 | 0,00% | 0,00 | -1,10R | €-32,91 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_UP_HIGH_VOL | 1 | 5 | 5 | 20,00% | 0,46 | -0,45R | €-22,60 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | ALT_ROTATION_DOWN | 2 | 4 | 4 | 50,00% | 1,77 | 0,42R | €16,61 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | ALT_ROTATION_UP | 1 | 6 | 6 | 33,33% | 0,90 | -0,07R | €-4,23 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE_HIGH_VOL | 1 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TRANSITION | 0 | 2 | 2 | 50,00% | 1,72 | 0,40R | €8,01 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_UP | 4 | 19 | 19 | 47,37% | 1,71 | 0,39R | €73,37 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_UP_HIGH_VOL | 5 | 9 | 9 | 22,22% | 0,52 | -0,39R | €-35,51 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | ALT_ROTATION_DOWN | 2 | 4 | 4 | 50,00% | 1,77 | 0,42R | €16,61 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | ALT_ROTATION_UP | 1 | 3 | 3 | 66,67% | 3,50 | 0,90R | €27,00 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_UP | 5 | 5 | 5 | 0,00% | 0,00 | -1,06R | €-53,20 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_UP_HIGH_VOL | 1 | 6 | 6 | 16,67% | 0,36 | -0,56R | €-33,71 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TRANSITION | 1 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,86 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TREND_UP | 1 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,18 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TRANSITION | 1 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,86 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TREND_UP | 1 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,18 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | ALT_ROTATION_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,84 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TRANSITION | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,18 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TRANSITION | 1 | 2 | 2 | 0,00% | 0,00 | -1,10R | €-21,93 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TREND_UP | 7 | 8 | 8 | 25,00% | 0,60 | -0,31R | €-24,98 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TREND_UP_HIGH_VOL | 2 | 6 | 6 | 16,67% | 0,36 | -0,56R | €-33,71 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_DOWN | 2 | 3 | 3 | 33,33% | 1,35 | 0,25R | €7,43 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_UP | 3 | 2 | 2 | 50,00% | 2,74 | 0,93R | €18,60 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | TREND_UP | 5 | 4 | 4 | 0,00% | 0,00 | -1,05R | €-42,15 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | TREND_UP_HIGH_VOL | 1 | 3 | 3 | 0,00% | 0,00 | -1,05R | €-31,38 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | ALT_ROTATION_DOWN | 2 | 3 | 3 | 33,33% | 1,35 | 0,25R | €7,43 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | ALT_ROTATION_UP | 3 | 2 | 2 | 50,00% | 2,74 | 0,93R | €18,60 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | TREND_UP | 5 | 4 | 4 | 0,00% | 0,00 | -1,05R | €-42,15 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | TREND_UP_HIGH_VOL | 1 | 3 | 3 | 0,00% | 0,00 | -1,05R | €-31,38 |
| SHADOW_COMBO_MEAN_REVERSION | ALT_ROTATION_DOWN | 0 | 2 | 2 | 0,00% | 0,00 | -1,08R | €-21,65 |
| SHADOW_COMBO_MEAN_REVERSION | RANGE | 0 | 4 | 4 | 75,00% | 4,46 | 0,88R | €35,25 |
| SHADOW_COMBO_MEAN_REVERSION | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,94 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_UP | 1 | 2 | 2 | 50,00% | 1,50 | 0,25R | €5,04 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,85 |
| SHADOW_COMBO_SCANNER | ALT_ROTATION_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_COMBO_SCANNER | ALT_ROTATION_UP | 0 | 4 | 4 | 50,00% | 2,09 | 0,57R | €22,81 |
| SHADOW_COMBO_SCANNER | RANGE | 0 | 2 | 2 | 50,00% | 2,10 | 0,57R | €11,44 |
| SHADOW_COMBO_SCANNER | RANGE_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_SCANNER | TRANSITION | 1 | 13 | 13 | 38,46% | 1,08 | 0,05R | €6,95 |
| SHADOW_COMBO_SCANNER | TREND_UP | 4 | 18 | 18 | 50,00% | 2,05 | 0,55R | €99,87 |
| SHADOW_COMBO_SCANNER | TREND_UP_HIGH_VOL | 3 | 6 | 6 | 50,00% | 2,05 | 0,55R | €32,82 |
| SHADOW_COMBO_TREND | ALT_ROTATION_DOWN | 3 | 2 | 2 | 50,00% | 1,91 | 0,50R | €10,05 |
| SHADOW_COMBO_TREND | ALT_ROTATION_UP | 0 | 5 | 5 | 40,00% | 1,39 | 0,24R | €12,22 |
| SHADOW_COMBO_TREND | RANGE | 0 | 8 | 8 | 12,50% | 0,29 | -0,67R | €-53,33 |
| SHADOW_COMBO_TREND | RANGE_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_TREND | TRANSITION | 1 | 14 | 14 | 42,86% | 1,55 | 0,33R | €46,22 |
| SHADOW_COMBO_TREND | TREND_UP | 4 | 21 | 21 | 38,10% | 1,28 | 0,18R | €37,44 |
| SHADOW_COMBO_TREND | TREND_UP_HIGH_VOL | 4 | 7 | 7 | 28,57% | 0,82 | -0,13R | €-9,36 |
| SHADOW_DOGE_DONCHIAN_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,12R | €-11,25 |
| SHADOW_DOGE_EMA_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_DONCHIAN_1H | ALT_ROTATION_DOWN | 2 | 2 | 2 | 50,00% | 2,19 | 0,65R | €13,05 |
| SHADOW_DONCHIAN_1H | ALT_ROTATION_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,85 |
| SHADOW_DONCHIAN_1H | RANGE | 0 | 8 | 8 | 12,50% | 0,32 | -0,64R | €-51,15 |
| SHADOW_DONCHIAN_1H | RANGE_HIGH_VOL | 1 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_DONCHIAN_1H | TRANSITION | 1 | 6 | 6 | 16,67% | 0,45 | -0,48R | €-28,95 |
| SHADOW_DONCHIAN_1H | TREND_UP | 0 | 11 | 11 | 45,45% | 1,89 | 0,53R | €57,82 |
| SHADOW_DONCHIAN_1H | TREND_UP_HIGH_VOL | 3 | 3 | 3 | 66,67% | 4,47 | 1,25R | €37,51 |
| SHADOW_EMA_TREND_1H | ALT_ROTATION_DOWN | 2 | 3 | 3 | 33,33% | 0,98 | -0,02R | €-0,50 |
| SHADOW_EMA_TREND_1H | ALT_ROTATION_UP | 1 | 4 | 4 | 25,00% | 0,71 | -0,23R | €-9,11 |
| SHADOW_EMA_TREND_1H | RANGE | 1 | 9 | 9 | 11,11% | 0,29 | -0,59R | €-53,03 |
| SHADOW_EMA_TREND_1H | RANGE_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_EMA_TREND_1H | TRANSITION | 1 | 14 | 14 | 42,86% | 1,55 | 0,33R | €46,21 |
| SHADOW_EMA_TREND_1H | TREND_UP | 3 | 27 | 27 | 33,33% | 1,09 | 0,06R | €15,61 |
| SHADOW_EMA_TREND_1H | TREND_UP_HIGH_VOL | 4 | 7 | 7 | 42,86% | 1,56 | 0,33R | €22,97 |
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
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | ALT_ROTATION_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,79 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TRANSITION | 1 | 1 | 1 | 100,00% | ∞ | 1,90R | €19,01 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TREND_UP | 6 | 4 | 4 | 0,00% | 0,00 | -1,07R | €-42,66 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,86 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TREND_UP | 7 | 5 | 5 | 0,00% | 0,00 | -1,08R | €-53,77 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TREND_UP | 7 | 6 | 6 | 0,00% | 0,00 | -1,08R | €-64,53 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,86 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | TREND_UP | 7 | 5 | 5 | 0,00% | 0,00 | -1,08R | €-53,77 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TREND_UP | 5 | 6 | 6 | 0,00% | 0,00 | -1,07R | €-63,97 |
| SHADOW_MASTER_ADAPTIVE_V1 | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_MASTER_ADAPTIVE_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,86 |
| SHADOW_MASTER_ADAPTIVE_V1 | TREND_UP | 7 | 5 | 5 | 0,00% | 0,00 | -1,08R | €-53,77 |
| Forza relativa 1H V1 | ALT_ROTATION_DOWN | 1 | 4 | 4 | 0,00% | 0,00 | -1,05R | €-42,19 |
| Forza relativa 1H V1 | ALT_ROTATION_UP | 1 | 12 | 12 | 33,33% | 1,02 | 0,01R | €1,43 |
| Forza relativa 1H V1 | RANGE | 0 | 20 | 20 | 20,00% | 0,55 | -0,36R | €-71,11 |
| Forza relativa 1H V1 | RANGE_HIGH_VOL | 1 | 2 | 2 | 0,00% | 0,00 | -1,02R | €-20,33 |
| Forza relativa 1H V1 | TRANSITION | 1 | 13 | 13 | 46,15% | 1,81 | 0,45R | €58,14 |
| Forza relativa 1H V1 | TREND_UP | 4 | 34 | 34 | 38,24% | 1,51 | 0,28R | €95,30 |
| Forza relativa 1H V1 | TREND_UP_HIGH_VOL | 1 | 8 | 8 | 12,50% | 0,30 | -0,64R | €-51,15 |
| Forza relativa 1H V2 | ALT_ROTATION_DOWN | 2 | 1 | 1 | 100,00% | ∞ | 2,11R | €21,13 |
| Forza relativa 1H V2 | ALT_ROTATION_UP | 1 | 3 | 3 | 33,33% | 0,98 | -0,02R | €-0,45 |
| Forza relativa 1H V2 | RANGE | 0 | 3 | 3 | 66,67% | 4,31 | 1,12R | €33,59 |
| Forza relativa 1H V2 | TRANSITION | 2 | 9 | 8 | 33,33% | 1,05 | 0,03R | €3,12 |
| Forza relativa 1H V2 | TREND_UP | 1 | 10 | 9 | 50,00% | 2,12 | 0,58R | €57,73 |
| Forza relativa 1H V2 | TREND_UP_HIGH_VOL | 0 | 4 | 3 | 0,00% | 0,00 | -1,04R | €-41,60 |
| SHADOW_SCANNER_BOTTOM5_SHORT | ALT_ROTATION_DOWN | 1 | 3 | 3 | 66,67% | 3,53 | 0,91R | €27,28 |
| SHADOW_SCANNER_BOTTOM5_SHORT | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| SHADOW_SCANNER_BOTTOM5_SHORT | RANGE | 0 | 7 | 7 | 0,00% | 0,00 | -1,08R | €-75,76 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TRANSITION | 1 | 12 | 12 | 33,33% | 0,98 | -0,01R | €-1,28 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP | 0 | 7 | 7 | 0,00% | 0,00 | -0,73R | €-51,04 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP_HIGH_VOL | 1 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,24 |
| SHADOW_SCANNER_TOP5_BTC | ALT_ROTATION_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_SCANNER_TOP5_BTC | ALT_ROTATION_UP | 0 | 5 | 5 | 40,00% | 1,39 | 0,25R | €12,28 |
| SHADOW_SCANNER_TOP5_BTC | RANGE | 0 | 5 | 5 | 60,00% | 5,82 | 1,06R | €53,24 |
| SHADOW_SCANNER_TOP5_BTC | RANGE_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC | TRANSITION | 1 | 11 | 11 | 36,36% | 1,20 | 0,13R | €14,31 |
| SHADOW_SCANNER_TOP5_BTC | TREND_UP | 4 | 17 | 17 | 47,06% | 1,84 | 0,47R | €79,16 |
| SHADOW_SCANNER_TOP5_BTC | TREND_UP_HIGH_VOL | 3 | 6 | 6 | 50,00% | 2,05 | 0,55R | €32,82 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | ALT_ROTATION_DOWN | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,86 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TRANSITION | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TREND_UP | 3 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TREND_UP_HIGH_VOL | 2 | 4 | 4 | 25,00% | 0,69 | -0,24R | €-9,71 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | ALT_ROTATION_DOWN | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,86 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TRANSITION | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_UP | 3 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_UP_HIGH_VOL | 2 | 4 | 4 | 25,00% | 0,69 | -0,24R | €-9,71 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | ALT_ROTATION_DOWN | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,79 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TRANSITION | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | ALT_ROTATION_DOWN | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,79 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TRANSITION | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | ALT_ROTATION_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,79 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TRANSITION | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_UP | 2 | 2 | 2 | 0,00% | 0,00 | -1,07R | €-21,47 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | ALT_ROTATION_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,79 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TRANSITION | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_UP | 2 | 2 | 2 | 0,00% | 0,00 | -1,07R | €-21,47 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | ALT_ROTATION_DOWN | 1 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,79 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TRANSITION | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_UP | 4 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_UP_HIGH_VOL | 3 | 6 | 6 | 33,33% | 1,01 | 0,00R | €0,29 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | ALT_ROTATION_UP | 2 | 2 | 2 | 50,00% | 2,74 | 0,93R | €18,60 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TRANSITION | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_UP | 4 | 2 | 2 | 0,00% | 0,00 | -1,09R | €-21,85 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_UP_HIGH_VOL | 1 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | ALT_ROTATION_UP | 2 | 2 | 2 | 50,00% | 2,74 | 0,93R | €18,60 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TRANSITION | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_UP | 4 | 2 | 2 | 0,00% | 0,00 | -1,09R | €-21,85 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_UP_HIGH_VOL | 1 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_LONG | ALT_ROTATION_DOWN | 1 | 2 | 2 | 0,00% | 0,00 | -1,11R | €-22,22 |
| SHADOW_SCANNER_TOP5_LONG | ALT_ROTATION_UP | 0 | 6 | 6 | 33,33% | 0,92 | -0,06R | €-3,32 |
| SHADOW_SCANNER_TOP5_LONG | RANGE | 0 | 6 | 6 | 66,67% | 7,07 | 1,12R | €67,10 |
| SHADOW_SCANNER_TOP5_LONG | RANGE_HIGH_VOL | 1 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_LONG | TRANSITION | 1 | 11 | 11 | 36,36% | 1,09 | 0,06R | €6,31 |
| SHADOW_SCANNER_TOP5_LONG | TREND_UP | 4 | 26 | 26 | 50,00% | 1,85 | 0,45R | €116,81 |
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

Generato: 2026-07-23T01:08:42+00:00

> Motore esclusivamente osservativo e Paper-only. Non modifica le uscite reali. I confronti escludono il funding sia dall'uscita originale sia dalle varianti.

## Stato operativo

- Gruppi di trade ancora monitorati: **267**
- Scenari virtuali ancora attivi: **2421**
- Gruppi in attesa dell'uscita originale: **153**
- Gruppi con originale chiuso ma Shadow ancora attive: **114**
- Confronti completati: **10410**

## Classifica osservativa complessiva

| Scenario | Campione completo | Campione totale | Δ medio vs originale | Migliora | Troppo presto | Troppo tardi | Stato dati |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| GB20_R050 | 476 | 537 | +€8,28 | 47,1% | 123 | 0 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R050 | 476 | 537 | +€6,51 | 46,0% | 123 | 7 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R050 | 476 | 537 | +€4,52 | 45,3% | 124 | 10 | READY_FOR_BLOCK4_EVALUATION |
| TP_R050 | 476 | 537 | +€3,67 | 45,6% | 132 | 0 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R050 | 476 | 537 | +€2,56 | 44,5% | 119 | 19 | READY_FOR_BLOCK4_EVALUATION |
| TIME_6H | 476 | 537 | €-0,60 | 50,5% | 109 | 60 | READY_FOR_BLOCK4_EVALUATION |
| TIME_12H | 475 | 536 | +€1,71 | 43,1% | 41 | 118 | READY_FOR_BLOCK4_EVALUATION |
| GB20_R100 | 469 | 530 | +€4,69 | 37,5% | 105 | 17 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R100 | 469 | 530 | +€3,21 | 37,0% | 96 | 29 | READY_FOR_BLOCK4_EVALUATION |
| TP_R100 | 469 | 530 | +€2,39 | 36,2% | 112 | 17 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R100 | 469 | 530 | +€1,87 | 37,0% | 76 | 47 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R100 | 469 | 530 | +€0,99 | 34,5% | 51 | 86 | READY_FOR_BLOCK4_EVALUATION |
| ATR15_R100 | 469 | 530 | €-3,56 | 28,5% | 33 | 120 | READY_FOR_BLOCK4_EVALUATION |
| ATR20_R100 | 454 | 515 | €-5,04 | 24,7% | 39 | 122 | READY_FOR_BLOCK4_EVALUATION |
| TIME_24H | 451 | 512 | €-3,44 | 29,9% | 22 | 142 | READY_FOR_BLOCK4_EVALUATION |
| ATR30_R100 | 448 | 509 | €-8,36 | 21,6% | 35 | 123 | READY_FOR_BLOCK4_EVALUATION |
| TP_R150 | 444 | 505 | +€1,33 | 27,7% | 48 | 53 | READY_FOR_BLOCK4_EVALUATION |
| BE_R050 | 433 | 494 | €-7,37 | 26,5% | 85 | 62 | READY_FOR_BLOCK4_EVALUATION |
| TP_R200 | 420 | 481 | €-0,63 | 30,4% | 20 | 81 | READY_FOR_BLOCK4_EVALUATION |
| BE_R100 | 396 | 456 | €-13,75 | 16,9% | 34 | 102 | READY_FOR_BLOCK4_EVALUATION |

## Come leggere il controllo

- **EARLIER_BETTER**: la variante è uscita prima e ha conservato più profitto.
- **TOO_EARLY**: la variante è uscita prima ma ha tagliato un movimento migliore.
- **LATER_BETTER**: la variante ha continuato dopo l'uscita originale e ha guadagnato di più.
- **TOO_LATE**: la variante è rimasta aperta più a lungo e ha peggiorato il risultato.

## Limiti e protezioni

Le regole Shadow mantengono entrata, quantità, commissioni, stop protettivo iniziale e liquidazione. Le ambiguità all'interno della stessa candela vengono risolte scegliendo l'esito peggiore. Le posizioni già aperte al momento dell'installazione sono marcate come campione parziale e non saranno utilizzate dal futuro Blocco 4 come prova piena.

# Blocco 4 — Valutazione statistica Shadow

Generato: 2026-07-23T01:08:43+00:00

> Modulo esclusivamente valutativo. Non modifica strategie, uscite, posizioni o capitale. Le candidature vengono consegnate al futuro Blocco 5, senza applicazione automatica.

## Stato

- Risultati Block 3 disponibili: **10410**
- Valutazioni prodotte: **3284**
- Candidature al Blocco 5: **0**
- Mutazioni create automaticamente: **0**

## Classifica complessiva

| Scenario | Campione pieno | Δ medio (R) | Mediana (R) | CI bootstrap basso | Migliora | Score | Stato |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| TIME_24H | 6 | 0,997 | 1,104 | 0,180 | 66,7% | 74,1 | INSUFFICIENT_DATA |
| GB20_R050 | 470 | 0,197 | 0,000 | 0,119 | 48,1% | 73,8 | VALIDATING |
| TP_R050 | 470 | 0,123 | 0,000 | 0,051 | 46,4% | 73,8 | VALIDATING |
| GB30_R050 | 470 | 0,163 | 0,000 | 0,096 | 46,8% | 73,7 | VALIDATING |
| GB40_R050 | 470 | 0,124 | 0,000 | 0,056 | 46,4% | 73,7 | VALIDATING |
| GB20_R100 | 463 | 0,108 | 0,000 | 0,058 | 37,4% | 73,5 | VALIDATING |
| GB30_R100 | 463 | 0,083 | 0,000 | 0,032 | 36,9% | 73,5 | VALIDATING |
| GB40_R100 | 463 | 0,060 | 0,000 | 0,011 | 36,9% | 73,3 | VALIDATING |
| TP_R150 | 438 | 0,048 | 0,000 | -0,011 | 27,4% | 71,4 | VALIDATING |
| TIME_6H | 470 | 0,028 | 0,039 | -0,049 | 53,6% | 70,2 | VALIDATING |
| GB50_R050 | 470 | 0,081 | 0,000 | 0,015 | 45,7% | 69,9 | VALIDATING |
| TP_R100 | 463 | 0,077 | 0,000 | 0,022 | 35,6% | 69,8 | VALIDATING |
| GB50_R100 | 463 | 0,043 | 0,000 | -0,002 | 34,6% | 68,3 | VALIDATING |
| TIME_12H | 469 | 0,040 | 0,000 | -0,026 | 44,3% | 59,4 | VALIDATING |
| TP_R200 | 6 | 0,472 | 0,250 | -0,017 | 50,0% | 58,7 | INSUFFICIENT_DATA |
| TP_R200 | 414 | -0,024 | 0,000 | -0,096 | 30,4% | 39,7 | VALIDATING |
| TIME_24H | 445 | -0,070 | 0,000 | -0,169 | 28,8% | 34,7 | VALIDATING |
| BE_R050 | 427 | -0,082 | 0,000 | -0,160 | 29,3% | 32,1 | UNDERPERFORMING |
| ATR15_R100 | 463 | -0,055 | 0,000 | -0,102 | 28,1% | 31,1 | UNDERPERFORMING |
| ATR30_R100 | 442 | -0,114 | 0,000 | -0,186 | 23,1% | 31,0 | UNDERPERFORMING |

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

Generato: 2026-07-23T01:08:49+00:00

Questi profili sono osservativi e Paper-only. Usano gli stessi trade della madre, ma applicano una specifica uscita Block 3 soltanto ai segnali aperti dopo la loro registrazione.
Nessuna promozione, modifica live o operazione reale viene eseguita automaticamente.

| Challenger | Madre | Scenario | Chiusi | Copertura | PF | PnL | Exp/trade | DD | Stato |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Rapida 1H V1 — giveback 20% dopo +0,5R | SHADOW_1H_FAST | GB20_R050 | 1 | 100,00% | 0,00 | €-54,51 | €-54,51 | 0,55% | COLLECTING |
| Rapida 1H V1 — giveback 30% dopo +0,5R | SHADOW_1H_FAST | GB30_R050 | 1 | 100,00% | 0,00 | €-54,51 | €-54,51 | 0,55% | COLLECTING |
| Relative Strength — giveback 20% dopo +0,5R | SHADOW_RELATIVE_STRENGTH | GB20_R050 | 1 | 100,00% | 0,00 | €-54,01 | €-54,01 | 0,54% | COLLECTING |
| Relative Strength — giveback 30% dopo +0,5R | SHADOW_RELATIVE_STRENGTH | GB30_R050 | 1 | 100,00% | 0,00 | €-54,01 | €-54,01 | 0,54% | COLLECTING |

## Regole di valutazione

- Prima fotografia a 30 trade indipendenti.
- Revisione per possibile promozione a 50 trade indipendenti.
- PF minimo 1,50, expectancy e PnL positivi, drawdown massimo 15%, copertura minima 90%.
- PF deve superare la madre e il drawdown non deve essere peggiore sulla stessa serie di trade.
- La promozione resta una decisione umana protetta; il rollback viene predisposto soltanto in fase di approvazione.

# Blocco 4.5 — Crash Cascade Guard

Generato: 2026-07-23T01:08:33+00:00

> Paper-only. In mercato NORMAL/WATCH non riduce i segnali. Le limitazioni iniziano soltanto in STRESS, RECOVERY, CRASH, EXTREME o con dati non affidabili.

## Stato corrente

- Livello: **NORMAL**
- Direzione: **NONE**
- Segnali bloccati nel ciclo: **1**
- Simulazioni bloccate attive: **7**
- Simulazioni completate nel ciclo: **0**
- Liquidazioni virtuali evitate totali: **0**
- Valore cumulato del filtro: **14.14 R**
- Profitto virtuale mancato: **0.00 R**

## Stress test portafogli Paper

| Scenario | Posizioni interessate | Liquidazioni stimate | Perdita stimata EUR |
| --- | ---: | ---: | ---: |
| DOWN_10 | 116 | 0 | 18564.44 |
| DOWN_20 | 116 | 0 | 37128.88 |
| DOWN_30 | 116 | 0 | 55693.31 |
| DOWN_40 | 116 | 28 | 69715.68 |
| UP_10 | 34 | 0 | 5560.71 |
| UP_20 | 34 | 0 | 11121.42 |
| UP_30 | 34 | 0 | 16682.13 |
| UP_40 | 34 | 9 | 21354.20 |

## Modello di esecuzione

Se una candela di cascata attraversa nello stesso intervallo sia lo stop sia il prezzo di liquidazione, il Paper usa il caso peggiore e registra una liquidazione intrabar. Gli stop in gap o in regime di stress ricevono slippage aggiuntivo.

## Requisiti prima del live futures

- modalità ISOLATED obbligatoria;
- stop nativo sull'exchange;
- conferma dello stop prima di accettare la posizione;
- cross margin vietato.

# Blocco 5 — Candidati evolutivi controllati

Generato: 2026-07-23T01:08:12+00:00

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

Generato: 2026-07-23T01:08:49+00:00

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

Generato: 2026-07-23T01:08:49+00:00

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

Generato: 2026-07-23T01:08:49+00:00

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

Generato: 2026-07-23T01:08:49+00:00

> Paper-only. La memoria può bloccare soltanto una futura proposta Block 5 classificata AVOID; non modifica strategie esistenti.

## Stato

- Strategie/portafogli valutati: **76**
- Hall of Fame: **3**
- Memorie genetiche: **0**
- Firme bloccate: **0**
- Azioni automatiche e live: **0**

## Hall of Fame

| Rank | Strategia | Stato | Score | Grade | Trade | PF | Expectancy R | DD R |
| ---: | --- | --- | ---: | --- | ---: | ---: | ---: | ---: |
| 1 | SHADOW_1H_BALANCED | BASELINE | 13.4 | E | 31 | 1.35 | 0.137 | 3.70 |
| 2 | SHADOW_1H_FAST_V3 | BASELINE | 9.1 | E | 47 | 0.99 | -0.002 | 5.36 |
| 3 | SHADOW_1H_FAST | BASELINE | 5.6 | E | 54 | 0.84 | -0.080 | 12.39 |

## Memoria genetica

| Scope | Famiglia | Mutazione | Target | Stato | Score | Prove | Coppie | Blocco |
| --- | --- | --- | --- | --- | ---: | ---: | ---: | --- |
| — | — | Nessuna candidata ancora creata | — | INSUFFICIENT | 0 | 0 | 0 | NO |

## Sicurezza

- Nessuna strategia, posizione o promozione esistente viene modificata.
- Nessuna mutazione, promozione, pensionamento o rollback automatico.
- Nessun effetto live e nessun ordine reale.

# Blocco 10 — Regime Fitness e specializzazione

Generato: 2026-07-23T01:08:49+00:00

> Paper-only e advisory. Il blocco misura quali strategie funzionano nei diversi regimi, ma non cambia automaticamente strategia o posizione.

## Stato

- Regime corrente: **RANGE**
- Righe di performance: **284**
- Strategie preferite nel regime corrente: **0**
- Strategie da evitare nel regime corrente: **0**
- Memorie contestuali: **142**
- Routing automatico: **NO**

## Classifica del regime corrente

| Rank | Portafoglio | Famiglia | Stato | Fitness | Trade | PF | Expectancy R | DD R |
| ---: | --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| 1 | SHADOW_BTC_BOLLINGER_1H | shadow-btc-bollinger-1h | INSUFFICIENT | 80.8 | 2 | 99.00 | 0.997 | 0.00 |
| 2 | SHADOW_RSI_LONG_15X_10_RSI25 | shadow-rsi-long-15x-10-rsi25 | INSUFFICIENT | 80.8 | 2 | 99.00 | 0.984 | 0.00 |
| 3 | SHADOW_RSI_LONG_15X_50_RSI25 | shadow-rsi-long-15x-50-rsi25 | INSUFFICIENT | 80.8 | 2 | 99.00 | 0.984 | 0.00 |
| 4 | SHADOW_DOGE_DONCHIAN_1H | shadow-doge-donchian-1h | INSUFFICIENT | 80.4 | 1 | 99.00 | 0.524 | 0.00 |
| 5 | SHADOW_COMBO_ADAPTIVE | shadow-combo-adaptive | OBSERVING | 77.8 | 18 | 2.10 | 0.333 | 1.10 |
| 6 | SHADOW_ETH_BOLLINGER_1H | shadow-eth-bollinger-1h | INSUFFICIENT | 76.6 | 1 | 99.00 | 0.309 | 0.00 |
| 7 | SHADOW_SCANNER_TOP5_BTC | shadow-scanner-top5-btc | OBSERVING | 69.1 | 17 | 1.87 | 0.328 | 3.09 |
| 8 | SHADOW_RSI_LONG_5X_RSI25 | shadow-rsi-long-5x-rsi25 | INSUFFICIENT | 65.0 | 2 | 10.75 | 0.262 | 0.05 |
| 9 | SHADOW_SCANNER_TOP5_LONG | shadow-scanner-top5-long | OBSERVING | 63.4 | 20 | 1.70 | 0.300 | 4.17 |
| 10 | SHADOW_1H_BALANCED_V3 | shadow-1h-balanced-v3 | OBSERVING | 59.0 | 16 | 1.48 | 0.252 | 3.15 |

## Sicurezza

- Il regime viene assegnato usando solo l'ultimo record noto prima dell'entrata del trade.
- Nessun uso di dati futuri per classificare il trade.
- Il Candidate Regime Gate è advisory per impostazione predefinita.
- Nessun cambio automatico di MASTER, posizione o live.

# Blocco 11 — Collegamento protetto al live

Generato: 2026-07-23T01:08:49+00:00

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

Generato: 2026-07-23T01:08:33+00:00

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
