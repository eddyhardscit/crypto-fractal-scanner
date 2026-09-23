# Paper trading automatico KuCoin

Generato: 2026-09-23T03:14:24+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-09-23T03:06:44+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-09-23T03:06:44+00:00 | 2026-09-23T03:06:44+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-09-23T02:45:00+00:00 | 2026-09-23T02:45:00+00:00 | 8,1 min | 25,0 min | OK |
| 60m | 12 | 2026-09-23T02:00:00+00:00 | 2026-09-23T02:00:00+00:00 | 8,1 min | 45,0 min | OK |
| 240m | 12 | 2026-09-22T20:00:00+00:00 | 2026-09-22T20:00:00+00:00 | 3,14 h | 1,00 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Rapida V3 NoHigh — Regime Guard | ZEC | 60m | LONG | 7,36 | 4,50 | 0,00 | OPENED | 8,1 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Master Adaptive GB20 — 50% a 0,75R | ZEC | 60m | LONG | 7,36 | 0,00 | 0,00 | OPENED | 8,1 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Master Adaptive GB20 — Breakeven 0,5R | ZEC | 60m | LONG | 7,36 | 0,00 | 0,00 | OPENED | 8,1 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Master Adaptive Gb20 V1 | ZEC | 60m | LONG | 7,36 | 0,00 | 0,00 | OPENED | 8,1 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Master Adaptive Expanded V1 | DOGE | 60m | LONG | 5,15 | 0,00 | 0,00 | OPENED | 8,1 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Master Adaptive V1 | ZEC | 60m | LONG | 7,36 | 0,00 | 0,00 | OPENED | 8,1 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Doge Bollinger 1H | DOGE | 60m | LONG | 5,15 | 5,00 | 0,00 | OPENED | 8,1 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top20 Long | HYPE | 60m | LONG | 5,48 | 5,00 | 0,00 | OPENED | 8,1 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top15 Long | HYPE | 60m | LONG | 5,48 | 5,00 | 0,00 | OPENED | 8,1 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V3 senza ESPORTS — MFE Lock | XRP | 60m | LONG | 6,97 | 4,50 | 0,00 | OPENED | 8,1 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V3 senza ESPORTS — Long Only | XRP | 60m | LONG | 6,97 | 4,50 | 0,00 | OPENED | 8,1 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V3 — senza ESPORTS | XRP | 60m | LONG | 6,97 | 4,50 | 0,00 | OPENED | 8,1 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V3 — Long Only | XRP | 60m | LONG | 6,97 | 4,50 | 0,00 | OPENED | 8,1 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V3 — no volatilità HIGH | XRP | 60m | LONG | 6,97 | 4,50 | 0,00 | OPENED | 8,1 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida 1H V3 Filtered — madre | XRP | 60m | LONG | 6,97 | 4,50 | 0,00 | OPENED | 8,1 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida V1 — senza PEPE | XRP | 60m | LONG | 6,97 | 4,50 | 0,00 | OPENED | 8,1 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Bilanciata 1H V2 | XRP | 60m | LONG | 6,97 | 5,50 | 0,00 | OPENED | 8,1 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Principale 4H | UNI | 240m | LONG | 8,25 | 6,00 | 0,00 | STALE_CANDLE | 3,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 188.1 minuti; tolleranza 60 minuti. |
| Principale 4H | NEAR | 240m | LONG | 7,75 | 6,00 | 0,00 | STALE_CANDLE | 3,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 188.1 minuti; tolleranza 60 minuti. |
| Principale 4H | PEPE | 240m | LONG | 7,75 | 6,00 | 0,00 | STALE_CANDLE | 3,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 188.1 minuti; tolleranza 60 minuti. |
| Principale 4H | XRP | 240m | LONG | 5,40 | 6,00 | 0,60 | STALE_CANDLE | 3,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 188.1 minuti; tolleranza 60 minuti. |
| Principale 4H | SUI | 240m | LONG | 4,75 | 6,00 | 1,25 | STALE_CANDLE | 3,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 188.1 minuti; tolleranza 60 minuti. |
| Principale 4H | SNDK | 240m | LONG | 4,17 | 6,00 | 1,83 | STALE_CANDLE | 3,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 188.1 minuti; tolleranza 60 minuti. |
| Principale 4H | ETH | 240m | LONG | 4,13 | 6,00 | 1,87 | STALE_CANDLE | 3,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 188.1 minuti; tolleranza 60 minuti. |
| Principale 4H | DOGE | 240m | LONG | 3,93 | 6,00 | 2,07 | STALE_CANDLE | 3,14 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 188.1 minuti; tolleranza 60 minuti. |
| Principale 4H | SOL | 240m | LONG | 3,60 | 6,00 | 2,40 | STALE_CANDLE | 3,14 h | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 188.1 minuti; tolleranza 60 minuti. |
| Principale 4H | BTC | 240m | LONG | 1,75 | 6,00 | 4,25 | STALE_CANDLE | 3,14 h | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 188.1 minuti; tolleranza 60 minuti. |
| Bilanciata 1H V1 | ZEC | 60m | LONG | 7,36 | 5,00 | 0,00 | READY | 8,1 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Bilanciata 1H — LONG senza Range High Vol | ZEC | 60m | LONG | 7,36 | 5,00 | 0,00 | READY | 8,1 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Bilanciata 1H V2 | ZEC | 60m | LONG | 7,36 | 5,50 | 0,00 | OPENED | 8,1 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top 5 Long 1H | ZEC | 60m | LONG | 7,36 | 5,00 | 0,00 | READY | 8,1 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Scanner Top10 Long | ZEC | 60m | LONG | 7,36 | 5,00 | 0,00 | READY | 8,1 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Scanner Top15 Long | ZEC | 60m | LONG | 7,36 | 5,00 | 0,00 | READY | 8,1 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Scanner Top20 Long | ZEC | 60m | LONG | 7,36 | 5,00 | 0,00 | READY | 8,1 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Scanner Top 5 + forza BTC 1H | ZEC | 60m | LONG | 7,36 | 5,00 | 0,00 | READY | 8,1 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Top 5 + BTC — solo MFE | ZEC | 60m | LONG | 7,36 | 5,00 | 0,00 | READY | 8,1 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Top 5 + BTC — BTC≤3 | ZEC | 60m | LONG | 7,36 | 5,00 | 0,00 | READY | 8,1 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €10.221,73 | +2,22% | €413,17 | €3.000,00 | 13,77% | 6 | 73 | 47,95% | 1,12 | 6,86% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 73 | 4027 | PRIME INDICAZIONI | 100 (mancano 27) |

- Trade del Principale 4H chiusi: **73**; win rate **47,95%**; profit factor **1,12**.
- Expectancy: **€2,80** per trade; P&L netto: **€204,12**; max drawdown: **6,86%**.
- Valutazione: **Si può osservare la direzione, ma il risultato resta fragile.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 6 | €10.221,73 | €810,34 | €2.431,03 | €204,65 | €19,08 |
| TEST | Benchmark Donchian breakout 1H | 0 | €12.610,81 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Donchian 1H Gb20 120R V1 | 0 | €12.313,90 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Trend — Side × Regime Guard | 6 | €11.645,25 | €2.674,23 | €5.348,45 | €232,40 | €131,95 |
| TEST | Rapida score 6–7,5 — Cost Aware | 5 | €11.620,38 | €2.691,24 | €8.073,72 | €232,88 | €-10,28 |
| TEST | Rapida V3 senza ESPORTS — Stress Guard | 0 | €11.427,03 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top 5 Long 1H | 5 | €11.156,36 | €3.086,22 | €6.172,44 | €222,77 | €-18,60 |
| TEST | Rapida V3 NoHigh — Regime Guard | 4 | €11.130,14 | €2.876,09 | €8.628,26 | €222,64 | €-40,08 |
| TEST | Combo Adaptive — madre | 6 | €11.088,28 | €2.299,30 | €4.598,59 | €221,81 | €-15,19 |
| TEST | Rapida V1 — senza PEPE | 5 | €11.071,50 | €2.353,92 | €7.061,77 | €221,43 | €34,76 |
| TEST | Rapida V1 — target pieno 2R | 0 | €10.941,17 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 senza ESPORTS — MFE Lock | 5 | €10.939,53 | €2.599,37 | €7.798,11 | €164,93 | €82,18 |
| TEST | Combo Adaptive — Long Only | 5 | €10.925,16 | €2.801,51 | €5.603,01 | €214,36 | €15,67 |
| TEST | MAIN — Side × Regime Guard | 5 | €10.904,33 | €875,73 | €2.627,20 | €219,40 | €11,44 |
| TEST | Combo Adaptive — Side × Regime Guard | 6 | €10.882,14 | €2.599,00 | €5.198,00 | €215,76 | €55,08 |
| TEST | Rapida 1H V3 Filtered — madre | 5 | €10.869,24 | €2.582,67 | €7.748,01 | €163,87 | €81,65 |
| TEST | Scanner Top15 Long | 8 | €10.829,40 | €2.661,52 | €5.323,03 | €215,60 | €30,13 |
| TEST | Scanner Top20 Long | 8 | €10.829,40 | €2.661,52 | €5.323,03 | €215,60 | €30,13 |
| TEST | Combo Adaptive — parziale 1R | 6 | €10.784,02 | €2.256,43 | €4.512,85 | €215,45 | €102,26 |
| TEST | Rapida 1H V2 | 0 | €10.702,82 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Scanner | 6 | €10.563,09 | €2.983,36 | €5.966,72 | €212,16 | €-37,47 |
| TEST | Scanner Top 5 + forza BTC 1H | 5 | €10.562,82 | €2.762,83 | €5.525,65 | €211,88 | €-51,37 |
| TEST | Rapida V1 — no HIGH + score <7,5 | 0 | €10.532,39 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 — no volatilità HIGH | 5 | €10.511,73 | €2.497,72 | €7.493,16 | €158,48 | €78,96 |
| TEST | Rapida V3 senza ESPORTS — Long Only | 5 | €10.479,94 | €2.490,17 | €7.470,50 | €158,01 | €78,73 |
| TEST | Bilanciata 1H V3 Filtered | 0 | €10.410,84 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Ampia 4H | 5 | €10.380,44 | €950,11 | €1.900,22 | €207,45 | €0,55 |
| TEST | Sol Donchian 1H | 0 | €10.372,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Forza relativa 1H V2 | 6 | €10.344,17 | €1.778,37 | €3.556,74 | €207,15 | €87,19 |
| TEST | Scanner Top10 Long | 6 | €10.337,90 | €2.799,10 | €5.598,20 | €207,43 | €-21,06 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 0 | €10.300,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 0 | €10.271,73 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | FAST NoHigh <7,5 · SHORT only | 0 | €10.270,06 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | MAIN — Dynamic Asset Selector | 0 | €10.264,13 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Benchmark trend following EMA 1H | 8 | €10.261,14 | €3.457,45 | €6.914,91 | €205,52 | €121,36 |
| TEST | Rapida V3 — senza ESPORTS | 5 | €10.257,31 | €2.437,27 | €7.311,80 | €154,65 | €77,05 |
| TEST | Doge Donchian 1H | 1 | €10.248,27 | €654,30 | €1.962,91 | €0,00 | €38,74 |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 0 | €10.239,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 0 | €10.235,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Ema 1H | 1 | €10.220,58 | €377,85 | €1.133,54 | €50,94 | €33,48 |
| TEST | Rapida V3 NoHigh — Range Only | 0 | €10.205,57 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 1H | 0 | €10.203,50 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 0 | €10.185,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida score 6–7,5 — Range Only | 0 | €10.175,88 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 4H | 1 | €10.150,55 | €546,20 | €1.092,40 | €50,69 | €12,49 |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 0 | €10.145,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 — Long Only | 5 | €10.111,28 | €2.402,57 | €7.207,71 | €152,45 | €75,96 |
| TEST | Btc Bollinger 4H | 0 | €10.101,88 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 0 | €10.099,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €10.086,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 0 | €10.048,77 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V1 — madre | 0 | €10.043,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 1H | 0 | €10.040,81 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Donchian 4H | 0 | €10.040,14 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €50 · 15x | 0 | €10.020,29 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · prudente · 5x | 0 | €10.019,53 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 4H | 1 | €10.018,25 | €588,03 | €1.176,05 | €50,03 | €13,45 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 0 | €10.017,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €50 · 15x | 0 | €10.011,55 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 0 | €10.008,92 | €0,00 | €0,00 | €0,00 | €0,00 |
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
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.975,54 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €50 · 15x | 0 | €9.966,02 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 4H | 0 | €9.964,84 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · prudente · 5x | 0 | €9.955,89 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · prudente · 5x | 0 | €9.951,01 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 0 | €9.940,92 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 1H | 0 | €9.939,78 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 1H | 0 | €9.934,84 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €50 · 15x | 0 | €9.927,87 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 4H | 0 | €9.914,14 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida score 6–7,5 — senza Trend Up | 0 | €9.902,86 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V3 — qualità completa + profit lock | 0 | €9.902,55 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Top 5 + BTC — solo MFE | 5 | €9.901,03 | €2.592,44 | €5.184,89 | €198,60 | €-48,43 |
| TEST | Rapida V3 — Long + no HIGH + score <7,5 | 0 | €9.891,96 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Bollinger 1H | 0 | €9.868,16 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida V1 — score 6–7,5 | 0 | €9.862,02 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Trend | 7 | €9.858,56 | €2.253,10 | €4.506,19 | €196,72 | €113,32 |
| TEST | Top 5 + BTC — target pieno 3R | 5 | €9.850,21 | €2.529,76 | €5.059,53 | €198,30 | €-52,26 |
| TEST | Bilanciata V3 · LONG only | 0 | €9.849,75 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Top 5 + BTC — 75% a 2,2R + runner 3R | 5 | €9.844,45 | €2.528,28 | €5.056,56 | €198,18 | €-52,23 |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 0 | €9.837,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Top 5 + BTC — Guard | 7 | €9.829,93 | €2.267,64 | €4.535,27 | €197,43 | €-26,16 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 0 | €9.817,34 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 4H | 0 | €9.808,89 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — 75% a 2R + runner 25% a 3R | 6 | €9.792,01 | €2.601,75 | €5.203,51 | €196,24 | €-42,63 |
| TEST | Combo Adaptive — Quality7 + Regime + parziale 1R | 4 | €9.784,29 | €2.070,96 | €4.141,91 | €194,46 | €-1,27 |
| TEST | Combo Adaptive — Quality7 | 4 | €9.781,63 | €2.111,30 | €4.222,59 | €194,47 | €24,08 |
| TEST | Global Confluence puro 1H | 0 | €9.779,96 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Ema 4H | 1 | €9.775,62 | €665,56 | €1.331,12 | €48,92 | €-6,72 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 0 | €9.762,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Runner25 V1 | 5 | €9.760,43 | €2.595,37 | €5.190,75 | €196,00 | €-15,86 |
| TEST | Bilanciata 1H V2 | 5 | €9.759,81 | €1.833,41 | €5.500,24 | €195,20 | €-6,41 |
| TEST | Bilanciata 1H — LONG senza Range High Vol | 6 | €9.750,10 | €1.829,51 | €5.488,54 | €195,75 | €-29,92 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 0 | €9.723,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Bollinger 1H | 1 | €9.708,21 | €630,89 | €1.892,66 | €48,55 | €-0,38 |
| TEST | Sol Bollinger 1H | 0 | €9.668,82 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive — Quality7 + Regime | 4 | €9.661,22 | €2.044,91 | €4.089,82 | €192,01 | €-1,25 |
| TEST | Top 5 + BTC — Guard + MFE | 6 | €9.636,86 | €2.029,97 | €4.059,95 | €193,65 | €-33,23 |
| TEST | Master Adaptive GB20 — Breakeven 0,5R | 7 | €9.631,34 | €1.953,82 | €3.907,65 | €192,63 | €27,16 |
| TEST | Eth Donchian 1H | 0 | €9.624,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive GB20 — 50% a 0,75R | 7 | €9.621,10 | €1.951,75 | €3.903,49 | €192,42 | €27,13 |
| TEST | Combo Adaptive — target pieno 3R | 6 | €9.608,83 | €2.553,08 | €5.106,16 | €192,57 | €-41,83 |
| TEST | Master Adaptive V1 | 7 | €9.583,88 | €1.944,20 | €3.888,39 | €191,68 | €27,03 |
| TEST | Combo Adaptive — Trend/Transition | 4 | €9.581,08 | €2.491,37 | €4.982,73 | €191,37 | €47,91 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 0 | €9.579,83 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom10 Short | 0 | €9.530,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom15 Short | 0 | €9.530,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom20 Short | 0 | €9.530,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Ema 1H | 1 | €9.480,51 | €1.023,67 | €3.071,02 | €47,27 | €28,78 |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | 0 | €9.464,68 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Gb20 V1 | 7 | €9.457,43 | €1.918,54 | €3.837,09 | €189,15 | €26,67 |
| TEST | Rapida V3 — score <7,5 | 0 | €9.454,76 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Profit Lock V1 | 0 | €9.450,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Adaptive 1H | 0 | €9.409,02 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Expanded V1 | 7 | €9.386,27 | €1.905,34 | €3.810,68 | €187,73 | €26,47 |
| TEST | Btc Ema 1H | 1 | €9.378,83 | €1.082,60 | €3.247,81 | €46,77 | €27,09 |
| TEST | Scanner Bottom 5 Short 1H | 0 | €9.377,56 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive GB20 — Loss Cap 0,75R | 5 | €9.353,65 | €2.928,10 | €5.856,19 | €188,05 | €-24,63 |
| TEST | Top 5 + BTC — BTC 2–3 | 5 | €9.344,43 | €2.558,18 | €5.116,36 | €187,37 | €77,24 |
| TEST | Combo Adaptive — MFE Trail esistente | 5 | €9.299,30 | €2.263,90 | €4.527,81 | €139,59 | €-8,85 |
| TEST | Rapida V1 — Long + BTC 1–3 + score <7,5 | 0 | €9.205,17 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H V1 | 5 | €9.192,63 | €1.918,41 | €5.755,22 | €184,38 | €-10,03 |
| TEST | Top 5 + BTC — Guard + BTC≤3 | 5 | €9.146,29 | €2.537,17 | €5.074,34 | €183,49 | €-23,04 |
| TEST | Forza relativa 1H V1 | 6 | €8.969,43 | €1.920,18 | €3.840,37 | €179,43 | €68,85 |
| TEST | Top 5 + BTC — Guard + BTC≤3 + MFE | 5 | €8.714,42 | €2.417,37 | €4.834,74 | €174,83 | €-21,96 |
| TEST | Top 5 + BTC — BTC≤3 | 5 | €8.680,91 | €2.412,05 | €4.824,10 | €174,39 | €-21,76 |
| TEST | Combo Mean Reversion | 1 | €8.622,92 | €736,11 | €1.472,22 | €43,10 | €4,45 |
| TEST | Master Adaptive Strict3 V1 | 4 | €8.464,60 | €2.596,60 | €5.193,19 | €169,16 | €24,76 |
| TEST | Master Adaptive No Alt V1 | 3 | €8.258,25 | €1.481,96 | €2.963,93 | €124,12 | €29,44 |
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
| PRINCIPALE | Principale 4H | Confluenza trend | €10.221,73 | €204,12 | 73 | 73 | 47,95% | 1,12 | €2,80 | 6,86% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €12.610,81 | €2.610,81 | 180 | 180 | 46,67% | 1,71 | €14,50 | 6,75% |
| TEST | Donchian 1H Gb20 120R V1 | Donchian breakout 20 barre | €12.313,90 | €2.313,90 | 148 | 148 | 45,95% | 1,84 | €15,63 | 6,75% |
| TEST | Combo Trend — Side × Regime Guard | Combo Trend | €11.645,25 | €1.516,50 | 176 | 176 | 52,27% | 1,48 | €8,62 | 10,10% |
| TEST | Rapida score 6–7,5 — Cost Aware | Momentum / breakout | €11.620,38 | €1.635,50 | 242 | 242 | 51,24% | 1,35 | €6,76 | 7,95% |
| TEST | Rapida V3 senza ESPORTS — Stress Guard | Momentum / breakout V3 Filtered | €11.427,03 | €1.427,03 | 194 | 194 | 50,52% | 1,38 | €7,36 | 5,29% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €11.156,36 | €1.178,66 | 214 | 214 | 46,73% | 1,31 | €5,51 | 8,85% |
| TEST | Rapida V3 NoHigh — Regime Guard | Momentum / breakout V3 Filtered | €11.130,14 | €1.119,69 | 213 | 212 | 51,17% | 1,35 | €5,26 | 5,24% |
| TEST | Combo Adaptive — madre | Combo Adaptive | €11.088,28 | €1.106,23 | 251 | 251 | 48,21% | 1,31 | €4,41 | 8,17% |
| TEST | Rapida V1 — senza PEPE | Momentum / breakout | €11.071,50 | €1.040,08 | 331 | 330 | 44,71% | 1,20 | €3,14 | 9,28% |
| TEST | Rapida V1 — target pieno 2R | Momentum / breakout | €10.941,17 | €941,17 | 306 | 306 | 42,16% | 1,19 | €3,08 | 6,56% |
| TEST | Rapida V3 senza ESPORTS — MFE Lock | Momentum / breakout V3 Filtered | €10.939,53 | €862,03 | 272 | 272 | 50,37% | 1,20 | €3,17 | 9,50% |
| TEST | Combo Adaptive — Long Only | Combo Adaptive | €10.925,16 | €912,84 | 207 | 207 | 46,38% | 1,26 | €4,41 | 7,78% |
| TEST | MAIN — Side × Regime Guard | Confluenza trend | €10.904,33 | €894,47 | 65 | 65 | 53,85% | 1,77 | €13,76 | 8,55% |
| TEST | Combo Adaptive — Side × Regime Guard | Combo Adaptive | €10.882,14 | €830,18 | 203 | 203 | 46,31% | 1,25 | €4,09 | 11,68% |
| TEST | Rapida 1H V3 Filtered — madre | Momentum / breakout V3 Filtered | €10.869,24 | €792,24 | 316 | 316 | 46,20% | 1,14 | €2,51 | 9,48% |
| TEST | Scanner Top15 Long | Scanner Top15 Long | €10.829,40 | €802,46 | 240 | 240 | 49,58% | 1,22 | €3,34 | 10,31% |
| TEST | Scanner Top20 Long | Scanner Top20 Long | €10.829,40 | €802,46 | 240 | 240 | 49,58% | 1,22 | €3,34 | 10,31% |
| TEST | Combo Adaptive — parziale 1R | Combo Adaptive | €10.784,02 | €684,47 | 208 | 208 | 47,60% | 1,23 | €3,29 | 8,69% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €10.702,82 | €702,82 | 96 | 86 | 48,96% | 1,31 | €7,32 | 3,89% |
| TEST | Combo Scanner | Combo Scanner | €10.563,09 | €604,14 | 211 | 211 | 45,50% | 1,15 | €2,86 | 11,38% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €10.562,82 | €617,50 | 179 | 179 | 46,37% | 1,18 | €3,45 | 11,27% |
| TEST | Rapida V1 — no HIGH + score <7,5 | Momentum / breakout | €10.532,39 | €532,39 | 241 | 241 | 44,81% | 1,13 | €2,21 | 10,86% |
| TEST | Rapida V3 — no volatilità HIGH | Momentum / breakout V3 Filtered | €10.511,73 | €433,04 | 236 | 235 | 46,61% | 1,12 | €1,83 | 7,10% |
| TEST | Rapida V3 senza ESPORTS — Long Only | Momentum / breakout V3 Filtered | €10.479,94 | €405,70 | 306 | 306 | 43,79% | 1,07 | €1,33 | 10,60% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €10.410,84 | €410,84 | 239 | 239 | 43,51% | 1,10 | €1,72 | 14,04% |
| TEST | Ampia 4H | Confluenza trend | €10.380,44 | €381,03 | 71 | 71 | 35,21% | 1,24 | €5,37 | 4,45% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €10.372,12 | €372,12 | 25 | 25 | 60,00% | 1,88 | €14,88 | 2,77% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €10.344,17 | €259,11 | 159 | 151 | 42,14% | 1,07 | €1,63 | 10,88% |
| TEST | Scanner Top10 Long | Scanner Top10 Long | €10.337,90 | €362,32 | 222 | 222 | 46,85% | 1,11 | €1,63 | 10,31% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | Momentum / breakout V3 Filtered | €10.300,05 | €300,05 | 33 | 33 | 48,48% | 2,04 | €9,09 | 2,01% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | Momentum / breakout V3 Filtered | €10.271,73 | €271,73 | 22 | 22 | 50,00% | 1,74 | €12,35 | 1,72% |
| TEST | FAST NoHigh <7,5 · SHORT only | Momentum / breakout | €10.270,06 | €270,06 | 204 | 204 | 44,12% | 1,08 | €1,32 | 10,86% |
| TEST | MAIN — Dynamic Asset Selector | Confluenza trend | €10.264,13 | €264,13 | 26 | 26 | 38,46% | 1,36 | €10,16 | 3,39% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €10.261,14 | €143,93 | 175 | 175 | 43,43% | 1,05 | €0,82 | 12,31% |
| TEST | Rapida V3 — senza ESPORTS | Momentum / breakout V3 Filtered | €10.257,31 | €184,64 | 279 | 279 | 44,80% | 1,03 | €0,66 | 10,92% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €10.248,27 | €210,71 | 21 | 21 | 61,90% | 1,45 | €10,03 | 3,08% |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | Momentum / breakout V3 Filtered | €10.239,20 | €239,20 | 17 | 17 | 52,94% | 4,50 | €14,07 | 1,01% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | Momentum / breakout V3 Filtered | €10.235,18 | €235,18 | 20 | 20 | 50,00% | 1,90 | €11,76 | 2,73% |
| TEST | Doge Ema 1H | Trend following EMA | €10.220,58 | €187,78 | 32 | 32 | 62,50% | 1,29 | €5,87 | 2,77% |
| TEST | Rapida V3 NoHigh — Range Only | Momentum / breakout V3 Filtered | €10.205,57 | €205,57 | 121 | 121 | 42,15% | 1,08 | €1,70 | 7,07% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.203,50 | €203,50 | 9 | 9 | 77,78% | 2,77 | €22,61 | 0,85% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | Momentum / breakout V3 Filtered | €10.185,37 | €185,37 | 22 | 22 | 40,91% | 1,57 | €8,43 | 2,27% |
| TEST | Rapida score 6–7,5 — Range Only | Momentum / breakout | €10.175,88 | €175,88 | 77 | 77 | 44,16% | 1,11 | €2,28 | 6,49% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €10.150,55 | €138,72 | 10 | 10 | 50,00% | 1,64 | €13,87 | 1,43% |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | Momentum / breakout V3 Filtered | €10.145,12 | €145,12 | 44 | 44 | 45,45% | 1,20 | €3,30 | 2,91% |
| TEST | Rapida V3 — Long Only | Momentum / breakout V3 Filtered | €10.111,28 | €39,65 | 309 | 309 | 43,37% | 1,01 | €0,13 | 12,52% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.101,88 | €101,88 | 4 | 4 | 75,00% | 2,86 | €25,47 | 0,91% |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | Momentum / breakout V3 Filtered | €10.099,04 | €99,04 | 55 | 55 | 54,55% | 1,12 | €1,80 | 3,59% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €10.086,00 | €86,00 | 35 | 35 | 48,57% | 1,59 | €2,46 | 0,33% |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | Momentum / breakout V3 Filtered | €10.048,77 | €48,77 | 23 | 23 | 43,48% | 1,12 | €2,12 | 3,05% |
| TEST | Rapida 1H V1 — madre | Momentum / breakout | €10.043,28 | €43,28 | 78 | 78 | 34,62% | 1,02 | €0,55 | 6,76% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €10.040,81 | €40,81 | 31 | 31 | 48,39% | 1,05 | €1,32 | 4,59% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €10.040,14 | €40,14 | 9 | 9 | 33,33% | 1,15 | €4,46 | 2,25% |
| TEST | Scalp RSI Short 85 · €50 · 15x | Inversione RSI estrema 15m | €10.020,29 | €20,29 | 7 | 7 | 57,14% | 1,71 | €2,90 | 0,31% |
| TEST | Scalp RSI Long 20 · prudente · 5x | Inversione RSI estrema 15m | €10.019,53 | €19,53 | 12 | 12 | 50,00% | 1,39 | €1,63 | 0,36% |
| TEST | Sol Ema 4H | Trend following EMA | €10.018,25 | €5,51 | 11 | 11 | 36,36% | 1,02 | €0,50 | 2,27% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €10.017,20 | €17,20 | 35 | 35 | 48,57% | 1,59 | €0,49 | 0,07% |
| TEST | Scalp RSI Short 80 · €50 · 15x | Inversione RSI estrema 15m | €10.011,55 | €11,55 | 19 | 19 | 42,11% | 1,20 | €0,61 | 0,53% |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | Momentum / breakout V3 Filtered | €10.008,92 | €8,92 | 30 | 30 | 36,67% | 1,02 | €0,30 | 4,84% |
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
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.975,54 | €-24,46 | 35 | 35 | 48,57% | 0,86 | €-0,70 | 0,84% |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | €9.966,02 | €-33,98 | 5 | 5 | 20,00% | 0,05 | €-6,80 | 0,34% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €9.964,84 | €-35,16 | 4 | 4 | 25,00% | 0,77 | €-8,79 | 1,10% |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | €9.955,89 | €-44,11 | 5 | 5 | 20,00% | 0,09 | €-8,82 | 0,45% |
| TEST | Scalp RSI Short 80 · prudente · 5x | Inversione RSI estrema 15m | €9.951,01 | €-48,99 | 19 | 19 | 36,84% | 0,53 | €-2,58 | 0,89% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €9.940,92 | €-59,08 | 22 | 22 | 31,82% | 0,53 | €-2,69 | 0,73% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €9.939,78 | €-60,22 | 16 | 16 | 50,00% | 0,85 | €-3,76 | 1,98% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €9.934,84 | €-65,16 | 14 | 14 | 50,00% | 0,80 | €-4,65 | 2,06% |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | €9.927,87 | €-72,13 | 22 | 22 | 36,36% | 0,31 | €-3,28 | 0,86% |
| TEST | Btc Ema 4H | Trend following EMA | €9.914,14 | €-85,86 | 5 | 5 | 20,00% | 0,58 | €-17,17 | 1,76% |
| TEST | Rapida score 6–7,5 — senza Trend Up | Momentum / breakout | €9.902,86 | €-97,14 | 223 | 223 | 45,29% | 0,98 | €-0,44 | 15,94% |
| TEST | Rapida V3 — qualità completa + profit lock | Momentum / breakout V3 Filtered | €9.902,55 | €-97,45 | 206 | 206 | 47,09% | 0,98 | €-0,47 | 8,44% |
| TEST | Top 5 + BTC — solo MFE | Scanner Top 5 + forza BTC | €9.901,03 | €-47,44 | 171 | 171 | 45,61% | 0,99 | €-0,28 | 12,28% |
| TEST | Rapida V3 — Long + no HIGH + score <7,5 | Momentum / breakout V3 Filtered | €9.891,96 | €-108,04 | 208 | 208 | 44,71% | 0,98 | €-0,52 | 6,64% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €9.868,16 | €-131,84 | 12 | 12 | 50,00% | 0,70 | €-10,99 | 4,16% |
| TEST | Rapida V1 — score 6–7,5 | Momentum / breakout | €9.862,02 | €-137,98 | 261 | 261 | 43,68% | 0,98 | €-0,53 | 15,64% |
| TEST | Combo Trend | Combo Trend | €9.858,56 | €-252,06 | 210 | 210 | 42,86% | 0,94 | €-1,20 | 14,08% |
| TEST | Top 5 + BTC — target pieno 3R | Scanner Top 5 + forza BTC | €9.850,21 | €-94,49 | 186 | 186 | 43,01% | 0,98 | €-0,51 | 11,91% |
| TEST | Bilanciata V3 · LONG only | Confluenza trend V3 Filtered | €9.849,75 | €-150,25 | 194 | 194 | 44,33% | 0,95 | €-0,77 | 13,79% |
| TEST | Top 5 + BTC — 75% a 2,2R + runner 3R | Scanner Top 5 + forza BTC | €9.844,45 | €-100,29 | 190 | 190 | 43,16% | 0,98 | €-0,53 | 12,06% |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | Momentum / breakout V3 Filtered | €9.837,38 | €-162,62 | 37 | 37 | 40,54% | 0,76 | €-4,40 | 3,08% |
| TEST | Top 5 + BTC — Guard | Scanner Top 5 + forza BTC | €9.829,93 | €-141,19 | 182 | 182 | 39,01% | 0,96 | €-0,78 | 7,34% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | Momentum / breakout V3 Filtered | €9.817,34 | €-182,66 | 24 | 24 | 41,67% | 0,64 | €-7,61 | 3,23% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €9.808,89 | €-191,11 | 7 | 7 | 14,29% | 0,41 | €-27,30 | 2,43% |
| TEST | Combo Adaptive — 75% a 2R + runner 25% a 3R | Combo Adaptive | €9.792,01 | €-162,24 | 178 | 178 | 39,33% | 0,95 | €-0,91 | 14,10% |
| TEST | Combo Adaptive — Quality7 + Regime + parziale 1R | Combo Adaptive | €9.784,29 | €-211,96 | 62 | 62 | 48,39% | 0,86 | €-3,42 | 4,27% |
| TEST | Combo Adaptive — Quality7 | Combo Adaptive | €9.781,63 | €-239,92 | 121 | 121 | 42,15% | 0,92 | €-1,98 | 8,88% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.779,96 | €-220,04 | 23 | 23 | 39,13% | 0,66 | €-9,57 | 3,93% |
| TEST | Eth Ema 4H | Trend following EMA | €9.775,62 | €-216,86 | 9 | 9 | 22,22% | 0,41 | €-24,10 | 2,54% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | Momentum / breakout V3 Filtered | €9.762,18 | €-237,82 | 7 | 7 | 14,29% | 0,02 | €-33,97 | 2,82% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €9.760,43 | €-220,59 | 116 | 116 | 34,48% | 0,93 | €-1,90 | 9,31% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €9.759,81 | €-230,47 | 190 | 174 | 45,79% | 0,94 | €-1,21 | 11,82% |
| TEST | Bilanciata 1H — LONG senza Range High Vol | Confluenza trend | €9.750,10 | €-216,68 | 162 | 162 | 46,30% | 0,92 | €-1,34 | 9,26% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | Momentum / breakout V3 Filtered | €9.723,72 | €-276,28 | 31 | 31 | 32,26% | 0,62 | €-8,91 | 4,83% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €9.708,21 | €-290,28 | 20 | 20 | 45,00% | 0,53 | €-14,51 | 3,66% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.668,82 | €-331,18 | 22 | 22 | 36,36% | 0,58 | €-15,05 | 3,69% |
| TEST | Combo Adaptive — Quality7 + Regime | Combo Adaptive | €9.661,22 | €-335,08 | 62 | 62 | 45,16% | 0,78 | €-5,40 | 5,41% |
| TEST | Top 5 + BTC — Guard + MFE | Scanner Top 5 + forza BTC | €9.636,86 | €-327,47 | 195 | 195 | 39,49% | 0,92 | €-1,68 | 8,78% |
| TEST | Master Adaptive GB20 — Breakeven 0,5R | Master Adaptive Consensus | €9.631,34 | €-393,48 | 133 | 133 | 33,83% | 0,89 | €-2,96 | 10,08% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.624,04 | €-375,96 | 24 | 24 | 33,33% | 0,57 | €-15,67 | 4,65% |
| TEST | Master Adaptive GB20 — 50% a 0,75R | Master Adaptive Consensus | €9.621,10 | €-403,70 | 128 | 128 | 35,94% | 0,88 | €-3,15 | 9,87% |
| TEST | Combo Adaptive — target pieno 3R | Combo Adaptive | €9.608,83 | €-346,28 | 158 | 158 | 39,24% | 0,88 | €-2,19 | 14,10% |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | €9.583,88 | €-440,82 | 130 | 130 | 35,38% | 0,88 | €-3,39 | 9,87% |
| TEST | Combo Adaptive — Trend/Transition | Combo Adaptive | €9.581,08 | €-463,84 | 99 | 99 | 46,46% | 0,80 | €-4,69 | 6,28% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | Momentum / breakout V3 Filtered | €9.579,83 | €-420,17 | 11 | 11 | 0,00% | 0,00 | €-38,20 | 4,20% |
| TEST | Scanner Bottom10 Short | Scanner Bottom10 Short | €9.530,72 | €-469,28 | 76 | 76 | 34,21% | 0,76 | €-6,17 | 9,06% |
| TEST | Scanner Bottom15 Short | Scanner Bottom15 Short | €9.530,72 | €-469,28 | 76 | 76 | 34,21% | 0,76 | €-6,17 | 9,06% |
| TEST | Scanner Bottom20 Short | Scanner Bottom20 Short | €9.530,72 | €-469,28 | 76 | 76 | 34,21% | 0,76 | €-6,17 | 9,06% |
| TEST | Eth Ema 1H | Trend following EMA | €9.480,51 | €-546,43 | 36 | 36 | 36,11% | 0,55 | €-15,18 | 5,88% |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | Scanner Bottom 5 Short | €9.464,68 | €-535,32 | 67 | 67 | 34,33% | 0,71 | €-7,99 | 9,08% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €9.457,43 | €-566,95 | 164 | 164 | 43,29% | 0,85 | €-3,46 | 10,69% |
| TEST | Rapida V3 — score <7,5 | Momentum / breakout V3 Filtered | €9.454,76 | €-545,24 | 281 | 281 | 42,35% | 0,91 | €-1,94 | 19,03% |
| TEST | Scanner Bottom5 Short Profit Lock V1 | Scanner Bottom 5 Short | €9.450,28 | €-549,72 | 68 | 68 | 33,82% | 0,69 | €-8,08 | 9,08% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.409,02 | €-590,98 | 27 | 27 | 33,33% | 0,40 | €-21,89 | 5,95% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €9.386,27 | €-637,91 | 108 | 108 | 36,11% | 0,78 | €-5,91 | 10,41% |
| TEST | Btc Ema 1H | Trend following EMA | €9.378,83 | €-646,31 | 28 | 28 | 25,00% | 0,36 | €-23,08 | 6,59% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.377,56 | €-622,44 | 95 | 95 | 33,68% | 0,73 | €-6,55 | 10,17% |
| TEST | Master Adaptive GB20 — Loss Cap 0,75R | Master Adaptive Consensus | €9.353,65 | €-618,20 | 124 | 124 | 28,23% | 0,83 | €-4,99 | 12,05% |
| TEST | Top 5 + BTC — BTC 2–3 | Scanner Top 5 + forza BTC | €9.344,43 | €-729,74 | 72 | 72 | 33,33% | 0,64 | €-10,14 | 12,43% |
| TEST | Combo Adaptive — MFE Trail esistente | Combo Adaptive | €9.299,30 | €-689,14 | 255 | 255 | 41,96% | 0,84 | €-2,70 | 15,45% |
| TEST | Rapida V1 — Long + BTC 1–3 + score <7,5 | Momentum / breakout | €9.205,17 | €-794,83 | 167 | 167 | 40,12% | 0,81 | €-4,76 | 13,09% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €9.192,63 | €-793,89 | 234 | 234 | 41,45% | 0,82 | €-3,39 | 15,68% |
| TEST | Top 5 + BTC — Guard + BTC≤3 | Scanner Top 5 + forza BTC | €9.146,29 | €-827,62 | 144 | 144 | 40,28% | 0,78 | €-5,75 | 16,24% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €8.969,43 | €-1.097,12 | 197 | 197 | 36,55% | 0,71 | €-5,57 | 19,11% |
| TEST | Top 5 + BTC — Guard + BTC≤3 + MFE | Scanner Top 5 + forza BTC | €8.714,42 | €-1.260,72 | 167 | 167 | 40,72% | 0,72 | €-7,55 | 18,17% |
| TEST | Top 5 + BTC — BTC≤3 | Scanner Top 5 + forza BTC | €8.680,91 | €-1.294,43 | 144 | 144 | 38,89% | 0,64 | €-8,99 | 20,25% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €8.622,92 | €-1.380,64 | 88 | 88 | 37,50% | 0,55 | €-15,69 | 16,26% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €8.464,60 | €-1.557,04 | 91 | 91 | 26,37% | 0,57 | €-17,11 | 16,25% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €8.258,25 | €-1.769,41 | 130 | 130 | 30,00% | 0,58 | €-13,61 | 17,99% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €7.569,99 | €-2.430,01 | 156 | 156 | 40,38% | 0,51 | €-15,58 | 26,04% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | ARB | LONG | Confluenza trend | 240m | 3,0x | 0,22709 | 0,22709 | 0,20271 | 0,15253 | 0,27584 | €18,13 | €54,39 | €5,84 | €0,00 |
| Principale 4H | NEAR | LONG | Confluenza trend | 240m | 3,0x | 4,12983 | 4,34100 | 3,70092 | 2,77387 | 4,98765 | €163,02 | €489,06 | €50,79 | €25,01 |
| Principale 4H | XMR | LONG | Confluenza trend | 240m | 3,0x | 582,85655 | 582,85655 | 534,94916 | 391,48531 | 678,67133 | €205,97 | €617,92 | €50,79 | €0,00 |
| Principale 4H | SUI | LONG | Confluenza trend | 240m | 3,0x | 1,03091 | 1,02650 | 0,95277 | 0,69243 | 1,18717 | €223,36 | €670,09 | €50,79 | €-2,86 |
| Principale 4H | PEPE | LONG | Confluenza trend | 240m | 3,0x | 0,00001 | 0,00000 | 0,00000 | 0,00000 | 0,00001 | €8,43 | €25,30 | €2,43 | €-1,10 |
| Principale 4H | ZEC | LONG | Confluenza trend | 240m | 3,0x | 1621,03414 | 1615,49000 | 1496,78264 | 1088,79460 | 1869,53714 | €191,42 | €574,26 | €44,02 | €-1,96 |
| Bilanciata 1H V1 | AVAX | LONG | Confluenza trend | 60m | 3,0x | 11,18924 | 11,18924 | 10,58712 | 7,51544 | 12,39348 | €13,07 | €39,21 | €2,11 | €0,00 |
| Bilanciata 1H V1 | XRP | LONG | Confluenza trend | 60m | 3,0x | 1,56886 | 1,58994 | 1,51998 | 1,05375 | 1,66664 | €491,46 | €1.474,38 | €45,94 | €19,81 |
| Bilanciata 1H V1 | SNDK | LONG | Confluenza trend | 60m | 3,0x | 1887,58744 | 1876,12000 | 1842,22509 | 1267,82957 | 1978,31214 | €625,26 | €1.875,79 | €45,08 | €-11,40 |
| Bilanciata 1H V1 | PEPE | LONG | Confluenza trend | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00001 | €347,42 | €1.042,26 | €46,10 | €-17,79 |
| Bilanciata 1H V1 | SUI | LONG | Confluenza trend | 60m | 3,0x | 1,02701 | 1,02650 | 0,99198 | 0,68981 | 1,09706 | €441,20 | €1.323,59 | €45,15 | €-0,65 |
| Bilanciata 1H — LONG senza Range High Vol | AVAX | LONG | Confluenza trend | 60m | 3,0x | 11,18924 | 11,18924 | 10,58712 | 7,51544 | 12,39348 | €300,54 | €901,63 | €48,52 | €0,00 |
| Bilanciata 1H — LONG senza Range High Vol | BTC | LONG | Confluenza trend | 60m | 3,0x | 86287,09397 | 86414,40000 | 85044,55981 | 57956,16478 | 88772,16227 | €12,49 | €37,46 | €0,54 | €0,06 |
| Bilanciata 1H — LONG senza Range High Vol | XRP | LONG | Confluenza trend | 60m | 3,0x | 1,56886 | 1,58994 | 1,51998 | 1,05375 | 1,66664 | €32,29 | €96,88 | €3,02 | €1,30 |
| Bilanciata 1H — LONG senza Range High Vol | SNDK | LONG | Confluenza trend | 60m | 3,0x | 1887,58744 | 1876,12000 | 1842,22509 | 1267,82957 | 1978,31214 | €641,78 | €1.925,35 | €46,27 | €-11,70 |
| Bilanciata 1H — LONG senza Range High Vol | PEPE | LONG | Confluenza trend | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00001 | €368,84 | €1.106,53 | €48,94 | €-18,88 |
| Bilanciata 1H — LONG senza Range High Vol | SUI | LONG | Confluenza trend | 60m | 3,0x | 1,02701 | 1,02650 | 0,99198 | 0,68981 | 1,09706 | €473,56 | €1.420,69 | €48,46 | €-0,70 |
| Bilanciata 1H V2 | AVAX | LONG | Confluenza trend V2 | 60m | 3,0x | 11,18924 | 11,18924 | 10,58712 | 7,51544 | 12,39348 | €302,59 | €907,76 | €48,85 | €0,00 |
| Bilanciata 1H V2 | TAO | LONG | Confluenza trend V2 | 60m | 3,0x | 319,16382 | 319,16382 | 303,23162 | 214,37170 | 351,02823 | €321,54 | €964,63 | €48,15 | €0,00 |
| Bilanciata 1H V2 | SNDK | LONG | Confluenza trend V2 | 60m | 3,0x | 1881,55624 | 1876,12000 | 1839,36608 | 1263,77861 | 1965,93654 | €705,00 | €2.115,00 | €47,42 | €-6,11 |
| Bilanciata 1H V2 | ZEC | LONG | Confluenza trend V2 | 60m | 3,0x | 1615,81310 | 1615,49000 | 1561,14549 | 1085,28780 | 1725,14832 | €480,85 | €1.442,54 | €48,81 | €-0,29 |
| Bilanciata 1H V2 | XRP | LONG | Confluenza trend V2 | 60m | 3,0x | 1,59026 | 1,58994 | 1,54579 | 1,06812 | 1,67919 | €23,44 | €70,31 | €1,97 | €-0,01 |
| Rapida score 6–7,5 — Cost Aware | SUI | LONG | Momentum / breakout | 60m | 3,0x | 1,01770 | 1,02650 | 0,97988 | 0,68356 | 1,07444 | €523,51 | €1.570,53 | €58,37 | €13,57 |
| Rapida score 6–7,5 — Cost Aware | PEPE | LONG | Momentum / breakout | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00001 | €417,50 | €1.252,50 | €58,30 | €-2,80 |
| Rapida score 6–7,5 — Cost Aware | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 96,71534 | 96,96500 | 95,19162 | 64,96047 | 99,00092 | €8,54 | €25,62 | €0,40 | €0,07 |
| Rapida score 6–7,5 — Cost Aware | SNDK | LONG | Momentum / breakout | 60m | 3,0x | 1887,58744 | 1876,12000 | 1852,30562 | 1267,82957 | 1940,51018 | €1.033,64 | €3.100,92 | €57,96 | €-18,84 |
| Rapida score 6–7,5 — Cost Aware | ZEC | LONG | Momentum / breakout | 60m | 3,0x | 1617,23338 | 1615,49000 | 1573,18890 | 1086,24175 | 1683,30010 | €708,05 | €2.124,14 | €57,85 | €-2,29 |
| Rapida V1 — senza PEPE | XMR | LONG | Momentum / breakout | 60m | 3,0x | 582,85655 | 582,85655 | 562,59219 | 391,48531 | 613,25308 | €543,24 | €1.629,72 | €56,66 | €0,00 |
| Rapida V1 — senza PEPE | ZEC | LONG | Momentum / breakout | 60m | 3,0x | 1617,23338 | 1615,49000 | 1573,18890 | 1086,24175 | 1683,30010 | €675,61 | €2.026,84 | €55,20 | €-2,18 |
| Rapida V1 — senza PEPE | SUI | LONG | Momentum / breakout | 60m | 3,0x | 1,02631 | 1,02650 | 0,99954 | 0,68934 | 1,06646 | €705,39 | €2.116,18 | €55,19 | €0,40 |
| Rapida V1 — senza PEPE | UNI | LONG | Momentum / breakout | 60m | 3,0x | 10,51710 | 10,82900 | 10,06359 | 7,06399 | 11,19737 | €410,86 | €1.232,57 | €53,15 | €36,55 |
| Rapida V1 — senza PEPE | XRP | LONG | Momentum / breakout | 60m | 3,0x | 1,59026 | 1,58994 | 1,55567 | 1,06812 | 1,64213 | €18,82 | €56,46 | €1,23 | €-0,01 |
| Rapida 1H V3 Filtered — madre | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1617,23338 | 1615,49000 | 1573,18890 | 1086,24175 | 1683,30010 | €660,45 | €1.981,36 | €53,96 | €-2,14 |
| Rapida 1H V3 Filtered — madre | SUI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,02631 | 1,02650 | 0,99954 | 0,68934 | 1,06646 | €689,56 | €2.068,69 | €53,95 | €0,39 |
| Rapida 1H V3 Filtered — madre | UNI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 10,51710 | 10,82900 | 10,06359 | 7,06399 | 11,19737 | €416,00 | €1.247,99 | €53,82 | €37,01 |
| Rapida 1H V3 Filtered — madre | DOGE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,10083 | 0,10282 | 0,10142 | 0,06772 | 0,10427 | €783,78 | €2.351,33 | €0,00 | €46,40 |
| Rapida 1H V3 Filtered — madre | XRP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,59026 | 1,58994 | 1,55567 | 1,06812 | 1,64213 | €32,88 | €98,64 | €2,15 | €-0,02 |
| Rapida V3 — no volatilità HIGH | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1617,23338 | 1615,49000 | 1573,18890 | 1086,24175 | 1683,30010 | €638,73 | €1.916,19 | €52,19 | €-2,07 |
| Rapida V3 — no volatilità HIGH | SUI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,02631 | 1,02650 | 0,99954 | 0,68934 | 1,06646 | €666,88 | €2.000,64 | €52,18 | €0,38 |
| Rapida V3 — no volatilità HIGH | UNI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 10,51710 | 10,82900 | 10,06359 | 7,06399 | 11,19737 | €402,31 | €1.206,94 | €52,05 | €35,79 |
| Rapida V3 — no volatilità HIGH | DOGE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,10083 | 0,10282 | 0,10142 | 0,06772 | 0,10427 | €758,00 | €2.273,99 | €0,00 | €44,88 |
| Rapida V3 — no volatilità HIGH | XRP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,59026 | 1,58994 | 1,55567 | 1,06812 | 1,64213 | €31,80 | €95,40 | €2,07 | €-0,02 |
| Rapida V3 — Long Only | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1617,23338 | 1615,49000 | 1573,18890 | 1086,24175 | 1683,30010 | €614,40 | €1.843,19 | €50,20 | €-1,99 |
| Rapida V3 — Long Only | SUI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,02631 | 1,02650 | 0,99954 | 0,68934 | 1,06646 | €641,48 | €1.924,43 | €50,19 | €0,37 |
| Rapida V3 — Long Only | UNI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 10,51710 | 10,82900 | 10,06359 | 7,06399 | 11,19737 | €386,99 | €1.160,96 | €50,06 | €34,43 |
| Rapida V3 — Long Only | DOGE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,10083 | 0,10282 | 0,10142 | 0,06772 | 0,10427 | €729,12 | €2.187,36 | €0,00 | €43,17 |
| Rapida V3 — Long Only | XRP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,59026 | 1,58994 | 1,55567 | 1,06812 | 1,64213 | €30,59 | €91,76 | €2,00 | €-0,02 |
| Rapida V3 — senza ESPORTS | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1617,23338 | 1615,49000 | 1573,18890 | 1086,24175 | 1683,30010 | €623,27 | €1.869,81 | €50,92 | €-2,02 |
| Rapida V3 — senza ESPORTS | SUI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,02631 | 1,02650 | 0,99954 | 0,68934 | 1,06646 | €650,74 | €1.952,22 | €50,92 | €0,37 |
| Rapida V3 — senza ESPORTS | UNI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 10,51710 | 10,82900 | 10,06359 | 7,06399 | 11,19737 | €392,58 | €1.177,73 | €50,79 | €34,93 |
| Rapida V3 — senza ESPORTS | DOGE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,10083 | 0,10282 | 0,10142 | 0,06772 | 0,10427 | €739,65 | €2.218,95 | €0,00 | €43,79 |
| Rapida V3 — senza ESPORTS | XRP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,59026 | 1,58994 | 1,55567 | 1,06812 | 1,64213 | €31,03 | €93,09 | €2,02 | €-0,02 |
| Rapida V3 senza ESPORTS — Long Only | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1617,23338 | 1615,49000 | 1573,18890 | 1086,24175 | 1683,30010 | €636,80 | €1.910,39 | €52,03 | €-2,06 |
| Rapida V3 senza ESPORTS — Long Only | SUI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,02631 | 1,02650 | 0,99954 | 0,68934 | 1,06646 | €664,86 | €1.994,59 | €52,02 | €0,38 |
| Rapida V3 senza ESPORTS — Long Only | UNI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 10,51710 | 10,82900 | 10,06359 | 7,06399 | 11,19737 | €401,10 | €1.203,29 | €51,89 | €35,69 |
| Rapida V3 senza ESPORTS — Long Only | DOGE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,10083 | 0,10282 | 0,10142 | 0,06772 | 0,10427 | €755,71 | €2.267,12 | €0,00 | €44,74 |
| Rapida V3 senza ESPORTS — Long Only | XRP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,59026 | 1,58994 | 1,55567 | 1,06812 | 1,64213 | €31,70 | €95,11 | €2,07 | €-0,02 |
| Rapida V3 senza ESPORTS — MFE Lock | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1617,23338 | 1615,49000 | 1573,18890 | 1086,24175 | 1683,30010 | €664,72 | €1.994,17 | €54,31 | €-2,15 |
| Rapida V3 senza ESPORTS — MFE Lock | SUI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,02631 | 1,02650 | 0,99954 | 0,68934 | 1,06646 | €694,02 | €2.082,06 | €54,30 | €0,40 |
| Rapida V3 senza ESPORTS — MFE Lock | UNI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 10,51710 | 10,82900 | 10,06359 | 7,06399 | 11,19737 | €418,69 | €1.256,06 | €54,16 | €37,25 |
| Rapida V3 senza ESPORTS — MFE Lock | DOGE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,10083 | 0,10282 | 0,10142 | 0,06772 | 0,10427 | €788,85 | €2.366,54 | €0,00 | €46,70 |
| Rapida V3 senza ESPORTS — MFE Lock | XRP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,59026 | 1,58994 | 1,55567 | 1,06812 | 1,64213 | €33,09 | €99,28 | €2,16 | €-0,02 |
| Ampia 4H | ARB | LONG | Confluenza trend | 240m | 2,0x | 0,22709 | 0,22709 | 0,19984 | 0,11468 | 0,30339 | €209,97 | €419,94 | €50,39 | €0,00 |
| Ampia 4H | XMR | LONG | Confluenza trend | 240m | 2,0x | 582,85655 | 582,85655 | 520,57694 | 294,34256 | 757,23945 | €241,58 | €483,16 | €51,63 | €0,00 |
| Ampia 4H | SUI | LONG | Confluenza trend | 240m | 2,0x | 1,03091 | 1,02650 | 0,92933 | 0,52061 | 1,31531 | €261,98 | €523,96 | €51,63 | €-2,24 |
| Ampia 4H | HYPE | LONG | Confluenza trend | 240m | 2,0x | 93,14162 | 96,96500 | 88,09003 | 47,03652 | 107,28609 | €22,62 | €45,24 | €2,45 | €1,86 |
| Ampia 4H | PEPE | LONG | Confluenza trend | 240m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00001 | €213,96 | €427,92 | €51,35 | €0,94 |
| Forza relativa 1H V1 | ZEC | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 1478,71568 | 1615,49000 | 1409,80814 | 746,75142 | 1630,31230 | €463,14 | €926,28 | €43,16 | €85,68 |
| Forza relativa 1H V1 | AVAX | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 11,18924 | 11,18924 | 10,58712 | 5,65056 | 12,51390 | €412,08 | €824,17 | €44,35 | €0,00 |
| Forza relativa 1H V1 | TAO | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 318,79375 | 318,79375 | 304,05530 | 160,99084 | 351,21832 | €470,01 | €940,03 | €43,46 | €0,00 |
| Forza relativa 1H V1 | XRP | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 1,56886 | 1,58994 | 1,51998 | 0,79228 | 1,67642 | €38,52 | €77,05 | €2,40 | €1,04 |
| Forza relativa 1H V1 | PEPE | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00001 | €507,13 | €1.014,27 | €44,86 | €-17,31 |
| Forza relativa 1H V1 | SNDK | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 1893,84869 | 1876,12000 | 1855,37474 | 956,39359 | 1978,49138 | €29,28 | €58,57 | €1,19 | €-0,55 |
| Forza relativa 1H V2 | ZEC | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 1478,71568 | 1615,49000 | 1409,80814 | 746,75142 | 1630,31230 | €535,87 | €1.071,75 | €49,94 | €99,13 |
| Forza relativa 1H V2 | ARB | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,21346 | 0,21346 | 0,19751 | 0,10780 | 0,24855 | €342,38 | €684,76 | €51,16 | €0,00 |
| Forza relativa 1H V2 | AVAX | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 11,18924 | 11,18924 | 10,58712 | 5,65056 | 12,51390 | €480,26 | €960,53 | €51,69 | €0,00 |
| Forza relativa 1H V2 | PEPE | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00001 | €372,31 | €744,61 | €51,24 | €-10,58 |
| Forza relativa 1H V2 | NEAR | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 4,45389 | 4,34100 | 4,18530 | 2,24921 | 5,04479 | €14,80 | €29,60 | €1,79 | €-0,75 |
| Forza relativa 1H V2 | SNDK | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 1893,84869 | 1876,12000 | 1855,37474 | 956,39359 | 1978,49138 | €32,75 | €65,49 | €1,33 | €-0,61 |
| Benchmark trend following EMA 1H | ZEC | LONG | Trend following EMA | 60m | 2,0x | 1478,71568 | 1615,49000 | 1402,15173 | 746,75142 | 1647,15637 | €474,62 | €949,23 | €49,15 | €87,80 |
| Benchmark trend following EMA 1H | ARB | LONG | Trend following EMA | 60m | 2,0x | 0,21346 | 0,21346 | 0,19574 | 0,10780 | 0,25245 | €13,97 | €27,94 | €2,32 | €0,00 |
| Benchmark trend following EMA 1H | TAO | LONG | Trend following EMA | 60m | 2,0x | 312,09241 | 312,09241 | 295,05688 | 157,60667 | 349,57055 | €459,30 | €918,60 | €50,14 | €0,00 |
| Benchmark trend following EMA 1H | ETH | LONG | Trend following EMA | 60m | 2,0x | 2732,80645 | 2758,42000 | 2686,07068 | 1380,06726 | 2835,62515 | €25,37 | €50,74 | €0,87 | €0,48 |
| Benchmark trend following EMA 1H | DOGE | LONG | Trend following EMA | 60m | 2,0x | 0,10018 | 0,10282 | 0,09604 | 0,05059 | 0,10928 | €19,87 | €39,75 | €1,64 | €1,05 |
| Benchmark trend following EMA 1H | BTC | LONG | Trend following EMA | 60m | 2,0x | 86287,09397 | 86414,40000 | 84906,50046 | 43574,98245 | 89324,39968 | €1.595,25 | €3.190,50 | €51,05 | €4,71 |
| Benchmark trend following EMA 1H | SNDK | LONG | Trend following EMA | 60m | 2,0x | 1846,65926 | 1876,12000 | 1793,32774 | 932,56293 | 1963,98862 | €847,88 | €1.695,76 | €48,97 | €27,05 |
| Benchmark trend following EMA 1H | XRP | LONG | Trend following EMA | 60m | 2,0x | 1,57957 | 1,58994 | 1,52811 | 0,79768 | 1,69276 | €21,20 | €42,39 | €1,38 | €0,28 |
| Scanner Top 5 Long 1H | AVAX | LONG | Scanner Top 5 Long | 60m | 2,0x | 11,18924 | 11,18924 | 10,58712 | 5,65056 | 12,39348 | €513,44 | €1.026,87 | €55,26 | €0,00 |
| Scanner Top 5 Long 1H | PEPE | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,00001 | 0,00000 | 0,00000 | 0,00000 | 0,00001 | €464,67 | €929,33 | €55,19 | €-28,83 |
| Scanner Top 5 Long 1H | TAO | LONG | Scanner Top 5 Long | 60m | 2,0x | 312,09241 | 312,09241 | 296,76044 | 157,60667 | 342,75635 | €14,18 | €28,35 | €1,39 | €0,00 |
| Scanner Top 5 Long 1H | DOGE | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,10031 | 0,10282 | 0,09647 | 0,05066 | 0,10799 | €718,97 | €1.437,95 | €55,07 | €35,98 |
| Scanner Top 5 Long 1H | SNDK | LONG | Scanner Top 5 Long | 60m | 2,0x | 1893,84869 | 1876,12000 | 1855,37474 | 956,39359 | 1970,79660 | €1.374,97 | €2.749,94 | €55,87 | €-25,74 |
| Scanner Top10 Long | DOGE | LONG | Scanner Top10 Long | 60m | 2,0x | 0,10031 | 0,10282 | 0,09647 | 0,05066 | 0,10799 | €674,88 | €1.349,76 | €51,69 | €33,77 |
| Scanner Top10 Long | BTC | LONG | Scanner Top10 Long | 60m | 2,0x | 86287,09397 | 86414,40000 | 85044,55981 | 43574,98245 | 88772,16227 | €17,94 | €35,88 | €0,52 | €0,05 |
| Scanner Top10 Long | NEAR | LONG | Scanner Top10 Long | 60m | 2,0x | 4,45089 | 4,34100 | 4,19594 | 2,24770 | 4,96079 | €448,23 | €896,46 | €51,35 | €-22,13 |
| Scanner Top10 Long | SNDK | LONG | Scanner Top10 Long | 60m | 2,0x | 1887,58744 | 1876,12000 | 1842,22509 | 953,23166 | 1978,31214 | €1.046,88 | €2.093,75 | €50,32 | €-12,72 |
| Scanner Top10 Long | PEPE | LONG | Scanner Top10 Long | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00001 | €586,29 | €1.172,59 | €51,86 | €-20,01 |
| Scanner Top10 Long | SUI | LONG | Scanner Top10 Long | 60m | 2,0x | 1,02701 | 1,02650 | 0,99198 | 0,51864 | 1,09706 | €24,88 | €49,75 | €1,70 | €-0,02 |
| Scanner Top15 Long | AVAX | LONG | Scanner Top15 Long | 60m | 2,0x | 11,18924 | 11,18924 | 10,58712 | 5,65056 | 12,39348 | €24,58 | €49,17 | €2,65 | €0,00 |
| Scanner Top15 Long | TAO | LONG | Scanner Top15 Long | 60m | 2,0x | 318,79375 | 318,79375 | 304,05530 | 160,99084 | 348,27063 | €575,95 | €1.151,91 | €53,25 | €0,00 |
| Scanner Top15 Long | PEPE | LONG | Scanner Top15 Long | 60m | 2,0x | 0,00001 | 0,00000 | 0,00000 | 0,00000 | 0,00001 | €441,80 | €883,59 | €52,47 | €-27,41 |
| Scanner Top15 Long | DOGE | LONG | Scanner Top15 Long | 60m | 2,0x | 0,10031 | 0,10282 | 0,09647 | 0,05066 | 0,10799 | €704,25 | €1.408,49 | €53,94 | €35,24 |
| Scanner Top15 Long | SNDK | LONG | Scanner Top15 Long | 60m | 2,0x | 1846,65926 | 1876,12000 | 1858,71883 | 932,56293 | 1942,65599 | €18,98 | €37,97 | €0,00 | €0,61 |
| Scanner Top15 Long | XRP | LONG | Scanner Top15 Long | 60m | 2,0x | 1,57010 | 1,58994 | 1,52309 | 0,79290 | 1,66413 | €859,45 | €1.718,90 | €51,47 | €21,72 |
| Scanner Top15 Long | SUI | LONG | Scanner Top15 Long | 60m | 2,0x | 1,02701 | 1,02650 | 0,99198 | 0,51864 | 1,09706 | €14,88 | €29,76 | €1,02 | €-0,01 |
| Scanner Top15 Long | HYPE | LONG | Scanner Top15 Long | 60m | 2,0x | 96,98439 | 96,96500 | 95,16897 | 48,97712 | 100,61523 | €21,62 | €43,24 | €0,81 | €-0,01 |
| Scanner Top20 Long | AVAX | LONG | Scanner Top20 Long | 60m | 2,0x | 11,18924 | 11,18924 | 10,58712 | 5,65056 | 12,39348 | €24,58 | €49,17 | €2,65 | €0,00 |
| Scanner Top20 Long | TAO | LONG | Scanner Top20 Long | 60m | 2,0x | 318,79375 | 318,79375 | 304,05530 | 160,99084 | 348,27063 | €575,95 | €1.151,91 | €53,25 | €0,00 |
| Scanner Top20 Long | PEPE | LONG | Scanner Top20 Long | 60m | 2,0x | 0,00001 | 0,00000 | 0,00000 | 0,00000 | 0,00001 | €441,80 | €883,59 | €52,47 | €-27,41 |
| Scanner Top20 Long | DOGE | LONG | Scanner Top20 Long | 60m | 2,0x | 0,10031 | 0,10282 | 0,09647 | 0,05066 | 0,10799 | €704,25 | €1.408,49 | €53,94 | €35,24 |
| Scanner Top20 Long | SNDK | LONG | Scanner Top20 Long | 60m | 2,0x | 1846,65926 | 1876,12000 | 1858,71883 | 932,56293 | 1942,65599 | €18,98 | €37,97 | €0,00 | €0,61 |
| Scanner Top20 Long | XRP | LONG | Scanner Top20 Long | 60m | 2,0x | 1,57010 | 1,58994 | 1,52309 | 0,79290 | 1,66413 | €859,45 | €1.718,90 | €51,47 | €21,72 |
| Scanner Top20 Long | SUI | LONG | Scanner Top20 Long | 60m | 2,0x | 1,02701 | 1,02650 | 0,99198 | 0,51864 | 1,09706 | €14,88 | €29,76 | €1,02 | €-0,01 |
| Scanner Top20 Long | HYPE | LONG | Scanner Top20 Long | 60m | 2,0x | 96,98439 | 96,96500 | 95,16897 | 48,97712 | 100,61523 | €21,62 | €43,24 | €0,81 | €-0,01 |
| Scanner Top 5 + forza BTC 1H | AVAX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 11,18924 | 11,18924 | 10,58712 | 5,65056 | 12,51390 | €487,93 | €975,86 | €52,51 | €0,00 |
| Scanner Top 5 + forza BTC 1H | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00001 | 0,00000 | 0,00000 | 0,00000 | 0,00001 | €445,04 | €890,08 | €52,86 | €-27,62 |
| Scanner Top 5 + forza BTC 1H | TAO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 315,91317 | 315,91317 | 299,73406 | 159,53615 | 351,50722 | €512,75 | €1.025,49 | €52,52 | €0,00 |
| Scanner Top 5 + forza BTC 1H | DOGE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,10031 | 0,10282 | 0,09647 | 0,05066 | 0,10876 | €13,14 | €26,29 | €1,01 | €0,66 |
| Scanner Top 5 + forza BTC 1H | SNDK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1893,84869 | 1876,12000 | 1855,37474 | 956,39359 | 1978,49138 | €1.303,97 | €2.607,94 | €52,98 | €-24,41 |
| Top 5 + BTC — solo MFE | AVAX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 11,18924 | 11,18924 | 10,58712 | 5,65056 | 12,51390 | €457,41 | €914,82 | €49,23 | €0,00 |
| Top 5 + BTC — solo MFE | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00001 | 0,00000 | 0,00000 | 0,00000 | 0,00001 | €417,20 | €834,41 | €49,55 | €-25,89 |
| Top 5 + BTC — solo MFE | TAO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 315,91317 | 315,91317 | 299,73406 | 159,53615 | 351,50722 | €480,68 | €961,35 | €49,23 | €0,00 |
| Top 5 + BTC — solo MFE | XRP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,57159 | 1,58994 | 1,52254 | 0,79366 | 1,67950 | €14,86 | €29,71 | €0,93 | €0,35 |
| Top 5 + BTC — solo MFE | SNDK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1893,84869 | 1876,12000 | 1855,37474 | 956,39359 | 1978,49138 | €1.222,30 | €2.444,60 | €49,66 | €-22,88 |
| Top 5 + BTC — Guard | TAO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 310,99219 | 310,99219 | 295,94100 | 157,05105 | 344,10479 | €505,15 | €1.010,30 | €48,90 | €0,00 |
| Top 5 + BTC — Guard | SUI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,02170 | 1,02650 | 0,97286 | 0,51596 | 1,12915 | €16,28 | €32,55 | €1,56 | €0,15 |
| Top 5 + BTC — Guard | XRP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,56819 | 1,58994 | 1,51999 | 0,79194 | 1,67424 | €13,21 | €26,43 | €0,81 | €0,37 |
| Top 5 + BTC — Guard | SNDK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1883,32659 | 1876,12000 | 1835,15614 | 951,07993 | 1989,30158 | €12,53 | €25,05 | €0,64 | €-0,10 |
| Top 5 + BTC — Guard | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00001 | €515,17 | €1.030,34 | €46,69 | €-1,19 |
| Top 5 + BTC — Guard | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1621,03414 | 1615,49000 | 1564,09034 | 818,62224 | 1746,31050 | €703,44 | €1.406,88 | €49,42 | €-4,81 |
| Top 5 + BTC — Guard | NEAR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 4,43189 | 4,34100 | 4,21369 | 2,23810 | 4,91191 | €501,86 | €1.003,71 | €49,42 | €-20,58 |
| Top 5 + BTC — BTC≤3 | XRP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,56819 | 1,58994 | 1,51999 | 0,79194 | 1,67424 | €700,60 | €1.401,20 | €43,07 | €19,43 |
| Top 5 + BTC — BTC≤3 | SNDK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1882,76648 | 1876,12000 | 1833,28933 | 950,79707 | 1991,61621 | €819,37 | €1.638,74 | €43,06 | €-5,79 |
| Top 5 + BTC — BTC≤3 | NEAR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 4,45089 | 4,34100 | 4,19594 | 2,24770 | 5,01178 | €375,90 | €751,80 | €43,06 | €-18,56 |
| Top 5 + BTC — BTC≤3 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00001 | €492,89 | €985,79 | €43,60 | €-16,82 |
| Top 5 + BTC — BTC≤3 | SUI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,02701 | 1,02650 | 0,99198 | 0,51864 | 1,10407 | €23,29 | €46,58 | €1,59 | €-0,02 |
| Top 5 + BTC — BTC 2–3 | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1485,33701 | 1615,49000 | 1415,48789 | 750,09519 | 1639,00507 | €477,40 | €954,81 | €44,90 | €83,67 |
| Top 5 + BTC — BTC 2–3 | XRP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,56819 | 1,58994 | 1,51999 | 0,79194 | 1,67424 | €756,92 | €1.513,84 | €46,53 | €20,99 |
| Top 5 + BTC — BTC 2–3 | SNDK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1882,76648 | 1876,12000 | 1833,28933 | 950,79707 | 1991,61621 | €885,24 | €1.770,48 | €46,53 | €-6,25 |
| Top 5 + BTC — BTC 2–3 | NEAR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 4,45089 | 4,34100 | 4,19594 | 2,24770 | 5,01178 | €406,59 | €813,18 | €46,58 | €-20,08 |
| Top 5 + BTC — BTC 2–3 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00001 | €32,02 | €64,04 | €2,83 | €-1,09 |
| Top 5 + BTC — Guard + MFE | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,21346 | 0,21346 | 0,19751 | 0,10780 | 0,24855 | €15,82 | €31,63 | €2,36 | €0,00 |
| Top 5 + BTC — Guard + MFE | TAO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 310,99219 | 310,99219 | 295,94100 | 157,05105 | 344,10479 | €487,98 | €975,95 | €47,23 | €0,00 |
| Top 5 + BTC — Guard + MFE | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00001 | €340,78 | €681,57 | €46,90 | €-9,68 |
| Top 5 + BTC — Guard + MFE | DOGE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,09987 | 0,10282 | 0,09538 | 0,05043 | 0,10974 | €15,14 | €30,27 | €1,36 | €0,89 |
| Top 5 + BTC — Guard + MFE | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1621,03414 | 1615,49000 | 1564,09034 | 818,62224 | 1746,31050 | €689,17 | €1.378,33 | €48,42 | €-4,71 |
| Top 5 + BTC — Guard + MFE | NEAR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 4,43189 | 4,34100 | 4,21369 | 2,23810 | 4,91191 | €481,10 | €962,19 | €47,37 | €-19,73 |
| Top 5 + BTC — Guard + BTC≤3 | XRP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,56819 | 1,58994 | 1,51999 | 0,79194 | 1,67424 | €738,16 | €1.476,33 | €45,38 | €20,47 |
| Top 5 + BTC — Guard + BTC≤3 | SNDK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1882,76648 | 1876,12000 | 1833,28933 | 950,79707 | 1991,61621 | €863,30 | €1.726,61 | €45,37 | €-6,10 |
| Top 5 + BTC — Guard + BTC≤3 | NEAR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 4,45089 | 4,34100 | 4,19594 | 2,24770 | 5,01178 | €396,05 | €792,11 | €45,37 | €-19,56 |
| Top 5 + BTC — Guard + BTC≤3 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00001 | €519,32 | €1.038,65 | €45,94 | €-17,73 |
| Top 5 + BTC — Guard + BTC≤3 | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1621,03414 | 1615,49000 | 1564,09034 | 818,62224 | 1746,31050 | €20,33 | €40,65 | €1,43 | €-0,14 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | XRP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,56819 | 1,58994 | 1,51999 | 0,79194 | 1,67424 | €703,31 | €1.406,62 | €43,24 | €19,51 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | SNDK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1882,76648 | 1876,12000 | 1833,28933 | 950,79707 | 1991,61621 | €822,54 | €1.645,08 | €43,23 | €-5,81 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | NEAR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 4,45089 | 4,34100 | 4,19594 | 2,24770 | 5,01178 | €377,35 | €754,70 | €43,23 | €-18,63 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00001 | €494,80 | €989,60 | €43,77 | €-16,89 |
| Top 5 + BTC — Guard + BTC≤3 + MFE | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1621,03414 | 1615,49000 | 1564,09034 | 818,62224 | 1746,31050 | €19,37 | €38,75 | €1,36 | €-0,13 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | TAO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 310,99219 | 310,99219 | 295,94100 | 157,05105 | 356,14574 | €511,28 | €1.022,56 | €49,49 | €0,00 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | NEAR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 4,45089 | 4,34100 | 4,19594 | 2,24770 | 5,21574 | €425,85 | €851,71 | €48,79 | €-21,03 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | SNDK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1887,58744 | 1876,12000 | 1842,22509 | 953,23166 | 2023,67449 | €991,12 | €1.982,23 | €47,64 | €-12,04 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00001 | €560,15 | €1.120,30 | €49,55 | €-19,12 |
| Top 5 + BTC — 75% a 2,2R + runner 3R | SUI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,02701 | 1,02650 | 0,99198 | 0,51864 | 1,13209 | €39,88 | €79,76 | €2,72 | €-0,04 |
| Top 5 + BTC — target pieno 3R | TAO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 310,99219 | 310,99219 | 295,94100 | 157,05105 | 356,14574 | €511,58 | €1.023,16 | €49,52 | €0,00 |
| Top 5 + BTC — target pieno 3R | NEAR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 4,45089 | 4,34100 | 4,19594 | 2,24770 | 5,21574 | €426,10 | €852,21 | €48,81 | €-21,04 |
| Top 5 + BTC — target pieno 3R | SNDK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1887,58744 | 1876,12000 | 1842,22509 | 953,23166 | 2023,67449 | €991,70 | €1.983,39 | €47,66 | €-12,05 |
| Top 5 + BTC — target pieno 3R | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00001 | €560,48 | €1.120,96 | €49,58 | €-19,13 |
| Top 5 + BTC — target pieno 3R | SUI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,02701 | 1,02650 | 0,99198 | 0,51864 | 1,13209 | €39,90 | €79,80 | €2,72 | €-0,04 |
| Combo Trend | ZEC | LONG | Combo Trend | 60m | 2,0x | 1478,71568 | 1615,49000 | 1402,15173 | 746,75142 | 1647,15637 | €460,25 | €920,51 | €47,66 | €85,14 |
| Combo Trend | ARB | LONG | Combo Trend | 60m | 2,0x | 0,21346 | 0,21346 | 0,19574 | 0,10780 | 0,25245 | €13,55 | €27,09 | €2,25 | €0,00 |
| Combo Trend | TAO | LONG | Combo Trend | 60m | 2,0x | 310,99219 | 310,99219 | 294,26865 | 157,05105 | 347,78397 | €450,58 | €901,16 | €48,46 | €0,00 |
| Combo Trend | DOGE | LONG | Combo Trend | 60m | 2,0x | 0,10031 | 0,10282 | 0,09604 | 0,05066 | 0,10970 | €579,80 | €1.159,60 | €49,34 | €29,02 |
| Combo Trend | SNDK | LONG | Combo Trend | 60m | 2,0x | 1846,65926 | 1876,12000 | 1793,32774 | 932,56293 | 1963,98862 | €14,52 | €29,04 | €0,84 | €0,46 |
| Combo Trend | XRP | LONG | Combo Trend | 60m | 2,0x | 1,59083 | 1,58994 | 1,53918 | 0,80337 | 1,70446 | €719,94 | €1.439,89 | €46,75 | €-0,80 |
| Combo Trend | PEPE | LONG | Combo Trend | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00001 | €14,45 | €28,90 | €1,42 | €-0,49 |
| Combo Mean Reversion | ZEC | SHORT | Combo Mean Reversion | 60m | 2,0x | 1620,38586 | 1615,49000 | 1667,82005 | 2422,47686 | 1544,49117 | €736,11 | €1.472,22 | €43,10 | €4,45 |
| Combo Scanner | TAO | LONG | Combo Scanner | 60m | 2,0x | 310,99219 | 310,99219 | 295,94100 | 157,05105 | 344,10479 | €543,27 | €1.086,54 | €52,59 | €0,00 |
| Combo Scanner | SUI | LONG | Combo Scanner | 60m | 2,0x | 1,02170 | 1,02650 | 0,97286 | 0,51596 | 1,12915 | €17,50 | €35,01 | €1,67 | €0,16 |
| Combo Scanner | DOGE | LONG | Combo Scanner | 60m | 2,0x | 0,10031 | 0,10282 | 0,09647 | 0,05066 | 0,10876 | €15,85 | €31,71 | €1,21 | €0,79 |
| Combo Scanner | SNDK | LONG | Combo Scanner | 60m | 2,0x | 1887,58744 | 1876,12000 | 1842,22509 | 953,23166 | 1987,38461 | €1.051,21 | €2.102,42 | €50,53 | €-12,77 |
| Combo Scanner | PEPE | LONG | Combo Scanner | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00001 | €600,21 | €1.200,43 | €53,09 | €-20,49 |
| Combo Scanner | ZEC | LONG | Combo Scanner | 60m | 2,0x | 1621,03414 | 1615,49000 | 1564,09034 | 818,62224 | 1746,31050 | €755,31 | €1.510,62 | €53,07 | €-5,17 |
| Combo Adaptive — madre | AVAX | LONG | Combo Adaptive | 60m | 2,0x | 11,18924 | 11,18924 | 10,58712 | 5,65056 | 12,39348 | €508,49 | €1.016,97 | €54,73 | €0,00 |
| Combo Adaptive — madre | TAO | LONG | Combo Adaptive | 60m | 2,0x | 318,79375 | 318,79375 | 304,05530 | 160,99084 | 348,27063 | €31,11 | €62,21 | €2,88 | €0,00 |
| Combo Adaptive — madre | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00001 | 0,00000 | 0,00000 | 0,00000 | 0,00001 | €455,86 | €911,72 | €54,14 | €-28,29 |
| Combo Adaptive — madre | DOGE | LONG | Combo Adaptive | 60m | 2,0x | 0,10031 | 0,10282 | 0,09647 | 0,05066 | 0,10799 | €720,29 | €1.440,58 | €55,17 | €36,05 |
| Combo Adaptive — madre | SNDK | LONG | Combo Adaptive | 60m | 2,0x | 1893,84869 | 1876,12000 | 1855,37474 | 956,39359 | 1970,79660 | €44,26 | €88,51 | €1,80 | €-0,83 |
| Combo Adaptive — madre | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 4,43189 | 4,34100 | 4,21369 | 2,23810 | 4,86827 | €539,30 | €1.078,59 | €53,10 | €-22,12 |
| Combo Adaptive — MFE Trail esistente | DOGE | LONG | Combo Adaptive | 60m | 2,0x | 0,09987 | 0,10282 | 0,09999 | 0,05043 | 0,10885 | €517,62 | €1.035,24 | €0,00 | €30,58 |
| Combo Adaptive — MFE Trail esistente | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 4,45089 | 4,34100 | 4,19594 | 2,24770 | 4,96079 | €401,09 | €802,18 | €45,95 | €-19,81 |
| Combo Adaptive — MFE Trail esistente | XRP | LONG | Combo Adaptive | 60m | 2,0x | 1,59083 | 1,58994 | 1,54434 | 0,80337 | 1,68380 | €776,41 | €1.552,81 | €45,38 | €-0,87 |
| Combo Adaptive — MFE Trail esistente | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00001 | €526,04 | €1.052,09 | €46,53 | €-17,96 |
| Combo Adaptive — MFE Trail esistente | SNDK | LONG | Combo Adaptive | 60m | 2,0x | 1893,84869 | 1876,12000 | 1855,37474 | 956,39359 | 1970,79660 | €42,75 | €85,49 | €1,74 | €-0,80 |
| Combo Adaptive — Quality7 | AVAX | LONG | Combo Adaptive | 60m | 2,0x | 11,18924 | 11,18924 | 10,58712 | 5,65056 | 12,39348 | €455,87 | €911,74 | €49,06 | €0,00 |
| Combo Adaptive — Quality7 | TAO | LONG | Combo Adaptive | 60m | 2,0x | 318,79375 | 318,79375 | 304,05530 | 160,99084 | 348,27063 | €528,74 | €1.057,48 | €48,89 | €0,00 |
| Combo Adaptive — Quality7 | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 1617,23338 | 1615,49000 | 1560,60477 | 816,70286 | 1730,49061 | €695,49 | €1.390,97 | €48,71 | €-1,50 |
| Combo Adaptive — Quality7 | UNI | LONG | Combo Adaptive | 60m | 2,0x | 10,51710 | 10,82900 | 9,93401 | 5,31114 | 11,68328 | €431,20 | €862,40 | €47,81 | €25,58 |
| Combo Adaptive — Trend/Transition | TAO | LONG | Combo Adaptive | 60m | 2,0x | 312,40247 | 312,40247 | 297,84064 | 157,76325 | 341,52612 | €518,42 | €1.036,84 | €48,33 | €0,00 |
| Combo Adaptive — Trend/Transition | DOGE | LONG | Combo Adaptive | 60m | 2,0x | 0,09987 | 0,10282 | 0,09538 | 0,05043 | 0,10885 | €536,30 | €1.072,61 | €48,20 | €31,68 |
| Combo Adaptive — Trend/Transition | XRP | LONG | Combo Adaptive | 60m | 2,0x | 1,57159 | 1,58994 | 1,52254 | 0,79366 | 1,66969 | €757,73 | €1.515,45 | €47,30 | €17,69 |
| Combo Adaptive — Trend/Transition | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 1617,23338 | 1615,49000 | 1560,60477 | 816,70286 | 1730,49061 | €678,92 | €1.357,83 | €47,55 | €-1,46 |
| Combo Adaptive — Quality7 + Regime | TAO | LONG | Combo Adaptive | 60m | 2,0x | 318,79375 | 318,79375 | 304,05530 | 160,99084 | 348,27063 | €531,82 | €1.063,64 | €49,17 | €0,00 |
| Combo Adaptive — Quality7 + Regime | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 4,48590 | 4,34100 | 4,21923 | 2,26538 | 5,01922 | €393,27 | €786,53 | €46,75 | €-25,41 |
| Combo Adaptive — Quality7 + Regime | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 1617,23338 | 1615,49000 | 1560,60477 | 816,70286 | 1730,49061 | €687,56 | €1.375,13 | €48,15 | €-1,48 |
| Combo Adaptive — Quality7 + Regime | UNI | LONG | Combo Adaptive | 60m | 2,0x | 10,51710 | 10,82900 | 9,93401 | 5,31114 | 11,68328 | €432,26 | €864,52 | €47,93 | €25,64 |
| Combo Adaptive — Long Only | DOGE | LONG | Combo Adaptive | 60m | 2,0x | 0,09987 | 0,10282 | 0,09538 | 0,05043 | 0,10885 | €597,74 | €1.195,47 | €53,72 | €35,31 |
| Combo Adaptive — Long Only | SNDK | LONG | Combo Adaptive | 60m | 2,0x | 1846,65926 | 1876,12000 | 1861,45820 | 932,56293 | 1942,65599 | €75,58 | €151,15 | €0,00 | €2,41 |
| Combo Adaptive — Long Only | XRP | LONG | Combo Adaptive | 60m | 2,0x | 1,59083 | 1,58994 | 1,54434 | 0,80337 | 1,68380 | €888,24 | €1.776,47 | €51,91 | €-0,99 |
| Combo Adaptive — Long Only | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00001 | €616,97 | €1.233,94 | €54,58 | €-21,06 |
| Combo Adaptive — Long Only | TAO | LONG | Combo Adaptive | 60m | 2,0x | 313,83275 | 313,83275 | 300,19413 | 158,48554 | 341,11001 | €622,99 | €1.245,98 | €54,15 | €0,00 |
| Combo Adaptive — parziale 1R | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 1485,33701 | 1615,49000 | 1415,48789 | 750,09519 | 1625,03524 | €544,86 | €1.089,72 | €51,25 | €95,49 |
| Combo Adaptive — parziale 1R | AVAX | LONG | Combo Adaptive | 60m | 2,0x | 11,18924 | 11,18924 | 10,58712 | 5,65056 | 12,39348 | €493,65 | €987,29 | €53,13 | €0,00 |
| Combo Adaptive — parziale 1R | TAO | LONG | Combo Adaptive | 60m | 2,0x | 318,79375 | 318,79375 | 304,05530 | 160,99084 | 348,27063 | €35,99 | €71,99 | €3,33 | €0,00 |
| Combo Adaptive — parziale 1R | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00001 | 0,00000 | 0,00000 | 0,00000 | 0,00001 | €442,57 | €885,14 | €52,56 | €-27,46 |
| Combo Adaptive — parziale 1R | DOGE | LONG | Combo Adaptive | 60m | 2,0x | 0,10031 | 0,10282 | 0,09647 | 0,05066 | 0,10799 | €699,14 | €1.398,28 | €53,55 | €34,99 |
| Combo Adaptive — parziale 1R | SNDK | LONG | Combo Adaptive | 60m | 2,0x | 1893,84869 | 1876,12000 | 1855,37474 | 956,39359 | 1970,79660 | €40,21 | €80,43 | €1,63 | €-0,75 |
| Combo Adaptive — Quality7 + Regime + parziale 1R | TAO | LONG | Combo Adaptive | 60m | 2,0x | 318,79375 | 318,79375 | 304,05530 | 160,99084 | 348,27063 | €538,59 | €1.077,19 | €49,80 | €0,00 |
| Combo Adaptive — Quality7 + Regime + parziale 1R | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 4,48590 | 4,34100 | 4,21923 | 2,26538 | 5,01922 | €398,27 | €796,55 | €47,35 | €-25,73 |
| Combo Adaptive — Quality7 + Regime + parziale 1R | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 1617,23338 | 1615,49000 | 1560,60477 | 816,70286 | 1730,49061 | €696,32 | €1.392,64 | €48,76 | €-1,50 |
| Combo Adaptive — Quality7 + Regime + parziale 1R | UNI | LONG | Combo Adaptive | 60m | 2,0x | 10,51710 | 10,82900 | 9,93401 | 5,31114 | 11,68328 | €437,77 | €875,53 | €48,54 | €25,96 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 1491,36821 | 1615,49000 | 1429,23993 | 753,14095 | 1677,75305 | €23,49 | €46,97 | €1,96 | €3,91 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | AVAX | LONG | Combo Adaptive | 60m | 2,0x | 11,18924 | 11,18924 | 10,58712 | 5,65056 | 12,99560 | €444,46 | €888,93 | €47,84 | €0,00 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | TAO | LONG | Combo Adaptive | 60m | 2,0x | 318,79375 | 318,79375 | 304,05530 | 160,99084 | 363,00907 | €525,17 | €1.050,33 | €48,56 | €0,00 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00001 | 0,00000 | 0,00000 | 0,00000 | 0,00001 | €406,62 | €813,23 | €48,29 | €-25,23 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | DOGE | LONG | Combo Adaptive | 60m | 2,0x | 0,09987 | 0,10282 | 0,09538 | 0,05043 | 0,11333 | €15,40 | €30,80 | €1,38 | €0,91 |
| Combo Adaptive — 75% a 2R + runner 25% a 3R | SNDK | LONG | Combo Adaptive | 60m | 2,0x | 1893,84869 | 1876,12000 | 1855,37474 | 956,39359 | 2009,27055 | €1.186,62 | €2.373,24 | €48,21 | €-22,22 |
| Combo Adaptive — target pieno 3R | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 1491,36821 | 1615,49000 | 1429,23993 | 753,14095 | 1677,75305 | €23,05 | €46,09 | €1,92 | €3,84 |
| Combo Adaptive — target pieno 3R | AVAX | LONG | Combo Adaptive | 60m | 2,0x | 11,18924 | 11,18924 | 10,58712 | 5,65056 | 12,99560 | €436,15 | €872,30 | €46,94 | €0,00 |
| Combo Adaptive — target pieno 3R | TAO | LONG | Combo Adaptive | 60m | 2,0x | 318,79375 | 318,79375 | 304,05530 | 160,99084 | 363,00907 | €515,34 | €1.030,68 | €47,65 | €0,00 |
| Combo Adaptive — target pieno 3R | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00001 | 0,00000 | 0,00000 | 0,00000 | 0,00001 | €399,01 | €798,02 | €47,39 | €-24,76 |
| Combo Adaptive — target pieno 3R | DOGE | LONG | Combo Adaptive | 60m | 2,0x | 0,09987 | 0,10282 | 0,09538 | 0,05043 | 0,11333 | €15,11 | €30,23 | €1,36 | €0,89 |
| Combo Adaptive — target pieno 3R | SNDK | LONG | Combo Adaptive | 60m | 2,0x | 1893,84869 | 1876,12000 | 1855,37474 | 956,39359 | 2009,27055 | €1.164,42 | €2.328,84 | €47,31 | €-21,80 |
| Btc Ema 1H | BTC | LONG | Trend following EMA | 60m | 3,0x | 85699,65650 | 86414,40000 | 84465,58145 | 57561,60262 | 88167,80661 | €1.082,60 | €3.247,81 | €46,77 | €27,09 |
| Sol Ema 4H | SOL | LONG | Trend following EMA | 240m | 2,0x | 116,97639 | 118,31400 | 112,00039 | 59,07308 | 129,41640 | €588,03 | €1.176,05 | €50,03 | €13,45 |
| Sol Adaptive 4H | SOL | LONG | Combo Adaptive | 240m | 2,0x | 116,97639 | 118,31400 | 111,54802 | 59,07308 | 130,54731 | €546,20 | €1.092,40 | €50,69 | €12,49 |
| Eth Ema 1H | ETH | LONG | Trend following EMA | 60m | 3,0x | 2732,80645 | 2758,42000 | 2690,74424 | 1835,53500 | 2816,93084 | €1.023,67 | €3.071,02 | €47,27 | €28,78 |
| Eth Ema 4H | ETH | LONG | Trend following EMA | 240m | 2,0x | 2772,42437 | 2758,42000 | 2670,54413 | 1400,07431 | 3027,12498 | €665,56 | €1.331,12 | €48,92 | €-6,72 |
| Doge Ema 1H | DOGE | LONG | Trend following EMA | 60m | 3,0x | 0,09987 | 0,10282 | 0,09538 | 0,06708 | 0,10885 | €377,85 | €1.133,54 | €50,94 | €33,48 |
| Doge Donchian 1H | DOGE | LONG | Donchian breakout 20 barre | 60m | 3,0x | 0,10083 | 0,10282 | 0,10142 | 0,06772 | 0,10608 | €654,30 | €1.962,91 | €0,00 | €38,74 |
| Doge Bollinger 1H | DOGE | SHORT | Bollinger mean reversion | 60m | 3,0x | 0,10280 | 0,10282 | 0,10544 | 0,13655 | 0,09884 | €630,89 | €1.892,66 | €48,55 | €-0,38 |
| Master Adaptive V1 | SUI | LONG | Master Adaptive Consensus | 60m | 2,0x | 1,00460 | 1,02650 | 0,95733 | 0,50732 | 1,09913 | €503,92 | €1.007,84 | €47,42 | €21,97 |
| Master Adaptive V1 | AVAX | LONG | Master Adaptive Consensus | 60m | 2,0x | 11,18924 | 11,18924 | 10,58712 | 5,65056 | 12,39348 | €440,55 | €881,10 | €47,41 | €0,00 |
| Master Adaptive V1 | TAO | LONG | Master Adaptive Consensus | 60m | 2,0x | 314,16282 | 314,16282 | 298,50384 | 158,65222 | 345,48079 | €25,77 | €51,55 | €2,57 | €0,00 |
| Master Adaptive V1 | PEPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00001 | €544,53 | €1.089,05 | €48,17 | €-18,59 |
| Master Adaptive V1 | SNDK | LONG | Master Adaptive Consensus | 60m | 2,0x | 1893,84869 | 1876,12000 | 1855,37476 | 956,39359 | 1970,79658 | €13,68 | €27,35 | €0,56 | €-0,26 |
| Master Adaptive V1 | UNI | LONG | Master Adaptive Consensus | 60m | 2,0x | 10,51710 | 10,82900 | 9,93401 | 5,31114 | 11,68328 | €403,08 | €806,16 | €44,69 | €23,91 |
| Master Adaptive V1 | ZEC | LONG | Master Adaptive Consensus | 60m | 2,0x | 1615,81310 | 1615,49000 | 1561,14547 | 815,98561 | 1725,14835 | €12,67 | €25,34 | €0,86 | €-0,01 |
| Master Adaptive No Alt V1 | TAO | LONG | Master Adaptive Consensus | 60m | 2,0x | 314,16282 | 314,16282 | 298,50384 | 158,65222 | 345,48079 | €421,99 | €843,98 | €42,07 | €0,00 |
| Master Adaptive No Alt V1 | DOGE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,09959 | 0,10282 | 0,09528 | 0,05029 | 0,10821 | €473,33 | €946,66 | €40,97 | €30,70 |
| Master Adaptive No Alt V1 | ZEC | LONG | Master Adaptive Consensus | 60m | 2,0x | 1617,23338 | 1615,49000 | 1560,60476 | 816,70286 | 1730,49063 | €586,64 | €1.173,29 | €41,08 | €-1,26 |
| Master Adaptive Strict3 V1 | TAO | LONG | Master Adaptive Consensus | 60m | 2,0x | 314,16282 | 314,16282 | 298,50384 | 158,65222 | 345,48079 | €423,74 | €847,47 | €42,24 | €0,00 |
| Master Adaptive Strict3 V1 | SNDK | LONG | Master Adaptive Consensus | 60m | 2,0x | 1846,65926 | 1876,12000 | 1798,66089 | 932,56293 | 1942,65599 | €811,89 | €1.623,79 | €42,21 | €25,91 |
| Master Adaptive Strict3 V1 | ZEC | LONG | Master Adaptive Consensus | 60m | 2,0x | 1617,23338 | 1615,49000 | 1560,60476 | 816,70286 | 1730,49063 | €604,86 | €1.209,72 | €42,36 | €-1,30 |
| Master Adaptive Strict3 V1 | XRP | LONG | Master Adaptive Consensus | 60m | 2,0x | 1,58978 | 1,58994 | 1,54525 | 0,80284 | 1,67883 | €756,11 | €1.512,21 | €42,35 | €0,15 |
| Master Adaptive Expanded V1 | SUI | LONG | Master Adaptive Consensus | 60m | 2,0x | 1,00460 | 1,02650 | 0,95733 | 0,50732 | 1,09913 | €493,53 | €987,06 | €46,44 | €21,52 |
| Master Adaptive Expanded V1 | AVAX | LONG | Master Adaptive Consensus | 60m | 2,0x | 11,18924 | 11,18924 | 10,58712 | 5,65056 | 12,39348 | €431,47 | €862,94 | €46,44 | €0,00 |
| Master Adaptive Expanded V1 | TAO | LONG | Master Adaptive Consensus | 60m | 2,0x | 314,16282 | 314,16282 | 298,50384 | 158,65222 | 345,48079 | €25,24 | €50,48 | €2,52 | €0,00 |
| Master Adaptive Expanded V1 | PEPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00001 | €533,30 | €1.066,60 | €47,17 | €-18,20 |
| Master Adaptive Expanded V1 | SNDK | LONG | Master Adaptive Consensus | 60m | 2,0x | 1893,84869 | 1876,12000 | 1855,37476 | 956,39359 | 1970,79658 | €13,39 | €26,79 | €0,54 | €-0,25 |
| Master Adaptive Expanded V1 | UNI | LONG | Master Adaptive Consensus | 60m | 2,0x | 10,51710 | 10,82900 | 9,93401 | 5,31114 | 11,68328 | €394,77 | €789,53 | €43,77 | €23,41 |
| Master Adaptive Expanded V1 | DOGE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,10284 | 0,10282 | 0,09968 | 0,05193 | 0,10917 | €13,64 | €27,28 | €0,84 | €-0,01 |
| Master Adaptive Gb20 V1 | SUI | LONG | Master Adaptive Consensus | 60m | 2,0x | 1,00460 | 1,02650 | 0,95733 | 0,50732 | 1,09913 | €497,27 | €994,54 | €46,79 | €21,68 |
| Master Adaptive Gb20 V1 | AVAX | LONG | Master Adaptive Consensus | 60m | 2,0x | 11,18924 | 11,18924 | 10,58712 | 5,65056 | 12,39348 | €434,74 | €869,48 | €46,79 | €0,00 |
| Master Adaptive Gb20 V1 | TAO | LONG | Master Adaptive Consensus | 60m | 2,0x | 314,16282 | 314,16282 | 298,50384 | 158,65222 | 345,48079 | €25,43 | €50,87 | €2,54 | €0,00 |
| Master Adaptive Gb20 V1 | PEPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00001 | €537,34 | €1.074,68 | €47,53 | €-18,34 |
| Master Adaptive Gb20 V1 | SNDK | LONG | Master Adaptive Consensus | 60m | 2,0x | 1893,84869 | 1876,12000 | 1855,37476 | 956,39359 | 1970,79658 | €13,50 | €26,99 | €0,55 | €-0,25 |
| Master Adaptive Gb20 V1 | UNI | LONG | Master Adaptive Consensus | 60m | 2,0x | 10,51710 | 10,82900 | 9,93401 | 5,31114 | 11,68328 | €397,76 | €795,52 | €44,11 | €23,59 |
| Master Adaptive Gb20 V1 | ZEC | LONG | Master Adaptive Consensus | 60m | 2,0x | 1615,81310 | 1615,49000 | 1561,14547 | 815,98561 | 1725,14835 | €12,50 | €25,01 | €0,85 | €-0,01 |
| Master Adaptive Runner25 V1 | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,21346 | 0,21346 | 0,19751 | 0,10780 | 0,26131 | €68,73 | €137,46 | €10,27 | €0,00 |
| Master Adaptive Runner25 V1 | SUI | LONG | Master Adaptive Consensus | 60m | 2,0x | 1,00460 | 1,02650 | 0,95733 | 0,50732 | 1,14640 | €510,15 | €1.020,30 | €48,00 | €22,24 |
| Master Adaptive Runner25 V1 | AVAX | LONG | Master Adaptive Consensus | 60m | 2,0x | 11,18924 | 11,18924 | 10,58712 | 5,65056 | 12,99560 | €437,29 | €874,58 | €47,06 | €0,00 |
| Master Adaptive Runner25 V1 | PEPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00001 | €553,97 | €1.107,95 | €49,00 | €-18,91 |
| Master Adaptive Runner25 V1 | SNDK | LONG | Master Adaptive Consensus | 60m | 2,0x | 1893,84869 | 1876,12000 | 1855,37476 | 956,39359 | 2009,27051 | €1.025,23 | €2.050,46 | €41,66 | €-19,19 |
| Combo Adaptive — Side × Regime Guard | AVAX | LONG | Combo Adaptive | 60m | 2,0x | 11,18924 | 11,18924 | 10,58712 | 5,65056 | 12,39348 | €503,86 | €1.007,72 | €54,23 | €0,00 |
| Combo Adaptive — Side × Regime Guard | DOGE | LONG | Combo Adaptive | 60m | 2,0x | 0,09987 | 0,10282 | 0,09538 | 0,05043 | 0,10885 | €593,33 | €1.186,65 | €53,33 | €35,05 |
| Combo Adaptive — Side × Regime Guard | XRP | LONG | Combo Adaptive | 60m | 2,0x | 1,57159 | 1,58994 | 1,52254 | 0,79366 | 1,66969 | €872,57 | €1.745,15 | €54,47 | €20,37 |
| Combo Adaptive — Side × Regime Guard | SNDK | LONG | Combo Adaptive | 60m | 2,0x | 1846,65926 | 1876,12000 | 1861,45820 | 932,56293 | 1942,65599 | €31,19 | €62,38 | €0,00 | €1,00 |
| Combo Adaptive — Side × Regime Guard | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00001 | €582,31 | €1.164,61 | €52,77 | €-1,35 |
| Combo Adaptive — Side × Regime Guard | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 1615,00294 | 1615,49000 | 1565,33023 | 815,57648 | 1714,34834 | €15,74 | €31,48 | €0,97 | €0,01 |
| Master Adaptive GB20 — Breakeven 0,5R | SUI | LONG | Master Adaptive Consensus | 60m | 2,0x | 1,00460 | 1,02650 | 0,95733 | 0,50732 | 1,09913 | €506,42 | €1.012,83 | €47,65 | €22,08 |
| Master Adaptive GB20 — Breakeven 0,5R | AVAX | LONG | Master Adaptive Consensus | 60m | 2,0x | 11,18924 | 11,18924 | 10,58712 | 5,65056 | 12,39348 | €442,73 | €885,47 | €47,65 | €0,00 |
| Master Adaptive GB20 — Breakeven 0,5R | TAO | LONG | Master Adaptive Consensus | 60m | 2,0x | 314,16282 | 314,16282 | 298,50384 | 158,65222 | 345,48079 | €25,90 | €51,80 | €2,58 | €0,00 |
| Master Adaptive GB20 — Breakeven 0,5R | PEPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00001 | €547,22 | €1.094,45 | €48,41 | €-18,68 |
| Master Adaptive GB20 — Breakeven 0,5R | SNDK | LONG | Master Adaptive Consensus | 60m | 2,0x | 1893,84869 | 1876,12000 | 1855,37476 | 956,39359 | 1970,79658 | €13,74 | €27,49 | €0,56 | €-0,26 |
| Master Adaptive GB20 — Breakeven 0,5R | UNI | LONG | Master Adaptive Consensus | 60m | 2,0x | 10,51710 | 10,82900 | 9,93401 | 5,31114 | 11,68328 | €405,07 | €810,15 | €44,92 | €24,03 |
| Master Adaptive GB20 — Breakeven 0,5R | ZEC | LONG | Master Adaptive Consensus | 60m | 2,0x | 1615,81310 | 1615,49000 | 1561,14547 | 815,98561 | 1725,14835 | €12,73 | €25,47 | €0,86 | €-0,01 |
| Master Adaptive GB20 — 50% a 0,75R | SUI | LONG | Master Adaptive Consensus | 60m | 2,0x | 1,00460 | 1,02650 | 0,95733 | 0,50732 | 1,09913 | €505,88 | €1.011,75 | €47,60 | €22,06 |
| Master Adaptive GB20 — 50% a 0,75R | AVAX | LONG | Master Adaptive Consensus | 60m | 2,0x | 11,18924 | 11,18924 | 10,58712 | 5,65056 | 12,39348 | €442,26 | €884,53 | €47,60 | €0,00 |
| Master Adaptive GB20 — 50% a 0,75R | TAO | LONG | Master Adaptive Consensus | 60m | 2,0x | 314,16282 | 314,16282 | 298,50384 | 158,65222 | 345,48079 | €25,87 | €51,75 | €2,58 | €0,00 |
| Master Adaptive GB20 — 50% a 0,75R | PEPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00001 | €546,64 | €1.093,28 | €48,36 | €-18,66 |
| Master Adaptive GB20 — 50% a 0,75R | SNDK | LONG | Master Adaptive Consensus | 60m | 2,0x | 1893,84869 | 1876,12000 | 1855,37476 | 956,39359 | 1970,79658 | €13,73 | €27,46 | €0,56 | €-0,26 |
| Master Adaptive GB20 — 50% a 0,75R | UNI | LONG | Master Adaptive Consensus | 60m | 2,0x | 10,51710 | 10,82900 | 9,93401 | 5,31114 | 11,68328 | €404,64 | €809,29 | €44,87 | €24,00 |
| Master Adaptive GB20 — 50% a 0,75R | ZEC | LONG | Master Adaptive Consensus | 60m | 2,0x | 1615,81310 | 1615,49000 | 1561,14547 | 815,98561 | 1725,14835 | €12,72 | €25,44 | €0,86 | €-0,01 |
| Master Adaptive GB20 — Loss Cap 0,75R | SUI | LONG | Master Adaptive Consensus | 60m | 2,0x | 1,00460 | 1,02650 | 0,96915 | 0,50732 | 1,09913 | €662,16 | €1.324,33 | €46,73 | €28,87 |
| Master Adaptive GB20 — Loss Cap 0,75R | TAO | LONG | Master Adaptive Consensus | 60m | 2,0x | 314,16282 | 314,16282 | 302,41858 | 158,65222 | 345,48079 | €46,01 | €92,01 | €3,44 | €0,00 |
| Master Adaptive GB20 — Loss Cap 0,75R | ZEC | LONG | Master Adaptive Consensus | 60m | 2,0x | 1621,03414 | 1615,49000 | 1578,32630 | 818,62224 | 1734,92171 | €892,44 | €1.784,88 | €47,02 | €-6,10 |
| Master Adaptive GB20 — Loss Cap 0,75R | PEPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00001 | €733,94 | €1.467,88 | €47,02 | €-23,05 |
| Master Adaptive GB20 — Loss Cap 0,75R | NEAR | LONG | Master Adaptive Consensus | 60m | 2,0x | 4,43189 | 4,34100 | 4,26824 | 2,23810 | 4,86827 | €593,55 | €1.187,09 | €43,83 | €-24,34 |
| Rapida V3 NoHigh — Regime Guard | SNDK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1883,32659 | 1876,12000 | 1845,86069 | 1264,96769 | 1939,52545 | €937,82 | €2.813,46 | €55,97 | €-10,77 |
| Rapida V3 NoHigh — Regime Guard | PEPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00001 | €544,13 | €1.632,39 | €56,16 | €-27,86 |
| Rapida V3 NoHigh — Regime Guard | SUI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,02701 | 1,02650 | 0,99976 | 0,68981 | 1,06787 | €704,63 | €2.113,89 | €56,08 | €-1,04 |
| Rapida V3 NoHigh — Regime Guard | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1615,81310 | 1615,49000 | 1573,29385 | 1085,28780 | 1679,59199 | €689,51 | €2.068,52 | €54,43 | €-0,41 |
| MAIN — Side × Regime Guard | NEAR | LONG | Confluenza trend | 240m | 3,0x | 4,12983 | 4,34100 | 3,70092 | 2,77387 | 4,98765 | €174,83 | €524,50 | €54,47 | €26,82 |
| MAIN — Side × Regime Guard | XMR | LONG | Confluenza trend | 240m | 3,0x | 582,85655 | 582,85655 | 534,94916 | 391,48531 | 678,67133 | €220,90 | €662,70 | €54,47 | €0,00 |
| MAIN — Side × Regime Guard | SUI | LONG | Confluenza trend | 240m | 3,0x | 1,03091 | 1,02650 | 0,95277 | 0,69243 | 1,18717 | €239,55 | €718,65 | €54,47 | €-3,07 |
| MAIN — Side × Regime Guard | PEPE | LONG | Confluenza trend | 240m | 3,0x | 0,00001 | 0,00000 | 0,00000 | 0,00000 | 0,00001 | €229,50 | €688,51 | €54,45 | €-13,79 |
| MAIN — Side × Regime Guard | XRP | LONG | Confluenza trend | 240m | 3,0x | 1,52135 | 1,58994 | 1,45004 | 1,02184 | 1,66397 | €10,94 | €32,83 | €1,54 | €1,48 |
| Combo Trend — Side × Regime Guard | ZEC | LONG | Combo Trend | 60m | 2,0x | 1478,71568 | 1615,49000 | 1402,15173 | 746,75142 | 1647,15637 | €542,53 | €1.085,06 | €56,18 | €100,36 |
| Combo Trend — Side × Regime Guard | TAO | LONG | Combo Trend | 60m | 2,0x | 310,99219 | 310,99219 | 294,26865 | 157,05105 | 347,78397 | €514,43 | €1.028,86 | €55,33 | €0,00 |
| Combo Trend — Side × Regime Guard | DOGE | LONG | Combo Trend | 60m | 2,0x | 0,10031 | 0,10282 | 0,09604 | 0,05066 | 0,10970 | €684,34 | €1.368,68 | €58,24 | €34,25 |
| Combo Trend — Side × Regime Guard | SNDK | LONG | Combo Trend | 60m | 2,0x | 1846,65926 | 1876,12000 | 1793,32774 | 932,56293 | 1963,98862 | €16,94 | €33,88 | €0,98 | €0,54 |
| Combo Trend — Side × Regime Guard | XRP | LONG | Combo Trend | 60m | 2,0x | 1,59083 | 1,58994 | 1,53918 | 0,80337 | 1,70446 | €850,12 | €1.700,24 | €55,20 | €-0,95 |
| Combo Trend — Side × Regime Guard | PEPE | LONG | Combo Trend | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00001 | €65,87 | €131,73 | €6,47 | €-2,25 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Master Adaptive GB20 — 50% a 0,75R | AKE | LONG | 2026-09-23T02:09:18+00:00 | 0,04814 | €-53,83 | -1,15 | STOP_GAP_STRESS_MARK_AFTER_GAP |
| Master Adaptive GB20 — Breakeven 0,5R | AKE | LONG | 2026-09-23T02:09:18+00:00 | 0,04814 | €-53,89 | -1,15 | STOP_GAP_STRESS_MARK_AFTER_GAP |
| Master Adaptive Gb20 V1 | AKE | LONG | 2026-09-23T02:09:18+00:00 | 0,04814 | €-52,92 | -1,15 | STOP_GAP_STRESS_MARK_AFTER_GAP |
| Master Adaptive Expanded V1 | AKE | LONG | 2026-09-23T02:09:18+00:00 | 0,04814 | €-52,52 | -1,15 | STOP_GAP_STRESS_MARK_AFTER_GAP |
| Master Adaptive No Alt V1 | AKE | LONG | 2026-09-23T02:09:18+00:00 | 0,04814 | €-48,05 | -1,15 | STOP_GAP_STRESS_MARK_AFTER_GAP |
| Master Adaptive V1 | AKE | LONG | 2026-09-23T02:09:18+00:00 | 0,04814 | €-53,62 | -1,15 | STOP_GAP_STRESS_MARK_AFTER_GAP |
| Bilanciata 1H V2 | ARB | LONG | 2026-09-23T02:09:18+00:00 | 0,24531 | €95,80 | 1,98 | TARGET_MARK_AFTER_GAP |
| Rapida V3 NoHigh — Regime Guard | ZEC | LONG | 2026-09-22T23:15:00+00:00 | 1587,61103 | €81,29 | 1,44 | TARGET |
| Combo Adaptive — Quality7 | ZEC | LONG | 2026-09-23T00:08:55+00:00 | 1616,20748 | €93,87 | 1,97 | TARGET_MARK_AFTER_GAP |
| Combo Adaptive — madre | ZEC | LONG | 2026-09-23T00:08:55+00:00 | 1616,20748 | €104,87 | 1,97 | TARGET_MARK_AFTER_GAP |
| Rapida 1H V2 | ZEC | LONG | 2026-09-22T23:15:00+00:00 | 1587,61103 | €76,59 | 1,44 | TARGET |
| Rapida score 6–7,5 — Cost Aware | ZEC | LONG | 2026-09-22T23:15:00+00:00 | 1587,61103 | €1,76 | 1,44 | TARGET |

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
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 914/30 | 33/30 | 0,90 | 2,04 | -0,05R | €9,09 | 2,01% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 861/30 | 20/30 | 0,87 | 1,90 | -0,06R | €11,76 | 2,73% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 427/30 | 22/30 | 1,03 | 1,74 | 0,02R | €12,35 | 1,72% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 436/30 | 22/30 | 0,98 | 1,57 | -0,01R | €8,43 | 2,27% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 785/30 | 31/30 | 0,96 | 0,62 | -0,02R | €-8,91 | 4,83% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 734/30 | 11/30 | 0,95 | 0,00 | -0,03R | €-38,20 | 4,20% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 244/30 | 8/30 | 0,90 | 1,02 | -0,05R | €0,42 | 2,15% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 597/30 | 17/30 | 0,87 | 4,50 | -0,07R | €14,07 | 1,01% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 828/30 | 24/30 | 0,85 | 0,64 | -0,07R | €-7,61 | 3,23% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 775/30 | 7/30 | 0,78 | 0,02 | -0,11R | €-33,97 | 2,82% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 785/30 | 30/30 | 0,98 | 1,02 | -0,01R | €0,30 | 4,84% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 1290/30 | 55/30 | 0,89 | 1,12 | -0,05R | €1,80 | 3,59% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 347/30 | 15/30 | 0,80 | 0,99 | -0,11R | €-0,32 | 2,70% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 1129/30 | 44/30 | 0,84 | 1,20 | -0,08R | €3,30 | 2,91% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 1133/30 | 37/30 | 0,84 | 0,76 | -0,08R | €-4,40 | 3,08% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 1061/30 | 23/30 | 0,80 | 1,12 | -0,10R | €2,12 | 3,05% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| MAIN | Principale 4H | 473/30 | 73/30 | 0,85 | 1,12 | -0,09R | €2,80 | 6,86% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| MAIN_DYNAMIC_ASSET_SELECTOR_V1 | MAIN — Dynamic Asset Selector | 0/30 | 26/30 | 0,00 | 1,36 | 0,00R | €10,16 | 3,39% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| MAIN_SIDE_REGIME_GUARD_V1 | MAIN — Side × Regime Guard | 0/30 | 65/30 | 0,00 | 1,77 | 0,00R | €13,76 | 8,55% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| RSI_EXTREME_LONG_15M | Scalp RSI Long 25 · prudente · 5x (riferimento tra 9 varianti) | 40/30 | 22/30 | 0,36 | 0,53 | -0,36R | €-2,69 | 0,73% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| RSI_EXTREME_SHORT_15M | Scalp RSI Short 75 · prudente · 5x (riferimento tra 9 varianti) | 58/30 | 35/30 | 0,87 | 0,86 | -0,07R | €-0,70 | 0,84% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_BALANCED | Bilanciata 1H V1 | 1270/30 | 234/30 | 0,90 | 0,82 | -0,05R | €-3,39 | 15,68% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_BALANCED_LONG_NO_RHV_V1 | Bilanciata 1H — LONG senza Range High Vol | 0/30 | 162/30 | 0,00 | 0,92 | 0,00R | €-1,34 | 9,26% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_BALANCED_SHORT_TREND_DOWN_STRICT_V1 | Bilanciata 1H — SHORT Trend Down stretto | 0/30 | 15/30 | 0,00 | 1,01 | 0,00R | €0,14 | 1,80% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_BALANCED_V2 | Bilanciata 1H V2 | 431/30 | 174/30 | 1,05 | 0,94 | 0,02R | €-1,21 | 11,82% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_BALANCED_V3 | Bilanciata 1H V3 Filtered | 826/30 | 239/30 | 0,97 | 1,10 | -0,02R | €1,72 | 14,04% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | Bilanciata V3 · LONG only | 747/30 | 194/30 | 0,93 | 0,95 | -0,04R | €-0,77 | 13,79% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST | Rapida 1H V1 — madre | 208/30 | 78/30 | 0,92 | 1,02 | -0,05R | €0,55 | 6,76% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | Rapida V1 — Long + BTC 1–3 + score <7,5 | 406/30 | 167/30 | 0,93 | 0,81 | -0,04R | €-4,76 | 13,09% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | FAST NoHigh <7,5 · SHORT only | 863/30 | 204/30 | 0,96 | 1,08 | -0,02R | €1,32 | 10,86% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | Rapida V1 — no HIGH + score <7,5 | 930/30 | 241/30 | 0,97 | 1,13 | -0,01R | €2,21 | 10,86% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_NO_PEPE_V1 | Rapida V1 — senza PEPE | 1452/30 | 330/30 | 0,87 | 1,20 | -0,07R | €3,14 | 9,28% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_SCORE_6_75_COST_AWARE_V1 | Rapida score 6–7,5 — Cost Aware | 0/30 | 242/30 | 0,00 | 1,35 | 0,00R | €6,76 | 7,95% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_SCORE_6_75_NO_TREND_UP_V1 | Rapida score 6–7,5 — senza Trend Up | 0/30 | 223/30 | 0,00 | 0,98 | 0,00R | €-0,44 | 15,94% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_SCORE_6_75_RANGE_ONLY_V1 | Rapida score 6–7,5 — Range Only | 0/30 | 77/30 | 0,00 | 1,11 | 0,00R | €2,28 | 6,49% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_SCORE_6_75_V1 | Rapida V1 — score 6–7,5 | 837/30 | 261/30 | 0,95 | 0,98 | -0,02R | €-0,53 | 15,64% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_TP2_V1 | Rapida V1 — target pieno 2R | 1402/30 | 306/30 | 0,84 | 1,19 | -0,08R | €3,08 | 6,56% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V2 | Rapida 1H V2 | 112/30 | 86/30 | 1,01 | 1,31 | 0,00R | €7,32 | 3,89% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3 | Rapida 1H V3 Filtered — madre | 1342/30 | 316/30 | 0,88 | 1,14 | -0,06R | €2,51 | 9,48% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_CAP75_V1 | Rapida V3 — score <7,5 | 1029/30 | 281/30 | 0,92 | 0,91 | -0,04R | €-1,94 | 19,03% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | Rapida V3 — qualità completa + profit lock | 485/30 | 206/30 | 1,08 | 0,98 | 0,04R | €-0,47 | 8,44% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | Rapida V3 — Long + no HIGH + score <7,5 | 493/30 | 208/30 | 1,02 | 0,98 | 0,01R | €-0,52 | 6,64% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | Rapida V3 — Long Only | 889/30 | 309/30 | 0,98 | 1,01 | -0,01R | €0,13 | 12,52% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V1 | Rapida V3 NoHigh — Range Only | 0/30 | 121/30 | 0,00 | 1,08 | 0,00R | €1,70 | 7,07% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_V1 | Rapida V3 NoHigh — Regime Guard | 0/30 | 212/30 | 0,00 | 1,35 | 0,00R | €5,26 | 5,24% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | Rapida V3 — no volatilità HIGH | 969/30 | 235/30 | 0,90 | 1,12 | -0,05R | €1,83 | 7,10% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONLY_V1 | Rapida V3 senza ESPORTS — Long Only | 0/30 | 306/30 | 0,00 | 1,07 | 0,00R | €1,33 | 10,60% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_V1 | Rapida V3 senza ESPORTS — MFE Lock | 0/30 | 272/30 | 0,00 | 1,20 | 0,00R | €3,17 | 9,50% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_GUARD_V1 | Rapida V3 senza ESPORTS — Stress Guard | 0/30 | 194/30 | 0,00 | 1,38 | 0,00R | €7,36 | 5,29% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | Rapida V3 — senza ESPORTS | 1295/30 | 279/30 | 0,86 | 1,03 | -0,07R | €0,66 | 10,92% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_4H_WIDE | Ampia 4H | 441/30 | 71/30 | 0,87 | 1,24 | -0,08R | €5,37 | 4,45% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_BOLLINGER_MR_1H | Benchmark Bollinger mean reversion 1H | 436/30 | 156/30 | 1,02 | 0,51 | 0,01R | €-15,58 | 26,04% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_BTC_ADAPTIVE_1H | Btc Adaptive 1H | 20/30 | 14/30 | 0,65 | 0,80 | -0,18R | €-4,65 | 2,06% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_BTC_ADAPTIVE_4H | Btc Adaptive 4H | 4/30 | 4/30 | 0,76 | 0,77 | -0,19R | €-8,79 | 1,10% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_BTC_BOLLINGER_1H | Btc Bollinger 1H | 12/30 | 9/30 | 2,57 | 2,77 | 0,45R | €22,61 | 0,85% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_BTC_BOLLINGER_4H | Btc Bollinger 4H | 4/30 | 4/30 | 2,81 | 2,86 | 0,50R | €25,47 | 0,91% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_BTC_DONCHIAN_1H | Btc Donchian 1H | 23/30 | 16/30 | 0,40 | 0,85 | -0,42R | €-3,76 | 1,98% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_BTC_DONCHIAN_4H | Btc Donchian 4H | 9/30 | 7/30 | 0,32 | 0,41 | -0,65R | €-27,30 | 2,43% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_BTC_EMA_1H | Btc Ema 1H | 34/30 | 28/30 | 0,52 | 0,36 | -0,32R | €-23,08 | 6,59% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_BTC_EMA_4H | Btc Ema 4H | 6/30 | 5/30 | 0,45 | 0,58 | -0,49R | €-17,17 | 1,76% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE | Combo Adaptive — madre | 1063/30 | 251/30 | 0,97 | 1,31 | -0,01R | €4,41 | 8,17% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | Combo Adaptive — Long Only | 697/30 | 207/30 | 1,02 | 1,26 | 0,01R | €4,41 | 7,78% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | Combo Adaptive — MFE Trail esistente | 1195/30 | 255/30 | 0,99 | 0,84 | -0,01R | €-2,70 | 15,45% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | Combo Adaptive — parziale 1R | 1004/30 | 208/30 | 0,95 | 1,23 | -0,03R | €3,29 | 8,69% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | Combo Adaptive — Quality7 + Regime + parziale 1R | 106/30 | 62/30 | 1,30 | 0,86 | 0,13R | €-3,42 | 4,27% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | Combo Adaptive — Quality7 + Regime | 106/30 | 62/30 | 1,25 | 0,78 | 0,11R | €-5,40 | 5,41% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | Combo Adaptive — Quality7 | 378/30 | 121/30 | 0,91 | 0,92 | -0,05R | €-1,98 | 8,88% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | Combo Adaptive — Trend/Transition | 304/30 | 99/30 | 1,01 | 0,80 | 0,00R | €-4,69 | 6,28% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | Combo Adaptive — 75% a 2R + runner 25% a 3R | 47/30 | 178/30 | 0,74 | 0,95 | -0,20R | €-0,91 | 14,10% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_SIDE_REGIME_GUARD_V1 | Combo Adaptive — Side × Regime Guard | 0/30 | 203/30 | 0,00 | 1,25 | 0,00R | €4,09 | 11,68% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | Combo Adaptive — target pieno 3R | 47/30 | 158/30 | 0,74 | 0,88 | -0,20R | €-2,19 | 14,10% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_MEAN_REVERSION | Combo Mean Reversion | 164/30 | 88/30 | 1,02 | 0,55 | 0,01R | €-15,69 | 16,26% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_SCANNER | Combo Scanner | 681/30 | 211/30 | 1,04 | 1,15 | 0,02R | €2,86 | 11,38% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_TREND | Combo Trend | 879/30 | 210/30 | 0,98 | 0,94 | -0,01R | €-1,20 | 14,08% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_COMBO_TREND_SIDE_REGIME_GUARD_V1 | Combo Trend — Side × Regime Guard | 0/30 | 176/30 | 0,00 | 1,48 | 0,00R | €8,62 | 10,10% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_DOGE_BOLLINGER_1H | Doge Bollinger 1H | 23/30 | 20/30 | 0,93 | 0,53 | -0,03R | €-14,51 | 3,66% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_DOGE_DONCHIAN_1H | Doge Donchian 1H | 27/30 | 21/30 | 0,81 | 1,45 | -0,12R | €10,03 | 3,08% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_DOGE_EMA_1H | Doge Ema 1H | 45/30 | 32/30 | 0,64 | 1,29 | -0,22R | €5,87 | 2,77% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_DONCHIAN_1H | Benchmark Donchian breakout 1H | 464/30 | 180/30 | 0,95 | 1,71 | -0,03R | €14,50 | 6,75% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | Donchian 1H Gb20 120R V1 | 394/30 | 148/30 | 0,97 | 1,84 | -0,02R | €15,63 | 6,75% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_EMA_TREND_1H | Benchmark trend following EMA 1H | 893/30 | 175/30 | 0,94 | 1,05 | -0,03R | €0,82 | 12,31% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_ETH_ADAPTIVE_1H | Eth Adaptive 1H | 37/30 | 27/30 | 0,56 | 0,40 | -0,31R | €-21,89 | 5,95% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_ETH_BOLLINGER_1H | Eth Bollinger 1H | 21/30 | 12/30 | 2,42 | 0,70 | 0,45R | €-10,99 | 4,16% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_ETH_DONCHIAN_1H | Eth Donchian 1H | 33/30 | 24/30 | 0,68 | 0,57 | -0,22R | €-15,67 | 4,65% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_ETH_EMA_1H | Eth Ema 1H | 51/30 | 36/30 | 0,50 | 0,55 | -0,35R | €-15,18 | 5,88% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_ETH_EMA_4H | Eth Ema 4H | 9/30 | 9/30 | 0,58 | 0,41 | -0,25R | €-24,10 | 2,54% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_GLOBAL_PURE | Global Confluence puro 1H | 21/30 | 23/30 | 1,00 | 0,66 | -0,00R | €-9,57 | 3,93% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | Master Adaptive Expanded V1 | 457/30 | 108/30 | 1,07 | 0,78 | 0,05R | €-5,91 | 10,41% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_MASTER_ADAPTIVE_GB20_BE_V1 | Master Adaptive GB20 — Breakeven 0,5R | 0/30 | 133/30 | 0,00 | 0,89 | 0,00R | €-2,96 | 10,08% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_MASTER_ADAPTIVE_GB20_LOSS_CAP_V1 | Master Adaptive GB20 — Loss Cap 0,75R | 0/30 | 124/30 | 0,00 | 0,83 | 0,00R | €-4,99 | 12,05% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_MASTER_ADAPTIVE_GB20_PARTIAL_V1 | Master Adaptive GB20 — 50% a 0,75R | 0/30 | 128/30 | 0,00 | 0,88 | 0,00R | €-3,15 | 9,87% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | Master Adaptive Gb20 V1 | 869/30 | 164/30 | 1,23 | 0,85 | 0,08R | €-3,46 | 10,69% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | Master Adaptive No Alt V1 | 363/30 | 130/30 | 1,01 | 0,58 | 0,01R | €-13,61 | 17,99% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | Master Adaptive Runner25 V1 | 419/30 | 116/30 | 1,09 | 0,93 | 0,06R | €-1,90 | 9,31% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | Master Adaptive Strict3 V1 | 259/30 | 91/30 | 0,91 | 0,57 | -0,06R | €-17,11 | 16,25% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_MASTER_ADAPTIVE_V1 | Master Adaptive V1 | 438/30 | 130/30 | 1,07 | 0,88 | 0,04R | €-3,39 | 9,87% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_RELATIVE_STRENGTH | Forza relativa 1H V1 | 1053/30 | 197/30 | 0,90 | 0,71 | -0,05R | €-5,57 | 19,11% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_RELATIVE_STRENGTH_V2 | Forza relativa 1H V2 | 411/30 | 151/30 | 1,03 | 1,07 | 0,01R | €1,63 | 10,88% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_BOTTOM10_SHORT | Scanner Bottom10 Short | 345/30 | 76/30 | 0,57 | 0,76 | -0,25R | €-6,17 | 9,06% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_BOTTOM15_SHORT | Scanner Bottom15 Short | 345/30 | 76/30 | 0,57 | 0,76 | -0,25R | €-6,17 | 9,06% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_BOTTOM20_SHORT | Scanner Bottom20 Short | 345/30 | 76/30 | 0,57 | 0,76 | -0,25R | €-6,17 | 9,06% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_BOTTOM5_SHORT | Scanner Bottom 5 Short 1H | 365/30 | 95/30 | 0,68 | 0,73 | -0,18R | €-6,55 | 10,17% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_BOTTOM5_SHORT_CONTINUATION_V1 | Scanner Bottom5 Short Continuation V1 | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | Scanner Bottom5 Short Mfe Trail V1 | 414/30 | 67/30 | 0,77 | 0,71 | -0,10R | €-7,99 | 9,08% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | Scanner Bottom5 Short Profit Lock V1 | 372/30 | 68/30 | 0,71 | 0,69 | -0,13R | €-8,08 | 9,08% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP10_LONG | Scanner Top10 Long | 707/30 | 222/30 | 1,00 | 1,11 | -0,00R | €1,63 | 10,31% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP15_LONG | Scanner Top15 Long | 710/30 | 240/30 | 1,00 | 1,22 | 0,00R | €3,34 | 10,31% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP20_LONG | Scanner Top20 Long | 710/30 | 240/30 | 1,00 | 1,22 | 0,00R | €3,34 | 10,31% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC | Scanner Top 5 + forza BTC 1H | 654/30 | 179/30 | 1,04 | 1,18 | 0,02R | €3,45 | 11,27% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | Top 5 + BTC — BTC 2–3 | 231/30 | 72/30 | 0,70 | 0,64 | -0,18R | €-10,14 | 12,43% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | Top 5 + BTC — BTC≤3 | 486/30 | 144/30 | 0,85 | 0,64 | -0,08R | €-8,99 | 20,25% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | Top 5 + BTC — Guard + BTC≤3 + MFE | 529/30 | 167/30 | 1,00 | 0,72 | 0,00R | €-7,55 | 18,17% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | Top 5 + BTC — Guard + BTC≤3 | 437/30 | 144/30 | 0,90 | 0,78 | -0,05R | €-5,75 | 16,24% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | Top 5 + BTC — Guard + MFE | 686/30 | 195/30 | 1,06 | 0,92 | 0,03R | €-1,68 | 8,78% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | Top 5 + BTC — Guard | 558/30 | 182/30 | 1,03 | 0,96 | 0,02R | €-0,78 | 7,34% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | Top 5 + BTC — solo MFE | 757/30 | 171/30 | 1,00 | 0,99 | 0,00R | €-0,28 | 12,28% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | Top 5 + BTC — 75% a 2,2R + runner 3R | 601/30 | 190/30 | 0,99 | 0,98 | -0,00R | €-0,53 | 12,06% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | Top 5 + BTC — target pieno 3R | 573/30 | 186/30 | 1,01 | 0,98 | 0,01R | €-0,51 | 11,91% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SCANNER_TOP5_LONG | Scanner Top 5 Long 1H | 716/30 | 214/30 | 1,05 | 1,31 | 0,03R | €5,51 | 8,85% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SOL_ADAPTIVE_1H | Sol Adaptive 1H | 48/30 | 31/30 | 0,98 | 1,05 | -0,01R | €1,32 | 4,59% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SOL_ADAPTIVE_4H | Sol Adaptive 4H | 12/30 | 10/30 | 1,78 | 1,64 | 0,34R | €13,87 | 1,43% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SOL_BOLLINGER_1H | Sol Bollinger 1H | 34/30 | 22/30 | 0,68 | 0,58 | -0,19R | €-15,05 | 3,69% | COERENTE − | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SOL_BOLLINGER_4H | Sol Bollinger 4H | 8/30 | 5/30 | 1,24 | 0,88 | 0,12R | €-3,80 | 1,96% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SOL_DONCHIAN_1H | Sol Donchian 1H | 39/30 | 25/30 | 1,25 | 1,88 | 0,12R | €14,88 | 2,77% | COERENTE + | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SOL_DONCHIAN_4H | Sol Donchian 4H | 11/30 | 9/30 | 0,85 | 1,15 | -0,10R | €4,46 | 2,25% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SOL_EMA_1H | Sol Ema 1H | 49/30 | 33/30 | 0,98 | 1,00 | -0,01R | €0,08 | 4,45% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |
| SHADOW_SOL_EMA_4H | Sol Ema 4H | 13/30 | 11/30 | 0,80 | 1,02 | -0,13R | €0,50 | 2,27% | DIVERGENTE | RESEARCH NON ELIGIBILE · EVIDENCE GATE |

Per le famiglie RSI con più configurazioni di leva o margine, il lato paper usa il conto con il maggior numero di eventi indipendenti; i conti duplicati non vengono aggregati.
`PRONTA PER REVISIONE LIVE` non invia ordini e non sposta capitale: abilita soltanto una revisione manuale finale.

## 🎯 DOGE Rejection Short — conto dedicato €3.600

Simulazione separata **paper only**: capitale/margine iniziale **€3.600**, leva **5x**, esposizione iniziale **€18.000**. Non modifica i conti paper da €10.000 e non invia ordini reali.

- Stato: **INVALIDATED**
- Prezzo DOGE: **0.10282**
- Pre-allarme: **0.0765**; zona armata: **0.0775**; trigger rejection: **0.078**
- Invalidazione prima dell’entrata: chiusura 15m sopra **0.07966**

| Capitale iniziale | Balance | Equity | P&L aperto | Eventi chiusi | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- |
| €3.600,00 | €3.600,00 | €3.600,00 | €0,00 | 0 | 0,00% | 0,00 | 0,00% |

### Filtri correnti

| Filtro | Valore | Stato |
| --- | --- | --- |
| Dati mercato | FRESH | OK |
| Candela 15m | 29.4 min | OK |
| Global DOGE | -6.0 | OK |
| Classic raw | -11.0 | OK |
| DOGE/BTC raw | -6.0 | OK |
| Pattern ribassista | MATURO | OK |
| BTC sotto filtro | 86414.4 | NO |

### Ultima candela 15m valutata

- Rejection accettata: **NO**; motivo: **closed_back_below_trigger, close_below_invalidation, entry_not_chased, upper_wick, bearish_confirmation, volume_valid, stop_within_limit**
- High **0.10376**; close **0.10344**; wick alta **16.1%**; volume **x3.04**

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
Campioni separati per causal/evidence generation: LEGACY_PRE_CAUSAL_V3=548; LEGACY_RESEARCH_EVIDENCE_V3=22715; UNKNOWN_EVIDENCE_GENERATION=31764

Registro parallelo senza limite globale di quattro posizioni. Considera soltanto segnali validi con dati freschi; non modifica i conti paper e non genera ordini reali.

### Regime di mercato osservato

- Regime: **ALT_ROTATION_UP**
- Famiglia: **ALT_ROTATION**
- Confidenza: **90,00%**
- Volatilità: **NORMAL**
- Rotazione strategie: **SOLO OSSERVAZIONE — nessun peso operativo viene ancora modificato**
- Motivo: Le altcoin stanno sovraperformando BTC: mediana relativa +3.58%, 55% oltre +1%.
- BTC trend score: **3,00**; ADX: **50,38**; breadth sopra EMA50: **100,00%**
- Mediana alt vs BTC: **3,58%**; dispersione: **5,93%**

- Aperti in questo ciclo: **48**
- Chiusi in questo ciclo: **0**
- Posizioni research aperte: **1607**
- Trade research chiusi: **53718**
- Eventi di mercato indipendenti chiusi: **7040**
- Segnali sovrapposti saltati sullo stesso asset/profilo: **148015**
- Posizioni Research V1 senza regime scartate durante la migrazione: **28**

### Risultati complessivi per strategia

| Profilo | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | 26 | 914 | 914 | 37,96% | 0,90 | -0,05R | €-442,50 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | 25 | 861 | 861 | 37,51% | 0,87 | -0,06R | €-547,42 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | 16 | 427 | 427 | 51,29% | 1,03 | 0,02R | €70,57 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | 17 | 436 | 436 | 38,99% | 0,98 | -0,01R | €-48,97 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | 20 | 785 | 785 | 38,60% | 0,96 | -0,02R | €-150,54 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | 20 | 734 | 734 | 38,83% | 0,95 | -0,03R | €-192,02 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | 2 | 244 | 244 | 39,34% | 0,90 | -0,05R | €-116,28 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | 19 | 597 | 597 | 37,35% | 0,87 | -0,07R | €-398,07 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | 24 | 828 | 828 | 36,11% | 0,85 | -0,07R | €-613,75 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | 24 | 775 | 775 | 35,35% | 0,78 | -0,11R | €-849,54 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | 20 | 785 | 785 | 38,85% | 0,98 | -0,01R | €-90,88 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | 26 | 1290 | 1290 | 41,71% | 0,89 | -0,05R | €-642,06 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | 10 | 347 | 347 | 40,63% | 0,80 | -0,11R | €-373,52 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | 28 | 1129 | 1129 | 36,05% | 0,84 | -0,08R | €-892,34 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | 28 | 1133 | 1133 | 36,01% | 0,84 | -0,08R | €-892,87 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | 28 | 1061 | 1061 | 35,53% | 0,80 | -0,10R | €-1048,03 |
| MAIN | 31 | 473 | 473 | 31,92% | 0,85 | -0,09R | €-417,68 |
| RSI_EXTREME_LONG_15M | 0 | 40 | 40 | 37,50% | 0,36 | -0,36R | €-145,44 |
| RSI_EXTREME_SHORT_15M | 0 | 58 | 58 | 43,10% | 0,87 | -0,07R | €-38,08 |
| Bilanciata 1H V1 | 36 | 1270 | 1270 | 38,66% | 0,90 | -0,05R | €-688,04 |
| Bilanciata 1H V2 | 19 | 496 | 431 | 42,14% | 1,05 | 0,02R | €122,38 |
| Bilanciata 1H V3 Filtered | 27 | 826 | 826 | 39,95% | 0,97 | -0,02R | €-130,38 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | 27 | 747 | 747 | 40,03% | 0,93 | -0,04R | €-275,72 |
| Rapida 1H V1 | 0 | 208 | 208 | 38,94% | 0,92 | -0,05R | €-101,45 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | 12 | 406 | 406 | 39,66% | 0,93 | -0,04R | €-144,31 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | 25 | 863 | 863 | 40,09% | 0,96 | -0,02R | €-162,35 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | 25 | 930 | 930 | 40,32% | 0,97 | -0,01R | €-128,02 |
| SHADOW_1H_FAST_NO_PEPE_V1 | 31 | 1452 | 1452 | 38,15% | 0,87 | -0,07R | €-990,50 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | 22 | 837 | 837 | 40,26% | 0,95 | -0,02R | €-206,82 |
| SHADOW_1H_FAST_TP2_V1 | 32 | 1402 | 1402 | 36,16% | 0,84 | -0,08R | €-1116,90 |
| Rapida 1H V2 | 0 | 127 | 112 | 45,67% | 1,01 | 0,00R | €5,29 |
| Rapida 1H V3 Filtered | 28 | 1342 | 1342 | 38,38% | 0,88 | -0,06R | €-818,44 |
| SHADOW_1H_FAST_V3_CAP75_V1 | 25 | 1029 | 1029 | 39,94% | 0,92 | -0,04R | €-413,31 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | 16 | 485 | 485 | 51,55% | 1,08 | 0,04R | €186,46 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | 16 | 493 | 493 | 40,97% | 1,02 | 0,01R | €52,75 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | 20 | 889 | 889 | 40,61% | 0,98 | -0,01R | €-88,54 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | 24 | 969 | 969 | 38,18% | 0,90 | -0,05R | €-504,94 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | 28 | 1295 | 1295 | 38,07% | 0,86 | -0,07R | €-900,40 |
| SHADOW_4H_WIDE | 42 | 441 | 441 | 26,53% | 0,87 | -0,08R | €-348,53 |
| SHADOW_BOLLINGER_MR_1H | 4 | 436 | 436 | 47,71% | 1,02 | 0,01R | €35,33 |
| SHADOW_BTC_ADAPTIVE_1H | 0 | 20 | 20 | 50,00% | 0,65 | -0,18R | €-35,17 |
| SHADOW_BTC_ADAPTIVE_4H | 0 | 4 | 4 | 25,00% | 0,76 | -0,19R | €-7,44 |
| SHADOW_BTC_BOLLINGER_1H | 0 | 12 | 12 | 75,00% | 2,57 | 0,45R | €53,43 |
| SHADOW_BTC_BOLLINGER_4H | 0 | 4 | 4 | 75,00% | 2,81 | 0,50R | €19,94 |
| SHADOW_BTC_DONCHIAN_1H | 0 | 23 | 23 | 34,78% | 0,40 | -0,42R | €-95,85 |
| SHADOW_BTC_DONCHIAN_4H | 0 | 9 | 9 | 11,11% | 0,32 | -0,65R | €-58,49 |
| SHADOW_BTC_EMA_1H | 1 | 34 | 34 | 38,24% | 0,52 | -0,32R | €-109,09 |
| SHADOW_BTC_EMA_4H | 0 | 6 | 6 | 16,67% | 0,45 | -0,49R | €-29,19 |
| SHADOW_COMBO_ADAPTIVE | 29 | 1063 | 1063 | 41,39% | 0,97 | -0,01R | €-156,57 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | 20 | 697 | 697 | 42,90% | 1,02 | 0,01R | €86,72 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | 29 | 1195 | 1195 | 41,26% | 0,99 | -0,01R | €-75,86 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | 29 | 1004 | 1004 | 43,13% | 0,95 | -0,03R | €-268,02 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | 4 | 106 | 106 | 48,11% | 1,30 | 0,13R | €135,16 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | 4 | 106 | 106 | 43,40% | 1,25 | 0,11R | €112,62 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | 18 | 378 | 378 | 40,74% | 0,91 | -0,05R | €-173,82 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | 8 | 304 | 304 | 41,78% | 1,01 | 0,00R | €14,16 |
| SHADOW_COMBO_ADAPTIVE_RUNNER25_V1 | 0 | 47 | 47 | 19,15% | 0,74 | -0,20R | €-92,41 |
| SHADOW_COMBO_ADAPTIVE_TP3_V1 | 0 | 47 | 47 | 19,15% | 0,74 | -0,20R | €-92,41 |
| SHADOW_COMBO_MEAN_REVERSION | 1 | 164 | 164 | 46,95% | 1,02 | 0,01R | €19,65 |
| SHADOW_COMBO_SCANNER | 23 | 681 | 681 | 40,38% | 1,04 | 0,02R | €137,78 |
| SHADOW_COMBO_TREND | 31 | 879 | 879 | 38,57% | 0,98 | -0,01R | €-80,60 |
| SHADOW_DOGE_BOLLINGER_1H | 1 | 23 | 23 | 52,17% | 0,93 | -0,03R | €-7,71 |
| SHADOW_DOGE_DONCHIAN_1H | 1 | 27 | 27 | 44,44% | 0,81 | -0,12R | €-31,49 |
| SHADOW_DOGE_EMA_1H | 1 | 45 | 45 | 37,78% | 0,64 | -0,22R | €-98,69 |
| SHADOW_DONCHIAN_1H | 10 | 464 | 464 | 37,50% | 0,95 | -0,03R | €-137,83 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | 10 | 394 | 394 | 39,59% | 0,97 | -0,02R | €-72,75 |
| SHADOW_EMA_TREND_1H | 34 | 893 | 893 | 37,74% | 0,94 | -0,03R | €-288,82 |
| SHADOW_ETH_ADAPTIVE_1H | 0 | 37 | 37 | 35,14% | 0,56 | -0,31R | €-116,14 |
| SHADOW_ETH_BOLLINGER_1H | 0 | 21 | 21 | 66,67% | 2,42 | 0,45R | €94,65 |
| SHADOW_ETH_DONCHIAN_1H | 0 | 33 | 33 | 36,36% | 0,68 | -0,22R | €-71,35 |
| SHADOW_ETH_EMA_1H | 1 | 51 | 51 | 35,29% | 0,50 | -0,35R | €-176,44 |
| SHADOW_ETH_EMA_4H | 1 | 9 | 9 | 44,44% | 0,58 | -0,25R | €-22,36 |
| SHADOW_GLOBAL_PURE | 0 | 21 | 21 | 47,62% | 1,00 | -0,00R | €-0,01 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | 21 | 457 | 457 | 35,23% | 1,07 | 0,05R | €211,42 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | 19 | 869 | 869 | 65,82% | 1,23 | 0,08R | €656,70 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | 15 | 363 | 363 | 33,33% | 1,01 | 0,01R | €21,53 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | 21 | 419 | 419 | 34,84% | 1,09 | 0,06R | €239,18 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | 11 | 259 | 259 | 31,27% | 0,91 | -0,06R | €-150,27 |
| SHADOW_MASTER_ADAPTIVE_V1 | 21 | 438 | 438 | 35,16% | 1,07 | 0,04R | €192,19 |
| Forza relativa 1H V1 | 36 | 1053 | 1053 | 35,33% | 0,90 | -0,05R | €-577,31 |
| Forza relativa 1H V2 | 26 | 444 | 411 | 38,51% | 1,03 | 0,01R | €63,62 |
| SHADOW_SCANNER_BOTTOM10_SHORT | 9 | 345 | 345 | 31,30% | 0,57 | -0,25R | €-852,04 |
| SHADOW_SCANNER_BOTTOM15_SHORT | 9 | 345 | 345 | 31,30% | 0,57 | -0,25R | €-852,04 |
| SHADOW_SCANNER_BOTTOM20_SHORT | 9 | 345 | 345 | 31,30% | 0,57 | -0,25R | €-852,04 |
| SHADOW_SCANNER_BOTTOM5_SHORT | 9 | 365 | 365 | 32,05% | 0,68 | -0,18R | €-662,32 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | 9 | 414 | 414 | 53,86% | 0,77 | -0,10R | €-428,37 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | 9 | 372 | 372 | 52,96% | 0,71 | -0,13R | €-491,15 |
| SHADOW_SCANNER_TOP10_LONG | 26 | 707 | 707 | 41,58% | 1,00 | -0,00R | €-1,73 |
| SHADOW_SCANNER_TOP15_LONG | 26 | 710 | 710 | 41,69% | 1,00 | 0,00R | €4,28 |
| SHADOW_SCANNER_TOP20_LONG | 26 | 710 | 710 | 41,69% | 1,00 | 0,00R | €4,28 |
| SHADOW_SCANNER_TOP5_BTC | 23 | 654 | 654 | 39,91% | 1,04 | 0,02R | €135,06 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | 15 | 231 | 231 | 34,20% | 0,70 | -0,18R | €-422,81 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | 20 | 486 | 486 | 36,42% | 0,85 | -0,08R | €-410,50 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | 16 | 529 | 529 | 43,29% | 1,00 | 0,00R | €6,96 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | 17 | 437 | 437 | 37,99% | 0,90 | -0,05R | €-232,96 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | 21 | 686 | 686 | 44,17% | 1,06 | 0,03R | €179,62 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | 21 | 558 | 558 | 40,68% | 1,03 | 0,02R | €94,09 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | 23 | 757 | 757 | 43,20% | 1,00 | 0,00R | €13,01 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | 23 | 601 | 601 | 39,27% | 0,99 | -0,00R | €-29,75 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | 23 | 573 | 573 | 38,92% | 1,01 | 0,01R | €41,26 |
| SHADOW_SCANNER_TOP5_LONG | 22 | 716 | 716 | 41,20% | 1,05 | 0,03R | €182,06 |
| SHADOW_SOL_ADAPTIVE_1H | 0 | 48 | 48 | 43,75% | 0,98 | -0,01R | €-6,90 |
| SHADOW_SOL_ADAPTIVE_4H | 1 | 12 | 12 | 58,33% | 1,78 | 0,34R | €40,79 |
| SHADOW_SOL_BOLLINGER_1H | 0 | 34 | 34 | 44,12% | 0,68 | -0,19R | €-64,07 |
| SHADOW_SOL_BOLLINGER_4H | 0 | 8 | 8 | 50,00% | 1,24 | 0,12R | €9,94 |
| SHADOW_SOL_DONCHIAN_1H | 0 | 39 | 39 | 53,85% | 1,25 | 0,12R | €48,25 |
| SHADOW_SOL_DONCHIAN_4H | 0 | 11 | 11 | 36,36% | 0,85 | -0,10R | €-10,82 |
| SHADOW_SOL_EMA_1H | 0 | 49 | 49 | 40,82% | 0,98 | -0,01R | €-6,35 |
| SHADOW_SOL_EMA_4H | 1 | 13 | 13 | 38,46% | 0,80 | -0,13R | €-16,87 |

### Matrice strategia × regime all’entrata

| Profilo | Regime entrata | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | ALT_ROTATION_DOWN | 3 | 130 | 130 | 32,31% | 0,65 | -0,19R | €-249,52 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | ALT_ROTATION_UP | 12 | 268 | 268 | 45,15% | 1,12 | 0,05R | €142,94 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | RANGE | 4 | 208 | 208 | 41,35% | 0,98 | -0,01R | €-18,44 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | RANGE_HIGH_VOL | 1 | 49 | 49 | 26,53% | 0,30 | -0,45R | €-220,07 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | RANGE_LOW_VOL | 1 | 7 | 7 | 71,43% | 2,09 | 0,32R | €22,14 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TRANSITION | 0 | 68 | 68 | 36,76% | 1,38 | 0,16R | €105,93 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_DOWN | 0 | 60 | 60 | 26,67% | 0,55 | -0,26R | €-153,33 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_DOWN_HIGH_VOL | 1 | 6 | 6 | 16,67% | 0,14 | -0,47R | €-28,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_UP | 4 | 72 | 72 | 20,83% | 0,47 | -0,28R | €-200,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R200_86882aa9 | TREND_UP_HIGH_VOL | 0 | 46 | 46 | 50,00% | 1,89 | 0,34R | €156,05 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | ALT_ROTATION_DOWN | 3 | 120 | 120 | 31,67% | 0,57 | -0,25R | €-302,47 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | ALT_ROTATION_UP | 11 | 249 | 249 | 43,78% | 1,12 | 0,06R | €137,86 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | RANGE | 4 | 199 | 199 | 40,70% | 0,86 | -0,07R | €-136,17 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | RANGE_HIGH_VOL | 1 | 47 | 47 | 25,53% | 0,28 | -0,47R | €-219,69 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | RANGE_LOW_VOL | 1 | 6 | 6 | 83,33% | 5,17 | 0,70R | €42,28 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TRANSITION | 0 | 67 | 67 | 37,31% | 1,37 | 0,15R | €99,32 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TREND_DOWN | 0 | 56 | 56 | 25,00% | 0,52 | -0,27R | €-151,45 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TREND_DOWN_HIGH_VOL | 1 | 6 | 6 | 16,67% | 0,14 | -0,47R | €-28,21 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TREND_UP | 4 | 68 | 68 | 23,53% | 0,50 | -0,26R | €-176,48 |
| EVO_CAND_SHADOW_1H_FAST_V3_CAP75_V1_TP_R250_3b03ece1 | TREND_UP_HIGH_VOL | 0 | 43 | 43 | 51,16% | 2,15 | 0,44R | €187,59 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | ALT_ROTATION_DOWN | 0 | 17 | 17 | 41,18% | 0,64 | -0,22R | €-37,79 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | ALT_ROTATION_UP | 9 | 164 | 164 | 56,10% | 1,23 | 0,10R | €169,55 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | RANGE | 2 | 113 | 113 | 46,02% | 0,83 | -0,09R | €-105,26 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | RANGE_LOW_VOL | 1 | 6 | 6 | 66,67% | 2,10 | 0,37R | €22,35 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | TRANSITION | 0 | 42 | 42 | 64,29% | 2,20 | 0,39R | €163,01 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | TREND_DOWN | 0 | 30 | 30 | 43,33% | 0,70 | -0,17R | €-49,70 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_L_TP_R200_903364ad | TREND_UP | 4 | 55 | 55 | 43,64% | 0,68 | -0,17R | €-91,61 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | ALT_ROTATION_DOWN | 0 | 16 | 16 | 31,25% | 0,65 | -0,21R | €-33,15 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | ALT_ROTATION_UP | 10 | 168 | 168 | 42,86% | 1,06 | 0,03R | €45,35 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | RANGE | 2 | 118 | 118 | 41,53% | 0,91 | -0,05R | €-53,78 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | RANGE_LOW_VOL | 1 | 6 | 6 | 66,67% | 2,03 | 0,35R | €20,87 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | TRANSITION | 0 | 42 | 42 | 38,10% | 1,86 | 0,26R | €109,81 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | TREND_DOWN | 0 | 30 | 30 | 30,00% | 0,68 | -0,20R | €-58,87 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V_TP_R200_051501d0 | TREND_UP | 4 | 56 | 56 | 26,79% | 0,69 | -0,14R | €-79,20 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | ALT_ROTATION_DOWN | 0 | 57 | 57 | 31,58% | 0,80 | -0,09R | €-50,86 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | ALT_ROTATION_UP | 13 | 313 | 313 | 40,89% | 0,93 | -0,04R | €-110,18 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | RANGE | 2 | 153 | 153 | 40,52% | 0,95 | -0,03R | €-39,89 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | RANGE_HIGH_VOL | 0 | 32 | 32 | 28,12% | 0,54 | -0,29R | €-91,25 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | RANGE_LOW_VOL | 1 | 7 | 7 | 57,14% | 1,96 | 0,42R | €29,27 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TRANSITION | 0 | 58 | 58 | 41,38% | 1,78 | 0,26R | €147,93 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TREND_DOWN | 0 | 41 | 41 | 34,15% | 0,81 | -0,10R | €-40,79 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TREND_DOWN_HIGH_VOL | 0 | 3 | 3 | 33,33% | 14,98 | 0,14R | €4,28 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TREND_UP | 4 | 77 | 77 | 29,87% | 0,73 | -0,13R | €-103,12 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R200_751e55c4 | TREND_UP_HIGH_VOL | 0 | 44 | 44 | 45,45% | 1,56 | 0,24R | €104,07 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | ALT_ROTATION_DOWN | 0 | 56 | 56 | 32,14% | 0,75 | -0,11R | €-62,58 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | ALT_ROTATION_UP | 13 | 291 | 291 | 40,21% | 0,93 | -0,03R | €-95,92 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | RANGE | 2 | 140 | 140 | 42,14% | 0,91 | -0,05R | €-63,04 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | RANGE_HIGH_VOL | 0 | 30 | 30 | 30,00% | 0,59 | -0,24R | €-73,45 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | RANGE_LOW_VOL | 1 | 5 | 5 | 60,00% | 2,47 | 0,60R | €29,85 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TRANSITION | 0 | 57 | 57 | 42,11% | 1,81 | 0,26R | €145,55 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TREND_DOWN | 0 | 38 | 38 | 31,58% | 0,61 | -0,21R | €-81,29 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TREND_DOWN_HIGH_VOL | 0 | 3 | 3 | 33,33% | 14,98 | 0,14R | €4,28 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TREND_UP | 4 | 70 | 70 | 31,43% | 0,67 | -0,16R | €-111,16 |
| EVO_CAND_SHADOW_1H_FAST_V3_LONG_ONLY_V1_TP_R250_bfc04ed6 | TREND_UP_HIGH_VOL | 0 | 44 | 44 | 45,45% | 1,62 | 0,26R | €115,72 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | RANGE | 2 | 240 | 240 | 39,17% | 0,90 | -0,05R | €-116,52 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_RANGE_ONLY_V_TP_R200_52488eb5 | RANGE_LOW_VOL | 0 | 4 | 4 | 50,00% | 1,01 | 0,01R | €0,24 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | ALT_ROTATION_DOWN | 3 | 58 | 58 | 37,93% | 0,62 | -0,24R | €-137,42 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | ALT_ROTATION_UP | 14 | 204 | 204 | 39,22% | 0,88 | -0,06R | €-120,78 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | RANGE | 2 | 210 | 210 | 40,48% | 0,97 | -0,02R | €-34,86 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | RANGE_LOW_VOL | 0 | 4 | 4 | 50,00% | 1,01 | 0,01R | €0,24 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | TRANSITION | 0 | 50 | 50 | 36,00% | 1,35 | 0,14R | €69,11 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | TREND_DOWN | 0 | 57 | 57 | 26,32% | 0,62 | -0,20R | €-116,81 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | TREND_UP | 0 | 14 | 14 | 7,14% | 0,26 | -0,41R | €-57,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | ALT_ROTATION_DOWN | 3 | 99 | 99 | 33,33% | 0,60 | -0,24R | €-241,67 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | ALT_ROTATION_UP | 11 | 215 | 215 | 39,53% | 0,92 | -0,04R | €-84,76 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | RANGE | 5 | 261 | 261 | 40,23% | 0,96 | -0,02R | €-46,49 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | RANGE_LOW_VOL | 1 | 9 | 9 | 66,67% | 2,65 | 0,56R | €50,33 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | TRANSITION | 0 | 68 | 68 | 33,82% | 1,20 | 0,08R | €53,09 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | TREND_DOWN | 0 | 80 | 80 | 28,75% | 0,64 | -0,19R | €-150,63 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R200_8346046b | TREND_UP | 4 | 96 | 96 | 25,00% | 0,61 | -0,20R | €-193,63 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | ALT_ROTATION_DOWN | 3 | 93 | 93 | 31,18% | 0,53 | -0,30R | €-281,01 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | ALT_ROTATION_UP | 11 | 198 | 198 | 38,89% | 0,90 | -0,05R | €-106,08 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | RANGE | 5 | 247 | 247 | 39,68% | 0,87 | -0,06R | €-154,41 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | RANGE_LOW_VOL | 1 | 6 | 6 | 66,67% | 2,53 | 0,52R | €31,12 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | TRANSITION | 0 | 67 | 67 | 34,33% | 1,14 | 0,05R | €36,28 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | TREND_DOWN | 0 | 74 | 74 | 27,03% | 0,58 | -0,21R | €-158,45 |
| EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_V1_TP_R250_c467005a | TREND_UP | 4 | 90 | 90 | 25,56% | 0,54 | -0,24R | €-217,00 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | ALT_ROTATION_DOWN | 0 | 57 | 57 | 31,58% | 0,80 | -0,09R | €-50,86 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | ALT_ROTATION_UP | 13 | 314 | 314 | 41,08% | 0,94 | -0,03R | €-90,62 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | RANGE | 2 | 153 | 153 | 41,83% | 1,03 | 0,01R | €19,77 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | RANGE_HIGH_VOL | 0 | 32 | 32 | 28,12% | 0,54 | -0,29R | €-91,25 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | RANGE_LOW_VOL | 1 | 6 | 6 | 50,00% | 1,32 | 0,16R | €9,72 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TRANSITION | 0 | 58 | 58 | 41,38% | 1,78 | 0,26R | €147,93 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TREND_DOWN | 0 | 41 | 41 | 34,15% | 0,81 | -0,10R | €-40,79 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TREND_DOWN_HIGH_VOL | 0 | 3 | 3 | 33,33% | 14,98 | 0,14R | €4,28 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TREND_UP | 4 | 77 | 77 | 29,87% | 0,73 | -0,13R | €-103,12 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_LONG_ONL_TP_R200_7bbb9481 | TREND_UP_HIGH_VOL | 0 | 44 | 44 | 45,45% | 1,56 | 0,24R | €104,07 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | ALT_ROTATION_DOWN | 3 | 198 | 198 | 37,37% | 0,64 | -0,18R | €-364,90 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | ALT_ROTATION_UP | 13 | 380 | 380 | 43,95% | 0,97 | -0,01R | €-53,35 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | RANGE | 4 | 290 | 290 | 41,72% | 0,99 | -0,00R | €-12,34 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | RANGE_HIGH_VOL | 1 | 67 | 67 | 38,81% | 0,48 | -0,29R | €-193,07 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | RANGE_LOW_VOL | 1 | 8 | 8 | 50,00% | 0,84 | -0,08R | €-6,57 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TRANSITION | 0 | 89 | 89 | 47,19% | 1,55 | 0,17R | €151,33 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_DOWN | 0 | 92 | 92 | 38,04% | 0,78 | -0,09R | €-85,87 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_DOWN_HIGH_VOL | 1 | 5 | 5 | 20,00% | 0,59 | -0,12R | €-5,97 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_UP | 3 | 107 | 107 | 40,19% | 0,74 | -0,13R | €-135,18 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_TP_R200_6b7c560f | TREND_UP_HIGH_VOL | 0 | 54 | 54 | 46,30% | 1,28 | 0,12R | €63,87 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | ALT_ROTATION_DOWN | 1 | 64 | 64 | 43,75% | 0,82 | -0,11R | €-67,30 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | ALT_ROTATION_UP | 6 | 107 | 107 | 40,19% | 0,85 | -0,08R | €-82,61 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | RANGE | 0 | 109 | 109 | 44,04% | 0,82 | -0,09R | €-99,61 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | RANGE_LOW_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,96R | €19,56 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | TRANSITION | 0 | 15 | 15 | 60,00% | 1,97 | 0,42R | €63,22 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | TREND_DOWN | 0 | 15 | 15 | 33,33% | 0,56 | -0,20R | €-30,48 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_G_TP_R200_89ab3f19 | TREND_UP | 3 | 36 | 36 | 19,44% | 0,30 | -0,49R | €-176,29 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | ALT_ROTATION_DOWN | 3 | 168 | 168 | 29,17% | 0,56 | -0,25R | €-423,18 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | ALT_ROTATION_UP | 14 | 330 | 330 | 40,61% | 0,94 | -0,03R | €-100,39 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | RANGE | 4 | 253 | 253 | 39,53% | 0,94 | -0,03R | €-79,62 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | RANGE_HIGH_VOL | 1 | 66 | 66 | 31,82% | 0,46 | -0,31R | €-206,41 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | RANGE_LOW_VOL | 1 | 9 | 9 | 66,67% | 2,65 | 0,56R | €50,33 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TRANSITION | 0 | 80 | 80 | 37,50% | 1,43 | 0,17R | €133,54 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_DOWN | 0 | 80 | 80 | 28,75% | 0,64 | -0,19R | €-150,63 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_DOWN_HIGH_VOL | 1 | 4 | 4 | 25,00% | 0,39 | -0,18R | €-7,14 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_UP | 4 | 93 | 93 | 24,73% | 0,58 | -0,22R | €-202,65 |
| EVO_CAND_SHADOW_1H_FAST_V3_NO_ESPORTS_V1_TP_R200_68f866e1 | TREND_UP_HIGH_VOL | 0 | 46 | 46 | 43,48% | 1,48 | 0,20R | €93,81 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | ALT_ROTATION_DOWN | 3 | 168 | 168 | 29,17% | 0,56 | -0,25R | €-423,18 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | ALT_ROTATION_UP | 14 | 332 | 332 | 40,66% | 0,94 | -0,03R | €-90,66 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | RANGE | 4 | 254 | 254 | 39,37% | 0,93 | -0,04R | €-89,75 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | RANGE_HIGH_VOL | 1 | 66 | 66 | 31,82% | 0,46 | -0,31R | €-206,41 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | RANGE_LOW_VOL | 1 | 9 | 9 | 66,67% | 2,65 | 0,56R | €50,33 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TRANSITION | 0 | 80 | 80 | 37,50% | 1,43 | 0,17R | €133,54 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_DOWN | 0 | 80 | 80 | 28,75% | 0,64 | -0,19R | €-150,63 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_DOWN_HIGH_VOL | 1 | 4 | 4 | 25,00% | 0,39 | -0,18R | €-7,14 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_UP | 4 | 93 | 93 | 24,73% | 0,58 | -0,22R | €-202,65 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R200_3ee5afb4 | TREND_UP_HIGH_VOL | 0 | 47 | 47 | 42,55% | 1,47 | 0,20R | €93,67 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | ALT_ROTATION_DOWN | 3 | 158 | 158 | 28,48% | 0,53 | -0,28R | €-443,38 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | ALT_ROTATION_UP | 14 | 306 | 306 | 40,20% | 0,94 | -0,03R | €-88,45 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | RANGE | 4 | 241 | 241 | 38,59% | 0,81 | -0,09R | €-220,78 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | RANGE_HIGH_VOL | 1 | 61 | 61 | 31,15% | 0,49 | -0,29R | €-179,32 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | RANGE_LOW_VOL | 1 | 6 | 6 | 66,67% | 2,53 | 0,52R | €31,12 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TRANSITION | 0 | 79 | 79 | 37,97% | 1,45 | 0,17R | €133,59 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TREND_DOWN | 0 | 74 | 74 | 27,03% | 0,58 | -0,21R | €-158,45 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TREND_DOWN_HIGH_VOL | 1 | 4 | 4 | 25,00% | 0,39 | -0,18R | €-7,14 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TREND_UP | 4 | 86 | 86 | 25,58% | 0,51 | -0,26R | €-220,68 |
| EVO_CAND_SHADOW_1H_FAST_V3_TP_R250_6b45fc13 | TREND_UP_HIGH_VOL | 0 | 46 | 46 | 43,48% | 1,54 | 0,23R | €105,45 |
| MAIN | ALT_ROTATION_DOWN | 8 | 46 | 46 | 30,43% | 0,82 | -0,10R | €-47,27 |
| MAIN | ALT_ROTATION_UP | 9 | 133 | 133 | 33,83% | 0,74 | -0,16R | €-216,53 |
| MAIN | RANGE | 4 | 105 | 105 | 29,52% | 0,82 | -0,11R | €-114,02 |
| MAIN | RANGE_HIGH_VOL | 2 | 27 | 27 | 25,93% | 0,85 | -0,08R | €-20,96 |
| MAIN | RANGE_LOW_VOL | 1 | 5 | 5 | 60,00% | 2,01 | 0,41R | €20,46 |
| MAIN | TRANSITION | 2 | 43 | 43 | 30,23% | 0,83 | -0,10R | €-42,41 |
| MAIN | TREND_DOWN | 0 | 47 | 47 | 27,66% | 0,74 | -0,16R | €-74,94 |
| MAIN | TREND_DOWN_HIGH_VOL | 0 | 4 | 4 | 50,00% | 1,96 | 0,48R | €19,39 |
| MAIN | TREND_UP | 2 | 49 | 49 | 30,61% | 0,96 | -0,03R | €-12,61 |
| MAIN | TREND_UP_HIGH_VOL | 3 | 14 | 14 | 57,14% | 2,37 | 0,51R | €71,20 |
| RSI_EXTREME_LONG_15M | ALT_ROTATION_DOWN | 0 | 3 | 3 | 0,00% | 0,00 | -0,48R | €-14,27 |
| RSI_EXTREME_LONG_15M | ALT_ROTATION_UP | 0 | 3 | 3 | 33,33% | 0,63 | -0,21R | €-6,42 |
| RSI_EXTREME_LONG_15M | RANGE | 0 | 25 | 25 | 32,00% | 0,13 | -0,59R | €-146,37 |
| RSI_EXTREME_LONG_15M | TRANSITION | 0 | 2 | 2 | 50,00% | 1,14 | 0,08R | €1,56 |
| RSI_EXTREME_LONG_15M | TREND_DOWN | 0 | 5 | 5 | 80,00% | 6,42 | 0,48R | €23,84 |
| RSI_EXTREME_LONG_15M | TREND_UP | 0 | 2 | 2 | 50,00% | 0,63 | -0,19R | €-3,79 |
| RSI_EXTREME_SHORT_15M | ALT_ROTATION_DOWN | 0 | 3 | 3 | 100,00% | ∞ | 1,09R | €32,57 |
| RSI_EXTREME_SHORT_15M | ALT_ROTATION_UP | 0 | 26 | 26 | 46,15% | 1,04 | 0,02R | €4,92 |
| RSI_EXTREME_SHORT_15M | RANGE | 0 | 12 | 12 | 41,67% | 0,85 | -0,08R | €-10,11 |
| RSI_EXTREME_SHORT_15M | RANGE_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,32R | €13,24 |
| RSI_EXTREME_SHORT_15M | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -0,41R | €-4,13 |
| RSI_EXTREME_SHORT_15M | TREND_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 0,31R | €3,08 |
| RSI_EXTREME_SHORT_15M | TREND_UP | 0 | 12 | 12 | 25,00% | 0,34 | -0,45R | €-53,48 |
| RSI_EXTREME_SHORT_15M | TREND_UP_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,21R | €-24,16 |
| Bilanciata 1H V1 | ALT_ROTATION_DOWN | 6 | 159 | 159 | 30,19% | 0,56 | -0,28R | €-452,43 |
| Bilanciata 1H V1 | ALT_ROTATION_UP | 16 | 339 | 339 | 46,31% | 1,11 | 0,06R | €187,79 |
| Bilanciata 1H V1 | RANGE | 7 | 291 | 291 | 41,58% | 0,95 | -0,03R | €-76,47 |
| Bilanciata 1H V1 | RANGE_HIGH_VOL | 1 | 74 | 74 | 31,08% | 0,53 | -0,30R | €-219,07 |
| Bilanciata 1H V1 | RANGE_LOW_VOL | 2 | 10 | 10 | 30,00% | 0,95 | -0,03R | €-2,77 |
| Bilanciata 1H V1 | TRANSITION | 0 | 117 | 117 | 37,61% | 1,08 | 0,04R | €48,40 |
| Bilanciata 1H V1 | TREND_DOWN | 0 | 89 | 89 | 31,46% | 0,75 | -0,13R | €-113,61 |
| Bilanciata 1H V1 | TREND_DOWN_HIGH_VOL | 0 | 6 | 6 | 50,00% | 1,44 | 0,24R | €14,27 |
| Bilanciata 1H V1 | TREND_UP | 4 | 132 | 132 | 31,82% | 0,89 | -0,05R | €-72,13 |
| Bilanciata 1H V1 | TREND_UP_HIGH_VOL | 0 | 53 | 53 | 41,51% | 0,99 | -0,00R | €-2,03 |
| Bilanciata 1H V2 | ALT_ROTATION_UP | 13 | 185 | 156 | 48,11% | 1,24 | 0,12R | €220,80 |
| Bilanciata 1H V2 | RANGE | 6 | 214 | 191 | 38,32% | 0,83 | -0,09R | €-201,04 |
| Bilanciata 1H V2 | TRANSITION | 0 | 97 | 84 | 39,18% | 1,21 | 0,11R | €102,62 |
| Bilanciata 1H V3 Filtered | ALT_ROTATION_DOWN | 3 | 118 | 118 | 28,81% | 0,50 | -0,33R | €-384,51 |
| Bilanciata 1H V3 Filtered | ALT_ROTATION_UP | 11 | 218 | 218 | 46,79% | 1,19 | 0,10R | €207,99 |
| Bilanciata 1H V3 Filtered | RANGE | 6 | 194 | 194 | 44,33% | 1,09 | 0,05R | €88,01 |
| Bilanciata 1H V3 Filtered | RANGE_HIGH_VOL | 2 | 37 | 37 | 27,03% | 0,41 | -0,37R | €-138,27 |
| Bilanciata 1H V3 Filtered | RANGE_LOW_VOL | 1 | 6 | 6 | 33,33% | 1,25 | 0,13R | €7,85 |
| Bilanciata 1H V3 Filtered | TRANSITION | 0 | 64 | 64 | 37,50% | 1,15 | 0,07R | €44,08 |
| Bilanciata 1H V3 Filtered | TREND_DOWN | 0 | 61 | 61 | 34,43% | 0,66 | -0,19R | €-114,28 |
| Bilanciata 1H V3 Filtered | TREND_DOWN_HIGH_VOL | 0 | 8 | 8 | 37,50% | 0,88 | -0,08R | €-6,12 |
| Bilanciata 1H V3 Filtered | TREND_UP | 4 | 79 | 79 | 35,44% | 1,14 | 0,07R | €54,39 |
| Bilanciata 1H V3 Filtered | TREND_UP_HIGH_VOL | 0 | 41 | 41 | 48,78% | 1,64 | 0,27R | €110,47 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 3 | 107 | 107 | 27,10% | 0,41 | -0,39R | €-417,88 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | ALT_ROTATION_UP | 11 | 216 | 216 | 47,22% | 1,21 | 0,11R | €228,99 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | RANGE | 6 | 172 | 172 | 43,60% | 0,97 | -0,02R | €-28,15 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | RANGE_HIGH_VOL | 2 | 35 | 35 | 28,57% | 0,45 | -0,34R | €-117,44 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | RANGE_LOW_VOL | 1 | 6 | 6 | 33,33% | 1,25 | 0,13R | €7,85 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TRANSITION | 0 | 56 | 56 | 37,50% | 1,16 | 0,07R | €38,40 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TREND_DOWN | 0 | 62 | 62 | 33,87% | 0,63 | -0,20R | €-125,39 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TREND_DOWN_HIGH_VOL | 0 | 8 | 8 | 37,50% | 0,88 | -0,08R | €-6,12 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TREND_UP | 4 | 58 | 58 | 32,76% | 0,98 | -0,01R | €-6,44 |
| SHADOW_1H_BALANCED_V3_LONG_ONLY_V1 | TREND_UP_HIGH_VOL | 0 | 27 | 27 | 62,96% | 3,02 | 0,56R | €150,46 |
| Rapida 1H V1 | ALT_ROTATION_DOWN | 0 | 22 | 22 | 22,73% | 0,43 | -0,42R | €-91,69 |
| Rapida 1H V1 | ALT_ROTATION_UP | 0 | 13 | 13 | 53,85% | 1,58 | 0,29R | €37,18 |
| Rapida 1H V1 | RANGE | 0 | 67 | 67 | 44,78% | 1,20 | 0,11R | €71,76 |
| Rapida 1H V1 | RANGE_HIGH_VOL | 0 | 11 | 11 | 0,00% | 0,00 | -1,09R | €-119,90 |
| Rapida 1H V1 | TRANSITION | 0 | 26 | 26 | 50,00% | 1,57 | 0,27R | €68,95 |
| Rapida 1H V1 | TREND_UP | 0 | 48 | 48 | 41,67% | 0,97 | -0,02R | €-9,20 |
| Rapida 1H V1 | TREND_UP_HIGH_VOL | 0 | 21 | 21 | 28,57% | 0,59 | -0,28R | €-58,55 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | ALT_ROTATION_DOWN | 0 | 31 | 31 | 22,58% | 0,49 | -0,26R | €-80,47 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | ALT_ROTATION_UP | 9 | 154 | 154 | 44,16% | 1,01 | 0,01R | €8,03 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | RANGE | 0 | 82 | 82 | 43,90% | 1,05 | 0,03R | €20,62 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | RANGE_HIGH_VOL | 0 | 19 | 19 | 15,79% | 0,18 | -0,71R | €-135,38 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | RANGE_LOW_VOL | 1 | 9 | 9 | 55,56% | 1,36 | 0,17R | €15,33 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TRANSITION | 0 | 37 | 37 | 45,95% | 1,50 | 0,20R | €74,56 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TREND_UP | 2 | 63 | 63 | 33,33% | 0,87 | -0,06R | €-35,07 |
| SHADOW_1H_FAST_LONG_BTC_1_3_CAP75_V1 | TREND_UP_HIGH_VOL | 0 | 11 | 11 | 36,36% | 0,72 | -0,11R | €-11,94 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | ALT_ROTATION_DOWN | 4 | 86 | 86 | 40,70% | 0,97 | -0,01R | €-12,67 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | ALT_ROTATION_UP | 10 | 230 | 230 | 45,65% | 1,13 | 0,06R | €141,37 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | RANGE | 5 | 274 | 274 | 40,88% | 0,93 | -0,04R | €-106,86 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | RANGE_LOW_VOL | 2 | 11 | 11 | 72,73% | 2,81 | 0,52R | €57,56 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | TRANSITION | 0 | 78 | 78 | 39,74% | 1,13 | 0,05R | €41,79 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | TREND_DOWN | 0 | 82 | 82 | 29,27% | 0,62 | -0,22R | €-176,89 |
| SHADOW_1H_FAST_NOHIGH_CAP75_SHORT_ONLY_V1 | TREND_UP | 4 | 102 | 102 | 30,39% | 0,78 | -0,10R | €-106,66 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | ALT_ROTATION_DOWN | 4 | 104 | 104 | 37,50% | 0,83 | -0,09R | €-94,89 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | ALT_ROTATION_UP | 10 | 231 | 231 | 45,89% | 1,15 | 0,07R | €155,27 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | RANGE | 5 | 304 | 304 | 42,76% | 1,02 | 0,01R | €38,33 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | RANGE_LOW_VOL | 2 | 11 | 11 | 72,73% | 2,81 | 0,52R | €57,56 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TRANSITION | 0 | 80 | 80 | 41,25% | 1,23 | 0,09R | €71,48 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TREND_DOWN | 0 | 82 | 82 | 29,27% | 0,62 | -0,22R | €-176,89 |
| SHADOW_1H_FAST_NOHIGH_CAP75_V1 | TREND_UP | 4 | 118 | 118 | 29,66% | 0,71 | -0,15R | €-178,87 |
| SHADOW_1H_FAST_NO_PEPE_V1 | ALT_ROTATION_DOWN | 5 | 206 | 206 | 30,58% | 0,62 | -0,22R | €-457,55 |
| SHADOW_1H_FAST_NO_PEPE_V1 | ALT_ROTATION_UP | 15 | 406 | 406 | 42,36% | 0,95 | -0,03R | €-101,58 |
| SHADOW_1H_FAST_NO_PEPE_V1 | RANGE | 4 | 344 | 344 | 41,28% | 0,95 | -0,03R | €-88,13 |
| SHADOW_1H_FAST_NO_PEPE_V1 | RANGE_HIGH_VOL | 1 | 75 | 75 | 38,67% | 0,66 | -0,19R | €-143,83 |
| SHADOW_1H_FAST_NO_PEPE_V1 | RANGE_LOW_VOL | 2 | 11 | 11 | 54,55% | 1,45 | 0,17R | €18,77 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TRANSITION | 0 | 109 | 109 | 42,20% | 1,33 | 0,13R | €141,25 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_DOWN | 0 | 104 | 104 | 29,81% | 0,64 | -0,19R | €-202,58 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_DOWN_HIGH_VOL | 1 | 5 | 5 | 20,00% | 0,66 | -0,15R | €-7,59 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_UP | 3 | 132 | 132 | 28,79% | 0,71 | -0,15R | €-201,74 |
| SHADOW_1H_FAST_NO_PEPE_V1 | TREND_UP_HIGH_VOL | 0 | 60 | 60 | 43,33% | 1,21 | 0,09R | €52,48 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | ALT_ROTATION_DOWN | 3 | 120 | 120 | 33,33% | 0,63 | -0,22R | €-259,65 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | ALT_ROTATION_UP | 10 | 241 | 241 | 43,98% | 1,05 | 0,03R | €61,05 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | RANGE | 3 | 190 | 190 | 45,79% | 1,24 | 0,11R | €210,60 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | RANGE_HIGH_VOL | 1 | 40 | 40 | 35,00% | 0,41 | -0,36R | €-143,00 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | RANGE_LOW_VOL | 1 | 7 | 7 | 100,00% | ∞ | 0,89R | €62,08 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TRANSITION | 0 | 61 | 61 | 42,62% | 1,60 | 0,20R | €120,86 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_DOWN | 0 | 59 | 59 | 27,12% | 0,55 | -0,25R | €-145,13 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_DOWN_HIGH_VOL | 0 | 6 | 6 | 16,67% | 0,34 | -0,47R | €-28,15 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_UP | 4 | 79 | 79 | 27,85% | 0,62 | -0,21R | €-166,55 |
| SHADOW_1H_FAST_SCORE_6_75_V1 | TREND_UP_HIGH_VOL | 0 | 34 | 34 | 52,94% | 1,58 | 0,24R | €81,07 |
| SHADOW_1H_FAST_TP2_V1 | ALT_ROTATION_DOWN | 5 | 206 | 206 | 28,64% | 0,60 | -0,24R | €-484,88 |
| SHADOW_1H_FAST_TP2_V1 | ALT_ROTATION_UP | 16 | 396 | 396 | 42,17% | 0,99 | -0,00R | €-12,29 |
| SHADOW_1H_FAST_TP2_V1 | RANGE | 4 | 320 | 320 | 40,00% | 0,93 | -0,04R | €-112,01 |
| SHADOW_1H_FAST_TP2_V1 | RANGE_HIGH_VOL | 1 | 77 | 77 | 32,47% | 0,53 | -0,26R | €-203,44 |
| SHADOW_1H_FAST_TP2_V1 | RANGE_LOW_VOL | 2 | 10 | 10 | 50,00% | 1,49 | 0,20R | €20,16 |
| SHADOW_1H_FAST_TP2_V1 | TRANSITION | 0 | 104 | 104 | 39,42% | 1,35 | 0,14R | €146,34 |
| SHADOW_1H_FAST_TP2_V1 | TREND_DOWN | 0 | 98 | 98 | 29,59% | 0,67 | -0,18R | €-179,94 |
| SHADOW_1H_FAST_TP2_V1 | TREND_DOWN_HIGH_VOL | 1 | 5 | 5 | 20,00% | 0,21 | -0,35R | €-17,65 |
| SHADOW_1H_FAST_TP2_V1 | TREND_UP | 3 | 124 | 124 | 22,58% | 0,51 | -0,27R | €-331,16 |
| SHADOW_1H_FAST_TP2_V1 | TREND_UP_HIGH_VOL | 0 | 62 | 62 | 38,71% | 1,22 | 0,09R | €57,95 |
| Rapida 1H V2 | ALT_ROTATION_UP | 0 | 43 | 39 | 46,51% | 0,99 | -0,01R | €-2,94 |
| Rapida 1H V2 | RANGE | 0 | 73 | 62 | 42,47% | 0,95 | -0,03R | €-19,03 |
| Rapida 1H V2 | TRANSITION | 0 | 11 | 11 | 63,64% | 1,79 | 0,25R | €27,27 |
| Rapida 1H V3 Filtered | ALT_ROTATION_DOWN | 3 | 197 | 197 | 30,46% | 0,56 | -0,25R | €-501,71 |
| Rapida 1H V3 Filtered | ALT_ROTATION_UP | 14 | 372 | 372 | 43,01% | 1,00 | -0,00R | €-5,58 |
| Rapida 1H V3 Filtered | RANGE | 4 | 306 | 306 | 40,52% | 0,97 | -0,02R | €-47,86 |
| Rapida 1H V3 Filtered | RANGE_HIGH_VOL | 1 | 70 | 70 | 38,57% | 0,60 | -0,23R | €-158,07 |
| Rapida 1H V3 Filtered | RANGE_LOW_VOL | 1 | 10 | 10 | 60,00% | 1,91 | 0,29R | €28,95 |
| Rapida 1H V3 Filtered | TRANSITION | 0 | 94 | 94 | 40,43% | 1,27 | 0,11R | €104,32 |
| Rapida 1H V3 Filtered | TREND_DOWN | 0 | 91 | 91 | 28,57% | 0,63 | -0,19R | €-176,81 |
| Rapida 1H V3 Filtered | TREND_DOWN_HIGH_VOL | 1 | 4 | 4 | 25,00% | 1,25 | 0,07R | €2,92 |
| Rapida 1H V3 Filtered | TREND_UP | 4 | 129 | 129 | 36,43% | 0,96 | -0,02R | €-24,06 |
| Rapida 1H V3 Filtered | TREND_UP_HIGH_VOL | 0 | 69 | 69 | 37,68% | 0,89 | -0,06R | €-40,54 |
| SHADOW_1H_FAST_V3_CAP75_V1 | ALT_ROTATION_DOWN | 3 | 152 | 152 | 33,55% | 0,63 | -0,21R | €-320,95 |
| SHADOW_1H_FAST_V3_CAP75_V1 | ALT_ROTATION_UP | 11 | 294 | 294 | 46,26% | 1,12 | 0,05R | €155,74 |
| SHADOW_1H_FAST_V3_CAP75_V1 | RANGE | 4 | 240 | 240 | 42,08% | 1,05 | 0,02R | €56,58 |
| SHADOW_1H_FAST_V3_CAP75_V1 | RANGE_HIGH_VOL | 1 | 55 | 55 | 32,73% | 0,41 | -0,38R | €-206,58 |
| SHADOW_1H_FAST_V3_CAP75_V1 | RANGE_LOW_VOL | 1 | 8 | 8 | 87,50% | 6,12 | 0,65R | €51,94 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TRANSITION | 0 | 71 | 71 | 40,85% | 1,26 | 0,11R | €75,52 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_DOWN | 0 | 66 | 66 | 27,27% | 0,61 | -0,22R | €-144,01 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_DOWN_HIGH_VOL | 1 | 6 | 6 | 16,67% | 0,45 | -0,30R | €-18,15 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_UP | 4 | 90 | 90 | 28,89% | 0,65 | -0,19R | €-167,97 |
| SHADOW_1H_FAST_V3_CAP75_V1 | TREND_UP_HIGH_VOL | 0 | 47 | 47 | 51,06% | 1,56 | 0,22R | €104,59 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | ALT_ROTATION_DOWN | 0 | 24 | 24 | 29,17% | 0,29 | -0,52R | €-125,13 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | ALT_ROTATION_UP | 9 | 181 | 181 | 55,80% | 1,19 | 0,09R | €156,28 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | RANGE | 2 | 131 | 131 | 47,33% | 1,04 | 0,02R | €27,17 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | RANGE_LOW_VOL | 1 | 6 | 6 | 83,33% | 4,68 | 0,62R | €37,35 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TRANSITION | 0 | 43 | 43 | 65,12% | 2,22 | 0,36R | €154,71 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TREND_DOWN | 0 | 33 | 33 | 42,42% | 0,84 | -0,09R | €-30,17 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_LOCK_V1 | TREND_UP | 4 | 67 | 67 | 49,25% | 0,90 | -0,05R | €-33,75 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | ALT_ROTATION_DOWN | 0 | 23 | 23 | 21,74% | 0,28 | -0,52R | €-120,49 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | ALT_ROTATION_UP | 9 | 184 | 184 | 43,48% | 1,06 | 0,03R | €50,61 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | RANGE | 2 | 135 | 135 | 44,44% | 1,13 | 0,07R | €89,81 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | RANGE_LOW_VOL | 1 | 6 | 6 | 83,33% | 4,54 | 0,60R | €35,87 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TRANSITION | 0 | 43 | 43 | 44,19% | 1,85 | 0,26R | €109,67 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TREND_DOWN | 0 | 33 | 33 | 33,33% | 0,76 | -0,14R | €-46,76 |
| SHADOW_1H_FAST_V3_LONG_NOHIGH_CAP75_V1 | TREND_UP | 4 | 69 | 69 | 31,88% | 0,80 | -0,10R | €-65,97 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 0 | 68 | 68 | 26,47% | 0,51 | -0,26R | €-177,16 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | ALT_ROTATION_UP | 13 | 355 | 355 | 42,82% | 0,98 | -0,01R | €-25,93 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | RANGE | 2 | 177 | 177 | 42,94% | 1,06 | 0,03R | €48,89 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | RANGE_HIGH_VOL | 0 | 33 | 33 | 36,36% | 0,66 | -0,20R | €-64,35 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | RANGE_LOW_VOL | 1 | 8 | 8 | 62,50% | 1,88 | 0,35R | €27,84 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TRANSITION | 0 | 62 | 62 | 46,77% | 1,73 | 0,25R | €153,48 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_DOWN | 0 | 48 | 48 | 35,42% | 0,81 | -0,10R | €-49,05 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_DOWN_HIGH_VOL | 0 | 3 | 3 | 33,33% | 47,80 | 0,48R | €14,34 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_UP | 4 | 88 | 88 | 34,09% | 0,87 | -0,07R | €-58,63 |
| SHADOW_1H_FAST_V3_LONG_ONLY_V1 | TREND_UP_HIGH_VOL | 0 | 47 | 47 | 44,68% | 1,19 | 0,09R | €42,04 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | ALT_ROTATION_DOWN | 3 | 122 | 122 | 33,61% | 0,60 | -0,24R | €-294,86 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | ALT_ROTATION_UP | 11 | 239 | 239 | 41,42% | 0,96 | -0,02R | €-46,08 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | RANGE | 5 | 315 | 315 | 41,90% | 1,03 | 0,01R | €46,93 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | RANGE_LOW_VOL | 1 | 10 | 10 | 60,00% | 1,91 | 0,29R | €28,95 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TRANSITION | 0 | 74 | 74 | 39,19% | 1,32 | 0,12R | €87,36 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TREND_DOWN | 0 | 91 | 91 | 28,57% | 0,63 | -0,19R | €-176,81 |
| SHADOW_1H_FAST_V3_NOHIGH_V1 | TREND_UP | 4 | 118 | 118 | 31,36% | 0,76 | -0,13R | €-150,43 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | ALT_ROTATION_DOWN | 3 | 196 | 196 | 30,61% | 0,57 | -0,25R | €-490,28 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | ALT_ROTATION_UP | 14 | 371 | 371 | 42,59% | 0,97 | -0,01R | €-46,70 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | RANGE | 4 | 304 | 304 | 40,46% | 0,96 | -0,02R | €-62,60 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | RANGE_HIGH_VOL | 1 | 69 | 69 | 39,13% | 0,61 | -0,21R | €-147,94 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | RANGE_LOW_VOL | 1 | 10 | 10 | 60,00% | 1,91 | 0,29R | €28,95 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TRANSITION | 0 | 89 | 89 | 40,45% | 1,31 | 0,12R | €107,09 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_DOWN | 0 | 91 | 91 | 28,57% | 0,63 | -0,19R | €-176,81 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_DOWN_HIGH_VOL | 1 | 4 | 4 | 25,00% | 1,25 | 0,07R | €2,92 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_UP | 4 | 112 | 112 | 31,25% | 0,75 | -0,13R | €-146,80 |
| SHADOW_1H_FAST_V3_NO_ESPORTS_V1 | TREND_UP_HIGH_VOL | 0 | 49 | 49 | 42,86% | 1,14 | 0,06R | €31,77 |
| SHADOW_4H_WIDE | ALT_ROTATION_DOWN | 9 | 46 | 46 | 26,09% | 0,92 | -0,05R | €-21,30 |
| SHADOW_4H_WIDE | ALT_ROTATION_UP | 11 | 110 | 110 | 35,45% | 0,94 | -0,04R | €-43,22 |
| SHADOW_4H_WIDE | RANGE | 5 | 98 | 98 | 20,41% | 0,75 | -0,16R | €-158,83 |
| SHADOW_4H_WIDE | RANGE_HIGH_VOL | 2 | 21 | 21 | 19,05% | 0,84 | -0,10R | €-21,46 |
| SHADOW_4H_WIDE | RANGE_LOW_VOL | 1 | 4 | 4 | 0,00% | 0,00 | -0,76R | €-30,53 |
| SHADOW_4H_WIDE | TRANSITION | 2 | 44 | 44 | 20,45% | 0,59 | -0,28R | €-121,03 |
| SHADOW_4H_WIDE | TREND_DOWN | 1 | 46 | 46 | 26,09% | 0,91 | -0,06R | €-28,84 |
| SHADOW_4H_WIDE | TREND_DOWN_HIGH_VOL | 0 | 5 | 5 | 40,00% | 2,73 | 0,71R | €35,33 |
| SHADOW_4H_WIDE | TREND_UP | 7 | 47 | 47 | 29,79% | 1,26 | 0,14R | €66,40 |
| SHADOW_4H_WIDE | TREND_UP_HIGH_VOL | 4 | 20 | 20 | 25,00% | 0,80 | -0,13R | €-25,04 |
| SHADOW_BOLLINGER_MR_1H | ALT_ROTATION_DOWN | 1 | 56 | 56 | 44,64% | 0,84 | -0,08R | €-45,66 |
| SHADOW_BOLLINGER_MR_1H | ALT_ROTATION_UP | 2 | 153 | 153 | 48,37% | 1,01 | 0,01R | €9,62 |
| SHADOW_BOLLINGER_MR_1H | RANGE | 0 | 102 | 102 | 49,02% | 0,97 | -0,02R | €-16,51 |
| SHADOW_BOLLINGER_MR_1H | RANGE_HIGH_VOL | 0 | 16 | 16 | 50,00% | 1,36 | 0,15R | €23,95 |
| SHADOW_BOLLINGER_MR_1H | RANGE_LOW_VOL | 0 | 3 | 3 | 33,33% | 0,70 | -0,21R | €-6,33 |
| SHADOW_BOLLINGER_MR_1H | TRANSITION | 0 | 19 | 19 | 52,63% | 1,52 | 0,23R | €44,43 |
| SHADOW_BOLLINGER_MR_1H | TREND_DOWN | 0 | 18 | 18 | 66,67% | 2,87 | 0,45R | €80,90 |
| SHADOW_BOLLINGER_MR_1H | TREND_UP | 1 | 45 | 45 | 42,22% | 0,85 | -0,07R | €-33,39 |
| SHADOW_BOLLINGER_MR_1H | TREND_UP_HIGH_VOL | 0 | 24 | 24 | 37,50% | 0,80 | -0,09R | €-21,69 |
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
| SHADOW_BTC_EMA_1H | ALT_ROTATION_UP | 1 | 5 | 5 | 40,00% | 0,27 | -0,48R | €-24,20 |
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
| SHADOW_COMBO_ADAPTIVE | ALT_ROTATION_UP | 11 | 289 | 289 | 46,37% | 1,14 | 0,08R | €218,68 |
| SHADOW_COMBO_ADAPTIVE | RANGE | 6 | 241 | 241 | 44,81% | 0,94 | -0,03R | €-73,87 |
| SHADOW_COMBO_ADAPTIVE | RANGE_HIGH_VOL | 1 | 58 | 58 | 34,48% | 0,53 | -0,26R | €-153,32 |
| SHADOW_COMBO_ADAPTIVE | RANGE_LOW_VOL | 1 | 10 | 10 | 40,00% | 0,95 | -0,03R | €-3,06 |
| SHADOW_COMBO_ADAPTIVE | TRANSITION | 0 | 92 | 92 | 42,39% | 1,23 | 0,11R | €98,46 |
| SHADOW_COMBO_ADAPTIVE | TREND_DOWN | 0 | 76 | 76 | 35,53% | 0,95 | -0,02R | €-18,40 |
| SHADOW_COMBO_ADAPTIVE | TREND_DOWN_HIGH_VOL | 0 | 4 | 4 | 75,00% | 4,61 | 0,91R | €36,57 |
| SHADOW_COMBO_ADAPTIVE | TREND_UP | 4 | 108 | 108 | 37,96% | 1,08 | 0,04R | €40,72 |
| SHADOW_COMBO_ADAPTIVE | TREND_UP_HIGH_VOL | 0 | 47 | 47 | 40,43% | 0,88 | -0,06R | €-30,40 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | ALT_ROTATION_DOWN | 1 | 47 | 47 | 31,91% | 0,81 | -0,11R | €-50,70 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | ALT_ROTATION_UP | 11 | 279 | 279 | 45,88% | 1,10 | 0,05R | €147,24 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | RANGE | 3 | 133 | 133 | 46,62% | 0,98 | -0,01R | €-14,79 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | RANGE_HIGH_VOL | 0 | 23 | 23 | 30,43% | 0,38 | -0,37R | €-86,15 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | RANGE_LOW_VOL | 1 | 9 | 9 | 44,44% | 1,14 | 0,08R | €7,09 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TRANSITION | 0 | 53 | 53 | 47,17% | 1,65 | 0,22R | €114,73 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_DOWN | 0 | 45 | 45 | 37,78% | 1,22 | 0,10R | €44,99 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_DOWN_HIGH_VOL | 0 | 3 | 3 | 66,67% | 3,88 | 0,97R | €29,16 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_UP | 4 | 67 | 67 | 32,84% | 0,69 | -0,15R | €-98,92 |
| SHADOW_COMBO_ADAPTIVE_LONG_ONLY_V1 | TREND_UP_HIGH_VOL | 0 | 38 | 38 | 44,74% | 0,97 | -0,02R | €-5,92 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | ALT_ROTATION_DOWN | 5 | 166 | 166 | 35,54% | 0,72 | -0,14R | €-229,09 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | ALT_ROTATION_UP | 14 | 339 | 339 | 41,00% | 1,05 | 0,02R | €73,57 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE | 6 | 255 | 255 | 42,35% | 1,08 | 0,04R | €91,71 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE_HIGH_VOL | 1 | 66 | 66 | 34,85% | 0,49 | -0,26R | €-171,59 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | RANGE_LOW_VOL | 1 | 12 | 12 | 33,33% | 0,51 | -0,30R | €-35,58 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TRANSITION | 0 | 84 | 84 | 45,24% | 1,22 | 0,09R | €71,97 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_DOWN | 0 | 100 | 100 | 38,00% | 0,96 | -0,02R | €-16,64 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_DOWN_HIGH_VOL | 0 | 4 | 4 | 75,00% | 3,69 | 0,68R | €27,30 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_UP | 2 | 114 | 114 | 49,12% | 1,26 | 0,11R | €119,70 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_UP_HIGH_VOL | 0 | 55 | 55 | 45,45% | 0,97 | -0,01R | €-7,21 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | ALT_ROTATION_DOWN | 6 | 138 | 138 | 32,61% | 0,69 | -0,19R | €-263,36 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | ALT_ROTATION_UP | 11 | 287 | 287 | 46,69% | 1,09 | 0,05R | €139,08 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | RANGE | 6 | 229 | 229 | 47,16% | 1,00 | -0,00R | €-3,40 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | RANGE_HIGH_VOL | 1 | 56 | 56 | 37,50% | 0,63 | -0,20R | €-113,63 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | RANGE_LOW_VOL | 1 | 10 | 10 | 40,00% | 0,75 | -0,16R | €-15,75 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TRANSITION | 0 | 75 | 75 | 46,67% | 1,21 | 0,09R | €70,55 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_DOWN | 0 | 76 | 76 | 39,47% | 0,96 | -0,02R | €-14,90 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_DOWN_HIGH_VOL | 0 | 4 | 4 | 75,00% | 4,07 | 0,78R | €31,07 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_UP | 4 | 87 | 87 | 39,08% | 0,79 | -0,10R | €-84,28 |
| SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | TREND_UP_HIGH_VOL | 0 | 42 | 42 | 45,24% | 0,94 | -0,03R | €-13,40 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TRANSITION | 0 | 45 | 45 | 42,22% | 0,97 | -0,01R | €-6,60 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TREND_UP | 3 | 41 | 41 | 48,78% | 1,26 | 0,11R | €46,68 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_PARTIAL_1R_V1 | TREND_UP_HIGH_VOL | 1 | 20 | 20 | 60,00% | 2,81 | 0,48R | €95,08 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TRANSITION | 0 | 45 | 45 | 42,22% | 0,88 | -0,06R | €-26,38 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TREND_UP | 3 | 41 | 41 | 39,02% | 1,13 | 0,06R | €24,11 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_REGIME_V1 | TREND_UP_HIGH_VOL | 1 | 20 | 20 | 55,00% | 3,18 | 0,57R | €114,89 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | ALT_ROTATION_DOWN | 4 | 43 | 43 | 37,21% | 0,74 | -0,14R | €-59,10 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | ALT_ROTATION_UP | 7 | 133 | 133 | 44,36% | 0,87 | -0,08R | €-100,11 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | RANGE | 2 | 76 | 76 | 36,84% | 0,79 | -0,13R | €-96,03 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | RANGE_HIGH_VOL | 2 | 15 | 15 | 46,67% | 1,19 | 0,08R | €11,47 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | RANGE_LOW_VOL | 0 | 4 | 4 | 75,00% | 2,67 | 0,42R | €16,87 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TRANSITION | 0 | 39 | 39 | 41,03% | 0,90 | -0,05R | €-19,83 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_DOWN | 0 | 28 | 28 | 25,00% | 0,63 | -0,18R | €-50,57 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_DOWN_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_UP | 2 | 26 | 26 | 38,46% | 1,17 | 0,06R | €15,70 |
| SHADOW_COMBO_ADAPTIVE_QUALITY7_V1 | TREND_UP_HIGH_VOL | 1 | 13 | 13 | 61,54% | 6,45 | 0,91R | €117,92 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TRANSITION | 1 | 110 | 110 | 41,82% | 1,06 | 0,03R | €30,23 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TREND_UP | 7 | 134 | 134 | 37,31% | 0,81 | -0,09R | €-124,72 |
| SHADOW_COMBO_ADAPTIVE_REGIME_V1 | TREND_UP_HIGH_VOL | 0 | 60 | 60 | 51,67% | 1,39 | 0,18R | €108,65 |
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
| SHADOW_COMBO_MEAN_REVERSION | ALT_ROTATION_UP | 1 | 24 | 24 | 50,00% | 1,24 | 0,12R | €29,32 |
| SHADOW_COMBO_MEAN_REVERSION | RANGE | 0 | 53 | 53 | 45,28% | 0,87 | -0,07R | €-37,33 |
| SHADOW_COMBO_MEAN_REVERSION | RANGE_HIGH_VOL | 0 | 10 | 10 | 20,00% | 0,44 | -0,38R | €-38,09 |
| SHADOW_COMBO_MEAN_REVERSION | TRANSITION | 0 | 8 | 8 | 62,50% | 2,67 | 0,46R | €36,75 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_DOWN | 0 | 14 | 14 | 64,29% | 1,44 | 0,17R | €23,50 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_UP | 0 | 17 | 17 | 58,82% | 1,72 | 0,23R | €38,61 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 50,00% | 1,42 | 0,23R | €9,02 |
| SHADOW_COMBO_SCANNER | ALT_ROTATION_DOWN | 1 | 51 | 51 | 27,45% | 0,49 | -0,34R | €-174,70 |
| SHADOW_COMBO_SCANNER | ALT_ROTATION_UP | 14 | 225 | 225 | 44,00% | 1,09 | 0,05R | €112,47 |
| SHADOW_COMBO_SCANNER | RANGE | 4 | 145 | 145 | 44,14% | 1,08 | 0,04R | €61,11 |
| SHADOW_COMBO_SCANNER | RANGE_HIGH_VOL | 0 | 25 | 25 | 40,00% | 0,56 | -0,24R | €-60,42 |
| SHADOW_COMBO_SCANNER | RANGE_LOW_VOL | 1 | 10 | 10 | 30,00% | 0,84 | -0,10R | €-9,67 |
| SHADOW_COMBO_SCANNER | TRANSITION | 0 | 72 | 72 | 43,06% | 1,49 | 0,22R | €160,17 |
| SHADOW_COMBO_SCANNER | TREND_DOWN | 0 | 45 | 45 | 31,11% | 0,82 | -0,10R | €-45,10 |
| SHADOW_COMBO_SCANNER | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 2,14 | 0,58R | €11,58 |
| SHADOW_COMBO_SCANNER | TREND_UP | 3 | 76 | 76 | 34,21% | 1,11 | 0,05R | €40,78 |
| SHADOW_COMBO_SCANNER | TREND_UP_HIGH_VOL | 0 | 30 | 30 | 43,33% | 1,28 | 0,14R | €41,56 |
| SHADOW_COMBO_TREND | ALT_ROTATION_DOWN | 6 | 107 | 107 | 28,97% | 0,54 | -0,30R | €-323,14 |
| SHADOW_COMBO_TREND | ALT_ROTATION_UP | 12 | 253 | 253 | 46,64% | 1,17 | 0,09R | €229,30 |
| SHADOW_COMBO_TREND | RANGE | 6 | 201 | 201 | 38,81% | 1,06 | 0,03R | €61,92 |
| SHADOW_COMBO_TREND | RANGE_HIGH_VOL | 1 | 44 | 44 | 40,91% | 1,03 | 0,01R | €6,54 |
| SHADOW_COMBO_TREND | RANGE_LOW_VOL | 2 | 8 | 8 | 37,50% | 1,00 | -0,00R | €-0,10 |
| SHADOW_COMBO_TREND | TRANSITION | 0 | 76 | 76 | 36,84% | 1,15 | 0,08R | €60,00 |
| SHADOW_COMBO_TREND | TREND_DOWN | 0 | 68 | 68 | 30,88% | 0,76 | -0,13R | €-86,73 |
| SHADOW_COMBO_TREND | TREND_DOWN_HIGH_VOL | 0 | 3 | 3 | 66,67% | 1,61 | 0,21R | €6,21 |
| SHADOW_COMBO_TREND | TREND_UP | 4 | 84 | 84 | 30,95% | 0,99 | -0,01R | €-5,46 |
| SHADOW_COMBO_TREND | TREND_UP_HIGH_VOL | 0 | 35 | 35 | 40,00% | 0,85 | -0,08R | €-29,14 |
| SHADOW_DOGE_BOLLINGER_1H | ALT_ROTATION_DOWN | 0 | 6 | 6 | 50,00% | 0,62 | -0,21R | €-12,31 |
| SHADOW_DOGE_BOLLINGER_1H | ALT_ROTATION_UP | 1 | 6 | 6 | 66,67% | 3,84 | 0,56R | €33,45 |
| SHADOW_DOGE_BOLLINGER_1H | RANGE | 0 | 9 | 9 | 55,56% | 0,84 | -0,08R | €-7,12 |
| SHADOW_DOGE_BOLLINGER_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,15 |
| SHADOW_DOGE_BOLLINGER_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,58 |
| SHADOW_DOGE_DONCHIAN_1H | ALT_ROTATION_DOWN | 0 | 8 | 8 | 25,00% | 0,33 | -0,56R | €-44,78 |
| SHADOW_DOGE_DONCHIAN_1H | ALT_ROTATION_UP | 0 | 5 | 5 | 20,00% | 0,14 | -0,73R | €-36,57 |
| SHADOW_DOGE_DONCHIAN_1H | RANGE | 0 | 9 | 9 | 55,56% | 1,07 | 0,03R | €3,05 |
| SHADOW_DOGE_DONCHIAN_1H | RANGE_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,89R | €18,92 |
| SHADOW_DOGE_DONCHIAN_1H | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,88R | €18,76 |
| SHADOW_DOGE_DONCHIAN_1H | TREND_DOWN | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,25 |
| SHADOW_DOGE_DONCHIAN_1H | TREND_UP | 1 | 1 | 1 | 100,00% | ∞ | 1,88R | €18,75 |
| SHADOW_DOGE_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,16R | €1,62 |
| SHADOW_DOGE_EMA_1H | ALT_ROTATION_DOWN | 0 | 11 | 11 | 9,09% | 0,08 | -0,74R | €-81,45 |
| SHADOW_DOGE_EMA_1H | ALT_ROTATION_UP | 0 | 11 | 11 | 18,18% | 0,41 | -0,51R | €-56,27 |
| SHADOW_DOGE_EMA_1H | RANGE | 0 | 13 | 13 | 46,15% | 1,23 | 0,12R | €15,53 |
| SHADOW_DOGE_EMA_1H | RANGE_HIGH_VOL | 0 | 4 | 4 | 100,00% | ∞ | 0,81R | €32,50 |
| SHADOW_DOGE_EMA_1H | TRANSITION | 0 | 2 | 2 | 50,00% | 0,54 | -0,26R | €-5,10 |
| SHADOW_DOGE_EMA_1H | TREND_DOWN | 0 | 3 | 3 | 66,67% | 0,52 | -0,18R | €-5,34 |
| SHADOW_DOGE_EMA_1H | TREND_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_DOGE_EMA_1H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,14R | €1,44 |
| SHADOW_DONCHIAN_1H | ALT_ROTATION_DOWN | 1 | 72 | 72 | 29,17% | 0,55 | -0,31R | €-225,72 |
| SHADOW_DONCHIAN_1H | ALT_ROTATION_UP | 1 | 139 | 139 | 38,13% | 0,86 | -0,09R | €-121,45 |
| SHADOW_DONCHIAN_1H | RANGE | 1 | 109 | 109 | 41,28% | 1,12 | 0,07R | €75,55 |
| SHADOW_DONCHIAN_1H | RANGE_HIGH_VOL | 1 | 16 | 16 | 50,00% | 1,82 | 0,38R | €60,21 |
| SHADOW_DONCHIAN_1H | RANGE_LOW_VOL | 1 | 3 | 3 | 33,33% | 0,58 | -0,29R | €-8,57 |
| SHADOW_DONCHIAN_1H | TRANSITION | 1 | 33 | 33 | 39,39% | 1,29 | 0,15R | €48,35 |
| SHADOW_DONCHIAN_1H | TREND_DOWN | 1 | 22 | 22 | 27,27% | 0,43 | -0,41R | €-89,96 |
| SHADOW_DONCHIAN_1H | TREND_UP | 2 | 44 | 44 | 29,55% | 1,10 | 0,05R | €22,01 |
| SHADOW_DONCHIAN_1H | TREND_UP_HIGH_VOL | 1 | 26 | 26 | 53,85% | 1,80 | 0,39R | €101,75 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | ALT_ROTATION_DOWN | 1 | 62 | 62 | 29,03% | 0,46 | -0,38R | €-234,20 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | ALT_ROTATION_UP | 1 | 131 | 131 | 39,69% | 0,91 | -0,05R | €-71,03 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | RANGE | 1 | 89 | 89 | 43,82% | 1,13 | 0,07R | €60,49 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | RANGE_HIGH_VOL | 1 | 14 | 14 | 57,14% | 2,52 | 0,57R | €80,48 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | RANGE_LOW_VOL | 1 | 2 | 2 | 50,00% | 1,15 | 0,08R | €1,56 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | TRANSITION | 1 | 26 | 26 | 46,15% | 1,68 | 0,30R | €77,62 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | TREND_DOWN | 1 | 20 | 20 | 30,00% | 0,46 | -0,40R | €-79,67 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | TREND_UP | 2 | 30 | 30 | 26,67% | 0,96 | -0,02R | €-4,96 |
| SHADOW_DONCHIAN_1H_GB20_120R_V1 | TREND_UP_HIGH_VOL | 1 | 20 | 20 | 60,00% | 2,15 | 0,48R | €96,97 |
| SHADOW_EMA_TREND_1H | ALT_ROTATION_DOWN | 7 | 114 | 114 | 28,07% | 0,50 | -0,34R | €-390,31 |
| SHADOW_EMA_TREND_1H | ALT_ROTATION_UP | 15 | 259 | 259 | 46,33% | 1,15 | 0,08R | €203,62 |
| SHADOW_EMA_TREND_1H | RANGE | 6 | 194 | 194 | 37,63% | 1,01 | 0,00R | €8,92 |
| SHADOW_EMA_TREND_1H | RANGE_HIGH_VOL | 1 | 46 | 46 | 41,30% | 1,16 | 0,08R | €37,87 |
| SHADOW_EMA_TREND_1H | RANGE_LOW_VOL | 2 | 8 | 8 | 37,50% | 1,00 | -0,00R | €-0,10 |
| SHADOW_EMA_TREND_1H | TRANSITION | 0 | 72 | 72 | 34,72% | 1,04 | 0,02R | €17,55 |
| SHADOW_EMA_TREND_1H | TREND_DOWN | 0 | 69 | 69 | 30,43% | 0,68 | -0,17R | €-115,23 |
| SHADOW_EMA_TREND_1H | TREND_DOWN_HIGH_VOL | 0 | 3 | 3 | 33,33% | 0,51 | -0,34R | €-10,34 |
| SHADOW_EMA_TREND_1H | TREND_UP | 3 | 92 | 92 | 28,26% | 0,81 | -0,11R | €-99,12 |
| SHADOW_EMA_TREND_1H | TREND_UP_HIGH_VOL | 0 | 36 | 36 | 47,22% | 1,32 | 0,16R | €58,32 |
| SHADOW_ETH_ADAPTIVE_1H | ALT_ROTATION_DOWN | 0 | 3 | 3 | 0,00% | 0,00 | -1,10R | €-33,02 |
| SHADOW_ETH_ADAPTIVE_1H | ALT_ROTATION_UP | 0 | 12 | 12 | 33,33% | 0,70 | -0,22R | €-26,02 |
| SHADOW_ETH_ADAPTIVE_1H | RANGE | 0 | 10 | 10 | 30,00% | 0,38 | -0,48R | €-48,41 |
| SHADOW_ETH_ADAPTIVE_1H | RANGE_HIGH_VOL | 0 | 3 | 3 | 33,33% | 0,00 | -0,71R | €-21,28 |
| SHADOW_ETH_ADAPTIVE_1H | TRANSITION | 0 | 2 | 2 | 100,00% | ∞ | 0,54R | €10,89 |
| SHADOW_ETH_ADAPTIVE_1H | TREND_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 1,89R | €18,89 |
| SHADOW_ETH_ADAPTIVE_1H | TREND_UP | 0 | 3 | 3 | 66,67% | 2,41 | 0,52R | €15,63 |
| SHADOW_ETH_ADAPTIVE_1H | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -1,09R | €-32,84 |
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
| SHADOW_ETH_DONCHIAN_1H | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 25,00% | 0,57 | -0,36R | €-14,30 |
| SHADOW_ETH_EMA_1H | ALT_ROTATION_DOWN | 0 | 4 | 4 | 0,00% | 0,00 | -1,10R | €-43,91 |
| SHADOW_ETH_EMA_1H | ALT_ROTATION_UP | 1 | 21 | 21 | 47,62% | 0,91 | -0,05R | €-10,09 |
| SHADOW_ETH_EMA_1H | RANGE | 0 | 9 | 9 | 33,33% | 0,25 | -0,55R | €-49,78 |
| SHADOW_ETH_EMA_1H | RANGE_HIGH_VOL | 0 | 5 | 5 | 20,00% | 0,43 | -0,49R | €-24,67 |
| SHADOW_ETH_EMA_1H | TRANSITION | 0 | 2 | 2 | 50,00% | 0,45 | -0,30R | €-6,08 |
| SHADOW_ETH_EMA_1H | TREND_DOWN | 0 | 2 | 2 | 50,00% | 0,75 | -0,14R | €-2,73 |
| SHADOW_ETH_EMA_1H | TREND_UP | 0 | 5 | 5 | 40,00% | 0,81 | -0,13R | €-6,46 |
| SHADOW_ETH_EMA_1H | TREND_UP_HIGH_VOL | 0 | 3 | 3 | 0,00% | 0,00 | -1,09R | €-32,72 |
| SHADOW_ETH_EMA_4H | ALT_ROTATION_UP | 0 | 5 | 5 | 60,00% | 1,09 | 0,04R | €1,91 |
| SHADOW_ETH_EMA_4H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,07R | €-10,72 |
| SHADOW_ETH_EMA_4H | RANGE_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,04R | €-10,39 |
| SHADOW_ETH_EMA_4H | TREND_UP | 1 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,57 |
| SHADOW_ETH_EMA_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 0,74R | €7,41 |
| SHADOW_GLOBAL_PURE | ALT_ROTATION_DOWN | 0 | 1 | 1 | 100,00% | ∞ | 0,35R | €3,51 |
| SHADOW_GLOBAL_PURE | ALT_ROTATION_UP | 0 | 3 | 3 | 0,00% | 0,00 | -1,10R | €-33,00 |
| SHADOW_GLOBAL_PURE | RANGE | 0 | 10 | 10 | 40,00% | 0,80 | -0,13R | €-13,34 |
| SHADOW_GLOBAL_PURE | RANGE_HIGH_VOL | 0 | 1 | 1 | 100,00% | ∞ | 1,59R | €15,85 |
| SHADOW_GLOBAL_PURE | TRANSITION | 0 | 4 | 4 | 75,00% | 4,43 | 0,94R | €37,75 |
| SHADOW_GLOBAL_PURE | TREND_DOWN | 0 | 2 | 2 | 50,00% | 0,02 | -0,54R | €-10,79 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | ALT_ROTATION_DOWN | 0 | 31 | 31 | 38,71% | 1,27 | 0,16R | €50,15 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | ALT_ROTATION_UP | 12 | 101 | 101 | 40,59% | 1,23 | 0,15R | €149,13 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | RANGE | 4 | 144 | 144 | 29,86% | 0,85 | -0,10R | €-149,95 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | RANGE_LOW_VOL | 1 | 9 | 9 | 33,33% | 0,95 | -0,04R | €-3,18 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TRANSITION | 0 | 46 | 46 | 47,83% | 1,97 | 0,46R | €212,56 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TREND_DOWN | 0 | 50 | 50 | 38,00% | 1,29 | 0,17R | €82,76 |
| SHADOW_MASTER_ADAPTIVE_EXPANDED_V1 | TREND_UP | 4 | 76 | 76 | 27,63% | 0,76 | -0,17R | €-130,06 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | ALT_ROTATION_DOWN | 1 | 49 | 49 | 59,18% | 1,01 | 0,01R | €2,65 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | ALT_ROTATION_UP | 13 | 217 | 217 | 67,28% | 1,25 | 0,08R | €176,14 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | RANGE | 3 | 268 | 268 | 66,04% | 1,26 | 0,08R | €221,24 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | RANGE_LOW_VOL | 1 | 15 | 15 | 80,00% | 1,61 | 0,12R | €18,62 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TRANSITION | 0 | 100 | 100 | 73,00% | 1,75 | 0,18R | €181,85 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TREND_DOWN | 0 | 78 | 78 | 64,10% | 1,36 | 0,12R | €94,03 |
| SHADOW_MASTER_ADAPTIVE_GB20_V1 | TREND_UP | 1 | 142 | 142 | 59,86% | 0,93 | -0,03R | €-37,83 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | ALT_ROTATION_DOWN | 0 | 28 | 28 | 39,29% | 1,40 | 0,22R | €61,61 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | RANGE | 6 | 146 | 146 | 30,82% | 0,89 | -0,08R | €-110,85 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | RANGE_LOW_VOL | 1 | 9 | 9 | 44,44% | 1,51 | 0,29R | €26,16 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TRANSITION | 1 | 46 | 46 | 45,65% | 1,79 | 0,40R | €182,06 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TREND_DOWN | 0 | 45 | 45 | 40,00% | 1,37 | 0,21R | €96,58 |
| SHADOW_MASTER_ADAPTIVE_NO_ALT_V1 | TREND_UP | 7 | 89 | 89 | 24,72% | 0,65 | -0,26R | €-234,03 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_DOWN | 0 | 25 | 25 | 48,00% | 1,99 | 0,49R | €123,26 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | ALT_ROTATION_UP | 11 | 102 | 102 | 38,24% | 1,12 | 0,08R | €84,51 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | RANGE | 4 | 129 | 129 | 31,01% | 0,97 | -0,02R | €-21,82 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | RANGE_LOW_VOL | 1 | 8 | 8 | 37,50% | 1,10 | 0,06R | €5,18 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | TRANSITION | 0 | 41 | 41 | 43,90% | 1,70 | 0,36R | €145,68 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | TREND_DOWN | 0 | 42 | 42 | 40,48% | 1,42 | 0,24R | €100,50 |
| SHADOW_MASTER_ADAPTIVE_RUNNER25_V1 | TREND_UP | 5 | 72 | 72 | 23,61% | 0,63 | -0,28R | €-198,14 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | ALT_ROTATION_DOWN | 0 | 19 | 19 | 26,32% | 0,73 | -0,19R | €-35,51 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | RANGE | 4 | 100 | 100 | 31,00% | 0,86 | -0,10R | €-101,93 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | RANGE_LOW_VOL | 1 | 7 | 7 | 28,57% | 0,75 | -0,19R | €-12,99 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TRANSITION | 0 | 36 | 36 | 47,22% | 2,12 | 0,49R | €176,16 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TREND_DOWN | 0 | 32 | 32 | 25,00% | 0,70 | -0,21R | €-67,12 |
| SHADOW_MASTER_ADAPTIVE_STRICT3_V1 | TREND_UP | 6 | 65 | 65 | 27,69% | 0,77 | -0,17R | €-108,89 |
| SHADOW_MASTER_ADAPTIVE_V1 | ALT_ROTATION_DOWN | 0 | 28 | 28 | 39,29% | 1,32 | 0,18R | €51,75 |
| SHADOW_MASTER_ADAPTIVE_V1 | ALT_ROTATION_UP | 12 | 103 | 103 | 40,78% | 1,23 | 0,15R | €156,60 |
| SHADOW_MASTER_ADAPTIVE_V1 | RANGE | 4 | 135 | 135 | 31,85% | 0,94 | -0,04R | €-53,96 |
| SHADOW_MASTER_ADAPTIVE_V1 | RANGE_LOW_VOL | 1 | 9 | 9 | 33,33% | 0,95 | -0,04R | €-3,19 |
| SHADOW_MASTER_ADAPTIVE_V1 | TRANSITION | 0 | 45 | 45 | 44,44% | 1,71 | 0,36R | €162,62 |
| SHADOW_MASTER_ADAPTIVE_V1 | TREND_DOWN | 0 | 43 | 43 | 39,53% | 1,35 | 0,20R | €86,84 |
| SHADOW_MASTER_ADAPTIVE_V1 | TREND_UP | 4 | 75 | 75 | 24,00% | 0,63 | -0,28R | €-208,46 |
| Forza relativa 1H V1 | ALT_ROTATION_DOWN | 7 | 133 | 133 | 32,33% | 0,61 | -0,24R | €-315,45 |
| Forza relativa 1H V1 | ALT_ROTATION_UP | 15 | 282 | 282 | 42,91% | 1,08 | 0,04R | €123,37 |
| Forza relativa 1H V1 | RANGE | 8 | 254 | 254 | 33,86% | 0,80 | -0,11R | €-280,42 |
| Forza relativa 1H V1 | RANGE_HIGH_VOL | 1 | 50 | 50 | 28,00% | 0,48 | -0,34R | €-170,72 |
| Forza relativa 1H V1 | RANGE_LOW_VOL | 1 | 11 | 11 | 27,27% | 0,72 | -0,18R | €-19,83 |
| Forza relativa 1H V1 | TRANSITION | 0 | 92 | 92 | 39,13% | 1,34 | 0,17R | €155,94 |
| Forza relativa 1H V1 | TREND_DOWN | 0 | 78 | 78 | 29,49% | 0,95 | -0,02R | €-19,05 |
| Forza relativa 1H V1 | TREND_DOWN_HIGH_VOL | 1 | 3 | 3 | 100,00% | ∞ | 1,66R | €49,91 |
| Forza relativa 1H V1 | TREND_UP | 3 | 111 | 111 | 27,03% | 0,88 | -0,07R | €-74,32 |
| Forza relativa 1H V1 | TREND_UP_HIGH_VOL | 0 | 39 | 39 | 33,33% | 0,89 | -0,07R | €-26,73 |
| Forza relativa 1H V2 | ALT_ROTATION_DOWN | 5 | 62 | 60 | 43,55% | 0,84 | -0,08R | €-50,02 |
| Forza relativa 1H V2 | ALT_ROTATION_UP | 9 | 114 | 103 | 43,86% | 1,17 | 0,10R | €111,29 |
| Forza relativa 1H V2 | RANGE | 7 | 113 | 107 | 31,86% | 0,73 | -0,16R | €-183,75 |
| Forza relativa 1H V2 | RANGE_LOW_VOL | 0 | 8 | 7 | 25,00% | 0,66 | -0,18R | €-14,36 |
| Forza relativa 1H V2 | TRANSITION | 0 | 49 | 44 | 40,82% | 1,54 | 0,25R | €122,15 |
| Forza relativa 1H V2 | TREND_DOWN | 0 | 36 | 35 | 27,78% | 0,89 | -0,05R | €-17,72 |
| Forza relativa 1H V2 | TREND_DOWN_HIGH_VOL | 0 | 6 | 6 | 33,33% | 0,69 | -0,21R | €-12,82 |
| Forza relativa 1H V2 | TREND_UP | 5 | 44 | 39 | 47,73% | 1,77 | 0,34R | €151,54 |
| Forza relativa 1H V2 | TREND_UP_HIGH_VOL | 0 | 12 | 10 | 25,00% | 0,52 | -0,36R | €-42,68 |
| SHADOW_SCANNER_BOTTOM10_SHORT | ALT_ROTATION_DOWN | 4 | 96 | 96 | 22,92% | 0,33 | -0,49R | €-470,21 |
| SHADOW_SCANNER_BOTTOM10_SHORT | ALT_ROTATION_UP | 0 | 18 | 18 | 44,44% | 1,47 | 0,19R | €35,01 |
| SHADOW_SCANNER_BOTTOM10_SHORT | RANGE | 3 | 104 | 104 | 37,50% | 0,70 | -0,14R | €-149,93 |
| SHADOW_SCANNER_BOTTOM10_SHORT | RANGE_HIGH_VOL | 1 | 31 | 31 | 41,94% | 0,91 | -0,04R | €-12,88 |
| SHADOW_SCANNER_BOTTOM10_SHORT | RANGE_LOW_VOL | 1 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,15 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TRANSITION | 0 | 26 | 26 | 42,31% | 1,15 | 0,08R | €21,58 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_DOWN | 0 | 45 | 45 | 26,67% | 0,37 | -0,37R | €-166,77 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_DOWN_HIGH_VOL | 0 | 3 | 3 | 33,33% | 0,31 | -0,51R | €-15,18 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_UP | 0 | 17 | 17 | 5,88% | 0,25 | -0,33R | €-56,36 |
| SHADOW_SCANNER_BOTTOM10_SHORT | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 25,00% | 0,42 | -0,68R | €-27,16 |
| SHADOW_SCANNER_BOTTOM15_SHORT | ALT_ROTATION_DOWN | 4 | 96 | 96 | 22,92% | 0,33 | -0,49R | €-470,21 |
| SHADOW_SCANNER_BOTTOM15_SHORT | ALT_ROTATION_UP | 0 | 18 | 18 | 44,44% | 1,47 | 0,19R | €35,01 |
| SHADOW_SCANNER_BOTTOM15_SHORT | RANGE | 3 | 104 | 104 | 37,50% | 0,70 | -0,14R | €-149,93 |
| SHADOW_SCANNER_BOTTOM15_SHORT | RANGE_HIGH_VOL | 1 | 31 | 31 | 41,94% | 0,91 | -0,04R | €-12,88 |
| SHADOW_SCANNER_BOTTOM15_SHORT | RANGE_LOW_VOL | 1 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,15 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TRANSITION | 0 | 26 | 26 | 42,31% | 1,15 | 0,08R | €21,58 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_DOWN | 0 | 45 | 45 | 26,67% | 0,37 | -0,37R | €-166,77 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_DOWN_HIGH_VOL | 0 | 3 | 3 | 33,33% | 0,31 | -0,51R | €-15,18 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_UP | 0 | 17 | 17 | 5,88% | 0,25 | -0,33R | €-56,36 |
| SHADOW_SCANNER_BOTTOM15_SHORT | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 25,00% | 0,42 | -0,68R | €-27,16 |
| SHADOW_SCANNER_BOTTOM20_SHORT | ALT_ROTATION_DOWN | 4 | 96 | 96 | 22,92% | 0,33 | -0,49R | €-470,21 |
| SHADOW_SCANNER_BOTTOM20_SHORT | ALT_ROTATION_UP | 0 | 18 | 18 | 44,44% | 1,47 | 0,19R | €35,01 |
| SHADOW_SCANNER_BOTTOM20_SHORT | RANGE | 3 | 104 | 104 | 37,50% | 0,70 | -0,14R | €-149,93 |
| SHADOW_SCANNER_BOTTOM20_SHORT | RANGE_HIGH_VOL | 1 | 31 | 31 | 41,94% | 0,91 | -0,04R | €-12,88 |
| SHADOW_SCANNER_BOTTOM20_SHORT | RANGE_LOW_VOL | 1 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,15 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TRANSITION | 0 | 26 | 26 | 42,31% | 1,15 | 0,08R | €21,58 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_DOWN | 0 | 45 | 45 | 26,67% | 0,37 | -0,37R | €-166,77 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_DOWN_HIGH_VOL | 0 | 3 | 3 | 33,33% | 0,31 | -0,51R | €-15,18 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_UP | 0 | 17 | 17 | 5,88% | 0,25 | -0,33R | €-56,36 |
| SHADOW_SCANNER_BOTTOM20_SHORT | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 25,00% | 0,42 | -0,68R | €-27,16 |
| SHADOW_SCANNER_BOTTOM5_SHORT | ALT_ROTATION_DOWN | 4 | 83 | 83 | 24,10% | 0,40 | -0,43R | €-353,10 |
| SHADOW_SCANNER_BOTTOM5_SHORT | ALT_ROTATION_UP | 0 | 19 | 19 | 47,37% | 1,74 | 0,29R | €54,88 |
| SHADOW_SCANNER_BOTTOM5_SHORT | RANGE | 3 | 116 | 116 | 37,93% | 0,88 | -0,06R | €-68,89 |
| SHADOW_SCANNER_BOTTOM5_SHORT | RANGE_HIGH_VOL | 1 | 30 | 30 | 46,67% | 1,14 | 0,06R | €17,21 |
| SHADOW_SCANNER_BOTTOM5_SHORT | RANGE_LOW_VOL | 1 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,15 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TRANSITION | 0 | 42 | 42 | 38,10% | 1,01 | 0,01R | €2,87 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_DOWN | 0 | 41 | 41 | 26,83% | 0,37 | -0,35R | €-144,97 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 0,62 | -0,21R | €-4,24 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP | 0 | 24 | 24 | 4,17% | 0,15 | -0,45R | €-107,40 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP_HIGH_VOL | 0 | 7 | 7 | 14,29% | 0,29 | -0,69R | €-48,54 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | ALT_ROTATION_DOWN | 4 | 102 | 102 | 44,12% | 0,49 | -0,28R | €-288,70 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | ALT_ROTATION_UP | 0 | 14 | 14 | 50,00% | 1,32 | 0,15R | €20,41 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | RANGE | 3 | 132 | 132 | 62,88% | 0,99 | -0,00R | €-4,42 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | RANGE_HIGH_VOL | 1 | 35 | 35 | 62,86% | 1,17 | 0,07R | €23,75 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | RANGE_LOW_VOL | 1 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,26 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TRANSITION | 0 | 33 | 33 | 57,58% | 1,30 | 0,13R | €44,05 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_DOWN | 0 | 68 | 68 | 52,94% | 0,63 | -0,16R | €-108,67 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_DOWN_HIGH_VOL | 0 | 4 | 4 | 50,00% | 0,62 | -0,21R | €-8,36 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_UP | 0 | 20 | 20 | 40,00% | 0,58 | -0,20R | €-40,01 |
| SHADOW_SCANNER_BOTTOM5_SHORT_MFE_TRAIL_V1 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 25,00% | 0,04 | -1,13R | €-45,16 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | ALT_ROTATION_DOWN | 4 | 83 | 83 | 39,76% | 0,37 | -0,37R | €-307,11 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | ALT_ROTATION_UP | 0 | 17 | 17 | 52,94% | 1,61 | 0,23R | €38,54 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | RANGE | 3 | 120 | 120 | 64,17% | 0,92 | -0,03R | €-33,92 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | RANGE_HIGH_VOL | 1 | 34 | 34 | 58,82% | 0,96 | -0,02R | €-6,50 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | RANGE_LOW_VOL | 1 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,26 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TRANSITION | 0 | 32 | 32 | 59,38% | 1,50 | 0,21R | €67,96 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_DOWN | 0 | 57 | 57 | 50,88% | 0,60 | -0,18R | €-103,46 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_DOWN_HIGH_VOL | 0 | 4 | 4 | 50,00% | 0,37 | -0,35R | €-14,07 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_UP | 0 | 19 | 19 | 36,84% | 0,30 | -0,35R | €-66,17 |
| SHADOW_SCANNER_BOTTOM5_SHORT_PROFIT_LOCK_V1 | TREND_UP_HIGH_VOL | 0 | 4 | 4 | 25,00% | 0,04 | -1,13R | €-45,16 |
| SHADOW_SCANNER_TOP10_LONG | ALT_ROTATION_DOWN | 2 | 44 | 44 | 36,36% | 0,88 | -0,07R | €-29,49 |
| SHADOW_SCANNER_TOP10_LONG | ALT_ROTATION_UP | 15 | 292 | 292 | 45,21% | 1,04 | 0,02R | €62,27 |
| SHADOW_SCANNER_TOP10_LONG | RANGE | 4 | 126 | 126 | 45,24% | 0,98 | -0,01R | €-11,25 |
| SHADOW_SCANNER_TOP10_LONG | RANGE_HIGH_VOL | 0 | 25 | 25 | 28,00% | 0,56 | -0,29R | €-71,85 |
| SHADOW_SCANNER_TOP10_LONG | RANGE_LOW_VOL | 1 | 10 | 10 | 30,00% | 0,95 | -0,03R | €-3,27 |
| SHADOW_SCANNER_TOP10_LONG | TRANSITION | 0 | 57 | 57 | 40,35% | 1,36 | 0,14R | €78,21 |
| SHADOW_SCANNER_TOP10_LONG | TREND_DOWN | 0 | 46 | 46 | 30,43% | 1,02 | 0,01R | €5,92 |
| SHADOW_SCANNER_TOP10_LONG | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,95 | 0,48R | €9,58 |
| SHADOW_SCANNER_TOP10_LONG | TREND_UP | 4 | 68 | 68 | 30,88% | 0,67 | -0,17R | €-113,06 |
| SHADOW_SCANNER_TOP10_LONG | TREND_UP_HIGH_VOL | 0 | 37 | 37 | 54,05% | 1,51 | 0,19R | €71,21 |
| SHADOW_SCANNER_TOP15_LONG | ALT_ROTATION_DOWN | 2 | 44 | 44 | 36,36% | 0,88 | -0,07R | €-29,43 |
| SHADOW_SCANNER_TOP15_LONG | ALT_ROTATION_UP | 15 | 297 | 297 | 45,79% | 1,05 | 0,03R | €75,45 |
| SHADOW_SCANNER_TOP15_LONG | RANGE | 4 | 126 | 126 | 45,24% | 0,98 | -0,01R | €-11,25 |
| SHADOW_SCANNER_TOP15_LONG | RANGE_HIGH_VOL | 0 | 25 | 25 | 28,00% | 0,56 | -0,29R | €-71,85 |
| SHADOW_SCANNER_TOP15_LONG | RANGE_LOW_VOL | 1 | 10 | 10 | 30,00% | 0,95 | -0,03R | €-3,27 |
| SHADOW_SCANNER_TOP15_LONG | TRANSITION | 0 | 57 | 57 | 40,35% | 1,36 | 0,14R | €78,21 |
| SHADOW_SCANNER_TOP15_LONG | TREND_DOWN | 0 | 46 | 46 | 30,43% | 1,02 | 0,01R | €5,92 |
| SHADOW_SCANNER_TOP15_LONG | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,95 | 0,48R | €9,58 |
| SHADOW_SCANNER_TOP15_LONG | TREND_UP | 4 | 68 | 68 | 30,88% | 0,67 | -0,17R | €-113,06 |
| SHADOW_SCANNER_TOP15_LONG | TREND_UP_HIGH_VOL | 0 | 35 | 35 | 51,43% | 1,46 | 0,18R | €63,97 |
| SHADOW_SCANNER_TOP20_LONG | ALT_ROTATION_DOWN | 2 | 44 | 44 | 36,36% | 0,88 | -0,07R | €-29,43 |
| SHADOW_SCANNER_TOP20_LONG | ALT_ROTATION_UP | 15 | 297 | 297 | 45,79% | 1,05 | 0,03R | €75,45 |
| SHADOW_SCANNER_TOP20_LONG | RANGE | 4 | 126 | 126 | 45,24% | 0,98 | -0,01R | €-11,25 |
| SHADOW_SCANNER_TOP20_LONG | RANGE_HIGH_VOL | 0 | 25 | 25 | 28,00% | 0,56 | -0,29R | €-71,85 |
| SHADOW_SCANNER_TOP20_LONG | RANGE_LOW_VOL | 1 | 10 | 10 | 30,00% | 0,95 | -0,03R | €-3,27 |
| SHADOW_SCANNER_TOP20_LONG | TRANSITION | 0 | 57 | 57 | 40,35% | 1,36 | 0,14R | €78,21 |
| SHADOW_SCANNER_TOP20_LONG | TREND_DOWN | 0 | 46 | 46 | 30,43% | 1,02 | 0,01R | €5,92 |
| SHADOW_SCANNER_TOP20_LONG | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,95 | 0,48R | €9,58 |
| SHADOW_SCANNER_TOP20_LONG | TREND_UP | 4 | 68 | 68 | 30,88% | 0,67 | -0,17R | €-113,06 |
| SHADOW_SCANNER_TOP20_LONG | TREND_UP_HIGH_VOL | 0 | 35 | 35 | 51,43% | 1,46 | 0,18R | €63,97 |
| SHADOW_SCANNER_TOP5_BTC | ALT_ROTATION_DOWN | 1 | 47 | 47 | 29,79% | 0,56 | -0,28R | €-131,01 |
| SHADOW_SCANNER_TOP5_BTC | ALT_ROTATION_UP | 14 | 223 | 223 | 43,95% | 1,08 | 0,05R | €103,10 |
| SHADOW_SCANNER_TOP5_BTC | RANGE | 4 | 134 | 134 | 44,03% | 1,10 | 0,05R | €70,86 |
| SHADOW_SCANNER_TOP5_BTC | RANGE_HIGH_VOL | 0 | 22 | 22 | 31,82% | 0,48 | -0,32R | €-71,39 |
| SHADOW_SCANNER_TOP5_BTC | RANGE_LOW_VOL | 1 | 10 | 10 | 30,00% | 0,84 | -0,10R | €-9,67 |
| SHADOW_SCANNER_TOP5_BTC | TRANSITION | 0 | 67 | 67 | 41,79% | 1,48 | 0,22R | €145,48 |
| SHADOW_SCANNER_TOP5_BTC | TREND_DOWN | 0 | 44 | 44 | 29,55% | 0,82 | -0,10R | €-45,52 |
| SHADOW_SCANNER_TOP5_BTC | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 2,14 | 0,58R | €11,58 |
| SHADOW_SCANNER_TOP5_BTC | TREND_UP | 3 | 75 | 75 | 33,33% | 1,05 | 0,03R | €20,07 |
| SHADOW_SCANNER_TOP5_BTC | TREND_UP_HIGH_VOL | 0 | 30 | 30 | 43,33% | 1,28 | 0,14R | €41,56 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | ALT_ROTATION_DOWN | 1 | 18 | 18 | 11,11% | 0,18 | -0,67R | €-119,88 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | ALT_ROTATION_UP | 11 | 95 | 95 | 37,89% | 0,63 | -0,25R | €-235,03 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | RANGE | 1 | 12 | 12 | 41,67% | 0,44 | -0,35R | €-41,60 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | RANGE_HIGH_VOL | 0 | 4 | 4 | 25,00% | 0,27 | -0,58R | €-23,05 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TRANSITION | 0 | 30 | 30 | 53,33% | 2,17 | 0,40R | €120,24 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TREND_UP | 2 | 58 | 58 | 29,31% | 0,86 | -0,07R | €-42,83 |
| SHADOW_SCANNER_TOP5_BTC_BTC_2_3_V1 | TREND_UP_HIGH_VOL | 0 | 14 | 14 | 14,29% | 0,24 | -0,58R | €-80,67 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | ALT_ROTATION_DOWN | 1 | 40 | 40 | 27,50% | 0,53 | -0,30R | €-120,90 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | ALT_ROTATION_UP | 11 | 122 | 122 | 39,34% | 0,76 | -0,15R | €-181,16 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | RANGE | 5 | 130 | 130 | 43,08% | 1,01 | 0,00R | €5,12 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | RANGE_HIGH_VOL | 0 | 21 | 21 | 33,33% | 0,52 | -0,29R | €-60,69 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | RANGE_LOW_VOL | 1 | 10 | 10 | 30,00% | 0,84 | -0,10R | €-9,67 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TRANSITION | 0 | 51 | 51 | 47,06% | 2,10 | 0,38R | €193,93 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_DOWN | 0 | 44 | 44 | 29,55% | 0,82 | -0,10R | €-45,52 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 2,14 | 0,58R | €11,58 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_UP | 2 | 52 | 52 | 23,08% | 0,59 | -0,24R | €-122,50 |
| SHADOW_SCANNER_TOP5_BTC_BTC_LE3_V1 | TREND_UP_HIGH_VOL | 0 | 14 | 14 | 14,29% | 0,24 | -0,58R | €-80,67 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | ALT_ROTATION_DOWN | 1 | 37 | 37 | 32,43% | 0,69 | -0,14R | €-50,92 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | ALT_ROTATION_UP | 7 | 127 | 127 | 42,52% | 0,92 | -0,04R | €-48,23 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | RANGE | 5 | 156 | 156 | 43,59% | 1,08 | 0,04R | €58,79 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | RANGE_HIGH_VOL | 0 | 33 | 33 | 33,33% | 0,61 | -0,18R | €-60,32 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | RANGE_LOW_VOL | 1 | 12 | 12 | 33,33% | 0,56 | -0,26R | €-31,74 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TRANSITION | 0 | 51 | 51 | 47,06% | 1,28 | 0,11R | €54,83 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_DOWN | 0 | 51 | 51 | 47,06% | 0,98 | -0,01R | €-5,20 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 2,14 | 0,58R | €11,58 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_UP | 2 | 53 | 53 | 50,94% | 1,34 | 0,14R | €72,98 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 7 | 7 | 57,14% | 1,17 | 0,07R | €5,17 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | ALT_ROTATION_DOWN | 1 | 30 | 30 | 33,33% | 0,62 | -0,22R | €-67,08 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | ALT_ROTATION_UP | 8 | 101 | 101 | 42,57% | 0,89 | -0,07R | €-66,87 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | RANGE | 5 | 134 | 134 | 44,03% | 1,04 | 0,02R | €24,81 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | RANGE_HIGH_VOL | 0 | 25 | 25 | 32,00% | 0,44 | -0,35R | €-88,53 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | RANGE_LOW_VOL | 1 | 10 | 10 | 30,00% | 0,84 | -0,10R | €-9,67 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TRANSITION | 0 | 46 | 46 | 39,13% | 1,52 | 0,21R | €97,22 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_DOWN | 0 | 40 | 40 | 30,00% | 0,76 | -0,14R | €-57,22 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 2,14 | 0,58R | €11,58 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_UP | 2 | 41 | 41 | 26,83% | 0,78 | -0,12R | €-47,64 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_BTC_LE3_V1 | TREND_UP_HIGH_VOL | 0 | 8 | 8 | 12,50% | 0,42 | -0,37R | €-29,56 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | ALT_ROTATION_DOWN | 1 | 45 | 45 | 37,78% | 0,83 | -0,08R | €-35,16 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | ALT_ROTATION_UP | 13 | 238 | 238 | 43,28% | 1,04 | 0,02R | €44,37 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | RANGE | 4 | 157 | 157 | 43,95% | 1,10 | 0,05R | €71,67 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | RANGE_HIGH_VOL | 0 | 33 | 33 | 33,33% | 0,61 | -0,18R | €-60,32 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | RANGE_LOW_VOL | 1 | 12 | 12 | 33,33% | 0,56 | -0,26R | €-31,74 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TRANSITION | 0 | 57 | 57 | 43,86% | 1,25 | 0,09R | €51,57 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_DOWN | 0 | 51 | 51 | 47,06% | 0,98 | -0,01R | €-5,20 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 2,14 | 0,58R | €11,58 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_UP | 2 | 62 | 62 | 50,00% | 1,32 | 0,13R | €80,27 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 29 | 29 | 62,07% | 1,56 | 0,18R | €52,58 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | ALT_ROTATION_DOWN | 1 | 37 | 37 | 35,14% | 0,68 | -0,18R | €-67,50 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | ALT_ROTATION_UP | 13 | 193 | 193 | 46,63% | 1,21 | 0,11R | €216,77 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | RANGE | 4 | 133 | 133 | 44,36% | 1,05 | 0,03R | €37,33 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | RANGE_HIGH_VOL | 0 | 25 | 25 | 32,00% | 0,44 | -0,35R | €-88,53 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | RANGE_LOW_VOL | 1 | 10 | 10 | 30,00% | 0,84 | -0,10R | €-9,67 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TRANSITION | 0 | 51 | 51 | 39,22% | 1,34 | 0,15R | €73,97 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_DOWN | 0 | 40 | 40 | 30,00% | 0,76 | -0,14R | €-57,22 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 2,14 | 0,58R | €11,58 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_UP | 2 | 48 | 48 | 27,08% | 0,81 | -0,10R | €-48,83 |
| SHADOW_SCANNER_TOP5_BTC_GUARD_V1 | TREND_UP_HIGH_VOL | 0 | 19 | 19 | 42,11% | 1,28 | 0,14R | €26,18 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | ALT_ROTATION_DOWN | 1 | 56 | 56 | 35,71% | 0,70 | -0,14R | €-78,18 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | ALT_ROTATION_UP | 15 | 267 | 267 | 41,95% | 0,94 | -0,03R | €-81,10 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | RANGE | 4 | 148 | 148 | 44,59% | 1,11 | 0,05R | €73,98 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | RANGE_HIGH_VOL | 0 | 30 | 30 | 30,00% | 0,45 | -0,26R | €-78,43 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | RANGE_LOW_VOL | 1 | 12 | 12 | 33,33% | 0,56 | -0,26R | €-31,74 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TRANSITION | 0 | 65 | 65 | 44,62% | 1,28 | 0,10R | €67,21 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_DOWN | 0 | 58 | 58 | 44,83% | 1,01 | 0,00R | €1,84 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 2,14 | 0,58R | €11,58 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_UP | 2 | 79 | 79 | 49,37% | 1,31 | 0,11R | €90,32 |
| SHADOW_SCANNER_TOP5_BTC_MFE_V1 | TREND_UP_HIGH_VOL | 0 | 40 | 40 | 52,50% | 1,23 | 0,09R | €37,53 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | ALT_ROTATION_DOWN | 1 | 40 | 40 | 35,00% | 0,69 | -0,19R | €-77,15 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | ALT_ROTATION_UP | 14 | 223 | 223 | 43,50% | 1,08 | 0,05R | €101,31 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | RANGE | 4 | 125 | 125 | 42,40% | 1,04 | 0,02R | €25,66 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | RANGE_HIGH_VOL | 0 | 21 | 21 | 33,33% | 0,52 | -0,29R | €-61,69 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | RANGE_LOW_VOL | 1 | 9 | 9 | 33,33% | 0,99 | -0,01R | €-0,54 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TRANSITION | 0 | 55 | 55 | 40,00% | 1,41 | 0,18R | €99,29 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_DOWN | 0 | 43 | 43 | 30,23% | 0,87 | -0,07R | €-31,88 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 2,08 | 0,55R | €10,95 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_UP | 3 | 58 | 58 | 27,59% | 0,72 | -0,14R | €-82,52 |
| SHADOW_SCANNER_TOP5_BTC_RUNNER25_V1 | TREND_UP_HIGH_VOL | 0 | 25 | 25 | 40,00% | 0,90 | -0,05R | €-13,19 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | ALT_ROTATION_DOWN | 1 | 38 | 38 | 34,21% | 0,71 | -0,18R | €-68,52 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | ALT_ROTATION_UP | 14 | 214 | 214 | 42,06% | 1,07 | 0,04R | €91,00 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | RANGE | 4 | 119 | 119 | 42,02% | 1,06 | 0,03R | €41,18 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | RANGE_HIGH_VOL | 0 | 21 | 21 | 33,33% | 0,54 | -0,28R | €-58,63 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | RANGE_LOW_VOL | 1 | 9 | 9 | 33,33% | 0,68 | -0,18R | €-16,36 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TRANSITION | 0 | 49 | 49 | 38,78% | 1,59 | 0,24R | €116,44 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_DOWN | 0 | 40 | 40 | 30,00% | 0,93 | -0,04R | €-14,25 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,23 | 0,12R | €2,31 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_UP | 3 | 57 | 57 | 29,82% | 0,78 | -0,11R | €-61,53 |
| SHADOW_SCANNER_TOP5_BTC_TP3_V1 | TREND_UP_HIGH_VOL | 0 | 24 | 24 | 45,83% | 1,08 | 0,04R | €9,63 |
| SHADOW_SCANNER_TOP5_LONG | ALT_ROTATION_DOWN | 1 | 53 | 53 | 32,08% | 0,69 | -0,18R | €-97,82 |
| SHADOW_SCANNER_TOP5_LONG | ALT_ROTATION_UP | 13 | 233 | 233 | 44,21% | 1,02 | 0,01R | €22,63 |
| SHADOW_SCANNER_TOP5_LONG | RANGE | 4 | 141 | 141 | 44,68% | 1,06 | 0,03R | €42,81 |
| SHADOW_SCANNER_TOP5_LONG | RANGE_HIGH_VOL | 0 | 27 | 27 | 25,93% | 0,49 | -0,34R | €-92,68 |
| SHADOW_SCANNER_TOP5_LONG | RANGE_LOW_VOL | 1 | 10 | 10 | 30,00% | 0,95 | -0,03R | €-3,27 |
| SHADOW_SCANNER_TOP5_LONG | TRANSITION | 0 | 70 | 70 | 41,43% | 1,43 | 0,18R | €124,25 |
| SHADOW_SCANNER_TOP5_LONG | TREND_DOWN | 0 | 46 | 46 | 30,43% | 1,02 | 0,01R | €5,92 |
| SHADOW_SCANNER_TOP5_LONG | TREND_DOWN_HIGH_VOL | 0 | 2 | 2 | 50,00% | 1,95 | 0,48R | €9,58 |
| SHADOW_SCANNER_TOP5_LONG | TREND_UP | 3 | 96 | 96 | 39,58% | 1,18 | 0,08R | €78,81 |
| SHADOW_SCANNER_TOP5_LONG | TREND_UP_HIGH_VOL | 0 | 38 | 38 | 52,63% | 1,61 | 0,24R | €91,83 |
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
| SHADOW_SOL_ADAPTIVE_4H | TREND_UP | 1 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,77 |
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
| SHADOW_SOL_DONCHIAN_4H | ALT_ROTATION_UP | 0 | 4 | 4 | 50,00% | 1,05 | 0,03R | €1,08 |
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
| SHADOW_SOL_EMA_4H | TREND_UP | 1 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,84 |
| SHADOW_SOL_EMA_4H | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,06R | €-10,58 |

Il P&L è normalizzato a **€10 di rischio per evento**, così leva e size non falsano il confronto.
La matrice diventerà utilizzabile per una rotazione automatica soltanto dopo un campione sufficiente per ciascuna coppia strategia-regime.

# Block 3 — Shadow Exit Engine

Generato: 2026-09-23T03:08:41+00:00

> Motore esclusivamente osservativo e Paper-only. Non modifica le uscite reali. I confronti escludono il funding sia dall'uscita originale sia dalle varianti.

## Stato operativo

- Gruppi di trade ancora monitorati: **519**
- Scenari virtuali ancora attivi: **16884**
- Gruppi in attesa dell'uscita originale: **312**
- Gruppi con originale chiuso ma Shadow ancora attive: **207**
- Confronti completati: **698970**

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

Generato: 2026-09-23T03:10:40+00:00

> Modulo esclusivamente valutativo. Non modifica strategie, uscite, posizioni o capitale. Le candidature vengono consegnate al futuro Blocco 5, senza applicazione automatica.

## Stato

- Risultati Block 3 disponibili: **698970**
- Valutazioni prodotte: **29939**
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
Aggiornamento aggregazione UTC: 2026-09-23T03:14:05+00:00
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

Generato: 2026-09-23T03:08:21+00:00

> Paper-only. In mercato NORMAL/WATCH non riduce i segnali. Le limitazioni iniziano soltanto in STRESS, RECOVERY, CRASH, EXTREME o con dati non affidabili.

## Stato corrente

- Livello: **NORMAL**
- Direzione: **NONE**
- Segnali bloccati nel ciclo: **0**
- Simulazioni bloccate attive: **15**
- Simulazioni completate nel ciclo: **0**
- Liquidazioni virtuali evitate totali: **2**
- Valore cumulato del filtro: **835.79 R**
- Profitto virtuale mancato: **1993.38 R**

## Stress test portafogli Paper

| Scenario | Posizioni interessate | Liquidazioni stimate | Perdita stimata EUR |
| --- | ---: | ---: | ---: |
| DOWN_10 | 293 | 0 | 29364.40 |
| DOWN_20 | 293 | 0 | 58728.81 |
| DOWN_30 | 293 | 1 | 88094.06 |
| DOWN_40 | 293 | 65 | 111070.99 |
| UP_10 | 1 | 0 | 147.22 |
| UP_20 | 1 | 0 | 294.44 |
| UP_30 | 1 | 0 | 441.67 |
| UP_40 | 1 | 0 | 588.89 |

## Modello di esecuzione

Se una candela di cascata attraversa nello stesso intervallo sia lo stop sia il prezzo di liquidazione, il Paper usa il caso peggiore e registra una liquidazione intrabar. Gli stop in gap o in regime di stress ricevono slippage aggiuntivo.

## Requisiti prima del live futures

- modalità ISOLATED obbligatoria;
- stop nativo sull'exchange;
- conferma dello stop prima di accettare la posizione;
- cross margin vietato.

# Blocco 5 — Candidati evolutivi controllati

Generato: 2026-09-23T03:06:31+00:00

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

Generato: 2026-09-23T03:14:13+00:00

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

Generato: 2026-09-23T03:14:13+00:00

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

Generato: 2026-09-23T03:14:13+00:00

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

Generato: 2026-09-23T03:14:13+00:00

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
| 1 | SHADOW_COMBO_TREND_SIDE_REGIME_GUARD_V1 | BASELINE | 24.9 | E | 176 | 1.57 | 0.278 | 23.36 |
| 2 | SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_V1 | BASELINE | 22.7 | E | 212 | 1.41 | 0.177 | 14.92 |
| 3 | SHADOW_1H_FAST_V3_NO_ESPORTS_STRESS_GUARD_V1 | BASELINE | 22.5 | E | 194 | 1.27 | 0.123 | 10.66 |
| 4 | SHADOW_DONCHIAN_1H_GB20_120R_V1 | BASELINE | 22.4 | E | 148 | 1.41 | 0.236 | 20.49 |
| 5 | SHADOW_DONCHIAN_1H | BASELINE | 22.3 | E | 180 | 1.37 | 0.217 | 20.49 |
| 6 | SHADOW_1H_FAST_SCORE_6_75_COST_AWARE_V1 | BASELINE | 21.7 | E | 242 | 1.31 | 0.145 | 25.45 |
| 7 | SHADOW_COMBO_ADAPTIVE | BASELINE | 21.2 | E | 251 | 1.30 | 0.146 | 23.82 |
| 8 | SHADOW_1H_FAST_V3_NO_ESPORTS_MFE_LOCK_V1 | BASELINE | 20.0 | E | 272 | 1.17 | 0.083 | 30.08 |
| 9 | SHADOW_COMBO_ADAPTIVE_SIDE_REGIME_GUARD_V1 | BASELINE | 19.7 | E | 203 | 1.18 | 0.098 | 25.62 |
| 10 | SHADOW_COMBO_ADAPTIVE_PARTIAL_1R_V1 | BASELINE | 19.7 | E | 208 | 1.16 | 0.090 | 23.60 |

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

Generato: 2026-09-23T03:14:13+00:00

> Paper-only e advisory. Il blocco misura quali strategie funzionano nei diversi regimi, ma non cambia automaticamente strategia o posizione.

## Stato

- Regime corrente: **BULL_TREND**
- Righe di performance: **1126**
- Strategie preferite nel regime corrente: **20**
- Strategie da evitare nel regime corrente: **3**
- Memorie contestuali: **538**
- Routing automatico: **NO**

## Classifica del regime corrente

| Rank | Portafoglio | Famiglia | Stato | Fitness | Trade | PF | Expectancy R | DD R |
| ---: | --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| 1 | SHADOW_BTC_BOLLINGER_1H | shadow-btc-bollinger-1h | INSUFFICIENT | 80.4 | 1 | 99.00 | 0.621 | 0.00 |
| 2 | SHADOW_BTC_BOLLINGER_4H | shadow-btc-bollinger-4h | INSUFFICIENT | 80.4 | 1 | 99.00 | 0.668 | 0.00 |
| 3 | SHADOW_1H_FAST_SCORE_6_75_RANGE_ONLY_V1 | shadow-1h-fast-score-6-75-range-only-v1 | INSUFFICIENT | 80.4 | 1 | 99.00 | 1.454 | 0.00 |
| 4 | SHADOW_EMA_TREND_1H | shadow-ema-trend-1h | SPECIALIST | 80.0 | 68 | 1.99 | 0.407 | 9.45 |
| 5 | SHADOW_SOL_ADAPTIVE_1H | shadow-sol-adaptive-1h | OBSERVING | 78.5 | 11 | 3.07 | 0.627 | 1.17 |
| 6 | SHADOW_SOL_EMA_1H | shadow-sol-ema-1h | OBSERVING | 77.1 | 11 | 3.08 | 0.627 | 2.14 |
| 7 | SHADOW_SOL_DONCHIAN_1H | shadow-sol-donchian-1h | INSUFFICIENT | 77.0 | 8 | 5.18 | 0.686 | 1.20 |
| 8 | SHADOW_SOL_BOLLINGER_4H | shadow-sol-bollinger-4h | INSUFFICIENT | 75.5 | 3 | 2.66 | 0.572 | 1.04 |
| 9 | SHADOW_SCANNER_TOP5_BTC | shadow-scanner-top5-btc | COMPATIBLE | 75.0 | 82 | 1.98 | 0.434 | 10.21 |
| 10 | EVO_CAND_SHADOW_1H_FAST_V3_NOHIGH_REGIME_GUARD_TP_R200_934590ed | momentum_breakout_v3_filtered | OBSERVING | 74.8 | 12 | 4.37 | 0.378 | 1.07 |

## Sicurezza

- Il regime viene assegnato usando solo l'ultimo record noto prima dell'entrata del trade.
- Nessun uso di dati futuri per classificare il trade.
- Il Candidate Regime Gate è advisory per impostazione predefinita.
- Nessun cambio automatico di MASTER, posizione o live.

# Blocco 11 — Collegamento protetto al live

Generato: 2026-09-23T03:14:14+00:00

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

Generato: 2026-09-23T03:08:21+00:00

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
