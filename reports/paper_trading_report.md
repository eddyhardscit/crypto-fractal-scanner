# Paper trading automatico KuCoin

Generato: 2026-08-27T05:33:24+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-08-27T05:05:29+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-08-27T05:05:29+00:00 | 2026-08-27T05:05:29+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-08-27T04:45:00+00:00 | 2026-08-27T04:45:00+00:00 | 5,6 min | 25,0 min | OK |
| 60m | 12 | 2026-08-27T04:00:00+00:00 | 2026-08-27T04:00:00+00:00 | 5,6 min | 45,0 min | OK |
| 240m | 12 | 2026-08-27T00:00:00+00:00 | 2026-08-27T00:00:00+00:00 | 1,09 h | 1,00 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1H Fast Nohigh Cap75 Short Only V1 | BTR | 60m | LONG | 5,75 | 4,50 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Master Adaptive Gb20 Partial V1 | BTR | 60m | LONG | 5,75 | 0,00 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Master Adaptive Gb20 Be V1 | BTR | 60m | LONG | 5,75 | 0,00 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Master Adaptive Runner25 V1 | SKHYNIX | 60m | LONG | 5,20 | 0,00 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Master Adaptive Gb20 V1 | BTR | 60m | LONG | 5,75 | 0,00 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Master Adaptive No Alt V1 | SKHYNIX | 60m | LONG | 5,20 | 0,00 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Master Adaptive V1 | BTR | 60m | LONG | 5,75 | 0,00 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Principale 4H | ENA | 240m | LONG | 4,25 | 6,00 | 1,75 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | HYPE | 240m | LONG | 4,14 | 6,00 | 1,86 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | SKHYNIX | 240m | LONG | 3,54 | 6,00 | 2,46 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | BTC | 240m | LONG | 3,25 | 6,00 | 2,75 | STALE_CANDLE | 1,09 h | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | SUI | 240m | SHORT | -2,75 | 6,00 | 3,25 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | ZEC | 240m | LONG | 2,72 | 6,00 | 3,28 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | PEPE | 240m | LONG | 1,02 | 6,00 | 4,98 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | XRP | 240m | LONG | 0,89 | 6,00 | 5,11 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | DOGE | 240m | SHORT | -0,80 | 6,00 | 5,20 | STALE_CANDLE | 1,09 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| 1H Balanced Long No Rhv V1 | BTR | 60m | LONG | 5,75 | 5,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Fast Nohigh Cap75 V1 | BTR | 60m | LONG | 5,75 | 4,50 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Long Btc 1 3 Cap75 V1 | BTR | 60m | LONG | 5,75 | 4,50 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast No Pepe V1 | BTR | 60m | LONG | 5,75 | 4,50 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Tp2 V1 | BTR | 60m | LONG | 5,75 | 4,50 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Benchmark trend following EMA 1H | BTR | 60m | LONG | 5,75 | 5,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Scanner Top 5 Long 1H | BTR | 60m | LONG | 5,75 | 5,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Scanner Top10 Long | BTR | 60m | LONG | 5,75 | 5,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Scanner Top15 Long | BTR | 60m | LONG | 5,75 | 5,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Scanner Top20 Long | BTR | 60m | LONG | 5,75 | 5,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Scanner Top 5 + forza BTC 1H | BTR | 60m | LONG | 5,75 | 5,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.807,62 | -1,92% | €59,28 | €3.000,00 | 1,98% | 6 | 52 | 38,46% | 0,87 | 6,86% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 52 | 2289 | PRIME INDICAZIONI | 100 (mancano 48) |

- Trade del Principale 4H chiusi: **52**; win rate **38,46%**; profit factor **0,87**.
- Expectancy: **€-3,67** per trade; P&L netto: **€-190,76**; max drawdown: **6,86%**.
- Valutazione: **Si può osservare la direzione, ma il risultato resta fragile.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 6 | €9.807,62 | €699,00 | €2.096,99 | €196,05 | €-0,51 |
| TEST | Benchmark Donchian breakout 1H | 6 | €11.290,01 | €2.894,15 | €5.788,31 | €221,61 | €66,62 |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | 6 | €11.087,05 | €2.865,79 | €8.597,37 | €175,88 | €-18,15 |
| TEST | Combo Trend Side Regime Guard V1 | 5 | €11.059,81 | €3.827,11 | €7.654,22 | €167,60 | €-7,47 |
| TEST | Donchian 1H Gb20 120R V1 | 6 | €11.024,19 | €2.826,01 | €5.652,03 | €216,39 | €65,05 |
| TEST | Scanner Top 5 Long 1H | 5 | €10.847,57 | €3.462,60 | €6.925,20 | €216,98 | €-11,21 |
| TEST | Main Side Regime Guard V1 | 6 | €10.821,50 | €672,38 | €2.017,15 | €163,22 | €78,33 |
| TEST | 1H Fast No Pepe V1 | 9 | €10.599,14 | €2.055,48 | €6.166,45 | €211,40 | €-35,68 |
| TEST | Combo Adaptive | 7 | €10.561,80 | €3.499,76 | €6.999,53 | €212,39 | €-54,27 |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | 5 | €10.409,37 | €2.325,05 | €6.975,16 | €208,88 | €-32,33 |
| TEST | Rapida 1H V3 Filtered | 5 | €10.342,49 | €2.310,11 | €6.930,34 | €207,54 | €-32,12 |
| TEST | Combo Adaptive Side Regime Guard V1 | 5 | €10.342,22 | €2.490,20 | €4.980,39 | €155,69 | €-50,25 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 0 | €10.300,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Ampia 4H | 7 | €10.276,43 | €1.057,57 | €2.115,14 | €205,57 | €-2,91 |
| TEST | Combo Adaptive Long Only V1 | 5 | €10.274,96 | €4.512,56 | €9.025,12 | €206,73 | €-28,89 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 0 | €10.271,73 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Nohigh Cap75 V1 | 8 | €10.252,80 | €1.968,40 | €5.905,21 | €204,38 | €-34,46 |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | 4 | €10.250,92 | €2.678,99 | €8.036,96 | €151,87 | €-12,64 |
| TEST | 1H Fast V3 Nohigh Range Only V1 | 0 | €10.247,95 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 0 | €10.239,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 0 | €10.235,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 4H | 1 | €10.213,16 | €367,30 | €734,59 | €50,97 | €19,64 |
| TEST | Btc Bollinger 1H | 0 | €10.209,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Donchian 1H | 1 | €10.209,11 | €828,76 | €2.486,27 | €0,00 | €17,98 |
| TEST | Sol Donchian 4H | 0 | €10.196,46 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Tp2 V1 | 6 | €10.195,40 | €1.795,80 | €5.387,40 | €154,19 | €-31,25 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 0 | €10.185,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Main Dynamic Asset Selector V1 | 0 | €10.161,45 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Score 6 75 Range Only V1 | 0 | €10.149,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 0 | €10.145,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | 2 | €10.124,13 | €2.312,44 | €6.937,33 | €47,99 | €-11,27 |
| TEST | Rapida 1H V2 | 2 | €10.110,49 | €2.386,94 | €7.160,82 | €50,64 | €-13,04 |
| TEST | Sol Ema 1H | 1 | €10.099,15 | €728,87 | €2.186,61 | €50,42 | €15,82 |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 0 | €10.099,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 4H | 1 | €10.076,72 | €395,27 | €790,53 | €50,28 | €21,13 |
| TEST | Scanner Top 5 + forza BTC 1H | 5 | €10.073,02 | €3.227,27 | €6.454,55 | €202,28 | €-10,57 |
| TEST | Btc Bollinger 4H | 1 | €10.061,24 | €775,58 | €1.551,16 | €50,15 | €32,35 |
| TEST | Combo Adaptive Partial 1R V1 | 7 | €10.049,82 | €2.013,69 | €4.027,37 | €150,19 | €-26,06 |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 0 | €10.048,77 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €10.045,08 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V1 | 0 | €10.043,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 4H | 1 | €10.041,52 | €648,94 | €1.297,88 | €50,35 | €-27,57 |
| TEST | 1H Balanced Short Trend Down Strict V1 | 0 | €10.035,46 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · prudente · 5x | 0 | €10.028,67 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €50 · 15x | 0 | €10.017,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top10 Long | 4 | €10.014,31 | €4.430,46 | €8.860,92 | €201,18 | €-35,39 |
| TEST | Scalp RSI Short 80 · €50 · 15x | 0 | €10.009,36 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 0 | €10.009,02 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 0 | €10.008,92 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €10 · 15x | 0 | €10.003,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 0 | €10.003,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Tp3 V1 | 4 | €10.001,89 | €3.960,24 | €7.920,49 | €201,25 | €-28,69 |
| TEST | Scalp RSI Short 80 · €10 · 15x | 0 | €10.001,87 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Continuation V1 | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €10 · 15x | 0 | €9.999,33 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | 8 | €9.997,66 | €1.919,42 | €5.758,26 | €199,29 | €-33,60 |
| TEST | Scalp RSI Long 15 · €10 · 15x | 0 | €9.997,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €50 · 15x | 0 | €9.996,64 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Runner25 V1 | 4 | €9.996,04 | €3.957,93 | €7.915,85 | €201,13 | €-28,67 |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 0 | €9.995,23 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Bollinger 1H | 0 | €9.992,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · prudente · 5x | 0 | €9.991,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €10 · 15x | 0 | €9.990,45 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Ema 1H | 0 | €9.988,85 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 4H | 1 | €9.988,30 | €704,37 | €1.408,74 | €50,10 | €-29,93 |
| TEST | Scalp RSI Long 15 · €50 · 15x | 0 | €9.988,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 0 | €9.987,48 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · prudente · 5x | 0 | €9.980,94 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 4H | 1 | €9.974,11 | €435,50 | €871,00 | €49,91 | €-7,12 |
| TEST | Bilanciata 1H V3 Filtered | 6 | €9.973,34 | €1.587,80 | €4.763,39 | €200,34 | €-1,98 |
| TEST | Btc Adaptive 1H | 0 | €9.968,58 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 1H | 0 | €9.957,15 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 1H | 1 | €9.955,52 | €718,50 | €2.155,51 | €49,71 | €15,59 |
| TEST | Scalp RSI Long 25 · €50 · 15x | 0 | €9.952,25 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Ema 4H | 1 | €9.948,10 | €487,73 | €975,47 | €49,56 | €37,97 |
| TEST | Scalp RSI Short 80 · prudente · 5x | 0 | €9.940,42 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.939,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 4H | 1 | €9.934,86 | €700,60 | €1.401,20 | €49,83 | €-29,77 |
| TEST | Doge Donchian 1H | 0 | €9.924,84 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | 0 | €9.912,24 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | 5 | €9.869,22 | €3.124,54 | €9.373,63 | €197,39 | €-97,43 |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 0 | €9.837,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 1H | 1 | €9.835,77 | €797,97 | €2.393,90 | €49,11 | €16,01 |
| TEST | Btc Ema 1H | 0 | €9.833,66 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 No Esports Long Only V1 | 4 | €9.824,53 | €2.388,05 | €7.164,14 | €147,25 | €-50,27 |
| TEST | Combo Adaptive Regime V1 | 4 | €9.824,32 | €3.823,27 | €7.646,53 | €147,25 | €-4,33 |
| TEST | Eth Adaptive 1H | 1 | €9.817,39 | €1.094,40 | €3.283,20 | €49,22 | €-25,27 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 0 | €9.817,34 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Ema 1H | 1 | €9.798,25 | €1.072,00 | €3.216,01 | €49,07 | €-13,40 |
| TEST | Combo Adaptive Quality7 Regime V1 | 0 | €9.787,56 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 0 | €9.762,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Forza relativa 1H V2 | 4 | €9.739,55 | €2.188,10 | €4.376,21 | €97,76 | €5,01 |
| TEST | Combo Adaptive Quality7 V1 | 3 | €9.738,12 | €1.894,84 | €3.789,69 | €145,51 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 0 | €9.723,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Bollinger 1H | 0 | €9.703,71 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top15 Long | 6 | €9.685,66 | €3.793,14 | €7.586,29 | €194,49 | €-30,23 |
| TEST | Scanner Top20 Long | 6 | €9.685,66 | €3.793,14 | €7.586,29 | €194,49 | €-30,23 |
| TEST | Global Confluence puro 1H | 0 | €9.679,31 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Scanner | 5 | €9.677,88 | €3.099,48 | €6.198,96 | €194,35 | €-10,17 |
| TEST | Eth Donchian 1H | 1 | €9.647,94 | €1.210,37 | €3.631,11 | €48,39 | €-27,95 |
| TEST | 1H Fast V3 No Esports V1 | 5 | €9.629,18 | €1.800,27 | €5.400,81 | €193,25 | €-30,95 |
| TEST | 1H Balanced Long No Rhv V1 | 5 | €9.622,82 | €2.080,20 | €6.240,60 | €193,38 | €14,69 |
| TEST | 1H Fast V3 Nohigh V1 | 5 | €9.612,09 | €2.504,83 | €7.514,48 | €192,45 | €-49,56 |
| TEST | Scanner Top5 Btc Guard V1 | 4 | €9.604,38 | €1.449,43 | €2.898,86 | €97,98 | €64,91 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 0 | €9.579,83 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | 2 | €9.548,64 | €2.181,72 | €6.545,17 | €94,94 | €-48,86 |
| TEST | Master Adaptive Runner25 V1 | 6 | €9.472,98 | €3.655,55 | €7.311,11 | €189,46 | €152,60 |
| TEST | Bilanciata 1H V2 | 3 | €9.460,20 | €2.163,09 | €6.489,26 | €140,73 | €32,50 |
| TEST | 1H Fast V3 Long Only V1 | 5 | €9.458,74 | €2.846,04 | €8.538,13 | €190,06 | €-48,29 |
| TEST | Scanner Top5 Btc Mfe V1 | 5 | €9.442,96 | €3.025,41 | €6.050,82 | €189,63 | €-9,91 |
| TEST | Master Adaptive Gb20 Be V1 | 5 | €9.434,99 | €3.567,70 | €7.135,40 | €188,41 | €-13,11 |
| TEST | 1H Balanced V3 Long Only V1 | 6 | €9.433,84 | €1.505,55 | €4.516,64 | €189,51 | €-2,50 |
| TEST | Master Adaptive No Alt V1 | 5 | €9.426,72 | €3.594,72 | €7.189,44 | €188,54 | €39,26 |
| TEST | Master Adaptive Gb20 Partial V1 | 5 | €9.424,96 | €3.563,91 | €7.127,82 | €188,21 | €-13,10 |
| TEST | 1H Fast Score 6 75 V1 | 0 | €9.415,87 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive V1 | 5 | €9.388,50 | €3.550,12 | €7.100,25 | €187,48 | €-13,05 |
| TEST | Scanner Top5 Btc Guard Mfe V1 | 4 | €9.381,02 | €1.415,72 | €2.831,44 | €95,70 | €63,40 |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | 2 | €9.370,06 | €2.147,45 | €6.442,35 | €93,39 | €-48,09 |
| TEST | Master Adaptive Expanded V1 | 5 | €9.357,25 | €3.581,77 | €7.163,54 | €187,75 | €-28,86 |
| TEST | Combo Trend | 5 | €9.331,16 | €2.556,81 | €5.113,62 | €140,82 | €-37,73 |
| TEST | Scanner Bottom10 Short | 4 | €9.320,74 | €1.261,36 | €2.522,73 | €140,86 | €0,00 |
| TEST | Scanner Bottom15 Short | 4 | €9.320,74 | €1.261,36 | €2.522,73 | €140,86 | €0,00 |
| TEST | Scanner Bottom20 Short | 4 | €9.320,74 | €1.261,36 | €2.522,73 | €140,86 | €0,00 |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | 4 | €9.320,05 | €3.676,85 | €7.353,70 | €139,88 | €21,49 |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | 3 | €9.304,57 | €1.213,15 | €2.426,29 | €49,07 | €62,88 |
| TEST | Master Adaptive Gb20 V1 | 5 | €9.263,76 | €3.502,95 | €7.005,91 | €184,99 | €-12,88 |
| TEST | Master Adaptive Gb20 Loss Cap V1 | 4 | €9.261,89 | €3.376,65 | €6.753,29 | €137,95 | €-24,57 |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | 4 | €9.256,15 | €1.252,64 | €2.505,29 | €139,88 | €0,00 |
| TEST | Benchmark trend following EMA 1H | 5 | €9.255,55 | €1.267,77 | €2.535,55 | €140,48 | €-1,37 |
| TEST | Scanner Bottom5 Short Profit Lock V1 | 4 | €9.242,07 | €1.250,74 | €2.501,48 | €139,67 | €0,00 |
| TEST | Scanner Bottom 5 Short 1H | 4 | €9.170,95 | €1.241,11 | €2.482,23 | €138,60 | €0,00 |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | 0 | €9.165,52 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H V1 | 0 | €9.150,69 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | 2 | €9.142,42 | €1.179,53 | €2.359,05 | €45,66 | €61,79 |
| TEST | 1H Fast V3 Cap75 V1 | 0 | €9.106,22 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Mfe Trail | 6 | €9.072,48 | €2.850,43 | €5.700,85 | €182,13 | €-24,35 |
| TEST | Combo Mean Reversion | 0 | €8.967,07 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Runner25 V1 | 0 | €8.964,11 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Strict3 V1 | 2 | €8.881,45 | €2.396,63 | €4.793,26 | €89,27 | €-26,92 |
| TEST | Scanner Top5 Btc Btc Le3 V1 | 4 | €8.864,81 | €3.497,25 | €6.994,50 | €133,05 | €20,44 |
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
| PRINCIPALE | Principale 4H | Confluenza trend | €9.807,62 | €-190,76 | 52 | 52 | 38,46% | 0,87 | €-3,67 | 6,86% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €11.290,01 | €1.225,61 | 105 | 105 | 47,62% | 1,51 | €11,67 | 5,85% |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | Momentum / breakout | €11.087,05 | €1.110,49 | 145 | 145 | 53,10% | 1,39 | €7,66 | 5,23% |
| TEST | Combo Trend Side Regime Guard V1 | Combo Trend | €11.059,81 | €1.071,48 | 111 | 111 | 54,05% | 1,53 | €9,65 | 6,20% |
| TEST | Donchian 1H Gb20 120R V1 | Donchian breakout 20 barre | €11.024,19 | €961,32 | 73 | 73 | 46,58% | 1,64 | €13,17 | 5,85% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.847,57 | €862,97 | 139 | 139 | 47,48% | 1,32 | €6,21 | 8,85% |
| TEST | Main Side Regime Guard V1 | Confluenza trend | €10.821,50 | €744,99 | 35 | 35 | 54,29% | 2,09 | €21,29 | 3,82% |
| TEST | 1H Fast No Pepe V1 | Momentum / breakout | €10.599,14 | €638,62 | 211 | 211 | 47,39% | 1,16 | €3,03 | 7,45% |
| TEST | Combo Adaptive | Combo Adaptive | €10.561,80 | €621,13 | 147 | 147 | 46,26% | 1,25 | €4,23 | 7,91% |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | Momentum / breakout V3 Filtered | €10.409,37 | €446,00 | 190 | 190 | 50,00% | 1,14 | €2,35 | 9,50% |
| TEST | Rapida 1H V3 Filtered | Momentum / breakout V3 Filtered | €10.342,49 | €378,89 | 234 | 234 | 44,44% | 1,09 | €1,62 | 9,48% |
| TEST | Combo Adaptive Side Regime Guard V1 | Combo Adaptive | €10.342,22 | €396,27 | 115 | 115 | 47,83% | 1,17 | €3,45 | 8,68% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | Momentum / breakout V3 Filtered | €10.300,05 | €300,05 | 33 | 33 | 48,48% | 2,04 | €9,09 | 2,01% |
| TEST | Ampia 4H | Confluenza trend | €10.276,43 | €280,43 | 52 | 52 | 34,62% | 1,24 | €5,39 | 4,45% |
| TEST | Combo Adaptive Long Only V1 | Combo Adaptive | €10.274,96 | €309,26 | 120 | 120 | 46,67% | 1,12 | €2,58 | 7,78% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | Momentum / breakout V3 Filtered | €10.271,73 | €271,73 | 22 | 22 | 50,00% | 1,74 | €12,35 | 1,72% |
| TEST | 1H Fast Nohigh Cap75 V1 | Momentum / breakout | €10.252,80 | €290,80 | 136 | 136 | 44,85% | 1,10 | €2,14 | 7,10% |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | Momentum / breakout V3 Filtered | €10.250,92 | €268,39 | 72 | 72 | 48,61% | 1,18 | €3,73 | 5,24% |
| TEST | 1H Fast V3 Nohigh Range Only V1 | Momentum / breakout V3 Filtered | €10.247,95 | €247,95 | 41 | 41 | 46,34% | 1,25 | €6,05 | 3,97% |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | Momentum / breakout V3 Filtered | €10.239,20 | €239,20 | 17 | 17 | 52,94% | 4,50 | €14,07 | 1,01% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | Momentum / breakout V3 Filtered | €10.235,18 | €235,18 | 20 | 20 | 50,00% | 1,90 | €11,76 | 2,73% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €10.213,16 | €193,98 | 7 | 7 | 57,14% | 2,72 | €27,71 | 1,01% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.209,20 | €209,20 | 6 | 6 | 83,33% | 4,66 | €34,87 | 0,85% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €10.209,11 | €192,62 | 13 | 13 | 53,85% | 1,78 | €14,82 | 2,77% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €10.196,46 | €196,46 | 6 | 6 | 50,00% | 2,73 | €32,74 | 1,05% |
| TEST | 1H Fast Tp2 V1 | Momentum / breakout | €10.195,40 | €229,87 | 227 | 227 | 40,09% | 1,06 | €1,01 | 6,56% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | Momentum / breakout V3 Filtered | €10.185,37 | €185,37 | 22 | 22 | 40,91% | 1,57 | €8,43 | 2,27% |
| TEST | Main Dynamic Asset Selector V1 | Confluenza trend | €10.161,45 | €161,45 | 13 | 13 | 38,46% | 1,47 | €12,42 | 2,04% |
| TEST | 1H Fast Score 6 75 Range Only V1 | Momentum / breakout | €10.149,62 | €149,62 | 38 | 38 | 44,74% | 1,14 | €3,94 | 3,35% |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | Momentum / breakout V3 Filtered | €10.145,12 | €145,12 | 44 | 44 | 45,45% | 1,20 | €3,30 | 2,91% |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | Momentum / breakout V3 Filtered | €10.124,13 | €139,56 | 53 | 53 | 50,94% | 1,12 | €2,63 | 4,50% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €10.110,49 | €127,83 | 46 | 41 | 45,65% | 1,11 | €2,78 | 3,89% |
| TEST | Sol Ema 1H | Trend following EMA | €10.099,15 | €84,65 | 14 | 14 | 42,86% | 1,22 | €6,05 | 3,33% |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | Momentum / breakout V3 Filtered | €10.099,04 | €99,04 | 55 | 55 | 54,55% | 1,12 | €1,80 | 3,59% |
| TEST | Sol Ema 4H | Trend following EMA | €10.076,72 | €56,08 | 8 | 8 | 37,50% | 1,26 | €7,01 | 2,27% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €10.073,02 | €87,49 | 125 | 125 | 44,00% | 1,03 | €0,70 | 11,27% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.061,24 | €29,45 | 2 | 2 | 50,00% | 1,54 | €14,72 | 0,91% |
| TEST | Combo Adaptive Partial 1R V1 | Combo Adaptive | €10.049,82 | €78,27 | 152 | 152 | 44,74% | 1,03 | €0,51 | 8,69% |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | Momentum / breakout V3 Filtered | €10.048,77 | €48,77 | 23 | 23 | 43,48% | 1,12 | €2,12 | 3,05% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €10.045,08 | €45,08 | 28 | 28 | 46,43% | 1,40 | €1,61 | 0,33% |
| TEST | Rapida 1H V1 | Momentum / breakout | €10.043,28 | €43,28 | 78 | 78 | 34,62% | 1,02 | €0,55 | 6,76% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €10.041,52 | €70,19 | 2 | 2 | 50,00% | 2,39 | €35,09 | 0,96% |
| TEST | 1H Balanced Short Trend Down Strict V1 | Confluenza trend | €10.035,46 | €35,46 | 13 | 13 | 38,46% | 1,13 | €2,73 | 1,80% |
| TEST | Scalp RSI Long 20 · prudente · 5x | Inversione RSI estrema 15m | €10.028,67 | €28,67 | 9 | 9 | 55,56% | 1,80 | €3,19 | 0,36% |
| TEST | Scalp RSI Short 85 · €50 · 15x | Inversione RSI estrema 15m | €10.017,98 | €17,98 | 5 | 5 | 60,00% | 1,69 | €3,60 | 0,31% |
| TEST | Scanner Top10 Long | Scanner Top10 Long | €10.014,31 | €55,02 | 128 | 128 | 47,66% | 1,02 | €0,43 | 10,31% |
| TEST | Scalp RSI Short 80 · €50 · 15x | Inversione RSI estrema 15m | €10.009,36 | €9,36 | 16 | 16 | 37,50% | 1,17 | €0,58 | 0,53% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €10.009,02 | €9,02 | 28 | 28 | 46,43% | 1,40 | €0,32 | 0,07% |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | Momentum / breakout V3 Filtered | €10.008,92 | €8,92 | 30 | 30 | 36,67% | 1,02 | €0,30 | 4,84% |
| TEST | Scalp RSI Short 85 · €10 · 15x | Inversione RSI estrema 15m | €10.003,60 | €3,60 | 5 | 5 | 60,00% | 1,69 | €0,72 | 0,06% |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | Momentum / breakout V3 Filtered | €10.003,37 | €3,37 | 8 | 8 | 37,50% | 1,02 | €0,42 | 2,15% |
| TEST | Scanner Top5 Btc Tp3 V1 | Scanner Top 5 + forza BTC | €10.001,89 | €35,33 | 105 | 105 | 40,95% | 1,01 | €0,34 | 11,78% |
| TEST | Scalp RSI Short 80 · €10 · 15x | Inversione RSI estrema 15m | €10.001,87 | €1,87 | 16 | 16 | 37,50% | 1,17 | €0,12 | 0,11% |
| TEST | Scanner Bottom5 Short Continuation V1 | Scanner Bottom5 Short Continuation | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 20 · €10 · 15x | Inversione RSI estrema 15m | €9.999,33 | €-0,67 | 9 | 9 | 44,44% | 0,85 | €-0,07 | 0,04% |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | Momentum / breakout | €9.997,66 | €34,72 | 100 | 100 | 44,00% | 1,02 | €0,35 | 7,10% |
| TEST | Scalp RSI Long 15 · €10 · 15x | Inversione RSI estrema 15m | €9.997,60 | €-2,40 | 3 | 3 | 33,33% | 0,13 | €-0,80 | 0,02% |
| TEST | Scalp RSI Long 20 · €50 · 15x | Inversione RSI estrema 15m | €9.996,64 | €-3,36 | 9 | 9 | 44,44% | 0,85 | €-0,37 | 0,21% |
| TEST | Scanner Top5 Btc Runner25 V1 | Scanner Top 5 + forza BTC | €9.996,04 | €29,46 | 109 | 109 | 41,28% | 1,01 | €0,27 | 12,06% |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | Momentum / breakout V3 Filtered | €9.995,23 | €-4,77 | 15 | 15 | 46,67% | 0,99 | €-0,32 | 2,70% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €9.992,60 | €-7,40 | 10 | 10 | 50,00% | 0,97 | €-0,74 | 1,89% |
| TEST | Scalp RSI Short 85 · prudente · 5x | Inversione RSI estrema 15m | €9.991,38 | €-8,62 | 5 | 5 | 60,00% | 0,61 | €-1,72 | 0,30% |
| TEST | Scalp RSI Long 25 · €10 · 15x | Inversione RSI estrema 15m | €9.990,45 | €-9,55 | 15 | 15 | 40,00% | 0,36 | €-0,64 | 0,14% |
| TEST | Doge Ema 1H | Trend following EMA | €9.988,85 | €-11,15 | 17 | 17 | 58,82% | 0,97 | €-0,66 | 2,77% |
| TEST | Btc Ema 4H | Trend following EMA | €9.988,30 | €19,41 | 3 | 3 | 33,33% | 1,19 | €6,47 | 1,76% |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | €9.988,00 | €-12,00 | 3 | 3 | 33,33% | 0,13 | €-4,00 | 0,12% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €9.987,48 | €-12,52 | 15 | 15 | 40,00% | 0,83 | €-0,83 | 0,71% |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | €9.980,94 | €-19,06 | 3 | 3 | 33,33% | 0,19 | €-6,35 | 0,20% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €9.974,11 | €-18,28 | 3 | 3 | 33,33% | 0,83 | €-6,09 | 1,36% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €9.973,34 | €-20,28 | 152 | 152 | 42,11% | 0,99 | €-0,13 | 9,12% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €9.968,58 | €-31,42 | 9 | 9 | 44,44% | 0,86 | €-3,49 | 1,23% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €9.957,15 | €-42,85 | 10 | 10 | 50,00% | 0,85 | €-4,29 | 1,49% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €9.955,52 | €-58,78 | 15 | 15 | 40,00% | 0,87 | €-3,92 | 4,59% |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | €9.952,25 | €-47,75 | 15 | 15 | 40,00% | 0,36 | €-3,18 | 0,72% |
| TEST | Eth Ema 4H | Trend following EMA | €9.948,10 | €-88,72 | 5 | 5 | 20,00% | 0,58 | €-17,74 | 1,83% |
| TEST | Scalp RSI Short 80 · prudente · 5x | Inversione RSI estrema 15m | €9.940,42 | €-59,58 | 16 | 16 | 37,50% | 0,40 | €-3,72 | 0,89% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.939,62 | €-60,38 | 28 | 28 | 46,43% | 0,60 | €-2,16 | 0,84% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €9.934,86 | €-34,19 | 4 | 4 | 25,00% | 0,80 | €-8,55 | 2,43% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €9.924,84 | €-75,16 | 13 | 13 | 53,85% | 0,79 | €-5,78 | 3,08% |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | Combo Adaptive | €9.912,24 | €-87,76 | 39 | 39 | 46,15% | 0,91 | €-2,25 | 4,21% |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | Momentum / breakout | €9.869,22 | €-27,73 | 63 | 63 | 41,27% | 0,98 | €-0,44 | 3,73% |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | Momentum / breakout V3 Filtered | €9.837,38 | €-162,62 | 37 | 37 | 40,54% | 0,76 | €-4,40 | 3,08% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.835,77 | €-178,80 | 11 | 11 | 36,36% | 0,61 | €-16,25 | 2,37% |
| TEST | Btc Ema 1H | Trend following EMA | €9.833,66 | €-166,34 | 13 | 13 | 30,77% | 0,61 | €-12,80 | 1,94% |
| TEST | 1H Fast V3 No Esports Long Only V1 | Momentum / breakout V3 Filtered | €9.824,53 | €-120,90 | 154 | 154 | 43,51% | 0,96 | €-0,79 | 10,60% |
| TEST | Combo Adaptive Regime V1 | Combo Adaptive | €9.824,32 | €-166,77 | 58 | 58 | 48,28% | 0,88 | €-2,88 | 5,38% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.817,39 | €-155,37 | 13 | 13 | 38,46% | 0,66 | €-11,95 | 3,14% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | Momentum / breakout V3 Filtered | €9.817,34 | €-182,66 | 24 | 24 | 41,67% | 0,64 | €-7,61 | 3,23% |
| TEST | Eth Ema 1H | Trend following EMA | €9.798,25 | €-186,42 | 18 | 18 | 38,89% | 0,71 | €-10,36 | 4,80% |
| TEST | Combo Adaptive Quality7 Regime V1 | Combo Adaptive | €9.787,56 | €-212,44 | 39 | 39 | 41,03% | 0,79 | €-5,45 | 5,41% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | Momentum / breakout V3 Filtered | €9.762,18 | €-237,82 | 7 | 7 | 14,29% | 0,02 | €-33,97 | 2,82% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €9.739,55 | €-262,74 | 112 | 106 | 41,96% | 0,92 | €-2,35 | 10,88% |
| TEST | Combo Adaptive Quality7 V1 | Combo Adaptive | €9.738,12 | €-259,61 | 80 | 80 | 38,75% | 0,87 | €-3,25 | 8,88% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | Momentum / breakout V3 Filtered | €9.723,72 | €-276,28 | 31 | 31 | 32,26% | 0,62 | €-8,91 | 4,83% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €9.703,71 | €-296,29 | 7 | 7 | 28,57% | 0,22 | €-42,33 | 4,16% |
| TEST | Scanner Top15 Long | Scanner Top15 Long | €9.685,66 | €-279,53 | 125 | 125 | 47,20% | 0,89 | €-2,24 | 10,31% |
| TEST | Scanner Top20 Long | Scanner Top20 Long | €9.685,66 | €-279,53 | 125 | 125 | 47,20% | 0,89 | €-2,24 | 10,31% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.679,31 | €-320,69 | 17 | 17 | 29,41% | 0,41 | €-18,86 | 3,93% |
| TEST | Combo Scanner | Combo Scanner | €9.677,88 | €-308,19 | 130 | 130 | 43,85% | 0,90 | €-2,37 | 11,38% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.647,94 | €-321,93 | 13 | 13 | 23,08% | 0,47 | €-24,76 | 3,74% |
| TEST | 1H Fast V3 No Esports V1 | Momentum / breakout V3 Filtered | €9.629,18 | €-336,51 | 204 | 204 | 43,14% | 0,92 | €-1,65 | 9,00% |
| TEST | 1H Balanced Long No Rhv V1 | Confluenza trend | €9.622,82 | €-388,06 | 99 | 99 | 44,44% | 0,82 | €-3,92 | 9,26% |
| TEST | 1H Fast V3 Nohigh V1 | Momentum / breakout V3 Filtered | €9.612,09 | €-333,85 | 123 | 123 | 43,09% | 0,88 | €-2,71 | 7,10% |
| TEST | Scanner Top5 Btc Guard V1 | Scanner Top 5 + forza BTC | €9.604,38 | €-458,79 | 106 | 106 | 38,68% | 0,83 | €-4,33 | 7,34% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | Momentum / breakout V3 Filtered | €9.579,83 | €-420,17 | 11 | 11 | 0,00% | 0,00 | €-38,20 | 4,20% |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | Momentum / breakout V3 Filtered | €9.548,64 | €-398,58 | 82 | 82 | 40,24% | 0,82 | €-4,86 | 6,64% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €9.472,98 | €-674,88 | 52 | 52 | 30,77% | 0,64 | €-12,98 | 8,18% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €9.460,20 | €-568,34 | 103 | 94 | 42,72% | 0,75 | €-5,52 | 8,84% |
| TEST | 1H Fast V3 Long Only V1 | Momentum / breakout V3 Filtered | €9.458,74 | €-487,84 | 165 | 165 | 40,61% | 0,86 | €-2,96 | 12,52% |
| TEST | Scanner Top5 Btc Mfe V1 | Scanner Top 5 + forza BTC | €9.442,96 | €-543,47 | 117 | 117 | 42,74% | 0,78 | €-4,65 | 12,28% |
| TEST | Master Adaptive Gb20 Be V1 | Master Adaptive Consensus | €9.434,99 | €-547,27 | 59 | 59 | 30,51% | 0,69 | €-9,28 | 8,39% |
| TEST | 1H Balanced V3 Long Only V1 | Confluenza trend V3 Filtered | €9.433,84 | €-559,50 | 106 | 106 | 42,45% | 0,73 | €-5,28 | 8,85% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €9.426,72 | €-607,88 | 60 | 60 | 35,00% | 0,70 | €-10,13 | 7,26% |
| TEST | Master Adaptive Gb20 Partial V1 | Master Adaptive Consensus | €9.424,96 | €-557,32 | 54 | 54 | 35,19% | 0,68 | €-10,32 | 7,98% |
| TEST | 1H Fast Score 6 75 V1 | Momentum / breakout | €9.415,87 | €-584,13 | 137 | 137 | 40,15% | 0,84 | €-4,26 | 12,33% |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | €9.388,50 | €-593,85 | 56 | 56 | 33,93% | 0,69 | €-10,60 | 7,80% |
| TEST | Scanner Top5 Btc Guard Mfe V1 | Scanner Top 5 + forza BTC | €9.381,02 | €-680,68 | 123 | 123 | 39,84% | 0,77 | €-5,53 | 8,78% |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | Momentum / breakout V3 Filtered | €9.370,06 | €-577,98 | 87 | 87 | 44,83% | 0,78 | €-6,64 | 8,22% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €9.357,25 | €-609,24 | 66 | 66 | 36,36% | 0,71 | €-9,23 | 7,96% |
| TEST | Combo Trend | Combo Trend | €9.331,16 | €-627,65 | 154 | 154 | 38,96% | 0,83 | €-4,08 | 10,85% |
| TEST | Scanner Bottom10 Short | Scanner Bottom10 Short | €9.320,74 | €-677,79 | 70 | 70 | 31,43% | 0,65 | €-9,68 | 9,06% |
| TEST | Scanner Bottom15 Short | Scanner Bottom15 Short | €9.320,74 | €-677,79 | 70 | 70 | 31,43% | 0,65 | €-9,68 | 9,06% |
| TEST | Scanner Bottom20 Short | Scanner Bottom20 Short | €9.320,74 | €-677,79 | 70 | 70 | 31,43% | 0,65 | €-9,68 | 9,06% |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | Scanner Top 5 + forza BTC | €9.320,05 | €-697,02 | 26 | 26 | 19,23% | 0,26 | €-26,81 | 8,44% |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | Scanner Top 5 + forza BTC | €9.304,57 | €-756,85 | 70 | 70 | 35,71% | 0,66 | €-10,81 | 9,79% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €9.263,76 | €-718,82 | 91 | 91 | 48,35% | 0,65 | €-7,90 | 9,02% |
| TEST | Master Adaptive Gb20 Loss Cap V1 | Master Adaptive Consensus | €9.261,89 | €-709,49 | 48 | 48 | 25,00% | 0,61 | €-14,78 | 11,41% |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | Scanner Bottom 5 Short | €9.256,15 | €-742,38 | 61 | 61 | 31,15% | 0,58 | €-12,17 | 9,08% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.255,55 | €-741,47 | 125 | 125 | 38,40% | 0,71 | €-5,93 | 12,31% |
| TEST | Scanner Bottom5 Short Profit Lock V1 | Scanner Bottom 5 Short | €9.242,07 | €-756,47 | 62 | 62 | 30,65% | 0,56 | €-12,20 | 9,08% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.170,95 | €-827,60 | 89 | 89 | 31,46% | 0,64 | €-9,30 | 10,17% |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | Momentum / breakout | €9.165,52 | €-834,48 | 95 | 95 | 41,05% | 0,72 | €-8,78 | 12,64% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €9.150,69 | €-849,31 | 121 | 121 | 36,36% | 0,69 | €-7,02 | 13,99% |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | Scanner Top 5 + forza BTC | €9.142,42 | €-917,95 | 86 | 86 | 36,05% | 0,63 | €-10,67 | 9,10% |
| TEST | 1H Fast V3 Cap75 V1 | Momentum / breakout V3 Filtered | €9.106,22 | €-893,78 | 136 | 136 | 36,03% | 0,75 | €-6,57 | 14,10% |
| TEST | Combo Adaptive Mfe Trail | Combo Adaptive | €9.072,48 | €-899,77 | 160 | 160 | 41,25% | 0,72 | €-5,62 | 15,45% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €8.967,07 | €-1.032,93 | 47 | 47 | 36,17% | 0,47 | €-21,98 | 12,56% |
| TEST | Combo Adaptive Runner25 V1 | Combo Adaptive | €8.964,11 | €-1.035,89 | 94 | 94 | 30,85% | 0,53 | €-11,02 | 12,67% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €8.881,45 | €-1.088,76 | 56 | 56 | 26,79% | 0,56 | €-19,44 | 11,51% |
| TEST | Scanner Top5 Btc Btc Le3 V1 | Scanner Top 5 + forza BTC | €8.864,81 | €-1.151,44 | 72 | 72 | 30,56% | 0,48 | €-15,99 | 13,50% |
| TEST | Combo Adaptive Tp3 V1 | Combo Adaptive | €8.796,64 | €-1.203,36 | 75 | 75 | 29,33% | 0,38 | €-16,04 | 12,67% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €8.740,52 | €-1.259,48 | 81 | 81 | 38,27% | 0,55 | €-15,55 | 14,60% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €8.445,51 | €-1.554,49 | 105 | 105 | 27,62% | 0,47 | €-14,80 | 17,39% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | SPCX | LONG | Confluenza trend | 240m | 3,0x | 136,56189 | 136,56189 | 128,79610 | 91,72407 | 152,09346 | €285,50 | €856,50 | €48,71 | €0,00 |
| Principale 4H | VELVET | LONG | Confluenza trend | 240m | 3,0x | 0,55987 | 0,55987 | 0,49269 | 0,37605 | 0,69424 | €131,08 | €393,24 | €47,19 | €0,00 |
| Principale 4H | EDEN | LONG | Confluenza trend | 240m | 3,0x | 0,06195 | 0,06195 | 0,05451 | 0,04161 | 0,07681 | €130,34 | €391,02 | €46,92 | €0,00 |
| Principale 4H | TRUMP | LONG | Confluenza trend | 240m | 3,0x | 2,46049 | 2,46049 | 2,16523 | 1,65263 | 3,05101 | €134,98 | €404,95 | €48,59 | €0,00 |
| Principale 4H | XRP | LONG | Confluenza trend | 240m | 3,0x | 1,46057 | 1,39828 | 1,30460 | 0,98102 | 1,77252 | €8,58 | €25,73 | €2,75 | €-1,10 |
| Principale 4H | HYPE | LONG | Confluenza trend | 240m | 3,0x | 78,87277 | 80,67500 | 73,04357 | 52,97621 | 90,53117 | €8,52 | €25,56 | €1,89 | €0,58 |
| 1H Balanced Long No Rhv V1 | SKHYNIX | LONG | Confluenza trend | 60m | 3,0x | 1214,11277 | 1254,35000 | 1170,18211 | 815,47908 | 1301,97411 | €413,43 | €1.240,28 | €44,88 | €41,10 |
| 1H Balanced Long No Rhv V1 | BOME | LONG | Confluenza trend | 60m | 3,0x | 0,00129 | 0,00129 | 0,00114 | 0,00087 | 0,00160 | €134,98 | €404,95 | €48,59 | €0,00 |
| 1H Balanced Long No Rhv V1 | TAO | LONG | Confluenza trend | 60m | 3,0x | 247,38947 | 247,38947 | 237,94346 | 166,16326 | 266,28148 | €428,20 | €1.284,61 | €49,05 | €0,00 |
| 1H Balanced Long No Rhv V1 | ETH | LONG | Confluenza trend | 60m | 3,0x | 2502,31036 | 2483,05000 | 2464,79465 | 1680,71846 | 2577,34176 | €1.075,18 | €3.225,54 | €48,36 | €-24,83 |
| 1H Balanced Long No Rhv V1 | HYPE | LONG | Confluenza trend | 60m | 3,0x | 82,20244 | 80,67500 | 79,78758 | 55,21264 | 87,03215 | €28,40 | €85,21 | €2,50 | €-1,58 |
| Bilanciata 1H V2 | SKHYNIX | LONG | Confluenza trend V2 | 60m | 3,0x | 1214,11277 | 1254,35000 | 1170,18211 | 815,47908 | 1301,97411 | €422,38 | €1.267,15 | €45,85 | €41,99 |
| Bilanciata 1H V2 | ETH | LONG | Confluenza trend V2 | 60m | 3,0x | 2502,31036 | 2483,05000 | 2464,79465 | 1680,71846 | 2577,34176 | €1.055,40 | €3.166,20 | €47,47 | €-24,37 |
| Bilanciata 1H V2 | SOL | LONG | Confluenza trend V2 | 60m | 3,0x | 100,22404 | 100,94900 | 97,91287 | 67,31715 | 104,84638 | €685,30 | €2.055,91 | €47,41 | €14,87 |
| Bilanciata 1H V3 Filtered | SKHYNIX | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1220,85412 | 1254,35000 | 1177,63561 | 820,00702 | 1307,29117 | €460,42 | €1.381,27 | €48,90 | €37,90 |
| Bilanciata 1H V3 Filtered | ZEC | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 807,93155 | 776,09000 | 737,89694 | 542,66069 | 948,00078 | €195,29 | €585,88 | €50,79 | €-23,09 |
| Bilanciata 1H V3 Filtered | XRP | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1,47399 | 1,39828 | 1,35380 | 0,99003 | 1,71438 | €205,84 | €617,51 | €50,35 | €-31,72 |
| Bilanciata 1H V3 Filtered | ADA | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,20238 | 0,20238 | 0,20803 | 0,26883 | 0,19107 | €19,31 | €57,92 | €1,62 | €-0,00 |
| Bilanciata 1H V3 Filtered | ETH | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 2502,31036 | 2483,05000 | 2464,79465 | 1680,71846 | 2577,34176 | €9,10 | €27,30 | €0,41 | €-0,21 |
| Bilanciata 1H V3 Filtered | SOL | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 100,22404 | 100,94900 | 97,91287 | 67,31715 | 104,84638 | €697,84 | €2.093,51 | €48,28 | €15,14 |
| 1H Fast Score 6 75 Cost Aware V1 | BTW | LONG | Momentum / breakout | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €8,91 | €26,72 | €3,13 | €0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00086 | 0,00146 | €215,92 | €647,76 | €57,03 | €0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | NEAR | LONG | Momentum / breakout | 60m | 3,0x | 2,08142 | 2,08142 | 2,02315 | 1,39802 | 2,16882 | €42,86 | €128,59 | €3,60 | €0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €157,13 | €471,39 | €56,57 | €-0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | ETH | LONG | Momentum / breakout | 60m | 3,0x | 2502,31036 | 2483,05000 | 2473,13147 | 1680,71846 | 2546,07867 | €1.587,89 | €4.763,66 | €55,55 | €-36,67 |
| 1H Fast Score 6 75 Cost Aware V1 | SOL | LONG | Momentum / breakout | 60m | 3,0x | 100,22404 | 100,94900 | 100,46539 | 67,31715 | 102,92041 | €853,08 | €2.559,25 | €0,00 | €18,51 |
| 1H Fast Nohigh Cap75 V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €139,29 | €417,86 | €50,14 | €-0,00 |
| 1H Fast Nohigh Cap75 V1 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €141,57 | €424,71 | €50,14 | €-0,00 |
| 1H Fast Nohigh Cap75 V1 | ADA | SHORT | Momentum / breakout | 60m | 3,0x | 0,20481 | 0,20481 | 0,20925 | 0,27205 | 0,19815 | €53,21 | €159,62 | €3,46 | €-0,00 |
| 1H Fast Nohigh Cap75 V1 | ETH | LONG | Momentum / breakout | 60m | 3,0x | 2502,31036 | 2483,05000 | 2473,13147 | 1680,71846 | 2546,07867 | €1.468,46 | €4.405,38 | €51,37 | €-33,91 |
| 1H Fast Nohigh Cap75 V1 | SOL | LONG | Momentum / breakout | 60m | 3,0x | 100,22404 | 100,94900 | 100,46539 | 67,31715 | 102,92041 | €12,71 | €38,12 | €0,00 | €0,28 |
| 1H Fast Nohigh Cap75 V1 | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 82,02040 | 80,67500 | 80,13051 | 55,09037 | 84,85524 | €8,75 | €26,25 | €0,60 | €-0,43 |
| 1H Fast Nohigh Cap75 V1 | SKHYNIX | LONG | Momentum / breakout | 60m | 3,0x | 1266,44941 | 1254,35000 | 1241,20633 | 850,63186 | 1304,31405 | €11,10 | €33,31 | €0,66 | €-0,32 |
| 1H Fast Nohigh Cap75 V1 | BTR | LONG | Momentum / breakout | 60m | 3,0x | 0,17284 | 0,17281 | 0,15210 | 0,11609 | 0,20396 | €133,32 | €399,96 | €48,00 | €-0,08 |
| 1H Fast Long Btc 1 3 Cap75 V1 | ETH | LONG | Momentum / breakout | 60m | 3,0x | 2502,31036 | 2483,05000 | 2473,13147 | 1680,71846 | 2546,07867 | €1.420,65 | €4.261,95 | €49,70 | €-32,80 |
| 1H Fast Long Btc 1 3 Cap75 V1 | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 82,20244 | 80,67500 | 80,32422 | 55,21264 | 85,01977 | €724,52 | €2.173,57 | €49,66 | €-40,39 |
| 1H Fast Long Btc 1 3 Cap75 V1 | SOL | LONG | Momentum / breakout | 60m | 3,0x | 101,66933 | 100,94900 | 99,72283 | 68,28790 | 104,58908 | €19,33 | €58,00 | €1,11 | €-0,41 |
| 1H Fast Long Btc 1 3 Cap75 V1 | SKHYNIX | LONG | Momentum / breakout | 60m | 3,0x | 1266,44941 | 1254,35000 | 1241,20633 | 850,63186 | 1304,31405 | €828,42 | €2.485,26 | €49,54 | €-23,74 |
| 1H Fast Long Btc 1 3 Cap75 V1 | BTR | LONG | Momentum / breakout | 60m | 3,0x | 0,17284 | 0,17281 | 0,15210 | 0,11609 | 0,20396 | €131,62 | €394,86 | €47,38 | €-0,08 |
| 1H Fast No Pepe V1 | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €172,22 | €516,67 | €49,86 | €0,00 |
| 1H Fast No Pepe V1 | TAO | LONG | Momentum / breakout | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €47,93 | €143,78 | €4,27 | €0,00 |
| 1H Fast No Pepe V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €136,27 | €408,80 | €49,06 | €-0,00 |
| 1H Fast No Pepe V1 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €9,48 | €28,43 | €3,41 | €-0,00 |
| 1H Fast No Pepe V1 | ETH | LONG | Momentum / breakout | 60m | 3,0x | 2502,31036 | 2483,05000 | 2473,13147 | 1680,71846 | 2546,07867 | €1.517,98 | €4.553,94 | €53,10 | €-35,05 |
| 1H Fast No Pepe V1 | SOL | LONG | Momentum / breakout | 60m | 3,0x | 100,22404 | 100,94900 | 100,46539 | 67,31715 | 102,92041 | €11,02 | €33,07 | €0,00 | €0,24 |
| 1H Fast No Pepe V1 | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 82,02040 | 80,67500 | 80,13051 | 55,09037 | 84,85524 | €9,11 | €27,32 | €0,63 | €-0,45 |
| 1H Fast No Pepe V1 | SKHYNIX | LONG | Momentum / breakout | 60m | 3,0x | 1266,44941 | 1254,35000 | 1241,20633 | 850,63186 | 1304,31405 | €11,54 | €34,62 | €0,69 | €-0,33 |
| 1H Fast No Pepe V1 | BTR | LONG | Momentum / breakout | 60m | 3,0x | 0,17284 | 0,17281 | 0,15210 | 0,11609 | 0,20396 | €139,94 | €419,82 | €50,38 | €-0,08 |
| 1H Fast Tp2 V1 | BTW | LONG | Momentum / breakout | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,56752 | €142,85 | €428,56 | €50,25 | €0,00 |
| 1H Fast Tp2 V1 | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00132 | 0,00132 | 0,00119 | 0,00088 | 0,00158 | €18,87 | €56,62 | €5,59 | €0,00 |
| 1H Fast Tp2 V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,17246 | 0,17246 | 0,17246 | 0,22908 | 0,13107 | €139,71 | €419,14 | €0,00 | €-0,00 |
| 1H Fast Tp2 V1 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03379 | €141,13 | €423,40 | €50,81 | €-0,00 |
| 1H Fast Tp2 V1 | ETH | LONG | Momentum / breakout | 60m | 3,0x | 2502,31036 | 2483,05000 | 2473,13147 | 1680,71846 | 2560,66812 | €1.344,34 | €4.033,01 | €47,03 | €-31,04 |
| 1H Fast Tp2 V1 | SOL | LONG | Momentum / breakout | 60m | 3,0x | 101,73634 | 100,94900 | 99,75933 | 68,33291 | 105,69037 | €8,89 | €26,67 | €0,52 | €-0,21 |
| Rapida 1H V2 | ETH | LONG | Momentum / breakout V2 | 60m | 3,0x | 2502,31036 | 2483,05000 | 2473,13147 | 1680,71846 | 2546,07867 | €1.447,56 | €4.342,69 | €50,64 | €-33,43 |
| Rapida 1H V2 | SOL | LONG | Momentum / breakout V2 | 60m | 3,0x | 100,22404 | 100,94900 | 100,46539 | 67,31715 | 102,92041 | €939,38 | €2.818,13 | €0,00 | €20,38 |
| Rapida 1H V3 Filtered | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €172,00 | €515,99 | €49,79 | €0,00 |
| Rapida 1H V3 Filtered | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €589,98 | €1.769,95 | €52,56 | €0,00 |
| Rapida 1H V3 Filtered | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €140,02 | €420,06 | €50,41 | €-0,00 |
| Rapida 1H V3 Filtered | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €16,99 | €50,96 | €6,11 | €-0,00 |
| Rapida 1H V3 Filtered | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2502,31036 | 2483,05000 | 2473,13147 | 1680,71846 | 2546,07867 | €1.391,13 | €4.173,39 | €48,66 | €-32,12 |
| 1H Fast V3 Nohigh V1 | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €131,05 | €393,14 | €47,18 | €-0,00 |
| 1H Fast V3 Nohigh V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €133,20 | €399,59 | €47,18 | €-0,00 |
| 1H Fast V3 Nohigh V1 | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,20238 | 0,20238 | 0,20677 | 0,26883 | 0,19578 | €27,66 | €82,98 | €1,80 | €-0,00 |
| 1H Fast V3 Nohigh V1 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2502,31036 | 2483,05000 | 2473,13147 | 1680,71846 | 2546,07867 | €1.372,20 | €4.116,59 | €48,00 | €-31,69 |
| 1H Fast V3 Nohigh V1 | SOL | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 101,66933 | 100,94900 | 99,72283 | 68,28790 | 104,58908 | €840,73 | €2.522,18 | €48,29 | €-17,87 |
| 1H Fast V3 Long Only V1 | BTW | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €126,57 | €379,72 | €44,52 | €0,00 |
| 1H Fast V3 Long Only V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00147 | €9,56 | €28,69 | €2,66 | €0,00 |
| 1H Fast V3 Long Only V1 | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €554,42 | €1.663,26 | €49,39 | €0,00 |
| 1H Fast V3 Long Only V1 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2502,31036 | 2483,05000 | 2473,13147 | 1680,71846 | 2546,07867 | €1.350,31 | €4.050,93 | €47,24 | €-31,18 |
| 1H Fast V3 Long Only V1 | SOL | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 101,66933 | 100,94900 | 99,72283 | 68,28790 | 104,58908 | €805,18 | €2.415,53 | €46,25 | €-17,11 |
| 1H Fast V3 Long Nohigh Cap75 V1 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2502,31036 | 2483,05000 | 2473,13147 | 1680,71846 | 2546,07867 | €1.352,71 | €4.058,14 | €47,32 | €-31,24 |
| 1H Fast V3 Long Nohigh Cap75 V1 | SOL | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 101,66933 | 100,94900 | 99,72283 | 68,28790 | 104,58908 | €829,01 | €2.487,02 | €47,62 | €-17,62 |
| 1H Fast V3 No Esports V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €169,36 | €508,09 | €49,03 | €0,00 |
| 1H Fast V3 No Esports V1 | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €27,04 | €81,13 | €2,41 | €0,00 |
| 1H Fast V3 No Esports V1 | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €133,96 | €401,88 | €48,23 | €-0,00 |
| 1H Fast V3 No Esports V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €129,73 | €389,20 | €46,70 | €-0,00 |
| 1H Fast V3 No Esports V1 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2502,31036 | 2483,05000 | 2473,13147 | 1680,71846 | 2546,07867 | €1.340,17 | €4.020,52 | €46,88 | €-30,95 |
| 1H Fast V3 No Esports Long Only V1 | BTW | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €132,94 | €398,81 | €46,76 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00147 | €10,06 | €30,18 | €2,80 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2502,31036 | 2483,05000 | 2473,13147 | 1680,71846 | 2546,07867 | €1.391,98 | €4.175,94 | €48,69 | €-32,14 |
| 1H Fast V3 No Esports Long Only V1 | SOL | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 101,66933 | 100,94900 | 99,72283 | 68,28790 | 104,58908 | €853,07 | €2.559,21 | €49,00 | €-18,13 |
| 1H Fast V3 No Esports Mfe Lock V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €173,11 | €519,32 | €50,11 | €0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €593,79 | €1.781,38 | €52,90 | €0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €140,93 | €422,78 | €50,73 | €-0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €17,09 | €51,28 | €6,15 | €-0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2502,31036 | 2483,05000 | 2473,13147 | 1680,71846 | 2546,07867 | €1.400,13 | €4.200,39 | €48,98 | €-32,33 |
| 1H Fast V3 No Esports Stress Guard V1 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2502,31036 | 2483,05000 | 2473,13147 | 1680,71846 | 2546,07867 | €1.371,88 | €4.115,65 | €47,99 | €-31,68 |
| 1H Fast V3 No Esports Stress Guard V1 | SOL | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 100,22404 | 100,94900 | 100,46539 | 67,31715 | 102,92041 | €940,56 | €2.821,68 | €0,00 | €20,41 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2502,31036 | 2483,05000 | 2473,13147 | 1680,71846 | 2546,07867 | €1.333,94 | €4.001,81 | €46,66 | €-30,80 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | SOL | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 101,66933 | 100,94900 | 99,72283 | 68,28790 | 104,58908 | €813,51 | €2.440,54 | €46,73 | €-17,29 |
| Ampia 4H | SPCX | LONG | Confluenza trend | 240m | 2,0x | 136,56189 | 136,56189 | 126,46637 | 68,96375 | 164,82935 | €323,86 | €647,73 | €47,88 | €0,00 |
| Ampia 4H | VELVET | LONG | Confluenza trend | 240m | 2,0x | 0,55987 | 0,55987 | 0,49269 | 0,28274 | 0,74799 | €201,63 | €403,26 | €48,39 | €0,00 |
| Ampia 4H | LINK | LONG | Confluenza trend | 240m | 2,0x | 11,96839 | 11,96839 | 11,08055 | 6,04404 | 14,45436 | €14,07 | €28,15 | €2,09 | €0,00 |
| Ampia 4H | ETH | LONG | Confluenza trend | 240m | 2,0x | 2430,03591 | 2483,05000 | 2267,54364 | 1227,16813 | 2885,01426 | €18,82 | €37,65 | €2,52 | €0,82 |
| Ampia 4H | HYPE | LONG | Confluenza trend | 240m | 2,0x | 79,31286 | 80,67500 | 70,73982 | 40,05299 | 103,31737 | €13,82 | €27,64 | €2,99 | €0,47 |
| Ampia 4H | TRUMP | LONG | Confluenza trend | 240m | 2,0x | 2,37347 | 2,37347 | 2,08866 | 1,19860 | 3,17096 | €210,83 | €421,66 | €50,60 | €0,00 |
| Ampia 4H | DOGE | SHORT | Confluenza trend | 240m | 2,0x | 0,08583 | 0,08649 | 0,09382 | 0,12832 | 0,06346 | €274,53 | €549,07 | €51,10 | €-4,20 |
| Forza relativa 1H V2 | BEAT | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,25984 | 0,25984 | 0,25657 | 0,38847 | 0,19125 | €200,38 | €400,75 | €0,00 | €-0,00 |
| Forza relativa 1H V2 | TUT | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,04452 | 0,04452 | 0,04986 | 0,06656 | 0,03277 | €204,64 | €409,28 | €49,11 | €-0,00 |
| Forza relativa 1H V2 | ADA | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,20989 | 0,20989 | 0,20756 | 0,31379 | 0,19609 | €816,97 | €1.633,95 | €0,00 | €-0,00 |
| Forza relativa 1H V2 | SOL | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 100,68813 | 100,94900 | 98,15309 | 50,84751 | 106,26524 | €966,11 | €1.932,23 | €48,65 | €5,01 |
| Benchmark Donchian breakout 1H | SKHYNIX | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1174,33482 | 1254,35000 | 1128,44989 | 593,03908 | 1289,04713 | €641,25 | €1.282,50 | €50,11 | €87,39 |
| Benchmark Donchian breakout 1H | VELVET | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,14787 | 0,14787 | 0,16561 | 0,22107 | 0,10351 | €237,23 | €474,47 | €56,94 | €-0,00 |
| Benchmark Donchian breakout 1H | DOGE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,08603 | 0,08649 | 0,08867 | 0,12862 | 0,07943 | €921,23 | €1.842,45 | €56,55 | €-9,79 |
| Benchmark Donchian breakout 1H | ETH | LONG | Donchian breakout 20 barre | 60m | 2,0x | 2502,31036 | 2483,05000 | 2460,62625 | 1263,66673 | 2606,52065 | €42,45 | €84,89 | €1,41 | €-0,65 |
| Benchmark Donchian breakout 1H | SOL | LONG | Donchian breakout 20 barre | 60m | 2,0x | 101,66933 | 100,94900 | 98,88861 | 51,34301 | 108,62113 | €1.034,66 | €2.069,32 | €56,60 | €-14,66 |
| Benchmark Donchian breakout 1H | BTR | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,15358 | 0,17281 | 0,15358 | 0,07756 | 0,19965 | €17,34 | €34,68 | €0,00 | €4,34 |
| Donchian 1H Gb20 120R V1 | SKHYNIX | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1174,33482 | 1254,35000 | 1128,44989 | 593,03908 | 1289,04713 | €626,15 | €1.252,30 | €48,93 | €85,33 |
| Donchian 1H Gb20 120R V1 | VELVET | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,14787 | 0,14787 | 0,16561 | 0,22107 | 0,10351 | €231,65 | €463,30 | €55,60 | €-0,00 |
| Donchian 1H Gb20 120R V1 | DOGE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,08603 | 0,08649 | 0,08867 | 0,12862 | 0,07943 | €899,54 | €1.799,07 | €55,22 | €-9,56 |
| Donchian 1H Gb20 120R V1 | ETH | LONG | Donchian breakout 20 barre | 60m | 2,0x | 2502,31036 | 2483,05000 | 2460,62625 | 1263,66673 | 2606,52065 | €41,45 | €82,89 | €1,38 | €-0,64 |
| Donchian 1H Gb20 120R V1 | SOL | LONG | Donchian breakout 20 barre | 60m | 2,0x | 101,66933 | 100,94900 | 98,88861 | 51,34301 | 108,62113 | €1.010,30 | €2.020,60 | €55,26 | €-14,32 |
| Donchian 1H Gb20 120R V1 | BTR | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,15358 | 0,17281 | 0,15358 | 0,07756 | 0,19965 | €16,93 | €33,86 | €0,00 | €4,24 |
| Benchmark trend following EMA 1H | BEAT | SHORT | Trend following EMA | 60m | 2,0x | 0,28257 | 0,28257 | 0,25706 | 0,42244 | 0,20797 | €186,11 | €372,23 | €0,00 | €-0,00 |
| Benchmark trend following EMA 1H | ZEC | LONG | Trend following EMA | 60m | 2,0x | 807,93155 | 776,09000 | 730,11531 | 408,00543 | 979,12728 | €17,42 | €34,84 | €3,36 | €-1,37 |
| Benchmark trend following EMA 1H | TUT | SHORT | Trend following EMA | 60m | 2,0x | 0,04446 | 0,04446 | 0,04980 | 0,06647 | 0,03272 | €194,70 | €389,39 | €46,73 | €-0,00 |
| Benchmark trend following EMA 1H | VELVET | SHORT | Trend following EMA | 60m | 2,0x | 0,14786 | 0,14786 | 0,16560 | 0,22105 | 0,10883 | €187,91 | €375,83 | €45,10 | €-0,00 |
| Benchmark trend following EMA 1H | ADA | SHORT | Trend following EMA | 60m | 2,0x | 0,20989 | 0,20989 | 0,21687 | 0,31379 | 0,19455 | €681,63 | €1.363,26 | €45,30 | €-0,00 |
| Scanner Top 5 Long 1H | BOME | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00160 | €218,24 | €436,47 | €52,38 | €0,00 |
| Scanner Top 5 Long 1H | TRUMP | LONG | Scanner Top 5 Long | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,08367 | €238,89 | €477,78 | €55,13 | €0,00 |
| Scanner Top 5 Long 1H | ETH | LONG | Scanner Top 5 Long | 60m | 2,0x | 2502,31036 | 2483,05000 | 2464,79465 | 1263,66673 | 2577,34176 | €1.811,62 | €3.623,23 | €54,32 | €-27,89 |
| Scanner Top 5 Long 1H | SOL | LONG | Scanner Top 5 Long | 60m | 2,0x | 100,22404 | 100,94900 | 97,91287 | 50,61314 | 104,84638 | €1.176,11 | €2.352,22 | €54,24 | €17,01 |
| Scanner Top 5 Long 1H | SKHYNIX | LONG | Scanner Top 5 Long | 60m | 2,0x | 1266,44941 | 1254,35000 | 1233,99401 | 639,55695 | 1331,36020 | €17,74 | €35,49 | €0,91 | €-0,34 |
| Scanner Bottom 5 Short 1H | SOXL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €378,86 | €757,72 | €48,07 | €-0,00 |
| Scanner Bottom 5 Short 1H | SNDK | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €492,80 | €985,60 | €47,71 | €-0,00 |
| Scanner Bottom 5 Short 1H | VELVET | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €191,07 | €382,14 | €0,00 | €-0,00 |
| Scanner Bottom 5 Short 1H | TUT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €178,38 | €356,76 | €42,81 | €-0,00 |
| Scanner Top10 Long | TAO | LONG | Scanner Top10 Long | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €678,43 | €1.356,86 | €51,81 | €0,00 |
| Scanner Top10 Long | ETH | LONG | Scanner Top10 Long | 60m | 2,0x | 2502,31036 | 2483,05000 | 2464,79465 | 1263,66673 | 2577,34176 | €1.685,15 | €3.370,31 | €50,53 | €-25,94 |
| Scanner Top10 Long | SOL | LONG | Scanner Top10 Long | 60m | 2,0x | 100,22404 | 100,94900 | 97,91287 | 50,61314 | 104,84638 | €1.094,01 | €2.188,02 | €50,46 | €15,83 |
| Scanner Top10 Long | SKHYNIX | LONG | Scanner Top10 Long | 60m | 2,0x | 1270,86206 | 1254,35000 | 1239,26059 | 641,78534 | 1334,06500 | €972,86 | €1.945,72 | €48,38 | €-25,28 |
| Scanner Bottom10 Short | SOXL | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom10 Short | SNDK | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Bottom10 Short | VELVET | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €194,19 | €388,38 | €0,00 | €-0,00 |
| Scanner Bottom10 Short | TUT | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €181,31 | €362,61 | €43,51 | €-0,00 |
| Scanner Top15 Long | NEAR | LONG | Scanner Top15 Long | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €16,79 | €33,59 | €1,21 | €0,00 |
| Scanner Top15 Long | TAO | LONG | Scanner Top15 Long | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €88,53 | €177,07 | €6,76 | €0,00 |
| Scanner Top15 Long | TRUMP | LONG | Scanner Top15 Long | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,08367 | €215,87 | €431,75 | €49,81 | €0,00 |
| Scanner Top15 Long | ETH | LONG | Scanner Top15 Long | 60m | 2,0x | 2502,31036 | 2483,05000 | 2464,79465 | 1263,66673 | 2577,34176 | €1.627,80 | €3.255,61 | €48,81 | €-25,06 |
| Scanner Top15 Long | SOL | LONG | Scanner Top15 Long | 60m | 2,0x | 100,22404 | 100,94900 | 97,91287 | 50,61314 | 104,84638 | €1.056,78 | €2.113,56 | €48,74 | €15,29 |
| Scanner Top15 Long | SKHYNIX | LONG | Scanner Top15 Long | 60m | 2,0x | 1270,86206 | 1254,35000 | 1239,26059 | 641,78534 | 1334,06500 | €787,36 | €1.574,72 | €39,16 | €-20,46 |
| Scanner Bottom15 Short | SOXL | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom15 Short | SNDK | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Bottom15 Short | VELVET | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €194,19 | €388,38 | €0,00 | €-0,00 |
| Scanner Bottom15 Short | TUT | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €181,31 | €362,61 | €43,51 | €-0,00 |
| Scanner Top20 Long | NEAR | LONG | Scanner Top20 Long | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €16,79 | €33,59 | €1,21 | €0,00 |
| Scanner Top20 Long | TAO | LONG | Scanner Top20 Long | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €88,53 | €177,07 | €6,76 | €0,00 |
| Scanner Top20 Long | TRUMP | LONG | Scanner Top20 Long | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,08367 | €215,87 | €431,75 | €49,81 | €0,00 |
| Scanner Top20 Long | ETH | LONG | Scanner Top20 Long | 60m | 2,0x | 2502,31036 | 2483,05000 | 2464,79465 | 1263,66673 | 2577,34176 | €1.627,80 | €3.255,61 | €48,81 | €-25,06 |
| Scanner Top20 Long | SOL | LONG | Scanner Top20 Long | 60m | 2,0x | 100,22404 | 100,94900 | 97,91287 | 50,61314 | 104,84638 | €1.056,78 | €2.113,56 | €48,74 | €15,29 |
| Scanner Top20 Long | SKHYNIX | LONG | Scanner Top20 Long | 60m | 2,0x | 1270,86206 | 1254,35000 | 1239,26059 | 641,78534 | 1334,06500 | €787,36 | €1.574,72 | €39,16 | €-20,46 |
| Scanner Bottom20 Short | SOXL | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom20 Short | SNDK | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Bottom20 Short | VELVET | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €194,19 | €388,38 | €0,00 | €-0,00 |
| Scanner Bottom20 Short | TUT | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €181,31 | €362,61 | €43,51 | €-0,00 |
| Scanner Top 5 + forza BTC 1H | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €203,45 | €406,91 | €48,83 | €0,00 |
| Scanner Top 5 + forza BTC 1H | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,14149 | €223,03 | €446,06 | €51,47 | €0,00 |
| Scanner Top 5 + forza BTC 1H | ETH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2502,31036 | 2483,05000 | 2464,79465 | 1263,66673 | 2584,84492 | €1.690,50 | €3.381,00 | €50,69 | €-26,02 |
| Scanner Top 5 + forza BTC 1H | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 100,22404 | 100,94900 | 97,91287 | 50,61314 | 105,30861 | €1.092,06 | €2.184,13 | €50,37 | €15,80 |
| Scanner Top 5 + forza BTC 1H | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1254,35000 | 1233,99401 | 639,55695 | 1337,85129 | €18,23 | €36,45 | €0,93 | €-0,35 |
| Scanner Top5 Btc Mfe V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €190,73 | €381,46 | €45,77 | €0,00 |
| Scanner Top5 Btc Mfe V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,14149 | €209,08 | €418,16 | €48,25 | €0,00 |
| Scanner Top5 Btc Mfe V1 | ETH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2502,31036 | 2483,05000 | 2464,79465 | 1263,66673 | 2584,84492 | €1.584,76 | €3.169,52 | €47,52 | €-24,40 |
| Scanner Top5 Btc Mfe V1 | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 100,22404 | 100,94900 | 97,91287 | 50,61314 | 105,30861 | €1.023,76 | €2.047,51 | €47,22 | €14,81 |
| Scanner Top5 Btc Mfe V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1254,35000 | 1233,99401 | 639,55695 | 1337,85129 | €17,09 | €34,17 | €0,88 | €-0,33 |
| Scanner Top5 Btc Guard V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €197,27 | €394,55 | €47,35 | €0,00 |
| Scanner Top5 Btc Guard V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,55551 | 2,55551 | 2,29388 | 1,29053 | 3,13109 | €13,03 | €26,06 | €2,67 | €0,00 |
| Scanner Top5 Btc Guard V1 | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 100,22404 | 100,94900 | 97,91287 | 50,61314 | 105,30861 | €1.040,01 | €2.080,02 | €47,97 | €15,05 |
| Scanner Top5 Btc Guard V1 | BTR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15358 | 0,17281 | 0,15358 | 0,07756 | 0,19413 | €199,12 | €398,24 | €0,00 | €49,86 |
| Scanner Top5 Btc Btc Le3 V1 | ETH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2502,31036 | 2483,05000 | 2464,79465 | 1263,66673 | 2584,84492 | €1.498,78 | €2.997,56 | €44,94 | €-23,07 |
| Scanner Top5 Btc Btc Le3 V1 | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 100,22404 | 100,94900 | 97,91287 | 50,61314 | 105,30861 | €968,21 | €1.936,42 | €44,65 | €14,01 |
| Scanner Top5 Btc Btc Le3 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1254,35000 | 1233,99401 | 639,55695 | 1337,85129 | €847,75 | €1.695,49 | €43,45 | €-16,20 |
| Scanner Top5 Btc Btc Le3 V1 | BTR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15358 | 0,17281 | 0,15358 | 0,07756 | 0,19413 | €182,51 | €365,03 | €0,00 | €45,70 |
| Scanner Top5 Btc Btc 2 3 V1 | ETH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2502,31036 | 2483,05000 | 2464,79465 | 1263,66673 | 2584,84492 | €1.575,75 | €3.151,50 | €47,25 | €-24,26 |
| Scanner Top5 Btc Btc 2 3 V1 | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 100,22404 | 100,94900 | 97,91287 | 50,61314 | 105,30861 | €1.017,93 | €2.035,86 | €46,95 | €14,73 |
| Scanner Top5 Btc Btc 2 3 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1254,35000 | 1233,99401 | 639,55695 | 1337,85129 | €891,28 | €1.782,56 | €45,68 | €-17,03 |
| Scanner Top5 Btc Btc 2 3 V1 | BTR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15358 | 0,17281 | 0,15358 | 0,07756 | 0,19413 | €191,89 | €383,78 | €0,00 | €48,05 |
| Scanner Top5 Btc Guard Mfe V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €192,69 | €385,37 | €46,24 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,55551 | 2,55551 | 2,29388 | 1,29053 | 3,13109 | €12,72 | €25,45 | €2,61 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 100,22404 | 100,94900 | 97,91287 | 50,61314 | 105,30861 | €1.015,82 | €2.031,64 | €46,85 | €14,70 |
| Scanner Top5 Btc Guard Mfe V1 | BTR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15358 | 0,17281 | 0,15358 | 0,07756 | 0,19413 | €194,49 | €388,97 | €0,00 | €48,70 |
| Scanner Top5 Btc Guard Btc Le3 V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,55551 | 2,55551 | 2,29388 | 1,29053 | 3,13109 | €12,70 | €25,40 | €2,60 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 100,22404 | 100,94900 | 97,91287 | 50,61314 | 105,30861 | €1.007,54 | €2.015,09 | €46,47 | €14,58 |
| Scanner Top5 Btc Guard Btc Le3 V1 | BTR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15358 | 0,17281 | 0,15358 | 0,07756 | 0,19413 | €192,90 | €385,80 | €0,00 | €48,31 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 100,22404 | 100,94900 | 97,91287 | 50,61314 | 105,30861 | €989,99 | €1.979,97 | €45,66 | €14,32 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | BTR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15358 | 0,17281 | 0,15358 | 0,07756 | 0,19413 | €189,54 | €379,08 | €0,00 | €47,46 |
| Scanner Top5 Btc Runner25 V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00176 | €210,95 | €421,90 | €50,63 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | ETH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2502,31036 | 2483,05000 | 2464,79465 | 1263,66673 | 2614,85748 | €1.689,83 | €3.379,66 | €50,67 | €-26,01 |
| Scanner Top5 Btc Runner25 V1 | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 100,22404 | 100,94900 | 97,91287 | 50,61314 | 107,15755 | €1.091,63 | €2.183,26 | €50,35 | €15,79 |
| Scanner Top5 Btc Runner25 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1254,35000 | 1233,99401 | 639,55695 | 1363,81560 | €965,52 | €1.931,04 | €49,49 | €-18,45 |
| Scanner Top5 Btc Tp3 V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00176 | €211,07 | €422,14 | €50,66 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | ETH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2502,31036 | 2483,05000 | 2464,79465 | 1263,66673 | 2614,85748 | €1.690,82 | €3.381,63 | €50,70 | €-26,03 |
| Scanner Top5 Btc Tp3 V1 | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 100,22404 | 100,94900 | 97,91287 | 50,61314 | 107,15755 | €1.092,27 | €2.184,54 | €50,38 | €15,80 |
| Scanner Top5 Btc Tp3 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1254,35000 | 1233,99401 | 639,55695 | 1363,81560 | €966,09 | €1.932,17 | €49,52 | €-18,46 |
| Combo Trend | BEAT | SHORT | Combo Trend | 60m | 2,0x | 0,25984 | 0,25984 | 0,25657 | 0,38847 | 0,19125 | €193,71 | €387,42 | €0,00 | €-0,00 |
| Combo Trend | ZEC | LONG | Combo Trend | 60m | 2,0x | 807,93155 | 776,09000 | 730,11531 | 408,00543 | 979,12728 | €247,61 | €495,23 | €47,70 | €-19,52 |
| Combo Trend | DOGE | SHORT | Combo Trend | 60m | 2,0x | 0,08663 | 0,08649 | 0,08935 | 0,12952 | 0,08067 | €744,01 | €1.488,02 | €46,59 | €2,45 |
| Combo Trend | ADA | SHORT | Combo Trend | 60m | 2,0x | 0,20238 | 0,20238 | 0,20866 | 0,30256 | 0,18856 | €29,18 | €58,37 | €1,81 | €-0,00 |
| Combo Trend | ETH | LONG | Combo Trend | 60m | 2,0x | 2502,31036 | 2483,05000 | 2460,62625 | 1263,66673 | 2594,01541 | €1.342,29 | €2.684,59 | €44,72 | €-20,66 |
| Combo Scanner | BOME | LONG | Combo Scanner | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €195,20 | €390,40 | €46,85 | €0,00 |
| Combo Scanner | TRUMP | LONG | Combo Scanner | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,14149 | €213,98 | €427,96 | €49,38 | €0,00 |
| Combo Scanner | ETH | LONG | Combo Scanner | 60m | 2,0x | 2502,31036 | 2483,05000 | 2464,79465 | 1263,66673 | 2584,84492 | €1.616,25 | €3.232,50 | €48,46 | €-24,88 |
| Combo Scanner | SOL | LONG | Combo Scanner | 60m | 2,0x | 100,22404 | 100,94900 | 97,91287 | 50,61314 | 105,30861 | €1.049,28 | €2.098,56 | €48,39 | €15,18 |
| Combo Scanner | SKHYNIX | LONG | Combo Scanner | 60m | 2,0x | 1266,44941 | 1254,35000 | 1233,99401 | 639,55695 | 1337,85129 | €24,78 | €49,55 | €1,27 | €-0,47 |
| Combo Adaptive | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,01735 | 121,01735 | 128,90956 | 180,92093 | 105,23292 | €367,30 | €734,61 | €47,91 | €-0,00 |
| Combo Adaptive | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €40,89 | €81,77 | €3,12 | €0,00 |
| Combo Adaptive | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 807,93155 | 776,09000 | 737,89694 | 408,00543 | 948,00078 | €307,94 | €615,88 | €53,39 | €-24,27 |
| Combo Adaptive | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,52450 | 2,33981 | 1,27487 | 2,89389 | €18,69 | €37,37 | €2,73 | €0,00 |
| Combo Adaptive | ADA | SHORT | Combo Adaptive | 60m | 2,0x | 0,20238 | 0,20238 | 0,20803 | 0,30256 | 0,19107 | €40,31 | €80,63 | €2,25 | €-0,00 |
| Combo Adaptive | ETH | LONG | Combo Adaptive | 60m | 2,0x | 2493,43859 | 2483,05000 | 2455,39522 | 1259,18649 | 2569,52529 | €1.704,48 | €3.408,96 | €52,01 | €-14,20 |
| Combo Adaptive | SOL | LONG | Combo Adaptive | 60m | 2,0x | 101,73634 | 100,94900 | 99,19447 | 51,37685 | 106,82009 | €1.020,15 | €2.040,31 | €50,98 | €-15,79 |
| Combo Adaptive Mfe Trail | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €54,29 | €108,58 | €4,15 | €0,00 |
| Combo Adaptive Mfe Trail | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,52450 | 2,33981 | 1,27487 | 2,89389 | €315,75 | €631,50 | €46,20 | €0,00 |
| Combo Adaptive Mfe Trail | TUT | SHORT | Combo Adaptive | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €190,04 | €380,09 | €45,61 | €-0,00 |
| Combo Adaptive Mfe Trail | ADA | SHORT | Combo Adaptive | 60m | 2,0x | 0,20238 | 0,20238 | 0,20803 | 0,30256 | 0,19107 | €40,65 | €81,31 | €2,27 | €-0,00 |
| Combo Adaptive Mfe Trail | ETH | LONG | Combo Adaptive | 60m | 2,0x | 2493,43859 | 2483,05000 | 2455,39522 | 1259,18649 | 2569,52529 | €1.465,62 | €2.931,24 | €44,72 | €-12,21 |
| Combo Adaptive Mfe Trail | SOL | LONG | Combo Adaptive | 60m | 2,0x | 101,73634 | 100,94900 | 99,19447 | 51,37685 | 106,82009 | €784,07 | €1.568,13 | €39,18 | €-12,14 |
| Combo Adaptive Quality7 V1 | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €371,68 | €743,36 | €47,16 | €-0,00 |
| Combo Adaptive Quality7 V1 | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €646,78 | €1.293,57 | €49,39 | €0,00 |
| Combo Adaptive Quality7 V1 | ADA | SHORT | Combo Adaptive | 60m | 2,0x | 0,20238 | 0,20238 | 0,20803 | 0,30256 | 0,19107 | €876,38 | €1.752,76 | €48,96 | €-0,00 |
| Combo Adaptive Regime V1 | ETH | LONG | Combo Adaptive | 60m | 2,0x | 2502,31036 | 2483,05000 | 2464,79465 | 1263,66673 | 2577,34176 | €1.636,31 | €3.272,61 | €49,06 | €-25,19 |
| Combo Adaptive Regime V1 | SOL | LONG | Combo Adaptive | 60m | 2,0x | 101,16923 | 100,94900 | 98,67777 | 51,09046 | 106,15214 | €996,83 | €1.993,65 | €49,10 | €-4,34 |
| Combo Adaptive Regime V1 | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1270,86206 | 1254,35000 | 1239,26059 | 641,78534 | 1334,06500 | €987,06 | €1.974,12 | €49,09 | €-25,65 |
| Combo Adaptive Regime V1 | BTR | LONG | Combo Adaptive | 60m | 2,0x | 0,15358 | 0,17281 | 0,15358 | 0,07756 | 0,19044 | €203,07 | €406,14 | €0,00 | €50,85 |
| Combo Adaptive Long Only V1 | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €645,48 | €1.290,95 | €46,47 | €0,00 |
| Combo Adaptive Long Only V1 | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,52450 | 2,33981 | 1,27487 | 2,89389 | €48,12 | €96,24 | €7,04 | €0,00 |
| Combo Adaptive Long Only V1 | ETH | LONG | Combo Adaptive | 60m | 2,0x | 2502,31036 | 2483,05000 | 2464,79465 | 1263,66673 | 2577,34176 | €1.728,09 | €3.456,18 | €51,82 | €-26,60 |
| Combo Adaptive Long Only V1 | SOL | LONG | Combo Adaptive | 60m | 2,0x | 100,22404 | 100,94900 | 97,91287 | 50,61314 | 104,84638 | €1.121,89 | €2.243,77 | €51,74 | €16,23 |
| Combo Adaptive Long Only V1 | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1266,44941 | 1254,35000 | 1233,99401 | 639,55695 | 1331,36020 | €968,99 | €1.937,97 | €49,66 | €-18,52 |
| Combo Adaptive Partial 1R V1 | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,01735 | 121,01735 | 128,90956 | 180,92093 | 105,23292 | €352,70 | €705,40 | €46,00 | €-0,00 |
| Combo Adaptive Partial 1R V1 | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,52450 | 2,33981 | 1,27487 | 2,89389 | €347,19 | €694,38 | €50,80 | €0,00 |
| Combo Adaptive Partial 1R V1 | VELVET | SHORT | Combo Adaptive | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €207,76 | €415,52 | €0,00 | €-0,00 |
| Combo Adaptive Partial 1R V1 | ADA | SHORT | Combo Adaptive | 60m | 2,0x | 0,20989 | 0,20989 | 0,20688 | 0,31379 | 0,19734 | €18,50 | €37,00 | €0,00 | €-0,00 |
| Combo Adaptive Partial 1R V1 | ETH | LONG | Combo Adaptive | 60m | 2,0x | 2502,31036 | 2483,05000 | 2464,79465 | 1263,66673 | 2577,34176 | €27,02 | €54,03 | €0,81 | €-0,42 |
| Combo Adaptive Partial 1R V1 | SOL | LONG | Combo Adaptive | 60m | 2,0x | 100,22404 | 100,94900 | 97,91287 | 50,61314 | 104,84638 | €47,32 | €94,64 | €2,18 | €0,68 |
| Combo Adaptive Partial 1R V1 | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1270,86206 | 1254,35000 | 1239,26059 | 641,78534 | 1334,06500 | €1.013,20 | €2.026,40 | €50,39 | €-26,33 |
| Btc Ema 4H | BTC | LONG | Trend following EMA | 240m | 2,0x | 80355,23783 | 78648,03000 | 77497,66656 | 40579,39511 | 87499,16561 | €704,37 | €1.408,74 | €50,10 | €-29,93 |
| Btc Donchian 4H | BTC | LONG | Donchian breakout 20 barre | 240m | 2,0x | 80355,23783 | 78648,03000 | 77497,66656 | 40579,39511 | 88356,43707 | €700,60 | €1.401,20 | €49,83 | €-29,77 |
| Btc Bollinger 4H | BTC | SHORT | Bollinger mean reversion | 240m | 2,0x | 80323,10217 | 78648,03000 | 82919,85488 | 120083,03774 | 75648,94663 | €775,58 | €1.551,16 | €50,15 | €32,35 |
| Btc Adaptive 4H | BTC | LONG | Combo Adaptive | 240m | 2,0x | 80355,23783 | 78648,03000 | 77237,88772 | 40579,39511 | 88148,61352 | €648,94 | €1.297,88 | €50,35 | €-27,57 |
| Sol Ema 1H | SOL | LONG | Trend following EMA | 60m | 3,0x | 100,22404 | 100,94900 | 97,91287 | 67,31715 | 104,84638 | €728,87 | €2.186,61 | €50,42 | €15,82 |
| Sol Ema 4H | SOL | LONG | Trend following EMA | 240m | 2,0x | 98,32066 | 100,94900 | 92,06715 | 49,65193 | 113,95442 | €395,27 | €790,53 | €50,28 | €21,13 |
| Sol Donchian 1H | SOL | LONG | Donchian breakout 20 barre | 60m | 3,0x | 100,22404 | 100,94900 | 100,46539 | 67,31715 | 104,33279 | €828,76 | €2.486,27 | €0,00 | €17,98 |
| Sol Bollinger 1H | SOL | SHORT | Bollinger mean reversion | 60m | 3,0x | 101,62867 | 100,94900 | 103,71338 | 134,99675 | 98,50161 | €797,97 | €2.393,90 | €49,11 | €16,01 |
| Sol Bollinger 4H | SOL | SHORT | Bollinger mean reversion | 240m | 2,0x | 100,13097 | 100,94900 | 105,86849 | 149,69580 | 89,80342 | €435,50 | €871,00 | €49,91 | €-7,12 |
| Sol Adaptive 1H | SOL | LONG | Combo Adaptive | 60m | 3,0x | 100,22404 | 100,94900 | 97,91287 | 67,31715 | 104,84638 | €718,50 | €2.155,51 | €49,71 | €15,59 |
| Sol Adaptive 4H | SOL | LONG | Combo Adaptive | 240m | 2,0x | 98,32066 | 100,94900 | 91,49865 | 49,65193 | 115,37567 | €367,30 | €734,59 | €50,97 | €19,64 |
| Eth Ema 1H | ETH | LONG | Trend following EMA | 60m | 3,0x | 2493,43859 | 2483,05000 | 2455,39522 | 1674,75958 | 2569,52529 | €1.072,00 | €3.216,01 | €49,07 | €-13,40 |
| Eth Ema 4H | ETH | LONG | Trend following EMA | 240m | 2,0x | 2390,02791 | 2483,05000 | 2268,60778 | 1206,96409 | 2693,57826 | €487,73 | €975,47 | €49,56 | €37,97 |
| Eth Donchian 1H | ETH | LONG | Donchian breakout 20 barre | 60m | 3,0x | 2502,31036 | 2483,05000 | 2468,96307 | 1680,71846 | 2569,00494 | €1.210,37 | €3.631,11 | €48,39 | €-27,95 |
| Eth Adaptive 1H | ETH | LONG | Combo Adaptive | 60m | 3,0x | 2502,31036 | 2483,05000 | 2464,79465 | 1680,71846 | 2577,34176 | €1.094,40 | €3.283,20 | €49,22 | €-25,27 |
| Master Adaptive V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 80,35907 | 80,67500 | 78,17754 | 40,58133 | 84,72212 | €858,86 | €1.717,73 | €46,63 | €6,75 |
| Master Adaptive V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 2502,31036 | 2483,05000 | 2464,79465 | 1263,66673 | 2577,34181 | €1.560,29 | €3.120,58 | €46,79 | €-24,02 |
| Master Adaptive V1 | SOL | LONG | Master Adaptive Consensus | 60m | 2,0x | 100,68813 | 100,94900 | 98,15309 | 50,84751 | 105,75823 | €912,62 | €1.825,23 | €45,95 | €4,73 |
| Master Adaptive V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1254,35000 | 1233,99403 | 639,55695 | 1331,36019 | €22,75 | €45,50 | €1,17 | €-0,43 |
| Master Adaptive V1 | BTR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,17284 | 0,17281 | 0,15210 | 0,08729 | 0,21433 | €195,60 | €391,20 | €46,94 | €-0,08 |
| Master Adaptive No Alt V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 80,35907 | 80,67500 | 78,17754 | 40,58133 | 84,72212 | €861,47 | €1.722,94 | €46,77 | €6,77 |
| Master Adaptive No Alt V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 2502,31036 | 2483,05000 | 2464,79465 | 1263,66673 | 2577,34181 | €1.565,03 | €3.130,05 | €46,93 | €-24,09 |
| Master Adaptive No Alt V1 | BTR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,14959 | 0,17281 | 0,13164 | 0,07554 | 0,18549 | €195,68 | €391,35 | €46,96 | €60,75 |
| Master Adaptive No Alt V1 | SOL | LONG | Master Adaptive Consensus | 60m | 2,0x | 101,16923 | 100,94900 | 98,67777 | 51,09046 | 106,15214 | €953,46 | €1.906,91 | €46,96 | €-4,15 |
| Master Adaptive No Alt V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1255,10261 | 1254,35000 | 1225,12158 | 633,82682 | 1315,06467 | €19,09 | €38,19 | €0,91 | €-0,02 |
| Master Adaptive Strict3 V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 2502,31036 | 2483,05000 | 2464,79465 | 1263,66673 | 2577,34181 | €1.493,28 | €2.986,56 | €44,78 | €-22,99 |
| Master Adaptive Strict3 V1 | SOL | LONG | Master Adaptive Consensus | 60m | 2,0x | 101,16923 | 100,94900 | 98,67777 | 51,09046 | 106,15214 | €903,35 | €1.806,70 | €44,49 | €-3,93 |
| Master Adaptive Expanded V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03814 | 0,02188 | 0,05374 | €197,50 | €395,01 | €47,40 | €0,00 |
| Master Adaptive Expanded V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 80,35907 | 80,67500 | 78,17754 | 40,58133 | 84,72212 | €861,38 | €1.722,77 | €46,77 | €6,77 |
| Master Adaptive Expanded V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 2502,31036 | 2483,05000 | 2464,79465 | 1263,66673 | 2577,34181 | €1.572,67 | €3.145,34 | €47,16 | €-24,21 |
| Master Adaptive Expanded V1 | SOL | LONG | Master Adaptive Consensus | 60m | 2,0x | 101,73634 | 100,94900 | 99,19447 | 51,37685 | 106,82009 | €15,99 | €31,99 | €0,80 | €-0,25 |
| Master Adaptive Expanded V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1261,89668 | 1254,35000 | 1231,08309 | 637,25783 | 1323,52387 | €934,21 | €1.868,43 | €45,62 | €-11,17 |
| Master Adaptive Gb20 V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 80,35907 | 80,67500 | 78,17754 | 40,58133 | 84,72212 | €847,45 | €1.694,91 | €46,01 | €6,66 |
| Master Adaptive Gb20 V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 2502,31036 | 2483,05000 | 2464,79465 | 1263,66673 | 2577,34181 | €1.539,56 | €3.079,12 | €46,16 | €-23,70 |
| Master Adaptive Gb20 V1 | SOL | LONG | Master Adaptive Consensus | 60m | 2,0x | 100,68813 | 100,94900 | 98,15309 | 50,84751 | 105,75823 | €900,49 | €1.800,98 | €45,34 | €4,67 |
| Master Adaptive Gb20 V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1254,35000 | 1233,99403 | 639,55695 | 1331,36019 | €22,45 | €44,90 | €1,15 | €-0,43 |
| Master Adaptive Gb20 V1 | BTR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,17284 | 0,17281 | 0,15210 | 0,08729 | 0,21433 | €193,00 | €386,00 | €46,32 | €-0,08 |
| Master Adaptive Runner25 V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03814 | 0,02188 | 0,05894 | €34,77 | €69,54 | €8,34 | €0,00 |
| Master Adaptive Runner25 V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 80,35907 | 80,67500 | 78,17754 | 40,58133 | 86,90364 | €864,19 | €1.728,38 | €46,92 | €6,80 |
| Master Adaptive Runner25 V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 2502,31036 | 2483,05000 | 2464,79465 | 1263,66673 | 2614,85753 | €1.568,97 | €3.137,94 | €47,05 | €-24,15 |
| Master Adaptive Runner25 V1 | SOL | LONG | Master Adaptive Consensus | 60m | 2,0x | 98,42868 | 100,94900 | 96,44960 | 49,70648 | 104,36592 | €964,43 | €1.928,85 | €38,78 | €49,39 |
| Master Adaptive Runner25 V1 | BTR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,13218 | 0,17281 | 0,11632 | 0,06675 | 0,17976 | €196,14 | €392,29 | €47,07 | €120,60 |
| Master Adaptive Runner25 V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1255,10261 | 1254,35000 | 1225,12158 | 633,82682 | 1345,04570 | €27,05 | €54,10 | €1,29 | €-0,03 |
| Combo Adaptive Side Regime Guard V1 | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €77,52 | €155,04 | €5,58 | €0,00 |
| Combo Adaptive Side Regime Guard V1 | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 807,93155 | 776,09000 | 737,89694 | 408,00543 | 948,00078 | €305,89 | €611,78 | €53,03 | €-24,11 |
| Combo Adaptive Side Regime Guard V1 | VELVET | SHORT | Combo Adaptive | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €216,61 | €433,23 | €0,00 | €-0,00 |
| Combo Adaptive Side Regime Guard V1 | TUT | SHORT | Combo Adaptive | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €192,40 | €384,79 | €46,18 | €-0,00 |
| Combo Adaptive Side Regime Guard V1 | ETH | LONG | Combo Adaptive | 60m | 2,0x | 2502,31036 | 2483,05000 | 2464,79465 | 1263,66673 | 2577,34176 | €1.697,78 | €3.395,56 | €50,91 | €-26,14 |
| Master Adaptive Gb20 Be V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 80,35907 | 80,67500 | 78,17754 | 40,58133 | 84,72212 | €863,12 | €1.726,23 | €46,86 | €6,79 |
| Master Adaptive Gb20 Be V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 2502,31036 | 2483,05000 | 2464,79465 | 1263,66673 | 2577,34181 | €1.568,02 | €3.136,03 | €47,02 | €-24,14 |
| Master Adaptive Gb20 Be V1 | SOL | LONG | Master Adaptive Consensus | 60m | 2,0x | 100,68813 | 100,94900 | 98,15309 | 50,84751 | 105,75823 | €917,13 | €1.834,27 | €46,18 | €4,75 |
| Master Adaptive Gb20 Be V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1254,35000 | 1233,99403 | 639,55695 | 1331,36019 | €22,86 | €45,73 | €1,17 | €-0,44 |
| Master Adaptive Gb20 Be V1 | BTR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,17284 | 0,17281 | 0,15210 | 0,08729 | 0,21433 | €196,57 | €393,14 | €47,18 | €-0,08 |
| Master Adaptive Gb20 Partial V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 80,35907 | 80,67500 | 78,17754 | 40,58133 | 84,72212 | €862,20 | €1.724,40 | €46,81 | €6,78 |
| Master Adaptive Gb20 Partial V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 2502,31036 | 2483,05000 | 2464,79465 | 1263,66673 | 2577,34181 | €1.566,35 | €3.132,70 | €46,97 | €-24,11 |
| Master Adaptive Gb20 Partial V1 | SOL | LONG | Master Adaptive Consensus | 60m | 2,0x | 100,68813 | 100,94900 | 98,15309 | 50,84751 | 105,75823 | €916,16 | €1.832,32 | €46,13 | €4,75 |
| Master Adaptive Gb20 Partial V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1254,35000 | 1233,99403 | 639,55695 | 1331,36019 | €22,84 | €45,68 | €1,17 | €-0,44 |
| Master Adaptive Gb20 Partial V1 | BTR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,17284 | 0,17281 | 0,15210 | 0,08729 | 0,21433 | €196,36 | €392,72 | €47,13 | €-0,08 |
| Master Adaptive Gb20 Loss Cap V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03828 | 0,02188 | 0,05682 | €195,70 | €391,41 | €45,67 | €0,00 |
| Master Adaptive Gb20 Loss Cap V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 2502,31036 | 2483,05000 | 2474,17356 | 1263,66673 | 2577,34181 | €1.829,31 | €3.658,61 | €41,14 | €-28,16 |
| Master Adaptive Gb20 Loss Cap V1 | SOL | LONG | Master Adaptive Consensus | 60m | 2,0x | 100,68813 | 100,94900 | 98,78685 | 50,84751 | 105,75823 | €1.211,09 | €2.422,17 | €45,74 | €6,28 |
| Master Adaptive Gb20 Loss Cap V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1254,35000 | 1242,10788 | 639,55695 | 1331,36019 | €140,55 | €281,10 | €5,40 | €-2,69 |
| 1H Fast V3 Nohigh Regime Guard V1 | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €140,84 | €422,53 | €50,70 | €-0,00 |
| 1H Fast V3 Nohigh Regime Guard V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €143,15 | €429,46 | €50,70 | €-0,00 |
| 1H Fast V3 Nohigh Regime Guard V1 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2502,31036 | 2483,05000 | 2473,13147 | 1680,71846 | 2546,07867 | €1.442,59 | €4.327,77 | €50,47 | €-33,31 |
| 1H Fast V3 Nohigh Regime Guard V1 | SOL | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 100,22404 | 100,94900 | 100,46539 | 67,31715 | 102,92041 | €952,40 | €2.857,19 | €0,00 | €20,67 |
| Main Side Regime Guard V1 | VELVET | LONG | Confluenza trend | 240m | 3,0x | 0,55987 | 0,55987 | 0,49269 | 0,37605 | 0,69424 | €142,25 | €426,74 | €51,21 | €0,00 |
| Main Side Regime Guard V1 | AKE | LONG | Confluenza trend | 240m | 3,0x | 0,01021 | 0,01021 | 0,00899 | 0,00686 | 0,01266 | €145,97 | €437,90 | €52,55 | €0,00 |
| Main Side Regime Guard V1 | HYPE | LONG | Confluenza trend | 240m | 3,0x | 77,65853 | 80,67500 | 71,20755 | 52,16065 | 90,56048 | €216,52 | €649,56 | €53,96 | €25,23 |
| Main Side Regime Guard V1 | XRP | LONG | Confluenza trend | 240m | 3,0x | 1,47102 | 1,39828 | 1,31178 | 0,98804 | 1,78951 | €12,77 | €38,31 | €4,15 | €-1,89 |
| Main Side Regime Guard V1 | ETH | LONG | Confluenza trend | 240m | 3,0x | 2437,91749 | 2483,05000 | 2326,72117 | 1637,46791 | 2660,31012 | €9,94 | €29,83 | €1,36 | €0,55 |
| Main Side Regime Guard V1 | BTR | LONG | Confluenza trend | 240m | 3,0x | 0,15358 | 0,17281 | 0,15358 | 0,10316 | 0,19044 | €144,94 | €434,83 | €0,00 | €54,44 |
| Combo Trend Side Regime Guard V1 | VELVET | SHORT | Combo Trend | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,12693 | €217,86 | €435,73 | €0,00 | €-0,00 |
| Combo Trend Side Regime Guard V1 | TUT | SHORT | Combo Trend | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03364 | €12,81 | €25,62 | €3,07 | €-0,00 |
| Combo Trend Side Regime Guard V1 | DOGE | SHORT | Combo Trend | 60m | 2,0x | 0,08663 | 0,08649 | 0,08935 | 0,12952 | 0,08067 | €881,95 | €1.763,89 | €55,22 | €2,90 |
| Combo Trend Side Regime Guard V1 | ETH | LONG | Combo Trend | 60m | 2,0x | 2502,31036 | 2483,05000 | 2460,62625 | 1263,66673 | 2594,01541 | €1.662,43 | €3.324,85 | €55,39 | €-25,59 |
| Combo Trend Side Regime Guard V1 | SOL | LONG | Combo Trend | 60m | 2,0x | 100,22404 | 100,94900 | 97,65607 | 50,61314 | 105,87357 | €1.052,06 | €2.104,12 | €53,91 | €15,22 |
| 1H Fast Nohigh Cap75 Short Only V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €135,82 | €407,46 | €48,90 | €-0,00 |
| 1H Fast Nohigh Cap75 Short Only V1 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €138,05 | €414,14 | €48,89 | €-0,00 |
| 1H Fast Nohigh Cap75 Short Only V1 | ADA | SHORT | Momentum / breakout | 60m | 3,0x | 0,20481 | 0,20481 | 0,20925 | 0,27205 | 0,19815 | €51,88 | €155,65 | €3,37 | €-0,00 |
| 1H Fast Nohigh Cap75 Short Only V1 | ETH | LONG | Momentum / breakout | 60m | 3,0x | 2502,31036 | 2483,05000 | 2473,13147 | 1680,71846 | 2546,07867 | €1.431,92 | €4.295,75 | €50,09 | €-33,06 |
| 1H Fast Nohigh Cap75 Short Only V1 | SOL | LONG | Momentum / breakout | 60m | 3,0x | 100,22404 | 100,94900 | 100,46539 | 67,31715 | 102,92041 | €12,39 | €37,17 | €0,00 | €0,27 |
| 1H Fast Nohigh Cap75 Short Only V1 | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 82,02040 | 80,67500 | 80,13051 | 55,09037 | 84,85524 | €8,53 | €25,60 | €0,59 | €-0,42 |
| 1H Fast Nohigh Cap75 Short Only V1 | SKHYNIX | LONG | Momentum / breakout | 60m | 3,0x | 1266,44941 | 1254,35000 | 1241,20633 | 850,63186 | 1304,31405 | €10,83 | €32,48 | €0,65 | €-0,31 |
| 1H Fast Nohigh Cap75 Short Only V1 | BTR | LONG | Momentum / breakout | 60m | 3,0x | 0,17284 | 0,17281 | 0,15210 | 0,11609 | 0,20396 | €130,00 | €390,01 | €46,80 | €-0,08 |
| 1H Balanced V3 Long Only V1 | SKHYNIX | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1220,85412 | 1254,35000 | 1177,63561 | 820,00702 | 1307,29117 | €435,49 | €1.306,46 | €46,25 | €35,84 |
| 1H Balanced V3 Long Only V1 | ZEC | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 807,93155 | 776,09000 | 737,89694 | 542,66069 | 948,00078 | €184,72 | €554,15 | €48,04 | €-21,84 |
| 1H Balanced V3 Long Only V1 | XRP | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1,47399 | 1,39828 | 1,35380 | 0,99003 | 1,71438 | €194,69 | €584,07 | €47,63 | €-30,00 |
| 1H Balanced V3 Long Only V1 | DOGE | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,08603 | 0,08649 | 0,08841 | 0,11428 | 0,08128 | €18,32 | €54,97 | €1,52 | €-0,29 |
| 1H Balanced V3 Long Only V1 | ETH | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 2502,31036 | 2483,05000 | 2464,79465 | 1680,71846 | 2577,34176 | €17,97 | €53,92 | €0,81 | €-0,42 |
| 1H Balanced V3 Long Only V1 | SOL | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 100,22404 | 100,94900 | 97,91287 | 67,31715 | 104,84638 | €654,36 | €1.963,07 | €45,27 | €14,20 |
| Scanner Bottom5 Short Profit Lock V1 | SOXL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €381,80 | €763,60 | €48,45 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | SNDK | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €496,62 | €993,25 | €48,08 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | VELVET | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €192,55 | €385,10 | €0,00 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | TUT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €179,76 | €359,53 | €43,14 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | SOXL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €382,38 | €764,76 | €48,52 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | SNDK | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €497,38 | €994,76 | €48,15 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | VELVET | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €192,85 | €385,69 | €0,00 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | TUT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €180,04 | €360,08 | €43,21 | €-0,00 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Master Adaptive Gb20 Loss Cap V1 | BTR | LONG | 2026-08-27T04:45:00+00:00 | 0,17444 | €122,19 | 2,65 | TARGET |
| Master Adaptive V1 | BTR | LONG | 2026-08-27T03:15:00+00:00 | 0,16387 | €93,29 | 1,99 | TARGET |
| Master Adaptive Gb20 V1 | BTR | LONG | 2026-08-27T03:15:00+00:00 | 0,16387 | €92,05 | 1,99 | TARGET |
| Master Adaptive Gb20 Partial V1 | BTR | LONG | 2026-08-27T03:15:00+00:00 | 0,16387 | €93,65 | 1,99 | TARGET |
| Master Adaptive Gb20 Be V1 | BTR | LONG | 2026-08-27T03:15:00+00:00 | 0,16387 | €93,75 | 1,99 | TARGET |
| Master Adaptive Expanded V1 | BTR | LONG | 2026-08-27T03:15:00+00:00 | 0,16292 | €89,05 | 1,99 | TARGET |
| 1H Fast V3 No Esports Long Only V1 | BTR | LONG | 2026-08-27T03:15:00+00:00 | 0,15504 | €71,31 | 1,49 | TARGET |
| 1H Fast V3 Long Nohigh Cap75 V1 | BTR | LONG | 2026-08-27T03:15:00+00:00 | 0,15504 | €70,53 | 1,49 | TARGET |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | BTR | LONG | 2026-08-27T03:15:00+00:00 | 0,15504 | €69,21 | 1,49 | TARGET |
| 1H Fast No Pepe V1 | BTR | LONG | 2026-08-27T03:15:00+00:00 | 0,15504 | €74,21 | 1,49 | TARGET |
| 1H Fast Nohigh Cap75 V1 | BTR | LONG | 2026-08-27T03:15:00+00:00 | 0,15504 | €70,71 | 1,49 | TARGET |
| 1H Fast Nohigh Cap75 Short Only V1 | BTR | LONG | 2026-08-27T03:15:00+00:00 | 0,15504 | €68,96 | 1,49 | TARGET |

## Regole invarianti

- Nessuna martingala e nessuna mediazione automatica in perdita.
- Il target mensile riduce il rischio quando viene avvicinato o raggiunto; non lo aumenta mai.
- Il portafoglio principale e le simulazioni di confronto hanno contabilità separata.
- Commissioni, slippage e funding sono inclusi nella simulazione secondo i parametri configurati.
- Quando stop e target risultano toccati nella stessa candela, prevale lo stop salvo modifica esplicita della configurazione.
