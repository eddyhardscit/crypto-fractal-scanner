# Paper trading automatico KuCoin

Generato: 2026-07-24T11:03:19+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-07-24T11:02:47+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-07-24T11:02:47+00:00 | 2026-07-24T11:02:47+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-07-24T10:45:00+00:00 | 2026-07-24T10:45:00+00:00 | 2,9 min | 25,0 min | OK |
| 60m | 12 | 2026-07-24T10:00:00+00:00 | 2026-07-24T10:00:00+00:00 | 2,9 min | 45,0 min | OK |
| 240m | 12 | 2026-07-24T04:00:00+00:00 | 2026-07-24T04:00:00+00:00 | 3,05 h | 1,00 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Master Adaptive Strict3 V1 | BANK | 60m | LONG | 7,75 | 0,00 | 0,00 | OPENED | 2,9 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive — Quality7 + Regime + parziale 1R | AKE | 60m | LONG | 7,75 | 7,00 | 0,00 | OPENED | 2,9 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive — Quality7 + Regime | AKE | 60m | LONG | 7,75 | 7,00 | 0,00 | OPENED | 2,9 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive — Trend/Transition | DOGE | 60m | SHORT | -6,78 | 5,00 | 0,00 | OPENED | 2,9 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive — Quality7 | AKE | 60m | LONG | 7,75 | 7,00 | 0,00 | OPENED | 2,9 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Top 5 + BTC — Guard + BTC≤3 + MFE | BANK | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 2,9 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Top 5 + BTC — Guard + BTC≤3 + MFE | AKE | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 2,9 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Top 5 + BTC — Guard + MFE | BANK | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 2,9 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Top 5 + BTC — Guard + MFE | AKE | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 2,9 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Top 5 + BTC — BTC 2–3 | AKE | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 2,9 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Top 5 + BTC — solo MFE | AKE | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 2,9 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V3 — senza ESPORTS | BANK | 60m | LONG | 7,75 | 4,50 | 0,00 | OPENED | 2,9 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V3 — no volatilità HIGH | BANK | 60m | LONG | 7,75 | 4,50 | 0,00 | OPENED | 2,9 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida 1H V3 Filtered — madre | BANK | 60m | LONG | 7,75 | 4,50 | 0,00 | OPENED | 2,9 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V1 — target pieno 2R | BANK | 60m | LONG | 7,75 | 4,50 | 0,00 | OPENED | 2,9 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V1 — senza PEPE | BANK | 60m | LONG | 7,75 | 4,50 | 0,00 | OPENED | 2,9 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida 1H V1 — madre | BANK | 60m | LONG | 7,75 | 4,50 | 0,00 | OPENED | 2,9 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Principale 4H | DOGE | 240m | SHORT | -8,77 | 6,00 | 0,00 | STALE_CANDLE | 3,05 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 182.9 minuti; tolleranza 60 minuti. |
| Principale 4H | AKE | 240m | LONG | 8,25 | 6,00 | 0,00 | STALE_CANDLE | 3,05 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 182.9 minuti; tolleranza 60 minuti. |
| Principale 4H | BANK | 240m | LONG | 7,75 | 6,00 | 0,00 | STALE_CANDLE | 3,05 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 182.9 minuti; tolleranza 60 minuti. |
| Principale 4H | HYPE | 240m | SHORT | -5,99 | 6,00 | 0,01 | STALE_CANDLE | 3,05 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 182.9 minuti; tolleranza 60 minuti. |
| Principale 4H | SOL | 240m | SHORT | -4,99 | 6,00 | 1,01 | STALE_CANDLE | 3,05 h | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 182.9 minuti; tolleranza 60 minuti. |
| Principale 4H | ZEC | 240m | SHORT | -3,77 | 6,00 | 2,23 | STALE_CANDLE | 3,05 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 182.9 minuti; tolleranza 60 minuti. |
| Principale 4H | BTC | 240m | LONG | 2,50 | 6,00 | 3,50 | STALE_CANDLE | 3,05 h | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 182.9 minuti; tolleranza 60 minuti. |
| Principale 4H | ETH | 240m | LONG | 0,93 | 6,00 | 5,07 | STALE_CANDLE | 3,05 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 182.9 minuti; tolleranza 60 minuti. |
| Principale 4H | XRP | 240m | LONG | 0,77 | 6,00 | 5,23 | STALE_CANDLE | 3,05 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 182.9 minuti; tolleranza 60 minuti. |
| Principale 4H | RIF | 240m | LONG | 0,75 | 6,00 | 5,25 | STALE_CANDLE | 3,05 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 182.9 minuti; tolleranza 60 minuti. |
| Principale 4H | PEPE | 240m | SHORT | -0,29 | 6,00 | 5,71 | STALE_CANDLE | 3,05 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 182.9 minuti; tolleranza 60 minuti. |
| Principale 4H | ADA | 240m | LONG | 0,22 | 6,00 | 5,78 | STALE_CANDLE | 3,05 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 182.9 minuti; tolleranza 60 minuti. |
| Bilanciata 1H V2 | AKE | 60m | LONG | 7,75 | 5,50 | 0,00 | OPENED | 2,9 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida 1H V1 — madre | AKE | 60m | LONG | 7,75 | 4,50 | 0,00 | OPENED | 2,9 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V1 — senza PEPE | AKE | 60m | LONG | 7,75 | 4,50 | 0,00 | OPENED | 2,9 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V1 — target pieno 2R | AKE | 60m | LONG | 7,75 | 4,50 | 0,00 | OPENED | 2,9 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida 1H V3 Filtered — madre | AKE | 60m | LONG | 7,75 | 4,50 | 0,00 | OPENED | 2,9 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V3 — no volatilità HIGH | AKE | 60m | LONG | 7,75 | 4,50 | 0,00 | OPENED | 2,9 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V3 — senza ESPORTS | AKE | 60m | LONG | 7,75 | 4,50 | 0,00 | OPENED | 2,9 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Forza relativa 1H V2 | AKE | 60m | LONG | 7,75 | 5,50 | 0,00 | OPENED | 2,9 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.935,59 | -0,64% | €-64,41 | €3.000,00 | -2,15% | 4 | 18 | 33,33% | 0,91 | 4,26% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 18 | 466 | CAMPIONE INSUFFICIENTE | 30 (mancano 12) |

- Trade del Principale 4H chiusi: **18**; win rate **33,33%**; profit factor **0,91**.
- Expectancy: **€-2,94** per trade; P&L netto: **€-52,87**; max drawdown: **4,26%**.
- Valutazione: **Servono altri eventi indipendenti prima di trarre conclusioni.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 4 | €9.935,59 | €1.462,87 | €4.388,60 | €148,39 | €-9,61 |
| TEST | Scanner Top 5 Long 1H | 3 | €10.688,03 | €1.269,32 | €2.538,64 | €105,45 | €61,77 |
| TEST | Scanner Top 5 + forza BTC 1H | 3 | €10.439,51 | €1.331,37 | €2.662,75 | €104,27 | €60,33 |
| TEST | Bilanciata 1H V1 | 4 | €10.390,52 | €2.717,92 | €8.153,75 | €154,30 | €59,49 |
| TEST | Combo Adaptive — madre | 3 | €10.234,95 | €2.803,92 | €5.607,85 | €154,09 | €-24,87 |
| TEST | Benchmark Bollinger mean reversion 1H | 2 | €10.234,09 | €4.026,08 | €8.052,15 | €96,63 | €6,80 |
| TEST | Benchmark Donchian breakout 1H | 2 | €10.229,60 | €2.359,86 | €4.719,72 | €51,18 | €56,62 |
| TEST | Bilanciata 1H V3 Filtered | 4 | €10.215,10 | €3.050,39 | €9.151,18 | €153,08 | €-23,92 |
| TEST | Top 5 + BTC — target pieno 3R | 3 | €10.198,90 | €1.281,05 | €2.562,10 | €100,06 | €58,94 |
| TEST | Forza relativa 1H V2 | 4 | €10.160,48 | €3.366,12 | €6.732,25 | €151,54 | €-45,97 |
| TEST | Top 5 + BTC — 75% a 2,2R + runner 3R | 3 | €10.152,39 | €1.280,09 | €2.560,17 | €100,06 | €58,67 |
| TEST | Doge Ema 1H | 1 | €10.115,91 | €1.173,45 | €3.520,36 | €50,69 | €-20,48 |
| TEST | Rapida V1 — score 6–7,5 | 3 | €10.103,12 | €4.266,19 | €12.798,57 | €151,57 | €-4,46 |
| TEST | Btc Bollinger 1H | 0 | €10.099,96 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Scanner | 3 | €10.093,54 | €2.818,85 | €5.637,69 | €150,23 | €-20,40 |
| TEST | Sol Bollinger 4H | 1 | €10.074,06 | €968,56 | €1.937,11 | €0,00 | €75,61 |
| TEST | Rapida V3 — score <7,5 | 4 | €10.064,67 | €4.929,03 | €14.787,09 | €200,21 | €23,00 |
| TEST | Btc Bollinger 4H | 1 | €10.062,50 | €1.313,84 | €2.627,69 | €0,00 | €66,35 |
| TEST | Top 5 + BTC — Guard + BTC≤3 | 3 | €10.054,57 | €1.285,16 | €2.570,32 | €98,81 | €58,11 |
| TEST | Rapida 1H V3 Filtered — madre | 4 | €10.050,62 | €1.901,42 | €5.704,26 | €201,02 | €22,00 |
| TEST | Combo Mean Reversion | 1 | €10.049,13 | €2.006,38 | €4.012,76 | €48,15 | €-2,60 |
| TEST | Bilanciata 1H V2 | 4 | €10.035,14 | €2.604,82 | €7.814,46 | €150,69 | €-46,34 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €10.028,40 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Top 5 + BTC — BTC≤3 | 3 | €10.026,18 | €1.300,19 | €2.600,39 | €100,07 | €57,94 |
| TEST | Eth Bollinger 1H | 0 | €10.015,45 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Ampia 4H | 4 | €10.015,43 | €1.903,22 | €3.806,44 | €150,70 | €-18,69 |
| TEST | Sol Donchian 1H | 1 | €10.008,50 | €1.301,74 | €3.905,22 | €49,99 | €13,31 |
| TEST | Combo Adaptive — Quality7 | 3 | €10.007,91 | €2.809,87 | €5.619,74 | €149,84 | €-24,91 |
| TEST | Rapida V1 — no HIGH + score <7,5 | 4 | €10.007,26 | €4.884,63 | €14.653,90 | €198,72 | €17,47 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 0 | €10.005,68 | €0,00 | €0,00 | €0,00 | €0,00 |
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
| TEST | Rapida V1 — senza PEPE | 4 | €9.998,04 | €1.889,45 | €5.668,35 | €199,95 | €24,79 |
| TEST | Rapida 1H V2 | 2 | €9.996,12 | €2.348,51 | €7.045,53 | €99,77 | €22,93 |
| TEST | Scalp RSI Long 15 · €50 · 15x | 0 | €9.992,50 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · prudente · 5x | 0 | €9.988,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 4H | 1 | €9.985,39 | €1.105,63 | €2.211,26 | €50,00 | €-17,02 |
| TEST | Btc Donchian 4H | 1 | €9.985,39 | €1.105,63 | €2.211,26 | €50,00 | €-17,02 |
| TEST | Eth Donchian 1H | 0 | €9.982,54 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 0 | €9.980,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 1H | 1 | €9.975,45 | €1.156,05 | €3.468,15 | €49,94 | €-10,37 |
| TEST | Doge Donchian 1H | 1 | €9.975,36 | €1.095,98 | €3.287,94 | €49,99 | €-20,08 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.964,86 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Bollinger 1H | 1 | €9.964,31 | €1.381,14 | €4.143,42 | €49,72 | €22,44 |
| TEST | Btc Adaptive 4H | 1 | €9.961,22 | €1.047,40 | €2.094,81 | €50,00 | €-40,04 |
| TEST | Combo Adaptive — target pieno 3R | 3 | €9.960,81 | €2.844,67 | €5.689,33 | €149,61 | €-31,28 |
| TEST | Sol Donchian 4H | 1 | €9.959,40 | €830,21 | €1.660,43 | €49,74 | €12,39 |
| TEST | Sol Adaptive 4H | 1 | €9.958,62 | €761,04 | €1.522,08 | €49,74 | €11,36 |
| TEST | Combo Adaptive — 75% a 2R + runner 3R | 3 | €9.956,15 | €2.840,61 | €5.681,22 | €99,73 | €26,53 |
| TEST | Top 5 + BTC — BTC 2–3 | 3 | €9.948,39 | €1.299,78 | €2.599,56 | €149,81 | €-0,08 |
| TEST | Sol Ema 4H | 0 | €9.948,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 1H | 1 | €9.947,17 | €1.150,16 | €3.450,47 | €49,69 | €11,76 |
| TEST | Eth Ema 4H | 0 | €9.947,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — Trend/Transition | 3 | €9.940,61 | €2.690,74 | €5.381,48 | €148,49 | €-0,69 |
| TEST | Btc Donchian 1H | 1 | €9.936,07 | €1.293,96 | €3.881,87 | €49,69 | €0,96 |
| TEST | Rapida V3 — senza ESPORTS | 4 | €9.933,22 | €2.498,02 | €7.494,07 | €198,67 | €-0,18 |
| TEST | Btc Ema 1H | 1 | €9.928,22 | €1.149,81 | €3.449,44 | €49,67 | €-3,87 |
| TEST | Sol Bollinger 1H | 1 | €9.925,78 | €1.381,14 | €4.143,42 | €49,72 | €-15,77 |
| TEST | Benchmark trend following EMA 1H | 3 | €9.921,86 | €3.318,79 | €6.637,59 | €149,27 | €-23,59 |
| TEST | Combo Trend | 3 | €9.916,26 | €1.962,11 | €3.924,22 | €99,80 | €57,66 |
| TEST | Rapida V3 — no volatilità HIGH | 4 | €9.906,36 | €2.489,01 | €7.467,03 | €198,14 | €-0,18 |
| TEST | Forza relativa 1H V1 | 4 | €9.897,55 | €3.080,20 | €6.160,40 | €148,54 | €-24,14 |
| TEST | Eth Adaptive 1H | 1 | €9.891,55 | €1.146,74 | €3.440,21 | €49,54 | €-14,19 |
| TEST | Rapida V1 — Long + BTC 1–3 + score <7,5 | 1 | €9.891,12 | €783,06 | €2.349,19 | €50,00 | €0,00 |
| TEST | Top 5 + BTC — Guard | 3 | €9.890,09 | €1.163,95 | €2.327,90 | €97,72 | €57,16 |
| TEST | Combo Adaptive — Quality7 + Regime + parziale 1R | 2 | €9.889,37 | €1.070,31 | €2.140,61 | €99,06 | €-0,08 |
| TEST | Sol Adaptive 1H | 1 | €9.885,49 | €1.149,09 | €3.447,26 | €49,64 | €-40,41 |
| TEST | Rapida V1 — target pieno 2R | 4 | €9.872,94 | €2.486,65 | €7.459,94 | €197,47 | €-0,18 |
| TEST | Combo Adaptive — Quality7 + Regime | 2 | €9.867,14 | €1.069,84 | €2.139,69 | €98,95 | €-0,08 |
| TEST | Combo Adaptive — Long Only | 2 | €9.865,72 | €1.099,22 | €2.198,44 | €98,72 | €0,00 |
| TEST | Master Adaptive Expanded V1 | 3 | €9.834,10 | €1.240,15 | €2.480,31 | €146,90 | €64,08 |
| TEST | Combo Adaptive — parziale 1R | 3 | €9.831,98 | €2.809,64 | €5.619,28 | €147,90 | €-23,89 |
| TEST | Global Confluence puro 1H | 1 | €9.830,10 | €1.539,06 | €3.078,12 | €49,25 | €-17,91 |
| TEST | Rapida 1H V1 — madre | 4 | €9.824,04 | €1.865,42 | €5.596,27 | €196,49 | €21,51 |
| TEST | Eth Ema 1H | 1 | €9.819,14 | €1.138,34 | €3.415,02 | €49,18 | €-14,08 |
| TEST | Rapida V3 — Long + no HIGH + score <7,5 | 0 | €9.808,39 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive V1 | 3 | €9.795,26 | €1.239,48 | €2.478,96 | €146,74 | €68,38 |
| TEST | Master Adaptive No Alt V1 | 3 | €9.795,26 | €1.239,48 | €2.478,96 | €146,74 | €68,38 |
| TEST | Master Adaptive Runner25 V1 | 3 | €9.795,26 | €1.239,48 | €2.478,96 | €146,74 | €68,38 |
| TEST | Rapida V3 — qualità completa + profit lock | 0 | €9.773,29 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 — Long Only | 0 | €9.769,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom 5 Short 1H | 3 | €9.764,92 | €3.281,30 | €6.562,60 | €97,65 | €-8,29 |
| TEST | Top 5 + BTC — Guard + BTC≤3 + MFE | 3 | €9.763,18 | €1.277,87 | €2.555,74 | €147,04 | €-0,16 |
| TEST | Top 5 + BTC — solo MFE | 3 | €9.736,28 | €2.552,34 | €5.104,68 | €148,68 | €-0,08 |
| TEST | Combo Adaptive — MFE Trail esistente | 3 | €9.681,02 | €1.149,02 | €2.298,05 | €96,76 | €0,00 |
| TEST | Master Adaptive Gb20 V1 | 3 | €9.671,70 | €1.249,77 | €2.499,54 | €97,15 | €29,99 |
| TEST | Top 5 + BTC — Guard + MFE | 3 | €9.652,34 | €1.158,82 | €2.317,64 | €145,65 | €-0,16 |
| TEST | Master Adaptive Strict3 V1 | 3 | €9.591,13 | €1.286,13 | €2.572,26 | €144,80 | €52,21 |

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
| PRINCIPALE | Principale 4H | Confluenza trend | €9.935,59 | €-52,87 | 18 | 18 | 33,33% | 0,91 | €-2,94 | 4,26% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.688,03 | €627,89 | 30 | 30 | 53,33% | 2,18 | €20,93 | 2,70% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €10.439,51 | €381,10 | 22 | 22 | 50,00% | 1,96 | €17,32 | 2,01% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €10.390,52 | €336,34 | 37 | 37 | 51,35% | 1,46 | €9,09 | 2,30% |
| TEST | Combo Adaptive — madre | Combo Adaptive | €10.234,95 | €262,84 | 21 | 21 | 47,62% | 1,78 | €12,52 | 1,31% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €10.234,09 | €232,16 | 25 | 25 | 48,00% | 1,52 | €9,29 | 2,06% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €10.229,60 | €174,63 | 18 | 18 | 50,00% | 1,44 | €9,70 | 2,12% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €10.215,10 | €244,07 | 31 | 31 | 45,16% | 1,30 | €7,87 | 2,20% |
| TEST | Top 5 + BTC — target pieno 3R | Scanner Top 5 + forza BTC | €10.198,90 | €141,80 | 8 | 8 | 62,50% | 1,87 | €17,72 | 2,33% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €10.160,48 | €210,49 | 31 | 30 | 38,71% | 1,24 | €6,79 | 3,69% |
| TEST | Top 5 + BTC — 75% a 2,2R + runner 3R | Scanner Top 5 + forza BTC | €10.152,39 | €95,56 | 8 | 8 | 62,50% | 1,59 | €11,95 | 2,33% |
| TEST | Doge Ema 1H | Trend following EMA | €10.115,91 | €138,64 | 6 | 6 | 66,67% | 2,24 | €23,11 | 1,36% |
| TEST | Rapida V1 — score 6–7,5 | Momentum / breakout | €10.103,12 | €115,30 | 27 | 27 | 37,04% | 1,22 | €4,27 | 2,49% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.099,96 | €99,96 | 2 | 2 | 100,00% | ∞ | €49,98 | 0,31% |
| TEST | Combo Scanner | Combo Scanner | €10.093,54 | €117,73 | 23 | 23 | 43,48% | 1,20 | €5,12 | 2,66% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €10.074,06 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,40% |
| TEST | Rapida V3 — score <7,5 | Momentum / breakout V3 Filtered | €10.064,67 | €50,31 | 23 | 23 | 34,78% | 1,10 | €2,19 | 2,49% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.062,50 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,30% |
| TEST | Top 5 + BTC — Guard + BTC≤3 | Scanner Top 5 + forza BTC | €10.054,57 | €-1,60 | 4 | 4 | 50,00% | 0,99 | €-0,40 | 1,64% |
| TEST | Rapida 1H V3 Filtered — madre | Momentum / breakout V3 Filtered | €10.050,62 | €31,38 | 58 | 58 | 34,48% | 1,03 | €0,54 | 2,89% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €10.049,13 | €54,00 | 12 | 12 | 41,67% | 1,16 | €4,50 | 2,31% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €10.035,14 | €86,47 | 24 | 22 | 54,17% | 1,16 | €3,60 | 2,75% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €10.028,40 | €28,40 | 6 | 6 | 33,33% | 1,98 | €4,73 | 0,25% |
| TEST | Top 5 + BTC — BTC≤3 | Scanner Top 5 + forza BTC | €10.026,18 | €-29,80 | 4 | 4 | 50,00% | 0,73 | €-7,45 | 2,20% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €10.015,45 | €15,45 | 1 | 1 | 100,00% | ∞ | €15,45 | 0,51% |
| TEST | Ampia 4H | Confluenza trend | €10.015,43 | €35,68 | 13 | 13 | 23,08% | 1,09 | €2,74 | 2,71% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €10.008,50 | €-2,63 | 2 | 2 | 50,00% | 0,41 | €-1,31 | 0,79% |
| TEST | Combo Adaptive — Quality7 | Combo Adaptive | €10.007,91 | €36,18 | 6 | 6 | 66,67% | 1,34 | €6,03 | 1,51% |
| TEST | Rapida V1 — no HIGH + score <7,5 | Momentum / breakout | €10.007,26 | €-1,00 | 28 | 28 | 35,71% | 1,00 | €-0,04 | 2,83% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €10.005,68 | €5,68 | 6 | 6 | 33,33% | 1,98 | €0,95 | 0,05% |
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
| TEST | Rapida V1 — senza PEPE | Momentum / breakout | €9.998,04 | €-24,01 | 26 | 26 | 34,62% | 0,96 | €-0,92 | 2,10% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €9.996,12 | €-22,68 | 6 | 5 | 33,33% | 0,82 | €-3,78 | 1,69% |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | €9.992,50 | €-7,50 | 1 | 1 | 0,00% | 0,00 | €-7,50 | 0,11% |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | €9.988,38 | €-11,62 | 1 | 1 | 0,00% | 0,00 | €-11,62 | 0,17% |
| TEST | Btc Ema 4H | Trend following EMA | €9.985,39 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,68% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €9.985,39 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,68% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.982,54 | €-17,46 | 3 | 3 | 33,33% | 0,84 | €-5,82 | 1,38% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €9.980,00 | €-20,00 | 4 | 4 | 25,00% | 0,22 | €-5,00 | 0,34% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €9.975,45 | €-11,74 | 2 | 2 | 50,00% | 0,78 | €-5,87 | 0,89% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €9.975,36 | €-2,55 | 3 | 3 | 66,67% | 0,96 | €-0,85 | 0,96% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.964,86 | €-35,14 | 6 | 6 | 16,67% | 0,18 | €-5,86 | 0,36% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €9.964,31 | €-55,79 | 1 | 1 | 0,00% | 0,00 | €-55,79 | 0,93% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €9.961,22 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,64% |
| TEST | Combo Adaptive — target pieno 3R | Combo Adaptive | €9.960,81 | €-4,53 | 9 | 9 | 55,56% | 0,98 | €-0,50 | 1,41% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €9.959,40 | €-52,00 | 1 | 1 | 0,00% | 0,00 | €-52,00 | 0,60% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €9.958,62 | €-51,83 | 1 | 1 | 0,00% | 0,00 | €-51,83 | 0,59% |
| TEST | Combo Adaptive — 75% a 2R + runner 3R | Combo Adaptive | €9.956,15 | €-67,21 | 13 | 13 | 46,15% | 0,83 | €-5,17 | 2,12% |
| TEST | Top 5 + BTC — BTC 2–3 | Scanner Top 5 + forza BTC | €9.948,39 | €-49,59 | 3 | 3 | 33,33% | 0,54 | €-16,53 | 2,22% |
| TEST | Sol Ema 4H | Trend following EMA | €9.948,00 | €-52,00 | 1 | 1 | 0,00% | 0,00 | €-52,00 | 0,56% |
| TEST | Sol Ema 1H | Trend following EMA | €9.947,17 | €-62,66 | 3 | 3 | 33,33% | 0,42 | €-20,89 | 1,67% |
| TEST | Eth Ema 4H | Trend following EMA | €9.947,12 | €-52,88 | 1 | 1 | 0,00% | 0,00 | €-52,88 | 0,68% |
| TEST | Combo Adaptive — Trend/Transition | Combo Adaptive | €9.940,61 | €-55,38 | 9 | 9 | 44,44% | 0,80 | €-6,15 | 2,18% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €9.936,07 | €-62,42 | 3 | 3 | 33,33% | 0,43 | €-20,81 | 1,49% |
| TEST | Rapida V3 — senza ESPORTS | Momentum / breakout V3 Filtered | €9.933,22 | €-62,50 | 30 | 30 | 30,00% | 0,90 | €-2,08 | 2,49% |
| TEST | Btc Ema 1H | Trend following EMA | €9.928,22 | €-65,61 | 4 | 4 | 25,00% | 0,60 | €-16,40 | 1,56% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.925,78 | €-55,79 | 1 | 1 | 0,00% | 0,00 | €-55,79 | 0,81% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.921,86 | €-50,19 | 17 | 17 | 35,29% | 0,88 | €-2,95 | 2,25% |
| TEST | Combo Trend | Combo Trend | €9.916,26 | €-139,04 | 25 | 25 | 28,00% | 0,82 | €-5,56 | 3,58% |
| TEST | Rapida V3 — no volatilità HIGH | Momentum / breakout V3 Filtered | €9.906,36 | €-89,37 | 31 | 31 | 32,26% | 0,88 | €-2,88 | 2,96% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €9.897,55 | €-74,62 | 23 | 23 | 26,09% | 0,83 | €-3,24 | 3,25% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.891,55 | €-92,21 | 4 | 4 | 50,00% | 0,16 | €-23,05 | 1,24% |
| TEST | Rapida V1 — Long + BTC 1–3 + score <7,5 | Momentum / breakout | €9.891,12 | €-107,47 | 8 | 8 | 12,50% | 0,40 | €-13,43 | 1,55% |
| TEST | Top 5 + BTC — Guard | Scanner Top 5 + forza BTC | €9.890,09 | €-165,42 | 7 | 7 | 28,57% | 0,41 | €-23,63 | 3,31% |
| TEST | Combo Adaptive — Quality7 + Regime + parziale 1R | Combo Adaptive | €9.889,37 | €-109,26 | 4 | 4 | 25,00% | 0,32 | €-27,31 | 1,95% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €9.885,49 | €-71,90 | 3 | 3 | 33,33% | 0,34 | €-23,97 | 1,85% |
| TEST | Rapida V1 — target pieno 2R | Momentum / breakout | €9.872,94 | €-122,80 | 27 | 27 | 25,93% | 0,81 | €-4,55 | 2,58% |
| TEST | Combo Adaptive — Quality7 + Regime | Combo Adaptive | €9.867,14 | €-131,50 | 4 | 4 | 25,00% | 0,18 | €-32,87 | 1,95% |
| TEST | Combo Adaptive — Long Only | Combo Adaptive | €9.865,72 | €-132,59 | 5 | 5 | 20,00% | 0,42 | €-26,52 | 2,34% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €9.834,10 | €-227,96 | 7 | 7 | 14,29% | 0,29 | €-32,57 | 2,80% |
| TEST | Combo Adaptive — parziale 1R | Combo Adaptive | €9.831,98 | €-140,65 | 11 | 11 | 36,36% | 0,64 | €-12,79 | 2,24% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.830,10 | €-150,03 | 8 | 8 | 37,50% | 0,45 | €-18,75 | 2,92% |
| TEST | Rapida 1H V1 — madre | Momentum / breakout | €9.824,04 | €-194,76 | 66 | 66 | 31,82% | 0,88 | €-2,95 | 6,76% |
| TEST | Eth Ema 1H | Trend following EMA | €9.819,14 | €-164,74 | 6 | 6 | 33,33% | 0,25 | €-27,46 | 1,92% |
| TEST | Rapida V3 — Long + no HIGH + score <7,5 | Momentum / breakout V3 Filtered | €9.808,39 | €-191,61 | 19 | 19 | 31,58% | 0,66 | €-10,08 | 2,77% |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | €9.795,26 | €-271,00 | 5 | 5 | 0,00% | 0,00 | €-54,20 | 3,19% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €9.795,26 | €-271,00 | 5 | 5 | 0,00% | 0,00 | €-54,20 | 3,19% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €9.795,26 | €-271,00 | 5 | 5 | 0,00% | 0,00 | €-54,20 | 3,19% |
| TEST | Rapida V3 — qualità completa + profit lock | Momentum / breakout V3 Filtered | €9.773,29 | €-226,71 | 19 | 19 | 42,11% | 0,62 | €-11,93 | 3,16% |
| TEST | Rapida V3 — Long Only | Momentum / breakout V3 Filtered | €9.769,04 | €-230,96 | 24 | 24 | 25,00% | 0,65 | €-9,62 | 3,31% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.764,92 | €-222,24 | 22 | 22 | 31,82% | 0,61 | €-10,10 | 5,48% |
| TEST | Top 5 + BTC — Guard + BTC≤3 + MFE | Scanner Top 5 + forza BTC | €9.763,18 | €-235,12 | 13 | 13 | 30,77% | 0,41 | €-18,09 | 2,37% |
| TEST | Top 5 + BTC — solo MFE | Scanner Top 5 + forza BTC | €9.736,28 | €-260,88 | 11 | 11 | 27,27% | 0,17 | €-23,72 | 3,52% |
| TEST | Combo Adaptive — MFE Trail esistente | Combo Adaptive | €9.681,02 | €-317,53 | 27 | 27 | 25,93% | 0,45 | €-11,76 | 4,11% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €9.671,70 | €-356,79 | 27 | 27 | 51,85% | 0,44 | €-13,21 | 4,16% |
| TEST | Top 5 + BTC — Guard + MFE | Scanner Top 5 + forza BTC | €9.652,34 | €-346,25 | 16 | 16 | 25,00% | 0,32 | €-21,64 | 3,54% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €9.591,13 | €-459,54 | 13 | 13 | 15,38% | 0,29 | €-35,35 | 4,60% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | LAB | SHORT | Confluenza trend | 240m | 3,0x | 0,17841 | 0,17841 | 0,17841 | 0,23699 | 0,13559 | €136,26 | €408,77 | €0,00 | €-0,00 |
| Principale 4H | SUI | LONG | Confluenza trend | 240m | 3,0x | 0,76296 | 0,76296 | 0,73998 | 0,51245 | 0,80891 | €547,52 | €1.642,56 | €49,46 | €0,00 |
| Principale 4H | ONDO | LONG | Confluenza trend | 240m | 3,0x | 0,40344 | 0,40344 | 0,37762 | 0,27098 | 0,45509 | €254,70 | €764,09 | €48,91 | €0,00 |
| Principale 4H | DOGE | SHORT | Confluenza trend | 240m | 3,0x | 0,06940 | 0,06982 | 0,07160 | 0,09218 | 0,06498 | €524,39 | €1.573,18 | €50,01 | €-9,61 |
| Bilanciata 1H V1 | ONDO | LONG | Confluenza trend | 60m | 3,0x | 0,39694 | 0,39694 | 0,38539 | 0,26661 | 0,42004 | €581,76 | €1.745,29 | €50,78 | €0,00 |
| Bilanciata 1H V1 | DOGE | SHORT | Confluenza trend | 60m | 3,0x | 0,06953 | 0,06982 | 0,07070 | 0,09235 | 0,06717 | €1.013,54 | €3.040,62 | €51,54 | €-12,85 |
| Bilanciata 1H V1 | ADA | SHORT | Confluenza trend | 60m | 3,0x | 0,16703 | 0,16634 | 0,16999 | 0,22187 | 0,16112 | €978,72 | €2.936,17 | €51,97 | €12,12 |
| Bilanciata 1H V1 | BANK | LONG | Confluenza trend | 60m | 3,0x | 0,26033 | 0,29665 | 0,26891 | 0,17486 | 0,32281 | €143,89 | €431,67 | €0,00 | €60,22 |
| Bilanciata 1H V2 | ESPORTS | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,02164 | 0,02164 | 0,02164 | 0,02874 | 0,01644 | €138,69 | €416,06 | €0,00 | €-0,00 |
| Bilanciata 1H V2 | BTC | SHORT | Confluenza trend V2 | 60m | 3,0x | 64717,76386 | 64907,07000 | 65649,69966 | 85966,76299 | 62853,89226 | €1.163,40 | €3.490,20 | €50,26 | €-10,21 |
| Bilanciata 1H V2 | DOGE | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,06911 | 0,06982 | 0,07010 | 0,09180 | 0,06712 | €1.163,35 | €3.490,05 | €50,26 | €-36,05 |
| Bilanciata 1H V2 | AKE | LONG | Confluenza trend V2 | 60m | 3,0x | 0,00271 | 0,00271 | 0,00239 | 0,00182 | 0,00336 | €139,38 | €418,14 | €50,18 | €-0,08 |
| Bilanciata 1H V3 Filtered | ESPORTS | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,02126 | 0,02126 | 0,02126 | 0,02823 | 0,01615 | €141,51 | €424,52 | €0,00 | €-0,00 |
| Bilanciata 1H V3 Filtered | ONDO | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,40134 | 0,40134 | 0,38898 | 0,26957 | 0,42605 | €557,59 | €1.672,77 | €51,50 | €0,00 |
| Bilanciata 1H V3 Filtered | BTC | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 64923,19276 | 64907,07000 | 65858,08674 | 86239,64105 | 63053,40481 | €1.167,13 | €3.501,39 | €50,42 | €0,87 |
| Bilanciata 1H V3 Filtered | DOGE | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,06934 | 0,06982 | 0,07033 | 0,09210 | 0,06734 | €1.184,17 | €3.552,50 | €51,16 | €-24,79 |
| Rapida 1H V1 — madre | ONDO | LONG | Momentum / breakout | 60m | 3,0x | 0,39924 | 0,39924 | 0,38995 | 0,26816 | 0,41318 | €708,01 | €2.124,02 | €49,43 | €0,00 |
| Rapida 1H V1 — madre | ZEC | SHORT | Momentum / breakout | 60m | 3,0x | 503,83921 | 499,59000 | 513,54273 | 669,26642 | 489,28394 | €857,19 | €2.571,57 | €49,53 | €21,69 |
| Rapida 1H V1 — madre | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00271 | 0,00271 | 0,00239 | 0,00182 | 0,00319 | €139,05 | €417,14 | €49,12 | €-0,08 |
| Rapida 1H V1 — madre | BANK | LONG | Momentum / breakout | 60m | 3,0x | 0,29671 | 0,29665 | 0,26700 | 0,19929 | 0,34127 | €161,18 | €483,53 | €48,41 | €-0,10 |
| Rapida V1 — score 6–7,5 | BTC | SHORT | Momentum / breakout | 60m | 3,0x | 65079,58148 | 64907,07000 | 65808,47279 | 86447,37740 | 63986,24451 | €1.483,09 | €4.449,28 | €49,83 | €11,79 |
| Rapida V1 — score 6–7,5 | DOGE | SHORT | Momentum / breakout | 60m | 3,0x | 0,06953 | 0,06982 | 0,07044 | 0,09235 | 0,06815 | €1.281,83 | €3.845,50 | €50,70 | €-16,26 |
| Rapida V1 — score 6–7,5 | TAO | SHORT | Momentum / breakout | 60m | 3,0x | 192,24458 | 192,24458 | 194,42319 | 255,36489 | 188,97667 | €1.501,26 | €4.503,79 | €51,04 | €-0,00 |
| Rapida V1 — no HIGH + score <7,5 | ONDO | LONG | Momentum / breakout | 60m | 3,0x | 0,39924 | 0,39924 | 0,38995 | 0,26816 | 0,41318 | €704,39 | €2.113,17 | €49,18 | €0,00 |
| Rapida V1 — no HIGH + score <7,5 | BTC | SHORT | Momentum / breakout | 60m | 3,0x | 64923,19276 | 64907,07000 | 65650,33252 | 86239,64105 | 63832,48313 | €1.473,17 | €4.419,52 | €49,50 | €1,10 |
| Rapida V1 — no HIGH + score <7,5 | TAO | SHORT | Momentum / breakout | 60m | 3,0x | 192,24458 | 192,24458 | 194,42319 | 255,36489 | 188,97667 | €1.474,44 | €4.423,31 | €50,13 | €-0,00 |
| Rapida V1 — no HIGH + score <7,5 | ADA | SHORT | Momentum / breakout | 60m | 3,0x | 0,16708 | 0,16634 | 0,16933 | 0,22194 | 0,16370 | €1.232,63 | €3.697,90 | €49,91 | €16,37 |
| Rapida V1 — Long + BTC 1–3 + score <7,5 | ONDO | LONG | Momentum / breakout | 60m | 3,0x | 0,39694 | 0,39694 | 0,38849 | 0,26661 | 0,40961 | €783,06 | €2.349,19 | €50,00 | €0,00 |
| Rapida V1 — senza PEPE | ONDO | LONG | Momentum / breakout | 60m | 3,0x | 0,39924 | 0,39924 | 0,38995 | 0,26816 | 0,41318 | €713,68 | €2.141,05 | €49,83 | €0,00 |
| Rapida V1 — senza PEPE | ZEC | SHORT | Momentum / breakout | 60m | 3,0x | 504,42909 | 499,59000 | 514,14397 | 670,04998 | 489,85678 | €867,81 | €2.603,42 | €50,14 | €24,98 |
| Rapida V1 — senza PEPE | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00271 | 0,00271 | 0,00239 | 0,00182 | 0,00319 | €141,51 | €424,53 | €49,99 | €-0,08 |
| Rapida V1 — senza PEPE | BANK | LONG | Momentum / breakout | 60m | 3,0x | 0,29671 | 0,29665 | 0,26700 | 0,19929 | 0,34127 | €166,45 | €499,35 | €49,99 | €-0,10 |
| Rapida V1 — target pieno 2R | ONDO | LONG | Momentum / breakout | 60m | 3,0x | 0,39924 | 0,39924 | 0,38995 | 0,26816 | 0,41782 | €712,92 | €2.138,77 | €49,77 | €0,00 |
| Rapida V1 — target pieno 2R | TAO | SHORT | Momentum / breakout | 60m | 3,0x | 192,24458 | 192,24458 | 194,42319 | 255,36489 | 187,88737 | €1.473,39 | €4.420,17 | €50,09 | €-0,00 |
| Rapida V1 — target pieno 2R | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00271 | 0,00271 | 0,00239 | 0,00182 | 0,00335 | €139,74 | €419,22 | €49,37 | €-0,08 |
| Rapida V1 — target pieno 2R | BANK | LONG | Momentum / breakout | 60m | 3,0x | 0,29671 | 0,29665 | 0,26700 | 0,19929 | 0,35612 | €160,59 | €481,78 | €48,23 | €-0,10 |
| Rapida 1H V2 | BTC | SHORT | Momentum / breakout V2 | 60m | 3,0x | 64923,19276 | 64907,07000 | 65650,33252 | 86239,64105 | 63832,48313 | €1.485,87 | €4.457,60 | €49,93 | €1,11 |
| Rapida 1H V2 | ZEC | SHORT | Momentum / breakout V2 | 60m | 3,0x | 503,83921 | 499,59000 | 513,54273 | 669,26642 | 489,28394 | €862,65 | €2.587,94 | €49,84 | €21,83 |
| Rapida 1H V3 Filtered — madre | ONDO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,39924 | 0,39924 | 0,38995 | 0,26816 | 0,41318 | €715,14 | €2.145,42 | €49,93 | €0,00 |
| Rapida 1H V3 Filtered — madre | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 503,83921 | 499,59000 | 513,54273 | 669,26642 | 489,28394 | €877,00 | €2.631,00 | €50,67 | €22,19 |
| Rapida 1H V3 Filtered — madre | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00271 | 0,00271 | 0,00239 | 0,00182 | 0,00319 | €142,26 | €426,77 | €50,26 | €-0,09 |
| Rapida 1H V3 Filtered — madre | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,29671 | 0,29665 | 0,26700 | 0,19929 | 0,34127 | €167,02 | €501,07 | €50,17 | €-0,10 |
| Rapida V3 — score <7,5 | ONDO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,39924 | 0,39924 | 0,38995 | 0,26816 | 0,41318 | €712,28 | €2.136,85 | €49,73 | €0,00 |
| Rapida V3 — score <7,5 | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 64923,19276 | 64907,07000 | 65650,33252 | 86239,64105 | 63832,48313 | €1.484,27 | €4.452,81 | €49,87 | €1,11 |
| Rapida V3 — score <7,5 | TAO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 192,24458 | 192,24458 | 194,42319 | 255,36489 | 188,97667 | €1.485,79 | €4.457,37 | €50,51 | €-0,00 |
| Rapida V3 — score <7,5 | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16732 | 0,16634 | 0,16956 | 0,22226 | 0,16396 | €1.246,68 | €3.740,05 | €50,10 | €21,90 |
| Rapida V3 — no volatilità HIGH | ONDO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,39924 | 0,39924 | 0,38995 | 0,26816 | 0,41318 | €707,41 | €2.122,22 | €49,39 | €0,00 |
| Rapida V3 — no volatilità HIGH | TAO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 192,24458 | 192,24458 | 194,42319 | 255,36489 | 188,97667 | €1.478,41 | €4.435,24 | €50,26 | €-0,00 |
| Rapida V3 — no volatilità HIGH | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00271 | 0,00271 | 0,00239 | 0,00182 | 0,00319 | €140,21 | €420,64 | €49,54 | €-0,08 |
| Rapida V3 — no volatilità HIGH | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,29671 | 0,29665 | 0,26700 | 0,19929 | 0,34127 | €162,98 | €488,93 | €48,95 | €-0,10 |
| Rapida V3 — senza ESPORTS | ONDO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,39924 | 0,39924 | 0,38995 | 0,26816 | 0,41318 | €712,28 | €2.136,85 | €49,73 | €0,00 |
| Rapida V3 — senza ESPORTS | TAO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 192,24458 | 192,24458 | 194,42319 | 255,36489 | 188,97667 | €1.482,41 | €4.447,24 | €50,40 | €-0,00 |
| Rapida V3 — senza ESPORTS | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00271 | 0,00271 | 0,00239 | 0,00182 | 0,00319 | €140,59 | €421,78 | €49,67 | €-0,08 |
| Rapida V3 — senza ESPORTS | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,29671 | 0,29665 | 0,26700 | 0,19929 | 0,34127 | €162,73 | €488,20 | €48,88 | €-0,10 |
| Ampia 4H | DOGE | SHORT | Confluenza trend | 240m | 2,0x | 0,07237 | 0,06982 | 0,07105 | 0,10819 | 0,06457 | €649,49 | €1.298,97 | €0,00 | €45,71 |
| Ampia 4H | ZEC | LONG | Confluenza trend | 240m | 2,0x | 522,36445 | 499,59000 | 483,09844 | 263,79405 | 632,30930 | €332,53 | €665,06 | €49,99 | €-29,00 |
| Ampia 4H | PEPE | LONG | Confluenza trend | 240m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €497,18 | €994,35 | €50,70 | €-34,87 |
| Ampia 4H | HYPE | SHORT | Confluenza trend | 240m | 2,0x | 58,36732 | 58,40400 | 61,80927 | 87,25915 | 48,72988 | €424,03 | €848,06 | €50,01 | €-0,53 |
| Forza relativa 1H V1 | ESPORTS | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,02126 | 0,02126 | 0,02126 | 0,03178 | 0,01564 | €208,05 | €416,10 | €0,00 | €-0,00 |
| Forza relativa 1H V1 | NIGHT | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,02031 | 0,02031 | 0,02210 | 0,03036 | 0,01637 | €285,91 | €571,83 | €50,45 | €-0,00 |
| Forza relativa 1H V1 | ONDO | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,42171 | €891,90 | €1.783,80 | €49,29 | €0,00 |
| Forza relativa 1H V1 | DOGE | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,06933 | 0,06982 | 0,07032 | 0,10364 | 0,06713 | €1.694,34 | €3.388,67 | €48,80 | €-24,14 |
| Forza relativa 1H V2 | ESPORTS | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,02126 | 0,02126 | 0,02126 | 0,03178 | 0,01564 | €215,33 | €430,67 | €0,00 | €-0,00 |
| Forza relativa 1H V2 | HYPE | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 57,89642 | 58,40400 | 59,12372 | 86,55515 | 55,19635 | €1.212,96 | €2.425,92 | €51,43 | €-21,27 |
| Forza relativa 1H V2 | DOGE | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,06933 | 0,06982 | 0,07032 | 0,10364 | 0,06713 | €1.728,07 | €3.456,14 | €49,77 | €-24,62 |
| Forza relativa 1H V2 | AKE | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,00271 | 0,00271 | 0,00239 | 0,00137 | 0,00343 | €209,76 | €419,52 | €50,34 | €-0,08 |
| Benchmark Donchian breakout 1H | SUI | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,76606 | 0,76606 | 0,75182 | 0,38686 | 0,80165 | €1.377,00 | €2.754,00 | €51,18 | €0,00 |
| Benchmark Donchian breakout 1H | ZEC | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 514,40710 | 499,59000 | 514,36486 | 769,03861 | 481,15276 | €982,86 | €1.965,73 | €0,00 | €56,62 |
| Benchmark Bollinger mean reversion 1H | DOGE | LONG | Bollinger mean reversion | 60m | 2,0x | 0,06944 | 0,06982 | 0,06861 | 0,03507 | 0,07069 | €2.013,01 | €4.026,02 | €48,31 | €21,81 |
| Benchmark Bollinger mean reversion 1H | SOL | LONG | Bollinger mean reversion | 60m | 2,0x | 75,67913 | 75,39700 | 74,77098 | 38,21796 | 77,04136 | €2.013,07 | €4.026,14 | €48,31 | €-15,01 |
| Benchmark trend following EMA 1H | LAB | LONG | Trend following EMA | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €207,05 | €414,10 | €49,69 | €0,00 |
| Benchmark trend following EMA 1H | DOGE | SHORT | Trend following EMA | 60m | 2,0x | 0,06933 | 0,06982 | 0,07044 | 0,10364 | 0,06689 | €1.556,03 | €3.112,05 | €49,79 | €-22,17 |
| Benchmark trend following EMA 1H | PEPE | SHORT | Trend following EMA | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.555,71 | €3.111,43 | €49,78 | €-1,42 |
| Scanner Top 5 Long 1H | ONDO | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,40114 | 0,40114 | 0,38834 | 0,20258 | 0,42673 | €828,91 | €1.657,82 | €52,88 | €0,00 |
| Scanner Top 5 Long 1H | LAB | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €219,03 | €438,05 | €52,57 | €0,00 |
| Scanner Top 5 Long 1H | BANK | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,26033 | 0,29665 | 0,26891 | 0,13147 | 0,32281 | €221,39 | €442,77 | €0,00 | €61,77 |
| Scanner Bottom 5 Short 1H | ESPORTS | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,02150 | 0,02150 | 0,02150 | 0,03214 | 0,01634 | €207,40 | €414,80 | €0,00 | €-0,00 |
| Scanner Bottom 5 Short 1H | DOGE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,06942 | 0,06982 | 0,07042 | 0,10378 | 0,06742 | €1.692,83 | €3.385,67 | €48,75 | €-19,70 |
| Scanner Bottom 5 Short 1H | ADA | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,16703 | 0,16634 | 0,16999 | 0,24971 | 0,16112 | €1.381,07 | €2.762,13 | €48,89 | €11,41 |
| Scanner Top 5 + forza BTC 1H | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39694 | 0,39694 | 0,38539 | 0,20045 | 0,42235 | €898,57 | €1.797,15 | €52,29 | €0,00 |
| Scanner Top 5 + forza BTC 1H | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €216,56 | €433,12 | €51,97 | €0,00 |
| Scanner Top 5 + forza BTC 1H | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,26033 | 0,29665 | 0,26891 | 0,13147 | 0,32906 | €216,24 | €432,48 | €0,00 | €60,33 |
| Top 5 + BTC — solo MFE | SUI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,76776 | 0,76776 | 0,75508 | 0,38772 | 0,79565 | €1.514,04 | €3.028,08 | €50,00 | €0,00 |
| Top 5 + BTC — solo MFE | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39924 | 0,39924 | 0,38729 | 0,20162 | 0,42552 | €835,46 | €1.670,91 | €50,00 | €0,00 |
| Top 5 + BTC — solo MFE | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00271 | 0,00271 | 0,00239 | 0,00137 | 0,00343 | €202,85 | €405,69 | €48,68 | €-0,08 |
| Top 5 + BTC — Guard | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39724 | 0,39724 | 0,38434 | 0,20061 | 0,42561 | €756,62 | €1.513,24 | €49,13 | €0,00 |
| Top 5 + BTC — Guard | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €202,47 | €404,95 | €48,59 | €0,00 |
| Top 5 + BTC — Guard | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,26033 | 0,29665 | 0,26891 | 0,13147 | 0,32906 | €204,86 | €409,72 | €0,00 | €57,16 |
| Top 5 + BTC — BTC≤3 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39974 | 0,39974 | 0,38840 | 0,20187 | 0,42468 | €884,65 | €1.769,29 | €50,18 | €0,00 |
| Top 5 + BTC — BTC≤3 | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €207,87 | €415,74 | €49,89 | €0,00 |
| Top 5 + BTC — BTC≤3 | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,26033 | 0,29665 | 0,26891 | 0,13147 | 0,32906 | €207,68 | €415,35 | €0,00 | €57,94 |
| Top 5 + BTC — BTC 2–3 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39974 | 0,39974 | 0,38840 | 0,20187 | 0,42468 | €884,65 | €1.769,29 | €50,18 | €0,00 |
| Top 5 + BTC — BTC 2–3 | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €207,87 | €415,74 | €49,89 | €0,00 |
| Top 5 + BTC — BTC 2–3 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00271 | 0,00271 | 0,00239 | 0,00137 | 0,00343 | €207,27 | €414,53 | €49,74 | €-0,08 |
| Top 5 + BTC — Guard + MFE | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39724 | 0,39724 | 0,38434 | 0,20061 | 0,42561 | €756,62 | €1.513,24 | €49,13 | €0,00 |
| Top 5 + BTC — Guard + MFE | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00271 | 0,00271 | 0,00239 | 0,00137 | 0,00343 | €201,10 | €402,21 | €48,26 | €-0,08 |
| Top 5 + BTC — Guard + MFE | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,29671 | 0,29665 | 0,26110 | 0,14984 | 0,37504 | €201,10 | €402,19 | €48,26 | €-0,08 |
| Top 5 + BTC — Guard + BTC≤3 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39974 | 0,39974 | 0,38840 | 0,20187 | 0,42468 | €871,05 | €1.742,11 | €49,41 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €205,84 | €411,68 | €49,40 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,26033 | 0,29665 | 0,26891 | 0,13147 | 0,32906 | €208,27 | €416,53 | €0,00 | €58,11 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39974 | 0,39974 | 0,38840 | 0,20187 | 0,42468 | €871,05 | €1.742,11 | €49,41 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00271 | 0,00271 | 0,00239 | 0,00137 | 0,00343 | €203,41 | €406,83 | €48,82 | €-0,08 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,29671 | 0,29665 | 0,26110 | 0,14984 | 0,37504 | €203,41 | €406,81 | €48,82 | €-0,08 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39694 | 0,39694 | 0,38539 | 0,20045 | 0,43159 | €861,83 | €1.723,66 | €50,15 | €0,00 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,21338 | €207,96 | €415,92 | €49,91 | €0,00 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,26033 | 0,29665 | 0,26891 | 0,13147 | 0,35405 | €210,29 | €420,58 | €0,00 | €58,67 |
| Top 5 + BTC — target pieno 3R | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39694 | 0,39694 | 0,38539 | 0,20045 | 0,43159 | €861,83 | €1.723,66 | €50,15 | €0,00 |
| Top 5 + BTC — target pieno 3R | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,21338 | €207,96 | €415,92 | €49,91 | €0,00 |
| Top 5 + BTC — target pieno 3R | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,26033 | 0,29665 | 0,26891 | 0,13147 | 0,35405 | €211,25 | €422,51 | €0,00 | €58,94 |
| Global Confluence puro 1H | DOGE | SHORT | Global Confluence puro | 60m | 2,0x | 0,06942 | 0,06982 | 0,07053 | 0,10378 | 0,06664 | €1.539,06 | €3.078,12 | €49,25 | €-17,91 |
| Combo Trend | ESPORTS | SHORT | Combo Trend | 60m | 2,0x | 0,01883 | 0,01883 | 0,02109 | 0,02815 | 0,01386 | €209,57 | €419,14 | €50,30 | €-0,00 |
| Combo Trend | DOGE | SHORT | Combo Trend | 60m | 2,0x | 0,06929 | 0,06982 | 0,07039 | 0,10358 | 0,06685 | €1.546,95 | €3.093,91 | €49,50 | €-23,84 |
| Combo Trend | BANK | LONG | Combo Trend | 60m | 2,0x | 0,24758 | 0,29665 | 0,26056 | 0,12503 | 0,31294 | €205,58 | €411,17 | €0,00 | €81,49 |
| Combo Mean Reversion | BTC | LONG | Combo Mean Reversion | 60m | 2,0x | 64949,16724 | 64907,07000 | 64169,77723 | 32799,32945 | 66196,19125 | €2.006,38 | €4.012,76 | €48,15 | €-2,60 |
| Combo Scanner | ONDO | LONG | Combo Scanner | 60m | 2,0x | 0,39694 | 0,39694 | 0,38539 | 0,20045 | 0,42235 | €857,88 | €1.715,77 | €49,92 | €0,00 |
| Combo Scanner | LAB | LONG | Combo Scanner | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €207,54 | €415,08 | €49,81 | €0,00 |
| Combo Scanner | DOGE | SHORT | Combo Scanner | 60m | 2,0x | 0,06942 | 0,06982 | 0,07042 | 0,10378 | 0,06722 | €1.753,42 | €3.506,85 | €50,50 | €-20,40 |
| Combo Adaptive — madre | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,40114 | 0,40114 | 0,38834 | 0,20258 | 0,42673 | €809,25 | €1.618,50 | €51,63 | €0,00 |
| Combo Adaptive — madre | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15861 | 0,13958 | 0,08010 | 0,19668 | €213,13 | €426,26 | €51,15 | €0,00 |
| Combo Adaptive — madre | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,06934 | 0,06982 | 0,07033 | 0,10366 | 0,06734 | €1.781,54 | €3.563,09 | €51,31 | €-24,87 |
| Combo Adaptive — MFE Trail esistente | ESPORTS | SHORT | Combo Adaptive | 60m | 2,0x | 0,02156 | 0,02156 | 0,02091 | 0,03223 | 0,01638 | €202,62 | €405,24 | €0,00 | €-0,00 |
| Combo Adaptive — MFE Trail esistente | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39784 | 0,39784 | 0,38492 | 0,20091 | 0,42367 | €744,71 | €1.489,41 | €48,35 | €0,00 |
| Combo Adaptive — MFE Trail esistente | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15861 | 0,13958 | 0,08010 | 0,19668 | €201,70 | €403,39 | €48,41 | €0,00 |
| Combo Adaptive — Quality7 | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,40304 | 0,40304 | 0,39140 | 0,20354 | 0,42632 | €859,15 | €1.718,30 | €49,62 | €0,00 |
| Combo Adaptive — Quality7 | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,06933 | 0,06982 | 0,07032 | 0,10364 | 0,06733 | €1.742,21 | €3.484,43 | €50,18 | €-24,82 |
| Combo Adaptive — Quality7 | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,00271 | 0,00271 | 0,00239 | 0,00137 | 0,00336 | €208,50 | €417,01 | €50,04 | €-0,08 |
| Combo Adaptive — Trend/Transition | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39724 | 0,39724 | 0,38434 | 0,20061 | 0,42303 | €757,94 | €1.515,88 | €49,21 | €0,00 |
| Combo Adaptive — Trend/Transition | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15861 | 0,13958 | 0,08010 | 0,19668 | €206,52 | €413,04 | €49,56 | €0,00 |
| Combo Adaptive — Trend/Transition | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,06981 | 0,06982 | 0,07081 | 0,10436 | 0,06780 | €1.726,28 | €3.452,56 | €49,72 | €-0,69 |
| Combo Adaptive — Quality7 + Regime | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,40554 | 0,40554 | 0,39390 | 0,20480 | 0,42882 | €864,27 | €1.728,54 | €49,61 | €0,00 |
| Combo Adaptive — Quality7 + Regime | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,00271 | 0,00271 | 0,00239 | 0,00137 | 0,00336 | €205,57 | €411,14 | €49,34 | €-0,08 |
| Combo Adaptive — Long Only | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,41951 | €893,67 | €1.787,34 | €49,39 | €0,00 |
| Combo Adaptive — Long Only | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €205,55 | €411,10 | €49,33 | €0,00 |
| Combo Adaptive — parziale 1R | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,41951 | €893,02 | €1.786,04 | €49,36 | €0,00 |
| Combo Adaptive — parziale 1R | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €205,22 | €410,44 | €49,25 | €0,00 |
| Combo Adaptive — parziale 1R | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,06934 | 0,06982 | 0,07033 | 0,10366 | 0,06734 | €1.711,40 | €3.422,80 | €49,29 | €-23,89 |
| Combo Adaptive — Quality7 + Regime + parziale 1R | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,40554 | 0,40554 | 0,39390 | 0,20480 | 0,42882 | €864,27 | €1.728,54 | €49,61 | €0,00 |
| Combo Adaptive — Quality7 + Regime + parziale 1R | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,00271 | 0,00271 | 0,00239 | 0,00137 | 0,00336 | €206,04 | €412,07 | €49,45 | €-0,08 |
| Combo Adaptive — 75% a 2R + runner 3R | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,43050 | €902,18 | €1.804,37 | €49,86 | €0,00 |
| Combo Adaptive — 75% a 2R + runner 3R | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,06920 | 0,06982 | 0,07019 | 0,10345 | 0,06621 | €1.731,45 | €3.462,90 | €49,87 | €-31,22 |
| Combo Adaptive — 75% a 2R + runner 3R | BANK | LONG | Combo Adaptive | 60m | 2,0x | 0,26033 | 0,29665 | 0,27089 | 0,13147 | 0,35405 | €206,98 | €413,96 | €0,00 | €57,75 |
| Combo Adaptive — target pieno 3R | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,43050 | €902,18 | €1.804,37 | €49,86 | €0,00 |
| Combo Adaptive — target pieno 3R | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15861 | 0,13958 | 0,08010 | 0,21571 | €207,43 | €414,86 | €49,78 | €0,00 |
| Combo Adaptive — target pieno 3R | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,06920 | 0,06982 | 0,07019 | 0,10345 | 0,06621 | €1.735,05 | €3.470,11 | €49,97 | €-31,28 |
| Btc Ema 1H | BTC | SHORT | Trend following EMA | 60m | 3,0x | 64834,39053 | 64907,07000 | 65768,00575 | 86121,68208 | 62967,16008 | €1.149,81 | €3.449,44 | €49,67 | €-3,87 |
| Btc Ema 4H | BTC | LONG | Trend following EMA | 240m | 2,0x | 65410,57950 | 64907,07000 | 63931,54687 | 33032,34265 | 69108,16107 | €1.105,63 | €2.211,26 | €50,00 | €-17,02 |
| Btc Donchian 1H | BTC | SHORT | Donchian breakout 20 barre | 60m | 3,0x | 64923,19276 | 64907,07000 | 65754,20963 | 86239,64105 | 63261,15903 | €1.293,96 | €3.881,87 | €49,69 | €0,96 |
| Btc Donchian 4H | BTC | LONG | Donchian breakout 20 barre | 240m | 2,0x | 65410,57950 | 64907,07000 | 63931,54687 | 33032,34265 | 69551,87112 | €1.105,63 | €2.211,26 | €50,00 | €-17,02 |
| Btc Bollinger 4H | BTC | SHORT | Bollinger mean reversion | 240m | 2,0x | 66588,49964 | 64907,07000 | 65621,81812 | 99549,80696 | 64307,80290 | €1.313,84 | €2.627,69 | €0,00 | €66,35 |
| Btc Adaptive 1H | BTC | SHORT | Combo Adaptive | 60m | 3,0x | 64713,55470 | 64907,07000 | 65645,42989 | 85961,17183 | 62849,80432 | €1.156,05 | €3.468,15 | €49,94 | €-10,37 |
| Btc Adaptive 4H | BTC | LONG | Combo Adaptive | 240m | 2,0x | 66171,85172 | 64907,07000 | 64592,42491 | 33416,78512 | 70120,41876 | €1.047,40 | €2.094,81 | €50,00 | €-40,04 |
| Sol Ema 1H | SOL | SHORT | Trend following EMA | 60m | 3,0x | 75,65487 | 75,39700 | 76,74430 | 100,49488 | 73,47601 | €1.150,16 | €3.450,47 | €49,69 | €11,76 |
| Sol Donchian 1H | SOL | SHORT | Donchian breakout 20 barre | 60m | 3,0x | 75,65487 | 75,39700 | 76,62325 | 100,49488 | 73,71810 | €1.301,74 | €3.905,22 | €49,99 | €13,31 |
| Sol Donchian 4H | SOL | SHORT | Donchian breakout 20 barre | 240m | 2,0x | 75,96380 | 75,39700 | 78,23939 | 113,56589 | 69,59218 | €830,21 | €1.660,43 | €49,74 | €12,39 |
| Sol Bollinger 1H | SOL | LONG | Bollinger mean reversion | 60m | 3,0x | 75,68513 | 75,39700 | 74,77691 | 50,83518 | 77,04747 | €1.381,14 | €4.143,42 | €49,72 | €-15,77 |
| Sol Bollinger 4H | SOL | SHORT | Bollinger mean reversion | 240m | 2,0x | 78,45931 | 75,39700 | 76,84028 | 117,29666 | 74,81402 | €968,56 | €1.937,11 | €0,00 | €75,61 |
| Sol Adaptive 1H | SOL | LONG | Combo Adaptive | 60m | 3,0x | 76,29126 | 75,39700 | 75,19266 | 51,24229 | 78,48844 | €1.149,09 | €3.447,26 | €49,64 | €-40,41 |
| Sol Adaptive 4H | SOL | SHORT | Combo Adaptive | 240m | 2,0x | 75,96380 | 75,39700 | 78,44626 | 113,56589 | 69,75767 | €761,04 | €1.522,08 | €49,74 | €11,36 |
| Eth Ema 1H | ETH | SHORT | Trend following EMA | 60m | 3,0x | 1873,22528 | 1880,95000 | 1900,19972 | 2488,26758 | 1819,27639 | €1.138,34 | €3.415,02 | €49,18 | €-14,08 |
| Eth Adaptive 1H | ETH | SHORT | Combo Adaptive | 60m | 3,0x | 1873,22528 | 1880,95000 | 1900,19972 | 2488,26758 | 1819,27639 | €1.146,74 | €3.440,21 | €49,54 | €-14,19 |
| Doge Ema 1H | DOGE | SHORT | Trend following EMA | 60m | 3,0x | 0,06942 | 0,06982 | 0,07042 | 0,09221 | 0,06742 | €1.173,45 | €3.520,36 | €50,69 | €-20,48 |
| Doge Donchian 1H | DOGE | SHORT | Donchian breakout 20 barre | 60m | 3,0x | 0,06940 | 0,06982 | 0,07045 | 0,09218 | 0,06729 | €1.095,98 | €3.287,94 | €49,99 | €-20,08 |
| Doge Bollinger 1H | DOGE | LONG | Bollinger mean reversion | 60m | 3,0x | 0,06944 | 0,06982 | 0,06861 | 0,04664 | 0,07069 | €1.381,14 | €4.143,42 | €49,72 | €22,44 |
| Master Adaptive V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39854 | 0,39854 | 0,38677 | 0,20126 | 0,42207 | €833,00 | €1.665,99 | €49,19 | €0,00 |
| Master Adaptive V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €203,80 | €407,60 | €48,91 | €0,00 |
| Master Adaptive V1 | BANK | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,25383 | 0,29665 | 0,22337 | 0,12818 | 0,31475 | €202,68 | €405,37 | €48,64 | €68,38 |
| Master Adaptive No Alt V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39854 | 0,39854 | 0,38677 | 0,20126 | 0,42207 | €833,00 | €1.665,99 | €49,19 | €0,00 |
| Master Adaptive No Alt V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €203,80 | €407,60 | €48,91 | €0,00 |
| Master Adaptive No Alt V1 | BANK | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,25383 | 0,29665 | 0,22337 | 0,12818 | 0,31475 | €202,68 | €405,37 | €48,64 | €68,38 |
| Master Adaptive Strict3 V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,41951 | €887,07 | €1.774,14 | €49,03 | €0,00 |
| Master Adaptive Strict3 V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00240 | 0,00271 | 0,00211 | 0,00121 | 0,00297 | €199,24 | €398,48 | €47,82 | €52,29 |
| Master Adaptive Strict3 V1 | BANK | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,29671 | 0,29665 | 0,26110 | 0,14984 | 0,36792 | €199,82 | €399,64 | €47,96 | €-0,08 |
| Master Adaptive Expanded V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39854 | 0,39854 | 0,38677 | 0,20126 | 0,42207 | €833,00 | €1.665,99 | €49,19 | €0,00 |
| Master Adaptive Expanded V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €203,80 | €407,60 | €48,91 | €0,00 |
| Master Adaptive Expanded V1 | BANK | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,25627 | 0,29665 | 0,22552 | 0,12942 | 0,31778 | €203,36 | €406,71 | €48,81 | €64,08 |
| Master Adaptive Gb20 V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,40304 | 0,40304 | 0,39140 | 0,20354 | 0,42632 | €848,64 | €1.697,27 | €49,02 | €0,00 |
| Master Adaptive Gb20 V1 | BANK | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,25875 | 0,29665 | 0,29430 | 0,13067 | 0,32085 | €200,57 | €401,14 | €0,00 | €58,75 |
| Master Adaptive Gb20 V1 | RIF | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,11127 | 0,10329 | 0,09792 | 0,05619 | 0,13797 | €200,57 | €401,13 | €48,14 | €-28,76 |
| Master Adaptive Runner25 V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39854 | 0,39854 | 0,38677 | 0,20126 | 0,43384 | €833,00 | €1.665,99 | €49,19 | €0,00 |
| Master Adaptive Runner25 V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,21338 | €203,80 | €407,60 | €48,91 | €0,00 |
| Master Adaptive Runner25 V1 | BANK | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,25383 | 0,29665 | 0,22337 | 0,12818 | 0,34521 | €202,68 | €405,37 | €48,64 | €68,38 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Rapida V3 — qualità completa + profit lock | RIF | LONG | 2026-07-24T11:02:58+00:00 | 0,10344 | €-49,71 | -1,01 | STOP |
| Rapida V3 — senza ESPORTS | RIF | LONG | 2026-07-24T11:02:58+00:00 | 0,10344 | €-50,53 | -1,01 | STOP |
| Rapida V3 — Long + no HIGH + score <7,5 | RIF | LONG | 2026-07-24T11:02:58+00:00 | 0,10344 | €-49,89 | -1,01 | STOP |
| Rapida V3 — Long Only | RIF | LONG | 2026-07-24T11:02:58+00:00 | 0,10344 | €-49,69 | -1,01 | STOP |
| Rapida V3 — no volatilità HIGH | RIF | LONG | 2026-07-24T11:02:58+00:00 | 0,10344 | €-50,39 | -1,01 | STOP |
| Rapida 1H V3 Filtered — madre | RIF | LONG | 2026-07-24T11:02:58+00:00 | 0,10344 | €-50,95 | -1,01 | STOP |
| Rapida V1 — target pieno 2R | RIF | LONG | 2026-07-24T11:02:58+00:00 | 0,10344 | €-50,22 | -1,01 | STOP |
| Rapida V1 — senza PEPE | RIF | LONG | 2026-07-24T11:02:58+00:00 | 0,10344 | €-50,57 | -1,01 | STOP |
| Rapida V1 — Long + BTC 1–3 + score <7,5 | RIF | LONG | 2026-07-24T11:02:58+00:00 | 0,10344 | €-50,31 | -1,01 | STOP |
| Rapida 1H V1 — madre | RIF | LONG | 2026-07-24T11:02:58+00:00 | 0,10344 | €-49,16 | -1,01 | STOP |
| Top 5 + BTC — solo MFE | BANK | LONG | 2026-07-24T06:53:35+00:00 | 0,23306 | €-56,71 | -1,16 | STOP_STRESS_SLIPPAGE |
| Top 5 + BTC — Guard + MFE | AKE | LONG | 2026-07-24T06:53:35+00:00 | 0,00233 | €-12,47 | -0,26 | STOP_GAP_STRESS |

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
| MAIN | Principale 4H | 45/30 | 18/30 | 0,96 | 0,91 | -0,02R | €-2,94 | 4,26% | COERENTE − | BOCCIATA RESEARCH |
| RSI_EXTREME_LONG_15M | Scalp RSI Long 25 · prudente · 5x (riferimento tra 9 varianti) | 8/30 | 4/30 | 0,30 | 0,22 | -0,56R | €-5,00 | 0,34% | COERENTE − | RACCOLTA RESEARCH |
| RSI_EXTREME_SHORT_15M | Scalp RSI Short 75 · prudente · 5x (riferimento tra 9 varianti) | 7/30 | 6/30 | 0,62 | 0,18 | -0,24R | €-5,86 | 0,36% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_1H_BALANCED | Bilanciata 1H V1 | 150/30 | 37/30 | 0,95 | 1,46 | -0,03R | €9,09 | 2,30% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_BALANCED_V2 | Bilanciata 1H V2 | 29/30 | 22/30 | 1,43 | 1,16 | 0,25R | €3,60 | 2,75% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_1H_BALANCED_V3 | Bilanciata 1H V3 Filtered | 56/30 | 31/30 | 1,11 | 1,30 | 0,07R | €7,87 | 2,20% | COERENTE + | PRONTA PER REVISIONE LIVE |
| SHADOW_1H_FAST | Rapida 1H V1 — madre | 176/30 | 66/30 | 0,88 | 0,88 | -0,08R | €-2,95 | 6,76% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | Rapida V1 — Long + BTC 1–3 + score <7,5 | 9/30 | 8/30 | 1,12 | 0,40 | 0,07R | €-13,43 | 1,55% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | Rapida V1 — no HIGH + score <7,5 | 40/30 | 28/30 | 0,81 | 1,00 | -0,13R | €-0,04 | 2,83% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_NO_PEPE_V1 | Rapida V1 — senza PEPE | 43/30 | 26/30 | 0,72 | 0,96 | -0,19R | €-0,92 | 2,10% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_V1 | Rapida V1 — score 6–7,5 | 28/30 | 27/30 | 1,00 | 1,22 | 0,00R | €4,27 | 2,49% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_TP2_V1 | Rapida V1 — target pieno 2R | 40/30 | 27/30 | 0,60 | 0,81 | -0,32R | €-4,55 | 2,58% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V2 | Rapida 1H V2 | 7/30 | 5/30 | 0,40 | 0,82 | -0,50R | €-3,78 | 1,69% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3 | Rapida 1H V3 Filtered — madre | 85/30 | 58/30 | 0,93 | 1,03 | -0,04R | €0,54 | 2,89% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_CAP75_V1 | Rapida V3 — score <7,5 | 36/30 | 23/30 | 0,76 | 1,10 | -0,17R | €2,19 | 2,49% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | Rapida V3 — qualità completa + profit lock | 20/30 | 19/30 | 0,73 | 0,62 | -0,19R | €-11,93 | 3,16% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | Rapida V3 — Long + no HIGH + score <7,5 | 20/30 | 19/30 | 0,73 | 0,66 | -0,19R | €-10,08 | 2,77% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | Rapida V3 — Long Only | 24/30 | 24/30 | 0,56 | 0,65 | -0,33R | €-9,62 | 3,31% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | Rapida V3 — no volatilità HIGH | 40/30 | 31/30 | 0,72 | 0,88 | -0,19R | €-2,88 | 2,96% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | Rapida V3 — senza ESPORTS | 41/30 | 30/30 | 0,69 | 0,90 | -0,22R | €-2,08 | 2,49% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_4H_WIDE | Ampia 4H | 42/30 | 13/30 | 0,97 | 1,09 | -0,03R | €2,74 | 2,71% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_BOLLINGER_MR_1H | Benchmark Bollinger mean reversion 1H | 35/30 | 25/30 | 1,12 | 1,52 | 0,07R | €9,29 | 2,06% | COERENTE + | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_BTC_ADAPTIVE_1H | Btc Adaptive 1H | 2/30 | 2/30 | 0,00 | 0,78 | -1,11R | €-5,87 | 0,89% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_ADAPTIVE_4H | Btc Adaptive 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,64% | n/a | RACCOLTA RESEARCH |
| SHADOW_BTC_BOLLINGER_1H | Btc Bollinger 1H | 2/30 | 2/30 | ∞ | ∞ | 1,37R | €49,98 | 0,31% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_BTC_BOLLINGER_4H | Btc Bollinger 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,30% | n/a | RACCOLTA RESEARCH |
| SHADOW_BTC_DONCHIAN_1H | Btc Donchian 1H | 3/30 | 3/30 | 0,00 | 0,43 | -1,12R | €-20,81 | 1,49% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_DONCHIAN_4H | Btc Donchian 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,68% | n/a | RACCOLTA RESEARCH |
| SHADOW_BTC_EMA_1H | Btc Ema 1H | 4/30 | 4/30 | 0,57 | 0,60 | -0,36R | €-16,40 | 1,56% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_EMA_4H | Btc Ema 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,68% | n/a | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE | Combo Adaptive — madre | 94/30 | 21/30 | 1,11 | 1,78 | 0,07R | €12,52 | 1,31% | COERENTE + | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | Combo Adaptive — Long Only | 24/30 | 5/30 | 0,61 | 0,42 | -0,30R | €-26,52 | 2,34% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | Combo Adaptive — MFE Trail esistente | 61/30 | 27/30 | 0,97 | 0,45 | -0,02R | €-11,76 | 4,11% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | Combo Adaptive — parziale 1R | 38/30 | 11/30 | 0,65 | 0,64 | -0,28R | €-12,79 | 2,24% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | Combo Adaptive — Quality7 + Regime + parziale 1R | 3/30 | 4/30 | 0,00 | 0,32 | -1,07R | €-27,31 | 1,95% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | Combo Adaptive — Quality7 + Regime | 3/30 | 4/30 | 0,00 | 0,18 | -1,07R | €-32,87 | 1,95% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | Combo Adaptive — Quality7 | 6/30 | 6/30 | 0,38 | 1,34 | -0,54R | €6,03 | 1,51% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | Combo Adaptive — Trend/Transition | 24/30 | 9/30 | 0,26 | 0,80 | -0,69R | €-6,15 | 2,18% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | Combo Adaptive — 75% a 2R + runner 3R | 28/30 | 13/30 | 0,46 | 0,83 | -0,50R | €-5,17 | 2,12% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | Combo Adaptive — target pieno 3R | 28/30 | 9/30 | 0,46 | 0,98 | -0,50R | €-0,50 | 1,41% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_MEAN_REVERSION | Combo Mean Reversion | 14/30 | 12/30 | 1,07 | 1,16 | 0,04R | €4,50 | 2,31% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_COMBO_SCANNER | Combo Scanner | 59/30 | 23/30 | 1,46 | 1,20 | 0,28R | €5,12 | 2,66% | COERENTE + | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_COMBO_TREND | Combo Trend | 72/30 | 25/30 | 1,03 | 0,82 | 0,02R | €-5,56 | 3,58% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_DOGE_BOLLINGER_1H | Doge Bollinger 1H | 1/30 | 1/30 | 0,00 | 0,00 | -1,13R | €-55,79 | 0,93% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_DOGE_DONCHIAN_1H | Doge Donchian 1H | 2/30 | 3/30 | 1,67 | 0,96 | 0,38R | €-0,85 | 0,96% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_DOGE_EMA_1H | Doge Ema 1H | 3/30 | 6/30 | 3,40 | 2,24 | 0,89R | €23,11 | 1,36% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_DONCHIAN_1H | Benchmark Donchian breakout 1H | 40/30 | 18/30 | 0,98 | 1,44 | -0,01R | €9,70 | 2,12% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_EMA_TREND_1H | Benchmark trend following EMA 1H | 78/30 | 17/30 | 1,01 | 0,88 | 0,00R | €-2,95 | 2,25% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_ETH_ADAPTIVE_1H | Eth Adaptive 1H | 4/30 | 4/30 | 0,57 | 0,16 | -0,36R | €-23,05 | 1,24% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_BOLLINGER_1H | Eth Bollinger 1H | 1/30 | 1/30 | 0,00 | ∞ | -1,13R | €15,45 | 0,51% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_ETH_DONCHIAN_1H | Eth Donchian 1H | 3/30 | 3/30 | 0,84 | 0,84 | -0,12R | €-5,82 | 1,38% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_EMA_1H | Eth Ema 1H | 4/30 | 6/30 | 0,57 | 0,25 | -0,36R | €-27,46 | 1,92% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_EMA_4H | Eth Ema 4H | 1/30 | 1/30 | 0,00 | 0,00 | -1,06R | €-52,88 | 0,68% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_GLOBAL_PURE | Global Confluence puro 1H | 3/30 | 8/30 | 3,47 | 0,45 | 0,91R | €-18,75 | 2,92% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | Master Adaptive Expanded V1 | 19/30 | 7/30 | 0,50 | 0,29 | -0,42R | €-32,57 | 2,80% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | Master Adaptive Gb20 V1 | 19/30 | 27/30 | 0,35 | 0,44 | -0,57R | €-13,21 | 4,16% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | Master Adaptive No Alt V1 | 19/30 | 5/30 | 0,35 | 0,00 | -0,57R | €-54,20 | 3,19% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | Master Adaptive Runner25 V1 | 14/30 | 5/30 | 0,22 | 0,00 | -0,77R | €-54,20 | 3,19% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | Master Adaptive Strict3 V1 | 19/30 | 13/30 | 0,35 | 0,29 | -0,57R | €-35,35 | 4,60% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_V1 | Master Adaptive V1 | 19/30 | 5/30 | 0,35 | 0,00 | -0,57R | €-54,20 | 3,19% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_RELATIVE_STRENGTH | Forza relativa 1H V1 | 105/30 | 23/30 | 0,96 | 0,83 | -0,03R | €-3,24 | 3,25% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_RELATIVE_STRENGTH_V2 | Forza relativa 1H V2 | 34/30 | 30/30 | 1,43 | 1,24 | 0,27R | €6,79 | 3,69% | COERENTE + | PRONTA PER REVISIONE LIVE |
| SHADOW_SCANNER_BOTTOM5_SHORT | Scanner Bottom 5 Short 1H | 37/30 | 22/30 | 0,77 | 0,61 | -0,15R | €-10,10 | 5,48% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC | Scanner Top 5 + forza BTC 1H | 58/30 | 22/30 | 1,40 | 1,96 | 0,24R | €17,32 | 2,01% | COERENTE + | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | Top 5 + BTC — BTC 2–3 | 10/30 | 3/30 | 0,86 | 0,54 | -0,10R | €-16,53 | 2,22% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | Top 5 + BTC — BTC≤3 | 17/30 | 4/30 | 0,64 | 0,73 | -0,29R | €-7,45 | 2,20% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | Top 5 + BTC — Guard + BTC≤3 + MFE | 12/30 | 13/30 | 0,71 | 0,41 | -0,22R | €-18,09 | 2,37% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | Top 5 + BTC — Guard + BTC≤3 | 12/30 | 4/30 | 0,71 | 0,99 | -0,22R | €-0,40 | 1,64% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | Top 5 + BTC — Guard + MFE | 15/30 | 16/30 | 0,53 | 0,32 | -0,39R | €-21,64 | 3,54% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | Top 5 + BTC — Guard | 15/30 | 7/30 | 0,53 | 0,41 | -0,39R | €-23,63 | 3,31% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | Top 5 + BTC — solo MFE | 20/30 | 11/30 | 0,68 | 0,17 | -0,25R | €-23,72 | 3,52% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | Top 5 + BTC — 75% a 2,2R + runner 3R | 14/30 | 8/30 | 0,46 | 1,59 | -0,49R | €11,95 | 2,33% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | Top 5 + BTC — target pieno 3R | 14/30 | 8/30 | 0,46 | 1,87 | -0,49R | €17,72 | 2,33% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_LONG | Scanner Top 5 Long 1H | 71/30 | 30/30 | 1,31 | 2,18 | 0,19R | €20,93 | 2,70% | COERENTE + | PRONTA PER REVISIONE LIVE |
| SHADOW_SOL_ADAPTIVE_1H | Sol Adaptive 1H | 3/30 | 3/30 | 0,86 | 0,34 | -0,11R | €-23,97 | 1,85% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_ADAPTIVE_4H | Sol Adaptive 4H | 1/30 | 1/30 | 0,00 | 0,00 | -1,05R | €-51,83 | 0,59% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_BOLLINGER_1H | Sol Bollinger 1H | 1/30 | 1/30 | 0,00 | 0,00 | -1,13R | €-55,79 | 0,81% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_BOLLINGER_4H | Sol Bollinger 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,40% | n/a | RACCOLTA RESEARCH |
| SHADOW_SOL_DONCHIAN_1H | Sol Donchian 1H | 2/30 | 2/30 | 0,00 | 0,41 | -1,12R | €-1,31 | 0,79% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_DONCHIAN_4H | Sol Donchian 4H | 1/30 | 1/30 | 0,00 | 0,00 | -1,06R | €-52,00 | 0,60% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_EMA_1H | Sol Ema 1H | 3/30 | 3/30 | 0,86 | 0,42 | -0,11R | €-20,89 | 1,67% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_EMA_4H | Sol Ema 4H | 1/30 | 1/30 | 0,00 | 0,00 | -1,06R | €-52,00 | 0,56% | COERENTE − | RACCOLTA RESEARCH |

Per le famiglie RSI con più configurazioni di leva o margine, il lato paper usa il conto con il maggior numero di eventi indipendenti; i conti duplicati non vengono aggregati.
`PRONTA PER REVISIONE LIVE` non invia ordini e non sposta capitale: abilita soltanto una revisione manuale finale.

## 🎯 DOGE Rejection Short — conto dedicato €3.600

Simulazione separata **paper only**: capitale/margine iniziale **€3.600**, leva **5x**, esposizione iniziale **€18.000**. Non modifica i conti paper da €10.000 e non invia ordini reali.

- Stato: **WAITING**
- Prezzo DOGE: **0.06982**
- Pre-allarme: **0.0765**; zona armata: **0.0775**; trigger rejection: **0.078**
- Invalidazione prima dell’entrata: chiusura 15m sopra **0.07966**

| Capitale iniziale | Balance | Equity | P&L aperto | Eventi chiusi | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- |
| €3.600,00 | €3.600,00 | €3.600,00 | €0,00 | 0 | 0,00% | 0,00 | 0,00% |

### Filtri correnti

| Filtro | Valore | Stato |
| --- | --- | --- |
| Dati mercato | FRESH | OK |
| Candela 15m | 18.3 min | OK |
| Global DOGE | -6.0 | OK |
| Classic raw | -11.0 | OK |
| DOGE/BTC raw | -6.0 | OK |
| Pattern ribassista | MATURO | OK |
| BTC sotto filtro | 64907.07 | OK |

### Ultima candela 15m valutata

- Rejection accettata: **NO**; motivo: **trigger_touched, entry_not_chased**
- High **0.06993**; close **0.06983**; wick alta **50.0%**; volume **x0.14**

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

- Regime: **TRANSITION**
- Famiglia: **TRANSITION**
- Confidenza: **78,00%**
- Volatilità: **NORMAL**
- Rotazione strategie: **SOLO OSSERVAZIONE — nessun peso operativo viene ancora modificato**
- Motivo: Segnali contrastanti tra trend BTC, breadth e forza delle altcoin.
- BTC trend score: **3,00**; ADX: **20,54**; breadth sopra EMA50: **25,00%**
- Mediana alt vs BTC: **-1,24%**; dispersione: **13,65%**

- Aperti in questo ciclo: **43**
- Chiusi in questo ciclo: **70**
- Posizioni research aperte: **438**
- Trade research chiusi: **2149**
- Eventi di mercato indipendenti chiusi: **606**
- Segnali sovrapposti saltati sullo stesso asset/profilo: **8606**
- Posizioni Research V1 senza regime scartate durante la migrazione: **28**

### Risultati complessivi per strategia

| Profilo | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| MAIN | 14 | 45 | 45 | 33,33% | 0,96 | -0,02R | €-10,84 |
| RSI_EXTREME_LONG_15M | 0 | 8 | 8 | 25,00% | 0,30 | -0,56R | €-45,05 |
| RSI_EXTREME_SHORT_15M | 0 | 7 | 7 | 28,57% | 0,62 | -0,24R | €-16,64 |
| Bilanciata 1H V1 | 15 | 150 | 150 | 33,33% | 0,95 | -0,03R | €-50,61 |
| Bilanciata 1H V2 | 8 | 33 | 29 | 42,42% | 1,43 | 0,25R | €83,04 |
| Bilanciata 1H V3 Filtered | 12 | 56 | 56 | 37,50% | 1,11 | 0,07R | €41,21 |
| Rapida 1H V1 | 10 | 176 | 176 | 38,07% | 0,88 | -0,08R | €-133,65 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | 2 | 9 | 9 | 44,44% | 1,12 | 0,07R | €6,06 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | 9 | 40 | 40 | 37,50% | 0,81 | -0,13R | €-51,07 |
| SHADOW_1H_FAST_NO_PEPE_V1 | 10 | 43 | 43 | 34,88% | 0,72 | -0,19R | €-83,81 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | 6 | 28 | 28 | 42,86% | 1,00 | 0,00R | €0,15 |
| SHADOW_1H_FAST_TP2_V1 | 11 | 40 | 40 | 25,00% | 0,60 | -0,32R | €-126,35 |
| Rapida 1H V2 | 0 | 8 | 7 | 25,00% | 0,40 | -0,50R | €-39,89 |
| Rapida 1H V3 Filtered | 7 | 85 | 85 | 40,00% | 0,93 | -0,04R | €-35,80 |
| SHADOW_1H_FAST_V3_CAP75_V1 | 6 | 36 | 36 | 36,11% | 0,76 | -0,17R | €-59,45 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | 1 | 20 | 20 | 35,00% | 0,73 | -0,19R | €-37,10 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | 1 | 20 | 20 | 35,00% | 0,73 | -0,19R | €-37,10 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | 2 | 24 | 24 | 29,17% | 0,56 | -0,33R | €-80,00 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | 7 | 40 | 40 | 35,00% | 0,72 | -0,19R | €-76,64 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | 7 | 41 | 41 | 34,15% | 0,69 | -0,22R | €-88,16 |
| SHADOW_4H_WIDE | 20 | 42 | 42 | 26,19% | 0,97 | -0,03R | €-10,68 |
| SHADOW_BOLLINGER_MR_1H | 2 | 35 | 35 | 45,71% | 1,12 | 0,07R | €24,02 |
| SHADOW_BTC_ADAPTIVE_1H | 1 | 2 | 2 | 0,00% | 0,00 | -1,11R | €-22,22 |
| SHADOW_BTC_ADAPTIVE_4H | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_BOLLINGER_1H | 0 | 2 | 2 | 100,00% | ∞ | 1,37R | €27,33 |
| SHADOW_BTC_BOLLINGER_4H | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_DONCHIAN_1H | 1 | 3 | 3 | 0,00% | 0,00 | -1,12R | €-33,75 |
| SHADOW_BTC_DONCHIAN_4H | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_EMA_1H | 1 | 4 | 4 | 25,00% | 0,57 | -0,36R | €-14,44 |
| SHADOW_BTC_EMA_4H | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_ADAPTIVE | 16 | 94 | 94 | 37,23% | 1,11 | 0,07R | €68,38 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | 5 | 24 | 24 | 25,00% | 0,61 | -0,30R | €-73,20 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | 16 | 61 | 61 | 34,43% | 0,97 | -0,02R | €-13,07 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | 13 | 38 | 38 | 26,32% | 0,65 | -0,28R | €-105,00 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | 3 | 3 | 3 | 0,00% | 0,00 | -1,07R | €-32,05 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | 3 | 3 | 3 | 0,00% | 0,00 | -1,07R | €-32,05 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | 5 | 6 | 6 | 16,67% | 0,38 | -0,54R | €-32,52 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | 7 | 24 | 24 | 12,50% | 0,26 | -0,69R | €-166,75 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | 14 | 28 | 28 | 14,29% | 0,46 | -0,50R | €-139,26 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | 14 | 28 | 28 | 14,29% | 0,46 | -0,50R | €-139,26 |
| SHADOW_COMBO_MEAN_REVERSION | 2 | 14 | 14 | 42,86% | 1,07 | 0,04R | €5,86 |
| SHADOW_COMBO_SCANNER | 7 | 59 | 59 | 42,37% | 1,46 | 0,28R | €165,49 |
| SHADOW_COMBO_TREND | 16 | 72 | 72 | 33,33% | 1,03 | 0,02R | €13,62 |
| SHADOW_DOGE_BOLLINGER_1H | 1 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,33 |
| SHADOW_DOGE_DONCHIAN_1H | 1 | 2 | 2 | 50,00% | 1,67 | 0,38R | €7,50 |
| SHADOW_DOGE_EMA_1H | 1 | 3 | 3 | 66,67% | 3,40 | 0,89R | €26,67 |
| SHADOW_DONCHIAN_1H | 11 | 40 | 40 | 30,00% | 0,98 | -0,01R | €-5,29 |
| SHADOW_EMA_TREND_1H | 17 | 78 | 78 | 32,05% | 1,01 | 0,00R | €3,53 |
| SHADOW_ETH_ADAPTIVE_1H | 0 | 4 | 4 | 25,00% | 0,57 | -0,36R | €-14,44 |
| SHADOW_ETH_BOLLINGER_1H | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,33 |
| SHADOW_ETH_DONCHIAN_1H | 0 | 3 | 3 | 33,33% | 0,84 | -0,12R | €-3,61 |
| SHADOW_ETH_EMA_1H | 0 | 4 | 4 | 25,00% | 0,57 | -0,36R | €-14,33 |
| SHADOW_ETH_EMA_4H | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,57 |
| SHADOW_GLOBAL_PURE | 1 | 3 | 3 | 66,67% | 3,47 | 0,91R | €27,17 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | 6 | 19 | 19 | 21,05% | 0,50 | -0,42R | €-79,81 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | 6 | 19 | 19 | 15,79% | 0,35 | -0,57R | €-109,02 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | 6 | 19 | 19 | 15,79% | 0,35 | -0,57R | €-108,88 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | 6 | 14 | 14 | 7,14% | 0,22 | -0,77R | €-108,31 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | 3 | 19 | 19 | 15,79% | 0,35 | -0,57R | €-108,74 |
| SHADOW_MASTER_ADAPTIVE_V1 | 6 | 19 | 19 | 15,79% | 0,35 | -0,57R | €-109,02 |
| Forza relativa 1H V1 | 14 | 105 | 105 | 30,48% | 0,96 | -0,03R | €-26,88 |
| Forza relativa 1H V2 | 8 | 37 | 34 | 40,54% | 1,43 | 0,27R | €98,58 |
| SHADOW_SCANNER_BOTTOM5_SHORT | 9 | 37 | 37 | 27,03% | 0,77 | -0,15R | €-56,93 |
| SHADOW_SCANNER_TOP5_BTC | 6 | 58 | 58 | 39,66% | 1,40 | 0,24R | €141,64 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | 5 | 10 | 10 | 30,00% | 0,86 | -0,10R | €-10,17 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | 5 | 17 | 17 | 23,53% | 0,64 | -0,29R | €-49,18 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | 4 | 12 | 12 | 25,00% | 0,71 | -0,22R | €-26,34 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | 4 | 12 | 12 | 25,00% | 0,71 | -0,22R | €-26,34 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | 4 | 15 | 15 | 20,00% | 0,53 | -0,39R | €-58,92 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | 4 | 15 | 15 | 20,00% | 0,53 | -0,39R | €-58,92 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | 6 | 20 | 20 | 25,00% | 0,68 | -0,25R | €-50,05 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | 6 | 14 | 14 | 14,29% | 0,46 | -0,49R | €-68,15 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | 6 | 14 | 14 | 14,29% | 0,46 | -0,49R | €-68,15 |
| SHADOW_SCANNER_TOP5_LONG | 6 | 71 | 71 | 40,85% | 1,31 | 0,19R | €135,81 |
| SHADOW_SOL_ADAPTIVE_1H | 2 | 3 | 3 | 33,33% | 0,86 | -0,11R | €-3,18 |
| SHADOW_SOL_ADAPTIVE_4H | 1 | 1 | 1 | 0,00% | 0,00 | -1,05R | €-10,52 |
| SHADOW_SOL_BOLLINGER_1H | 1 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,33 |
| SHADOW_SOL_BOLLINGER_4H | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SOL_DONCHIAN_1H | 1 | 2 | 2 | 0,00% | 0,00 | -1,12R | €-22,33 |
| SHADOW_SOL_DONCHIAN_4H | 1 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,56 |
| SHADOW_SOL_EMA_1H | 1 | 3 | 3 | 33,33% | 0,86 | -0,11R | €-3,18 |
| SHADOW_SOL_EMA_4H | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,56 |

### Matrice strategia × regime all’entrata

| Profilo | Regime entrata | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| MAIN | ALT_ROTATION_DOWN | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| MAIN | ALT_ROTATION_UP | 3 | 3 | 3 | 0,00% | 0,00 | -1,01R | €-30,40 |
| MAIN | RANGE | 4 | 15 | 15 | 26,67% | 0,70 | -0,23R | €-33,95 |
| MAIN | RANGE_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| MAIN | TRANSITION | 1 | 7 | 7 | 42,86% | 1,45 | 0,26R | €18,34 |
| MAIN | TREND_UP | 1 | 16 | 16 | 37,50% | 1,15 | 0,10R | €15,71 |
| MAIN | TREND_UP_HIGH_VOL | 3 | 3 | 3 | 33,33% | 0,98 | -0,01R | €-0,40 |
| RSI_EXTREME_LONG_15M | RANGE | 0 | 6 | 6 | 0,00% | 0,00 | -1,07R | €-64,49 |
| RSI_EXTREME_LONG_15M | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,29R | €12,88 |
| RSI_EXTREME_LONG_15M | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 0,66R | €6,56 |
| RSI_EXTREME_SHORT_15M | ALT_ROTATION_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 1,47R | €14,67 |
| RSI_EXTREME_SHORT_15M | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,90 |
| RSI_EXTREME_SHORT_15M | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -0,41R | €-4,13 |
| RSI_EXTREME_SHORT_15M | TREND_UP | 0 | 4 | 4 | 25,00% | 0,44 | -0,41R | €-16,27 |
| Bilanciata 1H V1 | ALT_ROTATION_DOWN | 2 | 10 | 10 | 30,00% | 0,77 | -0,17R | €-17,14 |
| Bilanciata 1H V1 | ALT_ROTATION_UP | 0 | 14 | 14 | 50,00% | 1,84 | 0,44R | €61,99 |
| Bilanciata 1H V1 | RANGE | 8 | 33 | 33 | 33,33% | 0,96 | -0,02R | €-8,15 |
| Bilanciata 1H V1 | RANGE_HIGH_VOL | 0 | 11 | 11 | 0,00% | 0,00 | -1,07R | €-118,08 |
| Bilanciata 1H V1 | TRANSITION | 1 | 29 | 29 | 31,03% | 0,90 | -0,07R | €-19,92 |
| Bilanciata 1H V1 | TREND_UP | 2 | 42 | 42 | 40,48% | 1,31 | 0,19R | €78,29 |
| Bilanciata 1H V1 | TREND_UP_HIGH_VOL | 2 | 11 | 11 | 27,27% | 0,68 | -0,25R | €-27,61 |
| Bilanciata 1H V2 | ALT_ROTATION_UP | 0 | 6 | 5 | 66,67% | 3,52 | 0,92R | €55,11 |
| Bilanciata 1H V2 | RANGE | 3 | 12 | 10 | 33,33% | 1,05 | 0,03R | €3,48 |
| Bilanciata 1H V2 | TRANSITION | 5 | 15 | 14 | 40,00% | 1,26 | 0,16R | €24,46 |
| Bilanciata 1H V3 Filtered | ALT_ROTATION_DOWN | 2 | 8 | 8 | 37,50% | 1,11 | 0,07R | €5,51 |
| Bilanciata 1H V3 Filtered | ALT_ROTATION_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,05R | €-20,99 |
| Bilanciata 1H V3 Filtered | RANGE | 6 | 5 | 5 | 60,00% | 2,88 | 0,77R | €38,27 |
| Bilanciata 1H V3 Filtered | RANGE_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,83 |
| Bilanciata 1H V3 Filtered | TRANSITION | 0 | 8 | 8 | 37,50% | 1,11 | 0,07R | €5,68 |
| Bilanciata 1H V3 Filtered | TREND_UP | 1 | 20 | 20 | 45,00% | 1,54 | 0,31R | €61,36 |
| Bilanciata 1H V3 Filtered | TREND_UP_HIGH_VOL | 3 | 11 | 11 | 27,27% | 0,68 | -0,25R | €-27,79 |
| Rapida 1H V1 | ALT_ROTATION_DOWN | 3 | 14 | 14 | 21,43% | 0,36 | -0,53R | €-73,80 |
| Rapida 1H V1 | ALT_ROTATION_UP | 0 | 13 | 13 | 53,85% | 1,58 | 0,29R | €37,18 |
| Rapida 1H V1 | RANGE | 6 | 44 | 44 | 43,18% | 1,16 | 0,08R | €36,51 |
| Rapida 1H V1 | RANGE_HIGH_VOL | 0 | 11 | 11 | 0,00% | 0,00 | -1,09R | €-119,90 |
| Rapida 1H V1 | TRANSITION | 1 | 25 | 25 | 48,00% | 1,45 | 0,22R | €54,11 |
| Rapida 1H V1 | TREND_UP | 0 | 48 | 48 | 41,67% | 0,97 | -0,02R | €-9,20 |
| Rapida 1H V1 | TREND_UP_HIGH_VOL | 0 | 21 | 21 | 28,57% | 0,59 | -0,28R | €-58,55 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | ALT_ROTATION_DOWN | 1 | 3 | 3 | 0,00% | 0,00 | -1,02R | €-30,49 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,39R | €13,89 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | RANGE | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 1,48R | €29,69 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TREND_UP | 0 | 3 | 3 | 33,33% | 0,68 | -0,23R | €-7,03 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | ALT_ROTATION_DOWN | 3 | 13 | 13 | 23,08% | 0,40 | -0,48R | €-62,34 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,39R | €13,89 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | RANGE | 6 | 8 | 8 | 62,50% | 2,25 | 0,50R | €39,89 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 1,48R | €29,69 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TREND_UP | 0 | 16 | 16 | 25,00% | 0,44 | -0,45R | €-72,21 |
| SHADOW_1H_FAST_NO_PEPE_V1 | ALT_ROTATION_DOWN | 3 | 13 | 13 | 23,08% | 0,40 | -0,48R | €-62,37 |
| SHADOW_1H_FAST_NO_PEPE_V1 | ALT_ROTATION_UP | 0 | 6 | 6 | 50,00% | 1,27 | 0,15R | €8,94 |
| SHADOW_1H_FAST_NO_PEPE_V1 | RANGE | 6 | 8 | 8 | 50,00% | 1,35 | 0,19R | €14,83 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TRANSITION | 1 | 2 | 2 | 100,00% | ∞ | 1,48R | €29,69 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_UP | 0 | 14 | 14 | 21,43% | 0,36 | -0,54R | €-74,90 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | ALT_ROTATION_DOWN | 2 | 8 | 8 | 37,50% | 0,79 | -0,14R | €-11,04 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | ALT_ROTATION_UP | 0 | 4 | 4 | 50,00% | 1,23 | 0,13R | €5,07 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | RANGE | 4 | 7 | 7 | 71,43% | 3,57 | 0,75R | €52,41 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_UP | 0 | 8 | 8 | 12,50% | 0,18 | -0,76R | €-61,17 |
| SHADOW_1H_FAST_TP2_V1 | ALT_ROTATION_DOWN | 3 | 13 | 13 | 15,38% | 0,33 | -0,59R | €-76,16 |
| SHADOW_1H_FAST_TP2_V1 | ALT_ROTATION_UP | 0 | 4 | 4 | 25,00% | 0,55 | -0,37R | €-14,93 |
| SHADOW_1H_FAST_TP2_V1 | RANGE | 6 | 8 | 8 | 37,50% | 1,10 | 0,07R | €5,36 |
| SHADOW_1H_FAST_TP2_V1 | TRANSITION | 2 | 1 | 1 | 100,00% | ∞ | 1,98R | €19,82 |
| SHADOW_1H_FAST_TP2_V1 | TREND_UP | 0 | 14 | 14 | 21,43% | 0,49 | -0,43R | €-60,45 |
| Rapida 1H V2 | ALT_ROTATION_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,10R | €-21,92 |
| Rapida 1H V2 | RANGE | 0 | 5 | 4 | 40,00% | 0,81 | -0,13R | €-6,55 |
| Rapida 1H V2 | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -1,14R | €-11,43 |
| Rapida 1H V3 Filtered | ALT_ROTATION_DOWN | 2 | 14 | 14 | 21,43% | 0,36 | -0,52R | €-73,25 |
| Rapida 1H V3 Filtered | ALT_ROTATION_UP | 0 | 5 | 5 | 60,00% | 1,92 | 0,41R | €20,43 |
| Rapida 1H V3 Filtered | RANGE | 4 | 10 | 10 | 60,00% | 2,06 | 0,44R | €44,36 |
| Rapida 1H V3 Filtered | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| Rapida 1H V3 Filtered | TRANSITION | 1 | 6 | 6 | 50,00% | 1,37 | 0,20R | €12,10 |
| Rapida 1H V3 Filtered | TREND_UP | 0 | 29 | 29 | 48,28% | 1,27 | 0,15R | €43,00 |
| Rapida 1H V3 Filtered | TREND_UP_HIGH_VOL | 0 | 20 | 20 | 25,00% | 0,49 | -0,36R | €-72,31 |
| SHADOW_1H_FAST_V3_CAP75_V1 | ALT_ROTATION_DOWN | 2 | 12 | 12 | 25,00% | 0,45 | -0,43R | €-51,65 |
| SHADOW_1H_FAST_V3_CAP75_V1 | ALT_ROTATION_UP | 0 | 4 | 4 | 50,00% | 1,23 | 0,13R | €5,07 |
| SHADOW_1H_FAST_V3_CAP75_V1 | RANGE | 4 | 8 | 8 | 62,50% | 2,29 | 0,51R | €40,98 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_UP | 0 | 11 | 11 | 18,18% | 0,29 | -0,62R | €-68,73 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | ALT_ROTATION_DOWN | 0 | 5 | 5 | 0,00% | 0,00 | -1,04R | €-52,05 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,39R | €13,89 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | RANGE | 1 | 6 | 6 | 66,67% | 2,90 | 0,65R | €38,84 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TREND_UP | 0 | 7 | 7 | 14,29% | 0,20 | -0,75R | €-52,65 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | ALT_ROTATION_DOWN | 0 | 5 | 5 | 0,00% | 0,00 | -1,04R | €-52,05 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,39R | €13,89 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | RANGE | 1 | 6 | 6 | 66,67% | 2,90 | 0,65R | €38,84 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TREND_UP | 0 | 7 | 7 | 14,29% | 0,20 | -0,75R | €-52,65 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 0 | 6 | 6 | 0,00% | 0,00 | -1,04R | €-62,22 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | ALT_ROTATION_UP | 0 | 4 | 4 | 50,00% | 1,23 | 0,13R | €5,07 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | RANGE | 1 | 7 | 7 | 57,14% | 1,94 | 0,41R | €28,65 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TRANSITION | 1 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_UP | 0 | 6 | 6 | 0,00% | 0,00 | -1,11R | €-66,36 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | ALT_ROTATION_DOWN | 2 | 13 | 13 | 23,08% | 0,40 | -0,48R | €-61,82 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | ALT_ROTATION_UP | 0 | 2 | 2 | 50,00% | 1,27 | 0,15R | €3,00 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | RANGE | 4 | 10 | 10 | 60,00% | 2,06 | 0,44R | €44,36 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TRANSITION | 1 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TREND_UP | 0 | 14 | 14 | 21,43% | 0,35 | -0,55R | €-77,05 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | ALT_ROTATION_DOWN | 2 | 13 | 13 | 23,08% | 0,40 | -0,48R | €-61,82 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | ALT_ROTATION_UP | 0 | 5 | 5 | 40,00% | 0,83 | -0,12R | €-5,83 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | RANGE | 4 | 10 | 10 | 60,00% | 2,06 | 0,44R | €44,36 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TRANSITION | 1 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_UP | 0 | 12 | 12 | 16,67% | 0,26 | -0,66R | €-79,74 |
| SHADOW_4H_WIDE | ALT_ROTATION_DOWN | 4 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_4H_WIDE | ALT_ROTATION_UP | 2 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_4H_WIDE | RANGE | 4 | 16 | 16 | 25,00% | 0,90 | -0,07R | €-11,95 |
| SHADOW_4H_WIDE | TRANSITION | 3 | 7 | 7 | 14,29% | 0,46 | -0,47R | €-33,10 |
| SHADOW_4H_WIDE | TREND_UP | 3 | 13 | 13 | 46,15% | 2,32 | 0,73R | €95,17 |
| SHADOW_4H_WIDE | TREND_UP_HIGH_VOL | 4 | 4 | 4 | 0,00% | 0,00 | -1,01R | €-40,53 |
| SHADOW_BOLLINGER_MR_1H | ALT_ROTATION_DOWN | 0 | 5 | 5 | 60,00% | 1,99 | 0,43R | €21,52 |
| SHADOW_BOLLINGER_MR_1H | ALT_ROTATION_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,02R | €-20,30 |
| SHADOW_BOLLINGER_MR_1H | RANGE | 2 | 10 | 10 | 40,00% | 0,88 | -0,08R | €-7,56 |
| SHADOW_BOLLINGER_MR_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_BOLLINGER_MR_1H | TRANSITION | 0 | 3 | 3 | 33,33% | 0,71 | -0,20R | €-6,14 |
| SHADOW_BOLLINGER_MR_1H | TREND_UP | 0 | 12 | 12 | 50,00% | 1,28 | 0,15R | €18,32 |
| SHADOW_BOLLINGER_MR_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,31 | 0,17R | €3,31 |
| SHADOW_BTC_ADAPTIVE_1H | RANGE | 0 | 2 | 2 | 0,00% | 0,00 | -1,11R | €-22,22 |
| SHADOW_BTC_ADAPTIVE_1H | TREND_UP_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_ADAPTIVE_4H | TREND_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_BOLLINGER_1H | RANGE | 0 | 1 | 1 | 100,00% | ∞ | 1,37R | €13,67 |
| SHADOW_BTC_BOLLINGER_1H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,37R | €13,67 |
| SHADOW_BTC_BOLLINGER_4H | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_DONCHIAN_1H | RANGE | 0 | 2 | 2 | 0,00% | 0,00 | -1,12R | €-22,50 |
| SHADOW_BTC_DONCHIAN_1H | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -1,12R | €-11,25 |
| SHADOW_BTC_DONCHIAN_1H | TREND_UP_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_DONCHIAN_4H | TREND_UP_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_EMA_1H | RANGE | 1 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_BTC_EMA_1H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_BTC_EMA_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,70 | 0,39R | €7,78 |
| SHADOW_BTC_EMA_4H | TREND_UP_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_ADAPTIVE | ALT_ROTATION_DOWN | 3 | 9 | 9 | 22,22% | 0,52 | -0,40R | €-35,62 |
| SHADOW_COMBO_ADAPTIVE | ALT_ROTATION_UP | 0 | 6 | 6 | 50,00% | 1,86 | 0,45R | €26,75 |
| SHADOW_COMBO_ADAPTIVE | RANGE | 7 | 20 | 20 | 35,00% | 0,98 | -0,01R | €-2,54 |
| SHADOW_COMBO_ADAPTIVE | RANGE_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,83 |
| SHADOW_COMBO_ADAPTIVE | TRANSITION | 1 | 19 | 19 | 42,11% | 1,46 | 0,26R | €49,12 |
| SHADOW_COMBO_ADAPTIVE | TREND_UP | 2 | 29 | 29 | 44,83% | 1,52 | 0,30R | €87,02 |
| SHADOW_COMBO_ADAPTIVE | TREND_UP_HIGH_VOL | 3 | 9 | 9 | 22,22% | 0,52 | -0,39R | €-35,52 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 1 | 3 | 3 | 0,00% | 0,00 | -1,01R | €-30,42 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | ALT_ROTATION_UP | 0 | 4 | 4 | 75,00% | 5,34 | 1,17R | €46,86 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | RANGE | 1 | 5 | 5 | 40,00% | 1,30 | 0,19R | €9,27 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TRANSITION | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_UP | 2 | 6 | 6 | 0,00% | 0,00 | -1,09R | €-65,26 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_UP_HIGH_VOL | 0 | 6 | 6 | 16,67% | 0,36 | -0,56R | €-33,65 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | ALT_ROTATION_DOWN | 3 | 9 | 9 | 22,22% | 0,52 | -0,40R | €-35,62 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | ALT_ROTATION_UP | 0 | 7 | 7 | 42,86% | 1,37 | 0,22R | €15,64 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE | 7 | 8 | 8 | 50,00% | 1,86 | 0,45R | €35,94 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,83 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TRANSITION | 1 | 3 | 3 | 33,33% | 0,87 | -0,09R | €-2,74 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_UP | 2 | 21 | 21 | 42,86% | 1,42 | 0,25R | €52,12 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_UP_HIGH_VOL | 3 | 11 | 11 | 18,18% | 0,40 | -0,52R | €-57,58 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | ALT_ROTATION_DOWN | 3 | 9 | 9 | 22,22% | 0,52 | -0,40R | €-35,62 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | ALT_ROTATION_UP | 0 | 4 | 4 | 75,00% | 5,34 | 1,17R | €46,86 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | RANGE | 7 | 8 | 8 | 50,00% | 1,86 | 0,45R | €35,94 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TRANSITION | 1 | 2 | 2 | 0,00% | 0,00 | -1,09R | €-21,86 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_UP | 2 | 8 | 8 | 0,00% | 0,00 | -1,07R | €-85,56 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_UP_HIGH_VOL | 0 | 7 | 7 | 14,29% | 0,30 | -0,64R | €-44,76 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TRANSITION | 2 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,86 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TREND_UP | 1 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,18 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TRANSITION | 2 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,86 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TREND_UP | 1 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,18 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | ALT_ROTATION_DOWN | 2 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,84 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | RANGE | 1 | 3 | 3 | 33,33% | 0,98 | -0,02R | €-0,50 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TRANSITION | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,18 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TRANSITION | 5 | 3 | 3 | 0,00% | 0,00 | -1,09R | €-32,68 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TREND_UP | 2 | 13 | 13 | 15,38% | 0,33 | -0,60R | €-78,20 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TREND_UP_HIGH_VOL | 0 | 8 | 8 | 12,50% | 0,26 | -0,70R | €-55,87 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_DOWN | 3 | 5 | 5 | 20,00% | 0,67 | -0,29R | €-14,37 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_UP | 0 | 5 | 5 | 40,00% | 1,80 | 0,52R | €26,25 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | RANGE | 9 | 5 | 5 | 20,00% | 0,69 | -0,25R | €-12,68 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | TRANSITION | 0 | 2 | 2 | 0,00% | 0,00 | -1,09R | €-21,86 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | TREND_UP | 2 | 7 | 7 | 0,00% | 0,00 | -1,06R | €-74,11 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 0,00% | 0,00 | -1,06R | €-42,49 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | ALT_ROTATION_DOWN | 3 | 5 | 5 | 20,00% | 0,67 | -0,29R | €-14,37 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | ALT_ROTATION_UP | 0 | 5 | 5 | 40,00% | 1,80 | 0,52R | €26,25 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | RANGE | 9 | 5 | 5 | 20,00% | 0,69 | -0,25R | €-12,68 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | TRANSITION | 0 | 2 | 2 | 0,00% | 0,00 | -1,09R | €-21,86 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | TREND_UP | 2 | 7 | 7 | 0,00% | 0,00 | -1,06R | €-74,11 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 0,00% | 0,00 | -1,06R | €-42,49 |
| SHADOW_COMBO_MEAN_REVERSION | ALT_ROTATION_DOWN | 0 | 3 | 3 | 33,33% | 0,73 | -0,19R | €-5,83 |
| SHADOW_COMBO_MEAN_REVERSION | RANGE | 2 | 6 | 6 | 50,00% | 1,39 | 0,21R | €12,69 |
| SHADOW_COMBO_MEAN_REVERSION | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,94 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_UP | 0 | 3 | 3 | 33,33% | 0,75 | -0,17R | €-5,09 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,85 |
| SHADOW_COMBO_SCANNER | ALT_ROTATION_DOWN | 1 | 4 | 4 | 0,00% | 0,00 | -1,04R | €-41,53 |
| SHADOW_COMBO_SCANNER | ALT_ROTATION_UP | 0 | 4 | 4 | 50,00% | 2,09 | 0,57R | €22,81 |
| SHADOW_COMBO_SCANNER | RANGE | 2 | 8 | 8 | 50,00% | 2,09 | 0,56R | €44,63 |
| SHADOW_COMBO_SCANNER | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,69 |
| SHADOW_COMBO_SCANNER | TRANSITION | 1 | 14 | 14 | 42,86% | 1,34 | 0,21R | €28,81 |
| SHADOW_COMBO_SCANNER | TREND_UP | 2 | 20 | 20 | 50,00% | 2,04 | 0,55R | €110,63 |
| SHADOW_COMBO_SCANNER | TREND_UP_HIGH_VOL | 1 | 8 | 8 | 37,50% | 1,20 | 0,14R | €10,84 |
| SHADOW_COMBO_TREND | ALT_ROTATION_DOWN | 4 | 5 | 5 | 20,00% | 0,50 | -0,42R | €-21,22 |
| SHADOW_COMBO_TREND | ALT_ROTATION_UP | 0 | 5 | 5 | 40,00% | 1,39 | 0,24R | €12,22 |
| SHADOW_COMBO_TREND | RANGE | 5 | 16 | 16 | 31,25% | 0,93 | -0,05R | €-8,19 |
| SHADOW_COMBO_TREND | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,63 |
| SHADOW_COMBO_TREND | TRANSITION | 2 | 14 | 14 | 42,86% | 1,55 | 0,33R | €46,22 |
| SHADOW_COMBO_TREND | TREND_UP | 2 | 23 | 23 | 34,78% | 1,10 | 0,07R | €15,44 |
| SHADOW_COMBO_TREND | TREND_UP_HIGH_VOL | 3 | 8 | 8 | 25,00% | 0,68 | -0,25R | €-20,22 |
| SHADOW_DOGE_BOLLINGER_1H | RANGE | 1 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,33 |
| SHADOW_DOGE_DONCHIAN_1H | RANGE | 1 | 2 | 2 | 50,00% | 1,67 | 0,38R | €7,50 |
| SHADOW_DOGE_EMA_1H | RANGE | 1 | 3 | 3 | 66,67% | 3,40 | 0,89R | €26,67 |
| SHADOW_DONCHIAN_1H | ALT_ROTATION_DOWN | 4 | 4 | 4 | 25,00% | 0,77 | -0,18R | €-7,22 |
| SHADOW_DONCHIAN_1H | ALT_ROTATION_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,85 |
| SHADOW_DONCHIAN_1H | RANGE | 3 | 12 | 12 | 25,00% | 0,76 | -0,19R | €-22,61 |
| SHADOW_DONCHIAN_1H | RANGE_HIGH_VOL | 1 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_DONCHIAN_1H | TRANSITION | 1 | 6 | 6 | 16,67% | 0,45 | -0,48R | €-28,95 |
| SHADOW_DONCHIAN_1H | TREND_UP | 0 | 11 | 11 | 45,45% | 1,89 | 0,53R | €57,82 |
| SHADOW_DONCHIAN_1H | TREND_UP_HIGH_VOL | 2 | 4 | 4 | 50,00% | 2,23 | 0,67R | €26,65 |
| SHADOW_EMA_TREND_1H | ALT_ROTATION_DOWN | 3 | 6 | 6 | 16,67% | 0,40 | -0,53R | €-31,76 |
| SHADOW_EMA_TREND_1H | ALT_ROTATION_UP | 0 | 5 | 5 | 20,00% | 0,52 | -0,40R | €-20,11 |
| SHADOW_EMA_TREND_1H | RANGE | 6 | 16 | 16 | 31,25% | 1,03 | 0,02R | €3,11 |
| SHADOW_EMA_TREND_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,63 |
| SHADOW_EMA_TREND_1H | TRANSITION | 3 | 14 | 14 | 42,86% | 1,55 | 0,33R | €46,21 |
| SHADOW_EMA_TREND_1H | TREND_UP | 2 | 28 | 28 | 32,14% | 1,02 | 0,02R | €4,61 |
| SHADOW_EMA_TREND_1H | TREND_UP_HIGH_VOL | 3 | 8 | 8 | 37,50% | 1,23 | 0,15R | €12,10 |
| SHADOW_ETH_ADAPTIVE_1H | ALT_ROTATION_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_ETH_ADAPTIVE_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_ETH_ADAPTIVE_1H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,89R | €18,89 |
| SHADOW_ETH_ADAPTIVE_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_ETH_BOLLINGER_1H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,33 |
| SHADOW_ETH_DONCHIAN_1H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_ETH_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,68 | 0,38R | €7,64 |
| SHADOW_ETH_EMA_1H | ALT_ROTATION_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_ETH_EMA_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_ETH_EMA_1H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,89R | €18,89 |
| SHADOW_ETH_EMA_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,10R | €-10,99 |
| SHADOW_ETH_EMA_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,57 |
| SHADOW_GLOBAL_PURE | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,10R | €-11,00 |
| SHADOW_GLOBAL_PURE | RANGE | 1 | 1 | 1 | 100,00% | ∞ | 2,40R | €24,00 |
| SHADOW_GLOBAL_PURE | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,42R | €14,17 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | ALT_ROTATION_DOWN | 3 | 4 | 4 | 0,00% | 0,00 | -1,04R | €-41,53 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,79 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | RANGE | 0 | 4 | 4 | 25,00% | 0,65 | -0,26R | €-10,60 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TRANSITION | 1 | 2 | 2 | 100,00% | ∞ | 1,94R | €38,87 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TREND_UP | 2 | 8 | 8 | 12,50% | 0,26 | -0,70R | €-55,77 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | ALT_ROTATION_DOWN | 3 | 3 | 3 | 0,00% | 0,00 | -1,01R | €-30,42 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,86 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | RANGE | 0 | 5 | 5 | 40,00% | 1,30 | 0,19R | €9,27 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TRANSITION | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TREND_UP | 2 | 10 | 10 | 10,00% | 0,21 | -0,77R | €-77,01 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | ALT_ROTATION_DOWN | 3 | 3 | 3 | 0,00% | 0,00 | -1,01R | €-30,42 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | RANGE | 0 | 5 | 5 | 40,00% | 1,30 | 0,19R | €9,27 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TRANSITION | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TREND_UP | 2 | 11 | 11 | 9,09% | 0,18 | -0,80R | €-87,73 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_DOWN | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,86 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | RANGE | 2 | 3 | 3 | 0,00% | 0,00 | -1,01R | €-30,44 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | TREND_UP | 2 | 10 | 10 | 10,00% | 0,31 | -0,67R | €-67,01 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | ALT_ROTATION_DOWN | 0 | 3 | 3 | 0,00% | 0,00 | -1,01R | €-30,42 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | RANGE | 1 | 6 | 6 | 50,00% | 1,96 | 0,49R | €29,12 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TRANSITION | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TREND_UP | 1 | 10 | 10 | 0,00% | 0,00 | -1,07R | €-107,43 |
| SHADOW_MASTER_ADAPTIVE_V1 | ALT_ROTATION_DOWN | 3 | 3 | 3 | 0,00% | 0,00 | -1,01R | €-30,42 |
| SHADOW_MASTER_ADAPTIVE_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,86 |
| SHADOW_MASTER_ADAPTIVE_V1 | RANGE | 0 | 5 | 5 | 40,00% | 1,30 | 0,19R | €9,27 |
| SHADOW_MASTER_ADAPTIVE_V1 | TRANSITION | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_MASTER_ADAPTIVE_V1 | TREND_UP | 2 | 10 | 10 | 10,00% | 0,21 | -0,77R | €-77,01 |
| Forza relativa 1H V1 | ALT_ROTATION_DOWN | 5 | 5 | 5 | 0,00% | 0,00 | -1,05R | €-52,34 |
| Forza relativa 1H V1 | ALT_ROTATION_UP | 0 | 13 | 13 | 30,77% | 0,90 | -0,07R | €-9,26 |
| Forza relativa 1H V1 | RANGE | 5 | 25 | 25 | 24,00% | 0,69 | -0,24R | €-58,81 |
| Forza relativa 1H V1 | RANGE_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -1,03R | €-31,02 |
| Forza relativa 1H V1 | TRANSITION | 1 | 15 | 15 | 46,67% | 1,84 | 0,46R | €69,26 |
| Forza relativa 1H V1 | TREND_UP | 2 | 36 | 36 | 38,89% | 1,54 | 0,30R | €106,45 |
| Forza relativa 1H V1 | TREND_UP_HIGH_VOL | 1 | 8 | 8 | 12,50% | 0,30 | -0,64R | €-51,15 |
| Forza relativa 1H V2 | ALT_ROTATION_DOWN | 4 | 3 | 3 | 33,33% | 1,04 | 0,03R | €0,86 |
| Forza relativa 1H V2 | ALT_ROTATION_UP | 0 | 4 | 4 | 50,00% | 2,00 | 0,54R | €21,41 |
| Forza relativa 1H V2 | RANGE | 0 | 6 | 6 | 66,67% | 4,31 | 1,12R | €67,19 |
| Forza relativa 1H V2 | TRANSITION | 4 | 9 | 8 | 33,33% | 1,05 | 0,03R | €3,12 |
| Forza relativa 1H V2 | TREND_UP | 0 | 11 | 10 | 45,45% | 1,77 | 0,43R | €47,60 |
| Forza relativa 1H V2 | TREND_UP_HIGH_VOL | 0 | 4 | 3 | 0,00% | 0,00 | -1,04R | €-41,60 |
| SHADOW_SCANNER_BOTTOM5_SHORT | ALT_ROTATION_DOWN | 1 | 4 | 4 | 75,00% | 5,32 | 1,17R | €46,61 |
| SHADOW_SCANNER_BOTTOM5_SHORT | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| SHADOW_SCANNER_BOTTOM5_SHORT | RANGE | 7 | 9 | 9 | 22,22% | 0,50 | -0,42R | €-37,98 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TRANSITION | 0 | 14 | 14 | 28,57% | 0,85 | -0,09R | €-13,14 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP | 0 | 7 | 7 | 0,00% | 0,00 | -0,73R | €-51,04 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP_HIGH_VOL | 1 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,24 |
| SHADOW_SCANNER_TOP5_BTC | ALT_ROTATION_DOWN | 1 | 4 | 4 | 0,00% | 0,00 | -1,04R | €-41,53 |
| SHADOW_SCANNER_TOP5_BTC | ALT_ROTATION_UP | 0 | 5 | 5 | 40,00% | 1,39 | 0,25R | €12,28 |
| SHADOW_SCANNER_TOP5_BTC | RANGE | 1 | 9 | 9 | 44,44% | 2,08 | 0,50R | €44,64 |
| SHADOW_SCANNER_TOP5_BTC | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,69 |
| SHADOW_SCANNER_TOP5_BTC | TRANSITION | 1 | 12 | 12 | 41,67% | 1,49 | 0,30R | €36,18 |
| SHADOW_SCANNER_TOP5_BTC | TREND_UP | 2 | 19 | 19 | 47,37% | 1,85 | 0,47R | €89,92 |
| SHADOW_SCANNER_TOP5_BTC | TREND_UP_HIGH_VOL | 1 | 8 | 8 | 37,50% | 1,20 | 0,14R | €10,84 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | ALT_ROTATION_DOWN | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,86 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TRANSITION | 2 | 1 | 1 | 100,00% | ∞ | 2,19R | €21,87 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TREND_UP | 1 | 2 | 2 | 50,00% | 1,97 | 0,54R | €10,76 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TREND_UP_HIGH_VOL | 0 | 6 | 6 | 16,67% | 0,40 | -0,53R | €-31,93 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | ALT_ROTATION_DOWN | 2 | 3 | 3 | 0,00% | 0,00 | -1,01R | €-30,42 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,86 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | RANGE | 1 | 4 | 4 | 25,00% | 0,72 | -0,21R | €-8,60 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TRANSITION | 1 | 1 | 1 | 100,00% | ∞ | 2,19R | €21,87 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_UP | 1 | 2 | 2 | 50,00% | 1,97 | 0,54R | €10,76 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_UP_HIGH_VOL | 0 | 6 | 6 | 16,67% | 0,40 | -0,53R | €-31,93 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | ALT_ROTATION_DOWN | 2 | 3 | 3 | 0,00% | 0,00 | -1,01R | €-30,42 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,79 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | RANGE | 1 | 4 | 4 | 25,00% | 0,72 | -0,21R | €-8,60 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TRANSITION | 1 | 1 | 1 | 100,00% | ∞ | 2,19R | €21,87 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 2,19R | €21,87 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | ALT_ROTATION_DOWN | 2 | 3 | 3 | 0,00% | 0,00 | -1,01R | €-30,42 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,79 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | RANGE | 1 | 4 | 4 | 25,00% | 0,72 | -0,21R | €-8,60 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TRANSITION | 1 | 1 | 1 | 100,00% | ∞ | 2,19R | €21,87 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 2,19R | €21,87 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | ALT_ROTATION_DOWN | 1 | 4 | 4 | 0,00% | 0,00 | -1,04R | €-41,53 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,79 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | RANGE | 1 | 4 | 4 | 25,00% | 0,72 | -0,21R | €-8,60 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TRANSITION | 1 | 1 | 1 | 100,00% | ∞ | 2,19R | €21,87 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_UP | 1 | 3 | 3 | 33,33% | 1,02 | 0,01R | €0,39 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | ALT_ROTATION_DOWN | 1 | 4 | 4 | 0,00% | 0,00 | -1,04R | €-41,53 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,79 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | RANGE | 1 | 4 | 4 | 25,00% | 0,72 | -0,21R | €-8,60 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TRANSITION | 1 | 1 | 1 | 100,00% | ∞ | 2,19R | €21,87 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_UP | 1 | 3 | 3 | 33,33% | 1,02 | 0,01R | €0,39 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | ALT_ROTATION_DOWN | 1 | 4 | 4 | 0,00% | 0,00 | -1,04R | €-41,53 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,79 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | RANGE | 1 | 4 | 4 | 25,00% | 0,72 | -0,21R | €-8,60 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TRANSITION | 1 | 1 | 1 | 100,00% | ∞ | 2,19R | €21,87 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_UP | 2 | 2 | 2 | 50,00% | 1,97 | 0,54R | €10,76 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_UP_HIGH_VOL | 1 | 8 | 8 | 25,00% | 0,66 | -0,27R | €-21,76 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | ALT_ROTATION_UP | 0 | 4 | 4 | 25,00% | 0,89 | -0,09R | €-3,61 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | RANGE | 2 | 3 | 3 | 0,00% | 0,00 | -1,02R | €-30,46 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 2,99R | €29,87 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_UP | 3 | 3 | 3 | 0,00% | 0,00 | -1,09R | €-32,57 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -1,05R | €-31,38 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | ALT_ROTATION_DOWN | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | ALT_ROTATION_UP | 0 | 4 | 4 | 25,00% | 0,89 | -0,09R | €-3,61 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | RANGE | 2 | 3 | 3 | 0,00% | 0,00 | -1,02R | €-30,46 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 2,99R | €29,87 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_UP | 3 | 3 | 3 | 0,00% | 0,00 | -1,09R | €-32,57 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -1,05R | €-31,38 |
| SHADOW_SCANNER_TOP5_LONG | ALT_ROTATION_DOWN | 1 | 5 | 5 | 0,00% | 0,00 | -1,05R | €-52,64 |
| SHADOW_SCANNER_TOP5_LONG | ALT_ROTATION_UP | 0 | 6 | 6 | 33,33% | 0,92 | -0,06R | €-3,32 |
| SHADOW_SCANNER_TOP5_LONG | RANGE | 1 | 10 | 10 | 50,00% | 2,36 | 0,57R | €56,51 |
| SHADOW_SCANNER_TOP5_LONG | RANGE_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,83 |
| SHADOW_SCANNER_TOP5_LONG | TRANSITION | 1 | 12 | 12 | 41,67% | 1,36 | 0,22R | €26,18 |
| SHADOW_SCANNER_TOP5_LONG | TREND_UP | 2 | 28 | 28 | 50,00% | 1,84 | 0,45R | €125,56 |
| SHADOW_SCANNER_TOP5_LONG | TREND_UP_HIGH_VOL | 1 | 8 | 8 | 37,50% | 1,08 | 0,05R | €4,35 |
| SHADOW_SOL_ADAPTIVE_1H | RANGE | 2 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_SOL_ADAPTIVE_1H | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,89R | €18,89 |
| SHADOW_SOL_ADAPTIVE_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,10R | €-10,96 |
| SHADOW_SOL_ADAPTIVE_4H | RANGE | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SOL_ADAPTIVE_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,05R | €-10,52 |
| SHADOW_SOL_BOLLINGER_1H | RANGE | 1 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,33 |
| SHADOW_SOL_BOLLINGER_4H | TREND_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SOL_DONCHIAN_1H | RANGE | 1 | 1 | 1 | 0,00% | 0,00 | -1,12R | €-11,25 |
| SHADOW_SOL_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,08 |
| SHADOW_SOL_DONCHIAN_4H | RANGE | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SOL_DONCHIAN_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,56 |
| SHADOW_SOL_EMA_1H | RANGE | 1 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_SOL_EMA_1H | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,89R | €18,89 |
| SHADOW_SOL_EMA_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,10R | €-10,96 |
| SHADOW_SOL_EMA_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,56 |

Il P&L è normalizzato a **€10 di rischio per evento**, così leva e size non falsano il confronto.
La matrice diventerà utilizzabile per una rotazione automatica soltanto dopo un campione sufficiente per ciascuna coppia strategia-regime.

# Block 3 — Shadow Exit Engine

Generato: 2026-07-24T11:03:06+00:00

> Motore esclusivamente osservativo e Paper-only. Non modifica le uscite reali. I confronti escludono il funding sia dall'uscita originale sia dalle varianti.

## Stato operativo

- Gruppi di trade ancora monitorati: **345**
- Scenari virtuali ancora attivi: **2839**
- Gruppi in attesa dell'uscita originale: **181**
- Gruppi con originale chiuso ma Shadow ancora attive: **164**
- Confronti completati: **15753**

## Classifica osservativa complessiva

| Scenario | Campione completo | Campione totale | Δ medio vs originale | Migliora | Troppo presto | Troppo tardi | Stato dati |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| GB20_R050 | 752 | 815 | +€7,18 | 50,1% | 200 | 1 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R050 | 752 | 815 | +€5,04 | 48,8% | 205 | 8 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R050 | 752 | 815 | +€2,75 | 47,5% | 211 | 13 | READY_FOR_BLOCK4_EVALUATION |
| TP_R050 | 752 | 815 | +€1,62 | 47,6% | 223 | 0 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R050 | 749 | 812 | +€1,41 | 45,8% | 206 | 27 | READY_FOR_BLOCK4_EVALUATION |
| TIME_6H | 742 | 805 | €-0,90 | 49,7% | 166 | 112 | READY_FOR_BLOCK4_EVALUATION |
| TIME_12H | 738 | 801 | €-0,49 | 42,9% | 85 | 187 | READY_FOR_BLOCK4_EVALUATION |
| GB20_R100 | 737 | 800 | +€5,89 | 43,1% | 169 | 22 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R100 | 737 | 800 | +€3,93 | 43,0% | 158 | 34 | READY_FOR_BLOCK4_EVALUATION |
| TP_R100 | 737 | 800 | +€3,78 | 41,2% | 184 | 22 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R100 | 736 | 799 | +€2,69 | 42,6% | 135 | 58 | READY_FOR_BLOCK4_EVALUATION |
| ATR15_R100 | 736 | 799 | €-1,46 | 34,2% | 61 | 175 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R100 | 733 | 796 | +€2,28 | 39,3% | 99 | 115 | READY_FOR_BLOCK4_EVALUATION |
| ATR20_R100 | 732 | 795 | €-5,14 | 29,8% | 44 | 221 | READY_FOR_BLOCK4_EVALUATION |
| ATR30_R100 | 705 | 768 | €-9,77 | 26,4% | 40 | 218 | READY_FOR_BLOCK4_EVALUATION |
| TP_R150 | 699 | 762 | +€1,38 | 30,7% | 78 | 88 | READY_FOR_BLOCK4_EVALUATION |
| BE_R050 | 696 | 759 | €-10,51 | 28,7% | 125 | 138 | READY_FOR_BLOCK4_EVALUATION |
| TIME_24H | 684 | 747 | €-4,00 | 33,6% | 46 | 207 | READY_FOR_BLOCK4_EVALUATION |
| TP_R200 | 671 | 734 | €-0,04 | 35,8% | 36 | 131 | READY_FOR_BLOCK4_EVALUATION |
| BE_R100 | 653 | 716 | €-17,04 | 20,9% | 39 | 216 | READY_FOR_BLOCK4_EVALUATION |

## Come leggere il controllo

- **EARLIER_BETTER**: la variante è uscita prima e ha conservato più profitto.
- **TOO_EARLY**: la variante è uscita prima ma ha tagliato un movimento migliore.
- **LATER_BETTER**: la variante ha continuato dopo l'uscita originale e ha guadagnato di più.
- **TOO_LATE**: la variante è rimasta aperta più a lungo e ha peggiorato il risultato.

## Limiti e protezioni

Le regole Shadow mantengono entrata, quantità, commissioni, stop protettivo iniziale e liquidazione. Le ambiguità all'interno della stessa candela vengono risolte scegliendo l'esito peggiore. Le posizioni già aperte al momento dell'installazione sono marcate come campione parziale e non saranno utilizzate dal futuro Blocco 4 come prova piena.

# Blocco 4 — Valutazione statistica Shadow

Generato: 2026-07-24T11:03:08+00:00

> Modulo esclusivamente valutativo. Non modifica strategie, uscite, posizioni o capitale. Le candidature vengono consegnate al futuro Blocco 5, senza applicazione automatica.

## Stato

- Risultati Block 3 disponibili: **15753**
- Valutazioni prodotte: **4372**
- Candidature al Blocco 5: **0**
- Mutazioni create automaticamente: **0**

## Classifica complessiva

| Scenario | Campione pieno | Δ medio (R) | Mediana (R) | CI bootstrap basso | Migliora | Score | Stato |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| GB20_R050 | 124 | 0,481 | 0,359 | 0,346 | 80,6% | 98,7 | ELIGIBLE_FOR_MUTATION |
| GB30_R050 | 124 | 0,428 | 0,294 | 0,309 | 80,6% | 98,7 | ELIGIBLE_FOR_MUTATION |
| GB20_R100 | 121 | 0,492 | 0,394 | 0,370 | 79,3% | 98,6 | ELIGIBLE_FOR_MUTATION |
| GB30_R100 | 121 | 0,454 | 0,322 | 0,341 | 81,8% | 98,6 | ELIGIBLE_FOR_MUTATION |
| TP_R100 | 121 | 0,451 | 0,322 | 0,338 | 78,5% | 98,6 | ELIGIBLE_FOR_MUTATION |
| GB40_R050 | 124 | 0,369 | 0,283 | 0,250 | 78,2% | 98,6 | ELIGIBLE_FOR_MUTATION |
| GB40_R100 | 120 | 0,394 | 0,305 | 0,294 | 78,3% | 98,5 | ELIGIBLE_FOR_MUTATION |
| GB50_R050 | 124 | 0,359 | 0,287 | 0,260 | 77,4% | 98,4 | ELIGIBLE_FOR_MUTATION |
| GB50_R100 | 120 | 0,342 | 0,322 | 0,247 | 76,7% | 98,3 | ELIGIBLE_FOR_MUTATION |
| TP_R050 | 124 | 0,278 | 0,287 | 0,165 | 78,2% | 96,8 | ELIGIBLE_FOR_MUTATION |
| ATR15_R100 | 120 | 0,044 | 0,116 | -0,048 | 62,5% | 84,0 | VALIDATING |
| TIME_24H | 6 | 0,997 | 1,104 | 0,180 | 66,7% | 74,1 | INSUFFICIENT_DATA |
| GB20_R050 | 622 | 0,102 | 0,000 | 0,034 | 45,2% | 70,0 | VALIDATING |
| GB20_R100 | 610 | 0,062 | 0,000 | 0,013 | 36,6% | 69,7 | VALIDATING |
| GB30_R050 | 622 | 0,062 | 0,000 | -0,002 | 43,6% | 69,7 | VALIDATING |
| TP_R150 | 599 | 0,058 | 0,000 | 0,009 | 27,4% | 69,7 | VALIDATING |
| TIME_12H | 625 | 0,039 | 0,000 | -0,038 | 43,7% | 61,2 | VALIDATING |
| GB30_R100 | 610 | 0,024 | 0,000 | -0,024 | 36,1% | 59,0 | VALIDATING |
| TP_R200 | 6 | 0,472 | 0,250 | -0,017 | 50,0% | 58,7 | INSUFFICIENT_DATA |
| TP_R100 | 610 | 0,030 | 0,000 | -0,022 | 34,1% | 57,8 | VALIDATING |

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

Generato: 2026-07-24T11:03:18+00:00

Questi profili sono osservativi e Paper-only. Usano gli stessi trade della madre, ma applicano una specifica uscita Block 3 soltanto ai segnali aperti dopo la loro registrazione.
Nessuna promozione, modifica live o operazione reale viene eseguita automaticamente.

| Challenger | Madre | Scenario | Chiusi | Copertura | PF | PnL | Exp/trade | DD | Stato |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Rapida 1H V1 — giveback 20% dopo +0,5R | SHADOW_1H_FAST | GB20_R050 | 11 | 100,00% | 1,16 | +€41,41 | +€3,76 | 1,14% | COLLECTING |
| Rapida 1H V1 — giveback 30% dopo +0,5R | SHADOW_1H_FAST | GB30_R050 | 11 | 100,00% | 1,01 | +€1,90 | +€0,17 | 1,19% | COLLECTING |
| Relative Strength — giveback 20% dopo +0,5R | SHADOW_RELATIVE_STRENGTH | GB20_R050 | 2 | 100,00% | 0,39 | €-32,83 | €-16,42 | 0,54% | COLLECTING |
| Relative Strength — giveback 30% dopo +0,5R | SHADOW_RELATIVE_STRENGTH | GB30_R050 | 2 | 100,00% | 0,34 | €-35,84 | €-17,92 | 0,54% | COLLECTING |

## Regole di valutazione

- Prima fotografia a 30 trade indipendenti.
- Revisione per possibile promozione a 50 trade indipendenti.
- PF minimo 1,50, expectancy e PnL positivi, drawdown massimo 15%, copertura minima 90%.
- PF deve superare la madre e il drawdown non deve essere peggiore sulla stessa serie di trade.
- La promozione resta una decisione umana protetta; il rollback viene predisposto soltanto in fase di approvazione.

# Blocco 4.5 — Crash Cascade Guard

Generato: 2026-07-24T11:02:58+00:00

> Paper-only. In mercato NORMAL/WATCH non riduce i segnali. Le limitazioni iniziano soltanto in STRESS, RECOVERY, CRASH, EXTREME o con dati non affidabili.

## Stato corrente

- Livello: **NORMAL**
- Direzione: **NONE**
- Segnali bloccati nel ciclo: **0**
- Simulazioni bloccate attive: **16**
- Simulazioni completate nel ciclo: **6**
- Liquidazioni virtuali evitate totali: **0**
- Valore cumulato del filtro: **-39.46 R**
- Profitto virtuale mancato: **77.89 R**

## Stress test portafogli Paper

| Scenario | Posizioni interessate | Liquidazioni stimate | Perdita stimata EUR |
| --- | ---: | ---: | ---: |
| DOWN_10 | 102 | 0 | 13169.25 |
| DOWN_20 | 102 | 0 | 26338.50 |
| DOWN_30 | 102 | 10 | 39645.53 |
| DOWN_40 | 102 | 26 | 49908.22 |
| UP_10 | 64 | 0 | 18403.79 |
| UP_20 | 64 | 0 | 36807.58 |
| UP_30 | 64 | 0 | 55211.37 |
| UP_40 | 64 | 36 | 65562.11 |

## Modello di esecuzione

Se una candela di cascata attraversa nello stesso intervallo sia lo stop sia il prezzo di liquidazione, il Paper usa il caso peggiore e registra una liquidazione intrabar. Gli stop in gap o in regime di stress ricevono slippage aggiuntivo.

## Requisiti prima del live futures

- modalità ISOLATED obbligatoria;
- stop nativo sull'exchange;
- conferma dello stop prima di accettare la posizione;
- cross margin vietato.

# Blocco 5 — Candidati evolutivi controllati

Generato: 2026-07-24T11:02:34+00:00

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

Generato: 2026-07-24T11:03:18+00:00

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

Generato: 2026-07-24T11:03:18+00:00

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

Generato: 2026-07-24T11:03:18+00:00

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

Generato: 2026-07-24T11:03:18+00:00

> Paper-only. La memoria può bloccare soltanto una futura proposta Block 5 classificata AVOID; non modifica strategie esistenti.

## Stato

- Strategie/portafogli valutati: **84**
- Hall of Fame: **8**
- Memorie genetiche: **0**
- Firme bloccate: **0**
- Azioni automatiche e live: **0**

## Hall of Fame

| Rank | Strategia | Stato | Score | Grade | Trade | PF | Expectancy R | DD R |
| ---: | --- | --- | ---: | --- | ---: | ---: | ---: | ---: |
| 1 | SHADOW_SCANNER_TOP5_LONG | BASELINE | 20.2 | E | 30 | 2.21 | 0.412 | 5.75 |
| 2 | SHADOW_1H_BALANCED | BASELINE | 15.5 | E | 37 | 1.48 | 0.184 | 4.17 |
| 3 | SHADOW_1H_BALANCED_V3 | BASELINE | 13.2 | E | 31 | 1.32 | 0.163 | 3.23 |
| 4 | SHADOW_RELATIVE_STRENGTH_V2 | BASELINE | 10.8 | E | 31 | 1.26 | 0.145 | 6.62 |
| 5 | SHADOW_1H_FAST_V3 | BASELINE | 10.6 | E | 58 | 1.03 | 0.012 | 5.36 |
| 6 | SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | BASELINE | 7.1 | E | 30 | 0.91 | -0.039 | 3.68 |
| 7 | SHADOW_1H_FAST | BASELINE | 7.0 | E | 66 | 0.88 | -0.059 | 13.48 |
| 8 | SHADOW_1H_FAST_V3_NOHIGH_V1 | BASELINE | 6.2 | E | 31 | 0.88 | -0.057 | 5.53 |

## Memoria genetica

| Scope | Famiglia | Mutazione | Target | Stato | Score | Prove | Coppie | Blocco |
| --- | --- | --- | --- | --- | ---: | ---: | ---: | --- |
| — | — | Nessuna candidata ancora creata | — | INSUFFICIENT | 0 | 0 | 0 | NO |

## Sicurezza

- Nessuna strategia, posizione o promozione esistente viene modificata.
- Nessuna mutazione, promozione, pensionamento o rollback automatico.
- Nessun effetto live e nessun ordine reale.

# Blocco 10 — Regime Fitness e specializzazione

Generato: 2026-07-24T11:03:18+00:00

> Paper-only e advisory. Il blocco misura quali strategie funzionano nei diversi regimi, ma non cambia automaticamente strategia o posizione.

## Stato

- Regime corrente: **RANGE**
- Righe di performance: **308**
- Strategie preferite nel regime corrente: **0**
- Strategie da evitare nel regime corrente: **0**
- Memorie contestuali: **154**
- Routing automatico: **NO**

## Classifica del regime corrente

| Rank | Portafoglio | Famiglia | Stato | Fitness | Trade | PF | Expectancy R | DD R |
| ---: | --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| 1 | SHADOW_DOGE_DONCHIAN_1H | shadow-doge-donchian-1h | INSUFFICIENT | 80.8 | 2 | 99.00 | 0.548 | 0.00 |
| 2 | SHADOW_BTC_BOLLINGER_1H | shadow-btc-bollinger-1h | INSUFFICIENT | 80.8 | 2 | 99.00 | 0.997 | 0.00 |
| 3 | SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | shadow-scanner-top5-btc-guard-btc-le3-v1 | INSUFFICIENT | 80.8 | 2 | 99.00 | 1.186 | 0.00 |
| 4 | SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | shadow-scanner-top5-btc-btc-le3-v1 | INSUFFICIENT | 80.3 | 1 | 99.00 | 0.398 | 0.00 |
| 5 | SHADOW_COMBO_ADAPTIVE | shadow-combo-adaptive | OBSERVING | 79.1 | 19 | 2.19 | 0.339 | 1.10 |
| 6 | SHADOW_DOGE_EMA_1H | shadow-doge-ema-1h | INSUFFICIENT | 77.8 | 5 | 4.56 | 0.781 | 1.10 |
| 7 | SHADOW_ETH_BOLLINGER_1H | shadow-eth-bollinger-1h | INSUFFICIENT | 76.6 | 1 | 99.00 | 0.309 | 0.00 |
| 8 | SHADOW_SCANNER_TOP5_LONG | shadow-scanner-top5-long | OBSERVING | 74.4 | 22 | 1.96 | 0.371 | 4.17 |
| 9 | SHADOW_SCANNER_TOP5_BTC | shadow-scanner-top5-btc | OBSERVING | 71.2 | 18 | 1.93 | 0.332 | 3.09 |
| 10 | SHADOW_SCANNER_TOP5_BTC_TP3_V1 | shadow-scanner-top5-btc-tp3-v1 | INSUFFICIENT | 70.3 | 5 | 1.93 | 0.400 | 2.15 |

## Sicurezza

- Il regime viene assegnato usando solo l'ultimo record noto prima dell'entrata del trade.
- Nessun uso di dati futuri per classificare il trade.
- Il Candidate Regime Gate è advisory per impostazione predefinita.
- Nessun cambio automatico di MASTER, posizione o live.

# Blocco 11 — Collegamento protetto al live

Generato: 2026-07-24T11:03:18+00:00

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

Generato: 2026-07-24T11:02:58+00:00

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
