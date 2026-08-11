# Paper trading automatico KuCoin

Generato: 2026-08-11T15:43:54+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-08-11T15:38:30+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-08-11T15:38:30+00:00 | 2026-08-11T15:38:30+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-08-11T15:15:00+00:00 | 2026-08-11T15:15:00+00:00 | 8,9 min | 25,0 min | OK |
| 60m | 12 | 2026-08-11T14:00:00+00:00 | 2026-08-11T14:00:00+00:00 | 38,9 min | 45,0 min | OK |
| 240m | 12 | 2026-08-11T08:00:00+00:00 | 2026-08-11T08:00:00+00:00 | 3,65 h | 1,00 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | BEAT | 240m | SHORT | -9,75 | 6,00 | 0,00 | STALE_CANDLE | 3,65 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 218.9 minuti; tolleranza 60 minuti. |
| Principale 4H | VELVET | 240m | LONG | 7,75 | 6,00 | 0,00 | STALE_CANDLE | 3,65 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 218.9 minuti; tolleranza 60 minuti. |
| Principale 4H | XRP | 240m | SHORT | -6,89 | 6,00 | 0,00 | STALE_CANDLE | 3,65 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 218.9 minuti; tolleranza 60 minuti. |
| Principale 4H | SOL | 240m | LONG | 3,31 | 6,00 | 2,69 | STALE_CANDLE | 3,65 h | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 218.9 minuti; tolleranza 60 minuti. |
| Principale 4H | TUT | 240m | LONG | 2,75 | 6,00 | 3,25 | STALE_CANDLE | 3,65 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 218.9 minuti; tolleranza 60 minuti. |
| Principale 4H | ZEC | 240m | SHORT | -1,71 | 6,00 | 4,29 | STALE_CANDLE | 3,65 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 218.9 minuti; tolleranza 60 minuti. |
| Principale 4H | DOGE | 240m | SHORT | -1,59 | 6,00 | 4,41 | STALE_CANDLE | 3,65 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 218.9 minuti; tolleranza 60 minuti. |
| Principale 4H | HYPE | 240m | SHORT | -1,43 | 6,00 | 4,57 | STALE_CANDLE | 3,65 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 218.9 minuti; tolleranza 60 minuti. |
| Principale 4H | PEPE | 240m | LONG | 1,35 | 6,00 | 4,65 | STALE_CANDLE | 3,65 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 218.9 minuti; tolleranza 60 minuti. |
| Principale 4H | SOXL | 240m | LONG | 0,50 | 6,00 | 5,50 | STALE_CANDLE | 3,65 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 218.9 minuti; tolleranza 60 minuti. |
| Principale 4H | BTC | 240m | SHORT | -0,25 | 6,00 | 5,75 | STALE_CANDLE | 3,65 h | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 218.9 minuti; tolleranza 60 minuti. |
| Principale 4H | ETH | 240m | LONG | 0,15 | 6,00 | 5,85 | STALE_CANDLE | 3,65 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 218.9 minuti; tolleranza 60 minuti. |
| Scalp RSI Long 20 · €10 · 15x | PEPE | 15m | LONG | 10,00 | 8,00 | 0,00 | OPENED | 8,9 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scalp RSI Long 25 · €10 · 15x | PEPE | 15m | LONG | 10,00 | 8,00 | 0,00 | OPENED | 8,9 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scalp RSI Long 20 · €50 · 15x | PEPE | 15m | LONG | 10,00 | 8,00 | 0,00 | OPENED | 8,9 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scalp RSI Long 25 · €50 · 15x | PEPE | 15m | LONG | 10,00 | 8,00 | 0,00 | OPENED | 8,9 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scalp RSI Long 20 · prudente · 5x | PEPE | 15m | LONG | 10,00 | 8,00 | 0,00 | OPENED | 8,9 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scalp RSI Long 25 · prudente · 5x | PEPE | 15m | LONG | 10,00 | 8,00 | 0,00 | OPENED | 8,9 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Bilanciata 1H V1 | VELVET | 60m | LONG | 8,25 | 5,00 | 0,00 | READY | 38,9 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Bilanciata 1H V2 | VELVET | 60m | LONG | 8,25 | 5,50 | 0,00 | READY | 38,9 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.908,92 | -0,91% | €160,57 | €3.000,00 | 5,35% | 3 | 36 | 38,89% | 0,90 | 6,36% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 36 | 1092 | PRIME INDICAZIONI | 50 (mancano 14) |

- Trade del Principale 4H chiusi: **36**; win rate **38,89%**; profit factor **0,90**.
- Expectancy: **€-3,08** per trade; P&L netto: **€-110,81**; max drawdown: **6,36%**.
- Valutazione: **Si può osservare la direzione, ma il risultato resta fragile.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 3 | €9.908,92 | €1.134,98 | €3.404,94 | €97,42 | €21,28 |
| TEST | Benchmark Donchian breakout 1H | 5 | €10.761,11 | €5.024,13 | €10.048,27 | €108,97 | €171,06 |
| TEST | Rapida score 6–7,5 — Cost Aware | 2 | €10.744,76 | €2.885,68 | €8.657,03 | €106,94 | €53,86 |
| TEST | Rapida V1 — no HIGH + score <7,5 | 4 | €10.728,54 | €4.642,20 | €13.926,61 | €159,78 | €80,84 |
| TEST | Rapida V3 NoHigh — Regime Guard | 3 | €10.671,04 | €4.450,33 | €13.351,00 | €159,45 | €45,07 |
| TEST | Combo Adaptive — Side × Regime Guard | 3 | €10.635,92 | €5.179,38 | €10.358,76 | €159,05 | €60,02 |
| TEST | Rapida V1 — score 6–7,5 | 3 | €10.635,56 | €3.032,34 | €9.097,01 | €105,85 | €53,31 |
| TEST | Rapida V3 NoHigh — Range Only | 3 | €10.564,16 | €4.405,76 | €13.217,28 | €157,86 | €44,62 |
| TEST | Donchian 1H Gb20 120R V1 | 5 | €10.507,75 | €4.905,84 | €9.811,69 | €106,41 | €167,03 |
| TEST | FAST NoHigh <7,5 · SHORT only | 4 | €10.461,57 | €4.526,68 | €13.580,05 | €155,81 | €78,83 |
| TEST | Rapida score 6–7,5 — Range Only | 3 | €10.409,55 | €2.991,17 | €8.973,51 | €103,61 | €52,18 |
| TEST | Bilanciata 1H V3 Filtered | 5 | €10.363,72 | €3.020,80 | €9.062,41 | €204,47 | €16,55 |
| TEST | Rapida score 6–7,5 — senza Trend Up | 3 | €10.352,78 | €2.951,71 | €8.855,14 | €103,04 | €51,89 |
| TEST | MAIN — Side × Regime Guard | 1 | €10.338,53 | €747,08 | €2.241,25 | €51,13 | €22,33 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 0 | €10.300,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H V1 | 5 | €10.284,63 | €1.839,48 | €5.518,43 | €101,70 | €1,26 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 0 | €10.271,73 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 0 | €10.239,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 0 | €10.235,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | MAIN — Dynamic Asset Selector | 0 | €10.230,30 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top 5 Long 1H | 2 | €10.221,74 | €996,34 | €1.992,67 | €51,78 | €0,00 |
| TEST | Combo Adaptive — madre | 5 | €10.217,16 | €4.515,81 | €9.031,62 | €152,59 | €35,79 |
| TEST | Rapida V1 — senza PEPE | 4 | €10.212,49 | €3.872,69 | €11.618,06 | €152,92 | €12,03 |
| TEST | Scanner Bottom10 Short | 4 | €10.211,48 | €5.323,61 | €10.647,22 | €153,72 | €50,60 |
| TEST | Scanner Bottom15 Short | 4 | €10.211,48 | €5.323,61 | €10.647,22 | €153,72 | €50,60 |
| TEST | Scanner Bottom20 Short | 4 | €10.211,48 | €5.323,61 | €10.647,22 | €153,72 | €50,60 |
| TEST | Bilanciata 1H V2 | 3 | €10.198,37 | €2.460,24 | €7.380,73 | €100,12 | €19,52 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 0 | €10.185,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 0 | €10.145,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | 3 | €10.141,71 | €4.913,75 | €9.827,51 | €150,97 | €51,16 |
| TEST | Sol Donchian 1H | 1 | €10.134,14 | €1.316,92 | €3.950,75 | €50,57 | €22,59 |
| TEST | Rapida V3 — score <7,5 | 4 | €10.133,95 | €3.551,99 | €10.655,97 | €150,83 | €50,13 |
| TEST | Scanner Bottom5 Short Profit Lock V1 | 3 | €10.126,28 | €4.906,28 | €9.812,56 | €150,74 | €51,09 |
| TEST | Rapida V3 senza ESPORTS — Stress Guard | 3 | €10.111,02 | €4.216,78 | €12.650,33 | €151,08 | €42,70 |
| TEST | Btc Bollinger 1H | 0 | €10.110,96 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Trend — Side × Regime Guard | 2 | €10.107,86 | €2.911,09 | €5.822,18 | €0,00 | €147,81 |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 0 | €10.099,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top 5 + forza BTC 1H | 2 | €10.092,14 | €983,70 | €1.967,41 | €51,12 | €0,00 |
| TEST | Sol Bollinger 4H | 0 | €10.086,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 4H | 0 | €10.084,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 0 | €10.048,77 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom 5 Short 1H | 3 | €10.048,36 | €4.868,52 | €9.737,05 | €149,58 | €50,69 |
| TEST | Rapida V3 — no volatilità HIGH | 4 | €10.044,73 | €4.378,00 | €13.134,00 | €150,09 | €42,42 |
| TEST | Rapida 1H V1 — madre | 0 | €10.043,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Ema 1H | 0 | €10.039,73 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — 75% a 2R + runner 25% a 3R | 5 | €10.033,96 | €4.381,07 | €8.762,15 | €146,42 | €40,03 |
| TEST | Ampia 4H | 5 | €10.014,01 | €1.925,45 | €3.850,91 | €148,66 | €16,55 |
| TEST | Btc Donchian 1H | 1 | €10.011,77 | €1.301,67 | €3.905,01 | €49,98 | €17,28 |
| TEST | Combo Adaptive — Quality7 | 0 | €10.010,16 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 0 | €10.008,92 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €10.003,85 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 0 | €10.003,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €50 · 15x | 0 | €10.001,42 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 0 | €10.000,77 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €10 · 15x | 0 | €10.000,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Continuation V1 | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · prudente · 5x | 0 | €9.999,47 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €10 · 15x | 0 | €9.997,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €10 · 15x | 1 | €9.996,51 | €10,00 | €150,00 | €1,31 | €-0,09 |
| TEST | Rapida V1 — Long + BTC 1–3 + score <7,5 | 0 | €9.996,45 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · prudente · 5x | 1 | €9.996,32 | €229,00 | €1.145,02 | €10,00 | €-0,69 |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 0 | €9.995,23 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €10 · 15x | 0 | €9.994,44 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €10 · 15x | 1 | €9.988,86 | €10,00 | €150,00 | €1,31 | €-0,09 |
| TEST | Scalp RSI Long 15 · €50 · 15x | 0 | €9.988,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Donchian 4H | 0 | €9.985,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 senza ESPORTS — MFE Lock | 5 | €9.983,91 | €3.821,17 | €11.463,52 | €150,65 | €12,04 |
| TEST | Scalp RSI Long 20 · €50 · 15x | 1 | €9.982,55 | €50,00 | €750,00 | €6,55 | €-0,45 |
| TEST | Sol Adaptive 4H | 0 | €9.982,09 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Donchian 1H | 0 | €9.981,34 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · prudente · 5x | 0 | €9.980,94 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V1 — target pieno 2R | 4 | €9.976,30 | €3.784,21 | €11.352,64 | €149,47 | €11,74 |
| TEST | Btc Adaptive 1H | 1 | €9.972,77 | €1.152,72 | €3.458,17 | €49,80 | €15,30 |
| TEST | Scalp RSI Short 80 · €50 · 15x | 0 | €9.972,22 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 1H | 0 | €9.970,30 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Top 5 + BTC — BTC 2–3 | 0 | €9.968,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Bollinger 1H | 0 | €9.959,49 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Bollinger 1H | 1 | €9.956,89 | €1.375,28 | €4.125,84 | €0,00 | €57,35 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 1 | €9.951,84 | €227,99 | €1.139,93 | €9,95 | €-0,68 |
| TEST | Btc Ema 4H | 0 | €9.950,68 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 4H | 0 | €9.949,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €50 · 15x | 1 | €9.944,32 | €50,00 | €750,00 | €6,55 | €-0,45 |
| TEST | Bilanciata 1H — SHORT Trend Down stretto | 0 | €9.943,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V2 | 3 | €9.928,15 | €3.144,09 | €9.432,26 | €99,14 | €17,42 |
| TEST | Scalp RSI Short 80 · prudente · 5x | 0 | €9.925,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — Quality7 + Regime + parziale 1R | 0 | €9.922,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.921,51 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V3 Filtered — madre | 5 | €9.918,67 | €3.796,20 | €11.388,61 | €149,67 | €11,96 |
| TEST | Combo Adaptive — Trend/Transition | 0 | €9.903,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 4H | 0 | €9.898,26 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Ema 4H | 0 | €9.894,27 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 1H | 1 | €9.886,33 | €1.141,05 | €3.423,15 | €49,29 | €29,15 |
| TEST | Sol Ema 1H | 1 | €9.885,39 | €1.142,11 | €3.426,34 | €49,34 | €19,59 |
| TEST | Eth Donchian 1H | 0 | €9.871,99 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — target pieno 3R | 5 | €9.846,50 | €4.299,23 | €8.598,45 | €143,68 | €39,28 |
| TEST | Sol Ema 4H | 0 | €9.845,78 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 — qualità completa + profit lock | 1 | €9.841,82 | €189,96 | €569,87 | €49,62 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 0 | €9.837,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Forza relativa 1H V2 | 3 | €9.834,35 | €3.492,71 | €6.985,43 | €98,59 | €73,11 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 0 | €9.817,34 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — parziale 1R | 5 | €9.810,98 | €4.336,29 | €8.672,57 | €146,53 | €34,37 |
| TEST | Combo Adaptive — Long Only | 2 | €9.803,39 | €955,57 | €1.911,15 | €49,66 | €0,00 |
| TEST | Bilanciata V3 · LONG only | 5 | €9.802,42 | €2.857,20 | €8.571,59 | €193,40 | €15,65 |
| TEST | Eth Adaptive 1H | 0 | €9.799,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 1H | 1 | €9.798,57 | €1.132,08 | €3.396,25 | €48,91 | €19,42 |
| TEST | Combo Mean Reversion | 0 | €9.798,03 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — Quality7 + Regime | 0 | €9.797,24 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 senza ESPORTS — Long Only | 2 | €9.789,25 | €832,01 | €2.496,03 | €49,58 | €0,00 |
| TEST | Benchmark trend following EMA 1H | 5 | €9.782,23 | €3.635,19 | €7.270,38 | €146,85 | €90,86 |
| TEST | Rapida V3 — Long + no HIGH + score <7,5 | 1 | €9.776,15 | €188,69 | €566,07 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 0 | €9.762,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Ema 1H | 1 | €9.753,83 | €1.125,91 | €3.377,73 | €48,64 | €27,77 |
| TEST | Global Confluence puro 1H | 0 | €9.730,31 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 0 | €9.723,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 — senza ESPORTS | 5 | €9.716,77 | €3.718,93 | €11.156,79 | €146,62 | €11,72 |
| TEST | Top 5 + BTC — target pieno 3R | 2 | €9.716,20 | €947,06 | €1.894,12 | €49,22 | €0,00 |
| TEST | Master Adaptive Expanded V1 | 3 | €9.712,14 | €2.870,99 | €5.741,99 | €147,26 | €-30,13 |
| TEST | Top 5 + BTC — 75% a 2,2R + runner 3R | 2 | €9.710,51 | €946,50 | €1.893,01 | €49,19 | €0,00 |
| TEST | Top 5 + BTC — Guard + BTC≤3 | 2 | €9.680,97 | €943,62 | €1.887,25 | €49,04 | €0,00 |
| TEST | Master Adaptive GB20 — Breakeven 0,5R | 2 | €9.675,65 | €1.160,64 | €2.321,27 | €98,03 | €0,00 |
| TEST | Master Adaptive GB20 — 50% a 0,75R | 2 | €9.665,37 | €1.159,40 | €2.318,80 | €97,93 | €0,00 |
| TEST | Master Adaptive Runner25 V1 | 2 | €9.644,57 | €1.156,91 | €2.313,82 | €97,71 | €0,00 |
| TEST | Top 5 + BTC — BTC≤3 | 2 | €9.644,05 | €940,03 | €1.880,05 | €48,85 | €0,00 |
| TEST | Master Adaptive No Alt V1 | 2 | €9.631,95 | €1.155,39 | €2.310,79 | €97,59 | €0,00 |
| TEST | Benchmark Bollinger mean reversion 1H | 3 | €9.631,88 | €3.863,04 | €7.726,08 | €143,64 | €-37,35 |
| TEST | Master Adaptive V1 | 2 | €9.627,98 | €1.154,92 | €2.309,83 | €97,55 | €0,00 |
| TEST | Forza relativa 1H V1 | 5 | €9.622,55 | €4.258,56 | €8.517,12 | €140,53 | €2,52 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 0 | €9.579,83 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Top 5 + BTC — Guard | 2 | €9.563,48 | €932,17 | €1.864,35 | €48,44 | €0,00 |
| TEST | Combo Trend | 6 | €9.526,44 | €5.090,91 | €10.181,82 | €141,39 | €65,73 |
| TEST | Combo Scanner | 2 | €9.515,64 | €932,59 | €1.865,18 | €48,46 | €0,00 |
| TEST | Top 5 + BTC — Guard + BTC≤3 + MFE | 2 | €9.514,86 | €927,43 | €1.854,87 | €48,20 | €0,00 |
| TEST | Master Adaptive Gb20 V1 | 2 | €9.500,06 | €1.139,57 | €2.279,14 | €96,25 | €0,00 |
| TEST | Top 5 + BTC — solo MFE | 2 | €9.459,92 | €922,08 | €1.844,16 | €47,92 | €0,00 |
| TEST | Bilanciata 1H — LONG senza Range High Vol | 2 | €9.446,02 | €1.252,04 | €3.756,11 | €48,30 | €-24,82 |
| TEST | Master Adaptive GB20 — Loss Cap 0,75R | 1 | €9.437,48 | €262,28 | €524,56 | €48,40 | €0,00 |
| TEST | Scanner Top10 Long | 2 | €9.415,02 | €917,70 | €1.835,40 | €47,69 | €0,00 |
| TEST | Scanner Top15 Long | 2 | €9.415,02 | €917,70 | €1.835,40 | €47,69 | €0,00 |
| TEST | Scanner Top20 Long | 2 | €9.415,02 | €917,70 | €1.835,40 | €47,69 | €0,00 |
| TEST | Top 5 + BTC — Guard + MFE | 2 | €9.341,06 | €910,49 | €1.820,99 | €47,31 | €0,00 |
| TEST | Rapida V3 — Long Only | 2 | €9.320,43 | €792,16 | €2.376,49 | €47,21 | €0,00 |
| TEST | Combo Adaptive — MFE Trail esistente | 4 | €9.295,57 | €4.075,30 | €8.150,61 | €138,17 | €32,18 |
| TEST | Master Adaptive Strict3 V1 | 1 | €9.223,98 | €195,94 | €391,88 | €47,03 | €0,00 |

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
| PRINCIPALE | Principale 4H | Confluenza trend | €9.908,92 | €-110,81 | 36 | 36 | 38,89% | 0,90 | €-3,08 | 6,36% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €10.761,11 | €595,13 | 43 | 43 | 51,16% | 1,59 | €13,84 | 3,09% |
| TEST | Rapida score 6–7,5 — Cost Aware | Momentum / breakout | €10.744,76 | €696,09 | 41 | 41 | 56,10% | 2,16 | €16,98 | 1,96% |
| TEST | Rapida V1 — no HIGH + score <7,5 | Momentum / breakout | €10.728,54 | €656,09 | 71 | 71 | 47,89% | 1,49 | €9,24 | 2,83% |
| TEST | Rapida V3 NoHigh — Regime Guard | Momentum / breakout V3 Filtered | €10.671,04 | €633,99 | 23 | 23 | 69,57% | 4,83 | €27,56 | 1,39% |
| TEST | Combo Adaptive — Side × Regime Guard | Combo Adaptive | €10.635,92 | €582,12 | 41 | 41 | 56,10% | 2,22 | €14,20 | 1,58% |
| TEST | Rapida V1 — score 6–7,5 | Momentum / breakout | €10.635,56 | €587,73 | 81 | 81 | 45,68% | 1,40 | €7,26 | 2,49% |
| TEST | Rapida V3 NoHigh — Range Only | Momentum / breakout V3 Filtered | €10.564,16 | €527,47 | 15 | 15 | 66,67% | 4,21 | €35,16 | 1,78% |
| TEST | Donchian 1H Gb20 120R V1 | Donchian breakout 20 barre | €10.507,75 | €345,68 | 11 | 11 | 54,55% | 3,21 | €31,43 | 1,61% |
| TEST | FAST NoHigh <7,5 · SHORT only | Momentum / breakout | €10.461,57 | €390,91 | 35 | 35 | 48,57% | 1,82 | €11,17 | 1,76% |
| TEST | Rapida score 6–7,5 — Range Only | Momentum / breakout | €10.409,55 | €362,75 | 17 | 17 | 58,82% | 1,96 | €21,34 | 2,28% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €10.363,72 | €351,96 | 71 | 71 | 39,44% | 1,23 | €4,96 | 3,20% |
| TEST | Rapida score 6–7,5 — senza Trend Up | Momentum / breakout | €10.352,78 | €306,22 | 39 | 39 | 53,85% | 1,39 | €7,85 | 3,20% |
| TEST | MAIN — Side × Regime Guard | Confluenza trend | €10.338,53 | €317,32 | 18 | 18 | 50,00% | 1,84 | €17,63 | 2,40% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | Momentum / breakout V3 Filtered | €10.300,05 | €300,05 | 33 | 33 | 48,48% | 2,04 | €9,09 | 2,01% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €10.284,63 | €286,03 | 80 | 80 | 45,00% | 1,21 | €3,58 | 3,56% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | Momentum / breakout V3 Filtered | €10.271,73 | €271,73 | 22 | 22 | 50,00% | 1,74 | €12,35 | 1,72% |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | Momentum / breakout V3 Filtered | €10.239,20 | €239,20 | 17 | 17 | 52,94% | 4,50 | €14,07 | 1,01% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | Momentum / breakout V3 Filtered | €10.235,18 | €235,18 | 20 | 20 | 50,00% | 1,90 | €11,76 | 2,73% |
| TEST | MAIN — Dynamic Asset Selector | Confluenza trend | €10.230,30 | €230,30 | 11 | 11 | 45,45% | 1,85 | €20,94 | 1,50% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.221,74 | €222,29 | 52 | 52 | 42,31% | 1,17 | €4,27 | 6,09% |
| TEST | Combo Adaptive — madre | Combo Adaptive | €10.217,16 | €186,15 | 46 | 46 | 41,30% | 1,28 | €4,05 | 3,05% |
| TEST | Rapida V1 — senza PEPE | Momentum / breakout | €10.212,49 | €206,66 | 77 | 77 | 44,16% | 1,14 | €2,68 | 2,79% |
| TEST | Scanner Bottom10 Short | Scanner Bottom10 Short | €10.211,48 | €166,70 | 33 | 33 | 45,45% | 1,29 | €5,05 | 2,72% |
| TEST | Scanner Bottom15 Short | Scanner Bottom15 Short | €10.211,48 | €166,70 | 33 | 33 | 45,45% | 1,29 | €5,05 | 2,72% |
| TEST | Scanner Bottom20 Short | Scanner Bottom20 Short | €10.211,48 | €166,70 | 33 | 33 | 45,45% | 1,29 | €5,05 | 2,72% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €10.198,37 | €183,30 | 45 | 43 | 51,11% | 1,21 | €4,07 | 2,75% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | Momentum / breakout V3 Filtered | €10.185,37 | €185,37 | 22 | 22 | 40,91% | 1,57 | €8,43 | 2,27% |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | Momentum / breakout V3 Filtered | €10.145,12 | €145,12 | 44 | 44 | 45,45% | 1,20 | €3,30 | 2,91% |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | Scanner Bottom 5 Short | €10.141,71 | €95,87 | 26 | 26 | 46,15% | 1,24 | €3,69 | 1,38% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €10.134,14 | €113,92 | 4 | 4 | 75,00% | 26,39 | €28,48 | 0,79% |
| TEST | Rapida V3 — score <7,5 | Momentum / breakout V3 Filtered | €10.133,95 | €89,43 | 71 | 71 | 43,66% | 1,06 | €1,26 | 4,96% |
| TEST | Scanner Bottom5 Short Profit Lock V1 | Scanner Bottom 5 Short | €10.126,28 | €80,51 | 27 | 27 | 44,44% | 1,24 | €2,98 | 1,53% |
| TEST | Rapida V3 senza ESPORTS — Stress Guard | Momentum / breakout V3 Filtered | €10.111,02 | €75,90 | 20 | 20 | 45,00% | 1,17 | €3,80 | 2,17% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.110,96 | €110,96 | 4 | 4 | 75,00% | 2,94 | €27,74 | 0,70% |
| TEST | Combo Trend — Side × Regime Guard | Combo Trend | €10.107,86 | €-37,35 | 34 | 34 | 47,06% | 0,94 | €-1,10 | 2,89% |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | Momentum / breakout V3 Filtered | €10.099,04 | €99,04 | 55 | 55 | 54,55% | 1,12 | €1,80 | 3,59% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €10.092,14 | €92,68 | 43 | 43 | 37,21% | 1,09 | €2,16 | 5,26% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €10.086,98 | €86,98 | 1 | 1 | 100,00% | ∞ | €86,98 | 0,40% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.084,12 | €84,12 | 1 | 1 | 100,00% | ∞ | €84,12 | 0,30% |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | Momentum / breakout V3 Filtered | €10.048,77 | €48,77 | 23 | 23 | 43,48% | 1,12 | €2,12 | 3,05% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €10.048,36 | €2,94 | 54 | 54 | 38,89% | 1,00 | €0,05 | 5,48% |
| TEST | Rapida V3 — no volatilità HIGH | Momentum / breakout V3 Filtered | €10.044,73 | €10,19 | 66 | 66 | 40,91% | 1,01 | €0,15 | 2,96% |
| TEST | Rapida 1H V1 — madre | Momentum / breakout | €10.043,28 | €43,28 | 78 | 78 | 34,62% | 1,02 | €0,55 | 6,76% |
| TEST | Doge Ema 1H | Trend following EMA | €10.039,73 | €39,73 | 11 | 11 | 63,64% | 1,18 | €3,61 | 1,44% |
| TEST | Combo Adaptive — 75% a 2R + runner 25% a 3R | Combo Adaptive | €10.033,96 | €-1,46 | 51 | 51 | 35,29% | 1,00 | €-0,03 | 2,62% |
| TEST | Ampia 4H | Confluenza trend | €10.014,01 | €-0,74 | 29 | 29 | 27,59% | 1,00 | €-0,03 | 4,21% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €10.011,77 | €-3,16 | 5 | 5 | 60,00% | 0,97 | €-0,63 | 1,49% |
| TEST | Combo Adaptive — Quality7 | Combo Adaptive | €10.010,16 | €10,16 | 29 | 29 | 34,48% | 1,02 | €0,35 | 2,73% |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | Momentum / breakout V3 Filtered | €10.008,92 | €8,92 | 30 | 30 | 36,67% | 1,02 | €0,30 | 4,84% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €10.003,85 | €3,85 | 23 | 23 | 43,48% | 1,04 | €0,17 | 0,33% |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | Momentum / breakout V3 Filtered | €10.003,37 | €3,37 | 8 | 8 | 37,50% | 1,02 | €0,42 | 2,15% |
| TEST | Scalp RSI Short 85 · €50 · 15x | Inversione RSI estrema 15m | €10.001,42 | €1,42 | 3 | 3 | 66,67% | 2,74 | €0,47 | 0,08% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €10.000,77 | €0,77 | 23 | 23 | 43,48% | 1,04 | €0,03 | 0,07% |
| TEST | Scalp RSI Short 85 · €10 · 15x | Inversione RSI estrema 15m | €10.000,28 | €0,28 | 3 | 3 | 66,67% | 2,74 | €0,09 | 0,02% |
| TEST | Scanner Bottom5 Short Continuation V1 | Scanner Bottom5 Short Continuation | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 85 · prudente · 5x | Inversione RSI estrema 15m | €9.999,47 | €-0,53 | 3 | 3 | 66,67% | 0,77 | €-0,18 | 0,16% |
| TEST | Scalp RSI Long 15 · €10 · 15x | Inversione RSI estrema 15m | €9.997,60 | €-2,40 | 3 | 3 | 33,33% | 0,13 | €-0,80 | 0,02% |
| TEST | Scalp RSI Long 20 · €10 · 15x | Inversione RSI estrema 15m | €9.996,51 | €-3,31 | 7 | 7 | 28,57% | 0,24 | €-0,47 | 0,04% |
| TEST | Rapida V1 — Long + BTC 1–3 + score <7,5 | Momentum / breakout | €9.996,45 | €-3,55 | 25 | 25 | 36,00% | 0,99 | €-0,14 | 2,27% |
| TEST | Scalp RSI Long 20 · prudente · 5x | Inversione RSI estrema 15m | €9.996,32 | €-2,30 | 7 | 7 | 42,86% | 0,94 | €-0,33 | 0,36% |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | Momentum / breakout V3 Filtered | €9.995,23 | €-4,77 | 15 | 15 | 46,67% | 0,99 | €-0,32 | 2,70% |
| TEST | Scalp RSI Short 80 · €10 · 15x | Inversione RSI estrema 15m | €9.994,44 | €-5,56 | 11 | 11 | 27,27% | 0,38 | €-0,51 | 0,11% |
| TEST | Scalp RSI Long 25 · €10 · 15x | Inversione RSI estrema 15m | €9.988,86 | €-10,96 | 13 | 13 | 30,77% | 0,26 | €-0,84 | 0,14% |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | €9.988,00 | €-12,00 | 3 | 3 | 33,33% | 0,13 | €-4,00 | 0,12% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €9.985,00 | €-15,00 | 2 | 2 | 50,00% | 0,71 | €-7,50 | 0,79% |
| TEST | Rapida V3 senza ESPORTS — MFE Lock | Momentum / breakout V3 Filtered | €9.983,91 | €-22,02 | 62 | 62 | 50,00% | 0,98 | €-0,36 | 4,32% |
| TEST | Scalp RSI Long 20 · €50 · 15x | Inversione RSI estrema 15m | €9.982,55 | €-16,55 | 7 | 7 | 28,57% | 0,24 | €-2,36 | 0,20% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €9.982,09 | €-17,91 | 2 | 2 | 50,00% | 0,65 | €-8,96 | 0,77% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €9.981,34 | €-18,66 | 7 | 7 | 57,14% | 0,89 | €-2,67 | 1,27% |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | €9.980,94 | €-19,06 | 3 | 3 | 33,33% | 0,19 | €-6,35 | 0,20% |
| TEST | Rapida V1 — target pieno 2R | Momentum / breakout | €9.976,30 | €-29,39 | 85 | 85 | 36,47% | 0,98 | €-0,35 | 2,94% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €9.972,77 | €-40,46 | 4 | 4 | 50,00% | 0,63 | €-10,11 | 0,89% |
| TEST | Scalp RSI Short 80 · €50 · 15x | Inversione RSI estrema 15m | €9.972,22 | €-27,78 | 11 | 11 | 27,27% | 0,38 | €-2,53 | 0,53% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.970,30 | €-29,70 | 5 | 5 | 40,00% | 0,82 | €-5,94 | 1,89% |
| TEST | Top 5 + BTC — BTC 2–3 | Scanner Top 5 + forza BTC | €9.968,72 | €-31,28 | 10 | 10 | 30,00% | 0,87 | €-3,13 | 2,84% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €9.959,49 | €-40,51 | 2 | 2 | 50,00% | 0,28 | €-20,26 | 0,91% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €9.956,89 | €-97,98 | 4 | 4 | 25,00% | 0,41 | €-24,49 | 1,89% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €9.951,84 | €-46,79 | 13 | 13 | 30,77% | 0,37 | €-3,60 | 0,71% |
| TEST | Btc Ema 4H | Trend following EMA | €9.950,68 | €-49,32 | 1 | 1 | 0,00% | 0,00 | €-49,32 | 0,96% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €9.949,62 | €-50,38 | 1 | 1 | 0,00% | 0,00 | €-50,38 | 0,74% |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | €9.944,32 | €-54,78 | 13 | 13 | 30,77% | 0,26 | €-4,21 | 0,72% |
| TEST | Bilanciata 1H — SHORT Trend Down stretto | Confluenza trend | €9.943,38 | €-56,62 | 2 | 2 | 0,00% | 0,00 | €-28,31 | 1,11% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €9.928,15 | €-83,61 | 18 | 16 | 38,89% | 0,81 | €-4,64 | 2,38% |
| TEST | Scalp RSI Short 80 · prudente · 5x | Inversione RSI estrema 15m | €9.925,12 | €-74,88 | 11 | 11 | 27,27% | 0,10 | €-6,81 | 0,89% |
| TEST | Combo Adaptive — Quality7 + Regime + parziale 1R | Combo Adaptive | €9.922,04 | €-77,96 | 11 | 11 | 45,45% | 0,71 | €-7,09 | 1,95% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.921,51 | €-78,49 | 23 | 23 | 43,48% | 0,39 | €-3,41 | 0,84% |
| TEST | Rapida 1H V3 Filtered — madre | Momentum / breakout V3 Filtered | €9.918,67 | €-87,22 | 106 | 106 | 37,74% | 0,96 | €-0,82 | 4,29% |
| TEST | Combo Adaptive — Trend/Transition | Combo Adaptive | €9.903,28 | €-96,72 | 22 | 22 | 45,45% | 0,79 | €-4,40 | 2,18% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €9.898,26 | €-101,74 | 2 | 2 | 0,00% | 0,00 | €-50,87 | 1,48% |
| TEST | Eth Ema 4H | Trend following EMA | €9.894,27 | €-105,73 | 2 | 2 | 0,00% | 0,00 | €-52,87 | 1,21% |
| TEST | Btc Ema 1H | Trend following EMA | €9.886,33 | €-141,33 | 7 | 7 | 28,57% | 0,48 | €-20,19 | 1,72% |
| TEST | Sol Ema 1H | Trend following EMA | €9.885,39 | €-132,14 | 7 | 7 | 28,57% | 0,52 | €-18,88 | 2,16% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.871,99 | €-128,01 | 5 | 5 | 20,00% | 0,42 | €-25,60 | 1,62% |
| TEST | Combo Adaptive — target pieno 3R | Combo Adaptive | €9.846,50 | €-188,25 | 32 | 32 | 34,38% | 0,70 | €-5,88 | 2,62% |
| TEST | Sol Ema 4H | Trend following EMA | €9.845,78 | €-154,22 | 3 | 3 | 0,00% | 0,00 | €-51,41 | 1,57% |
| TEST | Rapida V3 — qualità completa + profit lock | Momentum / breakout V3 Filtered | €9.841,82 | €-157,84 | 50 | 50 | 46,00% | 0,87 | €-3,16 | 3,21% |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | Momentum / breakout V3 Filtered | €9.837,38 | €-162,62 | 37 | 37 | 40,54% | 0,76 | €-4,40 | 3,08% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €9.834,35 | €-234,54 | 58 | 57 | 36,21% | 0,88 | €-4,04 | 6,44% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | Momentum / breakout V3 Filtered | €9.817,34 | €-182,66 | 24 | 24 | 41,67% | 0,64 | €-7,61 | 3,23% |
| TEST | Combo Adaptive — parziale 1R | Combo Adaptive | €9.810,98 | €-218,79 | 47 | 47 | 38,30% | 0,74 | €-4,66 | 3,97% |
| TEST | Combo Adaptive — Long Only | Combo Adaptive | €9.803,39 | €-196,09 | 22 | 22 | 22,73% | 0,60 | €-8,91 | 2,82% |
| TEST | Bilanciata V3 · LONG only | Confluenza trend V3 Filtered | €9.802,42 | €-208,71 | 27 | 27 | 33,33% | 0,67 | €-7,73 | 2,91% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.799,60 | €-200,40 | 6 | 6 | 33,33% | 0,08 | €-33,40 | 2,09% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €9.798,57 | €-218,81 | 7 | 7 | 28,57% | 0,24 | €-31,26 | 2,95% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €9.798,03 | €-201,97 | 22 | 22 | 36,36% | 0,73 | €-9,18 | 4,18% |
| TEST | Combo Adaptive — Quality7 + Regime | Combo Adaptive | €9.797,24 | €-202,76 | 11 | 11 | 27,27% | 0,31 | €-18,43 | 2,32% |
| TEST | Rapida V3 senza ESPORTS — Long Only | Momentum / breakout V3 Filtered | €9.789,25 | €-210,00 | 38 | 38 | 36,84% | 0,77 | €-5,53 | 5,84% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.782,23 | €-305,33 | 48 | 48 | 31,25% | 0,71 | €-6,36 | 4,10% |
| TEST | Rapida V3 — Long + no HIGH + score <7,5 | Momentum / breakout V3 Filtered | €9.776,15 | €-223,51 | 45 | 45 | 40,00% | 0,80 | €-4,97 | 3,40% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | Momentum / breakout V3 Filtered | €9.762,18 | €-237,82 | 7 | 7 | 14,29% | 0,02 | €-33,97 | 2,82% |
| TEST | Eth Ema 1H | Trend following EMA | €9.753,83 | €-272,13 | 8 | 8 | 25,00% | 0,16 | €-34,02 | 3,12% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.730,31 | €-269,69 | 14 | 14 | 28,57% | 0,39 | €-19,26 | 2,92% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | Momentum / breakout V3 Filtered | €9.723,72 | €-276,28 | 31 | 31 | 32,26% | 0,62 | €-8,91 | 4,83% |
| TEST | Rapida V3 — senza ESPORTS | Momentum / breakout V3 Filtered | €9.716,77 | €-289,00 | 80 | 80 | 37,50% | 0,83 | €-3,61 | 4,26% |
| TEST | Top 5 + BTC — target pieno 3R | Scanner Top 5 + forza BTC | €9.716,20 | €-283,28 | 28 | 28 | 28,57% | 0,68 | €-10,12 | 5,99% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €9.712,14 | €-254,55 | 23 | 23 | 30,43% | 0,69 | €-11,07 | 3,64% |
| TEST | Top 5 + BTC — 75% a 2,2R + runner 3R | Scanner Top 5 + forza BTC | €9.710,51 | €-288,97 | 32 | 32 | 31,25% | 0,68 | €-9,03 | 6,29% |
| TEST | Top 5 + BTC — Guard + BTC≤3 | Scanner Top 5 + forza BTC | €9.680,97 | €-318,52 | 21 | 21 | 28,57% | 0,58 | €-15,17 | 5,67% |
| TEST | Master Adaptive GB20 — Breakeven 0,5R | Master Adaptive Consensus | €9.675,65 | €-323,22 | 24 | 24 | 16,67% | 0,55 | €-13,47 | 4,69% |
| TEST | Master Adaptive GB20 — 50% a 0,75R | Master Adaptive Consensus | €9.665,37 | €-333,51 | 19 | 19 | 26,32% | 0,50 | €-17,55 | 4,27% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €9.644,57 | €-354,30 | 23 | 23 | 26,09% | 0,58 | €-15,40 | 3,98% |
| TEST | Top 5 + BTC — BTC≤3 | Scanner Top 5 + forza BTC | €9.644,05 | €-355,43 | 24 | 24 | 29,17% | 0,54 | €-14,81 | 5,74% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €9.631,95 | €-366,93 | 21 | 21 | 23,81% | 0,57 | €-17,47 | 4,03% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €9.631,88 | €-326,14 | 53 | 53 | 39,62% | 0,77 | €-6,15 | 5,90% |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | €9.627,98 | €-370,90 | 21 | 21 | 23,81% | 0,56 | €-17,66 | 4,07% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €9.622,55 | €-375,46 | 59 | 59 | 27,12% | 0,74 | €-6,36 | 7,55% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | Momentum / breakout V3 Filtered | €9.579,83 | €-420,17 | 11 | 11 | 0,00% | 0,00 | €-38,20 | 4,20% |
| TEST | Top 5 + BTC — Guard | Scanner Top 5 + forza BTC | €9.563,48 | €-436,01 | 26 | 26 | 23,08% | 0,51 | €-16,77 | 5,26% |
| TEST | Combo Trend | Combo Trend | €9.526,44 | €-534,34 | 70 | 70 | 30,00% | 0,74 | €-7,63 | 7,64% |
| TEST | Combo Scanner | Combo Scanner | €9.515,64 | €-483,84 | 53 | 53 | 33,96% | 0,68 | €-9,13 | 6,89% |
| TEST | Top 5 + BTC — Guard + BTC≤3 + MFE | Scanner Top 5 + forza BTC | €9.514,86 | €-484,63 | 36 | 36 | 33,33% | 0,54 | €-13,46 | 4,93% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €9.500,06 | €-498,83 | 56 | 56 | 53,57% | 0,52 | €-8,91 | 5,35% |
| TEST | Top 5 + BTC — solo MFE | Scanner Top 5 + forza BTC | €9.459,92 | €-539,57 | 36 | 36 | 30,56% | 0,39 | €-14,99 | 6,33% |
| TEST | Bilanciata 1H — LONG senza Range High Vol | Confluenza trend | €9.446,02 | €-526,88 | 23 | 23 | 21,74% | 0,37 | €-22,91 | 6,39% |
| TEST | Master Adaptive GB20 — Loss Cap 0,75R | Master Adaptive Consensus | €9.437,48 | €-562,18 | 23 | 23 | 17,39% | 0,41 | €-24,44 | 7,16% |
| TEST | Scanner Top10 Long | Scanner Top10 Long | €9.415,02 | €-584,48 | 24 | 24 | 25,00% | 0,29 | €-24,35 | 7,60% |
| TEST | Scanner Top15 Long | Scanner Top15 Long | €9.415,02 | €-584,48 | 24 | 24 | 25,00% | 0,29 | €-24,35 | 7,60% |
| TEST | Scanner Top20 Long | Scanner Top20 Long | €9.415,02 | €-584,48 | 24 | 24 | 25,00% | 0,29 | €-24,35 | 7,60% |
| TEST | Top 5 + BTC — Guard + MFE | Scanner Top 5 + forza BTC | €9.341,06 | €-658,44 | 43 | 43 | 32,56% | 0,48 | €-15,31 | 6,73% |
| TEST | Rapida V3 — Long Only | Momentum / breakout V3 Filtered | €9.320,43 | €-678,86 | 58 | 58 | 27,59% | 0,57 | €-11,70 | 7,87% |
| TEST | Combo Adaptive — MFE Trail esistente | Combo Adaptive | €9.295,57 | €-732,31 | 59 | 59 | 32,20% | 0,45 | €-12,41 | 7,57% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €9.223,98 | €-775,76 | 30 | 30 | 20,00% | 0,43 | €-25,86 | 8,03% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | XRP | SHORT | Confluenza trend | 240m | 3,0x | 1,01047 | 1,00040 | 1,03352 | 1,34224 | 0,96437 | €711,84 | €2.135,52 | €48,72 | €21,28 |
| Principale 4H | SPCX | LONG | Confluenza trend | 240m | 3,0x | 136,56189 | 136,56189 | 128,79610 | 91,72407 | 152,09346 | €285,50 | €856,50 | €48,71 | €0,00 |
| Principale 4H | CYS | LONG | Confluenza trend | 240m | 3,0x | 1,29448 | 1,29448 | 1,29448 | 0,86946 | 1,60515 | €137,64 | €412,91 | €0,00 | €0,00 |
| Bilanciata 1H V1 | SPCX | LONG | Confluenza trend | 60m | 3,0x | 136,85206 | 136,85206 | 132,31345 | 91,91897 | 145,92928 | €517,88 | €1.553,64 | €51,53 | €0,00 |
| Bilanciata 1H V1 | CYS | LONG | Confluenza trend | 60m | 3,0x | 1,28356 | 1,28356 | 1,31375 | 0,86212 | 1,59161 | €142,82 | €428,45 | €0,00 | €0,00 |
| Bilanciata 1H V1 | DOGE | LONG | Confluenza trend | 60m | 3,0x | 0,07057 | 0,07005 | 0,06956 | 0,04740 | 0,07260 | €18,28 | €54,85 | €0,79 | €-0,41 |
| Bilanciata 1H V1 | ZEC | SHORT | Confluenza trend | 60m | 3,0x | 486,56267 | 471,00000 | 476,70736 | 646,31741 | 471,40169 | €17,36 | €52,09 | €0,00 | €1,67 |
| Bilanciata 1H V1 | ADA | SHORT | Confluenza trend | 60m | 3,0x | 0,18533 | 0,18533 | 0,18800 | 0,24618 | 0,17999 | €1.143,13 | €3.429,40 | €49,38 | €-0,00 |
| Bilanciata 1H — LONG senza Range High Vol | CYS | LONG | Confluenza trend | 60m | 3,0x | 1,32770 | 1,32770 | 1,32770 | 0,89177 | 1,64634 | €134,09 | €402,26 | €0,00 | €0,00 |
| Bilanciata 1H — LONG senza Range High Vol | DOGE | LONG | Confluenza trend | 60m | 3,0x | 0,07057 | 0,07005 | 0,06956 | 0,04740 | 0,07260 | €1.117,95 | €3.353,85 | €48,30 | €-24,82 |
| Bilanciata 1H V2 | CYS | LONG | Confluenza trend V2 | 60m | 3,0x | 1,32770 | 1,32770 | 1,32770 | 0,89177 | 1,64634 | €142,72 | €428,16 | €0,00 | €0,00 |
| Bilanciata 1H V2 | ADA | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,18533 | 0,18533 | 0,18800 | 0,24618 | 0,17999 | €1.179,68 | €3.539,03 | €50,96 | €-0,00 |
| Bilanciata 1H V2 | SOL | SHORT | Confluenza trend V2 | 60m | 3,0x | 75,18996 | 74,76000 | 76,27269 | 99,87733 | 73,02449 | €1.137,85 | €3.413,54 | €49,15 | €19,52 |
| Bilanciata 1H V3 Filtered | SPCX | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 136,85206 | 136,85206 | 132,31345 | 91,91897 | 145,92928 | €524,66 | €1.573,99 | €52,20 | €0,00 |
| Bilanciata 1H V3 Filtered | CYS | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1,33140 | 1,33140 | 1,17163 | 0,89426 | 1,65093 | €142,48 | €427,43 | €51,29 | €0,00 |
| Bilanciata 1H V3 Filtered | ZEC | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 486,56267 | 471,00000 | 476,70736 | 646,31741 | 471,40169 | €16,19 | €48,57 | €0,00 | €1,55 |
| Bilanciata 1H V3 Filtered | ADA | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,18533 | 0,18533 | 0,18800 | 0,24618 | 0,17999 | €1.207,94 | €3.623,82 | €52,18 | €-0,00 |
| Bilanciata 1H V3 Filtered | BTC | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 63807,23600 | 63524,90000 | 64726,06020 | 84757,27849 | 61969,58760 | €1.129,53 | €3.388,60 | €48,80 | €14,99 |
| Rapida V1 — score 6–7,5 | CYS | LONG | Momentum / breakout | 60m | 3,0x | 1,33140 | 1,33140 | 1,35248 | 0,89426 | 1,52898 | €175,99 | €527,96 | €0,00 | €0,00 |
| Rapida V1 — score 6–7,5 | BTC | SHORT | Momentum / breakout | 60m | 3,0x | 63807,23600 | 63524,90000 | 64521,87704 | 84757,27849 | 62735,27444 | €1.575,50 | €4.726,51 | €52,94 | €20,91 |
| Rapida V1 — score 6–7,5 | ZEC | SHORT | Momentum / breakout | 60m | 3,0x | 475,00498 | 471,00000 | 481,54658 | 630,96495 | 465,19258 | €1.280,85 | €3.842,54 | €52,92 | €32,40 |
| Rapida score 6–7,5 — senza Trend Up | CYS | LONG | Momentum / breakout | 60m | 3,0x | 1,33140 | 1,33140 | 1,35248 | 0,89426 | 1,52898 | €171,31 | €513,92 | €0,00 | €0,00 |
| Rapida score 6–7,5 — senza Trend Up | BTC | SHORT | Momentum / breakout | 60m | 3,0x | 63807,23600 | 63524,90000 | 64521,87704 | 84757,27849 | 62735,27444 | €1.533,61 | €4.600,84 | €51,53 | €20,36 |
| Rapida score 6–7,5 — senza Trend Up | ZEC | SHORT | Momentum / breakout | 60m | 3,0x | 475,00498 | 471,00000 | 481,54658 | 630,96495 | 465,19258 | €1.246,79 | €3.740,37 | €51,51 | €31,54 |
| Rapida score 6–7,5 — Range Only | CYS | LONG | Momentum / breakout | 60m | 3,0x | 1,33920 | 1,33920 | 1,36751 | 0,89950 | 1,51411 | €195,52 | €586,56 | €0,00 | €0,00 |
| Rapida score 6–7,5 — Range Only | BTC | SHORT | Momentum / breakout | 60m | 3,0x | 63807,23600 | 63524,90000 | 64521,87704 | 84757,27849 | 62735,27444 | €1.542,02 | €4.626,07 | €51,81 | €20,47 |
| Rapida score 6–7,5 — Range Only | ZEC | SHORT | Momentum / breakout | 60m | 3,0x | 475,00498 | 471,00000 | 481,54658 | 630,96495 | 465,19258 | €1.253,63 | €3.760,88 | €51,79 | €31,71 |
| Rapida score 6–7,5 — Cost Aware | BTC | SHORT | Momentum / breakout | 60m | 3,0x | 63807,23600 | 63524,90000 | 64521,87704 | 84757,27849 | 62735,27444 | €1.591,68 | €4.775,04 | €53,48 | €21,13 |
| Rapida score 6–7,5 — Cost Aware | ZEC | SHORT | Momentum / breakout | 60m | 3,0x | 475,00498 | 471,00000 | 481,54658 | 630,96495 | 465,19258 | €1.294,00 | €3.881,99 | €53,46 | €32,73 |
| Rapida V1 — no HIGH + score <7,5 | CYS | LONG | Momentum / breakout | 60m | 3,0x | 1,32770 | 1,32770 | 1,35661 | 0,89177 | 1,51824 | €182,77 | €548,30 | €0,00 | €0,00 |
| Rapida V1 — no HIGH + score <7,5 | BTC | SHORT | Momentum / breakout | 60m | 3,0x | 63807,23600 | 63524,90000 | 64521,87704 | 84757,27849 | 62735,27444 | €1.585,67 | €4.757,02 | €53,28 | €21,05 |
| Rapida V1 — no HIGH + score <7,5 | ZEC | SHORT | Momentum / breakout | 60m | 3,0x | 475,00498 | 471,00000 | 481,54658 | 630,96495 | 465,19258 | €1.289,11 | €3.867,34 | €53,26 | €32,61 |
| Rapida V1 — no HIGH + score <7,5 | SOL | SHORT | Momentum / breakout | 60m | 3,0x | 75,18996 | 74,76000 | 76,03209 | 99,87733 | 73,92677 | €1.584,65 | €4.753,94 | €53,24 | €27,18 |
| Rapida V1 — senza PEPE | CYS | LONG | Momentum / breakout | 60m | 3,0x | 1,28356 | 1,28356 | 1,33719 | 0,86212 | 1,49729 | €152,86 | €458,58 | €0,00 | €0,00 |
| Rapida V1 — senza PEPE | SPCX | LONG | Momentum / breakout | 60m | 3,0x | 136,80203 | 136,80203 | 133,40452 | 91,88536 | 141,89830 | €682,89 | €2.048,66 | €50,88 | €0,00 |
| Rapida V1 — senza PEPE | XRP | SHORT | Momentum / breakout | 60m | 3,0x | 0,99862 | 1,00040 | 1,00980 | 1,32650 | 0,98184 | €1.518,74 | €4.556,22 | €51,03 | €-8,12 |
| Rapida V1 — senza PEPE | BTC | SHORT | Momentum / breakout | 60m | 3,0x | 63807,23600 | 63524,90000 | 64521,87704 | 84757,27849 | 62735,27444 | €1.518,20 | €4.554,59 | €51,01 | €20,15 |
| Rapida V1 — target pieno 2R | CYS | LONG | Momentum / breakout | 60m | 3,0x | 1,28356 | 1,28356 | 1,33719 | 0,86212 | 1,56853 | €149,69 | €449,08 | €0,00 | €0,00 |
| Rapida V1 — target pieno 2R | SPCX | LONG | Momentum / breakout | 60m | 3,0x | 136,80203 | 136,80203 | 133,40452 | 91,88536 | 143,59705 | €668,73 | €2.006,20 | €49,82 | €0,00 |
| Rapida V1 — target pieno 2R | XRP | SHORT | Momentum / breakout | 60m | 3,0x | 0,99862 | 1,00040 | 1,00980 | 1,32650 | 0,97625 | €1.483,62 | €4.450,85 | €49,85 | €-7,93 |
| Rapida V1 — target pieno 2R | BTC | SHORT | Momentum / breakout | 60m | 3,0x | 63807,23600 | 63524,90000 | 64521,87704 | 84757,27849 | 62377,95391 | €1.482,17 | €4.446,51 | €49,80 | €19,68 |
| Rapida 1H V2 | CYS | LONG | Momentum / breakout V2 | 60m | 3,0x | 1,37342 | 1,37342 | 1,37342 | 0,92248 | 1,55049 | €193,41 | €580,23 | €0,00 | €0,00 |
| Rapida 1H V2 | XRP | SHORT | Momentum / breakout V2 | 60m | 3,0x | 0,99862 | 1,00040 | 1,00980 | 1,32650 | 0,98184 | €1.475,60 | €4.426,81 | €49,58 | €-7,89 |
| Rapida 1H V2 | SOL | SHORT | Momentum / breakout V2 | 60m | 3,0x | 75,18996 | 74,76000 | 76,03209 | 99,87733 | 73,92677 | €1.475,07 | €4.425,22 | €49,56 | €25,30 |
| Rapida 1H V3 Filtered — madre | SPCX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 136,80203 | 136,80203 | 133,40452 | 91,88536 | 141,89830 | €672,56 | €2.017,68 | €50,11 | €0,00 |
| Rapida 1H V3 Filtered — madre | CYS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,33140 | 1,33140 | 1,35248 | 0,89426 | 1,52898 | €163,19 | €489,56 | €0,00 | €0,00 |
| Rapida 1H V3 Filtered — madre | XRP | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,99862 | 1,00040 | 1,00980 | 1,32650 | 0,98184 | €1.475,01 | €4.425,02 | €49,56 | €-7,89 |
| Rapida 1H V3 Filtered — madre | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 63807,23600 | 63524,90000 | 64521,87704 | 84757,27849 | 62735,27444 | €1.474,48 | €4.423,44 | €49,54 | €19,57 |
| Rapida 1H V3 Filtered — madre | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 475,00498 | 471,00000 | 481,54658 | 630,96495 | 465,19258 | €10,97 | €32,92 | €0,45 | €0,28 |
| Rapida V3 — score <7,5 | SPCX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 136,80203 | 136,80203 | 133,40452 | 91,88536 | 141,89830 | €685,11 | €2.055,32 | €51,04 | €0,00 |
| Rapida V3 — score <7,5 | CYS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,33140 | 1,33140 | 1,35248 | 0,89426 | 1,52898 | €171,42 | €514,25 | €0,00 | €0,00 |
| Rapida V3 — score <7,5 | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 63807,23600 | 63524,90000 | 64521,87704 | 84757,27849 | 62735,27444 | €1.501,29 | €4.503,87 | €50,44 | €19,93 |
| Rapida V3 — score <7,5 | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 475,00498 | 471,00000 | 481,54658 | 630,96495 | 465,19258 | €1.194,18 | €3.582,54 | €49,34 | €30,21 |
| Rapida V3 — no volatilità HIGH | CYS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,33920 | 1,33920 | 1,36751 | 0,89950 | 1,51411 | €188,87 | €566,60 | €0,00 | €0,00 |
| Rapida V3 — no volatilità HIGH | XRP | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,99862 | 1,00040 | 1,00980 | 1,32650 | 0,98184 | €1.489,56 | €4.468,68 | €50,05 | €-7,96 |
| Rapida V3 — no volatilità HIGH | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 63807,23600 | 63524,90000 | 64521,87704 | 84757,27849 | 62735,27444 | €1.489,03 | €4.467,09 | €50,03 | €19,77 |
| Rapida V3 — no volatilità HIGH | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 475,00498 | 471,00000 | 481,54658 | 630,96495 | 465,19258 | €1.210,54 | €3.631,63 | €50,01 | €30,62 |
| Rapida V3 — Long Only | SPCX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 136,80203 | 136,80203 | 133,40452 | 91,88536 | 141,89830 | €633,63 | €1.900,88 | €47,21 | €0,00 |
| Rapida V3 — Long Only | CYS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,33140 | 1,33140 | 1,35248 | 0,89426 | 1,52898 | €158,54 | €475,61 | €0,00 | €0,00 |
| Rapida V3 — Long + no HIGH + score <7,5 | CYS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,33920 | 1,33920 | 1,36751 | 0,89950 | 1,51411 | €188,69 | €566,07 | €0,00 | €0,00 |
| Rapida V3 — senza ESPORTS | SPCX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 136,80203 | 136,80203 | 133,40452 | 91,88536 | 141,89830 | €658,87 | €1.976,61 | €49,09 | €0,00 |
| Rapida V3 — senza ESPORTS | CYS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,33140 | 1,33140 | 1,35248 | 0,89426 | 1,52898 | €159,86 | €479,59 | €0,00 | €0,00 |
| Rapida V3 — senza ESPORTS | XRP | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,99862 | 1,00040 | 1,00980 | 1,32650 | 0,98184 | €1.444,98 | €4.334,94 | €48,55 | €-7,73 |
| Rapida V3 — senza ESPORTS | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 63807,23600 | 63524,90000 | 64521,87704 | 84757,27849 | 62735,27444 | €1.444,46 | €4.333,39 | €48,53 | €19,17 |
| Rapida V3 — senza ESPORTS | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 475,00498 | 471,00000 | 481,54658 | 630,96495 | 465,19258 | €10,75 | €32,25 | €0,44 | €0,27 |
| Rapida V3 senza ESPORTS — Long Only | SPCX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 136,80203 | 136,80203 | 133,40452 | 91,88536 | 141,89830 | €665,50 | €1.996,50 | €49,58 | €0,00 |
| Rapida V3 senza ESPORTS — Long Only | CYS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,33140 | 1,33140 | 1,35248 | 0,89426 | 1,52898 | €166,51 | €499,53 | €0,00 | €0,00 |
| Rapida V3 senza ESPORTS — MFE Lock | SPCX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 136,80203 | 136,80203 | 133,40452 | 91,88536 | 141,89830 | €676,98 | €2.030,95 | €50,44 | €0,00 |
| Rapida V3 senza ESPORTS — MFE Lock | CYS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,33140 | 1,33140 | 1,35248 | 0,89426 | 1,52898 | €164,26 | €492,78 | €0,00 | €0,00 |
| Rapida V3 senza ESPORTS — MFE Lock | XRP | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,99862 | 1,00040 | 1,00980 | 1,32650 | 0,98184 | €1.484,71 | €4.454,12 | €49,89 | €-7,94 |
| Rapida V3 senza ESPORTS — MFE Lock | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 63807,23600 | 63524,90000 | 64521,87704 | 84757,27849 | 62735,27444 | €1.484,18 | €4.452,53 | €49,87 | €19,70 |
| Rapida V3 senza ESPORTS — MFE Lock | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 475,00498 | 471,00000 | 481,54658 | 630,96495 | 465,19258 | €11,04 | €33,13 | €0,46 | €0,28 |
| Rapida V3 senza ESPORTS — Stress Guard | XRP | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,99862 | 1,00040 | 1,00980 | 1,32650 | 0,98184 | €1.499,39 | €4.498,17 | €50,38 | €-8,02 |
| Rapida V3 senza ESPORTS — Stress Guard | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 63807,23600 | 63524,90000 | 64521,87704 | 84757,27849 | 62735,27444 | €1.498,86 | €4.496,57 | €50,36 | €19,90 |
| Rapida V3 senza ESPORTS — Stress Guard | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 475,00498 | 471,00000 | 481,54658 | 630,96495 | 465,19258 | €1.218,53 | €3.655,60 | €50,34 | €30,82 |
| Rapida V3 — qualità completa + profit lock | CYS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,33920 | 1,33920 | 1,22260 | 0,89950 | 1,51411 | €189,96 | €569,87 | €49,62 | €0,00 |
| Ampia 4H | XMR | LONG | Confluenza trend | 240m | 2,0x | 364,45854 | 364,45854 | 386,58243 | 184,05156 | 410,69083 | €544,42 | €1.088,84 | €0,00 | €0,00 |
| Ampia 4H | DOGE | SHORT | Confluenza trend | 240m | 2,0x | 0,07002 | 0,07005 | 0,07288 | 0,10467 | 0,06199 | €17,06 | €34,13 | €1,40 | €-0,02 |
| Ampia 4H | XRP | SHORT | Confluenza trend | 240m | 2,0x | 1,01047 | 1,00040 | 1,04043 | 1,51065 | 0,92656 | €831,51 | €1.663,02 | €49,32 | €16,57 |
| Ampia 4H | SPCX | LONG | Confluenza trend | 240m | 2,0x | 136,56189 | 136,56189 | 126,46637 | 68,96375 | 164,82935 | €323,86 | €647,73 | €47,88 | €0,00 |
| Ampia 4H | CYS | LONG | Confluenza trend | 240m | 2,0x | 1,29448 | 1,29448 | 1,13914 | 0,65371 | 1,72942 | €208,60 | €417,20 | €50,06 | €0,00 |
| Forza relativa 1H V1 | SPCX | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 146,83700 | €726,10 | €1.452,21 | €48,16 | €0,00 |
| Forza relativa 1H V1 | CYS | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 1,28356 | 1,28356 | 1,30203 | 0,64820 | 1,62242 | €200,59 | €401,18 | €0,00 | €0,00 |
| Forza relativa 1H V1 | ZEC | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 486,56267 | 471,00000 | 477,11503 | 727,41119 | 469,88559 | €124,55 | €249,10 | €0,00 | €7,97 |
| Forza relativa 1H V1 | ADA | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17946 | €1.677,78 | €3.355,57 | €48,32 | €-0,00 |
| Forza relativa 1H V1 | XRP | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,99862 | 1,00040 | 1,01300 | 1,49294 | 0,96698 | €1.529,53 | €3.059,06 | €44,05 | €-5,45 |
| Forza relativa 1H V2 | CYS | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 1,32770 | 1,32770 | 1,16837 | 0,67049 | 1,67821 | €206,96 | €413,93 | €49,67 | €0,00 |
| Forza relativa 1H V2 | ZEC | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 482,10356 | 471,00000 | 477,03759 | 720,74482 | 465,78857 | €1.587,07 | €3.174,15 | €0,00 | €73,11 |
| Forza relativa 1H V2 | ADA | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17946 | €1.698,68 | €3.397,35 | €48,92 | €-0,00 |
| Scalp RSI Long 20 · €10 · 15x | PEPE | LONG | Inversione RSI estrema 15m | 15m | 15,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €10,00 | €150,00 | €1,31 | €-0,09 |
| Scalp RSI Long 25 · €10 · 15x | PEPE | LONG | Inversione RSI estrema 15m | 15m | 15,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €10,00 | €150,00 | €1,31 | €-0,09 |
| Scalp RSI Long 20 · €50 · 15x | PEPE | LONG | Inversione RSI estrema 15m | 15m | 15,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €50,00 | €750,00 | €6,55 | €-0,45 |
| Scalp RSI Long 25 · €50 · 15x | PEPE | LONG | Inversione RSI estrema 15m | 15m | 15,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €50,00 | €750,00 | €6,55 | €-0,45 |
| Scalp RSI Long 20 · prudente · 5x | PEPE | LONG | Inversione RSI estrema 15m | 15m | 5,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €229,00 | €1.145,02 | €10,00 | €-0,69 |
| Scalp RSI Long 25 · prudente · 5x | PEPE | LONG | Inversione RSI estrema 15m | 15m | 5,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €227,99 | €1.139,93 | €9,95 | €-0,68 |
| Benchmark Donchian breakout 1H | XRP | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 1,01197 | 1,00040 | 1,00817 | 1,51289 | 0,97149 | €1.650,43 | €3.300,86 | €0,00 | €37,73 |
| Benchmark Donchian breakout 1H | ZEC | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 491,45169 | 471,00000 | 478,01957 | 734,72028 | 468,56302 | €1.415,57 | €2.831,15 | €0,00 | €117,82 |
| Benchmark Donchian breakout 1H | CYS | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1,37342 | 1,37342 | 1,20861 | 0,69358 | 1,78545 | €222,66 | €445,33 | €53,44 | €0,00 |
| Benchmark Donchian breakout 1H | BTC | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 63807,23600 | 63524,90000 | 64828,15178 | 95391,81782 | 61254,94656 | €1.676,44 | €3.352,88 | €53,65 | €14,84 |
| Benchmark Donchian breakout 1H | SOL | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 75,18996 | 74,76000 | 76,39300 | 112,40899 | 72,18236 | €59,02 | €118,05 | €1,89 | €0,68 |
| Donchian 1H Gb20 120R V1 | XRP | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 1,01197 | 1,00040 | 1,00817 | 1,51289 | 0,97149 | €1.611,57 | €3.223,15 | €0,00 | €36,84 |
| Donchian 1H Gb20 120R V1 | ZEC | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 491,45169 | 471,00000 | 478,01957 | 734,72028 | 468,56302 | €1.382,25 | €2.764,49 | €0,00 | €115,04 |
| Donchian 1H Gb20 120R V1 | CYS | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1,37342 | 1,37342 | 1,20861 | 0,69358 | 1,78545 | €217,42 | €434,84 | €52,18 | €0,00 |
| Donchian 1H Gb20 120R V1 | BTC | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 63807,23600 | 63524,90000 | 64828,15178 | 95391,81782 | 61254,94656 | €1.636,97 | €3.273,94 | €52,38 | €14,49 |
| Donchian 1H Gb20 120R V1 | SOL | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 75,18996 | 74,76000 | 76,39300 | 112,40899 | 72,18236 | €57,63 | €115,27 | €1,84 | €0,66 |
| Benchmark Bollinger mean reversion 1H | CYS | SHORT | Bollinger mean reversion | 60m | 2,0x | 1,45822 | 1,45822 | 1,58290 | 2,18005 | 1,27120 | €284,88 | €569,76 | €48,72 | €-0,00 |
| Benchmark Bollinger mean reversion 1H | ZEC | LONG | Bollinger mean reversion | 60m | 2,0x | 475,19502 | 471,00000 | 468,18336 | 239,97349 | 485,71251 | €1.642,69 | €3.285,38 | €48,48 | €-29,00 |
| Benchmark Bollinger mean reversion 1H | XRP | LONG | Bollinger mean reversion | 60m | 2,0x | 1,00256 | 1,00040 | 0,99053 | 0,50629 | 1,02061 | €1.935,47 | €3.870,94 | €46,45 | €-8,34 |
| Benchmark trend following EMA 1H | BTC | SHORT | Trend following EMA | 60m | 2,0x | 64070,44335 | 63524,90000 | 65095,57044 | 95785,31281 | 61815,16374 | €1.516,95 | €3.033,89 | €48,54 | €25,83 |
| Benchmark trend following EMA 1H | SPCX | LONG | Trend following EMA | 60m | 2,0x | 136,85206 | 136,85206 | 131,80916 | 69,11029 | 147,94644 | €658,50 | €1.316,99 | €48,53 | €0,00 |
| Benchmark trend following EMA 1H | ZEC | SHORT | Trend following EMA | 60m | 2,0x | 482,10356 | 471,00000 | 490,34345 | 720,74482 | 463,97579 | €1.405,03 | €2.810,05 | €48,03 | €64,72 |
| Benchmark trend following EMA 1H | ADA | SHORT | Trend following EMA | 60m | 2,0x | 0,18533 | 0,18533 | 0,18829 | 0,27707 | 0,17881 | €28,20 | €56,39 | €0,90 | €-0,00 |
| Benchmark trend following EMA 1H | SOL | SHORT | Trend following EMA | 60m | 2,0x | 75,18996 | 74,76000 | 76,39300 | 112,40899 | 72,54327 | €26,53 | €53,05 | €0,85 | €0,30 |
| Scanner Top 5 Long 1H | CYS | LONG | Scanner Top 5 Long | 60m | 2,0x | 1,28356 | 1,28356 | 1,31375 | 0,64820 | 1,59161 | €215,74 | €431,48 | €0,00 | €0,00 |
| Scanner Top 5 Long 1H | SPCX | LONG | Scanner Top 5 Long | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 145,92928 | €780,60 | €1.561,19 | €51,78 | €0,00 |
| Scanner Bottom 5 Short 1H | BTC | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 64070,44335 | 63524,90000 | 64993,05773 | 95785,31281 | 62225,21458 | €1.717,08 | €3.434,17 | €49,45 | €29,24 |
| Scanner Bottom 5 Short 1H | ADA | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17999 | €1.735,51 | €3.471,03 | €49,98 | €-0,00 |
| Scanner Bottom 5 Short 1H | ZEC | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 474,59506 | 471,00000 | 482,99843 | 709,51962 | 457,78833 | €1.415,93 | €2.831,85 | €50,14 | €21,45 |
| Scanner Top10 Long | CYS | LONG | Scanner Top10 Long | 60m | 2,0x | 1,28356 | 1,28356 | 1,31375 | 0,64820 | 1,59161 | €198,71 | €397,43 | €0,00 | €0,00 |
| Scanner Top10 Long | SPCX | LONG | Scanner Top10 Long | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 145,92928 | €718,99 | €1.437,98 | €47,69 | €0,00 |
| Scanner Bottom10 Short | BTC | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 64070,44335 | 63524,90000 | 64993,05773 | 95785,31281 | 62225,21458 | €1.728,30 | €3.456,61 | €49,78 | €29,43 |
| Scanner Bottom10 Short | ADA | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17999 | €1.763,98 | €3.527,95 | €50,80 | €-0,00 |
| Scanner Bottom10 Short | SOL | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 75,18996 | 74,76000 | 76,27269 | 112,40899 | 73,02449 | €1.771,42 | €3.542,83 | €51,02 | €20,26 |
| Scanner Bottom10 Short | ZEC | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 474,59506 | 471,00000 | 482,99843 | 709,51962 | 457,78833 | €59,91 | €119,83 | €2,12 | €0,91 |
| Scanner Top15 Long | CYS | LONG | Scanner Top15 Long | 60m | 2,0x | 1,28356 | 1,28356 | 1,31375 | 0,64820 | 1,59161 | €198,71 | €397,43 | €0,00 | €0,00 |
| Scanner Top15 Long | SPCX | LONG | Scanner Top15 Long | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 145,92928 | €718,99 | €1.437,98 | €47,69 | €0,00 |
| Scanner Bottom15 Short | BTC | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 64070,44335 | 63524,90000 | 64993,05773 | 95785,31281 | 62225,21458 | €1.728,30 | €3.456,61 | €49,78 | €29,43 |
| Scanner Bottom15 Short | ADA | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17999 | €1.763,98 | €3.527,95 | €50,80 | €-0,00 |
| Scanner Bottom15 Short | SOL | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 75,18996 | 74,76000 | 76,27269 | 112,40899 | 73,02449 | €1.771,42 | €3.542,83 | €51,02 | €20,26 |
| Scanner Bottom15 Short | ZEC | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 474,59506 | 471,00000 | 482,99843 | 709,51962 | 457,78833 | €59,91 | €119,83 | €2,12 | €0,91 |
| Scanner Top20 Long | CYS | LONG | Scanner Top20 Long | 60m | 2,0x | 1,28356 | 1,28356 | 1,31375 | 0,64820 | 1,59161 | €198,71 | €397,43 | €0,00 | €0,00 |
| Scanner Top20 Long | SPCX | LONG | Scanner Top20 Long | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 145,92928 | €718,99 | €1.437,98 | €47,69 | €0,00 |
| Scanner Bottom20 Short | BTC | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 64070,44335 | 63524,90000 | 64993,05773 | 95785,31281 | 62225,21458 | €1.728,30 | €3.456,61 | €49,78 | €29,43 |
| Scanner Bottom20 Short | ADA | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17999 | €1.763,98 | €3.527,95 | €50,80 | €-0,00 |
| Scanner Bottom20 Short | SOL | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 75,18996 | 74,76000 | 76,27269 | 112,40899 | 73,02449 | €1.771,42 | €3.542,83 | €51,02 | €20,26 |
| Scanner Bottom20 Short | ZEC | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 474,59506 | 471,00000 | 482,99843 | 709,51962 | 457,78833 | €59,91 | €119,83 | €2,12 | €0,91 |
| Scanner Top 5 + forza BTC 1H | CYS | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,28356 | 1,28356 | 1,31375 | 0,64820 | 1,62242 | €213,00 | €426,01 | €0,00 | €0,00 |
| Scanner Top 5 + forza BTC 1H | SPCX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 146,83700 | €770,70 | €1.541,40 | €51,12 | €0,00 |
| Top 5 + BTC — solo MFE | CYS | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,28356 | 1,28356 | 1,31375 | 0,64820 | 1,62242 | €199,66 | €399,32 | €0,00 | €0,00 |
| Top 5 + BTC — solo MFE | SPCX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 146,83700 | €722,42 | €1.444,84 | €47,92 | €0,00 |
| Top 5 + BTC — Guard | CYS | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,28356 | 1,28356 | 1,31375 | 0,64820 | 1,62242 | €201,85 | €403,69 | €0,00 | €0,00 |
| Top 5 + BTC — Guard | SPCX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 146,83700 | €730,33 | €1.460,65 | €48,44 | €0,00 |
| Top 5 + BTC — BTC≤3 | CYS | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,28356 | 1,28356 | 1,31375 | 0,64820 | 1,62242 | €203,55 | €407,09 | €0,00 | €0,00 |
| Top 5 + BTC — BTC≤3 | SPCX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 146,83700 | €736,48 | €1.472,96 | €48,85 | €0,00 |
| Top 5 + BTC — Guard + MFE | CYS | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,28356 | 1,28356 | 1,31375 | 0,64820 | 1,62242 | €197,15 | €394,30 | €0,00 | €0,00 |
| Top 5 + BTC — Guard + MFE | SPCX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 146,83700 | €713,34 | €1.426,68 | €47,31 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 | CYS | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,28356 | 1,28356 | 1,31375 | 0,64820 | 1,62242 | €204,33 | €408,65 | €0,00 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 | SPCX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 146,83700 | €739,30 | €1.478,60 | €49,04 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | CYS | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,28356 | 1,28356 | 1,31375 | 0,64820 | 1,62242 | €200,82 | €401,64 | €0,00 | €0,00 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | SPCX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 146,83700 | €726,61 | €1.453,23 | €48,20 | €0,00 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | CYS | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,28356 | 1,28356 | 1,31375 | 0,64820 | 1,74564 | €204,95 | €409,90 | €0,00 | €0,00 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | SPCX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 150,46789 | €741,55 | €1.483,11 | €49,19 | €0,00 |
| Top 5 + BTC — target pieno 3R | CYS | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,28356 | 1,28356 | 1,31375 | 0,64820 | 1,74564 | €205,07 | €410,14 | €0,00 | €0,00 |
| Top 5 + BTC — target pieno 3R | SPCX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 150,46789 | €741,99 | €1.483,98 | €49,22 | €0,00 |
| Combo Trend | SPCX | LONG | Combo Trend | 60m | 2,0x | 136,85206 | 136,85206 | 131,80916 | 69,11029 | 147,94644 | €646,55 | €1.293,10 | €47,65 | €0,00 |
| Combo Trend | XRP | SHORT | Combo Trend | 60m | 2,0x | 1,01197 | 1,00040 | 1,00759 | 1,51289 | 0,97635 | €1.480,58 | €2.961,16 | €0,00 | €33,85 |
| Combo Trend | ZEC | SHORT | Combo Trend | 60m | 2,0x | 491,45169 | 471,00000 | 477,58085 | 734,72028 | 471,30966 | €34,52 | €69,05 | €0,00 | €2,87 |
| Combo Trend | ADA | SHORT | Combo Trend | 60m | 2,0x | 0,18533 | 0,18533 | 0,18829 | 0,27707 | 0,17881 | €56,81 | €113,62 | €1,82 | €-0,00 |
| Combo Trend | BTC | SHORT | Combo Trend | 60m | 2,0x | 63807,23600 | 63524,90000 | 64828,15178 | 95391,81782 | 61561,22129 | €1.485,14 | €2.970,29 | €47,52 | €13,14 |
| Combo Trend | SOL | SHORT | Combo Trend | 60m | 2,0x | 75,18996 | 74,76000 | 76,39300 | 112,40899 | 72,54327 | €1.387,30 | €2.774,60 | €44,39 | €15,87 |
| Combo Scanner | CYS | LONG | Combo Scanner | 60m | 2,0x | 1,28356 | 1,28356 | 1,31375 | 0,64820 | 1,62242 | €201,94 | €403,87 | €0,00 | €0,00 |
| Combo Scanner | SPCX | LONG | Combo Scanner | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 146,83700 | €730,65 | €1.461,31 | €48,46 | €0,00 |
| Combo Adaptive — madre | CYS | LONG | Combo Adaptive | 60m | 2,0x | 1,28356 | 1,28356 | 1,32547 | 0,64820 | 1,59161 | €210,67 | €421,33 | €0,00 | €0,00 |
| Combo Adaptive — madre | SPCX | LONG | Combo Adaptive | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 145,92928 | €762,24 | €1.524,48 | €50,56 | €0,00 |
| Combo Adaptive — madre | ADA | SHORT | Combo Adaptive | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17999 | €13,06 | €26,13 | €0,38 | €-0,00 |
| Combo Adaptive — madre | BTC | SHORT | Combo Adaptive | 60m | 2,0x | 63807,23600 | 63524,90000 | 64726,06020 | 95391,81782 | 61969,58760 | €1.768,38 | €3.536,76 | €50,93 | €15,65 |
| Combo Adaptive — madre | SOL | SHORT | Combo Adaptive | 60m | 2,0x | 75,18996 | 74,76000 | 76,27269 | 112,40899 | 73,02449 | €1.761,46 | €3.522,93 | €50,73 | €20,15 |
| Combo Adaptive — MFE Trail esistente | CYS | LONG | Combo Adaptive | 60m | 2,0x | 1,28356 | 1,28356 | 1,40742 | 0,64820 | 1,59161 | €194,41 | €388,82 | €0,00 | €0,00 |
| Combo Adaptive — MFE Trail esistente | SPCX | LONG | Combo Adaptive | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 145,92928 | €703,43 | €1.406,85 | €46,66 | €0,00 |
| Combo Adaptive — MFE Trail esistente | BTC | SHORT | Combo Adaptive | 60m | 2,0x | 63807,23600 | 63524,90000 | 64726,06020 | 95391,81782 | 61969,58760 | €1.608,91 | €3.217,82 | €46,34 | €14,24 |
| Combo Adaptive — MFE Trail esistente | SOL | SHORT | Combo Adaptive | 60m | 2,0x | 75,18996 | 74,76000 | 76,27269 | 112,40899 | 73,02449 | €1.568,55 | €3.137,11 | €45,17 | €17,94 |
| Combo Adaptive — Long Only | CYS | LONG | Combo Adaptive | 60m | 2,0x | 1,28356 | 1,28356 | 1,32547 | 0,64820 | 1,59161 | €206,91 | €413,83 | €0,00 | €0,00 |
| Combo Adaptive — Long Only | SPCX | LONG | Combo Adaptive | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 145,92928 | €748,66 | €1.497,32 | €49,66 | €0,00 |
| Combo Adaptive — parziale 1R | CYS | LONG | Combo Adaptive | 60m | 2,0x | 1,28356 | 1,28356 | 1,32547 | 0,64820 | 1,59161 | €202,29 | €404,58 | €0,00 | €0,00 |
| Combo Adaptive — parziale 1R | SPCX | LONG | Combo Adaptive | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 145,92928 | €731,94 | €1.463,87 | €48,55 | €0,00 |
| Combo Adaptive — parziale 1R | ADA | SHORT | Combo Adaptive | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17999 | €12,54 | €25,09 | €0,36 | €-0,00 |
| Combo Adaptive — parziale 1R | BTC | SHORT | Combo Adaptive | 60m | 2,0x | 63807,23600 | 63524,90000 | 64726,06020 | 95391,81782 | 61969,58760 | €1.698,08 | €3.396,15 | €48,90 | €15,03 |
| Combo Adaptive — parziale 1R | SOL | SHORT | Combo Adaptive | 60m | 2,0x | 75,18996 | 74,76000 | 76,27269 | 112,40899 | 73,02449 | €1.691,44 | €3.382,88 | €48,71 | €19,34 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | CYS | LONG | Combo Adaptive | 60m | 2,0x | 1,28356 | 1,28356 | 1,32547 | 0,64820 | 1,74564 | €209,83 | €419,66 | €0,00 | €0,00 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | SPCX | LONG | Combo Adaptive | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 150,46789 | €759,21 | €1.518,41 | €50,36 | €0,00 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | ZEC | SHORT | Combo Adaptive | 60m | 2,0x | 491,45169 | 471,00000 | 476,70340 | 734,72028 | 466,73193 | €76,64 | €153,27 | €0,00 | €6,38 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | BTC | SHORT | Combo Adaptive | 60m | 2,0x | 63807,23600 | 63524,90000 | 64726,06020 | 95391,81782 | 61050,76340 | €1.736,70 | €3.473,39 | €50,02 | €15,37 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | SOL | SHORT | Combo Adaptive | 60m | 2,0x | 75,18996 | 74,76000 | 76,27269 | 112,40899 | 71,94175 | €1.598,71 | €3.197,42 | €46,04 | €18,28 |
| Combo Adaptive — target pieno 3R | CYS | LONG | Combo Adaptive | 60m | 2,0x | 1,28356 | 1,28356 | 1,32547 | 0,64820 | 1,74564 | €205,91 | €411,82 | €0,00 | €0,00 |
| Combo Adaptive — target pieno 3R | SPCX | LONG | Combo Adaptive | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 150,46789 | €745,02 | €1.490,04 | €49,42 | €0,00 |
| Combo Adaptive — target pieno 3R | ZEC | SHORT | Combo Adaptive | 60m | 2,0x | 491,45169 | 471,00000 | 476,70340 | 734,72028 | 466,73193 | €75,20 | €150,41 | €0,00 | €6,26 |
| Combo Adaptive — target pieno 3R | BTC | SHORT | Combo Adaptive | 60m | 2,0x | 63807,23600 | 63524,90000 | 64726,06020 | 95391,81782 | 61050,76340 | €1.704,25 | €3.408,50 | €49,08 | €15,08 |
| Combo Adaptive — target pieno 3R | SOL | SHORT | Combo Adaptive | 60m | 2,0x | 75,18996 | 74,76000 | 76,27269 | 112,40899 | 71,94175 | €1.568,84 | €3.137,68 | €45,18 | €17,94 |
| Btc Ema 1H | BTC | SHORT | Trend following EMA | 60m | 3,0x | 64070,44335 | 63524,90000 | 64993,05773 | 85106,90558 | 62225,21458 | €1.141,05 | €3.423,15 | €49,29 | €29,15 |
| Btc Donchian 1H | BTC | SHORT | Donchian breakout 20 barre | 60m | 3,0x | 63807,23600 | 63524,90000 | 64623,96862 | 84757,27849 | 62173,77076 | €1.301,67 | €3.905,01 | €49,98 | €17,28 |
| Btc Adaptive 1H | BTC | SHORT | Combo Adaptive | 60m | 3,0x | 63807,23600 | 63524,90000 | 64726,06020 | 84757,27849 | 61969,58760 | €1.152,72 | €3.458,17 | €49,80 | €15,30 |
| Sol Ema 1H | SOL | SHORT | Trend following EMA | 60m | 3,0x | 75,18996 | 74,76000 | 76,27269 | 99,87733 | 73,02449 | €1.142,11 | €3.426,34 | €49,34 | €19,59 |
| Sol Donchian 1H | SOL | SHORT | Donchian breakout 20 barre | 60m | 3,0x | 75,18996 | 74,76000 | 76,15239 | 99,87733 | 73,26510 | €1.316,92 | €3.950,75 | €50,57 | €22,59 |
| Sol Adaptive 1H | SOL | SHORT | Combo Adaptive | 60m | 3,0x | 75,18996 | 74,76000 | 76,27269 | 99,87733 | 73,02449 | €1.132,08 | €3.396,25 | €48,91 | €19,42 |
| Eth Ema 1H | ETH | SHORT | Trend following EMA | 60m | 3,0x | 1873,61520 | 1858,21000 | 1900,59526 | 2488,78553 | 1819,65508 | €1.125,91 | €3.377,73 | €48,64 | €27,77 |
| Doge Bollinger 1H | DOGE | SHORT | Bollinger mean reversion | 60m | 3,0x | 0,07104 | 0,07005 | 0,07039 | 0,09436 | 0,06976 | €1.375,28 | €4.125,84 | €0,00 | €57,35 |
| Master Adaptive V1 | CYS | LONG | Master Adaptive Consensus | 60m | 2,0x | 1,32770 | 1,32770 | 1,16837 | 0,67049 | 1,64634 | €203,23 | €406,45 | €48,77 | €0,00 |
| Master Adaptive V1 | SPCX | LONG | Master Adaptive Consensus | 60m | 2,0x | 136,76201 | 136,76201 | 133,25764 | 69,06481 | 143,77074 | €951,69 | €1.903,38 | €48,77 | €0,00 |
| Master Adaptive No Alt V1 | CYS | LONG | Master Adaptive Consensus | 60m | 2,0x | 1,32770 | 1,32770 | 1,16837 | 0,67049 | 1,64634 | €203,31 | €406,62 | €48,79 | €0,00 |
| Master Adaptive No Alt V1 | SPCX | LONG | Master Adaptive Consensus | 60m | 2,0x | 136,76201 | 136,76201 | 133,25764 | 69,06481 | 143,77074 | €952,08 | €1.904,17 | €48,79 | €0,00 |
| Master Adaptive Strict3 V1 | CYS | LONG | Master Adaptive Consensus | 60m | 2,0x | 1,32770 | 1,32770 | 1,16837 | 0,67049 | 1,64634 | €195,94 | €391,88 | €47,03 | €0,00 |
| Master Adaptive Expanded V1 | CYS | LONG | Master Adaptive Consensus | 60m | 2,0x | 1,32770 | 1,32770 | 1,16837 | 0,67049 | 1,64634 | €204,15 | €408,29 | €49,00 | €0,00 |
| Master Adaptive Expanded V1 | SPCX | LONG | Master Adaptive Consensus | 60m | 2,0x | 136,76201 | 136,76201 | 133,25764 | 69,06481 | 143,77074 | €956,00 | €1.912,01 | €48,99 | €0,00 |
| Master Adaptive Expanded V1 | DOGE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,07067 | 0,07005 | 0,06965 | 0,03569 | 0,07271 | €1.710,84 | €3.421,69 | €49,27 | €-30,13 |
| Master Adaptive Gb20 V1 | CYS | LONG | Master Adaptive Consensus | 60m | 2,0x | 1,32770 | 1,32770 | 1,16837 | 0,67049 | 1,64634 | €200,53 | €401,05 | €48,13 | €0,00 |
| Master Adaptive Gb20 V1 | SPCX | LONG | Master Adaptive Consensus | 60m | 2,0x | 136,76201 | 136,76201 | 133,25764 | 69,06481 | 143,77074 | €939,05 | €1.878,09 | €48,12 | €0,00 |
| Master Adaptive Runner25 V1 | CYS | LONG | Master Adaptive Consensus | 60m | 2,0x | 1,32770 | 1,32770 | 1,16837 | 0,67049 | 1,80567 | €203,58 | €407,15 | €48,86 | €0,00 |
| Master Adaptive Runner25 V1 | SPCX | LONG | Master Adaptive Consensus | 60m | 2,0x | 136,76201 | 136,76201 | 133,25764 | 69,06481 | 147,27511 | €953,33 | €1.906,66 | €48,86 | €0,00 |
| Combo Adaptive — Side × Regime Guard | BTC | SHORT | Combo Adaptive | 60m | 2,0x | 63807,23600 | 63524,90000 | 64726,06020 | 95391,81782 | 61969,58760 | €1.842,32 | €3.684,64 | €53,06 | €16,30 |
| Combo Adaptive — Side × Regime Guard | SOL | SHORT | Combo Adaptive | 60m | 2,0x | 75,18996 | 74,76000 | 76,27269 | 112,40899 | 73,02449 | €1.841,81 | €3.683,62 | €53,04 | €21,06 |
| Combo Adaptive — Side × Regime Guard | ZEC | SHORT | Combo Adaptive | 60m | 2,0x | 474,59506 | 471,00000 | 482,99843 | 709,51962 | 457,78833 | €1.495,25 | €2.990,51 | €52,95 | €22,65 |
| Master Adaptive GB20 — Breakeven 0,5R | CYS | LONG | Master Adaptive Consensus | 60m | 2,0x | 1,32770 | 1,32770 | 1,16837 | 0,67049 | 1,64634 | €204,23 | €408,47 | €49,02 | €0,00 |
| Master Adaptive GB20 — Breakeven 0,5R | SPCX | LONG | Master Adaptive Consensus | 60m | 2,0x | 136,76201 | 136,76201 | 133,25764 | 69,06481 | 143,77074 | €956,40 | €1.912,81 | €49,01 | €0,00 |
| Master Adaptive GB20 — 50% a 0,75R | CYS | LONG | Master Adaptive Consensus | 60m | 2,0x | 1,32770 | 1,32770 | 1,16837 | 0,67049 | 1,64634 | €204,02 | €408,03 | €48,96 | €0,00 |
| Master Adaptive GB20 — 50% a 0,75R | SPCX | LONG | Master Adaptive Consensus | 60m | 2,0x | 136,76201 | 136,76201 | 133,25764 | 69,06481 | 143,77074 | €955,39 | €1.910,77 | €48,96 | €0,00 |
| Master Adaptive GB20 — Loss Cap 0,75R | CYS | LONG | Master Adaptive Consensus | 60m | 2,0x | 1,32770 | 1,32770 | 1,20521 | 0,67049 | 1,65434 | €262,28 | €524,56 | €48,40 | €0,00 |
| Rapida V3 NoHigh — Range Only | XRP | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,99862 | 1,00040 | 1,00980 | 1,32650 | 0,98184 | €1.566,59 | €4.699,76 | €52,64 | €-8,38 |
| Rapida V3 NoHigh — Range Only | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 63807,23600 | 63524,90000 | 64521,87704 | 84757,27849 | 62735,27444 | €1.566,03 | €4.698,09 | €52,62 | €20,79 |
| Rapida V3 NoHigh — Range Only | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 475,00498 | 471,00000 | 481,54658 | 630,96495 | 465,19258 | €1.273,14 | €3.819,43 | €52,60 | €32,20 |
| Rapida V3 NoHigh — Regime Guard | XRP | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,99862 | 1,00040 | 1,00980 | 1,32650 | 0,98184 | €1.582,44 | €4.747,32 | €53,17 | €-8,46 |
| Rapida V3 NoHigh — Regime Guard | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 63807,23600 | 63524,90000 | 64521,87704 | 84757,27849 | 62735,27444 | €1.581,87 | €4.745,62 | €53,15 | €21,00 |
| Rapida V3 NoHigh — Regime Guard | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 475,00498 | 471,00000 | 481,54658 | 630,96495 | 465,19258 | €1.286,02 | €3.858,07 | €53,13 | €32,53 |
| MAIN — Side × Regime Guard | XRP | SHORT | Confluenza trend | 240m | 3,0x | 1,01047 | 1,00040 | 1,03352 | 1,34224 | 0,96437 | €747,08 | €2.241,25 | €51,13 | €22,33 |
| Combo Trend — Side × Regime Guard | XRP | SHORT | Combo Trend | 60m | 2,0x | 1,01197 | 1,00040 | 1,00759 | 1,51289 | 0,97635 | €1.565,11 | €3.130,22 | €0,00 | €35,78 |
| Combo Trend — Side × Regime Guard | ZEC | SHORT | Combo Trend | 60m | 2,0x | 491,45169 | 471,00000 | 477,58085 | 734,72028 | 471,30966 | €1.345,98 | €2.691,96 | €0,00 | €112,03 |
| FAST NoHigh <7,5 · SHORT only | CYS | LONG | Momentum / breakout | 60m | 3,0x | 1,32770 | 1,32770 | 1,35661 | 0,89177 | 1,51824 | €178,22 | €534,66 | €0,00 | €0,00 |
| FAST NoHigh <7,5 · SHORT only | BTC | SHORT | Momentum / breakout | 60m | 3,0x | 63807,23600 | 63524,90000 | 64521,87704 | 84757,27849 | 62735,27444 | €1.546,22 | €4.638,65 | €51,95 | €20,53 |
| FAST NoHigh <7,5 · SHORT only | ZEC | SHORT | Momentum / breakout | 60m | 3,0x | 475,00498 | 471,00000 | 481,54658 | 630,96495 | 465,19258 | €1.257,03 | €3.771,10 | €51,93 | €31,80 |
| FAST NoHigh <7,5 · SHORT only | SOL | SHORT | Momentum / breakout | 60m | 3,0x | 75,18996 | 74,76000 | 76,03209 | 99,87733 | 73,92677 | €1.545,21 | €4.635,64 | €51,92 | €26,51 |
| Bilanciata V3 · LONG only | SPCX | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 136,85206 | 136,85206 | 132,31345 | 91,91897 | 145,92928 | €496,25 | €1.488,74 | €49,37 | €0,00 |
| Bilanciata V3 · LONG only | CYS | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1,33140 | 1,33140 | 1,17163 | 0,89426 | 1,65093 | €134,76 | €404,29 | €48,51 | €0,00 |
| Bilanciata V3 · LONG only | ZEC | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 486,56267 | 471,00000 | 476,70736 | 646,31741 | 471,40169 | €15,31 | €45,94 | €0,00 | €1,47 |
| Bilanciata V3 · LONG only | ADA | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,18533 | 0,18533 | 0,18800 | 0,24618 | 0,17999 | €1.142,52 | €3.427,55 | €49,36 | €-0,00 |
| Bilanciata V3 · LONG only | BTC | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 63807,23600 | 63524,90000 | 64726,06020 | 84757,27849 | 61969,58760 | €1.068,36 | €3.205,08 | €46,15 | €14,18 |
| Scanner Bottom5 Short Profit Lock V1 | BTC | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 64070,44335 | 63524,90000 | 64993,05773 | 95785,31281 | 62225,21458 | €1.730,40 | €3.460,80 | €49,84 | €29,47 |
| Scanner Bottom5 Short Profit Lock V1 | ADA | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17999 | €1.748,97 | €3.497,95 | €50,37 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | ZEC | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 474,59506 | 471,00000 | 482,99843 | 709,51962 | 457,78833 | €1.426,91 | €2.853,82 | €50,53 | €21,62 |
| Scanner Bottom5 Short Mfe Trail V1 | BTC | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 64070,44335 | 63524,90000 | 64993,05773 | 95785,31281 | 62225,21458 | €1.733,03 | €3.466,07 | €49,91 | €29,51 |
| Scanner Bottom5 Short Mfe Trail V1 | ADA | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17999 | €1.751,64 | €3.503,27 | €50,45 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | ZEC | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 474,59506 | 471,00000 | 482,99843 | 709,51962 | 457,78833 | €1.429,08 | €2.858,16 | €50,61 | €21,65 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Scanner Bottom5 Short Mfe Trail V1 | XRP | SHORT | 2026-08-11T15:39:43+00:00 | 1,00599 | €2,64 | 0,05 | STOP |
| Scanner Bottom5 Short Profit Lock V1 | XRP | SHORT | 2026-08-11T15:39:43+00:00 | 1,00599 | €2,64 | 0,05 | STOP |
| Bilanciata V3 · LONG only | XRP | SHORT | 2026-08-11T15:39:43+00:00 | 1,00599 | €0,10 | 0,06 | STOP |
| Combo Adaptive — Side × Regime Guard | XRP | SHORT | 2026-08-11T15:39:43+00:00 | 1,00662 | €15,31 | 0,30 | STOP |
| Combo Adaptive — target pieno 3R | XRP | SHORT | 2026-08-11T15:39:43+00:00 | 1,00557 | €-0,06 | -0,09 | STOP |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | XRP | SHORT | 2026-08-11T15:39:43+00:00 | 1,00557 | €-0,06 | -0,09 | STOP |
| Combo Adaptive — parziale 1R | XRP | SHORT | 2026-08-11T15:39:43+00:00 | 1,00557 | €-0,04 | -0,09 | STOP |
| Combo Adaptive — MFE Trail esistente | XRP | SHORT | 2026-08-11T15:39:43+00:00 | 1,00195 | €0,07 | 0,16 | STOP |
| Combo Adaptive — madre | XRP | SHORT | 2026-08-11T15:39:43+00:00 | 1,00557 | €-0,05 | -0,09 | STOP |
| Combo Mean Reversion | DOGE | SHORT | 2026-08-11T15:39:43+00:00 | 0,07060 | €19,53 | 0,42 | STOP |
| Scanner Bottom20 Short | XRP | SHORT | 2026-08-11T15:39:43+00:00 | 1,00599 | €2,70 | 0,05 | STOP |
| Scanner Bottom15 Short | XRP | SHORT | 2026-08-11T15:39:43+00:00 | 1,00599 | €2,70 | 0,05 | STOP |

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
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 280/30 | 33/30 | 0,72 | 2,04 | -0,15R | €9,09 | 2,01% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 251/30 | 20/30 | 0,60 | 1,90 | -0,21R | €11,76 | 2,73% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 162/30 | 22/30 | 0,78 | 1,74 | -0,12R | €12,35 | 1,72% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 164/30 | 22/30 | 0,79 | 1,57 | -0,11R | €8,43 | 2,27% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 222/30 | 31/30 | 0,79 | 0,62 | -0,11R | €-8,91 | 4,83% | COERENTE − | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 195/30 | 11/30 | 0,72 | 0,00 | -0,14R | €-38,20 | 4,20% | COERENTE − | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 96/30 | 8/30 | 0,64 | 1,02 | -0,19R | €0,42 | 2,15% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 196/30 | 17/30 | 0,56 | 4,50 | -0,27R | €14,07 | 1,01% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 297/30 | 24/30 | 0,72 | 0,64 | -0,15R | €-7,61 | 3,23% | COERENTE − | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 266/30 | 7/30 | 0,59 | 0,02 | -0,22R | €-33,97 | 2,82% | COERENTE − | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 222/30 | 30/30 | 0,84 | 1,02 | -0,08R | €0,30 | 4,84% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 393/30 | 55/30 | 0,83 | 1,12 | -0,08R | €1,80 | 3,59% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 103/30 | 15/30 | 0,46 | 0,99 | -0,37R | €-0,32 | 2,70% | COERENTE − | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 348/30 | 44/30 | 0,72 | 1,20 | -0,15R | €3,30 | 2,91% | DIVERGENTE | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 352/30 | 37/30 | 0,72 | 0,76 | -0,15R | €-4,40 | 3,08% | COERENTE − | BOCCIATA RESEARCH |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 317/30 | 23/30 | 0,61 | 1,12 | -0,21R | €2,12 | 3,05% | DIVERGENTE | BOCCIATA RESEARCH |
| MAIN | Principale 4H | 203/30 | 36/30 | 0,69 | 0,90 | -0,19R | €-3,08 | 6,36% | COERENTE − | BOCCIATA RESEARCH |
| MAIN_DYNAMIC_ASSET_SELECTOR_V1 | MAIN — Dynamic Asset Selector | 0/30 | 11/30 | 0,00 | 1,85 | 0,00R | €20,94 | 1,50% | n/a | RACCOLTA RESEARCH |
| MAIN_SIDE_REGIME_GUARD_V1 | MAIN — Side × Regime Guard | 0/30 | 18/30 | 0,00 | 1,84 | 0,00R | €17,63 | 2,40% | n/a | RACCOLTA RESEARCH |
| RSI_EXTREME_LONG_15M | Scalp RSI Long 25 · prudente · 5x (riferimento tra 9 varianti) | 22/30 | 13/30 | 0,47 | 0,37 | -0,33R | €-3,60 | 0,71% | COERENTE − | RACCOLTA RESEARCH |
| RSI_EXTREME_SHORT_15M | Scalp RSI Short 75 · prudente · 5x (riferimento tra 9 varianti) | 36/30 | 23/30 | 0,44 | 0,39 | -0,33R | €-3,41 | 0,84% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_BALANCED | Bilanciata 1H V1 | 505/30 | 80/30 | 0,94 | 1,21 | -0,04R | €3,58 | 3,56% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_BALANCED_LONG_NO_RHV_V1 | Bilanciata 1H — LONG senza Range High Vol | 0/30 | 23/30 | 0,00 | 0,37 | 0,00R | €-22,91 | 6,39% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_BALANCED_SHORT_TREND_DOWN_STRICT_V1 | Bilanciata 1H — SHORT Trend Down stretto | 0/30 | 2/30 | 0,00 | 0,00 | 0,00R | €-28,31 | 1,11% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_BALANCED_V2 | Bilanciata 1H V2 | 176/30 | 43/30 | 1,13 | 1,21 | 0,07R | €4,07 | 2,75% | COERENTE + | PRONTA PER REVISIONE LIVE |
| SHADOW_1H_BALANCED_V3 | Bilanciata 1H V3 Filtered | 314/30 | 71/30 | 0,93 | 1,23 | -0,04R | €4,96 | 3,20% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | Bilanciata V3 · LONG only | 235/30 | 27/30 | 0,80 | 0,67 | -0,12R | €-7,73 | 2,91% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST | Rapida 1H V1 — madre | 208/30 | 78/30 | 0,92 | 1,02 | -0,05R | €0,55 | 6,76% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | Rapida V1 — Long + BTC 1–3 + score <7,5 | 167/30 | 25/30 | 0,97 | 0,99 | -0,01R | €-0,14 | 2,27% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | FAST NoHigh <7,5 · SHORT only | 312/30 | 35/30 | 0,83 | 1,82 | -0,08R | €11,17 | 1,76% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | Rapida V1 — no HIGH + score <7,5 | 379/30 | 71/30 | 0,88 | 1,49 | -0,06R | €9,24 | 2,83% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_NO_PEPE_V1 | Rapida V1 — senza PEPE | 505/30 | 77/30 | 0,80 | 1,14 | -0,11R | €2,68 | 2,79% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_COST_AWARE_V1 | Rapida score 6–7,5 — Cost Aware | 0/30 | 41/30 | 0,00 | 2,16 | 0,00R | €16,98 | 1,96% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_NO_TREND_UP_V1 | Rapida score 6–7,5 — senza Trend Up | 0/30 | 39/30 | 0,00 | 1,39 | 0,00R | €7,85 | 3,20% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_RANGE_ONLY_V1 | Rapida score 6–7,5 — Range Only | 0/30 | 17/30 | 0,00 | 1,96 | 0,00R | €21,34 | 2,28% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_SCORE_6_75_V1 | Rapida V1 — score 6–7,5 | 303/30 | 81/30 | 0,87 | 1,40 | -0,07R | €7,26 | 2,49% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_TP2_V1 | Rapida V1 — target pieno 2R | 471/30 | 85/30 | 0,77 | 0,98 | -0,12R | €-0,35 | 2,94% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V2 | Rapida 1H V2 | 37/30 | 16/30 | 0,51 | 0,81 | -0,30R | €-4,64 | 2,38% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3 | Rapida 1H V3 Filtered — madre | 501/30 | 106/30 | 0,84 | 0,96 | -0,09R | €-0,82 | 4,29% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_CAP75_V1 | Rapida V3 — score <7,5 | 362/30 | 71/30 | 0,82 | 1,06 | -0,09R | €1,26 | 4,96% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | Rapida V3 — qualità completa + profit lock | 203/30 | 50/30 | 0,95 | 0,87 | -0,03R | €-3,16 | 3,21% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | Rapida V3 — Long + no HIGH + score <7,5 | 206/30 | 45/30 | 0,94 | 0,80 | -0,03R | €-4,97 | 3,40% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | Rapida V3 — Long Only | 280/30 | 58/30 | 0,88 | 0,57 | -0,06R | €-11,70 | 7,87% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V1 | Rapida V3 NoHigh — Range Only | 0/30 | 15/30 | 0,00 | 4,21 | 0,00R | €35,16 | 1,78% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_V1 | Rapida V3 NoHigh — Regime Guard | 0/30 | 23/30 | 0,00 | 4,83 | 0,00R | €27,56 | 1,39% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | Rapida V3 — no volatilità HIGH | 399/30 | 66/30 | 0,81 | 1,01 | -0,10R | €0,15 | 2,96% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONLY_V1 | Rapida V3 senza ESPORTS — Long Only | 0/30 | 38/30 | 0,00 | 0,77 | 0,00R | €-5,53 | 5,84% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_V1 | Rapida V3 senza ESPORTS — MFE Lock | 0/30 | 62/30 | 0,00 | 0,98 | 0,00R | €-0,36 | 4,32% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_GUARD_V1 | Rapida V3 senza ESPORTS — Stress Guard | 0/30 | 20/30 | 0,00 | 1,17 | 0,00R | €3,80 | 2,17% | n/a | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | Rapida V3 — senza ESPORTS | 454/30 | 80/30 | 0,79 | 0,83 | -0,11R | €-3,61 | 4,26% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_4H_WIDE | Ampia 4H | 182/30 | 29/30 | 0,71 | 1,00 | -0,20R | €-0,03 | 4,21% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_BOLLINGER_MR_1H | Benchmark Bollinger mean reversion 1H | 155/30 | 53/30 | 1,09 | 0,77 | 0,04R | €-6,15 | 5,90% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_BTC_ADAPTIVE_1H | Btc Adaptive 1H | 9/30 | 4/30 | 0,59 | 0,63 | -0,20R | €-10,11 | 0,89% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_ADAPTIVE_4H | Btc Adaptive 4H | 1/30 | 1/30 | 0,00 | 0,00 | -1,07R | €-50,38 | 0,74% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_BOLLINGER_1H | Btc Bollinger 1H | 7/30 | 4/30 | 5,58 | 2,94 | 0,74R | €27,74 | 0,70% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_BTC_BOLLINGER_4H | Btc Bollinger 4H | 1/30 | 1/30 | ∞ | ∞ | 1,72R | €84,12 | 0,30% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_BTC_DONCHIAN_1H | Btc Donchian 1H | 12/30 | 5/30 | 0,16 | 0,97 | -0,71R | €-0,63 | 1,49% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_DONCHIAN_4H | Btc Donchian 4H | 3/30 | 2/30 | 0,00 | 0,00 | -1,07R | €-50,87 | 1,48% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_EMA_1H | Btc Ema 1H | 12/30 | 7/30 | 0,69 | 0,48 | -0,20R | €-20,19 | 1,72% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_EMA_4H | Btc Ema 4H | 2/30 | 1/30 | 0,00 | 0,00 | -1,07R | €-49,32 | 0,96% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE | Combo Adaptive — madre | 415/30 | 46/30 | 1,00 | 1,28 | -0,00R | €4,05 | 3,05% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | Combo Adaptive — Long Only | 226/30 | 22/30 | 0,92 | 0,60 | -0,04R | €-8,91 | 2,82% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | Combo Adaptive — MFE Trail esistente | 428/30 | 59/30 | 1,00 | 0,45 | 0,00R | €-12,41 | 7,57% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | Combo Adaptive — parziale 1R | 356/30 | 47/30 | 0,94 | 0,74 | -0,03R | €-4,66 | 3,97% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | Combo Adaptive — Quality7 + Regime + parziale 1R | 43/30 | 11/30 | 1,55 | 0,71 | 0,22R | €-7,09 | 1,95% | DIVERGENTE | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | Combo Adaptive — Quality7 + Regime | 43/30 | 11/30 | 1,43 | 0,31 | 0,17R | €-18,43 | 2,32% | DIVERGENTE | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | Combo Adaptive — Quality7 | 116/30 | 29/30 | 0,95 | 1,02 | -0,02R | €0,35 | 2,73% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | Combo Adaptive — Trend/Transition | 157/30 | 22/30 | 0,83 | 0,79 | -0,09R | €-4,40 | 2,18% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | Combo Adaptive — 75% a 2R + runner 25% a 3R | 47/30 | 51/30 | 0,74 | 1,00 | -0,20R | €-0,03 | 2,62% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_SIDE_REGIME_GUARD_V1 | Combo Adaptive — Side × Regime Guard | 0/30 | 41/30 | 0,00 | 2,22 | 0,00R | €14,20 | 1,58% | n/a | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | Combo Adaptive — target pieno 3R | 47/30 | 32/30 | 0,74 | 0,70 | -0,20R | €-5,88 | 2,62% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_MEAN_REVERSION | Combo Mean Reversion | 75/30 | 22/30 | 1,23 | 0,73 | 0,10R | €-9,18 | 4,18% | DIVERGENTE | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_COMBO_SCANNER | Combo Scanner | 259/30 | 53/30 | 1,11 | 0,68 | 0,06R | €-9,13 | 6,89% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_COMBO_TREND | Combo Trend | 337/30 | 70/30 | 0,91 | 0,74 | -0,06R | €-7,63 | 7,64% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_COMBO_TREND_SIDE_REGIME_GUARD_V1 | Combo Trend — Side × Regime Guard | 0/30 | 34/30 | 0,00 | 0,94 | 0,00R | €-1,10 | 2,89% | n/a | RACCOLTA RESEARCH |
| SHADOW_DOGE_BOLLINGER_1H | Doge Bollinger 1H | 7/30 | 4/30 | 1,03 | 0,41 | 0,02R | €-24,49 | 1,89% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_DOGE_DONCHIAN_1H | Doge Donchian 1H | 9/30 | 7/30 | 0,61 | 0,89 | -0,29R | €-2,67 | 1,27% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_DOGE_EMA_1H | Doge Ema 1H | 16/30 | 11/30 | 0,43 | 1,18 | -0,40R | €3,61 | 1,44% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_DONCHIAN_1H | Benchmark Donchian breakout 1H | 169/30 | 43/30 | 0,79 | 1,59 | -0,14R | €13,84 | 3,09% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | Donchian 1H Gb20 120R V1 | 99/30 | 11/30 | 0,71 | 3,21 | -0,18R | €31,43 | 1,61% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_EMA_TREND_1H | Benchmark trend following EMA 1H | 343/30 | 48/30 | 0,88 | 0,71 | -0,07R | €-6,36 | 4,10% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_ETH_ADAPTIVE_1H | Eth Adaptive 1H | 12/30 | 6/30 | 0,37 | 0,08 | -0,46R | €-33,40 | 2,09% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_BOLLINGER_1H | Eth Bollinger 1H | 6/30 | 2/30 | 1,46 | 0,28 | 0,17R | €-20,26 | 0,91% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_ETH_DONCHIAN_1H | Eth Donchian 1H | 11/30 | 5/30 | 0,35 | 0,42 | -0,54R | €-25,60 | 1,62% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_EMA_1H | Eth Ema 1H | 17/30 | 8/30 | 0,37 | 0,16 | -0,45R | €-34,02 | 3,12% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_EMA_4H | Eth Ema 4H | 2/30 | 2/30 | 0,00 | 0,00 | -1,06R | €-52,87 | 1,21% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_GLOBAL_PURE | Global Confluence puro 1H | 10/30 | 14/30 | 1,24 | 0,39 | 0,13R | €-19,26 | 2,92% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | Master Adaptive Expanded V1 | 203/30 | 23/30 | 1,00 | 0,69 | 0,00R | €-11,07 | 3,64% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_BE_V1 | Master Adaptive GB20 — Breakeven 0,5R | 0/30 | 24/30 | 0,00 | 0,55 | 0,00R | €-13,47 | 4,69% | n/a | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_LOSS_CAP_V1 | Master Adaptive GB20 — Loss Cap 0,75R | 0/30 | 23/30 | 0,00 | 0,41 | 0,00R | €-24,44 | 7,16% | n/a | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_PARTIAL_V1 | Master Adaptive GB20 — 50% a 0,75R | 0/30 | 19/30 | 0,00 | 0,50 | 0,00R | €-17,55 | 4,27% | n/a | RACCOLTA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | Master Adaptive Gb20 V1 | 377/30 | 56/30 | 1,39 | 0,52 | 0,13R | €-8,91 | 5,35% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | Master Adaptive No Alt V1 | 178/30 | 21/30 | 1,01 | 0,57 | 0,01R | €-17,47 | 4,03% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | Master Adaptive Runner25 V1 | 185/30 | 23/30 | 0,98 | 0,58 | -0,01R | €-15,40 | 3,98% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | Master Adaptive Strict3 V1 | 131/30 | 30/30 | 0,94 | 0,43 | -0,04R | €-25,86 | 8,03% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_MASTER_ADAPTIVE_V1 | Master Adaptive V1 | 198/30 | 21/30 | 0,96 | 0,56 | -0,02R | €-17,66 | 4,07% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_RELATIVE_STRENGTH | Forza relativa 1H V1 | 425/30 | 59/30 | 0,87 | 0,74 | -0,08R | €-6,36 | 7,55% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_RELATIVE_STRENGTH_V2 | Forza relativa 1H V2 | 172/30 | 57/30 | 1,17 | 0,88 | 0,09R | €-4,04 | 6,44% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_SCANNER_BOTTOM10_SHORT | Scanner Bottom10 Short | 128/30 | 33/30 | 0,57 | 1,29 | -0,24R | €5,05 | 2,72% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_SCANNER_BOTTOM15_SHORT | Scanner Bottom15 Short | 128/30 | 33/30 | 0,57 | 1,29 | -0,24R | €5,05 | 2,72% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_SCANNER_BOTTOM20_SHORT | Scanner Bottom20 Short | 128/30 | 33/30 | 0,57 | 1,29 | -0,24R | €5,05 | 2,72% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT | Scanner Bottom 5 Short 1H | 163/30 | 54/30 | 0,81 | 1,00 | -0,10R | €0,05 | 5,48% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT_CONTINUATION_V1 | Scanner Bottom5 Short Continuation V1 | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | Scanner Bottom5 Short Mfe Trail V1 | 147/30 | 26/30 | 0,77 | 1,24 | -0,11R | €3,69 | 1,38% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | Scanner Bottom5 Short Profit Lock V1 | 126/30 | 27/30 | 0,72 | 1,24 | -0,13R | €2,98 | 1,53% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP10_LONG | Scanner Top10 Long | 195/30 | 24/30 | 0,98 | 0,29 | -0,01R | €-24,35 | 7,60% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP15_LONG | Scanner Top15 Long | 196/30 | 24/30 | 0,97 | 0,29 | -0,02R | €-24,35 | 7,60% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP20_LONG | Scanner Top20 Long | 196/30 | 24/30 | 0,97 | 0,29 | -0,02R | €-24,35 | 7,60% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC | Scanner Top 5 + forza BTC 1H | 250/30 | 43/30 | 1,12 | 1,09 | 0,06R | €2,16 | 5,26% | COERENTE + | BOCCIATA PAPER |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | Top 5 + BTC — BTC 2–3 | 124/30 | 10/30 | 0,87 | 0,87 | -0,07R | €-3,13 | 2,84% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | Top 5 + BTC — BTC≤3 | 204/30 | 24/30 | 0,93 | 0,54 | -0,04R | €-14,81 | 5,74% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | Top 5 + BTC — Guard + BTC≤3 + MFE | 211/30 | 36/30 | 1,16 | 0,54 | 0,07R | €-13,46 | 4,93% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | Top 5 + BTC — Guard + BTC≤3 | 178/30 | 21/30 | 1,04 | 0,58 | 0,02R | €-15,17 | 5,67% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | Top 5 + BTC — Guard + MFE | 221/30 | 43/30 | 1,16 | 0,48 | 0,07R | €-15,31 | 6,73% | DIVERGENTE | BOCCIATA PAPER |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | Top 5 + BTC — Guard | 185/30 | 26/30 | 1,05 | 0,51 | 0,03R | €-16,77 | 5,26% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | Top 5 + BTC — solo MFE | 254/30 | 36/30 | 1,05 | 0,39 | 0,02R | €-14,99 | 6,33% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | Top 5 + BTC — 75% a 2,2R + runner 3R | 200/30 | 32/30 | 0,96 | 0,68 | -0,02R | €-9,03 | 6,29% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | Top 5 + BTC — target pieno 3R | 190/30 | 28/30 | 0,97 | 0,68 | -0,02R | €-10,12 | 5,99% | COERENTE − | BOCCIATA RESEARCH |
| SHADOW_SCANNER_TOP5_LONG | Scanner Top 5 Long 1H | 274/30 | 52/30 | 1,11 | 1,17 | 0,06R | €4,27 | 6,09% | COERENTE + | PRONTA PER REVISIONE LIVE |
| SHADOW_SOL_ADAPTIVE_1H | Sol Adaptive 1H | 18/30 | 7/30 | 0,44 | 0,24 | -0,45R | €-31,26 | 2,95% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_ADAPTIVE_4H | Sol Adaptive 4H | 2/30 | 2/30 | 1,18 | 0,65 | 0,10R | €-8,96 | 0,77% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SOL_BOLLINGER_1H | Sol Bollinger 1H | 11/30 | 5/30 | 0,61 | 0,82 | -0,24R | €-5,94 | 1,89% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_BOLLINGER_4H | Sol Bollinger 4H | 2/30 | 1/30 | ∞ | ∞ | 1,20R | €86,98 | 0,40% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_SOL_DONCHIAN_1H | Sol Donchian 1H | 11/30 | 4/30 | 0,77 | 26,39 | -0,16R | €28,48 | 0,79% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SOL_DONCHIAN_4H | Sol Donchian 4H | 2/30 | 2/30 | 1,29 | 0,71 | 0,15R | €-7,50 | 0,79% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SOL_EMA_1H | Sol Ema 1H | 17/30 | 7/30 | 0,59 | 0,52 | -0,32R | €-18,88 | 2,16% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_EMA_4H | Sol Ema 4H | 3/30 | 3/30 | 0,00 | 0,00 | -1,05R | €-51,41 | 1,57% | COERENTE − | RACCOLTA RESEARCH |

Per le famiglie RSI con più configurazioni di leva o margine, il lato paper usa il conto con il maggior numero di eventi indipendenti; i conti duplicati non vengono aggregati.
`PRONTA PER REVISIONE LIVE` non invia ordini e non sposta capitale: abilita soltanto una revisione manuale finale.

## 🎯 DOGE Rejection Short — conto dedicato €3.600

Simulazione separata **paper only**: capitale/margine iniziale **€3.600**, leva **5x**, esposizione iniziale **€18.000**. Non modifica i conti paper da €10.000 e non invia ordini reali.

- Stato: **WAITING**
- Prezzo DOGE: **0.07005**
- Pre-allarme: **0.0765**; zona armata: **0.0775**; trigger rejection: **0.078**
- Invalidazione prima dell’entrata: chiusura 15m sopra **0.07966**

| Capitale iniziale | Balance | Equity | P&L aperto | Eventi chiusi | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- |
| €3.600,00 | €3.600,00 | €3.600,00 | €0,00 | 0 | 0,00% | 0,00 | 0,00% |

### Filtri correnti

| Filtro | Valore | Stato |
| --- | --- | --- |
| Dati mercato | FRESH | OK |
| Candela 15m | 28.9 min | OK |
| Global DOGE | -6.0 | OK |
| Classic raw | -11.0 | OK |
| DOGE/BTC raw | -6.0 | OK |
| Pattern ribassista | MATURO | OK |
| BTC sotto filtro | 63524.9 | OK |

### Ultima candela 15m valutata

- Rejection accettata: **NO**; motivo: **trigger_touched, entry_not_chased, upper_wick, bearish_confirmation**
- High **0.07057**; close **0.07057**; wick alta **0.0%**; volume **x1.02**

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
- Motivo: Direzione poco definita: score BTC +0.0, breadth EMA50 8%, ADX 24.1.
- BTC trend score: **0,00**; ADX: **24,05**; breadth sopra EMA50: **8,33%**
- Mediana alt vs BTC: **-0,07%**; dispersione: **20,35%**

- Aperti in questo ciclo: **1**
- Chiusi in questo ciclo: **23**
- Posizioni research aperte: **399**
- Trade research chiusi: **19453**
- Eventi di mercato indipendenti chiusi: **2817**
- Segnali sovrapposti saltati sullo stesso asset/profilo: **52376**
- Posizioni Research V1 senza regime scartate durante la migrazione: **28**

### Risultati complessivi per strategia

| Profilo | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | 4 | 280 | 280 | 30,36% | 0,72 | -0,15R | €-411,84 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | 4 | 251 | 251 | 29,08% | 0,60 | -0,21R | €-539,08 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | 2 | 162 | 162 | 45,68% | 0,78 | -0,12R | €-187,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | 2 | 164 | 164 | 32,93% | 0,79 | -0,11R | €-176,89 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | 2 | 222 | 222 | 31,98% | 0,79 | -0,11R | €-240,30 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | 2 | 195 | 195 | 32,31% | 0,72 | -0,14R | €-269,51 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | 2 | 96 | 96 | 32,29% | 0,64 | -0,19R | €-184,60 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | 2 | 196 | 196 | 26,53% | 0,56 | -0,27R | €-524,98 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | 4 | 297 | 297 | 29,97% | 0,72 | -0,15R | €-448,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | 4 | 266 | 266 | 28,57% | 0,59 | -0,22R | €-581,16 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | 2 | 222 | 222 | 32,88% | 0,84 | -0,08R | €-180,63 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | 4 | 393 | 393 | 40,71% | 0,83 | -0,08R | €-320,79 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | 1 | 103 | 103 | 26,21% | 0,46 | -0,37R | €-382,60 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | 4 | 348 | 348 | 29,60% | 0,72 | -0,15R | €-515,01 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | 4 | 352 | 352 | 29,55% | 0,72 | -0,15R | €-515,55 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | 4 | 317 | 317 | 28,08% | 0,61 | -0,21R | €-652,59 |
| MAIN | 13 | 203 | 203 | 25,12% | 0,69 | -0,19R | €-392,74 |
| RSI_EXTREME_LONG_15M | 1 | 22 | 22 | 36,36% | 0,47 | -0,33R | €-73,68 |
| RSI_EXTREME_SHORT_15M | 0 | 36 | 36 | 33,33% | 0,44 | -0,33R | €-119,37 |
| Bilanciata 1H V1 | 15 | 505 | 505 | 34,46% | 0,94 | -0,04R | €-177,75 |
| Bilanciata 1H V2 | 5 | 200 | 176 | 38,50% | 1,13 | 0,07R | €141,37 |
| Bilanciata 1H V3 Filtered | 9 | 314 | 314 | 34,39% | 0,93 | -0,04R | €-125,76 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | 9 | 235 | 235 | 32,77% | 0,80 | -0,12R | €-271,11 |
| Rapida 1H V1 | 0 | 208 | 208 | 38,94% | 0,92 | -0,05R | €-101,45 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | 1 | 167 | 167 | 37,72% | 0,97 | -0,01R | €-23,09 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | 6 | 312 | 312 | 34,94% | 0,83 | -0,08R | €-261,86 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | 6 | 379 | 379 | 36,41% | 0,88 | -0,06R | €-227,53 |
| SHADOW_1H_FAST_NO_PEPE_V1 | 6 | 505 | 505 | 34,46% | 0,80 | -0,11R | €-547,30 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | 5 | 303 | 303 | 35,97% | 0,87 | -0,07R | €-213,17 |
| SHADOW_1H_FAST_TP2_V1 | 5 | 471 | 471 | 31,21% | 0,77 | -0,12R | €-587,06 |
| Rapida 1H V2 | 1 | 44 | 37 | 31,82% | 0,51 | -0,30R | €-133,93 |
| Rapida 1H V3 Filtered | 5 | 501 | 501 | 35,33% | 0,84 | -0,09R | €-430,19 |
| SHADOW_1H_FAST_V3_CAP75_V1 | 5 | 362 | 362 | 35,08% | 0,82 | -0,09R | €-336,06 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | 2 | 203 | 203 | 47,78% | 0,95 | -0,03R | €-50,81 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | 2 | 206 | 206 | 37,38% | 0,94 | -0,03R | €-64,83 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | 2 | 280 | 280 | 36,43% | 0,88 | -0,06R | €-170,39 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | 5 | 399 | 399 | 34,59% | 0,81 | -0,10R | €-402,92 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | 5 | 454 | 454 | 34,14% | 0,79 | -0,11R | €-512,14 |
| SHADOW_4H_WIDE | 29 | 182 | 182 | 20,88% | 0,71 | -0,20R | €-371,88 |
| SHADOW_BOLLINGER_MR_1H | 2 | 155 | 155 | 47,10% | 1,09 | 0,04R | €61,77 |
| SHADOW_BTC_ADAPTIVE_1H | 1 | 9 | 9 | 55,56% | 0,59 | -0,20R | €-18,05 |
| SHADOW_BTC_ADAPTIVE_4H | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,67 |
| SHADOW_BTC_BOLLINGER_1H | 1 | 7 | 7 | 85,71% | 5,58 | 0,74R | €51,91 |
| SHADOW_BTC_BOLLINGER_4H | 0 | 1 | 1 | 100,00% | ∞ | 1,72R | €17,16 |
| SHADOW_BTC_DONCHIAN_1H | 1 | 12 | 12 | 25,00% | 0,16 | -0,71R | €-84,97 |
| SHADOW_BTC_DONCHIAN_4H | 1 | 3 | 3 | 0,00% | 0,00 | -1,07R | €-32,12 |
| SHADOW_BTC_EMA_1H | 1 | 12 | 12 | 41,67% | 0,69 | -0,20R | €-24,31 |
| SHADOW_BTC_EMA_4H | 0 | 2 | 2 | 0,00% | 0,00 | -1,07R | €-21,35 |
| SHADOW_COMBO_ADAPTIVE | 9 | 415 | 415 | 37,35% | 1,00 | -0,00R | €-0,80 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | 3 | 226 | 226 | 35,40% | 0,92 | -0,04R | €-89,37 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | 7 | 428 | 428 | 41,59% | 1,00 | 0,00R | €8,66 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | 9 | 356 | 356 | 39,33% | 0,94 | -0,03R | €-113,03 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | 0 | 43 | 43 | 48,84% | 1,55 | 0,22R | €92,56 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | 0 | 43 | 43 | 37,21% | 1,43 | 0,17R | €72,42 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | 0 | 116 | 116 | 32,76% | 0,95 | -0,02R | €-27,43 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | 2 | 157 | 157 | 34,39% | 0,83 | -0,09R | €-138,48 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | 0 | 47 | 47 | 19,15% | 0,74 | -0,20R | €-92,41 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | 0 | 47 | 47 | 19,15% | 0,74 | -0,20R | €-92,41 |
| SHADOW_COMBO_MEAN_REVERSION | 0 | 75 | 75 | 49,33% | 1,23 | 0,10R | €76,44 |
| SHADOW_COMBO_SCANNER | 4 | 259 | 259 | 35,52% | 1,11 | 0,06R | €160,18 |
| SHADOW_COMBO_TREND | 13 | 337 | 337 | 31,45% | 0,91 | -0,06R | €-186,27 |
| SHADOW_DOGE_BOLLINGER_1H | 0 | 7 | 7 | 57,14% | 1,03 | 0,02R | €1,06 |
| SHADOW_DOGE_DONCHIAN_1H | 0 | 9 | 9 | 33,33% | 0,61 | -0,29R | €-26,05 |
| SHADOW_DOGE_EMA_1H | 0 | 16 | 16 | 25,00% | 0,43 | -0,40R | €-63,80 |
| SHADOW_DONCHIAN_1H | 9 | 169 | 169 | 27,81% | 0,79 | -0,14R | €-238,34 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | 9 | 99 | 99 | 29,29% | 0,71 | -0,18R | €-173,26 |
| SHADOW_EMA_TREND_1H | 12 | 343 | 343 | 30,61% | 0,88 | -0,07R | €-242,98 |
| SHADOW_ETH_ADAPTIVE_1H | 0 | 12 | 12 | 33,33% | 0,37 | -0,46R | €-55,67 |
| SHADOW_ETH_BOLLINGER_1H | 0 | 6 | 6 | 66,67% | 1,46 | 0,17R | €10,43 |
| SHADOW_ETH_DONCHIAN_1H | 0 | 11 | 11 | 27,27% | 0,35 | -0,54R | €-58,86 |
| SHADOW_ETH_EMA_1H | 0 | 17 | 17 | 35,29% | 0,37 | -0,45R | €-76,84 |
| SHADOW_ETH_EMA_4H | 0 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,23 |
| SHADOW_GLOBAL_PURE | 0 | 10 | 10 | 50,00% | 1,24 | 0,13R | €13,30 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | 5 | 203 | 203 | 32,51% | 1,00 | 0,00R | €1,97 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | 3 | 377 | 377 | 66,05% | 1,39 | 0,13R | €474,69 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | 4 | 178 | 178 | 32,58% | 1,01 | 0,01R | €11,68 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | 4 | 185 | 185 | 30,27% | 0,98 | -0,01R | €-26,41 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | 3 | 131 | 131 | 31,30% | 0,94 | -0,04R | €-55,49 |
| SHADOW_MASTER_ADAPTIVE_V1 | 4 | 198 | 198 | 31,82% | 0,96 | -0,02R | €-45,16 |
| Forza relativa 1H V1 | 12 | 425 | 425 | 29,65% | 0,87 | -0,08R | €-326,03 |
| Forza relativa 1H V2 | 5 | 185 | 172 | 36,22% | 1,17 | 0,09R | €165,60 |
| SHADOW_SCANNER_BOTTOM10_SHORT | 8 | 128 | 128 | 28,91% | 0,57 | -0,24R | €-310,14 |
| SHADOW_SCANNER_BOTTOM15_SHORT | 8 | 128 | 128 | 28,91% | 0,57 | -0,24R | €-310,14 |
| SHADOW_SCANNER_BOTTOM20_SHORT | 8 | 128 | 128 | 28,91% | 0,57 | -0,24R | €-310,14 |
| SHADOW_SCANNER_BOTTOM5_SHORT | 7 | 163 | 163 | 31,90% | 0,81 | -0,10R | €-169,85 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | 5 | 147 | 147 | 50,34% | 0,77 | -0,11R | €-158,93 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | 6 | 126 | 126 | 49,21% | 0,72 | -0,13R | €-164,19 |
| SHADOW_SCANNER_TOP10_LONG | 4 | 195 | 195 | 34,87% | 0,98 | -0,01R | €-23,26 |
| SHADOW_SCANNER_TOP15_LONG | 4 | 196 | 196 | 34,69% | 0,97 | -0,02R | €-34,37 |
| SHADOW_SCANNER_TOP20_LONG | 4 | 196 | 196 | 34,69% | 0,97 | -0,02R | €-34,37 |
| SHADOW_SCANNER_TOP5_BTC | 4 | 250 | 250 | 34,80% | 1,12 | 0,06R | €159,42 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | 1 | 124 | 124 | 31,45% | 0,87 | -0,07R | €-90,72 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | 3 | 204 | 204 | 32,35% | 0,93 | -0,04R | €-83,26 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | 2 | 211 | 211 | 44,55% | 1,16 | 0,07R | €148,86 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | 2 | 178 | 178 | 33,71% | 1,04 | 0,02R | €37,12 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | 3 | 221 | 221 | 44,34% | 1,16 | 0,07R | €160,28 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | 3 | 185 | 185 | 33,51% | 1,05 | 0,03R | €48,07 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | 4 | 254 | 254 | 42,52% | 1,05 | 0,02R | €62,19 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | 4 | 200 | 200 | 31,50% | 0,96 | -0,02R | €-40,74 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | 4 | 190 | 190 | 31,05% | 0,97 | -0,02R | €-33,05 |
| SHADOW_SCANNER_TOP5_LONG | 4 | 274 | 274 | 36,50% | 1,11 | 0,06R | €155,06 |
| SHADOW_SOL_ADAPTIVE_1H | 1 | 18 | 18 | 27,78% | 0,44 | -0,45R | €-80,57 |
| SHADOW_SOL_ADAPTIVE_4H | 0 | 2 | 2 | 50,00% | 1,18 | 0,10R | €1,93 |
| SHADOW_SOL_BOLLINGER_1H | 0 | 11 | 11 | 45,45% | 0,61 | -0,24R | €-26,43 |
| SHADOW_SOL_BOLLINGER_4H | 0 | 2 | 2 | 100,00% | ∞ | 1,20R | €24,01 |
| SHADOW_SOL_DONCHIAN_1H | 1 | 11 | 11 | 36,36% | 0,77 | -0,16R | €-17,67 |
| SHADOW_SOL_DONCHIAN_4H | 0 | 2 | 2 | 50,00% | 1,29 | 0,15R | €3,02 |
| SHADOW_SOL_EMA_1H | 1 | 17 | 17 | 29,41% | 0,59 | -0,32R | €-54,38 |
| SHADOW_SOL_EMA_4H | 0 | 3 | 3 | 0,00% | 0,00 | -1,05R | €-31,62 |

### Matrice strategia × regime all’entrata

| Profilo | Regime entrata | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | ALT_ROTATION_DOWN | 0 | 36 | 36 | 22,22% | 0,48 | -0,32R | €-116,66 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | ALT_ROTATION_UP | 0 | 44 | 44 | 40,91% | 1,30 | 0,14R | €60,32 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | RANGE | 2 | 84 | 84 | 36,90% | 0,75 | -0,12R | €-102,36 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | RANGE_HIGH_VOL | 1 | 7 | 7 | 14,29% | 0,04 | -0,74R | €-51,71 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TRANSITION | 0 | 31 | 31 | 35,48% | 1,17 | 0,09R | €26,53 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_DOWN | 0 | 20 | 20 | 30,00% | 0,42 | -0,36R | €-71,46 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_UP | 1 | 51 | 51 | 17,65% | 0,47 | -0,27R | €-136,57 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_UP_HIGH_VOL | 0 | 5 | 5 | 20,00% | 0,09 | -0,19R | €-9,63 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | ALT_ROTATION_DOWN | 0 | 35 | 35 | 20,00% | 0,30 | -0,49R | €-170,51 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | ALT_ROTATION_UP | 0 | 31 | 31 | 41,94% | 1,38 | 0,16R | €48,72 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | RANGE | 2 | 79 | 79 | 35,44% | 0,59 | -0,21R | €-161,96 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | RANGE_HIGH_VOL | 1 | 6 | 6 | 0,00% | 0,00 | -0,90R | €-53,98 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TRANSITION | 0 | 30 | 30 | 36,67% | 1,33 | 0,16R | €48,62 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TREND_DOWN | 0 | 17 | 17 | 29,41% | 0,38 | -0,37R | €-63,22 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TREND_UP | 1 | 48 | 48 | 16,67% | 0,31 | -0,37R | €-177,08 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 25,00% | 0,09 | -0,24R | €-9,50 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | ALT_ROTATION_DOWN | 0 | 6 | 6 | 50,00% | 0,78 | -0,12R | €-7,06 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | ALT_ROTATION_UP | 0 | 39 | 39 | 56,41% | 1,39 | 0,17R | €66,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | RANGE | 1 | 54 | 54 | 38,89% | 0,44 | -0,35R | €-188,25 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | TRANSITION | 0 | 14 | 14 | 50,00% | 1,19 | 0,10R | €13,42 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | TREND_DOWN | 0 | 11 | 11 | 45,45% | 0,46 | -0,30R | €-32,65 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | TREND_UP | 1 | 37 | 37 | 43,24% | 0,85 | -0,08R | €-28,60 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | ALT_ROTATION_DOWN | 0 | 5 | 5 | 40,00% | 1,08 | 0,04R | €1,77 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | ALT_ROTATION_UP | 0 | 41 | 41 | 41,46% | 1,33 | 0,15R | €61,04 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | RANGE | 1 | 56 | 56 | 30,36% | 0,40 | -0,35R | €-197,04 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | TRANSITION | 0 | 14 | 14 | 35,71% | 1,30 | 0,14R | €18,91 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | TREND_DOWN | 0 | 11 | 11 | 36,36% | 0,64 | -0,23R | €-25,22 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | TREND_UP | 1 | 36 | 36 | 25,00% | 0,82 | -0,07R | €-26,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | ALT_ROTATION_DOWN | 0 | 9 | 9 | 11,11% | 0,37 | -0,37R | €-33,41 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | ALT_ROTATION_UP | 0 | 44 | 44 | 38,64% | 1,15 | 0,07R | €31,09 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | RANGE | 1 | 67 | 67 | 32,84% | 0,61 | -0,22R | €-149,71 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | RANGE_HIGH_VOL | 0 | 7 | 7 | 0,00% | 0,00 | -0,93R | €-65,23 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | RANGE_LOW_VOL | 0 | 2 | 2 | 50,00% | 1,93 | 0,47R | €9,42 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TRANSITION | 0 | 20 | 20 | 35,00% | 1,46 | 0,19R | €38,11 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TREND_DOWN | 0 | 14 | 14 | 42,86% | 0,86 | -0,08R | €-11,70 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TREND_UP | 1 | 54 | 54 | 29,63% | 0,81 | -0,09R | €-49,19 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 25,00% | 0,09 | -0,24R | €-9,50 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | ALT_ROTATION_DOWN | 0 | 9 | 9 | 11,11% | 0,18 | -0,48R | €-43,52 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | ALT_ROTATION_UP | 0 | 36 | 36 | 38,89% | 1,19 | 0,09R | €32,59 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | RANGE | 1 | 58 | 58 | 34,48% | 0,53 | -0,25R | €-144,60 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | RANGE_HIGH_VOL | 0 | 6 | 6 | 0,00% | 0,00 | -0,92R | €-55,08 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TRANSITION | 0 | 19 | 19 | 36,84% | 1,81 | 0,31R | €58,34 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TREND_DOWN | 0 | 13 | 13 | 46,15% | 0,92 | -0,05R | €-6,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TREND_UP | 1 | 49 | 49 | 28,57% | 0,56 | -0,21R | €-101,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 25,00% | 0,09 | -0,24R | €-9,50 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | RANGE | 2 | 94 | 94 | 31,91% | 0,62 | -0,21R | €-194,02 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | RANGE_LOW_VOL | 0 | 2 | 2 | 50,00% | 1,93 | 0,47R | €9,42 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | ALT_ROTATION_DOWN | 0 | 17 | 17 | 5,88% | 0,04 | -0,87R | €-147,58 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | ALT_ROTATION_UP | 0 | 44 | 44 | 31,82% | 0,83 | -0,09R | €-41,40 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | RANGE | 2 | 82 | 82 | 31,71% | 0,67 | -0,18R | €-150,75 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | RANGE_LOW_VOL | 0 | 2 | 2 | 50,00% | 1,93 | 0,47R | €9,42 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | TRANSITION | 0 | 15 | 15 | 13,33% | 0,35 | -0,49R | €-73,97 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | TREND_DOWN | 0 | 22 | 22 | 31,82% | 0,53 | -0,29R | €-63,14 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | TREND_UP | 0 | 14 | 14 | 7,14% | 0,26 | -0,41R | €-57,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | ALT_ROTATION_DOWN | 0 | 24 | 24 | 8,33% | 0,14 | -0,67R | €-161,06 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | ALT_ROTATION_UP | 0 | 50 | 50 | 36,00% | 1,12 | 0,06R | €29,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | RANGE | 3 | 104 | 104 | 34,62% | 0,73 | -0,15R | €-153,32 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 3,88 | 0,97R | €29,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | TRANSITION | 0 | 22 | 22 | 22,73% | 0,70 | -0,16R | €-34,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | TREND_DOWN | 0 | 24 | 24 | 37,50% | 0,71 | -0,16R | €-39,37 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | TREND_UP | 1 | 70 | 70 | 24,29% | 0,66 | -0,17R | €-118,41 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | ALT_ROTATION_DOWN | 0 | 24 | 24 | 8,33% | 0,09 | -0,71R | €-171,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | ALT_ROTATION_UP | 0 | 38 | 38 | 36,84% | 1,12 | 0,06R | €21,23 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | RANGE | 3 | 97 | 97 | 32,99% | 0,59 | -0,22R | €-210,35 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | TRANSITION | 0 | 21 | 21 | 23,81% | 0,77 | -0,11R | €-23,94 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | TREND_DOWN | 0 | 21 | 21 | 38,10% | 0,81 | -0,10R | €-21,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | TREND_UP | 1 | 65 | 65 | 23,08% | 0,47 | -0,27R | €-175,79 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | ALT_ROTATION_DOWN | 0 | 9 | 9 | 11,11% | 0,37 | -0,37R | €-33,41 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | ALT_ROTATION_UP | 0 | 45 | 45 | 40,00% | 1,24 | 0,11R | €50,65 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | RANGE | 1 | 67 | 67 | 35,82% | 0,75 | -0,13R | €-90,05 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | RANGE_HIGH_VOL | 0 | 7 | 7 | 0,00% | 0,00 | -0,93R | €-65,23 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TRANSITION | 0 | 20 | 20 | 35,00% | 1,46 | 0,19R | €38,11 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TREND_DOWN | 0 | 14 | 14 | 42,86% | 0,86 | -0,08R | €-11,70 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TREND_UP | 1 | 54 | 54 | 29,63% | 0,81 | -0,09R | €-49,19 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 25,00% | 0,09 | -0,24R | €-9,50 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | ALT_ROTATION_DOWN | 0 | 53 | 53 | 32,08% | 0,42 | -0,35R | €-184,74 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | ALT_ROTATION_UP | 0 | 54 | 54 | 48,15% | 1,05 | 0,03R | €14,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | RANGE | 1 | 118 | 118 | 38,14% | 0,88 | -0,05R | €-60,01 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | RANGE_HIGH_VOL | 1 | 17 | 17 | 29,41% | 0,39 | -0,42R | €-70,97 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TRANSITION | 1 | 34 | 34 | 50,00% | 1,34 | 0,12R | €42,01 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_DOWN | 0 | 30 | 30 | 50,00% | 0,99 | -0,01R | €-1,74 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_UP | 1 | 80 | 80 | 41,25% | 0,85 | -0,07R | €-56,08 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_UP_HIGH_VOL | 0 | 5 | 5 | 40,00% | 1,66 | 0,14R | €6,91 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | ALT_ROTATION_DOWN | 0 | 15 | 15 | 6,67% | 0,04 | -0,92R | €-138,39 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | ALT_ROTATION_UP | 0 | 15 | 15 | 26,67% | 0,68 | -0,24R | €-35,76 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | RANGE | 1 | 38 | 38 | 34,21% | 0,51 | -0,30R | €-113,31 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | RANGE_LOW_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,96R | €19,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | TRANSITION | 0 | 2 | 2 | 50,00% | 1,76 | 0,41R | €8,25 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | TREND_DOWN | 0 | 8 | 8 | 37,50% | 0,75 | -0,10R | €-8,35 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | TREND_UP | 0 | 24 | 24 | 16,67% | 0,34 | -0,48R | €-114,61 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | ALT_ROTATION_DOWN | 0 | 48 | 48 | 16,67% | 0,31 | -0,43R | €-206,78 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | ALT_ROTATION_UP | 0 | 48 | 48 | 35,42% | 1,09 | 0,04R | €19,39 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | RANGE | 2 | 101 | 101 | 34,65% | 0,72 | -0,15R | €-151,62 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | RANGE_HIGH_VOL | 1 | 17 | 17 | 17,65% | 0,26 | -0,50R | €-85,45 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 3,88 | 0,97R | €29,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TRANSITION | 0 | 32 | 32 | 37,50% | 1,50 | 0,21R | €67,69 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_DOWN | 0 | 24 | 24 | 37,50% | 0,71 | -0,16R | €-39,37 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_UP | 1 | 69 | 69 | 23,19% | 0,60 | -0,20R | €-138,28 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_UP_HIGH_VOL | 0 | 5 | 5 | 20,00% | 0,09 | -0,19R | €-9,63 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | ALT_ROTATION_DOWN | 0 | 48 | 48 | 16,67% | 0,31 | -0,43R | €-206,78 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | ALT_ROTATION_UP | 0 | 50 | 50 | 36,00% | 1,12 | 0,06R | €29,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | RANGE | 2 | 102 | 102 | 34,31% | 0,70 | -0,16R | €-161,75 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | RANGE_HIGH_VOL | 1 | 17 | 17 | 17,65% | 0,26 | -0,50R | €-85,45 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 3,88 | 0,97R | €29,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TRANSITION | 0 | 32 | 32 | 37,50% | 1,50 | 0,21R | €67,69 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_DOWN | 0 | 24 | 24 | 37,50% | 0,71 | -0,16R | €-39,37 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_UP | 1 | 69 | 69 | 23,19% | 0,60 | -0,20R | €-138,28 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_UP_HIGH_VOL | 0 | 6 | 6 | 16,67% | 0,08 | -0,16R | €-9,76 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | ALT_ROTATION_DOWN | 0 | 48 | 48 | 16,67% | 0,26 | -0,48R | €-230,77 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | ALT_ROTATION_UP | 0 | 38 | 38 | 36,84% | 1,12 | 0,06R | €21,23 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | RANGE | 2 | 96 | 96 | 32,29% | 0,54 | -0,25R | €-235,22 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | RANGE_HIGH_VOL | 1 | 13 | 13 | 7,69% | 0,26 | -0,55R | €-71,01 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TRANSITION | 0 | 31 | 31 | 38,71% | 1,76 | 0,31R | €94,78 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TREND_DOWN | 0 | 21 | 21 | 38,10% | 0,81 | -0,10R | €-21,13 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TREND_UP | 1 | 64 | 64 | 21,88% | 0,39 | -0,31R | €-200,65 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TREND_UP_HIGH_VOL | 0 | 5 | 5 | 20,00% | 0,09 | -0,19R | €-9,63 |
| MAIN | ALT_ROTATION_DOWN | 0 | 20 | 20 | 30,00% | 0,89 | -0,05R | €-10,79 |
| MAIN | ALT_ROTATION_UP | 5 | 33 | 33 | 21,21% | 0,40 | -0,41R | €-134,29 |
| MAIN | RANGE | 3 | 59 | 59 | 20,34% | 0,57 | -0,29R | €-168,37 |
| MAIN | RANGE_HIGH_VOL | 2 | 8 | 8 | 12,50% | 0,48 | -0,27R | €-21,36 |
| MAIN | RANGE_LOW_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| MAIN | TRANSITION | 0 | 21 | 21 | 23,81% | 0,52 | -0,35R | €-74,24 |
| MAIN | TREND_DOWN | 0 | 15 | 15 | 26,67% | 0,72 | -0,15R | €-22,75 |
| MAIN | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,96 | 0,49R | €9,73 |
| MAIN | TREND_UP | 2 | 37 | 37 | 29,73% | 0,96 | -0,02R | €-8,04 |
| MAIN | TREND_UP_HIGH_VOL | 1 | 7 | 7 | 42,86% | 1,42 | 0,25R | €17,52 |
| RSI_EXTREME_LONG_15M | ALT_ROTATION_UP | 0 | 3 | 3 | 33,33% | 0,63 | -0,21R | €-6,42 |
| RSI_EXTREME_LONG_15M | RANGE | 1 | 11 | 11 | 18,18% | 0,10 | -0,77R | €-85,05 |
| RSI_EXTREME_LONG_15M | TRANSITION | 0 | 2 | 2 | 50,00% | 1,14 | 0,08R | €1,56 |
| RSI_EXTREME_LONG_15M | TREND_DOWN | 0 | 4 | 4 | 75,00% | 5,55 | 0,50R | €20,01 |
| RSI_EXTREME_LONG_15M | TREND_UP | 0 | 2 | 2 | 50,00% | 0,63 | -0,19R | €-3,79 |
| RSI_EXTREME_SHORT_15M | ALT_ROTATION_DOWN | 0 | 2 | 2 | 100,00% | ∞ | 1,04R | €20,80 |
| RSI_EXTREME_SHORT_15M | ALT_ROTATION_UP | 0 | 10 | 10 | 30,00% | 0,22 | -0,48R | €-48,02 |
| RSI_EXTREME_SHORT_15M | RANGE | 0 | 10 | 10 | 30,00% | 0,42 | -0,38R | €-37,61 |
| RSI_EXTREME_SHORT_15M | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -0,41R | €-4,13 |
| RSI_EXTREME_SHORT_15M | TREND_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 0,31R | €3,08 |
| RSI_EXTREME_SHORT_15M | TREND_UP | 0 | 12 | 12 | 25,00% | 0,34 | -0,45R | €-53,48 |
| Bilanciata 1H V1 | ALT_ROTATION_DOWN | 0 | 56 | 56 | 21,43% | 0,44 | -0,39R | €-221,17 |
| Bilanciata 1H V1 | ALT_ROTATION_UP | 1 | 64 | 64 | 39,06% | 1,16 | 0,08R | €54,04 |
| Bilanciata 1H V1 | RANGE | 7 | 133 | 133 | 41,35% | 1,19 | 0,10R | €131,46 |
| Bilanciata 1H V1 | RANGE_HIGH_VOL | 3 | 25 | 25 | 16,00% | 0,33 | -0,51R | €-126,98 |
| Bilanciata 1H V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| Bilanciata 1H V1 | TRANSITION | 0 | 71 | 71 | 40,85% | 1,24 | 0,13R | €91,68 |
| Bilanciata 1H V1 | TREND_DOWN | 0 | 29 | 29 | 34,48% | 0,78 | -0,11R | €-32,03 |
| Bilanciata 1H V1 | TREND_DOWN_HIGH_VOL | 0 | 3 | 3 | 66,67% | 2,44 | 0,53R | €15,80 |
| Bilanciata 1H V1 | TREND_UP | 4 | 105 | 105 | 31,43% | 0,93 | -0,04R | €-39,28 |
| Bilanciata 1H V1 | TREND_UP_HIGH_VOL | 0 | 18 | 18 | 22,22% | 0,65 | -0,23R | €-41,15 |
| Bilanciata 1H V2 | ALT_ROTATION_UP | 2 | 45 | 39 | 40,00% | 1,20 | 0,10R | €46,24 |
| Bilanciata 1H V2 | RANGE | 3 | 100 | 91 | 36,00% | 0,89 | -0,06R | €-64,87 |
| Bilanciata 1H V2 | TRANSITION | 0 | 55 | 46 | 41,82% | 1,60 | 0,29R | €160,00 |
| Bilanciata 1H V3 Filtered | ALT_ROTATION_DOWN | 0 | 42 | 42 | 26,19% | 0,54 | -0,30R | €-128,02 |
| Bilanciata 1H V3 Filtered | ALT_ROTATION_UP | 0 | 36 | 36 | 33,33% | 1,24 | 0,13R | €45,30 |
| Bilanciata 1H V3 Filtered | RANGE | 4 | 91 | 91 | 42,86% | 1,15 | 0,08R | €71,66 |
| Bilanciata 1H V3 Filtered | RANGE_HIGH_VOL | 2 | 6 | 6 | 16,67% | 0,37 | -0,55R | €-32,98 |
| Bilanciata 1H V3 Filtered | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| Bilanciata 1H V3 Filtered | TRANSITION | 1 | 37 | 37 | 35,14% | 1,09 | 0,05R | €19,63 |
| Bilanciata 1H V3 Filtered | TREND_DOWN | 0 | 22 | 22 | 31,82% | 0,29 | -0,44R | €-95,77 |
| Bilanciata 1H V3 Filtered | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,34R | €26,74 |
| Bilanciata 1H V3 Filtered | TREND_UP | 2 | 60 | 60 | 31,67% | 1,06 | 0,03R | €19,01 |
| Bilanciata 1H V3 Filtered | TREND_UP_HIGH_VOL | 0 | 17 | 17 | 23,53% | 0,65 | -0,24R | €-41,19 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 0 | 31 | 31 | 19,35% | 0,26 | -0,52R | €-161,39 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | ALT_ROTATION_UP | 0 | 34 | 34 | 35,29% | 1,39 | 0,19R | €66,29 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | RANGE | 4 | 69 | 69 | 40,58% | 0,88 | -0,06R | €-44,50 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | RANGE_HIGH_VOL | 2 | 4 | 4 | 25,00% | 0,61 | -0,30R | €-12,15 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TRANSITION | 1 | 29 | 29 | 34,48% | 1,09 | 0,05R | €13,94 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TREND_DOWN | 0 | 23 | 23 | 30,43% | 0,27 | -0,46R | €-106,88 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,34R | €26,74 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TREND_UP | 2 | 39 | 39 | 25,64% | 0,78 | -0,11R | €-41,83 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 33,33% | 0,94 | -0,04R | €-1,20 |
| Rapida 1H V1 | ALT_ROTATION_DOWN | 0 | 22 | 22 | 22,73% | 0,43 | -0,42R | €-91,69 |
| Rapida 1H V1 | ALT_ROTATION_UP | 0 | 13 | 13 | 53,85% | 1,58 | 0,29R | €37,18 |
| Rapida 1H V1 | RANGE | 0 | 67 | 67 | 44,78% | 1,20 | 0,11R | €71,76 |
| Rapida 1H V1 | RANGE_HIGH_VOL | 0 | 11 | 11 | 0,00% | 0,00 | -1,09R | €-119,90 |
| Rapida 1H V1 | TRANSITION | 0 | 26 | 26 | 50,00% | 1,57 | 0,27R | €68,95 |
| Rapida 1H V1 | TREND_UP | 0 | 48 | 48 | 41,67% | 0,97 | -0,02R | €-9,20 |
| Rapida 1H V1 | TREND_UP_HIGH_VOL | 0 | 21 | 21 | 28,57% | 0,59 | -0,28R | €-58,55 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | ALT_ROTATION_DOWN | 0 | 11 | 11 | 18,18% | 0,25 | -0,50R | €-54,74 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | ALT_ROTATION_UP | 0 | 40 | 40 | 50,00% | 1,44 | 0,17R | €66,26 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | RANGE | 0 | 41 | 41 | 36,59% | 0,92 | -0,04R | €-18,41 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,02R | €-10,15 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TRANSITION | 0 | 23 | 23 | 39,13% | 1,16 | 0,07R | €16,89 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TREND_UP | 1 | 48 | 48 | 31,25% | 0,80 | -0,08R | €-37,28 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 66,67% | 108,55 | 0,48R | €14,34 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | ALT_ROTATION_DOWN | 0 | 19 | 19 | 15,79% | 0,25 | -0,52R | €-99,51 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | ALT_ROTATION_UP | 0 | 52 | 52 | 44,23% | 1,10 | 0,05R | €24,62 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | RANGE | 3 | 107 | 107 | 37,38% | 0,88 | -0,06R | €-67,15 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 100,00% | ∞ | 1,47R | €44,18 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | TRANSITION | 1 | 28 | 28 | 32,14% | 0,74 | -0,14R | €-38,98 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | TREND_DOWN | 0 | 32 | 32 | 34,38% | 0,76 | -0,13R | €-41,49 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | TREND_UP | 2 | 71 | 71 | 28,17% | 0,74 | -0,12R | €-83,53 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | ALT_ROTATION_DOWN | 0 | 37 | 37 | 18,92% | 0,33 | -0,49R | €-181,74 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | ALT_ROTATION_UP | 0 | 53 | 53 | 45,28% | 1,16 | 0,07R | €38,51 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | RANGE | 3 | 137 | 137 | 42,34% | 1,12 | 0,06R | €78,04 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 100,00% | ∞ | 1,47R | €44,18 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TRANSITION | 1 | 30 | 30 | 36,67% | 0,94 | -0,03R | €-9,29 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TREND_DOWN | 0 | 32 | 32 | 34,38% | 0,76 | -0,13R | €-41,49 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TREND_UP | 2 | 87 | 87 | 27,59% | 0,65 | -0,18R | €-155,74 |
| SHADOW_1H_FAST_NO_PEPE_V1 | ALT_ROTATION_DOWN | 0 | 77 | 77 | 20,78% | 0,38 | -0,43R | €-330,64 |
| SHADOW_1H_FAST_NO_PEPE_V1 | ALT_ROTATION_UP | 0 | 58 | 58 | 39,66% | 0,95 | -0,03R | €-15,73 |
| SHADOW_1H_FAST_NO_PEPE_V1 | RANGE | 1 | 159 | 159 | 38,99% | 0,90 | -0,05R | €-82,45 |
| SHADOW_1H_FAST_NO_PEPE_V1 | RANGE_HIGH_VOL | 2 | 18 | 18 | 33,33% | 0,70 | -0,18R | €-32,41 |
| SHADOW_1H_FAST_NO_PEPE_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 153,43 | 0,97R | €29,23 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TRANSITION | 1 | 44 | 44 | 43,18% | 1,30 | 0,13R | €57,03 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_DOWN | 0 | 38 | 38 | 36,84% | 0,80 | -0,11R | €-41,96 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_UP | 2 | 102 | 102 | 28,43% | 0,70 | -0,16R | €-159,27 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_UP_HIGH_VOL | 0 | 5 | 5 | 60,00% | 110,03 | 0,58R | €29,07 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | ALT_ROTATION_DOWN | 0 | 44 | 44 | 22,73% | 0,37 | -0,46R | €-202,42 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | ALT_ROTATION_UP | 0 | 43 | 43 | 37,21% | 0,98 | -0,01R | €-4,78 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | RANGE | 1 | 94 | 94 | 46,81% | 1,35 | 0,15R | €145,13 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | RANGE_HIGH_VOL | 2 | 6 | 6 | 33,33% | 0,41 | -0,42R | €-24,95 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | RANGE_LOW_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,48R | €29,66 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TRANSITION | 1 | 31 | 31 | 41,94% | 1,24 | 0,10R | €32,16 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_DOWN | 0 | 22 | 22 | 27,27% | 0,59 | -0,23R | €-50,88 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_UP | 1 | 58 | 58 | 27,59% | 0,60 | -0,22R | €-126,66 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -0,51R | €-10,27 |
| SHADOW_1H_FAST_TP2_V1 | ALT_ROTATION_DOWN | 0 | 75 | 75 | 20,00% | 0,42 | -0,40R | €-298,22 |
| SHADOW_1H_FAST_TP2_V1 | ALT_ROTATION_UP | 0 | 59 | 59 | 40,68% | 1,15 | 0,07R | €43,11 |
| SHADOW_1H_FAST_TP2_V1 | RANGE | 2 | 140 | 140 | 37,14% | 0,90 | -0,05R | €-73,64 |
| SHADOW_1H_FAST_TP2_V1 | RANGE_HIGH_VOL | 1 | 18 | 18 | 22,22% | 0,43 | -0,37R | €-66,50 |
| SHADOW_1H_FAST_TP2_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 33,33% | 1,89 | 0,31R | €9,20 |
| SHADOW_1H_FAST_TP2_V1 | TRANSITION | 0 | 43 | 43 | 41,86% | 1,63 | 0,25R | €107,35 |
| SHADOW_1H_FAST_TP2_V1 | TREND_DOWN | 0 | 32 | 32 | 37,50% | 0,73 | -0,16R | €-50,72 |
| SHADOW_1H_FAST_TP2_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_TP2_V1 | TREND_UP | 2 | 93 | 93 | 21,51% | 0,53 | -0,25R | €-236,27 |
| SHADOW_1H_FAST_TP2_V1 | TREND_UP_HIGH_VOL | 0 | 7 | 7 | 14,29% | 0,04 | -0,30R | €-21,19 |
| Rapida 1H V2 | ALT_ROTATION_UP | 0 | 9 | 8 | 22,22% | 0,21 | -0,68R | €-61,12 |
| Rapida 1H V2 | RANGE | 1 | 32 | 26 | 34,38% | 0,63 | -0,21R | €-67,05 |
| Rapida 1H V2 | TRANSITION | 0 | 3 | 3 | 33,33% | 0,53 | -0,19R | €-5,76 |
| Rapida 1H V3 Filtered | ALT_ROTATION_DOWN | 0 | 74 | 74 | 20,27% | 0,37 | -0,43R | €-315,89 |
| Rapida 1H V3 Filtered | ALT_ROTATION_UP | 0 | 57 | 57 | 40,35% | 1,06 | 0,03R | €16,05 |
| Rapida 1H V3 Filtered | RANGE | 1 | 144 | 144 | 39,58% | 0,94 | -0,03R | €-46,15 |
| Rapida 1H V3 Filtered | RANGE_HIGH_VOL | 2 | 17 | 17 | 29,41% | 0,57 | -0,27R | €-45,44 |
| Rapida 1H V3 Filtered | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 183,36 | 0,98R | €29,26 |
| Rapida 1H V3 Filtered | TRANSITION | 1 | 40 | 40 | 42,50% | 1,21 | 0,10R | €38,82 |
| Rapida 1H V3 Filtered | TREND_DOWN | 0 | 34 | 34 | 32,35% | 0,72 | -0,15R | €-51,64 |
| Rapida 1H V3 Filtered | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| Rapida 1H V3 Filtered | TREND_UP | 1 | 107 | 107 | 37,38% | 1,00 | 0,00R | €1,78 |
| Rapida 1H V3 Filtered | TREND_UP_HIGH_VOL | 0 | 24 | 24 | 29,17% | 0,60 | -0,24R | €-56,81 |
| SHADOW_1H_FAST_V3_CAP75_V1 | ALT_ROTATION_DOWN | 0 | 56 | 56 | 23,21% | 0,41 | -0,41R | €-232,01 |
| SHADOW_1H_FAST_V3_CAP75_V1 | ALT_ROTATION_UP | 0 | 51 | 51 | 41,18% | 1,07 | 0,03R | €17,37 |
| SHADOW_1H_FAST_V3_CAP75_V1 | RANGE | 1 | 115 | 115 | 41,74% | 1,10 | 0,05R | €56,31 |
| SHADOW_1H_FAST_V3_CAP75_V1 | RANGE_HIGH_VOL | 2 | 8 | 8 | 25,00% | 0,32 | -0,46R | €-36,85 |
| SHADOW_1H_FAST_V3_CAP75_V1 | RANGE_LOW_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,48R | €29,66 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TRANSITION | 1 | 32 | 32 | 40,62% | 1,00 | 0,00R | €0,72 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_DOWN | 0 | 26 | 26 | 26,92% | 0,62 | -0,21R | €-55,77 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_UP | 1 | 68 | 68 | 29,41% | 0,67 | -0,17R | €-115,95 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 33,33% | 3,38 | 0,02R | €0,64 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | ALT_ROTATION_DOWN | 0 | 13 | 13 | 23,08% | 0,19 | -0,65R | €-84,38 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | ALT_ROTATION_UP | 0 | 44 | 44 | 56,82% | 1,24 | 0,11R | €46,83 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | RANGE | 1 | 69 | 69 | 43,48% | 0,89 | -0,07R | €-45,83 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TRANSITION | 0 | 15 | 15 | 53,33% | 1,49 | 0,20R | €30,11 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TREND_DOWN | 0 | 14 | 14 | 42,86% | 0,93 | -0,04R | €-5,61 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TREND_UP | 1 | 47 | 47 | 51,06% | 0,97 | -0,01R | €-6,79 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | ALT_ROTATION_DOWN | 0 | 12 | 12 | 16,67% | 0,19 | -0,63R | €-75,54 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | ALT_ROTATION_UP | 0 | 45 | 45 | 42,22% | 1,11 | 0,05R | €21,97 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | RANGE | 1 | 71 | 71 | 38,03% | 0,94 | -0,03R | €-21,73 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,49R | €14,87 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TRANSITION | 0 | 15 | 15 | 46,67% | 1,45 | 0,19R | €28,11 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TREND_DOWN | 0 | 14 | 14 | 35,71% | 0,90 | -0,06R | €-8,11 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TREND_UP | 1 | 48 | 48 | 33,33% | 0,88 | -0,05R | €-24,39 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 0 | 18 | 18 | 5,56% | 0,10 | -0,73R | €-131,04 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | ALT_ROTATION_UP | 0 | 53 | 53 | 39,62% | 0,99 | -0,01R | €-2,81 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | RANGE | 0 | 87 | 87 | 40,23% | 0,98 | -0,01R | €-7,71 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | RANGE_HIGH_VOL | 1 | 6 | 6 | 0,00% | 0,00 | -0,92R | €-55,08 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | RANGE_LOW_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,47R | €29,42 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TRANSITION | 0 | 23 | 23 | 43,48% | 1,31 | 0,14R | €32,01 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_DOWN | 0 | 20 | 20 | 40,00% | 0,93 | -0,04R | €-7,42 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_UP | 1 | 67 | 67 | 34,33% | 0,87 | -0,06R | €-43,23 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 66,67% | 118,27 | 0,52R | €15,64 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | ALT_ROTATION_DOWN | 0 | 46 | 46 | 17,39% | 0,32 | -0,51R | €-234,33 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | ALT_ROTATION_UP | 0 | 54 | 54 | 38,89% | 0,99 | -0,00R | €-1,39 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | RANGE | 3 | 145 | 145 | 40,00% | 0,96 | -0,02R | €-31,28 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 183,36 | 0,98R | €29,26 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TRANSITION | 1 | 24 | 24 | 33,33% | 0,91 | -0,04R | €-10,14 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TREND_DOWN | 0 | 34 | 34 | 32,35% | 0,72 | -0,15R | €-51,64 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TREND_UP | 1 | 93 | 93 | 32,26% | 0,79 | -0,11R | €-103,40 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | ALT_ROTATION_DOWN | 0 | 73 | 73 | 20,55% | 0,38 | -0,42R | €-304,46 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | ALT_ROTATION_UP | 0 | 56 | 56 | 37,50% | 0,91 | -0,04R | €-25,07 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | RANGE | 1 | 142 | 142 | 39,44% | 0,92 | -0,04R | €-60,88 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | RANGE_HIGH_VOL | 2 | 16 | 16 | 31,25% | 0,63 | -0,22R | €-35,31 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | RANGE_LOW_VOL | 0 | 3 | 3 | 66,67% | 183,36 | 0,98R | €29,26 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TRANSITION | 1 | 35 | 35 | 42,86% | 1,27 | 0,12R | €41,59 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_DOWN | 0 | 34 | 34 | 32,35% | 0,72 | -0,15R | €-51,64 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,02R | €-0,17 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_UP | 1 | 90 | 90 | 31,11% | 0,75 | -0,13R | €-120,96 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 50,00% | 59,13 | 0,39R | €15,50 |
| SHADOW_4H_WIDE | ALT_ROTATION_DOWN | 3 | 13 | 13 | 30,77% | 1,26 | 0,15R | €19,06 |
| SHADOW_4H_WIDE | ALT_ROTATION_UP | 8 | 25 | 25 | 24,00% | 0,47 | -0,41R | €-101,53 |
| SHADOW_4H_WIDE | RANGE | 7 | 51 | 51 | 17,65% | 0,66 | -0,25R | €-127,53 |
| SHADOW_4H_WIDE | RANGE_HIGH_VOL | 3 | 6 | 6 | 16,67% | 0,55 | -0,38R | €-22,80 |
| SHADOW_4H_WIDE | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_4H_WIDE | TRANSITION | 2 | 21 | 21 | 14,29% | 0,43 | -0,44R | €-92,77 |
| SHADOW_4H_WIDE | TREND_DOWN | 0 | 16 | 16 | 31,25% | 1,22 | 0,13R | €20,05 |
| SHADOW_4H_WIDE | TREND_DOWN_HIGH_VOL | 0 | 3 | 3 | 33,33% | 2,71 | 0,59R | €17,60 |
| SHADOW_4H_WIDE | TREND_UP | 5 | 36 | 36 | 22,22% | 0,91 | -0,05R | €-19,19 |
| SHADOW_4H_WIDE | TREND_UP_HIGH_VOL | 1 | 10 | 10 | 10,00% | 0,34 | -0,55R | €-54,65 |
| SHADOW_BOLLINGER_MR_1H | ALT_ROTATION_DOWN | 0 | 17 | 17 | 47,06% | 0,91 | -0,04R | €-7,32 |
| SHADOW_BOLLINGER_MR_1H | ALT_ROTATION_UP | 0 | 20 | 20 | 50,00% | 1,11 | 0,05R | €10,60 |
| SHADOW_BOLLINGER_MR_1H | RANGE | 1 | 53 | 53 | 45,28% | 1,02 | 0,01R | €3,84 |
| SHADOW_BOLLINGER_MR_1H | RANGE_HIGH_VOL | 1 | 4 | 4 | 50,00% | 1,39 | 0,21R | €8,27 |
| SHADOW_BOLLINGER_MR_1H | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_BOLLINGER_MR_1H | TRANSITION | 0 | 10 | 10 | 60,00% | 2,81 | 0,57R | €56,63 |
| SHADOW_BOLLINGER_MR_1H | TREND_DOWN | 0 | 8 | 8 | 62,50% | 2,18 | 0,34R | €26,82 |
| SHADOW_BOLLINGER_MR_1H | TREND_UP | 0 | 40 | 40 | 42,50% | 0,84 | -0,08R | €-30,24 |
| SHADOW_BOLLINGER_MR_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,31 | 0,17R | €3,31 |
| SHADOW_BTC_ADAPTIVE_1H | ALT_ROTATION_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 0,03R | €0,30 |
| SHADOW_BTC_ADAPTIVE_1H | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 0,52R | €5,16 |
| SHADOW_BTC_ADAPTIVE_1H | RANGE | 1 | 5 | 5 | 40,00% | 0,36 | -0,43R | €-21,25 |
| SHADOW_BTC_ADAPTIVE_1H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 0,88R | €8,85 |
| SHADOW_BTC_ADAPTIVE_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_BTC_ADAPTIVE_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,67 |
| SHADOW_BTC_BOLLINGER_1H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 50,00% | 0,32 | -0,38R | €-7,66 |
| SHADOW_BTC_BOLLINGER_1H | RANGE | 0 | 2 | 2 | 100,00% | ∞ | 1,37R | €27,33 |
| SHADOW_BTC_BOLLINGER_1H | RANGE_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_BOLLINGER_1H | TREND_DOWN | 0 | 2 | 2 | 100,00% | ∞ | 0,93R | €18,57 |
| SHADOW_BTC_BOLLINGER_1H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,37R | €13,67 |
| SHADOW_BTC_BOLLINGER_4H | ALT_ROTATION_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 1,72R | €17,16 |
| SHADOW_BTC_DONCHIAN_1H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 50,00% | 0,03 | -0,55R | €-10,91 |
| SHADOW_BTC_DONCHIAN_1H | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 0,58R | €5,81 |
| SHADOW_BTC_DONCHIAN_1H | RANGE | 0 | 6 | 6 | 16,67% | 0,18 | -0,77R | €-46,12 |
| SHADOW_BTC_DONCHIAN_1H | RANGE_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_DONCHIAN_1H | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -1,12R | €-11,25 |
| SHADOW_BTC_DONCHIAN_1H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_BTC_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_BTC_DONCHIAN_4H | ALT_ROTATION_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,77 |
| SHADOW_BTC_DONCHIAN_4H | ALT_ROTATION_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_DONCHIAN_4H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,64 |
| SHADOW_BTC_DONCHIAN_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,71 |
| SHADOW_BTC_EMA_1H | ALT_ROTATION_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_BTC_EMA_1H | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 0,52R | €5,16 |
| SHADOW_BTC_EMA_1H | RANGE | 0 | 4 | 4 | 50,00% | 1,16 | 0,09R | €3,64 |
| SHADOW_BTC_EMA_1H | RANGE_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_EMA_1H | TREND_DOWN | 0 | 2 | 2 | 50,00% | 0,32 | -0,38R | €-7,56 |
| SHADOW_BTC_EMA_1H | TREND_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,11R | €-22,22 |
| SHADOW_BTC_EMA_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,70 | 0,39R | €7,78 |
| SHADOW_BTC_EMA_4H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,64 |
| SHADOW_BTC_EMA_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,71 |
| SHADOW_COMBO_ADAPTIVE | ALT_ROTATION_DOWN | 0 | 46 | 46 | 26,09% | 0,62 | -0,24R | €-109,67 |
| SHADOW_COMBO_ADAPTIVE | ALT_ROTATION_UP | 0 | 54 | 54 | 37,04% | 1,11 | 0,05R | €29,40 |
| SHADOW_COMBO_ADAPTIVE | RANGE | 6 | 112 | 112 | 45,54% | 1,12 | 0,06R | €72,79 |
| SHADOW_COMBO_ADAPTIVE | RANGE_HIGH_VOL | 1 | 16 | 16 | 31,25% | 0,83 | -0,09R | €-14,08 |
| SHADOW_COMBO_ADAPTIVE | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE | TRANSITION | 0 | 53 | 53 | 41,51% | 1,41 | 0,21R | €113,40 |
| SHADOW_COMBO_ADAPTIVE | TREND_DOWN | 0 | 23 | 23 | 30,43% | 0,49 | -0,30R | €-68,69 |
| SHADOW_COMBO_ADAPTIVE | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,74R | €7,41 |
| SHADOW_COMBO_ADAPTIVE | TREND_UP | 2 | 92 | 92 | 36,96% | 1,12 | 0,05R | €48,94 |
| SHADOW_COMBO_ADAPTIVE | TREND_UP_HIGH_VOL | 0 | 17 | 17 | 17,65% | 0,46 | -0,41R | €-70,17 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 0 | 13 | 13 | 15,38% | 0,48 | -0,33R | €-42,51 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | ALT_ROTATION_UP | 0 | 48 | 48 | 37,50% | 1,15 | 0,08R | €36,41 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | RANGE | 1 | 60 | 60 | 48,33% | 1,19 | 0,10R | €57,84 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | RANGE_HIGH_VOL | 1 | 2 | 2 | 0,00% | 0,00 | -1,05R | €-21,08 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TRANSITION | 0 | 23 | 23 | 47,83% | 2,29 | 0,46R | €106,09 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_DOWN | 0 | 16 | 16 | 25,00% | 0,53 | -0,31R | €-48,86 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_UP | 1 | 53 | 53 | 28,30% | 0,61 | -0,19R | €-101,17 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_UP_HIGH_VOL | 0 | 10 | 10 | 10,00% | 0,23 | -0,66R | €-65,96 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | ALT_ROTATION_DOWN | 0 | 55 | 55 | 30,91% | 0,58 | -0,25R | €-135,11 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | ALT_ROTATION_UP | 0 | 60 | 60 | 41,67% | 1,02 | 0,01R | €6,58 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE | 3 | 110 | 110 | 44,55% | 1,35 | 0,15R | €159,94 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE_HIGH_VOL | 2 | 16 | 16 | 43,75% | 0,71 | -0,15R | €-24,54 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TRANSITION | 0 | 40 | 40 | 42,50% | 1,18 | 0,09R | €34,19 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_DOWN | 0 | 32 | 32 | 34,38% | 0,64 | -0,18R | €-56,64 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,85R | €8,53 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_UP | 2 | 94 | 94 | 51,06% | 1,33 | 0,14R | €128,70 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_UP_HIGH_VOL | 0 | 19 | 19 | 15,79% | 0,32 | -0,54R | €-102,85 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | ALT_ROTATION_DOWN | 0 | 46 | 46 | 26,09% | 0,65 | -0,22R | €-102,31 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | ALT_ROTATION_UP | 0 | 52 | 52 | 38,46% | 1,14 | 0,07R | €37,29 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | RANGE | 6 | 100 | 100 | 49,00% | 1,24 | 0,11R | €114,57 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | RANGE_HIGH_VOL | 1 | 14 | 14 | 42,86% | 1,15 | 0,07R | €9,49 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TRANSITION | 0 | 36 | 36 | 38,89% | 1,17 | 0,09R | €31,92 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_DOWN | 0 | 23 | 23 | 34,78% | 0,55 | -0,26R | €-60,33 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,05R | €10,47 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_UP | 2 | 71 | 71 | 38,03% | 0,74 | -0,12R | €-87,18 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_UP_HIGH_VOL | 0 | 12 | 12 | 25,00% | 0,41 | -0,47R | €-56,80 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TRANSITION | 0 | 13 | 13 | 30,77% | 1,08 | 0,05R | €5,95 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TREND_UP | 0 | 28 | 28 | 53,57% | 1,69 | 0,24R | €66,48 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,01R | €20,13 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TRANSITION | 0 | 13 | 13 | 30,77% | 1,08 | 0,05R | €5,95 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TREND_UP | 0 | 28 | 28 | 39,29% | 1,48 | 0,17R | €46,73 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 50,00% | 149,00 | 0,99R | €19,73 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | ALT_ROTATION_DOWN | 0 | 12 | 12 | 8,33% | 0,04 | -0,60R | €-71,62 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | ALT_ROTATION_UP | 0 | 17 | 17 | 23,53% | 0,44 | -0,34R | €-57,94 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | RANGE | 0 | 35 | 35 | 42,86% | 1,38 | 0,18R | €64,55 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | RANGE_HIGH_VOL | 0 | 6 | 6 | 16,67% | 0,65 | -0,18R | €-10,80 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TRANSITION | 0 | 12 | 12 | 33,33% | 1,27 | 0,14R | €16,81 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_DOWN | 0 | 12 | 12 | 33,33% | 0,75 | -0,15R | €-18,18 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_UP | 0 | 20 | 20 | 40,00% | 1,56 | 0,15R | €30,02 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 50,00% | 149,00 | 0,99R | €19,73 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TRANSITION | 0 | 47 | 47 | 38,30% | 1,09 | 0,05R | €22,80 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TREND_UP | 2 | 97 | 97 | 35,05% | 0,80 | -0,10R | €-92,96 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TREND_UP_HIGH_VOL | 0 | 13 | 13 | 15,38% | 0,36 | -0,53R | €-68,31 |
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
| SHADOW_COMBO_MEAN_REVERSION | ALT_ROTATION_DOWN | 0 | 11 | 11 | 27,27% | 0,42 | -0,30R | €-33,27 |
| SHADOW_COMBO_MEAN_REVERSION | ALT_ROTATION_UP | 0 | 4 | 4 | 75,00% | 4,11 | 0,85R | €33,98 |
| SHADOW_COMBO_MEAN_REVERSION | RANGE | 0 | 27 | 27 | 48,15% | 1,26 | 0,12R | €33,16 |
| SHADOW_COMBO_MEAN_REVERSION | RANGE_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -0,79R | €-23,63 |
| SHADOW_COMBO_MEAN_REVERSION | TRANSITION | 0 | 4 | 4 | 75,00% | 4,12 | 0,88R | €35,34 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_DOWN | 0 | 9 | 9 | 66,67% | 1,56 | 0,21R | €18,66 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_UP | 0 | 16 | 16 | 56,25% | 1,43 | 0,14R | €23,05 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,85 |
| SHADOW_COMBO_SCANNER | ALT_ROTATION_DOWN | 0 | 15 | 15 | 6,67% | 0,21 | -0,55R | €-82,64 |
| SHADOW_COMBO_SCANNER | ALT_ROTATION_UP | 0 | 46 | 46 | 39,13% | 1,21 | 0,12R | €54,43 |
| SHADOW_COMBO_SCANNER | RANGE | 1 | 66 | 66 | 45,45% | 1,51 | 0,25R | €165,84 |
| SHADOW_COMBO_SCANNER | RANGE_HIGH_VOL | 1 | 3 | 3 | 0,00% | 0,00 | -1,06R | €-31,76 |
| SHADOW_COMBO_SCANNER | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_SCANNER | TRANSITION | 0 | 38 | 38 | 47,37% | 1,73 | 0,34R | €129,44 |
| SHADOW_COMBO_SCANNER | TREND_DOWN | 0 | 16 | 16 | 18,75% | 0,52 | -0,31R | €-49,15 |
| SHADOW_COMBO_SCANNER | TREND_UP | 2 | 61 | 61 | 31,15% | 1,02 | 0,01R | €6,58 |
| SHADOW_COMBO_SCANNER | TREND_UP_HIGH_VOL | 0 | 13 | 13 | 23,08% | 0,74 | -0,17R | €-22,43 |
| SHADOW_COMBO_TREND | ALT_ROTATION_DOWN | 0 | 35 | 35 | 25,71% | 0,65 | -0,21R | €-73,73 |
| SHADOW_COMBO_TREND | ALT_ROTATION_UP | 0 | 47 | 47 | 31,91% | 0,87 | -0,08R | €-38,00 |
| SHADOW_COMBO_TREND | RANGE | 7 | 89 | 89 | 37,08% | 1,03 | 0,02R | €16,85 |
| SHADOW_COMBO_TREND | RANGE_HIGH_VOL | 3 | 10 | 10 | 20,00% | 0,51 | -0,26R | €-26,15 |
| SHADOW_COMBO_TREND | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_TREND | TRANSITION | 1 | 45 | 45 | 35,56% | 1,19 | 0,11R | €49,97 |
| SHADOW_COMBO_TREND | TREND_DOWN | 0 | 23 | 23 | 26,09% | 0,49 | -0,30R | €-68,62 |
| SHADOW_COMBO_TREND | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,57R | €5,70 |
| SHADOW_COMBO_TREND | TREND_UP | 2 | 70 | 70 | 30,00% | 1,03 | 0,01R | €10,31 |
| SHADOW_COMBO_TREND | TREND_UP_HIGH_VOL | 0 | 16 | 16 | 18,75% | 0,55 | -0,33R | €-52,46 |
| SHADOW_DOGE_BOLLINGER_1H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 50,00% | 1,22 | 0,13R | €2,52 |
| SHADOW_DOGE_BOLLINGER_1H | RANGE | 0 | 5 | 5 | 60,00% | 0,94 | -0,03R | €-1,46 |
| SHADOW_DOGE_DONCHIAN_1H | ALT_ROTATION_DOWN | 0 | 3 | 3 | 0,00% | 0,00 | -1,12R | €-33,50 |
| SHADOW_DOGE_DONCHIAN_1H | RANGE | 0 | 5 | 5 | 40,00% | 0,66 | -0,23R | €-11,31 |
| SHADOW_DOGE_DONCHIAN_1H | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,88R | €18,76 |
| SHADOW_DOGE_EMA_1H | ALT_ROTATION_DOWN | 0 | 6 | 6 | 0,00% | 0,00 | -0,75R | €-45,24 |
| SHADOW_DOGE_EMA_1H | RANGE | 0 | 7 | 7 | 42,86% | 0,98 | -0,01R | €-0,86 |
| SHADOW_DOGE_EMA_1H | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_DOGE_EMA_1H | TREND_DOWN | 0 | 2 | 2 | 50,00% | 0,41 | -0,33R | €-6,59 |
| SHADOW_DONCHIAN_1H | ALT_ROTATION_DOWN | 0 | 27 | 27 | 22,22% | 0,51 | -0,37R | €-98,95 |
| SHADOW_DONCHIAN_1H | ALT_ROTATION_UP | 1 | 18 | 18 | 16,67% | 0,18 | -0,67R | €-120,83 |
| SHADOW_DONCHIAN_1H | RANGE | 2 | 46 | 46 | 28,26% | 0,84 | -0,11R | €-50,23 |
| SHADOW_DONCHIAN_1H | RANGE_HIGH_VOL | 2 | 7 | 7 | 28,57% | 0,83 | -0,10R | €-6,83 |
| SHADOW_DONCHIAN_1H | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_DONCHIAN_1H | TRANSITION | 1 | 16 | 16 | 37,50% | 1,58 | 0,31R | €49,09 |
| SHADOW_DONCHIAN_1H | TREND_DOWN | 0 | 10 | 10 | 30,00% | 0,21 | -0,49R | €-49,11 |
| SHADOW_DONCHIAN_1H | TREND_UP | 3 | 37 | 37 | 29,73% | 1,09 | 0,05R | €19,00 |
| SHADOW_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 7 | 7 | 42,86% | 1,68 | 0,42R | €29,65 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | ALT_ROTATION_DOWN | 0 | 17 | 17 | 17,65% | 0,23 | -0,63R | €-107,43 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | ALT_ROTATION_UP | 1 | 10 | 10 | 20,00% | 0,04 | -0,70R | €-70,41 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | RANGE | 2 | 26 | 26 | 26,92% | 0,62 | -0,25R | €-65,29 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | RANGE_HIGH_VOL | 2 | 5 | 5 | 40,00% | 1,66 | 0,27R | €13,44 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | TRANSITION | 1 | 9 | 9 | 55,56% | 3,53 | 0,87R | €78,36 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | TREND_DOWN | 0 | 8 | 8 | 37,50% | 0,25 | -0,49R | €-38,82 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | TREND_UP | 3 | 23 | 23 | 26,09% | 0,92 | -0,03R | €-7,97 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 2,49R | €24,87 |
| SHADOW_EMA_TREND_1H | ALT_ROTATION_DOWN | 0 | 37 | 37 | 24,32% | 0,57 | -0,27R | €-100,46 |
| SHADOW_EMA_TREND_1H | ALT_ROTATION_UP | 0 | 46 | 46 | 30,43% | 0,80 | -0,13R | €-59,75 |
| SHADOW_EMA_TREND_1H | RANGE | 7 | 89 | 89 | 37,08% | 1,10 | 0,05R | €48,43 |
| SHADOW_EMA_TREND_1H | RANGE_HIGH_VOL | 3 | 11 | 11 | 27,27% | 1,00 | 0,00R | €0,11 |
| SHADOW_EMA_TREND_1H | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_EMA_TREND_1H | TRANSITION | 1 | 44 | 44 | 34,09% | 1,11 | 0,07R | €29,96 |
| SHADOW_EMA_TREND_1H | TREND_DOWN | 0 | 24 | 24 | 29,17% | 0,51 | -0,28R | €-66,86 |
| SHADOW_EMA_TREND_1H | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,08R | €-10,84 |
| SHADOW_EMA_TREND_1H | TREND_UP | 1 | 74 | 74 | 28,38% | 0,95 | -0,03R | €-20,43 |
| SHADOW_EMA_TREND_1H | TREND_UP_HIGH_VOL | 0 | 16 | 16 | 18,75% | 0,55 | -0,33R | €-53,00 |
| SHADOW_ETH_ADAPTIVE_1H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 0,00% | 0,00 | -1,11R | €-22,22 |
| SHADOW_ETH_ADAPTIVE_1H | ALT_ROTATION_UP | 0 | 3 | 3 | 33,33% | 0,15 | -0,63R | €-18,84 |
| SHADOW_ETH_ADAPTIVE_1H | RANGE | 0 | 3 | 3 | 33,33% | 0,26 | -0,55R | €-16,36 |
| SHADOW_ETH_ADAPTIVE_1H | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 0,50R | €5,03 |
| SHADOW_ETH_ADAPTIVE_1H | TREND_UP | 0 | 2 | 2 | 50,00% | 1,71 | 0,39R | €7,82 |
| SHADOW_ETH_ADAPTIVE_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_ETH_BOLLINGER_1H | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,37R | €13,67 |
| SHADOW_ETH_BOLLINGER_1H | RANGE | 0 | 1 | 1 | 100,00% | ∞ | 0,11R | €1,10 |
| SHADOW_ETH_BOLLINGER_1H | TREND_DOWN | 0 | 2 | 2 | 50,00% | 1,21 | 0,12R | €2,33 |
| SHADOW_ETH_BOLLINGER_1H | TREND_UP | 0 | 2 | 2 | 50,00% | 0,41 | -0,33R | €-6,68 |
| SHADOW_ETH_DONCHIAN_1H | ALT_ROTATION_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,13R | €-22,50 |
| SHADOW_ETH_DONCHIAN_1H | RANGE | 0 | 4 | 4 | 25,00% | 0,20 | -0,68R | €-27,16 |
| SHADOW_ETH_DONCHIAN_1H | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 0,57R | €5,66 |
| SHADOW_ETH_DONCHIAN_1H | TREND_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,13R | €-22,50 |
| SHADOW_ETH_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,68 | 0,38R | €7,64 |
| SHADOW_ETH_EMA_1H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 0,00% | 0,00 | -1,11R | €-22,22 |
| SHADOW_ETH_EMA_1H | ALT_ROTATION_UP | 0 | 3 | 3 | 33,33% | 0,12 | -0,65R | €-19,52 |
| SHADOW_ETH_EMA_1H | RANGE | 0 | 5 | 5 | 40,00% | 0,31 | -0,46R | €-23,07 |
| SHADOW_ETH_EMA_1H | TRANSITION | 0 | 2 | 2 | 50,00% | 0,45 | -0,30R | €-6,08 |
| SHADOW_ETH_EMA_1H | TREND_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 0,84R | €8,38 |
| SHADOW_ETH_EMA_1H | TREND_UP | 0 | 3 | 3 | 33,33% | 0,85 | -0,11R | €-3,33 |
| SHADOW_ETH_EMA_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,10R | €-10,99 |
| SHADOW_ETH_EMA_4H | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,67 |
| SHADOW_ETH_EMA_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,57 |
| SHADOW_GLOBAL_PURE | ALT_ROTATION_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,10R | €-22,00 |
| SHADOW_GLOBAL_PURE | RANGE | 0 | 4 | 4 | 50,00% | 1,36 | 0,20R | €7,90 |
| SHADOW_GLOBAL_PURE | TRANSITION | 0 | 3 | 3 | 66,67% | 3,47 | 0,91R | €27,19 |
| SHADOW_GLOBAL_PURE | TREND_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 0,02R | €0,21 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | ALT_ROTATION_DOWN | 0 | 16 | 16 | 25,00% | 0,69 | -0,22R | €-35,19 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | ALT_ROTATION_UP | 1 | 28 | 28 | 32,14% | 0,90 | -0,07R | €-20,48 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | RANGE | 4 | 61 | 61 | 31,15% | 0,97 | -0,02R | €-10,48 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TRANSITION | 0 | 16 | 16 | 50,00% | 2,19 | 0,53R | €85,35 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TREND_DOWN | 0 | 22 | 22 | 40,91% | 1,55 | 0,28R | €62,57 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TREND_UP | 0 | 59 | 59 | 28,81% | 0,83 | -0,12R | €-69,67 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | ALT_ROTATION_DOWN | 0 | 18 | 18 | 44,44% | 0,85 | -0,08R | €-14,12 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | ALT_ROTATION_UP | 1 | 65 | 65 | 76,92% | 2,21 | 0,29R | €188,84 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | RANGE | 1 | 119 | 119 | 67,23% | 1,57 | 0,17R | €204,45 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TRANSITION | 0 | 34 | 34 | 67,65% | 1,36 | 0,11R | €36,89 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TREND_DOWN | 0 | 33 | 33 | 63,64% | 1,33 | 0,11R | €37,35 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TREND_UP | 1 | 107 | 107 | 62,62% | 1,08 | 0,03R | €31,42 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | ALT_ROTATION_DOWN | 1 | 13 | 13 | 23,08% | 0,64 | -0,26R | €-33,81 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | RANGE | 3 | 62 | 62 | 35,48% | 1,19 | 0,11R | €68,26 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | RANGE_LOW_VOL | 0 | 2 | 2 | 50,00% | 1,86 | 0,44R | €8,76 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TRANSITION | 0 | 15 | 15 | 33,33% | 1,07 | 0,04R | €6,42 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TREND_DOWN | 0 | 20 | 20 | 40,00% | 1,39 | 0,22R | €44,20 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TREND_UP | 0 | 66 | 66 | 28,79% | 0,82 | -0,12R | €-82,14 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_DOWN | 0 | 9 | 9 | 33,33% | 1,36 | 0,21R | €18,74 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_UP | 1 | 31 | 31 | 25,81% | 0,68 | -0,25R | €-78,29 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | RANGE | 3 | 56 | 56 | 32,14% | 1,21 | 0,13R | €71,58 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | TRANSITION | 0 | 13 | 13 | 38,46% | 1,42 | 0,23R | €30,22 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | TREND_DOWN | 0 | 18 | 18 | 44,44% | 1,71 | 0,37R | €66,49 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | TREND_UP | 0 | 57 | 57 | 24,56% | 0,70 | -0,22R | €-125,02 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | ALT_ROTATION_DOWN | 1 | 7 | 7 | 0,00% | 0,00 | -1,02R | €-71,71 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | RANGE | 2 | 52 | 52 | 34,62% | 1,04 | 0,03R | €14,21 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TRANSITION | 0 | 12 | 12 | 41,67% | 1,89 | 0,39R | €46,35 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TREND_DOWN | 0 | 13 | 13 | 23,08% | 0,65 | -0,25R | €-32,52 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TREND_UP | 0 | 46 | 46 | 32,61% | 0,99 | -0,00R | €-1,69 |
| SHADOW_MASTER_ADAPTIVE_V1 | ALT_ROTATION_DOWN | 0 | 14 | 14 | 21,43% | 0,57 | -0,31R | €-43,94 |
| SHADOW_MASTER_ADAPTIVE_V1 | ALT_ROTATION_UP | 1 | 30 | 30 | 33,33% | 0,94 | -0,04R | €-12,77 |
| SHADOW_MASTER_ADAPTIVE_V1 | RANGE | 3 | 59 | 59 | 35,59% | 1,21 | 0,12R | €70,76 |
| SHADOW_MASTER_ADAPTIVE_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_MASTER_ADAPTIVE_V1 | TRANSITION | 0 | 15 | 15 | 40,00% | 1,44 | 0,24R | €36,39 |
| SHADOW_MASTER_ADAPTIVE_V1 | TREND_DOWN | 0 | 19 | 19 | 42,11% | 1,52 | 0,29R | €54,33 |
| SHADOW_MASTER_ADAPTIVE_V1 | TREND_UP | 0 | 60 | 60 | 25,00% | 0,68 | -0,23R | €-139,80 |
| Forza relativa 1H V1 | ALT_ROTATION_DOWN | 0 | 46 | 46 | 19,57% | 0,44 | -0,37R | €-168,98 |
| Forza relativa 1H V1 | ALT_ROTATION_UP | 0 | 56 | 56 | 33,93% | 0,94 | -0,04R | €-20,37 |
| Forza relativa 1H V1 | RANGE | 7 | 124 | 124 | 33,87% | 0,94 | -0,04R | €-43,70 |
| Forza relativa 1H V1 | RANGE_HIGH_VOL | 2 | 12 | 12 | 8,33% | 0,30 | -0,43R | €-51,78 |
| Forza relativa 1H V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| Forza relativa 1H V1 | TRANSITION | 0 | 51 | 51 | 39,22% | 1,35 | 0,18R | €92,51 |
| Forza relativa 1H V1 | TREND_DOWN | 0 | 26 | 26 | 26,92% | 0,75 | -0,14R | €-36,21 |
| Forza relativa 1H V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 100,00% | ∞ | 1,41R | €28,20 |
| Forza relativa 1H V1 | TREND_UP | 3 | 92 | 92 | 26,09% | 0,91 | -0,05R | €-44,68 |
| Forza relativa 1H V1 | TREND_UP_HIGH_VOL | 0 | 15 | 15 | 13,33% | 0,38 | -0,47R | €-70,88 |
| Forza relativa 1H V2 | ALT_ROTATION_DOWN | 0 | 20 | 20 | 25,00% | 0,64 | -0,21R | €-41,24 |
| Forza relativa 1H V2 | ALT_ROTATION_UP | 0 | 26 | 23 | 38,46% | 1,35 | 0,18R | €47,67 |
| Forza relativa 1H V2 | RANGE | 4 | 54 | 53 | 35,19% | 0,98 | -0,01R | €-7,34 |
| Forza relativa 1H V2 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -0,01R | €-0,13 |
| Forza relativa 1H V2 | TRANSITION | 0 | 28 | 24 | 42,86% | 1,83 | 0,37R | €103,63 |
| Forza relativa 1H V2 | TREND_DOWN | 0 | 13 | 12 | 30,77% | 1,03 | 0,02R | €1,95 |
| Forza relativa 1H V2 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,63 | -0,19R | €-3,80 |
| Forza relativa 1H V2 | TREND_UP | 1 | 35 | 32 | 45,71% | 1,70 | 0,33R | €116,73 |
| Forza relativa 1H V2 | TREND_UP_HIGH_VOL | 0 | 6 | 5 | 0,00% | 0,00 | -0,86R | €-51,87 |
| SHADOW_SCANNER_BOTTOM10_SHORT | ALT_ROTATION_DOWN | 0 | 29 | 29 | 13,79% | 0,17 | -0,62R | €-180,83 |
| SHADOW_SCANNER_BOTTOM10_SHORT | ALT_ROTATION_UP | 1 | 5 | 5 | 40,00% | 0,94 | -0,03R | €-1,39 |
| SHADOW_SCANNER_BOTTOM10_SHORT | RANGE | 4 | 35 | 35 | 31,43% | 0,54 | -0,26R | €-90,54 |
| SHADOW_SCANNER_BOTTOM10_SHORT | RANGE_HIGH_VOL | 1 | 11 | 11 | 27,27% | 1,14 | 0,07R | €7,16 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TRANSITION | 0 | 15 | 15 | 46,67% | 1,08 | 0,05R | €6,96 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_DOWN | 0 | 16 | 16 | 43,75% | 0,71 | -0,14R | €-21,73 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,63 | -0,20R | €-4,07 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_UP | 2 | 14 | 14 | 7,14% | 0,29 | -0,33R | €-45,57 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| SHADOW_SCANNER_BOTTOM15_SHORT | ALT_ROTATION_DOWN | 0 | 29 | 29 | 13,79% | 0,17 | -0,62R | €-180,83 |
| SHADOW_SCANNER_BOTTOM15_SHORT | ALT_ROTATION_UP | 1 | 5 | 5 | 40,00% | 0,94 | -0,03R | €-1,39 |
| SHADOW_SCANNER_BOTTOM15_SHORT | RANGE | 4 | 35 | 35 | 31,43% | 0,54 | -0,26R | €-90,54 |
| SHADOW_SCANNER_BOTTOM15_SHORT | RANGE_HIGH_VOL | 1 | 11 | 11 | 27,27% | 1,14 | 0,07R | €7,16 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TRANSITION | 0 | 15 | 15 | 46,67% | 1,08 | 0,05R | €6,96 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_DOWN | 0 | 16 | 16 | 43,75% | 0,71 | -0,14R | €-21,73 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,63 | -0,20R | €-4,07 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_UP | 2 | 14 | 14 | 7,14% | 0,29 | -0,33R | €-45,57 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| SHADOW_SCANNER_BOTTOM20_SHORT | ALT_ROTATION_DOWN | 0 | 29 | 29 | 13,79% | 0,17 | -0,62R | €-180,83 |
| SHADOW_SCANNER_BOTTOM20_SHORT | ALT_ROTATION_UP | 1 | 5 | 5 | 40,00% | 0,94 | -0,03R | €-1,39 |
| SHADOW_SCANNER_BOTTOM20_SHORT | RANGE | 4 | 35 | 35 | 31,43% | 0,54 | -0,26R | €-90,54 |
| SHADOW_SCANNER_BOTTOM20_SHORT | RANGE_HIGH_VOL | 1 | 11 | 11 | 27,27% | 1,14 | 0,07R | €7,16 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TRANSITION | 0 | 15 | 15 | 46,67% | 1,08 | 0,05R | €6,96 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_DOWN | 0 | 16 | 16 | 43,75% | 0,71 | -0,14R | €-21,73 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,63 | -0,20R | €-4,07 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_UP | 2 | 14 | 14 | 7,14% | 0,29 | -0,33R | €-45,57 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| SHADOW_SCANNER_BOTTOM5_SHORT | ALT_ROTATION_DOWN | 0 | 25 | 25 | 24,00% | 0,65 | -0,22R | €-56,17 |
| SHADOW_SCANNER_BOTTOM5_SHORT | ALT_ROTATION_UP | 1 | 6 | 6 | 50,00% | 1,83 | 0,31R | €18,48 |
| SHADOW_SCANNER_BOTTOM5_SHORT | RANGE | 3 | 49 | 49 | 36,73% | 0,92 | -0,04R | €-21,61 |
| SHADOW_SCANNER_BOTTOM5_SHORT | RANGE_HIGH_VOL | 1 | 12 | 12 | 33,33% | 1,29 | 0,12R | €14,60 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TRANSITION | 0 | 30 | 30 | 40,00% | 1,00 | -0,00R | €-0,64 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_DOWN | 0 | 14 | 14 | 42,86% | 0,66 | -0,16R | €-22,16 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,62 | -0,21R | €-4,24 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP | 2 | 21 | 21 | 4,76% | 0,16 | -0,46R | €-96,61 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 25,00% | 0,93 | -0,04R | €-1,51 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | ALT_ROTATION_DOWN | 0 | 27 | 27 | 29,63% | 0,29 | -0,48R | €-128,52 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | ALT_ROTATION_UP | 0 | 3 | 3 | 33,33% | 0,85 | -0,06R | €-1,73 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | RANGE | 2 | 40 | 40 | 60,00% | 0,89 | -0,04R | €-16,25 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | RANGE_HIGH_VOL | 1 | 15 | 15 | 66,67% | 1,55 | 0,19R | €28,00 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TRANSITION | 0 | 18 | 18 | 61,11% | 1,52 | 0,22R | €38,86 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_DOWN | 0 | 24 | 24 | 41,67% | 0,58 | -0,21R | €-49,35 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,77 | -0,13R | €-2,58 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_UP | 2 | 17 | 17 | 47,06% | 0,65 | -0,17R | €-29,22 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,19R | €1,87 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | ALT_ROTATION_DOWN | 0 | 24 | 24 | 29,17% | 0,22 | -0,52R | €-124,34 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | ALT_ROTATION_UP | 1 | 4 | 4 | 50,00% | 1,86 | 0,24R | €9,72 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | RANGE | 2 | 32 | 32 | 62,50% | 0,76 | -0,08R | €-26,08 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | RANGE_HIGH_VOL | 1 | 12 | 12 | 58,33% | 1,41 | 0,17R | €20,60 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TRANSITION | 0 | 17 | 17 | 58,82% | 1,59 | 0,26R | €43,88 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_DOWN | 0 | 18 | 18 | 38,89% | 0,65 | -0,17R | €-30,22 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,62 | -0,21R | €-4,24 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_UP | 2 | 16 | 16 | 43,75% | 0,34 | -0,35R | €-55,38 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,19R | €1,87 |
| SHADOW_SCANNER_TOP10_LONG | ALT_ROTATION_DOWN | 0 | 9 | 9 | 22,22% | 0,77 | -0,13R | €-11,96 |
| SHADOW_SCANNER_TOP10_LONG | ALT_ROTATION_UP | 0 | 44 | 44 | 34,09% | 1,01 | 0,00R | €2,00 |
| SHADOW_SCANNER_TOP10_LONG | RANGE | 1 | 49 | 49 | 48,98% | 1,48 | 0,21R | €104,22 |
| SHADOW_SCANNER_TOP10_LONG | RANGE_HIGH_VOL | 1 | 2 | 2 | 0,00% | 0,00 | -1,05R | €-21,06 |
| SHADOW_SCANNER_TOP10_LONG | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP10_LONG | TRANSITION | 0 | 24 | 24 | 45,83% | 1,91 | 0,35R | €83,82 |
| SHADOW_SCANNER_TOP10_LONG | TREND_DOWN | 0 | 16 | 16 | 18,75% | 0,58 | -0,27R | €-43,36 |
| SHADOW_SCANNER_TOP10_LONG | TREND_UP | 2 | 46 | 46 | 28,26% | 0,58 | -0,21R | €-94,48 |
| SHADOW_SCANNER_TOP10_LONG | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 0,00% | 0,00 | -0,81R | €-32,31 |
| SHADOW_SCANNER_TOP15_LONG | ALT_ROTATION_DOWN | 0 | 9 | 9 | 22,22% | 0,77 | -0,13R | €-11,96 |
| SHADOW_SCANNER_TOP15_LONG | ALT_ROTATION_UP | 0 | 45 | 45 | 33,33% | 0,96 | -0,02R | €-9,11 |
| SHADOW_SCANNER_TOP15_LONG | RANGE | 1 | 49 | 49 | 48,98% | 1,48 | 0,21R | €104,22 |
| SHADOW_SCANNER_TOP15_LONG | RANGE_HIGH_VOL | 1 | 2 | 2 | 0,00% | 0,00 | -1,05R | €-21,06 |
| SHADOW_SCANNER_TOP15_LONG | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP15_LONG | TRANSITION | 0 | 24 | 24 | 45,83% | 1,91 | 0,35R | €83,82 |
| SHADOW_SCANNER_TOP15_LONG | TREND_DOWN | 0 | 16 | 16 | 18,75% | 0,58 | -0,27R | €-43,36 |
| SHADOW_SCANNER_TOP15_LONG | TREND_UP | 2 | 46 | 46 | 28,26% | 0,58 | -0,21R | €-94,48 |
| SHADOW_SCANNER_TOP15_LONG | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 0,00% | 0,00 | -0,81R | €-32,31 |
| SHADOW_SCANNER_TOP20_LONG | ALT_ROTATION_DOWN | 0 | 9 | 9 | 22,22% | 0,77 | -0,13R | €-11,96 |
| SHADOW_SCANNER_TOP20_LONG | ALT_ROTATION_UP | 0 | 45 | 45 | 33,33% | 0,96 | -0,02R | €-9,11 |
| SHADOW_SCANNER_TOP20_LONG | RANGE | 1 | 49 | 49 | 48,98% | 1,48 | 0,21R | €104,22 |
| SHADOW_SCANNER_TOP20_LONG | RANGE_HIGH_VOL | 1 | 2 | 2 | 0,00% | 0,00 | -1,05R | €-21,06 |
| SHADOW_SCANNER_TOP20_LONG | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP20_LONG | TRANSITION | 0 | 24 | 24 | 45,83% | 1,91 | 0,35R | €83,82 |
| SHADOW_SCANNER_TOP20_LONG | TREND_DOWN | 0 | 16 | 16 | 18,75% | 0,58 | -0,27R | €-43,36 |
| SHADOW_SCANNER_TOP20_LONG | TREND_UP | 2 | 46 | 46 | 28,26% | 0,58 | -0,21R | €-94,48 |
| SHADOW_SCANNER_TOP20_LONG | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 0,00% | 0,00 | -0,81R | €-32,31 |
| SHADOW_SCANNER_TOP5_BTC | ALT_ROTATION_DOWN | 0 | 14 | 14 | 7,14% | 0,23 | -0,51R | €-71,62 |
| SHADOW_SCANNER_TOP5_BTC | ALT_ROTATION_UP | 0 | 46 | 46 | 39,13% | 1,22 | 0,12R | €55,01 |
| SHADOW_SCANNER_TOP5_BTC | RANGE | 1 | 63 | 63 | 44,44% | 1,59 | 0,28R | €176,61 |
| SHADOW_SCANNER_TOP5_BTC | RANGE_HIGH_VOL | 1 | 3 | 3 | 0,00% | 0,00 | -1,06R | €-31,76 |
| SHADOW_SCANNER_TOP5_BTC | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC | TRANSITION | 0 | 34 | 34 | 47,06% | 1,82 | 0,37R | €127,02 |
| SHADOW_SCANNER_TOP5_BTC | TREND_DOWN | 0 | 16 | 16 | 18,75% | 0,52 | -0,31R | €-49,15 |
| SHADOW_SCANNER_TOP5_BTC | TREND_UP | 2 | 60 | 60 | 30,00% | 0,96 | -0,02R | €-14,13 |
| SHADOW_SCANNER_TOP5_BTC | TREND_UP_HIGH_VOL | 0 | 13 | 13 | 23,08% | 0,74 | -0,17R | €-22,43 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | ALT_ROTATION_DOWN | 0 | 5 | 5 | 0,00% | 0,00 | -0,64R | €-31,86 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | ALT_ROTATION_UP | 0 | 37 | 37 | 37,84% | 0,97 | -0,02R | €-5,77 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | RANGE | 0 | 5 | 5 | 20,00% | 0,10 | -0,75R | €-37,70 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TRANSITION | 0 | 21 | 21 | 47,62% | 2,16 | 0,45R | €95,41 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TREND_UP | 1 | 46 | 46 | 28,26% | 0,81 | -0,10R | €-46,56 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TREND_UP_HIGH_VOL | 0 | 10 | 10 | 10,00% | 0,25 | -0,64R | €-64,24 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | ALT_ROTATION_DOWN | 0 | 12 | 12 | 0,00% | 0,00 | -0,77R | €-92,81 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | ALT_ROTATION_UP | 0 | 43 | 43 | 39,53% | 1,15 | 0,08R | €34,14 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | RANGE | 1 | 58 | 58 | 43,10% | 1,43 | 0,21R | €123,37 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | RANGE_HIGH_VOL | 1 | 2 | 2 | 0,00% | 0,00 | -1,05R | €-21,06 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TRANSITION | 0 | 22 | 22 | 54,55% | 2,71 | 0,56R | €122,84 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_DOWN | 0 | 16 | 16 | 18,75% | 0,52 | -0,31R | €-49,15 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_UP | 1 | 40 | 40 | 20,00% | 0,46 | -0,32R | €-126,23 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_UP_HIGH_VOL | 0 | 10 | 10 | 10,00% | 0,25 | -0,64R | €-64,24 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | ALT_ROTATION_DOWN | 0 | 11 | 11 | 9,09% | 0,04 | -0,54R | €-59,83 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | ALT_ROTATION_UP | 0 | 36 | 36 | 50,00% | 1,41 | 0,18R | €63,95 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | RANGE | 0 | 72 | 72 | 45,83% | 1,39 | 0,16R | €113,74 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | RANGE_HIGH_VOL | 2 | 2 | 2 | 0,00% | 0,00 | -1,05R | €-21,06 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TRANSITION | 0 | 22 | 22 | 50,00% | 1,79 | 0,30R | €65,30 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_DOWN | 0 | 18 | 18 | 38,89% | 0,66 | -0,19R | €-35,03 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_UP | 0 | 45 | 45 | 51,11% | 1,28 | 0,12R | €53,08 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 25,00% | 0,30 | -0,53R | €-21,15 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | ALT_ROTATION_DOWN | 0 | 11 | 11 | 0,00% | 0,00 | -0,75R | €-82,68 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | ALT_ROTATION_UP | 0 | 31 | 31 | 41,94% | 1,49 | 0,25R | €75,99 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | RANGE | 1 | 61 | 61 | 45,90% | 1,53 | 0,25R | €154,57 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | RANGE_HIGH_VOL | 1 | 2 | 2 | 0,00% | 0,00 | -1,05R | €-21,06 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TRANSITION | 0 | 20 | 20 | 45,00% | 2,15 | 0,42R | €83,46 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_DOWN | 0 | 14 | 14 | 21,43% | 0,53 | -0,34R | €-47,76 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_UP | 0 | 34 | 34 | 20,59% | 0,55 | -0,25R | €-84,74 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 0,00% | 0,00 | -0,76R | €-30,53 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | ALT_ROTATION_DOWN | 0 | 15 | 15 | 26,67% | 0,54 | -0,25R | €-38,04 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | ALT_ROTATION_UP | 0 | 36 | 36 | 50,00% | 1,41 | 0,18R | €63,95 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | RANGE | 0 | 72 | 72 | 45,83% | 1,39 | 0,16R | €113,74 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | RANGE_HIGH_VOL | 2 | 2 | 2 | 0,00% | 0,00 | -1,05R | €-21,06 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TRANSITION | 0 | 24 | 24 | 45,83% | 1,59 | 0,23R | €55,04 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_DOWN | 0 | 18 | 18 | 38,89% | 0,66 | -0,19R | €-35,03 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_UP | 1 | 49 | 49 | 48,98% | 1,25 | 0,11R | €52,98 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 25,00% | 0,30 | -0,53R | €-21,15 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | ALT_ROTATION_DOWN | 0 | 13 | 13 | 7,69% | 0,26 | -0,47R | €-61,49 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | ALT_ROTATION_UP | 0 | 31 | 31 | 41,94% | 1,49 | 0,25R | €75,99 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | RANGE | 1 | 61 | 61 | 45,90% | 1,53 | 0,25R | €154,57 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | RANGE_HIGH_VOL | 1 | 2 | 2 | 0,00% | 0,00 | -1,05R | €-21,06 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TRANSITION | 0 | 21 | 21 | 42,86% | 1,89 | 0,35R | €73,32 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_DOWN | 0 | 14 | 14 | 21,43% | 0,53 | -0,34R | €-47,76 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_UP | 1 | 38 | 38 | 21,05% | 0,59 | -0,22R | €-84,84 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 0,00% | 0,00 | -0,76R | €-30,53 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | ALT_ROTATION_DOWN | 0 | 16 | 16 | 25,00% | 0,48 | -0,30R | €-48,17 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | ALT_ROTATION_UP | 0 | 47 | 47 | 44,68% | 1,06 | 0,03R | €14,19 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | RANGE | 0 | 67 | 67 | 46,27% | 1,37 | 0,15R | €103,33 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | RANGE_HIGH_VOL | 2 | 2 | 2 | 0,00% | 0,00 | -1,05R | €-21,06 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TRANSITION | 0 | 28 | 28 | 46,43% | 1,48 | 0,20R | €55,10 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_DOWN | 0 | 21 | 21 | 33,33% | 0,58 | -0,23R | €-47,25 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_UP | 2 | 59 | 59 | 49,15% | 1,26 | 0,10R | €61,85 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 13 | 13 | 23,08% | 0,53 | -0,35R | €-45,65 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | ALT_ROTATION_DOWN | 0 | 7 | 7 | 14,29% | 0,51 | -0,29R | €-20,19 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | ALT_ROTATION_UP | 0 | 47 | 47 | 36,17% | 1,16 | 0,09R | €42,67 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | RANGE | 0 | 55 | 55 | 41,82% | 1,46 | 0,23R | €127,42 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | RANGE_HIGH_VOL | 1 | 2 | 2 | 0,00% | 0,00 | -1,05R | €-21,06 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TRANSITION | 1 | 21 | 21 | 47,62% | 1,94 | 0,37R | €76,97 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_DOWN | 0 | 16 | 16 | 18,75% | 0,54 | -0,30R | €-47,64 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_UP | 2 | 44 | 44 | 20,45% | 0,51 | -0,28R | €-125,08 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_UP_HIGH_VOL | 0 | 7 | 7 | 0,00% | 0,00 | -0,91R | €-63,69 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | ALT_ROTATION_DOWN | 0 | 7 | 7 | 0,00% | 0,00 | -0,60R | €-41,69 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | ALT_ROTATION_UP | 0 | 47 | 47 | 38,30% | 1,11 | 0,06R | €27,77 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | RANGE | 0 | 51 | 51 | 41,18% | 1,51 | 0,27R | €136,48 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | RANGE_HIGH_VOL | 1 | 2 | 2 | 0,00% | 0,00 | -1,05R | €-21,06 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TRANSITION | 1 | 17 | 17 | 47,06% | 2,69 | 0,51R | €87,51 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_DOWN | 0 | 15 | 15 | 20,00% | 0,61 | -0,24R | €-35,84 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_UP | 2 | 43 | 43 | 20,93% | 0,54 | -0,26R | €-112,40 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_UP_HIGH_VOL | 0 | 7 | 7 | 0,00% | 0,00 | -0,91R | €-63,69 |
| SHADOW_SCANNER_TOP5_LONG | ALT_ROTATION_DOWN | 0 | 16 | 16 | 12,50% | 0,35 | -0,47R | €-74,87 |
| SHADOW_SCANNER_TOP5_LONG | ALT_ROTATION_UP | 0 | 47 | 47 | 36,17% | 1,08 | 0,04R | €19,68 |
| SHADOW_SCANNER_TOP5_LONG | RANGE | 1 | 64 | 64 | 48,44% | 1,60 | 0,27R | €174,75 |
| SHADOW_SCANNER_TOP5_LONG | RANGE_HIGH_VOL | 1 | 4 | 4 | 0,00% | 0,00 | -1,05R | €-41,89 |
| SHADOW_SCANNER_TOP5_LONG | RANGE_LOW_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_LONG | TRANSITION | 0 | 37 | 37 | 45,95% | 1,78 | 0,35R | €129,86 |
| SHADOW_SCANNER_TOP5_LONG | TREND_DOWN | 0 | 16 | 16 | 18,75% | 0,58 | -0,27R | €-43,36 |
| SHADOW_SCANNER_TOP5_LONG | TREND_UP | 2 | 76 | 76 | 35,53% | 1,08 | 0,04R | €29,95 |
| SHADOW_SCANNER_TOP5_LONG | TREND_UP_HIGH_VOL | 0 | 13 | 13 | 23,08% | 0,67 | -0,22R | €-28,93 |
| SHADOW_SOL_ADAPTIVE_1H | ALT_ROTATION_DOWN | 0 | 5 | 5 | 0,00% | 0,00 | -1,10R | €-55,07 |
| SHADOW_SOL_ADAPTIVE_1H | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 0,94R | €9,38 |
| SHADOW_SOL_ADAPTIVE_1H | RANGE | 1 | 6 | 6 | 33,33% | 0,51 | -0,36R | €-21,78 |
| SHADOW_SOL_ADAPTIVE_1H | TRANSITION | 0 | 2 | 2 | 50,00% | 1,70 | 0,39R | €7,78 |
| SHADOW_SOL_ADAPTIVE_1H | TREND_UP | 0 | 2 | 2 | 50,00% | 1,11 | 0,06R | €1,19 |
| SHADOW_SOL_ADAPTIVE_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,10R | €-22,07 |
| SHADOW_SOL_ADAPTIVE_4H | RANGE | 0 | 1 | 1 | 100,00% | ∞ | 1,25R | €12,45 |
| SHADOW_SOL_ADAPTIVE_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,05R | €-10,52 |
| SHADOW_SOL_BOLLINGER_1H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 100,00% | ∞ | 0,31R | €6,19 |
| SHADOW_SOL_BOLLINGER_1H | ALT_ROTATION_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,13R | €-22,67 |
| SHADOW_SOL_BOLLINGER_1H | RANGE | 0 | 5 | 5 | 40,00% | 0,80 | -0,13R | €-6,67 |
| SHADOW_SOL_BOLLINGER_1H | TREND_UP | 0 | 2 | 2 | 50,00% | 0,71 | -0,16R | €-3,29 |
| SHADOW_SOL_BOLLINGER_4H | RANGE | 0 | 1 | 1 | 100,00% | ∞ | 0,66R | €6,63 |
| SHADOW_SOL_BOLLINGER_4H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,74R | €17,38 |
| SHADOW_SOL_DONCHIAN_1H | ALT_ROTATION_DOWN | 0 | 4 | 4 | 0,00% | 0,00 | -1,11R | €-44,59 |
| SHADOW_SOL_DONCHIAN_1H | RANGE | 1 | 4 | 4 | 75,00% | 3,71 | 0,76R | €30,50 |
| SHADOW_SOL_DONCHIAN_1H | TREND_UP | 0 | 2 | 2 | 50,00% | 1,67 | 0,38R | €7,50 |
| SHADOW_SOL_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,08 |
| SHADOW_SOL_DONCHIAN_4H | RANGE | 0 | 1 | 1 | 100,00% | ∞ | 1,36R | €13,58 |
| SHADOW_SOL_DONCHIAN_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,56 |
| SHADOW_SOL_EMA_1H | ALT_ROTATION_DOWN | 0 | 4 | 4 | 0,00% | 0,00 | -1,10R | €-43,99 |
| SHADOW_SOL_EMA_1H | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 0,94R | €9,38 |
| SHADOW_SOL_EMA_1H | RANGE | 1 | 6 | 6 | 33,33% | 0,85 | -0,11R | €-6,67 |
| SHADOW_SOL_EMA_1H | TRANSITION | 0 | 2 | 2 | 50,00% | 1,70 | 0,39R | €7,78 |
| SHADOW_SOL_EMA_1H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_SOL_EMA_1H | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,23R | €12,30 |
| SHADOW_SOL_EMA_1H | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,10R | €-22,07 |
| SHADOW_SOL_EMA_4H | ALT_ROTATION_DOWN | 0 | 2 | 2 | 0,00% | 0,00 | -1,05R | €-21,06 |
| SHADOW_SOL_EMA_4H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,56 |

Il P&L è normalizzato a **€10 di rischio per evento**, così leva e size non falsano il confronto.
La matrice diventerà utilizzabile per una rotazione automatica soltanto dopo un campione sufficiente per ciascuna coppia strategia-regime.

# Block 3 — Shadow Exit Engine

Generato: 2026-08-11T15:40:04+00:00

> Motore esclusivamente osservativo e Paper-only. Non modifica le uscite reali. I confronti escludono il funding sia dall'uscita originale sia dalle varianti.

## Stato operativo

- Gruppi di trade ancora monitorati: **345**
- Scenari virtuali ancora attivi: **10467**
- Gruppi in attesa dell'uscita originale: **240**
- Gruppi con originale chiuso ma Shadow ancora attive: **105**
- Confronti completati: **136866**

## Classifica osservativa complessiva

| Scenario | Campione completo | Campione totale | Δ medio vs originale | Migliora | Troppo presto | Troppo tardi | Stato dati |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| GB20_R050 | 3583 | 3649 | +€7,88 | 50,7% | 1002 | 13 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R050 | 3583 | 3649 | +€6,75 | 49,6% | 987 | 57 | READY_FOR_BLOCK4_EVALUATION |
| TP_R050 | 3583 | 3649 | +€3,71 | 47,7% | 1117 | 12 | READY_FOR_BLOCK4_EVALUATION |
| GB20_R100 | 3581 | 3647 | +€6,25 | 43,0% | 786 | 93 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R050 | 3581 | 3647 | +€5,45 | 48,1% | 986 | 108 | READY_FOR_BLOCK4_EVALUATION |
| TP_R100 | 3581 | 3647 | +€4,12 | 41,2% | 854 | 91 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R100 | 3579 | 3645 | +€4,54 | 42,4% | 747 | 153 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R100 | 3575 | 3641 | +€3,76 | 41,5% | 657 | 245 | READY_FOR_BLOCK4_EVALUATION |
| TP_R150 | 3564 | 3630 | +€5,22 | 33,4% | 458 | 386 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R050 | 3563 | 3629 | +€4,03 | 48,3% | 926 | 153 | READY_FOR_BLOCK4_EVALUATION |
| TIME_6H | 3561 | 3627 | €-0,66 | 46,6% | 722 | 533 | READY_FOR_BLOCK4_EVALUATION |
| ATR15_R100 | 3560 | 3626 | +€0,31 | 32,9% | 378 | 729 | READY_FOR_BLOCK4_EVALUATION |
| TP_R200 | 3558 | 3624 | +€3,93 | 36,1% | 219 | 636 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R100 | 3557 | 3623 | +€2,05 | 40,0% | 571 | 390 | READY_FOR_BLOCK4_EVALUATION |
| ATR20_R100 | 3555 | 3621 | €-0,71 | 30,1% | 323 | 872 | READY_FOR_BLOCK4_EVALUATION |
| TIME_12H | 3538 | 3604 | +€0,12 | 41,5% | 423 | 752 | READY_FOR_BLOCK4_EVALUATION |
| ATR30_R100 | 3505 | 3571 | €-4,85 | 28,1% | 272 | 934 | READY_FOR_BLOCK4_EVALUATION |
| BE_R050 | 3497 | 3563 | €-3,71 | 33,0% | 573 | 734 | READY_FOR_BLOCK4_EVALUATION |
| BE_R100 | 3490 | 3556 | €-8,22 | 23,4% | 272 | 1067 | READY_FOR_BLOCK4_EVALUATION |
| TIME_24H | 3478 | 3544 | €-4,16 | 32,2% | 199 | 1018 | READY_FOR_BLOCK4_EVALUATION |

## Come leggere il controllo

- **EARLIER_BETTER**: la variante è uscita prima e ha conservato più profitto.
- **TOO_EARLY**: la variante è uscita prima ma ha tagliato un movimento migliore.
- **LATER_BETTER**: la variante ha continuato dopo l'uscita originale e ha guadagnato di più.
- **TOO_LATE**: la variante è rimasta aperta più a lungo e ha peggiorato il risultato.

## Limiti e protezioni

Le regole Shadow mantengono entrata, quantità, commissioni, stop protettivo iniziale e liquidazione. Le ambiguità all'interno della stessa candela vengono risolte scegliendo l'esito peggiore. Le posizioni già aperte al momento dell'installazione sono marcate come campione parziale e non saranno utilizzate dal futuro Blocco 4 come prova piena.

# Blocco 4 — Valutazione statistica Shadow

Generato: 2026-08-11T15:40:12+00:00

> Modulo esclusivamente valutativo. Non modifica strategie, uscite, posizioni o capitale. Le candidature vengono consegnate al futuro Blocco 5, senza applicazione automatica.

## Stato

- Risultati Block 3 disponibili: **136866**
- Valutazioni prodotte: **18630**
- Candidature al Blocco 5: **33**
- Mutazioni create automaticamente: **0**

## Classifica complessiva

| Scenario | Campione pieno | Δ medio (R) | Mediana (R) | CI bootstrap basso | Migliora | Score | Stato |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| CH_MBV3_GB20_R100 | 209 | 0,332 | 0,149 | 0,237 | 59,8% | 91,8 | ELIGIBLE_FOR_MUTATION |
| GB20_R040 | 2171 | 0,249 | 0,149 | 0,207 | 54,7% | 87,9 | VALIDATING |
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

Generato: 2026-08-11T15:43:33+00:00

Questi profili sono osservativi e Paper-only. Usano gli stessi trade della madre, ma applicano una specifica uscita Block 3 soltanto ai segnali aperti dopo la loro registrazione.
Nessuna promozione, modifica live o operazione reale viene eseguita automaticamente.

| Challenger | Madre | Scenario | Chiusi | Copertura | PF | PnL | Exp/trade | DD | Stato |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Rapida 1H V1 — giveback 20% dopo +0,5R | SHADOW_1H_FAST | GB20_R050 | 22 | 100,00% | 1,16 | +€67,59 | +€3,07 | 1,41% | COLLECTING |
| Rapida 1H V1 — giveback 30% dopo +0,5R | SHADOW_1H_FAST | GB30_R050 | 22 | 100,00% | 1,01 | +€2,56 | +€0,12 | 1,48% | COLLECTING |
| Relative Strength — giveback 20% dopo +0,5R | SHADOW_RELATIVE_STRENGTH | GB20_R050 | 35 | 100,00% | 1,07 | +€33,23 | +€0,95 | 1,50% | EARLY_NOT_CONFIRMED |
| Relative Strength — giveback 30% dopo +0,5R | SHADOW_RELATIVE_STRENGTH | GB30_R050 | 35 | 100,00% | 1,14 | +€68,27 | +€1,95 | 1,48% | EARLY_NOT_CONFIRMED |
| Scanner Top 5 BTC Strength — giveback 20% dopo +1,4R | SHADOW_SCANNER_TOP5_BTC | GB20_R140 | 11 | 100,00% | 0,41 | €-217,84 | €-19,80 | 2,18% | COLLECTING |
| Master Adaptive Consensus — breakeven dopo +0,2R | SHADOW_MASTER_ADAPTIVE_V1 | BE_A020 | 8 | 100,00% | 0,00 | €-110,01 | €-13,75 | 1,10% | COLLECTING |
| Momentum Breakout V3 Filtered — giveback 20% dopo +1,0R | SHADOW_1H_FAST_V3 | GB20_R100 | 28 | 100,00% | 0,92 | €-48,37 | €-1,73 | 2,13% | COLLECTING |
| Momentum Breakout — giveback 20% dopo +1,4R | SHADOW_1H_FAST | GB20_R140 | 0 | 0,00% | 0,00 | €0,00 | €0,00 | 0,00% | COLLECTING |

## Regole di valutazione

- Prima fotografia a 30 trade indipendenti.
- Revisione per possibile promozione a 50 trade indipendenti.
- PF minimo 1,50, expectancy e PnL positivi, drawdown massimo 15%, copertura minima 90%.
- PF deve superare la madre e il drawdown non deve essere peggiore sulla stessa serie di trade.
- La promozione resta una decisione umana protetta; il rollback viene predisposto soltanto in fase di approvazione.

# Blocco 4.5 — Crash Cascade Guard

Generato: 2026-08-11T15:39:43+00:00

> Paper-only. In mercato NORMAL/WATCH non riduce i segnali. Le limitazioni iniziano soltanto in STRESS, RECOVERY, CRASH, EXTREME o con dati non affidabili.

## Stato corrente

- Livello: **NORMAL**
- Direzione: **NONE**
- Segnali bloccati nel ciclo: **0**
- Simulazioni bloccate attive: **81**
- Simulazioni completate nel ciclo: **0**
- Liquidazioni virtuali evitate totali: **0**
- Valore cumulato del filtro: **145.47 R**
- Profitto virtuale mancato: **417.45 R**

## Stress test portafogli Paper

| Scenario | Posizioni interessate | Liquidazioni stimate | Perdita stimata EUR |
| --- | ---: | ---: | ---: |
| DOWN_10 | 106 | 0 | 10948.21 |
| DOWN_20 | 106 | 0 | 21896.42 |
| DOWN_30 | 106 | 0 | 32844.62 |
| DOWN_40 | 106 | 37 | 41374.76 |
| UP_10 | 148 | 0 | 43450.24 |
| UP_20 | 148 | 0 | 86900.48 |
| UP_30 | 148 | 0 | 130350.72 |
| UP_40 | 148 | 68 | 157884.14 |

## Modello di esecuzione

Se una candela di cascata attraversa nello stesso intervallo sia lo stop sia il prezzo di liquidazione, il Paper usa il caso peggiore e registra una liquidazione intrabar. Gli stop in gap o in regime di stress ricevono slippage aggiuntivo.

## Requisiti prima del live futures

- modalità ISOLATED obbligatoria;
- stop nativo sull'exchange;
- conferma dello stop prima di accettare la posizione;
- cross margin vietato.

# Blocco 5 — Candidati evolutivi controllati

Generato: 2026-08-11T15:38:16+00:00

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

Generato: 2026-08-11T15:43:39+00:00

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

Generato: 2026-08-11T15:43:39+00:00

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

Generato: 2026-08-11T15:43:39+00:00

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

Generato: 2026-08-11T15:43:39+00:00

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
| 1 | SHADOW_COMBO_ADAPTIVE_SIDE_REGIME_GUARD_V1 | BASELINE | 19.1 | E | 41 | 1.81 | 0.311 | 6.54 |
| 2 | SHADOW_1H_FAST_SCORE_6_75_COST_AWARE_V1 | BASELINE | 19.0 | E | 41 | 1.72 | 0.259 | 3.32 |
| 3 | SHADOW_1H_FAST_NOHIGH_CAP75_V1 | BASELINE | 18.4 | E | 71 | 1.50 | 0.199 | 5.40 |
| 4 | SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | BASELINE | 17.1 | E | 35 | 1.72 | 0.237 | 3.90 |
| 5 | SHADOW_1H_FAST_SCORE_6_75_V1 | BASELINE | 17.1 | E | 81 | 1.26 | 0.104 | 3.78 |
| 6 | SHADOW_1H_FAST_NO_PEPE_V1 | BASELINE | 16.2 | E | 77 | 1.26 | 0.107 | 4.82 |
| 7 | SHADOW_COMBO_ADAPTIVE | BASELINE | 16.1 | E | 46 | 1.55 | 0.171 | 2.72 |
| 8 | SHADOW_1H_FAST_SCORE_6_75_NO_TREND_UP_V1 | BASELINE | 16.0 | E | 39 | 1.47 | 0.198 | 4.19 |
| 9 | SHADOW_1H_FAST_V3 | BASELINE | 15.4 | E | 106 | 1.07 | 0.030 | 7.65 |
| 10 | SHADOW_DONCHIAN_1H | BASELINE | 14.8 | E | 43 | 1.43 | 0.232 | 8.55 |

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

Generato: 2026-08-11T15:43:40+00:00

> Paper-only e advisory. Il blocco misura quali strategie funzionano nei diversi regimi, ma non cambia automaticamente strategia o posizione.

## Stato

- Regime corrente: **RANGE**
- Righe di performance: **628**
- Strategie preferite nel regime corrente: **8**
- Strategie da evitare nel regime corrente: **8**
- Memorie contestuali: **296**
- Routing automatico: **NO**

## Classifica del regime corrente

| Rank | Portafoglio | Famiglia | Stato | Fitness | Trade | PF | Expectancy R | DD R |
| ---: | --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| 1 | SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_V1 | shadow-1h-fast-v3-nohigh-regime-guard-v1 | OBSERVING | 82.2 | 20 | 3.46 | 0.640 | 2.17 |
| 2 | SHADOW_1H_FAST_SCORE_6_75_COST_AWARE_V1 | shadow-1h-fast-score-6-75-cost-aware-v1 | OBSERVING | 82.2 | 23 | 2.55 | 0.467 | 3.16 |
| 3 | SHADOW_1H_FAST_SCORE_6_75_NO_TREND_UP_V1 | shadow-1h-fast-score-6-75-no-trend-up-v1 | OBSERVING | 82.0 | 21 | 1.98 | 0.394 | 2.56 |
| 4 | SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V1 | shadow-1h-fast-v3-nohigh-range-only-v1 | OBSERVING | 81.9 | 15 | 4.21 | 0.690 | 2.17 |
| 5 | SHADOW_BTC_BOLLINGER_1H | shadow-btc-bollinger-1h | INSUFFICIENT | 81.2 | 3 | 99.00 | 1.115 | 0.00 |
| 6 | SHADOW_SOL_BOLLINGER_4H | shadow-sol-bollinger-4h | INSUFFICIENT | 80.4 | 1 | 99.00 | 1.740 | 0.00 |
| 7 | SHADOW_BTC_BOLLINGER_4H | shadow-btc-bollinger-4h | INSUFFICIENT | 80.4 | 1 | 99.00 | 1.682 | 0.00 |
| 8 | SHADOW_DOGE_EMA_1H | shadow-doge-ema-1h | INSUFFICIENT | 76.1 | 7 | 2.35 | 0.426 | 1.11 |
| 9 | EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | momentum_breakout_v3_filtered | OBSERVING | 74.5 | 12 | 2.82 | 0.322 | 1.04 |
| 10 | SHADOW_1H_FAST_SCORE_6_75_RANGE_ONLY_V1 | shadow-1h-fast-score-6-75-range-only-v1 | OBSERVING | 74.3 | 17 | 1.99 | 0.430 | 3.04 |

## Sicurezza

- Il regime viene assegnato usando solo l'ultimo record noto prima dell'entrata del trade.
- Nessun uso di dati futuri per classificare il trade.
- Il Candidate Regime Gate è advisory per impostazione predefinita.
- Nessun cambio automatico di MASTER, posizione o live.

# Blocco 11 — Collegamento protetto al live

Generato: 2026-08-11T15:43:40+00:00

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

Generato: 2026-08-11T15:39:43+00:00

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
