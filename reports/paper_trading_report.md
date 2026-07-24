# Paper trading automatico KuCoin

Generato: 2026-07-24T05:15:08+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-07-24T05:08:24+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-07-24T05:08:24+00:00 | 2026-07-24T05:08:24+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-07-24T04:45:00+00:00 | 2026-07-24T04:45:00+00:00 | 8,5 min | 25,0 min | OK |
| 60m | 12 | 2026-07-24T04:00:00+00:00 | 2026-07-24T04:00:00+00:00 | 8,5 min | 45,0 min | OK |
| 240m | 12 | 2026-07-24T00:00:00+00:00 | 2026-07-24T00:00:00+00:00 | 1,14 h | 1,00 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Master Adaptive Gb20 V1 | RIF | 60m | LONG | 4,75 | 0,00 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Master Adaptive Strict3 V1 | AKE | 60m | LONG | 6,25 | 0,00 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | AKE | 60m | LONG | 6,25 | 5,00 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top5 Btc Guard Mfe V1 | AKE | 60m | LONG | 6,25 | 5,00 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | AKE | 60m | LONG | 6,25 | 4,50 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Principale 4H | DOGE | 240m | SHORT | -8,73 | 6,00 | 0,00 | STALE_CANDLE | 1,14 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | AKE | 240m | LONG | 8,25 | 6,00 | 0,00 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | BANK | 240m | LONG | 7,75 | 6,00 | 0,00 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | HYPE | 240m | SHORT | -7,41 | 6,00 | 0,00 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | TAO | 240m | SHORT | -6,56 | 6,00 | 0,00 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | ZEC | 240m | SHORT | -3,73 | 6,00 | 2,27 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | SOL | 240m | SHORT | -3,01 | 6,00 | 2,99 | STALE_CANDLE | 1,14 h | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | PEPE | 240m | SHORT | -1,32 | 6,00 | 4,68 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | XRP | 240m | SHORT | -0,79 | 6,00 | 5,21 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | RIF | 240m | LONG | 0,75 | 6,00 | 5,25 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | ETH | 240m | SHORT | -0,73 | 6,00 | 5,27 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | BTC | 240m | LONG | 0,50 | 6,00 | 5,50 | STALE_CANDLE | 1,14 h | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| 1H Fast Score 6 75 V1 | AKE | 60m | LONG | 6,25 | 6,00 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Long Btc 1 3 Cap75 V1 | AKE | 60m | LONG | 6,25 | 4,50 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast No Pepe V1 | AKE | 60m | LONG | 6,25 | 4,50 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Tp2 V1 | AKE | 60m | LONG | 6,25 | 4,50 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 Nohigh V1 | AKE | 60m | LONG | 6,25 | 4,50 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 Long Only V1 | AKE | 60m | LONG | 6,25 | 4,50 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 Long Nohigh Cap75 V1 | AKE | 60m | LONG | 6,25 | 4,50 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 No Esports V1 | AKE | 60m | LONG | 6,25 | 4,50 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.952,25 | -0,48% | €-47,75 | €3.000,00 | -1,59% | 4 | 18 | 33,33% | 0,91 | 4,26% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 18 | 460 | CAMPIONE INSUFFICIENTE | 30 (mancano 12) |

- Trade del Principale 4H chiusi: **18**; win rate **33,33%**; profit factor **0,91**.
- Expectancy: **€-2,94** per trade; P&L netto: **€-52,87**; max drawdown: **4,26%**.
- Valutazione: **Servono altri eventi indipendenti prima di trarre conclusioni.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 4 | €9.952,25 | €1.462,87 | €4.388,60 | €148,39 | €7,17 |
| TEST | Scanner Top 5 Long 1H | 3 | €10.607,38 | €1.269,32 | €2.538,64 | €158,58 | €-18,90 |
| TEST | Scanner Top 5 + forza BTC 1H | 3 | €10.360,74 | €1.331,37 | €2.662,75 | €156,16 | €-18,46 |
| TEST | Bilanciata 1H V1 | 4 | €10.332,42 | €2.717,92 | €8.153,75 | €206,10 | €1,08 |
| TEST | Combo Adaptive | 3 | €10.272,71 | €2.803,92 | €5.607,85 | €154,09 | €13,16 |
| TEST | Bilanciata 1H V3 Filtered | 4 | €10.228,70 | €3.050,39 | €9.151,18 | €153,08 | €-10,21 |
| TEST | Forza relativa 1H V2 | 4 | €10.217,01 | €3.370,64 | €6.741,29 | €152,62 | €-48,99 |
| TEST | Benchmark Bollinger mean reversion 1H | 2 | €10.211,94 | €4.026,08 | €8.052,15 | €96,63 | €-15,89 |
| TEST | Benchmark Donchian breakout 1H | 2 | €10.188,40 | €2.359,86 | €4.719,72 | €51,18 | €15,62 |
| TEST | Doge Ema 1H | 1 | €10.153,18 | €1.173,45 | €3.520,36 | €50,69 | €17,05 |
| TEST | Combo Scanner | 3 | €10.130,66 | €2.818,85 | €5.637,69 | €150,23 | €16,98 |
| TEST | Scanner Top5 Btc Tp3 V1 | 3 | €10.121,94 | €1.281,05 | €2.562,10 | €150,77 | €-18,03 |
| TEST | 1H Fast Score 6 75 V1 | 4 | €10.104,01 | €4.406,51 | €13.219,54 | €202,09 | €-16,21 |
| TEST | Btc Bollinger 1H | 0 | €10.099,96 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Mean Reversion | 1 | €10.076,68 | €2.006,38 | €4.012,76 | €48,15 | €25,12 |
| TEST | Scanner Top5 Btc Runner25 V1 | 3 | €10.075,79 | €1.280,09 | €2.560,17 | €150,53 | €-17,95 |
| TEST | Rapida 1H V3 Filtered | 4 | €10.070,15 | €1.904,58 | €5.713,73 | €201,79 | €-96,80 |
| TEST | Sol Bollinger 4H | 1 | €10.064,57 | €968,56 | €1.937,11 | €0,00 | €66,22 |
| TEST | Bilanciata 1H V2 | 3 | €10.048,84 | €2.465,44 | €7.396,31 | €100,52 | €-33,09 |
| TEST | Combo Adaptive Quality7 V1 | 2 | €10.045,43 | €2.601,36 | €5.202,73 | €99,80 | €12,37 |
| TEST | Btc Bollinger 4H | 1 | €10.044,94 | €1.313,84 | €2.627,69 | €0,00 | €48,65 |
| TEST | Ampia 4H | 4 | €10.042,32 | €1.903,22 | €3.806,44 | €150,70 | €8,24 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €10.028,40 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Bollinger 1H | 0 | €10.015,45 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Donchian 1H | 1 | €10.010,18 | €1.095,98 | €3.287,94 | €49,99 | €14,98 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 0 | €10.005,68 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €50 · 15x | 0 | €10.002,52 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €10 · 15x | 0 | €10.000,50 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 4H | 1 | €10.000,43 | €1.105,63 | €2.211,26 | €50,00 | €-1,85 |
| TEST | Btc Donchian 4H | 1 | €10.000,43 | €1.105,63 | €2.211,26 | €50,00 | €-1,85 |
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
| TEST | Combo Adaptive Tp3 V1 | 3 | €9.997,66 | €2.844,67 | €5.689,33 | €149,61 | €5,83 |
| TEST | Scalp RSI Long 15 · €50 · 15x | 0 | €9.992,50 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Cap75 V1 | 4 | €9.990,51 | €4.929,03 | €14.787,09 | €200,21 | €-51,36 |
| TEST | Sol Donchian 1H | 1 | €9.988,65 | €1.301,74 | €3.905,22 | €49,99 | €-6,30 |
| TEST | Scalp RSI Long 15 · prudente · 5x | 0 | €9.988,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast No Pepe V1 | 4 | €9.983,77 | €1.858,48 | €5.575,44 | €199,68 | €-52,89 |
| TEST | Eth Donchian 1H | 0 | €9.982,54 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 0 | €9.980,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | 3 | €9.978,71 | €1.285,16 | €2.570,32 | €148,79 | €-17,78 |
| TEST | Btc Adaptive 4H | 1 | €9.975,31 | €1.047,40 | €2.094,81 | €50,00 | €-25,83 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.964,86 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Benchmark trend following EMA 1H | 3 | €9.959,43 | €2.803,05 | €5.606,10 | €99,49 | €16,87 |
| TEST | 1H Fast V3 No Esports V1 | 4 | €9.952,48 | €2.469,50 | €7.408,50 | €199,06 | €-44,11 |
| TEST | Btc Adaptive 1H | 1 | €9.951,60 | €1.156,05 | €3.468,15 | €49,94 | €-34,42 |
| TEST | Sol Donchian 4H | 1 | €9.951,10 | €830,21 | €1.660,43 | €49,74 | €4,08 |
| TEST | Sol Adaptive 4H | 1 | €9.951,01 | €761,04 | €1.522,08 | €49,74 | €3,74 |
| TEST | Scanner Top5 Btc Btc Le3 V1 | 3 | €9.950,53 | €1.300,19 | €2.600,39 | €149,91 | €-17,73 |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | 2 | €9.948,72 | €1.092,52 | €2.185,03 | €100,07 | €0,00 |
| TEST | Sol Ema 4H | 0 | €9.948,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Ema 4H | 0 | €9.947,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 1H | 1 | €9.946,82 | €1.381,14 | €4.143,42 | €49,72 | €5,03 |
| TEST | Combo Adaptive Regime V1 | 2 | €9.943,37 | €964,46 | €1.928,92 | €98,78 | €0,00 |
| TEST | 1H Fast Nohigh Cap75 V1 | 4 | €9.939,66 | €4.884,63 | €14.653,90 | €198,72 | €-50,97 |
| TEST | Forza relativa 1H V1 | 4 | €9.933,72 | €3.080,20 | €6.160,40 | €148,54 | €12,03 |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | 3 | €9.931,35 | €1.059,26 | €3.177,77 | €149,43 | €-22,37 |
| TEST | Sol Ema 1H | 1 | €9.929,64 | €1.150,16 | €3.450,47 | €49,69 | €-5,57 |
| TEST | 1H Fast V3 Nohigh V1 | 4 | €9.925,62 | €2.460,46 | €7.381,37 | €198,52 | €-43,99 |
| TEST | Doge Bollinger 1H | 1 | €9.920,47 | €1.381,14 | €4.143,42 | €49,72 | €-21,71 |
| TEST | Combo Adaptive Runner25 V1 | 3 | €9.917,53 | €2.840,61 | €5.681,22 | €149,40 | €-11,86 |
| TEST | Rapida 1H V2 | 2 | €9.910,39 | €2.348,51 | €7.045,53 | €99,77 | €-62,99 |
| TEST | Btc Donchian 1H | 1 | €9.909,41 | €1.293,96 | €3.881,87 | €49,69 | €-25,86 |
| TEST | Btc Ema 1H | 1 | €9.904,55 | €1.149,81 | €3.449,44 | €49,67 | €-27,74 |
| TEST | Sol Adaptive 1H | 1 | €9.902,86 | €1.149,09 | €3.447,26 | €49,64 | €-23,24 |
| TEST | Eth Adaptive 1H | 1 | €9.893,43 | €1.146,74 | €3.440,21 | €49,54 | €-12,29 |
| TEST | 1H Fast Tp2 V1 | 4 | €9.891,98 | €2.458,48 | €7.375,45 | €197,85 | €-43,84 |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | 1 | €9.889,70 | €864,27 | €1.728,54 | €49,61 | €0,00 |
| TEST | Combo Trend | 3 | €9.870,53 | €1.962,11 | €3.924,22 | €149,14 | €11,93 |
| TEST | Combo Adaptive Partial 1R V1 | 3 | €9.868,25 | €2.809,64 | €5.619,28 | €147,90 | €12,64 |
| TEST | Combo Adaptive Quality7 Regime V1 | 1 | €9.867,47 | €864,27 | €1.728,54 | €49,61 | €0,00 |
| TEST | Combo Adaptive Long Only V1 | 2 | €9.865,72 | €1.099,22 | €2.198,44 | €98,72 | €0,00 |
| TEST | Global Confluence puro 1H | 1 | €9.862,69 | €1.539,06 | €3.078,12 | €49,25 | €14,90 |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | 2 | €9.848,28 | €273,88 | €821,65 | €98,60 | €-22,19 |
| TEST | Rapida 1H V1 | 4 | €9.842,77 | €1.868,82 | €5.606,45 | €197,23 | €-94,33 |
| TEST | Eth Ema 1H | 1 | €9.821,01 | €1.138,34 | €3.415,02 | €49,18 | €-12,20 |
| TEST | Scanner Top5 Btc Guard V1 | 3 | €9.815,47 | €1.163,95 | €2.327,90 | €146,88 | €-17,49 |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | 2 | €9.813,03 | €272,90 | €818,71 | €98,24 | €-22,11 |
| TEST | 1H Fast V3 Long Only V1 | 2 | €9.808,76 | €272,78 | €818,35 | €98,20 | €-22,10 |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | 3 | €9.800,77 | €1.280,87 | €2.561,73 | €147,76 | €-32,41 |
| TEST | Scanner Bottom 5 Short 1H | 3 | €9.789,84 | €3.281,30 | €6.562,60 | €97,65 | €16,39 |
| TEST | Scanner Top5 Btc Mfe V1 | 3 | €9.761,21 | €2.553,52 | €5.107,05 | €148,96 | €-31,86 |
| TEST | Master Adaptive Expanded V1 | 3 | €9.758,85 | €1.240,15 | €2.480,31 | €146,90 | €-11,19 |
| TEST | Master Adaptive V1 | 3 | €9.719,68 | €1.239,48 | €2.478,96 | €146,74 | €-7,36 |
| TEST | Master Adaptive No Alt V1 | 3 | €9.719,68 | €1.239,48 | €2.478,96 | €146,74 | €-7,36 |
| TEST | Master Adaptive Runner25 V1 | 3 | €9.719,68 | €1.239,48 | €2.478,96 | €146,74 | €-7,36 |
| TEST | Scanner Top5 Btc Guard Mfe V1 | 3 | €9.689,50 | €1.161,78 | €2.323,56 | €146,36 | €-32,04 |
| TEST | Combo Adaptive Mfe Trail | 3 | €9.681,02 | €1.149,02 | €2.298,05 | €96,76 | €0,00 |
| TEST | Master Adaptive Gb20 V1 | 3 | €9.626,85 | €1.249,77 | €2.499,54 | €145,29 | €-14,86 |
| TEST | Master Adaptive Strict3 V1 | 3 | €9.563,19 | €1.286,20 | €2.572,41 | €144,82 | €-31,29 |

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
| PRINCIPALE | Principale 4H | Confluenza trend | €9.952,25 | €-52,87 | 18 | 18 | 33,33% | 0,91 | €-2,94 | 4,26% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.607,38 | €627,89 | 30 | 30 | 53,33% | 2,18 | €20,93 | 2,70% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €10.360,74 | €381,10 | 22 | 22 | 50,00% | 1,96 | €17,32 | 2,01% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €10.332,42 | €336,34 | 37 | 37 | 51,35% | 1,46 | €9,09 | 2,30% |
| TEST | Combo Adaptive | Combo Adaptive | €10.272,71 | €262,84 | 21 | 21 | 47,62% | 1,78 | €12,52 | 1,31% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €10.228,70 | €244,07 | 31 | 31 | 45,16% | 1,30 | €7,87 | 2,20% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €10.217,01 | €270,05 | 30 | 29 | 40,00% | 1,32 | €9,00 | 3,69% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €10.211,94 | €232,16 | 25 | 25 | 48,00% | 1,52 | €9,29 | 2,06% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €10.188,40 | €174,63 | 18 | 18 | 50,00% | 1,44 | €9,70 | 2,12% |
| TEST | Doge Ema 1H | Trend following EMA | €10.153,18 | €138,64 | 6 | 6 | 66,67% | 2,24 | €23,11 | 1,36% |
| TEST | Combo Scanner | Combo Scanner | €10.130,66 | €117,73 | 23 | 23 | 43,48% | 1,20 | €5,12 | 2,66% |
| TEST | Scanner Top5 Btc Tp3 V1 | Scanner Top 5 + forza BTC | €10.121,94 | €141,80 | 8 | 8 | 62,50% | 1,87 | €17,72 | 2,33% |
| TEST | 1H Fast Score 6 75 V1 | Momentum / breakout | €10.104,01 | €128,30 | 26 | 26 | 38,46% | 1,25 | €4,93 | 2,49% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.099,96 | €99,96 | 2 | 2 | 100,00% | ∞ | €49,98 | 0,31% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €10.076,68 | €54,00 | 12 | 12 | 41,67% | 1,16 | €4,50 | 2,31% |
| TEST | Scanner Top5 Btc Runner25 V1 | Scanner Top 5 + forza BTC | €10.075,79 | €95,56 | 8 | 8 | 62,50% | 1,59 | €11,95 | 2,33% |
| TEST | Rapida 1H V3 Filtered | Momentum / breakout V3 Filtered | €10.070,15 | €169,71 | 55 | 55 | 36,36% | 1,16 | €3,09 | 2,89% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €10.064,57 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,40% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €10.048,84 | €86,47 | 24 | 22 | 54,17% | 1,16 | €3,60 | 2,75% |
| TEST | Combo Adaptive Quality7 V1 | Combo Adaptive | €10.045,43 | €36,18 | 6 | 6 | 66,67% | 1,34 | €6,03 | 1,51% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.044,94 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,28% |
| TEST | Ampia 4H | Confluenza trend | €10.042,32 | €35,68 | 13 | 13 | 23,08% | 1,09 | €2,74 | 2,56% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €10.028,40 | €28,40 | 6 | 6 | 33,33% | 1,98 | €4,73 | 0,25% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €10.015,45 | €15,45 | 1 | 1 | 100,00% | ∞ | €15,45 | 0,51% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €10.010,18 | €-2,55 | 3 | 3 | 66,67% | 0,96 | €-0,85 | 0,96% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €10.005,68 | €5,68 | 6 | 6 | 33,33% | 1,98 | €0,95 | 0,05% |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | €10.002,52 | €2,52 | 4 | 4 | 50,00% | 1,22 | €0,63 | 0,11% |
| TEST | Scalp RSI Long 25 · €10 · 15x | Inversione RSI estrema 15m | €10.000,50 | €0,50 | 4 | 4 | 50,00% | 1,22 | €0,13 | 0,02% |
| TEST | Btc Ema 4H | Trend following EMA | €10.000,43 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,68% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €10.000,43 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,68% |
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
| TEST | Combo Adaptive Tp3 V1 | Combo Adaptive | €9.997,66 | €-4,53 | 9 | 9 | 55,56% | 0,98 | €-0,50 | 1,41% |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | €9.992,50 | €-7,50 | 1 | 1 | 0,00% | 0,00 | €-7,50 | 0,11% |
| TEST | 1H Fast V3 Cap75 V1 | Momentum / breakout V3 Filtered | €9.990,51 | €50,31 | 23 | 23 | 34,78% | 1,10 | €2,19 | 2,49% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €9.988,65 | €-2,63 | 2 | 2 | 50,00% | 0,41 | €-1,31 | 0,79% |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | €9.988,38 | €-11,62 | 1 | 1 | 0,00% | 0,00 | €-11,62 | 0,17% |
| TEST | 1H Fast No Pepe V1 | Momentum / breakout | €9.983,77 | €39,35 | 24 | 24 | 37,50% | 1,08 | €1,64 | 2,10% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.982,54 | €-17,46 | 3 | 3 | 33,33% | 0,84 | €-5,82 | 1,38% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €9.980,00 | €-20,00 | 4 | 4 | 25,00% | 0,22 | €-5,00 | 0,34% |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | Scanner Top 5 + forza BTC | €9.978,71 | €-1,60 | 4 | 4 | 50,00% | 0,99 | €-0,40 | 1,64% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €9.975,31 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,64% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.964,86 | €-35,14 | 6 | 6 | 16,67% | 0,18 | €-5,86 | 0,36% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.959,43 | €-54,01 | 16 | 16 | 31,25% | 0,87 | €-3,38 | 2,25% |
| TEST | 1H Fast V3 No Esports V1 | Momentum / breakout V3 Filtered | €9.952,48 | €0,63 | 28 | 28 | 32,14% | 1,00 | €0,02 | 2,49% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €9.951,60 | €-11,74 | 2 | 2 | 50,00% | 0,78 | €-5,87 | 0,89% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €9.951,10 | €-52,00 | 1 | 1 | 0,00% | 0,00 | €-52,00 | 0,60% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €9.951,01 | €-51,83 | 1 | 1 | 0,00% | 0,00 | €-51,83 | 0,59% |
| TEST | Scanner Top5 Btc Btc Le3 V1 | Scanner Top 5 + forza BTC | €9.950,53 | €-29,80 | 4 | 4 | 50,00% | 0,73 | €-7,45 | 2,20% |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | Scanner Top 5 + forza BTC | €9.948,72 | €-49,59 | 3 | 3 | 33,33% | 0,54 | €-16,53 | 2,22% |
| TEST | Sol Ema 4H | Trend following EMA | €9.948,00 | €-52,00 | 1 | 1 | 0,00% | 0,00 | €-52,00 | 0,56% |
| TEST | Eth Ema 4H | Trend following EMA | €9.947,12 | €-52,88 | 1 | 1 | 0,00% | 0,00 | €-52,88 | 0,68% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.946,82 | €-55,79 | 1 | 1 | 0,00% | 0,00 | €-55,79 | 0,81% |
| TEST | Combo Adaptive Regime V1 | Combo Adaptive | €9.943,37 | €-55,38 | 9 | 9 | 44,44% | 0,80 | €-6,15 | 2,18% |
| TEST | 1H Fast Nohigh Cap75 V1 | Momentum / breakout | €9.939,66 | €-1,00 | 28 | 28 | 35,71% | 1,00 | €-0,04 | 2,83% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €9.933,72 | €-74,62 | 23 | 23 | 26,09% | 0,83 | €-3,24 | 3,25% |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | Momentum / breakout | €9.931,35 | €-44,37 | 6 | 6 | 16,67% | 0,62 | €-7,40 | 1,55% |
| TEST | Sol Ema 1H | Trend following EMA | €9.929,64 | €-62,66 | 3 | 3 | 33,33% | 0,42 | €-20,89 | 1,67% |
| TEST | 1H Fast V3 Nohigh V1 | Momentum / breakout V3 Filtered | €9.925,62 | €-26,36 | 29 | 29 | 34,48% | 0,96 | €-0,91 | 2,96% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €9.920,47 | €-55,79 | 1 | 1 | 0,00% | 0,00 | €-55,79 | 0,93% |
| TEST | Combo Adaptive Runner25 V1 | Combo Adaptive | €9.917,53 | €-67,21 | 13 | 13 | 46,15% | 0,83 | €-5,17 | 2,12% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €9.910,39 | €-22,68 | 6 | 5 | 33,33% | 0,82 | €-3,78 | 1,69% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €9.909,41 | €-62,42 | 3 | 3 | 33,33% | 0,43 | €-20,81 | 1,49% |
| TEST | Btc Ema 1H | Trend following EMA | €9.904,55 | €-65,61 | 4 | 4 | 25,00% | 0,60 | €-16,40 | 1,56% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €9.902,86 | €-71,90 | 3 | 3 | 33,33% | 0,34 | €-23,97 | 1,85% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.893,43 | €-92,21 | 4 | 4 | 50,00% | 0,16 | €-23,05 | 1,11% |
| TEST | 1H Fast Tp2 V1 | Momentum / breakout | €9.891,98 | €-60,15 | 25 | 25 | 28,00% | 0,89 | €-2,41 | 2,58% |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | Combo Adaptive | €9.889,70 | €-109,26 | 4 | 4 | 25,00% | 0,32 | €-27,31 | 1,95% |
| TEST | Combo Trend | Combo Trend | €9.870,53 | €-139,04 | 25 | 25 | 28,00% | 0,82 | €-5,56 | 3,58% |
| TEST | Combo Adaptive Partial 1R V1 | Combo Adaptive | €9.868,25 | €-140,65 | 11 | 11 | 36,36% | 0,64 | €-12,79 | 2,24% |
| TEST | Combo Adaptive Quality7 Regime V1 | Combo Adaptive | €9.867,47 | €-131,50 | 4 | 4 | 25,00% | 0,18 | €-32,87 | 1,95% |
| TEST | Combo Adaptive Long Only V1 | Combo Adaptive | €9.865,72 | €-132,59 | 5 | 5 | 20,00% | 0,42 | €-26,52 | 2,34% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.862,69 | €-150,03 | 8 | 8 | 37,50% | 0,45 | €-18,75 | 2,92% |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | Momentum / breakout V3 Filtered | €9.848,28 | €-129,04 | 17 | 17 | 35,29% | 0,74 | €-7,59 | 2,77% |
| TEST | Rapida 1H V1 | Momentum / breakout | €9.842,77 | €-60,19 | 63 | 63 | 33,33% | 0,96 | €-0,96 | 6,76% |
| TEST | Eth Ema 1H | Trend following EMA | €9.821,01 | €-164,74 | 6 | 6 | 33,33% | 0,25 | €-27,46 | 1,79% |
| TEST | Scanner Top5 Btc Guard V1 | Scanner Top 5 + forza BTC | €9.815,47 | €-165,42 | 7 | 7 | 28,57% | 0,41 | €-23,63 | 3,31% |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | Momentum / breakout V3 Filtered | €9.813,03 | €-164,37 | 17 | 17 | 47,06% | 0,70 | €-9,67 | 3,16% |
| TEST | 1H Fast V3 Long Only V1 | Momentum / breakout V3 Filtered | €9.808,76 | €-168,65 | 22 | 22 | 27,27% | 0,72 | €-7,67 | 2,93% |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | Scanner Top 5 + forza BTC | €9.800,77 | €-165,28 | 11 | 11 | 36,36% | 0,50 | €-15,03 | 2,30% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.789,84 | €-222,24 | 22 | 22 | 31,82% | 0,61 | €-10,10 | 5,48% |
| TEST | Scanner Top5 Btc Mfe V1 | Scanner Top 5 + forza BTC | €9.761,21 | €-204,18 | 10 | 10 | 30,00% | 0,21 | €-20,42 | 3,30% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €9.758,85 | €-227,96 | 7 | 7 | 14,29% | 0,29 | €-32,57 | 2,80% |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | €9.719,68 | €-271,00 | 5 | 5 | 0,00% | 0,00 | €-54,20 | 3,19% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €9.719,68 | €-271,00 | 5 | 5 | 0,00% | 0,00 | €-54,20 | 3,19% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €9.719,68 | €-271,00 | 5 | 5 | 0,00% | 0,00 | €-54,20 | 3,19% |
| TEST | Scanner Top5 Btc Guard Mfe V1 | Scanner Top 5 + forza BTC | €9.689,50 | €-277,20 | 14 | 14 | 28,57% | 0,37 | €-19,80 | 3,47% |
| TEST | Combo Adaptive Mfe Trail | Combo Adaptive | €9.681,02 | €-317,53 | 27 | 27 | 25,93% | 0,45 | €-11,76 | 4,11% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €9.626,85 | €-356,79 | 27 | 27 | 51,85% | 0,44 | €-13,21 | 4,16% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €9.563,19 | €-403,98 | 12 | 12 | 16,67% | 0,32 | €-33,66 | 4,59% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | LAB | SHORT | Confluenza trend | 240m | 3,0x | 0,17841 | 0,17841 | 0,17841 | 0,23699 | 0,13559 | €136,26 | €408,77 | €0,00 | €-0,00 |
| Principale 4H | SUI | LONG | Confluenza trend | 240m | 3,0x | 0,76296 | 0,76296 | 0,73998 | 0,51245 | 0,80891 | €547,52 | €1.642,56 | €49,46 | €0,00 |
| Principale 4H | ONDO | LONG | Confluenza trend | 240m | 3,0x | 0,40344 | 0,40344 | 0,37762 | 0,27098 | 0,45509 | €254,70 | €764,09 | €48,91 | €0,00 |
| Principale 4H | DOGE | SHORT | Confluenza trend | 240m | 3,0x | 0,06940 | 0,06908 | 0,07160 | 0,09218 | 0,06498 | €524,39 | €1.573,18 | €50,01 | €7,17 |
| Bilanciata 1H V1 | ONDO | LONG | Confluenza trend | 60m | 3,0x | 0,39694 | 0,39694 | 0,38539 | 0,26661 | 0,42004 | €581,76 | €1.745,29 | €50,78 | €0,00 |
| Bilanciata 1H V1 | DOGE | SHORT | Confluenza trend | 60m | 3,0x | 0,06953 | 0,06908 | 0,07070 | 0,09235 | 0,06717 | €1.013,54 | €3.040,62 | €51,54 | €19,51 |
| Bilanciata 1H V1 | ADA | SHORT | Confluenza trend | 60m | 3,0x | 0,16703 | 0,16703 | 0,16999 | 0,22187 | 0,16112 | €978,72 | €2.936,17 | €51,97 | €-0,00 |
| Bilanciata 1H V1 | BANK | LONG | Confluenza trend | 60m | 3,0x | 0,26033 | 0,24922 | 0,22909 | 0,17486 | 0,32281 | €143,89 | €431,67 | €51,80 | €-18,43 |
| Bilanciata 1H V2 | ESPORTS | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,02164 | 0,02164 | 0,02164 | 0,02874 | 0,01644 | €138,69 | €416,06 | €0,00 | €-0,00 |
| Bilanciata 1H V2 | BTC | SHORT | Confluenza trend V2 | 60m | 3,0x | 64717,76386 | 65355,77000 | 65649,69966 | 85966,76299 | 62853,89226 | €1.163,40 | €3.490,20 | €50,26 | €-34,41 |
| Bilanciata 1H V2 | DOGE | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,06911 | 0,06908 | 0,07010 | 0,09180 | 0,06712 | €1.163,35 | €3.490,05 | €50,26 | €1,32 |
| Bilanciata 1H V3 Filtered | ESPORTS | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,02126 | 0,02126 | 0,02126 | 0,02823 | 0,01615 | €141,51 | €424,52 | €0,00 | €-0,00 |
| Bilanciata 1H V3 Filtered | ONDO | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,40134 | 0,40134 | 0,38898 | 0,26957 | 0,42605 | €557,59 | €1.672,77 | €51,50 | €0,00 |
| Bilanciata 1H V3 Filtered | BTC | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 64923,19276 | 65355,77000 | 65858,08674 | 86239,64105 | 63053,40481 | €1.167,13 | €3.501,39 | €50,42 | €-23,33 |
| Bilanciata 1H V3 Filtered | DOGE | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,06934 | 0,06908 | 0,07033 | 0,09210 | 0,06734 | €1.184,17 | €3.552,50 | €51,16 | €13,12 |
| Rapida 1H V1 | ONDO | LONG | Momentum / breakout | 60m | 3,0x | 0,39924 | 0,39924 | 0,38995 | 0,26816 | 0,41318 | €708,01 | €2.124,02 | €49,43 | €0,00 |
| Rapida 1H V1 | ZEC | SHORT | Momentum / breakout | 60m | 3,0x | 503,83921 | 510,32000 | 513,54273 | 669,26642 | 489,28394 | €857,19 | €2.571,57 | €49,53 | €-33,08 |
| Rapida 1H V1 | BANK | LONG | Momentum / breakout | 60m | 3,0x | 0,27032 | 0,24922 | 0,24378 | 0,18157 | 0,31014 | €168,54 | €505,62 | €49,65 | €-39,47 |
| Rapida 1H V1 | RIF | LONG | Momentum / breakout | 60m | 3,0x | 0,11756 | 0,11124 | 0,10346 | 0,07896 | 0,13872 | €135,08 | €405,23 | €48,63 | €-21,78 |
| 1H Fast Score 6 75 V1 | BTC | SHORT | Momentum / breakout | 60m | 3,0x | 65079,58148 | 65355,77000 | 65808,47279 | 86447,37740 | 63986,24451 | €1.483,09 | €4.449,28 | €49,83 | €-18,88 |
| 1H Fast Score 6 75 V1 | DOGE | SHORT | Momentum / breakout | 60m | 3,0x | 0,06953 | 0,06908 | 0,07044 | 0,09235 | 0,06815 | €1.281,83 | €3.845,50 | €50,70 | €24,67 |
| 1H Fast Score 6 75 V1 | TAO | SHORT | Momentum / breakout | 60m | 3,0x | 192,24458 | 193,18000 | 194,42319 | 255,36489 | 188,97667 | €1.501,26 | €4.503,79 | €51,04 | €-21,91 |
| 1H Fast Score 6 75 V1 | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00240 | 0,00240 | 0,00211 | 0,00161 | 0,00283 | €140,32 | €420,97 | €50,52 | €-0,08 |
| 1H Fast Nohigh Cap75 V1 | ONDO | LONG | Momentum / breakout | 60m | 3,0x | 0,39924 | 0,39924 | 0,38995 | 0,26816 | 0,41318 | €704,39 | €2.113,17 | €49,18 | €0,00 |
| 1H Fast Nohigh Cap75 V1 | BTC | SHORT | Momentum / breakout | 60m | 3,0x | 64923,19276 | 65355,77000 | 65650,33252 | 86239,64105 | 63832,48313 | €1.473,17 | €4.419,52 | €49,50 | €-29,45 |
| 1H Fast Nohigh Cap75 V1 | TAO | SHORT | Momentum / breakout | 60m | 3,0x | 192,24458 | 193,18000 | 194,42319 | 255,36489 | 188,97667 | €1.474,44 | €4.423,31 | €50,13 | €-21,52 |
| 1H Fast Nohigh Cap75 V1 | ADA | SHORT | Momentum / breakout | 60m | 3,0x | 0,16708 | 0,16708 | 0,16933 | 0,22194 | 0,16370 | €1.232,63 | €3.697,90 | €49,91 | €-0,00 |
| 1H Fast Long Btc 1 3 Cap75 V1 | ONDO | LONG | Momentum / breakout | 60m | 3,0x | 0,39694 | 0,39694 | 0,38849 | 0,26661 | 0,40961 | €783,06 | €2.349,19 | €50,00 | €0,00 |
| 1H Fast Long Btc 1 3 Cap75 V1 | RIF | LONG | Momentum / breakout | 60m | 3,0x | 0,11756 | 0,11124 | 0,10346 | 0,07896 | 0,13872 | €138,25 | €414,76 | €49,77 | €-22,29 |
| 1H Fast Long Btc 1 3 Cap75 V1 | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00240 | 0,00240 | 0,00211 | 0,00161 | 0,00283 | €137,94 | €413,82 | €49,66 | €-0,08 |
| 1H Fast No Pepe V1 | ONDO | LONG | Momentum / breakout | 60m | 3,0x | 0,39924 | 0,39924 | 0,38995 | 0,26816 | 0,41318 | €713,68 | €2.141,05 | €49,83 | €0,00 |
| 1H Fast No Pepe V1 | ZEC | SHORT | Momentum / breakout | 60m | 3,0x | 504,42909 | 510,32000 | 514,14397 | 670,04998 | 489,85678 | €867,81 | €2.603,42 | €50,14 | €-30,40 |
| 1H Fast No Pepe V1 | RIF | LONG | Momentum / breakout | 60m | 3,0x | 0,11756 | 0,11124 | 0,10346 | 0,07896 | 0,13872 | €138,96 | €416,88 | €50,03 | €-22,41 |
| 1H Fast No Pepe V1 | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00240 | 0,00240 | 0,00211 | 0,00161 | 0,00283 | €138,03 | €414,09 | €49,69 | €-0,08 |
| 1H Fast Tp2 V1 | ONDO | LONG | Momentum / breakout | 60m | 3,0x | 0,39924 | 0,39924 | 0,38995 | 0,26816 | 0,41782 | €712,92 | €2.138,77 | €49,77 | €0,00 |
| 1H Fast Tp2 V1 | TAO | SHORT | Momentum / breakout | 60m | 3,0x | 192,24458 | 193,18000 | 194,42319 | 255,36489 | 187,88737 | €1.473,39 | €4.420,17 | €50,09 | €-21,51 |
| 1H Fast Tp2 V1 | RIF | LONG | Momentum / breakout | 60m | 3,0x | 0,11756 | 0,11124 | 0,10346 | 0,07896 | 0,14578 | €138,00 | €414,01 | €49,68 | €-22,25 |
| 1H Fast Tp2 V1 | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00240 | 0,00240 | 0,00211 | 0,00161 | 0,00297 | €134,17 | €402,50 | €48,30 | €-0,08 |
| Rapida 1H V2 | BTC | SHORT | Momentum / breakout V2 | 60m | 3,0x | 64923,19276 | 65355,77000 | 65650,33252 | 86239,64105 | 63832,48313 | €1.485,87 | €4.457,60 | €49,93 | €-29,70 |
| Rapida 1H V2 | ZEC | SHORT | Momentum / breakout V2 | 60m | 3,0x | 503,83921 | 510,32000 | 513,54273 | 669,26642 | 489,28394 | €862,65 | €2.587,94 | €49,84 | €-33,29 |
| Rapida 1H V3 Filtered | ONDO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,39924 | 0,39924 | 0,38995 | 0,26816 | 0,41318 | €715,14 | €2.145,42 | €49,93 | €0,00 |
| Rapida 1H V3 Filtered | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 503,83921 | 510,32000 | 513,54273 | 669,26642 | 489,28394 | €877,00 | €2.631,00 | €50,67 | €-33,84 |
| Rapida 1H V3 Filtered | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,27032 | 0,24922 | 0,24378 | 0,18157 | 0,31014 | €172,44 | €517,32 | €50,80 | €-40,39 |
| Rapida 1H V3 Filtered | RIF | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,11756 | 0,11124 | 0,10346 | 0,07896 | 0,13872 | €140,00 | €419,99 | €50,40 | €-22,57 |
| 1H Fast V3 Cap75 V1 | ONDO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,39924 | 0,39924 | 0,38995 | 0,26816 | 0,41318 | €712,28 | €2.136,85 | €49,73 | €0,00 |
| 1H Fast V3 Cap75 V1 | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 64923,19276 | 65355,77000 | 65650,33252 | 86239,64105 | 63832,48313 | €1.484,27 | €4.452,81 | €49,87 | €-29,67 |
| 1H Fast V3 Cap75 V1 | TAO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 192,24458 | 193,18000 | 194,42319 | 255,36489 | 188,97667 | €1.485,79 | €4.457,37 | €50,51 | €-21,69 |
| 1H Fast V3 Cap75 V1 | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16732 | 0,16732 | 0,16956 | 0,22226 | 0,16396 | €1.246,68 | €3.740,05 | €50,10 | €-0,00 |
| 1H Fast V3 Nohigh V1 | ONDO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,39924 | 0,39924 | 0,38995 | 0,26816 | 0,41318 | €707,41 | €2.122,22 | €49,39 | €0,00 |
| 1H Fast V3 Nohigh V1 | TAO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 192,24458 | 193,18000 | 194,42319 | 255,36489 | 188,97667 | €1.478,41 | €4.435,24 | €50,26 | €-21,58 |
| 1H Fast V3 Nohigh V1 | RIF | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,11756 | 0,11124 | 0,10346 | 0,07896 | 0,13872 | €138,47 | €415,42 | €49,85 | €-22,33 |
| 1H Fast V3 Nohigh V1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00240 | 0,00240 | 0,00211 | 0,00161 | 0,00283 | €136,16 | €408,49 | €49,02 | €-0,08 |
| 1H Fast V3 Long Only V1 | RIF | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,11756 | 0,11124 | 0,10346 | 0,07896 | 0,13872 | €136,55 | €409,64 | €49,16 | €-22,02 |
| 1H Fast V3 Long Only V1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00240 | 0,00240 | 0,00211 | 0,00161 | 0,00283 | €136,24 | €408,71 | €49,05 | €-0,08 |
| 1H Fast V3 Long Nohigh Cap75 V1 | RIF | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,11756 | 0,11124 | 0,10346 | 0,07896 | 0,13872 | €137,10 | €411,29 | €49,35 | €-22,10 |
| 1H Fast V3 Long Nohigh Cap75 V1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00240 | 0,00240 | 0,00211 | 0,00161 | 0,00283 | €136,79 | €410,36 | €49,24 | €-0,08 |
| 1H Fast V3 No Esports V1 | ONDO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,39924 | 0,39924 | 0,38995 | 0,26816 | 0,41318 | €712,28 | €2.136,85 | €49,73 | €0,00 |
| 1H Fast V3 No Esports V1 | TAO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 192,24458 | 193,18000 | 194,42319 | 255,36489 | 188,97667 | €1.482,41 | €4.447,24 | €50,40 | €-21,64 |
| 1H Fast V3 No Esports V1 | RIF | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,11756 | 0,11124 | 0,10346 | 0,07896 | 0,13872 | €138,85 | €416,54 | €49,99 | €-22,39 |
| 1H Fast V3 No Esports V1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00240 | 0,00240 | 0,00211 | 0,00161 | 0,00283 | €135,96 | €407,87 | €48,94 | €-0,08 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | RIF | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,11756 | 0,11124 | 0,10346 | 0,07896 | 0,13872 | €136,61 | €409,82 | €49,18 | €-22,03 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00240 | 0,00240 | 0,00211 | 0,00161 | 0,00283 | €136,30 | €408,89 | €49,07 | €-0,08 |
| Ampia 4H | DOGE | SHORT | Confluenza trend | 240m | 2,0x | 0,07237 | 0,06908 | 0,07105 | 0,10819 | 0,06457 | €649,49 | €1.298,97 | €0,00 | €58,99 |
| Ampia 4H | ZEC | LONG | Confluenza trend | 240m | 2,0x | 522,36445 | 510,32000 | 483,09844 | 263,79405 | 632,30930 | €332,53 | €665,06 | €49,99 | €-15,33 |
| Ampia 4H | PEPE | LONG | Confluenza trend | 240m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €497,18 | €994,35 | €50,70 | €-32,62 |
| Ampia 4H | HYPE | SHORT | Confluenza trend | 240m | 2,0x | 58,36732 | 58,56000 | 61,80927 | 87,25915 | 48,72988 | €424,03 | €848,06 | €50,01 | €-2,80 |
| Forza relativa 1H V1 | ESPORTS | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,02126 | 0,02126 | 0,02126 | 0,03178 | 0,01564 | €208,05 | €416,10 | €0,00 | €-0,00 |
| Forza relativa 1H V1 | NIGHT | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,02031 | 0,02031 | 0,02210 | 0,03036 | 0,01637 | €285,91 | €571,83 | €50,45 | €-0,00 |
| Forza relativa 1H V1 | ONDO | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,42171 | €891,90 | €1.783,80 | €49,29 | €0,00 |
| Forza relativa 1H V1 | DOGE | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,06933 | 0,06908 | 0,07032 | 0,10364 | 0,06713 | €1.694,34 | €3.388,67 | €48,80 | €12,03 |
| Forza relativa 1H V2 | ESPORTS | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,02126 | 0,02126 | 0,02126 | 0,03178 | 0,01564 | €215,33 | €430,67 | €0,00 | €-0,00 |
| Forza relativa 1H V2 | BANK | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,27032 | 0,24922 | 0,23789 | 0,13651 | 0,34169 | €214,28 | €428,56 | €51,43 | €-33,46 |
| Forza relativa 1H V2 | HYPE | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 57,89642 | 58,56000 | 59,12372 | 86,55515 | 55,19635 | €1.212,96 | €2.425,92 | €51,43 | €-27,80 |
| Forza relativa 1H V2 | DOGE | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,06933 | 0,06908 | 0,07032 | 0,10364 | 0,06713 | €1.728,07 | €3.456,14 | €49,77 | €12,27 |
| Benchmark Donchian breakout 1H | SUI | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,76606 | 0,76606 | 0,75182 | 0,38686 | 0,80165 | €1.377,00 | €2.754,00 | €51,18 | €0,00 |
| Benchmark Donchian breakout 1H | ZEC | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 514,40710 | 510,32000 | 514,36486 | 769,03861 | 481,15276 | €982,86 | €1.965,73 | €0,00 | €15,62 |
| Benchmark Bollinger mean reversion 1H | DOGE | LONG | Bollinger mean reversion | 60m | 2,0x | 0,06944 | 0,06908 | 0,06861 | 0,03507 | 0,07069 | €2.013,01 | €4.026,02 | €48,31 | €-21,10 |
| Benchmark Bollinger mean reversion 1H | SOL | LONG | Bollinger mean reversion | 60m | 2,0x | 75,67913 | 75,77700 | 74,77098 | 38,21796 | 77,04136 | €2.013,07 | €4.026,14 | €48,31 | €5,21 |
| Benchmark trend following EMA 1H | LAB | LONG | Trend following EMA | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €207,05 | €414,10 | €49,69 | €0,00 |
| Benchmark trend following EMA 1H | HYPE | SHORT | Trend following EMA | 60m | 2,0x | 58,72425 | 58,56000 | 58,54319 | 87,79276 | 55,64481 | €1.039,97 | €2.079,94 | €0,00 | €5,82 |
| Benchmark trend following EMA 1H | DOGE | SHORT | Trend following EMA | 60m | 2,0x | 0,06933 | 0,06908 | 0,07044 | 0,10364 | 0,06689 | €1.556,03 | €3.112,05 | €49,79 | €11,05 |
| Scanner Top 5 Long 1H | ONDO | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,40114 | 0,40114 | 0,38834 | 0,20258 | 0,42673 | €828,91 | €1.657,82 | €52,88 | €0,00 |
| Scanner Top 5 Long 1H | LAB | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €219,03 | €438,05 | €52,57 | €0,00 |
| Scanner Top 5 Long 1H | BANK | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,26033 | 0,24922 | 0,22909 | 0,13147 | 0,32281 | €221,39 | €442,77 | €53,13 | €-18,90 |
| Scanner Bottom 5 Short 1H | ESPORTS | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,02150 | 0,02150 | 0,02150 | 0,03214 | 0,01634 | €207,40 | €414,80 | €0,00 | €-0,00 |
| Scanner Bottom 5 Short 1H | DOGE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,06942 | 0,06908 | 0,07042 | 0,10378 | 0,06742 | €1.692,83 | €3.385,67 | €48,75 | €16,39 |
| Scanner Bottom 5 Short 1H | ADA | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,16703 | 0,16703 | 0,16999 | 0,24971 | 0,16112 | €1.381,07 | €2.762,13 | €48,89 | €-0,00 |
| Scanner Top 5 + forza BTC 1H | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39694 | 0,39694 | 0,38539 | 0,20045 | 0,42235 | €898,57 | €1.797,15 | €52,29 | €0,00 |
| Scanner Top 5 + forza BTC 1H | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €216,56 | €433,12 | €51,97 | €0,00 |
| Scanner Top 5 + forza BTC 1H | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,26033 | 0,24922 | 0,22909 | 0,13147 | 0,32906 | €216,24 | €432,48 | €51,90 | €-18,46 |
| Scanner Top5 Btc Mfe V1 | SUI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,76776 | 0,76776 | 0,75508 | 0,38772 | 0,79565 | €1.514,04 | €3.028,08 | €50,00 | €0,00 |
| Scanner Top5 Btc Mfe V1 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39924 | 0,39924 | 0,38729 | 0,20162 | 0,42552 | €835,46 | €1.670,91 | €50,00 | €0,00 |
| Scanner Top5 Btc Mfe V1 | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,27032 | 0,24922 | 0,23789 | 0,13651 | 0,34169 | €204,03 | €408,05 | €48,97 | €-31,86 |
| Scanner Top5 Btc Guard V1 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39724 | 0,39724 | 0,38434 | 0,20061 | 0,42561 | €756,62 | €1.513,24 | €49,13 | €0,00 |
| Scanner Top5 Btc Guard V1 | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €202,47 | €404,95 | €48,59 | €0,00 |
| Scanner Top5 Btc Guard V1 | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,26033 | 0,24922 | 0,22909 | 0,13147 | 0,32906 | €204,86 | €409,72 | €49,17 | €-17,49 |
| Scanner Top5 Btc Btc Le3 V1 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39974 | 0,39974 | 0,38840 | 0,20187 | 0,42468 | €884,65 | €1.769,29 | €50,18 | €0,00 |
| Scanner Top5 Btc Btc Le3 V1 | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €207,87 | €415,74 | €49,89 | €0,00 |
| Scanner Top5 Btc Btc Le3 V1 | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,26033 | 0,24922 | 0,22909 | 0,13147 | 0,32906 | €207,68 | €415,35 | €49,84 | €-17,73 |
| Scanner Top5 Btc Btc 2 3 V1 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39974 | 0,39974 | 0,38840 | 0,20187 | 0,42468 | €884,65 | €1.769,29 | €50,18 | €0,00 |
| Scanner Top5 Btc Btc 2 3 V1 | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €207,87 | €415,74 | €49,89 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39724 | 0,39724 | 0,38434 | 0,20061 | 0,42561 | €756,62 | €1.513,24 | €49,13 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,27048 | 0,24922 | 0,23803 | 0,13659 | 0,34189 | €203,29 | €406,58 | €48,79 | €-31,96 |
| Scanner Top5 Btc Guard Mfe V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00240 | 0,00240 | 0,00211 | 0,00121 | 0,00303 | €201,87 | €403,74 | €48,45 | €-0,08 |
| Scanner Top5 Btc Guard Btc Le3 V1 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39974 | 0,39974 | 0,38840 | 0,20187 | 0,42468 | €871,05 | €1.742,11 | €49,41 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €205,84 | €411,68 | €49,40 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,26033 | 0,24922 | 0,22909 | 0,13147 | 0,32906 | €208,27 | €416,53 | €49,98 | €-17,78 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39974 | 0,39974 | 0,38840 | 0,20187 | 0,42468 | €871,05 | €1.742,11 | €49,41 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,27048 | 0,24922 | 0,23803 | 0,13659 | 0,34189 | €205,62 | €411,25 | €49,35 | €-32,33 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00240 | 0,00240 | 0,00211 | 0,00121 | 0,00303 | €204,19 | €408,38 | €49,01 | €-0,08 |
| Scanner Top5 Btc Runner25 V1 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39694 | 0,39694 | 0,38539 | 0,20045 | 0,43159 | €861,83 | €1.723,66 | €50,15 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,21338 | €207,96 | €415,92 | €49,91 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,26033 | 0,24922 | 0,22909 | 0,13147 | 0,35405 | €210,29 | €420,58 | €50,47 | €-17,95 |
| Scanner Top5 Btc Tp3 V1 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39694 | 0,39694 | 0,38539 | 0,20045 | 0,43159 | €861,83 | €1.723,66 | €50,15 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,21338 | €207,96 | €415,92 | €49,91 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,26033 | 0,24922 | 0,22909 | 0,13147 | 0,35405 | €211,25 | €422,51 | €50,70 | €-18,03 |
| Global Confluence puro 1H | DOGE | SHORT | Global Confluence puro | 60m | 2,0x | 0,06942 | 0,06908 | 0,07053 | 0,10378 | 0,06664 | €1.539,06 | €3.078,12 | €49,25 | €14,90 |
| Combo Trend | ESPORTS | SHORT | Combo Trend | 60m | 2,0x | 0,01883 | 0,01883 | 0,02109 | 0,02815 | 0,01386 | €209,57 | €419,14 | €50,30 | €-0,00 |
| Combo Trend | DOGE | SHORT | Combo Trend | 60m | 2,0x | 0,06929 | 0,06908 | 0,07039 | 0,10358 | 0,06685 | €1.546,95 | €3.093,91 | €49,50 | €9,20 |
| Combo Trend | BANK | LONG | Combo Trend | 60m | 2,0x | 0,24758 | 0,24922 | 0,21787 | 0,12503 | 0,31294 | €205,58 | €411,17 | €49,34 | €2,72 |
| Combo Mean Reversion | BTC | LONG | Combo Mean Reversion | 60m | 2,0x | 64949,16724 | 65355,77000 | 64169,77723 | 32799,32945 | 66196,19125 | €2.006,38 | €4.012,76 | €48,15 | €25,12 |
| Combo Scanner | ONDO | LONG | Combo Scanner | 60m | 2,0x | 0,39694 | 0,39694 | 0,38539 | 0,20045 | 0,42235 | €857,88 | €1.715,77 | €49,92 | €0,00 |
| Combo Scanner | LAB | LONG | Combo Scanner | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €207,54 | €415,08 | €49,81 | €0,00 |
| Combo Scanner | DOGE | SHORT | Combo Scanner | 60m | 2,0x | 0,06942 | 0,06908 | 0,07042 | 0,10378 | 0,06722 | €1.753,42 | €3.506,85 | €50,50 | €16,98 |
| Combo Adaptive | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,40114 | 0,40114 | 0,38834 | 0,20258 | 0,42673 | €809,25 | €1.618,50 | €51,63 | €0,00 |
| Combo Adaptive | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15861 | 0,13958 | 0,08010 | 0,19668 | €213,13 | €426,26 | €51,15 | €0,00 |
| Combo Adaptive | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,06934 | 0,06908 | 0,07033 | 0,10366 | 0,06734 | €1.781,54 | €3.563,09 | €51,31 | €13,16 |
| Combo Adaptive Mfe Trail | ESPORTS | SHORT | Combo Adaptive | 60m | 2,0x | 0,02156 | 0,02156 | 0,02091 | 0,03223 | 0,01638 | €202,62 | €405,24 | €0,00 | €-0,00 |
| Combo Adaptive Mfe Trail | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39784 | 0,39784 | 0,38492 | 0,20091 | 0,42367 | €744,71 | €1.489,41 | €48,35 | €0,00 |
| Combo Adaptive Mfe Trail | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15861 | 0,13958 | 0,08010 | 0,19668 | €201,70 | €403,39 | €48,41 | €0,00 |
| Combo Adaptive Quality7 V1 | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,40304 | 0,40304 | 0,39140 | 0,20354 | 0,42632 | €859,15 | €1.718,30 | €49,62 | €0,00 |
| Combo Adaptive Quality7 V1 | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,06933 | 0,06908 | 0,07032 | 0,10364 | 0,06733 | €1.742,21 | €3.484,43 | €50,18 | €12,37 |
| Combo Adaptive Regime V1 | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39724 | 0,39724 | 0,38434 | 0,20061 | 0,42303 | €757,94 | €1.515,88 | €49,21 | €0,00 |
| Combo Adaptive Regime V1 | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15861 | 0,13958 | 0,08010 | 0,19668 | €206,52 | €413,04 | €49,56 | €0,00 |
| Combo Adaptive Quality7 Regime V1 | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,40554 | 0,40554 | 0,39390 | 0,20480 | 0,42882 | €864,27 | €1.728,54 | €49,61 | €0,00 |
| Combo Adaptive Long Only V1 | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,41951 | €893,67 | €1.787,34 | €49,39 | €0,00 |
| Combo Adaptive Long Only V1 | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €205,55 | €411,10 | €49,33 | €0,00 |
| Combo Adaptive Partial 1R V1 | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,41951 | €893,02 | €1.786,04 | €49,36 | €0,00 |
| Combo Adaptive Partial 1R V1 | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €205,22 | €410,44 | €49,25 | €0,00 |
| Combo Adaptive Partial 1R V1 | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,06934 | 0,06908 | 0,07033 | 0,10366 | 0,06734 | €1.711,40 | €3.422,80 | €49,29 | €12,64 |
| Combo Adaptive Quality7 Regime Partial 1R V1 | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,40554 | 0,40554 | 0,39390 | 0,20480 | 0,42882 | €864,27 | €1.728,54 | €49,61 | €0,00 |
| Combo Adaptive Runner25 V1 | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,43050 | €902,18 | €1.804,37 | €49,86 | €0,00 |
| Combo Adaptive Runner25 V1 | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,06920 | 0,06908 | 0,07019 | 0,10345 | 0,06621 | €1.731,45 | €3.462,90 | €49,87 | €5,81 |
| Combo Adaptive Runner25 V1 | BANK | LONG | Combo Adaptive | 60m | 2,0x | 0,26033 | 0,24922 | 0,22909 | 0,13147 | 0,35405 | €206,98 | €413,96 | €49,67 | €-17,67 |
| Combo Adaptive Tp3 V1 | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,43050 | €902,18 | €1.804,37 | €49,86 | €0,00 |
| Combo Adaptive Tp3 V1 | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15861 | 0,13958 | 0,08010 | 0,21571 | €207,43 | €414,86 | €49,78 | €0,00 |
| Combo Adaptive Tp3 V1 | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,06920 | 0,06908 | 0,07019 | 0,10345 | 0,06621 | €1.735,05 | €3.470,11 | €49,97 | €5,83 |
| Btc Ema 1H | BTC | SHORT | Trend following EMA | 60m | 3,0x | 64834,39053 | 65355,77000 | 65768,00575 | 86121,68208 | 62967,16008 | €1.149,81 | €3.449,44 | €49,67 | €-27,74 |
| Btc Ema 4H | BTC | LONG | Trend following EMA | 240m | 2,0x | 65410,57950 | 65355,77000 | 63931,54687 | 33032,34265 | 69108,16107 | €1.105,63 | €2.211,26 | €50,00 | €-1,85 |
| Btc Donchian 1H | BTC | SHORT | Donchian breakout 20 barre | 60m | 3,0x | 64923,19276 | 65355,77000 | 65754,20963 | 86239,64105 | 63261,15903 | €1.293,96 | €3.881,87 | €49,69 | €-25,86 |
| Btc Donchian 4H | BTC | LONG | Donchian breakout 20 barre | 240m | 2,0x | 65410,57950 | 65355,77000 | 63931,54687 | 33032,34265 | 69551,87112 | €1.105,63 | €2.211,26 | €50,00 | €-1,85 |
| Btc Bollinger 4H | BTC | SHORT | Bollinger mean reversion | 240m | 2,0x | 66588,49964 | 65355,77000 | 65621,81812 | 99549,80696 | 64307,80290 | €1.313,84 | €2.627,69 | €0,00 | €48,65 |
| Btc Adaptive 1H | BTC | SHORT | Combo Adaptive | 60m | 3,0x | 64713,55470 | 65355,77000 | 65645,42989 | 85961,17183 | 62849,80432 | €1.156,05 | €3.468,15 | €49,94 | €-34,42 |
| Btc Adaptive 4H | BTC | LONG | Combo Adaptive | 240m | 2,0x | 66171,85172 | 65355,77000 | 64592,42491 | 33416,78512 | 70120,41876 | €1.047,40 | €2.094,81 | €50,00 | €-25,83 |
| Sol Ema 1H | SOL | SHORT | Trend following EMA | 60m | 3,0x | 75,65487 | 75,77700 | 76,74430 | 100,49488 | 73,47601 | €1.150,16 | €3.450,47 | €49,69 | €-5,57 |
| Sol Donchian 1H | SOL | SHORT | Donchian breakout 20 barre | 60m | 3,0x | 75,65487 | 75,77700 | 76,62325 | 100,49488 | 73,71810 | €1.301,74 | €3.905,22 | €49,99 | €-6,30 |
| Sol Donchian 4H | SOL | SHORT | Donchian breakout 20 barre | 240m | 2,0x | 75,96380 | 75,77700 | 78,23939 | 113,56589 | 69,59218 | €830,21 | €1.660,43 | €49,74 | €4,08 |
| Sol Bollinger 1H | SOL | LONG | Bollinger mean reversion | 60m | 3,0x | 75,68513 | 75,77700 | 74,77691 | 50,83518 | 77,04747 | €1.381,14 | €4.143,42 | €49,72 | €5,03 |
| Sol Bollinger 4H | SOL | SHORT | Bollinger mean reversion | 240m | 2,0x | 78,45931 | 75,77700 | 76,84028 | 117,29666 | 74,81402 | €968,56 | €1.937,11 | €0,00 | €66,22 |
| Sol Adaptive 1H | SOL | LONG | Combo Adaptive | 60m | 3,0x | 76,29126 | 75,77700 | 75,19266 | 51,24229 | 78,48844 | €1.149,09 | €3.447,26 | €49,64 | €-23,24 |
| Sol Adaptive 4H | SOL | SHORT | Combo Adaptive | 240m | 2,0x | 75,96380 | 75,77700 | 78,44626 | 113,56589 | 69,75767 | €761,04 | €1.522,08 | €49,74 | €3,74 |
| Eth Ema 1H | ETH | SHORT | Trend following EMA | 60m | 3,0x | 1873,22528 | 1879,92000 | 1900,19972 | 2488,26758 | 1819,27639 | €1.138,34 | €3.415,02 | €49,18 | €-12,20 |
| Eth Adaptive 1H | ETH | SHORT | Combo Adaptive | 60m | 3,0x | 1873,22528 | 1879,92000 | 1900,19972 | 2488,26758 | 1819,27639 | €1.146,74 | €3.440,21 | €49,54 | €-12,29 |
| Doge Ema 1H | DOGE | SHORT | Trend following EMA | 60m | 3,0x | 0,06942 | 0,06908 | 0,07042 | 0,09221 | 0,06742 | €1.173,45 | €3.520,36 | €50,69 | €17,05 |
| Doge Donchian 1H | DOGE | SHORT | Donchian breakout 20 barre | 60m | 3,0x | 0,06940 | 0,06908 | 0,07045 | 0,09218 | 0,06729 | €1.095,98 | €3.287,94 | €49,99 | €14,98 |
| Doge Bollinger 1H | DOGE | LONG | Bollinger mean reversion | 60m | 3,0x | 0,06944 | 0,06908 | 0,06861 | 0,04664 | 0,07069 | €1.381,14 | €4.143,42 | €49,72 | €-21,71 |
| Master Adaptive V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39854 | 0,39854 | 0,38677 | 0,20126 | 0,42207 | €833,00 | €1.665,99 | €49,19 | €0,00 |
| Master Adaptive V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €203,80 | €407,60 | €48,91 | €0,00 |
| Master Adaptive V1 | BANK | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,25383 | 0,24922 | 0,22337 | 0,12818 | 0,31475 | €202,68 | €405,37 | €48,64 | €-7,36 |
| Master Adaptive No Alt V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39854 | 0,39854 | 0,38677 | 0,20126 | 0,42207 | €833,00 | €1.665,99 | €49,19 | €0,00 |
| Master Adaptive No Alt V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €203,80 | €407,60 | €48,91 | €0,00 |
| Master Adaptive No Alt V1 | BANK | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,25383 | 0,24922 | 0,22337 | 0,12818 | 0,31475 | €202,68 | €405,37 | €48,64 | €-7,36 |
| Master Adaptive Strict3 V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,41951 | €887,07 | €1.774,14 | €49,03 | €0,00 |
| Master Adaptive Strict3 V1 | BANK | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,27032 | 0,24922 | 0,23789 | 0,13651 | 0,33520 | €199,89 | €399,79 | €47,97 | €-31,21 |
| Master Adaptive Strict3 V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00240 | 0,00240 | 0,00211 | 0,00121 | 0,00297 | €199,24 | €398,48 | €47,82 | €-0,08 |
| Master Adaptive Expanded V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39854 | 0,39854 | 0,38677 | 0,20126 | 0,42207 | €833,00 | €1.665,99 | €49,19 | €0,00 |
| Master Adaptive Expanded V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €203,80 | €407,60 | €48,91 | €0,00 |
| Master Adaptive Expanded V1 | BANK | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,25627 | 0,24922 | 0,22552 | 0,12942 | 0,31778 | €203,36 | €406,71 | €48,81 | €-11,19 |
| Master Adaptive Gb20 V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,40304 | 0,40304 | 0,39140 | 0,20354 | 0,42632 | €848,64 | €1.697,27 | €49,02 | €0,00 |
| Master Adaptive Gb20 V1 | BANK | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,25875 | 0,24922 | 0,22770 | 0,13067 | 0,32085 | €200,57 | €401,14 | €48,14 | €-14,78 |
| Master Adaptive Gb20 V1 | RIF | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,11127 | 0,11124 | 0,09792 | 0,05619 | 0,13797 | €200,57 | €401,13 | €48,14 | €-0,08 |
| Master Adaptive Runner25 V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39854 | 0,39854 | 0,38677 | 0,20126 | 0,43384 | €833,00 | €1.665,99 | €49,19 | €0,00 |
| Master Adaptive Runner25 V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,21338 | €203,80 | €407,60 | €48,91 | €0,00 |
| Master Adaptive Runner25 V1 | BANK | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,25383 | 0,24922 | 0,22337 | 0,12818 | 0,34521 | €202,68 | €405,37 | €48,64 | €-7,36 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Master Adaptive Gb20 V1 | RIF | LONG | 2026-07-24T04:38:35+00:00 | 0,11359 | €22,95 | 0,48 | STOP_STRESS_SLIPPAGE |
| Combo Trend | BANK | LONG | 2026-07-24T04:08:34+00:00 | 0,24375 | €-51,35 | -1,03 | STOP_STRESS_SLIPPAGE |
| 1H Fast No Pepe V1 | BANK | LONG | 2026-07-24T04:08:34+00:00 | 0,24420 | €-53,07 | -1,05 | STOP_STRESS_SLIPPAGE |
| Benchmark Donchian breakout 1H | HYPE | SHORT | 2026-07-24T03:53:33+00:00 | 58,38314 | €17,07 | 0,34 | STOP |
| 1H Fast V3 No Esports V1 | BANK | LONG | 2026-07-24T03:53:33+00:00 | 0,25715 | €-7,20 | -0,14 | STOP_STRESS_SLIPPAGE |
| 1H Fast V3 Nohigh V1 | BANK | LONG | 2026-07-24T03:53:33+00:00 | 0,25715 | €-7,18 | -0,14 | STOP_STRESS_SLIPPAGE |
| 1H Fast V3 Long Only V1 | BANK | LONG | 2026-07-24T03:53:33+00:00 | 0,25715 | €-7,07 | -0,14 | STOP_STRESS_SLIPPAGE |
| 1H Fast Tp2 V1 | BANK | LONG | 2026-07-24T03:53:33+00:00 | 0,25715 | €-7,16 | -0,14 | STOP_STRESS_SLIPPAGE |
| Forza relativa 1H V2 | ZEC | SHORT | 2026-07-24T03:38:34+00:00 | 510,60730 | €6,59 | 0,13 | STOP |
| Forza relativa 1H V1 | ZEC | SHORT | 2026-07-24T03:38:34+00:00 | 511,01998 | €-2,04 | -0,04 | STOP |
| Benchmark trend following EMA 1H | ZEC | SHORT | 2026-07-24T03:38:34+00:00 | 511,54998 | €-1,87 | -0,04 | STOP |
| 1H Fast V3 No Esports V1 | DOGE | SHORT | 2026-07-24T03:38:34+00:00 | 0,06943 | €-6,71 | -0,13 | STOP |

## Regole invarianti

- Nessuna martingala e nessuna mediazione automatica in perdita.
- Il target mensile riduce il rischio quando viene avvicinato o raggiunto; non lo aumenta mai.
- Il portafoglio principale e le simulazioni di confronto hanno contabilità separata.
- Commissioni, slippage e funding sono inclusi nella simulazione secondo i parametri configurati.
- Quando stop e target risultano toccati nella stessa candela, prevale lo stop salvo modifica esplicita della configurazione.
